# 夜間ゲート 2026-11-20（連休前最終営業日・翌営業日 11/24(火)）

## サマリー
- 評価数: 545（プール543＋前夜提案のみ2） / PASS: 27（PASS_DOJI 11件を含む）
- 発注可能提案数: 8件（✅3／⏳2／⏸位置不適3／⏸トラップ疑い0）
- 市場一言: 市場モード「弱気」（market.latest 2026-11-20）。全面安の日でプールの PASS 比率 5.0%（陰線FAIL 448件・上髭FAIL 70件）。TOPIX(1306) 当日-4.0%・5日-7.1%・20日-8.2%
- 実行モード: 通常（11/20(金)=営業日・翌11/21(土)非営業日だが本日が営業日のため通常モード）
- base_day: 2026-11-20（run_at 2026-11-20T20:31:00+09:00）
- week_open: true（翌営業日 11/24(火)＝3連休明けの週初営業日）→ STEP 4.8 実行
- 📆 翌営業日 11/24: カレンダーイベントなし（3連休明け。T+2 11/25: なし）／本日 11/20 は連休前最終営業日
- 📑指数: 低減対象 提案4件／PASS7件／プール75件・新規採用 8件（index_flags 2026-10-07 公表分）・次の TOPIX 低減日 01/29 第2回/8（あと46営業日）

## 検証結果
- V1 → はい（提案8=results8=模擬8=通知母数8）
- V2 → はい（PASS27=提案8+除外14+常駐5・order_status欠落0）
- V3 → はい（results543件重複0）
- V4 → はい（既存static変更0）
- V5 → はい（変更トップキー['earnings_log', 'night_gate', 'pipeline', 'profile_cache']・pipeline他run不変True・spec等不変True）
- V6 → はい（gyoseki_cache不整合0）
- V7 → はい（必須セクション存在（📅含む））
- V8 → はい（模擬8行: ｜後ろ空・単元あり・カンマなし）
- V9 → はい（gate_history/2026-11-20.json 新規作成・today と一致）
- V10 → はい（4箇所 base_day=2026-11-20）
- V11 → いいえ（+13122/-13705（W=2・往復一致で検出・仮ファイル経由））
- V12 → はい（(a)True(b)True(c)True）
- V13 → はい（1142銘柄/680KB・(c)和集合1122⊆stocks・20キーTrue・nx一致True・業種中央値26業種）
- V14 → はい（保持70件/null473件・出所不明/不一致0）
- V15 → はい（PASS27件中27件付与（欠落0）・5キーTrue・(c)組み立て由来の未取得/取得不可0（キャッシュのグレード名転記1件は除く））
- V16 → はい（📊1件すべて記録True・(b)再計算未実施のため該当なし・history超過0・総数508）
- V17 → はい（pool_bars 546銘柄/468KB・先読み0・保有0銘柄（3日ルール判定対象なし））
- V18 → はい（誤除外0・鮮度切れ6件すべて nom_age>10・nom_age欠損0）
- V19 → はい（verdicts545=評価545・12要素True・nominations174=last_seen当日True・写し漏れなしTrue・ctx判定不能2）
- V20 → はい（1186銘柄/156KB・nx非null215・hist有830・pxd501・不正(b)False(c)0(d)False(e)False）
- V21 → はい（recent_pass520・出所なし0・当夜提案の欠落0・保有キー無しTrue（保有0銘柄））
- V22 → はい（十字線True・位置True・トラップTrue・RSTrue（rs20付与545/545））
- 注: V11 は night_gate.results の全置換（543件×約50行）と pool 更新による実変更行数であり、インデント幅は往復一致で検出した W=2 を維持（全体再フォーマットではない）。前夜（+16352/-10898）と同じ構造
- 公開物への保有情報: 保有0銘柄のため書き込み対象なし（board／gate_history／PR 本文に保有コード・数量・建値・損益・R/streak なし）

## 保有アラート
- 保有0銘柄・アラート0件（詳細は通知）

## 🧾直近提案の決算接近
- 窓内（直近20営業日）の提案銘柄 520・日程不明（❓）452・当夜評価外 157（保有情報は使っていない）
- 📋カルテ窓 12/15(残16営業日) 3565 Ascentech KK｜最後の提案 11/20（momentum 421・⏳確認足待ち）｜当夜 PASS_DOJI
- 📋カルテ窓 12/11(残14営業日) 446A ノースサンド｜最後の提案 11/20（momentum 2406・⏸位置不適(25MA下 -9.63%)）｜当夜 PASS
- 📋カルテ窓 12/15(残16営業日) 4431 Smaregi, Inc.｜最後の提案 11/19（reversal 3090・✅即時可）｜当夜 FAIL_INSEN
- 📋カルテ窓 12/15(残16営業日) 5136 tripla Co.,Ltd.｜最後の提案 11/17（momentum 2730・✅即時可）｜当夜 評価外
- 📋カルテ窓 12/11(残14営業日) 6336 石井表記｜最後の提案 11/17（reversal 1164・✅即時可）｜当夜 FAIL_INSEN
- 📋カルテ窓 12/16(残17営業日) 8975 Ichigo Office REIT Investment Corporation｜最後の提案 11/16（reversal 88800・✅即時可）｜当夜 FAIL_INSEN
- 📋カルテ窓 12/09(残12営業日) 7678 ASAKUMA CO.,LTD.｜最後の提案 11/13（momentum 4450・✅即時可）｜当夜 PASS
- 📋カルテ窓 12/11(残14営業日) 218A Liberaware｜最後の提案 11/11（changepoint 830・✅即時可）｜当夜 FAIL_INSEN
- 📋カルテ窓 12/10(残13営業日) 3491 ＧＡ　ｔｅｃｈｎｏｌｏｇｉｅｓ（ＧＡテクノ）｜最後の提案 11/11（momentum 1568・✅即時可）｜当夜 FAIL_INSEN
- 📋カルテ窓 12/14(残15営業日) 460A ＢＲＡＮＵ｜最後の提案 11/11（reversal 1098・✅即時可）｜当夜 FAIL_INSEN
- 📋カルテ窓 12/08(残11営業日) 9824 泉州電業｜最後の提案 11/11（momentum 7880・⏸位置不適(25MA下 -2.36%)）｜当夜 FAIL_INSEN
- 📋カルテ窓 12/08(残11営業日) 1436 GreenEnergy & Company｜最後の提案 11/10（reversal 1368・✅即時可）｜当夜 FAIL_INSEN
- 📋カルテ窓 12/10(残13営業日) 1928 積水ハウス｜最後の提案 11/09（momentum 3568・✅即時可）｜当夜 FAIL_INSEN
- 📋カルテ窓 12/11(残14営業日) 4075 ブレインズテクノロジー｜最後の提案 11/09（reversal 1037・✅即時可）｜当夜 FAIL_INSEN
- 📋カルテ窓 12/09(残12営業日) 5132 pluszero,Inc.｜最後の提案 11/04（momentum 1761・✅即時可）｜当夜 評価外
- 📋カルテ窓 12/15(残16営業日) 9163 Nareru Group Inc.｜最後の提案 11/04（momentum 2088・✅即時可）｜当夜 FAIL_INSEN
- 📋カルテ窓 12/11(残14営業日) 3653 Morpho, Inc.｜最後の提案 10/29（reversal 918.0・✅即時可）｜当夜 評価外
- 📋カルテ窓 12/10(残13営業日) 8927 Meiho Enterprise Co., Ltd.｜最後の提案 10/29（momentum 466.0・✅即時可）｜当夜 評価外
- 📋カルテ窓 12/11(残14営業日) 186A Astroscale Holdings Inc.｜最後の提案 10/27（momentum 1084.0・✅即時可）｜当夜 評価外
- 📋カルテ窓 12/15(残16営業日) 212A FIT EASY Inc.｜最後の提案 10/27（momentum 2771.0・✅即時可）｜当夜 評価外
- 📋カルテ窓 12/11(残14営業日) 456A Human Made Inc.｜最後の提案 10/27（oshime 1940.0・✅即時可）｜当夜 評価外
- 📋カルテ窓 12/15(残16営業日) 4666 Park24 Co., Ltd.｜最後の提案 10/26（reversal 1850.0・✅即時可）｜当夜 評価外

## 📅今週のカタリスト（11/24〜11/30）
### (a) 今週のカタリスト日程
- 11/24(火) 669A — M&Aロイヤルアドバイザリー(669A) 公開価格決定予定
- 11/25(水) 664A — TOKIUM(664A) 東証グロース上場予定
- 11/25(水) 667A — ジャパンホームシールド(667A) 購入申込期限 11/25
- 11/27(金) 673A — NOTA(673A) BB申込期限 11/27(BB11/24-27)
- 11/30(月) 667A — ジャパンホームシールド(667A) 東証スタンダード上場予定
- 11/30(月) 676A/679A — スマートニュース(676A)・WHI Holdings(679A) 仮条件決定予定
### (b) 今週の市場イベント（日付計算）
- 11/24(火) 3連休明け（11/23 勤労感謝の日の振替なし・11/21-23 休場）
- 11/26(木) 11月 権利付き最終日（参考・11月決算/権利月の銘柄）
- 11/27(金) 11月 権利落ち日（参考）
- 11/30(月) 月末最終営業日・11月 権利確定日
- 市場イベント（WebSearch）: 取得不可（11/24週の「来週の重要イベント」記事が未掲載。推定で埋めない）
### (c) 週末の材料
- 週末材料: 該当なし（金曜夜の実行。base_day 大引け以降の開示は ⚡材料後出し と 📢開示 に反映済み）
### (d) theme_watch / changepoint_watch のシグナル点灯
- theme_watch saas_naiseika: 4418 🔔・4071 🔔
- changepoint_watch: 4419 🔔・6866 🔔・6597 🔔・593A 🔔・5803 🔔
- カタリストは日程であって売買理由ではない。跨ぐか手仕舞うかは事前に決める（教訓⑲）

## 前夜の結果
- PL5口座への正式な反映は週次①-11の採点で行われる。ここは参考情報
- 前夜2026-11-19の提案94件 → 約定59・不約定35・判定不能0
- 4434 momentum 発注3160 → 2026-11-20 O3030.0 H3095.0 L2957.0 C2995.0：不約定
- 8704 momentum 発注1202 → 2026-11-20 O1161.0 H1172.0 L1141.0 C1144.0：不約定
- 4286 momentum 発注1496 → 2026-11-20 O1465.0 H1481.0 L1446.0 C1462.0：不約定
- 147A momentum 発注991 → 2026-11-20 O974.0 H979.0 L933.0 C943.0：不約定
- 7637 momentum 発注3345 → 2026-11-20 O3235.0 H3280.0 L3155.0 C3200.0：不約定
- 3556 momentum 発注857 → 2026-11-20 O825.0 H825.0 L778.0 C783.0：不約定
- 558A momentum 発注6180 → 2026-11-20 O6060.0 H6080.0 L5780.0 C5990.0：不約定
- 9554 momentum 発注1783 → 2026-11-20 O1730.0 H1741.0 L1672.0 C1688.0：不約定
- 6943 momentum 発注6890 → 2026-11-20 O6870.0 H6870.0 L6510.0 C6740.0：不約定
- 6238 momentum 発注1696 → 2026-11-20 O1664.0 H1729.0 L1660.0 C1725.0：約定 1696 含み+1.71%
- 4933 momentum 発注2531 → 2026-11-20 O2510.0 H2528.0 L2450.0 C2466.0：不約定
- 7433 reversal 発注1547 → 2026-11-20 O1510.0 H1526.0 L1485.0 C1488.0：約定 1510.0 含み-1.46%
- 5703 reversal 発注2391 → 2026-11-20 O2341.0 H2376.0 L2294.0 C2300.0：約定 2341.0 含み-1.75%
- 167A reversal 発注3115 → 2026-11-20 O3050.0 H3095.0 L2984.0 C2986.0：約定 3050.0 含み-2.10%
- 6588 reversal 発注2451 → 2026-11-20 O2450.0 H2494.0 L2413.0 C2415.0：約定 2450.0 含み-1.43%
- 6952 reversal 発注2054.5 → 2026-11-20 O2004.5 H2009.5 L1955.5 C1968.0：約定 2004.5 含み-1.82%
- 8133 reversal 発注2003 → 2026-11-20 O1976.0 H2005.0 L1960.0 C1960.0：約定 1976.0 含み-0.81%
- 5331 reversal 発注2840 → 2026-11-20 O2790.0 H2790.0 L2681.0 C2697.0：約定 2790.0 含み-3.33%
- 7004 reversal 発注944 → 2026-11-20 O929.0 H934.0 L897.0 C901.0：約定 929.0 含み-3.01%
- 6651 reversal 発注4065 → 2026-11-20 O3960.0 H4010.0 L3925.0 C3945.0：約定 3960.0 含み-0.38%
- 3569 reversal 発注3570 → 2026-11-20 O3500.0 H3535.0 L3405.0 C3405.0：約定 3500.0 含み-2.71%
- 4403 reversal 発注2572.5 → 2026-11-20 O2529.0 H2550.0 L2458.0 C2469.5：約定 2529.0 含み-2.35%
- 6845 reversal 発注1498.5 → 2026-11-20 O1471.5 H1489.0 L1464.5 C1464.5：約定 1471.5 含み-0.48%
- 5021 reversal 発注3343 → 2026-11-20 O3273.0 H3293.0 L3217.0 C3217.0：約定 3273.0 含み-1.71%
- 6055 reversal 発注1606 → 2026-11-20 O1511.0 H1516.0 L1436.0 C1450.0：約定 1511.0 含み-4.04%
- 6750 reversal 発注1940 → 2026-11-20 O1931.0 H1941.0 L1880.0 C1889.0：約定 1931.0 含み-2.18%
- 5602 reversal 発注1438 → 2026-11-20 O1410.0 H1427.0 L1380.0 C1389.0：約定 1410.0 含み-1.49%
- 9468 reversal 発注3465 → 2026-11-20 O3410.0 H3458.0 L3381.0 C3404.0：約定 3410.0 含み-0.18%
- 4746 reversal 発注1719 → 2026-11-20 O1697.0 H1715.0 L1693.0 C1705.0：約定 1697.0 含み+0.47%
- 6379 reversal 発注950 → 2026-11-20 O944.0 H953.0 L909.0 C909.0：約定 944.0 含み-3.71%
- 5019 reversal 発注1210.5 → 2026-11-20 O1180.5 H1195.5 L1152.0 C1154.5：約定 1180.5 含み-2.20%
- 8366 reversal 発注2075.5 → 2026-11-20 O2032.5 H2075.5 L1919.0 C1926.5：約定 2032.5 含み-5.22%
- 8032 reversal 発注1124 → 2026-11-20 O1118.0 H1140.0 L1094.0 C1100.0：約定 1118.0 含み-1.61%
- 7177 reversal 発注1036 → 2026-11-20 O1010.0 H1026.0 L996.0 C996.0：約定 1010.0 含み-1.39%
- 3994 momentum 発注6919 → 2026-11-20 O6353.0 H6498.0 L6280.0 C6314.0：不約定
- 6777 momentum 発注17980 → 2026-11-20 O17020.0 H17630.0 L16260.0 C16420.0：不約定
- 6613 momentum 発注1700 → 2026-11-20 O1553.0 H1617.0 L1517.0 C1520.0：不約定
- 3374 reversal 発注3355 → 2026-11-20 O3215.0 H3215.0 L3055.0 C3080.0：約定 3215.0 含み-4.20%
- 6834 reversal 発注3790 → 2026-11-20 O3510.0 H3605.0 L3405.0 C3420.0：約定 3510.0 含み-2.56%
- 4062 momentum 発注5334 → 2026-11-20 O4735.0 H4778.0 L4522.0 C4672.0：不約定
- 5801 reversal 発注1855 → 2026-11-20 O1753.0 H1762.0 L1594.0 C1620.0：約定 1753.0 含み-7.59%
- 6787 reversal 発注8370 → 2026-11-20 O8070.0 H8160.0 L7480.0 C7720.0：約定 8070.0 含み-4.34%
- 6918 reversal 発注2800 → 2026-11-20 O2701.0 H2720.0 L2575.0 C2597.0：約定 2701.0 含み-3.85%
- 6524 reversal 発注4190 → 2026-11-20 O4055.0 H4085.0 L3830.0 C3865.0：約定 4055.0 含み-4.69%
- 3110 momentum 発注2381.5 → 2026-11-20 O2200.0 H2203.5 L2084.0 C2098.5：不約定
- 4182 momentum 発注3134 → 2026-11-20 O3000.0 H3029.0 L2904.0 C2923.0：不約定
- 4368 reversal 発注2741 → 2026-11-20 O2609.0 H2633.0 L2504.0 C2540.0：約定 2609.0 含み-2.64%
- 6779 reversal 発注1673 → 2026-11-20 O1540.0 H1557.0 L1476.0 C1493.0：約定 1540.0 含み-3.05%
- 6235 reversal 発注2053 → 2026-11-20 O1950.0 H1960.0 L1845.0 C1875.0：約定 1950.0 含み-3.85%
- 6762 reversal 発注2273.5 → 2026-11-20 O2182.5 H2195.0 L2101.5 C2116.5：約定 2182.5 含み-3.02%
- 6981 reversal 発注5161 → 2026-11-20 O4891.0 H5039.0 L4664.0 C4700.0：約定 4891.0 含み-3.91%
- 7729 reversal 発注12170 → 2026-11-20 O11460.0 H11600.0 L10940.0 C11185.0：約定 11460.0 含み-2.40%
- 1961 reversal 発注2418 → 2026-11-20 O2368.0 H2384.0 L2305.0 C2322.0：約定 2368.0 含み-1.94%
- 5384 reversal 発注2769 → 2026-11-20 O2669.0 H2748.0 L2594.0 C2630.0：約定 2669.0 含み-1.46%
- 6941 reversal 発注6500 → 2026-11-20 O6100.0 H6260.0 L5840.0 C6150.0：約定 6100.0 含み+0.82%
- 3436 momentum 発注2093 → 2026-11-20 O1928.0 H1931.0 L1778.0 C1829.0：不約定
- 4022 momentum 発注1291 → 2026-11-20 O1178.0 H1183.0 L1089.0 C1124.0：不約定
- 6965 reversal 発注2035 → 2026-11-20 O1945.5 H1947.5 L1863.0 C1881.0：約定 1945.5 含み-3.32%
- 5367 momentum 発注981 → 2026-11-20 O921.0 H926.0 L876.0 C883.0：不約定
- 4911 momentum 発注4408 → 2026-11-20 O4323.0 H4349.0 L4095.0 C4139.0：不約定
- 408A reversal 発注232.4 → 2026-11-20 O221.2 H221.3 L215.7 C215.8：約定 221.2 含み-2.44%
- 4523 momentum 発注5344 → 2026-11-20 O5213.0 H5360.0 L5210.0 C5280.0：約定 5344 含み-1.20%
- 4848 momentum 発注1819 → 2026-11-20 O1788.0 H1807.0 L1758.0 C1771.0：不約定
- 8016 momentum 発注792 → 2026-11-20 O778.0 H790.0 L778.0 C783.0：不約定
- 2206 momentum 発注5157 → 2026-11-20 O5100.0 H5143.0 L5069.0 C5069.0：不約定
- 7606 momentum 発注2674 → 2026-11-20 O2659.0 H2683.0 L2631.0 C2665.0：約定 2674 含み-0.34%
- 417A momentum 発注1999 → 2026-11-20 O1991.5 H2013.0 L1976.0 C1976.0：約定 1999 含み-1.15%
- 3092 momentum 発注1218.5 → 2026-11-20 O1200.5 H1213.0 L1196.0 C1198.5：不約定
- 8056 momentum 発注4798 → 2026-11-20 O4706.0 H4866.0 L4706.0 C4845.0：約定 4798 含み+0.98%
- 6412 momentum 発注2172 → 2026-11-20 O2155.0 H2174.0 L2117.0 C2141.0：約定 2172 含み-1.43%
- 4540 momentum 発注4080 → 2026-11-20 O4005.0 H4056.0 L3970.0 C3973.0：不約定
- 5423 momentum 発注1746 → 2026-11-20 O1708.0 H1727.0 L1703.0 C1705.0：不約定
- 4528 momentum 発注2506 → 2026-11-20 O2454.0 H2508.5 L2451.5 C2460.0：約定 2506 含み-1.84%
- 3252 momentum 発注2841 → 2026-11-20 O2788.0 H2802.0 L2754.0 C2766.0：不約定
- 3156 momentum 発注4355 → 2026-11-20 O4100.0 H4165.0 L3835.0 C3890.0：不約定
- 8392 momentum 発注2451 → 2026-11-20 O2350.0 H2427.0 L2250.0 C2277.0：不約定
- 3673 momentum 発注318 → 2026-11-20 O306.0 H314.0 L300.0 C308.0：不約定
- 7504 oshime 発注5145 → 2026-11-20 O5130.0 H5220.0 L5100.0 C5190.0：約定 5130.0 含み+1.17%
- 2326 oshime 発注5689 → 2026-11-20 O5610.0 H5720.0 L5550.0 C5680.0：約定 5610.0 含み+1.25%
- 7537 oshime 発注1988 → 2026-11-20 O1957.0 H1978.0 L1915.0 C1929.0：約定 1957.0 含み-1.43%
- 4968 reversal 発注1854 → 2026-11-20 O1748.0 H1777.0 L1679.0 C1697.0：約定 1748.0 含み-2.92%
- 7713 reversal 発注2541 → 2026-11-20 O2410.0 H2410.0 L2324.0 C2339.0：約定 2410.0 含み-2.95%
- 4431 reversal 発注3090 → 2026-11-20 O2952.0 H2970.0 L2893.0 C2918.0：約定 2952.0 含み-1.15%
- 8344 momentum 発注3875 → 2026-11-20 O3655.0 H3780.0 L3490.0 C3525.0：不約定
- 7826 momentum 発注7940 → 2026-11-20 O7470.0 H7600.0 L7130.0 C7180.0：不約定
- 3763 reversal 発注1860 → 2026-11-20 O1854.0 H1857.0 L1806.0 C1813.0：約定 1854.0 含み-2.21%
- 428A reversal 発注1353 → 2026-11-20 O1363.0 H1368.0 L1310.0 C1324.0：約定 1353 含み-2.14%
- 3371 reversal 発注2007 → 2026-11-20 O2011.0 H2023.0 L1964.0 C1982.0：約定 2007 含み-1.25%
- 3909 reversal 発注780 → 2026-11-20 O870.0 H889.0 L664.0 C674.0：約定 780 含み-13.59%
- 3858 reversal 発注400 → 2026-11-20 O376.0 H388.0 L357.0 C361.0：約定 376.0 含み-3.99%
- 8551 momentum 発注2095 → 2026-11-20 O1999.0 H2052.0 L1919.0 C1926.0：不約定
- 7184 momentum 発注2803 → 2026-11-20 O2737.0 H2775.0 L2622.0 C2640.0：不約定
- 4493 changepoint 発注1871 → 2026-11-20 O1791.0 H1839.0 L1681.0 C1681.0：約定 1791.0 含み-6.14%
- 4259 momentum 発注528 → 2026-11-20 O500.0 H500.0 L478.0 C485.0：不約定

