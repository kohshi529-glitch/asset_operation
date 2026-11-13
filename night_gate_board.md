# 夜間ゲート 2026-11-13

## サマリー
- 評価数: 506 / PASS: 93（PASS_DOJI 7件を含む）
- 発注可能提案数: 50件（✅40／⏳0／⏸位置不適10／⏸トラップ疑い0）
- 市場一言: 市場モード「レンジ様子見」（market.latest 2026-11-13）。プール505銘柄中 PASS比率18.4%（陰線FAIL 305件・上髭FAIL 108件）
- 実行モード: 通常（base_day=当日の引け値を対象）
- base_day: 2026-11-13（run_at 2026-11-13 20:30起動）
- week_open: true（翌営業日 11/16(月)＝週初）→ STEP 4.8 週末ブリーフを実行
- 📆 翌営業日 11/16: カレンダーイベントなし（T+2 11/17: カレンダーイベントなし）
- 📑指数: 低減対象 提案6件／PASS15件／プール75件・新規採用 12件（index_flags 2026-10-07 公表分）・次の TOPIX 低減日 01/29 第2回/8（あと51営業日）

## 検証結果
- V1 → はい（提案50=results50=模擬50=通知母数50）
- V2 → はい（PASS93=提案50+除外43・order_status欠落0）
- V3 → はい（results506件重複0）
- V4 → はい（既存static変更0）
- V5 → はい（変更トップキー['earnings_log', 'night_gate', 'pipeline', 'profile_cache', 'valuation_cache']・pipeline他run不変True・spec不変True・profile既存書換なしTrue）
- V6 → はい（gyoseki_cache不整合0）
- V7 → はい（必須セクション＋📅今週のカタリスト存在）
- V8 → はい（模擬50行 不正0）
- V9 → はい（gate_history と today 一致）
- V10 → はい（base_day一致 2026-11-13）
- V11 → いいえ（+13336/-13450（indent=2・往復一致で検出））
- V12 → はい（並び順 (a)True(b)True(c)True）
- V13 → はい（1092銘柄/609.9KiB・GC∪VC1088全収録True（profile_cache由来+4）・20キーTrue・型True・nx一致True・ix非null224・業種PER中央値26業種）
- V14 → はい（保持55件/null451件・出所不明/不一致0=True・内訳{'granville_oshime': 3, 'kenmo_momentum': 14, 'kenmo_newhigh': 1, 'ai_reversal': 5, 'choruko_reversal': 16, 'stf_kakuhen': 15, 'ai_momentum': 1}）
- V15 → はい（PASS93件中93件に付与（欠落0）・5キーTrue・(c)4項目の未取得/取得不可9（水準の「－未評価」等キャッシュ転記を含む））
- V16 → はい（📊82件全件記録True・grade_beforeは再計算前（本夜は業績再計算なし）・history>4=0・総数492）
- V17 → はい（508銘柄/433.1KiB・先読み0=True・保有1銘柄すべて収録=True・3日ルール判定1銘柄）
- V18 → はい（鮮度切れ21件・誤除外0=True・nom_age分布 0-2:166/3-10:221/11+:119）
- V19 → はい（verdicts506=評価506・nominations83（新規20/再指名63）・集合一致True・ctx判定不能3・(d)True・(e)True）
- V20 → はい（1098銘柄・nx非null445・hist持ち773・pxd371・取得元名称なしTrue）
- V21 → はい（recent_pass545銘柄・出所実在True・保有情報不使用True）
- V22 → はい（PASS_DOJI7・⏸位置不適10誤通過0=True・⏸トラップ0・rs20付与506/506）
- VLEAK → はい（公開物（ボード/today/gate_history）への保有情報 検出0件（保有1銘柄・アラート3件（詳細は通知のみ）））
- 注: V11 は night_gate.results の全置換（506件・indent=2）による実データ差分であり全体再フォーマットではない（往復一致で W=2 を検出し同一幅で書き出し）。前夜（+16003/-14660）と同じ構造的超過

## 保有アラート
保有1銘柄・アラート3件（詳細は通知）

## 🧾直近提案の決算接近
窓内（直近20営業日）の提案銘柄 545・日程不明 306・当夜評価外 128。保有情報は使っていない（候補だった銘柄の日程）
- 🚨決算直前 11/16(残1営業日) 6890 Ferrotec Corporation｜最後の提案 11/11（reversal 7617・✅即時可）｜提案4回｜当夜 FAIL_INSEN
- 🚨決算直前 11/16(残1営業日) 478A Hutzper Inc.｜最後の提案 11/10（changepoint 668・✅即時可）｜提案5回｜当夜 FAIL_UWAHIGE
- 🚨決算直前 11/16(残1営業日) 5105 ＴＯＹＯ　ＴＩＲＥ｜最後の提案 11/09（momentum 4249・✅即時可）｜提案2回｜当夜 PASS
- 🚨決算直前 11/16(残1営業日) 5582 （名称取得不可）｜最後の提案 10/29（changepoint 1819・✅即時可）｜提案4回｜当夜 PASS
- 🚨決算直前 11/16(残1営業日) 7047 PORT INC.｜最後の提案 10/19（momentum 2172・✅即時可）｜提案1回｜当夜 評価外
- 🚨決算直前 11/16(残1営業日) 4346 NEXYZ.Group Corporation｜最後の提案 10/16（reversal 750・✅即時可）｜提案1回｜当夜 評価外
- 📉決算反応日 11/16 2384 ＳＢＳホールディングス｜最後の提案 11/13（oshime 5690・✅即時可）｜提案1回｜当夜 PASS
- 📉決算反応日 11/13 3182 オイシックス｜最後の提案 11/13（momentum 1883・✅即時可）｜提案1回｜当夜 PASS
- 📉決算反応日 11/13 4743 ITFOR Inc.｜最後の提案 11/13（momentum 1628・✅即時可）｜提案6回｜当夜 PASS
- 📉決算反応日 11/16 5101 Yokohama Rubber Co., Ltd.｜最後の提案 11/13（reversal 7321・✅即時可）｜提案4回｜当夜 PASS
- 📉決算反応日 11/16 5252 日本ナレッジ｜最後の提案 11/13（reversal 1000・✅即時可）｜提案4回｜当夜 PASS
- 📉決算反応日 11/13 558A SQUEEZE Inc.｜最後の提案 11/13（momentum 6210・✅即時可）｜提案3回｜当夜 PASS
- 📉決算反応日 11/13 6750 エレコム｜最後の提案 11/13（reversal 1887・✅即時可）｜提案1回｜当夜 PASS
- 📉決算反応日 11/16 2502 Asahi Group Holdings, Ltd.｜最後の提案 11/12（momentum 1750.5・✅即時可）｜提案1回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/16 3989 シェアテク｜最後の提案 11/12（changepoint 1539・✅即時可）｜提案3回｜当夜 PASS
- 📉決算反応日 11/16 7744 ノーリツ鋼機｜最後の提案 11/12（momentum 2073・✅即時可）｜提案5回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 7747 朝日インテック｜最後の提案 11/12（momentum 3875・✅即時可）｜提案4回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 1961 三機工業｜最後の提案 11/11（reversal 2412・✅即時可）｜提案3回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/13 1975 新日本空調｜最後の提案 11/11（momentum 3485・⏸位置不適(25MA下 -6.23%)）｜提案5回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 2962 テクニスコ｜最後の提案 11/11（reversal 1607・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 3374 内外テック｜最後の提案 11/11（reversal 4110・✅即時可）｜提案6回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 3927 アークン｜最後の提案 11/11（momentum 933・⏸位置不適(25MA下 -9.3%／52週 26.3%)）｜提案6回｜当夜 FAIL_INSEN
- 📉決算反応日 11/13 4419 Finatext Holdings Ltd.｜最後の提案 11/11（reversal 1237・✅即時可）｜提案4回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 4634 ａｒｔｉｅｎｃｅ（ａｒｔｉｅｎ）｜最後の提案 11/11（reversal 4875・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 5027 AnyMind Group Inc.｜最後の提案 11/11（momentum 734・⏸位置不適(25MA下 -4.64%)）｜提案6回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 5844 Kyoto Financial Group,Inc.｜最後の提案 11/11（reversal 4241・✅即時可）｜提案5回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 6268 ナブテスコ｜最後の提案 11/11（reversal 4235・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 6317 Kitagawa Corporation｜最後の提案 11/11（reversal 2293・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 6407 CKD｜最後の提案 11/11（reversal 4139・✅即時可）｜提案5回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 6481 THK Co., Ltd.｜最後の提案 11/11（reversal 5579・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- 📉決算反応日 11/13 6524 湖北工業｜最後の提案 11/11（reversal 4825・✅即時可）｜提案4回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/13 6613 QD Laser, Inc.｜最後の提案 11/11（momentum 2222・✅即時可）｜提案4回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 6742 京三製作所｜最後の提案 11/11（reversal 975・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 6840 ＡＫＩＢＡホールディングス｜最後の提案 11/11（reversal 641・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 📉決算反応日 11/13 6862 ミナト HD｜最後の提案 11/11（reversal 3360・✅即時可）｜提案5回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 6877 ＯＢＡＲＡ　ＧＲＯＵＰ（ＯＢＡＲＡＧ）｜最後の提案 11/11（oshime 6762・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 📉決算反応日 11/13 6918 アバールデータ｜最後の提案 11/11（reversal 3270・✅即時可）｜提案5回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 7322 三十三フィナンシャルグループ｜最後の提案 11/11（reversal 1859・✅即時可）｜提案4回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 7384 Procrea Holdings,Inc.｜最後の提案 11/11（reversal 4130・✅即時可）｜提案9回｜当夜 FAIL_INSEN
- 📉決算反応日 11/13 7433 Hakuto Co., Ltd.｜最後の提案 11/11（reversal 1615・✅即時可）｜提案2回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/16 8344 Yamagata Bank, Ltd.｜最後の提案 11/11（reversal 4410・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 📉決算反応日 11/13 8345 Bank of Iwate Ltd.｜最後の提案 11/11（reversal 2128・✅即時可）｜提案8回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 8364 清水銀行｜最後の提案 11/11（reversal 2812・✅即時可）｜提案5回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/16 8366 滋賀銀行｜最後の提案 11/11（reversal 2374・✅即時可）｜提案4回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 8522 Bank of Nagoya, Ltd.｜最後の提案 11/11（reversal 5860・✅即時可）｜提案6回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/13 8551 北日本銀行｜最後の提案 11/11（reversal 2373・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 8600 トモニホールディングス｜最後の提案 11/11（reversal 1029・✅即時可）｜提案6回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 8714 池田泉州ホールディングス｜最後の提案 11/11（reversal 863・✅即時可）｜提案3回｜当夜 評価外
- 📉決算反応日 11/13 1435 robot home Inc.｜最後の提案 11/10（momentum 164・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 📉決算反応日 11/13 150A ＪＳＨ｜最後の提案 11/10（reversal 624・✅即時可）｜提案4回｜当夜 PASS
- 📉決算反応日 11/16 3556 RenetJapanGroup, Inc.｜最後の提案 11/10（momentum 922・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 3851 日本一ソフトウェア｜最後の提案 11/10（reversal 1162・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 3923 ラクス｜最後の提案 11/10（changepoint 1155.5・✅即時可）｜提案3回｜当夜 PASS
- 📉決算反応日 11/16 4011 Headwaters Co.,Ltd｜最後の提案 11/10（changepoint 1927・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 4053 Sun Asterisk, Inc.｜最後の提案 11/10（momentum 579・✅即時可）｜提案4回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/13 4165 PLAID Inc.｜最後の提案 11/10（changepoint 760・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 479A PRONI Inc.｜最後の提案 11/10（reversal 1545・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 5137 Smart Drive Co. Ltd.｜最後の提案 11/10（momentum 313・✅即時可）｜提案5回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 6676 BUFFALO INC.｜最後の提案 11/10（reversal 3180・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 3042 セキュアヴェイル（セキュアヴェ）｜最後の提案 11/09（oshime 891・⏳待機: 到達まで乖離8.7%）｜提案1回｜当夜 PASS_DOJI
- 📉決算反応日 11/16 4058 Toyokumo, Inc.｜最後の提案 11/09（momentum 2189・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 4293 セプテーニ・ホールディングス（セプテニＨＤ）｜最後の提案 11/09（reversal 461・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 📉決算反応日 11/13 6490 ＰＩＬＬＡＲ｜最後の提案 11/09（reversal 8770・✅即時可）｜提案6回｜当夜 FAIL_INSEN
- 📉決算反応日 11/13 7715 長野計器｜最後の提案 11/09（reversal 3190・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 8388 阿波銀行｜最後の提案 11/09（reversal 1760・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 📉決算反応日 11/13 8804 東京建物｜最後の提案 11/09（momentum 3371・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 9552 クオンツ総研ホールディングス｜最後の提案 11/09（oshime 1066・✅即時可）｜提案1回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/13 167A リョーサン菱洋ホールディングス（リョー菱ＨＤ）｜最後の提案 11/06（reversal 2956・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 265A エイチエムコム｜最後の提案 11/06（changepoint 587・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 286A ユカリア｜最後の提案 11/06（changepoint 755・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 📉決算反応日 11/13 598A チャットプラス｜最後の提案 11/06（changepoint 950・✅即時可）｜提案4回｜当夜 FAIL_INSEN
- 📉決算反応日 11/13 6055 Japan Material Co., Ltd.｜最後の提案 11/06（reversal 1623・✅即時可）｜提案5回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 6071 IBJ, Inc.｜最後の提案 11/06（momentum 919・✅即時可）｜提案3回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/16 6227 AIMECHATEC Ltd.｜最後の提案 11/06（reversal 4025・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 6597 HPC SYSTEMS Inc.｜最後の提案 11/06（reversal 2396・✅即時可）｜提案3回｜当夜 評価外
- 📉決算反応日 11/16 7161 Jimoto Holdings, Inc.｜最後の提案 11/06（momentum 500・✅即時可）｜提案3回｜当夜 評価外
- 📉決算反応日 11/16 7318 セレンディップ・ホールディングス｜最後の提案 11/06（changepoint 1031・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 7695 交換できるくん｜最後の提案 11/06（changepoint 830・✅即時可）｜提案5回｜当夜 FAIL_INSEN
- 📉決算反応日 11/13 3591 WACOAL HOLDINGS CORP｜最後の提案 11/05（reversal 3919・✅即時可）｜提案4回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/16 8253 Credit Saison Co., Ltd.｜最後の提案 11/05（reversal 4233・✅即時可）｜提案3回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/13 7734 Riken Keiki Co., Ltd.｜最後の提案 11/02（momentum 3480・✅即時可）｜提案3回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/13 1719 HAZAMA ANDO Corporation｜最後の提案 10/29（reversal 1759.5・✅即時可）｜提案5回｜当夜 評価外
- 📉決算反応日 11/16 1860 Toda Corporation｜最後の提案 10/29（reversal 1465.5・✅即時可）｜提案7回｜当夜 評価外
- 📉決算反応日 11/13 1952 Shin Nippon Air Technologies Co., Ltd.｜最後の提案 10/29（reversal 3065・✅即時可）｜提案5回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/13 3040 ソリトンシステムズ｜最後の提案 10/29（oshime 3051.2・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 📉決算反応日 11/13 3496 アズーム｜最後の提案 10/29（momentum 4810・✅即時可）｜提案3回｜当夜 PASS_DOJI
- 📉決算反応日 11/16 4180 ＡＰＰＩＥＲ　ＧＲＯＵＰ｜最後の提案 10/29（oshime 1412.2・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- 📉決算反応日 11/13 5537 AlbaLink Co.,Ltd.｜最後の提案 10/29（momentum 3405・✅即時可）｜提案4回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 5757 CK San-Etsu Co., Ltd.｜最後の提案 10/29（momentum 4505・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 593A ティアフォー｜最後の提案 10/29（changepoint 2364・✅即時可）｜提案4回｜当夜 PASS
- 📉決算反応日 11/16 6736 Suncorporation｜最後の提案 10/29（oshime 9748.9・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 8360 Yamanashi Chuo Bank, Ltd.｜最後の提案 10/29（reversal 1321・✅即時可）｜提案5回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 9553 MicroAd, Inc.｜最後の提案 10/29（momentum 593・✅即時可）｜提案6回｜当夜 評価外
- 📉決算反応日 11/16 3691 DIGITAL PLUS, Inc.｜最後の提案 10/28（reversal 1487・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- 📉決算反応日 11/13 4377 ONE CAREER Inc.｜最後の提案 10/28（momentum 2509・✅即時可）｜提案1回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/13 1861 Kumagai Gumi Co., Ltd.｜最後の提案 10/27（reversal 1246・✅即時可）｜提案5回｜当夜 評価外
- 📉決算反応日 11/13 5254 Arent, Inc.｜最後の提案 10/27（momentum 3880・✅即時可）｜提案4回｜当夜 FAIL_INSEN
- 📉決算反応日 11/13 5590 NETSTARS Co.,Ltd.｜最後の提案 10/27（changepoint 656・✅即時可）｜提案3回｜当夜 評価外
- 📉決算反応日 11/16 584A LiNKX, Inc.｜最後の提案 10/27（changepoint 2308・✅即時可）｜提案4回｜当夜 評価外
- 📉決算反応日 11/16 8524 North Pacific Bank, Ltd.｜最後の提案 10/27（reversal 1176・✅即時可）｜提案4回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 8713 Fidea Holdings Co.Ltd.｜最後の提案 10/27（reversal 2527・✅即時可）｜提案5回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 6203 Howa Machinery, Ltd.｜最後の提案 10/26（reversal 2279・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 6298 Y.A.C.HOLDINGS CO.,LTD.｜最後の提案 10/26（momentum 1099・✅即時可）｜提案3回｜当夜 評価外
- 📉決算反応日 11/13 7567 Sakae Electronics Corp.｜最後の提案 10/26（momentum 635・✅即時可）｜提案3回｜当夜 評価外
- 📉決算反応日 11/16 8944 Land Business Co., Ltd.｜最後の提案 10/26（momentum 256・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 9211 f-code Inc.｜最後の提案 10/26（momentum 1204・✅即時可）｜提案2回｜当夜 評価外
- 📉決算反応日 11/13 3993 PKSHA Technology, Inc.｜最後の提案 10/23（changepoint 3700・✅即時可）｜提案2回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/16 477A Startline CO.,LTD.｜最後の提案 10/23（reversal 750・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 8995 Makoto Construction Co,Ltd｜最後の提案 10/23（reversal 1484・✅即時可）｜提案1回｜当夜 評価外
- 📉決算反応日 11/13 1662 Japan Petroleum Exploration Co., Ltd.｜最後の提案 10/22（reversal 1715・✅即時可）｜提案3回｜当夜 評価外
- 📉決算反応日 11/16 4493 Cyber Security Cloud, Inc.｜最後の提案 10/22（changepoint 3865・✅即時可）｜提案2回｜当夜 評価外
- 📉決算反応日 11/13 5034 unerry, Inc.｜最後の提案 10/22（momentum 2841・✅即時可）｜提案2回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/16 5038 eWeLL Co.,Ltd｜最後の提案 10/21（momentum 2331・✅即時可）｜提案1回｜当夜 評価外
- 📉決算反応日 11/16 3097 Monogatari Corporation｜最後の提案 10/20（oshime 5520・⏳待機: 到達まで乖離-9.4%）｜提案2回｜当夜 評価外
- 📉決算反応日 11/16 5242 EYEZ INC.｜最後の提案 10/20（reversal 2866・✅即時可）｜提案3回｜当夜 評価外
- 📉決算反応日 11/16 1815 鉄建建設｜最後の提案 10/19（momentum 2191・✅即時可）｜提案2回｜当夜 評価外
- 📉決算反応日 11/16 4691 Washington Hotel Corp.｜最後の提案 10/19（reversal 1913・✅即時可）｜提案1回｜当夜 評価外
- 📉決算反応日 11/16 6254 野村マイクロ・サイエンス｜最後の提案 10/19（changepoint 3160・✅即時可）｜提案2回｜当夜 評価外
- 📉決算反応日 11/16 6379 RAIZNEXT Corporation｜最後の提案 10/19（oshime 1000・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 6804 Hosiden Corp.｜最後の提案 10/19（reversal 2380・✅即時可）｜提案2回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/13 8066 Mitani Corporation｜最後の提案 10/19（reversal 3140・✅即時可）｜提案1回｜当夜 評価外
- 📉決算反応日 11/13 8511 Japan Securities Finance Co., Ltd.｜最後の提案 10/19（reversal 2217・✅即時可）｜提案1回｜当夜 評価外
- 📉決算反応日 11/16 9554 AViC Co. Ltd.｜最後の提案 10/19（momentum 1721・✅即時可）｜提案2回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/13 3696 セレス｜最後の提案 10/16（momentum 2397・✅即時可）｜提案1回｜当夜 FAIL_UWAHIGE
- 📉決算反応日 11/13 4044 Central Glass Co., Ltd.｜最後の提案 10/16（oshime 4510・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 4166 Cacco, Inc.｜最後の提案 10/16（momentum 733・✅即時可）｜提案1回｜当夜 PASS
- 📉決算反応日 11/13 4488 AI inside Inc.｜最後の提案 10/16（changepoint 2116・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 📉決算反応日 11/13 5036 Japan Business Systems, Inc.｜最後の提案 10/16（momentum 1898・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 5892 yutori,Inc.｜最後の提案 10/16（momentum 3180・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 📉決算反応日 11/16 6562 Geniee, Inc.｜最後の提案 10/16（momentum 1005・✅即時可）｜提案1回｜当夜 評価外
- ⏰決算 11/19(残4営業日) 8986 Daiwa Securities Living Investment Corporation｜最後の提案 10/26（reversal 83900・✅即時可）｜提案1回｜当夜 評価外
- 📋カルテ窓 12/11(残19営業日) 446A ノースサンド｜最後の提案 11/13（momentum 2663・⏸位置不適(25MA下 -2.43%)）｜提案4回｜当夜 PASS
- 📋カルテ窓 12/09(残17営業日) 7678 ASAKUMA CO.,LTD.｜最後の提案 11/13（momentum 4450・✅即時可）｜提案6回｜当夜 PASS
- 📋カルテ窓 12/11(残19営業日) 218A Liberaware｜最後の提案 11/11（changepoint 830・✅即時可）｜提案6回｜当夜 FAIL_UWAHIGE
- 📋カルテ窓 12/10(残18営業日) 3491 ＧＡ　ｔｅｃｈｎｏｌｏｇｉｅｓ（ＧＡテクノ）｜最後の提案 11/11（momentum 1568・✅即時可）｜提案2回｜当夜 FAIL_UWAHIGE
- 📋カルテ窓 12/14(残20営業日) 460A ＢＲＡＮＵ｜最後の提案 11/11（reversal 1098・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 📋カルテ窓 12/11(残19営業日) 6336 石井表記｜最後の提案 11/11（reversal 1266・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- 📋カルテ窓 12/08(残16営業日) 9824 泉州電業｜最後の提案 11/11（momentum 7880・⏸位置不適(25MA下 -2.36%)）｜提案6回｜当夜 FAIL_INSEN
- 📋カルテ窓 12/08(残16営業日) 1436 GreenEnergy & Company｜最後の提案 11/10（reversal 1368・✅即時可）｜提案3回｜当夜 FAIL_UWAHIGE
- 📋カルテ窓 12/04(残14営業日) 436A サイバーソリューションズ（サイバＳＯＬ）｜最後の提案 11/10（oshime 1776・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 📋カルテ窓 12/10(残18営業日) 1928 積水ハウス｜最後の提案 11/09（momentum 3568・✅即時可）｜提案2回｜当夜 PASS
- 📋カルテ窓 12/11(残19営業日) 4075 ブレインズテクノロジー｜最後の提案 11/09（reversal 1037・✅即時可）｜提案2回｜当夜 FAIL_INSEN
- 📋カルテ窓 12/09(残17営業日) 5132 pluszero,Inc.｜最後の提案 11/04（momentum 1761・✅即時可）｜提案3回｜当夜 FAIL_INSEN
- 📋カルテ窓 12/11(残19営業日) 3653 Morpho, Inc.｜最後の提案 10/29（reversal 918・✅即時可）｜提案4回｜当夜 評価外
- 📋カルテ窓 12/10(残18営業日) 8927 Meiho Enterprise Co., Ltd.｜最後の提案 10/29（momentum 466・✅即時可）｜提案1回｜当夜 評価外
- 📋カルテ窓 12/11(残19営業日) 186A Astroscale Holdings Inc.｜最後の提案 10/27（momentum 1084・✅即時可）｜提案4回｜当夜 評価外
- 📋カルテ窓 12/11(残19営業日) 456A Human Made Inc.｜最後の提案 10/27（oshime 1940・✅即時可）｜提案3回｜当夜 FAIL_UWAHIGE
- 📋カルテ窓 12/11(残19営業日) 4382 HEROZ, Inc.｜最後の提案 10/21（changepoint 1631・✅即時可）｜提案2回｜当夜 評価外
- 📋カルテ窓 12/14(残20営業日) 9166 GENDA Inc.｜最後の提案 10/21（oshime 673.5・✅即時可）｜提案1回｜当夜 FAIL_INSEN
- 📋カルテ窓 12/07(残15営業日) 7856 HAGIHARA INDUSTRIES INC.｜最後の提案 10/19（oshime 2044・✅即時可）｜提案2回｜当夜 評価外
- 📋カルテ窓 12/11(残19営業日) 9556 INTLOOP, Inc.｜最後の提案 10/16（momentum 2267・✅即時可）｜提案1回｜当夜 評価外
-  2206 江崎グリコ｜最後の提案 11/13（momentum 5122・⏸位置不適(52週 26.9%)）｜提案3回｜当夜 PASS
-  2897 Nissin Foods Holdings Co., Ltd.｜最後の提案 11/13（momentum 2974.5・⏸位置不適(25MA下 -1.59%)）｜提案4回｜当夜 PASS
-  3405 クラレ｜最後の提案 11/13（momentum 1917.5・✅即時可）｜提案4回｜当夜 PASS
-  7606 ＴＡＢＡＹＡホールディングス｜最後の提案 11/13（momentum 2668・✅即時可）｜提案4回｜当夜 PASS
-  8113 Unicharm Corporation｜最後の提案 11/13（momentum 1120.5・✅即時可）｜提案5回｜当夜 PASS
-  8801 三井不動産｜最後の提案 11/13（momentum 1631・⏸位置不適(52週 29.4%)）｜提案3回｜当夜 PASS
-  8975 Ichigo Office REIT Investment Corporation｜最後の提案 11/13（reversal 87500・✅即時可）｜提案5回｜当夜 PASS
-  9006 Keikyu Corporation｜最後の提案 11/13（momentum 1630.5・✅即時可）｜提案2回｜当夜 PASS
-  9045 Keihan Holdings Co., Ltd.｜最後の提案 11/13（momentum 3409・✅即時可）｜提案2回｜当夜 PASS
-  9401 東京放送ホールディングス｜最後の提案 11/13（momentum 6313・✅即時可）｜提案1回｜当夜 PASS
-  9735 セコム｜最後の提案 11/13（momentum 7121・✅即時可）｜提案1回｜当夜 PASS
-  9956 Valor Holdings Co., Ltd.｜最後の提案 11/13（momentum 1636.5・⏸位置不適(25MA下 -0.95%／52週 29.0%)）｜提案2回｜当夜 PASS
-  1926 ライト工業（ライト）｜最後の提案 11/12（reversal 1016・✅即時可）｜提案1回｜当夜 FAIL_UWAHIGE
-  3565 Ascentech KK｜最後の提案 11/12（reversal 453・✅即時可）｜提案1回｜当夜 FAIL_UWAHIGE
-  3798 ULS Group Incorporated｜最後の提案 11/12（momentum 493・⏸位置不適(25MA下 -7.55%／52週 8.4%)）｜提案5回｜当夜 PASS_DOJI
-  4008 住友精化｜最後の提案 11/12（reversal 1377・✅即時可）｜提案1回｜当夜 FAIL_INSEN
-  4396 System Support Holdings Inc.｜最後の提案 11/12（reversal 1315・✅即時可）｜提案1回｜当夜 FAIL_UWAHIGE
-  9075 福山通運｜最後の提案 11/12（momentum 6440・✅即時可）｜提案1回｜当夜 FAIL_INSEN
-  1982 日比谷総合設備｜最後の提案 11/11（momentum 3195・⏸位置不適(25MA下 -1.2%)）｜提案4回｜当夜 FAIL_INSEN
-  4028 石原産業｜最後の提案 11/11（reversal 2616・✅即時可）｜提案1回｜当夜 FAIL_UWAHIGE
-  4403 日油｜最後の提案 11/11（momentum 2570・⏳確認足待ち）｜提案1回｜当夜 FAIL_INSEN
-  4968 Arakawa Chemical Industries,Ltd.｜最後の提案 11/11（reversal 1969・✅即時可）｜提案2回｜当夜 FAIL_INSEN
-  6138 ダイジェット工業（ダイジェト）｜最後の提案 11/11（reversal 1760・✅即時可）｜提案1回｜当夜 FAIL_INSEN
-  7826 フルヤ金属｜最後の提案 11/11（reversal 9050・✅即時可）｜提案1回｜当夜 FAIL_INSEN
-  147A SORACOM,INC.｜最後の提案 11/10（momentum 939・✅即時可）｜提案1回｜当夜 FAIL_UWAHIGE
-  4071 Plus Alpha Consulting Co. LTD.｜最後の提案 11/10（changepoint 2318・✅即時可）｜提案3回｜当夜 FAIL_UWAHIGE
-  4966 上村工業｜最後の提案 11/10（reversal 17270・✅即時可）｜提案4回｜当夜 FAIL_INSEN
-  5019 出光興産｜最後の提案 11/10（reversal 1290・✅即時可）｜提案1回｜当夜 FAIL_INSEN
-  5136 tripla Co.,Ltd.｜最後の提案 11/10（momentum 2741・✅即時可）｜提案5回｜当夜 FAIL_UWAHIGE
-  6027 Bengo4.com, Inc.｜最後の提案 11/10（oshime 4890・✅即時可）｜提案2回｜当夜 FAIL_INSEN
-  6284 日精エー・エス・ビー機械｜最後の提案 11/10（reversal 7850・✅即時可）｜提案6回｜当夜 FAIL_INSEN
-  6570 Kyowa Corporation Co. Ltd.｜最後の提案 11/10（oshime 4290・✅即時可）｜提案1回｜当夜 FAIL_INSEN
-  1963 日揮ホールディングス｜最後の提案 11/09（reversal 2051.5・✅即時可）｜提案5回｜当夜 FAIL_INSEN
-  4980 Dexerials Corp.｜最後の提案 11/09（reversal 2385.5・✅即時可）｜提案3回｜当夜 FAIL_INSEN
-  7186 横浜フィナンシャルグループ｜最後の提案 11/09（reversal 1662.5・✅即時可）｜提案6回｜当夜 FAIL_INSEN
-  8151 東陽テクニカ｜最後の提案 11/09（changepoint 1668・✅即時可）｜提案3回｜当夜 FAIL_INSEN
-  255A GLテクノHD｜最後の提案 11/06（reversal 3940・✅即時可）｜提案1回｜当夜 FAIL_INSEN
-  3436 SUMCO｜最後の提案 11/06（reversal 1784.5・✅即時可）｜提案1回｜当夜 FAIL_INSEN
-  4022 ラサ工業｜最後の提案 11/06（reversal 1182・✅即時可）｜提案1回｜当夜 FAIL_INSEN
-  421A Movin' Strategic Career CO.,LTD.｜最後の提案 11/06（momentum 3335・✅即時可）｜提案4回｜当夜 評価外
-  4401 ＡＤＥＫＡ｜最後の提案 11/06（momentum 4068・✅即時可）｜提案2回｜当夜 FAIL_INSEN
-  4971 メック｜最後の提案 11/06（reversal 4925・✅即時可）｜提案3回｜当夜 FAIL_INSEN
-  6278 ユニオンツール｜最後の提案 11/06（reversal 9750・✅即時可）｜提案3回｜当夜 FAIL_INSEN
-  7167 めぶきフィナンシャルグループ｜最後の提案 11/06（reversal 1375・✅即時可）｜提案1回｜当夜 FAIL_INSEN
-  5711 三菱マテリアル｜最後の提案 11/04（reversal 4193・✅即時可）｜提案1回｜当夜 FAIL_INSEN
-  5838 Rakuten Bank, Ltd.｜最後の提案 11/04（momentum 6028・✅即時可）｜提案5回｜当夜 評価外
-  9163 Nareru Group Inc.｜最後の提案 11/04（momentum 2088・✅即時可）｜提案2回｜当夜 FAIL_INSEN
-  4100 Toda Kogyo Corp.｜最後の提案 11/02（reversal 1757・✅即時可）｜提案2回｜当夜 FAIL_INSEN
-  4478 freee K.K.｜最後の提案 11/02（changepoint 4645・✅即時可）｜提案4回｜当夜 FAIL_INSEN
-  7806 MTG Co., Ltd.｜最後の提案 11/02（oshime 8756・✅即時可）｜提案3回｜当夜 FAIL_INSEN
-  8304 あおぞら銀行｜最後の提案 11/02（reversal 2981・✅即時可）｜提案4回｜当夜 FAIL_INSEN
-  4933 I-ne CO., LTD.｜最後の提案 10/29（momentum 2479・✅即時可）｜提案1回｜当夜 FAIL_INSEN
-  5184 ニチリン｜最後の提案 10/29（momentum 4185・✅即時可）｜提案1回｜当夜 FAIL_INSEN
-  6324 Harmonic Drive Systems Inc.｜最後の提案 10/29（reversal 5480・✅即時可）｜提案4回｜当夜 FAIL_INSEN
-  7199 プレミアグループ｜最後の提案 10/29（momentum 2263・✅即時可）｜提案3回｜当夜 評価外
-  8346 東邦銀行｜最後の提案 10/29（reversal 986・✅即時可）｜提案3回｜当夜 評価外
-  8399 琉球銀行｜最後の提案 10/29（reversal 2868・✅即時可）｜提案5回｜当夜 FAIL_INSEN
-  9064 ヤマトホールディングス｜最後の提案 10/29（momentum 1965・✅即時可）｜提案2回｜当夜 評価外
-  4431 スマレジ｜最後の提案 10/28（oshime 3707.6・✅即時可）｜提案3回｜当夜 評価外
-  1893 Penta-Ocean Construction Co., Ltd.｜最後の提案 10/27（reversal 1382・✅即時可）｜提案5回｜当夜 評価外
-  212A FIT EASY Inc.｜最後の提案 10/27（momentum 2771・✅即時可）｜提案2回｜当夜 評価外
-  268A Rigaku Holdings Corporation｜最後の提案 10/27（reversal 1485・✅即時可）｜提案2回｜当夜 FAIL_UWAHIGE
-  4658 日本空調サービス｜最後の提案 10/27（reversal 1545・✅即時可）｜提案3回｜当夜 評価外
-  5021 Cosmo Energy Holdings Co., Ltd.｜最後の提案 10/27（reversal 4370・✅即時可）｜提案3回｜当夜 FAIL_INSEN
-  8088 岩谷産業｜最後の提案 10/27（reversal 1928・✅即時可）｜提案3回｜当夜 評価外
-  9699 NISHIO HOLDINGS CO. LTD.｜最後の提案 10/27（reversal 4305・✅即時可）｜提案2回｜当夜 評価外
-  1833 Okumura Corporation｜最後の提案 10/26（reversal 5350・✅即時可）｜提案1回｜当夜 評価外
-  4666 Park24 Co., Ltd.｜最後の提案 10/26（reversal 1850・✅即時可）｜提案2回｜当夜 評価外
-  6269 Modec, Inc.｜最後の提案 10/26（reversal 8130・✅即時可）｜提案5回｜当夜 評価外
-  1803 Shimizu Corporation｜最後の提案 10/23（reversal 2029・✅即時可）｜提案3回｜当夜 評価外
-  2820 Yamami Co.｜最後の提案 10/23（momentum 6580・✅即時可）｜提案2回｜当夜 評価外
-  3289 Tokyu Fudosan Holdings Corp.｜最後の提案 10/23（reversal 1235・✅即時可）｜提案1回｜当夜 評価外
-  4259 ExaWizards Inc.｜最後の提案 10/23（changepoint 753・✅即時可）｜提案3回｜当夜 FAIL_INSEN
-  6643 戸上電機製作所｜最後の提案 10/23（reversal 5070・✅即時可）｜提案4回｜当夜 評価外
-  4928 Noevir Holdings Co., Ltd.｜最後の提案 10/22（reversal 4695・✅即時可）｜提案1回｜当夜 評価外
-  2815 ARIAKE JAPAN Co., Ltd.｜最後の提案 10/20（reversal 5270・✅即時可）｜提案1回｜当夜 評価外
-  4544 H.U.Group Holdings, Inc.｜最後の提案 10/20（momentum 3720・✅即時可）｜提案2回｜当夜 評価外
-  9432 NTT｜最後の提案 10/20（reversal 177.1・✅即時可）｜提案1回｜当夜 PASS
-  6492 Okano Valve Mfg. Co., Ltd.｜最後の提案 10/19（momentum 13760・✅即時可）｜提案2回｜当夜 評価外
-  2980 SRE Holdings Corp.｜最後の提案 10/16（momentum 2398・✅即時可）｜提案1回｜当夜 評価外
-  4183 Mitsui Chemicals, Inc.｜最後の提案 10/16（momentum 2108・✅即時可）｜提案1回｜当夜 評価外
-  4331 Take and Give. Needs Co., Ltd.｜最後の提案 10/16（momentum 834・✅即時可）｜提案1回｜当夜 評価外
-  5461 Chubu Steel Plate Co., Ltd.｜最後の提案 10/16（momentum 2153・✅即時可）｜提案1回｜当夜 評価外
-  6208 Ishikawa Seisakusho,Ltd.｜最後の提案 10/16（momentum 1674・✅即時可）｜提案1回｜当夜 評価外
-  8020 Kanematsu Corporation｜最後の提案 10/16（momentum 2403・✅即時可）｜提案1回｜当夜 評価外
-  8043 Starzen Company Limited｜最後の提案 10/16（oshime 1524・✅即時可）｜提案1回｜当夜 評価外
-  8059 Daiichi Jitsugyo Co., Ltd.｜最後の提案 10/16（oshime 3595・✅即時可）｜提案1回｜当夜 評価外
-  8282 K'S HOLDINGS CORPORATION｜最後の提案 10/16（reversal 1743・✅即時可）｜提案1回｜当夜 評価外

