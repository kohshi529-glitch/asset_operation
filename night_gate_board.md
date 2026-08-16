# 夜間ゲート 2026-08-14（休日準備モード）

休日準備モード: 実行日2026-08-16(日)は非営業日、翌営業日2026-08-17(月)に向けた発注準備。trading_day=直近営業日2026-08-14(金)。

## サマリー

- 評価数: 225銘柄（method 78 / granville 134 / changepoint 13）
- PASS: 91件（PASS 90 + PASS_DOJI 1）
- 発注可能提案数: 74件（除外17件）
- 市場一言: 堅調（2026-08-14, 日経+1.16%・半導体主導リスクオン）
- 実行モード: 休日準備モード
- base_day: 2026-08-14
- week_open: true（実行日が日曜のため週末ブリーフを実施）

## 検証結果

- V1 四者一致: night_gate_today.json proposals=74 / results entry_price保持=74 / 模擬テンプレ「模擬 」行=74（見送り除く）/ 通知母数=74 → **一致**
- V2 PASS収支: PASS+PASS_DOJI=91 = 発注可能74 + 除外17（型不一致5・材料後出し2・単元不明7・手法不明3）。除外全件にorder_status記載・null 0件 → **OK**
- V3 code重複: 0件・各verdict単一値 → **OK**
- V4 valuation_cache既存static変更: 0件（既存84銘柄のstaticは未変更、dynamic層のみ更新） → **OK**
- V5 master.json許可キー以外の変更: 0箇所（night_gate.*/gyoseki_cache/valuation_cache/pipeline.runs.night_gateのみ変更を確認） → **OK**
- V6 gyoseki_cache grade整合: 全96対象銘柄でemoji/グレード名がgyoseki_spec.categoriesと一致（判定保留系の特殊値2件を除き不整合0件） → **OK**
- V7 board.md必須セクション: サマリー/検証結果/前夜の結果/模擬テンプレ/PASS内訳/📅今週のカタリスト すべて存在 → **OK**
- V8 模擬テンプレ書式: 74行すべて①｜後ろ空 ②単元記載あり ③カンマなし → **OK**
- V9 gate_history: gate_history/2026-08-14.json 新規作成・night_gate_today.jsonとバイト単位一致 → **OK**
- V10 base_day整合: night_gate.results / night_gate_today.json / gate_history/2026-08-14.json / 模擬テンプレ1行目 すべて2026-08-14で一致 → **OK**
- V11 書き出し整形: git diff --numstat master.json = +4646/-3578（5,000行未満）。検出indent幅=1。過大な全体再フォーマットなし → **OK**

## 保有アラート

保有6銘柄・アラートあり（5銘柄で足の崩れ検知）。Drive取得: trade_master JSON（2026-08-15 06:58更新・prices_as_of 2026-08-14）読み取り成功。

- **9304 澁澤倉庫**（現物）: 終値1977.0円 含み損益+19,100円 | 業績⚡好調(6/13) 値頃感⚪妥当(4.0/7,PER15.22倍/52週84.5%) | ⚠足が崩れた（premise_kill）陰線/上髭0.5263 25日線乖離+4.5% | stop1800(残9.0%,枠解放) target2150(残8.8%) | 経過10営業日(タイムストップ残0)
- **4536 参天製薬**（現物/ちょる子リバ）: 終値1918.5円 含み損益-150円 | 業績✅順調(4/13) 値頃感判定不能(None/7,PER15.41倍/52週57.9%) | ⚠足が崩れた（premise_kill）陰線/上髭0.2385 25日線乖離-3.6% | stop1840(残4.1%,リスク未解放) target2250(残17.3%) | 経過5営業日(タイムストップ残5)
- **3407 旭化成**（信用買建/G④下げすぎリバ）: 終値1702.0円 含み損益+5,200円 | 業績⚡好調(6/13) 値頃感⚪妥当(3.0/7,PER14.25倍/52週74.3%) | ⚠足が崩れた（premise_kill）陰線/上髭0.0323 25日線乖離-4.4% | stop1650(残3.1%,枠解放) target1900(残11.6%) | 経過6営業日(タイムストップ残4)
- **4413 ボードルア**（信用買建）: 終値2843.0円 含み損益+4,300円 | 業績🔥絶好調(8/13) 値頃感判定不能(None/7,PER28.29倍/52週68.0%) | ⚠足が崩れた（premise_kill）陰線/上髭0.4589 25日線乖離-3.4% | ⚠目標未設定(SL/target未記録) | 経過2営業日(タイムストップ残8)
- **7888 三光合成**（信用買建）: 終値931.0円 含み損益+200円 | 業績⚡好調(5/13) 値頃感⚪妥当(4.0/7,PER6.31倍/52週54.1%) | ⚠足が崩れた（premise_kill）陰線/上髭0.3158 25日線乖離+2.5% | ⚠目標未設定(SL/target未記録) | 経過0営業日(タイムストップ残10)
- **8008 ４℃HD**（信用買建）: 終値2118.0円 含み損益+2,800円 | 業績🔥絶好調(8/13) 値頃感⚪妥当(3.0/7,PER17.18倍/52週81.7%) | ⚠目標未設定(SL/target未記録) | 経過0営業日(タイムストップ残10)

## 📅今週のカタリスト

- 今週のカタリスト: 該当なし（保有銘柄・PASS銘柄とも次回決算日は取得不可＝⚠日程不明。catalyst_schedule.eventsにも該当期間(08/17〜08/21)のイベントなし）
- 今週の市場イベント:
  - 08/17(月) 日本4-6月期GDP速報値
  - 08/19(水) FOMC議事要旨(7/28-29開催分)公表
  - 08/21(金) 日本7月全国CPI
- 週末材料: 該当なし（WebSearchで保有銘柄・PASS銘柄に関する有意な週末材料は確認できず）
- theme_watch/changepoint_watch週次サマリー: saas_naiseika テーマ 20銘柄中15銘柄が🔔/🔔🔔点灯（479A🔔🔔/478A🔔/4478🔔/4418🔔🔔/5574🔔🔔/4493🔔/4475🔔/4165🔔/4443🔔/3993🔔🔔/4483🔔🔔/3994🔔/4375🔔/4180🔔/3923🔔）。changepoint_watch 7銘柄中7銘柄点灯（3374🔔🔔/4441🔔/4478🔔🔔/4498🔔🔔/479A🔔/584A🔔/6857🔔🔔）
- カタリストは日程であって売買理由ではない。跨ぐか手仕舞うかは事前に決める（教訓⑲）

## 前夜の結果

PL5口座への正式な反映は週次①-11の採点で行われる。ここは参考情報。

前夜(2026-08-13)の提案49件 → 約定29・不約定20・判定不能0

約定した銘柄（29件）の一部抜粋（詳細はnight_gate_today.json.prev_fillsを参照）:
- 421A: 約定・含み益+6.85%
- 5724: 約定・含み益+5.63%
- 8056: 約定・含み益+2.76%
- 9101: 約定・含み益+2.58%
- 9888: 約定・含み益+1.5%

## 模擬テンプレ

```
# base_day 2026-08-14 ／ 提案74件
# 使い方: 参戦する0〜3銘柄の行だけをコピーし、｜の後ろに参戦理由を書いてポジション株PJへ送る。
# 選ばなかった行は送らなくてよい（全行に理由を書く必要はない）。見送りは末尾の1行で足りる。
# 特定銘柄を理由つきで見送る場合のみ『模擬 見送り {code} ｜{理由}』を送る。
模擬 7089 kenmo_momentum 逆指値1607 SL1509.6 単元100 ｜
模擬 4826 granville_tenkan 逆指値540 SL506.7 単元100 ｜
模擬 6718 granville_tenkan 逆指値2866 SL2693.1 単元100 ｜
模擬 4420 granville_rebound 指値737 SL677 単元100 ｜
模擬 3915 kenmo_momentum 逆指値2441 SL2293.6 単元100 ｜
模擬 8081 granville_rebound 指値2521 SL2377 単元100 ｜
模擬 8056 granville_tenkan 逆指値4669 SL4387.9 単元100 ｜
模擬 456A choruko_reversal 指値1429 SL1352 単元100 ｜
模擬 276A granville_oshime 指値3521.3 SL3503.8 単元100 ｜
模擬 5574 kenmo_momentum 逆指値3046 SL2862.3 単元100 ｜
模擬 7085 granville_oshime 指値951.3 SL946.52 単元100 ｜
模擬 7730 choruko_reversal 指値1620 SL1515 単元100 ｜
模擬 5892 kenmo_momentum 逆指値2549 SL2395.1 単元100 ｜
模擬 9274 granville_oshime 指値1090.6 SL1085.16 単元100 ｜
模擬 8098 granville_tenkan 逆指値4196 SL3943.3 単元100 ｜
模擬 4165 kenmo_momentum 逆指値691 SL648.6 単元100 ｜
模擬 2602 granville_oshime 指値1934.5 SL1924.88 単元100 ｜
模擬 7611 granville_tenkan 逆指値2920 SL2743.9 単元100 ｜
模擬 2980 kenmo_momentum 逆指値2627 SL2468.4 単元100 ｜
模擬 3491 granville_tenkan 逆指値1532 SL1439.1 単元100 ｜
模擬 7047 kenmo_momentum 逆指値2284 SL2146 単元100 ｜
模擬 9854 granville_rebound 指値293 SL274 単元100 ｜
模擬 4419 granville_oshime 指値1394 SL1252 単元100 ｜
模擬 6135 choruko_reversal 指値15350 SL14340 単元100 ｜
模擬 212A kenmo_momentum 逆指値3091 SL2904.6 単元100 ｜
模擬 8141 granville_rebound 指値1570 SL1565 単元100 ｜
模擬 5076 granville_rebound 指値2838 SL2534.5 単元100 ｜
模擬 4249 kenmo_newhigh 逆指値2940 SL2762.7 単元100 ｜
模擬 8242 granville_oshime 指値2849.1 SL2834.92 単元100 ｜
模擬 7231 granville_tenkan 逆指値3021 SL2838.8 単元100 ｜
模擬 1898 granville_tenkan 逆指値1496 SL1405.3 単元100 ｜
模擬 9517 granville_oshime 指値854.2 SL849.92 単元100 ｜
模擬 3993 granville_tenkan 逆指値3186 SL2993.9 単元100 ｜
模擬 5757 kenmo_momentum 逆指値5141 SL4831.6 単元100 ｜
模擬 9302 choruko_reversal 指値3385 SL3187 単元100 ｜
模擬 9533 choruko_reversal 指値1175 SL1117 単元100 ｜
模擬 9037 granville_tenkan 逆指値1892 SL1777.5 単元100 ｜
模擬 2659 granville_tenkan 逆指値3331 SL3130.2 単元100 ｜
模擬 8008 granville_oshime 指値2086.2 SL2075.8 単元100 ｜
模擬 3151 granville_oshime 指値1614 SL1550 単元100 ｜
模擬 421A granville_rebound 指値3900 SL3140 単元100 ｜
模擬 205A granville_rebound 指値1691 SL1627 単元100 ｜
模擬 5989 granville_rebound 指値1510 SL1396 単元100 ｜
模擬 325A granville_oshime 指値1567.2 SL1559.44 単元100 ｜
模擬 135A kenmo_momentum 逆指値4141 SL3891.6 単元100 ｜
模擬 9341 granville_tenkan 逆指値619 SL580.9 単元100 ｜
模擬 3968 granville_tenkan 逆指値655 SL614.8 単元100 ｜
模擬 4765 granville_tenkan 逆指値619 SL580.9 単元100 ｜
模擬 8919 granville_tenkan 逆指値3576 SL3360.5 単元100 ｜
模擬 3765 granville_tenkan 逆指値2453 SL2304.9 単元100 ｜
模擬 8086 granville_tenkan 逆指値1599.5 SL1502.6 単元100 ｜
模擬 8057 granville_tenkan 逆指値2189 SL2056.7 単元100 ｜
模擬 4392 granville_rebound 指値1050 SL811 単元100 ｜
模擬 2483 granville_rebound 指値2207 SL2080 単元100 ｜
模擬 150A granville_rebound 指値619 SL461 単元100 ｜
模擬 2874 granville_oshime 指値2110 SL2003 単元100 ｜
模擬 5724 kenmo_momentum 逆指値3031 SL2848.2 単元100 ｜
模擬 1435 kenmo_momentum 逆指値180 SL168.3 単元100 ｜
模擬 5036 granville_tenkan 逆指値1618 SL1520 単元100 ｜
模擬 208A granville_tenkan 逆指値3036 SL2852.9 単元100 ｜
模擬 9041 granville_tenkan 逆指値3568 SL3353 単元100 ｜
模擬 4415 granville_oshime 指値1368 SL1361.16 単元100 ｜
模擬 8923 granville_oshime 指値1787.8 SL1778.92 単元100 ｜
模擬 9941 granville_rebound 指値1202 SL1128 単元100 ｜
模擬 7505 granville_rebound 指値2109 SL2000 単元100 ｜
模擬 9319 granville_rebound 指値1890 SL1688 単元100 ｜
模擬 9502 granville_rebound 指値2818 SL2661 単元100 ｜
模擬 4478 changepoint🔔🔔 指値3345 SL2517 単元100 🔒 ｜
模擬 8927 kenmo_momentum 逆指値479 SL449.3 単元100 ｜
模擬 9503 granville_tenkan 逆指値2409 SL2263.5 単元100 ｜
模擬 2317 granville_tenkan 逆指値442 SL414.5 単元100 ｜
模擬 6380 granville_rebound 指値3635 SL3600 単元100 ｜
模擬 1860 granville_rebound 指値1487 SL1455.5 単元100 ｜
模擬 479A changepoint🔔 指値1734 SL1330 単元100 🔒 ｜
模擬 見送り ｜
```

