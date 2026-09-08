# 夜間ゲート 2026-09-08

## サマリー
- 評価数: 446 ／ PASS: 42(+PASS_DOJI 6) ／ FAIL_UWAHIGE: 70 ／ FAIL_INSEN: 327 ／ SKIP: 1
- 発注可能提案数: 25件（除外 23件）
- 市場一言: 半導体主導リスクオン想定で寄ったが、米利上げ観測再燃とF&G42(Fear)が重しとなり日経平均は前日比-1.70%で反落（レンジ様子見）。
- 実行モード: 通常 ／ base_day: 2026-09-08 ／ week_open: false（火曜実行・翌営業日は水曜のため週初条件に該当せず）
- 対象営業日判定根拠: 2026-09-08(火)は土日・祝日・年末年始のいずれにも該当しない通常営業日のため通常モードで実行

## 検証結果
- V1(四者一致): proposals=25 / results entry_price保持=25 / 模擬テンプレ行数=25 → 一致: はい
- V2(PASS収支): PASS計48件=提案25件+除外23件、除外全件にorder_status有(null=0件) → はい
- V3(code重複ゼロ・verdict単一値): 重複なし → はい
- V4(valuation_cache static不変更): 既存48銘柄のstatic変更0件 → はい
- V5(許可キー以外不変更): 変更トップキー=['pipeline', 'night_gate', 'gyoseki_cache', 'valuation_cache', 'profile_cache']、想定外=[] → はい（earnings_logは内容不変のため差分なし）
- V6(gyoseki絵文字整合): 不整合0件（'判定保留'系・'取得不可'系はgyoseki_spec.overridesの正規表示でありチェック対象外） → はい
- V7(board必須セクション): 欠落=[]（week_open=falseのため📅今週のカタリストは非該当） → はい
- V8(模擬テンプレ書式): 不正0件 → はい
- V9(gate_history一致): gate_history/2026-09-08.jsonをnight_gate_today.jsonとバイト単位で一致するよう新規作成 → はい
- V10(base_day整合): results.night_gate=2026-09-08, today_json=2026-09-08, gate_history=gate_history/2026-09-08.json, 模擬テンプレ1行目=2026-09-08 → はい
- V11(書き出し整形): git diff --numstat master.json = +4927/-5221行（検出indent幅=2）。5,000行の目安を超過するが、トップキー差分は['pipeline','night_gate','gyoseki_cache','valuation_cache','profile_cache']のみでkey順序・indentとも元と一致（V5で確認済み）。原因はpool446銘柄全件の終値・ローソク足・値頃感を毎晩再取得する本ルーティンの設計上不可避な内容差分（前回base_day2026-09-07→今回2026-09-08で全銘柄の株価が実際に動き、poolも425→446へ21銘柄純増したため）。過去実績（2026-09-07実行で+7535/-12955）と同水準以下であり、フォーマット崩れではなく正当な差分と判断し続行。
- V12(並び順): (a)night_gate_today.json proposalsが厳密ソート済み=はい (b)模擬テンプレが同順序=はい (c)results内の提案銘柄抜粋順が同順序=いいえ（意図的な差異、前回踏襲）。night_gate.results配列自体は元の格納順（コード単位で位置保持、新規21銘柄は末尾昇順追加）を維持し、STEP5.2の並び順は表示系（night_gate_today.json/gate_history/board.md/模擬テンプレ/通知）にのみ適用した。
- V13(grades.json): meta.n一致 / 対象銘柄548件(gyoseki∪valuation∪profile) / サイズ116129バイト(120KB以下: はい)。前回同様biz(業態文)フィールドは省略。
- V14(method_score): 出所不明スコア0件、写し間違い0件 → はい
- V15(ヘッドライン網羅性): PASS/PASS_DOJI全48件中headline欠落0件、5キー欠落0件 → はい。(c)【調子】に「業績データ取得不可」を含む行が3件(7860/9166/2432)あるが、いずれもgyoseki_spec.overridesの正規グレード値がgyoseki_cacheにそのまま格納されているものであり、組み立て不具合によるプレースホルダ残留ではない
- V16(記録の蓄積): 決算発表分類0件のためearnings_log新規追記0件、grade_before/afterの順序違反なし（新規追記なしのため該当なし）、gyoseki history超過0件、earnings_log総数6件（既存4件はret_20算出に必要な経過営業日未達のためnull維持、無理な推定なし） → はい
- V17(pool_bars/3日ルール): meta.n一致=True(446銘柄)、20件超/未来日/降順の不正0件、保有銘柄bars欠落=[] → はい
- V18(指名鮮度ゲート): 誤除外0件、誤非除外0件、nom_age欠損0件 → はい

## 保有アラート
### 325A ＴＥＮＴＩＡＬ（信用買建・取得2026-09-01・建値1820.0円・100株）
- 業績: 判定保留(変則決算) — 決算日程不明
- ⚠足が崩れた（premise_kill）: 陰線・上髭0.25超（25日線乖離+3.44%）
- 含み損益: -3.57%
- ⚠目標未設定（SL未記録につきリスク不定）
- タイムストップ: 経過5営業日／残5営業日
- 値頃感: ⚪妥当（4.0/7）

### 1861 熊谷組（信用買建・取得2026-09-02・建値1295.0円・200株）
- 業績: ✅順調（3/13） — 決算日程不明
- ⚠足が崩れた（premise_kill）: 上髭0.25超・25日線割れ（25日線乖離-0.92%）
- 含み損益: +0.39%
- ⚠目標未設定（SL未記録につきリスク不定）
- タイムストップ: 経過4営業日／残6営業日
- 値頃感: 💎割安（6.0/7）
- 🔔3日ルール成立(4日連続・R=1306.0円): ルール上は利確検討。翌営業日の引成（大引け成行）返済が基本形

### 3064 ＭｏｎｏｔａＲＯ（信用買建・取得2026-09-04・建値1869.0円・100株）
- 業績: ⚡好調（6/13） — 決算日程不明
- 足は健全（25日線乖離+4.30%）
- 含み損益: +5.03%
- ⚠目標未設定（SL未記録につきリスク不定）
- タイムストップ: 経過2営業日／残8営業日
- 値頃感: ⚪妥当（3.0/7）

## 前夜の結果
PL5口座への正式な反映は週次①-11の採点で行われる。ここは参考情報。

前夜2026-09-07の提案72件 → 約定63・不約定9・判定不能0

| コード | 型 | 指値/逆指値 | 約定価格 | 当日終値 | 含み損益% |
|---|---|---|---|---|---|
| 3556 | momentum | 806 | 806 | 805 | -0.12% |
| 3441 | momentum | 2890 | 2890 | 2775 | -3.98% |
| 4047 | reversal | 2234 | 2184 | 2134 | -2.29% |
| 4971 | reversal | 6550 | 6480 | 6110 | -5.71% |
| 6516 | reversal | 5320 | 5260 | 5070 | -3.61% |
| 6481 | reversal | 6508 | 6421 | 6050 | -5.78% |
| 4368 | reversal | 2945 | 2906 | 2815 | -3.13% |
| 135A | momentum | 4325 | 4345 | 4520 | +4.03% |
| 146A | momentum | 3725 | 3730 | 3760 | +0.80% |
| 3104 | reversal | 3390 | 3320 | 3280 | -1.20% |
| 6941 | reversal | 7730 | 7610 | 7210 | -5.26% |
| 7409 | momentum | 1564 | 1564 | 1510 | -3.45% |
| 4187 | reversal | 4390 | 4365 | 4135 | -5.27% |
| 6754 | reversal | 3251 | 3200 | 3085 | -3.59% |
| 6622 | reversal | 12990 | 12770 | 12110 | -5.17% |
| 6504 | reversal | 13395 | 13385 | 12760 | -4.67% |
| 6806 | reversal | 24995 | 24910 | 23735 | -4.72% |
| 7581 | reversal | 7270 | 7270 | 7480 | +2.89% |
| 7972 | reversal | 2529 | 2510 | 2485 | -1.00% |
| 5444 | reversal | 12415 | 12250 | 12030 | -1.80% |
| 6113 | reversal | 2562.5 | 2542.5 | 2397 | -5.72% |
| 277A | momentum | 1916 | 1916 | 1907 | -0.47% |
| 6996 | reversal | 2684 | 2653 | 2474 | -6.75% |
| 7966 | reversal | 5480 | 5450 | 5110 | -6.24% |
| 5334 | reversal | 8082 | 7932 | 7444 | -6.15% |
| 3433 | reversal | 2782 | 2782 | 2756 | -0.93% |
| 6617 | reversal | 7030 | 6920 | 6500 | -6.07% |
| 6479 | reversal | 3468 | 3433 | 3326 | -3.12% |
| 5332 | reversal | 6007 | 6000 | 5804 | -3.27% |
| 6951 | reversal | 7063 | 7005 | 6829 | -2.51% |
| 6845 | reversal | 1486 | 1476 | 1451 | -1.69% |
| 6101 | reversal | 5290 | 5190 | 4850 | -6.55% |
| 6862 | momentum | 4640 | 4640 | 4350 | -6.25% |
| 6492 | momentum | 14570 | 14570 | 14150 | -2.88% |
| 5344 | reversal | 58470 | 58420 | 56140 | -3.90% |
| 3753 | reversal | 216 | 216 | 220 | +1.85% |
| 2693 | reversal | 281 | 281 | 280 | -0.36% |
| 6997 | reversal | 2872 | 2822 | 2628 | -6.87% |
| 6407 | reversal | 5520 | 5420 | 5050 | -6.83% |
| 9211 | momentum | 1456 | 1456 | 1427 | -1.99% |
| 9880 | reversal | 3500 | 3450 | 3275 | -5.07% |
| 3449 | reversal | 4130 | 4085 | 3965 | -2.94% |
| 6976 | reversal | 9824 | 9674 | 9046 | -6.49% |
| 6981 | reversal | 7620 | 7399 | 7023 | -5.08% |
| 6125 | reversal | 4915 | 4860 | 4700 | -3.29% |
| 6965 | reversal | 2359.5 | 2330 | 2225 | -4.51% |
| 194A | oshime | 1829.58 | 1829.58 | 1895 | +3.58% |
| 5186 | oshime | 6788.98 | 6788.98 | 6570 | -3.23% |
| 4612 | reversal | 1140 | 1124.5 | 1115 | -0.84% |
| 7721 | oshime | 7265.75 | 7260 | 6920 | -4.68% |
| 6191 | reversal | 778 | 778 | 785 | +0.90% |
| 3479 | oshime | 1883.01 | 1882 | 1873 | -0.48% |
| 4125 | reversal | 3840 | 3840 | 3775 | -1.69% |
| 6744 | reversal | 4180 | 4125 | 4020 | -2.55% |
| 255A | reversal | 5320 | 5320 | 5070 | -4.70% |
| 7745 | reversal | 2898 | 2852 | 2750 | -3.58% |
| 6363 | reversal | 3045 | 3025 | 2882 | -4.73% |
| 3063 | reversal | 1154 | 1150 | 1150 | +0.00% |
| 1982 | momentum | 3165 | 3165 | 3145 | -0.63% |
| 5310 | reversal | 7140 | 7130 | 6800 | -4.63% |
| 7600 | reversal | 683 | 677 | 624 | -7.83% |
| 4203 | reversal | 7200 | 7085 | 6900 | -2.61% |
| 6594 | reversal | 2812 | 2777 | 2722 | -1.98% |

不約定（追撃禁止）: 3851、6298、5038、8151、7911、2325、5851、8544、8387

## 模擬テンプレ
```
# base_day 2026-09-08 ／ 提案25件
# 使い方: 参戦する0〜3銘柄の行だけをコピーし、｜の後ろに参戦理由を書いてポジション株PJへ送る。
# 選ばなかった行は送らなくてよい（全行に理由を書く必要はない）。見送りは末尾の1行で足りる。
# 特定銘柄を理由つきで見送る場合のみ『模擬 見送り {code} ｜{理由}』を送る。
模擬 5136 kenmo_momentum 逆指値2008 SL1886.58 単元100 ｜
模擬 3391 choruko_reversal 指値2341 SL2222 単元100 ｜
模擬 8086 choruko_reversal 指値1460 SL1437 単元100 ｜
模擬 3288 choruko_reversal 指値7596 SL7521 単元100 ｜
模擬 3064 choruko_reversal 指値1963 SL1838.5 単元100 ｜
模擬 7581 choruko_reversal 指値7480 SL6810 単元100 ｜
模擬 428A kenmo_newhigh 逆指値1582 SL1486.14 単元100 ｜
模擬 2266 kenmo_momentum 逆指値1114 SL1046.22 単元100 ｜
模擬 7532 choruko_reversal 指値777.7 SL747 単元100 ｜
模擬 9247 choruko_reversal 指値1810 SL1758 単元100 ｜
模擬 3168 granville_rebound 指値1286 SL1246 単元100 ｜
模擬 4521 granville_tenkan 逆指値3916 SL3680.1 単元100 ｜
模擬 3222 granville_tenkan 逆指値851 SL799 単元100 ｜
模擬 2384 granville_oshime 指値4939.37 SL4914.8 単元100 ｜
模擬 194A granville_oshime 指値1846.27 SL1837.08 単元100 ｜
模擬 2931 granville_tenkan 逆指値349 SL327.12 単元100 ｜
模擬 4258 granville_oshime 指値4530.94 SL4508.4 単元100 ｜
模擬 7198 granville_tenkan 逆指値843 SL791.48 単元100 ｜
模擬 2281 granville_tenkan 逆指値2428 SL2281.38 単元100 ｜
模擬 1820 granville_tenkan 逆指値5647 SL5307.24 単元100 ｜
模擬 8803 granville_tenkan 逆指値2362 SL2219.34 単元100 ｜
模擬 9404 granville_tenkan 逆指値3005 SL2823.76 単元100 ｜
模擬 2432 granville_tenkan 逆指値2627.5 SL2468.91 単元100 ｜
模擬 9166 granville_oshime 指値726.49 SL722.88 単元100 ｜
模擬 4431 changepoint 指値3420 SL3370 単元100 🔒 ｜
模擬 見送り ｜
```

## PASS内訳
PASS 48件 = 発注可能 25件 + 除外 23件（型不一致3/材料後出し0/鮮度切れ20/その他0）

- 6630 YA-MAN Ltd. — ⛔提案なし(指名鮮度切れ 13営業日)
- 2594 Key Coffee Inc. — ⛔提案なし(指名鮮度切れ 11営業日)
- 7649 Sugi Holdings Co., Ltd. — ⛔提案なし(指名鮮度切れ 13営業日)
- 2702 日本マクドナルド HD — ⛔提案なし(指名鮮度切れ 19営業日)
- 1605 Inpex Corporation — ⛔提案なし(指名鮮度切れ 17営業日)
- 7679 Yakuodo Holdings Co., Ltd. — ⛔提案なし(指名鮮度切れ 12営業日)
- 2282 NH Foods Limited — ⛔提案なし(指名鮮度切れ 11営業日)
- 2292 S Foods Inc. — ⛔提案なし(指名鮮度切れ 16営業日)
- 4480 Medley, Inc. — ⛔型不一致: 既に支持帯以下
- 3034 Qol Holdings Co., Ltd. — ⛔型不一致: 既に支持帯以下
- 1375 Yukiguni Factory Co., Ltd. — ⛔提案なし(指名鮮度切れ 13営業日)
- 9861 Yoshinoya Holdings Co., Ltd. — ⛔提案なし(指名鮮度切れ 12営業日)
- 2001 NIPPN Corporation — ⛔提案なし(指名鮮度切れ 13営業日)
- 2810 ハウス食品グループ本社 — ⛔提案なし(指名鮮度切れ 15営業日)
- 7860 Avex Inc. — ⛔提案なし(指名鮮度切れ 16営業日)
- 9006 Keikyu Corporation — ⛔提案なし(指名鮮度切れ 13営業日)
- 3191 Joyful Honda Co. Ltd. — ⛔提案なし(指名鮮度切れ 12営業日)
- 7459 MEDIPAL HOLDINGS Corporation — ⛔提案なし(指名鮮度切れ 13営業日)
- 1878 Daito Trust Construction Co., Ltd. — ⛔提案なし(指名鮮度切れ 12営業日)
- 9735 Secom Co., Ltd. — ⛔提案なし(指名鮮度切れ 13営業日)
- 479A PRONI INC — ⛔提案なし(指名鮮度切れ 15営業日)
- 7695 交換できるくん — ⛔提案なし(指名鮮度切れ 11営業日)
- 9010 Fuji Kyuko Co., Ltd. — ⛔型不一致: 既に支持帯以下

