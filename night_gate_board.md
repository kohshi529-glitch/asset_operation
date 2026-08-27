# 夜間ゲート 2026-08-27

## サマリー
- 評価数: 397
- PASS数: 55（PASS_DOJI: 0）
- 発注可能提案数: 52
- 市場一言: レンジ様子見（先物乖離）
- 実行モード: 通常モード
- base_day: 2026-08-27
- week_open: false（STEP4.8週末ブリーフはスキップ）

## 検証結果
- V1 四者一致: proposals=52 / results entry_price=52 / sim行=52 → はい
- V2 PASS収支: PASS55件=提案52件+除外3件・null件数0 → はい
- V3 code重複/verdict単一: 重複False → はい
- V4 valuation static非改変: はい（新規5銘柄のみ追加、既存396銘柄は無変更）
- V5 master.json許可キー以外不変: はい（night_gate/gyoseki_cache/valuation_cache/profile_cache のみ変更を確認）
- V6 gyoseki_cache絵文字整合: 不整合0件 → はい
- V7 board必須セクション: はい（本ファイル参照）
- V8 模擬テンプレ書式: はい（｜後ろ空・単元記載・カンマなし、全52行で確認）
- V9 gate_history: バイト一致=True → はい
- V10 base_day整合: はい（results/night_gate_today/gate_history/模擬テンプレ全て2026-08-27）
- V11 書き出し整形: master.json変更行数は本文末尾「機械詳細」参照。indent幅=1を検出・使用
- V12 並び順: (a)(b)(c)すべて一致 → はい
- V13 grades.json: 401銘柄/110.3KB（120KB以下・和集合一致） → はい
- V14 method_score出所整合: 出所不明0件 → はい
- V15 ヘッドライン網羅性: PASS55件中欠落0件・禁止語0件 → はい
- V16 記録の蓄積: はい（当夜📊決算発表0件のためearnings_log追記なし・history超過0件）

## 保有アラート
target/stop は未同期の目標コマンド由来（pos_targets_20260823_1245.json 2026-08-23）。次の週次同期で trade_master に確定します

- **9304 澁澤倉庫**（現物・100株・取得2026-07-31）
  - 終値2,141円／取得1,786円／含み損益35,500円／25日線乖離11.93%
  - target=2,150円 stop=1,920円（stopまで10.32%）／残存リスク=0円
  - 業績⚡好調（6/13）／値頃感🔴過熱（0.0/7・PER16.5倍・52週98%）
  - （timestop期日超過・経過19営業日） / 🔴過熱圏（16.4819倍/52週98.35%）— 利確・トレール切り上げの検討材料 / 残存リスク0円（枠解放）
- **4413 ボードルア**（信用買建・100株・取得2026-08-12）
  - 終値2,968円／取得2,800円／含み損益16,800円／25日線乖離2.8%
  - target=—円 stop=2,870円（stopまで3.3%）／残存リスク=0円
  - 業績🔥絶好調（8/13）／値頃感🔴過熱（0.0/7・PER29.5倍・52週79%）
  - ⚠足が崩れた（premise_kill: 上髭0.25超） / （timestop期日超過・経過11営業日） / 🔴過熱圏（29.5323倍/52週78.61%）— 利確・トレール切り上げの検討材料 / 残存リスク0円（枠解放）
- **7685 ＢｕｙＳｅｌｌ　Ｔｅｃｈｎｏｌｏｇｉｅｓ**（信用買建・100株・取得2026-08-19）
  - 終値3,275円／取得3,080円／含み損益19,500円／25日線乖離3.57%
  - target=—円 stop=3,165円（stopまで3.36%）／残存リスク=0円
  - 業績🚀確変（12/13）／値頃感🟢値頃（5.0/7・PER20.7倍・52週66%）
  - ⚠足が崩れた（premise_kill: 陰線,上髭0.25超） / 残存リスク0円（枠解放）
- **8008 ４℃ＨＤ**（信用買建・100株・取得2026-08-14）
  - 終値2,164円／取得2,090円／含み損益7,400円／25日線乖離3.4%
  - target=—円 stop=1,995円（stopまで7.81%）／残存リスク=9,500円
  - 業績🔥絶好調（8/13）／値頃感⚪妥当（3.0/7・PER17.6倍・52週90%）
  - ⚠足が崩れた（premise_kill: 陰線,上髭0.25超）
- **9270 バリュエンスＨＤ**（信用買建・100株・取得2026-08-18）
  - 終値2,028円／取得2,105円／含み損益-7,700円／25日線乖離2.03%
  - target=—円 stop=1,980円（stopまで2.37%）／残存リスク=12,500円
  - 業績🔥絶好調（10/13）／値頃感🟢値頃（5.0/7・PER8.9倍・52週60%）
  - ⚠足が崩れた（premise_kill: 陰線） / ⏱タイムストップ接近

## 前夜の結果
PL5口座への正式な反映は週次①-11の採点で行われる。ここは参考情報。

前夜2026-08-27の提案53件 → 約定37・不約定16・判定不能0

| コード | 種別 | 指値/トリガー | 高値 | 安値 | 終値 | 約定 | 約定値 | 含み損益% |
|---|---|---|---|---|---|---|---|---|
| 5137 | momentum | 295.0 | 306.0 | 284.0 | 302.0 | ○ | 295.0 | 2.37 |
| 3723 | momentum | 2900.0 | 2899.0 | 2848.0 | 2851.0 | × | — | — |
| 9554 | momentum | 1786.0 | 1820.0 | 1745.0 | 1749.0 | ○ | 1786.0 | -2.07 |
| 6298 | momentum | 1334.0 | 1363.0 | 1315.0 | 1316.0 | × | — | — |
| 5537 | momentum | 3456.0 | 3490.0 | 3285.0 | 3285.0 | ○ | 3456.0 | -4.95 |
| 5574 | momentum | 2851.0 | 3000.0 | 2843.0 | 2973.0 | × | — | — |
| 7409 | momentum | 1610.0 | 1680.0 | 1603.0 | 1657.0 | ○ | 1626.0 | 1.91 |
| 9552 | momentum | 1101.0 | 1109.0 | 1053.0 | 1085.0 | ○ | 1101.0 | -1.45 |
| 505A | momentum | 1439.0 | 1444.0 | 1412.0 | 1415.0 | ○ | 1439.0 | -1.67 |
| 6785 | momentum | 2919.0 | 2978.0 | 2895.0 | 2939.0 | ○ | 2948.0 | -0.31 |
| 5334 | reversal | 8658.0 | 8810.0 | 8474.0 | 8474.0 | ○ | 8658.0 | -2.13 |
| 1861 | reversal | 1304.0 | 1313.0 | 1302.0 | 1303.0 | ○ | 1304.0 | -0.08 |
| 6632 | reversal | 1025.0 | 1041.5 | 1011.0 | 1032.5 | ○ | 1020.0 | 1.23 |
| 1975 | reversal | 3920.0 | 3955.0 | 3890.0 | 3920.0 | ○ | 3920.0 | 0.0 |
| 1980 | reversal | 2749.0 | 2819.0 | 2760.0 | 2794.0 | × | — | — |
| 276A | momentum | 3771.0 | 3835.0 | 3695.0 | 3730.0 | × | — | — |
| 8366 | reversal | 2755.0 | 2786.0 | 2749.0 | 2763.0 | ○ | 2755.0 | 0.29 |
| 543A | reversal | 273.0 | 277.0 | 271.0 | 274.0 | ○ | 273.0 | 0.37 |
| 150A | reversal | 765.0 | 769.0 | 733.0 | 741.0 | ○ | 760.0 | -2.5 |
| 9279 | oshime | 5157.9 | 5150.0 | 5000.0 | 5120.0 | ○ | 5090.0 | 0.59 |
| 3222 | momentum | 847.0 | 850.0 | 834.0 | 850.0 | ○ | 848.0 | 0.24 |
| 6125 | reversal | 4895.0 | 5010.0 | 4805.0 | 4835.0 | ○ | 4895.0 | -1.23 |
| 9941 | reversal | 1266.0 | 1260.0 | 1202.0 | 1220.0 | ○ | 1260.0 | -3.17 |
| 2874 | oshime | 2140.2 | 2205.0 | 2147.0 | 2197.0 | × | — | — |
| 9902 | oshime | 3015.4 | 3090.0 | 3045.0 | 3060.0 | × | — | — |
| 6023 | momentum | 2993.0 | 3000.0 | 2959.0 | 2998.0 | ○ | 2993.0 | 0.17 |
| 7911 | momentum | 5088.0 | 5161.0 | 4992.0 | 5001.0 | × | — | — |
| 6571 | momentum | 1311.0 | 1309.0 | 1300.0 | 1301.0 | × | — | — |
| 9319 | reversal | 1847.0 | 1851.0 | 1820.0 | 1847.0 | ○ | 1844.0 | 0.16 |
| 9828 | oshime | 3401.9 | 3595.0 | 3495.0 | 3510.0 | × | — | — |
| 1911 | momentum | 1351.5 | 1357.5 | 1333.5 | 1344.0 | ○ | 1351.5 | -0.55 |
| 7198 | momentum | 848.0 | 847.0 | 840.0 | 843.0 | × | — | — |
| 4718 | reversal | 2557.0 | 2541.0 | 2510.0 | 2541.0 | ○ | 2540.0 | 0.04 |
| 4553 | oshime | 3955.1 | 3970.0 | 3880.0 | 3930.0 | ○ | 3940.0 | -0.25 |
| 255A | reversal | 5200.0 | 5340.0 | 5090.0 | 5260.0 | ○ | 5150.0 | 2.14 |
| 3191 | reversal | 2294.0 | 2292.0 | 2253.0 | 2292.0 | ○ | 2271.0 | 0.92 |
| 1375 | oshime | 1159.9 | 1182.0 | 1168.0 | 1178.0 | × | — | — |
| 2483 | reversal | 2238.0 | 2243.0 | 2227.0 | 2239.0 | ○ | 2238.0 | 0.04 |
| 5189 | reversal | 3640.0 | 3710.0 | 3520.0 | 3520.0 | ○ | 3640.0 | -3.3 |
| 3063 | reversal | 1181.0 | 1164.0 | 1146.0 | 1150.0 | ○ | 1151.0 | -0.09 |
| 6770 | momentum | 2205.0 | 2233.5 | 2196.5 | 2211.5 | ○ | 2208.0 | 0.16 |
| 6333 | oshime | 3328.2 | 3475.0 | 3405.0 | 3430.0 | × | — | — |
| 7943 | momentum | 3131.0 | 3200.0 | 3110.0 | 3120.0 | ○ | 3140.0 | -0.64 |
| 8367 | oshime | 1862.8 | 1950.0 | 1912.0 | 1922.0 | × | — | — |
| 7182 | reversal | 3243.0 | 3328.0 | 3235.0 | 3301.0 | ○ | 3243.0 | 1.79 |
| 7184 | oshime | 3115.4 | 3450.0 | 3340.0 | 3400.0 | × | — | — |
| 3863 | reversal | 1377.0 | 1405.0 | 1370.0 | 1405.0 | ○ | 1377.0 | 2.03 |
| 4765 | momentum | 641.0 | 648.0 | 628.0 | 648.0 | ○ | 641.0 | 1.09 |
| 7860 | oshime | 1279.9 | 1302.0 | 1278.0 | 1282.0 | ○ | 1279.9 | 0.16 |
| 9519 | reversal | 976.0 | 951.0 | 914.0 | 924.0 | ○ | 950.0 | -2.74 |
| 9888 | changepoint | 1223.0 | 1269.0 | 1237.0 | 1247.0 | × | — | — |
| 3994 | changepoint | 6170.0 | 6645.0 | 6151.0 | 6428.0 | ○ | 6170.0 | 4.18 |
| 4488 | changepoint | 2153.0 | 2172.0 | 2135.0 | 2164.0 | ○ | 2135.0 | 1.36 |

## 模擬テンプレ
```
# base_day 2026-08-27 ／ 提案52件
# 使い方: 参戦する0〜3銘柄の行だけをコピーし、｜の後ろに参戦理由を書いてポジション株PJへ送る。
# 選ばなかった行は送らなくてよい（全行に理由を書く必要はない）。見送りは末尾の1行で足りる。
# 特定銘柄を理由つきで見送る場合のみ『模擬 見送り {code} ｜{理由}』を送る。
模擬 5724 kenmo_momentum 逆指値3535 SL3318.2 単元100 ｜
模擬 135A kenmo_momentum 逆指値4235 SL3976.2 単元100 ｜
模擬 4058 kenmo_momentum 逆指値2433 SL2286.08 単元100 ｜
模擬 558A kenmo_momentum 逆指値5990 SL5621.2 単元100 ｜
模擬 341A kenmo_momentum 逆指値2012 SL1890.34 単元100 ｜
模擬 8139 kenmo_momentum 逆指値2273 SL2135.68 単元100 ｜
模擬 4894 kenmo_momentum 逆指値5910 SL5546 単元100 ｜
模擬 8614 kenmo_momentum 逆指値741 SL695.6 単元100 ｜
模擬 5301 choruko_reversal 指値1670.5 SL1629 単元100 ｜
模擬 6013 choruko_reversal 指値3100 SL3035 単元100 ｜
模擬 9072 choruko_reversal 指値5442 SL5266 単元100 ｜
模擬 9302 choruko_reversal 指値3333 SL3284 単元100 ｜
模擬 1802 choruko_reversal 指値2993 SL2925 単元100 ｜
模擬 3222 granville_tenkan 逆指値851 SL799 単元100 ｜
模擬 7047 granville_tenkan 逆指値2320 SL2179.86 単元100 ｜
模擬 6023 granville_tenkan 逆指値3001 SL2820 単元100 ｜
模擬 9037 granville_tenkan 逆指値1885 SL1770.96 単元100 ｜
模擬 1808 granville_tenkan 逆指値2900 SL2725.06 単元100 ｜
模擬 4826 granville_tenkan 逆指値548 SL514.18 単元100 ｜
模擬 5302 granville_tenkan 逆指値5050 SL4737.6 単元100 ｜
模擬 2768 granville_tenkan 逆指値5610 SL5264 単元100 ｜
模擬 4765 granville_tenkan 逆指値649 SL609.12 単元100 ｜
模擬 2874 granville_oshime 指値2138.5 SL2127.88 単元100 ｜
模擬 7616 granville_oshime 指値2053 SL2042.74 単元100 ｜
模擬 7350 granville_oshime 指値7613.9 SL7576 単元100 ｜
模擬 9934 granville_oshime 指値2953.4 SL2938.66 単元100 ｜
模擬 3479 granville_oshime 指値1882.1 SL1872.76 単元100 ｜
模擬 5232 granville_oshime 指値5696.1 SL5667.72 単元100 ｜
模擬 6055 granville_oshime 指値2202.9 SL2191.92 単元100 ｜
模擬 8101 granville_oshime 指値2720.2 SL2706.64 単元100 ｜
模擬 9616 granville_oshime 指値3368.5 SL3351.76 単元100 ｜
模擬 4415 granville_rebound 指値1377.9 SL1371 単元100 ｜
模擬 8387 granville_oshime 指値3447.8 SL3430.6 単元100 ｜
模擬 8511 granville_oshime 指値2478.5 SL2466.2 単元100 ｜
模擬 8628 granville_oshime 指値1098.9 SL1093.48 単元100 ｜
模擬 8707 granville_oshime 指値4379.6 SL4357.8 単元100 ｜
模擬 3449 granville_rebound 指値4020 SL3660 単元100 ｜
模擬 4392 granville_rebound 指値1155 SL978 単元100 ｜
模擬 4220 granville_rebound 指値2676 SL2581 単元100 ｜
模擬 6656 granville_rebound 指値839 SL784 単元100 ｜
模擬 7120 granville_rebound 指値1007 SL995 単元100 ｜
模擬 5076 granville_rebound 指値2841 SL2706.5 単元100 ｜
模擬 9319 granville_rebound 指値1847 SL1796 単元100 ｜
模擬 3393 granville_rebound 指値3020 SL2993 単元100 ｜
模擬 4718 granville_rebound 指値2541 SL2403 単元100 ｜
模擬 3191 granville_rebound 指値2292 SL2253 単元100 ｜
模擬 4972 granville_rebound 指値3485 SL3300 単元100 ｜
模擬 7745 granville_rebound 指値2904 SL2703 単元100 ｜
模擬 5998 granville_rebound 指値2764 SL2305 単元100 ｜
模擬 3863 granville_rebound 指値1405 SL1340 単元100 ｜
模擬 4498 changepoint 指値1287 SL1282 単元100 🔒 ｜
模擬 593A 変化点🔔 指値1599 SL985 単元100 🔒 ｜
模擬 見送り ｜
```

## PASS内訳
PASS 55件 → 提案 52件（除外 3件: 型不一致2/材料後出し0/その他1）

除外銘柄一覧:
- 9279 GIFT HOLDINGS INC.: ⛔型不一致: 既に支持帯以下
- 4258 AMIYA Corporation: ⛔型不一致: 既に支持帯以下
- 479A PRONI INC: ⛔要確認: R比が負
## 5手法銘柄
| コード 銘柄名 | 手法 | 業績 | 値頃感 | 判定 | 終値 | 単元金額 | 提案 | チップ |
|---|---|---|---|---|---|---|---|---|
| 5137 Smart Drive Co. Ltd. | kenmo_momentum | 🚀確変(12) | 💎割安(6.0) | FAIL_UWAHIGE | 302.0 | 29,200 |  |  |
| 5254 Arent, Inc. | granville_oshime・kenmo_momentum | 🚀確変(12) | ⚪妥当(4.0) | FAIL_INSEN | 4075.0 | 406,000 |  |  |
| 3441 Sanno Co., Ltd. | kenmo_momentum・未マージPR由来 | 🚀確変(11) | 🟢値頃(5.0) | FAIL_INSEN | 2730.0 | 275,800 |  |  |
| 3556 RenetJapanGroup, Inc. | kenmo_momentum | 🚀確変(11) | 🟢値頃(5.0) | FAIL_INSEN | 860.0 | 88,000 |  |  |
| 5136 tripla Co.,Ltd. | kenmo_momentum | 🚀確変(11) | ⚪妥当(4.0) | FAIL_UWAHIGE | 1922.0 | 192,600 |  |  |
| 5243 note inc. | kenmo_momentum・未マージPR由来 | 🚀確変(11) | ⚪妥当(4.0) | FAIL_UWAHIGE | 2792.0 | 255,100 |  |  |
| 5586 Laboro.AI, Inc. | kenmo_momentum | 🚀確変(11) | ⚪妥当(4.0) | FAIL_UWAHIGE | 885.0 | 87,700 |  |  |
| 5724 Asaka Riken Co., Ltd. | kenmo_momentum | 🚀確変(11) | ⚪妥当(4.0) | PASS | 3505.0 | 350,500 | momentum 3535.0/SL3318.2/上限3570.35 |  |

> 📌【業態】電子部品等からの貴金属回収・精錬。独自技術に強み。環境事業に注力。
> 【いま】終値3,505円・直近5日+24.96%（材料未確認）
> 【調子】🚀確変（11/13） — E軸=進捗率データ制約のため直近QoQトレンドで代用
> 【水準】⚪妥当（4.0/7）— PER22.5倍・PEG0.16・52週54.0% ／ 💰単元35.0万円
> 【戦略】当日高値超えの逆指値3535.0円で順張り参戦を検討。上限3570.35円・SL3318.2円目安