## 模擬テンプレ
```
# base_day 2026-11-20 ／ 提案8件
# 使い方: 参戦する0〜3銘柄の行だけをコピーし、｜の後ろに参戦理由を書いてポジション株PJへ送る。
# 選ばなかった行は送らなくてよい（全行に理由を書く必要はない）。見送りは末尾の1行で足りる。
# 特定銘柄を理由つきで見送る場合のみ『模擬 見送り {code} ｜{理由}』を送る。
模擬 5821 kenmo_momentum 逆指値3085 SL2895.2 単元100 ｜
模擬 446A kenmo_newhigh 逆指値2406 SL2260.7 単元100 ｜
模擬 6238 kenmo_newhigh 逆指値1730 SL1625.3 単元100 ｜
模擬 4180 stf_kakuhen 逆指値1401 SL1342 単元100 ｜
模擬 9006 granville_tenkan 逆指値1601.5 SL1504.5 単元100 ｜
模擬 7504 granville_oshime 指値5170.9 SL5145.2 単元100 ｜
模擬 2326 granville_oshime 指値5675.8 SL5647.6 単元100 ｜
模擬 3565 granville_rebound 逆指値421 SL409 単元100 ｜
模擬 見送り ｜
```

## PASS内訳
- PASS 27件 = 提案 8件（✅即時可3／⏳待機・確認足待ち2／⏸位置不適3／⏸トラップ疑い0） + 常駐観測（提案なし）5件 + 除外 14件（型不一致5（うち十字線3）/材料後出し2/鮮度切れ6/その他1）
- 除外 4379 Photosynth inc.：⛔提案なし(指名鮮度切れ 20営業日)（nom_age 20）
- 除外 9204 Skymark Airlines Inc.：⛔提案なし(指名鮮度切れ 12営業日)（nom_age 12）
- 除外 1926 ライト工業（ライト）：⛔提案なし(材料後出し)
- 除外 1662 Japan Petroleum Exploration Co., Ltd.：⛔型不一致(十字線: トウバ)
- 除外 2109 ＤＭ三井製糖：⛔提案なし(指名鮮度切れ 12営業日)（nom_age 12）
- 除外 2331 ＡＬＳＯＫ：⛔提案なし(手法ブランチ不明)
- 除外 1975 新日本空調：⛔提案なし(指名鮮度切れ 15営業日)（nom_age 15）
- 除外 1982 日比谷総合設備：⛔型不一致(十字線: トウバ)
- 除外 2488 ＪＴＰ：⛔提案なし(指名鮮度切れ 11営業日)（nom_age 11）
- 除外 8056 ＢＩＰＲＯＧＹ：⛔提案なし(指名鮮度切れ 11営業日)（nom_age 11）
- 除外 4443 Ｓａｎｓａｎ：⛔提案なし(材料後出し)
- 除外 3040 ソリトンシステムズ：⛔型不一致(十字線: トウバ)
- 除外 7678 ASAKUMA CO.,LTD.：⛔型不一致(既に支持帯以下)
- 除外 2664 Cawachi Limited：⛔型不一致(既に支持帯以下)
- 常駐観測 7201 日産自動車：📡常駐観測（提案なし）
- 常駐観測 4684 オービック：📡常駐観測（提案なし）
- 常駐観測 4689 LINEヤフー：📡常駐観測（提案なし）
- 常駐観測 9201 日本航空：📡常駐観測（提案なし）
- 常駐観測 9202 ANAホールディングス：📡常駐観測（提案なし）

## 5手法銘柄
- 4249 MORIROKU COMPANY LTD.｜kenmo_momentum｜🚀確変｜🟢値頃｜FAIL_INSEN｜2730｜💰27.3万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈不一致
- 4434 Serverworks Co., Ltd.｜kenmo_momentum｜🚀確変｜⚪妥当｜FAIL_INSEN｜2995｜💰29.9万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈合致
- 8704 TRADERS HOLDINGS CO LTD｜kenmo_momentum｜🔥絶好調｜💎割安｜FAIL_INSEN｜1144｜💰11.4万円｜⚠日程不明｜📈不一致
- 147A SORACOM,INC.｜kenmo_momentum｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜943｜💰9.4万円｜⚠日程不明｜📈レンジ
- 4286 CL Holdings Inc.｜kenmo_momentum/kenmo_newhigh｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜1462｜💰14.6万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈合致
- 6418 Japan Cash Machine Co., Ltd.｜kenmo_momentum/kenmo_newhigh/granville_oshime｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜1371｜💰13.7万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈合致
- 5137 Smart Drive Co. Ltd.｜kenmo_momentum/granville_oshime｜🔥絶好調｜💎割安｜FAIL_INSEN｜285｜💰2.9万円｜⚡材料後出し｜📈レンジ
- 6071 IBJ, Inc.｜kenmo_momentum/kenmo_newhigh/stf_kakuhen｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜902｜💰9.0万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈不一致
- 7637 Hakudo Co., Ltd.｜kenmo_momentum｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜3200｜💰32.0万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈レンジ
- 4771 F&M Co., Ltd.｜kenmo_momentum/kenmo_newhigh/granville_oshime｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜2935｜💰29.4万円｜⚠日程不明｜📈合致
- 1435 robot home Inc.｜kenmo_momentum｜⚡好調｜💎割安｜FAIL_INSEN｜157｜💰1.6万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈レンジ
- 3556 RenetJapanGroup, Inc.｜kenmo_momentum/granville_tenkan｜⚡好調｜💎割安｜FAIL_INSEN｜783｜💰7.8万円｜⚠日程不明｜📈不一致
- 5821 Hirakawa Hewtech Corp.｜kenmo_momentum｜⚡好調｜💎割安｜PASS｜3060｜💰30.6万円｜momentum 3085 SL2895.2・⏸位置不適(25MA下 -2.37%／52週 18.8%)（乖離0.8%）｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明 📐進捗 上振れ 11.8%｜📈レンジ
  > 📌【業態】電線・放送機器メーカー。光中継システム等。医療用チューブも展開。海外でも生産。
  > 📌【いま】終値3,060円・直近5日-4.97%（材料未確認）
  > 📌【調子】⚡好調（7/13）
  > 📌【水準】💎割安（6.0/7）— PER11.61倍・PEG0.508・52週18.8% ／ 💰単元30.6万円
  > 📌【戦略】当日高値超えの逆指値3085円で順張り参戦を検討。上限3115.8円・SL2895.2円目安
- 558A SQUEEZE Inc.｜kenmo_momentum｜⚡好調｜🟡やや割高｜FAIL_INSEN｜5990｜💰59.9万円｜📈レンジ
- 2975 Star Mica Holdings Co., Ltd.｜kenmo_momentum｜⚡好調｜💎割安｜FAIL_INSEN｜1075｜💰10.8万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈不一致
- 9554 AViC Co. Ltd.｜kenmo_momentum｜⚡好調｜🟢値頃｜FAIL_INSEN｜1688｜💰16.9万円｜⚠日程不明｜📈レンジ
- 262A INTERMESTIC INC.｜kenmo_momentum｜⚡好調｜💎割安｜FAIL_INSEN｜1457｜💰14.6万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈不一致
- 3798 ULS Group Incorporated｜kenmo_momentum/granville_tenkan｜✅順調｜💎割安｜FAIL_INSEN｜458｜💰4.6万円｜⚠日程不明｜📈レンジ
- 4743 ITFOR Inc.｜kenmo_momentum｜✅順調｜💎割安｜FAIL_INSEN｜1555｜💰15.6万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈不一致
- 6167 FUJI DIE Co., Ltd.｜kenmo_momentum｜✅順調｜🟡やや割高｜FAIL_UWAHIGE｜1091｜💰10.9万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈レンジ
- 618A KOMPEITO Inc.｜kenmo_momentum/kenmo_newhigh｜取得不可｜⚪妥当｜FAIL_INSEN｜1555｜💰15.6万円｜⚠日程不明｜📈判定不能
- 6943 ＮＫＫスイッチズ｜kenmo_newhigh｜🚀確変｜🟢値頃｜FAIL_INSEN｜6740｜💰67.4万円｜⚠日程不明｜📈合致
- 446A ノースサンド｜kenmo_newhigh/granville_oshime/granville_rebound｜🔥絶好調｜⚪妥当｜PASS｜2389｜💰23.9万円｜momentum 2406 SL2260.7・⏸位置不適(25MA下 -9.63%)（乖離0.7%）｜📋カルテ窓 12/11(残14営業日) ⚠市場に劣後 RS20 -5.9pt｜📈不一致
  > 📌【業態】ITコンサルティング、ビジネスコンサルティングやNotionサービスの提供などを手掛ける。
  > 📌【いま】終値2,389円・直近5日-8.26%（材料未確認）
  > 📌【調子】🔥絶好調（9/13）— ⚠進捗遅れ
  > 📌【水準】⚪妥当（4.0/7）— PER24.16倍・PEG0.354・52週70.3% ／ 💰単元23.9万円
  > 📌【戦略】当日高値超えの逆指値2406円で順張り参戦を検討。上限2430.1円・SL2260.7円目安
- 6238 フリュー｜kenmo_newhigh｜⚡好調｜🟡やや割高｜PASS｜1725｜💰17.2万円｜momentum 1730 SL1625.3・✅即時可（乖離0.3%）｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明 📐進捗 遅れ -10.1%｜📈合致
  > 📌【業態】プリントシール機、開発・販売で圧倒的。関連の消耗品や有料アプリ会員が拡大。
  > 📌【いま】終値1,725円・直近5日+14.62%（材料未確認）
  > 📌【調子】⚡好調（6/13）— ⚠進捗遅れ
  > 📌【水準】🟡やや割高（2.0/7）— PER18.27倍・PEG0.864・52週99.4% ／ 💰単元17.2万円
  > 📌【戦略】当日高値超えの逆指値1730円で順張り参戦を検討。上限1747.3円・SL1625.3円目安
- 4379 Photosynth inc.｜kenmo_newhigh｜✅順調｜🟡やや割高｜PASS_DOJI｜416｜💰4.2万円｜⛔提案なし(指名鮮度切れ 20営業日)｜⚠日程不明｜📈不一致
  > 📌【業態】IoT関連機器や「Akerun入退室管理システム」など展開。住宅向け市場も注力。
  > 📌【いま】終値416円・直近5日-8.17%（材料未確認）
  > 📌【調子】✅順調（4/13）— 質注意
  > 📌【水準】🟡やや割高（2.0/7）— PER21.78倍・PEG8.494・52週37.9% ／ 💰単元4.2万円
  > 📌【戦略】発注対象外（⛔提案なし(指名鮮度切れ 20営業日)）
- 9204 Skymark Airlines Inc.｜kenmo_newhigh｜🔻悪化｜🔴過熱｜PASS｜524｜💰5.2万円｜⛔提案なし(指名鮮度切れ 12営業日)｜⚠日程不明 ⚠業績基調が下向き（🔻悪化）｜📈合致
  > 📌【業態】国内第3位の航空会社。割安運賃で旅客の輸送サービスを手掛ける。
  > 📌【いま】終値524円・直近5日+6.94%（材料未確認）
  > 📌【調子】🔻悪化（3/13）— 質注意
  > 📌【水準】🔴過熱（0.0/7）— PER39.40倍・PEG—・52週99.5% ／ 💰単元5.2万円
  > 📌【戦略】発注対象外（⛔提案なし(指名鮮度切れ 12営業日)）
- 1960 サンテック｜kenmo_newhigh｜➖横ばい｜🔴過熱｜FAIL_INSEN｜1641｜💰16.4万円｜⚠日程不明｜📈レンジ
- 4933 I-ne CO., LTD.｜kenmo_newhigh｜取得不可｜⚪妥当｜FAIL_INSEN｜2466｜💰24.7万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚡材料後出し ⚠日程不明｜📈合致
- 6278 ユニオンツール｜choruko_reversal｜🚀確変｜🟢値頃｜FAIL_INSEN｜9550｜💰95.5万円｜⚠日程不明｜📈不一致（長期下向き）
- 5711 三菱マテリアル｜choruko_reversal｜🚀確変｜💎割安｜FAIL_INSEN｜3512｜💰35.1万円｜⚠日程不明｜📈不一致（長期下向き）
- 6481 THK Co., Ltd.｜choruko_reversal｜🚀確変｜💎割安｜FAIL_INSEN｜4249｜💰42.5万円｜⚠日程不明｜📈合致
- 3036 アルコニックス｜choruko_reversal｜🚀確変｜🟢値頃｜FAIL_INSEN｜2802｜💰28.0万円｜⚠日程不明｜📈不一致
- 7995 Valqua Ltd.｜choruko_reversal/granville_rebound｜🚀確変｜🟢値頃｜FAIL_INSEN｜5460｜💰54.6万円｜⚠日程不明｜📈不一致
- 6516 Sanyo Denki Co., Ltd.｜choruko_reversal/ai_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜4195｜💰42.0万円｜⚠日程不明｜📈不一致
- 8336 Musashino Bank, Ltd.｜choruko_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜2254｜💰22.5万円｜⚠日程不明｜📈合致
- 5344 MARUWA CO., LTD.｜choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜37660｜💰376.6万円｜⚠日程不明｜📈不一致（長期下向き）
- 9107 Kawasaki Kisen Kaisha, Ltd.｜choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜3000｜💰30.0万円｜⚠日程不明｜📈不一致
- 4216 ASAHI YUKIZAI CORPORATION｜choruko_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜4890｜💰48.9万円｜⚠日程不明｜📈不一致（長期下向き）
- 4471 三洋化成工業｜choruko_reversal/granville_oshime/granville_rebound｜🔥絶好調｜💎割安｜FAIL_INSEN｜1347｜💰13.5万円｜⚠日程不明｜📈レンジ
- 5703 日本軽金属ホールディングス（日軽金ＨＤ）｜choruko_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜2300｜💰23.0万円｜⚠日程不明｜📈不一致（長期下向き）
- 6135 牧野フライス製作所｜choruko_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜2520｜💰25.2万円｜⚠日程不明｜📈合致
- 6652 IDEC Corporation｜choruko_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜2905｜💰29.1万円｜⚠日程不明｜📈合致
- 167A リョーサン菱洋ホールディングス（リョー菱ＨＤ）｜choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜2986｜💰29.9万円｜⚠日程不明｜📈不一致（長期下向き）
- 5301 Tokai Carbon Co., Ltd.｜choruko_reversal/granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1408｜💰14.1万円｜⚠日程不明｜📈合致
- 6588 東芝テック｜choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜2415｜💰24.1万円｜⚠日程不明｜📈不一致（長期下向き）
- 6724 セイコーエプソン｜choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜2580.5｜💰25.8万円｜⚠日程不明｜📈合致
- 6925 Ushio Inc.｜choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜2739｜💰27.4万円｜⚡材料後出し ⚠日程不明｜📈不一致
- 6474 Nachi-Fujikoshi Corp.｜choruko_reversal｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜4495｜💰45.0万円｜⚠日程不明｜📈不一致（長期下向き）
- 6914 OPTEX GROUP Company Limited｜choruko_reversal｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜2657｜💰26.6万円｜⚠日程不明｜📈合致
- 6952 カシオ｜choruko_reversal｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜1968｜💰19.7万円｜⚠日程不明｜📈不一致
- 6875 メガチップス｜choruko_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜8240｜💰82.4万円｜⚡材料後出し ⚠日程不明｜📈不一致（長期下向き）
- 3106 倉敷紡績｜choruko_reversal/granville_oshime｜🔥絶好調｜💎割安｜FAIL_INSEN｜1937｜💰19.4万円｜⚠日程不明｜📈レンジ
- 6471 日本精工｜choruko_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜892.5｜💰8.9万円｜⚡材料後出し ⚠日程不明｜📈不一致（長期下向き）
- 8084 ＲＹＯＤＥＮ｜choruko_reversal/granville_rebound｜🔥絶好調｜💎割安｜FAIL_INSEN｜2064｜💰20.6万円｜⚠日程不明｜📈合致
- 7731 ニコン｜choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1477.5｜💰14.8万円｜⚠日程不明｜📈不一致（長期下向き）
- 9902 Nichiden Corporation｜choruko_reversal/granville_oshime｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜2800｜💰28.0万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈不一致
- 4088 Air Water Inc.｜choruko_reversal｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜3010｜💰30.1万円｜⚠日程不明｜📈レンジ
- 8133 伊藤忠エネクス｜choruko_reversal｜🔥絶好調｜🟡やや割高｜FAIL_INSEN｜1960｜💰19.6万円｜⚠日程不明｜📈不一致（長期下向き）
- 5333 ＮＧＫ｜choruko_reversal/ai_reversal｜⚡好調｜💎割安｜FAIL_INSEN｜4170｜💰41.7万円｜⚡材料後出し ⚠日程不明｜📈レンジ
- 6036 ＫｅｅＰｅｒ技研｜choruko_reversal/granville_oshime/granville_rebound｜⚡好調｜💎割安｜FAIL_INSEN｜1605｜💰16.1万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚡材料後出し ⚠日程不明 🎯2手法一致｜📈レンジ
- 8154 加賀電子｜choruko_reversal/stf_kakuhen/granville_oshime/granville_rebound｜⚡好調｜💎割安｜FAIL_INSEN｜4655｜💰46.5万円｜⚠日程不明｜📈レンジ
- 4401 ＡＤＥＫＡ｜choruko_reversal/granville_tenkan｜⚡好調｜🟢値頃｜FAIL_INSEN｜3884｜💰38.8万円｜⚠日程不明｜📈不一致（長期下向き）
- 5186 ニッタ｜choruko_reversal/granville_rebound｜⚡好調｜🟢値頃｜FAIL_INSEN｜6000｜💰60.0万円｜⚠日程不明 🎯2手法一致｜📈合致
- 6268 ナブテスコ｜choruko_reversal｜⚡好調｜🟢値頃｜FAIL_INSEN｜3105｜💰31.1万円｜⚠日程不明｜📈不一致（長期下向き）
- 6448 ブラザー工業（ブラザー）｜choruko_reversal｜⚡好調｜🟢値頃｜FAIL_INSEN｜4129｜💰41.3万円｜⚠日程不明｜📈レンジ
- 4634 ａｒｔｉｅｎｃｅ（ａｒｔｉｅｎ）｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜4765｜💰47.6万円｜⚠日程不明｜📈レンジ
- 3116 Toyota Boshoku Corp.｜choruko_reversal/sr_universe｜⚡好調｜💎割安｜FAIL_INSEN｜2002｜💰20.0万円｜⚠日程不明｜📈不一致（長期下向き）
- 5331 ノリタケ｜choruko_reversal/ai_reversal｜⚡好調｜💎割安｜FAIL_INSEN｜2697｜💰27.0万円｜⚠日程不明｜📈不一致（長期下向き）
- 7004 Kanadevia Corporation｜choruko_reversal｜⚠減速｜💎割安｜FAIL_INSEN｜901｜💰9.0万円｜⚠日程不明｜📈不一致（長期下向き）
- 4205 Zeon Corporation｜choruko_reversal｜⚡好調｜💎割安｜FAIL_INSEN｜1914.5｜💰19.1万円｜⚠日程不明｜📈不一致
- 6651 NITTO KOGYO Corporation｜choruko_reversal｜⚡好調｜💎割安｜FAIL_INSEN｜3945｜💰39.5万円｜⚠日程不明｜📈不一致（長期下向き）
- 4206 アイカ工業｜choruko_reversal/granville_oshime｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜4072｜💰40.7万円｜⚠日程不明｜📈不一致
- 4966 上村工業｜choruko_reversal｜⚡好調｜🟢値頃｜FAIL_INSEN｜14590｜💰145.9万円｜📑TOPIX新規採用（2026-10-30 組入） ⚠日程不明｜📈不一致（長期下向き）
- 5463 丸一鋼管（丸一管）｜choruko_reversal｜⚡好調｜🟢値頃｜FAIL_INSEN｜1585.5｜💰15.9万円｜⚠日程不明｜📈レンジ
- 6250 Yamabiko Corporation｜choruko_reversal/granville_oshime｜⚡好調｜🟢値頃｜FAIL_INSEN｜3385｜💰33.9万円｜⚡材料後出し ⚠日程不明｜📈合致
- 6473 ジェイテクト｜choruko_reversal｜⚠減速｜🟢値頃｜FAIL_INSEN｜1858.5｜💰18.6万円｜⚠日程不明｜📈レンジ
- 3569 セーレン｜choruko_reversal/granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜3405｜💰34.0万円｜⚠日程不明｜📈レンジ
- 9037 Hamakyorex Co., Ltd.｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜1615｜💰16.1万円｜⚠日程不明｜📈不一致（長期下向き）
- 268A Rigaku Holdings Corporation｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜1231｜💰12.3万円｜⚠日程不明｜📈不一致
- 5444 大和工業｜choruko_reversal｜⚡好調｜💎割安｜FAIL_INSEN｜10545｜💰105.5万円｜⚠日程不明｜📈不一致（長期下向き）
- 1968 Taihei Dengyo Kaisha, Ltd.｜choruko_reversal｜⚡好調｜🟢値頃｜FAIL_INSEN｜2122｜💰21.2万円｜⚠日程不明｜📈不一致（長期下向き）
- 9934 因幡電機産業｜choruko_reversal｜⚡好調｜🟢値頃｜FAIL_INSEN｜2496.5｜💰25.0万円｜⚠日程不明｜📈不一致（長期下向き）
- 6432 Takeuchi Mfg.Co., Ltd.｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜6850｜💰68.5万円｜⚠日程不明｜📈レンジ
- 9960 トーテック｜choruko_reversal/ai_momentum/ai_reversal/granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜4000｜💰40.0万円｜⚠日程不明｜📈レンジ
- 1721 コムシスホールディングス｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜5123｜💰51.2万円｜⚡材料後出し ⚠日程不明｜📈不一致
- 1926 ライト工業（ライト）｜choruko_reversal｜⚡好調｜⚪妥当｜PASS_DOJI｜958｜💰9.6万円｜⛔提案なし(材料後出し)｜⚡材料後出し ⚠日程不明 📐進捗 上振れ 26.9%｜📈不一致
  > 📌【業態】法面吹付け工事大手。地盤改良・薬液注入工事に強み。耐震補強に注力。
  > 📌【いま】終値958円・直近5日-7.88%・📌その他重要開示[Updated] Consolidated Financial Results for the Six Months Ended September 30, 2026
  > 📌【調子】⚡好調（5/13）— ⚠減速
  > 📌【水準】⚪妥当（3.0/7）— PER12.59倍・PEG4.569・52週53.4% ／ 💰単元9.6万円
  > 📌【戦略】発注対象外（⛔提案なし(材料後出し)）
