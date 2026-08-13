# 夜間ゲート 2026-08-13

## サマリー
- 評価数: 210銘柄
- PASS数: 57件（PASS 57 / PASS_DOJI 0）
- 発注可能提案数: 49件
- 市場一言: 堅調（半導体主導リスクオン）
- 実行モード: 通常モード
- base_day: 2026-08-13

## 検証結果
- V1(四者一致): ✅ today_proposals=49 / results_entry_price=49 / template_lines=49
- V2(PASS収支): ✅ PASS=57 = 発注可能49 + 除外8、null order_status=0件
- V3(重複/単一verdict): ✅ 重複0件
- V4(valuation static不変): ✅ 変更0件
- V5(許可キー以外不変): ✅ top差分[] / pipeline差分[]
- V6(gyoseki絵文字整合): ✅ 不整合0件
- V7(board必須セクション): 本ファイル生成により充足
- V8(模擬テンプレ書式): ✅ 違反0件（｜後空白/単元記載/カンマ無し を機械検証済み）

## 保有アラート
### 9304 澁澤倉庫（現物）
- 終値1955.0円／取得1786.0円／stop1800／target2150／25日線乖離3.63%
- 業績: ⚡好調
- 値頃感: ⚪妥当
- SLまで7.93% / targetまで9.97%。✅建値へSL切り上げ済み/超(stop=1800>=cost=1786.0、残存リスク0円以下=枠解放)
- タイムストップ期日2026-08-17（残2営業日）(問題なし)
- memo: G②押し目(中期上昇トレンド内)/急落からの25日線上反発継続シナリオ/否定=1620割れ(構造SL)

### 4536 参天製薬（現物/ちょる子リバ）
- 終値1964.0円／取得1920.0円／stop1840／target2250／25日線乖離-1.79%
- ⚠足が崩れた（premise_kill）: 陰線・25日線割れ
- 業績: ✅順調
- 値頃感: ⚪妥当
- SLまで6.31% / targetまで14.56%。
- タイムストップ期日2026-08-24（残7営業日）(問題なし)
- memo: ちょる子リバ/決算後のちょい押しも業績は好調/否定=直近の上昇機運の打ち消し

### 3407 旭化成（信用買建/G④下げすぎリバ）
- 終値1724.0円／取得1650.0円／stop1650／target1900／25日線乖離-3.53%
- ⚠足が崩れた（premise_kill）: 陰線・上髭0.25超・25日線割れ
- 業績: ⚡好調
- 値頃感: 🟡やや割高
- SLまで4.29% / targetまで10.21%。✅建値へSL切り上げ済み/超(stop=1650>=cost=1650.0、残存リスク0円以下=枠解放)
- タイムストップ期日2026-08-21（残6営業日）(問題なし)
- memo: G④下げすぎリバ/谷からの陽線坊主に乗っかり順調に上昇(SL 1580→1650へトレール済み)/否定=未記入(要追記)

### 6327 北川精機（信用買建/G④下げすぎリバ）
- 終値3640.0円／取得3240.0円／stop3400／target6900／25日線乖離-6.99%
- ⚠足が崩れた（premise_kill）: 陰線・上髭0.25超・25日線割れ
- ⚠決算接近(2026-08-18, 残3営業日)
- 業績: 🔥絶好調
- 値頃感: ⚪妥当
- SLまで6.59% / targetまで89.56%。✅建値へSL切り上げ済み/超(stop=3400>=cost=3240.0、残存リスク0円以下=枠解放)
- タイムストップ期日2026-08-25（残8営業日）(問題なし)
- memo: G④下げすぎリバ/揉み合いの中での前日陽線に期待し再参戦、決算近く業績も良いので決算前の上昇を取りに行く(SL 3080→3400へトレール済み)/否定=未記入(要追記)

### 7685 ＢｕｙＳｅｌｌ　Ｔｅｃｈｎｏｌｏｇｉｅｓ（信用買建）
- 終値3305.0円／取得3055.0円／stop3080／target4000／25日線乖離1.69%
- 🚨決算直前(2026-08-14, 残1営業日) — 跨ぐか手仕舞うかを今夜決める
- 業績: 🚀確変
- 値頃感: ⚪妥当
- SLまで6.81% / targetまで21.03%。✅建値へSL切り上げ済み/超(stop=3080>=cost=3055.0、残存リスク0円以下=枠解放)
- タイムストップ期日2026-08-25（残8営業日）(問題なし)
- memo: 手法ブランチ未記入/強烈な上げと下げが続く中、下髭の長い十字陽線をきっかけに参戦(SL 2900→3080へトレール済み)/否定=未記入(要追記)

## 前夜の結果
PL5口座への正式な反映は週次①-11の採点で行われる。ここは参考情報。
前夜2026-08-12の提案53件 → 約定38件・不約定15件・判定不能0件

約定銘柄:

| コード | 約定価格 | 当日終値 | 含み損益% |
|---|---|---|---|
| 3915 | 2315.0 | 2339.0 | +1.04% |
| 9211 | 1551.0 | 1529.0 | -1.42% |
| 4063 | 6410.0 | 6378.0 | -0.50% |
| 6656 | 865.0 | 897.0 | +3.70% |
| 7730 | 1595.0 | 1604.0 | +0.56% |
| 5301 | 1818.5 | 1812.5 | -0.33% |
| 5254 | 4430.0 | 4365.0 | -1.47% |
| 6327 | 3550.0 | 3640.0 | +2.54% |
| 3776 | 254.0 | 250.0 | -1.57% |
| 7685 | 3285.0 | 3305.0 | +0.61% |
| 7318 | 1588.0 | 1421.0 | -10.52% |
| 9147 | 5668.0 | 5592.0 | -1.34% |
| 5537 | 3200.0 | 3125.0 | -2.34% |
| 3491 | 1517.0 | 1479.0 | -2.50% |
| 5189 | 3670.0 | 3630.0 | -1.09% |
| 5590 | 712.0 | 709.0 | -0.42% |
| 1898 | 1463.0 | 1471.0 | +0.55% |
| 6071 | 852.0 | 857.0 | +0.59% |
| 6080 | 4040.0 | 4035.0 | -0.12% |
| 3993 | 2940.0 | 2951.0 | +0.37% |
| 4536 | 1969.5 | 1964.0 | -0.28% |
| 8844 | 1218.0 | 1234.0 | +1.31% |
| 5243 | 2491.0 | 2532.0 | +1.65% |
| 9037 | 1867.0 | 1859.0 | -0.43% |
| 2982 | 420.0 | 424.0 | +0.95% |
| 205A | 1677.0 | 1674.0 | -0.18% |
| 9341 | 606.0 | 603.0 | -0.50% |
| 4765 | 615.0 | 622.0 | +1.14% |
| 8057 | 2150.0 | 2140.0 | -0.47% |
| 7182 | 3142.0 | 3223.0 | +2.58% |
| 9888 | 1271.0 | 1275.0 | +0.31% |
| 3441 | 2751.0 | 2715.0 | -1.31% |
| 5036 | 1632.0 | 1642.0 | +0.61% |
| 5302 | 5000.0 | 5050.0 | +1.00% |
| 4972 | 3305.0 | 3315.0 | +0.30% |
| 3994 | 5696.0 | 5874.0 | +3.12% |
| 4478 | 2808.0 | 2844.0 | +1.28% |
| 265A | 675.0 | 677.0 | +0.30% |

