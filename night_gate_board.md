# 夜間ゲート 2026-08-24

## サマリー
- 評価数: 341銘柄（プール341件）
- 判定内訳: PASS 66 / PASS_DOJI 4 / FAIL_UWAHIGE 80 / FAIL_INSEN 191 / SKIP 0
- PASS計 70件 → 発注可能提案 62件（除外 8件）
- 市場一言: レンジ様子見（バリューシフト）日経66016.36・SOX-0.51%
- 実行モード: 通常モード（平日実行）
- base_day: 2026-08-24
- week_open: false（STEP4.8週末ブリーフはスキップ）

## 検証結果
- V1(四者一致): proposals62件 = results entry_price保持62件 = 模擬テンプレ行数62行 = 通知母数62件 → はい
- V2(PASS収支): PASS+PASS_DOJI 70件 = 発注可能62件 + 除外8件。除外全件にorder_status記載 → はい
- V3(重複/verdict単一値): code重複0件・verdict全て単一文字列 → はい
- V4(valuation_cache static不変): 既存銘柄static変更0件（新規7716のみ追加） → はい
- V5(許可キー以外不変): night_gate/gyoseki_cache/valuation_cache/profile_cache/pipeline以外の変更0件（night_gate内もpool/results/log/recalc_queue以外不変） → はい
- V6(グレード絵文字整合): gyoseki_cache 316件チェック・不整合0件 → はい
- V7(board必須セクション): サマリー/検証結果/前夜の結果/模擬テンプレ/PASS内訳すべて存在（week_open=falseのため週末カタリストは無し） → はい
- V8(模擬テンプレ書式): 全62行で｜後に文字なし・単元記載あり・カンマなし → はい
- V9(gate_history): gate_history/2026-08-24.json 新規作成・night_gate_today.jsonとバイト一致 → はい
- V10(base_day整合): results/night_gate_today.json/gate_historyファイル名/模擬テンプレ1行目すべて2026-08-24 → はい
- V11(書き出し整形): git diff --numstat = +7640/-6604（indent=1検出・使用）。5,000行の目安を超過しているが、top-level差分キーがnight_gate/gyoseki_cache/valuation_cache/profile_cache/pipelineの5つのみであることをJSON値比較で確認済み・全体再フォーマットではない。過去実績でも同種の超過は常態（2026-08-21 PR#222: +7977/-6213／2026-08-20: +11522/-7309／2026-08-18: +6731/-4367）であり、プール341件×results全項目の毎晩全量再生成に起因する構造的な規模。インデント異常なしを確認のうえ続行 → 数値上は超過・実質は正常
- V12(並び順): proposalsの並び / 模擬テンプレのコード列 / results提案順、いずれもSTEP5.2(1)キーで独立ソートした結果と一致 → はい
- V13(grades.json): 360銘柄・93,327バイト。meta.n=stocks件数一致・gyoseki∪valuation和集合と一致・120KB以下 → はい
- V14(method_score出所): method_score非nullエントリ51件すべてmethod_score_srcも非null。値はcandidatesのscoreをそのまま複写(写し間違いなし) → はい
- V15(ヘッドライン網羅性): PASS/PASS_DOJI 70件中70件に付与(欠落0件)。5キーすべて存在。プレースホルダ「未取得（次回以降に取得）」は業態欠落時のみで他4項目への漏出なし → はい
- V16(記録の蓄積): 本夜📊決算発表0件のためearnings_log追記0件（該当なし）。gyoseki_cache history超過0件。earnings_log総数0件(1,200件以下) → はい

## 保有アラート
target/stop は未同期の目標コマンド由来（pos_targets_20260823_1245.json 2026-08-23T12:45:33+09:00）。次の週次同期で trade_master に確定します

### 9304 澁澤倉庫（現物）
- 終値2,009円 ／ コスト1,786円 ／ 含み損益+22,300円（+12.49%）
- ローソク判定: FAIL_UWAHIGE ／ ⚠足が崩れた（premise_kill）（上髭40%） ／ 25日線乖離+5.80%
- target: 2150円 ／ stop: 1920円（未同期改定 1800→1920） ／ 残存リスク: 0円（枠解放）
- 業績グレード: ⚡好調（6/13）※キャッシュ有効のため再計算なし・変化なし
- 値頃感: 🔴過熱（1.8/7）— PER15.5倍・52週87.4%
- 🔴過熱圏（15.5倍/52週87.4%）— 利確・トレール切り上げの検討材料
- 決算日程: ⚠日程不明
- タイムストップ: 含み益のため対象外

### 4413 ボードルア（信用買建）
- 終値2,980円 ／ コスト2,800円 ／ 含み損益+18,000円（+6.43%）
- ローソク判定: FAIL_INSEN ／ ⚠足が崩れた（premise_kill）（陰線・上髭57%） ／ 25日線乖離+2.82%
- target: ⚠目標未設定 ／ stop: 2870円（未同期・目標コマンド由来） ／ 残存リスク: 0円（枠解放）
- 業績グレード: 🔥絶好調（8/13）※キャッシュ有効のため再計算なし・変化なし
- 値頃感: 🟡やや割高（2.0/7）— PER29.7倍・52週79.3%
- 決算日程: ⚠日程不明
- タイムストップ: 含み益のため対象外

### 7685 BuySell Technologies（信用買建）
- 終値3,285円 ／ コスト3,080円 ／ 含み損益+20,500円（+6.66%）
- ローソク判定: FAIL_UWAHIGE ／ ⚠足が崩れた（premise_kill）（上髭41%） ／ 25日線乖離+3.73%
- target: ⚠目標未設定 ／ stop: 3165円（未同期・目標コマンド由来） ／ 残存リスク: 0円（枠解放）
- 業績グレード: 🚀確変（12/13）※キャッシュ有効のため再計算なし・変化なし
- 値頃感: 🟢値頃（5.0/7）— PER20.7倍・52週66.6%
- 決算日程: ⚠日程不明
- タイムストップ: 含み益のため対象外

### 8008 4℃HD（信用買建）
- 終値2,191円 ／ コスト2,090円 ／ 含み損益+10,100円（+4.83%）
- ローソク判定: FAIL_INSEN ／ ⚠足が崩れた（premise_kill）（陰線） ／ 25日線乖離+5.10%
- target: ⚠目標未設定 ／ stop: 1995円（未同期・目標コマンド由来） ／ 残存リスク: 9500円
- ✅建値へSL切り上げ可（+1.06R到達・残存リスク9500円→0円で枠解放）
- 業績グレード: 🔥絶好調（8/13）※キャッシュ有効のため再計算なし・変化なし
- 値頃感: ⚪妥当（3.0/7）— PER17.8倍・52週95.6%
- 決算日程: ⚠日程不明
- タイムストップ: 含み益のため対象外

### 9270 バリュエンスHD（信用買建）
- 終値2,132円 ／ コスト2,105円 ／ 含み損益+2,700円（+1.28%）
- ローソク判定: FAIL_INSEN ／ ⚠足が崩れた（premise_kill）（陰線・上髭64%） ／ 25日線乖離+7.34%
- target: ⚠目標未設定 ／ stop: 1980円（未同期・目標コマンド由来） ／ 残存リスク: 12500円
- 業績グレード: 🔥絶好調（10/13）※キャッシュ有効のため再計算なし・変化なし
- 値頃感: 🟢値頃（5.0/7）— PER9.4倍・52週65.5%
- 決算日程: ⚠日程不明
- タイムストップ: 含み益のため対象外

**保有5銘柄、全銘柄が陰線または上髭超過で足の健全性に警告あり。25日線割れは0件。**

## 前夜の結果
PL5口座への正式な反映は週次①-11の採点で行われる。ここは参考情報。

前夜2026-08-21の提案94件 → 約定70・不約定24・判定不能0

約定銘柄（含み損益順・上位10件）:
- 3968: 注文629円 → 約定629円・当日終値653.0円（+3.82%）
- 5757: 注文5360円 → 約定5360円・当日終値5520.0円（+2.99%）
- 9147: 注文5559.0円 → 約定5550.0円・当日終値5713.0円（+2.94%）
- 1975: 注文3835.0円 → 約定3800.0円・当日終値3905.0円（+2.76%）
- 7972: 注文2565.0円 → 約定2560.0円・当日終値2597.0円（+1.45%）
- 9533: 注文1215.0円 → 約定1204.0円・当日終値1220.0円（+1.33%）
- 1861: 注文1287.0円 → 約定1284.0円・当日終値1300.0円（+1.25%）
- 3086: 注文3023.0円 → 約定3023.0円・当日終値3056.0円（+1.09%）
- 9735: 注文6413.0円 → 約定6368.0円・当日終値6435.0円（+1.05%）
- 5989: 注文1550.0円 → 約定1550.0円・当日終値1566.0円（+1.03%）
他60件はgate_history/2026-08-21.jsonを参照

## 模擬テンプレ
```
# base_day 2026-08-24 ／ 提案62件
# 使い方: 参戦する0〜3銘柄の行だけをコピーし、｜の後ろに参戦理由を書いてポジション株PJへ送る。
# 選ばなかった行は送らなくてよい（全行に理由を書く必要はない）。見送りは末尾の1行で足りる。
# 特定銘柄を理由つきで見送る場合のみ『模擬 見送り {code} ｜{理由}』を送る。
模擬 5757 kenmo_momentum 逆指値5540 SL5198.2 単元100 ｜
模擬 5537 kenmo_momentum 逆指値3245 SL3045.6 単元100 ｜
模擬 7409 kenmo_momentum 逆指値1461 SL1372.4 単元100 ｜
模擬 3798 kenmo_momentum 逆指値539 SL505.72 単元100 ｜
模擬 3374 changepoint🔔🔔 逆指値4075 SL3825.8 単元100 ｜
模擬 1960 kenmo_newhigh 逆指値1685 SL1582.96 単元100 ｜
模擬 7972 choruko_reversal 指値2597 SL2482 単元100 ｜
模擬 5444 choruko_reversal 指値12400 SL11545 単元100 ｜
模擬 7649 choruko_reversal 指値2740 SL2655.5 単元100 ｜
模擬 1812 choruko_reversal 指値4831 SL4670 単元100 ｜
模擬 9302 choruko_reversal 指値3339 SL3267 単元100 ｜
模擬 6135 choruko_reversal 指値15630 SL14830 単元100 ｜
模擬 1861 choruko_reversal 指値1300 SL1249 単元100 ｜
模擬 1802 choruko_reversal 指値2998 SL2891 単元100 ｜
模擬 6586 choruko_reversal 指値5303 SL5081 単元100 ｜
模擬 1975 choruko_reversal 指値3905 SL3710 単元100 ｜
模擬 1979 choruko_reversal 指値3955 SL3860 単元100 ｜
模擬 9533 choruko_reversal 指値1220 SL1174.5 単元100 ｜
模擬 5020 granville_tenkan 逆指値1344 SL1262.42 単元100 ｜
模擬 5592 granville_tenkan 逆指値2713 SL2549.28 単元100 ｜
模擬 9037 granville_tenkan 逆指値1870 SL1756.86 単元100 ｜
模擬 2702 granville_tenkan 逆指値8190 SL7689.2 単元100 ｜
模擬 1808 granville_tenkan 逆指値2881 SL2707.2 単元100 ｜
模擬 6305 granville_tenkan 逆指値6060 SL5680.42 単元100 ｜
模擬 9101 granville_tenkan 逆指値7230 SL6785.86 単元100 ｜
模擬 8098 granville_tenkan 逆指値4285 SL4023.2 単元100 ｜
模擬 8056 granville_tenkan 逆指値4670 SL4383.22 単元100 ｜
模擬 1925 granville_tenkan 逆指値4715 SL4425.52 単元100 ｜
模擬 9503 granville_tenkan 逆指値2586 SL2429.9 単元100 ｜
模擬 9041 granville_tenkan 逆指値3580 SL3358.62 単元100 ｜
模擬 3865 granville_tenkan 逆指値913 SL857.28 単元100 ｜
模擬 6770 granville_tenkan 逆指値2214 SL2080.22 単元100 ｜
模擬 3003 granville_tenkan 逆指値1803 SL1693.88 単元100 ｜
模擬 7616 granville_oshime 指値2038.52 SL2028.38 単元100 ｜
模擬 9828 granville_oshime 指値3394.49 SL3377.6 単元100 ｜
模擬 2659 granville_oshime 指値3296.4 SL3280 単元100 ｜
模擬 7278 granville_oshime 指値6081.05 SL6050.8 単元100 ｜
模擬 3151 granville_oshime 指値1644.46 SL1636.28 単元100 ｜
模擬 8242 granville_oshime 指値2868.39 SL2854.12 単元100 ｜
模擬 6613 granville_rebound 指値2330 SL1922 単元100 ｜
模擬 150A granville_rebound 指値752 SL636 単元100 ｜
模擬 9147 granville_rebound 指値5713 SL5374 単元100 ｜
模擬 4420 granville_rebound 指値703 SL678 単元100 ｜
模擬 6656 granville_rebound 指値808 SL764 単元100 ｜
模擬 7505 granville_rebound 指値2127 SL2050 単元100 ｜
模擬 4718 granville_rebound 指値2502 SL2362 単元100 ｜
模擬 4063 granville_rebound 指値6051 SL6024 単元100 ｜
模擬 7460 granville_rebound 指値1710 SL1647 単元100 ｜
模擬 1860 granville_rebound 指値1523.5 SL1462 単元100 ｜
模擬 5998 granville_rebound 指値2611 SL2262 単元100 ｜
模擬 5189 granville_rebound 指値3600 SL3425 単元100 ｜
模擬 5989 granville_rebound 指値1566 SL1486 単元100 ｜
模擬 1878 granville_rebound 指値3338 SL3172 単元100 ｜
模擬 3086 granville_rebound 指値3056 SL2818.5 単元100 ｜
模擬 3776 granville_rebound 指値243 SL237 単元100 ｜
模擬 9735 granville_rebound 指値6435 SL6252 単元100 ｜
模擬 9301 granville_rebound 指値1533 SL1490 単元100 ｜
模擬 479A 変化点🔔 指値1979 SL1652 単元100 🔒 ｜
模擬 584A 変化点🔔 指値2668 SL2635 単元100 🔒 ｜
模擬 3994 変化点🔔 指値6450 SL5640 単元100 🔒 ｜
模擬 598A 変化点🔔 指値1384 SL1282 単元100 🔒 ｜
模擬 4478 変化点🔔🔔 指値3920 SL3270 単元100 🔒 ｜
模擬 見送り ｜
```

## PASS内訳
PASS 70件 = 発注可能 62件 + 除外 8件

除外銘柄:
- 7480 スズデン: ⛔提案なし(手法ブランチ不明)
- 4249 森六: ⛔提案なし(手法ブランチ不明)
- 6136 OSG Corp: ⛔型不一致: 既に支持帯以下
- 7716 Nakanishi Inc.: ⛔型不一致: 既に支持帯以下
- 6284 Nissei ASB Machine Co., Ltd.: ⛔型不一致: 既に支持帯以下
- 6432 Takeuchi Mfg.Co., Ltd.: ⛔型不一致: 既に支持帯以下
- 6638 ミマキエンジニアリング: ⛔型不一致: 既に支持帯以下
- 2810 ハウス食品グループ本社: ⛔型不一致: 既に支持帯以下

