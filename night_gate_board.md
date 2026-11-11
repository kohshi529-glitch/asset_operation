# 夜間ゲート 2026-11-11

## サマリー
- 評価数: 511 / PASS: 240（PASS_DOJI 3件を含む）
- 発注可能提案数: 154件（✅140／⏳1／⏸位置不適12／⏸トラップ疑い1）
- 市場一言: 市場モード「軟調」（market.latest 2026-11-11）。プール511銘柄中 PASS比率47.0%（陰線FAIL 147件・上髭FAIL 124件）
- 実行モード: 通常（base_day=当日の引け値を対象）
- base_day: 2026-11-11（run_at 2026-11-11 20:40起動）
- week_open: false（翌営業日 11/12(木)＝週初でない）→ STEP 4.8 週末ブリーフはスキップ
- 📆 翌営業日 11/12: なし（T+2 11/13: マイナーSQ）
- 📑指数: 低減対象 提案18件／PASS33件／プール79件・新規採用 12件（index_flags 2026-10-07 公表分）・次の TOPIX 低減日 01/29 第2回/8（あと53営業日）

## 検証結果
- V1 → はい（提案154=results154=模擬154=通知母数154）
- V2 → はい（PASS240=提案154+除外86・order_status欠落0）
- V3 → はい（results511件重複0）
- V4 → はい（既存static変更0）
- V5 → はい（変更トップキー['earnings_log', 'night_gate', 'pipeline', 'valuation_cache']・pipeline他run不変True・spec不変True・profile既存書換なしTrue）
- V6 → はい（gyoseki_cache不整合0）
- V7 → はい（必須セクション存在（week_open=false のためカタリスト節なし））
- V8 → はい（模擬154行 不正0）
- V9 → はい（gate_history と today 一致）
- V10 → はい（base_day一致 2026-11-11）
- V11 → いいえ（+26160/-21619（indent=2・往復一致で検出））
- V12 → はい（並び順 (a)(b)(c) 一致）
- V13 → はい（1084銘柄/604.2KiB・和集合1084・20キーTrue・型True・nx一致True・ix非null222・業種PER中央値26業種）
- V14 → はい（保持78件/null433件・出所不明/不一致0）
- V15 → はい（PASS240件中240件に付与（欠落0）・5キーTrue・(c)4項目の未取得/取得不可34（キャッシュ保存値の転記を含む））
- V16 → はい（📊49件全件記録True・grade_beforeは再計算前（本夜は業績再計算なし）・history>4=0・総数356）
- V17 → はい（513銘柄/436.8KiB・保有1銘柄すべて収録・3日ルール判定1銘柄）
- V18 → はい（鮮度切れ45件・誤除外0・nom_age分布 0-2:174/3-10:216/11+:121）
- V19 → はい（verdicts511=評価511・nominations104（新規9/再指名95）・集合一致True・ctx判定不能3）
- V20 → はい（1088銘柄・nx非null511・hist持ち741・pxd368・取得元名称なしTrue）
- V21 → はい（recent_pass543銘柄・出所実在True・保有情報不使用True）
- V22 → はい（PASS_DOJI3・⏸位置不適12誤通過0=True・⏸トラップ1・rs20付与511/511）
- VLEAK → はい（公開物（ボード/today/gate_history）への保有情報 検出0件（保有1銘柄・アラート3件（詳細は通知のみ）））

## 保有アラート
保有1銘柄・アラート3件（詳細は通知）

## 🧾直近提案の決算接近
窓内（直近20営業日）の提案銘柄 543・日程不明 301・当夜評価外 135。保有情報は使っていない（候補だった銘柄の日程）
- 🚨決算直前 11/12(残1営業日) 1975 新日本空調｜最後の提案 11/11（momentum 3485・⏸位置不適(25MA下 -6.23%)）｜提案5回｜当夜 PASS
- 🚨決算直前 11/12(残1営業日) 4419 Ｆｉｎａｔｅｘｔホールディングス｜最後の提案 11/11（reversal 1237・✅即時可）｜提案4回｜当夜 PASS
- 🚨決算直前 11/12(残1営業日) 4743 ITFOR Inc.｜最後の提案 11/11（momentum 1585・⏸位置不適(25MA下 -2.11%／52週 23.7%)）｜提案6回｜当夜 PASS
- 🚨決算直前 11/12(残1営業日) 6524 湖北工業｜最後の提案 11/11（reversal 4825・✅即時可）｜提案4回｜当夜 PASS
- 🚨決算直前 11/12(残1営業日) 6613 QD Laser, Inc.｜最後の提案 11/11（momentum 2222・✅即時可）｜提案4回｜当夜 PASS
- 🚨決算直前 11/12(残1営業日) 6862 Minato Holdings Inc.｜最後の提案 11/11（reversal 3360・✅即時可）｜提案5回｜当夜 PASS
- 🚨決算直前 11/12(残1営業日) 6918 Aval Data Corporation｜最後の提案 11/11（reversal 3270・✅即時可）｜提案5回｜当夜 PASS
- 🚨決算直前 11/12(残1営業日) 7433 伯東｜最後の提案 11/11（reversal 1615・✅即時可）｜提案2回｜当夜 PASS
- 🚨決算直前 11/12(残1営業日) 8345 Bank of Iwate Ltd.｜最後の提案 11/11（reversal 2128・✅即時可）｜提案8回｜当夜 PASS
- 🚨決算直前 11/12(残1営業日) 8381 San-in Godo Bank Ltd.｜最後の提案 11/11（reversal 2190.5・✅即時可）｜提案4回｜当夜 PASS
- 🚨決算直前 11/12(残1営業日) 8551 北日本銀行｜最後の提案 11/11（reversal 2373・✅即時可）｜提案2回｜当夜 PASS
- 🚨決算直前 11/12(残1営業日) 1435 robot home Inc.｜最後の提案 11/10（momentum 164・✅即時可）｜提案1回｜当夜 FAIL_UWAHIGE
- 🚨決算直前 11/12(残1営業日) 150A ＪＳＨ｜最後の提案 11/10（reversal 624・✅即時可）｜提案4回｜当夜 FAIL_UWAHIGE
- 🚨決算直前 11/12(残1営業日) 4165 PLAID,Inc.｜最後の提案 11/10（changepoint 760・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- 🚨決算直前 11/12(残1営業日) 6490 ＰＩＬＬＡＲ｜最後の提案 11/09（reversal 8770・✅即時可）｜提案6回｜当夜 FAIL_UWAHIGE
- 🚨決算直前 11/12(残1営業日) 7715 長野計器｜最後の提案 11/09（reversal 3190・✅即時可）｜提案3回｜当夜 PASS
- 🚨決算直前 11/12(残1営業日) 8804 東京建物｜最後の提案 11/09（momentum 3371・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 🚨決算直前 11/12(残1営業日) 167A リョーサン菱洋ホールディングス（リョー菱ＨＤ）｜最後の提案 11/06（reversal 2956・✅即時可）｜提案1回｜当夜 FAIL_UWAHIGE
- 🚨決算直前 11/12(残1営業日) 598A チャットプラス｜最後の提案 11/06（changepoint 950・✅即時可）｜提案4回｜当夜 FAIL_UWAHIGE
- 🚨決算直前 11/12(残1営業日) 6055 Japan Material Co., Ltd.｜最後の提案 11/06（reversal 1623・✅即時可）｜提案5回｜当夜 PASS
- 🚨決算直前 11/12(残1営業日) 3591 WACOAL HOLDINGS CORP｜最後の提案 11/05（reversal 3919・✅即時可）｜提案4回｜当夜 FAIL_INSEN
- 🚨決算直前 11/12(残1営業日) 7734 Riken Keiki Co., Ltd.｜最後の提案 11/02（momentum 3480・✅即時可）｜提案3回｜当夜 FAIL_UWAHIGE
- 🚨決算直前 11/12(残1営業日) 1719 HAZAMA ANDO Corporation｜最後の提案 10/29（reversal 1759.5・✅即時可）｜提案5回｜当夜 FAIL_INSEN
- 🚨決算直前 11/12(残1営業日) 1952 Shin Nippon Air Technologies Co., Ltd.｜最後の提案 10/29（reversal 3065・✅即時可）｜提案5回｜当夜 PASS
- 🚨決算直前 11/12(残1営業日) 3040 ソリトンシステムズ｜最後の提案 10/29（oshime 3051.2・✅即時可）｜提案1回｜当夜 PASS
- 🚨決算直前 11/12(残1営業日) 3496 AZOOM CO.,LTD｜最後の提案 10/29（momentum 4810・✅即時可）｜提案4回｜当夜 FAIL_INSEN
- 🚨決算直前 11/12(残1営業日) 5537 AlbaLink Co.,Ltd.｜最後の提案 10/29（momentum 3405・✅即時可）｜提案4回｜当夜 FAIL_INSEN
- 🚨決算直前 11/12(残1営業日) 4377 ONE CAREER Inc.｜最後の提案 10/28（momentum 2509・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 🚨決算直前 11/12(残1営業日) 1861 Kumagai Gumi Co., Ltd.｜最後の提案 10/27（reversal 1246・✅即時可）｜提案5回｜当夜 評価外
- 🚨決算直前 11/12(残1営業日) 5254 Arent, Inc.｜最後の提案 10/27（momentum 3880・✅即時可）｜提案4回｜当夜 FAIL_INSEN
- 🚨決算直前 11/12(残1営業日) 5590 NETSTARS Co.,Ltd.｜最後の提案 10/27（changepoint 656・✅即時可）｜提案3回｜当夜 評価外
- 🚨決算直前 11/12(残1営業日) 7567 Sakae Electronics Corp.｜最後の提案 10/26（momentum 635・✅即時可）｜提案3回｜当夜 FAIL_UWAHIGE
- 🚨決算直前 11/12(残1営業日) 3993 PKSHA Technology, Inc.｜最後の提案 10/23（changepoint 3700・✅即時可）｜提案2回｜当夜 PASS
- 🚨決算直前 11/12(残1営業日) 558A SQUEEZE Inc.｜最後の提案 10/23（momentum 5890・✅即時可）｜提案2回｜当夜 FAIL_UWAHIGE
- 🚨決算直前 11/12(残1営業日) 1662 Japan Petroleum Exploration Co., Ltd.｜最後の提案 10/22（reversal 1715・✅即時可）｜提案3回｜当夜 評価外
- 🚨決算直前 11/12(残1営業日) 5034 unerry, Inc.｜最後の提案 10/22（momentum 2841・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- 🚨決算直前 11/12(残1営業日) 8066 Mitani Corporation｜最後の提案 10/19（reversal 3140・✅即時可）｜提案1回｜当夜 評価外
- 🚨決算直前 11/12(残1営業日) 8511 Japan Securities Finance Co., Ltd.｜最後の提案 10/19（reversal 2217・✅即時可）｜提案1回｜当夜 評価外
- 🚨決算直前 11/12(残1営業日) 3696 セレス｜最後の提案 10/16（momentum 2397・✅即時可）｜提案1回｜当夜 PASS
- 🚨決算直前 11/12(残1営業日) 4044 Central Glass Co., Ltd.｜最後の提案 10/16（oshime 4510・✅即時可）｜提案1回｜当夜 PASS
- 🚨決算直前 11/12(残1営業日) 4488 AI inside Inc.｜最後の提案 10/16（changepoint 2116・✅即時可）｜提案1回｜当夜 FAIL_UWAHIGE
- 🚨決算直前 11/12(残1営業日) 5036 Japan Business Systems, Inc.｜最後の提案 10/16（momentum 1898・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- 🚨決算直前 11/12(残1営業日) 2874 YOKOREI CO. LTD.｜最後の提案 10/15（reversal 1761・✅即時可）｜提案1回｜当夜 評価外
- 🚨決算直前 11/12(残1営業日) 9900 Sagami Holdings Corp.｜最後の提案 10/15（oshime 1096・✅即時可）｜提案1回｜当夜 評価外
- 📉決算反応日 11/12 1982 日比谷総合設備｜最後の提案 11/11（momentum 3195・⏸位置不適(25MA下 -1.2%)）｜提案4回｜当夜 PASS
- 📉決算反応日 11/12 147A SORACOM,INC.｜最後の提案 11/10（momentum 939・✅即時可）｜提案1回｜当夜 PASS
- 📉決算反応日 11/12 4071 Plus Alpha Consulting Co. LTD.｜最後の提案 11/10（changepoint 2318・✅即時可）｜提案3回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/12 4966 C. Uyemura & Co., Ltd.｜最後の提案 11/10（reversal 17270・✅即時可）｜提案4回｜当夜 FAIL_INSEN
- 📉決算反応日 11/12 5019 出光興産｜最後の提案 11/10（reversal 1290・✅即時可）｜提案1回｜当夜 PASS
- 📉決算反応日 11/12 6027 Bengo4.com, Inc.｜最後の提案 11/10（oshime 4890・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- 📉決算反応日 11/12 6284 日精エー・エス・ビー機械｜最後の提案 11/10（reversal 7850・✅即時可）｜提案6回｜当夜 PASS
- 📉決算反応日 11/12 6570 Kyowa Corporation Co. Ltd.｜最後の提案 11/10（oshime 4290・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 📉決算反応日 11/12 1963 JGC Holdings Corporation｜最後の提案 11/09（reversal 2051.5・✅即時可）｜提案5回｜当夜 PASS
- 📉決算反応日 11/12 2897 Nissin Foods Holdings Co., Ltd.｜最後の提案 11/09（momentum 3171・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 📉決算反応日 11/12 3405 クラレ｜最後の提案 11/09（momentum 1897・✅即時可）｜提案3回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/12 4980 Dexerials Corp.｜最後の提案 11/09（reversal 2385.5・✅即時可）｜提案3回｜当夜 PASS
- 📉決算反応日 11/12 7186 横浜フィナンシャルグループ｜最後の提案 11/09（reversal 1662.5・✅即時可）｜提案6回｜当夜 PASS
- 📉決算反応日 11/12 8151 東陽テクニカ｜最後の提案 11/09（changepoint 1668・✅即時可）｜提案3回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/12 255A GLテクノHD｜最後の提案 11/06（reversal 3940・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 📉決算反応日 11/12 3436 SUMCO｜最後の提案 11/06（reversal 1784.5・✅即時可）｜提案1回｜当夜 PASS
- 📉決算反応日 11/12 4022 ラサ工業｜最後の提案 11/06（reversal 1182・✅即時可）｜提案1回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/12 421A Movin' Strategic Career CO.,LTD.｜最後の提案 11/06（momentum 3335・✅即時可）｜提案4回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/12 4401 ＡＤＥＫＡ｜最後の提案 11/06（momentum 4068・✅即時可）｜提案2回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/12 4971 メック｜最後の提案 11/06（reversal 4925・✅即時可）｜提案3回｜当夜 PASS
- 📉決算反応日 11/12 6278 ユニオンツール｜最後の提案 11/06（reversal 9750・✅即時可）｜提案3回｜当夜 PASS
- 📉決算反応日 11/12 7167 めぶきフィナンシャルグループ｜最後の提案 11/06（reversal 1375・✅即時可）｜提案1回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/12 5711 三菱マテリアル｜最後の提案 11/04（reversal 4193・✅即時可）｜提案1回｜当夜 PASS
- 📉決算反応日 11/12 5838 Rakuten Bank, Ltd.｜最後の提案 11/04（momentum 6028・✅即時可）｜提案5回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/12 4100 Toda Kogyo Corp.｜最後の提案 11/02（reversal 1757・✅即時可）｜提案2回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/12 4478 freee K.K.｜最後の提案 11/02（changepoint 4645・✅即時可）｜提案4回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/12 7806 MTG Co., Ltd.｜最後の提案 11/02（oshime 8756・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 📉決算反応日 11/12 8304 Aozora Bank, Ltd.｜最後の提案 11/02（reversal 2981・✅即時可）｜提案4回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/12 4933 I-ne CO., LTD.｜最後の提案 10/29（momentum 2479・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 📉決算反応日 11/12 5184 ニチリン｜最後の提案 10/29（momentum 4185・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 📉決算反応日 11/12 6324 Harmonic Drive Systems Inc.｜最後の提案 10/29（reversal 5480・✅即時可）｜提案4回｜当夜 PASS
- 📉決算反応日 11/11 7199 Premium Group Co., Ltd.｜最後の提案 10/29（momentum 2263・✅即時可）｜提案3回｜当夜 評価外
- 📉決算反応日 11/12 8399 Bank Of The Ryukyus,Limited｜最後の提案 10/29（reversal 2868・✅即時可）｜提案6回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/12 268A Rigaku Holdings Corporation｜最後の提案 10/27（reversal 1485・✅即時可）｜提案2回｜当夜 PASS
- 📉決算反応日 11/11 5021 Cosmo Energy Holdings Co., Ltd.｜最後の提案 10/27（reversal 4370・✅即時可）｜提案3回｜当夜 評価外
- 📉決算反応日 11/11 8088 IWATANI Corporation｜最後の提案 10/27（reversal 1928・✅即時可）｜提案3回｜当夜 評価外
- 📉決算反応日 11/11 9699 NISHIO HOLDINGS CO. LTD.｜最後の提案 10/27（reversal 4305・✅即時可）｜提案3回｜当夜 評価外
- 📉決算反応日 11/12 1833 Okumura Corporation｜最後の提案 10/26（reversal 5350・✅即時可）｜提案1回｜当夜 評価外
- 📉決算反応日 11/11 6269 Modec, Inc.｜最後の提案 10/26（reversal 8130・✅即時可）｜提案5回｜当夜 評価外
- 📉決算反応日 11/12 2820 Yamami Co.｜最後の提案 10/23（momentum 6580・✅即時可）｜提案2回｜当夜 評価外
- 📉決算反応日 11/12 4259 ExaWizards Inc.｜最後の提案 10/23（changepoint 753・✅即時可）｜提案3回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/11 4928 Noevir Holdings Co., Ltd.｜最後の提案 10/22（reversal 4695・✅即時可）｜提案2回｜当夜 評価外
- 📉決算反応日 11/12 4544 H.U.Group Holdings, Inc.｜最後の提案 10/20（momentum 3720・✅即時可）｜提案3回｜当夜 評価外
- 📉決算反応日 11/12 2980 SRE Holdings Corp.｜最後の提案 10/16（momentum 2398・✅即時可）｜提案1回｜当夜 評価外
- 📉決算反応日 11/12 4183 Mitsui Chemicals, Inc.｜最後の提案 10/16（momentum 2108・✅即時可）｜提案2回｜当夜 評価外
- 📉決算反応日 11/12 4331 Take and Give. Needs Co., Ltd.｜最後の提案 10/16（momentum 834・✅即時可）｜提案1回｜当夜 評価外
- 📉決算反応日 11/11 8043 Starzen Company Limited｜最後の提案 10/16（oshime 1524・✅即時可）｜提案2回｜当夜 評価外
- 📉決算反応日 11/11 8097 SAN-AI OBBLI CO. LTD｜最後の提案 10/15（oshime 2440・✅即時可）｜提案1回｜当夜 評価外
- 📉決算反応日 11/11 2122 インタースペース｜最後の提案 10/14（reversal 1365・✅即時可）｜提案1回｜当夜 評価外
- ⏰決算 11/13(残2営業日) 1961 三機工業｜最後の提案 11/11（reversal 2412・✅即時可）｜提案3回｜当夜 PASS
- ⏰決算 11/13(残2営業日) 2962 テクニスコ｜最後の提案 11/11（reversal 1607・✅即時可）｜提案3回｜当夜 PASS
- ⏰決算 11/13(残2営業日) 3374 Naigai Tec Corporation｜最後の提案 11/11（reversal 4110・✅即時可）｜提案6回｜当夜 PASS
- ⏰決算 11/13(残2営業日) 3927 アークン｜最後の提案 11/11（momentum 933・⏸位置不適(25MA下 -9.3%／52週 26.3%)）｜提案6回｜当夜 PASS
- ⏰決算 11/13(残2営業日) 4634 ａｒｔｉｅｎｃｅ（ａｒｔｉｅｎ）｜最後の提案 11/11（reversal 4875・✅即時可）｜提案2回｜当夜 PASS
- ⏰決算 11/13(残2営業日) 5027 AnyMind Group Inc.｜最後の提案 11/11（momentum 734・⏸位置不適(25MA下 -4.64%)）｜提案6回｜当夜 PASS
- ⏰決算 11/13(残2営業日) 5844 Kyoto Financial Group,Inc.｜最後の提案 11/11（reversal 4241・✅即時可）｜提案5回｜当夜 PASS
- ⏰決算 11/13(残2営業日) 6268 Nabtesco Corporation｜最後の提案 11/11（reversal 4235・✅即時可）｜提案3回｜当夜 PASS
- ⏰決算 11/13(残2営業日) 6317 Kitagawa Corporation｜最後の提案 11/11（reversal 2293・✅即時可）｜提案1回｜当夜 PASS
- ⏰決算 11/13(残2営業日) 6407 CKD｜最後の提案 11/11（reversal 4139・✅即時可）｜提案5回｜当夜 PASS
- ⏰決算 11/13(残2営業日) 6481 THK Co., Ltd.｜最後の提案 11/11（reversal 5579・✅即時可）｜提案2回｜当夜 PASS
- ⏰決算 11/13(残2営業日) 6742 京三製作所｜最後の提案 11/11（reversal 975・✅即時可）｜提案3回｜当夜 PASS
- ⏰決算 11/13(残2営業日) 6840 ＡＫＩＢＡホールディングス｜最後の提案 11/11（reversal 641・✅即時可）｜提案3回｜当夜 PASS
- ⏰決算 11/13(残2営業日) 6877 ＯＢＡＲＡ　ＧＲＯＵＰ（ＯＢＡＲＡＧ）｜最後の提案 11/11（oshime 6762・✅即時可）｜提案1回｜当夜 PASS
- ⏰決算 11/16(残3営業日) 6890 Ferrotec Corporation｜最後の提案 11/11（reversal 7617・✅即時可）｜提案4回｜当夜 PASS
- ⏰決算 11/13(残2営業日) 7322 San ju San Financial Group, Inc.｜最後の提案 11/11（reversal 1859・✅即時可）｜提案4回｜当夜 PASS
- ⏰決算 11/13(残2営業日) 7384 Procrea Holdings,Inc.｜最後の提案 11/11（reversal 4130・✅即時可）｜提案9回｜当夜 PASS
- ⏰決算 11/13(残2営業日) 8344 Yamagata Bank, Ltd.｜最後の提案 11/11（reversal 4410・✅即時可）｜提案3回｜当夜 PASS
- ⏰決算 11/13(残2営業日) 8364 清水銀行｜最後の提案 11/11（reversal 2812・✅即時可）｜提案5回｜当夜 PASS
- ⏰決算 11/13(残2営業日) 8366 Shiga Bank, Ltd.｜最後の提案 11/11（reversal 2374・✅即時可）｜提案4回｜当夜 PASS
- ⏰決算 11/13(残2営業日) 8522 Bank of Nagoya, Ltd.｜最後の提案 11/11（reversal 5860・✅即時可）｜提案6回｜当夜 PASS
- ⏰決算 11/13(残2営業日) 8600 トモニホールディングス｜最後の提案 11/11（reversal 1029・✅即時可）｜提案6回｜当夜 PASS
- ⏰決算 11/13(残2営業日) 8714 池田泉州ホールディングス｜最後の提案 11/11（reversal 863・✅即時可）｜提案3回｜当夜 PASS
- ⏰決算 11/13(残2営業日) 3556 RenetJapanGroup, Inc.｜最後の提案 11/10（momentum 922・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- ⏰決算 11/13(残2営業日) 3851 日本一ソフトウェア｜最後の提案 11/10（reversal 1162・✅即時可）｜提案3回｜当夜 FAIL_UWAHIGE
- ⏰決算 11/13(残2営業日) 3923 ラクス｜最後の提案 11/10（changepoint 1155.5・✅即時可）｜提案3回｜当夜 FAIL_UWAHIGE
- ⏰決算 11/13(残2営業日) 4011 Headwaters Co.,Ltd｜最後の提案 11/10（changepoint 1927・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- ⏰決算 11/13(残2営業日) 4053 Sun Asterisk, Inc.｜最後の提案 11/10（momentum 579・✅即時可）｜提案5回｜当夜 FAIL_INSEN
- ⏰決算 11/16(残3営業日) 478A Hutzper Inc.｜最後の提案 11/10（changepoint 668・✅即時可）｜提案5回｜当夜 FAIL_INSEN
- ⏰決算 11/13(残2営業日) 479A PRONI Inc.｜最後の提案 11/10（reversal 1545・✅即時可）｜提案3回｜当夜 FAIL_UWAHIGE
- ⏰決算 11/13(残2営業日) 5137 Smart Drive Co. Ltd.｜最後の提案 11/10（momentum 313・✅即時可）｜提案5回｜当夜 FAIL_UWAHIGE
- ⏰決算 11/13(残2営業日) 5252 日本ナレッジ｜最後の提案 11/10（reversal 931・✅即時可）｜提案3回｜当夜 PASS
- ⏰決算 11/13(残2営業日) 6676 BUFFALO INC.｜最後の提案 11/10（reversal 3180・✅即時可）｜提案1回｜当夜 FAIL_UWAHIGE
- ⏰決算 11/13(残2営業日) 7744 Noritsu Koki Co., Ltd.｜最後の提案 11/10（momentum 2046・✅即時可）｜提案4回｜当夜 FAIL_INSEN
- ⏰決算 11/13(残2営業日) 3042 セキュアヴェイル（セキュアヴェ）｜最後の提案 11/09（oshime 891・⏳待機: 到達まで乖離8.7%）｜提案1回｜当夜 FAIL_INSEN
- ⏰決算 11/13(残2営業日) 3989 シェアテク｜最後の提案 11/09（changepoint 1539・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- ⏰決算 11/13(残2営業日) 4058 Toyokumo, Inc.｜最後の提案 11/09（momentum 2189・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- ⏰決算 11/13(残2営業日) 4293 セプテーニ・ホールディングス（セプテニＨＤ）｜最後の提案 11/09（reversal 461・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- ⏰決算 11/16(残3営業日) 5105 ＴＯＹＯ　ＴＩＲＥ｜最後の提案 11/09（momentum 4249・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- ⏰決算 11/13(残2営業日) 8388 阿波銀行｜最後の提案 11/09（reversal 1760・✅即時可）｜提案1回｜当夜 PASS
- ⏰決算 11/13(残2営業日) 9552 クオンツ総研ホールディングス｜最後の提案 11/09（oshime 1066・✅即時可）｜提案1回｜当夜 FAIL_UWAHIGE
- ⏰決算 11/13(残2営業日) 265A エイチエムコム｜最後の提案 11/06（changepoint 587・✅即時可）｜提案1回｜当夜 PASS
- ⏰決算 11/13(残2営業日) 286A ユカリア｜最後の提案 11/06（changepoint 755・✅即時可）｜提案1回｜当夜 FAIL_UWAHIGE
- ⏰決算 11/13(残2営業日) 6071 IBJ, Inc.｜最後の提案 11/06（momentum 919・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- ⏰決算 11/13(残2営業日) 6227 AIMECHATEC Ltd.｜最後の提案 11/06（reversal 4025・✅即時可）｜提案2回｜当夜 FAIL_UWAHIGE
- ⏰決算 11/13(残2営業日) 6597 HPC SYSTEMS Inc.｜最後の提案 11/06（reversal 2396・✅即時可）｜提案3回｜当夜 評価外
- ⏰決算 11/13(残2営業日) 7161 Jimoto Holdings, Inc.｜最後の提案 11/06（momentum 500・✅即時可）｜提案3回｜当夜 評価外
- ⏰決算 11/13(残2営業日) 7318 セレンディップ・ホールディングス｜最後の提案 11/06（changepoint 1031・✅即時可）｜提案3回｜当夜 PASS
- ⏰決算 11/13(残2営業日) 7695 交換できるくん｜最後の提案 11/06（changepoint 830・✅即時可）｜提案5回｜当夜 FAIL_INSEN
- ⏰決算 11/13(残2営業日) 5101 Yokohama Rubber Co., Ltd.｜最後の提案 11/05（reversal 7251・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- ⏰決算 11/13(残2営業日) 7747 朝日インテック｜最後の提案 11/05（momentum 3920・✅即時可）｜提案3回｜当夜 FAIL_UWAHIGE
- ⏰決算 11/13(残2営業日) 8253 Credit Saison Co., Ltd.｜最後の提案 11/05（reversal 4233・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- ⏰決算 11/13(残2営業日) 1860 Toda Corporation｜最後の提案 10/29（reversal 1465.5・✅即時可）｜提案7回｜当夜 FAIL_UWAHIGE
- ⏰決算 11/13(残2営業日) 4180 ＡＰＰＩＥＲ　ＧＲＯＵＰ｜最後の提案 10/29（oshime 1412.2・✅即時可）｜提案2回｜当夜 評価外
- ⏰決算 11/16(残3営業日) 5582 （名称取得不可）｜最後の提案 10/29（changepoint 1819・✅即時可）｜提案4回｜当夜 FAIL_INSEN
- ⏰決算 11/13(残2営業日) 5757 CK San-Etsu Co., Ltd.｜最後の提案 10/29（momentum 4505・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- ⏰決算 11/13(残2営業日) 593A ティアフォー｜最後の提案 10/29（changepoint 2364・✅即時可）｜提案4回｜当夜 PASS
- ⏰決算 11/13(残2営業日) 6736 Suncorporation｜最後の提案 10/29（oshime 9748.9・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- ⏰決算 11/13(残2営業日) 8360 Yamanashi Chuo Bank, Ltd.｜最後の提案 10/29（reversal 1321・✅即時可）｜提案5回｜当夜 PASS
- ⏰決算 11/13(残2営業日) 9553 MicroAd, Inc.｜最後の提案 10/29（momentum 593・✅即時可）｜提案6回｜当夜 評価外
- ⏰決算 11/13(残2営業日) 3691 DIGITAL PLUS, Inc.｜最後の提案 10/28（reversal 1487・✅即時可）｜提案2回｜当夜 FAIL_UWAHIGE
- ⏰決算 11/13(残2営業日) 584A LiNKX, Inc.｜最後の提案 10/27（changepoint 2308・✅即時可）｜提案4回｜当夜 評価外
- ⏰決算 11/13(残2営業日) 8524 North Pacific Bank, Ltd.｜最後の提案 10/27（reversal 1176・✅即時可）｜提案4回｜当夜 PASS
- ⏰決算 11/13(残2営業日) 8713 Fidea Holdings Co.Ltd.｜最後の提案 10/27（reversal 2527・✅即時可）｜提案5回｜当夜 PASS
- ⏰決算 11/13(残2営業日) 6203 Howa Machinery, Ltd.｜最後の提案 10/26（reversal 2279・✅即時可）｜提案3回｜当夜 PASS
- ⏰決算 11/13(残2営業日) 6298 Y.A.C.HOLDINGS CO.,LTD.｜最後の提案 10/26（momentum 1099・✅即時可）｜提案3回｜当夜 評価外
- ⏰決算 11/13(残2営業日) 8944 Land Business Co., Ltd.｜最後の提案 10/26（momentum 256・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- ⏰決算 11/13(残2営業日) 9211 f-code Inc.｜最後の提案 10/26（momentum 1204・✅即時可）｜提案2回｜当夜 評価外
- ⏰決算 11/13(残2営業日) 477A Startline CO.,LTD.｜最後の提案 10/23（reversal 750・✅即時可）｜提案1回｜当夜 FAIL_UWAHIGE
- ⏰決算 11/13(残2営業日) 8995 Makoto Construction Co,Ltd｜最後の提案 10/23（reversal 1484・✅即時可）｜提案1回｜当夜 FAIL_UWAHIGE
- ⏰決算 11/13(残2営業日) 4493 Cyber Security Cloud, Inc.｜最後の提案 10/22（changepoint 3865・✅即時可）｜提案2回｜当夜 評価外
- ⏰決算 11/13(残2営業日) 5038 eWeLL Co.,Ltd｜最後の提案 10/21（momentum 2331・✅即時可）｜提案1回｜当夜 評価外
- ⏰決算 11/13(残2営業日) 3097 Monogatari Corporation｜最後の提案 10/20（oshime 5520・⏳待機: 到達まで乖離-9.4%）｜提案3回｜当夜 評価外
- ⏰決算 11/13(残2営業日) 5242 EYEZ INC.｜最後の提案 10/20（reversal 2866・✅即時可）｜提案5回｜当夜 評価外
- ⏰決算 11/13(残2営業日) 1815 鉄建建設｜最後の提案 10/19（momentum 2191・✅即時可）｜提案2回｜当夜 評価外
- ⏰決算 11/13(残2営業日) 4691 Washington Hotel Corp.｜最後の提案 10/19（reversal 1913・✅即時可）｜提案1回｜当夜 評価外
- ⏰決算 11/13(残2営業日) 6254 野村マイクロ・サイエンス｜最後の提案 10/19（changepoint 3160・✅即時可）｜提案2回｜当夜 評価外
- ⏰決算 11/13(残2営業日) 6379 RAIZNEXT Corporation｜最後の提案 10/19（oshime 1000・✅即時可）｜提案3回｜当夜 評価外
- ⏰決算 11/13(残2営業日) 6804 Hosiden Corp.｜最後の提案 10/19（reversal 2380・✅即時可）｜提案2回｜当夜 FAIL_UWAHIGE
- ⏰決算 11/16(残3営業日) 7047 PORT INC.｜最後の提案 10/19（momentum 2172・✅即時可）｜提案1回｜当夜 評価外
- ⏰決算 11/13(残2営業日) 9554 AViC Co. Ltd.｜最後の提案 10/19（momentum 1721・✅即時可）｜提案2回｜当夜 評価外
- ⏰決算 11/13(残2営業日) 4166 Cacco, Inc.｜最後の提案 10/16（momentum 733・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- ⏰決算 11/16(残3営業日) 4346 NEXYZ.Group Corporation｜最後の提案 10/16（reversal 750・✅即時可）｜提案2回｜当夜 評価外
- ⏰決算 11/13(残2営業日) 5892 yutori,Inc.｜最後の提案 10/16（momentum 3180・✅即時可）｜提案2回｜当夜 PASS
- ⏰決算 11/13(残2営業日) 6562 Geniee, Inc.｜最後の提案 10/16（momentum 1005・✅即時可）｜提案1回｜当夜 評価外
- ⏰決算 11/16(残3営業日) 8952 Japan Real Estate Investment Corp.｜最後の提案 10/15（reversal 107800・✅即時可）｜提案1回｜当夜 評価外
- ⏰決算 11/13(残2営業日) 1518 三井松島ホールディングス｜最後の提案 10/14（oshime 2275・✅即時可）｜提案1回｜当夜 評価外
- ⏰決算 11/13(残2営業日) 4392 ＦＩＧ｜最後の提案 10/14（reversal 990・✅即時可）｜提案1回｜当夜 評価外
- ⏰決算 11/13(残2営業日) 4418 JAPAN DATA SCIENCE CONSORTIUM C｜最後の提案 10/14（oshime 1112・✅即時可）｜提案1回｜当夜 評価外
- ⏰決算 11/13(残2営業日) 9268 OPTIMUS GROUP Co., Ltd.｜最後の提案 10/14（momentum 363・✅即時可）｜提案1回｜当夜 評価外
- 📋カルテ窓 12/10(残20営業日) 3491 ＧＡ　ｔｅｃｈｎｏｌｏｇｉｅｓ（ＧＡテクノ）｜最後の提案 11/11（momentum 1568・✅即時可）｜提案2回｜当夜 PASS
- 📋カルテ窓 12/08(残18営業日) 9824 泉州電業｜最後の提案 11/11（momentum 7880・⏸位置不適(25MA下 -2.36%)）｜提案6回｜当夜 PASS
- 📋カルテ窓 12/08(残18営業日) 1436 GreenEnergy & Company｜最後の提案 11/10（reversal 1368・✅即時可）｜提案3回｜当夜 FAIL_UWAHIGE
- 📋カルテ窓 12/04(残16営業日) 436A サイバーソリューションズ（サイバＳＯＬ）｜最後の提案 11/10（oshime 1776・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 📋カルテ窓 12/09(残19営業日) 7678 ASAKUMA CO.,LTD.｜最後の提案 11/10（momentum 4405・✅即時可）｜提案6回｜当夜 FAIL_INSEN
- 📋カルテ窓 12/10(残20営業日) 1928 積水ハウス｜最後の提案 11/09（momentum 3568・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- 📋カルテ窓 12/09(残19営業日) 5132 pluszero,Inc.｜最後の提案 11/04（momentum 1761・✅即時可）｜提案3回｜当夜 FAIL_UWAHIGE
- 📋カルテ窓 12/10(残20営業日) 8927 Meiho Enterprise Co., Ltd.｜最後の提案 10/29（momentum 466・✅即時可）｜提案1回｜当夜 評価外
- 📋カルテ窓 12/07(残17営業日) 7856 HAGIHARA INDUSTRIES INC.｜最後の提案 10/19（oshime 2044・✅即時可）｜提案3回｜当夜 評価外
- 📋カルテ窓 12/04(残16営業日) 9678 Kanamoto Co., Ltd.｜最後の提案 10/14（oshime 5420・✅即時可）｜提案1回｜当夜 評価外

## 前夜の結果
PL5口座への正式な反映は週次①-11の採点で行われる。ここは参考情報。
前夜2026-11-10 の提案119件 → 約定109・不約定10・判定不能0
- 6890 reversal 注文6832 → 約定6,829.0・終値7,617（+11.54%）
- 6862 reversal 注文3060 → 約定3,060・終値3,360（+9.80%）
- 4062 reversal 注文6418 → 約定6,342.0・終値6,920（+9.11%）
- 6524 reversal 注文4485 → 約定4,435.0・終値4,825（+8.79%）
- 5801 reversal 注文2197 → 約定2,190.0・終値2,373（+8.36%）
- （下位）7678 momentum 注文4405 → 約定4,405・終値4,275（-2.95%）
- （下位）446A momentum 注文2544 → 約定2,544・終値2,404（-5.50%）
- （下位）6570 oshime 注文4290 → 約定4,290・終値3,755（-12.47%）
- 約定109件の含み損益 中央値 +1.91%