## 模擬テンプレ
```
# base_day 2026-08-13 ／ 提案49件
# 使い方: 参戦する0〜3銘柄の行だけをコピーし、｜の後ろに参戦理由を書いてポジション株PJへ送る。
# 選ばなかった行は送らなくてよい（全行に理由を書く必要はない）。見送りは末尾の1行で足りる。
# 特定銘柄を理由つきで見送る場合のみ『模擬 見送り {code} ｜{理由}』を送る。
模擬 4826 granville_tenkan 逆指値530 SL497.3 単元100 ｜
模擬 8056 granville_tenkan 逆指値4508 SL4236.6 単元100 ｜
模擬 8511 granville_oshime 指値2444.4 SL2432.24 単元100 ｜
模擬 276A kenmo_momentum 逆指値3416 SL3210.1 単元100 ｜
模擬 7085 granville_oshime 指値949.85 SL945.12 単元100 ｜
模擬 6656 granville_rebound 指値897 SL794 単元100 ｜
模擬 9627 granville_tenkan 逆指値6099 SL5732.1 単元100 ｜
模擬 2602 granville_oshime 指値1929.68 SL1920.08 単元100 ｜
模擬 7611 granville_tenkan 逆指値2892 SL2717.5 単元100 ｜
模擬 7685 choruko_reversal 指値3305 SL2968 単元100 ｜
模擬 8361 granville_oshime 指値7712.37 SL7674 単元100 ｜
模擬 8366 choruko_reversal 指値2691 SL2466 単元100 ｜
模擬 9101 granville_tenkan 逆指値6216 SL5842.1 単元100 ｜
模擬 4249 kenmo_newhigh 逆指値2901 SL2726 単元100 ｜
模擬 9552 kenmo_momentum 逆指値1017 SL955 単元100 ｜
模擬 6071 granville_rebound 指値857 SL811 単元100 ｜
模擬 5243 kenmo_momentum 逆指値2544 SL2390.4 単元100 ｜
模擬 6632 choruko_reversal 指値1029 SL937 単元100 ｜
模擬 8522 granville_oshime 指値6612.1 SL6579.2 単元100 ｜
模擬 8008 granville_oshime 指値2081.44 SL2071.08 単元100 ｜
模擬 9324 granville_oshime 指値2527.9 SL2515.32 単元100 ｜
模擬 8628 granville_oshime 指値1077.24 SL1071.88 単元100 ｜
模擬 421A granville_rebound 指値3650 SL3140 単元100 ｜
模擬 9519 granville_rebound 指値944 SL864 単元100 ｜
模擬 5989 granville_rebound 指値1457 SL1396 単元100 ｜
模擬 4498 変化点🔔🔔 指値1287 SL1199 単元100 🔒 ｜
模擬 146A kenmo_momentum 逆指値4006 SL3764.7 単元100 ｜
模擬 4765 granville_tenkan 逆指値624 SL585.6 単元100 ｜
模擬 7184 granville_oshime 指値2954.14 SL2939.44 単元100 ｜
模擬 7182 granville_rebound 指値3223 SL3036 単元100 ｜
模擬 2483 granville_rebound 指値2174 SL2080 単元100 ｜
模擬 9888 変化点🔔🔔 指値1275 SL990 単元100 🔒 ｜
模擬 5724 kenmo_momentum 逆指値2839 SL2667.7 単元100 ｜
模擬 1960 kenmo_newhigh 逆指値1730 SL1625.3 単元100 ｜
模擬 166A granville_oshime 指値1107.71 SL1102.2 単元100 ｜
模擬 4415 granville_oshime 指値1365.67 SL1358.88 単元100 ｜
模擬 8544 granville_oshime 指値2696.82 SL2683.4 単元100 ｜
模擬 6703 granville_rebound 指値2960 SL2736 単元100 ｜
模擬 7505 granville_rebound 指値2068 SL2000 単元100 ｜
模擬 9502 granville_rebound 指値2821 SL2661 単元100 ｜
模擬 3994 変化点🔔 指値5874 SL5098 単元100 🔒 ｜
模擬 6492 kenmo_momentum 逆指値15731 SL14786.2 単元100 ｜
模擬 3723 kenmo_momentum 逆指値2900 SL2725.1 単元100 ｜
模擬 8927 kenmo_momentum 逆指値473 SL443.7 単元100 ｜
模擬 4599 kenmo_newhigh 逆指値360 SL337.5 単元100 ｜
模擬 9503 granville_tenkan 逆指値2407 SL2261.6 単元100 ｜
模擬 2975 granville_tenkan 逆指値1602 SL1504.9 単元100 ｜
模擬 7888 granville_oshime 指値918.57 SL901.64 単元100 ｜
模擬 584A 変化点🔔 指値2730 SL2172 単元100 🔒 ｜
模擬 見送り ｜
```

## PASS内訳
PASS 57件 = 発注可能 49件 + 除外 8件

除外銘柄:
- 8084 ＲＹＯＤＥＮ: ⛔提案なし(手法ブランチ不明)
- 9274 ＫＰＰグループホールディングス: ⛔型不一致: 既に支持帯以下
- 3151 バイタルケーエスケー・ホールディングス（バイタルＫＳ）: ⛔型不一致: 既に支持帯以下
- 6324 ハーモニック・ドライブ・システムズ（ハーモニック）: ⛔提案なし(手法ブランチ不明)
- 7480 スズデン: ⛔提案なし(手法ブランチ不明)
- 150A JSH: ⛔提案なし(材料後出し)
- 2810 ハウス食品グループ本社: ⛔型不一致: 既に支持帯以下
- 6638 ミマキエンジニアリング: ⛔型不一致: 既に支持帯以下

## 5手法銘柄
| コード 名前 | 手法チップ | 業績チップ | 値頃感チップ | ゲート判定 | 終値 | 💰単元金額 | 提案 | ⚠/📋チップ |
|---|---|---|---|---|---|---|---|---|
| 7480 スズデン | stf_kakuhen | 🚀確変(13/13) | ⚪妥当(3.0/7) | PASS | 3420.0 | 34.2万円 | ⛔提案なし(手法ブランチ不明) |  |

> 📌【業態】FA機器主力、技術商社。オムロンと特約店契約。電設資材中心。ネット販売に強み。
> 【いま】本日+4.1%（終値3420円）。材料未確認
> 【調子】🚀確変（13/13） — A4/B4軸
> 【水準】⚪妥当（3.0/7） — PER15.6倍・PEG0.19・52週91% ／ 💰単元34.2万円
> 【戦略】⛔提案なし(手法ブランチ不明)のため見送りまたは待機。チャート再確認を推奨。

| 7685 ＢＵＹＳＥＬＬ　ＴＥＣＨＮＯＬＯＧＩＥＳ | choruko_reversal/granville_rebound | 🚀確変(11/13) | ⚪妥当(4.0/7) | PASS | 3305.0 | 33.0万円 | reversal 3305.0 | ⚠決算 08/14(残1営業日) |

