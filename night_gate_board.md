# 夜間ゲート 2026-10-22

## サマリー
- 評価数: 433 / PASS: 36（PASS_DOJI 1件を含む）
- 発注可能提案数: 23件
- 市場一言: 市場モード「堅調」（market.latest 2026-10-22）。日経平均 −2.65% の全面安の日で、プール433銘柄中PASS比率8.3%（陰線FAIL 307件・上髭FAIL 90件）
- 実行モード: 通常（base_day=当日の引け値を対象）
- base_day: 2026-10-22（run_at 2026-10-22 20:53起動）
- week_open: false（翌営業日10/23(金)は週初でない）→ STEP 4.8 週末ブリーフはスキップ
- 📆 翌営業日 10/23(金): カレンダーイベントなし。T+2 10/26(月): カレンダーイベントなし。次の TOPIX 低減日 10/30(金) 第1回/8（あと6営業日）
- 📑指数: 低減対象 提案2件／PASS5件／プール66件・新規採用 17件（index_flags 2026-10-07 公表分）

## 検証結果
- V1 → はい（proposals23=results23=template23）
- V2 → はい（PASS36=提案23+除外13・order_status欠落0）
- V3 → はい（results433件重複0）
- V4 → はい（既存static変更0件）
- V5 → はい（許可キー外の変更0件・profile既存改変0）
- V6 → はい（不整合0件（「取得不可」は絵文字無しの既存状態））
- V10 → はい（base_day 4箇所一致）
- V12 → はい（proposals/template/results 同順）
- V14 → はい（保持59件/null374件・出所不明/不一致0件）
- V15 → はい（PASS36件中36件付与・欠落0・語句違反0（8174は業績グレード自体が「業績データ取得不可」＝キャッシュ値））
- V16 → はい（決算発表2件→earnings_log総数73・追記2・再計算前値保存(b)該当0・history超過0）
- V18 → はい（提案23件・鮮度切れ除外10件・誤除外0）
- V19 → はい（verdicts433=評価433・nominations93=pool last_seen・ctx {'不一致': 177, 'レンジ': 136, '合致': 113, '判定不能': 7}・既存gyotai変更0）
- V11 → いいえ（+7900/-6466（myers）／indent=2・往復一致で検出。results全置換433件とcache更新による。全体再フォーマットではない。前夜 +7940/-6472 と同水準）
- V9 → はい（gate_history/2026-10-22.json 新規作成・残りキー一致 True）
- V13 → いいえ（891銘柄/452.6KiB（463,512B）・和集合891・15キー欠落0・nx不一致0・業種中央値25業種再計算一致True（サイズ上限450KiBを2.6KiB超過。銘柄数増加が原因・前夜 451.1KiB も超過）
- V17 → はい（435銘柄/372KiB・保有4銘柄すべて収録・3日ルール判定4銘柄）
- V20 → はい（922銘柄/95KiB・nx非null740・hist持ち280・pxd187）
- V7 → はい（必須セクションすべて存在（週初でないため今週のカタリスト不要））
- V8 → はい（模擬23行の書式OK）
- LEAK → はい（公開物の保有情報漏えい確認は STEP 8 参照）

## 保有アラート
保有4銘柄・アラート15件（詳細は通知）

## 前夜の結果
PL5口座への正式な反映は週次①-11の採点で行われる。ここは参考情報。
前夜2026-10-21の提案54件 → 約定45・不約定9・判定不能0
- 5137 momentum 指定313 → 約定313・終値302（-3.51%）
- 5136 momentum 指定2724 → 約定2724・終値2597（-4.66%）
- 618A momentum 指定1913 → 約定1918・終値1965（+2.45%）
- 421A momentum 指定4485 → 約定4485・終値4285（-4.46%）
- 5537 momentum 指定3940 → 約定3940・終値3560（-9.64%）
- 505A momentum 指定1159 → 約定1159・終値1149（-0.86%）
- 3798 momentum 指定543 → 約定543・終値560（+3.13%）
- 5038 momentum 指定2331 → 約定2331・終値2383（+2.23%）
- 7567 momentum 指定639 → 約定639・終値614（-3.91%）
- 3843 momentum 指定1772 → 約定1773・終値1769（-0.23%）
- 7161 momentum 指定589 → 約定589・終値558（-5.26%）
- 8393 reversal 指定2462 → 約定2462・終値2356（-4.31%）
- 1952 reversal 指定2986 → 約定2986・終値2970（-0.54%）
- 6269 reversal 指定8027 → 約定8026・終値7858（-2.09%）
- 5631 reversal 指定6460 → 約定6456・終値6251（-3.18%）
- 1662 reversal 指定1699 → 約定1690・終値1715（+1.48%）
- 8194 reversal 指定2378 → 約定2370・終値2411（+1.73%）
- 7381 reversal 指定1176 → 約定1176・終値1123（-4.51%）
- 8345 reversal 指定2198 → 約定2198・終値2055（-6.51%）
- 8399 reversal 指定2863 → 約定2863・終値2764（-3.46%）
- 7384 reversal 指定4230 → 約定4230・終値3920（-7.33%）
- 8304 reversal 指定3103 → 約定3103・終値3023（-2.58%）
- 6643 reversal 指定5270 → 約定5220・終値5140（-1.53%）
- 5254 momentum 指定4100 → 約定4100・終値3985（-2.80%）
- 9064 momentum 指定2062 → 約定2062・終値2069.5（+0.36%）
- 6328 momentum 指定2473 → 約定2475・終値2478（+0.12%）
- 456A oshime 指定1858.6 → 約定1858.6・終値1880（+1.15%）
- 9166 oshime 指定673.5 → 約定673.5・終値660（-2.00%）
- 3691 reversal 指定1693 → 約定1684・終値1626（-3.44%）
- 6963 reversal 指定3958 → 約定3930・終値3758（-4.38%）
- 8524 reversal 指定1159 → 約定1153・終値1127（-2.25%）
- 3653 reversal 指定907 → 約定894・終値885（-1.01%）
- 8360 reversal 指定1301 → 約定1300・終値1248（-4.00%）
- 3778 reversal 指定3160 → 約定3160・終値2895（-8.39%）
- 8366 reversal 指定2694 → 約定2694・終値2573（-4.49%）
- 8368 reversal 指定2186 → 約定2186・終値2089（-4.44%）
- 8713 reversal 指定2433 → 約定2433・終値2377（-2.30%）
- 7695 changepoint 指定885 → 約定879・終値875（-0.46%）
- 4382 changepoint 指定1631 → 約定1631・終値1640（+0.55%）
- 9888 changepoint 指定1182 → 約定1176・終値1477（+25.60%）
- 5590 changepoint 指定675 → 約定671・終値661（-1.49%）
- 478A changepoint 指定680 → 約定680・終値673（-1.03%）
- 218A changepoint 指定930 → 約定930・終値891（-4.19%）
- 593A changepoint 指定2010 → 約定2010・終値1943（-3.33%）
- 339A changepoint 指定825 → 約定820・終値824（+0.49%）

## 模擬テンプレ
```
# base_day 2026-10-22 ／ 提案23件
# 使い方: 参戦する0〜3銘柄の行だけをコピーし、｜の後ろに参戦理由を書いてポジション株PJへ送る。
# 選ばなかった行は送らなくてよい（全行に理由を書く必要はない）。見送りは末尾の1行で足りる。
# 特定銘柄を理由つきで見送る場合のみ『模擬 見送り {code} ｜{理由}』を送る。
模擬 5034 kenmo_momentum 逆指値2841 SL2669.6 単元100 ｜
模擬 4743 kenmo_momentum 逆指値1693 SL1590.5 単元100 ｜
模擬 3222 choruko_reversal 指値769 SL729 単元100 ｜
模擬 8987 choruko_reversal 指値124200 SL122700 単元1 ｜
模擬 8198 choruko_reversal 指値3165 SL3100 単元100 ｜
模擬 2659 choruko_reversal 指値3185 SL3095 単元100 ｜
模擬 5021 choruko_reversal 指値4283 SL4079 単元100 ｜
模擬 8276 choruko_reversal 指値2579 SL2498 単元100 ｜
模擬 9974 choruko_reversal 指値6360 SL5980 単元100 ｜
模擬 3234 choruko_reversal 指値116400 SL115300 単元1 ｜
模擬 3249 choruko_reversal 指値126800 SL125600 単元1 ｜
模擬 3283 choruko_reversal 指値79900 SL77900 単元1 ｜
模擬 8955 choruko_reversal 指値90000 SL89100 単元1 ｜
模擬 8961 choruko_reversal 指値66900 SL66000 単元1 ｜
模擬 6183 choruko_reversal 指値1376 SL1314 単元100 ｜
模擬 4928 choruko_reversal 指値4695 SL4635 単元100 ｜
模擬 1662 choruko_reversal 指値1715 SL1669 単元100 ｜
模擬 8174 choruko_reversal 指値933.4 SL895.4 単元100 ｜
模擬 3591 choruko_reversal 指値3576 SL3522 単元100 ｜
模擬 6432 granville_tenkan 逆指値7880 SL7397.8 単元100 ｜
模擬 9888 変化点🔔🔔 指値1477 SL1160 単元100 🔒 ｜
模擬 4498 変化点🔔🔔 指値2560 SL1570 単元100 🔒 ｜
模擬 4493 変化点 指値3865 SL2995 単元100 ｜
模擬 見送り ｜
```

## PASS内訳
PASS 36件 = 発注可能 23件 + 除外 13件（型不一致1/材料後出し0/鮮度切れ10/その他2）
- 7811 Nakamoto Packs Co. Ltd.｜⛔提案なし(手法ブランチ不明)
- 4176 ココナラ｜⛔提案なし(手法ブランチ不明)
- 9044 NANKAI Co., Ltd.｜⛔型不一致: 既に支持帯以下
- 鮮度切れ（コードとnom_age）: 9006(17営業日)、4763(12営業日)、2288(17営業日)、6988(15営業日)、8060(19営業日)、8850(15営業日)、1879(15営業日)、3107(12営業日)、9616(15営業日)、9900(14営業日)

## 5手法銘柄
- 6627 Tera Probe, Inc.｜kenmo_momentum｜🚀確変(13)｜💎割安｜FAIL_INSEN｜1,807円｜💰21.1万円｜—
- 5137 Smart Drive Co. Ltd.｜kenmo_momentum｜🚀確変(12)｜💎割安｜FAIL_INSEN｜302円｜💰3.1万円｜—
- 276A CCReB Advisors Inc.｜granville_oshime/kenmo_momentum｜🚀確変(12)｜⚪妥当｜FAIL_INSEN｜4,310円｜💰44.8万円｜—
- 3556 RenetJapanGroup, Inc.｜kenmo_momentum｜🚀確変(11)｜💎割安｜FAIL_INSEN｜916円｜💰7.9万円｜—
- 6862 Minato Holdings Inc.｜kenmo_momentum/granville_rebound｜🚀確変(11)｜🟢値頃｜FAIL_INSEN｜4,005円｜💰47.0万円｜—
- 4053 Sun Asterisk, Inc.｜kenmo_momentum｜🚀確変(11)｜⚪妥当｜FAIL_UWAHIGE｜603円｜💰5.8万円｜—
- 4434 Serverworks Co., Ltd.｜kenmo_momentum/stf_kakuhen｜🚀確変(11)｜⚪妥当｜FAIL_UWAHIGE｜3,135円｜💰30.4万円｜—
- 5027 AnyMind Group Inc.｜kenmo_momentum｜🚀確変(11)｜⚪妥当｜FAIL_INSEN｜767円｜💰8.1万円｜—
- 5136 tripla Co.,Ltd.｜kenmo_momentum/changepoint🔔🔔｜🚀確変(11)｜⚪妥当｜FAIL_INSEN｜2,597円｜💰27.0万円｜—
- 5757 CK San-Etsu Co., Ltd.｜kenmo_momentum｜🔥絶好調(10)｜💎割安｜FAIL_INSEN｜4,600円｜💰46.9万円｜—
- 212A FIT EASY Inc.｜kenmo_momentum/granville_oshime｜🔥絶好調(10)｜⚪妥当｜FAIL_INSEN｜2,731円｜💰28.5万円｜—
- 618A KOMPEITO Inc.｜kenmo_momentum｜🔥絶好調(10)｜⚪妥当｜FAIL_UWAHIGE｜1,965円｜💰18.9万円｜—
- 9554 AViC Co. Ltd.｜kenmo_momentum/granville_tenkan｜🔥絶好調(10)｜⚪妥当｜FAIL_INSEN｜1,598円｜💰17.2万円｜—
- 421A Movin' Strategic Career CO.,LTD.｜kenmo_momentum/kenmo_newhigh｜🔥絶好調(10)｜⚪妥当｜FAIL_INSEN｜4,285円｜💰44.3万円｜—
- 5132 pluszero,Inc.｜kenmo_momentum｜🔥絶好調(9)｜🟢値頃｜FAIL_INSEN｜1,859円｜💰19.6万円｜—
- 6298 Y.A.C.HOLDINGS CO.,LTD.｜kenmo_momentum｜🔥絶好調(9)｜🟢値頃｜FAIL_INSEN｜1,106円｜💰11.6万円｜—
- 4377 ONE CAREER Inc.｜kenmo_momentum｜🔥絶好調(9)｜⚪妥当｜FAIL_UWAHIGE｜2,668円｜💰26.7万円｜—
- 5537 AlbaLink Co.,Ltd.｜kenmo_momentum｜🔥絶好調(9)｜⚪妥当｜FAIL_INSEN｜3,560円｜💰39.0万円｜—
- 9556 INTLOOP, Inc.｜kenmo_momentum｜🔥絶好調(8)｜💎割安｜FAIL_INSEN｜2,125円｜💰22.6万円｜—
- 7047 PORT INC.｜kenmo_momentum｜🔥絶好調(8)｜💎割安｜FAIL_INSEN｜2,040円｜💰21.7万円｜—
- 3915 TerraSky Co., Ltd.｜kenmo_momentum｜🔥絶好調(8)｜🟢値頃｜FAIL_INSEN｜2,412円｜💰22.2万円｜—
- 5821 Hirakawa Hewtech Corp.｜kenmo_momentum｜⚡好調(7)｜💎割安｜FAIL_INSEN｜3,065円｜💰30.9万円｜—
- 4058 Toyokumo, Inc.｜kenmo_momentum｜⚡好調(7)｜⚪妥当｜FAIL_UWAHIGE｜2,332円｜💰23.1万円｜—
- 6071 IBJ, Inc.｜kenmo_momentum｜⚡好調(7)｜⚪妥当｜FAIL_UWAHIGE｜915円｜💰9.3万円｜—
- 5034 unerry, Inc.｜kenmo_momentum｜⚡好調(7)｜⚪妥当｜PASS｜2,822円｜💰28.2万円｜momentum 2841 想定損失幅6.0%。｜📋カルテ窓 11/12(残14営業日)
  > 【業態】人流データによるビッグデータプラットフォームの運営。企業のDX化を支援。
  > 【いま】終値2,822円・直近5日+9.21%（材料未確認）
  > 【調子】⚡好調（7/13） — 質注意
  > 【水準】⚪妥当（3.0/7）— PER25.75倍・PEG0.9117・52週46.7% ／ 💰単元28.2万円
  > 【戦略】当日高値超えの逆指値2,841円で順張り参戦を検討。上限2,869.4円・SL2,669.6円目安
