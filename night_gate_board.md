# 夜間ゲート 2026-11-18

## サマリー
- 評価数: 476 / PASS: 55（PASS_DOJI 9件を含む）
- 発注可能提案数: 32件（✅22／⏳5／⏸位置不適4／⏸トラップ疑い1）
- 市場一言: 市場モード「レンジ様子見」（market.latest 2026-11-18）。プール476銘柄中 PASS比率11.6%（陰線FAIL 365件・上髭FAIL 56件）
- 実行モード: 通常（base_day=当日の引け値を対象。11/18(水)=営業日・翌11/19(木)=営業日）
- base_day: 2026-11-18（run_at 2026-11-18T20:31:00+09:00）
- week_open: false（翌営業日 11/19(木)＝週中）→ STEP 4.8 はスキップ
- 📆 翌営業日 11/19: カレンダーイベントなし（T+2 11/20: 連休前最終営業日（次の営業日 11/24(火)））
- 📑指数: 低減対象 提案3件／PASS5件／プール77件・新規採用 9件（index_flags 2026-10-07 公表分）・次の TOPIX 低減日 01/29 第2回/8（あと48営業日）

## 検証結果
- V1 → はい（提案32=results32=模擬32=通知母数32）
- V2 → はい（PASS55=提案32+除外23・order_status欠落0）
- V3 → はい（results476件重複0）
- V4 → はい（既存static変更0）
- V5 → はい（変更トップキー['earnings_log', 'gyoseki_cache', 'night_gate', 'pipeline', 'profile_cache']・pipeline他run不変True・spec不変True・profile既存書換なしTrue）
- V6 → はい（gyoseki_cache不整合0）
- V7 → はい（必須セクション存在・week_open=false のため📅今週のカタリストは対象外）
- V8 → はい（模擬32行 不正0）
- V9 → はい（gate_history と today 一致）
- V10 → はい（base_day一致 2026-11-18）
- V11 → いいえ（+12065/-11538（indent=2・往復一致で検出・仮ファイル経由））
- V12 → はい（並び順 (a)True(b)True(c)True）
- V13 → はい（1125銘柄/647.8KB・GC∪VC∪PC1125全収録True・20キーTrue・型True・nx一致True・ix非null229・業種PER中央値26業種True・pg範囲外0）
- V14 → はい（保持81件/null395件・出所不明0・写し一致=True・内訳{'kenmo_momentum': 13, 'stf_kakuhen': 25, 'granville_rebound': 2, 'choruko_reversal': 20, 'ai_reversal': 19, 'granville_tenkan': 1, 'granville_oshime': 1}）
- V15 → はい（PASS55件中55件に付与（欠落0）・5キーTrue・(c)未取得/取得不可1（キャッシュのグレード名転記を含む））
- V16 → はい（📊2件→earnings_log 追記2件・grade_beforeは再計算前（本夜は業績再計算なし）・history>4=0・総数506）
- V17 → はい（477銘柄/406.7KB・先読み0=True・保有0銘柄（収録対象なし）・3日ルール判定0銘柄）
- V18 → はい（鮮度切れ12件・誤除外0=True・nom_age分布 0-2:168/3-10:187/11+:121・欠損99=0）
- V19 → はい（verdicts476=評価476・nominations106（新規16/再指名90）・集合一致True・ctx判定不能2・(d)True・(e)True）
- V20 → はい（1130銘柄・nx非null213・hist持ち788・pxd376・取得元名称なしTrue・(c)True・(d)True）
- V21 → はい（recent_pass511銘柄・当夜提案全収録True・保有情報不使用True（保有0銘柄））
- V22 → はい（PASS_DOJI9・⏸位置不適4誤通過0=True・⏸トラップ1=True・rs20付与476/476・RSチップ整合True）
- VLEAK → はい（公開物（ボード/today/gate_history）への保有情報 検出0件（保有0銘柄））
- 注: V11 は night_gate.results の全置換（476件×約50行）と pool・log の更新による実変更行数であり、インデント幅は往復一致で検出した W=2 を維持（全体再フォーマットではない）

## 保有アラート
- 保有0銘柄・アラート0件（詳細は通知）

## 🧾直近提案の決算接近
- 窓内（直近20営業日）の提案銘柄 511・日程不明 439（🚨1／📉0／⏰0／📋25・当夜評価外150）。保有情報は使っていない（候補だった銘柄の日程）
- 🚨決算直前 11/19(残1営業日) 8986 Daiwa Securities Living Investment Corporation｜最後の提案 10/26（reversal 83900・✅即時可）｜当夜 評価外
- 📋カルテ窓 12/04(残11営業日) 436A サイバーソリューションズ（サイバＳＯＬ）｜最後の提案 11/18（oshime 1737・⏸位置不適(25日線 下向き -2.92%)）｜当夜 PASS
- 📋カルテ窓 12/15(残18営業日) 5136 tripla Co.,Ltd.｜最後の提案 11/17（momentum 2730・✅即時可）｜当夜 FAIL_INSEN
- 📋カルテ窓 12/11(残16営業日) 6336 石井表記｜最後の提案 11/17（reversal 1164・✅即時可）｜当夜 FAIL_UWAHIGE
- 📋カルテ窓 12/11(残16営業日) 446A ノースサンド｜最後の提案 11/16（momentum 2631・⏸位置不適(25MA下 -2.7%)）｜当夜 FAIL_INSEN
- 📋カルテ窓 12/16(残19営業日) 8975 Ichigo Office REIT Investment Corporation｜最後の提案 11/16（reversal 88800・✅即時可）｜当夜 FAIL_INSEN
- 📋カルテ窓 12/09(残14営業日) 7678 ASAKUMA CO.,LTD.｜最後の提案 11/13（momentum 4450・✅即時可）｜当夜 FAIL_INSEN
- 📋カルテ窓 12/15(残18営業日) 3565 Ascentech KK｜最後の提案 11/12（reversal 453・✅即時可）｜当夜 FAIL_INSEN
- 📋カルテ窓 12/11(残16営業日) 218A Liberaware｜最後の提案 11/11（changepoint 830・✅即時可）｜当夜 FAIL_INSEN
- 📋カルテ窓 12/10(残15営業日) 3491 ＧＡ　ｔｅｃｈｎｏｌｏｇｉｅｓ（ＧＡテクノ）｜最後の提案 11/11（momentum 1568・✅即時可）｜当夜 FAIL_INSEN
- 📋カルテ窓 12/14(残17営業日) 460A ＢＲＡＮＵ｜最後の提案 11/11（reversal 1098・✅即時可）｜当夜 FAIL_UWAHIGE
- 📋カルテ窓 12/08(残13営業日) 9824 泉州電業｜最後の提案 11/11（momentum 7880・⏸位置不適(25MA下 -2.36%)）｜当夜 PASS
- 📋カルテ窓 12/08(残13営業日) 1436 GreenEnergy & Company｜最後の提案 11/10（reversal 1368・✅即時可）｜当夜 FAIL_INSEN
- 📋カルテ窓 12/10(残15営業日) 1928 積水ハウス｜最後の提案 11/09（momentum 3568・✅即時可）｜当夜 FAIL_INSEN
- 📋カルテ窓 12/11(残16営業日) 4075 ブレインズテクノロジー｜最後の提案 11/09（reversal 1037・✅即時可）｜当夜 FAIL_UWAHIGE
- 📋カルテ窓 12/09(残14営業日) 5132 pluszero,Inc.｜最後の提案 11/04（momentum 1761・✅即時可）｜当夜 評価外
- 📋カルテ窓 12/15(残18営業日) 9163 Nareru Group Inc.｜最後の提案 11/04（momentum 2088・✅即時可）｜当夜 FAIL_INSEN
- 📋カルテ窓 12/11(残16営業日) 3653 Morpho, Inc.｜最後の提案 10/29（reversal 918・✅即時可）｜当夜 評価外
- 📋カルテ窓 12/10(残15営業日) 8927 Meiho Enterprise Co., Ltd.｜最後の提案 10/29（momentum 466・✅即時可）｜当夜 評価外
- 📋カルテ窓 12/15(残18営業日) 4431 スマレジ｜最後の提案 10/28（oshime 3707.6・✅即時可）｜当夜 FAIL_INSEN
- 📋カルテ窓 12/11(残16営業日) 186A Astroscale Holdings Inc.｜最後の提案 10/27（momentum 1084・✅即時可）｜当夜 評価外
- 📋カルテ窓 12/15(残18営業日) 212A FIT EASY Inc.｜最後の提案 10/27（momentum 2771・✅即時可）｜当夜 評価外
- 📋カルテ窓 12/11(残16営業日) 456A Human Made Inc.｜最後の提案 10/27（oshime 1940・✅即時可）｜当夜 FAIL_INSEN
- 📋カルテ窓 12/15(残18営業日) 4666 Park24 Co., Ltd.｜最後の提案 10/26（reversal 1850・✅即時可）｜当夜 評価外
- 📋カルテ窓 12/11(残16営業日) 4382 HEROZ, Inc.｜最後の提案 10/21（changepoint 1631・✅即時可）｜当夜 評価外
- 📋カルテ窓 12/14(残17営業日) 9166 GENDA Inc.｜最後の提案 10/21（oshime 673.5・✅即時可）｜当夜 評価外

## 前夜の結果
- PL5口座への正式な反映は週次①-11の採点で行われる。ここは参考情報
- 前夜 2026-11-17 の提案41件 → 約定33・不約定8・判定不能0（判定日 11/18）
- 5136 momentum 注文2730/上限2757.3｜始2710 高2720 安2527 終2663｜不約定
- 5821 momentum 注文3195/上限3226.9｜始3230 高3280 安3075 終3155｜不約定
- 558A momentum 注文6200/上限6262｜始6100 高6180 安5920 終6180｜不約定
- 4933 momentum 注文2501/上限2526｜始2489 高2529 安2472 終2501｜約定 @2501（終値比 +0.00%）
- 7433 reversal 注文1531｜始1571 高1571 安1517 終1549｜約定 @1531（終値比 +1.18%）
- 4216 reversal 注文5500｜始5580 高5680 安5360 終5560｜約定 @5500（終値比 +1.09%）
- 167A reversal 注文3085｜始3120 高3125 安3050 終3080｜約定 @3085（終値比 -0.16%）
- 6588 reversal 注文2468｜始2450 高2473 安2381 終2437｜約定 @2450（終値比 -0.53%）
- 6952 reversal 注文2028.5｜始2029 高2038.5 安1990.5 終2026｜約定 @2028.5（終値比 -0.12%）
- 6754 reversal 注文2245｜始2345 高2346 安2180 終2262｜約定 @2245（終値比 +0.76%）
- 5186 reversal 注文6140｜始6170 高6180 安6020 終6100｜約定 @6140（終値比 -0.65%）
- 4205 reversal 注文2018.5｜始2053.5 高2053.5 安1986 終2009｜約定 @2018.5（終値比 -0.47%）
- 5444 reversal 注文10865｜始10920 高10970 安10785 終10880｜約定 @10865（終値比 +0.14%）
- 4403 reversal 注文2627｜始2606 高2620.5 安2541.5 終2551｜約定 @2606（終値比 -2.11%）
- 4021 reversal 注文6669｜始6835 高6899 安6631 終6757｜約定 @6669（終値比 +1.32%）
- 6750 reversal 注文1917｜始1915 高1930 安1885 終1910｜約定 @1915（終値比 -0.26%）
- 4028 reversal 注文2604｜始2631 高2646 安2535 終2596｜約定 @2604（終値比 -0.31%）
- 6804 reversal 注文2145｜始2143 高2160 安2108 終2154｜約定 @2143（終値比 +0.51%）
- 6807 reversal 注文2263｜始2290 高2318 安2225 終2264｜約定 @2263（終値比 +0.04%）
- 6632 reversal 注文796｜始804 高807 安781 終787｜約定 @796（終値比 -1.13%）
- 5101 reversal 注文7482｜始7528 高7575 安7266 終7337｜約定 @7482（終値比 -1.94%）
- 8698 reversal 注文591｜始590 高592 安576 終576｜約定 @590（終値比 -2.37%）
- 6918 reversal 注文2780｜始2830 高2843 安2714 終2797｜約定 @2780（終値比 +0.61%）
- 4368 reversal 注文2690｜始2790 高2790 安2644 終2735｜約定 @2690（終値比 +1.67%）
- 2760 reversal 注文3825｜始3895 高3960 安3750 終3895｜約定 @3825（終値比 +1.83%）
- 5384 reversal 注文2775｜始2865 高2866 安2693 終2785｜約定 @2775（終値比 +0.36%）
- 6336 reversal 注文1164｜始1176 高1198 安1140 終1181｜約定 @1164（終値比 +1.46%）
- 2802 reversal 注文4155｜始4209 高4233 安4133 終4191｜約定 @4155（終値比 +0.87%）
- 3964 momentum 注文1274/上限1286.7｜始1262 高1271 安1247 終1262｜不約定
- 3092 momentum 注文1214/上限1226.1｜始1203.5 高1205 安1181.5 終1183.5｜不約定
- 6412 momentum 注文2159/上限2180.6｜始2154 高2155 安2112 終2135｜不約定
- 6877 oshime 注文6828｜始7400 高7400 安7100 終7280｜不約定
- 3851 momentum 注文927/上限936.3｜始932 高932 安869 終887｜約定 @932（終値比 -4.83%）
- 2489 reversal 注文316｜始316 高316 安304 終309｜約定 @316（終値比 -2.22%）
- 7609 reversal 注文3540｜始3680 高3815 安3585 終3770｜不約定
- 5256 reversal 注文2581｜始2580 高2580 安2440 終2499｜約定 @2580（終値比 -3.14%）
- 3850 reversal 注文3225｜始3200 高3215 安3160 終3190｜約定 @3200（終値比 -0.31%）
- 5599 momentum 注文1444/上限1458.4｜始1401 高1549 安1397 終1515｜約定 @1444（終値比 +4.92%）
- 8551 reversal 注文2112｜始2140 高2140 安2067 終2124｜約定 @2112（終値比 +0.57%）
- 3858 momentum 注文399/上限403｜始396 高444 安394 終405｜約定 @399（終値比 +1.50%）
- 3989 changepoint 注文1548｜始1537 高1543 安1535 終1535｜約定 @1537（終値比 -0.13%）

## 模擬テンプレ
```
# base_day 2026-11-18 ／ 提案32件
# 使い方: 参戦する0〜3銘柄の行だけをコピーし、｜の後ろに参戦理由を書いてポジション株PJへ送る。
# 選ばなかった行は送らなくてよい（全行に理由を書く必要はない）。見送りは末尾の1行で足りる。
# 特定銘柄を理由つきで見送る場合のみ『模擬 見送り {code} ｜{理由}』を送る。
模擬 5137 kenmo_momentum 逆指値316 SL296.1 単元100 ｜
模擬 558A kenmo_momentum 逆指値6190 SL5809.2 単元100 ｜
模擬 1721 choruko_reversal 指値5325 SL5152 単元100 ｜
模擬 9302 choruko_reversal 指値3229 SL3177 単元100 ｜
模擬 4272 choruko_reversal 指値1882 SL1830 単元100 ｜
模擬 6923 choruko_reversal 指値3250 SL3175 単元100 ｜
模擬 4768 choruko_reversal 指値3790 SL3603 単元100 ｜
模擬 6804 choruko_reversal 指値2154 SL2074 単元100 ｜
模擬 9468 choruko_reversal 指値3407 SL3358 単元100 ｜
模擬 9301 choruko_reversal 指値1266 SL1230.5 単元100 ｜
模擬 6779 ai_reversal 逆指値1714 SL1597 単元100 ｜
模擬 6762 ai_reversal 指値2264 SL2161.5 単元100 ｜
模擬 6941 ai_reversal 指値6510 SL6120 単元100 ｜
模擬 4022 ai_reversal 指値1271 SL1189 単元100 ｜
模擬 1982 ai_reversal 指値3040 SL2964 単元100 ｜
模擬 6617 ai_reversal 逆指値4810 SL4525 単元100 ｜
模擬 9075 granville_tenkan 逆指値6640 SL6232.2 単元100 ｜
模擬 4568 granville_tenkan 逆指値2780.5 SL2612.7 単元100 ｜
模擬 4540 granville_tenkan 逆指値4011 SL3765.6 単元100 ｜
模擬 4528 granville_tenkan 逆指値2497.5 SL2346.7 単元100 ｜
模擬 9404 granville_tenkan 逆指値2950 SL2772.1 単元100 ｜
模擬 5930 granville_tenkan 逆指値1901 SL1786 単元100 ｜
模擬 3156 granville_oshime 逆指値4490 SL4185 単元100 ｜
模擬 7970 granville_oshime 指値2399 SL2387.5 単元100 ｜
模擬 436A granville_oshime 指値1737 SL1728.4 単元100 ｜
模擬 4968 granville_rebound 指値1834 SL1696 単元100 ｜
模擬 7609 granville_rebound 指値3770 SL3450 単元100 ｜
模擬 6958 granville_rebound 指値698 SL668 単元100 ｜
模擬 7826 granville_rebound 逆指値8250 SL7650 単元100 ｜
模擬 4025 granville_rebound 指値5490 SL5210 単元100 ｜
模擬 5599 granville_rebound 指値1515 SL1365 単元100 ｜
模擬 3909 granville_rebound 逆指値681 SL522 単元100 ｜
模擬 見送り ｜
```

## PASS内訳
- PASS 55件 = 提案 32件（✅即時可22／⏳待機・確認足待ち5／⏸位置不適4／⏸トラップ疑い1） + 除外 23件（型不一致6（うち十字線0）/材料後出し3/鮮度切れ12/その他2）
  - 7995 Valqua Ltd.：⛔提案なし(指名鮮度切れ 11営業日)（nom_age 11）
  - 6875 メガチップス：⛔提案なし(指名鮮度切れ 13営業日)（nom_age 13）
  - 8154 加賀電子：⛔提案なし(材料後出し)
  - 3105 日清紡ホールディングス：⛔提案なし(指名鮮度切れ 13営業日)（nom_age 13）
  - 5310 Toyo Tanso Co., Ltd.：⛔提案なし(指名鮮度切れ 11営業日)（nom_age 11）
  - 6969 松尾電機：⛔提案なし(手法ブランチ不明)
  - 6668 ＡＤプラズマ：⛔提案なし(手法ブランチ不明)
  - 3927 アークン：⛔提案なし(指名鮮度切れ 14営業日)（nom_age 14）
  - 6768 Tamura Corporation：⛔提案なし(指名鮮度切れ 14営業日)（nom_age 14）
  - 4549 Eiken Chemical Co., Ltd.：⛔提案なし(指名鮮度切れ 20営業日)（nom_age 20）
  - 6072 ERTH Group Co.,Ltd.：⛔提案なし(材料後出し)
  - 7480 スズデン：⛔型不一致(既に支持帯以下)
  - 9824 Senshu Electric Co., Ltd.：⛔型不一致(既に支持帯以下)
  - 4258 AMIYA Corporation：⛔型不一致(既に支持帯以下)
  - 338A ZenmuTech,Inc.：⛔型不一致(既に支持帯以下)
  - 3042 セキュアヴェイル（セキュアヴェ）：⛔型不一致(既に支持帯以下)
  - 2326 Digital Arts Inc.：⛔型不一致(既に支持帯以下)
  - 6490 ＰＩＬＬＡＲ：⛔提案なし(指名鮮度切れ 17営業日)（nom_age 17）
  - 5033 Nulab Inc.：⛔提案なし(材料後出し)
  - 5367 Nikkato Corporation：⛔提案なし(指名鮮度切れ 12営業日)（nom_age 12）
  - 9697 カプコン：⛔提案なし(指名鮮度切れ 14営業日)（nom_age 14）
  - 278A Ｔｅｒｒａ　Ｄｒｏｎｅ：⛔提案なし(指名鮮度切れ 16営業日)（nom_age 16）
  - 6203 Howa Machinery, Ltd.：⛔提案なし(指名鮮度切れ 21営業日)（nom_age 21）