- 4403 日油｜choruko_reversal/granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜2469.5｜💰24.7万円｜⚠日程不明｜📈レンジ
- 9072 NIKKON Holdings Co., Ltd.｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜4010｜💰40.1万円｜⚠日程不明｜📈不一致
- 6454 マックス｜choruko_reversal｜⚡好調｜🟡やや割高｜FAIL_INSEN｜1754｜💰17.5万円｜⚠日程不明｜📈レンジ
- 9302 三井倉庫ホールディングス｜choruko_reversal｜⚡好調｜🟡やや割高｜FAIL_UWAHIGE｜3199｜💰32.0万円｜⚠日程不明｜📈不一致（長期下向き）
- 6845 アズビル｜choruko_reversal｜⚡好調｜🔴過熱｜FAIL_INSEN｜1464.5｜💰14.6万円｜⚠日程不明｜📈レンジ
- 6340 澁谷工業｜choruko_reversal/granville_oshime/granville_rebound｜✅順調｜🟢値頃｜FAIL_INSEN｜4415｜💰44.1万円｜⚠日程不明｜📈合致
- 6674 ジーエス・ユアサ　コーポレーション｜choruko_reversal｜✅順調｜🟢値頃｜FAIL_INSEN｜3862｜💰38.6万円｜⚠日程不明｜📈合致
- 8395 佐賀銀行｜choruko_reversal/granville_oshime/granville_rebound｜⚠減速｜🟢値頃｜FAIL_INSEN｜5290｜💰52.9万円｜⚠日程不明｜📈合致
- 1663 K&O Energy Group, Inc.｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜1682｜💰16.8万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈不一致（長期下向き）
- 6923 Stanley Electric Co., Ltd.｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜3015｜💰30.1万円｜⚠日程不明｜📈不一致
- 3445 RS Technologies Co. Ltd.｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜3750｜💰37.5万円｜⚠日程不明｜📈不一致
- 4021 Nissan Chemical Corporation｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜6471｜💰64.7万円｜⚠日程不明｜📈合致
- 4042 東ソー｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜2354｜💰23.5万円｜⚠日程不明｜📈不一致（長期下向き）
- 5021 コスモＨＤ｜choruko_reversal｜🔻悪化｜⚪妥当｜FAIL_INSEN｜3217｜💰32.2万円｜⚠日程不明｜📈不一致（長期下向き）
- 6055 Japan Material Co., Ltd.｜choruko_reversal/ai_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜1450｜💰14.5万円｜⚠日程不明｜📈不一致（長期下向き）
- 7276 Koito Manufacturing Co., Ltd.｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜2385.5｜💰23.9万円｜⚠日程不明｜📈レンジ
- 6750 エレコム｜choruko_reversal｜✅順調｜🟡やや割高｜FAIL_INSEN｜1889｜💰18.9万円｜⚠日程不明｜📈不一致
- 4768 OTSUKA CORPORATION｜choruko_reversal/granville_rebound｜✅順調｜🔴過熱｜FAIL_UWAHIGE｜3867｜💰38.7万円｜⚠日程不明｜📈不一致
- 6277 Hosokawa Micron Corporation｜choruko_reversal｜✅順調｜🔴過熱｜FAIL_INSEN｜5390｜💰53.9万円｜⚡材料後出し ⚠日程不明｜📈不一致（長期下向き）
- 6332 月島ホールディングス｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜2115｜💰21.1万円｜⚠日程不明｜📈不一致（長期下向き）
- 6368 Organo Corp.｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜1494.5｜💰14.9万円｜⚠日程不明｜📈不一致（長期下向き）
- 1951 エクシオグループ（エクシオＧ）｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_UWAHIGE｜2308｜💰23.1万円｜⚠日程不明｜📈不一致（長期下向き）
- 1963 日揮ホールディングス｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜1934.5｜💰19.3万円｜⚠日程不明｜📈不一致
- 3105 日清紡ホールディングス｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜1743｜💰17.4万円｜⚠日程不明｜📈合致
- 4028 石原産業｜choruko_reversal｜🔻悪化｜⚪妥当｜FAIL_INSEN｜2412｜💰24.1万円｜⚠日程不明｜📈不一致（長期下向き）
- 5602 栗本鐵工所（栗本鉄）｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜1389｜💰13.9万円｜⚠日程不明｜📈不一致（長期下向き）
- 6804 ホシデン｜choruko_reversal｜🔻悪化｜⚪妥当｜FAIL_INSEN｜2056｜💰20.6万円｜📈不一致（長期下向き）
- 5201 AGC Inc.｜choruko_reversal｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜4504｜💰45.0万円｜⚠日程不明｜📈不一致（長期下向き）
- 5310 Toyo Tanso Co., Ltd.｜choruko_reversal/ai_reversal｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜5540｜💰55.4万円｜⚡材料後出し ⚠日程不明｜📈不一致
- 6741 日本信号｜choruko_reversal｜✅順調｜🟡やや割高｜FAIL_INSEN｜1536｜💰15.4万円｜⚠日程不明｜📈合致
- 6807 Japan Aviation Electronics Industry, Limited｜choruko_reversal｜✅順調｜🟡やや割高｜FAIL_INSEN｜2187｜💰21.9万円｜⚠日程不明｜📈不一致（長期下向き）
- 7220 Musashi Seimitsu Industry Co., Ltd.｜choruko_reversal｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜1853｜💰18.5万円｜⚠日程不明｜📈不一致（長期下向き）
- 4902 Konica Minolta, Inc.｜choruko_reversal/granville_tenkan｜➖横ばい｜💎割安｜FAIL_INSEN｜514｜💰5.1万円｜⚠日程不明｜📈不一致（長期下向き）
- 6479 ミネベア｜choruko_reversal｜➖横ばい｜💎割安｜FAIL_INSEN｜2637｜💰26.4万円｜⚡材料後出し ⚠日程不明｜📈不一致（長期下向き）
- 1979 大気社｜choruko_reversal｜➖横ばい｜⚪妥当｜FAIL_INSEN｜3240｜💰32.4万円｜⚠日程不明｜📈不一致（長期下向き）
- 4008 住友精化｜choruko_reversal｜🔻悪化｜⚪妥当｜FAIL_INSEN｜1270｜💰12.7万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈合致
- 4061 Denka Co., Ltd.｜choruko_reversal｜➖横ばい｜🔴過熱｜FAIL_INSEN｜2619｜💰26.2万円｜⚠日程不明｜📈不一致（長期下向き）
- 9468 カドカワ｜choruko_reversal｜➖横ばい｜🔴過熱｜FAIL_INSEN｜3404｜💰34.0万円｜📈レンジ
- 6632 JVCKENWOOD Corporation｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜757｜💰7.6万円｜⚠日程不明｜📈不一致（長期下向き）
- 4746 東計電算｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_UWAHIGE｜1705｜💰17.1万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈合致
- 4980 Dexerials Corp.｜choruko_reversal/ai_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜1850｜💰18.5万円｜⚠日程不明｜📈不一致（長期下向き）
- 9722 藤田観光｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜2622｜💰26.2万円｜⚠日程不明｜📈合致
- 6370 栗田工業｜choruko_reversal｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜5159｜💰51.6万円｜⚠日程不明｜📈不一致（長期下向き）
- 6436 アマノ｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜3531｜💰35.3万円｜⚠日程不明｜📈不一致（長期下向き）
- 8508 J Trust Co., Ltd.｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜619｜💰6.2万円｜📑TOPIX新規採用（2026-10-30 組入） ⚠日程不明｜📈レンジ
- 9301 三菱倉｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜1223｜💰12.2万円｜⚠日程不明｜📈不一致（長期下向き）
- 1662 Japan Petroleum Exploration Co., Ltd.｜choruko_reversal｜🔻悪化｜⚪妥当｜PASS_DOJI｜1467｜💰14.7万円｜⛔型不一致(十字線: トウバ)｜⚠業績基調が下向き（🔻悪化）｜📈不一致（長期下向き）
  > 📌【業態】資源開発大手。原油・天然ガスの探鉱、開発、生産。国内で天然ガス・インフラ事業。
  > 📌【いま】終値1,467円・直近5日-8.83%（材料未確認）
  > 📌【調子】🔻悪化（0/13）— 減収・質注意
  > 📌【水準】⚪妥当（4.0/7）— PER5.78倍・PEG—・52週8.8% ／ 💰単元14.7万円
  > 📌【戦略】発注対象外（⛔型不一致(十字線: トウバ)）
- 7148 Financial Products Group Co., Ltd.｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜1299｜💰13.0万円｜⚠日程不明｜📈不一致（長期下向き）
- 6379 レイズネク｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜909｜💰9.1万円｜⚠日程不明｜📈レンジ
- 7278 Exedy Corporation｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜5100｜💰51.0万円｜⚠日程不明｜📈不一致（長期下向き）
- 2109 ＤＭ三井製糖｜choruko_reversal｜⚠減速｜🟡やや割高｜PASS｜3585｜💰35.9万円｜⛔提案なし(指名鮮度切れ 12営業日)｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明 ⚠業績基調が下向き（⚠減速）｜📈レンジ
  > 📌【業態】精糖最大手「スプーン印」三井糖と「ばら印」大日明治が統合。食品化学も注力。
  > 📌【いま】終値3,585円・直近5日-1.10%（材料未確認）
  > 📌【調子】⚠減速（0/13）— ⚠減速
  > 📌【水準】🟡やや割高（2.0/7）— PER14.48倍・PEG30.515・52週56.5% ／ 💰単元35.9万円
  > 📌【戦略】発注対象外（⛔提案なし(指名鮮度切れ 12営業日)）
- 6349 Komori Corporation｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜1604｜💰16.0万円｜⚠日程不明｜📈合致
- 3612 WORLD CO.,LTD.｜choruko_reversal｜業績データ取得不可(経常益予想非開示)｜💎割安｜FAIL_INSEN｜1435｜💰14.3万円｜⚡材料後出し ⚠日程不明｜📈不一致（長期下向き）
- 6810 Maxell, Ltd.｜choruko_reversal/granville_oshime/granville_rebound｜業績データ取得不可(経常益予想非開示)｜💎割安｜FAIL_INSEN｜1968｜💰19.7万円｜⚠日程不明｜📈不一致（長期下向き）
- 7322 三十三フィナンシャルグループ｜choruko_reversal/granville_rebound｜取得不可｜💎割安｜FAIL_INSEN｜1546｜💰15.5万円｜⚠日程不明｜📈合致
- 8366 滋賀銀行｜choruko_reversal/granville_rebound｜取得不可｜💎割安｜FAIL_INSEN｜1926.5｜💰19.3万円｜⚠日程不明｜📈合致
- 8975 Ichigo Office REIT Investment Corporation｜choruko_reversal｜判定保留(変則決算)｜🟢値頃｜FAIL_INSEN｜88200｜💰8.8万円｜📋カルテ窓 12/16(残17営業日)｜📈レンジ
- 4293 セプテーニ・ホールディングス（セプテニＨＤ）｜choruko_reversal｜取得不可｜🟢値頃｜FAIL_INSEN｜431｜💰4.3万円｜⚠日程不明｜📈不一致（長期下向き）
- 5101 Yokohama Rubber Co., Ltd.｜choruko_reversal｜取得不可｜🟢値頃｜FAIL_INSEN｜6814｜💰68.1万円｜⚠日程不明｜📈不一致
- 6141 DMG MORI CO., LTD.｜choruko_reversal｜取得不可｜🟢値頃｜FAIL_INSEN｜2361.5｜💰23.6万円｜⚠日程不明｜📈不一致（長期下向き）
- 7157 Lifenet Insurance Company｜choruko_reversal｜業績データ取得不可(経常益予想非開示)｜🟢値頃｜FAIL_INSEN｜1251｜💰12.5万円｜⚠日程不明｜📈不一致（長期下向き）
- 7167 めぶきフィナンシャルグループ｜choruko_reversal/granville_rebound｜取得不可｜🟢値頃｜FAIL_INSEN｜1355.5｜💰13.6万円｜⚠日程不明｜📈不一致
- 7186 横浜フィナンシャルグループ｜choruko_reversal｜取得不可｜🟢値頃｜FAIL_INSEN｜1543.5｜💰15.4万円｜⚠日程不明｜📈不一致
- 8343 Akita Bank, Ltd.｜choruko_reversal｜業績データ取得不可(売上/経常欠損)｜🟢値頃｜FAIL_INSEN｜1220｜💰12.2万円｜📈合致
- 8354 ふくおかフィナンシャルグループ｜choruko_reversal｜業績データ取得不可(売上/経常欠損)｜🟢値頃｜FAIL_INSEN｜6462｜💰64.6万円｜⚠日程不明｜📈不一致
- 8359 Hachijuni Nagano Bank, Ltd.｜choruko_reversal/granville_rebound｜業績データ取得不可(売上/経常欠損)｜🟢値頃｜FAIL_INSEN｜2159｜💰21.6万円｜⚠日程不明｜📈不一致
- 8370 紀陽銀行｜choruko_reversal｜業績データ取得不可(売上/経常欠損)｜🟢値頃｜FAIL_INSEN｜1347｜💰13.5万円｜⚠日程不明｜📈合致
- 8334 Gunma Bank, Ltd.｜choruko_reversal/granville_rebound｜業績データ取得不可(売上/経常欠損)｜⚪妥当｜FAIL_INSEN｜2276｜💰22.8万円｜⚡材料後出し ⚠日程不明｜📈不一致
- 8600 トモニホールディングス｜choruko_reversal｜取得不可｜⚪妥当｜FAIL_INSEN｜879｜💰8.8万円｜⚠日程不明｜📈合致
- 8032 紙パル商｜choruko_reversal｜取得不可｜🟡やや割高｜FAIL_INSEN｜1100｜💰11.0万円｜⚠日程不明｜📈合致
- 4043 Tokuyama Corporation｜choruko_reversal｜—｜—｜FAIL_INSEN｜3335｜💰—｜⚠日程不明｜📈不一致（長期下向き）
- 4095 Nihon Parkerizing Co., Ltd.｜choruko_reversal｜—｜—｜FAIL_INSEN｜1644｜💰—｜⚠日程不明｜📈不一致
- 4188 三菱ケミカルグループ｜choruko_reversal/sr_universe｜—｜—｜FAIL_INSEN｜988.8｜💰—｜⚠日程不明｜📈レンジ
- 4633 Sakata Inx Corp.｜choruko_reversal｜—｜—｜FAIL_INSEN｜2434｜💰—｜⚠日程不明｜📈不一致
- 4975 JCU Corporation｜choruko_reversal｜—｜—｜FAIL_INSEN｜4660｜💰—｜⚠日程不明｜📈不一致（長期下向き）
- 5019 出光興産｜choruko_reversal｜取得不可｜⏸判定不能｜FAIL_INSEN｜1154.5｜💰11.5万円｜⚠日程不明｜📈不一致（長期下向き）
- 7177 ＧＭＯフィナンシャルホールディングス｜choruko_reversal｜取得不可｜⏸判定不能｜FAIL_INSEN｜996｜💰10.0万円｜⚠日程不明｜📈不一致
- 8616 Tokai Tokyo Financial Holdings, Inc.｜choruko_reversal｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜708｜💰7.1万円｜⚠日程不明｜📈不一致
- 8698 Monex Group, Inc.｜choruko_reversal｜業績データ取得不可(経常益予想非開示)｜⏸判定不能｜FAIL_INSEN｜550｜💰5.5万円｜⚠日程不明｜📈不一致（長期下向き）
- 9303 Sumitomo Warehouse Co., Ltd.｜choruko_reversal｜—｜—｜FAIL_INSEN｜3845｜💰—｜⚠日程不明｜📈不一致
- 3131 Shinden Hightex Corp.｜stf_kakuhen/ai_reversal/granville_oshime/granville_rebound｜🚀確変｜💎割安｜FAIL_INSEN｜6100｜💰61.0万円｜⚠日程不明｜📈不一致
- 9308 乾汽船｜stf_kakuhen/granville_oshime/changepoint/changepoint🔔🔔｜🚀確変｜🟢値頃｜FAIL_INSEN｜2050｜💰20.5万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈レンジ
- 6969 松尾電機｜stf_kakuhen｜🔥絶好調｜💎割安｜FAIL_INSEN｜1083｜💰10.8万円｜📈レンジ
- 5832 ちゅうぎんフィナンシャルグループ（ちゅうぎんＦ）｜stf_kakuhen｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜3162｜💰31.6万円｜⚠日程不明｜📈不一致
- 3205 ダイドー｜stf_kakuhen｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜734｜💰7.3万円｜⚠日程不明｜📈レンジ
- 4410 ハリマ化成グループ（ハリマ化成Ｇ）｜stf_kakuhen｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1200｜💰12.0万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈不一致
- 4180 Appier Group, Inc.｜stf_kakuhen/granville_oshime｜🔥絶好調｜⚪妥当｜PASS_DOJI｜1371｜💰13.7万円｜momentum 1401 SL1342・⏳確認足待ち｜⚠日程不明｜📈レンジ
  > 📌【業態】企業の販促など経営課題の解決を支援するAI搭載のプラットフォームを提供。
  > 📌【いま】終値1,371円・直近5日-5.51%（材料未確認）
  > 📌【調子】🔥絶好調（10/13）— ⚠減速
  > 📌【水準】⚪妥当（4.0/7）— PER28.04倍・PEG0.295・52週68.4% ／ 💰単元13.7万円
  > 📌【戦略】当日高値超えの逆指値1401円で順張り参戦を検討。上限1415円・SL1342円目安