## 5手法銘柄
- 3131 シンデンハイ｜stf_kakuhen｜🚀確変12/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値6,360円｜💰663,000円｜[—]｜
- 5137 Smart Drive Co. Ltd.｜kenmo_momentum｜🚀確変12/13｜🟢値頃5.0/7｜FAIL_UWAHIGE｜終値309円｜💰32,400円｜[—]｜
- 6278 ユニオンツール｜choruko_reversal｜🚀確変12/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値13,000円｜💰1,343,000円｜[—]｜
- 3851 Nippon Ichi Software, Inc.｜kenmo_newhigh｜🚀確変12/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値1,504円｜💰148,500円｜[—]｜
- 3556 RenetJapanGroup, Inc.｜kenmo_momentum｜🚀確変11/13｜💎割安6.0/7｜FAIL_UWAHIGE｜終値805円｜💰80,400円｜[—]｜
- 4099 SHIKOKU KASEI HOLDINGS CORPORATION｜choruko_reversal｜🚀確変11/13｜💎割安6.0/7｜FAIL_INSEN｜終値2,079円｜💰221,500円｜[—]｜
- 3441 Sanno Co., Ltd.｜kenmo_momentum｜🚀確変11/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値2,775円｜💰288,900円｜[—]｜
- 5136 tripla Co., Ltd.｜kenmo_momentum｜🚀確変11/13｜⚪妥当4.0/7｜PASS｜終値2,001円｜💰200,100円｜逆指値2008 SL1886.58｜
  > 📌ヘッドライン
  > 【業態】宿泊予約システムや会話ツールのAIチャットボットシステム提供。決済システムも。アジアに拡大。
  > 【いま】終値2,001円・直近5日-1.33%（材料未確認）
  > 【調子】🚀確変（11/13）
  > 【水準】⚪妥当（4.0/7）— PER19.8倍・PEG0.34・52週75% ／ 💰単元20.0万円
  > 【戦略】当日高値超えの逆指値2008円で順張り参戦を検討。上限2028.08円・SL1886.58円目安
- 5586 Laboro.AI, Inc.｜kenmo_momentum｜🚀確変11/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値933円｜💰94,200円｜[—]｜
- 5724 Asaka Riken Co., Ltd.｜kenmo_momentum｜🚀確変11/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値3,100円｜💰319,000円｜[—]｜
- 269A ＳＡＰＥＥＴ｜kenmo_newhigh｜🚀確変11/13｜⚪妥当3.0/7｜FAIL_UWAHIGE｜終値2,890円｜💰283,600円｜[—]｜
- 3723 Nihon Falcom Corporation｜kenmo_momentum｜🚀確変11/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値2,660円｜💰272,400円｜[—]｜
- 5027 AnyMind Group Inc.｜kenmo_momentum｜🚀確変11/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値723円｜💰74,800円｜[—]｜
- 3391 TSURUHA Holdings, Inc.｜choruko_reversal｜🔥絶好調10/13｜🟢値頃5.6/7｜PASS｜終値2,341円｜💰234,100円｜指値2341 SL2222｜
  > 📌ヘッドライン
  > 【業態】ドラッグストア大手。25年12月ウエルシアHDと経営統合。イオンが子会社化へ。
  > 【いま】終値2,341円・直近5日+3.91%（材料未確認）
  > 【調子】🔥絶好調（10/13）
  > 【水準】🟢値頃（5.6/7）— PER25.6倍・PEG0.46・52週41% ／ 💰単元23.4万円
  > 【戦略】当日終値2341円の指値で反転を取りにいく。SL2222円（直近5日安値）
- 4047 関東電化工業｜choruko_reversal｜🔥絶好調10/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値2,134円｜💰223,400円｜[—]｜
- 4971 MEC Company Ltd.｜choruko_reversal｜🔥絶好調10/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値6,110円｜💰655,000円｜[—]｜
- 9270 Valuence Holdings, Inc.｜kenmo_momentum｜🔥絶好調10/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値2,013円｜💰205,500円｜[—]｜
- 9341 GENOVA Inc.｜kenmo_momentum｜🔥絶好調10/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値612円｜💰62,800円｜[—]｜
- 5246 ELEMENTS,Inc.｜kenmo_momentum｜🔥絶好調10/13｜⚪妥当4.0/7｜FAIL_UWAHIGE｜終値821円｜💰80,800円｜[—]｜
- 6516 山洋電気｜choruko_reversal｜🔥絶好調10/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値5,070円｜💰532,000円｜[—]｜
- 9554 AViC Co. Ltd.｜kenmo_momentum｜🔥絶好調10/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値1,730円｜💰173,600円｜[—]｜
- 9824 泉州電業｜stf_kakuhen｜🔥絶好調10/13｜⚪妥当4.0/7｜FAIL_UWAHIGE｜終値7,910円｜💰738,000円｜[—]｜
- 421A Movin' Strategic Career CO.,LTD.｜kenmo_momentum｜🔥絶好調10/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値3,815円｜💰400,000円｜[—]｜
- 1435 robot home Inc.｜kenmo_momentum｜🔥絶好調9/13｜💎割安7.0/7｜FAIL_INSEN｜終値178円｜💰17,900円｜[—]｜
- 3465 ケイアイスター不動産｜choruko_reversal｜🔥絶好調9/13｜💎割安6.0/7｜FAIL_INSEN｜終値3,250円｜💰327,500円｜[—]｜
- 6103 Okuma Corporation｜choruko_reversal｜🔥絶好調9/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値4,320円｜💰463,000円｜[—]｜
- 6298 ワイエイシイホールディングス｜kenmo_momentum｜🔥絶好調9/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値1,310円｜💰136,000円｜[—]｜
- 6481 THK Co., Ltd.｜choruko_reversal｜🔥絶好調9/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値6,050円｜💰650,800円｜[—]｜
- 4377 ONE CAREER Inc.｜kenmo_momentum｜🔥絶好調9/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値2,279円｜💰246,900円｜[—]｜
- 4479 Makuake, Inc.｜kenmo_momentum｜🔥絶好調9/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値962円｜💰100,700円｜[—]｜
- 4627 ナトコ｜stf_kakuhen｜🔥絶好調9/13｜⚪妥当4.0/7｜FAIL_UWAHIGE｜終値1,872円｜💰194,000円｜[—]｜
- 6268 Nabtesco Corporation｜choruko_reversal｜🔥絶好調9/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値4,337円｜💰445,700円｜[—]｜
- 7433 伯東｜stf_kakuhen｜🔥絶好調9/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値5,190円｜💰528,000円｜[—]｜
- 9279 ギフトホールディングス｜choruko_reversal｜🔥絶好調9/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値2,289円｜💰237,300円｜[—]｜
- 5537 AlbaLink Co.,Ltd.｜kenmo_momentum｜🔥絶好調9/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値3,290円｜💰351,000円｜[—]｜
- 8086 ニプロ｜choruko_reversal｜🔥絶好調8/13｜💎割安6.0/7｜PASS｜終値1,460円｜💰146,000円｜指値1460 SL1437｜
  > 📌ヘッドライン
  > 【業態】使い捨て医療器具大手。人工腎臓に強み。後発医薬品・受託を強化。
  > 【いま】終値1,460円・直近5日-5.99%（材料未確認）
  > 【調子】🔥絶好調（8/13）
  > 【水準】💎割安（6.0/7）— PER15.9倍・PEG0.41・52週16% ／ 💰単元14.6万円
  > 【戦略】当日終値1460円の指値で反転を取りにいく。SL1437円（直近5日安値）
- 6235 オプトラン｜choruko_reversal｜🔥絶好調8/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値2,450円｜💰250,600円｜[—]｜
- 7352 TWOSTONE&Sons Co.Ltd.｜kenmo_momentum｜🔥絶好調8/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値324円｜💰32,600円｜[—]｜
- 2334 Eole, Inc.｜kenmo_momentum｜🔥絶好調8/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値575円｜💰57,400円｜[—]｜
- 3109 Shikibo Ltd.｜kenmo_momentum｜🔥絶好調8/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値1,044円｜💰105,800円｜[—]｜
- 3915 TerraSky Co., Ltd.｜kenmo_momentum｜🔥絶好調8/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値2,314円｜💰247,400円｜[—]｜
- 4368 Fuso Chemical Co., Ltd.｜choruko_reversal｜🔥絶好調8/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値2,815円｜💰294,500円｜[—]｜
- 5574 ABEJA,Inc.｜kenmo_momentum｜🔥絶好調8/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値2,968円｜💰307,500円｜[—]｜
- 5582 GRID Inc.｜kenmo_momentum｜🔥絶好調8/13｜⚪妥当4.0/7｜FAIL_UWAHIGE｜終値2,148円｜💰195,200円｜[—]｜
- 4186 東京応化工業｜choruko_reversal｜🔥絶好調8/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値8,104円｜💰827,600円｜[—]｜
- 6630 YA-MAN Ltd.｜kenmo_momentum｜🔥絶好調8/13｜⚪妥当3.0/7｜PASS｜終値801円｜💰80,100円｜[—]｜
  > 📌ヘッドライン
  > 【業態】美顔・痩身器具など美容健康機器の製造・販売。量販店と通販が主力。
  > 【いま】終値801円・直近5日-1.60%（材料未確認）
  > 【調子】🔥絶好調（8/13）
  > 【水準】⚪妥当（3.0/7）— PER125.2倍・PEG0.70・52週77% ／ 💰単元8.0万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 13営業日)）
- 7729 東京精密｜choruko_reversal｜🔥絶好調8/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値16,685円｜💰1,685,000円｜[—]｜
- 135A VRAIN Solution,Inc.｜kenmo_momentum｜🔥絶好調8/13｜🟡やや割高2.0/7｜FAIL_UWAHIGE｜終値4,520円｜💰432,000円｜[—]｜
- 146A コロンビア・ワークス｜kenmo_momentum｜⚡好調7/13｜💎割安6.0/7｜FAIL_UWAHIGE｜終値3,760円｜💰371,500円｜[—]｜
- 5892 yutori,Inc.｜kenmo_momentum｜⚡好調7/13｜💎割安6.0/7｜FAIL_INSEN｜終値2,411円｜💰255,300円｜[—]｜
- 8927 Meiho Enterprise Co., Ltd.｜kenmo_momentum｜⚡好調7/13｜💎割安6.0/7｜FAIL_INSEN｜終値484円｜💰48,600円｜[—]｜
- 3104 富士紡ホールディングス｜choruko_reversal｜⚡好調7/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値3,280円｜💰339,000円｜[—]｜
- 5590 ネットスターズ｜kenmo_momentum｜⚡好調7/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値729円｜💰72,500円｜[—]｜
- 6941 山一電機｜choruko_reversal｜⚡好調7/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値7,210円｜💰773,000円｜[—]｜
- 4058 Toyokumo, Inc.｜kenmo_momentum｜⚡好調7/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値2,300円｜💰244,500円｜[—]｜
- 5938 LIXIL Corporation｜choruko_reversal｜⚡好調7/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値1,744.5円｜💰175,850円｜[—]｜
- 6071 IBJ, Inc.｜kenmo_momentum｜⚡好調7/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値853円｜💰93,500円｜[—]｜
- 6856 Horiba, Ltd.｜choruko_reversal｜⚡好調7/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値21,610円｜💰2,255,000円｜[—]｜
- 7409 AeroEdge Co.,Ltd｜kenmo_momentum｜⚡好調7/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値1,510円｜💰155,900円｜[—]｜
- 4187 大阪有機化学工業｜choruko_reversal｜⚡好調7/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値4,135円｜💰439,000円｜[—]｜
- 6370 Kurita Water Industries Ltd.｜choruko_reversal｜⚡好調7/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値7,499円｜💰783,300円｜[—]｜
- 6754 アンリツ｜choruko_reversal｜⚡好調7/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値3,085円｜💰325,100円｜[—]｜
- 558A SQUEEZE Inc.｜kenmo_momentum｜⚡好調7/13｜🟡やや割高2.8/7｜FAIL_INSEN｜終値5,610円｜💰588,000円｜[—]｜
- 147A ソラコム｜stf_kakuhen｜⚡好調7/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値985円｜💰99,500円｜[—]｜
- 3288 オープンハウスグループ｜choruko_reversal｜⚡好調6/13｜💎割安7.0/7｜PASS_DOJI｜終値7,596円｜💰759,600円｜指値7596 SL7521｜
  > 📌ヘッドライン
  > 【業態】首都圏中心に不動産事業を展開。狭小地の戸建てに強み。マンション分譲も。
  > 【いま】終値7,596円・直近5日-5.24%（材料未確認）
  > 【調子】⚡好調（6/13）
  > 【水準】💎割安（7.0/7）— PER7.0倍・PEG0.32・52週9% ／ 💰単元76.0万円
  > 【戦略】当日終値7596円の指値で反転を取りにいく。SL7521円（直近5日安値）
- 5991 日本発條｜choruko_reversal｜⚡好調6/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値3,261円｜💰332,700円｜[—]｜
- 6622 ダイヘン｜choruko_reversal｜⚡好調6/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値12,110円｜💰1,299,000円｜[—]｜
- 3064 ＭＯＮＯＴＡＲＯ｜choruko_reversal｜⚡好調6/13｜⚪妥当3.0/7｜PASS｜終値1,963円｜💰196,300円｜指値1963 SL1838.5｜
  > 📌ヘッドライン
  > 【業態】米系、作業場向け間接資材をネット通販。小規模業者に低価格と品揃えが強み。
  > 【いま】終値1,963円・直近5日+3.21%（材料未確認）
  > 【調子】⚡好調（6/13）
  > 【水準】⚪妥当（3.0/7）— PER26.7倍・PEG1.82・52週30% ／ 💰単元19.6万円
  > 【戦略】当日終値1963円の指値で反転を取りにいく。SL1838.5円（直近5日安値）
- 4477 BASE, Inc.｜kenmo_momentum｜⚡好調6/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値339円｜💰34,700円｜[—]｜
- 6504 Fuji Electric Co., Ltd.｜choruko_reversal｜⚡好調6/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値12,760円｜💰1,339,500円｜[—]｜
- 6544 Japan Elevator Service Holdings Co., Ltd.｜choruko_reversal｜⚡好調6/13｜⚪妥当3.0/7｜FAIL_UWAHIGE｜終値1,473円｜💰147,150円｜[—]｜
- 7944 Roland Corporation｜choruko_reversal｜⚡好調6/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値3,675円｜💰383,500円｜[—]｜
- 9412 スカパーＪＳＡＴ｜choruko_reversal｜⚡好調6/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値2,010円｜💰203,300円｜[—]｜
- 5333 ＮＧＫ｜choruko_reversal｜⚡好調6/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値5,025円｜💰524,400円｜[—]｜
- 6806 ヒロセ電機｜choruko_reversal｜⚡好調6/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値23,735円｜💰2,499,500円｜[—]｜
- 7581 Saizeriya Co., Ltd.｜choruko_reversal｜⚡好調6/13｜🟡やや割高2.0/7｜PASS｜終値7,480円｜💰748,000円｜指値7480 SL6810｜
  > 📌ヘッドライン
  > 【業態】イタリアンレストラン「サイゼリヤ」を直営展開。低価格メニューに特色。中国展開に注力。
  > 【いま】終値7,480円・直近5日+6.55%（材料未確認）
  > 【調子】⚡好調（6/13）
  > 【水準】🟡やや割高（2.0/7）— PER31.2倍・PEG1.97・52週75% ／ 💰単元74.8万円
  > 【戦略】当日終値7480円の指値で反転を取りにいく。SL6810円（直近5日安値）／⚠1単元でリスク枠超過（67000円）