> 📌【業態】出張買取を中心に多様なリユース商材の買取や販売。高額品などシニア向け強み。
> 【いま】本日-0.3%（終値3305円）。材料未確認
> 【調子】🚀確変（11/13） — A3/B4軸
> 【水準】⚪妥当（4.0/7） — PER21.7倍・PEG0.27・52週69% ／ 💰単元33.0万円
> 【戦略】終値指値3305.0円でのリバウンド狙い。SL2968.0円。

| 5243 note inc. | kenmo_momentum/未マージPR由来 | 🚀確変(11/13) | ⚪妥当(4.0/7) | PASS | 2532.0 | 25.3万円 | momentum 2544.0 | 抵抗圏(60日高値近接・閾値0.15) |
| 5724 Asaka Riken Co., Ltd. | kenmo_momentum | 🚀確変(11/13) | 🟢値頃(5.0/7) | PASS | 2828.0 | 28.3万円 | momentum 2839.0 |  |

> 📌【業態】電子部品等からの貴金属回収・精錬。独自技術に強み。環境事業に注力。
> 【いま】本日+3.9%（終値2828円）。材料未確認
> 【調子】🚀確変（11/13） — A2/B4軸
> 【水準】🟢値頃（5.0/7） — PER18.2倍・PEG0.13・52週38% ／ 💰単元28.3万円
> 【戦略】逆指値2839.0円で高値超えを確認してからの追随。上限2866.4円、SL2667.7円。

| 3723 Nihon Falcom Corporation | kenmo_momentum | 🚀確変(11/13) | ⚪妥当(3.0/7) | PASS | 2899.0 | 29.0万円 | momentum 2900.0 |  |

> 📌【業態】プレステ用ゲームソフトの開発が主力。RPG系に強み。アプリなどのライセンス事業も。
> 【いま】本日+9.4%（終値2899円）。材料未確認
> 【調子】🚀確変（11/13） — A3/B3軸
> 【水準】⚪妥当（3.0/7） — PER19.1倍・PEG0.31・52週96% ／ 💰単元29.0万円
> 【戦略】逆指値2900.0円で高値超えを確認してからの追随。上限2928.0円、SL2725.1円。

| 8084 ＲＹＯＤＥＮ | stf_kakuhen | 🔥絶好調(9/13) | ⚪妥当(3.0/7) | PASS | 4605.0 | 46.0万円 | ⛔提案なし(手法ブランチ不明) | 抵抗圏(60日高値近接・閾値0.15) |

> 📌【業態】三菱電機系最大商社。半導体、冷熱住機、ビル昇降機など他社も幅広く展開。
> 【いま】本日+3.4%（終値4605円）。材料未確認
> 【調子】🔥絶好調（9/13） — A2/B2軸
> 【水準】⚪妥当（3.0/7） — PER16.5倍・PEG0.55・52週95% ／ 💰単元46.0万円
> 【戦略】⛔提案なし(手法ブランチ不明)のため見送りまたは待機。チャート再確認を推奨。

| 6324 ハーモニック・ドライブ・システムズ（ハーモニック） | stf_kakuhen | 🔥絶好調(9/13) | ⚪妥当(4.0/7) | PASS | 6750.0 | 67.5万円 | ⛔提案なし(手法ブランチ不明) |  |

> 📌【業態】精密制御減速装置が軸。小型・軽量強み。産業用ロボット向け等。メカトロ製品も。
> 【いま】本日+5.5%（終値6750円）。材料未確認
> 【調子】🔥絶好調（9/13） — A2/B4軸
> 【水準】⚪妥当（4.0/7） — PER106.5倍・PEG0.48・52週65% ／ 💰単元67.5万円
> 【戦略】⛔提案なし(手法ブランチ不明)のため見送りまたは待機。チャート再確認を推奨。

| 4249 森六 | kenmo_newhigh/stf_kakuhen | 🔥絶好調(8/13) | 🟢値頃(5.0/7) | PASS | 2900.0 | 29.0万円 | momentum 2901.0 | 抵抗圏(60日高値近接・閾値0.15) |

> 📌【業態】化学製品、樹脂加工品の製造販売。ホンダ車の内・外装向け大。点滴バッグも。
> 【いま】本日+1.1%（終値2900円）。材料未確認
> 【調子】🔥絶好調（8/13） — A4/B3軸
> 【水準】🟢値頃（5.0/7） — PER7.7倍・PEG0.19・52週100% ／ 💰単元29.0万円
> 【戦略】逆指値2901.0円で高値超えを確認してからの追随。上限2929.0円、SL2726.0円。

| 146A Columbia Works Inc. | kenmo_momentum | ⚡好調(7/13) | 💎割安(6.0/7) | PASS | 4005.0 | 40.0万円 | momentum 4006.0 | 抵抗圏(60日高値近接・閾値0.15) |
| 8927 Meiho Enterprise Co., Ltd. | kenmo_momentum | ⚡好調(7/13) | 💎割安(7.0/7) | PASS | 472.0 | 4.7万円 | momentum 473.0 | 抵抗圏(60日高値近接・閾値0.15) |

> 📌【業態】首都圏中心に賃貸アパート開発。マンション開発は休止。仲介や管理、中古再生も。
> 【いま】本日+1.5%（終値472円）。材料未確認
> 【調子】⚡好調（7/13） — A2/B3軸
> 【水準】💎割安（7.0/7） — PER5.8倍・PEG0.13・52週37% ／ 💰単元4.7万円
> 【戦略】逆指値473.0円で高値超えを確認してからの追随。上限476.7円、SL443.7円。

| 9552 Quants Research Institute Holdings, Inc. | kenmo_momentum/未マージPR由来 | ⚡好調(6/13) | ⚪妥当(4.0/7) | PASS | 1012.0 | 10.1万円 | momentum 1017.0 | ⚠決算 08/14(残1営業日) |
| 6632 ＪＶＣケンウッド | choruko_reversal | ➖横ばい(2/13) | ⚪妥当(3.0/7) | PASS | 1029.0 | 10.3万円 | reversal 1029.0 |  |
| 1960 サンテック | kenmo_newhigh | ➖横ばい(2/13) | 🔴過熱(1.0/7) | PASS | 1720.0 | 17.2万円 | momentum 1730.0 | 抵抗圏(60日高値近接・閾値0.15) |
| 276A CCReB Advisors Inc. | kenmo_momentum | 判定保留 | 🟢値頃(5.0/7) | PASS | 3400.0 | 34.0万円 | momentum 3416.0 |  |
| 8366 滋賀銀行 | choruko_reversal | 取得不可 | ⚪妥当(3.0/7) | PASS | 2691.0 | 26.9万円 | reversal 2691.0 |  |
| 6492 Okano Valve Mfg. Co., Ltd. | kenmo_momentum | 判定保留(変則決算) | ⚪妥当(4.0/7) | PASS | 15720.0 | 157.2万円 | momentum 15731.0 |  |

> 📌【業態】発電用バルブ最大手。原子力、火力向けに強み。保守点検も手掛ける。
> 【いま】本日+7.9%（終値15720円）。材料未確認
> 【調子】判定保留(変則決算) — 決算期変更(変マーク検出)のため前期比較不能
> 【水準】⚪妥当（4.0/7） — PER18.0倍・PEG0.17・52週59% ／ 💰単元157.2万円
> 【戦略】逆指値15731.0円で高値超えを確認してからの追随。上限15887.3円、SL14786.2円。

