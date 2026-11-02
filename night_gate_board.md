# 夜間ゲート 2026-11-02

## サマリー
- 評価数: 470 / PASS: 83（PASS_DOJI 10件を含む）
- 発注可能提案数: 60件
- 市場一言: 市場モード「弱気」（market.latest 2026-11-02）。プール469銘柄中PASS比率17.7%（陰線FAIL 244件・上髭FAIL 143件）
- 実行モード: 通常（base_day=当日の引け値を対象）
- base_day: 2026-11-02（run_at 2026-11-02 20:46起動）
- week_open: false（翌営業日 11/04(水)。11/03は祝日）→ STEP 4.8 週末ブリーフはスキップ
- 📆 翌営業日 11/04(水): カレンダーイベントなし（T+2 11/05(木): カレンダーイベントなし。次の TOPIX 低減日 01/29 は10営業日超先）
- 📑指数: 低減対象 提案6件／PASS12件／プール68件・新規採用 0件（index_flags 2026-10-07 公表分・組入は10/30に実施済み）

## 検証結果
- V1 → はい（proposals60=results60=template60）
- V2 → はい（PASS83=提案60+除外23・order_status欠落0）
- V3 → はい（results470件重複0）
- V4 → はい（既存 valuation static 変更0）
- V5 → はい（許可キー外の変更 top[] ng[] pipeline[]）
- V6 → はい（grade絵文字不整合0（gyoseki_cache は今夜未変更））
- V9 → はい（gate_history と today 一致）
- V10 → はい（base_day 4箇所一致 2026-11-02）
- V12 → はい（results・proposals・template 同順（STEP5.2(1)）True）
- V13 → はい（1009銘柄/571.5KiB・キー欠落0・nx不一致0）
- V14 → はい（method_score 保持72件/null398件・出所不明0）
- V15 → はい（PASS83件中83件に付与（欠落0・要確認0））
- V16 → はい（earnings_log総数157・本夜追記5・grade_beforeは再計算前（今夜は再計算なし）・history<=4 True）
- V17 → はい（470銘柄/402.6KiB・保有5銘柄すべて収録・3日ルール判定5銘柄）
- V18 → はい（鮮度切れ14件・誤除外0）
- V19 → はい（verdicts470=評価470・nominations105（新規30/再指名75）・pool last_seen集合一致True）
- V20 → はい（1009銘柄・nx非null665・hist持ち496・pxd361・取得元名称なし）
- V7 → はい（必須セクション存在・week_open=false のため今週のカタリストは対象外）
- V8 → はい（模擬60行 不正0）
- V11 → いいえ（+12463/-13583（indent=2・往復一致）＝results470件全置換＋キャッシュ更新による実変更で全体再フォーマットではない（往復一致を検証済み）。5,000行を超過（前夜と同様の構造））
- VLEAK → はい（公開物への保有情報 検出0件。保有5銘柄・アラート詳細は通知のみ）

## 保有アラート
保有5銘柄・アラート13件（詳細は通知）

## 前夜の結果
PL5口座への正式な反映は週次①-11の採点で行われる。ここは参考情報。
前夜2026-10-30の提案25件 → 約定18・不約定7・判定不能0
- 4743 momentum 指値/トリガー1,608 → 約定1,608（終値1,584 含み-1.49%）
- 8276 reversal 2,597 → 不約定（H2,631/L2,605）
- 9974 reversal 指値/トリガー6,500 → 約定6,480（終値6,520 含み+0.62%）
- 8954 reversal 指値/トリガー86,800 → 約定86,800（終値86,500 含み-0.35%）
- 9948 reversal 指値/トリガー3,535 → 約定3,535（終値3,535 含み+0.00%）
- 8194 reversal 2,470 → 不約定（H2,537/L2,471）
- 6810 reversal 指値/トリガー2,265 → 約定2,259（終値2,279 含み+0.89%）
- 3927 momentum 967 → 不約定（H957/L923）
- 8697 momentum 指値/トリガー2,118 → 約定2,118（終値2,101.5 含み-0.78%）
- 4763 momentum 指値/トリガー1,509 → 約定1,509（終値1,498 含み-0.73%）
- 4568 momentum 2,758 → 不約定（H2,892.5/L2,800.5）
- 4848 momentum 1,862 → 不約定（H1,854/L1,826）
- 8113 momentum 指値/トリガー1,013 → 約定1,020（終値1,027 含み+0.69%）
- 2897 momentum 指値/トリガー3,045 → 約定3,051（終値3,050 含み-0.03%）
- 5233 momentum 指値/トリガー4,239 → 約定4,240（終値4,281 含み+0.97%）
- 2811 momentum 2,739.5 → 不約定（H2,790/L2,758）
- 4922 momentum 指値/トリガー6,036 → 約定6,036（終値5,999 含み-0.61%）
- 8167 momentum 指値/トリガー1,381 → 約定1,389（終値1,372 含み-1.22%）
- 7921 momentum 指値/トリガー4,205 → 約定4,205（終値4,205 含み+0.00%）
- 4912 momentum 指値/トリガー1,838 → 約定1,844.5（終値1,838 含み-0.35%）
- 3563 momentum 指値/トリガー5,845 → 約定5,845（終値5,808 含み-0.63%）
- 9536 oshime 2,493.4 → 不約定（H2,868/L2,779）
- 8364 reversal 指値/トリガー2,837 → 約定2,758（終値2,739 含み-0.69%）
- 9697 reversal 指値/トリガー3,957 → 約定3,957（終値3,878 含み-2.00%）
- 4498 changepoint 指値/トリガー2,150 → 約定2,150（終値2,077 含み-3.40%）

## 模擬テンプレ
```
# base_day 2026-11-02 ／ 提案60件
# 使い方: 参戦する0〜3銘柄の行だけをコピーし、｜の後ろに参戦理由を書いてポジション株PJへ送る。
# 選ばなかった行は送らなくてよい（全行に理由を書く必要はない）。見送りは末尾の1行で足りる。
# 特定銘柄を理由つきで見送る場合のみ『模擬 見送り {code} ｜{理由}』を送る。
模擬 3915 kenmo_momentum 逆指値2214 SL2080.2 単元100 ｜
模擬 6652 choruko_reversal 指値3330 SL3305 単元100 ｜
模擬 7995 choruko_reversal 指値6230 SL6070 単元100 ｜
模擬 5333 choruko_reversal 指値5118 SL4573 単元100 ｜
模擬 6302 choruko_reversal 指値5520 SL5053 単元100 ｜
模擬 5101 choruko_reversal 指値6365 SL6160 単元100 ｜
模擬 9072 choruko_reversal 指値4110 SL4006 単元100 ｜
模擬 7731 choruko_reversal 指値1694 SL1624.5 単元100 ｜
模擬 6925 choruko_reversal 指値3243 SL3180 単元100 ｜
模擬 6368 choruko_reversal 指値2229 SL2132 単元100 ｜
模擬 6651 choruko_reversal 指値4135 SL4090 単元100 ｜
模擬 9533 choruko_reversal 指値1286 SL1183 単元100 ｜
模擬 4966 choruko_reversal 指値18350 SL17800 単元100 ｜
模擬 6674 choruko_reversal 指値4636 SL4510 単元100 ｜
模擬 6479 choruko_reversal 指値3145 SL3061 単元100 ｜
模擬 6632 choruko_reversal 指値873 SL859 単元100 ｜
模擬 4980 choruko_reversal 指値2904.5 SL2830 単元100 ｜
模擬 1963 choruko_reversal 指値2122 SL2075.5 単元100 ｜
模擬 5310 choruko_reversal 指値6550 SL6300 単元100 ｜
模擬 7148 choruko_reversal 指値1415 SL1375 単元100 ｜
模擬 6349 choruko_reversal 指値1737 SL1708 単元100 ｜
模擬 3612 choruko_reversal 指値1436 SL1360 単元100 ｜
模擬 8975 choruko_reversal 指値82600 SL80100 単元1 ｜
模擬 5831 choruko_reversal 指値3030 SL2948.5 単元100 ｜
模擬 8304 choruko_reversal 指値2981 SL2903 単元100 ｜
模擬 6810 choruko_reversal 指値2279 SL2150 単元100 ｜
模擬 7186 choruko_reversal 指値1653.5 SL1625 単元100 ｜
模擬 8354 choruko_reversal 指値6865 SL6695 単元100 ｜
模擬 8698 choruko_reversal 指値625 SL614 単元100 ｜
模擬 4187 ai_momentum 逆指値4435 SL4164.2 単元100 ｜
模擬 1975 ai_momentum 逆指値3710 SL3482.7 単元100 ｜
模擬 4971 ai_reversal 指値6020 SL5770 単元100 ｜
模擬 6235 ai_reversal 指値2227 SL2164 単元100 ｜
模擬 7729 ai_reversal 指値15420 SL14640 単元100 ｜
模擬 6752 ai_reversal 指値3740 SL3466 単元100 ｜
模擬 6787 ai_reversal 指値8300 SL8190 単元100 ｜
模擬 4973 ai_reversal 指値4185 SL4065 単元100 ｜
模擬 6590 ai_reversal 指値3115 SL3010 単元100 ｜
模擬 3927 granville_tenkan 逆指値958 SL899.6 単元100 ｜
模擬 9742 granville_tenkan 逆指値2441 SL2293.6 単元100 ｜
模擬 6255 granville_tenkan 逆指値689 SL646.7 単元100 ｜
模擬 3405 granville_tenkan 逆指値1876 SL1762.5 単元100 ｜
模擬 4401 granville_tenkan 逆指値4541 SL4263.8 単元100 ｜
模擬 4617 granville_tenkan 逆指値3540 SL3322.9 単元100 ｜
模擬 4568 granville_tenkan 逆指値2893.5 SL2718.9 単元100 ｜
模擬 6592 granville_tenkan 逆指値1740 SL1634.7 単元100 ｜
模擬 3549 granville_tenkan 逆指値4510 SL4234.7 単元100 ｜
模擬 7734 granville_tenkan 逆指値3480 SL3266.5 単元100 ｜
模擬 5233 granville_tenkan 逆指値4288 SL4026 単元100 ｜
模擬 6196 granville_tenkan 逆指値1714 SL1610.2 単元100 ｜
模擬 6328 granville_tenkan 逆指値2478 SL2328.4 単元100 ｜
模擬 7806 granville_oshime 指値8756 SL8712.4 単元100 ｜
模擬 3793 granville_rebound 指値444 SL428 単元100 ｜
模擬 8084 granville_rebound 指値2217 SL2101 単元100 ｜
模擬 150A granville_rebound 指値575 SL533 単元100 ｜
模擬 6508 granville_rebound 指値8677 SL8280 単元100 ｜
模擬 6490 granville_rebound 指値9960 SL9610 単元100 ｜
模擬 4100 granville_rebound 指値1757 SL1591 単元100 ｜
模擬 7175 granville_rebound 指値1647 SL1610 単元100 ｜
模擬 4478 changepoint 指値4645 SL4055 単元100 🔒 ｜
模擬 見送り ｜
```

## PASS内訳
PASS 83件 = 発注可能 60件 + 除外 23件（型不一致5/材料後出し4/鮮度切れ14/その他0）
- 7276 Koito Manufacturing Co., Ltd.: ⛔提案なし(材料後出し)
- 7278 Exedy Corporation: ⛔提案なし(材料後出し)
- 7220 Musashi Seimitsu Industry Co., Ltd.: ⛔提案なし(材料後出し)
- 6080 Ｍ＆Ａキャピタルパートナーズ: ⛔型不一致: 既に支持帯以下
- 6523 ＰＨＣホールディングス: ⛔型不一致: 既に支持帯以下
- 6340 澁谷工業: ⛔型不一致: 既に支持帯以下
- 9509 Hokkaido Electric Power Company,Incorporated: ⛔型不一致: 既に支持帯以下
- 7630 Ichibanya Co., Ltd.: ⛔型不一致: 既に支持帯以下
- 7480 スズデン: ⛔提案なし(材料後出し)
- 鮮度切れ 14件: 2980(nom_age 15)、6629(nom_age 14)、8282(nom_age 13)、7721(nom_age 11)、9882(nom_age 15)、6183(nom_age 15)、1982(nom_age 14)、9432(nom_age 15)、3935(nom_age 11)、5461(nom_age 11)、4937(nom_age 19)、2681(nom_age 17)、6136(nom_age 13)、6284(nom_age 11)

## 5手法銘柄
- 5137 Smart Drive Co. Ltd.｜kenmo_momentum｜🚀確変｜💎割安｜FAIL_INSEN｜307円｜💰3.1万円｜—
- 276A CCReB Advisors Inc.｜granville_oshime/kenmo_momentum｜🚀確変｜🟢値頃｜FAIL_UWAHIGE｜4,470円｜💰44.1万円｜—｜⚠日程不明｜📌
- 3556 RenetJapanGroup, Inc.｜kenmo_momentum/granville_tenkan｜🚀確変｜🟢値頃｜FAIL_UWAHIGE｜856円｜💰8.5万円｜—
- 4434 Serverworks Co., Ltd.｜kenmo_momentum/stf_kakuhen｜🚀確変｜🟢値頃｜FAIL_UWAHIGE｜2,791円｜💰28.0万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚠日程不明
- 5027 AnyMind Group Inc.｜kenmo_momentum/changepoint🔔｜🚀確変｜⚪妥当｜FAIL_INSEN｜726円｜💰7.5万円｜—
- 4053 Sun Asterisk, Inc.｜kenmo_momentum｜🚀確変｜⚪妥当｜FAIL_INSEN｜565円｜💰5.7万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 5136 tripla Co.,Ltd.｜changepoint/kenmo_momentum/changepoint🔔🔔/granville_oshime｜🚀確変｜⚪妥当｜FAIL_INSEN｜2,471円｜💰24.7万円｜—｜⚠日程不明
- 5757 CK San-Etsu Co., Ltd.｜kenmo_momentum｜🔥絶好調｜💎割安｜FAIL_UWAHIGE｜4,555円｜💰45.5万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 9554 AViC Co. Ltd.｜kenmo_momentum/granville_tenkan｜🔥絶好調｜💎割安｜FAIL_INSEN｜1,465円｜💰15.3万円｜—
- 3915 TerraSky Co., Ltd.｜kenmo_momentum｜🔥絶好調｜🟢値頃｜PASS_DOJI｜2,162円｜💰21.6万円｜提案あり｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚠日程不明｜📐進捗 上振れ +34.1%
  > 【業態】クラウドシステムの導入支援や開発。セールスフォースと提携。大企業、AWS向け拡大。
  > 【いま】終値2,162円・直近5日-6.00%（材料未確認）
  > 【調子】🔥絶好調（10/13）
  > 【水準】🟢値頃（5.0/7）— PER18.29倍・PEG0.3506・52週30.1% ／ 💰単元21.6万円
  > 【戦略】当日高値超えの逆指値2,214円で順張り参戦を検討。上限2,236.1円・SL2,080.2円目安
- 212A FIT EASY Inc.｜kenmo_momentum/granville_oshime｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜2,640円｜💰26.5万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚠日程不明｜⚡材料後出し｜📌
- 421A Movin' Strategic Career CO.,LTD.｜kenmo_momentum/kenmo_newhigh｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜3,655円｜💰37.0万円｜—
- 5132 pluszero,Inc.｜kenmo_momentum｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1,748円｜💰17.8万円｜—｜⚠日程不明
- 4377 ONE CAREER Inc.｜kenmo_momentum/granville_oshime｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜2,425円｜💰24.2万円｜—
- 5537 AlbaLink Co.,Ltd.｜kenmo_momentum/granville_oshime/granville_rebound｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜3,320円｜💰33.9万円｜—｜⚡材料後出し｜📌
- 7047 PORT INC.｜kenmo_momentum｜🔥絶好調｜💎割安｜FAIL_INSEN｜1,845円｜💰18.9万円｜—
- 4771 F&M Co., Ltd.｜kenmo_momentum/kenmo_newhigh｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜3,055円｜💰28.8万円｜—｜⚠日程不明｜📐進捗 上振れ +68.2%｜🎯2手法一致｜🎯
- 6071 IBJ, Inc.｜kenmo_momentum｜⚡好調｜🟢値頃｜FAIL_INSEN｜862円｜💰8.8万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚡材料後出し｜📌
- 4058 Toyokumo, Inc.｜kenmo_momentum｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,162円｜💰22.2万円｜—
- 5034 unerry, Inc.｜kenmo_momentum｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,483円｜💰25.3万円｜—
- 147A SORACOM,INC.｜kenmo_momentum｜⚡好調｜⚪妥当｜FAIL_INSEN｜906円｜💰9.2万円｜—｜📌
- 9560 PROGRIT, Inc.｜kenmo_momentum｜⚡好調｜⚪妥当｜FAIL_INSEN｜1,079円｜💰11.0万円｜—｜⚠日程不明｜📌
- 7678 ASAKUMA CO.,LTD.｜kenmo_momentum/kenmo_newhigh｜⚡好調｜🔴過熱｜FAIL_INSEN｜4,100円｜💰41.3万円｜—｜⚠日程不明
- 4477 BASE, Inc.｜kenmo_momentum/granville_oshime/granville_rebound｜⚡好調｜⚪妥当｜FAIL_INSEN｜319円｜💰3.3万円｜—｜⚠日程不明
- 2980 SRE Holdings Corp.｜kenmo_momentum｜⚡好調｜💎割安｜PASS｜2,203円｜💰22.0万円｜⛔提案なし(指名鮮度切れ 15営業日)｜📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】不動産業（不動産関連・不動産テック・賃貸仲介関連）
  > 【いま】終値2,203円・直近5日-1.87%（材料未確認）
  > 【調子】⚡好調（5/13） — E軸判定不能(進捗データ不足)
  > 【水準】💎割安（6.0/7）— PER12.56倍・PEG0.7321・52週3.0% ／ 💰単元22.0万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 15営業日)）
- 4412 Science Arts, Inc.｜kenmo_momentum｜⚡好調｜⚪妥当｜FAIL_INSEN｜1,186円｜💰12.2万円｜—｜⚠日程不明
- 6629 TECHNO HORIZON Co., Ltd.｜granville_tenkan/kenmo_momentum｜⚡好調｜⚪妥当｜PASS｜1,047円｜💰10.5万円｜⛔提案なし(指名鮮度切れ 14営業日)｜⚠日程不明｜📐進捗 上振れ +61.7%
  > 【業態】映像・ITとロボティクス技術を核に教育、生活、医療、FA分野で応用・製品化。
  > 【いま】終値1,047円・直近5日+11.74%（材料未確認）
  > 【調子】⚡好調（5/13） — 上方修正済み、質注意
  > 【水準】⚪妥当（3.0/7）— PER7.43倍・PEG3.3485・52週50.2% ／ 💰単元10.5万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 14営業日)）
- 505A Geekly,Inc.｜kenmo_momentum｜✅順調｜💎割安｜FAIL_INSEN｜1,151円｜💰11.8万円｜—｜⚠日程不明｜⚡材料後出し｜📌
- 4743 ITFOR Inc.｜kenmo_momentum｜✅順調｜🟢値頃｜FAIL_INSEN｜1,584円｜💰16.0万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 6289 Giken Ltd.｜granville_tenkan/kenmo_momentum｜⚠減速｜🟡やや割高｜FAIL_UWAHIGE｜1,952円｜💰19.8万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚠日程不明｜⚠業績基調が下向き（減速）
- 3077 Horiifoodservice Co., Ltd.｜kenmo_momentum/granville_rebound｜判定保留(変則決算)｜🟢値頃｜FAIL_INSEN｜1,151円｜💰11.8万円｜—｜⚠日程不明
- 618A KOMPEITO Inc.｜kenmo_momentum/kenmo_newhigh｜取得不可｜⚪妥当｜FAIL_INSEN｜1,881円｜💰19.9万円｜—｜⚠日程不明
- 7567 Sakae Electronics Corp.｜kenmo_newhigh｜🚀確変｜⚪妥当｜FAIL_UWAHIGE｜635円｜💰6.4万円｜—
- 6337 Tesec Corporation｜kenmo_newhigh/granville_rebound｜🔥絶好調｜💎割安｜FAIL_UWAHIGE｜2,584円｜💰25.8万円｜—｜⚠日程不明｜📐進捗 上振れ +22.9%
- 446A ノースサンド｜kenmo_newhigh｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜2,780円｜💰28.2万円｜—｜⚠日程不明
- 3696 セレス｜kenmo_newhigh｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜2,159円｜💰21.8万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚡材料後出し｜🔁
- 2930 北の達人コーポレーション｜kenmo_newhigh｜⚡好調｜🔴過熱｜FAIL_INSEN｜148円｜💰1.5万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚠日程不明
- 4379 Photosynth inc.｜kenmo_newhigh｜⚡好調｜🔴過熱｜FAIL_INSEN｜481円｜💰4.9万円｜—｜📐進捗 上振れ +18.7%
- 2820 Yamami Co.｜kenmo_newhigh｜✅順調｜🟡やや割高｜FAIL_INSEN｜6,730円｜💰69.0万円｜—
- 3843 Freebit Co., Ltd.｜kenmo_newhigh/granville_tenkan｜✅順調｜🟡やや割高｜FAIL_UWAHIGE｜2,035円｜💰20.1万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚠日程不明
- 4933 I-ne CO., LTD.｜kenmo_newhigh｜🔻悪化｜⚪妥当｜FAIL_UWAHIGE｜2,483円｜💰24.6万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚠業績基調が下向き（悪化）
- 7161 Jimoto Holdings, Inc.｜kenmo_newhigh/granville_rebound｜業績データ取得不可｜⚪妥当｜FAIL_INSEN｜532円｜💰5.7万円｜—
- 4565 Nxera Pharma Co., Ltd.｜granville_oshime/kenmo_newhigh｜業績データ取得不可(経常益予想非開示)｜🟡やや割高｜FAIL_UWAHIGE｜1,585円｜💰14.4万円｜—｜⚠日程不明
- 6278 ユニオンツール｜choruko_reversal｜🚀確変｜🟢値頃｜FAIL_UWAHIGE｜12,420円｜💰122.8万円｜—
- 6516 Sanyo Denki Co., Ltd.｜choruko_reversal/ai_reversal｜🔥絶好調｜💎割安｜FAIL_UWAHIGE｜4,780円｜💰48.0万円｜—｜⚠日程不明｜🤖AI特需 ❄️冷却・空調/中流｜⚡材料後出し｜📌
- 6875 メガチップス｜choruko_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜9,420円｜💰98.8万円｜—｜⏰決算 11/06(残3営業日)｜📐進捗 上振れ +20.3%
- 3391 TSURUHA Holdings, Inc.｜choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜2,276.5円｜💰22.2万円｜—｜⚠日程不明
- 5344 MARUWA CO., LTD.｜choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜50,710円｜💰514.7万円｜—｜⚠日程不明
- 6652 IDEC Corporation｜choruko_reversal｜🔥絶好調｜🟢値頃｜PASS_DOJI｜3,330円｜💰33.3万円｜提案あり｜⏰決算 11/06(残3営業日)｜📐進捗 上振れ +11.5%
  > 【業態】制御機器大手。スイッチや表示灯に強み。自動認識機器や防災・防爆関連強化。
  > 【いま】終値3,330円・直近5日-5.40%（材料未確認）
  > 【調子】🔥絶好調（10/13） — 上方修正済み、進捗モデル値域外
  > 【水準】🟢値頃（5.0/7）— PER11.48倍・PEG0.3167・52週54.9% ／ 💰単元33.3万円
  > 【戦略】当日終値3,330円の指値で反転を取りにいく。SL3,305円（直近5日安値）