## PASS内訳

PASS 91件 = 発注可能 74件 + 除外 17件（型不一致5/材料後出し2/単元不明7/手法不明3）

除外銘柄一覧:
- 1605 Inpex Corporation | ⛔提案なし(単元株数不明でリスク計算不可)
- 2175 エス・エム・エス | ⛔型不一致: 既に支持帯以下
- 2217 Morozoff Limited | ⛔提案なし(単元株数不明でリスク計算不可)
- 2292 S Foods Inc. | ⛔提案なし(単元株数不明でリスク計算不可)
- 2810 House Foods Group Inc. | ⛔型不一致: 既に支持帯以下
- 3036 アルコニックス（アルコニクス） | ⛔提案なし(手法ブランチ不明)
- 3923 ラクス | ⛔提案なし(材料後出し)
- 6333 TEIKOKU Corp. | ⛔提案なし(単元株数不明でリスク計算不可)
- 6562 Geniee, Inc. | ⛔提案なし(材料後出し)
- 6571 QB Net Holdings Co., Ltd. | ⛔提案なし(単元株数不明でリスク計算不可)
- 7679 Yakuodo Holdings Co., Ltd. | ⛔提案なし(単元株数不明でリスク計算不可)
- 7860 エイベックス | ⛔型不一致: 既に支持帯以下
- 7981 タカラスタンダード | ⛔型不一致: 既に支持帯以下
- 8084 ＲＹＯＤＥＮ | ⛔提案なし(手法ブランチ不明)
- 9301 Mitsubishi Logistics Corporation | ⛔提案なし(単元株数不明でリスク計算不可)
- 9882 Yellow Hat Ltd. | ⛔型不一致: 既に支持帯以下
- 9962 ミスミグループ本社 | ⛔提案なし(手法ブランチ不明)

## 5手法銘柄

| コード | 名前 | 手法 | 業績 | 値頃感 | 判定 | 終値 | 単元金額 | 提案 | チップ |
|---|---|---|---|---|---|---|---|---|---|
| 3723 | Nihon Falcom Corporation | kenmo_momentum | - | - | FAIL_INSEN | 2903.0 | - | - | 抵抗圏(60日高値98%以上) |
| 1435 | robot home Inc. | kenmo_momentum | 🔥絶好調(8) | 💎割安(7.0) | PASS | 178.0 | 1.8万円 | momentum 180.0 | 抵抗圏(60日高値98%以上) |

> 📌 **1435 robot home Inc.**
> 【業態】不動産業。IoT賃貸経営プラットホーム「robot home」を展開。投資用不動産売買マッチングも。
> 【いま】178.0円(+4.1%)。材料未確認
> 【調子】🔥絶好調(8/13) — 経常成長率+23.1%
> 【水準】💎割安(7.0/7) — PER7.91倍・PEG0.34・52週21.4% ／ 💰単元1.8万円
> 【戦略】モメ系: 逆指値180.0(高値+1呼値) 上限181.8 SL候補168.3(高値-6%)

| 5586 | Laboro.AI, Inc. | kenmo_momentum | - | - | FAIL_INSEN | 902.0 | - | - | 抵抗圏(60日高値98%以上) |
| 5574 | ABEJA,Inc. | kenmo_momentum/変化点🔔🔔 | 🔥絶好調(8) | ⚪妥当(4.0) | PASS | 3030.0 | 30.3万円 | momentum 3046.0 | 抵抗圏(60日高値98%以上) |

> 📌 **5574 ABEJA,Inc.**
> 【業態】情報・通信業。企業のDXを支援。AIによるデジタルプラットフォーム事業の運営を手掛ける。
> 【いま】3030.0円(+7.6%)。材料未確認
> 【調子】🔥絶好調(8/13) — 各軸データより算定
> 【水準】⚪妥当(4.0/7) — PER35.48倍・PEG0.58・52週57.0% ／ 💰単元30.3万円
> 【戦略】モメ系: 逆指値3046.0(高値+1呼値) 上限3076.5 SL候補2862.3(高値-6%)

| 325A | TENTIAL, Inc. | granville_oshime/kenmo_momentum | 判定保留(変則決算) | 🟢値頃(5.0) | PASS | 1585.0 | 15.8万円 | oshime 1567.2 |  |

> 📌 **325A TENTIAL, Inc.**
> 【業態】繊維製品。リカバリーウェア「BAKUNE」などコンディショニングブランドを展開。EC軸に実店舗も。
> 【いま】1585.0円(+2.4%)。材料未確認
> 【調子】判定保留(変則決算) — 決算期変更等で前期比較不能
> 【水準】🟢値頃(5.0/7) — PER14.03倍・PEG0.06・52週67.5% ／ 💰単元15.8万円
> 【戦略】押し目系: 指値1567.2(=max(25日線1559.44,押し安値1465.0)×1.005) SL候補1559.44(25日線)

| 4377 | ONE CAREER Inc. | kenmo_momentum | - | - | FAIL_UWAHIGE | 2557.0 | - | - | 抵抗圏(60日高値98%以上) |
| 135A | VRAIN Solution,Inc. | kenmo_momentum | 🔥絶好調(8) | ⚪妥当(4.0) | PASS | 4120.0 | 41.2万円 | momentum 4141.0 |  |

> 📌 **135A VRAIN Solution,Inc.**
> 【業態】情報・通信業。製造業に特化した人工知能(AI)ソリューションの提供。検査システム。DX支援も。
> 【いま】4120.0円(+6.5%)。材料未確認
> 【調子】🔥絶好調(8/13) — D軸判定不能(四半期データ不足)
> 【水準】⚪妥当(4.0/7) — PER43.46倍・PEG0.74・52週74.7% ／ 💰単元41.2万円
> 【戦略】モメ系: 逆指値4141.0(高値+1呼値) 上限4182.4 SL候補3891.6(高値-6%)

| 5892 | yutori,Inc. | kenmo_momentum/未マージPR由来 | ⚡好調(7) | 💎割安(6.0) | PASS | 2534.0 | 25.3万円 | momentum 2549.0 | 抵抗圏(60日高値98%以上) |

> 📌 **5892 yutori,Inc.**
> 【業態】小売業。若者向け衣料品や雑貨などブランドの企画・卸売。EC販売が主軸。ZOZO傘下。
> 【いま】2534.0円(+15.3%)。材料未確認
> 【調子】⚡好調(7/13) — E軸判定不能(当期進捗率取得不可(未算出))
> 【水準】💎割安(6.0/7) — PER17.29倍・PEG0.58・52週15.3% ／ 💰単元25.3万円
> 【戦略】モメ系: 逆指値2549.0(高値+1呼値) 上限2574.5 SL候補2395.1(高値-6%)

| 4058 | Toyokumo, Inc. | kenmo_momentum | - | - | FAIL_UWAHIGE | 2382.0 | - | - |  |
| 6492 | Okano Valve Mfg. Co., Ltd. | kenmo_momentum | - | - | FAIL_INSEN | 15310.0 | - | - |  |
| 9270 | Valuence Holdings, Inc. | kenmo_momentum | - | - | FAIL_UWAHIGE | 2059.0 | - | - |  |
| 8927 | Meiho Enterprise Co., Ltd. | kenmo_momentum | ⚡好調(7) | 💎割安(7.0) | PASS | 477.0 | 4.8万円 | momentum 479.0 | 抵抗圏(60日高値98%以上) |

> 📌 **8927 Meiho Enterprise Co., Ltd.**
> 【業態】不動産業。首都圏中心に賃貸アパート開発。マンション開発は休止。仲介や管理、中古再生も。
> 【いま】477.0円(+1.1%)。材料未確認
> 【調子】⚡好調(7/13) — E軸=進捗率データ制約のため直近QoQトレンドで代用
> 【水準】💎割安(7.0/7) — PER5.84倍・PEG0.13・52週39.6% ／ 💰単元4.8万円
> 【戦略】モメ系: 逆指値479.0(高値+1呼値) 上限483.8 SL候補449.3(高値-6%)

| 5537 | AlbaLink Co.,Ltd. | kenmo_momentum/未マージPR由来 | - | - | FAIL_INSEN | 2720.0 | - | - |  |
| 4599 | ステムリム | kenmo_newhigh | - | - | FAIL_INSEN | 348.0 | - | - | 抵抗圏(60日高値98%以上) |
| 4894 | Cuorips Inc. | kenmo_momentum | - | - | FAIL_UWAHIGE | 5400.0 | - | - | 抵抗圏(60日高値98%以上) |
| 262A | INTERMESTIC INC. | kenmo_momentum | - | - | FAIL_INSEN | 1926.0 | - | - |  |
| 3915 | TerraSky Co., Ltd. | kenmo_momentum | 🔥絶好調(8) | ⚪妥当(4.0) | PASS | 2424.0 | 24.2万円 | momentum 2441.0 |  |

> 📌 **3915 TerraSky Co., Ltd.**
> 【業態】情報・通信業。クラウドシステムの導入支援や開発。セールスフォースと提携。大企業、AWS向け拡大。
> 【いま】2424.0円(+3.6%)。材料未確認
> 【調子】🔥絶好調(8/13) — E軸判定不能(進捗データ不足)
> 【水準】⚪妥当(4.0/7) — PER20.51倍・PEG0.39・52週41.9% ／ 💰単元24.2万円
> 【戦略】モメ系: 逆指値2441.0(高値+1呼値) 上限2465.4 SL候補2293.6(高値-6%)

| 5724 | Asaka Riken Co., Ltd. | kenmo_momentum | 🚀確変(11) | ⚪妥当(4.0) | PASS | 3000.0 | 30.0万円 | momentum 3031.0 | 抵抗圏(60日高値98%以上) |

> 📌 **5724 Asaka Riken Co., Ltd.**
> 【業態】非鉄金属。電子部品等からの貴金属回収・精錬。独自技術に強み。環境事業に注力。
> 【いま】3000.0円(+6.1%)。材料未確認
> 【調子】🚀確変(11/13) — E軸=進捗率データ制約のため直近QoQトレンドで代用
> 【水準】⚪妥当(4.0/7) — PER19.26倍・PEG0.14・52週42.1% ／ 💰単元30.0万円
> 【戦略】モメ系: 逆指値3031.0(高値+1呼値) 上限3061.3 SL候補2848.2(高値-6%)