## 5手法銘柄
（128銘柄・並び順はSTEP5.2(1)）

- 5254 Arent, Inc.｜granville_oshime/kenmo_momentum｜🚀確変｜⚪妥当｜FAIL_INSEN｜終値4,180円｜💰426,000円｜—｜
- 3441 Sanno Co., Ltd.｜kenmo_momentum｜🚀確変｜🟢値頃｜FAIL_INSEN｜終値2,662円｜💰269,900円｜—｜
- 3556 RenetJapanGroup, Inc.｜kenmo_momentum｜🚀確変｜🟢値頃｜FAIL_UWAHIGE｜終値879円｜💰87,400円｜—｜
- 5724 Asaka Riken Co., Ltd.｜kenmo_momentum｜🚀確変｜🟢値頃｜FAIL_UWAHIGE｜終値3,060円｜💰283,400円｜—｜
- 5136 tripla Co.,Ltd.｜kenmo_momentum｜🚀確変｜⚪妥当｜FAIL_INSEN｜終値1,930円｜💰198,700円｜—｜
- 5243 note inc.｜kenmo_momentum/未マージPR由来｜🚀確変｜⚪妥当｜FAIL_INSEN｜終値2,550円｜💰255,000円｜—｜
- 5586 Laboro.AI, Inc.｜kenmo_momentum｜🚀確変｜⚪妥当｜FAIL_INSEN｜終値894円｜💰89,500円｜—｜
- 3723 Nihon Falcom Corporation｜kenmo_momentum｜🚀確変｜⚪妥当｜FAIL_INSEN｜終値2,899円｜💰287,100円｜—｜
- 5027 AnyMind Group｜changepoint/kenmo_momentum/変化点🔔🔔｜🚀確変｜⚪妥当｜FAIL_INSEN｜終値811円｜💰80,300円｜—｜
- 9341 GENOVA Inc.｜granville_tenkan/kenmo_momentum｜🔥絶好調｜💎割安｜FAIL_UWAHIGE｜終値636円｜💰62,500円｜—｜
- 5757 CK San-Etsu Co., Ltd.｜kenmo_momentum/未マージPR由来｜🔥絶好調｜🟢値頃｜PASS｜終値5,520円｜💰552,000円｜逆指値5540円(上限5595.4円)｜⚠リスク枠超過
  > 📌業態: 黄銅棒・黄銅線で国内首位。精密部品、配管も。日本伸銅を子会社化。
  > いま: 終値5,520円・直近5日+8.66%（材料未確認）
  > 調子: 🔥絶好調（10/13）— E軸判定不能(進捗データ不足)
  > 水準: 🟢値頃（5.0/7）— PER7.0倍・PEG0.09・52週85.2% ／ 💰単元55.2万円
  > 戦略: 当日高値超えの逆指値5540円で順張り参戦を検討。上限5595.4円・SL5198.2円目安／⚠1単元リスク34180円（枠超過）
- 9270 Valuence Holdings, Inc.｜kenmo_momentum/未マージPR由来｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜終値2,132円｜💰213,200円｜—｜
- 212A FIT EASY Inc.｜kenmo_momentum/未マージPR由来｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜終値3,085円｜💰308,500円｜—｜
- 5246 ELEMENTS,Inc.｜kenmo_momentum/未マージPR由来｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜終値838円｜💰85,300円｜—｜
- 9554 AViC Co. Ltd.｜granville_tenkan/kenmo_momentum｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜終値1,761円｜💰180,000円｜—｜
- 421A Movin' Strategic Career CO.,LTD.｜kenmo_momentum｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜終値3,945円｜💰412,500円｜—｜
- 1435 robot home Inc.｜kenmo_momentum｜🔥絶好調｜💎割安｜FAIL_INSEN｜終値178円｜💰18,500円｜—｜
- 9211 f-code Inc.｜granville_tenkan/kenmo_momentum｜🔥絶好調｜💎割安｜FAIL_UWAHIGE｜終値1,532円｜💰150,500円｜—｜
- 6298 Y.A.C.HOLDINGS CO.,LTD.｜kenmo_momentum｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜終値1,321円｜💰133,100円｜—｜
- 4377 ONE CAREER Inc.｜kenmo_momentum｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜終値2,404円｜💰244,300円｜—｜
- 5537 AlbaLink Co.,Ltd.｜kenmo_momentum｜🔥絶好調｜⚪妥当｜PASS｜終値3,220円｜💰322,000円｜逆指値3245円(上限3277.45円)｜
  > 📌業態: 流動性が低下している不動産の買取再販やコンサルティングなどを手掛ける。
  > いま: 終値3,220円・直近5日+9.26%（材料未確認）
  > 調子: 🔥絶好調（9/13）— D軸判定不能(直近Qデータ取得不可)
  > 水準: ⚪妥当（3.0/7）— PER18.5倍・PEG0.42・52週81.3% ／ 💰単元32.2万円
  > 戦略: 当日高値超えの逆指値3245円で順張り参戦を検討。上限3277.45円・SL3045.6円目安
- 6562 Geniee, Inc.｜kenmo_momentum/未マージPR由来｜🔥絶好調｜💎割安｜FAIL_UWAHIGE｜終値877円｜💰86,300円｜—｜
- 262A INTERMESTIC INC.｜kenmo_momentum｜🔥絶好調｜💎割安｜FAIL_UWAHIGE｜終値1,872円｜💰185,000円｜—｜
- 7318 SERENDIP HOLDINGS Co. Ltd.｜kenmo_momentum/変化点🔔🔔｜🔥絶好調｜💎割安｜FAIL_INSEN｜終値1,450円｜💰147,900円｜—｜
- 2334 Eole, Inc.｜kenmo_momentum｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜終値505円｜💰50,800円｜—｜
- 3915 TerraSky Co., Ltd.｜kenmo_momentum｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜終値2,281円｜💰234,700円｜—｜
- 7047 PORT INC.｜granville_oshime/kenmo_momentum/未マージPR由来｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜終値2,414円｜💰234,100円｜—｜
- 3109 Shikibo Ltd.｜kenmo_momentum｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜終値1,089円｜💰108,900円｜—｜
- 5574 ABEJA,Inc.｜changepoint/kenmo_momentum/変化点🔔/変化点🔔🔔｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜終値2,774円｜💰274,600円｜—｜
- 6630 YA-MAN Ltd.｜kenmo_momentum｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜終値823円｜💰83,300円｜—｜
- 135A VRAIN Solution,Inc.｜kenmo_momentum/未マージPR由来｜🔥絶好調｜🟡やや割高｜FAIL_INSEN｜終値4,345円｜💰439,000円｜—｜
- 146A Columbia Works Inc.｜kenmo_momentum｜⚡好調｜💎割安｜FAIL_INSEN｜終値3,735円｜💰377,000円｜—｜
- 5892 yutori,Inc.｜kenmo_momentum/未マージPR由来｜⚡好調｜💎割安｜FAIL_INSEN｜終値2,382円｜💰245,500円｜—｜
- 8927 Meiho Enterprise Co., Ltd.｜kenmo_momentum｜⚡好調｜💎割安｜FAIL_UWAHIGE｜終値479円｜💰47,800円｜—｜
- 5590 ネットスターズ｜changepoint/kenmo_momentum/変化点🔔🔔｜⚡好調｜🟢値頃｜FAIL_INSEN｜終値693円｜💰69,900円｜—｜
- 4058 Toyokumo, Inc.｜kenmo_momentum｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値2,449円｜💰246,300円｜—｜
- 558A SQUEEZE Inc.｜kenmo_momentum｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜終値5,630円｜💰557,000円｜—｜
- 6071 IBJ, Inc.｜kenmo_momentum｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値947円｜💰95,500円｜—｜
- 7409 AeroEdge Co.,Ltd｜kenmo_momentum｜⚡好調｜⚪妥当｜PASS｜終値1,443円｜💰144,300円｜逆指値1461円(上限1475.61円)｜
  > 📌業態: 航空機エンジン部品などの製造・販売やエンジニアリングサービスの提供を手掛ける。
  > いま: 終値1,443円・直近5日-4.44%（材料未確認）
  > 調子: ⚡好調（7/13）— E軸判定不能(進捗データ不足)
  > 水準: ⚪妥当（4.0/7）— PER37.3倍・PEG1.29・52週33.6% ／ 💰単元14.4万円
  > 戦略: 当日高値超えの逆指値1461円で順張り参戦を検討。上限1475.61円・SL1372.4円目安
- 9552 Quants Research Institute Holdings, Inc.｜kenmo_momentum｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値1,105円｜💰110,100円｜—｜
- 4477 BASE, Inc.｜granville_rebound/kenmo_momentum/未マージPR由来｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜終値313円｜💰31,200円｜—｜
- 2980 SRE Holdings Corp.｜kenmo_momentum｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜終値2,453円｜💰240,300円｜—｜
- 4475 HENNGE K.K.｜kenmo_momentum/未マージPR由来｜⚡好調｜🔴過熱｜FAIL_UWAHIGE｜終値1,561円｜💰151,200円｜—｜
- 3798 ULS Group Incorporated｜kenmo_momentum｜✅順調｜💎割安｜PASS｜終値534円｜💰53,400円｜逆指値539円(上限544.39円)｜
  > 📌業態: ITシステムの設計・構築・コンサルを展開。流通・製造・情報サービス業向けが中心。
  > いま: 終値534円・直近5日+1.14%（材料未確認）
  > 調子: ✅順調（4/13）— E軸:進捗26.1%<前年同期29.2%
  > 水準: 💎割安（6.0/7）— PER13.2倍・PEG0.63・52週16.2% ／ 💰単元5.3万円
  > 戦略: 当日高値超えの逆指値539円で順張り参戦を検討。上限544.39円・SL505.72円目安
- 277A Globe-Ing, Inc.｜kenmo_momentum｜✅順調｜🟢値頃｜FAIL_INSEN｜終値1,851円｜💰184,600円｜—｜
- 6785 Suzuki Co., Ltd.｜kenmo_momentum/未マージPR由来｜✅順調｜🟢値頃｜FAIL_INSEN｜終値2,876円｜💰288,800円｜—｜
- 341A TOYOKOH Inc.｜kenmo_momentum｜✅順調｜⚪妥当｜FAIL_INSEN｜終値2,003円｜💰201,000円｜—｜
- 5038 eWeLL Co.,Ltd｜kenmo_momentum｜✅順調｜⚪妥当｜FAIL_INSEN｜終値2,176円｜💰225,600円｜—｜
- 4493 Cyber Security Cloud, Inc.｜kenmo_momentum/未マージPR由来｜✅順調｜🟡やや割高｜FAIL_UWAHIGE｜終値1,952円｜💰187,400円｜—｜
- 276A ククレブ・アドバイザーズ｜granville_oshime/kenmo_momentum｜判定保留｜🟢値頃｜FAIL_INSEN｜終値3,555円｜💰357,500円｜—｜
- 325A TENTIAL, Inc.｜kenmo_momentum/kenmo_newhigh｜判定保留(変則決算)｜⚪妥当｜FAIL_INSEN｜終値1,800円｜💰182,400円｜—｜🎯
- 6492 Okano Valve Mfg. Co., Ltd.｜kenmo_momentum｜判定保留(変則決算)｜⚪妥当｜FAIL_INSEN｜終値13,660円｜💰1,383,000円｜—｜
- 4894 Cuorips Inc.｜kenmo_momentum｜判定保留｜🔴過熱｜FAIL_INSEN｜終値5,250円｜💰519,000円｜—｜
- 4165 PLAID Inc.｜changepoint/kenmo_momentum/変化点🔔🔔｜判定保留(変則決算: 連2025.09→連 予2026.12)｜🔴過熱｜FAIL_INSEN｜終値716円｜💰73,400円｜—｜
- 3932 Akatsuki, Inc.｜kenmo_momentum｜業績?｜🔴過熱｜FAIL_UWAHIGE｜終値3,820円｜💰373,000円｜—｜
- 2594 Key Coffee Inc.｜kenmo_momentum/未マージPR由来｜業績?｜水準?｜FAIL_INSEN｜終値2,037円｜💰—｜—｜
- 4973 Japan Pure Chemical Co., Ltd.｜kenmo_momentum/未マージPR由来｜業績?｜水準?｜FAIL_INSEN｜終値4,665円｜💰—｜—｜
- 8139 Nagahori Corporation｜kenmo_momentum/未マージPR由来｜業績?｜水準?｜FAIL_INSEN｜終値2,344円｜💰—｜—｜
- 8614 Toyo Securities Co., Ltd.｜kenmo_momentum｜業績データ取得不可｜⏸判定不能｜FAIL_UWAHIGE｜終値721円｜💰71,600円｜—｜
- 9467 Alphapolis Co., Ltd.｜kenmo_momentum/未マージPR由来｜業績?｜水準?｜FAIL_INSEN｜終値1,215円｜💰—｜—｜
- 3374 内外テック｜changepoint🔔🔔/kenmo_newhigh/変化点🔔🔔｜🚀確変｜🟢値頃｜PASS｜終値4,065円｜💰406,500円｜逆指値4075円(上限4115.75円)｜
  > 📌業態: 半導体製造装置部品商社。組立や受託製造、保守も。東エレクへ依存度大。
  > いま: 終値4,065円・直近5日-5.90%（材料未確認）
  > 調子: 🚀確変（12/13）
  > 水準: 🟢値頃（5.0/7）— PER8.5倍・PEG0.10・52週77.9% ／ 💰単元40.6万円
  > 戦略: 当日高値超えの逆指値4075円で順張り参戦を検討。上限4115.75円・SL3825.8円目安
- 1960 サンテック｜kenmo_newhigh｜➖横ばい｜🔴過熱｜PASS｜終値1,684円｜💰168,400円｜逆指値1685円(上限1701.85円)｜
  > 📌業態: 独立系の電気工事大手。電力・民間・公共に展開。海外工事でも実績。
  > いま: 終値1,684円・直近5日-5.39%（材料未確認）
  > 調子: ➖横ばい（2/13）— E軸=進捗率データ制約のため直近QoQトレンドで代用
  > 水準: 🔴過熱（1.0/7）— PER11.2倍・PEG—・52週87.4% ／ 💰単元16.8万円
  > 戦略: 当日高値超えの逆指値1685円で順張り参戦を検討。上限1701.85円・SL1582.96円目安