- 428A Cypress Holdings Co. Ltd.｜kenmo_newhigh｜⚡好調6/13｜🔴過熱0.0/7｜PASS｜終値1,580円｜💰158,000円｜逆指値1582 SL1486.14｜
  > 📌ヘッドライン
  > 【業態】「築地食堂源ちゃん」などの飲食事業やグループ会社の経営管理を手掛ける。
  > 【いま】終値1,580円・直近5日+6.11%（材料未確認）
  > 【調子】⚡好調（6/13）
  > 【水準】🔴過熱（0.0/7）— PER38.7倍・PEG2.56・52週97% ／ 💰単元15.8万円
  > 【戦略】当日高値超えの逆指値1582円で順張り参戦を検討。上限1597.82円・SL1486.14円目安
- 2266 Rokko Butter Co., Ltd.｜kenmo_momentum｜⚡好調5/13｜💎割安6.0/7｜PASS｜終値1,109円｜💰110,900円｜逆指値1114 SL1046.22｜
  > 📌ヘッドライン
  > 【業態】ベビーチーズで首位。QBBブランドが主力。輸入ナッツ加工品も。三菱商事と親密。
  > 【いま】終値1,109円・直近5日-4.48%（材料未確認）
  > 【調子】⚡好調（5/13）
  > 【水準】💎割安（6.0/7）— PER14.6倍・PEG0.71・52週32% ／ 💰単元11.1万円
  > 【戦略】当日高値超えの逆指値1114円で順張り参戦を検討。上限1125.14円・SL1046.22円目安
- 7202 Isuzu Motors Limited｜choruko_reversal｜⚡好調5/13｜💎割安6.0/7｜FAIL_INSEN｜終値2,129.5円｜💰222,250円｜[—]｜
- 7972 ITOKI Corporation｜choruko_reversal｜⚡好調5/13｜💎割安6.0/7｜FAIL_INSEN｜終値2,485円｜💰252,900円｜[—]｜
- 5444 Yamato Kogyo Co., Ltd.｜choruko_reversal｜⚡好調5/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値12,030円｜💰1,241,500円｜[—]｜
- 6728 アルバック｜choruko_reversal｜⚠減速5/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値7,030円｜💰721,000円｜[—]｜
- 9560 PROGRIT, Inc.｜kenmo_momentum｜⚡好調5/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値872円｜💰92,000円｜[—]｜
- 6013 タクマ｜choruko_reversal｜⚡好調5/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値2,965円｜💰301,000円｜[—]｜
- 6113 アマダホールディングス｜choruko_reversal｜⚡好調5/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値2,397円｜💰256,250円｜[—]｜
- 6707 サンケン電気｜choruko_reversal｜⚡好調5/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値6,771円｜💰680,500円｜[—]｜
- 268A Rigaku Holdings Corporation｜choruko_reversal｜⚡好調5/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値1,607円｜💰162,500円｜[—]｜
- 6383 ダイフク｜choruko_reversal｜⚡好調5/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値5,545円｜💰566,100円｜[—]｜
- 186A アストロスケールホールディングス｜choruko_reversal｜⚡好調5/13｜🟡やや割高2.8/7｜FAIL_INSEN｜終値1,054円｜💰104,700円｜[—]｜
- 4091 日本酸素ホールディングス｜choruko_reversal｜⚡好調5/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値5,367円｜💰547,100円｜[—]｜
- 4973 Japan Pure Chemical Co., Ltd.｜kenmo_momentum｜⚡好調5/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値4,735円｜💰473,000円｜[—]｜
- 3798 ＵＬＳグループ｜kenmo_momentum｜✅順調4/13｜💎割安6.0/7｜FAIL_INSEN｜終値534円｜💰54,900円｜[—]｜
- 7649 Sugi Holdings Co., Ltd.｜choruko_reversal｜✅順調4/13｜💎割安6.0/7｜PASS｜終値1,323円｜💰132,300円｜[—]｜
  > 📌ヘッドライン
  > 【業態】中部地盤にドラッグストア「スギ薬局」をチェーン展開。調剤薬局併設店に強み。
  > 【いま】終値1,323円・直近5日+0.42%（材料未確認）
  > 【調子】✅順調（4/13）
  > 【水準】💎割安（6.0/7）— PER7.5倍・PEG0.76・52週6% ／ 💰単元13.2万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 13営業日)）
- 277A Globe-Ing, Inc.｜kenmo_momentum｜✅順調4/13｜🟢値頃5.0/7｜FAIL_UWAHIGE｜終値1,907円｜💰190,100円｜[—]｜
- 505A Geekly,Inc.｜kenmo_momentum｜✅順調4/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値1,388円｜💰143,500円｜[—]｜
- 2579 Coca-Cola Bottlers Japan Holdings Inc.｜choruko_reversal｜✅順調4/13｜⚪妥当4.0/7｜FAIL_UWAHIGE｜終値3,806円｜💰379,500円｜[—]｜
- 5038 eWeLL Co.,Ltd｜kenmo_momentum｜✅順調4/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値2,151円｜💰215,600円｜[—]｜
- 9467 Alphapolis Co., Ltd.｜kenmo_momentum｜✅順調4/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値1,108円｜💰113,900円｜[—]｜
- 1812 Kajima Corporation｜choruko_reversal｜⚠減速4/13｜⚪妥当3.0/7｜FAIL_UWAHIGE｜終値5,062円｜💰493,800円｜[—]｜
- 341A TOYOKOH Inc.｜kenmo_momentum｜✅順調4/13｜⚪妥当3.0/7｜FAIL_UWAHIGE｜終値2,226円｜💰211,000円｜[—]｜
- 9065 Sankyu Inc.｜choruko_reversal｜✅順調4/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値8,000円｜💰810,000円｜[—]｜
- 6996 Nichicon Corporation｜choruko_reversal｜✅順調4/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値2,474円｜💰268,400円｜[—]｜
- 7966 Lintec Corporation｜choruko_reversal｜✅順調4/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値5,110円｜💰548,000円｜[—]｜
- 5334 Niterra Co.,Ltd.｜choruko_reversal｜✅順調4/13｜🔴過熱1.0/7｜FAIL_INSEN｜終値7,444円｜💰808,200円｜[—]｜
- 6925 ウシオ電機｜choruko_reversal｜✅順調4/13｜🔴過熱1.0/7｜FAIL_INSEN｜終値3,623円｜💰367,000円｜[—]｜
- 8139 Nagahori Corporation｜kenmo_momentum｜🔻悪化4/13｜🔴過熱1.0/7｜FAIL_INSEN｜終値2,191円｜💰219,800円｜[—]｜
- 1861 Kumagai Gumi Co., Ltd.｜choruko_reversal｜✅順調3/13｜💎割安6.0/7｜FAIL_UWAHIGE｜終値1,300円｜💰130,000円｜[—]｜
- 3433 TOCALO Co., Ltd.｜choruko_reversal｜✅順調3/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値2,756円｜💰278,200円｜[—]｜
- 8537 大光銀行｜kenmo_newhigh｜⚠減速3/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値3,090円｜💰315,500円｜[—]｜
- 1802 Obayashi Corporation｜choruko_reversal｜✅順調3/13｜⚪妥当3.0/7｜FAIL_UWAHIGE｜終値3,050円｜💰301,100円｜[—]｜
- 6323 ローツェ｜choruko_reversal｜✅順調3/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値3,655円｜💰375,000円｜[—]｜
- 7701 島津製作所｜choruko_reversal｜✅順調3/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値3,766円｜💰384,600円｜[—]｜
- 6586 Makita Corporation｜choruko_reversal｜✅順調3/13｜🔴過熱1.0/7｜FAIL_INSEN｜終値5,201円｜💰524,700円｜[—]｜
- 2264 森永乳業｜choruko_reversal｜➖横ばい2/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値1,116.5円｜💰110,000円｜[—]｜
- 6674 ジーエス・ユアサ　コーポレーション｜choruko_reversal｜➖横ばい2/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値4,981円｜💰496,100円｜[—]｜
- 6368 Organo Corp.｜choruko_reversal｜➖横ばい2/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値12,415円｜💰1,274,000円｜[—]｜
- 6617 TAKAOKA TOKO CO., LTD.｜choruko_reversal｜➖横ばい2/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値6,500円｜💰703,000円｜[—]｜
- 6841 横河電機｜choruko_reversal｜➖横ばい2/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値4,518円｜💰472,400円｜[—]｜
- 7220 Musashi Seimitsu Industry Co., Ltd.｜choruko_reversal｜🔻悪化2/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値2,684円｜💰292,600円｜[—]｜
- 7532 パン・パシフィック・インターナショナルホールディングス｜choruko_reversal｜➖横ばい2/13｜🟡やや割高2.0/7｜PASS｜終値777.7円｜💰77,770円｜指値777.7 SL747｜
  > 📌ヘッドライン
  > 【業態】総合ディスカウント「ドンキ」主力に総合スーパーのユニー、長崎屋など。アジア出店を加速。
  > 【いま】終値777円・直近5日+0.14%（材料未確認）
  > 【調子】➖横ばい（2/13） — 質注意
  > 【水準】🟡やや割高（2.0/7）— PER21.2倍・PEG—・52週8% ／ 💰単元7.8万円
  > 【戦略】当日終値777.7円の指値で反転を取りにいく。SL747円（直近5日安値）
- 1960 サンテック｜kenmo_newhigh｜➖横ばい2/13｜🔴過熱1.0/7｜FAIL_INSEN｜終値1,693円｜💰172,900円｜[—]｜
- 2594 Key Coffee Inc.｜kenmo_momentum｜🔻悪化2/13｜🔴過熱1.0/7｜PASS｜終値2,026円｜💰202,600円｜[—]｜
  > 📌ヘッドライン
  > 【業態】レギュラーコーヒー大手。業務用主体。インドネシアに直営農園。イタリアントマトを運営。
  > 【いま】終値2,026円・直近5日-0.44%（材料未確認）
  > 【調子】🔻悪化（2/13） — 質注意
  > 【水準】🔴過熱（1.0/7）— PER57.9倍・PEG—・52週70% ／ 💰単元20.3万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 11営業日)）
- 4061 デンカ｜choruko_reversal｜➖横ばい2/13｜🔴過熱1.0/7｜FAIL_INSEN｜終値3,219円｜💰324,500円｜[—]｜
- 9247 TRE HOLDINGS CORPORATION｜choruko_reversal｜🔻悪化2/13｜🔴過熱1.0/7｜PASS_DOJI｜終値1,810円｜💰181,000円｜指値1810 SL1758｜
  > 📌ヘッドライン
  > 【業態】廃棄物処理・リサイクルが主力。タケエイとリバーHDが経営統合。バイオマス発電も注力。
  > 【いま】終値1,810円・直近5日-6.46%（材料未確認）
  > 【調子】🔻悪化（2/13） — 質注意
  > 【水準】🔴過熱（1.0/7）— PER20.8倍・PEG—・52週46% ／ 💰単元18.1万円
  > 【戦略】当日終値1810円の指値で反転を取りにいく。SL1758円（直近5日安値）
- 6479 ミネベア｜choruko_reversal｜⚠減速1/13｜💎割安6.0/7｜FAIL_INSEN｜終値3,326円｜💰346,800円｜[—]｜
- 5105 Toyo Tire Corporation｜choruko_reversal｜⚠減速1/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値3,528円｜💰372,200円｜[—]｜
- 8111 Goldwin Inc.｜choruko_reversal｜⚠減速1/13｜⚪妥当3.0/7｜FAIL_UWAHIGE｜終値2,107.5円｜💰211,300円｜[—]｜
- 5332 ＴＯＴＯ｜choruko_reversal｜⚠減速1/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値5,804円｜💰600,700円｜[—]｜
- 6951 日本電子｜choruko_reversal｜⚠減速1/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値6,829円｜💰706,300円｜[—]｜
- 6845 Azbil Corporation｜choruko_reversal｜⚠減速1/13｜🔴過熱1.0/7｜FAIL_INSEN｜終値1,451円｜💰148,600円｜[—]｜
- 6804 ホシデン｜choruko_reversal｜🔻悪化0/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値2,542円｜💰263,000円｜[—]｜
- 276A CCReB Advisors Inc.｜kenmo_momentum｜判定保留｜🟢値頃5.0/7｜FAIL_UWAHIGE｜終値4,165円｜💰389,500円｜[—]｜
- 6101 ツガミ｜choruko_reversal｜業績データ取得不可｜🟢値頃5.0/7｜FAIL_INSEN｜終値4,850円｜💰529,000円｜[—]｜
- 6862 Minato Holdings Inc.｜kenmo_momentum｜判定保留(変則決算)｜🟢値頃5.0/7｜FAIL_INSEN｜終値4,350円｜💰463,000円｜[—]｜
- 325A TENTIAL, Inc.｜kenmo_momentum｜判定保留(変則決算)｜⚪妥当4.0/7｜FAIL_INSEN｜終値1,755円｜💰175,500円｜[—]｜
- 6492 Okano Valve Mfg. Co., Ltd.｜kenmo_momentum｜判定保留(変則決算)｜⚪妥当4.0/7｜FAIL_INSEN｜終値14,150円｜💰1,452,000円｜[—]｜
- 7161 Jimoto Holdings, Inc.｜kenmo_newhigh｜業績データ取得不可｜⚪妥当3.0/7｜FAIL_INSEN｜終値598円｜💰62,200円｜[—]｜
- 4894 Cuorips Inc.｜kenmo_momentum｜判定保留｜🔴過熱2.8/7｜FAIL_UWAHIGE｜終値5,420円｜💰537,000円｜[—]｜
- 5344 MARUWA CO., LTD.｜choruko_reversal｜業績データ取得不可｜🟡やや割高2.0/7｜FAIL_INSEN｜終値56,140円｜💰5,847,000円｜[—]｜
- 3932 Akatsuki, Inc.｜kenmo_momentum｜—｜⏸判定不能｜FAIL_INSEN｜終値3,480円｜💰368,500円｜[—]｜
- 4599 StemRIM Inc.｜kenmo_newhigh｜取得不可｜⏸判定不能｜FAIL_UWAHIGE｜終値330円｜💰33,100円｜[—]｜
- 6141 DMG MORI CO., LTD.｜choruko_reversal｜取得不可｜⏸判定不能｜FAIL_INSEN｜終値2,758円｜💰287,750円｜[—]｜
- 6838 Tamagawa Holdings Co., Ltd.｜kenmo_momentum｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜終値1,516円｜💰155,100円｜[—]｜
- 7157 ライフネット生命保険｜choruko_reversal｜業績データ取得不可(経常益予想非開示)｜⏸判定不能｜FAIL_UWAHIGE｜終値1,415円｜💰145,100円｜[—]｜
- 7678 ASAKUMA CO.,LTD.｜kenmo_momentum｜—｜—｜FAIL_UWAHIGE｜終値3,295円｜💰—円｜[—]｜
- 7774 ジャパン・ティッシュエンジニアリング｜kenmo_newhigh｜—｜—｜FAIL_UWAHIGE｜終値912円｜💰—円｜[—]｜
- 8614 Toyo Securities Co., Ltd.｜kenmo_momentum｜業績データ取得不可｜⏸判定不能｜FAIL_UWAHIGE｜終値736円｜💰74,200円｜[—]｜

