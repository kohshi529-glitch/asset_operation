#!/usr/bin/env python3
# master.json（リポジトリ唯一の正）から、公開ページ docs/index.html を生成する。
# 使い方: リポジトリ直下で  python3 scripts/render_master.py
# master.json を編集 → 本スクリプトで再生成 → commit/push。
import json, html, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = json.load(open(os.path.join(ROOT, "master.json"), encoding="utf-8"))["scoring_spec"]

def esc(x): return html.escape(str(x))

# ---- 検証：completeメソッドの点数上限合計=21 ----
for mid, m in spec["methods"].items():
    if m.get("status") != "complete":
        print(f"[skip] {m['name']}: {m.get('status')}", file=sys.stderr); continue
    tot = sum(it["max"] for it in m["items"])
    print(f"[{'OK' if tot==spec['common']['max_score'] else '★NG★'}] {m['name']}: {tot}/{spec['common']['max_score']}", file=sys.stderr)

BG="#0d1b1e"; CARD="#12292e"; ACCENT="#1fb6a6"; ACCENT2="#7fe3d6"; TXT="#e6f4f1"; SUB="#8fb3ad"; BORDER="#1d3a40"
grade_color={"◎":"#1fb6a6","○":"#4a9d92","△":"#c9a24a","✗":"#a05252","維持":"#4a9d92"}

def item_block(it):
    axis=f"<span class='axis'>{esc(it['axis'])}</span>" if it.get("axis") else ""
    rows="".join(f"<tr><td class='gr' style='color:{grade_color.get(g['grade'],'#4a9d92')}'>{esc(g['grade'])}</td><td class='pt'>{esc(g['points'])}点</td><td>{esc(g['criteria'])}</td></tr>" for g in it["grades"])
    note=f"<div class='note'>💡 {esc(it['note'])}</div>" if it.get("note") else ""
    return f"<div class='item'><div class='ihead'><span class='ino'>{esc(it['no'])}</span> {esc(it['name'])} <span class='imax'>最大{esc(it['max'])}点</span>{axis}</div><table class='gtab'><tbody>{rows}</tbody></table>{note}</div>"

def method_section(mid,m):
    pending=m.get("status")!="complete"
    banner=("<div class='pending'>⚠ 実数基準が未着（取得不可）。枠のみ。</div>" if pending else "")
    if m.get("notice"): banner+=f"<div class='notice'>ⓘ {esc(m['notice'])}</div>"
    screen=""
    if m.get("screening"):
        rows="".join(f"<tr><td class='sl'>{esc(c['label'])}</td><td>{esc(c['value'])}</td></tr>" for c in m['screening']['conditions'])
        screen=f"<div class='sub'>スクリーニング事前条件</div><div class='snote'>{esc(m['screening'].get('note',''))}</div><table class='stab'><tbody>{rows}</tbody></table>"
    elif m.get("screening_note"):
        screen=f"<div class='sub'>スクリーニング事前条件</div><div class='snote muted'>{esc(m['screening_note'])}</div>"
    items="<div class='sub'>スコアリング項目</div>"+"".join(item_block(it) for it in m["items"]) if m.get("items") else ""
    ths=""
    if m.get("thresholds"):
        rows="".join(f"<tr><td class='rng'>{esc(t['range'])}点</td><td class='vd'>{esc(t['verdict'])}</td><td><span class='act act-{t['action']}'>{esc(t['action'])}</span></td><td class='mng'>{esc(t.get('meaning',''))}</td></tr>" for t in m["thresholds"])
        ths=f"<div class='sub'>判定閾値（5段階）</div><table class='ttab'><thead><tr><th>合計点</th><th>判定</th><th>アクション</th><th>意味</th></tr></thead><tbody>{rows}</tbody></table>"
    ops=""
    if m.get("operation"):
        ops="<div class='sub'>運用ルール</div><ul class='ops'>"+"".join(f"<li>{esc(x)}</li>" for x in m["operation"])+"</ul>"
    elif m.get("operation_note"):
        ops=f"<div class='sub'>運用ルール</div><div class='snote muted'>{esc(m['operation_note'])}</div>"
    weak=""
    if m.get("weak_models"):
        rows="".join(f"<tr><td>{esc(w['model'])}</td><td>{esc(w['reason'])}</td><td class='alt'>{esc(w['alt'])}</td></tr>" for w in m["weak_models"])
        weak=f"<div class='sub'>苦手なビジネスモデル（他手法推奨）</div><table class='wtab'><thead><tr><th>モデル</th><th>理由</th><th>代替手法</th></tr></thead><tbody>{rows}</tbody></table>"
    st="pending" if pending else "ok"
    return f"<section class='method {st}' id='{esc(mid)}'><div class='mhead'><span class='emoji'>{esc(m.get('emoji',''))}</span><span class='mname'>{esc(m['name'])}</span><span class='sess'>{esc(m.get('session',''))}</span></div><div class='phil'>{esc(m['philosophy'])}</div>{banner}{screen}{items}{ths}{ops}{weak}</section>"

nav="".join(f"<a href='#{esc(mid)}'>{esc(m.get('emoji',''))} {esc(m['name'])}</a>" for mid,m in spec["methods"].items())
sections="".join(method_section(mid,m) for mid,m in spec["methods"].items())
common=spec["common"]
gp="　".join(f"{k}={v}点" for k,v in common["grade_points"].items())
acts="".join(f"<tr><td><span class='act act-{k}'>{esc(k)}</span></td><td>{esc(v)}</td></tr>" for k,v in common["actions"].items())