- 4599 StemRIM Inc.｜kenmo_newhigh｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜終値354円｜💰35,700円｜—｜
- 7685 ＢＵＹＳＥＬＬ　ＴＥＣＨＮＯＬＯＧＩＥＳ｜choruko_reversal/granville_rebound｜🚀確変｜🟢値頃｜FAIL_UWAHIGE｜終値3,285円｜💰328,500円｜—｜
- 5938 LIXIL Corporation｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値1,760円｜💰175,600円｜—｜
- 5301 東海カーボン｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値1,651円｜💰168,500円｜—｜⚡材料後出し
- 7730 マニー｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜終値1,618円｜💰160,300円｜—｜
- 3288 Open House Group Co. Ltd｜choruko_reversal｜⚡好調｜💎割安｜FAIL_INSEN｜終値8,071円｜💰813,600円｜—｜
- 4516 日本新薬｜choruko_reversal｜⚡好調｜💎割安｜FAIL_INSEN｜終値3,623円｜💰366,700円｜—｜
- 6544 Japan Elevator Service Holdings Co., Ltd.｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜終値1,562円｜💰155,150円｜—｜
- 7419 Nojima Co.,Ltd.｜choruko_reversal｜⚡好調｜💎割安｜FAIL_UWAHIGE｜終値1,275円｜💰128,000円｜—｜
- 7972 ITOKI Corporation｜choruko_reversal｜⚡好調｜💎割安｜PASS｜終値2,597円｜💰259,700円｜指値2597.0円｜
  > 📌業態: オフィス家具大手。公共、医療施設向けも。製販一貫体制確立で効率経営。
  > いま: 終値2,597円・直近5日-0.88%（材料未確認）
  > 調子: ⚡好調（5/13）— 進捗データ取得不可(判定不能)
  > 水準: 💎割安（6.0/7）— PER11.5倍・PEG0.70・52週26.5% ／ 💰単元26.0万円
  > 戦略: 当日終値2597.0円の指値で反転を取りにいく。SL2482.0円（直近5日安値）
- 5444 Yamato Kogyo Co., Ltd.｜choruko_reversal/未マージPR由来｜⚡好調｜🟢値頃｜PASS_DOJI｜終値12,400円｜💰1,240,000円｜指値12400.0円｜⚠リスク枠超過
  > 📌業態: 独立系電炉大手。主力はH形鋼、溝形鋼。海外多、韓・タイ・米・中東で操業。
  > いま: 終値12,400円・直近5日-5.81%（材料未確認）
  > 調子: ⚡好調（5/13）
  > 水準: 🟢値頃（5.0/7）— PER12.9倍・PEG0.39・52週64.5% ／ 💰単元124.0万円
  > 戦略: 当日終値12400.0円の指値で反転を取りにいく。SL11545.0円（直近5日安値）／⚠1単元リスク85500円（枠超過）
- 7202 Isuzu Motors Limited｜choruko_reversal｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜終値2,238円｜💰222,850円｜—｜
- 3064 MonotaRO Co., Ltd.｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜終値1,840円｜💰181,600円｜—｜
- 6013 Takuma Co., Ltd.｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値3,065円｜💰310,500円｜—｜
- 9072 ニッコンホールディングス｜choruko_reversal｜⚡好調｜🔴過熱｜FAIL_INSEN｜終値5,454円｜💰544,800円｜—｜
- 2579 Coca-Cola Bottlers Japan Holdings Inc.｜choruko_reversal/granville_rebound｜✅順調｜⚪妥当｜FAIL_UWAHIGE｜終値3,866円｜💰386,300円｜—｜🎯
- 7649 Sugi Holdings Co., Ltd.｜choruko_reversal｜✅順調｜⚪妥当｜PASS｜終値2,740円｜💰274,000円｜指値2740.0円｜
  > 📌業態: 中部地盤にドラッグストア「スギ薬局」をチェーン展開。調剤薬局併設店に強み。
  > いま: 終値2,740円・直近5日+0.16%（材料未確認）
  > 調子: ✅順調（4/13）— 進捗データ取得不可(判定不能)
  > 水準: ⚪妥当（4.0/7）— PER15.5倍・PEG1.58・52週6.3% ／ 💰単元27.4万円
  > 戦略: 当日終値2740.0円の指値で反転を取りにいく。SL2655.5円（直近5日安値）
- 7731 ニコン｜choruko_reversal/granville_rebound｜✅順調｜⚪妥当｜FAIL_INSEN｜終値1,980円｜💰200,800円｜—｜
- 4536 参天製薬｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜終値1,874円｜💰187,950円｜—｜
- 1812 Kajima Corporation｜choruko_reversal/未マージPR由来｜⚠減速｜⚪妥当｜PASS｜終値4,831円｜💰483,100円｜指値4831.0円｜⚠業績基調下向き
  > 📌業態: 総合建設大手。超高層ビル・耐震・原発など技術に強み。内外で不動産開発。
  > いま: 終値4,831円・直近5日-3.01%（材料未確認）
  > 調子: ⚠減速（4/13）— 進捗データ取得不可(判定不能)
  > 水準: ⚪妥当（3.0/7）— PER13.0倍・PEG—・52週17.7% ／ 💰単元48.3万円
  > 戦略: 当日終値4831.0円の指値で反転を取りにいく。SL4670.0円（直近5日安値）
- 9065 Sankyu Inc.｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_UWAHIGE｜終値8,363円｜💰833,700円｜—｜
- 9302 三井倉庫ホールディングス｜choruko_reversal｜✅順調｜🟡やや割高｜PASS｜終値3,339円｜💰333,900円｜指値3339.0円｜
  > 📌業態: 倉庫業大手。総合物流業務に強み。国際サプライチェーン展開。不動産賃貸が収益。
  > いま: 終値3,339円・直近5日-0.09%（材料未確認）
  > 調子: ✅順調（4/13）— 質注意
  > 水準: 🟡やや割高（2.0/7）— PER20.0倍・PEG—・52週16.6% ／ 💰単元33.4万円
  > 戦略: 当日終値3339.0円の指値で反転を取りにいく。SL3267.0円（直近5日安値）
- 6135 牧野フライス製作所｜choruko_reversal｜✅順調｜🔴過熱｜PASS｜終値15,630円｜💰1,563,000円｜指値15630.0円｜⚠リスク枠超過
  > 📌業態: 工作機械大手。マシニングセンタ、放電加工機が主力。レーザ加工機にも注力。
  > いま: 終値15,630円・直近5日-4.87%（材料未確認）
  > 調子: ✅順調（4/13）
  > 水準: 🔴過熱（0.0/7）— PER16.5倍・PEG4.10・52週85.8% ／ 💰単元156.3万円
  > 戦略: 当日終値15630.0円の指値で反転を取りにいく。SL14830.0円（直近5日安値）／⚠1単元リスク80000円（枠超過）
- 1861 Kumagai Gumi Co., Ltd.｜choruko_reversal｜✅順調｜💎割安｜PASS｜終値1,300円｜💰130,000円｜指値1300.0円｜
  > 📌業態: 総合建設準大手。大型土木・超高層ビル建築で実績。筆頭株主に住友林業。
  > いま: 終値1,300円・直近5日-0.99%（材料未確認）
  > 調子: ✅順調（3/13）— 進捗データ取得不可(判定不能)
  > 水準: 💎割安（6.0/7）— PER10.8倍・PEG0.74・52週15.4% ／ 💰単元13.0万円
  > 戦略: 当日終値1300.0円の指値で反転を取りにいく。SL1249.0円（直近5日安値）
- 4553 Towa Pharmaceutical Co., Ltd.｜choruko_reversal/granville_oshime｜✅順調｜⚪妥当｜FAIL_INSEN｜終値3,875円｜💰389,500円｜—｜
- 1802 Obayashi Corporation｜choruko_reversal｜✅順調｜⚪妥当｜PASS｜終値2,998円｜💰299,800円｜指値2998.0円｜
  > 📌業態: 総合建設大手。関西地盤で首都圏で都市開発。トンネルに強み。発電関連強化。
  > いま: 終値2,998円・直近5日-1.19%（材料未確認）
  > 調子: ✅順調（3/13）— 進捗データ取得不可(判定不能)
  > 水準: ⚪妥当（3.0/7）— PER13.1倍・PEG—・52週32.6% ／ 💰単元30.0万円
  > 戦略: 当日終値2998.0円の指値で反転を取りにいく。SL2891.0円（直近5日安値）
- 6586 Makita Corporation｜choruko_reversal｜✅順調｜🔴過熱｜PASS｜終値5,303円｜💰530,300円｜指値5303.0円｜
  > 📌業態: 電動工具最大手。世界各国で現地生産・販売。園芸、清掃向けも展開。
  > いま: 終値5,303円・直近5日-0.53%（材料未確認）
  > 調子: ✅順調（3/13）— E軸判定不能(進捗データ不足)
  > 水準: 🔴過熱（1.0/7）— PER16.9倍・PEG6.11・52週57.7% ／ 💰単元53.0万円
  > 戦略: 当日終値5303.0円の指値で反転を取りにいく。SL5081.0円（直近5日安値）
- 456A ＨＵＭＡＮ　ＭＡＤＥ｜choruko_reversal｜✅順調｜🔴過熱｜FAIL_INSEN｜終値1,657円｜💰166,200円｜—｜
- 6632 ＪＶＣケンウッド｜choruko_reversal｜➖横ばい｜⚪妥当｜FAIL_INSEN｜終値1,008円｜💰100,700円｜—｜
- 1975 朝日工業社｜choruko_reversal｜➖横ばい｜🟡やや割高｜PASS｜終値3,905円｜💰390,500円｜指値3905.0円｜
  > 📌業態: 空調・衛生工事の大手。ハイテク環境制御装置に優れる。民間受注が中心。
  > いま: 終値3,905円・直近5日-0.89%（材料未確認）
  > 調子: ➖横ばい（2/13）— E軸判定不能(進捗データ不足)
  > 水準: 🟡やや割高（2.0/7）— PER10.9倍・PEG3.56・52週53.1% ／ 💰単元39.0万円
  > 戦略: 当日終値3905.0円の指値で反転を取りにいく。SL3710.0円（直近5日安値）
- 5105 Toyo Tire Corporation｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_UWAHIGE｜終値3,824円｜💰381,100円｜—｜
- 8111 Goldwin Inc.｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_UWAHIGE｜終値2,172円｜💰213,900円｜—｜
- 1979 Taikisha Ltd.｜choruko_reversal/granville_rebound/未マージPR由来｜⚠減速｜🟡やや割高｜PASS｜終値3,955円｜💰395,500円｜指値3955.0円｜⚠業績基調下向き
  > 📌業態: 空調工事大手。自動車塗装設備工事で国内トップ。海外積極展開。
  > いま: 終値3,955円・直近5日-4.47%（材料未確認）
  > 調子: ⚠減速（1/13）— E軸判定不能(進捗データ不足)
  > 水準: 🟡やや割高（2.0/7）— PER13.8倍・PEG16.34・52週51.7% ／ 💰単元39.5万円
  > 戦略: 当日終値3955.0円の指値で反転を取りにいく。SL3860.0円（直近5日安値）
- 1980 ダイダン｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_UWAHIGE｜終値2,733円｜💰269,800円｜—｜
- 6845 Azbil Corporation｜choruko_reversal/granville_rebound｜⚠減速｜🔴過熱｜FAIL_UWAHIGE｜終値1,508円｜💰149,600円｜—｜🎯
- 9533 東邦瓦斯｜choruko_reversal｜🔻悪化｜🔴過熱｜PASS｜終値1,220円｜💰122,000円｜指値1220.0円｜⚠業績基調下向き
  > 📌業態: 都市ガス大手。愛知、岐阜、三重が拠点。LPGに強み。コージェネ事業に注力。
  > いま: 終値1,220円・直近5日+2.95%（材料未確認）
  > 調子: 🔻悪化（0/13）— E軸判定不能(進捗データ不足)
  > 水準: 🔴過熱（1.0/7）— PER18.9倍・PEG—・52週45.4% ／ 💰単元12.2万円
  > 戦略: 当日終値1220.0円の指値で反転を取りにいく。SL1174.5円（直近5日安値）
- 543A ＡＲＣＨＩＯＮ｜choruko_reversal｜業績データ取得不可｜💎割安｜FAIL_INSEN｜終値273円｜💰28,000円｜—｜
- 7157 Lifenet Insurance Company｜choruko_reversal｜業績データ取得不可(経常益予想非開示)｜⚪妥当｜FAIL_INSEN｜終値1,481円｜💰152,900円｜—｜
- 8366 滋賀銀行｜choruko_reversal｜取得不可｜⚪妥当｜FAIL_INSEN｜終値2,641円｜💰266,600円｜—｜
- 7480 スズデン｜stf_kakuhen｜🚀確変｜⚪妥当｜PASS｜終値3,490円｜💰349,000円｜⛔提案なし(手法ブランチ不明)｜
  > 📌業態: FA機器主力、技術商社。オムロンと特約店契約。電設資材中心。ネット販売に強み。
  > いま: 終値3,490円・直近5日+2.35%（材料未確認）
  > 調子: 🚀確変（13/13）
  > 水準: ⚪妥当（3.0/7）— PER15.9倍・PEG0.19・52週94.4% ／ 💰単元34.9万円
  > 戦略: 発注対象外（⛔提案なし(手法ブランチ不明)）
- 3131 シンデンハイ｜stf_kakuhen｜🚀確変｜🟢値頃｜FAIL_INSEN｜終値5,840円｜💰608,000円｜—｜
- 6134 ＦＵＪＩ｜stf_kakuhen｜🚀確変｜🟢値頃｜FAIL_UWAHIGE｜終値7,286円｜💰725,700円｜—｜
- 9308 乾汽船｜stf_kakuhen｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜終値2,136円｜💰209,700円｜—｜
- 3036 アルコニックス（アルコニクス）｜stf_kakuhen｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜終値3,465円｜💰343,000円｜—｜
- 6324 ハーモニック・ドライブ・システムズ（ハーモニック）｜stf_kakuhen｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜終値5,680円｜💰570,000円｜—｜
- 7433 伯東｜granville_oshime/stf_kakuhen｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜終値5,290円｜💰522,000円｜—｜
- 7637 白銅｜stf_kakuhen｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜終値3,805円｜💰371,500円｜—｜
- 9962 ミスミグループ本社｜stf_kakuhen｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜終値3,626円｜💰361,500円｜—｜
- 6857 アドバンテスト｜stf_kakuhen｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜終値34,500円｜💰3,590,000円｜—｜
- 8084 ＲＹＯＤＥＮ｜stf_kakuhen｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜終値4,745円｜💰480,500円｜—｜
- 4249 森六｜stf_kakuhen｜🔥絶好調｜🟢値頃｜PASS｜終値2,953円｜💰295,300円｜⛔提案なし(手法ブランチ不明)｜
  > 📌業態: 化学製品、樹脂加工品の製造販売。ホンダ車の内・外装向け大。点滴バッグも。
  > いま: 終値2,953円・直近5日-0.10%（材料未確認）
  > 調子: 🔥絶好調（8/13）
  > 水準: 🟢値頃（5.0/7）— PER7.8倍・PEG0.20・52週99.4% ／ 💰単元29.5万円
  > 戦略: 発注対象外（⛔提案なし(手法ブランチ不明)）
