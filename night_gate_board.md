# 夜間ゲート 2026-11-12

## サマリー
- 評価数: 522 / PASS: 100（PASS_DOJI 2件を含む）
- 発注可能提案数: 57件（✅49／⏳0／⏸位置不適8／⏸トラップ疑い0）
- 市場一言: 市場モード「強気ギャップアップ」（market.latest 2026-11-12）。プール522銘柄中 PASS比率19.2%（陰線FAIL 329件・上髭FAIL 93件）。寄り高→引けにかけて売られた銘柄が多い
- 実行モード: 通常（base_day=当日の引け値を対象）
- base_day: 2026-11-12（run_at 2026-11-12 20:30起動）
- week_open: false（翌営業日 11/13(金)＝週初でない）→ STEP 4.8 週末ブリーフはスキップ
- 📆 翌営業日 11/13: マイナーSQ（T+2 11/16: カレンダーイベントなし）
- 📑指数: 低減対象 提案6件／PASS12件／プール80件・新規採用 12件（index_flags 2026-10-07 公表分）・次の TOPIX 低減日 01/29 第2回/8（あと52営業日）

## 検証結果
- V1 → はい（提案57=results57=模擬57=通知母数57）
- V2 → はい（PASS100=提案57+除外43・order_status欠落0）
- V3 → はい（results522件重複0）
- V4 → はい（既存static変更0）
- V5 → はい（変更トップキー['earnings_log', 'night_gate', 'pipeline', 'profile_cache', 'valuation_cache']・pipeline他run不変True・spec不変True・profile既存書換なしTrue）
- V6 → はい（gyoseki_cache不整合0）
- V7 → はい（必須セクション存在（week_open=false のためカタリスト節なし））
- V8 → はい（模擬57行 不正0）
- V9 → はい（gate_history と today 一致）
- V10 → はい（base_day一致 2026-11-12）
- V11 → いいえ（+16003/-14660（indent=2・往復一致で検出））
- V12 → はい（並び順 (a)(b)(c) 一致）
- V13 → はい（1090銘柄/610.5KiB・GC∪VC1088全収録True（profile_cache由来+2）・20キーTrue・型True・nx一致True・ix非null224・業種PER中央値26業種）
- V14 → はい（保持61件/null461件・出所不明/不一致0）
- V15 → はい（PASS100件中100件に付与（欠落0）・5キーTrue・(c)4項目の未取得/取得不可16（キャッシュ保存値の転記を含む））
- V16 → はい（📊54件全件記録True・grade_beforeは再計算前（本夜は業績再計算なし）・history>4=0・総数410）
- V17 → はい（524銘柄/446.5KiB・保有1銘柄すべて収録・3日ルール判定1銘柄）
- V18 → はい（鮮度切れ29件・誤除外0・nom_age分布 0-2:170/3-10:228/11+:124）
- V19 → はい（verdicts522=評価522・nominations92（新規11/再指名81）・集合一致True・ctx判定不能3・(d)True）
- V20 → はい（1094銘柄・nx非null487・hist持ち751・pxd369・取得元名称なしTrue）
- V21 → はい（recent_pass556銘柄・出所実在True・保有情報不使用True）
- V22 → はい（PASS_DOJI2・⏸位置不適8誤通過0=True・⏸トラップ0・rs20付与522/522）
- VLEAK → はい（公開物（ボード/today/gate_history）への保有情報 検出0件（保有1銘柄・アラート4件（詳細は通知のみ）））

## 保有アラート
保有1銘柄・アラート4件（詳細は通知）

## 🧾直近提案の決算接近
窓内（直近20営業日）の提案銘柄 556・日程不明 349・当夜評価外 126。保有情報は使っていない（候補だった銘柄の日程）
- 🚨決算直前 11/13(残1営業日) 2502 Asahi Group Holdings, Ltd.｜最後の提案 11/12（momentum 1750.5・✅即時可）｜提案1回｜当夜 PASS
- 🚨決算直前 11/13(残1営業日) 3989 シェアテク｜最後の提案 11/12（changepoint 1539・✅即時可）｜提案3回｜当夜 PASS
- 🚨決算直前 11/13(残1営業日) 7744 ノーリツ鋼機｜最後の提案 11/12（momentum 2073・✅即時可）｜提案5回｜当夜 PASS
- 🚨決算直前 11/13(残1営業日) 7747 朝日インテック｜最後の提案 11/12（momentum 3875・✅即時可）｜提案4回｜当夜 PASS
- 🚨決算直前 11/13(残1営業日) 1961 三機工業｜最後の提案 11/11（reversal 2412・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 2962 テクニスコ｜最後の提案 11/11（reversal 1607・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 3374 内外テック｜最後の提案 11/11（reversal 4110・✅即時可）｜提案6回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 3927 アークン｜最後の提案 11/11（momentum 933・⏸位置不適(25MA下 -9.3%／52週 26.3%)）｜提案6回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 4634 ａｒｔｉｅｎｃｅ（ａｒｔｉｅｎ）｜最後の提案 11/11（reversal 4875・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 5027 AnyMind Group Inc.｜最後の提案 11/11（momentum 734・⏸位置不適(25MA下 -4.64%)）｜提案6回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 5844 Kyoto Financial Group,Inc.｜最後の提案 11/11（reversal 4241・✅即時可）｜提案5回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 6268 ナブテスコ｜最後の提案 11/11（reversal 4235・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 6317 Kitagawa Corporation｜最後の提案 11/11（reversal 2293・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 6407 CKD｜最後の提案 11/11（reversal 4139・✅即時可）｜提案5回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 6481 THK Co., Ltd.｜最後の提案 11/11（reversal 5579・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 6742 京三製作所｜最後の提案 11/11（reversal 975・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 6840 ＡＫＩＢＡホールディングス｜最後の提案 11/11（reversal 641・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 6877 ＯＢＡＲＡ　ＧＲＯＵＰ（ＯＢＡＲＡＧ）｜最後の提案 11/11（oshime 6762・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 7322 三十三フィナンシャルグループ｜最後の提案 11/11（reversal 1859・✅即時可）｜提案4回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 7384 Procrea Holdings,Inc.｜最後の提案 11/11（reversal 4130・✅即時可）｜提案9回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 8344 Yamagata Bank, Ltd.｜最後の提案 11/11（reversal 4410・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 8364 清水銀行｜最後の提案 11/11（reversal 2812・✅即時可）｜提案5回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 8366 滋賀銀行｜最後の提案 11/11（reversal 2374・✅即時可）｜提案4回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 8522 Bank of Nagoya, Ltd.｜最後の提案 11/11（reversal 5860・✅即時可）｜提案6回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 8600 トモニホールディングス｜最後の提案 11/11（reversal 1029・✅即時可）｜提案6回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 8714 池田泉州ホールディングス｜最後の提案 11/11（reversal 863・✅即時可）｜提案3回｜当夜 FAIL_UWAHIGE
- 🚨決算直前 11/13(残1営業日) 3556 RenetJapanGroup, Inc.｜最後の提案 11/10（momentum 922・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 3851 日本一ソフトウェア｜最後の提案 11/10（reversal 1162・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 3923 ラクス｜最後の提案 11/10（changepoint 1155.5・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 4011 Headwaters Co.,Ltd｜最後の提案 11/10（changepoint 1927・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 4053 Sun Asterisk, Inc.｜最後の提案 11/10（momentum 579・✅即時可）｜提案5回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 479A PRONI Inc.｜最後の提案 11/10（reversal 1545・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 5137 Smart Drive Co. Ltd.｜最後の提案 11/10（momentum 313・✅即時可）｜提案5回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 5252 日本ナレッジ｜最後の提案 11/10（reversal 931・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 6676 BUFFALO INC.｜最後の提案 11/10（reversal 3180・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 3042 セキュアヴェイル（セキュアヴェ）｜最後の提案 11/09（oshime 891・⏳待機: 到達まで乖離8.7%）｜提案1回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 4058 Toyokumo, Inc.｜最後の提案 11/09（momentum 2189・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 4293 セプテーニ・ホールディングス（セプテニＨＤ）｜最後の提案 11/09（reversal 461・✅即時可）｜提案1回｜当夜 FAIL_UWAHIGE
- 🚨決算直前 11/13(残1営業日) 6191 エボラブルアジア｜最後の提案 11/09（oshime 1433・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 8388 阿波銀行｜最後の提案 11/09（reversal 1760・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 9552 クオンツ総研ホールディングス｜最後の提案 11/09（oshime 1066・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 265A エイチエムコム｜最後の提案 11/06（changepoint 587・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 286A ユカリア｜最後の提案 11/06（changepoint 755・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 6071 IBJ, Inc.｜最後の提案 11/06（momentum 919・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 6227 AIMECHATEC Ltd.｜最後の提案 11/06（reversal 4025・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 6597 HPC SYSTEMS Inc.｜最後の提案 11/06（reversal 2396・✅即時可）｜提案3回｜当夜 評価外
- 🚨決算直前 11/13(残1営業日) 7161 Jimoto Holdings, Inc.｜最後の提案 11/06（momentum 500・✅即時可）｜提案3回｜当夜 評価外
- 🚨決算直前 11/13(残1営業日) 7318 セレンディップ・ホールディングス｜最後の提案 11/06（changepoint 1031・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 7695 交換できるくん｜最後の提案 11/06（changepoint 830・✅即時可）｜提案5回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 5101 Yokohama Rubber Co., Ltd.｜最後の提案 11/05（reversal 7251・✅即時可）｜提案3回｜当夜 FAIL_UWAHIGE
- 🚨決算直前 11/13(残1営業日) 8253 Credit Saison Co., Ltd.｜最後の提案 11/05（reversal 4233・✅即時可）｜提案3回｜当夜 PASS
- 🚨決算直前 11/13(残1営業日) 1860 Toda Corporation｜最後の提案 10/29（reversal 1465.5・✅即時可）｜提案7回｜当夜 PASS
- 🚨決算直前 11/13(残1営業日) 4180 ＡＰＰＩＥＲ　ＧＲＯＵＰ｜最後の提案 10/29（oshime 1412.2・✅即時可）｜提案2回｜当夜 評価外
- 🚨決算直前 11/13(残1営業日) 5757 CK San-Etsu Co., Ltd.｜最後の提案 10/29（momentum 4505.0・✅即時可）｜提案2回｜当夜 FAIL_UWAHIGE
- 🚨決算直前 11/13(残1営業日) 593A ティアフォー｜最後の提案 10/29（changepoint 2364.0・✅即時可）｜提案4回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 6736 Suncorporation｜最後の提案 10/29（oshime 9748.9・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 8360 Yamanashi Chuo Bank, Ltd.｜最後の提案 10/29（reversal 1321.0・✅即時可）｜提案5回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 9553 MicroAd, Inc.｜最後の提案 10/29（momentum 593.0・✅即時可）｜提案6回｜当夜 評価外
- 🚨決算直前 11/13(残1営業日) 3691 DIGITAL PLUS, Inc.｜最後の提案 10/28（reversal 1487.0・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 584A LiNKX, Inc.｜最後の提案 10/27（changepoint 2308.0・✅即時可）｜提案4回｜当夜 評価外
- 🚨決算直前 11/13(残1営業日) 8524 North Pacific Bank, Ltd.｜最後の提案 10/27（reversal 1176.0・✅即時可）｜提案4回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 8713 Fidea Holdings Co.Ltd.｜最後の提案 10/27（reversal 2527.0・✅即時可）｜提案5回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 6203 Howa Machinery, Ltd.｜最後の提案 10/26（reversal 2279.0・✅即時可）｜提案3回｜当夜 FAIL_UWAHIGE
- 🚨決算直前 11/13(残1営業日) 6298 Y.A.C.HOLDINGS CO.,LTD.｜最後の提案 10/26（momentum 1099.0・✅即時可）｜提案3回｜当夜 評価外
- 🚨決算直前 11/13(残1営業日) 8944 Land Business Co., Ltd.｜最後の提案 10/26（momentum 256.0・✅即時可）｜提案2回｜当夜 PASS
- 🚨決算直前 11/13(残1営業日) 9211 f-code Inc.｜最後の提案 10/26（momentum 1204.0・✅即時可）｜提案2回｜当夜 評価外
- 🚨決算直前 11/13(残1営業日) 477A Startline CO.,LTD.｜最後の提案 10/23（reversal 750.0・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 8995 Makoto Construction Co,Ltd｜最後の提案 10/23（reversal 1484.0・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 4493 Cyber Security Cloud, Inc.｜最後の提案 10/22（changepoint 3865・✅即時可）｜提案2回｜当夜 評価外
- 🚨決算直前 11/13(残1営業日) 5038 eWeLL Co.,Ltd｜最後の提案 10/21（momentum 2331.0・✅即時可）｜提案1回｜当夜 評価外
- 🚨決算直前 11/13(残1営業日) 3097 Monogatari Corporation｜最後の提案 10/20（oshime 5520.0・⏳待機: 到達まで乖離-9.4%）｜提案3回｜当夜 評価外
- 🚨決算直前 11/13(残1営業日) 5242 EYEZ INC.｜最後の提案 10/20（reversal 2866.0・✅即時可）｜提案4回｜当夜 評価外
- 🚨決算直前 11/13(残1営業日) 1815 鉄建建設｜最後の提案 10/19（momentum 2191.0・✅即時可）｜提案2回｜当夜 評価外
- 🚨決算直前 11/13(残1営業日) 4691 Washington Hotel Corp.｜最後の提案 10/19（reversal 1913.0・✅即時可）｜提案1回｜当夜 評価外
- 🚨決算直前 11/13(残1営業日) 6254 野村マイクロ・サイエンス｜最後の提案 10/19（changepoint 3160.0・✅即時可）｜提案2回｜当夜 評価外
- 🚨決算直前 11/13(残1営業日) 6379 RAIZNEXT Corporation｜最後の提案 10/19（oshime 1000.0・✅即時可）｜提案2回｜当夜 評価外
- 🚨決算直前 11/13(残1営業日) 6804 Hosiden Corp.｜最後の提案 10/19（reversal 2380.0・✅即時可）｜提案2回｜当夜 FAIL_UWAHIGE
- 🚨決算直前 11/13(残1営業日) 9554 AViC Co. Ltd.｜最後の提案 10/19（momentum 1721.0・✅即時可）｜提案2回｜当夜 評価外
- 🚨決算直前 11/13(残1営業日) 4166 Cacco, Inc.｜最後の提案 10/16（momentum 733.0・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 5892 yutori,Inc.｜最後の提案 10/16（momentum 3180.0・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 🚨決算直前 11/13(残1営業日) 6562 Geniee, Inc.｜最後の提案 10/16（momentum 1005.0・✅即時可）｜提案1回｜当夜 評価外
- 📉決算反応日 11/12 1926 ライト工業（ライト）｜最後の提案 11/12（reversal 1016・✅即時可）｜提案1回｜当夜 PASS
- 📉決算反応日 11/12 4008 住友精化｜最後の提案 11/12（reversal 1377・✅即時可）｜提案1回｜当夜 PASS
- 📉決算反応日 11/12 4396 System Support Holdings Inc.｜最後の提案 11/12（reversal 1315・✅即時可）｜提案1回｜当夜 PASS
- 📉決算反応日 11/12 9006 Keikyu Corporation｜最後の提案 11/12（momentum 1590・✅即時可）｜提案1回｜当夜 PASS
- 📉決算反応日 11/12 9075 福山通運｜最後の提案 11/12（momentum 6440・✅即時可）｜提案1回｜当夜 PASS
- 📉決算反応日 11/12 9956 Valor Holdings Co., Ltd.｜最後の提案 11/12（momentum 1620・⏸位置不適(25MA下 -1.33%／52週 28.2%)）｜提案1回｜当夜 PASS
- 📉決算反応日 11/13 1975 新日本空調｜最後の提案 11/11（momentum 3485・⏸位置不適(25MA下 -6.23%)）｜提案5回｜当夜 FAIL_INSEN
- 📉決算反応日 11/12 1982 日比谷総合設備｜最後の提案 11/11（momentum 3195・⏸位置不適(25MA下 -1.2%)）｜提案4回｜当夜 FAIL_INSEN
- 📉決算反応日 11/13 4419 Finatext Holdings Ltd.｜最後の提案 11/11（reversal 1237・✅即時可）｜提案4回｜当夜 FAIL_INSEN
- 📉決算反応日 11/13 4743 ITFOR Inc.｜最後の提案 11/11（momentum 1585・⏸位置不適(25MA下 -2.11%／52週 23.7%)）｜提案6回｜当夜 PASS
- 📉決算反応日 11/13 6524 湖北工業｜最後の提案 11/11（reversal 4825・✅即時可）｜提案4回｜当夜 FAIL_INSEN
- 📉決算反応日 11/13 6613 QD Laser, Inc.｜最後の提案 11/11（momentum 2222・✅即時可）｜提案4回｜当夜 FAIL_INSEN
- 📉決算反応日 11/13 6862 ミナト HD｜最後の提案 11/11（reversal 3360・✅即時可）｜提案5回｜当夜 FAIL_INSEN
- 📉決算反応日 11/13 6918 アバールデータ｜最後の提案 11/11（reversal 3270・✅即時可）｜提案5回｜当夜 FAIL_INSEN
- 📉決算反応日 11/13 7433 Hakuto Co., Ltd.｜最後の提案 11/11（reversal 1615・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- 📉決算反応日 11/13 8345 Bank of Iwate Ltd.｜最後の提案 11/11（reversal 2128・✅即時可）｜提案8回｜当夜 FAIL_INSEN
- 📉決算反応日 11/13 8381 San-in Godo Bank Ltd.｜最後の提案 11/11（reversal 2190.5・✅即時可）｜提案4回｜当夜 FAIL_INSEN
- 📉決算反応日 11/13 8551 北日本銀行｜最後の提案 11/11（reversal 2373・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- 📉決算反応日 11/13 1435 robot home Inc.｜最後の提案 11/10（momentum 164・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 📉決算反応日 11/12 147A SORACOM,INC.｜最後の提案 11/10（momentum 939・✅即時可）｜提案1回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/13 150A ＪＳＨ｜最後の提案 11/10（reversal 624・✅即時可）｜提案4回｜当夜 FAIL_INSEN
- 📉決算反応日 11/12 4071 Plus Alpha Consulting Co. LTD.｜最後の提案 11/10（changepoint 2318・✅即時可）｜提案3回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/13 4165 PLAID Inc.｜最後の提案 11/10（changepoint 760・✅即時可）｜提案1回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/12 4966 上村工業｜最後の提案 11/10（reversal 17270・✅即時可）｜提案4回｜当夜 FAIL_INSEN
- 📉決算反応日 11/12 5019 出光興産｜最後の提案 11/10（reversal 1290・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 📉決算反応日 11/12 6027 Bengo4.com, Inc.｜最後の提案 11/10（oshime 4890・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- 📉決算反応日 11/12 6284 日精エー・エス・ビー機械｜最後の提案 11/10（reversal 7850・✅即時可）｜提案6回｜当夜 FAIL_INSEN
- 📉決算反応日 11/12 6570 Kyowa Corporation Co. Ltd.｜最後の提案 11/10（oshime 4290・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 📉決算反応日 11/12 1963 日揮ホールディングス｜最後の提案 11/09（reversal 2051.5・✅即時可）｜提案5回｜当夜 FAIL_INSEN
- 📉決算反応日 11/12 2897 Nissin Foods Holdings Co., Ltd.｜最後の提案 11/09（momentum 3171・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 📉決算反応日 11/12 3405 クラレ｜最後の提案 11/09（momentum 1897・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 📉決算反応日 11/12 4980 Dexerials Corp.｜最後の提案 11/09（reversal 2385.5・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 📉決算反応日 11/13 6490 ＰＩＬＬＡＲ｜最後の提案 11/09（reversal 8770・✅即時可）｜提案6回｜当夜 FAIL_INSEN
- 📉決算反応日 11/12 7186 横浜フィナンシャルグループ｜最後の提案 11/09（reversal 1662.5・✅即時可）｜提案6回｜当夜 FAIL_INSEN
- 📉決算反応日 11/13 7715 長野計器｜最後の提案 11/09（reversal 3190・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 📉決算反応日 11/12 8151 東陽テクニカ｜最後の提案 11/09（changepoint 1668・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 📉決算反応日 11/13 8804 東京建物｜最後の提案 11/09（momentum 3371・✅即時可）｜提案1回｜当夜 PASS
- 📉決算反応日 11/13 167A リョーサン菱洋ホールディングス（リョー菱ＨＤ）｜最後の提案 11/06（reversal 2956・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 📉決算反応日 11/12 255A GLテクノHD｜最後の提案 11/06（reversal 3940・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 📉決算反応日 11/12 3436 SUMCO｜最後の提案 11/06（reversal 1784.5・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 📉決算反応日 11/12 4022 ラサ工業｜最後の提案 11/06（reversal 1182・✅即時可）｜提案1回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/12 421A Movin' Strategic Career CO.,LTD.｜最後の提案 11/06（momentum 3335・✅即時可）｜提案4回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/12 4401 ＡＤＥＫＡ｜最後の提案 11/06（momentum 4068・✅即時可）｜提案2回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/12 4971 メック｜最後の提案 11/06（reversal 4925・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 📉決算反応日 11/13 598A チャットプラス｜最後の提案 11/06（changepoint 950・✅即時可）｜提案4回｜当夜 FAIL_INSEN
- 📉決算反応日 11/13 6055 Japan Material Co., Ltd.｜最後の提案 11/06（reversal 1623・✅即時可）｜提案5回｜当夜 FAIL_INSEN
- 📉決算反応日 11/12 6278 ユニオンツール｜最後の提案 11/06（reversal 9750・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 📉決算反応日 11/12 7167 めぶきフィナンシャルグループ｜最後の提案 11/06（reversal 1375・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 📉決算反応日 11/13 3591 WACOAL HOLDINGS CORP｜最後の提案 11/05（reversal 3919・✅即時可）｜提案4回｜当夜 PASS
- 📉決算反応日 11/12 5711 三菱マテリアル｜最後の提案 11/04（reversal 4193・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 📉決算反応日 11/12 5838 Rakuten Bank, Ltd.｜最後の提案 11/04（momentum 6028・✅即時可）｜提案5回｜当夜 FAIL_INSEN
- 📉決算反応日 11/12 4100 Toda Kogyo Corp.｜最後の提案 11/02（reversal 1757・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- 📉決算反応日 11/12 4478 freee K.K.｜最後の提案 11/02（changepoint 4645・✅即時可）｜提案4回｜当夜 PASS_DOJI
- 📉決算反応日 11/13 7734 Riken Keiki Co., Ltd.｜最後の提案 11/02（momentum 3480・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 📉決算反応日 11/12 7806 MTG Co., Ltd.｜最後の提案 11/02（oshime 8756・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 📉決算反応日 11/12 8304 あおぞら銀行｜最後の提案 11/02（reversal 2981・✅即時可）｜提案4回｜当夜 FAIL_INSEN
- 📉決算反応日 11/13 1719 HAZAMA ANDO Corporation｜最後の提案 10/29（reversal 1759.5・✅即時可）｜提案5回｜当夜 PASS
- 📉決算反応日 11/13 1952 Shin Nippon Air Technologies Co., Ltd.｜最後の提案 10/29（reversal 3065.0・✅即時可）｜提案5回｜当夜 PASS
- 📉決算反応日 11/13 3040 ソリトンシステムズ｜最後の提案 10/29（oshime 3051.2・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 📉決算反応日 11/13 3496 アズーム｜最後の提案 10/29（momentum 4810.0・✅即時可）｜提案4回｜当夜 FAIL_INSEN
- 📉決算反応日 11/12 4933 I-ne CO., LTD.｜最後の提案 10/29（momentum 2479.0・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 📉決算反応日 11/12 5184 ニチリン｜最後の提案 10/29（momentum 4185.0・✅即時可）｜提案1回｜当夜 PASS
- 📉決算反応日 11/13 5537 AlbaLink Co.,Ltd.｜最後の提案 10/29（momentum 3405.0・✅即時可）｜提案4回｜当夜 FAIL_INSEN
- 📉決算反応日 11/12 6324 Harmonic Drive Systems Inc.｜最後の提案 10/29（reversal 5480.0・✅即時可）｜提案4回｜当夜 FAIL_INSEN
- 📉決算反応日 11/12 8399 琉球銀行｜最後の提案 10/29（reversal 2868.0・✅即時可）｜提案6回｜当夜 FAIL_INSEN
- 📉決算反応日 11/13 4377 ONE CAREER Inc.｜最後の提案 10/28（momentum 2509.0・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 📉決算反応日 11/13 1861 Kumagai Gumi Co., Ltd.｜最後の提案 10/27（reversal 1246.0・✅即時可）｜提案5回｜当夜 評価外
- 📉決算反応日 11/12 268A Rigaku Holdings Corporation｜最後の提案 10/27（reversal 1485.0・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- 📉決算反応日 11/13 5254 Arent, Inc.｜最後の提案 10/27（momentum 3880.0・✅即時可）｜提案4回｜当夜 FAIL_INSEN
- 📉決算反応日 11/13 5590 NETSTARS Co.,Ltd.｜最後の提案 10/27（changepoint 656.0・✅即時可）｜提案3回｜当夜 評価外
- 📉決算反応日 11/12 1833 Okumura Corporation｜最後の提案 10/26（reversal 5350.0・✅即時可）｜提案1回｜当夜 評価外
- 📉決算反応日 11/13 7567 Sakae Electronics Corp.｜最後の提案 10/26（momentum 635.0・✅即時可）｜提案3回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/12 2820 Yamami Co.｜最後の提案 10/23（momentum 6580.0・✅即時可）｜提案2回｜当夜 評価外
- 📉決算反応日 11/13 3993 PKSHA Technology, Inc.｜最後の提案 10/23（changepoint 3700.0・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- 📉決算反応日 11/12 4259 ExaWizards Inc.｜最後の提案 10/23（changepoint 753.0・✅即時可）｜提案3回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/13 558A SQUEEZE Inc.｜最後の提案 10/23（momentum 5890.0・✅即時可）｜提案2回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/13 1662 Japan Petroleum Exploration Co., Ltd.｜最後の提案 10/22（reversal 1715・✅即時可）｜提案3回｜当夜 評価外
- 📉決算反応日 11/13 5034 unerry, Inc.｜最後の提案 10/22（momentum 2841・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- 📉決算反応日 11/12 4544 H.U.Group Holdings, Inc.｜最後の提案 10/20（momentum 3720.0・✅即時可）｜提案3回｜当夜 評価外
- 📉決算反応日 11/13 8066 Mitani Corporation｜最後の提案 10/19（reversal 3140.0・✅即時可）｜提案1回｜当夜 評価外
- 📉決算反応日 11/13 8511 Japan Securities Finance Co., Ltd.｜最後の提案 10/19（reversal 2217.0・✅即時可）｜提案1回｜当夜 評価外
- 📉決算反応日 11/12 2980 SRE Holdings Corp.｜最後の提案 10/16（momentum 2398.0・✅即時可）｜提案1回｜当夜 評価外
- 📉決算反応日 11/13 3696 セレス｜最後の提案 10/16（momentum 2397.0・✅即時可）｜提案1回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/13 4044 Central Glass Co., Ltd.｜最後の提案 10/16（oshime 4510・✅即時可）｜提案1回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/12 4183 Mitsui Chemicals, Inc.｜最後の提案 10/16（momentum 2108.0・✅即時可）｜提案1回｜当夜 評価外
- 📉決算反応日 11/12 4331 Take and Give. Needs Co., Ltd.｜最後の提案 10/16（momentum 834.0・✅即時可）｜提案1回｜当夜 評価外
- 📉決算反応日 11/13 4488 AI inside Inc.｜最後の提案 10/16（changepoint 2116.0・✅即時可）｜提案1回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/13 5036 Japan Business Systems, Inc.｜最後の提案 10/16（momentum 1898.0・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 📉決算反応日 11/13 2874 YOKOREI CO. LTD.｜最後の提案 10/15（reversal 1761.0・✅即時可）｜提案1回｜当夜 評価外
- 📉決算反応日 11/13 9900 Sagami Holdings Corp.｜最後の提案 10/15（oshime 1096・✅即時可）｜提案1回｜当夜 評価外
- ⏰決算 11/16(残2営業日) 6890 Ferrotec Corporation｜最後の提案 11/11（reversal 7617・✅即時可）｜提案4回｜当夜 FAIL_INSEN
- ⏰決算 11/16(残2営業日) 478A Hutzper Inc.｜最後の提案 11/10（changepoint 668・✅即時可）｜提案5回｜当夜 FAIL_INSEN
- ⏰決算 11/16(残2営業日) 5105 ＴＯＹＯ　ＴＩＲＥ｜最後の提案 11/09（momentum 4249・✅即時可）｜提案2回｜当夜 PASS
- ⏰決算 11/16(残2営業日) 5582 （名称取得不可）｜最後の提案 10/29（changepoint 1819.0・✅即時可）｜提案4回｜当夜 FAIL_INSEN
- ⏰決算 11/19(残5営業日) 8986 Daiwa Securities Living Investment Corporation｜最後の提案 10/26（reversal 83900.0・✅即時可）｜提案2回｜当夜 評価外
- ⏰決算 11/16(残2営業日) 7047 PORT INC.｜最後の提案 10/19（momentum 2172.0・✅即時可）｜提案1回｜当夜 評価外
- ⏰決算 11/16(残2営業日) 4346 NEXYZ.Group Corporation｜最後の提案 10/16（reversal 750.0・✅即時可）｜提案2回｜当夜 評価外
- ⏰決算 11/16(残2営業日) 8952 Japan Real Estate Investment Corp.｜最後の提案 10/15（reversal 107800.0・✅即時可）｜提案1回｜当夜 評価外
- 📋カルテ窓 12/11(残20営業日) 446A ノースサンド｜最後の提案 11/12（momentum 2404・⏸位置不適(25MA下 -10.65%)）｜提案3回｜当夜 PASS
- 📋カルテ窓 12/11(残20営業日) 218A Liberaware｜最後の提案 11/11（changepoint 830・✅即時可）｜提案6回｜当夜 FAIL_INSEN
- 📋カルテ窓 12/10(残19営業日) 3491 ＧＡ　ｔｅｃｈｎｏｌｏｇｉｅｓ（ＧＡテクノ）｜最後の提案 11/11（momentum 1568・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- 📋カルテ窓 12/11(残20営業日) 6336 石井表記｜最後の提案 11/11（reversal 1266・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- 📋カルテ窓 12/08(残17営業日) 9824 泉州電業｜最後の提案 11/11（momentum 7880・⏸位置不適(25MA下 -2.36%)）｜提案6回｜当夜 FAIL_INSEN
- 📋カルテ窓 12/08(残17営業日) 1436 GreenEnergy & Company｜最後の提案 11/10（reversal 1368・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 📋カルテ窓 12/04(残15営業日) 436A サイバーソリューションズ（サイバＳＯＬ）｜最後の提案 11/10（oshime 1776・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 📋カルテ窓 12/09(残18営業日) 7678 ASAKUMA CO.,LTD.｜最後の提案 11/10（momentum 4405・✅即時可）｜提案6回｜当夜 FAIL_UWAHIGE
- 📋カルテ窓 12/10(残19営業日) 1928 積水ハウス｜最後の提案 11/09（momentum 3568・✅即時可）｜提案2回｜当夜 FAIL_UWAHIGE
- 📋カルテ窓 12/11(残20営業日) 4075 ブレインズテクノロジー｜最後の提案 11/09（reversal 1037・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- 📋カルテ窓 12/09(残18営業日) 5132 pluszero,Inc.｜最後の提案 11/04（momentum 1761・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 📋カルテ窓 12/11(残20営業日) 3653 Morpho, Inc.｜最後の提案 10/29（reversal 918.0・✅即時可）｜提案5回｜当夜 評価外
- 📋カルテ窓 12/10(残19営業日) 8927 Meiho Enterprise Co., Ltd.｜最後の提案 10/29（momentum 466.0・✅即時可）｜提案1回｜当夜 評価外
- 📋カルテ窓 12/11(残20営業日) 186A Astroscale Holdings Inc.｜最後の提案 10/27（momentum 1084.0・✅即時可）｜提案4回｜当夜 評価外
- 📋カルテ窓 12/11(残20営業日) 456A Human Made Inc.｜最後の提案 10/27（oshime 1940.0・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 📋カルテ窓 12/11(残20営業日) 4382 HEROZ, Inc.｜最後の提案 10/21（changepoint 1631.0・✅即時可）｜提案2回｜当夜 FAIL_UWAHIGE
- 📋カルテ窓 12/07(残16営業日) 7856 HAGIHARA INDUSTRIES INC.｜最後の提案 10/19（oshime 2044.0・✅即時可）｜提案2回｜当夜 評価外
- 📋カルテ窓 12/11(残20営業日) 9556 INTLOOP, Inc.｜最後の提案 10/16（momentum 2267.0・✅即時可）｜提案1回｜当夜 評価外

