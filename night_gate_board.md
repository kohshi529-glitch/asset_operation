# 夜間ゲート 2026-09-24

## サマリー
- 評価数: 400件（pool内訳398件＋前夜proposals差分）
- PASS数: 64件（うちPASS_DOJI 0件）
- 発注可能提案数: 47件（即時可43／待機4）
- 市場一言: 堅調／半導体主導リスクオン
- 実行モード: 通常モード（base_day=本日、4連休(9/19-23)明けの通常営業日）
- base_day: 2026-09-24
- week_open: false（翌営業日は金曜のため週初判定に該当せず、STEP4.8はスキップ）

## 検証結果
- V1 四者一致: proposals47件=results entry_price47件=模擬テンプレ行47件=通知母数47件 → はい
- V2 PASS収支: PASS64件=発注可能47件(即時可43+待機4)+除外17件(型不一致3/鮮度切れ12/手法不明2)、除外全件order_status記入 → はい
- V3 重複・単一verdict: コード重複0件、verdict単一値 → はい
- V4 valuation_cache static不変更: はい（既存681件のstatic差分0）
- V5 master.json許可キー外不変更: はい（night_gate.*/gyoseki_cache/valuation_cache/profile_cache/earnings_log/pipeline.runs.night_gateのみ変更）
- V6 grade絵文字整合: 本夜更新分(8697)は適合。レガシー42件(取得不可/判定保留の簡略表記・null3件)は本夜のキャッシュ再計算トリガー対象外のため据え置き
- V7 board必須セクション: サマリー/検証結果/前夜の結果/模擬テンプレ/PASS内訳すべて存在（week_open=falseのため📅今週のカタリストは省略）→ はい
- V8 模擬テンプレ書式: ｜後ろ文字なし/単元記載あり/カンマなし → はい
- V9 gate_history整合: verdicts/nominations除去後にnight_gate_today.jsonと完全一致 → はい
- V10 base_day整合: results/night_gate_today.json/gate_historyファイル名/模擬テンプレ1行目すべて2026-09-24 → はい
- V11 書き出し整形: git diff --numstat master.json = +11163/-13460（indent=2検出）。目安5,000行を超過するが、night_gate.results全置換(398件×新設trend/headline項目)由来の正当な内容量であり全体再フォーマットではない。過去同型run(2026-09-14/16/18)も+12,000〜+14,000/-11,000〜-12,000で同水準に推移しており本夜も同傾向 → はい（過大でない・正当）
- V12 並び順: proposals/模擬テンプレ/results抜粋 すべてSTEP5.2(1)キーで厳密一致 → はい
- V13 grades.json: 681銘柄/251KB、meta.n=stocks件数一致、gy∪va和集合一致、300KB以内、全銘柄nx保持 → はい
- V14 method_score: 出所不明0件・写し間違い0件（保持数/手法別内訳は機械詳細参照） → はい
- V15 ヘッドライン網羅性: PASS64件中64件に付与（欠落0件）・5キー完備・調子/水準/戦略/いまへの「未取得」混入はgyoseki_cacheの正規フラグ由来15件(組み立て不具合ではない、詳細は機械詳細) → はい
- V16 記録の蓄積: 本夜📊決算発表0件(pool/holdings該当なし)、earnings_log grade_before順序違反0件、gyoseki history4件超過0件、earnings_log 14件(≤1200) → はい
- V17 pool_bars/3日ルール: 400銘柄/340KB、最大20件・日付昇順・先読みゼロ、保有3銘柄すべてbars収録、3日ルール判定3銘柄全件streak記録 → はい
- V18 指名鮮度ゲート: 鮮度切れ除外全件nom_age>10、誤除外0件、全results nom_age保持 → はい
- V19 記録の凍結: gate_history verdicts400件(＝評価400件)、nominations61件(新規8/再指名53)、写し漏れ0件、profile_cache既存gyotai/fetched_at不変更 → はい

## 保有アラート
- 保有3銘柄・アラート3件（詳細は通知）

## 前夜の結果
PL5口座への正式な反映は週次①-11の採点で行われる。ここは参考情報。

- 前夜2026-09-18の提案63件 → 約定35・不約定28・判定不能0
- 上位5件:
  - 6928 momentum 約定2976.0円 → 終値3115.0円（+4.67%）
  - 6336 reversal 約定1424.0円 → 終値1483.0円（+4.14%）
  - 186A reversal 約定1153.0円 → 終値1190.0円（+3.21%）
  - 6866 changepoint 約定10180.0円 → 終値10480.0円（+2.95%）
  - 4187 reversal 約定4100.0円 → 終値4210.0円（+2.68%）
- 下位3件:
  - 479A momentum 約定2259.0円 → 終値2188.0円（-3.14%）
  - 4667 changepoint 約定3410.0円 → 終値3260.0円（-4.40%）
  - 9343 changepoint 約定800.0円 → 終値800.0円（+0.00%）

## 模擬テンプレ
```
# base_day 2026-09-24 ／ 提案47件
# 使い方: 参戦する0〜3銘柄の行だけをコピーし、｜の後ろに参戦理由を書いてポジション株PJへ送る。
# 選ばなかった行は送らなくてよい（全行に理由を書く必要はない）。見送りは末尾の1行で足りる。
# 特定銘柄を理由つきで見送る場合のみ『模擬 見送り {code} ｜{理由}』を送る。
模擬 5137 kenmo_momentum 逆指値319 SL298.92 単元100 ｜
模擬 3723 kenmo_momentum 逆指値2980 SL2800.26 単元100 ｜
模擬 421A granville_oshime 逆指値4015 SL3769.4 単元100 ｜
模擬 6838 kenmo_momentum 逆指値1440 SL1352.66 単元100 ｜
模擬 4047 choruko_reversal 指値2400 SL2036 単元100 ｜
模擬 3465 choruko_reversal 指値3295 SL3215 単元100 ｜
模擬 7730 choruko_reversal 指値1459 SL1437 単元100 ｜
模擬 6523 choruko_reversal 指値1395 SL1276 単元100 ｜
模擬 5333 choruko_reversal 指値5366 SL4964 単元100 ｜
模擬 6806 choruko_reversal 指値24920 SL23685 単元100 ｜
模擬 8923 choruko_reversal 指値1717 SL1665 単元100 ｜
模擬 6113 choruko_reversal 指値2486 SL2271.5 単元100 ｜
模擬 7731 choruko_reversal 指値1858.5 SL1682.5 単元100 ｜
模擬 5602 choruko_reversal 指値1659 SL1584 単元100 ｜
模擬 7956 choruko_reversal 指値2027.5 SL1940.5 単元100 ｜
模擬 2875 choruko_reversal 指値9722 SL9563 単元100 ｜
模擬 2685 choruko_reversal 指値3170 SL3100 単元100 ｜
模擬 8976 choruko_reversal 指値306500 SL301500 単元1 ｜
模擬 5110 choruko_reversal 指値2031.5 SL1985.5 単元100 ｜
模擬 8984 choruko_reversal 指値113700 SL109800 単元1 ｜
模擬 8151 granville_rebound 逆指値1900 SL1785.06 単元100 ｜
模擬 6706 granville_rebound 逆指値3385 SL3177.2 単元100 ｜
模擬 9470 granville_tenkan 逆指値1074 SL1008.62 単元100 ｜
模擬 7276 granville_tenkan 逆指値2675.5 SL2514.03 単元100 ｜
模擬 4272 granville_tenkan 逆指値2136.5 SL2007.37 単元100 ｜
模擬 9987 granville_tenkan 逆指値5428 SL5092.92 単元100 ｜
模擬 4694 granville_tenkan 逆指値3695 SL3468.6 単元100 ｜
模擬 1982 granville_tenkan 逆指値3275 SL3073.8 単元100 ｜
模擬 4967 granville_tenkan 逆指値5902 SL5538.48 単元100 ｜
模擬 6834 granville_oshime 指値5253.94 SL5227.8 単元100 ｜
模擬 2760 granville_oshime 指値4130.95 SL4110.4 単元100 ｜
模擬 3040 granville_oshime 指値2389.25 SL2377.36 単元100 ｜
模擬 7609 granville_oshime 指値4061.41 SL4041.2 単元100 ｜
模擬 4968 granville_oshime 指値2196.69 SL2185.76 単元100 ｜
模擬 6570 granville_oshime 指値3764.53 SL3745.8 単元100 ｜
模擬 8022 granville_oshime 指値4069.04 SL4048.8 単元100 ｜
模擬 6958 granville_oshime 指値755.8 SL752.04 単元100 ｜
模擬 6134 granville_rebound 指値7399 SL6595 単元100 ｜
模擬 6336 granville_rebound 指値1483 SL1316 単元100 ｜
模擬 6470 granville_rebound 指値1141 SL1053 単元100 ｜
模擬 6952 granville_rebound 指値2183 SL2037 単元100 ｜
模擬 3093 granville_rebound 指値1977 SL1873 単元100 ｜
模擬 3774 granville_rebound 指値3443 SL3382 単元100 ｜
模擬 5108 granville_rebound 指値3801 SL3698 単元100 ｜
模擬 4543 granville_rebound 指値2274.5 SL2228.5 単元100 ｜
模擬 4203 granville_rebound 指値8030 SL7666 単元100 ｜
模擬 8697 changepoint 指値2274 SL2182.5 単元100 🔒 ｜
模擬 見送り ｜
```

## PASS内訳
PASS 64件 = 発注可能 47件（即時可43/待機4） + 除外 17件（型不一致3/材料後出し0/鮮度切れ12/その他2[手法ブランチ不明]）

除外銘柄一覧:
- 9560 PROGRIT, Inc.｜⛔提案なし(指名鮮度切れ 16営業日)
- 4971 MEC Company Ltd.｜⛔提案なし(指名鮮度切れ 15営業日)
- 6235 オプトラン｜⛔提案なし(指名鮮度切れ 14営業日)
- 6856 Horiba, Ltd.｜⛔提案なし(指名鮮度切れ 16営業日)
- 7966 Lintec Corporation｜⛔提案なし(指名鮮度切れ 14営業日)
- 6479 ミネベア｜⛔提案なし(指名鮮度切れ 14営業日)
- 6951 日本電子｜⛔提案なし(指名鮮度切れ 14営業日)
- 1436 グリーンエナジー＆カンパニー｜⛔提案なし(手法ブランチ不明)
- 2983 アールプランナー｜⛔提案なし(手法ブランチ不明)
- 7806 Ｇ−ＭＴＧ｜⛔型不一致: 既に支持帯以下
- 3498 霞ヶ関キャピタル｜⛔型不一致: 既に支持帯以下
- 2384 SBS Holdings Inc｜⛔提案なし(指名鮮度切れ 13営業日)
- 8005 Scroll Corporation｜⛔型不一致: 既に支持帯以下
- 7453 Ryohin Keikaku Co., Ltd.｜⛔提案なし(指名鮮度切れ 12営業日)
- 6125 Okamoto Machine Tool Works,Ltd.｜⛔提案なし(指名鮮度切れ 17営業日)
- 3405 Kuraray Co., Ltd.｜⛔提案なし(指名鮮度切れ 15営業日)
- 5310 Toyo Tanso Co., Ltd.｜⛔提案なし(指名鮮度切れ 14営業日)

## 5手法銘柄
- 5137 Smart Drive Co. Ltd.｜kenmo_momentum｜🚀確変(12/13)｜💎割安(6.0/7)｜PASS｜316.0円｜💰31,600円｜momentum319/SL298.92｜⚠日程不明
  > 📌【業態】モビリティデータ活用の車両管理サービス提供。自動車、保険会社向け支援も。
  > 【いま】終値316円・直近5日+2.93%（材料未確認）
  > 【調子】🚀確変（12/13）
  > 【水準】💎割安（6.0/7）— PER13.2倍・PEG0.14・52週36% ／ 💰単元3.2万円
  > 【戦略】当日高値超えの逆指値319.0円で順張り参戦を検討。上限322.19円・SL298.92円目安
- 5254 Arent｜kenmo_momentum｜🚀確変(12/13)｜—｜FAIL_UWAHIGE｜4130.0円｜💰—｜—｜
- 3723 Nihon Falcom Corporation｜kenmo_momentum｜🚀確変(11/13)｜⚪妥当(3.0/7)｜PASS｜2954.0円｜💰295,400円｜momentum2980/SL2800.26｜⚠日程不明
  > 📌【業態】プレステ用ゲームソフトの開発が主力。RPG系に強み。アプリなどのライセンス事業も。
  > 【いま】終値2,954円・直近5日+9.12%（材料未確認）
  > 【調子】🚀確変（11/13） — E軸=進捗率データ制約のため直近QoQトレンドで代用
  > 【水準】⚪妥当（3.0/7）— PER19.4倍・PEG0.31・52週95% ／ 💰単元29.5万円
  > 【戦略】当日高値超えの逆指値2980.0円で順張り参戦を検討。上限3009.8円・SL2800.26円目安
- 4053 Sun Asterisk, Inc.｜granville_tenkan/kenmo_momentum｜🚀確変(11/13)｜—｜FAIL_UWAHIGE｜504.0円｜💰—｜—｜
- 5027 AnyMind Group Inc.｜kenmo_momentum｜🚀確変(11/13)｜—｜FAIL_UWAHIGE｜820.0円｜💰—｜—｜
- 5136 tripla Co.,Ltd.｜changepoint/kenmo_momentum/stf_kakuhen｜🚀確変(11/13)｜—｜FAIL_INSEN｜2325.0円｜💰—｜—｜
- 5724 Asaka Riken Co., Ltd.｜kenmo_momentum｜🚀確変(11/13)｜—｜FAIL_INSEN｜3155.0円｜💰—｜—｜
- 421A Movin' Strategic Career CO.,LTD.｜granville_oshime/kenmo_momentum｜🔥絶好調(10/13)｜⚪妥当(3.0/7)｜PASS｜3985.0円｜💰398,500円｜momentum4015/SL3769.4｜⚠日程不明
  > 📌【業態】サービス業（人材紹介・転職支援・コンサルティング関連）
  > 【いま】終値3,985円・直近5日+8.73%（材料未確認）
  > 【調子】🔥絶好調（10/13） — D軸データ取得不可(中央値1点採用)
  > 【水準】⚪妥当（3.0/7）— PER19.2倍・PEG0.37・52週83% ／ 💰単元39.9万円
  > 【戦略】当日高値超えの逆指値4015.0円で順張り参戦を検討。上限4055.15円・SL3769.4円目安
- 479A PRONI Inc.｜kenmo_momentum/kenmo_newhigh｜🔥絶好調(10/13)｜—｜FAIL_INSEN｜2188.0円｜💰—｜—｜
- 9252 ラストワンマイル｜kenmo_momentum｜🔥絶好調(10/13)｜—｜FAIL_INSEN｜4115.0円｜💰—｜—｜
- 4479 Makuake, Inc.｜kenmo_momentum｜🔥絶好調(9/13)｜—｜FAIL_UWAHIGE｜987.0円｜💰—｜—｜
- 5537 AlbaLink Co.,Ltd.｜kenmo_momentum｜🔥絶好調(9/13)｜—｜FAIL_UWAHIGE｜3915.0円｜💰—｜—｜
- 9211 f-code Inc.｜granville_tenkan/kenmo_momentum｜🔥絶好調(9/13)｜—｜FAIL_UWAHIGE｜1557.0円｜💰—｜—｜
- 135A VRAIN Solution,Inc.｜kenmo_momentum｜🔥絶好調(8/13)｜—｜FAIL_UWAHIGE｜4915.0円｜💰—｜—｜
- 3915 TerraSky Co., Ltd.｜kenmo_momentum｜🔥絶好調(8/13)｜—｜FAIL_INSEN｜2287.0円｜💰—｜—｜
- 5574 ABEJA,Inc.｜kenmo_momentum｜🔥絶好調(8/13)｜—｜FAIL_INSEN｜3345.0円｜💰—｜—｜
- 5582 GRID Inc.｜kenmo_momentum｜🔥絶好調(8/13)｜—｜FAIL_UWAHIGE｜2103.0円｜💰—｜—｜
- 7352 TWOSTONE&Sons Co.Ltd.｜kenmo_momentum｜🔥絶好調(8/13)｜—｜FAIL_UWAHIGE｜324.0円｜💰—｜—｜
- 558A SQUEEZE Inc.｜kenmo_momentum｜⚡好調(7/13)｜—｜FAIL_UWAHIGE｜6200.0円｜💰—｜—｜
- 5590 NETSTARS Co.｜kenmo_momentum｜⚡好調(7/13)｜—｜FAIL_INSEN｜724.0円｜💰—｜—｜
- 5892 yutori,Inc.｜kenmo_momentum/変化点🔔｜⚡好調(7/13)｜—｜FAIL_UWAHIGE｜2994.0円｜💰—｜—｜
- 6071 ＩＢＪ｜granville_oshime/kenmo_momentum｜⚡好調(7/13)｜—｜FAIL_INSEN｜914.0円｜💰—｜—｜
- 7409 AeroEdge Co.,Ltd｜kenmo_momentum｜⚡好調(7/13)｜—｜FAIL_INSEN｜1503.0円｜💰—｜—｜
- 7678 ASAKUMA CO.｜kenmo_momentum｜⚡好調(7/13)｜—｜FAIL_UWAHIGE｜3875.0円｜💰—｜—｜
- 4477 BASE, Inc.｜kenmo_momentum｜⚡好調(6/13)｜—｜FAIL_INSEN｜337.0円｜💰—｜—｜
- 9560 PROGRIT, Inc.｜kenmo_momentum｜⚡好調(5/13)｜🟢値頃(5.0/7)｜PASS｜913.0円｜💰91,300円｜⛔提案なし(指名鮮度切れ 16営業日)｜📋カルテ窓 10/14(残14営業日)
  > 📌【業態】英語コーチングサービス、サブスクリプション型英語学習サービスの提供を手掛ける。
  > 【いま】終値913円・直近5日+3.63%（材料未確認）
  > 【調子】⚡好調（5/13）
  > 【水準】🟢値頃（5.0/7）— PER10.6倍・PEG0.55・52週45% ／ 💰単元9.1万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 16営業日)）
