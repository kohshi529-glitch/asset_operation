# 夜間ゲート 2026-11-17

## サマリー
- 評価数: 460 / PASS: 69（PASS_DOJI 11件を含む）
- 発注可能提案数: 41件（✅36／⏳4／⏸位置不適1／⏸トラップ疑い0）
- 市場一言: 市場モード「弱気」（market.latest 2026-11-17・半導体主導リスクオフ（AIトレード疲労））。プール460銘柄中 PASS比率15.0%（陰線FAIL 311件・上髭FAIL 80件）
- 実行モード: 通常（base_day=当日の引け値を対象。11/17(火)=営業日・翌11/18(水)=営業日）
- base_day: 2026-11-17（run_at 2026-11-17 20:30）
- week_open: false（翌営業日 11/18(水)＝週中）→ STEP 4.8 はスキップ
- 📆 翌営業日 11/18: カレンダーイベントなし（T+2 11/19: カレンダーイベントなし）
- 📑指数: 低減対象 提案6件／PASS15件／プール74件・新規採用 8件（index_flags 2026-10-07 公表分）・次の TOPIX 低減日 01/29 第2回/8（あと49営業日）

## 検証結果
- V1 → はい（提案41=results41=模擬41=通知母数41）
- V2 → はい（PASS69=提案41+除外28・order_status欠落0）
- V3 → はい（results460件重複0）
- V4 → はい（既存static変更0）
- V5 → はい（変更トップキー['earnings_log', 'night_gate', 'pipeline', 'profile_cache', 'valuation_cache']・pipeline他run不変True・spec不変True・profile既存書換なしTrue）
- V6 → はい（gyoseki_cache不整合0）
- V7 → はい（必須セクション存在・week_open=false のため📅今週のカタリストは対象外）
- V8 → はい（模擬41行 不正0）
- V9 → はい（gate_history と today 一致）
- V10 → はい（base_day一致 2026-11-17）
- V11 → いいえ（+10294/-8270（indent=2・往復一致で検出・仮ファイル経由））
- V12 → はい（並び順 (a)True(b)True(c)True）
- V13 → はい（1109銘柄/619.8KiB・GC∪VC∪PC1109全収録True・20キーTrue・型True・nx一致True・ix非null225・業種PER中央値26業種・pg範囲外0）
- V14 → はい（保持73件/null387件・出所不明0=True・写し一致=True・内訳{'kenmo_momentum': 11, 'stf_kakuhen': 25, 'granville_rebound': 2, 'kenmo_newhigh': 1, 'ai_reversal': 12, 'choruko_reversal': 20, 'granville_oshime': 2}）
- V15 → はい（PASS69件中69件に付与（欠落0）・5キーTrue・(c)4項目の未取得/取得不可12（業績グレード名のキャッシュ転記を含む））
- V16 → はい（📊0件（pool内に決算短信の開示なし）・grade_beforeは再計算前（本夜は業績再計算なし）・history>4=0・総数504）
- V17 → はい（461銘柄/393.2KiB・先読み0=True・保有0銘柄（収録対象なし）・3日ルール判定0銘柄）
- V18 → はい（鮮度切れ14件・誤除外0=True・nom_age分布 0-2:164/3-10:189/11+:107・欠損99=0）
- V19 → はい（verdicts460=評価460・nominations100（新規25/再指名75）・集合一致True・ctx判定不能1・(d)True・(e)True）
- V20 → はい（1126銘柄・nx非null212・hist持ち774・pxd371・取得元名称なしTrue）
- V21 → はい（recent_pass514銘柄・出所実在True・保有情報不使用True（保有0銘柄））
- V22 → はい（PASS_DOJI11・⏸位置不適1誤通過0=True・⏸トラップ0・rs20付与460/460・RSチップ整合True）
- VLEAK → はい（公開物（ボード/today/gate_history）への保有情報 検出0件（保有0銘柄））
- 注: V11 は night_gate.results の全置換（460件）と pool 更新による実データ差分であり全体再フォーマットではない（往復一致で W=2 を検出し同一幅で書き出し）。前夜（+12518/-16876）と同じ構造的超過

## 保有アラート
保有0銘柄・アラート0件（詳細は通知）

## 🧾直近提案の決算接近
窓内（直近20営業日）の提案銘柄 514・日程不明 479・当夜評価外 165。保有情報は使っていない（候補だった銘柄の日程）
- 📉決算反応日 11/17 4021 Nissan Chemical Corporation｜最後の提案 11/17（reversal 6669・✅即時可）｜提案2回｜当夜 PASS
- 📉決算反応日 11/17 5252 日本ナレッジ｜最後の提案 11/13（reversal 1000.0・✅即時可）｜提案4回｜当夜 FAIL_INSEN
- 📉決算反応日 11/17 9960 トーテック｜最後の提案 11/13（reversal 4515.0・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- 📉決算反応日 11/17 6741 日本信号｜最後の提案 11/12（reversal 1667・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 📉決算反応日 11/17 6890 Ferrotec Corporation｜最後の提案 11/11（reversal 7617・✅即時可）｜提案4回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/17 478A Hutzper Inc.｜最後の提案 11/10（changepoint 668・✅即時可）｜提案4回｜当夜 評価外
- 📉決算反応日 11/17 5105 ＴＯＹＯ　ＴＩＲＥ｜最後の提案 11/09（momentum 4249・✅即時可）｜提案2回｜当夜 PASS
- 📉決算反応日 11/17 4088 Air Water Inc.｜最後の提案 10/29（reversal 2877.0・✅即時可）｜提案2回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/17 5582 （名称取得不可）｜最後の提案 10/29（changepoint 1819.0・✅即時可）｜提案3回｜当夜 評価外
- ⏰決算 11/19(残2営業日) 8986 Daiwa Securities Living Investment Corporation｜最後の提案 10/26（reversal 83900.0・✅即時可）｜提案1回｜当夜 評価外
- 📋カルテ窓 12/15(残19営業日) 5136 tripla Co.,Ltd.｜最後の提案 11/17（momentum 2730・✅即時可）｜提案6回｜当夜 PASS
- 📋カルテ窓 12/11(残17営業日) 6336 石井表記｜最後の提案 11/17（reversal 1164・✅即時可）｜提案3回｜当夜 PASS
- 📋カルテ窓 12/11(残17営業日) 446A ノースサンド｜最後の提案 11/16（momentum 2631・⏸位置不適(25MA下 -2.7%)）｜提案5回｜当夜 FAIL_INSEN
- 📋カルテ窓 12/16(残20営業日) 8975 Ichigo Office REIT Investment Corporation｜最後の提案 11/16（reversal 88800・✅即時可）｜提案6回｜当夜 PASS
- 📋カルテ窓 12/09(残15営業日) 7678 ASAKUMA CO.,LTD.｜最後の提案 11/13（momentum 4450・✅即時可）｜提案4回｜当夜 評価外
- 📋カルテ窓 12/15(残19営業日) 3565 Ascentech KK｜最後の提案 11/12（reversal 453・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 📋カルテ窓 12/11(残17営業日) 218A Liberaware｜最後の提案 11/11（changepoint 830・✅即時可）｜提案6回｜当夜 FAIL_INSEN
- 📋カルテ窓 12/10(残16営業日) 3491 ＧＡ　ｔｅｃｈｎｏｌｏｇｉｅｓ（ＧＡテクノ）｜最後の提案 11/11（momentum 1568・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- 📋カルテ窓 12/14(残18営業日) 460A ＢＲＡＮＵ｜最後の提案 11/11（reversal 1098・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 📋カルテ窓 12/08(残14営業日) 9824 泉州電業｜最後の提案 11/11（momentum 7880・⏸位置不適(25MA下 -2.36%)）｜提案5回｜当夜 評価外
- 📋カルテ窓 12/08(残14営業日) 1436 GreenEnergy & Company｜最後の提案 11/10（reversal 1368・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 📋カルテ窓 12/04(残12営業日) 436A サイバーソリューションズ（サイバＳＯＬ）｜最後の提案 11/10（oshime 1776・✅即時可）｜提案1回｜当夜 FAIL_UWAHIGE
- 📋カルテ窓 12/10(残16営業日) 1928 積水ハウス｜最後の提案 11/09（momentum 3568・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- 📋カルテ窓 12/11(残17営業日) 4075 ブレインズテクノロジー｜最後の提案 11/09（reversal 1037・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- 📋カルテ窓 12/09(残15営業日) 5132 pluszero,Inc.｜最後の提案 11/04（momentum 1761・✅即時可）｜提案1回｜当夜 評価外
- 📋カルテ窓 12/15(残19営業日) 9163 Nareru Group Inc.｜最後の提案 11/04（momentum 2088・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- 📋カルテ窓 12/11(残17営業日) 3653 Morpho, Inc.｜最後の提案 10/29（reversal 918.0・✅即時可）｜提案3回｜当夜 評価外
- 📋カルテ窓 12/10(残16営業日) 8927 Meiho Enterprise Co., Ltd.｜最後の提案 10/29（momentum 466.0・✅即時可）｜提案1回｜当夜 評価外
- 📋カルテ窓 12/15(残19営業日) 4431 スマレジ｜最後の提案 10/28（oshime 3707.6・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- 📋カルテ窓 12/11(残17営業日) 186A Astroscale Holdings Inc.｜最後の提案 10/27（momentum 1084.0・✅即時可）｜提案4回｜当夜 評価外
- 📋カルテ窓 12/15(残19営業日) 212A FIT EASY Inc.｜最後の提案 10/27（momentum 2771.0・✅即時可）｜提案1回｜当夜 評価外
- 📋カルテ窓 12/11(残17営業日) 456A Human Made Inc.｜最後の提案 10/27（oshime 1940.0・✅即時可）｜提案3回｜当夜 PASS
- 📋カルテ窓 12/15(残19営業日) 4666 Park24 Co., Ltd.｜最後の提案 10/26（reversal 1850.0・✅即時可）｜提案1回｜当夜 評価外
- 📋カルテ窓 12/11(残17営業日) 4382 HEROZ, Inc.｜最後の提案 10/21（changepoint 1631.0・✅即時可）｜提案1回｜当夜 評価外
- 📋カルテ窓 12/14(残18営業日) 9166 GENDA Inc.｜最後の提案 10/21（oshime 673.5・✅即時可）｜提案1回｜当夜 評価外

## 前夜の結果
PL5口座への正式な反映は週次①-11の採点で行われる。ここは参考情報
前夜2026-11-16の提案23件 → 約定14・不約定9・判定不能0
- 6071 momentum 注文1077｜2026-11-17 O1058.0 H1060.0 L1023.0 C1027.0｜不約定
- 262A momentum 注文1679｜2026-11-17 O1667.0 H1667.0 L1593.0 C1593.0｜不約定
- 6167 momentum 注文1131｜2026-11-17 O1145.0 H1148.0 L1093.0 C1106.0｜不約定
- 446A momentum 注文2631｜2026-11-17 O2550.0 H2580.0 L2329.0 C2329.0｜不約定
- 5021 reversal 注文3495｜2026-11-17 O3396.0 H3417.0 L3345.0 C3373.0｜約定 3396.0 終値比-0.68%
- 7276 reversal 注文2541｜2026-11-17 O2510.5 H2535.0 L2494.0 C2507.0｜約定 2510.5 終値比-0.14%
- 4768 reversal 注文3808｜2026-11-17 O3811.0 H3841.0 L3751.0 C3803.0｜約定 3808 終値比-0.13%
- 8975 reversal 注文88800｜2026-11-17 O88800.0 H89400.0 L88300.0 C89200.0｜約定 88800 終値比+0.45%
- 3612 reversal 注文1522｜2026-11-17 O1525.0 H1526.0 L1500.0 C1508.0｜約定 1522 終値比-0.92%
- 8804 momentum 注文3464｜2026-11-17 O3450.0 H3454.0 L3384.0 C3395.0｜不約定
- 2206 momentum 注文5160｜2026-11-17 O5174.0 H5185.0 L5121.0 C5142.0｜約定 5174.0 終値比-0.62%
- 8016 momentum 注文815｜2026-11-17 O807.0 H808.0 L798.0 C802.0｜不約定
- 3092 momentum 注文1210｜2026-11-17 O1204.0 H1213.0 L1190.5 C1211.5｜約定 1210 終値比+0.12%
- 8160 momentum 注文2600｜2026-11-17 O2589.0 H2630.0 L2586.0 C2603.0｜約定 2600 終値比+0.12%
- 9956 momentum 注文1661｜2026-11-17 O1667.0 H1674.0 L1647.0 C1656.0｜約定 1667.0 終値比-0.66%
- 9404 momentum 注文3052｜2026-11-17 O3033.0 H3033.0 L2982.0 C2991.0｜不約定
- 2897 momentum 注文2999｜2026-11-17 O2994.5 H3012.0 L2970.5 C2991.5｜約定 2999 終値比-0.25%
- 2811 momentum 注文2888.5｜2026-11-17 O2890.0 H2900.0 L2871.0 C2879.5｜約定 2890.0 終値比-0.36%
- 9605 momentum 注文6290｜2026-11-17 O6200.0 H6200.0 L6120.0 C6180.0｜不約定
- 6191 oshime 注文1442｜2026-11-17 O1542.0 H1608.0 L1529.0 C1567.0｜不約定
- 3851 reversal 注文930｜2026-11-17 O920.0 H926.0 L894.0 C917.0｜約定 920.0 終値比-0.33%
- 6317 reversal 注文2785｜2026-11-17 O2835.0 H2835.0 L2694.0 C2723.0｜約定 2785 終値比-2.23%
- 6904 reversal 注文689｜2026-11-17 O679.0 H684.0 L655.0 C657.0｜約定 679.0 終値比-3.24%

## 模擬テンプレ
```
# base_day 2026-11-17 ／ 提案41件
# 使い方: 参戦する0〜3銘柄の行だけをコピーし、｜の後ろに参戦理由を書いてポジション株PJへ送る。
# 選ばなかった行は送らなくてよい（全行に理由を書く必要はない）。見送りは末尾の1行で足りる。
# 特定銘柄を理由つきで見送る場合のみ『模擬 見送り {code} ｜{理由}』を送る。
模擬 5136 kenmo_momentum 逆指値2730 SL2565.3 単元100 ｜
模擬 5821 kenmo_momentum 逆指値3195 SL2998.6 単元100 ｜
模擬 558A kenmo_momentum 逆指値6200 SL5818.6 単元100 ｜
模擬 4933 kenmo_newhigh 逆指値2501 SL2350 単元100 ｜
模擬 7433 choruko_reversal 指値1531 SL1512 単元100 ｜
模擬 4216 choruko_reversal 指値5500 SL5340 単元100 ｜
模擬 167A choruko_reversal 指値3085 SL3010 単元100 ｜
模擬 6588 choruko_reversal 指値2468 SL2400 単元100 ｜
模擬 6952 choruko_reversal 指値2028.5 SL1940.5 単元100 ｜
模擬 6754 choruko_reversal 指値2245 SL2153.5 単元100 ｜
模擬 5186 choruko_reversal 指値6140 SL6040 単元100 ｜
模擬 4205 choruko_reversal 指値2018.5 SL1982.5 単元100 ｜
模擬 5444 choruko_reversal 指値10865 SL10655 単元100 ｜
模擬 4403 choruko_reversal 指値2627 SL2501 単元100 ｜
模擬 4021 choruko_reversal 指値6669 SL6525 単元100 ｜
模擬 6750 choruko_reversal 指値1917 SL1799 単元100 ｜
模擬 4028 choruko_reversal 指値2604 SL2550 単元100 ｜
模擬 6804 choruko_reversal 指値2145 SL2074 単元100 ｜
模擬 6807 choruko_reversal 指値2263 SL2221 単元100 ｜
模擬 6632 choruko_reversal 指値796 SL781 単元100 ｜
模擬 5101 choruko_reversal 指値7482 SL6889 単元100 ｜
模擬 8698 choruko_reversal 指値591 SL577 単元100 ｜
模擬 6918 ai_reversal 指値2780 SL2700 単元100 ｜
模擬 4368 ai_reversal 指値2690 SL2584 単元100 ｜
模擬 2760 ai_reversal 指値3825 SL3700 単元100 ｜
模擬 5384 ai_reversal 指値2775 SL2699 単元100 ｜
模擬 6336 ai_reversal 指値1164 SL1125 単元100 ｜
模擬 2802 ai_reversal 指値4155 SL4018 単元100 ｜
模擬 3964 granville_tenkan 逆指値1274 SL1241 単元100 ｜
模擬 3092 granville_tenkan 逆指値1214 SL1140.2 単元100 ｜
模擬 6412 granville_tenkan 逆指値2159 SL2028.5 単元100 ｜
模擬 6877 granville_oshime 指値6828 SL6794.4 単元100 ｜
模擬 3851 granville_rebound 逆指値927 SL885 単元100 ｜
模擬 2489 granville_rebound 指値316 SL310 単元100 ｜
模擬 7609 granville_rebound 指値3540 SL3450 単元100 ｜
模擬 5256 granville_rebound 指値2581 SL2320 単元100 ｜
模擬 3850 granville_rebound 指値3225 SL3185 単元100 ｜
模擬 5599 granville_rebound 逆指値1444 SL1364 単元100 ｜
模擬 8551 granville_rebound 指値2112 SL2073 単元100 ｜
模擬 3858 granville_rebound 逆指値399 SL367 単元100 ｜
模擬 3989 changepoint🔔 指値1548 SL1533 単元100 🔒 ｜
模擬 見送り ｜
```

## PASS内訳
PASS 69件 = 提案 41件（✅即時可36／⏳待機・確認足待ち4／⏸位置不適1／⏸トラップ疑い0） + 除外 28件（型不一致9（うち十字線4）/材料後出し2/鮮度切れ14/その他3）
- 3843 Freebit Co., Ltd.｜⛔提案なし(指名鮮度切れ 19営業日)｜nom_age 19
- 6925 Ushio Inc.｜⛔提案なし(指名鮮度切れ 17営業日)｜nom_age 17
- 6875 メガチップス｜⛔提案なし(指名鮮度切れ 12営業日)｜nom_age 12
- 8975 Ichigo Office REIT Investment Corporation｜⛔提案なし(指名鮮度切れ 11営業日)｜nom_age 11
- 8359 Hachijuni Nagano Bank, Ltd.｜⛔提案なし(指名鮮度切れ 13営業日)｜nom_age 13
- 6969 松尾電機｜⛔提案なし(手法ブランチ不明)｜nom_age 0
- 6532 ベイカレント｜⛔提案なし(手法ブランチ不明)｜nom_age 2
- 7366 ＬＩＴＡＬＩＣＯ（りたりこ）｜⛔提案なし(手法ブランチ不明)｜nom_age 0
- 4973 JCU｜⛔提案なし(指名鮮度切れ 11営業日)｜nom_age 11
- 6768 Tamura Corporation｜⛔提案なし(指名鮮度切れ 13営業日)｜nom_age 13
- 4922 コーセーホールディングス｜⛔提案なし(指名鮮度切れ 12営業日)｜nom_age 12
- 6328 Ebara Jitsugyo Co., Ltd.｜⛔提案なし(指名鮮度切れ 15営業日)｜nom_age 15
- 5105 ＴＯＹＯ　ＴＩＲＥ｜⛔提案なし(指名鮮度切れ 15営業日)｜nom_age 15
- 7480 スズデン｜⛔型不一致(既に支持帯以下)｜nom_age 0
- 4258 AMIYA Corporation｜⛔型不一致(十字線: トウバ)｜nom_age 1
- 7970 Shin-Etsu Polymer Co., Ltd.｜⛔型不一致(既に支持帯以下)｜nom_age 0
- 2384 ＳＢＳホールディングス｜⛔型不一致(既に支持帯以下)｜nom_age 6
- 4398 ブロードバンドセキュリティ｜⛔型不一致(十字線: トウバ)｜nom_age 8
- 456A Human Made Inc.｜⛔型不一致(既に支持帯以下)｜nom_age 0
- 6027 Bengo4.com, Inc.｜⛔型不一致(既に支持帯以下)｜nom_age 9
- 4968 Arakawa Chemical Industries,Ltd.｜⛔型不一致(十字線: 下放れ直後)｜nom_age 8
- 6508 Meidensha Corporation｜⛔提案なし(指名鮮度切れ 11営業日)｜nom_age 11
- 5367 Nikkato Corporation｜⛔提案なし(指名鮮度切れ 11営業日)｜nom_age 11
- 8344 Yamagata Bank, Ltd.｜⛔型不一致(十字線: 下放れ直後)｜nom_age 7
- 7256 河西工業｜⛔提案なし(指名鮮度切れ 15営業日)｜nom_age 15
- 6676 BUFFALO INC.｜⛔提案なし(材料後出し)｜nom_age 1
- 4884 Kringle Pharma, Inc.｜⛔提案なし(材料後出し)｜nom_age 3
- 8739 スパークス・グループ｜⛔提案なし(指名鮮度切れ 15営業日)｜nom_age 15

## 5手法銘柄
- 4434 Serverworks Co., Ltd.｜kenmo_momentum｜業績 🚀確変｜値頃 ⚪妥当｜FAIL_UWAHIGE｜終値3015.0｜💰30.5万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 5136 tripla Co.,Ltd.｜kenmo_momentum/granville_oshime/changepoint/changepoint🔔🔔/changepoint🔔｜業績 🚀確変｜値頃 ⚪妥当｜PASS｜終値2710.0｜💰27.1万円｜momentum 2730 SL2565.3 上限2757.3・✅即時可・乖離0.7%｜📋カルテ窓 12/15(残19営業日)
  > 📌【業態】宿泊予約システムや会話ツールのAIチャットボットシステム提供。決済システムも。アジアに拡大。
  > 📌【いま】終値2,710円・直近5日+0.11%（材料未確認）
  > 📌【調子】🚀確変（11/13）
  > 📌【水準】⚪妥当（3.0/7）— PER26.78倍・PEG0.454・52週93.9% ／ 💰単元27.1万円
  > 📌【戦略】当日高値超えの逆指値2730円で順張り参戦を検討。上限2757.3円・SL2565.3円目安