## グランビル銘柄
- 6134 富士機械製造｜granville_rebound｜🚀確変11/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値6,690円｜💰688,600円｜[—]｜
- 3753 フライトソリューションズ｜granville_rebound｜🚀確変11/13｜⚪妥当4.0/7｜FAIL_UWAHIGE｜終値220円｜💰21,600円｜[—]｜
- 7806 MTG Co., Ltd.｜granville_oshime｜🚀確変11/13｜⚪妥当3.0/7｜FAIL_UWAHIGE｜終値8,230円｜💰840,000円｜[—]｜
- 145A L is B Corp.｜granville_tenkan｜🔥絶好調10/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値893円｜💰90,900円｜[—]｜
- 2693 YKT Corporation｜granville_rebound｜🔥絶好調10/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値280円｜💰28,100円｜[—]｜
- 2760 東京エレクトロン　デバイス｜granville_oshime｜🔥絶好調10/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値3,955円｜💰411,500円｜[—]｜
- 6264 マルマエ｜granville_rebound｜🔥絶好調10/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値1,933円｜💰192,700円｜[—]｜
- 6997 Nippon Chemi-Con Corporation｜granville_rebound｜🔥絶好調10/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値2,628円｜💰287,200円｜[—]｜
- 212A フィットイージー｜granville_oshime｜🔥絶好調10/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値2,938円｜💰294,400円｜[—]｜
- 6136 オーエスジー｜granville_oshime｜🔥絶好調10/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値3,425円｜💰360,000円｜[—]｜
- 6407 CKD Corporation｜granville_rebound｜🔥絶好調10/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値5,050円｜💰552,000円｜[—]｜
- 2986 LA Holdings Co.,Ltd｜granville_tenkan｜🔥絶好調9/13｜💎割安7.0/7｜FAIL_INSEN｜終値2,803円｜💰282,900円｜[—]｜
- 3168 MERF Inc.｜granville_rebound｜🔥絶好調9/13｜💎割安6.0/7｜PASS_DOJI｜終値1,286円｜💰128,600円｜指値1286 SL1246｜
  > 📌ヘッドライン
  > 【業態】非鉄金属加工。スクラップと銅インゴット両輪。船スクリュー用首位級。美術品鋳造も。
  > 【いま】終値1,286円・直近5日-8.60%（材料未確認）
  > 【調子】🔥絶好調（9/13）
  > 【水準】💎割安（6.0/7）— PER6.5倍・PEG0.00・52週54% ／ 💰単元12.9万円
  > 【戦略】当日終値1286円の指値で反転を取りにいく。SL1246円（直近5日安値）
- 3498 霞ヶ関キャピタル｜granville_oshime｜🔥絶好調9/13｜💎割安6.0/7｜FAIL_UWAHIGE｜終値7,380円｜💰748,000円｜[—]｜
- 9211 エフ・コード｜granville_tenkan｜🔥絶好調9/13｜💎割安6.0/7｜FAIL_INSEN｜終値1,427円｜💰145,500円｜[—]｜
- 9880 Innotech Corporation｜granville_rebound｜🔥絶好調9/13｜💎割安6.0/7｜FAIL_INSEN｜終値3,275円｜💰350,000円｜[—]｜
- 3449 Technoflex Corporation｜granville_rebound｜🔥絶好調9/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値3,965円｜💰413,000円｜[—]｜
- 4382 HEROZ, Inc.｜granville_tenkan｜🔥絶好調9/13｜🟢値頃5.0/7｜FAIL_UWAHIGE｜終値764円｜💰75,100円｜[—]｜
- 6914 オプテックス｜granville_rebound｜🔥絶好調9/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値3,000円｜💰313,000円｜[—]｜
- 6976 Taiyo Yuden Co., Ltd.｜granville_rebound｜🔥絶好調9/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値9,046円｜💰982,400円｜[—]｜
- 3036 アルコニックス｜granville_oshime｜🔥絶好調9/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値3,330円｜💰337,500円｜[—]｜
- 3663 セルシス｜granville_oshime｜🔥絶好調9/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値1,768円｜💰183,400円｜[—]｜
- 4521 Kaken Pharmaceutical Co., Ltd.｜granville_tenkan｜🔥絶好調9/13｜⚪妥当4.0/7｜PASS｜終値3,905円｜💰390,500円｜逆指値3916 SL3680.1｜
  > 📌ヘッドライン
  > 【業態】製薬の中堅。関節機能改善剤、爪白癬症薬が主力。後発医薬品、農薬も展開。
  > 【いま】終値3,905円・直近5日-2.62%（材料未確認）
  > 【調子】🔥絶好調（9/13）
  > 【水準】⚪妥当（4.0/7）— PER22.8倍・PEG0.01・52週40% ／ 💰単元39.0万円
  > 【戦略】当日高値超えの逆指値3916円で順張り参戦を検討。上限3955.16円・SL3680.1円目安
- 5703 Nippon Light Metal Holdings Co., Ltd.｜granville_tenkan｜🔥絶好調9/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値2,930円｜💰301,000円｜[—]｜
- 8151 TOYO Corporation｜granville_tenkan｜🔥絶好調9/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値1,877円｜💰189,500円｜[—]｜
- 8562 Fukushima Bank, Ltd.｜granville_tenkan｜🔥絶好調9/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値381円｜💰40,000円｜[—]｜
- 150A JSH｜granville_rebound｜🔥絶好調9/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値707円｜💰77,300円｜[—]｜
- 6981 村田製作所｜granville_rebound｜🔥絶好調9/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値7,023円｜💰762,000円｜[—]｜
- 3222 United Super Markets Holdings, Inc.｜granville_tenkan｜🔥絶好調9/13｜🔴過熱2.0/7｜PASS｜終値848円｜💰84,800円｜逆指値851 SL799｜
  > 📌ヘッドライン
  > 【業態】イオン系、首都圏の食品スーパー最大手。マルエツ、カスミ、マックスバリュ関東が統合。
  > 【いま】終値848円・直近5日+3.67%（材料未確認）
  > 【調子】🔥絶好調（9/13）
  > 【水準】🔴過熱（2.0/7）— PER1211.4倍・PEG12.69・52週33% ／ 💰単元8.5万円
  > 【戦略】当日高値超えの逆指値851円で順張り参戦を検討。上限859.51円・SL799円目安
- 7453 Ryohin Keikaku Co., Ltd.｜granville_rebound｜🔥絶好調9/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値4,136円｜💰423,800円｜[—]｜
- 4424 Amazia, Inc.｜granville_rebound｜🔥絶好調8/13｜💎割安7.0/7｜FAIL_UWAHIGE｜終値337円｜💰33,900円｜[—]｜
- 1407 West Holdings Corporation｜granville_oshime｜🔥絶好調8/13｜🟢値頃5.0/7｜FAIL_UWAHIGE｜終値2,338円｜💰236,300円｜[—]｜
- 6125 Okamoto Machine Tool Works,Ltd.｜granville_rebound｜🔥絶好調8/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値4,700円｜💰491,500円｜[—]｜
- 6222 Shima Seiki Mfg. Ltd.｜granville_tenkan｜🔥絶好調8/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値923円｜💰95,300円｜[—]｜
- 6425 Universal Entertainment Corporation｜granville_tenkan｜🔥絶好調8/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値710円｜💰76,000円｜[—]｜
- 9006 Keikyu Corporation｜granville_rebound｜🔥絶好調8/13｜🟢値頃5.0/7｜PASS｜終値1,561.5円｜💰156,150円｜[—]｜
  > 📌ヘッドライン
  > 【業態】京浜・三浦半島が地盤。品川・羽田・横浜を核に沿線再開発を推進。
  > 【いま】終値1,561円・直近5日-0.22%（材料未確認）
  > 【調子】🔥絶好調（8/13）
  > 【水準】🟢値頃（5.0/7）— PER13.7倍・PEG0.26・52週60% ／ 💰単元15.6万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 13営業日)）
- 2384 SBS Holdings Inc｜granville_oshime｜🔥絶好調8/13｜⚪妥当4.0/7｜PASS_DOJI｜終値4,975円｜💰497,500円｜指値4939.37 SL4914.8｜
  > 📌ヘッドライン
  > 【業態】総合物流会社。物流一括受託が主力。食品輸送に力。物流施設の流動化も。
  > 【いま】終値4,975円・直近5日-5.06%（材料未確認）
  > 【調子】🔥絶好調（8/13）
  > 【水準】⚪妥当（4.0/7）— PER13.6倍・PEG0.59・52週82% ／ 💰単元49.8万円
  > 【戦略】4939.37円までの押し目を指値で待つ。SL4914.8円（25日線基準）
- 2590 DyDo Group Holdings, Inc.｜granville_oshime｜🔥絶好調8/13｜⚪妥当4.0/7｜FAIL_UWAHIGE｜終値3,035円｜💰300,500円｜[—]｜
- 3623 Billing System Corporation｜granville_tenkan｜🔥絶好調8/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値1,273円｜💰128,300円｜[—]｜
- 3968 セグエグループ｜granville_tenkan｜🔥絶好調8/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値625円｜💰64,200円｜[—]｜
- 6588 Toshiba Tec Corp.｜granville_oshime｜🔥絶好調8/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値2,801円｜💰297,500円｜[—]｜
- 4480 Medley, Inc.｜granville_oshime｜🔥絶好調8/13｜⚪妥当3.0/7｜PASS｜終値2,470円｜💰247,000円｜[—]｜
  > 📌ヘッドライン
  > 【業態】医療ヘルスケア領域の人材採用システムが主力。ネット診療システムや医療情報サービスも。
  > 【いま】終値2,470円・直近5日-5.62%（材料未確認）
  > 【調子】🔥絶好調（8/13）
  > 【水準】⚪妥当（3.0/7）— PER41.4倍・PEG0.87・52週57% ／ 💰単元24.7万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 6965 Hamamatsu Photonics K.K.｜granville_rebound｜🔥絶好調8/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値2,225円｜💰235,950円｜[—]｜
- 4392 FIG｜granville_rebound｜🔥絶好調8/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値985円｜💰104,800円｜[—]｜
- 4413 ボードルア｜granville_oshime｜🔥絶好調8/13｜⏸判定不能｜FAIL_INSEN｜終値2,964円｜💰296,400円｜[—]｜
- 194A WOLVES HAND Co.,Ltd.｜granville_oshime｜⚡好調7/13｜🟢値頃5.0/7｜PASS｜終値1,895円｜💰189,500円｜指値1846.27 SL1837.08｜
  > 📌ヘッドライン
  > 【業態】動物病院を展開。一次診療から高度医療まで対応。トリミングサロンや創薬も。
  > 【いま】終値1,895円・直近5日-7.20%（材料未確認）
  > 【調子】⚡好調（7/13）
  > 【水準】🟢値頃（5.0/7）— PER14.3倍・PEG0.37・52週50% ／ 💰単元18.9万円
  > 【戦略】1846.27円までの押し目を指値で待つ。SL1837.08円（25日線基準）
- 4220 リケンテクノス｜granville_rebound｜⚡好調7/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値2,365円｜💰247,800円｜[—]｜
- 5020 ＪＸホールディングス｜granville_tenkan｜⚡好調7/13｜🟢値頃5.0/7｜FAIL_UWAHIGE｜終値1,393.5円｜💰134,550円｜[—]｜
- 8793 NEC Capital Solutions Limited｜granville_tenkan｜⚡好調7/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値4,185円｜💰418,000円｜[—]｜
- 9941 太洋物産｜granville_rebound｜⚡好調7/13｜🟢値頃5.0/7｜FAIL_UWAHIGE｜終値1,236円｜💰124,000円｜[—]｜
- 166A TASUKI Holdings Inc.｜granville_oshime｜⚡好調7/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値1,108円｜💰112,300円｜[—]｜
- 2874 横浜冷凍｜granville_oshime｜⚠減速7/13｜⚪妥当4.0/7｜FAIL_UWAHIGE｜終値2,198円｜💰216,700円｜[—]｜
- 3405 Kuraray Co., Ltd.｜granville_rebound｜⚡好調7/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値1,761円｜💰183,850円｜[—]｜
- 5186 Nitta Corporation｜granville_oshime｜⚡好調7/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値6,570円｜💰690,000円｜[—]｜
- 5932 Sankyo Tateyama, Inc.｜granville_tenkan｜⚡好調7/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値641円｜💰64,900円｜[—]｜
- 6706 電気興業｜granville_rebound｜⚡好調7/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値3,220円｜💰330,000円｜[—]｜
- 7744 ノーリツ鋼機｜granville_tenkan｜⚡好調7/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値1,970円｜💰205,500円｜[—]｜
- 9902 Nichiden Corporation｜granville_oshime｜⚡好調7/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値3,025円｜💰307,000円｜[—]｜
- 3040 Soliton Systems K.K.｜granville_oshime｜⚡好調7/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値2,291円｜💰235,500円｜[—]｜
- 4051 GMO Financial Gate, Inc.｜granville_oshime｜⚡好調7/13｜⚪妥当3.0/7｜FAIL_UWAHIGE｜終値5,950円｜💰609,000円｜[—]｜
- 4507 塩野義製薬｜granville_tenkan｜⚡好調7/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値2,897.5円｜💰290,900円｜[—]｜
- 3116 Toyota Boshoku Corp.｜granville_tenkan｜⚡好調6/13｜💎割安6.0/7｜FAIL_INSEN｜終値2,201円｜💰229,100円｜[—]｜
- 5592 Kusurinomadoguchi, Inc.｜granville_tenkan｜⚡好調6/13｜💎割安6.0/7｜FAIL_INSEN｜終値2,652円｜💰266,400円｜[—]｜
- 8011 Sanyo Shokai Ltd.｜granville_rebound｜⚡好調6/13｜💎割安6.0/7｜FAIL_INSEN｜終値1,333円｜💰142,900円｜[—]｜
- 2652 Mandarake Inc.｜granville_oshime｜⚡好調6/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値425円｜💰43,800円｜[—]｜
- 2674 Hard Off Corporation Co., Ltd.｜granville_oshime｜⚡好調6/13｜🟢値頃5.0/7｜FAIL_UWAHIGE｜終値2,583円｜💰260,700円｜[—]｜
- 2975 Star Mica Holdings Co., Ltd.｜granville_tenkan｜⚡好調6/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値1,430円｜💰149,500円｜[—]｜
- 5632 三菱製鋼｜granville_oshime｜⚡好調6/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値2,247円｜💰234,300円｜[—]｜
- 7199 Premium Group Co., Ltd.｜granville_oshime｜⚡好調6/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値2,111円｜💰211,300円｜[—]｜
- 7609 Daitron Co., Ltd.｜granville_oshime｜⚡好調6/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値3,875円｜💰413,500円｜[—]｜
- 3854 アイル｜granville_tenkan｜⚡好調6/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値2,169円｜💰244,100円｜[—]｜
- 6023 ダイハツインフィニアース｜granville_tenkan｜⚡好調6/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値3,280円｜💰337,000円｜[—]｜
- 7606 UNITED ARROWS LTD.｜granville_rebound｜⚡好調6/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値2,356円｜💰240,000円｜[—]｜
- 3048 BIC Cameras Inc.｜granville_tenkan｜⚡好調6/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値1,712.5円｜💰174,800円｜[—]｜
- 4968 荒川化学工業｜granville_oshime｜⚡好調6/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値2,016円｜💰213,900円｜[—]｜
- 4417 グローバルセキュリティエキスパート｜granville_oshime｜⚡好調6/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値4,270円｜💰444,000円｜[—]｜
- 6946 Nippon Avionics Co., Ltd.｜granville_tenkan｜⚡好調6/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値6,110円｜💰620,000円｜[—]｜
- 7716 Nakanishi Inc.｜granville_oshime｜⚡好調6/13｜🔴過熱1.0/7｜FAIL_INSEN｜終値3,050円｜💰312,500円｜[—]｜
- 7911 TOPPAN Holdings Inc.｜granville_tenkan｜⚡好調6/13｜🔴過熱1.0/7｜FAIL_INSEN｜終値5,020円｜💰524,600円｜[—]｜
- 8022 Mizuno Corporation｜granville_oshime｜⚡好調6/13｜🔴過熱1.0/7｜FAIL_INSEN｜終値4,045円｜💰413,500円｜[—]｜
- 8919 カチタス｜granville_tenkan｜⚡好調6/13｜🔴過熱1.0/7｜FAIL_INSEN｜終値3,550円｜💰361,500円｜[—]｜
- 7616 コロワイド｜granville_oshime｜⚡好調6/13｜⏸判定不能｜FAIL_INSEN｜終値2,053.5円｜💰211,000円｜[—]｜
- 2931 ユーグレナ｜granville_tenkan｜⚡好調5/13｜💎割安7.0/7｜PASS｜終値347円｜💰34,700円｜逆指値349 SL327.12｜
  > 📌ヘッドライン
  > 【業態】食料品（健康・機能性食品・化粧品・スキンケア関連）
  > 【いま】終値347円・直近5日-0.57%（材料未確認）
  > 【調子】⚡好調（5/13）
  > 【水準】💎割安（7.0/7）— PER—・PEG—・52週19% ／ 💰単元3.5万円
  > 【戦略】当日高値超えの逆指値349円で順張り参戦を検討。上限352.49円・SL327.12円目安