- 2266 Rokko Butter Co., Ltd.｜kenmo_momentum/granville_tenkan｜⚡好調(5/13)｜—｜FAIL_INSEN｜1102.0円｜💰—｜—｜
- 341A TOYOKOH Inc.｜kenmo_momentum｜✅順調(4/13)｜—｜FAIL_UWAHIGE｜2407.0円｜💰—｜—｜
- 3798 ULS Group Incorporated｜kenmo_momentum｜✅順調(4/13)｜—｜FAIL_INSEN｜570.0円｜💰—｜—｜
- 4743 ITFOR Inc.｜kenmo_momentum｜✅順調(4/13)｜—｜FAIL_INSEN｜1666.0円｜💰—｜—｜
- 505A Geekly,Inc.｜kenmo_momentum｜✅順調(4/13)｜—｜FAIL_INSEN｜1391.0円｜💰—｜—｜
- 6838 Tamagawa Holdings Co.｜kenmo_momentum｜業績データ取得不可｜💎割安(6.0/7)｜PASS｜1436.0円｜💰143,600円｜momentum1440/SL1352.66｜⚠日程不明
  > 📌【業態】高周波回路素子が主力。無線機の計測機器を開発・製販。再生エネ事業も。
  > 【いま】終値1,436円・直近5日-4.46%（材料未確認）
  > 【調子】業績データ取得不可（None/13） — 取得不可
  > 【水準】💎割安（6.0/7）— PER7.1倍・PEG—・52週42% ／ 💰単元14.4万円
  > 【戦略】当日高値超えの逆指値1440.0円で順張り参戦を検討。上限1454.4円・SL1352.66円目安
- 325A TENTIAL, Inc.｜kenmo_momentum｜判定保留(変則決算)｜⚪妥当(3.0/7)｜FAIL_UWAHIGE｜1954.0円｜💰195,400円｜—｜
- 276A CCReB Advisors Inc.｜kenmo_momentum｜判定保留｜—｜FAIL_INSEN｜4270.0円｜💰—｜—｜
- 6492 Okano Valve Mfg. Co., Ltd.｜kenmo_momentum｜判定保留(変則決算)｜—｜FAIL_UWAHIGE｜15100.0円｜💰—｜—｜
- 6862 Minato Holdings Inc.｜kenmo_momentum｜判定保留(変則決算)｜—｜FAIL_UWAHIGE｜5590.0円｜💰—｜—｜
- 3851 Nippon Ichi Software, Inc.｜kenmo_newhigh｜🚀確変(12/13)｜—｜FAIL_INSEN｜1429.0円｜💰—｜—｜
- 269A SAPEET｜kenmo_newhigh｜🚀確変(11/13)｜—｜FAIL_UWAHIGE｜3095.0円｜💰—｜—｜
- 7774 ジャパン・ティッシュエンジニアリング｜kenmo_newhigh｜🚀確変(11/13)｜—｜FAIL_UWAHIGE｜858.0円｜💰—｜—｜
- 6317 Kitagawa Corporation｜kenmo_newhigh｜🔥絶好調(8/13)｜—｜FAIL_INSEN｜2570.0円｜💰—｜—｜
- 9251 G-AB&Company Co.,Ltd.｜kenmo_newhigh｜🔥絶好調(8/13)｜—｜FAIL_INSEN｜1604.0円｜💰—｜—｜
- 428A Cypress Holdings Co. Ltd.｜kenmo_newhigh｜⚡好調(6/13)｜—｜FAIL_UWAHIGE｜1725.0円｜💰—｜—｜
- 4258 AMIYA Corporation｜kenmo_newhigh/granville_oshime｜⚡好調(5/13)｜—｜FAIL_INSEN｜5800.0円｜💰—｜—｜
- 8537 大光銀行｜kenmo_newhigh｜⚠減速(3/13)｜—｜FAIL_INSEN｜3230.0円｜💰—｜—｜
- 7161 Jimoto Holdings, Inc.｜kenmo_newhigh｜業績データ取得不可｜—｜FAIL_INSEN｜626.0円｜💰—｜—｜
- 7175 今村証券｜kenmo_newhigh｜業績データ取得不可｜—｜FAIL_INSEN｜2112.0円｜💰—｜—｜
- 8370 Kiyo Bank, Ltd.｜kenmo_newhigh｜取得不可｜—｜FAIL_INSEN｜5200.0円｜💰—｜—｜
- 6278 ユニオンツール｜choruko_reversal｜🚀確変(12/13)｜—｜FAIL_UWAHIGE｜14250.0円｜💰—｜—｜
- 4099 SHIKOKU KASEI HOLDINGS CORPORATION｜choruko_reversal/granville_rebound｜🚀確変(11/13)｜—｜FAIL_UWAHIGE｜2256.0円｜💰—｜—｜
- 4971 MEC Company Ltd.｜choruko_reversal｜🔥絶好調(10/13)｜🟢値頃(5.0/7)｜PASS｜6720.0円｜💰672,000円｜⛔提案なし(指名鮮度切れ 15営業日)｜⚠日程不明
  > 📌【業態】電子基板向け薬品会社。半導体実装パッケージ基板で独占的。研究開発に力。
  > 【いま】終値6,720円・直近5日+11.26%（材料未確認）
  > 【調子】🔥絶好調（10/13）
  > 【水準】🟢値頃（5.0/7）— PER20.5倍・PEG0.51・52週35% ／ 💰単元67.2万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 15営業日)）
- 4047 関東電化工業｜choruko_reversal/granville_rebound｜🔥絶好調(10/13)｜⚪妥当(4.0/7)｜PASS｜2400.0円｜💰240,000円｜reversal2400/SL2036｜⚠日程不明 ⚠1単元でリスク枠超過（36400円）
  > 📌【業態】古河系、特殊ガス大手。独自フッ素系技術や半導体・FPD用特殊ガスに強み。
  > 【いま】終値2,400円・直近5日+15.83%（材料未確認）
  > 【調子】🔥絶好調（10/13） — E軸判定不能(進捗データ不足)
  > 【水準】⚪妥当（4.0/7）— PER18.1倍・PEG0.26・52週43% ／ 💰単元24.0万円
  > 【戦略】当日終値2400.0円の指値で反転を取りにいく。SL2036.0円（直近5日安値）／⚠1単元でリスク枠超過（36400円）
- 3391 TSURUHA Holdings, Inc.｜choruko_reversal｜🔥絶好調(10/13)｜—｜FAIL_UWAHIGE｜2165.5円｜💰—｜—｜
- 6516 山洋電気｜choruko_reversal｜🔥絶好調(10/13)｜—｜FAIL_UWAHIGE｜5420.0円｜💰—｜—｜
- 3465 KI-Star Real Estate Co., Ltd.｜choruko_reversal｜🔥絶好調(9/13)｜💎割安(6.0/7)｜PASS｜3295.0円｜💰329,500円｜reversal3295/SL3215｜⚠日程不明
  > 📌【業態】首都圏で1次取得者向け分譲住宅。注文住宅やリフォームなど多角的な展開。
  > 【いま】終値3,295円・直近5日+1.70%（材料未確認）
  > 【調子】🔥絶好調（9/13）
  > 【水準】💎割安（6.0/7）— PER5.3倍・PEG0.20・52週46% ／ 💰単元33.0万円
  > 【戦略】当日終値3295.0円の指値で反転を取りにいく。SL3215.0円（直近5日安値）
- 6268 Nabtesco Corporation｜choruko_reversal｜🔥絶好調(9/13)｜—｜FAIL_UWAHIGE｜4759.0円｜💰—｜—｜
- 6235 オプトラン｜choruko_reversal｜🔥絶好調(8/13)｜🟢値頃(5.0/7)｜PASS｜2542.0円｜💰254,200円｜⛔提案なし(指名鮮度切れ 14営業日)｜⚠日程不明
  > 📌【業態】光学薄膜装置の製造・販売。車載カメラ、スマホ向けに注力。保守まで一貫に強み。
  > 【いま】終値2,542円・直近5日+9.10%（材料未確認）
  > 【調子】🔥絶好調（8/13） — D軸データ取得不可(中央値1点採用)
  > 【水準】🟢値頃（5.0/7）— PER18.1倍・PEG0.14・52週30% ／ 💰単元25.4万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 14営業日)）
- 4186 東京応化工業｜choruko_reversal｜🔥絶好調(8/13)｜—｜FAIL_UWAHIGE｜8290.0円｜💰—｜—｜
- 4368 Fuso Chemical Co., Ltd.｜changepoint/choruko_reversal｜🔥絶好調(8/13)｜—｜FAIL_UWAHIGE｜3035.0円｜💰—｜—｜
- 6474 Nachi-Fujikoshi Corp.｜choruko_reversal｜🔥絶好調(8/13)｜—｜FAIL_UWAHIGE｜5460.0円｜💰—｜—｜
- 6588 Toshiba Tec Corp.｜choruko_reversal｜🔥絶好調(8/13)｜—｜FAIL_INSEN｜2909.0円｜💰—｜—｜
- 7729 東京精密｜choruko_reversal｜🔥絶好調(8/13)｜—｜FAIL_INSEN｜17290.0円｜💰—｜—｜
- 8086 NIPRO Corporation｜choruko_reversal｜🔥絶好調(8/13)｜—｜FAIL_INSEN｜1441.0円｜💰—｜—｜
- 6856 Horiba, Ltd.｜choruko_reversal｜⚡好調(7/13)｜⚪妥当(4.0/7)｜PASS｜23530.0円｜💰2,353,000円｜⛔提案なし(指名鮮度切れ 16営業日)｜⚠日程不明
  > 📌【業態】独立系の分析機器大手。エンジン計測装置は世界首位。半導体や医用関連も。
  > 【いま】終値23,530円・直近5日+9.19%（材料未確認）
  > 【調子】⚡好調（7/13） — E軸判定不能(進捗データ不足)
  > 【水準】⚪妥当（4.0/7）— PER19.8倍・PEG0.64・52週63% ／ 💰単元235.3万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 16営業日)）
- 7730 Mani, Inc.｜choruko_reversal｜⚡好調(7/13)｜⚪妥当(4.0/7)｜PASS｜1459.0円｜💰145,900円｜reversal1459/SL1437｜📋カルテ窓 10/15(残15営業日)
  > 📌【業態】手術用縫合針で首位。眼科用ナイフや歯科治療器も高シェア。既往品は海外生産。
  > 【いま】終値1,459円・直近5日+1.32%（材料未確認）
  > 【調子】⚡好調（7/13）
  > 【水準】⚪妥当（4.0/7）— PER21.1倍・PEG0.93・52週31% ／ 💰単元14.6万円
  > 【戦略】当日終値1459.0円の指値で反転を取りにいく。SL1437.0円（直近5日安値）
- 3104 富士紡ホールディングス｜choruko_reversal｜⚡好調(7/13)｜—｜FAIL_UWAHIGE｜3290.0円｜💰—｜—｜
- 4187 大阪有機化学工業｜changepoint/choruko_reversal｜⚡好調(7/13)｜—｜FAIL_UWAHIGE｜4210.0円｜💰—｜—｜
- 4220 Riken Technos Corporation｜choruko_reversal｜⚡好調(7/13)｜—｜FAIL_UWAHIGE｜2374.0円｜💰—｜—｜
- 6370 Kurita Water Industries Ltd.｜choruko_reversal｜⚡好調(7/13)｜—｜FAIL_INSEN｜7674.0円｜💰—｜—｜
- 6754 アンリツ｜choruko_reversal｜⚡好調(7/13)｜—｜FAIL_UWAHIGE｜3333.0円｜💰—｜—｜
- 6941 山一電機｜choruko_reversal｜⚡好調(7/13)｜—｜FAIL_UWAHIGE｜8460.0円｜💰—｜—｜
- 7550 Zensho Holdings Co., Ltd.｜choruko_reversal｜⚡好調(7/13)｜—｜FAIL_INSEN｜10220.0円｜💰—｜—｜
- 7906 Yonex Co., Ltd.｜choruko_reversal｜⚡好調(7/13)｜—｜FAIL_UWAHIGE｜2382.0円｜💰—｜—｜
- 6523 ＰＨＣＨＤ｜choruko_reversal/granville_oshime｜⚠減速(6/13)｜🟢値頃(5.0/7)｜PASS｜1395.0円｜💰139,500円｜reversal1395/SL1276｜⚠日程不明 ⚠業績基調が下向き（⚠減速） ⚠バリュートラップ疑い
  > 📌【業態】各種ヘルスケア機器・サービスの開発・製造販売。糖尿病ケアに強み。ファンド傘下。
  > 【いま】終値1,395円・直近5日+9.24%（材料未確認）
  > 【調子】⚠減速（6/13） — E軸判定不能(進捗データ不足)
  > 【水準】🟢値頃（5.0/7）— PER11.5倍・PEG0.05・52週68% ／ 💰単元13.9万円
  > 【戦略】当日終値1395.0円の指値で反転を取りにいく。SL1276.0円（直近5日安値）
- 5333 ＮＧＫ｜choruko_reversal｜⚡好調(6/13)｜🟡やや割高(2.0/7)｜PASS｜5366.0円｜💰536,600円｜reversal5366/SL4964｜⚠1単元でリスク枠超過（40200円）
  > 📌【業態】ガラス・土石（電力設備投資関連・自動車部材・部品・セラミックス関連）
  > 【いま】終値5,366円・直近5日+6.26%（材料未確認）
  > 【調子】⚡好調（6/13） — E軸判定不能(進捗データ不足)
  > 【水準】🟡やや割高（2.0/7）— PER18.4倍・PEG1.79・52週54% ／ 💰単元53.7万円
  > 【戦略】当日終値5366.0円の指値で反転を取りにいく。SL4964.0円（直近5日安値）／⚠1単元でリスク枠超過（40200円）
- 6806 ヒロセ電機｜choruko_reversal｜⚡好調(6/13)｜🟡やや割高(2.0/7)｜PASS｜24920.0円｜💰2,492,000円｜reversal24920/SL23685｜⚠日程不明 ⚠1単元でリスク枠超過（123500円）
  > 📌【業態】コネクター専業大手。産業機器、車載、スマホ向けが主力。国内は開発・営業特化。
  > 【いま】終値24,920円・直近5日+3.92%（材料未確認）
  > 【調子】⚡好調（6/13）
  > 【水準】🟡やや割高（2.0/7）— PER23.1倍・PEG1.69・52週54% ／ 💰単元249.2万円
  > 【戦略】当日終値24920.0円の指値で反転を取りにいく。SL23685.0円（直近5日安値）／⚠1単元でリスク枠超過（123500円）
- 2503 Kirin Holdings Co. Ltd.｜choruko_reversal｜⚡好調(6/13)｜—｜FAIL_INSEN｜2821.0円｜💰—｜—｜
- 5991 日本発條｜choruko_reversal｜⚡好調(6/13)｜—｜FAIL_INSEN｜3430.0円｜💰—｜—｜
- 6504 Fuji Electric Co., Ltd.｜choruko_reversal｜⚡好調(6/13)｜—｜FAIL_INSEN｜13370.0円｜💰—｜—｜
- 6622 ダイヘン｜choruko_reversal｜⚡好調(6/13)｜—｜FAIL_UWAHIGE｜12840.0円｜💰—｜—｜
- 7944 Roland Corporation｜choruko_reversal｜⚡好調(6/13)｜—｜FAIL_INSEN｜3740.0円｜💰—｜—｜
- 9412 スカパーＪＳＡＴ｜choruko_reversal｜⚡好調(6/13)｜—｜FAIL_INSEN｜2067.0円｜💰—｜—｜
- 8923 Tosei Corporation｜choruko_reversal｜⚡好調(5/13)｜⚪妥当(4.0/7)｜PASS｜1717.0円｜💰171,700円｜reversal1717/SL1665｜⚠日程不明
  > 📌【業態】賃貸住宅、オフィスの再生・流動化。ファンド運用、不動産開発、ホテルも。名鉄と提携。
  > 【いま】終値1,717円・直近5日+2.02%（材料未確認）
  > 【調子】⚡好調（5/13） — 質注意
  > 【水準】⚪妥当（4.0/7）— PER11.0倍・PEG1.66・52週52% ／ 💰単元17.2万円
  > 【戦略】当日終値1717.0円の指値で反転を取りにいく。SL1665.0円（直近5日安値）