| 276A | CCReB Advisors Inc. | granville_oshime/kenmo_momentum | 判定保留 | 🟢値頃(5.0) | PASS | 3540.0 | 35.4万円 | oshime 3521.3 |  |

> 📌 **276A CCReB Advisors Inc.**
> 【業態】不動産業。AIを活用した企業不動産(CRE)に関するソリューションの提供などを手掛ける。
> 【いま】3540.0円(+4.1%)。材料未確認
> 【調子】判定保留 — 判定保留(変則決算)
> 【水準】🟢値頃(5.0/7) — PER25.93倍・PEG0.35・52週18.7% ／ 💰単元35.4万円
> 【戦略】押し目系: 指値3521.3(=max(25日線3503.8,押し安値3240.0)×1.005) SL候補3503.8(25日線)

| 6857 | アドバンテスト | changepoint🔔🔔/stf_kakuhen/変化点🔔🔔 | - | - | FAIL_INSEN | 36870.0 | - | - | 抵抗圏(60日高値98%以上) |
| 3131 | シンデンハイ | stf_kakuhen | - | - | FAIL_UWAHIGE | 6880.0 | - | - | 抵抗圏(60日高値98%以上) |
| 9302 | 三井倉庫ホールディングス | choruko_reversal | ✅順調(4) | 🟡やや割高(2.0) | PASS | 3385.0 | 33.9万円 | reversal 3385.0 |  |

> 📌 **9302 三井倉庫ホールディングス**
> 【業態】倉庫・運輸。倉庫業大手。総合物流業務に強み。国際サプライチェーン展開。不動産賃貸が収益。
> 【いま】3385.0円(+1.7%)。材料未確認
> 【調子】✅順調(4/13) — 質注意
> 【水準】🟡やや割高(2.0/7) — PER20.25倍・PEG算出不可・52週20.2% ／ 💰単元33.9万円
> 【戦略】リバ系: 指値3385.0(終値指値) SL候補3187.0(直近5日安値)

| 9533 | 東邦瓦斯 | choruko_reversal | 🔻悪化(0) | 🟡やや割高(2.0) | PASS | 1175.0 | 11.8万円 | reversal 1175.0 | ⚠業績基調が下向き（🔻悪化） |

> 📌 **9533 東邦瓦斯**
> 【業態】電気・ガス。都市ガス大手。愛知、岐阜、三重が拠点。LPGに強み。コージェネ事業に注力。
> 【いま】1175.0円(+0.3%)。材料未確認
> 【調子】🔻悪化(0/13) — E軸判定不能(進捗データ不足)
> 【水準】🟡やや割高(2.0/7) — PER18.16倍・PEG算出不可・52週33.4% ／ 💰単元11.8万円
> 【戦略】リバ系: 指値1175.0(終値指値) SL候補1117.0(直近5日安値)

| 6324 | ハーモニック・ドライブ・システムズ（ハーモニック） | stf_kakuhen | - | - | FAIL_INSEN | 6510.0 | - | - |  |
| 8084 | ＲＹＯＤＥＮ | stf_kakuhen | 🔥絶好調(9) | ⚪妥当(3.0) | PASS | 4680.0 | 46.8万円 | ⛔提案なし(手法ブランチ不明) | 抵抗圏(60日高値98%以上) |

> 📌 **8084 ＲＹＯＤＥＮ**
> 【業態】卸売業。三菱電機系最大商社。半導体、冷熱住機、ビル昇降機など他社も幅広く展開。
> 【いま】4680.0円(+1.6%)。材料未確認
> 【調子】🔥絶好調(9/13) — 各軸データより算定
> 【水準】⚪妥当(3.0/7) — PER16.79倍・PEG0.56・52週99.4% ／ 💰単元46.8万円
> 【戦略】手法不明(stf_kakuhen)のため提案なし・チャート確認のみ

| 8697 | 日本取引所グループ | stf_kakuhen/変化点🔔🔔 | - | - | FAIL_INSEN | 2244.0 | - | - |  |
| 4516 | 日本新薬 | choruko_reversal | - | - | FAIL_INSEN | 3640.0 | - | - |  |
| 9308 | 乾汽船 | stf_kakuhen | - | - | FAIL_UWAHIGE | 2059.0 | - | - | 抵抗圏(60日高値98%以上) |
| 8388 | 阿波銀行 | stf_kakuhen | - | - | FAIL_INSEN | 9320.0 | - | - | 抵抗圏(60日高値98%以上) |
| 9962 | ミスミグループ本社 | stf_kakuhen | 🔥絶好調(9) | ⚪妥当(3.0) | PASS | 3831.0 | 38.3万円 | ⛔提案なし(手法ブランチ不明) |  |
| 7685 | ＢＵＹＳＥＬＬ　ＴＥＣＨＮＯＬＯＧＩＥＳ | choruko_reversal/granville_rebound | - | - | FAIL_INSEN | 3165.0 | - | - | ⚡材料後出し |
| 1979 | Taikisha Ltd. | choruko_reversal/granville_rebound/未マージPR由来 | - | - | FAIL_UWAHIGE | 4080.0 | - | - |  |
| 4249 | 森六 | kenmo_newhigh/stf_kakuhen | 🔥絶好調(8) | 🟢値頃(5.0) | PASS | 2935.0 | 29.4万円 | momentum 2940.0 | 抵抗圏(60日高値98%以上) |
| 6134 | ＦＵＪＩ | stf_kakuhen | - | - | FAIL_UWAHIGE | 8290.0 | - | - |  |
| 7480 | スズデン | stf_kakuhen | - | - | FAIL_UWAHIGE | 3410.0 | - | - |  |
| 3036 | アルコニックス（アルコニクス） | stf_kakuhen | 🔥絶好調(9) | ⚪妥当(4.0) | PASS | 3755.0 | 37.5万円 | ⛔提案なし(手法ブランチ不明) | 抵抗圏(60日高値98%以上) |
| 7267 | ホンダ | stf_kakuhen | - | - | FAIL_INSEN | 1658.0 | - | - | 抵抗圏(60日高値98%以上) |
| 6490 | ＰＩＬＬＡＲ | stf_kakuhen | - | - | FAIL_INSEN | 10180.0 | - | - |  |
| 7637 | 白銅 | stf_kakuhen | - | - | FAIL_UWAHIGE | 3970.0 | - | - | 抵抗圏(60日高値98%以上) |
| 147A | ソラコム | kenmo_momentum/stf_kakuhen | - | - | FAIL_UWAHIGE | 1077.0 | - | - |  |
| 7433 | 伯東 | stf_kakuhen | - | - | FAIL_UWAHIGE | 5280.0 | - | - |  |
| 6632 | ＪＶＣケンウッド | choruko_reversal | - | - | FAIL_UWAHIGE | 1044.0 | - | - |  |
| 7089 | For Startups, Inc. | kenmo_momentum/kenmo_newhigh | ⚡好調(7) | ⚪妥当(4.0) | PASS | 1600.0 | 16.0万円 | momentum 1607.0 |  |
| 9211 | f-code Inc. | granville_tenkan/kenmo_momentum | - | - | FAIL_UWAHIGE | 1584.0 | - | - | 抵抗圏(60日高値98%以上) ⚡材料後出し |
| 456A | ＨＵＭＡＮ　ＭＡＤＥ | choruko_reversal | ✅順調(3) | 🔴過熱(1.0) | PASS | 1429.0 | 14.3万円 | reversal 1429.0 |  |
| 1980 | ダイダン | choruko_reversal | - | - | FAIL_UWAHIGE | 2770.0 | - | - |  |
| 7731 | ニコン | choruko_reversal/granville_rebound | - | - | FAIL_UWAHIGE | 2045.5 | - | - |  |
| 7730 | マニー | choruko_reversal | ⚡好調(7) | ⚪妥当(3.0) | PASS | 1620.0 | 16.2万円 | reversal 1620.0 |  |
| 5301 | 東海カーボン | choruko_reversal | - | - | FAIL_INSEN | 1797.0 | - | - |  |
| 5254 | Arent, Inc. | granville_oshime/kenmo_momentum | - | - | FAIL_INSEN | 4305.0 | - | - |  |
| 4165 | PLAID Inc. | kenmo_momentum | ✅順調(4) | 🟡やや割高(2.8) | PASS | 683.0 | 6.8万円 | momentum 691.0 | 抵抗圏(60日高値98%以上) |
| 7409 | AeroEdge Co.,Ltd | kenmo_momentum | - | - | FAIL_INSEN | 1683.0 | - | - |  |
| 7318 | SERENDIP HOLDINGS Co. Ltd. | kenmo_momentum/変化点🔔🔔 | - | - | FAIL_UWAHIGE | 1476.0 | - | - |  |
| 2980 | SRE Holdings Corp. | kenmo_momentum | ⚡好調(5) | 🟢値頃(5.0) | PASS | 2597.0 | 26.0万円 | momentum 2627.0 |  |
| 4477 | BASE, Inc. | granville_rebound/kenmo_momentum | - | - | FAIL_UWAHIGE | 290.0 | - | - |  |
| 7047 | PORT INC. | kenmo_momentum/未マージPR由来 | 🔥絶好調(8) | 🟢値頃(5.0) | PASS | 2256.0 | 22.6万円 | momentum 2284.0 |  |
| 5027 | AnyMind Group Inc. | kenmo_momentum | - | - | FAIL_UWAHIGE | 623.0 | - | - | 抵抗圏(60日高値98%以上) ⚡材料後出し |
| 8366 | 滋賀銀行 | choruko_reversal | - | - | FAIL_UWAHIGE | 2775.0 | - | - |  |
| 6135 | 牧野フライス製作所 | choruko_reversal | ✅順調(4) | 🔴過熱(0.0) | PASS | 15350.0 | 153.5万円 | reversal 15350.0 |  |
| 212A | FIT EASY Inc. | kenmo_momentum/未マージPR由来 | 🔥絶好調(10) | ⚪妥当(4.0) | PASS | 3075.0 | 30.8万円 | momentum 3091.0 |  |
| 341A | TOYOKOH Inc. | kenmo_momentum | - | - | FAIL_UWAHIGE | 1977.0 | - | - |  |
| 3091 | ブロンコビリー | granville_oshime/stf_kakuhen | - | - | FAIL_INSEN | 2619.0 | - | - |  |
| 9072 | ニッコンホールディングス | choruko_reversal | - | - | FAIL_INSEN | 5386.0 | - | - |  |
| 9552 | Quants Research Institute Holdings, Inc. | kenmo_momentum/未マージPR由来 | - | - | FAIL_INSEN | 997.0 | - | - | ⚡材料後出し |
| 3374 | 内外テック | changepoint🔔🔔/kenmo_newhigh/変化点🔔🔔 | - | - | FAIL_INSEN | 4455.0 | - | - | 抵抗圏(60日高値98%以上) |
| 5590 | NETSTARS Co.,Ltd. | kenmo_momentum | - | - | FAIL_INSEN | 674.0 | - | - |  |
| 1975 | 朝日工業社 | choruko_reversal | - | - | FAIL_UWAHIGE | 3835.0 | - | - |  |
| 4536 | 参天製薬 | choruko_reversal | - | - | FAIL_INSEN | 1918.5 | - | - |  |
| 6785 | Suzuki Co., Ltd. | kenmo_momentum/未マージPR由来 | - | - | FAIL_UWAHIGE | 3065.0 | - | - |  |
| 543A | ＡＲＣＨＩＯＮ | choruko_reversal | - | - | FAIL_UWAHIGE | 276.0 | - | - |  |
| 5757 | CK San-Etsu Co., Ltd. | kenmo_momentum/未マージPR由来 | 🔥絶好調(10) | 💎割安(6.0) | PASS | 5100.0 | 51.0万円 | momentum 5141.0 |  |
| 5243 | note inc. | kenmo_momentum/未マージPR由来 | - | - | FAIL_UWAHIGE | 2560.0 | - | - | 抵抗圏(60日高値98%以上) |
| 6562 | Geniee, Inc. | kenmo_momentum/未マージPR由来 | 🔥絶好調(8) | 💎割安(7.0) | PASS | 1105.0 | 11.1万円 | ⛔提案なし(材料後出し) | 抵抗圏(60日高値98%以上) ⚡材料後出し |
| 146A | Columbia Works Inc. | kenmo_momentum | - | - | FAIL_INSEN | 3870.0 | - | - | 抵抗圏(60日高値98%以上) |
| 9341 | GENOVA Inc. | granville_tenkan/kenmo_momentum | 🔥絶好調(10) | 💎割安(6.0) | PASS | 616.0 | 6.2万円 | momentum 619.0 |  |
| 3798 | ULS Group Incorporated | kenmo_momentum | - | - | FAIL_UWAHIGE | 525.0 | - | - |  |
| 3441 | Sanno Co., Ltd. | kenmo_momentum | - | - | FAIL_INSEN | 2739.0 | - | - |  |
| 1960 | サンテック | kenmo_newhigh | - | - | FAIL_INSEN | 1694.0 | - | - | 抵抗圏(60日高値98%以上) |