- 9560 PROGRIT, Inc.｜kenmo_momentum｜⚡好調(7)｜⚪妥当｜FAIL_INSEN｜1,073円｜💰11.2万円｜—
- 558A SQUEEZE Inc.｜kenmo_momentum/kenmo_newhigh｜⚡好調(7)｜🟡やや割高｜FAIL_INSEN｜5,590円｜💰58.2万円｜—
- 147A SORACOM,INC.｜kenmo_momentum｜⚡好調(7)｜🟡やや割高｜FAIL_INSEN｜940円｜💰9.8万円｜—
- 7678 ASAKUMA CO.,LTD.｜kenmo_momentum｜⚡好調(7)｜🔴過熱｜FAIL_INSEN｜3,710円｜💰37.9万円｜—
- 9268 OPTIMUS GROUP Co., Ltd.｜kenmo_momentum｜⚡好調(6)｜💎割安｜FAIL_INSEN｜332円｜💰3.5万円｜—
- 4477 BASE, Inc.｜kenmo_momentum/granville_oshime｜⚡好調(6)｜🟡やや割高｜FAIL_INSEN｜350円｜💰3.9万円｜—
- 9628 San Holdings,Inc.｜kenmo_momentum｜⚡好調(6)｜🟡やや割高｜FAIL_INSEN｜1,204円｜💰13.3万円｜—
- 2980 SRE Holdings Corp.｜kenmo_momentum｜⚡好調(5)｜🟢値頃｜FAIL_INSEN｜2,297円｜💰23.9万円｜—
- 4412 Science Arts, Inc.｜kenmo_momentum｜⚡好調(5)｜⚪妥当｜FAIL_INSEN｜1,315円｜💰14.4万円｜—
- 505A Geekly,Inc.｜kenmo_momentum｜✅順調(4)｜💎割安｜FAIL_INSEN｜1,149円｜💰11.6万円｜—
- 3798 ULS Group Incorporated｜kenmo_momentum/granville_tenkan｜✅順調(4)｜💎割安｜FAIL_UWAHIGE｜560円｜💰5.4万円｜—
- 4743 ITFOR Inc.｜kenmo_momentum｜✅順調(4)｜🟢値頃｜PASS｜1,687円｜💰16.9万円｜momentum 1693 想定損失幅6.1%。 移行措置銘柄: 10/30 の引けにパッシブ売り（8回に分けて低減）。実施日前後の寄り・引けの需給に注意｜📋カルテ窓 11/12(残14営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）｜📌
  > 【業態】未取得（次回以降に取得）
  > 【いま】終値1,687円・直近5日+3.31%・📌（訂正）2026年10月14日に公表したPR情報の一部訂正について
  > 【調子】✅順調（4/13）
  > 【水準】🟢値頃（5.0/7）— PER13.13倍・PEG0.6291・52週69.5% ／ 💰単元16.9万円
  > 【戦略】当日高値超えの逆指値1,693円で順張り参戦を検討。上限1,709.9円・SL1,590.5円目安
- 5038 eWeLL Co.,Ltd｜kenmo_momentum｜✅順調(4)｜⚪妥当｜FAIL_UWAHIGE｜2,383円｜💰23.1万円｜—
- 6629 TECHNO HORIZON Co., Ltd.｜granville_tenkan/kenmo_momentum｜✅順調(4)｜⚪妥当｜FAIL_INSEN｜962円｜💰9.8万円｜—
- 6289 Giken Ltd.｜granville_tenkan/kenmo_momentum｜⚠減速(1)｜🔴過熱｜FAIL_UWAHIGE｜2,051円｜💰20.4万円｜—
- 3077 Horiifoodservice Co., Ltd.｜kenmo_momentum/granville_rebound｜判定保留(変則決算)(None)｜None｜FAIL_INSEN｜1,151円｜💰0.0万円｜—
- 6918 Aval Data Corporation｜kenmo_newhigh/granville_rebound｜🚀確変(13)｜⚪妥当｜FAIL_INSEN｜3,640円｜💰39.5万円｜—
- 7567 Sakae Electronics Corp.｜kenmo_newhigh｜🚀確変(12)｜⚪妥当｜FAIL_INSEN｜614円｜💰6.3万円｜—
- 269A SAPEET｜kenmo_newhigh｜🚀確変(11)｜⚪妥当｜FAIL_INSEN｜2,886円｜💰29.0万円｜—
- 6337 Tesec Corporation｜kenmo_newhigh｜🚀確変(11)｜⚪妥当｜FAIL_INSEN｜3,160円｜💰34.4万円｜—
- 3696 セレス｜kenmo_newhigh｜🔥絶好調(8)｜🟢値頃｜FAIL_INSEN｜2,288円｜💰23.8万円｜—
- 2930 北の達人コーポレーション｜kenmo_newhigh｜⚡好調(6)｜🔴過熱｜FAIL_INSEN｜151円｜💰1.5万円｜—
- 2820 Yamami Co.｜kenmo_newhigh｜✅順調(4)｜🟡やや割高｜FAIL_INSEN｜6,570円｜💰67.8万円｜—
- 3843 Freebit Co., Ltd.｜kenmo_newhigh/granville_tenkan｜✅順調(3)｜⚪妥当｜FAIL_INSEN｜1,769円｜💰17.6万円｜—
- 4331 Take and Give. Needs Co., Ltd.｜kenmo_newhigh｜✅順調(3)｜🟡やや割高｜FAIL_INSEN｜813円｜💰8.2万円｜—
- 7161 Jimoto Holdings, Inc.｜kenmo_newhigh｜業績データ取得不可(None)｜⚪妥当｜FAIL_INSEN｜558円｜💰5.9万円｜—
- 4565 Nxera Pharma Co., Ltd.｜granville_oshime/kenmo_newhigh｜業績データ取得不可(経常益予想非開示)(None)｜🟡やや割高｜FAIL_INSEN｜1,298円｜💰12.5万円｜—
- 2340 Gokurakuyu Holdings Co., Ltd.｜kenmo_newhigh｜業績データ取得不可(None)｜⏸判定不能｜FAIL_INSEN｜505円｜💰5.1万円｜—
- 4379 Photosynth inc.｜kenmo_newhigh｜None(None)｜None｜FAIL_UWAHIGE｜554円｜💰0.0万円｜—
- 446A ノースサンド｜kenmo_newhigh｜None(None)｜None｜FAIL_INSEN｜2,779円｜💰0.0万円｜—
- 8871 GOLDCREST Co., Ltd.｜choruko_reversal｜🔥絶好調(10)｜💎割安｜FAIL_UWAHIGE｜2,862円｜💰29.3万円｜—
- 3391 TSURUHA Holdings, Inc.｜choruko_reversal｜🔥絶好調(10)｜🟢値頃｜FAIL_INSEN｜2,182.5円｜💰22.6万円｜—
- 3186 ネクステージ｜choruko_reversal｜🔥絶好調(9)｜💎割安｜FAIL_INSEN｜2,511円｜💰25.9万円｜—
- 6268 Nabtesco Corporation｜choruko_reversal｜🔥絶好調(9)｜⚪妥当｜FAIL_INSEN｜4,166円｜💰49.3万円｜—
- 6324 Harmonic Drive Systems Inc.｜choruko_reversal｜🔥絶好調(9)｜⚪妥当｜FAIL_INSEN｜4,875円｜💰53.0万円｜—
- 3222 United Super Markets Holdings, Inc.｜choruko_reversal｜🔥絶好調(9)｜🔴過熱｜PASS｜769円｜💰7.7万円｜reversal 769 想定損失幅5.2%。｜⚠日程不明｜織り込み済みの可能性（押し目待ち推奨圏）
  > 【業態】イオン系、首都圏の食品スーパー最大手。マルエツ、カスミ、マックスバリュ関東が統合。
  > 【いま】終値769円・直近5日+2.12%（材料未確認）
  > 【調子】🔥絶好調（9/13）
  > 【水準】🔴過熱（2.0/7）— PER1098.57倍・PEG11.5058・52週16.2% ／ 💰単元7.7万円
  > 【戦略】当日終値769円の指値で反転を取りにいく。SL729円（直近5日安値）
- 1803 Shimizu Corporation｜choruko_reversal｜🔥絶好調(8)｜💎割安｜FAIL_INSEN｜2,011円｜💰20.2万円｜—
- 4023 クレハ｜choruko_reversal｜🔥絶好調(8)｜🟢値頃｜FAIL_INSEN｜3,880円｜💰38.5万円｜—
- 7733 Olympus Corp.｜choruko_reversal｜🔥絶好調(8)｜⚪妥当｜FAIL_UWAHIGE｜1,683円｜💰17.3万円｜—
- 5301 Tokai Carbon Co., Ltd.｜choruko_reversal｜🔥絶好調(8)｜⚪妥当｜FAIL_INSEN｜1,886.5円｜💰18.2万円｜—
- 7004 Kanadevia Corporation｜choruko_reversal｜⚠減速(7)｜💎割安｜FAIL_INSEN｜1,046円｜💰10.9万円｜—
- 2874 YOKOREI CO. LTD.｜granville_rebound/choruko_reversal｜⚠減速(7)｜🟢値頃｜FAIL_INSEN｜1,711円｜💰17.6万円｜—
- 8522 Bank of Nagoya, Ltd.｜choruko_reversal｜⚡好調(7)｜🟢値頃｜FAIL_INSEN｜5,920円｜💰63.0万円｜—
- 8987 Japan Excellent, Inc.｜choruko_reversal｜⚡好調(6)｜🟢値頃｜PASS｜124,200円｜💰12.4万円｜reversal 124200 想定損失幅1.2%。｜⚠日程不明
  > 【業態】大都市のオフィスビル中心に投資。日鉄興和不動産、第一ライフ、みずほFGが出資。
  > 【いま】終値124,200円・直近5日-1.04%（材料未確認）
  > 【調子】⚡好調（6/13）
  > 【水準】🟢値頃（5.6/7）— PER28.99倍・PEG1.0698・52週4.4% ／ 💰単元12.4万円
  > 【戦略】当日終値124,200円の指値で反転を取りにいく。SL122,700円（直近5日安値）
- 8282 K'S HOLDINGS CORPORATION｜choruko_reversal｜⚡好調(6)｜🟢値頃｜FAIL_UWAHIGE｜1,714円｜💰17.4万円｜—
- 8088 IWATANI Corporation｜choruko_reversal｜⚡好調(6)｜⚪妥当｜FAIL_INSEN｜1,883円｜💰19.4万円｜—
- 8386 Hyakujushi Bank, Ltd.｜choruko_reversal/granville_rebound｜⚡好調(6)｜⚪妥当｜FAIL_INSEN｜2,662円｜💰28.5万円｜—
- 9412 SKY Perfect JSAT Corporation｜choruko_reversal｜⚡好調(6)｜⚪妥当｜FAIL_INSEN｜1,866円｜💰19.2万円｜—
- 8125 Wakita & Co., Ltd.｜choruko_reversal｜⚡好調(6)｜🔴過熱｜FAIL_UWAHIGE｜1,860円｜💰18.5万円｜—
- 9861 吉野家ホールディングス｜choruko_reversal｜⚡好調(6)｜🔴過熱｜FAIL_INSEN｜4,279円｜💰44.6万円｜—
- 4666 Park24 Co., Ltd.｜choruko_reversal｜⚡好調(5)｜💎割安｜FAIL_INSEN｜1,791円｜💰18.0万円｜—
- 7721 Tokyo Keiki Inc.｜choruko_reversal｜⚡好調(5)｜🟢値頃｜FAIL_INSEN｜5,730円｜💰63.5万円｜—
- 8278 Fuji Co., Ltd.｜choruko_reversal｜⚡好調(5)｜🟢値頃｜FAIL_UWAHIGE｜1,973円｜💰19.6万円｜—
- 8381 San-in Godo Bank Ltd.｜choruko_reversal/granville_rebound｜⚡好調(5)｜⚪妥当｜FAIL_INSEN｜2,097円｜💰23.0万円｜—
- 8954 ORIX JREIT Inc.｜choruko_reversal｜⚡好調(5)｜⚪妥当｜FAIL_INSEN｜88,600円｜💰8.8万円｜—
- 8393 Miyazaki Bank Ltd.｜choruko_reversal｜⚡好調(5)｜⚪妥当｜FAIL_INSEN｜2,356円｜💰24.6万円｜—
- 268A Rigaku Holdings Corporation｜choruko_reversal｜⚡好調(5)｜⚪妥当｜FAIL_INSEN｜1,407円｜💰16.7万円｜—
- 7458 Daiichikosho Co., Ltd.｜choruko_reversal｜⚡好調(5)｜⚪妥当｜FAIL_UWAHIGE｜1,766円｜💰17.6万円｜—
- 2702 日本マクドナルドホールディングス｜choruko_reversal｜⚠減速(5)｜🔴過熱｜FAIL_UWAHIGE｜8,250円｜💰79.1万円｜—
- 2782 Seria Co., Ltd.｜choruko_reversal｜⚡好調(5)｜🔴過熱｜FAIL_UWAHIGE｜4,225円｜💰41.6万円｜—
- 2809 Kewpie Corporation｜choruko_reversal｜⚡好調(5)｜🔴過熱｜FAIL_UWAHIGE｜4,543円｜💰45.7万円｜—
- 3279 Activia Properties, Inc.｜choruko_reversal｜✅順調(4)｜⚪妥当｜FAIL_UWAHIGE｜123,600円｜💰12.5万円｜—
- 8524 North Pacific Bank, Ltd.｜granville_rebound/choruko_reversal｜⚠減速(4)｜⚪妥当｜FAIL_INSEN｜1,127円｜💰11.6万円｜—
- 3282 Comforia Residential REIT, Inc.｜choruko_reversal｜✅順調(4)｜🟡やや割高｜FAIL_INSEN｜88,400円｜💰8.9万円｜—
- 8952 Japan Real Estate Investment Corp.｜choruko_reversal｜✅順調(4)｜🟡やや割高｜FAIL_INSEN｜105,800円｜💰10.8万円｜—
- 6925 Ushio Inc.｜choruko_reversal｜✅順調(4)｜🔴過熱｜FAIL_INSEN｜3,365円｜💰35.4万円｜—
- 1861 Kumagai Gumi Co., Ltd.｜choruko_reversal｜✅順調(3)｜💎割安｜FAIL_INSEN｜1,205円｜💰12.2万円｜—
- 1417 MIRAIT ONE Corporation｜choruko_reversal｜✅順調(3)｜🟢値頃｜FAIL_INSEN｜3,336円｜💰33.7万円｜—
- 3148 Create SD Holdings Co., Ltd.｜choruko_reversal｜✅順調(3)｜⚪妥当｜FAIL_UWAHIGE｜3,200円｜💰32.1万円｜—
- 8198 Maxvalu Tokai Co., Ltd.｜choruko_reversal｜✅順調(3)｜⚪妥当｜PASS｜3,165円｜💰31.6万円｜reversal 3165 想定損失幅2.1%。｜⚠日程不明
  > 【業態】イオン系の食品スーパー。旧ヤオハンを母体に静岡県を中心とする出店。
  > 【いま】終値3,165円・直近5日+1.44%（材料未確認）
  > 【調子】✅順調（3/13）
  > 【水準】⚪妥当（4.0/7）— PER10.85倍・PEG1.6089・52週10.8% ／ 💰単元31.6万円
  > 【戦略】当日終値3,165円の指値で反転を取りにいく。SL3,100円（直近5日安値）
- 1820 Nishimatsu Construction Co., Ltd.｜choruko_reversal｜✅順調(3)｜⚪妥当｜FAIL_UWAHIGE｜5,335円｜💰52.9万円｜—
- 1952 Shin Nippon Air Technologies Co., Ltd.｜choruko_reversal｜✅順調(3)｜⚪妥当｜FAIL_INSEN｜2,970円｜💰29.9万円｜—
- 6269 Modec, Inc.｜choruko_reversal｜✅順調(3)｜⚪妥当｜FAIL_INSEN｜7,858円｜💰80.3万円｜—
- 7003 Mitsui ES Holdings Co., Ltd.｜choruko_reversal｜✅順調(3)｜⚪妥当｜FAIL_INSEN｜3,558円｜💰38.3万円｜—
- 8584 Jaccs Co., Ltd.｜choruko_reversal｜🔻悪化(3)｜⚪妥当｜FAIL_INSEN｜3,420円｜💰34.9万円｜—
- 9882 Yellow Hat Ltd.｜choruko_reversal｜✅順調(3)｜⚪妥当｜FAIL_UWAHIGE｜1,611円｜💰16.3万円｜—
- 1860 Toda Corporation｜choruko_reversal｜✅順調(3)｜🟡やや割高｜FAIL_UWAHIGE｜1,415円｜💰14.1万円｜—
- 1944 Kinden Corporation｜choruko_reversal｜✅順調(3)｜🟡やや割高｜FAIL_INSEN｜6,325円｜💰64.7万円｜—
- 8066 Mitani Corporation｜granville_rebound/choruko_reversal｜⚠減速(3)｜🟡やや割高｜FAIL_INSEN｜2,962円｜💰31.4万円｜—
- 2659 SAN-A CO., LTD.｜choruko_reversal｜✅順調(3)｜🔴過熱｜PASS｜3,185円｜💰31.9万円｜reversal 3185 想定損失幅2.8%。｜⚠日程不明
  > 【業態】沖縄県内流通首位。スーパー、レストラン、ドラッグストアを展開。ローソンと提携。ニチリウG。
  > 【いま】終値3,185円・直近5日+2.91%（材料未確認）
  > 【調子】✅順調（3/13） — 質注意
  > 【水準】🔴過熱（1.0/7）— PER17.25倍・PEG14.8097・52週64.0% ／ 💰単元31.9万円
  > 【戦略】当日終値3,185円の指値で反転を取りにいく。SL3,095円（直近5日安値）
- 2805 S&B Foods Inc.｜granville_rebound/choruko_reversal｜✅順調(3)｜🔴過熱｜FAIL_INSEN｜6,020円｜💰63.3万円｜—
- 5021 Cosmo Energy Holdings Co., Ltd.｜choruko_reversal｜🔻悪化(3)｜🔴過熱｜PASS｜4,283円｜💰42.8万円｜reversal 4283 想定損失幅4.8%。｜📋カルテ窓 11/10(残12営業日)｜⚠業績基調が下向き（🔻悪化）
  > 【業態】石油元売り大手。石油化学、石油開発、再生エネルギーなど多角。岩谷産業系。
  > 【いま】終値4,283円・直近5日+5.26%（材料未確認）
  > 【調子】🔻悪化（3/13） — 質注意
  > 【水準】🔴過熱（1.0/7）— PER15.46倍・PEG—・52週53.9% ／ 💰単元42.8万円
  > 【戦略】当日終値4,283円の指値で反転を取りにいく。SL4,079円（直近5日安値）
- 6055 Japan Material Co., Ltd.｜choruko_reversal｜✅順調(3)｜🔴過熱｜FAIL_INSEN｜1,980円｜💰21.5万円｜—
- 7984 Kokuyo Co., Ltd.｜choruko_reversal｜✅順調(3)｜🔴過熱｜FAIL_UWAHIGE｜886.2円｜💰8.9万円｜—
- 3289 Tokyu Fudosan Holdings Corp.｜choruko_reversal｜➖横ばい(2)｜💎割安｜FAIL_INSEN｜1,205円｜💰12.1万円｜—
- 8818 Keihanshin Building Co., Ltd.｜choruko_reversal｜➖横ばい(2)｜⚪妥当｜FAIL_UWAHIGE｜928円｜💰9.4万円｜—
- 1333 Umios Corporation｜choruko_reversal｜➖横ばい(2)｜⚪妥当｜FAIL_UWAHIGE｜1,208円｜💰12.0万円｜—
- 1719 HAZAMA ANDO Corporation｜choruko_reversal｜➖横ばい(2)｜⚪妥当｜FAIL_INSEN｜1,759.5円｜💰17.5万円｜—
- 1833 Okumura Corporation｜choruko_reversal｜⚠減速(2)｜⚪妥当｜FAIL_INSEN｜5,280円｜💰52.7万円｜—
- 9503 Kansai Electric Power Company, Incorporated｜choruko_reversal/granville_rebound｜🔻悪化(2)｜⚪妥当｜FAIL_INSEN｜2,739円｜💰27.2万円｜—
- 8953 Japan Metropolitan Fund Investment Corporation｜choruko_reversal｜➖横ばい(2)｜🟡やや割高｜FAIL_UWAHIGE｜103,200円｜💰10.4万円｜—
- 6366 Chiyoda Corp.｜choruko_reversal｜🔻悪化(2)｜🟡やや割高｜FAIL_INSEN｜583円｜💰6.2万円｜—
- 7220 Musashi Seimitsu Industry Co., Ltd.｜choruko_reversal｜🔻悪化(2)｜🟡やや割高｜FAIL_INSEN｜2,456円｜💰31.4万円｜—
- 5844 Kyoto Financial Group,Inc.｜choruko_reversal｜🔻悪化(2)｜🔴過熱｜FAIL_INSEN｜4,113円｜💰42.5万円｜—
- 2379 dip Corporation｜choruko_reversal｜⚠減速(1)｜💎割安｜FAIL_INSEN｜1,445円｜💰16.6万円｜—
- 6479 MinebeaMitsumi Inc.｜choruko_reversal｜⚠減速(1)｜⚪妥当｜FAIL_INSEN｜3,129円｜💰38.1万円｜—
- 1893 Penta-Ocean Construction Co., Ltd.｜choruko_reversal｜⚠減速(1)｜⚪妥当｜FAIL_INSEN｜1,342円｜💰13.5万円｜—
- 6753 Sharp Corporation｜choruko_reversal｜🔻悪化(1)｜⚪妥当｜FAIL_UWAHIGE｜599円｜💰5.9万円｜—
- 8276 HEIWADO CO., LTD.｜choruko_reversal｜⚠減速(1)｜⚪妥当｜PASS｜2,579円｜💰25.8万円｜reversal 2579 想定損失幅3.1%。｜⚠日程不明｜⚠業績基調が下向き（⚠減速）
  > 【業態】滋賀地盤のスーパー。大型店が主力。ドミナント戦略で拡大。中国に百貨店進出。
  > 【いま】終値2,579円・直近5日+2.50%（材料未確認）
  > 【調子】⚠減速（1/13）
  > 【水準】⚪妥当（3.0/7）— PER13.01倍・PEG3.1940・52週24.1% ／ 💰単元25.8万円
  > 【戦略】当日終値2,579円の指値で反転を取りにいく。SL2,498円（直近5日安値）
- 9948 Arcs Company, Limited｜choruko_reversal｜⚠減速(1)｜⚪妥当｜FAIL_UWAHIGE｜3,470円｜💰34.4万円｜—
- 9974 BELC Co., Ltd.｜choruko_reversal｜⚠減速(1)｜⚪妥当｜PASS｜6,360円｜💰63.6万円｜reversal 6360 想定損失幅6.0%。 ⚠1単元リスク38,000円（枠超過）｜⚠日程不明｜⚠業績基調が下向き（⚠減速）｜⚠1単元でリスク枠超過（38,000円）
  > 【業態】埼玉地盤に食品スーパー「ベルク」を展開。自社物流などに強み。イオンと提携。
  > 【いま】終値6,360円・直近5日+4.61%（材料未確認）
  > 【調子】⚠減速（1/13） — 質注意
  > 【水準】⚪妥当（3.0/7）— PER13.38倍・PEG—・52週17.5% ／ 💰単元63.6万円
  > 【戦略】当日終値6,360円の指値で反転を取りにいく。SL5,980円（直近5日安値）／⚠1単元リスク38,000円（枠超過）
- 3234 Mori Hills Reit Investment Corporation｜choruko_reversal｜⚠減速(1)｜🟡やや割高｜PASS｜116,400円｜💰11.6万円｜reversal 116400 想定損失幅0.9%。｜⚠日程不明｜⚠業績基調が下向き（⚠減速）
  > 【業態】東京都心5区のオフィス中心に商業施設・住居に投資。運用:森ビル・インベスト。
  > 【いま】終値116,400円・直近5日-2.43%（材料未確認）
  > 【調子】⚠減速（1/13） — 質注意
  > 【水準】🟡やや割高（2.8/7）— PER39.45倍・PEG—・52週3.0% ／ 💰単元11.6万円
  > 【戦略】当日終値116,400円の指値で反転を取りにいく。SL115,300円（直近5日安値）
- 3249 Industrial & Infrastructure Fund Investment Corporation｜choruko_reversal｜⚠減速(1)｜🟡やや割高｜PASS｜126,800円｜💰12.7万円｜reversal 126800 想定損失幅0.9%。｜⚠日程不明｜⚠業績基調が下向き（⚠減速）
  > 【業態】産業用不動産、物流施設やインフラ不動産へ投資。運用:KJRマネジメント。
  > 【いま】終値126,800円・直近5日-1.17%（材料未確認）
  > 【調子】⚠減速（1/13） — 質注意
  > 【水準】🟡やや割高（2.8/7）— PER33.05倍・PEG—・52週6.4% ／ 💰単元12.7万円
  > 【戦略】当日終値126,800円の指値で反転を取りにいく。SL125,600円（直近5日安値）
- 3283 Nippon Prologis REIT, Inc.｜choruko_reversal｜⚠減速(1)｜🟡やや割高｜PASS｜79,900円｜💰8.0万円｜reversal 79900 想定損失幅2.5%。｜⚠日程不明｜⚠業績基調が下向き（⚠減速）
  > 【業態】物流施設特化型、グループで開発した大型物流施設に投資。運用:プロロジス。
  > 【いま】終値79,900円・直近5日+0.38%（材料未確認）
  > 【調子】⚠減速（1/13）
  > 【水準】🟡やや割高（2.8/7）— PER42.02倍・PEG11.4297・52週10.0% ／ 💰単元8.0万円
  > 【戦略】当日終値79,900円の指値で反転を取りにいく。SL77,900円（直近5日安値）
- 3292 AEON REIT Investment Corp.｜choruko_reversal｜⚠減速(1)｜🟡やや割高｜FAIL_INSEN｜103,800円｜💰10.5万円｜—
- 3296 NIPPON REIT Investment Corp｜choruko_reversal｜🔻悪化(1)｜🟡やや割高｜FAIL_INSEN｜74,500円｜💰7.6万円｜—
- 3309 Sekisui House Reit. Inc.｜choruko_reversal｜⚠減速(1)｜🟡やや割高｜FAIL_UWAHIGE｜67,200円｜💰6.7万円｜—
- 3462 Nomura Real Estate Master Fund, Inc.｜choruko_reversal｜⚠減速(1)｜🟡やや割高｜FAIL_INSEN｜127,300円｜💰13.5万円｜—
- 5482 Aichi Steel Corporation｜choruko_reversal｜⚠減速(1)｜🟡やや割高｜FAIL_INSEN｜2,857円｜💰29.4万円｜—
- 8955 Japan Prime Realty Investment Corporation｜choruko_reversal｜⚠減速(1)｜🟡やや割高｜PASS｜90,000円｜💰9.0万円｜reversal 90000 想定損失幅1.0%。｜⚠日程不明｜⚠業績基調が下向き（⚠減速）
  > 【業態】東京建物系の不動産投資法人。首都圏のオフィス中心にホテル、商業施設に投資。
  > 【いま】終値90,000円・直近5日-0.33%（材料未確認）
  > 【調子】⚠減速（1/13） — 質注意
  > 【水準】🟡やや割高（2.8/7）— PER45.44倍・PEG—・52週11.2% ／ 💰単元9.0万円
  > 【戦略】当日終値90,000円の指値で反転を取りにいく。SL89,100円（直近5日安値）
- 8961 MORI TRUST REIT.Inc｜choruko_reversal｜⚠減速(1)｜🔴過熱｜PASS｜66,900円｜💰6.7万円｜reversal 66900 想定損失幅1.3%。 決算前に建てるなら反応日の引けまでに撤収（教訓⑲）｜🚨決算直前 10/23(残1営業日)｜⚠業績基調が下向き（⚠減速）
  > 【業態】東京都心部のオフィス、ホテル中心に総合型。運用:森トラスト・アセットマネジメント。
  > 【いま】終値66,900円・直近5日-0.59%（材料未確認）
  > 【調子】⚠減速（1/13） — 質注意
  > 【水準】🔴過熱（2.8/7）— PER36.91倍・PEG—・52週5.7% ／ 💰単元6.7万円
  > 【戦略】当日終値66,900円の指値で反転を取りにいく。SL66,000円（直近5日安値）
- 8986 Daiwa Securities Living Investment Corporation｜choruko_reversal｜⚠減速(1)｜🟡やや割高｜FAIL_INSEN｜82,600円｜💰8.4万円｜—
- 1946 Toenec Corporation｜choruko_reversal｜⚠減速(1)｜🟡やや割高｜FAIL_INSEN｜2,023円｜💰20.7万円｜—
- 2815 ARIAKE JAPAN Co., Ltd.｜choruko_reversal｜⚠減速(1)｜🟡やや割高｜FAIL_UWAHIGE｜5,260円｜💰52.7万円｜—
- 5631 Japan Steel Works, Ltd.｜choruko_reversal｜⚠減速(1)｜🟡やや割高｜FAIL_INSEN｜6,251円｜💰64.6万円｜—
- 6183 BELLSYSTEM24 Holdings, Inc.｜choruko_reversal｜⚠減速(1)｜🟡やや割高｜PASS｜1,376円｜💰13.8万円｜reversal 1376 想定損失幅4.5%。 移行措置銘柄: 10/30 の引けにパッシブ売り（8回に分けて低減）。実施日前後の寄り・引けの需給に注意｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）｜⚠業績基調が下向き（⚠減速）
  > 【業態】コールセンターのCRM事業を中心にBPO事業も。伊藤忠が資本参加。凸版と提携。
  > 【いま】終値1,376円・直近5日+3.23%（材料未確認）
  > 【調子】⚠減速（1/13）
  > 【水準】🟡やや割高（2.0/7）— PER12.03倍・PEG4.7685・52週40.9% ／ 💰単元13.8万円
  > 【戦略】当日終値1,376円の指値で反転を取りにいく。SL1,314円（直近5日安値）
- 4928 Noevir Holdings Co., Ltd.｜choruko_reversal｜⚠減速(1)｜🔴過熱｜PASS｜4,695円｜💰47.0万円｜reversal 4695 想定損失幅1.3%。｜📋カルテ窓 11/10(残12営業日)｜⚠業績基調が下向き（⚠減速）
  > 【業態】化粧品中堅。高級基礎化粧品が主力。医薬も。傘下に飴、ドリンク剤の常盤薬。
  > 【いま】終値4,695円・直近5日+0.32%（材料未確認）
  > 【調子】⚠減速（1/13）
  > 【水準】🔴過熱（1.0/7）— PER19.55倍・PEG88.5511・52週57.4% ／ 💰単元47.0万円
  > 【戦略】当日終値4,695円の指値で反転を取りにいく。SL4,635円（直近5日安値）
- 5310 Toyo Tanso Co., Ltd.｜choruko_reversal｜🔻悪化(1)｜🔴過熱｜FAIL_INSEN｜6,480円｜💰77.2万円｜—
- 6960 Fukuda Denshi Co., Ltd.｜choruko_reversal｜⚠減速(1)｜🔴過熱｜FAIL_INSEN｜10,540円｜💰108.6万円｜—
- 9436 Okinawa Cellular Telephone Company｜choruko_reversal｜⚠減速(1)｜🔴過熱｜FAIL_INSEN｜3,400円｜💰34.6万円｜—
- 1662 Japan Petroleum Exploration Co., Ltd.｜choruko_reversal｜🔻悪化(0)｜⚪妥当｜PASS｜1,715円｜💰17.1万円｜reversal 1715 想定損失幅2.7%。｜📋カルテ窓 11/12(残14営業日)｜⚠業績基調が下向き（🔻悪化）
  > 【業態】資源開発大手。原油・天然ガスの探鉱、開発、生産。国内で天然ガス・インフラ事業。
  > 【いま】終値1,715円・直近5日+2.45%（材料未確認）
  > 【調子】🔻悪化（0/13） — 質注意
  > 【水準】⚪妥当（4.0/7）— PER6.75倍・PEG—・52週29.9% ／ 💰単元17.1万円
  > 【戦略】当日終値1,715円の指値で反転を取りにいく。SL1,669円（直近5日安値）
- 6804 Hosiden Corp.｜choruko_reversal｜🔻悪化(0)｜⚪妥当｜FAIL_INSEN｜2,334円｜💰23.8万円｜—
- 1969 Takasago Thermal Engineering Co., Ltd.｜choruko_reversal｜⚠減速(0)｜⚪妥当｜FAIL_INSEN｜4,127円｜💰41.9万円｜—
- 8585 Orient Corporation｜choruko_reversal｜⚠減速(0)｜⚪妥当｜FAIL_UWAHIGE｜760円｜💰7.8万円｜—
- 8194 Life Corporation｜choruko_reversal｜⚠減速(0)｜🟡やや割高｜FAIL_UWAHIGE｜2,411円｜💰24.1万円｜—
- 9533 TOHO GAS Co., Ltd.｜choruko_reversal｜🔻悪化(0)｜🟡やや割高｜FAIL_UWAHIGE｜1,210.5円｜💰11.8万円｜—
- 9699 NISHIO HOLDINGS CO. LTD.｜choruko_reversal｜⚠減速(0)｜🟡やや割高｜FAIL_UWAHIGE｜4,295円｜💰43.0万円｜—
- 8253 Credit Saison Co., Ltd.｜choruko_reversal｜取得不可(None)｜💎割安｜FAIL_INSEN｜4,180円｜💰41.9万円｜—
- 5831 Shizuoka Financial Group, Inc.｜choruko_reversal/granville_rebound｜取得不可(None)｜🟢値頃｜FAIL_INSEN｜2,952.5円｜💰31.8万円｜—
- 7201 Nissan Motor Co., Ltd.｜choruko_reversal｜業績データ取得不可(経常益予想非開示)(None)｜🟢値頃｜FAIL_INSEN｜269.6円｜💰2.8万円｜—
- 7381 CCI Group, Inc.｜choruko_reversal｜取得不可(None)｜🟢値頃｜FAIL_INSEN｜1,123円｜💰11.8万円｜—
- 8345 Bank of Iwate Ltd.｜choruko_reversal｜業績データ取得不可(売上/経常欠損)(None)｜🟢値頃｜FAIL_INSEN｜2,055円｜💰22.0万円｜—
- 3471 Mitsui Fudosan Logistics Park, Inc.｜choruko_reversal｜判定保留(変則決算)(None)｜⚪妥当｜FAIL_INSEN｜97,000円｜💰9.8万円｜—
- 8399 Bank Of The Ryukyus,Limited｜choruko_reversal｜業績データ取得不可(売上/経常欠損)(None)｜⚪妥当｜FAIL_INSEN｜2,764円｜💰28.6万円｜—
- 7384 Procrea Holdings,Inc.｜granville_rebound/choruko_reversal｜業績データ取得不可(売上/経常欠損)(None)｜⚪妥当｜FAIL_INSEN｜3,920円｜💰42.3万円｜—
- 8174 NIPPON GAS Co., Ltd.｜choruko_reversal｜業績データ取得不可(None)｜⚪妥当｜PASS｜933.4円｜💰9.3万円｜reversal 933.4 想定損失幅4.1%。 決算前に建てるなら反応日の引けまでに撤収（教訓⑲）｜⏰決算 10/29(残5営業日)
  > 【業態】LPG、都市ガス、電力を販売。関東一円展開。家庭エネ販売一元化。M&Aで拡販。
  > 【いま】終値933.4円・直近5日+2.99%（材料未確認）
  > 【調子】業績データ取得不可
  > 【水準】⚪妥当（4.0/7）— PER21.31倍・PEG—・52週28.8% ／ 💰単元9.3万円
  > 【戦略】当日終値933.4円の指値で反転を取りにいく。SL895.4円（直近5日安値）
- 8304 Aozora Bank, Ltd.｜choruko_reversal｜取得不可(None)｜⚪妥当｜FAIL_INSEN｜3,023円｜💰31.0万円｜—
- 3591 WACOAL HOLDINGS CORP｜choruko_reversal｜🔻悪化(None)｜🟡やや割高｜PASS｜3,576円｜💰35.8万円｜reversal 3576 想定損失幅1.5%。｜📋カルテ窓 11/12(残14営業日)｜⚠業績基調が下向き（🔻悪化）
  > 【業態】婦人下着最大手。「ワコール」、「ウイング」ブランドなど。傘下に販売のピーチ・ジョン。
  > 【いま】終値3,576円・直近5日+1.25%（材料未確認）
  > 【調子】🔻悪化
  > 【水準】🟡やや割高（2.0/7）— PER98.24倍・PEG—・52週3.8% ／ 💰単元35.8万円
  > 【戦略】当日終値3,576円の指値で反転を取りにいく。SL3,522円（直近5日安値）
- 5344 MARUWA CO., LTD.｜choruko_reversal｜業績データ取得不可(None)｜🟡やや割高｜FAIL_INSEN｜47,700円｜💰583.5万円｜—
- 8511 Japan Securities Finance Co., Ltd.｜choruko_reversal｜取得不可(None)｜🔴過熱｜FAIL_INSEN｜2,156円｜💰22.2万円｜—
- 1963 JGC Holdings Corporation｜choruko_reversal｜None(None)｜None｜FAIL_INSEN｜2,038.5円｜💰0.0万円｜—
- 3105 Nisshinbo Holdings Inc.｜choruko_reversal｜None(None)｜None｜FAIL_INSEN｜2,262.5円｜💰0.0万円｜—
- 3445 RS Technologies Co. Ltd.｜choruko_reversal｜None(None)｜None｜FAIL_INSEN｜4,945円｜💰0.0万円｜—
- 4088 Air Water Inc.｜choruko_reversal｜None(None)｜None｜FAIL_INSEN｜2,642円｜💰0.0万円｜—
- 4966 C. Uyemura & Co., Ltd.｜choruko_reversal｜None(None)｜None｜FAIL_INSEN｜17,800円｜💰0.0万円｜—
- 6332 TSUKISHIMA HOLDINGS CO. LTD.｜choruko_reversal｜None(None)｜None｜FAIL_INSEN｜2,367円｜💰0.0万円｜—
- 6645 OMRON Corporation｜granville_rebound/choruko_reversal｜None(None)｜None｜FAIL_INSEN｜5,499円｜💰0.0万円｜—
- 6875 Megachips Corporation｜choruko_reversal｜None(None)｜None｜FAIL_INSEN｜9,770円｜💰0.0万円｜—
- 7322 San ju San Financial Group, Inc.｜choruko_reversal｜None(None)｜None｜FAIL_INSEN｜1,839円｜💰0.0万円｜—
- 8334 Gunma Bank, Ltd.｜granville_rebound/choruko_reversal｜None(None)｜None｜FAIL_INSEN｜2,561.5円｜💰0.0万円｜—
- 8359 Hachijuni Nagano Bank, Ltd.｜choruko_reversal｜None(None)｜None｜FAIL_INSEN｜2,393円｜💰0.0万円｜—
- 7624 NaITO｜stf_kakuhen｜🔥絶好調(10)｜🟢値頃｜FAIL_UWAHIGE｜171円｜💰1.8万円｜—
- 5018 ＭＯＲＥＳＣＯ｜stf_kakuhen｜🔥絶好調(10)｜⚪妥当｜FAIL_INSEN｜2,911円｜💰29.8万円｜—
- 6668 ＡＤプラズマ｜stf_kakuhen/granville_oshime｜🔥絶好調(10)｜⚪妥当｜FAIL_INSEN｜4,775円｜💰49.4万円｜—
- 7713 シグマ光機｜stf_kakuhen｜🔥絶好調(10)｜⚪妥当｜FAIL_INSEN｜3,215円｜💰33.2万円｜—
- 5246 ELEMENTS,Inc.｜granville_oshime/stf_kakuhen｜🔥絶好調(10)｜⚪妥当｜FAIL_INSEN｜1,036円｜💰12.8万円｜—
- 3498 霞ヶ関Ｃ｜stf_kakuhen｜🔥絶好調(9)｜💎割安｜FAIL_INSEN｜6,700円｜💰69.0万円｜—
- 3994 マネーフォワード｜stf_kakuhen｜🔥絶好調(9)｜🔴過熱｜FAIL_INSEN｜6,747円｜💰65.8万円｜—
- 7811 Nakamoto Packs Co. Ltd.｜granville_oshime/stf_kakuhen｜🔥絶好調(8)｜⚪妥当｜PASS｜2,614円｜💰26.1万円｜—｜⚠日程不明｜⛔提案なし(手法ブランチ不明)
  > 【業態】グラビア印刷やドライラミネート加工などコーティング事業。食品包装、医療関連など。
  > 【いま】終値2,614円・直近5日+11.95%（材料未確認）
  > 【調子】🔥絶好調（8/13）
  > 【水準】⚪妥当（4.0/7）— PER9.02倍・PEG0.2913・52週100.0% ／ 💰単元26.1万円
  > 【戦略】発注対象外（⛔提案なし(手法ブランチ不明)）
- 4443 Ｓａｎｓａｎ｜stf_kakuhen/changepoint🔔🔔｜🔥絶好調(8)｜⚪妥当｜FAIL_INSEN｜2,085円｜💰20.7万円｜—
- 6814 古野電｜stf_kakuhen｜⚡好調(7)｜⚪妥当｜FAIL_INSEN｜7,640円｜💰87.3万円｜—
- 5932 三協立山｜stf_kakuhen｜⚡好調(7)｜⚪妥当｜FAIL_UWAHIGE｜777円｜💰7.8万円｜—
- 3479 ティーケーピー｜granville_tenkan/stf_kakuhen｜⚡好調(6)｜🔴過熱｜FAIL_UWAHIGE｜1,940円｜💰19.6万円｜—
- 6532 ベイカレント｜stf_kakuhen｜⚡好調(5)｜🟡やや割高｜FAIL_UWAHIGE｜11,440円｜💰108.5万円｜—
- 4176 ココナラ｜stf_kakuhen｜✅順調(4)｜🟢値頃｜PASS_DOJI｜310円｜💰3.1万円｜—｜⚠日程不明｜⛔提案なし(手法ブランチ不明)
  > 【業態】個人の知識・スキル・経験を売買できるスキルマーケット「ココナラ」を運営。法律相談も。
  > 【いま】終値310円・直近5日-7.74%（材料未確認）
  > 【調子】✅順調（4/13）
  > 【水準】🟢値頃（5.0/7）— PER14.49倍・PEG0.7420・52週46.8% ／ 💰単元3.1万円
  > 【戦略】発注対象外（⛔提案なし(手法ブランチ不明)）
- 9960 トーテック｜granville_tenkan/granville_oshime｜⚠減速(1)｜🔴過熱｜FAIL_UWAHIGE｜4,380円｜💰43.2万円｜—
- 6779 Nihon Dempa Kogyo Co., Ltd.｜granville_rebound/ai_reversal｜⚡好調(7)｜⚪妥当｜FAIL_INSEN｜2,626円｜💰28.9万円｜—
- 4658 日本空調サービス｜granville_tenkan/ai_reversal｜⚡好調(5)｜⚪妥当｜FAIL_UWAHIGE｜1,561円｜💰15.7万円｜—
- 5208 Arisawa Mfg.Co., Ltd.｜granville_oshime/ai_reversal｜✅順調(4)｜🔴過熱｜FAIL_INSEN｜2,607円｜💰28.3万円｜—
- 9211 f-code Inc.｜granville_tenkan/changepoint🔔｜🔥絶好調(9)｜💎割安｜FAIL_INSEN｜1,213円｜💰14.5万円｜—
- 2334 Eole, Inc.｜granville_oshime/granville_rebound｜🔥絶好調(8)｜⚪妥当｜FAIL_INSEN｜512円｜💰5.6万円｜—
- 4431 スマレジ｜changepoint/変化点🔔🔔｜🔥絶好調(8)｜🟡やや割高｜FAIL_INSEN｜3,765円｜💰40.7万円｜—
- 5590 NETSTARS Co.,Ltd.｜changepoint🔔｜⚡好調(7)｜🟢値頃｜FAIL_INSEN｜661円｜💰6.8万円｜—
- 4493 Cyber Security Cloud, Inc.｜changepoint🔔｜✅順調(3)｜🔴過熱｜PASS｜3,865円｜💰38.6万円｜changepoint 3865 想定損失幅22.5%。 ⚠1単元リスク87,000円（枠超過）｜📋カルテ窓 11/13(残15営業日)｜⚠1単元でリスク枠超過（87,000円）
  > 【業態】人工知能(AI)技術を活用したサイバーセキュリティサービスの開発・提供を手掛ける。
  > 【いま】終値3,865円・直近5日+22.89%（材料未確認）
  > 【調子】✅順調（3/13）
  > 【水準】🔴過熱（0.0/7）— PER44.89倍・PEG4.5388・52週81.9% ／ 💰単元38.6万円
  > 【戦略】発火日終値3,865円の指値。追撃禁止・SL2,995円。🔒実弾封印中（PL3紙ログ収集中）／⚠1単元リスク87,000円（枠超過）

## グランビル銘柄
- 3374 Naigai Tec Corporation｜kenmo_newhigh/ai_momentum｜🚀確変(12)｜⚪妥当｜FAIL_INSEN｜4,625円｜💰50.5万円｜—
- 6752 パナソニックHD｜ai_reversal/granville_rebound｜⚠減速(7)｜⚪妥当｜FAIL_INSEN｜3,700円｜💰39.8万円｜—
- 3103 ユニチカ｜ai_reversal/granville_rebound｜🔻悪化(2)｜🟡やや割高｜FAIL_INSEN｜1,269円｜💰13.3万円｜—
- 5254 Arent, Inc.｜granville_tenkan｜🚀確変(12)｜⚪妥当｜FAIL_INSEN｜3,985円｜💰40.8万円｜—
- 8944 Land Business Co., Ltd.｜granville_tenkan｜🔥絶好調(10)｜💎割安｜FAIL_INSEN｜252円｜💰2.6万円｜—
- 7725 INTER ACTION Corporation｜granville_tenkan｜🔥絶好調(10)｜🟢値頃｜FAIL_INSEN｜1,734円｜💰17.2万円｜—
- 9553 MicroAd, Inc.｜granville_tenkan｜🔥絶好調(10)｜🟢値頃｜FAIL_INSEN｜579円｜💰6.1万円｜—
- 6905 Cosel Co., Ltd.｜granville_tenkan｜🔥絶好調(10)｜⚪妥当｜FAIL_INSEN｜1,303円｜💰13.4万円｜—
- 2986 LA Holdings Co.,Ltd｜granville_tenkan｜🔥絶好調(9)｜💎割安｜FAIL_INSEN｜2,699円｜💰27.1万円｜—
- 6562 Geniee, Inc.｜granville_tenkan｜🔥絶好調(8)｜💎割安｜FAIL_INSEN｜916円｜💰10.0万円｜—
- 1945 Tokyo Energy & Systems Inc.｜granville_tenkan｜🔥絶好調(8)｜💎割安｜FAIL_INSEN｜1,968円｜💰20.0万円｜—
- 9006 京浜急行電鉄｜granville_tenkan｜🔥絶好調(8)｜🟢値頃｜PASS｜1,562円｜💰15.6万円｜—｜📋カルテ窓 11/11(残13営業日)｜⛔提案なし(指名鮮度切れ 17営業日)
  > 【業態】京浜・三浦半島が地盤。品川・羽田・横浜を核に沿線再開発を推進。
  > 【いま】終値1,562円・直近5日+1.66%（材料未確認）
  > 【調子】🔥絶好調（8/13）
  > 【水準】🟢値頃（5.0/7）— PER13.71倍・PEG0.2613・52週60.4% ／ 💰単元15.6万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 17営業日)）