## 模擬テンプレ
```
# base_day 2026-11-11 ／ 提案154件
# 使い方: 参戦する0〜3銘柄の行だけをコピーし、｜の後ろに参戦理由を書いてポジション株PJへ送る。
# 選ばなかった行は送らなくてよい（全行に理由を書く必要はない）。見送りは末尾の1行で足りる。
# 特定銘柄を理由つきで見送る場合のみ『模擬 見送り {code} ｜{理由}』を送る。
模擬 5027 kenmo_momentum 逆指値734 SL689 単元100 ｜
模擬 3915 kenmo_momentum 逆指値2176 SL2044.5 単元100 ｜
模擬 5821 kenmo_momentum 逆指値3330 SL3125.5 単元100 ｜
模擬 4477 kenmo_momentum 逆指値312 SL292.3 単元100 ｜
模擬 4743 kenmo_momentum 逆指値1585 SL1489 単元100 ｜
模擬 618A kenmo_momentum 逆指値1969 SL1849.9 単元100 ｜
模擬 9204 kenmo_newhigh 逆指値477 SL447.4 単元100 ｜
模擬 7995 choruko_reversal 指値6260 SL5130 単元100 ｜
模擬 6516 choruko_reversal 指値4615 SL3945 単元100 ｜
模擬 8336 choruko_reversal 指値2555 SL2200 単元100 ｜
模擬 4216 choruko_reversal 指値5720 SL5160 単元100 ｜
模擬 4471 choruko_reversal 指値1510 SL1408 単元100 ｜
模擬 5703 choruko_reversal 指値2567 SL2338 単元100 ｜
模擬 7433 choruko_reversal 指値1615 SL1516 単元100 ｜
模擬 8084 choruko_reversal 指値2229 SL2025 単元100 ｜
模擬 5301 choruko_reversal 指値1665.5 SL1450.5 単元100 ｜
模擬 6268 choruko_reversal 指値4235 SL3622 単元100 ｜
模擬 6481 choruko_reversal 指値5579 SL4707 単元100 ｜
模擬 6652 choruko_reversal 指値3155 SL2905 単元100 ｜
模擬 6875 choruko_reversal 指値8720 SL7880 単元100 ｜
模擬 6471 choruko_reversal 指値1011 SL913 単元100 ｜
模擬 8386 choruko_reversal 指値2847 SL2390 単元100 ｜
模擬 6754 choruko_reversal 指値2435 SL2060 単元100 ｜
模擬 7731 choruko_reversal 指値1648 SL1497 単元100 ｜
模擬 9902 choruko_reversal 指値2957 SL2766 単元100 ｜
模擬 8133 choruko_reversal 指値2029 SL1966 単元100 ｜
模擬 5333 choruko_reversal 指値4834 SL4206 単元100 ｜
模擬 3433 choruko_reversal 指値2601 SL2123 単元100 ｜
模擬 5186 choruko_reversal 指値6430 SL5770 単元100 ｜
模擬 8522 choruko_reversal 指値5860 SL5250 単元100 ｜
模擬 6448 choruko_reversal 指値4603 SL4078 単元100 ｜
模擬 5331 choruko_reversal 指値3050 SL2683 単元100 ｜
模擬 7004 choruko_reversal 指値968 SL828 単元100 ｜
模擬 4205 choruko_reversal 指値2101.5 SL1881 単元100 ｜
模擬 6473 choruko_reversal 指値2081.5 SL1842 単元100 ｜
模擬 3569 choruko_reversal 指値3515 SL3100 単元100 ｜
模擬 4634 choruko_reversal 指値4875 SL4475 単元100 ｜
模擬 5444 choruko_reversal 指値10950 SL9989 単元100 ｜
模擬 8714 choruko_reversal 指値863 SL773 単元100 ｜
模擬 9934 choruko_reversal 指値2661.5 SL2513.5 単元100 ｜
模擬 1721 choruko_reversal 指値5177 SL4767 単元100 ｜
模擬 9072 choruko_reversal 指値4254 SL4007 単元100 ｜
模擬 9960 choruko_reversal 指値4385 SL3745 単元100 ｜
模擬 6135 choruko_reversal 指値2812 SL2450 単元100 ｜
模擬 6340 choruko_reversal 指値5090 SL4350 単元100 ｜
模擬 6674 choruko_reversal 指値4587 SL3940 単元100 ｜
模擬 8381 choruko_reversal 指値2190.5 SL1921 単元100 ｜
模擬 4272 choruko_reversal 指値1857.5 SL1752 単元100 ｜
模擬 4042 choruko_reversal 指値2497 SL2305.5 単元100 ｜
模擬 6332 choruko_reversal 指値2395 SL2096 単元100 ｜
模擬 6368 choruko_reversal 指値1800 SL1509 単元100 ｜
模擬 4028 choruko_reversal 指値2616 SL2195 単元100 ｜
模擬 3105 choruko_reversal 指値1991 SL1791 単元100 ｜
模擬 6741 choruko_reversal 指値1647 SL1508 単元100 ｜
模擬 6807 choruko_reversal 指値2324 SL2087 単元100 ｜
模擬 5310 choruko_reversal 指値6310 SL5360 単元100 ｜
模擬 1979 choruko_reversal 指値3365 SL3240 単元100 ｜
模擬 7278 choruko_reversal 指値5290 SL5010 単元100 ｜
模擬 5844 choruko_reversal 指値4241 SL3790 単元100 ｜
模擬 4746 choruko_reversal 指値1767 SL1667 単元100 ｜
模擬 6370 choruko_reversal 指値5445 SL4678 単元100 ｜
模擬 8367 choruko_reversal 指値1797 SL1558 単元100 ｜
模擬 7381 choruko_reversal 指値1146 SL985 単元100 ｜
模擬 8345 choruko_reversal 指値2128 SL1819 単元100 ｜
模擬 8370 choruko_reversal 指値1536 SL1419 単元100 ｜
模擬 7384 choruko_reversal 指値4130 SL3470 単元100 ｜
模擬 8366 choruko_reversal 指値2374 SL2097.5 単元100 ｜
模擬 6810 choruko_reversal 指値2205 SL2010 単元100 ｜
模擬 7177 choruko_reversal 指値1060 SL960 単元100 ｜
模擬 7322 choruko_reversal 指値1859 SL1579 単元100 ｜
模擬 8600 choruko_reversal 指値1029 SL901 単元100 ｜
模擬 8616 choruko_reversal 指値776 SL705 単元100 ｜
模擬 6777 ai_momentum 逆指値21330 SL20040.8 単元100 ｜
模擬 9824 ai_momentum 逆指値7880 SL7397.8 単元100 ｜
模擬 6613 ai_momentum 逆指値2222 SL2087.7 単元100 ｜
模擬 4063 ai_momentum 逆指値5745 SL5390.9 単元100 ｜
模擬 1975 ai_momentum 逆指値3485 SL3271.2 単元100 ｜
模擬 1982 ai_momentum 逆指値3195 SL2998.6 単元100 ｜
模擬 5803 ai_reversal 指値3121 SL2622.5 単元100 ｜
模擬 4047 ai_reversal 指値1812 SL1460 単元100 ｜
模擬 6918 ai_reversal 指値3270 SL2804 単元100 ｜
模擬 3374 ai_reversal 指値4110 SL3300 単元100 ｜
模擬 4062 ai_reversal 指値6920 SL5726 単元100 ｜
模擬 6857 ai_reversal 指値31440 SL24655 単元100 ｜
模擬 5801 ai_reversal 指値2373 SL1692.5 単元100 ｜
模擬 6787 ai_reversal 指値8320 SL5650 単元100 ｜
模擬 8035 ai_reversal 指値9272 SL7502 単元100 ｜
模擬 6407 ai_reversal 指値4139 SL3430 単元100 ｜
模擬 3110 ai_reversal 指値2802 SL1931 単元100 ｜
模擬 4368 ai_reversal 指値3020 SL2450 単元100 ｜
模擬 6779 ai_reversal 指値1984 SL1713 単元100 ｜
模擬 2760 ai_reversal 指値3985 SL3235 単元100 ｜
模擬 6235 ai_reversal 指値2289 SL1673 単元100 ｜
模擬 6762 ai_reversal 指値2365.5 SL1972.5 単元100 ｜
模擬 6981 ai_reversal 指値5457 SL4286 単元100 ｜
模擬 7729 ai_reversal 指値13495 SL9922 単元100 ｜
模擬 6323 ai_reversal 指値3365 SL2560.5 単元100 ｜
模擬 7735 ai_reversal 指値8777 SL7125 単元100 ｜
模擬 6941 ai_reversal 指値6960 SL5090 単元100 ｜
模擬 6524 ai_reversal 指値4825 SL3510 単元100 ｜
模擬 5384 ai_reversal 指値3010 SL2449 単元100 ｜
模擬 6752 ai_reversal 指値3257 SL2808 単元100 ｜
模擬 6336 ai_reversal 指値1266 SL998 単元100 ｜
模擬 4973 ai_reversal 指値4120 SL3650 単元100 ｜
模擬 6590 ai_reversal 指値2921 SL2035 単元100 ｜
模擬 5706 ai_reversal 指値1669.5 SL1384 単元100 ｜
模擬 5208 ai_reversal 指値2334 SL1979 単元100 ｜
模擬 6965 ai_reversal 指値2357.5 SL1800.5 単元100 ｜
模擬 6617 ai_reversal 指値5180 SL4195 単元100 ｜
模擬 4203 ai_reversal 指値7574 SL5690 単元100 ｜
模擬 1961 ai_reversal 指値2412 SL2046 単元100 ｜
模擬 6146 ai_reversal 指値47580 SL37210 単元100 ｜
模擬 6723 ai_reversal 指値2922 SL2228 単元100 ｜
模擬 9984 ai_reversal 指値3855 SL3350 単元100 ｜
模擬 3927 granville_tenkan 逆指値933 SL876.1 単元100 ｜
模擬 6768 granville_tenkan 逆指値732 SL687.1 単元100 ｜
模擬 3491 granville_tenkan 逆指値1568 SL1473 単元100 ｜
模擬 8012 granville_tenkan 逆指値1216.5 SL1142.6 単元100 ｜
模擬 9742 granville_tenkan 逆指値2399 SL2254.1 単元100 ｜
模擬 6371 granville_tenkan 逆指値2649 SL2489.1 単元100 ｜
模擬 4617 granville_tenkan 逆指値3585 SL3365.2 単元100 ｜
模擬 4403 granville_tenkan 逆指値2570 SL2476.5 単元100 ｜
模擬 7606 granville_tenkan 逆指値2629 SL2470.3 単元100 ｜
模擬 8056 granville_tenkan 逆指値4660 SL4375.7 単元100 ｜
模擬 4375 granville_tenkan 逆指値622 SL583.7 単元100 ｜
模擬 6877 granville_oshime 指値6762 SL6728.4 単元100 ｜
模擬 6080 granville_oshime 指値4333 SL4311.4 単元100 ｜
模擬 3891 granville_rebound 指値5790 SL4405 単元100 ｜
模擬 6138 granville_rebound 指値1760 SL1532 単元100 ｜
模擬 6862 granville_rebound 指値3360 SL2326 単元100 ｜
模擬 4968 granville_rebound 指値1969 SL1580 単元100 ｜
模擬 2962 granville_rebound 指値1607 SL1206 単元100 ｜
模擬 4419 granville_rebound 指値1237 SL1123 単元100 ｜
模擬 2489 granville_rebound 指値334 SL308 単元100 ｜
模擬 3793 granville_rebound 指値457 SL398 単元100 ｜
模擬 6317 granville_rebound 指値2293 SL2069 単元100 ｜
模擬 8364 granville_rebound 指値2812 SL2436 単元100 ｜
模擬 460A granville_rebound 指値1098 SL949 単元100 ｜
模擬 6508 granville_rebound 指値7616 SL6374 単元100 ｜
模擬 5367 granville_rebound 指値1076 SL850 単元100 ｜
模擬 6958 granville_rebound 指値747 SL604 単元100 ｜
模擬 8344 granville_rebound 指値4410 SL3730 単元100 ｜
模擬 6742 granville_rebound 指値975 SL840 単元100 ｜
模擬 5574 granville_rebound 指値2041 SL1757 単元100 ｜
模擬 4025 granville_rebound 指値5360 SL4910 単元100 ｜
模擬 8368 granville_rebound 指値2136 SL1822 単元100 ｜
模擬 7184 granville_rebound 指値3200 SL2765 単元100 ｜
模擬 3371 granville_rebound 指値2047 SL1914 単元100 ｜
模擬 6840 granville_rebound 指値641 SL521 単元100 ｜
模擬 6890 granville_rebound 指値7617 SL5701 単元100 ｜
模擬 7826 granville_rebound 指値9050 SL6970 単元100 ｜
模擬 8551 granville_rebound 指値2373 SL2018 単元100 ｜
模擬 8609 granville_rebound 指値1048 SL925 単元100 ｜
模擬 218A changepoint 指値830 SL695 単元100 🔒 ｜
模擬 見送り ｜
```

## PASS内訳
PASS 240件 = 提案 154件（✅即時可140／⏳待機・確認足待ち1／⏸位置不適12／⏸トラップ疑い1） + 除外 86件（型不一致18（うち十字線0）/材料後出し17/鮮度切れ45/その他6）
- 147A SORACOM,INC.: ⛔提案なし(材料後出し)（nom_age 0）
- 3696 セレス: ⛔提案なし(指名鮮度切れ 17営業日)（nom_age 17）
- 3843 Freebit Co., Ltd.: ⛔提案なし(指名鮮度切れ 15営業日)（nom_age 15）
- 5711 三菱マテリアル: ⛔提案なし(材料後出し)（nom_age 5）
- 6278 ユニオンツール: ⛔提案なし(材料後出し)（nom_age 8）
- 5344 MARUWA CO., LTD.: ⛔提案なし(指名鮮度切れ 13営業日)（nom_age 13）
- 6645 OMRON Corporation: ⛔提案なし(指名鮮度切れ 13営業日)（nom_age 13）
- 6324 Harmonic Drive Systems Inc.: ⛔提案なし(指名鮮度切れ 14営業日)（nom_age 14）
- 6925 Ushio Inc.: ⛔提案なし(指名鮮度切れ 13営業日)（nom_age 13）
- 5019 出光興産: ⛔提案なし(材料後出し)（nom_age 4）
- 4088 Air Water Inc.: ⛔提案なし(指名鮮度切れ 13営業日)（nom_age 13）
- 7721 Tokyo Keiki Inc.: ⛔提案なし(指名鮮度切れ 17営業日)（nom_age 17）
- 8393 Miyazaki Bank Ltd.: ⛔提案なし(指名鮮度切れ 14営業日)（nom_age 14）
- 6284 日精エー・エス・ビー機械: ⛔提案なし(材料後出し)（nom_age 0）
- 268A Rigaku Holdings Corporation: ⛔提案なし(指名鮮度切れ 13営業日)（nom_age 13）
- 6923 Stanley Electric Co., Ltd.: ⛔提案なし(材料後出し)（nom_age 5）
- 8524 North Pacific Bank, Ltd.: ⛔提案なし(指名鮮度切れ 13営業日)（nom_age 13）
- 5631 Japan Steel Works, Ltd.: ⛔提案なし(指名鮮度切れ 18営業日)（nom_age 18）
- 1944 Kinden Corporation: ⛔提案なし(指名鮮度切れ 18営業日)（nom_age 18）
- 1952 Shin Nippon Air Technologies Co., Ltd.: ⛔提案なし(指名鮮度切れ 18営業日)（nom_age 18）
- 6055 Japan Material Co., Ltd.: ⛔提案なし(指名鮮度切れ 13営業日)（nom_age 13）
- 3445 RS Technologies Co. Ltd.: ⛔提案なし(指名鮮度切れ 13営業日)（nom_age 13）
- 1946 Toenec Corporation: ⛔提案なし(指名鮮度切れ 18営業日)（nom_age 18）
- 4980 Dexerials Corp.: ⛔提案なし(材料後出し)（nom_age 6）
- 7003 Mitsui ES Holdings Co., Ltd.: ⛔提案なし(指名鮮度切れ 19営業日)（nom_age 19）
- 5482 Aichi Steel Corporation: ⛔提案なし(指名鮮度切れ 18営業日)（nom_age 18）
- 1963 日揮ホールディングス: ⛔提案なし(材料後出し)（nom_age 8）
- 8359 Hachijuni Nagano Bank, Ltd.: ⛔提案なし(材料後出し)（nom_age 9）
- 8334 Gunma Bank, Ltd.: ⛔提案なし(指名鮮度切れ 13営業日)（nom_age 13）
- 7186 横浜フィナンシャルグループ: ⛔提案なし(材料後出し)（nom_age 8）
- 6668 ＡＤプラズマ: ⛔提案なし(手法ブランチ不明)（nom_age 3）
- 7713 シグマ光機: ⛔提案なし(手法ブランチ不明)（nom_age 3）
- 5832 ちゅうぎんフィナンシャルグループ（ちゅうぎんＦ）: ⛔提案なし(手法ブランチ不明)（nom_age 0）
- 9962 ミスミグループ本社: ⛔提案なし(手法ブランチ不明)（nom_age 0）
- 6814 古野電: ⛔提案なし(手法ブランチ不明)（nom_age 3）
- 5932 三協立山: ⛔提案なし(手法ブランチ不明)（nom_age 4）
- 6521 オキサイド: ⛔提案なし(指名鮮度切れ 12営業日)（nom_age 12）
- 3131 Shinden Hightex Corp.: ⛔型不一致: 既に支持帯以下（nom_age 0）
- 4971 メック: ⛔提案なし(材料後出し)（nom_age 5）
- 3436 SUMCO: ⛔提案なし(材料後出し)（nom_age 1）
- 7725 INTER ACTION Corporation: ⛔提案なし(指名鮮度切れ 19営業日)（nom_age 19）
- 6470 Taiho Kogyo Co., Ltd.: ⛔提案なし(指名鮮度切れ 14営業日)（nom_age 14）
- 7970 Shin-Etsu Polymer Co., Ltd.: ⛔提案なし(指名鮮度切れ 14営業日)（nom_age 14）
- 8061 Seika Corporation: ⛔提案なし(指名鮮度切れ 19営業日)（nom_age 19）
- 4902 Konica Minolta, Inc.: ⛔提案なし(指名鮮度切れ 13営業日)（nom_age 13）
- 6574 コンヴァノ: ⛔型不一致: 既に支持帯以下（nom_age 5）
- 7480 スズデン: ⛔型不一致: 既に支持帯以下（nom_age 0）
- 6834 精工技研: ⛔型不一致: 既に支持帯以下（nom_age 5）
- 7609 ダイトロン: ⛔型不一致: 既に支持帯以下（nom_age 4）
- 4382 HEROZ, Inc.: ⛔型不一致: 既に支持帯以下（nom_age 9）
- 8137 サンワテクノス: ⛔型不一致: 既に支持帯以下（nom_age 6）
- 8392 大分銀行: ⛔型不一致: 既に支持帯以下（nom_age 8）
- 3156 レスター: ⛔型不一致: 既に支持帯以下（nom_age 3）
- 9304 澁澤倉庫: ⛔提案なし(指名鮮度切れ 12営業日)（nom_age 12）
- 5892 ＹＵＴＯＲＩ: ⛔型不一致: 既に支持帯以下（nom_age 9）
- 3040 ソリトンシステムズ: ⛔型不一致: 既に支持帯以下（nom_age 0）
- 4398 ブロードバンドセキュリティ: ⛔型不一致: 既に支持帯以下（nom_age 4）
- 2492 インフォマート（インフォＭＴ）: ⛔型不一致: 既に支持帯以下（nom_age 0）
- 8388 阿波銀行: ⛔型不一致: 既に支持帯以下（nom_age 0）
- 4498 Cybertrust Japan Co.Ltd.: ⛔型不一致: 既に支持帯以下（nom_age 1）
- 4258 AMIYA Corporation: ⛔提案なし(材料後出し)（nom_age 0）
- 8395 佐賀銀行: ⛔型不一致: 既に支持帯以下（nom_age 2）
- 5985 SUNCALL CORPORATION: ⛔提案なし(指名鮮度切れ 16営業日)（nom_age 16）
- 338A ZenmuTech,Inc.: ⛔型不一致: 既に支持帯以下（nom_age 7）
- 4044 Central Glass Co., Ltd.: ⛔提案なし(指名鮮度切れ 19営業日)（nom_age 19）
- 3993 PKSHA Technology, Inc.: ⛔型不一致: 既に支持帯以下（nom_age 1）
- 8362 Fukui Bank, Ltd.: ⛔提案なし(指名鮮度切れ 20営業日)（nom_age 20）
- 3778 SAKURA Internet Inc.: ⛔提案なし(指名鮮度切れ 18営業日)（nom_age 18）
- 6769 Thine Electronics, Inc.: ⛔提案なし(指名鮮度切れ 18営業日)（nom_age 18）
- 6963 ROHM Company Limited: ⛔提案なし(指名鮮度切れ 18営業日)（nom_age 18）
- 7715 長野計器: ⛔提案なし(指名鮮度切れ 11営業日)（nom_age 11）
- 5252 日本ナレッジ: ⛔提案なし(材料後出し)（nom_age 4）
- 4667 Aisan Technology Co.,Ltd.: ⛔提案なし(材料後出し)（nom_age 0）
- 278A Ｔｅｒｒａ　Ｄｒｏｎｅ: ⛔提案なし(指名鮮度切れ 11営業日)（nom_age 11）
- 4440 WITZ Corp.: ⛔提案なし(指名鮮度切れ 17営業日)（nom_age 17）
- 3687 Fixstars Corp.: ⛔提案なし(指名鮮度切れ 18営業日)（nom_age 18）
- 6203 Howa Machinery, Ltd.: ⛔提案なし(指名鮮度切れ 16営業日)（nom_age 16）
- 8360 Yamanashi Chuo Bank, Ltd.: ⛔提案なし(指名鮮度切れ 12営業日)（nom_age 12）
- 8377 ほくほくフィナンシャルグループ: ⛔提案なし(指名鮮度切れ 12営業日)（nom_age 12）
- 7380 Juroku Financial Group,Inc.: ⛔提案なし(指名鮮度切れ 14営業日)（nom_age 14）
- 8713 Fidea Holdings Co.Ltd.: ⛔提案なし(指名鮮度切れ 14営業日)（nom_age 14）
- 8739 スパークス・グループ: ⛔提案なし(指名鮮度切れ 11営業日)（nom_age 11）
- 265A エイチエムコム: ⛔提案なし(材料後出し)（nom_age 2）
- 6136 OSG CORP: ⛔提案なし(指名鮮度切れ 19営業日)（nom_age 19）
- 7318 セレンディップ・ホールディングス: ⛔提案なし(指名鮮度切れ 13営業日)（nom_age 13）
- 593A Tier IV, Inc.: ⛔提案なし(材料後出し)（nom_age 1）

## 5手法銘柄
- 5137 Smart Drive Co. Ltd.｜kenmo_momentum｜🚀確変｜💎割安｜FAIL_UWAHIGE｜309円｜💰3.1万円｜—
- 276A CCReB Advisors Inc.｜kenmo_momentum/granville_oshime｜🚀確変｜🟢値頃｜FAIL_INSEN｜4,025円｜💰40.9万円｜—
- 3556 RenetJapanGroup, Inc.｜kenmo_momentum/granville_tenkan｜🚀確変｜🟢値頃｜FAIL_INSEN｜915円｜💰9.2万円｜—
- 5027 AnyMind Group Inc.｜kenmo_momentum/granville_oshime/granville_rebound/changepoint｜🚀確変｜⚪妥当｜PASS｜730円｜💰7.3万円｜momentum 734/SL689（⏸位置不適(25MA下 -4.64%)）｜⏰決算 11/13(残2営業日) ⚠市場に劣後 RS20 -5.8pt
  > 【業態】ブランド企業向けマーケティング支援やクリエイター向け収益化支援。海外売上が大。
  > 【いま】終値730円・直近5日+1.25%（材料未確認）
  > 【調子】🚀確変（11/13） — E軸判定不能(進捗データ不足)
  > 【水準】⚪妥当（4.0/7）— PER26.55倍・PEG0.3397・52週67% ／ 💰単元7.3万円
  > 【戦略】当日高値超えの逆指値734円で順張り参戦を検討。上限741.3円・SL689円目安（⏸位置不適(25MA下 -4.64%)）
- 4053 Sun Asterisk, Inc.｜kenmo_momentum｜🚀確変｜⚪妥当｜FAIL_INSEN｜564円｜💰5.7万円｜—
- 4434 Serverworks Co., Ltd.｜kenmo_momentum/stf_kakuhen/granville_oshime｜🚀確変｜⚪妥当｜FAIL_UWAHIGE｜3,060円｜💰30.4万円｜—
- 5136 tripla Co.,Ltd.｜kenmo_momentum/granville_oshime/changepoint｜🚀確変｜⚪妥当｜FAIL_UWAHIGE｜2,743円｜💰27.1万円｜—
- 5757 CK San-Etsu Co., Ltd.｜kenmo_momentum｜🔥絶好調｜💎割安｜FAIL_INSEN｜4,585円｜💰45.5万円｜—
- 3915 TerraSky Co., Ltd.｜kenmo_momentum｜🔥絶好調｜🟢値頃｜PASS｜2,170円｜💰21.7万円｜momentum 2176/SL2044.5（⏸位置不適(25MA下 -3.64%)）｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8） 📐進捗 上振れ 34.1%
  > 【業態】クラウドシステムの導入支援や開発。セールスフォースと提携。大企業、AWS向け拡大。
  > 【いま】終値2,170円・直近5日+5.49%（材料未確認）
  > 【調子】🔥絶好調（10/13） — 🔼進捗先行
  > 【水準】🟢値頃（5.0/7）— PER18.36倍・PEG0.3519・52週30.4% ／ 💰単元21.7万円
  > 【戦略】当日高値超えの逆指値2176円で順張り参戦を検討。上限2197.8円・SL2044.5円目安（⏸位置不適(25MA下 -3.64%)）
- 421A Movin' Strategic Career CO.,LTD.｜kenmo_momentum/kenmo_newhigh｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜3,480円｜💰34.7万円｜—｜⚡材料後出し
- 4286 CL Holdings Inc.｜kenmo_momentum/kenmo_newhigh｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜1,418円｜💰13.6万円｜—｜🎯2手法一致
- 1435 robot home Inc.｜kenmo_momentum｜🔥絶好調｜💎割安｜FAIL_UWAHIGE｜162円｜💰1.6万円｜—
- 5132 pluszero,Inc.｜kenmo_momentum｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜1,794円｜💰17.8万円｜—
- 4377 ONE CAREER Inc.｜kenmo_momentum/granville_oshime/granville_rebound｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜2,363円｜💰24.2万円｜—
- 5537 AlbaLink Co.,Ltd.｜kenmo_momentum/granville_oshime/granville_rebound｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜3,120円｜💰32.2万円｜—
- 4771 F&M Co., Ltd.｜kenmo_momentum/kenmo_newhigh｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜3,010円｜💰29.8万円｜—
- 5821 Hirakawa Hewtech Corp.｜kenmo_momentum｜⚡好調｜💎割安｜PASS｜3,320円｜💰33.2万円｜momentum 3330/SL3125.5（✅即時可）｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8） 📐進捗 上振れ 11.8%
  > 【業態】電線・放送機器メーカー。光中継システム等。医療用チューブも展開。海外でも生産。
  > 【いま】終値3,320円・直近5日+5.40%（材料未確認）
  > 【調子】⚡好調（7/13） — 上方修正済み
  > 【水準】💎割安（6.0/7）— PER12.59倍・PEG0.5507・52週31.6% ／ 💰単元33.2万円
  > 【戦略】当日高値超えの逆指値3330円で順張り参戦を検討。上限3363.3円・SL3125.5円目安
- 9560 PROGRIT, Inc.｜kenmo_momentum｜⚡好調｜🟢値頃｜FAIL_INSEN｜994円｜💰10.2万円｜—
- 558A SQUEEZE Inc.｜kenmo_momentum｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜5,770円｜💰57.6万円｜—
- 4058 Toyokumo, Inc.｜kenmo_momentum｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,212円｜💰22.1万円｜—
- 5034 unerry, Inc.｜kenmo_momentum｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,450円｜💰25.1万円｜—
- 6071 IBJ, Inc.｜kenmo_momentum/kenmo_newhigh｜⚡好調｜⚪妥当｜FAIL_INSEN｜990円｜💰10.2万円｜—
- 147A SORACOM,INC.｜kenmo_momentum｜⚡好調｜⚪妥当｜PASS｜940円｜💰9.4万円｜⛔提案なし(材料後出し)｜⚡材料後出し 📉決算反応日 11/12
  > 【業態】KDDI系。スマホSIMカードを基にしたIoTプラットフォーム「SORACOM」の開発・提供。
  > 【いま】終値940円・直近5日+4.10%・📊2027年３月期第２四半期（中間期）決算短信〔日本基準〕(連結)
  > 【調子】⚡好調（7/13） — E軸判定不能(進捗データ不足)
  > 【水準】⚪妥当（3.0/7）— PER61.04倍・PEG2.4218・52週17.9% ／ 💰単元9.4万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 7678 ASAKUMA CO.,LTD.｜kenmo_momentum/kenmo_newhigh｜⚡好調｜🔴過熱｜FAIL_INSEN｜4,275円｜💰43.7万円｜—
- 2975 Star Mica Holdings Co., Ltd.｜kenmo_momentum｜⚡好調｜💎割安｜FAIL_UWAHIGE｜1,220円｜💰11.8万円｜—
- 4477 BASE, Inc.｜kenmo_momentum/granville_oshime/granville_rebound｜⚡好調｜⚪妥当｜PASS｜310円｜💰3.1万円｜momentum 312/SL292.3（⏸位置不適(25MA下 -11.3%)）｜⚠日程不明 ⚠市場に劣後 RS20 -13.5pt
  > 【業態】個人・小規模企業向けECプラットフォーム「BASE」、オンライン決済サービス「PAY.JP」運営。
  > 【いま】終値310円・直近5日-4.02%（材料未確認）
  > 【調子】⚡好調（6/13） — ⚠減速
  > 【水準】⚪妥当（4.0/7）— PER23.85倍・PEG1.0183・52週34.1% ／ 💰単元3.1万円
  > 【戦略】当日高値超えの逆指値312円で順張り参戦を検討。上限315.1円・SL292.3円目安（⏸位置不適(25MA下 -11.3%)）
- 262A INTERMESTIC INC.｜kenmo_momentum｜⚡好調｜💎割安｜FAIL_UWAHIGE｜1,668円｜💰16.2万円｜—
- 505A Geekly,Inc.｜kenmo_momentum｜✅順調｜💎割安｜FAIL_INSEN｜1,140円｜💰11.3万円｜—
- 3798 ULS Group Incorporated｜kenmo_momentum/granville_tenkan｜✅順調｜💎割安｜FAIL_UWAHIGE｜482円｜💰4.9万円｜—
- 4743 ITFOR Inc.｜kenmo_momentum｜✅順調｜💎割安｜PASS｜1,582円｜💰15.8万円｜momentum 1585/SL1489（⏸位置不適(25MA下 -2.11%／52週 23.7%)）｜🚨決算直前 11/12(残1営業日) 📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】未取得（次回以降に取得）
  > 【いま】終値1,582円・直近5日+0.70%（材料未確認）
  > 【調子】✅順調（4/13） — E軸判定不能(進捗データ不足)
  > 【水準】💎割安（6.0/7）— PER12.31倍・PEG0.59・52週23.7% ／ 💰単元15.8万円
  > 【戦略】当日高値超えの逆指値1585円で順張り参戦を検討。上限1600.8円・SL1489円目安（⏸位置不適(25MA下 -2.11%／52週 23.7%)）
- 3077 Horiifoodservice Co., Ltd.｜kenmo_momentum/granville_rebound｜判定保留(変則決算)｜🟢値頃｜FAIL_INSEN｜1,185円｜💰11.9万円｜—
- 618A KOMPEITO Inc.｜kenmo_momentum/kenmo_newhigh｜取得不可｜🔴過熱｜PASS｜1,948円｜💰19.5万円｜momentum 1969/SL1849.9（✅即時可）｜⚠日程不明
  > 【業態】設置型の健康社食サービス「OFFICE DEYASAI」などの企画・運営を手掛ける。
  > 【いま】終値1,948円・直近5日+1.72%（材料未確認）
  > 【調子】取得不可（—/13） — 業績データ取得不可(前期比行なし)
  > 【水準】🔴過熱（1.8/7）— PER18.89倍・PEG—・52週65.4% ／ 💰単元19.5万円
  > 【戦略】当日高値超えの逆指値1969円で順張り参戦を検討。上限1988.7円・SL1849.9円目安
- 7567 Sakae Electronics Corp.｜kenmo_newhigh｜🚀確変｜⚪妥当｜FAIL_UWAHIGE｜609円｜💰6.0万円｜—
- 6418 Japan Cash Machine Co., Ltd.｜kenmo_newhigh/granville_oshime｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜1,465円｜💰12.4万円｜—
- 446A ノースサンド｜kenmo_newhigh/granville_oshime｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜2,404円｜💰25.0万円｜—
- 3696 セレス｜kenmo_newhigh｜🔥絶好調｜💎割安｜PASS｜2,081円｜💰20.8万円｜⛔提案なし(指名鮮度切れ 17営業日)｜⚡材料後出し 🚨決算直前 11/12(残1営業日) 📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】ポイントサイト「モッピー」などスマホ向けサイト運営。仮想通貨、ブロックチェーン、投資事業も。
  > 【いま】終値2,081円・直近5日-1.14%・📌ラボルがギークスのITフリーランス向け福利厚生プログラム「フリノベ」と提携開始～ITフリーランスの資金繰りをサポート～
  > 【調子】🔥絶好調（8/13）
  > 【水準】💎割安（6.0/7）— PER4倍・PEG0.0705・52週68.6% ／ 💰単元20.8万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 17営業日)）
- 2930 北の達人コーポレーション｜kenmo_newhigh｜⚡好調｜🔴過熱｜FAIL_INSEN｜147円｜💰1.5万円｜—
- 4379 Photosynth inc.｜kenmo_newhigh｜⚡好調｜🔴過熱｜FAIL_INSEN｜459円｜💰4.6万円｜—
- 3843 Freebit Co., Ltd.｜kenmo_newhigh/granville_tenkan｜✅順調｜🟡やや割高｜PASS｜1,982円｜💰19.8万円｜⛔提案なし(指名鮮度切れ 15営業日)｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】ネット接続にインフラ提供サービス。ドコモと提携、MVNOトーン運営。企業DX支援も展開。
  > 【いま】終値1,982円・直近5日+0.71%（材料未確認）
  > 【調子】✅順調（4/13）
  > 【水準】🟡やや割高（2.0/7）— PER9.61倍・PEG1.9221・52週83.4% ／ 💰単元19.8万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 15営業日)）
- 4933 I-ne CO., LTD.｜kenmo_newhigh｜🔻悪化｜⚪妥当｜FAIL_INSEN｜2,478円｜💰25.1万円｜—｜⚡材料後出し
- 9204 Skymark Airlines Inc.｜kenmo_newhigh｜🔻悪化｜🔴過熱｜PASS｜474円｜💰4.7万円｜momentum 477/SL447.4（✅即時可）｜⚠日程不明 ⚠業績基調が下向き（🔻悪化）
  > 【業態】国内第3位の航空会社。割安運賃で旅客の輸送サービスを手掛ける。
  > 【いま】終値474円・直近5日+5.80%（材料未確認）
  > 【調子】🔻悪化（3/13） — 進捗モデル値域外
  > 【水準】🔴過熱（0.0/7）— PER35.64倍・PEG—・52週98.7% ／ 💰単元4.7万円
  > 【戦略】当日高値超えの逆指値477円で順張り参戦を検討。上限481.8円・SL447.4円目安
- 1960 サンテック｜kenmo_newhigh｜➖横ばい｜🔴過熱｜FAIL_UWAHIGE｜1,846円｜💰16.5万円｜—
- 4565 Nxera Pharma Co., Ltd.｜kenmo_newhigh/granville_oshime｜業績データ取得不可(経常益予想非開示)｜🟡やや割高｜FAIL_UWAHIGE｜1,811円｜💰18.0万円｜—
- 5711 三菱マテリアル｜choruko_reversal｜🚀確変｜💎割安｜PASS｜4,132円｜💰41.3万円｜⛔提案なし(材料後出し)｜⚡材料後出し 📉決算反応日 11/12
  > 【業態】総合材料メーカー。加工、電子材、超硬工具、鉱山が柱。伸銅品首位。セメント分離。
  > 【いま】終値4,132円・直近5日-1.45%・📊2027年3月期第２四半期（中間期）決算短信［日本基準］（連結）
  > 【調子】🚀確変（12/13）
  > 【水準】💎割安（7.0/7）— PER3.86倍・PEG0.0457・52週37.6% ／ 💰単元41.3万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 3036 アルコニックス｜choruko_reversal｜🚀確変｜🟢値頃｜FAIL_UWAHIGE｜3,270円｜💰32.6万円｜—
- 6278 ユニオンツール｜choruko_reversal｜🚀確変｜🟢値頃｜PASS｜11,770円｜💰117.7万円｜⛔提案なし(材料後出し)｜⚡材料後出し 📉決算反応日 11/12
  > 【業態】プリント配線板用ドリル世界最大手。直動軸受け、測定器や生体センサも展開。
  > 【いま】終値11,770円・直近5日-1.09%・📊2026年12月期 第３四半期決算短信［日本基準］(連結)
  > 【調子】🚀確変（12/13）
  > 【水準】🟢値頃（5.0/7）— PER18.64倍・PEG0.1637・52週22.7% ／ 💰単元117.7万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 7995 Valqua Ltd.｜choruko_reversal/granville_rebound｜🚀確変｜🟢値頃｜PASS｜6,260円｜💰62.6万円｜reversal 6260/SL5130（✅即時可）｜⚠日程不明 ⚠1単元でリスク枠超過（113000円）
  > 【業態】工業用液漏れシール最大手。ゴム・金属・ファイバー製など製品多。先端産業向け力。
  > 【いま】終値6,260円・直近5日+4.51%（材料未確認）
  > 【調子】🚀確変（11/13） — 上方修正済み
  > 【水準】🟢値頃（5.0/7）— PER11.04倍・PEG0.1437・52週51.4% ／ 💰単元62.6万円
  > 【戦略】当日終値6260円の指値で反転を取りにいく。SL5130円（直近5日安値）／⚠1単元リスク113000円（枠超過）
- 6516 Sanyo Denki Co., Ltd.｜choruko_reversal/ai_reversal｜🔥絶好調｜💎割安｜PASS｜4,615円｜💰46.1万円｜reversal 4615/SL3945（✅即時可）｜⚠日程不明 ⚠1単元でリスク枠超過（67000円）
  > 【業態】通信機器用冷却ファン、電源、工作機械向けなど小型・精密サーボモーターが主軸。
  > 【いま】終値4,615円・直近5日-1.70%（材料未確認）
  > 【調子】🔥絶好調（10/13）
  > 【水準】💎割安（6.0/7）— PER13.67倍・PEG0.3248・52週23% ／ 💰単元46.1万円
  > 【戦略】当日終値4615円の指値で反転を取りにいく。SL3945円（直近5日安値）／⚠1単元リスク67000円（枠超過）
- 8336 武蔵野銀行｜choruko_reversal/granville_oshime/granville_rebound｜🔥絶好調｜💎割安｜PASS｜2,555円｜💰25.6万円｜reversal 2555/SL2200（✅即時可）｜⚠日程不明 ⚠1単元でリスク枠超過（35500円）
  > 【業態】埼玉地盤で全域に店舗網。地域密着型営業展開。千葉銀と提携。
  > 【いま】終値2,555円・直近5日+2.24%（材料未確認）
  > 【調子】🔥絶好調（10/13）
  > 【水準】💎割安（6.0/7）— PER11.92倍・PEG0.2894・52週70.7% ／ 💰単元25.6万円
  > 【戦略】当日終値2555円の指値で反転を取りにいく。SL2200円（直近5日安値）／⚠1単元リスク35500円（枠超過）