## グランビル銘柄

| コード | 名前 | 手法 | 業績 | 値頃感 | 判定 | 終値 | 単元金額 | 提案 | チップ |
|---|---|---|---|---|---|---|---|---|---|
| 269A | Sapeet, Inc. | granville_tenkan | - | - | FAIL_INSEN | 2436.0 | - | - |  |
| 5932 | Sankyo Tateyama, Inc. | granville_tenkan | - | - | FAIL_UWAHIGE | 670.0 | - | - | 抵抗圏(60日高値98%以上) |
| 8101 | GSI Creos Corporation | granville_oshime | - | - | FAIL_UWAHIGE | 2690.0 | - | - |  |
| 7679 | Yakuodo Holdings Co., Ltd. | granville_tenkan | ➖横ばい(2) | －未評価（次回①-9で算定） | PASS | 1751.0 | - | ⛔提案なし(単元株数不明でリスク計算不可) | (質注意) |
| 4826 | ＣＩＪ | granville_tenkan | ✅順調(3) | 🔴過熱(1.0) | PASS | 537.0 | 5.4万円 | momentum 540.0 | 抵抗圏(60日高値98%以上) |
| 7956 | ピジョン | granville_oshime | - | - | FAIL_INSEN | 2113.5 | - | - | 抵抗圏(60日高値98%以上) |
| 6718 | アイホン | granville_tenkan | ⚡好調(6) | 🟢値頃(5.0) | PASS | 2860.0 | 28.6万円 | momentum 2866.0 | 抵抗圏(60日高値98%以上) |
| 4420 | イーソル | granville_rebound | 🔥絶好調(8) | ⚪妥当(4.0) | PASS | 737.0 | 7.4万円 | reversal 737.0 |  |
| 4848 | フルキャストホールディングス | granville_tenkan | - | - | FAIL_UWAHIGE | 1856.0 | - | - | 抵抗圏(60日高値98%以上) |
| 8081 | カナデン | granville_rebound | ✅順調(3) | 🟡やや割高(2.0) | PASS | 2521.0 | 25.2万円 | reversal 2521.0 |  |
| 8276 | 平和堂 | granville_tenkan/未マージPR由来 | - | - | FAIL_UWAHIGE | 2750.0 | - | - | 抵抗圏(60日高値98%以上) |
| 8056 | ＢＩＰＲＯＧＹ | granville_tenkan | ✅順調(3) | 🟢値頃(5.0) | PASS | 4653.0 | 46.5万円 | momentum 4669.0 |  |
| 3880 | 大王製紙 | granville_tenkan | - | - | FAIL_UWAHIGE | 973.0 | - | - |  |
| 8511 | 日本証券金融 | granville_oshime | - | - | FAIL_INSEN | 2527.0 | - | - | 抵抗圏(60日高値98%以上) |
| 4063 | 信越化学工業 | granville_rebound | - | - | FAIL_INSEN | 6372.0 | - | - |  |
| 8707 | 岩井コスモホールディングス | granville_oshime | - | - | FAIL_UWAHIGE | 4430.0 | - | - | 抵抗圏(60日高値98%以上) |
| 6590 | 芝浦メカトロニクス | granville_oshime | - | - | FAIL_INSEN | 4485.0 | - | - |  |
| 7085 | カーブスホールディングス | granville_oshime | ⚡好調(5) | 🟡やや割高(2.0) | PASS | 955.0 | 9.6万円 | oshime 951.3 |  |
| 6656 | インスペック | granville_rebound/未マージPR由来 | - | - | FAIL_INSEN | 873.0 | - | - |  |
| 8367 | 南都銀行 | granville_oshime | - | - | FAIL_UWAHIGE | 1941.0 | - | - | 抵抗圏(60日高値98%以上) |
| 9031 | Nishi-Nippon Railroad Co., Ltd. | granville_oshime | - | - | FAIL_UWAHIGE | 3038.0 | - | - |  |
| 9274 | ＫＰＰグループホールディングス | granville_oshime | ✅順調(3) | 🔴過熱(1.0) | PASS | 1095.0 | 10.9万円 | oshime 1090.6 |  |
| 9627 | アインホールディングス | granville_tenkan | - | - | FAIL_UWAHIGE | 6178.0 | - | - | 抵抗圏(60日高値98%以上) |
| 6327 | 北川精機 | granville_rebound | - | - | FAIL_INSEN | 3580.0 | - | - |  |
| 2175 | エス・エム・エス | granville_oshime | ➖横ばい(2) | 🔴過熱(0.0) | PASS | 2353.0 | 23.5万円 | ⛔型不一致: 既に支持帯以下 |  |
| 8098 | 稲畑産業 | granville_tenkan | ✅順調(4) | 🔴過熱(1.0) | PASS | 4190.0 | 41.9万円 | momentum 4196.0 | 抵抗圏(60日高値98%以上) |
| 2602 | 日清オイリオグループ | granville_oshime | ⚡好調(6) | ⚪妥当(3.0) | PASS | 2016.0 | 20.2万円 | oshime 1934.5 | 抵抗圏(60日高値98%以上) |
| 9869 | 加藤産業 | granville_tenkan | - | - | FAIL_UWAHIGE | 6480.0 | - | - |  |
| 3989 | シェアリングテクノロジー | granville_oshime | - | - | FAIL_UWAHIGE | 1481.0 | - | - | 抵抗圏(60日高値98%以上) ⚡材料後出し |
| 8570 | イオンフィナンシャルサービス | granville_tenkan | - | - | FAIL_INSEN | 1634.5 | - | - | 抵抗圏(60日高値98%以上) |
| 7611 | ハイデイ日高 | granville_tenkan | ✅順調(4) | 🟡やや割高(2.0) | PASS | 2914.0 | 29.1万円 | momentum 2920.0 |  |
| 3776 | ブロードバンドタワー | granville_rebound | - | - | FAIL_INSEN | 250.0 | - | - |  |
| 6613 | Ｇ−ＱＤレーザ | granville_rebound | - | - | FAIL_INSEN | 1806.0 | - | - |  |
| 8361 | 大垣共立銀行 | granville_oshime | - | - | FAIL_UWAHIGE | 8050.0 | - | - | 抵抗圏(60日高値98%以上) |
| 9147 | ＮＩＰＰＯＮ　ＥＸＰＲＥＳＳ　ホールディングス | granville_rebound | - | - | FAIL_UWAHIGE | 5684.0 | - | - | 抵抗圏(60日高値98%以上) |
| 3491 | ＧＡ　ｔｅｃｈｎｏｌｏｇｉｅｓ | granville_tenkan | 🔥絶好調(8) | 💎割安(6.0) | PASS | 1531.0 | 15.3万円 | momentum 1532.0 |  |
| 8876 | リログループ | granville_oshime | - | - | FAIL_UWAHIGE | 2161.0 | - | - | 抵抗圏(60日高値98%以上) |
| 9101 | 日本郵船 | granville_tenkan | - | - | FAIL_UWAHIGE | 6400.0 | - | - | 抵抗圏(60日高値98%以上) |
| 9854 | 愛眼 | granville_rebound | ✅順調(3) | 🔴過熱(0.0) | PASS | 293.0 | 2.9万円 | reversal 293.0 |  |
| 4419 | Ｆｉｎａｔｅｘｔホールディングス | granville_oshime/granville_rebound/変化点🔔 | 🔥絶好調(10) | ⚪妥当(4.0) | PASS | 1394.0 | 13.9万円 | reversal 1394.0 |  |
| 8141 | 新光商事 | granville_rebound/未マージPR由来 | 🔥絶好調(8) | 🟡やや割高(2.0) | PASS | 1570.0 | 15.7万円 | reversal 1570.0 |  |
| 5076 | インフロニアＨＤ | granville_rebound | ⚡好調(5) | ⚪妥当(4.0) | PASS | 2838.0 | 28.4万円 | reversal 2838.0 |  |
| 4320 | ＣＥホールディングス | granville_rebound | - | - | FAIL_INSEN | 1648.0 | - | - |  |
| 8242 | エイチ・ツー・オー　リテイリング | granville_oshime/未マージPR由来 | ⚠減速(1) | 🔴過熱(1.0) | PASS | 2867.5 | 28.7万円 | oshime 2849.1 | ⚠業績基調が下向き（⚠減速） |
| 5189 | 櫻護謨 | granville_rebound | - | - | FAIL_UWAHIGE | 3825.0 | - | - |  |
| 7970 | 信越ポリマー | granville_oshime | - | - | FAIL_UWAHIGE | 2330.0 | - | - |  |
| 7231 | トピー工業 | granville_tenkan | ➖横ばい(2) | ⚪妥当(3.0) | PASS | 3020.0 | 30.2万円 | momentum 3021.0 | 抵抗圏(60日高値98%以上) |
| 4847 | インテリジェント　ウェイブ | granville_tenkan | - | - | FAIL_UWAHIGE | 1281.0 | - | - | 抵抗圏(60日高値98%以上) |
| 7806 | ＭＴＧ | granville_oshime | - | - | FAIL_INSEN | 8130.0 | - | - | 抵抗圏(60日高値98%以上) |
| 1898 | 世紀東急工業 | granville_tenkan | ✅順調(3) | ⚪妥当(4.0) | PASS | 1495.0 | 14.9万円 | momentum 1496.0 | 抵抗圏(60日高値98%以上) |
| 6071 | ＩＢＪ | granville_rebound | - | - | FAIL_INSEN | 841.0 | - | - | ⚡材料後出し |
| 9517 | イーレックス | granville_oshime | ⚡好調(5) | 🟡やや割高(2.0) | PASS | 866.0 | 8.7万円 | oshime 854.2 |  |
| 3993 | PKSHA Technology Inc. | granville_tenkan/変化点🔔 | 業績データ取得不可 | 判定不能 | PASS | 3170.0 | 31.7万円 | momentum 3186.0 |  |
| 8844 | Cosmos Initia Co., Ltd. | granville_rebound | - | - | FAIL_INSEN | 1243.0 | - | - |  |
| 547A | ムニノバホールディングス（ムニノバＨＤ） | granville_tenkan/未マージPR由来 | - | - | FAIL_UWAHIGE | 455.0 | - | - |  |
| 9037 | ハマキョウレックス（ハマキョウ） | granville_tenkan/未マージPR由来 | ⚡好調(5) | 🟡やや割高(2.0) | PASS | 1889.0 | 18.9万円 | momentum 1892.0 | 抵抗圏(60日高値98%以上) |
| 5406 | 神戸製鋼所（神戸鋼） | granville_tenkan/未マージPR由来 | - | - | FAIL_UWAHIGE | 1986.0 | - | - |  |
| 2982 | ＡＤワークスグループ（ＡＤＷＧ） | granville_tenkan/未マージPR由来 | - | - | FAIL_INSEN | 425.0 | - | - |  |
| 2659 | サンエー | granville_tenkan/未マージPR由来 | ✅順調(3) | 🔴過熱(0.0) | PASS | 3330.0 | 33.3万円 | momentum 3331.0 | 抵抗圏(60日高値98%以上) |
| 3865 | 北越コーポレーション（北越コーポ） | granville_tenkan/未マージPR由来 | - | - | FAIL_INSEN | 895.0 | - | - |  |
| 1925 | 大和ハウス工業（大和ハウス） | granville_tenkan/未マージPR由来 | - | - | FAIL_INSEN | 4609.0 | - | - |  |
| 4413 | baudroie,inc. | granville_oshime/granville_rebound | - | - | FAIL_UWAHIGE | 2843.0 | - | - |  |
| 8522 | 名古屋銀行（名古屋銀） | granville_oshime/未マージPR由来 | - | - | FAIL_INSEN | 6870.0 | - | - | 抵抗圏(60日高値98%以上) |
| 8008 | ヨンドシーホールディングス（４℃ホールデ） | granville_oshime/未マージPR由来 | 🔥絶好調(8) | ⚪妥当(3.0) | PASS | 2118.0 | 21.2万円 | oshime 2086.2 |  |
| 9882 | Yellow Hat Ltd. | granville_oshime/未マージPR由来 | ✅順調(3) | ⚪妥当(3.0) | PASS | 1761.0 | 17.6万円 | ⛔型不一致: 既に支持帯以下 |  |
| 3151 | バイタルケーエスケー・ホールディングス（バイタルＫＳ） | granville_oshime/granville_rebound/未マージPR由来 | 🔻悪化(1) | 🔴過熱(1.0) | PASS | 1614.0 | 16.1万円 | reversal 1614.0 | ⚠業績基調が下向き（🔻悪化） |
| 9324 | 安田倉庫（安田倉） | granville_oshime/未マージPR由来 | - | - | FAIL_UWAHIGE | 2560.0 | - | - |  |
| 8628 | 松井証券（松井） | granville_oshime/未マージPR由来 | - | - | FAIL_UWAHIGE | 1105.0 | - | - | 抵抗圏(60日高値98%以上) |
| 254A | ＡＩフュージョンキャピタルグループ（ＡＩＦＣＧ） | granville_rebound/未マージPR由来 | - | - | FAIL_UWAHIGE | 1168.0 | - | - | ⚡材料後出し |
| 421A | ムービン・ストラテジック・キャリア（ムービン） | granville_rebound | 🔥絶好調(10) | ⚪妥当(3.0) | PASS | 3900.0 | 39.0万円 | reversal 3900.0 |  |
| 9519 | レノバ | granville_rebound/未マージPR由来 | - | - | FAIL_INSEN | 940.0 | - | - |  |
| 205A | ロゴスホールディングス（ロゴスＨＤ） | granville_rebound/未マージPR由来 | 🔥絶好調(8) | 💎割安(6.0) | PASS | 1691.0 | 16.9万円 | reversal 1691.0 |  |
| 5989 | エイチワン | granville_rebound/未マージPR由来 | ⚠減速(1) | ⚪妥当(3.0) | PASS | 1510.0 | 15.1万円 | reversal 1510.0 | ⚠業績基調が下向き（⚠減速） |
| 6266 | タツモ | granville_rebound/未マージPR由来 | - | - | FAIL_UWAHIGE | 4020.0 | - | - |  |
| 6284 | Nissei ASB Machine Co., Ltd. | changepoint/granville_oshime/変化点🔔 | - | - | FAIL_UWAHIGE | 9420.0 | - | - |  |
| 3968 | セグエグループ | granville_tenkan | 🔥絶好調(9) | ⚪妥当(4.0) | PASS | 648.0 | 6.5万円 | momentum 655.0 | 抵抗圏(60日高値98%以上) |
| 4765 | SBIグローバルアセットマネジメント | granville_tenkan | 判定保留 | 判定不能 | PASS | 618.0 | 6.2万円 | momentum 619.0 |  |
| 8919 | カチタス | granville_tenkan | ⚡好調(6) | 🔴過熱(1.0) | PASS | 3570.0 | 35.7万円 | momentum 3576.0 |  |
| 7744 | ノーリツ鋼機 | granville_tenkan | - | - | FAIL_UWAHIGE | 2168.0 | - | - | 抵抗圏(60日高値98%以上) ⚡材料後出し |
| 3765 | ガンホー・オンライン・エンターテイメント | granville_tenkan | 取得不可 | 判定不能 | PASS | 2448.0 | 24.5万円 | momentum 2453.0 |  |
| 2702 | 日本マクドナルド HD | granville_tenkan | - | - | FAIL_INSEN | 7800.0 | - | - |  |
| 8086 | ニプロ | granville_tenkan | 🔥絶好調(8) | ⚪妥当(4.0) | PASS | 1595.0 | 15.9万円 | momentum 1599.5 |  |
| 8057 | 内田洋行 | granville_tenkan | ⚡好調(6) | 💎割安(6.0) | PASS | 2185.0 | 21.9万円 | momentum 2189.0 |  |
| 6023 | ダイハツインフィニアース | granville_tenkan | - | - | FAIL_UWAHIGE | 2974.0 | - | - |  |
| 7184 | 富山第一銀行 | granville_oshime | - | - | FAIL_UWAHIGE | 3310.0 | - | - | 抵抗圏(60日高値98%以上) |
| 5384 | フジミインコーポレーテッド | granville_oshime | - | - | FAIL_INSEN | 4045.0 | - | - |  |
| 6925 | ウシオ電機 | granville_oshime | - | - | FAIL_INSEN | 4324.0 | - | - |  |
| 7182 | ゆうちょ銀行 | granville_rebound | - | - | FAIL_UWAHIGE | 3275.0 | - | - |  |
| 4392 | FIG | granville_rebound | 🔥絶好調(8) | 🟡やや割高(2.0) | PASS | 1050.0 | 10.5万円 | reversal 1050.0 |  |
| 3393 | スターティア HD | granville_rebound | - | - | FAIL_UWAHIGE | 3030.0 | - | - |  |
| 2483 | 翻訳センター | granville_rebound | ➖横ばい(2) | 🟡やや割高(2.0) | PASS | 2207.0 | 22.1万円 | reversal 2207.0 |  |
| 150A | JSH | granville_rebound | 🔥絶好調(9) | ⚪妥当(3.0) | PASS | 619.0 | 6.2万円 | reversal 619.0 | ストップ高 |
| 2874 | 横浜冷凍 | granville_oshime/granville_rebound | ⚠減速(7) | ⚪妥当(4.0) | PASS | 2110.0 | 21.1万円 | reversal 2110.0 | ⚠業績基調が下向き（⚠減速） |
| 9247 | TRE HD | granville_rebound | - | - | FAIL_INSEN | 2018.0 | - | - |  |
| 5036 | 日本ビジネスシステムズ | granville_tenkan | ✅順調(4) | 🟢値頃(5.0) | PASS | 1612.0 | 16.1万円 | momentum 1618.0 |  |
| 5020 | ＥＮＥＯＳホールディングス | granville_tenkan | - | - | FAIL_UWAHIGE | 1291.0 | - | - |  |
| 3048 | BIC Cameras Inc. | granville_oshime/granville_tenkan | - | - | FAIL_UWAHIGE | 1727.5 | - | - |  |
| 208A | 構造計画研究所ホールディングス | granville_tenkan | ✅順調(4) | 💎割安(6.0) | PASS | 3035.0 | 30.4万円 | momentum 3036.0 |  |
| 9041 | 近鉄グループホールディングス | granville_tenkan | ✅順調(3) | 🔴過熱(1.0) | PASS | 3555.0 | 35.5万円 | momentum 3568.0 |  |
| 5302 | 日本カーボン | granville_tenkan | - | - | FAIL_INSEN | 5060.0 | - | - | 抵抗圏(60日高値98%以上) |
| 166A | タスキホールディングス | granville_oshime | - | - | FAIL_INSEN | 1145.0 | - | - |  |
| 4415 | ブロードエンタープライズ | granville_oshime | 業績データ取得不可 | ⚪妥当(3.0) | PASS | 1387.0 | 13.9万円 | oshime 1368.0 |  |
| 8544 | 京葉銀行 | granville_oshime | - | - | FAIL_INSEN | 2788.0 | - | - |  |
| 8923 | Tosei Corporation | granville_oshime | ⚡好調(5) | ⚪妥当(4.0) | PASS | 1795.0 | 17.9万円 | oshime 1787.8 |  |
| 7981 | タカラスタンダード | granville_oshime | ⚠減速(1) | 🟡やや割高(2.0) | PASS | 3075.0 | 30.8万円 | ⛔型不一致: 既に支持帯以下 | ⚠業績基調が下向き（⚠減速） |
| 9941 | 太洋物産 | granville_rebound | ⚡好調(7) | 🟢値頃(5.0) | PASS | 1202.0 | 12.0万円 | reversal 1202.0 |  |
| 6703 | 沖電気工業 | granville_rebound | - | - | FAIL_UWAHIGE | 2986.0 | - | - |  |
| 7505 | 扶桑電通 | granville_rebound | ⚡好調(5) | ⚪妥当(4.0) | PASS | 2109.0 | 21.1万円 | reversal 2109.0 |  |
| 4972 | 綜研化学 | granville_rebound | - | - | FAIL_UWAHIGE | 3345.0 | - | - |  |
| 9319 | 中央倉庫 | granville_rebound | ⚡好調(5) | 🟡やや割高(2.0) | PASS | 1890.0 | 18.9万円 | reversal 1890.0 | 抵抗圏(60日高値98%以上) |
| 9502 | 中部電力 | granville_rebound | 🔻悪化(1) | 🟡やや割高(2.0) | PASS | 2818.0 | 28.2万円 | reversal 2818.0 | ⚠業績基調が下向き（🔻悪化） |
| 6305 | Hitachi Construction Machinery Co., Ltd. | granville_tenkan | - | - | FAIL_INSEN | 5556.0 | - | - |  |
| 9503 | 関西電力 | granville_tenkan | 🔻悪化(2) | ⚪妥当(3.0) | PASS | 2401.0 | 24.0万円 | momentum 2409.0 | ⚠業績基調が下向き（🔻悪化） |
| 2317 | システナ | granville_tenkan | ⚠減速(1) | ⚪妥当(3.0) | PASS | 438.0 | 4.4万円 | momentum 442.0 | ⚠業績基調が下向き（⚠減速） |
| 2975 | スターマイカ | granville_tenkan | - | - | FAIL_INSEN | 1585.0 | - | - | 抵抗圏(60日高値98%以上) |
| 7860 | エイベックス | granville_oshime | 業績データ取得不可 | 判定不能 | PASS | 1242.0 | 12.4万円 | ⛔型不一致: 既に支持帯以下 |  |
| 7888 | 三光合成 | granville_oshime | - | - | FAIL_UWAHIGE | 931.0 | - | - |  |
| 2810 | House Foods Group Inc. | granville_oshime | ⚠減速(1) | 🔴過熱(1.0) | PASS | 3790.0 | 37.9万円 | ⛔型不一致: 既に支持帯以下 | ⚠業績基調が下向き（⚠減速） |
| 6638 | ミマキエンジニアリング | granville_oshime | - | - | FAIL_UWAHIGE | 2002.0 | - | - |  |
| 6380 | オリエンタルチエン工業 | granville_rebound | ⚡好調(6) | ⚪妥当(4.0) | PASS_DOJI | 3635.0 | 36.4万円 | reversal 3635.0 |  |
| 3544 | サツドラＨＤ | granville_rebound | - | - | FAIL_UWAHIGE | 1249.0 | - | - |  |
| 3863 | 日本製紙 | granville_rebound | - | - | FAIL_UWAHIGE | 1420.0 | - | - |  |
| 1860 | 戸田建設 | granville_rebound | ✅順調(3) | 🟡やや割高(2.0) | PASS | 1487.0 | 14.9万円 | reversal 1487.0 |  |
| 5998 | アドバネクス | granville_rebound | - | - | FAIL_UWAHIGE | 2381.0 | - | - |  |
| 1605 | Inpex Corporation | granville_tenkan | ⚠減速(2) | －未評価（次回①-9で算定） | PASS | 3782.0 | - | ⛔提案なし(単元株数不明でリスク計算不可) | ⚠業績基調が下向き（⚠減速） |
| 160A | As Partners CO.,LTD. | granville_tenkan | - | - | FAIL_UWAHIGE | 2123.0 | - | - | 抵抗圏(60日高値98%以上) ⚡材料後出し |
| 2217 | Morozoff Limited | granville_rebound | 🔻悪化(2) | －未評価（次回①-9で算定） | PASS | 1525.0 | - | ⛔提案なし(単元株数不明でリスク計算不可) | ⚠業績基調が下向き（🔻悪化） (質注意) |
| 2292 | S Foods Inc. | granville_tenkan | ➖横ばい(2) | －未評価（次回①-9で算定） | PASS | 2785.0 | - | ⛔提案なし(単元株数不明でリスク計算不可) | (質注意) |
| 3623 | Billing System Corporation | granville_tenkan | - | - | FAIL_INSEN | 1034.0 | - | - |  |
| 6333 | TEIKOKU Corp. | granville_oshime | ⚠減速(1) | －未評価（次回①-9で算定） | PASS | 3210.0 | - | ⛔提案なし(単元株数不明でリスク計算不可) | ⚠業績基調が下向き（⚠減速） (質注意) |
| 6571 | QB Net Holdings Co., Ltd. | granville_tenkan | ⚡好調(5) | －未評価（次回①-9で算定） | PASS | 1291.0 | - | ⛔提案なし(単元株数不明でリスク計算不可) |  |
| 7120 | SHINKO Inc. | granville_rebound | - | - | FAIL_INSEN | 976.0 | - | - | 抵抗圏(60日高値98%以上) |
| 7419 | Nojima Co.,Ltd. | granville_rebound | - | - | FAIL_UWAHIGE | 1318.0 | - | - |  |
| 9301 | Mitsubishi Logistics Corporation | granville_rebound | ⚠減速(1) | －未評価（次回①-9で算定） | PASS | 1501.5 | - | ⛔提案なし(単元株数不明でリスク計算不可) | ⚠業績基調が下向き（⚠減速） (質注意) |