- 6473 JTEKT Corporation｜granville_tenkan｜⚠減速(8)｜⚪妥当｜FAIL_INSEN｜2,038円｜💰21.4万円｜—
- 8697 Japan Exchange Group, Inc.｜granville_tenkan/changepoint🔔｜🔥絶好調(8)｜🟡やや割高｜FAIL_INSEN｜2,225円｜💰22.4万円｜—
- 6255 NPC Incorporated｜granville_tenkan｜⚡好調(7)｜🟢値頃｜FAIL_INSEN｜658円｜💰6.8万円｜—
- 8095 Astena Holdings Co.,Ltd.｜granville_tenkan｜⚡好調(7)｜🟢値頃｜FAIL_UWAHIGE｜523円｜💰5.2万円｜—
- 8793 ＮＥＣキャピタルソリューション｜granville_tenkan｜⚡好調(7)｜🟢値頃｜FAIL_UWAHIGE｜4,055円｜💰40.2万円｜—
- 3496 AZOOM CO.,LTD｜granville_tenkan｜⚡好調(7)｜⚪妥当｜FAIL_UWAHIGE｜4,835円｜💰49.2万円｜—
- 4544 H.U.Group Holdings, Inc.｜granville_tenkan｜⚡好調(7)｜⚪妥当｜FAIL_INSEN｜3,736円｜💰37.1万円｜—
- 7744 Noritsu Koki Co., Ltd.｜granville_tenkan｜⚡好調(7)｜⚪妥当｜FAIL_UWAHIGE｜2,110円｜💰20.8万円｜—
- 9064 ヤマトホールディングス｜granville_tenkan｜⚡好調(7)｜⚪妥当｜FAIL_UWAHIGE｜2,069.5円｜💰20.6万円｜—
- 3741 Systems Engineering Consultants Co., Ltd.｜granville_tenkan｜⚡好調(7)｜⚪妥当｜FAIL_INSEN｜2,986円｜💰30.7万円｜—
- 6302 Sumitomo Heavy Industries, Ltd.｜granville_tenkan｜⚡好調(7)｜⚪妥当｜FAIL_INSEN｜5,409円｜💰57.2万円｜—
- 4507 Shionogi & Co., Ltd.｜granville_tenkan｜⚡好調(7)｜🟡やや割高｜FAIL_UWAHIGE｜3,028円｜💰29.8万円｜—
- 5838 Rakuten Bank, Ltd.｜granville_tenkan｜⚡好調(6)｜💎割安｜FAIL_INSEN｜5,975円｜💰60.3万円｜—
- 4763 クリーク・アンド・リバー社｜granville_tenkan｜⚡好調(6)｜🟢値頃｜PASS｜1,497円｜💰15.0万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）｜⛔提案なし(指名鮮度切れ 12営業日)
  > 【業態】映像・ゲーム分野の派遣と制作主力。メタバース・NFT分野注力。医療職等派遣も。
  > 【いま】終値1,497円・直近5日+5.57%（材料未確認）
  > 【調子】⚡好調（6/13）
  > 【水準】🟢値頃（5.0/7）— PER8.93倍・PEG0.5950・52週70.0% ／ 💰単元15.0万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 12営業日)）