- 5344 MARUWA CO., LTD.｜choruko_reversal｜🔥絶好調｜🟢値頃｜PASS｜45,860円｜💰458.6万円｜⛔提案なし(指名鮮度切れ 13営業日)｜⚠日程不明
  > 【業態】ガラス・土石（セラミックス・電子部品・携帯電話部材・部品関連）
  > 【いま】終値45,860円・直近5日-4.14%（材料未確認）
  > 【調子】🔥絶好調（10/13） — E軸:進捗46.1%>=前年同期42.3%
  > 【水準】🟢値頃（5.0/7）— PER21.77倍・PEG0.4783・52週18.2% ／ 💰単元458.6万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 13営業日)）
- 6645 OMRON Corporation｜choruko_reversal/granville_rebound｜🔥絶好調｜🟢値頃｜PASS｜4,936円｜💰49.4万円｜⛔提案なし(指名鮮度切れ 13営業日)｜⚠日程不明 📐進捗 上振れ 68.9%
  > 【業態】制御機器大手。感知・リレー制御技術が得意。車載、鉄道システム、ヘルスケアも展開。
  > 【いま】終値4,936円・直近5日-4.66%（材料未確認）
  > 【調子】🔥絶好調（10/13） — 税引前代替
  > 【水準】🟢値頃（5.0/7）— PER22.57倍・PEG0.3603・52週35% ／ 💰単元49.4万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 13営業日)）
- 8871 GOLDCREST Co., Ltd.｜choruko_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜2,435円｜💰24.2万円｜—
- 4216 ASAHI YUKIZAI CORPORATION｜choruko_reversal｜🔥絶好調｜💎割安｜PASS｜5,720円｜💰57.2万円｜reversal 5720/SL5160（✅即時可）｜⚠日程不明 📐進捗 遅れ -15.1% ⚠1単元でリスク枠超過（56000円）
  > 【業態】旭化成系で樹脂バルブの独占的メーカー。水資源開発も。中国・アジア市場を開拓。
  > 【いま】終値5,720円・直近5日-5.77%（材料未確認）
  > 【調子】🔥絶好調（9/13） — 上方修正済み
  > 【水準】💎割安（6.0/7）— PER13.11倍・PEG0.2402・52週38.7% ／ 💰単元57.2万円
  > 【戦略】当日終値5720円の指値で反転を取りにいく。SL5160円（直近5日安値）／⚠1単元リスク56000円（枠超過）
- 4471 三洋化成工業｜choruko_reversal/granville_oshime/granville_rebound｜🔥絶好調｜💎割安｜PASS｜1,510円｜💰15.1万円｜reversal 1510/SL1408（✅即時可）｜⚠日程不明 📐進捗 上振れ 38.0%
  > 【業態】界面制御技術が主軸。車関連、電池、メディカル注力。高吸水性樹脂事業は撤退。
  > 【いま】終値1,510円・直近5日-3.88%（材料未確認）
  > 【調子】🔥絶好調（9/13） — 上方修正済み
  > 【水準】💎割安（6.0/7）— PER10.61倍・PEG0.248・52週62% ／ 💰単元15.1万円
  > 【戦略】当日終値1510円の指値で反転を取りにいく。SL1408円（直近5日安値）
- 5703 日本軽金属ホールディングス（日軽金ＨＤ）｜choruko_reversal｜🔥絶好調｜💎割安｜PASS｜2,567円｜💰25.7万円｜reversal 2567/SL2338（✅即時可）｜⚠日程不明
  > 【業態】アルミ総合メーカー。アルミ製品と化成品が主力。アジア急展開。国内精錬工場を閉鎖。
  > 【いま】終値2,567円・直近5日-0.73%（材料未確認）
  > 【調子】🔥絶好調（9/13）
  > 【水準】💎割安（6.0/7）— PER9.3倍・PEG0.2991・52週31.6% ／ 💰単元25.7万円
  > 【戦略】当日終値2567円の指値で反転を取りにいく。SL2338円（直近5日安値）
- 7433 Hakuto Co., Ltd.｜choruko_reversal/ai_reversal/granville_oshime/granville_rebound｜🔥絶好調｜💎割安｜PASS｜1,615円｜💰16.1万円｜reversal 1615/SL1516（✅即時可）｜🚨決算直前 11/12(残1営業日)
  > 【業態】エレクトロニクス商社。半導体製造装置に強み。工業薬品製造も併営。海外開拓。
  > 【いま】終値1,615円・直近5日-2.30%（材料未確認）
  > 【調子】🔥絶好調（9/13） — E軸判定不能(進捗データ不足)
  > 【水準】💎割安（6.0/7）— PER4.75倍・PEG0.0877・52週53.7% ／ 💰単元16.1万円
  > 【戦略】当日終値1615円の指値で反転を取りにいく。SL1516円（直近5日安値）
- 8084 ＲＹＯＤＥＮ｜choruko_reversal/granville_rebound｜🔥絶好調｜💎割安｜PASS｜2,229円｜💰22.3万円｜reversal 2229/SL2025（✅即時可）｜⚠日程不明
  > 【業態】三菱電機系最大商社。半導体、冷熱住機、ビル昇降機など他社も幅広く展開。
  > 【いま】終値2,229円・直近5日+3.39%（材料未確認）
  > 【調子】🔥絶好調（9/13）
  > 【水準】💎割安（6.0/7）— PER8倍・PEG0.2661・52週65.7% ／ 💰単元22.3万円
  > 【戦略】当日終値2229円の指値で反転を取りにいく。SL2025円（直近5日安値）
- 5301 Tokai Carbon Co., Ltd.｜choruko_reversal/granville_rebound｜🔥絶好調｜🟢値頃｜PASS｜1,666円｜💰16.7万円｜reversal 1665.5/SL1450.5（✅即時可）｜⚠日程不明
  > 【業態】ガラス・土石
  > 【いま】終値1,666円・直近5日-8.64%（材料未確認）
  > 【調子】🔥絶好調（9/13） — 🔼加速
  > 【水準】🟢値頃（5.0/7）— PER15.49倍・PEG0.5103・52週51% ／ 💰単元16.7万円
  > 【戦略】当日終値1665.5円の指値で反転を取りにいく。SL1450.5円（直近5日安値）
- 6268 ナブテスコ｜choruko_reversal｜🔥絶好調｜🟢値頃｜PASS｜4,235円｜💰42.4万円｜reversal 4235/SL3622（✅即時可）｜⏰決算 11/13(残2営業日) ⚠1単元でリスク枠超過（61300円）
  > 【業態】産業ロボット用精密減速機は世界6割。自動ドアで世界トップ級。鉄道ブレーキも。
  > 【いま】終値4,235円・直近5日+1.63%（材料未確認）
  > 【調子】🔥絶好調（9/13） — E軸:進捗47.8%>=例年42.6%
  > 【水準】🟢値頃（5.0/7）— PER20.41倍・PEG0.3134・52週35.6% ／ 💰単元42.4万円
  > 【戦略】当日終値4235円の指値で反転を取りにいく。SL3622円（直近5日安値）／⚠1単元リスク61300円（枠超過）
- 6324 Harmonic Drive Systems Inc.｜choruko_reversal｜🔥絶好調｜🟢値頃｜PASS｜4,993円｜💰49.9万円｜⛔提案なし(指名鮮度切れ 14営業日)｜⚡材料後出し 📉決算反応日 11/12
  > 【業態】精密制御減速装置が軸。小型・軽量強み。産業用ロボット向け等。メカトロ製品も。
  > 【いま】終値4,993円・直近5日+1.26%・📊2027年３月期第２四半期（中間期）決算短信〔日本基準〕(連結)
  > 【調子】🔥絶好調（9/13） — E軸判定不能(進捗データ不足)
  > 【水準】🟢値頃（5.0/7）— PER78.75倍・PEG0.3532・52週38.2% ／ 💰単元49.9万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 14営業日)）
- 6481 THK Co., Ltd.｜choruko_reversal｜🔥絶好調｜🟢値頃｜PASS｜5,579円｜💰55.8万円｜reversal 5579/SL4707（✅即時可）｜⏰決算 11/13(残2営業日) ⚠1単元でリスク枠超過（87200円）
  > 【業態】機械（軸受け・機械・部品・FA関連関連）
  > 【いま】終値5,579円・直近5日-0.76%（材料未確認）
  > 【調子】🔥絶好調（9/13）
  > 【水準】🟢値頃（5.0/7）— PER11.41倍・PEG0.0573・52週40.6% ／ 💰単元55.8万円
  > 【戦略】当日終値5579円の指値で反転を取りにいく。SL4707円（直近5日安値）／⚠1単元リスク87200円（枠超過）
- 6652 IDEC Corporation｜choruko_reversal｜🔥絶好調｜🟢値頃｜PASS｜3,155円｜💰31.6万円｜reversal 3155/SL2905（✅即時可）｜⚠日程不明 📐進捗 上振れ 59.9%
  > 【業態】制御機器大手。スイッチや表示灯に強み。自動認識機器や防災・防爆関連強化。
  > 【いま】終値3,155円・直近5日-3.52%（材料未確認）
  > 【調子】🔥絶好調（9/13） — 上方修正済み
  > 【水準】🟢値頃（5.0/7）— PER10.89倍・PEG0.3004・52週40.2% ／ 💰単元31.6万円
  > 【戦略】当日終値3155円の指値で反転を取りにいく。SL2905円（直近5日安値）
- 6724 セイコーエプソン｜choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜2,858円｜💰26.6万円｜—
- 6925 Ushio Inc.｜choruko_reversal｜🔥絶好調｜🟢値頃｜PASS｜3,228円｜💰32.3万円｜⛔提案なし(指名鮮度切れ 13営業日)｜⚠日程不明 📐進捗 上振れ 32.7%
  > 【業態】産業用ランプで世界首位。光源や光学装置を展開。医療装置分野も強化。
  > 【いま】終値3,228円・直近5日+2.31%（材料未確認）
  > 【調子】🔥絶好調（9/13） — 上方修正済み
  > 【水準】🟢値頃（5.0/7）— PER21.35倍・PEG0.6122・52週32.6% ／ 💰単元32.3万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 13営業日)）
- 3222 United Super Markets Holdings, Inc.｜choruko_reversal｜🔥絶好調｜🔴過熱｜FAIL_INSEN｜777円｜💰7.8万円｜—
- 6875 メガチップス｜choruko_reversal｜🔥絶好調｜💎割安｜PASS｜8,720円｜💰87.2万円｜reversal 8720/SL7880（✅即時可）｜⚠日程不明 📐進捗 遅れ -48.4% ⚠1単元でリスク枠超過（84000円）
  > 【業態】カスタムLSI、画像転送システムが主力。生産外部委託。任天堂向け中心。5G向けも。
  > 【いま】終値8,720円・直近5日-5.93%（材料未確認）
  > 【調子】🔥絶好調（8/13） — 突出ボーナス
  > 【水準】💎割安（7.0/7）— PER3.51倍・PEG0・52週23.8% ／ 💰単元87.2万円
  > 【戦略】当日終値8720円の指値で反転を取りにいく。SL7880円（直近5日安値）／⚠1単元リスク84000円（枠超過）
- 6471 日本精工｜choruko_reversal｜🔥絶好調｜💎割安｜PASS｜1,011円｜💰10.1万円｜reversal 1011/SL913（✅即時可）｜⚠日程不明
  > 【業態】ベアリング最大手。電動パワステ等自動車軸受、産機用展開。27年NTNと統合へ。
  > 【いま】終値1,011円・直近5日+2.43%（材料未確認）
  > 【調子】🔥絶好調（8/13） — 税引前代替
  > 【水準】💎割安（6.0/7）— PER14.57倍・PEG0.3584・52週26.1% ／ 💰単元10.1万円
  > 【戦略】当日終値1011円の指値で反転を取りにいく。SL913円（直近5日安値）
- 8386 百十四銀行｜choruko_reversal/granville_rebound｜🔥絶好調｜💎割安｜PASS｜2,847円｜💰28.5万円｜reversal 2847/SL2390（✅即時可）｜⚠日程不明 ⚠1単元でリスク枠超過（45700円）
  > 【業態】香川地盤の地銀で県内首位。大阪や岡山などに展開。大企業取引が多い。
  > 【いま】終値2,847円・直近5日+4.59%（材料未確認）
  > 【調子】🔥絶好調（8/13）
  > 【水準】💎割安（6.0/7）— PER12.89倍・PEG0.3806・52週74.5% ／ 💰単元28.5万円
  > 【戦略】当日終値2847円の指値で反転を取りにいく。SL2390円（直近5日安値）／⚠1単元リスク45700円（枠超過）
- 6588 東芝テック｜choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜2,692円｜💰27.1万円｜—｜⚡材料後出し
- 6754 アンリツ｜choruko_reversal/ai_reversal｜🔥絶好調｜🟢値頃｜PASS｜2,435円｜💰24.4万円｜reversal 2435/SL2060（✅即時可）｜⚠日程不明 ⚠1単元でリスク枠超過（37500円）
  > 【業態】携帯・基地局向けなど計測機器大手。海外も高シェア。食品・医薬品検査機も。
  > 【いま】終値2,435円・直近5日-4.92%（材料未確認）
  > 【調子】🔥絶好調（8/13） — 税引前代替
  > 【水準】🟢値頃（5.0/7）— PER19.48倍・PEG0.5374・52週13.4% ／ 💰単元24.4万円
  > 【戦略】当日終値2435円の指値で反転を取りにいく。SL2060円（直近5日安値）／⚠1単元リスク37500円（枠超過）
- 7731 ニコン｜choruko_reversal｜🔥絶好調｜🟢値頃｜PASS｜1,648円｜💰16.5万円｜reversal 1648/SL1497（✅即時可）｜⚠日程不明
  > 【業態】カメラ・回路露光装置の両輪。一眼レフでキヤノンと双璧。ヘルスケア、エネルギー関連強化。
  > 【いま】終値1,648円・直近5日+3.16%（材料未確認）
  > 【調子】🔥絶好調（8/13） — 黒字転換
  > 【水準】🟢値頃（5.0/7）— PER33.91倍・PEG0.2821・52週16.9% ／ 💰単元16.5万円
  > 【戦略】当日終値1648円の指値で反転を取りにいく。SL1497円（直近5日安値）
- 9902 Nichiden Corporation｜choruko_reversal/granville_oshime｜🔥絶好調｜🟢値頃｜PASS｜2,957円｜💰29.6万円｜reversal 2957/SL2766（✅即時可）｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8） 📐進捗 上振れ 21.3%
  > 【業態】産業機器・部品商社。動力伝導機器や軸受け主力でシェア首位級。アジア強化。
  > 【いま】終値2,957円・直近5日-2.89%（材料未確認）
  > 【調子】🔥絶好調（8/13） — 🔼加速
  > 【水準】🟢値頃（5.0/7）— PER12.41倍・PEG0.5339・52週63.5% ／ 💰単元29.6万円
  > 【戦略】当日終値2957円の指値で反転を取りにいく。SL2766円（直近5日安値）
- 7733 Olympus Corp.｜choruko_reversal｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜1,752円｜💰17.7万円｜—
- 5019 出光興産｜choruko_reversal｜⚠減速｜⚪妥当｜PASS｜1,318円｜💰13.2万円｜⛔提案なし(材料後出し)｜⚡材料後出し 📉決算反応日 11/12 ⚠業績基調が下向き（⚠減速）
  > 【業態】石油精製元売り大手。石油化学に強み。豪州石炭権益も。昭和シェルと統合。
  > 【いま】終値1,318円・直近5日-7.80%・📊2027年３月期 第2四半期（中間期）決算短信〔ＩＦＲＳ会計基準〕（連結）
  > 【調子】⚠減速（8/13） — 4Q換算（変則決算）
  > 【水準】⚪妥当（3.5/7）— PER21.06倍・PEG—・52週36.6% ／ 💰単元13.2万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 4088 Air Water Inc.｜choruko_reversal｜🔥絶好調｜⚪妥当｜PASS｜2,897円｜💰29.0万円｜⛔提案なし(指名鮮度切れ 13営業日)｜⚠日程不明
  > 【業態】工業用ガス大手。医療用酸素で首位。鉄鋼、半導体向けに強み。M&Aで拡大。
  > 【いま】終値2,897円・直近5日+2.01%（材料未確認）
  > 【調子】🔥絶好調（8/13） — 赤字→黒字転換
  > 【水準】⚪妥当（3.0/7）— PER23.73倍・PEG0.1279・52週78.8% ／ 💰単元29.0万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 13営業日)）
- 8133 伊藤忠エネクス｜choruko_reversal｜🔥絶好調｜🟡やや割高｜PASS｜2,029円｜💰20.3万円｜reversal 2029/SL1966（✅即時可）｜⚠日程不明 📐進捗 上振れ 83.7%
  > 【業態】伊藤忠系の燃料商社最大手。産業用燃料やLPGなど。カーライフ部門が拡大。
  > 【いま】終値2,029円・直近5日-3.38%（材料未確認）
  > 【調子】🔥絶好調（8/13） — 4Q換算（変則決算）
  > 【水準】🟡やや割高（2.0/7）— PER13.89倍・PEG7.4493・52週42.2% ／ 💰単元20.3万円
  > 【戦略】当日終値2029円の指値で反転を取りにいく。SL1966円（直近5日安値）
- 5333 ＮＧＫ｜choruko_reversal/ai_reversal｜⚡好調｜💎割安｜PASS｜4,834円｜💰48.3万円｜reversal 4834/SL4206（✅即時可）｜⚠日程不明 📐進捗 上振れ 14.0% ⚠1単元でリスク枠超過（62800円）
  > 【業態】ガラス・土石（電力設備投資関連・自動車部材・部品・セラミックス関連）
  > 【いま】終値4,834円・直近5日-3.26%（材料未確認）
  > 【調子】⚡好調（7/13） — 上方修正済み
  > 【水準】💎割安（6.0/7）— PER13.61倍・PEG0.4208・52週38.7% ／ 💰単元48.3万円
  > 【戦略】当日終値4834円の指値で反転を取りにいく。SL4206円（直近5日安値）／⚠1単元リスク62800円（枠超過）
- 7721 Tokyo Keiki Inc.｜choruko_reversal｜⚡好調｜💎割安｜PASS｜5,430円｜💰54.3万円｜⛔提案なし(指名鮮度切れ 17営業日)｜⚠日程不明
  > 【業態】精密機器（計測機器・通信機器・航空機関連）
  > 【いま】終値5,430円・直近5日-0.37%（材料未確認）
  > 【調子】⚡好調（7/13） — 進捗モデル値域外
  > 【水準】💎割安（6.0/7）— PER15.91倍・PEG0.4728・52週17.1% ／ 💰単元54.3万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 17営業日)）
- 8154 加賀電子｜choruko_reversal/granville_rebound｜⚡好調｜💎割安｜FAIL_UWAHIGE｜5,150円｜💰47.2万円｜—
- 3433 TOCALO Co., Ltd.｜choruko_reversal/ai_reversal/granville_tenkan｜⚡好調｜🟢値頃｜PASS｜2,601円｜💰26.0万円｜reversal 2601/SL2123（✅即時可）｜⚠日程不明 ⚠1単元でリスク枠超過（47800円）
  > 【業態】金属製品（表面処理加工・半導体製造装置・液晶製造装置関連）
  > 【いま】終値2,601円・直近5日+1.52%（材料未確認）
  > 【調子】⚡好調（7/13） — 上方修正済み
  > 【水準】🟢値頃（5.0/7）— PER13.22倍・PEG0.6382・52週40.3% ／ 💰単元26.0万円
  > 【戦略】当日終値2601円の指値で反転を取りにいく。SL2123円（直近5日安値）／⚠1単元リスク47800円（枠超過）
- 5186 ニッタ｜choruko_reversal｜⚡好調｜🟢値頃｜PASS｜6,430円｜💰64.3万円｜reversal 6430/SL5770（✅即時可）｜⚠日程不明 📐進捗 上振れ 21.2% ⚠1単元でリスク枠超過（66000円）
  > 【業態】伝動用ベルト大手。産業機械向け主力。自動車ホース、半導体関連なども強み。
  > 【いま】終値6,430円・直近5日-2.58%（材料未確認）
  > 【調子】⚡好調（7/13） — 上方修正済み
  > 【水準】🟢値頃（5.0/7）— PER11.78倍・PEG0.5468・52週73.2% ／ 💰単元64.3万円
  > 【戦略】当日終値6430円の指値で反転を取りにいく。SL5770円（直近5日安値）／⚠1単元リスク66000円（枠超過）
- 8393 Miyazaki Bank Ltd.｜choruko_reversal｜⚡好調｜🟢値頃｜PASS｜2,541円｜💰25.4万円｜⛔提案なし(指名鮮度切れ 14営業日)｜⚠日程不明
  > 【業態】宮崎地盤の地銀中位。県指定金融機関。農業、医療、介護向け融資攻勢。
  > 【いま】終値2,541円・直近5日+8.73%（材料未確認）
  > 【調子】⚡好調（7/13）
  > 【水準】🟢値頃（5.0/7）— PER12.54倍・PEG0.5327・52週75.3% ／ 💰単元25.4万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 14営業日)）
- 8522 Bank of Nagoya, Ltd.｜choruko_reversal/granville_rebound｜⚡好調｜🟢値頃｜PASS｜5,860円｜💰58.6万円｜reversal 5860/SL5250（✅即時可）｜⏰決算 11/13(残2営業日) ⚠1単元でリスク枠超過（61000円）
  > 【業態】愛知県内首位で地銀中位。地域密着営業。28年4月しずおかFGと統合予定。
  > 【いま】終値5,860円・直近5日+0.00%（材料未確認）
  > 【調子】⚡好調（7/13）
  > 【水準】🟢値頃（5.0/7）— PER12.54倍・PEG0.6266・52週54.5% ／ 💰単元58.6万円
  > 【戦略】当日終値5860円の指値で反転を取りにいく。SL5250円（直近5日安値）／⚠1単元リスク61000円（枠超過）
- 167A リョーサン菱洋ホールディングス（リョー菱ＨＤ）｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜3,095円｜💰30.6万円｜—
- 6302 住友重機械工業｜choruko_reversal/granville_tenkan｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜5,240円｜💰52.1万円｜—
- 6448 ブラザー工業（ブラザー）｜choruko_reversal｜⚡好調｜⚪妥当｜PASS｜4,603円｜💰46.0万円｜reversal 4603/SL4078（✅即時可）｜⚠日程不明 📐進捗 上振れ 47.8% ⚠1単元でリスク枠超過（52500円）
  > 【業態】ミシンからプリンター、デジタル複合機が主力に。産業機も。中国生産で欧米へ輸出。
  > 【いま】終値4,603円・直近5日+5.60%（材料未確認）
  > 【調子】⚡好調（7/13） — 税引前代替
  > 【水準】⚪妥当（4.0/7）— PER12.86倍・PEG0.3761・52週79.7% ／ 💰単元46.0万円
  > 【戦略】当日終値4603円の指値で反転を取りにいく。SL4078円（直近5日安値）／⚠1単元リスク52500円（枠超過）
- 3116 Toyota Boshoku Corp.｜choruko_reversal｜⚡好調｜💎割安｜FAIL_INSEN｜2,046円｜💰20.6万円｜—
- 5331 ノリタケ｜choruko_reversal/ai_reversal｜⚡好調｜💎割安｜PASS｜3,050円｜💰30.5万円｜reversal 3050/SL2683（✅即時可）｜⚠日程不明 📐進捗 上振れ 17.3% ⚠1単元でリスク枠超過（36700円）
  > 【業態】森村グループ中核で高級陶磁器、砥石最大手。セラミック材、エンジニアリングが主軸。
  > 【いま】終値3,050円・直近5日-4.24%（材料未確認）
  > 【調子】⚡好調（6/13） — 上方修正済み
  > 【水準】💎割安（7.0/7）— PER9.32倍・PEG0.5049・52週27.4% ／ 💰単元30.5万円
  > 【戦略】当日終値3050円の指値で反転を取りにいく。SL2683円（直近5日安値）／⚠1単元リスク36700円（枠超過）
- 7004 カナデビア｜choruko_reversal｜⚠減速｜💎割安｜PASS｜968円｜💰9.7万円｜reversal 968/SL828（✅即時可）｜⚠日程不明 ⚠業績基調が下向き（⚠減速） ⚠バリュートラップ疑い
  > 【業態】ゴミ焼却発電設備が主柱。淡水化プラント、橋梁、掘進機など。持分で内海造船。
  > 【いま】終値968円・直近5日-4.91%（材料未確認）
  > 【調子】⚠減速（6/13） — A成長率0以下のためレバレッジ計算不可(C=0)
  > 【水準】💎割安（7.0/7）— PER7.76倍・PEG0.1261・52週20.4% ／ 💰単元9.7万円
  > 【戦略】当日終値968円の指値で反転を取りにいく。SL828円（直近5日安値）
- 6651 NITTO KOGYO Corporation｜choruko_reversal｜⚡好調｜💎割安｜FAIL_UWAHIGE｜4,190円｜💰41.7万円｜—
- 4205 Zeon Corporation｜choruko_reversal｜⚡好調｜🟢値頃｜PASS｜2,102円｜💰21.0万円｜reversal 2101.5/SL1881（✅即時可）｜⚠日程不明 📐進捗 上振れ 39.7%
  > 【業態】古河系。合成ゴム大手。耐油性特殊ゴムで世界的。合成ラテックス、高機能材も。
  > 【いま】終値2,102円・直近5日+1.33%（材料未確認）
  > 【調子】⚡好調（6/13） — 上方修正済み
  > 【水準】🟢値頃（5.0/7）— PER9.36倍・PEG0.58・52週47% ／ 💰単元21.0万円
  > 【戦略】当日終値2101.5円の指値で反転を取りにいく。SL1881円（直近5日安値）
- 5101 Yokohama Rubber Co., Ltd.｜choruko_reversal｜⚡好調｜🟢値頃｜FAIL_INSEN｜7,090円｜💰71.7万円｜—
- 5463 丸一鋼管（丸一管）｜choruko_reversal｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜1,638円｜💰16.2万円｜—
- 8098 稲畑産業｜choruko_reversal/ai_reversal/granville_oshime｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜4,260円｜💰42.0万円｜—
- 6473 ジェイテクト｜choruko_reversal｜⚠減速｜⚪妥当｜PASS｜2,082円｜💰20.8万円｜reversal 2081.5/SL1842（✅即時可）｜⚠日程不明 ⚠業績基調が下向き（⚠減速）
  > 【業態】ベアリング大手、光洋精工と豊田工機が合併。ステアリング、工作機械にも強み。
  > 【いま】終値2,082円・直近5日+6.42%（材料未確認）
  > 【調子】⚠減速（6/13） — 税引前代替
  > 【水準】⚪妥当（4.0/7）— PER13.26倍・PEG0.0852・52週75% ／ 💰単元20.8万円
  > 【戦略】当日終値2081.5円の指値で反転を取りにいく。SL1842円（直近5日安値）
- 9412 SKY Perfect JSAT Corporation｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜1,812円｜💰18.2万円｜—
- 3569 セーレン｜choruko_reversal/granville_tenkan｜⚡好調｜⚪妥当｜PASS｜3,515円｜💰35.1万円｜reversal 3515/SL3100（✅即時可）｜⚠日程不明 ⚠1単元でリスク枠超過（41500円）
  > 【業態】総合繊維会社。染色技術に強み。車用シート・エアバッグ材が主力。化粧品育成。
  > 【いま】終値3,515円・直近5日+8.82%（材料未確認）
  > 【調子】⚡好調（6/13） — 上方修正済み
  > 【水準】⚪妥当（3.0/7）— PER11.65倍・PEG0.8557・52週78.3% ／ 💰単元35.1万円
  > 【戦略】当日終値3515円の指値で反転を取りにいく。SL3100円（直近5日安値）／⚠1単元リスク41500円（枠超過）
- 4634 ａｒｔｉｅｎｃｅ（ａｒｔｉｅｎ）｜choruko_reversal｜⚡好調｜⚪妥当｜PASS｜4,875円｜💰48.8万円｜reversal 4875/SL4475（✅即時可）｜⏰決算 11/13(残2営業日) 📐進捗 上振れ 34.0% ⚠1単元でリスク枠超過（40000円）
  > 【業態】凸版印刷系で印刷インキの国内最大手。液晶パネル用顔料、フィルム、樹脂が柱。
  > 【いま】終値4,875円・直近5日+1.14%（材料未確認）
  > 【調子】⚡好調（6/13） — 🔼加速
  > 【水準】⚪妥当（3.0/7）— PER10.89倍・PEG1.4107・52週83.2% ／ 💰単元48.8万円
  > 【戦略】当日終値4875円の指値で反転を取りにいく。SL4475円（直近5日安値）／⚠1単元リスク40000円（枠超過）
- 6845 アズビル｜choruko_reversal｜⚡好調｜🟡やや割高｜FAIL_UWAHIGE｜1,518円｜💰14.3万円｜—｜⚡材料後出し
- 5444 大和工業｜choruko_reversal｜⚡好調｜💎割安｜PASS｜10,950円｜💰109.5万円｜reversal 10950/SL9989（✅即時可）｜⚠日程不明 ⚠1単元でリスク枠超過（96100円）
  > 【業態】独立系電炉大手。主力はH形鋼、溝形鋼。海外多、韓・タイ・米・中東で操業。
  > 【いま】終値10,950円・直近5日-6.57%（材料未確認）
  > 【調子】⚡好調（5/13）
  > 【水準】💎割安（6.0/7）— PER11.38倍・PEG0.3411・52週31.4% ／ 💰単元109.5万円
  > 【戦略】当日終値10950円の指値で反転を取りにいく。SL9989円（直近5日安値）／⚠1単元リスク96100円（枠超過）
- 8714 池田泉州ホールディングス｜choruko_reversal/granville_oshime｜⚡好調｜🟢値頃｜PASS｜863円｜💰8.6万円｜reversal 863/SL773（✅即時可）｜⏰決算 11/13(残2営業日)
  > 【業態】池田銀と泉州銀が経営統合。関西地銀、大阪府内最大。地域主義推進。
  > 【いま】終値863円・直近5日-1.03%（材料未確認）
  > 【調子】⚡好調（5/13）
  > 【水準】🟢値頃（5.6/7）— PER12.58倍・PEG0.9716・52週35.8% ／ 💰単元8.6万円
  > 【戦略】当日終値863円の指値で反転を取りにいく。SL773円（直近5日安値）
- 6284 日精エー・エス・ビー機械｜choruko_reversal/changepoint｜⚡好調｜🟢値頃｜PASS｜7,970円｜💰79.7万円｜⛔提案なし(材料後出し)｜⚡材料後出し 📉決算反応日 11/12
  > 【業態】PETボトルなど非飲料容器成形機の世界大手。海外比率が9割。汎用機拡大。
  > 【いま】終値7,970円・直近5日+2.57%・📊2026年9月期　決算短信〔日本基準〕（連結）
  > 【調子】⚡好調（5/13）
  > 【水準】🟢値頃（5.0/7）— PER13.13倍・PEG0.6548・52週46.4% ／ 💰単元79.7万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 8399 琉球銀行｜choruko_reversal/granville_rebound｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜2,700円｜💰26.3万円｜—
- 9934 因幡電機産業｜choruko_reversal｜⚡好調｜⚪妥当｜PASS｜2,662円｜💰26.6万円｜reversal 2661.5/SL2513.5（✅即時可）｜⚠日程不明
  > 【業態】卸売業
  > 【いま】終値2,662円・直近5日-3.60%（材料未確認）
  > 【調子】⚡好調（5/13） — E軸判定不能(進捗データ不足)
  > 【水準】⚪妥当（4.0/7）— PER12.67倍・PEG1.5217・52週39.8% ／ 💰単元26.6万円
  > 【戦略】当日終値2661.5円の指値で反転を取りにいく。SL2513.5円（直近5日安値）
- 1721 コムシスホールディングス｜choruko_reversal｜⚡好調｜⚪妥当｜PASS｜5,177円｜💰51.8万円｜reversal 5177/SL4767（✅即時可）｜⚠日程不明 📐進捗 上振れ 14.9% ⚠1単元でリスク枠超過（41000円）
  > 【業態】電気通信工事で首位。日本コムシス中核、NTT向けが過半。携帯各社の工事も。
  > 【いま】終値5,177円・直近5日-3.76%（材料未確認）
  > 【調子】⚡好調（5/13） — 上方修正済み
  > 【水準】⚪妥当（3.0/7）— PER14.77倍・PEG1.5932・52週53.3% ／ 💰単元51.8万円
  > 【戦略】当日終値5177円の指値で反転を取りにいく。SL4767円（直近5日安値）／⚠1単元リスク41000円（枠超過）
- 268A Rigaku Holdings Corporation｜choruko_reversal｜⚡好調｜⚪妥当｜PASS｜1,385円｜💰13.8万円｜⛔提案なし(指名鮮度切れ 13営業日)｜⚡材料後出し 📉決算反応日 11/12
  > 【業態】X線分析技術・世界大手。X線技術を用いた理科学機器の製造・販売。(精密機器)
  > 【いま】終値1,385円・直近5日+1.54%・📊2026年12月期第３四半期決算短信〔ＩＦＲＳ〕(連結)
  > 【調子】⚡好調（5/13）
  > 【水準】⚪妥当（3.0/7）— PER25.09倍・PEG1.6497・52週19.8% ／ 💰単元13.8万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 13営業日)）
- 9072 NIKKON Holdings Co., Ltd.｜choruko_reversal｜⚡好調｜⚪妥当｜PASS｜4,254円｜💰42.5万円｜reversal 4254/SL4007（✅即時可）｜⚠日程不明 📐進捗 遅れ -10.5%
  > 【業態】陸運業
  > 【いま】終値4,254円・直近5日+1.07%（材料未確認）
  > 【調子】⚡好調（5/13） — ⚠進捗遅れ
  > 【水準】⚪妥当（3.0/7）— PER23.91倍・PEG2.2452・52週27.7% ／ 💰単元42.5万円
  > 【戦略】当日終値4254円の指値で反転を取りにいく。SL4007円（直近5日安値）
- 9960 トーテック｜choruko_reversal｜⚡好調｜⚪妥当｜PASS｜4,385円｜💰43.9万円｜reversal 4385/SL3745（✅即時可）｜⚠日程不明 📐進捗 上振れ 11.8% ℹ相対強い RS20 7.5pt ⚠1単元でリスク枠超過（64000円）
  > 【業態】空調機器・関連機器専門商社で首位。設計・施工・保守の工事部門を拡大。
  > 【いま】終値4,385円・直近5日+7.08%（材料未確認）
  > 【調子】⚡好調（5/13） — 上方修正済み
  > 【水準】⚪妥当（3.0/7）— PER12.49倍・PEG1.4809・52週86.1% ／ 💰単元43.9万円
  > 【戦略】当日終値4385円の指値で反転を取りにいく。SL3745円（直近5日安値）／⚠1単元リスク64000円（枠超過）
- 6454 マックス｜choruko_reversal｜⚡好調｜🟡やや割高｜FAIL_UWAHIGE｜1,792円｜💰17.0万円｜—
- 9302 三井倉庫ホールディングス｜choruko_reversal｜⚡好調｜🟡やや割高｜FAIL_INSEN｜3,189円｜💰32.1万円｜—
- 4666 Park24 Co., Ltd.｜choruko_reversal｜✅順調｜💎割安｜FAIL_UWAHIGE｜1,822円｜💰18.1万円｜—
- 6135 牧野フライス製作所｜choruko_reversal｜✅順調｜💎割安｜PASS｜2,812円｜💰28.1万円｜reversal 2812/SL2450（✅即時可）｜⚠日程不明 ⚠1単元でリスク枠超過（36200円）
  > 【業態】工作機械大手。マシニングセンタ、放電加工機が主力。レーザ加工機にも注力。
  > 【いま】終値2,812円・直近5日-1.16%（材料未確認）
  > 【調子】✅順調（4/13）
  > 【水準】💎割安（6.0/7）— PER2.98倍・PEG0.738・52週54.8% ／ 💰単元28.1万円
  > 【戦略】当日終値2812円の指値で反転を取りにいく。SL2450円（直近5日安値）／⚠1単元リスク36200円（枠超過）
- 1417 MIRAIT ONE Corporation｜choruko_reversal｜✅順調｜🟢値頃｜FAIL_UWAHIGE｜3,304円｜💰33.1万円｜—
- 6340 澁谷工業｜choruko_reversal/granville_oshime/granville_rebound｜✅順調｜🟢値頃｜PASS｜5,090円｜💰50.9万円｜reversal 5090/SL4350（✅即時可）｜⚠日程不明 ⚠1単元でリスク枠超過（74000円）
  > 【業態】飲料用充填装置の最大手。無菌充填機に定評。メカトロシステム製販、農業設備も。
  > 【いま】終値5,090円・直近5日-1.55%（材料未確認）
  > 【調子】✅順調（4/13） — E軸判定不能(進捗データ不足)
  > 【水準】🟢値頃（5.0/7）— PER12.8倍・PEG0.6575・52週65.8% ／ 💰単元50.9万円
  > 【戦略】当日終値5090円の指値で反転を取りにいく。SL4350円（直近5日安値）／⚠1単元リスク74000円（枠超過）
- 6674 ジーエス・ユアサ　コーポレーション｜choruko_reversal｜✅順調｜🟢値頃｜PASS｜4,587円｜💰45.9万円｜reversal 4587/SL3940（✅即時可）｜⚠日程不明 📐進捗 上振れ 26.1% ⚠1単元でリスク枠超過（64700円）
  > 【業態】産業用・車載用の鉛蓄電池大手。三相蓄電システム、車載用リチウム電池に注力。
  > 【いま】終値4,587円・直近5日+0.22%（材料未確認）
  > 【調子】✅順調（4/13） — 上方修正済み
  > 【水準】🟢値頃（5.0/7）— PER11.23倍・PEG1.2402・52週24.2% ／ 💰単元45.9万円
  > 【戦略】当日終値4587円の指値で反転を取りにいく。SL3940円（直近5日安値）／⚠1単元リスク64700円（枠超過）
- 8381 San-in Godo Bank Ltd.｜choruko_reversal/granville_rebound｜✅順調｜⚪妥当｜PASS｜2,190円｜💰21.9万円｜reversal 2190.5/SL1921（✅即時可）｜🚨決算直前 11/12(残1営業日)
  > 【業態】山陰が地盤。鳥取・島根で預金トップ。広島・岡山等に展開、法人取引拡大へ。
  > 【いま】終値2,190円・直近5日+5.59%（材料未確認）
  > 【調子】✅順調（4/13） — E軸判定不能(進捗データ不足)
  > 【水準】⚪妥当（4.2/7）— PER12.79倍・PEG0.801・52週62.2% ／ 💰単元21.9万円
  > 【戦略】当日終値2190.5円の指値で反転を取りにいく。SL1921円（直近5日安値）