- 7995 Valqua Ltd.｜choruko_reversal/granville_rebound｜🔥絶好調｜🟢値頃｜PASS｜6,230円｜💰62.3万円｜提案あり｜🚨決算直前 11/04(残1営業日)
  > 【業態】工業用液漏れシール最大手。ゴム・金属・ファイバー製など製品多。先端産業向け力。
  > 【いま】終値6,230円・直近5日+0.00%（材料未確認）
  > 【調子】🔥絶好調（10/13） — 上方修正済み
  > 【水準】🟢値頃（5.0/7）— PER12.63倍・PEG0.2337・52週51.1% ／ 💰単元62.3万円
  > 【戦略】当日終値6,230円の指値で反転を取りにいく。SL6,070円（直近5日安値）
- 7433 Hakuto Co., Ltd.｜ai_reversal/granville_oshime/choruko_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜1,699円｜💰17.5万円｜—
- 8871 GOLDCREST Co., Ltd.｜choruko_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜2,447円｜💰25.0万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚠日程不明｜📐進捗 上振れ +14.6%
- 8336 武蔵野銀行｜granville_oshime/choruko_reversal/granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜2,512円｜💰26.0万円｜—｜⏰決算 11/06(残3営業日)
- 3036 アルコニックス｜choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜3,010円｜💰30.1万円｜—｜⏰決算 11/06(残3営業日)
- 4216 ASAHI YUKIZAI CORPORATION｜choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜6,200円｜💰62.4万円｜—｜⚠日程不明｜📐進捗 遅れ -15.1%
- 6268 ナブテスコ｜choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜4,283円｜💰43.1万円｜—｜⚡材料後出し｜🔁
- 6481 THK Co., Ltd.｜choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜5,716円｜💰57.3万円｜—
- 6324 Harmonic Drive Systems Inc.｜choruko_reversal｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜5,204円｜💰51.6万円｜—
- 6645 OMRON Corporation｜granville_rebound/choruko_reversal｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜5,234円｜💰52.7万円｜—｜⏰決算 11/10(残5営業日)
- 3222 United Super Markets Holdings, Inc.｜choruko_reversal｜🔥絶好調｜🔴過熱｜FAIL_UWAHIGE｜758円｜💰7.5万円｜—｜⚠日程不明
- 6471 日本精工｜choruko_reversal｜🔥絶好調｜💎割安｜FAIL_UWAHIGE｜999.9円｜💰10.0万円｜—｜⚠日程不明
- 6754 アンリツ｜ai_reversal/choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜2,680円｜💰27.5万円｜—｜⚠日程不明
- 8346 東邦銀行｜granville_oshime/granville_rebound/choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜932円｜💰9.7万円｜—｜⏰決算 11/06(残3営業日)
- 5301 Tokai Carbon Co., Ltd.｜choruko_reversal/granville_rebound｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜1,865.5円｜💰19.3万円｜—｜⏰決算 11/05(残2営業日)
- 7733 Olympus Corp.｜choruko_reversal｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜1,736円｜💰17.4万円｜—｜⏰決算 11/10(残5営業日)
- 4088 Air Water Inc.｜choruko_reversal｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜2,873円｜💰28.8万円｜—｜⚠日程不明｜⚡材料後出し｜🔁
- 7004 カナデビア｜choruko_reversal｜⚠減速｜💎割安｜FAIL_UWAHIGE｜1,029円｜💰10.2万円｜—｜⏰決算 11/05(残2営業日)｜⚠業績基調が下向き（減速）
- 5333 ＮＧＫ｜choruko_reversal/ai_reversal｜⚡好調｜🟢値頃｜PASS｜5,118円｜💰51.2万円｜提案あり｜⚠日程不明｜📐進捗 上振れ +14.0%｜⚠1単元でリスク枠超過（54,500円）
  > 【業態】ガラス・土石（電力設備投資関連・自動車部材・部品・セラミックス関連）
  > 【いま】終値5,118円・直近5日+11.84%（材料未確認）
  > 【調子】⚡好調（7/13） — 上方修正済み
  > 【水準】🟢値頃（5.0/7）— PER14.41倍・PEG0.4455・52週47.3% ／ 💰単元51.2万円
  > 【戦略】当日終値5,118円の指値で反転を取りにいく。SL4,573円（直近5日安値）／⚠1単元リスク54,500円（枠超過）
- 6370 栗田工業｜choruko_reversal｜⚡好調｜🟢値頃｜FAIL_INSEN｜4,647円｜💰56.5万円｜—｜⏰決算 11/05(残2営業日)
- 8386 百十四銀行｜choruko_reversal/granville_rebound｜⚡好調｜🟢値頃｜FAIL_INSEN｜2,711円｜💰28.5万円｜—｜⏰決算 11/10(残5営業日)
- 8522 Bank of Nagoya, Ltd.｜choruko_reversal/granville_rebound｜⚡好調｜🟢値頃｜FAIL_INSEN｜5,870円｜💰59.8万円｜—
- 6302 住友重機械工業｜granville_tenkan/choruko_reversal｜⚡好調｜⚪妥当｜PASS｜5,520円｜💰55.2万円｜提案あり｜⚠日程不明｜📐進捗 上振れ +21.6%｜⚠1単元でリスク枠超過（46,700円）｜🔁
  > 【業態】住友系重工大手。変減速機や射出成形機に強み。建機、エネルギー・ライフラインも。
  > 【いま】終値5,520円・直近5日+1.77%・🔁自己株式の取得状況に関するお知らせ（会社法第165条第2項の規定による定款の定めに基づく自己株式の取得）
  > 【調子】⚡好調（7/13） — 上方修正済み
  > 【水準】⚪妥当（4.0/7）— PER18.69倍・PEG0.6019・52週65.3% ／ 💰単元55.2万円
  > 【戦略】当日終値5,520円の指値で反転を取りにいく。SL5,053円（直近5日安値）／⚠1単元リスク46,700円（枠超過）
- 3116 Toyota Boshoku Corp.｜choruko_reversal｜⚡好調｜💎割安｜FAIL_INSEN｜2,000円｜💰20.2万円｜—｜⚠日程不明
- 5101 Yokohama Rubber Co., Ltd.｜choruko_reversal｜⚡好調｜💎割安｜PASS｜6,365円｜💰63.6万円｜提案あり
  > 【業態】タイヤ大手。工業資材や航空部品、ゴルフ用品も展開。北米や農機用タイヤが拡大。
  > 【いま】終値6,365円・直近5日-0.36%（材料未確認）
  > 【調子】⚡好調（6/13） — 経常非開示(IFRS等)のため最終益成長率で代替、税引前代替、E軸判定不能(進捗データ不足)
  > 【水準】💎割安（7.0/7）— PER8.58倍・PEG—・52週31.8% ／ 💰単元63.6万円
  > 【戦略】当日終値6,365円の指値で反転を取りにいく。SL6,160円（直近5日安値）
- 8987 Japan Excellent, Inc.｜choruko_reversal｜⚡好調｜🟢値頃｜FAIL_INSEN｜123,600円｜💰12.6万円｜—｜⚠日程不明
- 4205 Zeon Corporation｜choruko_reversal｜⚡好調｜🟢値頃｜FAIL_INSEN｜2,091.5円｜💰21.3万円｜—｜⚠日程不明｜📐進捗 上振れ +39.7%
- 8282 K'S HOLDINGS CORPORATION｜choruko_reversal｜⚡好調｜🟢値頃｜PASS｜1,724.5円｜💰17.2万円｜⛔提案なし(指名鮮度切れ 13営業日)｜⏰決算 11/05(残2営業日)
  > 【業態】北関東地盤の家電量販大手。デンコードーなど買収で全国。現金値引きに特徴。
  > 【いま】終値1,724.5円・直近5日+0.76%（材料未確認）
  > 【調子】⚡好調（6/13）
  > 【水準】🟢値頃（5.0/7）— PER13.33倍・PEG1.3951・52週37.4% ／ 💰単元17.2万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 13営業日)）
- 6332 月島ホールディングス｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜2,341円｜💰23.2万円｜—｜⏰決算 11/06(残3営業日)｜📐進捗 上振れ +66.0%
- 2782 Seria Co., Ltd.｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜4,240円｜💰43.3万円｜—｜⚠日程不明｜📐進捗 上振れ +20.0%
- 9412 SKY Perfect JSAT Corporation｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜1,784円｜💰18.6万円｜—｜🚨決算直前 11/04(残1営業日)
- 2805 S&B Foods Inc.｜granville_rebound/choruko_reversal｜⚡好調｜🟡やや割高｜FAIL_INSEN｜6,690円｜💰65.4万円｜—｜⚠日程不明｜📐進捗 上振れ +24.6%
- 9436 Okinawa Cellular Telephone Company｜choruko_reversal｜⚡好調｜🟡やや割高｜FAIL_INSEN｜3,295円｜💰34.2万円｜—｜⚠日程不明｜📐進捗 上振れ +16.4%｜⚡材料後出し｜🔁
- 8125 Wakita & Co., Ltd.｜choruko_reversal｜⚡好調｜🔴過熱｜FAIL_INSEN｜1,884円｜💰18.7万円｜—｜⚠日程不明
- 7721 Tokyo Keiki Inc.｜choruko_reversal｜⚡好調｜🟢値頃｜PASS｜5,560円｜💰55.6万円｜⛔提案なし(指名鮮度切れ 11営業日)｜⏰決算 11/06(残3営業日)
  > 【業態】精密機器（計測機器・通信機器・航空機関連）
  > 【いま】終値5,560円・直近5日-1.24%（材料未確認）
  > 【調子】⚡好調（5/13） — E軸判定不能(進捗データ不足)
  > 【水準】🟢値頃（5.0/7）— PER16.92倍・PEG0.5889・52週15.1% ／ 💰単元55.6万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 11営業日)）
- 8278 Fuji Co., Ltd.｜choruko_reversal｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜2,006円｜💰19.9万円｜—｜⚠日程不明
- 8714 池田泉州ホールディングス｜granville_oshime/choruko_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜877円｜💰9.2万円｜—
- 8393 Miyazaki Bank Ltd.｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,353円｜💰24.6万円｜—｜⏰決算 11/06(残3営業日)
- 8399 琉球銀行｜choruko_reversal/granville_rebound｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,663円｜💰28.1万円｜—
- 268A Rigaku Holdings Corporation｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜1,417円｜💰14.4万円｜—
- 7458 Daiichikosho Co., Ltd.｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜1,730円｜💰17.3万円｜—｜⏰決算 11/09(残4営業日)
- 9072 NIKKON Holdings Co., Ltd.｜choruko_reversal｜⚡好調｜⚪妥当｜PASS｜4,110円｜💰41.1万円｜提案あり｜⏰決算 11/06(残3営業日)
  > 【業態】陸運業
  > 【いま】終値4,110円・直近5日-1.91%（材料未確認）
  > 【調子】⚡好調（5/13）
  > 【水準】⚪妥当（3.0/7）— PER22.86倍・PEG2.1462・52週23.7% ／ 💰単元41.1万円
  > 【戦略】当日終値4,110円の指値で反転を取りにいく。SL4,006円（直近5日安値）
- 9882 Yellow Hat Ltd.｜choruko_reversal｜⚡好調｜⚪妥当｜PASS｜1,678円｜💰16.8万円｜⛔提案なし(指名鮮度切れ 15営業日)｜⚠日程不明｜📐進捗 上振れ +14.7%｜🔁
  > 【業態】カー用品販売大手。直営店販売とFC向け卸売りが軸。バイク・自転車販売も。
  > 【いま】終値1,678円・直近5日+2.50%・🔁自己株式立会外買付取引（ToSTNeT-3）による自己株式の取得結果に関するお知らせ
  > 【調子】⚡好調（5/13）
  > 【水準】⚪妥当（3.0/7）— PER11.49倍・PEG2.3298・52週53.1% ／ 💰単元16.8万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 15営業日)）
- 9934 因幡電機産業｜choruko_reversal｜⚡好調｜🟡やや割高｜FAIL_INSEN｜2,823.5円｜💰31.4万円｜—｜⚠日程不明
- 4666 Park24 Co., Ltd.｜choruko_reversal｜✅順調｜💎割安｜FAIL_UWAHIGE｜1,780円｜💰18.3万円｜—｜⚠日程不明
- 7276 Koito Manufacturing Co., Ltd.｜choruko_reversal｜⚠減速｜🟢値頃｜PASS_DOJI｜2,337.5円｜💰23.4万円｜⛔提案なし(材料後出し)｜⚠日程不明｜⚠業績基調が下向き（減速）｜⚡材料後出し｜🔁
  > 【業態】自動車用照明機器首位。トヨタ向け主力。航空機部品も。自動運転用センサー注力。
  > 【いま】終値2,337.5円・直近5日-9.56%・🔁自己株式の取得状況に関するお知らせ
  > 【調子】⚠減速（4/13） — 質注意
  > 【水準】🟢値頃（5.0/7）— PER15.19倍・PEG1.3310・52週18.4% ／ 💰単元23.4万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 7731 ニコン｜choruko_reversal｜✅順調｜🟢値頃｜PASS｜1,694円｜💰16.9万円｜提案あり｜⏰決算 11/05(残2営業日)
  > 【業態】カメラ・回路露光装置の両輪。一眼レフでキヤノンと双璧。ヘルスケア、エネルギー関連強化。
  > 【いま】終値1,694円・直近5日+0.50%（材料未確認）
  > 【調子】✅順調（4/13） — E軸判定不能(進捗データ不足)
  > 【水準】🟢値頃（5.0/7）— PER55.72倍・PEG0.4905・52週9.9% ／ 💰単元16.9万円
  > 【戦略】当日終値1,694円の指値で反転を取りにいく。SL1,624.5円（直近5日安値）
- 8381 San-in Godo Bank Ltd.｜choruko_reversal/granville_rebound｜✅順調｜⚪妥当｜FAIL_INSEN｜2,049円｜💰21.1万円｜—
- 8524 North Pacific Bank, Ltd.｜granville_rebound/choruko_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜1,183円｜💰12.1万円｜—｜⚠業績基調が下向き（減速）
- 6923 Stanley Electric Co., Ltd.｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜3,166円｜💰31.7万円｜—｜⚠日程不明｜📐進捗 遅れ -19.8%
- 3282 Comforia Residential REIT, Inc.｜choruko_reversal｜✅順調｜🟡やや割高｜FAIL_INSEN｜86,700円｜💰8.7万円｜—｜⚠日程不明
- 6925 Ushio Inc.｜choruko_reversal｜✅順調｜🟡やや割高｜PASS｜3,243円｜💰32.4万円｜提案あり｜⏰決算 11/06(残3営業日)
  > 【業態】産業用ランプで世界首位。光源や光学装置を展開。医療装置分野も強化。
  > 【いま】終値3,243円・直近5日-0.22%（材料未確認）
  > 【調子】✅順調（4/13） — E軸判定不能(進捗データ不足)、質注意
  > 【水準】🟡やや割高（2.0/7）— PER24.51倍・PEG5.0022・52週33.1% ／ 💰単元32.4万円
  > 【戦略】当日終値3,243円の指値で反転を取りにいく。SL3,180円（直近5日安値）
- 4021 Nissan Chemical Corporation｜choruko_reversal｜✅順調｜🔴過熱｜FAIL_INSEN｜7,672円｜💰78.0万円｜—｜⏰決算 11/09(残4営業日)｜📐進捗 上振れ +24.6%
- 6135 牧野フライス製作所｜choruko_reversal｜✅順調｜🔴過熱｜FAIL_UWAHIGE｜2,917円｜💰153.8万円｜—｜⚠日程不明｜⚡材料後出し｜🔁
- 1861 Kumagai Gumi Co., Ltd.｜choruko_reversal｜✅順調｜💎割安｜FAIL_UWAHIGE｜1,238円｜💰12.4万円｜—
- 5331 ノリタケ｜choruko_reversal｜✅順調｜🟢値頃｜FAIL_UWAHIGE｜3,265円｜💰32.2万円｜—｜⏰決算 11/05(残2営業日)
- 1417 MIRAIT ONE Corporation｜choruko_reversal｜✅順調｜🟢値頃｜FAIL_INSEN｜3,261円｜💰32.9万円｜—｜⏰決算 11/09(残4営業日)
- 1944 Kinden Corporation｜choruko_reversal｜✅順調｜🟢値頃｜FAIL_INSEN｜5,992円｜💰58.9万円｜—｜⚠日程不明｜📐進捗 上振れ +47.9%
- 3148 Create SD Holdings Co., Ltd.｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜3,165円｜💰31.4万円｜—｜⚠日程不明
- 3433 TOCALO Co., Ltd.｜granville_tenkan/ai_reversal/choruko_reversal｜✅順調｜⚪妥当｜FAIL_UWAHIGE｜2,642円｜💰26.5万円｜—｜⏰決算 11/05(残2営業日)
- 6368 Organo Corp.｜choruko_reversal｜✅順調｜⚪妥当｜PASS｜2,229円｜💰22.3万円｜提案あり｜🚨決算直前 11/04(残1営業日)
  > 【業態】機械（水ビジネス・半導体製造装置・原子力発電関連）
  > 【いま】終値2,229円・直近5日+0.45%（材料未確認）
  > 【調子】✅順調（3/13） — 質注意
  > 【水準】⚪妥当（4.0/7）— PER17.08倍・PEG3.4828・52週5.1% ／ 💰単元22.3万円
  > 【戦略】当日終値2,229円の指値で反転を取りにいく。SL2,132円（直近5日安値）
- 8198 Maxvalu Tokai Co., Ltd.｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_UWAHIGE｜3,105円｜💰31.0万円｜—｜⚠日程不明
- 1820 Nishimatsu Construction Co., Ltd.｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_UWAHIGE｜5,314円｜💰52.6万円｜—｜⏰決算 11/10(残5営業日)
- 1952 Shin Nippon Air Technologies Co., Ltd.｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_UWAHIGE｜2,950円｜💰29.5万円｜—
- 6651 NITTO KOGYO Corporation｜choruko_reversal｜✅順調｜⚪妥当｜PASS｜4,135円｜💰41.4万円｜提案あり｜⏰決算 11/09(残4営業日)｜📐進捗 上振れ +38.1%
  > 【業態】電設資材の配電盤・キャビネット大手。制御盤も。製販一貫体制。通信分野注力。
  > 【いま】終値4,135円・直近5日-1.78%（材料未確認）
  > 【調子】✅順調（3/13）
  > 【水準】⚪妥当（3.0/7）— PER13.52倍・PEG2.9712・52週39.2% ／ 💰単元41.4万円
  > 【戦略】当日終値4,135円の指値で反転を取りにいく。SL4,090円（直近5日安値）
- 7003 Mitsui ES Holdings Co., Ltd.｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_UWAHIGE｜3,506円｜💰35.9万円｜—｜⏰決算 11/10(残5営業日)
- 9533 TOHO GAS Co., Ltd.｜choruko_reversal｜🔻悪化｜⚪妥当｜PASS｜1,286円｜💰12.9万円｜提案あり｜⚠日程不明｜⚠業績基調が下向き（悪化）｜📐進捗 遅れ -81.6%
  > 【業態】都市ガス大手。愛知、岐阜、三重が拠点。LPGに強み。コージェネ事業に注力。
  > 【いま】終値1,286円・直近5日+4.94%（材料未確認）
  > 【調子】🔻悪化（3/13） — 質注意
  > 【水準】⚪妥当（3.0/7）— PER16.16倍・PEG—・52週56.2% ／ 💰単元12.9万円
  > 【戦略】当日終値1,286円の指値で反転を取りにいく。SL1,183円（直近5日安値）
- 1860 Toda Corporation｜choruko_reversal｜✅順調｜🟡やや割高｜FAIL_INSEN｜1,444.5円｜💰14.4万円｜—
- 4966 上村工業｜choruko_reversal｜✅順調｜🟡やや割高｜PASS｜18,350円｜💰183.5万円｜提案あり｜📐進捗 上振れ +27.7%｜⚠1単元でリスク枠超過（55,000円）
  > 【業態】メッキ用化学品とメッキ装置で首位。加工は海外工場で。微細な部品のメッキも。
  > 【いま】終値18,350円・直近5日+4.44%（材料未確認）
  > 【調子】✅順調（3/13） — 質注意、経常減益-5.4%
  > 【水準】🟡やや割高（2.0/7）— PER20.16倍・PEG—・52週38.2% ／ 💰単元183.5万円
  > 【戦略】当日終値18,350円の指値で反転を取りにいく。SL17,800円（直近5日安値）／⚠1単元リスク55,000円（枠超過）