- 8704 TRADERS HOLDINGS CO LTD｜kenmo_momentum｜業績 🔥絶好調｜値頃 💎割安｜FAIL_INSEN｜終値1206.0｜💰12.7万円｜⚠日程不明
- 3915 TerraSky Co., Ltd.｜kenmo_momentum｜業績 🔥絶好調｜値頃 🟢値頃｜FAIL_INSEN｜終値1942.0｜💰20.9万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 147A SORACOM,INC.｜kenmo_momentum｜業績 🔥絶好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値982.0｜💰9.8万円｜⚠日程不明
- 4286 CL Holdings Inc.｜kenmo_momentum/kenmo_newhigh｜業績 🔥絶好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値1479.0｜💰14.7万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 6418 Japan Cash Machine Co., Ltd.｜kenmo_momentum/kenmo_newhigh/granville_oshime｜業績 🔥絶好調｜値頃 ⚪妥当｜FAIL_UWAHIGE｜終値1416.0｜💰14.6万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 5537 AlbaLink Co.,Ltd.｜kenmo_momentum/granville_oshime/granville_rebound｜業績 🔥絶好調｜値頃 ⚪妥当｜FAIL_UWAHIGE｜終値3450.0｜💰34.4万円｜⚠日程不明
- 5137 Smart Drive Co. Ltd.｜kenmo_momentum/granville_oshime｜業績 🔥絶好調｜値頃 💎割安｜FAIL_INSEN｜終値301.0｜💰2.9万円｜⚠日程不明
- 6071 IBJ, Inc.｜kenmo_momentum/kenmo_newhigh/stf_kakuhen｜業績 🔥絶好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値1027.0｜💰10.8万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 7637 Hakudo Co., Ltd.｜kenmo_momentum｜業績 🔥絶好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値3400.0｜💰36.7万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 4377 ONE CAREER Inc.｜kenmo_momentum/stf_kakuhen/granville_oshime/granville_rebound｜業績 🔥絶好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値2500.0｜💰26.6万円｜⚠日程不明
- 4249 MORIROKU COMPANY LTD.｜kenmo_momentum｜業績 🔥絶好調｜値頃 🟢値頃｜FAIL_INSEN｜終値2864.0｜💰29.7万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 4053 Sun Asterisk, Inc.｜kenmo_momentum｜業績 🔥絶好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値576.0｜💰5.5万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 4771 F&M Co., Ltd.｜kenmo_momentum/kenmo_newhigh｜業績 🔥絶好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値2957.0｜💰30.1万円｜⚠日程不明
- 1435 robot home Inc.｜kenmo_momentum｜業績 ⚡好調｜値頃 💎割安｜FAIL_INSEN｜終値165.0｜💰1.6万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 3556 RenetJapanGroup, Inc.｜kenmo_momentum/granville_tenkan｜業績 ⚡好調｜値頃 💎割安｜FAIL_INSEN｜終値881.0｜💰9.2万円｜⚠日程不明
- 5821 Hirakawa Hewtech Corp.｜kenmo_momentum｜業績 ⚡好調｜値頃 💎割安｜PASS｜終値3160.0｜💰31.6万円｜momentum 3195 SL2998.6 上限3226.9・⏸位置不適(52週 23.8%)・乖離1.1%｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8） 📐進捗 上振れ 11.8%
  > 📌【業態】電線・放送機器メーカー。光中継システム等。医療用チューブも展開。海外でも生産。
  > 📌【いま】終値3,160円・直近5日-3.95%（材料未確認）
  > 📌【調子】⚡好調（7/13）— 上方修正済み・🔼進捗先行
  > 📌【水準】💎割安（6.0/7）— PER11.99倍・PEG0.524・52週23.8% ／ 💰単元31.6万円
  > 📌【戦略】当日高値超えの逆指値3195円で順張り参戦を検討。上限3226.9円・SL2998.6円目安
- 558A SQUEEZE Inc.｜kenmo_momentum｜業績 ⚡好調｜値頃 🟡やや割高｜PASS｜終値6110.0｜💰61.1万円｜momentum 6200 SL5818.6 上限6262.0・✅即時可・乖離1.5%｜⚠日程不明 ⚠1単元でリスク枠超過（38,140円）
  > 📌【業態】自社ホテル運営や、システム開発・提供、宿泊施設の企画・開発などを手掛ける。
  > 📌【いま】終値6,110円・直近5日+9.50%（材料未確認）
  > 📌【調子】⚡好調（7/13）— D軸判定不能(四半期データ不足・中立1点)・E軸判定不能(進捗データ不足)・🔼進捗先行
  > 📌【水準】🟡やや割高（2.8/7）— PER38.92倍・PEG1.176・52週84% ／ 💰単元61.1万円
  > 📌【戦略】当日高値超えの逆指値6200円で順張り参戦を検討。上限6262.0円・SL5818.6円目安／⚠1単元リスク38,140円（枠超過）
- 2975 Star Mica Holdings Co., Ltd.｜kenmo_momentum｜業績 ⚡好調｜値頃 💎割安｜FAIL_INSEN｜終値1162.0｜💰12.2万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 9554 AViC Co. Ltd.｜kenmo_momentum｜業績 ⚡好調｜値頃 💎割安｜FAIL_UWAHIGE｜終値1765.0｜💰16.1万円｜⚠日程不明
- 262A INTERMESTIC INC.｜kenmo_momentum｜業績 ⚡好調｜値頃 💎割安｜FAIL_INSEN｜終値1593.0｜💰16.7万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8） ⚡材料後出し
- 3798 ULS Group Incorporated｜kenmo_momentum/granville_tenkan｜業績 ✅順調｜値頃 💎割安｜FAIL_INSEN｜終値478.0｜💰4.9万円｜⚠日程不明 ⚡材料後出し
- 4743 ITFOR Inc.｜kenmo_momentum｜業績 ✅順調｜値頃 💎割安｜FAIL_INSEN｜終値1599.0｜💰16.2万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 6167 FUJI DIE Co., Ltd.｜kenmo_momentum｜業績 ✅順調｜値頃 🟡やや割高｜FAIL_INSEN｜終値1106.0｜💰11.3万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 618A KOMPEITO Inc.｜kenmo_momentum/kenmo_newhigh｜業績 取得不可｜値頃 ⚪妥当｜FAIL_INSEN｜終値1862.0｜💰20.8万円｜⚠日程不明
- 6943 ＮＫＫスイッチズ｜kenmo_newhigh｜業績 🚀確変｜値頃 🟢値頃｜FAIL_INSEN｜終値7030.0｜💰69.9万円｜⚠日程不明
- 446A ノースサンド｜kenmo_newhigh/granville_oshime/granville_rebound｜業績 🔥絶好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値2329.0｜💰26.0万円｜📋カルテ窓 12/11(残17営業日) ⚡材料後出し
- 3843 Freebit Co., Ltd.｜kenmo_newhigh/granville_tenkan｜業績 ✅順調｜値頃 🟡やや割高｜PASS｜終値2070.0｜💰20.7万円｜⛔提案なし(指名鮮度切れ 19営業日)｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
  > 📌【業態】ネット接続にインフラ提供サービス。ドコモと提携、MVNOトーン運営。企業DX支援も展開。
  > 📌【いま】終値2,070円・直近5日+5.08%（材料未確認）
  > 📌【調子】✅順調（4/13）
  > 📌【水準】🟡やや割高（2.0/7）— PER10.04倍・PEG2.007・52週94.5% ／ 💰単元20.7万円
  > 📌【戦略】発注対象外（⛔提案なし(指名鮮度切れ 19営業日)）
- 4379 Photosynth inc.｜kenmo_newhigh｜業績 ✅順調｜値頃 🔴過熱｜FAIL_INSEN｜終値436.0｜💰4.5万円｜⚠日程不明
- 9204 Skymark Airlines Inc.｜kenmo_newhigh｜業績 🔻悪化｜値頃 🔴過熱｜FAIL_UWAHIGE｜終値502.0｜💰4.9万円｜⚠日程不明
- 1960 サンテック｜kenmo_newhigh｜業績 ➖横ばい｜値頃 🔴過熱｜FAIL_INSEN｜終値1728.0｜💰18.4万円｜⚠日程不明
- 4933 I-ne CO., LTD.｜kenmo_newhigh｜業績 取得不可｜値頃 ⚪妥当｜PASS｜終値2489.0｜💰24.9万円｜momentum 2501 SL2350 上限2526.0・✅即時可・乖離0.5%｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
  > 📌【業態】ヘアケア製品と美容家電が主力。化粧品や健康食品関連の開発・販売を展開。
  > 📌【いま】終値2,489円・直近5日-0.76%（材料未確認）
  > 📌【調子】取得不可（—/13）— 業績データ取得不可(経常益予想非開示)・🔼加速
  > 📌【水準】⚪妥当（3.0/7）— PER—倍・PEG—・52週94.2% ／ 💰単元24.9万円
  > 📌【戦略】当日高値超えの逆指値2501円で順張り参戦を検討。上限2526.0円・SL2350円目安
- 6238 フリュー｜kenmo_newhigh｜業績 —｜値頃 —｜FAIL_UWAHIGE｜終値1688.0｜💰—｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 6278 ユニオンツール｜choruko_reversal｜業績 🚀確変｜値頃 🟢値頃｜FAIL_INSEN｜終値10050.0｜💰114.7万円｜⚠日程不明
- 5711 三菱マテリアル｜choruko_reversal｜業績 🚀確変｜値頃 💎割安｜FAIL_INSEN｜終値4002.0｜💰43.1万円｜⚠日程不明
- 6481 THK Co., Ltd.｜choruko_reversal｜業績 🚀確変｜値頃 💎割安｜FAIL_INSEN｜終値4512.0｜💰54.7万円｜⚠日程不明
- 3036 アルコニックス｜choruko_reversal｜業績 🚀確変｜値頃 🟢値頃｜FAIL_INSEN｜終値3000.0｜💰31.8万円｜⚠日程不明
- 6324 Harmonic Drive Systems Inc.｜choruko_reversal｜業績 🚀確変｜値頃 🟢値頃｜FAIL_INSEN｜終値4223.0｜💰49.9万円｜⚠日程不明
- 7995 Valqua Ltd.｜choruko_reversal/granville_rebound｜業績 🚀確変｜値頃 🟢値頃｜FAIL_INSEN｜終値5780.0｜💰61.8万円｜⚠日程不明
- 6516 Sanyo Denki Co., Ltd.｜choruko_reversal/ai_reversal｜業績 🔥絶好調｜値頃 💎割安｜FAIL_UWAHIGE｜終値4385.0｜💰45.5万円｜⚠日程不明
- 7433 Hakuto Co., Ltd.｜choruko_reversal/ai_reversal/granville_oshime/granville_rebound｜業績 🔥絶好調｜値頃 💎割安｜PASS｜終値1531.0｜💰15.3万円｜reversal 1531 SL1512・✅即時可｜⚠日程不明
  > 📌【業態】エレクトロニクス商社。半導体製造装置に強み。工業薬品製造も併営。海外開拓。
  > 📌【いま】終値1,531円・直近5日-3.04%（材料未確認）
  > 📌【調子】🔥絶好調（10/13）
  > 📌【水準】💎割安（6.0/7）— PER13.51倍・PEG0.25・52週41.4% ／ 💰単元15.3万円
  > 📌【戦略】当日終値1531円の指値で反転を取りにいく。SL1512円（直近5日安値）
- 5344 MARUWA CO., LTD.｜choruko_reversal｜業績 🔥絶好調｜値頃 🟢値頃｜FAIL_UWAHIGE｜終値39720.0｜💰458.6万円｜⚠日程不明
- 6645 OMRON Corporation｜choruko_reversal/granville_rebound｜業績 🔥絶好調｜値頃 🟢値頃｜FAIL_INSEN｜終値4580.0｜💰49.4万円｜⚠日程不明
- 4216 ASAHI YUKIZAI CORPORATION｜choruko_reversal｜業績 🔥絶好調｜値頃 💎割安｜PASS｜終値5500.0｜💰55.0万円｜reversal 5500 SL5340・✅即時可｜⚠日程不明 📐進捗 遅れ -15.1%
  > 📌【業態】旭化成系で樹脂バルブの独占的メーカー。水資源開発も。中国・アジア市場を開拓。
  > 📌【いま】終値5,500円・直近5日+0.73%（材料未確認）
  > 📌【調子】🔥絶好調（9/13）— 上方修正済み・⚠進捗遅れ
  > 📌【水準】💎割安（6.0/7）— PER12.61倍・PEG0.231・52週32.6% ／ 💰単元55.0万円
  > 📌【戦略】当日終値5500円の指値で反転を取りにいく。SL5340円（直近5日安値）
- 4471 三洋化成工業｜choruko_reversal/granville_oshime/granville_rebound｜業績 🔥絶好調｜値頃 💎割安｜FAIL_UWAHIGE｜終値1455.0｜💰14.9万円｜⚠日程不明
- 5703 日本軽金属ホールディングス（日軽金ＨＤ）｜choruko_reversal｜業績 🔥絶好調｜値頃 💎割安｜FAIL_INSEN｜終値2478.0｜💰25.6万円｜⚠日程不明
- 6652 IDEC Corporation｜choruko_reversal｜業績 🔥絶好調｜値頃 💎割安｜FAIL_UWAHIGE｜終値3005.0｜💰30.9万円｜⚠日程不明
- 8084 ＲＹＯＤＥＮ｜choruko_reversal/granville_rebound｜業績 🔥絶好調｜値頃 💎割安｜FAIL_INSEN｜終値2167.0｜💰22.4万円｜⚠日程不明
- 167A リョーサン菱洋ホールディングス（リョー菱ＨＤ）｜choruko_reversal｜業績 🔥絶好調｜値頃 🟢値頃｜PASS｜終値3085.0｜💰30.9万円｜reversal 3085 SL3010・✅即時可｜⚠日程不明 📐進捗 上振れ 53.4%
  > 📌【業態】半導体商社大手。24年4月に菱洋エレクとリョーサンが経営統合。CPU、GPUに特色。
  > 📌【いま】終値3,085円・直近5日+0.65%・📌その他重要開示リョーサン菱洋、北九州市主催の「北九州フィジカルAIハッカソン2026」に協賛
  > 📌【調子】🔥絶好調（9/13）— 上方修正済み・🔼進捗先行
  > 📌【水準】🟢値頃（5.0/7）— PER13.03倍・PEG0.286・52週54.2% ／ 💰単元30.9万円
  > 📌【戦略】当日終値3085円の指値で反転を取りにいく。SL3010円（直近5日安値）
- 5301 Tokai Carbon Co., Ltd.｜choruko_reversal/granville_rebound｜業績 🔥絶好調｜値頃 🟢値頃｜FAIL_UWAHIGE｜終値1547.0｜💰16.3万円｜⚠日程不明
- 6588 東芝テック｜choruko_reversal｜業績 🔥絶好調｜値頃 🟢値頃｜PASS｜終値2468.0｜💰24.7万円｜reversal 2468 SL2400・✅即時可｜⚠日程不明
  > 📌【業態】POSシステム端末の最大手。国内シェア5割。複合機はリコーと開発・製造統合。
  > 📌【いま】終値2,468円・直近5日-8.96%（材料未確認）
  > 📌【調子】🔥絶好調（9/13）— 上方修正済み
  > 📌【水準】🟢値頃（5.0/7）— PER18.7倍・PEG0.31・52週6.5% ／ 💰単元24.7万円
  > 📌【戦略】当日終値2468円の指値で反転を取りにいく。SL2400円（直近5日安値）
- 6724 セイコーエプソン｜choruko_reversal｜業績 🔥絶好調｜値頃 🟢値頃｜FAIL_INSEN｜終値2729.5｜💰28.5万円｜⚠日程不明
- 6925 Ushio Inc.｜choruko_reversal｜業績 🔥絶好調｜値頃 🟢値頃｜PASS｜終値2995.5｜💰30.0万円｜⛔提案なし(指名鮮度切れ 17営業日)｜⚠日程不明
  > 📌【業態】産業用ランプで世界首位。光源や光学装置を展開。医療装置分野も強化。
  > 📌【いま】終値2,996円・直近5日-2.55%（材料未確認）
  > 📌【調子】🔥絶好調（9/13）— 上方修正済み・🔼進捗先行
  > 📌【水準】🟢値頃（5.0/7）— PER19.81倍・PEG0.568・52週24.5% ／ 💰単元30.0万円
  > 📌【戦略】発注対象外（⛔提案なし(指名鮮度切れ 17営業日)）
- 6952 カシオ｜choruko_reversal｜業績 🔥絶好調｜値頃 ⚪妥当｜PASS｜終値2028.5｜💰20.3万円｜reversal 2028.5 SL1940.5・✅即時可｜⚠日程不明 📐進捗 上振れ 18.1%
  > 📌【業態】腕時計、電子辞書でシェア高い。業務用PDA、電子レジなど法人向け事業を強化。
  > 📌【いま】終値2,028円・直近5日-4.68%（材料未確認）
  > 📌【調子】🔥絶好調（9/13）— 🔼進捗先行
  > 📌【水準】⚪妥当（4.0/7）— PER16.48倍・PEG0.306・52週61.9% ／ 💰単元20.3万円
  > 📌【戦略】当日終値2028.5円の指値で反転を取りにいく。SL1940.5円（直近5日安値）
- 6875 メガチップス｜choruko_reversal｜業績 🔥絶好調｜値頃 💎割安｜PASS｜終値8350.0｜💰83.5万円｜⛔提案なし(指名鮮度切れ 12営業日)｜⚠日程不明
  > 📌【業態】カスタムLSI、画像転送システムが主力。生産外部委託。任天堂向け中心。5G向けも。
  > 📌【いま】終値8,350円・直近5日-1.18%（材料未確認）
  > 📌【調子】🔥絶好調（8/13）— 突出ボーナス・⚠進捗遅れ・⚠下期依存
  > 📌【水準】💎割安（7.0/7）— PER3.36倍・PEG0・52週17.8% ／ 💰単元83.5万円
  > 📌【戦略】発注対象外（⛔提案なし(指名鮮度切れ 12営業日)）
- 6471 日本精工｜choruko_reversal｜業績 🔥絶好調｜値頃 💎割安｜FAIL_INSEN｜終値955.7000122070312｜💰10.0万円｜⚠日程不明
- 8386 百十四銀行｜choruko_reversal/granville_rebound｜業績 🔥絶好調｜値頃 💎割安｜FAIL_INSEN｜終値2651.0｜💰28.5万円｜⚠日程不明
- 6754 アンリツ｜choruko_reversal/ai_reversal｜業績 🔥絶好調｜値頃 🟢値頃｜PASS｜終値2245.0｜💰22.4万円｜reversal 2245 SL2153.5・✅即時可｜⚠日程不明
  > 📌【業態】携帯・基地局向けなど計測機器大手。海外も高シェア。食品・医薬品検査機も。
  > 📌【いま】終値2,245円・直近5日-2.67%（材料未確認）
  > 📌【調子】🔥絶好調（8/13）— 税引前代替・D軸判定不能(直近Qデータ取得不可)・上方修正済み
  > 📌【水準】🟢値頃（5.0/7）— PER17.96倍・PEG0.495・52週6.6% ／ 💰単元22.4万円
  > 📌【戦略】当日終値2245円の指値で反転を取りにいく。SL2153.5円（直近5日安値）
- 7731 ニコン｜choruko_reversal｜業績 🔥絶好調｜値頃 🟢値頃｜FAIL_UWAHIGE｜終値1547.0｜💰16.0万円｜⚠日程不明
- 9902 Nichiden Corporation｜choruko_reversal/granville_oshime｜業績 🔥絶好調｜値頃 🟢値頃｜FAIL_INSEN｜終値2891.0｜💰29.4万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 7733 Olympus Corp.｜choruko_reversal｜業績 🔥絶好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値1792.0｜💰17.8万円｜⚠日程不明
- 8524 North Pacific Bank, Ltd.｜choruko_reversal/granville_rebound｜業績 🔥絶好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値1162.0｜💰12.3万円｜⚠日程不明
- 4088 Air Water Inc.｜choruko_reversal｜業績 🔥絶好調｜値頃 ⚪妥当｜FAIL_UWAHIGE｜終値2950.0｜💰28.9万円｜📉決算反応日 11/17
- 8133 伊藤忠エネクス｜choruko_reversal｜業績 🔥絶好調｜値頃 🟡やや割高｜FAIL_INSEN｜終値2039.0｜💰20.7万円｜⚠日程不明
- 5333 ＮＧＫ｜choruko_reversal/ai_reversal｜業績 ⚡好調｜値頃 💎割安｜FAIL_INSEN｜終値4403.0｜💰48.0万円｜⚠日程不明
- 6036 ＫｅｅＰｅｒ技研｜choruko_reversal/granville_oshime｜業績 ⚡好調｜値頃 💎割安｜FAIL_INSEN｜終値1708.0｜💰17.7万円｜📉決算反応日 11/17 📑TOPIX低減対象（次 01/29 第2回/8）
- 5186 ニッタ｜choruko_reversal/granville_rebound｜業績 ⚡好調｜値頃 🟢値頃｜PASS｜終値6140.0｜💰61.4万円｜reversal 6140 SL6040・✅即時可｜⚠日程不明 📐進捗 上振れ 21.2%
  > 📌【業態】伝動用ベルト大手。産業機械向け主力。自動車ホース、半導体関連なども強み。
  > 📌【いま】終値6,140円・直近5日-3.46%（材料未確認）
  > 📌【調子】⚡好調（7/13）— 上方修正済み・🔼加速・🔼進捗先行
  > 📌【水準】🟢値頃（5.0/7）— PER11.25倍・PEG0.522・52週64.8% ／ 💰単元61.4万円
  > 📌【戦略】当日終値6140円の指値で反転を取りにいく。SL6040円（直近5日安値）