## 5手法銘柄
- 4249 MORIROKU COMPANY LTD.｜kenmo_momentum｜🚀確変｜🟢値頃｜FAIL_INSEN｜終値2828｜💰単元28.6万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 5136 tripla Co.,Ltd.｜changepoint/kenmo_momentum/changepoint🔔🔔/granville_oshime/changepoint🔔｜🚀確変｜⚪妥当｜FAIL_INSEN｜終値2663｜💰単元27.1万円｜📋カルテ窓 12/15(残18営業日) 📐進捗 上振れ 64.3%
- 4434 Serverworks Co., Ltd.｜kenmo_momentum｜🚀確変｜⚪妥当｜FAIL_INSEN｜終値3030｜💰単元30.1万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 8704 TRADERS HOLDINGS CO LTD｜kenmo_momentum｜🔥絶好調｜💎割安｜FAIL_INSEN｜終値1200｜💰単元12.1万円｜📐進捗 上振れ 44.7%
- 3915 TerraSky Co., Ltd.｜kenmo_momentum｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜終値1904｜💰単元19.4万円｜📑TOPIX低減対象（次 01/29 第2回/8） 📐進捗 上振れ 34.1%
- 147A SORACOM,INC.｜kenmo_momentum｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜終値973｜💰単元9.8万円｜📐進捗 上振れ 17.7%
- 4286 CL Holdings Inc.｜kenmo_momentum/kenmo_newhigh｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜終値1500｜💰単元14.8万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 6418 Japan Cash Machine Co., Ltd.｜granville_oshime/kenmo_newhigh/kenmo_momentum｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜終値1378｜💰単元14.2万円｜📑TOPIX低減対象（次 01/29 第2回/8） 📐進捗 上振れ 37.3%
- 5537 AlbaLink Co.,Ltd.｜kenmo_momentum/granville_oshime/granville_rebound｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜終値3550｜💰単元34.5万円｜📐進捗 上振れ 85.9%
- 5137 Smart Drive Co. Ltd.｜kenmo_momentum/granville_oshime｜🔥絶好調｜🟢値頃｜PASS｜終値315｜💰単元3.1万円｜momentum 逆指値316 SL296.1 上限319.2 乖離0.3%・✅即時可
  > 【業態】モビリティデータ活用の車両管理サービス提供。自動車、保険会社向け支援も。
  > 【いま】終値315円・直近5日+1.94%（材料未確認）
  > 【調子】🔥絶好調（9/13）— E軸判定不能(期首・進捗なし)
  > 【水準】🟢値頃（5.0/7）— PER15.91倍・PEG0.346・52週41.7% ／ 💰単元3.1万円
  > 【戦略】当日高値超えの逆指値316円で順張り参戦を検討。上限319.2円・SL296.1円目安
- 4377 ONE CAREER Inc.｜kenmo_momentum/granville_oshime/granville_rebound/stf_kakuhen｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜終値2502｜💰単元25.0万円｜📐進捗 上振れ 15.9%
- 6071 IBJ, Inc.｜kenmo_momentum/kenmo_newhigh/stf_kakuhen｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜終値978｜💰単元10.3万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 7637 Hakudo Co., Ltd.｜kenmo_momentum｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜終値3380｜💰単元36.7万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 4771 F&M Co., Ltd.｜kenmo_momentum/kenmo_newhigh｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜終値2919｜💰単元29.6万円｜📐進捗 上振れ 68.2%
- 4053 Sun Asterisk, Inc.｜kenmo_momentum｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜終値563｜💰単元5.8万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 1435 robot home Inc.｜kenmo_momentum｜⚡好調｜💎割安｜FAIL_INSEN｜終値163｜💰単元1.6万円｜📑TOPIX低減対象（次 01/29 第2回/8） 📐進捗 上振れ 24.8%
- 3556 RenetJapanGroup, Inc.｜kenmo_momentum/granville_tenkan｜⚡好調｜💎割安｜FAIL_INSEN｜終値857｜💰単元8.8万円
- 5821 Hirakawa Hewtech Corp.｜kenmo_momentum｜⚡好調｜💎割安｜FAIL_INSEN｜終値3155｜💰単元31.6万円｜📑TOPIX低減対象（次 01/29 第2回/8） 📐進捗 上振れ 11.8%
- 558A SQUEEZE Inc.｜kenmo_momentum｜⚡好調｜🟡やや割高｜PASS｜終値6180｜💰単元61.8万円｜momentum 逆指値6190 SL5809.2 上限6251.9 乖離0.2%・✅即時可｜⚠1単元でリスク枠超過（38,080円）
  > 【業態】自社ホテル運営や、システム開発・提供、宿泊施設の企画・開発などを手掛ける。
  > 【いま】終値6,180円・直近5日+7.11%（材料未確認）
  > 【調子】⚡好調（7/13）— D軸判定不能(四半期データ不足・中立1点)・E軸判定不能(進捗データ不足)・🔼進捗先行
  > 【水準】🟡やや割高（2.8/7）— PER39.36倍・PEG1.190・52週85.9% ／ 💰単元61.8万円
  > 【戦略】当日高値超えの逆指値6190円で順張り参戦を検討。上限6251.9円・SL5809.2円目安／⚠1単元リスク38,080円（枠超過）
- 2975 Star Mica Holdings Co., Ltd.｜kenmo_momentum｜⚡好調｜💎割安｜FAIL_INSEN｜終値1142｜💰単元11.6万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 9554 AViC Co. Ltd.｜kenmo_momentum｜⚡好調｜🟢値頃｜FAIL_INSEN｜終値1699｜💰単元17.6万円
- 262A INTERMESTIC INC.｜kenmo_momentum｜⚡好調｜💎割安｜FAIL_INSEN｜終値1528｜💰単元15.9万円｜📑TOPIX低減対象（次 01/29 第2回/8） 📐進捗 遅れ -10.9%
- 3798 ULS Group Incorporated｜kenmo_momentum/granville_tenkan｜✅順調｜💎割安｜FAIL_INSEN｜終値467｜💰単元4.8万円｜📐進捗 遅れ -12.6%
- 4743 ITFOR Inc.｜kenmo_momentum｜✅順調｜💎割安｜FAIL_INSEN｜終値1577｜💰単元16.0万円｜📑TOPIX低減対象（次 01/29 第2回/8） 📐進捗 遅れ -23.4%
- 6167 FUJI DIE Co., Ltd.｜kenmo_momentum｜✅順調｜🟡やや割高｜FAIL_UWAHIGE｜終値1111｜💰単元11.1万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 618A KOMPEITO Inc.｜kenmo_momentum/kenmo_newhigh｜取得不可｜⚪妥当｜FAIL_INSEN｜終値1708｜💰単元18.6万円
- 6943 ＮＫＫスイッチズ｜kenmo_newhigh｜🚀確変｜🟢値頃｜FAIL_INSEN｜終値6750｜💰単元69.9万円
- 446A ノースサンド｜kenmo_newhigh/granville_oshime/granville_rebound｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜終値2252｜💰単元23.3万円｜📋カルテ窓 12/11(残16営業日)
- 6238 フリュー｜kenmo_newhigh｜⚡好調｜🟡やや割高｜FAIL_INSEN｜終値1661｜💰単元16.9万円｜📑TOPIX低減対象（次 01/29 第2回/8） 📐進捗 遅れ -10.1%
- 3843 Freebit Co., Ltd.｜kenmo_newhigh/granville_tenkan｜✅順調｜🟡やや割高｜FAIL_INSEN｜終値2043｜💰単元20.7万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 4379 Photosynth inc.｜kenmo_newhigh｜✅順調｜🔴過熱｜FAIL_INSEN｜終値431｜💰単元4.4万円
- 9204 Skymark Airlines Inc.｜kenmo_newhigh｜🔻悪化｜🔴過熱｜FAIL_INSEN｜終値494｜💰単元5.0万円
- 1960 サンテック｜kenmo_newhigh｜➖横ばい｜🔴過熱｜FAIL_INSEN｜終値1715｜💰単元18.4万円
- 4933 I-ne CO., LTD.｜kenmo_newhigh｜取得不可｜⚪妥当｜FAIL_UWAHIGE｜終値2501｜💰単元24.9万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 6278 ユニオンツール｜choruko_reversal｜🚀確変｜🟢値頃｜FAIL_INSEN｜終値10390｜💰単元100.5万円
- 5711 三菱マテリアル｜choruko_reversal｜🚀確変｜💎割安｜FAIL_INSEN｜終値3917｜💰単元40.0万円
- 6481 THK Co., Ltd.｜choruko_reversal｜🚀確変｜💎割安｜FAIL_INSEN｜終値4513｜💰単元45.1万円
- 3036 アルコニックス｜choruko_reversal｜🚀確変｜🟢値頃｜FAIL_INSEN｜終値3020｜💰単元30.0万円｜📐進捗 上振れ 43.2%
- 6324 Harmonic Drive Systems Inc.｜choruko_reversal｜🚀確変｜🟢値頃｜FAIL_INSEN｜終値4116｜💰単元42.2万円
- 7995 Valqua Ltd.｜choruko_reversal/granville_rebound｜🚀確変｜🟢値頃｜PASS_DOJI｜終値5850｜💰単元58.5万円｜⛔提案なし(指名鮮度切れ 11営業日)｜⚠日程不明
  > 【業態】工業用液漏れシール最大手。ゴム・金属・ファイバー製など製品多。先端産業向け力。
  > 【いま】終値5,850円・直近5日-6.55%（材料未確認）
  > 【調子】🚀確変（11/13）— 上方修正済み・突出ボーナス・🔼加速
  > 【水準】🟢値頃（5.0/7）— PER10.32倍・PEG0.134・52週43.1% ／ 💰単元58.5万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 11営業日)）
- 6516 Sanyo Denki Co., Ltd.｜choruko_reversal/ai_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜終値4455｜💰単元43.9万円
- 7433 Hakuto Co., Ltd.｜ai_reversal/granville_oshime/choruko_reversal/granville_rebound｜🔥絶好調｜💎割安｜FAIL_INSEN｜終値1549｜💰単元15.3万円｜⚡材料後出し
- 5344 MARUWA CO., LTD.｜choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜終値41060｜💰単元397.2万円
- 6645 OMRON Corporation｜granville_rebound/choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜終値4671｜💰単元45.8万円｜📐進捗 上振れ 68.9%
- 9107 Kawasaki Kisen Kaisha, Ltd.｜choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜終値3112｜💰単元30.5万円
- 4216 ASAHI YUKIZAI CORPORATION｜choruko_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜終値5560｜💰単元55.0万円｜📐進捗 遅れ -15.1%
- 4471 三洋化成工業｜granville_oshime/choruko_reversal/granville_rebound｜🔥絶好調｜💎割安｜FAIL_INSEN｜終値1470｜💰単元14.6万円｜📐進捗 上振れ 38.0%
- 5703 日本軽金属ホールディングス（日軽金ＨＤ）｜choruko_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜終値2432｜💰単元24.8万円
- 6135 牧野フライス製作所｜choruko_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜終値2684｜💰単元26.9万円｜📐進捗 上振れ 27.2%
- 6652 IDEC Corporation｜choruko_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜終値3015｜💰単元30.1万円｜📐進捗 上振れ 59.9%
- 167A リョーサン菱洋ホールディングス（リョー菱ＨＤ）｜choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜終値3080｜💰単元30.9万円｜📐進捗 上振れ 53.4%
- 5301 Tokai Carbon Co., Ltd.｜choruko_reversal/granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜終値1565.5｜💰単元15.5万円
- 6588 東芝テック｜choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜終値2437｜💰単元24.7万円
- 6724 セイコーエプソン｜choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜終値2748.5｜💰単元27.3万円｜📐進捗 上振れ 24.7%
- 6925 Ushio Inc.｜choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜終値3029｜💰単元30.0万円｜📐進捗 上振れ 32.8%
- 6952 カシオ｜choruko_reversal｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜終値2026｜💰単元20.3万円｜📐進捗 上振れ 18.1%
- 6875 メガチップス｜choruko_reversal｜🔥絶好調｜💎割安｜PASS｜終値8660｜💰単元86.6万円｜⛔提案なし(指名鮮度切れ 13営業日)｜⚠日程不明 📐進捗 遅れ -48.4%
  > 【業態】カスタムLSI、画像転送システムが主力。生産外部委託。任天堂向け中心。5G向けも。
  > 【いま】終値8,660円・直近5日-0.69%（材料未確認）
  > 【調子】🔥絶好調（8/13）— 突出ボーナス・⚠進捗遅れ・⚠下期依存
  > 【水準】💎割安（7.0/7）— PER3.49倍・PEG0.000・52週22.9% ／ 💰単元86.6万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 13営業日)）
- 6471 日本精工｜choruko_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜終値950.3｜💰単元9.6万円
- 8084 ＲＹＯＤＥＮ｜granville_rebound/choruko_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜終値2160｜💰単元21.7万円｜📐進捗 上振れ 34.7%
- 8386 百十四銀行｜choruko_reversal/granville_rebound｜🔥絶好調｜💎割安｜FAIL_INSEN｜終値2600｜💰単元26.5万円
- 6754 アンリツ｜ai_reversal/choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜終値2262｜💰単元22.4万円
- 7731 ニコン｜choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜終値1551.5｜💰単元15.5万円
- 8524 North Pacific Bank, Ltd.｜granville_rebound/choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜終値1153｜💰単元11.6万円
- 9902 Nichiden Corporation｜granville_oshime/choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜終値2888｜💰単元28.9万円｜📑TOPIX低減対象（次 01/29 第2回/8） 📐進捗 上振れ 21.3%
- 7733 Olympus Corp.｜choruko_reversal｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜終値1798｜💰単元17.9万円｜📐進捗 上振れ 16.6%
- 4088 Air Water Inc.｜choruko_reversal｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜終値3060｜💰単元29.5万円
- 8133 伊藤忠エネクス｜choruko_reversal｜🔥絶好調｜🟡やや割高｜FAIL_INSEN｜終値2012｜💰単元20.4万円｜📐進捗 上振れ 83.7%
- 5333 ＮＧＫ｜choruko_reversal/ai_reversal｜⚡好調｜💎割安｜FAIL_INSEN｜終値4497｜💰単元44.0万円｜📐進捗 上振れ 14.0%
- 6036 ＫｅｅＰｅｒ技研｜granville_oshime/choruko_reversal｜⚡好調｜💎割安｜FAIL_INSEN｜終値1668｜💰単元17.1万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 8154 加賀電子｜choruko_reversal/granville_rebound/granville_oshime/stf_kakuhen｜⚡好調｜💎割安｜PASS｜終値5190｜💰単元51.9万円｜⛔提案なし(材料後出し)｜⚠日程不明 📐進捗 上振れ 11.4% ⚡材料後出し
  > 【業態】独立系エレクトロニクス商社。EMS事業に注力。旧富士通エレク買収でグループ拡大。
  > 【いま】終値5,190円・直近5日+0.78%・📌その他重要開示Notice Regarding Receipt of SBT Certification
  > 【調子】⚡好調（7/13）— 上方修正済み・🔼進捗先行
  > 【水準】💎割安（6.0/7）— PER7.73倍・PEG0.381・52週74.4% ／ 💰単元51.9万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 8393 Miyazaki Bank Ltd.｜choruko_reversal｜⚡好調｜💎割安｜FAIL_INSEN｜終値2272｜💰単元22.9万円
- 5186 ニッタ｜choruko_reversal/granville_rebound｜⚡好調｜🟢値頃｜FAIL_INSEN｜終値6100｜💰単元61.4万円｜📐進捗 上振れ 21.2%
- 6268 ナブテスコ｜choruko_reversal｜⚡好調｜🟢値頃｜FAIL_INSEN｜終値3424｜💰単元34.4万円
- 6448 ブラザー工業（ブラザー）｜choruko_reversal｜⚡好調｜🟢値頃｜FAIL_INSEN｜終値4376｜💰単元44.0万円｜📐進捗 上振れ 47.8%
- 4634 ａｒｔｉｅｎｃｅ（ａｒｔｉｅｎ）｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値4910｜💰単元50.8万円｜📐進捗 上振れ 13.7%
- 3116 Toyota Boshoku Corp.｜choruko_reversal｜⚡好調｜💎割安｜FAIL_INSEN｜終値2045｜💰単元20.5万円
- 5331 ノリタケ｜choruko_reversal/ai_reversal｜⚡好調｜💎割安｜FAIL_INSEN｜終値2840｜💰単元28.8万円｜📐進捗 上振れ 17.3%
- 7004 Kanadevia Corporation｜choruko_reversal｜⚠減速｜💎割安｜FAIL_INSEN｜終値935｜💰単元9.4万円
- 4205 Zeon Corporation｜choruko_reversal｜⚡好調｜💎割安｜FAIL_INSEN｜終値2009｜💰単元20.2万円｜📐進捗 上振れ 39.7%
- 6651 NITTO KOGYO Corporation｜choruko_reversal｜⚡好調｜💎割安｜FAIL_INSEN｜終値4040｜💰単元40.4万円｜📐進捗 上振れ 17.0%
- 4206 アイカ工業｜granville_oshime/choruko_reversal｜⚡好調｜🟢値頃｜FAIL_INSEN｜終値4042｜💰単元40.2万円
- 4966 上村工業｜choruko_reversal｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜終値15910｜💰単元155.2万円｜📑TOPIX新規採用（2026-10-30 組入）
- 5463 丸一鋼管（丸一管）｜choruko_reversal｜⚡好調｜🟢値頃｜FAIL_INSEN｜終値1615｜💰単元16.2万円
- 6250 Yamabiko Corporation｜granville_oshime/choruko_reversal｜⚡好調｜🟢値頃｜FAIL_INSEN｜終値3745｜💰単元38.0万円
- 6473 ジェイテクト｜choruko_reversal｜⚠減速｜🟢値頃｜FAIL_INSEN｜終値1954｜💰単元19.7万円
- 3569 セーレン｜granville_tenkan/choruko_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値3515｜💰単元35.2万円
- 9037 Hamakyorex Co., Ltd.｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値1671｜💰単元16.8万円
- 268A Rigaku Holdings Corporation｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜終値1318｜💰単元12.7万円｜📐進捗 遅れ -62.5%
- 5444 大和工業｜choruko_reversal｜⚡好調｜💎割安｜FAIL_INSEN｜終値10880｜💰単元108.7万円
- 9934 因幡電機産業｜choruko_reversal｜⚡好調｜🟢値頃｜FAIL_INSEN｜終値2562｜💰単元25.6万円
- 9960 トーテック｜choruko_reversal/ai_momentum/ai_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値4105｜💰単元42.0万円｜📐進捗 上振れ 11.8%
- 1721 コムシスホールディングス｜choruko_reversal｜⚡好調｜⚪妥当｜PASS｜終値5325｜💰単元53.2万円｜reversal 指値5325 SL5152・✅即時可｜⚠日程不明 📐進捗 上振れ 14.9%
  > 【業態】電気通信工事で首位。日本コムシス中核、NTT向けが過半。携帯各社の工事も。
  > 【いま】終値5,325円・直近5日+2.86%（材料未確認）
  > 【調子】⚡好調（5/13）— 上方修正済み・🔼加速・🔼進捗先行
  > 【水準】⚪妥当（3.0/7）— PER15.19倍・PEG1.639・52週59.8% ／ 💰単元53.2万円
  > 【戦略】当日終値5325円の指値で反転を取りにいく。SL5152円（直近5日安値）