- 6113 アマダホールディングス｜choruko_reversal｜⚡好調(5/13)｜🔴過熱(1.0/7)｜PASS｜2486.0円｜💰248,600円｜reversal2486/SL2271.5｜⚠日程不明
  > 📌【業態】金属加工機械の世界大手。板金加工機械では国内トップ。M&Aで海外拡大。
  > 【いま】終値2,486円・直近5日+7.43%（材料未確認）
  > 【調子】⚡好調（5/13） — 税引前代替不可のため経常利益を営業利益で代替(IFRS・経常非開示)
  > 【水準】🔴過熱（1.0/7）— PER22.5倍・PEG3.15・52週50% ／ 💰単元24.9万円
  > 【戦略】当日終値2486.0円の指値で反転を取りにいく。SL2271.5円（直近5日安値）
- 268A Rigaku Holdings Corporation｜choruko_reversal｜⚡好調(5/13)｜—｜FAIL_UWAHIGE｜1631.0円｜💰—｜—｜
- 4091 日本酸素ホールディングス｜choruko_reversal｜⚡好調(5/13)｜—｜FAIL_UWAHIGE｜5570.0円｜💰—｜—｜
- 6383 ダイフク｜choruko_reversal｜⚡好調(5/13)｜—｜FAIL_INSEN｜5521.0円｜💰—｜—｜
- 6707 サンケン電気｜choruko_reversal｜⚡好調(5/13)｜—｜FAIL_UWAHIGE｜6915.0円｜💰—｜—｜
- 6728 アルバック｜choruko_reversal｜⚠減速(5/13)｜—｜FAIL_INSEN｜7431.0円｜💰—｜—｜
- 7309 Shimano Inc.｜choruko_reversal｜⚡好調(5/13)｜—｜FAIL_INSEN｜17960.0円｜💰—｜—｜
- 7564 Workman Co., Ltd.｜choruko_reversal｜⚡好調(5/13)｜—｜FAIL_INSEN｜5220.0円｜💰—｜—｜
- 7731 Nikon Corp.｜choruko_reversal｜✅順調(4/13)｜🟢値頃(5.0/7)｜PASS｜1858.5円｜💰185,850円｜reversal1858.5/SL1682.5｜⚠日程不明
  > 📌【業態】カメラ・回路露光装置の両輪。一眼レフでキヤノンと双璧。ヘルスケア、エネルギー関連強化。
  > 【いま】終値1,858円・直近5日+8.68%（材料未確認）
  > 【調子】✅順調（4/13） — E軸判定不能(進捗データ不足)
  > 【水準】🟢値頃（5.0/7）— PER61.1倍・PEG0.54・52週31% ／ 💰単元18.6万円
  > 【戦略】当日終値1858.5円の指値で反転を取りにいく。SL1682.5円（直近5日安値）
- 5602 Kurimoto,Ltd.｜choruko_reversal｜✅順調(4/13)｜🟡やや割高(2.0/7)｜PASS｜1659.0円｜💰165,900円｜reversal1659/SL1584｜⚠日程不明
  > 📌【業態】鋳鉄管大手。上下水道用ダクタイル鋳鉄管や産業機械を製造する機械メーカー。
  > 【いま】終値1,659円・直近5日+2.60%（材料未確認）
  > 【調子】✅順調（4/13） — E軸判定不能(進捗データ取得不可)
  > 【水準】🟡やや割高（2.0/7）— PER13.2倍・PEG3.90・52週46% ／ 💰単元16.6万円
  > 【戦略】当日終値1659.0円の指値で反転を取りにいく。SL1584.0円（直近5日安値）
- 7966 Lintec Corporation｜choruko_reversal/granville_rebound｜✅順調(4/13)｜🟡やや割高(2.0/7)｜PASS｜5710.0円｜💰571,000円｜⛔提案なし(指名鮮度切れ 14営業日)｜⚠日程不明
  > 📌【業態】粘接着素材で首位級。機能性フィルムなど光学関連向けに特色。日本製紙系。
  > 【いま】終値5,710円・直近5日+8.76%（材料未確認）
  > 【調子】✅順調（4/13） — E軸判定不能(進捗データ不足)
  > 【水準】🟡やや割高（2.0/7）— PER17.6倍・PEG2.46・52週57% ／ 💰単元57.1万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 14営業日)）
- 4680 ROUND ONE Corporation｜choruko_reversal｜✅順調(4/13)｜—｜FAIL_UWAHIGE｜1182.5円｜💰—｜—｜
- 5334 Niterra Co.,Ltd.｜choruko_reversal｜✅順調(4/13)｜—｜FAIL_UWAHIGE｜7417.0円｜💰—｜—｜
- 6465 HOSHIZAKI Corp.｜choruko_reversal｜✅順調(4/13)｜—｜FAIL_INSEN｜5350.0円｜💰—｜—｜
- 6744 Nohmi Bosai Ltd.｜choruko_reversal｜✅順調(4/13)｜—｜FAIL_INSEN｜4085.0円｜💰—｜—｜
- 6996 Nichicon Corporation｜choruko_reversal/granville_rebound｜✅順調(4/13)｜—｜FAIL_INSEN｜2632.0円｜💰—｜—｜
- 7762 Citizen Watch Co, Ltd.｜choruko_reversal｜✅順調(4/13)｜—｜FAIL_UWAHIGE｜2377.0円｜💰—｜—｜
- 8016 Onward Holdings Co., Ltd.｜choruko_reversal｜✅順調(4/13)｜—｜FAIL_UWAHIGE｜726.0円｜💰—｜—｜
- 9627 Ain Holdings Inc.｜choruko_reversal｜✅順調(4/13)｜—｜FAIL_UWAHIGE｜5490.0円｜💰—｜—｜
- 7956 Pigeon Corporation｜choruko_reversal｜✅順調(3/13)｜🔴過熱(1.0/7)｜PASS｜2027.5円｜💰202,750円｜reversal2027.5/SL1940.5｜⚠日程不明
  > 📌【業態】育児用品最大手。小物に強み。マタニティ・介護用品や保育事業も。中国が拡大。
  > 【いま】終値2,027円・直近5日+3.81%（材料未確認）
  > 【調子】✅順調（3/13）
  > 【水準】🔴過熱（1.0/7）— PER26.5倍・PEG7.73・52週73% ／ 💰単元20.3万円
  > 【戦略】当日終値2027.5円の指値で反転を取りにいく。SL1940.5円（直近5日安値）
- 1332 Nissui Corporation｜choruko_reversal｜✅順調(3/13)｜—｜FAIL_INSEN｜1156.5円｜💰—｜—｜
- 186A アストロスケールホールディングス｜choruko_reversal｜✅順調(3/13)｜—｜FAIL_UWAHIGE｜1190.0円｜💰—｜—｜
- 2801 Kikkoman Corporation｜choruko_reversal｜✅順調(3/13)｜—｜FAIL_INSEN｜1648.5円｜💰—｜—｜
- 3433 TOCALO Co., Ltd.｜choruko_reversal｜✅順調(3/13)｜—｜FAIL_UWAHIGE｜2891.0円｜💰—｜—｜
- 5943 Noritz Corporation｜choruko_reversal｜✅順調(3/13)｜—｜FAIL_INSEN｜2219.0円｜💰—｜—｜
- 6323 ローツェ｜choruko_reversal｜✅順調(3/13)｜—｜FAIL_UWAHIGE｜3706.0円｜💰—｜—｜
- 7701 Shimadzu Corporation｜choruko_reversal｜✅順調(3/13)｜—｜FAIL_UWAHIGE｜3962.0円｜💰—｜—｜
- 8233 Takashimaya Company, Limited｜choruko_reversal｜✅順調(3/13)｜—｜FAIL_INSEN｜2120.5円｜💰—｜—｜
- 8934 Sun Frontier Fudousan Co., Ltd.｜choruko_reversal｜✅順調(3/13)｜—｜FAIL_UWAHIGE｜2400.0円｜💰—｜—｜
- 2875 Toyo Suisan Kaisha, Ltd.｜choruko_reversal｜➖横ばい(2/13)｜⚪妥当(3.0/7)｜PASS｜9722.0円｜💰972,200円｜reversal9722/SL9563｜⚠日程不明
  > 📌【業態】即席麺国内大手。マルちゃんブランドの即席麺・水産・低温食品を展開。
  > 【いま】終値9,722円・直近5日-3.79%（材料未確認）
  > 【調子】➖横ばい（2/13） — E軸判定不能(進捗データ取得不可)
  > 【水準】⚪妥当（3.0/7）— PER14.0倍・PEG—・52週6% ／ 💰単元97.2万円
  > 【戦略】当日終値9722.0円の指値で反転を取りにいく。SL9563.0円（直近5日安値）
- 1871 PS Construction Co., Ltd.｜choruko_reversal｜⚠減速(2/13)｜—｜FAIL_UWAHIGE｜2215.0円｜💰—｜—｜
- 2264 森永乳業｜choruko_reversal｜➖横ばい(2/13)｜—｜FAIL_UWAHIGE｜1129.5円｜💰—｜—｜
- 3099 Isetan Mitsukoshi Holdings Ltd.｜choruko_reversal｜➖横ばい(2/13)｜—｜FAIL_UWAHIGE｜3331.0円｜💰—｜—｜
- 4028 ISHIHARA SANGYO KAISHA, LTD.｜choruko_reversal｜⚠減速(2/13)｜—｜FAIL_INSEN｜2907.0円｜💰—｜—｜
- 4061 デンカ｜choruko_reversal｜➖横ばい(2/13)｜—｜FAIL_UWAHIGE｜3360.0円｜💰—｜—｜
- 4996 Kumiai Chemical Industry Co., Ltd.｜choruko_reversal｜🔻悪化(2/13)｜—｜FAIL_UWAHIGE｜684.0円｜💰—｜—｜
- 6368 Organo Corp.｜choruko_reversal｜➖横ばい(2/13)｜—｜FAIL_UWAHIGE｜12675.0円｜💰—｜—｜
- 6617 TAKAOKA TOKO CO., LTD.｜choruko_reversal｜➖横ばい(2/13)｜—｜FAIL_INSEN｜6900.0円｜💰—｜—｜
- 6674 ジーエス・ユアサ　コーポレーション｜choruko_reversal｜➖横ばい(2/13)｜—｜FAIL_UWAHIGE｜5480.0円｜💰—｜—｜
- 6841 Yokogawa Electric Corp.｜choruko_reversal｜➖横ばい(2/13)｜—｜FAIL_INSEN｜4693.0円｜💰—｜—｜
- 7220 Musashi Seimitsu Industry Co., Ltd.｜choruko_reversal｜🔻悪化(2/13)｜—｜FAIL_UWAHIGE｜2930.0円｜💰—｜—｜
- 7532 パン・パシフィック・インターナショナルホールディングス｜choruko_reversal｜➖横ばい(2/13)｜—｜FAIL_UWAHIGE｜716.0円｜💰—｜—｜
- 9708 Imperial Hotel Ltd｜choruko_reversal｜➖横ばい(2/13)｜—｜FAIL_UWAHIGE｜957.0円｜💰—｜—｜
- 6479 ミネベア｜choruko_reversal｜⚠減速(1/13)｜🟢値頃(5.0/7)｜PASS｜3606.0円｜💰360,600円｜⛔提案なし(指名鮮度切れ 14営業日)｜⚠日程不明 ⚠業績基調が下向き（⚠減速） ⚠バリュートラップ疑い
  > 📌【業態】総合精密部品メーカー。極小ベアリングで世界高シェア。ミツミと統合で新分野開拓。
  > 【いま】終値3,606円・直近5日+6.47%（材料未確認）
  > 【調子】⚠減速（1/13） — 経常利益(または税引前代替)データ取得不可
  > 【水準】🟢値頃（5.0/7）— PER16.6倍・PEG—・52週39% ／ 💰単元36.1万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 14営業日)）
- 2685 AND ST HD Co.Ltd.｜choruko_reversal｜⚠減速(1/13)｜🟡やや割高(2.0/7)｜PASS｜3170.0円｜💰317,000円｜reversal3170/SL3100｜⚠日程不明 ⚠業績基調が下向き（⚠減速）
  > 📌【業態】アパレル小売大手。coenやGLOBAL WORK等の衣料品ブランドを展開する持株会社。
  > 【いま】終値3,170円・直近5日-0.94%（材料未確認）
  > 【調子】⚠減速（1/13） — E軸判定不能(進捗データ不足)
  > 【水準】🟡やや割高（2.0/7）— PER13.9倍・PEG6.28・52週56% ／ 💰単元31.7万円
  > 【戦略】当日終値3170.0円の指値で反転を取りにいく。SL3100.0円（直近5日安値）
- 6951 日本電子｜choruko_reversal/granville_rebound｜⚠減速(1/13)｜🔴過熱(1.0/7)｜PASS｜7564.0円｜💰756,400円｜⛔提案なし(指名鮮度切れ 14営業日)｜⚠日程不明 ⚠業績基調が下向き（⚠減速）
  > 📌【業態】電気機器（計測機器・半導体製造装置・EUV関連）
  > 【いま】終値7,564円・直近5日+11.46%（材料未確認）
  > 【調子】⚠減速（1/13） — D軸データ取得不可(中央値1点採用)
  > 【水準】🔴過熱（1.0/7）— PER17.3倍・PEG—・52週65% ／ 💰単元75.6万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 14営業日)）
- 2127 Nihon M&A Center Holdings Inc.｜choruko_reversal｜⚠減速(1/13)｜—｜FAIL_INSEN｜640.0円｜💰—｜—｜
- 5332 TOTO Ltd｜choruko_reversal｜⚠減速(1/13)｜—｜FAIL_UWAHIGE｜5859.0円｜💰—｜—｜
- 9715 transcosmos Inc.｜choruko_reversal｜⚠減速(1/13)｜—｜FAIL_UWAHIGE｜3600.0円｜💰—｜—｜
- 8976 Daiwa Office Investment Corporation｜choruko_reversal｜⚠減速(0/13)｜🔴過熱(2.8/7)｜PASS｜306500.0円｜💰306,500円｜reversal306500/SL301500｜⚠日程不明 ⚠業績基調が下向き（⚠減速）
  > 📌【業態】オフィスビル特化型投資。東京主要5区の比率大。運用:大和証券グループ本社。
  > 【いま】終値306,500円・直近5日+0.82%（材料未確認）
  > 【調子】⚠減速（0/13） — D軸判定不能(四半期データ不足)
  > 【水準】🔴過熱（2.8/7）— PER43.8倍・PEG—・52週8% ／ 💰単元30.6万円
  > 【戦略】当日終値306500.0円の指値で反転を取りにいく。SL301500.0円（直近5日安値）
- 6804 Hosiden Corp.｜choruko_reversal｜🔻悪化(0/13)｜—｜FAIL_UWAHIGE｜2532.0円｜💰—｜—｜
- 5110 Sumitomo Rubber Industries, Ltd.｜choruko_reversal｜業績データ取得不可(経常益予想非開示)｜💎割安(6.0/7)｜PASS｜2031.5円｜💰203,150円｜reversal2031.5/SL1985.5｜⚠日程不明
  > 📌【業態】タイヤ大手。ダンロップブランドのタイヤ製造に加えゴルフ用品(スリクソン)も展開。
  > 【いま】終値2,031円・直近5日+1.35%（材料未確認）
  > 【調子】業績データ取得不可(経常益予想非開示)（None/13） — 経常利益データ取得不可
  > 【水準】💎割安（6.0/7）— PER9.7倍・PEG—・52週29% ／ 💰単元20.3万円
  > 【戦略】当日終値2031.5円の指値で反転を取りにいく。SL1985.5円（直近5日安値）
- 8984 Daiwa House REIT Investment Corporation｜choruko_reversal｜取得不可｜🔴過熱(2.8/7)｜PASS｜113700.0円｜💰113,700円｜reversal113700/SL109800｜📋カルテ窓 10/19(残17営業日)
  > 📌【業態】物流・住宅特化型のJ-REIT。大和ハウスグループ系の不動産投資法人。
  > 【いま】終値113,700円・直近5日-1.64%（材料未確認）
  > 【調子】取得不可（None/13） — E軸判定不能(進捗データ取得不可)
  > 【水準】🔴過熱（2.8/7）— PER43.2倍・PEG—・52週11% ／ 💰単元11.4万円
  > 【戦略】当日終値113700.0円の指値で反転を取りにいく。SL109800.0円（直近5日安値）