- 6268 ナブテスコ｜choruko_reversal｜業績 ⚡好調｜値頃 🟢値頃｜FAIL_INSEN｜終値3436.0｜💰41.5万円｜⚠日程不明
- 8154 加賀電子｜choruko_reversal/stf_kakuhen/granville_oshime/granville_rebound｜業績 ⚡好調｜値頃 🟢値頃｜FAIL_INSEN｜終値5150.0｜💰53.2万円｜⚠日程不明
- 8393 Miyazaki Bank Ltd.｜choruko_reversal｜業績 ⚡好調｜値頃 🟢値頃｜FAIL_INSEN｜終値2294.0｜💰25.4万円｜⚠日程不明
- 4634 ａｒｔｉｅｎｃｅ（ａｒｔｉｅｎ）｜choruko_reversal｜業績 ⚡好調｜値頃 ⚪妥当｜FAIL_UWAHIGE｜終値5080.0｜💰48.1万円｜⚠日程不明
- 6448 ブラザー工業（ブラザー）｜choruko_reversal｜業績 ⚡好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値4404.0｜💰45.6万円｜⚠日程不明
- 3116 Toyota Boshoku Corp.｜choruko_reversal｜業績 ⚡好調｜値頃 💎割安｜FAIL_INSEN｜終値2051.0｜💰20.9万円｜⚠日程不明
- 5331 ノリタケ｜choruko_reversal/ai_reversal｜業績 ⚡好調｜値頃 💎割安｜FAIL_INSEN｜終値2876.0｜💰30.1万円｜⚠日程不明
- 7004 Kanadevia Corporation｜choruko_reversal｜業績 ⚠減速｜値頃 💎割安｜FAIL_INSEN｜終値941.0｜💰9.7万円｜⚠日程不明
- 4205 Zeon Corporation｜choruko_reversal｜業績 ⚡好調｜値頃 💎割安｜PASS｜終値2018.5｜💰20.2万円｜reversal 2018.5 SL1982.5・✅即時可｜⚠日程不明 📐進捗 上振れ 39.7%
  > 📌【業態】古河系。合成ゴム大手。耐油性特殊ゴムで世界的。合成ラテックス、高機能材も。
  > 📌【いま】終値2,018円・直近5日-2.30%（材料未確認）
  > 📌【調子】⚡好調（6/13）— 上方修正済み・🔼加速・🔼進捗先行
  > 📌【水準】💎割安（6.0/7）— PER8.99倍・PEG0.557・52週37.6% ／ 💰単元20.2万円
  > 📌【戦略】当日終値2018.5円の指値で反転を取りにいく。SL1982.5円（直近5日安値）
- 6651 NITTO KOGYO Corporation｜choruko_reversal｜業績 ⚡好調｜値頃 💎割安｜FAIL_INSEN｜終値4035.0｜💰41.8万円｜⚠日程不明
- 4206 アイカ工業｜choruko_reversal/granville_oshime｜業績 ⚡好調｜値頃 🟢値頃｜FAIL_UWAHIGE｜終値4021.0｜💰40.9万円｜⚠日程不明
- 4966 上村工業｜choruko_reversal｜業績 ⚡好調｜値頃 🟢値頃｜FAIL_UWAHIGE｜終値15520.0｜💰166.3万円｜⚠日程不明 📑TOPIX新規採用（2026-10-30 組入）
- 5463 丸一鋼管（丸一管）｜choruko_reversal｜業績 ⚡好調｜値頃 🟢値頃｜FAIL_INSEN｜終値1615.5｜💰16.6万円｜⚠日程不明
- 6250 Yamabiko Corporation｜choruko_reversal/granville_oshime｜業績 ⚡好調｜値頃 🟢値頃｜FAIL_INSEN｜終値3795.0｜💰39.9万円｜⚠日程不明
- 6473 ジェイテクト｜choruko_reversal｜業績 ⚠減速｜値頃 ⚪妥当｜FAIL_INSEN｜終値1966.5｜💰20.9万円｜⚠日程不明
- 268A Rigaku Holdings Corporation｜choruko_reversal｜業績 ⚡好調｜値頃 ⚪妥当｜FAIL_UWAHIGE｜終値1267.0｜💰13.8万円｜⚠日程不明
- 3569 セーレン｜choruko_reversal/granville_tenkan｜業績 ⚡好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値3520.0｜💰36.2万円｜⚠日程不明
- 5444 大和工業｜choruko_reversal｜業績 ⚡好調｜値頃 💎割安｜PASS｜終値10865.0｜💰108.7万円｜reversal 10865 SL10655・✅即時可｜⚠日程不明
  > 📌【業態】独立系電炉大手。主力はH形鋼、溝形鋼。海外多、韓・タイ・米・中東で操業。
  > 📌【いま】終値10,865円・直近5日+0.46%（材料未確認）
  > 📌【調子】⚡好調（5/13）
  > 📌【水準】💎割安（6.0/7）— PER11.29倍・PEG0.338・52週27.4% ／ 💰単元108.7万円
  > 📌【戦略】当日終値10865円の指値で反転を取りにいく。SL10655円（直近5日安値）
- 9934 因幡電機産業｜choruko_reversal｜業績 ⚡好調｜値頃 🟢値頃｜FAIL_UWAHIGE｜終値2560.5｜💰26.2万円｜⚠日程不明
- 1721 コムシスホールディングス｜choruko_reversal｜業績 ⚡好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値5173.0｜💰52.6万円｜⚠日程不明
- 4403 日油｜choruko_reversal/granville_tenkan｜業績 ⚡好調｜値頃 ⚪妥当｜PASS｜終値2627.0｜💰26.3万円｜reversal 2627 SL2501・✅即時可｜⚠日程不明
  > 📌【業態】油脂化学系製品大手。機能化成品、化薬、ライフサイエンス、DDS事業など多角化。
  > 📌【いま】終値2,627円・直近5日+3.90%（材料未確認）
  > 📌【調子】⚡好調（5/13）— 上方修正済み・質注意
  > 📌【水準】⚪妥当（3.0/7）— PER14.28倍・PEG5.017・52週16.2% ／ 💰単元26.3万円
  > 📌【戦略】当日終値2627円の指値で反転を取りにいく。SL2501円（直近5日安値）
- 9037 Hamakyorex Co., Ltd.｜choruko_reversal｜業績 ⚡好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値1683.0｜💰18.4万円｜⚠日程不明
- 9072 NIKKON Holdings Co., Ltd.｜choruko_reversal｜業績 ⚡好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値4141.0｜💰42.1万円｜⚠日程不明
- 1926 ライト工業（ライト）｜choruko_reversal｜業績 ⚡好調｜値頃 🟡やや割高｜FAIL_INSEN｜終値996.0｜💰10.4万円｜⚠日程不明
- 6454 マックス｜choruko_reversal｜業績 ⚡好調｜値頃 🟡やや割高｜FAIL_UWAHIGE｜終値1805.0｜💰18.1万円｜⚠日程不明
- 9302 三井倉庫ホールディングス｜choruko_reversal｜業績 ⚡好調｜値頃 🟡やや割高｜FAIL_INSEN｜終値3214.0｜💰32.1万円｜⚠日程不明
- 9960 トーテック｜choruko_reversal/ai_momentum/ai_reversal｜業績 ⚡好調｜値頃 🟡やや割高｜FAIL_INSEN｜終値4195.0｜💰45.1万円｜📉決算反応日 11/17
- 6845 アズビル｜choruko_reversal｜業績 ⚡好調｜値頃 🔴過熱｜FAIL_INSEN｜終値1508.5｜💰15.6万円｜⚠日程不明
- 6135 牧野フライス製作所｜choruko_reversal｜業績 ✅順調｜値頃 💎割安｜FAIL_INSEN｜終値2685.0｜💰27.9万円｜⚠日程不明
- 6340 澁谷工業｜choruko_reversal/granville_oshime/granville_rebound｜業績 ✅順調｜値頃 🟢値頃｜FAIL_INSEN｜終値4665.0｜💰49.4万円｜⚠日程不明
- 6674 ジーエス・ユアサ　コーポレーション｜choruko_reversal｜業績 ✅順調｜値頃 🟢値頃｜FAIL_INSEN｜終値4264.0｜💰44.6万円｜⚠日程不明
- 4272 Nippon Kayaku Co., Ltd.｜choruko_reversal/granville_tenkan/granville_oshime｜業績 ✅順調｜値頃 ⚪妥当｜FAIL_UWAHIGE｜終値1862.5｜💰18.8万円｜⚠日程不明
- 6923 Stanley Electric Co., Ltd.｜choruko_reversal｜業績 ✅順調｜値頃 ⚪妥当｜FAIL_INSEN｜終値3182.0｜💰32.4万円｜⚠日程不明
- 3445 RS Technologies Co. Ltd.｜choruko_reversal｜業績 ✅順調｜値頃 ⚪妥当｜FAIL_INSEN｜終値4080.0｜💰45.5万円｜⚠日程不明
- 4021 Nissan Chemical Corporation｜choruko_reversal｜業績 ✅順調｜値頃 ⚪妥当｜PASS｜終値6669.0｜💰66.7万円｜reversal 6669 SL6525・✅即時可｜📉決算反応日 11/17
  > 📌【業態】化学品事業・開発に強み。電子・無機・有機の材料、医薬等。農薬は首位。
  > 📌【いま】終値6,669円・直近5日-3.12%（材料未確認）
  > 📌【調子】✅順調（4/13）— 上方修正済み
  > 📌【水準】⚪妥当（3.0/7）— PER16.69倍・PEG1.773・52週39.3% ／ 💰単元66.7万円
  > 📌【戦略】当日終値6669円の指値で反転を取りにいく。SL6525円（直近5日安値）
- 4042 東ソー｜choruko_reversal｜業績 ✅順調｜値頃 ⚪妥当｜FAIL_INSEN｜終値2456.0｜💰25.3万円｜⚠日程不明
- 5021 コスモＨＤ｜choruko_reversal｜業績 🔻悪化｜値頃 ⚪妥当｜FAIL_INSEN｜終値3373.0｜💰35.0万円｜⚠日程不明
- 7276 Koito Manufacturing Co., Ltd.｜choruko_reversal｜業績 ⚠減速｜値頃 ⚪妥当｜FAIL_INSEN｜終値2507.0｜💰25.4万円｜⚠日程不明
- 6055 Japan Material Co., Ltd.｜choruko_reversal/ai_reversal｜業績 ✅順調｜値頃 🟡やや割高｜FAIL_INSEN｜終値1540.0｜💰16.7万円｜⚠日程不明
- 6750 エレコム｜choruko_reversal｜業績 ✅順調｜値頃 🟡やや割高｜PASS｜終値1917.0｜💰19.2万円｜reversal 1917 SL1799・✅即時可｜⚠日程不明 📐進捗 上振れ 25.2%
  > 📌【業態】PC周辺機器メーカー大手。マウス、キーボード、スマホ・タブレット周辺機器でトップ。ファブレス。
  > 📌【いま】終値1,917円・直近5日+2.51%（材料未確認）
  > 📌【調子】✅順調（4/13）— 質注意・🔼進捗先行
  > 📌【水準】🟡やや割高（2.0/7）— PER13.49倍・PEG—・52週69.1% ／ 💰単元19.2万円
  > 📌【戦略】当日終値1917円の指値で反転を取りにいく。SL1799円（直近5日安値）
- 4768 OTSUKA CORPORATION｜choruko_reversal/granville_rebound｜業績 ✅順調｜値頃 🔴過熱｜FAIL_INSEN｜終値3803.0｜💰38.1万円｜⚠日程不明
- 6332 月島ホールディングス｜choruko_reversal｜業績 ✅順調｜値頃 ⚪妥当｜FAIL_INSEN｜終値2273.0｜💰23.9万円｜⚠日程不明
- 6368 Organo Corp.｜choruko_reversal｜業績 ✅順調｜値頃 ⚪妥当｜FAIL_INSEN｜終値1656.0｜💰18.3万円｜⚠日程不明
- 1951 エクシオグループ（エクシオＧ）｜choruko_reversal｜業績 ⚠減速｜値頃 ⚪妥当｜FAIL_INSEN｜終値2397.5｜💰24.3万円｜⚠日程不明
- 1963 日揮ホールディングス｜choruko_reversal｜業績 ⚠減速｜値頃 ⚪妥当｜FAIL_INSEN｜終値2063.0｜💰21.1万円｜⚠日程不明
- 4028 石原産業｜choruko_reversal｜業績 🔻悪化｜値頃 ⚪妥当｜PASS｜終値2604.0｜💰26.0万円｜reversal 2604 SL2550・✅即時可｜⚠日程不明 ⚠業績基調が下向き（🔻悪化） 📐進捗 遅れ -11.2%
  > 📌【業態】未取得（次回以降に取得）
  > 📌【いま】終値2,604円・直近5日+1.64%・📌その他重要開示Integrated Report 2026
  > 📌【調子】🔻悪化（3/13）— A成長率0以下のためレバレッジ計算不可(C=0)・上方修正済み・質注意・経常減益-28.7%・⚠減速・⚠進捗遅れ
  > 📌【水準】⚪妥当（3.0/7）— PER14.07倍・PEG—・52週22.2% ／ 💰単元26.0万円
  > 📌【戦略】当日終値2604円の指値で反転を取りにいく。SL2550円（直近5日安値）
- 5602 栗本鐵工所（栗本鉄）｜choruko_reversal｜業績 ✅順調｜値頃 ⚪妥当｜FAIL_INSEN｜終値1425.0｜💰14.6万円｜⚠日程不明
- 6804 ホシデン｜choruko_reversal｜業績 🔻悪化｜値頃 ⚪妥当｜PASS｜終値2145.0｜💰21.4万円｜reversal 2145 SL2074・✅即時可｜⚠日程不明 ⚠業績基調が下向き（🔻悪化） 📐進捗 上振れ 31.8%
  > 📌【業態】電気機器（電子部品・コネクター・自動車部材・部品関連）
  > 📌【いま】終値2,145円・直近5日-2.59%（材料未確認）
  > 📌【調子】🔻悪化（3/13）— A成長率0以下のためレバレッジ計算不可(C=0)・質注意・経常減益-27.0%・⚠減速・🔼進捗先行
  > 📌【水準】⚪妥当（3.0/7）— PER8.45倍・PEG—・52週6.6% ／ 💰単元21.4万円
  > 📌【戦略】当日終値2145円の指値で反転を取りにいく。SL2074円（直近5日安値）
- 3105 日清紡ホールディングス｜choruko_reversal｜業績 ✅順調｜値頃 🟡やや割高｜FAIL_UWAHIGE｜終値1843.0｜💰19.4万円｜⚠日程不明
- 5310 Toyo Tanso Co., Ltd.｜choruko_reversal/ai_reversal｜業績 🔻悪化｜値頃 🟡やや割高｜FAIL_UWAHIGE｜終値5930.0｜💰62.2万円｜⚠日程不明
- 6741 日本信号｜choruko_reversal｜業績 ✅順調｜値頃 🟡やや割高｜FAIL_INSEN｜終値1630.0｜💰16.5万円｜📉決算反応日 11/17
- 6807 Japan Aviation Electronics Industry, Limited｜choruko_reversal｜業績 ✅順調｜値頃 🟡やや割高｜PASS｜終値2263.0｜💰22.6万円｜reversal 2263 SL2221・✅即時可｜⚠日程不明
  > 📌【業態】NEC系コネクター大手。小型、高速伝送で競争力。車、航空・宇宙向け電子機器も。
  > 📌【いま】終値2,263円・直近5日-0.48%（材料未確認）
  > 📌【調子】✅順調（3/13）— 質注意
  > 📌【水準】🟡やや割高（2.0/7）— PER25.43倍・PEG8.322・52週19.8% ／ 💰単元22.6万円
  > 📌【戦略】当日終値2263円の指値で反転を取りにいく。SL2221円（直近5日安値）
- 7220 Musashi Seimitsu Industry Co., Ltd.｜choruko_reversal｜業績 🔻悪化｜値頃 🟡やや割高｜FAIL_INSEN｜終値1988.0｜💰24.0万円｜⚠日程不明
- 6479 ミネベア｜choruko_reversal｜業績 ➖横ばい｜値頃 💎割安｜FAIL_INSEN｜終値2863.0｜💰30.5万円｜⚠日程不明
- 4902 Konica Minolta, Inc.｜choruko_reversal/granville_tenkan｜業績 ➖横ばい｜値頃 🟢値頃｜FAIL_UWAHIGE｜終値570.0｜💰5.7万円｜⚠日程不明
- 1979 大気社｜choruko_reversal｜業績 ➖横ばい｜値頃 ⚪妥当｜FAIL_INSEN｜終値3350.0｜💰35.3万円｜⚠日程不明
- 4008 住友精化｜choruko_reversal｜業績 🔻悪化｜値頃 ⚪妥当｜FAIL_INSEN｜終値1311.0｜💰13.6万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 9468 カドカワ｜choruko_reversal｜業績 ➖横ばい｜値頃 🔴過熱｜FAIL_INSEN｜終値3435.0｜💰34.3万円｜⚠日程不明
- 6632 JVCKENWOOD Corporation｜choruko_reversal｜業績 ⚠減速｜値頃 ⚪妥当｜PASS｜終値796.0｜💰8.0万円｜reversal 796 SL781・✅即時可｜⚠日程不明 ⚠業績基調が下向き（⚠減速）
  > 📌【業態】ビクターとケンウッドが統合。AV機器、車載、業務用に注力。ドラレコ関連事業を強化。
  > 📌【いま】終値796円・直近5日+0.89%（材料未確認）
  > 📌【調子】⚠減速（1/13）— 税引前代替・D軸判定不能(直近Qデータ取得不可)・E軸判定不能(期首・進捗なし)・質注意
  > 📌【水準】⚪妥当（4.0/7）— PER7.49倍・PEG—・52週3.2% ／ 💰単元8.0万円
  > 📌【戦略】当日終値796円の指値で反転を取りにいく。SL781円（直近5日安値）
- 4746 東計電算｜choruko_reversal｜業績 ⚠減速｜値頃 ⚪妥当｜FAIL_INSEN｜終値1713.0｜💰18.0万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 4980 Dexerials Corp.｜choruko_reversal/ai_reversal｜業績 ⚠減速｜値頃 ⚪妥当｜FAIL_INSEN｜終値1894.5｜💰20.7万円｜⚠日程不明
- 9722 藤田観光｜choruko_reversal｜業績 ⚠減速｜値頃 ⚪妥当｜FAIL_INSEN｜終値2775.0｜💰28.4万円｜⚠日程不明
- 6370 栗田工業｜choruko_reversal｜業績 🔻悪化｜値頃 🟡やや割高｜FAIL_UWAHIGE｜終値5545.0｜💰57.2万円｜⚠日程不明
- 6436 アマノ｜choruko_reversal｜業績 ⚠減速｜値頃 🟡やや割高｜FAIL_UWAHIGE｜終値3600.0｜💰35.6万円｜⚠日程不明
- 9301 三菱倉｜choruko_reversal｜業績 ⚠減速｜値頃 🟡やや割高｜FAIL_UWAHIGE｜終値1241.0｜💰12.6万円｜⚠日程不明
- 7148 Financial Products Group Co., Ltd.｜choruko_reversal｜業績 ⚠減速｜値頃 ⚪妥当｜FAIL_INSEN｜終値1408.0｜💰14.2万円｜⚠日程不明 ⚡材料後出し
- 6379 レイズネク｜choruko_reversal｜業績 ⚠減速｜値頃 ⚪妥当｜FAIL_INSEN｜終値959.0｜💰9.4万円｜⚠日程不明
- 7278 Exedy Corporation｜choruko_reversal｜業績 ⚠減速｜値頃 ⚪妥当｜FAIL_INSEN｜終値5190.0｜💰53.2万円｜⚠日程不明
- 2109 ＤＭ三井製糖｜choruko_reversal｜業績 ⚠減速｜値頃 🟡やや割高｜FAIL_UWAHIGE｜終値3630.0｜💰36.2万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 6349 Komori Corporation｜choruko_reversal｜業績 ⚠減速｜値頃 🟡やや割高｜FAIL_INSEN｜終値1693.0｜💰17.4万円｜⚠日程不明
- 6810 Maxell, Ltd.｜choruko_reversal/granville_oshime/granville_rebound｜業績 業績データ取得不可(経常益予想非開示)｜値頃 💎割安｜FAIL_UWAHIGE｜終値2128.0｜💰21.9万円｜⚠日程不明
- 7322 三十三フィナンシャルグループ｜choruko_reversal/granville_rebound｜業績 取得不可｜値頃 💎割安｜FAIL_INSEN｜終値1711.0｜💰18.1万円｜⚠日程不明
- 8253 Credit Saison Co., Ltd.｜choruko_reversal｜業績 取得不可｜値頃 💎割安｜FAIL_UWAHIGE｜終値4971.0｜💰41.6万円｜⚠日程不明
- 8366 滋賀銀行｜choruko_reversal/granville_rebound｜業績 取得不可｜値頃 💎割安｜FAIL_INSEN｜終値2099.0｜💰23.1万円｜⚠日程不明
- 7381 ＣＣＩグループ｜choruko_reversal/granville_rebound｜業績 業績データ取得不可(売上/経常欠損)｜値頃 🟢値頃｜FAIL_INSEN｜終値1050.0｜💰11.2万円｜⚠日程不明
- 8975 Ichigo Office REIT Investment Corporation｜choruko_reversal｜業績 判定保留(変則決算)｜値頃 🟢値頃｜PASS｜終値89200.0｜💰8.9万円｜⛔提案なし(指名鮮度切れ 11営業日)｜📋カルテ窓 12/16(残20営業日)
  > 📌【業態】投資は中規模オフィスビル特化型。価値向上修繕も。運用:いちごグループHD系。
  > 📌【いま】終値89,200円・直近5日+3.00%（材料未確認）
  > 📌【調子】判定保留(変則決算)（—/13）— 変則決算・四半期不足
  > 📌【水準】🟢値頃（5.6/7）— PER12.24倍・PEG0.06・52週44.6% ／ 💰単元8.9万円
  > 📌【戦略】発注対象外（⛔提案なし(指名鮮度切れ 11営業日)）