| 3723 Nihon Falcom Corporation | kenmo_momentum | 🚀確変(11) | ⚪妥当(3.0) | FAIL_INSEN | 2851.0 | 289,900 |  |  |
| 5757 CK San-Etsu Co., Ltd. | kenmo_momentum・未マージPR由来 | 🔥絶好調(10) | 🟢値頃(5.0) | FAIL_INSEN | 5420.0 | 544,000 |  |  |
| 9270 Valuence Holdings, Inc. | kenmo_momentum・未マージPR由来 | 🔥絶好調(10) | 🟢値頃(5.0) | FAIL_INSEN | 2028.0 | 202,800 |  |  |
| 9341 GENOVA Inc. | granville_tenkan・kenmo_momentum | 🔥絶好調(10) | 🟢値頃(5.0) | FAIL_UWAHIGE | 633.0 | 64,200 |  |  |
| 212A FIT EASY Inc. | kenmo_momentum・未マージPR由来・granville_oshime | 🔥絶好調(10) | ⚪妥当(4.0) | FAIL_INSEN | 2970.0 | 305,500 |  |  |
| 5246 ELEMENTS,Inc. | kenmo_momentum | 🔥絶好調(10) | ⚪妥当(4.0) | FAIL_UWAHIGE | 905.0 | 82,800 |  |  |
| 9554 AViC Co. Ltd. | granville_tenkan・kenmo_momentum | 🔥絶好調(10) | ⚪妥当(4.0) | FAIL_INSEN | 1749.0 | 178,100 |  |  |
| 421A Movin' Strategic Career CO.,LTD. | kenmo_momentum | 🔥絶好調(10) | ⚪妥当(3.0) | FAIL_UWAHIGE | 3900.0 | 388,000 |  |  |
| 1435 robot home Inc. | kenmo_momentum | 🔥絶好調(9) | 💎割安(7.0) | FAIL_UWAHIGE | 181.0 | 18,100 |  |  |
| 9211 f-code Inc. | granville_tenkan・kenmo_momentum | 🔥絶好調(9) | 💎割安(6.0) | FAIL_INSEN | 1498.0 | 149,100 |  |  |
| 6298 Y.A.C.HOLDINGS CO.,LTD. | kenmo_momentum | 🔥絶好調(9) | 🟢値頃(5.0) | FAIL_INSEN | 1316.0 | 133,300 |  |  |
| 4377 ONE CAREER Inc. | kenmo_momentum | 🔥絶好調(9) | ⚪妥当(4.0) | FAIL_INSEN | 2551.0 | 247,500 |  |  |
| 5537 AlbaLink Co.,Ltd. | kenmo_momentum | 🔥絶好調(9) | ⚪妥当(3.0) | FAIL_INSEN | 3285.0 | 343,500 |  |  |
| 6562 Geniee, Inc. | kenmo_momentum・未マージPR由来 | 🔥絶好調(8) | 💎割安(7.0) | FAIL_INSEN | 889.0 | 90,500 |  |  |
| 262A INTERMESTIC INC. | kenmo_momentum | 🔥絶好調(8) | 💎割安(6.0) | FAIL_UWAHIGE | 1846.0 | 185,100 |  |  |
| 7318 SERENDIP HOLDINGS Co. Ltd. | kenmo_momentum・変化点🔔🔔 | 🔥絶好調(8) | 💎割安(6.0) | FAIL_UWAHIGE | 1456.0 | 149,800 |  |  |
| 2334 Eole, Inc. | kenmo_momentum | 🔥絶好調(8) | 🟢値頃(5.0) | FAIL_UWAHIGE | 565.0 | 54,900 |  |  |
| 3915 TerraSky Co., Ltd. | kenmo_momentum・未マージPR由来 | 🔥絶好調(8) | 🟢値頃(5.0) | FAIL_INSEN | 2333.0 | 227,600 |  |  |
| 7352 TWOSTONE&Sons Co.Ltd. | kenmo_momentum | 🔥絶好調(8) | 🟢値頃(5.0) | FAIL_INSEN | 340.0 | 36,000 |  |  |
| 3109 Shikibo Ltd. | kenmo_momentum | 🔥絶好調(8) | ⚪妥当(4.0) | FAIL_UWAHIGE | 1094.0 | 109,600 |  |  |
| 5574 ABEJA,Inc. | kenmo_momentum | 🔥絶好調(8) | ⚪妥当(4.0) | FAIL_UWAHIGE | 2973.0 | 283,300 |  |  |
| 6630 YA-MAN Ltd. | kenmo_momentum | 🔥絶好調(8) | ⚪妥当(3.0) | FAIL_INSEN | 795.0 | 81,300 |  |  |
| 135A VRAIN Solution,Inc. | kenmo_momentum・未マージPR由来 | 🔥絶好調(8) | 🟡やや割高(2.0) | PASS | 4220.0 | 422,000 | momentum 4235.0/SL3976.2/上限4277.35 |  |

> 📌【業態】製造業に特化した人工知能(AI)ソリューションの提供。検査システム。DX支援も。
> 【いま】終値4,220円・直近5日-3.43%（材料未確認）
> 【調子】🔥絶好調（8/13） — D軸判定不能(四半期データ不足)
> 【水準】🟡やや割高（2.0/7）— PER44.5倍・PEG0.76・52週78.0% ／ 💰単元42.2万円
> 【戦略】当日高値超えの逆指値4235.0円で順張り参戦を検討。上限4277.35円・SL3976.2円目安

| 8927 Meiho Enterprise Co., Ltd. | kenmo_momentum | ⚡好調(7) | 💎割安(7.0) | FAIL_UWAHIGE | 476.0 | 47,600 |  |  |
| 146A Columbia Works Inc. | kenmo_momentum | ⚡好調(7) | 💎割安(6.0) | FAIL_INSEN | 3615.0 | 368,500 |  |  |
| 5892 yutori,Inc. | kenmo_momentum・未マージPR由来 | ⚡好調(7) | 💎割安(6.0) | FAIL_UWAHIGE | 2549.0 | 242,000 |  |  |
| 5590 ネットスターズ | changepoint・kenmo_momentum・変化点🔔🔔・未マージPR由来 | ⚡好調(7) | 🟢値頃(5.0) | FAIL_INSEN | 694.0 | 69,600 |  |  |
| 4058 Toyokumo, Inc. | kenmo_momentum・未マージPR由来 | ⚡好調(7) | ⚪妥当(4.0) | PASS | 2432.0 | 243,200 | momentum 2433.0/SL2286.08/上限2457.33 |  |

> 📌【業態】安否確認サービスや法人向けクラウド事業。サイボウズ「キントーン」連携アプリ構築も展開。
> 【いま】終値2,432円・直近5日-1.34%（材料未確認）
> 【調子】⚡好調（7/13） — E軸判定不能(進捗データ不足)
> 【水準】⚪妥当（4.0/7）— PER18.8倍・PEG0.62・52週42.0% ／ 💰単元24.3万円
> 【戦略】当日高値超えの逆指値2433.0円で順張り参戦を検討。上限2457.33円・SL2286.08円目安

| 6071 IBJ, Inc. | kenmo_momentum | ⚡好調(7) | ⚪妥当(4.0) | FAIL_INSEN | 931.0 | 93,300 |  |  |
| 7409 AeroEdge Co.,Ltd | kenmo_momentum | ⚡好調(7) | ⚪妥当(3.0) | FAIL_UWAHIGE | 1657.0 | 159,300 |  |  |
| 558A SQUEEZE Inc. | kenmo_momentum | ⚡好調(7) | 🟡やや割高(2.8) | PASS | 5960.0 | 596,000 | momentum 5990.0/SL5621.2/上限6049.9 |  |

> 📌【業態】自社ホテル運営や、システム開発・提供、宿泊施設の企画・開発などを手掛ける。
> 【いま】終値5,960円・直近5日+3.65%（材料未確認）
> 【調子】⚡好調（7/13） — D軸判定不能(四半期データ不足)
> 【水準】🟡やや割高（2.8/7）— PER37.8倍・PEG1.14・52週96.0% ／ 💰単元59.6万円
> 【戦略】当日高値超えの逆指値5990.0円で順張り参戦を検討。上限6049.9円・SL5621.2円目安／⚠1単元でリスク枠超過（36880円）

| 9552 Quants Research Institute Holdings, Inc. | kenmo_momentum | ⚡好調(6) | ⚪妥当(4.0) | FAIL_INSEN | 1085.0 | 109,500 |  |  |
| 4477 BASE, Inc. | granville_rebound・kenmo_momentum・未マージPR由来 | ⚡好調(6) | ⚪妥当(3.0) | FAIL_INSEN | 311.0 | 31,100 |  |  |
| 2980 SRE Holdings Corp. | kenmo_momentum | ⚡好調(5) | 🟢値頃(5.0) | FAIL_UWAHIGE | 2461.0 | 241,400 |  |  |
| 4973 Japan Pure Chemical Co., Ltd. | kenmo_momentum・未マージPR由来 | ⚡好調(5) | 🟡やや割高(2.0) | FAIL_INSEN | 4790.0 | 475,000 |  |  |
| 4475 HENNGE K.K. | kenmo_momentum・未マージPR由来 | ⚡好調(5) | 🔴過熱(1.0) | FAIL_UWAHIGE | 1597.0 | 153,900 |  |  |
| 3798 ULS Group Incorporated | kenmo_momentum | ✅順調(4) | 💎割安(6.0) | FAIL_INSEN | 529.0 | 53,600 |  |  |
| 277A Globe-Ing, Inc. | kenmo_momentum | ✅順調(4) | 🟢値頃(5.0) | FAIL_UWAHIGE | 1922.0 | 185,400 |  |  |
| 505A Geekly,Inc. | kenmo_momentum・未マージPR由来 | ✅順調(4) | 🟢値頃(5.0) | FAIL_INSEN | 1415.0 | 143,300 |  |  |
| 6785 Suzuki Co., Ltd. | kenmo_momentum・未マージPR由来 | ✅順調(4) | 🟢値頃(5.0) | FAIL_INSEN | 2939.0 | 291,800 |  |  |
| 5038 eWeLL Co.,Ltd | kenmo_momentum | ✅順調(4) | ⚪妥当(4.0) | FAIL_INSEN | 2120.0 | 211,900 |  |  |
| 9467 Alphapolis Co., Ltd. | kenmo_momentum・未マージPR由来 | ✅順調(4) | ⚪妥当(4.0) | FAIL_INSEN | 1200.0 | 121,200 |  |  |
| 341A TOYOKOH Inc. | kenmo_momentum | ✅順調(4) | ⚪妥当(3.0) | PASS | 2007.0 | 200,700 | momentum 2012.0/SL1890.34/上限2032.12 |  |

> 📌【業態】建設業
> 【いま】終値2,007円・直近5日-0.89%（材料未確認）
> 【調子】✅順調（4/13） — E軸判定不能(進捗データ不足)
> 【水準】⚪妥当（3.0/7）— PER41.9倍・PEG1.68・52週15.0% ／ 💰単元20.1万円
> 【戦略】当日高値超えの逆指値2012.0円で順張り参戦を検討。上限2032.12円・SL1890.34円目安

| 8139 Nagahori Corporation | kenmo_momentum・未マージPR由来 | 🔻悪化(4) | 🔴過熱(1.0) | PASS | 2272.0 | 227,200 | momentum 2273.0/SL2135.68/上限2295.73 |  |

> 📌【業態】卸売業
> 【いま】終値2,272円・直近5日-1.98%（材料未確認）
> 【調子】🔻悪化（4/13） — 経常減益-37.1%
> 【水準】🔴過熱（1.0/7）— PER58.1倍・PEG—・52週51.0% ／ 💰単元22.7万円
> 【戦略】当日高値超えの逆指値2273.0円で順張り参戦を検討。上限2295.73円・SL2135.68円目安

| 4493 Cyber Security Cloud, Inc. | kenmo_momentum・未マージPR由来・granville_tenkan | ✅順調(3) | 🟡やや割高(2.0) | FAIL_UWAHIGE | 1850.0 | 191,000 |  |  |
| 2594 Key Coffee Inc. | kenmo_momentum・未マージPR由来 | 🔻悪化(2) | 🔴過熱(0.0) | FAIL_UWAHIGE | 2035.0 | 203,700 |  |  |
| 276A ククレブ・アドバイザーズ | granville_oshime・kenmo_momentum | 判定保留(—) | 🟢値頃(5.0) | FAIL_INSEN | 3730.0 | 376,500 |  |  |
| 325A TENTIAL, Inc. | kenmo_momentum・kenmo_newhigh・未マージPR由来 | 判定保留(変則決算)(—) | ⚪妥当(4.0) | FAIL_INSEN | 1688.0 | 178,600 |  |  |
| 6492 Okano Valve Mfg. Co., Ltd. | kenmo_momentum・未マージPR由来 | 判定保留(変則決算)(—) | ⚪妥当(4.0) | FAIL_INSEN | 14270.0 | 1,406,000 |  |  |
| 4165 PLAID Inc. | changepoint・kenmo_momentum・変化点🔔🔔 | 判定保留(変則決算: 連2025.09→連 予2026.12)(—) | 🔴過熱(2.8) | FAIL_INSEN | 685.0 | 68,800 |  |  |
| 4894 Cuorips Inc. | kenmo_momentum | 判定保留(—) | 🔴過熱(2.8) | PASS | 5840.0 | 584,000 | momentum 5910.0/SL5546.0/上限5969.1 |  |

> 📌【業態】医薬品
> 【いま】終値5,840円・直近5日+11.03%（材料未確認）
> 【調子】—（—/13） — 判定保留(変則決算): 通期予想売上高が前期比2.55倍(M&A/連結範囲変更等の可能性)
> 【水準】🔴過熱（2.8/7）— PER—倍・PEG—・52週25.0% ／ 💰単元58.4万円
> 【戦略】当日高値超えの逆指値5910.0円で順張り参戦を検討。上限5969.1円・SL5546.0円目安／⚠1単元でリスク枠超過（36400円）

| 3932 Akatsuki, Inc. | kenmo_momentum | —(—) | ⏸判定不能(—) | FAIL_INSEN | 3850.0 | 379,500 |  |  |
| 8614 Toyo Securities Co., Ltd. | kenmo_momentum | 業績データ取得不可(—) | ⏸判定不能(—) | PASS | 739.0 | 73,900 | momentum 741.0/SL695.6/上限748.41 |  |

> 📌【業態】証券・商品
> 【いま】終値739円・直近5日+3.07%（材料未確認）
> 【調子】—（—/13） — 通期予想が非開示(会社側未公表)
> 【水準】⏸判定不能（—/7）— PER—倍・PEG—・52週78.0% ／ 💰単元7.4万円
> 【戦略】当日高値超えの逆指値741.0円で順張り参戦を検討。上限748.41円・SL695.6円目安

| 9560 PROGRIT, Inc. | kenmo_momentum・未マージPR由来 | —(—) | —(—) | FAIL_UWAHIGE | 900.0 | — |  |  |
| 3374 内外テック | changepoint🔔🔔・kenmo_newhigh・変化点🔔🔔 | 🚀確変(12) | ⚪妥当(4.0) | FAIL_UWAHIGE | 4320.0 | 423,000 |  |  |
| 3851 Nippon Ichi Software, Inc. | kenmo_newhigh | 🔥絶好調(9) | ⚪妥当(3.0) | FAIL_UWAHIGE | 1297.0 | 126,600 |  |  |
| 1960 サンテック | kenmo_newhigh | ➖横ばい(2) | 🔴過熱(1.0) | FAIL_INSEN | 1651.0 | 169,500 |  |  |
| 4599 StemRIM Inc. | kenmo_newhigh | 取得不可(—) | ⏸判定不能(—) | FAIL_INSEN | 351.0 | 35,300 |  |  |
| 7685 ＢＵＹＳＥＬＬ　ＴＥＣＨＮＯＬＯＧＩＥＳ | choruko_reversal・granville_rebound | 🚀確変(12) | 🟢値頃(5.0) | FAIL_INSEN | 3275.0 | 327,500 |  |  |
| 5301 東海カーボン | choruko_reversal | 🔥絶好調(8) | ⚪妥当(4.0) | PASS | 1670.5 | 167,050 | reversal 1670.5/SL1629.0 |  |

> 📌【業態】ガラス・土石
> 【いま】終値1,670円・直近5日-2.25%（材料未確認）
> 【調子】🔥絶好調（8/13）
> 【水準】⚪妥当（4.0/7）— PER15.4倍・PEG0.51・52週74.0% ／ 💰単元16.7万円
> 【戦略】当日終値1670.5円の指値で反転を取りにいく。SL1629.0円（直近5日安値）

| 5938 LIXIL Corporation | choruko_reversal | ⚡好調(7) | ⚪妥当(4.0) | FAIL_UWAHIGE | 1772.0 | 177,100 |  |  |
| 6856 Horiba, Ltd. | choruko_reversal | ⚡好調(7) | ⚪妥当(4.0) | FAIL_INSEN | 23675.0 | 2,332,500 |  |  |
| 6370 Kurita Water Industries Ltd. | choruko_reversal | ⚡好調(7) | ⚪妥当(3.0) | FAIL_INSEN | 8230.0 | 809,600 |  |  |
| 7730 マニー | choruko_reversal | ⚡好調(7) | ⚪妥当(3.0) | FAIL_INSEN | 1614.0 | 161,400 |  |  |
| 3288 Open House Group Co. Ltd | choruko_reversal | ⚡好調(6) | 💎割安(7.0) | FAIL_INSEN | 7957.0 | 800,300 |  |  |
| 4516 日本新薬 | choruko_reversal | ⚡好調(6) | 💎割安(6.0) | FAIL_UWAHIGE | 3598.0 | 353,100 |  |  |
| 6544 Japan Elevator Service Holdings Co., Ltd. | choruko_reversal | ⚡好調(6) | ⚪妥当(3.0) | FAIL_UWAHIGE | 1559.0 | 158,250 |  |  |
| 7202 Isuzu Motors Limited | choruko_reversal | ⚡好調(5) | 💎割安(6.0) | FAIL_INSEN | 2213.0 | 221,300 |  |  |
| 7419 Nojima Co.,Ltd. | choruko_reversal | ⚡好調(5) | 💎割安(6.0) | FAIL_INSEN | 1277.0 | 127,900 |  |  |
| 7972 ITOKI Corporation | choruko_reversal | ⚡好調(5) | 💎割安(6.0) | FAIL_INSEN | 2595.0 | 258,700 |  |  |
| 5444 Yamato Kogyo Co., Ltd. | choruko_reversal | ⚡好調(5) | 🟢値頃(5.0) | FAIL_INSEN | 12305.0 | 1,244,000 |  |  |
| 3064 MonotaRO Co., Ltd. | choruko_reversal | ⚡好調(5) | ⚪妥当(3.0) | FAIL_UWAHIGE | 1872.5 | 185,700 |  | ⚡材料後出し |
| 6013 Takuma Co., Ltd. | choruko_reversal | ⚡好調(5) | ⚪妥当(3.0) | PASS | 3100.0 | 310,000 | reversal 3100.0/SL3035.0 |  |

> 📌【業態】ボイラー中心に環境設備を展開。官公需への依存度大。バイオマス発電プラントも。
> 【いま】終値3,100円・直近5日+0.16%（材料未確認）
> 【調子】⚡好調（5/13） — 進捗判定不能(自動抽出範囲外)
> 【水準】⚪妥当（3.0/7）— PER14.5倍・PEG1.06・52週58.0% ／ 💰単元31.0万円
> 【戦略】当日終値3100.0円の指値で反転を取りにいく。SL3035.0円（直近5日安値）

| 9072 ニッコンホールディングス | choruko_reversal | ⚡好調(5) | 🔴過熱(1.0) | PASS | 5442.0 | 544,200 | reversal 5442.0/SL5266.0 |  |

> 📌【業態】陸運業
> 【いま】終値5,442円・直近5日-1.22%（材料未確認）
> 【調子】⚡好調（5/13）
> 【水準】🔴過熱（1.0/7）— PER30.3倍・PEG2.84・52週65.0% ／ 💰単元54.4万円
> 【戦略】当日終値5442.0円の指値で反転を取りにいく。SL5266.0円（直近5日安値）

| 2579 Coca-Cola Bottlers Japan Holdings Inc. | choruko_reversal・granville_rebound | ✅順調(4) | ⚪妥当(4.0) | FAIL_UWAHIGE | 3920.0 | 393,100 |  |  |
| 7649 Sugi Holdings Co., Ltd. | choruko_reversal | ✅順調(4) | ⚪妥当(4.0) | FAIL_INSEN | 2678.0 | 275,150 |  |  |
| 7731 ニコン | choruko_reversal・granville_rebound | ✅順調(4) | ⚪妥当(4.0) | FAIL_INSEN | 1957.0 | 197,050 |  |  |
| 1812 Kajima Corporation | choruko_reversal | ⚠減速(4) | ⚪妥当(3.0) | FAIL_UWAHIGE | 4826.0 | 483,500 |  |  |
| 9065 Sankyu Inc. | choruko_reversal | ✅順調(4) | ⚪妥当(3.0) | FAIL_INSEN | 8366.0 | 842,500 |  |  |
| 9302 三井倉庫ホールディングス | choruko_reversal | ✅順調(4) | 🟡やや割高(2.0) | PASS | 3333.0 | 333,300 | reversal 3333.0/SL3284.0 |  |

> 📌【業態】倉庫業大手。総合物流業務に強み。国際サプライチェーン展開。不動産賃貸が収益。
> 【いま】終値3,333円・直近5日+0.97%（材料未確認）
> 【調子】✅順調（4/13） — 質注意
> 【水準】🟡やや割高（2.0/7）— PER19.9倍・PEG—・52週16.0% ／ 💰単元33.3万円
> 【戦略】当日終値3333.0円の指値で反転を取りにいく。SL3284.0円（直近5日安値）

| 5334 Niterra Co.,Ltd. | choruko_reversal | ✅順調(4) | 🔴過熱(1.0) | FAIL_INSEN | 8474.0 | 865,800 |  |  |
| 6135 牧野フライス製作所 | choruko_reversal | ✅順調(4) | 🔴過熱(0.0) | FAIL_UWAHIGE | 15400.0 | 1,533,000 |  |  |
| 4536 参天製薬 | choruko_reversal | ✅順調(4) | ⏸判定不能(—) | FAIL_INSEN | 1862.0 | 187,500 |  |  |
| 1861 Kumagai Gumi Co., Ltd. | choruko_reversal | ✅順調(3) | 💎割安(6.0) | FAIL_INSEN | 1303.0 | 130,400 |  |  |
| 1802 Obayashi Corporation | choruko_reversal | ✅順調(3) | ⚪妥当(3.0) | PASS | 2993.0 | 299,300 | reversal 2993.0/SL2925.0 |  |