## 前夜の結果
PL5口座への正式な反映は週次①-11の採点で行われる。ここは参考情報。
前夜2026-11-11 の提案154件 → 約定139・不約定15・判定不能0（判定日 2026-11-12）
- 9204 momentum 注文477 → 約定477・終値491（+2.94%）
- 8056 momentum 注文4660 → 約定4699・終値4,830（+2.79%）
- 9960 reversal 注文4385 → 約定4355・終値4,465（+2.53%）
- 6370 reversal 注文5445 → 約定5445・終値5,578（+2.44%）
- 4471 reversal 注文1510 → 約定1498・終値1,524（+1.74%）
- （下位）8551 reversal 注文2373 → 約定2365・終値2,214（-6.38%）
- （下位）4062 reversal 注文6920 → 約定6833・終値6,344（-7.16%）
- （下位）3110 reversal 注文2802 → 約定2802・終値2,591（-7.53%）
- 約定139件の含み損益 中央値 -0.98%

## 模擬テンプレ
```
# base_day 2026-11-12 ／ 提案57件
# 使い方: 参戦する0〜3銘柄の行だけをコピーし、｜の後ろに参戦理由を書いてポジション株PJへ送る。
# 選ばなかった行は送らなくてよい（全行に理由を書く必要はない）。見送りは末尾の1行で足りる。
# 特定銘柄を理由つきで見送る場合のみ『模擬 見送り {code} ｜{理由}』を送る。
模擬 3798 kenmo_momentum 逆指値493 SL462.5 単元100 ｜
模擬 446A kenmo_newhigh 逆指値2404 SL2258.8 単元100 ｜
模擬 7733 choruko_reversal 指値1790.5 SL1728.5 単元100 ｜
模擬 8133 choruko_reversal 指値2055 SL1966 単元100 ｜
模擬 3116 choruko_reversal 指値2070 SL1997 単元100 ｜
模擬 8098 choruko_reversal 指値4355 SL4060 単元100 ｜
模擬 1721 choruko_reversal 指値5240 SL4767 単元100 ｜
模擬 1926 choruko_reversal 指値1016 SL878 単元100 ｜
模擬 9302 choruko_reversal 指値3201 SL3079 単元100 ｜
模擬 1417 choruko_reversal 指値3400 SL2995.5 単元100 ｜
模擬 5602 choruko_reversal 指値1456 SL1373 単元100 ｜
模擬 6741 choruko_reversal 指値1667 SL1508 単元100 ｜
模擬 1979 choruko_reversal 指値3395 SL3245 単元100 ｜
模擬 4008 choruko_reversal 指値1377 SL1327 単元100 ｜
模擬 6632 choruko_reversal 指値826 SL777 単元100 ｜
模擬 6370 choruko_reversal 指値5578 SL4678 単元100 ｜
模擬 6436 choruko_reversal 指値3489 SL3398 単元100 ｜
模擬 2109 choruko_reversal 指値3600 SL3490 単元100 ｜
模擬 3612 choruko_reversal 指値1498 SL1435 単元100 ｜
模擬 8975 choruko_reversal 指値86700 SL84600 単元1 ｜
模擬 8698 choruko_reversal 指値600 SL576 単元100 ｜
模擬 3131 ai_reversal 指値7310 SL4040 単元100 ｜
模擬 2502 granville_tenkan 逆指値1750.5 SL1644.5 単元100 ｜
模擬 4523 granville_tenkan 逆指値5180 SL4859.8 単元100 ｜
模擬 8697 granville_tenkan 逆指値2205 SL2071.8 単元100 ｜
模擬 9006 granville_tenkan 逆指値1590 SL1493.7 単元100 ｜
模擬 7744 granville_tenkan 逆指値2073 SL1947.7 単元100 ｜
模擬 9075 granville_tenkan 逆指値6440 SL6044.2 単元100 ｜
模擬 4507 granville_tenkan 逆指値3147 SL2953.5 単元100 ｜
模擬 1941 granville_tenkan 逆指値5170 SL4850.4 単元100 ｜
模擬 4848 granville_tenkan 逆指値1836 SL1724.9 単元100 ｜
模擬 4554 granville_tenkan 逆指値1888 SL1773.8 単元100 ｜
模擬 9842 granville_tenkan 逆指値1918 SL1802 単元100 ｜
模擬 8016 granville_tenkan 逆指値788 SL739.8 単元100 ｜
模擬 7747 granville_tenkan 逆指値3875 SL3637.8 単元100 ｜
模擬 4568 granville_tenkan 逆指値2865 SL2692.2 単元100 ｜
模擬 417A granville_tenkan 逆指値1919 SL1802.9 単元100 ｜
模擬 2488 granville_tenkan 逆指値1392 SL1307.5 単元100 ｜
模擬 7269 granville_tenkan 逆指値2203.5 SL2070.3 単元100 ｜
模擬 6592 granville_tenkan 逆指値1805 SL1695.8 単元100 ｜
模擬 8160 granville_tenkan 逆指値2511 SL2359.4 単元100 ｜
模擬 8056 granville_tenkan 逆指値4846 SL4550.5 単元100 ｜
模擬 9956 granville_tenkan 逆指値1620 SL1521.9 単元100 ｜
模擬 4540 granville_tenkan 逆指値3919 SL3679.2 単元100 ｜
模擬 9045 granville_tenkan 逆指値3351 SL3145.2 単元100 ｜
模擬 8801 granville_tenkan 逆指値1596.5 SL1499.8 単元100 ｜
模擬 5233 granville_tenkan 逆指値4033 SL3786.3 単元100 ｜
模擬 8803 granville_tenkan 逆指値2353 SL2210.9 単元100 ｜
模擬 4922 granville_tenkan 逆指値5909 SL5545.1 単元100 ｜
模擬 4912 granville_tenkan 逆指値2191.5 SL2059.1 単元100 ｜
模擬 1878 granville_tenkan 逆指値3373 SL3165.9 単元100 ｜
模擬 2811 granville_tenkan 逆指値2814 SL2644.2 単元100 ｜
模擬 4396 granville_rebound 指値1315 SL1281 単元100 ｜
模擬 3565 granville_rebound 指値453 SL398 単元100 ｜
模擬 4768 granville_rebound 指値3691 SL3560 単元100 ｜
模擬 8609 granville_rebound 指値1060 SL925 単元100 ｜
模擬 3989 changepoint 指値1539 SL1532 単元100 🔒 ｜
模擬 見送り ｜
```

## PASS内訳
PASS 100件 = 提案 57件（✅即時可49／⏳待機・確認足待ち0／⏸位置不適8／⏸トラップ疑い0） + 除外 43件（型不一致9（うち十字線2）/材料後出し4/鮮度切れ29/その他1）
- 505A Geekly,Inc.: ⛔提案なし(指名鮮度切れ 20営業日)（nom_age 20）
- 4743 ITFOR Inc.: ⛔提案なし(指名鮮度切れ 11営業日)（nom_age 11）
- 8871 GOLDCREST Co., Ltd.: ⛔提案なし(指名鮮度切れ 14営業日)（nom_age 14）
- 3222 United Super Markets Holdings, Inc.: ⛔提案なし(指名鮮度切れ 20営業日)（nom_age 20）
- 4666 Park24 Co., Ltd.: ⛔提案なし(指名鮮度切れ 20営業日)（nom_age 20）
- 1820 Nishimatsu Construction Co., Ltd.: ⛔提案なし(指名鮮度切れ 19営業日)（nom_age 19）
- 3282 Comforia Residential REIT, Inc.: ⛔提案なし(指名鮮度切れ 15営業日)（nom_age 15）
- 6750 エレコム: ⛔提案なし(材料後出し)（nom_age 0）
- 8198 Maxvalu Tokai Co., Ltd.: ⛔提案なし(指名鮮度切れ 19営業日)（nom_age 19）
- 1952 Shin Nippon Air Technologies Co., Ltd.: ⛔提案なし(指名鮮度切れ 19営業日)（nom_age 19）
- 9533 TOHO GAS Co., Ltd.: ⛔提案なし(指名鮮度切れ 15営業日)（nom_age 15）
- 1860 Toda Corporation: ⛔提案なし(指名鮮度切れ 19営業日)（nom_age 19）
- 1719 HAZAMA ANDO Corporation: ⛔提案なし(指名鮮度切れ 19営業日)（nom_age 19）
- 6753 Sharp Corporation: ⛔提案なし(指名鮮度切れ 15営業日)（nom_age 15）
- 7278 Exedy Corporation: ⛔提案なし(材料後出し)（nom_age 0）
- 2379 dip Corporation: ⛔提案なし(指名鮮度切れ 18営業日)（nom_age 18）
- 8253 Credit Saison Co., Ltd.: ⛔提案なし(指名鮮度切れ 15営業日)（nom_age 15）
- 8174 NIPPON GAS Co., Ltd.: ⛔提案なし(指名鮮度切れ 18営業日)（nom_age 18）
- 3591 WACOAL HOLDINGS CORP: ⛔提案なし(指名鮮度切れ 15営業日)（nom_age 15）
- 9766 コナミグループ（コナミＧ）: ⛔提案なし(手法ブランチ不明)（nom_age 0）
- 2802 味の素: ⛔型不一致(十字線: トウバ)（nom_age 2）
- 5302 日本カーボン: ⛔提案なし(指名鮮度切れ 18営業日)（nom_age 18）
- 9434 ソフトバンク: ⛔型不一致: 既に支持帯以下（nom_age 0）
- 8944 Land Business Co., Ltd.: ⛔提案なし(指名鮮度切れ 19営業日)（nom_age 19）
- 8095 Astena Holdings Co.,Ltd.: ⛔提案なし(指名鮮度切れ 21営業日)（nom_age 21）
- 8804 東京建物: ⛔提案なし(材料後出し)（nom_age 3）
- 4169 Enechange Ltd.: ⛔提案なし(指名鮮度切れ 14営業日)（nom_age 14）
- 6412 Heiwa Holdings Inc.: ⛔提案なし(材料後出し)（nom_age 0）
- 4549 Eiken Chemical Co., Ltd.: ⛔提案なし(指名鮮度切れ 16営業日)（nom_age 16）
- 5184 ニチリン: ⛔提案なし(指名鮮度切れ 13営業日)（nom_age 13）
- 5105 ＴＯＹＯ　ＴＩＲＥ: ⛔提案なし(指名鮮度切れ 12営業日)（nom_age 12）
- 7921 ＴＡＫＡＲＡ　＆　ＣＯＭＰＡＮＹ: ⛔提案なし(指名鮮度切れ 12営業日)（nom_age 12）
- 6523 ＰＨＣホールディングス: ⛔型不一致: 既に支持帯以下（nom_age 8）
- 2384 ＳＢＳホールディングス: ⛔型不一致: 既に支持帯以下（nom_age 3）
- 2492 インフォマート（インフォＭＴ）: ⛔型不一致: 既に支持帯以下（nom_age 1）
- 4674 クレスコ: ⛔型不一致: 既に支持帯以下（nom_age 0）
- 9536 SAIBU GAS HOLDINGS CO. LTD.: ⛔提案なし(指名鮮度切れ 14営業日)（nom_age 14）
- 8159 Tachibana Eletech Co., Ltd.: ⛔型不一致: 既に支持帯以下（nom_age 0）
- 9509 Hokkaido Electric Power Company,Incorporated: ⛔提案なし(指名鮮度切れ 17営業日)（nom_age 17）
- 8255 Axial Retailing, Inc.: ⛔提案なし(指名鮮度切れ 19営業日)（nom_age 19）
- 4432 ウイングアーク１ｓｔ: ⛔型不一致: 既に支持帯以下（nom_age 5）
- 3778 SAKURA Internet Inc.: ⛔提案なし(指名鮮度切れ 19営業日)（nom_age 19）
- 4478 freee K.K.: ⛔型不一致(十字線: トウバ)（nom_age 0）

## 5手法銘柄
- 5137 Smart Drive Co. Ltd.｜kenmo_momentum｜🚀確変｜💎割安｜FAIL_INSEN｜297円｜💰3.1万円｜—
- 276A CCReB Advisors Inc.｜kenmo_momentum/granville_oshime｜🚀確変｜🟢値頃｜FAIL_INSEN｜3,890円｜💰40.2万円｜—
- 3556 RenetJapanGroup, Inc.｜kenmo_momentum/granville_tenkan｜🚀確変｜🟢値頃｜FAIL_INSEN｜897円｜💰9.2万円｜—
- 421A Movin' Strategic Career CO.,LTD.｜kenmo_momentum/kenmo_newhigh｜🚀確変｜⚪妥当｜FAIL_UWAHIGE｜3,325円｜💰34.8万円｜—
- 5027 AnyMind Group Inc.｜kenmo_momentum/granville_oshime/granville_rebound/changepoint｜🚀確変｜⚪妥当｜FAIL_INSEN｜724円｜💰7.3万円｜—
- 4053 Sun Asterisk, Inc.｜kenmo_momentum｜🚀確変｜⚪妥当｜FAIL_INSEN｜555円｜💰5.6万円｜—
- 4434 Serverworks Co., Ltd.｜kenmo_momentum/stf_kakuhen/granville_oshime｜🚀確変｜⚪妥当｜FAIL_INSEN｜2,882円｜💰30.6万円｜—
- 5136 tripla Co.,Ltd.｜kenmo_momentum/granville_oshime/changepoint｜🚀確変｜⚪妥当｜FAIL_INSEN｜2,632円｜💰27.4万円｜—
- 5757 CK San-Etsu Co., Ltd.｜kenmo_momentum｜🔥絶好調｜💎割安｜FAIL_UWAHIGE｜4,600円｜💰45.5万円｜—
- 3915 TerraSky Co., Ltd.｜kenmo_momentum｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜2,106円｜💰21.7万円｜—
- 147A SORACOM,INC.｜kenmo_momentum｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜965円｜💰9.4万円｜—
- 4286 CL Holdings Inc.｜kenmo_momentum/kenmo_newhigh｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜1,498円｜💰14.2万円｜—
- 1435 robot home Inc.｜kenmo_momentum｜🔥絶好調｜💎割安｜FAIL_INSEN｜163円｜💰1.6万円｜—｜⚡材料後出し
- 5132 pluszero,Inc.｜kenmo_momentum｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1,735円｜💰17.8万円｜—
- 4377 ONE CAREER Inc.｜kenmo_momentum/granville_oshime/granville_rebound｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜2,342円｜💰23.6万円｜—｜⚡材料後出し
- 5537 AlbaLink Co.,Ltd.｜kenmo_momentum/granville_oshime/granville_rebound｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜3,100円｜💰31.2万円｜—｜⚡材料後出し
- 4771 F&M Co., Ltd.｜kenmo_momentum/kenmo_newhigh｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜3,060円｜💰30.1万円｜—｜🎯2手法一致
- 5821 Hirakawa Hewtech Corp.｜kenmo_momentum｜⚡好調｜💎割安｜FAIL_INSEN｜3,310円｜💰33.2万円｜—
- 9560 PROGRIT, Inc.｜kenmo_momentum｜⚡好調｜🟢値頃｜FAIL_INSEN｜994円｜💰9.9万円｜—｜⚡材料後出し
- 558A SQUEEZE Inc.｜kenmo_momentum｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜5,900円｜💰57.7万円｜—｜⚡材料後出し
- 4058 Toyokumo, Inc.｜kenmo_momentum｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,181円｜💰22.1万円｜—
- 5034 unerry, Inc.｜kenmo_momentum｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,436円｜💰25.1万円｜—｜⚡材料後出し
- 6071 IBJ, Inc.｜kenmo_momentum/kenmo_newhigh｜⚡好調｜⚪妥当｜FAIL_INSEN｜974円｜💰9.9万円｜—
- 7678 ASAKUMA CO.,LTD.｜kenmo_momentum/kenmo_newhigh｜⚡好調｜🔴過熱｜FAIL_UWAHIGE｜4,320円｜💰42.8万円｜—
- 2975 Star Mica Holdings Co., Ltd.｜kenmo_momentum｜⚡好調｜💎割安｜FAIL_INSEN｜1,215円｜💰12.2万円｜—
- 4477 BASE, Inc.｜kenmo_momentum/granville_oshime/granville_rebound｜⚡好調｜⚪妥当｜FAIL_INSEN｜303円｜💰3.1万円｜—
- 262A INTERMESTIC INC.｜kenmo_momentum｜⚡好調｜💎割安｜FAIL_INSEN｜1,668円｜💰16.7万円｜—
- 505A Geekly,Inc.｜kenmo_momentum｜✅順調｜💎割安｜PASS｜1,142円｜💰11.4万円｜⛔提案なし(指名鮮度切れ 20営業日)｜⚠日程不明
  > 【業態】IT・Web・ゲーム業界に特化した人材紹介(転職エージェント)事業を手掛ける。
  > 【いま】終値1,142円・直近5日+0.71%（材料未確認）
  > 【調子】✅順調（4/13） — E軸判定不能(進捗データ不足)・D軸判定不能(四半期データ不足・中立1点)
  > 【水準】💎割安（7.0/7）— PER8.11倍・PEG0.4619・52週14.6% ／ 💰単元11.4万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 20営業日)）
- 3798 ULS Group Incorporated｜kenmo_momentum/granville_tenkan｜✅順調｜💎割安｜PASS｜492円｜💰4.9万円｜momentum 493/SL462.5（⏸位置不適(25MA下 -7.55%／52週 8.4%)）｜📐進捗 遅れ -12.6% 📆SQ
  > 【業態】ITシステムの設計・構築・コンサルを展開。流通・製造・情報サービス業向けが中心。
  > 【いま】終値492円・直近5日-10.05%（材料未確認）
  > 【調子】✅順調（4/13） — ⚠減速・⚠進捗遅れ・⚠下期依存
  > 【水準】💎割安（6.0/7）— PER12.52倍・PEG0.602・52週8.4% ／ 💰単元4.9万円
  > 【戦略】当日高値超えの逆指値493円で順張り参戦を検討。上限497.9円・SL462.5円目安（⏸位置不適(25MA下 -7.55%／52週 8.4%)）
- 4743 ITFOR Inc.｜kenmo_momentum｜✅順調｜💎割安｜PASS｜1,580円｜💰15.8万円｜⛔提案なし(指名鮮度切れ 11営業日)｜📉決算反応日 11/13 📑TOPIX低減対象（次 01/29 第2回/8）｜⚡材料後出し
  > 【業態】未取得（次回以降に取得）
  > 【いま】終値1,580円・直近5日-1.31%・📊FY2026 Q2 Financial Results Briefing Material
  > 【調子】✅順調（4/13） — E軸判定不能(進捗データ不足)
  > 【水準】💎割安（6.0/7）— PER12.3倍・PEG0.5892・52週23% ／ 💰単元15.8万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 11営業日)）
- 3077 Horiifoodservice Co., Ltd.｜kenmo_momentum/granville_rebound｜判定保留(変則決算)｜🟢値頃｜FAIL_INSEN｜1,137円｜💰11.9万円｜—
- 618A KOMPEITO Inc.｜kenmo_momentum/kenmo_newhigh｜取得不可｜⚪妥当｜FAIL_UWAHIGE｜1,985円｜💰19.5万円｜—
- 7567 Sakae Electronics Corp.｜kenmo_newhigh｜🚀確変｜⚪妥当｜FAIL_UWAHIGE｜640円｜💰6.0万円｜—
- 6418 Japan Cash Machine Co., Ltd.｜kenmo_newhigh/granville_oshime｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜1,456円｜💰14.7万円｜—
- 446A ノースサンド｜kenmo_newhigh/granville_oshime｜🔥絶好調｜⚪妥当｜PASS｜2,384円｜💰23.8万円｜momentum 2404/SL2258.8（⏸位置不適(25MA下 -10.65%)）｜📋カルテ窓 12/11(残20営業日) 📆SQ
  > 【業態】ITコンサルティング、ビジネスコンサルティングやNotionサービスの提供などを手掛ける。
  > 【いま】終値2,384円・直近5日-12.39%（材料未確認）
  > 【調子】🔥絶好調（9/13） — D軸判定不能(四半期データ不足・中立1点)・E軸判定不能(進捗データ不足)・⚠進捗遅れ
  > 【水準】⚪妥当（4.0/7）— PER24.11倍・PEG0.3529・52週70% ／ 💰単元23.8万円
  > 【戦略】当日高値超えの逆指値2404円で順張り参戦を検討。上限2428.0円・SL2258.8円目安（⏸位置不適(25MA下 -10.65%)）
- 3696 セレス｜kenmo_newhigh｜🔥絶好調｜💎割安｜FAIL_UWAHIGE｜2,146円｜💰20.8万円｜—
- 2930 北の達人コーポレーション｜kenmo_newhigh｜⚡好調｜🔴過熱｜FAIL_INSEN｜148円｜💰1.5万円｜—
- 4379 Photosynth inc.｜kenmo_newhigh｜⚡好調｜🔴過熱｜FAIL_INSEN｜453円｜💰4.6万円｜—｜⚡材料後出し
- 3843 Freebit Co., Ltd.｜kenmo_newhigh/granville_tenkan｜✅順調｜🟡やや割高｜FAIL_UWAHIGE｜1,995円｜💰19.8万円｜—
- 9204 Skymark Airlines Inc.｜kenmo_newhigh｜🔻悪化｜🔴過熱｜FAIL_UWAHIGE｜491円｜💰4.7万円｜—
- 1960 サンテック｜kenmo_newhigh｜➖横ばい｜🔴過熱｜FAIL_UWAHIGE｜1,858円｜💰18.5万円｜—
- 4933 I-ne CO., LTD.｜kenmo_newhigh｜取得不可｜⚪妥当｜FAIL_INSEN｜2,391円｜💰24.8万円｜—
- 4565 Nxera Pharma Co., Ltd.｜kenmo_newhigh/granville_oshime｜業績データ取得不可(経常益予想非開示)｜🟡やや割高｜FAIL_INSEN｜1,788円｜💰18.0万円｜—
- 6278 ユニオンツール｜choruko_reversal｜🚀確変｜🟢値頃｜FAIL_INSEN｜11,920円｜💰117.7万円｜—
- 5711 三菱マテリアル｜choruko_reversal｜🚀確変｜💎割安｜FAIL_INSEN｜4,390円｜💰41.3万円｜—
- 3036 アルコニックス｜choruko_reversal｜🚀確変｜🟢値頃｜FAIL_INSEN｜3,225円｜💰32.7万円｜—
- 6324 Harmonic Drive Systems Inc.｜choruko_reversal｜🚀確変｜🟢値頃｜FAIL_INSEN｜4,785円｜💰49.9万円｜—
- 7995 Valqua Ltd.｜choruko_reversal/granville_rebound｜🚀確変｜🟢値頃｜FAIL_INSEN｜6,210円｜💰62.6万円｜—
- 6516 Sanyo Denki Co., Ltd.｜choruko_reversal/ai_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜4,580円｜💰46.1万円｜—
- 8336 武蔵野銀行｜choruko_reversal/granville_oshime/granville_rebound｜🔥絶好調｜💎割安｜FAIL_INSEN｜2,548円｜💰25.6万円｜—
- 5344 MARUWA CO., LTD.｜choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜44,930円｜💰458.6万円｜—
- 6645 OMRON Corporation｜choruko_reversal/granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜4,910円｜💰49.4万円｜—
- 4216 ASAHI YUKIZAI CORPORATION｜choruko_reversal｜🔥絶好調｜💎割安｜FAIL_UWAHIGE｜5,790円｜💰57.2万円｜—
- 4471 三洋化成工業｜choruko_reversal/granville_oshime/granville_rebound｜🔥絶好調｜💎割安｜FAIL_UWAHIGE｜1,524円｜💰15.1万円｜—
- 5703 日本軽金属ホールディングス（日軽金ＨＤ）｜choruko_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜2,588円｜💰25.7万円｜—
- 7433 Hakuto Co., Ltd.｜choruko_reversal/ai_reversal/granville_oshime/granville_rebound｜🔥絶好調｜💎割安｜FAIL_INSEN｜1,616円｜💰16.1万円｜—｜⚡材料後出し
- 8084 ＲＹＯＤＥＮ｜choruko_reversal/granville_rebound｜🔥絶好調｜💎割安｜FAIL_UWAHIGE｜2,250円｜💰22.3万円｜—
- 8871 GOLDCREST Co., Ltd.｜choruko_reversal｜🔥絶好調｜💎割安｜PASS｜2,512円｜💰25.1万円｜⛔提案なし(指名鮮度切れ 14営業日)｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8） 📐進捗 上振れ 14.6%
  > 【業態】首都圏基盤のマンション開発・分譲中堅。ファミリー向け展開。少人数効率経営。
  > 【いま】終値2,512円・直近5日-0.83%（材料未確認）
  > 【調子】🔥絶好調（9/13） — 🔼進捗先行・⚠下期依存
  > 【水準】💎割安（6.0/7）— PER8.79倍・PEG0.1334・52週9.7% ／ 💰単元25.1万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 14営業日)）