- 5246 ＥＬＥＭＥＮＴＳ｜stf_kakuhen/granville_oshime/granville_rebound｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜756｜💰7.6万円｜⚠日程不明｜📈不一致
- 7942 ＪＳＰ｜stf_kakuhen｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜2887｜💰28.9万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈レンジ
- 9962 ミスミグループ本社（ミスミＧ）｜stf_kakuhen｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜3416｜💰34.2万円｜⚠日程不明｜📈レンジ
- 3498 霞ヶ関Ｃ｜stf_kakuhen/granville_tenkan｜🔥絶好調｜💎割安｜FAIL_INSEN｜6190｜💰61.9万円｜⚠日程不明｜📈レンジ
- 9110 ＮＳユナイテッド海運（ユナイテド海）｜stf_kakuhen｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜10540｜💰105.4万円｜⚠日程不明｜📈合致
- 3994 マネーフォワード｜stf_kakuhen/sr_reversal/changepoint🔔🔔/changepoint🔔/changepoint/sr_universe｜🔥絶好調｜🔴過熱｜FAIL_INSEN｜6314｜💰63.1万円｜⚠日程不明｜📈不一致
- 9766 コナミグループ（コナミＧ）｜stf_kakuhen｜🔥絶好調｜🟡やや割高｜FAIL_INSEN｜29735｜💰297.4万円｜⚠日程不明｜📈合致
- 6850 チノー｜stf_kakuhen｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜1753｜💰17.5万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈レンジ
- 2331 ＡＬＳＯＫ｜stf_kakuhen｜⚡好調｜⚪妥当｜PASS｜1376.5｜💰13.8万円｜⛔提案なし(手法ブランチ不明)｜⚠日程不明 📐進捗 上振れ 15.6%｜📈合致
  > 📌【業態】警備サービス大手。機械警備が主力。現金輸送に強み。介護・高齢者向け注力。
  > 📌【いま】終値1,376.5円・直近5日+1.89%（材料未確認）
  > 📌【調子】⚡好調（7/13）
  > 📌【水準】⚪妥当（4.0/7）— PER12.61倍・PEG0.379・52週98.5% ／ 💰単元13.8万円
  > 📌【戦略】発注対象外（⛔提案なし(手法ブランチ不明)）
- 4503 アステラス製薬（アステラス）｜stf_kakuhen｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜2751.5｜💰27.5万円｜⚠日程不明｜📈合致
- 6758 ソニーグループ｜stf_kakuhen/ai_momentum｜⚡好調｜⚪妥当｜FAIL_INSEN｜4312｜💰43.1万円｜⚠日程不明｜📈合致
- 3091 ブロンコビリー｜stf_kakuhen/dm_reversal｜⚡好調｜🟡やや割高｜FAIL_INSEN｜2990｜💰29.9万円｜⚠日程不明｜📈不一致
- 1980 ダイダン｜stf_kakuhen｜⚡好調｜🟢値頃｜FAIL_INSEN｜2859｜💰28.6万円｜⚠日程不明｜📈レンジ
- 3479 ＴＫＰ｜stf_kakuhen/granville_tenkan｜⚡好調｜🔴過熱｜FAIL_INSEN｜1941｜💰19.4万円｜⚡材料後出し ⚠日程不明｜📈不一致
- 4417 グローバルセキュリティエキスパート（Ｇセキュリ）｜stf_kakuhen｜⚡好調｜🔴過熱｜FAIL_INSEN｜8480｜💰84.8万円｜⚠日程不明｜📈合致
- 6016 ジャパンエンジン｜stf_kakuhen｜⚡好調｜⚪妥当｜FAIL_INSEN｜9030｜💰90.3万円｜⚠日程不明｜📈レンジ
- 7747 朝日インテック｜stf_kakuhen/granville_tenkan｜⚡好調｜🔴過熱｜FAIL_UWAHIGE｜4348｜💰43.5万円｜⚠日程不明｜📈合致
- 7366 ＬＩＴＡＬＩＣＯ（りたりこ）｜stf_kakuhen｜業績データ取得不可(経常益予想非開示)｜⚪妥当｜FAIL_UWAHIGE｜1976｜💰19.8万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈レンジ
- 9434 ソフトバンク｜stf_kakuhen/ai_reversal/sr_universe｜取得不可｜⚪妥当｜FAIL_INSEN｜244.1｜💰2.4万円｜⚠日程不明｜📈レンジ
- 3932 アカツキ｜stf_kakuhen｜—｜⏸判定不能｜FAIL_INSEN｜1375｜💰13.8万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈合致
- 9048 名古屋鉄道｜value_gap｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜1974.5｜💰19.7万円｜⚠日程不明｜📈不一致

## グランビル銘柄
- 6768 Tamura Corporation｜granville_tenkan/granville_oshime｜🔥絶好調｜💎割安｜FAIL_INSEN｜626｜💰6.3万円｜⚠日程不明｜📈不一致
- 3927 アークン｜granville_tenkan｜🔥絶好調｜💎割安｜FAIL_INSEN｜775｜💰7.8万円｜📈レンジ
- 9279 GIFT HOLDINGS INC.｜granville_tenkan｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜2418｜💰24.2万円｜📑TOPIX低減対象（次 01/29 第2回/8） 📋カルテ窓 12/15(残16営業日)｜📈不一致
- 8012 Nagase & Co., Ltd.｜granville_tenkan｜🔥絶好調｜💎割安｜FAIL_INSEN｜1055.5｜💰10.6万円｜⚠日程不明｜📈レンジ
- 6744 能美防災｜granville_tenkan｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜4290｜💰42.9万円｜⚠日程不明｜📈不一致
- 3002 グンゼ｜granville_tenkan｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜4255｜💰42.5万円｜⚠日程不明｜📈合致
- 4523 エーザイ｜granville_tenkan｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜5280｜💰52.8万円｜⚠日程不明｜📈レンジ
- 9742 アイネス｜granville_tenkan｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜2351｜💰23.5万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈レンジ
- 3964 オークネット｜granville_tenkan｜⚡好調｜💎割安｜FAIL_INSEN｜1201｜💰12.0万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈レンジ
- 3405 クラレ｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_INSEN｜1748.5｜💰17.5万円｜⚠日程不明｜📈レンジ
- 4534 Mochida Pharmaceutical Co., Ltd.｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜3365｜💰33.6万円｜⚠日程不明｜📈合致
- 9006 Keikyu Corporation｜granville_tenkan｜⚡好調｜🟢値頃｜PASS｜1595.5｜💰16.0万円｜momentum 1601.5 SL1504.5・✅即時可（乖離0.4%）｜⚠日程不明 📐進捗 遅れ -20.6%｜📈レンジ
  > 📌【業態】京浜・三浦半島が地盤。品川・羽田・横浜を核に沿線再開発を推進。
  > 📌【いま】終値1,595.5円・直近5日-2.12%（材料未確認）
  > 📌【調子】⚡好調（7/13）— ⚠進捗遅れ・⚠下期依存
  > 📌【水準】🟢値頃（5.0/7）— PER13.75倍・PEG0.262・52週70.5% ／ 💰単元16.0万円
  > 📌【戦略】当日高値超えの逆指値1601.5円で順張り参戦を検討。上限1617.5円・SL1504.5円目安
- 5532 リアルゲイト｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜2856｜💰28.6万円｜⚠日程不明｜📈レンジ
- 9075 福山通運｜granville_tenkan/granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜6270｜💰62.7万円｜📈レンジ
- 4507 塩野義製薬｜granville_tenkan｜⚡好調｜🟡やや割高｜FAIL_UWAHIGE｜3121｜💰31.2万円｜⚠日程不明｜📈合致
- 3491 ＧＡ　ｔｅｃｈｎｏｌｏｇｉｅｓ（ＧＡテクノ）｜granville_tenkan｜⚡好調｜💎割安｜FAIL_INSEN｜1250｜💰12.5万円｜📋カルテ窓 12/10(残13営業日)｜📈不一致
- 1941 中電工｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_INSEN｜5000｜💰50.0万円｜⚠日程不明｜📈レンジ
- 3496 アズーム｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_INSEN｜3610｜💰36.1万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈不一致
- 2502 Asahi Group Holdings, Ltd.｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜1784｜💰17.8万円｜⚠日程不明｜📈合致
- 4848 Fullcast Holdings Co., Ltd.｜granville_tenkan/granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜1771｜💰17.7万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈レンジ
- 6099 エラン｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜778｜💰7.8万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚡材料後出し ⚠日程不明｜📈レンジ
- 4045 Toagosei Co., Ltd.｜granville_tenkan｜⚡好調｜🟡やや割高｜FAIL_INSEN｜1721｜💰17.2万円｜⚠日程不明｜📈不一致
- 4554 Fuji Pharma Co., Ltd.｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_INSEN｜1717｜💰17.2万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈レンジ
- 9842 アークランズ｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_INSEN｜1928｜💰19.3万円｜⚠日程不明｜📈合致
- 8804 東京建物｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜3267｜💰32.7万円｜⚠日程不明｜📈不一致
- 2206 江崎グリコ｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜5069｜💰50.7万円｜⚠日程不明｜📈レンジ
- 7606 ＴＡＢＡＹＡホールディングス｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜2665｜💰26.6万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈合致
- 8016 オンワード HD｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜783｜💰7.8万円｜⚠日程不明｜📈合致
- 4091 Nippon Sanso Holdings Corporation｜granville_tenkan｜⚡好調｜🟡やや割高｜FAIL_INSEN｜5714｜💰57.1万円｜⚠日程不明｜📈レンジ
- 9513 Electric Power Development Co., Ltd.｜granville_tenkan｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜3873｜💰38.7万円｜⚠日程不明｜📈レンジ
- 9065 Sankyu Inc.｜granville_tenkan｜✅順調｜💎割安｜FAIL_INSEN｜1592.5｜💰15.9万円｜⚡材料後出し ⚠日程不明｜📈不一致
- 4169 Enechange Ltd.｜granville_tenkan｜⚠減速｜⚪妥当｜FAIL_INSEN｜245｜💰2.5万円｜⚠日程不明｜📈レンジ
- 4568 第一三共｜granville_tenkan/sr_universe｜✅順調｜⚪妥当｜FAIL_INSEN｜2707｜💰27.1万円｜⚠日程不明｜📈レンジ
- 1911 Sumitomo Forestry Co., Ltd.｜granville_tenkan｜🔻悪化｜⚪妥当｜FAIL_INSEN｜1092.5｜💰10.9万円｜⚠日程不明｜📈レンジ
- 2488 ＪＴＰ｜granville_tenkan｜✅順調｜🟡やや割高｜PASS_DOJI｜1302｜💰13.0万円｜⛔提案なし(指名鮮度切れ 11営業日)｜⚠日程不明 📐進捗 上振れ 19.5%｜📈レンジ
  > 📌【業態】IT活用支援事業。セキュリティ、AIソフト開発・保守を展開。人材育成コンサルも。
  > 📌【いま】終値1,302円・直近5日-6.60%（材料未確認）
  > 📌【調子】✅順調（4/13）— ⚠減速
  > 📌【水準】🟡やや割高（2.0/7）— PER10.01倍・PEG4.904・52週42.8% ／ 💰単元13.0万円
  > 📌【戦略】発注対象外（⛔提案なし(指名鮮度切れ 11営業日)）
- 417A ブルーゾーンホールディングス｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_INSEN｜1976｜💰19.8万円｜⚠日程不明｜📈合致
- 5184 ニチリン｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_INSEN｜3975｜💰39.8万円｜⚠日程不明｜📈レンジ
- 7269 スズキ｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_UWAHIGE｜2204｜💰22.0万円｜⚠日程不明｜📈レンジ
- 9418 Ｕ－ＮＥＸＴ　ＨＯＬＤＩＮＧＳ｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_UWAHIGE｜1840｜💰18.4万円｜⚠日程不明｜📈レンジ
- 3092 ＺＯＺＯ｜granville_tenkan｜✅順調｜🔴過熱｜FAIL_INSEN｜1198.5｜💰12.0万円｜⚠日程不明｜📈レンジ
- 3549 クスリのアオキホールディングス｜granville_tenkan｜✅順調｜🔴過熱｜FAIL_UWAHIGE｜4917｜💰49.2万円｜⚠日程不明｜📈合致
- 8113 Unicharm Corporation｜granville_tenkan｜✅順調｜🔴過熱｜FAIL_INSEN｜1085.5｜💰10.9万円｜⚠日程不明｜📈合致
- 8160 KISOJI CO., LTD.｜granville_tenkan｜✅順調｜🔴過熱｜FAIL_UWAHIGE｜2593｜💰25.9万円｜⚠日程不明｜📈合致
- 8934 Sun Frontier Fudousan Co., Ltd.｜granville_tenkan｜✅順調｜💎割安｜FAIL_INSEN｜2282｜💰22.8万円｜⚡材料後出し｜📈不一致
- 9163 Nareru Group Inc.｜granville_tenkan｜✅順調｜🟢値頃｜FAIL_INSEN｜1984｜💰19.8万円｜📋カルテ窓 12/15(残16営業日)｜📈不一致
- 8056 ＢＩＰＲＯＧＹ｜granville_tenkan｜✅順調｜⚪妥当｜PASS｜4845｜💰48.5万円｜⛔提案なし(指名鮮度切れ 11営業日)｜⚠日程不明 📐進捗 遅れ -25.7%｜📈レンジ
  > 📌【業態】大日本印刷系の情報システム大手。クラウド事業に注力。金融、流通、空運に強み。
  > 📌【いま】終値4,845円・直近5日-0.72%（材料未確認）
  > 📌【調子】✅順調（3/13）— ⚠進捗遅れ
  > 📌【水準】⚪妥当（4.0/7）— PER14.54倍・PEG1.534・52週37.4% ／ 💰単元48.5万円
  > 📌【戦略】発注対象外（⛔提案なし(指名鮮度切れ 11営業日)）