> 📌【業態】総合建設大手。関西地盤で首都圏で都市開発。トンネルに強み。発電関連強化。
> 【いま】終値2,993円・直近5日+0.54%（材料未確認）
> 【調子】✅順調（3/13） — (質注意)
> 【水準】⚪妥当（3.0/7）— PER13.1倍・PEG—・52週32.0% ／ 💰単元29.9万円
> 【戦略】当日終値2993.0円の指値で反転を取りにいく。SL2925.0円（直近5日安値）

| 6586 Makita Corporation | choruko_reversal | ✅順調(3) | 🔴過熱(1.0) | FAIL_INSEN | 5300.0 | 530,900 |  |  |
| 456A ＨＵＭＡＮ　ＭＡＤＥ | choruko_reversal | ✅順調(3) | 🔴過熱(0.0) | FAIL_INSEN | 1581.0 | 172,100 |  |  |
| 6632 ＪＶＣケンウッド | choruko_reversal | ➖横ばい(2) | ⚪妥当(3.0) | FAIL_UWAHIGE | 1032.5 | 102,500 |  |  |
| 1975 朝日工業社 | choruko_reversal | ➖横ばい(2) | 🟡やや割高(2.0) | FAIL_INSEN | 3920.0 | 392,000 |  |  |
| 5105 Toyo Tire Corporation | choruko_reversal | ⚠減速(1) | ⚪妥当(3.0) | FAIL_INSEN | 3811.0 | 382,400 |  |  |
| 8111 Goldwin Inc. | choruko_reversal | ⚠減速(1) | ⚪妥当(3.0) | FAIL_UWAHIGE | 2170.0 | 218,500 |  |  |
| 1979 Taikisha Ltd. | choruko_reversal・granville_rebound・未マージPR由来 | ⚠減速(1) | 🟡やや割高(2.0) | FAIL_INSEN | 3895.0 | 390,000 |  |  |
| 1980 ダイダン | choruko_reversal | ⚠減速(1) | 🟡やや割高(2.0) | FAIL_UWAHIGE | 2794.0 | 274,900 |  |  |
| 6845 Azbil Corporation | choruko_reversal | ⚠減速(1) | 🔴過熱(1.0) | FAIL_INSEN | 1521.0 | 151,700 |  |  |
| 9533 東邦瓦斯 | choruko_reversal | 🔻悪化(0) | 🔴過熱(1.0) | FAIL_UWAHIGE | 1214.0 | 122,250 |  |  |
| 8366 滋賀銀行 | choruko_reversal | 取得不可(—) | ⚪妥当(3.0) | FAIL_INSEN | 2763.0 | 275,500 |  |  |
| 543A ＡＲＣＨＩＯＮ | choruko_reversal | 業績データ取得不可(—) | ⏸判定不能(—) | FAIL_INSEN | 274.0 | 27,300 |  |  |
| 7157 Lifenet Insurance Company | choruko_reversal | 業績データ取得不可(経常益予想非開示)(—) | ⏸判定不能(—) | FAIL_UWAHIGE | 1494.0 | 151,000 |  |  |
| 7480 スズデン | stf_kakuhen | 🚀確変(13) | ⚪妥当(3.0) | FAIL_INSEN | 3475.0 | 349,000 |  |  |
| 3131 シンデンハイ | stf_kakuhen | 🚀確変(12) | 🟢値頃(5.0) | FAIL_INSEN | 6020.0 | 620,000 |  |  |
| 6134 ＦＵＪＩ | stf_kakuhen・granville_rebound | 🚀確変(11) | 🟢値頃(5.0) | FAIL_INSEN | 7231.0 | 721,900 |  |  |
| 9308 乾汽船 | stf_kakuhen | 🔥絶好調(10) | ⚪妥当(4.0) | FAIL_UWAHIGE | 2102.0 | 210,400 |  |  |
| 3036 アルコニックス（アルコニクス） | stf_kakuhen | 🔥絶好調(9) | ⚪妥当(4.0) | FAIL_UWAHIGE | 3480.0 | 346,000 |  |  |
| 6324 ハーモニック・ドライブ・システムズ（ハーモニック） | stf_kakuhen・granville_rebound | 🔥絶好調(9) | ⚪妥当(4.0) | FAIL_INSEN | 5780.0 | 578,000 |  |  |
| 7433 伯東 | stf_kakuhen | 🔥絶好調(9) | ⚪妥当(4.0) | FAIL_UWAHIGE | 5290.0 | 529,000 |  |  |
| 7637 白銅 | stf_kakuhen | 🔥絶好調(9) | ⚪妥当(4.0) | FAIL_INSEN | 3755.0 | 382,000 |  |  |
| 9962 ミスミグループ本社 | stf_kakuhen | 🔥絶好調(9) | ⚪妥当(4.0) | FAIL_INSEN | 3667.0 | 366,600 |  |  |
| 6857 アドバンテスト | stf_kakuhen | 🔥絶好調(9) | ⚪妥当(3.0) | FAIL_INSEN | 34610.0 | 3,570,000 |  |  |
| 8084 ＲＹＯＤＥＮ | stf_kakuhen | 🔥絶好調(9) | ⚪妥当(3.0) | FAIL_UWAHIGE | 4740.0 | 472,000 |  |  |
| 4249 森六 | stf_kakuhen | 🔥絶好調(8) | 🟢値頃(5.0) | FAIL_UWAHIGE | 2936.0 | 290,900 |  |  |
| 6490 ＰＩＬＬＡＲ | stf_kakuhen | ⚡好調(7) | ⚪妥当(3.0) | FAIL_INSEN | 10140.0 | 1,030,000 |  |  |
| 147A ソラコム | stf_kakuhen | ⚡好調(7) | 🟡やや割高(2.0) | FAIL_UWAHIGE | 1038.0 | 103,900 |  |  |
| 3091 ブロンコビリー | granville_oshime・stf_kakuhen | ⚡好調(7) | 🟡やや割高(2.0) | FAIL_INSEN | 2735.0 | 278,000 |  |  |
| 8697 日本取引所グループ | stf_kakuhen | ⚡好調(7) | 🟡やや割高(2.0) | FAIL_INSEN | 2284.5 | 228,850 |  |  |
| 8388 阿波銀行 | stf_kakuhen | ⚡好調(6) | 🟡やや割高(2.0) | FAIL_UWAHIGE | 9950.0 | 929,000 |  |  |
| 7267 ホンダ | stf_kakuhen | ⚡好調(5) | ⚪妥当(3.0) | FAIL_INSEN | 1662.5 | 169,600 |  |  |
| 3289 Tokyu Fudosan Holdings Corp. | granville_tenkan・未マージPR由来 | ➖横ばい(2) | 🟢値頃(5.0) | FAIL_UWAHIGE | 1338.0 | 134,250 |  |  |
| 2733 Arata Corporation | granville_tenkan・未マージPR由来 | 🔻悪化(1) | 🟡やや割高(2.0) | FAIL_UWAHIGE | 2731.0 | 271,000 |  |  |
| 9861 Yoshinoya Holdings Co., Ltd. | granville_oshime・未マージPR由来 | ✅順調(3) | 🔴過熱(0.0) | FAIL_INSEN | 3785.0 | 385,800 |  |  |
| 9616 Kyoritsu Maintenance Co., Ltd. | granville_oshime・未マージPR由来 | ➖横ばい(2) | 🔴過熱(0.0) | PASS | 3432.0 | 343,200 | oshime 3368.5/SL3351.76 |  |

> 📌【業態】サービス業
> 【いま】終値3,432円・直近5日+1.96%（材料未確認）
> 【調子】➖横ばい（2/13） — (質注意)
> 【水準】🔴過熱（0.0/7）— PER17.3倍・PEG—・52週91.0% ／ 💰単元34.3万円
> 【戦略】3368.5円までの押し目を指値で待つ。SL3351.76円（25日線基準）

| 7581 Saizeriya Co., Ltd. | granville_rebound・未マージPR由来 | ⚡好調(6) | 🟡やや割高(2.0) | FAIL_UWAHIGE | 7220.0 | 731,000 |  |  |
| 4718 Waseda Academy Co., Ltd. | granville_rebound・未マージPR由来 | ✅順調(4) | 🟡やや割高(2.0) | PASS | 2541.0 | 254,100 | reversal 2541.0/SL2403.0 |  |

> 📌【業態】難関中高の進学塾「早稲田アカデミー」を運営。個別指導、社会人研修も展開。
> 【いま】終値2,541円・直近5日+4.70%（材料未確認）
> 【調子】✅順調（4/13）
> 【水準】🟡やや割高（2.0/7）— PER16.5倍・PEG2.14・52週60.0% ／ 💰単元25.4万円
> 【戦略】当日終値2541.0円の指値で反転を取りにいく。SL2403.0円（直近5日安値）

| 9044 NANKAI Co., Ltd. | granville_rebound・未マージPR由来 | ✅順調(3) | 🟡やや割高(2.0) | FAIL_INSEN | 3057.0 | 305,000 |  |  |
| 3191 Joyful Honda Co. Ltd. | granville_rebound・未マージPR由来 | ✅順調(3) | 🔴過熱(1.0) | PASS | 2292.0 | 229,200 | reversal 2292.0/SL2253.0 |  |

> 📌【業態】ホームセンター大手。茨城・千葉中心に関東で超大型店を展開。アークランズと統合へ。
> 【いま】終値2,292円・直近5日-0.35%（材料未確認）
> 【調子】✅順調（3/13） — (質注意)
> 【水準】🔴過熱（1.0/7）— PER20.9倍・PEG—・52週52.0% ／ 💰単元22.9万円
> 【戦略】当日終値2292.0円の指値で反転を取りにいく。SL2253.0円（直近5日安値）

| 1878 Daito Trust Construction Co., Ltd. | granville_rebound・未マージPR由来 | ⚠減速(1) | 🟡やや割高(2.0) | FAIL_INSEN | 3328.0 | 333,100 |  |  |

## グランビル銘柄
| コード 銘柄名 | 手法 | 業績 | 値頃感 | 判定 | 終値 | 単元金額 | 提案 | チップ |
|---|---|---|---|---|---|---|---|---|
| 269A Sapeet, Inc. | granville_tenkan | 🚀確変(11) | ⚪妥当(4.0) | FAIL_UWAHIGE | 2621.0 | 259,000 |  |  |
| 145A L is B Corp. | granville_tenkan | 🔥絶好調(10) | 🟢値頃(5.0) | FAIL_UWAHIGE | 910.0 | 89,700 |  |  |
| 4521 Kaken Pharmaceutical Co., Ltd. | granville_tenkan | 🔥絶好調(9) | ⚪妥当(4.0) | FAIL_INSEN | 3990.0 | 398,500 |  |  |
| 8151 TOYO Corporation | granville_tenkan | 🔥絶好調(9) | ⚪妥当(4.0) | FAIL_INSEN | 1959.0 | 197,200 |  |  |
| 3222 United Super Markets Holdings, Inc. | granville_tenkan | 🔥絶好調(9) | 🔴過熱(2.0) | PASS | 850.0 | 85,000 | momentum 851.0/SL799.0/上限859.51 |  |

> 📌【業態】イオン系、首都圏の食品スーパー最大手。マルエツ、カスミ、マックスバリュ関東が統合。
> 【いま】終値850円・直近5日+2.29%（材料未確認）
> 【調子】🔥絶好調（9/13）
> 【水準】🔴過熱（2.0/7）— PER1214.3倍・PEG12.72・52週34.0% ／ 💰単元8.5万円
> 【戦略】当日高値超えの逆指値851.0円で順張り参戦を検討。上限859.51円・SL799.0円目安

| 3491 GA technologies Co., Ltd. | granville_tenkan | 🔥絶好調(8) | 💎割安(6.0) | FAIL_INSEN | 1565.0 | 156,800 |  |  |
| 6425 Universal Entertainment Corporation | granville_tenkan | 🔥絶好調(8) | 🟢値頃(5.0) | FAIL_UWAHIGE | 718.0 | 73,000 |  |  |
| 7047 PORT INC. | granville_tenkan・granville_oshime | 🔥絶好調(8) | 🟢値頃(5.0) | PASS | 2307.0 | 230,700 | momentum 2320.0/SL2179.86/上限2343.2 |  |

> 📌【業態】サービス業
> 【いま】終値2,307円・直近5日-1.83%（材料未確認）
> 【調子】🔥絶好調（8/13） — E軸:進捗21.0%>=前年同期19.9%
> 【水準】🟢値頃（5.0/7）— PER9.1倍・PEG0.28・52週54.0% ／ 💰単元23.1万円
> 【戦略】当日高値超えの逆指値2320.0円で順張り参戦を検討。上限2343.2円・SL2179.86円目安

| 3623 Billing System Corporation | granville_tenkan | 🔥絶好調(8) | ⚪妥当(4.0) | FAIL_UWAHIGE | 1294.0 | 125,600 |  |  |
| 3968 セグエグループ | granville_tenkan | 🔥絶好調(8) | ⚪妥当(4.0) | FAIL_UWAHIGE | 642.0 | 63,800 |  |  |
| 6222 Shima Seiki Mfg. Ltd. | granville_tenkan | 🔥絶好調(8) | ⚪妥当(4.0) | FAIL_INSEN | 985.0 | 97,600 |  |  |
| 8086 ニプロ | granville_tenkan | 🔥絶好調(8) | ⚪妥当(4.0) | FAIL_INSEN | 1532.0 | 157,650 |  |  |
| 5020 ENEOS Holdings, Inc. | granville_tenkan | ⚡好調(7) | 🟢値頃(5.0) | FAIL_INSEN | 1331.0 | 134,150 |  |  |
| 5932 Sankyo Tateyama, Inc. | granville_tenkan | ⚡好調(7) | ⚪妥当(4.0) | FAIL_INSEN | 670.0 | 67,100 |  |  |
| 7744 ノーリツ鋼機 | granville_tenkan | ⚡好調(7) | ⚪妥当(4.0) | FAIL_INSEN | 2000.0 | 203,800 |  |  |
| 8793 NEC Capital Solutions Limited | granville_tenkan | ⚡好調(7) | ⚪妥当(4.0) | FAIL_INSEN | 4270.0 | 424,000 |  |  |
| 4507 Shionogi & Co., Ltd. | granville_tenkan | ⚡好調(7) | ⚪妥当(3.0) | FAIL_UWAHIGE | 2909.5 | 291,100 |  |  |
| 3116 Toyota Boshoku Corp. | granville_tenkan | ⚡好調(6) | 💎割安(6.0) | FAIL_INSEN | 2239.5 | 223,450 |  |  |
| 5592 Kusurinomadoguchi, Inc. | granville_tenkan | ⚡好調(6) | 💎割安(6.0) | FAIL_INSEN | 2722.0 | 270,800 |  |  |
| 8057 内田洋行 | granville_tenkan | ⚡好調(6) | 💎割安(6.0) | FAIL_UWAHIGE | 2267.0 | 222,900 |  |  |
| 2975 Star Mica Holdings Co., Ltd. | granville_tenkan | ⚡好調(6) | 🟢値頃(5.0) | FAIL_INSEN | 1599.0 | 159,700 |  |  |
| 6023 ダイハツインフィニアース | granville_tenkan | ⚡好調(6) | 🟢値頃(5.0) | PASS | 2998.0 | 299,800 | momentum 3001.0/SL2820.0/上限3031.01 |  |

> 📌【業態】船舶ディーゼル発電用補機の世界大手。コージェネ向けも。ダイハツ直系。
> 【いま】終値2,998円・直近5日+0.64%（材料未確認）
> 【調子】⚡好調（6/13）
> 【水準】🟢値頃（5.0/7）— PER10.8倍・PEG0.42・52週66.0% ／ 💰単元30.0万円
> 【戦略】当日高値超えの逆指値3001.0円で順張り参戦を検討。上限3031.01円・SL2820.0円目安

| 6718 アイホン | granville_tenkan | ⚡好調(6) | 🟢値頃(5.0) | FAIL_INSEN | 2888.0 | 286,800 |  |  |
| 4848 フルキャストホールディングス | granville_tenkan | ⚡好調(6) | ⚪妥当(3.0) | FAIL_INSEN | 1867.0 | 187,700 |  |  |
| 3048 BIC Cameras Inc. | granville_oshime・granville_tenkan | ⚡好調(6) | 🟡やや割高(2.0) | FAIL_INSEN | 1795.0 | 180,400 |  |  |
| 7911 TOPPAN Holdings Inc. | granville_tenkan・未マージPR由来 | ⚡好調(6) | 🟡やや割高(2.0) | FAIL_INSEN | 5001.0 | 504,600 |  | ⚡材料後出し |
| 8919 カチタス | granville_tenkan | ⚡好調(6) | 🔴過熱(1.0) | FAIL_UWAHIGE | 3855.0 | 370,000 |  |  |
| 547A ムニノバホールディングス（ムニノバＨＤ） | granville_tenkan・未マージPR由来 | ⚡好調(5) | 💎割安(7.0) | FAIL_INSEN | 452.0 | 45,500 |  |  |
| 2585 LIFEDRINK COMPANY INC. | granville_tenkan・未マージPR由来 | ⚡好調(5) | ⚪妥当(3.0) | FAIL_INSEN | 1548.0 | 165,000 |  |  |
| 6571 QB Net Holdings Co., Ltd. | granville_tenkan | ⚡好調(5) | ⚪妥当(3.0) | FAIL_INSEN | 1301.0 | 131,000 |  |  |
| 9037 ハマキョウレックス（ハマキョウ） | granville_tenkan・未マージPR由来 | ⚡好調(5) | 🟡やや割高(2.0) | PASS | 1884.0 | 188,400 | momentum 1885.0/SL1770.96/上限1903.85 |  |

> 📌【業態】3PL事業大手。物流業務の一括受託で急成長。通販拡大で個人向けも。
> 【いま】終値1,884円・直近5日+1.73%（材料未確認）
> 【調子】⚡好調（5/13） — E軸判定不能(進捗データ不足)
> 【水準】🟡やや割高（2.0/7）— PER12.9倍・PEG1.85・52週83.0% ／ 💰単元18.8万円
> 【戦略】当日高値超えの逆指値1885.0円で順張り参戦を検討。上限1903.85円・SL1770.96円目安

| 5885 GDEP ADVANCE,Inc. | granville_tenkan | ⚡好調(5) | 🔴過熱(1.0) | FAIL_UWAHIGE | 3295.0 | 318,000 |  |  |
| 2702 日本マクドナルド HD | granville_tenkan | ⚠減速(5) | 🔴過熱(0.0) | FAIL_INSEN | 8050.0 | 818,000 |  |  |
| 4847 インテリジェント　ウェイブ | granville_tenkan | ⚡好調(5) | 🔴過熱(0.0) | FAIL_UWAHIGE | 1354.0 | 133,000 |  |  |
| 208A 構造計画研究所ホールディングス | granville_tenkan | ✅順調(4) | 💎割安(6.0) | FAIL_UWAHIGE | 2967.0 | 298,100 |  |  |
| 5036 Japan Business Systems, Inc. | granville_tenkan・未マージPR由来 | ✅順調(4) | 💎割安(6.0) | FAIL_INSEN | 1601.0 | 158,200 |  |  |
| 1808 Haseko Corporation | granville_tenkan | ✅順調(4) | ⚪妥当(4.0) | PASS | 2896.0 | 289,600 | momentum 2900.0/SL2725.06/上限2929.0 |  |

> 📌【業態】マンション建築最大手。計画から施工まで一貫。独自ノウハウ持つ。サービス関連育成。
> 【いま】終値2,896円・直近5日+3.50%（材料未確認）
> 【調子】✅順調（4/13） — 進捗判定不能(自動抽出範囲外)
> 【水準】⚪妥当（4.0/7）— PER11.6倍・PEG1.0・52週44.0% ／ 💰単元29.0万円
> 【戦略】当日高値超えの逆指値2900.0円で順張り参戦を検討。上限2929.0円・SL2725.06円目安

| 6305 Hitachi Construction Machinery Co., Ltd. | granville_tenkan | ✅順調(4) | ⚪妥当(4.0) | FAIL_INSEN | 5819.0 | 593,600 |  |  |
| 9101 日本郵船 | granville_tenkan | ✅順調(4) | ⚪妥当(4.0) | FAIL_UWAHIGE | 6932.0 | 714,100 |  |  |
| 1911 Sumitomo Forestry Co., Ltd. | granville_tenkan・未マージPR由来 | 🔻悪化(4) | ⚪妥当(3.0) | FAIL_INSEN | 1344.0 | 134,700 |  |  |
| 7198 SBI ARUHI Corporation | granville_tenkan | ✅順調(4) | ⚪妥当(3.0) | FAIL_INSEN | 843.0 | 84,700 |  |  |
| 7611 ハイデイ日高 | granville_tenkan | ✅順調(4) | 🟡やや割高(2.0) | FAIL_UWAHIGE | 2993.0 | 299,200 |  |  |
| 9627 アインホールディングス | granville_tenkan | ✅順調(4) | 🟡やや割高(2.0) | FAIL_INSEN | 6133.0 | 618,000 |  |  |
| 8098 稲畑産業 | granville_tenkan | ✅順調(4) | 🔴過熱(1.0) | FAIL_UWAHIGE | 4300.0 | 423,500 |  |  |
| 160A As Partners CO.,LTD. | granville_tenkan | ✅順調(3) | 💎割安(7.0) | FAIL_INSEN | 1987.0 | 202,300 |  |  |
| 8056 ＢＩＰＲＯＧＹ | granville_tenkan | ✅順調(3) | 🟢値頃(5.0) | FAIL_UWAHIGE | 4656.0 | 462,900 |  |  |
| 1716 Daiichi Cutter Kogyo K.K. | granville_tenkan | ✅順調(3) | ⚪妥当(4.0) | FAIL_UWAHIGE | 1407.0 | 142,500 |  |  |
| 1898 世紀東急工業 | granville_tenkan | ✅順調(3) | ⚪妥当(4.0) | FAIL_INSEN | 1501.0 | 150,200 |  |  |
| 1925 大和ハウス工業（大和ハウス） | granville_tenkan・未マージPR由来 | 🔻悪化(3) | ⚪妥当(3.0) | FAIL_UWAHIGE | 4716.0 | 470,900 |  |  |
| 4826 ＣＩＪ | granville_tenkan | ✅順調(3) | 🔴過熱(1.0) | PASS | 545.0 | 54,500 | momentum 548.0/SL514.18/上限553.48 |  |