- 1926 ライト工業（ライト）｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値980｜💰単元10.0万円｜📐進捗 上振れ 26.9%
- 4403 日油｜granville_tenkan/choruko_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値2551｜💰単元26.3万円
- 9072 NIKKON Holdings Co., Ltd.｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値4154｜💰単元41.4万円｜📐進捗 遅れ -10.5%
- 6454 マックス｜choruko_reversal｜⚡好調｜🟡やや割高｜FAIL_INSEN｜終値1808｜💰単元18.1万円
- 9302 三井倉庫ホールディングス｜choruko_reversal｜⚡好調｜🟡やや割高｜PASS｜終値3229｜💰単元32.3万円｜reversal 指値3229 SL3177・✅即時可｜⚠日程不明
  > 【業態】倉庫業大手。総合物流業務に強み。国際サプライチェーン展開。不動産賃貸が収益。
  > 【いま】終値3,229円・直近5日+1.25%（材料未確認）
  > 【調子】⚡好調（5/13）— 上方修正済み・🔼加速
  > 【水準】🟡やや割高（2.0/7）— PER18.58倍・PEG3.252・52週12.1% ／ 💰単元32.3万円
  > 【戦略】当日終値3229円の指値で反転を取りにいく。SL3177円（直近5日安値）
- 6845 アズビル｜choruko_reversal｜⚡好調｜🔴過熱｜FAIL_INSEN｜終値1489.5｜💰単元15.1万円
- 6340 澁谷工業｜granville_oshime/choruko_reversal/granville_rebound｜✅順調｜🟢値頃｜FAIL_INSEN｜終値4715｜💰単元46.6万円
- 6674 ジーエス・ユアサ　コーポレーション｜choruko_reversal｜✅順調｜🟢値頃｜FAIL_INSEN｜終値4190｜💰単元42.6万円｜📐進捗 上振れ 26.1%
- 1663 K&O Energy Group, Inc.｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜終値1737｜💰単元17.3万円｜📑TOPIX低減対象（次 01/29 第2回/8） 📐進捗 上振れ 11.0%
- 4272 Nippon Kayaku Co., Ltd.｜granville_tenkan/granville_oshime/choruko_reversal｜✅順調｜⚪妥当｜PASS｜終値1882｜💰単元18.8万円｜reversal 指値1882 SL1830・✅即時可｜⚠日程不明 📐進捗 上振れ 13.1%
  > 【業態】火薬から機能化学品など多角化。医薬、自動車部材等。抗がん剤に強み。(化学)
  > 【いま】終値1,882円・直近5日+1.32%（材料未確認）
  > 【調子】✅順調（4/13）— 上方修正済み・⚠減速・🔼進捗先行
  > 【水準】⚪妥当（4.0/7）— PER11.18倍・PEG1.176・52週55.7% ／ 💰単元18.8万円
  > 【戦略】当日終値1882円の指値で反転を取りにいく。SL1830円（直近5日安値）
- 6923 Stanley Electric Co., Ltd.｜choruko_reversal｜✅順調｜⚪妥当｜PASS｜終値3250｜💰単元32.5万円｜reversal 指値3250 SL3175・✅即時可｜⚠日程不明 📐進捗 遅れ -19.8%
  > 【業態】自動車用照明器大手。ホンダ向け比重大。LEDの電子制御機器も収益大。
  > 【いま】終値3,250円・直近5日+0.03%（材料未確認）
  > 【調子】✅順調（4/13）— 🔼加速・⚠進捗遅れ
  > 【水準】⚪妥当（4.0/7）— PER11.76倍・PEG0.837・52週47.7% ／ 💰単元32.5万円
  > 【戦略】当日終値3250円の指値で反転を取りにいく。SL3175円（直近5日安値）
- 3445 RS Technologies Co. Ltd.｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜終値4165｜💰単元40.8万円
- 4021 Nissan Chemical Corporation｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜終値6757｜💰単元66.7万円
- 4042 東ソー｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜終値2491.5｜💰単元24.6万円
- 5021 コスモＨＤ｜choruko_reversal｜🔻悪化｜⚪妥当｜FAIL_INSEN｜終値3381｜💰単元35.0万円｜📐進捗 上振れ 12.4%
- 6055 Japan Material Co., Ltd.｜choruko_reversal/ai_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜終値1588｜💰単元15.4万円｜📐進捗 上振れ 41.2%
- 7276 Koito Manufacturing Co., Ltd.｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜終値2510｜💰単元25.1万円
- 6750 エレコム｜choruko_reversal｜✅順調｜🟡やや割高｜FAIL_INSEN｜終値1910｜💰単元19.2万円｜📐進捗 上振れ 25.2%
- 4768 OTSUKA CORPORATION｜granville_rebound/choruko_reversal｜✅順調｜🔴過熱｜PASS｜終値3790｜💰単元37.9万円｜reversal 指値3790 SL3603・✅即時可｜⚠日程不明
  > 【業態】独立系SI大手。開発から保守まで一貫。中小に強み。事務用品の販売も。
  > 【いま】終値3,790円・直近5日+2.10%（材料未確認）
  > 【調子】✅順調（4/13）— ⚠減速
  > 【水準】🔴過熱（1.0/7）— PER22.14倍・PEG4.429・52週60.0% ／ 💰単元37.9万円
  > 【戦略】当日終値3790円の指値で反転を取りにいく。SL3603円（直近5日安値）
- 6277 Hosokawa Micron Corporation｜choruko_reversal｜✅順調｜🔴過熱｜FAIL_INSEN｜終値5940｜💰単元59.6万円
- 6332 月島ホールディングス｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜終値2238｜💰単元22.7万円｜📐進捗 遅れ -23.7%
- 6368 Organo Corp.｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜終値1651｜💰単元16.6万円
- 1951 エクシオグループ（エクシオＧ）｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜終値2371｜💰単元24.0万円｜📐進捗 上振れ 57.9%
- 1963 日揮ホールディングス｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜終値2055｜💰単元20.6万円
- 4028 石原産業｜choruko_reversal｜🔻悪化｜⚪妥当｜FAIL_INSEN｜終値2596｜💰単元26.0万円｜📐進捗 遅れ -11.2%
- 5602 栗本鐵工所（栗本鉄）｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_UWAHIGE｜終値1445｜💰単元14.2万円
- 6804 ホシデン｜choruko_reversal｜🔻悪化｜⚪妥当｜PASS｜終値2154｜💰単元21.5万円｜reversal 指値2154 SL2074・✅即時可｜📐進捗 上振れ 31.8% ⚠業績基調が下向き（🔻悪化）
  > 【業態】電気機器（電子部品・コネクター・自動車部材・部品関連）
  > 【いま】終値2,154円・直近5日-1.91%（材料未確認）
  > 【調子】🔻悪化（3/13）— A成長率0以下のためレバレッジ計算不可(C=0)・質注意・経常減益-27.0%・⚠減速・🔼進捗先行
  > 【水準】⚪妥当（3.0/7）— PER8.48倍・PEG—・52週7.4% ／ 💰単元21.5万円
  > 【戦略】当日終値2154円の指値で反転を取りにいく。SL2074円（直近5日安値）
- 3105 日清紡ホールディングス｜choruko_reversal｜✅順調｜🟡やや割高｜PASS｜終値1890.5｜💰単元18.9万円｜⛔提案なし(指名鮮度切れ 13営業日)｜⚠日程不明
  > 【業態】綿紡老舗から転換。ブレーキ摩擦材で世界首位。防災無線、デジタル技術を推進。
  > 【いま】終値1,890円・直近5日-5.05%（材料未確認）
  > 【調子】✅順調（3/13）— 進捗モデル値域外・質注意・経常減益-4.5%・上方修正済み・🔼進捗先行
  > 【水準】🟡やや割高（2.0/7）— PER11.36倍・PEG—・52週42.6% ／ 💰単元18.9万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 13営業日)）
- 5201 AGC Inc.｜choruko_reversal｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜終値4836｜💰単元47.8万円｜📐進捗 上振れ 46.3%
- 5310 Toyo Tanso Co., Ltd.｜choruko_reversal/ai_reversal｜🔻悪化｜🟡やや割高｜PASS｜終値6100｜💰単元61.0万円｜⛔提案なし(指名鮮度切れ 11営業日)｜⚠日程不明 ⚠業績基調が下向き（🔻悪化）
  > 【業態】等方性黒鉛で先駆、世界高シェア。半導体製造用るつぼが主力。一貫生産。
  > 【いま】終値6,100円・直近5日-3.33%（材料未確認）
  > 【調子】🔻悪化（3/13）— 質注意・経常減益-25.8%・🔼加速
  > 【水準】🟡やや割高（2.0/7）— PER25.59倍・PEG—・52週35.8% ／ 💰単元61.0万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 11営業日)）
- 6741 日本信号｜choruko_reversal｜✅順調｜🟡やや割高｜FAIL_INSEN｜終値1631｜💰単元16.3万円｜📐進捗 上振れ 48.5%
- 6807 Japan Aviation Electronics Industry, Limited｜choruko_reversal｜✅順調｜🟡やや割高｜FAIL_INSEN｜終値2264｜💰単元22.6万円
- 7220 Musashi Seimitsu Industry Co., Ltd.｜choruko_reversal｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜終値2032｜💰単元19.9万円｜📐進捗 上振れ 45.3%
- 4902 Konica Minolta, Inc.｜granville_tenkan/choruko_reversal｜➖横ばい｜💎割安｜FAIL_INSEN｜終値565.7｜💰単元5.7万円
- 6479 ミネベア｜choruko_reversal｜➖横ばい｜💎割安｜FAIL_INSEN｜終値2852｜💰単元28.6万円
- 1979 大気社｜choruko_reversal｜➖横ばい｜⚪妥当｜FAIL_INSEN｜終値3335｜💰単元33.5万円
- 4008 住友精化｜choruko_reversal｜🔻悪化｜⚪妥当｜FAIL_INSEN｜終値1298｜💰単元13.1万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 9468 カドカワ｜choruko_reversal｜➖横ばい｜🔴過熱｜PASS｜終値3407｜💰単元34.1万円｜reversal 指値3407 SL3358・✅即時可｜📐進捗 遅れ -27.0%
  > 【業態】出版・動画配信大手。カドカワとドワンゴが経営統合。アニメ・電子書籍に強み。
  > 【いま】終値3,407円・直近5日-5.10%（材料未確認）
  > 【調子】➖横ばい（2/13）— 質注意・⚠進捗遅れ
  > 【水準】🔴過熱（1.0/7）— PER501.03倍・PEG196.072・52週55.7% ／ 💰単元34.1万円
  > 【戦略】当日終値3407円の指値で反転を取りにいく。SL3358円（直近5日安値）
- 6632 JVCKENWOOD Corporation｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜終値787｜💰単元8.0万円
- 4746 東計電算｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜終値1712｜💰単元17.1万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 4980 Dexerials Corp.｜choruko_reversal/ai_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜終値1925.5｜💰単元18.9万円｜📐進捗 遅れ -16.3%
- 9722 藤田観光｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜終値2759｜💰単元27.8万円
- 6370 栗田工業｜choruko_reversal｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜終値5622｜💰単元55.5万円｜📐進捗 遅れ -50.6%
- 6436 アマノ｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜終値3572｜💰単元36.0万円
- 8508 J Trust Co., Ltd.｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜終値680｜💰単元6.8万円｜📑TOPIX新規採用（2026-10-30 組入） 📐進捗 上振れ 40.4% ⚡材料後出し
- 9301 三菱倉｜choruko_reversal｜⚠減速｜🟡やや割高｜PASS｜終値1266｜💰単元12.7万円｜reversal 指値1266 SL1230.5・✅即時可｜⚠日程不明 ⚠業績基調が下向き（⚠減速）
  > 【業態】倉庫業大手。施設の高度化に注力。陸上・港湾・国際一貫輸送に強み。
  > 【いま】終値1,266円・直近5日+1.73%（材料未確認）
  > 【調子】⚠減速（1/13）— E軸判定不能(進捗データ不足)・質注意
  > 【水準】🟡やや割高（2.0/7）— PER18.70倍・PEG108.981・52週31.3% ／ 💰単元12.7万円
  > 【戦略】当日終値1266円の指値で反転を取りにいく。SL1230.5円（直近5日安値）
- 7148 Financial Products Group Co., Ltd.｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜終値1375｜💰単元14.1万円
- 6379 レイズネク｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜終値960｜💰単元9.4万円｜📐進捗 上振れ 21.9%
- 7278 Exedy Corporation｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜終値5190｜💰単元51.9万円｜📐進捗 遅れ -14.7%
- 2109 ＤＭ三井製糖｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜終値3575｜💰単元36.3万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 6349 Komori Corporation｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜終値1677｜💰単元16.9万円｜📐進捗 上振れ 24.1%
- 3612 WORLD CO.,LTD.｜choruko_reversal｜業績データ取得不可(経常益予想非開示)｜💎割安｜FAIL_INSEN｜終値1470｜💰単元15.1万円
- 6810 Maxell, Ltd.｜granville_oshime/choruko_reversal/granville_rebound｜業績データ取得不可(経常益予想非開示)｜💎割安｜FAIL_INSEN｜終値2113｜💰単元21.3万円
- 7322 三十三フィナンシャルグループ｜choruko_reversal/granville_rebound｜取得不可｜💎割安｜FAIL_INSEN｜終値1701｜💰単元17.1万円
- 8366 滋賀銀行｜granville_rebound/choruko_reversal｜取得不可｜💎割安｜FAIL_INSEN｜終値2076.5｜💰単元21.0万円
- 7381 ＣＣＩグループ｜choruko_reversal/granville_rebound｜業績データ取得不可(売上/経常欠損)｜🟢値頃｜FAIL_INSEN｜終値1028｜💰単元10.5万円｜📐進捗 遅れ -13.8%
- 8975 Ichigo Office REIT Investment Corporation｜choruko_reversal｜判定保留(変則決算)｜🟢値頃｜FAIL_INSEN｜終値88200｜💰単元8.9万円｜📋カルテ窓 12/16(残19営業日)
- 4293 セプテーニ・ホールディングス（セプテニＨＤ）｜choruko_reversal｜取得不可｜🟢値頃｜FAIL_UWAHIGE｜終値447｜💰単元4.5万円
- 5101 Yokohama Rubber Co., Ltd.｜choruko_reversal｜取得不可｜🟢値頃｜FAIL_INSEN｜終値7337｜💰単元74.8万円
- 5831 Shizuoka Financial Group, Inc.｜choruko_reversal/granville_rebound｜業績データ取得不可(売上/経常欠損)｜🟢値頃｜FAIL_INSEN｜終値3080｜💰単元31.1万円
- 7167 めぶきフィナンシャルグループ｜choruko_reversal/granville_rebound｜取得不可｜🟢値頃｜FAIL_INSEN｜終値1439.5｜💰単元14.6万円
- 7186 横浜フィナンシャルグループ｜choruko_reversal｜取得不可｜🟢値頃｜FAIL_INSEN｜終値1648｜💰単元16.8万円
- 8253 Credit Saison Co., Ltd.｜choruko_reversal｜取得不可｜🟢値頃｜FAIL_INSEN｜終値4925｜💰単元49.7万円
- 8354 ふくおかフィナンシャルグループ｜choruko_reversal｜業績データ取得不可(売上/経常欠損)｜🟢値頃｜FAIL_INSEN｜終値6833｜💰単元68.8万円
- 8359 Hachijuni Nagano Bank, Ltd.｜choruko_reversal/granville_rebound｜業績データ取得不可(売上/経常欠損)｜🟢値頃｜FAIL_INSEN｜終値2327.5｜💰単元24.0万円｜📐進捗 上振れ 10.1%
- 8370 紀陽銀行｜choruko_reversal｜業績データ取得不可(売上/経常欠損)｜🟢値頃｜FAIL_INSEN｜終値1425｜💰単元14.5万円
- 8304 あおぞら銀行｜choruko_reversal｜取得不可｜⚪妥当｜FAIL_INSEN｜終値3156｜💰単元31.8万円｜📐進捗 上振れ 11.0%
- 8334 Gunma Bank, Ltd.｜granville_rebound/choruko_reversal｜業績データ取得不可(売上/経常欠損)｜⚪妥当｜FAIL_INSEN｜終値2390｜💰単元24.3万円
- 8600 トモニホールディングス｜choruko_reversal｜取得不可｜⚪妥当｜FAIL_INSEN｜終値951｜💰単元9.6万円
- 8032 紙パル商｜choruko_reversal｜取得不可｜🟡やや割高｜FAIL_INSEN｜終値1127｜💰単元11.2万円
- 5019 出光興産｜choruko_reversal｜取得不可｜⏸判定不能｜FAIL_UWAHIGE｜終値1241｜💰単元12.3万円
- 7177 ＧＭＯフィナンシャルホールディングス｜choruko_reversal｜取得不可｜⏸判定不能｜FAIL_INSEN｜終値1042｜💰単元10.5万円
- 8616 Tokai Tokyo Financial Holdings, Inc.｜choruko_reversal｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜終値744｜💰単元7.6万円
- 8698 Monex Group, Inc.｜choruko_reversal｜業績データ取得不可(経常益予想非開示)｜⏸判定不能｜FAIL_INSEN｜終値576｜💰単元5.9万円
- 3131 Shinden Hightex Corp.｜granville_rebound/ai_reversal/stf_kakuhen/granville_oshime｜🚀確変｜💎割安｜FAIL_INSEN｜終値6600｜💰単元63.5万円｜📐進捗 上振れ 32.9%
- 9308 乾汽船｜changepoint/changepoint🔔🔔/granville_oshime/stf_kakuhen｜🚀確変｜🟢値頃｜FAIL_UWAHIGE｜終値2180｜💰単元21.6万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 6969 松尾電機｜stf_kakuhen｜🔥絶好調｜💎割安｜PASS｜終値1151｜💰単元11.5万円｜⛔提案なし(手法ブランチ不明)｜📐進捗 上振れ 21.9%
  > 【業態】コンデンサ大手。自動車用、産業用、タンタルに強み。電流ヒューズも。デンソー向け大。
  > 【いま】終値1,151円・直近5日-2.87%（材料未確認）
  > 【調子】🔥絶好調（10/13）— 🔼進捗先行・⚠下期依存
  > 【水準】💎割安（7.0/7）— PER7.61倍・PEG0.148・52週26.4% ／ 💰単元11.5万円
  > 【戦略】発注対象外（⛔提案なし(手法ブランチ不明)）
- 6668 ＡＤプラズマ｜stf_kakuhen/granville_oshime/granville_rebound｜🔥絶好調｜💎割安｜PASS｜終値3675｜💰単元36.8万円｜⛔提案なし(手法ブランチ不明)｜⚠日程不明
  > 【業態】高周波プラズマ電源装置最大手。液晶、半導体装置向け主力。技術に強み。
  > 【いま】終値3,675円・直近5日-7.31%（材料未確認）
  > 【調子】🔥絶好調（10/13）— E軸判定不能(進捗データ不足)
  > 【水準】💎割安（6.0/7）— PER8.48倍・PEG0.128・52週50.9% ／ 💰単元36.8万円
  > 【戦略】発注対象外（⛔提案なし(手法ブランチ不明)）