- 6490 ＰＩＬＬＡＲ｜stf_kakuhen｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜終値9,830円｜💰976,000円｜—｜
- 3091 ブロンコビリー｜granville_oshime/stf_kakuhen｜⚡好調｜🟡やや割高｜FAIL_UWAHIGE｜終値2,799円｜💰275,200円｜—｜
- 8697 日本取引所グループ｜stf_kakuhen｜⚡好調｜🟡やや割高｜FAIL_UWAHIGE｜終値2,238円｜💰223,800円｜—｜
- 147A ソラコム｜stf_kakuhen｜⚡好調｜🔴過熱｜FAIL_INSEN｜終値1,036円｜💰104,900円｜—｜
- 8388 阿波銀行｜stf_kakuhen｜⚡好調｜🟡やや割高｜FAIL_INSEN｜終値8,930円｜💰900,000円｜—｜
- 7267 ホンダ｜stf_kakuhen｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値1,747円｜💰175,300円｜—｜
- 3289 Tokyu Fudosan Holdings Corp.｜granville_tenkan/未マージPR由来｜➖横ばい｜⚪妥当｜FAIL_INSEN｜終値1,352円｜💰134,750円｜—｜
- 2733 Arata Corporation｜granville_tenkan/未マージPR由来｜🔻悪化｜⚪妥当｜FAIL_INSEN｜終値2,690円｜💰268,300円｜—｜
- 9861 Yoshinoya Holdings Co., Ltd.｜granville_oshime/未マージPR由来｜✅順調｜🔴過熱｜FAIL_INSEN｜終値3,843円｜💰386,000円｜—｜
- 9616 Kyoritsu Maintenance Co., Ltd.｜granville_oshime/未マージPR由来｜➖横ばい｜🔴過熱｜FAIL_INSEN｜終値3,418円｜💰348,200円｜—｜
- 7581 Saizeriya Co., Ltd.｜granville_rebound/未マージPR由来｜⚡好調｜🟡やや割高｜FAIL_INSEN｜終値7,250円｜💰735,000円｜—｜
- 4718 Waseda Academy Co., Ltd.｜granville_rebound/未マージPR由来｜✅順調｜⚪妥当｜PASS｜終値2,502円｜💰250,200円｜指値2502.0円｜
  > 📌業態: 難関中高の進学塾「早稲田アカデミー」を運営。個別指導、社会人研修も展開。
  > いま: 終値2,502円・直近5日+3.65%（材料未確認）
  > 調子: ✅順調（4/13）— 進捗データ取得不可(判定不能)
  > 水準: ⚪妥当（3.0/7）— PER16.3倍・PEG2.11・52週56.2% ／ 💰単元25.0万円
  > 戦略: 当日終値2502.0円の指値で反転を取りにいく。SL2362.0円（直近5日安値）
- 9044 NANKAI Co., Ltd.｜granville_rebound/未マージPR由来｜✅順調｜🟡やや割高｜FAIL_INSEN｜終値3,033円｜💰304,300円｜—｜
- 3191 Joyful Honda Co. Ltd.｜granville_rebound/未マージPR由来｜✅順調｜🔴過熱｜FAIL_INSEN｜終値2,298円｜💰230,800円｜—｜
- 1878 Daito Trust Construction Co., Ltd.｜granville_rebound/未マージPR由来｜⚠減速｜🟡やや割高｜PASS｜終値3,338円｜💰333,800円｜指値3338.0円｜⚠業績基調下向き
  > 📌業態: 地主に建物賃貸事業を提案。建設・賃貸仲介・管理・家賃保証など一貫。
  > いま: 終値3,338円・直近5日+3.31%（材料未確認）
  > 調子: ⚠減速（1/13）— 進捗判定不能(自動抽出範囲外)
  > 水準: 🟡やや割高（2.0/7）— PER10.1倍・PEG16.88・52週49.2% ／ 💰単元33.4万円
  > 戦略: 当日終値3338.0円の指値で反転を取りにいく。SL3172.0円（直近5日安値）

## グランビル銘柄
（193銘柄・並び順はSTEP5.2(1)）

- 269A Sapeet, Inc.｜granville_tenkan｜🚀確変｜⚪妥当｜FAIL_INSEN｜終値2,625円｜💰268,500円｜—｜
- 145A L is B Corp.｜granville_tenkan｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜終値895円｜💰88,900円｜—｜
- 4521 Kaken Pharmaceutical Co., Ltd.｜granville_tenkan｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜終値3,980円｜💰398,500円｜—｜
- 3491 GA technologies Co., Ltd.｜granville_tenkan｜🔥絶好調｜💎割安｜FAIL_UWAHIGE｜終値1,575円｜💰158,800円｜—｜
- 3623 Billing System Corporation｜granville_tenkan｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜終値1,198円｜💰122,200円｜—｜
- 3968 セグエグループ｜granville_tenkan｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜終値653円｜💰62,600円｜—｜
- 6222 Shima Seiki Mfg. Ltd.｜granville_tenkan｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜終値976円｜💰97,300円｜—｜
- 8086 ニプロ｜granville_tenkan｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜終値1,590円｜💰158,600円｜—｜
- 5020 ENEOS Holdings, Inc.｜granville_tenkan｜⚡好調｜🟢値頃｜PASS｜終値1,340円｜💰134,050円｜逆指値1344円(上限1357.44円)｜
  > 📌業態: 石油元売り最大手。東燃ゼネラルと統合。機能材や石油・天然ガス開発にも強み。
  > いま: 終値1,340円・直近5日+3.55%（材料未確認）
  > 調子: ⚡好調（7/13）— E軸判定不能(当期進捗率取得不可(未算出))
  > 水準: 🟢値頃（5.0/7）— PER8.6倍・PEG0.27・52週70.1% ／ 💰単元13.4万円
  > 戦略: 当日高値超えの逆指値1344円で順張り参戦を検討。上限1357.44円・SL1262.42円目安
- 8793 NEC Capital Solutions Limited｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜終値4,225円｜💰421,000円｜—｜
- 5932 Sankyo Tateyama, Inc.｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値672円｜💰67,700円｜—｜
- 7744 ノーリツ鋼機｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値2,005円｜💰200,000円｜—｜
- 4507 Shionogi & Co., Ltd.｜granville_tenkan/未マージPR由来｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜終値2,922円｜💰291,900円｜—｜
- 5592 Kusurinomadoguchi, Inc.｜granville_tenkan｜⚡好調｜💎割安｜PASS｜終値2,691円｜💰269,100円｜逆指値2713円(上限2740.13円)｜
  > 📌業態: 薬局検索・予約メディア事業から薬局・医療・介護向けソリューションを提供。
  > いま: 終値2,691円・直近5日-0.70%（材料未確認）
  > 調子: ⚡好調（6/13）
  > 水準: 💎割安（6.0/7）— PER9.8倍・PEG0.60・52週23.9% ／ 💰単元26.9万円
  > 戦略: 当日高値超えの逆指値2713円で順張り参戦を検討。上限2740.13円・SL2549.28円目安
- 8057 内田洋行｜granville_tenkan｜⚡好調｜💎割安｜FAIL_UWAHIGE｜終値2,218円｜💰220,000円｜—｜
- 2975 Star Mica Holdings Co., Ltd.｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_INSEN｜終値1,572円｜💰158,600円｜—｜
- 6023 ダイハツインフィニアース｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_INSEN｜終値2,984円｜💰301,000円｜—｜
- 6718 アイホン｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_INSEN｜終値2,863円｜💰286,400円｜—｜
- 3048 BIC Cameras Inc.｜granville_oshime/granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値1,797円｜💰179,000円｜—｜
- 4848 フルキャストホールディングス｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値1,881円｜💰188,400円｜—｜
- 8919 カチタス｜granville_tenkan｜⚡好調｜🔴過熱｜FAIL_INSEN｜終値3,680円｜💰380,500円｜—｜
- 547A ムニノバホールディングス（ムニノバＨＤ）｜granville_tenkan/未マージPR由来｜⚡好調｜💎割安｜FAIL_INSEN｜終値454円｜💰45,200円｜—｜
- 2585 LIFEDRINK COMPANY INC.｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値1,596円｜💰160,200円｜—｜
- 6571 QB Net Holdings Co., Ltd.｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値1,305円｜💰130,900円｜—｜
- 9037 ハマキョウレックス（ハマキョウ）｜granville_tenkan/未マージPR由来｜⚡好調｜🟡やや割高｜PASS｜終値1,867円｜💰186,700円｜逆指値1870円(上限1888.7円)｜
  > 📌業態: 3PL事業大手。物流業務の一括受託で急成長。通販拡大で個人向けも。
  > いま: 終値1,867円・直近5日-0.32%（材料未確認）
  > 調子: ⚡好調（5/13）— E軸判定不能(進捗データ不足)
  > 水準: 🟡やや割高（2.0/7）— PER12.8倍・PEG1.84・52週79.5% ／ 💰単元18.7万円
  > 戦略: 当日高値超えの逆指値1870円で順張り参戦を検討。上限1888.7円・SL1756.86円目安
- 5885 GDEP ADVANCE,Inc.｜granville_tenkan｜⚡好調｜🔴過熱｜FAIL_INSEN｜終値3,015円｜💰317,000円｜—｜
- 2702 日本マクドナルド HD｜granville_tenkan｜⚠減速｜🔴過熱｜PASS｜終値8,170円｜💰817,000円｜逆指値8190円(上限8271.9円)｜⚠業績基調下向き ⚠リスク枠超過
  > 📌業態: 世界的ハンバーガーチェーンで外食国内首位級。大都市圏中心に直営店を展開。
  > いま: 終値8,170円・直近5日+5.83%（材料未確認）
  > 調子: ⚠減速（5/13）— C軸: A成長率0以下のため比率不定(B成長率の符号で代替判定)
  > 水準: 🔴過熱（0.0/7）— PER31.0倍・PEG4.68・52週78.2% ／ 💰単元81.7万円
  > 戦略: 当日高値超えの逆指値8190円で順張り参戦を検討。上限8271.9円・SL7689.2円目安／⚠1単元リスク50080円（枠超過）
- 4847 インテリジェント　ウェイブ｜granville_tenkan｜⚡好調｜🔴過熱｜FAIL_INSEN｜終値1,315円｜💰131,900円｜—｜
- 208A 構造計画研究所ホールディングス｜granville_tenkan｜✅順調｜💎割安｜FAIL_INSEN｜終値3,015円｜💰301,500円｜—｜
- 5036 Japan Business Systems, Inc.｜granville_tenkan｜✅順調｜🟢値頃｜FAIL_INSEN｜終値1,636円｜💰164,100円｜—｜
- 1808 Haseko Corporation｜granville_tenkan｜✅順調｜⚪妥当｜PASS｜終値2,880円｜💰288,000円｜逆指値2881円(上限2909.81円)｜
  > 📌業態: マンション建築最大手。計画から施工まで一貫。独自ノウハウ持つ。サービス関連育成。
  > いま: 終値2,880円・直近5日+2.64%（材料未確認）
  > 調子: ✅順調（4/13）— 進捗判定不能(自動抽出範囲外)
  > 水準: ⚪妥当（4.0/7）— PER11.6倍・PEG0.99・52週42.8% ／ 💰単元28.8万円
  > 戦略: 当日高値超えの逆指値2881円で順張り参戦を検討。上限2909.81円・SL2707.2円目安
- 6305 Hitachi Construction Machinery Co., Ltd.｜granville_tenkan｜✅順調｜⚪妥当｜PASS｜終値6,005円｜💰600,500円｜逆指値6060円(上限6120.6円)｜⚠リスク枠超過
  > 📌業態: 総合建機大手。油圧ショベル世界シェア高、ICT化に強み。鉱山機械も拡大。
  > いま: 終値6,005円・直近5日+11.41%（材料未確認）
  > 調子: ✅順調（4/13）— E軸判定不能(当期進捗率取得不可(未算出))
  > 水準: ⚪妥当（4.0/7）— PER15.2倍・PEG1.01・52週58.1% ／ 💰単元60.0万円
  > 戦略: 当日高値超えの逆指値6060円で順張り参戦を検討。上限6120.6円・SL5680.42円目安／⚠1単元リスク37958円（枠超過）
- 9101 日本郵船｜granville_tenkan｜✅順調｜⚪妥当｜PASS｜終値7,200円｜💰720,000円｜逆指値7230円(上限7302.3円)｜⚠リスク枠超過
  > 📌業態: 総合海運大手。海運売上高で国内トップ。海・陸・空の物流サービスを連携。
  > いま: 終値7,200円・直近5日+10.94%（材料未確認）
  > 調子: ✅順調（4/13）
  > 水準: ⚪妥当（4.0/7）— PER12.1倍・PEG0.66・52週99.2% ／ 💰単元72.0万円
  > 戦略: 当日高値超えの逆指値7230円で順張り参戦を検討。上限7302.3円・SL6785.86円目安／⚠1単元リスク44414円（枠超過）
- 7611 ハイデイ日高｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_INSEN｜終値2,986円｜💰299,100円｜—｜
- 9627 アインホールディングス｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_INSEN｜終値6,152円｜💰614,000円｜—｜
- 8098 稲畑産業｜granville_tenkan｜✅順調｜🔴過熱｜PASS｜終値4,270円｜💰427,000円｜逆指値4285円(上限4327.85円)｜
  > 📌業態: 化学専門商社大手。電子材料や合成樹脂に強み。アジアで広域に展開。
  > いま: 終値4,270円・直近5日+2.40%（材料未確認）
  > 調子: ✅順調（4/13）— 質注意
  > 水準: 🔴過熱（1.0/7）— PER10.9倍・PEG—・52週88.3% ／ 💰単元42.7万円
  > 戦略: 当日高値超えの逆指値4285円で順張り参戦を検討。上限4327.85円・SL4023.2円目安
- 160A As Partners CO.,LTD.｜granville_tenkan｜✅順調｜💎割安｜FAIL_INSEN｜終値2,023円｜💰202,200円｜—｜
- 8056 ＢＩＰＲＯＧＹ｜granville_tenkan｜✅順調｜🟢値頃｜PASS｜終値4,660円｜💰466,000円｜逆指値4670円(上限4716.7円)｜
  > 📌業態: 大日本印刷系の情報システム大手。クラウド事業に注力。金融、流通、空運に強み。
  > いま: 終値4,660円・直近5日+4.44%（材料未確認）
  > 調子: ✅順調（3/13）— E軸判定不能(進捗データ不足)
  > 水準: 🟢値頃（5.0/7）— PER14.0倍・PEG1.48・52週25.6% ／ 💰単元46.6万円
  > 戦略: 当日高値超えの逆指値4670円で順張り参戦を検討。上限4716.7円・SL4383.22円目安
- 1716 Daiichi Cutter Kogyo K.K.｜granville_tenkan｜✅順調｜⚪妥当｜FAIL_INSEN｜終値1,435円｜💰143,500円｜—｜
- 1898 世紀東急工業｜granville_tenkan｜✅順調｜⚪妥当｜FAIL_INSEN｜終値1,500円｜💰150,000円｜—｜
- 1925 大和ハウス工業（大和ハウス）｜granville_tenkan/未マージPR由来｜🔻悪化｜⚪妥当｜PASS｜終値4,700円｜💰470,000円｜逆指値4715円(上限4762.15円)｜⚠業績基調下向き
  > 📌業態: 住宅大手。戸建て、マンション、都市開発など。賃貸住宅・商業・物流施設を展開。
  > いま: 終値4,700円・直近5日+2.82%（材料未確認）
  > 調子: 🔻悪化（3/13）— E軸判定不能(進捗データ不足)
  > 水準: ⚪妥当（3.0/7）— PER10.9倍・PEG—・52週35.9% ／ 💰単元47.0万円
  > 戦略: 当日高値超えの逆指値4715円で順張り参戦を検討。上限4762.15円・SL4425.52円目安