## 📅今週のカタリスト
### (a) 今週のカタリスト日程（候補＋重要日程）
- 11/16(月) 5105 ＴＯＹＯ　ＴＩＲＥ — 決算発表予定（候補・PASS）
- 11/16(月) 5582 （名称取得不可） — 決算発表予定（候補・PASS）
- 11/16(月) 6036 ＫｅｅＰｅｒ技研 — 決算発表予定（候補・PASS）
- 11/16(月) 664A — TOKIUM(664A) 公開価格決定予定
- 11/20(金) 657A — HiJoJo Partners(657A) 東証グロース上場予定
### (b) 今週の市場イベント（日付計算）
- 11/20(金): 連休前最終営業日（次の営業日 11/24(火)）
- 市場イベント（WebSearch補足）: 取得不可（検索結果が前年分のみで2026年の日程を確認できず。推定で埋めない）
### (c) 週末の材料
- 週末材料: 該当なし（実行時点で週末前）
### (d) theme_watch / changepoint_watch のシグナル点灯
- 🔔 4478 freee K.K.（theme:saas_naiseika）
- 🔔 4493 Cyber Security Cloud, Inc.（theme:saas_naiseika）
- 🔔 4165 PLAID Inc.（theme:saas_naiseika）
- 🔔 4443 Sansan, Inc.（theme:saas_naiseika）
- 🔔🔔 3993 PKSHA Technology, Inc.（theme:saas_naiseika）
- 🔔 4483 JMDC Inc.（theme:saas_naiseika）
- 🔔🔔 4071 Plus Alpha Consulting Co. LTD.（theme:saas_naiseika）
- 🔔 4180 Appier Group, Inc.（theme:saas_naiseika）
- 🔔 3923 RAKUS Co., Ltd.（theme:saas_naiseika）
- 🔔 6284 日精エー・エス・ビー機械（変化点・2026-11-12）
- 🔔🔔 4071 プラスアルファ・コンサルティング（変化点・2026-11-12）
- 🔔 8697 日本取引所グループ（変化点・2026-11-12）
- 🔔🔔 3994 マネーフォワード（変化点・2026-11-12）
- 🔔 593A ティアフォー（変化点・2026-11-12）
- 🔔 4667 アイサンテクノロジー（変化点・2026-11-12）
- 🔔 4478 フリー（変化点・2026-11-12）
- 🔔🔔 4259 エクサウィザーズ（変化点・2026-11-12）
- カタリストは日程であって売買理由ではない。跨ぐか手仕舞うかは事前に決める（教訓⑲）

## 前夜の結果
PL5口座への正式な反映は週次①-11の採点で行われる。ここは参考情報
前夜2026-11-12の提案57件 → 約定48・不約定9・判定不能0
- 3798 momentum 注文493｜2026-11-13 O489 H503 L485 C490｜約定 493・終値比-0.61%
- 446A momentum 注文2404｜2026-11-13 O2359 H2662 L2359 C2604｜約定 2404・終値比+8.32%
- 7733 reversal 注文1790.5｜2026-11-13 O1784 H1795 L1754 C1776｜約定 1784・終値比-0.45%
- 8133 reversal 注文2055｜2026-11-13 O2060 H2077 L2041 C2068｜約定 2055・終値比+0.63%
- 3116 reversal 注文2070｜2026-11-13 O2059.5 H2087.5 L2041 C2086.5｜約定 2059.5・終値比+1.31%
- 8098 reversal 注文4355｜2026-11-13 O4375 H4415 L4340 C4370｜約定 4355・終値比+0.34%
- 1721 reversal 注文5240｜2026-11-13 O5234 H5334 L5233 C5264｜約定 5234・終値比+0.57%
- 1926 reversal 注文1016｜2026-11-13 O1039 H1054 L1024 C1040｜不約定
- 9302 reversal 注文3201｜2026-11-13 O3207 H3217 L3198 C3215｜約定 3201・終値比+0.44%
- 1417 reversal 注文3400｜2026-11-13 O3435 H3478 L3411 C3434｜不約定
- 5602 reversal 注文1456｜2026-11-13 O1457 H1460 L1446 C1457｜約定 1456・終値比+0.07%
- 6741 reversal 注文1667｜2026-11-13 O1659 H1659 L1635 C1652｜約定 1659・終値比-0.42%
- 1979 reversal 注文3395｜2026-11-13 O3395 H3530 L3380 C3530｜約定 3395・終値比+3.98%
- 4008 reversal 注文1377｜2026-11-13 O1384 H1384 L1353 C1359｜約定 1377・終値比-1.31%
- 6632 reversal 注文826｜2026-11-13 O827 H834 L813 C820｜約定 826・終値比-0.73%
- 6370 reversal 注文5578｜2026-11-13 O5651 H5816 L5592 C5724｜不約定
- 6436 reversal 注文3489｜2026-11-13 O3489 H3565 L3466 C3565｜約定 3489・終値比+2.18%
- 2109 reversal 注文3600｜2026-11-13 O3580 H3630 L3570 C3625｜約定 3580・終値比+1.26%
- 3612 reversal 注文1498｜2026-11-13 O1499 H1503 L1485 C1493｜約定 1498・終値比-0.33%
- 8975 reversal 注文86700｜2026-11-13 O86700 H87500 L85900 C87500｜約定 86700・終値比+0.92%
- 8698 reversal 注文600｜2026-11-13 O596 H600 L592 C597｜約定 596・終値比+0.17%
- 3131 reversal 注文7310｜2026-11-13 O6930 H7530 L6900 C7100｜約定 6930・終値比+2.45%
- 2502 momentum 注文1750.5｜2026-11-13 O1750 H1820 L1736 C1805｜約定 1750.5・終値比+3.11%
- 4523 momentum 注文5180｜2026-11-13 O5152 H5216 L5093 C5186｜約定 5180・終値比+0.12%
- 8697 momentum 注文2205｜2026-11-13 O2228 H2237 L2198.5 C2216.5｜不約定
- 9006 momentum 注文1590｜2026-11-13 O1579.5 H1630 L1579.5 C1630｜約定 1590・終値比+2.52%
- 7744 momentum 注文2073｜2026-11-13 O2067 H2067 L2028 C2047｜不約定
- 9075 momentum 注文6440｜2026-11-13 O6390 H6490 L6340 C6380｜約定 6440・終値比-0.93%
- 4507 momentum 注文3147｜2026-11-13 O3117 H3188 L3101 C3172｜約定 3147・終値比+0.79%
- 1941 momentum 注文5170｜2026-11-13 O5190 H5230 L5150 C5220｜約定 5190・終値比+0.58%
- 4848 momentum 注文1836｜2026-11-13 O1835 H1857 L1814 C1851｜約定 1836・終値比+0.82%
- 4554 momentum 注文1888｜2026-11-13 O1877 H1881 L1840 C1857｜不約定
- 9842 momentum 注文1918｜2026-11-13 O1917 H1935 L1908 C1935｜約定 1918・終値比+0.89%
- 8016 momentum 注文788｜2026-11-13 O790 H795 L783 C794｜約定 790・終値比+0.51%
- 7747 momentum 注文3875｜2026-11-13 O3884 H3888 L3811 C3811｜約定 3884・終値比-1.88%
- 4568 momentum 注文2865｜2026-11-13 O2827.5 H2867 L2820 C2852.5｜約定 2865・終値比-0.44%
- 417A momentum 注文1919｜2026-11-13 O1912 H1949.5 L1901 C1948.5｜約定 1919・終値比+1.54%
- 2488 momentum 注文1392｜2026-11-13 O1395 H1407 L1378 C1394｜約定 1395・終値比-0.07%
- 7269 momentum 注文2203.5｜2026-11-13 O2194 H2200 L2151 C2168.5｜不約定
- 6592 momentum 注文1805｜2026-11-13 O1815 H1832 L1802.5 C1827.5｜約定 1815・終値比+0.69%
- 8160 momentum 注文2511｜2026-11-13 O2510 H2545 L2500 C2542｜約定 2511・終値比+1.23%
- 8056 momentum 注文4846｜2026-11-13 O4807 H4880 L4788 C4880｜約定 4846・終値比+0.70%
- 9956 momentum 注文1620｜2026-11-13 O1615 H1636 L1596 C1627｜約定 1620・終値比+0.43%
- 4540 momentum 注文3919｜2026-11-13 O3927 H3950 L3888 C3944｜約定 3927・終値比+0.43%
- 9045 momentum 注文3351｜2026-11-13 O3335 H3408 L3317 C3408｜約定 3351・終値比+1.70%
- 8801 momentum 注文1596.5｜2026-11-13 O1593.5 H1630.5 L1574.5 C1623｜約定 1596.5・終値比+1.66%
- 5233 momentum 注文4033｜2026-11-13 O4010 H4097 L3996 C4083｜約定 4033・終値比+1.24%
- 8803 momentum 注文2353｜2026-11-13 O2352 H2365 L2327 C2365｜約定 2353・終値比+0.51%
- 4922 momentum 注文5909｜2026-11-13 O5856 H6016 L5816 C5989｜約定 5909・終値比+1.35%
- 4912 momentum 注文2191.5｜2026-11-13 O2175 H2194 L2145 C2186｜約定 2191.5・終値比-0.25%
- 1878 momentum 注文3373｜2026-11-13 O3341 H3341 L3286 C3310｜不約定
- 2811 momentum 注文2814｜2026-11-13 O2814 H2845 L2790 C2839｜約定 2814・終値比+0.89%
- 4396 reversal 注文1315｜2026-11-13 O1327 H1355 L1312 C1336｜約定 1315・終値比+1.60%
- 3565 reversal 注文453｜2026-11-13 O450 H461 L447 C456｜約定 450・終値比+1.33%
- 4768 reversal 注文3691｜2026-11-13 O3708 H3756 L3694 C3746｜不約定
- 8609 reversal 注文1060｜2026-11-13 O1065 H1073 L1043 C1064｜約定 1060・終値比+0.38%
- 3989 changepoint 注文1539｜2026-11-13 O1539 H1549 L1538 C1549｜約定 1539・終値比+0.65%

## 模擬テンプレ
```
# base_day 2026-11-13 ／ 提案50件
# 使い方: 参戦する0〜3銘柄の行だけをコピーし、｜の後ろに参戦理由を書いてポジション株PJへ送る。
# 選ばなかった行は送らなくてよい（全行に理由を書く必要はない）。見送りは末尾の1行で足りる。
# 特定銘柄を理由つきで見送る場合のみ『模擬 見送り {code} ｜{理由}』を送る。
模擬 4434 kenmo_momentum 逆指値3100 SL2909.3 単元100 ｜
模擬 558A kenmo_momentum 逆指値6210 SL5828 単元100 ｜
模擬 7678 kenmo_momentum 逆指値4450 SL4178.3 単元100 ｜
模擬 4743 kenmo_momentum 逆指値1628 SL1529.4 単元100 ｜
模擬 446A kenmo_newhigh 逆指値2663 SL2502.3 単元100 ｜
模擬 8133 choruko_reversal 指値2068 SL1977 単元100 ｜
模擬 3116 choruko_reversal 指値2086.5 SL2022.5 単元100 ｜
模擬 5101 choruko_reversal 指値7321 SL6818 単元100 ｜
模擬 9302 choruko_reversal 指値3215 SL3177 単元100 ｜
模擬 9960 choruko_reversal 指値4515 SL3820 単元100 ｜
模擬 6750 choruko_reversal 指値1887 SL1799 単元100 ｜
模擬 1979 choruko_reversal 指値3530 SL3245 単元100 ｜
模擬 7148 choruko_reversal 指値1424 SL1380 単元100 ｜
模擬 2109 choruko_reversal 指値3625 SL3515 単元100 ｜
模擬 6349 choruko_reversal 指値1741 SL1673 単元100 ｜
模擬 8975 choruko_reversal 指値87500 SL85700 単元1 ｜
模擬 4768 choruko_reversal 指値3746 SL3603 単元100 ｜
模擬 9048 value_gap 逆指値2030.5 SL1908.2 単元100 ｜
模擬 6988 ai_momentum 逆指値3567 SL3352 単元100 ｜
模擬 6367 ai_momentum 逆指値23485 SL22071.2 単元100 ｜
模擬 9503 ai_reversal 指値2729.5 SL2583.5 単元100 ｜
模擬 3405 granville_tenkan 逆指値1917.5 SL1802 単元100 ｜
模擬 9006 granville_tenkan 逆指値1630.5 SL1532.2 単元100 ｜
模擬 1941 granville_tenkan 逆指値5240 SL4916.2 単元100 ｜
模擬 4848 granville_tenkan 逆指値1858 SL1745.6 単元100 ｜
模擬 8016 granville_tenkan 逆指値796 SL747.3 単元100 ｜
模擬 2206 granville_tenkan 逆指値5122 SL4813.7 単元100 ｜
模擬 7606 granville_tenkan 逆指値2668 SL2507 単元100 ｜
模擬 6412 granville_tenkan 逆指値2105 SL1977.8 単元100 ｜
模擬 1911 granville_tenkan 逆指値1278.5 SL1201.3 単元100 ｜
模擬 417A granville_tenkan 逆指値1950 SL1832.5 単元100 ｜
模擬 9418 granville_tenkan 逆指値1883 SL1769.1 単元100 ｜
模擬 3092 granville_tenkan 逆指値1177.5 SL1106.4 単元100 ｜
模擬 8113 granville_tenkan 逆指値1120.5 SL1052.8 単元100 ｜
模擬 8160 granville_tenkan 逆指値2546 SL2392.3 単元100 ｜
模擬 8056 granville_tenkan 逆指値4881 SL4587.2 単元100 ｜
模擬 9956 granville_tenkan 逆指値1636.5 SL1537.8 単元100 ｜
模擬 4540 granville_tenkan 逆指値3951 SL3713 単元100 ｜
模擬 9045 granville_tenkan 逆指値3409 SL3203.5 単元100 ｜
模擬 8801 granville_tenkan 逆指値1631 SL1532.7 単元100 ｜
模擬 5233 granville_tenkan 逆指値4098 SL3851.2 単元100 ｜
模擬 8803 granville_tenkan 逆指値2366 SL2223.1 単元100 ｜
模擬 9735 granville_tenkan 逆指値7121 SL6692.8 単元100 ｜
模擬 9404 granville_tenkan 逆指値2975.5 SL2796.5 単元100 ｜
模擬 9401 granville_tenkan 逆指値6313 SL5933.3 単元100 ｜
模擬 2897 granville_tenkan 逆指値2974.5 SL2795.6 単元100 ｜
模擬 3182 granville_tenkan 逆指値1883 SL1769.1 単元100 ｜
模擬 2811 granville_tenkan 逆指値2845.5 SL2674.3 単元100 ｜
模擬 2384 granville_oshime 指値5690 SL5671.2 単元100 ｜
模擬 5252 granville_rebound 指値1000 SL841 単元100 ｜
模擬 見送り ｜
```

## PASS内訳
PASS 93件 = 提案 50件（✅即時可40／⏳待機・確認足待ち0／⏸位置不適10／⏸トラップ疑い0） + 除外 43件（型不一致7（うち十字線4）/材料後出し12/鮮度切れ21/その他3）
- 3798 ULS Group Incorporated｜⛔型不一致(十字線: トウバ)
- 4379 Photosynth inc.｜⛔提案なし(指名鮮度切れ 15営業日)（nom_age 15）
- 3843 Freebit Co., Ltd.｜⛔提案なし(指名鮮度切れ 17営業日)（nom_age 17）
- 3282 Comforia Residential REIT, Inc.｜⛔提案なし(指名鮮度切れ 16営業日)（nom_age 16）
- 1820 Nishimatsu Construction Co., Ltd.｜⛔提案なし(指名鮮度切れ 20営業日)（nom_age 20）
- 8198 Maxvalu Tokai Co., Ltd.｜⛔提案なし(指名鮮度切れ 20営業日)（nom_age 20）
- 9533 TOHO GAS Co., Ltd.｜⛔提案なし(指名鮮度切れ 16営業日)（nom_age 16）
- 2379 dip Corporation｜⛔提案なし(指名鮮度切れ 19営業日)（nom_age 19）
- 6436 アマノ｜⛔提案なし(材料後出し)
- 9948 Arcs Company, Limited｜⛔提案なし(指名鮮度切れ 16営業日)（nom_age 16）
- 7942 ＪＳＰ｜⛔提案なし(手法ブランチ不明)
- 6758 ソニーグループ｜⛔提案なし(材料後出し)
- 3091 ブロンコビリー｜⛔提案なし(手法ブランチ不明)
- 6505 東洋電機製造｜⛔提案なし(材料後出し)
- 6532 ベイカレント｜⛔提案なし(手法ブランチ不明)
- 9432 NTT｜⛔型不一致(既に支持帯以下)
- 9434 ソフトバンク｜⛔型不一致(既に支持帯以下)
- 3496 アズーム｜⛔提案なし(材料後出し)
- 9842 アークランズ｜⛔提案なし(指名鮮度切れ 11営業日)（nom_age 11）
- 4549 Eiken Chemical Co., Ltd.｜⛔提案なし(指名鮮度切れ 17営業日)（nom_age 17）
- 4166 Cacco, Inc.｜⛔提案なし(指名鮮度切れ 17営業日)（nom_age 17）
- 3563 ＦＯＯＤ　＆　ＬＩＦＥ　ＣＯＭＰＡＮＩＥＳ｜⛔提案なし(指名鮮度切れ 11営業日)（nom_age 11）
- 9837 Morito Co., Ltd.｜⛔提案なし(指名鮮度切れ 15営業日)（nom_age 15）
- 4922 コーセーホールディングス｜⛔提案なし(材料後出し)
- 1928 積水ハウス｜⛔提案なし(材料後出し)
- 5105 ＴＯＹＯ　ＴＩＲＥ｜⛔提案なし(指名鮮度切れ 13営業日)（nom_age 13）
- 7921 ＴＡＫＡＲＡ　＆　ＣＯＭＰＡＮＹ｜⛔提案なし(指名鮮度切れ 13営業日)（nom_age 13）
- 4258 AMIYA Corporation｜⛔型不一致(十字線: トウバ)
- 3673 ブロードリーフ｜⛔型不一致(十字線: トウバ)
- 6036 ＫｅｅＰｅｒ技研｜⛔型不一致(既に支持帯以下)
- 6250 Yamabiko Corporation｜⛔提案なし(指名鮮度切れ 15営業日)（nom_age 15）
- 6191 エボラブルアジア｜⛔提案なし(材料後出し)
- 3042 セキュアヴェイル（セキュアヴェ）｜⛔提案なし(材料後出し)
- 4208 UBE Corporation｜⛔提案なし(指名鮮度切れ 21営業日)（nom_age 21）
- 150A ＪＳＨ｜⛔提案なし(指名鮮度切れ 11営業日)（nom_age 11）
- 9697 カプコン｜⛔提案なし(指名鮮度切れ 11営業日)（nom_age 11）
- 9278 BOOKOFF GROUP HOLDINGS LIMITED｜⛔提案なし(指名鮮度切れ 16営業日)（nom_age 16）
- 5256 Fusic Co.,Ltd.｜⛔提案なし(材料後出し)
- 5599 S&J Corporation｜⛔型不一致(十字線: トウバ)
- 5582 （名称取得不可）｜⛔提案なし(指名鮮度切れ 19営業日)（nom_age 19）
- 3923 ラクス｜⛔提案なし(材料後出し)
- 3989 シェアテク｜⛔提案なし(材料後出し)
- 593A Tier IV, Inc.｜⛔提案なし(材料後出し)

## 5手法銘柄
- 5137 Smart Drive Co. Ltd.｜kenmo_momentum｜🚀確変(12)｜💎割安(6.0)｜FAIL_INSEN｜293｜💰3.1万｜—
- 276A CCReB Advisors Inc.｜kenmo_momentum｜🚀確変(12)｜🟢値頃(5.0)｜FAIL_UWAHIGE｜3980｜💰40.2万｜—｜⚡材料後出し
- 3556 RenetJapanGroup, Inc.｜kenmo_momentum｜🚀確変(11)｜🟢値頃(5.0)｜FAIL_INSEN｜917｜💰9.2万｜—｜⚡材料後出し
- 5027 AnyMind Group Inc.｜kenmo_momentum｜🚀確変(11)｜⚪妥当(4.0)｜FAIL_INSEN｜717｜💰7.3万｜—｜⚡材料後出し
- 4053 Sun Asterisk, Inc.｜kenmo_momentum｜🚀確変(11)｜⚪妥当(3.0)｜FAIL_UWAHIGE｜555｜💰5.6万｜—｜⚡材料後出し 📑TOPIX低減対象（次 01/29 第2回/8）
- 4434 Serverworks Co., Ltd.｜kenmo_momentum｜🚀確変(11)｜⚪妥当(3.0)｜PASS｜3050｜💰30.5万｜逆指値3100 SL2909.3｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】アマゾンのクラウド「AWS」に特化。インフラ基盤構築、リセール、保守・運用代行。
  > 【いま】終値3,050円・直近5日+15.36%（材料未確認）
  > 【調子】🚀確変（11/13）
  > 【水準】⚪妥当（3.0/7）— PER14.76倍・PEG0.104・52週84.5% ／ 💰単元30.5万円
  > 【戦略】当日高値超えの逆指値3100円で順張り参戦を検討。上限3131円・SL2909.3円目安
- 5136 tripla Co.,Ltd.｜kenmo_momentum｜🚀確変(11)｜⚪妥当(3.0)｜FAIL_UWAHIGE｜2659｜💰27.4万｜—
- 5757 CK San-Etsu Co., Ltd.｜kenmo_momentum｜🔥絶好調(10)｜💎割安(7.0)｜FAIL_INSEN｜4600｜💰45.5万｜—｜⚡材料後出し 📑TOPIX低減対象（次 01/29 第2回/8）
- 8704 TRADERS HOLDINGS CO LTD｜kenmo_momentum｜🔥絶好調(10)｜💎割安(6.0)｜FAIL_UWAHIGE｜1274｜💰11.6万｜—
- 9554 AViC Co. Ltd.｜kenmo_momentum｜🔥絶好調(10)｜💎割安(6.0)｜FAIL_UWAHIGE｜1611｜💰14.6万｜—｜⚡材料後出し
- 3915 TerraSky Co., Ltd.｜kenmo_momentum｜🔥絶好調(10)｜🟢値頃(5.0)｜FAIL_INSEN｜2086｜💰21.7万｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 147A SORACOM,INC.｜kenmo_momentum｜🔥絶好調(10)｜⚪妥当(4.0)｜FAIL_UWAHIGE｜976｜💰9.4万｜—
- 4286 CL Holdings Inc.｜kenmo_momentum｜🔥絶好調(10)｜⚪妥当(4.0)｜FAIL_INSEN｜1466｜💰14.2万｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 6418 Japan Cash Machine Co., Ltd.｜kenmo_momentum｜🔥絶好調(10)｜⚪妥当(4.0)｜FAIL_UWAHIGE｜1458｜💰14.7万｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 1435 robot home Inc.｜kenmo_momentum｜🔥絶好調(9)｜💎割安(7.0)｜FAIL_INSEN｜165｜💰1.6万｜—｜⚡材料後出し 📑TOPIX低減対象（次 01/29 第2回/8）
- 5132 pluszero,Inc.｜kenmo_momentum｜🔥絶好調(9)｜🟢値頃(5.0)｜FAIL_INSEN｜1714｜💰17.8万｜—
- 4377 ONE CAREER Inc.｜kenmo_momentum｜🔥絶好調(9)｜⚪妥当(4.0)｜FAIL_UWAHIGE｜2665｜💰23.6万｜—
- 5537 AlbaLink Co.,Ltd.｜kenmo_momentum｜🔥絶好調(9)｜⚪妥当(4.0)｜FAIL_INSEN｜3440｜💰31.2万｜—
- 4771 F&M Co., Ltd.｜kenmo_momentum｜🔥絶好調(8)｜⚪妥当(4.0)｜FAIL_INSEN｜3015｜💰30.1万｜—
- 5821 Hirakawa Hewtech Corp.｜kenmo_momentum｜⚡好調(7)｜💎割安(6.0)｜FAIL_INSEN｜3220｜💰33.2万｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 9560 PROGRIT, Inc.｜kenmo_momentum｜⚡好調(7)｜🟢値頃(5.0)｜FAIL_UWAHIGE｜1001｜💰9.9万｜—
- 4058 Toyokumo, Inc.｜kenmo_momentum｜⚡好調(7)｜⚪妥当(4.0)｜FAIL_INSEN｜2147｜💰22.1万｜—
- 5034 unerry, Inc.｜kenmo_momentum｜⚡好調(7)｜⚪妥当(4.0)｜FAIL_UWAHIGE｜2289｜💰25.1万｜—｜⚡材料後出し
- 6071 IBJ, Inc.｜kenmo_momentum｜⚡好調(7)｜⚪妥当(4.0)｜FAIL_UWAHIGE｜986｜💰9.9万｜—｜⚡材料後出し 📑TOPIX低減対象（次 01/29 第2回/8）
- 558A SQUEEZE Inc.｜kenmo_momentum｜⚡好調(7)｜🟡やや割高(2.8)｜PASS｜6100｜💰61.0万｜逆指値6210 SL5828｜📉決算反応日 11/13 ⚠1単元でリスク枠超過（38200円）
  > 【業態】自社ホテル運営や、システム開発・提供、宿泊施設の企画・開発などを手掛ける。
  > 【いま】終値6,100円・直近5日+15.75%（材料未確認）
  > 【調子】⚡好調（7/13） — D軸判定不能(四半期データ不足)・E軸判定不能(進捗データ不足)
  > 【水準】🟡やや割高（2.8/7）— PER38.73倍・PEG1.171・52週83.8% ／ 💰単元61.0万円
  > 【戦略】当日高値超えの逆指値6210円で順張り参戦を検討。上限6272.1円・SL5828円目安／⚠1単元リスク38200円（枠超過）
- 7678 ASAKUMA CO.,LTD.｜kenmo_momentum｜⚡好調(7)｜🔴過熱(0.0)｜PASS｜4440｜💰44.4万｜逆指値4450 SL4178.3｜📋カルテ窓 12/09(残17営業日)
  > 【業態】愛知中心に「ステーキのあさくま」を店舗展開。テンポスホールディングス子会社。
  > 【いま】終値4,440円・直近5日+7.90%（材料未確認）
  > 【調子】⚡好調（7/13） — E軸判定不能(進捗データ不足)
  > 【水準】🔴過熱（0.0/7）— PER113.85倍・PEG4.159・52週95.3% ／ 💰単元44.4万円
  > 【戦略】当日高値超えの逆指値4450円で順張り参戦を検討。上限4494.5円・SL4178.3円目安
- 2975 Star Mica Holdings Co., Ltd.｜kenmo_momentum｜⚡好調(6)｜💎割安(6.0)｜FAIL_INSEN｜1220｜💰12.2万｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 262A INTERMESTIC INC.｜kenmo_momentum｜⚡好調(5)｜💎割安(6.0)｜FAIL_INSEN｜1646｜💰16.7万｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 505A Geekly,Inc.｜kenmo_momentum｜✅順調(4)｜💎割安(7.0)｜FAIL_INSEN｜1139｜💰11.4万｜—
- 3798 ULS Group Incorporated｜kenmo_momentum｜✅順調(4)｜💎割安(6.0)｜PASS_DOJI｜490｜💰4.9万｜⛔型不一致(十字線: トウバ)｜📐進捗 遅れ -12.6%
  > 【業態】ITシステムの設計・構築・コンサルを展開。流通・製造・情報サービス業向けが中心。
  > 【いま】終値490円・直近5日-6.67%・📌2027年3月期第2四半期（中間期）決算説明会資料
  > 【調子】✅順調（4/13） — ⚠減速・⚠進捗遅れ・⚠下期依存
  > 【水準】💎割安（6.0/7）— PER12.47倍・PEG0.600・52週7.6% ／ 💰単元4.9万円
  > 【戦略】発注対象外（⛔型不一致(十字線: トウバ)）
- 4743 ITFOR Inc.｜kenmo_momentum｜✅順調(4)｜💎割安(6.0)｜PASS｜1618｜💰16.2万｜逆指値1628 SL1529.4｜📉決算反応日 11/13 📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】未取得（次回以降に取得）
  > 【いま】終値1,618円・直近5日+5.41%（材料未確認）
  > 【調子】✅順調（4/13） — E軸判定不能(進捗データ不足)
  > 【水準】💎割安（6.0/7）— PER12.59倍・PEG0.603・52週37.7% ／ 💰単元16.2万円
  > 【戦略】当日高値超えの逆指値1628円で順張り参戦を検討。上限1644.3円・SL1529.4円目安
- 3077 Horiifoodservice Co., Ltd.｜kenmo_momentum｜判定保留(変則決算)(None)｜🟢値頃(5.6)｜FAIL_UWAHIGE｜1138｜💰11.9万｜—｜⚡材料後出し
- 618A KOMPEITO Inc.｜kenmo_momentum｜取得不可(None)｜⚪妥当(4.0)｜FAIL_UWAHIGE｜2075｜💰19.5万｜—
- 446A ノースサンド｜kenmo_newhigh｜🔥絶好調(9)｜⚪妥当(3.0)｜PASS｜2604｜💰26.0万｜逆指値2663 SL2502.3（⏸位置不適(25MA下 -2.43%)）｜📋カルテ窓 12/11(残19営業日)
  > 【業態】ITコンサルティング、ビジネスコンサルティングやNotionサービスの提供などを手掛ける。
  > 【いま】終値2,604円・直近5日+2.84%（材料未確認）
  > 【調子】🔥絶好調（9/13） — D軸判定不能(四半期データ不足・中立1点)・E軸判定不能(進捗データ不足)・⚠進捗遅れ
  > 【水準】⚪妥当（3.0/7）— PER26.33倍・PEG0.386・52週81.0% ／ 💰単元26.0万円
  > 【戦略】当日高値超えの逆指値2663円で順張り参戦を検討。上限2689.6円・SL2502.3円目安（⏸位置不適(25MA下 -2.43%)）
- 3696 セレス｜kenmo_newhigh｜🔥絶好調(8)｜💎割安(6.0)｜FAIL_UWAHIGE｜2157｜💰20.8万｜—｜⚡材料後出し 📑TOPIX低減対象（次 01/29 第2回/8）
- 2930 北の達人コーポレーション｜kenmo_newhigh｜⚡好調(6)｜🔴過熱(0.0)｜FAIL_INSEN｜148｜💰1.5万｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 4379 Photosynth inc.｜kenmo_newhigh｜⚡好調(5)｜🔴過熱(1.0)｜PASS｜453｜💰4.5万｜⛔提案なし(指名鮮度切れ 15営業日)｜📉決算反応日 11/13 ⚡材料後出し 📐進捗 上振れ 18.7%
  > 【業態】IoT関連機器や「Akerun入退室管理システム」など展開。住宅向け市場も注力。
  > 【いま】終値453円・直近5日+5.35%・📌2026年12月期第3四半期決算説明会（書き起こし＆質疑応答）
  > 【調子】⚡好調（5/13） — 質注意・🔼進捗先行
  > 【水準】🔴過熱（1.0/7）— PER23.72倍・PEG9.250・52週53.3% ／ 💰単元4.5万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 15営業日)）
- 3843 Freebit Co., Ltd.｜kenmo_newhigh｜✅順調(4)｜🟡やや割高(2.0)｜PASS｜2023｜💰20.2万｜⛔提案なし(指名鮮度切れ 17営業日)｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】ネット接続にインフラ提供サービス。ドコモと提携、MVNOトーン運営。企業DX支援も展開。
  > 【いま】終値2,023円・直近5日+2.07%（材料未確認）
  > 【調子】✅順調（4/13）
  > 【水準】🟡やや割高（2.0/7）— PER9.81倍・PEG1.962・52週88.6% ／ 💰単元20.2万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 17営業日)）