- 6807 Japan Aviation Electronics Industry, Limited｜choruko_reversal｜✅順調｜🟡やや割高｜FAIL_INSEN｜2,458円｜💰24.9万円｜—｜⚠日程不明
- 8066 Mitani Corporation｜granville_rebound/choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜2,784円｜💰28.3万円｜—｜⚠業績基調が下向き（減速）
- 2659 SAN-A CO., LTD.｜choruko_reversal｜✅順調｜🔴過熱｜FAIL_INSEN｜3,180円｜💰31.8万円｜—｜⚠日程不明｜🔁
- 5021 Cosmo Energy Holdings Co., Ltd.｜choruko_reversal｜🔻悪化｜🔴過熱｜FAIL_INSEN｜4,186円｜💰43.7万円｜—｜⏰決算 11/10(残5営業日)｜⚠業績基調が下向き（悪化）
- 6055 Japan Material Co., Ltd.｜choruko_reversal｜✅順調｜🔴過熱｜FAIL_UWAHIGE｜2,004円｜💰20.3万円｜—
- 6674 ジーエス・ユアサ　コーポレーション｜choruko_reversal｜➖横ばい｜⚪妥当｜PASS｜4,636円｜💰46.4万円｜提案あり｜⏰決算 11/06(残3営業日)
  > 【業態】産業用・車載用の鉛蓄電池大手。三相蓄電システム、車載用リチウム電池に注力。
  > 【いま】終値4,636円・直近5日-0.09%（材料未確認）
  > 【調子】➖横ばい（2/13） — 質注意
  > 【水準】⚪妥当（4.0/7）— PER11.78倍・PEG2.4745・52週25.3% ／ 💰単元46.4万円
  > 【戦略】当日終値4,636円の指値で反転を取りにいく。SL4,510円（直近5日安値）
- 1333 Umios Corporation｜choruko_reversal｜➖横ばい｜⚪妥当｜FAIL_INSEN｜1,203.5円｜💰12.2万円｜—｜⚠日程不明
- 1719 HAZAMA ANDO Corporation｜choruko_reversal｜➖横ばい｜⚪妥当｜FAIL_INSEN｜1,744.5円｜💰17.5万円｜—
- 1833 Okumura Corporation｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜5,260円｜💰52.9万円｜—｜⚠業績基調が下向き（減速）
- 7278 Exedy Corporation｜choruko_reversal｜➖横ばい｜⚪妥当｜PASS｜5,160円｜💰51.6万円｜⛔提案なし(材料後出し)｜⚠日程不明｜⚡材料後出し｜🔁
  > 【業態】アイシン系でクラッチ首位。自動車用トルクコンバーターが主力。マニュアル部品でも高シェア。
  > 【いま】終値5,160円・直近5日-7.53%・🔁自己株式の取得状況に関するお知らせ
  > 【調子】➖横ばい（2/13） — 進捗判定不能(自動抽出範囲外)、質注意
  > 【水準】⚪妥当（3.0/7）— PER13.25倍・PEG—・52週9.6% ／ 💰単元51.6万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 3445 RS Technologies Co. Ltd.｜choruko_reversal｜➖横ばい｜🟡やや割高｜FAIL_UWAHIGE｜4,815円｜💰48.8万円｜—｜⚠日程不明
- 6366 Chiyoda Corp.｜choruko_reversal｜🔻悪化｜🟡やや割高｜FAIL_UWAHIGE｜603円｜💰5.9万円｜—｜🚨決算直前 11/04(残1営業日)｜⚠業績基調が下向き（悪化）
- 7220 Musashi Seimitsu Industry Co., Ltd.｜choruko_reversal｜🔻悪化｜🟡やや割高｜PASS｜2,432円｜💰24.3万円｜⛔提案なし(材料後出し)｜⏰決算 11/10(残5営業日)｜⚠業績基調が下向き（悪化）｜⚡材料後出し｜📌
  > 【業態】輸送用機器（自動車部材・部品・オートバイ・電気自動車関連関連）
  > 【いま】終値2,432円・直近5日+0.37%・📌[Delayed]Corporate Governance Report
  > 【調子】🔻悪化（2/13） — E軸判定不能(進捗データ不足)、経常減益率20.9%、質注意
  > 【水準】🟡やや割高（2.0/7）— PER24.52倍・PEG—・52週2.7% ／ 💰単元24.3万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 5844 Kyoto Financial Group,Inc.｜choruko_reversal｜🔻悪化｜🔴過熱｜FAIL_UWAHIGE｜4,028円｜💰41.4万円｜—｜⚠業績基調が下向き（悪化）
- 2379 dip Corporation｜choruko_reversal｜⚠減速｜💎割安｜FAIL_INSEN｜1,480円｜💰15.0万円｜—｜⚠日程不明｜⚠業績基調が下向き（減速）
- 6479 ミネベア｜choruko_reversal｜⚠減速｜🟢値頃｜PASS｜3,145円｜💰31.4万円｜提案あり｜⏰決算 11/06(残3営業日)｜⚠業績基調が下向き（減速）
  > 【業態】総合精密部品メーカー。極小ベアリングで世界高シェア。ミツミと統合で新分野開拓。
  > 【いま】終値3,145円・直近5日+1.00%（材料未確認）
  > 【調子】⚠減速（1/13） — 経常利益(または税引前代替)データ取得不可、leverage算出不可、D軸データ取得不可(中央値1点採用)、E軸判定不能(進捗データ不足)
  > 【水準】🟢値頃（5.2/7）— PER14.52倍・PEG—・52週22.5% ／ 💰単元31.4万円
  > 【戦略】当日終値3,145円の指値で反転を取りにいく。SL3,061円（直近5日安値）
- 1946 Toenec Corporation｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜1,785円｜💰17.9万円｜—｜⚠日程不明｜⚠業績基調が下向き（減速）
- 6632 JVCKENWOOD Corporation｜choruko_reversal｜⚠減速｜⚪妥当｜PASS_DOJI｜873円｜💰8.7万円｜提案あり｜⚠日程不明｜⚠業績基調が下向き（減速）
  > 【業態】ビクターとケンウッドが統合。AV機器、車載、業務用に注力。ドラレコ関連事業を強化。
  > 【いま】終値873円・直近5日-5.56%（材料未確認）
  > 【調子】⚠減速（1/13） — 税引前代替、D軸判定不能(直近Qデータ取得不可)、E軸判定不能(期首・進捗なし)、質注意
  > 【水準】⚪妥当（4.0/7）— PER8.21倍・PEG—・52週2.3% ／ 💰単元8.7万円
  > 【戦略】当日終値873円の指値で反転を取りにいく。SL859円（直近5日安値）
- 1893 Penta-Ocean Construction Co., Ltd.｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜1,351円｜💰13.5万円｜—｜⏰決算 11/09(残4営業日)｜⚠業績基調が下向き（減速）
- 5482 Aichi Steel Corporation｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_UWAHIGE｜2,344円｜💰23.4万円｜—｜⚠日程不明｜⚠業績基調が下向き（減速）
- 6183 BELLSYSTEM24 Holdings, Inc.｜choruko_reversal｜⚠減速｜⚪妥当｜PASS｜1,360円｜💰13.6万円｜⛔提案なし(指名鮮度切れ 15営業日)｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚠日程不明｜⚠業績基調が下向き（減速）
  > 【業態】コールセンターのCRM事業を中心にBPO事業も。伊藤忠が資本参加。凸版と提携。
  > 【いま】終値1,360円・直近5日-3.13%（材料未確認）
  > 【調子】⚠減速（1/13） — E軸判定不能(進捗データ不足)、D軸判定不能(四半期データ不足・中立1点)
  > 【水準】⚪妥当（3.0/7）— PER11.89倍・PEG4.7131・52週35.6% ／ 💰単元13.6万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 15営業日)）
- 6753 Sharp Corporation｜choruko_reversal｜🔻悪化｜⚪妥当｜FAIL_INSEN｜540円｜💰5.4万円｜—｜⏰決算 11/09(残4営業日)｜⚠業績基調が下向き（悪化）
- 8276 HEIWADO CO., LTD.｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_UWAHIGE｜2,616円｜💰26.0万円｜—｜⚠日程不明｜⚠業績基調が下向き（減速）
- 8585 Orient Corporation｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜782円｜💰7.7万円｜—｜⚠日程不明｜⚠業績基調が下向き（減速）｜📐進捗 遅れ -32.2%
- 9974 BELC Co., Ltd.｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_UWAHIGE｜6,520円｜💰65.0万円｜—｜⚠日程不明｜⚠業績基調が下向き（減速）
- 3296 NIPPON REIT Investment Corp｜choruko_reversal｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜74,300円｜💰7.6万円｜—｜⚠日程不明｜⚠業績基調が下向き（悪化）
- 4980 Dexerials Corp.｜choruko_reversal/ai_reversal｜⚠減速｜🟡やや割高｜PASS｜2,904.5円｜💰29.0万円｜提案あり｜⚠業績基調が下向き（減速）｜🤖AI特需 🌐光通信/上流
  > 【業態】ディスプレーなどの光学材料、電子材料を製造、販売。スマホ向け世界高シェア。
  > 【いま】終値2,904.5円・直近5日-0.05%（材料未確認）
  > 【調子】⚠減速（1/13） — E軸判定不能(進捗データ不足)、質注意
  > 【水準】🟡やや割高（2.0/7）— PER17.69倍・PEG60.6283・52週26.1% ／ 💰単元29.0万円
  > 【戦略】当日終値2,904.5円の指値で反転を取りにいく。SL2,830円（直近5日安値）
- 5631 Japan Steel Works, Ltd.｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜5,855円｜💰58.9万円｜—｜⏰決算 11/10(残5営業日)｜⚠業績基調が下向き（減速）
- 9948 Arcs Company, Limited｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜3,535円｜💰35.4万円｜—｜⚠日程不明｜⚠業績基調が下向き（減速）
- 1963 日揮ホールディングス｜choruko_reversal｜🔻悪化｜🔴過熱｜PASS｜2,122円｜💰21.2万円｜提案あり｜⚠業績基調が下向き（悪化）
  > 【業態】総合エンジニアリング最大手。世界各地で石油、化学、発電、水素、LNGプラント建設。
  > 【いま】終値2,122円・直近5日+1.92%（材料未確認）
  > 【調子】🔻悪化（1/13） — 質注意、E軸判定不能(進捗データ不足)、D軸判定不能(四半期データ不足・中立1点)、減収、経常減益
  > 【水準】🔴過熱（1.4/7）— PER11.17倍・PEG—・52週43.4% ／ 💰単元21.2万円
  > 【戦略】当日終値2,122円の指値で反転を取りにいく。SL2,075.5円（直近5日安値）
- 3105 日清紡ホールディングス｜choruko_reversal｜🔻悪化｜🔴過熱｜FAIL_UWAHIGE｜2,224.5円｜💰22.4万円｜—｜⏰決算 11/10(残5営業日)｜⚠業績基調が下向き（悪化）
- 5310 Toyo Tanso Co., Ltd.｜choruko_reversal/ai_reversal｜🔻悪化｜🔴過熱｜PASS｜6,550円｜💰65.5万円｜提案あり｜⏰決算 11/09(残4営業日)｜⚠業績基調が下向き（悪化）｜🤖AI特需 🔬基板・素材/上流
  > 【業態】等方性黒鉛で先駆、世界高シェア。半導体製造用るつぼが主力。一貫生産。
  > 【いま】終値6,550円・直近5日+6.68%（材料未確認）
  > 【調子】🔻悪化（1/13） — 質注意
  > 【水準】🔴過熱（1.0/7）— PER27.47倍・PEG—・52週45.8% ／ 💰単元65.5万円
  > 【戦略】当日終値6,550円の指値で反転を取りにいく。SL6,300円（直近5日安値）
- 6960 Fukuda Denshi Co., Ltd.｜choruko_reversal｜⚠減速｜🔴過熱｜FAIL_INSEN｜9,740円｜💰114.1万円｜—｜⚠日程不明｜⚠業績基調が下向き（減速）
- 1662 Japan Petroleum Exploration Co., Ltd.｜choruko_reversal｜🔻悪化｜⚪妥当｜FAIL_INSEN｜1,728円｜💰17.5万円｜—｜⚠業績基調が下向き（悪化）
- 6804 Hosiden Corp.｜choruko_reversal｜🔻悪化｜⚪妥当｜FAIL_UWAHIGE｜2,287円｜💰23.2万円｜—｜⚠業績基調が下向き（悪化）
- 7148 Financial Products Group Co., Ltd.｜choruko_reversal｜⚠減速｜⚪妥当｜PASS｜1,415円｜💰14.2万円｜提案あり｜⚠日程不明｜⚠業績基調が下向き（減速）
  > 【業態】船舶やコンテナのオペリース事業が主力。不動産小口化、保険や証券など多角化。
  > 【いま】終値1,415円・直近5日-14.45%（材料未確認）
  > 【調子】⚠減速（0/13） — E軸判定不能(期首・進捗なし)、質注意
  > 【水準】⚪妥当（4.0/7）— PER7.90倍・PEG—・52週4.2% ／ 💰単元14.2万円
  > 【戦略】当日終値1,415円の指値で反転を取りにいく。SL1,375円（直近5日安値）
- 8194 Life Corporation｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_UWAHIGE｜2,514円｜💰24.7万円｜—｜⚠日程不明｜⚠業績基調が下向き（減速）
- 6349 Komori Corporation｜choruko_reversal｜⚠減速｜🟡やや割高｜PASS｜1,737円｜💰17.4万円｜提案あり｜⚠日程不明｜⚠業績基調が下向き（減速）｜📐進捗 上振れ +24.1%
  > 【業態】印刷機専業トップ。枚葉機、紙幣印刷機に強み。欧米に輸出、中国は中古も。
  > 【いま】終値1,737円・直近5日-10.97%（材料未確認）
  > 【調子】⚠減速（0/13） — 質注意
  > 【水準】🟡やや割高（2.0/7）— PER12.51倍・PEG—・52週51.2% ／ 💰単元17.4万円
  > 【戦略】当日終値1,737円の指値で反転を取りにいく。SL1,708円（直近5日安値）
- 9699 NISHIO HOLDINGS CO. LTD.｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜4,245円｜💰43.0万円｜—｜⏰決算 11/10(残5営業日)｜⚠業績基調が下向き（減速）
- 3612 WORLD CO.,LTD.｜choruko_reversal｜業績データ取得不可(経常益予想非開示)｜💎割安｜PASS｜1,436円｜💰14.4万円｜提案あり｜⚠日程不明
  > 【業態】繊維製品（アパレル・専門店・婦人服関連）
  > 【いま】終値1,436円・直近5日+1.34%（材料未確認）
  > 【調子】業績データ取得不可(経常益予想非開示)（—/13） — 経常欠損
  > 【水準】💎割安（7.0/7）— PER8.69倍・PEG—・52週24.6% ／ 💰単元14.4万円
  > 【戦略】当日終値1,436円の指値で反転を取りにいく。SL1,360円（直近5日安値）
- 8975 Ichigo Office REIT Investment Corporation｜choruko_reversal｜判定保留(変則決算)｜💎割安｜PASS｜82,600円｜💰8.3万円｜提案あり｜⚠日程不明
  > 【業態】投資は中規模オフィスビル特化型。価値向上修繕も。運用:いちごグループHD系。
  > 【いま】終値82,600円・直近5日-7.92%（材料未確認）
  > 【調子】判定保留(変則決算)（—/13） — 変則決算・四半期不足
  > 【水準】💎割安（7.0/7）— PER11.33倍・PEG0.0555・52週12.3% ／ 💰単元8.3万円
  > 【戦略】当日終値82,600円の指値で反転を取りにいく。SL80,100円（直近5日安値）
- 8253 Credit Saison Co., Ltd.｜choruko_reversal｜取得不可｜💎割安｜FAIL_INSEN｜4,099円｜💰41.4万円｜—
- 8370 紀陽銀行｜choruko_reversal｜取得不可｜💎割安｜FAIL_INSEN｜1,540円｜💰15.8万円｜—｜⏰決算 11/09(残4営業日)
- 7381 ＣＣＩグループ｜choruko_reversal/granville_rebound｜業績データ取得不可(売上/経常欠損)｜🟢値頃｜FAIL_INSEN｜1,075円｜💰11.3万円｜—｜⚠日程不明｜📐進捗 遅れ -13.8%
- 5831 Shizuoka Financial Group, Inc.｜choruko_reversal/granville_rebound｜取得不可｜🟢値頃｜PASS｜3,030円｜💰30.3万円｜提案あり｜⏰決算 11/10(残5営業日)
  > 【業態】静岡地盤の地銀上位。地銀有数の収益力。業務範囲拡大。マネックスGの株主。
  > 【いま】終値3,030円・直近5日+4.14%（材料未確認）
  > 【調子】取得不可（—/13） — 業績データ取得不可
  > 【水準】🟢値頃（5.0/7）— PER13.76倍・PEG0.4885・52週59.3% ／ 💰単元30.3万円
  > 【戦略】当日終値3,030円の指値で反転を取りにいく。SL2,948.5円（直近5日安値）
- 8304 あおぞら銀行｜choruko_reversal｜取得不可｜🟢値頃｜PASS｜2,981円｜💰29.8万円｜提案あり
  > 【業態】旧日債銀。不動産融資、金融商品販売などが中心。GMOとネット銀行。
  > 【いま】終値2,981円・直近5日-0.08%（材料未確認）
  > 【調子】取得不可（—/13） — 業績データ取得不可
  > 【水準】🟢値頃（5.0/7）— PER15.29倍・PEG0.4233・52週56.5% ／ 💰単元29.8万円
  > 【戦略】当日終値2,981円の指値で反転を取りにいく。SL2,903円（直近5日安値）
- 8345 Bank of Iwate Ltd.｜choruko_reversal｜業績データ取得不可(売上/経常欠損)｜🟢値頃｜FAIL_INSEN｜2,086円｜💰21.9万円｜—
- 8367 南都銀行｜granville_oshime/choruko_reversal｜取得不可｜🟢値頃｜FAIL_INSEN｜1,718円｜💰17.9万円｜—｜⏰決算 11/10(残5営業日)
- 7384 Procrea Holdings,Inc.｜granville_rebound/choruko_reversal｜業績データ取得不可(売上/経常欠損)｜⚪妥当｜FAIL_UWAHIGE｜3,875円｜💰42.8万円｜—｜⚠日程不明
- 8174 NIPPON GAS Co., Ltd.｜choruko_reversal｜業績データ取得不可(売上/経常欠損)｜⚪妥当｜FAIL_INSEN｜839.5円｜💰8.7万円｜—｜⚠日程不明｜📐進捗 上振れ +28.9%｜⚡材料後出し｜🔁
- 8334 Gunma Bank, Ltd.｜granville_rebound/choruko_reversal｜取得不可｜⚪妥当｜FAIL_INSEN｜2,535円｜💰26.1万円｜—｜⏰決算 11/09(残4営業日)
- 8366 滋賀銀行｜granville_rebound/choruko_reversal｜取得不可｜⚪妥当｜FAIL_UWAHIGE｜2,443.5円｜💰24.8万円｜—
- 6810 Maxell, Ltd.｜granville_oshime/choruko_reversal/granville_rebound｜業績データ取得不可(経常益予想非開示)｜⚪妥当｜PASS｜2,279円｜💰22.8万円｜提案あり｜⚠日程不明
  > 【業態】電池や産業用部材が主力。車載、理美容家電向け注力。全固体電池量産化。
  > 【いま】終値2,279円・直近5日-8.07%（材料未確認）
  > 【調子】業績データ取得不可(経常益予想非開示)（—/13） — 経常欠損
  > 【水準】⚪妥当（3.5/7）— PER12.54倍・PEG—・52週49.3% ／ 💰単元22.8万円
  > 【戦略】当日終値2,279円の指値で反転を取りにいく。SL2,150円（直近5日安値）
- 7201 Nissan Motor Co., Ltd.｜choruko_reversal｜業績データ取得不可(経常益予想非開示)｜⚪妥当｜FAIL_INSEN｜262.6円｜💰2.7万円｜—
- 3591 WACOAL HOLDINGS CORP｜choruko_reversal｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜3,611円｜💰36.1万円｜—｜⚠業績基調が下向き（悪化）
- 2109 ＤＭ三井製糖｜choruko_reversal｜—｜—｜FAIL_INSEN｜3,525円｜💰—｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚠日程不明
- 5711 三菱マテリアル｜choruko_reversal｜—｜—｜FAIL_INSEN｜4,253円｜💰—｜—
- 7167 めぶきフィナンシャルグループ｜choruko_reversal｜—｜—｜FAIL_INSEN｜1,455.5円｜💰—｜—
- 7177 ＧＭＯフィナンシャルホールディングス｜choruko_reversal｜—｜—｜FAIL_INSEN｜1,018円｜💰—｜—｜⚠日程不明
- 7186 横浜フィナンシャルグループ｜choruko_reversal｜業績データ取得不可｜⏸判定不能｜PASS｜1,653.5円｜💰16.8万円｜提案あり
  > 【業態】傘下に横浜銀、東日本銀、神奈川銀。総合力に強み。中小企業、個人に注力。
  > 【いま】終値1,653.5円・直近5日+1.26%（材料未確認）
  > 【調子】業績データ取得不可（—/13） — kabutan年次表を解析できず
  > 【水準】⏸判定不能（—/7）— PER—倍・PEG—・52週65.3% ／ 💰単元16.8万円
  > 【戦略】当日終値1,653.5円の指値で反転を取りにいく。SL1,625円（直近5日安値）
