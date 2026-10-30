# 夜間ゲート 2026-10-30

## サマリー
- 評価数: 504 / PASS: 56（PASS_DOJI 4件を含む）
- 発注可能提案数: 25件
- 市場一言: 市場モード「レンジ様子見」（market.latest 2026-10-30）。プール502銘柄中PASS比率11.1%（陰線FAIL 336件・上髭FAIL 112件）。日経平均 −2.12%の全面安の日
- 実行モード: 通常（base_day=当日の引け値を対象）
- base_day: 2026-10-30（run_at 2026-10-30 20:50起動）
- week_open: true（翌営業日 11/02(月)）→ STEP 4.8 週末ブリーフを実施
- 📆 翌営業日 11/02(月): カレンダーイベントなし（T+2 11/04(水): カレンダーイベントなし）
- 📑指数: 低減対象 提案6件／PASS10件／プール67件・新規採用 0件（index_flags 2026-10-07 公表分・組入は10/30に実施済み）

## 検証結果
- V1 → はい（proposals25=results25=template25）
- V2 → はい（PASS56=提案25+除外31・order_status欠落0）
- V3 → はい（results504件重複0）
- V4 → はい（既存 valuation static 変更0）
- V5 → はい（許可キー外の変更 top[] ng[] pipeline[]）
- V6 → はい（grade絵文字不整合0）
- V8 → はい（模擬25行 不正0）
- V9 → はい（gate_history と today 一致）
- V10 → はい（base_day 4箇所一致 2026-10-30）
- V11 → いいえ（+10849/-9517（indent=2・往復一致）＝results504件全置換＋キャッシュ更新による実変更で全体再フォーマットではない（往復一致を検証済み）。5,000行を超過（前夜と同様の構造））
- V12 → はい（(a)(b)(c)一致）
- V13 → はい（958銘柄/541.7KiB・キー欠落0・nx不一致0・ix非null177(期待177)・spm検算True）
- V14 → はい（method_score 保持60件/null444件・不正0）
- V15 → はい（PASS56件中56件に付与（欠落0・キー不足0・(c)要確認0））
- V16 → はい（earnings_log総数152・本夜追記34・(a)📊全件記録True (b)grade_beforeは再計算前の値True (c)history<=4 True）
- V17 → はい（505銘柄/433.6KiB・保有3銘柄すべて収録・3日ルール判定3銘柄）
- V18 → はい（鮮度切れ18件・誤除外0）
- V19 → はい（verdicts504=評価504・nominations88（新規38/再指名50）・pool last_seen集合一致True）
- V20 → はい（987銘柄・nx非null751・hist持ち487・pxd361・取得元名称なしTrue）
- V7 → はい（必須セクション存在・週初のため今週のカタリストも存在）
- VLEAK → はい（公開物への保有情報 検出0件）

## 保有アラート
保有3銘柄・アラート8件（詳細は通知）

## 📅今週のカタリスト
対象期間: 11/02(月)〜11/09(月)（base_day の翌営業日から5営業日）
- 11/02(月) 653A — MabGenesis(653A) 上場予定
- 11/02(月) 9044 NANKAI Co., Ltd. — 決算（PASS/PASS_DOJI）
- 11/04(水) 656A — Allganize Holdings(656A) 上場予定
- 11/04(水) 8255 Axial Retailing, Inc. — 決算（PASS/PASS_DOJI）
- 11/05(木) 655A — LTV-X(655A) 上場予定
- 11/06(金) 2681 2nd RETAILING Co., Ltd. — 決算（PASS/PASS_DOJI）
- 11/06(金) 3289 Tokyu Fudosan Holdings Corp. — 決算（PASS/PASS_DOJI）
- 11/06(金) 3563 ＦＯＯＤ　＆　ＬＩＦＥ　ＣＯＭＰＡＮＩＥＳ — 決算（PASS/PASS_DOJI）
- 11/06(金) 4848 Fullcast Holdings Co., Ltd. — 決算（PASS/PASS_DOJI）
- 11/06(金) 4912 ライオン — 決算（PASS/PASS_DOJI）
- 11/06(金) 658A — estie(658A) 上場予定
- 11/06(金) 664A — TOKIUM(664A) 仮条件決定予定(想定価格1,620円)
- 11/06(金) 8113 Unicharm Corporation — 決算（PASS/PASS_DOJI）
- 11/06(金) 8410 Seven Bank, Ltd. — 決算（PASS/PASS_DOJI）
- 11/09(月) 7458 Daiichikosho Co., Ltd. — 決算（PASS/PASS_DOJI）
- 11/09(月) 9616 共立メンテナンス — 決算（PASS/PASS_DOJI）

**今週の市場イベント（日付計算＋固定表）**
- 11/02(月) —
- 11/04(水) —
- 11/05(木) —
- 11/06(金) —
- 11/09(月) 雇用統計明け
- 11/03(火) 東証休場（文化の日）
- 11/06(金) 米雇用統計（通例・金曜夜。例外あり）→ 11/09(月) 雇用統計明け
- WebSearch による市場イベント補足: 本実行では未実施（取得不可と扱う）

**週末の材料**: 本日の大引け以降（15:00〜）の開示が出た銘柄は ⚡材料後出し として下に全件掲載（発注提案なし）。

**変化点ウォッチ（🔔点灯）**
- 🔔🔔 4478 freee K.K.｜検知器 D2/D3
- 🔔 7695 交換できるくん｜検知器 D5
- 🔔 218A Liberaware｜検知器 D3

カタリストは日程であって売買理由ではない。跨ぐか手仕舞うかは事前に決める（教訓⑲）

## 前夜の結果
PL5口座への正式な反映は週次①-11の採点で行われる。ここは参考情報。
前夜2026-10-29の提案90件 → 約定77・不約定13・判定不能0
- 4053 momentum 指定582 → 約定582・終値578（-0.69%）
- 5757 momentum 指定4,505 → 約定4,505・終値4,550（+1.00%）
- 5537 momentum 指定3,405 → 約定3,405・終値3,385（-0.59%）
- 3077 momentum 指定1,189 → 約定1,189・終値1,180（-0.76%）
- 3843 momentum 指定1,959 → 約定1,959・終値2,013（+2.76%）
- 5344 reversal 指定56,250 → 約定55,000・終値51,470（-6.42%）
- 8336 reversal 指定2,633 → 約定2,609・終値2,600（-0.34%）
- 6324 reversal 指定5,480 → 約定5,350・終値5,163（-3.50%）
- 7733 reversal 指定1,769 → 約定1,750・終値1,742（-0.46%）
- 8346 reversal 指定986 → 約定974・終値970（-0.41%）
- 4088 reversal 指定2,877 → 約定2,877・終値2,877（+0.00%）
- 8386 reversal 指定2,885 → 約定2,862・終値2,854（-0.28%）
- 8522 reversal 指定6,060 → 約定6,010・終値5,980（-0.50%）
- 5333 reversal 指定4,851 → 約定4,738・終値4,613（-2.64%）
- 8393 reversal 指定2,486 → 約定2,445・終値2,465（+0.82%）
- 8399 reversal 指定2,868 → 約定2,841・終値2,812（-1.02%）
- 5331 reversal 指定3,350 → 約定3,300・終値3,220（-2.42%）
- 1944 reversal 指定6,464 → 約定6,372・終値5,894（-7.50%）
- 1952 reversal 指定3,065 → 約定3,060・終値2,953（-3.50%）
- 1860 reversal 指定1,465.5 → 約定1,465.5・終値1,442.5（-1.57%）
- 6055 reversal 指定2,118 → 約定2,076・終値2,033（-2.07%）
- 1719 reversal 指定1,759.5 → 約定1,759.5・終値1,750.5（-0.51%）
- 5844 reversal 指定4,174 → 約定4,174・終値4,139（-0.84%）
- 2379 reversal 指定1,507 → 約定1,490・終値1,498（+0.54%）
- 1963 reversal 指定2,151.5 → 約定2,150・終値2,114（-1.67%）
- 1969 reversal 指定4,168 → 約定4,140・終値3,992（-3.57%）
- 8585 reversal 指定760 → 約定759・終値767（+1.05%）
- 8194 reversal 指定2,449 → 約定2,449・終値2,470（+0.86%）
- 8253 reversal 指定4,124 → 約定4,124・終値4,139（+0.36%）
- 5831 reversal 指定3,122 → 約定3,110・終値3,062（-1.54%）
- 7381 reversal 指定1,129 → 約定1,113・終値1,130（+1.53%）
- 8345 reversal 指定2,191 → 約定2,150・終値2,188（+1.77%）
- 8367 reversal 指定1,804 → 約定1,784・終値1,785（+0.06%）
- 8370 reversal 指定1,620 → 約定1,610・終値1,580（-1.86%）
- 7384 reversal 指定4,210 → 約定4,185・終値4,280（+2.27%）
- 8304 reversal 指定3,051 → 約定3,025・終値3,015（-0.33%）
- 8334 reversal 指定2,638 → 約定2,625・終値2,605（-0.76%）
- 7186 reversal 指定1,701 → 約定1,695.5・終値1,677（-1.09%）
- 7322 reversal 指定1,900 → 約定1,881・終値1,879（-0.11%）
- 8354 reversal 指定7,050 → 約定7,015・終値6,955（-0.86%）
- 8359 reversal 指定2,463.5 → 約定2,463.5・終値2,445.5（-0.73%）
- 8600 reversal 指定1,060 → 約定1,053・終値1,050（-0.28%）
- 6613 momentum 指定2,418 → 約定2,418・終値2,406（-0.50%）
- 6407 reversal 指定4,790 → 約定4,720・終値4,645（-1.59%）
- 6981 reversal 指定6,890 → 約定6,490・終値6,358（-2.03%）
- 6235 reversal 指定2,410 → 約定2,325・終値2,230（-4.09%）
- 5208 reversal 指定2,648 → 約定2,598・終値2,518（-3.08%）
- 5302 reversal 指定4,915 → 約定4,915・終値4,885（-0.61%）
- 3496 momentum 指定4,810 → 約定4,810・終値4,850（+0.83%）
- 9064 momentum 指定1,965 → 約定1,968・終値1,969.5（+0.08%）
- 7970 momentum 指定2,565 → 約定2,565・終値2,536（-1.13%）
- 5838 momentum 指定6,092 → 約定6,092・終値5,919（-2.84%）
- 7199 momentum 指定2,263 → 約定2,263・終値2,273（+0.44%）
- 6196 momentum 指定1,403 → 約定1,403・終値1,413（+0.71%）
- 7747 momentum 指定3,642 → 約定3,642・終値3,668（+0.71%）
- 5184 momentum 指定4,185 → 約定4,190・終値4,170（-0.48%）
- 9163 momentum 指定2,263 → 約定2,265・終値2,273（+0.35%）
- 3569 momentum 指定3,405 → 約定3,405・終値3,390（-0.44%）
- 7734 momentum 指定3,560 → 約定3,560・終値3,480（-2.25%）
- 8012 momentum 指定1,281.5 → 約定1,285・終値1,260（-1.95%）
- 9837 momentum 指定1,801 → 約定1,808・終値1,811（+0.17%）
- 4375 momentum 指定656 → 約定656・終値644（-1.83%）
- 4912 momentum 指定1,808 → 約定1,808・終値1,829.5（+1.19%）
- 3040 oshime 指定3,051.2 → 約定3,051.2・終値3,030（-0.69%）
- 9509 oshime 指定1,104.3 → 約定1,082.5・終値1,079（-0.32%）
- 3891 reversal 指定6,460 → 約定6,170・終値6,080（-1.46%）
- 8364 reversal 指定2,772 → 約定2,772・終値2,837（+2.34%）
- 6490 reversal 指定10,370 → 約定10,070・終値9,850（-2.18%）
- 3653 reversal 指定918 → 約定903・終値871（-3.54%）
- 8360 reversal 指定1,321 → 約定1,301・終値1,301（+0.00%）
- 7380 reversal 指定2,455 → 約定2,434.5・終値2,423.5（-0.45%）
- 8368 reversal 指定2,183 → 約定2,163・終値2,138（-1.16%）
- 8377 reversal 指定759.2 → 約定752・終値749.4（-0.35%）
- 9308 changepoint 指定2,360 → 約定2,360・終値2,344（-0.68%）
- 5582 changepoint 指定1,819 → 約定1,819・終値1,794（-1.37%）
- 4478 changepoint 指定4,385 → 約定4,385・終値4,600（+4.90%）
- 593A changepoint 指定2,364 → 約定2,314・終値2,403（+3.85%）

## 模擬テンプレ
```
# base_day 2026-10-30 ／ 提案25件
# 使い方: 参戦する0〜3銘柄の行だけをコピーし、｜の後ろに参戦理由を書いてポジション株PJへ送る。
# 選ばなかった行は送らなくてよい（全行に理由を書く必要はない）。見送りは末尾の1行で足りる。
# 特定銘柄を理由つきで見送る場合のみ『模擬 見送り {code} ｜{理由}』を送る。
模擬 4743 kenmo_momentum 逆指値1608 SL1510.6 単元100 ｜
模擬 8276 choruko_reversal 指値2597 SL2523 単元100 ｜
模擬 9974 choruko_reversal 指値6500 SL6260 単元100 ｜
模擬 8954 choruko_reversal 指値86800 SL85400 単元1 ｜
模擬 9948 choruko_reversal 指値3535 SL3405 単元100 ｜
模擬 8194 choruko_reversal 指値2470 SL2406 単元100 ｜
模擬 6810 choruko_reversal 指値2265 SL2150 単元100 🎯 ｜
模擬 3927 granville_tenkan 逆指値967 SL908 単元100 ｜
模擬 8697 granville_tenkan 逆指値2118 SL1990 単元100 ｜
模擬 4763 granville_tenkan 逆指値1509 SL1417.5 単元100 ｜
模擬 4568 granville_tenkan 逆指値2758 SL2591.6 単元100 ｜
模擬 4848 granville_tenkan 逆指値1862 SL1749.3 単元100 ｜
模擬 8113 granville_tenkan 逆指値1013 SL951.3 単元100 ｜
模擬 2897 granville_tenkan 逆指値3045 SL2857.6 単元100 ｜
模擬 5233 granville_tenkan 逆指値4239 SL3980 単元100 ｜
模擬 2811 granville_tenkan 逆指値2739.5 SL2574.2 単元100 ｜
模擬 4922 granville_tenkan 逆指値6036 SL5664.4 単元100 ｜
模擬 8167 granville_tenkan 逆指値1381 SL1297.2 単元100 ｜
模擬 7921 granville_tenkan 逆指値4205 SL3948 単元100 ｜
模擬 4912 granville_tenkan 逆指値1838 SL1726.8 単元100 ｜
模擬 3563 granville_tenkan 逆指値5845 SL5484.9 単元100 ｜
模擬 9536 granville_oshime 指値2493.4 SL2471.3 単元100 ｜
模擬 8364 granville_rebound 指値2837 SL2567 単元100 ｜
模擬 9697 granville_rebound 指値3957 SL3698 単元100 ｜
模擬 4498 変化点🔔🔔 指値2150 SL2060 単元100 🔒 ｜
模擬 見送り ｜
```

## PASS内訳
PASS 56件 = 発注可能 25件 + 除外 31件（型不一致3/材料後出し6/鮮度切れ18/その他4）
- 5757 CK San-Etsu Co., Ltd.｜⛔提案なし(指名鮮度切れ 11営業日)
- 505A Geekly,Inc.｜⛔提案なし(指名鮮度切れ 12営業日)
- 2820 Yamami Co.｜⛔提案なし(指名鮮度切れ 15営業日)
- 3222 United Super Markets Holdings, Inc.｜⛔提案なし(指名鮮度切れ 12営業日)
- 8278 Fuji Co., Ltd.｜⛔提案なし(指名鮮度切れ 14営業日)
- 7458 Daiichikosho Co., Ltd.｜⛔提案なし(指名鮮度切れ 14営業日)
- 2809 Kewpie Corporation｜⛔提案なし(指名鮮度切れ 15営業日)
- 8198 Maxvalu Tokai Co., Ltd.｜⛔提案なし(指名鮮度切れ 11営業日)
- 9533 TOHO GAS Co., Ltd.｜⛔提案なし(材料後出し)
- 3289 Tokyu Fudosan Holdings Corp.｜⛔提案なし(指名鮮度切れ 15営業日)
- 3309 Sekisui House Reit. Inc.｜⛔提案なし(材料後出し)
- 9436 Okinawa Cellular Telephone Company｜⛔提案なし(指名鮮度切れ 12営業日)
- 6960 Fukuda Denshi Co., Ltd.｜⛔提案なし(材料後出し)
- 3994 マネーフォワード｜⛔提案なし(手法ブランチ不明)
- 7811 中本パックス｜⛔提案なし(手法ブランチ不明)
- 4443 Ｓａｎｓａｎ｜⛔提案なし(手法ブランチ不明)
- 6814 古野電｜⛔提案なし(手法ブランチ不明)
- 4544 H.U.Group Holdings, Inc.｜⛔提案なし(指名鮮度切れ 15営業日)
- 9163 Nareru Group Inc.｜⛔提案なし(材料後出し)
- 2871 ニチレイ｜⛔提案なし(指名鮮度切れ 21営業日)
- 8008 Yondoshi Holdings, Inc.｜⛔提案なし(指名鮮度切れ 15営業日)
- 6523 ＰＨＣホールディングス｜⛔型不一致: 既に支持帯以下
- 8410 Seven Bank, Ltd.｜⛔型不一致: 既に支持帯以下
- 1518 三井松島ホールディングス｜⛔提案なし(指名鮮度切れ 17営業日)
- 9044 NANKAI Co., Ltd.｜⛔提案なし(指名鮮度切れ 15営業日)
- 8043 Starzen Company Limited｜⛔提案なし(指名鮮度切れ 15営業日)
- 9616 共立メンテナンス｜⛔提案なし(材料後出し)
- 8255 Axial Retailing, Inc.｜⛔提案なし(指名鮮度切れ 11営業日)
- 8343 Akita Bank, Ltd.｜⛔型不一致: 既に支持帯以下
- 2681 2nd RETAILING Co., Ltd.｜⛔提案なし(指名鮮度切れ 16営業日)
- 9962 ミスミグループ本社｜⛔提案なし(材料後出し)

## 5手法銘柄
- 5137 Smart Drive Co. Ltd.｜kenmo_momentum｜🚀確変｜💎割安｜FAIL_UWAHIGE｜310円｜💰3.0万円｜—
- 276A CCReB Advisors Inc.｜granville_oshime/kenmo_momentum｜🚀確変｜⚪妥当｜FAIL_UWAHIGE｜4,410円｜💰46.0万円｜—｜⚠日程不明
- 6862 ミナトホールディングス｜kenmo_momentum/granville_rebound/granville_oshime｜🚀確変｜💎割安｜FAIL_INSEN｜3,460円｜💰44.0万円｜—｜⚡材料後出し｜📌
- 3556 RenetJapanGroup, Inc.｜kenmo_momentum/granville_tenkan｜🚀確変｜🟢値頃｜FAIL_INSEN｜852円｜💰9.0万円｜—
- 4053 Sun Asterisk, Inc.｜kenmo_momentum｜🚀確変｜⚪妥当｜FAIL_UWAHIGE｜578円｜💰5.7万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 4434 Serverworks Co., Ltd.｜kenmo_momentum/stf_kakuhen｜🚀確変｜⚪妥当｜FAIL_INSEN｜2,801円｜💰30.4万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 01/29 第2回/8）
- 5027 AnyMind Group Inc.｜kenmo_momentum｜🚀確変｜⚪妥当｜FAIL_INSEN｜749円｜💰7.8万円｜—
- 5136 tripla Co.,Ltd.｜changepoint/kenmo_momentum/changepoint🔔🔔/granville_oshime｜🚀確変｜⚪妥当｜FAIL_UWAHIGE｜2,565円｜💰25.2万円｜—｜⚠日程不明
- 5757 CK San-Etsu Co., Ltd.｜kenmo_momentum｜🔥絶好調｜💎割安｜PASS｜4,550円｜💰45.5万円｜⛔提案なし(指名鮮度切れ 11営業日)｜📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】黄銅棒・黄銅線で国内首位。精密部品、配管も。日本伸銅を子会社化。
  > 【いま】終値4,550円・直近5日+0.66%（材料未確認）
  > 【調子】🔥絶好調（10/13） — E軸判定不能(進捗データ不足)
  > 【水準】💎割安（7.0/7）— PER5.79倍・PEG0.0747・52週38.8% ／ 💰単元45.5万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 11営業日)）