> 📌【業態】情報・通信業
> 【いま】終値545円・直近5日+1.11%（材料未確認）
> 【調子】✅順調（3/13） — E軸判定不能(進捗データ不足)
> 【水準】🔴過熱（1.0/7）— PER16.4倍・PEG3.73・52週59.0% ／ 💰単元5.5万円
> 【戦略】当日高値超えの逆指値548.0円で順張り参戦を検討。上限553.48円・SL514.18円目安

| 8570 イオンフィナンシャルサービス | granville_tenkan | 🔻悪化(3) | 🔴過熱(1.0) | FAIL_INSEN | 1719.0 | 172,400 |  |  |
| 1605 Inpex Corporation | granville_tenkan | ➖横ばい(2) | ⚪妥当(4.0) | FAIL_INSEN | 3856.0 | 387,800 |  |  |
| 7679 Yakuodo Holdings Co., Ltd. | granville_tenkan | ➖横ばい(2) | ⚪妥当(4.0) | FAIL_UWAHIGE | 1675.0 | 169,600 |  |  |
| 5851 Ryobi Limited | granville_tenkan | ➖横ばい(2) | ⚪妥当(3.0) | FAIL_INSEN | 2765.0 | 277,900 |  |  |
| 7231 トピー工業 | granville_tenkan | ➖横ばい(2) | ⚪妥当(3.0) | FAIL_INSEN | 3055.0 | 304,500 |  |  |
| 9503 Kansai Electric Power Company, Incorporated | granville_tenkan | 🔻悪化(2) | ⚪妥当(3.0) | FAIL_UWAHIGE | 2605.0 | 259,150 |  |  |
| 2282 NH Foods Limited | granville_tenkan | ➖横ばい(2) | 🟡やや割高(2.0) | FAIL_INSEN | 6332.0 | 640,700 |  |  |
| 2292 S Foods Inc. | granville_tenkan | ➖横ばい(2) | 🟡やや割高(2.0) | FAIL_INSEN | 2946.0 | 293,700 |  |  |
| 9869 加藤産業 | granville_tenkan | ➖横ばい(2) | 🟡やや割高(2.0) | FAIL_INSEN | 6620.0 | 660,000 |  |  |
| 9041 近鉄グループホールディングス | granville_tenkan | ➖横ばい(2) | 🔴過熱(1.0) | FAIL_INSEN | 3512.0 | 358,400 |  |  |
| 5302 日本カーボン | granville_tenkan | ➖横ばい(2) | 🔴過熱(0.0) | PASS | 5020.0 | 502,000 | momentum 5050.0/SL4737.6/上限5100.5 |  |

> 📌【業態】炭素製品の大手。電極や半導体向け特殊品、炭素繊維、リチウム電池向けなど。
> 【いま】終値5,020円・直近5日+1.93%（材料未確認）
> 【調子】➖横ばい（2/13） — E軸:進捗32.8%>=前年同期29.6%
> 【水準】🔴過熱（0.0/7）— PER19.8倍・PEG—・52週86.0% ／ 💰単元50.2万円
> 【戦略】当日高値超えの逆指値5050.0円で順張り参戦を検討。上限5100.5円・SL4737.6円目安／⚠1単元でリスク枠超過（31240円）

| 2317 システナ | granville_tenkan | ⚠減速(1) | ⚪妥当(3.0) | FAIL_INSEN | 443.0 | 44,400 |  |  |
| 3880 大王製紙 | granville_tenkan | 🔻悪化(1) | ⚪妥当(3.0) | FAIL_INSEN | 985.0 | 98,400 |  |  |
| 5406 神戸製鋼所（神戸鋼） | granville_tenkan・未マージPR由来 | ⚠減速(1) | ⚪妥当(3.0) | FAIL_INSEN | 2022.0 | 202,500 |  |  |
| 9404 Nippon Television Holdings, Inc. | granville_tenkan | 🔻悪化(1) | ⚪妥当(3.0) | FAIL_INSEN | 3012.0 | 301,700 |  |  |
| 6770 Alps Alpine Co., Ltd. | granville_tenkan・未マージPR由来 | ⚠減速(1) | 🟡やや割高(2.0) | FAIL_UWAHIGE | 2211.5 | 219,450 |  |  |
| 8276 平和堂 | granville_tenkan・未マージPR由来 | ⚠減速(1) | 🟡やや割高(2.0) | FAIL_UWAHIGE | 2704.0 | 272,100 |  |  |
| 3865 北越コーポレーション（北越コーポ） | granville_tenkan・未マージPR由来 | 🔻悪化(1) | 🔴過熱(1.0) | FAIL_INSEN | 919.0 | 92,000 |  |  |
| 7943 Nichiha Corporation | granville_tenkan | ⚠減速(1) | 🔴過熱(1.0) | FAIL_INSEN | 3120.0 | 312,500 |  |  |
| 2982 ＡＤワークスグループ（ＡＤＷＧ） | granville_tenkan・未マージPR由来 | ⚠減速(1) | ⏸判定不能(—) | FAIL_UWAHIGE | 428.0 | 42,300 |  |  |
| 4375 Safie Inc. | changepoint・変化点🔔・未マージPR由来・granville_tenkan | 取得不可(—) | 💎割安(7.0) | FAIL_UWAHIGE | 686.0 | 68,000 |  |  |
| 2768 Sojitz Corp. | granville_tenkan | 業績データ取得不可(経常益予想非開示)(—) | ⚪妥当(3.5) | PASS | 5589.0 | 558,900 | momentum 5610.0/SL5264.0/上限5666.1 |  |

> 📌【業態】卸売業
> 【いま】終値5,589円・直近5日+1.18%（材料未確認）
> 【調子】—（—/13） — 進捗判定不能(自動抽出範囲外)
> 【水準】⚪妥当（3.5/7）— PER8.9倍・PEG—・52週51.0% ／ 💰単元55.9万円
> 【戦略】当日高値超えの逆指値5610.0円で順張り参戦を検討。上限5666.1円・SL5264.0円目安／⚠1単元でリスク枠超過（34600円）

| 3003 ヒューリック | granville_tenkan | 業績データ取得不可(—) | 🔴過熱(2.8) | FAIL_UWAHIGE | 1793.0 | 180,350 |  |  |
| 8425 Mizuho Leasing Company, Limited | granville_tenkan | 業績データ取得不可(—) | 🔴過熱(2.8) | FAIL_INSEN | 1380.0 | 137,600 |  |  |
| 1833 Okumura Corporation | granville_tenkan・未マージPR由来 | —(—) | —(—) | FAIL_INSEN | 5860.0 | — |  |  |
| 2986 LA Holdings Co.,Ltd | granville_tenkan・未マージPR由来 | —(—) | —(—) | FAIL_UWAHIGE | 2843.0 | — |  |  |
| 3765 ガンホー・オンライン・エンターテイメント | granville_tenkan | 取得不可(—) | ⏸判定不能(—) | FAIL_UWAHIGE | 2440.0 | 243,300 |  |  |
| 3993 PKSHA Technology, Inc. | granville_tenkan | 業績データ取得不可(—) | ⏸判定不能(—) | FAIL_UWAHIGE | 3270.0 | 320,000 |  |  |
| 4666 PARK24 Co., Ltd. | granville_tenkan・未マージPR由来 | —(—) | —(—) | FAIL_INSEN | 1986.0 | — |  |  |
| 4765 ＳＢＩグローバルアセットマネジメント | granville_tenkan | 判定保留(—) | ⏸判定不能(—) | PASS | 648.0 | 64,800 | momentum 649.0/SL609.12/上限655.49 |  |

> 📌【業態】金融機関の運用受託や投信等金融情報の評価・データ提供。指数連動投信も。
> 【いま】終値648円・直近5日+4.85%（材料未確認）
> 【調子】—（—/13） — 判定保留(変則決算): 前期比2.41倍(売上急変・M&A/事業譲渡等の可能性)
> 【水準】⏸判定不能（—/7）— PER—倍・PEG—・52週92.0% ／ 💰単元6.5万円
> 【戦略】当日高値超えの逆指値649.0円で順張り参戦を検討。上限655.49円・SL609.12円目安

| 5703 Nippon Light Metal Holdings Company, Ltd. | granville_tenkan・未マージPR由来 | —(—) | —(—) | FAIL_INSEN | 3035.0 | — |  |  |
| 6167 FUJI DIE Co., Ltd. | granville_tenkan・未マージPR由来 | —(—) | —(—) | FAIL_UWAHIGE | 1048.0 | — |  |  |
| 6339 Sintokogio,Ltd. | granville_tenkan・未マージPR由来 | —(—) | —(—) | FAIL_INSEN | 1208.0 | — |  |  |
| 6794 Foster Electric Company, Limited | granville_tenkan・未マージPR由来 | —(—) | —(—) | FAIL_INSEN | 2982.0 | — |  |  |
| 7287 Nippon Seiki Co., Ltd. | granville_tenkan | 業績データ取得不可(経常益予想非開示)(—) | ⏸判定不能(—) | FAIL_INSEN | 2708.0 | 259,400 |  |  |
| 8562 Fukushima Bank, Ltd. | granville_tenkan・未マージPR由来 | —(—) | —(—) | FAIL_UWAHIGE | 372.0 | — |  |  |
| 9628 San Holdings,Inc. | granville_tenkan | 判定保留(変則決算)(—) | ⏸判定不能(—) | FAIL_INSEN | 1377.0 | 138,800 |  |  |
| 7806 Ｇ−ＭＴＧ | granville_oshime | 🚀確変(11) | ⚪妥当(3.0) | FAIL_INSEN | 8940.0 | 898,000 |  |  |
| 4419 Ｆｉｎａｔｅｘｔホールディングス | granville_oshime・granville_rebound・変化点🔔・未マージPR由来 | 🔥絶好調(10) | ⚪妥当(4.0) | FAIL_UWAHIGE | 1450.0 | 144,800 |  |  |
| 6136 OSG Corp | granville_oshime・granville_rebound・未マージPR由来 | 🔥絶好調(10) | ⚪妥当(3.0) | FAIL_INSEN | 3730.0 | 377,600 |  |  |
| 3498 Kasumigaseki Capital Co., Ltd. | granville_oshime | 🔥絶好調(9) | 💎割安(6.0) | FAIL_UWAHIGE | 8090.0 | 765,000 |  |  |
| 6103 Okuma Corporation | granville_oshime・granville_rebound | 🔥絶好調(9) | 🟢値頃(5.0) | FAIL_INSEN | 4865.0 | 490,500 |  |  |
| 9279 GIFT HOLDINGS INC. | granville_oshime | 🔥絶好調(9) | ⚪妥当(3.0) | PASS | 5120.0 | 512,000 | ⛔型不一致: 既に支持帯以下 | 📋カルテ窓 09/14(残12営業日) |

> 📌【業態】「横浜家系」などのラーメン店を運営。食材や開業のプロデュース事業に注力。
> 【いま】終値5,120円・直近5日+1.99%（材料未確認）
> 【調子】🔥絶好調（9/13）
> 【水準】⚪妥当（3.0/7）— PER34.0倍・PEG0.72・52週86.0% ／ 💰単元51.2万円
> 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）

| 1407 West Holdings Corporation | granville_oshime | 🔥絶好調(8) | 🟢値頃(5.0) | FAIL_INSEN | 2727.0 | 266,200 |  |  |
| 8008 Yondoshi Holdings, Inc. | granville_oshime・未マージPR由来 | 🔥絶好調(8) | ⚪妥当(3.0) | FAIL_INSEN | 2164.0 | 216,400 |  |  |
| 4413 ボードルア | granville_oshime・granville_rebound | 🔥絶好調(8) | 🔴過熱(0.0) | FAIL_INSEN | 2968.0 | 296,800 |  |  |
| 7089 For Startups, Inc. | granville_oshime | ⚡好調(7) | 🟢値頃(5.0) | FAIL_INSEN | 1514.0 | 152,200 |  |  |
| 2590 DyDo Group Holdings, Inc. | granville_oshime | ⚡好調(7) | ⚪妥当(4.2) | FAIL_INSEN | 3010.0 | 309,000 |  | ⚡材料後出し |
| 166A タスキホールディングス | granville_oshime | ⚡好調(7) | ⚪妥当(4.0) | FAIL_INSEN | 1203.0 | 119,800 |  |  |
| 2874 横浜冷凍 | granville_oshime・granville_rebound | ⚠減速(7) | ⚪妥当(4.0) | PASS | 2197.0 | 219,700 | oshime 2138.5/SL2127.88 |  |

> 📌【業態】冷蔵倉庫大手。水産品中心に農畜産物の加工、販売も。物流センター拡張。
> 【いま】終値2,197円・直近5日+1.06%（材料未確認）
> 【調子】⚠減速（7/13） — A成長率0以下のためレバレッジ計算不可(C=0)
> 【水準】⚪妥当（4.0/7）— PER27.1倍・PEG0.36・52週67.0% ／ 💰単元22.0万円
> 【戦略】2138.5円までの押し目を指値で待つ。SL2127.88円（25日線基準）

| 8522 名古屋銀行（名古屋銀） | granville_oshime・未マージPR由来 | ⚡好調(7) | ⚪妥当(4.0) | FAIL_INSEN | 7060.0 | 683,000 |  |  |
| 9902 Nichiden Corporation | granville_oshime・未マージPR由来 | ⚡好調(7) | ⚪妥当(4.0) | FAIL_INSEN | 3060.0 | 307,500 |  |  |
| 7609 Daitron Co., Ltd. | granville_oshime・未マージPR由来 | ⚡好調(6) | 🟢値頃(5.0) | FAIL_INSEN | 4090.0 | 397,000 |  |  |
| 2602 日清オイリオグループ | granville_oshime | ⚡好調(6) | 🟡やや割高(2.0) | FAIL_INSEN | 2049.0 | 205,100 |  |  |
| 7716 Nakanishi Inc. | granville_oshime | ⚡好調(6) | 🔴過熱(1.0) | FAIL_INSEN | 3165.0 | 320,500 |  |  |
| 7616 コロワイド | granville_oshime | ⚡好調(6) | 🔴過熱(0.0) | PASS | 2101.0 | 210,100 | oshime 2053.0/SL2042.74 |  |

> 📌【業態】外食大手。居酒屋中心に直営展開。傘下にレインズ、アトム、カッパクリエ、大戸屋など。
> 【いま】終値2,101円・直近5日+4.45%（材料未確認）
> 【調子】⚡好調（6/13） — 経常予想非開示のため最終利益成長率で代替(+19.6%)
> 【水準】🔴過熱（0.0/7）— PER105.6倍・PEG5.39・52週88.0% ／ 💰単元21.0万円
> 【戦略】2053.0円までの押し目を指値で待つ。SL2042.74円（25日線基準）

| 2780 Komehyo Holdings Co., Ltd. | granville_oshime | ⚡好調(5) | 🟢値頃(5.0) | FAIL_INSEN | 5100.0 | 505,000 |  |  |
| 6284 Nissei ASB Machine Co., Ltd. | changepoint・granville_oshime・変化点🔔 | ⚡好調(5) | 🟢値頃(5.0) | FAIL_UWAHIGE | 8900.0 | 881,000 |  |  |
| 7888 三光合成 | granville_oshime | ⚡好調(5) | ⚪妥当(4.0) | FAIL_INSEN | 910.0 | 91,600 |  |  |
| 8923 Tosei Corporation | granville_oshime | ⚡好調(5) | ⚪妥当(4.0) | FAIL_INSEN | 1834.0 | 182,600 |  |  |
| 7350 Okinawa Financial Group, Inc. | granville_oshime・未マージPR由来 | ⚡好調(5) | ⚪妥当(3.0) | PASS | 7800.0 | 780,000 | oshime 7613.9/SL7576.0 |  |

> 📌【業態】銀行業
> 【いま】終値7,800円・直近5日+1.43%（材料未確認）
> 【調子】⚡好調（5/13） — (質注意)
> 【水準】⚪妥当（3.0/7）— PER13.9倍・PEG1.29・52週90.0% ／ 💰単元78.0万円
> 【戦略】7613.9円までの押し目を指値で待つ。SL7576.0円（25日線基準）

| 7970 信越ポリマー | granville_oshime | ⚡好調(5) | ⚪妥当(3.0) | FAIL_INSEN | 2244.0 | 224,300 |  |  |
| 7085 カーブスホールディングス | granville_oshime | ⚡好調(5) | 🟡やや割高(2.0) | FAIL_INSEN | 960.0 | 97,400 |  |  |
| 9517 イーレックス | granville_oshime | ⚡好調(5) | 🟡やや割高(2.0) | FAIL_INSEN | 875.0 | 87,100 |  |  |
| 9934 Inaba Denki Sangyo Co.,Ltd. | granville_oshime・未マージPR由来 | ⚡好調(5) | 🟡やや割高(2.0) | PASS | 3025.0 | 302,500 | oshime 2953.4/SL2938.66 |  |

> 📌【業態】卸売業
> 【いま】終値3,025円・直近5日+2.65%（材料未確認）
> 【調子】⚡好調（5/13） — E軸判定不能(進捗データ不足)
> 【水準】🟡やや割高（2.0/7）— PER14.4倍・PEG1.73・52週94.0% ／ 💰単元30.2万円
> 【戦略】2953.4円までの押し目を指値で待つ。SL2938.66円（25日線基準）

| 3479 TKP Corporation | granville_oshime | ⚡好調(5) | 🔴過熱(1.0) | PASS | 1898.0 | 189,800 | oshime 1882.1/SL1872.76 |  |

> 📌【業態】不動産業
> 【いま】終値1,898円・直近5日+0.42%（材料未確認）
> 【調子】⚡好調（5/13） — E軸判定不能(進捗データ不足)
> 【水準】🔴過熱（1.0/7）— PER17.2倍・PEG2.6・52週46.0% ／ 💰単元19.0万円
> 【戦略】1882.1円までの押し目を指値で待つ。SL1872.76円（25日線基準）

| 4258 AMIYA Corporation | granville_oshime・未マージPR由来 | ⚡好調(5) | 🔴過熱(1.0) | PASS | 4330.0 | 433,000 | ⛔型不一致: 既に支持帯以下 |  |

> 📌【業態】情報・通信業
> 【いま】終値4,330円・直近5日-7.38%（材料未確認）
> 【調子】⚡好調（5/13） — (質注意)
> 【水準】🔴過熱（1.0/7）— PER41.0倍・PEG3.07・52週70.0% ／ 💰単元43.3万円
> 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）

| 9828 ＧＥＮＫＩ　ＧＬＯＢＡＬ　ＤＩＮＩＮＧ　ＣＯＮＣＥＰＴＳ | granville_oshime | ⚡好調(5) | 🔴過熱(1.0) | FAIL_INSEN | 3510.0 | 356,500 |  |  |
| 6454 Max Co., Ltd. | granville_oshime・未マージPR由来 | ⚡好調(5) | 🔴過熱(0.0) | FAIL_UWAHIGE | 1845.0 | 181,700 |  |  |
| 2288 Marudai Food Co., Ltd. | granville_oshime | ✅順調(4) | 🟢値頃(5.0) | FAIL_INSEN | 2254.0 | 225,900 |  |  |
| 5384 Fujimi Incorporated | granville_oshime | ✅順調(4) | 🔴過熱(1.0) | FAIL_INSEN | 3620.0 | 363,000 |  |  |
| 6925 ウシオ電機 | granville_oshime | ✅順調(4) | 🔴過熱(1.0) | FAIL_INSEN | 3961.0 | 393,600 |  |  |
| 9031 Nishi-Nippon Railroad Co., Ltd. | granville_oshime | 🔻悪化(4) | 🔴過熱(1.0) | FAIL_INSEN | 3104.0 | 310,800 |  |  |
| 7867 Tomy Company, Ltd. | granville_oshime | ✅順調(4) | 🔴過熱(0.0) | FAIL_INSEN | 3665.0 | 369,900 |  |  |
| 4553 Towa Pharmaceutical Co., Ltd. | granville_oshime | ✅順調(3) | ⚪妥当(4.0) | FAIL_INSEN | 3930.0 | 396,000 |  |  |
| 8876 リログループ | granville_oshime | ✅順調(3) | 🟡やや割高(2.0) | FAIL_UWAHIGE | 2161.0 | 218,900 |  |  |
| 5232 Sumitomo Osaka Cement Co., Ltd. | granville_oshime | ✅順調(3) | 🔴過熱(1.0) | PASS | 5769.0 | 576,900 | oshime 5696.1/SL5667.72 |  |