- 6470 Taiho Kogyo Co., Ltd.｜granville_tenkan｜⚡好調(6)｜⚪妥当｜FAIL_INSEN｜1,134円｜💰11.6万円｜—
- 7199 Premium Group Co., Ltd.｜granville_tenkan｜⚡好調(6)｜⚪妥当｜FAIL_INSEN｜2,199円｜💰22.2万円｜—
- 3064 MonotaRO Co., Ltd.｜granville_tenkan｜⚡好調(6)｜🔴過熱｜FAIL_INSEN｜2,292円｜💰23.9万円｜—
- 3935 Edia Co. Ltd.｜granville_tenkan｜⚡好調(5)｜💎割安｜FAIL_INSEN｜716円｜💰7.3万円｜—
- 6196 Strike Group Co. Ltd.｜granville_tenkan｜⚡好調(5)｜💎割安｜FAIL_INSEN｜1,436円｜💰14.1万円｜—
- 3562 No.1 Co., Ltd.｜granville_tenkan｜⚡好調(5)｜🟢値頃｜FAIL_INSEN｜1,730円｜💰17.0万円｜—
- 8061 Seika Corporation｜granville_tenkan｜⚡好調(5)｜🟢値頃｜FAIL_INSEN｜2,854円｜💰30.3万円｜—
- 9048 名古屋鉄道｜granville_tenkan｜⚡好調(5)｜🟢値頃｜FAIL_UWAHIGE｜1,859円｜💰18.5万円｜—
- 2331 ALSOK CO., LTD.｜granville_tenkan｜⚡好調(5)｜⚪妥当｜FAIL_UWAHIGE｜1,225円｜💰12.2万円｜—
- 3661 m-up holdings, Inc.｜granville_tenkan｜⚡好調(5)｜⚪妥当｜FAIL_UWAHIGE｜879円｜💰8.9万円｜—
- 6432 Takeuchi Mfg.Co., Ltd.｜granville_tenkan｜⚡好調(5)｜⚪妥当｜PASS｜7,850円｜💰78.5万円｜momentum 7880 想定損失幅6.1%。 ⚠1単元リスク48,219円（枠超過）｜⚠日程不明｜⚠1単元でリスク枠超過（48,219円）
  > 【業態】建機中堅。ミニショベルなど小型が主力。クローラーローダーを開発。欧米で高シェア。
  > 【いま】終値7,850円・直近5日+4.53%（材料未確認）
  > 【調子】⚡好調（5/13）
  > 【水準】⚪妥当（3.0/7）— PER11.52倍・PEG0.9003・52週91.6% ／ 💰単元78.5万円
  > 【戦略】当日高値超えの逆指値7,880円で順張り参戦を検討。上限7,958.8円・SL7,397.8円目安／⚠1単元リスク48,219円（枠超過）