- 7419 Nojima Co.,Ltd.｜granville_rebound｜⚡好調5/13｜💎割安7.0/7｜FAIL_INSEN｜終値1,242円｜💰125,300円｜[—]｜
- 7120 SHINKO Inc.｜granville_rebound｜⚡好調5/13｜💎割安6.0/7｜FAIL_INSEN｜終値996円｜💰99,800円｜[—]｜
- 2780 Komehyo Holdings Co., Ltd.｜granville_oshime｜⚡好調5/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値4,730円｜💰492,000円｜[—]｜
- 4666 PARK24 Co., Ltd.｜granville_tenkan｜⚡好調5/13｜🟢値頃5.0/7｜FAIL_UWAHIGE｜終値1,980円｜💰201,600円｜[—]｜
- 6339 Sintokogio,Ltd.｜granville_tenkan｜⚠減速5/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値1,151円｜💰119,800円｜[—]｜
- 2585 LIFEDRINK COMPANY INC.｜granville_tenkan｜⚡好調5/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値1,491円｜💰154,100円｜[—]｜
- 6380 オリエンタルチエン工業｜granville_rebound｜⚡好調5/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値4,035円｜💰423,500円｜[—]｜
- 6999 Koa Corporation｜granville_rebound｜⚡好調5/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値2,109円｜💰228,100円｜[—]｜
- 7505 扶桑電通｜granville_rebound｜⚡好調5/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値2,169円｜💰217,200円｜[—]｜
- 7888 三光合成｜granville_oshime｜⚡好調5/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値888円｜💰91,400円｜[—]｜
- 8923 Tosei Corporation｜granville_oshime｜⚡好調5/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値1,699円｜💰175,100円｜[—]｜
- 4612 Nippon Paint Holdings Co., Ltd.｜granville_rebound｜⚡好調5/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値1,115円｜💰114,000円｜[—]｜
- 4674 クレスコ｜granville_oshime｜⚡好調5/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値1,780円｜💰193,200円｜[—]｜
- 5461 Chubu Steel Plate Co., Ltd.｜granville_tenkan｜⚡好調5/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値2,129円｜💰213,700円｜[—]｜
- 6571 QB Net Holdings Co., Ltd.｜granville_tenkan｜⚡好調5/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値1,282円｜💰130,800円｜[—]｜
- 7350 Okinawa Financial Group, Inc.｜granville_oshime｜⚡好調5/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値7,640円｜💰791,000円｜[—]｜
- 7721 Tokyo Keiki Inc.｜granville_oshime｜⚡好調5/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値6,920円｜💰737,000円｜[—]｜
- 9319 中央倉庫｜granville_rebound｜⚡好調5/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値1,760円｜💰179,700円｜[—]｜
- 9828 ＧＥＮＫＩ　ＧＬＯＢＡＬ　ＤＩＮＩＮＧ　ＣＯＮＣＥＰＴＳ｜granville_oshime｜⚡好調5/13｜⚪妥当3.0/7｜FAIL_UWAHIGE｜終値3,360円｜💰336,500円｜[—]｜
- 6191 エボラブルアジア｜granville_rebound｜🔻悪化5/13｜🟡やや割高2.0/7｜FAIL_UWAHIGE｜終値785円｜💰77,800円｜[—]｜
- 8005 Scroll Corporation｜granville_oshime｜⚡好調5/13｜🟡やや割高2.0/7｜FAIL_UWAHIGE｜終値1,779円｜💰179,400円｜[—]｜
- 9934 Inaba Denki Sangyo Co.,Ltd.｜granville_oshime｜⚡好調5/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値2,988.5円｜💰306,300円｜[—]｜
- 3479 TKP Corporation｜granville_oshime｜⚡好調5/13｜🔴過熱1.0/7｜FAIL_INSEN｜終値1,873円｜💰190,000円｜[—]｜
- 3480 JSB Co. Ltd.｜granville_oshime｜⚡好調5/13｜🔴過熱1.0/7｜SKIP｜終値—円｜💰894,000円｜[—]｜
- 4125 SANWAYUKA INDUSTRY CORPORATION｜granville_rebound｜⚡好調5/13｜🔴過熱1.0/7｜FAIL_INSEN｜終値3,775円｜💰384,000円｜[—]｜
- 2702 日本マクドナルド HD｜granville_tenkan｜⚠減速5/13｜🔴過熱0.0/7｜PASS｜終値8,260円｜💰826,000円｜[—]｜
  > 📌ヘッドライン
  > 【業態】世界的ハンバーガーチェーンで外食国内首位級。大都市圏中心に直営店を展開。
  > 【いま】終値8,260円・直近5日+0.85%（材料未確認）
  > 【調子】⚠減速（5/13）
  > 【水準】🔴過熱（0.0/7）— PER31.4倍・PEG4.74・52週81% ／ 💰単元82.6万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 19営業日)）
- 4258 AMIYA Corporation｜granville_oshime｜⚡好調5/13｜🔴過熱0.0/7｜PASS｜終値4,730円｜💰473,000円｜指値4530.94 SL4508.4｜
  > 📌ヘッドライン
  > 【業態】情報・通信業
  > 【いま】終値4,730円・直近5日+3.96%（材料未確認）
  > 【調子】⚡好調（5/13）
  > 【水準】🔴過熱（0.0/7）— PER44.8倍・PEG3.35・52週85% ／ 💰単元47.3万円
  > 【戦略】4530.94円までの押し目を指値で待つ。SL4508.4円（25日線基準）
- 5885 GDEP ADVANCE,Inc.｜granville_tenkan｜⚡好調5/13｜🔴過熱0.0/7｜FAIL_INSEN｜終値3,455円｜💰338,000円｜[—]｜
- 6454 Max Co., Ltd.｜granville_oshime｜⚡好調5/13｜🔴過熱0.0/7｜FAIL_INSEN｜終値1,876円｜💰188,000円｜[—]｜
- 7376 ＢＣＣ｜granville_rebound｜✅順調4/13｜💎割安7.0/7｜FAIL_UWAHIGE｜終値751円｜💰79,300円｜[—]｜
- 208A 構造計画研究所ホールディングス｜granville_tenkan｜✅順調4/13｜💎割安6.0/7｜FAIL_INSEN｜終値2,875円｜💰289,900円｜[—]｜
- 5036 Japan Business Systems, Inc.｜granville_tenkan｜✅順調4/13｜💎割安6.0/7｜FAIL_UWAHIGE｜終値1,505円｜💰154,600円｜[—]｜
- 2288 Marudai Food Co., Ltd.｜granville_oshime｜✅順調4/13｜🟢値頃5.0/7｜FAIL_UWAHIGE｜終値2,254円｜💰225,300円｜[—]｜
- 1808 Haseko Corporation｜granville_tenkan｜✅順調4/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値2,800円｜💰285,400円｜[—]｜
- 3034 Qol Holdings Co., Ltd.｜granville_oshime｜✅順調4/13｜⚪妥当4.0/7｜PASS｜終値2,270円｜💰227,000円｜[—]｜
  > 📌ヘッドライン
  > 【業態】調剤薬局大手。ローソン、ビックカメラと共同出店。子会社に第一三共エスファ。
  > 【いま】終値2,270円・直近5日-5.06%（材料未確認）
  > 【調子】✅順調（4/13）
  > 【水準】⚪妥当（4.0/7）— PER10.9倍・PEG1.00・52週60% ／ 💰単元22.7万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 4092 日本化学工業｜granville_oshime｜✅順調4/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値5,100円｜💰538,000円｜[—]｜
- 6305 Hitachi Construction Machinery Co., Ltd.｜granville_tenkan｜✅順調4/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値5,750円｜💰597,700円｜[—]｜
- 7198 SBI ARUHI Corporation｜granville_tenkan｜✅順調4/13｜⚪妥当4.0/7｜PASS｜終値840円｜💰84,000円｜逆指値843 SL791.48｜
  > 📌ヘッドライン
  > 【業態】固定金利住宅ローン「フラット35」の貸出・回収・取次業務。取扱高トップ。SBI傘下。
  > 【いま】終値840円・直近5日-0.24%（材料未確認）
  > 【調子】✅順調（4/13）
  > 【水準】⚪妥当（4.0/7）— PER17.9倍・PEG1.18・52週40% ／ 💰単元8.4万円
  > 【戦略】当日高値超えの逆指値843円で順張り参戦を検討。上限851.43円・SL791.48円目安
- 1911 Sumitomo Forestry Co., Ltd.｜granville_tenkan｜🔻悪化4/13｜⚪妥当3.0/7｜FAIL_UWAHIGE｜終値1,272.5円｜💰130,050円｜[—]｜
- 2281 Prima Meat Packers,Ltd.｜granville_tenkan｜✅順調4/13｜⚪妥当3.0/7｜PASS｜終値2,427円｜💰242,700円｜逆指値2428 SL2281.38｜
  > 📌ヘッドライン
  > 【業態】ハム業界大手。伊藤忠傘下。加工食品・総菜に注力。ウインナ主力。滝沢ハムと提携。
  > 【いま】終値2,427円・直近5日-1.50%（材料未確認）
  > 【調子】✅順調（4/13）
  > 【水準】⚪妥当（3.0/7）— PER16.3倍・PEG2.23・52週30% ／ 💰単元24.3万円
  > 【戦略】当日高値超えの逆指値2428円で順張り参戦を検討。上限2452.28円・SL2281.38円目安
- 2325 NJS Co., Ltd.｜granville_tenkan｜✅順調4/13｜⚪妥当3.0/7｜FAIL_UWAHIGE｜終値4,725円｜💰476,500円｜[—]｜
- 4022 Rasa Industries,Ltd.｜granville_oshime｜✅順調4/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値1,939円｜💰204,700円｜[—]｜
- 8750 Daiichi Life Group. Inc.｜granville_rebound｜⚠減速4/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値1,822.5円｜💰187,750円｜[—]｜
- 9069 SENKO Group Holdings Co.Ltd.｜granville_rebound｜✅順調4/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値2,217円｜💰222,550円｜[—]｜
- 3393 スターティア　｜granville_rebound｜✅順調4/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値3,020円｜💰303,500円｜[—]｜
- 4718 Waseda Academy Co., Ltd.｜granville_rebound｜✅順調4/13｜🟡やや割高2.0/7｜FAIL_UWAHIGE｜終値2,632円｜💰264,900円｜[—]｜
- 5121 藤倉ゴム工業｜granville_oshime｜✅順調4/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値2,646円｜💰271,500円｜[—]｜
- 6167 冨士ダイス｜granville_tenkan｜✅順調4/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値978円｜💰100,300円｜[—]｜
- 7276 小糸製作所｜granville_tenkan｜⚠減速4/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値2,559円｜💰269,600円｜[—]｜
- 5384 Fujimi Incorporated｜granville_rebound｜✅順調4/13｜🔴過熱1.0/7｜FAIL_INSEN｜終値3,285円｜💰332,500円｜[—]｜
- 6744 Nohmi Bosai Ltd.｜granville_rebound｜✅順調4/13｜🔴過熱1.0/7｜FAIL_INSEN｜終値4,020円｜💰418,000円｜[—]｜
- 7740 Tamron Co., Ltd.｜granville_oshime｜✅順調4/13｜🔴過熱1.0/7｜FAIL_INSEN｜終値1,355円｜💰139,500円｜[—]｜
- 5208 有沢製作所｜granville_oshime｜✅順調4/13｜🔴過熱0.0/7｜FAIL_INSEN｜終値2,519円｜💰261,900円｜[—]｜
- 7867 Tomy Company, Ltd.｜granville_oshime｜✅順調4/13｜🔴過熱0.0/7｜FAIL_INSEN｜終値3,533円｜💰365,400円｜[—]｜
- 160A As Partners CO.,LTD.｜granville_tenkan｜✅順調3/13｜💎割安7.0/7｜FAIL_INSEN｜終値1,961円｜💰197,600円｜[—]｜
- 1716 Daiichi Cutter Kogyo K.K.｜granville_tenkan｜✅順調3/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値1,382円｜💰140,000円｜[—]｜
- 4553 Towa Pharmaceutical Co., Ltd.｜granville_oshime｜✅順調3/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値3,465円｜💰358,000円｜[—]｜
- 5985 SUNCALL CORPORATION｜granville_oshime｜✅順調3/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値2,121円｜💰203,300円｜[—]｜
- 7994 OKAMURA CORP｜granville_tenkan｜✅順調3/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値2,350円｜💰239,000円｜[—]｜
- 1820 西松建設｜granville_tenkan｜✅順調3/13｜⚪妥当3.0/7｜PASS｜終値5,634円｜💰563,400円｜逆指値5647 SL5307.24｜
  > 📌ヘッドライン
  > 【業態】総合建設会社。ダム・トンネルなど土木に強み。開発事業強化。伊藤忠の持分法。
  > 【いま】終値5,634円・直近5日-0.88%（材料未確認）
  > 【調子】✅順調（3/13） — 質注意
  > 【水準】⚪妥当（3.0/7）— PER10.9倍・PEG—・52週33% ／ 💰単元56.3万円
  > 【戦略】当日高値超えの逆指値5647円で順張り参戦を検討。上限5703.47円・SL5307.24円目安／⚠1単元でリスク枠超過（33976円）
- 6927 Helios Techno Holding Co., Ltd.｜granville_tenkan｜🔻悪化3/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値982円｜💰99,300円｜[—]｜
- 1518 Mitsui Matsushima Holdings Co., Ltd.｜granville_rebound｜✅順調3/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値2,291円｜💰228,900円｜[—]｜
- 255A Gltechno Holdings, Inc.｜granville_rebound｜✅順調3/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値5,070円｜💰532,000円｜[—]｜
- 3569 セーレン｜granville_tenkan｜✅順調3/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値3,265円｜💰340,500円｜[—]｜
- 4183 Mitsui Chemicals, Inc.｜granville_tenkan｜✅順調3/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値2,124.5円｜💰222,400円｜[—]｜
- 4956 Konishi Co., Ltd.｜granville_tenkan｜✅順調3/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値1,452円｜💰147,900円｜[—]｜
- 6730 アクセル｜granville_tenkan｜🔻悪化3/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値1,141円｜💰120,100円｜[—]｜
- 7460 Yagi & Co., Ltd.｜granville_rebound｜✅順調3/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値1,650円｜💰167,000円｜[—]｜
- 9041 近鉄グループホールディングス｜granville_tenkan｜✅順調3/13｜🟡やや割高2.0/7｜FAIL_UWAHIGE｜終値3,425円｜💰343,600円｜[—]｜
- 9044 NANKAI Co., Ltd.｜granville_rebound｜✅順調3/13｜🟡やや割高2.0/7｜FAIL_UWAHIGE｜終値3,133円｜💰311,500円｜[—]｜
- 1860 戸田建設｜granville_rebound｜✅順調3/13｜🔴過熱1.0/7｜FAIL_UWAHIGE｜終値1,513.5円｜💰151,500円｜[—]｜
- 3191 Joyful Honda Co. Ltd.｜granville_rebound｜✅順調3/13｜🔴過熱1.0/7｜PASS｜終値2,245円｜💰224,500円｜[—]｜
  > 📌ヘッドライン
  > 【業態】ホームセンター大手。茨城・千葉中心に関東で超大型店を展開。アークランズと統合へ。
  > 【いま】終値2,245円・直近5日+1.04%（材料未確認）
  > 【調子】✅順調（3/13）
  > 【水準】🔴過熱（1.0/7）— PER20.5倍・PEG—・52週43% ／ 💰単元22.4万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 12営業日)）
