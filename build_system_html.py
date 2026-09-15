#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""master.json の system_status からリポジトリ直下の system.html を生成する。

   ページは GitHub Pages の master.json を live fetch し、取得できた system_status.version が
   内蔵スナップショットと同じか新しいときだけそれを描画する（古い／失敗なら内蔵スナップショット）。
   raw.githubusercontent.com は全読み取り経路で使用禁止のため使わない。

   使い方: リポジトリ直下で  python3 build_system_html.py
   （system_status を変えたら再生成してコミットする。master.json 自体は丸ごとコミットしない）"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
MASTER = os.path.join(HERE, "master.json")
OUT = os.path.join(HERE, "system.html")
# 外部指定があればそちらの system_status を内蔵する（メンテナンスPRのマージ前に先行生成する用途）
SNAPSHOT_OVERRIDE = os.environ.get("SYSTEM_STATUS_JSON")

PAGES_URL = "https://kohshi529-glitch.github.io/asset_operation/master.json"

if SNAPSHOT_OVERRIDE:
    with open(SNAPSHOT_OVERRIDE, encoding="utf-8") as f:
        snapshot = json.load(f)
else:
    with open(MASTER, encoding="utf-8") as f:
        snapshot = json.load(f).get("system_status", {})

embedded = json.dumps(snapshot, ensure_ascii=False).replace("</", "<\\/")