- 7970 Shin-Etsu Polymer Co., Ltd.｜granville_tenkan｜⚡好調(5)｜🟡やや割高｜FAIL_INSEN｜2,236円｜💰23.8万円｜—
- 8020 Kanematsu Corporation｜granville_tenkan｜⚡好調(5)｜🟡やや割高｜FAIL_UWAHIGE｜2,326.5円｜💰24.0万円｜—
- 9828 Genki Global Dining Concepts Corp｜granville_tenkan｜⚡好調(5)｜🔴過熱｜FAIL_UWAHIGE｜3,440円｜💰35.3万円｜—
- 6454 Max Co., Ltd.｜granville_tenkan｜⚡好調(5)｜🔴過熱｜FAIL_INSEN｜1,910円｜💰19.3万円｜—
- 2288 Marudai Food Co., Ltd.｜granville_tenkan｜✅順調(4)｜🟢値頃｜PASS｜2,198円｜💰22.0万円｜—｜📋カルテ窓 11/09(残11営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）｜⛔提案なし(指名鮮度切れ 17営業日)
  > 【業態】食料品（ハム・ソーセージ・食肉・総菜関連）
  > 【いま】終値2,198円・直近5日+0.92%（材料未確認）
  > 【調子】✅順調（4/13）
  > 【水準】🟢値頃（5.0/7）— PER8.21倍・PEG1.3916・52週54.8% ／ 💰単元22.0万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 17営業日)）
- 5036 Japan Business Systems, Inc.｜granville_tenkan｜✅順調(4)｜⚪妥当｜FAIL_UWAHIGE｜1,928円｜💰18.8万円｜—
- 8014 Chori Co., Ltd.｜granville_tenkan｜✅順調(4)｜⚪妥当｜FAIL_INSEN｜4,245円｜💰43.0万円｜—
- 6988 日東電工｜granville_tenkan｜✅順調(4)｜🟡やや割高｜PASS｜3,709円｜💰37.1万円｜—｜⏰決算 10/27(残3営業日)｜⛔提案なし(指名鮮度切れ 15営業日)
  > 【業態】テープ、フィルムの総合材料メーカー。液晶・半導体、医療用など。ニッチ商品で高シェア。
  > 【いま】終値3,709円・直近5日+2.88%（材料未確認）
  > 【調子】✅順調（4/13）
  > 【水準】🟡やや割高（2.0/7）— PER17.19倍・PEG2.1161・52週69.7% ／ 💰単元37.1万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 15営業日)）
- 6371 Tsubakimoto Chain Co.｜granville_tenkan｜✅順調(4)｜🔴過熱｜FAIL_UWAHIGE｜2,641円｜💰26.8万円｜—
- 6592 Mabuchi Motor Co., Ltd.｜granville_tenkan｜✅順調(4)｜🔴過熱｜FAIL_INSEN｜1,710.5円｜💰17.7万円｜—
- 8060 キヤノンマーケティングジャパン｜granville_tenkan｜✅順調(4)｜🔴過熱｜PASS｜4,203円｜💰42.0万円｜—｜⏰決算 10/26(残2営業日)｜⛔提案なし(指名鮮度切れ 19営業日)
  > 【業態】OA機器販社。キヤノン国内販売が主力。SI・ITソリューションに注力。BPO、データセンターも。
  > 【いま】終値4,203円・直近5日+5.66%（材料未確認）
  > 【調子】✅順調（4/13）
  > 【水準】🔴過熱（0.0/7）— PER19.69倍・PEG2.8311・52週99.3% ／ 💰単元42.0万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 19営業日)）
- 4166 Cacco, Inc.｜granville_tenkan｜✅順調(3)｜💎割安｜FAIL_UWAHIGE｜764円｜💰7.3万円｜—
- 8850 スターツコーポレーション｜granville_tenkan｜✅順調(3)｜⚪妥当｜PASS｜4,560円｜💰45.6万円｜—｜📋カルテ窓 11/09(残11営業日)｜⛔提案なし(指名鮮度切れ 15営業日)
  > 【業態】不動産複合管理。「ピタットハウス」全国展開。ホテル、管理、建設、保育など多角。
  > 【いま】終値4,560円・直近5日-0.55%（材料未確認）
  > 【調子】✅順調（3/13） — 質注意
  > 【水準】⚪妥当（4.0/7）— PER8.31倍・PEG4.2056・52週17.7% ／ 💰単元45.6万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 15営業日)）
- 3433 TOCALO Co., Ltd.｜granville_tenkan｜✅順調(3)｜⚪妥当｜FAIL_INSEN｜2,731円｜💰29.1万円｜—
- 8927 Meiho Enterprise Co., Ltd.｜granville_tenkan｜✅順調(3)｜⚪妥当｜FAIL_INSEN｜480円｜💰4.9万円｜—
- 186A Astroscale Holdings Inc.｜granville_tenkan｜✅順調(3)｜🟡やや割高｜FAIL_INSEN｜1,025円｜💰10.7万円｜—
- 4183 Mitsui Chemicals, Inc.｜granville_tenkan｜✅順調(3)｜🟡やや割高｜FAIL_INSEN｜2,056円｜💰21.0万円｜—
- 4272 Nippon Kayaku Co., Ltd.｜granville_tenkan｜✅順調(3)｜🟡やや割高｜FAIL_INSEN｜2,041.5円｜💰21.6万円｜—
- 4956 Konishi Co., Ltd.｜granville_tenkan｜✅順調(3)｜🟡やや割高｜FAIL_INSEN｜1,509円｜💰15.2万円｜—
- 5461 Chubu Steel Plate Co., Ltd.｜granville_tenkan｜🔻悪化(3)｜🟡やや割高｜FAIL_UWAHIGE｜2,176円｜💰21.4万円｜—
- 7181 JAPAN POST INSURANCE Co., Ltd.｜granville_tenkan｜⚠減速(3)｜🔴過熱｜FAIL_INSEN｜1,695円｜💰17.3万円｜—
- 7734 Riken Keiki Co., Ltd.｜granville_tenkan｜✅順調(3)｜🔴過熱｜FAIL_INSEN｜3,385円｜💰35.5万円｜—
- 7513 Kojima Co., Ltd.｜granville_tenkan｜✅順調(3)｜🔴過熱｜FAIL_INSEN｜1,404円｜💰14.6万円｜—
- 6328 Ebara Jitsugyo Co., Ltd.｜granville_tenkan｜➖横ばい(2)｜⚪妥当｜FAIL_UWAHIGE｜2,478円｜💰24.6万円｜—
- 2002 日清製粉グループ本社｜granville_tenkan｜➖横ばい(2)｜🟡やや割高｜FAIL_UWAHIGE｜2,054.5円｜💰20.6万円｜—
- 6208 Ishikawa Seisakusho,Ltd.｜granville_tenkan｜🔻悪化(2)｜🟡やや割高｜FAIL_INSEN｜1,608円｜💰16.6万円｜—
- 2413 エムスリー｜granville_tenkan｜➖横ばい(2)｜🔴過熱｜FAIL_INSEN｜1,934.5円｜💰19.2万円｜—
- 4617 Chugoku Marine Paints,Ltd.｜granville_tenkan｜➖横ばい(2)｜🔴過熱｜FAIL_INSEN｜3,480円｜💰37.1万円｜—
- 7751 キヤノン｜granville_tenkan｜➖横ばい(2)｜🔴過熱｜FAIL_UWAHIGE｜4,898円｜💰48.2万円｜—
- 8081 Kanaden Corporation｜granville_tenkan｜➖横ばい(2)｜🔴過熱｜FAIL_INSEN｜2,639円｜💰28.0万円｜—
- 5071 VIS Co., Ltd.｜granville_tenkan｜⚠減速(1)｜⚪妥当｜FAIL_INSEN｜1,369円｜💰13.8万円｜—
- 6770 Alps Alpine Co., Ltd.｜granville_tenkan｜⚠減速(1)｜🟡やや割高｜FAIL_INSEN｜2,093円｜💰21.4万円｜—
- 1815 鉄建建設｜granville_tenkan｜⚠減速(0)｜⚪妥当｜FAIL_INSEN｜2,152円｜💰21.8万円｜—
- 4375 Safie Inc.｜granville_tenkan/changepoint🔔｜取得不可(None)｜💎割安｜FAIL_UWAHIGE｜676円｜💰6.8万円｜—
- 8424 芙蓉総合リース｜granville_tenkan｜取得不可(None)｜💎割安｜FAIL_UWAHIGE｜4,313円｜💰43.1万円｜—
- 2871 ニチレイ｜granville_tenkan｜業績データ取得不可(None)｜🔴過熱｜FAIL_UWAHIGE｜2,134.5円｜💰21.4万円｜—
- 4169 Enechange Ltd.｜granville_tenkan｜None(None)｜None｜FAIL_INSEN｜268円｜💰0.0万円｜—
- 4534 Mochida Pharmaceutical Co., Ltd.｜granville_tenkan｜None(None)｜None｜FAIL_INSEN｜3,265円｜💰0.0万円｜—
- 4549 Eiken Chemical Co., Ltd.｜granville_tenkan｜None(None)｜None｜FAIL_INSEN｜2,434円｜💰0.0万円｜—
- 4552 JCR Pharmaceuticals Co., Ltd.｜granville_tenkan｜None(None)｜None｜FAIL_INSEN｜534円｜💰0.0万円｜—
- 4902 Konica Minolta, Inc.｜granville_tenkan｜None(None)｜None｜FAIL_INSEN｜662.8円｜💰0.0万円｜—
- 6768 Tamura Corporation｜granville_tenkan｜None(None)｜None｜FAIL_INSEN｜836円｜💰0.0万円｜—
- 8012 Nagase & Co., Ltd.｜granville_tenkan｜None(None)｜None｜FAIL_INSEN｜1,194.5円｜💰0.0万円｜—
- 9163 Nareru Group Inc.｜granville_tenkan｜None(None)｜None｜FAIL_INSEN｜2,368円｜💰0.0万円｜—
- 9837 Morito Co., Ltd.｜granville_tenkan｜None(None)｜None｜FAIL_INSEN｜1,826円｜💰0.0万円｜—
- 4937 Ｇ−ＷＡＱＯＯ｜granville_oshime｜🚀確変(13)｜⚪妥当｜FAIL_INSEN｜2,347円｜💰23.2万円｜—
- 3083 Star seeds Co.,Ltd.｜granville_oshime/granville_rebound｜🚀確変(12)｜⚪妥当｜FAIL_INSEN｜1,023円｜💰10.6万円｜—
- 290A ＳＹＮＳＰＥＣＴＩＶＥ｜granville_oshime｜🚀確変(11)｜🟢値頃｜FAIL_INSEN｜1,190円｜💰12.2万円｜—
- 5243 note inc.｜granville_oshime｜🚀確変(11)｜⚪妥当｜FAIL_INSEN｜2,738円｜💰30.1万円｜—
- 7806 MTG Co., Ltd.｜granville_oshime/changepoint🔔｜🚀確変(11)｜⚪妥当｜FAIL_INSEN｜7,920円｜💰84.3万円｜—
- 6834 Seikoh Giken Co., Ltd.｜granville_oshime｜🔥絶好調(10)｜💎割安｜FAIL_INSEN｜5,310円｜💰58.9万円｜—
- 6613 QD Laser, Inc.｜granville_oshime｜🔥絶好調(10)｜🟡やや割高｜FAIL_INSEN｜1,999円｜💰20.6万円｜—
- 8336 Musashino Bank, Ltd.｜granville_oshime｜🔥絶好調(9)｜⚪妥当｜FAIL_INSEN｜2,554円｜💰26.3万円｜—
- 8008 Yondoshi Holdings, Inc.｜granville_oshime｜🔥絶好調(9)｜⚪妥当｜FAIL_INSEN｜2,004円｜💰20.1万円｜—
- 8346 Toho Bank, Ltd.｜granville_oshime/granville_rebound｜🔥絶好調(8)｜⚪妥当｜FAIL_INSEN｜947円｜💰10.3万円｜—
- 7856 HAGIHARA INDUSTRIES INC.｜granville_oshime｜🔥絶好調(8)｜🟡やや割高｜FAIL_INSEN｜2,028円｜💰20.7万円｜—
- 1879 新日本建設｜granville_oshime｜⚡好調(7)｜💎割安｜PASS｜2,192円｜💰21.9万円｜—｜📋カルテ窓 11/12(残14営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）｜⛔提案なし(指名鮮度切れ 15営業日)
  > 【業態】建設・マンション開発が主体。一括受注体制。首都圏中心から地方に進出。
  > 【いま】終値2,192円・直近5日+1.72%（材料未確認）
  > 【調子】⚡好調（7/13）
  > 【水準】💎割安（6.0/7）— PER7.33倍・PEG0.2910・52週69.7% ／ 💰単元21.9万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 15営業日)）