- 5832 ちゅうぎんフィナンシャルグループ（ちゅうぎんＦ）｜stf_kakuhen｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜終値3392｜💰単元34.1万円
- 3205 ダイドー｜stf_kakuhen｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜終値750｜💰単元7.6万円
- 4410 ハリマ化成グループ（ハリマ化成Ｇ）｜stf_kakuhen｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜終値1280｜💰単元13.0万円｜📑TOPIX低減対象（次 01/29 第2回/8） 📐進捗 上振れ 21.5%
- 5018 ＭＯＲＥＳＣＯ｜stf_kakuhen｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜終値2707｜💰単元27.6万円
- 5246 ＥＬＥＭＥＮＴＳ｜stf_kakuhen/granville_oshime/granville_rebound｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜終値833｜💰単元8.4万円
- 7942 ＪＳＰ｜stf_kakuhen｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜終値3075｜💰単元30.8万円｜📑TOPIX低減対象（次 01/29 第2回/8） 📐進捗 上振れ 61.9%
- 9962 ミスミグループ本社（ミスミＧ）｜stf_kakuhen｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜終値3656｜💰単元36.1万円
- 4180 Appier Group, Inc.｜granville_oshime/stf_kakuhen｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜終値1443｜💰単元15.0万円
- 3498 霞ヶ関Ｃ｜stf_kakuhen/granville_tenkan｜🔥絶好調｜💎割安｜FAIL_INSEN｜終値6610｜💰単元68.3万円
- 9110 ＮＳユナイテッド海運（ユナイテド海）｜stf_kakuhen｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜終値10550｜💰単元105.4万円｜📐進捗 上振れ 21.3%
- 3994 マネーフォワード｜stf_kakuhen/changepoint🔔🔔/changepoint🔔/changepoint｜🔥絶好調｜🔴過熱｜FAIL_INSEN｜終値6806｜💰単元72.6万円
- 9766 コナミグループ（コナミＧ）｜stf_kakuhen｜🔥絶好調｜🟡やや割高｜FAIL_UWAHIGE｜終値29600｜💰単元295.3万円
- 6850 チノー｜stf_kakuhen｜⚡好調｜🟢値頃｜FAIL_INSEN｜終値1764｜💰単元17.6万円｜📑TOPIX低減対象（次 01/29 第2回/8） 📐進捗 上振れ 30.4%
- 2331 ＡＬＳＯＫ｜stf_kakuhen｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値1350.5｜💰単元13.6万円｜📐進捗 上振れ 15.6%
- 4503 アステラス製薬（アステラス）｜stf_kakuhen｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜終値2725｜💰単元27.3万円｜📐進捗 遅れ -19.4%
- 6758 ソニーグループ｜ai_momentum/stf_kakuhen｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜終値4241｜💰単元42.7万円
- 3091 ブロンコビリー｜stf_kakuhen｜⚡好調｜🟡やや割高｜FAIL_INSEN｜終値3035｜💰単元31.2万円
- 1980 ダイダン｜stf_kakuhen｜⚡好調｜🟢値頃｜FAIL_INSEN｜終値3015｜💰単元29.8万円｜📐進捗 上振れ 52.8%
- 3479 ＴＫＰ｜stf_kakuhen/granville_tenkan｜⚡好調｜🔴過熱｜FAIL_INSEN｜終値2070｜💰単元21.2万円
- 4417 グローバルセキュリティエキスパート（Ｇセキュリ）｜stf_kakuhen｜⚡好調｜🔴過熱｜FAIL_INSEN｜終値8480｜💰単元84.8万円
- 6016 ジャパンエンジン｜stf_kakuhen｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値9870｜💰単元97.8万円
- 6532 ベイカレント｜stf_kakuhen｜⚡好調｜🟡やや割高｜FAIL_UWAHIGE｜終値12630｜💰単元127.8万円
- 7747 朝日インテック｜granville_tenkan/stf_kakuhen｜⚡好調｜🔴過熱｜FAIL_UWAHIGE｜終値4225｜💰単元42.6万円｜📐進捗 遅れ -35.4%
- 4176 ココナラ｜stf_kakuhen｜✅順調｜💎割安｜FAIL_INSEN｜終値262｜💰単元2.6万円
- 7366 ＬＩＴＡＬＩＣＯ（りたりこ）｜stf_kakuhen｜業績データ取得不可(経常益予想非開示)｜⚪妥当｜FAIL_INSEN｜終値2016｜💰単元20.9万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 9434 ソフトバンク｜ai_reversal/stf_kakuhen｜取得不可｜⚪妥当｜FAIL_INSEN｜終値245.9｜💰単元2.4万円
- 3932 アカツキ｜stf_kakuhen｜—｜⏸判定不能｜FAIL_INSEN｜終値1428｜💰単元14.6万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 9048 名古屋鉄道｜value_gap｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値2002｜💰単元20.3万円

## グランビル銘柄
- 3927 アークン｜granville_tenkan｜🔥絶好調｜💎割安｜PASS｜終値811｜💰単元8.1万円｜⛔提案なし(指名鮮度切れ 14営業日)
  > 【業態】情報セキュリティ製品の開発・販売・保守。中小企業向けの業務システムに注力。
  > 【いま】終値811円・直近5日-12.70%（材料未確認）
  > 【調子】🔥絶好調（10/13）— 進捗モデル値域外・突出ボーナス・⚠進捗遅れ・⚠下期依存
  > 【水準】💎割安（6.0/7）— PER13.19倍・PEG0.126・52週10.2% ／ 💰単元8.1万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 14営業日)）
- 6768 Tamura Corporation｜granville_tenkan/granville_oshime｜🔥絶好調｜💎割安｜PASS_DOJI｜終値671｜💰単元6.7万円｜⛔提案なし(指名鮮度切れ 14営業日)｜⚠日程不明 📐進捗 上振れ 15.1%
  > 【業態】弱電用トランス、リアクター大手。ハンダ、絶縁膜や音声・ワイヤレス機器も。海外生産メイン。
  > 【いま】終値671円・直近5日-7.70%（材料未確認）
  > 【調子】🔥絶好調（10/13）— 上方修正済み・🔼加速・🔼進捗先行
  > 【水準】💎割安（6.0/7）— PER8.21倍・PEG0.220・52週20.0% ／ 💰単元6.7万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 14営業日)）
- 8012 Nagase & Co., Ltd.｜granville_tenkan｜🔥絶好調｜💎割安｜FAIL_INSEN｜終値1149｜💰単元11.6万円｜📐進捗 上振れ 26.1%
- 6744 能美防災｜granville_tenkan｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜終値4550｜💰単元45.3万円｜📐進捗 上振れ 62.4%
- 3002 グンゼ｜granville_tenkan｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜終値4315｜💰単元43.8万円｜📐進捗 上振れ 31.1%
- 4523 エーザイ｜granville_tenkan｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜終値5240｜💰単元51.9万円
- 9742 アイネス｜granville_tenkan｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜終値2374｜💰単元23.5万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 3964 オークネット｜granville_tenkan｜⚡好調｜💎割安｜FAIL_INSEN｜終値1262｜💰単元12.6万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 4005 住友化学｜granville_tenkan｜⚡好調｜💎割安｜FAIL_INSEN｜終値493.2｜💰単元5.0万円
- 3405 クラレ｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_INSEN｜終値1829｜💰単元18.7万円｜📐進捗 上振れ 24.8%
- 4401 ＡＤＥＫＡ｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_INSEN｜終値4170｜💰単元42.1万円｜📐進捗 上振れ 20.2%
- 4534 Mochida Pharmaceutical Co., Ltd.｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_INSEN｜終値3325｜💰単元33.7万円｜📐進捗 上振れ 34.6%
- 5532 リアルゲイト｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜終値3090｜💰単元30.9万円｜⚡材料後出し
- 9006 Keikyu Corporation｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値1593.5｜💰単元16.3万円｜📐進捗 遅れ -20.6%
- 9075 福山通運｜granville_oshime/granville_tenkan｜⚡好調｜⚪妥当｜PASS｜終値6580｜💰単元65.8万円｜momentum 逆指値6640 SL6232.2 上限6706.4 乖離0.9%・✅即時可｜📐進捗 上振れ 10.4% ⚠1単元でリスク枠超過（40,780円）
  > 【業態】西日本地盤の路線トラック大手。小口雑貨に強み。セイノーHDと共同運送を推進。
  > 【いま】終値6,580円・直近5日+5.28%（材料未確認）
  > 【調子】⚡好調（7/13）— 上方修正済み・🔼進捗先行
  > 【水準】⚪妥当（4.0/7）— PER13.09倍・PEG0.403・52週83.7% ／ 💰単元65.8万円
  > 【戦略】当日高値超えの逆指値6640円で順張り参戦を検討。上限6706.4円・SL6232.2円目安／⚠1単元リスク40,780円（枠超過）
- 4507 塩野義製薬｜granville_tenkan｜⚡好調｜🟡やや割高｜FAIL_INSEN｜終値3175｜💰単元31.9万円｜📐進捗 上振れ 12.5%
- 3491 ＧＡ　ｔｅｃｈｎｏｌｏｇｉｅｓ（ＧＡテクノ）｜granville_tenkan｜⚡好調｜💎割安｜FAIL_INSEN｜終値1321｜💰単元14.2万円｜📋カルテ窓 12/10(残15営業日) 📐進捗 遅れ -31.4%
- 1941 中電工｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_INSEN｜終値5130｜💰単元50.8万円
- 3496 アズーム｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_INSEN｜終値3665｜💰単元37.1万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 2502 Asahi Group Holdings, Ltd.｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値1820｜💰単元18.1万円
- 4848 Fullcast Holdings Co., Ltd.｜granville_tenkan/granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値1817｜💰単元18.4万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 6099 エラン｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値759｜💰単元7.7万円｜📑TOPIX低減対象（次 01/29 第2回/8） 📐進捗 上振れ 13.5%
- 4045 Toagosei Co., Ltd.｜granville_tenkan｜⚡好調｜🟡やや割高｜FAIL_INSEN｜終値1755｜💰単元17.7万円
- 4554 Fuji Pharma Co., Ltd.｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_INSEN｜終値1784｜💰単元18.6万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 9842 アークランズ｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_INSEN｜終値1941｜💰単元19.7万円
- 8804 東京建物｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値3394｜💰単元34.6万円
- 2206 江崎グリコ｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値5108｜💰単元51.6万円｜📐進捗 遅れ -23.3%
- 7606 ＴＡＢＡＹＡホールディングス｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値2626｜💰単元27.1万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 8016 オンワード HD｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値776｜💰単元8.0万円
- 4091 Nippon Sanso Holdings Corporation｜granville_tenkan｜⚡好調｜🟡やや割高｜FAIL_INSEN｜終値5910｜💰単元53.5万円
- 9513 Electric Power Development Co., Ltd.｜granville_tenkan｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜終値4045｜💰単元40.5万円｜📐進捗 上振れ 18.7%
- 9065 Sankyu Inc.｜granville_tenkan｜✅順調｜💎割安｜FAIL_INSEN｜終値1692｜💰単元17.2万円
- 4169 Enechange Ltd.｜granville_tenkan｜⚠減速｜⚪妥当｜FAIL_INSEN｜終値249｜💰単元2.8万円｜📐進捗 遅れ -13.0% ⚡材料後出し
- 4568 第一三共｜granville_tenkan｜✅順調｜⚪妥当｜PASS｜終値2777.5｜💰単元27.8万円｜momentum 逆指値2780.5 SL2612.7 上限2808.3 乖離0.1%・⏸位置不適(25MA下 -0.3%／52週 25.4%)｜⚠日程不明
  > 【業態】国内製薬大手。循環器と感染症に強み。がん新薬で英アストラゼネカと提携。
  > 【いま】終値2,778円・直近5日+0.27%（材料未確認）
  > 【調子】✅順調（4/13）— 税引前代替・D軸判定不能(直近Qデータ取得不可)・上方修正済み
  > 【水準】⚪妥当（4.0/7）— PER20.16倍・PEG1.416・52週25.4% ／ 💰単元27.8万円
  > 【戦略】当日高値超えの逆指値2780.5円で順張り参戦を検討。上限2808.3円・SL2612.7円目安
- 1911 Sumitomo Forestry Co., Ltd.｜granville_tenkan｜🔻悪化｜⚪妥当｜FAIL_INSEN｜終値1198.5｜💰単元12.7万円
- 2488 ＪＴＰ｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_INSEN｜終値1340｜💰単元13.7万円｜📐進捗 上振れ 19.5%
- 417A ブルーゾーンホールディングス｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_INSEN｜終値1964.5｜💰単元19.5万円
- 4549 Eiken Chemical Co., Ltd.｜granville_tenkan｜✅順調｜🟡やや割高｜PASS｜終値2273｜💰単元22.7万円｜⛔提案なし(指名鮮度切れ 20営業日)｜⚠日程不明
  > 【業態】臨床検査薬大手。便潜血試薬で高シェア。微生物、遺伝子、尿検査なども。
  > 【いま】終値2,273円・直近5日+4.17%（材料未確認）
  > 【調子】✅順調（4/13）
  > 【水準】🟡やや割高（2.0/7）— PER36.31倍・PEG18.440・52週17.0% ／ 💰単元22.7万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 20営業日)）
- 5184 ニチリン｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_INSEN｜終値4080｜💰単元41.1万円｜📐進捗 上振れ 13.3%
- 7269 スズキ｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_INSEN｜終値2124｜💰単元21.5万円｜📐進捗 上振れ 20.4%
- 9418 Ｕ－ＮＥＸＴ　ＨＯＬＤＩＮＧＳ｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_UWAHIGE｜終値1863｜💰単元18.7万円
- 3092 ＺＯＺＯ｜granville_tenkan｜✅順調｜🔴過熱｜FAIL_INSEN｜終値1183.5｜💰単元12.1万円
- 3549 クスリのアオキホールディングス｜granville_tenkan｜✅順調｜🔴過熱｜FAIL_INSEN｜終値4949｜💰単元51.5万円
- 8113 Unicharm Corporation｜granville_tenkan｜✅順調｜🔴過熱｜FAIL_INSEN｜終値1127.5｜💰単元11.6万円
- 8160 KISOJI CO., LTD.｜granville_tenkan｜✅順調｜🔴過熱｜FAIL_UWAHIGE｜終値2579｜💰単元26.0万円
- 8934 Sun Frontier Fudousan Co., Ltd.｜granville_tenkan｜✅順調｜💎割安｜FAIL_INSEN｜終値2346｜💰単元21.6万円
- 8056 ＢＩＰＲＯＧＹ｜granville_tenkan｜✅順調｜🟢値頃｜FAIL_INSEN｜終値4698｜💰単元47.3万円｜📐進捗 遅れ -25.7%
- 9163 Nareru Group Inc.｜granville_tenkan｜✅順調｜🟢値頃｜FAIL_INSEN｜終値2017｜💰単元20.4万円｜📋カルテ窓 12/15(残18営業日) ⚡材料後出し
- 9956 Valor Holdings Co., Ltd.｜granville_tenkan｜✅順調｜⚪妥当｜FAIL_INSEN｜終値1626｜💰単元16.6万円
- 6412 Heiwa Holdings Inc.｜granville_tenkan｜✅順調｜⚪妥当｜FAIL_INSEN｜終値2135｜💰単元21.5万円｜📐進捗 遅れ -30.0%
- 3563 ＦＯＯＤ　＆　ＬＩＦＥ　ＣＯＭＰＡＮＩＥＳ｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_UWAHIGE｜終値6242｜💰単元62.4万円
- 4204 Sekisui Chemical Co., Ltd.｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_INSEN｜終値2645.5｜💰単元26.4万円｜📐進捗 上振れ 18.3%
- 4540 Tsumura & Co.｜granville_tenkan｜✅順調｜🟡やや割高｜PASS｜終値4006｜💰単元40.1万円｜momentum 逆指値4011 SL3765.6 上限4051.1 乖離0.1%・✅即時可｜⚠日程不明 📐進捗 上振れ 18.7%
  > 【業態】漢方薬特化で最大手。高齢者、がん患者、婦人処方薬を拡大。中国事業も。
  > 【いま】終値4,006円・直近5日+4.38%（材料未確認）
  > 【調子】✅順調（3/13）— 質注意・経常減益-9.1%・上方修正済み・🔼進捗先行
  > 【水準】🟡やや割高（2.0/7）— PER10.19倍・PEG—・52週55.4% ／ 💰単元40.1万円
  > 【戦略】当日高値超えの逆指値4011円で順張り参戦を検討。上限4051.1円・SL3765.6円目安
- 6745 ホーチキ｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_INSEN｜終値1956｜💰単元19.6万円｜📐進捗 上振れ 23.9%
- 9045 Keihan Holdings Co., Ltd.｜granville_tenkan｜⚠減速｜🟡やや割高｜FAIL_INSEN｜終値3339｜💰単元34.1万円｜📐進捗 上振れ 18.8%
- 8801 三井不動産｜granville_tenkan｜➖横ばい｜⚪妥当｜FAIL_INSEN｜終値1572.5｜💰単元16.2万円｜📐進捗 遅れ -16.9%
- 9837 Morito Co., Ltd.｜granville_tenkan｜➖横ばい｜⚪妥当｜FAIL_INSEN｜終値1776｜💰単元18.0万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 6072 ERTH Group Co.,Ltd.｜granville_tenkan｜🔻悪化｜🟡やや割高｜PASS_DOJI｜終値1087｜💰単元10.9万円｜⛔提案なし(材料後出し)｜⚡材料後出し ⚠業績基調が下向き（🔻悪化）
  > 【業態】地盤解析や品質証明の請負。工事は担わない。FC展開。個人住宅に進出。
  > 【いま】終値1,087円・直近5日-6.62%・📌その他重要開示2026年11月12日開催決算説明会のアーカイブ動画の公開及びいただいたご質問に対するご回答のお知らせ
  > 【調子】🔻悪化（2/13）— E軸判定不能(進捗データ不足)・質注意
  > 【水準】🟡やや割高（2.8/7）— PER—倍・PEG—・52週51.4% ／ 💰単元10.9万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 5105 ＴＯＹＯ　ＴＩＲＥ｜granville_tenkan｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜終値4011｜💰単元41.1万円
- 5233 太平洋セメント｜granville_tenkan｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜終値3868｜💰単元39.8万円｜📐進捗 上振れ 14.1%
- 8803 Heiwa Real Estate Co., Ltd.｜granville_tenkan｜➖横ばい｜🟡やや割高｜FAIL_INSEN｜終値2361｜💰単元23.6万円
- 4528 ONO Pharmaceutical Co., Ltd.｜granville_tenkan｜⚠減速｜🔴過熱｜PASS｜終値2489｜💰単元24.9万円｜momentum 逆指値2497.5 SL2346.7 上限2522.5 乖離0.3%・✅即時可｜⚠日程不明 ⚠業績基調が下向き（⚠減速）
  > 【業態】製薬準大手。自社開発多いが特許切れ比率高。がん新薬「オプジーボ」拡大。
  > 【いま】終値2,489円・直近5日+2.68%（材料未確認）
  > 【調子】⚠減速（2/13）— 税引前代替・A成長率0以下のためレバレッジ計算不可(C=0)・E軸:進捗62.1%>=前年同期56.3%・減収・⚠減速
  > 【水準】🔴過熱（1.0/7）— PER16.48倍・PEG11.347・52週73.0% ／ 💰単元24.9万円
  > 【戦略】当日高値超えの逆指値2497.5円で順張り参戦を検討。上限2522.5円・SL2346.7円目安