html = r"""<!doctype html><html lang='ja'><head><meta charset='utf-8'>
<meta name='viewport' content='width=device-width,initial-scale=1'>
<link rel='apple-touch-icon' href='apple-touch-icon.png'>
<link rel='icon' type='image/png' href='apple-touch-icon.png'>
<title>システム — 3層実行体制マップ</title><style>
:root{color-scheme:dark}*{box-sizing:border-box}
body{margin:0;background:#0d1b1e;color:#e6f4f1;font-family:-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif;line-height:1.55}
.wrap{max-width:1080px;margin:0 auto;padding:20px 16px 80px}
h1{font-size:22px;margin:6px 0 2px}
.ver{color:#8fb3ad;font-size:13px;margin-bottom:6px}
.ver b{color:#7fe3d6;font-weight:600}
.src{font-size:12px;color:#8fb3ad;margin-bottom:16px}
.src .live{color:#48e0b0}.src .snap{color:#e8c766}
.tabs{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:20px}
.tabs a{background:#12292e;border:1px solid #1d3a40;color:#e6f4f1;text-decoration:none;padding:7px 12px;border-radius:999px;font-size:13px}
.tabs a.here{border-color:#1fb6a6;color:#7fe3d6}
.desc{font-size:12.5px;color:#8fb3ad;background:#0f2429;border:1px solid #1d3a40;border-radius:10px;padding:10px 12px;margin-bottom:16px}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(110px,1fr));gap:10px;margin-bottom:22px}
.kpi{background:#12292e;border:1px solid #1d3a40;border-radius:12px;padding:12px 14px}
.kpi .n{font-size:26px;font-weight:700;color:#7fe3d6;line-height:1.1}
.kpi .l{font-size:12px;color:#8fb3ad;margin-top:2px}
.kpi.warn .n{color:#f0b866}
.cols{display:grid;grid-template-columns:1fr;gap:18px}
@media(min-width:820px){.cols{grid-template-columns:repeat(3,1fr)}}
.col{background:#0f2429;border:1px solid #1d3a40;border-radius:14px;padding:14px 12px}
.col h2{font-size:15px;margin:0 0 3px;display:flex;align-items:center;gap:8px}
.col .sub{font-size:11.5px;color:#8fb3ad;margin-bottom:12px}
.col .dot{width:10px;height:10px;border-radius:3px;display:inline-block}
.L1 .dot{background:#1fb6a6}.L2 .dot{background:#c9a24a}.L3 .dot{background:#5bb2e6}
.card{background:#12292e;border:1px solid #1d3a40;border-left:3px solid #1fb6a6;border-radius:10px;padding:10px 11px;margin-bottom:10px}
.L1 .card{border-left-color:#1fb6a6}.L2 .card{border-left-color:#c9a24a}.L3 .card{border-left-color:#5bb2e6}
.card.retired{opacity:.55;border-left-color:#5a6b6e}
.card .top{display:flex;align-items:center;gap:7px;margin-bottom:5px;flex-wrap:wrap}
.code{font-size:11px;color:#0d1b1e;background:#8fb3ad;border-radius:5px;padding:1px 6px;font-weight:700}
.sched{font-size:11px;color:#8fb3ad;margin-left:auto;text-align:right}
.cname{font-size:13.5px;font-weight:600;flex-basis:100%;margin-top:2px}
.proj{font-size:11px;color:#7fe3d6;margin-top:3px}
.meta{font-size:11px;color:#8fb3ad;margin-top:4px;display:flex;flex-wrap:wrap;gap:4px 10px}
.meta b{color:#c9e8e2;font-weight:600}
.meta code{font-size:10.5px;color:#7fe3d6;background:#0f2429;border-radius:4px;padding:0 4px}
.badge{display:inline-block;font-size:11px;font-weight:700;padding:2px 8px;border-radius:6px;border:1px solid}
.b-active{background:#123d33;color:#48e0b0;border-color:#1f6b57}
.b-testing{background:#10322c;color:#5fd6be;border-color:#1f6b57}
.b-done_once{background:#10322c;color:#5fd6be;border-color:#1f6b57}
.b-planned{background:#123047;color:#5bb2e6;border-color:#1f5079}
.b-needs_confirmation{background:#3a2a12;color:#f0b866;border-color:#6b4f1e}
.b-on_hold{background:#2a2410;color:#e8c766;border-color:#5c4a1e}
.b-under_review{background:#241a2e;color:#b98fe0;border-color:#432f6b}
.b-retired{background:#1a2426;color:#8fa3a6;border-color:#33474a}
.dep{margin-top:6px;font-size:11px;color:#8fb3ad}
.dep .chip,.wr .chip{display:inline-block;background:#0f2429;border:1px solid #1d3a40;border-radius:5px;padding:1px 6px;margin:2px 4px 0 0;color:#7fe3d6}
.wr{margin-top:5px;font-size:11px;color:#8fb3ad}
.note{font-size:11.5px;color:#8fb3ad;margin-top:6px;padding:6px 8px;background:#0f2429;border-radius:6px}
.sec{margin-top:26px}
.sec h2{font-size:16px;margin:0 0 10px;color:#e6f4f1;border-bottom:1px solid #1d3a40;padding-bottom:6px}
.q{background:#12292e;border:1px solid #1d3a40;border-left:3px solid #f0b866;border-radius:10px;padding:11px 12px;margin-bottom:10px}
.q.resolved{border-left-color:#1f6b57;opacity:.7}
.q .qt{font-size:14px;font-weight:600;margin-bottom:4px}
.q .qt .no{color:#f0b866;margin-right:6px}
.q .qd{font-size:12.5px;color:#8fb3ad}
.q .blk{margin-top:6px;font-size:11px;color:#8fb3ad}
.q .blk .chip{display:inline-block;background:#0f2429;border:1px solid #1d3a40;border-radius:5px;padding:1px 6px;margin-left:4px;color:#7fe3d6}
.risk{background:#241416;border:1px solid #5c2f2f;border-left:3px solid #c98a8a;border-radius:10px;padding:11px 12px;margin-bottom:10px}
.risk.resolved{background:#12292e;border-color:#1d3a40;border-left-color:#1f6b57;opacity:.75}
.risk .rt{font-size:14px;font-weight:600;color:#e6b3b3;margin-bottom:4px}
.risk.resolved .rt{color:#c9e8e2}
.risk .rt .sev{font-size:10.5px;background:#6b2f2f;color:#f0c9c9;border-radius:5px;padding:1px 7px;margin-left:6px}
.risk.resolved .rt .sev{background:#1f6b57;color:#d6f5ec}
.risk .rd{font-size:12.5px;color:#c9a9a9}
.risk.resolved .rd{color:#8fb3ad}
.bd{background:#12292e;border:1px solid #1d3a40;border-radius:10px;padding:10px 12px;margin-bottom:10px}
.bd .bt{font-size:14px;font-weight:600;margin-bottom:3px}
.bd .bv{font-size:11px;color:#f0b866;margin-left:6px;font-weight:400}
.bd .bl{font-size:12px;color:#8fb3ad}
.bd .bl b{color:#c9e8e2;font-weight:600}
.tbl{overflow-x:auto}
table{width:100%;border-collapse:collapse;font-size:12px}
td,th{border:1px solid #1d3a40;padding:6px 8px;text-align:left;vertical-align:top}
th{background:#0f2429;color:#7fe3d6;white-space:nowrap}
td code{color:#7fe3d6;font-size:11.5px}
.conv{font-size:12.5px;color:#c9e8e2;background:#12292e;border:1px solid #1d3a40;border-left:3px solid #c98a8a;border-radius:10px;padding:8px 12px;margin-bottom:8px}
.legend{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0 4px}
footer{color:#8fb3ad;font-size:12px;text-align:center;margin-top:34px}
</style></head><body><div class='wrap'>
<h1>🖥 システム — 3層実行体制マップ</h1>
<div class='ver'>version <b id='ver'>—</b> ／ master.json <code>system_status</code> を描画</div>
<div class='src' id='src'>データ取得中…</div>
<div class='tabs'>
<a href='./index.html'>📊 スコアリング基準</a>
<a href='./setup_guide.html'>🛠 設定要領</a>
<a href='./board.html'>📋 候補ボード</a>
<a class='here' href='./system.html'>🖥 システム</a>
<a href='./gate_history.html'>🕒 ゲート履歴</a>
</div>
<div class='desc' id='desc'></div>
<div class='kpis' id='kpis'></div>
<div class='cols' id='cols'></div>
<div class='sec' id='b-sec'></div>
<div class='sec' id='d-sec'></div>
<div class='sec' id='c-sec'></div>
<div class='sec' id='q-sec'></div>
<div class='sec' id='r-sec'></div>
<div class='legend' id='legend'></div>
<footer>system.html ／ 唯一の正 master.json の system_status から描画。変更は system_status のメンテナンスPR → <code>python3 build_system_html.py</code> で再生成。</footer>
</div>
<script>
// 読み取りは Pages 経由に固定（raw.githubusercontent.com は全読み取り経路で使用禁止）
const PAGES_URL = "__PAGES_URL__";
const EMBEDDED = __EMBEDDED__;
const STATUS_LABEL = {active:"稼働中",testing:"検証期間",planned:"予定",on_hold:"保留",under_review:"要検討",needs_confirmation:"確認待ち",done_once:"初回完了",retired:"統合・廃止"};
const LAYER_META = {L1:{name:"L1 Claude Code ルーティン",sub:"無人スケジュール実行 → PR → 翌朝マージ → リポジトリ蓄積"},L2:{name:"L2 Cowork",sub:"プロジェクト指示＋スケジュールタスク（Drive 非公開データの書き手）"},L3:{name:"L3 対話セッション",sub:"ライブ判断・仕様改訂・正典登録・ボード改修"}};
function esc(s){return (s==null?"":String(s)).replace(/[&<>]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[c]));}

function render(ss, live){
  document.getElementById('ver').textContent = ss.version || "—";
  const src = document.getElementById('src');
  src.innerHTML = live
    ? "<span class='live'>● LIVE</span> GitHub Pages の最新 master.json を表示中"
    : "<span class='snap'>● SNAPSHOT</span> 生成時点の内蔵データを表示中（ライブ版が取得できないか、内蔵より古い）";
  document.getElementById('desc').textContent = ss.description || "";
  const tasks = ss.tasks||[];
  const idMap = {}; tasks.forEach(t=>idMap[t.id]=t);
  const lg = (ss.legend&&ss.legend.layers)||{};
  Object.keys(lg).forEach(L=>{ if(LAYER_META[L]) LAYER_META[L].sub = lg[L]; });

  // KPI
  const byStatus={};
  tasks.forEach(t=>{byStatus[t.status]=(byStatus[t.status]||0)+1;});
  const openQ=(ss.open_questions||[]).filter(q=>q.status!=='resolved').length;
  const openR=(ss.known_risks||[]).filter(r=>r.severity!=='resolved').length;
  const kpis=[
    {n:tasks.filter(t=>t.status!=='retired').length,l:"現行タスク"},
    {n:(byStatus.active||0)+(byStatus.testing||0),l:"稼働中"},
    {n:byStatus.needs_confirmation||0,l:"確認待ち",warn:true},
    {n:openQ,l:"未確定（open）",warn:true},
    {n:openR,l:"リスク（未解決/監視）",warn:true},
  ];
  document.getElementById('kpis').innerHTML = kpis.map(k=>
    `<div class='kpi ${k.warn?'warn':''}'><div class='n'>${k.n}</div><div class='l'>${esc(k.l)}</div></div>`).join('');

  // 層別カラム（retired は末尾）
  const order=["L1","L2","L3"];
  const rank=t=>t.status==='retired'?1:0;
  document.getElementById('cols').innerHTML = order.map(L=>{
    const meta=LAYER_META[L];
    const list=tasks.filter(t=>t.layer===L).sort((a,b)=>rank(a)-rank(b));
    const cards=list.map(t=>{
      const deps=(t.depends_on||[]).map(d=>`<span class='chip'>${esc((idMap[d]&&(idMap[d].code||idMap[d].name))||d)}</span>`).join('');
      const writes=(t.writes||[]).map(w=>`<span class='chip'>${esc(w)}</span>`).join('');
      const metaRow = (t.version||t.canon) ? `<div class='meta'>${t.version?`<span>版 <b>${esc(t.version)}</b></span>`:''}${t.canon?`<span>正典 <code>${esc(t.canon)}</code></span>`:''}</div>` : '';
      return `<div class='card ${t.status==='retired'?'retired':''}'>
        <div class='top'>
          ${t.code?`<span class='code'>${esc(t.code)}</span>`:''}
          <span class='badge b-${esc(t.status)}'>${esc(STATUS_LABEL[t.status]||t.status)}</span>
          <span class='sched'>${esc(t.schedule||'')}</span>
          <span class='cname'>${esc(t.name)}</span>
        </div>
        ${t.project?`<div class='proj'>▸ ${esc(t.project)}</div>`:''}
        ${metaRow}
        ${writes?`<div class='wr'>書き込み先:${writes}</div>`:''}
        ${deps?`<div class='dep'>依存:${deps}</div>`:''}
        ${t.notes?`<div class='note'>${esc(t.notes)}</div>`:''}
      </div>`;
    }).join('');
    return `<div class='col ${L}'><h2><span class='dot'></span>${esc(meta.name)}</h2><div class='sub'>${esc(meta.sub)}</div>${cards}</div>`;
  }).join('');

  // ボード
  const bs=ss.boards||[];
  document.getElementById('b-sec').innerHTML = bs.length ? "<h2>🗂 ボード</h2>"+bs.map(b=>
    `<div class='bd'><div class='bt'>${esc(b.name)}<span class='bv'>${esc(b.visibility||'')}</span></div>
     <div class='bl'><b>データ源:</b> ${esc(b.source||'')}${b.tabs?` ／ <b>タブ:</b> ${esc(b.tabs)}`:''}</div>
     ${b.notes?`<div class='note'>${esc(b.notes)}</div>`:''}</div>`).join('') : '';

  // 派生ファイル
  const ds=ss.derived_files||[];
  document.getElementById('d-sec').innerHTML = ds.length ? "<h2>📦 派生ファイル（Pages 配信・master.json を重くしないための射影）</h2><div class='tbl'><table><thead><tr><th>ファイル</th><th>書き手</th><th>更新</th><th>サイズ</th><th>内容</th></tr></thead><tbody>"+
    ds.map(d=>`<tr><td><code>${esc(d.path)}</code></td><td>${esc(d.writer)}</td><td>${esc(d.when)}</td><td>${esc(d.size)}</td><td>${esc(d.content)}</td></tr>`).join('')+"</tbody></table></div>" : '';

  // 運用規約
  const cv=(ss.legend&&ss.legend.conventions)||[];
  document.getElementById('c-sec').innerHTML = cv.length ? "<h2>📜 運用規約（全層共通）</h2>"+cv.map(c=>`<div class='conv'>${esc(c)}</div>`).join('') : '';

  // 未確定
  const qs=ss.open_questions||[];
  document.getElementById('q-sec').innerHTML = "<h2>⚠️ 未確定事項</h2>"+qs.map(q=>{
    const blk=(q.blocks||[]).map(b=>`<span class='chip'>${esc((idMap[b]&&(idMap[b].code||idMap[b].name))||b)}</span>`).join('');
    return `<div class='q ${q.status==='resolved'?'resolved':''}'><div class='qt'><span class='no'>#${esc(q.no)}</span>${esc(q.topic)}${q.status?` <span class='badge b-${q.status==='resolved'?'active':'needs_confirmation'}'>${q.status==='resolved'?'解決':'open'}</span>`:''}</div>
      <div class='qd'>${esc(q.detail)}</div>
      ${blk?`<div class='blk'>影響先:${blk}</div>`:''}</div>`;
  }).join('');

  // リスク
  const rs=ss.known_risks||[];
  document.getElementById('r-sec').innerHTML = "<h2>🚧 既知リスク</h2>"+rs.map(r=>
    `<div class='risk ${r.severity==='resolved'?'resolved':''}'><div class='rt'>${esc(r.title)}<span class='sev'>${esc(r.severity||'')}</span></div>
     <div class='rd'>${esc(r.detail)}</div></div>`).join('');

  // 凡例
  const st=(ss.legend&&ss.legend.status)||STATUS_LABEL;
  document.getElementById('legend').innerHTML = Object.keys(st).map(k=>
    `<span class='badge b-${esc(k)}'>${esc(st[k])}</span>`).join('');
}

render(EMBEDDED, false);
fetch(PAGES_URL, {cache:"no-store"}).then(r=>r.ok?r.json():Promise.reject()).then(j=>{
  const ss = j && j.system_status;
  // ライブ版が内蔵より古い（メンテナンスPR未マージ等）ときは内蔵スナップショットのまま
  if(ss && String(ss.version||'') >= String(EMBEDDED.version||'')){ render(ss, true); }
}).catch(()=>{ /* フォールバックのまま */ });
</script>
</body></html>"""

html = html.replace("__PAGES_URL__", PAGES_URL).replace("__EMBEDDED__", embedded)

with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)

print("生成:", OUT)
print("bytes:", len(html.encode("utf-8")))
print("version:", snapshot.get("version"))
print("tasks:", len(snapshot.get("tasks", [])))