- 3591 WACOAL HOLDINGS CORP｜choruko_reversal｜🔻悪化｜—｜FAIL_UWAHIGE｜3960.0円｜💰—｜—｜
- 4385 Mercari, Inc.｜choruko_reversal/granville_rebound｜業績データ取得不可(経常益予想非開示)｜—｜FAIL_INSEN｜3554.0円｜💰—｜—｜
- 4912 Lion Corporation｜choruko_reversal｜業績データ取得不可(経常益予想非開示)｜—｜FAIL_INSEN｜1718.0円｜💰—｜—｜
- 5101 Yokohama Rubber Co., Ltd.｜choruko_reversal｜—｜—｜FAIL_INSEN｜6974.0円｜💰—｜—｜
- 5344 MARUWA CO., LTD.｜choruko_reversal｜業績データ取得不可｜—｜FAIL_INSEN｜55790.0円｜💰—｜—｜
- 6101 ツガミ｜choruko_reversal｜業績データ取得不可｜—｜FAIL_UWAHIGE｜5150.0円｜💰—｜—｜
- 6141 DMG MORI CO., LTD.｜choruko_reversal｜取得不可｜—｜FAIL_UWAHIGE｜2896.0円｜💰—｜—｜
- 6457 Glory Ltd.｜choruko_reversal｜業績データ取得不可(経常益予想非開示)｜—｜FAIL_INSEN｜4511.0円｜💰—｜—｜
- 4014 カラダノート｜stf_kakuhen｜🔥絶好調(10/13)｜—｜FAIL_INSEN｜447.0円｜💰—｜—｜
- 9824 泉州電業｜stf_kakuhen｜🔥絶好調(10/13)｜—｜FAIL_INSEN｜7850.0円｜💰—｜—｜
- 1436 グリーンエナジー＆カンパニー｜stf_kakuhen｜🔥絶好調(9/13)｜💎割安(6.0/7)｜PASS｜1750.0円｜💰175,000円｜⛔提案なし(手法ブランチ不明)｜⚠日程不明
  > 📌【業態】太陽光発電設備が標準の戸建販売。クリーンエネルギー発電・投資事業が主力に。
  > 【いま】終値1,750円・直近5日-0.96%（材料未確認）
  > 【調子】🔥絶好調（9/13） — E軸判定不能(進捗データ取得不可)
  > 【水準】💎割安（6.0/7）— PER22.6倍・PEG0.45・52週71% ／ 💰単元17.5万円
  > 【戦略】発注対象外（⛔提案なし(手法ブランチ不明)）
- 4627 ナトコ｜stf_kakuhen｜🔥絶好調(9/13)｜—｜FAIL_UWAHIGE｜1951.0円｜💰—｜—｜
- 2983 アールプランナー｜stf_kakuhen｜🔥絶好調(8/13)｜💎割安(6.0/7)｜PASS｜1716.0円｜💰171,600円｜⛔提案なし(手法ブランチ不明)｜⚠日程不明
  > 📌【業態】未取得（次回以降に取得）
  > 【いま】終値1,716円・直近5日+1.84%（材料未確認）
  > 【調子】🔥絶好調（8/13） — 上方修正済み
  > 【水準】💎割安（6.0/7）— PER5.6倍・PEG0.17・52週46% ／ 💰単元17.2万円
  > 【戦略】発注対象外（⛔提案なし(手法ブランチ不明)）
- 6184 鎌倉新書｜stf_kakuhen｜⚡好調(7/13)｜—｜FAIL_INSEN｜606.0円｜💰—｜—｜

## グランビル銘柄
- 5714 ＤＯＷＡホールディングス｜granville_tenkan｜🔥絶好調(10/13)｜—｜FAIL_INSEN｜8964.0円｜💰—｜—｜
- 8151 東陽テクニカ｜granville_rebound/granville_tenkan/変化点🔔｜🔥絶好調(9/13)｜⚪妥当(4.0/7)｜PASS｜1885.0円｜💰188,500円｜momentum1900/SL1785.06｜⚠日程不明
  > 📌【業態】電子計測器専門商社。研究開発用機器が主力。欧米から輸入販売中心。
  > 【いま】終値1,885円・直近5日+4.03%（材料未確認）
  > 【調子】🔥絶好調（9/13）
  > 【水準】⚪妥当（4.0/7）— PER15.7倍・PEG0.18・52週49% ／ 💰単元18.9万円
  > 【戦略】当日高値超えの逆指値1900.0円で順張り参戦を検討。上限1919.0円・SL1785.06円目安
- 2986 ＬＡホールディングス｜granville_tenkan｜🔥絶好調(9/13)｜—｜FAIL_INSEN｜2926.0円｜💰—｜—｜
- 5703 Nippon Light Metal Holdings Co., Ltd.｜granville_oshime/granville_tenkan｜🔥絶好調(9/13)｜—｜FAIL_INSEN｜2985.0円｜💰—｜—｜
- 6928 エノモト｜granville_tenkan｜🔥絶好調(9/13)｜—｜FAIL_UWAHIGE｜3115.0円｜💰—｜—｜
- 8562 Fukushima Bank, Ltd.｜granville_tenkan｜🔥絶好調(9/13)｜—｜FAIL_INSEN｜385.0円｜💰—｜—｜
- 3608 TSI Holdings Co.,Ltd.｜granville_tenkan｜🔥絶好調(8/13)｜—｜FAIL_UWAHIGE｜1237.0円｜💰—｜—｜
- 6706 電気興業｜granville_rebound/granville_tenkan｜⚡好調(7/13)｜⚪妥当(4.0/7)｜PASS｜3365.0円｜💰336,500円｜momentum3385/SL3177.2｜⚠日程不明
  > 📌【業態】大型通信アンテナの製造、工事。独自の高周波焼入れ技術。インフラ関連も展開。
  > 【いま】終値3,365円・直近5日+2.12%（材料未確認）
  > 【調子】⚡好調（7/13） — E軸判定不能(進捗データ不足)
  > 【水準】⚪妥当（4.0/7）— PER12.8倍・PEG0.36・52週85% ／ 💰単元33.6万円
  > 【戦略】当日高値超えの逆指値3385.0円で順張り参戦を検討。上限3418.85円・SL3177.2円目安
- 6395 TADANO Ltd.｜granville_tenkan｜⚡好調(7/13)｜—｜FAIL_INSEN｜1370.0円｜💰—｜—｜
- 6946 Nippon Avionics Co., Ltd.｜granville_tenkan｜⚡好調(6/13)｜—｜FAIL_UWAHIGE｜7450.0円｜💰—｜—｜
- 7199 Premium Group Co., Ltd.｜granville_oshime/granville_tenkan｜⚡好調(6/13)｜—｜FAIL_INSEN｜2118.0円｜💰—｜—｜
- 7270 Subaru Corporation｜granville_tenkan｜⚡好調(6/13)｜—｜FAIL_INSEN｜2628.0円｜💰—｜—｜
- 9470 学研 HD｜granville_tenkan｜⚡好調(5/13)｜⚪妥当(3.0/7)｜PASS｜1073.0円｜💰107,300円｜momentum1074/SL1008.62｜⚠日程不明
  > 📌【業態】教育関連出版大手。学習参考書や図鑑で首位。高齢者施設、保育園も。
  > 【いま】終値1,073円・直近5日+2.00%（材料未確認）
  > 【調子】⚡好調（5/13） — E軸判定不能(進捗データ不足)
  > 【水準】⚪妥当（3.0/7）— PER12.0倍・PEG1.91・52週62% ／ 💰単元10.7万円
  > 【戦略】当日高値超えの逆指値1074.0円で順張り参戦を検討。上限1084.74円・SL1008.62円目安
- 1968 Taihei Dengyo Kaisha, Ltd.｜granville_tenkan｜⚡好調(5/13)｜—｜FAIL_INSEN｜2551.0円｜💰—｜—｜
- 2931 ユーグレナ｜granville_tenkan｜⚡好調(5/13)｜—｜FAIL_INSEN｜347.0円｜💰—｜—｜
- 4666 PARK24 Co., Ltd.｜granville_tenkan｜⚡好調(5/13)｜—｜FAIL_UWAHIGE｜2008.5円｜💰—｜—｜
- 6339 Sintokogio,Ltd.｜granville_tenkan｜⚠減速(5/13)｜—｜FAIL_UWAHIGE｜1215.0円｜💰—｜—｜
- 7276 小糸製作所｜granville_tenkan｜⚠減速(4/13)｜🟡やや割高(2.0/7)｜PASS｜2667.0円｜💰266,700円｜momentum2675.5/SL2514.03｜⚠日程不明 ⚠業績基調が下向き（⚠減速）
  > 📌【業態】自動車用照明機器首位。トヨタ向け主力。航空機部品も。自動運転用センサー注力。
  > 【いま】終値2,667円・直近5日+2.42%（材料未確認）
  > 【調子】⚠減速（4/13） — 質注意
  > 【水準】🟡やや割高（2.0/7）— PER17.3倍・PEG1.52・52週61% ／ 💰単元26.7万円
  > 【戦略】当日高値超えの逆指値2675.5円で順張り参戦を検討。上限2702.26円・SL2514.03円目安
- 1911 Sumitomo Forestry Co., Ltd.｜granville_tenkan｜🔻悪化(4/13)｜—｜FAIL_INSEN｜1215.0円｜💰—｜—｜
- 2281 Prima Meat Packers,Ltd.｜granville_tenkan｜✅順調(4/13)｜—｜FAIL_INSEN｜2389.0円｜💰—｜—｜
- 2325 NJS Co., Ltd.｜granville_tenkan｜✅順調(4/13)｜—｜FAIL_UWAHIGE｜4595.0円｜💰—｜—｜
- 6167 冨士ダイス｜granville_rebound/granville_tenkan｜✅順調(4/13)｜—｜FAIL_UWAHIGE｜1008.0円｜💰—｜—｜
- 6412 平和｜granville_tenkan｜✅順調(4/13)｜—｜FAIL_INSEN｜2197.0円｜💰—｜—｜
- 7198 SBI ARUHI Corporation｜granville_tenkan｜✅順調(4/13)｜—｜FAIL_INSEN｜840.0円｜💰—｜—｜
- 9031 Nishi-Nippon Railroad Co., Ltd.｜granville_tenkan｜🔻悪化(4/13)｜—｜FAIL_INSEN｜3075.0円｜💰—｜—｜
- 9045 Keihan Holdings Co.,Ltd.｜granville_tenkan｜⚠減速(4/13)｜—｜FAIL_INSEN｜3211.0円｜💰—｜—｜
- 4272 Nippon Kayaku Co., Ltd.｜granville_tenkan/granville_oshime｜✅順調(3/13)｜🟡やや割高(2.0/7)｜PASS｜2131.5円｜💰213,150円｜momentum2136.5/SL2007.37｜⚠日程不明
  > 📌【業態】火薬から機能化学品など多角化。医薬、自動車部材等。抗がん剤に強み。(化学)
  > 【いま】終値2,131円・直近5日+3.90%（材料未確認）
  > 【調子】✅順調（3/13） — D軸簡易判定(四半期詳細未取得のため中立値)
  > 【水準】🟡やや割高（2.0/7）— PER13.4倍・PEG2.25・52週93% ／ 💰単元21.3万円
  > 【戦略】当日高値超えの逆指値2136.5円で順張り参戦を検討。上限2157.87円・SL2007.37円目安
- 1721 コムシスホールディングス｜granville_tenkan｜✅順調(3/13)｜—｜FAIL_INSEN｜5593.0円｜💰—｜—｜
- 1820 西松建設｜granville_tenkan｜✅順調(3/13)｜—｜FAIL_INSEN｜5692.0円｜💰—｜—｜
- 3549 KUSURI NO AOKI HOLDINGS CO.,LTD.｜granville_tenkan｜✅順調(3/13)｜—｜FAIL_UWAHIGE｜3976.0円｜💰—｜—｜
- 3569 セーレン｜granville_tenkan｜✅順調(3/13)｜—｜FAIL_INSEN｜3290.0円｜💰—｜—｜
- 4183 Mitsui Chemicals, Inc.｜granville_tenkan｜✅順調(3/13)｜—｜FAIL_INSEN｜2150.0円｜💰—｜—｜
- 4956 Konishi Co., Ltd.｜granville_tenkan｜✅順調(3/13)｜—｜FAIL_INSEN｜1510.0円｜💰—｜—｜
- 5423 Tokyo Steel Manufacturing Co., Ltd.｜granville_tenkan｜🔻悪化(3/13)｜—｜FAIL_INSEN｜1712.0円｜💰—｜—｜
- 5461 Chubu Steel Plate Co., Ltd.｜granville_tenkan｜🔻悪化(3/13)｜—｜FAIL_INSEN｜2120.0円｜💰—｜—｜
- 6730 アクセル｜granville_tenkan｜🔻悪化(3/13)｜—｜FAIL_UWAHIGE｜1233.0円｜💰—｜—｜
- 6807 日本航空電子工業｜granville_tenkan｜✅順調(3/13)｜—｜FAIL_UWAHIGE｜2570.0円｜💰—｜—｜
- 6927 Helios Techno Holding Co., Ltd.｜granville_tenkan｜🔻悪化(3/13)｜—｜FAIL_UWAHIGE｜996.0円｜💰—｜—｜
- 7269 Suzuki Motor Corp.｜granville_tenkan｜✅順調(3/13)｜—｜FAIL_INSEN｜1991.0円｜💰—｜—｜
- 7994 OKAMURA CORP｜granville_tenkan｜✅順調(3/13)｜—｜FAIL_INSEN｜2340.0円｜💰—｜—｜
- 8056 BIPROGY Inc.｜granville_tenkan｜✅順調(3/13)｜—｜FAIL_UWAHIGE｜4793.0円｜💰—｜—｜
- 1377 Sakata Seed Corporation｜granville_tenkan｜➖横ばい(2/13)｜—｜FAIL_INSEN｜4390.0円｜💰—｜—｜
- 1833 Okumura Corporation｜granville_tenkan｜⚠減速(2/13)｜—｜FAIL_INSEN｜5750.0円｜💰—｜—｜
- 4274 HOSOYA PYRO-ENGINEERING CO LTD｜granville_tenkan｜➖横ばい(2/13)｜—｜FAIL_INSEN｜1132.0円｜💰—｜—｜
- 4350 Medical System Network Co., Ltd.｜granville_tenkan｜➖横ばい(2/13)｜—｜FAIL_INSEN｜519.0円｜💰—｜—｜
- 5851 Ryobi Limited｜granville_tenkan｜➖横ばい(2/13)｜—｜FAIL_INSEN｜2736.0円｜💰—｜—｜
- 6328 荏原実業｜granville_tenkan｜➖横ばい(2/13)｜—｜FAIL_UWAHIGE｜2391.0円｜💰—｜—｜
- 6794 Foster Electric Company, Limited｜granville_tenkan｜➖横ばい(2/13)｜—｜FAIL_INSEN｜3255.0円｜💰—｜—｜
- 8803 Heiwa Real Estate Co., Ltd.｜granville_tenkan｜➖横ばい(2/13)｜—｜FAIL_INSEN｜2370.0円｜💰—｜—｜
- 9007 Odakyu Electric Railway Co., Ltd.｜granville_tenkan｜➖横ばい(2/13)｜—｜FAIL_INSEN｜1775.5円｜💰—｜—｜
- 9468 Kadokawa Corporation｜granville_tenkan｜➖横ばい(2/13)｜—｜FAIL_UWAHIGE｜3656.0円｜💰—｜—｜
- 9744 MEITEC Group Holdings Inc.｜granville_tenkan｜➖横ばい(2/13)｜—｜FAIL_UWAHIGE｜3482.0円｜💰—｜—｜
- 9987 Suzuken Co., Ltd.｜granville_tenkan｜⚠減速(1/13)｜⚪妥当(3.0/7)｜PASS｜5400.0円｜💰540,000円｜momentum5428/SL5092.92｜⚠業績基調が下向き（⚠減速） ⚠1単元でリスク枠超過（33507円）
  > 📌【業態】独立系の医薬品卸大手。M&Aで全国に営業網。子会社で医薬品製造も。(卸売業)
  > 【いま】終値5,400円・直近5日+2.74%（材料未確認）
  > 【調子】⚠減速（1/13） — E軸判定不能(進捗データ不足)
  > 【水準】⚪妥当（3.0/7）— PER14.4倍・PEG—・52週33% ／ 💰単元54.0万円
  > 【戦略】当日高値超えの逆指値5428.0円で順張り参戦を検討。上限5482.28円・SL5092.92円目安／⚠1単元でリスク枠超過（33507円）
- 4694 BML , Inc.｜granville_tenkan｜⚠減速(1/13)｜🟡やや割高(2.0/7)｜PASS｜3685.0円｜💰368,500円｜momentum3695/SL3468.6｜⚠日程不明 ⚠業績基調が下向き（⚠減速）
  > 📌【業態】臨床検査大手。全国にラボ網を積極展開。電子カルテなど医療システムに注力。
  > 【いま】終値3,685円・直近5日+1.94%（材料未確認）
  > 【調子】⚠減速（1/13） — 質注意
  > 【水準】🟡やや割高（2.0/7）— PER19.7倍・PEG—・52週31% ／ 💰単元36.9万円
  > 【戦略】当日高値超えの逆指値3695.0円で順張り参戦を検討。上限3731.95円・SL3468.6円目安