- 4272 Nippon Kayaku Co., Ltd.｜choruko_reversal/granville_tenkan/granville_oshime｜✅順調｜⚪妥当｜PASS｜1,858円｜💰18.6万円｜reversal 1857.5/SL1752（✅即時可）｜⚠日程不明 📐進捗 上振れ 13.1%
  > 【業態】火薬から機能化学品など多角化。医薬、自動車部材等。抗がん剤に強み。(化学)
  > 【いま】終値1,858円・直近5日-4.57%（材料未確認）
  > 【調子】✅順調（4/13） — 上方修正済み
  > 【水準】⚪妥当（4.0/7）— PER11.04倍・PEG1.161・52週57.3% ／ 💰単元18.6万円
  > 【戦略】当日終値1857.5円の指値で反転を取りにいく。SL1752円（直近5日安値）
- 6923 Stanley Electric Co., Ltd.｜choruko_reversal｜✅順調｜⚪妥当｜PASS｜3,249円｜💰32.5万円｜⛔提案なし(材料後出し)｜⚡材料後出し ⚠日程不明 📐進捗 遅れ -19.8%
  > 【業態】自動車用照明器大手。ホンダ向け比重大。LEDの電子制御機器も収益大。
  > 【いま】終値3,249円・直近5日+3.90%・📌「統合報告書2026」発行のお知らせ
  > 【調子】✅順調（4/13） — 🔼加速
  > 【水準】⚪妥当（4.0/7）— PER11.76倍・PEG0.8367・52週47.6% ／ 💰単元32.5万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 7276 Koito Manufacturing Co., Ltd.｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_UWAHIGE｜2,497円｜💰24.9万円｜—
- 1820 Nishimatsu Construction Co., Ltd.｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_UWAHIGE｜5,445円｜💰54.5万円｜—
- 4042 東ソー｜choruko_reversal｜✅順調｜⚪妥当｜PASS｜2,497円｜💰25.0万円｜reversal 2497/SL2305.5（✅即時可）｜⚠日程不明
  > 【業態】塩ビ・苛性ソーダ・石化大手。高機能材に強み。水処理、バイオ等の先端事業も。
  > 【いま】終値2,497円・直近5日-1.36%（材料未確認）
  > 【調子】✅順調（4/13） — 質注意
  > 【水準】⚪妥当（3.0/7）— PER13.03倍・PEG56.098・52週33.2% ／ 💰単元25.0万円
  > 【戦略】当日終値2497円の指値で反転を取りにいく。SL2305.5円（直近5日安値）
- 3282 Comforia Residential REIT, Inc.｜choruko_reversal｜✅順調｜🟡やや割高｜FAIL_INSEN｜85,600円｜💰8.7万円｜—
- 8524 North Pacific Bank, Ltd.｜choruko_reversal/granville_rebound｜⚠減速｜🟡やや割高｜PASS｜1,251円｜💰12.5万円｜⛔提案なし(指名鮮度切れ 13営業日)｜⏰決算 11/13(残2営業日) ⚠業績基調が下向き（⚠減速）
  > 【業態】北海道地盤で資金量第２地銀最大。拓銀と札幌銀の取込で拡大。
  > 【いま】終値1,251円・直近5日+5.93%（材料未確認）
  > 【調子】⚠減速（4/13） — 減収
  > 【水準】🟡やや割高（2.8/7）— PER15.92倍・PEG0.8698・52週78.1% ／ 💰単元12.5万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 13営業日)）
- 4021 Nissan Chemical Corporation｜choruko_reversal｜✅順調｜🟡やや割高｜FAIL_UWAHIGE｜7,015円｜💰68.8万円｜—
- 5631 Japan Steel Works, Ltd.｜choruko_reversal｜✅順調｜🟡やや割高｜PASS｜6,013円｜💰60.1万円｜⛔提案なし(指名鮮度切れ 18営業日)｜⚠日程不明
  > 【業態】大型鋳鍛鋼、樹脂成形機で世界有数。射出成形機にも強み。防衛関連も。
  > 【いま】終値6,013円・直近5日+3.83%（材料未確認）
  > 【調子】✅順調（4/13） — 質注意
  > 【水準】🟡やや割高（2.0/7）— PER21.08倍・PEG3.7905・52週20% ／ 💰単元60.1万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 18営業日)）
- 6750 エレコム｜choruko_reversal｜✅順調｜🟡やや割高｜FAIL_UWAHIGE｜1,854円｜💰18.7万円｜—
- 1944 Kinden Corporation｜choruko_reversal｜✅順調｜🟢値頃｜PASS｜5,870円｜💰58.7万円｜⛔提案なし(指名鮮度切れ 18営業日)｜⚠日程不明 📐進捗 上振れ 47.9%
  > 【業態】電設工事でトップ級。関電系で依存度約2割。情報通信工事など全国展開。
  > 【いま】終値5,870円・直近5日+0.41%（材料未確認）
  > 【調子】✅順調（3/13） — 上方修正済み
  > 【水準】🟢値頃（5.0/7）— PER12.87倍・PEG1.1577・52週21.5% ／ 💰単元58.7万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 18営業日)）
- 6332 月島ホールディングス｜choruko_reversal｜✅順調｜⚪妥当｜PASS｜2,395円｜💰23.9万円｜reversal 2395/SL2096（✅即時可）｜⚠日程不明 📐進捗 遅れ -23.7%
  > 【業態】上下水道の汚泥処理など水環境事業と化学プラントが主力。JFE水事業統合。
  > 【いま】終値2,395円・直近5日+2.39%（材料未確認）
  > 【調子】✅順調（3/13） — ⚠減速
  > 【水準】⚪妥当（4.0/7）— PER11.08倍・PEG1.7078・52週21% ／ 💰単元23.9万円
  > 【戦略】当日終値2395円の指値で反転を取りにいく。SL2096円（直近5日安値）
- 6368 Organo Corp.｜choruko_reversal｜✅順調｜⚪妥当｜PASS｜1,800円｜💰18.0万円｜reversal 1800/SL1509（✅即時可）｜⚠日程不明
  > 【業態】機械（水ビジネス・半導体製造装置・原子力発電関連）
  > 【いま】終値1,800円・直近5日-16.08%（材料未確認）
  > 【調子】✅順調（3/13） — 質注意
  > 【水準】⚪妥当（4.0/7）— PER13.8倍・PEG2.8146・52週11.5% ／ 💰単元18.0万円
  > 【戦略】当日終値1800円の指値で反転を取りにいく。SL1509円（直近5日安値）
- 8198 Maxvalu Tokai Co., Ltd.｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜3,150円｜💰31.8万円｜—｜⚡材料後出し
- 1951 エクシオグループ（エクシオＧ）｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜2,396円｜💰24.0万円｜—
- 1952 Shin Nippon Air Technologies Co., Ltd.｜choruko_reversal｜✅順調｜⚪妥当｜PASS｜2,925円｜💰29.2万円｜⛔提案なし(指名鮮度切れ 18営業日)｜🚨決算直前 11/12(残1営業日)
  > 【業態】三井系、空調設備工事会社。原子力空調、微粒子可視化など独自技術注力。
  > 【いま】終値2,925円・直近5日+2.17%（材料未確認）
  > 【調子】✅順調（3/13） — E軸判定不能(進捗データ不足)
  > 【水準】⚪妥当（3.0/7）— PER10.41倍・PEG2.6706・52週18.5% ／ 💰単元29.2万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 18営業日)）
- 4028 石原産業｜choruko_reversal｜🔻悪化｜⚪妥当｜PASS｜2,616円｜💰26.2万円｜reversal 2616/SL2195（✅即時可）｜⚠業績基調が下向き（🔻悪化） 📐進捗 遅れ -11.2% ⚠1単元でリスク枠超過（42100円）
  > 【業態】未取得（次回以降に取得）
  > 【いま】終値2,616円・直近5日+3.81%（材料未確認）
  > 【調子】🔻悪化（3/13） — 経常減益-28.7%
  > 【水準】⚪妥当（3.0/7）— PER14.1倍・PEG—・52週22.9% ／ 💰単元26.2万円
  > 【戦略】当日終値2616円の指値で反転を取りにいく。SL2195円（直近5日安値）／⚠1単元リスク42100円（枠超過）
- 5602 栗本鐵工所（栗本鉄）｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_UWAHIGE｜1,432円｜💰14.3万円｜—
- 9533 TOHO GAS Co., Ltd.｜choruko_reversal｜🔻悪化｜⚪妥当｜FAIL_UWAHIGE｜1,238円｜💰12.4万円｜—
- 1860 Toda Corporation｜choruko_reversal｜✅順調｜🟡やや割高｜FAIL_UWAHIGE｜1,440円｜💰14.4万円｜—
- 3105 日清紡ホールディングス｜choruko_reversal｜✅順調｜🟡やや割高｜PASS｜1,991円｜💰19.9万円｜reversal 1991/SL1791（✅即時可）｜⚠日程不明
  > 【業態】綿紡老舗から転換。ブレーキ摩擦材で世界首位。防災無線、デジタル技術を推進。
  > 【いま】終値1,991円・直近5日-6.00%（材料未確認）
  > 【調子】✅順調（3/13） — 進捗モデル値域外
  > 【水準】🟡やや割高（2.0/7）— PER11.97倍・PEG—・52週48.7% ／ 💰単元19.9万円
  > 【戦略】当日終値1991円の指値で反転を取りにいく。SL1791円（直近5日安値）
- 4008 住友精化｜choruko_reversal｜🔻悪化｜🔴過熱｜FAIL_INSEN｜1,355円｜💰14.3万円｜—
- 4966 上村工業｜choruko_reversal｜✅順調｜🟡やや割高｜FAIL_INSEN｜16,670円｜💰172.7万円｜—
- 6055 Japan Material Co., Ltd.｜choruko_reversal｜✅順調｜🟡やや割高｜PASS｜1,868円｜💰18.7万円｜⛔提案なし(指名鮮度切れ 13営業日)｜🚨決算直前 11/12(残1営業日)
  > 【業態】半導体製造向け特殊ガス供給装置製販。3D画像処理ツールや太陽光発電も。
  > 【いま】終値1,868円・直近5日-1.94%（材料未確認）
  > 【調子】✅順調（3/13） — E軸判定不能(進捗データ不足)
  > 【水準】🟡やや割高（2.0/7）— PER17.77倍・PEG7.1297・52週29.9% ／ 💰単元18.7万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 13営業日)）
- 6741 日本信号｜choruko_reversal｜✅順調｜🟡やや割高｜PASS｜1,647円｜💰16.5万円｜reversal 1647/SL1508（✅即時可）｜⚠日程不明 📐進捗 上振れ 48.5%
  > 【業態】信号最大手。鉄道、交通ともに高シェア。駅改札、ホームドアや駐車場機にも強み。
  > 【いま】終値1,647円・直近5日-5.02%（材料未確認）
  > 【調子】✅順調（3/13） — 質注意
  > 【水準】🟡やや割高（2.0/7）— PER10.28倍・PEG7.6079・52週61.1% ／ 💰単元16.5万円
  > 【戦略】当日終値1647円の指値で反転を取りにいく。SL1508円（直近5日安値）
- 6807 Japan Aviation Electronics Industry, Limited｜choruko_reversal｜✅順調｜🟡やや割高｜PASS｜2,324円｜💰23.2万円｜reversal 2324/SL2087（✅即時可）｜⚠日程不明
  > 【業態】NEC系コネクター大手。小型、高速伝送で競争力。車、航空・宇宙向け電子機器も。
  > 【いま】終値2,324円・直近5日-0.30%（材料未確認）
  > 【調子】✅順調（3/13） — 質注意
  > 【水準】🟡やや割高（2.0/7）— PER26.11倍・PEG8.5466・52週26.7% ／ 💰単元23.2万円
  > 【戦略】当日終値2324円の指値で反転を取りにいく。SL2087円（直近5日安値）
- 7220 Musashi Seimitsu Industry Co., Ltd.｜choruko_reversal｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜2,166円｜💰24.0万円｜—
- 5310 Toyo Tanso Co., Ltd.｜choruko_reversal/ai_reversal｜🔻悪化｜🔴過熱｜PASS｜6,310円｜💰63.1万円｜reversal 6310/SL5360（✅即時可）｜⚠日程不明 ⚠業績基調が下向き（🔻悪化） ⚠1単元でリスク枠超過（95000円）
  > 【業態】等方性黒鉛で先駆、世界高シェア。半導体製造用るつぼが主力。一貫生産。
  > 【いま】終値6,310円・直近5日-1.71%（材料未確認）
  > 【調子】🔻悪化（3/13） — 質注意
  > 【水準】🔴過熱（1.0/7）— PER26.47倍・PEG—・52週40.5% ／ 💰単元63.1万円
  > 【戦略】当日終値6310円の指値で反転を取りにいく。SL5360円（直近5日安値）／⚠1単元リスク95000円（枠超過）
- 6479 ミネベア｜choruko_reversal｜➖横ばい｜💎割安｜FAIL_UWAHIGE｜2,974円｜💰29.2万円｜—
- 1719 HAZAMA ANDO Corporation｜choruko_reversal｜➖横ばい｜⚪妥当｜FAIL_INSEN｜1,734円｜💰17.4万円｜—
- 1926 ライト工業（ライト）｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜921円｜💰9.2万円｜—｜⚡材料後出し
- 1979 大気社｜choruko_reversal｜➖横ばい｜⚪妥当｜PASS｜3,365円｜💰33.6万円｜reversal 3365/SL3240（✅即時可）｜⚠日程不明
  > 【業態】空調工事大手。自動車塗装設備工事で国内トップ。海外積極展開。
  > 【いま】終値3,365円・直近5日-5.87%（材料未確認）
  > 【調子】➖横ばい（2/13） — 質注意
  > 【水準】⚪妥当（3.0/7）— PER11.64倍・PEG13.7355・52週16.5% ／ 💰単元33.6万円
  > 【戦略】当日終値3365円の指値で反転を取りにいく。SL3240円（直近5日安値）
- 6753 Sharp Corporation｜choruko_reversal｜🔻悪化｜⚪妥当｜FAIL_INSEN｜503円｜💰5.4万円｜—
- 7278 Exedy Corporation｜choruko_reversal｜➖横ばい｜⚪妥当｜PASS｜5,290円｜💰52.9万円｜reversal 5290/SL5010（✅即時可）｜⚠日程不明
  > 【業態】アイシン系でクラッチ首位。自動車用トルクコンバーターが主力。マニュアル部品でも高シェア。
  > 【いま】終値5,290円・直近5日+3.93%（材料未確認）
  > 【調子】➖横ばい（2/13） — 進捗判定不能(自動抽出範囲外)
  > 【水準】⚪妥当（3.0/7）— PER13.59倍・PEG—・52週21.9% ／ 💰単元52.9万円
  > 【戦略】当日終値5290円の指値で反転を取りにいく。SL5010円（直近5日安値）
- 3445 RS Technologies Co. Ltd.｜choruko_reversal｜➖横ばい｜🟡やや割高｜PASS｜4,745円｜💰47.5万円｜⛔提案なし(指名鮮度切れ 13営業日)｜⚠日程不明
  > 【業態】半導体製造装置テスト用ウエハ再生加工大手。中国では新品生産。海外売上比大。
  > 【いま】終値4,745円・直近5日+2.04%（材料未確認）
  > 【調子】➖横ばい（2/13） — 質注意
  > 【水準】🟡やや割高（2.8/7）— PER12.62倍・PEG3.7155・52週25.4% ／ 💰単元47.5万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 13営業日)）
- 6366 Chiyoda Corp.｜choruko_reversal｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜744円｜💰7.6万円｜—
- 9722 藤田観光｜choruko_reversal｜➖横ばい｜🔴過熱｜FAIL_INSEN｜2,877円｜💰29.0万円｜—
- 5844 Kyoto Financial Group,Inc.｜choruko_reversal｜🔻悪化｜🔴過熱｜PASS｜4,241円｜💰42.4万円｜reversal 4241/SL3790（✅即時可）｜⏰決算 11/13(残2営業日) ⚠業績基調が下向き（🔻悪化） ⚠1単元でリスク枠超過（45100円）
  > 【業態】京都府内唯一の地銀。製造業に強み。近畿広域に拡大へ。財務体質に定評。
  > 【いま】終値4,241円・直近5日+4.51%（材料未確認）
  > 【調子】🔻悪化（2/13） — E軸判定不能(進捗データ不足)
  > 【水準】🔴過熱（1.4/7）— PER22.69倍・PEG—・52週53.2% ／ 💰単元42.4万円
  > 【戦略】当日終値4241円の指値で反転を取りにいく。SL3790円（直近5日安値）／⚠1単元リスク45100円（枠超過）
- 2379 dip Corporation｜choruko_reversal｜⚠減速｜💎割安｜FAIL_INSEN｜1,500円｜💰15.3万円｜—
- 6632 JVCKENWOOD Corporation｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_UWAHIGE｜805円｜💰7.9万円｜—
- 1946 Toenec Corporation｜choruko_reversal｜⚠減速｜⚪妥当｜PASS｜1,858円｜💰18.6万円｜⛔提案なし(指名鮮度切れ 18営業日)｜⚠日程不明 ⚠業績基調が下向き（⚠減速）
  > 【業態】電気工事大手。中部電系で依存度約4割。配電工事に強み。一般工事を強化。
  > 【いま】終値1,858円・直近5日+6.78%（材料未確認）
  > 【調子】⚠減速（1/13）
  > 【水準】⚪妥当（3.0/7）— PER9.65倍・PEG2.5366・52週29.7% ／ 💰単元18.6万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 18営業日)）
- 4746 東計電算｜choruko_reversal｜⚠減速｜⚪妥当｜PASS｜1,767円｜💰17.7万円｜reversal 1767/SL1667（✅即時可）｜⚠日程不明 ⚠業績基調が下向き（⚠減速） 📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】独立系の情報処理会社。ソフト開発を主力に運用、BPOやデータセンターなども。
  > 【いま】終値1,767円・直近5日-0.62%（材料未確認）
  > 【調子】⚠減速（1/13） — 質注意
  > 【水準】⚪妥当（3.0/7）— PER15.31倍・PEG6.209・52週66.1% ／ 💰単元17.7万円
  > 【戦略】当日終値1767円の指値で反転を取りにいく。SL1667円（直近5日安値）
- 4980 Dexerials Corp.｜choruko_reversal/ai_reversal｜⚠減速｜⚪妥当｜PASS｜2,598円｜💰26.0万円｜⛔提案なし(材料後出し)｜⚡材料後出し 📉決算反応日 11/12 ⚠業績基調が下向き（⚠減速）
  > 【業態】ディスプレーなどの光学材料、電子材料を製造、販売。スマホ向け世界高シェア。
  > 【いま】終値2,598円・直近5日-2.97%・📊2027年３月期 第２四半期（中間期）決算短信〔ＩＦＲＳ〕（連結）
  > 【調子】⚠減速（1/13） — E軸判定不能(進捗データ不足)
  > 【水準】⚪妥当（3.0/7）— PER15.82倍・PEG54.5592・52週16.4% ／ 💰単元26.0万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 7003 Mitsui ES Holdings Co., Ltd.｜choruko_reversal｜⚠減速｜⚪妥当｜PASS｜3,757円｜💰37.6万円｜⛔提案なし(指名鮮度切れ 19営業日)｜⚠日程不明 ⚠業績基調が下向き（⚠減速）
  > 【業態】船舶ディーゼル首位。船舶用推進、港湾物流事業が両輪。水素・SAF燃料注力。
  > 【いま】終値3,757円・直近5日+9.25%・📌[Delayed]Notice Concerning the Execution of an Agreement Relating to a Tender Offer for Shares of a Subsidiary (KAJI TECHNOLOGY CORPORATION) and ～
  > 【調子】⚠減速（1/13） — 上方修正済み
  > 【水準】⚪妥当（3.0/7）— PER11.49倍・PEG4.655・52週14.4% ／ 💰単元37.6万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 19営業日)）
- 5482 Aichi Steel Corporation｜choruko_reversal｜⚠減速｜🟡やや割高｜PASS｜2,580円｜💰25.8万円｜⛔提案なし(指名鮮度切れ 18営業日)｜⚠日程不明 ⚠業績基調が下向き（⚠減速）
  > 【業態】トヨタ系の特殊鋼大手。構造用鋼中心にチタン、ステンレス。磁気応用製品を拡大。
  > 【いま】終値2,580円・直近5日+8.63%（材料未確認）
  > 【調子】⚠減速（1/13） — 税引前代替
  > 【水準】🟡やや割高（2.0/7）— PER16.58倍・PEG—・52週23% ／ 💰単元25.8万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 18営業日)）
- 6370 栗田工業｜choruko_reversal｜🔻悪化｜🟡やや割高｜PASS｜5,445円｜💰54.5万円｜reversal 5445/SL4678（✅即時可）｜⚠日程不明 ⚠業績基調が下向き（🔻悪化） 📐進捗 遅れ -50.6% ⚠1単元でリスク枠超過（76700円）
  > 【業態】総合水処理最大手。超純水供給事業、水処理薬品事業に競争力。海外強化。
  > 【いま】終値5,445円・直近5日+1.83%（材料未確認）
  > 【調子】🔻悪化（1/13） — 経常減益-26.1%
  > 【水準】🟡やや割高（2.0/7）— PER19.95倍・PEG—・52週15.1% ／ 💰単元54.5万円
  > 【戦略】当日終値5445円の指値で反転を取りにいく。SL4678円（直近5日安値）／⚠1単元リスク76700円（枠超過）
- 6436 アマノ｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜3,419円｜💰34.4万円｜—
- 6960 Fukuda Denshi Co., Ltd.｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_UWAHIGE｜9,970円｜💰100.3万円｜—
- 9948 Arcs Company, Limited｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜3,610円｜💰36.5万円｜—
- 1963 日揮ホールディングス｜choruko_reversal｜🔻悪化｜🔴過熱｜PASS｜2,243円｜💰22.4万円｜⛔提案なし(材料後出し)｜⚡材料後出し 📉決算反応日 11/12 ⚠業績基調が下向き（🔻悪化）
  > 【業態】総合エンジニアリング最大手。世界各地で石油、化学、発電、水素、LNGプラント建設。
  > 【いま】終値2,243円・直近5日+5.80%・📊2027年３月期　第２四半期（中間期）決算短信〔日本基準〕(連結)
  > 【調子】🔻悪化（1/13） — 質注意
  > 【水準】🔴過熱（1.4/7）— PER11.81倍・PEG—・52週48.6% ／ 💰単元22.4万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 6804 ホシデン｜choruko_reversal｜🔻悪化｜⚪妥当｜FAIL_UWAHIGE｜2,196円｜💰22.0万円｜—
- 7148 Financial Products Group Co., Ltd.｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜1,400円｜💰14.1万円｜—
- 2109 ＤＭ三井製糖｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜3,535円｜💰35.1万円｜—
- 6349 Komori Corporation｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_UWAHIGE｜1,719円｜💰17.2万円｜—
- 8194 Life Corporation｜choruko_reversal｜⚠減速｜🔴過熱｜FAIL_UWAHIGE｜2,707円｜💰27.0万円｜—｜⚡材料後出し
- 3612 WORLD CO.,LTD.｜choruko_reversal｜業績データ取得不可(経常益予想非開示)｜💎割安｜FAIL_INSEN｜1,484円｜💰14.9万円｜—
- 8975 Ichigo Office REIT Investment Corporation｜choruko_reversal｜判定保留(変則決算)｜💎割安｜FAIL_INSEN｜86,200円｜💰8.7万円｜—
- 8253 Credit Saison Co., Ltd.｜choruko_reversal｜取得不可｜💎割安｜FAIL_INSEN｜4,134円｜💰41.5万円｜—
- 8367 南都銀行｜choruko_reversal/granville_oshime｜業績データ取得不可(売上/経常欠損)｜💎割安｜PASS｜1,797円｜💰18.0万円｜reversal 1797/SL1558（✅即時可）｜⚠日程不明
  > 【業態】奈良地盤の地銀で県内シェアは圧倒的。効率経営に定評。中小企業に積極。
  > 【いま】終値1,797円・直近5日+4.96%（材料未確認）
  > 【調子】業績データ取得不可(売上/経常欠損)（—/13） — 業績データ取得不可(売上/経常欠損)
  > 【水準】💎割安（6.0/7）— PER11.29倍・PEG0.23・52週70.8% ／ 💰単元18.0万円
  > 【戦略】当日終値1797円の指値で反転を取りにいく。SL1558円（直近5日安値）
- 7381 ＣＣＩグループ｜choruko_reversal/granville_rebound｜業績データ取得不可(売上/経常欠損)｜🟢値頃｜PASS｜1,146円｜💰11.5万円｜reversal 1146/SL985（✅即時可）｜⚠日程不明 📐進捗 遅れ -13.8%
  > 【業態】石川県を地盤。北國銀行を中核に総合金融サービス。富山県も重点。
  > 【いま】終値1,146円・直近5日+5.33%・🔁自己株式の取得状況に関するお知らせ
  > 【調子】業績データ取得不可(売上/経常欠損)（—/13） — 売上欠損
  > 【水準】🟢値頃（5.6/7）— PER13.26倍・PEG0.3886・52週65.4% ／ 💰単元11.5万円
  > 【戦略】当日終値1146円の指値で反転を取りにいく。SL985円（直近5日安値）
- 5831 Shizuoka Financial Group, Inc.｜choruko_reversal/granville_rebound｜業績データ取得不可(売上/経常欠損)｜🟢値頃｜FAIL_INSEN｜3,201円｜💰31.8万円｜—
- 7167 めぶきフィナンシャルグループ｜choruko_reversal/granville_rebound｜取得不可｜🟢値頃｜FAIL_UWAHIGE｜1,518円｜💰13.8万円｜—
- 8345 Bank of Iwate Ltd.｜choruko_reversal/granville_rebound｜業績データ取得不可(売上/経常欠損)｜🟢値頃｜PASS｜2,128円｜💰21.3万円｜reversal 2128/SL1819（✅即時可）｜🚨決算直前 11/12(残1営業日) ⚠1単元でリスク枠超過（30900円）
  > 【業態】岩手地盤の地銀中位。県内で圧倒的。青森銀、秋田銀と提携。リース、コンサルも。
  > 【いま】終値2,128円・直近5日+2.75%（材料未確認）
  > 【調子】業績データ取得不可(売上/経常欠損)（—/13） — 業績データ取得不可(売上/経常欠損)
  > 【水準】🟢値頃（5.0/7）— PER14.71倍・PEG1.1461・52週58.2% ／ 💰単元21.3万円
  > 【戦略】当日終値2128円の指値で反転を取りにいく。SL1819円（直近5日安値）／⚠1単元リスク30900円（枠超過）
- 8354 ふくおかフィナンシャルグループ｜choruko_reversal｜業績データ取得不可(売上/経常欠損)｜🟢値頃｜FAIL_UWAHIGE｜7,237円｜💰69.4万円｜—
- 8359 Hachijuni Nagano Bank, Ltd.｜choruko_reversal/granville_rebound｜業績データ取得不可(売上/経常欠損)｜🟢値頃｜PASS｜2,537円｜💰25.4万円｜⛔提案なし(材料後出し)｜⚡材料後出し ⚠日程不明 📐進捗 上振れ 10.1%
  > 【業態】長野地盤の地銀上位。県全域にシェア圧倒的。堅実経営。長野銀と合併。
  > 【いま】終値2,537円・直近5日+5.75%・📌Notice Concerning the Capital Ratio as of September 30, 2026
  > 【調子】業績データ取得不可(売上/経常欠損)（—/13） — 業績データ取得不可(売上/経常欠損)
  > 【水準】🟢値頃（5.0/7）— PER14.38倍・PEG0.313・52週74.3% ／ 💰単元25.4万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 8370 紀陽銀行｜choruko_reversal｜業績データ取得不可(売上/経常欠損)｜🟢値頃｜PASS｜1,536円｜💰15.4万円｜reversal 1536/SL1419（✅即時可）｜⚠日程不明
  > 【業態】未取得（次回以降に取得）
  > 【いま】終値1,536円・直近5日-0.78%（材料未確認）
  > 【調子】業績データ取得不可(売上/経常欠損)（—/13） — 業績データ取得不可(売上/経常欠損)
  > 【水準】🟢値頃（5.0/7）— PER11.87倍・PEG0.9081・52週67% ／ 💰単元15.4万円
  > 【戦略】当日終値1536円の指値で反転を取りにいく。SL1419円（直近5日安値）
- 4293 セプテーニ・ホールディングス（セプテニＨＤ）｜choruko_reversal｜業績データ取得不可(経常益予想非開示)｜⚪妥当｜FAIL_INSEN｜467円｜💰4.7万円｜—
- 7384 Procrea Holdings,Inc.｜choruko_reversal/granville_rebound｜業績データ取得不可(売上/経常欠損)｜⚪妥当｜PASS｜4,130円｜💰41.3万円｜reversal 4130/SL3470（✅即時可）｜⏰決算 11/13(残2営業日) ⚠1単元でリスク枠超過（66000円）
  > 【業態】青森地盤の地銀。青森銀とみちのく銀が経営統合。25年1月に合併。
  > 【いま】終値4,130円・直近5日+3.25%（材料未確認）
  > 【調子】業績データ取得不可(売上/経常欠損)（—/13） — 業績データ取得不可(売上/経常欠損)
  > 【水準】⚪妥当（4.0/7）— PER16.71倍・PEG0.231・52週56.3% ／ 💰単元41.3万円
  > 【戦略】当日終値4130円の指値で反転を取りにいく。SL3470円（直近5日安値）／⚠1単元リスク66000円（枠超過）
- 8174 NIPPON GAS Co., Ltd.｜choruko_reversal｜業績データ取得不可(売上/経常欠損)｜⚪妥当｜FAIL_UWAHIGE｜896円｜💰8.8万円｜—
- 8304 あおぞら銀行｜choruko_reversal｜取得不可｜⚪妥当｜FAIL_UWAHIGE｜3,175円｜💰31.4万円｜—｜⚡材料後出し
- 8334 Gunma Bank, Ltd.｜choruko_reversal/granville_rebound｜業績データ取得不可(売上/経常欠損)｜⚪妥当｜PASS｜2,634円｜💰26.3万円｜⛔提案なし(指名鮮度切れ 13営業日)｜⚠日程不明
  > 【業態】群馬地盤の地銀上位。県内で圧倒的シェア。東京など近県を強化。海外も。
  > 【いま】終値2,634円・直近5日+4.81%（材料未確認）
  > 【調子】業績データ取得不可(売上/経常欠損)（—/13） — 業績データ取得不可(売上/経常欠損)
  > 【水準】⚪妥当（4.0/7）— PER14.78倍・PEG0.8299・52週64.8% ／ 💰単元26.3万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 13営業日)）
- 8366 滋賀銀行｜choruko_reversal/granville_rebound｜取得不可｜⚪妥当｜PASS｜2,374円｜💰23.7万円｜reversal 2374/SL2097.5（✅即時可）｜⏰決算 11/13(残2営業日)
  > 【業態】滋賀県内で優位。徹底した収益管理体制。環境関連の法人融資に注力。
  > 【いま】終値2,374円・直近5日-1.49%（材料未確認）
  > 【調子】取得不可（—/13） — 業績データ取得不可
  > 【水準】⚪妥当（4.0/7）— PER19.15倍・PEG0.4253・52週59.4% ／ 💰単元23.7万円
  > 【戦略】当日終値2374円の指値で反転を取りにいく。SL2097.5円（直近5日安値）
- 6810 Maxell, Ltd.｜choruko_reversal/granville_oshime/granville_rebound｜業績データ取得不可(経常益予想非開示)｜⚪妥当｜PASS｜2,205円｜💰22.1万円｜reversal 2205/SL2010（✅即時可）｜⚠日程不明
  > 【業態】電池や産業用部材が主力。車載、理美容家電向け注力。全固体電池量産化。
  > 【いま】終値2,205円・直近5日-1.78%（材料未確認）
  > 【調子】業績データ取得不可(経常益予想非開示)（—/13） — 経常欠損
  > 【水準】⚪妥当（3.5/7）— PER12.14倍・PEG—・52週40.4% ／ 💰単元22.1万円
  > 【戦略】当日終値2205円の指値で反転を取りにいく。SL2010円（直近5日安値）
- 3591 WACOAL HOLDINGS CORP｜choruko_reversal｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜3,629円｜💰37.0万円｜—
- 7177 ＧＭＯフィナンシャルホールディングス｜choruko_reversal｜取得不可｜⏸判定不能｜PASS｜1,060円｜💰10.6万円｜reversal 1060/SL960（✅即時可）｜⚠日程不明
  > 【業態】外為証拠金取引最大手、GMOグループ。傘下にGMOクリック証券、GMOコイン。
  > 【いま】終値1,060円・直近5日+6.32%（材料未確認）
  > 【調子】取得不可（—/13） — 業績データ取得不可(経常益予想非開示)
  > 【水準】⏸判定不能（—/7）— PER—倍・PEG—・52週51.8% ／ 💰単元10.6万円
  > 【戦略】当日終値1060円の指値で反転を取りにいく。SL960円（直近5日安値）
- 7186 横浜フィナンシャルグループ｜choruko_reversal｜業績データ取得不可｜⏸判定不能｜PASS｜1,768円｜💰17.7万円｜⛔提案なし(材料後出し)｜⚡材料後出し 📉決算反応日 11/12
  > 【業態】傘下に横浜銀、東日本銀、神奈川銀。総合力に強み。中小企業、個人に注力。
  > 【いま】終値1,768円・直近5日+6.38%・📊2027年３月期 第２四半期（中間期）決算短信〔日本基準〕(連結)
  > 【調子】業績データ取得不可（—/13） — kabutan年次表を解析できず
  > 【水準】⏸判定不能（—/7）— PER—倍・PEG—・52週74.4% ／ 💰単元17.7万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 7322 三十三フィナンシャルグループ｜choruko_reversal/granville_rebound｜業績データ取得不可｜⏸判定不能｜PASS｜1,859円｜💰18.6万円｜reversal 1859/SL1579（✅即時可）｜⏰決算 11/13(残2営業日)
  > 【業態】三重県が地盤の三重銀行と第三銀行が経営統合。合併で三十三銀行へ。
  > 【いま】終値1,859円・直近5日+3.28%（材料未確認）
  > 【調子】業績データ取得不可（—/13） — kabutan年次表を解析できず
  > 【水準】⏸判定不能（—/7）— PER—倍・PEG—・52週66.4% ／ 💰単元18.6万円
  > 【戦略】当日終値1859円の指値で反転を取りにいく。SL1579円（直近5日安値）
- 8600 トモニホールディングス｜choruko_reversal｜業績データ取得不可｜⏸判定不能｜PASS｜1,029円｜💰10.3万円｜reversal 1029/SL901（✅即時可）｜⏰決算 11/13(残2営業日)
  > 【業態】傘下に香川銀と徳島大正銀。大阪や東京等店舗広域化。中小企業に注力。
  > 【いま】終値1,029円・直近5日+1.48%（材料未確認）
  > 【調子】業績データ取得不可（—/13） — kabutan年次表を解析できず
  > 【水準】⏸判定不能（—/7）— PER—倍・PEG—・52週63.8% ／ 💰単元10.3万円
  > 【戦略】当日終値1029円の指値で反転を取りにいく。SL901円（直近5日安値）
- 8616 Tokai Tokyo Financial Holdings, Inc.｜choruko_reversal｜業績データ取得不可｜⏸判定不能｜PASS｜776円｜💰7.8万円｜reversal 776/SL705（✅即時可）｜⚠日程不明
  > 【業態】中部地区地盤の証券準大手。対面営業が主体。有力地銀と提携推進。
  > 【いま】終値776円・直近5日+4.02%（材料未確認）
  > 【調子】業績データ取得不可（—/13） — 通期予想なし
  > 【水準】⏸判定不能（—/7）— PER—倍・PEG—・52週54.8% ／ 💰単元7.8万円
  > 【戦略】当日終値776円の指値で反転を取りにいく。SL705円（直近5日安値）
- 8698 Monex Group, Inc.｜choruko_reversal｜業績データ取得不可(経常益予想非開示)｜⏸判定不能｜FAIL_UWAHIGE｜592円｜💰5.8万円｜—｜⚡材料後出し
- 4410 ハリマ化成グループ（ハリマ化成Ｇ）｜stf_kakuhen｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜1,419円｜💰13.8万円｜—
- 6668 ＡＤプラズマ｜stf_kakuhen/granville_oshime｜🔥絶好調｜🟢値頃｜PASS｜3,965円｜💰39.6万円｜⛔提案なし(手法ブランチ不明)｜⚠日程不明
  > 【業態】高周波プラズマ電源装置最大手。液晶、半導体装置向け主力。技術に強み。
  > 【いま】終値3,965円・直近5日-6.49%（材料未確認）
  > 【調子】🔥絶好調（10/13） — E軸判定不能(進捗データ不足)
  > 【水準】🟢値頃（5.0/7）— PER9.15倍・PEG0.1384・52週56.8% ／ 💰単元39.6万円
  > 【戦略】発注対象外（⛔提案なし(手法ブランチ不明)）
- 7713 シグマ光機｜stf_kakuhen｜🔥絶好調｜🟢値頃｜PASS｜2,888円｜💰28.9万円｜⛔提案なし(手法ブランチ不明)｜⚠日程不明
  > 【業態】レーザー関連部品やユニット・システムの総合力に強み。半導体、液晶製造装置向け。
  > 【いま】終値2,888円・直近5日-1.94%（材料未確認）
  > 【調子】🔥絶好調（10/13） — 上方修正済み
  > 【水準】🟢値頃（5.0/7）— PER13.82倍・PEG0.2181・52週57.9% ／ 💰単元28.9万円
  > 【戦略】発注対象外（⛔提案なし(手法ブランチ不明)）
- 5832 ちゅうぎんフィナンシャルグループ（ちゅうぎんＦ）｜stf_kakuhen｜🔥絶好調｜⚪妥当｜PASS｜3,582円｜💰35.8万円｜⛔提案なし(手法ブランチ不明)｜⚠日程不明
  > 【業態】岡山地盤の地銀上位、中国銀行中核に総合サービス。香川、広島、兵庫で強化。
  > 【いま】終値3,582円・直近5日+2.55%（材料未確認）
  > 【調子】🔥絶好調（10/13）
  > 【水準】⚪妥当（4.2/7）— PER11.58倍・PEG0.2709・52週83.4% ／ 💰単元35.8万円
  > 【戦略】発注対象外（⛔提案なし(手法ブランチ不明)）
- 5018 ＭＯＲＥＳＣＯ｜stf_kakuhen｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜2,868円｜💰28.9万円｜—
- 5246 ＥＬＥＭＥＮＴＳ｜stf_kakuhen/granville_oshime｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜994円｜💰9.9万円｜—
- 7942 ＪＳＰ｜stf_kakuhen｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜3,105円｜💰30.6万円｜—
- 9962 ミスミグループ本社｜stf_kakuhen/changepoint｜🔥絶好調｜⚪妥当｜PASS｜4,269円｜💰42.7万円｜⛔提案なし(手法ブランチ不明)｜⚠日程不明
  > 【業態】金型用部品の専門商社・ミスミが中核。ネット・カタログ販売。半製品で納期短縮。
  > 【いま】終値4,269円・直近5日+6.78%（材料未確認）
  > 【調子】🔥絶好調（10/13） — 上方修正済み
  > 【水準】⚪妥当（3.0/7）— PER21.25倍・PEG0.3634・52週100% ／ 💰単元42.7万円
  > 【戦略】発注対象外（⛔提案なし(手法ブランチ不明)）