- 4972 綜研化学｜granville_rebound｜✅順調3/13｜🔴過熱1.0/7｜FAIL_INSEN｜終値3,645円｜💰407,500円｜[—]｜
- 5232 Sumitomo Osaka Cement Co., Ltd.｜granville_oshime｜✅順調3/13｜🔴過熱1.0/7｜FAIL_UWAHIGE｜終値5,497円｜💰537,600円｜[—]｜
- 5423 Tokyo Steel Manufacturing Co., Ltd.｜granville_tenkan｜🔻悪化3/13｜🔴過熱1.0/7｜FAIL_INSEN｜終値1,685円｜💰170,100円｜[—]｜
- 6055 Japan Material Co., Ltd.｜granville_oshime｜✅順調3/13｜🔴過熱1.0/7｜FAIL_INSEN｜終値2,196円｜💰214,800円｜[—]｜
- 6237 Iwaki Co. Ltd.｜granville_rebound｜✅順調3/13｜🔴過熱1.0/7｜FAIL_INSEN｜終値3,770円｜💰400,500円｜[—]｜
- 6432 Takeuchi Mfg.Co., Ltd.｜granville_oshime｜✅順調3/13｜🔴過熱1.0/7｜FAIL_INSEN｜終値7,240円｜💰762,000円｜[—]｜
- 6966 Mitsui High-Tec, Inc.｜granville_oshime｜✅順調3/13｜🔴過熱1.0/7｜FAIL_INSEN｜終値903円｜💰93,900円｜[—]｜
- 7745 A&D HOLON Holdings Company. Limited｜granville_rebound｜🔻悪化3/13｜🔴過熱1.0/7｜FAIL_INSEN｜終値2,750円｜💰289,800円｜[—]｜
- 9010 Fuji Kyuko Co., Ltd.｜granville_oshime｜✅順調3/13｜🔴過熱1.0/7｜PASS｜終値2,593円｜💰259,300円｜[—]｜
  > 📌ヘッドライン
  > 【業態】富士山麓が地盤。鉄道と富士急ハイランドが両輪、別荘・リゾートも。バスに強み。
  > 【いま】終値2,593円・直近5日-4.98%（材料未確認）
  > 【調子】✅順調（3/13） — 質注意
  > 【水準】🔴過熱（1.0/7）— PER23.9倍・PEG687.08・52週73% ／ 💰単元25.9万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 1375 Yukiguni Factory Co., Ltd.｜granville_oshime｜✅順調3/13｜🔴過熱0.0/7｜PASS｜終値1,178円｜💰117,800円｜[—]｜
  > 📌ヘッドライン
  > 【業態】まいたけ、エリンギなどきのこ生産・加工食品販売。健康食品も。神明グループ。
  > 【いま】終値1,178円・直近5日+0.51%（材料未確認）
  > 【調子】✅順調（3/13） — 質注意
  > 【水準】🔴過熱（0.0/7）— PER18.5倍・PEG—・52週87% ／ 💰単元11.8万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 13営業日)）
- 9861 Yoshinoya Holdings Co., Ltd.｜granville_oshime｜✅順調3/13｜🔴過熱0.0/7｜PASS｜終値3,824円｜💰382,400円｜[—]｜
  > 📌ヘッドライン
  > 【業態】牛丼屋老舗。収益柱「吉野家」と「はなまるうどん」を全国展開。ラーメン店も。
  > 【いま】終値3,824円・直近5日-1.34%（材料未確認）
  > 【調子】✅順調（3/13）
  > 【水準】🔴過熱（0.0/7）— PER50.2倍・PEG—・52週76% ／ 💰単元38.2万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 12営業日)）
- 3289 Tokyu Fudosan Holdings Corp.｜granville_tenkan｜➖横ばい2/13｜🟢値頃5.0/7｜FAIL_UWAHIGE｜終値1,295円｜💰131,200円｜[—]｜
- 1605 Inpex Corporation｜granville_tenkan｜➖横ばい2/13｜⚪妥当4.0/7｜PASS｜終値3,832円｜💰383,200円｜[—]｜
  > 📌ヘッドライン
  > 【業態】資源開発最大手。原油・ガス開発生産。政府が黄金株保有。豪でLNG。
  > 【いま】終値3,832円・直近5日-6.81%（材料未確認）
  > 【調子】➖横ばい（2/13） — 質注意
  > 【水準】⚪妥当（4.0/7）— PER8.7倍・PEG0.98・52週53% ／ 💰単元38.3万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 17営業日)）
- 7679 Yakuodo Holdings Co., Ltd.｜granville_tenkan｜➖横ばい2/13｜⚪妥当4.0/7｜PASS｜終値1,661円｜💰166,100円｜[—]｜
  > 📌ヘッドライン
  > 【業態】岩手地盤のドラッグストア。東北5県に集中出店。食品、化粧品、衣料等展開。
  > 【いま】終値1,661円・直近5日+0.91%（材料未確認）
  > 【調子】➖横ばい（2/13） — 質注意
  > 【水準】⚪妥当（4.0/7）— PER8.0倍・PEG48.87・52週7% ／ 💰単元16.6万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 12営業日)）
- 9959 Aseed Holdings Co., Ltd.｜granville_rebound｜➖横ばい2/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値954円｜💰96,400円｜[—]｜
- 2282 NH Foods Limited｜granville_tenkan｜➖横ばい2/13｜⚪妥当3.0/7｜PASS｜終値6,209円｜💰620,900円｜[—]｜
  > 📌ヘッドライン
  > 【業態】食肉加工品で国内最大手。飼育・加工・販売までグループで一貫体制が強み。
  > 【いま】終値6,209円・直近5日-2.57%（材料未確認）
  > 【調子】➖横ばい（2/13） — 質注意
  > 【水準】⚪妥当（3.0/7）— PER15.2倍・PEG18.16・52週35% ／ 💰単元62.1万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 11営業日)）
- 2292 S Foods Inc.｜granville_tenkan｜➖横ばい2/13｜⚪妥当3.0/7｜PASS_DOJI｜終値2,770円｜💰277,000円｜[—]｜
  > 📌ヘッドライン
  > 【業態】牛肉・ホルモン輸入の先駆。「こてっちゃん」が主力。焼き肉店も。丸紅と親密。
  > 【いま】終値2,770円・直近5日-5.69%（材料未確認）
  > 【調子】➖横ばい（2/13） — 質注意
  > 【水準】⚪妥当（3.0/7）— PER13.5倍・PEG—・52週36% ／ 💰単元27.7万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 16営業日)）
- 5851 Ryobi Limited｜granville_tenkan｜➖横ばい2/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値2,704円｜💰280,200円｜[—]｜
- 5998 アドバネクス｜granville_rebound｜➖横ばい2/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値2,649円｜💰275,200円｜[—]｜
- 6703 沖電気工業｜granville_rebound｜➖横ばい2/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値2,636円｜💰279,800円｜[—]｜
- 1833 Okumura Corporation｜granville_tenkan｜⚠減速2/13｜🟡やや割高2.0/7｜FAIL_UWAHIGE｜終値5,790円｜💰578,000円｜[—]｜
- 2483 翻訳センター｜granville_rebound｜➖横ばい2/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値2,166円｜💰223,000円｜[—]｜
- 6363 酉島製作所｜granville_rebound｜➖横ばい2/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値2,882円｜💰304,500円｜[—]｜
- 6794 Foster Electric Company, Limited｜granville_tenkan｜➖横ばい2/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値2,902円｜💰302,500円｜[—]｜
- 7459 MEDIPAL HOLDINGS Corporation｜granville_rebound｜➖横ばい2/13｜🟡やや割高2.0/7｜PASS｜終値2,932円｜💰293,200円｜[—]｜
  > 📌ヘッドライン
  > 【業態】医薬品卸最大手級。傘下にメディセオやパルタック等。大型物流センターを全国展開。
  > 【いま】終値2,932円・直近5日-0.02%（材料未確認）
  > 【調子】➖横ばい（2/13） — 質注意
  > 【水準】🟡やや割高（2.0/7）— PER14.0倍・PEG—・52週73% ／ 💰単元29.3万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 13営業日)）
- 8057 内田洋行｜granville_tenkan｜⚠減速2/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値2,224円｜💰229,900円｜[—]｜
- 8337 千葉興業銀行｜granville_oshime｜➖横ばい2/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値2,684円｜💰277,300円｜[—]｜
- 8803 Heiwa Real Estate Co., Ltd.｜granville_tenkan｜➖横ばい2/13｜🟡やや割高2.0/7｜PASS｜終値2,358円｜💰235,800円｜逆指値2362 SL2219.34｜
  > 📌ヘッドライン
  > 【業態】各地の証券取引所賃貸が収益源。一般賃貸、マンション分譲なども。REIT強化。
  > 【いま】終値2,358円・直近5日-2.24%（材料未確認）
  > 【調子】➖横ばい（2/13） — 質注意
  > 【水準】🟡やや割高（2.0/7）— PER13.5倍・PEG87.90・52週51% ／ 💰単元23.6万円
  > 【戦略】当日高値超えの逆指値2362円で順張り参戦を検討。上限2385.62円・SL2219.34円目安
- 9503 Kansai Electric Power Company, Incorporated｜granville_tenkan｜🔻悪化2/13｜🔴過熱2.0/7｜FAIL_INSEN｜終値2,939.5円｜💰294,700円｜[—]｜
- 3063 j-Group Holdings Corp.｜granville_rebound｜➖横ばい2/13｜🔴過熱1.0/7｜FAIL_INSEN｜終値1,150円｜💰115,400円｜[—]｜
- 5302 日本カーボン｜granville_tenkan｜➖横ばい2/13｜🔴過熱1.0/7｜FAIL_INSEN｜終値4,970円｜💰511,000円｜[—]｜
- 7278 Exedy Corporation｜granville_oshime｜➖横ばい2/13｜🔴過熱1.0/7｜FAIL_INSEN｜終値5,910円｜💰614,000円｜[—]｜
- 8101 GSI Creos Corporation｜granville_oshime｜⚠減速2/13｜🔴過熱1.0/7｜FAIL_INSEN｜終値2,610円｜💰268,400円｜[—]｜
- 3076 Ai Holdings Corporation｜granville_oshime｜➖横ばい2/13｜🔴過熱0.0/7｜FAIL_INSEN｜終値2,972円｜💰300,500円｜[—]｜
- 7780 Menicon Co., Ltd.｜granville_rebound｜➖横ばい2/13｜🔴過熱0.0/7｜FAIL_INSEN｜終値1,764円｜💰186,700円｜[—]｜
- 9616 共立メンテナンス｜granville_oshime｜➖横ばい2/13｜🔴過熱0.0/7｜FAIL_INSEN｜終値3,184円｜💰325,500円｜[—]｜
- 4228 Sekisui Kasei Co., Ltd.｜granville_oshime｜⚠減速1/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値559円｜💰60,000円｜[—]｜
- 2733 Arata Corporation｜granville_tenkan｜🔻悪化1/13｜⚪妥当3.0/7｜FAIL_UWAHIGE｜終値2,670円｜💰269,000円｜[—]｜
- 3946 Tomoku Co., Ltd.｜granville_oshime｜⚠減速1/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値4,260円｜💰437,000円｜[—]｜
- 6638 ミマキエンジニアリング｜granville_oshime｜⚠減速1/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値1,840円｜💰196,600円｜[—]｜
- 9404 Nippon Television Holdings, Inc.｜granville_tenkan｜🔻悪化1/13｜⚪妥当3.0/7｜PASS｜終値2,994円｜💰299,400円｜逆指値3005 SL2823.76｜
  > 📌ヘッドライン
  > 【業態】読売グループの民放大手。視聴率でトップ争い。動画配信「Hulu」、フィットネスも。
  > 【いま】終値2,994円・直近5日-2.73%（材料未確認）
  > 【調子】🔻悪化（1/13） — 質注意
  > 【水準】⚪妥当（3.0/7）— PER14.2倍・PEG—・52週22% ／ 💰単元29.9万円
  > 【戦略】当日高値超えの逆指値3005円で順張り参戦を検討。上限3035.05円・SL2823.76円目安
- 1878 Daito Trust Construction Co., Ltd.｜granville_rebound｜⚠減速1/13｜🟡やや割高2.0/7｜PASS｜終値3,290円｜💰329,000円｜[—]｜
  > 📌ヘッドライン
  > 【業態】地主に建物賃貸事業を提案。建設・賃貸仲介・管理・家賃保証など一貫。
  > 【いま】終値3,290円・直近5日-2.23%（材料未確認）
  > 【調子】⚠減速（1/13） — 質注意
  > 【水準】🟡やや割高（2.0/7）— PER9.9倍・PEG16.64・52週44% ／ 💰単元32.9万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 12営業日)）
- 1980 DAI-DAN Co., Ltd.｜granville_tenkan｜⚠減速1/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値2,800円｜💰273,700円｜[—]｜
- 2217 Morozoff Limited｜granville_rebound｜🔻悪化1/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値1,488円｜💰149,600円｜[—]｜
- 2317 システナ｜granville_tenkan｜⚠減速1/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値434円｜💰45,300円｜[—]｜
- 4980 Dexerials Corp.｜granville_rebound｜⚠減速1/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値2,779.5円｜💰299,150円｜[—]｜
- 5408 Nakayama Steel Works,Ltd.｜granville_tenkan｜🔻悪化1/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値640円｜💰66,400円｜[—]｜
- 7943 Nichiha Corporation｜granville_tenkan｜⚠減速1/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値2,974円｜💰304,000円｜[—]｜
- 9001 東武鉄道｜granville_rebound｜⚠減速1/13｜🟡やや割高2.0/7｜FAIL_UWAHIGE｜終値2,903.5円｜💰294,100円｜[—]｜
- 9502 中部電力｜granville_rebound｜🔻悪化1/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値2,978.5円｜💰292,600円｜[—]｜
- 1982 Hibiya Engineering,Ltd.｜granville_tenkan｜⚠減速1/13｜🔴過熱1.0/7｜FAIL_UWAHIGE｜終値3,145円｜💰316,000円｜[—]｜
- 2001 NIPPN Corporation｜granville_oshime｜⚠減速1/13｜🔴過熱1.0/7｜PASS｜終値2,952円｜💰295,200円｜[—]｜
  > 📌ヘッドライン
  > 【業態】製粉老舗で業界2位。加工食品、バイオ事業など多角化推進。アジアにも展開。
  > 【いま】終値2,952円・直近5日-0.57%（材料未確認）
  > 【調子】⚠減速（1/13）
  > 【水準】🔴過熱（1.0/7）— PER11.5倍・PEG—・52週94% ／ 💰単元29.5万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 13営業日)）