- 1982 Hibiya Engineering,Ltd.｜granville_tenkan｜⚠減速(1/13)｜🔴過熱(1.0/7)｜PASS｜3270.0円｜💰327,000円｜momentum3275/SL3073.8｜⚠日程不明 ⚠業績基調が下向き（⚠減速）
  > 📌【業態】空調工事大手。電気・衛生工事も。NTT向け主力。床下空調システムなどに強み。
  > 【いま】終値3,270円・直近5日+6.86%（材料未確認）
  > 【調子】⚠減速（1/13） — E軸判定不能(進捗データ不足)
  > 【水準】🔴過熱（1.0/7）— PER15.5倍・PEG5.33・52週85% ／ 💰単元32.7万円
  > 【戦略】当日高値超えの逆指値3275.0円で順張り参戦を検討。上限3307.75円・SL3073.8円目安
- 4967 小林製薬｜granville_tenkan｜🔻悪化(1/13)｜🔴過熱(0.0/7)｜PASS｜5885.0円｜💰588,500円｜momentum5902/SL5538.48｜⚠日程不明 ⚠業績基調が下向き（🔻悪化） ⚠1単元でリスク枠超過（36352円）
  > 📌【業態】芳香剤最大手。家庭用品を製造販売。医薬品・医療機器や健康食品も展開。
  > 【いま】終値5,885円・直近5日+1.64%（材料未確認）
  > 【調子】🔻悪化（1/13） — 質注意
  > 【水準】🔴過熱（0.0/7）— PER43.8倍・PEG—・52週77% ／ 💰単元58.9万円
  > 【戦略】当日高値超えの逆指値5902.0円で順張り参戦を検討。上限5961.02円・SL5538.48円目安／⚠1単元でリスク枠超過（36352円）
- 1887 JDC Corporation｜granville_tenkan｜⚠減速(1/13)｜—｜FAIL_INSEN｜548.0円｜💰—｜—｜
- 1946 Toenec Corporation｜granville_tenkan｜⚠減速(1/13)｜—｜FAIL_INSEN｜2275.0円｜💰—｜—｜
- 1980 ダイダン｜granville_tenkan｜⚠減速(1/13)｜—｜FAIL_INSEN｜2945.0円｜💰—｜—｜
- 2267 Yakult Honsha Co.,Ltd.｜granville_tenkan｜⚠減速(1/13)｜—｜FAIL_UWAHIGE｜2803.0円｜💰—｜—｜
- 3854 アイル｜granville_tenkan｜⚠減速(1/13)｜—｜FAIL_UWAHIGE｜2162.0円｜💰—｜—｜
- 5408 Nakayama Steel Works,Ltd.｜granville_tenkan｜🔻悪化(1/13)｜—｜FAIL_INSEN｜643.0円｜💰—｜—｜
- 6310 井関農機｜granville_tenkan｜⚠減速(1/13)｜—｜FAIL_UWAHIGE｜1969.0円｜💰—｜—｜
- 7211 Mitsubishi Motors Corporation｜granville_tenkan｜⚠減速(1/13)｜—｜FAIL_INSEN｜367.5円｜💰—｜—｜
- 7981 Takara Standard Co.,Ltd.｜granville_tenkan｜⚠減速(1/13)｜—｜FAIL_UWAHIGE｜3110.0円｜💰—｜—｜
- 8129 TOHO HOLDINGS CO., LTD.｜granville_tenkan｜⚠減速(1/13)｜—｜FAIL_UWAHIGE｜4063.0円｜💰—｜—｜
- 9502 Chubu Electric Power Company,Incorporated｜granville_tenkan｜🔻悪化(1/13)｜—｜FAIL_INSEN｜2869.0円｜💰—｜—｜
- 9531 東京瓦斯｜granville_tenkan｜⚠減速(1/13)｜—｜FAIL_INSEN｜6167.0円｜💰—｜—｜
- 8093 Kyokuto Boeki Kaisha, Ltd.｜granville_tenkan｜⚠減速(0/13)｜—｜FAIL_INSEN｜1809.0円｜💰—｜—｜
- 2002 日清製粉グループ本社｜granville_tenkan｜—｜—｜FAIL_UWAHIGE｜2013.5円｜💰—｜—｜
- 2160 GNI Group Ltd.｜granville_tenkan｜業績データ取得不可｜—｜FAIL_UWAHIGE｜3395.0円｜💰—｜—｜
- 2432 ディー・エヌ・エー｜granville_tenkan｜業績データ取得不可｜—｜FAIL_INSEN｜2548.5円｜💰—｜—｜
- 3053 Pepper Food Service Co., Ltd.｜granville_rebound/granville_tenkan｜業績データ取得不可｜—｜FAIL_INSEN｜202.0円｜💰—｜—｜
- 3452 B-Lot Company Limited｜granville_tenkan｜取得不可｜—｜FAIL_INSEN｜1455.0円｜💰—｜—｜
- 4005 住友化学｜granville_tenkan｜業績データ取得不可(経常益予想非開示)｜—｜FAIL_INSEN｜588.2000122070312円｜💰—｜—｜
- 4375 Safie Inc.｜changepoint/granville_tenkan｜取得不可｜—｜FAIL_INSEN｜684.0円｜💰—｜—｜
- 5071 ヴィス｜granville_tenkan｜—｜—｜FAIL_INSEN｜1401.0円｜💰—｜—｜
- 6326 Kubota Corporation｜granville_tenkan｜業績データ取得不可｜—｜FAIL_INSEN｜2750.5円｜💰—｜—｜
- 8002 Marubeni Corporation｜granville_tenkan｜業績データ取得不可｜—｜FAIL_INSEN｜4878.0円｜💰—｜—｜
- 8060 キヤノンマーケティングジャパン｜granville_tenkan｜—｜—｜FAIL_INSEN｜3679.0円｜💰—｜—｜
- 8253 Credit Saison Co., Ltd.｜granville_tenkan｜取得不可｜—｜FAIL_INSEN｜4590.0円｜💰—｜—｜
- 9628 San Holdings,Inc.｜granville_tenkan｜判定保留(変則決算)｜—｜FAIL_INSEN｜1352.0円｜💰—｜—｜
- 7480 Suzuden Corporation｜granville_oshime｜🚀確変(13/13)｜—｜FAIL_UWAHIGE｜3605.0円｜💰—｜—｜
- 7806 Ｇ−ＭＴＧ｜granville_oshime｜🚀確変(11/13)｜⚪妥当(3.0/7)｜PASS｜8170.0円｜💰817,000円｜⛔型不一致: 既に支持帯以下｜⚠日程不明
  > 📌【業態】美容ローラー「ReFa」・健康機器「SIXPAD」など健康美容関連の企画開発・販売。
  > 【いま】終値8,170円・直近5日+4.48%（材料未確認）
  > 【調子】🚀確変（11/13）
  > 【水準】⚪妥当（3.0/7）— PER29.2倍・PEG0.60・52週79% ／ 💰単元81.7万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 6834 Seikoh Giken Co., Ltd.｜granville_oshime｜🔥絶好調(10/13)｜💎割安(6.0/7)｜PASS｜6040.0円｜💰604,000円｜oshime5253.94/SL5227.8｜⚠日程不明
  > 📌【業態】光関連部品、金型技術に強み。携帯電話向けレンズ、自動車用センサーも展開。
  > 【いま】終値6,040円・直近5日+24.02%（材料未確認）
  > 【調子】🔥絶好調（10/13）
  > 【水準】💎割安（6.0/7）— PER29.3倍・PEG0.60・52週73% ／ 💰単元60.4万円
  > 【戦略】5253.94円までの押し目を指値で待つ。SL5227.8円（25日線基準）
- 2760 東京エレクトロン　デバイス｜granville_oshime｜🔥絶好調(10/13)｜⚪妥当(4.0/7)｜PASS｜4505.0円｜💰450,500円｜oshime4130.95/SL4110.4｜⚠日程不明
  > 📌【業態】電子部品の半導体商社。主に米国製を扱う。設計受託で産業用に強み。
  > 【いま】終値4,505円・直近5日+11.65%（材料未確認）
  > 【調子】🔥絶好調（10/13）
  > 【水準】⚪妥当（4.0/7）— PER14.1倍・PEG0.36・52週89% ／ 💰単元45.0万円
  > 【戦略】4130.95円までの押し目を指値で待つ。SL4110.4円（25日線基準）
- 212A フィットイージー｜granville_oshime｜🔥絶好調(10/13)｜—｜FAIL_UWAHIGE｜2832.0円｜💰—｜—｜
- 6966 Mitsui High-Tec, Inc.｜granville_oshime｜🔥絶好調(10/13)｜—｜FAIL_INSEN｜901.0円｜💰—｜—｜
- 3036 アルコニックス｜granville_oshime｜🔥絶好調(9/13)｜—｜FAIL_INSEN｜3370.0円｜💰—｜—｜
- 3663 セルシス｜granville_oshime｜🔥絶好調(9/13)｜—｜FAIL_UWAHIGE｜1856.0円｜💰—｜—｜
- 4377 ONE CAREER Inc.｜granville_oshime｜🔥絶好調(9/13)｜—｜FAIL_INSEN｜2362.0円｜💰—｜—｜
- 5702 大紀アルミニウム工業所｜granville_oshime｜🔥絶好調(9/13)｜—｜FAIL_INSEN｜1818.0円｜💰—｜—｜
- 3498 霞ヶ関キャピタル｜granville_oshime｜🔥絶好調(8/13)｜💎割安(6.0/7)｜PASS｜7480.0円｜💰748,000円｜⛔型不一致: 既に支持帯以下｜
  > 📌【業態】不動産コンサル業。再生可能エネ発電施設、投資用不動産の開発、投資家に売却。
  > 【いま】終値7,480円・直近5日+3.89%（材料未確認）
  > 【調子】🔥絶好調（8/13） — 開示キューにより上方修正確認(E軸)
  > 【水準】💎割安（6.0/7）— PER11.1倍・PEG0.22・52週37% ／ 💰単元74.8万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 2384 SBS Holdings Inc｜granville_oshime｜🔥絶好調(8/13)｜⚪妥当(4.0/7)｜PASS｜5320.0円｜💰532,000円｜⛔提案なし(指名鮮度切れ 13営業日)｜⚠日程不明
  > 📌【業態】総合物流会社。物流一括受託が主力。食品輸送に力。物流施設の流動化も。
  > 【いま】終値5,320円・直近5日+9.13%（材料未確認）
  > 【調子】🔥絶好調（8/13）
  > 【水準】⚪妥当（4.0/7）— PER14.6倍・PEG0.63・52週99% ／ 💰単元53.2万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 13営業日)）
- 4413 ボードルア｜granville_oshime｜🔥絶好調(8/13)｜—｜FAIL_INSEN｜2965.0円｜💰—｜—｜
- 4480 Medley, Inc.｜granville_oshime/granville_rebound｜🔥絶好調(8/13)｜—｜FAIL_INSEN｜2356.0円｜💰—｜—｜
- 5480 日本冶金工業｜granville_oshime｜🔥絶好調(8/13)｜—｜FAIL_INSEN｜5450.0円｜💰—｜—｜
- 3040 Soliton Systems K.K.｜granville_oshime/granville_rebound｜⚡好調(7/13)｜⚪妥当(3.0/7)｜PASS｜2670.0円｜💰267,000円｜oshime2389.25/SL2377.36｜⚠日程不明
  > 📌【業態】情報・通信業（ソフト・システム開発・情報セキュリティ・セキュリティソフト関連）
  > 【いま】終値2,670円・直近5日+14.94%（材料未確認）
  > 【調子】⚡好調（7/13） — E軸判定不能(進捗データ不足)
  > 【水準】⚪妥当（3.0/7）— PER18.6倍・PEG0.57・52週99% ／ 💰単元26.7万円
  > 【戦略】2389.25円までの押し目を指値で待つ。SL2377.36円（25日線基準）
- 146A Columbia Works Inc.｜granville_oshime｜⚡好調(7/13)｜—｜FAIL_UWAHIGE｜3720.0円｜💰—｜—｜
- 194A WOLVES HAND Co.,Ltd.｜granville_oshime/granville_rebound｜⚡好調(7/13)｜—｜FAIL_INSEN｜1670.0円｜💰—｜—｜
- 4471 Sanyo Chemical Industries, Ltd.｜granville_oshime｜⚡好調(7/13)｜—｜FAIL_UWAHIGE｜6390.0円｜💰—｜—｜
- 4919 ミルボン｜granville_oshime｜⚡好調(7/13)｜—｜FAIL_UWAHIGE｜3235.0円｜💰—｜—｜
- 5186 Nitta Corporation｜granville_oshime｜⚡好調(7/13)｜—｜FAIL_INSEN｜6890.0円｜💰—｜—｜
- 9902 Nichiden Corporation｜granville_oshime｜⚡好調(7/13)｜—｜FAIL_INSEN｜3250.0円｜💰—｜—｜
- 7609 Daitron Co., Ltd.｜granville_oshime/granville_rebound｜⚡好調(6/13)｜⚪妥当(4.0/7)｜PASS｜4290.0円｜💰429,000円｜oshime4061.41/SL4041.2｜⚠日程不明
  > 📌【業態】電子部品卸中堅。製造装置にも強み。スイッチ電源など自社製造製品に注力。
  > 【いま】終値4,290円・直近5日+11.00%（材料未確認）
  > 【調子】⚡好調（6/13） — E軸判定不能(進捗データ不足)
  > 【水準】⚪妥当（4.0/7）— PER14.0倍・PEG0.50・52週78% ／ 💰単元42.9万円
  > 【戦略】4061.41円までの押し目を指値で待つ。SL4041.2円（25日線基準）
- 4968 荒川化学工業｜granville_oshime｜⚡好調(6/13)｜🟡やや割高(2.0/7)｜PASS｜2398.0円｜💰239,800円｜oshime2196.69/SL2185.76｜⚠日程不明
  > 📌【業態】化学（ファインケミカル・接着剤・製紙関連）
  > 【いま】終値2,398円・直近5日+17.84%（材料未確認）
  > 【調子】⚡好調（6/13）
  > 【水準】🟡やや割高（2.0/7）— PER21.1倍・PEG1.23・52週83% ／ 💰単元24.0万円
  > 【戦略】2196.69円までの押し目を指値で待つ。SL2185.76円（25日線基準）
- 6570 共和コーポレーション｜granville_oshime｜⚡好調(6/13)｜🟡やや割高(2.0/7)｜PASS｜3805.0円｜💰380,500円｜oshime3764.53/SL3745.8｜⚠日程不明
  > 📌【業態】アミューズメント施設運営やゲーム機器の販売。業界、高シェア。長野から全国展開。
  > 【いま】終値3,805円・直近5日+9.34%（材料未確認）
  > 【調子】⚡好調（6/13） — 質注意
  > 【水準】🟡やや割高（2.0/7）— PER18.7倍・PEG1.30・52週81% ／ 💰単元38.0万円
  > 【戦略】3764.53円までの押し目を指値で待つ。SL3745.8円（25日線基準）
- 8022 Mizuno Corporation｜granville_oshime｜⚡好調(6/13)｜🔴過熱(1.0/7)｜PASS｜4105.0円｜💰410,500円｜oshime4069.04/SL4048.8｜⚠日程不明
  > 📌【業態】スポーツ用品大手。ゴルフ・野球・競泳に強み。ブランド力に定評。海外強化。
  > 【いま】終値4,105円・直近5日+2.50%（材料未確認）
  > 【調子】⚡好調（6/13）
  > 【水準】🔴過熱（1.0/7）— PER16.4倍・PEG1.57・52週81% ／ 💰単元41.0万円
  > 【戦略】4069.04円までの押し目を指値で待つ。SL4048.8円（25日線基準）
- 1899 福田組｜granville_oshime｜⚡好調(6/13)｜—｜FAIL_INSEN｜4765.0円｜💰—｜—｜
- 2652 Mandarake Inc.｜granville_oshime｜⚡好調(6/13)｜—｜FAIL_INSEN｜422.0円｜💰—｜—｜
- 3048 ビックカメラ｜granville_oshime｜⚡好調(6/13)｜—｜FAIL_UWAHIGE｜1724.5円｜💰—｜—｜
- 3994 Money Forward, Inc.｜granville_oshime｜⚡好調(6/13)｜—｜FAIL_INSEN｜5703.0円｜💰—｜—｜
- 4417 グローバルセキュリティエキスパート｜granville_oshime｜⚡好調(6/13)｜—｜FAIL_INSEN｜5660.0円｜💰—｜—｜
- 5632 三菱製鋼｜granville_oshime｜⚡好調(6/13)｜—｜FAIL_INSEN｜2570.0円｜💰—｜—｜
- 6250 Yamabiko Corporation｜granville_oshime｜⚡好調(6/13)｜—｜FAIL_INSEN｜4440.0円｜💰—｜—｜
- 6668 Adtec Plasma Technology Co., Ltd.｜granville_oshime｜⚡好調(6/13)｜—｜FAIL_UWAHIGE｜4280.0円｜💰—｜—｜
- 9075 Fukuyama Transporting Co., Ltd.｜granville_oshime｜⚡好調(6/13)｜—｜FAIL_INSEN｜6370.0円｜💰—｜—｜
- 6958 日本シイエムケイ｜granville_oshime｜⚡好調(5/13)｜🟡やや割高(2.0/7)｜PASS｜804.0円｜💰80,400円｜oshime755.8/SL752.04｜⚠日程不明
  > 📌【業態】プリント配線板の最大手。自動車、電機向けが主力。高付加価値品強化。
  > 【いま】終値804円・直近5日+9.54%（材料未確認）
  > 【調子】⚡好調（5/13）
  > 【水準】🟡やや割高（2.0/7）— PER19.1倍・PEG1.40・52週98% ／ 💰単元8.0万円
  > 【戦略】755.8円までの押し目を指値で待つ。SL752.04円（25日線基準）