- 9956 Valor Holdings Co., Ltd.｜granville_tenkan｜✅順調｜⚪妥当｜FAIL_INSEN｜1600｜💰16.0万円｜⚠日程不明｜📈レンジ
- 1925 Daiwa House Industry Co., Ltd.｜granville_tenkan/sr_universe｜🔻悪化｜⚪妥当｜FAIL_INSEN｜2312.5｜💰23.1万円｜⚠日程不明｜📈レンジ
- 6412 Heiwa Holdings Inc.｜granville_tenkan｜✅順調｜⚪妥当｜FAIL_INSEN｜2141｜💰21.4万円｜⚠日程不明｜📈レンジ
- 3563 ＦＯＯＤ　＆　ＬＩＦＥ　ＣＯＭＰＡＮＩＥＳ｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_INSEN｜5951｜💰59.5万円｜⚠日程不明｜📈レンジ
- 4204 Sekisui Chemical Co., Ltd.｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_INSEN｜2569｜💰25.7万円｜⚠日程不明｜📈レンジ
- 4540 Tsumura & Co.｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_INSEN｜3973｜💰39.7万円｜⚠日程不明｜📈レンジ
- 6745 ホーチキ｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_INSEN｜1890｜💰18.9万円｜⚠日程不明｜📈レンジ
- 7181 JAPAN POST INSURANCE Co., Ltd.｜granville_tenkan｜⚠減速｜🔴過熱｜FAIL_INSEN｜1717｜💰17.2万円｜📈レンジ
- 9045 Keihan Holdings Co., Ltd.｜granville_tenkan｜⚠減速｜🟡やや割高｜FAIL_UWAHIGE｜3306｜💰33.1万円｜⚠日程不明｜📈レンジ
- 5423 Tokyo Steel Manufacturing Co., Ltd.｜granville_tenkan｜🔻悪化｜🔴過熱｜FAIL_INSEN｜1705｜💰17.1万円｜⚠日程不明｜📈レンジ
- 2264 Morinaga Milk Industry Co., Ltd.｜granville_tenkan｜➖横ばい｜⚪妥当｜FAIL_INSEN｜1176.5｜💰11.8万円｜⚠日程不明｜📈合致
- 8801 三井不動産｜granville_tenkan/sr_universe｜➖横ばい｜⚪妥当｜FAIL_INSEN｜1542.5｜💰15.4万円｜⚠日程不明｜📈不一致
- 9837 Morito Co., Ltd.｜granville_tenkan｜➖横ばい｜⚪妥当｜FAIL_INSEN｜1786｜💰17.9万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈レンジ
- 6072 ERTH Group Co.,Ltd.｜granville_tenkan｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜922｜💰9.2万円｜📈レンジ
- 5105 ＴＯＹＯ　ＴＩＲＥ｜granville_tenkan｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜3830｜💰38.3万円｜⚠日程不明｜📈レンジ
- 5233 太平洋セメント｜granville_tenkan｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜3672｜💰36.7万円｜⚠日程不明｜📈不一致
- 8803 Heiwa Real Estate Co., Ltd.｜granville_tenkan｜➖横ばい｜🟡やや割高｜FAIL_INSEN｜2351｜💰23.5万円｜⚡材料後出し ⚠日程不明｜📈レンジ
- 9007 Odakyu Electric Railway Co., Ltd.｜granville_tenkan｜➖横ばい｜🟡やや割高｜FAIL_UWAHIGE｜1794｜💰17.9万円｜⚡材料後出し ⚠日程不明｜📈レンジ
- 4528 ONO Pharmaceutical Co., Ltd.｜granville_tenkan｜⚠減速｜🔴過熱｜FAIL_UWAHIGE｜2460｜💰24.6万円｜⚠日程不明｜📈レンジ
- 9869 Kato Sangyo Co., Ltd.｜granville_tenkan/granville_oshime｜➖横ばい｜🔴過熱｜FAIL_UWAHIGE｜6730｜💰67.3万円｜⚠日程不明｜📈レンジ
- 4922 コーセーホールディングス｜granville_tenkan｜➖横ばい｜🔴過熱｜FAIL_INSEN｜5880｜💰58.8万円｜⚠日程不明｜📈レンジ
- 9735 セコム｜granville_tenkan｜➖横ばい｜🔴過熱｜FAIL_UWAHIGE｜7220｜💰72.2万円｜⚠日程不明｜📈合致
- 4912 ライオン｜granville_tenkan｜⚠減速｜⚪妥当｜FAIL_UWAHIGE｜2261｜💰22.6万円｜⚠日程不明｜📈合致
- 9025 Konoike Transport Co., Ltd.｜granville_tenkan｜⚠減速｜⚪妥当｜FAIL_INSEN｜2843｜💰28.4万円｜⚠日程不明｜📈レンジ
- 9404 Nippon Television Holdings, Inc.｜granville_tenkan｜🔻悪化｜⚪妥当｜FAIL_INSEN｜2905.5｜💰29.1万円｜⚠日程不明｜📈レンジ
- 1878 Daito Trust Construction Co., Ltd.｜granville_tenkan｜⚠減速｜🟡やや割高｜FAIL_INSEN｜3221｜💰32.2万円｜⚠日程不明｜📈レンジ
- 1928 積水ハウス｜granville_tenkan/sr_universe｜⚠減速｜🟡やや割高｜FAIL_INSEN｜3431｜💰34.3万円｜📋カルテ窓 12/10(残13営業日)｜📈レンジ
- 8167 リテールパートナーズ｜granville_tenkan｜⚠減速｜🟡やや割高｜FAIL_INSEN｜1374｜💰13.7万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈レンジ
- 9401 東京放送ホールディングス｜granville_tenkan｜⚠減速｜🔴過熱｜FAIL_INSEN｜6304｜💰63.0万円｜⚠日程不明｜📈レンジ
- 3401 Teijin Limited｜granville_tenkan｜業績データ取得不可(経常益予想非開示)｜🟢値頃｜FAIL_INSEN｜1645.5｜💰16.5万円｜⚠日程不明｜📈不一致
- 2897 Nissin Foods Holdings Co., Ltd.｜granville_tenkan｜取得不可｜⚪妥当｜FAIL_INSEN｜2825.5｜💰28.3万円｜⚠日程不明｜📈レンジ
- 3182 オイシックス｜granville_tenkan｜取得不可｜⚪妥当｜FAIL_INSEN｜1743｜💰17.4万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈合致
- 2811 Kagome Co., Ltd.｜granville_tenkan｜業績データ取得不可(経常益予想非開示)｜⚪妥当｜FAIL_UWAHIGE｜2844｜💰28.4万円｜⚠日程不明｜📈合致
- 4543 Terumo Corporation｜granville_tenkan｜業績データ取得不可(経常益予想非開示)｜⚪妥当｜FAIL_INSEN｜2547｜💰25.5万円｜⚠日程不明｜📈レンジ
- 7921 ＴＡＫＡＲＡ　＆　ＣＯＭＰＡＮＹ｜granville_tenkan｜業績データ取得不可(経常益予想非開示)｜⚪妥当｜FAIL_INSEN｜4205｜💰42.0万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈レンジ
- 1938 NIPPON RIETEC CO., LTD.｜granville_tenkan｜—｜—｜FAIL_INSEN｜2517｜💰—｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈レンジ
- 3252 JINUSHI Co.,Ltd.｜granville_tenkan｜—｜—｜FAIL_INSEN｜2766｜💰—｜📑TOPIX低減対象（次 01/29 第2回/8） ⚡材料後出し ⚠日程不明｜📈不一致
- 3402 Toray Industries, Inc.｜granville_tenkan｜—｜—｜FAIL_INSEN｜1290｜💰—｜⚠日程不明｜📈不一致
- 4765 ＳＢＩグローバルアセットマネジメント｜granville_tenkan/granville_oshime｜判定保留｜⏸判定不能｜FAIL_INSEN｜584｜💰5.8万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚡材料後出し ⚠日程不明｜📈レンジ
- 5401 日本製鉄｜granville_tenkan/sr_universe｜—｜—｜FAIL_INSEN｜667｜💰—｜⚠日程不明｜📈不一致
- 5930 Bunka Shutter Co., Ltd.｜granville_tenkan｜—｜—｜FAIL_UWAHIGE｜1901｜💰—｜⚡材料後出し ⚠日程不明｜📈レンジ
- 9143 SG Holdings Co., Ltd.｜granville_tenkan｜—｜—｜FAIL_INSEN｜1586｜💰—｜⚠日程不明｜📈合致
- 9605 Toei Company, Ltd.｜granville_tenkan｜—｜—｜FAIL_INSEN｜6180｜💰—｜⚠日程不明｜📈レンジ
- 6570 Kyowa Corporation Co. Ltd.｜granville_oshime/granville_rebound｜🚀確変｜🟢値頃｜FAIL_INSEN｜2801｜💰28.0万円｜⚠日程不明｜📈レンジ
- 7480 スズデン｜granville_oshime/granville_rebound｜🚀確変｜⚪妥当｜FAIL_INSEN｜3260｜💰32.6万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈不一致
- 6574 コンヴァノ｜granville_oshime｜🚀確変｜🟢値頃｜FAIL_INSEN｜841｜💰8.4万円｜⚠日程不明｜📈レンジ
- 3156 レスター｜granville_oshime/granville_rebound｜🚀確変｜💎割安｜FAIL_INSEN｜3890｜💰38.9万円｜📈不一致
- 9824 Senshu Electric Co., Ltd.｜granville_oshime/granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜6500｜💰65.0万円｜📋カルテ窓 12/08(残11営業日)｜📈レンジ
- 8051 山善｜granville_oshime｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜1833｜💰18.3万円｜⚠日程不明｜📈不一致
- 8137 サンワテクノス｜granville_oshime/granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜3540｜💰35.4万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈不一致
- 4258 AMIYA Corporation｜granville_oshime/granville_rebound｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜5090｜💰50.9万円｜📈レンジ
- 8388 阿波銀行｜granville_oshime/granville_rebound｜🔥絶好調｜💎割安｜FAIL_INSEN｜1649｜💰16.5万円｜⚠日程不明｜📈不一致
- 8392 大分銀行｜granville_oshime/granville_rebound｜🔥絶好調｜💎割安｜FAIL_INSEN｜2277｜💰22.8万円｜⚠日程不明｜📈不一致
- 9304 澁澤倉庫｜granville_oshime｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜1838｜💰18.4万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈不一致
- 4443 Ｓａｎｓａｎ｜granville_oshime/changepoint🔔｜🔥絶好調｜⚪妥当｜PASS_DOJI｜1928｜💰19.3万円｜⛔提案なし(材料後出し)｜⚡材料後出し ⚠日程不明｜📈レンジ
  > 📌【業態】名刺管理サービス最大手。法人向けクラウド、個人向けアプリ展開。請求書データも。
  > 📌【いま】終値1,928円・直近5日-12.04%・📌その他重要開示Presentation Materials on KiteRa, Inc. Becoming a Group Company
  > 📌【調子】🔥絶好調（8/13）
  > 📌【水準】⚪妥当（4.0/7）— PER26.02倍・PEG0.394・52週66.4% ／ 💰単元19.3万円
  > 📌【戦略】発注対象外（⛔提案なし(材料後出し)）
- 153A Caulis, Inc.｜granville_oshime｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜2370｜💰23.7万円｜⚠日程不明｜📈レンジ
- 3968 セグエグループ｜granville_oshime｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜785｜💰7.8万円｜⚡材料後出し ⚠日程不明｜📈合致
- 3673 ブロードリーフ｜granville_oshime｜⚡好調｜💎割安｜FAIL_UWAHIGE｜308｜💰3.1万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈不一致
- 3040 ソリトンシステムズ｜granville_oshime/granville_rebound｜⚡好調｜🟢値頃｜PASS_DOJI｜2453｜💰24.5万円｜⛔型不一致(十字線: トウバ)｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明 📐進捗 上振れ 37.3%｜📈不一致
  > 📌【業態】情報・通信業（ソフト・システム開発・情報セキュリティ・セキュリティソフト関連）
  > 📌【いま】終値2,453円・直近5日-5.65%（材料未確認）
  > 📌【調子】⚡好調（7/13）
  > 📌【水準】🟢値頃（5.0/7）— PER17.05倍・PEG0.522・52週36.8% ／ 💰単元24.5万円
  > 📌【戦略】発注対象外（⛔型不一致(十字線: トウバ)）
- 5892 ＹＵＴＯＲＩ｜granville_oshime｜⚡好調｜🟢値頃｜FAIL_INSEN｜2100｜💰21.0万円｜⚠日程不明｜📈不一致
- 8159 Tachibana Eletech Co., Ltd.｜granville_oshime｜⚡好調｜🟢値頃｜FAIL_INSEN｜4015｜💰40.1万円｜⚠日程不明｜📈不一致
- 7970 Shin-Etsu Polymer Co., Ltd.｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜2226｜💰22.3万円｜⚠日程不明｜📈レンジ
- 2492 インフォマート（インフォＭＴ）｜granville_oshime｜⚡好調｜🟡やや割高｜FAIL_UWAHIGE｜695｜💰7.0万円｜⚠日程不明｜📈レンジ
- 7678 ASAKUMA CO.,LTD.｜granville_oshime｜⚡好調｜🔴過熱｜PASS｜4090｜💰40.9万円｜⛔型不一致(既に支持帯以下)｜📋カルテ窓 12/09(残12営業日)｜📈合致
  > 📌【業態】愛知中心に「ステーキのあさくま」を店舗展開。テンポスホールディングス子会社。
  > 📌【いま】終値4,090円・直近5日-7.88%（材料未確認）
  > 📌【調子】⚡好調（7/13）
  > 📌【水準】🔴過熱（0.0/7）— PER104.87倍・PEG3.831・52週80.2% ／ 💰単元40.9万円
  > 📌【戦略】発注対象外（⛔型不一致(既に支持帯以下)）
- 4674 クレスコ｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜1852｜💰18.5万円｜⚠日程不明｜📈合致
- 2384 ＳＢＳホールディングス｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜5330｜💰53.3万円｜⚠日程不明｜📈レンジ
- 4498 Cybertrust Japan Co.Ltd.｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜1590｜💰15.9万円｜⚠日程不明｜📈不一致
- 6947 図研｜granville_oshime/granville_rebound｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜5070｜💰50.7万円｜⚠日程不明｜📈レンジ
- 4475 Hennge K.K.｜granville_oshime/changepoint🔔🔔/changepoint｜⚡好調｜🟡やや割高｜FAIL_INSEN｜2371｜💰23.7万円｜⚡材料後出し ⚠日程不明｜📈不一致
- 4398 ブロードバンドセキュリティ｜granville_oshime/granville_rebound｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜2084｜💰20.8万円｜⚠日程不明｜📈不一致
- 338A ZenmuTech,Inc.｜granville_oshime/granville_rebound｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜3435｜💰34.4万円｜📈レンジ
- 9536 SAIBU GAS HOLDINGS CO. LTD.｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜2822｜💰28.2万円｜⚠日程不明｜📈不一致
- 436A サイバーソリューションズ（サイバＳＯＬ）｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜1684｜💰16.8万円｜📈合致
- 3042 セキュアヴェイル（セキュアヴェ）｜granville_oshime｜⚡好調｜🟡やや割高｜FAIL_INSEN｜802｜💰8.0万円｜📈不一致
- 4373 Simplex Holdings,Inc.｜granville_oshime｜⚡好調｜🟡やや割高｜FAIL_INSEN｜1131｜💰11.3万円｜⚠日程不明｜📈レンジ
- 6877 ＯＢＡＲＡ　ＧＲＯＵＰ（ＯＢＡＲＡＧ）｜granville_oshime｜⚡好調｜🟡やや割高｜FAIL_UWAHIGE｜7040｜💰70.4万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈不一致
- 3399 Maruchiyo Yamaokaya Corporation｜granville_oshime｜⚡好調｜🔴過熱｜FAIL_INSEN｜5300｜💰53.0万円｜📋カルテ窓 12/11(残14営業日)｜📈合致
- 5036 日本ビジネスシステムズ｜granville_oshime｜✅順調｜⚪妥当｜FAIL_INSEN｜1367｜💰13.7万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚡材料後出し ⚠日程不明｜📈不一致
- 6080 Ｍ＆Ａキャピタルパートナーズ｜granville_oshime/changepoint/changepoint🔔/changepoint🔔🔔｜✅順調｜🟡やや割高｜FAIL_INSEN｜4150｜💰41.5万円｜⚠日程不明｜📈レンジ
- 9552 クオンツ総研ホールディングス｜granville_oshime｜✅順調｜🟡やや割高｜FAIL_INSEN｜1016｜💰10.2万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚡材料後出し ⚠日程不明｜📈レンジ
- 3762 テクマトリックス（テクマト）｜granville_oshime｜✅順調｜🔴過熱｜FAIL_UWAHIGE｜3165｜💰31.6万円｜⚠日程不明｜📈合致
- 7504 Kohsoku Corporation｜granville_oshime｜✅順調｜🔴過熱｜PASS｜5190｜💰51.9万円｜oshime 5170.9 SL5145.2・✅即時可（乖離-0.4%）｜📈合致
  > 📌【業態】食品軽包装資材商社。食品加工業向け中心。東北・北関東地盤。M&Aで拡大。
  > 📌【いま】終値5,190円・直近5日-3.35%（材料未確認）
  > 📌【調子】✅順調（3/13）— 質注意
  > 📌【水準】🔴過熱（0.0/7）— PER25.08倍・PEG6.198・52週81.5% ／ 💰単元51.9万円
  > 📌【戦略】5170.9円までの押し目を指値で待つ。SL5145.2円（25日線基準）
- 3692 ＦＦＲＩセキュリティ｜granville_oshime｜➖横ばい｜🟡やや割高｜FAIL_INSEN｜6100｜💰61.0万円｜⚠日程不明｜📈不一致
- 336A ダイナミックマッププラットフォーム｜granville_oshime｜取得不可｜⚪妥当｜FAIL_INSEN｜1050｜💰10.5万円｜⚠日程不明｜📈レンジ
- 3697 SHIFT, Inc.｜granville_oshime｜業績データ取得不可(経常益予想非開示)｜⚪妥当｜FAIL_INSEN｜1010｜💰10.1万円｜⚠日程不明｜📈不一致
- 6027 Bengo4.com, Inc.｜granville_oshime｜取得不可｜⚪妥当｜FAIL_INSEN｜3750｜💰37.5万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈レンジ
- 6191 エボラブルアジア｜granville_oshime｜取得不可｜⚪妥当｜FAIL_INSEN｜1507｜💰15.1万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈不一致
- 4432 ウイングアーク１ｓｔ｜granville_oshime｜業績データ取得不可(経常益予想非開示)｜🟡やや割高｜FAIL_UWAHIGE｜3445｜💰34.5万円｜⚠日程不明｜📈レンジ
- 2326 Digital Arts Inc.｜granville_oshime｜—｜－未評価（次回①-9で算定）｜PASS｜5680｜💰—｜oshime 5675.8 SL5647.6・⏸位置不適(25日線 下向き -1.46%)（乖離-0.1%）｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈レンジ
  > 📌【業態】有害情報遮断フィルタリングソフトで国内首位。公共・教育機関、企業向け強化。
  > 📌【いま】終値5,680円・直近5日+4.03%（材料未確認）
  > 📌【調子】—（—/13）
  > 📌【水準】－未評価（次回①-9で算定）（—/7）— PER—倍・PEG—・52週—% ／ 💰単元—
  > 📌【戦略】5675.8円までの押し目を指値で待つ。SL5647.6円（25日線基準）
- 2664 Cawachi Limited｜granville_oshime｜—｜－未評価（次回①-9で算定）｜PASS｜4035｜💰—｜⛔型不一致(既に支持帯以下)｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈レンジ
  > 📌【業態】北関東・東北にドラッグチェーン展開。超大型店に注力。調剤、雑貨、食品販売大。
  > 📌【いま】終値4,035円・直近5日-1.10%（材料未確認）
  > 📌【調子】—（—/13）
  > 📌【水準】－未評価（次回①-9で算定）（—/7）— PER—倍・PEG—・52週—% ／ 💰単元—
  > 📌【戦略】発注対象外（⛔型不一致(既に支持帯以下)）