- 3086 J. FRONT RETAILING Co., Ltd.｜granville_rebound｜⚠減速1/13｜🔴過熱1.0/7｜FAIL_INSEN｜終値2,614.5円｜💰276,750円｜[—]｜
- 5310 Toyo Tanso Co., Ltd.｜granville_rebound｜🔻悪化1/13｜🔴過熱1.0/7｜FAIL_INSEN｜終値6,800円｜💰714,000円｜[—]｜
- 6333 TEIKOKU Corp.｜granville_oshime｜⚠減速1/13｜🔴過熱1.0/7｜FAIL_INSEN｜終値3,360円｜💰340,000円｜[—]｜
- 6770 Alps Alpine Co., Ltd.｜granville_tenkan｜⚠減速1/13｜🔴過熱1.0/7｜FAIL_INSEN｜終値2,069.5円｜💰225,800円｜[—]｜
- 7128 UNISOL Holdings Corporation｜granville_oshime｜⚠減速1/13｜🔴過熱1.0/7｜FAIL_UWAHIGE｜終値2,797円｜💰277,300円｜[—]｜
- 7600 日本エム・ディ・エム｜granville_rebound｜🔻悪化1/13｜🔴過熱1.0/7｜FAIL_INSEN｜終値624円｜💰68,300円｜[—]｜
- 7981 Takara standard Co., Ltd.｜granville_oshime｜⚠減速1/13｜🔴過熱1.0/7｜FAIL_INSEN｜終値3,075円｜💰311,000円｜[—]｜
- 9735 Secom Co., Ltd.｜granville_rebound｜⚠減速1/13｜🔴過熱1.0/7｜PASS｜終値6,303円｜💰630,300円｜[—]｜
  > 📌ヘッドライン
  > 【業態】警備最大手。賃貸センサー付システム警備が主力。防災、在宅医療など。海外強化。
  > 【いま】終値6,303円・直近5日-2.97%（材料未確認）
  > 【調子】⚠減速（1/13） — 質注意
  > 【水準】🔴過熱（1.0/7）— PER23.8倍・PEG—・52週57% ／ 💰単元63.0万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 13営業日)）
- 2810 ハウス食品グループ本社｜granville_oshime｜⚠減速1/13｜🔴過熱0.0/7｜PASS｜終値3,854円｜💰385,400円｜[—]｜
  > 📌ヘッドライン
  > 【業態】カレー、シチュー用ルウでトップ。飲料、健康食品も。乳酸菌事業を拡大。米国で豆腐。
  > 【いま】終値3,854円・直近5日-3.70%（材料未確認）
  > 【調子】⚠減速（1/13） — 質注意
  > 【水準】🔴過熱（0.0/7）— PER20.2倍・PEG—・52週80% ／ 💰単元38.5万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 15営業日)）
- 8566 Ricoh Leasing Company,Ltd.｜granville_rebound｜⚠減速1/13｜🔴過熱0.0/7｜FAIL_UWAHIGE｜終値6,820円｜💰682,000円｜[—]｜
- 9301 三菱倉庫｜granville_rebound｜⚠減速1/13｜🔴過熱0.0/7｜FAIL_INSEN｜終値1,536.5円｜💰154,000円｜[—]｜
- 1976 Meisei Industrial Co., Ltd.｜granville_rebound｜⚠減速0/13｜⚪妥当3.0/7｜FAIL_UWAHIGE｜終値1,724円｜💰170,000円｜[—]｜
- 2432 ディー・エヌ・エー｜granville_tenkan｜業績データ取得不可｜🟢値頃5.6/7｜PASS｜終値2,610.5円｜💰261,050円｜逆指値2627.5 SL2468.91｜
  > 📌ヘッドライン
  > 【業態】交流サイト「モバゲー」運営。ゲーム課金が収益の柱。AI、医療関連など多角化展開。
  > 【いま】終値2,610円・直近5日+0.15%（材料未確認）
  > 【調子】業績データ取得不可
  > 【水準】🟢値頃（5.6/7）— PER—・PEG—・52週55% ／ 💰単元26.1万円
  > 【戦略】当日高値超えの逆指値2627.5円で順張り参戦を検討。上限2653.78円・SL2468.91円目安
- 9166 GENDA Inc.｜granville_oshime｜業績データ取得不可｜🟢値頃5.6/7｜PASS｜終値745円｜💰74,500円｜指値726.49 SL722.88｜
  > 📌ヘッドライン
  > 【業態】「GiGO」ブランドを主としたアミューズメント施設の運営。M&Aで成長。
  > 【いま】終値745円・直近5日+1.50%（材料未確認）
  > 【調子】業績データ取得不可
  > 【水準】🟢値頃（5.6/7）— PER—・PEG—・52週56% ／ 💰単元7.5万円
  > 【戦略】726.49円までの押し目を指値で待つ。SL722.88円（25日線基準）
- 2160 GNI Group Ltd.｜granville_tenkan｜業績データ取得不可｜⚪妥当4.2/7｜FAIL_INSEN｜終値2,936円｜💰287,200円｜[—]｜
- 3053 Pepper Food Service Co., Ltd.｜granville_tenkan｜業績データ取得不可｜⚪妥当4.2/7｜FAIL_INSEN｜終値202円｜💰20,700円｜[—]｜
- 3778 SAKURA Internet Inc.｜granville_oshime｜業績データ取得不可｜⚪妥当4.0/7｜FAIL_UWAHIGE｜終値3,700円｜💰363,000円｜[—]｜
- 4203 住友ベークライト｜granville_rebound｜業績データ取得不可｜⚪妥当3.0/7｜FAIL_INSEN｜終値6,900円｜💰720,000円｜[—]｜
- 4415 BROAD ENTERPRISE CO.,LTD.｜granville_oshime｜業績データ取得不可｜⚪妥当3.0/7｜FAIL_INSEN｜終値1,393円｜💰140,500円｜[—]｜
- 7182 ゆうちょ銀行｜granville_rebound｜取得不可｜⚪妥当3.0/7｜FAIL_INSEN｜終値3,280円｜💰337,700円｜[—]｜
- 8544 Keiyo Bank, Ltd.｜granville_oshime｜取得不可｜⚪妥当3.0/7｜FAIL_INSEN｜終値2,781円｜💰287,800円｜[—]｜
- 3003 ヒューリック｜granville_tenkan｜業績データ取得不可｜🟡やや割高2.8/7｜FAIL_UWAHIGE｜終値1,745.5円｜💰176,800円｜[—]｜
- 8425 Mizuho Leasing Company, Limited｜granville_tenkan｜業績データ取得不可｜🟡やや割高2.8/7｜FAIL_INSEN｜終値1,356円｜💰136,800円｜[—]｜
- 9628 San Holdings,Inc.｜granville_tenkan｜判定保留(変則決算)｜🟡やや割高2.8/7｜FAIL_INSEN｜終値1,299円｜💰133,000円｜[—]｜
- 7184 富山第一銀行｜granville_oshime｜取得不可｜🔴過熱1.0/7｜FAIL_INSEN｜終値3,265円｜💰340,500円｜[—]｜
- 8387 Shikoku Bank Ltd.｜granville_oshime｜取得不可｜🔴過熱0.0/7｜FAIL_INSEN｜終値3,745円｜💰381,000円｜[—]｜
- 1515 Nittetsu Mining Co., Ltd.｜granville_oshime｜—｜—｜FAIL_UWAHIGE｜終値3,530円｜💰—円｜[—]｜
- 1887 JDC Corporation｜granville_tenkan｜—｜—｜FAIL_UWAHIGE｜終値552円｜💰—円｜[—]｜
- 1899 福田組｜granville_oshime｜—｜—｜FAIL_UWAHIGE｜終値4,590円｜💰—円｜[—]｜
- 1946 トーエネック｜granville_tenkan｜—｜—｜FAIL_INSEN｜終値2,238円｜💰—円｜[—]｜
- 2768 Sojitz Corp.｜granville_tenkan｜業績データ取得不可(経常益予想非開示)｜⏸判定不能｜FAIL_INSEN｜終値5,783円｜💰576,200円｜[—]｜
- 2914 日本たばこ産業｜granville_rebound｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜終値6,660円｜💰680,300円｜[—]｜
- 3093 Treasure Factory Co., Ltd.｜granville_rebound｜—｜—｜FAIL_INSEN｜終値1,850円｜💰—円｜[—]｜
- 3544 SATUDORA HOLDINGS CO., LTD.｜granville_rebound｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜終値1,249円｜💰124,900円｜[—]｜
- 3612 ワールド｜granville_oshime｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜終値1,580円｜💰161,200円｜[—]｜
- 3676 ハーツユナイテッドグループ｜granville_rebound｜—｜—｜FAIL_INSEN｜終値1,057円｜💰—円｜[—]｜
- 3763 プロシップ｜granville_rebound｜—｜—｜FAIL_INSEN｜終値1,944円｜💰—円｜[—]｜
- 3765 ガンホー・オンライン・エンターテイメント｜granville_tenkan｜取得不可｜⏸判定不能｜FAIL_INSEN｜終値2,484円｜💰252,700円｜[—]｜
- 3863 日本製紙｜granville_rebound｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜終値1,278円｜💰130,600円｜[—]｜
- 4631 DIC Corporation｜granville_rebound｜—｜—｜FAIL_INSEN｜終値4,608円｜💰—円｜[—]｜
- 4694 BML , Inc.｜granville_tenkan｜—｜—｜FAIL_UWAHIGE｜終値3,605円｜💰—円｜[—]｜
- 4722 Future Corporation｜granville_oshime｜取得不可｜⏸判定不能｜FAIL_INSEN｜終値2,446円｜💰244,600円｜[—]｜
- 4765 SBI Global Asset Management Co.Ltd.｜granville_tenkan｜判定保留｜⏸判定不能｜FAIL_INSEN｜終値623円｜💰63,900円｜[—]｜
- 5714 ＤＯＷＡホールディングス｜granville_tenkan｜—｜—｜FAIL_INSEN｜終値9,001円｜💰—円｜[—]｜
- 6310 Iseki & Co., Ltd.｜granville_tenkan｜—｜—｜FAIL_INSEN｜終値1,902円｜💰—円｜[—]｜
- 6328 荏原実業｜granville_tenkan｜—｜—｜FAIL_INSEN｜終値2,376円｜💰—円｜[—]｜
- 6412 平和｜granville_tenkan｜—｜—｜FAIL_INSEN｜終値2,138円｜💰—円｜[—]｜
- 6470 Taiho Kogyo Co., Ltd.｜granville_rebound｜—｜—｜FAIL_INSEN｜終値1,042円｜💰—円｜[—]｜
- 6594 Nidec Corporation｜granville_rebound｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜終値2,722円｜💰281,200円｜[—]｜
- 6723 Renesas Electronics Corporation｜granville_rebound｜取得不可｜⏸判定不能｜FAIL_INSEN｜終値3,252円｜💰330,200円｜[—]｜
- 6834 Seikoh Giken Co., Ltd.｜granville_oshime｜—｜—｜FAIL_INSEN｜終値5,100円｜💰—円｜[—]｜
- 6928 エノモト｜granville_tenkan｜—｜—｜FAIL_INSEN｜終値2,922円｜💰—円｜[—]｜
- 7287 Nippon Seiki Co., Ltd.｜granville_tenkan｜業績データ取得不可(経常益予想非開示)｜⏸判定不能｜FAIL_INSEN｜終値2,570円｜💰270,000円｜[—]｜
- 7860 Avex Inc.｜granville_oshime｜業績データ取得不可｜⏸判定不能｜PASS｜終値1,249円｜💰124,900円｜[—]｜
  > 📌ヘッドライン
  > 【業態】音楽ソフト大手。若者向け人気歌手を擁す。イベント、ライブ映像配信などを強化。
  > 【いま】終値1,249円・直近5日-3.25%（材料未確認）
  > 【調子】業績データ取得不可
  > 【水準】⏸判定不能
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 16営業日)）
- 8050 SEIKO GROUP CORPORATION｜granville_rebound｜—｜—｜FAIL_INSEN｜終値9,280円｜💰—円｜[—]｜
- 8065 佐藤商事｜granville_rebound｜—｜—｜FAIL_INSEN｜終値3,315円｜💰—円｜[—]｜
- 8395 Bank of Saga Ltd.｜granville_oshime｜—｜—｜FAIL_INSEN｜終値6,400円｜💰—円｜[—]｜
- 8439 Tokyo Century Corporation｜granville_rebound｜—｜⏸判定不能｜FAIL_INSEN｜終値2,667円｜💰268,900円｜[—]｜
- 8630 Sompo Holdings,Inc.｜granville_rebound｜🔻悪化｜⏸判定不能｜FAIL_INSEN｜終値6,647円｜💰685,600円｜[—]｜

## 変化点銘柄
- 265A HMCOMM INC｜changepoint｜🚀確変12/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値720円｜💰76,100円｜[—]｜
- 5803 フジクラ｜changepoint｜🚀確変12/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値5,083円｜💰529,200円｜[—]｜
- 6254 野村マイクロ・サイエンス｜changepoint｜🔥絶好調10/13｜💎割安6.0/7｜FAIL_INSEN｜終値3,340円｜💰345,500円｜[—]｜
- 479A PRONI INC｜changepoint｜🔥絶好調10/13｜⚪妥当4.0/7｜PASS｜終値1,943円｜💰194,300円｜[—]｜
  > 📌ヘッドライン
  > 【業態】法人向け受発注プラットフォーム「PRONI アイミツ」の運営などを手掛ける。
  > 【いま】終値1,943円・直近5日+3.35%（材料未確認）
  > 【調子】🔥絶好調（10/13）
  > 【水準】⚪妥当（4.0/7）— PER9.6倍・PEG0.08・52週83% ／ 💰単元19.4万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 15営業日)）
- 6866 日置電機｜changepoint｜🔥絶好調10/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値9,960円｜💰1,086,000円｜[—]｜
- 7695 交換できるくん｜changepoint｜🔥絶好調10/13｜⚪妥当3.0/7｜PASS｜終値923円｜💰92,300円｜[—]｜
  > 📌ヘッドライン
  > 【業態】住宅設備機器と工事をセットでネット販売。見積もり、注文をネットで低価格化。
  > 【いま】終値923円・直近5日+4.18%（材料未確認）
  > 【調子】🔥絶好調（10/13）
  > 【水準】⚪妥当（3.0/7）— PER27.6倍・PEG0.19・52週93% ／ 💰単元9.2万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 11営業日)）
- 584A LiNKX, Inc.｜changepoint｜🔥絶好調9/13｜🟢値頃5.0/7｜FAIL_UWAHIGE｜終値2,728円｜💰282,800円｜[—]｜
- 6857 アドバンテスト｜changepoint｜🔥絶好調9/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値33,800円｜💰3,309,000円｜[—]｜
- 3696 セレス｜changepoint｜🔥絶好調8/13｜💎割安6.0/7｜FAIL_INSEN｜終値2,120円｜💰221,300円｜[—]｜
- 7318 セレンディップ・ホールディングス｜changepoint｜🔥絶好調8/13｜💎割安6.0/7｜FAIL_INSEN｜終値1,353円｜💰135,400円｜[—]｜
- 9888 UEX, Ltd.｜changepoint｜🔥絶好調8/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値1,234円｜💰129,200円｜[—]｜
- 4180 ＡＰＰＩＥＲ　ＧＲＯＵＰ｜changepoint｜🔥絶好調8/13｜⚪妥当3.0/7｜FAIL_UWAHIGE｜終値1,473円｜💰151,200円｜[—]｜
- 4443 Sansan, Inc.｜changepoint｜🔥絶好調8/13｜⚪妥当3.0/7｜FAIL_INSEN｜終値1,995円｜💰222,800円｜[—]｜
- 478A フツパー｜changepoint｜⚡好調7/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値808円｜💰81,100円｜[—]｜
- 4431 Smaregi, Inc.｜changepoint｜⚡好調7/13｜🟡やや割高2.0/7｜PASS_DOJI｜終値3,420円｜💰342,000円｜指値3420 SL3370｜
  > 📌ヘッドライン
  > 【業態】小売店クラウド型POSレジ・スマホアプリ「スマレジ」開発販売。中小事業社需要に注力。
  > 【いま】終値3,420円・直近5日-6.04%（材料未確認）
  > 【調子】⚡好調（7/13）
  > 【水準】🟡やや割高（2.0/7）— PER23.7倍・PEG0.92・52週78% ／ 💰単元34.2万円
  > 【戦略】発火日終値3420円の指値。追撃禁止・SL3370円。🔒実弾封印中（PL3紙ログ収集中）