- 8005 Scroll Corporation｜granville_oshime/granville_rebound｜⚡好調(5/13)｜🟡やや割高(2.0/7)｜PASS｜1793.0円｜💰179,300円｜⛔型不一致: 既に支持帯以下｜⚠日程不明
  > 📌【業態】カタログ・ネット通販大手。女性向けアパレルや生活雑貨主力。決済代行・物流も。
  > 【いま】終値1,793円・直近5日+1.93%（材料未確認）
  > 【調子】⚡好調（5/13） — 上方修正済み
  > 【水準】🟡やや割高（2.0/7）— PER12.6倍・PEG2.32・52週86% ／ 💰単元17.9万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 3399 Maruchiyo Yamaokaya Corporation｜granville_oshime｜⚡好調(5/13)｜—｜FAIL_INSEN｜3855.0円｜💰—｜—｜
- 3480 JSB Co. Ltd.｜granville_oshime｜⚡好調(5/13)｜—｜SKIP｜None円｜💰—｜—｜
- 4674 クレスコ｜granville_oshime/granville_rebound｜⚡好調(5/13)｜—｜FAIL_INSEN｜1841.0円｜💰—｜—｜
- 7350 Okinawa Financial Group, Inc.｜granville_oshime｜⚡好調(5/13)｜—｜FAIL_INSEN｜7930.0円｜💰—｜—｜
- 7721 Tokyo Keiki Inc.｜granville_oshime｜⚡好調(5/13)｜—｜FAIL_INSEN｜7320.0円｜💰—｜—｜
- 9934 Inaba Denki Sangyo Co.,Ltd.｜granville_oshime｜⚡好調(5/13)｜—｜FAIL_INSEN｜3118.0円｜💰—｜—｜
- 3034 Qol Holdings Co., Ltd.｜granville_oshime/granville_rebound｜✅順調(4/13)｜—｜FAIL_UWAHIGE｜2345.0円｜💰—｜—｜
- 4092 日本化学工業｜granville_oshime｜✅順調(4/13)｜—｜FAIL_UWAHIGE｜5740.0円｜💰—｜—｜
- 4390 アイ・ピー・エス｜granville_oshime｜✅順調(4/13)｜—｜FAIL_UWAHIGE｜4160.0円｜💰—｜—｜
- 5121 藤倉ゴム工業｜granville_oshime｜✅順調(4/13)｜—｜FAIL_UWAHIGE｜2895.0円｜💰—｜—｜
- 5208 有沢製作所｜granville_oshime｜✅順調(4/13)｜—｜FAIL_UWAHIGE｜2720.0円｜💰—｜—｜
- 6418 Japan Cash Machine Co., Ltd.｜granville_oshime｜✅順調(4/13)｜—｜FAIL_INSEN｜1268.0円｜💰—｜—｜
- 8159 Tachibana Eletech Co., Ltd.｜granville_oshime｜✅順調(4/13)｜—｜FAIL_UWAHIGE｜4290.0円｜💰—｜—｜
- 8395 Bank of Saga Ltd.｜granville_oshime｜⚠減速(4/13)｜—｜FAIL_INSEN｜6720.0円｜💰—｜—｜
- 9678 Kanamoto Co., Ltd.｜granville_oshime｜✅順調(4/13)｜—｜FAIL_UWAHIGE｜5420.0円｜💰—｜—｜
- 1515 Nittetsu Mining Co., Ltd.｜granville_oshime｜🔻悪化(3/13)｜—｜FAIL_INSEN｜3275.0円｜💰—｜—｜
- 4208 UBE｜granville_oshime｜✅順調(3/13)｜—｜FAIL_INSEN｜3425.0円｜💰—｜—｜
- 5985 SUNCALL CORPORATION｜granville_oshime｜✅順調(3/13)｜—｜FAIL_INSEN｜2416.0円｜💰—｜—｜
- 8876 Relo Group, Inc.｜granville_oshime｜✅順調(3/13)｜—｜FAIL_UWAHIGE｜2294.5円｜💰—｜—｜
- 9010 Fuji Kyuko Co., Ltd.｜granville_oshime｜✅順調(3/13)｜—｜FAIL_UWAHIGE｜2644.0円｜💰—｜—｜
- 4189 KH Neochem Co.,Ltd.｜granville_oshime｜⚠減速(2/13)｜—｜FAIL_UWAHIGE｜3235.0円｜💰—｜—｜
- 6363 酉島製作所｜granville_oshime/granville_rebound｜➖横ばい(2/13)｜—｜FAIL_UWAHIGE｜2956.0円｜💰—｜—｜
- 8337 千葉興業銀行｜granville_oshime｜➖横ばい(2/13)｜—｜FAIL_INSEN｜2667.0円｜💰—｜—｜
- 3946 Tomoku Co., Ltd.｜granville_oshime｜⚠減速(1/13)｜—｜FAIL_INSEN｜4445.0円｜💰—｜—｜
- 4228 Sekisui Kasei Co., Ltd.｜granville_oshime｜⚠減速(1/13)｜—｜FAIL_INSEN｜615.0円｜💰—｜—｜
- 3612 ワールド｜granville_oshime｜業績データ取得不可｜—｜FAIL_UWAHIGE｜1602.0円｜💰—｜—｜
- 3697 SHIFT Inc.｜granville_oshime｜取得不可｜—｜FAIL_UWAHIGE｜885.0999755859375円｜💰—｜—｜
- 3778 SAKURA Internet Inc.｜granville_oshime｜業績データ取得不可｜—｜FAIL_UWAHIGE｜3830.0円｜💰—｜—｜
- 3993 ＰＫＳＨＡ　ＴＥＣＨＮＯＬＯＧＹ｜granville_oshime｜業績データ取得不可｜—｜FAIL_UWAHIGE｜3205.0円｜💰—｜—｜
- 4478 freee K.K.｜granville_oshime｜業績データ取得不可｜—｜FAIL_INSEN｜3750.0円｜💰—｜—｜
- 4765 ＳＢＩグローバルアセットマネジメント｜granville_oshime｜判定保留｜—｜FAIL_INSEN｜628.0円｜💰—｜—｜
- 6045 Rentracks Co., Ltd.｜granville_oshime｜判定保留(変則決算)｜—｜FAIL_INSEN｜2093.0円｜💰—｜—｜
- 6810 Maxell, Ltd.｜granville_oshime｜取得不可｜—｜FAIL_INSEN｜2560.0円｜💰—｜—｜
- 8360 Yamanashi Chuo Bank, Ltd.｜granville_oshime｜取得不可｜—｜FAIL_INSEN｜7300.0円｜💰—｜—｜
- 8544 Keiyo Bank, Ltd.｜granville_oshime｜取得不可｜—｜FAIL_INSEN｜2838.0円｜💰—｜—｜
- 8707 IwaiCosmo Holdings, Inc.｜granville_oshime｜取得不可｜—｜FAIL_INSEN｜4655.0円｜💰—｜—｜
- 9166 ＧＥＮＤＡ｜granville_oshime｜業績データ取得不可｜—｜FAIL_INSEN｜677.0円｜💰—｜—｜
- 6134 富士機械製造｜granville_rebound｜🚀確変(11/13)｜⚪妥当(3.0/7)｜PASS｜7399.0円｜💰739,900円｜reversal7399/SL6595｜⚠1単元でリスク枠超過（80400円）
  > 📌【業態】電子部品組立など自動装着装置で首位。スマホ向けや自動車用工作機械も。
  > 【いま】終値7,399円・直近5日+10.53%（材料未確認）
  > 【調子】🚀確変（11/13）
  > 【水準】⚪妥当（3.0/7）— PER14.8倍・PEG0.16・52週76% ／ 💰単元74.0万円
  > 【戦略】当日終値7399.0円の指値で反転を取りにいく。SL6595.0円（直近5日安値）／⚠1単元でリスク枠超過（80400円）
- 3753 フライトソリューションズ｜granville_rebound｜🚀確変(11/13)｜—｜FAIL_INSEN｜210.0円｜💰—｜—｜
- 7878 Kohsai Co.Ltd.｜granville_rebound｜🚀確変(11/13)｜—｜FAIL_INSEN｜1159.0円｜💰—｜—｜
- 2693 YKT Corporation｜granville_rebound｜🔥絶好調(10/13)｜—｜FAIL_INSEN｜285.0円｜💰—｜—｜
- 6264 Marumae Co., Ltd.｜granville_rebound｜🔥絶好調(10/13)｜—｜FAIL_UWAHIGE｜1895.0円｜💰—｜—｜
- 6407 CKD Corporation｜granville_rebound｜🔥絶好調(10/13)｜—｜FAIL_UWAHIGE｜5200.0円｜💰—｜—｜
- 6997 Nippon Chemi-Con Corporation｜granville_rebound｜🔥絶好調(10/13)｜—｜FAIL_INSEN｜2795.0円｜💰—｜—｜
- 9237 Emimen Co.,Ltd.｜granville_rebound｜🔥絶好調(10/13)｜—｜FAIL_INSEN｜842.0円｜💰—｜—｜
- 7453 Ryohin Keikaku Co., Ltd.｜granville_rebound｜🔥絶好調(9/13)｜⚪妥当(3.0/7)｜PASS｜3943.0円｜💰394,300円｜⛔提案なし(指名鮮度切れ 12営業日)｜⚠日程不明
  > 📌【業態】小売業（雑貨・日用品・カジュアル衣料関連）
  > 【いま】終値3,943円・直近5日-2.76%（材料未確認）
  > 【調子】🔥絶好調（9/13） — E軸判定不能(進捗データ不足)
  > 【水準】⚪妥当（3.0/7）— PER31.2倍・PEG0.85・52週66% ／ 💰単元39.4万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 12営業日)）
- 3168 ＭＥＲＦ｜granville_rebound｜🔥絶好調(9/13)｜—｜FAIL_INSEN｜1273.0円｜💰—｜—｜
- 3449 Technoflex Corporation｜granville_rebound｜🔥絶好調(9/13)｜—｜FAIL_INSEN｜4445.0円｜💰—｜—｜
- 4631 ＤＩＣ｜granville_rebound｜🔥絶好調(9/13)｜—｜FAIL_UWAHIGE｜4813.0円｜💰—｜—｜
- 6481 ＴＨＫ｜granville_rebound｜🔥絶好調(9/13)｜—｜FAIL_INSEN｜6235.0円｜💰—｜—｜
- 6914 オプテックス｜granville_rebound｜🔥絶好調(9/13)｜—｜FAIL_UWAHIGE｜3270.0円｜💰—｜—｜
- 6976 Taiyo Yuden Co., Ltd.｜granville_rebound｜🔥絶好調(9/13)｜—｜FAIL_INSEN｜8935.0円｜💰—｜—｜
- 6981 村田製作所｜granville_rebound｜🔥絶好調(9/13)｜—｜FAIL_INSEN｜7823.0円｜💰—｜—｜
- 9880 Innotech Corporation｜granville_rebound｜🔥絶好調(9/13)｜—｜FAIL_INSEN｜3490.0円｜💰—｜—｜
- 6125 Okamoto Machine Tool Works,Ltd.｜granville_rebound｜🔥絶好調(8/13)｜🟢値頃(5.0/7)｜PASS｜4805.0円｜💰480,500円｜⛔提案なし(指名鮮度切れ 17営業日)｜⚠日程不明
  > 📌【業態】工作機械中堅。平面研削盤首位。半導体関連装置も注力。三井物産と提携。
  > 【いま】終値4,805円・直近5日+7.74%（材料未確認）
  > 【調子】🔥絶好調（8/13） — E軸判定不能(進捗データ不足)
  > 【水準】🟢値頃（5.0/7）— PER15.9倍・PEG0.18・52週49% ／ 💰単元48.0万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 17営業日)）
- 6965 Hamamatsu Photonics K.K.｜granville_rebound｜🔥絶好調(8/13)｜⚪妥当(3.0/7)｜FAIL_UWAHIGE｜2316.0円｜💰231,600円｜—｜
- 1407 West Holdings Corporation｜granville_rebound｜🔥絶好調(8/13)｜—｜FAIL_INSEN｜2188.0円｜💰—｜—｜
- 4051 GMO Financial Gate, Inc.｜granville_rebound｜🔥絶好調(8/13)｜—｜FAIL_UWAHIGE｜6170.0円｜💰—｜—｜
- 4392 ＦＩＧ｜granville_rebound｜🔥絶好調(8/13)｜—｜FAIL_INSEN｜983.0円｜💰—｜—｜
- 4424 Amazia, Inc.｜granville_rebound｜🔥絶好調(8/13)｜—｜FAIL_UWAHIGE｜321.0円｜💰—｜—｜
- 5713 Sumitomo Metal Mining Co., Ltd.｜granville_rebound｜🔥絶好調(8/13)｜—｜FAIL_INSEN｜9538.0円｜💰—｜—｜
- 7733 Olympus Corp.｜granville_rebound｜🔥絶好調(8/13)｜—｜FAIL_INSEN｜1995.0円｜💰—｜—｜
- 8050 SEIKO GROUP CORPORATION｜granville_rebound｜🔥絶好調(8/13)｜—｜FAIL_INSEN｜10200.0円｜💰—｜—｜
- 3405 Kuraray Co., Ltd.｜granville_rebound｜⚡好調(7/13)｜⚪妥当(4.0/7)｜PASS｜1804.0円｜💰180,400円｜⛔提案なし(指名鮮度切れ 15営業日)｜⚠日程不明
  > 📌【業態】化学品大手。高分子機能素材・フィルムに強み。樹脂の世界トップ製品多数。
  > 【いま】終値1,804円・直近5日+1.12%（材料未確認）
  > 【調子】⚡好調（7/13）
  > 【水準】⚪妥当（4.0/7）— PER13.6倍・PEG0.56・52週52% ／ 💰単元18.0万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 15営業日)）
- 2933 KIBUN FOODS INC.｜granville_rebound｜⚡好調(7/13)｜—｜FAIL_INSEN｜1125.0円｜💰—｜—｜
- 3660 アイスタイル｜granville_rebound｜⚡好調(7/13)｜—｜FAIL_INSEN｜500.0円｜💰—｜—｜
- 7089 フォースタートアップス｜granville_rebound｜⚡好調(7/13)｜—｜FAIL_UWAHIGE｜1438.0円｜💰—｜—｜
- 8065 SATO SHO-JI CORPORATION｜granville_rebound｜⚡好調(7/13)｜—｜FAIL_INSEN｜3100.0円｜💰—｜—｜
- 9115 Meiji Shipping Group Co. Ltd.｜granville_rebound｜⚡好調(7/13)｜—｜FAIL_INSEN｜1060.0円｜💰—｜—｜
- 8011 Sanyo Shokai Ltd.｜granville_rebound｜⚡好調(6/13)｜💎割安(7.0/7)｜FAIL_INSEN｜1368.0円｜💰136,800円｜—｜
- 6336 Ishii Hyoki Co., Ltd.｜granville_rebound｜⚡好調(6/13)｜⚪妥当(5.6/7)｜PASS｜1483.0円｜💰148,300円｜reversal1483/SL1316｜⚠日程不明
  > 📌【業態】未取得（次回以降に取得）
  > 【いま】終値1,483円・直近5日+5.03%（材料未確認）
  > 【調子】⚡好調（6/13）
  > 【水準】⚪妥当（5.6/7）— PER11.1倍・PEG0.43・52週51% ／ 💰単元14.8万円
  > 【戦略】当日終値1483.0円の指値で反転を取りにいく。SL1316.0円（直近5日安値）
- 6470 Taiho Kogyo Co., Ltd.｜granville_rebound｜⚡好調(6/13)｜⚪妥当(4.0/7)｜PASS｜1141.0円｜💰114,100円｜reversal1141/SL1053｜
  > 📌【業態】トヨタ系。自動車向け軸受けやアルミダイカスト製品、金型が軸。EV向け製品に積極。
  > 【いま】終値1,141円・直近5日+7.24%（材料未確認）
  > 【調子】⚡好調（6/13）
  > 【水準】⚪妥当（4.0/7）— PER9.0倍・PEG0.15・52週81% ／ 💰単元11.4万円
  > 【戦略】当日終値1141.0円の指値で反転を取りにいく。SL1053.0円（直近5日安値）
- 6952 Casio Computer Co., Ltd.｜granville_rebound｜⚡好調(6/13)｜⚪妥当(4.0/7)｜PASS｜2183.0円｜💰218,300円｜reversal2183/SL2037｜⚠日程不明
  > 📌【業態】腕時計、電子辞書でシェア高い。業務用PDA、電子レジなど法人向け事業を強化。
  > 【いま】終値2,183円・直近5日+6.57%（材料未確認）
  > 【調子】⚡好調（6/13） — D軸簡易判定(四半期詳細未取得のため中立値)
  > 【水準】⚪妥当（4.0/7）— PER20.4倍・PEG0.63・52週74% ／ 💰単元21.8万円
  > 【戦略】当日終値2183.0円の指値で反転を取りにいく。SL2037.0円（直近5日安値）