- 7322 三十三フィナンシャルグループ｜choruko_reversal/granville_rebound｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜1,802円｜💰18.8万円｜—
- 8354 ふくおかフィナンシャルグループ｜choruko_reversal｜業績データ取得不可｜⏸判定不能｜PASS｜6,865円｜💰69.5万円｜提案あり｜⏰決算 11/10(残5営業日)
  > 【業態】傘下に福岡・熊本・十八親和など。総資産は地銀首位級。ネット銀行設立。
  > 【いま】終値6,865円・直近5日+2.77%（材料未確認）
  > 【調子】業績データ取得不可（—/13） — kabutan年次表を解析できず
  > 【水準】⏸判定不能（—/7）— PER—倍・PEG—・52週70.2% ／ 💰単元69.5万円
  > 【戦略】当日終値6,865円の指値で反転を取りにいく。SL6,695円（直近5日安値）
- 8359 Hachijuni Nagano Bank, Ltd.｜choruko_reversal/granville_rebound｜業績データ取得不可｜⏸判定不能｜FAIL_UWAHIGE｜2,400円｜💰24.5万円｜—｜⏰決算 11/06(残3営業日)
- 8600 トモニホールディングス｜choruko_reversal｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜1,018円｜💰10.5万円｜—
- 8616 Tokai Tokyo Financial Holdings, Inc.｜choruko_reversal｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜762円｜💰7.9万円｜—｜⚠日程不明｜⚡材料後出し｜📌
- 8628 Matsui Securities Co., Ltd.｜granville_oshime/choruko_reversal｜業績データ取得不可｜⏸判定不能｜FAIL_UWAHIGE｜1,004円｜💰10.2万円｜—｜⚠日程不明｜⚡材料後出し｜📌
- 8698 Monex Group, Inc.｜choruko_reversal｜業績データ取得不可｜⏸判定不能｜PASS｜625円｜💰6.2万円｜提案あり｜⏰決算 11/09(残4営業日)｜📌
  > 【業態】ネット証券。米など海外でも。国内証券はNTTドコモ傘下に。子会社にコインチェック。
  > 【いま】終値625円・直近5日-0.64%・📌Integrated Report 2026
  > 【調子】業績データ取得不可（—/13） — 通期予想なし
  > 【水準】⏸判定不能（—/7）— PER—倍・PEG—・52週6.4% ／ 💰単元6.2万円
  > 【戦略】当日終値625円の指値で反転を取りにいく。SL614円（直近5日安値）
- 7624 NaITO｜stf_kakuhen｜🔥絶好調｜💎割安｜FAIL_INSEN｜157円｜💰1.6万円｜—｜⚠日程不明
- 4410 ハリマ化成グループ（ハリマ化成Ｇ）｜stf_kakuhen｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1,319円｜💰13.6万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚠日程不明｜📐進捗 上振れ +21.5%
- 6668 ＡＤプラズマ｜stf_kakuhen/granville_oshime｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜4,440円｜💰45.1万円｜—｜⚠日程不明
- 7713 シグマ光機｜stf_kakuhen｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜3,025円｜💰30.1万円｜—｜⚠日程不明
- 5832 ちゅうぎんフィナンシャルグループ（ちゅうぎんＦ）｜stf_kakuhen｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜3,514円｜💰36.0万円｜—｜⚠日程不明
- 5018 ＭＯＲＥＳＣＯ｜stf_kakuhen｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜2,770円｜💰27.3万円｜—｜⚠日程不明
- 7942 ＪＳＰ｜stf_kakuhen｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜3,035円｜💰30.7万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚠日程不明｜📐進捗 上振れ +61.9%
- 9962 ミスミグループ本社｜changepoint/changepoint🔔/stf_kakuhen｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜4,073円｜💰39.2万円｜—｜⚠日程不明｜⚡材料後出し｜🔁
- 3498 霞ヶ関Ｃ｜stf_kakuhen｜🔥絶好調｜💎割安｜FAIL_UWAHIGE｜7,330円｜💰73.3万円｜—｜⚠日程不明｜⚡材料後出し｜📌
- 9110 ＮＳユナイテッド海運（ユナイテド海）｜stf_kakuhen｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜10,550円｜💰105.4万円｜—｜⚠日程不明｜📐進捗 上振れ +21.3%
- 3994 マネーフォワード｜stf_kakuhen｜🔥絶好調｜🔴過熱｜FAIL_INSEN｜7,000円｜💰68.5万円｜—｜⚠日程不明
- 7811 中本パックス｜granville_oshime/stf_kakuhen｜🔥絶好調｜💎割安｜FAIL_INSEN｜2,397円｜💰24.5万円｜—｜⚠日程不明｜📐進捗 上振れ +21.8%
- 4443 Ｓａｎｓａｎ｜changepoint/stf_kakuhen/changepoint🔔🔔｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜2,137円｜💰21.8万円｜—｜⚠日程不明
- 9766 コナミグループ（コナミＧ）｜stf_kakuhen｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜26,105円｜💰263.9万円｜—｜⚠日程不明
- 6814 古野電｜stf_kakuhen｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜7,910円｜💰78.1万円｜—｜⚠日程不明
- 5932 三協立山｜stf_kakuhen/granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜732円｜💰7.4万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚠日程不明
- 3091 ブロンコビリー｜changepoint/changepoint🔔🔔/stf_kakuhen｜⚡好調｜🟡やや割高｜FAIL_INSEN｜3,030円｜💰30.1万円｜—｜⚠日程不明
- 3479 ＴＫＰ｜stf_kakuhen/granville_tenkan｜⚡好調｜🔴過熱｜FAIL_UWAHIGE｜1,968円｜💰19.5万円｜—｜⚠日程不明｜📌
- 4417 グローバルセキュリティエキスパート（Ｇセキュリ）｜stf_kakuhen｜⚡好調｜🔴過熱｜FAIL_INSEN｜8,470円｜💰82.9万円｜—｜⚠日程不明
- 6505 東洋電機製造｜ai_momentum/stf_kakuhen｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜2,943円｜💰29.1万円｜—｜⚠日程不明
- 6532 ベイカレント｜stf_kakuhen｜⚡好調｜🟡やや割高｜FAIL_INSEN｜11,630円｜💰118.2万円｜—｜⚠日程不明
- 4176 ココナラ｜stf_kakuhen｜✅順調｜💎割安｜FAIL_INSEN｜284円｜💰2.9万円｜—｜⚠日程不明｜📌
- 8954 ORIX JREIT Inc.｜prev_proposal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜86,500円｜💰8.7万円｜—｜⚠日程不明｜⚠業績基調が下向き（減速）

## グランビル銘柄
- 5254 Arent, Inc.｜granville_tenkan｜🚀確変｜⚪妥当｜FAIL_INSEN｜3,690円｜💰37.7万円｜—｜📌
- 3927 アークン｜granville_tenkan｜🚀確変｜💎割安｜PASS_DOJI｜927円｜💰9.3万円｜提案あり
  > 【業態】情報セキュリティ製品の開発・販売・保守。中小企業向けの業務システムに注力。
  > 【いま】終値927円・直近5日-9.38%（材料未確認）
  > 【調子】🚀確変（11/13） — 進捗モデル値域外
  > 【水準】💎割安（6.0/7）— PER15.07倍・PEG0.1437・52週28.8% ／ 💰単元9.3万円
  > 【戦略】当日高値超えの逆指値958円で順張り参戦を検討。上限967.6円・SL899.6円目安
- 8944 Land Business Co., Ltd.｜granville_tenkan｜🔥絶好調｜💎割安｜FAIL_INSEN｜252円｜💰2.5万円｜—
- 6905 Cosel Co., Ltd.｜granville_tenkan｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜1,252円｜💰12.5万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚠日程不明
- 9553 MicroAd, Inc.｜granville_tenkan｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜535円｜💰5.7万円｜—
- 7725 INTER ACTION Corporation｜granville_tenkan｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜1,822円｜💰17.9万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚠日程不明
- 9211 f-code Inc.｜changepoint/granville_tenkan/changepoint🔔｜🔥絶好調｜💎割安｜FAIL_UWAHIGE｜1,134円｜💰11.5万円｜—
- 6562 Geniee, Inc.｜granville_tenkan｜🔥絶好調｜💎割安｜FAIL_INSEN｜804円｜💰9.1万円｜—
- 6470 Taiho Kogyo Co., Ltd.｜granville_tenkan｜🔥絶好調｜💎割安｜FAIL_INSEN｜1,045円｜💰10.7万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚠日程不明｜📐進捗 上振れ +13.0%
- 4956 Konishi Co., Ltd.｜granville_tenkan｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜1,545円｜💰15.3万円｜—｜⚠日程不明｜📐進捗 上振れ +17.3%
- 8697 日本取引所グループ｜granville_tenkan/changepoint🔔/changepoint｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜2,101.5円｜💰21.2万円｜—｜⚠日程不明｜📐進捗 上振れ +24.0%
- 9742 アイネス｜granville_tenkan｜🔥絶好調｜⚪妥当｜PASS｜2,424円｜💰24.2万円｜提案あり｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚠日程不明
  > 【業態】独立系のSI大手。組合・団体、地方自治体向けに強み。三菱総研と提携。
  > 【いま】終値2,424円・直近5日+3.68%（材料未確認）
  > 【調子】🔥絶好調（8/13） — E軸判定不能(進捗データ不足)
  > 【水準】⚪妥当（3.0/7）— PER29.71倍・PEG0.0462・52週88.1% ／ 💰単元24.2万円
  > 【戦略】当日高値超えの逆指値2,441円で順張り参戦を検討。上限2,465.4円・SL2,293.6円目安
- 4534 Mochida Pharmaceutical Co., Ltd.｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_INSEN｜3,265円｜💰32.9万円｜—｜⏰決算 11/09(残4営業日)｜📐進捗 上振れ +24.5%｜🔁
- 6255 NPC Incorporated｜granville_tenkan｜⚡好調｜🟢値頃｜PASS｜687円｜💰6.9万円｜提案あり｜⚠日程不明｜📌
  > 【業態】太陽電池製造装置大手。パネル解体装置やFA装置も展開。植物工場も。
  > 【いま】終値687円・直近5日+10.45%・📌Convocation Notice of the 34th Ordinary General Meeting of Shareholders for FY2026
  > 【調子】⚡好調（7/13） — E軸判定不能(進捗データ不足)
  > 【水準】🟢値頃（5.0/7）— PER17.44倍・PEG0.2857・52週37.5% ／ 💰単元6.9万円
  > 【戦略】当日高値超えの逆指値689円で順張り参戦を検討。上限695.9円・SL646.7円目安
- 3405 クラレ｜granville_tenkan｜⚡好調｜⚪妥当｜PASS｜1,875円｜💰18.8万円｜提案あり
  > 【業態】化学品大手。高分子機能素材・フィルムに強み。樹脂の世界トップ製品多数。
  > 【いま】終値1,875円・直近5日+1.63%（材料未確認）
  > 【調子】⚡好調（7/13）
  > 【水準】⚪妥当（4.0/7）— PER14.12倍・PEG0.5826・52週64.4% ／ 💰単元18.8万円
  > 【戦略】当日高値超えの逆指値1,876円で順張り参戦を検討。上限1,894.8円・SL1,762.5円目安
- 4401 ＡＤＥＫＡ｜granville_tenkan｜⚡好調｜⚪妥当｜PASS｜4,522円｜💰45.2万円｜提案あり｜📐進捗 上振れ +31.5%
  > 【業態】化学品・食品・ライフサイエンスが軸。樹脂添加剤・業務用食物油が主。海外販強化。
  > 【いま】終値4,522円・直近5日+1.28%（材料未確認）
  > 【調子】⚡好調（7/13） — 上方修正済み
  > 【水準】⚪妥当（4.0/7）— PER13.72倍・PEG0.8116・52週66.3% ／ 💰単元45.2万円
  > 【戦略】当日高値超えの逆指値4,541円で順張り参戦を検討。上限4,586.4円・SL4,263.8円目安
- 7744 ノーリツ鋼機｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,026円｜💰20.7万円｜—
- 8095 Astena Holdings Co.,Ltd.｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜555円｜💰5.5万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚠日程不明
- 3741 Systems Engineering Consultants Co., Ltd.｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,887円｜💰30.5万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 4544 H.U.Group Holdings, Inc.｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜3,928円｜💰39.4万円｜—
- 5532 リアルゲイト｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜3,565円｜💰35.5万円｜—｜⚠日程不明｜⚡材料後出し｜📌
- 7970 Shin-Etsu Polymer Co., Ltd.｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,504円｜💰25.4万円｜—｜⚠日程不明
- 5838 Rakuten Bank, Ltd.｜granville_tenkan｜⚡好調｜💎割安｜FAIL_UWAHIGE｜5,737円｜💰59.2万円｜—
- 4763 クリーク・アンド・リバー社｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_INSEN｜1,498円｜💰15.1万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚠日程不明
- 7199 プレミアグループ｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,217円｜💰22.7万円｜—｜⏰決算 11/10(残5営業日)｜⚡材料後出し｜📌
- 7606 ＴＡＢＡＹＡホールディングス｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,500円｜💰24.1万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⏰決算 11/06(残3営業日)
- 4848 Fullcast Holdings Co., Ltd.｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜1,834円｜💰18.5万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⏰決算 11/06(残3営業日)
- 6371 Tsubakimoto Chain Co.｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,593円｜💰26.6万円｜—｜⚠日程不明｜📐進捗 上振れ +18.4%｜⚡材料後出し｜🔁
- 4045 Toagosei Co., Ltd.｜granville_tenkan｜⚡好調｜🔴過熱｜FAIL_UWAHIGE｜1,803円｜💰18.2万円｜—｜⚠日程不明
- 3935 Edia Co. Ltd.｜granville_tenkan｜⚡好調｜💎割安｜PASS｜681円｜💰6.8万円｜⛔提案なし(指名鮮度切れ 11営業日)｜⚠日程不明
  > 【業態】ゲーム、コミックなどIP活用、電子書籍販売やBtoBを展開。版権ビジネスに強み。
  > 【いま】終値681円・直近5日-3.95%（材料未確認）
  > 【調子】⚡好調（5/13）
  > 【水準】💎割安（7.0/7）— PER7.71倍・PEG0.2587・52週17.4% ／ 💰単元6.8万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 11営業日)）
- 6768 Tamura Corporation｜granville_tenkan/granville_oshime｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜793円｜💰8.1万円｜—｜⏰決算 11/09(残4営業日)
- 3562 No.1 Co., Ltd.｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_INSEN｜1,566円｜💰15.9万円｜—｜⚠日程不明｜⚡材料後出し｜📌
- 4617 中国塗料｜granville_tenkan｜⚡好調｜🟢値頃｜PASS｜3,495円｜💰35.0万円｜提案あり｜⚠日程不明｜📐進捗 上振れ +16.2%
  > 【業態】船舶用塗料の世界大手。工業用塗料も展開。アジアを中心に海外販売網。
  > 【いま】終値3,495円・直近5日+2.64%（材料未確認）
  > 【調子】⚡好調（5/13） — 上方修正済み
  > 【水準】🟢値頃（5.0/7）— PER13.35倍・PEG0.8953・52週31.3% ／ 💰単元35.0万円
  > 【戦略】当日高値超えの逆指値3,540円で順張り参戦を検討。上限3,575.4円・SL3,322.9円目安
- 8061 Seika Corporation｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜2,890円｜💰29.8万円｜—｜⏰決算 11/10(残5営業日)
- 9842 アークランズ｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_INSEN｜1,897円｜💰19.1万円｜—｜⚠日程不明
- 4169 Enechange Ltd.｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜261円｜💰2.7万円｜—｜⏰決算 11/06(残3営業日)｜📐進捗 遅れ -85.0%
- 6432 竹内製作所｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜7,590円｜💰76.4万円｜—｜⚠日程不明｜🔁
- 8014 Chori Co., Ltd.｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜4,240円｜💰42.2万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚠日程不明
- 7747 朝日インテック｜granville_tenkan｜⚡好調｜🟡やや割高｜FAIL_INSEN｜3,528円｜💰36.7万円｜—
- 8020 Kanematsu Corporation｜granville_tenkan｜⚡好調｜🟡やや割高｜FAIL_INSEN｜2,248.5円｜💰23.8万円｜—｜⏰決算 11/05(残2営業日)
- 4568 第一三共｜granville_tenkan｜✅順調｜⚪妥当｜PASS｜2,892.5円｜💰28.9万円｜提案あり｜⚠日程不明
  > 【業態】国内製薬大手。循環器と感染症に強み。がん新薬で英アストラゼネカと提携。
  > 【いま】終値2,892.5円・直近5日+2.39%（材料未確認）
  > 【調子】✅順調（4/13） — 税引前代替、D軸判定不能(直近Qデータ取得不可)、上方修正済み
  > 【水準】⚪妥当（4.0/7）— PER20.99倍・PEG1.4750・52週33.0% ／ 💰単元28.9万円
  > 【戦略】当日高値超えの逆指値2,893.5円で順張り参戦を検討。上限2,922.4円・SL2,718.9円目安
- 4549 Eiken Chemical Co., Ltd.｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_INSEN｜2,238円｜💰23.1万円｜—｜⚠日程不明
- 6592 Mabuchi Motor Co., Ltd.｜granville_tenkan｜✅順調｜🟡やや割高｜PASS｜1,727円｜💰17.3万円｜提案あり｜⚠日程不明｜📊
  > 【業態】小型モーターで世界高シェア。海外生産比率100%。車載用電装機器が主軸。
  > 【いま】終値1,727円・直近5日-0.63%・📊2026年12月期第3四半期決算短信〔日本基準〕（連結）
  > 【調子】✅順調（4/13） — 質注意
  > 【水準】🟡やや割高（2.0/7）— PER18.20倍・PEG—・52週70.0% ／ 💰単元17.3万円
  > 【戦略】当日高値超えの逆指値1,740円で順張り参戦を検討。上限1,757.4円・SL1,634.7円目安
- 3092 ＺＯＺＯ｜granville_tenkan｜✅順調｜🔴過熱｜FAIL_INSEN｜1,132円｜💰11.6万円｜—｜⚠日程不明
- 3549 クスリのアオキホールディングス｜granville_tenkan｜✅順調｜🔴過熱｜PASS｜4,505円｜💰45.0万円｜提案あり｜⚠日程不明
  > 【業態】ドラッグストア中堅。北陸で首位。調剤併設店主軸に食品・生活必需品を拡大。
  > 【いま】終値4,505円・直近5日+1.72%（材料未確認）
  > 【調子】✅順調（4/13）
  > 【水準】🔴過熱（1.0/7）— PER22.51倍・PEG2.0277・52週78.8% ／ 💰単元45.0万円
  > 【戦略】当日高値超えの逆指値4,510円で順張り参戦を検討。上限4,555.1円・SL4,234.7円目安
- 5184 ニチリン｜granville_tenkan｜✅順調｜🔴過熱｜FAIL_INSEN｜4,135円｜💰41.7万円｜—｜📐進捗 上振れ +23.8%｜⚡材料後出し｜🔁
- 8113 Unicharm Corporation｜granville_tenkan｜✅順調｜🔴過熱｜FAIL_UWAHIGE｜1,027円｜💰10.1万円｜—｜⏰決算 11/06(残3営業日)
- 8160 KISOJI CO., LTD.｜granville_tenkan｜✅順調｜🔴過熱｜FAIL_INSEN｜2,464円｜💰24.7万円｜—｜⏰決算 11/10(残5営業日)
- 4166 Cacco, Inc.｜granville_tenkan｜✅順調｜💎割安｜FAIL_INSEN｜680円｜💰6.8万円｜—
- 2897 Nissin Foods Holdings Co., Ltd.｜granville_tenkan｜✅順調｜⚪妥当｜FAIL_INSEN｜3,050円｜💰30.4万円｜—｜⚡材料後出し｜📌
- 9163 Nareru Group Inc.｜granville_tenkan｜✅順調｜⚪妥当｜FAIL_INSEN｜2,070円｜💰22.7万円｜—｜⚠日程不明
- 186A Astroscale Holdings Inc.｜granville_tenkan｜✅順調｜🔴過熱｜FAIL_INSEN｜1,051円｜💰11.6万円｜—｜⚠日程不明
- 3569 セーレン｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_INSEN｜3,350円｜💰33.9万円｜—｜⏰決算 11/10(残5営業日)｜⚡材料後出し｜🔁
- 4183 Mitsui Chemicals, Inc.｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_UWAHIGE｜2,070.5円｜💰20.9万円｜—
- 4272 Nippon Kayaku Co., Ltd.｜granville_tenkan/granville_oshime｜✅順調｜🟡やや割高｜FAIL_UWAHIGE｜2,008.5円｜💰20.0万円｜—｜⏰決算 11/10(残5営業日)
- 7269 スズキ｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_INSEN｜2,096円｜💰20.9万円｜—｜⏰決算 11/10(残5営業日)
- 5461 Chubu Steel Plate Co., Ltd.｜granville_tenkan｜🔻悪化｜🔴過熱｜PASS｜2,198円｜💰22.0万円｜⛔提案なし(指名鮮度切れ 11営業日)｜📑TOPIX低減対象（次 01/29 第2回/8）｜⏰決算 11/06(残3営業日)｜⚠業績基調が下向き（悪化）
  > 【業態】電炉中堅、厚中板専業。産業・工作機械向け。エンジニアリング、物流、レンタルも。
  > 【いま】終値2,198円・直近5日-0.68%（材料未確認）
  > 【調子】🔻悪化（3/13） — E軸判定不能(進捗データ取得不可)、質注意、経常減益-46.1%
  > 【水準】🔴過熱（1.0/7）— PER194.51倍・PEG—・52週41.3% ／ 💰単元22.0万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 11営業日)）
