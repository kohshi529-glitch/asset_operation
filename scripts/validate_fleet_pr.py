#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fleet PR validator — 夜間・朝のルーティンが出す PR を、正典の厳守条項に照らして機械検証する。
使い方: python3 scripts/validate_fleet_pr.py --base <sha> --head <sha> --title "<PR title>" [--branch <head ref>] [--author <login>]
終了コード 0 = 合格（自動マージしてよい）、1 = 不合格（理由を stdout に出す。人の判断に回す）、2 = 対象外（手動運用の PR）。
依存: 標準ライブラリのみ。git は subprocess で呼ぶ（fetch-depth 0 で checkout されていること）。
"""
import argparse, json, re, subprocess, sys, fnmatch

OWNER = "kohshi529-glitch"

# 接頭辞ごとの許可表。正典の厳守条項（変更してよいキー・ファイル）と 2026-10 までの実績から転記。
# files: 触ってよいファイル（glob）。keys: master.json のトップレベルで変えてよいキー。
# cand: candidates.* で変えてよい子キー。runs: pipeline.runs.* で変えてよい子キー。
# max_lines: master.json の変更行数（追加＋削除）の上限（実績最大の約1.5倍。異常なふくらみの検知用。書式破壊は別途「往復一致」で見る）。
POLICY = {
  "night-gate":   dict(files=["master.json","grades.json","pool_bars.json","night_gate_today.json","night_gate_board.md","gate_history/*.json","earnings_calendar.json"],
                       keys={"night_gate","gyoseki_cache","valuation_cache","profile_cache","earnings_log","rights_cache","pipeline"},
                       cand=set(), runs={"night_gate"}, max_lines=70000),
  "nightly ①-S1": dict(files=["master.json"], keys={"candidates","pipeline"}, cand={"kenmo_momentum","kenmo_newhigh"}, runs={"kenmo_momentum","kenmo_newhigh"}, max_lines=1000),
  "nightly ①-S2": dict(files=["master.json"], keys={"candidates","pipeline","theme_watch"},
                       cand={"choruko_reversal","granville_tenkan","granville_oshime","granville_rebound"}, runs={"choruko_reversal","granville_night"}, max_lines=7000),
  "cpwatch":      dict(files=["master.json"], keys={"changepoint_watch","pipeline"}, cand=set(), runs={"changepoint_watch"}, max_lines=12000),
  "watch ①-12":   dict(files=["master.json"], keys={"watchlist","pipeline"}, cand=set(), runs={"watch_tracker"}, max_lines=12000),
  "ai-scan":      dict(files=["master.json","ai_scan_today.json"], keys={"candidates","ai_scan","pipeline"}, cand={"ai_momentum","ai_reversal"}, runs={"ai_scan"}, max_lines=1000),
  "morning ⑤":    dict(files=["master.json","market_today.json"], keys={"market","pipeline"}, cand=set(), runs={"morning_compass"}, max_lines=500),
  "eval":         dict(files=["master.json"], keys={"gyoseki_cache","valuation_cache","night_gate","pipeline"}, cand=set(), runs={"gyoseki_update"}, max_lines=40000),
  "ipo":          dict(files=["master.json"], keys={"ipo","catalyst_schedule","pipeline"}, cand=set(), runs={"ipo"}, max_lines=1000),
  "surge-log":    dict(files=["surge_log.json"], keys=set(), cand=set(), runs=set(), max_lines=0),
  "earn-stats":   dict(files=["earnings_stats.json"], keys=set(), cand=set(), runs=set(), max_lines=0),
  "kpi-company":  dict(files=["kpi_series.json"], keys=set(), cand=set(), runs=set(), max_lines=0),
  "gate-track":   dict(files=["gate_track.json"], keys=set(), cand=set(), runs=set(), max_lines=0),
  "stf":          dict(files=["master.json"], keys={"candidates","stf_log","pipeline"}, cand={"stf_kakuhen"}, runs={"stf_weekly"}, max_lines=10000),
}
# 派生ファイルのサイズ上限（暴走検知用。2026-10-11 実測: grades 385KB・pool_bars 352KB・night_gate_today 74KB・gate_history 516KB／日・gate_track 1.9MB・surge_log 80KB の約 1.5〜2 倍）。
# 2026-10-19: earnings_calendar.json（①-8 v1.43 の派生ファイル・次回決算日と過去の発表日。初回実測 86KB・889 銘柄）を night-gate の許可ファイルに追加。上限 300KB。
# 2026-10-20: R-C 決算反応統計（接頭辞 earn-stats・週次）が書く earnings_stats.json を追加。master.json は書かない（max_lines=0）。上限 300KB。
# 2026-10-21: R-B 決算 KPI 取込（接頭辞 kpi-company・火〜土 06:00）が書く kpi_series.json を追加。master.json は書かない。上限 1MB。
# 正典側の上限（①-8 V13(d) の grades 350KB 等）は正典の自己検証に委ね、ここでは「桁違い」だけを止める。無いものは上限なし（JSON として読めればよい）。
SIZE_CAPS = {"grades.json": 700_000, "pool_bars.json": 700_000, "earnings_calendar.json": 300_000, "earnings_stats.json": 300_000, "kpi_series.json": 1_000_000, "market_today.json": 50_000, "ai_scan_today.json": 200_000, "night_gate_today.json": 300_000, "gate_track.json": 4_000_000, "surge_log.json": 500_000}
GATE_HISTORY_CAP = 1_200_000

def git(*a):
    return subprocess.run(["git", *a], capture_output=True, text=True, check=True).stdout

def show(ref, path):
    r = subprocess.run(["git", "show", f"{ref}:{path}"], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None

def detect_indent(raw):
    try: obj = json.loads(raw)
    except Exception: return None, None
    body = raw.rstrip("\n")  # 末尾改行の有無は書式破壊とみなさない（ルーティンにより付く／付かないが混在。差分は 1 行）
    for w in (1, 2, 4):
        if json.dumps(obj, ensure_ascii=False, indent=w) == body: return w, obj
    return None, obj

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True); ap.add_argument("--head", required=True); ap.add_argument("--title", required=True)
    ap.add_argument("--branch", default=""); ap.add_argument("--author", default="")
    a = ap.parse_args()
    fails = []; notes = []

    # 0) 対象判定（手動運用のものは 2 で抜ける）
    pre = None
    for p in POLICY:
        if a.title.startswith(p + ":") or a.title.startswith(p + "："):
            pre = p; break
    if pre is None:
        print(f"SKIP: 接頭辞が許可表に無い（手動運用）: {a.title[:60]}"); return 2
    if a.branch and not a.branch.startswith("claude/"):
        print(f"SKIP: head ブランチが claude/ で始まらない（手動運用）: {a.branch}"); return 2
    if a.author and a.author != OWNER:
        fails.append(f"PR 作者が {OWNER} ではない: {a.author}")
    pol = POLICY[pre]

    # 1) 変更ファイルの許可
    numstat = git("diff", "--numstat", a.base, a.head)
    changed = {}
    for line in numstat.splitlines():
        p = line.split("\t")
        if len(p) == 3: changed[p[2]] = (p[0], p[1])
    if not changed: fails.append("変更ファイルがない")
    for f in changed:
        if not any(fnmatch.fnmatch(f, g) for g in pol["files"]):
            fails.append(f"許可外のファイルを変更: {f}（{pre} が触ってよいのは {pol['files']}）")
    for f in changed:
        if f.startswith(".github/") or f in ("board.html","index.html","system.html","gate_history.html"):
            fails.append(f"ワークフロー／ボードの変更は自動マージ対象外: {f}")

    # 2) gate_history は新規作成のみ・ファイル名は日付
    for f in changed:
        if f.startswith("gate_history/"):
            if show(a.base, f) is not None: fails.append(f"既存の gate_history を書き換えている: {f}（作成後不変）")
            if not re.fullmatch(r"gate_history/\d{4}-\d{2}-\d{2}\.json", f): fails.append(f"gate_history のファイル名が日付でない: {f}")

    # 3) master.json: 行数・往復一致・キー
    if "master.json" in changed:
        add, dele = changed["master.json"]
        lines = (int(add) if add.isdigit() else 0) + (int(dele) if dele.isdigit() else 0)
        if pol["max_lines"] == 0: fails.append(f"{pre} は master.json を変更しない規則だが変更している（{lines} 行）")
        elif lines > pol["max_lines"]: fails.append(f"master.json の変更行数 {lines} が上限 {pol['max_lines']} を超えている（全体再フォーマットの疑い）")
        raw_b = show(a.base, "master.json"); raw_h = show(a.head, "master.json")
        wb, ob = detect_indent(raw_b or ""); wh, oh = detect_indent(raw_h or "")
        if oh is None: fails.append("head の master.json が JSON として読めない")
        if wh is None and oh is not None: fails.append("head の master.json が json.dumps(indent=1/2/4) のどれとも往復一致しない（書式破壊）")
        if wb is not None and wh is not None and wb != wh: fails.append(f"master.json のインデント幅が変わっている（base {wb} → head {wh}）")
        if ob is not None and oh is not None:
            for k in set(ob) | set(oh):
                if ob.get(k) != oh.get(k) and k not in pol["keys"]:
                    fails.append(f"許可外のトップレベルキーを変更: {k}（{pre} が変えてよいのは {sorted(pol['keys'])}）")
            if "candidates" in pol["keys"]:
                cb = ob.get("candidates") or {}; ch = oh.get("candidates") or {}
                for ck in set(cb) | set(ch):
                    if cb.get(ck) != ch.get(ck) and ck not in pol["cand"]:
                        fails.append(f"許可外の candidates.{ck} を変更（{pre} は {sorted(pol['cand'])} のみ）")
            if "pipeline" in pol["keys"]:
                pb = (ob.get("pipeline") or {}); ph = (oh.get("pipeline") or {})
                for pk in set(pb) | set(ph):
                    if pk != "runs" and pb.get(pk) != ph.get(pk): fails.append(f"pipeline.{pk} を変更している（runs 以外は不可）")
                rb = pb.get("runs") or {}; rh = ph.get("runs") or {}
                for rk in set(rb) | set(rh):
                    if rb.get(rk) != rh.get(rk) and rk not in pol["runs"]:
                        fails.append(f"許可外の pipeline.runs.{rk} を変更（{pre} は {sorted(pol['runs'])} のみ）")
            notes.append(f"master.json: {lines} 行変更・indent={wh}・変更キー {sorted(k for k in set(ob)|set(oh) if ob.get(k)!=oh.get(k))}")

    # 4) 他の JSON: パースとサイズ上限
    for f in changed:
        if f.endswith(".json") and f != "master.json":
            raw = show(a.head, f)
            if raw is None: notes.append(f"{f}: 削除"); continue
            try: json.loads(raw)
            except Exception as e: fails.append(f"{f} が JSON として読めない: {e}")
            cap = SIZE_CAPS.get(f) or (GATE_HISTORY_CAP if f.startswith("gate_history/") else None)
            if cap and len(raw.encode("utf-8")) > cap: fails.append(f"{f} が上限 {cap} バイトを超えている（{len(raw.encode('utf-8'))}）")

    print(f"PREFIX: {pre}")
    for n in notes: print("NOTE:", n)
    if fails:
        print("FAIL:"); [print(" -", x) for x in fails]; return 1
    print("PASS"); return 0

if __name__ == "__main__":
    sys.exit(main())