- 6227 AIMECHATEC Ltd.｜granville_rebound｜⚡好調(6/13)｜—｜FAIL_UWAHIGE｜6610.0円｜💰—｜—｜
- 7245 大同メタル工業｜granville_rebound｜⚡好調(6/13)｜—｜FAIL_UWAHIGE｜1153.0円｜💰—｜—｜
- 7606 UNITED ARROWS LTD.｜granville_rebound｜⚡好調(6/13)｜—｜FAIL_UWAHIGE｜2405.0円｜💰—｜—｜
- 3093 Treasure Factory Co., Ltd.｜granville_rebound｜⚡好調(5/13)｜⚪妥当(4.0/7)｜PASS｜1977.0円｜💰197,700円｜reversal1977/SL1873｜📋カルテ窓 10/14(残14営業日)
  > 📌【業態】首都圏でリサイクル店を展開。家電・家具・雑貨など品揃え多彩。専門店も展開。
  > 【いま】終値1,977円・直近5日+4.27%（材料未確認）
  > 【調子】⚡好調（5/13）
  > 【水準】⚪妥当（4.0/7）— PER13.1倍・PEG1.34・52週51% ／ 💰単元19.8万円
  > 【戦略】当日終値1977.0円の指値で反転を取りにいく。SL1873.0円（直近5日安値）
- 3763 プロシップ｜granville_rebound｜⚡好調(5/13)｜—｜FAIL_INSEN｜2144.0円｜💰—｜—｜
- 4125 SANWAYUKA INDUSTRY CORPORATION｜granville_rebound｜⚡好調(5/13)｜—｜FAIL_INSEN｜3645.0円｜💰—｜—｜
- 4612 Nippon Paint Holdings Co., Ltd.｜granville_rebound｜⚡好調(5/13)｜—｜FAIL_INSEN｜1164.0円｜💰—｜—｜
- 5889 ＪＡＰＡＮ　ＥＹＥＷＥＡＲ　ＨＯＬＤＩＮＧＳ｜granville_rebound｜⚡好調(5/13)｜—｜FAIL_UWAHIGE｜2318.0円｜💰—｜—｜
- 6191 エボラブルアジア｜granville_rebound｜🔻悪化(5/13)｜—｜FAIL_INSEN｜1545.0円｜💰—｜—｜
- 6306 Nikko Co., Ltd.｜granville_rebound｜⚡好調(5/13)｜—｜FAIL_INSEN｜1010.0円｜💰—｜—｜
- 6999 Koa Corporation｜granville_rebound｜⚡好調(5/13)｜—｜FAIL_INSEN｜2291.0円｜💰—｜—｜
- 7085 カーブス HD｜granville_rebound｜⚡好調(5/13)｜—｜FAIL_INSEN｜884.0円｜💰—｜—｜
- 3774 インターネットイニシアティブ｜granville_rebound｜✅順調(4/13)｜🔴過熱(0.0/7)｜PASS｜3443.0円｜💰344,300円｜reversal3443/SL3382｜⚠日程不明
  > 📌【業態】インターネット接続サービスで先駆。法人向けクラウド事業、セキュリティー対策、格安スマホも。
  > 【いま】終値3,443円・直近5日-0.15%（材料未確認）
  > 【調子】✅順調（4/13） — 質注意
  > 【水準】🔴過熱（0.0/7）— PER24.4倍・PEG4.90・52週87% ／ 💰単元34.4万円
  > 【戦略】当日終値3443.0円の指値で反転を取りにいく。SL3382.0円（直近5日安値）
- 3676 ハーツユナイテッドグループ｜granville_rebound｜✅順調(4/13)｜—｜FAIL_INSEN｜1048.0円｜💰—｜—｜
- 4022 Rasa Industries,Ltd.｜granville_rebound｜✅順調(4/13)｜—｜FAIL_INSEN｜1869.0円｜💰—｜—｜
- 7376 ＢＣＣ｜granville_rebound｜✅順調(4/13)｜—｜FAIL_UWAHIGE｜794.0円｜💰—｜—｜
- 9069 SENKO Group Holdings Co.Ltd.｜granville_rebound｜✅順調(4/13)｜—｜FAIL_INSEN｜2355.0円｜💰—｜—｜
- 255A Gltechno Holdings, Inc.｜granville_rebound｜✅順調(3/13)｜—｜FAIL_UWAHIGE｜5440.0円｜💰—｜—｜
- 4927 ポーラ・オルビスホールディングス｜granville_rebound｜✅順調(3/13)｜—｜FAIL_UWAHIGE｜1383.0円｜💰—｜—｜
- 7745 A&D HOLON Holdings Company. Limited｜granville_rebound｜🔻悪化(3/13)｜—｜FAIL_UWAHIGE｜2943.0円｜💰—｜—｜
- 3063 j-Group Holdings Corp.｜granville_rebound｜➖横ばい(2/13)｜—｜FAIL_INSEN｜1174.0円｜💰—｜—｜
- 7780 Menicon Co., Ltd.｜granville_rebound｜➖横ばい(2/13)｜—｜FAIL_INSEN｜1763.0円｜💰—｜—｜
- 9959 Aseed Holdings Co., Ltd.｜granville_rebound｜➖横ばい(2/13)｜—｜FAIL_INSEN｜943.0円｜💰—｜—｜
- 5310 Toyo Tanso Co., Ltd.｜granville_rebound｜🔻悪化(1/13)｜🔴過熱(1.0/7)｜PASS｜7480.0円｜💰748,000円｜⛔提案なし(指名鮮度切れ 14営業日)｜⚠日程不明 ⚠業績基調が下向き（🔻悪化）
  > 📌【業態】等方性黒鉛で先駆、世界高シェア。半導体製造用るつぼが主力。一貫生産。
  > 【いま】終値7,480円・直近5日+9.52%（材料未確認）
  > 【調子】🔻悪化（1/13） — 質注意
  > 【水準】🔴過熱（1.0/7）— PER31.4倍・PEG—・52週68% ／ 💰単元74.8万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 14営業日)）
- 5726 大阪チタニウムテクノロジーズ｜granville_rebound｜🔻悪化(1/13)｜—｜FAIL_UWAHIGE｜2408.0円｜💰—｜—｜
- 7600 日本エム・ディ・エム｜granville_rebound｜🔻悪化(1/13)｜—｜FAIL_INSEN｜660.0円｜💰—｜—｜
- 5108 ブリヂストン｜granville_rebound｜業績データ取得不可｜💎割安(6.0/7)｜PASS｜3801.0円｜💰380,100円｜reversal3801/SL3698｜⚠日程不明
  > 📌【業態】タイヤ世界大手。タイヤデータ活用に注力。海外で生産拠点拡張。新興国を拡大。
  > 【いま】終値3,801円・直近5日+1.66%（材料未確認）
  > 【調子】業績データ取得不可（None/13） — 取得不可(軸欠損:B,C)
  > 【水準】💎割安（6.0/7）— PER13.8倍・PEG—・52週51% ／ 💰単元38.0万円
  > 【戦略】当日終値3801.0円の指値で反転を取りにいく。SL3698.0円（直近5日安値）
- 4543 Terumo Corporation｜granville_rebound｜業績データ取得不可(経常益予想非開示)｜⚪妥当(3.0/7)｜PASS｜2274.5円｜💰227,450円｜reversal2274.5/SL2228.5｜⚠日程不明
  > 📌【業態】医療器具大手。心臓・血管分野に強み。カテーテルや人工心肺装置で世界高シェア。
  > 【いま】終値2,274円・直近5日+0.53%（材料未確認）
  > 【調子】業績データ取得不可(経常益予想非開示)（None/13） — 経常利益データ取得不可
  > 【水準】⚪妥当（3.0/7）— PER17.4倍・PEG—・52週47% ／ 💰単元22.7万円
  > 【戦略】当日終値2274.5円の指値で反転を取りにいく。SL2228.5円（直近5日安値）
- 4203 住友ベークライト｜granville_rebound｜業績データ取得不可｜🟡やや割高(2.0/7)｜PASS｜8030.0円｜💰803,000円｜reversal8030/SL7666｜⚠日程不明 ⚠1単元でリスク枠超過（36400円）
  > 📌【業態】化学（ファインケミカル・電子材料・半導体部材・部品関連）
  > 【いま】終値8,030円・直近5日+3.25%（材料未確認）
  > 【調子】業績データ取得不可（None/13） — 業績データ取得不可(前期比行なし)
  > 【水準】🟡やや割高（2.0/7）— PER24.7倍・PEG—・52週98% ／ 💰単元80.3万円
  > 【戦略】当日終値8030.0円の指値で反転を取りにいく。SL7666.0円（直近5日安値）／⚠1単元でリスク枠超過（36400円）
- 2914 日本たばこ産業｜granville_rebound｜業績データ取得不可｜—｜FAIL_INSEN｜6872.0円｜💰—｜—｜
- 3563 FOOD & LIFE COMPANIES LTD.｜granville_rebound｜判定保留(データ不足)｜—｜FAIL_INSEN｜4894.0円｜💰—｜—｜
- 6594 Nidec Corporation｜granville_rebound｜業績データ取得不可｜—｜FAIL_INSEN｜2822.0円｜💰—｜—｜
- 6723 Renesas Electronics Corporation｜granville_rebound｜取得不可｜—｜FAIL_INSEN｜3490.0円｜💰—｜—｜

## 変化点銘柄
- 4419 Ｆｉｎａｔｅｘｔホールディングス｜changepoint｜🔥絶好調(10/13)｜—｜FAIL_INSEN｜1406.0円｜💰—｜—｜
- 6254 野村マイクロ・サイエンス｜changepoint｜🔥絶好調(10/13)｜—｜FAIL_INSEN｜3375.0円｜💰—｜—｜
- 6866 日置電機｜changepoint｜🔥絶好調(10/13)｜—｜FAIL_UWAHIGE｜10480.0円｜💰—｜—｜
- 9308 乾汽船｜changepoint｜🔥絶好調(10/13)｜—｜FAIL_UWAHIGE｜2355.0円｜💰—｜—｜
- 4382 HEROZ, Inc.｜changepoint｜🔥絶好調(9/13)｜—｜FAIL_INSEN｜838.0円｜💰—｜—｜
- 6857 アドバンテスト｜changepoint/変化点🔔｜🔥絶好調(9/13)｜—｜FAIL_UWAHIGE｜33060.0円｜💰—｜—｜
- 8697 日本取引所グループ｜changepoint｜🔥絶好調(8/13)｜🟡やや割高(2.0/7)｜PASS｜2274.0円｜💰227,400円｜changepoint2274/SL2182.5｜⚠日程不明 📢上方修正 🔒実弾封印中(PL3紙ログ収集中)
  > 📌【業態】総合取引所。現物は東証、デリバティブは大証に集約。東京商品取引所統合。
  > 【いま】終値2,274円・直近5日+2.64%・📢上方修正今期最終を7％上方修正・最高益予想を上乗せ、配当も5円増額
  > 【調子】🔥絶好調（8/13）
  > 【水準】🟡やや割高（2.0/7）— PER23.5倍・PEG0.91・52週89% ／ 💰単元22.7万円
  > 【戦略】発火日終値2274.0円の指値。追撃禁止・SL2182.5円。🔒実弾封印中（PL3紙ログ収集中）
- 4180 ＡＰＰＩＥＲ　ＧＲＯＵＰ｜changepoint｜🔥絶好調(8/13)｜—｜FAIL_INSEN｜1488.0円｜💰—｜—｜
- 4431 スマレジ｜changepoint｜🔥絶好調(8/13)｜—｜FAIL_INSEN｜3330.0円｜💰—｜—｜
- 7318 セレンディップ・ホールディングス｜changepoint｜🔥絶好調(8/13)｜—｜FAIL_UWAHIGE｜1371.0円｜💰—｜—｜
- 478A フツパー｜changepoint｜⚡好調(7/13)｜—｜FAIL_INSEN｜741.0円｜💰—｜—｜
- 4667 アイサンテクノロジー｜changepoint/変化点🔔｜⚡好調(6/13)｜—｜FAIL_INSEN｜3260.0円｜💰—｜—｜
- 9343 アイビス｜changepoint｜⚡好調(6/13)｜—｜FAIL_INSEN｜800.0円｜💰—｜—｜
- 286A EUCALIA Inc.｜changepoint｜⚡好調(5/13)｜—｜FAIL_INSEN｜747.0円｜💰—｜—｜
- 6284 日精エー・エス・ビー機械｜changepoint｜⚡好調(5/13)｜—｜FAIL_UWAHIGE｜8550.0円｜💰—｜—｜
- 8704 トレイダーズホールディングス｜changepoint｜⚡好調(5/13)｜—｜FAIL_INSEN｜1391.0円｜💰—｜—｜
- 5337 ダントーホールディングス｜changepoint｜✅順調(4/13)｜—｜FAIL_UWAHIGE｜864.0円｜💰—｜—｜
- 593A ティアフォー｜changepoint｜✅順調(4/13)｜—｜FAIL_UWAHIGE｜2120.0円｜💰—｜—｜
- 6785 鈴木｜changepoint｜✅順調(4/13)｜—｜FAIL_UWAHIGE｜3195.0円｜💰—｜—｜
- 7374 Interworks Confidence Inc.｜changepoint｜✅順調(4/13)｜—｜FAIL_INSEN｜1516.0円｜💰—｜—｜
- 4071 プラスアルファ・コンサルティング｜changepoint｜✅順調(3/13)｜—｜FAIL_UWAHIGE｜2113.0円｜💰—｜—｜
- 3923 ラクス｜changepoint｜判定保留(変則決算)｜—｜FAIL_UWAHIGE｜1073.0円｜💰—｜—｜
- 4259 ExaWizards Inc.｜changepoint｜業績データ取得不可｜—｜FAIL_INSEN｜899.0円｜💰—｜—｜

## 分類不明銘柄（レガシーデータ）
- 5803 フジクラ｜branch=['changepoint🔔']｜FAIL_INSEN｜4911.0円

## ⚡材料後出し
その日の足は開示前の情報。判定は参考値
該当なし

## 📢開示
使用した一覧URL: https://kabutan.jp/disclosures/?kubun=kgh (会社開示情報 決算区分), https://kabutan.jp/news/marketnews/?category=3 (市場ニュース 決算カテゴリ・方向性文言の確認用)
フォールバック使用: なし
- 8697 日本取引所グループ｜📢上方修正｜2026-09-24T12:00:00+09:00｜今期最終を7％上方修正・最高益予想を上乗せ、配当も5円増額
①-9へ引き渡し: 0件（当夜のPASS/保有該当分はSTEP4で直接強制再計算済みのためqueue追加なし）