- 9204 Skymark Airlines Inc.｜kenmo_newhigh｜🔻悪化(3)｜🔴過熱(0.0)｜FAIL_UWAHIGE｜490｜💰4.7万｜—
- 1960 サンテック｜kenmo_newhigh｜➖横ばい(2)｜🔴過熱(1.0)｜FAIL_INSEN｜1837｜💰18.5万｜—
- 4933 I-ne CO., LTD.｜kenmo_newhigh｜取得不可(None)｜⚪妥当(3.0)｜FAIL_INSEN｜2403｜💰24.8万｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 4565 Nxera Pharma Co., Ltd.｜kenmo_newhigh｜業績データ取得不可(経常益予想非開示)(None)｜🟡やや割高(2.8)｜FAIL_UWAHIGE｜1813｜💰18.0万｜—
- 6943 ＮＫＫスイッチズ｜kenmo_newhigh｜業績—｜－未評価｜FAIL_INSEN｜6990｜💰—｜—
- 6278 ユニオンツール｜choruko_reversal｜🚀確変(13)｜🟢値頃(5.0)｜FAIL_INSEN｜11470｜💰117.7万｜—
- 5711 三菱マテリアル｜choruko_reversal｜🚀確変(12)｜💎割安(7.0)｜FAIL_INSEN｜4307｜💰41.3万｜—
- 3036 アルコニックス｜choruko_reversal｜🚀確変(12)｜🟢値頃(5.0)｜FAIL_INSEN｜3180｜💰32.7万｜—
- 6324 Harmonic Drive Systems Inc.｜choruko_reversal｜🚀確変(12)｜🟢値頃(5.0)｜FAIL_INSEN｜4775｜💰49.9万｜—
- 7995 Valqua Ltd.｜choruko_reversal｜🚀確変(11)｜🟢値頃(5.0)｜FAIL_INSEN｜6180｜💰62.6万｜—
- 6516 Sanyo Denki Co., Ltd.｜choruko_reversal｜🔥絶好調(10)｜💎割安(6.0)｜FAIL_INSEN｜4545｜💰46.1万｜—
- 5344 MARUWA CO., LTD.｜choruko_reversal｜🔥絶好調(10)｜🟢値頃(5.0)｜FAIL_INSEN｜44130｜💰458.6万｜—
- 6645 OMRON Corporation｜choruko_reversal｜🔥絶好調(10)｜🟢値頃(5.0)｜FAIL_INSEN｜4977｜💰49.4万｜—
- 4216 ASAHI YUKIZAI CORPORATION｜choruko_reversal｜🔥絶好調(9)｜💎割安(6.0)｜FAIL_INSEN｜5730｜💰57.2万｜—
- 4471 三洋化成工業｜choruko_reversal｜🔥絶好調(9)｜💎割安(6.0)｜FAIL_INSEN｜1493｜💰15.1万｜—
- 5703 日本軽金属ホールディングス（日軽金ＨＤ）｜choruko_reversal｜🔥絶好調(9)｜💎割安(6.0)｜FAIL_INSEN｜2565｜💰25.7万｜—
- 7433 Hakuto Co., Ltd.｜choruko_reversal｜🔥絶好調(9)｜💎割安(6.0)｜FAIL_UWAHIGE｜1559｜💰16.1万｜—
- 8084 ＲＹＯＤＥＮ｜choruko_reversal｜🔥絶好調(9)｜💎割安(6.0)｜FAIL_INSEN｜2235｜💰22.3万｜—｜⚡材料後出し
- 5301 Tokai Carbon Co., Ltd.｜choruko_reversal｜🔥絶好調(9)｜🟢値頃(5.0)｜FAIL_INSEN｜1629.5｜💰16.7万｜—
- 6268 ナブテスコ｜choruko_reversal｜🔥絶好調(9)｜🟢値頃(5.0)｜FAIL_INSEN｜4149｜💰42.4万｜—｜⚡材料後出し
- 6481 THK Co., Ltd.｜choruko_reversal｜🔥絶好調(9)｜🟢値頃(5.0)｜FAIL_INSEN｜5472｜💰55.8万｜—｜⚡材料後出し
- 6588 東芝テック｜choruko_reversal｜🔥絶好調(9)｜🟢値頃(5.0)｜FAIL_INSEN｜2507｜💰26.9万｜—
- 6652 IDEC Corporation｜choruko_reversal｜🔥絶好調(9)｜🟢値頃(5.0)｜FAIL_INSEN｜3095｜💰31.6万｜—
- 6724 セイコーエプソン｜choruko_reversal｜🔥絶好調(9)｜🟢値頃(5.0)｜FAIL_INSEN｜2853.5｜💰28.6万｜—
- 6925 Ushio Inc.｜choruko_reversal｜🔥絶好調(9)｜🟢値頃(5.0)｜FAIL_INSEN｜3162｜💰32.3万｜—｜⚡材料後出し
- 6875 メガチップス｜choruko_reversal｜🔥絶好調(8)｜💎割安(7.0)｜FAIL_INSEN｜8610｜💰87.2万｜—
- 6471 日本精工｜choruko_reversal｜🔥絶好調(8)｜💎割安(6.0)｜FAIL_INSEN｜1002｜💰10.1万｜—
- 8386 百十四銀行｜choruko_reversal｜🔥絶好調(8)｜💎割安(6.0)｜FAIL_INSEN｜2854｜💰28.5万｜—
- 6754 アンリツ｜choruko_reversal｜🔥絶好調(8)｜🟢値頃(5.0)｜FAIL_INSEN｜2377｜💰24.4万｜—
- 7731 ニコン｜choruko_reversal｜🔥絶好調(8)｜🟢値頃(5.0)｜FAIL_INSEN｜1604｜💰16.5万｜—
- 9902 Nichiden Corporation｜choruko_reversal｜🔥絶好調(8)｜🟢値頃(5.0)｜FAIL_INSEN｜2940｜💰29.6万｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 7733 Olympus Corp.｜choruko_reversal｜🔥絶好調(8)｜⚪妥当(4.0)｜FAIL_INSEN｜1776｜💰17.9万｜—
- 4088 Air Water Inc.｜choruko_reversal｜🔥絶好調(8)｜⚪妥当(3.0)｜FAIL_UWAHIGE｜2886｜💰29.0万｜—
- 8133 伊藤忠エネクス｜choruko_reversal｜🔥絶好調(8)｜🟡やや割高(2.0)｜PASS｜2068｜💰20.7万｜指値2068 SL1977｜⚠日程不明 📐進捗 上振れ 83.7%
  > 【業態】伊藤忠系の燃料商社最大手。産業用燃料やLPGなど。カーライフ部門が拡大。
  > 【いま】終値2,068円・直近5日+5.08%（材料未確認）
  > 【調子】🔥絶好調（8/13） — 4Q換算（変則決算）・🔼進捗先行
  > 【水準】🟡やや割高（2.0/7）— PER14.15倍・PEG7.592・52週48.5% ／ 💰単元20.7万円
  > 【戦略】当日終値2068円の指値で反転を取りにいく。SL1977円（直近5日安値）
- 5333 ＮＧＫ｜choruko_reversal｜⚡好調(7)｜💎割安(6.0)｜FAIL_INSEN｜4805｜💰48.3万｜—
- 7721 Tokyo Keiki Inc.｜choruko_reversal｜⚡好調(7)｜💎割安(6.0)｜FAIL_INSEN｜4790｜💰54.3万｜—
- 8154 加賀電子｜choruko_reversal｜⚡好調(7)｜💎割安(6.0)｜FAIL_UWAHIGE｜5320｜💰51.5万｜—
- 3433 TOCALO Co., Ltd.｜choruko_reversal｜⚡好調(7)｜🟢値頃(5.0)｜FAIL_INSEN｜2602｜💰26.0万｜—
- 5186 ニッタ｜choruko_reversal｜⚡好調(7)｜🟢値頃(5.0)｜FAIL_INSEN｜6440｜💰64.3万｜—
- 8393 Miyazaki Bank Ltd.｜choruko_reversal｜⚡好調(7)｜🟢値頃(5.0)｜FAIL_INSEN｜2450｜💰25.4万｜—
- 8522 Bank of Nagoya, Ltd.｜choruko_reversal｜⚡好調(7)｜🟢値頃(5.0)｜FAIL_UWAHIGE｜6050｜💰58.6万｜—
- 167A リョーサン菱洋ホールディングス（リョー菱ＨＤ）｜choruko_reversal｜⚡好調(7)｜⚪妥当(4.0)｜FAIL_INSEN｜3140｜💰30.9万｜—
- 6302 住友重機械工業｜choruko_reversal｜⚡好調(7)｜⚪妥当(4.0)｜FAIL_INSEN｜5079｜💰52.4万｜—
- 6448 ブラザー工業（ブラザー）｜choruko_reversal｜⚡好調(7)｜⚪妥当(4.0)｜FAIL_INSEN｜4560｜💰46.0万｜—
- 3116 Toyota Boshoku Corp.｜choruko_reversal｜⚡好調(6)｜💎割安(7.0)｜PASS｜2086.5｜💰20.9万｜指値2086.5 SL2022.5｜⚠日程不明
  > 【業態】トヨタ系。アラコ、タカニチと合併。自動車シートとエアフィルターで国内首位。
  > 【いま】終値2,086円・直近5日+3.65%（材料未確認）
  > 【調子】⚡好調（6/13）
  > 【水準】💎割安（7.0/7）— PER8.11倍・PEG0.278・52週9.0% ／ 💰単元20.9万円
  > 【戦略】当日終値2086.5円の指値で反転を取りにいく。SL2022.5円（直近5日安値）
- 5331 ノリタケ｜choruko_reversal｜⚡好調(6)｜💎割安(7.0)｜FAIL_INSEN｜3005｜💰30.5万｜—
- 7004 カナデビア｜choruko_reversal｜⚠減速(6)｜💎割安(7.0)｜FAIL_INSEN｜967｜💰9.7万｜—
- 6651 NITTO KOGYO Corporation｜choruko_reversal｜⚡好調(6)｜💎割安(6.0)｜FAIL_INSEN｜4175｜💰41.9万｜—｜⚡材料後出し
- 4205 Zeon Corporation｜choruko_reversal｜⚡好調(6)｜🟢値頃(5.0)｜FAIL_INSEN｜2100｜💰21.0万｜—
- 4966 上村工業｜choruko_reversal｜⚡好調(6)｜🟢値頃(5.0)｜FAIL_INSEN｜16630｜💰166.7万｜—｜📑TOPIX新規採用（10/30 組入）
- 5101 Yokohama Rubber Co., Ltd.｜choruko_reversal｜⚡好調(6)｜🟢値頃(5.0)｜PASS｜7321｜💰73.2万｜指値7321 SL6818｜📉決算反応日 11/16 ⚠1単元でリスク枠超過（50300円） ℹ相対強い RS20 5.5pt
  > 【業態】タイヤ大手。工業資材や航空部品、ゴルフ用品も展開。北米や農機用タイヤが拡大。
  > 【いま】終値7,321円・直近5日+8.07%・📊Consolidated Financial Results for the Nine Months Ended September 30, 2026[IFRS]
  > 【調子】⚡好調（6/13） — 経常非開示(IFRS等)のため最終益成長率で代替・税引前代替・E軸判定不能(進捗データ不足)
  > 【水準】🟢値頃（5.0/7）— PER9.87倍・PEG—・52週63.9% ／ 💰単元73.2万円
  > 【戦略】当日終値7321円の指値で反転を取りにいく。SL6818円（直近5日安値）／⚠1単元リスク50300円（枠超過）
- 5463 丸一鋼管（丸一管）｜choruko_reversal｜⚡好調(6)｜🟢値頃(5.0)｜FAIL_INSEN｜1660｜💰16.4万｜—
- 6473 ジェイテクト｜choruko_reversal｜⚠減速(6)｜⚪妥当(4.0)｜FAIL_UWAHIGE｜2088.5｜💰20.8万｜—
- 8098 稲畑産業｜choruko_reversal｜⚡好調(6)｜⚪妥当(4.0)｜FAIL_INSEN｜4370｜💰43.5万｜—
- 268A Rigaku Holdings Corporation｜choruko_reversal｜⚡好調(6)｜⚪妥当(3.0)｜FAIL_UWAHIGE｜1369｜💰13.8万｜—
- 3569 セーレン｜choruko_reversal｜⚡好調(6)｜⚪妥当(3.0)｜FAIL_UWAHIGE｜3620｜💰35.1万｜—
- 4634 ａｒｔｉｅｎｃｅ（ａｒｔｉｅｎ）｜choruko_reversal｜⚡好調(6)｜⚪妥当(3.0)｜FAIL_INSEN｜4810｜💰48.8万｜—｜⚡材料後出し
- 6952 カシオ｜choruko_reversal｜⚡好調(6)｜⚪妥当(3.0)｜FAIL_INSEN｜2033｜💰22.7万｜—
- 6845 アズビル｜choruko_reversal｜⚡好調(6)｜🔴過熱(1.0)｜FAIL_INSEN｜1555｜💰15.2万｜—
- 5444 大和工業｜choruko_reversal｜⚡好調(5)｜💎割安(6.0)｜FAIL_INSEN｜10930｜💰109.5万｜—
- 9934 因幡電機産業｜choruko_reversal｜⚡好調(5)｜⚪妥当(4.0)｜FAIL_INSEN｜2617｜💰26.6万｜—
- 1721 コムシスホールディングス｜choruko_reversal｜⚡好調(5)｜⚪妥当(3.0)｜FAIL_UWAHIGE｜5264｜💰52.4万｜—
- 1926 ライト工業（ライト）｜choruko_reversal｜⚡好調(5)｜⚪妥当(3.0)｜FAIL_UWAHIGE｜1040｜💰10.2万｜—
- 9072 NIKKON Holdings Co., Ltd.｜choruko_reversal｜⚡好調(5)｜⚪妥当(3.0)｜FAIL_INSEN｜4209｜💰42.5万｜—
- 6454 マックス｜choruko_reversal｜⚡好調(5)｜🟡やや割高(2.0)｜FAIL_INSEN｜1811｜💰17.9万｜—
- 9302 三井倉庫ホールディングス｜choruko_reversal｜⚡好調(5)｜🟡やや割高(2.0)｜PASS｜3215｜💰32.1万｜指値3215 SL3177｜⚠日程不明
  > 【業態】倉庫業大手。総合物流業務に強み。国際サプライチェーン展開。不動産賃貸が収益。
  > 【いま】終値3,215円・直近5日+4.35%（材料未確認）
  > 【調子】⚡好調（5/13） — 上方修正済み・🔼加速
  > 【水準】🟡やや割高（2.0/7）— PER18.50倍・PEG3.238・52週11.0% ／ 💰単元32.1万円
  > 【戦略】当日終値3215円の指値で反転を取りにいく。SL3177円（直近5日安値）
- 9960 トーテック｜choruko_reversal｜⚡好調(5)｜🟡やや割高(2.0)｜PASS｜4515｜💰45.1万｜指値4515 SL3820｜⚠日程不明 📐進捗 上振れ 11.8% ⚠1単元でリスク枠超過（69500円） ℹ相対強い RS20 9.8pt
  > 【業態】空調機器・関連機器専門商社で首位。設計・施工・保守の工事部門を拡大。
  > 【いま】終値4,515円・直近5日+19.13%（材料未確認）
  > 【調子】⚡好調（5/13） — 上方修正済み・⚠減速・🔼進捗先行
  > 【水準】🟡やや割高（2.0/7）— PER12.86倍・PEG1.525・52週94.6% ／ 💰単元45.1万円
  > 【戦略】当日終値4515円の指値で反転を取りにいく。SL3820円（直近5日安値）／⚠1単元リスク69500円（枠超過）
- 6135 牧野フライス製作所｜choruko_reversal｜✅順調(4)｜💎割安(6.0)｜FAIL_INSEN｜2789｜💰28.1万｜—
- 1417 MIRAIT ONE Corporation｜choruko_reversal｜✅順調(4)｜🟢値頃(5.0)｜FAIL_INSEN｜3434｜💰34.0万｜—
- 6340 澁谷工業｜choruko_reversal｜✅順調(4)｜🟢値頃(5.0)｜FAIL_INSEN｜4935｜💰50.9万｜—
- 6674 ジーエス・ユアサ　コーポレーション｜choruko_reversal｜✅順調(4)｜🟢値頃(5.0)｜FAIL_INSEN｜4459｜💰45.9万｜—
- 8381 San-in Godo Bank Ltd.｜choruko_reversal｜✅順調(4)｜⚪妥当(4.2)｜FAIL_INSEN｜2144.5｜💰21.9万｜—
- 4272 Nippon Kayaku Co., Ltd.｜choruko_reversal｜✅順調(4)｜⚪妥当(4.0)｜FAIL_INSEN｜1883.5｜💰18.6万｜—
- 6284 日精エー・エス・ビー機械｜choruko_reversal｜✅順調(4)｜⚪妥当(4.0)｜FAIL_INSEN｜8610｜💰79.7万｜—
- 6923 Stanley Electric Co., Ltd.｜choruko_reversal｜✅順調(4)｜⚪妥当(4.0)｜FAIL_UWAHIGE｜3242｜💰32.5万｜—
- 7276 Koito Manufacturing Co., Ltd.｜choruko_reversal｜⚠減速(4)｜⚪妥当(4.0)｜FAIL_INSEN｜2524｜💰25.0万｜—
- 4042 東ソー｜choruko_reversal｜✅順調(4)｜⚪妥当(3.0)｜FAIL_UWAHIGE｜2531.5｜💰25.0万｜—
- 3282 Comforia Residential REIT, Inc.｜choruko_reversal｜✅順調(4)｜🟡やや割高(2.8)｜PASS｜87000｜💰8.7万｜⛔提案なし(指名鮮度切れ 16営業日)｜⚠日程不明
  > 【業態】東京圏の独身・小家族向け居住用賃貸住宅に投資。運用:東急不動産リート。
  > 【いま】終値87,000円・直近5日-0.91%（材料未確認）
  > 【調子】✅順調（4/13） — 前年同期比（半期決算等・期間が12か月でない）・E軸判定不能(進捗データ不足)・D軸判定不能(四半期データ不足・中立1点)
  > 【水準】🟡やや割高（2.8/7）— PER38.67倍・PEG3.619・52週7.1% ／ 💰単元8.7万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 16営業日)）
- 8524 North Pacific Bank, Ltd.｜choruko_reversal｜⚠減速(4)｜🟡やや割高(2.8)｜FAIL_INSEN｜1235｜💰12.5万｜—
- 1820 Nishimatsu Construction Co., Ltd.｜choruko_reversal｜✅順調(4)｜🟡やや割高(2.0)｜PASS｜5809｜💰58.1万｜⛔提案なし(指名鮮度切れ 20営業日)｜⚠日程不明 📐進捗 上振れ 66.1%
  > 【業態】総合建設会社。ダム・トンネルなど土木に強み。開発事業強化。伊藤忠の持分法。
  > 【いま】終値5,809円・直近5日+13.68%（材料未確認）
  > 【調子】✅順調（4/13） — 質注意・上方修正済み・🔼進捗先行
  > 【水準】🟡やや割高（2.0/7）— PER10.67倍・PEG4.743・52週41.1% ／ 💰単元58.1万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 20営業日)）
- 4021 Nissan Chemical Corporation｜choruko_reversal｜✅順調(4)｜🟡やや割高(2.0)｜FAIL_INSEN｜6955｜💰70.2万｜—
- 5631 Japan Steel Works, Ltd.｜choruko_reversal｜✅順調(4)｜🟡やや割高(2.0)｜FAIL_INSEN｜5419｜💰60.1万｜—
- 6750 エレコム｜choruko_reversal｜✅順調(4)｜🟡やや割高(2.0)｜PASS｜1887｜💰18.9万｜指値1887 SL1799｜📉決算反応日 11/13 📐進捗 上振れ 58.3%
  > 【業態】PC周辺機器メーカー大手。マウス、キーボード、スマホ・タブレット周辺機器でトップ。ファブレス。
  > 【いま】終値1,887円・直近5日+1.94%（材料未確認）
  > 【調子】✅順調（4/13） — 経常減益-1.2%・質注意・🔼進捗先行
  > 【水準】🟡やや割高（2.0/7）— PER13.28倍・PEG—・52週63.5% ／ 💰単元18.9万円
  > 【戦略】当日終値1887円の指値で反転を取りにいく。SL1799円（直近5日安値）
- 1944 Kinden Corporation｜choruko_reversal｜✅順調(3)｜🟢値頃(5.0)｜FAIL_INSEN｜5949｜💰58.7万｜—｜⚡材料後出し
- 6332 月島ホールディングス｜choruko_reversal｜✅順調(3)｜⚪妥当(4.0)｜FAIL_INSEN｜2388｜💰23.9万｜—
- 6368 Organo Corp.｜choruko_reversal｜✅順調(3)｜⚪妥当(4.0)｜FAIL_INSEN｜1830｜💰18.0万｜—
- 8198 Maxvalu Tokai Co., Ltd.｜choruko_reversal｜✅順調(3)｜⚪妥当(4.0)｜PASS｜3195｜💰31.9万｜⛔提案なし(指名鮮度切れ 20営業日)｜⚠日程不明
  > 【業態】イオン系の食品スーパー。旧ヤオハンを母体に静岡県を中心とする出店。
  > 【いま】終値3,195円・直近5日+3.90%（材料未確認）
  > 【調子】✅順調（3/13）
  > 【水準】⚪妥当（4.0/7）— PER10.96倍・PEG1.624・52週17.5% ／ 💰単元31.9万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 20営業日)）
- 1951 エクシオグループ（エクシオＧ）｜choruko_reversal｜⚠減速(3)｜⚪妥当(3.0)｜FAIL_INSEN｜2432.5｜💰24.0万｜—
- 1952 Shin Nippon Air Technologies Co., Ltd.｜choruko_reversal｜✅順調(3)｜⚪妥当(3.0)｜FAIL_UWAHIGE｜3120｜💰30.2万｜—
- 4028 石原産業｜choruko_reversal｜🔻悪化(3)｜⚪妥当(3.0)｜FAIL_UWAHIGE｜2659｜💰26.2万｜—
- 5021 コスモＨＤ｜choruko_reversal｜🔻悪化(3)｜⚪妥当(3.0)｜FAIL_INSEN｜3481｜💰36.0万｜—
- 5602 栗本鐵工所（栗本鉄）｜choruko_reversal｜✅順調(3)｜⚪妥当(3.0)｜FAIL_INSEN｜1457｜💰14.6万｜—
- 9533 TOHO GAS Co., Ltd.｜choruko_reversal｜🔻悪化(3)｜⚪妥当(3.0)｜PASS｜1267.5｜💰12.7万｜⛔提案なし(指名鮮度切れ 16営業日)｜⚠日程不明 ⚠業績基調が下向き（🔻悪化） 📐進捗 遅れ -81.6%
  > 【業態】都市ガス大手。愛知、岐阜、三重が拠点。LPGに強み。コージェネ事業に注力。
  > 【いま】終値1,268円・直近5日+4.06%（材料未確認）
  > 【調子】🔻悪化（3/13） — 質注意・⚠進捗遅れ
  > 【水準】⚪妥当（3.0/7）— PER15.92倍・PEG—・52週50.4% ／ 💰単元12.7万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 16営業日)）
- 1963 日揮ホールディングス｜choruko_reversal｜⚠減速(3)｜🟡やや割高(2.0)｜FAIL_INSEN｜2105.5｜💰22.4万｜—
- 3105 日清紡ホールディングス｜choruko_reversal｜✅順調(3)｜🟡やや割高(2.0)｜FAIL_INSEN｜1941｜💰19.9万｜—
- 6055 Japan Material Co., Ltd.｜choruko_reversal｜✅順調(3)｜🟡やや割高(2.0)｜FAIL_INSEN｜1668｜💰18.7万｜—
- 6379 レイズネク｜choruko_reversal｜✅順調(3)｜🔴過熱(2.0)｜FAIL_INSEN｜938｜💰10.2万｜—
- 6741 日本信号｜choruko_reversal｜✅順調(3)｜🟡やや割高(2.0)｜FAIL_INSEN｜1652｜💰16.7万｜—
- 6807 Japan Aviation Electronics Industry, Limited｜choruko_reversal｜✅順調(3)｜🟡やや割高(2.0)｜FAIL_INSEN｜2324｜💰23.2万｜—
- 7220 Musashi Seimitsu Industry Co., Ltd.｜choruko_reversal｜🔻悪化(3)｜🟡やや割高(2.0)｜FAIL_INSEN｜2155｜💰24.0万｜—
- 5310 Toyo Tanso Co., Ltd.｜choruko_reversal｜🔻悪化(3)｜🔴過熱(1.0)｜FAIL_INSEN｜6220｜💰63.1万｜—
- 6479 ミネベア｜choruko_reversal｜➖横ばい(2)｜💎割安(6.0)｜FAIL_INSEN｜3048｜💰29.7万｜—
- 1979 大気社｜choruko_reversal｜➖横ばい(2)｜⚪妥当(3.0)｜PASS｜3530｜💰35.3万｜指値3530 SL3245｜⚠日程不明
  > 【業態】空調工事大手。自動車塗装設備工事で国内トップ。海外積極展開。
  > 【いま】終値3,530円・直近5日+6.17%（材料未確認）
  > 【調子】➖横ばい（2/13） — 質注意・⚠減速
  > 【水準】⚪妥当（3.0/7）— PER12.21倍・PEG14.409・52週24.6% ／ 💰単元35.3万円
  > 【戦略】当日終値3530円の指値で反転を取りにいく。SL3245円（直近5日安値）
- 4008 住友精化｜choruko_reversal｜🔻悪化(2)｜⚪妥当(3.0)｜FAIL_INSEN｜1359｜💰13.8万｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 7278 Exedy Corporation｜choruko_reversal｜➖横ばい(2)｜⚪妥当(3.0)｜FAIL_INSEN｜5320｜💰53.2万｜—
- 3445 RS Technologies Co. Ltd.｜choruko_reversal｜➖横ばい(2)｜🟡やや割高(2.8)｜FAIL_INSEN｜4555｜💰47.5万｜—｜⚡材料後出し
- 6366 Chiyoda Corp.｜choruko_reversal｜🔻悪化(2)｜🟡やや割高(2.0)｜FAIL_INSEN｜721｜💰7.6万｜—｜📑TOPIX新規採用（10/30 組入）
- 9722 藤田観光｜choruko_reversal｜➖横ばい(2)｜🔴過熱(2.0)｜FAIL_UWAHIGE｜2838｜💰28.8万｜—｜⚡材料後出し
- 5844 Kyoto Financial Group,Inc.｜choruko_reversal｜🔻悪化(2)｜🔴過熱(1.4)｜FAIL_INSEN｜4153｜💰42.4万｜—｜⚡材料後出し
- 9468 カドカワ｜choruko_reversal｜➖横ばい(2)｜🔴過熱(0.0)｜FAIL_UWAHIGE｜3428｜💰38.7万｜—
- 2379 dip Corporation｜choruko_reversal｜⚠減速(1)｜💎割安(7.0)｜PASS｜1545｜💰15.4万｜⛔提案なし(指名鮮度切れ 19営業日)｜⚠日程不明 ⚠業績基調が下向き（⚠減速） ⚠バリュートラップ疑い
  > 【業態】求人・転職サイト「バイトル」を運営。派遣会社向け管理システムや業務自動化も展開。
  > 【いま】終値1,545円・直近5日+1.91%（材料未確認）
  > 【調子】⚠減速（1/13） — E軸判定不能(進捗データ不足)・赤字企業(経常赤字)
  > 【水準】💎割安（7.0/7）— PER—倍・PEG—・52週13.1% ／ 💰単元15.4万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 19営業日)）
- 6632 JVCKENWOOD Corporation｜choruko_reversal｜⚠減速(1)｜⚪妥当(4.0)｜FAIL_INSEN｜820｜💰8.3万｜—
- 1946 Toenec Corporation｜choruko_reversal｜⚠減速(1)｜⚪妥当(3.0)｜FAIL_INSEN｜1827｜💰18.6万｜—
- 4746 東計電算｜choruko_reversal｜⚠減速(1)｜⚪妥当(3.0)｜FAIL_UWAHIGE｜1799｜💰17.7万｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 4980 Dexerials Corp.｜choruko_reversal｜⚠減速(1)｜⚪妥当(3.0)｜FAIL_INSEN｜2067｜💰26.0万｜—
- 6370 栗田工業｜choruko_reversal｜🔻悪化(1)｜🟡やや割高(2.0)｜FAIL_UWAHIGE｜5724｜💰55.8万｜—
- 6436 アマノ｜choruko_reversal｜⚠減速(1)｜🟡やや割高(2.0)｜PASS｜3565｜💰35.6万｜⛔提案なし(材料後出し)｜⚠日程不明 ⚡材料後出し ⚠業績基調が下向き（⚠減速）
  > 【業態】就業情報システムは世界高シェア。駐車場管理システムや環境関連システムも拡大。
  > 【いま】終値3,565円・直近5日+3.30%・📌Amano Group Corporate Governance Report
  > 【調子】⚠減速（1/13） — 経常減益-11.7%・質注意
  > 【水準】🟡やや割高（2.0/7）— PER17.01倍・PEG—・52週18.2% ／ 💰単元35.6万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 6960 Fukuda Denshi Co., Ltd.｜choruko_reversal｜⚠減速(1)｜🟡やや割高(2.0)｜FAIL_UWAHIGE｜10120｜💰100.3万｜—｜📑TOPIX新規採用（10/30 組入）
- 9948 Arcs Company, Limited｜choruko_reversal｜⚠減速(1)｜🟡やや割高(2.0)｜PASS｜3725｜💰37.2万｜⛔提案なし(指名鮮度切れ 16営業日)｜⚠日程不明 ⚠業績基調が下向き（⚠減速）
  > 【業態】北海道最大の食品スーパー。青森、岩手も首位。ローコスト経営に強み。M&A積極。
  > 【いま】終値3,725円・直近5日+4.78%（材料未確認）
  > 【調子】⚠減速（1/13）
  > 【水準】🟡やや割高（2.0/7）— PER16.01倍・PEG6.987・52週66.1% ／ 💰単元37.2万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 16営業日)）
- 9301 三菱倉｜choruko_reversal｜⚠減速(1)｜🔴過熱(0.0)｜FAIL_INSEN｜1256｜💰15.4万｜—
- 6804 ホシデン｜choruko_reversal｜🔻悪化(0)｜⚪妥当(4.0)｜FAIL_UWAHIGE｜2217｜💰22.0万｜—｜⚡材料後出し
- 7148 Financial Products Group Co., Ltd.｜choruko_reversal｜⚠減速(0)｜⚪妥当(4.0)｜PASS｜1424｜💰14.2万｜指値1424 SL1380｜⚠日程不明 ⚠業績基調が下向き（⚠減速）
  > 【業態】船舶やコンテナのオペリース事業が主力。不動産小口化、保険や証券など多角化。
  > 【いま】終値1,424円・直近5日+3.64%（材料未確認）
  > 【調子】⚠減速（0/13） — E軸判定不能(期首・進捗なし)・質注意
  > 【水準】⚪妥当（4.0/7）— PER7.95倍・PEG—・52週7.3% ／ 💰単元14.2万円
  > 【戦略】当日終値1424円の指値で反転を取りにいく。SL1380円（直近5日安値）
- 2109 ＤＭ三井製糖｜choruko_reversal｜⚠減速(0)｜🟡やや割高(2.0)｜PASS｜3625｜💰36.2万｜指値3625 SL3515｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8） ⚠業績基調が下向き（⚠減速）
  > 【業態】精糖最大手「スプーン印」三井糖と「ばら印」大日明治が統合。食品化学も注力。
  > 【いま】終値3,625円・直近5日+3.28%（材料未確認）
  > 【調子】⚠減速（0/13） — ⚠減速
  > 【水準】🟡やや割高（2.0/7）— PER14.65倍・PEG30.855・52週61.7% ／ 💰単元36.2万円
  > 【戦略】当日終値3625円の指値で反転を取りにいく。SL3515円（直近5日安値）
- 6349 Komori Corporation｜choruko_reversal｜⚠減速(0)｜🟡やや割高(2.0)｜PASS｜1741｜💰17.4万｜指値1741 SL1673｜⚠日程不明 ⚠業績基調が下向き（⚠減速） 📐進捗 上振れ 24.1%
  > 【業態】印刷機専業トップ。枚葉機、紙幣印刷機に強み。欧米に輸出、中国は中古も。
  > 【いま】終値1,741円・直近5日+5.32%（材料未確認）
  > 【調子】⚠減速（0/13） — 経常減益-14.2%・質注意・🔼進捗先行
  > 【水準】🟡やや割高（2.0/7）— PER12.54倍・PEG—・52週51.8% ／ 💰単元17.4万円
  > 【戦略】当日終値1741円の指値で反転を取りにいく。SL1673円（直近5日安値）
- 3612 WORLD CO.,LTD.｜choruko_reversal｜業績データ取得不可(経常益予想非開示)(None)｜💎割安(7.0)｜FAIL_INSEN｜1493｜💰15.0万｜—
- 8975 Ichigo Office REIT Investment Corporation｜choruko_reversal｜判定保留(変則決算)(None)｜💎割安(7.0)｜PASS｜87500｜💰8.8万｜指値87500 SL85700
  > 【業態】投資は中規模オフィスビル特化型。価値向上修繕も。運用:いちごグループHD系。
  > 【いま】終値87,500円・直近5日+2.82%（材料未確認）
  > 【調子】判定保留(変則決算)（—/13） — 変則決算・四半期不足
  > 【水準】💎割安（7.0/7）— PER12.00倍・PEG0.059・52週36.3% ／ 💰単元8.8万円
  > 【戦略】当日終値87500円の指値で反転を取りにいく。SL85700円（直近5日安値）
- 8253 Credit Saison Co., Ltd.｜choruko_reversal｜取得不可(None)｜💎割安(6.0)｜FAIL_UWAHIGE｜4157｜💰41.9万｜—｜⚡材料後出し
- 7381 ＣＣＩグループ｜choruko_reversal｜業績データ取得不可(売上/経常欠損)(None)｜🟢値頃(5.6)｜FAIL_INSEN｜1117｜💰11.5万｜—
- 5831 Shizuoka Financial Group, Inc.｜choruko_reversal｜業績データ取得不可(売上/経常欠損)(None)｜🟢値頃(5.0)｜FAIL_UWAHIGE｜3232｜💰31.8万｜—
- 6810 Maxell, Ltd.｜choruko_reversal｜業績データ取得不可(経常益予想非開示)(None)｜🟢値頃(5.0)｜FAIL_INSEN｜2188｜💰22.1万｜—
- 7167 めぶきフィナンシャルグループ｜choruko_reversal｜取得不可(None)｜🟢値頃(5.0)｜FAIL_INSEN｜1513｜💰15.2万｜—
- 7186 横浜フィナンシャルグループ｜choruko_reversal｜取得不可(None)｜🟢値頃(5.0)｜FAIL_INSEN｜1747.5｜💰17.7万｜—
- 8345 Bank of Iwate Ltd.｜choruko_reversal｜業績データ取得不可(売上/経常欠損)(None)｜🟢値頃(5.0)｜FAIL_INSEN｜2047｜💰21.3万｜—
- 8359 Hachijuni Nagano Bank, Ltd.｜choruko_reversal｜業績データ取得不可(売上/経常欠損)(None)｜🟢値頃(5.0)｜FAIL_INSEN｜2483.5｜💰25.4万｜—
- 8370 紀陽銀行｜choruko_reversal｜業績データ取得不可(売上/経常欠損)(None)｜🟢値頃(5.0)｜FAIL_INSEN｜1527｜💰15.4万｜—
- 4293 セプテーニ・ホールディングス（セプテニＨＤ）｜choruko_reversal｜業績データ取得不可(経常益予想非開示)(None)｜⚪妥当(4.0)｜FAIL_INSEN｜471｜💰4.7万｜—｜⚡材料後出し
- 7384 Procrea Holdings,Inc.｜choruko_reversal｜業績データ取得不可(売上/経常欠損)(None)｜⚪妥当(4.0)｜FAIL_INSEN｜3955｜💰41.3万｜—｜⚡材料後出し
- 8304 あおぞら銀行｜choruko_reversal｜取得不可(None)｜⚪妥当(4.0)｜FAIL_INSEN｜3200｜💰31.8万｜—
- 8334 Gunma Bank, Ltd.｜choruko_reversal｜業績データ取得不可(売上/経常欠損)(None)｜⚪妥当(4.0)｜FAIL_INSEN｜2528｜💰26.3万｜—
- 8354 ふくおかフィナンシャルグループ｜choruko_reversal｜業績データ取得不可(売上/経常欠損)(None)｜⚪妥当(4.0)｜FAIL_INSEN｜7193｜💰72.4万｜—
- 8366 滋賀銀行｜choruko_reversal｜取得不可(None)｜⚪妥当(4.0)｜FAIL_INSEN｜2310.5｜💰23.7万｜—｜⚡材料後出し
- 8399 琉球銀行｜choruko_reversal｜取得不可(None)｜⚪妥当(4.0)｜FAIL_INSEN｜2660｜💰27.0万｜—
- 3591 WACOAL HOLDINGS CORP｜choruko_reversal｜🔻悪化(None)｜🟡やや割高(2.0)｜FAIL_UWAHIGE｜3999｜💰36.6万｜—｜⚡材料後出し
- 4768 OTSUKA CORPORATION｜choruko_reversal｜業績—｜－未評価｜PASS｜3746｜💰—｜指値3746 SL3603｜⚠日程不明
  > 【業態】独立系SI大手。開発から保守まで一貫。中小に強み。事務用品の販売も。
  > 【いま】終値3,746円・直近5日+4.52%（材料未確認）
  > 【調子】—（—/13）
  > 【水準】－未評価（次回①-9で算定）（—/7）— PER—倍・PEG—・52週—% ／ 💰単元—万円
  > 【戦略】当日終値3746円の指値で反転を取りにいく。SL3603円（直近5日安値）