- 4826 ＣＩＪ｜granville_tenkan｜✅順調｜🔴過熱｜FAIL_INSEN｜終値545円｜💰54,800円｜—｜
- 8570 イオンフィナンシャルサービス｜granville_tenkan｜🔻悪化｜🔴過熱｜FAIL_INSEN｜終値1,710円｜💰171,450円｜—｜
- 1605 Inpex Corporation｜granville_tenkan｜➖横ばい｜⚪妥当｜FAIL_INSEN｜終値3,889円｜💰395,400円｜—｜
- 7679 Yakuodo Holdings Co., Ltd.｜granville_tenkan｜➖横ばい｜⚪妥当｜FAIL_INSEN｜終値1,708円｜💰174,200円｜—｜
- 9503 Kansai Electric Power Company, Incorporated｜granville_tenkan｜🔻悪化｜⚪妥当｜PASS｜終値2,582円｜💰258,200円｜逆指値2586円(上限2611.86円)｜⚠業績基調下向き
  > 📌業態: 東電と並ぶ業界の雄。原発依存度高いが代替電源確保へ。情報通信も。
  > いま: 終値2,582円・直近5日+7.88%（材料未確認）
  > 調子: 🔻悪化（2/13）— E軸=進捗率データ制約のため直近QoQトレンドで代用
  > 水準: ⚪妥当（3.0/7）— PER9.3倍・PEG—・52週70.2% ／ 💰単元25.8万円
  > 戦略: 当日高値超えの逆指値2586円で順張り参戦を検討。上限2611.86円・SL2429.9円目安
- 2282 NH Foods Limited｜granville_tenkan｜➖横ばい｜🟡やや割高｜FAIL_INSEN｜終値6,391円｜💰642,300円｜—｜
- 2292 S Foods Inc.｜granville_tenkan｜➖横ばい｜🟡やや割高｜FAIL_UWAHIGE｜終値2,900円｜💰288,800円｜—｜
- 7231 トピー工業｜granville_tenkan｜➖横ばい｜🟡やや割高｜FAIL_INSEN｜終値3,095円｜💰309,500円｜—｜
- 9869 加藤産業｜granville_tenkan｜➖横ばい｜🟡やや割高｜FAIL_INSEN｜終値6,590円｜💰661,000円｜—｜
- 5302 日本カーボン｜granville_tenkan｜➖横ばい｜🔴過熱｜FAIL_INSEN｜終値4,855円｜💰488,000円｜—｜
- 9041 近鉄グループホールディングス｜granville_tenkan｜➖横ばい｜🔴過熱｜PASS｜終値3,562円｜💰356,200円｜逆指値3580円(上限3615.8円)｜
  > 📌業態: 私鉄で営業キロ数最長。グループ力は業界最大級。百貨店、不動産やホテルも。
  > いま: 終値3,562円・直近5日+0.85%（材料未確認）
  > 調子: ➖横ばい（2/13）— E軸判定不能(進捗データ不足)
  > 水準: 🔴過熱（1.0/7）— PER14.4倍・PEG—・52週82.7% ／ 💰単元35.6万円
  > 戦略: 当日高値超えの逆指値3580円で順張り参戦を検討。上限3615.8円・SL3358.62円目安
- 3076 Ai Holdings Corporation｜granville_oshime/granville_tenkan/未マージPR由来｜➖横ばい｜🔴過熱｜FAIL_INSEN｜終値2,935円｜💰293,300円｜—｜
- 2982 ＡＤワークスグループ（ＡＤＷＧ）｜granville_tenkan/未マージPR由来｜⚠減速｜💎割安｜FAIL_INSEN｜終値418円｜💰42,100円｜—｜
- 2317 システナ｜granville_tenkan｜⚠減速｜⚪妥当｜FAIL_UWAHIGE｜終値447円｜💰44,000円｜—｜
- 3880 大王製紙｜granville_tenkan｜🔻悪化｜⚪妥当｜FAIL_INSEN｜終値986円｜💰98,300円｜—｜
- 5406 神戸製鋼所（神戸鋼）｜granville_tenkan/未マージPR由来｜⚠減速｜⚪妥当｜FAIL_INSEN｜終値2,024円｜💰202,450円｜—｜
- 3865 北越コーポレーション（北越コーポ）｜granville_tenkan/未マージPR由来｜🔻悪化｜🟡やや割高｜PASS｜終値910円｜💰91,000円｜逆指値913円(上限922.13円)｜⚠業績基調下向き
  > 📌業態: 総合製紙中堅。上質紙・白板紙が2本柱。新潟工場は高効率。持分に大王紙。
  > いま: 終値910円・直近5日+4.24%（材料未確認）
  > 調子: 🔻悪化（1/13）— E軸判定不能(進捗データ不足)
  > 水準: 🟡やや割高（2.0/7）— PER28.9倍・PEG—・52週38.1% ／ 💰単元9.1万円
  > 戦略: 当日高値超えの逆指値913円で順張り参戦を検討。上限922.13円・SL857.28円目安
- 6770 Alps Alpine Co., Ltd.｜granville_tenkan/未マージPR由来｜⚠減速｜🟡やや割高｜PASS｜終値2,206円｜💰220,650円｜逆指値2214円(上限2236.14円)｜⚠業績基調下向き
  > 📌業態: 電子部品大手。車載・家電向けなど高シェア。金型の精密加工技術に強み。
  > いま: 終値2,206円・直近5日+0.07%（材料未確認）
  > 調子: ⚠減速（1/13）— 進捗データ取得不可(判定不能)
  > 水準: 🟡やや割高（2.0/7）— PER14.4倍・PEG—・52週72.5% ／ 💰単元22.1万円
  > 戦略: 当日高値超えの逆指値2214円で順張り参戦を検討。上限2236.14円・SL2080.22円目安
- 7943 Nichiha Corporation｜granville_tenkan｜⚠減速｜🟡やや割高｜FAIL_INSEN｜終値3,120円｜💰309,000円｜—｜
- 8276 平和堂｜granville_tenkan/未マージPR由来｜⚠減速｜🟡やや割高｜FAIL_UWAHIGE｜終値2,749円｜💰275,200円｜—｜
- 2768 Sojitz Corp.｜granville_tenkan｜業績データ取得不可(経常益予想非開示)｜⚪妥当｜FAIL_UWAHIGE｜終値5,670円｜💰562,400円｜—｜
- 3003 ヒューリック｜granville_tenkan｜業績データ取得不可｜⚪妥当｜PASS｜終値1,798円｜💰179,750円｜逆指値1803円(上限1821.03円)｜
  > 📌業態: 不動産投資会社。都区内に好物件所有、物件多角化へ。私募ファンドも運用。
  > いま: 終値1,798円・直近5日+3.30%（材料未確認）
  > 調子: 業績データ取得不可
  > 水準: ⚪妥当（3.5/7）— PER11.3倍・PEG—・52週47.8% ／ 💰単元18.0万円
  > 戦略: 当日高値超えの逆指値1803円で順張り参戦を検討。上限1821.03円・SL1693.88円目安
- 3993 PKSHA Technology, Inc.｜granville_tenkan｜業績データ取得不可｜⚪妥当｜FAIL_INSEN｜終値3,160円｜💰330,500円｜—｜
- 8425 Mizuho Leasing Company, Limited｜granville_tenkan｜業績データ取得不可｜⚪妥当｜FAIL_INSEN｜終値1,371円｜💰137,500円｜—｜
- 7287 Nippon Seiki Co., Ltd.｜granville_tenkan｜業績データ取得不可(経常益予想非開示)｜🔴過熱｜FAIL_INSEN｜終値2,592円｜💰259,900円｜—｜
- 3116 Toyota Boshoku Corp.｜granville_tenkan/未マージPR由来｜業績?｜水準?｜FAIL_INSEN｜終値2,261円｜💰—｜—｜
- 3222 United Super Markets Holdings, Inc.｜granville_tenkan/未マージPR由来｜業績?｜水準?｜FAIL_INSEN｜終値833円｜💰—｜—｜
- 3765 ガンホー・オンライン・エンターテイメント｜granville_tenkan｜取得不可｜⏸判定不能｜FAIL_INSEN｜終値2,433円｜💰245,500円｜—｜
- 4765 ＳＢＩグローバルアセットマネジメント｜granville_tenkan｜判定保留｜⏸判定不能｜FAIL_INSEN｜終値620円｜💰62,500円｜—｜
- 6425 Universal Entertainment Corporation｜granville_tenkan/未マージPR由来｜業績?｜水準?｜FAIL_UWAHIGE｜終値738円｜💰—｜—｜
- 7911 TOPPAN Holdings Inc.｜granville_tenkan/未マージPR由来｜業績?｜水準?｜FAIL_INSEN｜終値5,002円｜💰—｜—｜
- 9404 Nippon Television Holdings, Inc.｜granville_tenkan/未マージPR由来｜業績?｜水準?｜FAIL_UWAHIGE｜終値2,991円｜💰—｜—｜
- 7806 Ｇ−ＭＴＧ｜granville_oshime｜🚀確変｜⚪妥当｜FAIL_INSEN｜終値8,510円｜💰868,000円｜—｜
- 4419 Ｆｉｎａｔｅｘｔホールディングス｜granville_oshime/granville_rebound/変化点🔔｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜終値1,381円｜💰138,000円｜—｜
- 6136 OSG Corp｜granville_oshime/未マージPR由来｜🔥絶好調｜⚪妥当｜PASS｜終値3,707円｜💰370,700円｜⛔型不一致: 既に支持帯以下｜
  > 📌業態: タップ・エンドミルなど高シェアの精密切削工具大手。製販一貫体制。海外に注力。
  > いま: 終値3,707円・直近5日-6.27%（材料未確認）
  > 調子: 🔥絶好調（10/13）
  > 水準: ⚪妥当（3.0/7）— PER14.5倍・PEG0.34・52週76.8% ／ 💰単元37.1万円
  > 戦略: 発注対象外（⛔型不一致: 既に支持帯以下）
- 3498 霞ヶ関キャピタル｜granville_oshime｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜終値7,840円｜💰786,000円｜—｜
- 6103 Okuma Corporation｜granville_oshime/未マージPR由来｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜終値4,900円｜💰493,500円｜—｜
- 8008 Yondoshi Holdings, Inc.｜granville_oshime/未マージPR由来｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜終値2,191円｜💰219,100円｜—｜
- 4413 ボードルア｜granville_oshime/granville_rebound｜🔥絶好調｜🟡やや割高｜FAIL_INSEN｜終値2,980円｜💰298,000円｜—｜
- 7089 For Startups, Inc.｜granville_oshime｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜終値1,514円｜💰150,600円｜—｜
- 2590 DyDo Group Holdings, Inc.｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜終値3,060円｜💰302,500円｜—｜
- 166A タスキホールディングス｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜終値1,205円｜💰114,900円｜—｜
- 2874 横浜冷凍｜granville_oshime/granville_rebound｜⚠減速｜⚪妥当｜FAIL_UWAHIGE｜終値2,129円｜💰210,200円｜—｜
- 8522 名古屋銀行（名古屋銀）｜granville_oshime/未マージPR由来｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値6,820円｜💰698,000円｜—｜
- 2674 Hard Off Corporation Co., Ltd.｜granville_oshime/granville_rebound/未マージPR由来｜⚡好調｜🟢値頃｜FAIL_INSEN｜終値2,689円｜💰272,500円｜—｜
- 2602 日清オイリオグループ｜granville_oshime｜⚡好調｜🟡やや割高｜FAIL_INSEN｜終値2,053円｜💰206,700円｜—｜
- 7716 Nakanishi Inc.｜granville_oshime/未マージPR由来｜⚡好調｜🟡やや割高｜PASS｜終値3,110円｜💰311,000円｜⛔型不一致: 既に支持帯以下｜
  > 📌業態: 高速回転機器メーカー。歯科用で世界トップクラス。産業用も。海外比率高い。
  > いま: 終値3,110円・直近5日-3.27%（材料未確認）
  > 調子: ⚡好調（6/13）
  > 水準: 🟡やや割高（2.0/7）— PER18.8倍・PEG1.49・52週81.3% ／ 💰単元31.1万円
  > 戦略: 発注対象外（⛔型不一致: 既に支持帯以下）
- 7616 コロワイド｜granville_oshime｜⚡好調｜🔴過熱｜PASS｜終値2,098円｜💰209,750円｜指値2038.52円｜
  > 📌業態: 外食大手。居酒屋中心に直営展開。傘下にレインズ、アトム、カッパクリエ、大戸屋など。
  > いま: 終値2,098円・直近5日+4.61%（材料未確認）
  > 調子: ⚡好調（6/13）— 経常予想非開示のため最終利益成長率で代替(+19.6%)
  > 水準: 🔴過熱（0.0/7）— PER105.4倍・PEG5.38・52週86.9% ／ 💰単元21.0万円
  > 戦略: 2038.52円までの押し目を指値で待つ。SL2028.38円（25日線基準）
- 2780 Komehyo Holdings Co., Ltd.｜granville_oshime｜⚡好調｜🟢値頃｜FAIL_INSEN｜終値5,100円｜💰514,000円｜—｜
- 6284 Nissei ASB Machine Co., Ltd.｜changepoint/granville_oshime/変化点🔔｜⚡好調｜🟢値頃｜PASS_DOJI｜終値8,790円｜💰879,000円｜⛔型不一致: 既に支持帯以下｜
  > 📌業態: PETボトルなど非飲料容器成形機の世界大手。海外比率が9割。汎用機拡大。
  > いま: 終値8,790円・直近5日-6.09%（材料未確認）
  > 調子: ⚡好調（5/13）
  > 水準: 🟢値頃（5.0/7）— PER14.5倍・PEG0.72・52週65.4% ／ 💰単元87.9万円
  > 戦略: 発注対象外（⛔型不一致: 既に支持帯以下）
- 7888 三光合成｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値909円｜💰91,500円｜—｜
- 7970 信越ポリマー｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値2,240円｜💰224,400円｜—｜
- 8923 Tosei Corporation｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値1,818円｜💰182,900円｜—｜
- 7085 カーブスホールディングス｜granville_oshime｜⚡好調｜🟡やや割高｜FAIL_INSEN｜終値976円｜💰97,000円｜—｜
- 9517 イーレックス｜granville_oshime｜⚡好調｜🟡やや割高｜FAIL_INSEN｜終値890円｜💰89,200円｜—｜
- 3479 TKP Corporation｜granville_oshime/未マージPR由来｜⚡好調｜🔴過熱｜FAIL_INSEN｜終値1,871円｜💰188,900円｜—｜
- 6454 Max Co., Ltd.｜granville_oshime/未マージPR由来｜⚡好調｜🔴過熱｜FAIL_UWAHIGE｜終値1,782円｜💰177,700円｜—｜
- 9828 ＧＥＮＫＩ　ＧＬＯＢＡＬ　ＤＩＮＩＮＧ　ＣＯＮＣＥＰＴＳ｜granville_oshime｜⚡好調｜🔴過熱｜PASS｜終値3,535円｜💰353,500円｜指値3394.49円｜
  > 📌業態: 未取得（次回以降に取得）
  > いま: 終値3,535円・直近5日+7.28%（材料未確認）
  > 調子: ⚡好調（5/13）— E軸判定不能(進捗データ不足)
  > 水準: 🔴過熱（1.0/7）— PER18.9倍・PEG1.51・52週86.9% ／ 💰単元35.4万円
  > 戦略: 3394.49円までの押し目を指値で待つ。SL3377.6円（25日線基準）