## 変化点銘柄（changepoint由来のみ）

| コード | 名前 | signal | 判定 | 終値 | 提案 | チップ |
|---|---|---|---|---|---|---|
| 4483 | JMDC Inc. | 変化点🔔🔔 | FAIL_UWAHIGE | 3470.0 | - | 抵抗圏(60日高値98%以上) |
| 9343 | ibis inc. | changepoint/変化点🔔🔔/未マージPR由来 | FAIL_UWAHIGE | 760.0 | - |  |
| 6080 | M&A Capital Partners Co.,Ltd. | 変化点🔔🔔 | FAIL_UWAHIGE | 4085.0 | - | 抵抗圏(60日高値98%以上) |
| 4498 | サイバートラスト | changepoint/changepoint🔔🔔/変化点🔔🔔 | FAIL_UWAHIGE | 1313.0 | - | 抵抗圏(60日高値98%以上) |
| 4375 | Safie Inc. | changepoint/変化点🔔/未マージPR由来 | FAIL_UWAHIGE | 655.0 | - |  |
| 9888 | UEX, Ltd. | 変化点🔔🔔 | FAIL_UWAHIGE | 1284.0 | - | 抵抗圏(60日高値98%以上) |
| 3923 | ラクス | 変化点🔔 | PASS | 1175.0 | ⛔提案なし(材料後出し) | 抵抗圏(60日高値98%以上) ⚡材料後出し |
| 3994 | マネーフォワード | 変化点🔔 | FAIL_UWAHIGE | 6479.0 | - | 抵抗圏(60日高値98%以上) |
| 4478 | フリー | changepoint🔔🔔/変化点🔔🔔 | PASS | 3345.0 | changepoint 3345.0 | 抵抗圏(60日高値98%以上) 🔒実弾封印中(PL3紙ログ収集中) |
| 265A | HMCOMM | 変化点🔔 | FAIL_UWAHIGE | 716.0 | - | ⚡材料後出し |
| 4441 | トビラシステムズ | changepoint🔔/変化点🔔 | FAIL_INSEN | 1461.0 | - |  |
| 479A | ＰＲＯＮＩ | changepoint🔔/変化点🔔 | PASS | 1734.0 | changepoint 1734.0 | 抵抗圏(60日高値98%以上) 🔒実弾封印中(PL3紙ログ収集中) |
| 584A | ＬｉＮＫＸ | changepoint🔔/変化点🔔 | FAIL_INSEN | 2770.0 | - | ⚡材料後出し |