- 7513 Kojima Co., Ltd.｜granville_tenkan｜✅順調｜🔴過熱｜FAIL_INSEN｜1,362円｜💰13.8万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚠日程不明
- 7734 Riken Keiki Co., Ltd.｜granville_tenkan｜✅順調｜🔴過熱｜PASS｜3,470円｜💰34.7万円｜提案あり
  > 【業態】産業用ガス保安器・計測器で首位。公害監視装置に強み。防災関連に注力。
  > 【いま】終値3,470円・直近5日+1.76%（材料未確認）
  > 【調子】✅順調（3/13） — E軸判定不能(進捗データ不足)、質注意
  > 【水準】🔴過熱（1.0/7）— PER16.43倍・PEG—・52週55.1% ／ 💰単元34.7万円
  > 【戦略】当日高値超えの逆指値3,480円で順張り参戦を検討。上限3,514.8円・SL3,266.5円目安
- 8012 Nagase & Co., Ltd.｜granville_tenkan｜✅順調｜🔴過熱｜FAIL_UWAHIGE｜1,258円｜💰12.6万円｜—｜⏰決算 11/06(残3営業日)｜📐進捗 上振れ +53.3%
- 2811 Kagome Co., Ltd.｜granville_tenkan｜➖横ばい｜⚪妥当｜FAIL_UWAHIGE｜2,773.5円｜💰27.4万円｜—｜⚠日程不明
- 5233 太平洋セメント｜granville_tenkan｜➖横ばい｜⚪妥当｜PASS｜4,281円｜💰42.8万円｜提案あり｜⏰決算 11/10(残5営業日)｜📐進捗 上振れ +32.1%
  > 【業態】セメント最大手。海外にも展開。建材や電材など多角化。産廃・再資源化も。
  > 【いま】終値4,281円・直近5日+2.86%（材料未確認）
  > 【調子】➖横ばい（2/13） — E軸:進捗17.6%>=前年同期13.3%、経常減益-6.8%、質注意
  > 【水準】⚪妥当（3.0/7）— PER7.41倍・PEG—・52週59.7% ／ 💰単元42.8万円
  > 【戦略】当日高値超えの逆指値4,288円で順張り参戦を検討。上限4,330.9円・SL4,026円目安
- 6196 Strike Group Co. Ltd.｜granville_tenkan｜➖横ばい｜⚪妥当｜PASS｜1,713円｜💰17.1万円｜提案あり｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚠日程不明
  > 【業態】公認会計士、税理士主体のM&A仲介業務。ネット活用のマッチングシステムに強み。
  > 【いま】終値1,713円・直近5日+20.72%（材料未確認）
  > 【調子】➖横ばい（2/13） — D軸判定不能(直近Qデータ取得不可)、E軸判定不能(期首・進捗なし)
  > 【水準】⚪妥当（3.0/7）— PER12.55倍・PEG1.2275・52週100.0% ／ 💰単元17.1万円
  > 【戦略】当日高値超えの逆指値1,714円で順張り参戦を検討。上限1,731.1円・SL1,610.2円目安
- 6328 Ebara Jitsugyo Co., Ltd.｜granville_tenkan｜➖横ばい｜⚪妥当｜PASS｜2,463円｜💰24.6万円｜提案あり｜📑TOPIX低減対象（次 01/29 第2回/8）｜⏰決算 11/05(残2営業日)
  > 【業態】上下水処理施設から空調など環境関連事業に拡大。研究開発・ファブレス型。
  > 【いま】終値2,463円・直近5日-0.08%（材料未確認）
  > 【調子】➖横ばい（2/13） — 質注意
  > 【水準】⚪妥当（3.0/7）— PER12.87倍・PEG4.4172・52週46.3% ／ 💰単元24.6万円
  > 【戦略】当日高値超えの逆指値2,478円で順張り参戦を検討。上限2,502.8円・SL2,328.4円目安
- 6770 Alps Alpine Co., Ltd.｜granville_tenkan｜➖横ばい｜⚪妥当｜FAIL_INSEN｜1,856.5円｜💰20.9万円｜—｜⚠日程不明｜📐進捗 遅れ -13.3%
- 8081 Kanaden Corporation｜granville_tenkan｜➖横ばい｜🟡やや割高｜FAIL_INSEN｜2,484円｜💰26.0万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜🚨決算直前 11/04(残1営業日)
- 9837 Morito Co., Ltd.｜granville_tenkan｜➖横ばい｜🟡やや割高｜FAIL_INSEN｜1,800円｜💰18.1万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚠日程不明
- 4922 コーセーホールディングス｜granville_tenkan｜➖横ばい｜🔴過熱｜FAIL_INSEN｜5,999円｜💰60.1万円｜—｜⏰決算 11/10(残5営業日)
- 4902 Konica Minolta, Inc.｜granville_tenkan｜⚠減速｜🟢値頃｜FAIL_INSEN｜656円｜💰6.6万円｜—｜⏰決算 11/05(残2営業日)｜⚠業績基調が下向き（減速）
- 4552 JCR Pharmaceuticals Co., Ltd.｜granville_tenkan｜🔻悪化｜🔴過熱｜FAIL_INSEN｜514円｜💰5.4万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚠日程不明｜⚠業績基調が下向き（悪化）｜📐進捗 遅れ -15.4%
- 5105 ＴＯＹＯ　ＴＩＲＥ｜granville_tenkan｜⚠減速｜🟡やや割高｜FAIL_INSEN｜3,981円｜💰40.3万円｜—｜⚠業績基調が下向き（減速）
- 8167 リテールパートナーズ｜granville_tenkan｜⚠減速｜🟡やや割高｜FAIL_INSEN｜1,372円｜💰13.8万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚠日程不明｜⚠業績基調が下向き（減速）｜📐進捗 遅れ -18.2%
- 4375 セーフィー｜changepoint/granville_tenkan/changepoint🔔｜取得不可｜💎割安｜FAIL_INSEN｜636円｜💰6.4万円｜—｜⚠日程不明
- 4005 住友化学｜granville_tenkan｜業績データ取得不可(経常益予想非開示)｜🟢値頃｜FAIL_INSEN｜511.5円｜💰5.7万円｜—｜🚨決算直前 11/02(残0営業日)｜📊
- 7921 ＴＡＫＡＲＡ　＆　ＣＯＭＰＡＮＹ｜granville_tenkan｜業績データ取得不可(経常益予想非開示)｜🟢値頃｜FAIL_UWAHIGE｜4,205円｜💰41.9万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚠日程不明
- 4912 ライオン｜granville_tenkan｜業績データ取得不可(経常益予想非開示)｜⚪妥当｜FAIL_INSEN｜1,838円｜💰18.3万円｜—｜⏰決算 11/06(残3営業日)
- 3563 ＦＯＯＤ　＆　ＬＩＦＥ　ＣＯＭＰＡＮＩＥＳ｜granville_tenkan｜判定保留(データ不足)｜🟡やや割高｜FAIL_UWAHIGE｜5,808円｜💰58.1万円｜—｜⏰決算 11/06(残3営業日)
- 1928 積水ハウス｜granville_tenkan｜—｜—｜FAIL_INSEN｜3,482円｜💰—｜—｜⚠日程不明
- 1941 中電工｜granville_tenkan｜—｜—｜FAIL_INSEN｜5,190円｜💰—｜—｜⚠日程不明
- 3002 グンゼ｜granville_tenkan｜—｜—｜FAIL_INSEN｜4,095円｜💰—｜—｜⏰決算 11/05(残2営業日)
- 4403 日油｜granville_tenkan｜—｜—｜FAIL_INSEN｜2,754.5円｜💰—｜—｜⏰決算 11/05(残2営業日)
- 4937 Ｇ−ＷＡＱＯＯ｜granville_oshime｜🚀確変｜⚪妥当｜PASS｜2,278円｜💰22.8万円｜⛔提案なし(指名鮮度切れ 19営業日)
  > 【業態】化粧品の企画・開発・販売。血液由来加工受託や再生医療関連にも進出。
  > 【いま】終値2,278円・直近5日-2.57%（材料未確認）
  > 【調子】🚀確変（13/13） — 上方修正済み、進捗74%(前年同期-22%・3Q累計・経常ベース)
  > 【水準】⚪妥当（3.0/7）— PER19.79倍・PEG0.0756・52週81.6% ／ 💰単元22.8万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 19営業日)）
- 5243 ｎｏｔｅ｜granville_oshime/granville_rebound｜🚀確変｜⚪妥当｜FAIL_UWAHIGE｜2,944円｜💰28.5万円｜—｜⚠日程不明
- 7806 MTG Co., Ltd.｜changepoint/granville_oshime/changepoint🔔/changepoint🔔🔔｜🚀確変｜⚪妥当｜PASS｜9,040円｜💰90.4万円｜提案あり
  > 【業態】美容ローラー「ReFa」・健康機器「SIXPAD」など健康美容関連の企画開発・販売。
  > 【いま】終値9,040円・直近5日+3.08%（材料未確認）
  > 【調子】🚀確変（11/13）
  > 【水準】⚪妥当（3.0/7）— PER32.34倍・PEG0.6587・52週92.3% ／ 💰単元90.4万円
  > 【戦略】8,756円までの押し目を指値で待つ。SL8,712.4円（25日線基準）
- 6834 精工技研｜granville_oshime/granville_rebound｜🔥絶好調｜💎割安｜FAIL_UWAHIGE｜6,290円｜💰61.3万円｜—
- 6080 Ｍ＆Ａキャピタルパートナーズ｜changepoint/changepoint🔔/granville_oshime｜🔥絶好調｜⚪妥当｜PASS｜4,195円｜💰42.0万円｜⛔型不一致: 既に支持帯以下｜⚠日程不明
  > 【業態】独立系の中小向けM&A仲介サービス会社。事業売却・買収、事業承継に強み。
  > 【いま】終値4,195円・直近5日+0.84%（材料未確認）
  > 【調子】🔥絶好調（10/13）
  > 【水準】⚪妥当（3.0/7）— PER17.36倍・PEG0.3217・52週82.3% ／ 💰単元42.0万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 8008 Yondoshi Holdings, Inc.｜granville_oshime｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1,942円｜💰19.4万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚠日程不明
- 8137 サンワテクノス｜granville_oshime/granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜4,015円｜💰41.8万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚠日程不明
- 4382 HEROZ, Inc.｜changepoint/changepoint🔔/changepoint🔔🔔/granville_oshime｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜906円｜💰9.7万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚠日程不明
- 3156 レスター｜granville_oshime｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜5,520円｜💰56.7万円｜—
- 8051 山善｜granville_oshime｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜1,867円｜💰19.1万円｜—｜📐進捗 上振れ +22.8%
- 4180 ＡＰＰＩＥＲ　ＧＲＯＵＰ｜changepoint/changepoint🔔/granville_oshime/changepoint🔔🔔｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜1,414円｜💰14.5万円｜—
- 7856 HAGIHARA INDUSTRIES INC.｜granville_oshime｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜1,888円｜💰19.2万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚠日程不明
- 4431 Smaregi, Inc.｜changepoint/変化点🔔🔔/changepoint🔔/granville_oshime｜🔥絶好調｜🟡やや割高｜FAIL_INSEN｜3,785円｜💰37.9万円｜—｜⚠日程不明
- 4471 三洋化成工業｜granville_oshime｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜1,596円｜💰16.4万円｜—｜⏰決算 11/10(残5営業日)
- 5892 ＹＵＴＯＲＩ｜granville_oshime｜⚡好調｜🟢値頃｜FAIL_INSEN｜2,510円｜💰25.4万円｜—
- 6036 ＫｅｅＰｅｒ技研｜granville_oshime｜⚡好調｜🟢値頃｜FAIL_INSEN｜1,818円｜💰18.5万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 9902 Nichiden Corporation｜granville_oshime｜⚡好調｜🟢値頃｜FAIL_INSEN｜3,065円｜💰30.7万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⏰決算 11/05(残2営業日)
- 3040 ソリトンシステムズ｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,942円｜💰30.3万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 6736 Suncorporation｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜9,630円｜💰102.7万円｜—
- 6523 ＰＨＣホールディングス｜granville_oshime｜⚠減速｜🟢値頃｜PASS｜1,405円｜💰14.1万円｜⛔型不一致: 既に支持帯以下｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚠業績基調が下向き（減速）
  > 【業態】各種ヘルスケア機器・サービスの開発・製造販売。糖尿病ケアに強み。ファンド傘下。
  > 【いま】終値1,405円・直近5日+11.60%（材料未確認）
  > 【調子】⚠減速（6/13） — E軸判定不能(進捗データ不足)、減収、質注意
  > 【水準】🟢値頃（5.0/7）— PER11.59倍・PEG0.0475・52週61.6% ／ 💰単元14.1万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 7609 ダイトロン｜granville_oshime｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜3,965円｜💰40.0万円｜—｜🚨決算直前 11/04(残1営業日)
- 3106 倉敷紡績｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,247円｜💰23.1万円｜—
- 6250 Yamabiko Corporation｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜4,245円｜💰42.4万円｜—
- 9552 クオンツ総研ホールディングス｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜1,035円｜💰12.0万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 2602 日清オイリオグループ｜granville_oshime｜⚡好調｜🟡やや割高｜FAIL_INSEN｜2,054円｜💰20.5万円｜—｜⏰決算 11/09(残4営業日)
- 4413 baudroie,inc.｜granville_oshime｜⚡好調｜🟡やや割高｜FAIL_INSEN｜2,937円｜💰29.4万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚠日程不明
- 6570 Kyowa Corporation Co. Ltd.｜granville_oshime｜⚡好調｜🟡やや割高｜FAIL_INSEN｜3,975円｜💰41.9万円｜—
- 8410 Seven Bank, Ltd.｜granville_oshime｜⚡好調｜🔴過熱｜FAIL_INSEN｜335.3円｜💰3.4万円｜—｜⏰決算 11/06(残3営業日)｜📐進捗 上振れ +41.6%
- 9304 澁澤倉庫｜granville_oshime｜⚡好調｜⏸判定不能｜FAIL_INSEN｜1,962円｜💰20.1万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⏰決算 11/09(残4営業日)
- 6340 澁谷工業｜granville_oshime｜⚡好調｜🟢値頃｜PASS｜5,240円｜💰52.4万円｜⛔型不一致: 既に支持帯以下｜⏰決算 11/09(残4営業日)
  > 【業態】飲料用充填装置の最大手。無菌充填機に定評。メカトロシステム製販、農業設備も。
  > 【いま】終値5,240円・直近5日-0.19%（材料未確認）
  > 【調子】⚡好調（5/13） — E軸判定不能(期首・進捗なし)
  > 【水準】🟢値頃（5.0/7）— PER13.18倍・PEG0.6769・52週71.1% ／ 💰単元52.4万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 8392 大分銀行｜granville_rebound/granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,709円｜💰28.9万円｜—｜⏰決算 11/09(残4営業日)
- 7350 Okinawa Financial Group, Inc.｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜6,900円｜💰71.9万円｜—
- 9536 SAIBU GAS HOLDINGS CO. LTD.｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,788円｜💰27.9万円｜—｜⚠日程不明
- 6191 エボラブルアジア｜granville_oshime｜🔻悪化｜🔴過熱｜FAIL_INSEN｜1,392円｜💰14.5万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚠日程不明｜⚠業績基調が下向き（悪化）
- 4475 HENNGE K.K.｜granville_oshime｜⚡好調｜🔴過熱｜FAIL_INSEN｜2,022円｜💰23.2万円｜—｜⏰決算 11/05(残2営業日)
- 8395 佐賀銀行｜granville_oshime｜⚠減速｜⚪妥当｜FAIL_INSEN｜6,120円｜💰65.0万円｜—｜⏰決算 11/06(残3営業日)｜⚠業績基調が下向き（減速）
- 3097 Monogatari Corporation｜granville_oshime｜✅順調｜🔴過熱｜FAIL_INSEN｜5,970円｜💰58.4万円｜—
- 6418 Japan Cash Machine Co., Ltd.｜granville_oshime｜✅順調｜🔴過熱｜FAIL_INSEN｜1,229円｜💰12.5万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⏰決算 11/10(残5営業日)
- 6998 Nippon Tungsten Co., Ltd.｜granville_oshime｜✅順調｜🔴過熱｜FAIL_UWAHIGE｜2,866円｜💰31.6万円｜—
- 5985 SUNCALL CORPORATION｜granville_oshime｜✅順調｜🟢値頃｜FAIL_UWAHIGE｜1,816円｜💰18.5万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 9509 Hokkaido Electric Power Company,Incorporated｜granville_oshime｜🔻悪化｜⚪妥当｜PASS｜1,088.5円｜💰10.9万円｜⛔型不一致: 既に支持帯以下｜⚠日程不明｜⚠業績基調が下向き（悪化）｜📐進捗 遅れ -32.9%
  > 【業態】原子力と石炭火力が主力。需要は冬ピーク。原発3基が停止、再稼働目指す。
  > 【いま】終値1,088.5円・直近5日-0.64%（材料未確認）
  > 【調子】🔻悪化（3/13） — 上方修正済み、質注意
  > 【水準】⚪妥当（3.0/7）— PER7.08倍・PEG—・52週49.4% ／ 💰単元10.9万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 1518 三井松島ホールディングス｜granville_oshime｜✅順調｜🟡やや割高｜FAIL_UWAHIGE｜2,246円｜💰22.5万円｜—
- 4208 UBE Corporation｜granville_oshime｜✅順調｜🟡やや割高｜FAIL_UWAHIGE｜3,250円｜💰32.9万円｜—｜⏰決算 11/05(残2営業日)｜⚡材料後出し｜📌
- 9044 NANKAI Co., Ltd.｜granville_oshime｜✅順調｜🟡やや割高｜FAIL_INSEN｜2,950.5円｜💰30.3万円｜—｜🚨決算直前 11/02(残0営業日)｜📊
- 3107 ダイワボウホールディングス｜granville_oshime｜⚠減速｜🔴過熱｜FAIL_UWAHIGE｜3,753円｜💰38.6万円｜—｜⚠業績基調が下向き（減速）
- 338A ZenmuTech,Inc.｜granville_oshime｜✅順調｜🔴過熱｜FAIL_INSEN｜4,180円｜💰42.6万円｜—｜📐進捗 遅れ -20.9%｜📌
- 4044 Central Glass Co., Ltd.｜granville_oshime｜✅順調｜🔴過熱｜FAIL_UWAHIGE｜4,430円｜💰45.1万円｜—
- 456A Human Made Inc.｜granville_oshime｜✅順調｜🔴過熱｜FAIL_INSEN｜2,163円｜💰21.2万円｜—｜⚠日程不明
- 9505 Hokuriku Electric Power Company｜granville_oshime｜🔻悪化｜⚪妥当｜FAIL_INSEN｜1,068.5円｜💰10.8万円｜—｜⚠日程不明｜⚠業績基調が下向き（悪化）｜📐進捗 上振れ +49.5%
- 3692 ＦＦＲＩセキュリティ｜granville_oshime｜➖横ばい｜🔴過熱｜FAIL_INSEN｜7,600円｜💰77.0万円｜—｜📐進捗 遅れ -35.7%
- 7630 Ichibanya Co., Ltd.｜granville_oshime｜➖横ばい｜🔴過熱｜PASS｜1,059円｜💰10.6万円｜⛔型不一致: 既に支持帯以下｜⚠日程不明
  > 【業態】カレー専門店を直営・FCで全国展開。海外出店を加速。パスタなど新業態も。
  > 【いま】終値1,059円・直近5日-1.76%（材料未確認）
  > 【調子】➖横ばい（2/13） — 質注意
  > 【水準】🔴過熱（1.0/7）— PER62.29倍・PEG56.4611・52週62.4% ／ 💰単元10.6万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 8043 Starzen Company Limited｜granville_oshime｜➖横ばい｜🔴過熱｜FAIL_INSEN｜1,560円｜💰15.6万円｜—｜⏰決算 11/10(残5営業日)｜📌
- 8255 Axial Retailing, Inc.｜granville_oshime｜⚠減速｜🔴過熱｜FAIL_UWAHIGE｜1,352円｜💰13.5万円｜—｜🚨決算直前 11/04(残1営業日)｜⚠業績基調が下向き（減速）
- 8097 SAN-AI OBBLI CO. LTD｜granville_oshime｜⚠減速｜🔴過熱｜FAIL_INSEN｜2,420円｜💰25.0万円｜—｜⏰決算 11/10(残5営業日)｜⚠業績基調が下向き（減速）
- 9166 GENDA Inc.｜granville_oshime｜業績データ取得不可｜💎割安｜FAIL_UWAHIGE｜608円｜💰6.0万円｜—｜⚠日程不明
- 8361 Ogaki Kyoritsu Bank, Ltd.｜granville_oshime/granville_rebound｜取得不可｜💎割安｜FAIL_INSEN｜1,487円｜💰15.6万円｜—
- 8343 Akita Bank, Ltd.｜granville_oshime/granville_rebound｜業績データ取得不可(売上/経常欠損)｜🟢値頃｜FAIL_INSEN｜1,459円｜💰15.4万円｜—
- 3993 PKSHA Technology, Inc.｜changepoint/changepoint🔔/granville_oshime｜業績データ取得不可｜⚪妥当｜FAIL_INSEN｜3,450円｜💰35.9万円｜—
- 6027 Bengo4.com, Inc.｜granville_oshime｜業績データ取得不可｜🟡やや割高｜FAIL_INSEN｜4,640円｜💰47.1万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚡材料後出し｜🔁
- 8362 Fukui Bank, Ltd.｜granville_oshime｜🔻悪化｜🔴過熱｜FAIL_INSEN｜6,730円｜💰70.7万円｜—｜⚠業績基調が下向き（悪化）
- 7480 スズデン｜granville_rebound｜🚀確変｜🟢値頃｜PASS_DOJI｜3,360円｜💰33.6万円｜⛔提案なし(材料後出し)｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚠日程不明｜⚡材料後出し｜📊
  > 【業態】FA機器主力、技術商社。オムロンと特約店契約。電設資材中心。ネット販売に強み。
  > 【いま】終値3,360円・直近5日-6.93%・📊2027年３月期第２四半期（中間期）決算短信〔日本基準〕(連結)
  > 【調子】🚀確変（13/13）
  > 【水準】🟢値頃（5.0/7）— PER15.33倍・PEG0.1866・52週73.5% ／ 💰単元33.6万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 3778 SAKURA Internet Inc.｜granville_rebound｜🚀確変｜🟢値頃｜FAIL_INSEN｜2,991円｜💰30.4万円｜—