- 2288 Marudai Food Co., Ltd.｜granville_oshime｜✅順調｜🟢値頃｜FAIL_UWAHIGE｜終値2,255円｜💰224,800円｜—｜
- 5384 Fujimi Incorporated｜granville_oshime｜✅順調｜🔴過熱｜FAIL_INSEN｜終値3,610円｜💰365,000円｜—｜
- 6925 ウシオ電機｜granville_oshime｜✅順調｜🔴過熱｜FAIL_INSEN｜終値3,872円｜💰382,400円｜—｜
- 9031 Nishi-Nippon Railroad Co., Ltd.｜granville_oshime｜🔻悪化｜🔴過熱｜FAIL_INSEN｜終値3,106円｜💰314,300円｜—｜
- 7867 Tomy Company, Ltd.｜granville_oshime｜✅順調｜🔴過熱｜FAIL_UWAHIGE｜終値3,645円｜💰364,100円｜—｜
- 8876 リログループ｜granville_oshime｜✅順調｜🟡やや割高｜FAIL_UWAHIGE｜終値2,179円｜💰216,200円｜—｜
- 5232 Sumitomo Osaka Cement Co., Ltd.｜granville_oshime/未マージPR由来｜✅順調｜🔴過熱｜FAIL_UWAHIGE｜終値5,636円｜💰553,100円｜—｜
- 6055 Japan Material Co., Ltd.｜granville_oshime｜✅順調｜🔴過熱｜FAIL_INSEN｜終値2,059円｜💰206,700円｜—｜
- 6237 Iwaki Co. Ltd.｜granville_oshime/granville_rebound/未マージPR由来｜✅順調｜🔴過熱｜FAIL_INSEN｜終値4,185円｜💰440,000円｜—｜
- 6432 Takeuchi Mfg.Co., Ltd.｜granville_oshime｜✅順調｜🔴過熱｜PASS｜終値7,530円｜💰753,000円｜⛔型不一致: 既に支持帯以下｜
  > 📌業態: 建機中堅。ミニショベルなど小型が主力。クローラーローダーを開発。欧米で高シェア。
  > いま: 終値7,530円・直近5日-0.79%（材料未確認）
  > 調子: ✅順調（3/13）— 進捗判定不能(自動抽出範囲外)
  > 水準: 🔴過熱（1.0/7）— PER13.4倍・PEG—・52週85.8% ／ 💰単元75.3万円
  > 戦略: 発注対象外（⛔型不一致: 既に支持帯以下）
- 9274 ＫＰＰグループホールディングス｜granville_oshime｜✅順調｜🔴過熱｜FAIL_INSEN｜終値1,122円｜💰112,200円｜—｜
- 9882 Yellow Hat Ltd.｜granville_oshime/未マージPR由来｜✅順調｜🔴過熱｜FAIL_INSEN｜終値1,794円｜💰179,700円｜—｜
- 1375 Yukiguni Factory Co., Ltd.｜granville_oshime｜✅順調｜🔴過熱｜FAIL_INSEN｜終値1,170円｜💰116,700円｜—｜
- 2659 SAN-A CO., LTD.｜granville_oshime｜✅順調｜🔴過熱｜PASS｜終値3,380円｜💰338,000円｜指値3296.4円｜
  > 📌業態: 沖縄県内流通首位。スーパー、レストラン、ドラッグストアを展開。ローソンと提携。ニチリウG。
  > いま: 終値3,380円・直近5日+2.11%（材料未確認）
  > 調子: ✅順調（3/13）— 質注意
  > 水準: 🔴過熱（0.0/7）— PER18.3倍・PEG15.72・52週87.7% ／ 💰単元33.8万円
  > 戦略: 3296.4円までの押し目を指値で待つ。SL3280.0円（25日線基準）
- 7956 ピジョン｜granville_oshime｜✅順調｜🔴過熱｜FAIL_INSEN｜終値2,142円｜💰215,550円｜—｜
- 6590 芝浦メカトロニクス｜granville_oshime｜➖横ばい｜🔴過熱｜FAIL_UWAHIGE｜終値4,065円｜💰403,000円｜—｜
- 7278 Exedy Corporation｜granville_oshime｜➖横ばい｜🔴過熱｜PASS｜終値6,220円｜💰622,000円｜指値6081.05円｜
  > 📌業態: アイシン系でクラッチ首位。自動車用トルクコンバーターが主力。マニュアル部品でも高シェア。
  > いま: 終値6,220円・直近5日+0.48%（材料未確認）
  > 調子: ➖横ばい（2/13）— 進捗判定不能(自動抽出範囲外)
  > 水準: 🔴過熱（1.0/7）— PER16.0倍・PEG—・52週94.4% ／ 💰単元62.2万円
  > 戦略: 6081.05円までの押し目を指値で待つ。SL6050.8円（25日線基準）
- 8101 GSI Creos Corporation｜granville_oshime｜⚠減速｜🔴過熱｜FAIL_INSEN｜終値2,727円｜💰277,500円｜—｜
- 9247 TRE HOLDINGS CORPORATION｜granville_oshime/granville_rebound｜🔻悪化｜🔴過熱｜FAIL_INSEN｜終値1,966円｜💰197,500円｜—｜
- 2175 SMS Co., Ltd.｜granville_oshime｜➖横ばい｜🔴過熱｜FAIL_UWAHIGE｜終値2,370円｜💰236,600円｜—｜
- 6638 ミマキエンジニアリング｜granville_oshime｜⚠減速｜⚪妥当｜PASS｜終値1,937円｜💰193,700円｜⛔型不一致: 既に支持帯以下｜⚠業績基調下向き
  > 📌業態: 広告・看板向け大型プリンター製造。世界首位級。産業、衣料向け強み。FA参入。
  > いま: 終値1,937円・直近5日-1.42%（材料未確認）
  > 調子: ⚠減速（1/13）— E軸=進捗率データ制約のため直近QoQトレンドで代用
  > 水準: ⚪妥当（3.0/7）— PER9.2倍・PEG—・52週59.7% ／ 💰単元19.4万円
  > 戦略: 発注対象外（⛔型不一致: 既に支持帯以下）
- 7981 Takara standard Co., Ltd.｜granville_oshime/granville_rebound｜⚠減速｜🟡やや割高｜FAIL_UWAHIGE｜終値3,100円｜💰306,500円｜—｜
- 2001 NIPPN Corporation｜granville_oshime｜⚠減速｜🔴過熱｜FAIL_INSEN｜終値2,936円｜💰295,000円｜—｜
- 2810 ハウス食品グループ本社｜granville_oshime/granville_rebound｜⚠減速｜🔴過熱｜PASS｜終値3,757円｜💰375,700円｜⛔型不一致: 既に支持帯以下｜⚠業績基調下向き
  > 📌業態: カレー、シチュー用ルウでトップ。飲料、健康食品も。乳酸菌事業を拡大。米国で豆腐。
  > いま: 終値3,757円・直近5日-0.32%（材料未確認）
  > 調子: ⚠減速（1/13）— E軸=進捗率データ制約のため直近QoQトレンドで代用
  > 水準: 🔴過熱（1.0/7）— PER19.7倍・PEG—・52週72.6% ／ 💰単元37.6万円
  > 戦略: 発注対象外（⛔型不一致: 既に支持帯以下）
- 3151 バイタルケーエスケー・ホールディングス（バイタルＫＳ）｜granville_oshime/granville_rebound/未マージPR由来｜🔻悪化｜🔴過熱｜PASS｜終値1,674円｜💰167,400円｜指値1644.46円｜⚠業績基調下向き
  > 📌業態: 東北と関西の医薬品卸、バイタルネットとケーエスケーが統合。介護コンサルや動物薬卸も。
  > いま: 終値1,674円・直近5日+5.02%（材料未確認）
  > 調子: 🔻悪化（1/13）— E軸判定不能(進捗データ不足)
  > 水準: 🔴過熱（1.0/7）— PER10.7倍・PEG—・52週89.4% ／ 💰単元16.7万円
  > 戦略: 1644.46円までの押し目を指値で待つ。SL1636.28円（25日線基準）
- 6333 TEIKOKU Corp.｜granville_oshime｜⚠減速｜🔴過熱｜FAIL_UWAHIGE｜終値3,430円｜💰337,500円｜—｜
- 8242 エイチ・ツー・オー　リテイリング｜granville_oshime/未マージPR由来｜⚠減速｜🔴過熱｜PASS｜終値2,970円｜💰297,000円｜指値2868.39円｜⚠業績基調下向き
  > 📌業態: 阪急、阪神百貨店が統合。流通グループ。スーパーのオアシス、イズミヤ、関西スーパー等。
  > いま: 終値2,970円・直近5日+4.67%（材料未確認）
  > 調子: ⚠減速（1/13）— 質注意
  > 水準: 🔴過熱（1.0/7）— PER14.5倍・PEG—・52週92.6% ／ 💰単元29.7万円
  > 戦略: 2868.39円までの押し目を指値で待つ。SL2854.12円（25日線基準）
- 9324 安田倉庫（安田倉）｜granville_oshime/未マージPR由来｜⚠減速｜🔴過熱｜FAIL_INSEN｜終値2,573円｜💰258,600円｜—｜
- 7128 UNISOL Holdings Corporation｜granville_oshime｜⚠減速｜🔴過熱｜FAIL_INSEN｜終値2,876円｜💰288,200円｜—｜
- 4415 BROAD ENTERPRISE CO.,LTD.｜granville_oshime/granville_rebound/未マージPR由来｜業績データ取得不可｜⚪妥当｜FAIL_INSEN｜終値1,273円｜💰133,500円｜—｜
- 8361 大垣共立銀行｜granville_oshime｜取得不可｜⚪妥当｜FAIL_INSEN｜終値7,720円｜💰792,000円｜—｜
- 8367 南都銀行｜granville_oshime｜取得不可｜⚪妥当｜FAIL_INSEN｜終値1,842円｜💰187,200円｜—｜
- 8544 Keiyo Bank, Ltd.｜granville_oshime｜業績データ取得不可｜⚪妥当｜FAIL_INSEN｜終値2,650円｜💰268,700円｜—｜
- 7860 Avex Inc.｜granville_oshime｜業績データ取得不可｜🔴過熱｜FAIL_UWAHIGE｜終値1,284円｜💰127,600円｜—｜
- 7184 富山第一銀行｜granville_oshime｜取得不可｜🔴過熱｜FAIL_INSEN｜終値3,100円｜💰317,500円｜—｜
- 3989 シェアリングテクノロジー｜granville_oshime｜業績データ取得不可｜🔴過熱｜FAIL_UWAHIGE｜終値1,540円｜💰153,900円｜—｜
- 8387 Shikoku Bank Ltd.｜granville_oshime｜取得不可｜🔴過熱｜FAIL_INSEN｜終値3,310円｜💰337,000円｜—｜
- 8511 日本証券金融｜granville_oshime｜取得不可｜🔴過熱｜FAIL_INSEN｜終値2,455円｜💰247,900円｜—｜
- 4722 Future Corporation｜granville_oshime/未マージPR由来｜業績?｜水準?｜FAIL_INSEN｜終値2,446円｜💰—｜—｜
- 8628 松井証券｜granville_oshime/未マージPR由来｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜終値1,105円｜💰110,900円｜—｜
- 8707 岩井コスモホールディングス｜granville_oshime｜取得不可｜⏸判定不能｜FAIL_INSEN｜終値4,555円｜💰460,000円｜—｜
- 9279 GIFT HOLDINGS INC.｜granville_oshime/未マージPR由来｜業績?｜水準?｜FAIL_INSEN｜終値5,180円｜💰—｜—｜
- 6613 Ｇ−ＱＤレーザ｜granville_rebound｜🔥絶好調｜🔴過熱｜PASS｜終値2,330円｜💰233,000円｜指値2330.0円｜⚠リスク枠超過
  > 📌業態: 半導体レーザ、網膜走査型レーザアイウェアなどの開発・製造・販売を手掛ける。
  > いま: 終値2,330円・直近5日+11.86%（材料未確認）
  > 調子: 🔥絶好調（10/13）— 赤字→黒字転換
  > 水準: 🔴過熱（2.0/7）— PER221.9倍・PEG2.20・52週61.2% ／ 💰単元23.3万円
  > 戦略: 当日終値2330.0円の指値で反転を取りにいく。SL1922.0円（直近5日安値）／⚠1単元リスク40800円（枠超過）
- 150A JSH｜granville_rebound｜🔥絶好調｜⚪妥当｜PASS｜終値752円｜💰75,200円｜指値752.0円｜
  > 📌業態: 障がい者雇用支援の農園や訪問看護・診療サービスなどを手掛ける。
  > いま: 終値752円・直近5日+13.25%（材料未確認）
  > 調子: 🔥絶好調（9/13）— E軸判定不能(進捗データ不足)
  > 水準: ⚪妥当（3.0/7）— PER22.2倍・PEG0.05・52週85.8% ／ 💰単元7.5万円
  > 戦略: 当日終値752.0円の指値で反転を取りにいく。SL636.0円（直近5日安値）
- 9147 ＮＩＰＰＯＮ　ＥＸＰＲＥＳＳ　ホールディングス｜granville_rebound｜🔥絶好調｜⚪妥当｜PASS｜終値5,713円｜💰571,300円｜指値5713.0円｜⚠リスク枠超過
  > 📌業態: 未取得（次回以降に取得）
  > いま: 終値5,713円・直近5日+1.76%（材料未確認）
  > 調子: 🔥絶好調（9/13）
  > 水準: ⚪妥当（3.0/7）— PER19.4倍・PEG0.13・52週97.0% ／ 💰単元57.1万円
  > 戦略: 当日終値5713.0円の指値で反転を取りにいく。SL5374.0円（直近5日安値）／⚠1単元リスク33900円（枠超過）
- 205A ロゴスホールディングス（ロゴスＨＤ）｜granville_rebound/未マージPR由来｜🔥絶好調｜💎割安｜FAIL_UWAHIGE｜終値1,688円｜💰167,700円｜—｜
- 9006 Keikyu Corporation｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜終値1,570円｜💰156,500円｜—｜
- 4420 イーソル｜granville_rebound｜🔥絶好調｜⚪妥当｜PASS｜終値703円｜💰70,300円｜指値703.0円｜
  > 📌業態: 組込み機器向けOS開発や組込みソフトウェアの受託開発。自動車、通信機器など。
  > いま: 終値703円・直近5日-1.82%（材料未確認）
  > 調子: 🔥絶好調（8/13）
  > 水準: ⚪妥当（4.0/7）— PER16.8倍・PEG0.43・52週44.2% ／ 💰単元7.0万円
  > 戦略: 当日終値703.0円の指値で反転を取りにいく。SL678.0円（直近5日安値）
- 4392 FIG｜granville_rebound｜🔥絶好調｜🟡やや割高｜FAIL_INSEN｜終値995円｜💰113,200円｜—｜
- 8141 新光商事｜granville_rebound/未マージPR由来｜🔥絶好調｜🟡やや割高｜FAIL_INSEN｜終値1,569円｜💰157,600円｜—｜
- 9941 太洋物産｜granville_rebound｜⚡好調｜💎割安｜FAIL_UWAHIGE｜終値1,176円｜💰116,900円｜—｜
- 6656 インスペック｜granville_rebound/未マージPR由来｜⚡好調｜⚪妥当｜PASS｜終値808円｜💰80,800円｜指値808.0円｜
  > 📌業態: 半導体やIT関連デバイスの外観検査装置メーカー。プリント基板のパターン検査など。
  > いま: 終値808円・直近5日-11.01%（材料未確認）
  > 調子: ⚡好調（6/13）— E軸判定不能(進捗データ不足)
  > 水準: ⚪妥当（4.0/7）— PER40.6倍・PEG1.44・52週28.4% ／ 💰単元8.1万円
  > 戦略: 当日終値808.0円の指値で反転を取りにいく。SL764.0円（直近5日安値）