> 📌【業態】セメント大手、国内高シェア。廃棄物再資源化で先行。新素材や電池素材事業も。
> 【いま】終値5,769円・直近5日+3.18%（材料未確認）
> 【調子】✅順調（3/13） — 質注意
> 【水準】🔴過熱（1.0/7）— PER18.3倍・PEG27.74・52週74.0% ／ 💰単元57.7万円
> 【戦略】5696.1円までの押し目を指値で待つ。SL5667.72円（25日線基準）

| 6055 Japan Material Co., Ltd. | granville_oshime | ✅順調(3) | 🔴過熱(1.0) | PASS | 2215.0 | 221,500 | oshime 2202.9/SL2191.92 |  |

> 📌【業態】半導体製造向け特殊ガス供給装置製販。3D画像処理ツールや太陽光発電も。
> 【いま】終値2,215円・直近5日+6.34%（材料未確認）
> 【調子】✅順調（3/13） — E軸判定不能(進捗データ不足)
> 【水準】🔴過熱（1.0/7）— PER21.1倍・PEG8.45・52週59.0% ／ 💰単元22.1万円
> 【戦略】2202.9円までの押し目を指値で待つ。SL2191.92円（25日線基準）

| 6432 Takeuchi Mfg.Co., Ltd. | granville_oshime | ✅順調(3) | 🔴過熱(1.0) | FAIL_UWAHIGE | 7750.0 | 755,000 |  |  |
| 6966 Mitsui High-Tec, Inc. | granville_oshime | ✅順調(3) | 🔴過熱(1.0) | FAIL_INSEN | 938.0 | 93,800 |  |  |
| 9274 ＫＰＰグループホールディングス | granville_oshime | ✅順調(3) | 🔴過熱(1.0) | FAIL_INSEN | 1103.0 | 109,600 |  |  |
| 9882 Yellow Hat Ltd. | granville_oshime・未マージPR由来 | ✅順調(3) | 🔴過熱(1.0) | FAIL_INSEN | 1783.0 | 179,100 |  |  |
| 1375 Yukiguni Factory Co., Ltd. | granville_oshime | ✅順調(3) | 🔴過熱(0.0) | FAIL_UWAHIGE | 1178.0 | 117,400 |  |  |
| 2659 SAN-A CO., LTD. | granville_oshime | ✅順調(3) | 🔴過熱(0.0) | FAIL_INSEN | 3365.0 | 338,000 |  |  |
| 7956 ピジョン | granville_oshime | ✅順調(3) | 🔴過熱(0.0) | FAIL_INSEN | 2122.5 | 214,900 |  |  |
| 6590 芝浦メカトロニクス | granville_oshime | ➖横ばい(2) | 🔴過熱(1.0) | FAIL_INSEN | 4110.0 | 396,500 |  |  |
| 7278 Exedy Corporation | granville_oshime | ➖横ばい(2) | 🔴過熱(1.0) | FAIL_INSEN | 6160.0 | 620,000 |  |  |
| 8101 GSI Creos Corporation | granville_oshime | ⚠減速(2) | 🔴過熱(1.0) | PASS | 2747.0 | 274,700 | oshime 2720.2/SL2706.64 |  |

> 📌【業態】卸売業
> 【いま】終値2,747円・直近5日-2.07%（材料未確認）
> 【調子】⚠減速（2/13） — E軸判定不能(進捗データ不足)
> 【水準】🔴過熱（1.0/7）— PER12.8倍・PEG—・52週90.0% ／ 💰単元27.5万円
> 【戦略】2720.2円までの押し目を指値で待つ。SL2706.64円（25日線基準）

| 9247 TRE HOLDINGS CORPORATION | granville_oshime・granville_rebound | 🔻悪化(2) | 🔴過熱(1.0) | FAIL_INSEN | 1956.0 | 197,100 |  |  |
| 2175 SMS Co., Ltd. | granville_oshime | ➖横ばい(2) | 🔴過熱(0.0) | FAIL_UWAHIGE | 2412.0 | 238,200 |  |  |
| 3076 Ai Holdings Corporation | granville_oshime | ➖横ばい(2) | 🔴過熱(0.0) | FAIL_INSEN | 2967.0 | 296,200 |  |  |
| 4228 Sekisui Kasei Co., Ltd. | granville_oshime | ⚠減速(1) | ⚪妥当(4.0) | FAIL_INSEN | 595.0 | 59,500 |  |  |
| 6638 ミマキエンジニアリング | granville_oshime | ⚠減速(1) | ⚪妥当(3.0) | FAIL_INSEN | 1984.0 | 198,100 |  |  |
| 2001 NIPPN Corporation | granville_oshime | ⚠減速(1) | 🔴過熱(1.0) | FAIL_INSEN | 2904.0 | 294,500 |  |  |
| 2810 ハウス食品グループ本社 | granville_oshime・granville_rebound | ⚠減速(1) | 🔴過熱(1.0) | FAIL_INSEN | 3733.0 | 375,100 |  |  |
| 3151 バイタルケーエスケー・ホールディングス（バイタルＫＳ） | granville_oshime・granville_rebound・未マージPR由来 | 🔻悪化(1) | 🔴過熱(1.0) | FAIL_INSEN | 1665.0 | 167,100 |  |  |
| 6333 TEIKOKU Corp. | granville_oshime | ⚠減速(1) | 🔴過熱(1.0) | FAIL_INSEN | 3430.0 | 343,000 |  |  |
| 7981 Takara standard Co., Ltd. | granville_oshime・granville_rebound | ⚠減速(1) | 🔴過熱(1.0) | FAIL_INSEN | 3115.0 | 311,500 |  |  |
| 9324 安田倉庫（安田倉） | granville_oshime・未マージPR由来 | ⚠減速(1) | 🔴過熱(1.0) | FAIL_INSEN | 2537.0 | 253,300 |  |  |
| 7128 UNISOL Holdings Corporation | granville_oshime | ⚠減速(1) | 🔴過熱(0.0) | FAIL_UWAHIGE | 2826.0 | 282,100 |  |  |
| 8242 エイチ・ツー・オー　リテイリング | granville_oshime・未マージPR由来 | ⚠減速(1) | 🔴過熱(0.0) | FAIL_INSEN | 3019.0 | 301,900 |  |  |
| 8361 大垣共立銀行 | granville_oshime | 取得不可(—) | ⚪妥当(4.0) | FAIL_INSEN | 8150.0 | 794,000 |  |  |
| 8367 南都銀行 | granville_oshime | 取得不可(—) | ⚪妥当(4.0) | FAIL_INSEN | 1922.0 | 193,300 |  |  |
| 4415 BROAD ENTERPRISE CO.,LTD. | granville_rebound・granville_oshime | 業績データ取得不可(—) | ⚪妥当(3.0) | PASS | 1422.0 | 142,200 | oshime 1377.9/SL1371.0 |  |

> 📌【業態】マンション向け高速インターネットやIoTインターフォンシステムの販売。全戸一括でマンション管理も。
> 【いま】終値1,422円・直近5日+3.95%（材料未確認）
> 【調子】—（—/13）
> 【水準】⚪妥当（3.0/7）— PER—倍・PEG—・52週79.0% ／ 💰単元14.2万円
> 【戦略】1377.9円までの押し目を指値で待つ。SL1371.0円（25日線基準）

| 8544 Keiyo Bank, Ltd. | granville_oshime | 取得不可(—) | ⚪妥当(3.0) | FAIL_UWAHIGE | 2787.0 | 271,200 |  |  |
| 7184 富山第一銀行 | granville_oshime | 取得不可(—) | 🔴過熱(1.0) | FAIL_UWAHIGE | 3400.0 | 337,500 |  |  |
| 8387 Shikoku Bank Ltd. | granville_oshime | 取得不可(—) | 🔴過熱(0.0) | PASS | 3545.0 | 354,500 | oshime 3447.8/SL3430.6 |  |

> 📌【業態】銀行業
> 【いま】終値3,545円・直近5日+5.19%（材料未確認）
> 【調子】—（—/13） — 通期予想売上高(経常収益代替も含め)が非開示のためA/C軸を算出不可
> 【水準】🔴過熱（0.0/7）— PER16.9倍・PEG—・52週94.0% ／ 💰単元35.5万円
> 【戦略】3447.8円までの押し目を指値で待つ。SL3430.6円（25日線基準）

| 8511 日本証券金融 | granville_oshime | 取得不可(—) | 🔴過熱(0.0) | PASS | 2519.0 | 251,900 | oshime 2478.5/SL2466.2 |  |

> 📌【業態】その他金融業
> 【いま】終値2,519円・直近5日+1.49%（材料未確認）
> 【調子】—（—/13）
> 【水準】🔴過熱（0.0/7）— PER18.5倍・PEG3.45・52週91.0% ／ 💰単元25.2万円
> 【戦略】2478.5円までの押し目を指値で待つ。SL2466.2円（25日線基準）

| 3989 シェアリングテクノロジー | granville_oshime | 業績データ取得不可(—) | ⏸判定不能(—) | FAIL_INSEN | 1563.0 | 157,000 |  |  |
| 4051 GMO Financial Gate, Inc. | granville_oshime・未マージPR由来 | —(—) | —(—) | FAIL_INSEN | 6420.0 | — |  |  |
| 4092 Nippon Chemical Industrial Co., Ltd. | granville_oshime・未マージPR由来 | —(—) | —(—) | FAIL_INSEN | 5370.0 | — |  |  |
| 4417 Global Security Experts Inc. | granville_oshime・未マージPR由来 | —(—) | —(—) | FAIL_UWAHIGE | 4640.0 | — |  |  |
| 4722 Future Corporation | granville_oshime | 取得不可(—) | ⏸判定不能(—) | FAIL_INSEN | 2450.0 | 244,800 |  |  |
| 4968 Arakawa Chemical Industries, Ltd. | granville_oshime・未マージPR由来 | —(—) | —(—) | FAIL_INSEN | 2173.0 | — |  |  |
| 5186 Nitta Corporation | granville_oshime・未マージPR由来 | —(—) | —(—) | FAIL_INSEN | 6860.0 | — |  |  |
| 6588 Toshiba Tec Corp. | granville_oshime・未マージPR由来 | —(—) | —(—) | FAIL_INSEN | 3140.0 | — |  |  |
| 7860 Avex Inc. | granville_oshime | 業績データ取得不可(—) | ⏸判定不能(—) | FAIL_INSEN | 1282.0 | 129,900 |  |  |
| 8628 松井証券 | granville_oshime・未マージPR由来 | 業績データ取得不可(—) | ⏸判定不能(—) | PASS | 1180.0 | 118,000 | oshime 1098.9/SL1093.48 |  |

> 📌【業態】証券・商品
> 【いま】終値1,180円・直近5日+8.26%（材料未確認）
> 【調子】—（—/13） — 通期予想が非開示(会社側未公表)
> 【水準】⏸判定不能（—/7）— PER—倍・PEG—・52週100.0% ／ 💰単元11.8万円
> 【戦略】1098.9円までの押し目を指値で待つ。SL1093.48円（25日線基準）

| 8707 岩井コスモホールディングス | granville_oshime | 取得不可(—) | ⏸判定不能(—) | PASS | 4730.0 | 473,000 | oshime 4379.6/SL4357.8 |  |

> 📌【業態】証券・商品
> 【いま】終値4,730円・直近5日+3.96%（材料未確認）
> 【調子】—（—/13）
> 【水準】⏸判定不能（—/7）— PER—倍・PEG—・52週100.0% ／ 💰単元47.3万円
> 【戦略】4379.6円までの押し目を指値で待つ。SL4357.8円（25日線基準）

| 4047 Kanto Denka Kogyo Co., Ltd. | granville_rebound・未マージPR由来 | 🔥絶好調(10) | ⚪妥当(4.0) | FAIL_INSEN | 2393.0 | 233,300 |  |  |
| 6613 Ｇ−ＱＤレーザ | granville_rebound | 🔥絶好調(10) | 🔴過熱(2.0) | FAIL_INSEN | 2424.0 | 245,200 |  |  |
| 3449 Technoflex Corporation | granville_rebound・未マージPR由来 | 🔥絶好調(9) | 🟢値頃(5.0) | PASS | 4020.0 | 402,000 | reversal 4020.0/SL3660.0 |  |

> 📌【業態】金属製品
> 【いま】終値4,020円・直近5日+0.37%（材料未確認）
> 【調子】🔥絶好調（9/13）
> 【水準】🟢値頃（5.0/7）— PER18.0倍・PEG0.36・52週28.0% ／ 💰単元40.2万円
> 【戦略】当日終値4020.0円の指値で反転を取りにいく。SL3660.0円（直近5日安値）／⚠1単元でリスク枠超過（36000円）

| 150A JSH | granville_rebound | 🔥絶好調(9) | ⚪妥当(3.0) | FAIL_INSEN | 741.0 | 76,500 |  |  |
| 9147 ＮＩＰＰＯＮ　ＥＸＰＲＥＳＳ　ホールディングス | granville_rebound | 🔥絶好調(9) | ⚪妥当(3.0) | FAIL_INSEN | 5735.0 | 571,300 |  |  |
| 4424 Amazia, Inc. | granville_rebound | 🔥絶好調(8) | 💎割安(7.0) | FAIL_INSEN | 342.0 | 33,200 |  |  |
| 205A ロゴスホールディングス（ロゴスＨＤ） | granville_rebound・未マージPR由来 | 🔥絶好調(8) | 💎割安(6.0) | FAIL_INSEN | 1676.0 | 168,100 |  |  |
| 4420 イーソル | granville_rebound | 🔥絶好調(8) | 🟢値頃(5.0) | FAIL_UWAHIGE | 685.0 | 67,800 |  |  |
| 6125 Okamoto Machine Tool Works,Ltd. | granville_rebound・未マージPR由来 | 🔥絶好調(8) | 🟢値頃(5.0) | FAIL_INSEN | 4835.0 | 489,500 |  |  |
| 9006 Keikyu Corporation | granville_rebound | 🔥絶好調(8) | 🟢値頃(5.0) | FAIL_UWAHIGE | 1568.5 | 158,600 |  |  |
| 4392 FIG | granville_rebound | 🔥絶好調(8) | 🟡やや割高(2.0) | PASS | 1155.0 | 115,500 | reversal 1155.0/SL978.0 |  |

> 📌【業態】情報・通信業
> 【いま】終値1,155円・直近5日-11.22%（材料未確認）
> 【調子】🔥絶好調（8/13） — E軸=四半期経常ペース比較で近似(累計進捗率は未算出)
> 【水準】🟡やや割高（2.0/7）— PER59.8倍・PEG2.84・52週31.0% ／ 💰単元11.6万円
> 【戦略】当日終値1155.0円の指値で反転を取りにいく。SL978.0円（直近5日安値）

| 8141 新光商事 | granville_rebound・未マージPR由来 | 🔥絶好調(8) | 🟡やや割高(2.0) | FAIL_UWAHIGE | 1569.0 | 156,600 |  |  |
| 9941 太洋物産 | granville_rebound | ⚡好調(7) | 🟢値頃(5.0) | FAIL_INSEN | 1220.0 | 126,600 |  |  |
| 4220 Riken Technos Corporation | granville_rebound・未マージPR由来 | ⚡好調(7) | ⚪妥当(4.0) | PASS | 2676.0 | 267,600 | reversal 2676.0/SL2581.0 |  |

> 📌【業態】化学
> 【いま】終値2,676円・直近5日-0.15%（材料未確認）
> 【調子】⚡好調（7/13）
> 【水準】⚪妥当（4.0/7）— PER13.3倍・PEG0.58・52週86.0% ／ 💰単元26.8万円
> 【戦略】当日終値2676.0円の指値で反転を取りにいく。SL2581.0円（直近5日安値）

| 2674 Hard Off Corporation Co., Ltd. | granville_rebound | ⚡好調(6) | 🟢値頃(5.0) | FAIL_INSEN | 2672.0 | 272,300 |  |  |
| 6656 インスペック | granville_rebound・未マージPR由来 | ⚡好調(6) | ⚪妥当(4.0) | PASS | 839.0 | 83,900 | reversal 839.0/SL784.0 |  |

> 📌【業態】半導体やIT関連デバイスの外観検査装置メーカー。プリント基板のパターン検査など。
> 【いま】終値839円・直近5日+1.82%（材料未確認）
> 【調子】⚡好調（6/13） — E軸判定不能(進捗データ不足)
> 【水準】⚪妥当（4.0/7）— PER42.2倍・PEG1.49・52週31.0% ／ 💰単元8.4万円
> 【戦略】当日終値839.0円の指値で反転を取りにいく。SL784.0円（直近5日安値）

| 7120 SHINKO Inc. | granville_rebound | ⚡好調(5) | 💎割安(6.0) | PASS | 1007.0 | 100,700 | reversal 1007.0/SL995.0 |  |

> 📌【業態】卸売業
> 【いま】終値1,007円・直近5日+0.40%（材料未確認）
> 【調子】⚡好調（5/13） — E軸判定不能(進捗データ不足)
> 【水準】💎割安（6.0/7）— PER7.0倍・PEG0.62・52週66.0% ／ 💰単元10.1万円
> 【戦略】当日終値1007.0円の指値で反転を取りにいく。SL995.0円（直近5日安値）

| 5076 インフロニアＨＤ | granville_rebound | ⚡好調(5) | ⚪妥当(4.0) | PASS | 2841.0 | 284,100 | reversal 2841.0/SL2706.5 |  |

> 📌【業態】建設業
> 【いま】終値2,841円・直近5日+3.50%（材料未確認）
> 【調子】⚡好調（5/13） — E軸判定不能(進捗データ不足)
> 【水準】⚪妥当（4.0/7）— PER8.6倍・PEG0.61・52週92.0% ／ 💰単元28.4万円
> 【戦略】当日終値2841.0円の指値で反転を取りにいく。SL2706.5円（直近5日安値）

| 6380 オリエンタルチエン工業 | granville_rebound | ⚡好調(5) | ⚪妥当(4.0) | FAIL_INSEN | 3865.0 | 406,000 |  |  |
| 7505 扶桑電通 | granville_rebound | ⚡好調(5) | ⚪妥当(4.0) | FAIL_INSEN | 2144.0 | 212,600 |  |  |
| 6327 北川精機 | granville_rebound | ⚡好調(5) | ⚪妥当(3.0) | FAIL_INSEN | 3185.0 | 331,000 |  |  |
| 9319 中央倉庫 | granville_rebound | ⚡好調(5) | 🟡やや割高(2.0) | PASS | 1847.0 | 184,700 | reversal 1847.0/SL1796.0 |  |

> 📌【業態】京都地盤の内陸総合物流大手。安田倉庫と連携、国際貨物の拡大に注力。
> 【いま】終値1,847円・直近5日+1.60%（材料未確認）
> 【調子】⚡好調（5/13） — 経常成長率+6.5%
> 【水準】🟡やや割高（2.0/7）— PER15.6倍・PEG2.42・52週57.0% ／ 💰単元18.5万円
> 【戦略】当日終値1847.0円の指値で反転を取りにいく。SL1796.0円（直近5日安値）

| 8750 Daiichi Life Group. Inc. | granville_rebound | ⚠減速(4) | ⚪妥当(3.0) | FAIL_INSEN | 1816.5 | 180,200 |  |  |
| 3393 スターティア　 | granville_rebound | ✅順調(4) | 🟡やや割高(2.0) | PASS | 3020.0 | 302,000 | reversal 3020.0/SL2993.0 |  |

> 📌【業態】卸売業
> 【いま】終値3,020円・直近5日+0.00%（材料未確認）
> 【調子】✅順調（4/13） — E軸=四半期経常ペース比較で近似(累計進捗率は未算出)
> 【水準】🟡やや割高（2.0/7）— PER12.1倍・PEG1.56・52週79.0% ／ 💰単元30.2万円
> 【戦略】当日終値3020.0円の指値で反転を取りにいく。SL2993.0円（直近5日安値）

| 4063 信越化学工業 | granville_rebound | ✅順調(4) | 🟡やや割高(2.0) | FAIL_INSEN | 5993.0 | 600,500 |  |  |
| 7966 Lintec Corporation | granville_rebound | ✅順調(4) | 🟡やや割高(2.0) | FAIL_INSEN | 5570.0 | 547,000 |  |  |
| 7740 Tamron Co., Ltd. | granville_rebound | ✅順調(4) | 🔴過熱(1.0) | FAIL_INSEN | 1358.0 | 138,300 |  |  |
| 1518 Mitsui Matsushima Holdings Co., Ltd. | granville_rebound | ✅順調(3) | 🟡やや割高(2.0) | FAIL_UWAHIGE | 2318.0 | 227,900 |  |  |
| 255A Gltechno Holdings, Inc. | granville_rebound | ✅順調(3) | 🟡やや割高(2.0) | FAIL_UWAHIGE | 5260.0 | 520,000 |  |  |
| 7460 Yagi & Co., Ltd. | granville_rebound | ✅順調(3) | 🟡やや割高(2.0) | FAIL_INSEN | 1708.0 | 170,800 |  |  |
| 8081 カナデン | granville_rebound | ✅順調(3) | 🟡やや割高(2.0) | FAIL_INSEN | 2585.0 | 256,000 |  |  |
| 1860 戸田建設 | granville_rebound | ✅順調(3) | 🔴過熱(1.0) | FAIL_INSEN | 1522.0 | 151,500 |  |  |
| 4972 綜研化学 | granville_rebound | ✅順調(3) | 🔴過熱(1.0) | PASS | 3485.0 | 348,500 | reversal 3485.0/SL3300.0 |  |