- 6736 Suncorporation｜granville_oshime｜⚡好調(7)｜⚪妥当｜FAIL_INSEN｜9,670円｜💰97.4万円｜—
- 9902 Nichiden Corporation｜granville_oshime｜⚡好調(7)｜🟡やや割高｜FAIL_INSEN｜3,180円｜💰32.6万円｜—
- 6523 PHC Holdings Corp.｜granville_oshime｜⚠減速(6)｜🟢値頃｜FAIL_INSEN｜1,319円｜💰13.7万円｜—
- 7609 Daitron Co., Ltd.｜granville_oshime｜⚡好調(6)｜🟢値頃｜FAIL_INSEN｜4,120円｜💰41.6万円｜—
- 2767 円谷フィールズホールディングス｜granville_oshime｜⚡好調(6)｜⚪妥当｜FAIL_UWAHIGE｜2,519円｜💰25.2万円｜—
- 4667 Aisan Technology Co., Ltd.｜granville_oshime/changepoint🔔｜⚡好調(6)｜⚪妥当｜FAIL_INSEN｜922円｜💰9.7万円｜—
- 6023 ダイハツインフィニアース｜granville_oshime｜⚡好調(6)｜⚪妥当｜FAIL_INSEN｜2,764円｜💰31.9万円｜—
- 6250 Yamabiko Corporation｜granville_oshime｜⚡好調(6)｜⚪妥当｜FAIL_INSEN｜4,330円｜💰44.1万円｜—
- 6227 AIMECHATEC Ltd.｜granville_oshime｜⚡好調(6)｜⚪妥当｜FAIL_INSEN｜5,730円｜💰68.5万円｜—
- 2602 日清オイリオグループ｜granville_oshime｜⚡好調(6)｜🟡やや割高｜FAIL_INSEN｜2,063円｜💰20.5万円｜—
- 4413 baudroie,inc.｜granville_oshime｜⚡好調(6)｜🟡やや割高｜FAIL_UWAHIGE｜2,949円｜💰29.9万円｜—
- 8919 カチタス｜granville_oshime｜⚡好調(6)｜🟡やや割高｜FAIL_INSEN｜3,340円｜💰33.5万円｜—
- 6570 Kyowa Corporation Co. Ltd.｜granville_oshime｜⚡好調(6)｜🔴過熱｜FAIL_INSEN｜4,105円｜💰45.8万円｜—
- 7616 Colowide Co., Ltd.｜granville_oshime｜⚡好調(6)｜🔴過熱｜FAIL_INSEN｜2,155円｜💰22.0万円｜—
- 8714 Senshu Ikeda Holdings,Inc.｜granville_oshime｜⚡好調(5)｜⚪妥当｜FAIL_INSEN｜962円｜💰10.4万円｜—
- 7350 Okinawa Financial Group, Inc.｜granville_oshime｜⚡好調(5)｜⚪妥当｜FAIL_INSEN｜6,930円｜💰73.9万円｜—
- 6058 VECTOR Inc.｜granville_oshime｜⚡好調(5)｜🔴過熱｜FAIL_UWAHIGE｜2,165円｜💰20.4万円｜—
- 4475 HENNGE K.K.｜granville_oshime｜⚡好調(5)｜🔴過熱｜FAIL_UWAHIGE｜2,266円｜💰20.8万円｜—
- 4373 Simplex Holdings,Inc.｜granville_oshime｜✅順調(4)｜🟡やや割高｜FAIL_UWAHIGE｜1,282円｜💰12.6万円｜—
- 3097 Monogatari Corporation｜granville_oshime｜✅順調(4)｜🔴過熱｜FAIL_UWAHIGE｜5,930円｜💰60.9万円｜—
- 6998 Nippon Tungsten Co., Ltd.｜granville_oshime｜✅順調(4)｜🔴過熱｜FAIL_INSEN｜3,170円｜💰35.4万円｜—
- 5985 SUNCALL CORPORATION｜granville_oshime｜✅順調(3)｜⚪妥当｜FAIL_INSEN｜2,024円｜💰21.4万円｜—
- 1518 三井松島ホールディングス｜granville_oshime｜✅順調(3)｜🟡やや割高｜FAIL_INSEN｜2,200円｜💰22.9万円｜—
- 6379 RAIZNEXT Corporation｜granville_oshime｜✅順調(3)｜🔴過熱｜FAIL_INSEN｜1,006円｜💰10.3万円｜—
- 9044 NANKAI Co., Ltd.｜granville_oshime｜✅順調(3)｜🟡やや割高｜PASS｜3,015円｜💰30.1万円｜—｜⛔型不一致: 既に支持帯以下
  > 【業態】大阪南部と和歌山が地盤。関空関連となんば再開発が核。泉北ライナー注力。
  > 【いま】終値3,015円・直近5日+0.55%（材料未確認）
  > 【調子】✅順調（3/13） — 質注意
  > 【水準】🟡やや割高（2.0/7）— PER13.70倍・PEG—・52週58.7% ／ 💰単元30.1万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 3107 ダイワボウホールディングス｜granville_oshime｜⚠減速(3)｜🔴過熱｜PASS｜3,731円｜💰37.3万円｜—｜📋カルテ窓 11/11(残13営業日)｜⚠業績基調が下向き（⚠減速）｜⛔提案なし(指名鮮度切れ 12営業日)
  > 【業態】ダイワボウ情報システムが主力。祖業の紡績事業は譲渡。産業機械のIoTを拡大。
  > 【いま】終値3,731円・直近5日+6.15%（材料未確認）
  > 【調子】⚠減速（3/13） — 質注意
  > 【水準】🔴過熱（1.0/7）— PER12.59倍・PEG—・52週89.3% ／ 💰単元37.3万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 12営業日)）
- 4044 Central Glass Co., Ltd.｜granville_oshime｜✅順調(3)｜🔴過熱｜FAIL_INSEN｜4,465円｜💰46.2万円｜—
- 4208 UBE Corporation｜granville_oshime｜✅順調(3)｜🔴過熱｜FAIL_INSEN｜3,227円｜💰33.4万円｜—
- 456A Human Made Inc.｜granville_oshime｜✅順調(3)｜🔴過熱｜FAIL_UWAHIGE｜1,880円｜💰18.9万円｜—
- 7504 Kohsoku Corporation｜granville_oshime｜✅順調(3)｜🔴過熱｜FAIL_UWAHIGE｜4,875円｜💰47.9万円｜—
- 9509 Hokkaido Electric Power Company,Incorporated｜granville_oshime｜🔻悪化(2)｜⚪妥当｜FAIL_INSEN｜1,090.5円｜💰10.9万円｜—
- 6072 Jibannet Holdings Co., Ltd.｜granville_oshime｜🔻悪化(2)｜🟡やや割高｜FAIL_INSEN｜1,000円｜💰10.4万円｜—
- 9505 Hokuriku Electric Power Company｜granville_oshime｜🔻悪化(2)｜🟡やや割高｜FAIL_UWAHIGE｜1,072.5円｜💰10.5万円｜—
- 7630 Ichibanya Co., Ltd.｜granville_oshime｜➖横ばい(2)｜🔴過熱｜FAIL_INSEN｜1,057円｜💰10.8万円｜—
- 8043 Starzen Company Limited｜granville_oshime｜➖横ばい(2)｜🔴過熱｜FAIL_UWAHIGE｜1,551円｜💰15.5万円｜—
- 9616 共立メンテナンス｜granville_oshime｜➖横ばい(2)｜🔴過熱｜PASS｜3,415円｜💰34.1万円｜—｜📋カルテ窓 11/09(残11営業日)｜⛔提案なし(指名鮮度切れ 15営業日)
  > 【業態】サービス業
  > 【いま】終値3,415円・直近5日+2.46%（材料未確認）
  > 【調子】➖横ばい（2/13）
  > 【水準】🔴過熱（0.0/7）— PER17.26倍・PEG—・52週89.5% ／ 💰単元34.1万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 15営業日)）
- 9900 Sagami Holdings Corp.｜granville_oshime｜➖横ばい(2)｜🔴過熱｜PASS｜1,135円｜💰11.3万円｜—｜📋カルテ窓 11/12(残14営業日)｜⛔提案なし(指名鮮度切れ 14営業日)
  > 【業態】中部地盤の麺類中心とした外食チェーン。郊外中心に出店。海外に和食店も。
  > 【いま】終値1,135円・直近5日+1.43%（材料未確認）
  > 【調子】➖横ばい（2/13） — 質注意
  > 【水準】🔴過熱（0.0/7）— PER57.32倍・PEG—・52週88.1% ／ 💰単元11.3万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 14営業日)）
- 3048 ビックカメラ｜granville_oshime｜⚠減速(1)｜🟡やや割高｜FAIL_INSEN｜1,708.5円｜💰17.8万円｜—
- 8255 Axial Retailing, Inc.｜granville_oshime｜⚠減速(1)｜🔴過熱｜FAIL_UWAHIGE｜1,309円｜💰12.7万円｜—
- 8097 SAN-AI OBBLI CO. LTD｜granville_oshime｜⚠減速(1)｜🔴過熱｜FAIL_UWAHIGE｜2,525円｜💰24.8万円｜—
- 8059 Daiichi Jitsugyo Co., Ltd.｜granville_oshime｜⚠減速(0)｜🔴過熱｜FAIL_INSEN｜3,570円｜💰36.0万円｜—
- 8361 Ogaki Kyoritsu Bank, Ltd.｜granville_oshime/granville_rebound｜取得不可(None)｜💎割安｜FAIL_INSEN｜1,527円｜💰15.9万円｜—
- 9166 GENDA Inc.｜granville_oshime｜業績データ取得不可(None)｜🟢値頃｜FAIL_INSEN｜660円｜💰6.9万円｜—
- 8343 Akita Bank, Ltd.｜granville_oshime｜業績データ取得不可(売上/経常欠損)(None)｜🟢値頃｜FAIL_INSEN｜1,391円｜💰14.8万円｜—
- 8367 Nanto Bank Ltd.｜granville_oshime｜取得不可(None)｜🟢値頃｜FAIL_INSEN｜1,753円｜💰18.2万円｜—
- 336A ダイナミックマッププラットフォーム｜granville_oshime｜業績データ取得不可(経常益予想非開示)(None)｜⚪妥当｜FAIL_INSEN｜1,224円｜💰13.2万円｜—
- 6027 Bengo4.com, Inc.｜granville_oshime/granville_rebound｜業績データ取得不可(None)｜🟡やや割高｜FAIL_UWAHIGE｜4,980円｜💰48.1万円｜—
- 8362 Fukui Bank, Ltd.｜granville_oshime｜🔻悪化(None)｜🔴過熱｜FAIL_INSEN｜6,620円｜💰69.3万円｜—
- 8410 Seven Bank, Ltd.｜granville_oshime｜None(None)｜None｜FAIL_INSEN｜335.3円｜💰0.0万円｜—
- 8622 Mito Securities Co., Ltd.｜granville_oshime/granville_rebound｜取得不可(None)｜⏸判定不能｜FAIL_INSEN｜759円｜💰7.8万円｜—
- 8624 Ichiyoshi Securities Co., Ltd.｜granville_oshime/granville_rebound｜取得不可(None)｜⏸判定不能｜FAIL_INSEN｜1,517円｜💰15.7万円｜—
- 8628 松井証券｜granville_oshime｜業績データ取得不可(None)｜⏸判定不能｜FAIL_INSEN｜1,067円｜💰11.1万円｜—
- 8708 アイザワ証券グループ｜granville_oshime｜取得不可(None)｜⏸判定不能｜FAIL_INSEN｜1,524円｜💰16.1万円｜—
- 9536 SAIBU GAS HOLDINGS CO. LTD.｜granville_oshime｜None(None)｜None｜FAIL_UWAHIGE｜2,452円｜💰0.0万円｜—
- 6769 Thine Electronics, Inc.｜granville_rebound｜🚀確変(11)｜⚪妥当｜FAIL_INSEN｜1,000円｜💰11.1万円｜—
- 3691 DIGITAL PLUS, Inc.｜granville_rebound｜🔥絶好調(10)｜⚪妥当｜FAIL_INSEN｜1,626円｜💰16.9万円｜—
- 1436 GreenEnergy & Company｜granville_rebound｜🔥絶好調(9)｜💎割安｜FAIL_INSEN｜1,516円｜💰17.1万円｜—
- 2122 インタースペース｜granville_rebound｜🔥絶好調(9)｜⚪妥当｜FAIL_INSEN｜1,317円｜💰13.4万円｜—
- 6963 ROHM Company Limited｜granville_rebound｜🔥絶好調(9)｜⚪妥当｜FAIL_INSEN｜3,758円｜💰39.6万円｜—
- 8995 Makoto Construction Co,Ltd｜granville_rebound｜🔥絶好調(9)｜⚪妥当｜FAIL_INSEN｜1,472円｜💰16.5万円｜—
- 5242 EYEZ INC.｜granville_rebound｜⚡好調(7)｜🔴過熱｜FAIL_INSEN｜2,838円｜💰28.7万円｜—
- 2354 YE DIGITAL CORPORATION｜granville_rebound｜⚡好調(5)｜🟢値頃｜FAIL_INSEN｜1,029円｜💰10.8万円｜—
- 6597 HPC SYSTEMS Inc.｜changepoint/changepoint🔔｜⚡好調(5)｜🟢値頃｜FAIL_INSEN｜3,060円｜💰35.6万円｜—
- 3687 Fixstars Corp.｜granville_rebound｜⚡好調(5)｜⚪妥当｜FAIL_INSEN｜1,865円｜💰21.0万円｜—
- 5574 ABEJA,Inc.｜granville_rebound｜⚡好調(5)｜🟡やや割高｜FAIL_INSEN｜2,330円｜💰23.3万円｜—
- 4997 日本農薬｜granville_rebound｜✅順調(4)｜🟡やや割高｜FAIL_INSEN｜1,059円｜💰10.7万円｜—
- 1407 West Holdings Corporation｜granville_rebound｜✅順調(3)｜🟢値頃｜FAIL_INSEN｜2,176円｜💰22.7万円｜—
- 4346 NEXYZ.Group Corporation｜granville_rebound｜✅順調(3)｜🟢値頃｜FAIL_UWAHIGE｜749円｜💰7.5万円｜—
- 7354 Direct Marketing MiX Inc.｜granville_rebound｜✅順調(3)｜⚪妥当｜FAIL_UWAHIGE｜350円｜💰3.5万円｜—
- 2681 2nd RETAILING Co., Ltd.｜granville_rebound｜✅順調(3)｜🟡やや割高｜FAIL_INSEN｜1,973円｜💰21.9万円｜—
- 4082 第一稀元素化学工業｜granville_rebound｜🔻悪化(3)｜🟡やや割高｜FAIL_INSEN｜1,750円｜💰18.7万円｜—
- 3653 Morpho, Inc.｜granville_rebound｜🔻悪化(2)｜💎割安｜FAIL_INSEN｜885円｜💰9.1万円｜—
- 3907 Silicon Studio Corp.｜granville_rebound｜🔻悪化(2)｜🟢値頃｜FAIL_INSEN｜1,385円｜💰16.2万円｜—
- 4440 WITZ Corp.｜granville_rebound｜➖横ばい(2)｜🔴過熱｜FAIL_INSEN｜1,723円｜💰18.8万円｜—
- 8163 SRS HOLDINGS CO.,LTD.｜granville_rebound｜➖横ばい(2)｜🔴過熱｜FAIL_UWAHIGE｜1,681円｜💰16.8万円｜—
- 4691 Washington Hotel Corp.｜granville_rebound｜⚠減速(1)｜⚪妥当｜FAIL_INSEN｜1,818円｜💰19.1万円｜—
- 6203 Howa Machinery, Ltd.｜granville_rebound｜⚠減速(1)｜🟡やや割高｜FAIL_INSEN｜1,920円｜💰20.8万円｜—
- 6522 アスタリスク｜granville_rebound｜⚠減速(0)｜⚪妥当｜FAIL_INSEN｜811円｜💰9.2万円｜—
- 8360 Yamanashi Chuo Bank, Ltd.｜granville_rebound｜取得不可(None)｜💎割安｜FAIL_INSEN｜1,248円｜💰13.0万円｜—
- 3778 SAKURA Internet Inc.｜granville_rebound｜業績データ取得不可(None)｜🟢値頃｜FAIL_INSEN｜2,895円｜💰31.6万円｜—
- 8366 Shiga Bank, Ltd.｜granville_rebound｜取得不可(None)｜⚪妥当｜FAIL_INSEN｜2,573円｜💰26.9万円｜—
- 8368 Hyakugo Bank, Ltd.｜granville_rebound｜取得不可(None)｜🟡やや割高｜FAIL_INSEN｜2,089円｜💰21.9万円｜—
- 8713 Fidea Holdings Co.Ltd.｜granville_rebound｜業績データ取得不可(売上/経常欠損)(None)｜🔴過熱｜FAIL_INSEN｜2,377円｜💰24.3万円｜—
- 4100 Toda Kogyo Corp.｜granville_rebound｜None(None)｜None｜FAIL_INSEN｜1,610円｜💰0.0万円｜—
- 477A Startline CO.,LTD.｜granville_rebound｜None(None)｜None｜FAIL_UWAHIGE｜730円｜💰0.0万円｜—
- 6890 Ferrotec Corporation｜granville_rebound｜None(None)｜None｜FAIL_INSEN｜7,930円｜💰0.0万円｜—
- 7175 Imamura Securities Co.Ltd.｜granville_rebound｜業績データ取得不可(None)｜⏸判定不能｜FAIL_INSEN｜1,684円｜💰18.6万円｜—
- 7380 Juroku Financial Group,Inc.｜granville_rebound｜None(None)｜None｜FAIL_INSEN｜2,339円｜💰0.0万円｜—
- 8344 Yamagata Bank, Ltd.｜granville_rebound｜None(None)｜None｜FAIL_INSEN｜4,270円｜💰0.0万円｜—
- 8392 Oita Bank, Ltd.｜granville_rebound｜None(None)｜None｜FAIL_INSEN｜2,710円｜💰0.0万円｜—
- 9278 BOOKOFF GROUP HOLDINGS LIMITED｜granville_rebound｜None(None)｜None｜FAIL_INSEN｜2,412円｜💰0.0万円｜—
- 4418 Japan Data Science Consortium Co Ltd.｜changepoint🔔｜⚠減速(3)｜🟡やや割高｜FAIL_UWAHIGE｜1,123円｜💰11.6万円｜—

## 変化点銘柄
- 4180 ＡＰＰＩＥＲ　ＧＲＯＵＰ｜changepoint🔔/granville_oshime｜🔥絶好調(8)｜⚪妥当｜FAIL_INSEN｜1,437円｜💰14.1万円｜—
- 5803 フジクラ｜changepoint🔔/changepoint🔔｜🚀確変(12)｜🟢値頃｜FAIL_INSEN｜4,078円｜💰44.8万円｜—
- 4011 Headwaters Co.,Ltd｜changepoint🔔/changepoint｜🚀確変(11)｜🟢値頃｜FAIL_INSEN｜2,251円｜💰22.4万円｜—
- 6254 野村マイクロ・サイエンス｜changepoint🔔｜🔥絶好調(10)｜💎割安｜FAIL_INSEN｜2,910円｜💰31.6万円｜—
- 9888 UEX LTD｜changepoint/changepoint🔔｜🔥絶好調(10)｜🟢値頃｜PASS｜1,477円｜💰14.8万円｜changepoint 1477 想定損失幅21.5%。 ⚠1単元リスク31,700円（枠超過）｜📋カルテ窓 11/10(残12営業日)｜🔒実弾封印中(PL3紙ログ収集中)｜⚠1単元でリスク枠超過（31,700円）｜📢
  > 【業態】ステンレス鋼の専門商社。生産材が中心。中国での加工品製販や機械の製販も。
  > 【いま】終値1,477円・直近5日+24.33%・📢業績予想の修正に関するお知らせ
  > 【調子】🔥絶好調（10/13）
  > 【水準】🟢値頃（5.0/7）— PER5.07倍・PEG0.0678・52週99.4% ／ 💰単元14.8万円
  > 【戦略】発火日終値1,477円の指値。追撃禁止・SL1,160円。🔒実弾封印中（PL3紙ログ収集中）／⚠1単元リスク31,700円（枠超過）