- 3498 霞ヶ関Ｃ｜stf_kakuhen/granville_tenkan｜🔥絶好調｜💎割安｜FAIL_INSEN｜7,490円｜💰75.2万円｜—
- 9110 ＮＳユナイテッド海運（ユナイテド海）｜stf_kakuhen｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜10,540円｜💰105.6万円｜—
- 3994 マネーフォワード｜stf_kakuhen/changepoint｜🔥絶好調｜🔴過熱｜FAIL_UWAHIGE｜7,857円｜💰79.4万円｜—
- 9766 コナミグループ（コナミＧ）｜stf_kakuhen｜🔥絶好調｜🟡やや割高｜FAIL_INSEN｜28,150円｜💰289.8万円｜—
- 6814 古野電｜stf_kakuhen｜⚡好調｜🟢値頃｜PASS｜7,690円｜💰76.9万円｜⛔提案なし(手法ブランチ不明)｜⚠日程不明
  > 【業態】魚群探知機など船舶用電子機器で世界高シェア。GPSや医療機器も積極展開。
  > 【いま】終値7,690円・直近5日-0.65%（材料未確認）
  > 【調子】⚡好調（7/13） — 上方修正済み
  > 【水準】🟢値頃（5.0/7）— PER14.3倍・PEG0.7052・52週60.3% ／ 💰単元76.9万円
  > 【戦略】発注対象外（⛔提案なし(手法ブランチ不明)）
- 4503 アステラス製薬（アステラス）｜stf_kakuhen｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜2,634円｜💰26.2万円｜—
- 5932 三協立山｜stf_kakuhen/granville_oshime｜⚡好調｜⚪妥当｜PASS｜716円｜💰7.2万円｜⛔提案なし(手法ブランチ不明)｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】アルミ建材大手。住宅用、ビル向けなどに強み。マテリアル事業や商業施設事業も。
  > 【いま】終値716円・直近5日-0.83%（材料未確認）
  > 【調子】⚡好調（7/13） — E軸判定不能(進捗データ不足)
  > 【水準】⚪妥当（4.0/7）— PER22.45倍・PEG0.3203・52週64% ／ 💰単元7.2万円
  > 【戦略】発注対象外（⛔提案なし(手法ブランチ不明)）
- 6758 ソニーグループ｜stf_kakuhen/ai_momentum｜⚡好調｜⚪妥当｜FAIL_INSEN｜4,200円｜💰42.4万円｜—
- 3091 ブロンコビリー｜stf_kakuhen/granville_oshime/changepoint｜⚡好調｜🟡やや割高｜FAIL_UWAHIGE｜3,045円｜💰30.4万円｜—
- 3479 ＴＫＰ｜stf_kakuhen/granville_tenkan｜⚡好調｜🔴過熱｜FAIL_INSEN｜2,145円｜💰21.4万円｜—
- 4417 グローバルセキュリティエキスパート（Ｇセキュリ）｜stf_kakuhen｜⚡好調｜🔴過熱｜FAIL_INSEN｜8,480円｜💰84.7万円｜—
- 6505 東洋電機製造｜stf_kakuhen/ai_momentum｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜3,000円｜💰30.0万円｜—
- 6532 ベイカレント｜stf_kakuhen｜⚡好調｜🟡やや割高｜FAIL_INSEN｜11,970円｜💰124.2万円｜—
- 4176 ココナラ｜stf_kakuhen｜✅順調｜💎割安｜FAIL_UWAHIGE｜276円｜💰2.8万円｜—
- 7366 ＬＩＴＡＬＩＣＯ（りたりこ）｜stf_kakuhen｜業績データ取得不可(経常益予想非開示)｜⚪妥当｜FAIL_INSEN｜2,066円｜💰21.1万円｜—

## グランビル銘柄
- 5254 Arent, Inc.｜granville_tenkan｜🚀確変｜⚪妥当｜FAIL_INSEN｜3,875円｜💰39.2万円｜—
- 3927 アークン｜granville_tenkan｜🚀確変｜💎割安｜PASS｜929円｜💰9.3万円｜momentum 933/SL876.1（⏸位置不適(25MA下 -9.3%／52週 26.3%)）｜⏰決算 11/13(残2営業日) ⚠市場に劣後 RS20 -19.9pt
  > 【業態】情報セキュリティ製品の開発・販売・保守。中小企業向けの業務システムに注力。
  > 【いま】終値929円・直近5日+3.34%・📌フーバーブレイン、自社開発セキュリティ製品「Eye“247” Safety Zone」にAI統合分析機能を付加する開発に着手
  > 【調子】🚀確変（11/13） — 進捗モデル値域外
  > 【水準】💎割安（6.0/7）— PER15.11倍・PEG0.144・52週26.3% ／ 💰単元9.3万円
  > 【戦略】当日高値超えの逆指値933円で順張り参戦を検討。上限942.3円・SL876.1円目安（⏸位置不適(25MA下 -9.3%／52週 26.3%)）
- 6768 Tamura Corporation｜granville_tenkan/granville_oshime｜🔥絶好調｜💎割安｜PASS｜727円｜💰7.3万円｜momentum 732/SL687.1（⏸位置不適(25MA下 -13.49%／52週 29.7%)）｜⚠日程不明 📐進捗 上振れ 15.1% ⚠市場に劣後 RS20 -21.0pt
  > 【業態】弱電用トランス、リアクター大手。ハンダ、絶縁膜や音声・ワイヤレス機器も。海外生産メイン。
  > 【いま】終値727円・直近5日-3.84%（材料未確認）
  > 【調子】🔥絶好調（10/13） — 上方修正済み
  > 【水準】💎割安（6.0/7）— PER8.9倍・PEG0.2384・52週29.7% ／ 💰単元7.3万円
  > 【戦略】当日高値超えの逆指値732円で順張り参戦を検討。上限739.3円・SL687.1円目安（⏸位置不適(25MA下 -13.49%／52週 29.7%)）
- 8944 Land Business Co., Ltd.｜granville_tenkan｜🔥絶好調｜💎割安｜FAIL_INSEN｜243円｜💰2.4万円｜—
- 7725 INTER ACTION Corporation｜granville_tenkan｜🔥絶好調｜🟢値頃｜PASS｜1,737円｜💰17.4万円｜⛔提案なし(指名鮮度切れ 19営業日)｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】光源装置製造会社。CCD検査用、撮像素子に強み。排ガス処理や歯車試験も。
  > 【いま】終値1,737円・直近5日-2.42%（材料未確認）
  > 【調子】🔥絶好調（10/13） — E軸判定不能(進捗データ不足)
  > 【水準】🟢値頃（5.0/7）— PER16.8倍・PEG0.1787・52週46% ／ 💰単元17.4万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 19営業日)）
- 3491 ＧＡ　ｔｅｃｈｎｏｌｏｇｉｅｓ（ＧＡテクノ）｜granville_tenkan｜🔥絶好調｜💎割安｜PASS｜1,558円｜💰15.6万円｜momentum 1568/SL1473（✅即時可）｜📋カルテ窓 12/10(残20営業日)
  > 【業態】不動産投資ポータルサービス「リノシー」を運営。不動産業向けSaaS製品販売・開発も。
  > 【いま】終値1,558円・直近5日+7.60%・📌AI不動産投資のRENOSY、「不動産投資顧客動向レポート 2026年7～9月」を公開
  > 【調子】🔥絶好調（8/13）
  > 【水準】💎割安（6.0/7）— PER11.71倍・PEG0.2871・52週35.8% ／ 💰単元15.6万円
  > 【戦略】当日高値超えの逆指値1568円で順張り参戦を検討。上限1583.7円・SL1473円目安
- 6470 Taiho Kogyo Co., Ltd.｜granville_tenkan｜🔥絶好調｜💎割安｜PASS｜916円｜💰9.2万円｜⛔提案なし(指名鮮度切れ 14営業日)｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8） 📐進捗 上振れ 13.0%
  > 【業態】トヨタ系。自動車向け軸受けやアルミダイカスト製品、金型が軸。EV向け製品に積極。
  > 【いま】終値916円・直近5日-6.91%（材料未確認）
  > 【調子】🔥絶好調（8/13） — 🔼進捗先行
  > 【水準】💎割安（6.0/7）— PER6.82倍・PEG0.1143・52週43.9% ／ 💰単元9.2万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 14営業日)）
- 6744 能美防災｜granville_tenkan｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜4,495円｜💰43.3万円｜—
- 8012 Nagase & Co., Ltd.｜granville_tenkan｜🔥絶好調｜🟢値頃｜PASS｜1,211円｜💰12.1万円｜momentum 1216.5/SL1142.6（✅即時可）｜⚠日程不明 📐進捗 上振れ 26.1%
  > 【業態】染料、合成樹脂化学の専門商社最大手。医薬品原料に強み。海外を拡大。
  > 【いま】終値1,211円・直近5日+0.46%（材料未確認）
  > 【調子】🔥絶好調（8/13） — 上方修正済み
  > 【水準】🟢値頃（5.0/7）— PER10.17倍・PEG0.3225・52週78.3% ／ 💰単元12.1万円
  > 【戦略】当日高値超えの逆指値1216.5円で順張り参戦を検討。上限1228.7円・SL1142.6円目安
- 9006 Keikyu Corporation｜granville_tenkan｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1,556円｜💰15.9万円｜—｜⚡材料後出し
- 3002 グンゼ｜granville_tenkan｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜4,370円｜💰42.4万円｜—
- 8697 日本取引所グループ｜granville_tenkan/changepoint｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜2,179円｜💰21.5万円｜—
- 4523 エーザイ｜granville_tenkan｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜5,025円｜💰50.1万円｜—
- 9742 アイネス｜granville_tenkan｜🔥絶好調｜⚪妥当｜PASS｜2,390円｜💰23.9万円｜momentum 2399/SL2254.1（✅即時可）｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】独立系のSI大手。組合・団体、地方自治体向けに強み。三菱総研と提携。
  > 【いま】終値2,390円・直近5日+2.75%（材料未確認）
  > 【調子】🔥絶好調（8/13） — E軸判定不能(進捗データ不足)
  > 【水準】⚪妥当（3.0/7）— PER29.29倍・PEG0.0455・52週83.8% ／ 💰単元23.9万円
  > 【戦略】当日高値超えの逆指値2399円で順張り参戦を検討。上限2423円・SL2254.1円目安
- 4005 住友化学｜granville_tenkan｜⚡好調｜💎割安｜FAIL_UWAHIGE｜513円｜💰5.0万円｜—
- 3964 オークネット｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_INSEN｜1,326円｜💰14.1万円｜—
- 4534 Mochida Pharmaceutical Co., Ltd.｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_INSEN｜3,285円｜💰32.6万円｜—
- 3405 クラレ｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜1,946円｜💰19.2万円｜—｜⚡材料後出し
- 3496 アズーム｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜5,170円｜💰49.4万円｜—
- 4401 ＡＤＥＫＡ｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜4,408円｜💰43.2万円｜—
- 7744 ノーリツ鋼機｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,042円｜💰20.4万円｜—
- 8095 Astena Holdings Co.,Ltd.｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜548円｜💰5.5万円｜—
- 4507 塩野義製薬｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜3,056円｜💰30.4万円｜—｜⚡材料後出し
- 5532 リアルゲイト｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜3,400円｜💰33.9万円｜—
- 7970 Shin-Etsu Polymer Co., Ltd.｜granville_tenkan｜⚡好調｜⚪妥当｜PASS｜2,443円｜💰24.4万円｜⛔提案なし(指名鮮度切れ 14営業日)｜⚠日程不明
  > 【業態】信越化学系樹脂加工メーカー。ウエハ容器が主力。車載タッチスイッチや住生活資材も。
  > 【いま】終値2,443円・直近5日+0.70%（材料未確認）
  > 【調子】⚡好調（7/13） — E軸:進捗50.7%<前年同期51.7%
  > 【水準】⚪妥当（3.0/7）— PER16.65倍・PEG0.5844・52週79.4% ／ 💰単元24.4万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 14営業日)）
- 5838 Rakuten Bank, Ltd.｜granville_tenkan｜⚡好調｜💎割安｜FAIL_UWAHIGE｜6,421円｜💰63.0万円｜—｜⚡材料後出し
- 1941 中電工｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_INSEN｜5,080円｜💰49.0万円｜—
- 8061 Seika Corporation｜granville_tenkan｜⚡好調｜🟢値頃｜PASS｜2,866円｜💰28.7万円｜⛔提案なし(指名鮮度切れ 19営業日)｜⚠日程不明
  > 【業態】三菱重工系機械商社。重化学工業・発電プラントが主力。バルブ・水中ポンプも。
  > 【いま】終値2,866円・直近5日+0.77%（材料未確認）
  > 【調子】⚡好調（6/13） — 上方修正済み
  > 【水準】🟢値頃（5.0/7）— PER10.96倍・PEG0.4019・52週49.1% ／ 💰単元28.7万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 19営業日)）
- 4848 Fullcast Holdings Co., Ltd.｜granville_tenkan/granville_oshime｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜1,815円｜💰18.1万円｜—
- 6371 Tsubakimoto Chain Co.｜granville_tenkan｜⚡好調｜⚪妥当｜PASS｜2,642円｜💰26.4万円｜momentum 2649/SL2489.1（✅即時可）｜⚠日程不明 📐進捗 上振れ 18.4%
  > 【業態】自動車・産業用チェーン世界首位。搬送・保管システム装置も展開。モビリティに注力。
  > 【いま】終値2,642円・直近5日+1.93%（材料未確認）
  > 【調子】⚡好調（6/13） — 上方修正済み
  > 【水準】⚪妥当（3.0/7）— PER12.1倍・PEG0.9393・52週77.2% ／ 💰単元26.4万円
  > 【戦略】当日高値超えの逆指値2649円で順張り参戦を検討。上限2675.5円・SL2489.1円目安
- 4045 Toagosei Co., Ltd.｜granville_tenkan｜⚡好調｜🟡やや割高｜FAIL_UWAHIGE｜1,789円｜💰17.6万円｜—
- 6099 エラン｜granville_tenkan｜⚡好調｜🟡やや割高｜FAIL_INSEN｜781円｜💰7.8万円｜—
- 3935 Edia Co. Ltd.｜granville_tenkan｜⚡好調｜💎割安｜FAIL_INSEN｜654円｜💰6.6万円｜—
- 4554 Fuji Pharma Co., Ltd.｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜1,851円｜💰18.9万円｜—
- 4617 中国塗料｜granville_tenkan｜⚡好調｜🟢値頃｜PASS｜3,570円｜💰35.7万円｜momentum 3585/SL3365.2（✅即時可）｜⚠日程不明 📐進捗 上振れ 16.2%
  > 【業態】船舶用塗料の世界大手。工業用塗料も展開。アジアを中心に海外販売網。
  > 【いま】終値3,570円・直近5日+5.47%（材料未確認）
  > 【調子】⚡好調（5/13） — 上方修正済み
  > 【水準】🟢値頃（5.0/7）— PER13.64倍・PEG0.9146・52週35.2% ／ 💰単元35.7万円
  > 【戦略】当日高値超えの逆指値3585円で順張り参戦を検討。上限3620.8円・SL3365.2円目安
- 9842 アークランズ｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_INSEN｜1,901円｜💰19.2万円｜—
- 6432 竹内製作所｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜7,630円｜💰76.7万円｜—
- 8016 オンワード HD｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜784円｜💰7.6万円｜—
- 4403 日油｜granville_tenkan｜⚡好調｜⚪妥当｜PASS_DOJI｜2,541円｜💰25.4万円｜momentum 2570/SL2476.5（⏳確認足待ち）
  > 【業態】油脂化学系製品大手。機能化成品、化薬、ライフサイエンス、DDS事業など多角化。
  > 【いま】終値2,541円・直近5日-6.67%（材料未確認）
  > 【調子】⚡好調（5/13） — 質注意
  > 【水準】⚪妥当（3.0/7）— PER13.82倍・PEG4.853・52週6.9% ／ 💰単元25.4万円
  > 【戦略】当日高値超えの逆指値2570円で順張り参戦を検討。上限2595.7円・SL2476.5円目安（⏳確認足待ち）
- 7606 ＴＡＢＡＹＡホールディングス｜granville_tenkan｜⚡好調｜⚪妥当｜PASS｜2,610円｜💰26.1万円｜momentum 2629/SL2470.3（✅即時可）｜📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】セレクトショップ大手。婦人服・服飾や紳士服、雑貨を販売。「ユナイテッドアローズ」主力。
  > 【いま】終値2,610円・直近5日+3.61%（材料未確認）
  > 【調子】⚡好調（5/13）
  > 【水準】⚪妥当（3.0/7）— PER11.33倍・PEG1.3707・52週79.2% ／ 💰単元26.1万円
  > 【戦略】当日高値超えの逆指値2629円で順張り参戦を検討。上限2655.3円・SL2470.3円目安
- 7747 朝日インテック｜granville_tenkan｜⚡好調｜🔴過熱｜FAIL_UWAHIGE｜3,807円｜💰38.6万円｜—
- 4169 Enechange Ltd.｜granville_tenkan｜⚠減速｜⚪妥当｜FAIL_INSEN｜270円｜💰2.7万円｜—
- 4568 第一三共｜granville_tenkan｜✅順調｜⚪妥当｜FAIL_INSEN｜2,770円｜💰28.0万円｜—
- 9045 Keihan Holdings Co., Ltd.｜granville_tenkan｜⚠減速｜⚪妥当｜FAIL_INSEN｜3,301円｜💰31.8万円｜—
- 2488 ＪＴＰ｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_INSEN｜1,391円｜💰14.1万円｜—
- 417A ブルーゾーンホールディングス｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_INSEN｜1,898円｜💰19.5万円｜—
- 4549 Eiken Chemical Co., Ltd.｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_INSEN｜2,182円｜💰22.1万円｜—
- 7269 スズキ｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_UWAHIGE｜2,188円｜💰22.5万円｜—
- 3092 ＺＯＺＯ｜granville_tenkan｜✅順調｜🔴過熱｜FAIL_INSEN｜1,152円｜💰11.7万円｜—
- 3549 クスリのアオキホールディングス｜granville_tenkan｜✅順調｜🔴過熱｜FAIL_UWAHIGE｜5,084円｜💰50.8万円｜—
- 5184 ニチリン｜granville_tenkan｜✅順調｜🔴過熱｜FAIL_INSEN｜4,150円｜💰41.8万円｜—｜⚡材料後出し
- 6592 Mabuchi Motor Co., Ltd.｜granville_tenkan｜✅順調｜🔴過熱｜FAIL_INSEN｜1,794円｜💰18.2万円｜—
- 8160 KISOJI CO., LTD.｜granville_tenkan｜✅順調｜🔴過熱｜FAIL_UWAHIGE｜2,481円｜💰24.8万円｜—
- 8113 Unicharm Corporation｜granville_tenkan｜✅順調｜🔴過熱｜FAIL_INSEN｜1,094円｜💰10.9万円｜—
- 4166 Cacco, Inc.｜granville_tenkan｜✅順調｜💎割安｜FAIL_INSEN｜660円｜💰6.7万円｜—
- 8056 ＢＩＰＲＯＧＹ｜granville_tenkan｜✅順調｜🟢値頃｜PASS｜4,654円｜💰46.5万円｜momentum 4660/SL4375.7（⏸位置不適(25MA下 -4.51%／52週 28.6%)）｜⚠日程不明 📐進捗 遅れ -25.7%
  > 【業態】大日本印刷系の情報システム大手。クラウド事業に注力。金融、流通、空運に強み。
  > 【いま】終値4,654円・直近5日-4.49%（材料未確認）
  > 【調子】✅順調（3/13）
  > 【水準】🟢値頃（5.0/7）— PER13.97倍・PEG1.4739・52週28.6% ／ 💰単元46.5万円
  > 【戦略】当日高値超えの逆指値4660円で順張り参戦を検討。上限4706.6円・SL4375.7円目安（⏸位置不適(25MA下 -4.51%／52週 28.6%)）
- 9163 Nareru Group Inc.｜granville_tenkan｜✅順調｜🟢値頃｜FAIL_UWAHIGE｜2,041円｜💰20.5万円｜—
- 3563 ＦＯＯＤ　＆　ＬＩＦＥ　ＣＯＭＰＡＮＩＥＳ｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_UWAHIGE｜5,775円｜💰57.1万円｜—
- 4540 Tsumura & Co.｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_INSEN｜3,838円｜💰39.0万円｜—
- 7734 Riken Keiki Co., Ltd.｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_UWAHIGE｜3,335円｜💰33.2万円｜—
- 2897 Nissin Foods Holdings Co., Ltd.｜granville_tenkan｜✅順調｜🔴過熱｜FAIL_INSEN｜2,900円｜💰31.7万円｜—
- 6745 ホーチキ｜granville_tenkan｜✅順調｜🔴過熱｜FAIL_UWAHIGE｜2,169円｜💰21.1万円｜—
- 4902 Konica Minolta, Inc.｜granville_tenkan｜➖横ばい｜🟢値頃｜PASS_DOJI｜574円｜💰5.7万円｜⛔提案なし(指名鮮度切れ 13営業日)｜⚠日程不明
  > 【業態】複合機中堅で印刷関連を展開。液晶TACフィルムで世界高シェア。X線撮影装置も。
  > 【いま】終値574円・直近5日-9.39%（材料未確認）
  > 【調子】➖横ばい（2/13） — 税引前代替
  > 【水準】🟢値頃（5.2/7）— PER9.03倍・PEG—・52週36.1% ／ 💰単元5.7万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 13営業日)）
- 5233 太平洋セメント｜granville_tenkan｜🔻悪化｜⚪妥当｜FAIL_INSEN｜3,945円｜💰38.6万円｜—
- 9837 Morito Co., Ltd.｜granville_tenkan｜➖横ばい｜⚪妥当｜FAIL_INSEN｜1,816円｜💰18.2万円｜—
- 9956 Valor Holdings Co., Ltd.｜granville_tenkan｜➖横ばい｜⚪妥当｜FAIL_INSEN｜1,561円｜💰16.9万円｜—
- 8803 Heiwa Real Estate Co., Ltd.｜granville_tenkan｜➖横ばい｜🟡やや割高｜FAIL_INSEN｜2,307円｜💰23.3万円｜—
- 4922 コーセーホールディングス｜granville_tenkan｜➖横ばい｜🔴過熱｜FAIL_INSEN｜5,693円｜💰62.1万円｜—
- 6328 Ebara Jitsugyo Co., Ltd.｜granville_tenkan｜⚠減速｜⚪妥当｜FAIL_INSEN｜2,289円｜💰23.1万円｜—
- 4912 ライオン｜granville_tenkan｜⚠減速｜⚪妥当｜FAIL_INSEN｜2,108円｜💰21.3万円｜—
- 1928 積水ハウス｜granville_tenkan｜⚠減速｜🟡やや割高｜FAIL_INSEN｜3,507円｜💰35.4万円｜—
- 4552 JCR Pharmaceuticals Co., Ltd.｜granville_tenkan｜🔻悪化｜🔴過熱｜FAIL_INSEN｜493円｜💰5.0万円｜—
- 5105 ＴＯＹＯ　ＴＩＲＥ｜granville_tenkan｜⚠減速｜🟡やや割高｜FAIL_INSEN｜4,209円｜💰42.4万円｜—
- 8167 リテールパートナーズ｜granville_tenkan｜⚠減速｜🟡やや割高｜FAIL_INSEN｜1,361円｜💰13.8万円｜—
- 9735 セコム｜granville_tenkan｜⚠減速｜🔴過熱｜FAIL_INSEN｜6,765円｜💰68.0万円｜—｜⚡材料後出し
- 4375 セーフィー｜granville_tenkan/changepoint｜取得不可｜💎割安｜PASS｜620円｜💰6.2万円｜momentum 622/SL583.7（⏸位置不適(25MA下 -4.86%／52週 14.4%)）｜⚠日程不明
  > 【業態】クラウド型映像プラットフォーム「Safie」の開発・運営。防犯・監視カメラに強み。
  > 【いま】終値620円・直近5日-2.52%（材料未確認）
  > 【調子】取得不可（—/13） — 業績データ取得不可
  > 【水準】💎割安（7.0/7）— PER—倍・PEG—・52週14.4% ／ 💰単元6.2万円
  > 【戦略】当日高値超えの逆指値622円で順張り参戦を検討。上限628.2円・SL583.7円目安（⏸位置不適(25MA下 -4.86%／52週 14.4%)）
- 7921 ＴＡＫＡＲＡ　＆　ＣＯＭＰＡＮＹ｜granville_tenkan｜業績データ取得不可(経常益予想非開示)｜🟢値頃｜FAIL_INSEN｜4,170円｜💰41.7万円｜—
- 3182 オイシックス｜granville_tenkan｜業績データ取得不可(経常益予想非開示)｜🟡やや割高｜FAIL_INSEN｜1,629円｜💰16.4万円｜—
- 4765 ＳＢＩグローバルアセットマネジメント｜granville_tenkan/granville_oshime｜判定保留｜⏸判定不能｜FAIL_INSEN｜623円｜💰6.1万円｜—
- 2811 Kagome Co., Ltd.｜granville_tenkan｜業績データ取得不可(経常益予想非開示)｜🔴過熱｜FAIL_INSEN｜2,770円｜💰28.4万円｜—
- 2206 江崎グリコ｜granville_tenkan｜—｜—｜FAIL_INSEN｜5,017円｜💰—万円｜—
- 2502 Asahi Group Holdings, Ltd.｜granville_tenkan｜—｜—｜FAIL_INSEN｜1,710円｜💰—万円｜—
- 8801 三井不動産｜granville_tenkan｜—｜—｜FAIL_INSEN｜1,548円｜💰—万円｜—
- 8804 東京建物｜granville_tenkan｜—｜—｜FAIL_INSEN｜3,338円｜💰—万円｜—
- 9401 東京放送ホールディングス｜granville_tenkan｜—｜—｜FAIL_INSEN｜6,057円｜💰—万円｜—
- 9418 Ｕ－ＮＥＸＴ　ＨＯＬＤＩＮＧＳ｜granville_tenkan｜—｜—｜FAIL_INSEN｜1,831円｜💰—万円｜—
- 6574 コンヴァノ｜granville_oshime｜🚀確変｜🟢値頃｜PASS｜961円｜💰9.6万円｜⛔型不一致: 既に支持帯以下｜⏰決算 11/13(残2営業日) 📐進捗 上振れ 76.8%
  > 【業態】関東・東海・関西にネイルサロンを展開。美容医薬、コンサル、投資など新規事業注力。
  > 【いま】終値961円・直近5日-16.58%（材料未確認）
  > 【調子】🚀確変（13/13） — 進捗モデル値域外
  > 【水準】🟢値頃（5.0/7）— PER7.61倍・PEG0.0143・52週20.1% ／ 💰単元9.6万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 7480 スズデン｜granville_oshime/granville_rebound｜🚀確変｜⚪妥当｜PASS｜3,560円｜💰35.6万円｜⛔型不一致: 既に支持帯以下｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】FA機器主力、技術商社。オムロンと特約店契約。電設資材中心。ネット販売に強み。
  > 【いま】終値3,560円・直近5日-4.69%（材料未確認）
  > 【調子】🚀確変（13/13）
  > 【水準】⚪妥当（4.0/7）— PER14.15倍・PEG0.123・52週82% ／ 💰単元35.6万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 5243 ｎｏｔｅ｜granville_oshime/granville_rebound｜🚀確変｜⚪妥当｜FAIL_INSEN｜2,746円｜💰27.8万円｜—
- 7806 MTG Co., Ltd.｜granville_oshime/changepoint｜🚀確変｜⚪妥当｜FAIL_INSEN｜8,110円｜💰82.3万円｜—｜⚡材料後出し
- 6834 精工技研｜granville_oshime/granville_rebound｜🔥絶好調｜💎割安｜PASS｜5,280円｜💰52.8万円｜⛔型不一致: 既に支持帯以下｜⏰決算 11/13(残2営業日) 📑TOPIX新規採用（2026-10-30 組入）
  > 【業態】光関連部品、金型技術に強み。携帯電話向けレンズ、自動車用センサーも展開。
  > 【いま】終値5,280円・直近5日-8.01%（材料未確認）
  > 【調子】🔥絶好調（10/13）
  > 【水準】💎割安（6.0/7）— PER25.66倍・PEG0.5272・52週58.1% ／ 💰単元52.8万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 7609 ダイトロン｜granville_oshime/granville_rebound｜🔥絶好調｜💎割安｜PASS｜3,770円｜💰37.7万円｜⛔型不一致: 既に支持帯以下｜⚠日程不明 📐進捗 上振れ 26.2%
  > 【業態】電子部品卸中堅。製造装置にも強み。スイッチ電源など自社製造製品に注力。
  > 【いま】終値3,770円・直近5日-0.13%（材料未確認）
  > 【調子】🔥絶好調（9/13） — 上方修正済み
  > 【水準】💎割安（6.0/7）— PER11.29倍・PEG0.3374・52週57.1% ／ 💰単元37.7万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 4382 HEROZ, Inc.｜granville_oshime/changepoint｜🔥絶好調｜🟢値頃｜PASS｜820円｜💰8.2万円｜⛔型不一致: 既に支持帯以下｜📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】未取得（次回以降に取得）
  > 【いま】終値820円・直近5日-4.21%（材料未確認）
  > 【調子】🔥絶好調（9/13） — E軸判定不能(進捗データ不足)
  > 【水準】🟢値頃（5.0/7）— PER48.52倍・PEG0.678・52週10.9% ／ 💰単元8.2万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 8137 サンワテクノス｜granville_oshime/granville_rebound｜🔥絶好調｜🟢値頃｜PASS｜3,880円｜💰38.8万円｜⛔型不一致: 既に支持帯以下｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】電子部品主体の専門商社。電機と機械も柱。エンジニアリング事業を強化。
  > 【いま】終値3,880円・直近5日+2.24%（材料未確認）
  > 【調子】🔥絶好調（9/13） — 上方修正済み
  > 【水準】🟢値頃（5.0/7）— PER11.03倍・PEG0.1686・52週51.8% ／ 💰単元38.8万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 153A Caulis, Inc.｜granville_oshime｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜2,056円｜💰22.6万円｜—
- 8392 大分銀行｜granville_oshime/granville_rebound｜🔥絶好調｜💎割安｜PASS｜2,757円｜💰27.6万円｜⛔型不一致: 既に支持帯以下｜⚠日程不明
  > 【業態】大分地盤の地銀中位。県内首位、堅実経営。香港に駐在員事務所も。
  > 【いま】終値2,757円・直近5日+2.22%（材料未確認）
  > 【調子】🔥絶好調（8/13）
  > 【水準】💎割安（6.0/7）— PER14.84倍・PEG0.4755・52週71.5% ／ 💰単元27.6万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 3156 レスター｜granville_oshime/granville_rebound｜🔥絶好調｜🟢値頃｜PASS｜5,250円｜💰52.5万円｜⛔型不一致: 既に支持帯以下｜⏰決算 11/13(残2営業日)
  > 【業態】UKCHDとバイテックHD統合、エレクトロニクス総合商社。半導体、電子機器・部品、エネルギー。
  > 【いま】終値5,250円・直近5日-0.19%（材料未確認）
  > 【調子】🔥絶好調（8/13） — E軸判定不能(進捗データ不足)
  > 【水準】🟢値頃（5.6/7）— PER10.94倍・PEG0.2079・52週62.8% ／ 💰単元52.5万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 8051 山善｜granville_oshime｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜1,843円｜💰17.8万円｜—
- 9304 澁澤倉庫｜granville_oshime｜🔥絶好調｜🟢値頃｜PASS｜1,957円｜💰19.6万円｜⛔提案なし(指名鮮度切れ 12営業日)｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】渋沢栄一創業、倉庫準大手。総合物流。資産活用し不動産事業。アジア開拓。
  > 【いま】終値1,957円・直近5日+0.57%（材料未確認）
  > 【調子】🔥絶好調（8/13） — 上方修正済み
  > 【水準】🟢値頃（5.0/7）— PER14.87倍・PEG0.6326・52週73.4% ／ 💰単元19.6万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 12営業日)）
- 2384 ＳＢＳホールディングス｜granville_oshime｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜5,530円｜💰51.1万円｜—
- 3968 セグエグループ｜granville_oshime｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜798円｜💰8.0万円｜—
- 5892 ＹＵＴＯＲＩ｜granville_oshime｜⚡好調｜🟢値頃｜PASS｜2,585円｜💰25.9万円｜⛔型不一致: 既に支持帯以下｜⏰決算 11/13(残2営業日)
  > 【業態】若者向け衣料品や雑貨などブランドの企画・卸売。EC販売が主軸。ZOZO傘下。
  > 【いま】終値2,585円・直近5日+3.23%（材料未確認）
  > 【調子】⚡好調（7/13） — E軸判定不能(進捗データ不足)
  > 【水準】🟢値頃（5.0/7）— PER17.63倍・PEG0.5868・52週55% ／ 💰単元25.9万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 6036 ＫｅｅＰｅｒ技研｜granville_oshime｜⚡好調｜🟢値頃｜FAIL_INSEN｜1,829円｜💰18.7万円｜—
- 3040 ソリトンシステムズ｜granville_oshime/granville_rebound｜⚡好調｜⚪妥当｜PASS｜2,963円｜💰29.6万円｜⛔型不一致: 既に支持帯以下｜🚨決算直前 11/12(残1営業日) 📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】情報・通信業（ソフト・システム開発・情報セキュリティ・セキュリティソフト関連）
  > 【いま】終値2,963円・直近5日+5.52%（材料未確認）
  > 【調子】⚡好調（7/13） — E軸判定不能(進捗データ不足)
  > 【水準】⚪妥当（4.0/7）— PER20.59倍・PEG0.63・52週60.2% ／ 💰単元29.6万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 3673 ブロードリーフ｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜476円｜💰4.8万円｜—｜⚡材料後出し
- 4398 ブロードバンドセキュリティ｜granville_oshime｜⚡好調｜⚪妥当｜PASS｜2,260円｜💰22.6万円｜⛔型不一致: 既に支持帯以下｜🚨決算直前 11/12(残1営業日)
  > 【業態】SBI系。クレジットカードデータのセキュリティ監視やコンサルティングサービス。漏洩対策も。
  > 【いま】終値2,260円・直近5日-2.96%（材料未確認）
  > 【調子】⚡好調（7/13） — E軸判定不能(進捗データ不足)
  > 【水準】⚪妥当（4.0/7）— PER21.26倍・PEG0.6129・52週49.8% ／ 💰単元22.6万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 4206 アイカ工業｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜4,249円｜💰42.8万円｜—
- 6736 Suncorporation｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜11,390円｜💰131.3万円｜—
- 8410 Seven Bank, Ltd.｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜351円｜💰3.5万円｜—
- 2492 インフォマート（インフォＭＴ）｜granville_oshime｜⚡好調｜🟡やや割高｜PASS｜736円｜💰7.4万円｜⛔型不一致: 既に支持帯以下｜⚠日程不明
  > 【業態】企業間取引をデジタル化するプラットフォームの運営。契約書サービスなども展開。
  > 【いま】終値736円・直近5日+1.38%（材料未確認）
  > 【調子】⚡好調（7/13）
  > 【水準】🟡やや割高（2.0/7）— PER63.45倍・PEG0.9001・52週84.9% ／ 💰単元7.4万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 8388 阿波銀行｜granville_oshime/granville_rebound｜⚡好調｜💎割安｜PASS｜1,936円｜💰19.4万円｜⛔型不一致: 既に支持帯以下｜⏰決算 11/13(残2営業日)
  > 【業態】徳島地盤の地銀で県内シェア首位。中小企業金融に注力。野村證券と提携。
  > 【いま】終値1,936円・直近5日+1.84%（材料未確認）
  > 【調子】⚡好調（6/13）
  > 【水準】💎割安（6.0/7）— PER4.28倍・PEG0.2236・52週75% ／ 💰単元19.4万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 3106 倉敷紡績｜granville_oshime｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜2,221円｜💰22.1万円｜—
- 6523 ＰＨＣホールディングス｜granville_oshime｜⚠減速｜🟢値頃｜FAIL_UWAHIGE｜1,404円｜💰14.0万円｜—｜⚡材料後出し
- 4674 クレスコ｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜1,959円｜💰19.5万円｜—
- 6250 Yamabiko Corporation｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜4,385円｜💰43.2万円｜—
- 9075 福山通運｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜6,250円｜💰63.5万円｜—｜⚡材料後出し
- 9552 クオンツ総研ホールディングス｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜1,146円｜💰11.1万円｜—
- 4498 Cybertrust Japan Co.Ltd.｜granville_oshime｜⚡好調｜⚪妥当｜PASS｜1,815円｜💰18.1万円｜⛔型不一致: 既に支持帯以下｜⚠日程不明 📐進捗 上振れ 21.7%
  > 【業態】情報・通信業
  > 【いま】終値1,815円・直近5日-7.96%（材料未確認）
  > 【調子】⚡好調（6/13） — 🔼加速
  > 【水準】⚪妥当（3.0/7）— PER24.17倍・PEG1.907・52週38.5% ／ 💰単元18.1万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 4413 baudroie,inc.｜granville_oshime｜⚡好調｜🟡やや割高｜FAIL_INSEN｜2,938円｜💰29.4万円｜—
- 6570 Kyowa Corporation Co. Ltd.｜granville_oshime｜⚡好調｜🔴過熱｜FAIL_INSEN｜3,755円｜💰44.5万円｜—
- 9536 SAIBU GAS HOLDINGS CO. LTD.｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,828円｜💰28.4万円｜—
- 436A サイバーソリューションズ（サイバＳＯＬ）｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜1,733円｜💰17.8万円｜—
- 6877 ＯＢＡＲＡ　ＧＲＯＵＰ（ＯＢＡＲＡＧ）｜granville_oshime｜⚡好調｜⚪妥当｜PASS｜6,770円｜💰67.7万円｜oshime 6762/SL6728.4（✅即時可）｜⏰決算 11/13(残2営業日) 📑TOPIX低減対象（次 01/29 第2回/8） 📐進捗 上振れ 11.2%
  > 【業態】自動車業界向け抵抗溶接機器の最大手。半導体向け研磨装置も展開。
  > 【いま】終値6,770円・直近5日+2.73%（材料未確認）
  > 【調子】⚡好調（5/13）
  > 【水準】⚪妥当（3.0/7）— PER12.84倍・PEG0.8045・52週87.7% ／ 💰単元67.7万円
  > 【戦略】6762円までの押し目を指値で待つ。SL6728.4円（25日線基準）
- 4258 AMIYA Corporation｜granville_oshime｜⚡好調｜🔴過熱｜PASS｜5,960円｜💰59.6万円｜⛔提案なし(材料後出し)｜⚡材料後出し 📉決算反応日 11/12
  > 【業態】情報・通信業
  > 【いま】終値5,960円・直近5日+2.23%・📊2026年12月期第３四半期決算短信〔日本基準〕(連結)
  > 【調子】⚡好調（5/13） — (質注意)
  > 【水準】🔴過熱（1.0/7）— PER56.43倍・PEG4.2245・52週70% ／ 💰単元59.6万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 6191 エボラブルアジア｜granville_oshime｜🔻悪化｜🔴過熱｜FAIL_UWAHIGE｜1,487円｜💰14.7万円｜—