## ⚡材料後出し

その日の足は開示前の情報。判定は参考値。

- 9211 f-code Inc. | 判定FAIL_UWAHIGE(参考・否定件数に含めず) | 📊決算発表: 上期最終が35％増益で着地・4-6月期も27..
- 3989 シェアリングテクノロジー | 判定FAIL_UWAHIGE(参考・否定件数に含めず) | 📊決算発表: 10-6月期(3Q累計)最終が2.1倍増益で着地..
- 7685 ＢＵＹＳＥＬＬ　ＴＥＣＨＮＯＬＯＧＩＥＳ | 判定FAIL_INSEN(参考・否定件数に含めず) | 📢上方修正: 今期最終を4％上方修正・最高益予想を上..
- 5027 AnyMind Group Inc. | 判定FAIL_UWAHIGE(参考・否定件数に含めず) | 📊決算発表: 上期最終が3.1倍増益で着地・4-6月期も2...
- 9552 Quants Research Institute Holdings, Inc. | 判定FAIL_INSEN(参考・否定件数に含めず) | 📊決算発表: 10-6月期(3Q累計)最終が46％増益で着地・..
- 6071 ＩＢＪ | 判定FAIL_INSEN(参考・否定件数に含めず) | 📢上方修正: 今期経常を15％上方修正・最高益予想を上..
- 6562 Geniee, Inc. | 判定PASS(参考) | 📊決算発表: 4-6月期(1Q)最終は赤字転落で着地 | order_status: ⛔提案なし(材料後出し)
- 254A ＡＩフュージョンキャピタルグループ（ＡＩＦＣＧ） | 判定FAIL_UWAHIGE(参考・否定件数に含めず) | 📊決算発表: 4-6月期(1Q)最終は赤字拡大で着地
- 7744 ノーリツ鋼機 | 判定FAIL_UWAHIGE(参考・否定件数に含めず) | 📊決算発表: 上期最終は71％増益で上振れ着地
- 3923 ラクス | 判定PASS(参考) | 📊決算発表: 4-6月期(1Q)経常は33％増益で着地 | order_status: ⛔提案なし(材料後出し)
- 265A HMCOMM | 判定FAIL_UWAHIGE(参考・否定件数に含めず) | 📢上方修正: 今期経常を2.2倍上方修正
- 584A ＬｉＮＫＸ | 判定FAIL_INSEN(参考・否定件数に含めず) | 📌その他重要開示: 今期経常は63％増で5期連続最高益更新へ
- 160A As Partners CO.,LTD. | 判定FAIL_UWAHIGE(参考・否定件数に含めず) | 📊決算発表: 4-6月期(1Q)経常は74％減益で着地

## 📢開示

使用した一覧URL: https://kabutan.jp/warning/?mode=4_2 （08/14 取引時間中・5頁/69件） / https://kabutan.jp/warning/?mode=4_3 （08/14 取引終了後・21頁/314件） / https://kabutan.jp/warning/?mode=4_4 （市場速報 15:30以降・1頁/14件）。フォールバックなし（一覧取得に成功）。

保有銘柄の下方修正: 該当なし。

- 7120 ＳＨＩＮＫＯ | 📊決算発表 | 4-6月期(1Q)経常は赤字拡大で着地 | 判定FAIL_INSEN
- 2874 ヨコレイ | 📢上方修正 | 今期最終を31％上方修正・最高益予想を上.. | 判定PASS
- 9211 エフ・コード | 📊決算発表 | 上期最終が35％増益で着地・4-6月期も27.. | 判定FAIL_UWAHIGE(参考・材料後出し)
- 254A ＡＩＦＣＧ | 📊決算発表 | 4-6月期(1Q)最終は赤字拡大で着地 | 判定FAIL_UWAHIGE(参考・材料後出し)
- 265A Ｈｍｃｏｍｍ | 📢上方修正 | 今期経常を2.2倍上方修正 | 判定FAIL_UWAHIGE(参考・材料後出し)
- 160A アズパートナ | 📊決算発表 | 4-6月期(1Q)経常は74％減益で着地 | 判定FAIL_UWAHIGE(参考・材料後出し)
- 5027 エニマインド | 📊決算発表 | 上期最終が3.1倍増益で着地・4-6月期も2... | 判定FAIL_UWAHIGE(参考・材料後出し)
- 9552 クオンツ総研 | 📊決算発表 | 10-6月期(3Q累計)最終が46％増益で着地・.. | 判定FAIL_INSEN(参考・材料後出し)
- 3923 ラクス | 📊決算発表 | 4-6月期(1Q)経常は33％増益で着地 | 判定PASS(参考・材料後出し)
- 6562 ジーニー | 📊決算発表 | 4-6月期(1Q)最終は赤字転落で着地 | 判定PASS(参考・材料後出し)
- 3989 シェアテク | 📊決算発表 | 10-6月期(3Q累計)最終が2.1倍増益で着地.. | 判定FAIL_UWAHIGE(参考・材料後出し)
- 7685 バイセル | 📢上方修正 | 今期最終を4％上方修正・最高益予想を上.. | 判定FAIL_INSEN(参考・材料後出し)
- 584A ＬｉＮＫＸ | 📌その他重要開示 | 今期経常は63％増で5期連続最高益更新へ | 判定FAIL_INSEN(参考・材料後出し)
- 6071 ＩＢＪ | 📢上方修正 | 今期経常を15％上方修正・最高益予想を上.. | 判定FAIL_INSEN(参考・材料後出し)
- 7744 ノーリツ鋼機 | 📊決算発表 | 上期最終は71％増益で上振れ着地 | 判定FAIL_UWAHIGE(参考・材料後出し)

①-9へ引き渡し: 12件（PASS/保有以外のFAIL/SKIP銘柄の開示検出分）

## 総当りゲート

プール全225銘柄（method 78 / granville 134 / changepoint 13）。branch_type→判定でグループ化。

