#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""master.json の system_status から docs/system.html を生成する。
   ページは raw URL から master.json を live fetch し、失敗時は埋め込みスナップショットで描画する。"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
MASTER = os.path.join(ROOT, "master.json")
OUT = os.path.join(ROOT, "docs", "system.html")

RAW_URL = "https://raw.githubusercontent.com/kohshi529-glitch/asset_operation/main/master.json"

with open(MASTER, encoding="utf-8") as f:
    data = json.load(f)

snapshot = data.get("system_status", {})
embedded = json.dumps(snapshot, ensure_ascii=False)

html = """<!doctype html><html lang='ja'><head><meta charset='utf-8'>
<meta name='viewport' content='width=device-width,initial-scale=1'>
<title>システム — 3層実行体制マップ</title><style>
:root{color-scheme:dark}*{box-sizing:border-box}
body{margin:0;background:#0d1b1e;color:#e6f4f1;font-family:-apple-system,'Hiragino Sans','Noto Sans JP',sans-serif;line-height:1.55}
.wrap{max-width:1080px;margin:0 auto;padding:20px 16px 80px}
h1{font-size:22px;margin:6px 0 2px}
.ver{color:#8fb3ad;font-size:13px;margin-bottom:14px}
.ver b{color:#7fe3d6;font-weight:600}
.src{font-size:12px;color:#8fb3ad;margin-bottom:16px}
.src .live{color:#48e0b0}.src .snap{color:#e8c766}
.nav{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:20px}
.nav a{background:#12292e;border:1px solid #1d3a40;color:#e6f4f1;text-decoration:none;padding:7px 12px;border-radius:999px;font-size:13px}
.nav a.here{border-color:#1fb6a6;color:#7fe3d6}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:10px;margin-bottom:22px}
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
.card .top{display:flex;align-items:center;gap:7px;margin-bottom:5px;flex-wrap:wrap}
.code{font-size:11px;color:#0d1b1e;background:#8fb3ad;border-radius:5px;padding:1px 6px;font-weight:700}
.sched{font-size:11px;color:#8fb3ad;margin-left:auto;white-space:nowrap}
.cname{font-size:13.5px;font-weight:600;flex-basis:100%;margin-top:2px}
.proj{font-size:11px;color:#7fe3d6;margin-top:3px}
.badge{display:inline-block;font-size:11px;font-weight:700;padding:2px 8px;border-radius:6px;border:1px solid}
.b-active{background:#123d33;color:#48e0b0;border-color:#1f6b57}
.b-done_once{background:#10322c;color:#5fd6be;border-color:#1f6b57}
.b-planned{background:#123047;color:#5bb2e6;border-color:#1f5079}
.b-needs_confirmation{background:#3a2a12;color:#f0b866;border-color:#6b4f1e}
.b-on_hold{background:#2a2410;color:#e8c766;border-color:#5c4a1e}
.b-under_review{background:#241a2e;color:#b98fe0;border-color:#432f6b}
.dep{margin-top:6px;font-size:11px;color:#8fb3ad}
.dep .chip{display:inline-block;background:#0f2429;border:1px solid #1d3a40;border-radius:5px;padding:1px 6px;margin-left:4px;color:#7fe3d6}
.wave{font-size:10.5px;color:#8fb3ad;border:1px solid #1d3a40;border-radius:5px;padding:1px 5px}
.note{font-size:11.5px;color:#8fb3ad;margin-top:6px;padding:6px 8px;background:#0f2429;border-radius:6px}
.sec{margin-top:26px}
.sec h2{font-size:16px;margin:0 0 10px;color:#e6f4f1;border-bottom:1px solid #1d3a40;padding-bottom:6px}
.q{background:#12292e;border:1px solid #1d3a40;border-left:3px solid #f0b866;border-radius:10px;padding:11px 12px;margin-bottom:10px}
.q .qt{font-size:14px;font-weight:600;margin-bottom:4px}
.q .qt .no{color:#f0b866;margin-right:6px}
.q .qd{font-size:12.5px;color:#8fb3ad}
.q .blk{margin-top:6px;font-size:11px;color:#8fb3ad}
.q .blk .chip{display:inline-block;background:#0f2429;border:1px solid #1d3a40;border-radius:5px;padding:1px 6px;margin-left:4px;color:#7fe3d6}
.risk{background:#241416;border:1px solid #5c2f2f;border-left:3px solid #c98a8a;border-radius:10px;padding:11px 12px;margin-bottom:10px}
.risk .rt{font-size:14px;font-weight:600;color:#e6b3b3;margin-bottom:4px}
.risk .rt .sev{font-size:10.5px;background:#6b2f2f;color:#f0c9c9;border-radius:5px;padding:1px 7px;margin-left:6px}
.risk .rd{font-size:12.5px;color:#c9a9a9}
.legend{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0 4px}
footer{color:#8fb3ad;font-size:12px;text-align:center;margin-top:34px}
</style></head><body><div class='wrap'>
<h1>🖥 システム — 3層実行体制マップ</h1>
<div class='ver'>version <b id='ver'>—</b> ／ master.json <code>system_status</code> を描画</div>
<div class='src' id='src'>データ取得中…</div>
<div class='nav'>
<a href='./index.html'>📊 スコアリング基準</a>
<a href='./setup_guide.html'>🛠 設定要領</a>
<a href='./board.html'>📋 候補ボード</a>
<a class='here' href='./system.html'>🖥 システム</a>
</div>
<div class='kpis' id='kpis'></div>
<div class='cols' id='cols'></div>
<div class='sec' id='q-sec'></div>
<div class='sec' id='r-sec'></div>
<div class='legend' id='legend'></div>
<footer>docs/system.html ／ 唯一の正 master.json から描画。タスクの追加・状態変更は master.json の system_status を編集する。</footer>
</div>
<script>
const RAW_URL = "__RAW_URL__";
const EMBEDDED = __EMBEDDED__;
const STATUS_LABEL = {active:"稼働中",planned:"予定",on_hold:"保留",under_review:"要検討",needs_confirmation:"確定待ち",done_once:"初回完了"};
const LAYER_META = {L1:{name:"L1 Claude Codeルーティン",sub:"無人スケジュール実行→リポジトリ蓄積"},L2:{name:"L2 Cowork",sub:"プロジェクト＋ファイル処理＋スケジュールタスク"},L3:{name:"L3 対話セッション",sub:"ライブ判断・当面継続"}};
function esc(s){return (s==null?"":String(s)).replace(/[&<>]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[c]));}

function render(ss, live){
  document.getElementById('ver').textContent = ss.version || "—";
  const src = document.getElementById('src');
  src.innerHTML = live
    ? "<span class='live'>● LIVE</span> GitHub の最新 master.json を表示中"
    : "<span class='snap'>● SNAPSHOT</span> 取得失敗のため生成時点の内蔵データを表示中";
  const tasks = ss.tasks||[];
  const idMap = {}; tasks.forEach(t=>idMap[t.id]=t);

  // KPI
  const byLayer = {L1:0,L2:0,L3:0}, byStatus={};
  tasks.forEach(t=>{byLayer[t.layer]=(byLayer[t.layer]||0)+1;byStatus[t.status]=(byStatus[t.status]||0)+1;});
  const kpis=[
    {n:tasks.length,l:"総タスク"},
    {n:byStatus.active||0,l:"稼働中"},
    {n:byStatus.planned||0,l:"予定"},
    {n:(ss.open_questions||[]).length,l:"未確定",warn:true},
    {n:(ss.known_risks||[]).length,l:"リスク",warn:true},
  ];
  document.getElementById('kpis').innerHTML = kpis.map(k=>
    `<div class='kpi ${k.warn?'warn':''}'><div class='n'>${k.n}</div><div class='l'>${esc(k.l)}</div></div>`).join('');

  // 層別カラム
  const order=["L1","L2","L3"];
  document.getElementById('cols').innerHTML = order.map(L=>{
    const meta=LAYER_META[L];
    const list=tasks.filter(t=>t.layer===L);
    const cards=list.map(t=>{
      const deps=(t.depends_on||[]).map(d=>`<span class='chip'>${esc((idMap[d]&&(idMap[d].code||idMap[d].name))||d)}</span>`).join('');
      return `<div class='card'>
        <div class='top'>
          ${t.code?`<span class='code'>${esc(t.code)}</span>`:''}
          <span class='badge b-${t.status}'>${esc(STATUS_LABEL[t.status]||t.status)}</span>
          ${t.wave?`<span class='wave'>第${t.wave}弾</span>`:''}
          <span class='sched'>${esc(t.schedule||'')}</span>
          <span class='cname'>${esc(t.name)}</span>
        </div>
        ${t.project?`<div class='proj'>▸ ${esc(t.project)}</div>`:''}
        ${deps?`<div class='dep'>依存:${deps}</div>`:''}
        ${t.notes?`<div class='note'>${esc(t.notes)}</div>`:''}
      </div>`;
    }).join('');
    return `<div class='col ${L}'><h2><span class='dot'></span>${esc(meta.name)}</h2><div class='sub'>${esc(meta.sub)}</div>${cards}</div>`;
  }).join('');

  // 未確定
  const qs=ss.open_questions||[];
  document.getElementById('q-sec').innerHTML = "<h2>⚠️ 未確定事項</h2>"+qs.map(q=>{
    const blk=(q.blocks||[]).map(b=>`<span class='chip'>${esc((idMap[b]&&(idMap[b].code||idMap[b].name))||b)}</span>`).join('');
    return `<div class='q'><div class='qt'><span class='no'>#${q.no}</span>${esc(q.topic)}</div>
      <div class='qd'>${esc(q.detail)}</div>
      ${blk?`<div class='blk'>影響先:${blk}</div>`:''}</div>`;
  }).join('');

  // リスク
  const rs=ss.known_risks||[];
  document.getElementById('r-sec').innerHTML = "<h2>🚧 既知リスク</h2>"+rs.map(r=>
    `<div class='risk'><div class='rt'>${esc(r.title)}<span class='sev'>${esc(r.severity||'')}</span></div>
     <div class='rd'>${esc(r.detail)}</div></div>`).join('');

  // 凡例
  document.getElementById('legend').innerHTML = Object.keys(STATUS_LABEL).map(k=>
    `<span class='badge b-${k}'>${esc(STATUS_LABEL[k])}</span>`).join('');
}

render(EMBEDDED, false);
fetch(RAW_URL, {cache:"no-store"}).then(r=>r.ok?r.json():Promise.reject()).then(j=>{
  if(j && j.system_status){ render(j.system_status, true); }
}).catch(()=>{ /* フォールバックのまま */ });
</script>
</body></html>"""

html = html.replace("__RAW_URL__", RAW_URL).replace("__EMBEDDED__", embedded)

with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)

print("生成:", OUT)
print("bytes:", len(html))
print("tasks:", len(snapshot.get("tasks", [])))