| 4599 ステムリム | kenmo_newhigh | 業績データ取得不可 | ⏸判定不能 | PASS | 356.0 | 3.6万円 | momentum 360.0 | 抵抗圏(60日高値近接・閾値0.15) 📋カルテ窓 09/09(残19営業日) |

> 📌【業態】大阪大学発バイオベンチャー。自己組織再生を促進する「再生誘導医薬」開発。
> 【いま】本日+3.8%（終値356円）。材料未確認
> 【調子】業績データ取得不可 — 売上/経常データ欠落
> 【水準】⏸判定不能 — PER不明倍・PEG不明・52週97% ／ 💰単元3.6万円
> 【戦略】逆指値360.0円で高値超えを確認してからの追随。上限362.6円、SL337.5円。


## グランビル銘柄
| コード 名前 | 手法チップ | 業績チップ | 値頃感チップ | ゲート判定 | 終値 | 💰単元金額 | 提案 | ⚠/📋チップ |
|---|---|---|---|---|---|---|---|---|
| 421A ムービン・ストラテジック・キャリア（ムービン） | granville_rebound | 🔥絶好調(10/13) | ⚪妥当(4.0/7) | PASS | 3650.0 | 36.5万円 | reversal 3650.0 |  |
| 6071 ＩＢＪ | granville_rebound | 🔥絶好調(8/13) | ⚪妥当(3.0/7) | PASS | 857.0 | 8.6万円 | reversal 857.0 | ⚠決算 08/14(残1営業日) |
| 8008 ヨンドシーホールディングス（４℃ホールデ） | granville_oshime/未マージPR由来 | 🔥絶好調(8/13) | ⚪妥当(3.0/7) | PASS | 2085.0 | 20.9万円 | oshime 2081.44 |  |
| 150A JSH | granville_rebound | 🔥絶好調(8/13) | 🟢値頃(5.0/7) | PASS | 519.0 | 5.2万円 | ⛔提案なし(材料後出し) | ⚠決算 08/13(残0営業日) |

> 📌【業態】障がい者雇用支援の農園や訪問看護・診療サービスなどを手掛ける。
> 【いま】本日+3.6%（終値519円）。📊決算発表（4-6月期(1Q)経常は102倍増益で着地、今期..）
> 【調子】🔥絶好調（8/13） — C軸=黒字転換のためB/A比算出不可・QoQトレンドで代用
> 【水準】🟢値頃（5.0/7） — PER15.3倍・PEG0.03・52週52% ／ 💰単元5.2万円
> 【戦略】⛔提案なし(材料後出し)のため見送りまたは待機。チャート再確認を推奨。

| 8522 名古屋銀行（名古屋銀） | granville_oshime/未マージPR由来 | ⚡好調(7/13) | ⚪妥当(4.0/7) | PASS | 6910.0 | 69.1万円 | oshime 6612.1 | 抵抗圏(60日高値近接・閾値0.15) |
| 166A タスキホールディングス | granville_oshime | ⚡好調(7/13) | ⚪妥当(4.0/7) | PASS | 1158.0 | 11.6万円 | oshime 1107.71 |  |
| 6656 インスペック | granville_rebound/未マージPR由来 | ⚡好調(6/13) | ⚪妥当(3.0/7) | PASS | 897.0 | 9.0万円 | reversal 897.0 |  |
| 2602 日清オイリオグループ | granville_oshime | ⚡好調(6/13) | ⚪妥当(3.0/7) | PASS | 1978.0 | 19.8万円 | oshime 1929.68 | 抵抗圏(60日高値近接・閾値0.15) |
| 2975 スターマイカ | granville_tenkan | ⚡好調(6/13) | 🟢値頃(5.0/7) | PASS | 1598.0 | 16.0万円 | momentum 1602.0 |  |
| 7085 カーブスホールディングス | granville_oshime | ⚡好調(5/13) | 🟡やや割高(2.0/7) | PASS | 958.0 | 9.6万円 | oshime 949.85 |  |
| 7505 扶桑電通 | granville_rebound | ⚡好調(5/13) | ⚪妥当(4.0/7) | PASS | 2068.0 | 20.7万円 | reversal 2068.0 |  |
| 7888 三光合成 | granville_oshime | ⚡好調(5/13) | ⚪妥当(4.0/7) | PASS | 927.0 | 9.3万円 | oshime 918.57 |  |
| 9627 アインホールディングス | granville_tenkan | ✅順調(4/13) | ⚪妥当(3.0/7) | PASS | 6082.0 | 60.8万円 | momentum 6099.0 |  |
| 7611 ハイデイ日高 | granville_tenkan | ✅順調(4/13) | 🟡やや割高(2.0/7) | PASS | 2885.0 | 28.9万円 | momentum 2892.0 |  |
| 9101 日本郵船 | granville_tenkan | ✅順調(4/13) | ⚪妥当(4.0/7) | PASS | 6211.0 | 62.1万円 | momentum 6216.0 | 抵抗圏(60日高値近接・閾値0.15) |
| 4826 ＣＩＪ | granville_tenkan | ✅順調(3/13) | 🔴過熱(1.0/7) | PASS | 529.0 | 5.3万円 | momentum 530.0 | 抵抗圏(60日高値近接・閾値0.15) |
| 8056 ＢＩＰＲＯＧＹ | granville_tenkan | ✅順調(3/13) | 🟢値頃(5.0/7) | PASS | 4490.0 | 44.9万円 | momentum 4508.0 |  |
| 9274 ＫＰＰグループホールディングス | granville_oshime | ✅順調(3/13) | 🔴過熱(1.0/7) | PASS | 1085.0 | 10.8万円 | ⛔型不一致: 既に支持帯以下 |  |
| 2483 翻訳センター | granville_rebound | ➖横ばい(2/13) | 🟡やや割高(2.0/7) | PASS | 2174.0 | 21.7万円 | reversal 2174.0 |  |
| 6703 沖電気工業 | granville_rebound | ➖横ばい(2/13) | ⚪妥当(3.0/7) | PASS | 2960.0 | 29.6万円 | reversal 2960.0 |  |
| 9503 関西電力 | granville_tenkan | 🔻悪化(2/13) | ⚪妥当(3.0/7) | PASS | 2399.5 | 24.0万円 | momentum 2407.0 | ⚠業績基調が下向き（🔻悪化） |
| 3151 バイタルケーエスケー・ホールディングス（バイタルＫＳ） | granville_oshime/granville_rebound/未マージPR由来 | 🔻悪化(1/13) | 🔴過熱(1.0/7) | PASS | 1605.0 | 16.1万円 | ⛔型不一致: 既に支持帯以下 | ⚠業績基調が下向き（🔻悪化） |
| 9324 安田倉庫（安田倉） | granville_oshime/未マージPR由来 | ⚠減速(1/13) | 🔴過熱(1.0/7) | PASS | 2552.0 | 25.5万円 | oshime 2527.9 | ⚠業績基調が下向き（⚠減速） |
| 5989 エイチワン | granville_rebound/未マージPR由来 | ⚠減速(1/13) | ⚪妥当(3.0/7) | PASS | 1457.0 | 14.6万円 | reversal 1457.0 | ⚠業績基調が下向き（⚠減速） |
| 9502 中部電力 | granville_rebound | 🔻悪化(1/13) | 🟡やや割高(2.0/7) | PASS | 2821.0 | 28.2万円 | reversal 2821.0 | ⚠業績基調が下向き（🔻悪化） |
| 2810 ハウス食品グループ本社 | granville_oshime | ⚠減速(1/13) | 🔴過熱(1.0/7) | PASS | 3777.0 | 37.8万円 | ⛔型不一致: 既に支持帯以下 | ⚠業績基調が下向き（⚠減速） |
| 6638 ミマキエンジニアリング | granville_oshime | ⚠減速(1/13) | ⚪妥当(3.0/7) | PASS | 1933.0 | 19.3万円 | ⛔型不一致: 既に支持帯以下 | ⚠業績基調が下向き（⚠減速） |
| 8511 日本証券金融 | granville_oshime | 取得不可 | 🔴過熱(0.0/7) | PASS | 2530.0 | 25.3万円 | oshime 2444.4 |  |
| 8361 大垣共立銀行 | granville_oshime | 取得不可 | ⚪妥当(4.0/7) | PASS | 8040.0 | 80.4万円 | oshime 7712.37 |  |
| 8628 松井証券（松井） | granville_oshime/未マージPR由来 | 業績データ取得不可 | ⏸判定不能 | PASS | 1108.0 | 11.1万円 | oshime 1077.24 |  |
| 9519 レノバ | granville_rebound/未マージPR由来 | 取得不可 | ⚪妥当(4.0/7) | PASS | 944.0 | 9.4万円 | reversal 944.0 |  |
| 4765 SBIグローバルアセットマネジメント | granville_tenkan | 判定保留 | ⏸判定不能 | PASS | 622.0 | 6.2万円 | momentum 624.0 | 抵抗圏(60日高値近接・閾値0.15) |
| 7184 富山第一銀行 | granville_oshime | 取得不可 | 🔴過熱(1.0/7) | PASS | 3265.0 | 32.6万円 | oshime 2954.14 | 抵抗圏(60日高値近接・閾値0.15) |
| 7182 ゆうちょ銀行 | granville_rebound | 取得不可 | ⚪妥当(3.0/7) | PASS | 3223.0 | 32.2万円 | reversal 3223.0 |  |
| 4415 ブロードエンタープライズ | granville_oshime | 業績データ取得不可 | ⚪妥当(4.0/7) | PASS | 1378.0 | 13.8万円 | oshime 1365.67 |  |