- 5301 Tokai Carbon Co., Ltd.｜choruko_reversal/granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1,630円｜💰16.7万円｜—
- 6268 ナブテスコ｜choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜4,154円｜💰42.4万円｜—
- 6481 THK Co., Ltd.｜choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜5,487円｜💰55.8万円｜—
- 6588 東芝テック｜choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜2,592円｜💰26.9万円｜—
- 6652 IDEC Corporation｜choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜3,160円｜💰31.6万円｜—
- 6724 セイコーエプソン｜choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜2,842円｜💰28.6万円｜—
- 6925 Ushio Inc.｜choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜3,201円｜💰32.3万円｜—
- 3222 United Super Markets Holdings, Inc.｜choruko_reversal｜🔥絶好調｜🔴過熱｜PASS｜789円｜💰7.9万円｜⛔提案なし(指名鮮度切れ 20営業日)｜⚠日程不明
  > 【業態】イオン系、首都圏の食品スーパー最大手。マルエツ、カスミ、マックスバリュ関東が統合。
  > 【いま】終値789円・直近5日-0.25%（材料未確認）
  > 【調子】🔥絶好調（9/13）
  > 【水準】🔴過熱（2.0/7）— PER1127.14倍・PEG11.8051・52週23.4% ／ 💰単元7.9万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 20営業日)）
- 6875 メガチップス｜choruko_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜8,710円｜💰87.2万円｜—
- 6471 日本精工｜choruko_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜1,012円｜💰10.1万円｜—
- 8386 百十四銀行｜choruko_reversal/granville_rebound｜🔥絶好調｜💎割安｜FAIL_INSEN｜2,834円｜💰28.5万円｜—
- 6754 アンリツ｜choruko_reversal/ai_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜2,396円｜💰24.4万円｜—
- 7731 ニコン｜choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1,632円｜💰16.5万円｜—
- 9902 Nichiden Corporation｜choruko_reversal/granville_oshime｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜2,960円｜💰29.6万円｜—
- 7733 Olympus Corp.｜choruko_reversal｜🔥絶好調｜⚪妥当｜PASS｜1,790円｜💰17.9万円｜reversal 1790.5/SL1728.5（✅即時可）｜⚠日程不明 📐進捗 上振れ 16.6% 📆SQ ℹ相対強い RS20 5.7pt
  > 【業態】内視鏡世界首位。消化器向け高シェア。治療機器など医療関連に集中。
  > 【いま】終値1,790円・直近5日-2.98%（材料未確認）
  > 【調子】🔥絶好調（8/13） — 税引前代替・上方修正済み・🔼進捗先行
  > 【水準】⚪妥当（4.0/7）— PER17.66倍・PEG0.2666・52週53.7% ／ 💰単元17.9万円
  > 【戦略】当日終値1790.5円の指値で反転を取りにいく。SL1728.5円（直近5日安値）
- 4088 Air Water Inc.｜choruko_reversal｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜2,875円｜💰29.0万円｜—
- 8133 伊藤忠エネクス｜choruko_reversal｜🔥絶好調｜🟡やや割高｜PASS｜2,055円｜💰20.6万円｜reversal 2055/SL1966（✅即時可）｜⚠日程不明 📐進捗 上振れ 83.7% 📆SQ
  > 【業態】伊藤忠系の燃料商社最大手。産業用燃料やLPGなど。カーライフ部門が拡大。
  > 【いま】終値2,055円・直近5日-1.44%（材料未確認）
  > 【調子】🔥絶好調（8/13） — 4Q換算（変則決算）・🔼進捗先行
  > 【水準】🟡やや割高（2.0/7）— PER14.07倍・PEG7.5447・52週46.4% ／ 💰単元20.6万円
  > 【戦略】当日終値2055円の指値で反転を取りにいく。SL1966円（直近5日安値）
- 5333 ＮＧＫ｜choruko_reversal/ai_reversal｜⚡好調｜💎割安｜FAIL_INSEN｜4,801円｜💰48.3万円｜—
- 7721 Tokyo Keiki Inc.｜choruko_reversal｜⚡好調｜💎割安｜FAIL_INSEN｜5,280円｜💰54.3万円｜—
- 8154 加賀電子｜choruko_reversal/granville_rebound｜⚡好調｜💎割安｜FAIL_INSEN｜5,180円｜💰51.5万円｜—
- 3433 TOCALO Co., Ltd.｜choruko_reversal/ai_reversal/granville_tenkan｜⚡好調｜🟢値頃｜FAIL_INSEN｜2,610円｜💰26.0万円｜—
- 5186 ニッタ｜choruko_reversal｜⚡好調｜🟢値頃｜FAIL_INSEN｜6,440円｜💰64.3万円｜—
- 8393 Miyazaki Bank Ltd.｜choruko_reversal｜⚡好調｜🟢値頃｜FAIL_INSEN｜2,475円｜💰25.4万円｜—
- 8522 Bank of Nagoya, Ltd.｜choruko_reversal/granville_rebound｜⚡好調｜🟢値頃｜FAIL_INSEN｜5,860円｜💰58.6万円｜—
- 167A リョーサン菱洋ホールディングス（リョー菱ＨＤ）｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜3,115円｜💰30.9万円｜—｜⚡材料後出し
- 6302 住友重機械工業｜choruko_reversal/granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜5,201円｜💰52.4万円｜—
- 6448 ブラザー工業（ブラザー）｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜4,545円｜💰46.0万円｜—
- 3116 Toyota Boshoku Corp.｜choruko_reversal｜⚡好調｜💎割安｜PASS｜2,070円｜💰20.7万円｜reversal 2070/SL1997（✅即時可）｜⚠日程不明 📆SQ
  > 【業態】トヨタ系。アラコ、タカニチと合併。自動車シートとエアフィルターで国内首位。
  > 【いま】終値2,070円・直近5日-2.61%（材料未確認）
  > 【調子】⚡好調（6/13）
  > 【水準】💎割安（7.0/7）— PER8.04倍・PEG0.2754・52週7.7% ／ 💰単元20.7万円
  > 【戦略】当日終値2070円の指値で反転を取りにいく。SL1997円（直近5日安値）
- 5331 ノリタケ｜choruko_reversal/ai_reversal｜⚡好調｜💎割安｜FAIL_INSEN｜3,050円｜💰30.5万円｜—
- 7004 カナデビア｜choruko_reversal｜⚠減速｜💎割安｜FAIL_UWAHIGE｜966円｜💰9.7万円｜—
- 6651 NITTO KOGYO Corporation｜choruko_reversal｜⚡好調｜💎割安｜FAIL_INSEN｜4,215円｜💰41.9万円｜—
- 4205 Zeon Corporation｜choruko_reversal｜⚡好調｜🟢値頃｜FAIL_INSEN｜2,130円｜💰21.0万円｜—
- 4966 上村工業｜choruko_reversal｜⚡好調｜🟢値頃｜FAIL_INSEN｜16,560円｜💰166.7万円｜—
- 5101 Yokohama Rubber Co., Ltd.｜choruko_reversal｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜7,153円｜💰70.9万円｜—
- 5463 丸一鋼管（丸一管）｜choruko_reversal｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜1,661円｜💰16.4万円｜—
- 6473 ジェイテクト｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜2,060円｜💰20.8万円｜—
- 8098 稲畑産業｜choruko_reversal/ai_reversal/granville_oshime｜⚡好調｜⚪妥当｜PASS｜4,355円｜💰43.5万円｜reversal 4355/SL4060（✅即時可）｜🤖AI特需 🔬基板・素材/上流 ⚠日程不明 📐進捗 上振れ 15.9% 📆SQ
  > 【業態】化学専門商社大手。電子材料や合成樹脂に強み。アジアで広域に展開。
  > 【いま】終値4,355円・直近5日+1.63%（材料未確認）
  > 【調子】⚡好調（6/13） — 上方修正済み・🔼進捗先行
  > 【水準】⚪妥当（4.0/7）— PER10.57倍・PEG0.69・52週78.8% ／ 💰単元43.5万円
  > 【戦略】当日終値4355円の指値で反転を取りにいく。SL4060円（直近5日安値）
- 9412 SKY Perfect JSAT Corporation｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜1,766円｜💰18.2万円｜—
- 268A Rigaku Holdings Corporation｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜1,348円｜💰13.8万円｜—｜⚡材料後出し
- 3569 セーレン｜choruko_reversal/granville_tenkan｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜3,605円｜💰35.1万円｜—
- 4634 ａｒｔｉｅｎｃｅ（ａｒｔｉｅｎ）｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜4,870円｜💰48.8万円｜—
- 6845 アズビル｜choruko_reversal｜⚡好調｜🔴過熱｜FAIL_UWAHIGE｜1,547円｜💰15.2万円｜—
- 5444 大和工業｜choruko_reversal｜⚡好調｜💎割安｜FAIL_UWAHIGE｜11,035円｜💰109.5万円｜—
- 8714 池田泉州ホールディングス｜choruko_reversal/granville_oshime｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜851円｜💰8.6万円｜—
- 9934 因幡電機産業｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,666円｜💰26.6万円｜—
- 1721 コムシスホールディングス｜choruko_reversal｜⚡好調｜⚪妥当｜PASS｜5,240円｜💰52.4万円｜reversal 5240/SL4767（✅即時可）｜⚠日程不明 📐進捗 上振れ 14.9% 📆SQ ⚠1単元でリスク枠超過（47300円）
  > 【業態】電気通信工事で首位。日本コムシス中核、NTT向けが過半。携帯各社の工事も。
  > 【いま】終値5,240円・直近5日-3.75%（材料未確認）
  > 【調子】⚡好調（5/13） — 上方修正済み・🔼加速・🔼進捗先行
  > 【水準】⚪妥当（3.0/7）— PER14.95倍・PEG1.6126・52週56% ／ 💰単元52.4万円
  > 【戦略】当日終値5240円の指値で反転を取りにいく。SL4767円（直近5日安値）／⚠1単元リスク47300円（枠超過）
- 1926 ライト工業（ライト）｜choruko_reversal｜⚡好調｜⚪妥当｜PASS｜1,016円｜💰10.2万円｜reversal 1016/SL878（✅即時可）｜📉決算反応日 11/12 📐進捗 上振れ 26.9% 📆SQ ℹ相対強い RS20 9.8pt
  > 【業態】法面吹付け工事大手。地盤改良・薬液注入工事に強み。耐震補強に注力。
  > 【いま】終値1,016円・直近5日+9.25%（材料未確認）
  > 【調子】⚡好調（5/13） — 上方修正済み・⚠減速・🔼進捗先行
  > 【水準】⚪妥当（3.0/7）— PER13.39倍・PEG4.8585・52週73.2% ／ 💰単元10.2万円
  > 【戦略】当日終値1016円の指値で反転を取りにいく。SL878円（直近5日安値）
- 9072 NIKKON Holdings Co., Ltd.｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜4,175円｜💰42.5万円｜—
- 9960 トーテック｜choruko_reversal/ai_momentum｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜4,465円｜💰43.9万円｜—
- 6454 マックス｜choruko_reversal｜⚡好調｜🟡やや割高｜FAIL_UWAHIGE｜1,827円｜💰17.9万円｜—
- 9302 三井倉庫ホールディングス｜choruko_reversal｜⚡好調｜🟡やや割高｜PASS｜3,201円｜💰32.0万円｜reversal 3201/SL3079（✅即時可）｜⚠日程不明 📆SQ
  > 【業態】倉庫業大手。総合物流業務に強み。国際サプライチェーン展開。不動産賃貸が収益。
  > 【いま】終値3,201円・直近5日-0.50%（材料未確認）
  > 【調子】⚡好調（5/13） — 上方修正済み・🔼加速
  > 【水準】🟡やや割高（2.0/7）— PER18.42倍・PEG3.2237・52週9.8% ／ 💰単元32.0万円
  > 【戦略】当日終値3201円の指値で反転を取りにいく。SL3079円（直近5日安値）
- 4666 Park24 Co., Ltd.｜choruko_reversal｜✅順調｜💎割安｜PASS｜1,850円｜💰18.5万円｜⛔提案なし(指名鮮度切れ 20営業日)
  > 【業態】24時間貸駐車場「タイムズパーキング」を主力。カーシェア事業が成長。豪、英国も展開。
  > 【いま】終値1,850円・直近5日-0.43%（材料未確認）
  > 【調子】✅順調（4/13） — E軸判定不能(進捗データ不足)・D軸判定不能(四半期データ不足・中立1点)
  > 【水準】💎割安（7.0/7）— PER7.18倍・PEG0.4589・52週24.5% ／ 💰単元18.5万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 20営業日)）
- 6135 牧野フライス製作所｜choruko_reversal｜✅順調｜💎割安｜FAIL_INSEN｜2,808円｜💰28.1万円｜—
- 1417 MIRAIT ONE Corporation｜choruko_reversal｜✅順調｜🟢値頃｜PASS｜3,400円｜💰34.0万円｜reversal 3400/SL2995.5（✅即時可）｜⚠日程不明 📐進捗 上振れ 59.5% 📆SQ ℹ相対強い RS20 5.5pt ⚠1単元でリスク枠超過（40450円）
  > 【業態】通信工事大手。NTT向け大。西武建設、国際航業を買収。インフラ、デジタル化も。
  > 【いま】終値3,400円・直近5日+5.13%・📌2026年度 第２四半期決算説明会 （動画資料）
  > 【調子】✅順調（4/13） — 🔼加速・🔼進捗先行
  > 【水準】🟢値頃（5.0/7）— PER11.62倍・PEG1.2179・52週29.8% ／ 💰単元34.0万円
  > 【戦略】当日終値3400円の指値で反転を取りにいく。SL2995.5円（直近5日安値）／⚠1単元リスク40450円（枠超過）
- 6340 澁谷工業｜choruko_reversal/granville_oshime/granville_rebound｜✅順調｜🟢値頃｜FAIL_INSEN｜5,040円｜💰50.9万円｜—
- 6674 ジーエス・ユアサ　コーポレーション｜choruko_reversal｜✅順調｜🟢値頃｜FAIL_INSEN｜4,497円｜💰45.9万円｜—
- 8381 San-in Godo Bank Ltd.｜choruko_reversal/granville_rebound｜✅順調｜⚪妥当｜FAIL_INSEN｜2,142円｜💰21.9万円｜—
- 4272 Nippon Kayaku Co., Ltd.｜choruko_reversal/granville_tenkan/granville_oshime｜✅順調｜⚪妥当｜FAIL_UWAHIGE｜1,887円｜💰18.6万円｜—
- 6284 日精エー・エス・ビー機械｜choruko_reversal/changepoint｜✅順調｜⚪妥当｜FAIL_INSEN｜8,700円｜💰79.7万円｜—
- 6923 Stanley Electric Co., Ltd.｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜3,245円｜💰32.5万円｜—
- 7276 Koito Manufacturing Co., Ltd.｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_UWAHIGE｜2,527円｜💰25.0万円｜—
- 1820 Nishimatsu Construction Co., Ltd.｜choruko_reversal｜✅順調｜⚪妥当｜PASS｜5,694円｜💰56.9万円｜⛔提案なし(指名鮮度切れ 19営業日)｜⚠日程不明 📐進捗 上振れ 66.1%
  > 【業態】総合建設会社。ダム・トンネルなど土木に強み。開発事業強化。伊藤忠の持分法。
  > 【いま】終値5,694円・直近5日+4.55%（材料未確認）
  > 【調子】✅順調（4/13） — 質注意・上方修正済み・🔼進捗先行
  > 【水準】⚪妥当（3.0/7）— PER10.46倍・PEG4.6487・52週34.8% ／ 💰単元56.9万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 19営業日)）
- 4042 東ソー｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_UWAHIGE｜2,529円｜💰25.0万円｜—
- 3282 Comforia Residential REIT, Inc.｜choruko_reversal｜✅順調｜🟡やや割高｜PASS｜85,900円｜💰8.6万円｜⛔提案なし(指名鮮度切れ 15営業日)｜⚠日程不明
  > 【業態】東京圏の独身・小家族向け居住用賃貸住宅に投資。運用:東急不動産リート。
  > 【いま】終値85,900円・直近5日-4.13%（材料未確認）
  > 【調子】✅順調（4/13） — 前年同期比（半期決算等・期間が12か月でない）・E軸判定不能(進捗データ不足)・D軸判定不能(四半期データ不足・中立1点)
  > 【水準】🟡やや割高（2.8/7）— PER38.18倍・PEG3.5728・52週3.6% ／ 💰単元8.6万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 15営業日)）
- 8524 North Pacific Bank, Ltd.｜choruko_reversal/granville_rebound｜⚠減速｜🟡やや割高｜FAIL_INSEN｜1,240円｜💰12.5万円｜—
- 4021 Nissan Chemical Corporation｜choruko_reversal｜✅順調｜🟡やや割高｜FAIL_INSEN｜7,053円｜💰70.2万円｜—
- 5631 Japan Steel Works, Ltd.｜choruko_reversal｜✅順調｜🟡やや割高｜FAIL_INSEN｜5,920円｜💰60.1万円｜—
- 6750 エレコム｜choruko_reversal｜✅順調｜🟡やや割高｜PASS｜1,881円｜💰18.8万円｜⛔提案なし(材料後出し)｜📉決算反応日 11/13 📐進捗 上振れ 58.3%｜⚡材料後出し
  > 【業態】PC周辺機器メーカー大手。マウス、キーボード、スマホ・タブレット周辺機器でトップ。ファブレス。
  > 【いま】終値1,881円・直近5日-2.84%・📊Consolidated Financial Results for the First Six Months Ended September 30, 2026
  > 【調子】✅順調（4/13） — 経常減益-1.2%・質注意・🔼進捗先行
  > 【水準】🟡やや割高（2.0/7）— PER13.24倍・PEG—・52週62.4% ／ 💰単元18.8万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 1944 Kinden Corporation｜choruko_reversal｜✅順調｜🟢値頃｜FAIL_UWAHIGE｜5,919円｜💰58.7万円｜—
- 6332 月島ホールディングス｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_UWAHIGE｜2,414円｜💰23.9万円｜—
- 6368 Organo Corp.｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜1,784円｜💰18.0万円｜—
- 8198 Maxvalu Tokai Co., Ltd.｜choruko_reversal｜✅順調｜⚪妥当｜PASS｜3,185円｜💰31.9万円｜⛔提案なし(指名鮮度切れ 19営業日)｜⚠日程不明
  > 【業態】イオン系の食品スーパー。旧ヤオハンを母体に静岡県を中心とする出店。
  > 【いま】終値3,185円・直近5日+0.00%・📌人事異動に関するお知らせ
  > 【調子】✅順調（3/13）
  > 【水準】⚪妥当（4.0/7）— PER10.92倍・PEG1.6191・52週16.4% ／ 💰単元31.9万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 19営業日)）
- 1951 エクシオグループ（エクシオＧ）｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_UWAHIGE｜2,430円｜💰24.0万円｜—
- 1952 Shin Nippon Air Technologies Co., Ltd.｜choruko_reversal｜✅順調｜⚪妥当｜PASS｜3,025円｜💰30.2万円｜⛔提案なし(指名鮮度切れ 19営業日)｜📉決算反応日 11/13
  > 【業態】三井系、空調設備工事会社。原子力空調、微粒子可視化など独自技術注力。
  > 【いま】終値3,025円・直近5日+7.54%・📊[Summary]Consolidated Financial Results for the Six Months Ended September 30, 2026 (Under Japanese GAAP)
  > 【調子】✅順調（3/13） — E軸判定不能(進捗データ不足)
  > 【水準】⚪妥当（3.0/7）— PER10.77倍・PEG2.7619・52週24% ／ 💰単元30.2万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 19営業日)）
- 4028 石原産業｜choruko_reversal｜🔻悪化｜⚪妥当｜FAIL_INSEN｜2,629円｜💰26.2万円｜—
- 5602 栗本鐵工所（栗本鉄）｜choruko_reversal｜✅順調｜⚪妥当｜PASS｜1,456円｜💰14.6万円｜reversal 1456/SL1373（✅即時可）｜⚠日程不明 📆SQ
  > 【業態】鋳鉄管大手。上下水道用ダクタイル鋳鉄管や産業機械を製造する機械メーカー。
  > 【いま】終値1,456円・直近5日-10.51%（材料未確認）
  > 【調子】✅順調（3/13） — 上方修正済み・⚠減速
  > 【水準】⚪妥当（3.0/7）— PER11.22倍・PEG3.3209・52週17.8% ／ 💰単元14.6万円
  > 【戦略】当日終値1456円の指値で反転を取りにいく。SL1373円（直近5日安値）
- 9533 TOHO GAS Co., Ltd.｜choruko_reversal｜🔻悪化｜⚪妥当｜PASS｜1,256円｜💰12.6万円｜⛔提案なし(指名鮮度切れ 15営業日)｜⚠日程不明 📐進捗 遅れ -81.6% ⚠業績基調が下向き（🔻悪化）
  > 【業態】都市ガス大手。愛知、岐阜、三重が拠点。LPGに強み。コージェネ事業に注力。
  > 【いま】終値1,256円・直近5日-4.45%（材料未確認）
  > 【調子】🔻悪化（3/13） — 質注意・⚠進捗遅れ
  > 【水準】⚪妥当（3.0/7）— PER15.78倍・PEG—・52週46.8% ／ 💰単元12.6万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 15営業日)）
- 1860 Toda Corporation｜choruko_reversal｜✅順調｜🟡やや割高｜PASS｜1,472円｜💰14.7万円｜⛔提案なし(指名鮮度切れ 19営業日)｜🚨決算直前 11/13(残1営業日)
  > 【業態】名門で業界準大手。堅実経営。病院・学校に強み。洋上風力発電に注力。
  > 【いま】終値1,472円・直近5日+0.31%（材料未確認）
  > 【調子】✅順調（3/13） — E軸判定不能(当期進捗率取得不可(未算出))・質注意・経常成長率-9.1%
  > 【水準】🟡やや割高（2.0/7）— PER12.45倍・PEG—・52週67% ／ 💰単元14.7万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 19営業日)）
- 1963 日揮ホールディングス｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜2,166円｜💰22.4万円｜—
- 3105 日清紡ホールディングス｜choruko_reversal｜✅順調｜🟡やや割高｜FAIL_INSEN｜1,982円｜💰19.9万円｜—
- 6055 Japan Material Co., Ltd.｜choruko_reversal｜✅順調｜🟡やや割高｜FAIL_INSEN｜1,844円｜💰18.7万円｜—｜⚡材料後出し
- 6741 日本信号｜choruko_reversal｜✅順調｜🟡やや割高｜PASS｜1,667円｜💰16.7万円｜reversal 1667/SL1508（✅即時可）｜⚠日程不明 📐進捗 上振れ 48.5% 📆SQ
  > 【業態】信号最大手。鉄道、交通ともに高シェア。駅改札、ホームドアや駐車場機にも強み。
  > 【いま】終値1,667円・直近5日-2.74%（材料未確認）
  > 【調子】✅順調（3/13） — 質注意・🔼進捗先行
  > 【水準】🟡やや割高（2.0/7）— PER10.41倍・PEG7.7002・52週63.8% ／ 💰単元16.7万円
  > 【戦略】当日終値1667円の指値で反転を取りにいく。SL1508円（直近5日安値）
- 6807 Japan Aviation Electronics Industry, Limited｜choruko_reversal｜✅順調｜🟡やや割高｜FAIL_INSEN｜2,312円｜💰23.2万円｜—
- 7220 Musashi Seimitsu Industry Co., Ltd.｜choruko_reversal｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜2,186円｜💰24.0万円｜—
- 5310 Toyo Tanso Co., Ltd.｜choruko_reversal/ai_reversal｜🔻悪化｜🔴過熱｜FAIL_INSEN｜6,190円｜💰63.1万円｜—
- 6479 ミネベア｜choruko_reversal｜➖横ばい｜💎割安｜FAIL_INSEN｜2,984円｜💰29.7万円｜—
- 1719 HAZAMA ANDO Corporation｜choruko_reversal｜➖横ばい｜⚪妥当｜PASS｜1,822円｜💰18.2万円｜⛔提案なし(指名鮮度切れ 19営業日)｜📉決算反応日 11/13
  > 【業態】総合建設準大手。ダムやトンネルなど大型土木に定評。海外に積極展開。
  > 【いま】終値1,822円・直近5日+2.88%・📊Consolidated Financial Results for the Six Months Ended September 30, 2026 [Japanese GAAP]
  > 【調子】➖横ばい（2/13） — E軸判定不能(進捗データ不足)・質注意
  > 【水準】⚪妥当（3.0/7）— PER12.88倍・PEG12.4882・52週22.8% ／ 💰単元18.2万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 19営業日)）
- 1979 大気社｜choruko_reversal｜➖横ばい｜⚪妥当｜PASS｜3,395円｜💰34.0万円｜reversal 3395/SL3245（✅即時可）｜⚠日程不明 📆SQ
  > 【業態】空調工事大手。自動車塗装設備工事で国内トップ。海外積極展開。
  > 【いま】終値3,395円・直近5日-3.14%（材料未確認）
  > 【調子】➖横ばい（2/13） — 質注意・⚠減速
  > 【水準】⚪妥当（3.0/7）— PER11.74倍・PEG13.8579・52週18% ／ 💰単元34.0万円
  > 【戦略】当日終値3395円の指値で反転を取りにいく。SL3245円（直近5日安値）
- 4008 住友精化｜choruko_reversal｜🔻悪化｜⚪妥当｜PASS｜1,377円｜💰13.8万円｜reversal 1377/SL1327（✅即時可）｜📉決算反応日 11/12 📑TOPIX低減対象（次 01/29 第2回/8） ⚠業績基調が下向き（🔻悪化） 📆SQ
  > 【業態】主力は紙おむつ向け高吸水性樹脂。精密化学、半導体用ガスにも特色。
  > 【いま】終値1,377円・直近5日-2.69%（材料未確認）
  > 【調子】🔻悪化（2/13） — 質注意・上方修正済み・経常減益-26.6%
  > 【水準】⚪妥当（3.0/7）— PER11.01倍・PEG—・52週66.4% ／ 💰単元13.8万円
  > 【戦略】当日終値1377円の指値で反転を取りにいく。SL1327円（直近5日安値）
- 6753 Sharp Corporation｜choruko_reversal｜🔻悪化｜⚪妥当｜PASS｜516円｜💰5.2万円｜⛔提案なし(指名鮮度切れ 15営業日)｜⚠日程不明 ⚠業績基調が下向き（🔻悪化）
  > 【業態】総合家電大手。台湾鴻海の傘下。液晶パネル白物家電主力。デバイス、EVに注力。
  > 【いま】終値516円・直近5日-7.69%・📌Notice Regarding the Transfer of Fixed Assets and Recording of Extraordinary Income
  > 【調子】🔻悪化（2/13） — 進捗モデル値域外・A成長率0以下のためレバレッジ計算不可(C=0)・質注意・経常減益-62.0%・減収・🔼進捗先行
  > 【水準】⚪妥当（3.0/7）— PER13.4倍・PEG—・52週5.3% ／ 💰単元5.2万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 15営業日)）
- 7278 Exedy Corporation｜choruko_reversal｜➖横ばい｜⚪妥当｜PASS｜5,320円｜💰53.2万円｜⛔提案なし(材料後出し)｜⚠日程不明｜⚡材料後出し
  > 【業態】アイシン系でクラッチ首位。自動車用トルクコンバーターが主力。マニュアル部品でも高シェア。
  > 【いま】終値5,320円・直近5日+2.11%・📊(Correction  Correction of Numerical data) Notice concerning Partial Corrections to FY2026 2Q (Semi-annual) Consolidated Financial Results〔IFRS〕
  > 【調子】➖横ばい（2/13） — 進捗判定不能(自動抽出範囲外)・質注意
  > 【水準】⚪妥当（3.0/7）— PER13.67倍・PEG—・52週24.2% ／ 💰単元53.2万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 3445 RS Technologies Co. Ltd.｜choruko_reversal｜➖横ばい｜🟡やや割高｜FAIL_INSEN｜4,635円｜💰47.5万円｜—
- 6366 Chiyoda Corp.｜choruko_reversal｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜736円｜💰7.6万円｜—
- 9722 藤田観光｜choruko_reversal｜➖横ばい｜🔴過熱｜FAIL_INSEN｜2,816円｜💰28.8万円｜—
- 5844 Kyoto Financial Group,Inc.｜choruko_reversal｜🔻悪化｜🔴過熱｜FAIL_INSEN｜4,162円｜💰42.4万円｜—
- 2379 dip Corporation｜choruko_reversal｜⚠減速｜💎割安｜PASS｜1,512円｜💰15.1万円｜⛔提案なし(指名鮮度切れ 18営業日)｜⚠日程不明 ⚠業績基調が下向き（⚠減速）
  > 【業態】求人・転職サイト「バイトル」を運営。派遣会社向け管理システムや業務自動化も展開。
  > 【いま】終値1,512円・直近5日-4.00%（材料未確認）
  > 【調子】⚠減速（1/13） — E軸判定不能(進捗データ不足)・赤字企業(経常赤字)
  > 【水準】💎割安（7.0/7）— PER—倍・PEG—・52週9.1% ／ 💰単元15.1万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 18営業日)）