- 3612 WORLD CO.,LTD.｜choruko_reversal｜業績 業績データ取得不可(経常益予想非開示)｜値頃 🟢値頃｜FAIL_INSEN｜終値1508.0｜💰15.2万円｜⚠日程不明
- 5101 Yokohama Rubber Co., Ltd.｜choruko_reversal｜業績 取得不可｜値頃 🟢値頃｜PASS｜終値7482.0｜💰74.8万円｜reversal 7482 SL6889・✅即時可｜⚠日程不明 ⚠1単元でリスク枠超過（59,300円） ℹ相対強い RS20 11.6pt
  > 📌【業態】タイヤ大手。工業資材や航空部品、ゴルフ用品も展開。北米や農機用タイヤが拡大。
  > 📌【いま】終値7,482円・直近5日+4.41%（材料未確認）
  > 📌【調子】取得不可（—/13）— 業績データ取得不可(経常益予想非開示)
  > 📌【水準】🟢値頃（5.0/7）— PER10.09倍・PEG—・52週69.8% ／ 💰単元74.8万円
  > 📌【戦略】当日終値7482円の指値で反転を取りにいく。SL6889円（直近5日安値）／⚠1単元リスク59,300円（枠超過）
- 5831 Shizuoka Financial Group, Inc.｜choruko_reversal/granville_rebound｜業績 業績データ取得不可(売上/経常欠損)｜値頃 🟢値頃｜FAIL_INSEN｜終値3111.0｜💰31.8万円｜⚠日程不明
- 7167 めぶきフィナンシャルグループ｜choruko_reversal/granville_rebound｜業績 取得不可｜値頃 🟢値頃｜FAIL_INSEN｜終値1459.0｜💰15.1万円｜⚠日程不明
- 7186 横浜フィナンシャルグループ｜choruko_reversal｜業績 取得不可｜値頃 🟢値頃｜FAIL_INSEN｜終値1683.5｜💰17.5万円｜⚠日程不明
- 8359 Hachijuni Nagano Bank, Ltd.｜choruko_reversal/granville_rebound｜業績 業績データ取得不可(売上/経常欠損)｜値頃 🟢値頃｜PASS｜終値2396.0｜💰24.0万円｜⛔提案なし(指名鮮度切れ 13営業日)｜⚠日程不明
  > 📌【業態】長野地盤の地銀上位。県全域にシェア圧倒的。堅実経営。長野銀と合併。
  > 📌【いま】終値2,396円・直近5日-2.66%（材料未確認）
  > 📌【調子】業績データ取得不可(売上/経常欠損)（—/13）— 業績データ取得不可(売上/経常欠損)・🔼進捗先行
  > 📌【水準】🟢値頃（5.0/7）— PER13.58倍・PEG0.296・52週64.1% ／ 💰単元24.0万円
  > 📌【戦略】発注対象外（⛔提案なし(指名鮮度切れ 13営業日)）
- 8370 紀陽銀行｜choruko_reversal｜業績 業績データ取得不可(売上/経常欠損)｜値頃 🟢値頃｜FAIL_INSEN｜終値1449.0｜💰15.3万円｜⚠日程不明
- 4293 セプテーニ・ホールディングス（セプテニＨＤ）｜choruko_reversal｜業績 取得不可｜値頃 ⚪妥当｜FAIL_INSEN｜終値450.0｜💰4.7万円｜⚠日程不明
- 8304 あおぞら銀行｜choruko_reversal｜業績 取得不可｜値頃 ⚪妥当｜FAIL_INSEN｜終値3177.0｜💰32.0万円｜⚠日程不明
- 8334 Gunma Bank, Ltd.｜choruko_reversal/granville_rebound｜業績 業績データ取得不可(売上/経常欠損)｜値頃 ⚪妥当｜FAIL_INSEN｜終値2428.5｜💰26.3万円｜⚠日程不明
- 8354 ふくおかフィナンシャルグループ｜choruko_reversal｜業績 業績データ取得不可(売上/経常欠損)｜値頃 ⚪妥当｜FAIL_INSEN｜終値6882.0｜💰71.9万円｜⚠日程不明
- 8600 トモニホールディングス｜choruko_reversal｜業績 取得不可｜値頃 ⚪妥当｜FAIL_INSEN｜終値960.0｜💰10.2万円｜⚠日程不明
- 8032 紙パル商｜choruko_reversal｜業績 取得不可｜値頃 🟡やや割高｜FAIL_INSEN｜終値1124.0｜💰11.3万円｜⚠日程不明
- 1663 K&O Energy Group, Inc.｜choruko_reversal｜業績 —｜値頃 —｜FAIL_INSEN｜終値1734.0｜💰—｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 5019 出光興産｜choruko_reversal｜業績 取得不可｜値頃 ⏸判定不能｜FAIL_INSEN｜終値1230.5｜💰12.9万円｜⚠日程不明
- 5201 AGC Inc.｜choruko_reversal｜業績 —｜値頃 —｜FAIL_INSEN｜終値4775.0｜💰—｜⚠日程不明
- 6277 Hosokawa Micron Corporation｜choruko_reversal｜業績 —｜値頃 —｜FAIL_INSEN｜終値5960.0｜💰—｜⚠日程不明
- 7177 ＧＭＯフィナンシャルホールディングス｜choruko_reversal｜業績 取得不可｜値頃 取得不可｜FAIL_INSEN｜終値1053.0｜💰10.6万円｜⚠日程不明
- 8508 J Trust Co., Ltd.｜choruko_reversal｜業績 —｜値頃 —｜FAIL_INSEN｜終値683.0｜💰—｜⚠日程不明 📑TOPIX新規採用（2026-10-30 組入）
- 8616 Tokai Tokyo Financial Holdings, Inc.｜choruko_reversal｜業績 業績データ取得不可｜値頃 取得不可｜FAIL_INSEN｜終値758.0｜💰7.8万円｜⚠日程不明
- 8698 Monex Group, Inc.｜choruko_reversal｜業績 業績データ取得不可(経常益予想非開示)｜値頃 ⏸判定不能｜PASS｜終値591.0｜💰5.9万円｜reversal 591 SL577・✅即時可｜⚠日程不明
  > 📌【業態】ネット証券。米など海外でも。国内証券はNTTドコモ傘下に。子会社にコインチェック。
  > 📌【いま】終値591円・直近5日+1.03%（材料未確認）
  > 📌【調子】業績データ取得不可(経常益予想非開示)（—/13）— 業績データ取得不可(経常益予想非開示)
  > 📌【水準】⏸判定不能（—/7）— PER—倍・PEG—・52週7.3% ／ 💰単元5.9万円
  > 📌【戦略】当日終値591円の指値で反転を取りにいく。SL577円（直近5日安値）
- 9107 Kawasaki Kisen Kaisha, Ltd.｜choruko_reversal｜業績 —｜値頃 —｜FAIL_UWAHIGE｜終値3050.0｜💰—｜⚠日程不明
- 3131 Shinden Hightex Corp.｜stf_kakuhen/ai_reversal/granville_oshime/granville_rebound｜業績 🚀確変｜値頃 💎割安｜FAIL_INSEN｜終値6350.0｜💰71.0万円｜⚠日程不明
- 9308 乾汽船｜stf_kakuhen/granville_oshime/changepoint/changepoint🔔🔔｜業績 🚀確変｜値頃 ⚪妥当｜FAIL_INSEN｜終値2163.0｜💰22.6万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 6969 松尾電機｜stf_kakuhen｜業績 🔥絶好調｜値頃 💎割安｜PASS｜終値1094.0｜💰10.9万円｜⛔提案なし(手法ブランチ不明)｜⚠日程不明
  > 📌【業態】コンデンサ大手。自動車用、産業用、タンタルに強み。電流ヒューズも。デンソー向け大。
  > 📌【いま】終値1,094円・直近5日-4.70%（材料未確認）
  > 📌【調子】🔥絶好調（10/13）— 🔼進捗先行・⚠下期依存
  > 📌【水準】💎割安（7.0/7）— PER7.23倍・PEG0.141・52週22.9% ／ 💰単元10.9万円
  > 📌【戦略】発注対象外（⛔提案なし(手法ブランチ不明)）
- 3205 ダイドー｜stf_kakuhen｜業績 🔥絶好調｜値頃 🟢値頃｜FAIL_INSEN｜終値760.0｜💰7.7万円｜⚠日程不明
- 4410 ハリマ化成グループ（ハリマ化成Ｇ）｜stf_kakuhen｜業績 🔥絶好調｜値頃 🟢値頃｜FAIL_INSEN｜終値1301.0｜💰13.8万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 6668 ＡＤプラズマ｜stf_kakuhen/granville_oshime｜業績 🔥絶好調｜値頃 🟢値頃｜FAIL_UWAHIGE｜終値3440.0｜💰39.5万円｜⚠日程不明
- 5832 ちゅうぎんフィナンシャルグループ（ちゅうぎんＦ）｜stf_kakuhen｜業績 🔥絶好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値3413.0｜💰35.7万円｜⚠日程不明
- 5018 ＭＯＲＥＳＣＯ｜stf_kakuhen｜業績 🔥絶好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値2759.0｜💰28.0万円｜⚠日程不明
- 5246 ＥＬＥＭＥＮＴＳ｜stf_kakuhen/granville_oshime/granville_rebound｜業績 🔥絶好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値840.0｜💰9.3万円｜⚠日程不明
- 7942 ＪＳＰ｜stf_kakuhen｜業績 🔥絶好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値3075.0｜💰31.8万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 4180 Appier Group, Inc.｜stf_kakuhen/granville_oshime｜業績 🔥絶好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値1496.0｜💰14.5万円｜⚠日程不明
- 9962 ミスミグループ本社（ミスミＧ）｜stf_kakuhen｜業績 🔥絶好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値3613.0｜💰39.7万円｜⚠日程不明
- 3498 霞ヶ関Ｃ｜stf_kakuhen/granville_tenkan｜業績 🔥絶好調｜値頃 💎割安｜FAIL_INSEN｜終値6830.0｜💰71.5万円｜⚠日程不明
- 9110 ＮＳユナイテッド海運（ユナイテド海）｜stf_kakuhen｜業績 🔥絶好調｜値頃 ⚪妥当｜FAIL_UWAHIGE｜終値10540.0｜💰105.4万円｜⚠日程不明
- 3994 マネーフォワード｜stf_kakuhen/changepoint🔔🔔/changepoint🔔/changepoint｜業績 🔥絶好調｜値頃 🔴過熱｜FAIL_INSEN｜終値7260.0｜💰74.6万円｜⚠日程不明
- 9766 コナミグループ（コナミＧ）｜stf_kakuhen｜業績 🔥絶好調｜値頃 🟡やや割高｜FAIL_INSEN｜終値29530.0｜💰291.8万円｜⚠日程不明
- 2331 ＡＬＳＯＫ｜stf_kakuhen｜業績 ⚡好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値1360.0｜💰13.5万円｜⚠日程不明
- 4503 アステラス製薬（アステラス）｜stf_kakuhen｜業績 ⚡好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値2730.0｜💰27.0万円｜⚠日程不明
- 6850 チノー｜stf_kakuhen｜業績 ⚡好調｜値頃 ⚪妥当｜FAIL_UWAHIGE｜終値1756.0｜💰17.9万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 6758 ソニーグループ｜stf_kakuhen/ai_momentum｜業績 ⚡好調｜値頃 ⚪妥当｜FAIL_UWAHIGE｜終値4271.0｜💰43.5万円｜⚠日程不明
- 3091 ブロンコビリー｜stf_kakuhen｜業績 ⚡好調｜値頃 🟡やや割高｜FAIL_INSEN｜終値3125.0｜💰31.1万円｜⚠日程不明
- 3479 ＴＫＰ｜stf_kakuhen/granville_tenkan｜業績 ⚡好調｜値頃 🔴過熱｜FAIL_INSEN｜終値2121.0｜💰21.2万円｜⚠日程不明
- 4417 グローバルセキュリティエキスパート（Ｇセキュリ）｜stf_kakuhen｜業績 ⚡好調｜値頃 🔴過熱｜FAIL_INSEN｜終値8480.0｜💰84.7万円｜⚠日程不明
- 6016 ジャパンエンジン｜stf_kakuhen｜業績 ⚡好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値9780.0｜💰113.5万円｜⚠日程不明
- 6532 ベイカレント｜stf_kakuhen｜業績 ⚡好調｜値頃 🟡やや割高｜PASS｜終値12780.0｜💰127.8万円｜⛔提案なし(手法ブランチ不明)｜⚠日程不明
  > 📌【業態】ITコンサルで創業。企業戦略立案・課題解決・実行まで専門提供の総合コンサル。
  > 📌【いま】終値12,780円・直近5日+2.94%（材料未確認）
  > 📌【調子】⚡好調（5/13）— E軸判定不能(進捗データ不足)・D軸判定不能(四半期データ不足・中立1点)
  > 📌【水準】🟡やや割高（2.0/7）— PER39.05倍・PEG1.431・52週99.7% ／ 💰単元127.8万円
  > 📌【戦略】発注対象外（⛔提案なし(手法ブランチ不明)）
- 7747 朝日インテック｜stf_kakuhen/granville_tenkan｜業績 ⚡好調｜値頃 🔴過熱｜FAIL_UWAHIGE｜終値4259.0｜💰38.1万円｜⚠日程不明
- 4176 ココナラ｜stf_kakuhen｜業績 ✅順調｜値頃 💎割安｜FAIL_INSEN｜終値263.0｜💰2.7万円｜⚠日程不明
- 1980 ダイダン｜stf_kakuhen｜業績 ⚠減速｜値頃 🟡やや割高｜FAIL_INSEN｜終値2976.0｜💰32.0万円｜📉決算反応日 11/17
- 9434 ソフトバンク｜stf_kakuhen/ai_reversal｜業績 取得不可｜値頃 ⚪妥当｜FAIL_INSEN｜終値244.8000030517578｜💰2.4万円｜⚠日程不明
- 7366 ＬＩＴＡＬＩＣＯ（りたりこ）｜stf_kakuhen｜業績 業績データ取得不可(経常益予想非開示)｜値頃 ⚪妥当｜PASS｜終値2092.0｜💰20.9万円｜⛔提案なし(手法ブランチ不明)｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
  > 📌【業態】障害者向けの支援事業を展開。就労支援、発達障害児支援、家族向けなど。
  > 📌【いま】終値2,092円・直近5日-0.62%（材料未確認）
  > 📌【調子】業績データ取得不可(経常益予想非開示)（—/13）— 業績データ取得不可(経常益予想非開示)
  > 📌【水準】⚪妥当（3.0/7）— PER19.3倍・PEG—・52週92.9% ／ 💰単元20.9万円
  > 📌【戦略】発注対象外（⛔提案なし(手法ブランチ不明)）
- 3932 アカツキ｜stf_kakuhen｜業績 —｜値頃 ⏸判定不能｜FAIL_UWAHIGE｜終値1459.0｜💰14.6万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 9048 名古屋鉄道｜value_gap｜業績 ⚡好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値2024.0｜💰20.3万円｜⚠日程不明

## グランビル銘柄
- 6768 Tamura Corporation｜granville_tenkan/granville_oshime｜業績 🔥絶好調｜値頃 💎割安｜PASS_DOJI｜終値656.0｜💰6.6万円｜⛔提案なし(指名鮮度切れ 13営業日)｜⚠日程不明
  > 📌【業態】弱電用トランス、リアクター大手。ハンダ、絶縁膜や音声・ワイヤレス機器も。海外生産メイン。
  > 📌【いま】終値656円・直近5日-7.99%（材料未確認）
  > 📌【調子】🔥絶好調（10/13）— 上方修正済み・🔼加速・🔼進捗先行
  > 📌【水準】💎割安（7.0/7）— PER8.03倍・PEG0.215・52週17.4% ／ 💰単元6.6万円
  > 📌【戦略】発注対象外（⛔提案なし(指名鮮度切れ 13営業日)）
- 3927 アークン｜granville_tenkan｜業績 🔥絶好調｜値頃 💎割安｜FAIL_INSEN｜終値789.0｜💰8.4万円｜⚠日程不明
- 3491 ＧＡ　ｔｅｃｈｎｏｌｏｇｉｅｓ（ＧＡテクノ）｜granville_tenkan｜業績 🔥絶好調｜値頃 💎割安｜FAIL_INSEN｜終値1420.0｜💰14.7万円｜📋カルテ窓 12/10(残16営業日)
- 6744 能美防災｜granville_tenkan｜業績 🔥絶好調｜値頃 🟢値頃｜FAIL_UWAHIGE｜終値4530.0｜💰45.2万円｜⚠日程不明
- 8012 Nagase & Co., Ltd.｜granville_tenkan｜業績 🔥絶好調｜値頃 🟢値頃｜FAIL_INSEN｜終値1163.5｜💰12.1万円｜⚠日程不明
- 3002 グンゼ｜granville_tenkan｜業績 🔥絶好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値4380.0｜💰43.9万円｜⚠日程不明
- 4523 エーザイ｜granville_tenkan｜業績 🔥絶好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値5296.0｜💰51.9万円｜⚠日程不明
- 9742 アイネス｜granville_tenkan｜業績 🔥絶好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値2348.0｜💰24.0万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 3964 オークネット｜granville_tenkan｜業績 ⚡好調｜値頃 💎割安｜PASS_DOJI｜終値1262.0｜💰12.6万円｜momentum 1274 SL1241 上限1286.7・⏳確認足待ち・乖離1.0%｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
  > 📌【業態】業者間のネット・オークションを運営。中古車、スマホなどデジタル機器、ブランド品を展開。
  > 📌【いま】終値1,262円・直近5日-10.62%（材料未確認）
  > 📌【調子】⚡好調（7/13）— 上方修正済み
  > 📌【水準】💎割安（6.0/7）— PER14.69倍・PEG0.564・52週49.6% ／ 💰単元12.6万円
  > 📌【戦略】当日高値超えの逆指値1274円で順張り参戦を検討。上限1286.7円・SL1241円目安
- 4005 住友化学｜granville_tenkan｜業績 ⚡好調｜値頃 💎割安｜FAIL_INSEN｜終値500.5｜💰5.1万円｜⚠日程不明
- 3405 クラレ｜granville_tenkan｜業績 ⚡好調｜値頃 🟢値頃｜FAIL_INSEN｜終値1872.5｜💰19.2万円｜⚠日程不明
- 4401 ＡＤＥＫＡ｜granville_tenkan｜業績 ⚡好調｜値頃 🟢値頃｜FAIL_INSEN｜終値4208.0｜💰44.1万円｜⚠日程不明
- 4534 Mochida Pharmaceutical Co., Ltd.｜granville_tenkan｜業績 ⚡好調｜値頃 🟢値頃｜FAIL_INSEN｜終値3370.0｜💰32.6万円｜⚠日程不明 ⚡材料後出し
- 9006 Keikyu Corporation｜granville_tenkan｜業績 ⚡好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値1623.5｜💰16.3万円｜⚠日程不明
- 9075 福山通運｜granville_tenkan/granville_oshime｜業績 ⚡好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値6380.0｜💰63.8万円｜⚠日程不明
- 5532 リアルゲイト｜granville_tenkan｜業績 ⚡好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値3085.0｜💰34.0万円｜⚠日程不明 ⚡材料後出し
- 4507 塩野義製薬｜granville_tenkan｜業績 ⚡好調｜値頃 🟡やや割高｜FAIL_INSEN｜終値3188.0｜💰31.7万円｜⚠日程不明
- 1941 中電工｜granville_tenkan｜業績 ⚡好調｜値頃 🟢値頃｜FAIL_INSEN｜終値5080.0｜💰52.2万円｜⚠日程不明
- 3496 アズーム｜granville_tenkan｜業績 ⚡好調｜値頃 🟢値頃｜FAIL_INSEN｜終値3710.0｜💰40.7万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 2502 Asahi Group Holdings, Ltd.｜granville_tenkan｜業績 ⚡好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値1838.0｜💰18.1万円｜⚠日程不明
- 4848 Fullcast Holdings Co., Ltd.｜granville_tenkan/granville_oshime｜業績 ⚡好調｜値頃 ⚪妥当｜FAIL_UWAHIGE｜終値1845.0｜💰18.5万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 4045 Toagosei Co., Ltd.｜granville_tenkan｜業績 ⚡好調｜値頃 🟡やや割高｜FAIL_INSEN｜終値1773.0｜💰18.0万円｜⚠日程不明
- 6099 エラン｜granville_tenkan｜業績 ⚡好調｜値頃 🟡やや割高｜FAIL_INSEN｜終値771.0｜💰7.8万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 4554 Fuji Pharma Co., Ltd.｜granville_tenkan｜業績 ⚡好調｜値頃 🟢値頃｜FAIL_INSEN｜終値1826.0｜💰18.6万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 9842 アークランズ｜granville_tenkan｜業績 ⚡好調｜値頃 🟢値頃｜FAIL_INSEN｜終値1966.0｜💰19.7万円｜⚠日程不明
- 8804 東京建物｜granville_tenkan｜業績 ⚡好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値3395.0｜💰34.6万円｜⚠日程不明
- 2206 江崎グリコ｜granville_tenkan｜業績 ⚡好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値5142.0｜💰51.6万円｜⚠日程不明
- 7606 ＴＡＢＡＹＡホールディングス｜granville_tenkan｜業績 ⚡好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値2709.0｜💰26.7万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 8016 オンワード HD｜granville_tenkan｜業績 ⚡好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値802.0｜💰8.1万円｜⚠日程不明 ⚡材料後出し
- 4169 Enechange Ltd.｜granville_tenkan｜業績 ⚠減速｜値頃 ⚪妥当｜FAIL_INSEN｜終値276.0｜💰2.8万円｜⚠日程不明 ⚡材料後出し
- 4568 第一三共｜granville_tenkan｜業績 ✅順調｜値頃 ⚪妥当｜FAIL_INSEN｜終値2780.0｜💰28.5万円｜⚠日程不明
- 1911 Sumitomo Forestry Co., Ltd.｜granville_tenkan｜業績 🔻悪化｜値頃 ⚪妥当｜FAIL_INSEN｜終値1222.0｜💰12.7万円｜⚠日程不明
- 9065 Sankyu Inc.｜granville_tenkan｜業績 ✅順調｜値頃 ⚪妥当｜FAIL_INSEN｜終値1725.0｜💰80.6万円｜⚠日程不明
- 2488 ＪＴＰ｜granville_tenkan｜業績 ✅順調｜値頃 🟡やや割高｜FAIL_INSEN｜終値1367.0｜💰13.9万円｜⚠日程不明
- 417A ブルーゾーンホールディングス｜granville_tenkan｜業績 ✅順調｜値頃 🟡やや割高｜FAIL_INSEN｜終値1991.5｜💰19.5万円｜⚠日程不明
- 4549 Eiken Chemical Co., Ltd.｜granville_tenkan｜業績 ✅順調｜値頃 🟡やや割高｜FAIL_INSEN｜終値2240.0｜💰22.5万円｜⚠日程不明
- 5184 ニチリン｜granville_tenkan｜業績 ✅順調｜値頃 🟡やや割高｜FAIL_INSEN｜終値4115.0｜💰41.5万円｜⚠日程不明
- 7269 スズキ｜granville_tenkan｜業績 ✅順調｜値頃 🟡やや割高｜FAIL_INSEN｜終値2150.0｜💰22.0万円｜⚠日程不明
- 9418 Ｕ－ＮＥＸＴ　ＨＯＬＤＩＮＧＳ｜granville_tenkan｜業績 ✅順調｜値頃 🟡やや割高｜FAIL_INSEN｜終値1868.0｜💰18.8万円｜⚠日程不明
- 3092 ＺＯＺＯ｜granville_tenkan｜業績 ✅順調｜値頃 🔴過熱｜PASS｜終値1211.5｜💰12.1万円｜momentum 1214 SL1140.2 上限1226.1・✅即時可・乖離0.2%｜⚠日程不明
  > 📌【業態】LINEヤフー傘下。衣料品通販サイト「ZOZOTOWN」を運営。ブランド品を受託販売。
  > 📌【いま】終値1,212円・直近5日+3.59%（材料未確認）
  > 📌【調子】✅順調（4/13）
  > 📌【水準】🔴過熱（1.0/7）— PER21.14倍・PEG2.85・52週60.5% ／ 💰単元12.1万円
  > 📌【戦略】当日高値超えの逆指値1214円で順張り参戦を検討。上限1226.1円・SL1140.2円目安