> 📌【業態】マンション向け高速インターネットやIoTインターフォンシステムの販売。全戸一括でマンション管理も。
> 【いま】本日-0.3%（終値1378円）。材料未確認
> 【調子】業績データ取得不可 — 売上/経常データ欠落
> 【水準】⚪妥当（4.0/7） — PER不明倍・PEG不明・52週74% ／ 💰単元13.8万円
> 【戦略】押し目指値1365.67円で25日線/押し安値付近を待つ。SL1358.88円。

| 8544 京葉銀行 | granville_oshime | 業績データ取得不可 | ⚪妥当(3.0/7) | PASS | 2834.0 | 28.3万円 | oshime 2696.82 |  |

## 変化点銘柄（参考）
| コード 名前 | 手法チップ | 業績チップ | 値頃感チップ | ゲート判定 | 終値 | 💰単元金額 | 提案 | ⚠/📋チップ |
|---|---|---|---|---|---|---|---|---|
| 4498 Cybertrust Japan Co., Ltd. | changepoint/変化点🔔🔔 | ✅順調(4/13) | ⚪妥当(3.0/7) | PASS | 1287.0 | 12.9万円 | changepoint 1287.0 | 抵抗圏(60日高値近接・閾値0.15) |
| 9888 UEX, Ltd. | 変化点🔔🔔 | 🔥絶好調(8/13) | 🟢値頃(5.0/7) | PASS | 1275.0 | 12.8万円 | changepoint 1275.0 | 抵抗圏(60日高値近接・閾値0.15) |
| 3994 マネーフォワード | 変化点🔔 | ⚡好調(6/13) | 🔴過熱(1.4/7) | PASS | 5874.0 | 58.7万円 | changepoint 5874.0 |  |
| 584A ＬｉＮＫＸ | 変化点🔔 | ✅順調(4/13) | 🟡やや割高(2.0/7) | PASS | 2730.0 | 27.3万円 | changepoint 2730.0 | ⚠決算 08/14(残1営業日) |

（📌ヘッドラインは手法スコア降順で上位12件のみ生成。45件省略）

## ⭐理想形（🚀確変/🔥絶好調 × 💎割安/🟢値頃）
- 150A JSH: 🔥絶好調 × 🟢値頃
- 4249 森六: 🔥絶好調 × 🟢値頃
- 5724 Asaka Riken Co., Ltd.: 🚀確変 × 🟢値頃
- 9888 UEX, Ltd.: 🔥絶好調 × 🟢値頃

## ⚡材料後出し
その日の足は開示前の情報。判定は参考値。
- 5892 yutori,Inc.: verdict=FAIL_INSEN / 📊決算発表 「4-6月期(1Q)経常は26％減益で着地」（）/ order_status=(非PASS)
- 4165 PLAID Inc.: verdict=FAIL_UWAHIGE / 📉下方修正 「今期経常を33％下方修正」（）/ order_status=(非PASS)
- 5537 AlbaLink Co.,Ltd.: verdict=FAIL_INSEN / 📢上方修正 「今期経常を6％上方修正・最高益予想を上..」（）/ order_status=(非PASS)
- 5590 NETSTARS Co.,Ltd.: verdict=FAIL_UWAHIGE / 📊決算発表 「上期経常が61％増益で着地・4-6月期は17..」（）/ order_status=(非PASS)
- 3993 PKSHA Technology Inc.: verdict=FAIL_UWAHIGE / 📊決算発表 「4-6月期(3Q)最終は31％増益」（）/ order_status=(非PASS)
- 4377 ONE CAREER Inc.: verdict=FAIL_INSEN / 📊決算発表 「上期経常が75％増益で着地・4-6月期も66..」（）/ order_status=(非PASS)
- 150A JSH: verdict=PASS / 📊決算発表 「4-6月期(1Q)経常は102倍増益で着地、今期..」（）/ order_status=⛔提案なし(材料後出し)
- 5036 日本ビジネスシステムズ: verdict=FAIL_UWAHIGE / 📊決算発表 「10-6月期(3Q累計)経常が18％増益で着地・..」（）/ order_status=(非PASS)
- 4478 フリー: verdict=FAIL_UWAHIGE / 📊決算発表 「前期経常は81％増で2期連続最高益」（）/ order_status=(非PASS)
- 4894 Cuorips Inc.: verdict=FAIL_UWAHIGE / 📊決算発表 「4-6月期(1Q)経常は赤字拡大で着地」（）/ order_status=(非PASS)
- 5586 Laboro.AI, Inc.: verdict=FAIL_INSEN / 📢上方修正 「今期経常を31％上方修正・最高益予想を上..」（）/ order_status=(非PASS)
- 269A Sapeet, Inc.: verdict=FAIL_INSEN / 📊決算発表 「10-6月期(3Q累計)経常は18倍増益・通期計..」（）/ order_status=(非PASS)
- 479A ＰＲＯＮＩ: verdict=FAIL_UWAHIGE / 📊決算発表 「上期経常は2.2倍増益で着地」（）/ order_status=(非PASS)