- 9554 AViC Co. Ltd.｜kenmo_momentum/granville_tenkan｜🔥絶好調｜💎割安｜FAIL_INSEN｜1,535円｜💰15.5万円｜—
- 212A FIT EASY Inc.｜kenmo_momentum/granville_oshime｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜2,650円｜💰27.7万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 01/29 第2回/8）
- 3915 TerraSky Co., Ltd.｜kenmo_momentum｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜2,183円｜💰23.9万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 01/29 第2回/8）｜📌
- 421A Movin' Strategic Career CO.,LTD.｜kenmo_momentum/kenmo_newhigh｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜3,705円｜💰39.7万円｜—
- 5132 pluszero,Inc.｜kenmo_momentum｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1,778円｜💰18.6万円｜—｜⚠日程不明
- 6298 Y.A.C.HOLDINGS CO.,LTD.｜kenmo_momentum｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1,089円｜💰11.6万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 4377 ONE CAREER Inc.｜kenmo_momentum/granville_oshime｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜2,480円｜💰24.8万円｜—
- 5537 AlbaLink Co.,Ltd.｜kenmo_momentum/granville_oshime/granville_rebound｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜3,385円｜💰33.5万円｜—
- 7047 PORT INC.｜kenmo_momentum｜🔥絶好調｜💎割安｜FAIL_INSEN｜1,893円｜💰19.5万円｜—｜📋カルテ窓 11/16(残10営業日)
- 5821 Hirakawa Hewtech Corp.｜kenmo_momentum｜⚡好調｜💎割安｜FAIL_INSEN｜3,105円｜💰31.0万円｜—｜⏰決算 11/04(残2営業日)｜📑TOPIX低減対象（次 01/29 第2回/8）
- 4058 Toyokumo, Inc.｜kenmo_momentum｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,222円｜💰23.0万円｜—
- 6071 IBJ, Inc.｜kenmo_momentum｜⚡好調｜⚪妥当｜FAIL_INSEN｜884円｜💰9.1万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 9560 PROGRIT, Inc.｜kenmo_momentum｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜1,097円｜💰10.8万円｜—｜⚠日程不明
- 147A SORACOM,INC.｜kenmo_momentum｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜920円｜💰9.2万円｜—｜📌
- 5034 unerry, Inc.｜kenmo_momentum｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜2,531円｜💰27.4万円｜—
- 7678 ASAKUMA CO.,LTD.｜kenmo_momentum/kenmo_newhigh｜⚡好調｜🔴過熱｜FAIL_UWAHIGE｜4,130円｜💰39.5万円｜—｜⚠日程不明｜🎯2手法一致
- 9268 OPTIMUS GROUP Co., Ltd.｜kenmo_momentum｜⚡好調｜💎割安｜FAIL_INSEN｜333円｜💰3.4万円｜—
- 4771 F&M Co., Ltd.｜kenmo_momentum/kenmo_newhigh｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,883円｜💰29.6万円｜—｜📉決算反応日 11/02｜🎯2手法一致｜⚡材料後出し｜📊
- 4477 BASE, Inc.｜kenmo_momentum/granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜332円｜💰3.4万円｜—｜⚠日程不明｜⚡材料後出し｜👥
- 2980 SRE Holdings Corp.｜kenmo_momentum｜⚡好調｜💎割安｜FAIL_INSEN｜2,193円｜💰21.9万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 4412 Science Arts, Inc.｜kenmo_momentum｜⚡好調｜⚪妥当｜FAIL_INSEN｜1,216円｜💰12.9万円｜—｜⚠日程不明
- 505A Geekly,Inc.｜kenmo_momentum｜✅順調｜💎割安｜PASS｜1,182円｜💰11.8万円｜⛔提案なし(指名鮮度切れ 12営業日)｜⚠日程不明
  > 【業態】IT・Web・ゲーム業界に特化した人材紹介(転職エージェント)事業を手掛ける。
  > 【いま】終値1,182円・直近5日+4.51%（材料未確認）
  > 【調子】✅順調（4/13） — E軸判定不能(進捗データ不足)／D軸判定不能(四半期データ不足・中立1点)
  > 【水準】💎割安（7.0/7）— PER8.39倍・PEG0.4781・52週20.2% ／ 💰単元11.8万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 12営業日)）
- 4743 ITFOR Inc.｜kenmo_momentum｜✅順調｜🟢値頃｜PASS｜1,602円｜💰16.0万円｜momentum 1,608（✅即時可）｜📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】未取得（次回以降に取得）
  > 【いま】終値1,602円・直近5日-4.36%（材料未確認）
  > 【調子】✅順調（4/13） — E軸判定不能(進捗データ不足)
  > 【水準】🟢値頃（5.0/7）— PER12.47倍・PEG0.5974・52週40.9% ／ 💰単元16.0万円
  > 【戦略】当日高値超えの逆指値1,608円で順張り参戦を検討。上限1,624.1円・SL1,510.6円目安
- 5038 eWeLL Co.,Ltd｜kenmo_momentum｜✅順調｜⚪妥当｜FAIL_INSEN｜2,308円｜💰23.4万円｜—
- 6629 TECHNO HORIZON Co., Ltd.｜granville_tenkan/kenmo_momentum｜✅順調｜⚪妥当｜FAIL_INSEN｜897円｜💰9.5万円｜—｜📉決算反応日 11/02｜⚡材料後出し｜📊
- 6289 Giken Ltd.｜granville_tenkan/kenmo_momentum｜⚠減速｜🟡やや割高｜FAIL_UWAHIGE｜1,954円｜💰19.8万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 01/29 第2回/8）
- 3077 Horiifoodservice Co., Ltd.｜kenmo_momentum/granville_rebound｜判定保留(変則決算)｜🟢値頃｜FAIL_INSEN｜1,180円｜💰11.9万円｜—｜⚠日程不明
- 618A KOMPEITO Inc.｜kenmo_momentum/kenmo_newhigh｜取得不可｜⚪妥当｜FAIL_INSEN｜1,990円｜💰21.3万円｜—｜⚠日程不明
- 7567 Sakae Electronics Corp.｜kenmo_newhigh｜🚀確変｜⚪妥当｜FAIL_INSEN｜627円｜💰6.4万円｜—
- 6337 Tesec Corporation｜kenmo_newhigh/granville_rebound｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜2,582円｜💰34.2万円｜—｜⚠日程不明
- 446A ノースサンド｜kenmo_newhigh｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜2,820円｜💰28.6万円｜—｜⚠日程不明
- 3696 セレス｜kenmo_newhigh｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜2,180円｜💰22.5万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 2930 北の達人コーポレーション｜kenmo_newhigh｜⚡好調｜🔴過熱｜FAIL_INSEN｜150円｜💰1.5万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 01/29 第2回/8）
- 4379 Photosynth inc.｜kenmo_newhigh｜⚡好調｜🔴過熱｜FAIL_INSEN｜492円｜💰5.2万円｜—
- 2820 Yamami Co.｜kenmo_newhigh｜✅順調｜🟡やや割高｜PASS｜6,900円｜💰69.0万円｜⛔提案なし(指名鮮度切れ 15営業日)
  > 【業態】西日本で豆腐と関連製品を製造・販売。中国地方で高シェア。関東に注力中。
  > 【いま】終値6,900円・直近5日+5.83%（材料未確認）
  > 【調子】✅順調（4/13） — E軸判定不能(進捗データ不足)
  > 【水準】🟡やや割高（2.0/7）— PER23.26倍・PEG1.2261・52週92.1% ／ 💰単元69.0万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 15営業日)）
- 4933 I-ne CO., LTD.｜kenmo_newhigh｜🔻悪化｜⚪妥当｜FAIL_UWAHIGE｜2,460円｜💰24.8万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 3843 Freebit Co., Ltd.｜kenmo_newhigh/granville_tenkan｜✅順調｜🟡やや割高｜FAIL_UWAHIGE｜2,013円｜💰19.5万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 01/29 第2回/8）｜📌
- 4331 Take and Give. Needs Co., Ltd.｜kenmo_newhigh｜✅順調｜🔴過熱｜FAIL_UWAHIGE｜843円｜💰8.2万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 7161 Jimoto Holdings, Inc.｜kenmo_newhigh｜業績データ取得不可｜⚪妥当｜FAIL_INSEN｜560円｜💰5.7万円｜—
- 4565 Nxera Pharma Co., Ltd.｜granville_oshime/kenmo_newhigh｜業績データ取得不可(経常益予想非開示)｜🟡やや割高｜FAIL_UWAHIGE｜1,440円｜💰13.6万円｜—｜📉決算反応日 11/02｜⚡材料後出し｜📊
- 6278 ユニオンツール｜choruko_reversal｜🚀確変｜🟢値頃｜FAIL_INSEN｜12,280円｜💰134.0万円｜—
- 6875 メガチップス｜choruko_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜9,880円｜💰102.1万円｜—｜⏰決算 11/06(残4営業日)
- 8871 GOLDCREST Co., Ltd.｜choruko_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜2,496円｜💰28.7万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 3391 TSURUHA Holdings, Inc.｜choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜2,236円｜💰22.2万円｜—｜⚠日程不明
- 5344 MARUWA CO., LTD.｜choruko_reversal｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜51,470円｜💰562.5万円｜—｜⚠日程不明
- 6516 Sanyo Denki Co., Ltd.｜choruko_reversal｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜4,800円｜💰55.4万円｜—｜⚠日程不明
- 6754 アンリツ｜ai_reversal/choruko_reversal｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜2,754.5円｜💰31.2万円｜—
- 3036 アルコニックス｜choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜3,015円｜💰31.2万円｜—｜⏰決算 11/06(残4営業日)
- 6268 ナブテスコ｜choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜4,311円｜💰42.9万円｜—
- 6481 THK Co., Ltd.｜choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜5,727円｜💰64.3万円｜—
- 7433 Hakuto Co., Ltd.｜ai_reversal/granville_oshime/choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1,748円｜💰18.1万円｜—｜⚡材料後出し｜📌
- 8336 武蔵野銀行｜granville_oshime/choruko_reversal/granville_rebound｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜2,600円｜💰26.3万円｜—｜⏰決算 11/06(残4営業日)
- 6324 Harmonic Drive Systems Inc.｜choruko_reversal｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜5,163円｜💰54.8万円｜—
- 6645 OMRON Corporation｜granville_rebound/choruko_reversal｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜5,268円｜💰55.9万円｜—
- 3222 United Super Markets Holdings, Inc.｜choruko_reversal｜🔥絶好調｜🔴過熱｜PASS｜748円｜💰7.5万円｜⛔提案なし(指名鮮度切れ 12営業日)｜⚠日程不明｜⚠織り込み済みの可能性（押し目待ち推奨圏）
  > 【業態】イオン系、首都圏の食品スーパー最大手。マルエツ、カスミ、マックスバリュ関東が統合。
  > 【いま】終値748円・直近5日-2.73%（材料未確認）
  > 【調子】🔥絶好調（9/13）
  > 【水準】🔴過熱（1.0/7）— PER1068.57倍・PEG11.1916・52週8.6% ／ 💰単元7.5万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 12営業日)）
- 1803 Shimizu Corporation｜choruko_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜2,055円｜💰21.0万円｜—｜⏰決算 11/09(残5営業日)
- 5301 Tokai Carbon Co., Ltd.｜choruko_reversal/granville_rebound｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜1,926円｜💰19.3万円｜—｜⏰決算 11/05(残3営業日)
- 7733 Olympus Corp.｜choruko_reversal｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜1,742円｜💰17.7万円｜—
- 8346 東邦銀行｜granville_oshime/granville_rebound/choruko_reversal｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜970円｜💰9.9万円｜—｜⏰決算 11/06(残4営業日)
- 4088 Air Water Inc.｜choruko_reversal｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜2,877円｜💰28.8万円｜—｜⚠日程不明
- 7004 カナデビア｜choruko_reversal｜⚠減速｜💎割安｜FAIL_INSEN｜1,022円｜💰10.5万円｜—｜⏰決算 11/05(残3営業日)
- 6370 栗田工業｜choruko_reversal｜⚡好調｜🟢値頃｜FAIL_INSEN｜5,647円｜💰69.8万円｜—｜⏰決算 11/05(残3営業日)
- 8386 百十四銀行｜choruko_reversal/granville_rebound｜⚡好調｜🟢値頃｜FAIL_INSEN｜2,854円｜💰28.9万円｜—
- 8522 Bank of Nagoya, Ltd.｜choruko_reversal/granville_rebound｜⚡好調｜🟢値頃｜FAIL_INSEN｜5,980円｜💰60.6万円｜—
- 2874 YOKOREI CO. LTD.｜granville_rebound/choruko_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜1,724円｜💰17.9万円｜—｜📌
- 6302 住友重機械工業｜granville_tenkan/choruko_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜5,276円｜💰54.7万円｜—｜📉決算反応日 11/02｜⚡材料後出し｜📊
- 3116 Toyota Boshoku Corp.｜choruko_reversal｜⚡好調｜💎割安｜FAIL_INSEN｜2,020.5円｜💰22.2万円｜—｜⚠日程不明
- 8987 Japan Excellent, Inc.｜choruko_reversal｜⚡好調｜🟢値頃｜FAIL_INSEN｜124,100円｜💰12.6万円｜—｜⚠日程不明｜⚡材料後出し｜📌
- 5101 Yokohama Rubber Co., Ltd.｜choruko_reversal｜⚡好調｜🟢値頃｜FAIL_INSEN｜6,280円｜💰73.5万円｜—
- 8282 K'S HOLDINGS CORPORATION｜choruko_reversal｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜1,699.5円｜💰17.0万円｜—｜⏰決算 11/05(残3営業日)
- 6332 月島ホールディングス｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,318円｜💰23.7万円｜—｜⏰決算 11/06(残4営業日)
- 8088 岩谷産業｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜1,925円｜💰19.3万円｜—
- 9412 SKY Perfect JSAT Corporation｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜1,808円｜💰18.6万円｜—｜⏰決算 11/04(残2営業日)｜⚡材料後出し｜📌
- 5333 ＮＧＫ｜choruko_reversal/ai_reversal｜⚡好調｜🟡やや割高｜FAIL_INSEN｜4,613円｜💰48.5万円｜—｜📉決算反応日 11/02｜⚡材料後出し｜📊
- 8125 Wakita & Co., Ltd.｜choruko_reversal｜⚡好調｜🔴過熱｜FAIL_UWAHIGE｜1,896円｜💰18.7万円｜—｜⚠日程不明
- 7721 Tokyo Keiki Inc.｜choruko_reversal｜⚡好調｜🟢値頃｜FAIL_INSEN｜5,510円｜💰55.8万円｜—｜⏰決算 11/06(残4営業日)｜⚡材料後出し｜📌
- 8278 Fuji Co., Ltd.｜choruko_reversal｜⚡好調｜🟢値頃｜PASS｜1,995円｜💰19.9万円｜⛔提案なし(指名鮮度切れ 14営業日)｜⚠日程不明
  > 【業態】愛媛地盤で四国最大スーパー。中国地方も展開。マックスバリュ西日本と合併。
  > 【いま】終値1,995円・直近5日+0.10%（材料未確認）
  > 【調子】⚡好調（5/13）
  > 【水準】🟢値頃（5.0/7）— PER24.69倍・PEG0.6619・52週28.2% ／ 💰単元19.9万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 14営業日)）
- 8714 池田泉州ホールディングス｜granville_oshime/choruko_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜916円｜💰9.7万円｜—
- 8393 Miyazaki Bank Ltd.｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜2,465円｜💰24.9万円｜—｜⏰決算 11/06(残4営業日)
- 8399 琉球銀行｜choruko_reversal/granville_rebound｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,812円｜💰28.7万円｜—
- 268A Rigaku Holdings Corporation｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜1,438円｜💰14.8万円｜—
- 7458 Daiichikosho Co., Ltd.｜choruko_reversal｜⚡好調｜⚪妥当｜PASS｜1,728円｜💰17.3万円｜⛔提案なし(指名鮮度切れ 14営業日)｜⏰決算 11/09(残5営業日)
  > 【業態】業務用カラオケ機器の販売・レンタル最大手。カラオケルーム「ビッグエコー」や飲食店も運営。
  > 【いま】終値1,728円・直近5日-2.40%（材料未確認）
  > 【調子】⚡好調（5/13）
  > 【水準】⚪妥当（3.0/7）— PER14.18倍・PEG1.8043・52週50.0% ／ 💰単元17.3万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 14営業日)）
- 2782 Seria Co., Ltd.｜choruko_reversal｜⚡好調｜🔴過熱｜FAIL_UWAHIGE｜4,330円｜💰44.0万円｜—｜📉決算反応日 11/02｜⚡材料後出し｜📊
- 2809 Kewpie Corporation｜choruko_reversal｜⚡好調｜🔴過熱｜PASS｜4,613円｜💰46.1万円｜⛔提案なし(指名鮮度切れ 15営業日)｜⚠日程不明
  > 【業態】マヨネーズ・ドレッシング最大手。サラダ・惣菜も。医・介護食やファインケミカルにも展開。
  > 【いま】終値4,613円・直近5日+1.30%（材料未確認）
  > 【調子】⚡好調（5/13）
  > 【水準】🔴過熱（1.0/7）— PER24.42倍・PEG3.4969・52週69.9% ／ 💰単元46.1万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 15営業日)）
- 9072 NIKKON Holdings Co., Ltd.｜choruko_reversal｜⚡好調｜🔴過熱｜FAIL_INSEN｜4,082円｜💰50.8万円｜—｜⏰決算 11/06(残4営業日)
- 6454 Max Co., Ltd.｜granville_tenkan/choruko_reversal｜⚡好調｜🔴過熱｜FAIL_INSEN｜1,716円｜💰19.6万円｜—
- 4666 Park24 Co., Ltd.｜choruko_reversal｜✅順調｜💎割安｜FAIL_INSEN｜1,763円｜💰18.3万円｜—｜⚠日程不明
- 7731 ニコン｜choruko_reversal｜✅順調｜🟢値頃｜FAIL_INSEN｜1,633.5円｜💰17.3万円｜—｜⏰決算 11/05(残3営業日)｜⚡材料後出し｜📌
- 3279 Activia Properties, Inc.｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_UWAHIGE｜124,300円｜💰12.7万円｜—｜⚠日程不明｜⚡材料後出し｜📌
- 8381 San-in Godo Bank Ltd.｜choruko_reversal/granville_rebound｜✅順調｜⚪妥当｜FAIL_INSEN｜2,105円｜💰20.8万円｜—
- 8524 North Pacific Bank, Ltd.｜granville_rebound/choruko_reversal｜⚠減速｜⚪妥当｜FAIL_UWAHIGE｜1,214円｜💰11.8万円｜—
- 3282 Comforia Residential REIT, Inc.｜choruko_reversal｜✅順調｜🟡やや割高｜FAIL_INSEN｜86,800円｜💰9.0万円｜—｜⚠日程不明｜⚡材料後出し｜📌
- 8952 Japan Real Estate Investment Corp.｜choruko_reversal｜✅順調｜🟡やや割高｜FAIL_UWAHIGE｜107,600円｜💰10.9万円｜—｜📋カルテ窓 11/16(残10営業日)｜⚡材料後出し｜📌
- 6925 Ushio Inc.｜choruko_reversal｜✅順調｜🟡やや割高｜FAIL_INSEN｜3,212円｜💰33.5万円｜—｜⏰決算 11/06(残4営業日)
- 7276 Koito Manufacturing Co., Ltd.｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜2,343.5円｜💰26.9万円｜—｜⚠日程不明
- 1861 Kumagai Gumi Co., Ltd.｜choruko_reversal｜✅順調｜💎割安｜FAIL_INSEN｜1,240円｜💰12.5万円｜—
- 1417 MIRAIT ONE Corporation｜choruko_reversal｜✅順調｜🟢値頃｜FAIL_INSEN｜3,290円｜💰34.1万円｜—｜⏰決算 11/09(残5営業日)
- 5331 ノリタケ｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜3,220円｜💰33.5万円｜—｜⏰決算 11/05(残3営業日)
- 3148 Create SD Holdings Co., Ltd.｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_UWAHIGE｜3,170円｜💰31.4万円｜—｜⚠日程不明
- 3433 TOCALO Co., Ltd.｜granville_tenkan/ai_reversal/choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜2,647円｜💰27.0万円｜—｜⏰決算 11/05(残3営業日)
- 6368 Organo Corp.｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜2,202.5円｜💰25.4万円｜—｜⏰決算 11/04(残2営業日)
- 8198 Maxvalu Tokai Co., Ltd.｜choruko_reversal｜✅順調｜⚪妥当｜PASS｜3,100円｜💰31.0万円｜⛔提案なし(指名鮮度切れ 11営業日)｜⚠日程不明
  > 【業態】イオン系の食品スーパー。旧ヤオハンを母体に静岡県を中心とする出店。
  > 【いま】終値3,100円・直近5日-1.74%（材料未確認）
  > 【調子】✅順調（3/13）
  > 【水準】⚪妥当（4.0/7）— PER10.63倍・PEG1.5759・52週7.1% ／ 💰単元31.0万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 11営業日)）