- 5019 出光興産｜choruko_reversal｜取得不可(None)｜⏸判定不能(None)｜FAIL_INSEN｜1295｜💰13.2万｜—
- 7177 ＧＭＯフィナンシャルホールディングス｜choruko_reversal｜取得不可(None)｜⏸判定不能(None)｜FAIL_UWAHIGE｜1079｜💰10.6万｜—
- 7322 三十三フィナンシャルグループ｜choruko_reversal｜業績データ取得不可(None)｜⏸判定不能(None)｜FAIL_INSEN｜1813｜💰18.6万｜—｜⚡材料後出し
- 8032 紙パル商｜choruko_reversal｜業績—｜－未評価｜FAIL_INSEN｜1127｜💰—｜—
- 8600 トモニホールディングス｜choruko_reversal｜業績データ取得不可(None)｜⏸判定不能(None)｜FAIL_INSEN｜1021｜💰10.3万｜—
- 8616 Tokai Tokyo Financial Holdings, Inc.｜choruko_reversal｜業績データ取得不可(None)｜⏸判定不能(None)｜FAIL_UWAHIGE｜782｜💰7.8万｜—
- 8698 Monex Group, Inc.｜choruko_reversal｜業績データ取得不可(経常益予想非開示)(None)｜⏸判定不能(None)｜FAIL_UWAHIGE｜597｜💰6.0万｜—
- 4410 ハリマ化成グループ（ハリマ化成Ｇ）｜stf_kakuhen｜🔥絶好調(10)｜🟢値頃(5.0)｜FAIL_INSEN｜1377｜💰14.2万｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 6668 ＡＤプラズマ｜stf_kakuhen｜🔥絶好調(10)｜🟢値頃(5.0)｜FAIL_INSEN｜3945｜💰39.6万｜—
- 5832 ちゅうぎんフィナンシャルグループ（ちゅうぎんＦ）｜stf_kakuhen｜🔥絶好調(10)｜⚪妥当(4.2)｜FAIL_INSEN｜3573｜💰35.8万｜—
- 5018 ＭＯＲＥＳＣＯ｜stf_kakuhen｜🔥絶好調(10)｜⚪妥当(4.0)｜FAIL_INSEN｜2801｜💰28.7万｜—
- 5246 ＥＬＥＭＥＮＴＳ｜stf_kakuhen｜🔥絶好調(10)｜⚪妥当(4.0)｜FAIL_UWAHIGE｜928｜💰9.9万｜—
- 7942 ＪＳＰ｜stf_kakuhen｜🔥絶好調(10)｜⚪妥当(4.0)｜PASS｜3175｜💰31.8万｜⛔提案なし(手法ブランチ不明)｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8） 📐進捗 上振れ 61.9%
  > 【業態】三菱ガス化系。発泡樹脂大手。バンパーや住宅断熱材、食品・包装材なども。
  > 【いま】終値3,175円・直近5日+7.23%（材料未確認）
  > 【調子】🔥絶好調（10/13） — 上方修正済み・🔼加速・🔼進捗先行
  > 【水準】⚪妥当（4.0/7）— PER9.79倍・PEG0.220・52週94.5% ／ 💰単元31.8万円
  > 【戦略】発注対象外（⛔提案なし(手法ブランチ不明)）
- 9962 ミスミグループ本社｜stf_kakuhen｜🔥絶好調(10)｜⚪妥当(3.0)｜FAIL_INSEN｜3966｜💰42.7万｜—
- 3498 霞ヶ関Ｃ｜stf_kakuhen｜🔥絶好調(9)｜💎割安(6.0)｜FAIL_INSEN｜7150｜💰74.9万｜—
- 9110 ＮＳユナイテッド海運（ユナイテド海）｜stf_kakuhen｜🔥絶好調(9)｜⚪妥当(4.0)｜FAIL_INSEN｜10540｜💰105.4万｜—
- 3994 マネーフォワード｜stf_kakuhen｜🔥絶好調(9)｜🔴過熱(1.4)｜FAIL_UWAHIGE｜7460｜💰78.6万｜—
- 9766 コナミグループ（コナミＧ）｜stf_kakuhen｜🔥絶好調(8)｜🟡やや割高(2.0)｜FAIL_UWAHIGE｜29180｜💰286.5万｜—
- 4503 アステラス製薬（アステラス）｜stf_kakuhen｜⚡好調(7)｜⚪妥当(4.0)｜FAIL_UWAHIGE｜2699｜💰26.3万｜—
- 6758 ソニーグループ｜stf_kakuhen｜⚡好調(7)｜⚪妥当(3.0)｜PASS｜4353｜💰43.5万｜⛔提案なし(材料後出し)｜⚠日程不明 ⚡材料後出し
  > 【業態】AV機器世界大手。映画、ゲーム、音楽を展開。画像センサー等デバイス事業拡大。
  > 【いま】終値4,353円・直近5日+5.09%・📌Disposal of Treasury Shares upon Vesting of Restricted Stock Units (“RSUs”)
  > 【調子】⚡好調（7/13）
  > 【水準】⚪妥当（3.0/7）— PER19.07倍・PEG0.620・52週75.6% ／ 💰単元43.5万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 3091 ブロンコビリー｜stf_kakuhen｜⚡好調(7)｜🟡やや割高(2.0)｜PASS｜3105｜💰31.1万｜⛔提案なし(手法ブランチ不明)｜⚠日程不明
  > 【業態】名古屋地盤に高級ステーキ店チェーン展開。炭焼き等、高付加価値提供。関東進出。
  > 【いま】終値3,105円・直近5日+6.34%（材料未確認）
  > 【調子】⚡好調（7/13） — E軸:進捗76.4%>=前年同期70.5%
  > 【水準】🟡やや割高（2.0/7）— PER35.57倍・PEG1.081・52週83.6% ／ 💰単元31.1万円
  > 【戦略】発注対象外（⛔提案なし(手法ブランチ不明)）
- 3479 ＴＫＰ｜stf_kakuhen｜⚡好調(6)｜🔴過熱(1.0)｜FAIL_UWAHIGE｜2124｜💰21.4万｜—
- 4417 グローバルセキュリティエキスパート（Ｇセキュリ）｜stf_kakuhen｜⚡好調(6)｜🔴過熱(1.0)｜FAIL_INSEN｜8470｜💰84.8万｜—
- 6505 東洋電機製造｜stf_kakuhen｜⚡好調(5)｜⚪妥当(4.0)｜PASS｜3030｜💰30.3万｜⛔提案なし(材料後出し)｜⚠日程不明 ⚡材料後出し
  > 【業態】駆動装置など鉄道車両用電機品の大手。モーター、インバータで自動車開発支援も。
  > 【いま】終値3,030円・直近5日+4.92%・📌コーポレート・ガバナンスに関する報告書 2026/11/13
  > 【調子】⚡好調（5/13） — E軸判定不能(進捗データ不足)
  > 【水準】⚪妥当（4.0/7）— PER9.40倍・PEG0.689・52週87.6% ／ 💰単元30.3万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 6532 ベイカレント｜stf_kakuhen｜⚡好調(5)｜🟡やや割高(2.0)｜PASS｜12325｜💰123.2万｜⛔提案なし(手法ブランチ不明)｜⚠日程不明
  > 【業態】ITコンサルで創業。企業戦略立案・課題解決・実行まで専門提供の総合コンサル。
  > 【いま】終値12,325円・直近5日+5.03%（材料未確認）
  > 【調子】⚡好調（5/13） — E軸判定不能(進捗データ不足)・D軸判定不能(四半期データ不足・中立1点)
  > 【水準】🟡やや割高（2.0/7）— PER37.66倍・PEG1.380・52週94.8% ／ 💰単元123.2万円
  > 【戦略】発注対象外（⛔提案なし(手法ブランチ不明)）
- 4176 ココナラ｜stf_kakuhen｜✅順調(4)｜💎割安(6.0)｜FAIL_UWAHIGE｜273｜💰2.8万｜—
- 7366 ＬＩＴＡＬＩＣＯ（りたりこ）｜stf_kakuhen｜業績データ取得不可(経常益予想非開示)(None)｜⚪妥当(3.0)｜FAIL_UWAHIGE｜2063｜💰20.7万｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 9048 名古屋鉄道｜value_gap｜⚡好調(5)｜⚪妥当(4.0)｜PASS｜2030｜💰20.3万｜逆指値2030.5 SL1908.2｜⚠日程不明 🤷熟成
  > 【業態】中部最大の私鉄でグループの中核。不動産やホテル、レジャー施設など多角展開。
  > 【いま】終値2,030円・直近5日+6.59%（材料未確認）
  > 【調子】⚡好調（5/13） — E軸判定不能(進捗データ不足)
  > 【水準】⚪妥当（4.0/7）— PER10.21倍・PEG0.454・52週100.0% ／ 💰単元20.3万円
  > 【戦略】当日高値超えの逆指値2030.5円で順張り参戦を検討。上限2050.8円・SL1908.2円目安

## グランビル銘柄
- 5254 Arent, Inc.｜granville_tenkan｜🚀確変(12)｜⚪妥当(4.0)｜FAIL_INSEN｜3835｜💰39.2万｜—｜⚡材料後出し
- 3927 アークン｜granville_tenkan｜🚀確変(11)｜💎割安(6.0)｜FAIL_INSEN｜837｜💰9.3万｜—
- 6768 Tamura Corporation｜granville_tenkan｜🔥絶好調(10)｜💎割安(6.0)｜FAIL_INSEN｜707｜💰7.3万｜—｜⚡材料後出し
- 8944 Land Business Co., Ltd.｜granville_tenkan｜🔥絶好調(10)｜💎割安(6.0)｜FAIL_INSEN｜238｜💰2.5万｜—｜⚡材料後出し
- 7725 INTER ACTION Corporation｜granville_tenkan｜🔥絶好調(10)｜🟢値頃(5.0)｜FAIL_UWAHIGE｜1681｜💰17.4万｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 3491 ＧＡ　ｔｅｃｈｎｏｌｏｇｉｅｓ（ＧＡテクノ）｜granville_tenkan｜🔥絶好調(8)｜💎割安(6.0)｜FAIL_UWAHIGE｜1466｜💰15.6万｜—
- 6470 Taiho Kogyo Co., Ltd.｜granville_tenkan｜🔥絶好調(8)｜💎割安(6.0)｜FAIL_UWAHIGE｜909｜💰9.2万｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 6744 能美防災｜granville_tenkan｜🔥絶好調(8)｜🟢値頃(5.0)｜FAIL_INSEN｜4520｜💰45.0万｜—
- 8012 Nagase & Co., Ltd.｜granville_tenkan｜🔥絶好調(8)｜🟢値頃(5.0)｜FAIL_INSEN｜1206.5｜💰12.1万｜—
- 2502 Asahi Group Holdings, Ltd.｜granville_tenkan｜🔥絶好調(8)｜⚪妥当(4.0)｜FAIL_UWAHIGE｜1805｜💰17.5万｜—
- 3002 グンゼ｜granville_tenkan｜🔥絶好調(8)｜⚪妥当(4.0)｜FAIL_UWAHIGE｜4390｜💰43.7万｜—
- 4523 エーザイ｜granville_tenkan｜🔥絶好調(8)｜⚪妥当(3.0)｜FAIL_UWAHIGE｜5186｜💰51.7万｜—
- 8697 日本取引所グループ｜granville_tenkan｜🔥絶好調(8)｜⚪妥当(3.0)｜FAIL_INSEN｜2216.5｜💰22.0万｜—
- 9742 アイネス｜granville_tenkan｜🔥絶好調(8)｜⚪妥当(3.0)｜FAIL_UWAHIGE｜2404｜💰23.9万｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 3964 オークネット｜granville_tenkan｜⚡好調(7)｜💎割安(6.0)｜FAIL_INSEN｜1280｜💰13.3万｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 4005 住友化学｜granville_tenkan｜⚡好調(7)｜💎割安(6.0)｜FAIL_INSEN｜512｜💰5.1万｜—
- 3405 クラレ｜granville_tenkan｜⚡好調(7)｜🟢値頃(5.0)｜PASS｜1915.5｜💰19.2万｜逆指値1917.5 SL1802｜📐進捗 上振れ 24.8%
  > 【業態】化学品大手。高分子機能素材・フィルムに強み。樹脂の世界トップ製品多数。
  > 【いま】終値1,916円・直近5日+3.99%（材料未確認）
  > 【調子】⚡好調（7/13） — 上方修正済み・🔼進捗先行
  > 【水準】🟢値頃（5.0/7）— PER14.42倍・PEG0.595・52週71.1% ／ 💰単元19.2万円
  > 【戦略】当日高値超えの逆指値1917.5円で順張り参戦を検討。上限1936.7円・SL1802円目安
- 3496 アズーム｜granville_tenkan｜⚡好調(7)｜🟢値頃(5.0)｜PASS_DOJI｜4070｜💰40.7万｜⛔提案なし(材料後出し)｜📉決算反応日 11/13 ⚡材料後出し 📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】ビル駐車場のサブリースを展開。月極駐車場ポータルサイト「CarParking」運営も。
  > 【いま】終値4,070円・直近5日-17.53%・📌（訂正）「2026年９月期決算説明資料」の一部訂正について
  > 【調子】⚡好調（7/13）
  > 【水準】🟢値頃（5.0/7）— PER22.81倍・PEG1.116・52週6.7% ／ 💰単元40.7万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 4401 ＡＤＥＫＡ｜granville_tenkan｜⚡好調(7)｜🟢値頃(5.0)｜FAIL_INSEN｜4383｜💰44.1万｜—
- 4534 Mochida Pharmaceutical Co., Ltd.｜granville_tenkan｜⚡好調(7)｜🟢値頃(5.0)｜FAIL_UWAHIGE｜3355｜💰32.6万｜—
- 7744 ノーリツ鋼機｜granville_tenkan｜⚡好調(7)｜⚪妥当(4.0)｜FAIL_INSEN｜2047｜💰20.7万｜—｜⚡材料後出し
- 9006 Keikyu Corporation｜granville_tenkan｜⚡好調(7)｜⚪妥当(4.0)｜PASS｜1630｜💰16.3万｜逆指値1630.5 SL1532.2｜📐進捗 遅れ -20.6%
  > 【業態】京浜・三浦半島が地盤。品川・羽田・横浜を核に沿線再開発を推進。
  > 【いま】終値1,630円・直近5日+4.25%（材料未確認）
  > 【調子】⚡好調（7/13） — ⚠進捗遅れ・⚠下期依存
  > 【水準】⚪妥当（4.0/7）— PER14.05倍・PEG0.268・52週84.6% ／ 💰単元16.3万円
  > 【戦略】当日高値超えの逆指値1630.5円で順張り参戦を検討。上限1646.8円・SL1532.2円目安
- 9075 福山通運｜granville_tenkan｜⚡好調(7)｜⚪妥当(4.0)｜FAIL_INSEN｜6380｜💰64.0万｜—
- 5532 リアルゲイト｜granville_tenkan｜⚡好調(7)｜⚪妥当(3.0)｜FAIL_INSEN｜3300｜💰34.0万｜—
- 7970 Shin-Etsu Polymer Co., Ltd.｜granville_tenkan｜⚡好調(7)｜⚪妥当(3.0)｜FAIL_INSEN｜2432｜💰24.4万｜—
- 4507 塩野義製薬｜granville_tenkan｜⚡好調(7)｜🟡やや割高(2.0)｜FAIL_UWAHIGE｜3172｜💰31.4万｜—
- 1941 中電工｜granville_tenkan｜⚡好調(6)｜🟢値頃(5.0)｜PASS｜5220｜💰52.2万｜逆指値5240 SL4916.2｜⚠日程不明 ⚠1単元でリスク枠超過（32380円）
  > 【業態】中国電力系で依存度約3割。電気工事主体。総資産の投資有価証券が大。
  > 【いま】終値5,220円・直近5日+6.64%（材料未確認）
  > 【調子】⚡好調（6/13） — ⚠減速
  > 【水準】🟢値頃（5.0/7）— PER12.12倍・PEG0.488・52週67.5% ／ 💰単元52.2万円
  > 【戦略】当日高値超えの逆指値5240円で順張り参戦を検討。上限5292.4円・SL4916.2円目安／⚠1単元リスク32380円（枠超過）
- 8061 Seika Corporation｜granville_tenkan｜⚡好調(6)｜🟢値頃(5.0)｜FAIL_INSEN｜2753｜💰28.7万｜—
- 4848 Fullcast Holdings Co., Ltd.｜granville_tenkan｜⚡好調(6)｜⚪妥当(3.0)｜PASS｜1851｜💰18.5万｜逆指値1858 SL1745.6｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】日雇い派遣からアルバイト紹介・給与管理代行に転換。警備請負、ラーメンチェーンも。
  > 【いま】終値1,851円・直近5日+2.04%（材料未確認）
  > 【調子】⚡好調（6/13） — 質注意
  > 【水準】⚪妥当（3.0/7）— PER11.77倍・PEG0.914・52週80.8% ／ 💰単元18.5万円
  > 【戦略】当日高値超えの逆指値1858円で順張り参戦を検討。上限1876.6円・SL1745.6円目安
- 4045 Toagosei Co., Ltd.｜granville_tenkan｜⚡好調(6)｜🟡やや割高(2.0)｜FAIL_UWAHIGE｜1803.5｜💰17.9万｜—
- 6099 エラン｜granville_tenkan｜⚡好調(6)｜🟡やや割高(2.0)｜FAIL_INSEN｜778｜💰7.8万｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 3935 Edia Co. Ltd.｜granville_tenkan｜⚡好調(5)｜💎割安(7.0)｜FAIL_UWAHIGE｜665｜💰6.6万｜—
- 4554 Fuji Pharma Co., Ltd.｜granville_tenkan｜⚡好調(5)｜🟢値頃(5.0)｜FAIL_INSEN｜1857｜💰18.8万｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 4617 中国塗料｜granville_tenkan｜⚡好調(5)｜🟢値頃(5.0)｜FAIL_INSEN｜3435｜💰35.7万｜—
- 9842 アークランズ｜granville_tenkan｜⚡好調(5)｜🟢値頃(5.0)｜PASS｜1935｜💰19.4万｜⛔提案なし(指名鮮度切れ 11営業日)｜⚠日程不明
  > 【業態】新潟地盤でDIY中心の巨艦店「ムサシ」展開。傘下で外食。ジョイフル本田と統合へ。
  > 【いま】終値1,935円・直近5日+2.22%（材料未確認）
  > 【調子】⚡好調（5/13）
  > 【水準】🟢値頃（5.0/7）— PER12.15倍・PEG0.415・52週62.2% ／ 💰単元19.4万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 11営業日)）
- 8016 オンワード HD｜granville_tenkan｜⚡好調(5)｜⚪妥当(4.0)｜PASS｜794｜💰7.9万｜逆指値796 SL747.3｜⚠日程不明
  > 【業態】総合アパレル最大手。百貨店中心「23区」「組曲」等。EC販積極。ウェルネス関連も。
  > 【いま】終値794円・直近5日+3.93%（材料未確認）
  > 【調子】⚡好調（5/13）
  > 【水準】⚪妥当（4.0/7）— PER9.66倍・PEG0.960・52週74.7% ／ 💰単元7.9万円
  > 【戦略】当日高値超えの逆指値796円で順張り参戦を検討。上限804円・SL747.3円目安
- 8804 東京建物｜granville_tenkan｜⚡好調(5)｜⚪妥当(4.0)｜FAIL_INSEN｜3395｜💰34.1万｜—
- 2206 江崎グリコ｜granville_tenkan｜⚡好調(5)｜⚪妥当(3.0)｜PASS｜5117｜💰51.2万｜逆指値5122 SL4813.7（⏸位置不適(52週 26.9%)）｜📐進捗 遅れ -23.3% ⚠1単元でリスク枠超過（30830円）
  > 【業態】菓子大手。冷菓やチョコレート、スナックが主体。乳製品、カレーなども。栄養食品が拡大。
  > 【いま】終値5,117円・直近5日+1.77%（材料未確認）
  > 【調子】⚡好調（5/13） — ⚠減速・⚠進捗遅れ
  > 【水準】⚪妥当（3.0/7）— PER33.58倍・PEG1.660・52週26.9% ／ 💰単元51.2万円
  > 【戦略】当日高値超えの逆指値5122円で順張り参戦を検討。上限5173.2円・SL4813.7円目安（⏸位置不適(52週 26.9%)）／⚠1単元リスク30830円（枠超過）
- 4403 日油｜granville_tenkan｜⚡好調(5)｜⚪妥当(3.0)｜FAIL_INSEN｜2568.5｜💰25.4万｜—
- 7606 ＴＡＢＡＹＡホールディングス｜granville_tenkan｜⚡好調(5)｜⚪妥当(3.0)｜PASS｜2667｜💰26.7万｜逆指値2668 SL2507｜📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】セレクトショップ大手。婦人服・服飾や紳士服、雑貨を販売。「ユナイテッドアローズ」主力。
  > 【いま】終値2,667円・直近5日+9.80%（材料未確認）
  > 【調子】⚡好調（5/13） — 上方修正済み・⚠減速
  > 【水準】⚪妥当（3.0/7）— PER11.60倍・PEG1.403・52週87.3% ／ 💰単元26.7万円
  > 【戦略】当日高値超えの逆指値2668円で順張り参戦を検討。上限2694.7円・SL2507円目安
- 7747 朝日インテック｜granville_tenkan｜⚡好調(5)｜🔴過熱(1.0)｜FAIL_INSEN｜3811｜💰38.6万｜—｜⚡材料後出し
- 4169 Enechange Ltd.｜granville_tenkan｜⚠減速(4)｜⚪妥当(4.0)｜FAIL_UWAHIGE｜287｜💰2.8万｜—
- 4568 第一三共｜granville_tenkan｜✅順調(4)｜⚪妥当(4.0)｜FAIL_UWAHIGE｜2852.5｜💰28.6万｜—
- 6412 Heiwa Holdings Inc.｜granville_tenkan｜✅順調(4)｜⚪妥当(4.0)｜PASS｜2104｜💰21.0万｜逆指値2105 SL1977.8｜⚠日程不明
  > 【業態】パチンコ、パチスロ機大手。開発力に定評。傘下にゴルフ場運営のアコーディア、PGM。
  > 【いま】終値2,104円・直近5日-0.09%（材料未確認）
  > 【調子】✅順調（4/13）
  > 【水準】⚪妥当（4.0/7）— PER10.22倍・PEG0.829・52週69.8% ／ 💰単元21.0万円
  > 【戦略】当日高値超えの逆指値2105円で順張り参戦を検討。上限2126.1円・SL1977.8円目安
- 1911 Sumitomo Forestry Co., Ltd.｜granville_tenkan｜🔻悪化(4)｜⚪妥当(3.0)｜PASS｜1271｜💰12.7万｜逆指値1278.5 SL1201.3（⏸位置不適(52週 16.1%)）｜⚠日程不明 ⚠業績基調が下向き（🔻悪化）
  > 【業態】木造軸組工法に定評、住宅大手。住宅建材、リフォーム、都市開発も。海外堅調。
  > 【いま】終値1,271円・直近5日+2.13%（材料未確認）
  > 【調子】🔻悪化（4/13） — E軸判定不能(進捗データ不足)・経常減益-34.2%・質注意
  > 【水準】⚪妥当（3.0/7）— PER12.98倍・PEG—・52週16.1% ／ 💰単元12.7万円
  > 【戦略】当日高値超えの逆指値1278.5円で順張り参戦を検討。上限1291.3円・SL1201.3円目安（⏸位置不適(52週 16.1%)）
- 2488 ＪＴＰ｜granville_tenkan｜✅順調(4)｜🟡やや割高(2.0)｜FAIL_INSEN｜1394｜💰13.9万｜—
- 417A ブルーゾーンホールディングス｜granville_tenkan｜✅順調(4)｜🟡やや割高(2.0)｜PASS｜1948.5｜💰19.5万｜逆指値1950 SL1832.5｜⚠日程不明
  > 【業態】埼玉地盤の食品スーパー中堅。提案型売り場作りに定評。持株会社に移行。
  > 【いま】終値1,948円・直近5日+0.52%（材料未確認）
  > 【調子】✅順調（4/13） — 質注意
  > 【水準】🟡やや割高（2.0/7）— PER16.47倍・PEG9.445・52週76.3% ／ 💰単元19.5万円
  > 【戦略】当日高値超えの逆指値1950円で順張り参戦を検討。上限1969.5円・SL1832.5円目安
- 4549 Eiken Chemical Co., Ltd.｜granville_tenkan｜✅順調(4)｜🟡やや割高(2.0)｜PASS｜2250｜💰22.5万｜⛔提案なし(指名鮮度切れ 17営業日)｜⚠日程不明
  > 【業態】臨床検査薬大手。便潜血試薬で高シェア。微生物、遺伝子、尿検査なども。
  > 【いま】終値2,250円・直近5日+3.54%（材料未確認）
  > 【調子】✅順調（4/13）
  > 【水準】🟡やや割高（2.0/7）— PER35.94倍・PEG18.254・52週15.5% ／ 💰単元22.5万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 17営業日)）
- 5184 ニチリン｜granville_tenkan｜✅順調(4)｜🟡やや割高(2.0)｜FAIL_INSEN｜4170｜💰41.5万｜—
- 7269 スズキ｜granville_tenkan｜✅順調(4)｜🟡やや割高(2.0)｜FAIL_INSEN｜2168.5｜💰22.0万｜—
- 9418 Ｕ－ＮＥＸＴ　ＨＯＬＤＩＮＧＳ｜granville_tenkan｜✅順調(4)｜🟡やや割高(2.0)｜PASS｜1882｜💰18.8万｜逆指値1883 SL1769.1｜⚠日程不明
  > 【業態】持ち株会社。店舗向け音楽・動画有料配信が主力。施設ソルーション、電力小売も。
  > 【いま】終値1,882円・直近5日+5.61%（材料未確認）
  > 【調子】✅順調（4/13） — E軸判定不能(期首・進捗なし)・🔼加速
  > 【水準】🟡やや割高（2.0/7）— PER20.57倍・PEG2.289・52週58.2% ／ 💰単元18.8万円
  > 【戦略】当日高値超えの逆指値1883円で順張り参戦を検討。上限1901.8円・SL1769.1円目安
- 3092 ＺＯＺＯ｜granville_tenkan｜✅順調(4)｜🔴過熱(1.0)｜PASS｜1175.5｜💰11.8万｜逆指値1177.5 SL1106.4（⏸位置不適(25MA下 -0.63%)）｜⚠日程不明
  > 【業態】LINEヤフー傘下。衣料品通販サイト「ZOZOTOWN」を運営。ブランド品を受託販売。
  > 【いま】終値1,176円・直近5日+3.39%（材料未確認）
  > 【調子】✅順調（4/13）
  > 【水準】🔴過熱（1.0/7）— PER20.51倍・PEG2.765・52週51.3% ／ 💰単元11.8万円
  > 【戦略】当日高値超えの逆指値1177.5円で順張り参戦を検討。上限1189.3円・SL1106.4円目安（⏸位置不適(25MA下 -0.63%)）
- 3549 クスリのアオキホールディングス｜granville_tenkan｜✅順調(4)｜🔴過熱(1.0)｜FAIL_INSEN｜5073｜💰50.8万｜—
- 6592 Mabuchi Motor Co., Ltd.｜granville_tenkan｜✅順調(4)｜🔴過熱(1.0)｜FAIL_UWAHIGE｜1827.5｜💰18.0万｜—
- 8113 Unicharm Corporation｜granville_tenkan｜✅順調(4)｜🔴過熱(0.0)｜PASS｜1120｜💰11.2万｜逆指値1120.5 SL1052.8
  > 【業態】衛生用品大手。生理用品、紙おむつで首位。ペットケア用品も。アジアに強み。
  > 【いま】終値1,120円・直近5日+7.02%（材料未確認）
  > 【調子】✅順調（4/13） — 税引前代替
  > 【水準】🔴過熱（0.0/7）— PER27.52倍・PEG3.574・52週100.0% ／ 💰単元11.2万円
  > 【戦略】当日高値超えの逆指値1120.5円で順張り参戦を検討。上限1131.7円・SL1052.8円目安
- 8160 KISOJI CO., LTD.｜granville_tenkan｜✅順調(4)｜🔴過熱(0.0)｜PASS｜2542｜💰25.4万｜逆指値2546 SL2392.3｜⚠日程不明
  > 【業態】外食中堅。しゃぶしゃぶ「木曽路」は業界最大手。焼肉・居酒屋なども経営。
  > 【いま】終値2,542円・直近5日+3.63%（材料未確認）
  > 【調子】✅順調（4/13） — ⚠減速・⚠進捗遅れ
  > 【水準】🔴過熱（0.0/7）— PER34.08倍・PEG3.109・52週78.9% ／ 💰単元25.4万円
  > 【戦略】当日高値超えの逆指値2546円で順張り参戦を検討。上限2571.5円・SL2392.3円目安
- 4166 Cacco, Inc.｜granville_tenkan｜✅順調(3)｜💎割安(7.0)｜PASS｜667｜💰6.7万｜⛔提案なし(指名鮮度切れ 17営業日)｜📉決算反応日 11/16 ⚡材料後出し
  > 【業態】EC市場の不正検知サービスや決済コンサルサービスを提供。データサイエンス技術に強み。
  > 【いま】終値667円・直近5日+5.87%・📊2026年12月期 第３四半期 決算短信〔日本基準〕（連結）
  > 【調子】✅順調（3/13） — E軸判定不能(進捗データ不足)・C軸判定不能(四半期営業益不足)・赤字企業(経常赤字)・D軸判定不能(四半期データ不足・中立1点)
  > 【水準】💎割安（7.0/7）— PER—倍・PEG—・52週7.6% ／ 💰単元6.7万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 17営業日)）
- 9163 Nareru Group Inc.｜granville_tenkan｜✅順調(3)｜🟢値頃(5.0)｜FAIL_INSEN｜2054｜💰20.5万｜—
- 8056 ＢＩＰＲＯＧＹ｜granville_tenkan｜✅順調(3)｜⚪妥当(4.0)｜PASS｜4880｜💰48.8万｜逆指値4881 SL4587.2（⏸位置不適(25MA下 -0.13%)）｜⚠日程不明 📐進捗 遅れ -25.7%
  > 【業態】大日本印刷系の情報システム大手。クラウド事業に注力。金融、流通、空運に強み。
  > 【いま】終値4,880円・直近5日+12.52%（材料未確認）
  > 【調子】✅順調（3/13） — ⚠進捗遅れ
  > 【水準】⚪妥当（4.0/7）— PER14.65倍・PEG1.545・52週39.0% ／ 💰単元48.8万円
  > 【戦略】当日高値超えの逆指値4881円で順張り参戦を検討。上限4929.8円・SL4587.2円目安（⏸位置不適(25MA下 -0.13%)）
- 9956 Valor Holdings Co., Ltd.｜granville_tenkan｜✅順調(3)｜⚪妥当(4.0)｜PASS｜1627｜💰16.3万｜逆指値1636.5 SL1537.8（⏸位置不適(25MA下 -0.95%／52週 29.0%)）
  > 【業態】中部地盤の食品スーパー中堅。ドラッグストアやホームセンター、スポーツクラブも展開。
  > 【いま】終値1,627円・直近5日-2.40%（材料未確認）
  > 【調子】✅順調（3/13） — 質注意・上方修正済み・⚠減速
  > 【水準】⚪妥当（4.0/7）— PER11.45倍・PEG7.146・52週29.0% ／ 💰単元16.3万円
  > 【戦略】当日高値超えの逆指値1636.5円で順張り参戦を検討。上限1652.9円・SL1537.8円目安（⏸位置不適(25MA下 -0.95%／52週 29.0%)）
- 3563 ＦＯＯＤ　＆　ＬＩＦＥ　ＣＯＭＰＡＮＩＥＳ｜granville_tenkan｜✅順調(3)｜🟡やや割高(2.0)｜PASS｜6085｜💰60.9万｜⛔提案なし(指名鮮度切れ 11営業日)｜⚠日程不明
  > 【業態】「スシロー」ブランドで回転すしチェーン首位。「京樽」を子会社化。韓国・アジアに進出。
  > 【いま】終値6,085円・直近5日+19.50%（材料未確認）
  > 【調子】✅順調（3/13） — 税引前代替・経常非開示(IFRS等)のため最終益成長率で代替・E軸判定不能(期首・進捗なし)・⚠減速
  > 【水準】🟡やや割高（2.0/7）— PER35.46倍・PEG—・52週98.3% ／ 💰単元60.9万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 11営業日)）
- 4540 Tsumura & Co.｜granville_tenkan｜✅順調(3)｜🟡やや割高(2.0)｜PASS｜3944｜💰39.4万｜逆指値3951 SL3713｜⚠日程不明 📐進捗 上振れ 18.7%
  > 【業態】漢方薬特化で最大手。高齢者、がん患者、婦人処方薬を拡大。中国事業も。
  > 【いま】終値3,944円・直近5日+5.68%（材料未確認）
  > 【調子】✅順調（3/13） — 質注意・経常減益-9.1%・上方修正済み・🔼進捗先行
  > 【水準】🟡やや割高（2.0/7）— PER10.04倍・PEG—・52週48.4% ／ 💰単元39.4万円
  > 【戦略】当日高値超えの逆指値3951円で順張り参戦を検討。上限3990.5円・SL3713円目安
- 7734 Riken Keiki Co., Ltd.｜granville_tenkan｜✅順調(3)｜🟡やや割高(2.0)｜FAIL_UWAHIGE｜3455｜💰33.2万｜—
- 9045 Keihan Holdings Co., Ltd.｜granville_tenkan｜⚠減速(3)｜🟡やや割高(2.0)｜PASS｜3408｜💰34.1万｜逆指値3409 SL3203.5｜⚠業績基調が下向き（⚠減速） 📐進捗 上振れ 18.8%
  > 【業態】大阪京都間が主力の私鉄。京都観光に強み。中之島線沿線の開発に力。
  > 【いま】終値3,408円・直近5日+1.52%（材料未確認）
  > 【調子】⚠減速（3/13） — A成長率0以下のためレバレッジ計算不可(C=0)・質注意・上方修正済み・減収・🔼進捗先行
  > 【水準】🟡やや割高（2.0/7）— PER11.46倍・PEG—・52週66.8% ／ 💰単元34.1万円
  > 【戦略】当日高値超えの逆指値3409円で順張り参戦を検討。上限3443.1円・SL3203.5円目安
- 6745 ホーチキ｜granville_tenkan｜✅順調(3)｜🔴過熱(0.0)｜FAIL_INSEN｜2073｜💰21.7万｜—
- 4902 Konica Minolta, Inc.｜granville_tenkan｜➖横ばい(2)｜🟢値頃(5.2)｜FAIL_UWAHIGE｜581.1｜💰5.7万｜—
- 8801 三井不動産｜granville_tenkan｜➖横ばい(2)｜⚪妥当(3.0)｜PASS｜1623｜💰16.2万｜逆指値1631 SL1532.7（⏸位置不適(52週 29.4%)）｜📐進捗 遅れ -16.9%
  > 【業態】総合不動産、最大手。ビル賃貸が主力。街づくり主体に分譲、ホテル、商施設。
  > 【いま】終値1,623円・直近5日+0.68%（材料未確認）
  > 【調子】➖横ばい（2/13） — 質注意・勢い判定矛盾・⚠進捗遅れ
  > 【水準】⚪妥当（3.0/7）— PER15.33倍・PEG28.565・52週29.4% ／ 💰単元16.2万円
  > 【戦略】当日高値超えの逆指値1631円で順張り参戦を検討。上限1647.3円・SL1532.7円目安（⏸位置不適(52週 29.4%)）
- 5233 太平洋セメント｜granville_tenkan｜🔻悪化(2)｜🟡やや割高(2.0)｜PASS｜4083｜💰40.8万｜逆指値4098 SL3851.2（⏸位置不適(25MA下 -1.78%)）｜⚠日程不明 ⚠業績基調が下向き（🔻悪化） 📐進捗 上振れ 14.1%
  > 【業態】セメント最大手。海外にも展開。建材や電材など多角化。産廃・再資源化も。
  > 【いま】終値4,083円・直近5日-3.61%（材料未確認）
  > 【調子】🔻悪化（2/13） — 質注意・経常減益-26.1%・🔼進捗先行
  > 【水準】🟡やや割高（2.0/7）— PER8.74倍・PEG—・52週48.0% ／ 💰単元40.8万円
  > 【戦略】当日高値超えの逆指値4098円で順張り参戦を検討。上限4139円・SL3851.2円目安（⏸位置不適(25MA下 -1.78%)）
- 8803 Heiwa Real Estate Co., Ltd.｜granville_tenkan｜➖横ばい(2)｜🟡やや割高(2.0)｜PASS｜2365｜💰23.6万｜逆指値2366 SL2223.1｜⚠日程不明
  > 【業態】各地の証券取引所賃貸が収益源。一般賃貸、マンション分譲なども。REIT強化。
  > 【いま】終値2,365円・直近5日+3.14%（材料未確認）
  > 【調子】➖横ばい（2/13） — 質注意・E軸判定不能(進捗率非開示)
  > 【水準】🟡やや割高（2.0/7）— PER13.58倍・PEG88.161・52週52.7% ／ 💰単元23.6万円
  > 【戦略】当日高値超えの逆指値2366円で順張り参戦を検討。上限2389.7円・SL2223.1円目安