## 総当りゲート
### 5手法
- PASS（29件）: 1436(1750.0)、2685(3170.0)、2875(9722.0)、2983(1716.0)、3465(3295.0)、3723(2954.0)、4047(2400.0)、421A(3985.0)、4971(6720.0)、5110(2031.5)、5137(316.0)、5333(5366.0)、5602(1659.0)、6113(2486.0)、6235(2542.0)、6479(3606.0)、6523(1395.0)、6806(24920.0)、6838(1436.0)、6856(23530.0)、6951(7564.0)、7730(1459.0)、7731(1858.5)、7956(2027.5)、7966(5710.0)、8923(1717.0)、8976(306500.0)、8984(113700.0)、9560(913.0)
- FAIL_UWAHIGE（64件）: 135A(4915.0)、186A(1190.0)、1871(2215.0)、2264(1129.5)、268A(1631.0)、269A(3095.0)、3099(3331.0)、3104(3290.0)、325A(1954.0)、3391(2165.5)、341A(2407.0)、3433(2891.0)、3591(3960.0)、4053(504.0)、4061(3360.0)、4091(5570.0)、4099(2256.0)、4186(8290.0)、4187(4210.0)、4220(2374.0)、428A(1725.0)、4368(3035.0)、4479(987.0)、4627(1951.0)、4680(1182.5)、4996(684.0)、5027(820.0)、5254(4130.0)、5332(5859.0)、5334(7417.0)、5537(3915.0)、5582(2103.0)、558A(6200.0)、5892(2994.0)、6101(5150.0)、6141(2896.0)、6268(4759.0)、6278(14250.0)、6323(3706.0)、6368(12675.0)、6474(5460.0)、6492(15100.0)、6516(5420.0)、6622(12840.0)、6674(5480.0)、6707(6915.0)、6754(3333.0)、6804(2532.0)、6862(5590.0)、6941(8460.0)、7220(2930.0)、7352(324.0)、7532(716.0)、7678(3875.0)、7701(3962.0)、7762(2377.0)、7774(858.0)、7906(2382.0)、8016(726.0)、8934(2400.0)、9211(1557.0)、9627(5490.0)、9708(957.0)、9715(3600.0)
- FAIL_INSEN（56件）: 1332(1156.5)、2127(640.0)、2266(1102.0)、2503(2821.0)、276A(4270.0)、2801(1648.5)、3798(570.0)、3851(1429.0)、3915(2287.0)、4014(447.0)、4028(2907.0)、4258(5800.0)、4385(3554.0)、4477(337.0)、4743(1666.0)、479A(2188.0)、4912(1718.0)、505A(1391.0)、5101(6974.0)、5136(2325.0)、5344(55790.0)、5574(3345.0)、5590(724.0)、5724(3155.0)、5943(2219.0)、5991(3430.0)、6071(914.0)、6184(606.0)、6317(2570.0)、6370(7674.0)、6383(5521.0)、6457(4511.0)、6465(5350.0)、6504(13370.0)、6588(2909.0)、6617(6900.0)、6728(7431.0)、6744(4085.0)、6841(4693.0)、6996(2632.0)、7161(626.0)、7175(2112.0)、7309(17960.0)、7409(1503.0)、7550(10220.0)、7564(5220.0)、7729(17290.0)、7944(3740.0)、8086(1441.0)、8233(2120.5)、8370(5200.0)、8537(3230.0)、9251(1604.0)、9252(4115.0)、9412(2067.0)、9824(7850.0)
### グランビル
- PASS（34件）: 1982(3270.0)、2384(5320.0)、2760(4505.0)、3040(2670.0)、3093(1977.0)、3405(1804.0)、3498(7480.0)、3774(3443.0)、4203(8030.0)、4272(2131.5)、4543(2274.5)、4694(3685.0)、4967(5885.0)、4968(2398.0)、5108(3801.0)、5310(7480.0)、6125(4805.0)、6134(7399.0)、6336(1483.0)、6470(1141.0)、6570(3805.0)、6706(3365.0)、6834(6040.0)、6952(2183.0)、6958(804.0)、7276(2667.0)、7453(3943.0)、7609(4290.0)、7806(8170.0)、8005(1793.0)、8022(4105.0)、8151(1885.0)、9470(1073.0)、9987(5400.0)
- FAIL_UWAHIGE（62件）: 146A(3720.0)、2002(2013.5)、212A(2832.0)、2160(3395.0)、2267(2803.0)、2325(4595.0)、255A(5440.0)、3034(2345.0)、3048(1724.5)、3549(3976.0)、3608(1237.0)、3612(1602.0)、3663(1856.0)、3697(885.0999755859375)、3778(3830.0)、3854(2162.0)、3993(3205.0)、4051(6170.0)、4092(5740.0)、4189(3235.0)、4390(4160.0)、4424(321.0)、4471(6390.0)、4631(4813.0)、4666(2008.5)、4919(3235.0)、4927(1383.0)、5121(2895.0)、5208(2720.0)、5726(2408.0)、5889(2318.0)、6167(1008.0)、6227(6610.0)、6264(1895.0)、6310(1969.0)、6328(2391.0)、6339(1215.0)、6363(2956.0)、6407(5200.0)、6668(4280.0)、6730(1233.0)、6807(2570.0)、6914(3270.0)、6927(996.0)、6928(3115.0)、6946(7450.0)、6965(2316.0)、7089(1438.0)、7245(1153.0)、7376(794.0)、7480(3605.0)、7606(2405.0)、7745(2943.0)、7981(3110.0)、8056(4793.0)、8129(4063.0)、8159(4290.0)、8876(2294.5)、9010(2644.0)、9468(3656.0)、9678(5420.0)、9744(3482.0)
- FAIL_INSEN（128件）: 1377(4390.0)、1407(2188.0)、1515(3275.0)、1721(5593.0)、1820(5692.0)、1833(5750.0)、1887(548.0)、1899(4765.0)、1911(1215.0)、1946(2275.0)、194A(1670.0)、1968(2551.0)、1980(2945.0)、2281(2389.0)、2432(2548.5)、2652(422.0)、2693(285.0)、2914(6872.0)、2931(347.0)、2933(1125.0)、2986(2926.0)、3036(3370.0)、3053(202.0)、3063(1174.0)、3168(1273.0)、3399(3855.0)、3449(4445.0)、3452(1455.0)、3563(4894.0)、3569(3290.0)、3660(500.0)、3676(1048.0)、3753(210.0)、3763(2144.0)、3946(4445.0)、3994(5703.0)、4005(588.2000122070312)、4022(1869.0)、4125(3645.0)、4183(2150.0)、4208(3425.0)、4228(615.0)、4274(1132.0)、4350(519.0)、4375(684.0)、4377(2362.0)、4392(983.0)、4413(2965.0)、4417(5660.0)、4478(3750.0)、4480(2356.0)、4612(1164.0)、4674(1841.0)、4765(628.0)、4956(1510.0)、5071(1401.0)、5186(6890.0)、5408(643.0)、5423(1712.0)、5461(2120.0)、5480(5450.0)、5632(2570.0)、5702(1818.0)、5703(2985.0)、5713(9538.0)、5714(8964.0)、5851(2736.0)、5985(2416.0)、6045(2093.0)、6191(1545.0)、6250(4440.0)、6306(1010.0)、6326(2750.5)、6395(1370.0)、6412(2197.0)、6418(1268.0)、6481(6235.0)、6594(2822.0)、6723(3490.0)、6794(3255.0)、6810(2560.0)、6966(901.0)、6976(8935.0)、6981(7823.0)、6997(2795.0)、6999(2291.0)、7085(884.0)、7198(840.0)、7199(2118.0)、7211(367.5)、7269(1991.0)、7270(2628.0)、7350(7930.0)、7600(660.0)、7721(7320.0)、7733(1995.0)、7780(1763.0)、7878(1159.0)、7994(2340.0)、8002(4878.0)、8011(1368.0)、8050(10200.0)、8060(3679.0)、8065(3100.0)、8093(1809.0)、8253(4590.0)、8337(2667.0)、8360(7300.0)、8395(6720.0)、8544(2838.0)、8562(385.0)、8707(4655.0)、8803(2370.0)、9007(1775.5)、9031(3075.0)、9045(3211.0)、9069(2355.0)、9075(6370.0)、9115(1060.0)、9166(677.0)、9237(842.0)、9502(2869.0)、9531(6167.0)、9628(1352.0)、9880(3490.0)、9902(3250.0)、9934(3118.0)、9959(943.0)
- SKIP（1件）: 3480(None)
### 変化点
- PASS（1件）: 8697(2274.0)
- FAIL_UWAHIGE（10件）: 3923(1073.0)、4071(2113.0)、5337(864.0)、593A(2120.0)、6284(8550.0)、6785(3195.0)、6857(33060.0)、6866(10480.0)、7318(1371.0)、9308(2355.0)
- FAIL_INSEN（12件）: 286A(747.0)、4180(1488.0)、4259(899.0)、4382(838.0)、4419(1406.0)、4431(3330.0)、4667(3260.0)、478A(741.0)、6254(3375.0)、7374(1516.0)、8704(1391.0)、9343(800.0)

### 分類不明
- FAIL_INSEN: 5803(4911.0)

### 除籍リスト（first_seenから30暦日超・86件）
- 1375 Yukiguni Factory Co., Ltd.（first_seen 2026-08-19・36暦日経過）
- 145A L is B Corp.（first_seen 2026-08-19・36暦日経過）
- 1518 Mitsui Matsushima Holdings Co., Ltd.（first_seen 2026-08-19・36暦日経過）
- 1802 Obayashi Corporation（first_seen 2026-08-19・36暦日経過）
- 1808 Haseko Corporation（first_seen 2026-08-21・34暦日経過）
- 1812 Kajima Corporation（first_seen 2026-08-20・35暦日経過）
- 1861 Kumagai Gumi Co., Ltd.（first_seen 2026-08-19・36暦日経過）
- 1878 Daito Trust Construction Co., Ltd.（first_seen 2026-08-20・35暦日経過）
- 2001 NIPPN Corporation（first_seen 2026-08-19・36暦日経過）
- 218A Liberaware Co., Ltd.（first_seen 2026-08-20・35暦日経過）
- 2282 NH Foods Limited（first_seen 2026-08-21・34暦日経過）
- 2288 丸大食品（first_seen 2026-08-19・36暦日経過）
- 2334 Eole, Inc.（first_seen 2026-08-19・36暦日経過）
- 2579 Coca-Cola Bottlers Japan Holdings Inc.（first_seen 2026-08-19・36暦日経過）
- 2585 LIFEDRINK COMPANY INC.（first_seen 2026-08-19・36暦日経過）
- 2590 DyDo Group Holdings, Inc.（first_seen 2026-08-19・36暦日経過）
- 2594 Key Coffee Inc.（first_seen 2026-08-24・31暦日経過）
- 2733 Arata Corporation（first_seen 2026-08-20・35暦日経過）
- 2768 Sojitz Corp.（first_seen 2026-08-21・34暦日経過）
- 277A Globe-Ing, Inc.（first_seen 2026-08-21・34暦日経過）
- 3064 ＭＯＮＯＴＡＲＯ（first_seen 2026-08-19・36暦日経過）
- 3076 あい　ホールディングス（first_seen 2026-08-19・36暦日経過）
- 3086 J. FRONT RETAILING Co., Ltd.（first_seen 2026-08-19・36暦日経過）
- 3116 Toyota Boshoku Corp.（first_seen 2026-08-24・31暦日経過）
- 3191 Joyful Honda Co. Ltd.（first_seen 2026-08-20・35暦日経過）
- 3222 United Super Markets Holdings, Inc.（first_seen 2026-08-24・31暦日経過）
- 3288 オープンハウスグループ（first_seen 2026-08-19・36暦日経過）
- 3289 Tokyu Fudosan Holdings Corp.（first_seen 2026-08-20・35暦日経過）
- 3479 TKP Corporation（first_seen 2026-08-19・36暦日経過）
- 3932 Akatsuki, Inc.（first_seen 2026-08-19・36暦日経過）
- 4475 ＨＥＮＮＧＥ（first_seen 2026-08-24・31暦日経過）
- 4488 AI inside Inc.（first_seen 2026-08-19・36暦日経過）
- 4493 Cyber Security Cloud, Inc.（first_seen 2026-08-24・31暦日経過）
- 4507 塩野義製薬（first_seen 2026-08-20・35暦日経過）
- 4553 Towa Pharmaceutical Co., Ltd.（first_seen 2026-08-19・36暦日経過）
- 4718 Waseda Academy Co., Ltd.（first_seen 2026-08-20・35暦日経過）
- 4722 Future Corporation（first_seen 2026-08-24・31暦日経過）
- 4973 Japan Pure Chemical Co., Ltd.（first_seen 2026-08-24・31暦日経過）
- 5105 Toyo Tire Corporation（first_seen 2026-08-19・36暦日経過）
- 5232 Sumitomo Osaka Cement Co., Ltd.（first_seen 2026-08-20・35暦日経過）
- 5246 ELEMENTS,Inc.（first_seen 2026-08-20・35暦日経過）
- 5444 Yamato Kogyo Co., Ltd.（first_seen 2026-08-20・35暦日経過）
- 5592 Kusurinomadoguchi, Inc.（first_seen 2026-08-21・34暦日経過）
- 5885 GDEP ADVANCE,Inc.（first_seen 2026-08-19・36暦日経過）
- 5938 LIXIL Corporation（first_seen 2026-08-19・36暦日経過）
- 598A CHATPLUS CO LTD（first_seen 2026-08-19・36暦日経過）
- 6013 タクマ（first_seen 2026-08-21・34暦日経過）
- 6103 Okuma Corporation（first_seen 2026-08-20・35暦日経過）
- 6136 オーエスジー（first_seen 2026-08-24・31暦日経過）
- 6222 Shima Seiki Mfg. Ltd.（first_seen 2026-08-19・36暦日経過）
- 6425 Universal Entertainment Corporation（first_seen 2026-08-24・31暦日経過）
- 6432 Takeuchi Mfg.Co., Ltd.（first_seen 2026-08-21・34暦日経過）
- 6454 Max Co., Ltd.（first_seen 2026-08-20・35暦日経過）
- 6544 Japan Elevator Service Holdings Co., Ltd.（first_seen 2026-08-19・36暦日経過）
- 6630 YA-MAN Ltd.（first_seen 2026-08-19・36暦日経過）
- 6770 Alps Alpine Co., Ltd.（first_seen 2026-08-20・35暦日経過）
- 6845 Azbil Corporation（first_seen 2026-08-21・34暦日経過）
- 7128 UNISOL Holdings Corporation（first_seen 2026-08-19・36暦日経過）
- 7157 ライフネット生命保険（first_seen 2026-08-19・36暦日経過）
- 7202 Isuzu Motors Limited（first_seen 2026-08-19・36暦日経過）
- 7278 Exedy Corporation（first_seen 2026-08-21・34暦日経過）
- 7287 Nippon Seiki Co., Ltd.（first_seen 2026-08-21・34暦日経過）
- 7459 MEDIPAL HOLDINGS Corporation（first_seen 2026-08-19・36暦日経過）
- 7581 Saizeriya Co., Ltd.（first_seen 2026-08-20・35暦日経過）
- 7649 Sugi Holdings Co., Ltd.（first_seen 2026-08-19・36暦日経過）
- 7716 Nakanishi Inc.（first_seen 2026-08-24・31暦日経過）
- 7740 タムロン（first_seen 2026-08-24・31暦日経過）
- 7911 TOPPAN Holdings Inc.（first_seen 2026-08-24・31暦日経過）
- 7972 ITOKI Corporation（first_seen 2026-08-19・36暦日経過）
- 8111 Goldwin Inc.（first_seen 2026-08-19・36暦日経過）
- 8139 Nagahori Corporation（first_seen 2026-08-24・31暦日経過）
- 8387 Shikoku Bank Ltd.（first_seen 2026-08-21・34暦日経過）
- 8439 Tokyo Century Corporation（first_seen 2026-08-19・36暦日経過）
- 8566 Ricoh Leasing Company,Ltd.（first_seen 2026-08-19・36暦日経過）
- 8614 Toyo Securities Co., Ltd.（first_seen 2026-08-19・36暦日経過）
- 8750 Daiichi Life Group. Inc.（first_seen 2026-08-19・36暦日経過）
- 8793 ＮＥＣキャピタルソリューション（first_seen 2026-08-21・34暦日経過）
- 9006 Keikyu Corporation（first_seen 2026-08-19・36暦日経過）
- 9044 NANKAI Co., Ltd.（first_seen 2026-08-20・35暦日経過）
- 9065 Sankyu Inc.（first_seen 2026-08-19・36暦日経過）
- 9279 ギフトホールディングス（first_seen 2026-08-24・31暦日経過）
- 9404 Nippon Television Holdings, Inc.（first_seen 2026-08-24・31暦日経過）
- 9467 Alphapolis Co., Ltd.（first_seen 2026-08-24・31暦日経過）
- 9616 Kyoritsu Maintenance Co., Ltd.（first_seen 2026-08-20・35暦日経過）
- 9735 Secom Co., Ltd.（first_seen 2026-08-19・36暦日経過）
- 9861 Yoshinoya Holdings Co., Ltd.（first_seen 2026-08-20・35暦日経過）

## 機械詳細
- 検知内訳: PASS64/PASS_DOJI0/FAIL_UWAHIGE136/FAIL_INSEN197/SKIP1（pool398件ベース）。評価全体(pool+前夜proposals差分)は400件
- SKIP銘柄: {'3480': 'stale'}
- pool更新: 新規8件・既存last_seen更新61件・除籍86件・最終pool398件
- night_gate.log追記件数: 1件（base_day=2026-09-24、最新30営業日保持）
- 通知抜粋件数: 10件（method5/granville4/changepoint1/不明0）
- gate_historyの書き込み結果: gate_history/2026-09-24.json 新規作成（verdicts400件・nominations61件）
- grades.json: 681銘柄/251KB
- method_score: 保持44件／null354件
- ヘッドライン付与件数: 64件（PASS64件と一致: はい）
- kabutan新規取得件数: 業態5件＋業種埋め戻し44件（打ち切りなし・50件上限中49件使用）
- profile_cache総数: 627件（本夜追加5件・業種追加44件）
- 業態が「未取得」のまま出た件数: 2件（既存キャッシュのレガシー未取得プレースホルダー）
- earnings_log: 総数14件／本夜の追記0件／リターン補完1件(212A ret_5)／プール外で埋められず0件
- gyoseki_cacheのhistory退避: 1件（8697: ⚡好調7点→🔥絶好調8点）
- pool_bars.json: 400銘柄/340KB
- 鮮度ゲート: 提案47件・鮮度切れ除外12件・nom_age分布 0-2:134/3-10:168/11+:96・last_seen欠損0件
- 記録の凍結: gate_history verdicts400件(＝評価400件)／nominations61件(新規8・再指名53)／業種 付与済み244／未付与383・本夜の埋め戻し44件・残り381件
- トレンド文脈: {'不一致（長期下向き）': 22, '合致': 59, 'レンジ': 215, '不一致': 99, '判定不能': 4}
- PASSのうちctx合致7件・形態が付いた銘柄166件（全評価対象）
- 3日ルール判定: 判定3銘柄・streak≥3 1・streak=2 0・判定不可0
- STEP4.8: week_open=falseのためスキップ
- master.jsonの変更行数: +11163/-13460（indent=2検出）