- 3549 クスリのアオキホールディングス｜granville_tenkan｜業績 ✅順調｜値頃 🔴過熱｜FAIL_INSEN｜終値5150.0｜💰50.7万円｜⚠日程不明
- 8113 Unicharm Corporation｜granville_tenkan｜業績 ✅順調｜値頃 🔴過熱｜FAIL_INSEN｜終値1158.5｜💰11.2万円｜⚠日程不明
- 8160 KISOJI CO., LTD.｜granville_tenkan｜業績 ✅順調｜値頃 🔴過熱｜FAIL_UWAHIGE｜終値2603.0｜💰26.0万円｜⚠日程不明
- 9163 Nareru Group Inc.｜granville_tenkan｜業績 ✅順調｜値頃 🟢値頃｜FAIL_INSEN｜終値2043.0｜💰20.8万円｜📋カルテ窓 12/15(残19営業日)
- 8056 ＢＩＰＲＯＧＹ｜granville_tenkan｜業績 ✅順調｜値頃 ⚪妥当｜FAIL_INSEN｜終値4733.0｜💰48.8万円｜⚠日程不明
- 9956 Valor Holdings Co., Ltd.｜granville_tenkan｜業績 ✅順調｜値頃 ⚪妥当｜FAIL_INSEN｜終値1656.0｜💰16.6万円｜⚠日程不明
- 6412 Heiwa Holdings Inc.｜granville_tenkan｜業績 ✅順調｜値頃 ⚪妥当｜PASS｜終値2154.0｜💰21.5万円｜momentum 2159 SL2028.5 上限2180.6・✅即時可・乖離0.2%｜⚠日程不明 📐進捗 遅れ -30.0%
  > 📌【業態】パチンコ、パチスロ機大手。開発力に定評。傘下にゴルフ場運営のアコーディア、PGM。
  > 📌【いま】終値2,154円・直近5日+2.38%（材料未確認）
  > 📌【調子】✅順調（3/13）— ⚠減速・⚠進捗遅れ
  > 📌【水準】⚪妥当（3.0/7）— PER10.47倍・PEG0.849・52週79.7% ／ 💰単元21.5万円
  > 📌【戦略】当日高値超えの逆指値2159円で順張り参戦を検討。上限2180.6円・SL2028.5円目安
- 4540 Tsumura & Co.｜granville_tenkan｜業績 ✅順調｜値頃 🟡やや割高｜FAIL_INSEN｜終値3965.0｜💰39.4万円｜⚠日程不明
- 9045 Keihan Holdings Co., Ltd.｜granville_tenkan｜業績 ⚠減速｜値頃 🟡やや割高｜FAIL_INSEN｜終値3379.0｜💰34.1万円｜⚠日程不明
- 6745 ホーチキ｜granville_tenkan｜業績 ✅順調｜値頃 🔴過熱｜FAIL_INSEN｜終値1960.0｜💰20.7万円｜⚠日程不明
- 3563 ＦＯＯＤ　＆　ＬＩＦＥ　ＣＯＭＰＡＮＩＥＳ｜granville_tenkan｜業績 ✅順調｜値頃 🔴過熱｜FAIL_INSEN｜終値6244.0｜💰64.0万円｜⚠日程不明
- 8801 三井不動産｜granville_tenkan｜業績 ➖横ばい｜値頃 ⚪妥当｜FAIL_INSEN｜終値1589.0｜💰16.2万円｜⚠日程不明
- 5233 太平洋セメント｜granville_tenkan｜業績 🔻悪化｜値頃 🟡やや割高｜FAIL_INSEN｜終値3975.0｜💰40.8万円｜⚠日程不明
- 8803 Heiwa Real Estate Co., Ltd.｜granville_tenkan｜業績 ➖横ばい｜値頃 🟡やや割高｜FAIL_INSEN｜終値2378.0｜💰23.6万円｜⚠日程不明
- 9837 Morito Co., Ltd.｜granville_tenkan｜業績 ➖横ばい｜値頃 🟡やや割高｜FAIL_INSEN｜終値1798.0｜💰18.3万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 9869 Kato Sangyo Co., Ltd.｜granville_tenkan｜業績 ➖横ばい｜値頃 🔴過熱｜FAIL_INSEN｜終値6800.0｜💰67.4万円｜⚠日程不明
- 4922 コーセーホールディングス｜granville_tenkan｜業績 ➖横ばい｜値頃 🔴過熱｜PASS｜終値6218.0｜💰62.2万円｜⛔提案なし(指名鮮度切れ 12営業日)｜⚠日程不明
  > 📌【業態】化粧品大手。高級化粧品に強み。コスメタリー事業も展開。アジア・米国に進出。
  > 📌【いま】終値6,218円・直近5日+0.19%（材料未確認）
  > 📌【調子】➖横ばい（2/13）— 質注意・経常減益-14.7%
  > 📌【水準】🔴過熱（0.0/7）— PER33.61倍・PEG—・52週82.3% ／ 💰単元62.2万円
  > 📌【戦略】発注対象外（⛔提案なし(指名鮮度切れ 12営業日)）
- 9735 セコム｜granville_tenkan｜業績 ➖横ばい｜値頃 🔴過熱｜FAIL_INSEN｜終値7101.0｜💰71.2万円｜⚠日程不明
- 6328 Ebara Jitsugyo Co., Ltd.｜granville_tenkan｜業績 ⚠減速｜値頃 ⚪妥当｜PASS｜終値2292.0｜💰22.9万円｜⛔提案なし(指名鮮度切れ 15営業日)｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8） ⚠業績基調が下向き（⚠減速）
  > 📌【業態】上下水処理施設から空調など環境関連事業に拡大。研究開発・ファブレス型。
  > 📌【いま】終値2,292円・直近5日-0.99%（材料未確認）
  > 📌【調子】⚠減速（1/13）— 質注意・⚠減速・⚠下期依存
  > 📌【水準】⚪妥当（4.0/7）— PER11.99倍・PEG4.115・52週25.7% ／ 💰単元22.9万円
  > 📌【戦略】発注対象外（⛔提案なし(指名鮮度切れ 15営業日)）
- 4912 ライオン｜granville_tenkan｜業績 ⚠減速｜値頃 ⚪妥当｜FAIL_UWAHIGE｜終値2258.0｜💰21.9万円｜⚠日程不明
- 9025 Konoike Transport Co., Ltd.｜granville_tenkan｜業績 ⚠減速｜値頃 ⚪妥当｜FAIL_INSEN｜終値2979.0｜💰29.7万円｜⚠日程不明
- 9404 Nippon Television Holdings, Inc.｜granville_tenkan｜業績 🔻悪化｜値頃 ⚪妥当｜FAIL_INSEN｜終値2991.0｜💰30.5万円｜⚠日程不明
- 1878 Daito Trust Construction Co., Ltd.｜granville_tenkan｜業績 ⚠減速｜値頃 🟡やや割高｜FAIL_INSEN｜終値3385.0｜💰33.1万円｜⚠日程不明
- 1928 積水ハウス｜granville_tenkan｜業績 ⚠減速｜値頃 🟡やや割高｜FAIL_INSEN｜終値3580.0｜💰36.2万円｜📋カルテ窓 12/10(残16営業日)
- 4552 JCR Pharmaceuticals Co., Ltd.｜granville_tenkan｜業績 🔻悪化｜値頃 🔴過熱｜FAIL_INSEN｜終値500.0｜💰5.0万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 5105 ＴＯＹＯ　ＴＩＲＥ｜granville_tenkan｜業績 ⚠減速｜値頃 🟡やや割高｜PASS｜終値4106.0｜💰41.1万円｜⛔提案なし(指名鮮度切れ 15営業日)｜📉決算反応日 11/17 ⚠業績基調が下向き（⚠減速）
  > 📌【業態】タイヤ大手。トラック・バス用に強み。北米向けSUV用タイヤも。株主に三菱商事。
  > 📌【いま】終値4,106円・直近5日-3.07%（材料未確認）
  > 📌【調子】⚠減速（1/13）— 進捗データ取得不可(判定不能)・(質注意)
  > 📌【水準】🟡やや割高（2.0/7）— PER8.16倍・PEG—・52週47.6% ／ 💰単元41.1万円
  > 📌【戦略】発注対象外（⛔提案なし(指名鮮度切れ 15営業日)）
- 8167 リテールパートナーズ｜granville_tenkan｜業績 ⚠減速｜値頃 🟡やや割高｜FAIL_INSEN｜終値1385.0｜💰13.8万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 2267 Yakult Honsha Co., Ltd.｜granville_tenkan｜業績 ⚠減速｜値頃 🔴過熱｜FAIL_UWAHIGE｜終値2924.0｜💰28.6万円｜⚠日程不明
- 9401 東京放送ホールディングス｜granville_tenkan｜業績 ⚠減速｜値頃 🔴過熱｜FAIL_INSEN｜終値6322.0｜💰63.0万円｜⚠日程不明
- 4375 セーフィー｜granville_tenkan/changepoint/changepoint🔔｜業績 取得不可｜値頃 🟢値頃｜FAIL_INSEN｜終値614.0｜💰6.3万円｜⚠日程不明
- 3182 オイシックス｜granville_tenkan｜業績 取得不可｜値頃 ⚪妥当｜FAIL_INSEN｜終値1863.0｜💰18.7万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 4543 Terumo Corporation｜granville_tenkan｜業績 業績データ取得不可(経常益予想非開示)｜値頃 ⚪妥当｜FAIL_UWAHIGE｜終値2508.0｜💰23.3万円｜⚠日程不明
- 7921 ＴＡＫＡＲＡ　＆　ＣＯＭＰＡＮＹ｜granville_tenkan｜業績 業績データ取得不可(経常益予想非開示)｜値頃 ⚪妥当｜FAIL_INSEN｜終値4305.0｜💰43.0万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 2897 Nissin Foods Holdings Co., Ltd.｜granville_tenkan｜業績 取得不可｜値頃 🔴過熱｜FAIL_INSEN｜終値2991.5｜💰29.9万円｜⚠日程不明
- 2811 Kagome Co., Ltd.｜granville_tenkan｜業績 業績データ取得不可(経常益予想非開示)｜値頃 🔴過熱｜FAIL_INSEN｜終値2879.5｜💰28.9万円｜⚠日程不明
- 3401 Teijin Limited｜granville_tenkan｜業績 —｜値頃 —｜FAIL_INSEN｜終値1756.5｜💰—｜⚠日程不明
- 4204 Sekisui Chemical Co., Ltd.｜granville_tenkan｜業績 —｜値頃 —｜FAIL_INSEN｜終値2637.0｜💰—｜⚠日程不明
- 4528 ONO Pharmaceutical Co., Ltd.｜granville_tenkan｜業績 —｜値頃 —｜FAIL_INSEN｜終値2492.0｜💰—｜⚠日程不明
- 4765 ＳＢＩグローバルアセットマネジメント｜granville_tenkan/granville_oshime｜業績 判定保留｜値頃 取得不可｜FAIL_INSEN｜終値611.0｜💰6.2万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 5930 Bunka Shutter Co., Ltd.｜granville_tenkan｜業績 —｜値頃 —｜FAIL_INSEN｜終値1888.0｜💰—｜⚠日程不明
- 9513 Electric Power Development Co., Ltd.｜granville_tenkan｜業績 —｜値頃 —｜FAIL_INSEN｜終値4045.0｜💰—｜⚠日程不明 ⚡材料後出し
- 9605 Toei Company, Ltd.｜granville_tenkan｜業績 —｜値頃 —｜FAIL_INSEN｜終値6180.0｜💰—｜⚠日程不明
- 6570 Kyowa Corporation Co. Ltd.｜granville_oshime｜業績 🚀確変｜値頃 🟢値頃｜FAIL_UWAHIGE｜終値3185.0｜💰30.8万円｜⚠日程不明
- 6574 コンヴァノ｜granville_oshime｜業績 🚀確変｜値頃 🟢値頃｜FAIL_INSEN｜終値984.0｜💰11.4万円｜📉決算反応日 11/17
- 7480 スズデン｜granville_oshime/granville_rebound｜業績 🚀確変｜値頃 ⚪妥当｜PASS｜終値3470.0｜💰34.7万円｜⛔型不一致(既に支持帯以下)｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
  > 📌【業態】FA機器主力、技術商社。オムロンと特約店契約。電設資材中心。ネット販売に強み。
  > 📌【いま】終値3,470円・直近5日-1.70%（材料未確認）
  > 📌【調子】🚀確変（13/13）— 🔼加速
  > 📌【水準】⚪妥当（4.0/7）— PER13.79倍・PEG0.12・52週78.2% ／ 💰単元34.7万円
  > 📌【戦略】発注対象外（⛔型不一致(既に支持帯以下)）
- 3156 レスター｜granville_oshime/granville_rebound｜業績 🚀確変｜値頃 🟢値頃｜FAIL_UWAHIGE｜終値4335.0｜💰50.7万円｜⚠日程不明
- 8051 山善｜granville_oshime｜業績 🔥絶好調｜値頃 🟢値頃｜FAIL_INSEN｜終値1790.0｜💰18.4万円｜⚠日程不明
- 8137 サンワテクノス｜granville_oshime/granville_rebound｜業績 🔥絶好調｜値頃 🟢値頃｜FAIL_UWAHIGE｜終値3715.0｜💰38.7万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 4258 AMIYA Corporation｜granville_oshime/granville_rebound｜業績 🔥絶好調｜値頃 ⚪妥当｜PASS_DOJI｜終値4740.0｜💰47.4万円｜⛔型不一致(十字線: トウバ)｜📉決算反応日 11/17
  > 📌【業態】情報・通信業
  > 📌【いま】終値4,740円・直近5日-18.97%（材料未確認）
  > 📌【調子】🔥絶好調（9/13）— 上方修正済み・⚠下期依存
  > 📌【水準】⚪妥当（3.0/7）— PER38.07倍・PEG1.008・52週44.8% ／ 💰単元47.4万円
  > 📌【戦略】発注対象外（⛔型不一致(十字線: トウバ)）
- 3106 倉敷紡績｜granville_oshime｜業績 🔥絶好調｜値頃 💎割安｜FAIL_UWAHIGE｜終値2012.0｜💰21.3万円｜⚠日程不明
- 8388 阿波銀行｜granville_oshime/granville_rebound｜業績 🔥絶好調｜値頃 💎割安｜FAIL_INSEN｜終値1796.0｜💰19.3万円｜⚠日程不明
- 8392 大分銀行｜granville_oshime/granville_rebound｜業績 🔥絶好調｜値頃 💎割安｜FAIL_INSEN｜終値2475.0｜💰26.6万円｜⚠日程不明
- 9304 澁澤倉庫｜granville_oshime｜業績 🔥絶好調｜値頃 🟢値頃｜FAIL_INSEN｜終値1889.0｜💰19.6万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 153A Caulis, Inc.｜granville_oshime｜業績 🔥絶好調｜値頃 ⚪妥当｜FAIL_UWAHIGE｜終値2278.0｜💰20.7万円｜⚠日程不明
- 3968 セグエグループ｜granville_oshime｜業績 🔥絶好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値849.0｜💰9.0万円｜⚠日程不明
- 4443 Ｓａｎｓａｎ｜granville_oshime/changepoint🔔｜業績 🔥絶好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値2125.0｜💰21.9万円｜⚠日程不明
- 3673 ブロードリーフ｜granville_oshime｜業績 ⚡好調｜値頃 💎割安｜FAIL_UWAHIGE｜終値331.0｜💰3.4万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 5985 SUNCALL CORPORATION｜granville_oshime｜業績 ⚡好調｜値頃 💎割安｜FAIL_INSEN｜終値1480.0｜💰17.7万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 5892 ＹＵＴＯＲＩ｜granville_oshime｜業績 ⚡好調｜値頃 🟢値頃｜FAIL_INSEN｜終値2424.0｜💰26.0万円｜⚠日程不明
- 8159 Tachibana Eletech Co., Ltd.｜granville_oshime｜業績 ⚡好調｜値頃 🟢値頃｜FAIL_UWAHIGE｜終値4225.0｜💰43.5万円｜⚠日程不明
- 3040 ソリトンシステムズ｜granville_oshime/granville_rebound｜業績 ⚡好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値2432.0｜💰26.0万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 7970 Shin-Etsu Polymer Co., Ltd.｜granville_oshime｜業績 ⚡好調｜値頃 ⚪妥当｜PASS｜終値2356.0｜💰23.6万円｜⛔型不一致(既に支持帯以下)｜⚠日程不明
  > 📌【業態】信越化学系樹脂加工メーカー。ウエハ容器が主力。車載タッチスイッチや住生活資材も。
  > 📌【いま】終値2,356円・直近5日-0.30%（材料未確認）
  > 📌【調子】⚡好調（7/13）— E軸:進捗50.7%<前年同期51.7%・🔼加速
  > 📌【水準】⚪妥当（4.0/7）— PER16.06倍・PEG0.564・52週68.2% ／ 💰単元23.6万円
  > 📌【戦略】発注対象外（⛔型不一致(既に支持帯以下)）
- 8410 Seven Bank, Ltd.｜granville_oshime｜業績 ⚡好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値358.20001220703125｜💰3.5万円｜⚠日程不明
- 2492 インフォマート（インフォＭＴ）｜granville_oshime｜業績 ⚡好調｜値頃 🟡やや割高｜FAIL_INSEN｜終値723.0｜💰7.5万円｜⚠日程不明
- 4674 クレスコ｜granville_oshime｜業績 ⚡好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値1906.0｜💰19.6万円｜⚠日程不明
- 2384 ＳＢＳホールディングス｜granville_oshime｜業績 ⚡好調｜値頃 ⚪妥当｜PASS｜終値5650.0｜💰56.5万円｜⛔型不一致(既に支持帯以下)｜⚠日程不明
  > 📌【業態】総合物流会社。物流一括受託が主力。食品輸送に力。物流施設の流動化も。
  > 📌【いま】終値5,650円・直近5日+0.18%（材料未確認）
  > 📌【調子】⚡好調（6/13）— ⚠減速・🔼進捗先行
  > 📌【水準】⚪妥当（3.0/7）— PER15.48倍・PEG0.674・52週84.9% ／ 💰単元56.5万円
  > 📌【戦略】発注対象外（⛔型不一致(既に支持帯以下)）
- 4498 Cybertrust Japan Co.Ltd.｜granville_oshime｜業績 ⚡好調｜値頃 ⚪妥当｜FAIL_UWAHIGE｜終値1553.0｜💰16.7万円｜⚠日程不明
- 4475 HENNGE K.K.｜granville_oshime/changepoint🔔🔔｜業績 ⚡好調｜値頃 🔴過熱｜FAIL_INSEN｜終値2240.0｜💰23.8万円｜⚠日程不明
- 4398 ブロードバンドセキュリティ｜granville_oshime｜業績 ⚡好調｜値頃 🟢値頃｜PASS_DOJI｜終値1972.0｜💰19.7万円｜⛔型不一致(十字線: トウバ)｜⚠日程不明
  > 📌【業態】SBI系。クレジットカードデータのセキュリティ監視やコンサルティングサービス。漏洩対策も。
  > 📌【いま】終値1,972円・直近5日-13.13%（材料未確認）
  > 📌【調子】⚡好調（5/13）— ⚠進捗遅れ
  > 📌【水準】🟢値頃（5.0/7）— PER18.55倍・PEG0.535・52週36.3% ／ 💰単元19.7万円
  > 📌【戦略】発注対象外（⛔型不一致(十字線: トウバ)）