- 7120 SHINKO Inc.｜granville_rebound｜⚡好調｜💎割安｜FAIL_UWAHIGE｜終値1,003円｜💰100,200円｜—｜
- 5076 インフロニアＨＤ｜granville_rebound｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜終値2,765円｜💰275,500円｜—｜
- 6380 オリエンタルチエン工業｜granville_rebound｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜終値3,940円｜💰391,500円｜—｜
- 7505 扶桑電通｜granville_rebound｜⚡好調｜⚪妥当｜PASS｜終値2,127円｜💰212,700円｜指値2127.0円｜
  > 📌業態: 富士通系ディーラー。ネットワーク、ソリューション構築。関連機器販売、運用・保守なども。
  > いま: 終値2,127円・直近5日+1.48%（材料未確認）
  > 調子: ⚡好調（5/13）— E軸=進捗率データ制約のため直近QoQトレンドで代用
  > 水準: ⚪妥当（4.0/7）— PER9.6倍・PEG1.67・52週67.9% ／ 💰単元21.3万円
  > 戦略: 当日終値2127.0円の指値で反転を取りにいく。SL2050.0円（直近5日安値）
- 6327 北川精機｜granville_rebound｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値3,090円｜💰323,500円｜—｜
- 9319 中央倉庫｜granville_rebound｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜終値1,808円｜💰183,600円｜—｜
- 8750 Daiichi Life Group. Inc.｜granville_rebound｜⚠減速｜⚪妥当｜FAIL_INSEN｜終値1,777円｜💰178,850円｜—｜
- 3393 スターティア　｜granville_rebound｜✅順調｜🟡やや割高｜FAIL_INSEN｜終値3,005円｜💰301,500円｜—｜
- 4063 信越化学工業｜granville_rebound｜✅順調｜🟡やや割高｜PASS_DOJI｜終値6,051円｜💰605,100円｜指値6051.0円｜
  > 📌業態: 塩ビ・半導体ウエハーで世界トップ。シリコーン(ケイ素樹脂)大手。セルロース、レアアース磁石も。
  > いま: 終値6,051円・直近5日-5.23%（材料未確認）
  > 調子: ✅順調（4/13）— E軸判定不能(進捗データ不足)
  > 水準: 🟡やや割高（2.0/7）— PER20.9倍・PEG2.40・52週47.3% ／ 💰単元60.5万円
  > 戦略: 当日終値6051.0円の指値で反転を取りにいく。SL6024.0円（直近5日安値）
- 1518 Mitsui Matsushima Holdings Co., Ltd.｜granville_rebound｜✅順調｜🟡やや割高｜FAIL_INSEN｜終値2,279円｜💰228,300円｜—｜
- 7460 Yagi & Co., Ltd.｜granville_rebound｜✅順調｜🟡やや割高｜PASS｜終値1,710円｜💰171,000円｜指値1710.0円｜
  > 📌業態: 繊維専門商社の老舗。糸やテキスタイルから二次製品まで展開。EC部門を強化。
  > いま: 終値1,710円・直近5日+2.40%（材料未確認）
  > 調子: ✅順調（3/13）— E軸判定不能(進捗データ不足)
  > 水準: 🟡やや割高（2.0/7）— PER11.3倍・PEG3.09・52週81.5% ／ 💰単元17.1万円
  > 戦略: 当日終値1710.0円の指値で反転を取りにいく。SL1647.0円（直近5日安値）
- 8081 カナデン｜granville_rebound｜✅順調｜🟡やや割高｜FAIL_UWAHIGE｜終値2,552円｜💰252,500円｜—｜
- 1860 戸田建設｜granville_rebound｜✅順調｜🔴過熱｜PASS｜終値1,524円｜💰152,350円｜指値1523.5円｜
  > 📌業態: 名門で業界準大手。堅実経営。病院・学校に強み。洋上風力発電に注力。
  > いま: 終値1,524円・直近5日+1.47%（材料未確認）
  > 調子: ✅順調（3/13）— E軸判定不能(当期進捗率取得不可(未算出))
  > 水準: 🔴過熱（1.0/7）— PER12.9倍・PEG—・52週79.2% ／ 💰単元15.2万円
  > 戦略: 当日終値1523.5円の指値で反転を取りにいく。SL1462.0円（直近5日安値）
- 4972 綜研化学｜granville_rebound｜✅順調｜🔴過熱｜FAIL_INSEN｜終値3,370円｜💰334,500円｜—｜
- 9854 愛眼｜granville_rebound｜✅順調｜🔴過熱｜FAIL_INSEN｜終値280円｜💰28,400円｜—｜
- 4320 ＣＥホールディングス｜granville_rebound｜✅順調｜🔴過熱｜FAIL_INSEN｜終値1,662円｜💰167,500円｜—｜
- 5998 アドバネクス｜granville_rebound｜➖横ばい｜⚪妥当｜PASS｜終値2,611円｜💰261,100円｜指値2611.0円｜⚠リスク枠超過
  > 📌業態: 精密ばね大手。事務機、自動車向け主力。生活・医療機向けも。海外生産大。
  > いま: 終値2,611円・直近5日+8.21%（材料未確認）
  > 調子: ➖横ばい（2/13）— E軸判定不能(当期進捗率取得不可(未算出))
  > 水準: ⚪妥当（3.0/7）— PER5.4倍・PEG—・52週61.9% ／ 💰単元26.1万円
  > 戦略: 当日終値2611.0円の指値で反転を取りにいく。SL2262.0円（直近5日安値）／⚠1単元リスク34900円（枠超過）
- 6703 沖電気工業｜granville_rebound｜➖横ばい｜⚪妥当｜FAIL_UWAHIGE｜終値2,689円｜💰268,600円｜—｜
- 8844 Cosmos Initia Co., Ltd.｜granville_rebound｜➖横ばい｜⚪妥当｜FAIL_UWAHIGE｜終値1,282円｜💰126,200円｜—｜
- 2483 翻訳センター｜granville_rebound｜➖横ばい｜🟡やや割高｜FAIL_INSEN｜終値2,216円｜💰220,500円｜—｜
- 5189 櫻護謨｜granville_rebound｜🔻悪化｜🟡やや割高｜PASS｜終値3,600円｜💰360,000円｜指値3600.0円｜⚠業績基調下向き
  > 📌業態: ゴムホース大手。消防・防災関連向けなど。航空自衛隊、ボーイングの認定工場。
  > いま: 終値3,600円・直近5日-0.41%（材料未確認）
  > 調子: 🔻悪化（2/13）— E軸判定不能(進捗データ不足)
  > 水準: 🟡やや割高（2.0/7）— PER8.7倍・PEG—・52週73.2% ／ 💰単元36.0万円
  > 戦略: 当日終値3600.0円の指値で反転を取りにいく。SL3425.0円（直近5日安値）
- 7459 MEDIPAL HOLDINGS Corporation｜granville_rebound｜➖横ばい｜🟡やや割高｜FAIL_INSEN｜終値2,902円｜💰291,750円｜—｜
- 5989 エイチワン｜granville_rebound/未マージPR由来｜⚠減速｜⚪妥当｜PASS｜終値1,566円｜💰156,600円｜指値1566.0円｜⚠業績基調下向き
  > 📌業態: ホンダ系の車体骨格部品メーカー。加工・溶接技術に強み。インド、タイなど海外展開。
  > いま: 終値1,566円・直近5日+0.90%（材料未確認）
  > 調子: ⚠減速（1/13）— E軸判定不能(進捗データ不足)
  > 水準: ⚪妥当（3.0/7）— PER4.0倍・PEG—・52週62.0% ／ 💰単元15.7万円
  > 戦略: 当日終値1566.0円の指値で反転を取りにいく。SL1486.0円（直近5日安値）
- 2217 Morozoff Limited｜granville_rebound｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜終値1,514円｜💰151,400円｜—｜
- 4980 Dexerials Corp.｜granville_rebound｜⚠減速｜🟡やや割高｜FAIL_UWAHIGE｜終値2,904円｜💰289,600円｜—｜
- 9001 東武鉄道｜granville_rebound｜⚠減速｜🟡やや割高｜FAIL_UWAHIGE｜終値3,029円｜💰301,400円｜—｜
- 9502 中部電力｜granville_rebound｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜終値2,897円｜💰290,650円｜—｜
- 3086 J. FRONT RETAILING Co., Ltd.｜granville_rebound｜⚠減速｜🔴過熱｜PASS｜終値3,056円｜💰305,600円｜指値3056.0円｜⚠業績基調下向き
  > 📌業態: 大丸、松坂屋が統合。大手百貨店グループ。テナント導入推進。パルコ、GINZA-SIXも。
  > いま: 終値3,056円・直近5日+7.08%（材料未確認）
  > 調子: ⚠減速（1/13）— E軸判定不能(進捗データ不足)
  > 水準: 🔴過熱（1.0/7）— PER25.8倍・PEG—・52週63.5% ／ 💰単元30.6万円
  > 戦略: 当日終値3056.0円の指値で反転を取りにいく。SL2818.5円（直近5日安値）
- 3776 ブロードバンドタワー｜granville_rebound｜⚠減速｜🔴過熱｜PASS｜終値243円｜💰24,300円｜指値243.0円｜⚠業績基調下向き
  > 📌業態: 都市型データセンター運用が主力。ビッグデータ、AIも。映像配信ネットワーク対応事業も。
  > いま: 終値243円・直近5日-4.33%（材料未確認）
  > 調子: ⚠減速（1/13）— 質注意
  > 水準: 🔴過熱（1.0/7）— PER31.2倍・PEG—・52週60.1% ／ 💰単元2.4万円
  > 戦略: 当日終値243.0円の指値で反転を取りにいく。SL237.0円（直近5日安値）
- 9735 Secom Co., Ltd.｜granville_rebound｜⚠減速｜🔴過熱｜PASS｜終値6,435円｜💰643,500円｜指値6435.0円｜⚠業績基調下向き
  > 📌業態: 未取得（次回以降に取得）
  > いま: 終値6,435円・直近5日+0.42%（材料未確認）
  > 調子: ⚠減速（1/13）— 進捗判定不能(自動抽出範囲外)
  > 水準: 🔴過熱（1.0/7）— PER24.3倍・PEG—・52週63.5% ／ 💰単元64.3万円
  > 戦略: 当日終値6435.0円の指値で反転を取りにいく。SL6252.0円（直近5日安値）
- 8566 Ricoh Leasing Company,Ltd.｜granville_rebound｜⚠減速｜🔴過熱｜FAIL_INSEN｜終値6,760円｜💰676,000円｜—｜
- 9301 三菱倉庫｜granville_rebound｜⚠減速｜🔴過熱｜PASS｜終値1,533円｜💰153,300円｜指値1533.0円｜⚠業績基調下向き
  > 📌業態: 未取得（次回以降に取得）
  > いま: 終値1,533円・直近5日+2.30%（材料未確認）
  > 調子: ⚠減速（1/13）— E軸判定不能(進捗データ不足)
  > 水準: 🔴過熱（0.0/7）— PER22.6倍・PEG131.97・52週79.7% ／ 💰単元15.3万円
  > 戦略: 当日終値1533.0円の指値で反転を取りにいく。SL1490.0円（直近5日安値）
- 1976 Meisei Industrial Co., Ltd.｜granville_rebound｜⚠減速｜⚪妥当｜FAIL_INSEN｜終値1,770円｜💰176,900円｜—｜
- 254A ＡＩフュージョンキャピタルグループ（ＡＩＦＣＧ）｜granville_rebound/未マージPR由来｜判定保留｜⚪妥当｜FAIL_UWAHIGE｜終値1,169円｜💰116,400円｜—｜
- 7182 ゆうちょ銀行｜granville_rebound｜取得不可｜⚪妥当｜FAIL_INSEN｜終値3,151円｜💰315,100円｜—｜
- 8630 Sompo Holdings,Inc.｜granville_rebound｜🔻悪化｜🔴過熱｜FAIL_INSEN｜終値6,708円｜💰675,700円｜—｜
- 9519 レノバ｜granville_rebound/未マージPR由来｜取得不可｜🔴過熱｜FAIL_INSEN｜終値950円｜💰96,000円｜—｜
- 6266 タツモ｜granville_rebound/未マージPR由来｜🔻悪化｜🔴過熱｜FAIL_INSEN｜終値3,470円｜💰354,500円｜—｜
- 8439 Tokyo Century Corporation｜granville_rebound｜業績?｜🔴過熱｜FAIL_INSEN｜終値2,546円｜💰255,700円｜—｜
- 3544 SATUDORA HOLDINGS CO., LTD.｜granville_rebound｜業績データ取得不可｜⏸判定不能｜FAIL_UWAHIGE｜終値1,249円｜💰124,800円｜—｜
- 3863 日本製紙｜granville_rebound｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜終値1,363円｜💰139,600円｜—｜
- 7740 Tamron Co., Ltd.｜granville_rebound/未マージPR由来｜業績?｜水準?｜FAIL_INSEN｜終値1,352円｜💰—｜—｜

## 変化点銘柄
（20銘柄・並び順はSTEP5.2(1)）

- 265A HMCOMM INC｜changepoint_watch/変化点🔔｜🚀確変｜🟢値頃｜FAIL_INSEN｜終値700円｜💰70,900円｜—｜
- 479A PRONI INC｜changepoint🔔/変化点🔔/変化点🔔🔔｜🔥絶好調｜⚪妥当｜PASS｜終値1,979円｜💰197,900円｜指値1979.0円｜⚠リスク枠超過
  > 📌業態: 法人向け受発注プラットフォーム「PRONI アイミツ」の運営などを手掛ける。
  > いま: 終値1,979円・直近5日+14.86%（材料未確認）
  > 調子: 🔥絶好調（10/13）— D軸判定不能(四半期データ不足)
  > 水準: ⚪妥当（4.0/7）— PER9.8倍・PEG0.08・52週86.9% ／ 💰単元19.8万円
  > 戦略: 発火日終値1979.0円の指値。追撃禁止・SL1652.0円。🔒実弾封印中（PL3紙ログ収集中）／⚠1単元リスク32700円（枠超過）
- 6080 M&A Capital Partners Co.,Ltd.｜changepoint/変化点🔔🔔｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜終値4,165円｜💰413,000円｜—｜
- 7695 交換できるくん｜changepoint/変化点🔔🔔｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜終値869円｜💰85,500円｜—｜
- 584A LiNKX｜changepoint🔔/変化点🔔/変化点🔔🔔｜🔥絶好調｜🟢値頃｜PASS_DOJI｜終値2,668円｜💰266,800円｜指値2668.0円｜
  > 📌業態: 金融分野を中心とした基幹システムなどのモダナイゼーション事業を手掛ける。
  > いま: 終値2,668円・直近5日-18.41%（材料未確認）
  > 調子: 🔥絶好調（9/13）— D軸判定不能(四半期データ不足)
  > 水準: 🟢値頃（5.0/7）— PER38.3倍・PEG0.61・52週32.2% ／ 💰単元26.7万円
  > 戦略: 発火日終値2668.0円の指値。追撃禁止・SL2635.0円。🔒実弾封印中（PL3紙ログ収集中）