- 3547 UNISIA HOLDINGS CO.｜granville_oshime｜—｜—｜FAIL_INSEN｜1906｜💰—｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈レンジ
- 4686 JUSTSYSTEMS CORPORATION｜granville_oshime｜—｜—｜FAIL_UWAHIGE｜4715｜💰—｜⚠日程不明｜📈合致
- 5133 Terilogy Holdings Corporation｜granville_oshime/granville_rebound｜—｜—｜FAIL_UWAHIGE｜414｜💰—｜⚠日程不明｜📈レンジ
- 7537 Marubun Corporation｜granville_oshime｜—｜—｜FAIL_INSEN｜1929｜💰—｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈レンジ
- 7947 FP Corporation｜granville_oshime｜—｜—｜FAIL_UWAHIGE｜3025｜💰—｜⚠日程不明｜📈不一致
- 9551 METAWATER Co.Ltd.｜granville_oshime｜—｜—｜FAIL_INSEN｜3430｜💰—｜⚠日程不明｜📈不一致
- 9889 JBCC Holdings Inc.｜granville_oshime｜—｜—｜FAIL_INSEN｜2005｜💰—｜⚠日程不明｜📈合致
- 6490 ＰＩＬＬＡＲ｜granville_rebound｜🚀確変｜🟢値頃｜FAIL_UWAHIGE｜8940｜💰89.4万円｜📈不一致
- 4937 Waqoo Inc.｜granville_rebound｜🚀確変｜⚪妥当｜FAIL_INSEN｜1854｜💰18.5万円｜📈合致
- 6862 ミナト HD｜granville_rebound｜🚀確変｜💎割安｜FAIL_INSEN｜2557｜💰25.6万円｜⚡材料後出し ⚠日程不明｜📈不一致
- 5027 AnyMind Group Inc.｜granville_rebound｜🚀確変｜⚪妥当｜FAIL_INSEN｜536｜💰5.4万円｜⚠日程不明｜📈レンジ
- 3851 日本一ソフトウェア｜granville_rebound｜🚀確変｜💎割安｜FAIL_INSEN｜820｜💰8.2万円｜⚠日程不明｜📈合致
- 3891 ニッポン高度紙工業｜granville_rebound｜🚀確変｜💎割安｜FAIL_INSEN｜4710｜💰47.1万円｜⚠日程不明｜📈不一致
- 6138 ダイジェット工業（ダイジェト）｜granville_rebound｜🚀確変｜💎割安｜FAIL_INSEN｜1522｜💰15.2万円｜⚠日程不明｜📈合致
- 4419 Finatext Holdings Ltd.｜granville_rebound/changepoint🔔/changepoint｜🚀確変｜🟢値頃｜FAIL_INSEN｜979｜💰9.8万円｜⚠日程不明｜📈合致
- 5381 Mipox Corp.｜granville_rebound｜🚀確変｜🟢値頃｜FAIL_INSEN｜798｜💰8.0万円｜⚠日程不明｜📈レンジ
- 2962 テクニスコ｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1027｜💰10.3万円｜⚡材料後出し ⚠日程不明｜📈合致
- 4968 Arakawa Chemical Industries,Ltd.｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1697｜💰17.0万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈不一致
- 6317 Kitagawa Corporation｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜2532｜💰25.3万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈不一致
- 7713 Sigma Koki Co., Ltd.｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜2339｜💰23.4万円｜⚠日程不明｜📈合致
- 8364 清水銀行｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜2332｜💰23.3万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈合致
- 1436 GreenEnergy & Company｜granville_rebound｜🔥絶好調｜💎割安｜FAIL_INSEN｜1049｜💰10.5万円｜📋カルテ窓 12/08(残11営業日)｜📈合致
- 479A PRONI Inc.｜granville_rebound/changepoint🔔｜🔥絶好調｜💎割安｜FAIL_INSEN｜895｜💰8.9万円｜⚠日程不明｜📈不一致（長期下向き）
- 2489 アドウェイズ｜granville_rebound｜⚠減速｜💎割安｜FAIL_INSEN｜295｜💰3.0万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈合致
- 3793 Drecom Co., Ltd.｜granville_rebound｜⚠減速｜💎割安｜FAIL_INSEN｜412｜💰4.1万円｜⚠日程不明｜📈不一致
- 7609 Daitron Co., Ltd.｜granville_rebound｜🔥絶好調｜💎割安｜FAIL_INSEN｜3475｜💰34.8万円｜⚠日程不明｜📈不一致
- 7715 長野計器｜granville_rebound｜🔥絶好調｜💎割安｜FAIL_INSEN｜2862｜💰28.6万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈合致
- 3696 CERES INC.｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1980｜💰19.8万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈レンジ
- 5256 Fusic Co.,Ltd.｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜2250｜💰22.5万円｜⚠日程不明｜📈不一致（長期下向き）
- 150A ＪＳＨ｜granville_rebound｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜815｜💰8.2万円｜⚠日程不明｜📈不一致
- 6840 ＡＫＩＢＡホールディングス｜granville_rebound｜🔥絶好調｜💎割安｜FAIL_INSEN｜490｜💰4.9万円｜⚠日程不明｜📈合致
- 4100 Toda Kogyo Corp.｜granville_rebound｜🔥絶好調｜💎割安｜FAIL_INSEN｜1438｜💰14.4万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈レンジ
- 7256 河西工業｜granville_rebound｜🔥絶好調｜💎割安｜FAIL_INSEN｜327｜💰3.3万円｜⚠日程不明｜📈合致
- 460A ＢＲＡＮＵ｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1009｜💰10.1万円｜📋カルテ窓 12/14(残15営業日)｜📈レンジ
- 5033 Nulab Inc.｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1125｜💰11.2万円｜⚡材料後出し｜📈不一致
- 4431 Smaregi, Inc.｜granville_rebound｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜2918｜💰29.2万円｜📋カルテ窓 12/15(残16営業日)｜📈合致
- 5252 日本ナレッジ｜granville_rebound｜🔥絶好調｜🟡やや割高｜FAIL_INSEN｜880｜💰8.8万円｜⚠日程不明｜📈レンジ
- 8050 SEIKO GROUP CORPORATION｜granville_rebound｜🔥絶好調｜🟡やや割高｜FAIL_INSEN｜7701｜💰77.0万円｜⚠日程不明｜📈合致
- 6508 Meidensha Corporation｜granville_rebound｜⚡好調｜💎割安｜FAIL_INSEN｜6198｜💰62.0万円｜⚠日程不明｜📈合致
- 6742 京三製作所｜granville_rebound｜⚡好調｜🟢値頃｜FAIL_INSEN｜788｜💰7.9万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈合致
- 8344 Yamagata Bank, Ltd.｜granville_rebound｜⚡好調｜🟢値頃｜FAIL_INSEN｜3525｜💰35.2万円｜⚠日程不明｜📈合致
- 9697 カプコン｜granville_rebound｜⚡好調｜🔴過熱｜FAIL_INSEN｜4424｜💰44.2万円｜⚠日程不明｜📈レンジ
- 477A Startline CO.,LTD.｜granville_rebound｜⚡好調｜💎割安｜FAIL_INSEN｜503｜💰5.0万円｜⚠日程不明｜📈不一致（長期下向き）
- 4040 NANKAI CHEMICAL COMPANY LIMITED｜granville_rebound｜⚡好調｜💎割安｜FAIL_INSEN｜3470｜💰34.7万円｜⚠日程不明｜📈合致
- 3850 INTRAMART CORPORATION｜granville_rebound｜⚡好調｜🟢値頃｜FAIL_INSEN｜3080｜💰30.8万円｜⚠日程不明｜📈不一致（長期下向き）
- 6958 日本シイエムケイ｜granville_rebound｜⚡好調｜⚪妥当｜FAIL_INSEN｜644｜💰6.4万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈不一致
- 7826 フルヤ金属｜granville_rebound｜⚡好調｜⚪妥当｜FAIL_INSEN｜7180｜💰71.8万円｜⚠日程不明｜📈合致
- 7213 LECIP Holdings Corporation｜granville_rebound｜⚡好調｜💎割安｜FAIL_INSEN｜548｜💰5.5万円｜⚠日程不明｜📈不一致
- 4667 Aisan Technology Co.,Ltd.｜granville_rebound/changepoint/changepoint🔔｜⚡好調｜🟢値頃｜FAIL_INSEN｜594｜💰5.9万円｜⚠日程不明｜📈不一致（長期下向き）
- 6904 Harada Industry Co., Ltd.｜granville_rebound｜⚡好調｜⚪妥当｜FAIL_INSEN｜574｜💰5.7万円｜⚠日程不明｜📈合致
- 9278 BOOKOFF GROUP HOLDINGS LIMITED｜granville_rebound｜⚡好調｜🟡やや割高｜FAIL_INSEN｜2377｜💰23.8万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈レンジ
- 3763 Pro-Ship Incorporated｜granville_rebound｜⚡好調｜🔴過熱｜FAIL_INSEN｜1813｜💰18.1万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈不一致
- 4025 多木化学｜granville_rebound｜✅順調｜⚪妥当｜FAIL_UWAHIGE｜5260｜💰52.6万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈不一致
- 428A Cypress Holdings Co., Ltd.｜granville_rebound｜✅順調｜⚪妥当｜FAIL_INSEN｜1324｜💰13.2万円｜⚠日程不明｜📈合致
- 3371 ソフトクリエイトホールディングス｜granville_rebound｜✅順調｜🟡やや割高｜FAIL_INSEN｜1982｜💰19.8万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈不一致（長期下向き）
- 278A Ｔｅｒｒａ　Ｄｒｏｎｅ｜granville_rebound｜✅順調｜⏸判定不能｜FAIL_INSEN｜4590｜💰—｜📋カルテ窓 12/15(残16営業日)｜📈レンジ
- 4396 System Support Holdings Inc.｜granville_rebound｜✅順調｜⚪妥当｜FAIL_UWAHIGE｜1226｜💰12.3万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈不一致（長期下向き）
- 5599 S&J Corporation｜granville_rebound｜✅順調｜⚪妥当｜FAIL_INSEN｜1394｜💰13.9万円｜📈不一致（長期下向き）
- 6676 BUFFALO INC.｜granville_rebound｜⚠減速｜🟡やや割高｜FAIL_INSEN｜3095｜💰30.9万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈不一致
- 3909 Showcase, Inc. (Japan)｜granville_rebound｜🔻悪化｜🟢値頃｜FAIL_INSEN｜674｜💰6.7万円｜📈不一致
- 4884 Kringle Pharma, Inc.｜granville_rebound｜⚠減速｜🔴過熱｜FAIL_INSEN｜541｜💰5.4万円｜⚡材料後出し ⚠日程不明｜📈不一致
- 3858 Ubiquitous AI Corporation｜granville_rebound｜⚠減速｜💎割安｜FAIL_INSEN｜361｜💰3.6万円｜⚠日程不明｜📈不一致（長期下向き）
- 3565 Ascentech KK｜granville_rebound｜🔻悪化｜⚪妥当｜PASS_DOJI｜415｜💰4.2万円｜momentum 421 SL409・⏳確認足待ち｜📑TOPIX低減対象（次 01/29 第2回/8） 📋カルテ窓 12/15(残16営業日) ⚠業績基調が下向き（🔻悪化） ⚠市場に劣後 RS20 -14.4pt｜📈不一致（長期下向き）
  > 📌【業態】仮想デスクトップ関連の製品開発、販売。テレワーク強み。クラウドサービスやインフラ構築も。
  > 📌【いま】終値415円・直近5日-8.99%（材料未確認）
  > 📌【調子】🔻悪化（0/13）— 質注意・⚠減速・⚠下期依存
  > 📌【水準】⚪妥当（4.0/7）— PER12.50倍・PEG—・52週30.1% ／ 💰単元4.2万円
  > 📌【戦略】当日高値超えの逆指値421円で順張り参戦を検討。上限425.2円・SL409円目安
- 4240 Cluster Technology Co., Ltd.｜granville_rebound｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜466｜💰4.7万円｜⚠日程不明｜📈不一致
- 8377 ほくほくフィナンシャルグループ｜granville_rebound｜業績データ取得不可(売上/経常欠損)｜💎割安｜FAIL_INSEN｜677.7｜💰6.8万円｜⚠日程不明｜📈不一致
- 7380 Juroku Financial Group,Inc.｜granville_rebound｜業績データ取得不可(売上/経常欠損)｜⚪妥当｜FAIL_INSEN｜2041.5｜💰20.4万円｜⚠日程不明｜📈不一致
- 8551 北日本銀行｜granville_rebound｜取得不可｜⚪妥当｜FAIL_INSEN｜1926｜💰19.3万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈合致
- 7184 富山第一銀行｜granville_rebound｜取得不可｜🟡やや割高｜FAIL_INSEN｜2640｜💰26.4万円｜⚠日程不明｜📈合致
- 4075 ブレインズテクノロジー｜granville_rebound｜取得不可｜⏸判定不能｜FAIL_INSEN｜947｜💰9.5万円｜📋カルテ窓 12/11(残14営業日)｜📈レンジ
- 7175 Imamura Securities Co.Ltd.｜granville_rebound｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜1538｜💰15.4万円｜⚠日程不明｜📈不一致
- 8609 岡三証券グループ｜granville_rebound｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜925｜💰9.2万円｜⚠日程不明｜📈不一致
- 8739 スパークス・グループ｜granville_rebound｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜2375｜💰23.8万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈レンジ
- 9104 Mitsui O.S.K.Lines,Ltd.｜granville_rebound｜—｜—｜FAIL_UWAHIGE｜6444｜💰—｜⚠日程不明｜📈合致

## 変化点銘柄
- 5803 Fujikura Ltd.｜changepoint🔔/changepoint｜🚀確変｜💎割安｜FAIL_INSEN｜2252｜💰22.5万円｜⚠日程不明 🔒実弾封印中(PL3紙ログ収集中)｜📈不一致（長期下向き）
- 265A エイチエムコム｜changepoint/changepoint🔔｜🚀確変｜🟢値頃｜FAIL_INSEN｜499｜💰5.0万円｜⚡材料後出し ⚠日程不明 🔒実弾封印中(PL3紙ログ収集中)｜📈不一致（長期下向き）
- 4011 Headwaters Co.,Ltd｜changepoint🔔｜🚀確変｜🟢値頃｜FAIL_INSEN｜1453｜💰14.5万円｜⚠日程不明 🔒実弾封印中(PL3紙ログ収集中)｜📈不一致（長期下向き）
- 7695 交換できるくん｜changepoint/changepoint🔔/changepoint🔔🔔｜🚀確変｜⚪妥当｜FAIL_INSEN｜864｜💰8.6万円｜⚠日程不明 🔒実弾封印中(PL3紙ログ収集中)｜📈レンジ
- 6866 Hioki E.E. Corporation｜changepoint/changepoint🔔｜🔥絶好調｜💎割安｜FAIL_INSEN｜7750｜💰77.5万円｜⚠日程不明 🔒実弾封印中(PL3紙ログ収集中)｜📈不一致
- 7318 Serendip Holdings Co.,Ltd.｜changepoint｜🔥絶好調｜💎割安｜FAIL_INSEN｜831｜💰8.3万円｜⚠日程不明 🔒実弾封印中(PL3紙ログ収集中)｜📈不一致（長期下向き）
- 8151 東陽テクニカ｜changepoint🔔/changepoint🔔🔔｜⚡好調｜💎割安｜FAIL_INSEN｜1716｜💰17.2万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明 🔒実弾封印中(PL3紙ログ収集中)｜📈レンジ
- 593A Tier IV, Inc.｜changepoint🔔🔔/changepoint/changepoint🔔｜⚡好調｜⚪妥当｜FAIL_INSEN｜1685｜💰16.9万円｜📑TOPIX新規採用（2026-10-30 組入） ⚠日程不明 🔒実弾封印中(PL3紙ログ収集中)｜📈判定不能
- 4488 AI inside Inc.｜changepoint🔔｜⚡好調｜⚪妥当｜FAIL_INSEN｜1646｜💰16.5万円｜⚠日程不明 🔒実弾封印中(PL3紙ログ収集中)｜📈不一致（長期下向き）
- 9343 アイビス｜changepoint/changepoint🔔/changepoint🔔🔔｜⚡好調｜⚪妥当｜FAIL_INSEN｜627｜💰6.3万円｜⚠日程不明 🔒実弾封印中(PL3紙ログ収集中)｜📈不一致（長期下向き）
- 286A ユカリア｜changepoint🔔｜⚡好調｜💎割安｜FAIL_INSEN｜664｜💰6.6万円｜⚠日程不明 🔒実弾封印中(PL3紙ログ収集中)｜📈レンジ
- 6597 HPC SYSTEMS Inc.｜changepoint/changepoint🔔｜⚡好調｜💎割安｜FAIL_INSEN｜2121｜💰21.2万円｜🔒実弾封印中(PL3紙ログ収集中)｜📈合致
- 218A Liberaware｜changepoint/changepoint🔔｜⚡好調｜⚪妥当｜FAIL_INSEN｜677｜💰6.8万円｜📋カルテ窓 12/11(残14営業日) 🔒実弾封印中(PL3紙ログ収集中)｜📈レンジ
- 4483 JMDC｜changepoint🔔/changepoint🔔🔔｜⚡好調｜🔴過熱｜FAIL_INSEN｜3440｜💰34.4万円｜⚠日程不明 🔒実弾封印中(PL3紙ログ収集中)｜📈不一致（長期下向き）
- 3923 ラクス｜changepoint🔔🔔/changepoint🔔｜⚠減速｜⚪妥当｜FAIL_INSEN｜937.6｜💰9.4万円｜⚠日程不明 🔒実弾封印中(PL3紙ログ収集中)｜📈レンジ
- 4165 PLAID Inc.｜changepoint🔔🔔｜✅順調｜🟡やや割高｜FAIL_INSEN｜338｜💰3.4万円｜⚠日程不明 🔒実弾封印中(PL3紙ログ収集中)｜📈不一致（長期下向き）
- 4493 Cyber Security Cloud, Inc.｜changepoint｜✅順調｜🟡やや割高｜FAIL_INSEN｜1681｜💰16.8万円｜🔒実弾封印中(PL3紙ログ収集中)｜📈不一致（長期下向き）
- 3989 シェアテク｜changepoint🔔｜業績データ取得不可(売上/経常欠損)｜⏸判定不能｜FAIL_INSEN｜1534｜💰15.3万円｜⚠日程不明 🔒実弾封印中(PL3紙ログ収集中)｜📈レンジ

## 🤖AI特需銘柄（スキャン由来 ai/sr/dm/an）
- 波: なし／25MA 上回り率 エネマネ 0.0%・冷却 8.33%・光 0.0%・基板 2.38%
- 6777 santec｜ai_momentum/ai_reversal｜🚀確変｜🟢値頃｜FAIL_INSEN｜16420｜💰164.2万円｜📑TOPIX新規採用（2026-10-30 組入） ⚠日程不明｜📈レンジ
- 6613 QD Laser, Inc.｜ai_momentum/ai_reversal/granville_oshime｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜1520｜💰15.2万円｜📑TOPIX新規採用（2026-10-30 組入） ⚠日程不明｜📈レンジ
- 4063 信越化学工業｜ai_momentum/ai_reversal/sr_universe｜⚡好調｜⚪妥当｜FAIL_INSEN｜5237｜💰52.4万円｜⚠日程不明｜📈レンジ
- 6988 日東電工｜ai_momentum/ai_reversal｜⚡好調｜🟡やや割高｜FAIL_INSEN｜3390｜💰33.9万円｜⚠日程不明｜📈レンジ
- 6367 ダイキン工業｜ai_momentum/sr_universe｜✅順調｜🔴過熱｜FAIL_UWAHIGE｜23765｜💰237.7万円｜⚠日程不明｜📈合致
- 1975 新日本空調｜ai_momentum｜✅順調｜⚪妥当｜PASS_DOJI｜3045｜💰30.4万円｜⛔提案なし(指名鮮度切れ 15営業日)｜⚠日程不明｜📈不一致
  > 📌【業態】空調・衛生工事の大手。ハイテク環境制御装置に優れる。民間受注が中心。
  > 📌【いま】終値3,045円・直近5日-11.35%（材料未確認）
  > 📌【調子】✅順調（3/13）— 質注意
  > 📌【水準】⚪妥当（4.0/7）— PER8.52倍・PEG2.779・52週8.3% ／ 💰単元30.4万円
  > 📌【戦略】発注対象外（⛔提案なし(指名鮮度切れ 15営業日)）