- 338A ZenmuTech,Inc.｜granville_oshime｜業績 ⚡好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値2898.0｜💰32.4万円｜⚠日程不明
- 9536 SAIBU GAS HOLDINGS CO. LTD.｜granville_oshime｜業績 ⚡好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値2919.0｜💰29.0万円｜⚠日程不明
- 436A サイバーソリューションズ（サイバＳＯＬ）｜granville_oshime｜業績 ⚡好調｜値頃 ⚪妥当｜FAIL_UWAHIGE｜終値1606.0｜💰15.7万円｜📋カルテ窓 12/04(残12営業日)
- 3042 セキュアヴェイル（セキュアヴェ）｜granville_oshime｜業績 ⚡好調｜値頃 🟡やや割高｜FAIL_INSEN｜終値683.0｜💰7.4万円｜⚠日程不明
- 4373 Simplex Holdings,Inc.｜granville_oshime｜業績 ⚡好調｜値頃 🟡やや割高｜FAIL_INSEN｜終値1174.0｜💰12.0万円｜⚠日程不明
- 6877 ＯＢＡＲＡ　ＧＲＯＵＰ（ＯＢＡＲＡＧ）｜granville_oshime｜業績 ⚡好調｜値頃 🟡やや割高｜PASS｜終値7250.0｜💰72.5万円｜oshime 6828 SL6794.4・✅即時可・乖離-5.8%｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
  > 📌【業態】自動車業界向け抵抗溶接機器の最大手。半導体向け研磨装置も展開。
  > 📌【いま】終値7,250円・直近5日+8.21%（材料未確認）
  > 📌【調子】⚡好調（5/13）— E軸判定不能(期首・進捗なし)
  > 📌【水準】🟡やや割高（2.0/7）— PER11.06倍・PEG1.991・52週93.1% ／ 💰単元72.5万円
  > 📌【戦略】6828円までの押し目を指値で待つ。SL6794.4円（25日線基準）
- 8395 佐賀銀行｜granville_oshime/granville_rebound｜業績 ⚠減速｜値頃 🟢値頃｜FAIL_INSEN｜終値5760.0｜💰60.7万円｜⚠日程不明
- 5036 日本ビジネスシステムズ｜granville_oshime｜業績 ✅順調｜値頃 ⚪妥当｜FAIL_INSEN｜終値1475.0｜💰15.7万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 6080 Ｍ＆Ａキャピタルパートナーズ｜granville_oshime/changepoint/changepoint🔔/changepoint🔔🔔｜業績 ✅順調｜値頃 🟡やや割高｜FAIL_INSEN｜終値4490.0｜💰45.9万円｜⚠日程不明
- 9552 クオンツ総研ホールディングス｜granville_oshime｜業績 ✅順調｜値頃 🟡やや割高｜FAIL_INSEN｜終値1185.0｜💰11.5万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 3762 テクマトリックス（テクマト）｜granville_oshime｜業績 ✅順調｜値頃 🔴過熱｜FAIL_UWAHIGE｜終値3070.0｜💰31.4万円｜⚠日程不明
- 9509 Hokkaido Electric Power Company,Incorporated｜granville_oshime｜業績 🔻悪化｜値頃 ⚪妥当｜FAIL_INSEN｜終値1093.5｜💰11.5万円｜⚠日程不明
- 456A Human Made Inc.｜granville_oshime｜業績 ✅順調｜値頃 🔴過熱｜PASS｜終値1955.0｜💰19.6万円｜⛔型不一致(既に支持帯以下)｜📋カルテ窓 12/11(残17営業日)
  > 📌【業態】ストリートファッションなどを主力とするアパレルブランドを展開する。
  > 📌【いま】終値1,955円・直近5日-9.11%（材料未確認）
  > 📌【調子】✅順調（3/13）— D軸判定不能(直近Q比較不可)・E軸判定不能(進捗データ不足)・質注意
  > 📌【水準】🔴過熱（0.0/7）— PER54.31倍・PEG5.643・52週81.5% ／ 💰単元19.6万円
  > 📌【戦略】発注対象外（⛔型不一致(既に支持帯以下)）
- 3692 ＦＦＲＩセキュリティ｜granville_oshime｜業績 ➖横ばい｜値頃 🟡やや割高｜FAIL_UWAHIGE｜終値6070.0｜💰65.9万円｜⚠日程不明
- 336A ダイナミックマッププラットフォーム｜granville_oshime｜業績 取得不可｜値頃 ⚪妥当｜FAIL_INSEN｜終値1174.0｜💰13.2万円｜⚠日程不明
- 3697 SHIFT, Inc.｜granville_oshime｜業績 業績データ取得不可(経常益予想非開示)｜値頃 ⚪妥当｜FAIL_INSEN｜終値1072.0｜💰10.6万円｜⚠日程不明
- 6027 Bengo4.com, Inc.｜granville_oshime｜業績 取得不可｜値頃 ⚪妥当｜PASS｜終値4480.0｜💰44.8万円｜⛔型不一致(既に支持帯以下)｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
  > 📌【業態】法律相談と弁護士・税理士向け営業支援サイト運営。電子契約サービスが拡大。
  > 📌【いま】終値4,480円・直近5日-12.16%（材料未確認）
  > 📌【調子】取得不可（—/13）— 業績データ取得不可(経常益予想非開示)・🔼加速
  > 📌【水準】⚪妥当（3.0/7）— PER51.08倍・PEG—・52週61% ／ 💰単元44.8万円
  > 📌【戦略】発注対象外（⛔型不一致(既に支持帯以下)）
- 6191 エボラブルアジア｜granville_oshime｜業績 取得不可｜値頃 ⚪妥当｜FAIL_UWAHIGE｜終値1567.0｜💰15.4万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 4432 ウイングアーク１ｓｔ｜granville_oshime｜業績 業績データ取得不可(経常益予想非開示)｜値頃 🟡やや割高｜FAIL_INSEN｜終値3525.0｜💰35.5万円｜⚠日程不明
- 3547 UNISIA HOLDINGS CO.｜granville_oshime｜業績 —｜値頃 —｜FAIL_INSEN｜終値1950.0｜💰—｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 4686 JUSTSYSTEMS CORPORATION｜granville_oshime｜業績 —｜値頃 —｜FAIL_INSEN｜終値4795.0｜💰—｜⚠日程不明
- 6490 ＰＩＬＬＡＲ｜granville_rebound｜業績 🚀確変｜値頃 🟢値頃｜FAIL_INSEN｜終値8590.0｜💰91.7万円｜⚠日程不明
- 6862 ミナト HD｜granville_rebound｜業績 🚀確変｜値頃 💎割安｜FAIL_UWAHIGE｜終値2913.0｜💰30.2万円｜⚠日程不明
- 3851 日本一ソフトウェア｜granville_rebound｜業績 🚀確変｜値頃 💎割安｜PASS_DOJI｜終値917.0｜💰9.2万円｜momentum 927 SL885 上限936.3・⏳確認足待ち・乖離1.1%｜⚠日程不明 ⚠市場に劣後 RS20 -29.3pt 📐進捗 上振れ 51.0%
  > 📌【業態】ソニーPS5、ニンテンドースイッチ主力とするゲームソフトメーカー。スマホ向けゲームアプリにも注力。
  > 📌【いま】終値917円・直近5日-21.08%（材料未確認）
  > 📌【調子】🚀確変（11/13）— 黒字転換・E軸判定不能(進捗データ不足)・突出ボーナス・🔼加速・🔼進捗先行
  > 📌【水準】💎割安（7.0/7）— PER6.46倍・PEG0.004・52週19.3% ／ 💰単元9.2万円
  > 📌【戦略】当日高値超えの逆指値927円で順張り参戦を検討。上限936.3円・SL885円目安
- 3891 ニッポン高度紙工業｜granville_rebound｜業績 🚀確変｜値頃 💎割安｜FAIL_UWAHIGE｜終値5220.0｜💰57.9万円｜⚠日程不明
- 6138 ダイジェット工業（ダイジェト）｜granville_rebound｜業績 🚀確変｜値頃 💎割安｜FAIL_INSEN｜終値1624.0｜💰17.3万円｜⚠日程不明
- 5381 Mipox Corp.｜granville_rebound｜業績 🚀確変｜値頃 🟢値頃｜FAIL_UWAHIGE｜終値849.0｜💰8.4万円｜⚠日程不明
- 4419 Finatext Holdings Ltd.｜granville_rebound/changepoint🔔｜業績 🚀確変｜値頃 ⚪妥当｜FAIL_INSEN｜終値1069.0｜💰11.9万円｜⚠日程不明
- 4968 Arakawa Chemical Industries,Ltd.｜granville_rebound｜業績 🔥絶好調｜値頃 🟢値頃｜PASS_DOJI｜終値1736.0｜💰17.4万円｜⛔型不一致(十字線: 下放れ直後)｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
  > 📌【業態】化学（ファインケミカル・接着剤・製紙関連）
  > 📌【いま】終値1,736円・直近5日-6.67%（材料未確認）
  > 📌【調子】🔥絶好調（10/13）— 上方修正済み・突出ボーナス・🔼加速・🔼進捗先行
  > 📌【水準】🟢値頃（5.0/7）— PER10.76倍・PEG0.15・52週41.4% ／ 💰単元17.4万円
  > 📌【戦略】発注対象外（⛔型不一致(十字線: 下放れ直後)）
- 6317 Kitagawa Corporation｜granville_rebound｜業績 🔥絶好調｜値頃 🟢値頃｜FAIL_INSEN｜終値2723.0｜💰27.9万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 7713 Sigma Koki Co., Ltd.｜granville_rebound｜業績 🔥絶好調｜値頃 🟢値頃｜FAIL_INSEN｜終値2526.0｜💰28.9万円｜⚠日程不明
- 8364 清水銀行｜granville_rebound｜業績 🔥絶好調｜値頃 🟢値頃｜FAIL_INSEN｜終値2576.0｜💰27.4万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 2962 テクニスコ｜granville_rebound｜業績 🔥絶好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値1182.0｜💰14.9万円｜⚠日程不明
- 1436 GreenEnergy & Company｜granville_rebound｜業績 🔥絶好調｜値頃 💎割安｜FAIL_INSEN｜終値1289.0｜💰14.2万円｜📋カルテ窓 12/08(残14営業日)
- 2489 アドウェイズ｜granville_rebound｜業績 ⚠減速｜値頃 💎割安｜PASS｜終値316.0｜💰3.2万円｜reversal 316 SL310・✅即時可｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8） ⚠業績基調が下向き（⚠減速） 📐進捗 上振れ 93.0%
  > 📌【業態】PC・スマホ向けアフィリエイト広告で国内大手。広告自動配信ツール「UNICORN」が拡大。
  > 📌【いま】終値316円・直近5日-3.95%（材料未確認）
  > 📌【調子】⚠減速（9/13）— 減収上限・🔼進捗先行
  > 📌【水準】💎割安（6.0/7）— PER13.74倍・PEG0.073・52週33.9% ／ 💰単元3.2万円
  > 📌【戦略】当日終値316円の指値で反転を取りにいく。SL310円（直近5日安値）
- 479A PRONI Inc.｜granville_rebound/changepoint🔔｜業績 🔥絶好調｜値頃 💎割安｜FAIL_INSEN｜終値1016.0｜💰15.0万円｜⚠日程不明 ⚡材料後出し
- 7609 Daitron Co., Ltd.｜granville_rebound｜業績 🔥絶好調｜値頃 💎割安｜PASS｜終値3540.0｜💰35.4万円｜reversal 3540 SL3450・✅即時可｜⚠日程不明 📐進捗 上振れ 26.2%
  > 📌【業態】電子部品卸中堅。製造装置にも強み。スイッチ電源など自社製造製品に注力。
  > 📌【いま】終値3,540円・直近5日-1.39%（材料未確認）
  > 📌【調子】🔥絶好調（9/13）— 上方修正済み・🔼進捗先行
  > 📌【水準】💎割安（6.0/7）— PER10.6倍・PEG0.317・52週48.4% ／ 💰単元35.4万円
  > 📌【戦略】当日終値3540円の指値で反転を取りにいく。SL3450円（直近5日安値）
- 3793 Drecom Co., Ltd.｜granville_rebound｜業績 ⚠減速｜値頃 🟢値頃｜FAIL_INSEN｜終値432.0｜💰4.6万円｜⚠日程不明
- 5256 Fusic Co.,Ltd.｜granville_rebound｜業績 🔥絶好調｜値頃 🟢値頃｜PASS｜終値2581.0｜💰25.8万円｜reversal 2581 SL2320・✅即時可｜⚠日程不明 📐進捗 遅れ -66.0%
  > 📌【業態】研究機関向けシステム開発やIoT・クラウド・AI活用したデジタルトランスフォーメーション事業。
  > 📌【いま】終値2,581円・直近5日-2.97%（材料未確認）
  > 📌【調子】🔥絶好調（9/13）— 突出ボーナス・⚠進捗遅れ・⚠下期依存
  > 📌【水準】🟢値頃（5.0/7）— PER18.2倍・PEG0.098・52週26.7% ／ 💰単元25.8万円
  > 📌【戦略】当日終値2581円の指値で反転を取りにいく。SL2320円（直近5日安値）
- 7715 長野計器｜granville_rebound｜業績 🔥絶好調｜値頃 🟢値頃｜FAIL_INSEN｜終値3080.0｜💰33.5万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 150A ＪＳＨ｜granville_rebound｜業績 🔥絶好調｜値頃 ⚪妥当｜FAIL_UWAHIGE｜終値851.0｜💰8.4万円｜⚠日程不明
- 6840 ＡＫＩＢＡホールディングス｜granville_rebound｜業績 🔥絶好調｜値頃 💎割安｜FAIL_INSEN｜終値557.0｜💰6.0万円｜⚠日程不明
- 460A ＢＲＡＮＵ｜granville_rebound｜業績 🔥絶好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値1025.0｜💰10.5万円｜📋カルテ窓 12/14(残18営業日)
- 4431 Smaregi, Inc.｜granville_rebound｜業績 🔥絶好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値3215.0｜💰34.0万円｜📋カルテ窓 12/15(残19営業日)
- 6508 Meidensha Corporation｜granville_rebound｜業績 ⚡好調｜値頃 💎割安｜PASS_DOJI｜終値6869.0｜💰68.7万円｜⛔提案なし(指名鮮度切れ 11営業日)｜⚠日程不明
  > 📌【業態】住友系・老舗重電。電力・エネルギー、水処理制御システム、電鉄用、車電動化に強み。
  > 📌【いま】終値6,869円・直近5日-7.53%・📌その他重要開示法定事前開示書類（吸収分割）（明電ファシリティサービス株式会社）
  > 📌【調子】⚡好調（7/13）— 上方修正済み・進捗モデル値域外・⚠進捗遅れ
  > 📌【水準】💎割安（6.0/7）— PER11.98倍・PEG0.47・52週20.2% ／ 💰単元68.7万円
  > 📌【戦略】発注対象外（⛔提案なし(指名鮮度切れ 11営業日)）
- 5367 Nikkato Corporation｜granville_rebound｜業績 ⚡好調｜値頃 🟢値頃｜PASS_DOJI｜終値955.0｜💰9.6万円｜⛔提案なし(指名鮮度切れ 11営業日)｜⚠日程不明
  > 📌【業態】工業用セラミックス中堅。耐摩耗・耐熱など高付加価値品に強み。エンジニアリングも。
  > 📌【いま】終値955円・直近5日-7.64%（材料未確認）
  > 📌【調子】⚡好調（7/13）— 上方修正済み・🔼進捗先行
  > 📌【水準】🟢値頃（5.0/7）— PER12.7倍・PEG1.011・52週24.8% ／ 💰単元9.6万円
  > 📌【戦略】発注対象外（⛔提案なし(指名鮮度切れ 11営業日)）
- 6742 京三製作所｜granville_rebound｜業績 ⚡好調｜値頃 🟢値頃｜FAIL_UWAHIGE｜終値852.0｜💰9.6万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 8344 Yamagata Bank, Ltd.｜granville_rebound｜業績 ⚡好調｜値頃 🟢値頃｜PASS_DOJI｜終値3935.0｜💰39.4万円｜⛔型不一致(十字線: 下放れ直後)｜⚠日程不明
  > 📌【業態】山形地盤の地銀中堅。県内シェア首位。県指定金融機関で自治体取引に強み。
  > 📌【いま】終値3,935円・直近5日-7.41%（材料未確認）
  > 📌【調子】⚡好調（7/13）— 🔼進捗先行
  > 📌【水準】🟢値頃（5.0/7）— PER14.24倍・PEG0.326・52週52.4% ／ 💰単元39.4万円
  > 📌【戦略】発注対象外（⛔型不一致(十字線: 下放れ直後)）
- 5252 日本ナレッジ｜granville_rebound｜業績 ⚡好調｜値頃 🟡やや割高｜FAIL_INSEN｜終値967.0｜💰10.2万円｜📉決算反応日 11/17
- 9697 カプコン｜granville_rebound｜業績 ⚡好調｜値頃 🔴過熱｜FAIL_INSEN｜終値4493.0｜💰45.1万円｜⚠日程不明
- 477A Startline CO.,LTD.｜granville_rebound｜業績 ⚡好調｜値頃 💎割安｜FAIL_INSEN｜終値549.0｜💰6.0万円｜⚠日程不明
- 4100 Toda Kogyo Corp.｜granville_rebound｜業績 ⚡好調｜値頃 💎割安｜FAIL_UWAHIGE｜終値1537.0｜💰18.1万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8） ⚡材料後出し
- 3850 INTRAMART CORPORATION｜granville_rebound｜業績 ⚡好調｜値頃 🟢値頃｜PASS｜終値3225.0｜💰32.2万円｜reversal 3225 SL3185・✅即時可｜⚠日程不明 📐進捗 上振れ 46.6%
  > 📌【業態】NTTデータ子会社でシステム開発・販売会社。ウェブシステム基盤構築ソフトに強み。コンサルも。
  > 📌【いま】終値3,225円・直近5日-4.02%（材料未確認）
  > 📌【調子】⚡好調（6/13）— 上方修正済み・🔼進捗先行
  > 📌【水準】🟢値頃（5.0/7）— PER11.4倍・PEG0.683・52週42.6% ／ 💰単元32.2万円
  > 📌【戦略】当日終値3225円の指値で反転を取りにいく。SL3185円（直近5日安値）
- 6947 図研｜granville_rebound｜業績 ⚡好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値5100.0｜💰52.2万円｜⚠日程不明
- 6958 日本シイエムケイ｜granville_rebound｜業績 ⚡好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値685.0｜💰7.2万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 7826 フルヤ金属｜granville_rebound｜業績 ⚡好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値7800.0｜💰88.7万円｜⚠日程不明
- 7213 LECIP Holdings Corporation｜granville_rebound｜業績 ⚡好調｜値頃 💎割安｜FAIL_UWAHIGE｜終値579.0｜💰5.8万円｜⚠日程不明
- 4667 Aisan Technology Co.,Ltd.｜granville_rebound/changepoint/changepoint🔔｜業績 ⚡好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値662.0｜💰7.2万円｜⚠日程不明
- 6904 Harada Industry Co., Ltd.｜granville_rebound｜業績 ⚡好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値657.0｜💰6.9万円｜⚠日程不明
- 9278 BOOKOFF GROUP HOLDINGS LIMITED｜granville_rebound｜業績 ⚡好調｜値頃 🟡やや割高｜FAIL_INSEN｜終値2598.0｜💰25.9万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8） ⚡材料後出し
- 7256 河西工業｜granville_rebound｜業績 ⚡好調｜値頃 🔴過熱｜PASS｜終値375.0｜💰—｜⛔提案なし(指名鮮度切れ 15営業日)｜📉決算反応日 11/17
  > 📌【業態】自動車内装部品メーカー。日産向け過半。ドア・天井など主力。米英で現地生産。
  > 📌【いま】終値375円・直近5日-6.25%（材料未確認）
  > 📌【調子】⚡好調（5/13）— E軸判定不能(進捗データ不足)
  > 📌【水準】🔴過熱（1.4/7）— PER16.52倍・PEG3.161・52週54.1% ／ 💰単元—
  > 📌【戦略】発注対象外（⛔提案なし(指名鮮度切れ 15営業日)）
- 3763 Pro-Ship Incorporated｜granville_rebound｜業績 ⚡好調｜値頃 🔴過熱｜FAIL_INSEN｜終値1834.0｜💰21.0万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 4025 多木化学｜granville_rebound｜業績 ✅順調｜値頃 ⚪妥当｜FAIL_UWAHIGE｜終値5350.0｜💰52.7万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 428A Cypress Holdings Co., Ltd.｜granville_rebound｜業績 ✅順調｜値頃 ⚪妥当｜FAIL_INSEN｜終値1393.0｜💰14.9万円｜⚠日程不明
- 3371 ソフトクリエイトホールディングス｜granville_rebound｜業績 ✅順調｜値頃 🟡やや割高｜FAIL_INSEN｜終値2004.0｜💰20.5万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 278A Ｔｅｒｒａ　Ｄｒｏｎｅ｜granville_rebound｜業績 ✅順調｜値頃 ⏸判定不能｜FAIL_UWAHIGE｜終値4990.0｜💰—｜📋カルテ窓 12/15(残19営業日)
- 4396 System Support Holdings Inc.｜granville_rebound｜業績 ✅順調｜値頃 ⚪妥当｜FAIL_INSEN｜終値1292.0｜💰13.4万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
- 5599 S&J Corporation｜granville_rebound｜業績 ✅順調｜値頃 ⚪妥当｜PASS_DOJI｜終値1401.0｜💰14.0万円｜momentum 1444 SL1364 上限1458.4・⏳確認足待ち・乖離3.1%｜⚠日程不明 ⚠市場に劣後 RS20 -16.9pt 📐進捗 遅れ -20.2%
  > 📌【業態】サイバーセキュリティ対策専業。企業中心に監視・受託・コンサルティングサービスを手掛ける。
  > 📌【いま】終値1,401円・直近5日-16.85%（材料未確認）
  > 📌【調子】✅順調（3/13）— 質注意・⚠減速・⚠進捗遅れ・⚠下期依存
  > 📌【水準】⚪妥当（3.0/7）— PER19.27倍・PEG2.377・52週31.1% ／ 💰単元14.0万円
  > 📌【戦略】当日高値超えの逆指値1444円で順張り参戦を検討。上限1458.4円・SL1364円目安