- 3891 ニッポン高度紙工業｜granville_rebound｜🚀確変｜🟢値頃｜FAIL_UWAHIGE｜6,150円｜💰60.8万円｜—｜⚠日程不明｜📐進捗 遅れ -10.4%
- 6769 Thine Electronics, Inc.｜granville_rebound｜🚀確変｜⚪妥当｜FAIL_UWAHIGE｜992円｜💰10.1万円｜—｜⏰決算 11/05(残2営業日)
- 8704 TRADERS HOLDINGS CO LTD｜changepoint/changepoint🔔/granville_rebound｜🔥絶好調｜💎割安｜FAIL_INSEN｜1,232円｜💰12.2万円｜—｜⚠日程不明｜📐進捗 上振れ +44.7%
- 3691 DIGITAL PLUS, Inc.｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜1,313円｜💰13.4万円｜—
- 479A PRONI Inc.｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1,626円｜💰17.0万円｜—
- 5381 Mipox Corp.｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜908円｜💰9.4万円｜—｜⚠日程不明｜📐進捗 上振れ +10.3%
- 2962 テクニスコ｜granville_rebound｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜1,760円｜💰18.0万円｜—
- 4419 Finatext Holdings Ltd.｜granville_rebound｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜1,302円｜💰13.1万円｜—｜📌
- 1436 GreenEnergy & Company｜granville_rebound｜🔥絶好調｜💎割安｜FAIL_INSEN｜1,348円｜💰13.9万円｜—｜⚠日程不明
- 3793 Drecom Co., Ltd.｜granville_rebound｜⚠減速｜💎割安｜PASS｜444円｜💰4.4万円｜提案あり｜⚠日程不明｜⚠業績基調が下向き（減速）｜📐進捗 上振れ +25.6%
  > 【業態】スマホゲーム開発・運用を軸にアニメ等他社配信。ITサービスから出版・映像事業も。
  > 【いま】終値444円・直近5日-11.73%（材料未確認）
  > 【調子】⚠減速（9/13） — 上方修正済み
  > 【水準】💎割安（6.0/7）— PER13.96倍・PEG0.0534・52週34.8% ／ 💰単元4.4万円
  > 【戦略】当日終値444円の指値で反転を取りにいく。SL428円（直近5日安値）
- 8084 ＲＹＯＤＥＮ｜granville_rebound｜🔥絶好調｜💎割安｜PASS_DOJI｜2,217円｜💰22.2万円｜提案あり｜⚠日程不明
  > 【業態】三菱電機系最大商社。半導体、冷熱住機、ビル昇降機など他社も幅広く展開。
  > 【いま】終値2,217円・直近5日-12.54%（材料未確認）
  > 【調子】🔥絶好調（9/13）
  > 【水準】💎割安（6.0/7）— PER7.95倍・PEG0.2647・52週65.6% ／ 💰単元22.2万円
  > 【戦略】当日終値2,217円の指値で反転を取りにいく。SL2,101円（直近5日安値）
- 4968 Arakawa Chemical Industries,Ltd.｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜2,058円｜💰19.4万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⏰決算 11/05(残2営業日)
- 6963 ROHM Company Limited｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜3,554円｜💰35.7万円｜—｜⏰決算 11/05(残2営業日)
- 8995 Makoto Construction Co,Ltd｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1,565円｜💰15.7万円｜—
- 150A ＪＳＨ｜granville_rebound｜🔥絶好調｜⚪妥当｜PASS｜575円｜💰5.8万円｜提案あり｜📌
  > 【業態】障がい者雇用支援の農園や訪問看護・診療サービスなどを手掛ける。
  > 【いま】終値575円・直近5日-6.66%・📌事業所の統廃合及び移転に関するお知らせ
  > 【調子】🔥絶好調（9/13） — E軸判定不能(進捗データ不足)
  > 【水準】⚪妥当（4.0/7）— PER16.96倍・PEG0.0382・52週44.6% ／ 💰単元5.8万円
  > 【戦略】当日終値575円の指値で反転を取りにいく。SL533円（直近5日安値）
- 7715 長野計器｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜3,715円｜💰37.5万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜📐進捗 上振れ +10.5%
- 8364 清水銀行｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜2,739円｜💰28.4万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 5367 Nikkato Corporation｜granville_rebound｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜1,201円｜💰11.6万円｜—｜🚨決算直前 11/02(残0営業日)｜📐進捗 上振れ +75.9%｜⚡材料後出し｜📊
- 6508 Meidensha Corporation｜granville_rebound｜⚡好調｜🟢値頃｜PASS_DOJI｜8,677円｜💰86.8万円｜提案あり｜⚠日程不明｜⚠1単元でリスク枠超過（39,700円）
  > 【業態】住友系・老舗重電。電力・エネルギー、水処理制御システム、電鉄用、車電動化に強み。
  > 【いま】終値8,677円・直近5日-10.08%（材料未確認）
  > 【調子】⚡好調（7/13） — 上方修正済み、進捗モデル値域外
  > 【水準】🟢値頃（5.0/7）— PER15.14倍・PEG0.5937・52週44.5% ／ 💰単元86.8万円
  > 【戦略】当日終値8,677円の指値で反転を取りにいく。SL8,280円（直近5日安値）／⚠1単元リスク39,700円（枠超過）
- 6490 ＰＩＬＬＡＲ｜granville_rebound｜⚡好調｜⚪妥当｜PASS｜9,960円｜💰99.6万円｜提案あり｜⚠1単元でリスク枠超過（35,000円）
  > 【業態】流体制御関連のメカニカルシール大手。パッキン、ガスケットなど産業機械向け拡大。
  > 【いま】終値9,960円・直近5日+3.53%（材料未確認）
  > 【調子】⚡好調（7/13） — E軸判定不能(進捗データ不足)
  > 【水準】⚪妥当（4.0/7）— PER16.27倍・PEG0.2826・52週64.4% ／ 💰単元99.6万円
  > 【戦略】当日終値9,960円の指値で反転を取りにいく。SL9,610円（直近5日安値）／⚠1単元リスク35,000円（枠超過）
- 9697 カプコン｜granville_rebound｜⚡好調｜🟡やや割高｜FAIL_INSEN｜3,878円｜💰39.6万円｜—｜⚠日程不明｜📌
- 5242 EYEZ INC.｜granville_rebound｜⚡好調｜🔴過熱｜FAIL_INSEN｜2,791円｜💰30.0万円｜—
- 477A Startline CO.,LTD.｜granville_rebound｜⚡好調｜💎割安｜FAIL_INSEN｜715円｜💰7.5万円｜—｜📌
- 6336 石井表記｜granville_rebound｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜1,271円｜💰13.0万円｜—｜⚠日程不明
- 2354 YE DIGITAL CORPORATION｜granville_rebound｜⚡好調｜💎割安｜FAIL_INSEN｜953円｜💰10.4万円｜—｜⚠日程不明
- 4100 Toda Kogyo Corp.｜granville_rebound｜⚡好調｜🟢値頃｜PASS｜1,757円｜💰17.6万円｜提案あり｜📑TOPIX低減対象（次 01/29 第2回/8）
  > 【業態】磁性粉末材料で首位。機能性顔料に強み。リチウムイオン電池正極材注力。TDK系。
  > 【いま】終値1,757円・直近5日+11.70%（材料未確認）
  > 【調子】⚡好調（5/13） — 黒字転換、E軸判定不能(進捗データ不足)、D軸判定不能(四半期データ不足・中立1点)
  > 【水準】🟢値頃（5.6/7）— PER20.34倍・PEG0.0133・52週59.5% ／ 💰単元17.6万円
  > 【戦略】当日終値1,757円の指値で反転を取りにいく。SL1,591円（直近5日安値）
- 8344 Yamagata Bank, Ltd.｜granville_rebound｜⚡好調｜🟢値頃｜FAIL_INSEN｜4,360円｜💰46.2万円｜—
- 6597 HPC SYSTEMS Inc.｜changepoint/changepoint🔔/changepoint🔔🔔/granville_rebound｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜2,894円｜💰29.7万円｜—
- 3687 Fixstars Corp.｜granville_rebound｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜1,749円｜💰17.7万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⏰決算 11/06(残3営業日)
- 5574 ABEJA,Inc.｜granville_rebound｜⚡好調｜🟡やや割高｜FAIL_INSEN｜2,154円｜💰23.6万円｜—｜⚠日程不明
- 9278 BOOKOFF GROUP HOLDINGS LIMITED｜granville_rebound｜⚡好調｜🟡やや割高｜FAIL_UWAHIGE｜2,378円｜💰23.8万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚠日程不明
- 7256 河西工業｜granville_rebound｜⚡好調｜🔴過熱｜FAIL_INSEN｜389円｜💰—｜—
- 4997 日本農薬｜granville_rebound｜✅順調｜🟡やや割高｜FAIL_INSEN｜1,064円｜💰10.7万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⏰決算 11/10(残5営業日)
- 278A Ｔｅｒｒａ　Ｄｒｏｎｅ｜granville_rebound｜✅順調｜⏸判定不能｜FAIL_UWAHIGE｜5,990円｜💰—｜—｜⚠日程不明｜⚡材料後出し｜📌
- 2681 2nd RETAILING Co., Ltd.｜granville_rebound｜✅順調｜⚪妥当｜PASS_DOJI｜1,887円｜💰18.9万円｜⛔提案なし(指名鮮度切れ 17営業日)｜📑TOPIX低減対象（次 01/29 第2回/8）｜⏰決算 11/06(残3営業日)
  > 【業態】映像レンタル店を直営軸に全国展開。ゲーム・スマホ、衣料品の中古品販売が主力に。
  > 【いま】終値1,887円・直近5日-5.56%（材料未確認）
  > 【調子】✅順調（3/13） — E軸判定不能(進捗データ不足)、質注意
  > 【水準】⚪妥当（3.0/7）— PER12.51倍・PEG—・52週33.0% ／ 💰単元18.9万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 17営業日)）
- 3907 Silicon Studio Corp.｜granville_rebound｜🔻悪化｜💎割安｜FAIL_INSEN｜1,193円｜💰12.9万円｜—｜⚠日程不明｜⚠業績基調が下向き（悪化）
- 4440 WITZ Corp.｜granville_rebound｜➖横ばい｜⚪妥当｜FAIL_INSEN｜1,608円｜💰16.7万円｜—｜⚠日程不明｜📌
- 4691 Washington Hotel Corp.｜granville_rebound｜⚠減速｜⚪妥当｜FAIL_UWAHIGE｜1,767円｜💰18.3万円｜—｜⚠業績基調が下向き（減速）
- 6203 Howa Machinery, Ltd.｜granville_rebound｜⚠減速｜🟡やや割高｜FAIL_UWAHIGE｜2,034円｜💰20.0万円｜—｜⚠業績基調が下向き（減速）
- 6522 アスタリスク｜granville_rebound｜⚠減速｜🟢値頃｜FAIL_UWAHIGE｜753円｜💰8.1万円｜—｜⚠日程不明｜⚠業績基調が下向き（減速）
- 8360 Yamanashi Chuo Bank, Ltd.｜granville_rebound｜取得不可｜💎割安｜FAIL_INSEN｜1,266円｜💰13.0万円｜—
- 7380 Juroku Financial Group,Inc.｜granville_rebound｜取得不可｜⚪妥当｜FAIL_INSEN｜2,303円｜💰24.2万円｜—｜⏰決算 11/09(残4営業日)
- 8368 Hyakugo Bank, Ltd.｜granville_rebound｜取得不可｜🟡やや割高｜FAIL_INSEN｜2,059.5円｜💰21.4万円｜—｜⏰決算 11/10(残5営業日)
- 8713 Fidea Holdings Co.Ltd.｜granville_rebound｜業績データ取得不可(売上/経常欠損)｜🔴過熱｜FAIL_INSEN｜2,481円｜💰26.0万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）
- 4075 ブレインズテクノロジー｜granville_rebound｜—｜—｜FAIL_INSEN｜1,091円｜💰—｜—｜⚠日程不明
- 460A ＢＲＡＮＵ｜granville_rebound｜—｜—｜FAIL_INSEN｜975円｜💰—｜—｜⚠日程不明｜📌
- 6840 ＡＫＩＢＡホールディングス｜granville_rebound｜業績データ取得不可｜⏸判定不能｜FAIL_UWAHIGE｜675円｜💰6.8万円｜—
- 6890 Ferrotec Corporation｜granville_rebound｜業績データ取得不可｜⏸判定不能｜FAIL_UWAHIGE｜7,631円｜💰76.7万円｜—｜⚡材料後出し｜📌
- 7175 Imamura Securities Co.Ltd.｜granville_rebound｜業績データ取得不可｜⏸判定不能｜PASS｜1,647円｜💰16.5万円｜提案あり｜⚠日程不明
  > 【業態】富山、石川、福井の北陸３県が地盤の老舗証券会社。ネットと対面営業。
  > 【いま】終値1,647円・直近5日-2.08%（材料未確認）
  > 【調子】業績データ取得不可（—/13） — 通期予想が非開示(会社側未公表)
  > 【水準】⏸判定不能（—/7）— PER—倍・PEG—・52週48.5% ／ 💰単元16.5万円
  > 【戦略】当日終値1,647円の指値で反転を取りにいく。SL1,610円（直近5日安値）
- 8377 ほくほくフィナンシャルグループ｜granville_rebound｜業績データ取得不可｜⏸判定不能｜FAIL_UWAHIGE｜731.9円｜💰7.5万円｜—｜⏰決算 11/09(残4営業日)｜⚡材料後出し｜📌
- 8609 岡三証券グループ｜granville_rebound｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜1,001円｜💰10.1万円｜—｜⚠日程不明
- 8739 スパークス・グループ｜granville_rebound｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜2,298円｜💰23.7万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚠日程不明

## 変化点銘柄
- 265A エイチエムコム｜changepoint/changepoint🔔｜🚀確変｜🟢値頃｜FAIL_INSEN｜698円｜💰7.2万円｜—
- 5803 フジクラ｜changepoint/changepoint🔔/changepoint🔔🔔｜🚀確変｜🟢値頃｜FAIL_INSEN｜3,900円｜💰39.2万円｜—｜⏰決算 11/10(残5営業日)
- 4011 Headwaters Co.,Ltd｜changepoint🔔/changepoint｜🚀確変｜🟢値頃｜FAIL_INSEN｜2,001円｜💰21.0万円｜—
- 6857 アドバンテスト｜changepoint/changepoint🔔｜🚀確変｜⚪妥当｜FAIL_UWAHIGE｜35,770円｜💰348.6万円｜—｜⚠日程不明｜⚡材料後出し｜🔁
- 9888 UEX LTD｜changepoint/changepoint🔔/changepoint🔔🔔｜🔥絶好調｜💎割安｜FAIL_UWAHIGE｜1,321円｜💰12.8万円｜—｜⏰決算 11/10(残5営業日)
- 7695 交換できるくん｜changepoint/changepoint🔔｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜850円｜💰8.7万円｜—
- 9308 乾汽船｜changepoint/changepoint🔔🔔｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜2,258円｜💰23.4万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⏰決算 11/10(残5営業日)
- 6136 OSG CORP｜changepoint/changepoint🔔/changepoint🔔🔔｜🔥絶好調｜🟢値頃｜PASS｜3,534円｜💰35.3万円｜⛔提案なし(指名鮮度切れ 13営業日)｜⚠日程不明
  > 【業態】タップ・エンドミルなど高シェアの精密切削工具大手。製販一貫体制。海外に注力。
  > 【いま】終値3,534円・直近5日+2.97%（材料未確認）
  > 【調子】🔥絶好調（9/13） — E軸判定不能(進捗データ不足)
  > 【水準】🟢値頃（5.0/7）— PER12.09倍・PEG0.1728・52週66.8% ／ 💰単元35.3万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 13営業日)）
- 7318 セレンディップ・ホールディングス｜changepoint/changepoint🔔/changepoint🔔🔔｜🔥絶好調｜💎割安｜FAIL_UWAHIGE｜1,095円｜💰10.9万円｜—
- 5582 （名称取得不可）｜changepoint/changepoint🔔｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1,760円｜💰17.9万円｜—
- 5590 NETSTARS Co.,Ltd.｜changepoint/changepoint🔔｜⚡好調｜🟢値頃｜FAIL_INSEN｜633円｜💰6.4万円｜—
- 478A Hutzper Inc.｜changepoint/changepoint🔔/changepoint🔔🔔｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜654円｜💰6.6万円｜—
- 9343 アイビス｜changepoint｜⚡好調｜⚪妥当｜FAIL_INSEN｜753円｜💰7.6万円｜—｜⏰決算 11/10(残5営業日)
- 4498 Cybertrust Japan Co., Ltd.｜changepoint/changepoint🔔/changepoint🔔🔔｜⚡好調｜🟡やや割高｜FAIL_INSEN｜2,077円｜💰21.5万円｜—｜⚠日程不明｜📐進捗 上振れ +21.7%｜⚡材料後出し｜📌
- 6284 日精エー・エス・ビー機械｜changepoint/changepoint🔔｜⚡好調｜🟢値頃｜PASS｜7,960円｜💰79.6万円｜⛔提案なし(指名鮮度切れ 11営業日)
  > 【業態】PETボトルなど非飲料容器成形機の世界大手。海外比率が9割。汎用機拡大。
  > 【いま】終値7,960円・直近5日+0.76%（材料未確認）
  > 【調子】⚡好調（5/13）
  > 【水準】🟢値頃（5.0/7）— PER13.11倍・PEG0.6540・52週46.2% ／ 💰単元79.6万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 11営業日)）
- 218A Liberaware｜changepoint/changepoint🔔｜⚡好調｜⚪妥当｜FAIL_INSEN｜840円｜💰8.6万円｜—｜⚠日程不明
- 6785 鈴木｜changepoint/changepoint🔔🔔｜✅順調｜🟢値頃｜FAIL_UWAHIGE｜3,100円｜💰30.9万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⏰決算 11/10(残5営業日)
- 4165 PLAID Inc.｜changepoint/changepoint🔔｜🔻悪化｜🔴過熱｜FAIL_INSEN｜733円｜💰7.5万円｜—｜⚠業績基調が下向き（悪化）
- 4071 Plus Alpha Consulting Co. LTD.｜changepoint/changepoint🔔｜✅順調｜⚪妥当｜FAIL_INSEN｜2,216円｜💰22.6万円｜—
- 598A チャットプラス｜changepoint🔔/changepoint/changepoint🔔🔔｜✅順調｜⚪妥当｜FAIL_INSEN｜1,086円｜💰11.2万円｜—
- 339A PROGRESS TECHNOLOGIES GROUP INC｜changepoint/changepoint🔔/changepoint🔔🔔｜➖横ばい｜⚪妥当｜FAIL_INSEN｜774円｜💰7.9万円｜—｜⚠日程不明
- 4488 AI inside Inc.｜changepoint｜➖横ばい｜🟡やや割高｜FAIL_INSEN｜1,890円｜💰20.3万円｜—
- 4259 ExaWizards Inc.｜changepoint/changepoint🔔｜業績データ取得不可｜🟢値頃｜FAIL_INSEN｜752円｜💰7.8万円｜—
- 4478 freee K.K.｜changepoint/changepoint🔔/changepoint🔔🔔｜業績データ取得不可｜🔴過熱｜PASS｜4,645円｜💰46.5万円｜提案あり｜🔒実弾封印中(PL3紙ログ収集中)｜⚠1単元でリスク枠超過（59,000円）
  > 【業態】スモールビジネス向けクラウドERPサービスの提供。会計や会社設立、開業支援など。
  > 【いま】終値4,645円・直近5日+11.39%（材料未確認）
  > 【調子】業績データ取得不可（—/13） — 業績データ取得不可(売上/経常欠損)
  > 【水準】🔴過熱（1.4/7）— PER—倍・PEG—・52週99.6% ／ 💰単元46.5万円
  > 【戦略】発火日終値4,645円の指値。追撃禁止・SL4,055円。🔒実弾封印中（PL3紙ログ収集中）／⚠1単元リスク59,000円（枠超過）
- 593A ティアフォー｜changepoint/changepoint🔔/changepoint🔔🔔｜取得不可｜🔴過熱｜FAIL_UWAHIGE｜2,406円｜💰24.0万円｜—
- 4483 JMDC｜changepoint🔔｜⚡好調｜🔴過熱｜FAIL_INSEN｜3,540円｜💰37.1万円｜—｜⏰決算 11/05(残2営業日)

## 🤖AI特需銘柄
波: なし（wave_on のセクター無し）／25MA 上回り率 📡エネマネ・計量 14.29%・❄️冷却・空調 0.0%・🌐光通信 27.27%
- 3131 シンデン・ハイテックス｜ai_momentum/ai_reversal/granville_rebound｜🚀確変｜💎割安｜FAIL_UWAHIGE｜5,150円｜💰52.0万円｜—｜⏰決算 11/10(残5営業日)｜🤖AI特需 🔬基板・素材/装置・商社
- 4187 大阪有機化学工業｜changepoint/changepoint🔔/ai_momentum｜🔥絶好調｜💎割安｜PASS｜4,400円｜💰44.0万円｜提案あり｜⚠日程不明
  > 【業態】化学（化成品・ファインケミカル・電子材料関連）
  > 【いま】終値4,400円・直近5日+3.04%（材料未確認）
  > 【調子】🔥絶好調（10/13）
  > 【水準】💎割安（6.0/7）— PER13.56倍・PEG0.2922・52週36.2% ／ 💰単元44.0万円
  > 【戦略】当日高値超えの逆指値4,435円で順張り参戦を検討。上限4,479.4円・SL4,164.2円目安