## 📢開示
使用した一覧URL: https://kabutan.jp/warning/?mode=4_2 （取引時間中）, https://kabutan.jp/warning/?mode=4_3 （取引終了後）。フォールバックは使用せず（一覧取得に成功）。

- 150A JSH: 📊決算発表 「4-6月期(1Q)経常は102倍増益で着地、今期..」（, after_close）
- 3968 セグエグループ: 📢上方修正 「今期経常を13％上方修正・最高益予想を上..」（, intraday_before_close）
- 4058 Toyokumo, Inc.: 📢上方修正 「今期経常を11％上方修正・最高益予想を上..」（, intraday_before_close）
- 7409 AeroEdge Co.,Ltd: 📊決算発表 「今期経常は29％増で2期連続最高益更新へ」（, intraday_before_close）
- 269A Sapeet, Inc.: 📊決算発表 「10-6月期(3Q累計)経常は18倍増益・通期計..」（, after_close）
- 3993 PKSHA Technology Inc.: 📊決算発表 「4-6月期(3Q)最終は31％増益」（, after_close）
- 4165 PLAID Inc.: 📉下方修正 「今期経常を33％下方修正」（, after_close）
- 4377 ONE CAREER Inc.: 📊決算発表 「上期経常が75％増益で着地・4-6月期も66..」（, after_close）
- 4478 フリー: 📊決算発表 「前期経常は81％増で2期連続最高益」（, after_close）
- 479A ＰＲＯＮＩ: 📊決算発表 「上期経常は2.2倍増益で着地」（, after_close）
- 4894 Cuorips Inc.: 📊決算発表 「4-6月期(1Q)経常は赤字拡大で着地」（, after_close）
- 5036 日本ビジネスシステムズ: 📊決算発表 「10-6月期(3Q累計)経常が18％増益で着地・..」（, after_close）
- 5537 AlbaLink Co.,Ltd.: 📢上方修正 「今期経常を6％上方修正・最高益予想を上..」（, after_close）
- 5586 Laboro.AI, Inc.: 📢上方修正 「今期経常を31％上方修正・最高益予想を上..」（, after_close）
- 5590 NETSTARS Co.,Ltd.: 📊決算発表 「上期経常が61％増益で着地・4-6月期は17..」（, after_close）
- 5892 yutori,Inc.: 📊決算発表 「4-6月期(1Q)経常は26％減益で着地」（, after_close）

①-9へ引き渡し15件