- 4187 大阪有機化学工業｜changepoint/changepoint🔔｜🔥絶好調(10)｜⚪妥当｜FAIL_INSEN｜4,355円｜💰49.2万円｜—
- 7695 交換できるくん｜changepoint🔔｜🔥絶好調(10)｜⚪妥当｜FAIL_INSEN｜875円｜💰8.8万円｜—
- 6080 Ｍ＆Ａキャピタルパートナーズ｜changepoint/changepoint🔔｜🔥絶好調(10)｜⚪妥当｜FAIL_INSEN｜4,260円｜💰44.3万円｜—
- 584A LiNKX, Inc.｜changepoint🔔/changepoint🔔｜🔥絶好調(9)｜🟢値頃｜FAIL_UWAHIGE｜2,208円｜💰23.1万円｜—
- 6136 OSG CORP｜changepoint/changepoint🔔｜🔥絶好調(9)｜⚪妥当｜FAIL_INSEN｜3,571円｜💰38.6万円｜—
- 6857 アドバンテスト｜changepoint/changepoint🔔｜🔥絶好調(9)｜⚪妥当｜FAIL_INSEN｜32,370円｜💰344.5万円｜—
- 8151 東陽テクニカ｜changepoint🔔｜🔥絶好調(9)｜⚪妥当｜FAIL_UWAHIGE｜1,917円｜💰19.2万円｜—
- 9962 ミスミグループ本社｜changepoint/changepoint🔔｜🔥絶好調(9)｜⚪妥当｜FAIL_INSEN｜3,701円｜💰39.4万円｜—
- 4382 HEROZ, Inc.｜changepoint🔔/changepoint🔔🔔｜🔥絶好調(9)｜🟡やや割高｜FAIL_INSEN｜1,640円｜💰16.3万円｜—
- 7318 セレンディップ・ホールディングス｜changepoint🔔/changepoint🔔🔔｜🔥絶好調(8)｜💎割安｜FAIL_INSEN｜1,124円｜💰12.4万円｜—
- 4368 4368｜changepoint/changepoint🔔｜🔥絶好調(8)｜⚪妥当｜FAIL_INSEN｜2,880円｜💰31.6万円｜—
- 5582 （名称取得不可）｜changepoint🔔｜🔥絶好調(8)｜⚪妥当｜FAIL_INSEN｜1,905円｜💰19.9万円｜—
- 478A Hutzper Inc.｜changepoint🔔｜⚡好調(7)｜⚪妥当｜FAIL_INSEN｜673円｜💰6.8万円｜—
- 3091 ブロンコビリー｜changepoint/changepoint🔔🔔｜⚡好調(7)｜🟡やや割高｜FAIL_INSEN｜2,943円｜💰29.6万円｜—
- 8704 トレイダーズホールディングス｜changepoint/changepoint🔔｜⚡好調(5)｜💎割安｜FAIL_INSEN｜1,270円｜💰13.2万円｜—
- 6284 日精エー・エス・ビー機械｜changepoint🔔｜⚡好調(5)｜🟢値頃｜FAIL_INSEN｜8,060円｜💰85.4万円｜—
- 218A Liberaware｜changepoint/changepoint🔔｜⚡好調(5)｜⚪妥当｜FAIL_INSEN｜891円｜💰9.3万円｜—
- 6785 鈴木｜changepoint/changepoint🔔🔔｜✅順調(4)｜⚪妥当｜FAIL_INSEN｜3,240円｜💰34.0万円｜—
- 593A ティアフォー｜changepoint/changepoint🔔｜✅順調(4)｜🟡やや割高｜FAIL_INSEN｜1,943円｜💰20.1万円｜—
- 4165 PLAID Inc.｜changepoint🔔｜🔻悪化(4)｜🔴過熱｜FAIL_INSEN｜770円｜💰7.7万円｜—
- 4498 Cybertrust Japan Co., Ltd.｜changepoint🔔/changepoint🔔🔔｜✅順調(4)｜🔴過熱｜PASS｜2,560円｜💰25.6万円｜changepoint 2560 想定損失幅38.7%。 ⚠1単元リスク99,000円（枠超過） 決算前に建てるなら反応日の引けまでに撤収（教訓⑲）｜⏰決算 10/29(残5営業日)｜🔒実弾封印中(PL3紙ログ収集中)｜⚠1単元でリスク枠超過（99,000円）
  > 【業態】情報・通信業
  > 【いま】終値2,560円・直近5日+68.20%（材料未確認）
  > 【調子】✅順調（4/13）
  > 【水準】🔴過熱（0.0/7）— PER33.86倍・PEG2.6719・52週100.0% ／ 💰単元25.6万円
  > 【戦略】発火日終値2,560円の指値。追撃禁止・SL1,570円。🔒実弾封印中（PL3紙ログ収集中）／⚠1単元リスク99,000円（枠超過）
- 4071 Plus Alpha Consulting Co. LTD.｜changepoint🔔｜✅順調(3)｜⚪妥当｜FAIL_UWAHIGE｜2,321円｜💰22.6万円｜—
- 598A チャットプラス｜changepoint🔔/changepoint｜✅順調(3)｜⚪妥当｜FAIL_INSEN｜1,151円｜💰12.3万円｜—
- 339A PROGRESS TECHNOLOGIES GROUP INC｜changepoint/changepoint🔔｜➖横ばい(2)｜⚪妥当｜FAIL_UWAHIGE｜824円｜💰8.2万円｜—
- 4488 AI inside Inc.｜changepoint｜➖横ばい(2)｜🟡やや割高｜FAIL_UWAHIGE｜2,040円｜💰21.2万円｜—
- 4259 ExaWizards Inc.｜changepoint/changepoint🔔｜業績データ取得不可(None)｜⚪妥当｜FAIL_INSEN｜779円｜💰8.1万円｜—
- 4478 freee K.K.｜changepoint🔔｜業績データ取得不可(None)｜⚪妥当｜FAIL_INSEN｜3,950円｜💰37.9万円｜—
- 3993 PKSHA Technology, Inc.｜changepoint🔔｜業績データ取得不可(None)｜⚪妥当｜FAIL_UWAHIGE｜3,635円｜💰36.4万円｜—

## 🤖AI特需銘柄
波: なし（wave_on のセクター無し）／25MA 上回り率 📡エネマネ・計量 14.29%・❄️冷却・空調 16.67%・🌐光通信 9.09%・🔬基板・素材 4.76%（ai_scan 2026-10-22・候補 0件）
- 6754 アンリツ｜ai_reversal/choruko_reversal｜⚡好調(7)｜⚪妥当｜FAIL_INSEN｜2,845.5円｜💰30.3万円｜—
- 6505 東洋電機製造｜ai_momentum/stf_kakuhen｜⚡好調(5)｜⚪妥当｜FAIL_INSEN｜3,105円｜💰31.5万円｜—
- 3131 シンデンハイテックス｜ai_momentum｜🚀確変(12)｜💎割安｜FAIL_INSEN｜6,240円｜💰73.6万円｜—
- 2760 東京エレクトロンデバイス｜ai_momentum/granville_oshime｜🔥絶好調(10)｜⚪妥当｜FAIL_INSEN｜4,460円｜💰49.2万円｜—
- 9824 泉州電業｜ai_momentum｜🔥絶好調(10)｜⚪妥当｜FAIL_INSEN｜7,790円｜💰79.9万円｜—
- 6521 オキサイド｜ai_momentum｜⚡好調(7)｜🟢値頃｜FAIL_INSEN｜2,951円｜💰33.8万円｜—
- 1982 日比谷総合設備｜ai_momentum｜⚠減速(1)｜🔴過熱｜FAIL_INSEN｜3,185円｜💰33.5万円｜—
- 4062 IBIDEN CO., LTD.｜ai_reversal｜🔥絶好調(9)｜⚪妥当｜FAIL_INSEN｜8,598円｜💰97.6万円｜—
- 6981 村田製作所｜ai_reversal｜🔥絶好調(9)｜⚪妥当｜FAIL_INSEN｜6,432円｜💰68.0万円｜—
- 7433 伯東｜ai_reversal｜🔥絶好調(9)｜⚪妥当｜FAIL_INSEN｜1,791円｜💰54.1万円｜—
- 8098 稲畑産業｜ai_reversal/granville_oshime｜✅順調(4)｜🔴過熱｜FAIL_UWAHIGE｜4,475円｜💰44.8万円｜—
- 6643 戸上電機製作所｜ai_reversal｜✅順調(3)｜⚪妥当｜FAIL_INSEN｜5,140円｜💰52.7万円｜—
- 5302 日本カーボン｜ai_reversal｜➖横ばい(2)｜🔴過熱｜FAIL_INSEN｜4,900円｜💰50.9万円｜—
- 6590 芝浦メカトロニクス｜ai_reversal｜➖横ばい(2)｜🔴過熱｜FAIL_INSEN｜3,190円｜💰39.5万円｜—
- 9432 NTT｜ai_reversal｜➖横ばい(2)｜🔴過熱｜FAIL_UWAHIGE｜178.1円｜💰1.8万円｜—

## ⚡材料後出し
その日の足は開示前の情報。判定は参考値
- 2980 SRE Holdings Corp.｜FAIL_INSEN｜📌（訂正・数値データ訂正）「2026年３月期 決算短信〔日本基準〕（連結）」の一部訂正について｜15:30
- 6289 Giken Ltd.｜FAIL_UWAHIGE｜📌有償ストック・オプション（新株予約権）の発行に関するお知らせ｜15:30
- 3843 Freebit Co., Ltd.｜FAIL_INSEN｜📌当社連結子会社による株式取得（孫会社化）に関するお知らせ｜16:30
- 8954 ORIX JREIT Inc.｜FAIL_INSEN｜📊2026年8月期 決算短信(REIT)｜15:30
- 5932 三協立山｜FAIL_UWAHIGE｜📌株式報酬制度の導入に伴う信託設定及び自己株式の処分の中止に関するお知らせ｜18:00
- 6562 Geniee, Inc.｜FAIL_INSEN｜📌法定事後開示書類（合併）（CATS株式会社）｜15:30
- 3091 ブロンコビリー｜FAIL_INSEN｜📊2026年12月期　第３四半期決算短信〔日本基準〕（連結）｜15:30
- 8704 トレイダーズホールディングス｜FAIL_INSEN｜📌非上場の親会社等の決算に関するお知らせ｜16:00

## 📢開示
使用URL: https://kabutan.jp/disclosures/?kubun=&date=20261022&page=1〜21（全21ページ・312行を取得。フォールバックなし）。
- 📢 9888 UEX LTD｜業績予想の修正に関するお知らせ｜14:00
- 📊 3091 ブロンコビリー｜2026年12月期　第３四半期決算短信〔日本基準〕（連結）｜15:30
- 📊 8954 ORIX JREIT Inc.｜2026年8月期 決算短信(REIT)｜15:30
- 📌 5932 三協立山｜株式報酬制度の導入に伴う信託設定及び自己株式の処分の中止に関するお知らせ｜18:00
- 📌 3843 Freebit Co., Ltd.｜当社連結子会社による株式取得（孫会社化）に関するお知らせ｜16:30
- 📌 4743 ITFOR Inc.｜（訂正）2026年10月14日に公表したPR情報の一部訂正について｜16:00
- 📌 8704 トレイダーズホールディングス｜非上場の親会社等の決算に関するお知らせ｜16:00
- 📌 2334 Eole, Inc.｜イオレグループ、全国300拠点・総受電容量600MW規模の分散型AIデータセンター構築プロジェクトに参画｜15:30
- 📌 2980 SRE Holdings Corp.｜（訂正・数値データ訂正）「2026年３月期 決算短信〔日本基準〕（連結）」の一部訂正について｜15:30
- 📌 2980 SRE Holdings Corp.｜（訂正・数値データ訂正）「2027年３月期　第1四半期決算短信〔日本基準〕（連結）」の一部訂正について｜15:30
- 📌 4565 Nxera Pharma Co., Ltd.｜デュシェンヌ型筋ジストロフィー治療薬vamoroloneの韓国における製造販売承認申請のお知らせ｜15:30
- 📌 6289 Giken Ltd.｜有償ストック・オプション（新株予約権）の発行に関するお知らせ｜15:30
- 📌 6562 Geniee, Inc.｜法定事後開示書類（合併）（CATS株式会社）｜15:30
- 📌 5027 AnyMind Group Inc.｜AnyMind Group、米国法人「AnyMind USA, Inc.」を設立し、米国市場での事業を本格開始｜15:00
- 📌 4418 Japan Data Science Consortium Co Ltd.｜ストック・オプション（新株予約権）の発行に関するお知らせ｜14:00
- 📌 7350 Okinawa Financial Group, Inc.｜2027年３月期第２四半期末の有価証券含み損に関するお知らせ｜13:00
- 📌 4477 BASE, Inc.｜ＳＢＩＮＭ合同会社（ＳＢＩホールディングス株式会社の完全子会社）による当社株式に対する公開買付けの結果に関するお知らせ｜12:00
①-9へ引き渡し2件（📊でFAIL銘柄・recalc_queue）