- 9824 泉州電業｜ai_momentum/ai_reversal｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜7,970円｜💰81.4万円｜—｜⚠日程不明
- 6613 QD Laser, Inc.｜granville_oshime/ai_momentum｜🔥絶好調｜🔴過熱｜FAIL_UWAHIGE｜2,335円｜💰24.1万円｜—
- 2760 東京エレクトロン　デバイス｜ai_momentum/granville_oshime/ai_reversal｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜4,265円｜💰42.3万円｜—｜⚠日程不明
- 6521 オキサイド｜ai_momentum/ai_reversal｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜3,155円｜💰31.0万円｜—｜⚠日程不明
- 4063 信越化学工業｜ai_momentum｜✅順調｜🟡やや割高｜FAIL_INSEN｜5,921円｜💰59.7万円｜—｜⚠日程不明
- 1975 新日本空調｜ai_momentum｜➖横ばい｜🟡やや割高｜PASS｜3,670円｜💰36.7万円｜提案あり
  > 【業態】空調・衛生工事の大手。ハイテク環境制御装置に優れる。民間受注が中心。
  > 【いま】終値3,670円・直近5日-2.78%（材料未確認）
  > 【調子】➖横ばい（2/13） — E軸判定不能(進捗データ不足)、質注意
  > 【水準】🟡やや割高（2.0/7）— PER10.27倍・PEG3.3489・52週41.5% ／ 💰単元36.7万円
  > 【戦略】当日高値超えの逆指値3,710円で順張り参戦を検討。上限3,747.1円・SL3,482.7円目安
- 1982 日比谷総合設備｜ai_momentum｜⚠減速｜🔴過熱｜PASS｜3,155円｜💰31.6万円｜⛔提案なし(指名鮮度切れ 14営業日)｜⚠業績基調が下向き（減速）
  > 【業態】空調工事大手。電気・衛生工事も。NTT向け主力。床下空調システムなどに強み。
  > 【いま】終値3,155円・直近5日-3.81%（材料未確認）
  > 【調子】⚠減速（1/13） — E軸判定不能(進捗データ不足)、質注意
  > 【水準】🔴過熱（1.0/7）— PER14.97倍・PEG5.1380・52週76.2% ／ 💰単元31.6万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 14営業日)）
- 3374 内外テック｜ai_reversal｜🚀確変｜🟢値頃｜FAIL_UWAHIGE｜4,370円｜💰43.4万円｜—｜🤖AI特需 🔬基板・素材/装置・商社
- 4062 イビデン｜ai_reversal/granville_rebound｜🚀確変｜⚪妥当｜FAIL_UWAHIGE｜8,045円｜💰83.6万円｜—｜⚠日程不明｜📐進捗 遅れ -20.5%｜🤖AI特需 🔬基板・素材/中流
- 6254 野村マイクロ・サイエンス｜changepoint/changepoint🔔/ai_reversal｜🚀確変｜💎割安｜FAIL_UWAHIGE｜2,642円｜💰26.4万円｜—
- 4047 関東電化工業｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_UWAHIGE｜1,955円｜💰19.6万円｜—｜⏰決算 11/10(残5営業日)
- 4971 メック｜ai_reversal｜🔥絶好調｜🟢値頃｜PASS｜6,020円｜💰60.2万円｜提案あり｜🤖AI特需 🔬基板・素材/上流
  > 【業態】電子基板向け薬品会社。半導体実装パッケージ基板で独占的。研究開発に力。
  > 【いま】終値6,020円・直近5日+4.15%（材料未確認）
  > 【調子】🔥絶好調（10/13）
  > 【水準】🟢値頃（5.0/7）— PER18.32倍・PEG0.4527・52週21.6% ／ 💰単元60.2万円
  > 【戦略】当日終値6,020円の指値で反転を取りにいく。SL5,770円（直近5日安値）
- 6407 CKD｜ai_reversal｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜4,670円｜💰46.5万円｜—｜⚡材料後出し｜🔁
- 3110 日東紡｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_UWAHIGE｜2,825.5円｜💰28.1万円｜—｜⏰決算 11/05(残2営業日)｜📐進捗 上振れ +21.5%｜🤖AI特需 🔬基板・素材/上流
- 6981 村田製作所｜ai_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜6,340円｜💰63.6万円｜—｜⚠日程不明
- 6524 湖北工業｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_UWAHIGE｜4,560円｜💰45.0万円｜—｜🤖AI特需 🌐光通信/中流
- 6235 オプトラン｜ai_reversal｜🔥絶好調｜💎割安｜PASS｜2,227円｜💰22.3万円｜提案あり｜⏰決算 11/10(残5営業日)｜🤖AI特需 🌐光通信/中流
  > 【業態】光学薄膜装置の製造・販売。車載カメラ、スマホ向けに注力。保守まで一貫に強み。
  > 【いま】終値2,227円・直近5日+1.69%（材料未確認）
  > 【調子】🔥絶好調（8/13） — D軸データ取得不可(中央値1点採用)、E軸判定不能(進捗データ不足)
  > 【水準】💎割安（6.0/7）— PER15.86倍・PEG0.1210・52週20.3% ／ 💰単元22.3万円
  > 【戦略】当日終値2,227円の指値で反転を取りにいく。SL2,164円（直近5日安値）
- 7729 東京精密｜ai_reversal｜🔥絶好調｜⚪妥当｜PASS｜15,420円｜💰154.2万円｜提案あり｜🚨決算直前 11/04(残1営業日)｜⚠1単元でリスク枠超過（78,000円）
  > 【業態】半導体製造装置・計測機器メーカー。ウエハテスト用首位。精密位置決め技術に定評。
  > 【いま】終値15,420円・直近5日+4.01%（材料未確認）
  > 【調子】🔥絶好調（8/13）
  > 【水準】⚪妥当（3.0/7）— PER20.32倍・PEG0.7713・52週50.7% ／ 💰単元154.2万円
  > 【戦略】当日終値15,420円の指値で反転を取りにいく。SL14,640円（直近5日安値）／⚠1単元リスク78,000円（枠超過）
- 6779 Nihon Dempa Kogyo Co., Ltd.｜granville_rebound/ai_reversal｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜2,457円｜💰24.8万円｜—｜⏰決算 11/09(残4営業日)｜🤖AI特需 📡エネマネ・計量/中流
- 6941 山一電機｜ai_reversal｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜7,200円｜💰73.1万円｜—｜⏰決算 11/05(残2営業日)
- 6752 パナソニックHD｜ai_reversal/granville_rebound｜⚡好調｜⚪妥当｜PASS｜3,740円｜💰37.4万円｜提案あり｜⚠日程不明｜🤖AI特需 🔬基板・素材/下流
  > 【業態】総合家電大手。AV、白モノ家電が軸。電池、照明、デバイス、住設も。車機器売却。
  > 【いま】終値3,740円・直近5日+4.44%（材料未確認）
  > 【調子】⚡好調（7/13） — 税引前代替、D軸判定不能(直近Qデータ取得不可)、上方修正済み
  > 【水準】⚪妥当（4.0/7）— PER16.17倍・PEG0.0931・52週62.7% ／ 💰単元37.4万円
  > 【戦略】当日終値3,740円の指値で反転を取りにいく。SL3,466円（直近5日安値）
- 6787 メイコー｜ai_reversal｜⚡好調｜💎割安｜PASS_DOJI｜8,300円｜💰83.0万円｜提案あり｜⏰決算 11/06(残3営業日)
  > 【業態】プリント配線板製造大手。車載向け、スマホ向けが主軸。中国、ベトナムに生産工場。
  > 【いま】終値8,300円・直近5日-10.85%（材料未確認）
  > 【調子】⚡好調（6/13） — E軸判定不能(進捗データ不足)、D軸判定不能(四半期データ不足・中立1点)
  > 【水準】💎割安（7.0/7）— PER7.98倍・PEG0.2484・52週22.5% ／ 💰単元83.0万円
  > 【戦略】当日終値8,300円の指値で反転を取りにいく。SL8,190円（直近5日安値）
- 6227 AIMECHATEC Ltd.｜granville_oshime/ai_reversal｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜5,440円｜💰53.4万円｜—｜🤖AI特需 🔬基板・素材/装置・商社
- 6777 santec｜ai_reversal｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜17,230円｜💰175.2万円｜—｜⏰決算 11/06(残3営業日)｜📐進捗 上振れ +27.6%
- 4973 JCU｜ai_reversal｜⚡好調｜⚪妥当｜PASS｜4,185円｜💰41.9万円｜提案あり｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚠日程不明
  > 【業態】メッキ用薬品の開発・販売。電子基板向けが主力。実装品向けも。ファブレス企業。
  > 【いま】終値4,185円・直近5日-0.36%（材料未確認）
  > 【調子】⚡好調（5/13） — E軸判定不能(進捗データ不足)、質注意
  > 【水準】⚪妥当（3.0/7）— PER11.21倍・PEG3.6258・52週30.4% ／ 💰単元41.9万円
  > 【戦略】当日終値4,185円の指値で反転を取りにいく。SL4,065円（直近5日安値）
- 5208 Arisawa Mfg.Co., Ltd.｜granville_oshime/ai_reversal｜✅順調｜🔴過熱｜FAIL_INSEN｜2,495円｜💰25.2万円｜—｜⏰決算 11/05(残2営業日)｜🤖AI特需 🔬基板・素材/上流
- 8098 稲畑産業｜ai_reversal/granville_oshime｜✅順調｜🔴過熱｜FAIL_INSEN｜4,350円｜💰44.3万円｜—｜⏰決算 11/05(残2営業日)
- 6643 戸上電機製作所｜ai_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜5,140円｜💰51.2万円｜—｜🚨決算直前 11/04(残1営業日)
- 6323 ローツェ｜ai_reversal｜✅順調｜🟡やや割高｜FAIL_UWAHIGE｜3,696円｜💰42.2万円｜—｜🤖AI特需 🔬基板・素材/装置・商社
- 5706 三井金属鉱業｜ai_reversal｜🔻悪化｜🟡やや割高｜FAIL_UWAHIGE｜2,000円｜💰20.2万円｜—｜⏰決算 11/10(残5営業日)｜⚠業績基調が下向き（悪化）
- 3103 ユニチカ｜ai_reversal/granville_rebound｜🔻悪化｜🟡やや割高｜FAIL_UWAHIGE｜1,171円｜💰11.9万円｜—｜⏰決算 11/10(残5営業日)｜⚠業績基調が下向き（悪化）｜🤖AI特需 🔬基板・素材/上流
- 6590 芝浦メカトロニクス｜ai_reversal｜➖横ばい｜🟡やや割高｜PASS｜3,115円｜💰31.1万円｜提案あり｜⏰決算 11/05(残2営業日)｜🤖AI特需 🔬基板・素材/装置・商社
  > 【業態】液晶・半導体の製造装置メーカー。前工程ウエハ洗浄で世界トップ。自販機システムも。
  > 【いま】終値3,115円・直近5日+3.15%（材料未確認）
  > 【調子】➖横ばい（2/13） — E軸判定不能(進捗データ不足)、質注意
  > 【水準】🟡やや割高（2.0/7）— PER17.18倍・PEG3.2000・52週7.0% ／ 💰単元31.1万円
  > 【戦略】当日終値3,115円の指値で反転を取りにいく。SL3,010円（直近5日安値）
- 5302 日本カーボン｜ai_reversal｜➖横ばい｜🔴過熱｜FAIL_INSEN｜4,885円｜💰48.9万円｜—｜📑TOPIX低減対象（次 01/29 第2回/8）｜⚠日程不明
- 9432 NTT｜ai_reversal｜➖横ばい｜🔴過熱｜PASS｜174.5円｜💰1.7万円｜⛔提案なし(指名鮮度切れ 15営業日)｜🚨決算直前 11/04(残1営業日)｜⚡材料後出し｜🔁
  > 【業態】国内通信事業最大手。持ち株会社制で地域電話独占。携帯、光回線高シェア。
  > 【いま】終値174.5円・直近5日-1.08%・🔁自己株式の取得状況に関するお知らせ
  > 【調子】➖横ばい（2/13） — E軸判定不能(進捗データ不足)、質注意
  > 【水準】🔴過熱（1.0/7）— PER14.42倍・PEG—・52週82.4% ／ 💰単元1.7万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 15営業日)）
- 6617 東光高岳｜ai_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜5,270円｜💰54.6万円｜—｜⚠日程不明｜⚠業績基調が下向き（減速）｜📐進捗 上振れ +10.5%
- 4203 住友ベークライト｜ai_reversal｜業績データ取得不可｜⚪妥当｜FAIL_INSEN｜7,932円｜💰81.1万円｜—｜🚨決算直前 11/04(残1営業日)
- 3436 SUMCO｜ai_reversal｜—｜—｜FAIL_UWAHIGE｜2,272.5円｜💰—｜—｜🤖AI特需 🏢大型・指数寄与/素材部品
- 6146 ディスコ｜ai_reversal｜—｜—｜FAIL_UWAHIGE｜50,240円｜💰—｜—｜⚠日程不明｜🤖AI特需 🏢大型・指数寄与/装置
- 9984 ソフトバンクグループ｜ai_reversal｜—｜—｜FAIL_UWAHIGE｜4,410円｜💰—｜—｜⏰決算 11/10(残5営業日)｜🤖AI特需 🏢大型・指数寄与/投資通信

## ⚡材料後出し
その日の足は開示前の情報。判定は参考値。
- 212A FIT EASY Inc.｜FAIL_INSEN｜📌｜—
- 5537 AlbaLink Co.,Ltd.｜FAIL_INSEN｜📌｜—
- 6071 IBJ, Inc.｜FAIL_INSEN｜📌｜—
- 505A Geekly,Inc.｜FAIL_INSEN｜📌｜—
- 3696 セレス｜FAIL_INSEN｜🔁｜—
- 6516 Sanyo Denki Co., Ltd.｜FAIL_UWAHIGE｜📌｜—
- 6268 ナブテスコ｜FAIL_UWAHIGE｜🔁｜—
- 4088 Air Water Inc.｜FAIL_INSEN｜🔁｜—
- 9436 Okinawa Cellular Telephone Company｜FAIL_INSEN｜🔁｜—
- 7276 Koito Manufacturing Co., Ltd.｜PASS_DOJI｜🔁｜⛔提案なし(材料後出し)
- 6135 牧野フライス製作所｜FAIL_UWAHIGE｜🔁｜—
- 7278 Exedy Corporation｜PASS｜🔁｜⛔提案なし(材料後出し)
- 7220 Musashi Seimitsu Industry Co., Ltd.｜PASS｜📌｜⛔提案なし(材料後出し)
- 8174 NIPPON GAS Co., Ltd.｜FAIL_INSEN｜🔁｜—
- 8616 Tokai Tokyo Financial Holdings, Inc.｜FAIL_INSEN｜📌｜—
- 8628 Matsui Securities Co., Ltd.｜FAIL_UWAHIGE｜📌｜—
- 9962 ミスミグループ本社｜FAIL_UWAHIGE｜🔁｜—
- 3498 霞ヶ関Ｃ｜FAIL_UWAHIGE｜📌｜—
- 6407 CKD｜FAIL_UWAHIGE｜🔁｜—
- 9432 NTT｜PASS｜🔁｜⛔提案なし(指名鮮度切れ 15営業日)
- 5532 リアルゲイト｜FAIL_UWAHIGE｜📌｜—
- 7199 プレミアグループ｜FAIL_INSEN｜📌｜—
- 6371 Tsubakimoto Chain Co.｜FAIL_INSEN｜🔁｜—
- 3562 No.1 Co., Ltd.｜FAIL_INSEN｜📌｜—
- 5184 ニチリン｜FAIL_INSEN｜🔁｜—
- 2897 Nissin Foods Holdings Co., Ltd.｜FAIL_INSEN｜📌｜—
- 3569 セーレン｜FAIL_INSEN｜🔁｜—
- 4208 UBE Corporation｜FAIL_UWAHIGE｜📌｜—
- 6027 Bengo4.com, Inc.｜FAIL_INSEN｜🔁｜—
- 7480 スズデン｜PASS_DOJI｜📊｜⛔提案なし(材料後出し)
- 5367 Nikkato Corporation｜FAIL_UWAHIGE｜📊｜—
- 278A Ｔｅｒｒａ　Ｄｒｏｎｅ｜FAIL_UWAHIGE｜📌｜—
- 6890 Ferrotec Corporation｜FAIL_UWAHIGE｜📌｜—
- 8377 ほくほくフィナンシャルグループ｜FAIL_UWAHIGE｜📌｜—
- 6857 アドバンテスト｜FAIL_UWAHIGE｜🔁｜—
- 4498 Cybertrust Japan Co., Ltd.｜FAIL_INSEN｜📌｜—

## 📢開示
使用した一覧: https://kabutan.jp/disclosures/?kubun=&date=20261102（全ページ巡回）および date=20261030（20:45以降分）。フォールバック: なし。
- 📊 4005 住友化学｜決算発表｜2026年３月期第２四半期決算短信〔ＩＦＲＳ〕（連結）（11-02 13:30）
- 📊 5367 Nikkato Corporation｜決算発表｜2027年3月期 第2四半期決算短信〔日本基準〕（非連結）（11-02 15:30）
- 📊 6592 Mabuchi Motor Co., Ltd.｜決算発表｜2026年12月期第3四半期決算短信〔日本基準〕（連結）（11-02 12:30）
- 📊 7480 スズデン｜決算発表｜2027年３月期第２四半期（中間期）決算短信〔日本基準〕(連結)（11-02 15:30）
- 📊 9044 NANKAI Co., Ltd.｜決算発表｜2027年3月期 第2四半期（中間期）決算短信〔日本基準〕(連結)（11-02 14:00）
- 🔁 2659 SAN-A CO., LTD.｜自己株式取得｜自己株式の取得状況に関するお知らせ（11-02 09:45）
- 🔁 3569 セーレン｜自己株式取得｜自己株式取得状況に関するお知らせ（11-02 16:00）
- 🔁 3696 セレス｜自己株式取得｜自己株式の取得状況に関するお知らせ（11-02 15:30）
- 🔁 4088 Air Water Inc.｜自己株式取得｜譲渡制限付株式報酬としての自己株式の処分の払込完了に関するお知らせ（11-02 15:30）
- 🔁 4534 Mochida Pharmaceutical Co., Ltd.｜自己株式取得｜自己株式の取得状況に関するお知らせ（11-02 14:00）
- 🔁 5184 ニチリン｜自己株式取得｜自己株式取得状況に関するお知らせ（11-02 15:00）
- 🔁 6027 Bengo4.com, Inc.｜自己株式取得｜自己株式の取得状況に関するお知らせ （会社法第459条第１項の規定による定款の定めに基づく自己株式の取得）（11-02 15:30）
- 🔁 6135 牧野フライス製作所｜自己株式取得｜自己株式の取得状況に関するお知らせ（会社法第165条第２項の規定による定款の定めに基づく自己株式の取得）（11-02 15:30）
- 🔁 6268 ナブテスコ｜自己株式取得｜自己株式の取得状況及び取得終了に関するお知らせ（11-02 16:00）
- 🔁 6302 住友重機械工業｜自己株式取得｜自己株式の取得状況に関するお知らせ（会社法第165条第2項の規定による定款の定めに基づく自己株式の取得）（11-02 10:00）
- 🔁 6371 Tsubakimoto Chain Co.｜自己株式取得｜自己株式の取得状況に関するお知らせ（11-02 15:30）
- 🔁 6407 CKD｜自己株式取得｜自己株式の取得状況に関するお知らせ（11-02 16:00）
- 🔁 6432 竹内製作所｜自己株式取得｜自己株式の取得状況に関するお知らせ（11-02 14:30）
- 🔁 6857 アドバンテスト｜自己株式取得｜自己株式の取得状況に関するお知らせ（11-02 15:30）
- 🔁 7276 Koito Manufacturing Co., Ltd.｜自己株式取得｜自己株式の取得状況に関するお知らせ（11-02 15:00）
- 🔁 7278 Exedy Corporation｜自己株式取得｜自己株式の取得状況に関するお知らせ（11-02 16:00）
- 🔁 8174 NIPPON GAS Co., Ltd.｜自己株式取得｜自己株式の取得状況（途中経過）に関するお知らせ（11-02 15:30）
- 🔁 9432 NTT｜自己株式取得｜自己株式の取得状況に関するお知らせ（11-02 15:30）
- 🔁 9436 Okinawa Cellular Telephone Company｜自己株式取得｜自己株式の取得状況に関するお知らせ（11-02 15:30）
- 🔁 9882 Yellow Hat Ltd.｜自己株式取得｜自己株式立会外買付取引（ToSTNeT-3）による自己株式の取得結果に関するお知らせ（11-02 11:00）
- 🔁 9962 ミスミグループ本社｜自己株式取得｜自己株式の取得状況に関するお知らせ（11-02 15:00）
- 📌その他重要開示 83件（見出しのみ・ボード省略）
①-9へ引き渡し 5件（recalc_queue）