> 📌【業態】化学
> 【いま】終値3,485円・直近5日+4.34%（材料未確認）
> 【調子】✅順調（3/13） — E軸:進捗28.5%>=前年同期20.9%
> 【水準】🔴過熱（1.0/7）— PER13.5倍・PEG—・52週83.0% ／ 💰単元34.9万円
> 【戦略】当日終値3485.0円の指値で反転を取りにいく。SL3300.0円（直近5日安値）

| 6237 Iwaki Co. Ltd. | granville_rebound | ✅順調(3) | 🔴過熱(1.0) | FAIL_INSEN | 4130.0 | 420,000 |  |  |
| 7745 A&D HOLON Holdings Company. Limited | granville_rebound | 🔻悪化(3) | 🔴過熱(1.0) | PASS | 2904.0 | 290,400 | reversal 2904.0/SL2703.0 |  |

> 📌【業態】計測・計量機器メーカー。電子てんびんでシェア首位。傘下に半導体装置のホロン。
> 【いま】終値2,904円・直近5日+4.39%（材料未確認）
> 【調子】🔻悪化（3/13） — E軸判定不能(進捗データ不足)
> 【水準】🔴過熱（1.0/7）— PER17.7倍・PEG—・52週71.0% ／ 💰単元29.0万円
> 【戦略】当日終値2904.0円の指値で反転を取りにいく。SL2703.0円（直近5日安値）

| 9854 愛眼 | granville_rebound | ✅順調(3) | 🔴過熱(1.0) | FAIL_UWAHIGE | 282.0 | 28,000 |  |  |
| 4320 ＣＥホールディングス | granville_rebound | ✅順調(3) | 🔴過熱(0.0) | FAIL_INSEN | 1652.0 | 165,600 |  |  |
| 5998 アドバネクス | granville_rebound | ➖横ばい(2) | ⚪妥当(3.0) | PASS | 2764.0 | 276,400 | reversal 2764.0/SL2305.0 |  |

> 📌【業態】精密ばね大手。事務機、自動車向け主力。生活・医療機向けも。海外生産大。
> 【いま】終値2,764円・直近5日+16.92%（材料未確認）
> 【調子】➖横ばい（2/13） — 質注意
> 【水準】⚪妥当（3.0/7）— PER5.7倍・PEG—・52週68.0% ／ 💰単元27.6万円
> 【戦略】当日終値2764.0円の指値で反転を取りにいく。SL2305.0円（直近5日安値）／⚠1単元でリスク枠超過（45900円）

| 6703 沖電気工業 | granville_rebound | ➖横ばい(2) | ⚪妥当(3.0) | FAIL_UWAHIGE | 2817.0 | 275,100 |  |  |
| 8844 Cosmos Initia Co., Ltd. | granville_rebound | ➖横ばい(2) | ⚪妥当(3.0) | FAIL_INSEN | 1279.0 | 128,700 |  |  |
| 2483 翻訳センター | granville_rebound | ➖横ばい(2) | 🟡やや割高(2.0) | FAIL_INSEN | 2239.0 | 223,800 |  |  |
| 7459 MEDIPAL HOLDINGS Corporation | granville_rebound | ➖横ばい(2) | 🟡やや割高(2.0) | FAIL_INSEN | 2893.0 | 290,900 |  |  |
| 5189 櫻護謨 | granville_rebound | 🔻悪化(2) | 🔴過熱(1.0) | FAIL_INSEN | 3520.0 | 364,000 |  |  |
| 3063 j-Group Holdings Corp. | granville_rebound・未マージPR由来 | ➖横ばい(2) | 🔴過熱(0.0) | FAIL_INSEN | 1150.0 | 118,100 |  |  |
| 5989 エイチワン | granville_rebound・未マージPR由来 | ⚠減速(1) | ⚪妥当(3.0) | FAIL_INSEN | 1518.0 | 154,900 |  |  |
| 2217 Morozoff Limited | granville_rebound | 🔻悪化(1) | 🟡やや割高(2.0) | FAIL_UWAHIGE | 1517.0 | 151,500 |  |  |
| 4980 Dexerials Corp. | granville_rebound | ⚠減速(1) | 🟡やや割高(2.0) | FAIL_INSEN | 3078.0 | 302,100 |  |  |
| 9502 中部電力 | granville_rebound | 🔻悪化(1) | 🟡やや割高(2.0) | FAIL_INSEN | 2896.5 | 291,050 |  |  |
| 3086 J. FRONT RETAILING Co., Ltd. | granville_rebound | ⚠減速(1) | 🔴過熱(1.0) | FAIL_UWAHIGE | 3139.0 | 309,700 |  |  |
| 3776 ブロードバンドタワー | granville_rebound | ⚠減速(1) | 🔴過熱(1.0) | FAIL_INSEN | 251.0 | 25,400 |  |  |
| 9001 東武鉄道 | granville_rebound | ⚠減速(1) | 🔴過熱(1.0) | FAIL_UWAHIGE | 3013.0 | 304,300 |  |  |
| 9735 Secom Co., Ltd. | granville_rebound | ⚠減速(1) | 🔴過熱(1.0) | FAIL_UWAHIGE | 6413.0 | 644,000 |  |  |
| 8566 Ricoh Leasing Company,Ltd. | granville_rebound | ⚠減速(1) | 🔴過熱(0.0) | FAIL_INSEN | 6820.0 | 677,000 |  |  |
| 9301 三菱倉庫 | granville_rebound | ⚠減速(1) | 🔴過熱(0.0) | FAIL_INSEN | 1521.0 | 152,550 |  |  |
| 1976 Meisei Industrial Co., Ltd. | granville_rebound | ⚠減速(0) | ⚪妥当(3.0) | FAIL_INSEN | 1740.0 | 174,900 |  |  |
| 254A ＡＩフュージョンキャピタルグループ（ＡＩＦＣＧ） | granville_rebound・未マージPR由来 | 判定保留(—) | ⚪妥当(5.6) | FAIL_UWAHIGE | 1194.0 | 118,300 |  |  |
| 7182 ゆうちょ銀行 | granville_rebound | 取得不可(—) | ⚪妥当(3.0) | FAIL_UWAHIGE | 3301.0 | 324,300 |  |  |
| 8630 Sompo Holdings,Inc. | granville_rebound | 🔻悪化(—) | 🔴過熱(2.0) | FAIL_UWAHIGE | 6850.0 | 680,300 |  |  |
| 6266 タツモ | granville_rebound・未マージPR由来 | 🔻悪化(—) | 🔴過熱(1.0) | FAIL_INSEN | 3555.0 | 356,500 |  |  |
| 2693 YKT Corporation | granville_rebound・未マージPR由来 | —(—) | —(—) | FAIL_UWAHIGE | 293.0 | — |  |  |
| 2760 Tokyo Electron Device Limited | granville_rebound・未マージPR由来 | —(—) | —(—) | FAIL_INSEN | 4045.0 | — |  |  |
| 3544 SATUDORA HOLDINGS CO., LTD. | granville_rebound | 業績データ取得不可(—) | ⏸判定不能(—) | FAIL_INSEN | 1249.0 | 125,000 |  |  |
| 3863 日本製紙 | granville_rebound | 業績データ取得不可(—) | ⏸判定不能(—) | PASS | 1405.0 | 140,500 | reversal 1405.0/SL1340.0 |  |

> 📌【業態】製紙業界２強の一角。洋紙で首位。エネルギー、生活用品、建材、緑化なども。
> 【いま】終値1,405円・直近5日+3.01%（材料未確認）
> 【調子】—（—/13） — 軸データ不足のため合計不能
> 【水準】⏸判定不能（—/7）— PER—倍・PEG—・52週64.0% ／ 💰単元14.1万円
> 【戦略】当日終値1405.0円の指値で反転を取りにいく。SL1340.0円（直近5日安値）

| 6407 CKD Corporation | granville_rebound・未マージPR由来 | —(—) | —(—) | FAIL_INSEN | 5560.0 | — |  |  |
| 6481 THK Co., Ltd. | granville_rebound・未マージPR由来 | —(—) | —(—) | FAIL_INSEN | 6804.0 | — |  |  |
| 6594 Nidec Corporation | granville_rebound・未マージPR由来 | —(—) | —(—) | FAIL_INSEN | 2603.0 | — |  |  |
| 6723 Renesas Electronics Corporation | granville_rebound | 取得不可(—) | ⏸判定不能(—) | FAIL_INSEN | 3380.0 | 340,200 |  |  |
| 6914 OPTEX GROUP Company, Limited | granville_rebound・未マージPR由来 | —(—) | —(—) | FAIL_UWAHIGE | 3260.0 | — |  |  |
| 6976 Taiyo Yuden Co., Ltd. | granville_rebound・未マージPR由来 | —(—) | —(—) | FAIL_INSEN | 8900.0 | — |  |  |
| 6996 Nichicon Corporation | granville_rebound・未マージPR由来 | —(—) | —(—) | FAIL_INSEN | 2644.0 | — |  |  |
| 6997 Nippon Chemi-Con Corporation | granville_rebound・未マージPR由来 | —(—) | —(—) | FAIL_INSEN | 2701.0 | — |  |  |
| 8439 Tokyo Century Corporation | granville_rebound | —(—) | ⏸判定不能(—) | FAIL_UWAHIGE | 2632.0 | 258,450 |  |  |
| 9519 レノバ | granville_rebound・未マージPR由来 | 取得不可(—) | ⏸判定不能(—) | FAIL_INSEN | 924.0 | 97,600 |  |  |

## 変化点銘柄
| コード 銘柄名 | 手法 | 業績 | 値頃感 | 判定 | 終値 | 単元金額 | 提案 | チップ |
|---|---|---|---|---|---|---|---|---|
| 265A HMCOMM INC | changepoint_watch・変化点🔔 | 🚀確変(12) | 🟢値頃(5.0) | FAIL_INSEN | 701.0 | 69,800 |  |  |
| 5027 AnyMind Group | changepoint | 🚀確変(11) | ⚪妥当(3.0) | FAIL_INSEN | 829.0 | 78,400 |  |  |
| 479A PRONI INC | changepoint🔔・変化点🔔・変化点🔔🔔 | 🔥絶好調(10) | ⚪妥当(4.0) | PASS | 1955.0 | 195,500 | ⛔要確認: R比が負 |  |

> 📌【業態】法人向け受発注プラットフォーム「PRONI アイミツ」の運営などを手掛ける。
> 【いま】終値1,955円・直近5日+2.09%（材料未確認）
> 【調子】🔥絶好調（10/13） — D軸判定不能(四半期データ不足)
> 【水準】⚪妥当（4.0/7）— PER9.6倍・PEG0.08・52週84.0% ／ 💰単元19.6万円
> 【戦略】発注対象外（⛔要確認: R比が負）

| 6080 M&A Capital Partners Co.,Ltd. | 変化点🔔・changepoint | 🔥絶好調(10) | ⚪妥当(3.0) | FAIL_INSEN | 4255.0 | 423,500 |  |  |
| 7695 交換できるくん | changepoint・変化点🔔🔔 | 🔥絶好調(10) | ⚪妥当(3.0) | FAIL_INSEN | 914.0 | 90,200 |  |  |
| 584A LiNKX | changepoint🔔・変化点🔔・変化点🔔🔔 | 🔥絶好調(9) | 🟢値頃(5.0) | FAIL_UWAHIGE | 2892.0 | 266,600 |  |  |
| 3696 セレス | changepoint・変化点🔔🔔 | 🔥絶好調(8) | 💎割安(6.0) | FAIL_INSEN | 2252.0 | 229,900 |  |  |
| 9888 UEX, Ltd. | 変化点🔔🔔 | 🔥絶好調(8) | 🟢値頃(5.0) | FAIL_UWAHIGE | 1247.0 | 122,300 |  |  |
| 4443 Sansan, Inc. | changepoint・変化点🔔・変化点🔔🔔 | 🔥絶好調(8) | ⚪妥当(3.0) | FAIL_UWAHIGE | 2179.0 | 215,300 |  |  |
| 4431 Smaregi, Inc. | 変化点🔔🔔・未マージPR由来 | ⚡好調(7) | 🟡やや割高(2.0) | FAIL_INSEN | 3535.0 | 341,500 |  |  |
| 9343 ibis inc. | changepoint・変化点🔔🔔・未マージPR由来・変化点🔔 | ⚡好調(6) | ⚪妥当(3.0) | FAIL_UWAHIGE | 822.0 | 76,600 |  |  |
| 3994 マネーフォワード | changepoint・変化点🔔 | ⚡好調(6) | 🔴過熱(1.4) | FAIL_UWAHIGE | 6428.0 | 617,000 |  |  |
| 286A ユカリア | 変化点🔔🔔 | ⚡好調(5) | ⚪妥当(4.0) | FAIL_UWAHIGE | 817.0 | 81,800 |  |  |
| 4441 トビラシステムズ | changepoint・changepoint🔔・変化点🔔 | ⚡好調(5) | 🔴過熱(1.0) | FAIL_UWAHIGE | 1460.0 | 141,800 |  |  |
| 4483 JMDC Inc. | 変化点🔔🔔 | ⚡好調(5) | 🔴過熱(1.0) | FAIL_INSEN | 3430.0 | 342,500 |  |  |
| 4498 サイバートラスト | changepoint・changepoint🔔🔔・変化点🔔🔔 | ✅順調(4) | ⚪妥当(3.0) | PASS | 1301.0 | 130,100 | changepoint 1287.0/SL1282.0 | 🔒 |

> 📌【業態】情報・通信業
> 【いま】終値1,301円・直近5日-1.59%（材料未確認）
> 【調子】✅順調（4/13） — E軸判定不能(進捗データ不足)
> 【水準】⚪妥当（3.0/7）— PER17.2倍・PEG1.36・52週47.0% ／ 💰単元13.0万円
> 【戦略】発火日終値1287.0円の指値。追撃禁止・SL1282.0円。🔒実弾封印中（PL3紙ログ収集中）

| 218A リベラウェア | changepoint・changepoint_watch・変化点🔔・未マージPR由来 | 🔻悪化(4) | 🔴過熱(2.8) | FAIL_UWAHIGE | 1133.0 | 108,100 |  |  |
| 593A ティアフォー | 変化点🔔・changepoint・変化点🔔🔔・未マージPR由来 | ✅順調(4) | 🔴過熱(0.0) | PASS | 1599.0 | 159,900 | changepoint 1599.0/SL985.0 | 🔒 |

> 📌【業態】自動運転ソフトウェア「Autoware」を活用した自動運転車両の開発を手掛ける。
> 【いま】終値1,599円・直近5日+54.79%（材料未確認）
> 【調子】✅順調（4/13） — 赤字・上限適用
> 【水準】🔴過熱（0.0/7）— PER—倍・PEG—・52週96.0% ／ 💰単元16.0万円
> 【戦略】発火日終値1599.0円の指値。追撃禁止・SL985.0円。🔒実弾封印中（PL3紙ログ収集中）／⚠1単元でリスク枠超過（61400円）

| 598A CHATPLUS CO LTD | changepoint | ✅順調(3) | ⚪妥当(3.0) | FAIL_UWAHIGE | 1469.0 | 139,300 |  |  |
| 4488 AI inside Inc. | changepoint・changepoint_watch・変化点🔔・変化点🔔🔔 | ➖横ばい(2) | 🟡やや割高(2.0) | FAIL_UWAHIGE | 2164.0 | 215,300 |  |  |
| 3923 ラクス | 変化点🔔・未マージPR由来 | 判定保留(変則決算)(—) | ⚪妥当(3.0) | FAIL_UWAHIGE | 1137.0 | 110,100 |  |  |
| 4478 freee K.K. | changepoint・変化点🔔🔔・未マージPR由来 | 業績データ取得不可(—) | 🔴過熱(2.8) | FAIL_UWAHIGE | 4230.0 | 387,500 |  |  |

## ⚡材料後出し
その日の足は開示前の情報。判定は参考値。

- 3064 MonotaRO Co., Ltd.: FAIL_UWAHIGE（提案対象外）／📌その他重要開示自社株買いの実施を発表
- 7911 TOPPAN Holdings Inc.: FAIL_INSEN（提案対象外）／📌その他重要開示株式分割に伴い配当予想を修正
- 2590 DyDo Group Holdings, Inc.: FAIL_INSEN（提案対象外）／📢上方修正今期経常を12％上方修正・最高益予想を上..

## 📢開示
使用URL: https://kabutan.jp/warning/?mode=4_2（取引時間中）・?mode=4_3（取引終了後）・?mode=4_4（15時30分以降）
フォールバック発生: なし（一覧取得に成功）

- [プール] 2590 ＤｙＤｏ: 📢上方修正 「今期経常を12％上方修正・最高益予想を上..」（afterclose）
- [プール] 7911 ＴＯＰＰＡＮ: 📌その他重要開示 「株式分割に伴い配当予想を修正」（afterclose）
- [プール] 3064 モノタロウ: 📌その他重要開示 「自社株買いの実施を発表」（afterclose_1530）
- [対象外] 6768 タムラ: 📢上方修正 「今期経常を18％上方修正」（intraday）
- [対象外] 9818 大丸エナ: 📢上方修正 「今期配当を1円増額修正」（intraday）
- [対象外] 9832 オートバクス: 📢上方修正 「今期最終を24％上方修正・30期ぶり最高益..」（afterclose）
- [対象外] 6088 シグマクシス: 📌その他重要開示 「自社株の買付と消却を発表」（afterclose_1530）
- [対象外] 7426 山大: 📌その他重要開示 「自社株の消却を発表」（afterclose_1530）
- [対象外] 7426 山大: 📌その他重要開示 「株式併合を発表」（afterclose_1530）

①-9へ引き渡し（recalc_queue新規追加）: 3件
  - 2590 ＤｙＤｏ: 📢上方修正「今期経常を12％上方修正・最高益予想を上..」
  - 7911 ＴＯＰＰＡＮ: 📌その他重要開示「株式分割に伴い配当予想を修正」
  - 3064 モノタロウ: 📌その他重要開示「自社株買いの実施を発表」
## 総当りゲート
branch_typeでグループ化し、グループ内は判定別（本表のみSTEP5.2の並び順を適用しない）