- 9882 Yellow Hat Ltd.｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜1,600円｜💰16.1万円｜—｜📉決算反応日 11/02｜⚡材料後出し｜📊
- 1820 Nishimatsu Construction Co., Ltd.｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜5,257円｜💰53.9万円｜—｜📌
- 1944 Kinden Corporation｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜5,894円｜💰64.6万円｜—｜📉決算反応日 11/02｜⚡材料後出し｜📊
- 1952 Shin Nippon Air Technologies Co., Ltd.｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜2,953円｜💰30.6万円｜—
- 6269 Modec, Inc.｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜7,967円｜💰81.2万円｜—
- 7003 Mitsui ES Holdings Co., Ltd.｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜3,456円｜💰35.9万円｜—
- 8584 Jaccs Co., Ltd.｜choruko_reversal｜🔻悪化｜⚪妥当｜FAIL_INSEN｜3,340円｜💰33.2万円｜—｜⏰決算 11/05(残3営業日)
- 1860 Toda Corporation｜choruko_reversal｜✅順調｜🟡やや割高｜FAIL_INSEN｜1,442.5円｜💰14.7万円｜—
- 4966 上村工業｜choruko_reversal｜✅順調｜🟡やや割高｜FAIL_INSEN｜18,190円｜💰185.4万円｜—
- 8066 Mitani Corporation｜granville_rebound/choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_UWAHIGE｜2,833円｜💰28.2万円｜—
- 2659 SAN-A CO., LTD.｜choruko_reversal｜✅順調｜🔴過熱｜FAIL_INSEN｜3,200円｜💰31.8万円｜—｜⚠日程不明
- 5021 Cosmo Energy Holdings Co., Ltd.｜choruko_reversal｜🔻悪化｜🔴過熱｜FAIL_INSEN｜4,268円｜💰43.7万円｜—
- 6055 Japan Material Co., Ltd.｜choruko_reversal｜✅順調｜🔴過熱｜FAIL_INSEN｜2,033円｜💰21.2万円｜—
- 7984 Kokuyo Co., Ltd.｜choruko_reversal｜✅順調｜🔴過熱｜FAIL_UWAHIGE｜868.1円｜💰8.9万円｜—
- 9533 TOHO GAS Co., Ltd.｜choruko_reversal｜🔻悪化｜🔴過熱｜PASS｜1,275円｜💰12.8万円｜⛔提案なし(材料後出し)｜⚡材料後出し｜⚠業績基調が下向き（🔻悪化）｜🔁
  > 【業態】都市ガス大手。愛知、岐阜、三重が拠点。LPGに強み。コージェネ事業に注力。
  > 【いま】終値1,275円・直近5日+6.16%・🔁自己株式立会外買付取引（ToSTNeT-3）による自己株式の取得結果に関するお知らせ
  > 【調子】🔻悪化（3/13） — 経常減益-34.0%／質注意
  > 【水準】🔴過熱（1.0/7）— PER19.71倍・PEG—・52週52.8% ／ 💰単元12.8万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 2805 S&B Foods Inc.｜granville_rebound/choruko_reversal｜✅順調｜🔴過熱｜FAIL_INSEN｜6,540円｜💰68.3万円｜—｜📉決算反応日 11/02｜📊
- 6807 Japan Aviation Electronics Industry, Limited｜choruko_reversal｜✅順調｜🔴過熱｜FAIL_INSEN｜2,485円｜💰29.3万円｜—｜⚠日程不明
- 3289 Tokyu Fudosan Holdings Corp.｜choruko_reversal｜➖横ばい｜🟢値頃｜PASS｜1,230円｜💰12.3万円｜⛔提案なし(指名鮮度切れ 15営業日)｜⏰決算 11/06(残4営業日)
  > 【業態】総合不動産大手。首都圏で住宅事業。商業ビルが収益源。リゾート開発、再エネ等。
  > 【いま】終値1,230円・直近5日-0.40%（材料未確認）
  > 【調子】➖横ばい（2/13） — 進捗データ欠損(判定不能)
  > 【水準】🟢値頃（5.0/7）— PER8.77倍・PEG0.9826・52週14.5% ／ 💰単元12.3万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 15営業日)）
- 8818 Keihanshin Building Co., Ltd.｜choruko_reversal｜➖横ばい｜⚪妥当｜FAIL_INSEN｜926円｜💰9.4万円｜—｜📉決算反応日 11/02｜⚡材料後出し｜📊
- 1333 Umios Corporation｜choruko_reversal｜➖横ばい｜⚪妥当｜FAIL_UWAHIGE｜1,203円｜💰12.2万円｜—｜⚠日程不明
- 1719 HAZAMA ANDO Corporation｜choruko_reversal｜➖横ばい｜⚪妥当｜FAIL_INSEN｜1,750.5円｜💰17.6万円｜—
- 1833 Okumura Corporation｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜5,290円｜💰53.5万円｜—
- 6632 JVCKENWOOD Corporation｜choruko_reversal｜➖横ばい｜⚪妥当｜FAIL_INSEN｜885円｜💰9.9万円｜—｜📉決算反応日 11/02｜⚡材料後出し｜📊
- 6674 ジーエス・ユアサ　コーポレーション｜choruko_reversal｜➖横ばい｜⚪妥当｜FAIL_INSEN｜4,613円｜💰47.2万円｜—｜⏰決算 11/06(残4営業日)
- 9503 Kansai Electric Power Company, Incorporated｜choruko_reversal/granville_rebound｜🔻悪化｜⚪妥当｜FAIL_INSEN｜2,614.5円｜💰27.5万円｜—
- 3445 RS Technologies Co. Ltd.｜choruko_reversal｜➖横ばい｜🟡やや割高｜FAIL_INSEN｜4,875円｜💰50.1万円｜—｜⚠日程不明
- 6366 Chiyoda Corp.｜choruko_reversal｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜586円｜💰6.1万円｜—｜⏰決算 11/04(残2営業日)
- 7220 Musashi Seimitsu Industry Co., Ltd.｜choruko_reversal｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜2,449円｜💰24.2万円｜—
- 7278 Exedy Corporation｜choruko_reversal｜➖横ばい｜🟡やや割高｜FAIL_INSEN｜5,130円｜💰58.1万円｜—｜⚠日程不明
- 5844 Kyoto Financial Group,Inc.｜choruko_reversal｜🔻悪化｜🔴過熱｜FAIL_INSEN｜4,139円｜💰41.7万円｜—
- 2379 dip Corporation｜choruko_reversal｜⚠減速｜💎割安｜FAIL_UWAHIGE｜1,498円｜💰15.1万円｜—｜⚠日程不明
- 6479 ミネベア｜choruko_reversal｜⚠減速｜💎割安｜FAIL_INSEN｜3,118円｜💰32.2万円｜—｜⏰決算 11/06(残4営業日)
- 1893 Penta-Ocean Construction Co., Ltd.｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜1,354円｜💰13.8万円｜—｜⏰決算 11/09(残5営業日)
- 6183 BELLSYSTEM24 Holdings, Inc.｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜1,344円｜💰13.4万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 01/29 第2回/8）
- 6753 Sharp Corporation｜choruko_reversal｜🔻悪化｜⚪妥当｜FAIL_INSEN｜539円｜💰5.7万円｜—｜⏰決算 11/09(残5営業日)
- 8276 HEIWADO CO., LTD.｜choruko_reversal｜⚠減速｜⚪妥当｜PASS｜2,597円｜💰26.0万円｜reversal 2,597（✅即時可）｜⚠日程不明｜⚠業績基調が下向き（⚠減速）
  > 【業態】滋賀地盤のスーパー。大型店が主力。ドミナント戦略で拡大。中国に百貨店進出。
  > 【いま】終値2,597円・直近5日+0.08%（材料未確認）
  > 【調子】⚠減速（1/13）
  > 【水準】⚪妥当（3.0/7）— PER13.10倍・PEG3.2163・52週26.1% ／ 💰単元26.0万円
  > 【戦略】当日終値2,597円の指値で反転を取りにいく。SL2,523円（直近5日安値）
- 9974 BELC Co., Ltd.｜choruko_reversal｜⚠減速｜⚪妥当｜PASS｜6,500円｜💰65.0万円｜reversal 6,500（✅即時可）｜⚠日程不明｜⚠業績基調が下向き（⚠減速）
  > 【業態】埼玉地盤に食品スーパー「ベルク」を展開。自社物流などに強み。イオンと提携。
  > 【いま】終値6,500円・直近5日+1.88%（材料未確認）
  > 【調子】⚠減速（1/13） — 質注意
  > 【水準】⚪妥当（3.0/7）— PER13.68倍・PEG—・52週23.8% ／ 💰単元65.0万円
  > 【戦略】当日終値6,500円の指値で反転を取りにいく。SL6,260円（直近5日安値）
- 3234 Mori Hills Reit Investment Corporation｜choruko_reversal｜⚠減速｜🔴過熱｜FAIL_INSEN｜115,200円｜💰11.9万円｜—｜⚠日程不明
- 3249 Industrial & Infrastructure Fund Investment Corporation｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_UWAHIGE｜128,100円｜💰12.9万円｜—｜⚠日程不明
- 3283 Nippon Prologis REIT, Inc.｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_UWAHIGE｜81,100円｜💰8.2万円｜—｜⚠日程不明
- 3292 AEON REIT Investment Corp.｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_UWAHIGE｜103,800円｜💰10.6万円｜—｜⚠日程不明
- 3296 NIPPON REIT Investment Corp｜choruko_reversal｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜74,100円｜💰7.6万円｜—｜⚠日程不明
- 3309 Sekisui House Reit. Inc.｜choruko_reversal｜⚠減速｜🟡やや割高｜PASS｜64,800円｜💰6.5万円｜⛔提案なし(材料後出し)｜⚠日程不明｜⚡材料後出し｜⚠業績基調が下向き（⚠減速）｜📌
  > 【業態】3大都市圏のオフィスビル、住居を核に総合投資。運用:積水ハウス・アセットマネジメント。
  > 【いま】終値64,800円・直近5日-4.14%・📌GRESBリアルエステイト評価における「アジア・セクターリーダー」選出に関するお知らせ
  > 【調子】⚠減速（1/13） — 前年同期比（半期決算等・期間が12か月でない）／E軸判定不能(進捗データ不足)／減収でleverage参考値／質注意／D軸判定不能(四半期データ不足・中立1点)
  > 【水準】🟡やや割高（2.8/7）— PER34.54倍・PEG—・52週2.2% ／ 💰単元6.5万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 3462 Nomura Real Estate Master Fund, Inc.｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_UWAHIGE｜125,600円｜💰12.9万円｜—｜⚠日程不明
- 5482 Aichi Steel Corporation｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜2,338円｜💰28.5万円｜—｜📌
- 8953 Japan Metropolitan Fund Investment Corporation｜choruko_reversal｜🔻悪化｜🟡やや割高｜FAIL_UWAHIGE｜105,500円｜💰10.7万円｜—｜⚠日程不明
- 8954 ORIX JREIT Inc.｜choruko_reversal｜⚠減速｜🟡やや割高｜PASS｜86,800円｜💰8.7万円｜reversal 86,800（✅即時可）｜⚠日程不明｜⚠業績基調が下向き（⚠減速）
  > 【業態】オリックス系の不動産投資。オフィス過半、物流、商業施設、住宅、ホテルなど総合投資。
  > 【いま】終値86,800円・直近5日-2.14%（材料未確認）
  > 【調子】⚠減速（1/13） — 質注意／A成長率0以下のためレバレッジ計算不可(C=0)／D軸判定不能(四半期データ不足・中立1点)／E軸判定不能(進捗データ不足)／減収／経常減益-10.8%
  > 【水準】🟡やや割高（2.8/7）— PER37.32倍・PEG—・52週5.9% ／ 💰単元8.7万円
  > 【戦略】当日終値86,800円の指値で反転を取りにいく。SL85,400円（直近5日安値）
- 8955 Japan Prime Realty Investment Corporation｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_UWAHIGE｜91,100円｜💰9.3万円｜—｜⚠日程不明
- 8961 MORI TRUST REIT.Inc｜choruko_reversal｜⚠減速｜🔴過熱｜FAIL_INSEN｜65,900円｜💰6.7万円｜—｜⚠日程不明
- 8986 Daiwa Securities Living Investment Corporation｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜81,000円｜💰8.3万円｜—｜📋カルテ窓 11/19(残13営業日)
- 1946 Toenec Corporation｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜1,795円｜💰21.1万円｜—
- 2815 ARIAKE JAPAN Co., Ltd.｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_UWAHIGE｜5,160円｜💰51.2万円｜—｜⏰決算 11/06(残4営業日)
- 4980 Dexerials Corp.｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜2,895.5円｜💰29.7万円｜—
- 5631 Japan Steel Works, Ltd.｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜5,885円｜💰61.0万円｜—
- 9948 Arcs Company, Limited｜choruko_reversal｜⚠減速｜🟡やや割高｜PASS｜3,535円｜💰35.4万円｜reversal 3,535（✅即時可）｜⚠日程不明｜⚠業績基調が下向き（⚠減速）
  > 【業態】北海道最大の食品スーパー。青森、岩手も首位。ローコスト経営に強み。M&A積極。
  > 【いま】終値3,535円・直近5日+2.02%（材料未確認）
  > 【調子】⚠減速（1/13）
  > 【水準】🟡やや割高（2.0/7）— PER15.19倍・PEG6.6305・52週47.4% ／ 💰単元35.4万円
  > 【戦略】当日終値3,535円の指値で反転を取りにいく。SL3,405円（直近5日安値）
- 1963 日揮ホールディングス｜choruko_reversal｜🔻悪化｜🔴過熱｜FAIL_INSEN｜2,114円｜💰21.5万円｜—
- 3105 日清紡ホールディングス｜choruko_reversal｜🔻悪化｜🔴過熱｜FAIL_INSEN｜2,244円｜💰23.8万円｜—
- 4928 Noevir Holdings Co., Ltd.｜choruko_reversal｜⚠減速｜🔴過熱｜FAIL_UWAHIGE｜4,565円｜💰46.7万円｜—
- 5310 Toyo Tanso Co., Ltd.｜choruko_reversal/ai_reversal｜🔻悪化｜🔴過熱｜FAIL_INSEN｜6,490円｜💰68.1万円｜—｜⏰決算 11/09(残5営業日)
- 9436 Okinawa Cellular Telephone Company｜choruko_reversal｜⚠減速｜🔴過熱｜PASS｜3,425円｜💰34.2万円｜⛔提案なし(指名鮮度切れ 12営業日)｜⚠日程不明｜⚠業績基調が下向き（⚠減速）
  > 【業態】KDDIと沖縄経済界の共同出資による携帯サービス会社。県内携帯シェア首位。
  > 【いま】終値3,425円・直近5日+2.70%（材料未確認）
  > 【調子】⚠減速（1/13） — E軸判定不能(進捗データ不足)
  > 【水準】🔴過熱（1.0/7）— PER23.62倍・PEG10.2197・52週45.6% ／ 💰単元34.2万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 12営業日)）
- 6960 Fukuda Denshi Co., Ltd.｜choruko_reversal｜⚠減速｜🔴過熱｜PASS｜11,410円｜💰114.1万円｜⛔提案なし(材料後出し)｜📉決算反応日 11/02｜⚡材料後出し｜⚠業績基調が下向き（⚠減速）｜📊
  > 【業態】医療用電子機器メーカー。心電計で首位。循環器系に強み。フィリップス等と提携。
  > 【いま】終値11,410円・直近5日+7.34%・📊2027年３月期 第２四半期（中間期）決算短信〔日本基準〕（連結）
  > 【調子】⚠減速（1/13） — 質注意
  > 【水準】🔴過熱（0.0/7）— PER17.42倍・PEG—・52週81.7% ／ 💰単元114.1万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 1662 Japan Petroleum Exploration Co., Ltd.｜choruko_reversal｜🔻悪化｜⚪妥当｜FAIL_UWAHIGE｜1,747円｜💰17.5万円｜—
- 6804 Hosiden Corp.｜choruko_reversal｜🔻悪化｜⚪妥当｜FAIL_INSEN｜2,290円｜💰23.2万円｜—
- 1969 高砂熱学工業｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜3,992円｜💰41.7万円｜—｜⚠日程不明
- 8585 Orient Corporation｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_UWAHIGE｜767円｜💰7.6万円｜—｜📉決算反応日 11/02｜⚡材料後出し｜📊
- 8194 Life Corporation｜choruko_reversal｜⚠減速｜🟡やや割高｜PASS｜2,470円｜💰24.7万円｜reversal 2,470（✅即時可）｜⚠日程不明｜⚠業績基調が下向き（⚠減速）
  > 【業態】食品スーパー大手。首都圏・近畿地方で積極的に展開。三菱商事の持分法。
  > 【いま】終値2,470円・直近5日+1.44%（材料未確認）
  > 【調子】⚠減速（0/13）
  > 【水準】🟡やや割高（2.8/7）— PER11.25倍・PEG3.2667・52週33.3% ／ 💰単元24.7万円
  > 【戦略】当日終値2,470円の指値で反転を取りにいく。SL2,406円（直近5日安値）
- 9699 NISHIO HOLDINGS CO. LTD.｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜4,270円｜💰43.0万円｜—
- 3612 WORLD CO.,LTD.｜choruko_reversal｜業績データ取得不可｜💎割安｜FAIL_UWAHIGE｜1,422円｜💰15.3万円｜—｜📌
- 8253 Credit Saison Co., Ltd.｜choruko_reversal｜取得不可｜🟢値頃｜FAIL_UWAHIGE｜4,139円｜💰41.2万円｜—
- 5831 Shizuoka Financial Group, Inc.｜choruko_reversal/granville_rebound｜取得不可｜🟢値頃｜FAIL_INSEN｜3,062円｜💰31.2万円｜—
- 7381 ＣＣＩグループ｜choruko_reversal/granville_rebound｜取得不可｜🟢値頃｜FAIL_UWAHIGE｜1,130円｜💰11.3万円｜—｜📉決算反応日 11/02｜📊
- 8345 Bank of Iwate Ltd.｜choruko_reversal｜業績データ取得不可(売上/経常欠損)｜🟢値頃｜FAIL_UWAHIGE｜2,188円｜💰21.9万円｜—
- 8367 南都銀行｜granville_oshime/choruko_reversal｜取得不可｜🟢値頃｜FAIL_UWAHIGE｜1,785円｜💰18.0万円｜—
- 8370 紀陽銀行｜choruko_reversal｜取得不可｜🟢値頃｜FAIL_INSEN｜1,580円｜💰16.2万円｜—｜⏰決算 11/09(残5営業日)
- 3471 Mitsui Fudosan Logistics Park, Inc.｜choruko_reversal｜判定保留(変則決算)｜⚪妥当｜FAIL_INSEN｜96,900円｜💰9.9万円｜—｜⚠日程不明｜⚡材料後出し｜📌
- 7384 Procrea Holdings,Inc.｜granville_rebound/choruko_reversal｜業績データ取得不可(売上/経常欠損)｜⚪妥当｜FAIL_UWAHIGE｜4,280円｜💰42.1万円｜—｜⚠日程不明｜⚡材料後出し｜📌
- 8174 NIPPON GAS Co., Ltd.｜choruko_reversal｜業績データ取得不可｜⚪妥当｜FAIL_INSEN｜866.1円｜💰9.4万円｜—
- 8304 あおぞら銀行｜choruko_reversal｜取得不可｜⚪妥当｜FAIL_INSEN｜3,015円｜💰30.5万円｜—
- 8334 Gunma Bank, Ltd.｜granville_rebound/choruko_reversal｜取得不可｜⚪妥当｜FAIL_INSEN｜2,605円｜💰26.4万円｜—｜⏰決算 11/09(残5営業日)
- 8366 滋賀銀行｜granville_rebound/choruko_reversal｜取得不可｜⚪妥当｜FAIL_INSEN｜2,483.5円｜💰26.0万円｜—
- 6810 Maxell, Ltd.｜granville_oshime/choruko_reversal/granville_rebound｜取得不可｜⚪妥当｜PASS｜2,265円｜💰22.6万円｜reversal 2,265（✅即時可）｜⚠日程不明｜🎯2手法一致
  > 【業態】電池や産業用部材が主力。車載、理美容家電向け注力。全固体電池量産化。
  > 【いま】終値2,265円・直近5日-8.30%（材料未確認）
  > 【調子】欠損
  > 【水準】⚪妥当（3.5/7）— PER12.47倍・PEG—・52週47.6% ／ 💰単元22.6万円
  > 【戦略】当日終値2,265円の指値で反転を取りにいく。SL2,150円（直近5日安値）