- 8697 日本取引所グループ｜changepoint｜⚡好調7/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値2,203.5円｜💰223,900円｜[—]｜
- 3994 マネーフォワード｜changepoint｜⚡好調6/13｜🔴過熱1.4/7｜FAIL_INSEN｜終値6,045円｜💰671,000円｜[—]｜
- 4667 アイサンテクノロジー｜changepoint｜⚡好調6/13｜🔴過熱1.0/7｜FAIL_UWAHIGE｜終値3,400円｜💰297,000円｜[—]｜
- 6284 日精エー・エス・ビー機械｜changepoint｜⚡好調5/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値8,280円｜💰866,000円｜[—]｜
- 8704 トレイダーズホールディングス｜changepoint｜⚡好調5/13｜🟢値頃5.0/7｜FAIL_INSEN｜終値1,418円｜💰142,000円｜[—]｜
- 286A ユカリア｜changepoint｜⚡好調5/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値808円｜💰80,100円｜[—]｜
- 4441 トビラシステムズ｜changepoint｜⚡好調5/13｜🔴過熱0.0/7｜FAIL_INSEN｜終値1,440円｜💰151,900円｜[—]｜
- 4475 ＨＥＮＮＧＥ｜changepoint｜⚡好調5/13｜🔴過熱0.0/7｜FAIL_UWAHIGE｜終値1,590円｜💰166,400円｜[—]｜
- 7374 Interworks Confidence Inc.｜changepoint｜✅順調4/13｜💎割安6.0/7｜FAIL_INSEN｜終値1,522円｜💰152,800円｜[—]｜
- 6785 鈴木｜changepoint｜✅順調4/13｜⚪妥当4.0/7｜FAIL_INSEN｜終値3,035円｜💰319,500円｜[—]｜
- 218A Liberaware Co., Ltd.｜changepoint｜🔻悪化4/13｜🟡やや割高2.8/7｜FAIL_UWAHIGE｜終値1,180円｜💰115,300円｜[—]｜
- 5337 ダントーホールディングス｜changepoint｜✅順調4/13｜🔴過熱1.4/7｜FAIL_INSEN｜終値820円｜💰83,300円｜[—]｜
- 593A ティアフォー｜changepoint｜✅順調4/13｜🔴過熱1.4/7｜FAIL_INSEN｜終値2,354円｜💰287,000円｜[—]｜
- 4493 Cyber Security Cloud, Inc.｜changepoint｜✅順調3/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値1,781円｜💰180,800円｜[—]｜
- 598A CHATPLUS CO LTD｜changepoint｜✅順調3/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値1,638円｜💰182,000円｜[—]｜
- 4488 AI inside Inc.｜changepoint｜➖横ばい2/13｜🟡やや割高2.0/7｜FAIL_INSEN｜終値2,196円｜💰225,800円｜[—]｜
- 3923 Rakus Co., Ltd.｜changepoint｜判定保留(変則決算)｜⚪妥当3.0/7｜FAIL_UWAHIGE｜終値1,046.5円｜💰112,750円｜[—]｜
- 4478 freee K.K.｜changepoint｜業績データ取得不可｜🟡やや割高2.8/7｜FAIL_INSEN｜終値3,700円｜💰414,500円｜[—]｜

## ⚡材料後出し
該当なし

## 📢開示
使用したURL: https://kabutan.jp/warning/?mode=4_2 （取引時間中）／ https://kabutan.jp/warning/?mode=4_3 （取引終了後）／ https://kabutan.jp/warning/?mode=4_4 （15時30分以降のインパクト開示）
開示なし（プール・保有銘柄との一致0件。base_day分の株価注意報は11件検出したがいずれも非一致）
①-9へ引き渡し0件（recalc_queueは既存2件を維持・新規追加なし）

## 総当りゲート
プール全銘柄のコンパクト表（branch_typeで5手法→グランビル→変化点にグループ化、グループ内は判定別）
### 5手法（147件）
- **PASS**（11件）: 5136(2001円)、6630(801円)、2266(1109円)、2594(2026円)、428A(1580円)、3391(2341円)、8086(1460円)、3064(1963円)、7581(7480円)、7649(1323円)、7532(777.7円)
- **PASS_DOJI**（2件）: 3288(7596円)、9247(1810円)
- **FAIL_UWAHIGE**（24件）: 5137(309円)、3556(805円)、5246(821円)、135A(4520円)、146A(3760円)、277A(1907円)、276A(4165円)、4894(5420円)、8614(736円)、269A(2890円)、4599(330円)、6544(1473円)、2579(3806円)、1812(5062円)、1861(1300円)、1802(3050円)、8111(2107.5円)、7157(1415円)、9824(7910円)、4627(1872円)、5582(2148円)、341A(2226円)、7678(3295円)、7774(912円)
- **FAIL_INSEN**（110件）: 3441(2775円)、5586(933円)、5724(3100円)、3723(2660円)、5027(723円)、9270(2013円)、9341(612円)、9554(1730円)、421A(3815円)、1435(178円)、6298(1310円)、4377(2279円)、4479(962円)、5537(3290円)、7352(324円)、2334(575円)、3109(1044円)、3915(2314円)、5574(2968円)、5892(2411円)、8927(484円)、5590(729円)、4058(2300円)、6071(853円)、7409(1510円)、558A(5610円)、4477(339円)、9560(872円)、4973(4735円)、3798(534円)、505A(1388円)、5038(2151円)、9467(1108円)、8139(2191円)、6862(4350円)、325A(1755円)、6492(14150円)、3932(3480円)、6838(1516円)、3851(1504円)、8537(3090円)、1960(1693円)、7161(598円)、6278(13000円)、4099(2079円)、4047(2134円)、4971(6110円)、6516(5070円)、3465(3250円)、6103(4320円)、6481(6050円)、6268(4337円)、9279(2289円)、4368(2815円)、6235(2450円)、4186(8104円)、7729(16685円)、3104(3280円)、6941(7210円)、5938(1744.5円)、6856(21610円)、4187(4135円)、6370(7499円)、6754(3085円)、6622(12110円)、5991(3261円)、6504(12760円)、7944(3675円)、9412(2010円)、5333(5025円)、6806(23735円)、7202(2129.5円)、7972(2485円)、5444(12030円)、6728(7030円)、6013(2965円)、6707(6771円)、268A(1607円)、6383(5545円)、186A(1054円)、4091(5367円)、6113(2397円)、9065(8000円)、5334(7444円)、6996(2474円)、7966(5110円)、6925(3623円)、3433(2756円)、6323(3655円)、7701(3766円)、6586(5201円)、2264(1116.5円)、6674(4981円)、6368(12415円)、6617(6500円)、6841(4518円)、7220(2684円)、4061(3219円)、5105(3528円)、5332(5804円)、6951(6829円)、6845(1451円)、6479(3326円)、6804(2542円)、5344(56140円)、6101(4850円)、6141(2758円)、3131(6360円)、7433(5190円)、147A(985円)

### グランビル（266件）
- **PASS**（29件）: 4521(3905円)、3222(848円)、2931(347円)、2702(8260円)、7198(840円)、2281(2427円)、1820(5634円)、1605(3832円)、7679(1661円)、2282(6209円)、8803(2358円)、9404(2994円)、2432(2610.5円)、4480(2470円)、4258(4730円)、3034(2270円)、1375(1178円)、9861(3824円)、2001(2952円)、2810(3854円)、9166(745円)、7860(1249円)、9006(1561.5円)、194A(1895円)、3191(2245円)、7459(2932円)、1878(3290円)、9735(6303円)、9010(2593円)
- **PASS_DOJI**（3件）: 2292(2770円)、2384(4975円)、3168(1286円)
- **FAIL_UWAHIGE**（40件）: 5020(1393.5円)、4666(1980円)、5036(1505円)、1911(1272.5円)、2325(4725円)、9041(3425円)、3289(1295円)、1833(5790円)、2733(2670円)、1982(3145円)、3003(1745.5円)、3498(7380円)、1407(2338円)、2590(3035円)、2874(2198円)、4051(5950円)、2674(2583円)、9828(3360円)、2288(2254円)、5232(5497円)、7128(2797円)、3778(3700円)、3753(220円)、4424(337円)、9941(1236円)、6191(785円)、8005(1779円)、7376(751円)、4718(2632円)、9044(3133円)、1860(1513.5円)、9001(2903.5円)、8566(6820円)、1976(1724円)、1899(4590円)、1515(3530円)、1887(552円)、4382(764円)、4694(3605円)、7806(8230円)
- **FAIL_INSEN**（193件）: 212A(2938円)、9211(1427円)、6134(6690円)、3036(3330円)、145A(893円)、2986(2803円)、5703(2930円)、8151(1877円)、8562(381円)、6222(923円)、6425(710円)、3623(1273円)、3968(625円)、8793(4185円)、5932(641円)、7744(1970円)、4507(2897.5円)、3116(2201円)、5592(2652円)、2975(1430円)、3854(2169円)、6023(3280円)、3048(1712.5円)、6946(6110円)、7911(5020円)、8919(3550円)、6339(1151円)、2585(1491円)、5461(2129円)、6571(1282円)、5885(3455円)、208A(2875円)、1808(2800円)、6305(5750円)、6167(978円)、7276(2559円)、160A(1961円)、1716(1382円)、7994(2350円)、6927(982円)、3569(3265円)、4183(2124.5円)、4956(1452円)、6730(1141円)、5423(1685円)、5851(2704円)、6794(2902円)、8057(2224円)、9503(2939.5円)、5302(4970円)、2317(434円)、5408(640円)、7943(2974円)、6770(2069.5円)、2160(2936円)、3053(202円)、8425(1356円)、9628(1299円)、2768(5783円)、3765(2484円)、4765(623円)、7287(2570円)、2760(3955円)、6136(3425円)、3663(1768円)、6588(2801円)、4413(2964円)、166A(1108円)、5186(6570円)、9902(3025円)、2652(425円)、7199(2111円)、7609(3875円)、4417(4270円)、4968(2016円)、7716(3050円)、8022(4045円)、7616(2053.5円)、2780(4730円)、7888(888円)、8923(1699円)、4674(1780円)、7350(7640円)、7721(6920円)、9934(2988.5円)、3479(1873円)、6454(1876円)、4092(5100円)、4022(1939円)、5121(2646円)、7740(1355円)、7867(3533円)、4553(3465円)、5985(2121円)、6055(2196円)、6432(7240円)、6966(903円)、8337(2684円)、7278(5910円)、8101(2610円)、3076(2972円)、9616(3184円)、4228(559円)、3946(4260円)、6638(1840円)、6333(3360円)、7981(3075円)、4415(1393円)、8544(2781円)、7184(3265円)、8387(3745円)、3612(1580円)、4722(2446円)、2693(280円)、6264(1933円)、6997(2628円)、6407(5050円)、9880(3275円)、3449(3965円)、6914(3000円)、6976(9046円)、150A(707円)、6981(7023円)、7453(4136円)、6125(4700円)、6965(2225円)、4392(985円)、4220(2365円)、3405(1761円)、6706(3220円)、3040(2291円)、8011(1333円)、7606(2356円)、7419(1242円)、7120(996円)、6380(4035円)、6999(2109円)、7505(2169円)、4612(1115円)、9319(1760円)、4125(3775円)、8750(1822.5円)、9069(2217円)、3393(3020円)、5384(3285円)、6744(4020円)、1518(2291円)、255A(5070円)、7460(1650円)、4972(3645円)、6237(3770円)、7745(2750円)、9959(954円)、5998(2649円)、6703(2636円)、2483(2166円)、6363(2882円)、3063(1150円)、7780(1764円)、2217(1488円)、4980(2779.5円)、7600(624円)、9502(2978.5円)、3086(2614.5円)、5310(6800円)、9301(1536.5円)、7182(3280円)、2914(6660円)、3544(1249円)、3863(1278円)、4203(6900円)、6594(2722円)、6723(3252円)、8439(2667円)、8630(6647円)、5632(2247円)、5208(2519円)、1946(2238円)、3676(1057円)、3763(1944円)、5714(9001円)、6328(2376円)、6412(2138円)、6928(2922円)、8065(3315円)、1980(2800円)、3093(1850円)、4631(4608円)、6310(1902円)、6470(1042円)、6834(5100円)、8050(9280円)、8395(6400円)
- **SKIP**（1件）: 3480(?円)

### 変化点（33件）
- **PASS**（2件）: 479A(1943円)、7695(923円)
- **PASS_DOJI**（1件）: 4431(3420円)
- **FAIL_UWAHIGE**（6件）: 584A(2728円)、4180(1473円)、4667(3400円)、4475(1590円)、218A(1180円)、3923(1046.5円)
- **FAIL_INSEN**（24件）: 6785(3035円)、6857(33800円)、8697(2203.5円)、265A(720円)、6254(3340円)、3696(2120円)、9888(1234円)、4443(1995円)、478A(808円)、3994(6045円)、8704(1418円)、286A(808円)、4441(1440円)、7374(1522円)、5337(820円)、593A(2354円)、4493(1781円)、598A(1638円)、4488(2196円)、4478(3700円)、5803(5083円)、6284(8280円)、6866(9960円)、7318(1353円)

### 除籍リスト（first_seenから30暦日超・SBIグループ登録解除候補）
該当なし（本夜は30暦日超過に達した銘柄なし。直近除籍は2026-09-07の114件）

## 機械詳細
- STEP4.8週末ブリーフ: スキップ（week_open=false）
- gate_history: gate_history/2026-09-08.json 新規作成
- grades.json: 548銘柄／116129バイト（120KB以下）
- pool_bars.json: 446銘柄／384257バイト（500KB以下）
- profile_cache: 新規取得14件（kabutan概要欄より取得）、既存438件、合計452件
- kabutan新規取得(top/finance): トップページ14銘柄（静的層未取得2銘柄+業態未取得分・50件上限内で打ち切りなし）、financeページ50銘柄（PASS/PASS_DOJI+保有の全対象、うち新規フル計算2銘柄=3168・9010）
- gyoseki_cache 新規フル計算: 3168・9010（missing_from_cache）。他48銘柄はキャッシュ流用（再計算トリガー非該当）
- gyoseki_cache history退避: 0件（グレード/スコアが変化した既存銘柄なし。新規2件は退避対象外）
- valuation_cache 動的層更新: PASS/PASS_DOJI+保有 計51銘柄中、対象50銘柄の per/pbr/peg/pos52w/market_cap/tan_yen を当日終値で再計算（静的層は3168・9010のみ新規取得、既存48銘柄のstaticは不変更）
- 鮮度ゲート: 提案対象25件／鮮度切れ除外20件／nom_age分布 0-2:153・3-10:171・11+:122・欠損0件
- 3日ルール: 保有3銘柄判定。streak>=3: 1件(1861)／streak=2: 0件／判定不可: 0件
- pool 30日除籍: 0件（本夜は first_seen 最古29日のため該当なし。直近除籍は2026-09-07の114件）
- 開示ウォッチ: kabutan mode=4_2/4_3/4_4 計11件検出、プール一致0件、recalc_queueへの新規追加0件（既存2件を維持）
- master.json 変更行数: 書き出し後に git diff --numstat で実測（PR本文に記載）