- 3374 内外テック｜ai_reversal/granville_rebound｜🚀確変｜💎割安｜FAIL_INSEN｜3080｜💰30.8万円｜⚠日程不明｜📈合致
- 4047 関東電化工業｜ai_reversal｜🚀確変｜💎割安｜FAIL_INSEN｜1391｜💰13.9万円｜⚠日程不明｜📈合致
- 6834 精工技研｜ai_reversal｜🚀確変｜💎割安｜FAIL_INSEN｜3420｜💰34.2万円｜📑TOPIX新規採用（2026-10-30 組入） ⚠日程不明｜📈レンジ
- 6407 CKD｜ai_reversal｜🚀確変｜💎割安｜FAIL_INSEN｜3574｜💰35.7万円｜⚠日程不明｜📈不一致（長期下向き）
- 4062 イビデン｜ai_reversal/sr_reversal/an_reversal/sr_universe｜🚀確変｜🟢値頃｜FAIL_INSEN｜4672｜💰46.7万円｜⚠日程不明｜📈合致
- 6857 アドバンテスト｜ai_reversal/sr_universe｜🚀確変｜⚪妥当｜FAIL_INSEN｜24255｜💰242.6万円｜⚠日程不明｜📈合致
- 5801 古河電気工業｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜1620｜💰16.2万円｜⚠日程不明｜📈合致
- 6787 メイコー｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜7720｜💰77.2万円｜⚠日程不明｜📈不一致
- 8035 東京エレクトロン｜ai_reversal/sr_universe｜🔥絶好調｜💎割安｜FAIL_INSEN｜8309｜💰83.1万円｜⚠日程不明｜📈不一致
- 6918 アバールデータ｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜2597｜💰26.0万円｜⚠日程不明｜📈不一致（長期下向き）
- 6524 湖北工業｜ai_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜3865｜💰38.6万円｜⚠日程不明｜📈不一致
- 3110 日東紡｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜2098.5｜💰21.0万円｜⚠日程不明｜📈不一致（長期下向き）
- 4182 三菱ガス化学｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜2923｜💰29.2万円｜⚠日程不明｜📈不一致（長期下向き）
- 4368 扶桑化学工業｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜2540｜💰25.4万円｜⚠日程不明｜📈不一致
- 6323 ローツェ｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜2754｜💰27.5万円｜⚠日程不明｜📈不一致（長期下向き）
- 6762 TDK｜ai_reversal/sr_reversal/sr_universe｜🔥絶好調｜💎割安｜FAIL_INSEN｜2116.5｜💰21.2万円｜⚠日程不明｜📈合致
- 6779 日本電波工業｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜1493｜💰14.9万円｜⚠日程不明｜📈合致
- 7729 東京精密｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜11185｜💰111.8万円｜⚠日程不明｜📈不一致（長期下向き）
- 2760 東京エレクトロンデバイス｜ai_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜3630｜💰36.3万円｜⚠日程不明｜📈不一致
- 4971 メック｜ai_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜4715｜💰47.1万円｜⚠日程不明｜📈不一致（長期下向き）
- 6235 オプトラン｜ai_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1875｜💰18.8万円｜⚠日程不明｜📈不一致（長期下向き）
- 6981 村田製作所｜ai_reversal/sr_reversal/sr_universe｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜4700｜💰47.0万円｜⚠日程不明｜📈合致
- 7735 SCREENホールディングス｜ai_reversal/sr_universe｜🔥絶好調｜💎割安｜FAIL_INSEN｜7121｜💰71.2万円｜⚠日程不明｜📈不一致（長期下向き）
- 1961 三機工業｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜2322｜💰23.2万円｜⚠日程不明｜📈レンジ
- 5384 フジミインコーポレーテッド｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜2630｜💰26.3万円｜⚠日程不明｜📈合致
- 6941 山一電機｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_UWAHIGE｜6150｜💰61.5万円｜⚠日程不明｜📈不一致
- 6227 AIメカテック｜ai_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜3745｜💰37.5万円｜📑TOPIX新規採用（2026-10-30 組入） ⚠日程不明｜📈不一致
- 6752 パナソニックHD｜ai_reversal/an_reversal｜⚡好調｜🟢値頃｜FAIL_INSEN｜2687｜💰26.9万円｜⚠日程不明｜📈合致
- 3436 SUMCO｜ai_reversal｜⚡好調｜💎割安｜FAIL_INSEN｜1829｜💰18.3万円｜⚠日程不明｜📈不一致
- 6336 石井表記｜ai_reversal/granville_rebound｜⚡好調｜💎割安｜FAIL_INSEN｜1063｜💰10.6万円｜📋カルテ窓 12/11(残14営業日)｜📈不一致
- 6971 京セラ｜ai_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜2721.5｜💰27.2万円｜⚠日程不明｜📈合致
- 4022 ラサ工業｜ai_reversal｜⚡好調｜💎割安｜FAIL_INSEN｜1124｜💰11.2万円｜📈不一致（長期下向き）
- 6505 東洋電機製造｜ai_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜2845｜💰28.4万円｜⚠日程不明｜📈不一致
- 4973 JCU｜ai_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜3645｜💰36.5万円｜📑TOPIX低減対象（次 01/29 第2回/8） ⚠日程不明｜📈不一致（長期下向き）
- 255A GLテクノHD｜ai_reversal｜✅順調｜💎割安｜FAIL_UWAHIGE｜3540｜💰35.4万円｜⚠日程不明｜📈合致
- 6590 芝浦メカトロニクス｜ai_reversal｜✅順調｜🟢値頃｜FAIL_INSEN｜2338｜💰23.4万円｜⚠日程不明｜📈不一致（長期下向き）
- 5706 三井金属鉱業｜ai_reversal｜🔻悪化｜⚪妥当｜FAIL_INSEN｜1120｜💰11.2万円｜⚠日程不明｜📈不一致（長期下向き）
- 6965 浜松ホトニクス｜ai_reversal｜✅順調｜🟡やや割高｜FAIL_INSEN｜1881｜💰18.8万円｜⚠日程不明｜📈不一致
- 5208 有沢製作所｜ai_reversal｜✅順調｜🔴過熱｜FAIL_INSEN｜1988｜💰19.9万円｜⚠日程不明｜📈合致
- 6643 戸上電機製作所｜ai_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜4415｜💰44.1万円｜⚠日程不明｜📈不一致（長期下向き）
- 6501 日立製作所｜ai_reversal/sr_universe｜✅順調｜🟡やや割高｜FAIL_INSEN｜4763｜💰47.6万円｜⚠日程不明｜📈不一致（長期下向き）
- 2802 味の素｜ai_reversal/sr_reversal/dm_reversal/sr_universe｜➖横ばい｜⚪妥当｜FAIL_INSEN｜3819｜💰38.2万円｜⚠日程不明｜📈合致
- 1982 日比谷総合設備｜ai_reversal｜➖横ばい｜🟡やや割高｜PASS_DOJI｜2886｜💰28.9万円｜⛔型不一致(十字線: トウバ)｜📐進捗 上振れ 14.1%｜📈レンジ
  > 📌【業態】空調工事大手。電気・衛生工事も。NTT向け主力。床下空調システムなどに強み。
  > 📌【いま】終値2,886円・直近5日-8.82%（材料未確認）
  > 📌【調子】➖横ばい（2/13）— 質注意・⚠減速
  > 📌【水準】🟡やや割高（2.0/7）— PER13.69倍・PEG4.700・52週54.1% ／ 💰単元28.9万円
  > 📌【戦略】発注対象外（⛔型不一致(十字線: トウバ)）
- 9503 関西電力｜ai_reversal/dm_reversal｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜2518.5｜💰25.2万円｜⚠日程不明｜📈レンジ
- 6617 東光高岳｜ai_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜4195｜💰42.0万円｜⚠日程不明｜📈合致
- 9432 NTT｜ai_reversal/sr_universe｜⚠減速｜🟡やや割高｜FAIL_UWAHIGE｜167.7｜💰1.7万円｜⚠日程不明｜📈不一致
- 4203 住友ベークライト｜ai_reversal/granville_rebound｜業績データ取得不可｜⚪妥当｜FAIL_INSEN｜6189｜💰61.9万円｜⚠日程不明｜📈合致
- 6146 ディスコ｜ai_reversal/sr_universe｜取得不可｜⏸判定不能｜FAIL_INSEN｜41350｜💰413.5万円｜⚠日程不明｜📈不一致（長期下向き）
- 6723 ルネサスエレクトロニクス｜ai_reversal/sr_universe｜取得不可｜⏸判定不能｜FAIL_INSEN｜2425｜💰24.2万円｜⚠日程不明｜📈不一致
- 9984 ソフトバンクグループ｜ai_reversal/sr_universe｜業績データ取得不可(経常益予想非開示)｜⏸判定不能｜FAIL_INSEN｜3025｜💰30.2万円｜⚠日程不明｜📈不一致（長期下向き）
- 7832 バンダイナムコホールディングス｜sr_momentum/sr_universe｜—｜—｜FAIL_INSEN｜7068｜💰—｜⚠日程不明｜📈合致
- 9843 ニトリホールディングス｜sr_momentum/dm_momentum/sr_universe｜—｜—｜FAIL_INSEN｜3655｜💰—｜⚠日程不明｜📈レンジ
- 6963 ローム｜sr_reversal/sr_universe｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜2620.5｜💰26.2万円｜⚠日程不明｜📈合致
- 4005 住友化学｜sr_reversal/granville_tenkan/sr_universe｜⚡好調｜💎割安｜FAIL_INSEN｜459.6｜💰4.6万円｜⚠日程不明｜📈合致
- 5367 Nikkato Corporation｜sr_reversal/granville_rebound/sr_universe｜⚡好調｜🟢値頃｜FAIL_INSEN｜883｜💰8.8万円｜⚠日程不明｜📈不一致
- 1605 INPEX｜sr_reversal/sr_universe｜➖横ばい｜⚪妥当｜FAIL_UWAHIGE｜3312｜💰33.1万円｜⚠日程不明｜📈合致
- 2914 日本たばこ産業｜sr_reversal/dm_reversal/sr_universe｜業績データ取得不可｜⚪妥当｜FAIL_INSEN｜5265｜💰52.6万円｜⚠日程不明｜📈合致
- 4478 freee K.K.｜sr_reversal/changepoint/changepoint🔔/changepoint🔔🔔/sr_universe｜取得不可｜⚪妥当｜FAIL_INSEN｜3020｜💰30.2万円｜📑TOPIX新規採用（2026-10-30 組入） ⚠日程不明｜📈合致
- 4716 日本オラクル｜sr_reversal/sr_universe｜—｜—｜FAIL_UWAHIGE｜9828｜💰—｜⚠日程不明｜📈レンジ
- 8766 東京海上ホールディングス｜sr_reversal/sr_universe｜—｜—｜FAIL_UWAHIGE｜577.5｜💰—｜⚠日程不明｜📈不一致
- 4911 資生堂｜dm_momentum｜⚡好調｜⚪妥当｜FAIL_INSEN｜4139｜💰41.4万円｜📈合致
- 7630 壱番屋｜dm_momentum｜➖横ばい｜🔴過熱｜FAIL_UWAHIGE｜1213｜💰12.1万円｜⚠日程不明｜📈合致
- 2810 ハウス食品グループ本社｜dm_momentum｜⚠減速｜🔴過熱｜FAIL_UWAHIGE｜4854｜💰48.5万円｜⚠日程不明｜📈合致
- 2267 Yakult Honsha Co., Ltd.｜dm_reversal/granville_tenkan｜⚠減速｜🔴過熱｜FAIL_UWAHIGE｜2835｜💰28.4万円｜⚠日程不明｜📈レンジ
- 2695 くら寿司｜dm_reversal｜—｜—｜FAIL_UWAHIGE｜1731｜💰—｜📋カルテ窓 12/10(残13営業日)｜📈レンジ
- 7516 コーナン商事｜dm_reversal｜—｜—｜FAIL_INSEN｜4780｜💰—｜⚠日程不明｜📈合致
- 408A iシェアーズ AI グローバル・イノベーション アクティブ ETF（ベストAI）｜an_reversal｜取得不可｜⏸判定不能｜FAIL_INSEN｜215.8｜💰0.2万円｜⚠日程不明｜📈不一致

## 📡常駐観測（SR ユニバース）
- 7201 日産自動車｜⑥外需シクリカル｜PASS｜📡常駐観測（提案なし）
- 4684 オービック｜②ソフト・情報通信｜PASS｜📡常駐観測（提案なし）
- 4689 LINEヤフー｜②ソフト・情報通信｜PASS_DOJI｜📡常駐観測（提案なし）
- 9201 日本航空｜⑧テーマ（空運・高配当・REIT・防衛）｜PASS｜📡常駐観測（提案なし）
- 9202 ANAホールディングス｜⑧テーマ（空運・高配当・REIT・防衛）｜PASS｜📡常駐観測（提案なし）
- 常駐のみ 49銘柄（PASS 5）

## ⚡材料後出し
- その日の足は開示前の情報。判定は参考値
- 5137 Smart Drive Co. Ltd.｜FAIL_INSEN｜📌その他重要開示 役員人事に関するお知らせ（11-20 18:30）
- 4933 I-ne CO., LTD.｜FAIL_INSEN｜📌その他重要開示 Notice Regarding Commencement of Tender Offer for Shares, etc. of I-ne Co., Ltd. (Securities Code 4933) by JAMBO Co., Ltd.（11-20 20:00）
- 6925 Ushio Inc.｜FAIL_INSEN｜📌その他重要開示 Notice Regarding Secondary Offering of Shares（11-20 16:00）
- 6875 メガチップス｜FAIL_INSEN｜🔁自己株式取得 自己株式の取得状況及び取得終了に関するお知らせ（11-20 17:00）
- 6471 日本精工｜FAIL_INSEN｜📌その他重要開示 Notice Concerning Execution of Definitive Agreement Regarding Establishment of a Joint Holding Company (Share Transfer)（11-20 16:30）
- 5333 ＮＧＫ｜FAIL_INSEN｜📌その他重要開示 Notice Regarding Disposal of Treasury Stock as Employee Shareholding Association－Restricted Stock Incentive（11-20 15:40）
- 6036 ＫｅｅＰｅｒ技研｜FAIL_INSEN｜📦特需・大口 2027年6月期 第1四半期 決算及び資本業務提携についての説明会ライブ配信のお知らせ（11-20 15:30）
- 6250 Yamabiko Corporation｜FAIL_INSEN｜📌その他重要開示 Summary of financial results FY26.12 3Q（11-20 15:30）
- 1721 コムシスホールディングス｜FAIL_UWAHIGE｜📌その他重要開示 （変更）法定事前開示書類（株式交換）（株式会社アイネット）（11-20 17:00）
- 1926 ライト工業（ライト）｜PASS_DOJI｜📌その他重要開示 [Updated] Consolidated Financial Results for the Six Months Ended September 30, 2026（11-20 15:30）
- 6277 Hosokawa Micron Corporation｜FAIL_INSEN｜📌その他重要開示 Notice Concerning Revision of Shareholder Return Policy（11-20 16:40）
- 5310 Toyo Tanso Co., Ltd.｜FAIL_INSEN｜📌その他重要開示 組織変更および人事異動に関するお知らせ（11-20 15:30）
- 6479 ミネベア｜FAIL_INSEN｜📌その他重要開示 [Summary]Notice Concerning Secondary Offering of Shares（11-20 15:30）
- 3612 WORLD CO.,LTD.｜FAIL_INSEN｜📌その他重要開示 Notice Regarding Introduction of Share Compensation Plans at the Joint Holding Company and Revision of World's Restricted Share Compensation Plan（11-20 15:30）
- 8334 Gunma Bank, Ltd.｜FAIL_INSEN｜📌その他重要開示 Corporate Governance Report（11-20 15:00）
- 3479 ＴＫＰ｜FAIL_INSEN｜📌その他重要開示 株主優待制度の拡充に関するお知らせ（11-20 17:20）
- 6099 エラン｜FAIL_UWAHIGE｜📌その他重要開示 Notice Regarding Revision of Full-Year Earnings Forecast（11-20 15:30）
- 9065 Sankyu Inc.｜FAIL_INSEN｜📌その他重要開示 法定事後開示書類（会社分割）（サンキュウアセットマネジメント株式会社）（11-20 15:30）
- 8934 Sun Frontier Fudousan Co., Ltd.｜FAIL_INSEN｜📌その他重要開示 サンフロンティア主催ピッチコンテスト「FRONTIER PITCH TOKYO for Startups 2026」優勝企業発表（11-20 15:00）
- 8803 Heiwa Real Estate Co., Ltd.｜FAIL_INSEN｜📌その他重要開示 サステナブルファイナンスの推進「サステナビリティ・リンク・ローン」の取り組み（11-20 15:30）
- 9007 Odakyu Electric Railway Co., Ltd.｜FAIL_UWAHIGE｜📌その他重要開示 (October) Monthly Report of Operations (preliminary figures)（11-20 15:30）
- 3252 JINUSHI Co.,Ltd.｜FAIL_INSEN｜📌その他重要開示 山口県防府市で、イオンリテールをテナントとする土地を取得（11-20 15:30）
- 4765 ＳＢＩグローバルアセットマネジメント｜FAIL_INSEN｜📌その他重要開示 “成長”と“分配”の両立を目指すSBIの高配当／増配株式ファンド　本日決算5ファンドの分配金に関するお知らせ（11-20 18:45）
- 5930 Bunka Shutter Co., Ltd.｜FAIL_UWAHIGE｜📌その他重要開示 Corporate Governance Report（11-20 16:05）
- 4443 Ｓａｎｓａｎ｜PASS_DOJI｜📌その他重要開示 Presentation Materials on KiteRa, Inc. Becoming a Group Company（11-20 16:30）
- 3968 セグエグループ｜FAIL_INSEN｜👥主要株主・大量保有 主要株主の異動（予定）および公開買付けに準ずる行為として政令で定める買集め行為に関する知らせ（11-20 16:00）
- 4475 Hennge K.K.｜FAIL_INSEN｜📌その他重要開示 Notice Regarding Partial Amendment to the Articles of Incorporation（11-20 15:30）
- 5036 日本ビジネスシステムズ｜FAIL_INSEN｜📌その他重要開示 Notice Regarding Dividends from Surplus（11-20 15:30）
- 9552 クオンツ総研ホールディングス｜FAIL_INSEN｜📌その他重要開示 Notice Regarding Borrowing of Funds（11-20 15:30）
- 6862 ミナト HD｜FAIL_INSEN｜📌その他重要開示 ミナトホールディングスグループのブレイン「第9回［名古屋］スマート工場 EXPO」に出展～世界シェアNo.1のZebra端末×MSI高耐久タブレットで現場のDXを最適化～（11-20 15:30）
- 2962 テクニスコ｜FAIL_INSEN｜📌その他重要開示 譲渡制限付株式報酬としての新株式の発行の払込完了に関するお知らせ（11-20 15:30）
- 5033 Nulab Inc.｜FAIL_INSEN｜📌その他重要開示 当社サービス「Cacoo」の再開の目処および不正アクセスに関する現在の状況について（第三報）（11-20 15:45）
- 4884 Kringle Pharma, Inc.｜FAIL_INSEN｜📌その他重要開示 「WISH & SEEDsマッチング会2026」に当社取締役執行役員医薬開発部長の早田大真が登壇します（11-20 17:00）
- 265A エイチエムコム｜FAIL_INSEN｜📌その他重要開示 Ｈｍｃｏｍｍ、静岡市上下水道局とともに実証実験を実施 ～福山市に続き、AIによる下水道腐食リスク可視化・重点点検支援の検証を展開～（11-20 15:30）
- 7013 IHI｜FAIL_INSEN｜📌その他重要開示 Notice Regarding the Transfer of Non-current Assets and the Recording of Gain on Transfer（11-20 15:00）