- 7201 Nissan Motor Co., Ltd.｜choruko_reversal｜業績データ取得不可(経常益予想非開示)｜⚪妥当｜FAIL_INSEN｜266.7円｜💰2.7万円｜—
- 3591 WACOAL HOLDINGS CORP｜choruko_reversal｜🔻悪化｜🟡やや割高｜FAIL_UWAHIGE｜3,615円｜💰36.3万円｜—
- 4021 Nissan Chemical Corporation｜choruko_reversal｜—｜—｜FAIL_INSEN｜7,803円｜💰—｜—｜⏰決算 11/09(残5営業日)
- 4205 Zeon Corporation｜choruko_reversal｜—｜—｜FAIL_INSEN｜2,127円｜💰—｜—｜⚠日程不明
- 4216 ASAHI YUKIZAI CORPORATION｜choruko_reversal｜—｜—｜FAIL_INSEN｜6,240円｜💰—｜—｜📉決算反応日 11/02｜⚡材料後出し｜📊
- 6349 Komori Corporation｜choruko_reversal｜—｜—｜FAIL_INSEN｜1,738円｜💰—｜—｜⚠日程不明
- 6471 日本精工｜choruko_reversal｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜1,002.5円｜💰10.1万円｜—｜⚠日程不明
- 6651 NITTO KOGYO Corporation｜choruko_reversal｜—｜—｜FAIL_INSEN｜4,125円｜💰—｜—｜⏰決算 11/09(残5営業日)
- 6652 IDEC Corporation｜choruko_reversal｜—｜—｜FAIL_INSEN｜3,370円｜💰—｜—｜⏰決算 11/06(残4営業日)
- 6923 Stanley Electric Co., Ltd.｜choruko_reversal｜—｜—｜FAIL_INSEN｜3,169円｜💰—｜—｜⚠日程不明
- 7148 Financial Products Group Co., Ltd.｜choruko_reversal｜—｜—｜FAIL_INSEN｜1,400円｜💰—｜—｜⚠日程不明｜⚡材料後出し｜📌
- 7186 横浜フィナンシャルグループ｜choruko_reversal｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜1,677円｜💰17.0万円｜—
- 7322 三十三フィナンシャルグループ｜choruko_reversal/granville_rebound｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜1,879円｜💰19.0万円｜—
- 7995 Valqua Ltd.｜choruko_reversal｜—｜—｜FAIL_INSEN｜6,210円｜💰—｜—｜⏰決算 11/04(残2営業日)
- 8354 ふくおかフィナンシャルグループ｜choruko_reversal｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜6,955円｜💰70.5万円｜—
- 8359 Hachijuni Nagano Bank, Ltd.｜choruko_reversal/granville_rebound｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜2,445.5円｜💰24.6万円｜—｜⏰決算 11/06(残4営業日)
- 8600 トモニホールディングス｜choruko_reversal｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜1,050円｜💰10.6万円｜—｜📌
- 8616 Tokai Tokyo Financial Holdings, Inc.｜choruko_reversal｜—｜—｜FAIL_INSEN｜791円｜💰—｜—｜📉決算反応日 11/02｜📊
- 8628 Matsui Securities Co., Ltd.｜granville_oshime/choruko_reversal｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜1,015円｜💰10.6万円｜—
- 8698 Monex Group, Inc.｜choruko_reversal｜—｜—｜FAIL_INSEN｜620円｜💰—｜—｜⏰決算 11/09(残5営業日)
- 8975 Ichigo Office REIT Investment Corporation｜choruko_reversal｜—｜—｜FAIL_UWAHIGE｜81,900円｜💰—｜—｜⚠日程不明
- 7624 NaITO｜stf_kakuhen｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜159円｜💰1.6万円｜—｜⚠日程不明
- 7713 シグマ光機｜stf_kakuhen｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜3,010円｜💰32.1万円｜—｜⚠日程不明
- 5018 ＭＯＲＥＳＣＯ｜stf_kakuhen｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜2,730円｜💰28.9万円｜—｜⚠日程不明
- 5246 ＥＬＥＭＥＮＴＳ｜granville_oshime/stf_kakuhen｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜1,046円｜💰11.0万円｜—｜⚠日程不明
- 6668 ＡＤプラズマ｜stf_kakuhen/granville_oshime｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜4,515円｜💰52.8万円｜—｜⚠日程不明
- 3498 霞ヶ関Ｃ｜stf_kakuhen｜🔥絶好調｜💎割安｜FAIL_INSEN｜7,330円｜💰73.1万円｜—｜⚠日程不明
- 3994 マネーフォワード｜stf_kakuhen｜🔥絶好調｜🔴過熱｜PASS｜6,855円｜💰68.5万円｜⛔提案なし(手法ブランチ不明)｜⚠日程不明｜⚠織り込み済みの可能性（押し目待ち推奨圏）
  > 【業態】クラウド会計中心の法人向けバックオフィスSaaS事業が柱。個人向け家計簿アプリも。
  > 【いま】終値6,855円・直近5日+1.60%（材料未確認）
  > 【調子】🔥絶好調（9/13） — E軸判定不能(進捗データ不足)／赤字企業(経常赤字)
  > 【水準】🔴過熱（1.4/7）— PER—倍・PEG—・52週94.3% ／ 💰単元68.5万円
  > 【戦略】発注対象外（⛔提案なし(手法ブランチ不明)）
- 7811 中本パックス｜granville_oshime/stf_kakuhen｜🔥絶好調｜💎割安｜PASS_DOJI｜2,446円｜💰24.5万円｜⛔提案なし(手法ブランチ不明)｜⚠日程不明｜📐進捗 上振れ +21.8%
  > 【業態】グラビア印刷やドライラミネート加工などコーティング事業。食品包装、医療関連など。
  > 【いま】終値2,446円・直近5日-7.87%（材料未確認）
  > 【調子】🔥絶好調（8/13）
  > 【水準】💎割安（6.0/7）— PER8.44倍・PEG0.2726・52週73.7% ／ 💰単元24.5万円
  > 【戦略】発注対象外（⛔提案なし(手法ブランチ不明)）
- 4443 Ｓａｎｓａｎ｜changepoint/stf_kakuhen/changepoint🔔🔔｜🔥絶好調｜⚪妥当｜PASS｜2,183円｜💰21.8万円｜⛔提案なし(手法ブランチ不明)｜⚠日程不明
  > 【業態】名刺管理サービス最大手。法人向けクラウド、個人向けアプリ展開。請求書データも。
  > 【いま】終値2,183円・直近5日+3.07%（材料未確認）
  > 【調子】🔥絶好調（8/13） — E軸判定不能(進捗データ不足)
  > 【水準】⚪妥当（3.0/7）— PER29.46倍・PEG0.4458・52週87.4% ／ 💰単元21.8万円
  > 【戦略】発注対象外（⛔提案なし(手法ブランチ不明)）
- 6814 古野電｜stf_kakuhen｜⚡好調｜🟢値頃｜PASS｜7,810円｜💰78.1万円｜⛔提案なし(手法ブランチ不明)｜⚠日程不明
  > 【業態】魚群探知機など船舶用電子機器で世界高シェア。GPSや医療機器も積極展開。
  > 【いま】終値7,810円・直近5日+3.44%（材料未確認）
  > 【調子】⚡好調（7/13） — 上方修正済み
  > 【水準】🟢値頃（5.0/7）— PER14.52倍・PEG0.7162・52週54.8% ／ 💰単元78.1万円
  > 【戦略】発注対象外（⛔提案なし(手法ブランチ不明)）
- 5932 三協立山｜stf_kakuhen｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜740円｜💰7.3万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 01/29 第2回/8）
- 3091 ブロンコビリー｜changepoint/changepoint🔔🔔/stf_kakuhen｜⚡好調｜🟡やや割高｜FAIL_INSEN｜3,015円｜💰31.2万円｜—｜⚠日程不明
- 3479 ＴＫＰ｜stf_kakuhen/granville_tenkan｜⚡好調｜🔴過熱｜FAIL_UWAHIGE｜1,947円｜💰19.5万円｜—｜⚠日程不明
- 6505 東洋電機製造｜ai_momentum/stf_kakuhen｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,912円｜💰30.2万円｜—｜⚠日程不明
- 6532 ベイカレント｜stf_kakuhen｜⚡好調｜🟡やや割高｜FAIL_INSEN｜11,825円｜💰116.3万円｜—｜⚠日程不明
- 4176 ココナラ｜stf_kakuhen｜✅順調｜🟢値頃｜FAIL_INSEN｜289円｜💰3.0万円｜—｜⚠日程不明
- 3496 アズーム｜(前夜提案のみ)｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜4,850円｜💰48.0万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 9064 ヤマトホールディングス｜(前夜提案のみ)｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜1,969.5円｜💰19.6万円｜—｜⏰決算 11/04(残2営業日)

## グランビル銘柄
- 5254 Arent, Inc.｜granville_tenkan｜🚀確変｜⚪妥当｜FAIL_INSEN｜3,770円｜💰38.7万円｜—
- 3927 アークン｜granville_tenkan｜🚀確変｜💎割安｜PASS_DOJI｜937円｜💰9.4万円｜momentum 967（✅即時可）
  > 【業態】情報セキュリティ製品の開発・販売・保守。中小企業向けの業務システムに注力。
  > 【いま】終値937円・直近5日-5.07%（材料未確認）
  > 【調子】🚀確変（11/13） — 進捗モデル値域外
  > 【水準】💎割安（6.0/7）— PER15.24倍・PEG0.1453・52週30.1% ／ 💰単元9.4万円
  > 【戦略】当日高値超えの逆指値967円で順張り参戦を検討。上限976.7円・SL908円目安
- 8944 Land Business Co., Ltd.｜granville_tenkan｜🔥絶好調｜💎割安｜FAIL_UWAHIGE｜253円｜💰2.5万円｜—
- 6905 Cosel Co., Ltd.｜granville_tenkan｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1,251円｜💰12.9万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 01/29 第2回/8）
- 9553 MicroAd, Inc.｜granville_tenkan｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜565円｜💰5.9万円｜—
- 7725 INTER ACTION Corporation｜granville_tenkan｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜1,801円｜💰17.9万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 01/29 第2回/8）
- 2986 LA Holdings Co.,Ltd｜granville_tenkan｜🔥絶好調｜💎割安｜FAIL_INSEN｜2,662円｜💰27.0万円｜—
- 9211 f-code Inc.｜changepoint/granville_tenkan/changepoint🔔｜🔥絶好調｜💎割安｜FAIL_INSEN｜1,148円｜💰11.8万円｜—
- 6562 Geniee, Inc.｜granville_tenkan｜🔥絶好調｜💎割安｜FAIL_INSEN｜899円｜💰9.1万円｜—｜⚡材料後出し｜📌
- 6473 JTEKT Corporation｜granville_tenkan｜⚠減速｜🟢値頃｜FAIL_INSEN｜1,982円｜💰20.5万円｜—
- 8697 日本取引所グループ｜granville_tenkan/changepoint🔔/changepoint｜🔥絶好調｜⚪妥当｜PASS｜2,116.5円｜💰21.2万円｜momentum 2,118（✅即時可）｜⚠日程不明｜📐進捗 上振れ +24.0%
  > 【業態】総合取引所。現物は東証、デリバティブは大証に集約。東京商品取引所統合。
  > 【いま】終値2,116.5円・直近5日-4.60%（材料未確認）
  > 【調子】🔥絶好調（8/13） — E軸:進捗54.6%>=前年同期44.0%
  > 【水準】⚪妥当（4.0/7）— PER20.53倍・PEG0.6064・52週67.8% ／ 💰単元21.2万円
  > 【戦略】当日高値超えの逆指値2,118円で順張り参戦を検討。上限2,139.2円・SL1,990円目安
- 9742 アイネス｜granville_tenkan｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜2,369円｜💰22.8万円｜—｜📉決算反応日 11/02｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚡材料後出し｜📊
- 4534 Mochida Pharmaceutical Co., Ltd.｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜3,285円｜💰32.5万円｜—｜⏰決算 11/09(残5営業日)
- 6255 NPC Incorporated｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_INSEN｜673円｜💰6.5万円｜—｜⚠日程不明
- 3405 クラレ｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜1,847円｜💰18.5万円｜—
- 7744 ノーリツ鋼機｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,067円｜💰21.5万円｜—
- 8095 Astena Holdings Co.,Ltd.｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜559円｜💰5.5万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 01/29 第2回/8）
- 3741 Systems Engineering Consultants Co., Ltd.｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,990円｜💰30.5万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 4544 H.U.Group Holdings, Inc.｜granville_tenkan｜⚡好調｜⚪妥当｜PASS｜3,936円｜💰39.4万円｜⛔提案なし(指名鮮度切れ 15営業日)
  > 【業態】臨床検査薬大手・富士レビオと臨床検査・SRLが統合。ヘルス関連サービス事業も。
  > 【いま】終値3,936円・直近5日+5.35%（材料未確認）
  > 【調子】⚡好調（7/13） — E軸判定不能(進捗データ不足)
  > 【水準】⚪妥当（3.0/7）— PER42.55倍・PEG0.2334・52週98.2% ／ 💰単元39.4万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 15営業日)）
- 7970 Shin-Etsu Polymer Co., Ltd.｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,536円｜💰25.6万円｜—｜⚠日程不明
- 5838 Rakuten Bank, Ltd.｜granville_tenkan｜⚡好調｜💎割安｜FAIL_INSEN｜5,919円｜💰60.6万円｜—
- 6470 Taiho Kogyo Co., Ltd.｜granville_tenkan｜⚡好調｜💎割安｜FAIL_INSEN｜1,069円｜💰11.0万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 4763 クリーク・アンド・リバー社｜granville_tenkan｜⚡好調｜🟢値頃｜PASS｜1,507円｜💰15.1万円｜momentum 1,509（✅即時可）｜⚠日程不明｜📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】映像・ゲーム分野の派遣と制作主力。メタバース・NFT分野注力。医療職等派遣も。
  > 【いま】終値1,507円・直近5日+1.41%（材料未確認）
  > 【調子】⚡好調（6/13）
  > 【水準】🟢値頃（5.0/7）— PER8.99倍・PEG0.599・52週72.4% ／ 💰単元15.1万円
  > 【戦略】当日高値超えの逆指値1,509円で順張り参戦を検討。上限1,524.1円・SL1,417.5円目安
- 4568 第一三共｜granville_tenkan｜⚡好調｜⚪妥当｜PASS｜2,754円｜💰27.5万円｜momentum 2,758（✅即時可）｜📉決算反応日 11/02｜📐進捗 遅れ -18.0%｜📊
  > 【業態】国内製薬大手。循環器と感染症に強み。がん新薬で英アストラゼネカと提携。
  > 【いま】終値2,754円・直近5日-2.25%・📊2027年3月期 第2四半期（中間期）決算短信〔IFRS〕（連結）
  > 【調子】⚡好調（6/13）
  > 【水準】⚪妥当（4.0/7）— PER19.97倍・PEG1.4034・52週23.4% ／ 💰単元27.5万円
  > 【戦略】当日高値超えの逆指値2,758円で順張り参戦を検討。上限2,785.6円・SL2,591.6円目安
- 7199 プレミアグループ｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜2,273円｜💰22.5万円｜—
- 4848 Fullcast Holdings Co., Ltd.｜granville_tenkan｜⚡好調｜⚪妥当｜PASS｜1,854円｜💰18.5万円｜momentum 1,862（✅即時可）｜⏰決算 11/06(残4営業日)｜📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】日雇い派遣からアルバイト紹介・給与管理代行に転換。警備請負、ラーメンチェーンも。
  > 【いま】終値1,854円・直近5日-1.49%（材料未確認）
  > 【調子】⚡好調（6/13） — 質注意
  > 【水準】⚪妥当（3.0/7）— PER11.88倍・PEG0.9225・52週81.6% ／ 💰単元18.5万円
  > 【戦略】当日高値超えの逆指値1,862円で順張り参戦を検討。上限1,880.6円・SL1,749.3円目安
- 3935 Edia Co. Ltd.｜granville_tenkan｜⚡好調｜💎割安｜FAIL_INSEN｜688円｜💰7.0万円｜—｜⚠日程不明
- 6196 Strike Group Co. Ltd.｜granville_tenkan｜⚡好調｜💎割安｜FAIL_UWAHIGE｜1,413円｜💰14.0万円｜—｜📉決算反応日 11/02｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚡材料後出し｜📊
- 6768 Tamura Corporation｜granville_tenkan/granville_oshime｜⚡好調｜🟢値頃｜FAIL_INSEN｜809円｜💰8.8万円｜—｜⏰決算 11/09(残5営業日)｜📌
- 3562 No.1 Co., Ltd.｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜1,590円｜💰16.7万円｜—｜⚠日程不明
- 8061 Seika Corporation｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_INSEN｜2,979円｜💰29.8万円｜—｜⚡材料後出し｜📌
- 4169 Enechange Ltd.｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜266円｜💰2.7万円｜—｜⏰決算 11/06(残4営業日)
- 3661 m-up holdings, Inc.｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜874円｜💰8.9万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 6432 竹内製作所｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜7,640円｜💰77.8万円｜—｜⚠日程不明
- 6988 日東電工｜granville_tenkan｜⚡好調｜🟡やや割高｜FAIL_INSEN｜3,392円｜💰34.2万円｜—｜⚠日程不明
- 7747 朝日インテック｜granville_tenkan｜⚡好調｜🟡やや割高｜FAIL_UWAHIGE｜3,668円｜💰36.4万円｜—
- 8020 Kanematsu Corporation｜granville_tenkan｜⚡好調｜🟡やや割高｜FAIL_INSEN｜2,306.5円｜💰23.8万円｜—｜⏰決算 11/05(残3営業日)｜⚡材料後出し｜📌
- 8014 Chori Co., Ltd.｜granville_tenkan｜✅順調｜⚪妥当｜FAIL_INSEN｜4,220円｜💰42.9万円｜—｜📉決算反応日 11/02｜📑TOPIX低減対象（次 01/29 第2回/8）｜📊
- 3549 クスリのアオキホールディングス｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_UWAHIGE｜4,373円｜💰42.5万円｜—｜⚠日程不明
- 4549 Eiken Chemical Co., Ltd.｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_UWAHIGE｜2,307円｜💰24.2万円｜—｜📌
- 3092 ＺＯＺＯ｜granville_tenkan｜✅順調｜🔴過熱｜FAIL_INSEN｜1,160.5円｜💰11.7万円｜—
- 5184 ニチリン｜granville_tenkan｜✅順調｜🔴過熱｜FAIL_INSEN｜4,170円｜💰41.8万円｜—
- 6371 Tsubakimoto Chain Co.｜granville_tenkan｜✅順調｜🔴過熱｜FAIL_INSEN｜2,665円｜💰27.1万円｜—｜📉決算反応日 11/02｜⚡材料後出し｜📊
- 6592 Mabuchi Motor Co., Ltd.｜granville_tenkan｜✅順調｜🔴過熱｜FAIL_INSEN｜1,710円｜💰17.5万円｜—｜🚨決算直前 11/02(残1営業日)
- 8113 Unicharm Corporation｜granville_tenkan｜✅順調｜🔴過熱｜PASS｜1,012円｜💰10.1万円｜momentum 1,013（✅即時可）｜⏰決算 11/06(残4営業日)
  > 【業態】衛生用品大手。生理用品、紙おむつで首位。ペットケア用品も。アジアに強み。
  > 【いま】終値1,012円・直近5日-0.74%（材料未確認）
  > 【調子】✅順調（4/13）
  > 【水準】🔴過熱（1.0/7）— PER24.86倍・PEG3.2295・52週59.9% ／ 💰単元10.1万円
  > 【戦略】当日高値超えの逆指値1,013円で順張り参戦を検討。上限1,023.1円・SL951.3円目安
- 4166 Cacco, Inc.｜granville_tenkan｜✅順調｜🟢値頃｜FAIL_INSEN｜712円｜💰8.0万円｜—
- 8850 スターツコーポレーション｜granville_tenkan｜✅順調｜⚪妥当｜FAIL_INSEN｜4,510円｜💰46.5万円｜—｜⏰決算 11/09(残5営業日)
- 9163 Nareru Group Inc.｜granville_tenkan｜✅順調｜⚪妥当｜PASS｜2,273円｜💰22.7万円｜⛔提案なし(材料後出し)｜⚠日程不明｜⚡材料後出し｜📌
  > 【業態】建設技術者派遣、ITエンジニア派遣・システムエンジニアリングサービスなどを手掛ける。
  > 【いま】終値2,273円・直近5日-2.95%・📌2026年10月期 通期連結業績予想の修正に関するお知らせ
  > 【調子】✅順調（3/13） — 質注意／E軸判定不能(進捗データ不足)
  > 【水準】⚪妥当（4.0/7）— PER9.52倍・PEG1.443・52週51.1% ／ 💰単元22.7万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 8927 Meiho Enterprise Co., Ltd.｜granville_tenkan｜✅順調｜⚪妥当｜FAIL_INSEN｜456円｜💰4.6万円｜—｜⚠日程不明
- 186A Astroscale Holdings Inc.｜granville_tenkan｜✅順調｜🔴過熱｜FAIL_INSEN｜1,125円｜💰11.6万円｜—｜⚠日程不明
- 3569 セーレン｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_INSEN｜3,390円｜💰34.0万円｜—
- 4183 Mitsui Chemicals, Inc.｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_INSEN｜2,086円｜💰20.9万円｜—
- 4272 Nippon Kayaku Co., Ltd.｜granville_tenkan/granville_oshime｜✅順調｜🟡やや割高｜FAIL_INSEN｜2,000円｜💰20.6万円｜—
- 4956 Konishi Co., Ltd.｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_UWAHIGE｜1,530円｜💰15.2万円｜—
- 7181 JAPAN POST INSURANCE Co., Ltd.｜granville_tenkan｜⚠減速｜🔴過熱｜FAIL_UWAHIGE｜1,763.5円｜💰17.5万円｜—
- 7269 スズキ｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_INSEN｜2,095円｜💰20.4万円｜—
- 2897 Nissin Foods Holdings Co., Ltd.｜granville_tenkan｜✅順調｜🔴過熱｜PASS｜3,040円｜💰30.4万円｜momentum 3,045（✅即時可）
  > 【業態】即席麺のパイオニア。カップ麺でシェア首位。袋麺も強い。国内成熟、海外展開強化。
  > 【いま】終値3,040円・直近5日-1.78%（材料未確認）
  > 【調子】✅順調（3/13） — 営業益代替(経常非開示)／E軸判定不能(進捗データ不足)
  > 【水準】🔴過熱（1.8/7）— PER18.67倍・PEG—・52週62.0% ／ 💰単元30.4万円
  > 【戦略】当日高値超えの逆指値3,045円で順張り参戦を検討。上限3,075.4円・SL2,857.6円目安