## 総当りゲート
### 5手法
- PASS（21）: 5034 unerry, Inc.、4743 ITFOR Inc.、3222 United Super Markets Holdings, Inc.、8987 Japan Excellent, Inc.、8198 Maxvalu Tokai Co., Ltd.、2659 SAN-A CO., LTD.、5021 Cosmo Energy Holdings Co., Ltd.、8276 HEIWADO CO., LTD.、9974 BELC Co., Ltd.、3234 Mori Hills Reit Investment Corporation、3249 Industrial & Infrastructure Fund Investment Corporation、3283 Nippon Prologis REIT, Inc.、8955 Japan Prime Realty Investment Corporation、8961 MORI TRUST REIT.Inc、6183 BELLSYSTEM24 Holdings, Inc.、4928 Noevir Holdings Co., Ltd.、1662 Japan Petroleum Exploration Co., Ltd.、8174 NIPPON GAS Co., Ltd.、3591 WACOAL HOLDINGS CORP、7811 Nakamoto Packs Co. Ltd.、4493 Cyber Security Cloud, Inc.
- PASS_DOJI（1）: 4176 ココナラ
- FAIL_UWAHIGE（44）: 4053 Sun Asterisk, Inc.、4434 Serverworks Co., Ltd.、618A KOMPEITO Inc.、4377 ONE CAREER Inc.、4058 Toyokumo, Inc.、6071 IBJ, Inc.、3798 ULS Group Incorporated、5038 eWeLL Co.,Ltd、6289 Giken Ltd.、4379 Photosynth inc.、8871 GOLDCREST Co., Ltd.、7733 Olympus Corp.、8282 K'S HOLDINGS CORPORATION、8125 Wakita & Co., Ltd.、8278 Fuji Co., Ltd.、7458 Daiichikosho Co., Ltd.、2702 日本マクドナルドホールディングス、2782 Seria Co., Ltd.、2809 Kewpie Corporation、3279 Activia Properties, Inc.、3148 Create SD Holdings Co., Ltd.、1820 Nishimatsu Construction Co., Ltd.、9882 Yellow Hat Ltd.、1860 Toda Corporation、7984 Kokuyo Co., Ltd.、8818 Keihanshin Building Co., Ltd.、1333 Umios Corporation、8953 Japan Metropolitan Fund Investment Corporation、6753 Sharp Corporation、9948 Arcs Company, Limited、3309 Sekisui House Reit. Inc.、2815 ARIAKE JAPAN Co., Ltd.、8585 Orient Corporation、8194 Life Corporation、9533 TOHO GAS Co., Ltd.、9699 NISHIO HOLDINGS CO. LTD.、7624 NaITO、5932 三協立山、3479 ティーケーピー、6532 ベイカレント、9960 トーテック、4658 日本空調サービス、8098 稲畑産業、9432 NTT
- FAIL_INSEN（148）: 6627 Tera Probe, Inc.、5137 Smart Drive Co. Ltd.、276A CCReB Advisors Inc.、3556 RenetJapanGroup, Inc.、6862 Minato Holdings Inc.、5027 AnyMind Group Inc.、5136 tripla Co.,Ltd.、5757 CK San-Etsu Co., Ltd.、212A FIT EASY Inc.、9554 AViC Co. Ltd.、421A Movin' Strategic Career CO.,LTD.、5132 pluszero,Inc.、6298 Y.A.C.HOLDINGS CO.,LTD.、5537 AlbaLink Co.,Ltd.、9556 INTLOOP, Inc.、7047 PORT INC.、3915 TerraSky Co., Ltd.、5821 Hirakawa Hewtech Corp.、9560 PROGRIT, Inc.、558A SQUEEZE Inc.、147A SORACOM,INC.、7678 ASAKUMA CO.,LTD.、9268 OPTIMUS GROUP Co., Ltd.、4477 BASE, Inc.、9628 San Holdings,Inc.、2980 SRE Holdings Corp.、4412 Science Arts, Inc.、505A Geekly,Inc.、6629 TECHNO HORIZON Co., Ltd.、3077 Horiifoodservice Co., Ltd.、6918 Aval Data Corporation、7567 Sakae Electronics Corp.、269A SAPEET、6337 Tesec Corporation、3696 セレス、2930 北の達人コーポレーション、2820 Yamami Co.、3843 Freebit Co., Ltd.、4331 Take and Give. Needs Co., Ltd.、7161 Jimoto Holdings, Inc.、4565 Nxera Pharma Co., Ltd.、2340 Gokurakuyu Holdings Co., Ltd.、446A ノースサンド、3391 TSURUHA Holdings, Inc.、3186 ネクステージ、6268 Nabtesco Corporation、6324 Harmonic Drive Systems Inc.、1803 Shimizu Corporation、4023 クレハ、5301 Tokai Carbon Co., Ltd.、7004 Kanadevia Corporation、2874 YOKOREI CO. LTD.、8522 Bank of Nagoya, Ltd.、6754 アンリツ、8088 IWATANI Corporation、8386 Hyakujushi Bank, Ltd.、9412 SKY Perfect JSAT Corporation、9861 吉野家ホールディングス、4666 Park24 Co., Ltd.、7721 Tokyo Keiki Inc.、8381 San-in Godo Bank Ltd.、8954 ORIX JREIT Inc.、8393 Miyazaki Bank Ltd.、268A Rigaku Holdings Corporation、8524 North Pacific Bank, Ltd.、3282 Comforia Residential REIT, Inc.、8952 Japan Real Estate Investment Corp.、6925 Ushio Inc.、1861 Kumagai Gumi Co., Ltd.、1417 MIRAIT ONE Corporation、1952 Shin Nippon Air Technologies Co., Ltd.、6269 Modec, Inc.、7003 Mitsui ES Holdings Co., Ltd.、8584 Jaccs Co., Ltd.、1944 Kinden Corporation、8066 Mitani Corporation、2805 S&B Foods Inc.、6055 Japan Material Co., Ltd.、3289 Tokyu Fudosan Holdings Corp.、1719 HAZAMA ANDO Corporation、1833 Okumura Corporation、9503 Kansai Electric Power Company, Incorporated、6366 Chiyoda Corp.、7220 Musashi Seimitsu Industry Co., Ltd.、5844 Kyoto Financial Group,Inc.、2379 dip Corporation、6479 MinebeaMitsumi Inc.、1893 Penta-Ocean Construction Co., Ltd.、3292 AEON REIT Investment Corp.、3296 NIPPON REIT Investment Corp、3462 Nomura Real Estate Master Fund, Inc.、5482 Aichi Steel Corporation、8986 Daiwa Securities Living Investment Corporation、1946 Toenec Corporation、5631 Japan Steel Works, Ltd.、5310 Toyo Tanso Co., Ltd.、6960 Fukuda Denshi Co., Ltd.、9436 Okinawa Cellular Telephone Company、6804 Hosiden Corp.、1969 Takasago Thermal Engineering Co., Ltd.、8253 Credit Saison Co., Ltd.、5831 Shizuoka Financial Group, Inc.、7201 Nissan Motor Co., Ltd.、7381 CCI Group, Inc.、8345 Bank of Iwate Ltd.、3471 Mitsui Fudosan Logistics Park, Inc.、8399 Bank Of The Ryukyus,Limited、7384 Procrea Holdings,Inc.、8304 Aozora Bank, Ltd.、5344 MARUWA CO., LTD.、8511 Japan Securities Finance Co., Ltd.、1963 JGC Holdings Corporation、3105 Nisshinbo Holdings Inc.、3445 RS Technologies Co. Ltd.、4088 Air Water Inc.、4966 C. Uyemura & Co., Ltd.、6332 TSUKISHIMA HOLDINGS CO. LTD.、6645 OMRON Corporation、6875 Megachips Corporation、7322 San ju San Financial Group, Inc.、8334 Gunma Bank, Ltd.、8359 Hachijuni Nagano Bank, Ltd.、5018 ＭＯＲＥＳＣＯ、6668 ＡＤプラズマ、7713 シグマ光機、5246 ELEMENTS,Inc.、3498 霞ヶ関Ｃ、3994 マネーフォワード、4443 Ｓａｎｓａｎ、6814 古野電、6505 東洋電機製造、3131 シンデンハイテックス、2760 東京エレクトロンデバイス、9824 泉州電業、6521 オキサイド、1982 日比谷総合設備、4062 IBIDEN CO., LTD.、6981 村田製作所、7433 伯東、6779 Nihon Dempa Kogyo Co., Ltd.、5208 Arisawa Mfg.Co., Ltd.、6643 戸上電機製作所、5302 日本カーボン、6590 芝浦メカトロニクス、9211 f-code Inc.、2334 Eole, Inc.、4431 スマレジ、5590 NETSTARS Co.,Ltd.
### グランビル
- PASS（12）: 9006 京浜急行電鉄、4763 クリーク・アンド・リバー社、6432 Takeuchi Mfg.Co., Ltd.、2288 Marudai Food Co., Ltd.、6988 日東電工、8060 キヤノンマーケティングジャパン、8850 スターツコーポレーション、1879 新日本建設、9044 NANKAI Co., Ltd.、3107 ダイワボウホールディングス、9616 共立メンテナンス、9900 Sagami Holdings Corp.
- FAIL_UWAHIGE（40）: 8095 Astena Holdings Co.,Ltd.、8793 ＮＥＣキャピタルソリューション、3496 AZOOM CO.,LTD、7744 Noritsu Koki Co., Ltd.、9064 ヤマトホールディングス、4507 Shionogi & Co., Ltd.、9048 名古屋鉄道、2331 ALSOK CO., LTD.、3661 m-up holdings, Inc.、8020 Kanematsu Corporation、9828 Genki Global Dining Concepts Corp、5036 Japan Business Systems, Inc.、6371 Tsubakimoto Chain Co.、4166 Cacco, Inc.、5461 Chubu Steel Plate Co., Ltd.、6328 Ebara Jitsugyo Co., Ltd.、2002 日清製粉グループ本社、7751 キヤノン、4375 Safie Inc.、8424 芙蓉総合リース、2871 ニチレイ、2767 円谷フィールズホールディングス、4413 baudroie,inc.、6058 VECTOR Inc.、4475 HENNGE K.K.、4373 Simplex Holdings,Inc.、3097 Monogatari Corporation、456A Human Made Inc.、7504 Kohsoku Corporation、9505 Hokuriku Electric Power Company、8043 Starzen Company Limited、8255 Axial Retailing, Inc.、8097 SAN-AI OBBLI CO. LTD、6027 Bengo4.com, Inc.、9536 SAIBU GAS HOLDINGS CO. LTD.、4346 NEXYZ.Group Corporation、7354 Direct Marketing MiX Inc.、8163 SRS HOLDINGS CO.,LTD.、477A Startline CO.,LTD.、4418 Japan Data Science Consortium Co Ltd.
- FAIL_INSEN（134）: 3374 Naigai Tec Corporation、6752 パナソニックHD、3103 ユニチカ、5254 Arent, Inc.、8944 Land Business Co., Ltd.、7725 INTER ACTION Corporation、9553 MicroAd, Inc.、6905 Cosel Co., Ltd.、2986 LA Holdings Co.,Ltd、6562 Geniee, Inc.、1945 Tokyo Energy & Systems Inc.、6473 JTEKT Corporation、8697 Japan Exchange Group, Inc.、6255 NPC Incorporated、4544 H.U.Group Holdings, Inc.、3741 Systems Engineering Consultants Co., Ltd.、6302 Sumitomo Heavy Industries, Ltd.、5838 Rakuten Bank, Ltd.、6470 Taiho Kogyo Co., Ltd.、7199 Premium Group Co., Ltd.、3064 MonotaRO Co., Ltd.、3935 Edia Co. Ltd.、6196 Strike Group Co. Ltd.、3562 No.1 Co., Ltd.、8061 Seika Corporation、7970 Shin-Etsu Polymer Co., Ltd.、6454 Max Co., Ltd.、8014 Chori Co., Ltd.、6592 Mabuchi Motor Co., Ltd.、3433 TOCALO Co., Ltd.、8927 Meiho Enterprise Co., Ltd.、186A Astroscale Holdings Inc.、4183 Mitsui Chemicals, Inc.、4272 Nippon Kayaku Co., Ltd.、4956 Konishi Co., Ltd.、7181 JAPAN POST INSURANCE Co., Ltd.、7734 Riken Keiki Co., Ltd.、7513 Kojima Co., Ltd.、6208 Ishikawa Seisakusho,Ltd.、2413 エムスリー、4617 Chugoku Marine Paints,Ltd.、8081 Kanaden Corporation、5071 VIS Co., Ltd.、6770 Alps Alpine Co., Ltd.、1815 鉄建建設、4169 Enechange Ltd.、4534 Mochida Pharmaceutical Co., Ltd.、4549 Eiken Chemical Co., Ltd.、4552 JCR Pharmaceuticals Co., Ltd.、4902 Konica Minolta, Inc.、6768 Tamura Corporation、8012 Nagase & Co., Ltd.、9163 Nareru Group Inc.、9837 Morito Co., Ltd.、4937 Ｇ−ＷＡＱＯＯ、3083 Star seeds Co.,Ltd.、290A ＳＹＮＳＰＥＣＴＩＶＥ、5243 note inc.、7806 MTG Co., Ltd.、6834 Seikoh Giken Co., Ltd.、6613 QD Laser, Inc.、8336 Musashino Bank, Ltd.、8008 Yondoshi Holdings, Inc.、8346 Toho Bank, Ltd.、7856 HAGIHARA INDUSTRIES INC.、6736 Suncorporation、9902 Nichiden Corporation、6523 PHC Holdings Corp.、7609 Daitron Co., Ltd.、4667 Aisan Technology Co., Ltd.、6023 ダイハツインフィニアース、6250 Yamabiko Corporation、6227 AIMECHATEC Ltd.、2602 日清オイリオグループ、8919 カチタス、6570 Kyowa Corporation Co. Ltd.、7616 Colowide Co., Ltd.、8714 Senshu Ikeda Holdings,Inc.、7350 Okinawa Financial Group, Inc.、6998 Nippon Tungsten Co., Ltd.、5985 SUNCALL CORPORATION、1518 三井松島ホールディングス、6379 RAIZNEXT Corporation、4044 Central Glass Co., Ltd.、4208 UBE Corporation、9509 Hokkaido Electric Power Company,Incorporated、6072 Jibannet Holdings Co., Ltd.、7630 Ichibanya Co., Ltd.、3048 ビックカメラ、8059 Daiichi Jitsugyo Co., Ltd.、8361 Ogaki Kyoritsu Bank, Ltd.、9166 GENDA Inc.、8343 Akita Bank, Ltd.、8367 Nanto Bank Ltd.、336A ダイナミックマッププラットフォーム、8362 Fukui Bank, Ltd.、8410 Seven Bank, Ltd.、8622 Mito Securities Co., Ltd.、8624 Ichiyoshi Securities Co., Ltd.、8628 松井証券、8708 アイザワ証券グループ、6769 Thine Electronics, Inc.、3691 DIGITAL PLUS, Inc.、1436 GreenEnergy & Company、2122 インタースペース、6963 ROHM Company Limited、8995 Makoto Construction Co,Ltd、5242 EYEZ INC.、2354 YE DIGITAL CORPORATION、6597 HPC SYSTEMS Inc.、3687 Fixstars Corp.、5574 ABEJA,Inc.、4997 日本農薬、1407 West Holdings Corporation、2681 2nd RETAILING Co., Ltd.、4082 第一稀元素化学工業、3653 Morpho, Inc.、3907 Silicon Studio Corp.、4440 WITZ Corp.、4691 Washington Hotel Corp.、6203 Howa Machinery, Ltd.、6522 アスタリスク、8360 Yamanashi Chuo Bank, Ltd.、3778 SAKURA Internet Inc.、8366 Shiga Bank, Ltd.、8368 Hyakugo Bank, Ltd.、8713 Fidea Holdings Co.Ltd.、4100 Toda Kogyo Corp.、6890 Ferrotec Corporation、7175 Imamura Securities Co.Ltd.、7380 Juroku Financial Group,Inc.、8344 Yamagata Bank, Ltd.、8392 Oita Bank, Ltd.、9278 BOOKOFF GROUP HOLDINGS LIMITED
### 変化点
- PASS（2）: 9888 UEX LTD、4498 Cybertrust Japan Co., Ltd.
- FAIL_UWAHIGE（6）: 584A LiNKX, Inc.、8151 東陽テクニカ、4071 Plus Alpha Consulting Co. LTD.、339A PROGRESS TECHNOLOGIES GROUP INC、4488 AI inside Inc.、3993 PKSHA Technology, Inc.
- FAIL_INSEN（25）: 4180 ＡＰＰＩＥＲ　ＧＲＯＵＰ、5803 フジクラ、4011 Headwaters Co.,Ltd、6254 野村マイクロ・サイエンス、4187 大阪有機化学工業、7695 交換できるくん、6080 Ｍ＆Ａキャピタルパートナーズ、6136 OSG CORP、6857 アドバンテスト、9962 ミスミグループ本社、4382 HEROZ, Inc.、7318 セレンディップ・ホールディングス、4368 4368、5582 （名称取得不可）、478A Hutzper Inc.、3091 ブロンコビリー、8704 トレイダーズホールディングス、6284 日精エー・エス・ビー機械、218A Liberaware、6785 鈴木、593A ティアフォー、4165 PLAID Inc.、598A チャットプラス、4259 ExaWizards Inc.、4478 freee K.K.
- 除籍リスト（SBIグループ登録解除候補）: なし

## 機械詳細
- 検知内訳: 評価433（プール433＋前夜提案のみ0）・本夜指名93（新規34）・除籍0・SKIP0・未マージPR由来0件（24時間以内に候補を持つ他ブランチ無し）
- log追記: base_day=2026-10-22 を置換/追記（最新30営業日保持）。recalc_queue 追加2件
- 抜粋規則: 通知の通過10件の群別内訳は通知に記載。PASS群別 method22/ai0/granville12/changepoint2/不明0
- gate_history: gate_history/2026-10-22.json を新規作成（verdicts433件・nominations93件）
- grades.json: 891銘柄/453KiB（463,512B・nx 付与716件）
- method_score: 保持59件／null374件
- ヘッドライン付与: 36/36件（PASS全件）
- kabutan取得: 銘柄トップ1/50件（4176 の業態・業種）／決算ページ40件（PASS＋保有）／優待ページ11件は403で取得不可
- profile_cache: 総数867・本夜 業態追加1件・業種 付与済み866／未付与1・業態「未取得」のまま出た件数0
- earnings_log: 総数73／本夜追記2件／リターンを埋めた15件／日足が取れず埋められなかった4件
- gyoseki_cache: 再計算1件（history退避1件）・判定保留/取得不可につき据置0件・next_earnings 更新6件
- pool_bars.json: 435銘柄/372KiB
- 鮮度ゲート: 鮮度切れ除外10件・nom_age分布 0-2:175/3-10:193/11+:65・last_seen欠損0件
- 記録の凍結: verdicts433件（評価433件と一致）／nominations93件（新規34・再指名59）
- トレンド文脈: ctx 合致113／不一致177／レンジ136／判定不能7・PASSのうち合致7件・形態が付いた銘柄185件
- 3日ルール判定（件数のみ）: 判定4銘柄・streak≥3 1・streak=2 0・判定不可0。銘柄別の R/streak は通知にのみ
- 業種別PER中央値: 算出できた業種25／母数不足9・spm を写せた銘柄385件
- 開示の分類別件数: 📢1/📉0/📊2/🔁0/👥0/🏛0/📦0/📌13
- 熟成由来の候補: 0件（うちPASS0）
- 権利情報: rights_cache 総数349・本夜 配当更新11件／優待取得0件（優待ページが403で取得不可）・優待 不明のまま349件
- 次回決算日: 付与740件／未発表182件・前年同期発表日 付与187件・earnings_calendar.json 922銘柄/95KiB（nx 内訳 一覧723/株探17）
- STEP 4.8 週末ブリーフ: week_open=false のためスキップ
- master.json の変更行数: +7900/-6466（indent=2）