| コード | 名前 | branch_type | 判定 | 終値 | 上髭比率 |
|---|---|---|---|---|---|
| 135A | VRAIN Solution,Inc. | method | PASS | 4120.0 | 0.087 |
| 1435 | robot home Inc. | method | PASS | 178.0 | 0.1111 |
| 212A | FIT EASY Inc. | method | PASS | 3075.0 | 0.1667 |
| 276A | CCReB Advisors Inc. | method | PASS | 3540.0 | 0.069 |
| 2980 | SRE Holdings Corp. | method | PASS | 2597.0 | 0.2437 |
| 3036 | アルコニックス（アルコニクス） | method | PASS | 3755.0 | 0.1429 |
| 325A | TENTIAL, Inc. | method | PASS | 1585.0 | 0.1875 |
| 3915 | TerraSky Co., Ltd. | method | PASS | 2424.0 | 0.1379 |
| 4165 | PLAID Inc. | method | PASS | 683.0 | 0.0805 |
| 4249 | 森六 | method | PASS | 2935.0 | 0.0556 |
| 456A | ＨＵＭＡＮ　ＭＡＤＥ | method | PASS | 1429.0 | 0.0 |
| 5574 | ABEJA,Inc. | method | PASS | 3030.0 | 0.0615 |
| 5724 | Asaka Riken Co., Ltd. | method | PASS | 3000.0 | 0.1376 |
| 5757 | CK San-Etsu Co., Ltd. | method | PASS | 5100.0 | 0.2353 |
| 5892 | yutori,Inc. | method | PASS | 2534.0 | 0.0272 |
| 6135 | 牧野フライス製作所 | method | PASS | 15350.0 | 0.2105 |
| 6562 | Geniee, Inc. | method | PASS | 1105.0 | 0.1351 |
| 7047 | PORT INC. | method | PASS | 2256.0 | 0.2288 |
| 7089 | For Startups, Inc. | method | PASS | 1600.0 | 0.06 |
| 7730 | マニー | method | PASS | 1620.0 | 0.0323 |
| 8084 | ＲＹＯＤＥＮ | method | PASS | 4680.0 | 0.0 |
| 8927 | Meiho Enterprise Co., Ltd. | method | PASS | 477.0 | 0.1429 |
| 9302 | 三井倉庫ホールディングス | method | PASS | 3385.0 | 0.1786 |
| 9341 | GENOVA Inc. | method | PASS | 616.0 | 0.1111 |
| 9533 | 東邦瓦斯 | method | PASS | 1175.0 | 0.2432 |
| 9962 | ミスミグループ本社 | method | PASS | 3831.0 | 0.0 |
| 147A | ソラコム | method | FAIL_UWAHIGE | 1077.0 | 0.493 |
| 1975 | 朝日工業社 | method | FAIL_UWAHIGE | 3835.0 | 0.7222 |
| 1979 | Taikisha Ltd. | method | FAIL_UWAHIGE | 4080.0 | 0.2667 |
| 1980 | ダイダン | method | FAIL_UWAHIGE | 2770.0 | 0.4868 |
| 3131 | シンデンハイ | method | FAIL_UWAHIGE | 6880.0 | 0.1548 |
| 341A | TOYOKOH Inc. | method | FAIL_UWAHIGE | 1977.0 | 0.6515 |
| 3798 | ULS Group Incorporated | method | FAIL_UWAHIGE | 525.0 | 0.2917 |
| 4058 | Toyokumo, Inc. | method | FAIL_UWAHIGE | 2382.0 | 0.5556 |
| 4377 | ONE CAREER Inc. | method | FAIL_UWAHIGE | 2557.0 | 0.203 |
| 4477 | BASE, Inc. | method | FAIL_UWAHIGE | 290.0 | 0.4444 |
| 4894 | Cuorips Inc. | method | FAIL_UWAHIGE | 5400.0 | 0.2174 |
| 5027 | AnyMind Group Inc. | method | FAIL_UWAHIGE | 623.0 | 0.4 |
| 5243 | note inc. | method | FAIL_UWAHIGE | 2560.0 | 0.3571 |
| 543A | ＡＲＣＨＩＯＮ | method | FAIL_UWAHIGE | 276.0 | 0.3 |
| 6134 | ＦＵＪＩ | method | FAIL_UWAHIGE | 8290.0 | 0.645 |
| 6632 | ＪＶＣケンウッド | method | FAIL_UWAHIGE | 1044.0 | 0.5273 |
| 6785 | Suzuki Co., Ltd. | method | FAIL_UWAHIGE | 3065.0 | 0.5 |
| 7318 | SERENDIP HOLDINGS Co. Ltd. | method | FAIL_UWAHIGE | 1476.0 | 0.2987 |
| 7433 | 伯東 | method | FAIL_UWAHIGE | 5280.0 | 0.3333 |
| 7480 | スズデン | method | FAIL_UWAHIGE | 3410.0 | 0.3478 |
| 7637 | 白銅 | method | FAIL_UWAHIGE | 3970.0 | 0.4035 |
| 7731 | ニコン | method | FAIL_UWAHIGE | 2045.5 | 0.2617 |
| 8366 | 滋賀銀行 | method | FAIL_UWAHIGE | 2775.0 | 0.4384 |
| 9211 | f-code Inc. | method | FAIL_UWAHIGE | 1584.0 | 0.3956 |
| 9270 | Valuence Holdings, Inc. | method | FAIL_UWAHIGE | 2059.0 | 0.2857 |
| 9308 | 乾汽船 | method | FAIL_UWAHIGE | 2059.0 | 0.1837 |
| 146A | Columbia Works Inc. | method | FAIL_INSEN | 3870.0 | 0.2069 |
| 1960 | サンテック | method | FAIL_INSEN | 1694.0 | 0.0 |
| 262A | INTERMESTIC INC. | method | FAIL_INSEN | 1926.0 | 0.3469 |
| 3091 | ブロンコビリー | method | FAIL_INSEN | 2619.0 | 0.6094 |
| 3374 | 内外テック | method | FAIL_INSEN | 4455.0 | 0.55 |
| 3441 | Sanno Co., Ltd. | method | FAIL_INSEN | 2739.0 | 0.0943 |
| 3723 | Nihon Falcom Corporation | method | FAIL_INSEN | 2903.0 | 0.6667 |
| 4516 | 日本新薬 | method | FAIL_INSEN | 3640.0 | 0.6067 |
| 4536 | 参天製薬 | method | FAIL_INSEN | 1918.5 | 0.2385 |
| 4599 | ステムリム | method | FAIL_INSEN | 348.0 | 0.2857 |
| 5254 | Arent, Inc. | method | FAIL_INSEN | 4305.0 | 0.6111 |
| 5301 | 東海カーボン | method | FAIL_INSEN | 1797.0 | 0.6573 |
| 5537 | AlbaLink Co.,Ltd. | method | FAIL_INSEN | 2720.0 | 0.4554 |
| 5586 | Laboro.AI, Inc. | method | FAIL_INSEN | 902.0 | 0.3191 |
| 5590 | NETSTARS Co.,Ltd. | method | FAIL_INSEN | 674.0 | 0.0 |
| 6324 | ハーモニック・ドライブ・システムズ（ハーモニック） | method | FAIL_INSEN | 6510.0 | 0.2745 |
| 6490 | ＰＩＬＬＡＲ | method | FAIL_INSEN | 10180.0 | 0.25 |
| 6492 | Okano Valve Mfg. Co., Ltd. | method | FAIL_INSEN | 15310.0 | 0.1475 |
| 6857 | アドバンテスト | method | FAIL_INSEN | 36870.0 | 0.161 |
| 7267 | ホンダ | method | FAIL_INSEN | 1658.0 | 0.253 |
| 7409 | AeroEdge Co.,Ltd | method | FAIL_INSEN | 1683.0 | 0.3756 |
| 7685 | ＢＵＹＳＥＬＬ　ＴＥＣＨＮＯＬＯＧＩＥＳ | method | FAIL_INSEN | 3165.0 | 0.1364 |
| 8388 | 阿波銀行 | method | FAIL_INSEN | 9320.0 | 0.5758 |
| 8697 | 日本取引所グループ | method | FAIL_INSEN | 2244.0 | 0.2119 |
| 9072 | ニッコンホールディングス | method | FAIL_INSEN | 5386.0 | 0.4194 |
| 9552 | Quants Research Institute Holdings, Inc. | method | FAIL_INSEN | 997.0 | 0.0385 |
| 150A | JSH | granville | PASS | 619.0 | 0.0 |
| 1605 | Inpex Corporation | granville | PASS | 3782.0 | 0.0547 |
| 1860 | 戸田建設 | granville | PASS | 1487.0 | 0.2308 |
| 1898 | 世紀東急工業 | granville | PASS | 1495.0 | 0.0 |
| 205A | ロゴスホールディングス（ロゴスＨＤ） | granville | PASS | 1691.0 | 0.0769 |
| 208A | 構造計画研究所ホールディングス | granville | PASS | 3035.0 | 0.0 |
| 2175 | エス・エム・エス | granville | PASS | 2353.0 | 0.0879 |
| 2217 | Morozoff Limited | granville | PASS | 1525.0 | 0.2174 |
| 2292 | S Foods Inc. | granville | PASS | 2785.0 | 0.0 |
| 2317 | システナ | granville | PASS | 438.0 | 0.2308 |
| 2483 | 翻訳センター | granville | PASS | 2207.0 | 0.0 |
| 2602 | 日清オイリオグループ | granville | PASS | 2016.0 | 0.04 |
| 2659 | サンエー | granville | PASS | 3330.0 | 0.0 |
| 2810 | House Foods Group Inc. | granville | PASS | 3790.0 | 0.2407 |
| 2874 | 横浜冷凍 | granville | PASS | 2110.0 | 0.219 |
| 3151 | バイタルケーエスケー・ホールディングス（バイタルＫＳ） | granville | PASS | 1614.0 | 0.0 |
| 3491 | ＧＡ　ｔｅｃｈｎｏｌｏｇｉｅｓ | granville | PASS | 1531.0 | 0.0 |
| 3765 | ガンホー・オンライン・エンターテイメント | granville | PASS | 2448.0 | 0.093 |
| 3968 | セグエグループ | granville | PASS | 648.0 | 0.1304 |
| 3993 | PKSHA Technology Inc. | granville | PASS | 3170.0 | 0.0298 |
| 421A | ムービン・ストラテジック・キャリア（ムービン） | granville | PASS | 3900.0 | 0.1304 |
| 4392 | FIG | granville | PASS | 1050.0 | 0.0 |
| 4415 | ブロードエンタープライズ | granville | PASS | 1387.0 | 0.025 |
| 4419 | Ｆｉｎａｔｅｘｔホールディングス | granville | PASS | 1394.0 | 0.0119 |
| 4420 | イーソル | granville | PASS | 737.0 | 0.0 |
| 4765 | SBIグローバルアセットマネジメント | granville | PASS | 618.0 | 0.0 |
| 4826 | ＣＩＪ | granville | PASS | 537.0 | 0.1429 |
| 5036 | 日本ビジネスシステムズ | granville | PASS | 1612.0 | 0.0575 |
| 5076 | インフロニアＨＤ | granville | PASS | 2838.0 | 0.005 |
| 5989 | エイチワン | granville | PASS | 1510.0 | 0.0833 |
| 6333 | TEIKOKU Corp. | granville | PASS | 3210.0 | 0.1667 |
| 6571 | QB Net Holdings Co., Ltd. | granville | PASS | 1291.0 | 0.119 |
| 6718 | アイホン | granville | PASS | 2860.0 | 0.1471 |
| 7085 | カーブスホールディングス | granville | PASS | 955.0 | 0.2222 |
| 7231 | トピー工業 | granville | PASS | 3020.0 | 0.0 |
| 7505 | 扶桑電通 | granville | PASS | 2109.0 | 0.0179 |
| 7611 | ハイデイ日高 | granville | PASS | 2914.0 | 0.0926 |
| 7679 | Yakuodo Holdings Co., Ltd. | granville | PASS | 1751.0 | 0.0909 |
| 7860 | エイベックス | granville | PASS | 1242.0 | 0.0 |
| 7981 | タカラスタンダード | granville | PASS | 3075.0 | 0.0 |
| 8008 | ヨンドシーホールディングス（４℃ホールデ） | granville | PASS | 2118.0 | 0.1364 |
| 8056 | ＢＩＰＲＯＧＹ | granville | PASS | 4653.0 | 0.0938 |
| 8057 | 内田洋行 | granville | PASS | 2185.0 | 0.0625 |
| 8081 | カナデン | granville | PASS | 2521.0 | 0.0845 |
| 8086 | ニプロ | granville | PASS | 1595.0 | 0.1458 |
| 8098 | 稲畑産業 | granville | PASS | 4190.0 | 0.0667 |
| 8141 | 新光商事 | granville | PASS | 1570.0 | 0.0 |
| 8242 | エイチ・ツー・オー　リテイリング | granville | PASS | 2867.5 | 0.2276 |
| 8919 | カチタス | granville | PASS | 3570.0 | 0.0667 |
| 8923 | Tosei Corporation | granville | PASS | 1795.0 | 0.1034 |
| 9037 | ハマキョウレックス（ハマキョウ） | granville | PASS | 1889.0 | 0.05 |
| 9041 | 近鉄グループホールディングス | granville | PASS | 3555.0 | 0.1846 |
| 9274 | ＫＰＰグループホールディングス | granville | PASS | 1095.0 | 0.0476 |
| 9301 | Mitsubishi Logistics Corporation | granville | PASS | 1501.5 | 0.0213 |
| 9319 | 中央倉庫 | granville | PASS | 1890.0 | 0.0355 |
| 9502 | 中部電力 | granville | PASS | 2818.0 | 0.0424 |
| 9503 | 関西電力 | granville | PASS | 2401.0 | 0.2222 |
| 9517 | イーレックス | granville | PASS | 866.0 | 0.0 |
| 9854 | 愛眼 | granville | PASS | 293.0 | 0.0 |
| 9882 | Yellow Hat Ltd. | granville | PASS | 1761.0 | 0.0 |
| 9941 | 太洋物産 | granville | PASS | 1202.0 | 0.0513 |
| 6380 | オリエンタルチエン工業 | granville | PASS_DOJI | 3635.0 | 0.6111 |
| 160A | As Partners CO.,LTD. | granville | FAIL_UWAHIGE | 2123.0 | 0.4103 |
| 254A | ＡＩフュージョンキャピタルグループ（ＡＩＦＣＧ） | granville | FAIL_UWAHIGE | 1168.0 | 0.5294 |
| 3048 | BIC Cameras Inc. | granville | FAIL_UWAHIGE | 1727.5 | 0.3091 |
| 3393 | スターティア HD | granville | FAIL_UWAHIGE | 3030.0 | 0.2857 |
| 3544 | サツドラＨＤ | granville | FAIL_UWAHIGE | 1249.0 | 0.75 |
| 3863 | 日本製紙 | granville | FAIL_UWAHIGE | 1420.0 | 0.6774 |
| 3880 | 大王製紙 | granville | FAIL_UWAHIGE | 973.0 | 0.375 |
| 3989 | シェアリングテクノロジー | granville | FAIL_UWAHIGE | 1481.0 | 0.4359 |
| 4413 | baudroie,inc. | granville | FAIL_UWAHIGE | 2843.0 | 0.4589 |
| 4847 | インテリジェント　ウェイブ | granville | FAIL_UWAHIGE | 1281.0 | 0.4737 |
| 4848 | フルキャストホールディングス | granville | FAIL_UWAHIGE | 1856.0 | 0.2647 |
| 4972 | 綜研化学 | granville | FAIL_UWAHIGE | 3345.0 | 0.4 |
| 5020 | ＥＮＥＯＳホールディングス | granville | FAIL_UWAHIGE | 1291.0 | 0.3134 |
| 5189 | 櫻護謨 | granville | FAIL_UWAHIGE | 3825.0 | 0.5205 |
| 5406 | 神戸製鋼所（神戸鋼） | granville | FAIL_UWAHIGE | 1986.0 | 0.3421 |
| 547A | ムニノバホールディングス（ムニノバＨＤ） | granville | FAIL_UWAHIGE | 455.0 | 0.6364 |
| 5932 | Sankyo Tateyama, Inc. | granville | FAIL_UWAHIGE | 670.0 | 0.3125 |
| 5998 | アドバネクス | granville | FAIL_UWAHIGE | 2381.0 | 0.3077 |
| 6023 | ダイハツインフィニアース | granville | FAIL_UWAHIGE | 2974.0 | 0.2951 |
| 6266 | タツモ | granville | FAIL_UWAHIGE | 4020.0 | 0.4857 |
| 6284 | Nissei ASB Machine Co., Ltd. | granville | FAIL_UWAHIGE | 9420.0 | 0.3636 |
| 6638 | ミマキエンジニアリング | granville | FAIL_UWAHIGE | 2002.0 | 0.2581 |
| 6703 | 沖電気工業 | granville | FAIL_UWAHIGE | 2986.0 | 0.4068 |
| 7182 | ゆうちょ銀行 | granville | FAIL_UWAHIGE | 3275.0 | 0.5938 |
| 7184 | 富山第一銀行 | granville | FAIL_UWAHIGE | 3310.0 | 0.64 |
| 7419 | Nojima Co.,Ltd. | granville | FAIL_UWAHIGE | 1318.0 | 0.6667 |
| 7744 | ノーリツ鋼機 | granville | FAIL_UWAHIGE | 2168.0 | 0.3483 |
| 7888 | 三光合成 | granville | FAIL_UWAHIGE | 931.0 | 0.3158 |
| 7970 | 信越ポリマー | granville | FAIL_UWAHIGE | 2330.0 | 0.6471 |
| 8101 | GSI Creos Corporation | granville | FAIL_UWAHIGE | 2690.0 | 0.3478 |
| 8276 | 平和堂 | granville | FAIL_UWAHIGE | 2750.0 | 0.2093 |
| 8361 | 大垣共立銀行 | granville | FAIL_UWAHIGE | 8050.0 | 0.8966 |
| 8367 | 南都銀行 | granville | FAIL_UWAHIGE | 1941.0 | 0.6379 |
| 8628 | 松井証券（松井） | granville | FAIL_UWAHIGE | 1105.0 | 0.6818 |
| 8707 | 岩井コスモホールディングス | granville | FAIL_UWAHIGE | 4430.0 | 0.6875 |
| 8876 | リログループ | granville | FAIL_UWAHIGE | 2161.0 | 0.6923 |
| 9031 | Nishi-Nippon Railroad Co., Ltd. | granville | FAIL_UWAHIGE | 3038.0 | 0.2571 |
| 9101 | 日本郵船 | granville | FAIL_UWAHIGE | 6400.0 | 0.1981 |
| 9147 | ＮＩＰＰＯＮ　ＥＸＰＲＥＳＳ　ホールディングス | granville | FAIL_UWAHIGE | 5684.0 | 0.1607 |
| 9324 | 安田倉庫（安田倉） | granville | FAIL_UWAHIGE | 2560.0 | 0.65 |
| 9627 | アインホールディングス | granville | FAIL_UWAHIGE | 6178.0 | 0.2784 |
| 9869 | 加藤産業 | granville | FAIL_UWAHIGE | 6480.0 | 0.2727 |
| 166A | タスキホールディングス | granville | FAIL_INSEN | 1145.0 | 0.3 |
| 1925 | 大和ハウス工業（大和ハウス） | granville | FAIL_INSEN | 4609.0 | 0.0263 |
| 269A | Sapeet, Inc. | granville | FAIL_INSEN | 2436.0 | 0.2518 |
| 2702 | 日本マクドナルド HD | granville | FAIL_INSEN | 7800.0 | 0.4643 |
| 2975 | スターマイカ | granville | FAIL_INSEN | 1585.0 | 0.5161 |
| 2982 | ＡＤワークスグループ（ＡＤＷＧ） | granville | FAIL_INSEN | 425.0 | 0.3333 |
| 3623 | Billing System Corporation | granville | FAIL_INSEN | 1034.0 | 0.7 |
| 3776 | ブロードバンドタワー | granville | FAIL_INSEN | 250.0 | 0.625 |
| 3865 | 北越コーポレーション（北越コーポ） | granville | FAIL_INSEN | 895.0 | 0.4211 |
| 4063 | 信越化学工業 | granville | FAIL_INSEN | 6372.0 | 0.2041 |
| 4320 | ＣＥホールディングス | granville | FAIL_INSEN | 1648.0 | 1.0 |
| 5302 | 日本カーボン | granville | FAIL_INSEN | 5060.0 | 0.6154 |
| 5384 | フジミインコーポレーテッド | granville | FAIL_INSEN | 4045.0 | 0.25 |
| 6071 | ＩＢＪ | granville | FAIL_INSEN | 841.0 | 0.0 |
| 6305 | Hitachi Construction Machinery Co., Ltd. | granville | FAIL_INSEN | 5556.0 | 0.2222 |
| 6327 | 北川精機 | granville | FAIL_INSEN | 3580.0 | 0.4308 |
| 6590 | 芝浦メカトロニクス | granville | FAIL_INSEN | 4485.0 | 0.4474 |
| 6613 | Ｇ−ＱＤレーザ | granville | FAIL_INSEN | 1806.0 | 0.3043 |
| 6656 | インスペック | granville | FAIL_INSEN | 873.0 | 0.1429 |
| 6925 | ウシオ電機 | granville | FAIL_INSEN | 4324.0 | 0.5333 |
| 7120 | SHINKO Inc. | granville | FAIL_INSEN | 976.0 | 0.3154 |
| 7806 | ＭＴＧ | granville | FAIL_INSEN | 8130.0 | 0.6471 |
| 7956 | ピジョン | granville | FAIL_INSEN | 2113.5 | 0.2698 |
| 8511 | 日本証券金融 | granville | FAIL_INSEN | 2527.0 | 0.7288 |
| 8522 | 名古屋銀行（名古屋銀） | granville | FAIL_INSEN | 6870.0 | 0.5789 |
| 8544 | 京葉銀行 | granville | FAIL_INSEN | 2788.0 | 0.6746 |
| 8570 | イオンフィナンシャルサービス | granville | FAIL_INSEN | 1634.5 | 0.0909 |
| 8844 | Cosmos Initia Co., Ltd. | granville | FAIL_INSEN | 1243.0 | 0.5769 |
| 9247 | TRE HD | granville | FAIL_INSEN | 2018.0 | 0.4143 |
| 9519 | レノバ | granville | FAIL_INSEN | 940.0 | 0.5152 |
| 3923 | ラクス | changepoint | PASS | 1175.0 | 0.1103 |
| 4478 | フリー | changepoint | PASS | 3345.0 | 0.0 |
| 479A | ＰＲＯＮＩ | changepoint | PASS | 1734.0 | 0.0204 |
| 265A | HMCOMM | changepoint | FAIL_UWAHIGE | 716.0 | 0.3617 |
| 3994 | マネーフォワード | changepoint | FAIL_UWAHIGE | 6479.0 | 0.1648 |
| 4375 | Safie Inc. | changepoint | FAIL_UWAHIGE | 655.0 | 0.2703 |
| 4483 | JMDC Inc. | changepoint | FAIL_UWAHIGE | 3470.0 | 0.4706 |
| 4498 | サイバートラスト | changepoint | FAIL_UWAHIGE | 1313.0 | 0.2308 |
| 6080 | M&A Capital Partners Co.,Ltd. | changepoint | FAIL_UWAHIGE | 4085.0 | 0.381 |
| 9343 | ibis inc. | changepoint | FAIL_UWAHIGE | 760.0 | 0.3529 |
| 9888 | UEX, Ltd. | changepoint | FAIL_UWAHIGE | 1284.0 | 0.2727 |
| 4441 | トビラシステムズ | changepoint | FAIL_INSEN | 1461.0 | 0.9474 |
| 584A | ＬｉＮＫＸ | changepoint | FAIL_INSEN | 2770.0 | 0.5091 |