- 5036 日本ビジネスシステムズ｜granville_oshime｜✅順調｜🟢値頃｜FAIL_INSEN｜1,751円｜💰17.6万円｜—
- 8395 佐賀銀行｜granville_oshime/granville_rebound｜⚠減速｜🟢値頃｜PASS｜6,170円｜💰61.7万円｜⛔型不一致: 既に支持帯以下｜⚠日程不明 ⚠業績基調が下向き（⚠減速） ⚠バリュートラップ疑い
  > 【業態】佐賀地盤の地銀中位。県内で圧倒的シェア。福岡で出店攻勢、営業基盤強化。
  > 【いま】終値6,170円・直近5日+0.98%（材料未確認）
  > 【調子】⚠減速（4/13） — A成長率0以下のためレバレッジ計算不可(C=0)
  > 【水準】🟢値頃（5.0/7）— PER11.17倍・PEG0.5746・52週72.7% ／ 💰単元61.7万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 6080 Ｍ＆Ａキャピタルパートナーズ｜granville_oshime/changepoint｜✅順調｜🟡やや割高｜PASS｜4,650円｜💰46.5万円｜oshime 4333/SL4311.4（✅即時可）｜⚠日程不明
  > 【業態】独立系の中小向けM&A仲介サービス会社。事業売却・買収、事業承継に強み。
  > 【いま】終値4,650円・直近5日+12.18%（材料未確認）
  > 【調子】✅順調（4/13） — 税引前代替
  > 【水準】🟡やや割高（2.0/7）— PER17.21倍・PEG1.211・52週98.3% ／ 💰単元46.5万円
  > 【戦略】4333円までの押し目を指値で待つ。SL4311.4円（25日線基準）
- 3042 セキュアヴェイル（セキュアヴェ）｜granville_oshime｜✅順調｜🔴過熱｜FAIL_INSEN｜904円｜💰9.8万円｜—
- 3762 テクマトリックス（テクマト）｜granville_oshime｜✅順調｜🔴過熱｜FAIL_UWAHIGE｜3,200円｜💰31.6万円｜—
- 6998 Nippon Tungsten Co., Ltd.｜granville_oshime/granville_rebound｜✅順調｜🔴過熱｜FAIL_UWAHIGE｜2,746円｜💰26.9万円｜—｜⚡材料後出し
- 5985 SUNCALL CORPORATION｜granville_oshime｜✅順調｜🟢値頃｜PASS｜1,711円｜💰17.1万円｜⛔提案なし(指名鮮度切れ 16営業日)｜⏰決算 11/13(残2営業日) 📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】精密部品メーカー。車用精密ばね主力でトヨタ・ホンダ中心。プリンタ部品も。HDD撤退。
  > 【いま】終値1,711円・直近5日-2.45%（材料未確認）
  > 【調子】✅順調（3/13） — E軸判定不能ではなく例年比マイナス(進捗45.8%<前年同期56.0%)
  > 【水準】🟢値頃（5.2/7）— PER8.23倍・PEG—・52週40.7% ／ 💰単元17.1万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 16営業日)）
- 338A ZenmuTech,Inc.｜granville_oshime｜✅順調｜⚪妥当｜PASS｜3,220円｜💰32.2万円｜⛔型不一致: 既に支持帯以下｜🚨決算直前 11/12(残1営業日) 📐進捗 遅れ -20.9%
  > 【業態】暗号技術を応用したセキュリティ技術開発・販売など情報漏洩対策を手掛ける。
  > 【いま】終値3,220円・直近5日-16.80%（材料未確認）
  > 【調子】✅順調（3/13） — 質注意
  > 【水準】⚪妥当（4.0/7）— PER29.06倍・PEG2.3249・52週33.7% ／ 💰単元32.2万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 9509 Hokkaido Electric Power Company,Incorporated｜granville_oshime｜🔻悪化｜⚪妥当｜FAIL_UWAHIGE｜1,124円｜💰11.1万円｜—
- 4208 UBE Corporation｜granville_oshime｜✅順調｜🟡やや割高｜FAIL_UWAHIGE｜3,292円｜💰32.9万円｜—
- 4044 Central Glass Co., Ltd.｜granville_oshime｜✅順調｜🔴過熱｜PASS｜4,435円｜💰44.4万円｜⛔提案なし(指名鮮度切れ 19営業日)｜🚨決算直前 11/12(残1営業日)
  > 【業態】板ガラス3位。主力は洗浄剤など化成品、ファインケミカル。海外事業整理、多角化推進。
  > 【いま】終値4,435円・直近5日+2.07%（材料未確認）
  > 【調子】✅順調（3/13） — E軸判定不能(進捗データ不足)
  > 【水準】🔴過熱（1.0/7）— PER13.74倍・PEG—・52週78.3% ／ 💰単元44.4万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 19営業日)）
- 456A Human Made Inc.｜granville_oshime｜✅順調｜🔴過熱｜FAIL_INSEN｜2,078円｜💰21.5万円｜—｜⚡材料後出し
- 3692 ＦＦＲＩセキュリティ｜granville_oshime｜➖横ばい｜🔴過熱｜FAIL_UWAHIGE｜7,490円｜💰73.3万円｜—
- 8255 Axial Retailing, Inc.｜granville_oshime｜➖横ばい｜🔴過熱｜FAIL_INSEN｜1,529円｜💰15.3万円｜—
- 8361 Ogaki Kyoritsu Bank, Ltd.｜granville_oshime/granville_rebound｜取得不可｜💎割安｜FAIL_UWAHIGE｜1,554円｜💰14.7万円｜—
- 9166 GENDA Inc.｜granville_oshime｜業績データ取得不可｜🟢値頃｜FAIL_UWAHIGE｜700円｜💰6.8万円｜—
- 336A ダイナミックマッププラットフォーム｜granville_oshime｜業績データ取得不可(経常益予想非開示)｜⚪妥当｜FAIL_INSEN｜1,152円｜💰11.4万円｜—
- 3993 PKSHA Technology, Inc.｜granville_oshime/changepoint｜業績データ取得不可｜⚪妥当｜PASS｜3,255円｜💰32.5万円｜⛔型不一致: 既に支持帯以下｜🚨決算直前 11/12(残1営業日)
  > 【業態】AIベンチャー。画像認識・自動対話などディープラーニング技術開発が軸。トヨタと連携。
  > 【いま】終値3,255円・直近5日-0.15%（材料未確認）
  > 【調子】業績データ取得不可（—/13） — 業績データ取得不可(売上/経常欠損)
  > 【水準】⚪妥当（3.5/7）— PER35.3倍・PEG—・52週42.8% ／ 💰単元32.5万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 8362 Fukui Bank, Ltd.｜granville_oshime｜🔻悪化｜🔴過熱｜PASS｜6,850円｜💰68.5万円｜⛔提案なし(指名鮮度切れ 20営業日)｜⏰決算 11/13(残2営業日) ⚠業績基調が下向き（🔻悪化）
  > 【業態】福井地盤の地銀中位。石川や富山にも展開。福邦銀と26年5月合併。
  > 【いま】終値6,850円・直近5日+3.16%（材料未確認）
  > 【調子】🔻悪化（—/13） — 経常減益-24.1%
  > 【水準】🔴過熱（1.4/7）— PER18.01倍・PEG—・52週71.3% ／ 💰単元68.5万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 20営業日)）
- 4432 ウイングアーク１ｓｔ｜granville_oshime｜業績データ取得不可(経常益予想非開示)｜🔴過熱｜FAIL_UWAHIGE｜3,510円｜💰34.4万円｜—
- 6027 Bengo4.com, Inc.｜granville_oshime｜業績データ取得不可｜🔴過熱｜FAIL_INSEN｜5,110円｜💰51.0万円｜—｜⚡材料後出し
- 3851 日本一ソフトウェア｜granville_rebound｜🚀確変｜💎割安｜FAIL_UWAHIGE｜1,182円｜💰11.6万円｜—
- 3778 SAKURA Internet Inc.｜granville_rebound｜🚀確変｜🟢値頃｜PASS｜3,160円｜💰31.6万円｜⛔提案なし(指名鮮度切れ 18営業日)｜⚠日程不明
  > 【業態】情報・通信業（データセンター・ホスティング・クラウドコンピューティング関連）
  > 【いま】終値3,160円・直近5日+9.72%（材料未確認）
  > 【調子】🚀確変（12/13） — 上方修正済み
  > 【水準】🟢値頃（5.0/7）— PER84.27倍・PEG0.0403・52週37.4% ／ 💰単元31.6万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 18営業日)）
- 3891 ニッポン高度紙工業｜granville_rebound｜🚀確変｜💎割安｜PASS｜5,790円｜💰57.9万円｜reversal 5790/SL4405（✅即時可）｜⚠日程不明 📐進捗 遅れ -10.4% ⚠1単元でリスク枠超過（138500円）
  > 【業態】電気絶縁用紙大手。アルミ電解コンデンサ用で世界首位。2次電池用セパレーターに力。
  > 【いま】終値5,790円・直近5日-2.03%（材料未確認）
  > 【調子】🚀確変（11/13） — 上方修正済み
  > 【水準】💎割安（6.0/7）— PER11.1倍・PEG0.1057・52週37.4% ／ 💰単元57.9万円
  > 【戦略】当日終値5790円の指値で反転を取りにいく。SL4405円（直近5日安値）／⚠1単元リスク138500円（枠超過）
- 6138 ダイジェット工業（ダイジェト）｜granville_rebound｜🚀確変｜💎割安｜PASS｜1,760円｜💰17.6万円｜reversal 1760/SL1532（✅即時可）｜📐進捗 上振れ 10.1%
  > 【業態】総合超硬工具で大手。独自技術の自動車用切削工具に強み。海外に注力。
  > 【いま】終値1,760円・直近5日+0.74%（材料未確認）
  > 【調子】🚀確変（11/13） — 進捗モデル値域外
  > 【水準】💎割安（6.0/7）— PER4.02倍・PEG0.034・52週67.2% ／ 💰単元17.6万円
  > 【戦略】当日終値1760円の指値で反転を取りにいく。SL1532円（直近5日安値）
- 6862 ミナト HD｜granville_rebound｜🚀確変｜💎割安｜PASS｜3,360円｜💰33.6万円｜reversal 3360/SL2326（✅即時可）｜🚨決算直前 11/12(残1営業日) ⚠1単元でリスク枠超過（103400円）
  > 【業態】産業用メモリ、デバイスプログラム、ROM書込移植装置が主力。M&Aで業容拡大。
  > 【いま】終値3,360円・直近5日+7.52%（材料未確認）
  > 【調子】🚀確変（11/13） — E軸判定不能(進捗データ不足)
  > 【水準】💎割安（6.0/7）— PER4.17倍・PEG0.0321・52週49.8% ／ 💰単元33.6万円
  > 【戦略】当日終値3360円の指値で反転を取りにいく。SL2326円（直近5日安値）／⚠1単元リスク103400円（枠超過）
- 6769 Thine Electronics, Inc.｜granville_rebound｜🚀確変｜⚪妥当｜PASS｜953円｜💰9.5万円｜⛔提案なし(指名鮮度切れ 18営業日)｜⚠日程不明 📐進捗 上振れ 12.5%
  > 【業態】ファブレス半導体企業。特定用途向け標準品を開発。顔認証・体温検知など。
  > 【いま】終値953円・直近5日-0.21%（材料未確認）
  > 【調子】🚀確変（11/13） — 黒字転換
  > 【水準】⚪妥当（4.0/7）— PER94.36倍・PEG0.7792・52週27.3% ／ 💰単元9.5万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 18営業日)）
- 479A PRONI Inc.｜granville_rebound/changepoint｜🔥絶好調｜💎割安｜FAIL_UWAHIGE｜1,551円｜💰15.4万円｜—
- 5381 Mipox Corp.｜granville_rebound｜🔥絶好調｜💎割安｜FAIL_UWAHIGE｜882円｜💰7.4万円｜—
- 3691 DIGITAL PLUS, Inc.｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜1,324円｜💰13.2万円｜—｜⚡材料後出し
- 4968 Arakawa Chemical Industries,Ltd.｜granville_rebound｜🔥絶好調｜🟢値頃｜PASS｜1,969円｜💰19.7万円｜reversal 1969/SL1580（✅即時可）｜📑TOPIX低減対象（次 01/29 第2回/8） 📐進捗 上振れ 78.5% ⚠1単元でリスク枠超過（38900円）
  > 【業態】化学（ファインケミカル・接着剤・製紙関連）
  > 【いま】終値1,969円・直近5日+0.20%（材料未確認）
  > 【調子】🔥絶好調（10/13）
  > 【水準】🟢値頃（5.0/7）— PER12.21倍・PEG0.1706・52週56% ／ 💰単元19.7万円
  > 【戦略】当日終値1969円の指値で反転を取りにいく。SL1580円（直近5日安値）／⚠1単元リスク38900円（枠超過）
- 2962 テクニスコ｜granville_rebound｜🔥絶好調｜⚪妥当｜PASS｜1,607円｜💰16.1万円｜reversal 1607/SL1206（✅即時可）｜⏰決算 11/13(残2営業日) ⚠1単元でリスク枠超過（40100円）
  > 【業態】ヒートシンク製品やガラス製品など精密加工部品の製造・販売。センサー、医療用も。
  > 【いま】終値1,607円・直近5日-4.80%（材料未確認）
  > 【調子】🔥絶好調（10/13） — E軸判定不能(期首・進捗なし)
  > 【水準】⚪妥当（4.0/7）— PER73.72倍・PEG0.0649・52週44.9% ／ 💰単元16.1万円
  > 【戦略】当日終値1607円の指値で反転を取りにいく。SL1206円（直近5日安値）／⚠1単元リスク40100円（枠超過）
- 4419 Finatext Holdings Ltd.｜granville_rebound/changepoint｜🔥絶好調｜⚪妥当｜PASS｜1,237円｜💰12.4万円｜reversal 1237/SL1123（✅即時可）｜🚨決算直前 11/12(残1営業日)
  > 【業態】証券・保険ビジネス向けクラウド基幹システムの提供。人材育成やビッグデータ解析も。
  > 【いま】終値1,237円・直近5日-3.28%（材料未確認）
  > 【調子】🔥絶好調（10/13） — E軸判定不能(進捗データ不足)
  > 【水準】⚪妥当（4.0/7）— PER27.67倍・PEG0.3571・52週48.6% ／ 💰単元12.4万円
  > 【戦略】当日終値1237円の指値で反転を取りにいく。SL1123円（直近5日安値）
- 1436 GreenEnergy & Company｜granville_rebound｜🔥絶好調｜💎割安｜FAIL_UWAHIGE｜1,415円｜💰13.7万円｜—
- 2489 アドウェイズ｜granville_rebound｜⚠減速｜🟢値頃｜PASS｜334円｜💰3.3万円｜reversal 334/SL308（✅即時可）｜⚠日程不明 ⚠業績基調が下向き（⚠減速） ⚠バリュートラップ疑い 📑TOPIX低減対象（次 01/29 第2回/8） 📐進捗 上振れ 93.0%
  > 【業態】PC・スマホ向けアフィリエイト広告で国内大手。広告自動配信ツール「UNICORN」が拡大。
  > 【いま】終値334円・直近5日+5.36%（材料未確認）
  > 【調子】⚠減速（9/13） — 減収上限
  > 【水準】🟢値頃（5.0/7）— PER14.52倍・PEG0.0771・52週43.5% ／ 💰単元3.3万円
  > 【戦略】当日終値334円の指値で反転を取りにいく。SL308円（直近5日安値）
- 3793 Drecom Co., Ltd.｜granville_rebound｜⚠減速｜🟢値頃｜PASS｜457円｜💰4.6万円｜reversal 457/SL398（✅即時可）｜⚠日程不明 ⚠業績基調が下向き（⚠減速） ⚠バリュートラップ疑い 📐進捗 上振れ 25.6%
  > 【業態】スマホゲーム開発・運用を軸にアニメ等他社配信。ITサービスから出版・映像事業も。
  > 【いま】終値457円・直近5日+2.93%（材料未確認）
  > 【調子】⚠減速（9/13） — 上方修正済み
  > 【水準】🟢値頃（5.0/7）— PER14.37倍・PEG0.0549・52週41.1% ／ 💰単元4.6万円
  > 【戦略】当日終値457円の指値で反転を取りにいく。SL398円（直近5日安値）
- 6963 ROHM Company Limited｜granville_rebound｜🔥絶好調｜🟢値頃｜PASS｜3,170円｜💰31.7万円｜⛔提案なし(指名鮮度切れ 18営業日)｜⚠日程不明 📐進捗 遅れ -54.4%
  > 【業態】カスタムLSIで首位。半導体素子、抵抗器などに強み。SiCパワー半導体が拡大。
  > 【いま】終値3,170円・直近5日-8.25%（材料未確認）
  > 【調子】🔥絶好調（9/13） — 上方修正済み
  > 【水準】🟢値頃（5.0/7）— PER27.19倍・PEG0.1547・52週29.4% ／ 💰単元31.7万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 18営業日)）
- 8995 Makoto Construction Co,Ltd｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜1,406円｜💰14.1万円｜—
- 150A ＪＳＨ｜granville_rebound｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜632円｜💰6.2万円｜—
- 6317 Kitagawa Corporation｜granville_rebound｜🔥絶好調｜💎割安｜PASS｜2,293円｜💰22.9万円｜reversal 2293/SL2069（✅即時可）｜⏰決算 11/13(残2営業日) 📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】コンクリートプラント、鋳造部品、工作機械・器具、産業機械等を展開。海外にも拠点。
  > 【いま】終値2,293円・直近5日+0.57%（材料未確認）
  > 【調子】🔥絶好調（8/13） — D軸簡易判定(四半期詳細未取得のため中立値)
  > 【水準】💎割安（6.0/7）— PER6.38倍・PEG0.079・52週67.6% ／ 💰単元22.9万円
  > 【戦略】当日終値2293円の指値で反転を取りにいく。SL2069円（直近5日安値）
- 7715 長野計器｜granville_rebound｜🔥絶好調｜🟢値頃｜PASS｜3,545円｜💰35.5万円｜⛔提案なし(指名鮮度切れ 11営業日)｜🚨決算直前 11/12(残1営業日) 📑TOPIX低減対象（次 01/29 第2回/8） 📐進捗 上振れ 10.5%
  > 【業態】圧力計・圧力センサー大手。機械式圧力計で世界シェア首位。車載向け主力。
  > 【いま】終値3,545円・直近5日-1.25%（材料未確認）
  > 【調子】🔥絶好調（8/13） — E軸:進捗21.0%>=前年同期19.0%
  > 【水準】🟢値頃（5.0/7）— PER9.27倍・PEG0.1906・52週50% ／ 💰単元35.5万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 11営業日)）
- 8364 清水銀行｜granville_rebound｜🔥絶好調｜🟢値頃｜PASS｜2,812円｜💰28.1万円｜reversal 2812/SL2436（✅即時可）｜⏰決算 11/13(残2営業日) 📑TOPIX低減対象（次 01/29 第2回/8） ⚠1単元でリスク枠超過（37600円）
  > 【業態】静岡地盤の地銀中下位行。地元中小企業向け中心。SBIHDと資本業務提携。
  > 【いま】終値2,812円・直近5日+2.82%（材料未確認）
  > 【調子】🔥絶好調（8/13） — E軸判定不能(進捗データ不足)
  > 【水準】🟢値頃（5.0/7）— PER10.99倍・PEG0.22・52週60% ／ 💰単元28.1万円
  > 【戦略】当日終値2812円の指値で反転を取りにいく。SL2436円（直近5日安値）／⚠1単元リスク37600円（枠超過）
- 460A ＢＲＡＮＵ｜granville_rebound｜🔥絶好調｜⚪妥当｜PASS｜1,098円｜💰11.0万円｜reversal 1098/SL949（✅即時可）｜📐進捗 上振れ 10.8%
  > 【業態】中小建設事業者に特化した各種ITサービス提供。建設マッチング、統合型ツール等。
  > 【いま】終値1,098円・直近5日+5.98%・📌建設業界の新たな共創エコシステム構築に向け「CAREECON Plus販売パートナープログラム」を開始
  > 【調子】🔥絶好調（8/13）
  > 【水準】⚪妥当（4.0/7）— PER16.97倍・PEG0.4489・52週45.9% ／ 💰単元11.0万円
  > 【戦略】当日終値1098円の指値で反転を取りにいく。SL949円（直近5日安値）
- 6508 Meidensha Corporation｜granville_rebound｜⚡好調｜💎割安｜PASS｜7,616円｜💰76.2万円｜reversal 7616/SL6374（✅即時可）｜⚠日程不明 ⚠1単元でリスク枠超過（124200円）
  > 【業態】住友系・老舗重電。電力・エネルギー、水処理制御システム、電鉄用、車電動化に強み。
  > 【いま】終値7,616円・直近5日-8.62%（材料未確認）
  > 【調子】⚡好調（7/13） — 上方修正済み
  > 【水準】💎割安（6.0/7）— PER13.29倍・PEG0.5211・52週30.2% ／ 💰単元76.2万円
  > 【戦略】当日終値7616円の指値で反転を取りにいく。SL6374円（直近5日安値）／⚠1単元リスク124200円（枠超過）
- 5367 Nikkato Corporation｜granville_rebound｜⚡好調｜🟢値頃｜PASS｜1,076円｜💰10.8万円｜reversal 1076/SL850（✅即時可）｜📐進捗 上振れ 52.0%
  > 【業態】工業用セラミックス中堅。耐摩耗・耐熱など高付加価値品に強み。エンジニアリングも。
  > 【いま】終値1,076円・直近5日+0.00%（材料未確認）
  > 【調子】⚡好調（7/13）
  > 【水準】🟢値頃（5.0/7）— PER14.31倍・PEG1.1387・52週32.8% ／ 💰単元10.8万円
  > 【戦略】当日終値1076円の指値で反転を取りにいく。SL850円（直近5日安値）
- 6490 ＰＩＬＬＡＲ｜granville_rebound｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜9,550円｜💰93.8万円｜—
- 5252 日本ナレッジ｜granville_rebound｜⚡好調｜🟡やや割高｜PASS｜935円｜💰9.3万円｜⛔提案なし(材料後出し)｜⚡材料後出し ⏰決算 11/13(残2営業日)
  > 【業態】ソフトウェアのテスト・品質検証サービスのほかシステム受託開発。業務系システムに強み。
  > 【いま】終値935円・直近5日-0.11%・📌生成AIソフトウェア開発支援環境『digitest Local LLM Ver.1.0』の提供開始
  > 【調子】⚡好調（7/13） — E軸判定不能(進捗データ不足)
  > 【水準】🟡やや割高（2.0/7）— PER46.06倍・PEG2.033・52週57.6% ／ 💰単元9.3万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 9697 カプコン｜granville_rebound｜⚡好調｜🔴過熱｜FAIL_UWAHIGE｜4,389円｜💰44.1万円｜—
- 477A Startline CO.,LTD.｜granville_rebound｜⚡好調｜💎割安｜FAIL_UWAHIGE｜614円｜💰6.1万円｜—｜⚡材料後出し
- 4667 Aisan Technology Co.,Ltd.｜granville_rebound｜⚡好調｜💎割安｜PASS_DOJI｜810円｜💰8.1万円｜⛔提案なし(材料後出し)｜⚡材料後出し 📉決算反応日 11/12
  > 【業態】測量・土木ソフトが主力。高精度3次元計測システムに強み。自動運転実験に参加。
  > 【いま】終値810円・直近5日-9.70%・📊2027年3月期第2四半期（中間期）決算短信〔日本基準〕（連結）
  > 【調子】⚡好調（6/13） — E軸判定不能(進捗データ不足)
  > 【水準】💎割安（6.0/7）— PER7.82倍・PEG0.8623・52週36.7% ／ 💰単元8.1万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 3850 INTRAMART CORPORATION｜granville_rebound｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜3,340円｜💰33.6万円｜—
- 6947 図研｜granville_rebound｜⚡好調｜⚪妥当｜FAIL_INSEN｜5,080円｜💰50.8万円｜—
- 6958 日本シイエムケイ｜granville_rebound｜⚡好調｜⚪妥当｜PASS｜747円｜💰7.5万円｜reversal 747/SL604（✅即時可）｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8） 📐進捗 遅れ -42.9%
  > 【業態】プリント配線板の最大手。自動車、電機向けが主力。高付加価値品強化。
  > 【いま】終値747円・直近5日+5.81%（材料未確認）
  > 【調子】⚡好調（6/13）
  > 【水準】⚪妥当（3.0/7）— PER17.74倍・PEG1.3012・52週74.3% ／ 💰単元7.5万円
  > 【戦略】当日終値747円の指値で反転を取りにいく。SL604円（直近5日安値）
- 4100 Toda Kogyo Corp.｜granville_rebound｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜1,811円｜💰17.6万円｜—｜⚡材料後出し
- 8344 Yamagata Bank, Ltd.｜granville_rebound｜⚡好調｜🟢値頃｜PASS｜4,410円｜💰44.1万円｜reversal 4410/SL3730（✅即時可）｜⏰決算 11/13(残2営業日) ⚠1単元でリスク枠超過（68000円）
  > 【業態】山形地盤の地銀中堅。県内シェア首位。県指定金融機関で自治体取引に強み。
  > 【いま】終値4,410円・直近5日+0.57%（材料未確認）
  > 【調子】⚡好調（5/13） — E軸判定不能(進捗データ不足)
  > 【水準】🟢値頃（5.6/7）— PER18.18倍・PEG0.5384・52週63.4% ／ 💰単元44.1万円
  > 【戦略】当日終値4410円の指値で反転を取りにいく。SL3730円（直近5日安値）／⚠1単元リスク68000円（枠超過）
- 6742 京三製作所｜granville_rebound｜⚠減速｜⚪妥当｜PASS｜975円｜💰9.8万円｜reversal 975/SL840（✅即時可）｜⏰決算 11/13(残2営業日) ⚠業績基調が下向き（⚠減速） 📑TOPIX低減対象（次 01/29 第2回/8） 📐進捗 上振れ 24.3%
  > 【業態】信号大手3社の一角。鉄道、道路用信号と産業用電源装置が柱。海外も。
  > 【いま】終値975円・直近5日-3.27%（材料未確認）
  > 【調子】⚠減速（5/13） — E軸判定不能(進捗データ不足)
  > 【水準】⚪妥当（4.0/7）— PER14.32倍・PEG0.9347・52週62.8% ／ 💰単元9.8万円
  > 【戦略】当日終値975円の指値で反転を取りにいく。SL840円（直近5日安値）
- 5574 ABEJA,Inc.｜granville_rebound/changepoint｜⚡好調｜🟡やや割高｜PASS｜2,041円｜💰20.4万円｜reversal 2041/SL1757（✅即時可）｜⚠日程不明
  > 【業態】企業のDXを支援。AIによるデジタルプラットフォーム事業の運営を手掛ける。
  > 【いま】終値2,041円・直近5日-0.83%（材料未確認）
  > 【調子】⚡好調（5/13） — E軸判定不能(期首・進捗なし)
  > 【水準】🟡やや割高（2.0/7）— PER30.65倍・PEG232.6005・52週16.5% ／ 💰単元20.4万円
  > 【戦略】当日終値2041円の指値で反転を取りにいく。SL1757円（直近5日安値）
- 7256 河西工業｜granville_rebound｜⚡好調｜🔴過熱｜FAIL_UWAHIGE｜412円｜💰—万円｜—
- 9278 BOOKOFF GROUP HOLDINGS LIMITED｜granville_rebound｜⚡好調｜🔴過熱｜FAIL_INSEN｜2,609円｜💰26.2万円｜—
- 4025 多木化学｜granville_rebound｜✅順調｜⚪妥当｜PASS｜5,360円｜💰53.6万円｜reversal 5360/SL4910（✅即時可）｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8） 📐進捗 上振れ 31.9% ⚠1単元でリスク枠超過（45000円）
  > 【業態】人造肥料の草分けで化学肥料大手。水処理薬、機能性素材や商業施設も。
  > 【いま】終値5,360円・直近5日+0.00%（材料未確認）
  > 【調子】✅順調（4/13） — 上方修正済み
  > 【水準】⚪妥当（3.0/7）— PER12.78倍・PEG1.51・52週64.8% ／ 💰単元53.6万円
  > 【戦略】当日終値5360円の指値で反転を取りにいく。SL4910円（直近5日安値）／⚠1単元リスク45000円（枠超過）
- 428A Cypress Holdings Co., Ltd.｜granville_rebound｜✅順調｜🔴過熱｜FAIL_INSEN｜1,458円｜💰17.8万円｜—｜⚡材料後出し
- 278A Ｔｅｒｒａ　Ｄｒｏｎｅ｜granville_rebound｜✅順調｜⏸判定不能｜PASS｜5,560円｜💰—万円｜⛔提案なし(指名鮮度切れ 11営業日)
  > 【業態】測量・点検・農業におけるドローンを含むハード・ソフトの開発などを手掛ける。
  > 【いま】終値5,560円・直近5日-1.77%（材料未確認）
  > 【調子】✅順調（4/13） — 赤字ルート
  > 【水準】⏸判定不能（—/7）— PER—倍・PEG—・52週42.6% ／ 💰単元—万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 11営業日)）
- 4440 WITZ Corp.｜granville_rebound｜➖横ばい｜⚪妥当｜PASS｜1,689円｜💰16.9万円｜⛔提案なし(指名鮮度切れ 17営業日)｜⚠日程不明
  > 【業態】自動車や工作機械に組込むソフトウェアの開発・販売。アイシン、オークマが出資。
  > 【いま】終値1,689円・直近5日-0.94%（材料未確認）
  > 【調子】➖横ばい（2/13） — E軸判定不能(進捗データ不足)
  > 【水準】⚪妥当（3.0/7）— PER15.01倍・PEG10.5093・52週33.3% ／ 💰単元16.9万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 17営業日)）
- 3687 Fixstars Corp.｜granville_rebound｜➖横ばい｜🟡やや割高｜PASS｜1,700円｜💰17.0万円｜⛔提案なし(指名鮮度切れ 18営業日)｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】システムを高速化させるソフト開発会社。AI、量子分野や関連ハードウエア販売も。
  > 【いま】終値1,700円・直近5日+0.41%（材料未確認）
  > 【調子】➖横ばい（2/13） — E軸判定不能(期首・進捗なし)
  > 【水準】🟡やや割高（2.0/7）— PER24.96倍・PEG3.5625・52週20.5% ／ 💰単元17.0万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 18営業日)）
- 6676 BUFFALO INC.｜granville_rebound｜⚠減速｜⚪妥当｜FAIL_UWAHIGE｜3,215円｜💰31.8万円｜—
- 6203 Howa Machinery, Ltd.｜granville_rebound｜⚠減速｜🟡やや割高｜PASS｜2,022円｜💰20.2万円｜⛔提案なし(指名鮮度切れ 16営業日)｜⏰決算 11/13(残2営業日) ⚠業績基調が下向き（⚠減速）
  > 【業態】産業用機械の老舗。工作機械中心に特装車や防弾、火器など防衛機器も。
  > 【いま】終値2,022円・直近5日-2.93%（材料未確認）
  > 【調子】⚠減速（1/13） — 経常成長率+14.3%
  > 【水準】🟡やや割高（2.0/7）— PER22.49倍・PEG1.5699・52週47.6% ／ 💰単元20.2万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 16営業日)）
- 8360 Yamanashi Chuo Bank, Ltd.｜granville_rebound｜取得不可｜💎割安｜PASS｜1,286円｜💰12.9万円｜⛔提案なし(指名鮮度切れ 12営業日)｜⏰決算 11/13(残2営業日)
  > 【業態】未取得（次回以降に取得）
  > 【いま】終値1,286円・直近5日+2.55%（材料未確認）
  > 【調子】取得不可（—/13） — データ取得不可
  > 【水準】💎割安（6.0/7）— PER3.16倍・PEG0.0978・52週66.5% ／ 💰単元12.9万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 12営業日)）
- 8377 ほくほくフィナンシャルグループ｜granville_rebound｜業績データ取得不可(売上/経常欠損)｜💎割安｜PASS｜775円｜💰7.7万円｜⛔提案なし(指名鮮度切れ 12営業日)｜⚡材料後出し ⚠日程不明
  > 【業態】傘下に北陸銀と北海道銀持つ金融持ち株会社。横浜銀とシステム提携。
  > 【いま】終値775円・直近5日+3.53%・📌(Correction) Partial Correction to “Consolidated Financial Results for the Six Months Ended September 30, 2026 (Under Japanese GAAP)”
  > 【調子】業績データ取得不可(売上/経常欠損)（—/13） — 業績データ取得不可(売上/経常欠損)
  > 【水準】💎割安（6.0/7）— PER12.3倍・PEG0.3579・52週69.7% ／ 💰単元7.7万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 12営業日)）
- 7380 Juroku Financial Group,Inc.｜granville_rebound｜業績データ取得不可(売上/経常欠損)｜⚪妥当｜PASS｜2,333円｜💰23.3万円｜⛔提案なし(指名鮮度切れ 14営業日)｜⚠日程不明
  > 【業態】岐阜県内最大手の地銀、十六銀行が中核の総合金融サービス。愛知へ拡大。
  > 【いま】終値2,333円・直近5日+1.02%（材料未確認）
  > 【調子】業績データ取得不可(売上/経常欠損)（—/13） — 業績データ取得不可(売上/経常欠損)
  > 【水準】⚪妥当（3.0/7）— PER13.77倍・PEG4.7729・52週66.1% ／ 💰単元23.3万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 14営業日)）
- 8368 Hyakugo Bank, Ltd.｜granville_rebound｜業績データ取得不可(売上/経常欠損)｜⚪妥当｜PASS｜2,136円｜💰21.4万円｜reversal 2136/SL1822（✅即時可）｜⚠日程不明 ⚠1単元でリスク枠超過（31400円）
  > 【業態】三重地盤の地銀上位。県内で圧倒的。三菱UFJ、十六銀、名古屋銀と親密。
  > 【いま】終値2,136円・直近5日+4.17%（材料未確認）
  > 【調子】業績データ取得不可(売上/経常欠損)（—/13） — 業績データ取得不可(売上/経常欠損)
  > 【水準】⚪妥当（3.0/7）— PER16.64倍・PEG0.814・52週66.1% ／ 💰単元21.4万円
  > 【戦略】当日終値2136円の指値で反転を取りにいく。SL1822円（直近5日安値）／⚠1単元リスク31400円（枠超過）
- 7184 富山第一銀行｜granville_rebound｜取得不可｜🟡やや割高｜PASS｜3,200円｜💰32.0万円｜reversal 3200/SL2765（✅即時可）｜⚠日程不明 ⚠1単元でリスク枠超過（43500円）
  > 【業態】富山県の第2地銀。中小企業が中心。新潟、石川、岐阜にも展開。財務良好。
  > 【いま】終値3,200円・直近5日+2.07%（材料未確認）
  > 【調子】取得不可（—/13） — 売上高(経常収益代用含む)データ取得不可
  > 【水準】🟡やや割高（2.0/7）— PER14.98倍・PEG—・52週72.8% ／ 💰単元32.0万円
  > 【戦略】当日終値3200円の指値で反転を取りにいく。SL2765円（直近5日安値）／⚠1単元リスク43500円（枠超過）
- 8713 Fidea Holdings Co.Ltd.｜granville_rebound｜業績データ取得不可(売上/経常欠損)｜🔴過熱｜PASS｜2,559円｜💰25.6万円｜⛔提案なし(指名鮮度切れ 14営業日)｜⏰決算 11/13(残2営業日) 📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】荘内銀、北都銀が県を超えて統合。山形・秋田が地盤。27年1月両行合併へ。
  > 【いま】終値2,559円・直近5日+3.65%（材料未確認）
  > 【調子】業績データ取得不可(売上/経常欠損)（—/13） — 業績データ取得不可(売上/経常欠損)
  > 【水準】🔴過熱（1.4/7）— PER14.38倍・PEG—・52週71.2% ／ 💰単元25.6万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 14営業日)）
- 3371 ソフトクリエイトホールディングス｜granville_rebound｜—｜－未評価（次回①-9で算定）｜PASS｜2,047円｜💰20.5万円｜reversal 2047/SL1914（✅即時可）｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】ITソリューション、ECサイト構築パッケージが主力。IT、EC関連のクラウド、ソリューション事業注力。
  > 【いま】終値2,047円・直近5日+2.30%・📌Notice Regarding Completion of Off-Floor Distribution of Shares
  > 【調子】—（—/13）
  > 【水準】－未評価（次回①-9で算定）（—/7）— PER—倍・PEG—・52週62.2% ／ 💰単元20.5万円
  > 【戦略】当日終値2047円の指値で反転を取りにいく。SL1914円（直近5日安値）
- 4075 ブレインズテクノロジー｜granville_rebound｜取得不可｜⏸判定不能｜FAIL_UWAHIGE｜1,092円｜💰10.4万円｜—
- 4396 System Support Holdings Inc.｜granville_rebound｜—｜—｜FAIL_INSEN｜1,305円｜💰—万円｜—
- 6840 ＡＫＩＢＡホールディングス｜granville_rebound｜業績データ取得不可｜⏸判定不能｜PASS｜641円｜💰6.4万円｜reversal 641/SL521（✅即時可）｜⏰決算 11/13(残2営業日)
  > 【業態】増設メモリ、用途別モジュール、フラッシュメモリが主力。通信コンサル、通信工事が拡大。
  > 【いま】終値641円・直近5日-1.38%（材料未確認）
  > 【調子】業績データ取得不可（—/13） — 通期予想なし
  > 【水準】⏸判定不能（—/7）— PER—倍・PEG—・52週29% ／ 💰単元6.4万円
  > 【戦略】当日終値641円の指値で反転を取りにいく。SL521円（直近5日安値）
- 6890 Ferrotec Corporation｜granville_rebound｜業績データ取得不可｜⏸判定不能｜PASS｜7,617円｜💰76.2万円｜reversal 7617/SL5701（✅即時可）｜⏰決算 11/16(残3営業日) 📑TOPIX新規採用（2026-10-30 組入） ⚠1単元でリスク枠超過（191600円）
  > 【業態】半導体製造装置部品会社。真空シールで世界高シェア。磁性流体技術も。
  > 【いま】終値7,617円・直近5日-4.20%（材料未確認）
  > 【調子】業績データ取得不可（—/13） — kabutan年次表を解析できず
  > 【水準】⏸判定不能（—/7）— PER—倍・PEG—・52週40.1% ／ 💰単元76.2万円
  > 【戦略】当日終値7617円の指値で反転を取りにいく。SL5701円（直近5日安値）／⚠1単元リスク191600円（枠超過）