## 総当りゲート
| コード 名前 | branch_type | verdict | 終値 |
|---|---|---|---|
| 8084 ＲＹＯＤＥＮ | method | PASS | 4605.0 |
| 276A CCReB Advisors Inc. | method | PASS | 3400.0 |
| 7685 ＢＵＹＳＥＬＬ　ＴＥＣＨＮＯＬＯＧＩＥＳ | method | PASS | 3305.0 |
| 8366 滋賀銀行 | method | PASS | 2691.0 |
| 4249 森六 | method | PASS | 2900.0 |
| 9552 Quants Research Institute Holdings, Inc. | method | PASS | 1012.0 |
| 5243 note inc. | method | PASS | 2532.0 |
| 6632 ＪＶＣケンウッド | method | PASS | 1029.0 |
| 6324 ハーモニック・ドライブ・システムズ（ハーモニック） | method | PASS | 6750.0 |
| 7480 スズデン | method | PASS | 3420.0 |
| 146A Columbia Works Inc. | method | PASS | 4005.0 |
| 5724 Asaka Riken Co., Ltd. | method | PASS | 2828.0 |
| 1960 サンテック | method | PASS | 1720.0 |
| 6492 Okano Valve Mfg. Co., Ltd. | method | PASS | 15720.0 |
| 3723 Nihon Falcom Corporation | method | PASS | 2899.0 |
| 8927 Meiho Enterprise Co., Ltd. | method | PASS | 472.0 |
| 4599 ステムリム | method | PASS | 356.0 |
| 3915 TerraSky Co., Ltd. | method | FAIL_UWAHIGE | 2339.0 |
| 8697 日本取引所グループ | method | FAIL_UWAHIGE | 2289.0 |
| 8388 阿波銀行 | method | FAIL_UWAHIGE | 9390.0 |
| 456A ＨＵＭＡＮ　ＭＡＤＥ | method | FAIL_UWAHIGE | 1416.0 |
| 1980 ダイダン | method | FAIL_UWAHIGE | 2707.0 |
| 5574 ABEJA,Inc. | method | FAIL_UWAHIGE | 2815.0 |
| 7730 マニー | method | FAIL_UWAHIGE | 1604.0 |
| 4165 PLAID Inc. | method | FAIL_UWAHIGE | 594.0 |
| 341A TOYOKOH Inc. | method | FAIL_UWAHIGE | 1975.0 |
| 3091 ブロンコビリー | method | FAIL_UWAHIGE | 2632.0 |
| 3374 内外テック | method | FAIL_UWAHIGE | 4485.0 |
| 5590 NETSTARS Co.,Ltd. | method | FAIL_UWAHIGE | 709.0 |
| 6785 Suzuki Co., Ltd. | method | FAIL_UWAHIGE | 3055.0 |
| 5757 CK San-Etsu Co., Ltd. | method | FAIL_UWAHIGE | 5090.0 |
| 9533 東邦瓦斯 | method | FAIL_UWAHIGE | 1171.5 |
| 9341 GENOVA Inc. | method | FAIL_UWAHIGE | 603.0 |
| 1435 robot home Inc. | method | FAIL_UWAHIGE | 171.0 |
| 4894 Cuorips Inc. | method | FAIL_UWAHIGE | 5280.0 |
| 9270 Valuence Holdings, Inc. | method | FAIL_UWAHIGE | 2026.0 |
| 7089 For Startups, Inc. | method | FAIL_INSEN | 1576.0 |
| 262A INTERMESTIC INC. | method | FAIL_INSEN | 1930.0 |
| 9211 f-code Inc. | method | FAIL_INSEN | 1529.0 |
| 9962 ミスミグループ本社 | method | FAIL_INSEN | 3739.0 |
| 7731 ニコン | method | FAIL_INSEN | 2034.0 |
| 5301 東海カーボン | method | FAIL_INSEN | 1812.5 |
| 5892 yutori,Inc. | method | FAIL_INSEN | 2197.0 |
| 5254 Arent, Inc. | method | FAIL_INSEN | 4365.0 |
| 7409 AeroEdge Co.,Ltd | method | FAIL_INSEN | 1531.0 |
| 6857 アドバンテスト | method | FAIL_INSEN | 35940.0 |
| 7318 SERENDIP HOLDINGS Co. Ltd. | method | FAIL_INSEN | 1421.0 |
| 2980 SRE Holdings Corp. | method | FAIL_INSEN | 2518.0 |
| 4477 BASE, Inc. | method | FAIL_INSEN | 285.0 |
| 5537 AlbaLink Co.,Ltd. | method | FAIL_INSEN | 3125.0 |
| 7047 PORT INC. | method | FAIL_INSEN | 2200.0 |
| 5027 AnyMind Group Inc. | method | FAIL_INSEN | 588.0 |
| 6135 牧野フライス製作所 | method | FAIL_INSEN | 14680.0 |
| 212A FIT EASY Inc. | method | FAIL_INSEN | 3040.0 |
| 1979 大気社 | method | FAIL_INSEN | 4065.0 |
| 9072 ニッコンホールディングス | method | FAIL_INSEN | 5364.0 |
| 1975 朝日工業社 | method | FAIL_INSEN | 3810.0 |
| 4536 参天製薬 | method | FAIL_INSEN | 1964.0 |
| 543A ＡＲＣＨＩＯＮ | method | FAIL_INSEN | 272.0 |
| 6562 Geniee, Inc. | method | FAIL_INSEN | 1068.0 |
| 9302 三井倉庫ホールディングス | method | FAIL_INSEN | 3329.0 |
| 4516 日本新薬 | method | FAIL_INSEN | 3613.0 |
| 9308 乾汽船 | method | FAIL_INSEN | 2033.0 |
| 6134 ＦＵＪＩ | method | FAIL_INSEN | 8232.0 |
| 3036 アルコニックス（アルコニクス） | method | FAIL_INSEN | 3595.0 |
| 7267 ホンダ | method | FAIL_INSEN | 1647.5 |
| 6490 ＰＩＬＬＡＲ | method | FAIL_INSEN | 10440.0 |
| 7637 白銅 | method | FAIL_INSEN | 3810.0 |
| 325A TENTIAL, Inc. | method | FAIL_INSEN | 1548.0 |
| 135A VRAIN Solution,Inc. | method | FAIL_INSEN | 3870.0 |
| 4377 ONE CAREER Inc. | method | FAIL_INSEN | 2166.0 |
| 147A SORACOM,INC. | method | FAIL_INSEN | 1056.0 |
| 3798 ULS Group Incorporated | method | FAIL_INSEN | 509.0 |
| 3441 Sanno Co., Ltd. | method | FAIL_INSEN | 2715.0 |
| 4058 Toyokumo, Inc. | method | FAIL_INSEN | 2301.0 |
| 5586 Laboro.AI, Inc. | method | FAIL_INSEN | 840.0 |
| 4826 ＣＩＪ | granville | PASS | 529.0 |
| 8056 ＢＩＰＲＯＧＹ | granville | PASS | 4490.0 |
| 8511 日本証券金融 | granville | PASS | 2530.0 |
| 7085 カーブスホールディングス | granville | PASS | 958.0 |
| 6656 インスペック | granville | PASS | 897.0 |
| 9274 ＫＰＰグループホールディングス | granville | PASS | 1085.0 |
| 9627 アインホールディングス | granville | PASS | 6082.0 |
| 2602 日清オイリオグループ | granville | PASS | 1978.0 |
| 7611 ハイデイ日高 | granville | PASS | 2885.0 |
| 8361 大垣共立銀行 | granville | PASS | 8040.0 |
| 9101 日本郵船 | granville | PASS | 6211.0 |
| 6071 ＩＢＪ | granville | PASS | 857.0 |
| 8522 名古屋銀行（名古屋銀） | granville | PASS | 6910.0 |
| 8008 ヨンドシーホールディングス（４℃ホールデ） | granville | PASS | 2085.0 |
| 3151 バイタルケーエスケー・ホールディングス（バイタルＫＳ） | granville | PASS | 1605.0 |
| 9324 安田倉庫（安田倉） | granville | PASS | 2552.0 |
| 8628 松井証券（松井） | granville | PASS | 1108.0 |
| 421A ムービン・ストラテジック・キャリア（ムービン） | granville | PASS | 3650.0 |
| 9519 レノバ | granville | PASS | 944.0 |
| 5989 エイチワン | granville | PASS | 1457.0 |
| 4765 SBIグローバルアセットマネジメント | granville | PASS | 622.0 |
| 7184 富山第一銀行 | granville | PASS | 3265.0 |
| 7182 ゆうちょ銀行 | granville | PASS | 3223.0 |
| 2483 翻訳センター | granville | PASS | 2174.0 |
| 150A JSH | granville | PASS | 519.0 |
| 166A タスキホールディングス | granville | PASS | 1158.0 |
| 4415 ブロードエンタープライズ | granville | PASS | 1378.0 |
| 8544 京葉銀行 | granville | PASS | 2834.0 |
| 6703 沖電気工業 | granville | PASS | 2960.0 |
| 7505 扶桑電通 | granville | PASS | 2068.0 |
| 9502 中部電力 | granville | PASS | 2821.0 |
| 9503 関西電力 | granville | PASS | 2399.5 |
| 2975 スターマイカ | granville | PASS | 1598.0 |
| 7888 三光合成 | granville | PASS | 927.0 |
| 2810 ハウス食品グループ本社 | granville | PASS | 3777.0 |
| 6638 ミマキエンジニアリング | granville | PASS | 1933.0 |
| 7956 ピジョン | granville | FAIL_UWAHIGE | 2103.5 |
| 4848 フルキャストホールディングス | granville | FAIL_UWAHIGE | 1845.0 |
| 8276 平和堂 | granville | FAIL_UWAHIGE | 2728.0 |
| 8707 岩井コスモホールディングス | granville | FAIL_UWAHIGE | 4415.0 |
| 8367 南都銀行 | granville | FAIL_UWAHIGE | 1925.0 |
| 3989 シェアリングテクノロジー | granville | FAIL_UWAHIGE | 1466.0 |
| 5076 インフロニアＨＤ | granville | FAIL_UWAHIGE | 2744.0 |
| 8242 エイチ・ツー・オー　リテイリング | granville | FAIL_UWAHIGE | 2850.5 |
| 7970 信越ポリマー | granville | FAIL_UWAHIGE | 2310.0 |
| 7231 トピー工業 | granville | FAIL_UWAHIGE | 2944.0 |
| 1898 世紀東急工業 | granville | FAIL_UWAHIGE | 1471.0 |
| 9517 イーレックス | granville | FAIL_UWAHIGE | 843.0 |
| 3993 PKSHA Technology Inc. | granville | FAIL_UWAHIGE | 2951.0 |
| 8844 コスモスイニシア | granville | FAIL_UWAHIGE | 1234.0 |
| 2982 ＡＤワークスグループ（ＡＤＷＧ） | granville | FAIL_UWAHIGE | 424.0 |
| 6266 タツモ | granville | FAIL_UWAHIGE | 3910.0 |
| 7744 ノーリツ鋼機 | granville | FAIL_UWAHIGE | 2126.0 |
| 3765 ガンホー・オンライン・エンターテイメント | granville | FAIL_UWAHIGE | 2410.0 |
| 2702 日本マクドナルド HD | granville | FAIL_UWAHIGE | 7910.0 |
| 5384 フジミインコーポレーテッド | granville | FAIL_UWAHIGE | 4100.0 |
| 2874 横浜冷凍 | granville | FAIL_UWAHIGE | 2076.0 |
| 5036 日本ビジネスシステムズ | granville | FAIL_UWAHIGE | 1642.0 |
| 5302 日本カーボン | granville | FAIL_UWAHIGE | 5050.0 |
| 8923 トーセイ | granville | FAIL_UWAHIGE | 1766.0 |
| 9941 太洋物産 | granville | FAIL_UWAHIGE | 1164.0 |
| 4972 綜研化学 | granville | FAIL_UWAHIGE | 3315.0 |
| 9319 中央倉庫 | granville | FAIL_UWAHIGE | 1778.0 |
| 7860 エイベックス | granville | FAIL_UWAHIGE | 1225.0 |
| 3863 日本製紙 | granville | FAIL_UWAHIGE | 1402.0 |
| 1860 戸田建設 | granville | FAIL_UWAHIGE | 1488.5 |
| 6718 アイホン | granville | FAIL_INSEN | 2841.0 |
| 4420 イーソル | granville | FAIL_INSEN | 685.0 |
| 8081 カナデン | granville | FAIL_INSEN | 2474.0 |
| 3880 大王製紙 | granville | FAIL_INSEN | 964.0 |
| 4063 信越化学工業 | granville | FAIL_INSEN | 6378.0 |
| 6590 芝浦メカトロニクス | granville | FAIL_INSEN | 4380.0 |
| 9031 西日本鉄道 | granville | FAIL_INSEN | 3023.0 |
| 6327 北川精機 | granville | FAIL_INSEN | 3640.0 |
| 2175 エス・エム・エス | granville | FAIL_INSEN | 2295.0 |
| 8098 稲畑産業 | granville | FAIL_INSEN | 4125.0 |
| 9869 加藤産業 | granville | FAIL_INSEN | 6460.0 |
| 8570 イオンフィナンシャルサービス | granville | FAIL_INSEN | 1645.0 |
| 3776 ブロードバンドタワー | granville | FAIL_INSEN | 250.0 |
| 6613 Ｇ−ＱＤレーザ | granville | FAIL_INSEN | 1746.0 |
| 9147 ＮＩＰＰＯＮ　ＥＸＰＲＥＳＳ　ホールディングス | granville | FAIL_INSEN | 5592.0 |
| 3491 ＧＡ　ｔｅｃｈｎｏｌｏｇｉｅｓ | granville | FAIL_INSEN | 1479.0 |
| 8876 リログループ | granville | FAIL_INSEN | 2169.0 |
| 9854 愛眼 | granville | FAIL_INSEN | 283.0 |
| 4419 Ｆｉｎａｔｅｘｔホールディングス | granville | FAIL_INSEN | 1269.0 |
| 8141 新光商事 | granville | FAIL_INSEN | 1565.0 |
| 4320 ＣＥホールディングス | granville | FAIL_INSEN | 1649.0 |
| 5189 櫻護謨 | granville | FAIL_INSEN | 3630.0 |
| 4847 インテリジェント　ウェイブ | granville | FAIL_INSEN | 1273.0 |
| 7806 ＭＴＧ | granville | FAIL_INSEN | 8090.0 |
| 547A ムニノバホールディングス（ムニノバＨＤ） | granville | FAIL_INSEN | 453.0 |
| 9037 ハマキョウレックス（ハマキョウ） | granville | FAIL_INSEN | 1859.0 |
| 5406 神戸製鋼所（神戸鋼） | granville | FAIL_INSEN | 1980.0 |
| 2659 サンエー | granville | FAIL_INSEN | 3320.0 |
| 3865 北越コーポレーション（北越コーポ） | granville | FAIL_INSEN | 903.0 |
| 1925 大和ハウス工業（大和ハウス） | granville | FAIL_INSEN | 4607.0 |
| 4413 ボードルア | granville | FAIL_INSEN | 2754.0 |
| 9882 イエローハット（イエロハット） | granville | FAIL_INSEN | 1754.0 |
| 254A ＡＩフュージョンキャピタルグループ（ＡＩＦＣＧ） | granville | FAIL_INSEN | 1160.0 |
| 205A ロゴスホールディングス（ロゴスＨＤ） | granville | FAIL_INSEN | 1674.0 |
| 6284 Nissei ASB Machine Co., Ltd. | granville | FAIL_INSEN | 9450.0 |
| 3968 セグエグループ | granville | FAIL_INSEN | 590.0 |
| 8919 カチタス | granville | FAIL_INSEN | 3565.0 |
| 8086 ニプロ | granville | FAIL_INSEN | 1585.0 |
| 8057 内田洋行 | granville | FAIL_INSEN | 2140.0 |
| 6023 ダイハツインフィニアース | granville | FAIL_INSEN | 2921.0 |
| 6925 ウシオ電機 | granville | FAIL_INSEN | 4335.0 |
| 4392 FIG | granville | FAIL_INSEN | 900.0 |
| 3393 スターティア HD | granville | FAIL_INSEN | 3005.0 |
| 9247 TRE HD | granville | FAIL_INSEN | 2031.0 |
| 5020 ＥＮＥＯＳホールディングス | granville | FAIL_INSEN | 1282.5 |
| 3048 ビックカメラ | granville | FAIL_INSEN | 1722.0 |
| 208A 構造計画研究所ホールディングス | granville | FAIL_INSEN | 2995.0 |
| 9041 近鉄グループホールディングス | granville | FAIL_INSEN | 3539.0 |
| 7981 タカラスタンダード | granville | FAIL_INSEN | 3045.0 |
| 269A Sapeet, Inc. | granville | FAIL_INSEN | 2456.0 |
| 6305 日立建機 | granville | FAIL_INSEN | 5580.0 |
| 2317 システナ | granville | FAIL_INSEN | 428.0 |
| 6380 オリエンタルチエン工業 | granville | FAIL_INSEN | 3660.0 |
| 3544 サツドラＨＤ | granville | FAIL_INSEN | 1248.0 |
| 5998 アドバネクス | granville | FAIL_INSEN | 2346.0 |
| 4498 Cybertrust Japan Co., Ltd. | changepoint | PASS | 1287.0 |
| 9888 UEX, Ltd. | changepoint | PASS | 1275.0 |
| 3994 マネーフォワード | changepoint | PASS | 5874.0 |
| 584A ＬｉＮＫＸ | changepoint | PASS | 2730.0 |
| 3923 ラクス | changepoint | FAIL_UWAHIGE | 1094.0 |
| 4478 フリー | changepoint | FAIL_UWAHIGE | 2844.0 |
| 479A ＰＲＯＮＩ | changepoint | FAIL_UWAHIGE | 1437.0 |
| 4483 JMDC Inc. | changepoint | FAIL_INSEN | 3415.0 |
| 9343 ibis inc. | changepoint | FAIL_INSEN | 752.0 |
| 6080 M&A Capital Partners Co.,Ltd. | changepoint | FAIL_INSEN | 4035.0 |
| 4375 Safie Inc. | changepoint | FAIL_INSEN | 625.0 |
| 265A HMCOMM | changepoint | FAIL_INSEN | 677.0 |
| 4441 トビラシステムズ | changepoint | FAIL_INSEN | 1486.0 |

### 除籍リスト
該当なし

## 機械詳細
- 検知内訳: {'FAIL_INSEN': 101, 'PASS': 57, 'FAIL_UWAHIGE': 52}
- スキップ件数: 0
- log追記件数: 1件（2026-08-13分、既存同日分は置換）
- ヘッドライン省略件数: 45
- gyoseki再計算: 19件 / valuation再計算: 54件
- 開示検出: 取引時間中39件 / 引け後188件