- 6632 JVCKENWOOD Corporation｜choruko_reversal｜⚠減速｜⚪妥当｜PASS｜826円｜💰8.3万円｜reversal 826/SL777（✅即時可）｜⚠日程不明 ⚠業績基調が下向き（⚠減速） 📆SQ
  > 【業態】ビクターとケンウッドが統合。AV機器、車載、業務用に注力。ドラレコ関連事業を強化。
  > 【いま】終値826円・直近5日-1.78%（材料未確認）
  > 【調子】⚠減速（1/13） — 税引前代替・D軸判定不能(直近Qデータ取得不可)・E軸判定不能(期首・進捗なし)・質注意
  > 【水準】⚪妥当（4.0/7）— PER7.77倍・PEG—・52週7.2% ／ 💰単元8.3万円
  > 【戦略】当日終値826円の指値で反転を取りにいく。SL777円（直近5日安値）
- 1946 Toenec Corporation｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜1,838円｜💰18.6万円｜—
- 4746 東計電算｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_UWAHIGE｜1,779円｜💰17.7万円｜—
- 4980 Dexerials Corp.｜choruko_reversal/ai_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜2,168円｜💰26.0万円｜—｜⚡材料後出し
- 7003 Mitsui ES Holdings Co., Ltd.｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_UWAHIGE｜3,769円｜💰37.6万円｜—
- 5482 Aichi Steel Corporation｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜2,577円｜💰25.8万円｜—
- 6370 栗田工業｜choruko_reversal｜🔻悪化｜🟡やや割高｜PASS｜5,578円｜💰55.8万円｜reversal 5578/SL4678（✅即時可）｜⚠日程不明 📐進捗 遅れ -50.6% ⚠業績基調が下向き（🔻悪化） 📆SQ ⚠1単元でリスク枠超過（90000円）
  > 【業態】総合水処理最大手。超純水供給事業、水処理薬品事業に競争力。海外強化。
  > 【いま】終値5,578円・直近5日+4.11%（材料未確認）
  > 【調子】🔻悪化（1/13） — 経常減益-26.1%・質注意・⚠進捗遅れ
  > 【水準】🟡やや割高（2.0/7）— PER20.44倍・PEG—・52週17.7% ／ 💰単元55.8万円
  > 【戦略】当日終値5578円の指値で反転を取りにいく。SL4678円（直近5日安値）／⚠1単元リスク90000円（枠超過）
- 6436 アマノ｜choruko_reversal｜⚠減速｜🟡やや割高｜PASS｜3,489円｜💰34.9万円｜reversal 3489/SL3398（✅即時可）｜⚠日程不明 ⚠業績基調が下向き（⚠減速） 📆SQ
  > 【業態】就業情報システムは世界高シェア。駐車場管理システムや環境関連システムも拡大。
  > 【いま】終値3,489円・直近5日-4.25%（材料未確認）
  > 【調子】⚠減速（1/13） — 経常減益-11.7%・質注意
  > 【水準】🟡やや割高（2.0/7）— PER16.65倍・PEG—・52週9.9% ／ 💰単元34.9万円
  > 【戦略】当日終値3489円の指値で反転を取りにいく。SL3398円（直近5日安値）
- 6960 Fukuda Denshi Co., Ltd.｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜9,990円｜💰100.3万円｜—
- 9948 Arcs Company, Limited｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_UWAHIGE｜3,665円｜💰36.5万円｜—
- 6804 ホシデン｜choruko_reversal｜🔻悪化｜⚪妥当｜FAIL_UWAHIGE｜2,206円｜💰22.0万円｜—
- 7148 Financial Products Group Co., Ltd.｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_UWAHIGE｜1,407円｜💰14.0万円｜—
- 2109 ＤＭ三井製糖｜choruko_reversal｜⚠減速｜🟡やや割高｜PASS｜3,600円｜💰36.0万円｜reversal 3600/SL3490（✅即時可）｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8） ⚠業績基調が下向き（⚠減速） 📆SQ
  > 【業態】精糖最大手「スプーン印」三井糖と「ばら印」大日明治が統合。食品化学も注力。
  > 【いま】終値3,600円・直近5日-0.28%（材料未確認）
  > 【調子】⚠減速（0/13） — ⚠減速
  > 【水準】🟡やや割高（2.0/7）— PER14.55倍・PEG30.6424・52週58.4% ／ 💰単元36.0万円
  > 【戦略】当日終値3600円の指値で反転を取りにいく。SL3490円（直近5日安値）
- 6349 Komori Corporation｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_UWAHIGE｜1,734円｜💰17.2万円｜—
- 8194 Life Corporation｜choruko_reversal｜⚠減速｜🔴過熱｜FAIL_UWAHIGE｜2,705円｜💰27.0万円｜—
- 3612 WORLD CO.,LTD.｜choruko_reversal｜業績データ取得不可(経常益予想非開示)｜💎割安｜PASS｜1,498円｜💰15.0万円｜reversal 1498/SL1435（✅即時可）｜⚠日程不明 📆SQ
  > 【業態】繊維製品（アパレル・専門店・婦人服関連）
  > 【いま】終値1,498円・直近5日-2.16%（材料未確認）
  > 【調子】業績データ取得不可(経常益予想非開示)（—/13） — 経常欠損
  > 【水準】💎割安（7.0/7）— PER9.07倍・PEG—・52週37.5% ／ 💰単元15.0万円
  > 【戦略】当日終値1498円の指値で反転を取りにいく。SL1435円（直近5日安値）
- 8975 Ichigo Office REIT Investment Corporation｜choruko_reversal｜判定保留(変則決算)｜💎割安｜PASS｜86,700円｜💰8.7万円｜reversal 86700/SL84600（✅即時可）｜📆SQ
  > 【業態】投資は中規模オフィスビル特化型。価値向上修繕も。運用:いちごグループHD系。
  > 【いま】終値86,700円・直近5日-0.12%（材料未確認）
  > 【調子】判定保留(変則決算)（—/13） — 変則決算・四半期不足
  > 【水準】💎割安（7.0/7）— PER11.89倍・PEG0.0583・52週32.4% ／ 💰単元8.7万円
  > 【戦略】当日終値86700円の指値で反転を取りにいく。SL84600円（直近5日安値）
- 8253 Credit Saison Co., Ltd.｜choruko_reversal｜取得不可｜💎割安｜PASS｜4,185円｜💰41.9万円｜⛔提案なし(指名鮮度切れ 15営業日)｜🚨決算直前 11/13(残1営業日)
  > 【業態】信販会社大手。流通系カードで首位。ポイントビジネスに特色。ファイナンス事業も注力。
  > 【いま】終値4,185円・直近5日-1.13%（材料未確認）
  > 【調子】取得不可（—/13） — データ取得不可
  > 【水準】💎割安（6.0/7）— PER7.96倍・PEG—・52週45.3% ／ 💰単元41.9万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 15営業日)）
- 8367 南都銀行｜choruko_reversal/granville_oshime｜業績データ取得不可(売上/経常欠損)｜💎割安｜FAIL_INSEN｜1,786円｜💰18.0万円｜—
- 7381 ＣＣＩグループ｜choruko_reversal/granville_rebound｜業績データ取得不可(売上/経常欠損)｜🟢値頃｜FAIL_INSEN｜1,126円｜💰11.5万円｜—
- 5831 Shizuoka Financial Group, Inc.｜choruko_reversal/granville_rebound｜業績データ取得不可(売上/経常欠損)｜🟢値頃｜FAIL_INSEN｜3,200円｜💰31.8万円｜—
- 6810 Maxell, Ltd.｜choruko_reversal/granville_oshime/granville_rebound｜業績データ取得不可(経常益予想非開示)｜🟢値頃｜FAIL_INSEN｜2,174円｜💰22.1万円｜—
- 7167 めぶきフィナンシャルグループ｜choruko_reversal/granville_rebound｜取得不可｜🟢値頃｜FAIL_INSEN｜1,526円｜💰15.2万円｜—
- 7186 横浜フィナンシャルグループ｜choruko_reversal｜取得不可｜🟢値頃｜FAIL_INSEN｜1,740円｜💰17.7万円｜—
- 8345 Bank of Iwate Ltd.｜choruko_reversal/granville_rebound｜業績データ取得不可(売上/経常欠損)｜🟢値頃｜FAIL_INSEN｜2,103円｜💰21.3万円｜—
- 8359 Hachijuni Nagano Bank, Ltd.｜choruko_reversal/granville_rebound｜業績データ取得不可(売上/経常欠損)｜🟢値頃｜FAIL_INSEN｜2,498円｜💰25.4万円｜—
- 8370 紀陽銀行｜choruko_reversal｜業績データ取得不可(売上/経常欠損)｜🟢値頃｜FAIL_INSEN｜1,521円｜💰15.4万円｜—
- 4293 セプテーニ・ホールディングス（セプテニＨＤ）｜choruko_reversal｜業績データ取得不可(経常益予想非開示)｜⚪妥当｜FAIL_UWAHIGE｜472円｜💰4.7万円｜—
- 7384 Procrea Holdings,Inc.｜choruko_reversal/granville_rebound｜業績データ取得不可(売上/経常欠損)｜⚪妥当｜FAIL_INSEN｜4,030円｜💰41.3万円｜—
- 8174 NIPPON GAS Co., Ltd.｜choruko_reversal｜業績データ取得不可(売上/経常欠損)｜⚪妥当｜PASS｜915円｜💰9.2万円｜⛔提案なし(指名鮮度切れ 18営業日)｜⚠日程不明 📐進捗 上振れ 28.9%
  > 【業態】LPG、都市ガス、電力を販売。関東一円展開。家庭エネ販売一元化。M&Aで拡販。
  > 【いま】終値915円・直近5日+5.54%（材料未確認）
  > 【調子】業績データ取得不可(売上/経常欠損)（—/13） — 売上欠損・🔼進捗先行
  > 【水準】⚪妥当（4.0/7）— PER20.89倍・PEG—・52週39.3% ／ 💰単元9.2万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 18営業日)）
- 8304 あおぞら銀行｜choruko_reversal｜取得不可｜⚪妥当｜FAIL_INSEN｜3,190円｜💰31.8万円｜—
- 8334 Gunma Bank, Ltd.｜choruko_reversal/granville_rebound｜業績データ取得不可(売上/経常欠損)｜⚪妥当｜FAIL_INSEN｜2,569円｜💰26.3万円｜—
- 8354 ふくおかフィナンシャルグループ｜choruko_reversal｜業績データ取得不可(売上/経常欠損)｜⚪妥当｜FAIL_INSEN｜7,194円｜💰72.4万円｜—
- 8366 滋賀銀行｜choruko_reversal/granville_rebound｜取得不可｜⚪妥当｜FAIL_INSEN｜2,360円｜💰23.7万円｜—
- 8399 琉球銀行｜choruko_reversal/granville_rebound｜取得不可｜⚪妥当｜FAIL_INSEN｜2,663円｜💰27.0万円｜—
- 3591 WACOAL HOLDINGS CORP｜choruko_reversal｜🔻悪化｜🟡やや割高｜PASS｜3,665円｜💰36.6万円｜⛔提案なし(指名鮮度切れ 15営業日)｜📉決算反応日 11/13 ⚠業績基調が下向き（🔻悪化）｜⚡材料後出し
  > 【業態】婦人下着最大手。「ワコール」、「ウイング」ブランドなど。傘下に販売のピーチ・ジョン。
  > 【いま】終値3,665円・直近5日-6.48%・📊2027年3月期第2四半期（中間期）決算短信[ＩＦＲＳ]（連結）
  > 【調子】🔻悪化（—/13） — 経常減益-86.8%
  > 【水準】🟡やや割高（2.0/7）— PER100.69倍・PEG—・52週8.7% ／ 💰単元36.6万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 15営業日)）
- 5019 出光興産｜choruko_reversal｜取得不可｜⏸判定不能｜FAIL_INSEN｜1,314円｜💰13.2万円｜—
- 7177 ＧＭＯフィナンシャルホールディングス｜choruko_reversal｜取得不可｜⏸判定不能｜FAIL_INSEN｜1,066円｜💰10.6万円｜—
- 7322 三十三フィナンシャルグループ｜choruko_reversal/granville_rebound｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜1,832円｜💰18.6万円｜—
- 8600 トモニホールディングス｜choruko_reversal｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜1,009円｜💰10.3万円｜—
- 8616 Tokai Tokyo Financial Holdings, Inc.｜choruko_reversal｜業績データ取得不可｜⏸判定不能｜FAIL_UWAHIGE｜778円｜💰7.8万円｜—
- 8698 Monex Group, Inc.｜choruko_reversal｜業績データ取得不可(経常益予想非開示)｜⏸判定不能｜PASS｜600円｜💰6.0万円｜reversal 600/SL576（✅即時可）｜⚠日程不明 📆SQ
  > 【業態】ネット証券。米など海外でも。国内証券はNTTドコモ傘下に。子会社にコインチェック。
  > 【いま】終値600円・直近5日-7.69%（材料未確認）
  > 【調子】業績データ取得不可(経常益予想非開示)（—/13） — 業績データ取得不可(経常益予想非開示)
  > 【水準】⏸判定不能（—/7）— PER—倍・PEG—・52週11.7% ／ 💰単元6.0万円
  > 【戦略】当日終値600円の指値で反転を取りにいく。SL576円（直近5日安値）
- 4410 ハリマ化成グループ（ハリマ化成Ｇ）｜stf_kakuhen｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1,393円｜💰14.2万円｜—
- 6668 ＡＤプラズマ｜stf_kakuhen/granville_oshime｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜3,900円｜💰39.6万円｜—
- 7713 シグマ光機｜stf_kakuhen｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜2,827円｜💰28.9万円｜—
- 5832 ちゅうぎんフィナンシャルグループ（ちゅうぎんＦ）｜stf_kakuhen｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜3,557円｜💰35.8万円｜—
- 5018 ＭＯＲＥＳＣＯ｜stf_kakuhen｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜2,848円｜💰28.7万円｜—
- 5246 ＥＬＥＭＥＮＴＳ｜stf_kakuhen/granville_oshime｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜916円｜💰9.9万円｜—
- 7942 ＪＳＰ｜stf_kakuhen｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜3,140円｜💰31.1万円｜—
- 9962 ミスミグループ本社｜stf_kakuhen/changepoint｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜4,182円｜💰42.7万円｜—
- 3498 霞ヶ関Ｃ｜stf_kakuhen/granville_tenkan｜🔥絶好調｜💎割安｜FAIL_INSEN｜7,300円｜💰74.9万円｜—｜⚡材料後出し
- 9110 ＮＳユナイテッド海運（ユナイテド海）｜stf_kakuhen｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜10,540円｜💰105.4万円｜—
- 3994 マネーフォワード｜stf_kakuhen/changepoint｜🔥絶好調｜🔴過熱｜FAIL_INSEN｜7,286円｜💰78.6万円｜—
- 9766 コナミグループ（コナミＧ）｜stf_kakuhen｜🔥絶好調｜🟡やや割高｜PASS｜28,650円｜💰286.5万円｜⛔提案なし(手法ブランチ不明)｜⚠日程不明
  > 【業態】家庭・携帯用ゲームが主力。スポーツ施設で首位。健康施設、カジノ機など多角化。
  > 【いま】終値28,650円・直近5日-1.16%（材料未確認）
  > 【調子】🔥絶好調（8/13） — 税引前代替・D軸判定不能(直近Qデータ取得不可)・上方修正済み
  > 【水準】🟡やや割高（2.0/7）— PER28.77倍・PEG0.7733・52週94.4% ／ 💰単元286.5万円
  > 【戦略】発注対象外（⛔提案なし(手法ブランチ不明)）
- 6814 古野電｜stf_kakuhen｜⚡好調｜🟢値頃｜FAIL_INSEN｜7,660円｜💰76.9万円｜—
- 4503 アステラス製薬（アステラス）｜stf_kakuhen｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜2,678円｜💰26.3万円｜—
- 5932 三協立山｜stf_kakuhen/granville_oshime｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜726円｜💰7.2万円｜—
- 6758 ソニーグループ｜stf_kakuhen/ai_momentum｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜4,281円｜💰42.0万円｜—
- 3091 ブロンコビリー｜stf_kakuhen/granville_oshime/changepoint｜⚡好調｜🟡やや割高｜FAIL_UWAHIGE｜3,045円｜💰30.4万円｜—
- 3479 ＴＫＰ｜stf_kakuhen/granville_tenkan｜⚡好調｜🔴過熱｜FAIL_INSEN｜2,102円｜💰21.4万円｜—
- 4417 グローバルセキュリティエキスパート（Ｇセキュリ）｜stf_kakuhen｜⚡好調｜🔴過熱｜FAIL_INSEN｜8,470円｜💰84.8万円｜—
- 6505 東洋電機製造｜stf_kakuhen/ai_momentum｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,979円｜💰30.0万円｜—
- 6532 ベイカレント｜stf_kakuhen｜⚡好調｜🟡やや割高｜FAIL_INSEN｜11,660円｜💰119.7万円｜—
- 4176 ココナラ｜stf_kakuhen｜✅順調｜💎割安｜FAIL_INSEN｜272円｜💰2.8万円｜—
- 7366 ＬＩＴＡＬＩＣＯ（りたりこ）｜stf_kakuhen｜業績データ取得不可(経常益予想非開示)｜⚪妥当｜FAIL_INSEN｜2,039円｜💰20.7万円｜—

## グランビル銘柄
- 5254 Arent, Inc.｜granville_tenkan｜🚀確変｜⚪妥当｜FAIL_INSEN｜3,745円｜💰39.2万円｜—｜⚡材料後出し
- 3927 アークン｜granville_tenkan｜🚀確変｜💎割安｜FAIL_INSEN｜900円｜💰9.3万円｜—
- 6768 Tamura Corporation｜granville_tenkan/granville_oshime｜🔥絶好調｜💎割安｜FAIL_INSEN｜709円｜💰7.3万円｜—
- 8944 Land Business Co., Ltd.｜granville_tenkan｜🔥絶好調｜💎割安｜PASS｜250円｜💰2.5万円｜⛔提案なし(指名鮮度切れ 19営業日)｜🚨決算直前 11/13(残1営業日)
  > 【業態】都内中心にマンション、ビルを賃貸、管理。自社開発も。カフェ・レストラン、服飾に進出。
  > 【いま】終値250円・直近5日+3.73%（材料未確認）
  > 【調子】🔥絶好調（10/13） — E軸判定不能(進捗データ不足)・D軸判定不能(四半期データ不足・中立1点)
  > 【水準】💎割安（6.0/7）— PER9.62倍・PEG0.0054・52週21% ／ 💰単元2.5万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 19営業日)）
- 7725 INTER ACTION Corporation｜granville_tenkan｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1,680円｜💰17.4万円｜—
- 5838 Rakuten Bank, Ltd.｜granville_tenkan｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜5,466円｜💰64.2万円｜—
- 3491 ＧＡ　ｔｅｃｈｎｏｌｏｇｉｅｓ（ＧＡテクノ）｜granville_tenkan｜🔥絶好調｜💎割安｜FAIL_INSEN｜1,479円｜💰15.6万円｜—
- 6470 Taiho Kogyo Co., Ltd.｜granville_tenkan｜🔥絶好調｜💎割安｜FAIL_UWAHIGE｜903円｜💰9.2万円｜—
- 6744 能美防災｜granville_tenkan｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜4,555円｜💰45.0万円｜—
- 8012 Nagase & Co., Ltd.｜granville_tenkan｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1,212円｜💰12.1万円｜—
- 2502 Asahi Group Holdings, Ltd.｜granville_tenkan｜🔥絶好調｜⚪妥当｜PASS｜1,748円｜💰17.5万円｜momentum 1750.5/SL1644.5（✅即時可）｜🚨決算直前 11/13(残1営業日) 📐進捗 上振れ 17.5% 📆SQ
  > 【業態】ビール事業大手。傘下にアサヒ飲料、カルピス、ニッカなど。欧州ビール事業は再編。
  > 【いま】終値1,748円・直近5日-1.96%（材料未確認）
  > 【調子】🔥絶好調（8/13） — 税引前代替・🔼加速・🔼進捗先行
  > 【水準】⚪妥当（4.0/7）— PER13.19倍・PEG0.2496・52週77.3% ／ 💰単元17.5万円
  > 【戦略】当日高値超えの逆指値1750.5円で順張り参戦を検討。上限1768.0円・SL1644.5円目安
- 3002 グンゼ｜granville_tenkan｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜4,340円｜💰43.7万円｜—
- 4523 エーザイ｜granville_tenkan｜🔥絶好調｜⚪妥当｜PASS｜5,170円｜💰51.7万円｜momentum 5180/SL4859.8（✅即時可）｜⚠日程不明 📆SQ ⚠1単元でリスク枠超過（32020円）
  > 【業態】製薬大手。神経系と消化器系がん関連に強み。認知症薬分野に進出。
  > 【いま】終値5,170円・直近5日-2.08%（材料未確認）
  > 【調子】🔥絶好調（8/13） — 税引前代替・🔼加速
  > 【水準】⚪妥当（3.0/7）— PER27.92倍・PEG0.619・52週93% ／ 💰単元51.7万円
  > 【戦略】当日高値超えの逆指値5180円で順張り参戦を検討。上限5231.8円・SL4859.8円目安／⚠1単元リスク32020円（枠超過）
- 8697 日本取引所グループ｜granville_tenkan/changepoint｜🔥絶好調｜⚪妥当｜PASS｜2,197円｜💰22.0万円｜momentum 2205/SL2071.8（✅即時可）｜⚠日程不明 📐進捗 上振れ 24.0% 📆SQ
  > 【業態】総合取引所。現物は東証、デリバティブは大証に集約。東京商品取引所統合。
  > 【いま】終値2,197円・直近5日+0.48%（材料未確認）
  > 【調子】🔥絶好調（8/13） — E軸:進捗54.6%>=前年同期44.0%・🔼進捗先行
  > 【水準】⚪妥当（3.0/7）— PER21.31倍・PEG0.6294・52週78.3% ／ 💰単元22.0万円
  > 【戦略】当日高値超えの逆指値2205円で順張り参戦を検討。上限2227.1円・SL2071.8円目安
- 9742 アイネス｜granville_tenkan｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜2,387円｜💰23.9万円｜—｜⚡材料後出し
- 3964 オークネット｜granville_tenkan｜⚡好調｜💎割安｜FAIL_INSEN｜1,314円｜💰13.3万円｜—
- 4005 住友化学｜granville_tenkan｜⚡好調｜💎割安｜FAIL_INSEN｜520円｜💰5.1万円｜—
- 4401 ＡＤＥＫＡ｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜4,424円｜💰44.1万円｜—
- 4534 Mochida Pharmaceutical Co., Ltd.｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜3,350円｜💰32.6万円｜—
- 9006 Keikyu Corporation｜granville_tenkan｜⚡好調｜🟢値頃｜PASS｜1,589円｜💰15.9万円｜momentum 1590/SL1493.7（✅即時可）｜📉決算反応日 11/12 📐進捗 遅れ -20.6% 📆SQ
  > 【業態】京浜・三浦半島が地盤。品川・羽田・横浜を核に沿線再開発を推進。
  > 【いま】終値1,589円・直近5日-3.55%（材料未確認）
  > 【調子】⚡好調（7/13） — ⚠進捗遅れ・⚠下期依存
  > 【水準】🟢値頃（5.0/7）— PER13.7倍・PEG0.261・52週67.9% ／ 💰単元15.9万円
  > 【戦略】当日高値超えの逆指値1590円で順張り参戦を検討。上限1605.9円・SL1493.7円目安
- 3405 クラレ｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜1,894円｜💰19.5万円｜—｜⚡材料後出し
- 3496 アズーム｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜5,070円｜💰51.7万円｜—｜⚡材料後出し
- 7744 ノーリツ鋼機｜granville_tenkan｜⚡好調｜⚪妥当｜PASS｜2,067円｜💰20.7万円｜momentum 2073/SL1947.7（✅即時可）｜🚨決算直前 11/13(残1営業日) 📆SQ
  > 【業態】ペン先等金属加工部材からDJ・音響関連機事業が主軸に。金属部品、建材も。
  > 【いま】終値2,067円・直近5日+0.63%（材料未確認）
  > 【調子】⚡好調（7/13） — E軸判定不能(進捗データ不足)・質注意
  > 【水準】⚪妥当（4.0/7）— PER13.04倍・PEG1.0797・52週57.9% ／ 💰単元20.7万円
  > 【戦略】当日高値超えの逆指値2073円で順張り参戦を検討。上限2093.7円・SL1947.7円目安
- 8095 Astena Holdings Co.,Ltd.｜granville_tenkan｜⚡好調｜⚪妥当｜PASS｜555円｜💰5.5万円｜⛔提案なし(指名鮮度切れ 21営業日)｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】医薬品・原料商社から後発薬・医薬受託や表面処理薬の製造等に展開。
  > 【いま】終値555円・直近5日+0.18%（材料未確認）
  > 【調子】⚡好調（7/13）
  > 【水準】⚪妥当（4.0/7）— PER9.55倍・PEG0.7128・52週86.8% ／ 💰単元5.5万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 21営業日)）
- 9075 福山通運｜granville_tenkan/granville_oshime｜⚡好調｜⚪妥当｜PASS｜6,400円｜💰64.0万円｜momentum 6440/SL6044.2（✅即時可）｜📉決算反応日 11/12 📐進捗 上振れ 10.4% 📆SQ ⚠1単元でリスク枠超過（39580円）
  > 【業態】西日本地盤の路線トラック大手。小口雑貨に強み。セイノーHDと共同運送を推進。
  > 【いま】終値6,400円・直近5日-1.54%（材料未確認）
  > 【調子】⚡好調（7/13） — 上方修正済み・🔼進捗先行
  > 【水準】⚪妥当（4.0/7）— PER12.74倍・PEG0.3923・52週80% ／ 💰単元64.0万円
  > 【戦略】当日高値超えの逆指値6440円で順張り参戦を検討。上限6504.4円・SL6044.2円目安／⚠1単元リスク39580円（枠超過）
- 5532 リアルゲイト｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜3,350円｜💰34.0万円｜—
- 7970 Shin-Etsu Polymer Co., Ltd.｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,453円｜💰24.4万円｜—
- 4507 塩野義製薬｜granville_tenkan｜⚡好調｜🟡やや割高｜PASS｜3,138円｜💰31.4万円｜momentum 3147/SL2953.5（✅即時可）｜⚠日程不明 📐進捗 上振れ 12.5% 📆SQ
  > 【業態】抗HIV薬が大型化。高脂血症薬、鎮痛、感染分野に強み。海外進出本格化。
  > 【いま】終値3,138円・直近5日-1.69%（材料未確認）
  > 【調子】⚡好調（7/13） — 税引前代替・質注意・経常減益-9.1%・上方修正済み・突出ボーナス・🔼加速・🔼進捗先行
  > 【水準】🟡やや割高（2.0/7）— PER12.57倍・PEG—・52週47.2% ／ 💰単元31.4万円
  > 【戦略】当日高値超えの逆指値3147円で順張り参戦を検討。上限3178.5円・SL2953.5円目安
- 1941 中電工｜granville_tenkan｜⚡好調｜🟢値頃｜PASS｜5,150円｜💰51.5万円｜momentum 5170/SL4850.4（✅即時可）｜⚠日程不明 📆SQ ⚠1単元でリスク枠超過（31960円）
  > 【業態】中国電力系で依存度約3割。電気工事主体。総資産の投資有価証券が大。
  > 【いま】終値5,150円・直近5日+2.79%（材料未確認）
  > 【調子】⚡好調（6/13） — ⚠減速
  > 【水準】🟢値頃（5.0/7）— PER11.96倍・PEG0.4814・52週63% ／ 💰単元51.5万円
  > 【戦略】当日高値超えの逆指値5170円で順張り参戦を検討。上限5221.7円・SL4850.4円目安／⚠1単元リスク31960円（枠超過）
- 8061 Seika Corporation｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_INSEN｜2,849円｜💰28.7万円｜—
- 4848 Fullcast Holdings Co., Ltd.｜granville_tenkan/granville_oshime｜⚡好調｜⚪妥当｜PASS｜1,830円｜💰18.3万円｜momentum 1836/SL1724.9（⏸位置不適(25MA下 -0.63%)）｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8） 📆SQ
  > 【業態】日雇い派遣からアルバイト紹介・給与管理代行に転換。警備請負、ラーメンチェーンも。
  > 【いま】終値1,830円・直近5日-4.89%（材料未確認）
  > 【調子】⚡好調（6/13） — 質注意
  > 【水準】⚪妥当（3.0/7）— PER11.64倍・PEG0.9036・52週76.2% ／ 💰単元18.3万円
  > 【戦略】当日高値超えの逆指値1836円で順張り参戦を検討。上限1854.4円・SL1724.9円目安（⏸位置不適(25MA下 -0.63%)）