- 5461 Chubu Steel Plate Co., Ltd.｜granville_tenkan｜🔻悪化｜🔴過熱｜FAIL_INSEN｜2,189円｜💰22.0万円｜—｜⏰決算 11/06(残4営業日)｜📑TOPIX低減対象（次 01/29 第2回/8）
- 7513 Kojima Co., Ltd.｜granville_tenkan｜✅順調｜🔴過熱｜FAIL_UWAHIGE｜1,370円｜💰13.8万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 01/29 第2回/8）
- 7734 Riken Keiki Co., Ltd.｜granville_tenkan｜✅順調｜🔴過熱｜FAIL_INSEN｜3,480円｜💰35.5万円｜—
- 8012 Nagase & Co., Ltd.｜granville_tenkan｜✅順調｜🔴過熱｜FAIL_INSEN｜1,260円｜💰12.8万円｜—｜⏰決算 11/06(残4営業日)
- 4617 中国塗料｜granville_tenkan｜➖横ばい｜⚪妥当｜FAIL_INSEN｜3,515円｜💰35.5万円｜—｜📉決算反応日 11/02｜⚡材料後出し｜📊
- 5233 太平洋セメント｜granville_tenkan｜➖横ばい｜⚪妥当｜PASS｜4,231円｜💰42.3万円｜momentum 4,239（✅即時可）｜📐進捗 上振れ +32.1%
  > 【業態】セメント最大手。海外にも展開。建材や電材など多角化。産廃・再資源化も。
  > 【いま】終値4,231円・直近5日+2.59%（材料未確認）
  > 【調子】➖横ばい（2/13） — E軸:進捗17.6%>=前年同期13.3%／経常減益-6.8%／質注意
  > 【水準】⚪妥当（3.0/7）— PER7.32倍・PEG—・52週56.7% ／ 💰単元42.3万円
  > 【戦略】当日高値超えの逆指値4,239円で順張り参戦を検討。上限4,281.4円・SL3,980円目安
- 6328 Ebara Jitsugyo Co., Ltd.｜granville_tenkan｜➖横ばい｜⚪妥当｜FAIL_INSEN｜2,436円｜💰24.7万円｜—｜⏰決算 11/05(残3営業日)｜📑TOPIX低減対象（次 01/29 第2回/8）
- 9837 Morito Co., Ltd.｜granville_tenkan｜➖横ばい｜⚪妥当｜FAIL_UWAHIGE｜1,811円｜💰18.0万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 01/29 第2回/8）
- 4552 JCR Pharmaceuticals Co., Ltd.｜granville_tenkan｜🔻悪化｜🔴過熱｜FAIL_UWAHIGE｜544円｜💰5.1万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 6208 Ishikawa Seisakusho,Ltd.｜granville_tenkan｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜1,620円｜💰16.6万円｜—｜⏰決算 11/09(残5営業日)
- 8081 Kanaden Corporation｜granville_tenkan｜➖横ばい｜🟡やや割高｜FAIL_INSEN｜2,515円｜💰26.0万円｜—｜⏰決算 11/04(残2営業日)｜📑TOPIX低減対象（次 01/29 第2回/8）
- 2811 Kagome Co., Ltd.｜granville_tenkan｜➖横ばい｜🔴過熱｜PASS｜2,738.5円｜💰27.4万円｜momentum 2,739.5（✅即時可）｜⚠日程不明
  > 【業態】トマト加工品で首位。飲料ブランドに強み。農産品事業を育成。海外で業務用。
  > 【いま】終値2,738.5円・直近5日-1.97%（材料未確認）
  > 【調子】➖横ばい（2/13） — 営業益代替(経常非開示)／E軸判定不能(進捗データ不足)／質注意
  > 【水準】🔴過熱（1.8/7）— PER23.59倍・PEG—・52週57.3% ／ 💰単元27.4万円
  > 【戦略】当日高値超えの逆指値2,739.5円で順張り参戦を検討。上限2,766.9円・SL2,574.2円目安
- 4922 コーセーホールディングス｜granville_tenkan｜➖横ばい｜🔴過熱｜PASS｜6,014円｜💰60.1万円｜momentum 6,036（✅即時可）｜⚠1単元でリスク枠超過（37160円）
  > 【業態】化粧品大手。高級化粧品に強み。コスメタリー事業も展開。アジア・米国に進出。
  > 【いま】終値6,014円・直近5日+1.95%（材料未確認）
  > 【調子】➖横ばい（2/13） — 質注意
  > 【水準】🔴過熱（1.0/7）— PER28.21倍・PEG—・52週69.4% ／ 💰単元60.1万円
  > 【戦略】当日高値超えの逆指値6,036円で順張り参戦を検討。上限6,096.4円・SL5,664.4円目安／⚠1単元リスク37160円（枠超過）
- 6770 Alps Alpine Co., Ltd.｜granville_tenkan｜⚠減速｜⚪妥当｜FAIL_UWAHIGE｜2,085円｜💰20.8万円｜—｜📉決算反応日 11/02｜⚡材料後出し｜📊
- 5105 ＴＯＹＯ　ＴＩＲＥ｜granville_tenkan｜⚠減速｜🟡やや割高｜FAIL_UWAHIGE｜4,029円｜💰40.6万円｜—｜📋カルテ窓 11/16(残10営業日)
- 8167 リテールパートナーズ｜granville_tenkan｜⚠減速｜🟡やや割高｜PASS｜1,376円｜💰13.8万円｜momentum 1,381（✅即時可）｜⚠日程不明｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚠業績基調が下向き（⚠減速）｜📐進捗 遅れ -18.2%
  > 【業態】食品スーパー連合。山口・丸久、大分・マルミヤストア、福岡・マルキョウが経営統合。
  > 【いま】終値1,376円・直近5日-2.20%（材料未確認）
  > 【調子】⚠減速（1/13）
  > 【水準】🟡やや割高（2.0/7）— PER10.67倍・PEG5.6369・52週54.5% ／ 💰単元13.8万円
  > 【戦略】当日高値超えの逆指値1,381円で順張り参戦を検討。上限1,394.8円・SL1,297.2円目安
- 4902 Konica Minolta, Inc.｜granville_tenkan｜⚠減速｜🔴過熱｜FAIL_INSEN｜664.9円｜💰6.9万円｜—｜⏰決算 11/05(残3営業日)
- 4375 セーフィー｜changepoint/granville_tenkan/changepoint🔔｜取得不可｜💎割安｜FAIL_INSEN｜644円｜💰6.5万円｜—｜⚠日程不明
- 8424 芙蓉総合リース｜granville_tenkan｜取得不可｜💎割安｜FAIL_UWAHIGE｜4,273円｜💰43.2万円｜—｜⏰決算 11/06(残4営業日)｜⚡材料後出し｜📌
- 4005 住友化学｜granville_tenkan｜業績データ取得不可(経常益予想非開示)｜🟢値頃｜FAIL_INSEN｜565円｜💰5.7万円｜—｜🚨決算直前 11/02(残1営業日)
- 7921 ＴＡＫＡＲＡ　＆　ＣＯＭＰＡＮＹ｜granville_tenkan｜業績データ取得不可(経常益予想非開示)｜⚪妥当｜PASS｜4,185円｜💰41.9万円｜momentum 4,205（✅即時可）｜⚠日程不明｜📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】ディスクロージャー大手。有価証券報告書の作成が主力。通訳・翻訳事業が拡大。
  > 【いま】終値4,185円・直近5日-2.33%（材料未確認）
  > 【調子】業績データ欠損(経常益予想非開示)
  > 【水準】⚪妥当（3.5/7）— PER15.44倍・PEG—・52週69.7% ／ 💰単元41.9万円
  > 【戦略】当日高値超えの逆指値4,205円で順張り参戦を検討。上限4,247.1円・SL3,948円目安
- 4912 ライオン｜granville_tenkan｜業績データ取得不可(経常益予想非開示)｜🔴過熱｜PASS｜1,829.5円｜💰18.3万円｜momentum 1,838（✅即時可）｜⏰決算 11/06(残4営業日)
  > 【業態】家庭用品大手。歯磨きで国内首位級。薬品「バファリン」に強み。機能性食品も。
  > 【いま】終値1,829.5円・直近5日-0.79%（材料未確認）
  > 【調子】業績データ欠損(経常益予想非開示)
  > 【水準】🔴過熱（1.8/7）— PER20.24倍・PEG—・52週74.6% ／ 💰単元18.3万円
  > 【戦略】当日高値超えの逆指値1,838円で順張り参戦を検討。上限1,856.4円・SL1,726.8円目安
- 2871 ニチレイ｜granville_tenkan｜業績データ取得不可｜🔴過熱｜PASS｜2,148.5円｜💰21.5万円｜⛔提案なし(指名鮮度切れ 21営業日)
  > 【業態】冷蔵倉庫と冷凍食品でトップ。水産、畜産も。低温物流事業に強み。
  > 【いま】終値2,148.5円・直近5日-0.83%（材料未確認）
  > 【調子】業績データ欠損
  > 【水準】🔴過熱（1.4/7）— PER26.39倍・PEG—・52週65.4% ／ 💰単元21.5万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 21営業日)）
- 3563 ＦＯＯＤ　＆　ＬＩＦＥ　ＣＯＭＰＡＮＩＥＳ｜granville_tenkan｜判定保留(データ不足)｜🔴過熱｜PASS｜5,815円｜💰58.1万円｜momentum 5,845（✅即時可）｜⏰決算 11/06(残4営業日)｜⚠1単元でリスク枠超過（36010円）
  > 【業態】「スシロー」ブランドで回転すしチェーン首位。「京樽」を子会社化。韓国・アジアに進出。
  > 【いま】終値5,815円・直近5日-0.02%（材料未確認）
  > 【調子】判定保留(データ不足) — 売上/経常データ不足
  > 【水準】🔴過熱（0.0/7）— PER41.96倍・PEG—・52週89.4% ／ 💰単元58.1万円
  > 【戦略】当日高値超えの逆指値5,845円で順張り参戦を検討。上限5,903.4円・SL5,484.9円目安／⚠1単元リスク36010円（枠超過）
- 4045 Toagosei Co., Ltd.｜granville_tenkan｜—｜—｜FAIL_INSEN｜1,815.5円｜💰—｜—｜📉決算反応日 11/02｜📊
- 4401 ＡＤＥＫＡ｜granville_tenkan｜—｜—｜FAIL_INSEN｜4,515円｜💰—｜—
- 5532 リアルゲイト｜granville_tenkan｜—｜—｜FAIL_UWAHIGE｜3,555円｜💰—｜—｜⚠日程不明
- 8160 KISOJI CO., LTD.｜granville_tenkan｜—｜—｜FAIL_UWAHIGE｜2,471円｜💰—｜—
- 9842 アークランズ｜granville_tenkan｜—｜—｜FAIL_UWAHIGE｜1,907円｜💰—｜—｜⚠日程不明
- 4937 Ｇ−ＷＡＱＯＯ｜granville_oshime｜🚀確変｜⚪妥当｜FAIL_INSEN｜2,239円｜💰23.5万円｜—
- 5243 ｎｏｔｅ｜granville_oshime/granville_rebound｜🚀確変｜⚪妥当｜FAIL_UWAHIGE｜2,850円｜💰28.8万円｜—｜⚠日程不明
- 7806 MTG Co., Ltd.｜changepoint/granville_oshime/changepoint🔔/changepoint🔔🔔｜🚀確変｜⚪妥当｜FAIL_INSEN｜8,870円｜💰92.5万円｜—
- 6834 精工技研｜granville_oshime/granville_rebound｜🔥絶好調｜💎割安｜FAIL_UWAHIGE｜6,130円｜💰61.5万円｜—
- 6080 Ｍ＆Ａキャピタルパートナーズ｜changepoint/changepoint🔔/granville_oshime｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜4,195円｜💰41.5万円｜—｜📉決算反応日 11/02｜⚡材料後出し｜📌
- 8008 Yondoshi Holdings, Inc.｜granville_oshime｜🔥絶好調｜🟢値頃｜PASS｜1,973円｜💰19.7万円｜⛔提案なし(指名鮮度切れ 15営業日)｜⚠日程不明｜📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】ジュエリーブランド「4℃」を展開。アパレル卸や革小物なども。デイリーファッションに注力。
  > 【いま】終値1,973円・直近5日-2.76%（材料未確認）
  > 【調子】🔥絶好調（9/13）
  > 【水準】🟢値頃（5.0/7）— PER16.00倍・PEG0.3526・52週53.4% ／ 💰単元19.7万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 15営業日)）
- 4382 HEROZ, Inc.｜changepoint/changepoint🔔/changepoint🔔🔔/granville_oshime｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜972円｜💰13.7万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 01/29 第2回/8）
- 3156 レスター｜granville_oshime｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜5,670円｜💰62.5万円｜—
- 8051 山善｜granville_oshime｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜1,912円｜💰19.4万円｜—
- 4180 ＡＰＰＩＥＲ　ＧＲＯＵＰ｜changepoint/changepoint🔔/granville_oshime/changepoint🔔🔔｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜1,446円｜💰14.4万円｜—
- 7856 HAGIHARA INDUSTRIES INC.｜granville_oshime｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜1,890円｜💰19.2万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 01/29 第2回/8）
- 4431 Smaregi, Inc.｜changepoint/変化点🔔🔔/changepoint🔔/granville_oshime｜🔥絶好調｜🟡やや割高｜FAIL_UWAHIGE｜3,790円｜💰38.7万円｜—｜⚠日程不明
- 1879 新日本建設｜granville_oshime｜⚡好調｜💎割安｜FAIL_INSEN｜2,139円｜💰21.5万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚡材料後出し｜📌
- 3040 ソリトンシステムズ｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜3,030円｜💰31.1万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 5892 ＹＵＴＯＲＩ｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,537円｜💰31.6万円｜—｜📌
- 6736 Suncorporation｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜10,270円｜💰100.9万円｜—
- 9902 Nichiden Corporation｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜3,070円｜💰31.8万円｜—｜⏰決算 11/05(残3営業日)｜📑TOPIX低減対象（次 01/29 第2回/8）
- 6523 ＰＨＣホールディングス｜granville_oshime｜⚠減速｜🟢値頃｜PASS｜1,415円｜💰14.2万円｜⛔型不一致: 既に支持帯以下｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚠業績基調が下向き（⚠減速）｜⚠バリュートラップ疑い
  > 【業態】各種ヘルスケア機器・サービスの開発・製造販売。糖尿病ケアに強み。ファンド傘下。
  > 【いま】終値1,415円・直近5日+10.46%（材料未確認）
  > 【調子】⚠減速（6/13） — E軸判定不能(進捗データ不足)／減収／質注意
  > 【水準】🟢値頃（5.0/7）— PER11.68倍・PEG0.0478・52週62.9% ／ 💰単元14.2万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 3106 倉敷紡績｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,307円｜💰23.8万円｜—
- 4667 Aisan Technology Co., Ltd.｜granville_oshime/changepoint🔔/changepoint｜⚡好調｜⚪妥当｜FAIL_INSEN｜920円｜💰9.6万円｜—｜⚡材料後出し｜📌
- 6250 Yamabiko Corporation｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜4,240円｜💰43.5万円｜—
- 7609 ダイトロン｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜3,995円｜💰42.5万円｜—｜⏰決算 11/04(残2営業日)
- 9304 澁澤倉庫｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,011円｜💰20.6万円｜—｜⏰決算 11/09(残5営業日)｜📑TOPIX低減対象（次 01/29 第2回/8）
- 2602 日清オイリオグループ｜granville_oshime｜⚡好調｜🟡やや割高｜FAIL_UWAHIGE｜2,064円｜💰20.5万円｜—｜⏰決算 11/09(残5営業日)
- 4413 baudroie,inc.｜granville_oshime｜⚡好調｜🟡やや割高｜FAIL_INSEN｜2,936円｜💰29.4万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 01/29 第2回/8）
- 6570 Kyowa Corporation Co. Ltd.｜granville_oshime｜⚡好調｜🟡やや割高｜FAIL_UWAHIGE｜4,190円｜💰40.5万円｜—
- 8919 カチタス｜granville_oshime｜⚡好調｜🟡やや割高｜FAIL_UWAHIGE｜3,390円｜💰33.8万円｜—｜⏰決算 11/09(残5営業日)
- 8410 Seven Bank, Ltd.｜granville_oshime｜⚡好調｜🔴過熱｜PASS｜340.1円｜💰3.4万円｜⛔型不一致: 既に支持帯以下｜⏰決算 11/06(残4営業日)｜📐進捗 上振れ +41.6%
  > 【業態】セブンイレブン店舗内などにATMを全国展開。キャッシュレス化に備え非銀行と提携。
  > 【いま】終値340.1円・直近5日+2.25%（材料未確認）
  > 【調子】⚡好調（6/13）
  > 【水準】🔴過熱（1.0/7）— PER19.89倍・PEG1.7989・52週87.8% ／ 💰単元3.4万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 7616 Colowide Co., Ltd.｜granville_oshime｜⚡好調｜🔴過熱｜FAIL_UWAHIGE｜2,234円｜💰21.6万円｜—｜⏰決算 11/06(残4営業日)
- 8392 大分銀行｜granville_rebound/granville_oshime｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜2,888円｜💰29.0万円｜—｜⏰決算 11/09(残5営業日)
- 6340 澁谷工業｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜5,260円｜💰53.7万円｜—｜⏰決算 11/09(残5営業日)
- 7350 Okinawa Financial Group, Inc.｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜7,190円｜💰71.9万円｜—
- 9536 SAIBU GAS HOLDINGS CO. LTD.｜granville_oshime｜⚡好調｜🔴過熱｜PASS｜2,794円｜💰27.9万円｜oshime 2,493.4（⏳待機: 到達まで乖離10.8%）｜📐進捗 上振れ +57.7%
  > 【業態】都市ガス大手。福岡が基盤。家庭用燃料電池販売、太陽光発電、不動産も。
  > 【いま】終値2,794円・直近5日+13.62%（材料未確認）
  > 【調子】⚡好調（5/13）
  > 【水準】🔴過熱（1.0/7）— PER12.57倍・PEG—・52週99.2% ／ 💰単元27.9万円
  > 【戦略】2,493.4円までの押し目を指値で待つ。SL2,471.3円（25日線基準）
- 4475 HENNGE K.K.｜granville_oshime｜⚡好調｜🔴過熱｜FAIL_INSEN｜2,091円｜💰23.2万円｜—｜⏰決算 11/05(残3営業日)
- 8395 佐賀銀行｜granville_oshime｜⚠減速｜⚪妥当｜FAIL_UWAHIGE｜6,500円｜💰65.0万円｜—｜⏰決算 11/06(残4営業日)
- 4373 Simplex Holdings,Inc.｜granville_oshime｜✅順調｜🟡やや割高｜FAIL_UWAHIGE｜1,166円｜💰12.6万円｜—
- 3097 Monogatari Corporation｜granville_oshime｜✅順調｜🔴過熱｜FAIL_UWAHIGE｜5,980円｜💰58.4万円｜—
- 6418 Japan Cash Machine Co., Ltd.｜granville_oshime｜✅順調｜🔴過熱｜FAIL_INSEN｜1,248円｜💰12.6万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 6998 Nippon Tungsten Co., Ltd.｜granville_oshime｜✅順調｜🔴過熱｜FAIL_INSEN｜2,907円｜💰31.6万円｜—
- 5985 SUNCALL CORPORATION｜granville_oshime｜✅順調｜🟢値頃｜FAIL_INSEN｜1,850円｜💰19.7万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 1518 三井松島ホールディングス｜granville_oshime｜✅順調｜🟡やや割高｜PASS｜2,247円｜💰22.5万円｜⛔提案なし(指名鮮度切れ 17営業日)
  > 【業態】石炭事業撤退で事業投資会社へ。生活関連事業などM&A積極で多展開。(その他製品)
  > 【いま】終値2,247円・直近5日+1.35%（材料未確認）
  > 【調子】✅順調（3/13） — 進捗判定不能(自動抽出範囲外)
  > 【水準】🟡やや割高（2.0/7）— PER9.67倍・PEG2.1094・52週86.5% ／ 💰単元22.5万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 17営業日)）
- 4208 UBE Corporation｜granville_oshime｜✅順調｜🟡やや割高｜FAIL_INSEN｜3,255円｜💰32.9万円｜—｜⏰決算 11/05(残3営業日)
- 6379 RAIZNEXT Corporation｜granville_oshime｜✅順調｜🔴過熱｜FAIL_INSEN｜1,001円｜💰10.2万円｜—
- 9044 NANKAI Co., Ltd.｜granville_oshime｜✅順調｜🟡やや割高｜PASS｜3,026円｜💰30.3万円｜⛔提案なし(指名鮮度切れ 15営業日)｜🚨決算直前 11/02(残1営業日)
  > 【業態】大阪南部と和歌山が地盤。関空関連となんば再開発が核。泉北ライナー注力。
  > 【いま】終値3,026円・直近5日+0.30%（材料未確認）
  > 【調子】✅順調（3/13） — 進捗判定不能(自動抽出範囲外)／質注意
  > 【水準】🟡やや割高（2.0/7）— PER13.75倍・PEG—・52週60.2% ／ 💰単元30.3万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 15営業日)）
- 3107 ダイワボウホールディングス｜granville_oshime｜⚠減速｜🔴過熱｜FAIL_INSEN｜3,801円｜💰38.6万円｜—
- 4044 Central Glass Co., Ltd.｜granville_oshime｜✅順調｜🔴過熱｜FAIL_INSEN｜4,435円｜💰45.1万円｜—
- 456A Human Made Inc.｜granville_oshime｜✅順調｜🔴過熱｜FAIL_UWAHIGE｜2,120円｜💰20.9万円｜—｜⚠日程不明
- 9509 Hokkaido Electric Power Company,Incorporated｜granville_oshime｜🔻悪化｜⚪妥当｜FAIL_INSEN｜1,079円｜💰11.1万円｜—｜📉決算反応日 11/02｜⚡材料後出し｜📊
- 6072 Jibannet Holdings Co., Ltd.｜granville_oshime｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜957円｜💰9.9万円｜—｜⚡材料後出し｜📌
- 7630 Ichibanya Co., Ltd.｜granville_oshime｜➖横ばい｜🔴過熱｜FAIL_INSEN｜1,057円｜💰10.5万円｜—｜⚠日程不明
- 8043 Starzen Company Limited｜granville_oshime｜➖横ばい｜🔴過熱｜PASS｜1,563円｜💰15.6万円｜⛔提案なし(指名鮮度切れ 15営業日)
  > 【業態】食肉卸最大手。生産飼育、食肉処理・加工を手掛ける。海外と協業積極。
  > 【いま】終値1,563円・直近5日-0.82%（材料未確認）
  > 【調子】➖横ばい（2/13） — E軸判定不能(進捗データ不足)
  > 【水準】🔴過熱（1.0/7）— PER10.33倍・PEG3.054・52週90.6% ／ 💰単元15.6万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 15営業日)）