- 9837 Morito Co., Ltd.｜granville_tenkan｜➖横ばい(2)｜🟡やや割高(2.0)｜PASS｜1832｜💰18.3万｜⛔提案なし(指名鮮度切れ 15営業日)｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】服飾付属品の商社。金属ホックで世界首位。アパレル向け中心。車内装品も。
  > 【いま】終値1,832円・直近5日+3.68%（材料未確認）
  > 【調子】➖横ばい（2/13） — 質注意・E軸判定不能(進捗データ不足)
  > 【水準】🟡やや割高（2.0/7）— PER14.87倍・PEG3.062・52週42.3% ／ 💰単元18.3万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 15営業日)）
- 4922 コーセーホールディングス｜granville_tenkan｜➖横ばい(2)｜🔴過熱(1.0)｜PASS｜5989｜💰59.9万｜⛔提案なし(材料後出し)｜⚠日程不明 ⚡材料後出し
  > 【業態】化粧品大手。高級化粧品に強み。コスメタリー事業も展開。アジア・米国に進出。
  > 【いま】終値5,989円・直近5日+0.30%・📌Notice of Changes in Executives
  > 【調子】➖横ばい（2/13） — 質注意・経常減益-14.7%
  > 【水準】🔴過熱（1.0/7）— PER32.37倍・PEG—・52週67.9% ／ 💰単元59.9万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 9869 Kato Sangyo Co., Ltd.｜granville_tenkan｜➖横ばい(2)｜🔴過熱(1.0)｜FAIL_INSEN｜6740｜💰66.9万｜—
- 9735 セコム｜granville_tenkan｜➖横ばい(2)｜🔴過熱(0.0)｜PASS｜7117｜💰71.2万｜逆指値7121 SL6692.8｜📐進捗 上振れ 16.0% ⚠1単元でリスク枠超過（42820円）
  > 【業態】警備最大手。賃貸センサー付システム警備が主力。防災、在宅医療など。海外強化。
  > 【いま】終値7,117円・直近5日+6.65%（材料未確認）
  > 【調子】➖横ばい（2/13） — 質注意・🔼加速・🔼進捗先行
  > 【水準】🔴過熱（0.0/7）— PER26.40倍・PEG—・52週94.8% ／ 💰単元71.2万円
  > 【戦略】当日高値超えの逆指値7121円で順張り参戦を検討。上限7192.2円・SL6692.8円目安／⚠1単元リスク42820円（枠超過）
- 6328 Ebara Jitsugyo Co., Ltd.｜granville_tenkan｜⚠減速(1)｜⚪妥当(4.0)｜FAIL_INSEN｜2271｜💰22.9万｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 4912 ライオン｜granville_tenkan｜⚠減速(1)｜⚪妥当(3.0)｜FAIL_UWAHIGE｜2186｜💰21.9万｜—
- 9404 Nippon Television Holdings, Inc.｜granville_tenkan｜🔻悪化(1)｜⚪妥当(3.0)｜PASS｜2971｜💰29.7万｜逆指値2975.5 SL2796.5（⏸位置不適(25MA下 -0.08%／52週 22.5%)）｜⚠日程不明 ⚠業績基調が下向き（🔻悪化）
  > 【業態】読売グループの民放大手。視聴率でトップ争い。動画配信「Hulu」、フィットネスも。
  > 【いま】終値2,971円・直近5日+2.45%（材料未確認）
  > 【調子】🔻悪化（1/13） — 経常減益-28.1%・質注意
  > 【水準】⚪妥当（3.0/7）— PER14.05倍・PEG—・52週22.5% ／ 💰単元29.7万円
  > 【戦略】当日高値超えの逆指値2975.5円で順張り参戦を検討。上限3005.3円・SL2796.5円目安（⏸位置不適(25MA下 -0.08%／52週 22.5%)）
- 1878 Daito Trust Construction Co., Ltd.｜granville_tenkan｜⚠減速(1)｜🟡やや割高(2.0)｜FAIL_INSEN｜3310｜💰33.7万｜—
- 1928 積水ハウス｜granville_tenkan｜⚠減速(1)｜🟡やや割高(2.0)｜PASS｜3617｜💰36.2万｜⛔提案なし(材料後出し)｜📋カルテ窓 12/10(残18営業日) ⚡材料後出し ⚠業績基調が下向き（⚠減速） 📐進捗 上振れ 19.0%
  > 【業態】プレハブ住宅大手。鉄骨主体、木造も注力。賃貸、マンションや都市開発に積極。
  > 【いま】終値3,617円・直近5日+4.09%・📌Notice Concerning Commencement of Tender Offer for Gifu landscape architect Co., Ltd. (Securities Code: 1438)
  > 【調子】⚠減速（1/13） — 質注意・経常減益-3.6%・⚠減速・🔼進捗先行
  > 【水準】🟡やや割高（2.0/7）— PER10.47倍・PEG—・52週67.0% ／ 💰単元36.2万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 4552 JCR Pharmaceuticals Co., Ltd.｜granville_tenkan｜🔻悪化(1)｜🔴過熱(2.0)｜FAIL_UWAHIGE｜499｜💰4.9万｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 5105 ＴＯＹＯ　ＴＩＲＥ｜granville_tenkan｜⚠減速(1)｜🟡やや割高(2.0)｜PASS｜4257｜💰42.6万｜⛔提案なし(指名鮮度切れ 13営業日)｜🚨決算直前 11/16(残1営業日) ⚠業績基調が下向き（⚠減速）
  > 【業態】タイヤ大手。トラック・バス用に強み。北米向けSUV用タイヤも。株主に三菱商事。
  > 【いま】終値4,257円・直近5日+4.77%（材料未確認）
  > 【調子】⚠減速（1/13） — 進捗データ取得不可(判定不能)・(質注意)
  > 【水準】🟡やや割高（2.0/7）— PER8.46倍・PEG—・52週58.2% ／ 💰単元42.6万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 13営業日)）
- 8167 リテールパートナーズ｜granville_tenkan｜⚠減速(1)｜🟡やや割高(2.0)｜FAIL_INSEN｜1378｜💰13.8万｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 2267 Yakult Honsha Co., Ltd.｜granville_tenkan｜⚠減速(1)｜🔴過熱(1.0)｜FAIL_UWAHIGE｜2858.5｜💰28.5万｜—
- 9401 東京放送ホールディングス｜granville_tenkan｜⚠減速(1)｜🔴過熱(1.0)｜PASS｜6295｜💰63.0万｜逆指値6313 SL5933.3｜⚠業績基調が下向き（⚠減速） 📐進捗 遅れ -18.1% ⚠1単元でリスク枠超過（37970円）
  > 【業態】民放キー局の一角。「赤坂サカス」など不動産が収益源。傘下に雑貨店も。
  > 【いま】終値6,295円・直近5日+5.87%（材料未確認）
  > 【調子】⚠減速（1/13） — ⚠減速・⚠進捗遅れ
  > 【水準】🔴過熱（1.0/7）— PER19.75倍・PEG11.770・52週73.1% ／ 💰単元63.0万円
  > 【戦略】当日高値超えの逆指値6313円で順張り参戦を検討。上限6376.1円・SL5933.3円目安／⚠1単元リスク37970円（枠超過）
- 4375 セーフィー｜granville_tenkan｜取得不可(None)｜💎割安(7.0)｜FAIL_UWAHIGE｜626｜💰6.2万｜—｜⚡材料後出し
- 2897 Nissin Foods Holdings Co., Ltd.｜granville_tenkan｜取得不可(None)｜⚪妥当(4.0)｜PASS｜2972.5｜💰29.7万｜逆指値2974.5 SL2795.6（⏸位置不適(25MA下 -1.59%)）
  > 【業態】即席麺のパイオニア。カップ麺でシェア首位。袋麺も強い。国内成熟、海外展開強化。
  > 【いま】終値2,972円・直近5日-2.95%（材料未確認）
  > 【調子】取得不可（—/13） — 税引前代替・業績データ取得不可(経常益予想非開示)
  > 【水準】⚪妥当（4.0/7）— PER18.26倍・PEG—・52週53.9% ／ 💰単元29.7万円
  > 【戦略】当日高値超えの逆指値2974.5円で順張り参戦を検討。上限3004.2円・SL2795.6円目安（⏸位置不適(25MA下 -1.59%)）
- 3182 オイシックス｜granville_tenkan｜業績データ取得不可(経常益予想非開示)(None)｜⚪妥当(4.0)｜PASS｜1866｜💰18.7万｜逆指値1883 SL1769.1｜📉決算反応日 11/13 📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】有機野菜・青果物、加工品をネット販売。移動店舗、直納強化。傘下にシダックス。
  > 【いま】終値1,866円・直近5日+14.13%（材料未確認）
  > 【調子】業績データ取得不可(経常益予想非開示)（—/13） — 業績データ取得不可(経常益予想非開示)
  > 【水準】⚪妥当（4.0/7）— PER12.44倍・PEG—・52週97.3% ／ 💰単元18.7万円
  > 【戦略】当日高値超えの逆指値1883円で順張り参戦を検討。上限1901.8円・SL1769.1円目安
- 2811 Kagome Co., Ltd.｜granville_tenkan｜業績データ取得不可(経常益予想非開示)(None)｜⚪妥当(3.0)｜PASS｜2839｜💰28.4万｜逆指値2845.5 SL2674.3｜⚠日程不明
  > 【業態】トマト加工品で首位。飲料ブランドに強み。農産品事業を育成。海外で業務用。
  > 【いま】終値2,839円・直近5日+2.96%（材料未確認）
  > 【調子】業績データ取得不可(経常益予想非開示)（—/13） — 業績データ取得不可(経常益予想非開示)
  > 【水準】⚪妥当（3.0/7）— PER24.45倍・PEG—・52週80.8% ／ 💰単元28.4万円
  > 【戦略】当日高値超えの逆指値2845.5円で順張り参戦を検討。上限2874円・SL2674.3円目安
- 7921 ＴＡＫＡＲＡ　＆　ＣＯＭＰＡＮＹ｜granville_tenkan｜業績データ取得不可(経常益予想非開示)(None)｜⚪妥当(3.0)｜PASS｜4300｜💰43.0万｜⛔提案なし(指名鮮度切れ 13営業日)｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】ディスクロージャー大手。有価証券報告書の作成が主力。通訳・翻訳事業が拡大。
  > 【いま】終値4,300円・直近5日+3.74%（材料未確認）
  > 【調子】業績データ取得不可(経常益予想非開示)（—/13） — 業績データ取得不可(経常益予想非開示)
  > 【水準】⚪妥当（3.0/7）— PER15.86倍・PEG—・52週75.4% ／ 💰単元43.0万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 13営業日)）
- 4765 ＳＢＩグローバルアセットマネジメント｜granville_tenkan｜判定保留(None)｜⏸判定不能(None)｜FAIL_UWAHIGE｜619｜💰6.2万｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 9025 Konoike Transport Co., Ltd.｜granville_tenkan｜業績—｜－未評価｜FAIL_INSEN｜2969｜💰—｜—
- 6570 Kyowa Corporation Co. Ltd.｜granville_oshime｜🚀確変(13)｜🟢値頃(5.0)｜FAIL_INSEN｜3030｜💰37.5万｜—
- 6574 コンヴァノ｜granville_oshime｜🚀確変(13)｜🟢値頃(5.0)｜FAIL_INSEN｜990｜💰9.6万｜—｜⚡材料後出し
- 7480 スズデン｜granville_oshime｜🚀確変(13)｜⚪妥当(4.0)｜FAIL_UWAHIGE｜3615｜💰35.6万｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 5243 ｎｏｔｅ｜granville_oshime｜🚀確変(11)｜⚪妥当(4.0)｜FAIL_INSEN｜2660｜💰27.5万｜—
- 9308 乾汽船｜granville_oshime｜🚀確変(11)｜⚪妥当(4.0)｜FAIL_INSEN｜2260｜💰23.9万｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 6834 精工技研｜granville_oshime｜🔥絶好調(10)｜💎割安(6.0)｜FAIL_INSEN｜4950｜💰52.8万｜—｜⚡材料後出し 📑TOPIX新規採用（10/30 組入）
- 7609 ダイトロン｜granville_oshime｜🔥絶好調(9)｜💎割安(6.0)｜FAIL_INSEN｜3760｜💰37.7万｜—
- 8051 山善｜granville_oshime｜🔥絶好調(9)｜🟢値頃(5.0)｜FAIL_INSEN｜1828｜💰18.4万｜—
- 8137 サンワテクノス｜granville_oshime｜🔥絶好調(9)｜🟢値頃(5.0)｜FAIL_INSEN｜3870｜💰38.8万｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 153A Caulis, Inc.｜granville_oshime｜🔥絶好調(9)｜⚪妥当(3.0)｜FAIL_UWAHIGE｜2073｜💰20.6万｜—｜⚡材料後出し
- 4258 AMIYA Corporation｜granville_oshime｜🔥絶好調(9)｜⚪妥当(3.0)｜PASS_DOJI｜5040｜💰50.4万｜⛔型不一致(十字線: トウバ)
  > 【業態】情報・通信業
  > 【いま】終値5,040円・直近5日-5.62%（材料未確認）
  > 【調子】🔥絶好調（9/13） — 上方修正済み・⚠下期依存
  > 【水準】⚪妥当（3.0/7）— PER40.48倍・PEG1.071・52週51.0% ／ 💰単元50.4万円
  > 【戦略】発注対象外（⛔型不一致(十字線: トウバ)）
- 8392 大分銀行｜granville_oshime｜🔥絶好調(8)｜💎割安(6.0)｜FAIL_INSEN｜2656｜💰27.6万｜—
- 3156 レスター｜granville_oshime｜🔥絶好調(8)｜🟢値頃(5.6)｜FAIL_INSEN｜5070｜💰52.5万｜—｜⚡材料後出し
- 6523 ＰＨＣホールディングス｜granville_oshime｜🔥絶好調(8)｜🟢値頃(5.0)｜FAIL_INSEN｜1230｜💰12.8万｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 9304 澁澤倉庫｜granville_oshime｜🔥絶好調(8)｜🟢値頃(5.0)｜FAIL_UWAHIGE｜1940｜💰19.6万｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 2384 ＳＢＳホールディングス｜granville_oshime｜🔥絶好調(8)｜⚪妥当(3.0)｜PASS｜5820｜💰58.2万｜指値5690 SL5671.2｜📉決算反応日 11/16
  > 【業態】総合物流会社。物流一括受託が主力。食品輸送に力。物流施設の流動化も。
  > 【いま】終値5,820円・直近5日+6.40%・📊Summary of Consolidated Financial Results  for the Nine Months Ended September 30, 2026  (Under Japanese GAAP)
  > 【調子】🔥絶好調（8/13）
  > 【水準】⚪妥当（3.0/7）— PER15.94倍・PEG0.694・52週91.7% ／ 💰単元58.2万円
  > 【戦略】5690円までの押し目を指値で待つ。SL5671.2円（25日線基準）
- 3968 セグエグループ｜granville_oshime｜🔥絶好調(8)｜⚪妥当(3.0)｜FAIL_UWAHIGE｜903｜💰8.0万｜—
- 4180 Appier Group, Inc.｜granville_oshime｜🔥絶好調(8)｜⚪妥当(3.0)｜FAIL_INSEN｜1451｜💰13.3万｜—｜⚡材料後出し
- 4443 Ｓａｎｓａｎ｜granville_oshime｜🔥絶好調(8)｜⚪妥当(3.0)｜FAIL_INSEN｜2192｜💰23.2万｜—
- 3673 ブロードリーフ｜granville_oshime｜⚡好調(7)｜💎割安(6.0)｜PASS_DOJI｜341｜💰3.4万｜⛔型不一致(十字線: トウバ)｜📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】自動車整備向け部品取引のクラウドサービス提供。自動車部品データベースに強み。
  > 【いま】終値341円・直近5日-24.72%（材料未確認）
  > 【調子】⚡好調（7/13） — 税引前代替・突出ボーナス・⚠減速
  > 【水準】💎割安（6.0/7）— PER26.85倍・PEG0.322・52週21.7% ／ 💰単元3.4万円
  > 【戦略】発注対象外（⛔型不一致(十字線: トウバ)）
- 6036 ＫｅｅＰｅｒ技研｜granville_oshime｜⚡好調(7)｜💎割安(6.0)｜PASS｜1772｜💰17.7万｜⛔型不一致(既に支持帯以下)｜🚨決算直前 11/16(残1営業日) 📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】自動車ボディーのコーティング材料を販売。直営、FC店も展開。施工技術支援も。
  > 【いま】終値1,772円・直近5日-1.12%（材料未確認）
  > 【調子】⚡好調（7/13） — E軸判定不能(期首・進捗なし)
  > 【水準】💎割安（6.0/7）— PER15.54倍・PEG0.517・52週69.6% ／ 💰単元17.7万円
  > 【戦略】発注対象外（⛔型不一致(既に支持帯以下)）
- 5892 ＹＵＴＯＲＩ｜granville_oshime｜⚡好調(7)｜🟢値頃(5.0)｜FAIL_INSEN｜2540｜💰25.9万｜—｜⚡材料後出し
- 3040 ソリトンシステムズ｜granville_oshime｜⚡好調(7)｜⚪妥当(4.0)｜FAIL_INSEN｜2600｜💰29.6万｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 4398 ブロードバンドセキュリティ｜granville_oshime｜⚡好調(7)｜⚪妥当(4.0)｜FAIL_INSEN｜2107｜💰22.6万｜—
- 4206 アイカ工業｜granville_oshime｜⚡好調(7)｜⚪妥当(3.0)｜FAIL_INSEN｜4094｜💰42.5万｜—
- 6736 Suncorporation｜granville_oshime｜⚡好調(7)｜⚪妥当(3.0)｜FAIL_INSEN｜10570｜💰131.3万｜—｜⚡材料後出し 📑TOPIX新規採用（10/30 組入）
- 8410 Seven Bank, Ltd.｜granville_oshime｜⚡好調(7)｜⚪妥当(3.0)｜FAIL_UWAHIGE｜350.9｜💰3.5万｜—
- 2492 インフォマート（インフォＭＴ）｜granville_oshime｜⚡好調(7)｜🟡やや割高(2.0)｜FAIL_INSEN｜747｜💰7.5万｜—
- 7806 MTG Co., Ltd.｜granville_oshime｜⚡好調(7)｜🟡やや割高(2.0)｜FAIL_INSEN｜7230｜💰81.1万｜—｜📑TOPIX新規採用（10/30 組入）
- 8388 阿波銀行｜granville_oshime｜⚡好調(6)｜💎割安(6.0)｜FAIL_INSEN｜1929｜💰19.4万｜—
- 3106 倉敷紡績｜granville_oshime｜⚡好調(6)｜🟢値頃(5.6)｜FAIL_INSEN｜2133｜💰22.2万｜—
- 6250 Yamabiko Corporation｜granville_oshime｜⚡好調(6)｜🟢値頃(5.0)｜PASS_DOJI｜3990｜💰39.9万｜⛔提案なし(指名鮮度切れ 15営業日)｜📉決算反応日 11/13
  > 【業態】農林業機械首位。共立、新ダイワ工業が統合。刈払機等小型屋外作業機拡充。
  > 【いま】終値3,990円・直近5日-5.45%（材料未確認）
  > 【調子】⚡好調（6/13） — E軸判定不能(進捗データ取得不可)
  > 【水準】🟢値頃（5.0/7）— PER9.90倍・PEG0.558・52週71.3% ／ 💰単元39.9万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 15営業日)）
- 4674 クレスコ｜granville_oshime｜⚡好調(6)｜⚪妥当(4.0)｜FAIL_INSEN｜1960｜💰19.7万｜—
- 4498 Cybertrust Japan Co.Ltd.｜granville_oshime｜⚡好調(6)｜⚪妥当(3.0)｜FAIL_INSEN｜1666｜💰18.1万｜—
- 9552 クオンツ総研ホールディングス｜granville_oshime｜⚡好調(6)｜⚪妥当(3.0)｜FAIL_UWAHIGE｜1146｜💰11.5万｜—｜⚡材料後出し 📑TOPIX低減対象（次 01/29 第2回/8）
- 9536 SAIBU GAS HOLDINGS CO. LTD.｜granville_oshime｜⚡好調(5)｜⚪妥当(4.0)｜FAIL_UWAHIGE｜2933｜💰29.0万｜—
- 436A サイバーソリューションズ（サイバＳＯＬ）｜granville_oshime｜⚡好調(5)｜⚪妥当(3.0)｜FAIL_INSEN｜1570｜💰17.3万｜—
- 4373 Simplex Holdings,Inc.｜granville_oshime｜⚡好調(5)｜⚪妥当(3.0)｜FAIL_UWAHIGE｜1189｜💰11.7万｜—
- 6877 ＯＢＡＲＡ　ＧＲＯＵＰ（ＯＢＡＲＡＧ）｜granville_oshime｜⚡好調(5)｜⚪妥当(3.0)｜FAIL_INSEN｜6580｜💰67.7万｜—｜⚡材料後出し 📑TOPIX低減対象（次 01/29 第2回/8）
- 6191 エボラブルアジア｜granville_oshime｜🔻悪化(5)｜🔴過熱(1.0)｜PASS｜1484｜💰14.8万｜⛔提案なし(材料後出し)｜⚠日程不明 ⚡材料後出し 📑TOPIX低減対象（次 01/29 第2回/8） ⚠業績基調が下向き（🔻悪化）
  > 【業態】航空券予約サイト「エアトリ」運営。阪急交通と提携。投資事業、オフショア開発も展開。
  > 【いま】終値1,484円・直近5日+6.92%・📊Consolidated Financial Results  for the Fiscal Year Ended September 30, 2026 [IFRS]
  > 【調子】🔻悪化（5/13） — 質注意
  > 【水準】🔴過熱（1.0/7）— PER51.17倍・PEG—・52週74.4% ／ 💰単元14.8万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 5036 日本ビジネスシステムズ｜granville_oshime｜✅順調(4)｜🟢値頃(5.0)｜FAIL_INSEN｜1566｜💰17.5万｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 8395 佐賀銀行｜granville_oshime｜⚠減速(4)｜🟢値頃(5.0)｜FAIL_INSEN｜6070｜💰61.7万｜—
- 8159 Tachibana Eletech Co., Ltd.｜granville_oshime｜✅順調(4)｜⚪妥当(3.0)｜FAIL_INSEN｜4345｜💰43.2万｜—
- 3042 セキュアヴェイル（セキュアヴェ）｜granville_oshime｜✅順調(4)｜🟡やや割高(2.0)｜PASS_DOJI｜736｜💰7.4万｜⛔提案なし(材料後出し)｜📉決算反応日 11/16 ⚡材料後出し 📐進捗 遅れ -26.5%
  > 【業態】情報セキュリティの設計・構築・監視、ログ分析サービス。24時間有人対応。
  > 【いま】終値736円・直近5日-10.90%・📊Second Quarter (Semi-Annual) Financial Results Presentation  For the Fiscal Year Ending March 31, 2027  Six Months Ended September 30, 2026
  > 【調子】✅順調（4/13） — 進捗モデル値域外・⚠進捗遅れ
  > 【水準】🟡やや割高（2.0/7）— PER57.05倍・PEG2.853・52週29.1% ／ 💰単元7.4万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 6080 Ｍ＆Ａキャピタルパートナーズ｜granville_oshime｜✅順調(4)｜🟡やや割高(2.0)｜FAIL_UWAHIGE｜4590｜💰46.5万｜—｜⚡材料後出し
- 3762 テクマトリックス（テクマト）｜granville_oshime｜✅順調(4)｜🔴過熱(1.0)｜FAIL_INSEN｜3140｜💰32.0万｜—
- 5985 SUNCALL CORPORATION｜granville_oshime｜✅順調(3)｜🟢値頃(5.2)｜FAIL_UWAHIGE｜1769｜💰17.1万｜—｜⚡材料後出し 📑TOPIX低減対象（次 01/29 第2回/8）
- 338A ZenmuTech,Inc.｜granville_oshime｜✅順調(3)｜⚪妥当(4.0)｜FAIL_UWAHIGE｜3240｜💰32.2万｜—
- 9509 Hokkaido Electric Power Company,Incorporated｜granville_oshime｜🔻悪化(3)｜⚪妥当(3.0)｜FAIL_UWAHIGE｜1149.5｜💰11.5万｜—
- 4208 UBE Corporation｜granville_oshime｜✅順調(3)｜🟡やや割高(2.0)｜PASS｜3361｜💰33.6万｜⛔提案なし(指名鮮度切れ 21営業日)｜⚠日程不明
  > 【業態】ナイロン原料の大手。化学・医薬・機械と多角。建設資材をUBE三菱セメントへ移行。
  > 【いま】終値3,361円・直近5日+7.11%・📊(Delayed) Financial Results for the 1st Half FY2026
  > 【調子】✅順調（3/13） — 進捗モデル値域外・質注意・上方修正済み
  > 【水準】🟡やや割高（2.0/7）— PER12.81倍・PEG3.216・52週74.8% ／ 💰単元33.6万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 21営業日)）
- 4044 Central Glass Co., Ltd.｜granville_oshime｜✅順調(3)｜🔴過熱(1.0)｜FAIL_INSEN｜4715｜💰44.4万｜—
- 456A Human Made Inc.｜granville_oshime｜✅順調(3)｜🔴過熱(0.0)｜FAIL_UWAHIGE｜1995｜💰21.5万｜—
- 3692 ＦＦＲＩセキュリティ｜granville_oshime｜➖横ばい(2)｜🔴過熱(1.0)｜FAIL_INSEN｜6590｜💰74.9万｜—
- 8255 Axial Retailing, Inc.｜granville_oshime｜➖横ばい(2)｜🔴過熱(0.0)｜FAIL_UWAHIGE｜1555｜💰15.4万｜—
- 8361 Ogaki Kyoritsu Bank, Ltd.｜granville_oshime｜取得不可(None)｜💎割安(6.0)｜FAIL_INSEN｜1520｜💰14.7万｜—｜⚡材料後出し
- 9166 GENDA Inc.｜granville_oshime｜業績データ取得不可(None)｜🟢値頃(5.6)｜FAIL_INSEN｜673｜💰6.8万｜—
- 336A ダイナミックマッププラットフォーム｜granville_oshime｜業績データ取得不可(経常益予想非開示)(None)｜⚪妥当(4.2)｜FAIL_UWAHIGE｜1320｜💰11.5万｜—
- 3993 PKSHA Technology, Inc.｜granville_oshime｜業績データ取得不可(None)｜⚪妥当(4.2)｜FAIL_UWAHIGE｜3335｜💰32.5万｜—
- 4432 ウイングアーク１ｓｔ｜granville_oshime｜業績データ取得不可(経常益予想非開示)(None)｜🟡やや割高(2.0)｜FAIL_INSEN｜3545｜💰35.2万｜—
- 6027 Bengo4.com, Inc.｜granville_oshime｜取得不可(None)｜🔴過熱(1.0)｜FAIL_INSEN｜4265｜💰51.1万｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 3851 日本一ソフトウェア｜granville_rebound｜🚀確変(12)｜💎割安(6.0)｜FAIL_INSEN｜1125｜💰11.8万｜—｜⚡材料後出し
- 3778 SAKURA Internet Inc.｜granville_rebound｜🚀確変(12)｜🟢値頃(5.0)｜FAIL_INSEN｜3080｜💰31.6万｜—
- 3891 ニッポン高度紙工業｜granville_rebound｜🚀確変(11)｜💎割安(6.0)｜FAIL_INSEN｜5720｜💰57.9万｜—
- 6138 ダイジェット工業（ダイジェト）｜granville_rebound｜🚀確変(11)｜💎割安(6.0)｜FAIL_INSEN｜1733｜💰17.6万｜—
- 6862 ミナト HD｜granville_rebound｜🚀確変(11)｜💎割安(6.0)｜FAIL_INSEN｜3020｜💰33.6万｜—
- 6769 Thine Electronics, Inc.｜granville_rebound｜🚀確変(11)｜⚪妥当(4.0)｜FAIL_UWAHIGE｜934｜💰9.5万｜—
- 479A PRONI Inc.｜granville_rebound｜🔥絶好調(10)｜💎割安(6.0)｜FAIL_INSEN｜1502｜💰15.5万｜—｜⚡材料後出し
- 3691 DIGITAL PLUS, Inc.｜granville_rebound｜🔥絶好調(10)｜🟢値頃(5.6)｜FAIL_INSEN｜1280｜💰13.2万｜—｜⚡材料後出し
- 4968 Arakawa Chemical Industries,Ltd.｜granville_rebound｜🔥絶好調(10)｜🟢値頃(5.0)｜FAIL_INSEN｜1876｜💰19.7万｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 5381 Mipox Corp.｜granville_rebound｜🔥絶好調(10)｜🟢値頃(5.0)｜FAIL_INSEN｜841｜💰8.8万｜—｜⚡材料後出し
- 2962 テクニスコ｜granville_rebound｜🔥絶好調(10)｜⚪妥当(4.0)｜FAIL_INSEN｜1486｜💰16.1万｜—｜⚡材料後出し
- 4419 Finatext Holdings Ltd.｜granville_rebound｜🔥絶好調(10)｜⚪妥当(4.0)｜FAIL_INSEN｜1193｜💰12.4万｜—｜⚡材料後出し
- 1436 GreenEnergy & Company｜granville_rebound｜🔥絶好調(9)｜💎割安(6.0)｜FAIL_UWAHIGE｜1390｜💰14.2万｜—
- 2489 アドウェイズ｜granville_rebound｜⚠減速(9)｜🟢値頃(5.0)｜FAIL_INSEN｜328｜💰3.3万｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 3793 Drecom Co., Ltd.｜granville_rebound｜⚠減速(9)｜🟢値頃(5.0)｜FAIL_UWAHIGE｜456｜💰4.6万｜—
- 6963 ROHM Company Limited｜granville_rebound｜🔥絶好調(9)｜🟢値頃(5.0)｜FAIL_INSEN｜2917｜💰31.7万｜—
- 150A ＪＳＨ｜granville_rebound｜🔥絶好調(9)｜⚪妥当(4.0)｜PASS｜715｜💰7.2万｜⛔提案なし(指名鮮度切れ 11営業日)｜ストップ高 📉決算反応日 11/13
  > 【業態】障がい者雇用支援の農園や訪問看護・診療サービスなどを手掛ける。
  > 【いま】終値715円・直近5日+28.14%（材料未確認）
  > 【調子】🔥絶好調（9/13） — E軸判定不能(進捗データ不足)
  > 【水準】⚪妥当（4.0/7）— PER21.09倍・PEG0.048・52週70.1% ／ 💰単元7.2万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 11営業日)）
- 6317 Kitagawa Corporation｜granville_rebound｜🔥絶好調(8)｜💎割安(6.0)｜FAIL_INSEN｜2285｜💰22.9万｜—｜⚡材料後出し 📑TOPIX低減対象（次 01/29 第2回/8）
- 7715 長野計器｜granville_rebound｜🔥絶好調(8)｜🟢値頃(5.0)｜FAIL_INSEN｜3350｜💰35.5万｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 8364 清水銀行｜granville_rebound｜🔥絶好調(8)｜🟢値頃(5.0)｜FAIL_UWAHIGE｜2741｜💰28.1万｜—｜⚡材料後出し 📑TOPIX低減対象（次 01/29 第2回/8）
- 460A ＢＲＡＮＵ｜granville_rebound｜🔥絶好調(8)｜⚪妥当(4.0)｜FAIL_INSEN｜1050｜💰11.0万｜—
- 6508 Meidensha Corporation｜granville_rebound｜⚡好調(7)｜💎割安(6.0)｜FAIL_INSEN｜7378｜💰76.2万｜—
- 5367 Nikkato Corporation｜granville_rebound｜⚡好調(7)｜🟢値頃(5.0)｜FAIL_INSEN｜1030｜💰10.8万｜—
- 6490 ＰＩＬＬＡＲ｜granville_rebound｜⚡好調(7)｜⚪妥当(4.0)｜FAIL_INSEN｜9170｜💰93.8万｜—
- 5252 日本ナレッジ｜granville_rebound｜⚡好調(7)｜🟡やや割高(2.0)｜PASS｜1000｜💰10.0万｜指値1000 SL841｜📉決算反応日 11/16
  > 【業態】ソフトウェアのテスト・品質検証サービスのほかシステム受託開発。業務系システムに強み。
  > 【いま】終値1,000円・直近5日+13.77%（材料未確認）
  > 【調子】⚡好調（7/13） — E軸判定不能(進捗データ不足)・⚠進捗遅れ
  > 【水準】🟡やや割高（2.0/7）— PER49.26倍・PEG2.174・52週65.8% ／ 💰単元10.0万円
  > 【戦略】当日終値1000円の指値で反転を取りにいく。SL841円（直近5日安値）
- 9697 カプコン｜granville_rebound｜⚡好調(7)｜🔴過熱(0.0)｜PASS｜4512｜💰45.1万｜⛔提案なし(指名鮮度切れ 11営業日)｜⚠日程不明
  > 【業態】家庭用ゲームソフト大手。「モンハン」「戦国BASARA」等人気作品多数。SNS向け拡大。
  > 【いま】終値4,512円・直近5日+8.88%（材料未確認）
  > 【調子】⚡好調（7/13）
  > 【水準】🔴過熱（0.0/7）— PER32.55倍・PEG2.722・52週89.2% ／ 💰単元45.1万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 11営業日)）
- 477A Startline CO.,LTD.｜granville_rebound｜⚡好調(6)｜💎割安(7.0)｜FAIL_INSEN｜604｜💰6.1万｜—｜⚡材料後出し
- 4100 Toda Kogyo Corp.｜granville_rebound｜⚡好調(6)｜💎割安(6.0)｜FAIL_INSEN｜1651｜💰18.1万｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 7213 LECIP Holdings Corporation｜granville_rebound｜⚡好調(6)｜💎割安(6.0)｜FAIL_UWAHIGE｜576｜💰5.7万｜—
- 3850 INTRAMART CORPORATION｜granville_rebound｜⚡好調(6)｜🟢値頃(5.0)｜FAIL_INSEN｜3245｜💰33.4万｜—
- 6947 図研｜granville_rebound｜⚡好調(6)｜⚪妥当(3.0)｜FAIL_UWAHIGE｜5220｜💰50.8万｜—
- 6958 日本シイエムケイ｜granville_rebound｜⚡好調(6)｜⚪妥当(3.0)｜FAIL_INSEN｜721｜💰7.5万｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 8344 Yamagata Bank, Ltd.｜granville_rebound｜⚡好調(5)｜🟢値頃(5.6)｜FAIL_INSEN｜4270｜💰44.1万｜—｜⚡材料後出し
- 6742 京三製作所｜granville_rebound｜⚠減速(5)｜⚪妥当(4.0)｜FAIL_INSEN｜963｜💰9.8万｜—｜⚡材料後出し 📑TOPIX低減対象（次 01/29 第2回/8）
- 4667 Aisan Technology Co.,Ltd.｜granville_rebound｜⚡好調(5)｜⚪妥当(3.0)｜FAIL_INSEN｜715｜💰8.1万｜—
- 7826 フルヤ金属｜granville_rebound｜⚡好調(5)｜⚪妥当(3.0)｜FAIL_INSEN｜8870｜💰90.5万｜—
- 9278 BOOKOFF GROUP HOLDINGS LIMITED｜granville_rebound｜⚡好調(5)｜🟡やや割高(2.0)｜PASS｜2595｜💰25.9万｜⛔提案なし(指名鮮度切れ 16営業日)｜⚠日程不明 📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】中古書籍販売最大手。衣料、家電など総合リユース。トレカ店も。伊藤忠と提携。
  > 【いま】終値2,595円・直近5日+6.75%（材料未確認）
  > 【調子】⚡好調（5/13）
  > 【水準】🟡やや割高（2.0/7）— PER16.27倍・PEG2.743・52週68.6% ／ 💰単元25.9万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 16営業日)）