- 6371 Tsubakimoto Chain Co.｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜2,650円｜💰26.4万円｜—
- 4045 Toagosei Co., Ltd.｜granville_tenkan｜⚡好調｜🟡やや割高｜FAIL_UWAHIGE｜1,800円｜💰17.9万円｜—
- 6099 エラン｜granville_tenkan｜⚡好調｜🟡やや割高｜FAIL_UWAHIGE｜785円｜💰7.8万円｜—
- 3935 Edia Co. Ltd.｜granville_tenkan｜⚡好調｜💎割安｜FAIL_INSEN｜661円｜💰6.6万円｜—
- 4554 Fuji Pharma Co., Ltd.｜granville_tenkan｜⚡好調｜🟢値頃｜PASS｜1,878円｜💰18.8万円｜momentum 1888/SL1773.8（✅即時可）｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8） 📆SQ
  > 【業態】後発医薬品大手。不妊症治療剤と血管造影剤が主力。新薬・バイオ後発品も。
  > 【いま】終値1,878円・直近5日-0.84%（材料未確認）
  > 【調子】⚡好調（5/13） — E軸判定不能(期首・進捗なし)
  > 【水準】🟢値頃（5.0/7）— PER10.05倍・PEG0.8459・52週31% ／ 💰単元18.8万円
  > 【戦略】当日高値超えの逆指値1888円で順張り参戦を検討。上限1906.9円・SL1773.8円目安
- 4617 中国塗料｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_INSEN｜3,510円｜💰35.7万円｜—
- 9842 アークランズ｜granville_tenkan｜⚡好調｜🟢値頃｜PASS｜1,914円｜💰19.1万円｜momentum 1918/SL1802（✅即時可）｜⚠日程不明 📆SQ
  > 【業態】新潟地盤でDIY中心の巨艦店「ムサシ」展開。傘下で外食。ジョイフル本田と統合へ。
  > 【いま】終値1,914円・直近5日-1.85%（材料未確認）
  > 【調子】⚡好調（5/13）
  > 【水準】🟢値頃（5.0/7）— PER12.02倍・PEG0.41・52週55.1% ／ 💰単元19.1万円
  > 【戦略】当日高値超えの逆指値1918円で順張り参戦を検討。上限1937.2円・SL1802円目安
- 6432 竹内製作所｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜7,500円｜💰76.3万円｜—
- 8016 オンワード HD｜granville_tenkan｜⚡好調｜⚪妥当｜PASS｜787円｜💰7.9万円｜momentum 788/SL739.8（✅即時可）｜⚠日程不明 📆SQ
  > 【業態】総合アパレル最大手。百貨店中心「23区」「組曲」等。EC販積極。ウェルネス関連も。
  > 【いま】終値787円・直近5日-1.25%（材料未確認）
  > 【調子】⚡好調（5/13）
  > 【水準】⚪妥当（4.0/7）— PER9.57倍・PEG0.952・52週71.1% ／ 💰単元7.9万円
  > 【戦略】当日高値超えの逆指値788円で順張り参戦を検討。上限795.9円・SL739.8円目安
- 8804 東京建物｜granville_tenkan｜⚡好調｜⚪妥当｜PASS｜3,408円｜💰34.1万円｜⛔提案なし(材料後出し)｜📉決算反応日 11/13 📐進捗 遅れ -19.3%｜⚡材料後出し
  > 【業態】総合不動産。ビル賃貸が主力。マンション分譲やシニア向け住宅、駐車場なども。
  > 【いま】終値3,408円・直近5日-4.62%・📊[Summary]Consolidated Financial Results for the Nine Months Ended September 30, 2026 (Under Japanese GAAP)
  > 【調子】⚡好調（5/13） — 上方修正済み・⚠減速・⚠進捗遅れ
  > 【水準】⚪妥当（4.0/7）— PER10.86倍・PEG1.5982・52週32.2% ／ 💰単元34.1万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 2206 江崎グリコ｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜5,070円｜💰50.2万円｜—
- 4403 日油｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜2,579円｜💰25.4万円｜—
- 7606 ＴＡＢＡＹＡホールディングス｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜2,626円｜💰26.1万円｜—
- 7747 朝日インテック｜granville_tenkan｜⚡好調｜🔴過熱｜PASS｜3,862円｜💰38.6万円｜momentum 3875/SL3637.8（✅即時可）｜🚨決算直前 11/13(残1営業日) 📆SQ
  > 【業態】医療用器具を製造。カテーテル治療用ガイドワイヤなど。産業用ワイヤも。海外生産。
  > 【いま】終値3,862円・直近5日-0.72%（材料未確認）
  > 【調子】⚡好調（5/13） — E軸判定不能(期首・進捗なし)・🔼加速
  > 【水準】🔴過熱（1.0/7）— PER27.08倍・PEG1.6503・52週78.6% ／ 💰単元38.6万円
  > 【戦略】当日高値超えの逆指値3875円で順張り参戦を検討。上限3913.8円・SL3637.8円目安
- 4169 Enechange Ltd.｜granville_tenkan｜⚠減速｜⚪妥当｜PASS｜283円｜💰2.8万円｜⛔提案なし(指名鮮度切れ 14営業日)｜⚠日程不明 📐進捗 遅れ -13.0% ⚠業績基調が下向き（⚠減速）
  > 【業態】電力・ガスの切り替え行うプラットホーム「エネチェンジ」提供。電力事業のDX支援も。
  > 【いま】終値283円・直近5日+10.98%・📌ENECHANGE、エネルギーの「総合ソリューション化」へ─ 太陽光・蓄電池・省エネの提案サービスを開始
  > 【調子】⚠減速（4/13） — 4Q換算（変則決算）・赤字→黒字転換・C判定不能(黒字転換)・E軸判定不能(進捗データ不足)・減収・⚠進捗遅れ
  > 【水準】⚪妥当（4.0/7）— PER20.36倍・PEG0.0432・52週53.3% ／ 💰単元2.8万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 14営業日)）
- 4568 第一三共｜granville_tenkan｜✅順調｜⚪妥当｜PASS｜2,858円｜💰28.6万円｜momentum 2865/SL2692.2（✅即時可）｜⚠日程不明 📆SQ
  > 【業態】国内製薬大手。循環器と感染症に強み。がん新薬で英アストラゼネカと提携。
  > 【いま】終値2,858円・直近5日-7.16%（材料未確認）
  > 【調子】✅順調（4/13） — 税引前代替・D軸判定不能(直近Qデータ取得不可)・上方修正済み
  > 【水準】⚪妥当（4.0/7）— PER20.74倍・PEG1.4572・52週30.7% ／ 💰単元28.6万円
  > 【戦略】当日高値超えの逆指値2865円で順張り参戦を検討。上限2893.7円・SL2692.2円目安
- 6412 Heiwa Holdings Inc.｜granville_tenkan｜✅順調｜⚪妥当｜PASS｜2,112円｜💰21.1万円｜⛔提案なし(材料後出し)｜📉決算反応日 11/13｜⚡材料後出し
  > 【業態】パチンコ、パチスロ機大手。開発力に定評。傘下にゴルフ場運営のアコーディア、PGM。
  > 【いま】終値2,112円・直近5日-3.91%・📊2027年３月期  第２四半期（中間期）決算短信〔日本基準〕（連結）
  > 【調子】✅順調（4/13）
  > 【水準】⚪妥当（4.0/7）— PER10.26倍・PEG0.8326・52週71.4% ／ 💰単元21.1万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 417A ブルーゾーンホールディングス｜granville_tenkan｜✅順調｜⚪妥当｜PASS｜1,918円｜💰19.2万円｜momentum 1919/SL1802.9（✅即時可）｜⚠日程不明 📆SQ
  > 【業態】埼玉地盤の食品スーパー中堅。提案型売り場作りに定評。持株会社に移行。
  > 【いま】終値1,918円・直近5日-6.53%（材料未確認）
  > 【調子】✅順調（4/13） — 質注意
  > 【水準】⚪妥当（3.0/7）— PER16.21倍・PEG9.2976・52週69.7% ／ 💰単元19.2万円
  > 【戦略】当日高値超えの逆指値1919円で順張り参戦を検討。上限1938.2円・SL1802.9円目安
- 2488 ＪＴＰ｜granville_tenkan｜✅順調｜🟡やや割高｜PASS｜1,391円｜💰13.9万円｜momentum 1392/SL1307.5（⏸位置不適(25MA下 -3.6%)）｜⚠日程不明 📐進捗 上振れ 19.5% 📆SQ
  > 【業態】IT活用支援事業。セキュリティ、AIソフト開発・保守を展開。人材育成コンサルも。
  > 【いま】終値1,391円・直近5日-3.74%（材料未確認）
  > 【調子】✅順調（4/13） — ⚠減速・🔼進捗先行
  > 【水準】🟡やや割高（2.0/7）— PER10.69倍・PEG5.239・52週63.4% ／ 💰単元13.9万円
  > 【戦略】当日高値超えの逆指値1392円で順張り参戦を検討。上限1405.9円・SL1307.5円目安（⏸位置不適(25MA下 -3.6%)）
- 4549 Eiken Chemical Co., Ltd.｜granville_tenkan｜✅順調｜🟡やや割高｜PASS｜2,233円｜💰22.3万円｜⛔提案なし(指名鮮度切れ 16営業日)｜⚠日程不明
  > 【業態】臨床検査薬大手。便潜血試薬で高シェア。微生物、遺伝子、尿検査なども。
  > 【いま】終値2,233円・直近5日-1.98%（材料未確認）
  > 【調子】✅順調（4/13）
  > 【水準】🟡やや割高（2.0/7）— PER35.67倍・PEG18.1157・52週14.3% ／ 💰単元22.3万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 16営業日)）
- 5184 ニチリン｜granville_tenkan｜✅順調｜🟡やや割高｜PASS｜4,155円｜💰41.5万円｜⛔提案なし(指名鮮度切れ 13営業日)｜📉決算反応日 11/12 📐進捗 上振れ 13.2%
  > 【業態】独立系の自動車用ホース大手。二輪車用油圧ブレーキホース高シェア。内部熱交換器も。
  > 【いま】終値4,155円・直近5日-0.48%（材料未確認）
  > 【調子】✅順調（4/13） — 質注意・🔼進捗先行
  > 【水準】🟡やや割高（2.0/7）— PER9.63倍・PEG3.2925・52週72.5% ／ 💰単元41.5万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 13営業日)）
- 7269 スズキ｜granville_tenkan｜✅順調｜🟡やや割高｜PASS｜2,201円｜💰22.0万円｜momentum 2203.5/SL2070.3（✅即時可）｜⚠日程不明 📐進捗 上振れ 20.4% 📆SQ
  > 【業態】軽自動車国内2強。2輪も大手。インドで高シェア。中国撤退。トヨタと提携。
  > 【いま】終値2,201円・直近5日-3.19%（材料未確認）
  > 【調子】✅順調（4/13） — 税引前代替・質注意・経常減益-5.6%・上方修正済み・🔼進捗先行
  > 【水準】🟡やや割高（2.0/7）— PER10.11倍・PEG—・52週66.1% ／ 💰単元22.0万円
  > 【戦略】当日高値超えの逆指値2203.5円で順張り参戦を検討。上限2225.5円・SL2070.3円目安
- 9418 Ｕ－ＮＥＸＴ　ＨＯＬＤＩＮＧＳ｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_UWAHIGE｜1,854円｜💰18.3万円｜—
- 3092 ＺＯＺＯ｜granville_tenkan｜✅順調｜🔴過熱｜FAIL_UWAHIGE｜1,158円｜💰11.5万円｜—
- 3549 クスリのアオキホールディングス｜granville_tenkan｜✅順調｜🔴過熱｜FAIL_INSEN｜5,045円｜💰50.8万円｜—｜⚡材料後出し
- 6592 Mabuchi Motor Co., Ltd.｜granville_tenkan｜✅順調｜🔴過熱｜PASS｜1,802円｜💰18.0万円｜momentum 1805/SL1695.8（✅即時可）｜⚠日程不明 📐進捗 上振れ 38.9% 📆SQ
  > 【業態】小型モーターで世界高シェア。海外生産比率100%。車載用電装機器が主軸。
  > 【いま】終値1,802円・直近5日-0.14%（材料未確認）
  > 【調子】✅順調（4/13） — 質注意・経常減益-10.8%・🔼加速・🔼進捗先行
  > 【水準】🔴過熱（1.0/7）— PER18.98倍・PEG—・52週82.1% ／ 💰単元18.0万円
  > 【戦略】当日高値超えの逆指値1805円で順張り参戦を検討。上限1823.0円・SL1695.8円目安
- 8160 KISOJI CO., LTD.｜granville_tenkan｜✅順調｜🔴過熱｜PASS｜2,510円｜💰25.1万円｜momentum 2511/SL2359.4（✅即時可）｜⚠日程不明 📆SQ
  > 【業態】外食中堅。しゃぶしゃぶ「木曽路」は業界最大手。焼肉・居酒屋なども経営。
  > 【いま】終値2,510円・直近5日-1.72%（材料未確認）
  > 【調子】✅順調（4/13） — ⚠減速・⚠進捗遅れ
  > 【水準】🔴過熱（1.0/7）— PER33.65倍・PEG3.0701・52週70.9% ／ 💰単元25.1万円
  > 【戦略】当日高値超えの逆指値2511円で順張り参戦を検討。上限2536.1円・SL2359.4円目安
- 8113 Unicharm Corporation｜granville_tenkan｜✅順調｜🔴過熱｜FAIL_UWAHIGE｜1,103円｜💰10.9万円｜—
- 4166 Cacco, Inc.｜granville_tenkan｜✅順調｜💎割安｜FAIL_INSEN｜661円｜💰6.7万円｜—｜⚡材料後出し
- 9163 Nareru Group Inc.｜granville_tenkan｜✅順調｜🟢値頃｜FAIL_UWAHIGE｜2,050円｜💰20.5万円｜—
- 8056 ＢＩＰＲＯＧＹ｜granville_tenkan｜✅順調｜⚪妥当｜PASS｜4,830円｜💰48.3万円｜momentum 4846/SL4550.5（⏸位置不適(25MA下 -1.01%)）｜⚠日程不明 📐進捗 遅れ -25.7% 📆SQ
  > 【業態】大日本印刷系の情報システム大手。クラウド事業に注力。金融、流通、空運に強み。
  > 【いま】終値4,830円・直近5日-2.91%（材料未確認）
  > 【調子】✅順調（3/13） — ⚠進捗遅れ
  > 【水準】⚪妥当（4.0/7）— PER14.5倍・PEG1.5296・52週36.7% ／ 💰単元48.3万円
  > 【戦略】当日高値超えの逆指値4846円で順張り参戦を検討。上限4894.5円・SL4550.5円目安（⏸位置不適(25MA下 -1.01%)）
- 9956 Valor Holdings Co., Ltd.｜granville_tenkan｜✅順調｜⚪妥当｜PASS｜1,619円｜💰16.2万円｜momentum 1620/SL1521.9（⏸位置不適(25MA下 -1.33%／52週 28.2%)）｜📉決算反応日 11/12 📆SQ
  > 【業態】中部地盤の食品スーパー中堅。ドラッグストアやホームセンター、スポーツクラブも展開。
  > 【いま】終値1,619円・直近5日-9.04%（材料未確認）
  > 【調子】✅順調（3/13） — 質注意・上方修正済み・⚠減速
  > 【水準】⚪妥当（4.0/7）— PER11.39倍・PEG7.1106・52週28.2% ／ 💰単元16.2万円
  > 【戦略】当日高値超えの逆指値1620円で順張り参戦を検討。上限1636.2円・SL1521.9円目安（⏸位置不適(25MA下 -1.33%／52週 28.2%)）
- 3563 ＦＯＯＤ　＆　ＬＩＦＥ　ＣＯＭＰＡＮＩＥＳ｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_INSEN｜5,771円｜💰57.8万円｜—
- 4540 Tsumura & Co.｜granville_tenkan｜✅順調｜🟡やや割高｜PASS｜3,914円｜💰39.1万円｜momentum 3919/SL3679.2（✅即時可）｜⚠日程不明 📐進捗 上振れ 18.7% 📆SQ
  > 【業態】漢方薬特化で最大手。高齢者、がん患者、婦人処方薬を拡大。中国事業も。
  > 【いま】終値3,914円・直近5日+0.64%（材料未確認）
  > 【調子】✅順調（3/13） — 質注意・経常減益-9.1%・上方修正済み・🔼進捗先行
  > 【水準】🟡やや割高（2.0/7）— PER9.96倍・PEG—・52週45.1% ／ 💰単元39.1万円
  > 【戦略】当日高値超えの逆指値3919円で順張り参戦を検討。上限3958.2円・SL3679.2円目安
- 7734 Riken Keiki Co., Ltd.｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_INSEN｜3,350円｜💰33.2万円｜—
- 9045 Keihan Holdings Co., Ltd.｜granville_tenkan｜⚠減速｜🟡やや割高｜PASS｜3,346円｜💰33.5万円｜momentum 3351/SL3145.2（✅即時可）｜📐進捗 上振れ 18.8% ⚠業績基調が下向き（⚠減速） 📆SQ
  > 【業態】大阪京都間が主力の私鉄。京都観光に強み。中之島線沿線の開発に力。
  > 【いま】終値3,346円・直近5日-4.65%（材料未確認）
  > 【調子】⚠減速（3/13） — A成長率0以下のためレバレッジ計算不可(C=0)・質注意・上方修正済み・減収・🔼進捗先行
  > 【水準】🟡やや割高（2.0/7）— PER11.25倍・PEG—・52週55.9% ／ 💰単元33.5万円
  > 【戦略】当日高値超えの逆指値3351円で順張り参戦を検討。上限3384.5円・SL3145.2円目安
- 6745 ホーチキ｜granville_tenkan｜✅順調｜🔴過熱｜FAIL_INSEN｜2,132円｜💰21.7万円｜—
- 4902 Konica Minolta, Inc.｜granville_tenkan｜➖横ばい｜🟢値頃｜FAIL_UWAHIGE｜571円｜💰5.7万円｜—
- 8801 三井不動産｜granville_tenkan｜➖横ばい｜⚪妥当｜PASS｜1,596円｜💰16.0万円｜momentum 1596.5/SL1499.8（⏸位置不適(52週 25.8%)）｜📐進捗 遅れ -16.9% 📆SQ
  > 【業態】総合不動産、最大手。ビル賃貸が主力。街づくり主体に分譲、ホテル、商施設。
  > 【いま】終値1,596円・直近5日-8.17%（材料未確認）
  > 【調子】➖横ばい（2/13） — 質注意・勢い判定矛盾・⚠進捗遅れ
  > 【水準】⚪妥当（3.0/7）— PER15.07倍・PEG28.0815・52週25.8% ／ 💰単元16.0万円
  > 【戦略】当日高値超えの逆指値1596.5円で順張り参戦を検討。上限1612.5円・SL1499.8円目安（⏸位置不適(52週 25.8%)）
- 9837 Morito Co., Ltd.｜granville_tenkan｜➖横ばい｜⚪妥当｜FAIL_UWAHIGE｜1,826円｜💰18.2万円｜—
- 5233 太平洋セメント｜granville_tenkan｜🔻悪化｜🟡やや割高｜PASS｜4,013円｜💰40.1万円｜momentum 4033/SL3786.3（⏸位置不適(25MA下 -3.58%)）｜⚠日程不明 📐進捗 上振れ 14.1% ⚠業績基調が下向き（🔻悪化） 📆SQ
  > 【業態】セメント最大手。海外にも展開。建材や電材など多角化。産廃・再資源化も。
  > 【いま】終値4,013円・直近5日-10.42%（材料未確認）
  > 【調子】🔻悪化（2/13） — 質注意・経常減益-26.1%・🔼進捗先行
  > 【水準】🟡やや割高（2.0/7）— PER8.59倍・PEG—・52週43.9% ／ 💰単元40.1万円
  > 【戦略】当日高値超えの逆指値4033円で順張り参戦を検討。上限4073.3円・SL3786.3円目安（⏸位置不適(25MA下 -3.58%)）
- 8803 Heiwa Real Estate Co., Ltd.｜granville_tenkan｜➖横ばい｜🟡やや割高｜PASS｜2,352円｜💰23.5万円｜momentum 2353/SL2210.9（✅即時可）｜⚠日程不明 📆SQ
  > 【業態】各地の証券取引所賃貸が収益源。一般賃貸、マンション分譲なども。REIT強化。
  > 【いま】終値2,352円・直近5日-1.63%（材料未確認）
  > 【調子】➖横ばい（2/13） — 質注意・E軸判定不能(進捗率非開示)
  > 【水準】🟡やや割高（2.0/7）— PER13.51倍・PEG87.6765・52週49.4% ／ 💰単元23.5万円
  > 【戦略】当日高値超えの逆指値2353円で順張り参戦を検討。上限2376.5円・SL2210.9円目安
- 4922 コーセーホールディングス｜granville_tenkan｜➖横ばい｜🔴過熱｜PASS｜5,876円｜💰58.8万円｜momentum 5909/SL5545.1（✅即時可）｜⚠日程不明 📆SQ ⚠1単元でリスク枠超過（36390円）
  > 【業態】化粧品大手。高級化粧品に強み。コスメタリー事業も展開。アジア・米国に進出。
  > 【いま】終値5,876円・直近5日-6.64%（材料未確認）
  > 【調子】➖横ばい（2/13） — 質注意・経常減益-14.7%
  > 【水準】🔴過熱（1.0/7）— PER31.76倍・PEG—・52週60.8% ／ 💰単元58.8万円
  > 【戦略】当日高値超えの逆指値5909円で順張り参戦を検討。上限5968.1円・SL5545.1円目安／⚠1単元リスク36390円（枠超過）
- 9735 セコム｜granville_tenkan｜➖横ばい｜🔴過熱｜FAIL_UWAHIGE｜6,990円｜💰67.7万円｜—
- 6328 Ebara Jitsugyo Co., Ltd.｜granville_tenkan｜⚠減速｜⚪妥当｜FAIL_UWAHIGE｜2,297円｜💰22.9万円｜—
- 4912 ライオン｜granville_tenkan｜⚠減速｜⚪妥当｜PASS｜2,190円｜💰21.9万円｜momentum 2191.5/SL2059.1（✅即時可）｜⚠日程不明 ⚠業績基調が下向き（⚠減速） 📆SQ
  > 【業態】家庭用品大手。歯磨きで国内首位級。薬品「バファリン」に強み。機能性食品も。
  > 【いま】終値2,190円・直近5日+13.17%（材料未確認）
  > 【調子】⚠減速（1/13） — 税引前代替・経常非開示(IFRS等)のため最終益成長率で代替・質注意・経常減益-9.4%・E軸判定不能(進捗データ不足)
  > 【水準】⚪妥当（3.0/7）— PER23.76倍・PEG—・52週100% ／ 💰単元21.9万円
  > 【戦略】当日高値超えの逆指値2191.5円で順張り参戦を検討。上限2213.4円・SL2059.1円目安
- 1878 Daito Trust Construction Co., Ltd.｜granville_tenkan｜⚠減速｜🟡やや割高｜PASS｜3,368円｜💰33.7万円｜momentum 3373/SL3165.9（✅即時可）｜⚠日程不明 ⚠業績基調が下向き（⚠減速） 📆SQ
  > 【業態】地主に建物賃貸事業を提案。建設・賃貸仲介・管理・家賃保証など一貫。
  > 【いま】終値3,368円・直近5日-5.34%（材料未確認）
  > 【調子】⚠減速（1/13） — 進捗判定不能(自動抽出範囲外)・質注意
  > 【水準】🟡やや割高（2.0/7）— PER10.17倍・PEG17.0355・52週51% ／ 💰単元33.7万円
  > 【戦略】当日高値超えの逆指値3373円で順張り参戦を検討。上限3406.7円・SL3165.9円目安
- 1928 積水ハウス｜granville_tenkan｜⚠減速｜🟡やや割高｜FAIL_UWAHIGE｜3,564円｜💰35.1万円｜—
- 4552 JCR Pharmaceuticals Co., Ltd.｜granville_tenkan｜🔻悪化｜🔴過熱｜FAIL_UWAHIGE｜493円｜💰4.9万円｜—
- 5105 ＴＯＹＯ　ＴＩＲＥ｜granville_tenkan｜⚠減速｜🟡やや割高｜PASS｜4,247円｜💰42.5万円｜⛔提案なし(指名鮮度切れ 12営業日)｜⏰決算 11/16(残2営業日) ⚠業績基調が下向き（⚠減速）
  > 【業態】タイヤ大手。トラック・バス用に強み。北米向けSUV用タイヤも。株主に三菱商事。
  > 【いま】終値4,247円・直近5日-1.67%（材料未確認）
  > 【調子】⚠減速（1/13） — 進捗データ取得不可(判定不能)・(質注意)
  > 【水準】🟡やや割高（2.0/7）— PER8.44倍・PEG—・52週57.5% ／ 💰単元42.5万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 12営業日)）
- 8167 リテールパートナーズ｜granville_tenkan｜⚠減速｜🟡やや割高｜FAIL_UWAHIGE｜1,374円｜💰13.8万円｜—
- 9401 東京放送ホールディングス｜granville_tenkan｜⚠減速｜🔴過熱｜FAIL_UWAHIGE｜6,182円｜💰60.6万円｜—
- 4375 セーフィー｜granville_tenkan/changepoint｜取得不可｜💎割安｜FAIL_INSEN｜616円｜💰6.2万円｜—
- 3182 オイシックス｜granville_tenkan｜業績データ取得不可(経常益予想非開示)｜🟢値頃｜FAIL_INSEN｜1,632円｜💰16.3万円｜—｜⚡材料後出し
- 7921 ＴＡＫＡＲＡ　＆　ＣＯＭＰＡＮＹ｜granville_tenkan｜業績データ取得不可(経常益予想非開示)｜🟢値頃｜PASS｜4,245円｜💰42.5万円｜⛔提案なし(指名鮮度切れ 12営業日)｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】ディスクロージャー大手。有価証券報告書の作成が主力。通訳・翻訳事業が拡大。
  > 【いま】終値4,245円・直近5日-2.64%（材料未確認）
  > 【調子】業績データ取得不可(経常益予想非開示)（—/13） — 業績データ取得不可(経常益予想非開示)
  > 【水準】🟢値頃（5.0/7）— PER15.66倍・PEG—・52週72.7% ／ 💰単元42.5万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 12営業日)）
- 2811 Kagome Co., Ltd.｜granville_tenkan｜業績データ取得不可(経常益予想非開示)｜⚪妥当｜PASS｜2,810円｜💰28.1万円｜momentum 2814/SL2644.2（✅即時可）｜⚠日程不明 📆SQ
  > 【業態】トマト加工品で首位。飲料ブランドに強み。農産品事業を育成。海外で業務用。
  > 【いま】終値2,810円・直近5日-2.11%（材料未確認）
  > 【調子】業績データ取得不可(経常益予想非開示)（—/13） — 業績データ取得不可(経常益予想非開示)
  > 【水準】⚪妥当（4.0/7）— PER24.2倍・PEG—・52週74% ／ 💰単元28.1万円
  > 【戦略】当日高値超えの逆指値2814円で順張り参戦を検討。上限2842.1円・SL2644.2円目安