- 9869 Kato Sangyo Co., Ltd.｜granville_tenkan｜➖横ばい｜🔴過熱｜FAIL_INSEN｜終値6730｜💰単元67.4万円
- 4922 コーセーホールディングス｜granville_tenkan｜➖横ばい｜🔴過熱｜FAIL_INSEN｜終値6038｜💰単元62.2万円
- 9735 セコム｜granville_tenkan｜➖横ばい｜🔴過熱｜FAIL_UWAHIGE｜終値7193｜💰単元71.0万円｜📐進捗 上振れ 16.0%
- 6328 Ebara Jitsugyo Co., Ltd.｜granville_tenkan｜⚠減速｜⚪妥当｜FAIL_UWAHIGE｜終値2300｜💰単元22.9万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 4912 ライオン｜granville_tenkan｜⚠減速｜⚪妥当｜FAIL_UWAHIGE｜終値2232.5｜💰単元22.6万円｜⚡材料後出し
- 9025 Konoike Transport Co., Ltd.｜granville_tenkan｜⚠減速｜⚪妥当｜FAIL_INSEN｜終値2945｜💰単元29.7万円｜⚡材料後出し
- 9404 Nippon Television Holdings, Inc.｜granville_tenkan｜🔻悪化｜⚪妥当｜PASS｜終値2937.5｜💰単元29.4万円｜momentum 逆指値2950 SL2772.1 上限2979.5 乖離0.4%・⏸位置不適(25MA下 -1.85%／52週 20.1%)｜⚠日程不明 ⚠業績基調が下向き（🔻悪化）
  > 【業態】読売グループの民放大手。視聴率でトップ争い。動画配信「Hulu」、フィットネスも。
  > 【いま】終値2,938円・直近5日+3.03%（材料未確認）
  > 【調子】🔻悪化（1/13）— 経常減益-28.1%・質注意
  > 【水準】⚪妥当（3.0/7）— PER13.90倍・PEG—・52週20.1% ／ 💰単元29.4万円
  > 【戦略】当日高値超えの逆指値2950円で順張り参戦を検討。上限2979.5円・SL2772.1円目安
- 1878 Daito Trust Construction Co., Ltd.｜granville_tenkan｜⚠減速｜🟡やや割高｜FAIL_INSEN｜終値3318｜💰単元33.1万円
- 1928 積水ハウス｜granville_tenkan｜⚠減速｜🟡やや割高｜FAIL_INSEN｜終値3552｜💰単元35.8万円｜📋カルテ窓 12/10(残15営業日) 📐進捗 上振れ 19.0%
- 4552 JCR Pharmaceuticals Co., Ltd.｜granville_tenkan｜🔻悪化｜🔴過熱｜FAIL_UWAHIGE｜終値496｜💰単元5.0万円｜📑TOPIX低減対象（次 01/29 第2回/8） 📐進捗 遅れ -15.4% ⚡材料後出し
- 8167 リテールパートナーズ｜granville_tenkan｜⚠減速｜🟡やや割高｜FAIL_INSEN｜終値1376｜💰単元13.8万円｜📑TOPIX低減対象（次 01/29 第2回/8） 📐進捗 遅れ -18.2%
- 9401 東京放送ホールディングス｜granville_tenkan｜⚠減速｜🔴過熱｜FAIL_UWAHIGE｜終値6284｜💰単元63.0万円｜📐進捗 遅れ -18.1%
- 2267 Yakult Honsha Co., Ltd.｜granville_tenkan｜⚠減速｜🔴過熱｜FAIL_UWAHIGE｜終値2893.5｜💰単元29.2万円
- 3401 Teijin Limited｜granville_tenkan｜業績データ取得不可(経常益予想非開示)｜🟢値頃｜FAIL_INSEN｜終値1722｜💰単元17.6万円
- 4375 セーフィー｜changepoint/granville_tenkan/changepoint🔔｜取得不可｜🟢値頃｜FAIL_INSEN｜終値612｜💰単元6.1万円
- 2897 Nissin Foods Holdings Co., Ltd.｜granville_tenkan｜取得不可｜⚪妥当｜FAIL_INSEN｜終値2945.5｜💰単元29.9万円
- 3182 オイシックス｜granville_tenkan｜取得不可｜⚪妥当｜FAIL_INSEN｜終値1808｜💰単元18.6万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 2811 Kagome Co., Ltd.｜granville_tenkan｜業績データ取得不可(経常益予想非開示)｜⚪妥当｜FAIL_INSEN｜終値2844.5｜💰単元28.8万円
- 4543 Terumo Corporation｜granville_tenkan｜業績データ取得不可(経常益予想非開示)｜⚪妥当｜FAIL_UWAHIGE｜終値2534｜💰単元23.3万円
- 7921 ＴＡＫＡＲＡ　＆　ＣＯＭＰＡＮＹ｜granville_tenkan｜業績データ取得不可(経常益予想非開示)｜⚪妥当｜FAIL_INSEN｜終値4250｜💰単元43.0万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 1938 NIPPON RIETEC CO., LTD.｜granville_tenkan｜—｜—｜FAIL_INSEN｜終値2641｜💰単元—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 3252 JINUSHI Co.,Ltd.｜granville_tenkan｜—｜—｜FAIL_INSEN｜終値2846｜💰単元—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 4765 ＳＢＩグローバルアセットマネジメント｜granville_tenkan/granville_oshime｜判定保留｜⏸判定不能｜FAIL_INSEN｜終値602｜💰単元6.1万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 5930 Bunka Shutter Co., Ltd.｜granville_tenkan｜—｜－未評価（次回①-9で算定）｜PASS｜終値1900｜💰単元19.0万円｜momentum 逆指値1901 SL1786 上限1920 乖離0.1%・✅即時可｜⚠日程不明
  > 【業態】シャッター2位。住宅・ビル用を展開。メンテ・リフォーム、エコ・防災に重点。不二サッシと協業。
  > 【いま】終値1,900円・直近5日+2.76%（材料未確認）
  > 【調子】—（—/13）
  > 【水準】－未評価（次回①-9で算定）（—/7）— PER—倍・PEG—・52週34.2% ／ 💰単元19.0万円
  > 【戦略】当日高値超えの逆指値1901円で順張り参戦を検討。上限1920.0円・SL1786円目安
- 9605 Toei Company, Ltd.｜granville_tenkan｜—｜—｜FAIL_UWAHIGE｜終値6150｜💰単元—
- 6570 Kyowa Corporation Co. Ltd.｜granville_oshime/granville_rebound｜🚀確変｜🟢値頃｜FAIL_INSEN｜終値3025｜💰単元31.9万円｜📐進捗 上振れ 28.1% ⚡材料後出し
- 7480 スズデン｜granville_rebound/granville_oshime｜🚀確変｜⚪妥当｜PASS｜終値3520｜💰単元35.2万円｜⛔型不一致(既に支持帯以下)｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】FA機器主力、技術商社。オムロンと特約店契約。電設資材中心。ネット販売に強み。
  > 【いま】終値3,520円・直近5日-1.12%（材料未確認）
  > 【調子】🚀確変（13/13）— 🔼加速
  > 【水準】⚪妥当（4.0/7）— PER13.99倍・PEG0.122・52週80.3% ／ 💰単元35.2万円
  > 【戦略】発注対象外（⛔型不一致(既に支持帯以下)）
- 6574 コンヴァノ｜granville_oshime｜🚀確変｜🟢値頃｜FAIL_INSEN｜終値941｜💰単元9.8万円｜📐進捗 遅れ -65.4%
- 3156 レスター｜granville_oshime/granville_rebound｜🚀確変｜💎割安｜PASS_DOJI｜終値4380｜💰単元43.8万円｜momentum 逆指値4490 SL4185 上限4534.9 乖離2.5%・⏳確認足待ち｜📐進捗 上振れ 11.1% ⚠市場に劣後 RS20 -21.0pt ⚠1単元でリスク枠超過（30,500円）
  > 【業態】UKCHDとバイテックHD統合、エレクトロニクス総合商社。半導体、電子機器・部品、エネルギー。
  > 【いま】終値4,380円・直近5日-16.57%（材料未確認）
  > 【調子】🚀確変（11/13）— 進捗モデル値域外・上方修正済み・突出ボーナス・🔼加速・🔼進捗先行
  > 【水準】💎割安（6.0/7）— PER8.21倍・PEG0.096・52週43.1% ／ 💰単元43.8万円
  > 【戦略】当日高値超えの逆指値4490円で順張り参戦を検討。上限4534.9円・SL4185円目安／⚠1単元リスク30,500円（枠超過）
- 9824 Senshu Electric Co., Ltd.｜granville_oshime｜🔥絶好調｜⚪妥当｜PASS｜終値7590｜💰単元75.9万円｜⛔型不一致(既に支持帯以下)｜📋カルテ窓 12/08(残13営業日)
  > 【業態】電線専門商社。FA・機器・通信・電力向け電線、光ファイバーが軸。即納制に強み。
  > 【いま】終値7,590円・直近5日-3.07%（材料未確認）
  > 【調子】🔥絶好調（10/13）
  > 【水準】⚪妥当（4.0/7）— PER14.13倍・PEG0.351・52週75.2% ／ 💰単元75.9万円
  > 【戦略】発注対象外（⛔型不一致(既に支持帯以下)）
- 8051 山善｜granville_oshime｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜終値1812｜💰単元17.9万円｜📐進捗 上振れ 31.6%
- 8137 サンワテクノス｜granville_oshime/granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜終値3760｜💰単元37.1万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 4258 AMIYA Corporation｜granville_oshime/granville_rebound｜🔥絶好調｜⚪妥当｜PASS｜終値4950｜💰単元49.5万円｜⛔型不一致(既に支持帯以下)
  > 【業態】情報・通信業
  > 【いま】終値4,950円・直近5日-16.95%（材料未確認）
  > 【調子】🔥絶好調（9/13）— 上方修正済み・⚠下期依存
  > 【水準】⚪妥当（3.0/7）— PER39.76倍・PEG1.052・52週49.2% ／ 💰単元49.5万円
  > 【戦略】発注対象外（⛔型不一致(既に支持帯以下)）
- 3106 倉敷紡績｜granville_oshime｜🔥絶好調｜💎割安｜FAIL_INSEN｜終値2027｜💰単元20.1万円｜📐進捗 上振れ 25.2%
- 8388 阿波銀行｜granville_rebound/granville_oshime｜🔥絶好調｜💎割安｜FAIL_INSEN｜終値1770｜💰単元18.0万円
- 8392 大分銀行｜granville_rebound/granville_oshime｜🔥絶好調｜💎割安｜FAIL_INSEN｜終値2466｜💰単元24.8万円
- 9304 澁澤倉庫｜granville_oshime｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜終値1892｜💰単元18.9万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 153A Caulis, Inc.｜granville_oshime｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜終値2511｜💰単元20.7万円
- 3968 セグエグループ｜granville_oshime｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜終値791｜💰単元9.0万円｜📐進捗 上振れ 13.4%
- 4443 Ｓａｎｓａｎ｜changepoint🔔/granville_oshime｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜終値1977｜💰単元21.2万円
- 5985 SUNCALL CORPORATION｜granville_oshime｜⚡好調｜💎割安｜FAIL_UWAHIGE｜終値1563｜💰単元14.8万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 3673 ブロードリーフ｜granville_oshime｜⚡好調｜💎割安｜FAIL_INSEN｜終値321｜💰単元3.3万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 3040 ソリトンシステムズ｜granville_oshime/granville_rebound｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜終値2522｜💰単元24.3万円｜📑TOPIX低減対象（次 01/29 第2回/8） 📐進捗 上振れ 37.3%
- 5892 ＹＵＴＯＲＩ｜granville_oshime｜⚡好調｜🟢値頃｜FAIL_INSEN｜終値2360｜💰単元24.2万円｜📐進捗 上振れ 46.3%
- 8159 Tachibana Eletech Co., Ltd.｜granville_oshime｜⚡好調｜🟢値頃｜FAIL_INSEN｜終値4290｜💰単元43.5万円｜📐進捗 上振れ 33.1%
- 7970 Shin-Etsu Polymer Co., Ltd.｜granville_oshime｜⚡好調｜⚪妥当｜PASS｜終値2412｜💰単元24.1万円｜oshime 指値2399 SL2387.5 乖離-0.5%・⏸位置不適(25日線 下向き -0.66%)｜⚠日程不明
  > 【業態】信越化学系樹脂加工メーカー。ウエハ容器が主力。車載タッチスイッチや住生活資材も。
  > 【いま】終値2,412円・直近5日-1.27%（材料未確認）
  > 【調子】⚡好調（7/13）— E軸:進捗50.7%<前年同期51.7%・🔼加速
  > 【水準】⚪妥当（3.0/7）— PER16.44倍・PEG0.577・52週75.4% ／ 💰単元24.1万円
  > 【戦略】2399円までの押し目を指値で待つ。SL2387.5円（25日線基準）
- 8410 Seven Bank, Ltd.｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値349.5｜💰単元3.6万円
- 2492 インフォマート（インフォＭＴ）｜granville_oshime｜⚡好調｜🟡やや割高｜FAIL_INSEN｜終値702｜💰単元7.2万円
- 456A Human Made Inc.｜granville_oshime｜⚡好調｜🟡やや割高｜FAIL_INSEN｜終値1851｜💰単元19.6万円｜📋カルテ窓 12/11(残16営業日) 📐進捗 上振れ 14.7%
- 7678 ASAKUMA CO.,LTD.｜granville_oshime｜⚡好調｜🔴過熱｜FAIL_INSEN｜終値4120｜💰単元44.4万円｜📋カルテ窓 12/09(残14営業日)
- 4674 クレスコ｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値1881｜💰単元19.1万円｜📐進捗 遅れ -12.4%
- 2384 ＳＢＳホールディングス｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値5640｜💰単元56.5万円｜📐進捗 上振れ 13.7%
- 4498 Cybertrust Japan Co.Ltd.｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜終値1697｜💰単元15.5万円｜📐進捗 上振れ 21.7%
- 4475 None｜changepoint🔔🔔/granville_oshime｜⚡好調｜🟡やや割高｜FAIL_INSEN｜終値2367｜💰単元22.4万円
- 4398 ブロードバンドセキュリティ｜granville_oshime/granville_rebound｜⚡好調｜🟢値頃｜FAIL_INSEN｜終値2041｜💰単元19.7万円｜📐進捗 遅れ -14.8%
- 338A ZenmuTech,Inc.｜granville_oshime/granville_rebound｜⚡好調｜⚪妥当｜PASS｜終値3350｜💰単元33.5万円｜⛔型不一致(既に支持帯以下)｜📐進捗 遅れ -25.4%
  > 【業態】暗号技術を応用したセキュリティ技術開発・販売など情報漏洩対策を手掛ける。
  > 【いま】終値3,350円・直近5日+4.04%（材料未確認）
  > 【調子】⚡好調（5/13）— E軸判定不能(進捗データ不足)・質注意・勢い判定矛盾
  > 【水準】⚪妥当（4.0/7）— PER30.23倍・PEG2.419・52週37.0% ／ 💰単元33.5万円
  > 【戦略】発注対象外（⛔型不一致(既に支持帯以下)）
- 9536 SAIBU GAS HOLDINGS CO. LTD.｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値2873｜💰単元29.2万円
- 436A サイバーソリューションズ（サイバＳＯＬ）｜granville_oshime｜⚡好調｜⚪妥当｜PASS｜終値1818｜💰単元18.2万円｜oshime 指値1737 SL1728.4 乖離-4.5%・⏸位置不適(25日線 下向き -2.92%)｜📋カルテ窓 12/04(残11営業日)
  > 【業態】法人向けクラウドメールサービス等コミュニケーションツールやサイバーセキュリティ事業を展開。
  > 【いま】終値1,818円・直近5日+4.90%（材料未確認）
  > 【調子】⚡好調（5/13）— D軸判定不能(四半期不足)・E軸判定不能(進捗データ不足)
  > 【水準】⚪妥当（3.0/7）— PER24.05倍・PEG1.193・52週66.0% ／ 💰単元18.2万円
  > 【戦略】1737円までの押し目を指値で待つ。SL1728.4円（25日線基準）
- 3042 セキュアヴェイル（セキュアヴェ）｜granville_oshime｜⚡好調｜🟡やや割高｜PASS｜終値783｜💰単元7.8万円｜⛔型不一致(既に支持帯以下)
  > 【業態】情報セキュリティの設計・構築・監視、ログ分析サービス。24時間有人対応。
  > 【いま】終値783円・直近5日-13.38%（材料未確認）
  > 【調子】⚡好調（5/13）— 進捗モデル値域外・⚠減速・⚠進捗遅れ・⚠下期依存
  > 【水準】🟡やや割高（2.0/7）— PER60.70倍・PEG3.035・52週32.0% ／ 💰単元7.8万円
  > 【戦略】発注対象外（⛔型不一致(既に支持帯以下)）
- 4373 Simplex Holdings,Inc.｜granville_oshime｜⚡好調｜🟡やや割高｜FAIL_INSEN｜終値1152｜💰単元12.0万円
- 6877 ＯＢＡＲＡ　ＧＲＯＵＰ（ＯＢＡＲＡＧ）｜granville_oshime｜⚡好調｜🟡やや割高｜FAIL_INSEN｜終値7280｜💰単元72.5万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 8395 佐賀銀行｜granville_oshime/granville_rebound｜⚠減速｜🟢値頃｜FAIL_INSEN｜終値5690｜💰単元57.6万円
- 5036 日本ビジネスシステムズ｜granville_oshime｜✅順調｜⚪妥当｜FAIL_INSEN｜終値1418｜💰単元14.8万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 6080 Ｍ＆Ａキャピタルパートナーズ｜changepoint/changepoint🔔/granville_oshime/changepoint🔔🔔｜✅順調｜🟡やや割高｜FAIL_INSEN｜終値4275｜💰単元44.9万円
- 9552 クオンツ総研ホールディングス｜granville_oshime｜✅順調｜🟡やや割高｜FAIL_INSEN｜終値1114｜💰単元11.8万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 3762 テクマトリックス（テクマト）｜granville_oshime｜✅順調｜🔴過熱｜FAIL_INSEN｜終値3015｜💰単元31.4万円
- 9509 Hokkaido Electric Power Company,Incorporated｜granville_oshime｜🔻悪化｜⚪妥当｜FAIL_INSEN｜終値1095.5｜💰単元10.9万円｜📐進捗 遅れ -32.9%
- 3692 ＦＦＲＩセキュリティ｜granville_oshime｜➖横ばい｜🟡やや割高｜FAIL_UWAHIGE｜終値6400｜💰単元60.7万円｜📐進捗 遅れ -28.3%
- 336A ダイナミックマッププラットフォーム｜granville_oshime｜取得不可｜⚪妥当｜FAIL_INSEN｜終値1172｜💰単元11.7万円
- 3697 SHIFT, Inc.｜granville_oshime｜業績データ取得不可(経常益予想非開示)｜⚪妥当｜FAIL_INSEN｜終値1028｜💰単元10.7万円
- 6027 Bengo4.com, Inc.｜granville_oshime｜取得不可｜⚪妥当｜FAIL_INSEN｜終値4090｜💰単元44.8万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 6191 エボラブルアジア｜granville_oshime｜取得不可｜⚪妥当｜FAIL_INSEN｜終値1565｜💰単元15.7万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 4432 ウイングアーク１ｓｔ｜granville_oshime｜業績データ取得不可(経常益予想非開示)｜🟡やや割高｜FAIL_INSEN｜終値3455｜💰単元35.2万円
- 2326 Digital Arts Inc.｜granville_oshime｜—｜－未評価（次回①-9で算定）｜PASS｜終値5460｜💰単元54.6万円｜⛔型不一致(既に支持帯以下)｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】有害情報遮断フィルタリングソフトで国内首位。公共・教育機関、企業向け強化。
  > 【いま】終値5,460円・直近5日+1.49%（材料未確認）
  > 【調子】—（—/13）
  > 【水準】－未評価（次回①-9で算定）（—/7）— PER—倍・PEG—・52週51.6% ／ 💰単元54.6万円
  > 【戦略】発注対象外（⛔型不一致(既に支持帯以下)）