out=f"""<!doctype html><html lang='ja'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>
<title>5大手法 スコアリング基準マスター</title><style>
:root{{color-scheme:dark}}*{{box-sizing:border-box}}
body{{margin:0;background:{BG};color:{TXT};font-family:-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif;line-height:1.6}}
.wrap{{max-width:920px;margin:0 auto;padding:20px 16px 80px}}h1{{font-size:22px;margin:8px 0 4px}}
.ver{{color:{SUB};font-size:13px;margin-bottom:16px}}
.lead{{background:{CARD};border:1px solid {BORDER};border-radius:12px;padding:14px 16px;color:{ACCENT2};font-size:14px;margin-bottom:18px}}
.nav{{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:22px}}
.nav a{{background:{CARD};border:1px solid {BORDER};color:{TXT};text-decoration:none;padding:7px 12px;border-radius:999px;font-size:13px}}
.tabs{{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:18px}}
.tabs a{{background:{CARD};border:1px solid {BORDER};color:{TXT};text-decoration:none;padding:7px 12px;border-radius:999px;font-size:13px}}
.tabs a.here{{border-color:{ACCENT};color:{ACCENT2}}}
.common{{background:{CARD};border:1px solid {BORDER};border-radius:12px;padding:14px 16px;margin-bottom:22px}}
.common .gp{{font-size:15px;color:{ACCENT2};margin-bottom:10px}}
section.method{{background:{CARD};border:1px solid {BORDER};border-left:4px solid {ACCENT};border-radius:12px;padding:16px 16px 6px;margin-bottom:20px}}
section.method.pending{{border-left-color:#c9a24a}}
.mhead{{display:flex;align-items:center;gap:10px;margin-bottom:6px}}.emoji{{font-size:20px}}.mname{{font-size:19px;font-weight:700}}
.sess{{margin-left:auto;font-size:12px;color:{SUB};border:1px solid {BORDER};padding:2px 8px;border-radius:6px}}
.phil{{font-size:13.5px;color:{SUB};margin-bottom:12px}}
.pending{{background:#2a2410;border:1px solid #5c4a1e;color:#e8c766;padding:10px 12px;border-radius:8px;font-size:13px;margin-bottom:12px}}
.notice{{background:#0f2429;border:1px solid {BORDER};color:{SUB};padding:10px 12px;border-radius:8px;font-size:12.5px;margin-bottom:12px}}
.sub{{font-weight:700;color:{ACCENT2};font-size:14px;margin:16px 0 8px;border-bottom:1px solid {BORDER};padding-bottom:4px}}
.snote{{font-size:13px;margin-bottom:8px}}.snote.muted{{color:{SUB}}}
table{{width:100%;border-collapse:collapse;margin-bottom:8px;font-size:13px}}
td,th{{border:1px solid {BORDER};padding:6px 9px;text-align:left;vertical-align:top}}
th{{background:#0f2429;color:{ACCENT2};font-weight:600}}
.stab .sl,.wtab td:first-child{{color:{ACCENT2};white-space:nowrap;width:42%}}
.item{{margin-bottom:12px}}.ihead{{font-size:14px;font-weight:600;margin-bottom:5px}}
.ino{{display:inline-block;background:{ACCENT};color:{BG};width:22px;height:22px;text-align:center;border-radius:6px;font-size:12px;line-height:22px;margin-right:6px}}
.imax{{color:{SUB};font-size:12px;margin-left:6px}}.axis{{font-size:11px;color:{SUB};margin-left:8px}}
.gtab td{{padding:4px 9px}}.gtab .gr{{font-weight:700;width:34px;text-align:center}}.gtab .pt{{color:{SUB};width:44px;white-space:nowrap}}
.note{{font-size:12.5px;color:{SUB};margin:4px 0 0;padding:6px 10px;background:#0f2429;border-radius:6px}}
.ttab .rng{{white-space:nowrap;color:{ACCENT2};font-weight:600}}.ttab .vd{{white-space:nowrap}}
.act{{display:inline-block;padding:2px 8px;border-radius:6px;font-size:12px;font-weight:700}}
.act-BUY_NOW{{background:#123d33;color:#48e0b0;border:1px solid #1f6b57}}
.act-WATCH{{background:#123047;color:#5bb2e6;border:1px solid #1f5079}}
.act-AVOID{{background:#2e1a1a;color:#c98a8a;border:1px solid #6b2f2f}}
.ops{{margin:0;padding-left:18px;font-size:13px}}.ops li{{margin-bottom:6px}}.alt{{color:{ACCENT2}}}
footer{{color:{SUB};font-size:12px;text-align:center;margin-top:30px}}
</style></head><body><div class='wrap'>
<h1>5大手法 スコアリング基準マスター</h1>
<div class='ver'>version {esc(spec['version'])} ／ 唯一の正（master.json から自動生成）</div>
<div class='tabs'><a class='here' href='./index.html'>📊 スコアリング基準</a><a href='./setup_guide.html'>🛠 設定要領</a><a href='./board.html'>📋 候補ボード</a><a href='./system.html'>🖥 システム</a></div>
<div class='lead'>{esc(spec['description'])}</div>
<div class='common'><div class='gp'>共通配点：{esc(gp)}　／　満点 {esc(common['max_score'])}点</div>
<div class='sub'>アクション定義</div><table><tbody>{acts}</tbody></table></div>
<div class='nav'>{nav}</div>{sections}
<footer>index.html は scripts/render_master.py が master.json から生成。基準変更は master.json を編集し再生成すること。</footer>
</div></body></html>"""

with open(os.path.join(ROOT, "docs", "index.html"), "w", encoding="utf-8") as f:
    f.write(out)
print("written: docs/index.html", file=sys.stderr)