- 2897 Nissin Foods Holdings Co., Ltd.｜granville_tenkan｜取得不可｜⚪妥当｜FAIL_INSEN｜2,872円｜💰29.0万円｜—
- 4765 ＳＢＩグローバルアセットマネジメント｜granville_tenkan/granville_oshime｜判定保留｜⏸判定不能｜FAIL_INSEN｜618円｜💰6.2万円｜—｜⚡材料後出し
- 6998 Nippon Tungsten Co., Ltd.｜granville_oshime/granville_rebound｜🚀確変｜💎割安｜FAIL_INSEN｜2,868円｜💰27.5万円｜—
- 6570 Kyowa Corporation Co. Ltd.｜granville_oshime｜🚀確変｜🟢値頃｜FAIL_INSEN｜3,190円｜💰37.5万円｜—
- 6574 コンヴァノ｜granville_oshime｜🚀確変｜🟢値頃｜FAIL_UWAHIGE｜992円｜💰9.6万円｜—
- 7480 スズデン｜granville_oshime/granville_rebound｜🚀確変｜⚪妥当｜FAIL_UWAHIGE｜3,570円｜💰35.6万円｜—
- 5243 ｎｏｔｅ｜granville_oshime/granville_rebound｜🚀確変｜⚪妥当｜FAIL_INSEN｜2,691円｜💰27.5万円｜—
- 6834 精工技研｜granville_oshime/granville_rebound｜🔥絶好調｜💎割安｜FAIL_INSEN｜5,040円｜💰52.8万円｜—
- 7609 ダイトロン｜granville_oshime/granville_rebound｜🔥絶好調｜💎割安｜FAIL_INSEN｜3,735円｜💰37.7万円｜—
- 4382 HEROZ, Inc.｜granville_oshime/changepoint｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜800円｜💰8.2万円｜—
- 8051 山善｜granville_oshime｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜1,846円｜💰18.4万円｜—
- 8137 サンワテクノス｜granville_oshime/granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜3,865円｜💰38.8万円｜—
- 153A Caulis, Inc.｜granville_oshime｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜1,983円｜💰20.6万円｜—
- 4258 AMIYA Corporation｜granville_oshime｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜5,100円｜💰59.6万円｜—
- 8392 大分銀行｜granville_oshime/granville_rebound｜🔥絶好調｜💎割安｜FAIL_INSEN｜2,666円｜💰27.6万円｜—
- 3156 レスター｜granville_oshime/granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜5,090円｜💰52.5万円｜—
- 6523 ＰＨＣホールディングス｜granville_oshime｜🔥絶好調｜🟢値頃｜PASS｜1,284円｜💰12.8万円｜⛔型不一致: 既に支持帯以下｜📉決算反応日 11/12 📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】各種ヘルスケア機器・サービスの開発・製造販売。糖尿病ケアに強み。ファンド傘下。
  > 【いま】終値1,284円・直近5日-11.45%（材料未確認）
  > 【調子】🔥絶好調（8/13） — 税引前代替・上方修正済み・突出ボーナス・進捗モデル値域外・🔼進捗先行
  > 【水準】🟢値頃（5.0/7）— PER9.07倍・PEG0.0285・52週45.5% ／ 💰単元12.8万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 9304 澁澤倉庫｜granville_oshime｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1,930円｜💰19.6万円｜—
- 2384 ＳＢＳホールディングス｜granville_oshime｜🔥絶好調｜⚪妥当｜PASS｜5,620円｜💰56.2万円｜⛔型不一致: 既に支持帯以下｜🚨決算直前 11/13(残1営業日)
  > 【業態】総合物流会社。物流一括受託が主力。食品輸送に力。物流施設の流動化も。
  > 【いま】終値5,620円・直近5日-6.49%（材料未確認）
  > 【調子】🔥絶好調（8/13）
  > 【水準】⚪妥当（3.0/7）— PER15.39倍・PEG0.6701・52週83.8% ／ 💰単元56.2万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 3968 セグエグループ｜granville_oshime｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜818円｜💰8.0万円｜—
- 5892 ＹＵＴＯＲＩ｜granville_oshime｜⚡好調｜🟢値頃｜FAIL_INSEN｜2,585円｜💰25.9万円｜—
- 6036 ＫｅｅＰｅｒ技研｜granville_oshime｜⚡好調｜🟢値頃｜FAIL_INSEN｜1,775円｜💰18.3万円｜—｜⚡材料後出し
- 3040 ソリトンシステムズ｜granville_oshime/granville_rebound｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,606円｜💰29.6万円｜—｜⚡材料後出し
- 3673 ブロードリーフ｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜396円｜💰4.8万円｜—
- 4398 ブロードバンドセキュリティ｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜2,335円｜💰22.6万円｜—｜⚡材料後出し
- 4206 アイカ工業｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜4,289円｜💰42.5万円｜—
- 6736 Suncorporation｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜10,690円｜💰131.3万円｜—
- 8410 Seven Bank, Ltd.｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜351円｜💰3.5万円｜—
- 2492 インフォマート（インフォＭＴ）｜granville_oshime｜⚡好調｜🟡やや割高｜PASS｜748円｜💰7.5万円｜⛔型不一致: 既に支持帯以下｜⚠日程不明
  > 【業態】企業間取引をデジタル化するプラットフォームの運営。契約書サービスなども展開。
  > 【いま】終値748円・直近5日-2.73%（材料未確認）
  > 【調子】⚡好調（7/13）
  > 【水準】🟡やや割高（2.0/7）— PER64.48倍・PEG0.9148・52週87.4% ／ 💰単元7.5万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 7806 MTG Co., Ltd.｜granville_oshime/changepoint｜⚡好調｜🟡やや割高｜FAIL_INSEN｜7,620円｜💰81.1万円｜—
- 8388 阿波銀行｜granville_oshime/granville_rebound｜⚡好調｜💎割安｜FAIL_INSEN｜1,914円｜💰19.4万円｜—
- 3106 倉敷紡績｜granville_oshime｜⚡好調｜🟢値頃｜FAIL_INSEN｜2,201円｜💰22.2万円｜—
- 4674 クレスコ｜granville_oshime｜⚡好調｜⚪妥当｜PASS｜1,974円｜💰19.7万円｜⛔型不一致: 既に支持帯以下｜⚠日程不明 📐進捗 遅れ -12.4%
  > 【業態】情報・通信業（ソフト・システム開発・金融向けシステム・組み込みソフト関連）
  > 【いま】終値1,974円・直近5日+1.13%（材料未確認）
  > 【調子】⚡好調（6/13） — ⚠進捗遅れ
  > 【水準】⚪妥当（4.0/7）— PER14.07倍・PEG0.805・52週74.6% ／ 💰単元19.7万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 6250 Yamabiko Corporation｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜3,980円｜💰43.2万円｜—
- 4498 Cybertrust Japan Co.Ltd.｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜1,695円｜💰18.1万円｜—
- 9552 クオンツ総研ホールディングス｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜1,129円｜💰11.5万円｜—
- 4413 baudroie,inc.｜granville_oshime｜⚡好調｜🟡やや割高｜FAIL_INSEN｜2,938円｜💰29.4万円｜—
- 9536 SAIBU GAS HOLDINGS CO. LTD.｜granville_oshime｜⚡好調｜⚪妥当｜PASS｜2,897円｜💰29.0万円｜⛔提案なし(指名鮮度切れ 14営業日)｜⚠日程不明
  > 【業態】都市ガス大手。福岡が基盤。家庭用燃料電池販売、太陽光発電、不動産も。
  > 【いま】終値2,897円・直近5日-0.28%（材料未確認）
  > 【調子】⚡好調（5/13） — 上方修正済み・進捗モデル値域外・🔼進捗先行
  > 【水準】⚪妥当（4.0/7）— PER10.43倍・PEG0.5429・52週98.4% ／ 💰単元29.0万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 14営業日)）
- 436A サイバーソリューションズ（サイバＳＯＬ）｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜1,642円｜💰17.3万円｜—
- 4373 Simplex Holdings,Inc.｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜1,181円｜💰11.7万円｜—
- 6877 ＯＢＡＲＡ　ＧＲＯＵＰ（ＯＢＡＲＡＧ）｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜6,610円｜💰67.7万円｜—
- 6191 エボラブルアジア｜granville_oshime｜🔻悪化｜🔴過熱｜FAIL_INSEN｜1,471円｜💰14.9万円｜—
- 5036 日本ビジネスシステムズ｜granville_oshime｜✅順調｜🟢値頃｜FAIL_INSEN｜1,725円｜💰17.5万円｜—｜⚡材料後出し
- 8395 佐賀銀行｜granville_oshime/granville_rebound｜⚠減速｜🟢値頃｜FAIL_INSEN｜6,070円｜💰61.7万円｜—
- 8159 Tachibana Eletech Co., Ltd.｜granville_oshime｜✅順調｜⚪妥当｜PASS｜4,325円｜💰43.2万円｜⛔型不一致: 既に支持帯以下
  > 【業態】三菱電機系商社。FAシステム主力にルネサスなど半導体デバイス展開。製造受託も。
  > 【いま】終値4,325円・直近5日+0.12%（材料未確認）
  > 【調子】✅順調（4/13） — E軸判定不能(進捗データ不足)・質注意
  > 【水準】⚪妥当（3.0/7）— PER13.63倍・PEG1.587・52週65.5% ／ 💰単元43.2万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 3042 セキュアヴェイル（セキュアヴェ）｜granville_oshime｜✅順調｜🟡やや割高｜FAIL_INSEN｜754円｜💰9.0万円｜—
- 6080 Ｍ＆Ａキャピタルパートナーズ｜granville_oshime/changepoint｜✅順調｜🟡やや割高｜FAIL_INSEN｜4,540円｜💰46.5万円｜—
- 3762 テクマトリックス（テクマト）｜granville_oshime｜✅順調｜🔴過熱｜FAIL_INSEN｜3,140円｜💰32.0万円｜—
- 5985 SUNCALL CORPORATION｜granville_oshime｜✅順調｜🟢値頃｜FAIL_INSEN｜1,684円｜💰17.1万円｜—
- 338A ZenmuTech,Inc.｜granville_oshime｜✅順調｜⚪妥当｜FAIL_INSEN｜3,100円｜💰32.2万円｜—｜⚡材料後出し
- 9509 Hokkaido Electric Power Company,Incorporated｜granville_oshime｜🔻悪化｜⚪妥当｜PASS｜1,146円｜💰11.5万円｜⛔提案なし(指名鮮度切れ 17営業日)｜⚠日程不明 📐進捗 遅れ -32.9% ⚠業績基調が下向き（🔻悪化）
  > 【業態】原子力と石炭火力が主力。需要は冬ピーク。原発3基が停止、再稼働目指す。
  > 【いま】終値1,146円・直近5日+3.29%（材料未確認）
  > 【調子】🔻悪化（3/13） — 上方修正済み・質注意・⚠進捗遅れ・⚠下期依存
  > 【水準】⚪妥当（3.0/7）— PER7.45倍・PEG—・52週63.6% ／ 💰単元11.5万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 17営業日)）
- 4208 UBE Corporation｜granville_oshime｜✅順調｜🟡やや割高｜FAIL_UWAHIGE｜3,331円｜💰32.9万円｜—
- 4044 Central Glass Co., Ltd.｜granville_oshime｜✅順調｜🔴過熱｜FAIL_UWAHIGE｜4,690円｜💰44.4万円｜—
- 456A Human Made Inc.｜granville_oshime｜✅順調｜🔴過熱｜FAIL_INSEN｜1,924円｜💰21.5万円｜—
- 3692 ＦＦＲＩセキュリティ｜granville_oshime｜➖横ばい｜🔴過熱｜FAIL_INSEN｜7,190円｜💰74.9万円｜—｜⚡材料後出し
- 8255 Axial Retailing, Inc.｜granville_oshime｜➖横ばい｜🔴過熱｜PASS｜1,539円｜💰15.4万円｜⛔提案なし(指名鮮度切れ 19営業日)｜⚠日程不明 📐進捗 上振れ 16.7%
  > 【業態】新潟地盤の食品スーパー。群馬フレッセイを統合。袋詰めなど独自サービスに特色。
  > 【いま】終値1,539円・直近5日-2.35%（材料未確認）
  > 【調子】➖横ばい（2/13） — 質注意・経常減益-6.2%・⚠減速・🔼進捗先行
  > 【水準】🔴過熱（0.0/7）— PER16.71倍・PEG—・52週91.2% ／ 💰単元15.4万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 19営業日)）
- 8361 Ogaki Kyoritsu Bank, Ltd.｜granville_oshime/granville_rebound｜取得不可｜💎割安｜FAIL_INSEN｜1,520円｜💰14.7万円｜—
- 9166 GENDA Inc.｜granville_oshime｜業績データ取得不可｜🟢値頃｜FAIL_INSEN｜677円｜💰6.8万円｜—｜⚡材料後出し
- 336A ダイナミックマッププラットフォーム｜granville_oshime｜業績データ取得不可(経常益予想非開示)｜⚪妥当｜FAIL_INSEN｜1,083円｜💰11.5万円｜—｜⚡材料後出し
- 3993 PKSHA Technology, Inc.｜granville_oshime/changepoint｜業績データ取得不可｜⚪妥当｜FAIL_INSEN｜3,140円｜💰32.5万円｜—｜⚡材料後出し
- 4432 ウイングアーク１ｓｔ｜granville_oshime｜業績データ取得不可(経常益予想非開示)｜🟡やや割高｜PASS｜3,525円｜💰35.2万円｜⛔型不一致: 既に支持帯以下｜⚠日程不明
  > 【業態】企業の情報活用を促進するクラウドサービス提供。帳票・文書管理、データ分析等。
  > 【いま】終値3,525円・直近5日-2.49%（材料未確認）
  > 【調子】業績データ取得不可(経常益予想非開示)（—/13） — 業績データ取得不可(経常益予想非開示)
  > 【水準】🟡やや割高（2.0/7）— PER16.4倍・PEG—・52週78.4% ／ 💰単元35.2万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 8362 Fukui Bank, Ltd.｜granville_oshime｜🔻悪化｜🔴過熱｜FAIL_INSEN｜6,670円｜💰68.5万円｜—
- 6027 Bengo4.com, Inc.｜granville_oshime｜取得不可｜🔴過熱｜FAIL_INSEN｜4,400円｜💰51.1万円｜—
- 3851 日本一ソフトウェア｜granville_rebound｜🚀確変｜💎割安｜FAIL_INSEN｜1,156円｜💰11.8万円｜—
- 3778 SAKURA Internet Inc.｜granville_rebound｜🚀確変｜🟢値頃｜PASS｜3,160円｜💰31.6万円｜⛔提案なし(指名鮮度切れ 19営業日)｜⚠日程不明
  > 【業態】情報・通信業（データセンター・ホスティング・クラウドコンピューティング関連）
  > 【いま】終値3,160円・直近5日+9.68%（材料未確認）
  > 【調子】🚀確変（12/13） — 上方修正済み・前期経常が小さく成長率が大きく出る(105→3,900百万円)
  > 【水準】🟢値頃（5.0/7）— PER84.27倍・PEG0.0403・52週37.4% ／ 💰単元31.6万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 19営業日)）
- 3891 ニッポン高度紙工業｜granville_rebound｜🚀確変｜💎割安｜FAIL_INSEN｜5,700円｜💰57.9万円｜—
- 6138 ダイジェット工業（ダイジェト）｜granville_rebound｜🚀確変｜💎割安｜FAIL_INSEN｜1,753円｜💰17.6万円｜—
- 6862 ミナト HD｜granville_rebound｜🚀確変｜💎割安｜FAIL_INSEN｜3,265円｜💰33.6万円｜—｜⚡材料後出し
- 6769 Thine Electronics, Inc.｜granville_rebound｜🚀確変｜⚪妥当｜FAIL_INSEN｜925円｜💰9.5万円｜—
- 479A PRONI Inc.｜granville_rebound/changepoint｜🔥絶好調｜💎割安｜FAIL_INSEN｜1,525円｜💰15.5万円｜—
- 3691 DIGITAL PLUS, Inc.｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1,308円｜💰13.2万円｜—｜⚡材料後出し
- 4968 Arakawa Chemical Industries,Ltd.｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1,904円｜💰19.7万円｜—
- 5381 Mipox Corp.｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜868円｜💰8.8万円｜—
- 2962 テクニスコ｜granville_rebound｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜1,541円｜💰16.1万円｜—
- 4419 Finatext Holdings Ltd.｜granville_rebound/changepoint｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜1,215円｜💰12.4万円｜—｜⚡材料後出し
- 1436 GreenEnergy & Company｜granville_rebound｜🔥絶好調｜💎割安｜FAIL_INSEN｜1,369円｜💰14.2万円｜—
- 2489 アドウェイズ｜granville_rebound｜⚠減速｜🟢値頃｜FAIL_INSEN｜334円｜💰3.3万円｜—
- 3793 Drecom Co., Ltd.｜granville_rebound｜⚠減速｜🟢値頃｜FAIL_INSEN｜453円｜💰4.6万円｜—
- 6963 ROHM Company Limited｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜2,935円｜💰31.7万円｜—
- 8995 Makoto Construction Co,Ltd｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1,372円｜💰14.1万円｜—
- 150A ＪＳＨ｜granville_rebound｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜615円｜💰6.3万円｜—｜⚡材料後出し
- 6317 Kitagawa Corporation｜granville_rebound｜🔥絶好調｜💎割安｜FAIL_INSEN｜2,288円｜💰22.9万円｜—
- 7715 長野計器｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜3,415円｜💰35.5万円｜—｜⚡材料後出し
- 8364 清水銀行｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜2,739円｜💰28.1万円｜—
- 460A ＢＲＡＮＵ｜granville_rebound｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜1,050円｜💰11.0万円｜—
- 6508 Meidensha Corporation｜granville_rebound｜⚡好調｜💎割安｜FAIL_INSEN｜7,523円｜💰76.2万円｜—
- 5367 Nikkato Corporation｜granville_rebound｜⚡好調｜🟢値頃｜FAIL_INSEN｜1,034円｜💰10.8万円｜—
- 6490 ＰＩＬＬＡＲ｜granville_rebound｜⚡好調｜⚪妥当｜FAIL_INSEN｜9,280円｜💰93.8万円｜—｜⚡材料後出し
- 5252 日本ナレッジ｜granville_rebound｜⚡好調｜🟡やや割高｜FAIL_INSEN｜935円｜💰9.3万円｜—
- 9697 カプコン｜granville_rebound｜⚡好調｜🔴過熱｜FAIL_INSEN｜4,406円｜💰43.9万円｜—
- 477A Startline CO.,LTD.｜granville_rebound｜⚡好調｜💎割安｜FAIL_INSEN｜604円｜💰6.1万円｜—
- 4100 Toda Kogyo Corp.｜granville_rebound｜⚡好調｜💎割安｜FAIL_INSEN｜1,648円｜💰18.1万円｜—
- 7213 LECIP Holdings Corporation｜granville_rebound｜⚡好調｜💎割安｜FAIL_UWAHIGE｜571円｜💰5.7万円｜—
- 3850 INTRAMART CORPORATION｜granville_rebound｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜3,315円｜💰33.4万円｜—
- 6947 図研｜granville_rebound｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜5,140円｜💰50.8万円｜—
- 6958 日本シイエムケイ｜granville_rebound｜⚡好調｜⚪妥当｜FAIL_INSEN｜727円｜💰7.5万円｜—
- 8344 Yamagata Bank, Ltd.｜granville_rebound｜⚡好調｜🟢値頃｜FAIL_INSEN｜4,260円｜💰44.1万円｜—
- 6742 京三製作所｜granville_rebound｜⚠減速｜⚪妥当｜FAIL_INSEN｜968円｜💰9.8万円｜—
- 4667 Aisan Technology Co.,Ltd.｜granville_rebound/changepoint｜⚡好調｜⚪妥当｜FAIL_INSEN｜711円｜💰8.1万円｜—
- 7826 フルヤ金属｜granville_rebound｜⚡好調｜⚪妥当｜FAIL_INSEN｜8,770円｜💰90.5万円｜—
- 5574 ABEJA,Inc.｜granville_rebound/changepoint｜⚡好調｜🟡やや割高｜FAIL_INSEN｜2,015円｜💰20.4万円｜—
- 7256 河西工業｜granville_rebound｜⚡好調｜🔴過熱｜FAIL_INSEN｜398円｜💰—｜—
- 9278 BOOKOFF GROUP HOLDINGS LIMITED｜granville_rebound｜⚡好調｜🔴過熱｜FAIL_INSEN｜2,575円｜💰26.2万円｜—
- 4025 多木化学｜granville_rebound｜✅順調｜⚪妥当｜FAIL_INSEN｜5,300円｜💰53.6万円｜—
- 428A Cypress Holdings Co., Ltd.｜granville_rebound｜✅順調｜⚪妥当｜FAIL_UWAHIGE｜1,425円｜💰14.6万円｜—
- 3371 ソフトクリエイトホールディングス｜granville_rebound｜✅順調｜🟡やや割高｜FAIL_UWAHIGE｜2,063円｜💰20.5万円｜—
- 278A Ｔｅｒｒａ　Ｄｒｏｎｅ｜granville_rebound｜✅順調｜⏸判定不能｜FAIL_INSEN｜5,370円｜💰—｜—
- 4396 System Support Holdings Inc.｜granville_rebound｜✅順調｜⚪妥当｜PASS｜1,315円｜💰13.2万円｜reversal 1315/SL1281（✅即時可）｜📉決算反応日 11/12 📑TOPIX低減対象（次 01/29 第2回/8） 📆SQ
  > 【業態】ITシステム開発。データベースやクラウドの移行・基盤構築を展開。作業管理に強み。
  > 【いま】終値1,315円・直近5日-13.09%・📌連結子会社システムサポートの社員が、Celonisの高度な認定資格「Certified Data Analyst」を国内パートナー企業で初取得のお知らせ
  > 【調子】✅順調（3/13） — E軸判定不能(進捗データ不足)・⚠減速・⚠進捗遅れ
  > 【水準】⚪妥当（4.0/7）— PER12.57倍・PEG0.8358・52週57.2% ／ 💰単元13.2万円
  > 【戦略】当日終値1315円の指値で反転を取りにいく。SL1281円（直近5日安値）
- 4440 WITZ Corp.｜granville_rebound｜➖横ばい｜⚪妥当｜FAIL_INSEN｜1,633円｜💰16.9万円｜—
- 3687 Fixstars Corp.｜granville_rebound｜➖横ばい｜🟡やや割高｜FAIL_INSEN｜1,634円｜💰17.0万円｜—
- 6676 BUFFALO INC.｜granville_rebound｜⚠減速｜⚪妥当｜FAIL_INSEN｜3,190円｜💰32.1万円｜—
- 6203 Howa Machinery, Ltd.｜granville_rebound｜⚠減速｜🟡やや割高｜FAIL_UWAHIGE｜1,995円｜💰20.2万円｜—
- 8360 Yamanashi Chuo Bank, Ltd.｜granville_rebound｜取得不可｜💎割安｜FAIL_INSEN｜1,267円｜💰12.9万円｜—
- 8377 ほくほくフィナンシャルグループ｜granville_rebound｜業績データ取得不可(売上/経常欠損)｜💎割安｜FAIL_INSEN｜765円｜💰7.7万円｜—
- 7380 Juroku Financial Group,Inc.｜granville_rebound｜業績データ取得不可(売上/経常欠損)｜⚪妥当｜FAIL_INSEN｜2,302円｜💰23.3万円｜—
- 8368 Hyakugo Bank, Ltd.｜granville_rebound｜業績データ取得不可(売上/経常欠損)｜⚪妥当｜FAIL_INSEN｜2,059円｜💰21.4万円｜—
- 8551 北日本銀行｜granville_rebound｜取得不可｜⚪妥当｜FAIL_INSEN｜2,214円｜💰23.7万円｜—｜⚡材料後出し
- 7184 富山第一銀行｜granville_rebound｜取得不可｜🟡やや割高｜FAIL_INSEN｜3,095円｜💰32.0万円｜—
- 8713 Fidea Holdings Co.Ltd.｜granville_rebound｜業績データ取得不可(売上/経常欠損)｜🔴過熱｜FAIL_INSEN｜2,534円｜💰25.6万円｜—
- 3565 Ascentech KK｜granville_rebound｜—｜－未評価｜PASS｜453円｜💰—｜reversal 453/SL398（✅即時可）｜📑TOPIX低減対象（次 01/29 第2回/8） 📆SQ
  > 【業態】仮想デスクトップ関連の製品開発、販売。テレワーク強み。クラウドサービスやインフラ構築も。
  > 【いま】終値453円・直近5日+3.19%（材料未確認）
  > 【調子】—（—/13）
  > 【水準】－未評価（次回①-9で算定）（—/7）— PER—倍・PEG—・52週—% ／ 💰単元—
  > 【戦略】当日終値453円の指値で反転を取りにいく。SL398円（直近5日安値）
- 4075 ブレインズテクノロジー｜granville_rebound｜取得不可｜⏸判定不能｜FAIL_INSEN｜1,055円｜💰10.9万円｜—
- 4240 Cluster Technology Co., Ltd.｜granville_rebound｜—｜－未評価｜FAIL_INSEN｜511円｜💰—｜—
- 4768 OTSUKA CORPORATION｜granville_rebound｜—｜－未評価｜PASS｜3,691円｜💰—｜reversal 3691/SL3560（✅即時可）｜⚠日程不明 📆SQ
  > 【業態】独立系SI大手。開発から保守まで一貫。中小に強み。事務用品の販売も。
  > 【いま】終値3,691円・直近5日-2.23%（材料未確認）
  > 【調子】—（—/13）
  > 【水準】－未評価（次回①-9で算定）（—/7）— PER—倍・PEG—・52週—% ／ 💰単元—
  > 【戦略】当日終値3691円の指値で反転を取りにいく。SL3560円（直近5日安値）
- 4884 Kringle Pharma, Inc.｜granville_rebound｜—｜－未評価｜FAIL_INSEN｜519円｜💰—｜—
- 5256 Fusic Co.,Ltd.｜granville_rebound｜—｜－未評価｜FAIL_INSEN｜2,593円｜💰—｜—
- 5599 S&J Corporation｜granville_rebound｜—｜－未評価｜FAIL_INSEN｜1,471円｜💰—｜—
- 6840 ＡＫＩＢＡホールディングス｜granville_rebound｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜608円｜💰6.4万円｜—
- 6890 Ferrotec Corporation｜granville_rebound｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜7,241円｜💰76.2万円｜—
- 7175 Imamura Securities Co.Ltd.｜granville_rebound｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜1,611円｜💰16.1万円｜—
- 8609 岡三証券グループ｜granville_rebound｜業績データ取得不可｜⏸判定不能｜PASS｜1,060円｜💰10.6万円｜reversal 1060/SL925（✅即時可）｜⚠日程不明 📆SQ
  > 【業態】三重地盤の証券準大手。リテールに強み。傘下で証券ジャパンや投信運用会社。
  > 【いま】終値1,060円・直近5日+6.75%（材料未確認）
  > 【調子】業績データ取得不可（—/13） — 通期予想なし
  > 【水準】⏸判定不能（—/7）— PER—倍・PEG—・52週63.2% ／ 💰単元10.6万円
  > 【戦略】当日終値1060円の指値で反転を取りにいく。SL925円（直近5日安値）
- 8739 スパークス・グループ｜granville_rebound｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜2,415円｜💰24.4万円｜—

## 変化点銘柄
- 265A エイチエムコム｜changepoint｜🚀確変｜🟢値頃｜FAIL_INSEN｜668円｜💰6.9万円｜—
- 4011 Headwaters Co.,Ltd｜changepoint｜🚀確変｜🟢値頃｜FAIL_INSEN｜1,844円｜💰19.1万円｜—
- 9888 UEX LTD｜changepoint｜🚀確変｜🟢値頃｜FAIL_UWAHIGE｜1,520円｜💰14.9万円｜—
- 9308 乾汽船｜changepoint｜🚀確変｜⚪妥当｜FAIL_INSEN｜2,241円｜💰23.9万円｜—
- 7695 交換できるくん｜changepoint｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜842円｜💰8.3万円｜—
- 6136 OSG CORP｜changepoint｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜3,552円｜💰35.5万円｜—
- 7318 セレンディップ・ホールディングス｜changepoint｜🔥絶好調｜💎割安｜FAIL_INSEN｜1,086円｜💰11.3万円｜—｜⚡材料後出し
- 5582 （名称取得不可）｜changepoint｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1,740円｜💰17.9万円｜—
- 4443 Ｓａｎｓａｎ｜changepoint｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜2,184円｜💰23.2万円｜—
- 478A Hutzper Inc.｜changepoint｜⚡好調｜⚪妥当｜FAIL_INSEN｜638円｜💰6.6万円｜—
- 8151 東陽テクニカ｜changepoint｜⚡好調｜💎割安｜FAIL_INSEN｜1,838円｜💰17.4万円｜—
- 9343 アイビス｜changepoint｜⚡好調｜⚪妥当｜FAIL_INSEN｜707円｜💰7.2万円｜—
- 4475 None｜changepoint｜⚡好調｜🔴過熱｜FAIL_INSEN｜2,391円｜💰25.9万円｜—
- 218A Liberaware｜changepoint｜⚡好調｜⚪妥当｜FAIL_INSEN｜804円｜💰8.3万円｜—
- 286A ユカリア｜changepoint｜⚡好調｜⚪妥当｜FAIL_INSEN｜751円｜💰7.6万円｜—
- 4483 JMDC｜changepoint｜⚡好調｜🔴過熱｜FAIL_INSEN｜3,850円｜💰39.8万円｜—
- 4071 Plus Alpha Consulting Co. LTD.｜changepoint｜✅順調｜🟡やや割高｜FAIL_UWAHIGE｜2,387円｜💰23.1万円｜—
- 4165 PLAID Inc.｜changepoint｜🔻悪化｜🔴過熱｜FAIL_UWAHIGE｜741円｜💰7.4万円｜—｜⚡材料後出し
- 598A チャットプラス｜changepoint｜✅順調｜⚪妥当｜FAIL_INSEN｜1,057円｜💰10.8万円｜—｜⚡材料後出し
- 6785 鈴木｜changepoint｜✅順調｜🟡やや割高｜FAIL_INSEN｜3,025円｜💰30.1万円｜—
- 339A PROGRESS TECHNOLOGIES GROUP INC｜changepoint｜➖横ばい｜⚪妥当｜FAIL_INSEN｜741円｜💰7.5万円｜—
- 4488 AI inside Inc.｜changepoint｜➖横ばい｜🟡やや割高｜FAIL_UWAHIGE｜1,809円｜💰18.1万円｜—｜⚡材料後出し
- 4259 ExaWizards Inc.｜changepoint｜取得不可｜⚪妥当｜FAIL_UWAHIGE｜601円｜💰7.2万円｜—
- 3923 ラクス｜changepoint｜判定保留(変則決算)｜⚪妥当｜FAIL_INSEN｜1,112円｜💰11.4万円｜—
- 4478 freee K.K.｜changepoint｜取得不可｜⚪妥当｜PASS_DOJI｜4,120円｜💰41.2万円｜⛔型不一致(十字線: トウバ)｜📉決算反応日 11/12 📑TOPIX新規採用（2026-10-30 組入） 🔒実弾封印中(PL3紙ログ収集中)
  > 【業態】スモールビジネス向けクラウドERPサービスの提供。会計や会社設立、開業支援など。
  > 【いま】終値4,120円・直近5日-11.97%（材料未確認）
  > 【調子】取得不可（—/13） — 業績データ取得不可(経常益予想非開示)
  > 【水準】⚪妥当（3.0/7）— PER—倍・PEG—・52週74.8% ／ 💰単元41.2万円
  > 【戦略】発注対象外（⛔型不一致(十字線: トウバ)）