- 7256 河西工業｜granville_rebound｜⚡好調(5)｜🔴過熱(1.4)｜FAIL_INSEN｜393｜💰—｜—
- 4025 多木化学｜granville_rebound｜✅順調(4)｜⚪妥当(3.0)｜FAIL_INSEN｜5270｜💰53.6万｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 428A Cypress Holdings Co., Ltd.｜granville_rebound｜✅順調(4)｜⚪妥当(3.0)｜FAIL_UWAHIGE｜1494｜💰14.6万｜—
- 3371 ソフトクリエイトホールディングス｜granville_rebound｜✅順調(4)｜🟡やや割高(2.0)｜FAIL_INSEN｜2051｜💰20.5万｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 278A Ｔｅｒｒａ　Ｄｒｏｎｅ｜granville_rebound｜✅順調(4)｜⏸判定不能(None)｜FAIL_INSEN｜5440｜💰—｜—
- 4396 System Support Holdings Inc.｜granville_rebound｜✅順調(3)｜⚪妥当(4.0)｜FAIL_UWAHIGE｜1336｜💰13.2万｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 4440 WITZ Corp.｜granville_rebound｜➖横ばい(2)｜⚪妥当(3.0)｜FAIL_INSEN｜1627｜💰16.9万｜—
- 3687 Fixstars Corp.｜granville_rebound｜➖横ばい(2)｜🟡やや割高(2.0)｜FAIL_INSEN｜1598｜💰17.0万｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 6676 BUFFALO INC.｜granville_rebound｜⚠減速(1)｜⚪妥当(3.0)｜FAIL_INSEN｜3180｜💰32.1万｜—｜⚡材料後出し 📑TOPIX低減対象（次 01/29 第2回/8）
- 6203 Howa Machinery, Ltd.｜granville_rebound｜⚠減速(1)｜🟡やや割高(2.0)｜FAIL_INSEN｜1907｜💰20.2万｜—
- 8360 Yamanashi Chuo Bank, Ltd.｜granville_rebound｜取得不可(None)｜💎割安(6.0)｜FAIL_INSEN｜1249｜💰12.9万｜—
- 8377 ほくほくフィナンシャルグループ｜granville_rebound｜業績データ取得不可(売上/経常欠損)(None)｜💎割安(6.0)｜FAIL_INSEN｜758.1｜💰7.7万｜—
- 7380 Juroku Financial Group,Inc.｜granville_rebound｜業績データ取得不可(売上/経常欠損)(None)｜⚪妥当(3.0)｜FAIL_UWAHIGE｜2362｜💰23.3万｜—
- 8368 Hyakugo Bank, Ltd.｜granville_rebound｜業績データ取得不可(売上/経常欠損)(None)｜⚪妥当(3.0)｜FAIL_INSEN｜2059｜💰21.4万｜—
- 8551 北日本銀行｜granville_rebound｜取得不可(None)｜⚪妥当(3.0)｜FAIL_INSEN｜2251｜💰23.7万｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 7184 富山第一銀行｜granville_rebound｜取得不可(None)｜🟡やや割高(2.0)｜FAIL_INSEN｜3100｜💰32.0万｜—
- 8713 Fidea Holdings Co.Ltd.｜granville_rebound｜業績データ取得不可(売上/経常欠損)(None)｜🔴過熱(1.4)｜FAIL_INSEN｜2486｜💰25.6万｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 3565 Ascentech KK｜granville_rebound｜業績—｜－未評価｜FAIL_UWAHIGE｜456｜💰—｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 4075 ブレインズテクノロジー｜granville_rebound｜取得不可(None)｜⏸判定不能(None)｜FAIL_INSEN｜1039｜💰10.9万｜—
- 4240 Cluster Technology Co., Ltd.｜granville_rebound｜業績—｜－未評価｜FAIL_UWAHIGE｜529｜💰—｜—｜⚡材料後出し
- 4884 Kringle Pharma, Inc.｜granville_rebound｜業績—｜－未評価｜FAIL_UWAHIGE｜557｜💰—｜—｜⚡材料後出し
- 5256 Fusic Co.,Ltd.｜granville_rebound｜業績—｜－未評価｜PASS｜2660｜💰—｜⛔提案なし(材料後出し)｜📉決算反応日 11/16 ⚡材料後出し
  > 【業態】研究機関向けシステム開発やIoT・クラウド・AI活用したデジタルトランスフォーメーション事業。
  > 【いま】終値2,660円・直近5日+2.90%・📊2027年６月期第１四半期決算短信〔日本基準〕(非連結)
  > 【調子】—（—/13）
  > 【水準】－未評価（次回①-9で算定）（—/7）— PER—倍・PEG—・52週—% ／ 💰単元—万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 5599 S&J Corporation｜granville_rebound｜業績—｜－未評価｜PASS_DOJI｜1500｜💰—｜⛔型不一致(十字線: トウバ)｜⚠日程不明
  > 【業態】サイバーセキュリティ対策専業。企業中心に監視・受託・コンサルティングサービスを手掛ける。
  > 【いま】終値1,500円・直近5日-11.61%・📌S&J、加速するAIによるサイバー攻撃の高度化・高速化に対応、AIと専門家による「WebアプリソースコードAI診断」の提供を開始
  > 【調子】—（—/13）
  > 【水準】－未評価（次回①-9で算定）（—/7）— PER—倍・PEG—・52週—% ／ 💰単元—万円
  > 【戦略】発注対象外（⛔型不一致(十字線: トウバ)）
- 6840 ＡＫＩＢＡホールディングス｜granville_rebound｜業績データ取得不可(None)｜⏸判定不能(None)｜FAIL_INSEN｜598｜💰6.4万｜—｜⚡材料後出し
- 6890 Ferrotec Corporation｜granville_rebound｜業績データ取得不可(None)｜⏸判定不能(None)｜FAIL_INSEN｜7025｜💰76.2万｜—｜📑TOPIX新規採用（10/30 組入）
- 6904 Harada Industry Co., Ltd.｜granville_rebound｜業績—｜－未評価｜FAIL_INSEN｜674｜💰—｜—
- 7175 Imamura Securities Co.Ltd.｜granville_rebound｜業績データ取得不可(None)｜⏸判定不能(None)｜FAIL_UWAHIGE｜1619｜💰16.1万｜—
- 8609 岡三証券グループ｜granville_rebound｜業績データ取得不可(None)｜⏸判定不能(None)｜FAIL_INSEN｜1064｜💰10.6万｜—
- 8739 スパークス・グループ｜granville_rebound｜業績データ取得不可(None)｜⏸判定不能(None)｜FAIL_UWAHIGE｜2433｜💰24.4万｜—｜📑TOPIX低減対象（次 01/29 第2回/8）

## 変化点銘柄
- 265A エイチエムコム｜changepoint｜🚀確変(12)｜🟢値頃(5.0)｜FAIL_INSEN｜660｜💰6.9万｜—｜⚡材料後出し 🔒実弾封印中(PL3紙ログ収集中)
- 4011 Headwaters Co.,Ltd｜changepoint🔔｜🚀確変(11)｜🟢値頃(5.0)｜FAIL_INSEN｜1829｜💰19.1万｜—｜⚡材料後出し 🔒実弾封印中(PL3紙ログ収集中)
- 7695 交換できるくん｜changepoint｜🔥絶好調(10)｜⚪妥当(4.0)｜FAIL_INSEN｜839｜💰8.3万｜—｜⚡材料後出し 🔒実弾封印中(PL3紙ログ収集中)
- 7318 セレンディップ・ホールディングス｜changepoint｜🔥絶好調(8)｜💎割安(6.0)｜FAIL_INSEN｜1030｜💰11.3万｜—｜⚡材料後出し 🔒実弾封印中(PL3紙ログ収集中)
- 5582 （名称取得不可）｜changepoint｜🔥絶好調(8)｜🟢値頃(5.0)｜PASS｜1737｜💰17.4万｜⛔提案なし(指名鮮度切れ 19営業日)｜🚨決算直前 11/16(残1営業日) 🔒実弾封印中(PL3紙ログ収集中)
  > 【業態】人工知能を用いた計画最適化システムの開発・販売を展開。電力、交通、物流等。
  > 【いま】終値1,737円・直近5日+4.39%（材料未確認）
  > 【調子】🔥絶好調（8/13） — E軸判定不能(進捗データ不足)
  > 【水準】🟢値頃（5.0/7）— PER20.85倍・PEG0.675・52週7.2% ／ 💰単元17.4万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 19営業日)）
- 478A Hutzper Inc.｜changepoint｜⚡好調(7)｜⚪妥当(4.0)｜FAIL_UWAHIGE｜640｜💰6.6万｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 8151 東陽テクニカ｜changepoint🔔｜⚡好調(6)｜💎割安(6.0)｜FAIL_INSEN｜1812｜💰17.4万｜—｜📑TOPIX低減対象（次 01/29 第2回/8） 🔒実弾封印中(PL3紙ログ収集中)
- 9343 アイビス｜changepoint｜⚡好調(6)｜⚪妥当(3.0)｜FAIL_INSEN｜696｜💰7.2万｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 4475 （名称取得不可）｜changepoint🔔🔔｜⚡好調(6)｜🔴過熱(1.0)｜FAIL_UWAHIGE｜2378｜💰25.9万｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 218A Liberaware｜changepoint｜⚡好調(5)｜⚪妥当(4.2)｜FAIL_UWAHIGE｜799｜💰8.3万｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 286A ユカリア｜changepoint🔔｜⚡好調(5)｜⚪妥当(4.0)｜FAIL_INSEN｜747｜💰7.6万｜—｜⚡材料後出し 🔒実弾封印中(PL3紙ログ収集中)
- 4483 JMDC｜changepoint🔔｜⚡好調(5)｜🔴過熱(1.0)｜FAIL_INSEN｜3740｜💰39.8万｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 4071 Plus Alpha Consulting Co. LTD.｜changepoint｜✅順調(4)｜🟡やや割高(2.0)｜FAIL_UWAHIGE｜2501｜💰23.1万｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 4165 PLAID Inc.｜changepoint🔔🔔｜🔻悪化(4)｜🔴過熱(1.0)｜FAIL_INSEN｜781｜💰7.4万｜—｜⚡材料後出し 🔒実弾封印中(PL3紙ログ収集中)
- 598A チャットプラス｜changepoint🔔｜✅順調(3)｜⚪妥当(4.0)｜FAIL_INSEN｜981｜💰10.8万｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 6785 鈴木｜changepoint｜✅順調(3)｜🟡やや割高(2.0)｜FAIL_INSEN｜2988｜💰30.1万｜—｜📑TOPIX低減対象（次 01/29 第2回/8） 🔒実弾封印中(PL3紙ログ収集中)
- 4488 AI inside Inc.｜changepoint🔔｜➖横ばい(2)｜🟡やや割高(2.0)｜FAIL_INSEN｜1794｜💰18.1万｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 4259 ExaWizards Inc.｜changepoint｜取得不可(None)｜⚪妥当(4.0)｜FAIL_INSEN｜575｜💰7.2万｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 3923 ラクス｜changepoint🔔🔔｜判定保留(変則決算)(None)｜⚪妥当(3.0)｜PASS｜1142.5｜💰11.4万｜⛔提案なし(材料後出し)｜📉決算反応日 11/16 ⚡材料後出し 🔒実弾封印中(PL3紙ログ収集中)
  > 【業態】中小企業向けクラウドで開発・販売・支援。メール管理と経費精算ソフトが主軸。
  > 【いま】終値1,142円・直近5日+7.83%・📊Consolidated Financial Results for the Six Months Ended September 30, 2026
  > 【調子】判定保留(変則決算)（—/13） — 事業譲渡(IT人材事業を2026/4/1譲渡・連結除外)により前期比が壊れているため判定保留
  > 【水準】⚪妥当（3.0/7）— PER16.05倍・PEG0.915・52週73.7% ／ 💰単元11.4万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 4478 freee K.K.｜changepoint｜取得不可(None)｜⚪妥当(3.0)｜FAIL_INSEN｜3880｜💰41.2万｜—｜📑TOPIX新規採用（10/30 組入） 🔒実弾封印中(PL3紙ログ収集中)
- 3989 シェアテク｜changepoint🔔｜業績データ取得不可(None)｜🟡やや割高(2.8)｜PASS｜1549｜💰15.5万｜⛔提案なし(材料後出し)｜📉決算反応日 11/16 ⚡材料後出し 🔒実弾封印中(PL3紙ログ収集中)
  > 【業態】家庭の生活トラブルに対応するマッチングサイトを運営。登録は便利屋が中心。
  > 【いま】終値1,549円・直近5日+1.11%・📊2026年9月期　決算短信〔ＩＦＲＳ〕（連結）
  > 【調子】業績データ取得不可（—/13） — 業績データ取得不可(売上/経常欠損)
  > 【水準】🟡やや割高（2.8/7）— PER14.82倍・PEG—・52週88.9% ／ 💰単元15.5万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 593A Tier IV, Inc.｜changepoint🔔🔔｜取得不可(None)｜🟡やや割高(2.8)｜PASS｜2033｜💰20.3万｜⛔提案なし(材料後出し)｜📉決算反応日 11/16 ⚡材料後出し 📑TOPIX新規採用（10/30 組入） 🔒実弾封印中(PL3紙ログ収集中)
  > 【業態】自動運転ソフトウェア「Autoware」を活用した自動運転車両の開発を手掛ける。
  > 【いま】終値2,033円・直近5日-10.28%・📊Consolidated Financial Results for the Fiscal Year Ended September 30, 2026 (Under Japanese GAAP)
  > 【調子】取得不可（—/13） — 業績データ取得不可(前期比行なし)
  > 【水準】🟡やや割高（2.8/7）— PER—倍・PEG—・52週39.8% ／ 💰単元20.3万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）

## 🤖AI特需銘柄
波: wave_on なし／25MA 上回り率 📡エネマネ・計量 14.29% ・❄️冷却・空調 50.0% ・🌐光通信 27.27% ・🔬基板・素材 7.14% ・🏢大型・指数寄与 13.79%
- 6777 santec｜ai_momentum｜🚀確変(11)｜⚪妥当(4.0)｜FAIL_INSEN｜19540｜💰209.1万｜—｜📑TOPIX新規採用（10/30 組入） 🤖AI特需
- 9824 泉州電業｜ai_momentum｜🔥絶好調(10)｜⚪妥当(4.0)｜FAIL_INSEN｜7550｜💰78.3万｜—｜🤖AI特需
- 6613 QD Laser, Inc.｜ai_momentum｜🔥絶好調(10)｜🔴過熱(2.0)｜FAIL_INSEN｜1980｜💰21.9万｜—｜📑TOPIX新規採用（10/30 組入） 🤖AI特需
- 6521 オキサイド｜ai_momentum｜⚡好調(7)｜🟢値頃(5.0)｜FAIL_UWAHIGE｜3175｜💰30.9万｜—｜🤖AI特需
- 6988 日東電工｜ai_momentum｜⚡好調(5)｜🟡やや割高(2.0)｜PASS｜3550｜💰35.5万｜逆指値3567 SL3352｜⚠日程不明 🤖AI特需
  > 【業態】テープ、フィルムの総合材料メーカー。液晶・半導体、医療用など。ニッチ商品で高シェア。
  > 【いま】終値3,550円・直近5日+7.64%（材料未確認）
  > 【調子】⚡好調（5/13） — E軸:進捗53.2%>=前年同期51.4%
  > 【水準】🟡やや割高（2.0/7）— PER16.45倍・PEG2.025・52週57.8% ／ 💰単元35.5万円
  > 【戦略】当日高値超えの逆指値3567円で順張り参戦を検討。上限3602.7円・SL3352円目安
- 4063 信越化学工業｜ai_momentum｜✅順調(4)｜⚪妥当(3.0)｜FAIL_INSEN｜5704｜💰57.1万｜—｜⚡材料後出し 🤖AI特需
- 6367 ダイキン工業｜ai_momentum｜✅順調(4)｜🔴過熱(1.0)｜PASS｜23480｜💰234.8万｜逆指値23485 SL22071.2｜⚠日程不明 🤖AI特需 ❄️冷却・空調/下流 ⚠1単元でリスク枠超過（141380円）
  > 【業態】エアコンで世界トップ級。業務用は国内圧倒。冷凍・冷蔵機器やフッソ化学事業も。
  > 【いま】終値23,480円・直近5日+7.76%（材料未確認）
  > 【調子】✅順調（4/13） — 質注意
  > 【水準】🔴過熱（1.0/7）— PER23.33倍・PEG10.785・52週67.3% ／ 💰単元234.8万円
  > 【戦略】当日高値超えの逆指値23485円で順張り参戦を検討。上限23719.8円・SL22071.2円目安／⚠1単元リスク141380円（枠超過）
- 1975 新日本空調｜ai_momentum｜➖横ばい(2)｜⚪妥当(3.0)｜FAIL_INSEN｜3435｜💰34.6万｜—｜⚡材料後出し 🤖AI特需
- 3131 Shinden Hightex Corp.｜ai_reversal｜🚀確変(13)｜💎割安(6.0)｜FAIL_UWAHIGE｜7100｜💰73.1万｜—｜🤖AI特需
- 4047 関東電化工業｜ai_reversal｜🚀確変(13)｜💎割安(6.0)｜FAIL_INSEN｜1711｜💰18.1万｜—｜🤖AI特需
- 6918 アバールデータ｜ai_reversal｜🚀確変(13)｜🟢値頃(5.0)｜FAIL_INSEN｜2830｜💰32.7万｜—｜🤖AI特需 🔬基板・素材/装置・商社
- 3374 内外テック｜ai_reversal｜🚀確変(12)｜💎割安(6.0)｜FAIL_INSEN｜4020｜💰41.1万｜—｜⚡材料後出し 🤖AI特需
- 4062 イビデン｜ai_reversal｜🚀確変(12)｜🟢値頃(5.0)｜FAIL_INSEN｜6087｜💰69.2万｜—｜🤖AI特需
- 6857 アドバンテスト｜ai_reversal｜🚀確変(11)｜⚪妥当(4.0)｜FAIL_INSEN｜30610｜💰314.4万｜—｜🤖AI特需
- 5801 古河電気工業｜ai_reversal｜🔥絶好調(10)｜💎割安(7.0)｜FAIL_INSEN｜2167.5｜💰23.7万｜—｜🤖AI特需
- 6787 メイコー｜ai_reversal｜🔥絶好調(10)｜💎割安(7.0)｜FAIL_INSEN｜8190｜💰83.2万｜—｜🤖AI特需
- 8035 東京エレクトロン｜ai_reversal｜🔥絶好調(10)｜💎割安(7.0)｜FAIL_INSEN｜9461｜💰92.7万｜—｜🤖AI特需
- 6407 CKD｜ai_reversal｜🔥絶好調(10)｜💎割安(6.0)｜FAIL_INSEN｜4047｜💰41.4万｜—｜⚡材料後出し 🤖AI特需
- 3110 日東紡｜ai_reversal｜🔥絶好調(9)｜💎割安(7.0)｜FAIL_UWAHIGE｜2654.5｜💰28.0万｜—｜🤖AI特需
- 4368 扶桑化学工業｜ai_reversal｜🔥絶好調(9)｜💎割安(6.0)｜FAIL_INSEN｜2891｜💰30.2万｜—｜🤖AI特需
- 6779 Nihon Dempa Kogyo Co., Ltd.｜ai_reversal｜🔥絶好調(9)｜💎割安(6.0)｜FAIL_INSEN｜1836｜💰19.8万｜—｜🤖AI特需
- 2760 東京エレクトロンデバイス｜ai_reversal｜🔥絶好調(9)｜🟢値頃(5.0)｜FAIL_INSEN｜4040｜💰39.9万｜—｜🤖AI特需
- 4971 メック｜ai_reversal｜🔥絶好調(9)｜🟢値頃(5.0)｜FAIL_INSEN｜5310｜💰57.3万｜—｜🤖AI特需
- 6235 オプトラン｜ai_reversal｜🔥絶好調(9)｜🟢値頃(5.0)｜FAIL_INSEN｜2269｜💰22.9万｜—｜🤖AI特需
- 6762 TDK｜ai_reversal｜🔥絶好調(9)｜🟢値頃(5.0)｜FAIL_INSEN｜2310｜💰23.7万｜—｜🤖AI特需
- 6981 村田製作所｜ai_reversal｜🔥絶好調(9)｜🟢値頃(5.0)｜FAIL_INSEN｜5177｜💰54.6万｜—｜🤖AI特需
- 7729 東京精密｜ai_reversal｜🔥絶好調(9)｜🟢値頃(5.0)｜FAIL_INSEN｜13150｜💰134.9万｜—｜🤖AI特需
- 6323 ローツェ｜ai_reversal｜🔥絶好調(9)｜⚪妥当(4.0)｜FAIL_INSEN｜3253｜💰33.6万｜—｜🤖AI特需
- 7735 SCREENホールディングス｜ai_reversal｜🔥絶好調(8)｜💎割安(7.0)｜FAIL_INSEN｜8564｜💰87.8万｜—｜⚡材料後出し 🤖AI特需
- 6941 山一電機｜ai_reversal｜🔥絶好調(8)｜💎割安(6.0)｜FAIL_INSEN｜6610｜💰69.6万｜—｜🤖AI特需
- 6524 湖北工業｜ai_reversal｜🔥絶好調(8)｜🟢値頃(5.6)｜FAIL_UWAHIGE｜4485｜💰48.2万｜—｜🤖AI特需
- 5384 フジミインコーポレーテッド｜ai_reversal｜🔥絶好調(8)｜🟢値頃(5.0)｜FAIL_INSEN｜2938｜💰30.1万｜—｜🤖AI特需
- 6752 パナソニックHD｜ai_reversal｜⚡好調(7)｜🟢値頃(5.0)｜FAIL_INSEN｜3193｜💰32.6万｜—｜🤖AI特需
- 6336 石井表記｜ai_reversal｜⚡好調(6)｜💎割安(7.0)｜FAIL_INSEN｜1214｜💰12.7万｜—｜🤖AI特需
- 1961 三機工業｜ai_reversal｜⚡好調(6)｜⚪妥当(4.0)｜FAIL_UWAHIGE｜2532｜💰24.1万｜—｜🤖AI特需
- 6227 AIMECHATEC Ltd.｜ai_reversal｜⚡好調(6)｜⚪妥当(4.0)｜FAIL_INSEN｜4800｜💰48.5万｜—｜⚡材料後出し 📑TOPIX新規採用（10/30 組入） 🤖AI特需
- 6971 京セラ｜ai_reversal｜⚡好調(6)｜⚪妥当(3.0)｜FAIL_INSEN｜2977｜💰30.1万｜—｜⚡材料後出し 🤖AI特需
- 3436 SUMCO｜ai_reversal｜⚡好調(5)｜💎割安(7.0)｜FAIL_INSEN｜2114.5｜💰20.9万｜—｜🤖AI特需
- 4022 ラサ工業｜ai_reversal｜⚡好調(5)｜💎割安(7.0)｜FAIL_INSEN｜1319｜💰14.3万｜—｜🤖AI特需
- 4973 JCU｜ai_reversal｜⚡好調(5)｜⚪妥当(3.0)｜FAIL_INSEN｜4045｜💰41.2万｜—｜📑TOPIX低減対象（次 01/29 第2回/8） 🤖AI特需
- 6590 芝浦メカトロニクス｜ai_reversal｜✅順調(4)｜🟢値頃(5.0)｜FAIL_INSEN｜2924｜💰29.2万｜—｜🤖AI特需
- 255A GLテクノHD｜ai_reversal｜✅順調(4)｜⚪妥当(4.0)｜FAIL_INSEN｜4120｜💰41.0万｜—｜🤖AI特需
- 5706 三井金属鉱業｜ai_reversal｜🔻悪化(4)｜⚪妥当(4.0)｜FAIL_INSEN｜1538｜💰16.7万｜—｜🤖AI特需
- 5208 Arisawa Mfg.Co., Ltd.｜ai_reversal｜✅順調(4)｜🔴過熱(1.0)｜FAIL_INSEN｜2290｜💰23.3万｜—｜🤖AI特需
- 6965 浜松ホトニクス｜ai_reversal｜✅順調(4)｜🔴過熱(1.0)｜FAIL_INSEN｜2182｜💰23.6万｜—｜🤖AI特需
- 3103 ユニチカ｜ai_reversal｜⚠減速(3)｜💎割安(6.0)｜FAIL_INSEN｜1215｜💰13.1万｜—｜🤖AI特需
- 6501 日立製作所｜ai_reversal｜✅順調(3)｜🟡やや割高(2.0)｜FAIL_INSEN｜4962｜💰49.5万｜—｜🤖AI特需
- 2802 味の素｜ai_reversal｜➖横ばい(2)｜⚪妥当(4.0)｜FAIL_INSEN｜4227｜💰42.6万｜—｜🤖AI特需
- 9503 関西電力｜ai_reversal｜🔻悪化(2)｜🟡やや割高(2.0)｜PASS｜2729.5｜💰27.3万｜指値2729.5 SL2583.5｜⚠日程不明 🤖AI特需 ⚠業績基調が下向き（🔻悪化） 📐進捗 遅れ -36.3%
  > 【業態】東電と並ぶ業界の雄。原発依存度高いが代替電源確保へ。情報通信も。
  > 【いま】終値2,730円・直近5日+6.85%（材料未確認）
  > 【調子】🔻悪化（2/13） — 質注意・経常減益-44.1%・🔼加速・⚠進捗遅れ
  > 【水準】🟡やや割高（2.0/7）— PER9.81倍・PEG—・52週62.8% ／ 💰単元27.3万円
  > 【戦略】当日終値2729.5円の指値で反転を取りにいく。SL2583.5円（直近5日安値）
- 1982 日比谷総合設備｜ai_reversal｜➖横ばい(2)｜🔴過熱(1.0)｜FAIL_INSEN｜3165｜💰31.6万｜—｜🤖AI特需 ❄️冷却・空調/下流
- 5302 日本カーボン｜ai_reversal｜➖横ばい(2)｜🔴過熱(1.0)｜FAIL_INSEN｜4820｜💰48.5万｜—｜📑TOPIX低減対象（次 01/29 第2回/8） 🤖AI特需
- 6617 東光高岳｜ai_reversal｜⚠減速(1)｜⚪妥当(4.0)｜FAIL_INSEN｜5010｜💰51.8万｜—｜🤖AI特需
- 9432 NTT｜ai_reversal｜⚠減速(1)｜🟡やや割高(2.0)｜PASS｜168.4｜💰1.7万｜⛔型不一致(既に支持帯以下)｜🤖AI特需 🌐光通信/下流 ⚠業績基調が下向き（⚠減速） 📐進捗 遅れ -10.3%
  > 【業態】国内通信事業最大手。持ち株会社制で地域電話独占。携帯、光回線高シェア。
  > 【いま】終値168円・直近5日+5.12%（材料未確認）
  > 【調子】⚠減速（1/13） — 経常減益-3.9%・質注意・⚠進捗遅れ
  > 【水準】🟡やや割高（2.0/7）— PER13.69倍・PEG—・52週66.7% ／ 💰単元1.7万円
  > 【戦略】発注対象外（⛔型不一致(既に支持帯以下)）
- 4203 住友ベークライト｜ai_reversal｜業績データ取得不可(None)｜⚪妥当(4.0)｜FAIL_INSEN｜7285｜💰75.7万｜—｜🤖AI特需
- 9434 ソフトバンク｜ai_reversal｜業績データ取得不可(経常益予想非開示)(None)｜⚪妥当(4.0)｜PASS｜240.1｜💰2.4万｜⛔型不一致(既に支持帯以下)｜🤖AI特需 🏢大型・指数寄与/投資通信
  > 【業態】ソフトバンクグループの中核。携帯・固定通信ネットワーク基盤にICTソリューションを提供。
  > 【いま】終値240円・直近5日+2.00%（材料未確認）
  > 【調子】業績データ取得不可(経常益予想非開示)（—/13） — 経常欠損
  > 【水準】⚪妥当（4.0/7）— PER20.88倍・PEG—・52週74.6% ／ 💰単元2.4万円
  > 【戦略】発注対象外（⛔型不一致(既に支持帯以下)）
- 6146 ディスコ｜ai_reversal｜取得不可(None)｜⏸判定不能(None)｜FAIL_INSEN｜47470｜💰475.8万｜—｜🤖AI特需
- 6723 ルネサスエレクトロニクス｜ai_reversal｜取得不可(None)｜⏸判定不能(None)｜FAIL_INSEN｜2847.5｜💰29.2万｜—｜🤖AI特需
- 9984 ソフトバンクグループ｜ai_reversal｜業績データ取得不可(経常益予想非開示)(None)｜⏸判定不能(None)｜FAIL_INSEN｜3547｜💰38.5万｜—｜🤖AI特需

## ⚡材料後出し
その日の足は開示前の情報。判定は参考値
- 1435 robot home Inc.｜FAIL_INSEN｜📌[Delayed]Notice Concerning the Establishment of a Subsidiary(Second-tier Subsidiary)by a Consolidated  Subsidiary and Change in a Specified Subsidiary（15:30）
- 153A Caulis, Inc.｜FAIL_UWAHIGE｜📌2026年12月期_第３四半期決算説明資料（15:30）
- 1928 積水ハウス｜PASS｜📌Notice Concerning Commencement of Tender Offer for Gifu landscape architect Co., Ltd. (Securities Code: 1438)（17:00）
- 1944 Kinden Corporation｜FAIL_INSEN｜📊(Corrections / Corrections of Numerical Data) Partial Corrections to the “Consolidated Financial Results for the Six Months Ended September 30, 2026（15:30）
- 1975 新日本空調｜FAIL_INSEN｜📌Notice of Application for Extension of the Deadline for Submission of the Half-year Report for the Fiscal Year Ending March 2027（17:00）
- 265A エイチエムコム｜FAIL_INSEN｜📌2026年12月期通期業績予想の修正に関するお知らせ（15:30）
- 276A CCReB Advisors Inc.｜FAIL_UWAHIGE｜📌独立役員届出書（16:30）
- 286A ユカリア｜FAIL_INSEN｜📌連結子会社の業績予想の修正に関するお知らせ（16:00）
- 2962 テクニスコ｜FAIL_INSEN｜📊2027年６月期 第１四半期決算短信〔日本基準〕（連結）（15:30）
- 3042 セキュアヴェイル（セキュアヴェ）｜PASS_DOJI｜📊Second Quarter (Semi-Annual) Financial Results Presentation  For the Fiscal Year Ending March 31, 2027  Six Months Ended September 30, 2026（15:30）
- 3077 Horiifoodservice Co., Ltd.｜FAIL_UWAHIGE｜📌2026年11月期 月次売上速報（10月度）のお知らせ（16:00）
- 3156 レスター｜FAIL_INSEN｜📌Notice Concerning Upward Revisions to the Full-Year Consolidated Financial Forecast and Dividend Forecast for the Fiscal Year Ending March 31, 2027（16:00）
- 3374 内外テック｜FAIL_INSEN｜📌2027年3月期中間期決算説明資料（15:45）
- 3445 RS Technologies Co. Ltd.｜FAIL_INSEN｜📊Q&A Regarding Financial Results Briefing for the 3rd Quarter of FY2026（16:00）
- 3496 アズーム｜PASS_DOJI｜📌（訂正）「2026年９月期決算説明資料」の一部訂正について（15:30）
- 3556 RenetJapanGroup, Inc.｜FAIL_INSEN｜📌2026年９月期　決算に関するオンラインライブ配信開催のご案内（開始時刻の変更）（15:30）
- 3591 WACOAL HOLDINGS CORP｜FAIL_UWAHIGE｜📌Announcement Regarding Purchase of Treasury Stock through Tokyo Stock Exchange Off-Auction Treasury Stock Repurchase Trading (ToSTNeT-3)（16:30）
- 3691 DIGITAL PLUS, Inc.｜FAIL_INSEN｜📌減損損失計上のお知らせ（15:30）
- 3696 セレス｜FAIL_UWAHIGE｜📌日本経済新聞社「2026年度 脱炭素経営ランキング GX500」に選出（15:00）
- 3851 日本一ソフトウェア｜FAIL_INSEN｜📊令和9年3月期　第2四半期（中間期）決算短信〔日本基準〕（連結）（15:30）
- 3923 ラクス｜PASS｜📊Consolidated Financial Results for the Six Months Ended September 30, 2026（15:30）
- 3989 シェアテク｜PASS｜📌2026年9月期　決算説明資料（事業計画及び成長可能性に関する事項）（15:30）
- 4011 Headwaters Co.,Ltd｜FAIL_INSEN｜👥主要株主の異動に関するお知らせ（16:15）
- 4053 Sun Asterisk, Inc.｜FAIL_UWAHIGE｜📊Financial Results Explanatory Materials for the 3rd Quarter of the Fiscal Year Ending December 2026（15:30）
- 4063 信越化学工業｜FAIL_INSEN｜📌Notice Concerning Decisions Relating to Repurchase of Shares（15:30）
- 4165 PLAID Inc.｜FAIL_INSEN｜📌Notice Regarding Unauthorized Access to Our Service（17:00）
- 4166 Cacco, Inc.｜PASS｜📌2026年12月期 第３四半期 決算説明資料（15:30）
- 4180 Appier Group, Inc.｜FAIL_INSEN｜📌Presentation Materials for the 3rd Quarter of the Fiscal Year Ending December 31,2026（15:30）
- 4240 Cluster Technology Co., Ltd.｜FAIL_UWAHIGE｜📊[Summary] Financial Results for the Six Months Ended September 30, 2026（16:00）
- 4293 セプテーニ・ホールディングス（セプテニＨＤ）｜FAIL_INSEN｜📌Notice of Change in Consolidated Subsidiaries (Share Transfer)（15:30）
- 4375 セーフィー｜FAIL_UWAHIGE｜📌2026年12月期第3四半期 決算説明資料（スマホ向けサマリ版）（17:00）
- 4379 Photosynth inc.｜PASS｜📌2026年12月期第3四半期決算説明会（書き起こし＆質疑応答）（15:30）
- 4419 Finatext Holdings Ltd.｜FAIL_INSEN｜📌2027年３月期第２四半期決算説明会 動画公開のお知らせ（17:00）
- 4634 ａｒｔｉｅｎｃｅ（ａｒｔｉｅｎ）｜FAIL_INSEN｜📌役員人事等に関するお知らせ（15:30）
- 477A Startline CO.,LTD.｜FAIL_INSEN｜📌2027年3月期第2四半期 決算説明動画公開のお知らせ（16:00）
- 479A PRONI Inc.｜FAIL_INSEN｜📊2026年12月期第３四半期決算短信〔日本基準〕（連結）（15:31）
- 4884 Kringle Pharma, Inc.｜FAIL_UWAHIGE｜📌2026年９月期 通期決算説明会動画 掲載のお知らせ（17:30）
- 4922 コーセーホールディングス｜PASS｜📌Notice of Changes in Executives（15:30）
- 5027 AnyMind Group Inc.｜FAIL_INSEN｜📌Answers to Possible Questions (FY2026 Q3 Results)（15:30）
- 5034 unerry, Inc.｜FAIL_UWAHIGE｜📌2027年6月期 第1四半期 決算説明会 質疑応答（要旨）（16:00）
- 5254 Arent, Inc.｜FAIL_INSEN｜📌2027年6月期 第1四半期 決算説明会 事前質問の回答（16:15）
- 5256 Fusic Co.,Ltd.｜PASS｜📊2027年６月期第１四半期決算短信〔日本基準〕(非連結)（16:00）
- 5381 Mipox Corp.｜FAIL_INSEN｜📌Notice Concerning Revisions to Full-Year Financial and Dividend Forecasts (Dividend Increase) for FY Ending March 2027（16:00）
- 5757 CK San-Etsu Co., Ltd.｜FAIL_INSEN｜📌Notice Concerning Acquisition of Business by Consolidated Subsidiary（15:30）
- 5844 Kyoto Financial Group,Inc.｜FAIL_INSEN｜📌Notice Regarding Revisions of Earnings Forecasts and Year-end Dividend Forecast（15:30）
- 5892 ＹＵＴＯＲＩ｜FAIL_INSEN｜📌2027年３月期 第２四半期 決算説明資料 スマホ向けサマリ版（16:00）
- 593A Tier IV, Inc.｜PASS｜📊Consolidated Financial Results for the Fiscal Year Ended September 30, 2026 (Under Japanese GAAP)（16:00）
- 5985 SUNCALL CORPORATION｜FAIL_UWAHIGE｜📌2027年３月期 剰余金の配当（中間配当）及び期末配当予想の修正（増配）に関するお知らせ（15:30）
- 6071 IBJ, Inc.｜FAIL_UWAHIGE｜📌Notice Regarding Changes to the Shareholder Benefit Program（15:30）
- 6080 Ｍ＆Ａキャピタルパートナーズ｜FAIL_UWAHIGE｜📦神戸新聞社と業務提携のお知らせ（15:30）
- 6191 エボラブルアジア｜PASS｜📊Consolidated Financial Results  for the Fiscal Year Ended September 30, 2026 [IFRS]（18:45）
- 6227 AIMECHATEC Ltd.｜FAIL_INSEN｜📌譲渡制限付株式報酬としての自己株式処分の払込完了に関するお知らせ（15:35）
- 6268 ナブテスコ｜FAIL_INSEN｜📌Summary of Consolidated Financial Statements for the Third Quarter of Fiscal Year Ending December 31, 2026 (IFRS)（16:00）
- 6317 Kitagawa Corporation｜FAIL_INSEN｜📌企業版ふるさと納税を通じた寄附実施のお知らせ（15:30）
- 6407 CKD｜FAIL_INSEN｜📊Consolidated Financial Results for the Six Months Ended September 30, 2026 (Under Japanese GAAP)（16:00）
- 6436 アマノ｜PASS｜📌Amano Group Corporate Governance Report（15:45）
- 6481 THK Co., Ltd.｜FAIL_INSEN｜📌Notice Regarding the Revision of Financial Forecasts（15:30）
- 6505 東洋電機製造｜PASS｜📌コーポレート・ガバナンスに関する報告書 2026/11/13（16:00）
- 6574 コンヴァノ｜FAIL_INSEN｜📌連結子会社であるアクセルマーク株式会社の第三者割当による第34回新株予約権の引受けに関するお知らせ（16:30）
- 6651 NITTO KOGYO Corporation｜FAIL_INSEN｜📌（数値データ訂正）2027年3月期通期業績予想の修正に関するお知らせにおける数値データ(XBRL)の一部訂正について（15:30）
- 6676 BUFFALO INC.｜FAIL_INSEN｜🔁自己株式立会外買付取引（ToSTNeT-３）、自己株式の公開買付け及び市場買付けに関するお知らせ（16:30）
- 6736 Suncorporation｜FAIL_INSEN｜📌Notice Regarding the Personnel Changes（16:00）
- 6742 京三製作所｜FAIL_INSEN｜📊[Summary]Summary of Consolidated Financial Results for the Six Months Ended September 30, 2026 (Under Japanese GAAP)（15:30）
- 6758 ソニーグループ｜PASS｜📌Disposal of Treasury Shares upon Vesting of Restricted Stock Units (“RSUs”)（15:30）
- 6768 Tamura Corporation｜FAIL_INSEN｜📊Financial Results Presentation for FY2026 2Q（15:00）
- 6804 ホシデン｜FAIL_UWAHIGE｜📌Notice regarding Adjustment of Conversion Price for Zero Coupon Convertible Bonds due 2031（16:00）
- 6834 精工技研｜FAIL_INSEN｜📊2027年3月期　第2四半期(中間期)決算短信〔日本基準〕(連結)（16:00）
- 6840 ＡＫＩＢＡホールディングス｜FAIL_INSEN｜📌2027年３月期 通期連結業績予想の公表に関するお知らせ（16:00）
- 6877 ＯＢＡＲＡ　ＧＲＯＵＰ（ＯＢＡＲＡＧ）｜FAIL_INSEN｜📊2026年９月期決算短信〔日本基準〕(連結)（17:00）
- 6925 Ushio Inc.｜FAIL_INSEN｜📊(Corrections / Corrections of Numerical Data) Consolidated Financial Results for the Year Ended March 31,2026 [under Japanese GAAP]（15:45）
- 6971 京セラ｜FAIL_INSEN｜📌Semiannual Securities Report (The First Half of the 73rd Business Term)（16:00）
- 7318 セレンディップ・ホールディングス｜FAIL_INSEN｜📊Supplementary Material for Q2 FY2027 Financial Results（15:30）
- 7322 三十三フィナンシャルグループ｜FAIL_INSEN｜📊[Summary]Consolidated Financial Results for the Six Months Ended September 30, 2026 (Under Japanese GAAP)（15:00）
- 7384 Procrea Holdings,Inc.｜FAIL_INSEN｜📌Notice Concerning the Establishment of Specialized Investment Subsidiary at Subsidiary Bank（15:30）
- 7695 交換できるくん｜FAIL_INSEN｜📌リフォームテクノロジーグループ 「株式会社IMI」 急な住まいのトラブルに備える保証で安心生活「保証できすぎくん」提供開始（16:00）
- 7735 SCREENホールディングス｜FAIL_INSEN｜📌Corporate Governance Report（16:00）
- 7744 ノーリツ鋼機｜FAIL_INSEN｜📌Notice Concerning Revision to Dividend Forecast（15:30）
- 7747 朝日インテック｜FAIL_INSEN｜📊Financial Results for the 1st Quarter of FYE June 2027（15:30）
- 8084 ＲＹＯＤＥＮ｜FAIL_INSEN｜📌2027年3月期第2四半期（中間期）　決算説明会資料（15:30）
- 8253 Credit Saison Co., Ltd.｜FAIL_UWAHIGE｜📌Corporate Governance Report（15:50）
- 8344 Yamagata Bank, Ltd.｜FAIL_INSEN｜📊[Summary]Consolidated Financial Results for the Six Months Ended September 30, 2026 (Under Japanese GAAP)（15:30）
- 8361 Ogaki Kyoritsu Bank, Ltd.｜FAIL_INSEN｜📌Notice Concerning Revision to Year-End Dividend Forecast (Dividend Increase)（16:00）
- 8364 清水銀行｜FAIL_UWAHIGE｜📊[Summary]Consolidated Financial Results for the Six Months Ended September 30, 2026 (Under Japanese GAAP)（15:30）
- 8366 滋賀銀行｜FAIL_INSEN｜📌Notice Regarding "Revision of Earnings Forecasts" and "Determination of Dividends from Surplus (Interim Dividends)" and "Revision of Year-end Dividend（15:00）
- 8944 Land Business Co., Ltd.｜FAIL_INSEN｜📊2026年9月期決算短信〔日本基準〕（連結）（15:30）
- 9552 クオンツ総研ホールディングス｜FAIL_UWAHIGE｜📊Consolidated Financial Results for the Fiscal Year Ended September 30, 2026  (Under IFRS)（15:30）
- 9554 AViC Co. Ltd.｜FAIL_UWAHIGE｜📌配当方針の変更及び2027年９月期の配当予想（初配）に関するお知らせ（15:30）
- 9722 藤田観光｜FAIL_UWAHIGE｜📊[Delayed]Financial Results for the Nine Months Ended September 30, 2026（15:30）