- 6676 BUFFALO INC.｜granville_rebound｜業績 ⚠減速｜値頃 🟡やや割高｜PASS｜終値3180.0｜💰31.8万円｜⛔提案なし(材料後出し)｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8） ⚡材料後出し ⚠業績基調が下向き（⚠減速）
  > 📌【業態】PC周辺機器大手。WI-FI、ストレージに強み。製麺のシマダヤはスピンオフ上場。
  > 📌【いま】終値3,180円・直近5日+0.00%・📌その他重要開示[Delayed]Consolidated Financial Results for the Six Months Ended September 30, 2026
  > 📌【調子】⚠減速（3/13）— A成長率0以下のためレバレッジ計算不可(C=0)・上方修正済み・質注意・減収・🔼加速・🔼進捗先行
  > 📌【水準】🟡やや割高（2.0/7）— PER12.17倍・PEG—・52週62.6% ／ 💰単元31.8万円
  > 📌【戦略】発注対象外（⛔提案なし(材料後出し)）
- 6203 Howa Machinery, Ltd.｜granville_rebound｜業績 ⚠減速｜値頃 ⚪妥当｜FAIL_INSEN｜終値1707.0｜💰19.1万円｜⚠日程不明
- 4884 Kringle Pharma, Inc.｜granville_rebound｜業績 ⚠減速｜値頃 🔴過熱｜PASS｜終値574.0｜💰5.7万円｜⛔提案なし(材料後出し)｜⚠日程不明 ⚡材料後出し ⚠業績基調が下向き（⚠減速）
  > 📌【業態】HGFタンパク質を用いた難治性疾患の治療薬の研究開発を手掛ける。
  > 📌【いま】終値574円・直近5日+10.60%・📌その他重要開示2026年9月期 通期決算説明会 質疑応答について
  > 📌【調子】⚠減速（2/13）— 赤字企業(経常赤字)・E軸判定不能(期首・進捗なし)・減収
  > 📌【水準】🔴過熱（1.4/7）— PER—倍・PEG—・52週63.2% ／ 💰単元5.7万円
  > 📌【戦略】発注対象外（⛔提案なし(材料後出し)）
- 3565 Ascentech KK｜granville_rebound｜業績 🔻悪化｜値頃 ⚪妥当｜FAIL_INSEN｜終値440.0｜💰4.6万円｜📋カルテ窓 12/15(残19営業日) 📑TOPIX低減対象（次 01/29 第2回/8）
- 4240 Cluster Technology Co., Ltd.｜granville_rebound｜業績 🔻悪化｜値頃 🟡やや割高｜FAIL_INSEN｜終値495.0｜💰5.3万円｜⚠日程不明
- 8360 Yamanashi Chuo Bank, Ltd.｜granville_rebound｜業績 取得不可｜値頃 💎割安｜FAIL_INSEN｜終値1170.0｜💰12.5万円｜⚠日程不明
- 8377 ほくほくフィナンシャルグループ｜granville_rebound｜業績 業績データ取得不可(売上/経常欠損)｜値頃 💎割安｜FAIL_INSEN｜終値718.0999755859375｜💰7.7万円｜⚠日程不明
- 3691 DIGITAL PLUS, Inc.｜granville_rebound｜業績 取得不可｜値頃 🟢値頃｜FAIL_INSEN｜終値1246.0｜💰13.4万円｜⚠日程不明 ⚡材料後出し
- 8368 Hyakugo Bank, Ltd.｜granville_rebound｜業績 業績データ取得不可(売上/経常欠損)｜値頃 ⚪妥当｜FAIL_INSEN｜終値1934.0｜💰20.6万円｜⚠日程不明
- 7380 Juroku Financial Group,Inc.｜granville_rebound｜業績 業績データ取得不可(売上/経常欠損)｜値頃 ⚪妥当｜FAIL_INSEN｜終値2224.0｜💰23.3万円｜⚠日程不明
- 8551 北日本銀行｜granville_rebound｜業績 取得不可｜値頃 ⚪妥当｜PASS｜終値2112.0｜💰21.1万円｜reversal 2112 SL2073・✅即時可｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
  > 📌【業態】東北太平洋側地盤の地銀中位。岩手中心。サービス業取引に強み。個人にシフト。
  > 📌【いま】終値2,112円・直近5日-6.67%（材料未確認）
  > 📌【調子】取得不可（—/13）— 業績データ取得不可(売上予想非開示)・🔼進捗先行
  > 📌【水準】⚪妥当（3.0/7）— PER11.33倍・PEG2.796・52週44.2% ／ 💰単元21.1万円
  > 📌【戦略】当日終値2112円の指値で反転を取りにいく。SL2073円（直近5日安値）
- 7184 富山第一銀行｜granville_rebound｜業績 取得不可｜値頃 🟡やや割高｜FAIL_INSEN｜終値2883.0｜💰31.0万円｜⚠日程不明
- 3858 Ubiquitous AI Corporation｜granville_rebound｜業績 —｜値頃 －未評価（次回①-9で算定）｜PASS_DOJI｜終値388.0｜💰—｜momentum 399 SL367 上限403.0・⏳確認足待ち・乖離2.8%｜⚠日程不明
  > 📌【業態】組込みソフトの開発会社。海外製品の組込みも。IoT関連ソリューションに注力。
  > 📌【いま】終値388円・直近5日-22.24%（材料未確認）
  > 📌【調子】—（—/13）
  > 📌【水準】－未評価（次回①-9で算定）（—/7）— PER—倍・PEG—・52週20.7% ／ 💰単元—
  > 📌【戦略】当日高値超えの逆指値399円で順張り参戦を検討。上限403.0円・SL367円目安
- 3909 Showcase, Inc. (Japan)｜granville_rebound｜業績 —｜値頃 —｜FAIL_UWAHIGE｜終値580.0｜💰—｜⚠日程不明
- 4040 NANKAI CHEMICAL COMPANY LIMITED｜granville_rebound｜業績 —｜値頃 —｜FAIL_INSEN｜終値3835.0｜💰—｜⚠日程不明
- 4075 ブレインズテクノロジー｜granville_rebound｜業績 取得不可｜値頃 取得不可｜FAIL_INSEN｜終値995.0｜💰10.9万円｜📋カルテ窓 12/11(残17営業日)
- 5033 Nulab Inc.｜granville_rebound｜業績 —｜値頃 —｜FAIL_INSEN｜終値1075.0｜💰—｜⚠日程不明
- 6890 Ferrotec Corporation｜granville_rebound｜業績 業績データ取得不可｜値頃 取得不可｜FAIL_UWAHIGE｜終値6774.0｜💰76.2万円｜📉決算反応日 11/17 📑TOPIX新規採用（2026-10-30 組入）
- 7175 Imamura Securities Co.Ltd.｜granville_rebound｜業績 業績データ取得不可｜値頃 ⏸判定不能｜FAIL_INSEN｜終値1625.0｜💰16.1万円｜⚠日程不明
- 8609 岡三証券グループ｜granville_rebound｜業績 業績データ取得不可｜値頃 ⏸判定不能｜FAIL_INSEN｜終値1008.0｜💰10.6万円｜⚠日程不明
- 8739 スパークス・グループ｜granville_rebound｜業績 業績データ取得不可｜値頃 ⏸判定不能｜PASS｜終値2424.0｜💰24.2万円｜⛔提案なし(指名鮮度切れ 15営業日)｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
  > 📌【業態】独立系投資顧問。中小型株に定評。韓国、香港で資産運用子会社。運用多角。
  > 📌【いま】終値2,424円・直近5日+1.17%・📌その他重要開示Renewable Energy Aggregation Service Agreement Signed for the Existing Onshore Wind Farm
  > 📌【調子】業績データ取得不可（—/13）— 通期予想なし
  > 📌【水準】⏸判定不能（—/7）— PER—倍・PEG—・52週77.7% ／ 💰単元24.2万円
  > 📌【戦略】発注対象外（⛔提案なし(指名鮮度切れ 15営業日)）

## 変化点銘柄
- 5803 Fujikura Ltd.｜changepoint🔔｜業績 🚀確変｜値頃 💎割安｜FAIL_INSEN｜終値2590.5｜💰31.2万円｜⚠日程不明 🔒実弾封印中(PL3紙ログ収集中)
- 265A エイチエムコム｜changepoint/changepoint🔔｜業績 🚀確変｜値頃 🟢値頃｜FAIL_INSEN｜終値550.0｜💰6.6万円｜⚠日程不明 🔒実弾封印中(PL3紙ログ収集中)
- 4011 Headwaters Co.,Ltd｜changepoint🔔｜業績 🚀確変｜値頃 🟢値頃｜FAIL_INSEN｜終値1689.0｜💰18.3万円｜⚠日程不明 🔒実弾封印中(PL3紙ログ収集中)
- 7695 交換できるくん｜changepoint/changepoint🔔/changepoint🔔🔔｜業績 🚀確変｜値頃 ⚪妥当｜FAIL_UWAHIGE｜終値908.0｜💰8.4万円｜⚠日程不明 🔒実弾封印中(PL3紙ログ収集中)
- 8151 東陽テクニカ｜changepoint🔔/changepoint🔔🔔｜業績 ⚡好調｜値頃 💎割安｜FAIL_INSEN｜終値1753.0｜💰18.1万円｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8） 🔒実弾封印中(PL3紙ログ収集中)
- 593A Tier IV, Inc.｜changepoint🔔🔔/changepoint/changepoint🔔｜業績 ⚡好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値1962.0｜💰20.3万円｜⚠日程不明 📑TOPIX新規採用（2026-10-30 組入） ⚡材料後出し 🔒実弾封印中(PL3紙ログ収集中)
- 4488 AI inside Inc.｜changepoint🔔｜業績 ⚡好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値1749.0｜💰17.9万円｜⚠日程不明 🔒実弾封印中(PL3紙ログ収集中)
- 9343 アイビス｜changepoint/changepoint🔔/changepoint🔔🔔｜業績 ⚡好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値689.0｜💰7.0万円｜⚠日程不明 🔒実弾封印中(PL3紙ログ収集中)
- 286A ユカリア｜changepoint🔔｜業績 ⚡好調｜値頃 🟢値頃｜FAIL_INSEN｜終値718.0｜💰7.5万円｜⚠日程不明 🔒実弾封印中(PL3紙ログ収集中)
- 218A Liberaware｜changepoint/changepoint🔔｜業績 ⚡好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値728.0｜💰8.0万円｜📋カルテ窓 12/11(残17営業日) ⚡材料後出し 🔒実弾封印中(PL3紙ログ収集中)
- 4483 JMDC｜changepoint🔔/changepoint🔔🔔｜業績 ⚡好調｜値頃 🔴過熱｜FAIL_INSEN｜終値3685.0｜💰37.4万円｜⚠日程不明 🔒実弾封印中(PL3紙ログ収集中)
- 3923 ラクス｜changepoint🔔🔔/changepoint🔔｜業績 ⚠減速｜値頃 ⚪妥当｜FAIL_INSEN｜終値1104.0｜💰11.4万円｜⚠日程不明 🔒実弾封印中(PL3紙ログ収集中)
- 4165 PLAID Inc.｜changepoint🔔🔔｜業績 ✅順調｜値頃 🔴過熱｜FAIL_INSEN｜終値549.0｜💰7.8万円｜⚠日程不明 🔒実弾封印中(PL3紙ログ収集中)
- 4259 ExaWizards Inc.｜changepoint/changepoint🔔/changepoint🔔🔔｜業績 取得不可｜値頃 ⚪妥当｜FAIL_INSEN｜終値528.0｜💰5.8万円｜⚠日程不明 🔒実弾封印中(PL3紙ログ収集中)
- 4478 freee K.K.｜changepoint/changepoint🔔/changepoint🔔🔔｜業績 取得不可｜値頃 ⚪妥当｜FAIL_UWAHIGE｜終値3535.0｜💰38.8万円｜⚠日程不明 📑TOPIX新規採用（2026-10-30 組入） 🔒実弾封印中(PL3紙ログ収集中)
- 3989 シェアテク｜changepoint🔔｜業績 取得不可｜値頃 ⏸判定不能｜PASS｜終値1548.0｜💰15.5万円｜changepoint 1548 SL1533・✅即時可｜⚠日程不明 🔒実弾封印中(PL3紙ログ収集中) ℹ相対強い RS20 5.4pt
  > 📌【業態】家庭の生活トラブルに対応するマッチングサイトを運営。登録は便利屋が中心。
  > 📌【いま】終値1,548円・直近5日+0.45%（材料未確認）
  > 📌【調子】取得不可（—/13）— 業績データ取得不可(売上/経常欠損)
  > 📌【水準】⏸判定不能（—/7）— PER—倍・PEG—・52週88.4% ／ 💰単元15.5万円
  > 📌【戦略】発火日終値1548円の指値。追撃禁止・SL1533円。🔒実弾封印中（PL3紙ログ収集中）

## 🤖AI特需銘柄
波: なし（ai_scan 2026-11-17）
- 6777 santec｜ai_momentum/ai_reversal｜業績 🚀確変｜値頃 ⚪妥当｜FAIL_INSEN｜終値17310.0｜💰195.4万円｜⚠日程不明 📑TOPIX新規採用（2026-10-30 組入）
- 6613 QD Laser, Inc.｜ai_momentum/granville_oshime｜業績 🔥絶好調｜値頃 🔴過熱｜FAIL_INSEN｜終値1613.0｜💰19.8万円｜⚠日程不明 📑TOPIX新規採用（2026-10-30 組入）
- 6988 日東電工｜ai_momentum/ai_reversal｜業績 ⚡好調｜値頃 🟡やや割高｜FAIL_INSEN｜終値3544.0｜💰35.5万円｜⚠日程不明
- 4063 信越化学工業｜ai_momentum/ai_reversal｜業績 ✅順調｜値頃 ⚪妥当｜FAIL_UWAHIGE｜終値5574.0｜💰57.0万円｜⚠日程不明
- 6367 ダイキン工業｜ai_momentum｜業績 ✅順調｜値頃 🔴過熱｜FAIL_INSEN｜終値23130.0｜💰234.8万円｜⚠日程不明
- 1975 新日本空調｜ai_momentum｜業績 ➖横ばい｜値頃 ⚪妥当｜FAIL_INSEN｜終値3185.0｜💰34.6万円｜⚠日程不明
- 3374 内外テック｜ai_reversal/granville_rebound｜業績 🚀確変｜値頃 💎割安｜FAIL_UWAHIGE｜終値3325.0｜💰40.2万円｜⚠日程不明
- 4047 関東電化工業｜ai_reversal｜業績 🚀確変｜値頃 💎割安｜FAIL_INSEN｜終値1536.0｜💰17.1万円｜⚠日程不明 🤖AI特需 🔬基板・素材/上流
- 6407 CKD｜ai_reversal｜業績 🚀確変｜値頃 💎割安｜FAIL_INSEN｜終値3868.0｜💰40.5万円｜⚠日程不明
- 5801 古河電気工業｜ai_reversal｜業績 🔥絶好調｜値頃 💎割安｜FAIL_INSEN｜終値1870.0｜💰21.7万円｜⚠日程不明
- 6787 メイコー｜ai_reversal｜業績 🔥絶好調｜値頃 💎割安｜FAIL_UWAHIGE｜終値7440.0｜💰81.9万円｜⚠日程不明
- 8035 東京エレクトロン｜ai_reversal｜業績 🔥絶好調｜値頃 💎割安｜FAIL_INSEN｜終値8657.0｜💰94.6万円｜⚠日程不明
- 6918 アバールデータ｜ai_reversal｜業績 🔥絶好調｜値頃 💎割安｜PASS｜終値2780.0｜💰27.8万円｜reversal 2780 SL2700・✅即時可｜⚠日程不明 🤖AI特需 🔬基板・素材/装置・商社 📐進捗 遅れ -17.0%
  > 📌【業態】半導体製造装置の制御組込を受託。自社製品も。画像・計測・通信が主力。
  > 📌【いま】終値2,780円・直近5日-12.58%（材料未確認）
  > 📌【調子】🔥絶好調（10/13）— 突出ボーナス・⚠進捗遅れ・⚠下期依存
  > 📌【水準】💎割安（6.0/7）— PER8.54倍・PEG0.064・52週12.3% ／ 💰単元27.8万円
  > 📌【戦略】当日終値2780円の指値で反転を取りにいく。SL2700円（直近5日安値）
- 6524 湖北工業｜ai_reversal｜業績 🔥絶好調｜値頃 🟢値頃｜FAIL_INSEN｜終値4130.0｜💰44.9万円｜⚠日程不明
- 3110 日東紡｜ai_reversal｜業績 🔥絶好調｜値頃 💎割安｜FAIL_INSEN｜終値2375.0｜💰26.5万円｜⚠日程不明
- 4368 扶桑化学工業｜ai_reversal｜業績 🔥絶好調｜値頃 💎割安｜PASS｜終値2690.0｜💰26.9万円｜reversal 2690 SL2584・✅即時可｜⚠日程不明 signals不明→リバ系
  > 📌【業態】果実酸類大手。リンゴ酸で世界高シェア。電子材料ではウエハ研磨剤原料に強み。
  > 📌【いま】終値2,690円・直近5日-8.69%（材料未確認）
  > 📌【調子】🔥絶好調（9/13）— 上方修正済み
  > 📌【水準】💎割安（6.0/7）— PER13倍・PEG0.298・52週27.2% ／ 💰単元26.9万円
  > 📌【戦略】当日終値2690円の指値で反転を取りにいく。SL2584円（直近5日安値）
- 2760 東京エレクトロンデバイス｜ai_reversal｜業績 🔥絶好調｜値頃 🟢値頃｜PASS｜終値3825.0｜💰38.2万円｜reversal 3825 SL3700・✅即時可｜⚠日程不明 🤖AI特需 🔬基板・素材/装置・商社
  > 📌【業態】電子部品の半導体商社。主に米国製を扱う。設計受託で産業用に強み。
  > 📌【いま】終値3,825円・直近5日+0.92%（材料未確認）
  > 📌【調子】🔥絶好調（9/13）— ⚠下期依存
  > 📌【水準】🟢値頃（5.0/7）— PER10.21倍・PEG0.159・52週41.4% ／ 💰単元38.2万円
  > 📌【戦略】当日終値3825円の指値で反転を取りにいく。SL3700円（直近5日安値）
- 4971 メック｜ai_reversal｜業績 🔥絶好調｜値頃 🟢値頃｜FAIL_UWAHIGE｜終値5000.0｜💰53.1万円｜⚠日程不明
- 6235 オプトラン｜ai_reversal｜業績 🔥絶好調｜値頃 🟢値頃｜FAIL_INSEN｜終値2057.0｜💰22.7万円｜⚠日程不明
- 6323 ローツェ｜ai_reversal｜業績 🔥絶好調｜値頃 🟢値頃｜FAIL_UWAHIGE｜終値3047.0｜💰32.5万円｜⚠日程不明
- 6762 TDK｜ai_reversal｜業績 🔥絶好調｜値頃 🟢値頃｜FAIL_UWAHIGE｜終値2190.5｜💰23.1万円｜⚠日程不明
- 7729 東京精密｜ai_reversal｜業績 🔥絶好調｜値頃 🟢値頃｜FAIL_UWAHIGE｜終値11905.0｜💰131.5万円｜⚠日程不明 🤖AI特需 🔬基板・素材/装置・商社
- 7735 SCREENホールディングス｜ai_reversal｜業績 🔥絶好調｜値頃 💎割安｜FAIL_INSEN｜終値7768.0｜💰85.6万円｜⚠日程不明
- 1961 三機工業｜ai_reversal｜業績 🔥絶好調｜値頃 💎割安｜FAIL_INSEN｜終値2398.0｜💰25.3万円｜⚠日程不明
- 5384 フジミインコーポレーテッド｜ai_reversal｜業績 🔥絶好調｜値頃 💎割安｜PASS｜終値2775.0｜💰27.8万円｜reversal 2775 SL2699・✅即時可｜⚠日程不明 signals不明→リバ系 📐進捗 上振れ 20.0%
  > 📌【業態】半導体ウエハー用研磨材で世界首位。溶射技術にも強み。CMP製品が成長。
  > 📌【いま】終値2,775円・直近5日-4.67%（材料未確認）
  > 📌【調子】🔥絶好調（8/13）— 🔼加速・🔼進捗先行
  > 📌【水準】💎割安（6.0/7）— PER15.91倍・PEG0.677・52週19.6% ／ 💰単元27.8万円
  > 📌【戦略】当日終値2775円の指値で反転を取りにいく。SL2699円（直近5日安値）
- 6941 山一電機｜ai_reversal｜業績 🔥絶好調｜値頃 💎割安｜FAIL_INSEN｜終値6290.0｜💰66.1万円｜⚠日程不明
- 6227 AIメカテック｜ai_reversal｜業績 🔥絶好調｜値頃 ⚪妥当｜FAIL_INSEN｜終値4535.0｜💰48.0万円｜⚠日程不明 📑TOPIX新規採用（2026-10-30 組入） 🤖AI特需 🔬基板・素材/装置・商社
- 3436 SUMCO｜ai_reversal｜業績 ⚡好調｜値頃 💎割安｜FAIL_UWAHIGE｜終値1957.0｜💰21.1万円｜⚠日程不明
- 6336 石井表記｜ai_reversal/granville_rebound｜業績 ⚡好調｜値頃 💎割安｜PASS｜終値1164.0｜💰11.6万円｜reversal 1164 SL1125・✅即時可｜📋カルテ窓 12/11(残17営業日) signals不明→リバ系
  > 📌【業態】プリント基板製造装置の大手。ディスプレイ用インクジェット塗布機、印刷技術にも力。
  > 📌【いま】終値1,164円・直近5日-4.59%（材料未確認）
  > 📌【調子】⚡好調（6/13）
  > 📌【水準】💎割安（7.0/7）— PER8.7倍・PEG0.336・52週32% ／ 💰単元11.6万円
  > 📌【戦略】当日終値1164円の指値で反転を取りにいく。SL1125円（直近5日安値）