- 7175 Imamura Securities Co.Ltd.｜granville_rebound｜業績データ取得不可｜⏸判定不能｜FAIL_UWAHIGE｜1,608円｜💰16.1万円｜—
- 7213 LECIP Holdings Corporation｜granville_rebound｜—｜—｜FAIL_INSEN｜570円｜💰—万円｜—
- 7826 フルヤ金属｜granville_rebound｜—｜－未評価（次回①-9で算定）｜PASS｜9,050円｜💰90.5万円｜reversal 9050/SL6970（✅即時可）｜⚠日程不明 ⚠1単元でリスク枠超過（208000円）
  > 【業態】白金・レアメタルなど貴金属の製造・加工・回収。精製・改鋳、薄膜技術に強み。
  > 【いま】終値9,050円・直近5日+0.22%（材料未確認）
  > 【調子】—（—/13）
  > 【水準】－未評価（次回①-9で算定）（—/7）— PER—倍・PEG—・52週64.6% ／ 💰単元90.5万円
  > 【戦略】当日終値9050円の指値で反転を取りにいく。SL6970円（直近5日安値）／⚠1単元リスク208000円（枠超過）
- 8551 北日本銀行｜granville_rebound｜—｜－未評価（次回①-9で算定）｜PASS｜2,373円｜💰23.7万円｜reversal 2373/SL2018（✅即時可）｜🚨決算直前 11/12(残1営業日) 📑TOPIX低減対象（次 01/29 第2回/8） ⚠1単元でリスク枠超過（35500円）
  > 【業態】東北太平洋側地盤の地銀中位。岩手中心。サービス業取引に強み。個人にシフト。
  > 【いま】終値2,373円・直近5日+3.81%（材料未確認）
  > 【調子】—（—/13）
  > 【水準】－未評価（次回①-9で算定）（—/7）— PER—倍・PEG—・52週60.8% ／ 💰単元23.7万円
  > 【戦略】当日終値2373円の指値で反転を取りにいく。SL2018円（直近5日安値）／⚠1単元リスク35500円（枠超過）
- 8609 岡三証券グループ｜granville_rebound｜業績データ取得不可｜⏸判定不能｜PASS｜1,048円｜💰10.5万円｜reversal 1048/SL925（✅即時可）｜⚠日程不明
  > 【業態】三重地盤の証券準大手。リテールに強み。傘下で証券ジャパンや投信運用会社。
  > 【いま】終値1,048円・直近5日+6.29%（材料未確認）
  > 【調子】業績データ取得不可（—/13） — 通期予想なし
  > 【水準】⏸判定不能（—/7）— PER—倍・PEG—・52週61.2% ／ 💰単元10.5万円
  > 【戦略】当日終値1048円の指値で反転を取りにいく。SL925円（直近5日安値）
- 8739 スパークス・グループ｜granville_rebound｜業績データ取得不可｜⏸判定不能｜PASS｜2,435円｜💰24.4万円｜⛔提案なし(指名鮮度切れ 11営業日)｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】独立系投資顧問。中小型株に定評。韓国、香港で資産運用子会社。運用多角。
  > 【いま】終値2,435円・直近5日+4.37%（材料未確認）
  > 【調子】業績データ取得不可（—/13） — 通期予想なし
  > 【水準】⏸判定不能（—/7）— PER—倍・PEG—・52週78.5% ／ 💰単元24.4万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 11営業日)）

## 変化点銘柄
- 265A エイチエムコム｜changepoint｜🚀確変｜🟢値頃｜PASS｜686円｜💰6.9万円｜⛔提案なし(材料後出し)｜🔒実弾封印中(PL3紙ログ収集中) ⚡材料後出し ⏰決算 11/13(残2営業日)
  > 【業態】音声認識処理、自然言語解析処理を用いたプロダクト提供。AI自動応答も。
  > 【いま】終値686円・直近5日+3.63%・📌株式会社エンヴァリスによる当社アナリスト・レポート公開のお知らせ
  > 【調子】🚀確変（12/13） — 開示由来上方修正
  > 【水準】🟢値頃（5.0/7）— PER89.09倍・PEG0.5696・52週14.5% ／ 💰単元6.9万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 4011 Headwaters Co.,Ltd｜changepoint｜🚀確変｜🟢値頃｜FAIL_INSEN｜1,907円｜💰19.3万円｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 9888 UEX LTD｜changepoint｜🚀確変｜🟢値頃｜FAIL_INSEN｜1,487円｜💰15.1万円｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 9308 乾汽船｜changepoint｜🚀確変｜⚪妥当｜FAIL_UWAHIGE｜2,388円｜💰22.0万円｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 7695 交換できるくん｜changepoint｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜830円｜💰8.3万円｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 6136 OSG CORP｜changepoint｜🔥絶好調｜🟢値頃｜PASS｜3,550円｜💰35.5万円｜⛔提案なし(指名鮮度切れ 19営業日)｜🔒実弾封印中(PL3紙ログ収集中) ⚠日程不明
  > 【業態】タップ・エンドミルなど高シェアの精密切削工具大手。製販一貫体制。海外に注力。
  > 【いま】終値3,550円・直近5日+1.37%（材料未確認）
  > 【調子】🔥絶好調（9/13） — E軸判定不能(進捗データ不足)
  > 【水準】🟢値頃（5.0/7）— PER12.15倍・PEG0.1736・52週66.9% ／ 💰単元35.5万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 19営業日)）
- 8151 東陽テクニカ｜changepoint｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜1,745円｜💰16.7万円｜—｜🔒実弾封印中(PL3紙ログ収集中) ⚡材料後出し
- 7318 セレンディップ・ホールディングス｜changepoint｜🔥絶好調｜💎割安｜PASS｜1,134円｜💰11.3万円｜⛔提案なし(指名鮮度切れ 13営業日)｜🔒実弾封印中(PL3紙ログ収集中) ⚡材料後出し ⏰決算 11/13(残2営業日)
  > 【業態】中小企業をM&Aによる事業承継や再生コンサル。傘下の車部品、FA機の比重大。
  > 【いま】終値1,134円・直近5日+4.71%・📌PMIの実践を紹介、三井屋工業・エクセルは2027年4月にSerenACへ統合予定
  > 【調子】🔥絶好調（8/13） — E軸判定不能(進捗データ不足)
  > 【水準】💎割安（6.0/7）— PER9.38倍・PEG0.2571・52週11.2% ／ 💰単元11.3万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 13営業日)）
- 5582 （名称取得不可）｜changepoint｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1,762円｜💰17.9万円｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 4443 Ｓａｎｓａｎ｜changepoint｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜2,320円｜💰22.9万円｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 478A Hutzper Inc.｜changepoint｜⚡好調｜⚪妥当｜FAIL_INSEN｜660円｜💰6.7万円｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 9343 アイビス｜changepoint｜⚡好調｜⚪妥当｜FAIL_INSEN｜721円｜💰7.3万円｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 4475 None｜changepoint｜⚡好調｜🔴過熱｜FAIL_INSEN｜2,585円｜💰26.7万円｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 286A ユカリア｜changepoint｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜761円｜💰7.5万円｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 218A Liberaware｜changepoint｜⚡好調｜⚪妥当｜PASS｜830円｜💰8.3万円｜changepoint 830/SL695（✅即時可）｜🔒実弾封印中(PL3紙ログ収集中)
  > 【業態】産業分野に特化した非GPS型小型ドローンの開発・運用。屋内・狭空間に強み。
  > 【いま】終値830円・直近5日+5.20%（材料未確認）
  > 【調子】⚡好調（5/13） — Cp軸は通期営業損益トレンドで代替(四半期premium限定)
  > 【水準】⚪妥当（4.2/7）— PER—倍・PEG—・52週12.1% ／ 💰単元8.3万円
  > 【戦略】発火日終値830円の指値。追撃禁止・SL695円。🔒実弾封印中（PL3紙ログ収集中）
- 4483 JMDC｜changepoint｜⚡好調｜🔴過熱｜FAIL_UWAHIGE｜3,975円｜💰36.5万円｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 4165 PLAID Inc.｜changepoint｜🔻悪化｜🔴過熱｜FAIL_INSEN｜738円｜💰7.6万円｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 4071 Plus Alpha Consulting Co. LTD.｜changepoint｜✅順調｜⚪妥当｜FAIL_UWAHIGE｜2,315円｜💰23.2万円｜—｜🔒実弾封印中(PL3紙ログ収集中) ⚡材料後出し
- 598A チャットプラス｜changepoint｜✅順調｜⚪妥当｜FAIL_UWAHIGE｜1,080円｜💰10.8万円｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 6785 鈴木｜changepoint｜✅順調｜🟡やや割高｜FAIL_INSEN｜3,050円｜💰30.1万円｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 339A PROGRESS TECHNOLOGIES GROUP INC｜changepoint｜➖横ばい｜⚪妥当｜FAIL_INSEN｜752円｜💰7.5万円｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 4488 AI inside Inc.｜changepoint｜➖横ばい｜🟡やや割高｜FAIL_UWAHIGE｜1,808円｜💰16.9万円｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 4259 ExaWizards Inc.｜changepoint｜業績データ取得不可｜🟢値頃｜FAIL_UWAHIGE｜723円｜💰7.1万円｜—｜🔒実弾封印中(PL3紙ログ収集中) ⚡材料後出し
- 3923 ラクス｜changepoint｜判定保留(変則決算)｜🟡やや割高｜FAIL_UWAHIGE｜1,144円｜💰11.6万円｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 4478 freee K.K.｜changepoint｜業績データ取得不可｜🔴過熱｜FAIL_UWAHIGE｜4,820円｜💰47.5万円｜—｜🔒実弾封印中(PL3紙ログ収集中) ⚡材料後出し
- 593A Tier IV, Inc.｜changepoint｜取得不可｜🔴過熱｜PASS｜2,205円｜💰22.1万円｜⛔提案なし(材料後出し)｜🔒実弾封印中(PL3紙ログ収集中) ⚡材料後出し ⏰決算 11/13(残2営業日) 📑TOPIX新規採用（2026-10-30 組入）
  > 【業態】自動運転ソフトウェア「Autoware」を活用した自動運転車両の開発を手掛ける。
  > 【いま】終値2,205円・直近5日-17.42%・📌ドイツ ミュンヘン市内における「Autoware」を活用した大型路線バス向け 自動運転システムの開発支援に関するお知らせ
  > 【調子】取得不可（—/13） — 業績データ取得不可(前期比行なし)
  > 【水準】🔴過熱（1.4/7）— PER—倍・PEG—・52週45.7% ／ 💰単元22.1万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 3989 シェアテク｜changepoint｜業績データ取得不可｜🔴過熱｜FAIL_INSEN｜1,533円｜💰15.4万円｜—｜🔒実弾封印中(PL3紙ログ収集中)

## 🤖AI特需銘柄
波: wave_on なし／25MA 上回り率 エネマネ 14.3%・冷却 25.0%・光 27.3%・基板 2.4%
- 6777 santec｜ai_momentum/ai_reversal｜🚀確変｜⚪妥当｜PASS｜20,910円｜💰209.1万円｜momentum 21330/SL20040.8（✅即時可）｜🤖AI特需 🌐光通信/中流 ⚠日程不明 📑TOPIX新規採用（2026-10-30 組入） ⚠市場に劣後 RS20 -5.3pt ⚠1単元でリスク枠超過（128920円）
  > 【業態】光通信・産業・医療用の光測定器が収益源。光モニターや光フィルターなど光部品も。
  > 【いま】終値20,910円・直近5日+29.31%（材料未確認）
  > 【調子】🚀確変（11/13） — 上方修正済み
  > 【水準】⚪妥当（4.0/7）— PER19.67倍・PEG0.3105・52週49.5% ／ 💰単元209.1万円
  > 【戦略】当日高値超えの逆指値21330円で順張り参戦を検討。上限21543.3円・SL20040.8円目安／⚠1単元リスク128920円（枠超過）
- 9824 泉州電業｜ai_momentum/ai_reversal/granville_oshime｜🔥絶好調｜⚪妥当｜PASS｜7,830円｜💰78.3万円｜momentum 7880/SL7397.8（⏸位置不適(25MA下 -2.36%)）｜📋カルテ窓 12/08(残18営業日) ⚠1単元でリスク枠超過（48220円）
  > 【業態】電線専門商社。FA・機器・通信・電力向け電線、光ファイバーが軸。即納制に強み。
  > 【いま】終値7,830円・直近5日+1.95%（材料未確認）
  > 【調子】🔥絶好調（10/13）
  > 【水準】⚪妥当（4.0/7）— PER14.57倍・PEG0.3624・52週80.9% ／ 💰単元78.3万円
  > 【戦略】当日高値超えの逆指値7880円で順張り参戦を検討。上限7958.8円・SL7397.8円目安（⏸位置不適(25MA下 -2.36%)）／⚠1単元リスク48220円（枠超過）
- 6613 QD Laser, Inc.｜ai_momentum/granville_oshime｜🔥絶好調｜🔴過熱｜PASS｜2,185円｜💰21.9万円｜momentum 2222/SL2087.7（✅即時可）｜🚨決算直前 11/12(残1営業日) 織り込み済みの可能性（押し目待ち推奨圏） 📑TOPIX新規採用（2026-10-30 組入）
  > 【業態】半導体レーザ、網膜走査型レーザアイウェアなどの開発・製造・販売を手掛ける。
  > 【いま】終値2,185円・直近5日-10.38%（材料未確認）
  > 【調子】🔥絶好調（10/13） — 赤字→黒字転換
  > 【水準】🔴過熱（2.0/7）— PER208.1倍・PEG2.0607・52週56.9% ／ 💰単元21.9万円
  > 【戦略】当日高値超えの逆指値2222円で順張り参戦を検討。上限2244.2円・SL2087.7円目安
- 6521 オキサイド｜ai_momentum/ai_reversal｜⚡好調｜🟢値頃｜PASS｜3,090円｜💰30.9万円｜⛔提案なし(指名鮮度切れ 12営業日)｜⚡材料後出し ⚠日程不明
  > 【業態】単結晶や光部品、レーザ光源、計測装置の開発・販売。半導体、画像装置向け。
  > 【いま】終値3,090円・直近5日-0.16%・📌量子コンピュータ向け紫外線レーザ「Frequad-K」が光学・フォトニクス分野の国際賞「SPIE Prism Awards 2027」のファイナリストに選出
  > 【調子】⚡好調（7/13） — 経常成長率+83.1%
  > 【水準】🟢値頃（5.0/7）— PER27.06倍・PEG0.3257・52週28.1% ／ 💰単元30.9万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 12営業日)）
- 6988 日東電工｜ai_momentum/ai_reversal｜⚡好調｜🟡やや割高｜FAIL_UWAHIGE｜3,474円｜💰34.5万円｜—
- 4063 信越化学工業｜ai_momentum/ai_reversal｜✅順調｜⚪妥当｜PASS｜5,709円｜💰57.1万円｜momentum 5745/SL5390.9（⏸位置不適(25MA下 -3.2%)）｜⚠日程不明 ⚠1単元でリスク枠超過（35410円）
  > 【業態】塩ビ・半導体ウエハーで世界トップ。シリコーン(ケイ素樹脂)大手。セルロース、レアアース磁石も。
  > 【いま】終値5,709円・直近5日-1.55%（材料未確認）
  > 【調子】✅順調（4/13） — E軸判定不能(進捗データ不足)
  > 【水準】⚪妥当（3.0/7）— PER19.73倍・PEG2.2646・52週37.7% ／ 💰単元57.1万円
  > 【戦略】当日高値超えの逆指値5745円で順張り参戦を検討。上限5802.4円・SL5390.9円目安（⏸位置不適(25MA下 -3.2%)）／⚠1単元リスク35410円（枠超過）
- 6367 ダイキン工業｜ai_momentum｜✅順調｜🔴過熱｜FAIL_UWAHIGE｜23,235円｜💰224.4万円｜—
- 1975 新日本空調｜ai_momentum｜➖横ばい｜⚪妥当｜PASS｜3,465円｜💰34.6万円｜momentum 3485/SL3271.2（⏸位置不適(25MA下 -6.23%)）｜🚨決算直前 11/12(残1営業日) ⚠市場に劣後 RS20 -7.4pt
  > 【業態】空調・衛生工事の大手。ハイテク環境制御装置に優れる。民間受注が中心。
  > 【いま】終値3,465円・直近5日-0.86%（材料未確認）
  > 【調子】➖横ばい（2/13） — E軸判定不能(進捗データ不足)
  > 【水準】⚪妥当（3.0/7）— PER9.7倍・PEG3.1619・52週31.4% ／ 💰単元34.6万円
  > 【戦略】当日高値超えの逆指値3485円で順張り参戦を検討。上限3519.8円・SL3271.2円目安（⏸位置不適(25MA下 -6.23%)）
- 1982 日比谷総合設備｜ai_momentum/ai_reversal｜⚠減速｜🔴過熱｜PASS｜3,155円｜💰31.6万円｜momentum 3195/SL2998.6（⏸位置不適(25MA下 -1.2%)）｜📉決算反応日 11/12 ⚠業績基調が下向き（⚠減速）
  > 【業態】空調工事大手。電気・衛生工事も。NTT向け主力。床下空調システムなどに強み。
  > 【いま】終値3,155円・直近5日+3.10%・📊2027年３月期 第２四半期（中間期）決算短信〔日本基準〕（連結）
  > 【調子】⚠減速（1/13） — E軸判定不能(進捗データ不足)
  > 【水準】🔴過熱（1.0/7）— PER14.97倍・PEG5.138・52週76.2% ／ 💰単元31.6万円
  > 【戦略】当日高値超えの逆指値3195円で順張り参戦を検討。上限3226.9円・SL2998.6円目安（⏸位置不適(25MA下 -1.2%)）
- 5803 フジクラ｜ai_reversal/changepoint｜🚀確変｜💎割安｜PASS｜3,121円｜💰31.2万円｜reversal 3121/SL2622.5（⏸トラップ疑い・確認足待ち）｜🤖AI特需 🏢大型・指数寄与/電線光 ⚠日程不明 📐進捗 上振れ 30.1% ⚠1単元でリスク枠超過（49850円）
  > 【業態】電線3強の一角。フレキシブルプリント基板で世界的。電子電装に力。超電導線材も。
  > 【いま】終値3,121円・直近5日-15.19%（材料未確認）
  > 【調子】🚀確変（13/13） — 上方修正済み
  > 【水準】💎割安（7.0/7）— PER15.86倍・PEG0.1268・52週9.4% ／ 💰単元31.2万円
  > 【戦略】当日終値3121円の指値で反転を取りにいく。SL2622.5円（直近5日安値）（⏸トラップ疑い・確認足待ち）／⚠1単元リスク49850円（枠超過）
- 3131 Shinden Hightex Corp.｜ai_reversal/granville_rebound｜🚀確変｜💎割安｜PASS｜6,310円｜💰63.1万円｜⛔型不一致: 既に支持帯以下｜ストップ高 🤖AI特需 🔬基板・素材/装置・商社 ⚠日程不明 📐進捗 上振れ 32.9%
  > 【業態】液晶モジュール、半導体、電子機器、バッテリの専門商社。韓国LG、SK製品が主力。
  > 【いま】終値6,310円・直近5日+26.96%（材料未確認）
  > 【調子】🚀確変（13/13） — 上方修正済み
  > 【水準】💎割安（6.0/7）— PER2.97倍・PEG0.003・52週57.6% ／ 💰単元63.1万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 4047 関東電化工業｜ai_reversal｜🚀確変｜💎割安｜PASS｜1,812円｜💰18.1万円｜reversal 1812/SL1460（✅即時可）｜⚠日程不明 ⚠1単元でリスク枠超過（35200円）
  > 【業態】古河系、特殊ガス大手。独自フッ素系技術や半導体・FPD用特殊ガスに強み。
  > 【いま】終値1,812円・直近5日-3.31%（材料未確認）
  > 【調子】🚀確変（13/13） — 進捗モデル値域外
  > 【水準】💎割安（6.0/7）— PER10.5倍・PEG0.0884・52週25.4% ／ 💰単元18.1万円
  > 【戦略】当日終値1812円の指値で反転を取りにいく。SL1460円（直近5日安値）／⚠1単元リスク35200円（枠超過）
- 6918 アバールデータ｜ai_reversal｜🚀確変｜🟢値頃｜PASS｜3,270円｜💰32.7万円｜reversal 3270/SL2804（✅即時可）｜🤖AI特需 🔬基板・素材/装置・商社 🚨決算直前 11/12(残1営業日) ⚠1単元でリスク枠超過（46600円）
  > 【業態】半導体製造装置の制御組込を受託。自社製品も。画像・計測・通信が主力。
  > 【いま】終値3,270円・直近5日-4.39%（材料未確認）
  > 【調子】🚀確変（13/13）
  > 【水準】🟢値頃（5.0/7）— PER10.05倍・PEG0.0754・52週43% ／ 💰単元32.7万円
  > 【戦略】当日終値3270円の指値で反転を取りにいく。SL2804円（直近5日安値）／⚠1単元リスク46600円（枠超過）
- 3374 内外テック｜ai_reversal/granville_rebound｜🚀確変｜💎割安｜PASS｜4,110円｜💰41.1万円｜reversal 4110/SL3300（✅即時可）｜⏰決算 11/13(残2営業日) ⚠1単元でリスク枠超過（81000円）
  > 【業態】半導体製造装置部品商社。組立や受託製造、保守も。東エレクへ依存度大。
  > 【いま】終値4,110円・直近5日-2.49%（材料未確認）
  > 【調子】🚀確変（12/13）
  > 【水準】💎割安（6.0/7）— PER8.57倍・PEG0.1034・52週60.6% ／ 💰単元41.1万円
  > 【戦略】当日終値4110円の指値で反転を取りにいく。SL3300円（直近5日安値）／⚠1単元リスク81000円（枠超過）
- 4062 イビデン｜ai_reversal/granville_rebound｜🚀確変｜🟢値頃｜PASS｜6,920円｜💰69.2万円｜reversal 6920/SL5726（✅即時可）｜🤖AI特需 🔬基板・素材/中流 ⚠日程不明 📐進捗 遅れ -20.5% ⚠1単元でリスク枠超過（119400円）
  > 【業態】ICパッケージ、プリント配線板で首位級。スマホ用が拡大。自動車排ガス除去も大手。
  > 【いま】終値6,920円・直近5日-13.90%（材料未確認）
  > 【調子】🚀確変（12/13） — 上方修正済み
  > 【水準】🟢値頃（5.0/7）— PER43.96倍・PEG0.3629・52週38.6% ／ 💰単元69.2万円
  > 【戦略】当日終値6920円の指値で反転を取りにいく。SL5726円（直近5日安値）／⚠1単元リスク119400円（枠超過）
- 6857 アドバンテスト｜ai_reversal/changepoint｜🚀確変｜⚪妥当｜PASS｜31,440円｜💰314.4万円｜reversal 31440/SL24655（✅即時可）｜⚠日程不明 ⚠1単元でリスク枠超過（678500円）
  > 【業態】半導体試験装置で世界大手。DRAM用トップ。テストシステム、電子ビーム技術に強み。
  > 【いま】終値31,440円・直近5日-9.05%（材料未確認）
  > 【調子】🚀確変（11/13） — 税引前代替
  > 【水準】⚪妥当（4.0/7）— PER30.62倍・PEG0.3134・52週55.5% ／ 💰単元314.4万円
  > 【戦略】当日終値31440円の指値で反転を取りにいく。SL24655円（直近5日安値）／⚠1単元リスク678500円（枠超過）
- 5801 古河電気工業｜ai_reversal｜🔥絶好調｜💎割安｜PASS｜2,373円｜💰23.7万円｜reversal 2373/SL1692.5（✅即時可）｜🤖AI特需 🏢大型・指数寄与/電線光 ⚠日程不明 📐進捗 上振れ 31.9% ⚠1単元でリスク枠超過（68050円）
  > 【業態】電線3強の一角。光ファイバーで世界有数。電装材や軽金属、機能製品など多角。
  > 【いま】終値2,373円・直近5日-8.18%（材料未確認）
  > 【調子】🔥絶好調（10/13） — 上方修正済み
  > 【水準】💎割安（7.0/7）— PER14.15倍・PEG0.1356・52週27.9% ／ 💰単元23.7万円
  > 【戦略】当日終値2373円の指値で反転を取りにいく。SL1692.5円（直近5日安値）／⚠1単元リスク68050円（枠超過）
- 6787 メイコー｜ai_reversal｜🔥絶好調｜💎割安｜PASS｜8,320円｜💰83.2万円｜reversal 8320/SL5650（✅即時可）｜🤖AI特需 🔬基板・素材/中流 ⚠日程不明 📐進捗 遅れ -25.9% ⚠1単元でリスク枠超過（267000円）
  > 【業態】プリント配線板製造大手。車載向け、スマホ向けが主軸。中国、ベトナムに生産工場。
  > 【いま】終値8,320円・直近5日+7.63%（材料未確認）
  > 【調子】🔥絶好調（10/13） — 上方修正済み
  > 【水準】💎割安（7.0/7）— PER12.68倍・PEG0.1814・52週21.1% ／ 💰単元83.2万円
  > 【戦略】当日終値8320円の指値で反転を取りにいく。SL5650円（直近5日安値）／⚠1単元リスク267000円（枠超過）
- 8035 東京エレクトロン｜ai_reversal｜🔥絶好調｜💎割安｜PASS｜9,272円｜💰92.7万円｜reversal 9272/SL7502（✅即時可）｜⚠日程不明 ⚠1単元でリスク枠超過（177000円）
  > 【業態】半導体製造装置で世界的。前工程に強み。次世代微細加工に注力。
  > 【いま】終値9,272円・直近5日-4.05%（材料未確認）
  > 【調子】🔥絶好調（10/13）
  > 【水準】💎割安（7.0/7）— PER24.24倍・PEG0.2785・52週31.8% ／ 💰単元92.7万円
  > 【戦略】当日終値9272円の指値で反転を取りにいく。SL7502円（直近5日安値）／⚠1単元リスク177000円（枠超過）
- 6407 CKD｜ai_reversal｜🔥絶好調｜💎割安｜PASS｜4,139円｜💰41.4万円｜reversal 4139/SL3430（✅即時可）｜⏰決算 11/13(残2営業日) ⚠1単元でリスク枠超過（70900円）
  > 【業態】省力・自動機械大手。薬品包装機械、半導体用薬液制御機器などに強み。
  > 【いま】終値4,139円・直近5日-8.43%（材料未確認）
  > 【調子】🔥絶好調（10/13）
  > 【水準】💎割安（6.0/7）— PER14.56倍・PEG0.335・52週28.7% ／ 💰単元41.4万円
  > 【戦略】当日終値4139円の指値で反転を取りにいく。SL3430円（直近5日安値）／⚠1単元リスク70900円（枠超過）
- 4971 メック｜ai_reversal｜🔥絶好調｜🟢値頃｜PASS｜5,730円｜💰57.3万円｜⛔提案なし(材料後出し)｜⚡材料後出し 📉決算反応日 11/12
  > 【業態】電子基板向け薬品会社。半導体実装パッケージ基板で独占的。研究開発に力。
  > 【いま】終値5,730円・直近5日-1.55%・📊2026年12月期第３四半期決算短信〔日本基準〕(連結)
  > 【調子】🔥絶好調（10/13）
  > 【水準】🟢値頃（5.0/7）— PER17.44倍・PEG0.4308・52週16.5% ／ 💰単元57.3万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 3110 日東紡｜ai_reversal｜🔥絶好調｜💎割安｜PASS｜2,802円｜💰28.0万円｜reversal 2802/SL1931（✅即時可）｜⚠日程不明 📐進捗 上振れ 12.3% ⚠1単元でリスク枠超過（87100円）
  > 【業態】ガラス繊維活用の産業資材で世界有数。建材、ヘルスケア、メディカル事業など多角化。
  > 【いま】終値2,802円・直近5日+5.38%（材料未確認）
  > 【調子】🔥絶好調（9/13） — 上方修正済み
  > 【水準】💎割安（7.0/7）— PER21.24倍・PEG0.3674・52週18.7% ／ 💰単元28.0万円
  > 【戦略】当日終値2802円の指値で反転を取りにいく。SL1931円（直近5日安値）／⚠1単元リスク87100円（枠超過）
- 4368 扶桑化学工業｜ai_reversal｜🔥絶好調｜💎割安｜PASS｜3,020円｜💰30.2万円｜reversal 3020/SL2450（✅即時可）｜⚠日程不明 ⚠1単元でリスク枠超過（57000円）
  > 【業態】果実酸類大手。リンゴ酸で世界高シェア。電子材料ではウエハ研磨剤原料に強み。
  > 【いま】終値3,020円・直近5日-0.82%（材料未確認）
  > 【調子】🔥絶好調（9/13） — 上方修正済み
  > 【水準】💎割安（6.0/7）— PER14.59倍・PEG0.3349・52週37.6% ／ 💰単元30.2万円
  > 【戦略】当日終値3020円の指値で反転を取りにいく。SL2450円（直近5日安値）／⚠1単元リスク57000円（枠超過）
- 6779 Nihon Dempa Kogyo Co., Ltd.｜ai_reversal/granville_rebound｜🔥絶好調｜💎割安｜PASS｜1,984円｜💰19.8万円｜reversal 1984/SL1713（✅即時可）｜🤖AI特需 📡エネマネ・計量/中流 ⚠日程不明
  > 【業態】水晶関連専業で世界大手。小型デバイス製品に力。国内、中国、マレーシアで生産。
  > 【いま】終値1,984円・直近5日-13.13%（材料未確認）
  > 【調子】🔥絶好調（9/13） — 税引前代替
  > 【水準】💎割安（6.0/7）— PER14.22倍・PEG0.2076・52週26.2% ／ 💰単元19.8万円
  > 【戦略】当日終値1984円の指値で反転を取りにいく。SL1713円（直近5日安値）
- 2760 東京エレクトロンデバイス｜ai_reversal｜🔥絶好調｜🟢値頃｜PASS｜3,985円｜💰39.9万円｜reversal 3985/SL3235（✅即時可）｜⚠日程不明 ⚠1単元でリスク枠超過（75000円）
  > 【業態】電子部品の半導体商社。主に米国製を扱う。設計受託で産業用に強み。
  > 【いま】終値3,985円・直近5日-0.13%（材料未確認）
  > 【調子】🔥絶好調（9/13） — ⚠下期依存
  > 【水準】🟢値頃（5.0/7）— PER10.64倍・PEG0.166・52週48.1% ／ 💰単元39.9万円
  > 【戦略】当日終値3985円の指値で反転を取りにいく。SL3235円（直近5日安値）／⚠1単元リスク75000円（枠超過）
- 6235 オプトラン｜ai_reversal｜🔥絶好調｜🟢値頃｜PASS｜2,289円｜💰22.9万円｜reversal 2289/SL1673（✅即時可）｜⚠日程不明 ⚠1単元でリスク枠超過（61600円）
  > 【業態】光学薄膜装置の製造・販売。車載カメラ、スマホ向けに注力。保守まで一貫に強み。
  > 【いま】終値2,289円・直近5日+7.16%（材料未確認）
  > 【調子】🔥絶好調（9/13） — 突出ボーナス
  > 【水準】🟢値頃（5.0/7）— PER16.3倍・PEG0.1244・52週21.9% ／ 💰単元22.9万円
  > 【戦略】当日終値2289円の指値で反転を取りにいく。SL1673円（直近5日安値）／⚠1単元リスク61600円（枠超過）
- 6762 TDK｜ai_reversal｜🔥絶好調｜🟢値頃｜PASS｜2,366円｜💰23.7万円｜reversal 2365.5/SL1972.5（✅即時可）｜🤖AI特需 🏢大型・指数寄与/素材部品 ⚠日程不明 ⚠1単元でリスク枠超過（39300円）
  > 【業態】電子部品大手。HDD向け磁気ヘッドから、2次電池、センサ応用、受動部品も成長。
  > 【いま】終値2,366円・直近5日-3.49%（材料未確認）
  > 【調子】🔥絶好調（9/13）
  > 【水準】🟢値頃（5.0/7）— PER16.04倍・PEG0.4764・52週19.5% ／ 💰単元23.7万円
  > 【戦略】当日終値2365.5円の指値で反転を取りにいく。SL1972.5円（直近5日安値）／⚠1単元リスク39300円（枠超過）
- 6981 村田製作所｜ai_reversal｜🔥絶好調｜🟢値頃｜PASS｜5,457円｜💰54.6万円｜reversal 5457/SL4286（✅即時可）｜🤖AI特需 🔬基板・素材/中流 ⚠日程不明 ⚠1単元でリスク枠超過（117100円）
  > 【業態】電気機器（電子部品・セラミックコンデンサー・携帯電話部材・部品関連）
  > 【いま】終値5,457円・直近5日-9.53%（材料未確認）
  > 【調子】🔥絶好調（9/13） — 税引前代替
  > 【水準】🟢値頃（5.0/7）— PER24.94倍・PEG0.3446・52週26.2% ／ 💰単元54.6万円
  > 【戦略】当日終値5457円の指値で反転を取りにいく。SL4286円（直近5日安値）／⚠1単元リスク117100円（枠超過）
- 7729 東京精密｜ai_reversal｜🔥絶好調｜🟢値頃｜PASS｜13,495円｜💰134.9万円｜reversal 13495/SL9922（✅即時可）｜🤖AI特需 🔬基板・素材/装置・商社 ⚠日程不明 ⚠1単元でリスク枠超過（357300円）
  > 【業態】半導体製造装置・計測機器メーカー。ウエハテスト用首位。精密位置決め技術に定評。
  > 【いま】終値13,495円・直近5日-9.55%（材料未確認）
  > 【調子】🔥絶好調（9/13） — 🔼加速
  > 【水準】🟢値頃（5.0/7）— PER17.12倍・PEG0.5584・52週31.4% ／ 💰単元134.9万円
  > 【戦略】当日終値13495円の指値で反転を取りにいく。SL9922円（直近5日安値）／⚠1単元リスク357300円（枠超過）
- 6323 ローツェ｜ai_reversal｜🔥絶好調｜⚪妥当｜PASS｜3,365円｜💰33.6万円｜reversal 3365/SL2560.5（✅即時可）｜⚠日程不明 📐進捗 遅れ -11.4% ⚠1単元でリスク枠超過（80450円）
  > 【業態】機械（半導体製造装置・液晶製造装置・FA関連関連）
  > 【いま】終値3,365円・直近5日-2.49%（材料未確認）
  > 【調子】🔥絶好調（9/13） — 上方修正済み
  > 【水準】⚪妥当（4.0/7）— PER15.45倍・PEG0.2263・52週42.7% ／ 💰単元33.6万円
  > 【戦略】当日終値3365円の指値で反転を取りにいく。SL2560.5円（直近5日安値）／⚠1単元リスク80450円（枠超過）
- 7735 SCREENホールディングス｜ai_reversal｜🔥絶好調｜💎割安｜PASS｜8,777円｜💰87.8万円｜reversal 8777/SL7125（✅即時可）｜🤖AI特需 🏢大型・指数寄与/装置 ⚠日程不明 📐進捗 遅れ -10.4% ⚠1単元でリスク枠超過（165200円）
  > 【業態】半導体・液晶製造装置が主力。ウエハ洗浄装置で世界首位。画像処理機器も。
  > 【いま】終値8,777円・直近5日-1.92%（材料未確認）
  > 【調子】🔥絶好調（8/13） — ⚠進捗遅れ
  > 【水準】💎割安（7.0/7）— PER14.45倍・PEG0.5582・52週21.2% ／ 💰単元87.8万円
  > 【戦略】当日終値8777円の指値で反転を取りにいく。SL7125円（直近5日安値）／⚠1単元リスク165200円（枠超過）
- 6941 山一電機｜ai_reversal｜🔥絶好調｜💎割安｜PASS｜6,960円｜💰69.6万円｜reversal 6960/SL5090（✅即時可）｜⚠日程不明 ⚠1単元でリスク枠超過（187000円）
  > 【業態】半導体検査用ソケット大手。基板装置や実装用も。新分野育成し安定化へ。
  > 【いま】終値6,960円・直近5日+1.61%（材料未確認）
  > 【調子】🔥絶好調（8/13）
  > 【水準】💎割安（6.0/7）— PER11.42倍・PEG0.372・52週29.5% ／ 💰単元69.6万円
  > 【戦略】当日終値6960円の指値で反転を取りにいく。SL5090円（直近5日安値）／⚠1単元リスク187000円（枠超過）
- 6524 湖北工業｜ai_reversal｜🔥絶好調｜🟢値頃｜PASS｜4,825円｜💰48.2万円｜reversal 4825/SL3510（✅即時可）｜🚨決算直前 11/12(残1営業日) ⚠1単元でリスク枠超過（131500円）
  > 【業態】アルミ電解コンデンサー用のリード端子や通信網用光部品の製造・販売を手掛ける。
  > 【いま】終値4,825円・直近5日+10.03%（材料未確認）
  > 【調子】🔥絶好調（8/13） — E軸判定不能(進捗データ不足)
  > 【水準】🟢値頃（5.6/7）— PER27.08倍・PEG0.5259・52週40.9% ／ 💰単元48.2万円
  > 【戦略】当日終値4825円の指値で反転を取りにいく。SL3510円（直近5日安値）／⚠1単元リスク131500円（枠超過）
- 5384 フジミインコーポレーテッド｜ai_reversal｜🔥絶好調｜🟢値頃｜PASS｜3,010円｜💰30.1万円｜reversal 3010/SL2449（✅即時可）｜⚠日程不明 📐進捗 上振れ 20.0% ⚠1単元でリスク枠超過（56100円）
  > 【業態】半導体ウエハー用研磨材で世界首位。溶射技術にも強み。CMP製品が成長。
  > 【いま】終値3,010円・直近5日-0.33%（材料未確認）
  > 【調子】🔥絶好調（8/13）
  > 【水準】🟢値頃（5.0/7）— PER17.26倍・PEG0.7341・52週27.7% ／ 💰単元30.1万円
  > 【戦略】当日終値3010円の指値で反転を取りにいく。SL2449円（直近5日安値）／⚠1単元リスク56100円（枠超過）
- 6752 パナソニックHD｜ai_reversal/granville_rebound｜⚡好調｜🟢値頃｜PASS｜3,257円｜💰32.6万円｜reversal 3257/SL2808（✅即時可）｜🤖AI特需 🔬基板・素材/下流 ⚠日程不明 ⚠1単元でリスク枠超過（44900円）
  > 【業態】総合家電大手。AV、白モノ家電が軸。電池、照明、デバイス、住設も。車機器売却。
  > 【いま】終値3,257円・直近5日-6.97%（材料未確認）
  > 【調子】⚡好調（7/13） — 税引前代替
  > 【水準】🟢値頃（5.0/7）— PER14.08倍・PEG0.0811・52週47.5% ／ 💰単元32.6万円
  > 【戦略】当日終値3257円の指値で反転を取りにいく。SL2808円（直近5日安値）／⚠1単元リスク44900円（枠超過）
- 4022 ラサ工業｜ai_reversal｜⚡好調｜💎割安｜FAIL_UWAHIGE｜1,435円｜💰11.8万円｜—｜⚡材料後出し
- 6336 石井表記｜ai_reversal/granville_rebound｜⚡好調｜💎割安｜PASS｜1,266円｜💰12.7万円｜reversal 1266/SL998（✅即時可）
  > 【業態】プリント基板製造装置の大手。ディスプレイ用インクジェット塗布機、印刷技術にも力。
  > 【いま】終値1,266円・直近5日+3.77%（材料未確認）
  > 【調子】⚡好調（6/13）
  > 【水準】💎割安（7.0/7）— PER9.46倍・PEG0.3653・52週38.1% ／ 💰単元12.7万円
  > 【戦略】当日終値1266円の指値で反転を取りにいく。SL998円（直近5日安値）