## 📢開示
使用した一覧: https://kabutan.jp/disclosures/?date=20261113 （1〜215頁）＋ https://kabutan.jp/disclosures/?date=20261112 （前回実行 20:30 以降の分・1頁）・取得3222件。見出しをそのまま転記（解釈なし）。フォールバック: なし。①-9へ引き渡し（recalc_queue 追加）82件
- 📌 3156 レスター｜Notice Concerning Upward Revisions to the Full-Year Consolidated Financial Forecast and Dividend Forecast for the Fiscal Year Ending March 31, 2027｜11-13 16:00
- 📌 3156 レスター｜Notice Concerning Initiatives to Review the Business Portfolio｜11-13 16:00
- 📊 3156 レスター｜[Summary] Consolidated Financial Results for the Six Months Ended September 30, 2026 (Under Japanese GAAP)｜11-13 16:00
- 📌 3156 レスター｜事業ポートフォリオ見直しに向けた取り組みに関するお知らせ｜11-13 16:00
- 📢 3156 レスター｜2027年３月期通期連結業績予想の修正（上方修正）並びに配当予想の修正（増配）に関するお知らせ｜11-13 16:00
- 📊 3156 レスター｜2027年３月期　第２四半期（中間期）決算短信〔日本基準〕（連結）｜11-13 16:00
- 📊 4206 アイカ｜Support Data for the Summary of Consolidated Financial Results for the Six Months Ended September 30, 2026｜11-13 13:00
- 📊 4206 アイカ｜Notice Concerning Revision to Financial Results Forecast (Upward Revision)｜11-13 13:00
- 📌 4206 アイカ｜Notice Concerning Dividend of Surplus (Interim Dividend)｜11-13 13:00
- 📊 4206 アイカ｜Consolidated Financial Results for the Six Months Ended September 30, 2026 (Under Japanese GAAP)｜11-13 13:00
- 📌 4206 アイカ｜剰余金の配当（中間配当）に関するお知らせ｜11-13 13:00
- 📢 4206 アイカ｜業績予想の修正（上方修正）に関するお知らせ｜11-13 13:00
- 📊 4206 アイカ｜2027年３月期 第２四半期（中間期）決算短信補足資料｜11-13 13:00
- 📊 4206 アイカ｜2027年３月期 第２四半期（中間期）決算短信〔日本基準〕(連結)｜11-13 13:00
- 📌 7695 リフォームＴ｜リフォームテクノロジーグループ 「株式会社IMI」 急な住まいのトラブルに備える保証で安心生活「保証できすぎくん」提供開始｜11-13 16:00
- 📌 7695 リフォームＴ｜2027年3月期 第2四半期決算説明資料｜11-13 16:00
- 📊 7695 リフォームＴ｜2027年3月期 第2四半期(中間期)決算短信〔日本基準〕(連結)｜11-13 16:00
- 📢 7695 リフォームＴ｜通期業績予想の修正（上方修正）に関するお知らせ｜11-13 16:00
- 📌 153A カウリス｜2026年12月期_第３四半期決算説明資料｜11-13 15:30
- 📊 153A カウリス｜2026年12月期　第３四半期決算短信〔日本基準〕（非連結）｜11-13 15:30
- 📊 1944 きんでん｜(Corrections / Corrections of Numerical Data) Partial Corrections to the “Consolidated Financial Results for the Six Months Ended September 30, 2026｜11-13 15:30
- 📊 1944 きんでん｜（訂正・数値データ訂正）「2027年３月期　第２四半期（中間期）決算短信〔日本基準〕（連結）」の一部訂正について｜11-13 15:30
- 📌 1961 三機工｜Notice Concerning Dividends of Surplus (Interim Dividends) and Revision of Year-End Dividend Forecast (Dividend Increase)｜11-13 14:00
- 📊 1961 三機工｜Notice Concerning Revision of Financial Results Forecasts｜11-13 14:00
- 📊 1961 三機工｜〔Summary〕 Consolidated Financial Results for the Six Months Ended September 30, 2026 (Japanese GAAP)｜11-13 14:00
- 📌 1961 三機工｜剰余金の配当（中間配当）及び期末配当予想の修正（増配）に関するお知らせ｜11-13 14:00
- 📌 1961 三機工｜業績予想の修正に関するお知らせ｜11-13 14:00
- 📌 1961 三機工｜2026年度第2四半期 決算説明資料｜11-13 14:00
- 📊 1961 三機工｜2027年３月期第２四半期（中間期）決算短信〔日本基準〕(連結)｜11-13 14:00
- 📌 2267 ヤクルト｜Supplementary Materials for Financial Statements For the 2nd quarter Ended Sep. 30, 2026(Apr. 1, 2026 to Sep. 30, 2026)｜11-13 14:20
- 📊 2267 ヤクルト｜Consolidated Financial Results for the 2nd Quarter Ended September 30, 2026｜11-13 14:20
- 📊 2267 ヤクルト｜2027年3月期 第2四半期（中間期）決算短信補足説明資料｜11-13 14:20
- 📌 2267 ヤクルト｜Notification Regarding Transition to a Company with an Audit & Supervisory Committee｜11-13 14:20
- 📌 2267 ヤクルト｜監査等委員会設置会社への移行に関するお知らせ｜11-13 14:20
- 📌 2267 ヤクルト｜Notification Regarding a Fixed Asset Transfer｜11-13 14:20
- 📌 2267 ヤクルト｜固定資産の譲渡に関するお知らせ｜11-13 14:20
- 📌 2267 ヤクルト｜Notification Regarding the Formulation of Management Policy for Enhancing Corporate Value｜11-13 14:20
- 📌 2267 ヤクルト｜企業価値向上の実現に向けた経営方針の策定に関するお知らせ｜11-13 14:20
- 📊 2267 ヤクルト｜2027年3月期 第2四半期（中間期）決算短信［日本基準］（連結）｜11-13 14:20
- 📌 2384 ＳＢＳＨＤ｜2026年度 第3四半期　決算説明資料｜11-13 13:00
- 📊 2384 ＳＢＳＨＤ｜Summary of Consolidated Financial Results  for the Nine Months Ended September 30, 2026  (Under Japanese GAAP)｜11-13 13:00
- 📊 2384 ＳＢＳＨＤ｜2026年12月期　第３四半期決算短信〔日本基準〕(連結)｜11-13 13:00
- 📊 2502 アサヒ｜[Summary] Financial Results for the Nine Months Ended September 30, 2026｜11-13 11:30
- 📌 2502 アサヒ｜2026年12月期 第３四半期決算補足資料｜11-13 11:30
- 📊 2502 アサヒ｜2026年12月期 第３四半期決算短信〔ＩＦＲＳ〕（連結)｜11-13 11:30
- 📌 265A Ｈｍｃｏｍｍ｜2026年12月期通期業績予想の修正に関するお知らせ｜11-13 15:30
- 📌 265A Ｈｍｃｏｍｍ｜（開示事項の経過）連結子会社コラボテクノ株式会社のAI駆動開発体制への転換が進展｜11-13 15:30
- 📌 265A Ｈｍｃｏｍｍ｜2026年12月期　第３四半期決算説明資料｜11-13 15:30
- 📊 265A Ｈｍｃｏｍｍ｜2026年12月期 第３四半期決算短信〔日本基準〕（連結）｜11-13 15:30
- 📌 286A ユカリア｜連結子会社の業績予想の修正に関するお知らせ｜11-13 16:00
- 📌 286A ユカリア｜2026年12月期 第3四半期決算説明資料｜11-13 16:00
- 📊 286A ユカリア｜2026年12月期第3四半期決算短信〔日本基準〕(連結)｜11-13 16:00
- 📊 2962 テクニスコ｜2027年６月期 第１四半期決算短信〔日本基準〕（連結）｜11-13 15:30
- 📦 2962 テクニスコ｜大口受注に関するお知らせ｜11-13 15:30
- 📊 3042 セキュアヴェ｜Second Quarter (Semi-Annual) Financial Results Presentation  For the Fiscal Year Ending March 31, 2027  Six Months Ended September 30, 2026｜11-13 15:30
- 📌 3042 セキュアヴェ｜2027年3月期中間期決算説明資料｜11-13 15:30
- 📊 3042 セキュアヴェ｜Consolidated Financial Results   for the Six Months Ended September 30, 2026   (For the Fiscal Year Ending March 31, 2027)  ［Under Japanese GAAP］｜11-13 15:30
- 📊 3042 セキュアヴェ｜2027年３月期  第２四半期（中間期）決算短信〔日本基準〕（連結）｜11-13 15:30
- 📌 3374 内外テック｜2027年3月期中間期決算説明資料｜11-13 15:45
- 📌 3374 内外テック｜業績予想の修正および配当予想の修正に関するお知らせ｜11-13 15:45
- 📊 3374 内外テック｜2027年３月期　第２四半期（中間期）決算短信〔日本基準〕（連結）｜11-13 15:45
- 📊 3445 ＲＳテクノ｜Q&A Regarding Financial Results Briefing for the 3rd Quarter of FY2026｜11-13 16:00
- 📌 3445 ＲＳテクノ｜2026年12月期 第３四半期 決算説明 質疑応答集｜11-13 16:00
- 📊 3445 ＲＳテクノ｜FY2026/12 3Q Financial Results｜11-13 16:00
- 📌 3445 ＲＳテクノ｜2026年12月期 第３四半期 決算説明資料｜11-13 16:00
- 📊 3445 ＲＳテクノ｜[Summary] Consolidated Financial Results for the Nine Months Ended September 30, 2026｜11-13 16:00
- 📊 3445 ＲＳテクノ｜2026年12月期 第３四半期決算短信〔日本基準〕（連結）｜11-13 16:00
- 📌 3556 リネットＪ｜2026年９月期　決算に関するオンラインライブ配信開催のご案内（開始時刻の変更）｜11-13 15:30
- 📌 3556 リネットＪ｜役員人事に関するお知らせ｜11-13 08:00
- 📌 3556 リネットＪ｜定款一部変更に関するお知らせ｜11-13 08:00
- 📌 3556 リネットＪ｜2027年9月期配当予想（初配）及び株主優待制度の変更に関するお知らせ｜11-13 08:00
- 📌 3556 リネットＪ｜事業計画及び成長可能性に関する事項｜11-13 08:00
- 📌 3556 リネットＪ｜通期連結業績予想と実績値との差異及び個別決算における前事業年度の実績値との差異に関するお知らせ｜11-13 08:00
- 📌 3556 リネットＪ｜2026年9月期決算補足資料｜11-13 08:00
- 📊 3556 リネットＪ｜2026年9月期 決算短信〔日本基準〕（連結）｜11-13 08:00
- 📌 3691 デジプラ｜減損損失計上のお知らせ｜11-13 15:30
- 📌 3691 デジプラ｜2026年9月期通期　決算説明資料｜11-13 15:30
- 📊 3691 デジプラ｜2026年９月期　通期決算短信〔ＩＦＲＳ〕(連結)｜11-13 15:30
- 📊 3851 日本一ソフト｜令和9年3月期　第2四半期（中間期）決算短信〔日本基準〕（連結）｜11-13 15:30
- 📊 3923 ラクス｜Consolidated Financial Results for the Six Months Ended September 30, 2026｜11-13 15:30
- 📊 3923 ラクス｜2027年３月期 第２四半期（中間期）決算短信〔日本基準〕（連結）｜11-13 15:30
- 📌 3923 ラクス｜Notice Regarding the Decision on Acquisition and Cancellation of Treasury Shares｜11-13 15:30
- 📌 3923 ラクス｜自己株式取得に係る事項の決定及び自己株式消却に係る事項の決定に関するお知らせ｜11-13 15:30
- 📌 3923 ラクス｜Notice Regarding Revisions of Consolidated Guidance for the fiscal year ending March 2027｜11-13 15:30
- 📌 3923 ラクス｜2027年３月期通期連結業績予想の修正に関するお知らせ｜11-13 15:30
- 📌 3923 ラクス｜Notice Regarding Monthly Sales in FY2027 (Oct.)｜11-13 15:30
- 📌 3923 ラクス｜2027年3月期月次売上高（10月度）のお知らせ｜11-13 15:30
- 📌 3923 ラクス｜Earnings Results for H1 of the fiscal year ending March 2027｜11-13 15:30
- 📌 3923 ラクス｜2027年3月期第2四半期決算説明資料｜11-13 15:30
- 📌 3927 Ｆ－ブレイン｜剰余金の配当（中間配当）に関するお知らせ｜11-13 11:30
- 📌 3927 Ｆ－ブレイン｜2027年３月期 第２四半期（中間期）決算説明資料｜11-13 11:30
- 📊 3927 Ｆ－ブレイン｜2027年３月期 第２四半期（中間期）決算短信〔日本基準〕（連結）｜11-13 11:30
- 📌 3989 シェアテク｜2026年9月期　決算説明資料（事業計画及び成長可能性に関する事項）｜11-13 15:30
- 📊 3989 シェアテク｜2026年9月期　決算短信〔ＩＦＲＳ〕（連結）｜11-13 15:30
- 👥 4011 ヘッドウォ｜主要株主の異動に関するお知らせ｜11-13 16:15
- 📊 4011 ヘッドウォ｜2026年12月期第3四半期決算短信補足説明資料｜11-13 16:05
- 📊 4011 ヘッドウォ｜2026年12月期　第３四半期決算短信〔日本基準〕（連結）｜11-13 16:00
- 📊 4053 サンアスタ｜Financial Results Explanatory Materials for the 3rd Quarter of the Fiscal Year Ending December 2026｜11-13 15:30
- 📌 4053 サンアスタ｜2026年12月期第３四半期決算説明資料｜11-13 15:30
- 📊 4053 サンアスタ｜Consolidated Financial Results for the Nine Months ended September 30, 2026 [Japanese GAAP]｜11-13 15:30
- 📊 4053 サンアスタ｜2026年12月期  第３四半期決算短信〔日本基準〕（連結）｜11-13 15:30
- 📌 4058 トヨクモ｜Monthly Sales Report in FY2026 (Oct.)｜11-13 11:30
- 📌 4058 トヨクモ｜2026年10月度 月次売上速報に関するお知らせ｜11-13 11:30
- 📌 4058 トヨクモ｜2026年12月期 第３四半期 決算説明資料｜11-13 11:30
- 📊 4058 トヨクモ｜2026年12月期 第３四半期決算短信〔日本基準〕（連結）｜11-13 11:30
- 📊 4088 エアウォータ｜Notice Regarding the Determination of Scheduled Disclosure Dates for the First and Second Quarter Financial Results Summaries for FY2027｜11-13 13:30
- 📊 4088 エアウォータ｜2027年3月期第1四半期決算短信および第2四半期決算短信の開示予定日決定に関するお知らせ｜11-13 13:30
- 📌 4166 かっこ｜2026年12月期 第３四半期 決算説明資料｜11-13 15:30
- 📊 4166 かっこ｜2026年12月期 第３四半期 決算短信〔日本基準〕（連結）｜11-13 15:30
- 📌 4180 Ａｐｐｉｅｒ｜Presentation Materials for the 3rd Quarter of the Fiscal Year Ending December 31,2026｜11-13 15:30
- 📌 4180 Ａｐｐｉｅｒ｜2026年12月期 第3四半期 決算説明資料｜11-13 15:30
- 📌 4180 Ａｐｐｉｅｒ｜Announcement on Revision of the Consolidated Full-year Guidance and Dividend Forecast (Dividend Increase)｜11-13 15:30
- 📊 4180 Ａｐｐｉｅｒ｜Consolidated Financial Results for the Nine Months Ended September 30, 2026 [IFRS]｜11-13 15:30
- 📌 4180 Ａｐｐｉｅｒ｜通期連結業績予想の修正及び配当予想の修正（増配）に関するお知らせ｜11-13 15:30
- 📊 4180 Ａｐｐｉｅｒ｜2026年12月期　第３四半期決算短信〔ＩＦＲＳ〕（連結）｜11-13 15:30
- 📊 4208 ＵＢＥ｜(Delayed) Financial Results for the 1st Half FY2026｜11-13 11:00
- 📊 4240 クラスター｜[Summary] Financial Results for the Six Months Ended September 30, 2026｜11-13 16:00
- 📌 4240 クラスター｜2027年３月期第２四半期（中間期）個別業績予想と実績との差異に関するお知らせ｜11-13 16:00
- 📊 4240 クラスター｜2027年３月期第２四半期（中間期）決算短信〔日本基準〕(非連結)｜11-13 16:00
- 📌 4293 セプテニＨＤ｜Notice of Change in Consolidated Subsidiaries (Share Transfer)｜11-13 15:30
- 📌 4293 セプテニＨＤ｜連結子会社の異動（株式譲渡）に関するお知らせ｜11-13 15:30
- 📌 4293 セプテニＨＤ｜Summary of Consolidated Financial Statements for the Nine Months Ended September 30, 2026 [IFRS]｜11-13 15:30
- 📊 4293 セプテニＨＤ｜2026年12月期 第3四半期決算短信〔IFRS〕(連結)｜11-13 15:30
- 📌 4375 セーフィー｜2026年12月期第3四半期 決算説明資料（スマホ向けサマリ版）｜11-13 17:00
- 📌 4375 セーフィー｜Presentation Material for Q3 FY2026｜11-13 15:30
- 📌 4375 セーフィー｜2026年12月期第3四半期 決算説明資料｜11-13 15:30
- 📊 4375 セーフィー｜2026年12月期第3四半期 決算短信〔日本基準〕（連結）｜11-13 15:30
- 📊 4375 セーフィー｜[Summary] Financial Results for the Nine Months Ended September 30, 2026｜11-13 15:30
- 📌 4634 ａｒｔｉｅｎ｜役員人事等に関するお知らせ｜11-13 15:30
- 📌 4634 ａｒｔｉｅｎ｜Notice Regarding Change of Officers｜11-13 15:30
- 📌 4634 ａｒｔｉｅｎ｜Notice Concerning Treasury Share Acquisition and Tender Offer for Treasury Shares, and  Retirement of Treasury Shares｜11-13 15:30
- 📌 4634 ａｒｔｉｅｎ｜Notice of (Planned) Changes in Major Shareholders, the Largest Shareholder That is a Major Shareholder, and Other  Affiliated Companies｜11-13 15:30
- 📌 4634 ａｒｔｉｅｎ｜主要株主及び主要株主である筆頭株主並びにその他の関係会社の異動（予定）のお知らせ｜11-13 15:30
- 🔁 4634 ａｒｔｉｅｎ｜自己株式の取得及び自己株式の公開買付け並びに自己株式の消却に関するお知らせ｜11-13 15:30
- 📌 4634 ａｒｔｉｅｎ｜Notice Regarding the Revision to Consolidated Earnings Forecast, Revision to Gain on Sale of Investment Securities, and the Recording of Impairment Lo｜11-13 15:30
- 📌 4634 ａｒｔｉｅｎ｜連結業績予想の修正及び投資有価証券売却益の計上見込みの修正並びに減損損失の計上に関するお知らせ｜11-13 15:30
- 📊 4634 ａｒｔｉｅｎ｜Supplemental data of Q3 FY12/2026 Financial Results｜11-13 15:30
- 📌 4634 ａｒｔｉｅｎ｜2026年12月期 第3四半期 決算補足説明資料｜11-13 15:30
- 📊 4634 ａｒｔｉｅｎ｜Consolidated Quarterly Financial Results (Japanese Accounting Standards) for the First Three Quarters of the Fiscal Year Ending December 31, 2026｜11-13 15:30
- 📊 4634 ａｒｔｉｅｎ｜2026年12月期 第３四半期決算短信〔日本基準〕(連結)｜11-13 15:30
- 📌 477A スタートＬ｜2027年3月期第2四半期 決算説明動画公開のお知らせ｜11-13 16:00
- 📌 477A スタートＬ｜2027年3月期 第2四半期 決算説明資料｜11-13 16:00
- 📊 477A スタートＬ｜2027年3月期 第2四半期（中間期）決算短信〔日本基準〕（非連結）｜11-13 16:00
- 📊 479A ＰＲＯＮＩ｜2026年12月期第３四半期決算短信〔日本基準〕（連結）｜11-13 15:31
- 📌 479A ＰＲＯＮＩ｜2026年12月期第３四半期決算説明資料｜11-13 15:31
- 📦 479A ＰＲＯＮＩ｜株式会社商工組合中央金庫との資本業務提携に関するお知らせ｜11-13 15:31
- 📌 5027 エニマインド｜Answers to Possible Questions (FY2026 Q3 Results)｜11-13 15:30
- 📌 5027 エニマインド｜2026年12月期第3四半期決算において想定されるご質問への回答｜11-13 15:30
- 📊 5027 エニマインド｜Summary of Consolidated Financial Results for the First Three Quarters of the Fiscal Year Ending December 31, 2026｜11-13 15:30
- 📊 5027 エニマインド｜Presentation Material for FY2026 Q3 Financial Results｜11-13 15:30
- 📌 5027 エニマインド｜2026年12月期 第3四半期決算説明資料｜11-13 15:30
- 📊 5027 エニマインド｜2026年12月期第３四半期決算短信〔ＩＦＲＳ〕（連結）｜11-13 15:30
- 📊 5101 浜ゴム｜Consolidated Financial Results for the Nine Months Ended September 30, 2026[IFRS]｜11-13 14:00
- 📊 5101 浜ゴム｜FY2026 Third-Quarter Financial Results｜11-13 14:00
- 📌 5101 浜ゴム｜Progress of Technology & Production Transformation under YX2026｜11-13 14:00
- 📌 5101 浜ゴム｜2026年12月期  第３四半期決算説明会資料｜11-13 14:00
- 📌 5101 浜ゴム｜YX2026技術・生産改革の進捗｜11-13 14:00
- 📊 5101 浜ゴム｜2026年12月期　第３四半期決算短信〔ＩＦＲＳ〕（連結）｜11-13 14:00
- 📌 5137 スマートＤ｜特別損失の計上に関するお知らせ｜11-13 08:00
- 📌 5137 スマートＤ｜自己株式取得に係る事項の決定に関するお知らせ｜11-13 08:00
- 📌 5137 スマートＤ｜2026年９月期第４四半期　決算説明資料｜11-13 08:00
- 📊 5137 スマートＤ｜2026年９月期決算短信〔日本基準〕(連結)｜11-13 08:00
- 📊 5256 フュージック｜2027年６月期第１四半期決算短信〔日本基準〕(非連結)｜11-13 16:00
- 📌 5256 フュージック｜2027年６月期第１四半期決算補足説明資料｜11-13 16:00
- 📌 5381 マイポックス｜Notice Concerning Revisions to Full-Year Financial and Dividend Forecasts (Dividend Increase) for FY Ending March 2027｜11-13 16:00
- 📌 5381 マイポックス｜2027年3月期通期業績予想および配当予想の修正（増配）に関するお知らせ｜11-13 16:00
- 📊 5381 マイポックス｜Consolidated Financial Results for the Six Months Ended September 30, 2026 (Under Japanese GAAP)｜11-13 16:00
- 📊 5381 マイポックス｜2027年３月期 第２四半期（中間期）決算短信〔日本基準〕(連結)｜11-13 16:00
- 📌 5757 ＣＫサンエツ｜Notice Concerning Acquisition of Business by Consolidated Subsidiary｜11-13 15:30
- 📌 5757 ＣＫサンエツ｜当社連結子会社による事業譲受に関するお知らせ｜11-13 15:30
- 📌 5757 ＣＫサンエツ｜Notice Concerning Recording of Non-operating Expenses (Loss on Derivative Transactions and Loss on Valuation of Derivatives)｜11-13 15:30
- 📌 5757 ＣＫサンエツ｜営業外費用（デリバティブ損失およびデリバティブ評価損）の計上に関するお知らせ｜11-13 15:30
- 📌 5757 ＣＫサンエツ｜Notice Concerning Revision of Earnings Forecast of a Subsidiary (NIPPON SHINDO CO., LTD.)｜11-13 15:30
- 📌 5757 ＣＫサンエツ｜子会社（日本伸銅株式会社）の業績予想の修正に関するお知らせ｜11-13 15:30
- 📌 5757 ＣＫサンエツ｜Notice Concerning Revision of Earnings Forecast｜11-13 15:30
- 📌 5757 ＣＫサンエツ｜業績予想の修正に関するお知らせ｜11-13 15:30
- 📊 5757 ＣＫサンエツ｜[Summary]Consolidated Financial Results for the Six Months Ended September 30, 2026 (Under Japanese GAAP)｜11-13 15:30
- 📊 5757 ＣＫサンエツ｜2027年３月期 第２四半期（中間期）決算短信〔日本基準〕（連結）｜11-13 15:30
- 📌 5844 京都ＦＧ｜Notice Regarding Revisions of Earnings Forecasts and Year-end Dividend Forecast｜11-13 15:30
- 📌 5844 京都ＦＧ｜Notice Regarding Differences between Consolidated Earnings Forecasts and Actual Results for the Six Months Ended September 30, 2026｜11-13 15:30
- 📊 5844 京都ＦＧ｜Consolidated Financial Results (Under Japanese GAAP) for the Six Months Ended September 30, 2026｜11-13 15:30
- 📌 5844 京都ＦＧ｜通期業績予想の修正および期末配当予想の修正（増配）に関するお知らせ｜11-13 15:30
- 📌 5844 京都ＦＧ｜2027年3月期第2四半期（中間期）の業績予想と実績の差異に関するお知らせ｜11-13 15:30
- 📊 5844 京都ＦＧ｜2027年３月期 第２四半期（中間期）決算短信〔日本基準〕(連結)｜11-13 15:30
- 📌 5892 ユトリ｜2027年３月期 第２四半期 決算説明資料 スマホ向けサマリ版｜11-13 16:00
- 📊 5892 ユトリ｜FY 2027(ending March 31, 2027) 2nd Quarter Financial Results｜11-13 16:00
- 📌 5892 ユトリ｜2027年３月期 第２四半期 決算説明資料｜11-13 16:00
- 📊 5892 ユトリ｜Consolidated Financial Results for the second quarter (semi-annual period) of the fiscal year ending March 31, 2027 〔JGAAP〕｜11-13 16:00
- 📊 5892 ユトリ｜2027年３月期 第２四半期（中間期）決算短信〔日本基準〕(連結)｜11-13 16:00
- 📌 5892 ユトリ｜決算説明資料および説明動画の公開に関するお知らせ｜11-13 16:00
- 📊 593A ティアフォー｜Consolidated Financial Results for the Fiscal Year Ended September 30, 2026 (Under Japanese GAAP)｜11-13 16:00
- 📊 593A ティアフォー｜FY2026 Full-Year Financial Results Presentation｜11-13 16:00
- 📌 593A ティアフォー｜2026年９月期　通期決算説明資料｜11-13 16:00
- 📌 593A ティアフォー｜個別業績の前期実績値との差異に関するお知らせ｜11-13 16:00
- 📦 593A ティアフォー｜大口受注に関するお知らせ｜11-13 16:00
- 📌 593A ティアフォー｜特別損失（関係会社株式評価損）及び 営業外費用（持分法による投資損失）の計上に関するお知らせ｜11-13 16:00
- 📊 593A ティアフォー｜2026年９月期　決算短信〔日本基準〕(連結)｜11-13 16:00
- 📌 5985 サンコール｜2027年３月期 剰余金の配当（中間配当）及び期末配当予想の修正（増配）に関するお知らせ｜11-13 15:30
- 📊 5985 サンコール｜2027年３月期 第２四半期（中間期） 決算短信〔日本基準〕（連結）｜11-13 15:30
- 📌 6071 ＩＢＪ｜Notice Regarding Changes to the Shareholder Benefit Program｜11-13 15:30
- 📌 6071 ＩＢＪ｜株主優待制度の変更に関するお知らせ｜11-13 15:30
- 📊 6071 ＩＢＪ｜2026 3Q Financial Results Presentation｜11-13 15:30
- 📌 6071 ＩＢＪ｜2026年12月期3Q決算説明資料｜11-13 15:30
- 📊 6071 ＩＢＪ｜Consolidated Financial Results for the First Nine Months Ended September 30, 2026 (Under Japanese GAAP)｜11-13 15:30
- 📊 6071 ＩＢＪ｜2026年12月期第３四半期決算短信〔日本基準〕(連結)｜11-13 15:30
- 📊 6191 エアトリ｜Consolidated Financial Results  for the Fiscal Year Ended September 30, 2026 [IFRS]｜11-13 18:45
- 📌 6191 エアトリ｜Notice Regarding Differences Between Consolidated Earnings Forecasts and Actual Results｜11-13 17:12
- 📌 6191 エアトリ｜2026年９月期 第4四半期決算説明資料｜11-13 15:30
- 📌 6191 エアトリ｜連結業績予想数値と実績値との差異に関するお知らせ｜11-13 15:30
- 📊 6191 エアトリ｜2026年９月期決算短信〔ＩＦＲＳ〕(連結)｜11-13 15:30
- 📊 6203 豊和工｜[Summary] Financial Results for the Six Months Ended September 30, 2026｜11-13 14:00
- 📌 6203 豊和工｜2027年３月期　第２四半期（中間期）決算説明資料｜11-13 14:00
- 📊 6203 豊和工｜2027年３月期　第２四半期（中間期）決算短信〔日本基準〕（連結）｜11-13 14:00
- 📌 6227 ＡＩメカ｜譲渡制限付株式報酬としての自己株式処分の払込完了に関するお知らせ｜11-13 15:35
- 📊 6227 ＡＩメカ｜2027年６月期 第１四半期決算短信補足説明資料｜11-13 15:35
- 📊 6227 ＡＩメカ｜2027年６月期 第１四半期決算短信〔日本基準〕（連結）｜11-13 15:35
- 📌 6268 ナブテスコ｜Summary of Consolidated Financial Statements for the Third Quarter of Fiscal Year Ending December 31, 2026 (IFRS)｜11-13 16:00
- 📊 6268 ナブテスコ｜2026年12月期第３四半期決算短信〔ＩＦＲＳ〕（連結）｜11-13 16:00
- 📌 6317 北川鉄｜企業版ふるさと納税を通じた寄附実施のお知らせ｜11-13 15:30
- 📊 6317 北川鉄｜Consolidated Financial Results < under Japanese GAAP > For the Six Months Ended September 30 ,2026｜11-13 15:30
- 📌 6317 北川鉄｜2027年3月期連結業績予想の修正及び配当予想の修正に関するお知らせ｜11-13 15:30
- 📊 6317 北川鉄｜2027年3月期第2四半期（中間期）決算短信［日本基準］（連結）｜11-13 15:30
- 📌 6379 レイズネク｜Notice of Difference between Consolidated Financial Forecast and Actual Results for 1H FY2027｜11-13 14:00
- 📌 6379 レイズネク｜2027年3月期第2四半期決算説明資料｜11-13 14:00
- 📌 6379 レイズネク｜Notice Concerning Dividends of Surplus (Interim)｜11-13 14:00
- 📌 6379 レイズネク｜剰余金の配当（中間配当）に関するお知らせ｜11-13 14:00
- 📌 6379 レイズネク｜2027年3月期第2四半期（中間期）連結業績予想と実績値との差異に関するお知らせ｜11-13 14:00
- 📊 6379 レイズネク｜Consolidated Financial Results for the First Six Months (Interim) of the Fiscal Year Ending March 31,2027 [Japanese GAAP]｜11-13 14:00
- 📊 6379 レイズネク｜2027年3月期第2四半期（中間期）決算短信〔日本基準〕(連結)｜11-13 14:00
- 📊 6407 ＣＫＤ｜Consolidated Financial Results for the Six Months Ended September 30, 2026 (Under Japanese GAAP)｜11-13 16:00
- 📊 6407 ＣＫＤ｜2027年３月期第２四半期（中間期）決算短信〔日本基準〕(連結)｜11-13 16:00
- 📌 6407 ＣＫＤ｜通期連結業績予想の修正、剰余金の配当 (中間配当) 及び期末配当予想の修正に関するお知らせ｜11-13 16:00
- 📌 6407 ＣＫＤ｜Notice of Revisions in Consolidated Financial Forecasts for the Full Fiscal Year, Dividends of Surplus (Interim Dividends) and Revisions of Year-end D｜11-13 16:00
- 📌 6481 ＴＨＫ｜Notice Regarding the Revision of Financial Forecasts｜11-13 15:30
- 📌 6481 ＴＨＫ｜業績予想の修正に関するお知らせ｜11-13 15:30
- 📊 6481 ＴＨＫ｜Consolidated Financial Results for the Nine Months Ended September 30, 2026 under IFRS｜11-13 15:30
- 📊 6481 ＴＨＫ｜2026年12月期 第3四半期決算短信〔ＩＦＲＳ〕（連結）｜11-13 15:30
- 🔁 6676 ＢＵＦ｜自己株式立会外買付取引（ToSTNeT-３）、自己株式の公開買付け及び市場買付けに関するお知らせ｜11-13 16:30
- 📌 6676 ＢＵＦ｜自己株式取得に係る事項の一部変更（取得枠の拡大）に関するお知らせ｜11-13 16:30
- 📌 6676 ＢＵＦ｜剰余金の配当（中間配当）に関するお知らせ｜11-13 16:30
- 📌 6676 ＢＵＦ｜2027年３月期　第２四半期決算説明資料｜11-13 16:30
- 📊 6676 ＢＵＦ｜2027年３月期　第２四半期（中間期）決算短信〔日本基準〕（連結）｜11-13 16:30
- 📌 6736 サン電子｜Notice Regarding the Personnel Changes｜11-13 16:00
- 📌 6736 サン電子｜人事異動に関するお知らせ｜11-13 16:00
- 📌 6736 サン電子｜Notice Regarding Receipt of Written Notice of Reassessment from the Nagoya Regional Taxation Bureau｜11-13 16:00
- 📊 6736 サン電子｜Supplementary Presentation: Financial Results for the Six Months Ended September 30, 2026｜11-13 16:00
- 📌 6736 サン電子｜Notice Concerning Revision of Full-year Financial Forecasts｜11-13 16:00
- 📊 6736 サン電子｜Consolidated Financial Results for the Six Months Ended September 30, 2026｜11-13 16:00
- 📌 6736 サン電子｜名古屋国税局からの更正通知書受領に関するお知らせ｜11-13 16:00
- 📌 6736 サン電子｜2027年３月期 第２四半期（中間期）決算補足説明資料｜11-13 16:00
- 📌 6736 サン電子｜通期業績予想の修正に関するお知らせ｜11-13 16:00
- 📊 6736 サン電子｜2027年３月期 第２四半期（中間期）決算短信〔日本基準〕(連結)｜11-13 16:00
- 📊 6742 京三｜[Summary]Summary of Consolidated Financial Results for the Six Months Ended September 30, 2026 (Under Japanese GAAP)｜11-13 15:30
- 📌 6742 京三｜Notice Regarding Differences Between Earnings Forecasts and Actual Results and Revision of Full-Year Earnings Forecasts and Dividend Forecast｜11-13 15:30
- 📌 6742 京三｜2027年３月期第２四半期累計期間（中間期）業績予想値と実績値との差異ならびに通期業績予想および配当予想の修正（増配）に関するお知らせ｜11-13 15:30
- 📊 6742 京三｜2027年３月期　第２四半期（中間期）決算短信〔日本基準〕(連結)｜11-13 15:30
- 📊 6768 タムラ｜Financial Results Presentation for FY2026 2Q｜11-13 15:00
- 📌 6768 タムラ｜2027年3月期第2四半期（中間期）決算概要｜11-13 15:00
- 📌 6804 ホシデン｜Notice regarding Adjustment of Conversion Price for Zero Coupon Convertible Bonds due 2031｜11-13 16:00
- 📊 6804 ホシデン｜Notice Regarding Differences Between Financial Results Forecasts and Actual Financial  Results for the Six Months Ended September 30,2026｜11-13 16:00
- 📊 6804 ホシデン｜Consolidated Financial Results for the Six Months Ended September 30, 2026｜11-13 16:00
- 📌 6804 ホシデン｜2031年満期ユーロ円建転換社債型新株予約権付社債の転換価額の調整に関するお知らせ｜11-13 16:00
- 📌 6804 ホシデン｜第２四半期（中間期）業績予想と実績値との差異に関するお知らせ｜11-13 16:00
- 📊 6804 ホシデン｜2027年３月期第２四半期（中間期）決算短信〔日本基準〕(連結)｜11-13 16:00
- 📊 6834 精工技研｜2027年3月期　第2四半期(中間期)決算短信〔日本基準〕(連結)｜11-13 16:00
- 📌 6834 精工技研｜2027年3月期　通期連結業績予想の修正に関するお知らせ｜11-13 16:00
- 📌 6834 精工技研｜剰余金の配当(中間配当)に関するお知らせ｜11-13 16:00
- 📌 6840 ＡＫＩＢＡ｜2027年３月期 通期連結業績予想の公表に関するお知らせ｜11-13 16:00
- 📊 6840 ＡＫＩＢＡ｜2027年３月期 第２四半期（中間期）決算短信〔日本基準〕（連結）｜11-13 16:00
- 📊 6877 ＯＢＡＲＡＧ｜2026年９月期決算短信〔日本基準〕(連結)｜11-13 17:00
- 📌 6877 ＯＢＡＲＡＧ｜投資単位の引下げに関する考え方及び方針等について｜11-13 17:00
- 📊 6877 ＯＢＡＲＡＧ｜[Summary] Financial Results for the Year Ended September 30, 2026｜11-13 17:00
- 📊 6925 ウシオ電｜(Corrections / Corrections of Numerical Data) Consolidated Financial Results for the Year Ended March 31,2026 [under Japanese GAAP]｜11-13 15:45
- 📊 6925 ウシオ電｜(訂正・数値データ訂正) 「2026年３月期決算短信〔日本基準〕（連結）」の一部訂正について｜11-13 15:45
- 📊 7318 セレンＨＤ｜Supplementary Material for Q2 FY2027 Financial Results｜11-13 15:30
- 📊 7318 セレンＨＤ｜Consolidated Financial Results for the Six Months Ended September 30, 2026 (Under Japanese GAAP)｜11-13 15:30
- 📊 7318 セレンＨＤ｜2027年３月期 第２四半期（中間期）決算短信補足資料｜11-13 15:30
- 📊 7318 セレンＨＤ｜2027年３月期 第２四半期（中間期）決算短信〔日本基準〕（連結）｜11-13 15:30
- 📊 7322 三十三ＦＧ｜[Summary]Consolidated Financial Results for the Six Months Ended September 30, 2026 (Under Japanese GAAP)｜11-13 15:00
- 📊 7322 三十三ＦＧ｜2027年３月期 第２四半期（中間期）決算短信〔日本基準〕(連結)｜11-13 15:00
- 📌 7384 プロクレＨＤ｜Notice Concerning the Establishment of Specialized Investment Subsidiary at Subsidiary Bank｜11-13 15:30
- 📊 7384 プロクレＨＤ｜Notice Concerning Differences Between Consolidated Financial Results Forecasts and Actual Results for the Six Months Ended September 30_ 2026｜11-13 15:30
- 📊 7384 プロクレＨＤ｜[Summary] Consolidated Financial Results for the Six Months Ended September 30, 2026 (Under Japanese GAAP)｜11-13 15:30
- 📌 7384 プロクレＨＤ｜子銀行における投資専門子会社の設立のお知らせ｜11-13 15:30
- 📊 7384 プロクレＨＤ｜2027年３月期 第２四半期（中間期）決算短信〔日本基準〕(連結)｜11-13 15:30
- 📌 7384 プロクレＨＤ｜2027年３月期第２四半期(中間期)連結業績予想と実績値との差異に関するお知らせ｜11-13 15:30
- 📌 7744 ノーリツ鋼機｜Notice Concerning Revision to Dividend Forecast｜11-13 15:30
- 📌 7744 ノーリツ鋼機｜[Summary]Summary of Financial Statements for the Third Quarter of the Fiscal Year Ending December 31, 2026 [IFRS] (Consolidated）｜11-13 15:30
- 📌 7744 ノーリツ鋼機｜配当予想の修正に関するお知らせ｜11-13 15:30
- 📊 7744 ノーリツ鋼機｜FY26 3Q Supplementary Information to the Financial Results｜11-13 15:30
- 📌 7744 ノーリツ鋼機｜2026年12月期 第3四半期決算補足説明資料｜11-13 15:30
- 📊 7744 ノーリツ鋼機｜2026年12月期 第3四半期決算短信〔IFRS〕（連結）｜11-13 15:30
- 📊 7747 朝日インテク｜Financial Results for the 1st Quarter of FYE June 2027｜11-13 15:30
- 📌 7747 朝日インテク｜2027年6月期第1四半期決算説明資料｜11-13 15:30
- 📊 7747 朝日インテク｜Consolidated Financial Results for the Three Months Ended September 30, 2026 (Under Japanese GAAP)｜11-13 15:30
- 📊 7747 朝日インテク｜2027年６月期第１四半期決算短信〔日本基準〕(連結)｜11-13 15:30
- 📌 8253 クレセゾン｜Corporate Governance Report｜11-13 15:50
- 📌 8253 クレセゾン｜コーポレート・ガバナンスに関する報告書 2026/11/13｜11-13 15:33
- 📌 8253 クレセゾン｜Notice Regarding Revision to the Year-End Dividend Forecast｜11-13 15:30
- 📌 8253 クレセゾン｜期末配当予想の修正に関するお知らせ｜11-13 15:30
- 📌 8253 クレセゾン｜Notification Regarding the Revision of Forecast of Business Results for the Full Fiscal Year Ending March 31, 2027 (Consolidated and Non-Consolidated)｜11-13 15:30
- 📌 8253 クレセゾン｜Notice Regarding Resolution on Details of Stock Buyback and Cancellation of Treasury Shares｜11-13 15:30
- 📌 8253 クレセゾン｜自己株式取得に係る事項の決定及び自己株式消却に係る事項の決定に関するお知らせ｜11-13 15:30
- 📊 8253 クレセゾン｜[Summary]Consolidated Financial Results for the Six Months Ended September 30, 2026 (Under IFRS)｜11-13 15:30
- 📌 8253 クレセゾン｜2027年３月期通期（連結・個別）業績予想の修正に関するお知らせ｜11-13 15:30
- 📊 8253 クレセゾン｜2027年３月期 第２四半期（中間期）決算短信〔ＩＦＲＳ〕（連結）｜11-13 15:30
- 📊 8344 山形銀｜[Summary]Consolidated Financial Results for the Six Months Ended September 30, 2026 (Under Japanese GAAP)｜11-13 15:30
- 📊 8344 山形銀｜2027年３月期 第２四半期（中間期）決算短信〔日本基準〕（連結）｜11-13 15:30
- 📊 8360 山梨銀｜Notice Concerning Differences Compared with Financial Results for the Six Months Ended September 30, 2025｜11-13 14:00
- 📊 8360 山梨銀｜Consolidated Financial Results for the Six Months Ended September 30, 2026 (Under Japanese GAAP)｜11-13 14:00
- 📌 8360 山梨銀｜前期実績との差異に関するお知らせ｜11-13 14:00
- 📊 8360 山梨銀｜2027年3月期 第2四半期（中間期）決算短信〔日本基準〕(連結)｜11-13 14:00
- 📌 8361 大垣共立｜Notice Concerning Revision to Year-End Dividend Forecast (Dividend Increase)｜11-13 16:00
- 📌 8361 大垣共立｜期末配当予想の修正（増配）に関するお知らせ｜11-13 16:00
- 📊 8361 大垣共立｜Notice of Difference of Financial Results from Results for the Same Period of the Previous Fiscal Year｜11-13 16:00
- 📊 8361 大垣共立｜[Summary] Consolidated Financial Results for the Six Months Ended September 30, 2026 (Under Japanese GAAP)｜11-13 16:00
- 📌 8361 大垣共立｜前年同期実績との差異に関するお知らせ｜11-13 16:00
- 📊 8361 大垣共立｜2027年3月期 第２四半期（中間期）決算短信〔日本基準〕（連結）｜11-13 16:00
- 📊 8364 清水銀｜[Summary]Consolidated Financial Results for the Six Months Ended September 30, 2026 (Under Japanese GAAP)｜11-13 15:30
- 📊 8364 清水銀｜2027年3月期第2四半期(中間期)決算短信〔日本基準〕(連結)｜11-13 15:30
- 📌 8366 滋賀銀｜Notice Regarding "Revision of Earnings Forecasts" and "Determination of Dividends from Surplus (Interim Dividends)" and "Revision of Year-end Dividend｜11-13 15:00
- 📊 8366 滋賀銀｜Consolidated Financial Results for the Six Months Ended September 30, 2026 (Under Japanese GAAP)｜11-13 15:00
- 📌 8366 滋賀銀｜「業績予想の修正」ならびに「剰余金の配当（中間配当）の決定」および「期末配当予想の修正（増配）」に関するお知らせ｜11-13 15:00
- 📊 8366 滋賀銀｜2027年3月期 第2四半期（中間期）決算短信〔日本基準〕（連結）｜11-13 15:00
- 📌 8388 阿波銀｜[Summary]Notice Concerning Dividend of Surplus (Interim Dividend)｜11-13 14:00
- 📊 8388 阿波銀｜[Summary]Consolidated Financial Results for the Six Months Ended September 30, 2026 [Under Japanese GAAP]｜11-13 14:00
- 📌 8388 阿波銀｜剰余金の配当（中間配当）に関するお知らせ｜11-13 14:00
- 📊 8388 阿波銀｜2027年３月期 第２四半期(中間期)決算短信〔日本基準〕(連結)｜11-13 14:00
- 📌 8522 名古屋銀｜Notice Concerning Dividend from Surplus (Interim Dividend) and Revision to the Forecast of Year-End Dividend (Dividend Increase)｜11-13 14:40
- 📌 8522 名古屋銀｜剰余金の配当（中間配当）及び期末配当予想の修正（増配）に関するお知らせ｜11-13 14:40
- 📌 8522 名古屋銀｜Notice Concerning Revisions to Earnings Forecasts｜11-13 14:40
- 📌 8522 名古屋銀｜業績予想の修正に関するお知らせ｜11-13 14:40
- 📊 8522 名古屋銀｜Consolidated Financial Results for the Six Months Ended September 30, 2026 (Under Japanese GAAP)｜11-13 14:40
- 📊 8522 名古屋銀｜2027年３月期 第２四半期（中間期）決算短信〔日本基準〕（連結）｜11-13 14:40
- 📊 8524 北洋銀｜[Summary]Consolidated Financial Results for the Six Months Ended September 30, 2026 (Under Japanese GAAP)｜11-13 14:00
- 📊 8524 北洋銀｜2027年３月期　第２四半期（中間期）決算短信〔日本基準〕（連結）｜11-13 14:00
- 📌 8600 トモニＨＤ｜Notice Concerning Determination of Dividends of Surplus（Interim Dividend）and Revision of Year-end Dividend Forecast（Dividend Increase）｜11-13 14:30
- 📌 8600 トモニＨＤ｜剰余金の配当（中間配当）の決定及び期末配当予想の修正（増配）に関するお知らせ｜11-13 14:30
- 📌 8600 トモニＨＤ｜Notice Concerning Determination of Matters Related to Acquisition of Own Shares｜11-13 14:30
- 📌 8600 トモニＨＤ｜自己株式取得に係る事項の決定に関するお知らせ｜11-13 14:30
- 📊 8600 トモニＨＤ｜Consolidated Financial Results for the Six Months Ended September30,2026｜11-13 14:30
- 📊 8600 トモニＨＤ｜令和9年3月期 第2四半期（中間期）決算短信〔日本基準〕（連結）｜11-13 14:30
- 📊 8713 フィデアＨＤ｜［Summary］Consolidated Financial Results for the Six Months Ended September 30, 2026 (Under Japanese GAAP)｜11-13 12:30
- 📊 8713 フィデアＨＤ｜2027年3月期 第2四半期（中間期）決算短信〔日本基準〕（連結）｜11-13 12:30
- 📊 8944 ランビジネス｜2026年9月期決算短信〔日本基準〕（連結）｜11-13 15:30
- 📊 9552 クオンツ総研｜Consolidated Financial Results for the Fiscal Year Ended September 30, 2026  (Under IFRS)｜11-13 15:30
- 📊 9552 クオンツ総研｜2026年9月期　決算短信〔ＩＦＲＳ〕(連結)｜11-13 15:30
- 📌 9552 クオンツ総研｜Presentation Materials for the year ended September 30, 2026｜11-13 15:30
- 📌 9552 クオンツ総研｜2026年9月期 通期決算説明資料｜11-13 15:30
- 📌 9552 クオンツ総研｜Notice Regarding Reduction in Capital Reserve｜11-13 15:30
- 📌 9552 クオンツ総研｜Notice Regarding Provision for Allowance for Doubtful Accounts (Non-consolidated)｜11-13 15:30
- 📌 9552 クオンツ総研｜資本準備金の額の減少に関するお知らせ｜11-13 15:30
- 📌 9552 クオンツ総研｜貸倒引当金繰入額（個別）の計上に関するお知らせ｜11-13 15:30
- 📌 9554 エイビック｜配当方針の変更及び2027年９月期の配当予想（初配）に関するお知らせ｜11-13 15:30
- 📌 9554 エイビック｜2026年９月期 通期決算説明資料 事業計画及び成長可能性に関する事項｜11-13 15:30
- 📊 9554 エイビック｜2026年９月期 決算短信〔日本基準〕（連結）｜11-13 15:30
- 📊 9722 藤田観｜[Delayed]Financial Results for the Nine Months Ended September 30, 2026｜11-13 15:30
- 📊 9722 藤田観｜[Updated][Summary]Consolidated Financial Results for the Nine Months Ended September 30, 2026 [Japanese GAAP]｜11-13 15:30
- 📌 3591 ワコールＨＤ｜Announcement Regarding Purchase of Treasury Stock through Tokyo Stock Exchange Off-Auction Treasury Stock Repurchase Trading (ToSTNeT-3)｜11-13 16:30
- 🔁 3591 ワコールＨＤ｜自己株式立会外買付取引（ToSTNeT-3）による自己株式の買付けに関するお知らせ｜11-13 16:30
- 📦 6080 Ｍ＆Ａキャピ｜神戸新聞社と業務提携のお知らせ｜11-13 15:30
- 📌 1435 ロボホーム｜[Delayed]Notice Concerning the Establishment of a Subsidiary(Second-tier Subsidiary)by a Consolidated  Subsidiary and Change in a Specified Subsidiary｜11-13 15:30
- 📌 1928 積水ハウス｜Notice Concerning Commencement of Tender Offer for Gifu landscape architect Co., Ltd. (Securities Code: 1438)｜11-13 17:00
- 📌 1928 積水ハウス｜株式会社岐阜造園（証券コード：1438）に対する公開買付けの開始に関するお知らせ｜11-13 17:00
- 📌 1975 朝日工｜Notice of Application for Extension of the Deadline for Submission of the Half-year Report for the Fiscal Year Ending March 2027｜11-13 17:00
- 📌 1975 朝日工｜2027年３月期半期報告書の提出期限延長に係る承認申請書提出のお知らせ｜11-13 17:00
- 📌 218A リベラウェア｜Liberaware、千葉県のオープンイノベーションプログラム「PORT」における共創パートナーが決定～ロボット・カメラと地域人材が連携する仕組みを共創～｜11-13 13:00
- 📌 276A ククレブ｜独立役員届出書｜11-13 16:30
- 📌 276A ククレブ｜Notice Concerning Disposition of Real Estate for Sale and Provision of CRE Services｜11-13 15:30
- 📌 276A ククレブ｜販売用不動産の売却および業務受託に関するお知らせ｜11-13 15:30
- 📌 3077 ホリイフード｜2026年11月期 月次売上速報（10月度）のお知らせ｜11-13 16:00
- 📌 3077 ホリイフード｜組織変更及び人事異動に関するお知らせ｜11-13 16:00
- 📌 3106 クラボウ｜コーポレート・ガバナンスに関する報告書 2026/11/13｜11-13 11:35
- 📌 3491 ＧＡテクノ｜三菱地所ハウスネット、「ITANDI 賃貸管理」で入居者管理を電子化｜11-13 10:00
- 📌 3496 アズーム｜（訂正）「2026年９月期決算説明資料」の一部訂正について｜11-13 15:30
- 📌 3696 セレス｜日本経済新聞社「2026年度 脱炭素経営ランキング GX500」に選出｜11-13 15:00
- 📌 3798 ＵＬＳグルプ｜2027年3月期第2四半期（中間期）決算説明会資料｜11-13 10:00
- 📌 4063 信越化｜Notice Concerning Decisions Relating to Repurchase of Shares｜11-13 15:30
- 📌 4063 信越化｜自己株式取得に係る事項の決定に関するお知らせ｜11-13 15:30
- 📌 4165 プレイド｜Notice Regarding Unauthorized Access to Our Service｜11-13 17:00
- 📌 4165 プレイド｜当社サービスへの不正アクセスに関するお知らせ｜11-13 17:00
- 📌 428A サイプレス｜（訂正前）第８回定時株主総会招集ご通知（交付書面省略事項）｜11-13 08:00
- 📌 4379 フォトシンス｜2026年12月期第3四半期決算説明会（書き起こし＆質疑応答）｜11-13 15:30
- 📌 4379 フォトシンス｜小売店・飲食店の「諦め時短」に関する実態調査 人手不足による売上機会損失は全国で年間約1,940億円と推計 1店舗あたりで年間240万円｜11-13 11:30
- 📌 4419 フィナＨＤ｜2027年３月期第２四半期決算説明会 動画公開のお知らせ｜11-13 17:00
- 📌 4523 エーザイ｜LEQEMBI Pen (Subcutaneous Formulation of LEQEMBI) Now Available in Japan for Patients with Early Alzheimer’s Disease｜11-13 08:30
- 📌 4523 エーザイ｜「レケンビ」の皮下注製剤「レケンビ皮下注250mg ペン」日本において早期アルツハイマー病治療剤として新発売｜11-13 08:30
- 📌 4765 ＳＢＩＧＡＭ｜「ゴールドマン・サックス社債／ROBOPRO戦略ファンド2026-12」届出のお知らせ｜11-13 10:00
- 📌 4884 クリングル｜2026年９月期 通期決算説明会動画 掲載のお知らせ｜11-13 17:30
- 📌 4884 クリングル｜2026年９月期 通期決算説明会資料｜11-13 16:00
- 📌 4922 コーセーＨＤ｜Notice of Changes in Executives｜11-13 15:30
- 📌 4922 コーセーＨＤ｜役員の異動に関するお知らせ｜11-13 15:30
- 📌 4980 デクセリ｜Dexerials Selected for METI’s Large-Scale Growth Investment Subsidy Program｜11-13 10:30
- 📌 4980 デクセリ｜経済産業省の実施する「大規模成長投資補助金」事業に採択｜11-13 10:30
- 📌 5034 ウネリー｜2027年6月期 第1四半期 決算説明会 質疑応答（要旨）｜11-13 16:00
- 📌 5254 Ａｒｅｎｔ｜2027年6月期 第1四半期 決算説明会 事前質問の回答｜11-13 16:15
- 📌 5599 Ｓ＆Ｊ｜S&J、加速するAIによるサイバー攻撃の高度化・高速化に対応、AIと専門家による「WebアプリソースコードAI診断」の提供を開始｜11-13 12:00
- 📌 6436 アマノ｜Amano Group Corporate Governance Report｜11-13 15:45
- 📌 6436 アマノ｜コーポレート・ガバナンスに関する報告書 2026/11/13｜11-13 15:34
- 📌 6505 東洋電｜コーポレート・ガバナンスに関する報告書 2026/11/13｜11-13 16:00
- 📌 6505 東洋電｜執行役員の異動に関するお知らせ｜11-13 15:30
- 📌 6574 コンヴァノ｜連結子会社であるアクセルマーク株式会社の第三者割当による第34回新株予約権の引受けに関するお知らせ｜11-13 16:30
- 📌 6574 コンヴァノ｜（開示事項の経過）自己株式の消却に関するお知らせ｜11-13 16:30
- 📌 6651 日東工｜（数値データ訂正）2027年3月期通期業績予想の修正に関するお知らせにおける数値データ(XBRL)の一部訂正について｜11-13 15:30
- 📌 6758 ソニーＧ｜Disposal of Treasury Shares upon Vesting of Restricted Stock Units (“RSUs”)｜11-13 15:30
- 📌 6758 ソニーＧ｜譲渡制限付株式ユニット（RSU）の権利確定に伴う自己株式処分に関するお知らせ｜11-13 15:30
- 📌 6857 アドテスト｜Semi-Annual Securities Report (FY2026)｜11-13 12:00
- 📌 6918 アバール｜コーポレート・ガバナンスに関する報告書 2026/11/13｜11-13 10:21
- 📌 6971 京セラ｜Semiannual Securities Report (The First Half of the 73rd Business Term)｜11-13 16:00
- 📌 7735 スクリン｜Corporate Governance Report｜11-13 16:00
- 📌 7735 スクリン｜コーポレート・ガバナンスに関する報告書 2026/11/13｜11-13 15:29
- 📌 8084 ＲＹＯＤＥＮ｜2027年3月期第2四半期（中間期）　決算説明会資料｜11-13 15:30
- 📌 8159 立花エレ｜Notice Concerning Exhibition at EdgeTech+ 2026｜11-13 10:30
- 📌 8159 立花エレ｜「EdgeTech+2026」出展のお知らせ｜11-13 10:30
- 📌 8334 群馬銀｜Notice Concerning the Granting of Voting Rights at the Annual General Meeting of Shareholders in June 2027 (scheduled) to Shareholders｜11-13 13:00
- 📌 8334 群馬銀｜2027年６月（予定）定時株主総会における基準日後株主への議決権付与に関するお知らせ｜11-13 13:00
- 📌 8334 群馬銀｜Notice Concerning Tentative Appointment of Directors and Change in Representative Directors of the Holding Company upon Business Integration｜11-13 13:00
- 📌 8334 群馬銀｜株式会社群馬銀行と株式会社第四北越フィナンシャルグループの経営統合後の持株会社における取締役の内定および代表取締役の異動｜11-13 13:00

## 総当りゲート
### 5手法（268）
- PASS（37）: 1820 1979 2109 2379 3091 3116 3282 3843 4379 4434 446A 4743 4768 5101 558A 6349 6367 6436 6505 6532 6750 6758 6988 7148 7678 7942 8133 8198 8975 9048 9302 9432 9434 9503 9533 9948 9960
- PASS_DOJI（1）: 3798
- FAIL_UWAHIGE（53）: 147A 1721 1926 1952 1961 268A 276A 3077 3110 3131 3479 3569 3591 3696 3994 4028 4042 4053 4088 4176 4377 4503 4565 4746 5034 5136 5246 5831 6071 618A 6370 6418 6473 6521 6524 6804 6923 6960 7177 7366 7433 8154 8253 8522 8616 8698 8704 9204 9468 9554 9560 9722 9766
- FAIL_INSEN（177）: 1417 1435 167A 1944 1946 1951 1960 1963 1975 1982 255A 262A 2760 2802 2930 2975 3036 3103 3105 3374 3433 3436 3445 3498 3556 3612 3915 4008 4021 4022 4047 4058 4062 4063 4203 4205 4216 4272 4286 4293 4368 4410 4417 4471 4634 4771 4933 4966 4971 4973 4980 5018 5019 5021 5027 505A 5132 5137 5186 5208 5301 5302 5310 5331 5333 5344 5384 5444 5463 5537 5602 5631 5703 5706 5711 5757 5801 5821 5832 5844 6055 6135 6146 6227 6235 6268 6278 6284 6302 6323 6324 6332 6336 6340 6366 6368 6379 6407 6448 6454 6471 6479 6481 6501 6516 6588 6590 6613 6617 6632 6645 6651 6652 6668 6674 6723 6724 6741 6752 6754 6762 6777 6779 6787 6807 6810 6845 6857 6875 6918 6925 6941 6943 6952 6965 6971 6981 7004 7167 7186 7220 7276 7278 7322 7381 7384 7721 7729 7731 7733 7735 7995 8032 8035 8084 8098 8304 8334 8345 8354 8359 8366 8370 8381 8386 8393 8399 8524 8600 9072 9110 9301 9824 9902 9934 9962 9984
### グランビル（216）
- PASS（45）: 150A 1911 1928 1941 2206 2384 2811 2897 3092 3182 3405 3563 4166 417A 4208 4540 4549 4848 4922 5105 5233 5252 5256 6036 6191 6412 7606 7921 8016 8056 8113 8160 8801 8803 9006 9045 9278 9401 9404 9418 9697 9735 9837 9842 9956
- PASS_DOJI（6）: 3042 3496 3673 4258 5599 6250
- FAIL_UWAHIGE（51）: 1436 153A 2267 2502 3002 336A 338A 3491 3565 3793 3935 3968 3993 4045 4169 4240 428A 4373 4375 4396 4507 4523 4534 4552 4568 456A 4765 4884 4902 4912 5985 6080 6470 6592 6769 6947 7175 7213 7380 7480 7725 7734 8255 8364 8410 8739 9304 9509 9536 9552 9742
- FAIL_INSEN（114）: 1878 2488 2489 2492 278A 2962 3040 3106 3156 3371 3549 3687 3691 3692 3762 3778 3850 3851 3891 3927 3964 4005 4025 4044 4075 4100 4180 4206 436A 4398 4401 4403 4419 4432 4440 4443 4498 4554 460A 4617 4667 4674 477A 479A 4968 5036 5184 5243 5254 5367 5381 5532 5892 6027 6099 6138 6203 6317 6328 6490 6508 6523 6570 6574 6676 6736 6742 6744 6745 6768 6834 6840 6862 6877 6890 6904 6958 6963 7184 7256 7269 7609 7715 7744 7747 7806 7826 7970 8012 8051 8061 8137 8159 8167 8344 8360 8361 8368 8377 8388 8392 8395 8551 8609 8697 8713 8804 8944 9025 9075 9163 9166 9308 9869
### 変化点（22）
- PASS（4）: 3923 3989 5582 593A
- FAIL_UWAHIGE（4）: 218A 4071 4475 478A
- FAIL_INSEN（14）: 265A 286A 4011 4165 4259 4478 4483 4488 598A 6785 7318 7695 8151 9343
- 除籍（first_seen から30暦日超・SBIグループ登録解除候補 37件）: 4477 BASE, Inc. 421A Movin' Strategic Career CO.,LTD. 6071 IBJ, Inc. 7567 Sakae Electronics Corp. 9412 SKY Perfect JSAT Corporation 1860 Toda Corporation 8194 Life Corporation 4666 Park24 Co., Ltd. 6753 Sharp Corporation 8174 NIPPON GAS Co., Ltd. 7003 Mitsui ES Holdings Co., Ltd. 1719 HAZAMA ANDO Corporation 3222 United Super Markets Holdings, Inc. 5482 Aichi Steel Corporation 8871 GOLDCREST Co., Ltd. 7713 シグマ光機 6814 古野電 5932 三協立山 1982 日比谷総合設備 8098 稲畑産業 8095 Astena Holdings Co.,Ltd. 6371 Tsubakimoto Chain Co. 5838 Rakuten Bank, Ltd. 6432 竹内製作所 8336 武蔵野銀行 8367 南都銀行 8714 池田泉州ホールディングス 4413 baudroie,inc. 6998 Nippon Tungsten Co., Ltd. 8362 Fukui Bank, Ltd. 8995 Makoto Construction Co,Ltd 5574 ABEJA,Inc. 339A PROGRESS TECHNOLOGIES GROUP INC 4382 HEROZ, Inc. 5803 フジクラ 6136 OSG CORP 9888 UEX LTD

## 機械詳細
- 候補収集: 当夜候補83銘柄（新規20・再指名63）・未マージPR由来0件（直近24hのリモートブランチは main のみ）・dm_*/an_* は spec 未定義のため不使用・熟成由来 1件（9048・PASS）
- 評価506件（プール505＋前夜proposals由来1）・SKIP 0・log 追記1件（2026-11-13）
- ヘッドライン: PASS93件すべてに付与（抜粋なし）・通知の抜粋10件
- gate_history: gate_history/2026-11-13.json を新規作成（verdicts 506件／nominations 83件（新規20・再指名63））
- grades.json: 1092銘柄／609.9KiB（650KB上限のため per/pbr/peg/p52/psr を前夜と同じ表示精度（4/3/3/4/1桁）に丸めて書き出し）
- method_score: 保持55件／null451件
- kabutan 新規取得: 銘柄トップ4件（50件上限・打ち切り0）・profile_cache 総数1063（本夜追加2）・業種埋め戻し0件・残り1件（3480はページに業種表示なし）・業態「未取得」のまま出た件数1
- 業績グレード: 再計算は未実施（キャッシュ値を使用。📊/📢/📉 は recalc_queue へ）・gyoseki history 退避0件
- earnings_log: 総数492／本夜追記82件／リターン補完90項目／日足なしで未補完84件
- pool_bars.json: 508銘柄／433.1KiB
- 鮮度ゲート: 鮮度切れ除外21件・nom_age分布 0-2:166/3-10:221/11+:119・last_seen欠損0件
- 業種: 付与済み497/未付与9（評価銘柄ベース）
- トレンド文脈: ctx 合致65／不一致299／レンジ139／判定不能3・PASS のうち ctx 合致16件・形態が付いた銘柄173件
- 3日ルール: 判定1銘柄・streak≥3 0・streak=2 0・判定不可0
- 業種別PER中央値: 算出できた業種26・spm を写せた銘柄1019件
- 開示の分類別件数（プール＋保有と一致した分）: 📊160・📌247・🔁3・👥1・📢3・📦4
- 権利情報: rights_cache 総数503・本夜の更新0件（T+1/T+2 に権利落ち無し・保有の rights は前回決算後に取得済み）
- 次回決算日: 付与445件／未発表653件・前年同期発表日 付与371件・earnings_calendar.json 1098銘柄/141.1KiB
- STEP 4.8: 実行（week_open=true）
- master.json 変更行数: +13336/-13450（indent=2・往復一致で検出）