- 9505 Hokuriku Electric Power Company｜granville_oshime｜🔻悪化｜🔴過熱｜FAIL_UWAHIGE｜1,079円｜💰10.8万円｜—
- 9616 共立メンテナンス｜granville_oshime｜➖横ばい｜🔴過熱｜PASS｜3,454円｜💰34.5万円｜⛔提案なし(材料後出し)｜⏰決算 11/09(残5営業日)｜⚡材料後出し｜📌
  > 【業態】サービス業
  > 【いま】終値3,454円・直近5日-0.26%・📌2026年9月度　経営情報　Monthly Report
  > 【調子】➖横ばい（2/13） — 進捗データ欠損(判定不能)／(質注意)
  > 【水準】🔴過熱（0.0/7）— PER17.45倍・PEG—・52週92.7% ／ 💰単元34.5万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 9900 Sagami Holdings Corp.｜granville_oshime｜➖横ばい｜🔴過熱｜FAIL_UWAHIGE｜1,227円｜💰11.9万円｜—｜⚡材料後出し｜📌
- 8255 Axial Retailing, Inc.｜granville_oshime｜⚠減速｜🔴過熱｜PASS｜1,346円｜💰13.5万円｜⛔提案なし(指名鮮度切れ 11営業日)｜⏰決算 11/04(残2営業日)｜⚠業績基調が下向き（⚠減速）
  > 【業態】新潟地盤の食品スーパー。群馬フレッセイを統合。袋詰めなど独自サービスに特色。
  > 【いま】終値1,346円・直近5日+2.44%（材料未確認）
  > 【調子】⚠減速（1/13） — E軸判定不能(進捗データ不足)／質注意
  > 【水準】🔴過熱（1.0/7）— PER14.61倍・PEG—・52週95.5% ／ 💰単元13.5万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 11営業日)）
- 8097 SAN-AI OBBLI CO. LTD｜granville_oshime｜⚠減速｜🔴過熱｜FAIL_INSEN｜2,439円｜💰25.0万円｜—
- 8059 Daiichi Jitsugyo Co., Ltd.｜granville_oshime｜⚠減速｜🟡やや割高｜FAIL_INSEN｜3,450円｜💰35.0万円｜—｜⏰決算 11/06(残4営業日)
- 8361 Ogaki Kyoritsu Bank, Ltd.｜granville_oshime/granville_rebound｜取得不可｜💎割安｜FAIL_UWAHIGE｜1,555円｜💰15.9万円｜—
- 9166 GENDA Inc.｜granville_oshime｜業績データ取得不可｜🟢値頃｜FAIL_INSEN｜604円｜💰6.2万円｜—｜⚠日程不明｜⚡材料後出し｜📌
- 8343 Akita Bank, Ltd.｜granville_oshime/granville_rebound｜業績データ取得不可(売上/経常欠損)｜🟢値頃｜PASS｜1,536円｜💰15.4万円｜⛔型不一致: 既に支持帯以下
  > 【業態】秋田地盤の地銀中位。預金、融資とも県内シェア５割超。福島・北海道にも。
  > 【いま】終値1,536円・直近5日+9.32%（材料未確認）
  > 【調子】業績データ欠損(売上/経常欠損)
  > 【水準】🟢値頃（5.0/7）— PER16.13倍・PEG0.9787・52週59.4% ／ 💰単元15.4万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 6027 Bengo4.com, Inc.｜granville_oshime｜業績データ取得不可｜🔴過熱｜FAIL_UWAHIGE｜4,715円｜💰46.4万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 8362 Fukui Bank, Ltd.｜granville_oshime｜🔻悪化｜🔴過熱｜FAIL_UWAHIGE｜7,200円｜💰70.7万円｜—｜📌
- 338A ZenmuTech,Inc.｜granville_oshime｜—｜—｜FAIL_INSEN｜4,265円｜💰—｜—
- 3692 ＦＦＲＩセキュリティ｜granville_oshime｜—｜—｜FAIL_INSEN｜7,700円｜💰—｜—
- 6036 ＫｅｅＰｅｒ技研｜granville_oshime｜—｜—｜FAIL_INSEN｜1,852円｜💰—｜—｜📋カルテ窓 11/16(残10営業日)｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚡材料後出し｜📌
- 8137 サンワテクノス｜granville_oshime｜—｜—｜FAIL_INSEN｜4,180円｜💰—｜—｜📉決算反応日 11/02｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚡材料後出し｜📊
- 8624 Ichiyoshi Securities Co., Ltd.｜granville_oshime/granville_rebound｜取得不可｜⏸判定不能｜FAIL_INSEN｜1,441円｜💰14.5万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 01/29 第2回/8）
- 3778 SAKURA Internet Inc.｜granville_rebound｜🚀確変｜⚪妥当｜FAIL_INSEN｜3,035円｜💰34.7万円｜—
- 6769 Thine Electronics, Inc.｜granville_rebound｜🚀確変｜⚪妥当｜FAIL_UWAHIGE｜1,008円｜💰10.2万円｜—｜⏰決算 11/05(残3営業日)
- 3691 DIGITAL PLUS, Inc.｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1,344円｜💰14.9万円｜—
- 3891 ニッポン高度紙工業｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜6,080円｜💰64.6万円｜—
- 479A PRONI Inc.｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1,700円｜💰18.2万円｜—
- 4419 Finatext Holdings Ltd.｜granville_rebound｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜1,313円｜💰15.5万円｜—
- 1436 GreenEnergy & Company｜granville_rebound｜🔥絶好調｜💎割安｜FAIL_INSEN｜1,388円｜💰14.9万円｜—｜⚠日程不明｜⚡材料後出し｜📌
- 8995 Makoto Construction Co,Ltd｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1,610円｜💰15.7万円｜—
- 6963 ROHM Company Limited｜granville_rebound｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜3,568円｜💰37.0万円｜—｜⏰決算 11/05(残3営業日)
- 150A ＪＳＨ｜granville_rebound｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜580円｜💰7.7万円｜—｜🔁
- 7715 長野計器｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜3,745円｜💰39.8万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 8364 清水銀行｜granville_rebound｜🔥絶好調｜🟢値頃｜PASS｜2,837円｜💰28.4万円｜reversal 2,837（✅即時可）｜📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】静岡地盤の地銀中下位行。地元中小企業向け中心。SBIHDと資本業務提携。
  > 【いま】終値2,837円・直近5日+10.52%（材料未確認）
  > 【調子】🔥絶好調（8/13） — E軸判定不能(進捗データ不足)
  > 【水準】🟢値頃（5.0/7）— PER11.09倍・PEG0.222・52週61.7% ／ 💰単元28.4万円
  > 【戦略】当日終値2,837円の指値で反転を取りにいく。SL2,567円（直近5日安値）
- 6490 ＰＩＬＬＡＲ｜granville_rebound｜⚡好調｜⚪妥当｜FAIL_INSEN｜9,850円｜💰103.7万円｜—
- 9697 カプコン｜granville_rebound｜⚡好調｜🟡やや割高｜PASS｜3,957円｜💰39.6万円｜reversal 3,957（✅即時可）｜⚠日程不明
  > 【業態】家庭用ゲームソフト大手。「モンハン」「戦国BASARA」等人気作品多数。SNS向け拡大。
  > 【いま】終値3,957円・直近5日-7.98%（材料未確認）
  > 【調子】⚡好調（7/13）
  > 【水準】🟡やや割高（2.0/7）— PER28.55倍・PEG2.3872・52週61.4% ／ 💰単元39.6万円
  > 【戦略】当日終値3,957円の指値で反転を取りにいく。SL3,698円（直近5日安値）
- 5242 EYEZ INC.｜granville_rebound｜⚡好調｜🔴過熱｜FAIL_INSEN｜2,765円｜💰30.0万円｜—｜⚡材料後出し｜📌
- 477A Startline CO.,LTD.｜granville_rebound｜⚡好調｜💎割安｜FAIL_UWAHIGE｜745円｜💰7.7万円｜—
- 6336 石井表記｜granville_rebound｜⚡好調｜🟢値頃｜FAIL_INSEN｜1,297円｜💰13.4万円｜—｜⚠日程不明
- 4968 Arakawa Chemical Industries,Ltd.｜granville_rebound｜⚡好調｜🟡やや割高｜FAIL_INSEN｜1,943円｜💰24.2万円｜—｜⏰決算 11/05(残3営業日)｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚡材料後出し｜📢
- 2354 YE DIGITAL CORPORATION｜granville_rebound｜⚡好調｜💎割安｜FAIL_INSEN｜987円｜💰10.4万円｜—｜⚠日程不明
- 8704 TRADERS HOLDINGS CO LTD｜changepoint/changepoint🔔/granville_rebound｜⚡好調｜💎割安｜FAIL_INSEN｜1,215円｜💰12.5万円｜—｜📉決算反応日 11/02｜⚡材料後出し｜📢
- 4100 Toda Kogyo Corp.｜granville_rebound｜⚡好調｜🟢値頃｜FAIL_INSEN｜1,706円｜💰16.1万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 8344 Yamagata Bank, Ltd.｜granville_rebound｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜4,625円｜💰45.9万円｜—
- 6597 HPC SYSTEMS Inc.｜changepoint/changepoint🔔/changepoint🔔🔔/granville_rebound｜⚡好調｜🟢値頃｜FAIL_INSEN｜2,967円｜💰31.0万円｜—｜⚡材料後出し｜📌
- 3687 Fixstars Corp.｜granville_rebound｜⚡好調｜⚪妥当｜FAIL_INSEN｜1,769円｜💰18.5万円｜—｜⏰決算 11/06(残4営業日)｜📑TOPIX低減対象（次 01/29 第2回/8）
- 9278 BOOKOFF GROUP HOLDINGS LIMITED｜granville_rebound｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜2,384円｜💰23.5万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 01/29 第2回/8）
- 5574 ABEJA,Inc.｜granville_rebound｜⚡好調｜🟡やや割高｜FAIL_INSEN｜2,220円｜💰23.6万円｜—｜⚠日程不明｜📌
- 7256 河西工業｜granville_rebound｜⚡好調｜🔴過熱｜FAIL_INSEN｜397円｜💰—｜—｜📋カルテ窓 11/16(残10営業日)
- 4997 日本農薬｜granville_rebound｜✅順調｜🟡やや割高｜FAIL_UWAHIGE｜1,066円｜💰10.7万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 278A Ｔｅｒｒａ　Ｄｒｏｎｅ｜granville_rebound｜✅順調｜⏸判定不能｜FAIL_INSEN｜6,120円｜💰—｜—｜⚠日程不明
- 4346 NEXYZ.Group Corporation｜granville_rebound｜✅順調｜🟢値頃｜FAIL_INSEN｜740円｜💰7.6万円｜—｜📋カルテ窓 11/16(残10営業日)
- 7354 Direct Marketing MiX Inc.｜granville_rebound｜✅順調｜⚪妥当｜FAIL_INSEN｜367円｜💰3.8万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 2681 2nd RETAILING Co., Ltd.｜granville_rebound｜✅順調｜⚪妥当｜PASS_DOJI｜1,900円｜💰19.0万円｜⛔提案なし(指名鮮度切れ 16営業日)｜⏰決算 11/06(残4営業日)｜📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】映像レンタル店を直営軸に全国展開。ゲーム・スマホ、衣料品の中古品販売が主力に。
  > 【いま】終値1,900円・直近5日-6.40%（材料未確認）
  > 【調子】✅順調（3/13） — E軸判定不能(進捗データ不足)／質注意
  > 【水準】⚪妥当（3.0/7）— PER12.60倍・PEG—・52週34.5% ／ 💰単元19.0万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 16営業日)）
- 4082 第一稀元素化学工業｜granville_rebound｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜1,701円｜💰17.9万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚡材料後出し｜📌
- 3653 Morpho, Inc.｜granville_rebound｜🔻悪化｜💎割安｜FAIL_INSEN｜871円｜💰9.2万円｜—｜⚠日程不明
- 3907 Silicon Studio Corp.｜granville_rebound｜🔻悪化｜💎割安｜FAIL_INSEN｜1,219円｜💰12.9万円｜—｜⚠日程不明
- 4440 WITZ Corp.｜granville_rebound｜➖横ばい｜⚪妥当｜FAIL_INSEN｜1,666円｜💰18.0万円｜—｜⚠日程不明
- 8163 SRS HOLDINGS CO.,LTD.｜granville_rebound｜➖横ばい｜🔴過熱｜FAIL_UWAHIGE｜1,817円｜💰17.5万円｜—｜⏰決算 11/09(残5営業日)
- 4691 Washington Hotel Corp.｜granville_rebound｜⚠減速｜⚪妥当｜FAIL_UWAHIGE｜1,794円｜💰18.3万円｜—
- 6203 Howa Machinery, Ltd.｜granville_rebound｜⚠減速｜🟡やや割高｜FAIL_INSEN｜2,000円｜💰22.8万円｜—
- 6522 アスタリスク｜granville_rebound｜⚠減速｜🟢値頃｜FAIL_INSEN｜766円｜💰8.1万円｜—｜⚠日程不明
- 8360 Yamanashi Chuo Bank, Ltd.｜granville_rebound｜取得不可｜💎割安｜FAIL_INSEN｜1,301円｜💰13.2万円｜—
- 7380 Juroku Financial Group,Inc.｜granville_rebound｜取得不可｜⚪妥当｜FAIL_INSEN｜2,423.5円｜💰24.6万円｜—｜⏰決算 11/09(残5営業日)
- 8368 Hyakugo Bank, Ltd.｜granville_rebound｜取得不可｜🟡やや割高｜FAIL_INSEN｜2,138円｜💰21.8万円｜—
- 8713 Fidea Holdings Co.Ltd.｜granville_rebound｜業績データ取得不可(売上/経常欠損)｜🔴過熱｜FAIL_INSEN｜2,599円｜💰25.3万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 2962 テクニスコ｜granville_rebound｜—｜—｜FAIL_INSEN｜1,800円｜💰—｜—
- 3793 Drecom Co., Ltd.｜granville_rebound｜—｜—｜FAIL_INSEN｜453円｜💰—｜—｜⚠日程不明
- 5367 Nikkato Corporation｜granville_rebound｜—｜—｜FAIL_INSEN｜1,158円｜💰—｜—｜🚨決算直前 11/02(残1営業日)
- 5381 Mipox Corp.｜granville_rebound｜—｜—｜FAIL_INSEN｜940円｜💰—｜—｜⚠日程不明
- 6508 Meidensha Corporation｜granville_rebound｜—｜—｜FAIL_INSEN｜9,448円｜💰—｜—｜📉決算反応日 11/02｜⚡材料後出し｜📊
- 6840 ＡＫＩＢＡホールディングス｜granville_rebound｜—｜—｜FAIL_INSEN｜678円｜💰—｜—
- 6890 Ferrotec Corporation｜granville_rebound｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜7,666円｜💰79.4万円｜—｜📋カルテ窓 11/16(残10営業日)｜📌
- 7175 Imamura Securities Co.Ltd.｜granville_rebound｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜1,647円｜💰17.0万円｜—｜⚠日程不明
- 8377 ほくほくフィナンシャルグループ｜granville_rebound｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜749.4円｜💰7.6万円｜—｜⏰決算 11/09(残5営業日)
- 8609 岡三証券グループ｜granville_rebound｜—｜—｜FAIL_INSEN｜1,011円｜💰—｜—｜⚠日程不明
- 8739 スパークス・グループ｜granville_rebound｜業績データ取得不可｜⏸判定不能｜FAIL_UWAHIGE｜2,372円｜💰23.2万円｜—｜📉決算反応日 11/02｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚡材料後出し｜📊

## 変化点銘柄
- 265A エイチエムコム｜changepoint/changepoint🔔｜🚀確変｜🟢値頃｜FAIL_INSEN｜721円｜💰7.3万円｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 5803 フジクラ｜changepoint/changepoint🔔/changepoint🔔🔔｜🚀確変｜🟢値頃｜FAIL_INSEN｜3,918円｜💰40.9万円｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 4011 Headwaters Co.,Ltd｜changepoint🔔/changepoint｜🚀確変｜🟢値頃｜FAIL_INSEN｜2,100円｜💰21.6万円｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 9888 UEX LTD｜changepoint/changepoint🔔/changepoint🔔🔔｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1,282円｜💰13.8万円｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 7695 交換できるくん｜changepoint/changepoint🔔｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜865円｜💰8.7万円｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 9308 乾汽船｜changepoint/changepoint🔔🔔｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜2,344円｜💰23.6万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜🔒実弾封印中(PL3紙ログ収集中)
- 9962 ミスミグループ本社｜changepoint/changepoint🔔｜🔥絶好調｜⚪妥当｜PASS｜3,925円｜💰39.2万円｜⛔提案なし(材料後出し)｜📉決算反応日 11/02｜🔒実弾封印中(PL3紙ログ収集中)｜⚡材料後出し｜📊
  > 【業態】金型用部品の専門商社・ミスミが中核。ネット・カタログ販売。半製品で納期短縮。
  > 【いま】終値3,925円・直近5日+9.30%・📊2027年3月期第2四半期（中間期）決算短信〔日本基準〕(連結)
  > 【調子】🔥絶好調（10/13）
  > 【水準】⚪妥当（3.0/7）— PER23.02倍・PEG0.6208・52週86.6% ／ 💰単元39.2万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 6136 OSG CORP｜changepoint/changepoint🔔/changepoint🔔🔔｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜3,508円｜💰35.3万円｜—｜⚠日程不明｜🔒実弾封印中(PL3紙ログ収集中)
- 6857 アドバンテスト｜changepoint/changepoint🔔｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜34,860円｜💰338.6万円｜—｜🔒実弾封印中(PL3紙ログ収集中)｜⚡材料後出し｜📌
- 7318 セレンディップ・ホールディングス｜changepoint/changepoint🔔/changepoint🔔🔔｜🔥絶好調｜💎割安｜FAIL_INSEN｜1,091円｜💰10.9万円｜—｜🔒実弾封印中(PL3紙ログ収集中)｜⚡材料後出し｜📌
- 4368 4368｜changepoint/changepoint🔔｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜2,889円｜💰29.3万円｜—｜📉決算反応日 11/02｜🔒実弾封印中(PL3紙ログ収集中)｜⚡材料後出し｜📊
- 5582 （名称取得不可）｜changepoint/changepoint🔔｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1,794円｜💰18.2万円｜—｜📋カルテ窓 11/16(残10営業日)｜🔒実弾封印中(PL3紙ログ収集中)
- 5590 NETSTARS Co.,Ltd.｜changepoint/changepoint🔔｜⚡好調｜🟢値頃｜FAIL_INSEN｜642円｜💰6.6万円｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 478A Hutzper Inc.｜changepoint/changepoint🔔/changepoint🔔🔔｜⚡好調｜⚪妥当｜FAIL_INSEN｜660円｜💰7.3万円｜—｜📋カルテ窓 11/16(残10営業日)｜🔒実弾封印中(PL3紙ログ収集中)
- 9343 アイビス｜changepoint｜⚡好調｜⚪妥当｜FAIL_INSEN｜764円｜💰7.7万円｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 4498 Cybertrust Japan Co., Ltd.｜changepoint/changepoint🔔/changepoint🔔🔔｜⚡好調｜🟡やや割高｜PASS_DOJI｜2,150円｜💰21.5万円｜changepoint 2,150（✅即時可）｜🔒実弾封印中(PL3紙ログ収集中)
  > 【業態】情報・通信業
  > 【いま】終値2,150円・直近5日-12.96%（材料未確認）
  > 【調子】⚡好調（6/13）
  > 【水準】🟡やや割高（2.0/7）— PER28.44倍・PEG2.244・52週54.9% ／ 💰単元21.5万円
  > 【戦略】発火日終値2,150円の指値。追撃禁止・SL2,060円。🔒実弾封印中（PL3紙ログ収集中）