- 3547 UNISIA HOLDINGS CO.｜granville_oshime｜—｜—｜FAIL_INSEN｜終値1925｜💰単元—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 4686 JUSTSYSTEMS CORPORATION｜granville_oshime｜—｜—｜FAIL_INSEN｜終値4705｜💰単元—
- 6490 ＰＩＬＬＡＲ｜granville_rebound｜🚀確変｜🟢値頃｜PASS｜終値9400｜💰単元94.0万円｜⛔提案なし(指名鮮度切れ 17営業日)
  > 【業態】流体制御関連のメカニカルシール大手。パッキン、ガスケットなど産業機械向け拡大。
  > 【いま】終値9,400円・直近5日-1.57%（材料未確認）
  > 【調子】🚀確変（13/13）— 突出ボーナス・🔼加速
  > 【水準】🟢値頃（5.0/7）— PER13.11倍・PEG0.161・52週57.9% ／ 💰単元94.0万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 17営業日)）
- 4937 Waqoo Inc.｜granville_rebound｜🚀確変｜⚪妥当｜FAIL_INSEN｜終値1983｜💰単元23.1万円
- 6862 ミナト HD｜granville_rebound｜🚀確変｜💎割安｜FAIL_INSEN｜終値3010｜💰単元29.1万円｜📐進捗 上振れ 33.9%
- 5027 AnyMind Group Inc.｜granville_rebound｜🚀確変｜⚪妥当｜FAIL_INSEN｜終値584｜💰単元7.2万円｜📐進捗 上振れ 11.2%
- 3851 日本一ソフトウェア｜granville_rebound｜🚀確変｜💎割安｜FAIL_INSEN｜終値887｜💰単元9.2万円｜📐進捗 上振れ 51.0%
- 3891 ニッポン高度紙工業｜granville_rebound｜🚀確変｜💎割安｜FAIL_INSEN｜終値5360｜💰単元52.2万円｜📐進捗 遅れ -10.4%
- 6138 ダイジェット工業（ダイジェト）｜granville_rebound｜🚀確変｜💎割安｜FAIL_INSEN｜終値1623｜💰単元17.3万円｜📐進捗 上振れ 10.1%
- 4419 Finatext Holdings Ltd.｜granville_rebound/changepoint🔔/changepoint｜🚀確変｜🟢値頃｜FAIL_INSEN｜終値1023｜💰単元10.7万円｜📐進捗 遅れ -41.1%
- 5381 Mipox Corp.｜granville_rebound｜🚀確変｜🟢値頃｜FAIL_UWAHIGE｜終値873｜💰単元8.5万円｜📐進捗 上振れ 26.1%
- 2962 テクニスコ｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜終値1201｜💰単元11.8万円｜📐進捗 遅れ -37.1%
- 4968 Arakawa Chemical Industries,Ltd.｜granville_rebound｜🔥絶好調｜🟢値頃｜PASS｜終値1834｜💰単元18.3万円｜reversal 指値1834 SL1696・✅即時可｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8） 📐進捗 上振れ 78.5%
  > 【業態】化学（ファインケミカル・接着剤・製紙関連）
  > 【いま】終値1,834円・直近5日-6.86%（材料未確認）
  > 【調子】🔥絶好調（10/13）— 上方修正済み・突出ボーナス・🔼加速・🔼進捗先行
  > 【水準】🟢値頃（5.0/7）— PER11.37倍・PEG0.159・52週47.6% ／ 💰単元18.3万円
  > 【戦略】当日終値1834円の指値で反転を取りにいく。SL1696円（直近5日安値）
- 6317 Kitagawa Corporation｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜終値2729｜💰単元27.9万円｜📑TOPIX低減対象（次 01/29 第2回/8） 📐進捗 上振れ 78.2%
- 7713 Sigma Koki Co., Ltd.｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜終値2560｜💰単元28.9万円
- 8364 清水銀行｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜終値2560｜💰単元25.8万円｜📑TOPIX低減対象（次 01/29 第2回/8） 📐進捗 上振れ 14.4%
- 1436 GreenEnergy & Company｜granville_rebound｜🔥絶好調｜💎割安｜FAIL_INSEN｜終値1195｜💰単元12.9万円｜📋カルテ窓 12/08(残13営業日)
- 479A PRONI Inc.｜granville_rebound/changepoint🔔｜🔥絶好調｜💎割安｜FAIL_INSEN｜終値995｜💰単元10.2万円｜📐進捗 遅れ -24.9%
- 2489 アドウェイズ｜granville_rebound｜⚠減速｜💎割安｜FAIL_INSEN｜終値309｜💰単元3.2万円｜📑TOPIX低減対象（次 01/29 第2回/8） 📐進捗 上振れ 93.0%
- 3793 Drecom Co., Ltd.｜granville_rebound｜⚠減速｜💎割安｜FAIL_INSEN｜終値428｜💰単元4.3万円｜📐進捗 上振れ 25.6%
- 7609 Daitron Co., Ltd.｜granville_rebound｜🔥絶好調｜💎割安｜PASS｜終値3770｜💰単元37.7万円｜reversal 指値3770 SL3450・✅即時可｜⚠日程不明 📐進捗 上振れ 26.2% ⚠1単元でリスク枠超過（32,000円）
  > 【業態】電子部品卸中堅。製造装置にも強み。スイッチ電源など自社製造製品に注力。
  > 【いま】終値3,770円・直近5日+0.00%（材料未確認）
  > 【調子】🔥絶好調（9/13）— 上方修正済み・🔼進捗先行
  > 【水準】💎割安（6.0/7）— PER11.29倍・PEG0.337・52週57.1% ／ 💰単元37.7万円
  > 【戦略】当日終値3770円の指値で反転を取りにいく。SL3450円（直近5日安値）／⚠1単元リスク32,000円（枠超過）
- 7715 長野計器｜granville_rebound｜🔥絶好調｜💎割安｜FAIL_UWAHIGE｜終値3130｜💰単元30.8万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 5256 Fusic Co.,Ltd.｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜終値2499｜💰単元25.8万円｜📐進捗 遅れ -66.0%
- 150A ＪＳＨ｜granville_rebound｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜終値832｜💰単元8.5万円
- 6840 ＡＫＩＢＡホールディングス｜granville_rebound｜🔥絶好調｜💎割安｜FAIL_INSEN｜終値569｜💰単元5.6万円｜📐進捗 上振れ 42.5%
- 4100 Toda Kogyo Corp.｜granville_rebound｜🔥絶好調｜💎割安｜FAIL_UWAHIGE｜終値1575｜💰単元15.4万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 7256 河西工業｜granville_rebound｜🔥絶好調｜💎割安｜FAIL_INSEN｜終値364｜💰単元3.8万円｜📐進捗 上振れ 13.9%
- 460A ＢＲＡＮＵ｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜終値1037｜💰単元10.2万円｜📋カルテ窓 12/14(残17営業日) 📐進捗 上振れ 10.8%
- 5033 Nulab Inc.｜granville_rebound｜🔥絶好調｜⚪妥当｜PASS｜終値1155｜💰単元11.6万円｜⛔提案なし(材料後出し)｜📐進捗 遅れ -19.6% ⚡材料後出し
  > 【業態】クラウドサービス開発・提供。プロジェクト管理「Backlog」が柱。作図共有ツールも。
  > 【いま】終値1,155円・直近5日-6.48%・📌その他重要開示当社サービス「Cacoo」における不正アクセスに関する現在の状況について（第二報）
  > 【調子】🔥絶好調（8/13）— E軸:進捗48.3%<前年同期61.8%・突出ボーナス・⚠進捗遅れ
  > 【水準】⚪妥当（4.0/7）— PER15.20倍・PEG0.204・52週74.1% ／ 💰単元11.6万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 4431 Smaregi, Inc.｜granville_rebound｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜終値3080｜💰単元32.1万円｜📋カルテ窓 12/15(残18営業日)
- 5252 日本ナレッジ｜granville_rebound｜🔥絶好調｜🟡やや割高｜FAIL_INSEN｜終値995｜💰単元9.7万円
- 6508 Meidensha Corporation｜granville_rebound｜⚡好調｜💎割安｜FAIL_INSEN｜終値6993｜💰単元68.7万円
- 5367 Nikkato Corporation｜granville_rebound｜⚡好調｜🟢値頃｜PASS｜終値988｜💰単元9.9万円｜⛔提案なし(指名鮮度切れ 12営業日)｜⚠日程不明 📐進捗 上振れ 52.0%
  > 【業態】工業用セラミックス中堅。耐摩耗・耐熱など高付加価値品に強み。エンジニアリングも。
  > 【いま】終値988円・直近5日-8.18%（材料未確認）
  > 【調子】⚡好調（7/13）— 上方修正済み・🔼進捗先行
  > 【水準】🟢値頃（5.0/7）— PER13.14倍・PEG1.046・52週27.0% ／ 💰単元9.9万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 12営業日)）
- 6742 京三製作所｜granville_rebound｜⚡好調｜🟢値頃｜FAIL_INSEN｜終値853｜💰単元8.5万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 8344 Yamagata Bank, Ltd.｜granville_rebound｜⚡好調｜🟢値頃｜FAIL_INSEN｜終値3910｜💰単元39.4万円｜📐進捗 上振れ 19.2%
- 9697 カプコン｜granville_rebound｜⚡好調｜🔴過熱｜PASS｜終値4517｜💰単元45.2万円｜⛔提案なし(指名鮮度切れ 14営業日)｜⚠日程不明
  > 【業態】家庭用ゲームソフト大手。「モンハン」「戦国BASARA」等人気作品多数。SNS向け拡大。
  > 【いま】終値4,517円・直近5日+2.92%（材料未確認）
  > 【調子】⚡好調（7/13）
  > 【水準】🔴過熱（0.0/7）— PER32.59倍・PEG2.725・52週89.5% ／ 💰単元45.2万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 14営業日)）
- 477A Startline CO.,LTD.｜granville_rebound｜⚡好調｜💎割安｜FAIL_INSEN｜終値537｜💰単元5.5万円｜📐進捗 遅れ -48.3% ⚡材料後出し
- 4040 NANKAI CHEMICAL COMPANY LIMITED｜granville_rebound｜⚡好調｜💎割安｜FAIL_INSEN｜終値3760｜💰単元38.4万円｜📐進捗 上振れ 20.1%
- 3850 INTRAMART CORPORATION｜granville_rebound｜⚡好調｜🟢値頃｜FAIL_INSEN｜終値3190｜💰単元32.2万円｜📐進捗 上振れ 46.6%
- 6947 図研｜granville_rebound｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値5080｜💰単元52.2万円｜📐進捗 上振れ 23.2%
- 6958 日本シイエムケイ｜granville_rebound｜⚡好調｜⚪妥当｜PASS｜終値698｜💰単元7.0万円｜reversal 指値698 SL668・✅即時可｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8） 📐進捗 遅れ -42.9%
  > 【業態】プリント配線板の最大手。自動車、電機向けが主力。高付加価値品強化。
  > 【いま】終値698円・直近5日-6.56%（材料未確認）
  > 【調子】⚡好調（6/13）— ⚠進捗遅れ
  > 【水準】⚪妥当（3.0/7）— PER16.58倍・PEG1.216・52週61.8% ／ 💰単元7.0万円
  > 【戦略】当日終値698円の指値で反転を取りにいく。SL668円（直近5日安値）
- 7826 フルヤ金属｜granville_rebound｜⚡好調｜⚪妥当｜PASS_DOJI｜終値8050｜💰単元80.5万円｜momentum 逆指値8250 SL7650 上限8332.5 乖離2.5%・⏳確認足待ち｜⚠日程不明 📐進捗 上振れ 14.6% ⚠市場に劣後 RS20 -11.4pt ⚠1単元でリスク枠超過（60,000円）
  > 【業態】白金・レアメタルなど貴金属の製造・加工・回収。精製・改鋳、薄膜技術に強み。
  > 【いま】終値8,050円・直近5日-11.05%（材料未確認）
  > 【調子】⚡好調（6/13）— 🔼進捗先行
  > 【水準】⚪妥当（3.0/7）— PER11.19倍・PEG2.066・52週54.0% ／ 💰単元80.5万円
  > 【戦略】当日高値超えの逆指値8250円で順張り参戦を検討。上限8332.5円・SL7650円目安／⚠1単元リスク60,000円（枠超過）
- 7213 LECIP Holdings Corporation｜granville_rebound｜⚡好調｜💎割安｜FAIL_INSEN｜終値579｜💰単元5.8万円｜⚡材料後出し
- 4667 Aisan Technology Co.,Ltd.｜granville_rebound/changepoint/changepoint🔔｜⚡好調｜🟢値頃｜FAIL_INSEN｜終値658｜💰単元6.6万円｜📐進捗 遅れ -93.8%
- 6904 Harada Industry Co., Ltd.｜granville_rebound｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値639｜💰単元6.9万円｜📐進捗 上振れ 51.4%
- 9278 BOOKOFF GROUP HOLDINGS LIMITED｜granville_rebound｜⚡好調｜🟡やや割高｜FAIL_INSEN｜終値2453｜💰単元26.0万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 3763 Pro-Ship Incorporated｜granville_rebound｜⚡好調｜🔴過熱｜FAIL_INSEN｜終値1827｜💰単元21.0万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 4025 多木化学｜granville_rebound｜✅順調｜⚪妥当｜PASS｜終値5490｜💰単元54.9万円｜reversal 指値5490 SL5210・✅即時可｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8） 📐進捗 上振れ 31.9%
  > 【業態】人造肥料の草分けで化学肥料大手。水処理薬、機能性素材や商業施設も。
  > 【いま】終値5,490円・直近5日+2.43%（材料未確認）
  > 【調子】✅順調（4/13）— 上方修正済み・🔼進捗先行
  > 【水準】⚪妥当（3.0/7）— PER13.09倍・PEG1.547・52週69.3% ／ 💰単元54.9万円
  > 【戦略】当日終値5490円の指値で反転を取りにいく。SL5210円（直近5日安値）
- 428A Cypress Holdings Co., Ltd.｜granville_rebound｜✅順調｜⚪妥当｜FAIL_INSEN｜終値1334｜💰単元14.9万円
- 3371 ソフトクリエイトホールディングス｜granville_rebound｜✅順調｜🟡やや割高｜FAIL_INSEN｜終値1985｜💰単元20.5万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 278A Ｔｅｒｒａ　Ｄｒｏｎｅ｜granville_rebound｜✅順調｜⏸判定不能｜PASS｜終値5220｜💰単元—｜⛔提案なし(指名鮮度切れ 16営業日)｜📋カルテ窓 12/15(残18営業日)
  > 【業態】測量・点検・農業におけるドローンを含むハード・ソフトの開発などを手掛ける。
  > 【いま】終値5,220円・直近5日-6.12%（材料未確認）
  > 【調子】✅順調（4/13）— 赤字ルート・E軸判定不能(進捗データ不足)
  > 【水準】⏸判定不能（—/7）— PER—倍・PEG—・52週39.4% ／ 💰単元—万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 16営業日)）
- 4396 System Support Holdings Inc.｜granville_rebound｜✅順調｜⚪妥当｜FAIL_UWAHIGE｜終値1274｜💰単元12.9万円｜📑TOPIX低減対象（次 01/29 第2回/8） 📐進捗 遅れ -47.2%
- 5599 S&J Corporation｜granville_rebound｜✅順調｜🟡やや割高｜PASS｜終値1515｜💰単元15.2万円｜reversal 指値1515 SL1365・✅即時可｜📐進捗 遅れ -20.2%
  > 【業態】サイバーセキュリティ対策専業。企業中心に監視・受託・コンサルティングサービスを手掛ける。
  > 【いま】終値1,515円・直近5日-3.93%（材料未確認）
  > 【調子】✅順調（3/13）— 質注意・⚠減速・⚠進捗遅れ・⚠下期依存
  > 【水準】🟡やや割高（2.0/7）— PER20.84倍・PEG2.570・52週37.3% ／ 💰単元15.2万円
  > 【戦略】当日終値1515円の指値で反転を取りにいく。SL1365円（直近5日安値）
- 6676 BUFFALO INC.｜granville_rebound｜⚠減速｜🟡やや割高｜FAIL_INSEN｜終値3175｜💰単元31.8万円｜📑TOPIX低減対象（次 01/29 第2回/8） 📐進捗 上振れ 57.6% ⚡材料後出し
- 3909 Showcase, Inc. (Japan)｜granville_rebound｜🔻悪化｜⚪妥当｜PASS_DOJI｜終値680｜💰単元6.8万円｜momentum 逆指値681 SL522 上限687.8 乖離0.1%・⏳確認足待ち｜⚠業績基調が下向き（🔻悪化）
  > 【業態】Webサイト最適化・DXクラウドサービス。広告・メディア事業も。リユース事業売却。AIFC傘下。
  > 【いま】終値680円・直近5日-9.09%（材料未確認）
  > 【調子】🔻悪化（2/13）— 4Q換算（変則決算）・赤字企業(経常赤字)・黒字→赤字転落・E軸判定不能(進捗データ不足)・減収・⚠進捗遅れ
  > 【水準】⚪妥当（4.0/7）— PER53.12倍・PEG0.328・52週49.8% ／ 💰単元6.8万円
  > 【戦略】当日高値超えの逆指値681円で順張り参戦を検討。上限687.8円・SL522円目安
- 6203 Howa Machinery, Ltd.｜granville_rebound｜⚠減速｜⚪妥当｜PASS_DOJI｜終値1722｜💰単元17.2万円｜⛔提案なし(指名鮮度切れ 21営業日)｜📐進捗 上振れ 76.3% ⚠業績基調が下向き（⚠減速）
  > 【業態】産業用機械の老舗。工作機械中心に特装車や防弾、火器など防衛機器も。
  > 【いま】終値1,722円・直近5日-14.84%（材料未確認）
  > 【調子】⚠減速（2/13）— A成長率0以下のためレバレッジ計算不可(C=0)・減収・🔼進捗先行
  > 【水準】⚪妥当（4.0/7）— PER19.15倍・PEG1.337・52週32.8% ／ 💰単元17.2万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 21営業日)）