**除籍リスト**: 該当なし（first_seenから30暦日超の銘柄なし）

## 機械詳細

- 検知内訳: PASS 90 / PASS_DOJI 1 / FAIL_UWAHIGE 77 / FAIL_INSEN 59 / SKIP 0（※STEP2で全225銘柄base_day足取得成功、SKIPなし）
- スキップ件数: Yahoo取得失敗0件・kabutan finance取得失敗0件・kabutan top取得失敗0件
- log追記件数: night_gate.log に2026-08-14分を追加（既存30営業日分から古い分を除去し最新30営業日を保持）
- ヘッドライン省略件数: 91件中12件のみヘッドライン生成（手法スコア降順・13件目以降79件は省略）
- gate_history書き込み結果: gate_history/2026-08-14.json を新規作成（既存なし）
- STEP4.8週末ブリーフ: 実行（week_open=true）
- master.json変更行数: +4646/-3578（検出indent幅=1・上限5,000行以内=はい）
- gyoseki再計算: 10件（未キャッシュ7: 1605/2217/2292/6333/6571/7679/9301、開示強制3: 2874/3923/6562）。うち3923は事業譲渡による変則決算のため判定保留
- valuation計算: PASS 91件中84件で静的キャッシュを再利用し動的値頃感を再計算。7件(1605/2217/2292/6333/6571/7679/9301)は静的層未取得のため「－未評価（次回①-9で算定）」
- 次回決算日: kabutan上で個別銘柄の確定next決算日を取得できる情報源が見当たらず、対象96銘柄すべて⚠日程不明として記録（推定値は使用していない）