### ■5手法
| コード | 銘柄名 | 判定 | 終値 | 上髭比率 |
|---|---|---|---|---|
| 135A | VRAIN Solution,Inc. | PASS | 4220.0 | 0.0909 |
| 1802 | Obayashi Corporation | PASS | 2993.0 | 0.0980 |
| 3191 | Joyful Honda Co. Ltd. | PASS | 2292.0 | 0.0000 |
| 341A | TOYOKOH Inc. | PASS | 2007.0 | 0.1000 |
| 4058 | Toyokumo, Inc. | PASS | 2432.0 | 0.0000 |
| 4718 | Waseda Academy Co., Ltd. | PASS | 2541.0 | 0.0000 |
| 4894 | Cuorips Inc. | PASS | 5840.0 | 0.1333 |
| 5301 | 東海カーボン | PASS | 1670.5 | 0.2500 |
| 558A | SQUEEZE Inc. | PASS | 5960.0 | 0.0455 |
| 5724 | Asaka Riken Co., Ltd. | PASS | 3505.0 | 0.0633 |
| 6013 | Takuma Co., Ltd. | PASS | 3100.0 | 0.0000 |
| 8139 | Nagahori Corporation | PASS | 2272.0 | 0.0000 |
| 8614 | Toyo Securities Co., Ltd. | PASS | 739.0 | 0.0625 |
| 9072 | ニッコンホールディングス | PASS | 5442.0 | 0.2030 |
| 9302 | 三井倉庫ホールディングス | PASS | 3333.0 | 0.1042 |
| 9616 | Kyoritsu Maintenance Co., Ltd. | PASS | 3432.0 | 0.1758 |
| 1435 | robot home Inc. | FAIL_UWAHIGE | 181.0 | 0.4000 |
| 147A | ソラコム | FAIL_UWAHIGE | 1038.0 | 0.5000 |
| 1812 | Kajima Corporation | FAIL_UWAHIGE | 4826.0 | 0.5000 |
| 1980 | ダイダン | FAIL_UWAHIGE | 2794.0 | 0.4237 |
| 2334 | Eole, Inc. | FAIL_UWAHIGE | 565.0 | 0.2903 |
| 2579 | Coca-Cola Bottlers Japan Holdings Inc. | FAIL_UWAHIGE | 3920.0 | 0.4805 |
| 2594 | Key Coffee Inc. | FAIL_UWAHIGE | 2035.0 | 0.6000 |
| 262A | INTERMESTIC INC. | FAIL_UWAHIGE | 1846.0 | 0.3400 |
| 2733 | Arata Corporation | FAIL_UWAHIGE | 2731.0 | 0.4333 |
| 277A | Globe-Ing, Inc. | FAIL_UWAHIGE | 1922.0 | 0.5125 |
| 2980 | SRE Holdings Corp. | FAIL_UWAHIGE | 2461.0 | 0.4405 |
| 3036 | アルコニックス（アルコニクス） | FAIL_UWAHIGE | 3480.0 | 0.4545 |
| 3064 | MonotaRO Co., Ltd. | FAIL_UWAHIGE | 1872.5 | 0.2754 |
| 3109 | Shikibo Ltd. | FAIL_UWAHIGE | 1094.0 | 0.2500 |
| 3289 | Tokyu Fudosan Holdings Corp. | FAIL_UWAHIGE | 1338.0 | 0.7812 |
| 3374 | 内外テック | FAIL_UWAHIGE | 4320.0 | 0.4615 |
| 3851 | Nippon Ichi Software, Inc. | FAIL_UWAHIGE | 1297.0 | 0.3125 |
| 421A | Movin' Strategic Career CO.,LTD. | FAIL_UWAHIGE | 3900.0 | 0.3529 |
| 4249 | 森六 | FAIL_UWAHIGE | 2936.0 | 0.2258 |
| 4475 | HENNGE K.K. | FAIL_UWAHIGE | 1597.0 | 0.1845 |
| 4493 | Cyber Security Cloud, Inc. | FAIL_UWAHIGE | 1850.0 | 0.3919 |
| 4516 | 日本新薬 | FAIL_UWAHIGE | 3598.0 | 0.2791 |
| 5136 | tripla Co.,Ltd. | FAIL_UWAHIGE | 1922.0 | 0.5312 |
| 5137 | Smart Drive Co. Ltd. | FAIL_UWAHIGE | 302.0 | 0.1818 |
| 5243 | note inc. | FAIL_UWAHIGE | 2792.0 | 0.2240 |
| 5246 | ELEMENTS,Inc. | FAIL_UWAHIGE | 905.0 | 0.1739 |
| 5574 | ABEJA,Inc. | FAIL_UWAHIGE | 2973.0 | 0.1720 |
| 5586 | Laboro.AI, Inc. | FAIL_UWAHIGE | 885.0 | 0.4545 |
| 5892 | yutori,Inc. | FAIL_UWAHIGE | 2549.0 | 0.2684 |
| 5938 | LIXIL Corporation | FAIL_UWAHIGE | 1772.0 | 0.3929 |
| 6135 | 牧野フライス製作所 | FAIL_UWAHIGE | 15400.0 | 0.6667 |
| 6544 | Japan Elevator Service Holdings Co., Ltd. | FAIL_UWAHIGE | 1559.0 | 0.5091 |
| 6632 | ＪＶＣケンウッド | FAIL_UWAHIGE | 1032.5 | 0.2951 |
| 7157 | Lifenet Insurance Company | FAIL_UWAHIGE | 1494.0 | 0.6500 |
| 7318 | SERENDIP HOLDINGS Co. Ltd. | FAIL_UWAHIGE | 1456.0 | 0.2800 |
| 7409 | AeroEdge Co.,Ltd | FAIL_UWAHIGE | 1657.0 | 0.2987 |
| 7433 | 伯東 | FAIL_UWAHIGE | 5290.0 | 0.5000 |
| 7581 | Saizeriya Co., Ltd. | FAIL_UWAHIGE | 7220.0 | 0.7500 |
| 8084 | ＲＹＯＤＥＮ | FAIL_UWAHIGE | 4740.0 | 0.7895 |
| 8111 | Goldwin Inc. | FAIL_UWAHIGE | 2170.0 | 0.6000 |
| 8388 | 阿波銀行 | FAIL_UWAHIGE | 9950.0 | 0.2857 |
| 8927 | Meiho Enterprise Co., Ltd. | FAIL_UWAHIGE | 476.0 | 0.2500 |
| 9308 | 乾汽船 | FAIL_UWAHIGE | 2102.0 | 0.4655 |
| 9341 | GENOVA Inc. | FAIL_UWAHIGE | 633.0 | 0.8000 |
| 9533 | 東邦瓦斯 | FAIL_UWAHIGE | 1214.0 | 0.6087 |
| 9560 | PROGRIT, Inc. | FAIL_UWAHIGE | 900.0 | 0.5000 |
| 146A | Columbia Works Inc. | FAIL_INSEN | 3615.0 | 0.2143 |
| 1861 | Kumagai Gumi Co., Ltd. | FAIL_INSEN | 1303.0 | 0.0000 |
| 1878 | Daito Trust Construction Co., Ltd. | FAIL_INSEN | 3328.0 | 0.3509 |
| 1960 | サンテック | FAIL_INSEN | 1651.0 | 0.2692 |
| 1975 | 朝日工業社 | FAIL_INSEN | 3920.0 | 0.5385 |
| 1979 | Taikisha Ltd. | FAIL_INSEN | 3895.0 | 0.2000 |
| 212A | FIT EASY Inc. | FAIL_INSEN | 2970.0 | 0.0000 |
| 276A | ククレブ・アドバイザーズ | FAIL_INSEN | 3730.0 | 0.1071 |
| 3091 | ブロンコビリー | FAIL_INSEN | 2735.0 | 0.5750 |
| 3131 | シンデンハイ | FAIL_INSEN | 6020.0 | 0.3103 |
| 325A | TENTIAL, Inc. | FAIL_INSEN | 1688.0 | 0.0000 |
| 3288 | Open House Group Co. Ltd | FAIL_INSEN | 7957.0 | 0.2937 |
| 3441 | Sanno Co., Ltd. | FAIL_INSEN | 2730.0 | 0.6960 |
| 3556 | RenetJapanGroup, Inc. | FAIL_INSEN | 860.0 | 0.0000 |
| 3723 | Nihon Falcom Corporation | FAIL_INSEN | 2851.0 | 0.0000 |
| 3798 | ULS Group Incorporated | FAIL_INSEN | 529.0 | 0.3333 |
| 3915 | TerraSky Co., Ltd. | FAIL_INSEN | 2333.0 | 0.1940 |
| 3932 | Akatsuki, Inc. | FAIL_INSEN | 3850.0 | 0.3846 |
| 4165 | PLAID Inc. | FAIL_INSEN | 685.0 | 0.1905 |
| 4377 | ONE CAREER Inc. | FAIL_INSEN | 2551.0 | 0.0088 |
| 4477 | BASE, Inc. | FAIL_INSEN | 311.0 | 0.5556 |
| 4536 | 参天製薬 | FAIL_INSEN | 1862.0 | 0.4915 |
| 456A | ＨＵＭＡＮ　ＭＡＤＥ | FAIL_INSEN | 1581.0 | 0.0270 |
| 4599 | StemRIM Inc. | FAIL_INSEN | 351.0 | 0.3333 |
| 4973 | Japan Pure Chemical Co., Ltd. | FAIL_INSEN | 4790.0 | 0.2903 |
| 5038 | eWeLL Co.,Ltd | FAIL_INSEN | 2120.0 | 0.0000 |
| 505A | Geekly,Inc. | FAIL_INSEN | 1415.0 | 0.4688 |
| 5105 | Toyo Tire Corporation | FAIL_INSEN | 3811.0 | 0.0588 |
| 5254 | Arent, Inc. | FAIL_INSEN | 4075.0 | 0.1765 |
| 5334 | Niterra Co.,Ltd. | FAIL_INSEN | 8474.0 | 0.1577 |
| 543A | ＡＲＣＨＩＯＮ | FAIL_INSEN | 274.0 | 0.5000 |
| 5444 | Yamato Kogyo Co., Ltd. | FAIL_INSEN | 12305.0 | 0.3939 |
| 5537 | AlbaLink Co.,Ltd. | FAIL_INSEN | 3285.0 | 0.6098 |
| 5590 | ネットスターズ | FAIL_INSEN | 694.0 | 0.1429 |
| 5757 | CK San-Etsu Co., Ltd. | FAIL_INSEN | 5420.0 | 0.7778 |
| 6071 | IBJ, Inc. | FAIL_INSEN | 931.0 | 0.6000 |
| 6134 | ＦＵＪＩ | FAIL_INSEN | 7231.0 | 0.1483 |
| 6298 | Y.A.C.HOLDINGS CO.,LTD. | FAIL_INSEN | 1316.0 | 0.2708 |
| 6324 | ハーモニック・ドライブ・システムズ（ハーモニック） | FAIL_INSEN | 5780.0 | 0.1500 |
| 6370 | Kurita Water Industries Ltd. | FAIL_INSEN | 8230.0 | 0.3539 |
| 6490 | ＰＩＬＬＡＲ | FAIL_INSEN | 10140.0 | 0.3784 |
| 6492 | Okano Valve Mfg. Co., Ltd. | FAIL_INSEN | 14270.0 | 0.3448 |
| 6562 | Geniee, Inc. | FAIL_INSEN | 889.0 | 0.4000 |
| 6586 | Makita Corporation | FAIL_INSEN | 5300.0 | 0.6377 |
| 6630 | YA-MAN Ltd. | FAIL_INSEN | 795.0 | 0.3684 |
| 6785 | Suzuki Co., Ltd. | FAIL_INSEN | 2939.0 | 0.3614 |
| 6845 | Azbil Corporation | FAIL_INSEN | 1521.0 | 0.5254 |
| 6856 | Horiba, Ltd. | FAIL_INSEN | 23675.0 | 0.1768 |
| 6857 | アドバンテスト | FAIL_INSEN | 34610.0 | 0.0559 |
| 7202 | Isuzu Motors Limited | FAIL_INSEN | 2213.0 | 0.4105 |
| 7267 | ホンダ | FAIL_INSEN | 1662.5 | 0.2152 |
| 7352 | TWOSTONE&Sons Co.Ltd. | FAIL_INSEN | 340.0 | 0.3333 |
| 7419 | Nojima Co.,Ltd. | FAIL_INSEN | 1277.0 | 0.5769 |
| 7480 | スズデン | FAIL_INSEN | 3475.0 | 0.3333 |
| 7637 | 白銅 | FAIL_INSEN | 3755.0 | 0.0000 |
| 7649 | Sugi Holdings Co., Ltd. | FAIL_INSEN | 2678.0 | 0.3763 |
| 7685 | ＢＵＹＳＥＬＬ　ＴＥＣＨＮＯＬＯＧＩＥＳ | FAIL_INSEN | 3275.0 | 0.3500 |
| 7730 | マニー | FAIL_INSEN | 1614.0 | 0.5769 |
| 7731 | ニコン | FAIL_INSEN | 1957.0 | 0.3030 |
| 7972 | ITOKI Corporation | FAIL_INSEN | 2595.0 | 0.2540 |
| 8366 | 滋賀銀行 | FAIL_INSEN | 2763.0 | 0.4324 |
| 8697 | 日本取引所グループ | FAIL_INSEN | 2284.5 | 0.1739 |
| 9044 | NANKAI Co., Ltd. | FAIL_INSEN | 3057.0 | 0.1591 |
| 9065 | Sankyu Inc. | FAIL_INSEN | 8366.0 | 0.4599 |
| 9211 | f-code Inc. | FAIL_INSEN | 1498.0 | 0.7895 |
| 9270 | Valuence Holdings, Inc. | FAIL_INSEN | 2028.0 | 0.2192 |
| 9467 | Alphapolis Co., Ltd. | FAIL_INSEN | 1200.0 | 0.1250 |
| 9552 | Quants Research Institute Holdings, Inc. | FAIL_INSEN | 1085.0 | 0.4286 |
| 9554 | AViC Co. Ltd. | FAIL_INSEN | 1749.0 | 0.4667 |
| 9861 | Yoshinoya Holdings Co., Ltd. | FAIL_INSEN | 3785.0 | 0.0510 |
| 9962 | ミスミグループ本社 | FAIL_INSEN | 3667.0 | 0.3750 |