- 4884 Kringle Pharma, Inc.｜granville_rebound｜⚠減速｜🔴過熱｜FAIL_INSEN｜終値525｜💰単元5.7万円｜⚡材料後出し
- 3858 Ubiquitous AI Corporation｜granville_rebound｜⚠減速｜💎割安｜FAIL_UWAHIGE｜終値405｜💰単元3.9万円
- 3565 Ascentech KK｜granville_rebound｜🔻悪化｜⚪妥当｜FAIL_INSEN｜終値425｜💰単元4.6万円｜📋カルテ窓 12/15(残18営業日) 📑TOPIX低減対象（次 01/29 第2回/8）
- 4240 Cluster Technology Co., Ltd.｜granville_rebound｜🔻悪化｜🟡やや割高｜FAIL_UWAHIGE｜終値506｜💰単元5.0万円
- 8360 Yamanashi Chuo Bank, Ltd.｜granville_rebound｜取得不可｜💎割安｜FAIL_INSEN｜終値1156｜💰単元11.7万円
- 8377 ほくほくフィナンシャルグループ｜granville_rebound｜業績データ取得不可(売上/経常欠損)｜💎割安｜FAIL_INSEN｜終値711.5｜💰単元7.2万円
- 3691 DIGITAL PLUS, Inc.｜granville_rebound｜取得不可｜🟢値頃｜FAIL_UWAHIGE｜終値1243｜💰単元12.5万円
- 8368 Hyakugo Bank, Ltd.｜granville_rebound｜業績データ取得不可(売上/経常欠損)｜🟢値頃｜FAIL_INSEN｜終値1942｜💰単元19.3万円
- 7380 Juroku Financial Group,Inc.｜granville_rebound｜業績データ取得不可(売上/経常欠損)｜⚪妥当｜FAIL_INSEN｜終値2193｜💰単元22.2万円
- 8551 北日本銀行｜granville_rebound｜取得不可｜⚪妥当｜FAIL_INSEN｜終値2124｜💰単元21.1万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 7184 富山第一銀行｜granville_rebound｜取得不可｜🟡やや割高｜FAIL_INSEN｜終値2838｜💰単元31.0万円
- 4075 ブレインズテクノロジー｜granville_rebound｜取得不可｜⏸判定不能｜FAIL_UWAHIGE｜終値1010｜💰単元9.9万円｜📋カルテ窓 12/11(残16営業日)
- 5133 Terilogy Holdings Corporation｜granville_rebound｜—｜—｜FAIL_UWAHIGE｜終値370｜💰単元—
- 6890 Ferrotec Corporation｜granville_rebound｜業績データ取得不可(売上/経常欠損)｜⏸判定不能｜FAIL_INSEN｜終値6910｜💰単元67.7万円｜📑TOPIX新規採用（2026-10-30 組入）
- 7175 Imamura Securities Co.Ltd.｜granville_rebound｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜終値1626｜💰単元16.2万円
- 8609 岡三証券グループ｜granville_rebound｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜終値980｜💰単元10.1万円
- 8739 スパークス・グループ｜granville_rebound｜業績データ取得不可｜⏸判定不能｜FAIL_UWAHIGE｜終値2427｜💰単元24.2万円｜📑TOPIX低減対象（次 01/29 第2回/8）

## 変化点銘柄
- 5803 Fujikura Ltd.｜changepoint🔔｜🚀確変｜💎割安｜FAIL_INSEN｜終値2605.5｜💰単元25.9万円｜🔒実弾封印中(PL3紙ログ収集中) 📐進捗 上振れ 30.1%
- 265A エイチエムコム｜changepoint/changepoint🔔｜🚀確変｜🟢値頃｜FAIL_UWAHIGE｜終値556｜💰単元5.5万円｜🔒実弾封印中(PL3紙ログ収集中) 📐進捗 上振れ 13.2%
- 4011 Headwaters Co.,Ltd｜changepoint🔔｜🚀確変｜🟢値頃｜FAIL_INSEN｜終値1648｜💰単元16.9万円｜🔒実弾封印中(PL3紙ログ収集中) 📐進捗 遅れ -19.4% ⚡材料後出し
- 7695 交換できるくん｜changepoint/changepoint🔔/changepoint🔔🔔｜🚀確変｜⚪妥当｜FAIL_INSEN｜終値881｜💰単元9.1万円｜🔒実弾封印中(PL3紙ログ収集中) 📐進捗 上振れ 11.2%
- 8151 東陽テクニカ｜changepoint🔔/changepoint🔔🔔｜⚡好調｜💎割安｜FAIL_INSEN｜終値1763｜💰単元17.5万円｜📑TOPIX低減対象（次 01/29 第2回/8） 🔒実弾封印中(PL3紙ログ収集中) ⚡材料後出し
- 593A Tier IV, Inc.｜changepoint🔔🔔/changepoint/changepoint🔔｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値1877｜💰単元19.6万円｜📑TOPIX新規採用（2026-10-30 組入） 🔒実弾封印中(PL3紙ログ収集中)
- 4488 AI inside Inc.｜changepoint🔔｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値1746｜💰単元17.5万円｜🔒実弾封印中(PL3紙ログ収集中) 📐進捗 上振れ 38.5%
- 9343 アイビス｜changepoint/changepoint🔔/changepoint🔔🔔｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値683｜💰単元6.9万円｜🔒実弾封印中(PL3紙ログ収集中) ⚡材料後出し
- 286A ユカリア｜changepoint🔔｜⚡好調｜💎割安｜FAIL_INSEN｜終値688｜💰単元7.2万円｜🔒実弾封印中(PL3紙ログ収集中) 📐進捗 遅れ -50.7%
- 218A Liberaware｜changepoint/changepoint🔔｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値738｜💰単元7.3万円｜📋カルテ窓 12/11(残16営業日) 🔒実弾封印中(PL3紙ログ収集中)
- 4483 JMDC｜changepoint🔔/changepoint🔔🔔｜⚡好調｜🔴過熱｜FAIL_INSEN｜終値3410｜💰単元36.9万円｜🔒実弾封印中(PL3紙ログ収集中)
- 3923 ラクス｜changepoint🔔🔔/changepoint🔔｜⚠減速｜⚪妥当｜FAIL_INSEN｜終値1019.5｜💰単元11.0万円｜🔒実弾封印中(PL3紙ログ収集中)
- 4165 PLAID Inc.｜changepoint🔔🔔｜✅順調｜🟡やや割高｜FAIL_INSEN｜終値449｜💰単元5.5万円｜🔒実弾封印中(PL3紙ログ収集中) 📐進捗 遅れ -10.5%
- 4259 ExaWizards Inc.｜changepoint/changepoint🔔/changepoint🔔🔔｜取得不可｜⚪妥当｜FAIL_INSEN｜終値525｜💰単元5.3万円｜🔒実弾封印中(PL3紙ログ収集中)
- 4478 freee K.K.｜changepoint/changepoint🔔/changepoint🔔🔔｜取得不可｜⚪妥当｜FAIL_INSEN｜終値3270｜💰単元35.4万円｜📑TOPIX新規採用（2026-10-30 組入） 🔒実弾封印中(PL3紙ログ収集中)
- 3989 シェアテク｜changepoint🔔｜業績データ取得不可(売上/経常欠損)｜⏸判定不能｜FAIL_INSEN｜終値1535｜💰単元15.5万円｜🔒実弾封印中(PL3紙ログ収集中)

## 🤖AI特需銘柄
波: wave_on なし／25MA 上回り率 エネマネ 0.0%・冷却 25.0%・光 0.0%・基板 2.38%（ai_scan 2026-11-18）
- 6777 santec｜ai_reversal/ai_momentum｜🚀確変｜🟢値頃｜FAIL_INSEN｜終値18030｜💰単元173.1万円｜📑TOPIX新規採用（2026-10-30 組入）
- 6613 QD Laser, Inc.｜granville_oshime/ai_momentum｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜終値1651｜💰単元16.1万円｜📑TOPIX新規採用（2026-10-30 組入） 📐進捗 上振れ 11.8%
- 4063 信越化学工業｜ai_momentum/ai_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値5535｜💰単元55.7万円
- 6988 日東電工｜ai_momentum/ai_reversal｜⚡好調｜🟡やや割高｜FAIL_INSEN｜終値3500｜💰単元35.4万円
- 6367 ダイキン工業｜ai_momentum｜✅順調｜🔴過熱｜FAIL_INSEN｜終値23040｜💰単元231.3万円
- 1975 新日本空調｜ai_momentum｜✅順調｜⚪妥当｜FAIL_INSEN｜終値3210｜💰単元31.9万円
- 3374 内外テック｜ai_reversal/granville_rebound｜🚀確変｜💎割安｜FAIL_INSEN｜終値3380｜💰単元33.2万円｜📐進捗 上振れ 59.2%
- 4047 関東電化工業｜ai_reversal｜🚀確変｜💎割安｜FAIL_INSEN｜終値1561｜💰単元15.4万円
- 6834 精工技研｜ai_reversal｜🚀確変｜💎割安｜FAIL_INSEN｜終値3860｜💰単元49.5万円｜📑TOPIX新規採用（2026-10-30 組入） 📐進捗 上振れ 24.0%
- 6407 CKD｜ai_reversal｜🚀確変｜💎割安｜FAIL_INSEN｜終値3911｜💰単元38.7万円｜📐進捗 上振れ 13.4%
- 6857 アドバンテスト｜ai_reversal｜🚀確変｜⚪妥当｜FAIL_INSEN｜終値27195｜💰単元306.1万円
- 5801 古河電気工業｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜終値1889.5｜💰単元18.7万円｜📐進捗 上振れ 31.9%
- 6787 メイコー｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜終値7840｜💰単元74.4万円｜📐進捗 遅れ -25.9%
- 8035 東京エレクトロン｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜終値8699｜💰単元86.6万円
- 6918 アバールデータ｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜終値2797｜💰単元27.8万円｜📐進捗 遅れ -17.0%
- 6524 湖北工業｜ai_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜終値4220｜💰単元41.3万円｜📐進捗 上振れ 13.8%
- 3110 日東紡｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜終値2392.5｜💰単元23.8万円｜📐進捗 上振れ 12.3%
- 4182 三菱ガス化学｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜終値3148｜💰単元31.3万円
- 4368 扶桑化学工業｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜終値2735｜💰単元26.9万円
- 6323 ローツェ｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜終値3114｜💰単元30.5万円｜📐進捗 遅れ -11.4%
- 6779 日本電波工業｜ai_reversal｜🔥絶好調｜💎割安｜PASS_DOJI｜終値1688｜💰単元16.9万円｜momentum 逆指値1714 SL1597 上限1731.1 乖離1.5%・⏳確認足待ち｜⚠日程不明 ⚠市場に劣後 RS20 -33.4pt
  > 【業態】水晶関連専業で世界大手。小型デバイス製品に力。国内、中国、マレーシアで生産。
  > 【いま】終値1,688円・直近5日-14.92%（材料未確認）
  > 【調子】🔥絶好調（9/13）— 税引前代替・上方修正済み
  > 【水準】💎割安（6.0/7）— PER12.10倍・PEG0.177・52週19.0% ／ 💰単元16.9万円
  > 【戦略】当日高値超えの逆指値1714円で順張り参戦を検討。上限1731.1円・SL1597円目安
- 7729 東京精密｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_UWAHIGE｜終値12260｜💰単元119.0万円
- 2760 東京エレクトロンデバイス｜ai_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜終値3895｜💰単元38.2万円
- 4971 メック｜ai_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜終値5070｜💰単元50.0万円
- 6235 オプトラン｜ai_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜終値2083｜💰単元20.6万円
- 6762 TDK｜ai_reversal｜🔥絶好調｜🟢値頃｜PASS｜終値2264｜💰単元22.6万円｜reversal 指値2264 SL2161.5・✅即時可｜⚠日程不明
  > 【業態】電子部品大手。HDD向け磁気ヘッドから、2次電池、センサ応用、受動部品も成長。
  > 【いま】終値2,264円・直近5日-4.29%（材料未確認）
  > 【調子】🔥絶好調（9/13）
  > 【水準】🟢値頃（5.0/7）— PER15.35倍・PEG0.456・52週15.3% ／ 💰単元22.6万円
  > 【戦略】当日終値2264円の指値で反転を取りにいく。SL2161.5円（直近5日安値）
- 6981 村田製作所｜ai_reversal｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜終値5050｜💰単元51.8万円
- 7735 SCREENホールディングス｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜終値7800｜💰単元77.7万円｜📐進捗 遅れ -10.4%
- 1961 三機工業｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜終値2427｜💰単元25.3万円｜📐進捗 上振れ 39.8%
- 5384 フジミインコーポレーテッド｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜終値2785｜💰単元27.8万円｜📐進捗 上振れ 20.0%
- 6941 山一電機｜ai_reversal｜🔥絶好調｜💎割安｜PASS｜終値6510｜💰単元65.1万円｜reversal 指値6510 SL6120・✅即時可｜⚠日程不明 ⚠1単元でリスク枠超過（39,000円）
  > 【業態】半導体検査用ソケット大手。基板装置や実装用も。新分野育成し安定化へ。
  > 【いま】終値6,510円・直近5日-6.47%（材料未確認）
  > 【調子】🔥絶好調（8/13）
  > 【水準】💎割安（6.0/7）— PER10.68倍・PEG0.348・52週22.4% ／ 💰単元65.1万円
  > 【戦略】当日終値6510円の指値で反転を取りにいく。SL6120円（直近5日安値）／⚠1単元リスク39,000円（枠超過）
- 6227 AIメカテック｜ai_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜終値4810｜💰単元45.4万円｜📑TOPIX新規採用（2026-10-30 組入）
- 6752 パナソニックHD｜ai_reversal｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜終値3041｜💰単元31.9万円
- 3436 SUMCO｜ai_reversal｜⚡好調｜💎割安｜FAIL_INSEN｜終値2014.5｜💰単元19.6万円
- 6336 石井表記｜granville_rebound/ai_reversal｜⚡好調｜💎割安｜FAIL_UWAHIGE｜終値1181｜💰単元11.6万円｜📋カルテ窓 12/11(残16営業日)
- 6971 京セラ｜ai_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値2877｜💰単元28.6万円｜📐進捗 遅れ -13.6%
- 4022 ラサ工業｜ai_reversal｜⚡好調｜💎割安｜PASS｜終値1271｜💰単元12.7万円｜reversal 指値1271 SL1189・⏸トラップ疑い・確認足待ち｜📐進捗 上振れ 17.6%
  > 【業態】化成品・機械・電子材料が主力。リン酸から半導体向け、消臭剤、水処理剤等。
  > 【いま】終値1,271円・直近5日-11.43%（材料未確認）
  > 【調子】⚡好調（5/13）— 上方修正済み・🔼進捗先行・⚠下期依存
  > 【水準】💎割安（7.0/7）— PER9.55倍・PEG0.420・52週16.2% ／ 💰単元12.7万円
  > 【戦略】当日終値1271円の指値で反転を取りにいく。SL1189円（直近5日安値）
- 4973 JCU｜ai_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値3860｜💰単元38.9万円｜📑TOPIX低減対象（次 01/29 第2回/8）
- 255A GLテクノHD｜ai_reversal｜✅順調｜💎割安｜FAIL_INSEN｜終値3760｜💰単元37.3万円
- 6590 芝浦メカトロニクス｜ai_reversal｜✅順調｜🟢値頃｜FAIL_INSEN｜終値2679｜💰単元26.4万円｜📐進捗 遅れ -18.8%
- 5706 三井金属鉱業｜ai_reversal｜🔻悪化｜⚪妥当｜FAIL_INSEN｜終値1354｜💰単元13.4万円｜📐進捗 上振れ 60.7%
- 6965 浜松ホトニクス｜ai_reversal｜✅順調｜🟡やや割高｜FAIL_INSEN｜終値2028｜💰単元20.2万円
- 6643 戸上電機製作所｜ai_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜終値4525｜💰単元46.0万円｜📐進捗 上振れ 23.6%
- 6501 日立製作所｜ai_reversal｜✅順調｜🟡やや割高｜FAIL_INSEN｜終値4874｜💰単元48.1万円
- 2802 味の素｜ai_reversal｜➖横ばい｜⚪妥当｜FAIL_INSEN｜終値4191｜💰単元41.5万円
- 1982 日比谷総合設備｜ai_reversal｜➖横ばい｜🟡やや割高｜PASS｜終値3040｜💰単元30.4万円｜reversal 指値3040 SL2964・✅即時可｜📐進捗 上振れ 14.1%
  > 【業態】空調工事大手。電気・衛生工事も。NTT向け主力。床下空調システムなどに強み。
  > 【いま】終値3,040円・直近5日-3.65%（材料未確認）
  > 【調子】➖横ばい（2/13）— 質注意・⚠減速・🔼進捗先行
  > 【水準】🟡やや割高（2.0/7）— PER14.42倍・PEG4.951・52週66.3% ／ 💰単元30.4万円
  > 【戦略】当日終値3040円の指値で反転を取りにいく。SL2964円（直近5日安値）
- 9503 関西電力｜ai_reversal｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜終値2703.5｜💰単元27.3万円｜📐進捗 遅れ -36.3%
- 6617 東光高岳｜ai_reversal｜⚠減速｜⚪妥当｜PASS_DOJI｜終値4720｜💰単元47.2万円｜momentum 逆指値4810 SL4525 上限4858.1 乖離1.9%・⏳確認足待ち｜⚠日程不明 📐進捗 上振れ 10.5% ⚠業績基調が下向き（⚠減速） ⚠市場に劣後 RS20 -22.0pt
  > 【業態】東電系で送配電機器が主力。高岳と東光電が統合。自動検針システムに強み。
  > 【いま】終値4,720円・直近5日-8.88%（材料未確認）
  > 【調子】⚠減速（1/13）— 質注意・⚠減速・🔼進捗先行
  > 【水準】⚪妥当（4.0/7）— PER7.27倍・PEG45.794・52週25.1% ／ 💰単元47.2万円
  > 【戦略】当日高値超えの逆指値4810円で順張り参戦を検討。上限4858.1円・SL4525円目安
- 9432 NTT｜ai_reversal｜⚠減速｜🟡やや割高｜FAIL_UWAHIGE｜終値170.2｜💰単元1.7万円｜📐進捗 遅れ -10.3%
- 4203 住友ベークライト｜ai_reversal/granville_rebound｜業績データ取得不可｜⚪妥当｜FAIL_INSEN｜終値7003｜💰単元68.8万円
- 6146 ディスコ｜ai_reversal｜取得不可｜⏸判定不能｜FAIL_INSEN｜終値44380｜💰単元433.9万円
- 6723 ルネサスエレクトロニクス｜ai_reversal｜取得不可｜⏸判定不能｜FAIL_INSEN｜終値2618｜💰単元26.2万円
- 9984 ソフトバンクグループ｜ai_reversal｜業績データ取得不可(経常益予想非開示)｜⏸判定不能｜FAIL_INSEN｜終値3383｜💰単元32.8万円