## 総当りゲート
### 5手法
- PASS（34）: 2980 SRE Holdings Corp.、6629 TECHNO HORIZON Co., Ltd.、7995 Valqua Ltd.、5333 ＮＧＫ、6302 住友重機械工業、5101 Yokohama Rubber Co., Ltd.、8282 K'S HOLDINGS CORPORATION、7721 Tokyo Keiki Inc.、9072 NIKKON Holdings Co., Ltd.、9882 Yellow Hat Ltd.、7731 ニコン、6925 Ushio Inc.、6368 Organo Corp.、6651 NITTO KOGYO Corporation、9533 TOHO GAS Co., Ltd.、4966 上村工業、6674 ジーエス・ユアサ　コーポレーション、7278 Exedy Corporation、7220 Musashi Seimitsu Industry Co., Ltd.、6479 ミネベア、6183 BELLSYSTEM24 Holdings, Inc.、4980 Dexerials Corp.、1963 日揮ホールディングス、5310 Toyo Tanso Co., Ltd.、7148 Financial Products Group Co., Ltd.、6349 Komori Corporation、3612 WORLD CO.,LTD.、8975 Ichigo Office REIT Investment Corporation、5831 Shizuoka Financial Group, Inc.、8304 あおぞら銀行、6810 Maxell, Ltd.、7186 横浜フィナンシャルグループ、8354 ふくおかフィナンシャルグループ、8698 Monex Group, Inc.
- PASS_DOJI（4）: 3915 TerraSky Co., Ltd.、6652 IDEC Corporation、7276 Koito Manufacturing Co., Ltd.、6632 JVCKENWOOD Corporation
- FAIL_UWAHIGE（62）: 276A CCReB Advisors Inc.、3556 RenetJapanGroup, Inc.、4434 Serverworks Co., Ltd.、5757 CK San-Etsu Co., Ltd.、4771 F&M Co., Ltd.、6289 Giken Ltd.、7567 Sakae Electronics Corp.、6337 Tesec Corporation、3843 Freebit Co., Ltd.、4933 I-ne CO., LTD.、4565 Nxera Pharma Co., Ltd.、6278 ユニオンツール、6516 Sanyo Denki Co., Ltd.、3391 TSURUHA Holdings, Inc.、5344 MARUWA CO., LTD.、3036 アルコニックス、4216 ASAHI YUKIZAI CORPORATION、6268 ナブテスコ、6481 THK Co., Ltd.、6324 Harmonic Drive Systems Inc.、6645 OMRON Corporation、3222 United Super Markets Holdings, Inc.、6471 日本精工、5301 Tokai Carbon Co., Ltd.、7733 Olympus Corp.、7004 カナデビア、6332 月島ホールディングス、2782 Seria Co., Ltd.、8278 Fuji Co., Ltd.、268A Rigaku Holdings Corporation、4666 Park24 Co., Ltd.、6135 牧野フライス製作所、1861 Kumagai Gumi Co., Ltd.、5331 ノリタケ、3433 TOCALO Co., Ltd.、8198 Maxvalu Tokai Co., Ltd.、1820 Nishimatsu Construction Co., Ltd.、1952 Shin Nippon Air Technologies Co., Ltd.、7003 Mitsui ES Holdings Co., Ltd.、6055 Japan Material Co., Ltd.、3445 RS Technologies Co. Ltd.、6366 Chiyoda Corp.、5844 Kyoto Financial Group,Inc.、5482 Aichi Steel Corporation、8276 HEIWADO CO., LTD.、9974 BELC Co., Ltd.、3105 日清紡ホールディングス、6804 Hosiden Corp.、8194 Life Corporation、7384 Procrea Holdings,Inc.、8366 滋賀銀行、8359 Hachijuni Nagano Bank, Ltd.、8628 Matsui Securities Co., Ltd.、6668 ＡＤプラズマ、7713 シグマ光機、5832 ちゅうぎんフィナンシャルグループ（ちゅうぎんＦ）、5018 ＭＯＲＥＳＣＯ、9962 ミスミグループ本社、3498 霞ヶ関Ｃ、6814 古野電、3479 ＴＫＰ、6505 東洋電機製造
- FAIL_INSEN（108）: 5137 Smart Drive Co. Ltd.、5027 AnyMind Group Inc.、4053 Sun Asterisk, Inc.、5136 tripla Co.,Ltd.、9554 AViC Co. Ltd.、212A FIT EASY Inc.、421A Movin' Strategic Career CO.,LTD.、5132 pluszero,Inc.、4377 ONE CAREER Inc.、5537 AlbaLink Co.,Ltd.、7047 PORT INC.、6071 IBJ, Inc.、4058 Toyokumo, Inc.、5034 unerry, Inc.、147A SORACOM,INC.、9560 PROGRIT, Inc.、7678 ASAKUMA CO.,LTD.、4477 BASE, Inc.、4412 Science Arts, Inc.、505A Geekly,Inc.、4743 ITFOR Inc.、3077 Horiifoodservice Co., Ltd.、618A KOMPEITO Inc.、446A ノースサンド、3696 セレス、2930 北の達人コーポレーション、4379 Photosynth inc.、2820 Yamami Co.、7161 Jimoto Holdings, Inc.、6875 メガチップス、7433 Hakuto Co., Ltd.、8871 GOLDCREST Co., Ltd.、8336 武蔵野銀行、6754 アンリツ、8346 東邦銀行、4088 Air Water Inc.、6370 栗田工業、8386 百十四銀行、8522 Bank of Nagoya, Ltd.、3116 Toyota Boshoku Corp.、8987 Japan Excellent, Inc.、4205 Zeon Corporation、9412 SKY Perfect JSAT Corporation、2805 S&B Foods Inc.、9436 Okinawa Cellular Telephone Company、8125 Wakita & Co., Ltd.、8714 池田泉州ホールディングス、8393 Miyazaki Bank Ltd.、8399 琉球銀行、7458 Daiichikosho Co., Ltd.、9934 因幡電機産業、8381 San-in Godo Bank Ltd.、8524 North Pacific Bank, Ltd.、6923 Stanley Electric Co., Ltd.、3282 Comforia Residential REIT, Inc.、4021 Nissan Chemical Corporation、1417 MIRAIT ONE Corporation、1944 Kinden Corporation、3148 Create SD Holdings Co., Ltd.、1860 Toda Corporation、6807 Japan Aviation Electronics Industry, Limited、8066 Mitani Corporation、2659 SAN-A CO., LTD.、5021 Cosmo Energy Holdings Co., Ltd.、1333 Umios Corporation、1719 HAZAMA ANDO Corporation、1833 Okumura Corporation、2379 dip Corporation、1946 Toenec Corporation、1893 Penta-Ocean Construction Co., Ltd.、6753 Sharp Corporation、8585 Orient Corporation、3296 NIPPON REIT Investment Corp、5631 Japan Steel Works, Ltd.、9948 Arcs Company, Limited、6960 Fukuda Denshi Co., Ltd.、1662 Japan Petroleum Exploration Co., Ltd.、9699 NISHIO HOLDINGS CO. LTD.、8253 Credit Saison Co., Ltd.、8370 紀陽銀行、7381 ＣＣＩグループ、8345 Bank of Iwate Ltd.、8367 南都銀行、8174 NIPPON GAS Co., Ltd.、8334 Gunma Bank, Ltd.、7201 Nissan Motor Co., Ltd.、3591 WACOAL HOLDINGS CORP、2109 ＤＭ三井製糖、5711 三菱マテリアル、7167 めぶきフィナンシャルグループ、7177 ＧＭＯフィナンシャルホールディングス、7322 三十三フィナンシャルグループ、8600 トモニホールディングス、8616 Tokai Tokyo Financial Holdings, Inc.、7624 NaITO、4410 ハリマ化成グループ（ハリマ化成Ｇ）、7942 ＪＳＰ、9110 ＮＳユナイテッド海運（ユナイテド海）、3994 マネーフォワード、7811 中本パックス、4443 Ｓａｎｓａｎ、9766 コナミグループ（コナミＧ）、5932 三協立山、3091 ブロンコビリー、4417 グローバルセキュリティエキスパート（Ｇセキュリ）、6532 ベイカレント、4176 ココナラ、8954 ORIX JREIT Inc.
- SKIP（0）: なし
### グランビル
- PASS（26）: 9742 アイネス、6255 NPC Incorporated、3405 クラレ、4401 ＡＤＥＫＡ、3935 Edia Co. Ltd.、4617 中国塗料、4568 第一三共、6592 Mabuchi Motor Co., Ltd.、3549 クスリのアオキホールディングス、5461 Chubu Steel Plate Co., Ltd.、7734 Riken Keiki Co., Ltd.、5233 太平洋セメント、6196 Strike Group Co. Ltd.、6328 Ebara Jitsugyo Co., Ltd.、4937 Ｇ−ＷＡＱＯＯ、7806 MTG Co., Ltd.、6080 Ｍ＆Ａキャピタルパートナーズ、6523 ＰＨＣホールディングス、6340 澁谷工業、9509 Hokkaido Electric Power Company,Incorporated、7630 Ichibanya Co., Ltd.、3793 Drecom Co., Ltd.、150A ＪＳＨ、6490 ＰＩＬＬＡＲ、4100 Toda Kogyo Corp.、7175 Imamura Securities Co.Ltd.
- PASS_DOJI（5）: 3927 アークン、7480 スズデン、8084 ＲＹＯＤＥＮ、6508 Meidensha Corporation、2681 2nd RETAILING Co., Ltd.
- FAIL_UWAHIGE（54）: 6905 Cosel Co., Ltd.、7725 INTER ACTION Corporation、9211 f-code Inc.、4956 Konishi Co., Ltd.、8697 日本取引所グループ、5532 リアルゲイト、5838 Rakuten Bank, Ltd.、4045 Toagosei Co., Ltd.、6768 Tamura Corporation、8061 Seika Corporation、8014 Chori Co., Ltd.、8113 Unicharm Corporation、4183 Mitsui Chemicals, Inc.、4272 Nippon Kayaku Co., Ltd.、8012 Nagase & Co., Ltd.、2811 Kagome Co., Ltd.、7921 ＴＡＫＡＲＡ　＆　ＣＯＭＰＡＮＹ、3563 ＦＯＯＤ　＆　ＬＩＦＥ　ＣＯＭＰＡＮＩＥＳ、5243 ｎｏｔｅ、6834 精工技研、3156 レスター、7856 HAGIHARA INDUSTRIES INC.、4471 三洋化成工業、7609 ダイトロン、6250 Yamabiko Corporation、9552 クオンツ総研ホールディングス、6998 Nippon Tungsten Co., Ltd.、5985 SUNCALL CORPORATION、1518 三井松島ホールディングス、4208 UBE Corporation、3107 ダイワボウホールディングス、4044 Central Glass Co., Ltd.、8255 Axial Retailing, Inc.、9166 GENDA Inc.、3891 ニッポン高度紙工業、6769 Thine Electronics, Inc.、3691 DIGITAL PLUS, Inc.、2962 テクニスコ、4419 Finatext Holdings Ltd.、4968 Arakawa Chemical Industries,Ltd.、6963 ROHM Company Limited、7715 長野計器、5367 Nikkato Corporation、6336 石井表記、6597 HPC SYSTEMS Inc.、3687 Fixstars Corp.、9278 BOOKOFF GROUP HOLDINGS LIMITED、278A Ｔｅｒｒａ　Ｄｒｏｎｅ、4691 Washington Hotel Corp.、6203 Howa Machinery, Ltd.、6522 アスタリスク、6840 ＡＫＩＢＡホールディングス、6890 Ferrotec Corporation、8377 ほくほくフィナンシャルグループ
- FAIL_INSEN（110）: 5254 Arent, Inc.、8944 Land Business Co., Ltd.、9553 MicroAd, Inc.、6562 Geniee, Inc.、6470 Taiho Kogyo Co., Ltd.、4534 Mochida Pharmaceutical Co., Ltd.、7744 ノーリツ鋼機、8095 Astena Holdings Co.,Ltd.、3741 Systems Engineering Consultants Co., Ltd.、4544 H.U.Group Holdings, Inc.、7970 Shin-Etsu Polymer Co., Ltd.、4763 クリーク・アンド・リバー社、7199 プレミアグループ、7606 ＴＡＢＡＹＡホールディングス、4848 Fullcast Holdings Co., Ltd.、6371 Tsubakimoto Chain Co.、3562 No.1 Co., Ltd.、9842 アークランズ、4169 Enechange Ltd.、6432 竹内製作所、7747 朝日インテック、8020 Kanematsu Corporation、4549 Eiken Chemical Co., Ltd.、3092 ＺＯＺＯ、5184 ニチリン、8160 KISOJI CO., LTD.、4166 Cacco, Inc.、2897 Nissin Foods Holdings Co., Ltd.、9163 Nareru Group Inc.、186A Astroscale Holdings Inc.、3569 セーレン、7269 スズキ、7513 Kojima Co., Ltd.、6770 Alps Alpine Co., Ltd.、8081 Kanaden Corporation、9837 Morito Co., Ltd.、4922 コーセーホールディングス、4902 Konica Minolta, Inc.、4552 JCR Pharmaceuticals Co., Ltd.、5105 ＴＯＹＯ　ＴＩＲＥ、8167 リテールパートナーズ、4375 セーフィー、4005 住友化学、4912 ライオン、1928 積水ハウス、1941 中電工、3002 グンゼ、4403 日油、8008 Yondoshi Holdings, Inc.、8137 サンワテクノス、4382 HEROZ, Inc.、8051 山善、4180 ＡＰＰＩＥＲ　ＧＲＯＵＰ、4431 Smaregi, Inc.、5892 ＹＵＴＯＲＩ、6036 ＫｅｅＰｅｒ技研、9902 Nichiden Corporation、3040 ソリトンシステムズ、6736 Suncorporation、3106 倉敷紡績、2602 日清オイリオグループ、4413 baudroie,inc.、6570 Kyowa Corporation Co. Ltd.、8410 Seven Bank, Ltd.、9304 澁澤倉庫、8392 大分銀行、7350 Okinawa Financial Group, Inc.、9536 SAIBU GAS HOLDINGS CO. LTD.、6191 エボラブルアジア、4475 HENNGE K.K.、8395 佐賀銀行、3097 Monogatari Corporation、6418 Japan Cash Machine Co., Ltd.、9044 NANKAI Co., Ltd.、338A ZenmuTech,Inc.、456A Human Made Inc.、9505 Hokuriku Electric Power Company、3692 ＦＦＲＩセキュリティ、8043 Starzen Company Limited、8097 SAN-AI OBBLI CO. LTD、8361 Ogaki Kyoritsu Bank, Ltd.、8343 Akita Bank, Ltd.、3993 PKSHA Technology, Inc.、6027 Bengo4.com, Inc.、8362 Fukui Bank, Ltd.、3778 SAKURA Internet Inc.、8704 TRADERS HOLDINGS CO LTD、479A PRONI Inc.、5381 Mipox Corp.、1436 GreenEnergy & Company、8995 Makoto Construction Co,Ltd、8364 清水銀行、9697 カプコン、5242 EYEZ INC.、477A Startline CO.,LTD.、2354 YE DIGITAL CORPORATION、8344 Yamagata Bank, Ltd.、5574 ABEJA,Inc.、7256 河西工業、4997 日本農薬、3907 Silicon Studio Corp.、4440 WITZ Corp.、8360 Yamanashi Chuo Bank, Ltd.、7380 Juroku Financial Group,Inc.、8368 Hyakugo Bank, Ltd.、8713 Fidea Holdings Co.Ltd.、4075 ブレインズテクノロジー、460A ＢＲＡＮＵ、8609 岡三証券グループ、8739 スパークス・グループ
- SKIP（0）: なし
### 変化点
- PASS（3）: 6136 OSG CORP、6284 日精エー・エス・ビー機械、4478 freee K.K.
- PASS_DOJI（0）: なし
- FAIL_UWAHIGE（6）: 6857 アドバンテスト、9888 UEX LTD、7318 セレンディップ・ホールディングス、478A Hutzper Inc.、6785 鈴木、593A ティアフォー
- FAIL_INSEN（17）: 265A エイチエムコム、5803 フジクラ、4011 Headwaters Co.,Ltd、7695 交換できるくん、9308 乾汽船、5582 （名称取得不可）、5590 NETSTARS Co.,Ltd.、9343 アイビス、4498 Cybertrust Japan Co., Ltd.、218A Liberaware、4165 PLAID Inc.、4071 Plus Alpha Consulting Co. LTD.、598A チャットプラス、339A PROGRESS TECHNOLOGIES GROUP INC、4488 AI inside Inc.、4259 ExaWizards Inc.、4483 JMDC
- SKIP（0）: なし
### AI特需
- PASS（10）: 4187 大阪有機化学工業、1975 新日本空調、1982 日比谷総合設備、4971 メック、6235 オプトラン、7729 東京精密、6752 パナソニックHD、4973 JCU、6590 芝浦メカトロニクス、9432 NTT
- PASS_DOJI（1）: 6787 メイコー
- FAIL_UWAHIGE（21）: 3131 シンデン・ハイテックス、6613 QD Laser, Inc.、2760 東京エレクトロン　デバイス、6521 オキサイド、3374 内外テック、4062 イビデン、6254 野村マイクロ・サイエンス、4047 関東電化工業、6407 CKD、3110 日東紡、6524 湖北工業、6779 Nihon Dempa Kogyo Co., Ltd.、6941 山一電機、6227 AIMECHATEC Ltd.、6777 santec、6323 ローツェ、5706 三井金属鉱業、3103 ユニチカ、3436 SUMCO、6146 ディスコ、9984 ソフトバンクグループ
- FAIL_INSEN（9）: 9824 泉州電業、4063 信越化学工業、6981 村田製作所、5208 Arisawa Mfg.Co., Ltd.、8098 稲畑産業、6643 戸上電機製作所、5302 日本カーボン、6617 東光高岳、4203 住友ベークライト
- SKIP（0）: なし
### 除籍（30暦日超・SBIグループ登録解除候補）
5038 eWeLL Co.,Ltd、5821 Hirakawa Hewtech Corp.、8424 芙蓉総合リース、8850 スターツコーポレーション、9960 トーテック、6988 日東電工、2871 ニチレイ、1969 高砂熱学工業、1879 新日本建設、8919 カチタス、9616 共立メンテナンス、4082 第一稀元素化学工業、4368 4368、9268 OPTIMUS GROUP Co., Ltd.、6298 Y.A.C.HOLDINGS CO.,LTD.、7181 JAPAN POST INSURANCE Co., Ltd.、2986 LA Holdings Co.,Ltd、6208 Ishikawa Seisakusho,Ltd.、4373 Simplex Holdings,Inc.、7616 Colowide Co., Ltd.、6379 RAIZNEXT Corporation、8059 Daiichi Jitsugyo Co., Ltd.、9900 Sagami Holdings Corp.、2874 YOKOREI CO. LTD.、8163 SRS HOLDINGS CO.,LTD.、6862 ミナトホールディングス、4331 Take and Give. Needs Co., Ltd.、1803 Shimizu Corporation、2809 Kewpie Corporation、6269 Modec, Inc.、3289 Tokyu Fudosan Holdings Corp.、3283 Nippon Prologis REIT, Inc.、9503 Kansai Electric Power Company, Incorporated、8088 岩谷産業、3471 Mitsui Fudosan Logistics Park, Inc.、8953 Japan Metropolitan Fund Investment Corporation、3249 Industrial & Infrastructure Fund Investment Corporation、7984 Kokuyo Co., Ltd.、3462 Nomura Real Estate Master Fund, Inc.、8952 Japan Real Estate Investment Corp.、8818 Keihanshin Building Co., Ltd.、4928 Noevir Holdings Co., Ltd.、8954 ORIX JREIT Inc.、3309 Sekisui House Reit. Inc.、8961 MORI TRUST REIT.Inc、2815 ARIAKE JAPAN Co., Ltd.、3292 AEON REIT Investment Corp.、8986 Daiwa Securities Living Investment Corporation、3279 Activia Properties, Inc.、8955 Japan Prime Realty Investment Corporation、3234 Mori Hills Reit Investment Corporation、8584 Jaccs Co., Ltd.、6473 JTEKT Corporation、6454 Max Co., Ltd.、3661 m-up holdings, Inc.、8927 Meiho Enterprise Co., Ltd.、5246 ＥＬＥＭＥＮＴＳ、8624 Ichiyoshi Securities Co., Ltd.、4667 Aisan Technology Co., Ltd.、6072 Jibannet Holdings Co., Ltd.、3653 Morpho, Inc.、4346 NEXYZ.Group Corporation、7354 Direct Marketing MiX Inc.

## 機械詳細
- 検知: 評価470件（pool 469＋前夜提案の追加取得1件）・SKIP 0件・日足取得失敗 0件
- 開示の分類別件数（プール在籍分）: 📢0／📉0／📊5／🔁21／👥1／🏛0／📦0／📌83
- 開示ウォッチ: 一覧取得 945行（11/02 + 10/30 夕方）・⚡材料後出し 36件
- ヘッドライン: PASS83件中83件に付与（抜粋規則は適用せず全件）
- kabutan 新規取得 49/50件（PASS 業態欠け11件＋業種の埋め戻し38件・残り0件）／profile_cache 総数 988・本夜の追加/補完 95件・取得エラー0件
- 業態が「未取得」のまま出た件数: 0
- earnings_log 総数 157／本夜追記 5件／リターン補完 33件
- gyoseki_cache: 本夜は再計算を実施せず（history 退避 0件）。📢📉📊 の銘柄は recalc_queue に積んで ①-9 へ引き渡し
- gate_history: gate_history/2026-11-02.json を新規作成（verdicts 470件・nominations 105件）
- grades.json: 1009銘柄／571.5KiB／nx 付与665件・lx 496件・pxd 361件・pg 99件
- 次回決算日: 付与665件／未発表344件・earnings_calendar.json 1009銘柄/133.8KiB
- pool_bars.json: 470銘柄／402.6KiB
- method_score 保持 72件／null 398件
- 鮮度ゲート: 鮮度切れ除外14件・nom_age分布 0-2:203/3-10:149/11+:118
- 記録の凍結: 業種 付与済み468／未付与2（本夜埋め戻し38件・残り0件）
- トレンド文脈: ctx 合致128／不一致200／レンジ138／判定不能4・PASS のうち 合致26件
- 3日ルール判定（件数のみ）: 判定5銘柄・連続3日以上 0・連続2日 3・判定不可0
- 業種別PER中央値: 算出できた業種26／spm を写せた銘柄944件
- 熟成由来の候補 0件（うちPASS0）
- 権利情報（rights_cache）: 総数 503・本夜は権利落ち日が T+1/T+2 に無いため配当/優待の新規取得なし（0件・上限30）
- STEP 4.8: week_open=false のためスキップ
- 抜粋: 通知の【通過】は最大10件（ラウンドロビン）
- master.json の変更行数: +12463/-13583（W=2・仮ファイル経由で差し替え）