- 3989 シェアテク｜changepoint｜業績データ取得不可｜🟡やや割高｜PASS｜1,539円｜💰15.4万円｜changepoint 1539/SL1532（✅即時可）｜🚨決算直前 11/13(残1営業日) 🔒実弾封印中(PL3紙ログ収集中) 📆SQ
  > 【業態】家庭の生活トラブルに対応するマッチングサイトを運営。登録は便利屋が中心。
  > 【いま】終値1,539円・直近5日-0.58%（材料未確認）
  > 【調子】業績データ取得不可（—/13） — 業績データ取得不可(売上/経常欠損)
  > 【水準】🟡やや割高（2.8/7）— PER14.73倍・PEG—・52週87.5% ／ 💰単元15.4万円
  > 【戦略】発火日終値1539円の指値。追撃禁止・SL1532円。🔒実弾封印中（PL3紙ログ収集中）
- 593A Tier IV, Inc.｜changepoint｜取得不可｜🔴過熱｜FAIL_INSEN｜1,963円｜💰22.1万円｜—

## 🤖AI特需銘柄
波: wave_on なし／25MA 上回り率 エネマネ 14.3%・冷却 25.0%・光 18.2%・基板 4.8%
- 6777 santec｜ai_momentum/ai_reversal｜🚀確変｜⚪妥当｜FAIL_INSEN｜19,970円｜💰209.1万円｜—
- 9824 泉州電業｜ai_momentum/ai_reversal/granville_oshime｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜7,600円｜💰78.3万円｜—
- 6613 QD Laser, Inc.｜ai_momentum/granville_oshime｜🔥絶好調｜🔴過熱｜FAIL_INSEN｜2,079円｜💰21.9万円｜—｜⚡材料後出し
- 6521 オキサイド｜ai_momentum/ai_reversal｜⚡好調｜🟢値頃｜FAIL_INSEN｜3,025円｜💰30.9万円｜—
- 6988 日東電工｜ai_momentum/ai_reversal｜⚡好調｜🟡やや割高｜FAIL_UWAHIGE｜3,490円｜💰34.7万円｜—
- 4063 信越化学工業｜ai_momentum/ai_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜5,791円｜💰57.1万円｜—
- 6367 ダイキン工業｜ai_momentum｜✅順調｜🔴過熱｜FAIL_UWAHIGE｜23,245円｜💰232.3万円｜—
- 1975 新日本空調｜ai_momentum｜➖横ばい｜⚪妥当｜FAIL_INSEN｜3,450円｜💰34.6万円｜—｜⚡材料後出し
- 1982 日比谷総合設備｜ai_momentum/ai_reversal｜➖横ばい｜🔴過熱｜FAIL_INSEN｜3,145円｜💰31.6万円｜—
- 5803 フジクラ｜ai_reversal/changepoint｜🚀確変｜💎割安｜FAIL_INSEN｜3,002円｜💰31.2万円｜—
- 3131 Shinden Hightex Corp.｜ai_reversal/granville_rebound｜🚀確変｜💎割安｜PASS｜7,310円｜💰73.1万円｜reversal 7310/SL4040（✅即時可）｜🤖AI特需 🔬基板・素材/装置・商社 ⚠日程不明 📐進捗 上振れ 32.9% 📆SQ ⚠1単元でリスク枠超過（327000円）
  > 【業態】液晶モジュール、半導体、電子機器、バッテリの専門商社。韓国LG、SK製品が主力。
  > 【いま】終値7,310円・直近5日+61.37%（材料未確認）
  > 【調子】🚀確変（13/13） — 上方修正済み・突出ボーナス・🔼加速・🔼進捗先行
  > 【水準】💎割安（6.0/7）— PER3.44倍・PEG0.0035・52週73% ／ 💰単元73.1万円
  > 【戦略】当日終値7310円の指値で反転を取りにいく。SL4040円（直近5日安値）／⚠1単元リスク327000円（枠超過）
- 4047 関東電化工業｜ai_reversal｜🚀確変｜💎割安｜FAIL_INSEN｜1,767円｜💰18.1万円｜—
- 6918 アバールデータ｜ai_reversal｜🚀確変｜🟢値頃｜FAIL_INSEN｜3,235円｜💰32.7万円｜—｜⚡材料後出し
- 3374 内外テック｜ai_reversal/granville_rebound｜🚀確変｜💎割安｜FAIL_INSEN｜4,000円｜💰41.1万円｜—
- 4062 イビデン｜ai_reversal/granville_rebound｜🚀確変｜🟢値頃｜FAIL_INSEN｜6,344円｜💰69.2万円｜—
- 6857 アドバンテスト｜ai_reversal/changepoint｜🚀確変｜⚪妥当｜FAIL_INSEN｜29,985円｜💰314.4万円｜—
- 5801 古河電気工業｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜2,284円｜💰23.7万円｜—
- 6787 メイコー｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜8,170円｜💰83.2万円｜—
- 8035 東京エレクトロン｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜9,304円｜💰92.7万円｜—
- 6407 CKD｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜4,102円｜💰41.4万円｜—
- 3110 日東紡｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜2,591円｜💰28.0万円｜—
- 4368 扶桑化学工業｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜2,951円｜💰30.2万円｜—
- 6779 Nihon Dempa Kogyo Co., Ltd.｜ai_reversal/granville_rebound｜🔥絶好調｜💎割安｜FAIL_INSEN｜1,866円｜💰19.8万円｜—
- 2760 東京エレクトロンデバイス｜ai_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜4,025円｜💰39.9万円｜—
- 4971 メック｜ai_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜5,380円｜💰57.3万円｜—
- 6235 オプトラン｜ai_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜2,286円｜💰22.9万円｜—
- 6762 TDK｜ai_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜2,337円｜💰23.7万円｜—
- 6981 村田製作所｜ai_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜5,224円｜💰54.6万円｜—
- 7729 東京精密｜ai_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜13,290円｜💰134.9万円｜—
- 6323 ローツェ｜ai_reversal｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜3,276円｜💰33.6万円｜—
- 7735 SCREENホールディングス｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜8,619円｜💰87.8万円｜—
- 6941 山一電機｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜6,710円｜💰69.6万円｜—
- 6524 湖北工業｜ai_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜4,555円｜💰48.2万円｜—｜⚡材料後出し
- 5384 フジミインコーポレーテッド｜ai_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜2,962円｜💰30.1万円｜—
- 6752 パナソニックHD｜ai_reversal/granville_rebound｜⚡好調｜🟢値頃｜FAIL_INSEN｜3,217円｜💰32.6万円｜—
- 6336 石井表記｜ai_reversal/granville_rebound｜⚡好調｜💎割安｜FAIL_INSEN｜1,211円｜💰12.7万円｜—
- 1961 三機工業｜ai_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,393円｜💰24.1万円｜—
- 6227 AIMECHATEC Ltd.｜ai_reversal/granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜4,660円｜💰48.5万円｜—
- 6971 京セラ｜ai_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜3,018円｜💰30.1万円｜—
- 3436 SUMCO｜ai_reversal｜⚡好調｜💎割安｜FAIL_INSEN｜2,170円｜💰20.9万円｜—｜⚡材料後出し
- 4022 ラサ工業｜ai_reversal｜⚡好調｜💎割安｜FAIL_UWAHIGE｜1,377円｜💰14.3万円｜—
- 4973 JCU｜ai_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜4,070円｜💰41.2万円｜—
- 6590 芝浦メカトロニクス｜ai_reversal｜✅順調｜🟢値頃｜FAIL_INSEN｜2,926円｜💰29.2万円｜—
- 255A GLテクノHD｜ai_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜4,075円｜💰41.0万円｜—
- 5706 三井金属鉱業｜ai_reversal｜🔻悪化｜⚪妥当｜FAIL_INSEN｜1,618円｜💰16.7万円｜—
- 5208 Arisawa Mfg.Co., Ltd.｜ai_reversal/granville_oshime｜✅順調｜🔴過熱｜FAIL_INSEN｜2,311円｜💰23.3万円｜—
- 6965 浜松ホトニクス｜ai_reversal｜✅順調｜🔴過熱｜FAIL_INSEN｜2,205円｜💰23.6万円｜—
- 3103 ユニチカ｜ai_reversal/granville_rebound｜⚠減速｜💎割安｜FAIL_INSEN｜1,227円｜💰13.1万円｜—
- 6501 日立製作所｜ai_reversal｜✅順調｜🟡やや割高｜FAIL_INSEN｜4,981円｜💰49.5万円｜—
- 2802 味の素｜ai_reversal｜➖横ばい｜⚪妥当｜PASS_DOJI｜4,260円｜💰42.6万円｜⛔型不一致(十字線: トウバ)｜🤖AI特需 🔬基板・素材/中流 ⚠日程不明
  > 【業態】総合食品会社で調味料首位。冷凍食、医薬品、飼料や電子材など多角展開。
  > 【いま】終値4,260円・直近5日-12.56%（材料未確認）
  > 【調子】➖横ばい（2/13） — 税引前代替・経常非開示(IFRS等)のため最終益成長率で代替・質注意・E軸判定不能(進捗データ不足)
  > 【水準】⚪妥当（4.0/7）— PER29.98倍・PEG—・52週32.2% ／ 💰単元42.6万円
  > 【戦略】発注対象外（⛔型不一致(十字線: トウバ)）
- 9503 関西電力｜ai_reversal｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜2,672円｜💰26.4万円｜—
- 5302 日本カーボン｜ai_reversal｜➖横ばい｜🔴過熱｜PASS｜4,845円｜💰48.5万円｜⛔提案なし(指名鮮度切れ 18営業日)｜🤖AI特需 🔬基板・素材/上流 ⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8） 📐進捗 上振れ 11.0%
  > 【業態】炭素製品の大手。電極や半導体向け特殊品、炭素繊維、リチウム電池向けなど。
  > 【いま】終値4,845円・直近5日+1.57%（材料未確認）
  > 【調子】➖横ばい（2/13） — 質注意・経常減益-9.9%・🔼進捗先行
  > 【水準】🔴過熱（1.0/7）— PER18.9倍・PEG—・52週44.9% ／ 💰単元48.5万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 18営業日)）
- 6617 東光高岳｜ai_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜5,130円｜💰51.8万円｜—
- 4203 住友ベークライト｜ai_reversal/granville_rebound｜業績データ取得不可｜⚪妥当｜FAIL_INSEN｜7,428円｜💰75.7万円｜—
- 9434 ソフトバンク｜ai_reversal｜業績データ取得不可(経常益予想非開示)｜⚪妥当｜PASS｜237円｜💰2.4万円｜⛔型不一致: 既に支持帯以下｜🤖AI特需 🏢大型・指数寄与/投資通信
  > 【業態】ソフトバンクグループの中核。携帯・固定通信ネットワーク基盤にICTソリューションを提供。
  > 【いま】終値237円・直近5日-2.74%（材料未確認）
  > 【調子】業績データ取得不可(経常益予想非開示)（—/13） — 経常欠損
  > 【水準】⚪妥当（4.0/7）— PER20.64倍・PEG—・52週69.2% ／ 💰単元2.4万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 6146 ディスコ｜ai_reversal｜取得不可｜⏸判定不能｜FAIL_INSEN｜47,370円｜💰475.8万円｜—
- 6723 ルネサスエレクトロニクス｜ai_reversal｜取得不可｜⏸判定不能｜FAIL_INSEN｜2,840円｜💰29.2万円｜—
- 9984 ソフトバンクグループ｜ai_reversal｜業績データ取得不可(経常益予想非開示)｜⏸判定不能｜FAIL_INSEN｜3,738円｜💰38.5万円｜—

## ⚡材料後出し
その日の足は開示前の情報。判定は参考値
- 1435 robot home Inc.｜FAIL_INSEN｜📊 FY2026 3Q Financial Results Briefing Materials
- 4377 ONE CAREER Inc.｜FAIL_INSEN｜📊 [Summary] Consolidated Financial Results for the Nine Months Ended September 30, 2026 (Under Japanese GAAP)
- 5537 AlbaLink Co.,Ltd.｜FAIL_INSEN｜📊 2026年12月期 第３四半期決算短信〔日本基準〕（非連結）
- 9560 PROGRIT, Inc.｜FAIL_INSEN｜📌 有償ストック・オプション（新株予約権）の発行内容確定に関するお知らせ
- 558A SQUEEZE Inc.｜FAIL_UWAHIGE｜📊 FY26Q3_Financial Results
- 5034 unerry, Inc.｜FAIL_INSEN｜📊 Presentation Material for First Quarter Ending June 2027 Financial Results
- 4743 ITFOR Inc.｜PASS｜📊 FY2026 Q2 Financial Results Briefing Material
- 4379 Photosynth inc.｜FAIL_INSEN｜📊 2026年12月期第３四半期決算短信〔日本基準〕(連結)
- 7433 Hakuto Co., Ltd.｜FAIL_INSEN｜📊 Consolidated Financial Results  for the Six Months Ended September 30, 2026  (Under Japanese GAAP)
- 167A リョーサン菱洋ホールディングス（リョー菱ＨＤ）｜FAIL_INSEN｜📊 Notice Concerning Extraordinary Financial Results
- 268A Rigaku Holdings Corporation｜FAIL_INSEN｜📌 Corporate Governance Report
- 6750 エレコム｜PASS｜📊 Consolidated Financial Results for the First Six Months Ended September 30, 2026
- 6055 Japan Material Co., Ltd.｜FAIL_INSEN｜📊 Consolidated Financial Results for the Six Months Ended September 30, 2026 [Japanese GAAP]
- 7278 Exedy Corporation｜PASS｜📊 (Correction  Correction of Numerical data) Notice concerning Partial Corrections to FY2026 2Q (Semi-annual) Consolidated Financial Results〔IFRS〕
- 4980 Dexerials Corp.｜FAIL_INSEN｜📌 Dexerials CG Report English Translation
- 3591 WACOAL HOLDINGS CORP｜PASS｜📊 2027年3月期第2四半期（中間期）決算短信[ＩＦＲＳ]（連結）
- 3498 霞ヶ関Ｃ｜FAIL_INSEN｜📌 独立役員届出書
- 6613 QD Laser, Inc.｜FAIL_INSEN｜📊 Quarterly Financial Results Briefing Second Quarter of FY2026
- 1975 新日本空調｜FAIL_INSEN｜📌 Notice of dividend of surplus (Interim Dividend)
- 6918 アバールデータ｜FAIL_INSEN｜📊 2027年３月期　第２四半期（中間期）決算短信〔日本基準〕（非連結）
- 6524 湖北工業｜FAIL_INSEN｜📊 Financial Results Materials First Nine Months of FY12/2026
- 3436 SUMCO｜FAIL_INSEN｜📊 Consolidated Financial Results for the Nine Months Ended September 30, 2026 (Completion of Interim Review by an Independent Auditor)
- 5254 Arent, Inc.｜FAIL_INSEN｜📊 2027年6月期 第1四半期決算短信〔日本基準〕（連結）
- 9742 アイネス｜FAIL_INSEN｜📊 [Updated]Consolidated Financial Results for the Six Months Ended September 30, 2026
- 3405 クラレ｜FAIL_INSEN｜📌 法定事前開示書類（合併）（クラレ西条株式会社）
- 3496 アズーム｜FAIL_INSEN｜📊 Financial Results Briefing Materials for the Fiscal Year Ended September 30,2026
- 8804 東京建物｜PASS｜📊 [Summary]Consolidated Financial Results for the Nine Months Ended September 30, 2026 (Under Japanese GAAP)
- 6412 Heiwa Holdings Inc.｜PASS｜📊 2027年３月期  第２四半期（中間期）決算短信〔日本基準〕（連結）
- 3549 クスリのアオキホールディングス｜FAIL_INSEN｜🔁 自己株式の取得状況に関するお知らせ
- 4166 Cacco, Inc.｜FAIL_INSEN｜📌 CaccoグループのAnycloud、既存SFAからの移行に対応し、自社の業務に合わせて構築・保有できる「Anycloud オウンドSFA」の提供を開始
- 3182 オイシックス｜FAIL_INSEN｜📊 2027年３月期第２四半期（中間期）決算短信〔日本基準〕(連結)
- 4765 ＳＢＩグローバルアセットマネジメント｜FAIL_INSEN｜📌 SBI アセットマネジメントの高配当・増配株式ファンドの純資産総額が7,000億円を突破
- 6036 ＫｅｅＰｅｒ技研｜FAIL_INSEN｜📌 Announcement of the Opening of -KeePer LABO Kyoto Ginkakuji
- 3040 ソリトンシステムズ｜FAIL_INSEN｜📊 [Summary]Consolidated Financial Results for the Nine Months Ended September 30, 2026 (Under Japanese GAAP)
- 4398 ブロードバンドセキュリティ｜FAIL_UWAHIGE｜📊 2027年６月期　第1四半期決算短信〔日本基準〕（非連結）
- 5036 日本ビジネスシステムズ｜FAIL_INSEN｜📊 Consolidated Financial Results for the Year Ended September 30, 2026
- 338A ZenmuTech,Inc.｜FAIL_INSEN｜📊 2026年12月期 第３四半期決算短信〔日本基準〕（非連結）
- 3692 ＦＦＲＩセキュリティ｜FAIL_INSEN｜📊 令和９年３月期 第２四半期（中間期）決算短信補足説明資料
- 9166 GENDA Inc.｜FAIL_INSEN｜📌 「幽遊白書」のぬいぐるみを北米拠点にて展開開始
- 336A ダイナミックマッププラットフォーム｜FAIL_INSEN｜📊 2027年３月期第２四半期（中間期）決算短信〔日本基準〕(連結)
- 3993 PKSHA Technology, Inc.｜FAIL_INSEN｜📊 [Summary] Financial Results for the Year Ended September 30, 2026
- 6862 ミナト HD｜FAIL_INSEN｜📊 2027年３月期第２四半期（中間期）決算短信〔日本基準〕(連結)
- 3691 DIGITAL PLUS, Inc.｜FAIL_INSEN｜📌 リロクラブの国内最大級「福利厚生倶楽部」へデジタルギフトを提供開始
- 4419 Finatext Holdings Ltd.｜FAIL_INSEN｜📊 Financial Results for Q2 FY2026
- 150A ＪＳＨ｜FAIL_INSEN｜📊 2027年３月期第２四半期（中間期）決算短信〔日本基準〕(連結)
- 7715 長野計器｜FAIL_INSEN｜📊 Consolidated Financial Results for the Second Quarter (Six Months) Ended September 30, 2026 (Based on Japanese GAAP)
- 6490 ＰＩＬＬＡＲ｜FAIL_INSEN｜📊 Notice Concerning Revisions to Consolidated Financial Results Forecasts
- 8551 北日本銀行｜FAIL_INSEN｜📊 [Summary]Consolidated Financial Results for the Six Months Ended September 30, 2026(Under Japanese GAAP)
- 7318 セレンディップ・ホールディングス｜FAIL_INSEN｜📌 「セレンディップ・スタンダード」を軸とした独自のホールディング経営 ～Danaherの経営手法から得た示唆と、当社独自の実践を紹介～
- 4165 PLAID Inc.｜FAIL_UWAHIGE｜📊 Consolidated Financial Results for the 4th Quarter of the Fiscal Year Ending December 31, 2026
- 598A チャットプラス｜FAIL_INSEN｜📊 2027年６月期第１四半期決算短信〔日本基準〕（非連結）
- 4488 AI inside Inc.｜FAIL_UWAHIGE｜📊 2027年３月期第２四半期（中間期）決算短信〔日本基準〕(非連結)