## ⚡材料後出し
その日の足は開示前の情報。判定は参考値
- 4011 Headwaters Co.,Ltd｜FAIL_INSEN｜📌その他重要開示 ヘッドウォータース、Anthropic「Claude Security」の活用を本格化（16:00）
- 4169 Enechange Ltd.｜FAIL_INSEN｜📊決算発表 [Delayed][Summary]Consolidated Financial Results for the First Half of the Fiscal Year Ending March 31, 2027 (Under Japanese GAAP)（15:30） / 📌その他重要開示 [Delayed]Presentation Material for FY26 H1 Financial Result（15:30） / 📌その他重要開示 [Delayed]Notice Concerning the Recording of Non-operating Expenses (Share of Loss of Entities Accounted for Using the Equity Method)（15:30）
- 4552 JCR Pharmaceuticals Co., Ltd.｜FAIL_UWAHIGE｜📌その他重要開示 JCR Pharmaceuticals Strengthens Community Ties Through Plant Tour at Kobe Science Park Center（15:30） / 📌その他重要開示 地域住民の皆さまに向けた工場見学会を開催しました（15:30）
- 477A Startline CO.,LTD.｜FAIL_INSEN｜📌その他重要開示 新規出店のお知らせ（Diverse Village UTSUNOMIYA）（16:00）
- 4884 Kringle Pharma, Inc.｜FAIL_INSEN｜📌その他重要開示 定時株主総会の付議議案に関するお知らせ（16:50） / 📌その他重要開示 第三者割当による株式、第19回新株予約権及び第20回新株予約権（行使価額修正条項選択権付）の発行条件等の決定に関するお知らせ（16:50）
- 4912 ライオン｜FAIL_UWAHIGE｜📌その他重要開示 「キッザニア東京」での株主さま向けイベント開催のお知らせ（18:00）
- 5033 Nulab Inc.｜PASS｜📌その他重要開示 当社サービス「Cacoo」における不正アクセスに関する現在の状況について（第二報）（18:00）
- 5532 リアルゲイト｜FAIL_UWAHIGE｜📌その他重要開示 （開示事項の経過）固定資産取得に伴う資金借入に関するお知らせ（15:30）
- 6072 ERTH Group Co.,Ltd.｜PASS_DOJI｜📌その他重要開示 2026年11月12日開催決算説明会のアーカイブ動画の公開及びいただいたご質問に対するご回答のお知らせ（16:00）
- 6570 Kyowa Corporation Co. Ltd.｜FAIL_INSEN｜📌その他重要開示 株式の立会外分売実施に関するお知らせ（16:30）
- 6676 BUFFALO INC.｜FAIL_INSEN｜🔁自己株式取得 自己株式の公開買付け開始に関するお知らせ（16:30）
- 7213 LECIP Holdings Corporation｜FAIL_INSEN｜🔁自己株式取得 自己株式の取得状況及び取得終了に関するお知らせ（15:30）
- 7433 Hakuto Co., Ltd.｜FAIL_INSEN｜📌その他重要開示 伯東、「InterAqua」出展のお知らせ（16:30） / 📌その他重要開示 Notice Concerning Dividends of Surplus（15:30） / 📌その他重要開示 剰余金の配当に関するお知らせ（15:30）
- 8151 東陽テクニカ｜FAIL_INSEN｜📌その他重要開示 東陽テクニカ、米国・DryRun Security社と販売代理店契約を締結し、AI推論型アプリケーションセキュリティを提供開始（15:00）
- 8154 加賀電子｜PASS｜📌その他重要開示 Notice Regarding Receipt of SBT Certification（17:30） / 📌その他重要開示 SBT認定取得に関するお知らせ（17:30）
- 8508 J Trust Co., Ltd.｜FAIL_INSEN｜📌その他重要開示 公開買付けへの応募及び持分法適用関連会社の異動に関するお知らせ（16:00）
- 9025 Konoike Transport Co., Ltd.｜FAIL_INSEN｜📌その他重要開示 Notice Concerning Acquisition of Shares of NS Holdings Co., Ltd. (Making It a Wholly Owned Subsidiary) and Making Nissin Kiko Co., Ltd. a Second-tier（15:30） / 📌その他重要開示 NSホールディングス株式会社の株式取得（完全子会社化）及び日進機工株式会社の孫会社化に関するお知らせ（15:30）
- 9163 Nareru Group Inc.｜FAIL_INSEN｜📌その他重要開示 October 2026 KPI Announcement（15:30） / 📌その他重要開示 2026年10月度　ＫＰＩのお知らせ（15:30）
- 9343 アイビス｜FAIL_INSEN｜📌その他重要開示 世界累計5.6億ダウンロードの「ibisPaint」が「Google Play ベスト オブ 2026」アメリカ・インドで「クリエイティブ表現部門」を受賞（17:00）

## 📢開示
- 使用した一覧URL: https://kabutan.jp/disclosures/?kubun=&page=1 〜 https://kabutan.jp/disclosures/?kubun=&page=25（25ページ・期間 2026-11-17 20:30〜2026-11-18・全373件）。フォールバックなし
- プール突合 54件（📌その他重要開示48・🔁自己株式取得2・📊決算発表2・👥主要株主・大量保有2）・①-9へ引き渡し 2件
- 📊決算発表 4169 エネチェンジ：[Delayed][Summary]Consolidated Financial Results for the First Half of the Fiscal Year Ending March 31, 2027 (Under Japanese GAAP)（11-18 15:30）
- 📌その他重要開示 4169 エネチェンジ：[Delayed]Presentation Material for FY26 H1 Financial Result（11-18 15:30）
- 📌その他重要開示 4169 エネチェンジ：[Delayed]Notice Concerning the Recording of Non-operating Expenses (Share of Loss of Entities Accounted for Using the Equity Method)（11-18 15:30）
- 📊決算発表 6324 ハーモニック：[Updated] Consolidated Financial Results for the Six Months Ended September 30, 2026 [Japanese GAAP]（11-18 14:00）
- 🔁自己株式取得 6676 ＢＵＦ：自己株式の公開買付け開始に関するお知らせ（11-18 16:30）
- 🔁自己株式取得 7213 レシップＨＤ：自己株式の取得状況及び取得終了に関するお知らせ（11-18 15:30）
- 👥主要株主・大量保有 3964 オークネット：Notice Concerning Change of Major Shareholder（11-18 10:00）
- 👥主要株主・大量保有 3964 オークネット：主要株主の異動に関するお知らせ（11-18 10:00）
- 📌その他重要開示 147A ソラコム：OmdiaのIoT MVNO市場調査レポートで「リーダー」に選出（11-18 11:00）
- 📌その他重要開示 167A リョー菱ＨＤ：2026年度 第２四半期 決算説明会資料（11-18 10:00）
- 📌その他重要開示 218A リベラウェア：Liberaware、陸上自衛隊「令和8年度GTAイノベーションチャレンジ」革新研究部門に採択（11-18 13:00）
- 📌その他重要開示 2489 アドウェイズ：UNICORN、広告配信プラットフォームとしての広告品質管理の取り組みをまとめた「広告品質・透明性レポート」を公開（11-18 12:00）
- 📌その他重要開示 3691 デジプラ：テックファームホールディングスが株主優待としてデジタルギフトを採用（11-18 12:00）
- 📌その他重要開示 3762 テクマト：テクマトリックス、Tenable One Identity Exposure導入企業向け「TechMatrix AD Exposure Assessment」を提供開始（11-18 11:00）
- 📌その他重要開示 4011 ヘッドウォ：ヘッドウォータース、Anthropic「Claude Security」の活用を本格化（11-18 16:00）
- 📌その他重要開示 4040 南海化学：【再掲】SMART ENERGY WEEK関西2026出展のお知らせ（11-18 11:00）
- 📌その他重要開示 4045 東合成：Toagosei Announces Organizational and Officer Changes（11-18 14:00）
- 📌その他重要開示 4045 東合成：組織変更および役員の異動に関するお知らせ（11-18 14:00）
- 📌その他重要開示 4483 ＪＭＤＣ：順天堂大学とJMDC、医療・ヘルスケア領域で新たな価値の共創を目指す包括連携協定を締結（11-18 09:00）
- 📌その他重要開示 4507 塩野義：Notice Regarding SHIONOGI R&D Day 2026（11-18 12:15）
- 📌その他重要開示 4507 塩野義：SHIONOGI R&D Day 2026 の開催について（11-18 12:00）
- 📌その他重要開示 4507 塩野義：Shionogi Completes Acquisition of IntraBio Inc. and Adds AQNEURSA (levacetylleucine) to Growing Rare Disease Global Portfolio（11-18 09:00）
- 📌その他重要開示 4507 塩野義：IntraBio社の買収完了について（11-18 09:00）
- 📌その他重要開示 4552 ＪＣＲファ：JCR Pharmaceuticals Strengthens Community Ties Through Plant Tour at Kobe Science Park Center（11-18 15:30）
- 📌その他重要開示 4552 ＪＣＲファ：地域住民の皆さまに向けた工場見学会を開催しました（11-18 15:30）
- 📌その他重要開示 4554 富士製薬：2026年9月期通期決算説明会の動画および書き起こし公開のお知らせ（11-18 09:30）
- 📌その他重要開示 477A スタートＬ：新規出店のお知らせ（Diverse Village UTSUNOMIYA）（11-18 16:00）
- 📌その他重要開示 4884 クリングル：定時株主総会の付議議案に関するお知らせ（11-18 16:50）
- 📌その他重要開示 4884 クリングル：第三者割当による株式、第19回新株予約権及び第20回新株予約権（行使価額修正条項選択権付）の発行条件等の決定に関するお知らせ（11-18 16:50）
- 📌その他重要開示 4884 クリングル：「2026年９月期 通期決算説明会」の動画に関するログミーFinance書き起こし記事公開のお知らせ（11-18 14:00）
- 📌その他重要開示 4912 ライオン：「キッザニア東京」での株主さま向けイベント開催のお知らせ（11-18 18:00）
- 📌その他重要開示 5033 ヌーラボ：当社サービス「Cacoo」における不正アクセスに関する現在の状況について（第二報）（11-18 18:00）
- 📌その他重要開示 5133 テリロジＨＤ：テリロジーHD連結子会社テリロジー、AIセキュリティ分野の先進企業「DeepKeep社」と販売代理店契約を締結（11-18 10:00）
- 📌その他重要開示 5532 リアルゲイト：（開示事項の経過）固定資産取得に伴う資金借入に関するお知らせ（11-18 15:30）
- 📌その他重要開示 5532 リアルゲイト：2026年定時株主総会招集通知及び株主総会資料（11-18 08:00）
- 📌その他重要開示 6072 ＥＲＴＨ：2026年11月12日開催決算説明会のアーカイブ動画の公開及びいただいたご質問に対するご回答のお知らせ（11-18 16:00）
- 📌その他重要開示 6570 共和コーポ：株式の立会外分売実施に関するお知らせ（11-18 16:30）
- 📌その他重要開示 7148 ＦＰＧ：Notice of the 25th Ordinary General Meeting of Shareholders（11-18 08:00）
- 📌その他重要開示 7148 ＦＰＧ：第25期定時株主総会資料（電子提供措置事項のうち交付書面省略事項）（11-18 08:00）
- 📌その他重要開示 7148 ＦＰＧ：第25期定時株主総会招集通知（電子提供措置事項のうち交付書面記載事項）（11-18 08:00）
- 📌その他重要開示 7433 伯東：伯東、「InterAqua」出展のお知らせ（11-18 16:30）
- 📌その他重要開示 7433 伯東：Notice Concerning Dividends of Surplus（11-18 15:30）
- 📌その他重要開示 7433 伯東：剰余金の配当に関するお知らせ（11-18 15:30）
- 📌その他重要開示 8151 東陽テク：東陽テクニカ、米国・DryRun Security社と販売代理店契約を締結し、AI推論型アプリケーションセキュリティを提供開始（11-18 15:00）
- 📌その他重要開示 8154 加賀電子：Notice Regarding Receipt of SBT Certification（11-18 17:30）
- 📌その他重要開示 8154 加賀電子：SBT認定取得に関するお知らせ（11-18 17:30）
- 📌その他重要開示 8508 Ｊトラスト：公開買付けへの応募及び持分法適用関連会社の異動に関するお知らせ（11-18 16:00）
- 📌その他重要開示 8616 東海東京：2nd Quarter,Fiscal year ending March 2027　Management Strategy Briefing（11-18 13:00）
- 📌その他重要開示 8616 東海東京：2027年3月期中間　経営戦略説明会（11-18 13:00）
- 📌その他重要開示 9025 鴻池運輸：Notice Concerning Acquisition of Shares of NS Holdings Co., Ltd. (Making It a Wholly Owned Subsidiary) and Making Nissin Kiko Co., Ltd. a Second-tier（11-18 15:30）
- 📌その他重要開示 9025 鴻池運輸：NSホールディングス株式会社の株式取得（完全子会社化）及び日進機工株式会社の孫会社化に関するお知らせ（11-18 15:30）
- 📌その他重要開示 9163 ナレルＧ：October 2026 KPI Announcement（11-18 15:30）
- 📌その他重要開示 9163 ナレルＧ：2026年10月度　ＫＰＩのお知らせ（11-18 15:30）
- 📌その他重要開示 9343 アイビス：世界累計5.6億ダウンロードの「ibisPaint」が「Google Play ベスト オブ 2026」アメリカ・インドで「クリエイティブ表現部門」を受賞（11-18 17:00）

## 総当りゲート
### 5手法
- PASS（20）: 1721 1982 3105 4022 4272 4768 5137 5310 558A 6668 6762 6804 6875 6923 6941 6969 8154 9301 9302 9468
- PASS_DOJI（3）: 6617 6779 7995
- FAIL_UWAHIGE（25）: 268A 4088 4286 4293 4377 4503 4933 4966 5019 5537 5602 6167 6336 6532 6752 6758 6981 7729 7733 7747 9107 9110 9308 9432 9766
- FAIL_INSEN（203）: 1435 147A 1663 167A 1926 1951 1960 1961 1963 1975 1979 1980 2109 2331 255A 262A 2760 2802 2975 3036 3091 3110 3116 3131 3205 3374 3436 3445 3479 3498 3556 3569 3612 3798 3843 3915 3932 3994 4008 4021 4028 4042 4047 4053 4063 4176 4180 4182 4203 4205 4206 4216 4249 4368 4379 4403 4410 4417 4434 446A 4471 4634 4743 4746 4771 4902 4971 4973 4980 5018 5021 5101 5136 5186 5201 5246 5301 5331 5333 5344 5384 5444 5463 5703 5706 5711 5801 5821 5831 5832 6016 6036 6055 6071 6135 6146 618A 6227 6235 6238 6250 6268 6277 6278 6323 6324 6332 6340 6349 6367 6368 6370 6379 6407 6418 6436 6448 6454 6471 6473 6479 6481 6501 6516 6524 6588 6590 6613 6632 6643 6645 6651 6652 6674 6723 6724 6741 6750 6754 6777 6787 6807 6810 6834 6845 6850 6857 6918 6925 6943 6952 6965 6971 6988 7004 7148 7167 7177 7186 7220 7276 7278 7322 7366 7381 7433 7637 7731 7735 7942 8032 8035 8084 8133 8253 8304 8334 8354 8359 8366 8370 8386 8393 8508 8524 8600 8616 8698 8704 8975 9037 9048 9072 9204 9434 9503 9554 9722 9902 9934 9960 9962 9984
### グランビル
- PASS（26）: 2326 278A 3042 338A 3927 4025 4258 436A 4528 4540 4549 4568 4968 5033 5367 5599 5930 6490 6958 7480 7609 7970 9075 9404 9697 9824
- PASS_DOJI（6）: 3156 3909 6072 6203 6768 7826
- FAIL_UWAHIGE（30）: 153A 2267 3040 3563 3691 3692 3858 4075 4100 4240 4396 4498 4543 4552 460A 4912 5133 5381 5532 5985 6328 7715 8051 8160 8739 9401 9418 9605 9735 9742
- FAIL_INSEN（147）: 1436 150A 1878 1911 1928 1938 1941 2206 2384 2488 2489 2492 2502 2811 2897 2962 3002 3092 3106 3182 3252 336A 3371 3401 3405 3491 3496 3547 3549 3565 3673 3697 3762 3763 3793 3850 3851 3891 3964 3968 4005 4040 4045 4091 4169 417A 4204 428A 4373 4375 4398 4401 4419 4431 4432 4443 4475 4507 4523 4534 4554 456A 4667 4674 4686 4765 477A 479A 4848 4884 4922 4937 5027 5036 5105 5184 5233 5252 5256 5892 6027 6080 6099 6138 6191 6317 6412 6508 6570 6574 6676 6742 6744 6745 6840 6862 6877 6890 6904 6947 7175 7184 7213 7256 7269 7380 7606 7678 7713 7921 8012 8016 8056 8113 8137 8159 8167 8344 8360 8364 8368 8377 8388 8392 8395 8410 8551 8609 8801 8803 8804 8934 9006 9025 9045 9065 9163 9278 9304 9509 9513 9536 9552 9837 9842 9869 9956
### 変化点
- FAIL_UWAHIGE（1）: 265A
- FAIL_INSEN（15）: 218A 286A 3923 3989 4011 4165 4259 4478 4483 4488 5803 593A 7695 8151 9343
- 除籍（30暦日超）: 0件（なし）

## 機械詳細
- 候補収集: 当夜指名106銘柄（新規16・再指名90）・未マージPR由来0件（直近24hのリモートブランチは main と作業ブランチのみ）・熟成由来の候補 0件（うちPASS0）・dm_*/an_* はspec未定義のため不使用
- 日足: 477銘柄取得（失敗0・ステイルSKIP 0）・1306 取得可
- ヘッドライン: PASS55件中55件に付与・抜粋（通知10件 群別 method4/ai3/granville3/changepoint0/不明0）
- kabutan: 決算ページ 55件・トップページ新規取得 6/50件（打ち切り0）・業種の埋め戻し 0件（残り1件）
- profile_cache: 総数1074・本夜追加5件・業態『未取得』のまま出た件数 0
- 業績グレード: 再計算は未実施（キャッシュ値を使用）・gyoseki_cache history 退避 0件・next_earnings 更新 18件（kabutan 決算ページの決算発表予定日）
- earnings_log: 総数506／本夜追記2件／リターン補完45件／日足なしで未補完140件
- gate_history: gate_history/2026-11-18.json を新規作成（verdicts 476件＝評価476件・nominations 106件（新規16・再指名90））
- grades.json: 1125銘柄/647.8KB・業種PER中央値 26業種・spm 付与1030件
- pool_bars.json: 477銘柄/406.7KB
- earnings_calendar.json: 1130銘柄/142.2KB・次回決算日 付与213件／未発表917件・前年同期発表日 付与376件
- method_score: 保持81件/null395件（{'kenmo_momentum': 13, 'stf_kakuhen': 25, 'granville_rebound': 2, 'choruko_reversal': 20, 'ai_reversal': 19, 'granville_tenkan': 1, 'granville_oshime': 1}）
- 鮮度ゲート: 鮮度切れ除外12件・nom_age分布 0-2:168/3-10:187/11+:121・last_seen欠損0件
- トレンド文脈: ctx 合致104／不一致219／レンジ151／判定不能2・PASS のうち ctx 合致7件・形態が付いた銘柄166件
- 3日ルール: 判定0銘柄・streak≥3 0・streak=2 0・判定不可0（保有0）
- 開示の分類別件数（プール突合）: {'📌その他重要開示': 48, '🔁自己株式取得': 2, '📊決算発表': 2, '👥主要株主・大量保有': 2}
- 権利情報: rights_cache 総数503・本夜 配当更新0件／優待取得0件（T+1/T+2 に権利落ちなし・保有0のため未取得。minkabu は 403）・不明のまま503件
- STEP 4.8 週末ブリーフ: スキップ（week_open=false）
- master.json 変更行数: +12065/-11538（往復一致で検出した indent=2・仮ファイル経由で差し替え）