- 6284 日精エー・エス・ビー機械｜changepoint/changepoint🔔｜⚡好調｜🟢値頃｜FAIL_INSEN｜7,920円｜💰80.1万円｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 218A Liberaware｜changepoint/changepoint🔔｜⚡好調｜⚪妥当｜FAIL_INSEN｜855円｜💰9.1万円｜—｜⚠日程不明｜🔒実弾封印中(PL3紙ログ収集中)｜⚡材料後出し｜📌
- 6785 鈴木｜changepoint/changepoint🔔🔔｜✅順調｜⚪妥当｜FAIL_INSEN｜3,090円｜💰32.4万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜🔒実弾封印中(PL3紙ログ収集中)
- 4165 PLAID Inc.｜changepoint/changepoint🔔｜🔻悪化｜🔴過熱｜FAIL_UWAHIGE｜748円｜💰7.4万円｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 4071 Plus Alpha Consulting Co. LTD.｜changepoint/changepoint🔔｜✅順調｜⚪妥当｜FAIL_UWAHIGE｜2,262円｜💰23.1万円｜—｜🔒実弾封印中(PL3紙ログ収集中)｜⚡材料後出し｜📌
- 598A チャットプラス｜changepoint🔔/changepoint/changepoint🔔🔔｜✅順調｜⚪妥当｜FAIL_INSEN｜1,116円｜💰11.7万円｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 339A PROGRESS TECHNOLOGIES GROUP INC｜changepoint/changepoint🔔/changepoint🔔🔔｜➖横ばい｜⚪妥当｜FAIL_INSEN｜786円｜💰8.1万円｜—｜⚠日程不明｜🔒実弾封印中(PL3紙ログ収集中)
- 4488 AI inside Inc.｜changepoint｜➖横ばい｜🟡やや割高｜FAIL_INSEN｜1,949円｜💰20.3万円｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 4259 ExaWizards Inc.｜changepoint/changepoint🔔｜業績データ取得不可｜🟢値頃｜FAIL_INSEN｜785円｜💰7.6万円｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 3993 PKSHA Technology, Inc.｜changepoint/changepoint🔔｜業績データ取得不可｜⚪妥当｜FAIL_INSEN｜3,585円｜💰37.3万円｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 4478 freee K.K.｜changepoint/changepoint🔔/changepoint🔔🔔｜業績データ取得不可｜🔴過熱｜FAIL_UWAHIGE｜4,600円｜💰43.9万円｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 593A ティアフォー｜changepoint/changepoint🔔/changepoint🔔🔔｜取得不可｜🔴過熱｜FAIL_UWAHIGE｜2,403円｜💰23.6万円｜—｜🔒実弾封印中(PL3紙ログ収集中)

## 🤖AI特需銘柄
波: なし／25MA 上回り率 📡エネマネ・計量 14.29%・❄️冷却・空調 8.33%・🌐光通信 9.09%・🔬基板・素材 4.76%
- 3131 シンデン・ハイテックス｜ai_momentum/ai_reversal/granville_rebound｜🚀確変｜💎割安｜FAIL_INSEN｜5,200円｜💰64.0万円｜—
- 4187 大阪有機化学工業｜changepoint/changepoint🔔/ai_momentum｜🔥絶好調｜💎割安｜FAIL_INSEN｜4,360円｜💰44.0万円｜—｜⚠日程不明
- 2760 東京エレクトロン　デバイス｜ai_momentum/granville_oshime/ai_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜4,230円｜💰45.7万円｜—
- 9824 泉州電業｜ai_momentum/ai_reversal｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜8,140円｜💰82.0万円｜—｜⚠日程不明
- 6613 QD Laser, Inc.｜granville_oshime/ai_momentum｜🔥絶好調｜🔴過熱｜FAIL_INSEN｜2,406円｜💰24.2万円｜—
- 6521 オキサイド｜ai_momentum/ai_reversal｜⚡好調｜🟢値頃｜FAIL_INSEN｜3,100円｜💰35.8万円｜—｜⚠日程不明
- 4063 信越化学工業｜ai_momentum｜✅順調｜⚪妥当｜FAIL_INSEN｜5,966円｜💰57.9万円｜—｜⚠日程不明
- 1975 新日本空調｜ai_momentum｜➖横ばい｜🟡やや割高｜FAIL_INSEN｜3,640円｜💰39.9万円｜—
- 1982 日比谷総合設備｜ai_momentum｜⚠減速｜🔴過熱｜FAIL_INSEN｜3,145円｜💰33.4万円｜—
- 9960 トーテック｜granville_tenkan/granville_oshime/ai_momentum/ai_reversal｜⚠減速｜🔴過熱｜FAIL_INSEN｜4,270円｜💰43.8万円｜—
- 6254 野村マイクロ・サイエンス｜changepoint/changepoint🔔/ai_reversal｜🚀確変｜💎割安｜FAIL_INSEN｜2,645円｜💰28.2万円｜—
- 4047 関東電化工業｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜1,958円｜💰20.1万円｜—
- 4971 メック｜ai_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜5,870円｜💰60.1万円｜—
- 6407 CKD｜ai_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜4,645円｜💰47.9万円｜—
- 3110 日東紡｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜2,814.5円｜💰29.4万円｜—｜⏰決算 11/05(残3営業日)
- 4062 イビデン｜ai_reversal/granville_rebound｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜8,359円｜💰96.6万円｜—｜⚠日程不明
- 6981 村田製作所｜ai_reversal｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜6,358円｜💰68.9万円｜—｜📉決算反応日 11/02｜🤖AI特需 🔬基板・素材/中流｜📊
- 6524 湖北工業｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜4,495円｜💰45.9万円｜—
- 6235 オプトラン｜ai_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜2,230円｜💰24.1万円｜—
- 7729 東京精密｜ai_reversal｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜15,190円｜💰163.2万円｜—｜⏰決算 11/04(残2営業日)
- 6752 パナソニックHD｜ai_reversal/granville_rebound｜⚠減速｜⚪妥当｜FAIL_INSEN｜3,548円｜💰37.9万円｜—｜📉決算反応日 11/02｜⚡材料後出し｜📊
- 6779 Nihon Dempa Kogyo Co., Ltd.｜granville_rebound/ai_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,477円｜💰25.6万円｜—｜⏰決算 11/09(残5営業日)
- 6941 山一電機｜ai_reversal｜⚡好調｜🟡やや割高｜FAIL_INSEN｜7,310円｜💰96.2万円｜—｜⏰決算 11/05(残3営業日)｜🤖AI特需 🔬基板・素材/中流
- 6787 メイコー｜ai_reversal｜⚡好調｜💎割安｜FAIL_INSEN｜8,550円｜💰194.6万円｜—｜⏰決算 11/06(残4営業日)
- 6227 AIMECHATEC Ltd.｜granville_oshime/ai_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜5,340円｜💰57.7万円｜—
- 4973 JCU｜ai_reversal｜⚡好調｜🟡やや割高｜FAIL_INSEN｜4,160円｜💰48.3万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚡材料後出し｜🤖AI特需 🔬基板・素材/上流｜📌
- 8098 稲畑産業｜ai_reversal/granville_oshime｜✅順調｜🔴過熱｜FAIL_INSEN｜4,430円｜💰45.0万円｜—｜⏰決算 11/05(残3営業日)
- 5208 Arisawa Mfg.Co., Ltd.｜granville_oshime/ai_reversal｜✅順調｜🔴過熱｜FAIL_INSEN｜2,518円｜💰26.5万円｜—｜⏰決算 11/05(残3営業日)
- 6643 戸上電機製作所｜ai_reversal｜✅順調｜⚪妥当｜FAIL_UWAHIGE｜5,140円｜💰51.2万円｜—｜⏰決算 11/04(残2営業日)｜⚡材料後出し｜📌
- 5706 三井金属鉱業｜ai_reversal｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜2,017.5円｜💰21.5万円｜—
- 3103 ユニチカ｜ai_reversal/granville_rebound｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜1,193円｜💰12.3万円｜—
- 6590 芝浦メカトロニクス｜ai_reversal｜➖横ばい｜🟡やや割高｜FAIL_INSEN｜3,140円｜💰34.0万円｜—｜⏰決算 11/05(残3営業日)
- 5302 日本カーボン｜ai_reversal｜➖横ばい｜🔴過熱｜FAIL_INSEN｜4,885円｜💰49.1万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 01/29 第2回/8）
- 6617 東光高岳｜ai_reversal｜➖横ばい｜🔴過熱｜FAIL_INSEN｜5,460円｜💰74.4万円｜—｜📉決算反応日 11/02｜📊
- 9432 NTT｜ai_reversal｜➖横ばい｜🔴過熱｜FAIL_UWAHIGE｜173.3円｜💰1.7万円｜—｜⏰決算 11/04(残2営業日)
- 4203 住友ベークライト｜ai_reversal｜業績データ取得不可｜⚪妥当｜FAIL_INSEN｜8,109円｜💰78.3万円｜—｜⏰決算 11/04(残2営業日)｜📌
- 6777 santec｜ai_reversal｜—｜—｜FAIL_INSEN｜17,520円｜💰—｜—｜⏰決算 11/06(残4営業日)

## ⚡材料後出し
その日の足は開示前の情報。判定は参考値。
- 6862 ミナトホールディングス｜FAIL_INSEN｜📌｜
- 4771 F&M Co., Ltd.｜FAIL_INSEN｜📊｜
- 4477 BASE, Inc.｜FAIL_INSEN｜👥｜
- 6629 TECHNO HORIZON Co., Ltd.｜FAIL_INSEN｜📊｜
- 4565 Nxera Pharma Co., Ltd.｜FAIL_UWAHIGE｜📊｜
- 7433 Hakuto Co., Ltd.｜FAIL_INSEN｜📌｜
- 6302 住友重機械工業｜FAIL_INSEN｜📊｜
- 8987 Japan Excellent, Inc.｜FAIL_INSEN｜📌｜
- 9412 SKY Perfect JSAT Corporation｜FAIL_INSEN｜📌｜
- 5333 ＮＧＫ｜FAIL_INSEN｜📊｜
- 7721 Tokyo Keiki Inc.｜FAIL_INSEN｜📌｜
- 2782 Seria Co., Ltd.｜FAIL_UWAHIGE｜📊｜
- 7731 ニコン｜FAIL_INSEN｜📌｜
- 3279 Activia Properties, Inc.｜FAIL_UWAHIGE｜📌｜
- 3282 Comforia Residential REIT, Inc.｜FAIL_INSEN｜📌｜
- 8952 Japan Real Estate Investment Corp.｜FAIL_UWAHIGE｜📌｜
- 9882 Yellow Hat Ltd.｜FAIL_INSEN｜📊｜
- 1944 Kinden Corporation｜FAIL_INSEN｜📊｜
- 9533 TOHO GAS Co., Ltd.｜PASS｜🔁｜
- 8818 Keihanshin Building Co., Ltd.｜FAIL_INSEN｜📊｜
- 6632 JVCKENWOOD Corporation｜FAIL_INSEN｜📊｜
- 3309 Sekisui House Reit. Inc.｜PASS｜📌｜
- 6960 Fukuda Denshi Co., Ltd.｜PASS｜📊｜
- 8585 Orient Corporation｜FAIL_UWAHIGE｜📊｜
- 3471 Mitsui Fudosan Logistics Park, Inc.｜FAIL_INSEN｜📌｜
- 7384 Procrea Holdings,Inc.｜FAIL_UWAHIGE｜📌｜
- 4216 ASAHI YUKIZAI CORPORATION｜FAIL_INSEN｜📊｜
- 7148 Financial Products Group Co., Ltd.｜FAIL_INSEN｜📌｜
- 6752 パナソニックHD｜FAIL_INSEN｜📊｜
- 4973 JCU｜FAIL_INSEN｜📌｜
- 6643 戸上電機製作所｜FAIL_UWAHIGE｜📌｜
- 6562 Geniee, Inc.｜FAIL_INSEN｜📌｜
- 9742 アイネス｜FAIL_UWAHIGE｜📊｜
- 6196 Strike Group Co. Ltd.｜FAIL_UWAHIGE｜📊｜
- 8061 Seika Corporation｜FAIL_INSEN｜📌｜
- 8020 Kanematsu Corporation｜FAIL_INSEN｜📌｜
- 6371 Tsubakimoto Chain Co.｜FAIL_INSEN｜📊｜
- 9163 Nareru Group Inc.｜PASS｜📌｜
- 4617 中国塗料｜FAIL_INSEN｜📊｜
- 6770 Alps Alpine Co., Ltd.｜FAIL_UWAHIGE｜📊｜
- 8424 芙蓉総合リース｜FAIL_UWAHIGE｜📌｜
- 6080 Ｍ＆Ａキャピタルパートナーズ｜FAIL_UWAHIGE｜📌｜
- 1879 新日本建設｜FAIL_INSEN｜📌｜
- 4667 Aisan Technology Co., Ltd.｜FAIL_INSEN｜📌｜
- 9509 Hokkaido Electric Power Company,Incorporated｜FAIL_INSEN｜📊｜
- 6072 Jibannet Holdings Co., Ltd.｜FAIL_INSEN｜📌｜
- 9616 共立メンテナンス｜PASS｜📌｜
- 9900 Sagami Holdings Corp.｜FAIL_UWAHIGE｜📌｜
- 9166 GENDA Inc.｜FAIL_INSEN｜📌｜
- 6036 ＫｅｅＰｅｒ技研｜FAIL_INSEN｜📌｜
- 8137 サンワテクノス｜FAIL_INSEN｜📊｜
- 1436 GreenEnergy & Company｜FAIL_INSEN｜📌｜
- 5242 EYEZ INC.｜FAIL_INSEN｜📌｜
- 4968 Arakawa Chemical Industries,Ltd.｜FAIL_INSEN｜📢｜
- 8704 TRADERS HOLDINGS CO LTD｜FAIL_INSEN｜📢｜
- 6597 HPC SYSTEMS Inc.｜FAIL_INSEN｜📌｜
- 4082 第一稀元素化学工業｜FAIL_INSEN｜📌｜
- 6508 Meidensha Corporation｜FAIL_INSEN｜📊｜
- 8739 スパークス・グループ｜FAIL_UWAHIGE｜📊｜
- 9962 ミスミグループ本社｜PASS｜📊｜
- 6857 アドバンテスト｜FAIL_INSEN｜📌｜
- 7318 セレンディップ・ホールディングス｜FAIL_INSEN｜📌｜
- 4368 4368｜FAIL_INSEN｜📊｜
- 218A Liberaware｜FAIL_INSEN｜📌｜
- 4071 Plus Alpha Consulting Co. LTD.｜FAIL_UWAHIGE｜📌｜

## 📢開示
使用した一覧: https://kabutan.jp/disclosures/?kubun=&date=20261030 および date=20261029（全ページ巡回。2026-10-29 20:00 以降〜2026-10-30 の開示を対象）。フォールバック: なし。①-9へ引き渡し 32件（recalc_queue）
- 📊 4568 第一三共｜2027年3月期 第2四半期（中間期）決算短信〔IFRS〕（連結）（10-30 13:00）
- 📊 6960 Fukuda Denshi Co., Ltd.｜2027年３月期 第２四半期（中間期）決算短信〔日本基準〕（連結）（10-30 16:00）
- 📊 9962 ミスミグループ本社｜2027年3月期第2四半期（中間期）決算短信〔日本基準〕(連結)（10-30 15:00）
- 🔁 9533 TOHO GAS Co., Ltd.｜自己株式立会外買付取引（ToSTNeT-3）による自己株式の取得結果に関するお知らせ（10-30 10:30）
- 📢 4968 Arakawa Chemical Industries,Ltd.｜2027年３月期第２四半期（中間期）および通期連結業績予想の上方修正ならびに2027年３月期配当予想の修正（増配）に関するお知らせ（10-30 15:00）
- 📢 8704 TRADERS HOLDINGS CO LTD｜通期連結業績予想の修正(上方修正)に関するお知らせ（10-30 15:30）
- 📊 1944 Kinden Corporation｜2027年３月期 第２四半期（中間期）決算短信〔日本基準〕（連結）（10-30 15:30）
- 📊 2782 Seria Co., Ltd.｜2027年３月期 第２四半期（中間期）決算短信〔日本基準〕（非連結）（10-30 15:30）
- 📊 2805 S&B Foods Inc.｜2027年３月期　第２四半期（中間期）決算短信〔日本基準〕（連結）（10-30 14:00）
- 📊 4045 Toagosei Co., Ltd.｜2026年12月期 第3四半期決算短信 〔日本基準〕（連結）（10-30 14:00）
- 📊 4216 ASAHI YUKIZAI CORPORATION｜2027年3月期 第2四半期（中間期）決算短信〔日本基準〕 (連結)（10-30 16:00）
- 📊 4368 4368｜2027年3月期 第2四半期（中間期）決算短信〔日本基準〕（連結）（10-30 16:00）
- 📊 4565 Nxera Pharma Co., Ltd.｜2026年12月期第３四半期決算短信〔ＩＦＲＳ〕(連結)（10-30 15:30）
- 📊 4617 中国塗料｜2027年3月期 第2四半期（中間期）決算短信〔日本基準〕（連結）（10-30 15:30）
- 📊 4771 F&M Co., Ltd.｜2027年３月期 第２四半期（中間期）決算短信〔日本基準〕（連結）（10-30 15:00）
- 📊 5333 ＮＧＫ｜2027年３月期 第２四半期（中間期）決算短信〔日本基準〕（連結）（10-30 15:40）
- 📊 6196 Strike Group Co. Ltd.｜2026年９月期 決算短信〔日本基準〕(連結)（10-30 15:30）
- 📊 6302 住友重機械工業｜2026年12月期第３四半期決算短信〔日本基準〕(連結)（10-30 14:00）
- 📊 6371 Tsubakimoto Chain Co.｜2027年３月期第２四半期（中間期）決算短信〔日本基準〕(連結)（10-30 15:30）
- 📊 6508 Meidensha Corporation｜2027年３月期 第２四半期（中間期）決算短信〔日本基準〕(連結)（10-30 15:30）
- 📊 6617 東光高岳｜2027年３月期第２四半期（中間期）決算短信〔日本基準〕(連結)（10-30 14:00）
- 📊 6629 TECHNO HORIZON Co., Ltd.｜2027年３月期　第２四半期決算短信〔日本基準〕（連結）（10-30 16:00）
- 📊 6632 JVCKENWOOD Corporation｜2027年３月期　第２四半期（中間期）決算短信〔IFRS〕（連結）（10-30 15:45）
- 📊 6752 パナソニックHD｜2027年３月期 第２四半期（中間期）決算短信〔ＩＦＲＳ〕（連結）（10-30 15:30）
- 📊 6770 Alps Alpine Co., Ltd.｜2027年３月期第２四半期（中間期）決算短信〔日本基準〕（連結）（10-30 15:30）
- 📊 6981 村田製作所｜2027年３月期 第２四半期（中間期）決算短信〔ＩＦＲＳ〕（連結）（10-30 14:00）
- 📊 7381 ＣＣＩグループ｜2027年3月期　第2四半期（中間期）決算短信〔日本基準〕（連結）（10-30 13:00）
- 📊 8014 Chori Co., Ltd.｜2027年３月期第２四半期（中間期）決算短信〔日本基準〕(連結)（10-30 14:00）
- 📊 8137 サンワテクノス｜2027年３月期 第２四半期（中間期）決算短信〔日本基準〕（連結）（10-30 15:30）
- 📊 8585 Orient Corporation｜2027年３月期 第２四半期（中間期）決算短信〔日本基準〕（連結）（10-30 15:30）
- 📊 8616 Tokai Tokyo Financial Holdings, Inc.｜2027年３月期 第２四半期（中間期）決算短信〔日本基準〕(連結)（10-30 11:00）
- 📊 8704 TRADERS HOLDINGS CO LTD｜2027年３月期  第２四半期（中間期）決算短信〔日本基準〕（連結）（10-30 15:30）
- 📊 8739 スパークス・グループ｜2027年３月期 第２四半期（中間期）決算短信〔日本基準〕（連結）（10-30 12:30）
- 📊 8818 Keihanshin Building Co., Ltd.｜2027年３月期第２四半期（中間期）決算短信〔日本基準〕（連結）（10-30 15:00）
- 📊 9509 Hokkaido Electric Power Company,Incorporated｜2027年３月期　第２四半期（中間期）決算短信〔日本基準〕(連結)（10-30 15:30）
- 📊 9742 アイネス｜2027年3月期 第2四半期（中間期）決算短信〔日本基準〕（連結）（10-30 15:30）
- 📊 9882 Yellow Hat Ltd.｜2027年3月期　第2四半期（中間期）決算短信〔日本基準〕（連結）（10-30 15:30）
- 🔁 150A ＪＳＨ｜自己株式の取得結果及び取得終了に関するお知らせ（会社法第165条第２項の規定による定款の定めに基づく自己株式の取得）（10-30 11:30）
- 🔁 6196 Strike Group Co. Ltd.｜自己株式取得に係る事項の決定に関するお知らせ（10-30 15:30）
- 🔁 8739 スパークス・グループ｜自己株式取得に係る事項の決定及び自己株式の消却に関するお知らせ（10-30 12:30）
- 🔁 9882 Yellow Hat Ltd.｜自己株式立会外買付取引（ToSTNeT-3）による自己株式の買付けに関するお知らせ（10-30 16:30）
- 👥 4477 BASE, Inc.｜当社株主による大量保有報告書(変更報告書)の提出について（10-30 16:30）
- 📌その他重要開示: 123件（プール在籍・省略）