- 3696 セレス｜changepoint/変化点🔔🔔｜🔥絶好調｜💎割安｜FAIL_INSEN｜終値2,251円｜💰226,700円｜—｜
- 9888 UEX, Ltd.｜変化点🔔🔔｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜終値1,212円｜💰121,200円｜—｜
- 4443 Sansan, Inc.｜changepoint/変化点🔔/変化点🔔🔔｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜終値2,248円｜💰223,100円｜—｜
- 9343 ibis inc.｜changepoint/変化点🔔🔔/未マージPR由来｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値770円｜💰76,600円｜—｜
- 3994 マネーフォワード｜changepoint/変化点🔔｜⚡好調｜🔴過熱｜PASS｜終値6,450円｜💰645,000円｜指値6450.0円｜⚠リスク枠超過
  > 📌業態: クラウド会計中心の法人向けバックオフィスSaaS事業が柱。個人向け家計簿アプリも。
  > いま: 終値6,450円・直近5日+7.50%（材料未確認）
  > 調子: ⚡好調（6/13）— E軸判定不能(進捗データ不足)
  > 水準: 🔴過熱（1.4/7）— PER—・PEG—・52週96.5% ／ 💰単元64.5万円
  > 戦略: 発火日終値6450.0円の指値。追撃禁止・SL5640.0円。🔒実弾封印中（PL3紙ログ収集中）／⚠1単元リスク81000円（枠超過）
- 286A ユカリア｜変化点🔔🔔｜⚡好調｜⚪妥当｜FAIL_INSEN｜終値817円｜💰82,000円｜—｜
- 4483 JMDC Inc.｜変化点🔔🔔｜⚡好調｜🟡やや割高｜FAIL_INSEN｜終値3,390円｜💰336,500円｜—｜
- 4441 トビラシステムズ｜changepoint/changepoint🔔/変化点🔔｜⚡好調｜🔴過熱｜FAIL_INSEN｜終値1,445円｜💰145,600円｜—｜
- 4498 サイバートラスト｜changepoint/changepoint🔔🔔/変化点🔔🔔｜✅順調｜⚪妥当｜FAIL_UWAHIGE｜終値1,325円｜💰131,300円｜—｜
- 218A リベラウェア｜changepoint/changepoint_watch/変化点🔔/未マージPR由来｜🔻悪化｜🔴過熱｜FAIL_INSEN｜終値1,113円｜💰112,800円｜—｜
- 598A CHATPLUS CO LTD｜changepoint_watch/変化点🔔/未マージPR由来｜✅順調｜⚪妥当｜PASS｜終値1,384円｜💰138,400円｜指値1384.0円｜
  > 📌業態: AIチャットボットツール「ChatPlus」などの開発・提供を手掛ける。
  > いま: 終値1,384円・直近5日-8.10%（材料未確認）
  > 調子: ✅順調（3/13）— D軸判定不能(四半期データ不足)
  > 水準: ⚪妥当（3.0/7）— PER18.6倍・PEG3.05・52週6.8% ／ 💰単元13.8万円
  > 戦略: 発火日終値1384.0円の指値。追撃禁止・SL1282.0円。🔒実弾封印中（PL3紙ログ収集中）
- 4488 AI inside Inc.｜changepoint/changepoint_watch/変化点🔔/変化点🔔🔔｜➖横ばい｜🟡やや割高｜FAIL_INSEN｜終値2,171円｜💰215,600円｜—｜
- 4375 Safie Inc.｜changepoint/変化点🔔/未マージPR由来｜取得不可｜💎割安｜FAIL_INSEN｜終値656円｜💰66,700円｜—｜
- 3923 ラクス｜変化点🔔｜判定保留(変則決算)｜⚪妥当｜FAIL_UWAHIGE｜終値1,134円｜💰111,300円｜—｜
- 4478 freee K.K.｜changepoint/changepoint_watch/変化点🔔🔔｜業績データ取得不可｜🟡やや割高｜PASS｜終値3,920円｜💰392,000円｜指値3920.0円｜⚠リスク枠超過
  > 📌業態: スモールビジネス向けクラウドERPサービスの提供。会計や会社設立、開業支援など。
  > いま: 終値3,920円・直近5日+17.01%（材料未確認）
  > 調子: 業績データ取得不可
  > 水準: 🟡やや割高（2.8/7）— PER—・PEG—・52週99.8% ／ 💰単元39.2万円
  > 戦略: 発火日終値3920.0円の指値。追撃禁止・SL3270.0円。🔒実弾封印中（PL3紙ログ収集中）／⚠1単元リスク65000円（枠超過）

## ⚡材料後出し
その日の足は開示前の情報。判定は参考値。

- 5301 東海カーボン: verdict=FAIL_INSEN・disclosure=📌その他重要開示・order_status=（提案対象外）

## 📢開示
使用した一覧URL:
- https://kabutan.jp/warning/?mode=4_2 （08月24日の取引時間中に決算発表・業績予想を修正した銘柄）
- https://kabutan.jp/warning/?mode=4_3 （08月24日の取引終了後に決算発表・業績予想を修正した銘柄）
- https://kabutan.jp/warning/?mode=4_4 （株価にインパクトがある開示情報：08月24日15時30分以降）
フォールバックなし（3ページとも取得成功）。

検知件数: 取引時間中3件・取引終了後1件・15:30以降インパクト6件 = 計10件

night_gate.pool一致: 2件（保有銘柄一致: 0件）
- 5301 東海カーボン: 📌その他重要開示
- 9279 GIFT HOLDINGS INC.: 📢上方修正

①-9(recalc_queue)へ引き渡し: 2件（9279・5301。いずれもFAIL_INSENでPASS/保有に非該当のため強制再計算対象外）

## 総当りゲート
branch_typeで5手法→グランビル→変化点にグループ化し、グループ内は判定別。

### 5手法
- PASS (21件): 5757(5,520)、5537(3,220)、7409(1,443)、3798(534)、3374(4,065)、1960(1,684)、7972(2,597)、7649(2,740)、1812(4,831)、9302(3,339)、6135(15,630)、1861(1,300)、1802(2,998)、6586(5,303)、1975(3,905)、1979(3,955)、9533(1,220)、7480(3,490)、4249(2,953)、4718(2,502)、1878(3,338)
- PASS_DOJI (1件): 5444(12,400)
- FAIL_UWAHIGE (35件): 3556(879)、5724(3,060)、9341(636)、9211(1,532)、6562(877)、262A(1,872)、7047(2,414)、3109(1,089)、8927(479)、558A(5,630)、4477(313)、2980(2,453)、4475(1,561)、4493(1,952)、3932(3,820)、8614(721)、7685(3,285)、7730(1,618)、6544(1,562)、7419(1,275)、7202(2,238)、3064(1,840)、2579(3,866)、9065(8,363)、5105(3,824)、8111(2,172)、1980(2,733)、6845(1,508)、6134(7,286)、3036(3,465)、7433(5,290)、7637(3,805)、6490(9,830)、3091(2,799)、8697(2,238)
- FAIL_INSEN (71件): 5254(4,180)、3441(2,662)、5136(1,930)、5243(2,550)、5586(894)、3723(2,899)、5027(811)、9270(2,132)、212A(3,085)、5246(838)、9554(1,761)、421A(3,945)、1435(178)、6298(1,321)、4377(2,404)、7318(1,450)、2334(505)、3915(2,281)、5574(2,774)、6630(823)、135A(4,345)、146A(3,735)、5892(2,382)、5590(693)、4058(2,449)、6071(947)、9552(1,105)、277A(1,851)、6785(2,876)、341A(2,003)、5038(2,176)、276A(3,555)、325A(1,800)、6492(13,660)、4894(5,250)、4165(716)、2594(2,037)、4973(4,665)、8139(2,344)、9467(1,215)、4599(354)、5938(1,760)、5301(1,651)、3288(8,071)、4516(3,623)、6013(3,065)、9072(5,454)、7731(1,980)、4536(1,874)、4553(3,875)、456A(1,657)、6632(1,008)、543A(273)、7157(1,481)、8366(2,641)、3131(5,840)、9308(2,136)、6324(5,680)、9962(3,626)、6857(34,500)、8084(4,745)、147A(1,036)、8388(8,930)、7267(1,747)、3289(1,352)、2733(2,690)、9861(3,843)、9616(3,418)、7581(7,250)、9044(3,033)、3191(2,298)

### グランビル
- PASS (41件): 5020(1,340)、5592(2,691)、9037(1,867)、2702(8,170)、1808(2,880)、6305(6,005)、9101(7,200)、8098(4,270)、8056(4,660)、1925(4,700)、9503(2,582)、9041(3,562)、3865(910)、6770(2,206)、3003(1,798)、6136(3,707)、7716(3,110)、7616(2,098)、9828(3,535)、6432(7,530)、2659(3,380)、7278(6,220)、6638(1,937)、2810(3,757)、3151(1,674)、8242(2,970)、6613(2,330)、150A(752)、9147(5,713)、4420(703)、6656(808)、7505(2,127)、7460(1,710)、1860(1,524)、5998(2,611)、5189(3,600)、5989(1,566)、3086(3,056)、3776(243)、9735(6,435)、9301(1,533)
- PASS_DOJI (2件): 6284(8,790)、4063(6,051)
- FAIL_UWAHIGE (41件): 3491(1,575)、3968(653)、8086(1,590)、8793(4,225)、4507(2,922)、8057(2,218)、2292(2,900)、2317(447)、8276(2,749)、2768(5,670)、6425(738)、9404(2,991)、7089(1,514)、2590(3,060)、166A(1,205)、2874(2,129)、6454(1,782)、2288(2,255)、7867(3,645)、8876(2,179)、5232(5,636)、6590(4,065)、2175(2,370)、7981(3,100)、6333(3,430)、7860(1,284)、3989(1,540)、205A(1,688)、9006(1,570)、9941(1,176)、7120(1,003)、5076(2,765)、6380(3,940)、9319(1,808)、8081(2,552)、6703(2,689)、8844(1,282)、4980(2,904)、9001(3,029)、254A(1,169)、3544(1,249)
- FAIL_INSEN (109件): 269A(2,625)、145A(895)、4521(3,980)、3623(1,198)、6222(976)、5932(672)、7744(2,005)、2975(1,572)、6023(2,984)、6718(2,863)、3048(1,797)、4848(1,881)、8919(3,680)、547A(454)、2585(1,596)、6571(1,305)、5885(3,015)、4847(1,315)、208A(3,015)、5036(1,636)、7611(2,986)、9627(6,152)、160A(2,023)、1716(1,435)、1898(1,500)、4826(545)、8570(1,710)、1605(3,889)、7679(1,708)、2282(6,391)、7231(3,095)、9869(6,590)、5302(4,855)、3076(2,935)、2982(418)、3880(986)、5406(2,024)、7943(3,120)、3993(3,160)、8425(1,371)、7287(2,592)、3116(2,261)、3222(833)、3765(2,433)、4765(620)、7911(5,002)、7806(8,510)、4419(1,381)、3498(7,840)、6103(4,900)、8008(2,191)、4413(2,980)、8522(6,820)、2674(2,689)、2602(2,053)、2780(5,100)、7888(909)、7970(2,240)、8923(1,818)、7085(976)、9517(890)、3479(1,871)、5384(3,610)、6925(3,872)、9031(3,106)、6055(2,059)、6237(4,185)、9274(1,122)、9882(1,794)、1375(1,170)、7956(2,142)、8101(2,727)、9247(1,966)、2001(2,936)、9324(2,573)、7128(2,876)、4415(1,273)、8361(7,720)、8367(1,842)、8544(2,650)、7184(3,100)、8387(3,310)、8511(2,455)、4722(2,446)、8628(1,105)、8707(4,555)、9279(5,180)、4392(995)、8141(1,569)、6327(3,090)、8750(1,777)、3393(3,005)、1518(2,279)、4972(3,370)、9854(280)、4320(1,662)、2483(2,216)、7459(2,902)、2217(1,514)、9502(2,897)、8566(6,760)、1976(1,770)、7182(3,151)、8630(6,708)、9519(950)、6266(3,470)、8439(2,546)、3863(1,363)、7740(1,352)

### 変化点
- PASS (4件): 479A(1,979)、3994(6,450)、598A(1,384)、4478(3,920)
- PASS_DOJI (1件): 584A(2,668)
- FAIL_UWAHIGE (4件): 6080(4,165)、7695(869)、4498(1,325)、3923(1,134)
- FAIL_INSEN (11件): 265A(700)、3696(2,251)、9888(1,212)、4443(2,248)、9343(770)、286A(817)、4483(3,390)、4441(1,445)、218A(1,113)、4488(2,171)、4375(656)

除籍リスト（first_seenから30暦日超）: 該当なし（0件）

## 機械詳細
- 検知内訳: プール341件（新規16件・除籍0件・未マージPR由来27件をgracious/newton/euler 3ブランチから統合）
- スキップ件数: 0件（Yahoo Finance取得は341+保有専用1(9304)=342件全て成功、リトライ0回）
- log追記件数: 1件（2026-08-24分を新規追加、既存11件と合わせて12件・30営業日以内）
- ヘッドライン抜粋件数: 抜粋なし（PASS/PASS_DOJI全70件に付与、上限は業態取得のみに適用）
- 群別内訳（ヘッドライン対象70件）: method内訳は別掲の総当りゲート参照
- gate_historyの書き込み結果: gate_history/2026-08-24.json 新規作成（night_gate_today.jsonとバイト単位で一致）
- grades.jsonの銘柄数とバイト数: 360銘柄・93,327バイト
- method_scoreを保持できた件数／null件数: 51件／290件
- ヘッドライン付与件数（PASS全件と一致するか）: 70件／PASS全70件 → 一致
- kabutan新規取得件数／50件上限で打ち切った件数: TOPページ50件取得（優先①static不足1件=7716＋優先②ラウンドロビン49件）／打ち切り4件（need_profile 53件中、上限到達により4件を次回以降へ繰越）／financeページ1件（7716のみ、他74件はgyoseki_cache next_earnings経由でキャッシュ再利用）
- profile_cacheの総数と本夜の追加件数: 総数100件（本夜+50件、うち49件round-robin＋1件7716手動）
- 業態が「未取得」のまま出た件数: 0件（PASS/PASS_DOJI全70件で業態取得済み）
- earnings_logの総数／本夜の追記件数／リターンを埋めた件数／日足が取れず埋められなかった件数: 0件／0件／0件／0件（本夜📊決算発表の検知が0件のため対象なし）
- gyoseki_cacheのhistoryに退避した件数: 0件（本夜の再計算は7716の1件のみで、新規キャッシュのためhistory対象外＝グレード変化元データなし）
- STEP4.8を実行したかスキップしたか: スキップ（week_open=false）
- master.jsonの変更行数: +7640/-6604（indent=1、目安5,000行は超過。詳細は検証結果V11参照）