### ■グランビル
| コード | 銘柄名 | 判定 | 終値 | 上髭比率 |
|---|---|---|---|---|
| 1808 | Haseko Corporation | PASS | 2896.0 | 0.0583 |
| 2768 | Sojitz Corp. | PASS | 5589.0 | 0.0982 |
| 2874 | 横浜冷凍 | PASS | 2197.0 | 0.1379 |
| 3222 | United Super Markets Holdings, Inc. | PASS | 850.0 | 0.0000 |
| 3393 | スターティア　 | PASS | 3020.0 | 0.1852 |
| 3449 | Technoflex Corporation | PASS | 4020.0 | 0.1786 |
| 3479 | TKP Corporation | PASS | 1898.0 | 0.0000 |
| 3863 | 日本製紙 | PASS | 1405.0 | 0.0000 |
| 4220 | Riken Technos Corporation | PASS | 2676.0 | 0.2500 |
| 4258 | AMIYA Corporation | PASS | 4330.0 | 0.0455 |
| 4392 | FIG | PASS | 1155.0 | 0.1554 |
| 4415 | BROAD ENTERPRISE CO.,LTD. | PASS | 1422.0 | 0.1609 |
| 4765 | ＳＢＩグローバルアセットマネジメント | PASS | 648.0 | 0.0000 |
| 4826 | ＣＩＪ | PASS | 545.0 | 0.1429 |
| 4972 | 綜研化学 | PASS | 3485.0 | 0.0000 |
| 5076 | インフロニアＨＤ | PASS | 2841.0 | 0.0000 |
| 5232 | Sumitomo Osaka Cement Co., Ltd. | PASS | 5769.0 | 0.2314 |
| 5302 | 日本カーボン | PASS | 5020.0 | 0.1538 |
| 5998 | アドバネクス | PASS | 2764.0 | 0.1268 |
| 6023 | ダイハツインフィニアース | PASS | 2998.0 | 0.0488 |
| 6055 | Japan Material Co., Ltd. | PASS | 2215.0 | 0.0833 |
| 6656 | インスペック | PASS | 839.0 | 0.1176 |
| 7047 | PORT INC. | PASS | 2307.0 | 0.2449 |
| 7120 | SHINKO Inc. | PASS | 1007.0 | 0.2222 |
| 7350 | Okinawa Financial Group, Inc. | PASS | 7800.0 | 0.1250 |
| 7616 | コロワイド | PASS | 2101.0 | 0.2188 |
| 7745 | A&D HOLON Holdings Company. Limited | PASS | 2904.0 | 0.2344 |
| 8101 | GSI Creos Corporation | PASS | 2747.0 | 0.1034 |
| 8387 | Shikoku Bank Ltd. | PASS | 3545.0 | 0.1500 |
| 8511 | 日本証券金融 | PASS | 2519.0 | 0.1333 |
| 8628 | 松井証券 | PASS | 1180.0 | 0.0000 |
| 8707 | 岩井コスモホールディングス | PASS | 4730.0 | 0.0870 |
| 9037 | ハマキョウレックス（ハマキョウ） | PASS | 1884.0 | 0.0000 |
| 9279 | GIFT HOLDINGS INC. | PASS | 5120.0 | 0.2000 |
| 9319 | 中央倉庫 | PASS | 1847.0 | 0.1290 |
| 9934 | Inaba Denki Sangyo Co.,Ltd. | PASS | 3025.0 | 0.0968 |
| 1375 | Yukiguni Factory Co., Ltd. | FAIL_UWAHIGE | 1178.0 | 0.2857 |
| 145A | L is B Corp. | FAIL_UWAHIGE | 910.0 | 0.2903 |
| 1518 | Mitsui Matsushima Holdings Co., Ltd. | FAIL_UWAHIGE | 2318.0 | 0.5769 |
| 1716 | Daiichi Cutter Kogyo K.K. | FAIL_UWAHIGE | 1407.0 | 0.6500 |
| 1925 | 大和ハウス工業（大和ハウス） | FAIL_UWAHIGE | 4716.0 | 0.5616 |
| 208A | 構造計画研究所ホールディングス | FAIL_UWAHIGE | 2967.0 | 0.3704 |
| 2175 | SMS Co., Ltd. | FAIL_UWAHIGE | 2412.0 | 0.2571 |
| 2217 | Morozoff Limited | FAIL_UWAHIGE | 1517.0 | 0.5333 |
| 254A | ＡＩフュージョンキャピタルグループ（ＡＩＦＣＧ） | FAIL_UWAHIGE | 1194.0 | 0.5000 |
| 255A | Gltechno Holdings, Inc. | FAIL_UWAHIGE | 5260.0 | 0.3200 |
| 2693 | YKT Corporation | FAIL_UWAHIGE | 293.0 | 0.3333 |
| 269A | Sapeet, Inc. | FAIL_UWAHIGE | 2621.0 | 0.2957 |
| 2982 | ＡＤワークスグループ（ＡＤＷＧ） | FAIL_UWAHIGE | 428.0 | 0.4000 |
| 2986 | LA Holdings Co.,Ltd | FAIL_UWAHIGE | 2843.0 | 0.5094 |
| 3003 | ヒューリック | FAIL_UWAHIGE | 1793.0 | 0.6939 |
| 3086 | J. FRONT RETAILING Co., Ltd. | FAIL_UWAHIGE | 3139.0 | 0.8065 |
| 3498 | Kasumigaseki Capital Co., Ltd. | FAIL_UWAHIGE | 8090.0 | 0.1795 |
| 3623 | Billing System Corporation | FAIL_UWAHIGE | 1294.0 | 0.2059 |
| 3765 | ガンホー・オンライン・エンターテイメント | FAIL_UWAHIGE | 2440.0 | 0.5088 |
| 3968 | セグエグループ | FAIL_UWAHIGE | 642.0 | 0.5161 |
| 3993 | PKSHA Technology, Inc. | FAIL_UWAHIGE | 3270.0 | 0.4000 |
| 4375 | Safie Inc. | FAIL_UWAHIGE | 686.0 | 0.2692 |
| 4417 | Global Security Experts Inc. | FAIL_UWAHIGE | 4640.0 | 0.3488 |
| 4419 | Ｆｉｎａｔｅｘｔホールディングス | FAIL_UWAHIGE | 1450.0 | 0.5246 |
| 4420 | イーソル | FAIL_UWAHIGE | 685.0 | 0.3846 |
| 4507 | Shionogi & Co., Ltd. | FAIL_UWAHIGE | 2909.5 | 0.5000 |
| 4847 | インテリジェント　ウェイブ | FAIL_UWAHIGE | 1354.0 | 0.5938 |
| 5885 | GDEP ADVANCE,Inc. | FAIL_UWAHIGE | 3295.0 | 0.3235 |
| 6167 | FUJI DIE Co., Ltd. | FAIL_UWAHIGE | 1048.0 | 0.3684 |
| 6284 | Nissei ASB Machine Co., Ltd. | FAIL_UWAHIGE | 8900.0 | 0.5294 |
| 6425 | Universal Entertainment Corporation | FAIL_UWAHIGE | 718.0 | 0.9412 |
| 6432 | Takeuchi Mfg.Co., Ltd. | FAIL_UWAHIGE | 7750.0 | 0.3333 |
| 6454 | Max Co., Ltd. | FAIL_UWAHIGE | 1845.0 | 0.6087 |
| 6703 | 沖電気工業 | FAIL_UWAHIGE | 2817.0 | 0.4783 |
| 6770 | Alps Alpine Co., Ltd. | FAIL_UWAHIGE | 2211.5 | 0.5946 |
| 6914 | OPTEX GROUP Company, Limited | FAIL_UWAHIGE | 3260.0 | 0.6000 |
| 7128 | UNISOL Holdings Corporation | FAIL_UWAHIGE | 2826.0 | 0.6400 |
| 7182 | ゆうちょ銀行 | FAIL_UWAHIGE | 3301.0 | 0.2903 |
| 7184 | 富山第一銀行 | FAIL_UWAHIGE | 3400.0 | 0.4545 |
| 7611 | ハイデイ日高 | FAIL_UWAHIGE | 2993.0 | 0.4500 |
| 7679 | Yakuodo Holdings Co., Ltd. | FAIL_UWAHIGE | 1675.0 | 0.4583 |
| 8056 | ＢＩＰＲＯＧＹ | FAIL_UWAHIGE | 4656.0 | 0.6087 |
| 8057 | 内田洋行 | FAIL_UWAHIGE | 2267.0 | 0.4688 |
| 8098 | 稲畑産業 | FAIL_UWAHIGE | 4300.0 | 0.5000 |
| 8141 | 新光商事 | FAIL_UWAHIGE | 1569.0 | 0.5000 |
| 8276 | 平和堂 | FAIL_UWAHIGE | 2704.0 | 0.4524 |
| 8439 | Tokyo Century Corporation | FAIL_UWAHIGE | 2632.0 | 0.4769 |
| 8544 | Keiyo Bank, Ltd. | FAIL_UWAHIGE | 2787.0 | 0.4655 |
| 8562 | Fukushima Bank, Ltd. | FAIL_UWAHIGE | 372.0 | 0.5385 |
| 8630 | Sompo Holdings,Inc. | FAIL_UWAHIGE | 6850.0 | 0.4457 |
| 8876 | リログループ | FAIL_UWAHIGE | 2161.0 | 0.5072 |
| 8919 | カチタス | FAIL_UWAHIGE | 3855.0 | 0.1935 |
| 9001 | 東武鉄道 | FAIL_UWAHIGE | 3013.0 | 0.4500 |
| 9006 | Keikyu Corporation | FAIL_UWAHIGE | 1568.5 | 0.6383 |
| 9101 | 日本郵船 | FAIL_UWAHIGE | 6932.0 | 0.3860 |
| 9503 | Kansai Electric Power Company, Incorporated | FAIL_UWAHIGE | 2605.0 | 0.3514 |
| 9735 | Secom Co., Ltd. | FAIL_UWAHIGE | 6413.0 | 0.6129 |
| 9854 | 愛眼 | FAIL_UWAHIGE | 282.0 | 0.5000 |
| 1407 | West Holdings Corporation | FAIL_INSEN | 2727.0 | 0.0000 |
| 150A | JSH | FAIL_INSEN | 741.0 | 0.2500 |
| 1605 | Inpex Corporation | FAIL_INSEN | 3856.0 | 0.1373 |
| 160A | As Partners CO.,LTD. | FAIL_INSEN | 1987.0 | 0.0000 |
| 166A | タスキホールディングス | FAIL_INSEN | 1203.0 | 0.3636 |
| 1833 | Okumura Corporation | FAIL_INSEN | 5860.0 | 0.3750 |
| 1860 | 戸田建設 | FAIL_INSEN | 1522.0 | 0.0345 |
| 1898 | 世紀東急工業 | FAIL_INSEN | 1501.0 | 0.3077 |
| 1911 | Sumitomo Forestry Co., Ltd. | FAIL_INSEN | 1344.0 | 0.4167 |
| 1976 | Meisei Industrial Co., Ltd. | FAIL_INSEN | 1740.0 | 0.6875 |
| 2001 | NIPPN Corporation | FAIL_INSEN | 2904.0 | 0.4565 |
| 205A | ロゴスホールディングス（ロゴスＨＤ） | FAIL_INSEN | 1676.0 | 0.6667 |
| 2282 | NH Foods Limited | FAIL_INSEN | 6332.0 | 0.6848 |
| 2288 | Marudai Food Co., Ltd. | FAIL_INSEN | 2254.0 | 0.7500 |
| 2292 | S Foods Inc. | FAIL_INSEN | 2946.0 | 0.5085 |
| 2317 | システナ | FAIL_INSEN | 443.0 | 0.5714 |
| 2483 | 翻訳センター | FAIL_INSEN | 2239.0 | 0.0000 |
| 2585 | LIFEDRINK COMPANY INC. | FAIL_INSEN | 1548.0 | 0.5000 |
| 2590 | DyDo Group Holdings, Inc. | FAIL_INSEN | 3010.0 | 0.5333 |
| 2602 | 日清オイリオグループ | FAIL_INSEN | 2049.0 | 0.5455 |
| 2659 | SAN-A CO., LTD. | FAIL_INSEN | 3365.0 | 0.5000 |
| 2674 | Hard Off Corporation Co., Ltd. | FAIL_INSEN | 2672.0 | 0.5319 |
| 2702 | 日本マクドナルド HD | FAIL_INSEN | 8050.0 | 0.7500 |
| 2760 | Tokyo Electron Device Limited | FAIL_INSEN | 4045.0 | 0.6250 |
| 2780 | Komehyo Holdings Co., Ltd. | FAIL_INSEN | 5100.0 | 0.7273 |
| 2810 | ハウス食品グループ本社 | FAIL_INSEN | 3733.0 | 0.7255 |
| 2975 | Star Mica Holdings Co., Ltd. | FAIL_INSEN | 1599.0 | 0.4762 |
| 3048 | BIC Cameras Inc. | FAIL_INSEN | 1795.0 | 0.5309 |
| 3063 | j-Group Holdings Corp. | FAIL_INSEN | 1150.0 | 0.7222 |
| 3076 | Ai Holdings Corporation | FAIL_INSEN | 2967.0 | 0.4118 |
| 3116 | Toyota Boshoku Corp. | FAIL_INSEN | 2239.5 | 0.2414 |
| 3151 | バイタルケーエスケー・ホールディングス（バイタルＫＳ） | FAIL_INSEN | 1665.0 | 0.4231 |
| 3491 | GA technologies Co., Ltd. | FAIL_INSEN | 1565.0 | 0.0000 |
| 3544 | SATUDORA HOLDINGS CO., LTD. | FAIL_INSEN | 1249.0 | 0.5000 |
| 3776 | ブロードバンドタワー | FAIL_INSEN | 251.0 | 0.0000 |
| 3865 | 北越コーポレーション（北越コーポ） | FAIL_INSEN | 919.0 | 0.2857 |
| 3880 | 大王製紙 | FAIL_INSEN | 985.0 | 0.2857 |
| 3989 | シェアリングテクノロジー | FAIL_INSEN | 1563.0 | 0.0714 |
| 4047 | Kanto Denka Kogyo Co., Ltd. | FAIL_INSEN | 2393.0 | 0.2547 |
| 4051 | GMO Financial Gate, Inc. | FAIL_INSEN | 6420.0 | 0.6250 |
| 4063 | 信越化学工業 | FAIL_INSEN | 5993.0 | 0.1589 |
| 4092 | Nippon Chemical Industrial Co., Ltd. | FAIL_INSEN | 5370.0 | 0.2308 |
| 4228 | Sekisui Kasei Co., Ltd. | FAIL_INSEN | 595.0 | 0.2500 |
| 4320 | ＣＥホールディングス | FAIL_INSEN | 1652.0 | 0.2500 |
| 4413 | ボードルア | FAIL_INSEN | 2968.0 | 0.5000 |
| 4424 | Amazia, Inc. | FAIL_INSEN | 342.0 | 0.3500 |
| 4521 | Kaken Pharmaceutical Co., Ltd. | FAIL_INSEN | 3990.0 | 0.5556 |
| 4553 | Towa Pharmaceutical Co., Ltd. | FAIL_INSEN | 3930.0 | 0.3333 |
| 4666 | PARK24 Co., Ltd. | FAIL_INSEN | 1986.0 | 0.2917 |
| 4722 | Future Corporation | FAIL_INSEN | 2450.0 | 0.0000 |
| 4848 | フルキャストホールディングス | FAIL_INSEN | 1867.0 | 0.5357 |
| 4968 | Arakawa Chemical Industries, Ltd. | FAIL_INSEN | 2173.0 | 0.0510 |
| 4980 | Dexerials Corp. | FAIL_INSEN | 3078.0 | 0.3972 |
| 5020 | ENEOS Holdings, Inc. | FAIL_INSEN | 1331.0 | 0.0000 |
| 5036 | Japan Business Systems, Inc. | FAIL_INSEN | 1601.0 | 0.3636 |
| 5186 | Nitta Corporation | FAIL_INSEN | 6860.0 | 0.1818 |
| 5189 | 櫻護謨 | FAIL_INSEN | 3520.0 | 0.0000 |
| 5384 | Fujimi Incorporated | FAIL_INSEN | 3620.0 | 0.4074 |
| 5406 | 神戸製鋼所（神戸鋼） | FAIL_INSEN | 2022.0 | 0.5085 |
| 547A | ムニノバホールディングス（ムニノバＨＤ） | FAIL_INSEN | 452.0 | 0.0000 |
| 5592 | Kusurinomadoguchi, Inc. | FAIL_INSEN | 2722.0 | 0.0649 |
| 5703 | Nippon Light Metal Holdings Company, Ltd. | FAIL_INSEN | 3035.0 | 0.2353 |
| 5851 | Ryobi Limited | FAIL_INSEN | 2765.0 | 0.1463 |
| 5932 | Sankyo Tateyama, Inc. | FAIL_INSEN | 670.0 | 0.7143 |
| 5989 | エイチワン | FAIL_INSEN | 1518.0 | 0.0000 |
| 6103 | Okuma Corporation | FAIL_INSEN | 4865.0 | 0.0571 |
| 6125 | Okamoto Machine Tool Works,Ltd. | FAIL_INSEN | 4835.0 | 0.3415 |
| 6136 | OSG Corp | FAIL_INSEN | 3730.0 | 0.4630 |
| 6222 | Shima Seiki Mfg. Ltd. | FAIL_INSEN | 985.0 | 0.3750 |
| 6237 | Iwaki Co. Ltd. | FAIL_INSEN | 4130.0 | 0.2857 |
| 6266 | タツモ | FAIL_INSEN | 3555.0 | 0.2222 |
| 6305 | Hitachi Construction Machinery Co., Ltd. | FAIL_INSEN | 5819.0 | 0.2958 |
| 6327 | 北川精機 | FAIL_INSEN | 3185.0 | 0.1957 |
| 6333 | TEIKOKU Corp. | FAIL_INSEN | 3430.0 | 0.2857 |
| 6339 | Sintokogio,Ltd. | FAIL_INSEN | 1208.0 | 0.3333 |
| 6380 | オリエンタルチエン工業 | FAIL_INSEN | 3865.0 | 0.0000 |
| 6407 | CKD Corporation | FAIL_INSEN | 5560.0 | 0.0667 |
| 6481 | THK Co., Ltd. | FAIL_INSEN | 6804.0 | 0.1365 |
| 6571 | QB Net Holdings Co., Ltd. | FAIL_INSEN | 1301.0 | 0.4444 |
| 6588 | Toshiba Tec Corp. | FAIL_INSEN | 3140.0 | 0.3750 |
| 6590 | 芝浦メカトロニクス | FAIL_INSEN | 4110.0 | 0.1754 |
| 6594 | Nidec Corporation | FAIL_INSEN | 2603.0 | 0.7000 |
| 6613 | Ｇ−ＱＤレーザ | FAIL_INSEN | 2424.0 | 0.0588 |
| 6638 | ミマキエンジニアリング | FAIL_INSEN | 1984.0 | 0.2766 |
| 6718 | アイホン | FAIL_INSEN | 2888.0 | 0.4828 |
| 6723 | Renesas Electronics Corporation | FAIL_INSEN | 3380.0 | 0.0000 |
| 6794 | Foster Electric Company, Limited | FAIL_INSEN | 2982.0 | 0.4091 |
| 6925 | ウシオ電機 | FAIL_INSEN | 3961.0 | 0.3419 |
| 6966 | Mitsui High-Tec, Inc. | FAIL_INSEN | 938.0 | 0.3571 |
| 6976 | Taiyo Yuden Co., Ltd. | FAIL_INSEN | 8900.0 | 0.1985 |
| 6996 | Nichicon Corporation | FAIL_INSEN | 2644.0 | 0.2857 |
| 6997 | Nippon Chemi-Con Corporation | FAIL_INSEN | 2701.0 | 0.1863 |
| 7085 | カーブスホールディングス | FAIL_INSEN | 960.0 | 0.0000 |
| 7089 | For Startups, Inc. | FAIL_INSEN | 1514.0 | 0.0000 |
| 7198 | SBI ARUHI Corporation | FAIL_INSEN | 843.0 | 0.0000 |
| 7231 | トピー工業 | FAIL_INSEN | 3055.0 | 0.1818 |
| 7278 | Exedy Corporation | FAIL_INSEN | 6160.0 | 0.2857 |
| 7287 | Nippon Seiki Co., Ltd. | FAIL_INSEN | 2708.0 | 0.2418 |
| 7459 | MEDIPAL HOLDINGS Corporation | FAIL_INSEN | 2893.0 | 0.5091 |
| 7460 | Yagi & Co., Ltd. | FAIL_INSEN | 1708.0 | 0.0000 |
| 7505 | 扶桑電通 | FAIL_INSEN | 2144.0 | 0.5789 |
| 7609 | Daitron Co., Ltd. | FAIL_INSEN | 4090.0 | 0.3429 |
| 7716 | Nakanishi Inc. | FAIL_INSEN | 3165.0 | 0.2759 |
| 7740 | Tamron Co., Ltd. | FAIL_INSEN | 1358.0 | 0.6364 |
| 7744 | ノーリツ鋼機 | FAIL_INSEN | 2000.0 | 0.2131 |
| 7806 | Ｇ−ＭＴＧ | FAIL_INSEN | 8940.0 | 0.2308 |
| 7860 | Avex Inc. | FAIL_INSEN | 1282.0 | 0.7917 |
| 7867 | Tomy Company, Ltd. | FAIL_INSEN | 3665.0 | 0.3902 |
| 7888 | 三光合成 | FAIL_INSEN | 910.0 | 0.5714 |
| 7911 | TOPPAN Holdings Inc. | FAIL_INSEN | 5001.0 | 0.0828 |
| 7943 | Nichiha Corporation | FAIL_INSEN | 3120.0 | 0.6667 |
| 7956 | ピジョン | FAIL_INSEN | 2122.5 | 0.3654 |
| 7966 | Lintec Corporation | FAIL_INSEN | 5570.0 | 0.3846 |
| 7970 | 信越ポリマー | FAIL_INSEN | 2244.0 | 0.3864 |
| 7981 | Takara standard Co., Ltd. | FAIL_INSEN | 3115.0 | 0.3750 |
| 8008 | Yondoshi Holdings, Inc. | FAIL_INSEN | 2164.0 | 0.3548 |
| 8081 | カナデン | FAIL_INSEN | 2585.0 | 0.6000 |
| 8086 | ニプロ | FAIL_INSEN | 1532.0 | 0.0833 |
| 8151 | TOYO Corporation | FAIL_INSEN | 1959.0 | 0.7895 |
| 8242 | エイチ・ツー・オー　リテイリング | FAIL_INSEN | 3019.0 | 0.2414 |
| 8361 | 大垣共立銀行 | FAIL_INSEN | 8150.0 | 0.2500 |
| 8367 | 南都銀行 | FAIL_INSEN | 1922.0 | 0.5263 |
| 8425 | Mizuho Leasing Company, Limited | FAIL_INSEN | 1380.0 | 0.4706 |
| 8522 | 名古屋銀行（名古屋銀） | FAIL_INSEN | 7060.0 | 0.4000 |
| 8566 | Ricoh Leasing Company,Ltd. | FAIL_INSEN | 6820.0 | 0.7778 |
| 8570 | イオンフィナンシャルサービス | FAIL_INSEN | 1719.0 | 0.7455 |
| 8750 | Daiichi Life Group. Inc. | FAIL_INSEN | 1816.5 | 0.2653 |
| 8793 | NEC Capital Solutions Limited | FAIL_INSEN | 4270.0 | 0.3750 |
| 8844 | Cosmos Initia Co., Ltd. | FAIL_INSEN | 1279.0 | 0.0000 |
| 8923 | Tosei Corporation | FAIL_INSEN | 1834.0 | 0.5625 |
| 9031 | Nishi-Nippon Railroad Co., Ltd. | FAIL_INSEN | 3104.0 | 0.4773 |
| 9041 | 近鉄グループホールディングス | FAIL_INSEN | 3512.0 | 0.3704 |
| 9147 | ＮＩＰＰＯＮ　ＥＸＰＲＥＳＳ　ホールディングス | FAIL_INSEN | 5735.0 | 0.4189 |
| 9247 | TRE HOLDINGS CORPORATION | FAIL_INSEN | 1956.0 | 0.2703 |
| 9274 | ＫＰＰグループホールディングス | FAIL_INSEN | 1103.0 | 0.5217 |
| 9301 | 三菱倉庫 | FAIL_INSEN | 1521.0 | 0.5750 |
| 9324 | 安田倉庫（安田倉） | FAIL_INSEN | 2537.0 | 0.3810 |
| 9404 | Nippon Television Holdings, Inc. | FAIL_INSEN | 3012.0 | 0.5839 |
| 9502 | 中部電力 | FAIL_INSEN | 2896.5 | 0.0417 |
| 9517 | イーレックス | FAIL_INSEN | 875.0 | 0.4167 |
| 9519 | レノバ | FAIL_INSEN | 924.0 | 0.0270 |
| 9627 | アインホールディングス | FAIL_INSEN | 6133.0 | 0.0763 |
| 9628 | San Holdings,Inc. | FAIL_INSEN | 1377.0 | 0.0526 |
| 9828 | ＧＥＮＫＩ　ＧＬＯＢＡＬ　ＤＩＮＩＮＧ　ＣＯＮＣＥＰＴＳ | FAIL_INSEN | 3510.0 | 0.2500 |
| 9869 | 加藤産業 | FAIL_INSEN | 6620.0 | 0.0000 |
| 9882 | Yellow Hat Ltd. | FAIL_INSEN | 1783.0 | 0.0370 |
| 9902 | Nichiden Corporation | FAIL_INSEN | 3060.0 | 0.3333 |
| 9941 | 太洋物産 | FAIL_INSEN | 1220.0 | 0.0000 |

### ■変化点
| コード | 銘柄名 | 判定 | 終値 | 上髭比率 |
|---|---|---|---|---|
| 4498 | サイバートラスト | PASS | 1301.0 | 0.2083 |
| 479A | PRONI INC | PASS | 1955.0 | 0.0714 |
| 593A | ティアフォー | PASS | 1599.0 | 0.0853 |
| 218A | リベラウェア | FAIL_UWAHIGE | 1133.0 | 0.9600 |
| 286A | ユカリア | FAIL_UWAHIGE | 817.0 | 0.2143 |
| 3923 | ラクス | FAIL_UWAHIGE | 1137.0 | 0.3333 |
| 3994 | マネーフォワード | FAIL_UWAHIGE | 6428.0 | 0.4393 |
| 4441 | トビラシステムズ | FAIL_UWAHIGE | 1460.0 | 0.3235 |
| 4443 | Sansan, Inc. | FAIL_UWAHIGE | 2179.0 | 0.5690 |
| 4478 | freee K.K. | FAIL_UWAHIGE | 4230.0 | 0.2118 |
| 4488 | AI inside Inc. | FAIL_UWAHIGE | 2164.0 | 0.2162 |
| 584A | LiNKX | FAIL_UWAHIGE | 2892.0 | 0.3036 |
| 598A | CHATPLUS CO LTD | FAIL_UWAHIGE | 1469.0 | 0.3500 |
| 9343 | ibis inc. | FAIL_UWAHIGE | 822.0 | 0.2321 |
| 9888 | UEX, Ltd. | FAIL_UWAHIGE | 1247.0 | 0.6875 |
| 265A | HMCOMM INC | FAIL_INSEN | 701.0 | 0.1111 |
| 3696 | セレス | FAIL_INSEN | 2252.0 | 0.4634 |
| 4431 | Smaregi, Inc. | FAIL_INSEN | 3535.0 | 0.5246 |
| 4483 | JMDC Inc. | FAIL_INSEN | 3430.0 | 0.2727 |
| 5027 | AnyMind Group | FAIL_INSEN | 829.0 | 0.3077 |
| 6080 | M&A Capital Partners Co.,Ltd. | FAIL_INSEN | 4255.0 | 0.6667 |
| 7695 | 交換できるくん | FAIL_INSEN | 914.0 | 0.0000 |

### 除籍リスト（first_seenから30暦日超）
該当なし

## 機械詳細
- 検知内訳: PASS=55 / PASS_DOJI=0 / FAIL_UWAHIGE=116 / FAIL_INSEN=226 / SKIP=0
- スキップ件数: 0件（Yahoo Finance取得397銘柄すべて成功・ステイルなし）
- night_gate.log 追記: base_day=2026-08-27分を追記（同一base_day無し・最新30営業日保持）
- ヘッドラインの抜粋件数と群別内訳: 上限なし（PASS全55件に付与）。内訳=method16/granville36/changepoint3
- gate_history の書き込み結果: gate_history/2026-08-27.json を新規作成
- grades.json の銘柄数とバイト数: 401銘柄・112981バイト（110.3KB）
- method_score を保持できた件数／null件数: 60件／337件
- ヘッドライン付与件数（PASS全件と一致するか）: 55/55件（一致）
- kabutan 新規取得件数／50件上限で打ち切った件数: 27件／0件（上限未到達）
- profile_cache の総数と本夜の追加件数: 総数226件・本夜追加27件
- 業態が「未取得」のまま出た件数: 0件（PASS全55件で取得済み）
- earnings_log の総数／本夜の追記件数／リターンを埋めた件数／日足が取れず埋められなかった件数: 0件／0件／0件／0件（当夜📊決算発表の検知なし）
- gyoseki_cache の history に退避した件数: 0件（新規5銘柄はキャッシュ初回登録のためhistory対象外）
- STEP4.8週末ブリーフ: スキップ（week_open=false、実行日2026-08-27木曜・翌営業日2026-08-28金曜は週初条件に非該当）
- gyoseki再計算: 5件（no_cache: 3449/4220/4258/7350/9934）／valuation新規static: 5件（同一5銘柄）
- STEP1候補収集: main候補+未マージPR由来3ブランチ(claude/focused-newton-gbjs5p, claude/gracious-fermi-ftrm2l, claude/vigilant-euler-2le52h)から実差分37件を採用。pool 380→397件（新規17件・除籍0件）
- master.json 変更行数: 別途PR本文に記載（indent幅=1で書き出し・git diff --numstatで実測）