## 総当りゲート
### 5手法
- PASS（23）: 5757 CK San-Etsu Co., Ltd.、505A Geekly,Inc.、4743 ITFOR Inc.、2820 Yamami Co.、3222 United Super Markets Holdings, Inc.、8278 Fuji Co., Ltd.、7458 Daiichikosho Co., Ltd.、2809 Kewpie Corporation、8198 Maxvalu Tokai Co., Ltd.、9533 TOHO GAS Co., Ltd.、3289 Tokyu Fudosan Holdings Corp.、8276 HEIWADO CO., LTD.、9974 BELC Co., Ltd.、3309 Sekisui House Reit. Inc.、8954 ORIX JREIT Inc.、9948 Arcs Company, Limited、9436 Okinawa Cellular Telephone Company、6960 Fukuda Denshi Co., Ltd.、8194 Life Corporation、6810 Maxell, Ltd.、3994 マネーフォワード、4443 Ｓａｎｓａｎ、6814 古野電
- PASS_DOJI（1）: 7811 中本パックス
- FAIL_UWAHIGE（55）: 5137 Smart Drive Co. Ltd.、276A CCReB Advisors Inc.、4053 Sun Asterisk, Inc.、5136 tripla Co.,Ltd.、4377 ONE CAREER Inc.、5537 AlbaLink Co.,Ltd.、9560 PROGRIT, Inc.、147A SORACOM,INC.、5034 unerry, Inc.、7678 ASAKUMA CO.,LTD.、6289 Giken Ltd.、446A ノースサンド、3696 セレス、4933 I-ne CO., LTD.、3843 Freebit Co., Ltd.、4331 Take and Give. Needs Co., Ltd.、4565 Nxera Pharma Co., Ltd.、3391 TSURUHA Holdings, Inc.、8282 K'S HOLDINGS CORPORATION、8125 Wakita & Co., Ltd.、8393 Miyazaki Bank Ltd.、2782 Seria Co., Ltd.、3279 Activia Properties, Inc.、8524 North Pacific Bank, Ltd.、8952 Japan Real Estate Investment Corp.、3148 Create SD Holdings Co., Ltd.、8066 Mitani Corporation、7984 Kokuyo Co., Ltd.、1333 Umios Corporation、2379 dip Corporation、3249 Industrial & Infrastructure Fund Investment Corporation、3283 Nippon Prologis REIT, Inc.、3292 AEON REIT Investment Corp.、3462 Nomura Real Estate Master Fund, Inc.、8953 Japan Metropolitan Fund Investment Corporation、8955 Japan Prime Realty Investment Corporation、2815 ARIAKE JAPAN Co., Ltd.、4928 Noevir Holdings Co., Ltd.、1662 Japan Petroleum Exploration Co., Ltd.、8585 Orient Corporation、3612 WORLD CO.,LTD.、8253 Credit Saison Co., Ltd.、7381 ＣＣＩグループ、8345 Bank of Iwate Ltd.、8367 南都銀行、7384 Procrea Holdings,Inc.、3591 WACOAL HOLDINGS CORP、8975 Ichigo Office REIT Investment Corporation、5246 ＥＬＥＭＥＮＴＳ、5932 三協立山、3479 ＴＫＰ、6643 戸上電機製作所、9432 NTT、3496 アズーム、9064 ヤマトホールディングス
- FAIL_INSEN（191）: 6862 ミナトホールディングス、3556 RenetJapanGroup, Inc.、4434 Serverworks Co., Ltd.、5027 AnyMind Group Inc.、9554 AViC Co. Ltd.、212A FIT EASY Inc.、3915 TerraSky Co., Ltd.、421A Movin' Strategic Career CO.,LTD.、5132 pluszero,Inc.、6298 Y.A.C.HOLDINGS CO.,LTD.、7047 PORT INC.、5821 Hirakawa Hewtech Corp.、4058 Toyokumo, Inc.、6071 IBJ, Inc.、9268 OPTIMUS GROUP Co., Ltd.、4771 F&M Co., Ltd.、4477 BASE, Inc.、2980 SRE Holdings Corp.、4412 Science Arts, Inc.、5038 eWeLL Co.,Ltd、6629 TECHNO HORIZON Co., Ltd.、3077 Horiifoodservice Co., Ltd.、618A KOMPEITO Inc.、7567 Sakae Electronics Corp.、6337 Tesec Corporation、2930 北の達人コーポレーション、4379 Photosynth inc.、7161 Jimoto Holdings, Inc.、6278 ユニオンツール、6875 メガチップス、8871 GOLDCREST Co., Ltd.、5344 MARUWA CO., LTD.、6516 Sanyo Denki Co., Ltd.、6754 アンリツ、3036 アルコニックス、6268 ナブテスコ、6481 THK Co., Ltd.、7433 Hakuto Co., Ltd.、8336 武蔵野銀行、6324 Harmonic Drive Systems Inc.、6645 OMRON Corporation、1803 Shimizu Corporation、5301 Tokai Carbon Co., Ltd.、7733 Olympus Corp.、8346 東邦銀行、4088 Air Water Inc.、7004 カナデビア、6370 栗田工業、8386 百十四銀行、8522 Bank of Nagoya, Ltd.、2874 YOKOREI CO. LTD.、6302 住友重機械工業、3116 Toyota Boshoku Corp.、8987 Japan Excellent, Inc.、5101 Yokohama Rubber Co., Ltd.、6332 月島ホールディングス、8088 岩谷産業、9412 SKY Perfect JSAT Corporation、5333 ＮＧＫ、7721 Tokyo Keiki Inc.、8714 池田泉州ホールディングス、8399 琉球銀行、268A Rigaku Holdings Corporation、9072 NIKKON Holdings Co., Ltd.、6454 Max Co., Ltd.、4666 Park24 Co., Ltd.、7731 ニコン、8381 San-in Godo Bank Ltd.、3282 Comforia Residential REIT, Inc.、6925 Ushio Inc.、7276 Koito Manufacturing Co., Ltd.、1861 Kumagai Gumi Co., Ltd.、1417 MIRAIT ONE Corporation、5331 ノリタケ、3433 TOCALO Co., Ltd.、6368 Organo Corp.、9882 Yellow Hat Ltd.、1820 Nishimatsu Construction Co., Ltd.、1944 Kinden Corporation、1952 Shin Nippon Air Technologies Co., Ltd.、6269 Modec, Inc.、7003 Mitsui ES Holdings Co., Ltd.、8584 Jaccs Co., Ltd.、1860 Toda Corporation、4966 上村工業、2659 SAN-A CO., LTD.、5021 Cosmo Energy Holdings Co., Ltd.、6055 Japan Material Co., Ltd.、2805 S&B Foods Inc.、6807 Japan Aviation Electronics Industry, Limited、8818 Keihanshin Building Co., Ltd.、1719 HAZAMA ANDO Corporation、1833 Okumura Corporation、6632 JVCKENWOOD Corporation、6674 ジーエス・ユアサ　コーポレーション、9503 Kansai Electric Power Company, Incorporated、3445 RS Technologies Co. Ltd.、6366 Chiyoda Corp.、7220 Musashi Seimitsu Industry Co., Ltd.、7278 Exedy Corporation、5844 Kyoto Financial Group,Inc.、6479 ミネベア、1893 Penta-Ocean Construction Co., Ltd.、6183 BELLSYSTEM24 Holdings, Inc.、6753 Sharp Corporation、3234 Mori Hills Reit Investment Corporation、3296 NIPPON REIT Investment Corp、5482 Aichi Steel Corporation、8961 MORI TRUST REIT.Inc、8986 Daiwa Securities Living Investment Corporation、1946 Toenec Corporation、4980 Dexerials Corp.、5631 Japan Steel Works, Ltd.、1963 日揮ホールディングス、3105 日清紡ホールディングス、5310 Toyo Tanso Co., Ltd.、6804 Hosiden Corp.、1969 高砂熱学工業、9699 NISHIO HOLDINGS CO. LTD.、5831 Shizuoka Financial Group, Inc.、8370 紀陽銀行、3471 Mitsui Fudosan Logistics Park, Inc.、8174 NIPPON GAS Co., Ltd.、8304 あおぞら銀行、8334 Gunma Bank, Ltd.、8366 滋賀銀行、7201 Nissan Motor Co., Ltd.、4021 Nissan Chemical Corporation、4205 Zeon Corporation、4216 ASAHI YUKIZAI CORPORATION、6349 Komori Corporation、6471 日本精工、6651 NITTO KOGYO Corporation、6652 IDEC Corporation、6923 Stanley Electric Co., Ltd.、7148 Financial Products Group Co., Ltd.、7186 横浜フィナンシャルグループ、7322 三十三フィナンシャルグループ、7995 Valqua Ltd.、8354 ふくおかフィナンシャルグループ、8359 Hachijuni Nagano Bank, Ltd.、8600 トモニホールディングス、8616 Tokai Tokyo Financial Holdings, Inc.、8628 Matsui Securities Co., Ltd.、8698 Monex Group, Inc.、7624 NaITO、7713 シグマ光機、5018 ＭＯＲＥＳＣＯ、6668 ＡＤプラズマ、3498 霞ヶ関Ｃ、3091 ブロンコビリー、6505 東洋電機製造、6532 ベイカレント、4176 ココナラ、3131 シンデン・ハイテックス、4187 大阪有機化学工業、2760 東京エレクトロン　デバイス、9824 泉州電業、6613 QD Laser, Inc.、6521 オキサイド、4063 信越化学工業、1975 新日本空調、1982 日比谷総合設備、9960 トーテック、6254 野村マイクロ・サイエンス、4047 関東電化工業、4971 メック、6407 CKD、3110 日東紡、4062 イビデン、6981 村田製作所、6524 湖北工業、6235 オプトラン、7729 東京精密、6752 パナソニックHD、6779 Nihon Dempa Kogyo Co., Ltd.、6941 山一電機、6787 メイコー、6227 AIMECHATEC Ltd.、4973 JCU、8098 稲畑産業、5208 Arisawa Mfg.Co., Ltd.、5706 三井金属鉱業、3103 ユニチカ、6590 芝浦メカトロニクス、5302 日本カーボン、6617 東光高岳、4203 住友ベークライト、6777 santec、9211 f-code Inc.、5590 NETSTARS Co.,Ltd.
- SKIP（0）: なし
### グランビル
- PASS（28）: 8697 日本取引所グループ、4544 H.U.Group Holdings, Inc.、4763 クリーク・アンド・リバー社、4568 第一三共、4848 Fullcast Holdings Co., Ltd.、8113 Unicharm Corporation、9163 Nareru Group Inc.、2897 Nissin Foods Holdings Co., Ltd.、5233 太平洋セメント、2811 Kagome Co., Ltd.、4922 コーセーホールディングス、8167 リテールパートナーズ、7921 ＴＡＫＡＲＡ　＆　ＣＯＭＰＡＮＹ、4912 ライオン、2871 ニチレイ、3563 ＦＯＯＤ　＆　ＬＩＦＥ　ＣＯＭＰＡＮＩＥＳ、8008 Yondoshi Holdings, Inc.、6523 ＰＨＣホールディングス、8410 Seven Bank, Ltd.、9536 SAIBU GAS HOLDINGS CO. LTD.、1518 三井松島ホールディングス、9044 NANKAI Co., Ltd.、8043 Starzen Company Limited、9616 共立メンテナンス、8255 Axial Retailing, Inc.、8343 Akita Bank, Ltd.、8364 清水銀行、9697 カプコン
- PASS_DOJI（2）: 3927 アークン、2681 2nd RETAILING Co., Ltd.
- FAIL_UWAHIGE（52）: 8944 Land Business Co., Ltd.、7725 INTER ACTION Corporation、9742 アイネス、4534 Mochida Pharmaceutical Co., Ltd.、3405 クラレ、8095 Astena Holdings Co.,Ltd.、7199 プレミアグループ、6196 Strike Group Co. Ltd.、3562 No.1 Co., Ltd.、3661 m-up holdings, Inc.、6432 竹内製作所、7747 朝日インテック、3549 クスリのアオキホールディングス、4549 Eiken Chemical Co., Ltd.、4956 Konishi Co., Ltd.、7181 JAPAN POST INSURANCE Co., Ltd.、7513 Kojima Co., Ltd.、9837 Morito Co., Ltd.、4552 JCR Pharmaceuticals Co., Ltd.、6770 Alps Alpine Co., Ltd.、5105 ＴＯＹＯ　ＴＩＲＥ、8424 芙蓉総合リース、5532 リアルゲイト、8160 KISOJI CO., LTD.、9842 アークランズ、5243 ｎｏｔｅ、6834 精工技研、6080 Ｍ＆Ａキャピタルパートナーズ、4431 Smaregi, Inc.、6736 Suncorporation、2602 日清オイリオグループ、6570 Kyowa Corporation Co. Ltd.、8919 カチタス、7616 Colowide Co., Ltd.、8392 大分銀行、8395 佐賀銀行、4373 Simplex Holdings,Inc.、3097 Monogatari Corporation、456A Human Made Inc.、9505 Hokuriku Electric Power Company、9900 Sagami Holdings Corp.、8361 Ogaki Kyoritsu Bank, Ltd.、6027 Bengo4.com, Inc.、8362 Fukui Bank, Ltd.、6769 Thine Electronics, Inc.、477A Startline CO.,LTD.、8344 Yamagata Bank, Ltd.、9278 BOOKOFF GROUP HOLDINGS LIMITED、4997 日本農薬、8163 SRS HOLDINGS CO.,LTD.、4691 Washington Hotel Corp.、8739 スパークス・グループ
- FAIL_INSEN（124）: 5254 Arent, Inc.、6905 Cosel Co., Ltd.、9553 MicroAd, Inc.、2986 LA Holdings Co.,Ltd、6562 Geniee, Inc.、6473 JTEKT Corporation、6255 NPC Incorporated、7744 ノーリツ鋼機、3741 Systems Engineering Consultants Co., Ltd.、7970 Shin-Etsu Polymer Co., Ltd.、5838 Rakuten Bank, Ltd.、6470 Taiho Kogyo Co., Ltd.、3935 Edia Co. Ltd.、6768 Tamura Corporation、8061 Seika Corporation、4169 Enechange Ltd.、6988 日東電工、8020 Kanematsu Corporation、8014 Chori Co., Ltd.、3092 ＺＯＺＯ、5184 ニチリン、6371 Tsubakimoto Chain Co.、6592 Mabuchi Motor Co., Ltd.、4166 Cacco, Inc.、8850 スターツコーポレーション、8927 Meiho Enterprise Co., Ltd.、186A Astroscale Holdings Inc.、3569 セーレン、4183 Mitsui Chemicals, Inc.、4272 Nippon Kayaku Co., Ltd.、7269 スズキ、5461 Chubu Steel Plate Co., Ltd.、7734 Riken Keiki Co., Ltd.、8012 Nagase & Co., Ltd.、4617 中国塗料、6328 Ebara Jitsugyo Co., Ltd.、6208 Ishikawa Seisakusho,Ltd.、8081 Kanaden Corporation、4902 Konica Minolta, Inc.、4375 セーフィー、4005 住友化学、4045 Toagosei Co., Ltd.、4401 ＡＤＥＫＡ、4937 Ｇ−ＷＡＱＯＯ、7806 MTG Co., Ltd.、4382 HEROZ, Inc.、3156 レスター、8051 山善、7856 HAGIHARA INDUSTRIES INC.、1879 新日本建設、3040 ソリトンシステムズ、5892 ＹＵＴＯＲＩ、9902 Nichiden Corporation、3106 倉敷紡績、4667 Aisan Technology Co., Ltd.、6250 Yamabiko Corporation、7609 ダイトロン、9304 澁澤倉庫、4413 baudroie,inc.、6340 澁谷工業、7350 Okinawa Financial Group, Inc.、4475 HENNGE K.K.、6418 Japan Cash Machine Co., Ltd.、6998 Nippon Tungsten Co., Ltd.、5985 SUNCALL CORPORATION、4208 UBE Corporation、6379 RAIZNEXT Corporation、3107 ダイワボウホールディングス、4044 Central Glass Co., Ltd.、9509 Hokkaido Electric Power Company,Incorporated、6072 Jibannet Holdings Co., Ltd.、7630 Ichibanya Co., Ltd.、8097 SAN-AI OBBLI CO. LTD、8059 Daiichi Jitsugyo Co., Ltd.、9166 GENDA Inc.、338A ZenmuTech,Inc.、3692 ＦＦＲＩセキュリティ、6036 ＫｅｅＰｅｒ技研、8137 サンワテクノス、8624 Ichiyoshi Securities Co., Ltd.、3778 SAKURA Internet Inc.、3691 DIGITAL PLUS, Inc.、3891 ニッポン高度紙工業、479A PRONI Inc.、4419 Finatext Holdings Ltd.、1436 GreenEnergy & Company、8995 Makoto Construction Co,Ltd、6963 ROHM Company Limited、150A ＪＳＨ、7715 長野計器、6490 ＰＩＬＬＡＲ、5242 EYEZ INC.、6336 石井表記、4968 Arakawa Chemical Industries,Ltd.、2354 YE DIGITAL CORPORATION、8704 TRADERS HOLDINGS CO LTD、4100 Toda Kogyo Corp.、6597 HPC SYSTEMS Inc.、3687 Fixstars Corp.、5574 ABEJA,Inc.、7256 河西工業、278A Ｔｅｒｒａ　Ｄｒｏｎｅ、4346 NEXYZ.Group Corporation、7354 Direct Marketing MiX Inc.、4082 第一稀元素化学工業、3653 Morpho, Inc.、3907 Silicon Studio Corp.、4440 WITZ Corp.、6203 Howa Machinery, Ltd.、6522 アスタリスク、8360 Yamanashi Chuo Bank, Ltd.、7380 Juroku Financial Group,Inc.、8368 Hyakugo Bank, Ltd.、8713 Fidea Holdings Co.Ltd.、2962 テクニスコ、3793 Drecom Co., Ltd.、5367 Nikkato Corporation、5381 Mipox Corp.、6508 Meidensha Corporation、6840 ＡＫＩＢＡホールディングス、6890 Ferrotec Corporation、7175 Imamura Securities Co.Ltd.、8377 ほくほくフィナンシャルグループ、8609 岡三証券グループ
- SKIP（0）: なし
### 変化点
- PASS（1）: 9962 ミスミグループ本社
- PASS_DOJI（1）: 4498 Cybertrust Japan Co., Ltd.
- FAIL_UWAHIGE（5）: 4180 ＡＰＰＩＥＲ　ＧＲＯＵＰ、4165 PLAID Inc.、4071 Plus Alpha Consulting Co. LTD.、4478 freee K.K.、593A ティアフォー
- FAIL_INSEN（21）: 265A エイチエムコム、5803 フジクラ、4011 Headwaters Co.,Ltd、9888 UEX LTD、7695 交換できるくん、9308 乾汽船、6136 OSG CORP、6857 アドバンテスト、7318 セレンディップ・ホールディングス、4368 4368、5582 （名称取得不可）、478A Hutzper Inc.、9343 アイビス、6284 日精エー・エス・ビー機械、218A Liberaware、6785 鈴木、598A チャットプラス、339A PROGRESS TECHNOLOGIES GROUP INC、4488 AI inside Inc.、4259 ExaWizards Inc.、3993 PKSHA Technology, Inc.
- SKIP（0）: なし

除籍（first_seenから30暦日超・SBIグループ登録解除候補）: 6627 Tera Probe, Inc.、3374 Naigai Tec Corporation、6918 Aval Data Corporation、9064 ヤマトホールディングス、4658 日本空調サービス、8793 ＮＥＣキャピタルソリューション、1815 鉄建建設、3496 アズーム、7751 キヤノン、290A ＳＹＮＳＰＥＣＴＩＶＥ、6023 ダイハツインフィニアース、336A ダイナミックマッププラットフォーム、2767 円谷フィールズホールディングス、2122 インタースペース、584A LiNKX, Inc.、8151 東陽テクニカ

## 機械詳細
- 派生ファイル: grades.json 958銘柄/541.7KiB、pool_bars.json 505銘柄/433.6KiB、earnings_calendar.json 987銘柄/133.8KiB（nx非null 751・次回決算日 付与 751件）
- gate_history: gate_history/2026-10-30.json を新規作成（verdicts 504件=評価504件／nominations 88件）
- 抜粋規則: 通知【通過】10件（method/ai/granville/changepoint の群別ラウンドロビン）。PASS群別内訳 method24/ai0/granville30/changepoint2/不明0
- method_score 保持60件/null444件
- ヘッドライン付与 56件（PASS全件56と一致: True）
- kabutan 取得: 決算ページ57件（PASS+保有）・トップページ7件（上限50件に対し7件・打ち切り0件）。業種の埋め戻し 0件。開示一覧 2513行
- profile_cache 総数940・本夜追加5件・業態が「未取得」のまま出た件数 1
- earnings_log 総数152／本夜追記34件／リターン補完（直近60日）あり
- gyoseki_cache 再計算 11件（history 退避 3件・取得不可で据置 0件）: 4498、6960、9962、9533、9536、4568、9697、4922、8113、2897、2811
- 鮮度ゲート: 鮮度切れ除外18件・nom_age分布 0-2:185/3-10:168/11+:149・last_seen欠損0件
- 記録の凍結: verdicts 504件・nominations 88件（新規38・再指名50）・業種 付与済み474/未付与30
- トレンド文脈: ctx {'レンジ': 150, '合致': 128, '不一致': 144, '判定不能': 5, '不一致（長期下向き）': 77}・PASS のうち ctx 合致 12件・形態が付いた銘柄 187件
- 3日ルール: 判定3銘柄・streak≥3 1・streak=2 0・判定不可0
- 業種別PER中央値: 算出26業種・spm 付与 903銘柄
- 開示の分類別件数: 📢2/📉0/📊34/🔁5/👥1/🏛0/📦0/📌123（プール＋保有の突合分）
- 熟成由来(value_gap)の候補 0件（watchlist に nominate_for=2026-10-30 なし）
- 権利情報: rights_cache 総数503・本夜 配当取得13件（kabutan 決算ページの年間予想配当のみ・中間/期末の内訳は不明）／優待取得 0件（minkabu は取得せず不明のまま）
- 次回決算日: 付与751件（一覧由来706）・前年同期発表日 付与361件・earnings_calendar.json 987銘柄
- STEP 4.8 週末ブリーフ: 実施（市場イベントは固定表＋日付計算。WebSearch補足は未実施）
- master.json の変更行数: +10849/-9517（indent=2・往復一致）