## 📢開示
使用した一覧: https://kabutan.jp/disclosures/?date=20261112 （1〜131頁）＋ https://kabutan.jp/disclosures/?date=20261111 （前回実行 20:40 以降の分・1頁）・取得1967件。見出しをそのまま転記（解釈なし）。フォールバック: なし。①-9へ引き渡し（recalc_queue 追加）54件
- 📢 3968 セグエグループ｜通期連結業績予想の修正（上方修正）及び期末配当予想の修正（増配）に関するお知らせ｜11-12 11:30
- 📊 3968 セグエグループ｜Supplementary Explanation Materials for Q3 FY12 2026 Financial Results｜11-12 11:30
- 📊 3968 セグエグループ｜Consolidated Financial Results for the Nine Months Ended September 30, 2026 (Under Japanese GAAP)｜11-12 11:30
- 📊 1435 robot home Inc.｜FY2026 3Q Financial Results Briefing Materials｜11-12 15:30
- 📊 1435 robot home Inc.｜Consolidated Financial Results for the Nine Months Ended September 30,2026｜11-12 15:30
- 📊 1435 robot home Inc.｜2026年12月期　第３四半期決算短信〔日本基準〕（連結）｜11-12 15:30
- 📊 150A ＪＳＨ｜2027年３月期第２四半期（中間期）決算短信〔日本基準〕(連結)｜11-12 15:30
- 📌 150A ＪＳＨ｜第11期連結業績予想修正及び中期事業計画の修正に関するお知らせ｜11-12 15:30
- 📌 150A ＪＳＨ｜グループ分社化に向けた検討開始に関するお知らせ｜11-12 15:30
- 📊 167A リョーサン菱洋ホールディングス（リョー菱ＨＤ）｜Notice Concerning Extraordinary Financial Results｜11-12 16:00
- 📊 167A リョーサン菱洋ホールディングス（リョー菱ＨＤ）｜2027年3月期 第2四半期（中間期）決算短信〔日本基準〕（連結）｜11-12 16:00
- 📌 167A リョーサン菱洋ホールディングス（リョー菱ＨＤ）｜リョーサン菱洋、台湾の世界有数の半導体メーカー MediaTekと代理店契約を締結｜11-12 16:00
- 📊 1719 HAZAMA ANDO Corporation｜Consolidated Financial Results for the Six Months Ended September 30, 2026 [Japanese GAAP]｜11-12 14:00
- 📊 1719 HAZAMA ANDO Corporation｜2027年３月期第２四半期（中間期）決算短信〔日本基準〕(連結)｜11-12 14:00
- 📊 1952 Shin Nippon Air Technologies Co., Ltd.｜[Summary]Consolidated Financial Results for the Six Months Ended September 30, 2026 (Under Japanese GAAP)｜11-12 13:00
- 📊 1952 Shin Nippon Air Technologies Co., Ltd.｜2027年3月期 第2四半期（中間期）決算短信〔日本基準〕（連結）｜11-12 13:00
- 📌 1952 Shin Nippon Air Technologies Co., Ltd.｜2027年3月期 第2四半期（中間期）決算説明資料｜11-12 13:00
- 📊 3040 ソリトンシステムズ｜[Summary]Consolidated Financial Results for the Nine Months Ended September 30, 2026 (Under Japanese GAAP)｜11-12 11:30
- 📊 3040 ソリトンシステムズ｜2026年12月期　第３四半期決算短信[日本基準]（連結）｜11-12 11:30
- 📌 3040 ソリトンシステムズ｜2026年12月期　第３四半期決算補足説明資料｜11-12 16:00
- 📊 3106 倉敷紡績｜Notification on Expected Recording of Extraordinary Income (Gain on Sale of Investment Securities) and Revisions to Financial Results Forecasts｜11-12 13:30
- 📊 3106 倉敷紡績｜Consolidated Financial Results for the Six Months Ended September 30, 2026 (Under Japanese GAAP)｜11-12 13:30
- 📊 3106 倉敷紡績｜2027年3月期 第2四半期（中間期）決算短信〔日本基準〕（連結）｜11-12 13:30
- 📊 3182 オイシックス｜2027年３月期第２四半期（中間期）決算短信〔日本基準〕(連結)｜11-12 15:30
- 📌 3182 オイシックス｜シダックスフードサービスの高齢者施設向け給食モデル「元気ごはん with Oisix」今年度10月末時点で新規獲得件数が前年同期比約2倍成長！｜11-12 19:00
- 📌 3182 オイシックス｜家族で行きたい人気和食店の味が、自宅のレンジで5分温めるだけで食べられる！【デリOisix】初の大戸屋監修メニューを販売開始｜11-12 19:00
- 📊 336A ダイナミックマッププラットフォーム｜2027年３月期第２四半期（中間期）決算短信〔日本基準〕(連結)｜11-12 15:31
- 📌 336A ダイナミックマッププラットフォーム｜ダイナミックマッププラットフォーム、2027年３月期第２四半期決算を発表　フィジカルAI向けData for AIの事業展開が進展｜11-12 15:31
- 📌 336A ダイナミックマッププラットフォーム｜令和８年熊本地震に伴う特別損失の計上に関するお知らせ｜11-12 15:31
- 📊 338A ZenmuTech,Inc.｜2026年12月期 第３四半期決算短信〔日本基準〕（非連結）｜11-12 15:30
- 📌 338A ZenmuTech,Inc.｜2026年12月期 第３四半期 決算説明資料｜11-12 15:30
- 📊 3436 SUMCO｜Consolidated Financial Results for the Nine Months Ended September 30, 2026 (Completion of Interim Review by an Independent Auditor)｜11-12 17:40
- 📊 3436 SUMCO｜2026年12月期 第3四半期決算短信〔日本基準〕（連結）（公認会計士等による期中レビューの完了）｜11-12 17:40
- 📊 3496 アズーム｜Financial Results Briefing Materials for the Fiscal Year Ended September 30,2026｜11-12 15:30
- 📊 3496 アズーム｜Consolidated Financial Results for the Fiscal Year Ended September 30, 2026(Under Japanese GAAP)｜11-12 15:30
- 📊 3496 アズーム｜2026年９月期決算短信〔日本基準〕（連結）｜11-12 15:30
- 📊 3591 WACOAL HOLDINGS CORP｜2027年3月期第2四半期（中間期）決算短信[ＩＦＲＳ]（連結）｜11-12 16:00
- 🔁 3591 WACOAL HOLDINGS CORP｜自己株式の取得に係る事項の決定および自己株式の消却に関するお知らせ｜11-12 16:00
- 📌 3591 WACOAL HOLDINGS CORP｜Notice Regarding Decision to Sell Fixed Assets｜11-12 16:00
- 📊 3692 ＦＦＲＩセキュリティ｜令和９年３月期 第２四半期（中間期）決算短信補足説明資料｜11-12 15:30
- 📊 3692 ＦＦＲＩセキュリティ｜令和９年３月期 第２四半期（中間期）決算短信〔日本基準〕（連結）｜11-12 15:30
- 📊 3696 セレス｜Consolidated Financial Results for the Nine Months Ended September 30, 2026｜11-12 12:00
- 📊 3696 セレス｜2026年12月期 第３四半期決算短信〔日本基準〕（連結）｜11-12 12:00
- 📦 3696 セレス｜SBIホールディングス株式会社との資本業務提携契約締結に関するお知らせ｜11-12 12:00
- 📊 3993 PKSHA Technology, Inc.｜[Summary] Financial Results for the Year Ended September 30, 2026｜11-12 16:00
- 📊 3993 PKSHA Technology, Inc.｜2026年９月期 決算短信〔ＩＦＲＳ〕（連結）｜11-12 16:00
- 📌 3993 PKSHA Technology, Inc.｜Notice Concerning Differences Between Full-Year Earnings Forecasts and Actual Results for the Fiscal Year Ended September 30, 2026｜11-12 16:00
- 📊 4044 Central Glass Co., Ltd.｜Consolidated Financial Results for the Six Months Ended September 30, 2026｜11-12 13:00
- 📊 4044 Central Glass Co., Ltd.｜2027年3月期 第2四半期（中間期）決算短信〔日本基準〕（連結）｜11-12 13:00
- 📌 4044 Central Glass Co., Ltd.｜Notice of Differences between Consolidated Financial Forecast and Actual Results for the First Half and Revision of Financial Forecast for FY2026｜11-12 13:00
- 📊 4045 Toagosei Co., Ltd.｜[Updated] Consolidated Financial Results for the Nine Months Ended September 30, 2026 (Under Japanese GAAP)｜11-12 11:00
- 📊 4165 PLAID Inc.｜Consolidated Financial Results for the 4th Quarter of the Fiscal Year Ending December 31, 2026｜11-12 15:30
- 📊 4165 PLAID Inc.｜2026年12月期 第4四半期決算短信〔日本基準〕（連結）｜11-12 15:30
- 📌 4165 PLAID Inc.｜Announcement Regarding Disposal of Treasury Shares as Restricted Stock to Executive Officers｜11-12 15:30
- 📊 4377 ONE CAREER Inc.｜[Summary] Consolidated Financial Results for the Nine Months Ended September 30, 2026 (Under Japanese GAAP)｜11-12 15:30
- 📊 4377 ONE CAREER Inc.｜2026年12月期 第３四半期決算短信〔日本基準〕（連結）｜11-12 15:30
- 📌 4377 ONE CAREER Inc.｜Notice Regarding Revision of Dividend Forecast (Dividend Increase)｜11-12 15:30
- 📊 4379 Photosynth inc.｜2026年12月期第３四半期決算短信〔日本基準〕(連結)｜11-12 15:30
- 📌 4379 Photosynth inc.｜2026年12月期 第3四半期 決算説明資料（スマホ版サマリ）｜11-12 15:30
- 📌 4379 Photosynth inc.｜2026年12月期 第3四半期 決算説明資料｜11-12 15:30
- 📊 4398 ブロードバンドセキュリティ｜2027年６月期　第1四半期決算短信〔日本基準〕（非連結）｜11-12 16:30
- 📌 4398 ブロードバンドセキュリティ｜2027年６月期　第１四半期決算説明資料｜11-12 16:30
- 📌 4398 ブロードバンドセキュリティ｜「Gomez資産運用会社サイトランキング2026」の発表について｜11-12 13:00
- 📊 4419 Finatext Holdings Ltd.｜Financial Results for Q2 FY2026｜11-12 15:30
- 📊 4419 Finatext Holdings Ltd.｜2027年３月期第２四半期（中間期）決算短信〔日本基準〕(連結)｜11-12 15:30
- 📌 4419 Finatext Holdings Ltd.｜株式報酬型ストック・オプション（新株予約権）の発行内容確定に関するお知らせ｜11-12 15:30
- 📊 4488 AI inside Inc.｜2027年３月期第２四半期（中間期）決算短信〔日本基準〕(非連結)｜11-12 15:35
- 📌 4488 AI inside Inc.｜連結決算への移行に伴う連結業績予想の公表に関するお知らせ｜11-12 15:35
- 📌 4488 AI inside Inc.｜2027年３月期 第２四半期決算説明資料｜11-12 15:35
- 📊 4743 ITFOR Inc.｜FY2026 Q2 Financial Results Briefing Material｜11-12 15:30
- 📊 4743 ITFOR Inc.｜2027年3月期 第2四半期(中間期)決算短信〔日本基準〕(連結)｜11-12 15:30
- 📊 4743 ITFOR Inc.｜Consolidated Financial Results for the Six Months Ended September 30, 2026 (Under Japanese GAAP)｜11-12 15:30
- 📊 5034 unerry, Inc.｜Presentation Material for First Quarter Ending June 2027 Financial Results｜11-12 15:30
- 📊 5034 unerry, Inc.｜Summary of Consolidated Financial Results for the Three Months Ended September 30, 2026 (Under Japanese GAAP)｜11-12 15:30
- 📊 5034 unerry, Inc.｜2027年６月期 第１四半期 決算短信〔日本基準〕(連結)｜11-12 15:30
- 📊 5036 日本ビジネスシステムズ｜Consolidated Financial Results for the Year Ended September 30, 2026｜11-12 15:30
- 📊 5036 日本ビジネスシステムズ｜2026年９月期  決算短信〔日本基準〕（連結）｜11-12 15:30
- 📌 5036 日本ビジネスシステムズ｜Notice Regarding Change in Reportable Segments｜11-12 15:30
- 📊 5243 ｎｏｔｅ｜Main Questions and Answers on the Q3 FY2026 Financial Results｜11-12 11:00
- 📌 5243 ｎｏｔｅ｜投資家の皆さまから多く寄せられた質問と回答（2026年11月期第3四半期決算）｜11-12 11:00
- 📊 5254 Arent, Inc.｜2027年6月期 第1四半期決算短信〔日本基準〕（連結）｜11-12 16:00
- 📌 5254 Arent, Inc.｜2027年6月期第1四半期決算説明資料｜11-12 16:00
- 📊 5537 AlbaLink Co.,Ltd.｜2026年12月期 第３四半期決算短信〔日本基準〕（非連結）｜11-12 16:00
- 📌 5537 AlbaLink Co.,Ltd.｜株式分割及び株式分割に伴う定款の一部変更に関するお知らせ｜11-12 16:00
- 📌 5537 AlbaLink Co.,Ltd.｜ストック・オプション（無償ストック・オプション及び有償ストック・オプション）の発行に関するお知らせ｜11-12 16:00
- 📊 558A SQUEEZE Inc.｜FY26Q3_Financial Results｜11-12 15:30
- 📊 558A SQUEEZE Inc.｜2026年12月期第３四半期決算短信〔日本基準〕(連結)｜11-12 15:30
- 📌 558A SQUEEZE Inc.｜有償ストック・オプション（新株予約権）の発行に関するお知らせ｜11-12 15:30
- 📊 598A チャットプラス｜2027年６月期第１四半期決算短信〔日本基準〕（非連結）｜11-12 15:30
- 📌 598A チャットプラス｜2027年６月期第１四半期決算説明資料｜11-12 15:30
- 📊 6055 Japan Material Co., Ltd.｜Consolidated Financial Results for the Six Months Ended September 30, 2026 [Japanese GAAP]｜11-12 15:40
- 📊 6055 Japan Material Co., Ltd.｜2027年３月期 第２四半期（中間期）決算短信〔日本基準〕（連結）｜11-12 15:40
- 📊 6250 Yamabiko Corporation｜Consolidated Financial Results for the Nine Months Ended September 30,2026｜11-12 14:00
- 📊 6250 Yamabiko Corporation｜2026年12月期 第3四半期 決算短信〔日本基準〕（連結）｜11-12 14:00
- 📊 6412 Heiwa Holdings Inc.｜2027年３月期  第２四半期（中間期）決算短信〔日本基準〕（連結）｜11-12 15:30
- 📊 6412 Heiwa Holdings Inc.｜[Summary]Consolidated Financial Results for the Six Months Ended September 30, 2026 (Under Japanese GAAP)｜11-12 15:30
- 📊 6490 ＰＩＬＬＡＲ｜Notice Concerning Revisions to Consolidated Financial Results Forecasts｜11-12 15:30
- 📊 6490 ＰＩＬＬＡＲ｜Consolidated Financial Results for the Six Months Ended September 30,2026｜11-12 15:30
- 📊 6490 ＰＩＬＬＡＲ｜2027年3月期 第2四半期（中間期）決算短信〔日本基準〕（連結）｜11-12 15:30
- 📊 6524 湖北工業｜Financial Results Materials First Nine Months of FY12/2026｜11-12 15:30
- 📊 6524 湖北工業｜Consolidated Financial Results for the Nine Months Ended September 30, 2026 (Under Japanese GAAP)｜11-12 15:30
- 📊 6524 湖北工業｜2026年12月期 第３四半期決算短信〔日本基準〕(連結)｜11-12 15:30
- 📊 6613 QD Laser, Inc.｜Quarterly Financial Results Briefing Second Quarter of FY2026｜11-12 16:00
- 📊 6613 QD Laser, Inc.｜[Summary]Non-consolidated Financial Results for the Six Months Ended September 30, 2026 (Under Japanese GAAP)｜11-12 16:00
- 📊 6613 QD Laser, Inc.｜2027年３月期第２四半期（中間期）決算短信〔日本基準］（非連結）｜11-12 16:00
- 📊 6750 エレコム｜Consolidated Financial Results for the First Six Months Ended September 30, 2026｜11-12 15:30
- 📊 6750 エレコム｜2027年3月期 第2四半期（中間期）決算短信〔日本基準］（連結）｜11-12 15:30
- 📌 6750 エレコム｜Notice of Dividend Payment (Interim Dividend)｜11-12 15:30
- 📊 6787 メイコー｜FY2026 Q2 Financial Results Briefing｜11-12 09:30
- 📌 6787 メイコー｜2026年度上期 決算説明会資料｜11-12 09:30
- 📊 6845 アズビル｜（訂正）「2027年３月期　第２四半期（中間期）決算短信〔ＩＦＲＳ〕（連結）」の一部訂正について｜11-11 18:59
- 📊 6845 アズビル｜[Delayed] Notification Regarding Correction to FY2026 Second Quarter Consolidated Financial Results (IFRS)｜11-12 08:55
- 🔁 6845 アズビル｜（訂正）「自己株式の取得状況及び取得終了」及び「自己株式の取得及び消却」に関するお知らせの一部訂正について｜11-11 18:59
- 📊 6862 ミナト HD｜2027年３月期第２四半期（中間期）決算短信〔日本基準〕(連結)｜11-12 15:30
- 📌 6862 ミナト HD｜業績予想の修正に関するお知らせ｜11-12 15:30
- 📌 6862 ミナト HD｜2027年３月期　第２四半期決算説明資料｜11-12 15:30
- 📊 6918 アバールデータ｜2027年３月期　第２四半期（中間期）決算短信〔日本基準〕（非連結）｜11-12 15:30
- 📊 7278 Exedy Corporation｜(Correction  Correction of Numerical data) Notice concerning Partial Corrections to FY2026 2Q (Semi-annual) Consolidated Financial Results〔IFRS〕｜11-12 16:00
- 📊 7278 Exedy Corporation｜（訂正・数値データ訂正）「2027年３月期　第２四半期（中間期）決算短信〔ＩＦＲＳ〕（連結）」の一部訂正について｜11-12 16:00
- 📊 7433 Hakuto Co., Ltd.｜Consolidated Financial Results  for the Six Months Ended September 30, 2026  (Under Japanese GAAP)｜11-12 15:30
- 📊 7433 Hakuto Co., Ltd.｜[Summary] Financial Results for the Six Months Ended September 30, 2026｜11-12 15:30
- 📊 7433 Hakuto Co., Ltd.｜2027年３月期　第２四半期（中間期）決算短信〔日本基準〕（連結）｜11-12 15:30
- 📊 7567 Sakae Electronics Corp.｜2027年3月期第2四半期（中間期）決算短信（日本基準）（連結）｜11-12 11:00
- 📌 7567 Sakae Electronics Corp.｜2027年3月期第2四半期決算補足説明資料（データシート）｜11-12 11:00
- 📌 7567 Sakae Electronics Corp.｜2027年3月期第2四半期決算補足説明資料｜11-12 11:00
- 📊 7715 長野計器｜Consolidated Financial Results for the Second Quarter (Six Months) Ended September 30, 2026 (Based on Japanese GAAP)｜11-12 15:30
- 📊 7715 長野計器｜2027年３月期  第２四半期（中間期）決算短信〔日本基準〕（連結）｜11-12 15:30
- 📌 7715 長野計器｜Notice Concerning Capital Investment (Construction of New Plants)｜11-12 15:30
- 📊 7734 Riken Keiki Co., Ltd.｜Consolidated Financial Results for the Six Months Ended September 30, 2026｜11-12 11:30
- 📊 7734 Riken Keiki Co., Ltd.｜2027年３月期　第２四半期（中間期）決算短信〔日本基準〕(連結)｜11-12 11:30
- 📌 7734 Riken Keiki Co., Ltd.｜CORPORATE GOVERNANCE REPORT｜11-12 12:10
- 📊 8345 Bank of Iwate Ltd.｜Notice Regarding Revisions to Financial Results Forecasts,Dividends of Surplus(Interim Dividend/Increase), and Revision of Year-End Dividend Forecasts｜11-12 14:00
- 📊 8345 Bank of Iwate Ltd.｜[Summary]Consolidated Financial Results for the Six Months Ended September 30, 2026 (Under Japanese GAAP)｜11-12 14:00
- 📊 8345 Bank of Iwate Ltd.｜2027年3月期 第2四半期（中間期）決算短信〔日本基準〕（連結）｜11-12 14:00
- 📊 8381 San-in Godo Bank Ltd.｜[Summary]Consolidated Financial Results for the Six Months Ended September 30, 2026 (Under Japanese GAAP)｜11-12 13:00
- 📊 8381 San-in Godo Bank Ltd.｜2027年3月期 第2四半期（中間期）決算短信〔日本基準〕(連結)｜11-12 13:00
- 📌 8381 San-in Godo Bank Ltd.｜Announcement regarding the Revision of the Earnings Forecast and the Upward Revision of the Dividend Forecast for FY2026｜11-12 13:00
- 📊 8551 北日本銀行｜[Summary]Consolidated Financial Results for the Six Months Ended September 30, 2026(Under Japanese GAAP)｜11-12 15:00
- 📊 8551 北日本銀行｜2027年３月期第２四半期（中間期）決算短信〔日本基準〕(連結)｜11-12 15:00
- 📊 8804 東京建物｜[Summary]Consolidated Financial Results for the Nine Months Ended September 30, 2026 (Under Japanese GAAP)｜11-12 15:30
- 📊 8804 東京建物｜2026年12月期 第３四半期決算短信〔日本基準〕（連結）｜11-12 15:30
- 📌 8804 東京建物｜Notice Regarding Change in Consolidated Subsidiaries (Share Transfer)｜11-12 15:30
- 📊 9742 アイネス｜[Updated]Consolidated Financial Results for the Six Months Ended September 30, 2026｜11-12 17:00
- 🔁 3549 クスリのアオキホールディングス｜自己株式の取得状況に関するお知らせ｜11-12 15:30
- 📌 3549 クスリのアオキホールディングス｜Notice Regarding the Status of Purchase of Treasury Shares｜11-12 15:30
- 📌 1417 MIRAIT ONE Corporation｜2026年度 第２四半期決算説明会 （動画資料）｜11-12 12:00
- 📌 1975 新日本空調｜Notice of dividend of surplus (Interim Dividend)｜11-12 16:00
- 📌 1975 新日本空調｜剰余金の配当（中間配当）に関するお知らせ｜11-12 16:00
- 📌 268A Rigaku Holdings Corporation｜Corporate Governance Report｜11-12 18:00
- 📌 268A Rigaku Holdings Corporation｜コーポレート・ガバナンスに関する報告書 2026/11/12｜11-12 17:47
- 📌 278A Ｔｅｒｒａ　Ｄｒｏｎｅ｜テラドローン子会社 Unifly、欧州最大級の防衛ファンド「EDF」に採択、約 1.5 億円を獲得｜11-12 08:30
- 📌 3036 アルコニックス｜アルコニックス株式会社 2027年3月期　第2四半期　 決算説明資料｜11-12 13:00
- 📌 3405 クラレ｜法定事前開示書類（合併）（クラレ西条株式会社）｜11-12 17:00
- 📌 3498 霞ヶ関Ｃ｜独立役員届出書｜11-12 15:30
- 📌 3498 霞ヶ関Ｃ｜Our Opinion on ISS's Voting Recommendation｜11-12 08:00
- 📌 3498 霞ヶ関Ｃ｜ISS社の議決権行使助言に関する当社の見解について｜11-12 08:00
- 📌 3673 ブロードリーフ｜[Delayed]3Q FY2026 Business Results Briefing Material｜11-12 10:15
- 📌 3673 ブロードリーフ｜[Delayed]Data book 2026｜11-12 10:15
- 📌 3691 DIGITAL PLUS, Inc.｜リロクラブの国内最大級「福利厚生倶楽部」へデジタルギフトを提供開始｜11-12 18:00
- 📌 3927 アークン｜フーバーブレイン、自社開発の業務可視化製品「Eye“247” Work Smart Cloud」にAI分析機能を付加する開発に着手｜11-12 11:30
- 📌 4071 Plus Alpha Consulting Co. LTD.｜顧客の声活用プラットフォーム「見える化エンジン」に、 分析結果から報告資料を自動生成できる「AIレポート作成機能」を新規搭載｜11-12 08:59
- 📌 4166 Cacco, Inc.｜CaccoグループのAnycloud、既存SFAからの移行に対応し、自社の業務に合わせて構築・保有できる「Anycloud オウンドSFA」の提供を開始｜11-12 16:00
- 📌 4169 Enechange Ltd.｜ENECHANGE、エネルギーの「総合ソリューション化」へ─ 太陽光・蓄電池・省エネの提案サービスを開始｜11-12 12:00
- 📌 428A Cypress Holdings Co., Ltd.｜（訂正）第８回定時株主総会の招集に際しての電子提供措置事項｜11-12 08:00
- 📌 428A Cypress Holdings Co., Ltd.｜（訂正）第８回定時株主総会の招集に際しての電子提供措置事項の一部訂正について｜11-12 08:00
- 📌 4375 セーフィー｜セーフィー、屋内から軒下まで設置場所を選ばないクラウドカメラ「Safie UNICAM」の販売を開始｜11-12 12:00
- 📌 4396 System Support Holdings Inc.｜連結子会社システムサポートの社員が、Celonisの高度な認定資格「Certified Data Analyst」を国内パートナー企業で初取得のお知らせ｜11-12 14:30
- 📌 4765 ＳＢＩグローバルアセットマネジメント｜SBI アセットマネジメントの高配当・増配株式ファンドの純資産総額が7,000億円を突破｜11-12 18:20
- 📌 4765 ＳＢＩグローバルアセットマネジメント｜Notice Concerning Setting of Record Date for Convening an Extraordinary General Meeting  of Shareholders｜11-12 11:30
- 📌 4765 ＳＢＩグローバルアセットマネジメント｜臨時株主総会の招集のための基準日設定に関するお知らせ｜11-12 11:30
- 📌 4980 Dexerials Corp.｜Dexerials CG Report English Translation｜11-12 18:00
- 📌 4980 Dexerials Corp.｜コーポレート・ガバナンスに関する報告書 2026/11/12｜11-12 12:40
- 📌 4980 Dexerials Corp.｜デクセリアルズ統合レポート2026｜11-12 00:30
- 📌 5246 ＥＬＥＭＥＮＴＳ｜国産AIリーダーボード「Kurabe（クラベ）」のサービス提供開始に関するお知らせ｜11-12 10:00
- 📌 593A Tier IV, Inc.｜ダンプトラック輸送の自動運転化に向けた 周南バルクターミナル株式会社との協業に関するお知らせ｜11-12 11:30
- 📌 6036 ＫｅｅＰｅｒ技研｜Announcement of the Opening of -KeePer LABO Kyoto Ginkakuji｜11-12 17:00
- 📌 6036 ＫｅｅＰｅｒ技研｜「KeePer LABO 京都銀閣寺店」開店のお知らせ｜11-12 17:00
- 📌 6332 月島ホールディングス｜Other Matters Subject to Electronic Provision Measures(Matters Omitted from the Paper-Based Documents Delivered to Shareholders)｜11-12 08:00
- 📌 6332 月島ホールディングス｜NOTICE OF THE EXTRAORDINARY GENERAL MEETING OF SHAREHOLDERS｜11-12 08:00
- 📌 6332 月島ホールディングス｜臨時株主総会その他電子提供措置事項（交付書面省略事項）｜11-12 08:00
- 📌 6651 NITTO KOGYO Corporation｜コーポレート・ガバナンスに関する報告書 2026/11/12｜11-12 11:18
- 📌 6753 Sharp Corporation｜Notice Regarding the Transfer of Fixed Assets and Recording of Extraordinary Income｜11-12 11:00
- 📌 6753 Sharp Corporation｜固定資産の譲渡及び特別利益の計上に関するお知らせ｜11-12 11:00
- 📌 7318 セレンディップ・ホールディングス｜「セレンディップ・スタンダード」を軸とした独自のホールディング経営 ～Danaherの経営手法から得た示唆と、当社独自の実践を紹介～｜11-12 15:30
- 📌 8198 Maxvalu Tokai Co., Ltd.｜人事異動に関するお知らせ｜11-11 19:00
- 📌 9166 GENDA Inc.｜「幽遊白書」のぬいぐるみを北米拠点にて展開開始｜11-12 15:30
- 📌 9560 PROGRIT, Inc.｜有償ストック・オプション（新株予約権）の発行内容確定に関するお知らせ｜11-12 15:30
- 📌 9697 カプコン｜「Golden Joystick Awards 2026」で『バイオハザード レクイエム』がその年を代表する「Ultimate Game of the Year」を受賞！｜11-12 12:00

## 総当りゲート
### 5手法（277）
- PASS（44）: 1417 1719 1721 1820 1860 1926 1952 1979 2109 2379 3116 3131 3222 3282 3591 3612 3798 4008 446A 4666 4743 505A 5302 5602 6370 6436 6632 6741 6750 6753 7278 7733 8098 8133 8174 8198 8253 8698 8871 8975 9302 9434 9533 9766
- PASS_DOJI（1）: 2802
- FAIL_UWAHIGE（51）: 147A 1944 1951 1960 3091 3569 3696 3843 4022 4042 4088 4216 421A 4272 4286 4293 4471 4503 4746 4771 5018 5101 5444 5463 558A 5757 5932 618A 6332 6349 6367 6454 6758 6804 6845 6988 7003 7004 7148 7276 7567 7678 7942 8084 8194 8616 8714 9204 9412 9948 9960
- FAIL_INSEN（181）: 1435 167A 1946 1961 1963 1975 1982 255A 262A 268A 2760 276A 2930 2975 3036 3077 3103 3105 3110 3374 3433 3436 3445 3479 3498 3556 3915 3994 4021 4028 4047 4053 4058 4062 4063 4176 4203 4205 4368 4377 4379 4410 4417 4434 4477 4565 4634 4933 4966 4971 4973 4980 5019 5027 5034 5132 5136 5137 5186 5208 5246 5301 5310 5331 5333 5344 5384 5482 5537 5631 5703 5706 5711 5801 5803 5821 5831 5832 5844 6055 6071 6135 6146 6227 6235 6268 6278 6284 6302 6323 6324 6336 6340 6366 6368 6407 6418 6448 6471 6473 6479 6481 6501 6505 6516 6521 6524 6532 6588 6590 6613 6617 6645 6651 6652 6668 6674 6723 6724 6752 6754 6762 6777 6779 6787 6807 6810 6814 6857 6875 6918 6923 6925 6941 6960 6965 6971 6981 7167 7177 7186 7220 7322 7366 7381 7384 7433 7713 7721 7729 7731 7735 7995 8035 8154 8304 8334 8336 8345 8354 8359 8366 8367 8370 8381 8386 8393 8399 8522 8524 8600 9072 9110 9503 9560 9722 9824 9902 9934 9962 9984
### グランビル（218）
- PASS（53）: 1878 1941 2384 2488 2492 2502 2811 3565 3778 4169 417A 4396 4432 4507 4523 4540 4549 4554 4568 4674 4768 4848 4912 4922 5105 5184 5233 6412 6523 6592 7269 7744 7747 7921 8016 8056 8095 8159 8160 8255 8609 8697 8801 8803 8804 8944 9006 9045 9075 9509 9536 9842 9956
- FAIL_UWAHIGE（37）: 1928 2206 3092 3371 3850 3968 4044 4045 4206 4208 428A 4382 4398 4401 4403 4534 4552 4902 6099 6203 6328 6371 6470 6574 6947 7213 7480 7606 8051 8113 8167 8410 9163 9401 9418 9735 9837
- FAIL_INSEN（128）: 1436 150A 153A 2489 278A 2897 2962 3002 3040 3042 3106 3156 3182 336A 338A 3405 3491 3496 3549 3563 3673 3687 3691 3692 3762 3793 3851 3891 3927 3935 3964 3993 4005 4025 4075 4100 4166 4240 4258 436A 4373 4375 4413 4419 4440 4498 456A 460A 4617 4667 4765 477A 479A 4884 4968 5036 5243 5252 5254 5256 5367 5381 5532 5574 5599 5838 5892 5985 6027 6036 6080 6138 6191 6250 6317 6432 6490 6508 6570 6676 6736 6742 6744 6745 6768 6769 6834 6840 6862 6877 6890 6958 6963 6998 7175 7184 7256 7380 7609 7715 7725 7734 7806 7826 7970 8012 8061 8137 8344 8360 8361 8362 8364 8368 8377 8388 8392 8395 8551 8713 8739 8995 9166 9278 9304 9552 9697 9742
### 変化点（27）
- PASS（1）: 3989
- PASS_DOJI（1）: 4478
- FAIL_UWAHIGE（5）: 4071 4165 4259 4488 9888
- FAIL_INSEN（20）: 218A 265A 286A 339A 3923 4011 4443 4475 4483 478A 5582 593A 598A 6136 6785 7318 7695 8151 9308 9343
- 除籍: なし

## 機械詳細
- 3日ルール判定（件数のみ）: 判定1銘柄・streak≥3 0・streak=2 0・判定不可0（銘柄別は通知にのみ）
- 検知内訳: 候補92銘柄（新規11・再指名81）・プール522・評価522・SKIP0・日足取得失敗0・未マージPR由来0（直近24時間のリモートブランチ2本はいずれもマージ済み）
- gate_history: gate_history/2026-11-12.json を新規作成（verdicts 522・nominations 92）
- grades.json: 1090銘柄 / 625161 バイト・nx 付与485件・pxd 369件・gyf 非null337（[] 80）・trp 非null50
- method_score: 保持61件/null461件
- ヘッドライン付与: PASS100件中100件（欠落0）・抜粋（通知）10件（method3/ai3/granville2/changepoint2）
- kabutan トップページ新規取得 9件（業態・業種・単元株数。50件上限で打ち切り0件）・業種埋め戻し 1件試行（3480: ページから取得できず未付与）
- profile_cache: 総数1061・本夜の追加8件・業種追加0件・業態「未取得」のまま出た件数 1
- earnings_log: 総数410・本夜追記54件・リターン補完87件・日足が取れず未補完67件
- gyoseki_cache: history 退避0件（本夜は業績再計算を行わず。📊/📢/📉検出銘柄は recalc_queue へ追加 54件）
- pool_bars.json: 524銘柄 / 457183 バイト（1306 を含む）
- 鮮度ゲート: 提案57件／鮮度切れ除外29件・nom_age分布 0-2:170/3-10:228/11+:124・last_seen欠損0件
- 記録の凍結: gate_history verdicts 522件（＝評価522件）・nominations 92件（新規11・再指名81）・業種 付与済み515／未付与7・本夜の埋め戻し0件
- トレンド文脈: ctx 合致70／不一致315／レンジ134／判定不能3・PASS のうち ctx 合致18件・形態が付いた銘柄231件
- 入口の穴（v1.48）: recent_pass 556銘柄（🚨81/📉90/⏰8/📋18/❓349・当夜評価外126）・PASS_DOJI 2件（2802 ⛔型不一致(十字線: トウバ)／4478 ⛔型不一致(十字線: トウバ)）・⏸位置不適 8件（momentum8/oshime0）・⏸トラップ疑い 0件・位置判定不能 0件・1306 取得 可・rs20 付与 522/522・⚠市場に劣後 0件／ℹ相対強い 3件
- 業種別PER中央値: 算出できた業種26・spm を写せた銘柄1017件
- 開示の分類別件数（プール在籍・1銘柄1分類）: 📢1 📊53 🔁1 📌29
- 熟成由来の候補 0件（うちPASS0）
- 権利情報: T+1/T+2 に権利落ちが無いため rights_cache は本夜未更新・優待ページ取得0件
- 次回決算日: 付与487件／未発表（nx null）607件・前年同期発表日 付与369件・earnings_calendar.json 1094銘柄/146672バイト
- 値頃感: 当日終値で再計算98件・静的層なしで未評価2件
- 提案: 型別 {'momentum': 32, 'reversal': 24, 'changepoint': 1}
- 業績グレード: 本夜は kabutan 決算ページの読み取り・再計算を行わずキャッシュ値を使用（📊/📢/📉 は recalc_queue で ①-9 へ引き渡し）
- STEP 4.8 週末ブリーフ: スキップ（week_open=false）
- 📑指数: ix 付与 プール92件（out80/in12）
- master.json の変更行数: +16003/-14660（indent=2 往復一致・results 522件の全置換による。全体再フォーマットではない）