- 6971 京セラ｜ai_reversal｜業績 ⚡好調｜値頃 ⚪妥当｜FAIL_UWAHIGE｜終値2857.0｜💰29.8万円｜⚠日程不明 🤖AI特需 🏢大型・指数寄与/素材部品
- 4022 ラサ工業｜ai_reversal｜業績 ⚡好調｜値頃 💎割安｜FAIL_INSEN｜終値1216.0｜💰13.2万円｜⚠日程不明
- 4973 JCU｜ai_reversal｜業績 ⚡好調｜値頃 ⚪妥当｜PASS｜終値3890.0｜💰38.9万円｜⛔提案なし(指名鮮度切れ 11営業日)｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8） signals不明→リバ系
  > 📌【業態】メッキ用薬品の開発・販売。電子基板向けが主力。実装品向けも。ファブレス企業。
  > 📌【いま】終値3,890円・直近5日-3.83%（材料未確認）
  > 📌【調子】⚡好調（5/13）— E軸判定不能(進捗データ不足)・質注意
  > 📌【水準】⚪妥当（3.0/7）— PER10.42倍・PEG3.37・52週22.7% ／ 💰単元38.9万円
  > 📌【戦略】発注対象外（⛔提案なし(指名鮮度切れ 11営業日)）
- 6590 芝浦メカトロニクス｜ai_reversal｜業績 ✅順調｜値頃 🟢値頃｜FAIL_UWAHIGE｜終値2640.0｜💰29.2万円｜⚠日程不明
- 255A GLテクノHD｜ai_reversal｜業績 ✅順調｜値頃 ⚪妥当｜FAIL_INSEN｜終値3730.0｜💰41.2万円｜⚠日程不明
- 5706 三井金属鉱業｜ai_reversal｜業績 🔻悪化｜値頃 ⚪妥当｜FAIL_INSEN｜終値1344.5｜💰15.4万円｜⚠日程不明
- 6965 浜松ホトニクス｜ai_reversal｜業績 ✅順調｜値頃 🔴過熱｜FAIL_INSEN｜終値2015.5｜💰21.8万円｜⚠日程不明
- 6643 戸上電機製作所｜ai_reversal｜業績 ✅順調｜値頃 ⚪妥当｜FAIL_INSEN｜終値4595.0｜💰44.0万円｜⚠日程不明 🤖AI特需 📡エネマネ・計量/中流
- 6501 日立製作所｜ai_reversal｜業績 ✅順調｜値頃 🟡やや割高｜FAIL_INSEN｜終値4811.0｜💰49.6万円｜⚠日程不明
- 2802 味の素｜ai_reversal｜業績 ➖横ばい｜値頃 ⚪妥当｜PASS｜終値4155.0｜💰41.5万円｜reversal 4155 SL4018・✅即時可｜⚠日程不明 🤖AI特需 🔬基板・素材/中流
  > 📌【業態】総合食品会社で調味料首位。冷凍食、医薬品、飼料や電子材など多角展開。
  > 📌【いま】終値4,155円・直近5日-4.37%（材料未確認）
  > 📌【調子】➖横ばい（2/13）— 税引前代替・経常非開示(IFRS等)のため最終益成長率で代替・質注意・E軸判定不能(進捗データ不足)
  > 📌【水準】⚪妥当（4.0/7）— PER29.24倍・PEG—・52週28.8% ／ 💰単元41.5万円
  > 📌【戦略】当日終値4155円の指値で反転を取りにいく。SL4018円（直近5日安値）
- 9503 関西電力｜ai_reversal｜業績 🔻悪化｜値頃 🟡やや割高｜FAIL_INSEN｜終値2693.5｜💰27.3万円｜⚠日程不明
- 1982 日比谷総合設備｜ai_reversal｜業績 ➖横ばい｜値頃 🔴過熱｜FAIL_INSEN｜終値3020.0｜💰31.6万円｜⚠日程不明
- 6617 東光高岳｜ai_reversal｜業績 ⚠減速｜値頃 ⚪妥当｜FAIL_INSEN｜終値4660.0｜💰50.1万円｜⚠日程不明
- 9432 NTT｜ai_reversal｜業績 ⚠減速｜値頃 🟡やや割高｜FAIL_INSEN｜終値169.89999389648438｜💰1.7万円｜⚠日程不明
- 4203 住友ベークライト｜ai_reversal/granville_rebound｜業績 業績データ取得不可｜値頃 ⚪妥当｜FAIL_UWAHIGE｜終値6878.0｜💰72.8万円｜⚠日程不明
- 4182 三菱ガス化学｜ai_reversal｜業績 —｜値頃 —｜FAIL_UWAHIGE｜終値3130.0｜💰—｜⚠日程不明 🤖AI特需 🔬基板・素材/上流
- 6146 ディスコ｜ai_reversal｜業績 取得不可｜値頃 取得不可｜FAIL_UWAHIGE｜終値43390.0｜💰475.8万円｜⚠日程不明
- 6723 ルネサスエレクトロニクス｜ai_reversal｜業績 取得不可｜値頃 取得不可｜FAIL_INSEN｜終値2618.5｜💰29.2万円｜⚠日程不明
- 9984 ソフトバンクグループ｜ai_reversal｜業績 業績データ取得不可(経常益予想非開示)｜値頃 取得不可｜FAIL_INSEN｜終値3281.0｜💰38.5万円｜⚠日程不明

## ⚡材料後出し
その日の足は開示前の情報。判定は参考値
- 262A INTERMESTIC INC.｜FAIL_INSEN｜📌 Notice Concerning Change in Controlling Shareholder (Excluding the Parent Company) and Major Shareholder｜11-17 15:30
- 3798 ULS Group Incorporated｜FAIL_INSEN｜📌 ULSコンサルティング、日本IBMとパートナーシップを締結、AIエージェント駆動の開発支援パートナー「IBM Bob」を活用したモダナイゼーション支援を開始｜11-17 15:30
- 446A ノースサンド｜FAIL_INSEN｜📌 Notice Concerning Determination of Selling Price and Other Terms｜11-17 17:00
- 7148 Financial Products Group Co., Ltd.｜FAIL_INSEN｜📌 Notice Regarding Partial Amendment to Articles of Incorporation｜11-17 16:30
- 4534 Mochida Pharmaceutical Co., Ltd.｜FAIL_INSEN｜📌 静岡県藤枝市との女性の健康増進と活躍促進に関する連携協定締結のお知らせ｜11-17 15:00
- 5532 リアルゲイト｜FAIL_INSEN｜📌 定款の一部変更に関するお知らせ｜11-17 15:30
- 8016 オンワード HD｜FAIL_INSEN｜📌 株式の取得（完全子会社化）に関するお知らせ｜11-17 15:30
- 4169 Enechange Ltd.｜FAIL_INSEN｜📌 ラジオNIKKEI「マーケット・テラス」～櫻井英明が迫る、経営トップの素顔～ に当社代表取締役CEO 丸岡がゲスト出演しました｜11-17 15:30
- 9513 Electric Power Development Co., Ltd.｜FAIL_INSEN｜📌 Notice Regarding a Partial Correction to the English Version of the Financial Results for the Year Ended March 31, 2026｜11-17 17:00
- 479A PRONI Inc.｜FAIL_INSEN｜📌 2026年12月期第３四半期決算説明会「ログミーFinance 書き起こし」公開のお知らせ｜11-17 17:30
- 4100 Toda Kogyo Corp.｜FAIL_UWAHIGE｜📌 Corporate Governance Report｜11-17 15:00
- 9278 BOOKOFF GROUP HOLDINGS LIMITED｜FAIL_INSEN｜📌 Notice Regarding Change in Subsidiaries (Change in Amount of Investment and Commencement of Business)｜11-17 18:00
- 6676 BUFFALO INC.｜PASS｜📌 [Delayed]Consolidated Financial Results for the Six Months Ended September 30, 2026｜11-17 15:40
- 4884 Kringle Pharma, Inc.｜PASS｜📌 2026年9月期 通期決算説明会 質疑応答について｜11-17 17:30
- 3691 DIGITAL PLUS, Inc.｜FAIL_INSEN｜📌 ADワークスグループが株主優待としてデジタルギフトを採用｜11-17 15:30
- 593A Tier IV, Inc.｜FAIL_INSEN｜📌 2026年９月期通期決算説明会　動画及び書き起こし公開に関するお知らせ｜11-17 16:00
- 218A Liberaware｜FAIL_INSEN｜📌 Entry into High-Performance Battery Business for Domestic UAS and Plans to Conclude a JV Agreement and Establish a JV Materials｜11-17 17:01

## 📢開示
使用した一覧: https://kabutan.jp/disclosures/?date=20261116 （1〜1頁） ＋ https://kabutan.jp/disclosures/?date=20261117 （1〜27頁）・取得417件（11/16 は 20:30 以降のみ採用）。見出しをそのまま転記（解釈なし）。フォールバック: なし。①-9へ引き渡し0件（📢/📉/📊 の該当なし）
- 👥 262A インターメス｜親会社以外の支配株主及び主要株主の異動に関するお知らせ｜11-17 15:30
- 📌 167A リョー菱ＨＤ｜リョーサン菱洋、北九州市主催の「北九州フィジカルAIハッカソン2026」に協賛｜11-17 11:00
- 📌 218A リベラウェア｜Entry into High-Performance Battery Business for Domestic UAS and Plans to Conclude a JV Agreement and Establish a JV Materials｜11-17 17:01
- 📌 218A リベラウェア｜Notice Regarding Entry into High-Performance Battery Business for Domestic UAS and Plans to Conclude a JV Agreement and Establish a JV｜11-17 17:01
- 📌 218A リベラウェア｜国産無人機向け高性能バッテリー事業への参入、合弁契約締結方針及び合弁会社設立に関する補足資料｜11-17 17:00
- 📌 218A リベラウェア｜国産無人機向け高性能バッテリー事業への参入、合弁契約締結方針及び合弁会社設立に関するお知らせ｜11-17 17:00
- 📌 262A インターメス｜Notice Concerning Change in Controlling Shareholder (Excluding the Parent Company) and Major Shareholder｜11-17 15:30
- 📌 3042 セキュアヴェ｜SecuAvail’s Next-Generation SOC Service “AI-SOC” Now Supports SonicWall TZ Series｜11-17 09:00
- 📌 3042 セキュアヴェ｜セキュアヴェイルの次世代SOCサービス『AI-SOC』がSonicWall TZシリ ーズに対応｜11-17 09:00
- 📌 336A ダイナマップ｜ダイナミックマッププラットフォーム、国土交通省「港湾技術開発制度」に採択｜11-17 08:30
- 📌 3498 霞ヶ関Ｃ｜Supplementary Explanation Regarding Proposal No. 5 at the 15th Annual General Meeting of Shareholders｜11-17 08:00
- 📌 3498 霞ヶ関Ｃ｜第15期定時株主総会第5号議案に関する補足説明について｜11-17 08:00
- 📌 3691 デジプラ｜ADワークスグループが株主優待としてデジタルギフトを採用｜11-17 15:30
- 📌 3691 デジプラ｜ディスラプターズが「シェア型株主優待」としてデジタルギフトを採用｜11-17 12:00
- 📌 3798 ＵＬＳグルプ｜ULSコンサルティング、日本IBMとパートナーシップを締結、AIエージェント駆動の開発支援パートナー「IBM Bob」を活用したモダナイゼーション支援を開始｜11-17 15:30
- 📌 3909 ショーケース｜個人情報を外部送信しない「ProTech ID Checker」 Windows 版の提供を開始｜11-17 11:00
- 📌 3968 セグエＧ｜ジェイズ・テクノロジーが株式会社JTBの新オフィス移転に伴う大規模ネットワーク基盤の刷新を支援した導入事例を公開｜11-17 11:00
- 📌 4028 石原産｜Integrated Report 2026｜11-17 00:30
- 📌 4028 石原産｜統合報告書2026｜11-17 00:30
- 📌 4047 関電化｜統合報告書 2026｜11-17 00:30
- 📌 4100 戸田工｜Corporate Governance Report｜11-17 15:00
- 📌 4169 エネチェンジ｜ラジオNIKKEI「マーケット・テラス」～櫻井英明が迫る、経営トップの素顔～ に当社代表取締役CEO 丸岡がゲスト出演しました｜11-17 15:30
- 📌 4249 森六｜2027年3月期第２四半期 決算説明会資料｜11-17 12:00
- 📌 4443 Ｓａｎｓａｎ｜Sansan, Inc. Releases ANNUAL REPORT 2026｜11-17 00:30
- 📌 4443 Ｓａｎｓａｎ｜統合報告書 2026 の発行に関するお知らせ｜11-17 00:30
- 📌 446A ノースサンド｜Notice Concerning Determination of Selling Price and Other Terms｜11-17 17:00
- 📌 446A ノースサンド｜売出価格等の決定に関するお知らせ｜11-17 17:00
- 📌 4534 持田薬｜静岡県藤枝市との女性の健康増進と活躍促進に関する連携協定締結のお知らせ｜11-17 15:00
- 📌 4765 ＳＢＩＧＡＭ｜SBIアセットマネジメント運用の日本株トークン化商品、世界3拠点目へ グローバル暗号資産取引所Bybitで取扱開始｜11-17 08:45
- 📌 479A ＰＲＯＮＩ｜2026年12月期第３四半期決算説明会「ログミーFinance 書き起こし」公開のお知らせ｜11-17 17:30
- 📌 4884 クリングル｜2026年9月期 通期決算説明会 質疑応答について｜11-17 17:30
- 📌 5532 リアルゲイト｜定款の一部変更に関するお知らせ｜11-17 15:30
- 📌 593A ティアフォー｜2026年９月期通期決算説明会　動画及び書き起こし公開に関するお知らせ｜11-17 16:00
- 📌 6332 月島ＨＤ｜コーポレート・ガバナンスに関する報告書 2026/11/17｜11-17 13:57
- 📌 6508 明電舎｜法定事前開示書類（吸収分割）（明電ファシリティサービス株式会社）｜11-17 12:00
- 📌 6676 ＢＵＦ｜[Delayed]Consolidated Financial Results for the Six Months Ended September 30, 2026｜11-17 15:40
- 📌 6850 チノー｜Supplementary Materials for FY2026 2Q Financial Results｜11-17 10:00
- 📌 6850 チノー｜2027年3月期 第2四半期 決算補足説明資料｜11-17 10:00
- 📌 7148 ＦＰＧ｜Notice Regarding Partial Amendment to Articles of Incorporation｜11-17 16:30
- 📌 7148 ＦＰＧ｜定款の一部変更に関するお知らせ｜11-17 16:30
- 📌 7921 宝＆ＣＯ｜WizLaboと連結会計システム「Consoleasy」がAPI連携開始｜11-17 14:00
- 📌 8016 オンワード｜株式の取得（完全子会社化）に関するお知らせ｜11-17 15:30
- 📌 8016 オンワード｜Notice Regarding the Acquisition of Shares (Conversion into a Wholly Owned Subsidiary)｜11-17 15:30
- 📌 8739 スパークス｜Renewable Energy Aggregation Service Agreement Signed for the Existing Onshore Wind Farm｜11-17 13:00
- 📌 8739 スパークス｜既設陸上風力発電所の再エネアグリゲーションサービス契約を締結｜11-17 13:00
- 📌 9278 ブックオフＧ｜Notice Regarding Change in Subsidiaries (Change in Amount of Investment and Commencement of Business)｜11-17 18:00
- 📌 9278 ブックオフＧ｜子会社等の異動（出資額の変更及び事業開始）に関するお知らせ｜11-17 18:00
- 📌 9513 Ｊパワー｜Notice Regarding a Partial Correction to the English Version of the Financial Results for the Year Ended March 31, 2026｜11-17 17:00

## 総当りゲート
### 5手法（246件）
- PASS 37: 167A 2760 2802 3843 4021 4028 4205 4216 4368 4403 4933 4973 5101 5136 5186 5384 5444 558A 5821 6336 6532 6588 6632 6750 6754 6804 6807 6875 6918 6925 6952 6969 7366 7433 8359 8698 8975
- FAIL_UWAHIGE 49: 2109 268A 3105 3374 3436 3932 4063 4088 4182 4203 4206 4272 4434 4471 4634 4902 4966 4971 5301 5310 5344 5537 6146 6238 6323 6370 6418 6436 6454 6516 6590 6652 6668 6758 6762 6787 6810 6850 6971 7729 7731 7747 8253 9107 9110 9204 9301 9554 9934
- FAIL_INSEN 160: 1435 147A 1663 1721 1926 1951 1960 1961 1963 1975 1979 1980 1982 2331 255A 262A 2975 3036 3091 3110 3116 3131 3205 3445 3479 3498 3556 3569 3612 3798 3915 3994 4008 4022 4042 4047 4053 4176 4180 4249 4286 4293 4377 4379 4410 4417 446A 4503 4743 4746 4768 4771 4980 5018 5019 5021 5137 5201 5246 5331 5333 5463 5602 5703 5706 5711 5801 5831 5832 6016 6036 6055 6071 6135 6167 618A 6227 6235 6250 6268 6277 6278 6324 6332 6340 6349 6367 6368 6379 6407 6448 6471 6473 6479 6481 6501 6524 6613 6617 6643 6645 6651 6674 6723 6724 6741 6777 6845 6923 6941 6943 6965 6988 7004 7148 7167 7177 7186 7220 7276 7278 7322 7381 7637 7733 7735 7942 7995 8032 8035 8084 8133 8154 8304 8334 8354 8366 8370 8386 8393 8508 8524 8600 8616 8704 9037 9048 9072 9302 9308 9432 9434 9468 9503 9722 9766 9902 9960 9962 9984
### グランビル（198件）
- PASS 20: 2384 2489 3092 3850 456A 4884 4922 5105 5256 6027 6328 6412 6676 6877 7256 7480 7609 7970 8551 8739
- PASS_DOJI 11: 3851 3858 3964 4258 4398 4968 5367 5599 6508 6768 8344
- FAIL_UWAHIGE 29: 150A 153A 2267 278A 3106 3156 3673 3692 3762 3891 3909 4025 4100 436A 4498 4543 4848 4912 5381 6191 6570 6742 6744 6862 6890 7213 8137 8159 8160
- FAIL_INSEN 138: 1436 1878 1911 1928 1941 2206 2488 2492 2502 2811 2897 2962 3002 3040 3042 3182 336A 3371 338A 3401 3405 3491 3496 3547 3549 3563 3565 3691 3697 3763 3793 3927 3968 4005 4040 4045 4075 4169 417A 4204 4240 428A 4373 4375 4396 4401 4419 4431 4432 4443 4475 4507 4523 4528 4534 4540 4549 4552 4554 4568 460A 4667 4674 4686 4765 477A 479A 5033 5036 5184 5233 5252 5532 5892 5930 5985 6080 6099 6138 6203 6317 6490 6574 6745 6840 6904 6947 6958 7175 7184 7269 7380 7606 7713 7715 7826 7921 8012 8016 8051 8056 8113 8167 8360 8364 8368 8377 8388 8392 8395 8410 8609 8801 8803 8804 9006 9025 9045 9065 9075 9163 9278 9304 9401 9404 9418 9509 9513 9536 9552 9605 9697 9735 9742 9837 9842 9869 9956
### 変化点（16件）
- PASS 1: 3989
- FAIL_UWAHIGE 2: 4478 7695
- FAIL_INSEN 13: 218A 265A 286A 3923 4011 4165 4259 4483 4488 5803 593A 8151 9343
除籍（first_seenから30暦日超）: 0件

## 機械詳細
- 候補収集: 当夜候補100銘柄（新規25・再指名75）・未マージPR由来0・熟成トリガー0・除籍0・dm_*/an_* はspec未定義のため不使用
- 日足取得: 461本（プール460＋1306）・失敗0・ステイル0
- ゲート: PASS58・PASS_DOJI11・FAIL_UWAHIGE80・FAIL_INSEN311・SKIP0・log追記1件（2026-11-17）
- 通知の抜粋: 10件（method3/ai3/granville3/changepoint1/不明0）
- ヘッドライン付与: PASS69件中69件（業態キャッシュヒット65／新規取得3／未取得1）
- kabutan 新規取得: 4/50件（業態・業種 3件取得・1件（3480 業種埋め戻し）取得不可）・打ち切り0
- profile_cache: 総数1069・本夜追加3件・業種埋め戻し0件（残り1件）
- gate_history: gate_history/2026-11-17.json を新規作成（verdicts 460件＝評価件数・nominations 100件（新規25・再指名75））
- 業種 付与済み434/未付与26
- grades.json: 1109銘柄/619.8KiB（浮動小数は4桁丸め）・業種別PER中央値 26業種・spm を写せた銘柄1025件
- method_score: 保持73件／null387件
- earnings_log: 総数504／本夜追記0件／リターン補完53件／日足が無く未補完146件・gyoseki history 退避0件（業績再計算なし）
- pool_bars.json: 461銘柄/393.2KiB
- 鮮度ゲート: 鮮度切れ除外14件・nom_age分布 0-2:164/3-10:189/11+:107・last_seen欠損0件
- トレンド文脈: ctx 合致101／不一致214／レンジ144／判定不能1・PASSのうち ctx合致14件・形態が付いた銘柄245件
- 3日ルール: 判定0銘柄・streak≥3 0・streak=2 0・判定不可0（保有0）
- 開示の分類別件数: 📢0・📉0・📊0・🔁0・👥1・🏛0・📦0・📌47
- 熟成由来の候補 0件
- 権利情報: rights_cache 総数503・本夜 配当更新0件／優待取得0件（T+1/T+2 に権利落ち無し・保有0）
- 次回決算日: 付与212件／未発表897件・前年同期発表日 付与371件・earnings_calendar.json 1126銘柄/140KiB
- 業績グレード再計算: 未実施（キャッシュ値使用）・recalc_queue 新規0件（総数12）
- 値頃感: PASS/PASS_DOJI 68銘柄を当日終値で再計算（static 無し1件は未評価）
- STEP 4.8: スキップ（week_open=false）
- master.json 変更行数: +10294/-8270（W=2）