## 📢開示
- 使用した一覧URL: https://kabutan.jp/disclosures/?kubun=&page=1 〜 https://kabutan.jp/disclosures/?kubun=&page=38（期間 2026-11-19 20:30〜2026-11-20 20:30・全569件）。フォールバックなし
- プール突合 87件（📌その他重要開示81・👥主要株主・大量保有1・🔁自己株式取得3・📦特需・大口1・📊決算発表1）・①-9へ引き渡し 1件
- 📊決算発表 5832 ちゅうぎんＦ：（追加）「2027 年３月期第２四半期（中間期）決算短信〔日本基準〕 （連結）」補足説明資料の追加に関するお知らせ（11-20 14:00）
- 📌その他重要開示 5832 ちゅうぎんＦ：(Addendum)  Notice Regarding the Addition of Supplementary Materials  to the “Consolidated Financial Results for the Six Months  Ended September 2026（11-20 14:00）
- 🔁自己株式取得 6875 メガチップス：自己株式の取得状況及び取得終了に関するお知らせ（11-20 17:00）
- 📌その他重要開示 6875 メガチップス：Notice Regarding the Status and the Completion of Share Repurchases（11-20 17:00）
- 🔁自己株式取得 4307 野村総研：自己株式立会外買付取引（ToSTNeT-3）による自己株式の取得結果及び取得終了並びに自己株式の消却に関するお知らせ（11-20 10:30）
- 📌その他重要開示 4307 野村総研：Notice Concerning Results and Completion of Acquisition of Treasury Stock Through ToSTNet-3, and Cancellation of Treasury Stock（11-20 10:30）
- 🔁自己株式取得 7695 リフォームＴ：自己株式立会外買付取引（ToSTNeT-3）による自己株式の取得結果及び取得終了に関するお知らせ（11-20 10:00）
- 👥主要株主・大量保有 3968 セグエＧ：主要株主の異動（予定）および公開買付けに準ずる行為として政令で定める買集め行為に関する知らせ（11-20 16:00）
- 📌その他重要開示 3968 セグエＧ：Notice Regarding Expected Change in Major Shareholder and Buying Up of Shares Specified by Cabinet Order as an Act Equivalent to a Tender Offer（11-20 17:30）
- 📦特需・大口 6036 ＫｅｅＰｅｒ：2027年6月期 第1四半期 決算及び資本業務提携についての説明会ライブ配信のお知らせ（11-20 15:30）
- 📌その他重要開示 4933 Ｉｎｅ：Notice Regarding Commencement of Tender Offer for Shares, etc. of I-ne Co., Ltd. (Securities Code 4933) by JAMBO Co., Ltd.（11-20 20:00）
- 📌その他重要開示 4933 Ｉｎｅ：Notice Regarding Loss Compensation from Representative Director and President（11-20 17:45）
- 📌その他重要開示 4933 Ｉｎｅ：Notice Regarding Revision of Dividend Forecast (No Dividends) for the Fiscal Year Ending December 31, 2026 and Discontinuation of Shareholder Benefits（11-20 17:45）
- 📌その他重要開示 4933 Ｉｎｅ：当社代表取締役社長からの損失補填に関するお知らせ（11-20 17:45）
- 📌その他重要開示 4933 Ｉｎｅ：2026年12月期の配当予想の修正（無配）及び株主優待制度の廃止に関するお知らせ（11-20 17:45）
- 📌その他重要開示 4933 Ｉｎｅ：ジャンボ株式会社による株式会社Ｉ－ｎｅ（証券コード：4933）の株券等に対する公開買付けの開始に関するお知らせ（11-20 17:45）
- 📌その他重要開示 4933 Ｉｎｅ：ＭＢＯの実施に関する賛同及び応募中立の意見表明のお知らせ（11-20 17:45）
- 📌その他重要開示 4765 ＳＢＩＧＡＭ：“成長”と“分配”の両立を目指すSBIの高配当／増配株式ファンド　本日決算5ファンドの分配金に関するお知らせ（11-20 18:45）
- 📌その他重要開示 4765 ＳＢＩＧＡＭ：日本の構造変化をとらえた投資家企業「ビジネスインベスター」に投資する「ひふみビジネスインベスターpro」新規設定のお知らせ（11-20 11:30）
- 📌その他重要開示 5137 スマートＤ：役員人事に関するお知らせ（11-20 18:30）
- 📌その他重要開示 3479 ＴＫＰ：株主優待制度の拡充に関するお知らせ（11-20 17:20）
- 📌その他重要開示 3479 ＴＫＰ：連結子会社の吸収合併（簡易合併）に関するお知らせ（11-20 17:20）
- 📌その他重要開示 1721 コムシスＨＤ：（変更）法定事前開示書類（株式交換）（株式会社アイネット）（11-20 17:00）
- 📌その他重要開示 4884 クリングル：「WISH & SEEDsマッチング会2026」に当社取締役執行役員医薬開発部長の早田大真が登壇します（11-20 17:00）
- 📌その他重要開示 6277 ホソミクロン：Notice Concerning Revision of Shareholder Return Policy（11-20 16:40）
- 📌その他重要開示 6277 ホソミクロン：株主還元方針の変更に関するお知らせ（11-20 16:40）
- 📌その他重要開示 4443 Ｓａｎｓａｎ：Presentation Materials on KiteRa, Inc. Becoming a Group Company（11-20 16:30）
- 📌その他重要開示 4443 Ｓａｎｓａｎ：株式会社KiteRaのグループ会社化に関する説明資料（11-20 16:30）
- 📌その他重要開示 4443 Ｓａｎｓａｎ：Notification Regarding Acquisition of Shares in kiteRa Inc. (Making it a Subsidiary)（11-20 16:30）
- 📌その他重要開示 4443 Ｓａｎｓａｎ：株式会社KiteRaの株式の取得（子会社化）に関するお知らせ（11-20 16:30）
- 📌その他重要開示 6471 日精工：Notice Concerning Execution of Definitive Agreement Regarding Establishment of a Joint Holding Company (Share Transfer)（11-20 16:30）
- 📌その他重要開示 6471 日精工：日本精工株式会社とＮＴＮ株式会社との共同持株会社設立（株式移転）に関する最終契約書の締結について（11-20 16:30）
- 📌その他重要開示 5930 文化シヤタ：Corporate Governance Report（11-20 16:05）
- 📌その他重要開示 5930 文化シヤタ：コーポレート・ガバナンスに関する報告書 2026/11/20（11-20 15:35）
- 📌その他重要開示 5930 文化シヤタ：Notice concerning Abolition of Response Policy to Large-scale Purchase etc. of Company Share Certificates etc. in Preparation for Large-scale Purchase（11-20 15:00）
- 📌その他重要開示 5930 文化シヤタ：ダルトンらによる当社の株券等を対象とする大規模買付行為等を踏まえた当社の株券等の大規模買付行為等に関する対応方針の廃止に関するお知らせ（11-20 15:00）
- 📌その他重要開示 6925 ウシオ電：Notice Regarding Secondary Offering of Shares（11-20 16:00）
- 📌その他重要開示 6925 ウシオ電：株式の売出しに関するお知らせ（11-20 16:00）
- 📌その他重要開示 5033 ヌーラボ：当社サービス「Cacoo」の再開の目処および不正アクセスに関する現在の状況について（第三報）（11-20 15:45）
- 📌その他重要開示 5333 ＮＧＫ：Notice Regarding Disposal of Treasury Stock as Employee Shareholding Association－Restricted Stock Incentive（11-20 15:40）
- 📌その他重要開示 5333 ＮＧＫ：従業員持株会向け譲渡制限付株式インセンティブとしての自己株式の処分に関するお知らせ（11-20 15:40）
- 📌その他重要開示 1926 ライト：[Updated] Consolidated Financial Results for the Six Months Ended September 30, 2026（11-20 15:30）
- 📌その他重要開示 265A Ｈｍｃｏｍｍ：Ｈｍｃｏｍｍ、静岡市上下水道局とともに実証実験を実施 ～福山市に続き、AIによる下水道腐食リスク可視化・重点点検支援の検証を展開～（11-20 15:30）
- 📌その他重要開示 2962 テクニスコ：譲渡制限付株式報酬としての新株式の発行の払込完了に関するお知らせ（11-20 15:30）
- 📌その他重要開示 3252 地主：山口県防府市で、イオンリテールをテナントとする土地を取得（11-20 15:30）
- 📌その他重要開示 3612 ワールド：Notice Regarding Introduction of Share Compensation Plans at the Joint Holding Company and Revision of World's Restricted Share Compensation Plan（11-20 15:30）
- 📌その他重要開示 3612 ワールド：共同持株会社における株式報酬制度の導入及びワールドの譲渡制限付株式報酬制度の改定に関するお知らせ（11-20 15:30）
- 📌その他重要開示 4475 ＨＥＮＮＧＥ：Notice Regarding Partial Amendment to the Articles of Incorporation（11-20 15:30）
- 📌その他重要開示 4475 ＨＥＮＮＧＥ：定款の一部変更に関するお知らせ（11-20 15:30）
- 📌その他重要開示 5036 ＪＢＳ：Notice Regarding Dividends from Surplus（11-20 15:30）
- 📌その他重要開示 5036 ＪＢＳ：剰余金の配当に関するお知らせ（11-20 15:30）
- 📌その他重要開示 5310 東洋炭素：組織変更および人事異動に関するお知らせ（11-20 15:30）
- 📌その他重要開示 5310 東洋炭素：[Updated] Consolidated Financial Results for the Nine Months Ended September 30, 2026 (Under Japanese GAAP)（11-20 15:30）
- 📌その他重要開示 6099 エラン：Notice Regarding Revision of Full-Year Earnings Forecast（11-20 15:30）
- 📌その他重要開示 6099 エラン：通期業績予想の修正に関するお知らせ（11-20 15:30）
- 📌その他重要開示 6250 やまびこ：Summary of financial results FY26.12 3Q（11-20 15:30）
- 📌その他重要開示 6250 やまびこ：2026年12月期第3四半期決算説明資料（11-20 15:30）
- 📌その他重要開示 6479 ミネベア：[Summary]Notice Concerning Secondary Offering of Shares（11-20 15:30）
- 📌その他重要開示 6479 ミネベア：株式の売出しに関するお知らせ（11-20 15:30）
- 📌その他重要開示 6862 ミナトＨＤ：ミナトホールディングスグループのブレイン「第9回［名古屋］スマート工場 EXPO」に出展～世界シェアNo.1のZebra端末×MSI高耐久タブレットで現場のDXを最適化～（11-20 15:30）
- 📌その他重要開示 8803 平和不：サステナブルファイナンスの推進「サステナビリティ・リンク・ローン」の取り組み（11-20 15:30）
- 📌その他重要開示 9007 小田急：(October) Monthly Report of Operations (preliminary figures)（11-20 15:30）
- 📌その他重要開示 9007 小田急：2026年10月　月次営業概況（速報）に関するお知らせ（11-20 15:30）
- 📌その他重要開示 9065 山九：法定事後開示書類（会社分割）（サンキュウアセットマネジメント株式会社）（11-20 15:30）
- 📌その他重要開示 9552 クオンツ総研：Notice Regarding Borrowing of Funds（11-20 15:30）
- 📌その他重要開示 9552 クオンツ総研：資金の借入に関するお知らせ（11-20 15:30）
- 📌その他重要開示 7013 ＩＨＩ：Notice Regarding the Transfer of Non-current Assets and the Recording of Gain on Transfer（11-20 15:00）
- 📌その他重要開示 7013 ＩＨＩ：固定資産の譲渡および譲渡益の計上に関するお知らせ（11-20 15:00）
- 📌その他重要開示 8334 群馬銀：Corporate Governance Report（11-20 15:00）
- 📌その他重要開示 8334 群馬銀：コーポレート・ガバナンスに関する報告書 2026/11/24（11-20 13:46）
- 📌その他重要開示 8934 サンフロ不：サンフロンティア主催ピッチコンテスト「FRONTIER PITCH TOKYO for Startups 2026」優勝企業発表（11-20 15:00）
- 📌その他重要開示 2489 アドウェイズ：第三者割当による新株式発行及び自己株式処分に係る払込完了、並びに主要株主である筆頭株主及びその他の関係会社の異動に関するお知らせ（11-20 14:30）
- 📌その他重要開示 4165 プレイド：Notice of Investigation Results Regarding Unauthorized Access to KARTE and Outlook for Service Resumption（11-20 13:30）
- 📌その他重要開示 4165 プレイド：Notice Regarding Revision of Consolidated Financial Results Forecasts（11-20 13:30）
- 📌その他重要開示 4165 プレイド：業績予想の修正に関するお知らせ（11-20 13:00）
- 📌その他重要開示 4165 プレイド：「KARTE」への不正アクセスに関する調査結果およびサービス再開の見通しのお知らせ（11-20 13:00）
- 📌その他重要開示 1435 ロボホーム：[Delayed] Notice Concerning Change (Planned) in the Largest Shareholder and Major Shareholders, and Buying Up Equivalent to a Tender Offer（11-20 12:00）
- 📌その他重要開示 4633 サカタＩＮＸ：（Correction）Partial Correction to the "Announcement Regarding Executive Personnel Changes"（11-20 11:30）
- 📌その他重要開示 4633 サカタＩＮＸ：（訂正）「役員の異動に関するお知らせ」の一部訂正について（11-20 11:30）
- 📌その他重要開示 3036 アルコニクス：[Delayed]ALCONIX CORPORATION Financial Results for 1HFY3/27（11-20 11:00）
- 📌その他重要開示 3405 クラレ：Kuraray Receives SBTi Validation for Its Greenhouse Gas Emissions Reduction Targets（11-20 11:00）
- 📌その他重要開示 3405 クラレ：温室効果ガス排出削減目標についてSBTi による認定を取得（11-20 11:00）
- 📌その他重要開示 9025 鴻池運輸：KONOIKEグループのICT部門が新オフィスに集約（11-20 11:00）
- 📌その他重要開示 3927 Ｆ－ブレイン：2027年３月期 第２四半期決算説明会動画及び資料公開について（11-20 09:30）
- 📌その他重要開示 6971 京セラ：Notice Regarding the Recording of Non-Recurring Gain in Non-Consolidated Financial Results（11-20 08:45）
- 📌その他重要開示 6971 京セラ：個別決算における特別利益の計上に関するお知らせ（11-20 08:45）
- 📌その他重要開示 8601 大和：AIエージェントによるオンチェーン取引の実証実験に成功（11-20 08:30）

## 総当りゲート
### 5手法・スキャン（267）
- PASS（6）: 2109、2331、446A、5821、6238、9204
- PASS_DOJI（6）: 1662、1926、1975、1982、4180、4379
- FAIL_UWAHIGE（25）: 1605、1721、1951、2267、255A、2695、2810、4206、4503、4716、4746、4768、6167、6367、6418、6850、6941、7366、7630、7747、8766、9048、9107、9302、9432
- FAIL_INSEN（230）: 1435、147A、1663、167A、1960、1961、1963、1968、1979、1980、262A、268A、2760、2802、2914、2975、3036、3091、3105、3106、3110、3116、3131、3205、3374、3436、3445、3479、3498、3556、3569、3612、3798、3932、3994、4005、4008、4021、4022、4028、4042、4043、4047、4061、4062、4063、4088、408A、4095、4182、4188、4203、4205、4216、4249、4286、4293、4368、4401、4403、4410、4417、4434、4471、4478、4633、4634、4743、4771、4902、4911、4933、4966、4971、4973、4975、4980、5019、5021、5101、5137、5186、5201、5208、5246、5301、5310、5331、5333、5344、5367、5384、5444、5463、558A、5602、5703、5706、5711、5801、5832、6016、6036、6055、6071、6135、6141、6146、618A、6227、6235、6250、6268、6277、6278、6323、6332、6336、6340、6349、6368、6370、6379、6407、6432、6436、6448、6454、6471、6473、6474、6479、6481、6501、6505、6516、6524、6588、6590、6613、6617、6632、6643、6651、6652、6674、6723、6724、6741、6750、6752、6758、6762、6777、6779、6787、6804、6807、6810、6834、6845、6857、6875、6914、6918、6923、6925、6943、6952、6963、6965、6969、6971、6981、6988、7004、7148、7157、7167、7177、7186、7220、7276、7278、7322、7516、7637、7729、7731、7735、7832、7942、7995、8032、8035、8084、8133、8154、8334、8336、8343、8354、8359、8366、8370、8395、8508、8600、8616、8698、8704、8975、9037、9072、9110、9301、9303、9308、9434、9468、9503、9554、9722、9766、9843、9902、9934、9960、9962、9984
### グランビル（209）
- PASS（6）: 2326、2664、7504、7678、8056、9006
- PASS_DOJI（4）: 2488、3040、3565、4443
- FAIL_UWAHIGE（36）: 2492、2811、338A、3549、3673、3762、4025、4396、4398、4432、4507、4523、4528、4534、4686、4912、5133、5930、6099、6490、6877、6947、7269、7606、7947、8016、8051、8160、9007、9045、9104、9304、9418、9735、9742、9869
- FAIL_INSEN（163）: 1436、150A、153A、1878、1911、1925、1928、1938、1941、2206、2264、2384、2489、2502、278A、2897、2962、3002、3042、3092、3156、3182、3252、336A、3371、3399、3401、3402、3405、3491、3496、3547、3563、3692、3696、3697、3763、3793、3850、3851、3858、3891、3909、3927、3964、3968、4040、4045、4075、4091、4100、4169、417A、4204、4240、4258、428A、436A、4373、4419、4431、4475、4498、4540、4543、4554、4568、460A、4667、4674、4765、477A、479A、4848、4884、4922、4937、4968、5027、5033、5036、5105、5184、5233、5252、5256、5381、5401、5423、5532、5599、5892、6027、6072、6080、6138、6191、6317、6412、6508、6570、6574、6676、6742、6744、6745、6768、6840、6862、6904、6958、7175、7181、7184、7213、7256、7380、7480、7537、7609、7713、7715、7826、7921、7970、8012、8050、8113、8137、8159、8167、8344、8364、8377、8388、8392、8551、8609、8739、8801、8803、8804、8934、9025、9065、9075、9143、9163、9278、9279、9401、9404、9513、9536、9551、9552、9605、9697、9824、9837、9842、9889、9956
### 変化点（18）
- FAIL_INSEN（18）: 218A、265A、286A、3923、3989、4011、4165、4483、4488、4493、5803、593A、6597、6866、7318、7695、8151、9343
### 常駐観測（49）
- PASS（4）: 4684、7201、9201、9202
- PASS_DOJI（1）: 4689
- FAIL_UWAHIGE（9）: 4307、4452、4502、7741、8795、8952、9020、9501、9983
- FAIL_INSEN（35）: 1801、1812、3289、3382、3407、4519、4661、5020、5411、5713、5802、6301、6594、6920、7011、7012、7013、7182、7203、7267、8031、8058、8267、8306、8309、8316、8411、8591、8601、8604、8802、8830、8951、9433、9603
- プール外（前夜提案のみで評価）: 4259 FAIL_INSEN、7433 FAIL_INSEN
- 除籍（first_seen から30暦日超・SBIグループ登録解除候補）: 7433 Hakuto Co., Ltd.（2026-10-19〜2026-11-17）、3915 TerraSky Co., Ltd.（2026-10-20〜2026-10-29）、5537 AlbaLink Co.,Ltd.（2026-10-20〜2026-11-18）、4377 ONE CAREER Inc.（2026-10-20〜2026-11-20）、5136 tripla Co.,Ltd.（2026-10-20〜2026-11-19）、8253 Credit Saison Co., Ltd.（2026-10-20〜2026-10-21）、6668 ＡＤプラズマ（2026-10-20〜2026-11-18）、6328 Ebara Jitsugyo Co., Ltd.（2026-10-20〜2026-10-26）、4272 Nippon Kayaku Co., Ltd.（2026-10-20〜2026-11-20）、4552 JCR Pharmaceuticals Co., Ltd.（2026-10-20〜2026-11-02）、4549 Eiken Chemical Co., Ltd.（2026-10-20〜2026-10-20）、456A Human Made Inc.（2026-10-20〜2026-11-20）、8410 Seven Bank, Ltd.（2026-10-20〜2026-10-22）、6890 Ferrotec Corporation（2026-10-20〜2026-10-29）、8360 Yamanashi Chuo Bank, Ltd.（2026-10-20〜2026-10-23）、6645 OMRON Corporation（2026-10-20〜2026-10-22）、8524 North Pacific Bank, Ltd.（2026-10-20〜2026-10-22）、4259 ExaWizards Inc.（2026-10-20〜2026-11-13）
- 除籍保留（⚡材料後出しの翌営業日まで）: 6080、218A

## 機械詳細
- 候補収集: kenmo_momentum7・kenmo_newhigh1・choruko_reversal30・stf_kakuhen26・granville_tenkan10・granville_oshime10・granville_rebound10・ai_reversal2・dm_momentum1・dm_reversal3・an_reversal1・sr_reversal1・changepoint5・熟成0・未マージPR由来0（直近24時間のリモートブランチは main と本ブランチのみ）
- プール: 543（前夜533・新規指名28・常駐観測の新規0・除籍18・除籍保留2）
- 検知内訳: PASS 16・PASS_DOJI 11・上髭FAIL 70・陰線FAIL 448・SKIP 0・log 追記1件
- ヘッドライン: PASS 27件中 27件付与・業態 キャッシュヒット23／新規取得4／未取得0・kabutan トップ新規取得 7/50件（打ち切り0・業種埋め戻し0件・profile_cache 総数1098・本夜追加4）・決算ページ 27件
- 通知の抜粋: 10件（method4/ai2/granville4/changepoint0/不明0）／提案の群別 method4/ai0/granville4/changepoint0/不明0
- gate_history: gate_history/2026-11-20.json を新規作成（verdicts 545件＝評価545件／nominations 174件（新規28・再指名146））
- grades.json: 1142銘柄/680KB・業種別PER中央値 26業種（spm 付与1050件）
- pool_bars.json: 546銘柄/468KB（1306 含む）
- earnings_calendar.json: 1186銘柄/156KB・次回決算日 付与215件（一覧53/kabutan162）・未発表971件・前年同期発表日 付与501件
- method_score: 保持70件／null473件
- earnings_log: 総数508／本夜追記1件／リターン補完66件／日足が取れず未補完164件・gyoseki history 退避0件（再計算未実施）
- 鮮度ゲート: 鮮度切れ除外6件・nom_age分布 0-2:251/3-10:149/11+:143・last_seen欠損0件
- 記録の凍結: 業種 付与済み479/未付与64（本夜埋め戻し0件）
- トレンド文脈: ctx 不一致154／ctx 合致120／ctx レンジ172／ctx 判定不能2／ctx 不一致（長期下向き）95・PASS のうち ctx 合致5件・形態が付いた銘柄279件
- 3日ルール: 判定0銘柄・streak≥3 0・streak=2 0・判定不可0（保有0）
- 開示の分類別件数: 📌81・👥1・🔁3・📦1・📊1
- 熟成由来の候補 0件
- 権利情報: rights_cache 総数503・本夜 配当更新0件／優待取得0件（T+1/T+2 に権利落ちなし・保有0のため取得せず。minkabu 優待ページは 403）
- STEP 4.8: 実行（week_open=true）
- master.json 変更行数: +13122/-13705
- 業績グレード: 再計算は未実施（キャッシュ値を使用）。📊/📢/📉 の該当は recalc_queue へ
- 抜粋（通知の通過10件）: 5821、446A、6238、4379、1975、1982、9006、2488、8056、4443