- 6227 AIMECHATEC Ltd.｜ai_reversal/granville_oshime｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜4,855円｜💰46.0万円｜—｜🤖AI特需 🔬基板・素材/装置・商社
- 4973 JCU｜ai_reversal｜⚡好調｜⚪妥当｜PASS｜4,120円｜💰41.2万円｜reversal 4120/SL3650（✅即時可）｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8） ⚠1単元でリスク枠超過（47000円）
  > 【業態】メッキ用薬品の開発・販売。電子基板向けが主力。実装品向けも。ファブレス企業。
  > 【いま】終値4,120円・直近5日+0.73%（材料未確認）
  > 【調子】⚡好調（5/13） — E軸判定不能(進捗データ不足)
  > 【水準】⚪妥当（3.0/7）— PER11.04倍・PEG3.5695・52週28.7% ／ 💰単元41.2万円
  > 【戦略】当日終値4120円の指値で反転を取りにいく。SL3650円（直近5日安値）／⚠1単元リスク47000円（枠超過）
- 6590 芝浦メカトロニクス｜ai_reversal｜✅順調｜🟢値頃｜PASS｜2,921円｜💰29.2万円｜reversal 2921/SL2035（✅即時可）｜⚠日程不明 📐進捗 遅れ -18.8% ⚠1単元でリスク枠超過（88600円）
  > 【業態】液晶・半導体の製造装置メーカー。前工程ウエハ洗浄で世界トップ。自販機システムも。
  > 【いま】終値2,921円・直近5日-3.76%（材料未確認）
  > 【調子】✅順調（4/13） — ⚠進捗遅れ
  > 【水準】🟢値頃（5.0/7）— PER15.35倍・PEG0.9148・52週20.7% ／ 💰単元29.2万円
  > 【戦略】当日終値2921円の指値で反転を取りにいく。SL2035円（直近5日安値）／⚠1単元リスク88600円（枠超過）
- 5706 三井金属鉱業｜ai_reversal｜🔻悪化｜⚪妥当｜PASS｜1,670円｜💰16.7万円｜reversal 1669.5/SL1384（✅即時可）｜⚠日程不明 ⚠業績基調が下向き（🔻悪化） 📐進捗 上振れ 60.7%
  > 【業態】非鉄大手。銅箔で世界首位級。半導体材料にも強み。自動車部品に注力。
  > 【いま】終値1,670円・直近5日-12.02%（材料未確認）
  > 【調子】🔻悪化（4/13） — 質注意
  > 【水準】⚪妥当（4.0/7）— PER12.25倍・PEG—・52週6.5% ／ 💰単元16.7万円
  > 【戦略】当日終値1669.5円の指値で反転を取りにいく。SL1384円（直近5日安値）
- 5208 Arisawa Mfg.Co., Ltd.｜ai_reversal/granville_oshime｜✅順調｜🔴過熱｜PASS｜2,334円｜💰23.3万円｜reversal 2334/SL1979（✅即時可）｜🤖AI特需 🔬基板・素材/上流 ⚠日程不明 📐進捗 上振れ 23.9% ⚠1単元でリスク枠超過（35500円）
  > 【業態】プリント基板向け材料が主力。液晶用フィルムも。電気絶縁・産業用構造材に注力。
  > 【いま】終値2,334円・直近5日-2.14%（材料未確認）
  > 【調子】✅順調（4/13） — 質注意
  > 【水準】🔴過熱（1.0/7）— PER17.02倍・PEG4.3135・52週54.3% ／ 💰単元23.3万円
  > 【戦略】当日終値2334円の指値で反転を取りにいく。SL1979円（直近5日安値）／⚠1単元リスク35500円（枠超過）
- 6965 浜松ホトニクス｜ai_reversal｜✅順調｜🔴過熱｜PASS｜2,358円｜💰23.6万円｜reversal 2357.5/SL1800.5（✅即時可）｜⚠日程不明 ℹ相対強い RS20 5.1pt ⚠1単元でリスク枠超過（55700円）
  > 【業態】電気機器（計測機器・試験・検査・計測・光デバイス関連）
  > 【いま】終値2,358円・直近5日+12.42%（材料未確認）
  > 【調子】✅順調（4/13） — E軸判定不能(期首・進捗なし)
  > 【水準】🔴過熱（1.0/7）— PER30.9倍・PEG3.9608・52週53.9% ／ 💰単元23.6万円
  > 【戦略】当日終値2357.5円の指値で反転を取りにいく。SL1800.5円（直近5日安値）／⚠1単元リスク55700円（枠超過）
- 3103 ユニチカ｜ai_reversal/granville_rebound｜⚠減速｜💎割安｜FAIL_INSEN｜1,312円｜💰13.5万円｜—
- 255A GLテクノHD｜ai_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜4,100円｜💰41.2万円｜—｜⚡材料後出し
- 6501 日立製作所｜ai_reversal｜✅順調｜🟡やや割高｜FAIL_UWAHIGE｜4,950円｜💰45.4万円｜—
- 2802 味の素｜ai_reversal｜➖横ばい｜⚪妥当｜FAIL_INSEN｜4,264円｜💰43.5万円｜—
- 9503 関西電力｜ai_reversal｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜2,644円｜💰26.7万円｜—｜🤖AI特需 🏢大型・指数寄与/電力重電
- 5302 日本カーボン｜ai_reversal｜➖横ばい｜🔴過熱｜FAIL_INSEN｜4,775円｜💰48.0万円｜—
- 6617 東光高岳｜ai_reversal｜⚠減速｜⚪妥当｜PASS｜5,180円｜💰51.8万円｜reversal 5180/SL4195（✅即時可）｜🤖AI特需 📡エネマネ・計量/上流 ⚠日程不明 ⚠業績基調が下向き（⚠減速） 📐進捗 上振れ 10.5% ⚠1単元でリスク枠超過（98500円）
  > 【業態】東電系で送配電機器が主力。高岳と東光電が統合。自動検針システムに強み。
  > 【いま】終値5,180円・直近5日-0.19%（材料未確認）
  > 【調子】⚠減速（1/13） — 質注意
  > 【水準】⚪妥当（4.0/7）— PER7.97倍・PEG50.257・52週33.5% ／ 💰単元51.8万円
  > 【戦略】当日終値5180円の指値で反転を取りにいく。SL4195円（直近5日安値）／⚠1単元リスク98500円（枠超過）
- 4203 住友ベークライト｜ai_reversal/granville_rebound｜業績データ取得不可｜🔴過熱｜PASS｜7,574円｜💰75.7万円｜reversal 7574/SL5690（✅即時可）｜⚠日程不明 ⚠1単元でリスク枠超過（188400円）
  > 【業態】化学（ファインケミカル・電子材料・半導体部材・部品関連）
  > 【いま】終値7,574円・直近5日+3.65%（材料未確認）
  > 【調子】業績データ取得不可（—/13） — 業績データ取得不可(前期比行なし)
  > 【水準】🔴過熱（1.8/7）— PER23.32倍・PEG—・52週60.3% ／ 💰単元75.7万円
  > 【戦略】当日終値7574円の指値で反転を取りにいく。SL5690円（直近5日安値）／⚠1単元リスク188400円（枠超過）
- 1961 三機工業｜ai_reversal｜—｜－未評価（次回①-9で算定）｜PASS｜2,412円｜💰24.1万円｜reversal 2412/SL2046（✅即時可）｜⏰決算 11/13(残2営業日) ⚠1単元でリスク枠超過（36600円）
  > 【業態】三井系。設備工事大手。プラントなど総合エンジニアリング。搬送、環境関連に強み。
  > 【いま】終値2,412円・直近5日-0.58%（材料未確認）
  > 【調子】—（—/13）
  > 【水準】－未評価（次回①-9で算定）（—/7）— PER—倍・PEG—・52週45.3% ／ 💰単元24.1万円
  > 【戦略】当日終値2412円の指値で反転を取りにいく。SL2046円（直近5日安値）／⚠1単元リスク36600円（枠超過）
- 3436 SUMCO｜ai_reversal｜取得不可｜⏸判定不能｜PASS｜2,089円｜💰20.9万円｜⛔提案なし(材料後出し)｜⚡材料後出し 📉決算反応日 11/12
  > 【業態】三菱・住友・コマツ系、シリコンウエハー大手。半導体用で世界首位級。大口径に強み。
  > 【いま】終値2,089円・直近5日-5.84%・📊2026年12月期 第3四半期決算短信〔日本基準〕（連結）
  > 【調子】取得不可（—/13） — 業績データ取得不可(経常益予想非開示)
  > 【水準】⏸判定不能（—/7）— PER—倍・PEG—・52週19.9% ／ 💰単元20.9万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 6146 ディスコ｜ai_reversal｜取得不可｜⏸判定不能｜PASS｜47,580円｜💰475.8万円｜reversal 47580/SL37210（✅即時可）｜⚠日程不明 ⚠1単元でリスク枠超過（1037000円）
  > 【業態】半導体、電子部品の研削・切断・研磨装置で世界トップ。砥石等の消耗品も。
  > 【いま】終値47,580円・直近5日+0.44%（材料未確認）
  > 【調子】取得不可（—/13） — 業績データ取得不可(経常益予想非開示)
  > 【水準】⏸判定不能（—/7）— PER—倍・PEG—・52週19% ／ 💰単元475.8万円
  > 【戦略】当日終値47580円の指値で反転を取りにいく。SL37210円（直近5日安値）／⚠1単元リスク1037000円（枠超過）
- 6723 ルネサスエレクトロニクス｜ai_reversal｜取得不可｜⏸判定不能｜PASS｜2,922円｜💰29.2万円｜reversal 2922/SL2228（✅即時可）｜⚠日程不明 ⚠1単元でリスク枠超過（69400円）
  > 【業態】半導体大手。ルネサスとNECエレが統合。車載マイコン世界トップ級。FA、インフラ向けも。
  > 【いま】終値2,922円・直近5日+3.69%（材料未確認）
  > 【調子】取得不可（—/13） — 業績データ取得不可(通期予想非開示)
  > 【水準】⏸判定不能（—/7）— PER—倍・PEG—・52週32.9% ／ 💰単元29.2万円
  > 【戦略】当日終値2922円の指値で反転を取りにいく。SL2228円（直近5日安値）／⚠1単元リスク69400円（枠超過）
- 6971 京セラ｜ai_reversal｜—｜—｜FAIL_UWAHIGE｜3,015円｜💰—万円｜—｜🤖AI特需 🏢大型・指数寄与/素材部品
- 9984 ソフトバンクグループ｜ai_reversal｜業績データ取得不可(経常益予想非開示)｜⏸判定不能｜PASS｜3,855円｜💰38.5万円｜reversal 3855/SL3350（✅即時可）｜⚠日程不明 ⚠1単元でリスク枠超過（50500円）
  > 【業態】投資持ち株会社。傘下に投資のビジョンファンド、通信、英半導体設計アーム。
  > 【いま】終値3,855円・直近5日-9.70%（材料未確認）
  > 【調子】業績データ取得不可(経常益予想非開示)（—/13） — 業績データ取得不可(経常益予想非開示)
  > 【水準】⏸判定不能（—/7）— PER—倍・PEG—・52週8.8% ／ 💰単元38.5万円
  > 【戦略】当日終値3855円の指値で反転を取りにいく。SL3350円（直近5日安値）／⚠1単元リスク50500円（枠超過）

## ⚡材料後出し
その日の足は開示前の情報。判定は参考値
- 421A Movin' Strategic Career CO.,LTD.｜FAIL_UWAHIGE｜📊 [Summary] Consolidated Financial Results for the Nine Months Ended September 30, 2026 (Under Japanese GAAP)
- 147A SORACOM,INC.｜PASS｜📊 [Summary] Consolidated Financial Results for the Six Months of the Fiscal Year Ending March 31, 2027
- 3696 セレス｜PASS｜📌 ラボルがギークスのITフリーランス向け福利厚生プログラム「フリノベ」と提携開始～ITフリーランスの資金繰りをサポート～
- 4933 I-ne CO., LTD.｜FAIL_INSEN｜📊 Consolidated Financial Results for the Nine Months Ended September 30, 2026 (Under Japanese GAAP)
- 5711 三菱マテリアル｜PASS｜📊 Notice of the Adjustment of Conversion Price for Zero Coupon Convertible Bonds due 2030 and Zero Coupon Convertible Bonds due 2032
- 6278 ユニオンツール｜PASS｜📊 [Summary] Financial Results for the Nine Months Ended September 30, 2026
- 6324 Harmonic Drive Systems Inc.｜PASS｜📊 [Summary]Consolidated Financial Results for the Six Months Ended September 30, 2026(Under Japanese GAAP)
- 6588 東芝テック｜FAIL_UWAHIGE｜📊 Consolidated Financial Results for the Six Months Ended September 30, 2026 [Japanese GAAP]
- 5019 出光興産｜PASS｜📊 Announcement on Revisions to Consolidated Financial Results Forecasts and Year-End Dividend Forecast for the Fiscal Year Ending March 2027
- 6845 アズビル｜FAIL_UWAHIGE｜🔁 （訂正）「自己株式の取得状況及び取得終了」及び「自己株式の取得及び消却」に関するお知らせの一部訂正について
- 6284 日精エー・エス・ビー機械｜PASS｜📊 Position and Policy on Lowering Investment Units
- 268A Rigaku Holdings Corporation｜PASS｜📊 FY2026 3Q Earings Presentation
- 6923 Stanley Electric Co., Ltd.｜PASS｜📌 「統合報告書2026」発行のお知らせ
- 8198 Maxvalu Tokai Co., Ltd.｜FAIL_INSEN｜📌 人事異動に関するお知らせ
- 1926 ライト工業（ライト）｜FAIL_INSEN｜📊 [Summary] Consolidated Financial Results for the Six Months Ended September 30, 2026
- 4980 Dexerials Corp.｜PASS｜📊 Consolidated Financial Results for the Six Months Ended September 30, 2026
- 1963 日揮ホールディングス｜PASS｜📊 コーポレート・ガバナンスに関する報告書 2026/11/11
- 8194 Life Corporation｜FAIL_UWAHIGE｜📌 Notice Concerning Results of Tender Offer for ALBIS Co., Ltd. (Securities Code: 7475) and  Change in Subsidiaries
- 8359 Hachijuni Nagano Bank, Ltd.｜PASS｜📌 Notice Concerning the Capital Ratio as of September 30, 2026
- 8304 あおぞら銀行｜FAIL_UWAHIGE｜📊 Aozora Announces Second Quarter Dividend
- 7186 横浜フィナンシャルグループ｜PASS｜📊 Notice of Revisions of Earnings and Dividends Forecasts (Dividend Increase and 10th Anniversary Commemorative Dividend) for the Fiscal Year ending Mar
- 8698 Monex Group, Inc.｜FAIL_UWAHIGE｜📌 (Correction) Notice Regarding Correction to "Notice Concerning Dividends of Surplus (Interim Dividend) for the Fiscal Year Ending March 31, 2027"
- 6521 オキサイド｜PASS｜📌 量子コンピュータ向け紫外線レーザ「Frequad-K」が光学・フォトニクス分野の国際賞「SPIE Prism Awards 2027」のファイナリストに選出
- 4971 メック｜PASS｜📊 Disposal of Treasury Stock Due to Continuation of Share Compensation Plan
- 4022 ラサ工業｜FAIL_UWAHIGE｜📊 [Summary]Consolidated Financial Results for the Six Months Ended September 30, 2026 (Under Japanese GAAP)
- 255A GLテクノHD｜FAIL_INSEN｜📊 Consolidated Financial Results for the Six Months Ended September 30, 2026 (Under Japanese GAAP)
- 3436 SUMCO｜PASS｜📊 Announcement regarding Revision to Dividend Forecast
- 9006 Keikyu Corporation｜FAIL_INSEN｜📊 Notice of Difference Between Consolidated Financial Results Forecast and Results for the Second Quarter (Interim Period)
- 3405 クラレ｜FAIL_UWAHIGE｜📊 Notice Concerning the Merger of Wholly-Owned Subsidiary Kuraray Saijo Co., Ltd.
- 4507 塩野義製薬｜FAIL_INSEN｜📌 (Corrections / Correction of Numerical Data) Corrections to the Consolidated Financial Results for the First Quarter of Fiscal Year 2026 (IFRS)
- 5838 Rakuten Bank, Ltd.｜FAIL_UWAHIGE｜📊 Consolidated Financial Results for the Six Months Ended September 30, 2026 (Under Japanese GAAP)
- 5184 ニチリン｜FAIL_INSEN｜📊 2026年12月期　第3四半期決算短信〔日本基準〕（連結）
- 9735 セコム｜FAIL_INSEN｜📊 Consolidated Financial Results for the Six Months Ended September 30, 2026 (Under Japanese GAAP)
- 7806 MTG Co., Ltd.｜FAIL_INSEN｜📊 投資単位の引下げに関する考え方及び方針等について
- 3673 ブロードリーフ｜FAIL_UWAHIGE｜📊 データブック 2026
- 6523 ＰＨＣホールディングス｜FAIL_UWAHIGE｜📊 Consolidated Financial Results for the Six Months Ended September 30, 2026 [IFRS]
- 9075 福山通運｜FAIL_INSEN｜📊 Notice Concerning Dividends of Surplus (Interim Dividend)
- 4258 AMIYA Corporation｜PASS｜📊 2026年12月期第3四半期 決算説明資料
- 6998 Nippon Tungsten Co., Ltd.｜FAIL_UWAHIGE｜📢 [Summary] Financial Results for the Six Months Ended September 30, 2026
- 456A Human Made Inc.｜FAIL_INSEN｜📌 Notice Concerning Potential Leak of Customer Information Due to Unauthorized Access to an Outsourced Contractor
- 6027 Bengo4.com, Inc.｜FAIL_INSEN｜📊 JPY1 Billion ARR in 17.3 Months:Bengo4.com's Legal AI Agent Is the Fastest Among Major SaaS Products of Japanese Listed Companies
- 3691 DIGITAL PLUS, Inc.｜FAIL_UWAHIGE｜📌 世界5,000万以上のユーザーを持つ「17LIVE」へデジタルギフトを提供
- 5252 日本ナレッジ｜PASS｜📌 生成AIソフトウェア開発支援環境『digitest Local LLM Ver.1.0』の提供開始
- 477A Startline CO.,LTD.｜FAIL_UWAHIGE｜📌 新規出店のお知らせ（Diverse Village TODA）
- 4667 Aisan Technology Co.,Ltd.｜PASS_DOJI｜📊 2027年3月期第2四半期決算補足説明資料
- 4100 Toda Kogyo Corp.｜FAIL_UWAHIGE｜📊 特別利益の計上及び2027年３月期第２四半期（中間期）業績予想と実績との差異並びに通期連結業績予想の修正に関するお知らせ
- 428A Cypress Holdings Co., Ltd.｜FAIL_INSEN｜📌 （開示事項の経過）自己株式取得に係る事項の決定に関するお知らせ
- 8377 ほくほくフィナンシャルグループ｜PASS｜📌 (Correction) Partial Correction to “Consolidated Financial Results for the Six Months Ended September 30, 2026 (Under Japanese GAAP)”
- 265A エイチエムコム｜PASS｜📌 株式会社エンヴァリスによる当社アナリスト・レポート公開のお知らせ
- 8151 東陽テクニカ｜FAIL_UWAHIGE｜📊 Notice Concerning Action to Realize Management Conscious of Cost of Capital and Stock Price (Update)
- 7318 セレンディップ・ホールディングス｜PASS｜📌 PMIの実践を紹介、三井屋工業・エクセルは2027年4月にSerenACへ統合予定
- 4071 Plus Alpha Consulting Co. LTD.｜FAIL_UWAHIGE｜📊 Anticipated Questions for the Financial Results for the Fiscal Year Ended September 30, 2026
- 4259 ExaWizards Inc.｜FAIL_UWAHIGE｜📊 Financial Results for the Second Quarter of FY2027/03
- 4478 freee K.K.｜FAIL_UWAHIGE｜📊 Presentation Materials for Q1 FY2027.6
- 593A Tier IV, Inc.｜PASS｜📌 ドイツ ミュンヘン市内における「Autoware」を活用した大型路線バス向け 自動運転システムの開発支援に関するお知らせ

## 📢開示
使用した一覧: https://kabutan.jp/disclosures/?date=20261111 （1〜91頁・取得1365件）。見出しをそのまま転記（解釈なし）。フォールバック: なし。①-9へ引き渡し（recalc_queue 追加）49件
- 📢 6998 Nippon Tungsten Co., Ltd.｜営業外費用の計上ならびに通期業績予想および配当予想の修正（上方修正）に関するお知らせ｜15:30
- 📊 3673 ブロードリーフ｜2026年12月期  第３四半期決算短信〔ＩＦＲＳ〕（連結）｜15:30
- 📊 5711 三菱マテリアル｜2027年3月期第２四半期（中間期）決算短信［日本基準］（連結）｜15:30
- 📊 4933 I-ne CO., LTD.｜2026年12月期 第3四半期決算短信〔日本基準〕(連結)｜16:45
- 📊 421A Movin' Strategic Career CO.,LTD.｜2026年12月期 第３四半期決算短信〔日本基準〕(連結)｜16:30
- 📊 1963 日揮ホールディングス｜2027年３月期　第２四半期（中間期）決算短信〔日本基準〕(連結)｜15:30
- 📊 4258 AMIYA Corporation｜2026年12月期第３四半期決算短信〔日本基準〕(連結)｜16:05
- 📊 1926 ライト工業（ライト）｜2027年3月期第2四半期（中間期）決算短信〔日本基準〕（連結）｜16:00
- 📊 3405 クラレ｜2026年12月期 第３四半期決算短信〔日本基準〕(連結)｜13:00
- 📊 6027 Bengo4.com, Inc.｜2027年３月期 第２四半期（中間期）決算短信〔日本基準〕(連結)｜15:30
- 📊 6284 日精エー・エス・ビー機械｜2026年9月期　決算短信〔日本基準〕（連結）｜16:00
- 📊 6324 Harmonic Drive Systems Inc.｜2027年３月期第２四半期（中間期）決算短信〔日本基準〕(連結)｜16:00
- 📊 8151 東陽テクニカ｜2026年9月期  決算短信〔日本基準〕（連結）｜16:00
- 📊 8304 あおぞら銀行｜2027年３月期　第２四半期（中間期）決算短信〔日本基準〕（連結）｜16:00
- 📊 5838 Rakuten Bank, Ltd.｜2027年３月期 第２四半期（中間期）決算短信〔日本基準〕(連結)｜15:35
- 📊 147A SORACOM,INC.｜2027年３月期第２四半期（中間期）決算短信〔日本基準〕(連結)｜15:30
- 📊 268A Rigaku Holdings Corporation｜2026年12月期第３四半期決算短信〔ＩＦＲＳ〕(連結)｜15:30
- 📊 3436 SUMCO｜2026年12月期 第3四半期決算短信〔日本基準〕（連結）｜15:30
- 📊 4022 ラサ工業｜2027年３月期 第２四半期（中間期）決算短信〔日本基準〕(連結)｜15:30
- 📊 4071 Plus Alpha Consulting Co. LTD.｜2026年９月期  決算短信〔日本基準〕（連結）｜15:30
- 📊 4100 Toda Kogyo Corp.｜2027年３月期 第２四半期（中間期）決算短信〔日本基準〕（連結）｜15:30
- 📊 4259 ExaWizards Inc.｜2027年３月期第２四半期（中間期）決算短信〔日本基準〕(連結)｜15:30
- 📊 4478 freee K.K.｜2027年６月期第１四半期決算短信〔日本基準〕(連結)｜15:30
- 📊 4971 メック｜2026年12月期第３四半期決算短信〔日本基準〕(連結)｜15:30
- 📊 4980 Dexerials Corp.｜2027年３月期 第２四半期（中間期）決算短信〔ＩＦＲＳ〕（連結）｜15:30
- 📊 5019 出光興産｜2027年３月期 第2四半期（中間期）決算短信〔ＩＦＲＳ会計基準〕（連結）｜15:30
- 📊 6278 ユニオンツール｜2026年12月期 第３四半期決算短信［日本基準］(連結)｜15:30
- 📊 6523 ＰＨＣホールディングス｜2027年３月期 第２四半期（中間期）決算短信〔ＩＦＲＳ〕（連結）｜15:30
- 📊 6588 東芝テック｜2027年３月期 第２四半期（中間期）決算短信〔日本基準〕（連結）｜15:30
- 📊 7186 横浜フィナンシャルグループ｜2027年３月期 第２四半期（中間期）決算短信〔日本基準〕(連結)｜15:30
- 📊 7806 MTG Co., Ltd.｜2026年９月期 決算短信〔日本基準〕（連結）｜15:30
- 📊 9006 Keikyu Corporation｜2027年３月期 第２四半期（中間期）決算短信〔日本基準〕(連結)｜15:30
- 📊 9075 福山通運｜2027年３月期　第２四半期（中間期）決算短信〔日本基準〕（連結）｜15:30
- 📊 9735 セコム｜2027年３月期 第2四半期（中間期）決算短信〔日本基準〕（連結）｜15:30
- 📊 4667 Aisan Technology Co.,Ltd.｜2027年3月期第2四半期（中間期）決算短信〔日本基準〕（連結）｜15:20
- 📊 255A GLテクノHD｜2027年３月期第２四半期（中間期）決算短信〔日本基準〕(連結)｜15:00
- 📊 5184 ニチリン｜2026年12月期　第3四半期決算短信〔日本基準〕（連結）｜15:00
- 📊 4008 住友精化｜2027年３月期 第２四半期（中間期）決算短信〔日本基準〕（連結）｜14:30
- 📊 6570 Kyowa Corporation Co. Ltd.｜2027年３月期第２四半期（中間期）決算短信〔日本基準〕（連結）｜12:30
- 📊 8051 山善｜2027年３月期 第２四半期（中間期）決算短信〔日本基準〕（連結）｜14:00
- 📊 8399 琉球銀行｜2027年3月期　第2四半期(中間期)決算短信〔日本基準〕(連結)｜14:00
- 📊 7213 LECIP Holdings Corporation｜2027年３月期第２四半期決算短信（中間期）決算短信〔日本基準〕（連結）｜13:20
- 📊 2897 Nissin Foods Holdings Co., Ltd.｜2027年3月期 第2四半期（中間期）決算短信〔IFRS〕（連結）｜13:15
- 📊 4396 System Support Holdings Inc.｜2027年６月期 第１四半期決算短信〔日本基準〕（連結）｜13:00
- 📊 4401 ＡＤＥＫＡ｜2027年３月期 第２四半期（中間期）決算短信〔日本基準〕(連結)｜13:00
- 📊 9956 Valor Holdings Co., Ltd.｜2027年３月期　第２四半期（中間期）決算短信〔日本基準〕（連結)｜13:00
- 📊 1982 日比谷総合設備｜2027年３月期 第２四半期（中間期）決算短信〔日本基準〕（連結）｜12:30
- 📊 4966 上村工業｜2027年３月期　第２四半期（中間期）決算短信〔日本基準〕（連結）｜12:30
- 📊 7167 めぶきフィナンシャルグループ｜2027年３月期 第２四半期（中間期）決算短信〔日本基準〕(連結)｜12:00
- 🔁 6845 アズビル｜（訂正）「自己株式の取得状況及び取得終了」及び「自己株式の取得及び消却」に関するお知らせの一部訂正について｜18:59
- 🔁 7381 ＣＣＩグループ｜自己株式の取得状況に関するお知らせ｜13:00
- 📌 8198 Maxvalu Tokai Co., Ltd.｜人事異動に関するお知らせ｜19:00
- 📌 3696 セレス｜ラボルがギークスのITフリーランス向け福利厚生プログラム「フリノベ」と提携開始～ITフリーランスの資金繰りをサポート～｜18:00
- 📌 265A エイチエムコム｜株式会社エンヴァリスによる当社アナリスト・レポート公開のお知らせ｜17:30
- 📌 428A Cypress Holdings Co., Ltd.｜（開示事項の経過）自己株式取得に係る事項の決定に関するお知らせ｜17:20
- 📌 456A Human Made Inc.｜Notice Concerning Potential Leak of Customer Information Due to Unauthorized Access to an Outsourced Contractor｜17:00
- 📌 477A Startline CO.,LTD.｜新規出店のお知らせ（Diverse Village TODA）｜16:00
- 📌 593A Tier IV, Inc.｜ドイツ ミュンヘン市内における「Autoware」を活用した大型路線バス向け 自動運転システムの開発支援に関するお知らせ｜16:00
- 📌 6521 オキサイド｜量子コンピュータ向け紫外線レーザ「Frequad-K」が光学・フォトニクス分野の国際賞「SPIE Prism Awards 2027」のファイナリストに選出｜16:00
- 📌 3691 DIGITAL PLUS, Inc.｜世界5,000万以上のユーザーを持つ「17LIVE」へデジタルギフトを提供｜15:30
- 📌 4507 塩野義製薬｜(Corrections / Correction of Numerical Data) Corrections to the Consolidated Financial Results for the First Quarter of Fiscal Year 2026 (IFRS)｜15:30
- 📌 6923 Stanley Electric Co., Ltd.｜「統合報告書2026」発行のお知らせ｜15:30
- 📌 7318 セレンディップ・ホールディングス｜PMIの実践を紹介、三井屋工業・エクセルは2027年4月にSerenACへ統合予定｜15:30
- 📌 8194 Life Corporation｜Notice Concerning Results of Tender Offer for ALBIS Co., Ltd. (Securities Code: 7475) and  Change in Subsidiaries｜15:30
- 📌 8359 Hachijuni Nagano Bank, Ltd.｜Notice Concerning the Capital Ratio as of September 30, 2026｜15:30
- 📌 8377 ほくほくフィナンシャルグループ｜(Correction) Partial Correction to “Consolidated Financial Results for the Six Months Ended September 30, 2026 (Under Japanese GAAP)”｜15:30
- 📌 8698 Monex Group, Inc.｜(Correction) Notice Regarding Correction to "Notice Concerning Dividends of Surplus (Interim Dividend) for the Fiscal Year Ending March 31, 2027"｜15:30
- 📌 5252 日本ナレッジ｜生成AIソフトウェア開発支援環境『digitest Local LLM Ver.1.0』の提供開始｜15:00
- 📌 3762 テクマトリックス（テクマト）｜FastSeriesの導入企業 エステー株式会社様が「2026 CRMベストプラクティス賞」を受賞｜13:00
- 📌 3927 アークン｜フーバーブレイン、自社開発セキュリティ製品「Eye“247” Safety Zone」にAI統合分析機能を付加する開発に着手｜11:30
- 📌 3491 ＧＡ　ｔｅｃｈｎｏｌｏｇｉｅｓ（ＧＡテクノ）｜AI不動産投資のRENOSY、「不動産投資顧客動向レポート 2026年7～9月」を公開｜11:00
- 📌 4208 UBE Corporation｜(Updated)Consolidated Financial Report for the First Half Ended September 30, 2026｜11:00
- 📌 5243 ｎｏｔｅ｜note Renews the System That Supports Web Page Display - Faster article display and more comfortable reading｜11:00
- 📌 3371 ソフトクリエイトホールディングス｜Notice Regarding Completion of Off-Floor Distribution of Shares｜10:00
- 📌 460A ＢＲＡＮＵ｜建設業界の新たな共創エコシステム構築に向け「CAREECON Plus販売パートナープログラム」を開始｜10:00
- 📌 7003 Mitsui ES Holdings Co., Ltd.｜[Delayed]Notice Concerning the Execution of an Agreement Relating to a Tender Offer for Shares of a Subsidiary (KAJI TECHNOLOGY CORPORATION) and ～｜08:45

## 総当りゲート
### 5手法（276）
- PASS（154）: 147A 1721 1944 1946 1952 1961 1963 1975 1979 1982 268A 2760 3105 3110 3131 3374 3433 3436 3445 3569 3696 3843 3915 4028 4042 4047 4062 4063 4088 4203 4205 4216 4272 4368 4471 4477 4634 4743 4746 4971 4973 4980 5019 5027 5186 5208 5301 5310 5331 5333 5344 5384 5444 5482 5631 5703 5706 5711 5801 5803 5821 5832 5844 5932 6055 6135 6146 618A 6235 6268 6278 6284 6323 6324 6332 6336 6340 6368 6370 6407 6448 6471 6473 6481 6516 6521 6524 6590 6613 6617 6645 6652 6668 6674 6723 6741 6752 6754 6762 6777 6779 6787 6807 6810 6814 6857 6875 6918 6923 6925 6941 6965 6981 7003 7004 7177 7186 7278 7322 7381 7384 7433 7713 7721 7729 7731 7735 7995 8035 8084 8133 8334 8336 8345 8359 8366 8367 8370 8381 8386 8393 8522 8524 8600 8616 8714 9072 9204 9824 9902 9934 9960 9962 9984
- FAIL_UWAHIGE（61）: 1417 1435 167A 1820 1860 1960 262A 2975 3036 3091 3798 3994 4021 4022 4176 421A 4286 4410 4434 4503 4565 4666 5132 5136 5137 5246 5463 558A 5602 6227 6302 6349 6367 6454 6479 6501 6505 6588 6632 6651 6724 6750 6804 6845 6960 6971 6988 7167 7276 7567 7942 8098 8154 8174 8194 8304 8354 8399 8698 9412 9533
- FAIL_INSEN（61）: 1719 1926 1951 2109 2379 255A 276A 2802 2930 3077 3103 3116 3222 3282 3479 3498 3556 3591 3612 4008 4053 4058 4293 4377 4379 4417 446A 4771 4933 4966 5018 5034 505A 5101 5302 5537 5757 5831 6071 6366 6418 6436 6532 6753 6758 7148 7220 7366 7678 7733 8198 8253 8871 8975 9110 9302 9503 9560 9722 9766 9948
### グランビル（208）
- PASS（78）: 2489 2492 278A 2962 3040 3156 3371 338A 3491 3687 3778 3793 3891 3927 3993 4025 4044 4258 4375 4382 4398 4419 4440 4498 460A 4617 4968 5252 5367 5574 5892 5985 6080 6138 6203 6317 6371 6470 6508 6574 6742 6768 6769 6834 6840 6862 6877 6890 6958 6963 7184 7380 7480 7606 7609 7715 7725 7826 7970 8012 8056 8061 8137 8344 8360 8362 8364 8368 8377 8388 8392 8395 8551 8609 8713 8739 9304 9742
- PASS_DOJI（3）: 4403 4667 4902
- FAIL_UWAHIGE（52）: 1436 150A 3002 3106 3405 3549 3563 3673 3691 3692 3762 3850 3851 4005 4045 4075 4100 4208 4401 4432 4523 4554 4674 477A 479A 4848 5381 5838 6191 6250 6490 6523 6676 6745 6998 7175 7256 7269 7734 7747 8016 8051 8160 8361 8410 8697 8995 9163 9166 9509 9552 9697
- FAIL_INSEN（75）: 153A 1928 1941 2206 2384 2488 2502 2811 2897 3042 3092 3182 336A 3496 3935 3964 3968 4166 4169 417A 4206 428A 436A 4396 4413 4507 4534 4540 4549 4552 4568 456A 4765 4912 4922 5036 5105 5184 5233 5243 5254 5532 6027 6036 6099 6328 6432 6570 6592 6736 6744 6947 7213 7744 7806 7921 8095 8113 8167 8255 8801 8803 8804 8944 9006 9045 9075 9278 9401 9418 9536 9735 9837 9842 9956
### 変化点（27）
- PASS（5）: 218A 265A 593A 6136 7318
- FAIL_UWAHIGE（11）: 286A 3923 4071 4259 4443 4478 4483 4488 598A 8151 9308
- FAIL_INSEN（11）: 339A 3989 4011 4165 4475 478A 5582 6785 7695 9343 9888
- 除籍: なし

## 機械詳細
- 3日ルール判定（件数のみ）: 判定1銘柄・streak≥3 0・streak=2 0・判定不可0（銘柄別は通知にのみ）
- 検知内訳: 候補104銘柄（新規9・再指名95）・プール511・評価511・SKIP0・日足取得失敗0・未マージPR由来0
- gate_history: gate_history/2026-11-11.json を新規作成（verdicts 511・nominations 104）
- grades.json: 1084銘柄 / 618739 バイト・nx 付与508件・pxd 368件・gyf 非null211（[] 53）・trp 非null20
- method_score: 保持78件/null433件
- ヘッドライン付与: PASS240件中240件（欠落0）・抜粋（通知）10件（method3/ai3/granville2/changepoint2）
- kabutan トップページ新規取得 5件（単元株数・業態確認。50件上限で打ち切り0件）・業種埋め戻し 0件（対象なし）
- profile_cache: 総数1053・本夜の追加0件・業種追加0件・業態「未取得」のまま出た件数 5
- earnings_log: 総数356・本夜追記49件・リターン補完54件・日足が取れず未補完68件
- gyoseki_cache: history 退避0件（本夜は業績再計算を行わず。📊/📢/📉検出銘柄は recalc_queue へ追加 49件）
- pool_bars.json: 513銘柄 / 447259 バイト（1306 を含む）
- 鮮度ゲート: 提案154件／鮮度切れ除外45件・nom_age分布 0-2:174/3-10:216/11+:121・last_seen欠損0件
- 記録の凍結: gate_history verdicts 511件（＝評価511件）・nominations 104件（新規9・再指名95）・業種 付与済み503／未付与8・本夜の埋め戻し0件
- トレンド文脈: ctx 合致83／不一致304／レンジ121／判定不能3・PASS のうち ctx 合致30件・形態が付いた銘柄172件
- 入口の穴（v1.48）: recent_pass 543銘柄（🚨44/📉49/⏰90/📋10/❓301・当夜評価外135）・PASS_DOJI 3件（⏳確認足待ち1／⛔提案なし(指名鮮度切れ 13営業日)1／⛔提案なし(材料後出し)1）・⏸位置不適 12件（momentum12/oshime0）・⏸トラップ疑い 1件・位置判定不能 0件・1306 取得 可・rs20 付与 511/511・⚠市場に劣後 6件／ℹ相対強い 2件
- 業種別PER中央値: 算出できた業種26・spm を写せた銘柄1009件
- 開示の分類別件数（プール在籍・1銘柄1分類）: 📊48 📌25 🔁2 📢1
- 熟成由来の候補 0件（うちPASS0）
- 権利情報: T+1/T+2 に権利落ちが無いため rights_cache は本夜未更新・優待ページ取得0件
- 次回決算日: 付与511件／未発表（nx null）577件・前年同期発表日 付与368件・earnings_calendar.json 1088銘柄/147393バイト
- 値頃感: 当日終値で再計算236件・静的層なしで未評価4件
- 提案: 型別 {'momentum': 24, 'reversal': 127, 'oshime': 2, 'changepoint': 1}
- STEP 4.8 週末ブリーフ: スキップ（week_open=false）
- 📑指数: ix 付与 プール91件（out79/in12）
- master.json の変更行数: +26160/-21619
