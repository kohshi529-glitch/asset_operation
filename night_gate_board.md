# 夜間ゲート 2026-10-28

## サマリー
- 評価数: 474 / PASS: 47（PASS_DOJI 8件を含む）
- 発注可能提案数: 32件
- 市場一言: 市場モード「強気ギャップアップ」（market.latest 2026-10-28）。プール474銘柄中PASS比率9.9%（陰線FAIL 353件・上髭FAIL 74件）
- 実行モード: 通常（base_day=当日の引け値を対象）
- base_day: 2026-10-28（run_at 2026-10-28 20:48起動）
- week_open: false（翌営業日 10/29(木)）→ STEP 4.8 週末ブリーフはスキップ
- 📆 翌営業日 10/29: 権利落ち日（10月・参考）, FOMC明け。T+2 10/30: 権利確定日・月末最終営業日, 日銀 金融政策決定会合 結果（後場から）, 📑TOPIX 段階的ウエイト低減 第1回/8（定期入替実施日）。次の TOPIX 低減日 10/30 第1回/8（あと2営業日）
- 📑指数: 低減対象 提案1件／PASS4件／プール72件・新規採用 16件（index_flags 2026-10-07 公表分）

## 検証結果
- V1 → はい（proposals32=results32=template32・board模擬32行）
- V2 → はい（PASS47=提案32+除外15・order_status欠落0）
- V3 → はい（results474件重複0）
- V4 → はい（既存 valuation static 変更0）
- V5 → はい（許可キー外の変更0・night_gate変更キー['pool', 'results', 'log', 'recalc_queue']・pipeline.runs変更['night_gate']・外部トップキー変更[]）
- V6 → はい（gyoseki grade絵文字整合 不整合0）
- V7 → はい（必須セクション存在（week_open=false のため今週のカタリスト対象外））
- V8 → はい（模擬32行の書式 不正0）
- V9 → はい（gate_history/2026-10-28.json 新規作成・today一致）
- V10 → はい（base_day 4箇所一致 2026-10-28）
- V11 → いいえ（+10677/-9568（indent=2・往復一致）＝results全置換＋キャッシュ更新のため5,000行を超過（全体再フォーマットではない：往復一致で同indent・総行数 約147k））
- V12 → はい（proposals/template/results 同順（厳密ソート一致））
- V13 → はい（948銘柄/534.5KiB（600KiB以下: True）・18キー欠落0・nx不一致0・ix非null197・spm検算True）
- V14 → はい（method_score 保持56件/null418件・出所不明・写し違い0）
- V15 → はい（PASS47件中47件に付与・欠落0・(c)違反0[]）
- V16 → はい（earnings_log総数96・本夜追記10・📊10件すべて記録（欠落0）・history<=4）
- V17 → はい（475銘柄/406.7KiB・保有3銘柄すべて収録・3日ルール判定3銘柄）
- V18 → はい（鮮度ゲート整合（鮮度切れ5件・誤除外0・誤提案0））
- V19 → はい（verdicts474件=評価474件・nominations87件（新規15/再指名72）・ctx {'不一致': 214, 'レンジ': 143, '合致': 111, '判定不能': 6}・profile既存変更0）
- V20 → はい（956銘柄・nx非null757・hist持ち409・pxd301）
- VLEAK → はい（公開物への保有情報 検出0件[]）

## 保有アラート
保有3銘柄・アラート19件（詳細は通知）

## 前夜の結果
PL5口座への正式な反映は週次①-11の採点で行われる。ここは参考情報。
前夜2026-10-27の提案78件 → 約定56・不約定22・判定不能0
- 276A momentum 指定4,655 → 約定4,655・終値4,500（-3.33%）
- 212A momentum 指定2,771 → 約定2,771・終値2,735（-1.30%）
- 505A momentum 指定1,171 → 約定1,172・終値1,165（-0.60%）
- 618A momentum 指定2,138 → 約定2,138・終値2,136（-0.09%）
- 8336 reversal 指定2,565 → 約定2,565・終値2,580（+0.58%）
- 3036 reversal 指定3,120 → 約定3,120・終値3,160（+1.28%）
- 8346 reversal 指定957 → 約定957・終値955（-0.21%）
- 8088 reversal 指定1,928 → 約定1,928・終値1,915.5（-0.65%）
- 8714 reversal 指定948 → 約定948・終値944（-0.42%）
- 8399 reversal 指定2,835 → 約定2,835・終値2,828（-0.25%）
- 8381 reversal 指定2,076 → 約定2,076・終値2,080（+0.19%）
- 8524 reversal 指定1,176 → 約定1,176・終値1,183（+0.60%）
- 1861 reversal 指定1,246 → 約定1,246・終値1,235（-0.88%）
- 1417 reversal 指定3,409 → 約定3,409・終値3,392（-0.50%）
- 1860 reversal 指定1,470.5 → 約定1,470.5・終値1,461（-0.65%）
- 2659 reversal 指定3,220 → 約定3,220・終値3,165（-1.71%）
- 5021 reversal 指定4,370 → 約定4,278・終値4,300（+0.51%）
- 1963 reversal 指定2,137.5 → 約定2,137.5・終値2,147.5（+0.47%）
- 1969 reversal 指定4,155 → 約定4,155・終値4,126（-0.70%）
- 9699 reversal 指定4,305 → 約定4,265・終値4,270（+0.12%）
- 9533 reversal 指定1,221.5 → 約定1,210.5・終値1,198（-1.03%）
- 8370 reversal 指定1,566 → 約定1,566・終値1,572（+0.38%）
- 5831 reversal 指定3,030 → 約定3,030・終値3,053（+0.76%）
- 7381 reversal 指定1,115 → 約定1,115・終値1,105（-0.90%）
- 8345 reversal 指定2,116 → 約定2,116・終値2,115（-0.05%）
- 8367 reversal 指定1,762 → 約定1,762・終値1,768（+0.34%）
- 7384 reversal 指定4,075 → 約定4,075・終値4,080（+0.12%）
- 8174 reversal 指定951.7 → 約定951.7・終値933.3（-1.93%）
- 8334 reversal 指定2,575 → 約定2,575・終値2,569.5（-0.21%）
- 8366 reversal 指定2,550 → 約定2,550・終値2,532（-0.71%）
- 7186 reversal 指定1,660 → 約定1,660・終値1,663（+0.18%）
- 7322 reversal 指定1,838 → 約定1,838・終値1,845（+0.38%）
- 8354 reversal 指定6,880 → 約定6,880・終値6,891（+0.16%）
- 8359 reversal 指定2,403 → 約定2,403・終値2,404（+0.04%）
- 8600 reversal 指定1,038 → 約定1,038・終値1,035（-0.29%）
- 4658 reversal 指定1,545 → 約定1,545・終値1,525（-1.29%）
- 5254 momentum 指定3,880 → 約定3,900・終値3,840（-1.54%）
- 9553 momentum 指定580 → 約定580・終値593（+2.24%）
- 7744 momentum 指定2,152 → 約定2,152・終値2,125（-1.25%）
- 4272 momentum 指定2,065 → 約定2,084.5・終値2,061.5（-1.10%）
- 8012 momentum 指定1,220 → 約定1,232・終値1,253（+1.70%）
- 4617 momentum 指定3,595 → 約定3,615・終値3,575（-1.11%）
- 6328 momentum 指定2,477 → 約定2,490・終値2,445（-1.81%）
- 5105 momentum 指定4,064 → 約定4,064・終値4,009（-1.35%）
- 4431 oshime 指定3,690.6 → 約定3,690.6・終値3,870（+4.86%）
- 8364 reversal 指定2,724 → 約定2,724・終値2,721（-0.11%）
- 3907 reversal 指定1,369 → 約定1,369・終値1,276（-6.79%）
- 8360 reversal 指定1,279 → 約定1,279・終値1,288（+0.70%）
- 7380 reversal 指定2,358 → 約定2,358・終値2,383（+1.06%）
- 8368 reversal 指定2,089 → 約定2,089・終値2,118（+1.39%）
- 8713 reversal 指定2,527 → 約定2,527・終値2,521（-0.24%）
- 8377 reversal 指定737.7 → 約定737.7・終値745.2（+1.02%）
- 8151 changepoint 指定1,924 → 約定1,924・終値1,912（-0.62%）
- 5590 changepoint 指定656 → 約定655・終値658（+0.46%）
- 6785 changepoint 指定3,240 → 約定3,240・終値3,250（+0.31%）
- 4478 changepoint 指定4,175 → 約定4,175・終値4,320（+3.47%）

## 模擬テンプレ
```
# base_day 2026-10-28 ／ 提案32件
# 使い方: 参戦する0〜3銘柄の行だけをコピーし、｜の後ろに参戦理由を書いてポジション株PJへ送る。
# 選ばなかった行は送らなくてよい（全行に理由を書く必要はない）。見送りは末尾の1行で足りる。
# 特定銘柄を理由つきで見送る場合のみ『模擬 見送り {code} ｜{理由}』を送る。
模擬 4377 kenmo_momentum 逆指値2509 SL2357.5 単元100 ｜
模擬 4058 kenmo_momentum 逆指値2313 SL2173.3 単元100 ｜
模擬 4477 kenmo_momentum 逆指値343 SL321.5 単元100 ｜
模擬 3077 kenmo_momentum 逆指値1176 SL1104.5 単元100 ｜
模擬 6278 choruko_reversal 指値13400 SL11660 単元100 ｜
模擬 6875 choruko_reversal 指値10210 SL9110 単元100 ｜
模擬 6645 choruko_reversal 指値5589 SL5094 単元100 ｜
模擬 6754 choruko_reversal 指値3029 SL2611 単元100 ｜
模擬 6055 choruko_reversal 指値2112 SL1854 単元100 ｜
模擬 5310 choruko_reversal 指値6810 SL5970 単元100 ｜
模擬 6521 ai_momentum 逆指値3585 SL3365.2 単元100 ｜
模擬 4062 ai_reversal 指値9663 SL7883 単元100 ｜
模擬 7729 ai_reversal 指値16325 SL14315 単元100 ｜
模擬 6752 ai_reversal 指値3787 SL3494 単元100 ｜
模擬 5706 ai_reversal 指値2152.5 SL1908.5 単元100 ｜
模擬 6590 ai_reversal 指値3400 SL2874 単元100 ｜
模擬 9553 granville_tenkan 逆指値594 SL557.4 単元100 ｜
模擬 8697 granville_tenkan 逆指値2123.5 SL1995.1 単元100 ｜
模擬 5838 granville_tenkan 逆指値5868 SL5506.5 単元100 ｜
模擬 6768 granville_tenkan 逆指値884 SL830 単元100 ｜
模擬 8012 granville_tenkan 逆指値1255 SL1178.8 単元100 ｜
模擬 4902 granville_tenkan 逆指値691.3 SL648.9 単元100 ｜
模擬 3563 granville_tenkan 逆指値5626 SL5279 単元100 ｜
模擬 4431 granville_oshime 指値3707.6 SL3689.2 単元100 ｜
模擬 3778 granville_rebound 指値3470 SL2711 単元100 ｜
模擬 3691 granville_rebound 指値1487 SL1395 単元100 ｜
模擬 7715 granville_rebound 指値3980 SL3585 単元100 ｜
模擬 7175 granville_rebound 指値1701 SL1613 単元100 ｜
模擬 7695 changepoint🔔 指値869 SL844 単元100 🔒 ｜
模擬 6136 changepoint 指値3535 SL3376 単元100 🔒 ｜
模擬 9962 changepoint 指値3882 SL3477 単元100 🔒 ｜
模擬 5582 changepoint🔔 指値1822 SL1758 単元100 🔒 ｜
模擬 見送り ｜
```

## PASS内訳
PASS 47件 = 発注可能 32件 + 除外 15件（型不一致5/材料後出し4/鮮度切れ5/その他1）
- 6668 ＡＤプラズマ｜⛔提案なし(手法ブランチ不明)
- 8944 Land Business Co., Ltd.｜⛔型不一致: 既にトリガー超（追いかけ禁止・教訓⑬）
- 4169 Enechange Ltd.｜⛔提案なし(材料後出し)
- 8927 Meiho Enterprise Co., Ltd.｜⛔提案なし(材料後出し)
- 6834 Seikoh Giken Co., Ltd.｜⛔型不一致: 既に支持帯以下
- 6523 PHC Holdings Corp.｜⛔型不一致: 既に支持帯以下
- 9166 GENDA Inc.｜⛔型不一致: 既に支持帯以下
- 336A ダイナミックマッププラットフォーム｜⛔型不一致: 既に支持帯以下
- 8704 トレイダーズホールディングス｜⛔提案なし(材料後出し)
- 4478 freee K.K.｜⛔提案なし(材料後出し)
- 鮮度切れ: 6298(nom_age 12)、3107(nom_age 16)、8624(nom_age 13)、1407(nom_age 21)、4488(nom_age 16)

## 5手法銘柄
- 6627 Tera Probe, Inc.｜kenmo_momentum｜🚀確変｜💎割安｜FAIL_INSEN｜1,924円｜💰17.5万円｜—｜📋カルテ窓 11/13(残11営業日)
- 5137 Smart Drive Co. Ltd.｜kenmo_momentum｜🚀確変｜💎割安｜FAIL_INSEN｜307円｜💰3.0万円｜—｜📋カルテ窓 11/13(残11営業日)
- 276A CCReB Advisors Inc.｜granville_oshime/kenmo_momentum｜🚀確変｜⚪妥当｜FAIL_INSEN｜4,500円｜💰46.0万円｜—｜⚠日程不明｜⚡材料後出し
- 6862 ミナトホールディングス｜kenmo_momentum/granville_rebound/granville_oshime｜🚀確変｜💎割安｜FAIL_INSEN｜3,850円｜💰44.0万円｜—｜📋カルテ窓 11/12(残10営業日)
- 3556 RenetJapanGroup, Inc.｜kenmo_momentum｜🚀確変｜🟢値頃｜FAIL_INSEN｜877円｜💰9.0万円｜—｜📋カルテ窓 11/13(残11営業日)
- 4053 Sun Asterisk, Inc.｜kenmo_momentum｜🚀確変｜⚪妥当｜FAIL_INSEN｜582円｜💰5.9万円｜—｜📋カルテ窓 11/13(残11営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 4434 Serverworks Co., Ltd.｜kenmo_momentum/stf_kakuhen｜🚀確変｜⚪妥当｜FAIL_INSEN｜2,898円｜💰30.4万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）
- 5027 AnyMind Group Inc.｜kenmo_momentum｜🚀確変｜⚪妥当｜FAIL_INSEN｜782円｜💰7.8万円｜—｜📋カルテ窓 11/13(残11営業日)
- 5136 tripla Co.,Ltd.｜kenmo_momentum/changepoint🔔🔔/granville_oshime｜🚀確変｜⚪妥当｜FAIL_UWAHIGE｜2,561円｜💰25.2万円｜—｜⚠日程不明
- 5757 CK San-Etsu Co., Ltd.｜kenmo_momentum｜🔥絶好調｜💎割安｜FAIL_INSEN｜4,480円｜💰45.0万円｜—｜📋カルテ窓 11/13(残11営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 9554 AViC Co. Ltd.｜kenmo_momentum/granville_tenkan｜🔥絶好調｜💎割安｜FAIL_INSEN｜1,563円｜💰15.5万円｜—｜📋カルテ窓 11/13(残11営業日)
- 212A FIT EASY Inc.｜kenmo_momentum/granville_oshime｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜2,735円｜💰27.7万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）
- 3915 TerraSky Co., Ltd.｜kenmo_momentum｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜2,417円｜💰23.9万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）｜📐進捗 上振れ 34.1%
- 421A Movin' Strategic Career CO.,LTD.｜kenmo_momentum/kenmo_newhigh｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜3,920円｜💰39.7万円｜—
- 5132 pluszero,Inc.｜kenmo_momentum｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜1,882円｜💰18.6万円｜—｜⚠日程不明
- 6298 Y.A.C.HOLDINGS CO.,LTD.｜kenmo_momentum｜🔥絶好調｜🟢値頃｜PASS｜1,158円｜💰11.6万円｜⛔提案なし(指名鮮度切れ 12営業日)｜📋カルテ窓 11/13(残11営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
  > 【業態】各種自動化機器中堅。メカトロ、ディスプレイ、半導体など関連機器主力。医療用も。
  > 【いま】終値1,158円・直近5日+1.49%（材料未確認）
  > 【調子】🔥絶好調（9/13） — E軸判定不能(進捗データ不足)
  > 【水準】🟢値頃（5.0/7）— PER10.18倍・PEG0.0699・52週42.1% ／ 💰単元11.6万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 12営業日)）
- 4377 ONE CAREER Inc.｜kenmo_momentum｜🔥絶好調｜⚪妥当｜PASS_DOJI｜2,476円｜💰24.8万円｜momentum 2,509（✅即時可）｜📋カルテ窓 11/12(残10営業日)｜📆FOMC明け
  > 【業態】採用支援サービスの提供。就活支援・新卒採用サービス「ワンキャリア」などを展開。
  > 【いま】終値2,476円・直近5日-5.93%（材料未確認）
  > 【調子】🔥絶好調（9/13） — E軸判定不能(進捗データ不足)
  > 【水準】⚪妥当（4.0/7）— PER21.22倍・PEG0.4659・52週68.8% ／ 💰単元24.8万円
  > 【戦略】当日高値超えの逆指値2,509円で順張り参戦を検討。上限2,534.1円・SL2,357.5円目安
- 5537 AlbaLink Co.,Ltd.｜kenmo_momentum/granville_oshime｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜3,395円｜💰34.6万円｜—｜📋カルテ窓 11/12(残10営業日)
- 7047 PORT INC.｜kenmo_momentum｜🔥絶好調｜💎割安｜FAIL_INSEN｜1,942円｜💰19.5万円｜—｜📋カルテ窓 11/16(残12営業日)
- 5821 Hirakawa Hewtech Corp.｜kenmo_momentum｜⚡好調｜💎割安｜FAIL_INSEN｜3,165円｜💰31.0万円｜—｜⏰決算 11/04(残4営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 4058 Toyokumo, Inc.｜kenmo_momentum｜⚡好調｜⚪妥当｜PASS｜2,299円｜💰23.0万円｜momentum 2,313（✅即時可）｜📋カルテ窓 11/13(残11営業日)｜📆FOMC明け
  > 【業態】安否確認サービスや法人向けクラウド事業。サイボウズ「キントーン」連携アプリ構築も展開。
  > 【いま】終値2,299円・直近5日-0.39%（材料未確認）
  > 【調子】⚡好調（7/13） — E軸判定不能(進捗データ不足)
  > 【水準】⚪妥当（4.0/7）— PER17.79倍・PEG0.5816・52週46.3% ／ 💰単元23.0万円
  > 【戦略】当日高値超えの逆指値2,313円で順張り参戦を検討。上限2,336.1円・SL2,173.3円目安
- 6071 IBJ, Inc.｜kenmo_momentum｜⚡好調｜⚪妥当｜FAIL_INSEN｜890円｜💰9.1万円｜—｜📋カルテ窓 11/13(残11営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 9560 PROGRIT, Inc.｜kenmo_momentum｜⚡好調｜⚪妥当｜FAIL_INSEN｜1,041円｜💰10.8万円｜—｜⚠日程不明｜⚡材料後出し
- 147A SORACOM,INC.｜kenmo_momentum｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜934円｜💰9.2万円｜—
- 5034 unerry, Inc.｜kenmo_momentum｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,601円｜💰27.4万円｜—｜📋カルテ窓 11/12(残10営業日)
- 7678 ASAKUMA CO.,LTD.｜kenmo_momentum/kenmo_newhigh｜⚡好調｜🔴過熱｜FAIL_UWAHIGE｜4,000円｜💰39.5万円｜—｜⚠日程不明｜🎯2手法一致
- 9268 OPTIMUS GROUP Co., Ltd.｜kenmo_momentum｜⚡好調｜💎割安｜FAIL_INSEN｜336円｜💰3.4万円｜—｜📋カルテ窓 11/13(残11営業日)
- 4477 BASE, Inc.｜kenmo_momentum/granville_oshime｜⚡好調｜⚪妥当｜PASS_DOJI｜340円｜💰3.4万円｜momentum 343（✅即時可）｜⚠日程不明｜📆FOMC明け
  > 【業態】個人・小規模企業向けECプラットフォーム「BASE」、オンライン決済サービス「PAY.JP」運営。
  > 【いま】終値340円・直近5日-12.14%（材料未確認）
  > 【調子】⚡好調（6/13）
  > 【水準】⚪妥当（3.0/7）— PER26.15倍・PEG1.1168・52週51.8% ／ 💰単元3.4万円
  > 【戦略】当日高値超えの逆指値343円で順張り参戦を検討。上限346.4円・SL321.5円目安
- 9628 San Holdings,Inc.｜kenmo_momentum｜⚡好調｜🟡やや割高｜FAIL_INSEN｜1,140円｜💰11.5万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）
- 2980 SRE Holdings Corp.｜kenmo_momentum｜⚡好調｜💎割安｜FAIL_INSEN｜2,200円｜💰21.9万円｜—｜📑TOPIX低減対象（次 10/30 第1回/8）
- 4412 Science Arts, Inc.｜kenmo_momentum｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜1,301円｜💰12.9万円｜—｜⚠日程不明
- 505A Geekly,Inc.｜kenmo_momentum｜✅順調｜💎割安｜FAIL_INSEN｜1,165円｜💰11.7万円｜—｜⚠日程不明
- 4743 ITFOR Inc.｜kenmo_momentum｜✅順調｜🟢値頃｜FAIL_INSEN｜1,605円｜💰16.4万円｜—｜📋カルテ窓 11/12(残10営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 5038 eWeLL Co.,Ltd｜kenmo_momentum｜✅順調｜⚪妥当｜FAIL_INSEN｜2,339円｜💰23.4万円｜—｜📋カルテ窓 11/13(残11営業日)
- 6629 TECHNO HORIZON Co., Ltd.｜granville_tenkan/kenmo_momentum｜✅順調｜⚪妥当｜FAIL_INSEN｜955円｜💰9.5万円｜—｜⏰決算 10/30(残2営業日)｜📐進捗 上振れ 14.4%
- 6289 Giken Ltd.｜granville_tenkan/kenmo_momentum｜⚠減速｜🟡やや割高｜FAIL_INSEN｜1,965円｜💰19.8万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）
- 3077 Horiifoodservice Co., Ltd.｜kenmo_momentum/granville_rebound｜判定保留(変則決算)｜🟢値頃｜PASS｜1,175円｜💰11.8万円｜momentum 1,176（✅即時可）｜⚠日程不明｜📆FOMC明け
  > 【業態】外食チェーン。北関東地盤に、個室型レストラン「忍家」など展開。シティクリエイションHD傘下。
  > 【いま】終値1,175円・直近5日+0.43%（材料未確認）
  > 【調子】—（判定保留(変則決算): 2025.11→予2026.11・四半期8本不足/欠損で4Q換算不可）
  > 【水準】🟢値頃（5.6/7）— PER12.93倍・PEG0.0557・52週68.4% ／ 💰単元11.8万円
  > 【戦略】当日高値超えの逆指値1,176円で順張り参戦を検討。上限1,187.8円・SL1,104.5円目安
- 618A KOMPEITO Inc.｜kenmo_momentum/kenmo_newhigh｜取得不可｜⚪妥当｜FAIL_UWAHIGE｜2,136円｜💰21.3万円｜—｜⚠日程不明｜🎯2手法一致
- 6918 Aval Data Corporation｜kenmo_newhigh/granville_rebound｜🚀確変｜🟢値頃｜FAIL_INSEN｜3,815円｜💰37.5万円｜—｜📋カルテ窓 11/12(残10営業日)
- 3374 Naigai Tec Corporation｜kenmo_newhigh/ai_momentum/granville_oshime｜🚀確変｜🟢値頃｜FAIL_UWAHIGE｜4,790円｜💰46.0万円｜—｜📋カルテ窓 11/13(残11営業日)
- 7567 Sakae Electronics Corp.｜kenmo_newhigh｜🚀確変｜⚪妥当｜FAIL_INSEN｜632円｜💰6.4万円｜—｜📋カルテ窓 11/12(残10営業日)
- 6337 Tesec Corporation｜kenmo_newhigh/granville_rebound｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜2,787円｜💰34.2万円｜—｜⚠日程不明｜📐進捗 上振れ 22.9%
- 446A ノースサンド｜kenmo_newhigh｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜2,920円｜💰28.6万円｜—｜⚠日程不明
- 3696 セレス｜kenmo_newhigh｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜2,203円｜💰22.5万円｜—｜📋カルテ窓 11/12(残10営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 2930 北の達人コーポレーション｜kenmo_newhigh｜⚡好調｜🔴過熱｜FAIL_UWAHIGE｜145円｜💰1.5万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）
- 4379 Photosynth inc.｜kenmo_newhigh｜⚡好調｜🔴過熱｜FAIL_INSEN｜516円｜💰5.2万円｜—｜📋カルテ窓 11/12(残10営業日)｜📐進捗 上振れ 18.7%
- 2820 Yamami Co.｜kenmo_newhigh｜✅順調｜🟡やや割高｜FAIL_INSEN｜6,520円｜💰67.3万円｜—
- 3843 Freebit Co., Ltd.｜kenmo_newhigh/granville_tenkan｜✅順調｜⚪妥当｜FAIL_INSEN｜1,745円｜💰17.5万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）｜⚡材料後出し
- 4331 Take and Give. Needs Co., Ltd.｜kenmo_newhigh｜✅順調｜🟡やや割高｜FAIL_INSEN｜810円｜💰8.2万円｜—｜📑TOPIX低減対象（次 10/30 第1回/8）
- 7161 Jimoto Holdings, Inc.｜kenmo_newhigh｜業績データ取得不可｜⚪妥当｜FAIL_INSEN｜569円｜💰5.6万円｜—｜📋カルテ窓 11/13(残11営業日)
- 4565 Nxera Pharma Co., Ltd.｜granville_oshime/kenmo_newhigh｜業績データ取得不可(経常益予想非開示)｜🟡やや割高｜FAIL_UWAHIGE｜1,403円｜💰13.6万円｜—｜⏰決算 10/30(残2営業日)｜⚡材料後出し
- 6278 ユニオンツール｜choruko_reversal｜🚀確変｜🟢値頃｜PASS｜13,400円｜💰134.0万円｜reversal 13,400（✅即時可）｜⚠1単元でリスク枠超過（174000円）｜📆FOMC明け
  > 【業態】プリント配線板用ドリル世界最大手。直動軸受け、測定器や生体センサも展開。
  > 【いま】終値13,400円・直近5日-0.59%（材料未確認）
  > 【調子】🚀確変（12/13）
  > 【水準】🟢値頃（5.0/7）— PER21.23倍・PEG0.1864・52週30.9% ／ 💰単元134.0万円
  > 【戦略】当日終値13,400円の指値で反転を取りにいく。SL11,660円（直近5日安値）／⚠1単元リスク174000円（枠超過）
- 6875 メガチップス｜choruko_reversal｜🔥絶好調｜💎割安｜PASS｜10,210円｜💰102.1万円｜reversal 10,210（✅即時可）｜📐進捗 上振れ 20.3%｜⚠1単元でリスク枠超過（110000円）｜📆権利月不明｜📆FOMC明け
  > 【業態】カスタムLSI、画像転送システムが主力。生産外部委託。任天堂向け中心。5G向けも。
  > 【いま】終値10,210円・直近5日+2.10%（材料未確認）
  > 【調子】🔥絶好調（10/13） — E軸判定不能(進捗データ不足)
  > 【水準】💎割安（6.0/7）— PER4.22倍・PEG0.0000・52週48.0% ／ 💰単元102.1万円
  > 【戦略】当日終値10,210円の指値で反転を取りにいく。SL9,110円（直近5日安値）／⚠1単元リスク110000円（枠超過）
- 8871 GOLDCREST Co., Ltd.｜choruko_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜2,810円｜💰28.7万円｜—｜📉決算反応日 10/28｜📑TOPIX低減対象（次 10/30 第1回/8）｜⚡材料後出し
- 3391 TSURUHA Holdings, Inc.｜choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜2,148.5円｜💰22.2万円｜—｜⚠日程不明
- 5344 MARUWA CO., LTD.｜choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜54,000円｜💰470.0万円｜—｜⚠日程不明
- 8336 武蔵野銀行｜granville_oshime/choruko_reversal/granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜2,580円｜💰25.6万円｜—
- 3036 アルコニックス｜choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜3,160円｜💰31.2万円｜—
- 6268 ナブテスコ｜choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜4,420円｜💰42.9万円｜—｜📋カルテ窓 11/13(残11営業日)
- 6324 Harmonic Drive Systems Inc.｜choruko_reversal｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜5,530円｜💰53.4万円｜—
- 6645 OMRON Corporation｜granville_rebound/choruko_reversal｜🔥絶好調｜⚪妥当｜PASS｜5,589円｜💰55.9万円｜reversal 5,589（✅即時可）｜⚠1単元でリスク枠超過（49500円）｜📆権利月不明｜📆FOMC明け
  > 【業態】制御機器大手。感知・リレー制御技術が得意。車載、鉄道システム、ヘルスケアも展開。
  > 【いま】終値5,589円・直近5日-1.83%（材料未確認）
  > 【調子】🔥絶好調（9/13） — 進捗モデル値域外
  > 【水準】⚪妥当（4.0/7）— PER27.13倍・PEG0.5397・52週53.4% ／ 💰単元55.9万円
  > 【戦略】当日終値5,589円の指値で反転を取りにいく。SL5,094円（直近5日安値）／⚠1単元リスク49500円（枠超過）
- 3222 United Super Markets Holdings, Inc.｜choruko_reversal｜🔥絶好調｜🔴過熱｜FAIL_INSEN｜753円｜💰7.7万円｜—｜⚠日程不明
- 1803 Shimizu Corporation｜choruko_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜2,076円｜💰20.9万円｜—
- 8346 東邦銀行｜granville_oshime/granville_rebound/choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜955円｜💰9.6万円｜—
- 4088 Air Water Inc.｜choruko_reversal｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜2,800円｜💰27.6万円｜—｜⚠日程不明｜⚡材料後出し
- 5301 Tokai Carbon Co., Ltd.｜choruko_reversal/granville_rebound｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜1,975.5円｜💰19.3万円｜—｜⏰決算 11/05(残5営業日)
- 7733 Olympus Corp.｜choruko_reversal｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜1,753円｜💰17.5万円｜—
- 7004 カナデビア｜choruko_reversal｜⚠減速｜💎割安｜FAIL_INSEN｜1,062円｜💰10.5万円｜—｜⏰決算 11/05(残5営業日)
- 8386 百十四銀行｜choruko_reversal/granville_rebound｜⚡好調｜💎割安｜FAIL_UWAHIGE｜2,804円｜💰27.4万円｜—
- 6370 栗田工業｜choruko_reversal｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜7,176円｜💰69.8万円｜—｜⏰決算 11/05(残5営業日)
- 8522 Bank of Nagoya, Ltd.｜choruko_reversal｜⚡好調｜🟢値頃｜FAIL_INSEN｜5,930円｜💰59.1万円｜—｜📋カルテ窓 11/13(残11営業日)
- 2874 YOKOREI CO. LTD.｜granville_rebound/choruko_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜1,767円｜💰18.3万円｜—｜📋カルテ窓 11/12(残10営業日)
- 6302 住友重機械工業｜granville_tenkan/choruko_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜5,529円｜💰54.7万円｜—｜⏰決算 10/30(残2営業日)
- 6754 アンリツ｜ai_reversal/choruko_reversal｜⚡好調｜⚪妥当｜PASS｜3,029円｜💰30.3万円｜reversal 3,029（✅即時可）｜🚨決算直前 10/29(残1営業日)｜⚠1単元でリスク枠超過（41800円）｜📆FOMC明け
  > 【業態】携帯・基地局向けなど計測機器大手。海外も高シェア。食品・医薬品検査機も。
  > 【いま】終値3,029円・直近5日+2.06%・📌（開示事項の経過）持分法適用関連会社の株式追加取得（連結子会社化）完了に関するお知らせ
  > 【調子】⚡好調（7/13） — E軸判定不能(進捗データ不足)
  > 【水準】⚪妥当（3.0/7）— PER25.84倍・PEG1.0831・52週40.0% ／ 💰単元30.3万円
  > 【戦略】当日終値3,029円の指値で反転を取りにいく。SL2,611円（直近5日安値）／⚠1単元リスク41800円（枠超過）
- 8987 Japan Excellent, Inc.｜choruko_reversal｜⚡好調｜🟢値頃｜FAIL_INSEN｜124,900円｜💰12.6万円｜—｜⚠日程不明
- 8282 K'S HOLDINGS CORPORATION｜choruko_reversal｜⚡好調｜🟢値頃｜FAIL_INSEN｜1,684.5円｜💰17.0万円｜—｜⏰決算 11/05(残5営業日)
- 6332 月島ホールディングス｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,368円｜💰23.7万円｜—｜📐進捗 上振れ 66.0%
- 8088 岩谷産業｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜1,915.5円｜💰19.3万円｜—｜⚡材料後出し
- 9412 SKY Perfect JSAT Corporation｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜1,897円｜💰18.6万円｜—｜⏰決算 11/04(残4営業日)
- 5333 ＮＧＫ｜choruko_reversal｜⚡好調｜🟡やや割高｜FAIL_UWAHIGE｜4,829円｜💰46.9万円｜—｜⏰決算 10/30(残2営業日)
- 8125 Wakita & Co., Ltd.｜choruko_reversal｜⚡好調｜🔴過熱｜FAIL_INSEN｜1,859円｜💰18.7万円｜—｜⚠日程不明
- 7721 Tokyo Keiki Inc.｜choruko_reversal｜⚡好調｜🟢値頃｜FAIL_INSEN｜5,720円｜💰55.8万円｜—
- 8278 Fuji Co., Ltd.｜choruko_reversal｜⚡好調｜🟢値頃｜FAIL_INSEN｜1,947円｜💰20.0万円｜—｜⚠日程不明
- 8714 池田泉州ホールディングス｜granville_oshime/choruko_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜944円｜💰9.5万円｜—｜📋カルテ窓 11/13(残11営業日)
- 8393 Miyazaki Bank Ltd.｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,419円｜💰24.1万円｜—
- 8399 琉球銀行｜choruko_reversal/granville_rebound｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,828円｜💰28.4万円｜—
- 268A Rigaku Holdings Corporation｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜1,555円｜💰14.8万円｜—
- 7458 Daiichikosho Co., Ltd.｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜1,718.5円｜💰17.5万円｜—
- 2782 Seria Co., Ltd.｜choruko_reversal｜⚡好調｜🔴過熱｜FAIL_INSEN｜4,345円｜💰44.0万円｜—｜⏰決算 10/30(残2営業日)｜📑TOPIX新規採用（10/30 組入）
- 2809 Kewpie Corporation｜choruko_reversal｜⚡好調｜🔴過熱｜FAIL_INSEN｜4,407円｜💰45.5万円｜—｜⚠日程不明
- 4666 Park24 Co., Ltd.｜choruko_reversal｜✅順調｜💎割安｜FAIL_INSEN｜1,785円｜💰18.3万円｜—｜⚠日程不明
- 7731 ニコン｜choruko_reversal｜✅順調｜🟢値頃｜FAIL_INSEN｜1,756円｜💰17.3万円｜—｜⏰決算 11/05(残5営業日)
- 3279 Activia Properties, Inc.｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜124,600円｜💰12.7万円｜—｜⚠日程不明
- 8381 San-in Godo Bank Ltd.｜choruko_reversal/granville_rebound｜✅順調｜⚪妥当｜FAIL_INSEN｜2,080円｜💰20.8万円｜—｜📋カルテ窓 11/12(残10営業日)
- 8524 North Pacific Bank, Ltd.｜granville_rebound/choruko_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜1,183円｜💰11.8万円｜—｜📋カルテ窓 11/13(残11営業日)
- 3282 Comforia Residential REIT, Inc.｜choruko_reversal｜✅順調｜🟡やや割高｜FAIL_INSEN｜89,100円｜💰9.0万円｜—｜⚠日程不明
- 8952 Japan Real Estate Investment Corp.｜choruko_reversal｜✅順調｜🟡やや割高｜FAIL_INSEN｜108,100円｜💰10.9万円｜—｜📋カルテ窓 11/16(残12営業日)
- 6925 Ushio Inc.｜choruko_reversal｜✅順調｜🟡やや割高｜FAIL_INSEN｜3,399円｜💰33.5万円｜—
- 1861 Kumagai Gumi Co., Ltd.｜choruko_reversal｜✅順調｜💎割安｜FAIL_INSEN｜1,235円｜💰12.5万円｜—｜📋カルテ窓 11/12(残10営業日)
- 1417 MIRAIT ONE Corporation｜choruko_reversal｜✅順調｜🟢値頃｜FAIL_INSEN｜3,392円｜💰34.1万円｜—
- 5331 ノリタケ｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜3,345円｜💰32.9万円｜—｜⏰決算 11/05(残5営業日)
- 3148 Create SD Holdings Co., Ltd.｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜3,135円｜💰32.2万円｜—｜⚠日程不明
- 8198 Maxvalu Tokai Co., Ltd.｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜3,060円｜💰31.2万円｜—｜⚠日程不明
- 9882 Yellow Hat Ltd.｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜1,591円｜💰16.1万円｜—｜⏰決算 10/30(残2営業日)
- 1820 Nishimatsu Construction Co., Ltd.｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜5,312円｜💰53.9万円｜—
- 1944 Kinden Corporation｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜6,369円｜💰63.9万円｜—｜⏰決算 10/30(残2営業日)
- 1952 Shin Nippon Air Technologies Co., Ltd.｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜3,040円｜💰30.2万円｜—｜📋カルテ窓 11/12(残10営業日)
- 6269 Modec, Inc.｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜8,115円｜💰81.2万円｜—
- 7003 Mitsui ES Holdings Co., Ltd.｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜3,609円｜💰35.9万円｜—
- 8584 Jaccs Co., Ltd.｜choruko_reversal｜🔻悪化｜⚪妥当｜FAIL_INSEN｜3,310円｜💰33.6万円｜—｜⏰決算 11/05(残5営業日)
- 1860 Toda Corporation｜choruko_reversal｜✅順調｜🟡やや割高｜FAIL_INSEN｜1,461円｜💰14.7万円｜—｜📋カルテ窓 11/13(残11営業日)
- 4966 上村工業｜choruko_reversal｜✅順調｜🟡やや割高｜FAIL_INSEN｜18,940円｜💰185.4万円｜—｜📑TOPIX新規採用（10/30 組入）｜📐進捗 上振れ 27.7%
- 8066 Mitani Corporation｜granville_rebound/choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜2,778円｜💰28.2万円｜—｜📋カルテ窓 11/12(残10営業日)
- 2659 SAN-A CO., LTD.｜choruko_reversal｜✅順調｜🔴過熱｜FAIL_INSEN｜3,165円｜💰32.2万円｜—｜⚠日程不明
- 5021 Cosmo Energy Holdings Co., Ltd.｜choruko_reversal｜🔻悪化｜🔴過熱｜FAIL_UWAHIGE｜4,300円｜💰43.7万円｜—
- 6055 Japan Material Co., Ltd.｜choruko_reversal｜✅順調｜🔴過熱｜PASS｜2,112円｜💰21.1万円｜reversal 2,112（✅即時可）｜📋カルテ窓 11/12(残10営業日)｜📆FOMC明け
  > 【業態】半導体製造向け特殊ガス供給装置製販。3D画像処理ツールや太陽光発電も。
  > 【いま】終値2,112円・直近5日+0.52%（材料未確認）
  > 【調子】✅順調（3/13） — E軸判定不能(進捗データ不足)、質注意
  > 【水準】🔴過熱（1.0/7）— PER20.10倍・PEG8.0610・52週48.2% ／ 💰単元21.1万円
  > 【戦略】当日終値2,112円の指値で反転を取りにいく。SL1,854円（直近5日安値）
- 7984 Kokuyo Co., Ltd.｜choruko_reversal｜✅順調｜🔴過熱｜FAIL_INSEN｜866.4円｜💰8.9万円｜—｜🚨決算直前 10/29(残1営業日)
- 2805 S&B Foods Inc.｜granville_rebound/choruko_reversal｜✅順調｜🔴過熱｜FAIL_INSEN｜6,710円｜💰68.3万円｜—｜⏰決算 10/30(残2営業日)｜📑TOPIX新規採用（10/30 組入）
- 3289 Tokyu Fudosan Holdings Corp.｜choruko_reversal｜➖横ばい｜💎割安｜FAIL_INSEN｜1,200円｜💰12.3万円｜—
- 8818 Keihanshin Building Co., Ltd.｜choruko_reversal｜➖横ばい｜⚪妥当｜FAIL_INSEN｜935円｜💰9.3万円｜—｜⏰決算 10/30(残2営業日)
- 1333 Umios Corporation｜choruko_reversal｜➖横ばい｜⚪妥当｜FAIL_INSEN｜1,195円｜💰12.2万円｜—｜⚠日程不明｜⚡材料後出し
- 1719 HAZAMA ANDO Corporation｜choruko_reversal｜➖横ばい｜⚪妥当｜FAIL_INSEN｜1,752.5円｜💰17.9万円｜—｜📋カルテ窓 11/12(残10営業日)
- 1833 Okumura Corporation｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜5,290円｜💰53.5万円｜—
- 6674 ジーエス・ユアサ　コーポレーション｜choruko_reversal｜➖横ばい｜⚪妥当｜FAIL_UWAHIGE｜4,805円｜💰47.2万円｜—
- 9503 Kansai Electric Power Company, Incorporated｜choruko_reversal/granville_rebound｜🔻悪化｜⚪妥当｜FAIL_INSEN｜2,708円｜💰27.4万円｜—｜🚨決算直前 10/29(残1営業日)
- 3445 RS Technologies Co. Ltd.｜choruko_reversal｜➖横ばい｜🟡やや割高｜FAIL_INSEN｜5,120円｜💰50.1万円｜—｜⚠日程不明
- 6366 Chiyoda Corp.｜choruko_reversal｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜611円｜💰6.1万円｜—｜⏰決算 11/04(残4営業日)｜📑TOPIX新規採用（10/30 組入）
- 7220 Musashi Seimitsu Industry Co., Ltd.｜choruko_reversal｜🔻悪化｜🟡やや割高｜FAIL_UWAHIGE｜2,542円｜💰24.2万円｜—
- 5844 Kyoto Financial Group,Inc.｜choruko_reversal｜🔻悪化｜🔴過熱｜FAIL_INSEN｜4,128円｜💰40.6万円｜—｜📋カルテ窓 11/13(残11営業日)
- 2379 dip Corporation｜choruko_reversal｜⚠減速｜💎割安｜FAIL_UWAHIGE｜1,512円｜💰15.1万円｜—｜⚠日程不明
- 6479 ミネベア｜choruko_reversal｜⚠減速｜💎割安｜FAIL_INSEN｜3,306円｜💰32.2万円｜—｜⚡材料後出し
- 1893 Penta-Ocean Construction Co., Ltd.｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_UWAHIGE｜1,400.5円｜💰13.8万円｜—
- 6183 BELLSYSTEM24 Holdings, Inc.｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜1,326円｜💰13.5万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）
- 6753 Sharp Corporation｜choruko_reversal｜🔻悪化｜⚪妥当｜FAIL_INSEN｜565.3円｜💰5.7万円｜—
- 8276 HEIWADO CO., LTD.｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜2,549円｜💰26.1万円｜—｜⚠日程不明
- 9974 BELC Co., Ltd.｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜6,290円｜💰63.7万円｜—｜⚠日程不明
- 3234 Mori Hills Reit Investment Corporation｜choruko_reversal｜⚠減速｜🔴過熱｜FAIL_INSEN｜117,000円｜💰11.9万円｜—｜⚠日程不明｜⚡材料後出し
- 3249 Industrial & Infrastructure Fund Investment Corporation｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜128,500円｜💰12.9万円｜—｜⚠日程不明
- 3283 Nippon Prologis REIT, Inc.｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜81,000円｜💰8.2万円｜—｜⚠日程不明
- 3292 AEON REIT Investment Corp.｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜105,100円｜💰10.6万円｜—｜⚠日程不明
- 3296 NIPPON REIT Investment Corp｜choruko_reversal｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜74,900円｜💰7.6万円｜—｜⚠日程不明
- 3309 Sekisui House Reit. Inc.｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜66,900円｜💰6.8万円｜—｜⚠日程不明
- 3462 Nomura Real Estate Master Fund, Inc.｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜127,800円｜💰12.9万円｜—｜⚠日程不明
- 5482 Aichi Steel Corporation｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜2,830円｜💰28.5万円｜—｜🚨決算直前 10/29(残1営業日)
- 8953 Japan Metropolitan Fund Investment Corporation｜choruko_reversal｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜105,800円｜💰10.7万円｜—｜⚠日程不明
- 8954 ORIX JREIT Inc.｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜87,400円｜💰8.9万円｜—｜⚠日程不明
- 8955 Japan Prime Realty Investment Corporation｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜92,500円｜💰9.3万円｜—｜⚠日程不明
- 8961 MORI TRUST REIT.Inc｜choruko_reversal｜⚠減速｜🔴過熱｜FAIL_INSEN｜66,700円｜💰6.7万円｜—｜⚠日程不明
- 8986 Daiwa Securities Living Investment Corporation｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜82,400円｜💰8.3万円｜—｜📋カルテ窓 11/19(残15営業日)
- 1946 Toenec Corporation｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_UWAHIGE｜2,180円｜💰21.1万円｜—｜🚨決算直前 10/29(残1営業日)
- 2815 ARIAKE JAPAN Co., Ltd.｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜5,100円｜💰52.4万円｜—
- 5631 Japan Steel Works, Ltd.｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜6,213円｜💰61.0万円｜—
- 9948 Arcs Company, Limited｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜3,420円｜💰35.1万円｜—｜⚠日程不明
- 1963 日揮ホールディングス｜choruko_reversal｜🔻悪化｜🔴過熱｜FAIL_UWAHIGE｜2,147.5円｜💰21.4万円｜—
- 3105 日清紡ホールディングス｜choruko_reversal｜🔻悪化｜🔴過熱｜FAIL_INSEN｜2,352.5円｜💰23.8万円｜—
- 4928 Noevir Holdings Co., Ltd.｜choruko_reversal｜⚠減速｜🔴過熱｜FAIL_INSEN｜4,530円｜💰46.7万円｜—
- 5310 Toyo Tanso Co., Ltd.｜choruko_reversal/ai_reversal｜🔻悪化｜🔴過熱｜PASS｜6,810円｜💰68.1万円｜reversal 6,810（✅即時可）｜⚠業績基調が下向き（🔻悪化）｜⚠1単元でリスク枠超過（84000円）｜📆FOMC明け
  > 【業態】等方性黒鉛で先駆、世界高シェア。半導体製造用るつぼが主力。一貫生産。
  > 【いま】終値6,810円・直近5日+0.44%（材料未確認）
  > 【調子】🔻悪化（1/13） — 質注意
  > 【水準】🔴過熱（1.0/7）— PER28.57倍・PEG—・52週51.6% ／ 💰単元68.1万円
  > 【戦略】当日終値6,810円の指値で反転を取りにいく。SL5,970円（直近5日安値）／⚠1単元リスク84000円（枠超過）
- 9436 Okinawa Cellular Telephone Company｜choruko_reversal｜⚠減速｜🔴過熱｜FAIL_INSEN｜3,345円｜💰33.4万円｜—｜🚨決算直前 10/29(残1営業日)｜📑TOPIX新規採用（10/30 組入）
- 6960 Fukuda Denshi Co., Ltd.｜choruko_reversal｜⚠減速｜🔴過熱｜FAIL_UWAHIGE｜11,070円｜💰110.2万円｜—｜⏰決算 10/30(残2営業日)｜📑TOPIX新規採用（10/30 組入）
- 1662 Japan Petroleum Exploration Co., Ltd.｜choruko_reversal｜🔻悪化｜⚪妥当｜FAIL_INSEN｜1,739円｜💰17.5万円｜—｜📋カルテ窓 11/12(残10営業日)
- 6804 Hosiden Corp.｜choruko_reversal｜🔻悪化｜⚪妥当｜FAIL_INSEN｜2,313円｜💰23.2万円｜—｜📋カルテ窓 11/13(残11営業日)
- 1969 高砂熱学工業｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜4,126円｜💰41.5万円｜—｜⚠日程不明
- 8585 Orient Corporation｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜752円｜💰7.5万円｜—｜⏰決算 10/30(残2営業日)
- 8194 Life Corporation｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜2,440円｜💰24.7万円｜—｜⚠日程不明
- 9699 NISHIO HOLDINGS CO. LTD.｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_UWAHIGE｜4,270円｜💰43.0万円｜—
- 9533 TOHO GAS Co., Ltd.｜choruko_reversal｜🔻悪化｜🔴過熱｜FAIL_INSEN｜1,198円｜💰12.2万円｜—｜🚨決算直前 10/29(残1営業日)
- 8253 Credit Saison Co., Ltd.｜choruko_reversal｜取得不可｜💎割安｜FAIL_INSEN｜4,109円｜💰41.4万円｜—｜📋カルテ窓 11/13(残11営業日)
- 8370 紀陽銀行｜choruko_reversal｜取得不可｜💎割安｜FAIL_INSEN｜1,572円｜💰15.7万円｜—
- 5831 Shizuoka Financial Group, Inc.｜choruko_reversal/granville_rebound｜取得不可｜🟢値頃｜FAIL_INSEN｜3,053円｜💰30.3万円｜—
- 7201 Nissan Motor Co., Ltd.｜choruko_reversal｜業績データ取得不可(経常益予想非開示)｜🟢値頃｜FAIL_INSEN｜262.4円｜💰2.6万円｜—
- 7381 ＣＣＩグループ｜choruko_reversal/granville_rebound｜取得不可｜🟢値頃｜FAIL_INSEN｜1,105円｜💰11.2万円｜—｜⏰決算 10/30(残2営業日)
- 8304 あおぞら銀行｜choruko_reversal｜取得不可｜🟢値頃｜FAIL_INSEN｜2,992円｜💰30.1万円｜—
- 8345 Bank of Iwate Ltd.｜choruko_reversal｜業績データ取得不可(売上/経常欠損)｜🟢値頃｜FAIL_INSEN｜2,115円｜💰21.2万円｜—｜📋カルテ窓 11/12(残10営業日)
- 8367 南都銀行｜granville_oshime/choruko_reversal｜取得不可｜🟢値頃｜FAIL_INSEN｜1,768円｜💰17.6万円｜—
- 3471 Mitsui Fudosan Logistics Park, Inc.｜choruko_reversal｜判定保留(変則決算)｜⚪妥当｜FAIL_INSEN｜98,200円｜💰9.9万円｜—｜⚠日程不明
- 7384 Procrea Holdings,Inc.｜granville_rebound/choruko_reversal｜業績データ取得不可(売上/経常欠損)｜⚪妥当｜FAIL_INSEN｜4,080円｜💰40.8万円｜—｜⚠日程不明
- 8174 NIPPON GAS Co., Ltd.｜choruko_reversal｜業績データ取得不可｜⚪妥当｜FAIL_INSEN｜933.3円｜💰9.5万円｜—｜🚨決算直前 10/29(残1営業日)
- 8334 Gunma Bank, Ltd.｜granville_rebound/choruko_reversal｜取得不可｜⚪妥当｜FAIL_INSEN｜2,569.5円｜💰25.8万円｜—
- 8366 滋賀銀行｜granville_rebound/choruko_reversal｜取得不可｜⚪妥当｜FAIL_INSEN｜2,532円｜💰25.5万円｜—｜📋カルテ窓 11/13(残11営業日)
- 3591 WACOAL HOLDINGS CORP｜choruko_reversal｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜3,540円｜💰36.3万円｜—｜📋カルテ窓 11/12(残10営業日)
- 8511 Japan Securities Finance Co., Ltd.｜choruko_reversal｜取得不可｜🟡やや割高｜FAIL_INSEN｜2,105円｜💰21.0万円｜—｜📋カルテ窓 11/12(残10営業日)
- 6471 日本精工｜choruko_reversal｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜1,024.5円｜💰10.1万円｜—｜🚨決算直前 10/29(残1営業日)
- 7186 横浜フィナンシャルグループ｜choruko_reversal｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜1,663円｜💰16.6万円｜—
- 7322 三十三フィナンシャルグループ｜choruko_reversal/granville_rebound｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜1,845円｜💰18.4万円｜—｜📋カルテ窓 11/13(残11営業日)
- 8354 ふくおかフィナンシャルグループ｜choruko_reversal｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜6,891円｜💰68.8万円｜—
- 8359 Hachijuni Nagano Bank, Ltd.｜choruko_reversal/granville_rebound｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜2,404円｜💰24.0万円｜—
- 8600 トモニホールディングス｜choruko_reversal｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜1,035円｜💰10.4万円｜—｜📋カルテ窓 11/13(残11営業日)
- 7624 NaITO｜stf_kakuhen｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜163円｜💰1.6万円｜—｜⚠日程不明
- 7713 シグマ光機｜stf_kakuhen｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜3,360円｜💰32.1万円｜—｜⚠日程不明
- 5018 ＭＯＲＥＳＣＯ｜stf_kakuhen｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜2,883円｜💰28.9万円｜—｜⚠日程不明
- 5246 ＥＬＥＭＥＮＴＳ｜granville_oshime/stf_kakuhen｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜1,071円｜💰11.0万円｜—｜⚠日程不明
- 6668 ＡＤプラズマ｜stf_kakuhen/granville_oshime｜🔥絶好調｜⚪妥当｜PASS｜5,280円｜💰52.8万円｜⛔提案なし(手法ブランチ不明)｜⚠日程不明
  > 【業態】高周波プラズマ電源装置最大手。液晶、半導体装置向け主力。技術に強み。
  > 【いま】終値5,280円・直近5日+3.94%（材料未確認）
  > 【調子】🔥絶好調（10/13） — E軸判定不能(進捗データ不足)
  > 【水準】⚪妥当（4.0/7）— PER12.18倍・PEG0.1843・52週83.9% ／ 💰単元52.8万円
  > 【戦略】発注対象外（⛔提案なし(手法ブランチ不明)）
- 3498 霞ヶ関Ｃ｜stf_kakuhen｜🔥絶好調｜💎割安｜FAIL_INSEN｜7,180円｜💰71.8万円｜—｜⚠日程不明
- 3994 マネーフォワード｜stf_kakuhen｜🔥絶好調｜🔴過熱｜FAIL_UWAHIGE｜6,723円｜💰66.9万円｜—｜⚠日程不明
- 7811 中本パックス｜granville_oshime/stf_kakuhen｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜2,476円｜💰25.3万円｜—｜⚠日程不明｜📐進捗 上振れ 21.8%
- 4443 Ｓａｎｓａｎ｜stf_kakuhen/changepoint🔔🔔｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜2,184円｜💰21.7万円｜—｜⚠日程不明
- 6814 古野電｜stf_kakuhen｜⚡好調｜🟢値頃｜FAIL_INSEN｜7,730円｜💰79.1万円｜—｜⚠日程不明
- 5932 三協立山｜stf_kakuhen｜⚡好調｜⚪妥当｜FAIL_INSEN｜735円｜💰7.4万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）
- 3091 ブロンコビリー｜changepoint/changepoint🔔🔔/stf_kakuhen｜⚡好調｜🟡やや割高｜FAIL_INSEN｜3,080円｜💰31.2万円｜—｜⚠日程不明
- 3479 ＴＫＰ｜stf_kakuhen/granville_tenkan｜⚡好調｜🔴過熱｜FAIL_INSEN｜1,935円｜💰19.5万円｜—｜⚠日程不明
- 6505 東洋電機製造｜ai_momentum/stf_kakuhen｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,968円｜💰30.2万円｜—｜⚠日程不明
- 6532 ベイカレント｜stf_kakuhen｜⚡好調｜🟡やや割高｜FAIL_INSEN｜11,330円｜💰116.2万円｜—｜⚠日程不明
- 4176 ココナラ｜stf_kakuhen｜✅順調｜🟢値頃｜FAIL_INSEN｜305円｜💰3.0万円｜—｜⚠日程不明

## グランビル銘柄
- 5254 Arent, Inc.｜granville_tenkan｜🚀確変｜⚪妥当｜FAIL_INSEN｜3,840円｜💰38.7万円｜—｜📋カルテ窓 11/12(残10営業日)
- 3927 アークン｜granville_tenkan｜🚀確変｜⚪妥当｜FAIL_INSEN｜1,002円｜💰10.6万円｜—｜📋カルテ窓 11/13(残11営業日)
- 8944 Land Business Co., Ltd.｜granville_tenkan｜🔥絶好調｜💎割安｜PASS｜252円｜💰2.5万円｜⛔型不一致: 既にトリガー超（追いかけ禁止・教訓⑬）｜📋カルテ窓 11/13(残11営業日)
  > 【業態】都内中心にマンション、ビルを賃貸、管理。自社開発も。カフェ・レストラン、服飾に進出。
  > 【いま】終値252円・直近5日-0.79%（材料未確認）
  > 【調子】🔥絶好調（10/13） — E軸判定不能(進捗データ不足)、D軸判定不能(四半期データ不足・中立1点)
  > 【水準】💎割安（6.0/7）— PER9.69倍・PEG0.0054・52週22.6% ／ 💰単元2.5万円
  > 【戦略】発注対象外（⛔型不一致: 既にトリガー超（追いかけ禁止・教訓⑬））
- 6905 Cosel Co., Ltd.｜granville_tenkan｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1,311円｜💰12.9万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）
- 9553 MicroAd, Inc.｜granville_tenkan｜🔥絶好調｜🟢値頃｜PASS｜593円｜💰5.9万円｜momentum 594（✅即時可）｜📋カルテ窓 11/13(残11営業日)｜📆FOMC明け
  > 【業態】データとテクノロジー活用でマーケティングプラットフォーム事業。広告コンサル、サイネージ配信も。
  > 【いま】終値593円・直近5日+0.17%（材料未確認）
  > 【調子】🔥絶好調（10/13） — 上方修正済み、進捗81%(前年同期87%・3Q累計・経常ベース)
  > 【水準】🟢値頃（5.0/7）— PER23.16倍・PEG0.2922・52週32.7% ／ 💰単元5.9万円
  > 【戦略】当日高値超えの逆指値594円で順張り参戦を検討。上限599.9円・SL557.4円目安
- 7725 INTER ACTION Corporation｜granville_tenkan｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜1,883円｜💰17.9万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）｜⚡材料後出し
- 2986 LA Holdings Co.,Ltd｜granville_tenkan｜🔥絶好調｜💎割安｜FAIL_INSEN｜2,684円｜💰26.9万円｜—｜📋カルテ窓 11/12(残10営業日)
- 9211 f-code Inc.｜granville_tenkan/changepoint🔔｜🔥絶好調｜💎割安｜FAIL_INSEN｜1,182円｜💰11.8万円｜—｜📋カルテ窓 11/13(残11営業日)
- 6562 Geniee, Inc.｜granville_tenkan｜🔥絶好調｜💎割安｜FAIL_INSEN｜911円｜💰9.1万円｜—｜📋カルテ窓 11/13(残11営業日)
- 6473 JTEKT Corporation｜granville_tenkan｜⚠減速｜🟢値頃｜FAIL_INSEN｜2,083.5円｜💰20.5万円｜—｜🚨決算直前 10/29(残1営業日)
- 8697 日本取引所グループ｜granville_tenkan/changepoint🔔/changepoint｜🔥絶好調｜⚪妥当｜PASS_DOJI｜2,084.5円｜💰20.8万円｜momentum 2,123.5（✅即時可）｜⚠日程不明｜📐進捗 上振れ 24.0%｜📆FOMC明け
  > 【業態】総合取引所。現物は東証、デリバティブは大証に集約。東京商品取引所統合。
  > 【いま】終値2,084.5円・直近5日-6.31%（材料未確認）
  > 【調子】🔥絶好調（8/13） — E軸:進捗54.6%>=前年同期44.0%
  > 【水準】⚪妥当（4.0/7）— PER20.22倍・PEG0.5972・52週63.6% ／ 💰単元20.8万円
  > 【戦略】当日高値超えの逆指値2,123.5円で順張り参戦を検討。上限2,144.7円・SL1,995.1円目安
- 3496 アズーム｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_INSEN｜4,650円｜💰48.0万円｜—｜📋カルテ窓 11/12(残10営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 4534 Mochida Pharmaceutical Co., Ltd.｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_INSEN｜3,230円｜💰32.5万円｜—｜📐進捗 上振れ 24.5%
- 6255 NPC Incorporated｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜696円｜💰6.5万円｜—｜⚠日程不明
- 8793 ＮＥＣキャピタルソリューション｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_INSEN｜4,030円｜💰40.8万円｜—｜⏰決算 10/30(残2営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 3405 クラレ｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜1,845円｜💰18.5万円｜—
- 7744 Noritsu Koki Co., Ltd.｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,125円｜💰21.5万円｜—｜📋カルテ窓 11/13(残11営業日)
- 8095 Astena Holdings Co.,Ltd.｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜531円｜💰5.3万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）｜⚡材料後出し
- 9064 ヤマトホールディングス｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜1,968円｜💰20.1万円｜—｜⏰決算 11/04(残4営業日)
- 3741 Systems Engineering Consultants Co., Ltd.｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜3,065円｜💰30.5万円｜—｜📋カルテ窓 11/12(残10営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 4544 H.U.Group Holdings, Inc.｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜3,770円｜💰38.0万円｜—
- 7970 Shin-Etsu Polymer Co., Ltd.｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,522円｜💰25.1万円｜—｜⚠日程不明
- 5838 Rakuten Bank, Ltd.｜granville_tenkan｜⚡好調｜💎割安｜PASS｜5,858円｜💰58.6万円｜momentum 5,868（✅即時可）｜⚠1単元でリスク枠超過（36150円）｜📆FOMC明け
  > 【業態】楽天グループ。日本最大級のネット銀行。子会社に楽天信託。
  > 【いま】終値5,858円・直近5日-5.27%（材料未確認）
  > 【調子】⚡好調（6/13） — 進捗率は経常累計÷通期予想で自前算出
  > 【水準】💎割安（7.0/7）— PER11.60倍・PEG0.5270・52週30.5% ／ 💰単元58.6万円
  > 【戦略】当日高値超えの逆指値5,868円で順張り参戦を検討。上限5,926.7円・SL5,506.5円目安／⚠1単元リスク36150円（枠超過）
- 6470 Taiho Kogyo Co., Ltd.｜granville_tenkan｜⚡好調｜💎割安｜FAIL_INSEN｜1,082円｜💰11.0万円｜—｜📉決算反応日 10/28｜📑TOPIX低減対象（次 10/30 第1回/8）｜⚡材料後出し
- 4763 クリーク・アンド・リバー社｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_INSEN｜1,446円｜💰14.6万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）
- 7199 プレミアグループ｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,092円｜💰21.2万円｜—
- 4848 フルキャストホールディングス｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜1,810円｜💰18.5万円｜—｜📑TOPIX低減対象（次 10/30 第1回/8）
- 3935 Edia Co. Ltd.｜granville_tenkan｜⚡好調｜💎割安｜FAIL_INSEN｜704円｜💰7.0万円｜—｜⚠日程不明
- 6196 Strike Group Co. Ltd.｜granville_tenkan｜⚡好調｜💎割安｜FAIL_INSEN｜1,388円｜💰14.0万円｜—｜⏰決算 10/30(残2営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 6768 Tamura Corporation｜granville_tenkan/granville_oshime｜⚡好調｜🟢値頃｜PASS｜878円｜💰8.8万円｜momentum 884（✅即時可）｜📆FOMC明け
  > 【業態】弱電用トランス、リアクター大手。ハンダ、絶縁膜や音声・ワイヤレス機器も。海外生産メイン。
  > 【いま】終値878円・直近5日+0.80%（材料未確認）
  > 【調子】⚡好調（5/13） — E軸判定不能(進捗データ不足)、D軸判定不能(四半期データ不足・中立1点)
  > 【水準】🟢値頃（5.6/7）— PER13.45倍・PEG0.7123・52週58.7% ／ 💰単元8.8万円
  > 【戦略】当日高値超えの逆指値884円で順張り参戦を検討。上限892.8円・SL830円目安
- 3562 No.1 Co., Ltd.｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_INSEN｜1,604円｜💰16.7万円｜—｜⚠日程不明｜⚡材料後出し
- 8061 Seika Corporation｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_INSEN｜3,000円｜💰29.8万円｜—
- 2331 ALSOK CO., LTD.｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜1,190円｜💰12.2万円｜—
- 4169 Enechange Ltd.｜granville_tenkan｜⚡好調｜⚪妥当｜PASS｜268円｜💰2.7万円｜⛔提案なし(材料後出し)｜⚡材料後出し｜📐進捗 遅れ -85.0%
  > 【業態】電力・ガスの切り替え行うプラットホーム「エネチェンジ」提供。電力事業のDX支援も。
  > 【いま】終値268円・直近5日-1.47%・👥主要株主の異動に関するお知らせ
  > 【調子】⚡好調（5/13） — 赤字→黒字転換
  > 【水準】⚪妥当（4.0/7）— PER19.28倍・PEG0.0409・52週46.7% ／ 💰単元2.7万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 4568 第一三共｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,580円｜💰25.9万円｜—｜⏰決算 10/30(残2営業日)｜📐進捗 遅れ -18.0%
- 3661 m-up holdings, Inc.｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜887円｜💰8.9万円｜—｜📋カルテ窓 11/13(残11営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 6432 竹内製作所｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜7,670円｜💰77.8万円｜—｜⚠日程不明
- 6988 日東電工｜granville_tenkan｜⚡好調｜🟡やや割高｜FAIL_INSEN｜3,388円｜💰36.0万円｜—｜⚠日程不明
- 7747 朝日インテック｜granville_tenkan｜⚡好調｜🟡やや割高｜FAIL_INSEN｜3,572円｜💰36.8万円｜—｜📋カルテ窓 11/13(残11営業日)
- 8020 Kanematsu Corporation｜granville_tenkan｜⚡好調｜🟡やや割高｜FAIL_INSEN｜2,366.5円｜💰23.8万円｜—｜⏰決算 11/05(残5営業日)
- 9828 Genki Global Dining Concepts Corp｜granville_tenkan｜⚡好調｜🔴過熱｜FAIL_INSEN｜3,360円｜💰35.3万円｜—｜⏰決算 10/30(残2営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 6454 Max Co., Ltd.｜granville_tenkan｜⚡好調｜🔴過熱｜FAIL_INSEN｜1,925円｜💰19.6万円｜—｜🚨決算直前 10/29(残1営業日)
- 2288 Marudai Food Co., Ltd.｜granville_tenkan｜✅順調｜🟢値頃｜FAIL_INSEN｜2,036円｜💰22.0万円｜—｜📑TOPIX低減対象（次 10/30 第1回/8）
- 5036 Japan Business Systems, Inc.｜granville_tenkan｜✅順調｜⚪妥当｜FAIL_UWAHIGE｜1,881円｜💰19.0万円｜—｜📋カルテ窓 11/12(残10営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 8014 Chori Co., Ltd.｜granville_tenkan｜✅順調｜⚪妥当｜FAIL_INSEN｜4,270円｜💰42.9万円｜—｜⏰決算 10/30(残2営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 3549 クスリのアオキホールディングス｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_INSEN｜4,221円｜💰42.5万円｜—｜⚠日程不明
- 4549 Eiken Chemical Co., Ltd.｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_INSEN｜2,377円｜💰24.2万円｜—｜🚨決算直前 10/29(残1営業日)
- 5184 ニチリン｜granville_tenkan｜✅順調｜🔴過熱｜FAIL_INSEN｜4,160円｜💰41.8万円｜—｜📐進捗 上振れ 23.8%
- 6371 Tsubakimoto Chain Co.｜granville_tenkan｜✅順調｜🔴過熱｜FAIL_INSEN｜2,704円｜💰27.1万円｜—｜⏰決算 10/30(残2営業日)
- 6592 Mabuchi Motor Co., Ltd.｜granville_tenkan｜✅順調｜🔴過熱｜FAIL_INSEN｜1,742円｜💰17.5万円｜—｜⚠日程不明
- 4166 Cacco, Inc.｜granville_tenkan｜✅順調｜🟢値頃｜FAIL_INSEN｜726円｜💰8.0万円｜—｜📋カルテ窓 11/13(残11営業日)
- 8850 スターツコーポレーション｜granville_tenkan｜✅順調｜⚪妥当｜FAIL_INSEN｜4,475円｜💰46.5万円｜—
- 9163 Nareru Group Inc.｜granville_tenkan｜✅順調｜⚪妥当｜FAIL_INSEN｜2,326円｜💰23.4万円｜—｜⚠日程不明
- 8927 Meiho Enterprise Co., Ltd.｜granville_tenkan｜✅順調｜⚪妥当｜PASS｜481円｜💰4.8万円｜⛔提案なし(材料後出し)｜⚠日程不明｜⚡材料後出し
  > 【業態】首都圏中心に賃貸アパート開発。マンション開発は休止。仲介や管理、中古再生も。
  > 【いま】終値481円・直近5日+0.00%・📌株式会社フィスコによる企業調査レポート公開に関するお知らせ
  > 【調子】✅順調（3/13） — E軸判定不能(進捗データ不足)、質注意
  > 【水準】⚪妥当（3.0/7）— PER5.26倍・PEG11.0144・52週65.5% ／ 💰単元4.8万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 186A Astroscale Holdings Inc.｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_INSEN｜1,125円｜💰10.8万円｜—｜⚠日程不明｜📑TOPIX新規採用（10/30 組入）
- 3569 セーレン｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_INSEN｜3,375円｜💰34.0万円｜—
- 4183 Mitsui Chemicals, Inc.｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_INSEN｜2,114円｜💰20.9万円｜—
- 4272 Nippon Kayaku Co., Ltd.｜granville_tenkan/granville_oshime｜✅順調｜🟡やや割高｜FAIL_INSEN｜2,061.5円｜💰20.6万円｜—
- 4956 Konishi Co., Ltd.｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_INSEN｜1,475円｜💰15.2万円｜—｜📉決算反応日 10/28｜⚡材料後出し
- 7181 JAPAN POST INSURANCE Co., Ltd.｜granville_tenkan｜⚠減速｜🔴過熱｜FAIL_INSEN｜1,714円｜💰17.3万円｜—｜📋カルテ窓 11/13(残11営業日)
- 7269 スズキ｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_INSEN｜2,089円｜💰20.4万円｜—
- 5461 Chubu Steel Plate Co., Ltd.｜granville_tenkan｜🔻悪化｜🔴過熱｜FAIL_INSEN｜2,212円｜💰22.0万円｜—｜📑TOPIX低減対象（次 10/30 第1回/8）
- 7513 Kojima Co., Ltd.｜granville_tenkan｜✅順調｜🔴過熱｜FAIL_INSEN｜1,342円｜💰13.8万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）
- 7734 Riken Keiki Co., Ltd.｜granville_tenkan｜✅順調｜🔴過熱｜FAIL_INSEN｜3,515円｜💰34.6万円｜—｜📋カルテ窓 11/12(残10営業日)
- 8012 Nagase & Co., Ltd.｜granville_tenkan｜✅順調｜🔴過熱｜PASS｜1,253円｜💰12.5万円｜momentum 1,255（✅即時可）｜📐進捗 上振れ 53.3%｜📆FOMC明け
  > 【業態】染料、合成樹脂化学の専門商社最大手。医薬品原料に強み。海外を拡大。
  > 【いま】終値1,253円・直近5日+5.03%（材料未確認）
  > 【調子】✅順調（3/13）
  > 【水準】🔴過熱（1.0/7）— PER14.72倍・PEG7.1821・52週88.8% ／ 💰単元12.5万円
  > 【戦略】当日高値超えの逆指値1,255円で順張り参戦を検討。上限1,267.5円・SL1,178.8円目安
- 4617 中国塗料｜granville_tenkan｜➖横ばい｜⚪妥当｜FAIL_INSEN｜3,575円｜💰35.5万円｜—｜⏰決算 10/30(残2営業日)
- 5233 太平洋セメント｜granville_tenkan｜➖横ばい｜⚪妥当｜FAIL_INSEN｜4,124円｜💰41.8万円｜—｜📐進捗 上振れ 32.1%
- 6328 Ebara Jitsugyo Co., Ltd.｜granville_tenkan｜➖横ばい｜⚪妥当｜FAIL_INSEN｜2,445円｜💰24.7万円｜—｜⏰決算 11/05(残5営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 4552 JCR Pharmaceuticals Co., Ltd.｜granville_tenkan｜🔻悪化｜🔴過熱｜FAIL_UWAHIGE｜512円｜💰5.1万円｜—｜🚨決算直前 10/29(残1営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 6208 Ishikawa Seisakusho,Ltd.｜granville_tenkan｜🔻悪化｜🟡やや割高｜FAIL_UWAHIGE｜1,681円｜💰16.6万円｜—
- 8081 Kanaden Corporation｜granville_tenkan｜➖横ばい｜🟡やや割高｜FAIL_INSEN｜2,545円｜💰26.0万円｜—｜⏰決算 11/04(残4営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 9837 Morito Co., Ltd.｜granville_tenkan｜➖横ばい｜🟡やや割高｜FAIL_INSEN｜1,788円｜💰18.1万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）
- 7751 キヤノン｜granville_tenkan｜➖横ばい｜🔴過熱｜FAIL_INSEN｜4,610円｜💰49.0万円｜—｜⚠日程不明｜📐進捗 上振れ 13.9%
- 6770 Alps Alpine Co., Ltd.｜granville_tenkan｜⚠減速｜⚪妥当｜FAIL_INSEN｜2,077.5円｜💰20.8万円｜—｜⏰決算 10/30(残2営業日)
- 5105 ＴＯＹＯ　ＴＩＲＥ｜granville_tenkan｜⚠減速｜🟡やや割高｜FAIL_INSEN｜4,009円｜💰40.6万円｜—｜📋カルテ窓 11/16(残12営業日)
- 8167 リテールパートナーズ｜granville_tenkan｜⚠減速｜🟡やや割高｜FAIL_INSEN｜1,347円｜💰14.0万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）｜📐進捗 遅れ -18.2%
- 4902 Konica Minolta, Inc.｜granville_tenkan｜⚠減速｜🔴過熱｜PASS｜688.1円｜💰6.9万円｜momentum 691.3（✅即時可）｜⏰決算 11/05(残5営業日)｜⚠業績基調が下向き（⚠減速）｜📆FOMC明け
  > 【業態】複合機中堅で印刷関連を展開。液晶TACフィルムで世界高シェア。X線撮影装置も。
  > 【いま】終値688.1円・直近5日+2.40%（材料未確認）
  > 【調子】⚠減速（1/13） — 質注意、経常非開示(IFRS等)のため最終益成長率で代替、E軸判定不能(進捗データ不足)、経常減益-5.8%
  > 【水準】🔴過熱（1.8/7）— PER11.95倍・PEG—・52週81.1% ／ 💰単元6.9万円
  > 【戦略】当日高値超えの逆指値691.3円で順張り参戦を検討。上限698.2円・SL648.9円目安
- 1815 鉄建建設｜granville_tenkan｜⚠減速｜⚪妥当｜FAIL_INSEN｜2,122円｜💰21.8万円｜—｜📋カルテ窓 11/13(残11営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 4375 セーフィー｜granville_tenkan/changepoint🔔｜取得不可｜💎割安｜FAIL_INSEN｜654円｜💰6.6万円｜—｜⚠日程不明
- 8424 芙蓉総合リース｜granville_tenkan｜取得不可｜💎割安｜FAIL_INSEN｜4,237円｜💰43.2万円｜—
- 7921 ＴＡＫＡＲＡ　＆　ＣＯＭＰＡＮＹ｜granville_tenkan｜業績データ取得不可(経常益予想非開示)｜🟢値頃｜FAIL_INSEN｜4,065円｜💰41.7万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）
- 4912 ライオン｜granville_tenkan｜業績データ取得不可(経常益予想非開示)｜⚪妥当｜FAIL_INSEN｜1,788円｜💰18.3万円｜—
- 2871 ニチレイ｜granville_tenkan｜業績データ取得不可｜🔴過熱｜FAIL_INSEN｜2,114.5円｜💰21.9万円｜—
- 3563 ＦＯＯＤ　＆　ＬＩＦＥ　ＣＯＭＰＡＮＩＥＳ｜granville_tenkan｜判定保留(データ不足)｜🔴過熱｜PASS_DOJI｜5,486円｜💰54.9万円｜momentum 5,626（✅即時可）｜⚠1単元でリスク枠超過（34700円）｜📆FOMC明け
  > 【業態】「スシロー」ブランドで回転すしチェーン首位。「京樽」を子会社化。韓国・アジアに進出。
  > 【いま】終値5,486円・直近5日-7.49%（材料未確認）
  > 【調子】—（売上/経常データ不足）
  > 【水準】🔴過熱（0.0/7）— PER39.58倍・PEG—・52週78.5% ／ 💰単元54.9万円
  > 【戦略】当日高値超えの逆指値5,626円で順張り参戦を検討。上限5,682.3円・SL5,279円目安／⚠1単元リスク34700円（枠超過）
- 4401 ＡＤＥＫＡ｜granville_tenkan｜業績—｜—｜FAIL_INSEN｜4,659円｜💰—｜—
- 5532 リアルゲイト｜granville_tenkan｜業績—｜—｜FAIL_UWAHIGE｜3,495円｜💰—｜—｜⚠日程不明
- 9842 アークランズ｜granville_tenkan｜業績—｜—｜FAIL_INSEN｜1,882円｜💰—｜—｜⚠日程不明
- 4937 Ｇ−ＷＡＱＯＯ｜granville_oshime｜🚀確変｜⚪妥当｜FAIL_INSEN｜2,280円｜💰23.5万円｜—｜📋カルテ窓 11/12(残10営業日)
- 290A ＳＹＮＳＰＥＣＴＩＶＥ｜granville_oshime｜🚀確変｜🟢値頃｜FAIL_UWAHIGE｜1,230円｜💰11.8万円｜—｜📋カルテ窓 11/13(残11営業日)｜📑TOPIX新規採用（10/30 組入）
- 5243 ｎｏｔｅ｜granville_oshime/granville_rebound｜🚀確変｜⚪妥当｜FAIL_INSEN｜2,878円｜💰28.8万円｜—｜⚠日程不明
- 7806 MTG Co., Ltd.｜granville_oshime/changepoint🔔｜🚀確変｜⚪妥当｜FAIL_UWAHIGE｜9,030円｜💰89.8万円｜—｜📑TOPIX新規採用（10/30 組入）
- 6834 Seikoh Giken Co., Ltd.｜granville_oshime/granville_rebound｜🔥絶好調｜💎割安｜PASS｜6,150円｜💰61.5万円｜⛔型不一致: 既に支持帯以下｜📋カルテ窓 11/13(残11営業日)｜📑TOPIX新規採用（10/30 組入）
  > 【業態】光関連部品、金型技術に強み。携帯電話向けレンズ、自動車用センサーも展開。
  > 【いま】終値6,150円・直近5日+7.52%（材料未確認）
  > 【調子】🔥絶好調（10/13）
  > 【水準】💎割安（6.0/7）— PER29.88倍・PEG0.6140・52週74.3% ／ 💰単元61.5万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 6080 Ｍ＆Ａキャピタルパートナーズ｜changepoint/changepoint🔔/granville_oshime｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜4,175円｜💰41.5万円｜—｜⏰決算 10/30(残2営業日)
- 6613 QD Laser, Inc.｜granville_oshime｜🔥絶好調｜🔴過熱｜FAIL_UWAHIGE｜2,303円｜💰22.2万円｜—｜📋カルテ窓 11/12(残10営業日)｜📑TOPIX新規採用（10/30 組入）
- 8008 Yondoshi Holdings, Inc.｜granville_oshime｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜1,952円｜💰20.3万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）
- 4382 HEROZ, Inc.｜changepoint🔔/changepoint🔔🔔/changepoint🔔🔔/granville_oshime｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜1,146円｜💰13.7万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）
- 3156 レスター｜granville_oshime｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜6,000円｜💰62.5万円｜—｜📋カルテ窓 11/13(残11営業日)
- 8051 山善｜granville_oshime｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜1,923円｜💰19.4万円｜—｜📐進捗 上振れ 22.8%
- 4180 ＡＰＰＩＥＲ　ＧＲＯＵＰ｜changepoint🔔/granville_oshime/changepoint🔔🔔｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜1,453円｜💰14.4万円｜—｜📋カルテ窓 11/13(残11営業日)
- 4431 スマレジ｜changepoint/変化点🔔🔔/changepoint🔔/granville_oshime｜🔥絶好調｜🟡やや割高｜PASS｜3,870円｜💰38.7万円｜oshime 3,707.6（✅即時可）｜⚠日程不明｜📆FOMC明け
  > 【業態】小売店クラウド型POSレジ・スマホアプリ「スマレジ」開発販売。中小事業社需要に注力。
  > 【いま】終値3,870円・直近5日+1.84%（材料未確認）
  > 【調子】🔥絶好調（8/13） — E軸判定不能(進捗データ不足)
  > 【水準】🟡やや割高（2.0/7）— PER26.82倍・PEG1.0446・52週87.6% ／ 💰単元38.7万円
  > 【戦略】3,707.6円までの押し目を指値で待つ。SL3,689.2円（25日線基準）
- 7856 HAGIHARA INDUSTRIES INC.｜granville_oshime｜🔥絶好調｜🟡やや割高｜FAIL_INSEN｜1,986円｜💰20.1万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）
- 1879 新日本建設｜granville_oshime｜⚡好調｜💎割安｜FAIL_INSEN｜2,132円｜💰21.9万円｜—｜📋カルテ窓 11/12(残10営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 5892 ＹＵＴＯＲＩ｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,608円｜💰31.6万円｜—｜📋カルテ窓 11/13(残11営業日)
- 6736 Suncorporation｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜9,970円｜💰98.5万円｜—｜📋カルテ窓 11/13(残11営業日)｜📑TOPIX新規採用（10/30 組入）
- 9902 Nichiden Corporation｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜3,135円｜💰31.8万円｜—｜⏰決算 11/05(残5営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 6023 ダイハツインフィニアース｜granville_oshime/granville_rebound｜⚡好調｜🟢値頃｜FAIL_INSEN｜2,727円｜💰28.9万円｜—｜📉決算反応日 10/28
- 6523 PHC Holdings Corp.｜granville_oshime｜⚠減速｜🟢値頃｜PASS｜1,371円｜💰13.7万円｜⛔型不一致: 既に支持帯以下｜📑TOPIX低減対象（次 10/30 第1回/8）｜⚠業績基調が下向き（⚠減速）｜⚠バリュートラップ疑い
  > 【業態】各種ヘルスケア機器・サービスの開発・製造販売。糖尿病ケアに強み。ファンド傘下。
  > 【いま】終値1,371円・直近5日+4.02%（材料未確認）
  > 【調子】⚠減速（6/13） — E軸判定不能(進捗データ不足)、減収、質注意
  > 【水準】🟢値頃（5.0/7）— PER11.31倍・PEG0.0463・52週57.0% ／ 💰単元13.7万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 3106 倉敷紡績｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,378円｜💰24.0万円｜—｜📋カルテ窓 11/12(残10営業日)
- 2767 円谷フィールズホールディングス｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,424円｜💰24.9万円｜—
- 4667 Aisan Technology Co., Ltd.｜granville_oshime/changepoint🔔/changepoint｜⚡好調｜⚪妥当｜FAIL_INSEN｜958円｜💰9.6万円｜—
- 6250 Yamabiko Corporation｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜4,340円｜💰43.7万円｜—｜📋カルテ窓 11/12(残10営業日)
- 7609 ダイトロン｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜4,285円｜💰42.5万円｜—｜⏰決算 11/04(残4営業日)
- 9304 澁澤倉庫｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,025円｜💰20.6万円｜—｜📑TOPIX低減対象（次 10/30 第1回/8）
- 2602 日清オイリオグループ｜granville_oshime｜⚡好調｜🟡やや割高｜FAIL_INSEN｜2,017円｜💰20.5万円｜—
- 4413 baudroie,inc.｜granville_oshime｜⚡好調｜🟡やや割高｜FAIL_INSEN｜2,936円｜💰29.4万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）
- 6570 Kyowa Corporation Co. Ltd.｜granville_oshime｜⚡好調｜🟡やや割高｜FAIL_UWAHIGE｜4,185円｜💰40.5万円｜—
- 8919 カチタス｜granville_oshime｜⚡好調｜🟡やや割高｜FAIL_INSEN｜3,330円｜💰33.6万円｜—
- 8410 Seven Bank, Ltd.｜granville_oshime｜⚡好調｜🔴過熱｜FAIL_INSEN｜336.3円｜💰3.4万円｜—｜📐進捗 上振れ 41.6%
- 7616 Colowide Co., Ltd.｜granville_oshime｜⚡好調｜🔴過熱｜FAIL_INSEN｜2,140円｜💰22.4万円｜—｜⚠日程不明
- 6340 澁谷工業｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜5,390円｜💰53.7万円｜—
- 7350 Okinawa Financial Group, Inc.｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜7,040円｜💰70.2万円｜—｜📋カルテ窓 11/13(残11営業日)
- 4475 HENNGE K.K.｜granville_oshime｜⚡好調｜🔴過熱｜FAIL_INSEN｜2,243円｜💰23.2万円｜—｜⏰決算 11/05(残5営業日)
- 6058 VECTOR Inc.｜granville_oshime｜⚡好調｜🔴過熱｜FAIL_INSEN｜2,060円｜💰21.6万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）｜📐進捗 上振れ 29.5%
- 4373 Simplex Holdings,Inc.｜granville_oshime｜✅順調｜🟡やや割高｜FAIL_UWAHIGE｜1,246円｜💰12.6万円｜—｜📉決算反応日 10/28｜⚡材料後出し
- 3097 Monogatari Corporation｜granville_oshime｜✅順調｜🔴過熱｜FAIL_INSEN｜5,800円｜💰59.8万円｜—｜📋カルテ窓 11/13(残11営業日)
- 6998 Nippon Tungsten Co., Ltd.｜granville_oshime｜✅順調｜🔴過熱｜FAIL_INSEN｜3,135円｜💰31.6万円｜—
- 5985 SUNCALL CORPORATION｜granville_oshime｜✅順調｜🟢値頃｜FAIL_INSEN｜2,002円｜💰19.7万円｜—｜📋カルテ窓 11/13(残11営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 1518 三井松島ホールディングス｜granville_oshime｜✅順調｜🟡やや割高｜FAIL_INSEN｜2,212円｜💰22.9万円｜—｜📋カルテ窓 11/13(残11営業日)
- 4208 UBE Corporation｜granville_oshime｜✅順調｜🟡やや割高｜FAIL_INSEN｜3,322円｜💰32.9万円｜—｜⏰決算 11/05(残5営業日)
- 6379 RAIZNEXT Corporation｜granville_oshime｜✅順調｜🔴過熱｜FAIL_INSEN｜999円｜💰10.2万円｜—｜📋カルテ窓 11/13(残11営業日)
- 9044 NANKAI Co., Ltd.｜granville_oshime｜✅順調｜🟡やや割高｜FAIL_INSEN｜2,975円｜💰30.7万円｜—｜⏰決算 11/02(残3営業日)
- 3107 ダイワボウホールディングス｜granville_oshime｜⚠減速｜🔴過熱｜PASS｜3,856円｜💰38.6万円｜⛔提案なし(指名鮮度切れ 16営業日)｜⚠業績基調が下向き（⚠減速）
  > 【業態】ダイワボウ情報システムが主力。祖業の紡績事業は譲渡。産業機械のIoTを拡大。
  > 【いま】終値3,856円・直近5日+8.68%（材料未確認）
  > 【調子】⚠減速（3/13） — leverage分母ゼロ近傍、進捗21%(前年同期22%・1Q累計・経常ベース)、減収、質注意、経常成長-18.3%
  > 【水準】🔴過熱（1.0/7）— PER13.01倍・PEG—・52週99.4% ／ 💰単元38.6万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 16営業日)）
- 4044 Central Glass Co., Ltd.｜granville_oshime｜✅順調｜🔴過熱｜FAIL_UWAHIGE｜4,505円｜💰45.1万円｜—｜📋カルテ窓 11/12(残10営業日)
- 456A Human Made Inc.｜granville_oshime｜✅順調｜🔴過熱｜FAIL_UWAHIGE｜2,093円｜💰20.9万円｜—｜⚠日程不明
- 7504 Kohsoku Corporation｜granville_oshime｜✅順調｜🔴過熱｜FAIL_INSEN｜5,310円｜💰53.3万円｜—｜⏰決算 10/30(残2営業日)
- 9509 Hokkaido Electric Power Company,Incorporated｜granville_oshime｜🔻悪化｜⚪妥当｜FAIL_INSEN｜1,086円｜💰11.0万円｜—｜⏰決算 10/30(残2営業日)
- 6072 Jibannet Holdings Co., Ltd.｜granville_oshime｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜985円｜💰9.9万円｜—｜📋カルテ窓 11/12(残10営業日)
- 7630 Ichibanya Co., Ltd.｜granville_oshime｜➖横ばい｜🔴過熱｜FAIL_INSEN｜1,043円｜💰10.7万円｜—｜⚠日程不明
- 8043 Starzen Company Limited｜granville_oshime｜➖横ばい｜🔴過熱｜FAIL_INSEN｜1,511円｜💰15.8万円｜—
- 9505 Hokuriku Electric Power Company｜granville_oshime｜🔻悪化｜🔴過熱｜FAIL_INSEN｜1,062円｜💰10.8万円｜—｜🚨決算直前 10/29(残1営業日)
- 9616 共立メンテナンス｜granville_oshime｜➖横ばい｜🔴過熱｜FAIL_INSEN｜3,348円｜💰34.6万円｜—
- 9900 Sagami Holdings Corp.｜granville_oshime｜➖横ばい｜🔴過熱｜FAIL_INSEN｜1,156円｜💰11.3万円｜—｜📋カルテ窓 11/12(残10営業日)
- 8255 Axial Retailing, Inc.｜granville_oshime｜⚠減速｜🔴過熱｜FAIL_INSEN｜1,280円｜💰13.2万円｜—｜⏰決算 11/04(残4営業日)
- 9536 SAIBU GAS HOLDINGS CO. LTD.｜granville_oshime｜⚠減速｜🔴過熱｜FAIL_INSEN｜2,490円｜💰25.3万円｜—｜🚨決算直前 10/29(残1営業日)｜📐進捗 上振れ 57.7%
- 8097 SAN-AI OBBLI CO. LTD｜granville_oshime｜⚠減速｜🔴過熱｜FAIL_INSEN｜2,470円｜💰25.0万円｜—
- 8059 Daiichi Jitsugyo Co., Ltd.｜granville_oshime｜⚠減速｜🔴過熱｜FAIL_INSEN｜3,475円｜💰36.0万円｜—
- 8361 Ogaki Kyoritsu Bank, Ltd.｜granville_oshime/granville_rebound｜取得不可｜💎割安｜FAIL_INSEN｜1,554円｜💰15.2万円｜—｜📋カルテ窓 11/13(残11営業日)
- 9166 GENDA Inc.｜granville_oshime｜業績データ取得不可｜🟢値頃｜PASS_DOJI｜623円｜💰6.2万円｜⛔型不一致: 既に支持帯以下｜⚠日程不明
  > 【業態】「GiGO」ブランドを主としたアミューズメント施設の運営。M&Aで成長。
  > 【いま】終値623円・直近5日-10.10%（材料未確認）
  > 【調子】—（算出不可）
  > 【水準】🟢値頃（5.6/7）— PER—倍・PEG—・52週40.2% ／ 💰単元6.2万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 8343 Akita Bank, Ltd.｜granville_oshime｜業績データ取得不可(売上/経常欠損)｜🟢値頃｜FAIL_INSEN｜1,483円｜💰14.8万円｜—｜📋カルテ窓 11/13(残11営業日)
- 336A ダイナミックマッププラットフォーム｜granville_oshime｜業績データ取得不可(経常益予想非開示)｜⚪妥当｜PASS｜1,390円｜💰13.9万円｜⛔型不一致: 既に支持帯以下｜📋カルテ窓 11/12(残10営業日)
  > 【業態】政府主導、自動運転・先進運転支援向け「高精度3次元地図データ」を提供。
  > 【いま】終値1,390円・直近5日+5.78%・📦連結子会社における大規模道路データ整備案件の受注に関するお知らせ
  > 【調子】—（業績データ算出不可(経常益予想非開示)）
  > 【水準】⚪妥当（4.2/7）— PER—倍・PEG—・52週56.7% ／ 💰単元13.9万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 6810 マクセル｜granville_oshime｜取得不可｜⚪妥当｜FAIL_INSEN｜2,530円｜💰25.0万円｜—｜🚨決算直前 10/29(残1営業日)｜⚡材料後出し
- 6027 弁護士ドットコム｜granville_oshime｜業績データ取得不可｜🟡やや割高｜FAIL_UWAHIGE｜4,670円｜💰46.6万円｜—｜📑TOPIX低減対象（次 10/30 第1回/8）
- 8362 Fukui Bank, Ltd.｜granville_oshime｜🔻悪化｜🔴過熱｜FAIL_INSEN｜6,870円｜💰68.5万円｜—｜📋カルテ窓 11/13(残11営業日)
- 8137 サンワテクノス｜granville_oshime｜業績—｜—｜FAIL_INSEN｜4,510円｜💰—｜—｜⏰決算 10/30(残2営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 8622 Mito Securities Co., Ltd.｜granville_oshime/granville_rebound｜取得不可｜⏸判定不能｜FAIL_INSEN｜737円｜💰7.4万円｜—｜🚨決算直前 10/29(残1営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 8624 Ichiyoshi Securities Co., Ltd.｜granville_oshime/granville_rebound｜取得不可｜⏸判定不能｜PASS_DOJI｜1,453円｜💰14.5万円｜⛔提案なし(指名鮮度切れ 13営業日)｜🚨決算直前 10/29(残1営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
  > 【業態】関西発祥。個人営業主体で中・小型株に特化。首都圏で富裕層に強み。
  > 【いま】終値1,453円・直近5日-6.62%（材料未確認）
  > 【調子】—（業績データ算出不可(経常益予想非開示)）
  > 【水準】⏸判定不能（—/7）— PER—倍・PEG—・52週64.4% ／ 💰単元14.5万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 13営業日)）
- 8628 松井証券｜granville_oshime｜業績データ取得不可｜⏸判定不能｜FAIL_UWAHIGE｜1,063円｜💰10.6万円｜—｜📉決算反応日 10/28
- 3778 SAKURA Internet Inc.｜granville_rebound｜🚀確変｜⚪妥当｜PASS｜3,470円｜💰34.7万円｜reversal 3,470（✅即時可）｜📉決算反応日 10/28｜⚠1単元でリスク枠超過（75900円）｜📆FOMC明け
  > 【業態】情報・通信業（データセンター・ホスティング・クラウドコンピューティング関連）
  > 【いま】終値3,470円・直近5日+9.81%・📊2027年3月期第2四半期（中間期）決算短信〔日本基準〕（連結）
  > 【調子】🚀確変（12/13） — 上方修正済み、前期経常が小さく成長率が大きく出る(105→3,900百万円)
  > 【水準】⚪妥当（4.0/7）— PER92.53倍・PEG0.0443・52週53.7% ／ 💰単元34.7万円
  > 【戦略】当日終値3,470円の指値で反転を取りにいく。SL2,711円（直近5日安値）／⚠1単元リスク75900円（枠超過）
- 6769 Thine Electronics, Inc.｜granville_rebound｜🚀確変｜⚪妥当｜FAIL_INSEN｜1,025円｜💰10.2万円｜—｜⏰決算 11/05(残5営業日)
- 3691 DIGITAL PLUS, Inc.｜granville_rebound｜🔥絶好調｜🟢値頃｜PASS｜1,487円｜💰14.9万円｜reversal 1,487（✅即時可）｜📋カルテ窓 11/13(残11営業日)｜📆FOMC明け
  > 【業態】金券をキャッシュレスで贈るデジタルギフト事業が主力。デジタルマーケティングは譲渡。
  > 【いま】終値1,487円・直近5日-12.17%（材料未確認）
  > 【調子】🔥絶好調（10/13） — 営業益代替、黒字転換、D軸判定不能、E軸判定不能(進捗データ不足)、E簡易判定
  > 【水準】🟢値頃（5.6/7）— PER—倍・PEG—・52週29.2% ／ 💰単元14.9万円
  > 【戦略】当日終値1,487円の指値で反転を取りにいく。SL1,395円（直近5日安値）
- 479A PRONI Inc.｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1,804円｜💰18.2万円｜—｜📋カルテ窓 11/13(残11営業日)
- 1436 GreenEnergy & Company｜granville_rebound｜🔥絶好調｜💎割安｜FAIL_INSEN｜1,403円｜💰14.9万円｜—｜⚠日程不明｜⚡材料後出し
- 8995 Makoto Construction Co,Ltd｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜1,780円｜💰15.7万円｜—｜📋カルテ窓 11/13(残11営業日)
- 2122 インタースペース｜granville_rebound｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜1,315円｜💰13.4万円｜—
- 6963 ROHM Company Limited｜granville_rebound｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜3,830円｜💰37.0万円｜—｜⏰決算 11/05(残5営業日)
- 150A ＪＳＨ｜granville_rebound｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜624円｜💰7.7万円｜—｜📋カルテ窓 11/12(残10営業日)
- 7715 長野計器｜granville_rebound｜🔥絶好調｜🟢値頃｜PASS｜3,980円｜💰39.8万円｜reversal 3,980（✅即時可）｜📋カルテ窓 11/12(残10営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）｜📐進捗 上振れ 10.5%｜⚠1単元でリスク枠超過（39500円）｜📆FOMC明け
  > 【業態】圧力計・圧力センサー大手。機械式圧力計で世界シェア首位。車載向け主力。
  > 【いま】終値3,980円・直近5日-1.85%（材料未確認）
  > 【調子】🔥絶好調（8/13） — E軸:進捗21.0%>=前年同期19.0%
  > 【水準】🟢値頃（5.0/7）— PER10.41倍・PEG0.2140・52週66.8% ／ 💰単元39.8万円
  > 【戦略】当日終値3,980円の指値で反転を取りにいく。SL3,585円（直近5日安値）／⚠1単元リスク39500円（枠超過）
- 8364 清水銀行｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜2,721円｜💰27.2万円｜—｜📋カルテ窓 11/13(残11営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 6490 ＰＩＬＬＡＲ｜granville_rebound｜⚡好調｜⚪妥当｜FAIL_INSEN｜10,390円｜💰100.2万円｜—｜📋カルテ窓 11/12(残10営業日)
- 5242 EYEZ INC.｜granville_rebound｜⚡好調｜🔴過熱｜FAIL_UWAHIGE｜3,125円｜💰30.0万円｜—｜📋カルテ窓 11/13(残11営業日)
- 477A Startline CO.,LTD.｜granville_rebound｜⚡好調｜💎割安｜FAIL_INSEN｜756円｜💰7.7万円｜—｜📋カルテ窓 11/13(残11営業日)
- 6336 石井表記｜granville_rebound｜⚡好調｜🟢値頃｜FAIL_INSEN｜1,371円｜💰13.4万円｜—｜⚠日程不明
- 2354 YE DIGITAL CORPORATION｜granville_rebound｜⚡好調｜💎割安｜FAIL_INSEN｜1,032円｜💰10.4万円｜—｜⚠日程不明
- 4100 Toda Kogyo Corp.｜granville_rebound｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜1,745円｜💰16.1万円｜—｜📑TOPIX低減対象（次 10/30 第1回/8）
- 8344 Yamagata Bank, Ltd.｜granville_rebound｜⚡好調｜🟢値頃｜FAIL_INSEN｜4,425円｜💰43.8万円｜—｜📋カルテ窓 11/13(残11営業日)
- 8392 大分銀行｜granville_rebound｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜2,787円｜💰27.3万円｜—
- 6597 HPC SYSTEMS Inc.｜changepoint/changepoint🔔/changepoint🔔🔔/granville_rebound｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜3,180円｜💰31.0万円｜—｜📋カルテ窓 11/13(残11営業日)
- 3687 Fixstars Corp.｜granville_rebound｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜1,902円｜💰18.5万円｜—｜📑TOPIX低減対象（次 10/30 第1回/8）
- 5574 ABEJA,Inc.｜granville_rebound｜⚡好調｜🟡やや割高｜FAIL_UWAHIGE｜2,441円｜💰23.6万円｜—｜⚠日程不明
- 9278 BOOKOFF GROUP HOLDINGS LIMITED｜granville_rebound｜⚡好調｜🟡やや割高｜FAIL_INSEN｜2,355円｜💰24.1万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）
- 7256 河西工業｜granville_rebound｜⚡好調｜🔴過熱｜FAIL_INSEN｜411円｜💰—｜—｜📋カルテ窓 11/16(残12営業日)
- 4997 日本農薬｜granville_rebound｜✅順調｜🟡やや割高｜FAIL_INSEN｜1,050円｜💰10.7万円｜—｜📑TOPIX低減対象（次 10/30 第1回/8）
- 278A Ｔｅｒｒａ　Ｄｒｏｎｅ｜granville_rebound｜✅順調｜⏸判定不能｜FAIL_INSEN｜6,460円｜💰—｜—｜⚠日程不明
- 1407 West Holdings Corporation｜granville_rebound｜✅順調｜🟢値頃｜PASS｜2,186円｜💰21.9万円｜⛔提案なし(指名鮮度切れ 21営業日)｜⚠日程不明
  > 【業態】太陽光発電設置、保守。再生可能エネ供給や省エネ提案。タイで日系企業へ供給。
  > 【いま】終値2,186円・直近5日-0.27%（材料未確認）
  > 【調子】✅順調（3/13） — E軸判定不能(進捗データ不足)
  > 【水準】🟢値頃（5.0/7）— PER9.24倍・PEG0.5118・52週45.1% ／ 💰単元21.9万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 21営業日)）
- 4346 NEXYZ.Group Corporation｜granville_rebound｜✅順調｜🟢値頃｜FAIL_INSEN｜743円｜💰7.5万円｜—｜📋カルテ窓 11/16(残12営業日)
- 7354 Direct Marketing MiX Inc.｜granville_rebound｜✅順調｜⚪妥当｜FAIL_UWAHIGE｜375円｜💰4.0万円｜—｜📋カルテ窓 11/13(残11営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 2681 2nd RETAILING Co., Ltd.｜granville_rebound｜✅順調｜🟡やや割高｜FAIL_INSEN｜1,899円｜💰20.3万円｜—｜📑TOPIX低減対象（次 10/30 第1回/8）
- 4082 第一稀元素化学工業｜granville_rebound｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜1,821円｜💰17.9万円｜—｜📋カルテ窓 11/12(残10営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 3653 Morpho, Inc.｜granville_rebound｜🔻悪化｜💎割安｜FAIL_INSEN｜912円｜💰9.2万円｜—｜⚠日程不明
- 3907 Silicon Studio Corp.｜granville_rebound｜🔻悪化｜💎割安｜FAIL_INSEN｜1,276円｜💰13.7万円｜—｜⚠日程不明
- 4440 WITZ Corp.｜granville_rebound｜➖横ばい｜⚪妥当｜FAIL_INSEN｜1,746円｜💰18.0万円｜—｜⚠日程不明
- 8163 SRS HOLDINGS CO.,LTD.｜granville_rebound｜➖横ばい｜🔴過熱｜FAIL_INSEN｜1,669円｜💰17.1万円｜—
- 4691 Washington Hotel Corp.｜granville_rebound｜⚠減速｜⚪妥当｜FAIL_UWAHIGE｜1,830円｜💰18.3万円｜—｜📋カルテ窓 11/13(残11営業日)
- 6203 Howa Machinery, Ltd.｜granville_rebound｜⚠減速｜🟡やや割高｜FAIL_INSEN｜2,175円｜💰22.8万円｜—｜📋カルテ窓 11/13(残11営業日)
- 6522 アスタリスク｜granville_rebound｜⚠減速｜🟢値頃｜FAIL_INSEN｜794円｜💰8.1万円｜—｜⚠日程不明
- 8360 Yamanashi Chuo Bank, Ltd.｜granville_rebound｜取得不可｜💎割安｜FAIL_INSEN｜1,288円｜💰12.8万円｜—｜📋カルテ窓 11/13(残11営業日)
- 7380 Juroku Financial Group,Inc.｜granville_rebound｜取得不可｜⚪妥当｜FAIL_INSEN｜2,383円｜💰23.6万円｜—
- 8368 Hyakugo Bank, Ltd.｜granville_rebound｜取得不可｜🟡やや割高｜FAIL_INSEN｜2,118円｜💰20.9万円｜—
- 8713 Fidea Holdings Co.Ltd.｜granville_rebound｜業績データ取得不可(売上/経常欠損)｜🔴過熱｜FAIL_INSEN｜2,521円｜💰25.3万円｜—｜📋カルテ窓 11/13(残11営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 3891 ニッポン高度紙工業｜granville_rebound｜業績—｜—｜FAIL_INSEN｜6,010円｜💰—｜—｜🚨決算直前 10/29(残1営業日)
- 6840 ＡＫＩＢＡホールディングス｜granville_rebound｜業績—｜—｜FAIL_INSEN｜718円｜💰—｜—｜📋カルテ窓 11/13(残11営業日)
- 6890 Ferrotec Corporation｜granville_rebound｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜8,390円｜💰79.4万円｜—｜📋カルテ窓 11/16(残12営業日)｜📑TOPIX新規採用（10/30 組入）
- 7175 Imamura Securities Co.Ltd.｜granville_rebound｜業績データ取得不可｜⏸判定不能｜PASS｜1,701円｜💰17.0万円｜reversal 1,701（✅即時可）｜⚠日程不明｜📆FOMC明け
  > 【業態】富山、石川、福井の北陸３県が地盤の老舗証券会社。ネットと対面営業。
  > 【いま】終値1,701円・直近5日-0.35%（材料未確認）
  > 【調子】—（通期予想が非開示(会社側未公表)）
  > 【水準】⏸判定不能（—/7）— PER—倍・PEG—・52週53.3% ／ 💰単元17.0万円
  > 【戦略】当日終値1,701円の指値で反転を取りにいく。SL1,613円（直近5日安値）
- 8377 ほくほくフィナンシャルグループ｜granville_rebound｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜745.2円｜💰7.4万円｜—
- 8609 岡三証券グループ｜granville_rebound｜業績—｜—｜FAIL_UWAHIGE｜1,071円｜💰—｜—｜🚨決算直前 10/29(残1営業日)
- 8739 スパークス・グループ｜granville_rebound｜業績データ取得不可｜⏸判定不能｜FAIL_UWAHIGE｜2,336円｜💰23.2万円｜—｜⏰決算 10/30(残2営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 9697 カプコン｜granville_rebound｜業績—｜—｜FAIL_INSEN｜3,835円｜💰—｜—｜⚠日程不明

## 変化点銘柄
- 265A エイチエムコム｜changepoint🔔｜🚀確変｜🟢値頃｜FAIL_INSEN｜725円｜💰7.3万円｜—｜📋カルテ窓 11/13(残11営業日)｜🔒実弾封印中(PL3紙ログ収集中)｜⚡材料後出し
- 5803 フジクラ｜changepoint🔔/changepoint🔔/changepoint🔔🔔｜🚀確変｜🟢値頃｜FAIL_INSEN｜4,111円｜💰40.9万円｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 4011 Headwaters Co.,Ltd｜changepoint🔔/changepoint｜🚀確変｜🟢値頃｜FAIL_INSEN｜2,181円｜💰21.6万円｜—｜📋カルテ窓 11/13(残11営業日)｜🔒実弾封印中(PL3紙ログ収集中)
- 4187 大阪有機化学工業｜changepoint/changepoint🔔｜🔥絶好調｜💎割安｜FAIL_UWAHIGE｜4,585円｜💰44.0万円｜—｜⚠日程不明｜🔒実弾封印中(PL3紙ログ収集中)
- 9888 UEX LTD｜changepoint/changepoint🔔/changepoint🔔🔔｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1,333円｜💰13.8万円｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 7695 交換できるくん｜changepoint🔔｜🔥絶好調｜⚪妥当｜PASS｜869円｜💰8.7万円｜changepoint 869（✅即時可）｜📋カルテ窓 11/13(残11営業日)｜🔒実弾封印中(PL3紙ログ収集中)｜📆FOMC明け
  > 【業態】住宅設備機器と工事をセットでネット販売。見積もり、注文をネットで低価格化。
  > 【いま】終値869円・直近5日-1.81%（材料未確認）
  > 【調子】🔥絶好調（10/13） — E軸判定不能(進捗データ不足)
  > 【水準】⚪妥当（4.0/7）— PER25.94倍・PEG0.1762・52週69.2% ／ 💰単元8.7万円
  > 【戦略】発火日終値869円の指値。追撃禁止・SL844円。🔒実弾封印中（PL3紙ログ収集中）
- 584A LiNKX, Inc.｜changepoint🔔/changepoint🔔｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜2,331円｜💰23.1万円｜—｜📋カルテ窓 11/13(残11営業日)｜🔒実弾封印中(PL3紙ログ収集中)
- 6136 OSG CORP｜changepoint/changepoint🔔/changepoint🔔🔔｜🔥絶好調｜🟢値頃｜PASS_DOJI｜3,535円｜💰35.4万円｜changepoint 3,535（✅即時可）｜⚠日程不明｜🔒実弾封印中(PL3紙ログ収集中)｜📆FOMC明け
  > 【業態】タップ・エンドミルなど高シェアの精密切削工具大手。製販一貫体制。海外に注力。
  > 【いま】終値3,535円・直近5日-5.33%（材料未確認）
  > 【調子】🔥絶好調（9/13） — E軸判定不能(進捗データ不足)
  > 【水準】🟢値頃（5.0/7）— PER12.10倍・PEG0.1728・52週66.9% ／ 💰単元35.4万円
  > 【戦略】発火日終値3,535円の指値。追撃禁止・SL3,376円。🔒実弾封印中（PL3紙ログ収集中）
- 6857 アドバンテスト｜changepoint/changepoint🔔｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜34,930円｜💰338.6万円｜—｜📉決算反応日 10/28｜🔒実弾封印中(PL3紙ログ収集中)｜⚡材料後出し
- 8151 東陽テクニカ｜changepoint🔔｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜1,912円｜💰19.2万円｜—｜📑TOPIX低減対象（次 10/30 第1回/8）｜🔒実弾封印中(PL3紙ログ収集中)
- 9962 ミスミグループ本社｜changepoint/changepoint🔔｜🔥絶好調｜⚪妥当｜PASS｜3,882円｜💰38.8万円｜changepoint 3,882（✅即時可）｜⏰決算 10/30(残2営業日)｜🔒実弾封印中(PL3紙ログ収集中)｜⚠1単元でリスク枠超過（40500円）｜📆FOMC明け
  > 【業態】金型用部品の専門商社・ミスミが中核。ネット・カタログ販売。半製品で納期短縮。
  > 【いま】終値3,882円・直近5日+1.20%（材料未確認）
  > 【調子】🔥絶好調（9/13）
  > 【水準】⚪妥当（3.0/7）— PER22.77倍・PEG0.6140・52週84.6% ／ 💰単元38.8万円
  > 【戦略】発火日終値3,882円の指値。追撃禁止・SL3,477円。🔒実弾封印中（PL3紙ログ収集中）／⚠1単元リスク40500円（枠超過）
- 7318 セレンディップ・ホールディングス｜changepoint🔔/changepoint🔔🔔/changepoint🔔🔔｜🔥絶好調｜💎割安｜FAIL_UWAHIGE｜1,133円｜💰10.9万円｜—｜📋カルテ窓 11/13(残11営業日)｜🔒実弾封印中(PL3紙ログ収集中)
- 4368 4368｜changepoint/changepoint🔔｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜3,045円｜💰29.3万円｜—｜⏰決算 10/30(残2営業日)｜🔒実弾封印中(PL3紙ログ収集中)
- 5582 （名称取得不可）｜changepoint🔔｜🔥絶好調｜🟢値頃｜PASS_DOJI｜1,822円｜💰18.2万円｜changepoint 1,822（✅即時可）｜📋カルテ窓 11/16(残12営業日)｜🔒実弾封印中(PL3紙ログ収集中)｜📆FOMC明け
  > 【業態】人工知能を用いた計画最適化システムの開発・販売を展開。電力、交通、物流等。
  > 【いま】終値1,822円・直近5日-6.80%（材料未確認）
  > 【調子】🔥絶好調（8/13） — E軸判定不能(進捗データ不足)
  > 【水準】🟢値頃（5.0/7）— PER21.87倍・PEG0.7078・52週9.8% ／ 💰単元18.2万円
  > 【戦略】発火日終値1,822円の指値。追撃禁止・SL1,758円。🔒実弾封印中（PL3紙ログ収集中）
- 5590 NETSTARS Co.,Ltd.｜changepoint🔔｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜658円｜💰6.6万円｜—｜📋カルテ窓 11/12(残10営業日)｜🔒実弾封印中(PL3紙ログ収集中)
- 478A Hutzper Inc.｜changepoint🔔/changepoint🔔🔔｜⚡好調｜⚪妥当｜FAIL_INSEN｜713円｜💰7.3万円｜—｜📋カルテ窓 11/16(残12営業日)｜🔒実弾封印中(PL3紙ログ収集中)
- 9343 アイビス｜changepoint｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜776円｜💰7.7万円｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 8704 トレイダーズホールディングス｜changepoint/changepoint🔔｜⚡好調｜💎割安｜PASS｜1,254円｜💰12.5万円｜⛔提案なし(材料後出し)｜⏰決算 10/30(残2営業日)｜🔒実弾封印中(PL3紙ログ収集中)｜⚡材料後出し
  > 【業態】証券・商品（外国為替証拠金取引・金融向けシステム・コンサルティング関連）
  > 【いま】終値1,254円・直近5日-5.00%・📌トレイダーズ証券「みんなのシストレ」に関する2件の特許取得のお知らせ
  > 【調子】⚡好調（5/13） — E軸判定不能(進捗データ不足)
  > 【水準】💎割安（6.0/7）— PER6.89倍・PEG0.5060・52週65.2% ／ 💰単元12.5万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 6284 日精エー・エス・ビー機械｜changepoint🔔｜⚡好調｜🟢値頃｜FAIL_INSEN｜8,120円｜💰80.1万円｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 218A Liberaware｜changepoint/changepoint🔔｜⚡好調｜⚪妥当｜FAIL_INSEN｜914円｜💰9.1万円｜—｜⚠日程不明｜🔒実弾封印中(PL3紙ログ収集中)
- 6785 鈴木｜changepoint/changepoint🔔🔔｜✅順調｜⚪妥当｜FAIL_INSEN｜3,250円｜💰32.4万円｜—｜📑TOPIX低減対象（次 10/30 第1回/8）｜🔒実弾封印中(PL3紙ログ収集中)
- 4165 PLAID Inc.｜changepoint🔔｜🔻悪化｜🔴過熱｜FAIL_UWAHIGE｜758円｜💰7.4万円｜—｜📋カルテ窓 11/12(残10営業日)｜🔒実弾封印中(PL3紙ログ収集中)
- 4498 Cybertrust Japan Co., Ltd.｜changepoint🔔/changepoint🔔🔔｜✅順調｜🔴過熱｜FAIL_INSEN｜2,447円｜💰29.5万円｜—｜🚨決算直前 10/29(残1営業日)｜🔒実弾封印中(PL3紙ログ収集中)
- 4071 Plus Alpha Consulting Co. LTD.｜changepoint🔔｜✅順調｜⚪妥当｜FAIL_INSEN｜2,268円｜💰23.1万円｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 4418 Japan Data Science Consortium Co Ltd.｜changepoint🔔｜⚠減速｜⚪妥当｜FAIL_UWAHIGE｜1,128円｜💰10.9万円｜—｜📋カルテ窓 11/13(残11営業日)｜🔒実弾封印中(PL3紙ログ収集中)
- 598A チャットプラス｜changepoint🔔/changepoint/changepoint🔔🔔｜✅順調｜⚪妥当｜FAIL_UWAHIGE｜1,177円｜💰11.7万円｜—｜📋カルテ窓 11/12(残10営業日)｜🔒実弾封印中(PL3紙ログ収集中)
- 4493 Cyber Security Cloud, Inc.｜changepoint🔔｜✅順調｜🔴過熱｜FAIL_INSEN｜3,165円｜💰35.5万円｜—｜📋カルテ窓 11/13(残11営業日)｜🔒実弾封印中(PL3紙ログ収集中)
- 339A PROGRESS TECHNOLOGIES GROUP INC｜changepoint/changepoint🔔/changepoint🔔🔔｜➖横ばい｜⚪妥当｜FAIL_INSEN｜803円｜💰8.1万円｜—｜⚠日程不明｜🔒実弾封印中(PL3紙ログ収集中)
- 4488 AI inside Inc.｜changepoint｜➖横ばい｜🟡やや割高｜PASS｜2,008円｜💰20.1万円｜⛔提案なし(指名鮮度切れ 16営業日)｜📋カルテ窓 11/12(残10営業日)｜🔒実弾封印中(PL3紙ログ収集中)
  > 【業態】AI技術を用いた光学式文字読み取り装置(OCR)サービス提供。手書きに強み。
  > 【いま】終値2,008円・直近5日-0.10%（材料未確認）
  > 【調子】➖横ばい（2/13） — E軸判定不能(進捗データ不足)
  > 【水準】🟡やや割高（2.0/7）— PER22.14倍・PEG3.8506・52週8.3% ／ 💰単元20.1万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 16営業日)）
- 4259 ExaWizards Inc.｜changepoint/changepoint🔔｜業績データ取得不可｜🟢値頃｜FAIL_INSEN｜793円｜💰7.6万円｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 3993 PKSHA Technology, Inc.｜changepoint🔔｜業績データ取得不可｜⚪妥当｜FAIL_UWAHIGE｜3,830円｜💰37.3万円｜—｜📋カルテ窓 11/12(残10営業日)｜🔒実弾封印中(PL3紙ログ収集中)
- 4478 freee K.K.｜changepoint🔔/changepoint🔔🔔/changepoint｜業績データ取得不可｜🟡やや割高｜PASS｜4,320円｜💰43.2万円｜⛔提案なし(材料後出し)｜📑TOPIX新規採用（10/30 組入）｜🔒実弾封印中(PL3紙ログ収集中)｜⚡材料後出し
  > 【業態】スモールビジネス向けクラウドERPサービスの提供。会計や会社設立、開業支援など。
  > 【いま】終値4,320円・直近5日+10.20%・📌譲渡制限付株式としての自己株式処分及び業績連動型株式報酬制度に基づく自己株式処分の払込完了に関するお知らせ
  > 【調子】—（業績データ算出不可(売上/経常欠損)）
  > 【水準】🟡やや割高（2.8/7）— PER—倍・PEG—・52週90.4% ／ 💰単元43.2万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 593A ティアフォー｜changepoint/changepoint🔔/changepoint🔔🔔｜取得不可｜🔴過熱｜FAIL_INSEN｜2,161円｜💰22.4万円｜—｜📋カルテ窓 11/13(残11営業日)｜📑TOPIX新規採用（10/30 組入）｜🔒実弾封印中(PL3紙ログ収集中)

## 🤖AI特需銘柄
①-S3 は本夜分(scored_at=2026-10-28)が未更新のため、候補としては使わず、プール在籍分のみ継続評価。参考: ai_scan base_day=2026-10-23｜25MA上回り率 📡エネマネ・計量 14.29%; ❄️冷却・空調 16.67%; 🌐光通信 9.09%; 🔬基板・素材 4.76%
- 3131 シンデン・ハイテックス｜ai_momentum/ai_reversal/granville_rebound｜🚀確変｜💎割安｜FAIL_INSEN｜5,420円｜💰64.0万円｜—
- 2760 東京エレクトロン　デバイス｜ai_momentum/granville_oshime/ai_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜4,700円｜💰45.7万円｜—｜📉決算反応日 10/28｜⚡材料後出し
- 9824 泉州電業｜ai_momentum｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜8,390円｜💰82.0万円｜—｜⚠日程不明
- 6521 オキサイド｜ai_momentum/ai_reversal｜⚡好調｜🟢値頃｜PASS｜3,575円｜💰35.8万円｜momentum 3,585（✅即時可）｜⚠日程不明｜📆FOMC明け
  > 【業態】単結晶や光部品、レーザ光源、計測装置の開発・販売。半導体、画像装置向け。
  > 【いま】終値3,575円・直近5日+10.68%（材料未確認）
  > 【調子】⚡好調（7/13） — 経常成長率+83.1%、D軸判定不能(直近Qデータ算出不可)、E軸判定不能(進捗データ不足)
  > 【水準】🟢値頃（5.0/7）— PER31.30倍・PEG0.3768・52週36.2% ／ 💰単元35.8万円
  > 【戦略】当日高値超えの逆指値3,585円で順張り参戦を検討。上限3,620.8円・SL3,365.2円目安
- 1982 日比谷総合設備｜ai_momentum｜⚠減速｜🔴過熱｜FAIL_INSEN｜3,350円｜💰33.4万円｜—
- 9960 トーテック｜granville_tenkan/granville_oshime/ai_momentum｜⚠減速｜🔴過熱｜FAIL_INSEN｜4,345円｜💰43.8万円｜—
- 6254 野村マイクロ・サイエンス｜changepoint🔔/ai_reversal｜🚀確変｜💎割安｜FAIL_UWAHIGE｜2,930円｜💰28.2万円｜—｜📋カルテ窓 11/13(残11営業日)
- 4047 関東電化工業｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_UWAHIGE｜2,071円｜💰20.1万円｜—
- 4971 メック｜ai_reversal｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜6,320円｜💰60.1万円｜—
- 3110 日東紡｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜3,025円｜💰29.4万円｜—｜⏰決算 11/05(残5営業日)｜📐進捗 上振れ 21.5%
- 6981 村田製作所｜ai_reversal｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜6,701円｜💰63.7万円｜—｜⏰決算 10/30(残2営業日)
- 7433 伯東｜ai_reversal/granville_oshime｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1,800円｜💰18.1万円｜—｜📋カルテ窓 11/12(残10営業日)
- 4062 イビデン｜ai_reversal/granville_rebound｜🔥絶好調｜⚪妥当｜PASS｜9,663円｜💰96.6万円｜reversal 9,663（✅即時可）｜🚨決算直前 10/29(残1営業日)｜⚠1単元でリスク枠超過（178000円）｜📆FOMC明け
  > 【業態】ICパッケージ、プリント配線板で首位級。スマホ用が拡大。自動車排ガス除去も大手。
  > 【いま】終値9,663円・直近5日+1.72%（材料未確認）
  > 【調子】🔥絶好調（9/13） — E軸判定不能(進捗データ不足)
  > 【水準】⚪妥当（4.0/7）— PER65.03倍・PEG0.5976・52週63.3% ／ 💰単元96.6万円
  > 【戦略】当日終値9,663円の指値で反転を取りにいく。SL7,883円（直近5日安値）／⚠1単元リスク178000円（枠超過）
- 6524 湖北工業｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜4,785円｜💰45.9万円｜—｜📋カルテ窓 11/12(残10営業日)
- 6235 オプトラン｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_UWAHIGE｜2,385円｜💰22.6万円｜—
- 7729 東京精密｜ai_reversal｜🔥絶好調｜⚪妥当｜PASS｜16,325円｜💰163.2万円｜reversal 16,325（✅即時可）｜⏰決算 11/04(残4営業日)｜⚠1単元でリスク枠超過（201000円）｜📆FOMC明け
  > 【業態】半導体製造装置・計測機器メーカー。ウエハテスト用首位。精密位置決め技術に定評。
  > 【いま】終値16,325円・直近5日-4.45%（材料未確認）
  > 【調子】🔥絶好調（8/13）
  > 【水準】⚪妥当（3.0/7）— PER21.51倍・PEG0.8166・52週58.3% ／ 💰単元163.2万円
  > 【戦略】当日終値16,325円の指値で反転を取りにいく。SL14,315円（直近5日安値）／⚠1単元リスク201000円（枠超過）
- 6752 パナソニックHD｜ai_reversal/granville_rebound｜⚠減速｜⚪妥当｜PASS｜3,787円｜💰37.9万円｜reversal 3,787（✅即時可）｜⏰決算 10/30(残2営業日)｜⚠業績基調が下向き（⚠減速）｜📆FOMC明け
  > 【業態】総合家電大手。AV、白モノ家電が軸。電池、照明、デバイス、住設も。車機器売却。
  > 【いま】終値3,787円・直近5日-3.02%（材料未確認）
  > 【調子】⚠減速（7/13） — E軸判定不能(進捗データ不足)、減収でleverage参考値、D軸判定不能(四半期データ不足・中立1点)、減収
  > 【水準】⚪妥当（4.0/7）— PER19.65倍・PEG0.1582・52週64.1% ／ 💰単元37.9万円
  > 【戦略】当日終値3,787円の指値で反転を取りにいく。SL3,494円（直近5日安値）
- 6779 Nihon Dempa Kogyo Co., Ltd.｜granville_rebound/ai_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,669円｜💰25.6万円｜—
- 6787 メイコー｜ai_reversal｜⚡好調｜💎割安｜FAIL_INSEN｜20,300円｜💰194.6万円｜—
- 6227 AIMECHATEC Ltd.｜granville_oshime/ai_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜6,060円｜💰57.7万円｜—｜📋カルテ窓 11/13(残11営業日)｜📑TOPIX新規採用（10/30 組入）
- 4658 日本空調サービス｜granville_tenkan/ai_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜1,525円｜💰15.4万円｜—｜⏰決算 10/30(残2営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 8098 稲畑産業｜ai_reversal/granville_oshime｜✅順調｜🔴過熱｜FAIL_INSEN｜4,460円｜💰45.0万円｜—｜⏰決算 11/05(残5営業日)｜⚡材料後出し
- 5208 Arisawa Mfg.Co., Ltd.｜granville_oshime/ai_reversal｜✅順調｜🔴過熱｜FAIL_INSEN｜2,666円｜💰26.4万円｜—｜⏰決算 11/05(残5営業日)
- 3433 TOCALO Co., Ltd.｜granville_tenkan/ai_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜2,755円｜💰27.0万円｜—｜⏰決算 11/05(残5営業日)
- 6643 戸上電機製作所｜ai_reversal｜✅順調｜⚪妥当｜FAIL_UWAHIGE｜5,190円｜💰51.2万円｜—｜⏰決算 11/04(残4営業日)
- 5706 三井金属鉱業｜ai_reversal｜🔻悪化｜🟡やや割高｜PASS｜2,152.5円｜💰21.5万円｜reversal 2,152.5（✅即時可）｜⚠業績基調が下向き（🔻悪化）｜📆FOMC明け
  > 【業態】非鉄大手。銅箔で世界首位級。半導体材料にも強み。自動車部品に注力。
  > 【いま】終値2,152.5円・直近5日-5.28%（材料未確認）
  > 【調子】🔻悪化（2/13） — 質注意、E軸判定不能(進捗データ不足)、D軸判定不能(四半期データ不足・中立1点)、経常減益
  > 【水準】🟡やや割高（2.8/7）— PER15.40倍・PEG—・52週16.7% ／ 💰単元21.5万円
  > 【戦略】当日終値2,152.5円の指値で反転を取りにいく。SL1,908.5円（直近5日安値）
- 3103 ユニチカ｜ai_reversal/granville_rebound｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜1,260円｜💰12.3万円｜—
- 6590 芝浦メカトロニクス｜ai_reversal｜➖横ばい｜🟡やや割高｜PASS｜3,400円｜💰34.0万円｜reversal 3,400（✅即時可）｜⏰決算 11/05(残5営業日)｜⚠1単元でリスク枠超過（52600円）｜📆FOMC明け
  > 【業態】液晶・半導体の製造装置メーカー。前工程ウエハ洗浄で世界トップ。自販機システムも。
  > 【いま】終値3,400円・直近5日-1.02%（材料未確認）
  > 【調子】➖横ばい（2/13） — E軸判定不能(進捗データ不足)、質注意
  > 【水準】🟡やや割高（2.0/7）— PER18.75倍・PEG3.4928・52週15.3% ／ 💰単元34.0万円
  > 【戦略】当日終値3,400円の指値で反転を取りにいく。SL2,874円（直近5日安値）／⚠1単元リスク52600円（枠超過）
- 5302 日本カーボン｜ai_reversal｜➖横ばい｜🔴過熱｜FAIL_INSEN｜4,905円｜💰49.2万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）
- 9432 NTT｜ai_reversal｜➖横ばい｜🔴過熱｜FAIL_INSEN｜171.9円｜💰1.7万円｜—｜⏰決算 11/04(残4営業日)
- 4203 住友ベークライト｜ai_reversal｜業績データ取得不可｜⚪妥当｜FAIL_INSEN｜8,309円｜💰78.3万円｜—｜⏰決算 11/04(残4営業日)

## ⚡材料後出し
その日の足は開示前の情報。判定は参考値
- 276A CCReB Advisors Inc.｜FAIL_INSEN｜📌販売用不動産の取得完了に関するお知らせ｜15:30
- 9560 PROGRIT, Inc.｜FAIL_INSEN｜📌有償ストック・オプション（新株予約権）の発行に関するお知らせ｜15:30
- 3843 Freebit Co., Ltd.｜FAIL_INSEN｜📌再発防止策の実施状況に関するお知らせ｜17:00
- 3843 Freebit Co., Ltd.｜FAIL_INSEN｜📌第26回定時株主総会の継続会の開催日等に関するお知らせ｜17:00
- 3843 Freebit Co., Ltd.｜FAIL_INSEN｜📌過年度の半期報告書の訂正報告書の提出及び過年度の決算短信等の訂正に関するお知らせ｜17:00
- 3843 Freebit Co., Ltd.｜FAIL_INSEN｜📌2026年４月期決算短信の開示が期末後 50日を超えたことに関するお知らせ｜17:00
- 3843 Freebit Co., Ltd.｜FAIL_INSEN｜📌2026年４月期 有価証券報告書の提出完了に関するお知らせ｜17:00
- 3843 Freebit Co., Ltd.｜FAIL_INSEN｜📊2026年４月期  決算短信〔日本基準〕（連結）｜17:00
- 3843 Freebit Co., Ltd.｜FAIL_INSEN｜📌（訂正・数値データ訂正）2026年４月期 第３四半期決算短信〔日本基準〕（連結）の一部訂正に関するお知らせ｜17:00
- 3843 Freebit Co., Ltd.｜FAIL_INSEN｜📌（訂正・数値データ訂正）2026年４月期 第２四半期（中間期）決算短信〔日本基準〕（連結）の一部訂正に関するお知らせ｜17:00
- 4565 Nxera Pharma Co., Ltd.｜FAIL_UWAHIGE｜📌ファブリー病治療薬候補lucerastatの日本およびアジア太平洋の一部地域における独占的ライセンス契約締結のお知らせ｜16:00
- 8871 GOLDCREST Co., Ltd.｜FAIL_INSEN｜📊2027年3月期第2四半期（中間期）決算短信〔日本基準〕（連結）｜15:30
- 4088 Air Water Inc.｜FAIL_INSEN｜📌「改善計画・状況報告書（改訂版）」の公表に関するお知らせ｜15:30
- 8088 岩谷産業｜FAIL_INSEN｜📌コーポレート・ガバナンスに関する報告書 2026/10/28｜19:52
- 1333 Umios Corporation｜FAIL_INSEN｜📌(訂正)法定事後開示書類(会社分割)(大洋エーアンドエフ株式会社)｜15:00
- 6479 ミネベア｜FAIL_INSEN｜📌当社による事業譲受における事業譲受日変更に関するお知らせ｜16:00
- 3234 Mori Hills Reit Investment Corporation｜FAIL_INSEN｜📌不動産投資信託証券に関する発行者等の運用体制に関する報告書 2026/10/28｜16:38
- 3234 Mori Hills Reit Investment Corporation｜FAIL_INSEN｜📌(訂正) 「2026年7月期 決算短信（ＲＥＩＴ）」の一部訂正に関するお知らせ｜16:30
- 2760 東京エレクトロン　デバイス｜FAIL_INSEN｜📌2027年3月期通期連結業績予想の修正並びに剰余金の配当（中間配当）及び期末配当予想の修正（増配）に関するお知らせ｜15:30
- 2760 東京エレクトロン　デバイス｜FAIL_INSEN｜📊2027年3月期　第2四半期（中間期）決算短信〔日本基準〕（連結）｜15:30
- 8098 稲畑産業｜FAIL_INSEN｜📌（訂正）「持分法適用関連会社の異動（子会社化）に関するお知らせ」の一部訂正について｜17:00
- 7725 INTER ACTION Corporation｜FAIL_UWAHIGE｜📌PHPの脆弱性対応に伴う当社Webサイトの公開再開に関するお知らせ｜16:00
- 8095 Astena Holdings Co.,Ltd.｜FAIL_INSEN｜📌株主優待制度における優待区分判定方法の変更に関するお知らせ｜15:00
- 6470 Taiho Kogyo Co., Ltd.｜FAIL_INSEN｜🔁自己株式の取得及び自己株式立会外買付取引（ToSTNeT-3）による自己株式の買付けに関するお知らせ｜16:30
- 3562 No.1 Co., Ltd.｜FAIL_INSEN｜📌2027年２月期第２四半期 決算説明会 「アーカイブ動画」及び「ログミーFinance 書き起こし記事」公開のお知らせ｜17:00
- 4169 Enechange Ltd.｜PASS｜👥主要株主の異動に関するお知らせ｜16:45
- 8927 Meiho Enterprise Co., Ltd.｜PASS｜📌株式会社フィスコによる企業調査レポート公開に関するお知らせ｜15:30
- 4956 Konishi Co., Ltd.｜FAIL_INSEN｜🔁自己株式の取得及び自己株式立会外買付取引（ToSNeT-3）による自己株式の買付けに関するお知らせ｜16:30
- 4373 Simplex Holdings,Inc.｜FAIL_UWAHIGE｜📊2027年３月期 第２四半期（中間期）決算短信〔ＩＦＲＳ〕（連結）｜15:30
- 4373 Simplex Holdings,Inc.｜FAIL_UWAHIGE｜📌通期業績予想の修正に関するお知らせ｜15:30
- 6810 マクセル｜FAIL_INSEN｜📌マクセルと東京科学大学、水分子をセラミックス粒子界面に持つ電解質を用いた次世代電池の共同研究を開始｜15:30
- 1436 GreenEnergy & Company｜FAIL_INSEN｜📦系統用蓄電所システムの工事受注に関するお知らせ｜15:30
- 265A エイチエムコム｜FAIL_INSEN｜📌【補足資料】ドライブバイ方式によるインフラ監視の実現に向けた技術連携 －Braveridge製平面アンテナを活用し、ドライブバイ監視の実用化へ－｜15:30
- 265A エイチエムコム｜FAIL_INSEN｜📌（開示事項の経過）ドライブバイ方式によるインフラ監視の実現に向けた株式会社Braveridgeとの技術連携について｜15:30
- 6857 アドバンテスト｜FAIL_INSEN｜📌2026年度第2四半期決算説明会資料｜15:30
- 6857 アドバンテスト｜FAIL_INSEN｜📌事後交付型譲渡制限付株式ユニット制度に基づく自己株式の処分の払込完了に関するお知らせ｜15:30
- 6857 アドバンテスト｜FAIL_INSEN｜🔁自己株式の取得に係る事項の決定に関するお知らせ｜15:30
- 6857 アドバンテスト｜FAIL_INSEN｜📌2031年満期ユーロ円建転換社債型新株予約権付社債の転換価額の調整に関するお知らせ｜15:30
- 6857 アドバンテスト｜FAIL_INSEN｜📊2027年3月期 第2四半期（中間期）決算短信〔IFRS〕(連結)｜15:30
- 6857 アドバンテスト｜FAIL_INSEN｜📌剰余金の配当（中間配当）に関するお知らせ｜15:30
- 8704 トレイダーズホールディングス｜PASS｜📌トレイダーズ証券「みんなのシストレ」に関する2件の特許取得のお知らせ｜15:30
- 4478 freee K.K.｜PASS｜📌譲渡制限付株式としての自己株式処分及び業績連動型株式報酬制度に基づく自己株式処分の払込完了に関するお知らせ｜16:00

## 📢開示
使用URL: https://kabutan.jp/disclosures/?kubun=&date=20261028&page=1〜43（全43ページ・637行を取得。フォールバックなし）。週末分: なし（前営業日の取得は前夜実行済み）。①-9へ引き渡し9件（recalc_queue）
- 🔁 4956 Konishi Co., Ltd.｜自己株式の取得及び自己株式立会外買付取引（ToSNeT-3）による自己株式の買付けに関するお知らせ｜16:30
- 📢 4956 Konishi Co., Ltd.｜2027年３月期　第２四半期（中間期）業績予想との差異および通期業績予想の上方修正に関するお知らせ｜11:30
- 📊 4956 Konishi Co., Ltd.｜2027年３月期　第２四半期（中間期）決算短信（日本基準）（連結）｜11:30
- 📌 3843 Freebit Co., Ltd.｜再発防止策の実施状況に関するお知らせ｜17:00
- 📌 3843 Freebit Co., Ltd.｜第26回定時株主総会の継続会の開催日等に関するお知らせ｜17:00
- 📌 3843 Freebit Co., Ltd.｜過年度の半期報告書の訂正報告書の提出及び過年度の決算短信等の訂正に関するお知らせ｜17:00
- 📌 3843 Freebit Co., Ltd.｜2026年４月期決算短信の開示が期末後 50日を超えたことに関するお知らせ｜17:00
- 📌 3843 Freebit Co., Ltd.｜2026年４月期 有価証券報告書の提出完了に関するお知らせ｜17:00
- 📊 3843 Freebit Co., Ltd.｜2026年４月期  決算短信〔日本基準〕（連結）｜17:00
- 📌 3843 Freebit Co., Ltd.｜（訂正・数値データ訂正）2026年４月期 第３四半期決算短信〔日本基準〕（連結）の一部訂正に関するお知らせ｜17:00
- 📌 3843 Freebit Co., Ltd.｜（訂正・数値データ訂正）2026年４月期 第２四半期（中間期）決算短信〔日本基準〕（連結）の一部訂正に関するお知らせ｜17:00
- 🔁 6470 Taiho Kogyo Co., Ltd.｜自己株式の取得及び自己株式立会外買付取引（ToSTNeT-3）による自己株式の買付けに関するお知らせ｜16:30
- 📌 6470 Taiho Kogyo Co., Ltd.｜剰余金の配当（中間配当）に関するお知らせ｜14:00
- 📌 6470 Taiho Kogyo Co., Ltd.｜2027年３月期 第２四半期決算概要｜14:00
- 📊 6470 Taiho Kogyo Co., Ltd.｜2027年３月期 第２四半期決算短信〔日本基準〕（連結）｜14:00
- 📌 2760 東京エレクトロン　デバイス｜2027年3月期通期連結業績予想の修正並びに剰余金の配当（中間配当）及び期末配当予想の修正（増配）に関するお知らせ｜15:30
- 📊 2760 東京エレクトロン　デバイス｜2027年3月期　第2四半期（中間期）決算短信〔日本基準〕（連結）｜15:30
- 📊 4373 Simplex Holdings,Inc.｜2027年３月期 第２四半期（中間期）決算短信〔ＩＦＲＳ〕（連結）｜15:30
- 📌 4373 Simplex Holdings,Inc.｜通期業績予想の修正に関するお知らせ｜15:30
- 📌 6857 アドバンテスト｜2026年度第2四半期決算説明会資料｜15:30
- 📌 6857 アドバンテスト｜事後交付型譲渡制限付株式ユニット制度に基づく自己株式の処分の払込完了に関するお知らせ｜15:30
- 🔁 6857 アドバンテスト｜自己株式の取得に係る事項の決定に関するお知らせ｜15:30
- 📌 6857 アドバンテスト｜2031年満期ユーロ円建転換社債型新株予約権付社債の転換価額の調整に関するお知らせ｜15:30
- 📊 6857 アドバンテスト｜2027年3月期 第2四半期（中間期）決算短信〔IFRS〕(連結)｜15:30
- 📌 6857 アドバンテスト｜剰余金の配当（中間配当）に関するお知らせ｜15:30
- 📊 8871 GOLDCREST Co., Ltd.｜2027年3月期第2四半期（中間期）決算短信〔日本基準〕（連結）｜15:30
- 📌 6023 ダイハツインフィニアース｜連結子会社の吸収合併（簡易合併・略式合併）に関するお知らせ｜13:00
- 📊 6023 ダイハツインフィニアース｜2027年3月期 第2四半期（中間期）決算短信〔日本基準〕（連結）｜13:00
- 📌 8628 松井証券｜一部報道について｜12:55
- 📌 8628 松井証券｜剰余金の配当（中間配当）に関するお知らせ｜11:30
- 📌 8628 松井証券｜2027年3月期第2四半期 決算報告資料｜11:30
- 📊 8628 松井証券｜2027年3月期第2四半期（中間期）決算短信〔日本基準〕（非連結）｜11:30
- 📌 3778 SAKURA Internet Inc.｜2027年3月期第2四半期決算説明資料｜12:30
- 📌 3778 SAKURA Internet Inc.｜剰余金の配当（創業30周年記念配当）に関するお知らせ｜12:30
- 📌 3778 SAKURA Internet Inc.｜第２四半期連結業績予想と実績値との差異及び通期連結業績予想の修正に関するお知らせ｜12:30
- 📊 3778 SAKURA Internet Inc.｜2027年3月期第2四半期（中間期）決算短信〔日本基準〕（連結）｜12:30
- 🔁 9824 泉州電業｜自己株式取得に係る事項の決定に関するお知らせ｜14:00
- 🔁 5243 ｎｏｔｅ｜自己株式立会外買付取引（ToSTNeT-3）による自己株式の取得結果及び取得終了に関するお知らせ｜10:00
- 👥 4169 Enechange Ltd.｜主要株主の異動に関するお知らせ｜16:45
- 📦 1436 GreenEnergy & Company｜系統用蓄電所システムの工事受注に関するお知らせ｜15:30
- 📦 336A ダイナミックマッププラットフォーム｜連結子会社における大規模道路データ整備案件の受注に関するお知らせ｜10:00
- 📌 8088 岩谷産業｜コーポレート・ガバナンスに関する報告書 2026/10/28｜19:52
- 📌 3562 No.1 Co., Ltd.｜2027年２月期第２四半期 決算説明会 「アーカイブ動画」及び「ログミーFinance 書き起こし記事」公開のお知らせ｜17:00
- 📌 8098 稲畑産業｜（訂正）「持分法適用関連会社の異動（子会社化）に関するお知らせ」の一部訂正について｜17:00
- 📌 3234 Mori Hills Reit Investment Corporation｜不動産投資信託証券に関する発行者等の運用体制に関する報告書 2026/10/28｜16:38
- 📌 3234 Mori Hills Reit Investment Corporation｜(訂正) 「2026年7月期 決算短信（ＲＥＩＴ）」の一部訂正に関するお知らせ｜16:30
- 📌 4478 freee K.K.｜譲渡制限付株式としての自己株式処分及び業績連動型株式報酬制度に基づく自己株式処分の払込完了に関するお知らせ｜16:00
- 📌 4565 Nxera Pharma Co., Ltd.｜ファブリー病治療薬候補lucerastatの日本およびアジア太平洋の一部地域における独占的ライセンス契約締結のお知らせ｜16:00
- 📌 6479 ミネベア｜当社による事業譲受における事業譲受日変更に関するお知らせ｜16:00
- 📌 7725 INTER ACTION Corporation｜PHPの脆弱性対応に伴う当社Webサイトの公開再開に関するお知らせ｜16:00
- 📌 265A エイチエムコム｜【補足資料】ドライブバイ方式によるインフラ監視の実現に向けた技術連携 －Braveridge製平面アンテナを活用し、ドライブバイ監視の実用化へ－｜15:30
- 📌 265A エイチエムコム｜（開示事項の経過）ドライブバイ方式によるインフラ監視の実現に向けた株式会社Braveridgeとの技術連携について｜15:30
- 📌 276A CCReB Advisors Inc.｜販売用不動産の取得完了に関するお知らせ｜15:30
- 📌 4088 Air Water Inc.｜「改善計画・状況報告書（改訂版）」の公表に関するお知らせ｜15:30
- 📌 6810 マクセル｜マクセルと東京科学大学、水分子をセラミックス粒子界面に持つ電解質を用いた次世代電池の共同研究を開始｜15:30
- 📌 8704 トレイダーズホールディングス｜トレイダーズ証券「みんなのシストレ」に関する2件の特許取得のお知らせ｜15:30
- 📌 8927 Meiho Enterprise Co., Ltd.｜株式会社フィスコによる企業調査レポート公開に関するお知らせ｜15:30
- 📌 9560 PROGRIT, Inc.｜有償ストック・オプション（新株予約権）の発行に関するお知らせ｜15:30
- 📌 1333 Umios Corporation｜(訂正)法定事後開示書類(会社分割)(大洋エーアンドエフ株式会社)｜15:00
- 📌 8095 Astena Holdings Co.,Ltd.｜株主優待制度における優待区分判定方法の変更に関するお知らせ｜15:00
- 📌 4534 Mochida Pharmaceutical Co., Ltd.｜バイオシミラーに関する包括的提携契約締結のお知らせ｜14:00
- 📌 5803 フジクラ｜連結子会社からの配当金受領に関するお知らせ｜14:00
- 📌 8524 North Pacific Bank, Ltd.｜業績予想の修正及び配当予想の修正（増配）に関するお知らせ｜14:00
- 📌 478A Hutzper Inc.｜製造業の技能継承AIを農業へ。農林水産省のAI実装プログラムに選定｜13:30
- 📌 5844 Kyoto Financial Group,Inc.｜コーポレート・ガバナンスに関する報告書 2026/10/28｜13:15
- 📌 5844 Kyoto Financial Group,Inc.｜独立役員届出書｜13:00
- 📌 5844 Kyoto Financial Group,Inc.｜監査等委員である社外取締役の逝去及び退任に関するお知らせ｜13:00
- 📌 218A Liberaware｜東京都が実施する「SusHi Tech Global 成長加速プログラム」採択のお知らせ｜13:05
- 📌 3036 アルコニックス｜アルコニックスグループ、「統合報告書2026」を公開｜11:45
- 📌 6754 アンリツ｜（開示事項の経過）持分法適用関連会社の株式追加取得（連結子会社化）完了に関するお知らせ｜11:30
- 📌 7181 JAPAN POST INSURANCE Co., Ltd.｜2027年3月期第2四半期末の有価証券含み損に関するお知らせ｜11:30
- 📌 147A SORACOM,INC.｜ソラコム、LTE内蔵・組み立て不要の屋外対応クラウド型カメラ「ソラカメ Pro」を販売開始｜11:00
- 📌 3391 TSURUHA Holdings, Inc.｜子どもたちのみらいのために「未来応援プロジェクト２０２６」の 展開企業として参画｜11:00
- 📌 4071 Plus Alpha Consulting Co. LTD.｜CRM/MAツールカスタマーリングスに、 マーケター業務を支援する「AIエージェント」を搭載｜08:59
- 📌 3927 アークン｜フーバーブレイン、PC操作ログ×AI×業務改革コンサルによる新サービス「Work Smart AX」を提供開始｜08:00

## 総当りゲート
### 5手法
- PASS（10）: 6298 Y.A.C.HOLDINGS CO.,LTD.、4058 Toyokumo, Inc.、3077 Horiifoodservice Co., Ltd.、6278 ユニオンツール、6875 メガチップス、6645 OMRON Corporation、6754 アンリツ、6055 Japan Material Co., Ltd.、5310 Toyo Tanso Co., Ltd.、6668 ＡＤプラズマ
- PASS_DOJI（2）: 4377 ONE CAREER Inc.、4477 BASE, Inc.
- FAIL_UWAHIGE（31）: 5136 tripla Co.,Ltd.、5132 pluszero,Inc.、147A SORACOM,INC.、7678 ASAKUMA CO.,LTD.、4412 Science Arts, Inc.、618A KOMPEITO Inc.、3374 Naigai Tec Corporation、446A ノースサンド、2930 北の達人コーポレーション、4565 Nxera Pharma Co., Ltd.、6268 ナブテスコ、6324 Harmonic Drive Systems Inc.、7733 Olympus Corp.、8386 百十四銀行、6370 栗田工業、9412 SKY Perfect JSAT Corporation、5333 ＮＧＫ、268A Rigaku Holdings Corporation、5021 Cosmo Energy Holdings Co., Ltd.、6674 ジーエス・ユアサ　コーポレーション、7220 Musashi Seimitsu Industry Co., Ltd.、2379 dip Corporation、1893 Penta-Ocean Construction Co., Ltd.、1946 Toenec Corporation、1963 日揮ホールディングス、6960 Fukuda Denshi Co., Ltd.、9699 NISHIO HOLDINGS CO. LTD.、7713 シグマ光機、5246 ＥＬＥＭＥＮＴＳ、3994 マネーフォワード、4443 Ｓａｎｓａｎ
- FAIL_INSEN（160）: 6627 Tera Probe, Inc.、5137 Smart Drive Co. Ltd.、276A CCReB Advisors Inc.、6862 ミナトホールディングス、3556 RenetJapanGroup, Inc.、4053 Sun Asterisk, Inc.、4434 Serverworks Co., Ltd.、5027 AnyMind Group Inc.、5757 CK San-Etsu Co., Ltd.、9554 AViC Co. Ltd.、212A FIT EASY Inc.、3915 TerraSky Co., Ltd.、421A Movin' Strategic Career CO.,LTD.、5537 AlbaLink Co.,Ltd.、7047 PORT INC.、5821 Hirakawa Hewtech Corp.、6071 IBJ, Inc.、9560 PROGRIT, Inc.、5034 unerry, Inc.、9268 OPTIMUS GROUP Co., Ltd.、9628 San Holdings,Inc.、2980 SRE Holdings Corp.、505A Geekly,Inc.、4743 ITFOR Inc.、5038 eWeLL Co.,Ltd、6629 TECHNO HORIZON Co., Ltd.、6289 Giken Ltd.、6918 Aval Data Corporation、7567 Sakae Electronics Corp.、6337 Tesec Corporation、3696 セレス、4379 Photosynth inc.、2820 Yamami Co.、3843 Freebit Co., Ltd.、4331 Take and Give. Needs Co., Ltd.、7161 Jimoto Holdings, Inc.、8871 GOLDCREST Co., Ltd.、3391 TSURUHA Holdings, Inc.、5344 MARUWA CO., LTD.、8336 武蔵野銀行、3036 アルコニックス、3222 United Super Markets Holdings, Inc.、1803 Shimizu Corporation、8346 東邦銀行、4088 Air Water Inc.、5301 Tokai Carbon Co., Ltd.、7004 カナデビア、8522 Bank of Nagoya, Ltd.、2874 YOKOREI CO. LTD.、6302 住友重機械工業、8987 Japan Excellent, Inc.、8282 K'S HOLDINGS CORPORATION、6332 月島ホールディングス、8088 岩谷産業、8125 Wakita & Co., Ltd.、7721 Tokyo Keiki Inc.、8278 Fuji Co., Ltd.、8714 池田泉州ホールディングス、8393 Miyazaki Bank Ltd.、8399 琉球銀行、7458 Daiichikosho Co., Ltd.、2782 Seria Co., Ltd.、2809 Kewpie Corporation、4666 Park24 Co., Ltd.、7731 ニコン、3279 Activia Properties, Inc.、8381 San-in Godo Bank Ltd.、8524 North Pacific Bank, Ltd.、3282 Comforia Residential REIT, Inc.、8952 Japan Real Estate Investment Corp.、6925 Ushio Inc.、1861 Kumagai Gumi Co., Ltd.、1417 MIRAIT ONE Corporation、5331 ノリタケ、3148 Create SD Holdings Co., Ltd.、8198 Maxvalu Tokai Co., Ltd.、9882 Yellow Hat Ltd.、1820 Nishimatsu Construction Co., Ltd.、1944 Kinden Corporation、1952 Shin Nippon Air Technologies Co., Ltd.、6269 Modec, Inc.、7003 Mitsui ES Holdings Co., Ltd.、8584 Jaccs Co., Ltd.、1860 Toda Corporation、4966 上村工業、8066 Mitani Corporation、2659 SAN-A CO., LTD.、7984 Kokuyo Co., Ltd.、2805 S&B Foods Inc.、3289 Tokyu Fudosan Holdings Corp.、8818 Keihanshin Building Co., Ltd.、1333 Umios Corporation、1719 HAZAMA ANDO Corporation、1833 Okumura Corporation、9503 Kansai Electric Power Company, Incorporated、3445 RS Technologies Co. Ltd.、6366 Chiyoda Corp.、5844 Kyoto Financial Group,Inc.、6479 ミネベア、6183 BELLSYSTEM24 Holdings, Inc.、6753 Sharp Corporation、8276 HEIWADO CO., LTD.、9974 BELC Co., Ltd.、3234 Mori Hills Reit Investment Corporation、3249 Industrial & Infrastructure Fund Investment Corporation、3283 Nippon Prologis REIT, Inc.、3292 AEON REIT Investment Corp.、3296 NIPPON REIT Investment Corp、3309 Sekisui House Reit. Inc.、3462 Nomura Real Estate Master Fund, Inc.、5482 Aichi Steel Corporation、8953 Japan Metropolitan Fund Investment Corporation、8954 ORIX JREIT Inc.、8955 Japan Prime Realty Investment Corporation、8961 MORI TRUST REIT.Inc、8986 Daiwa Securities Living Investment Corporation、2815 ARIAKE JAPAN Co., Ltd.、5631 Japan Steel Works, Ltd.、9948 Arcs Company, Limited、3105 日清紡ホールディングス、4928 Noevir Holdings Co., Ltd.、9436 Okinawa Cellular Telephone Company、1662 Japan Petroleum Exploration Co., Ltd.、6804 Hosiden Corp.、1969 高砂熱学工業、8585 Orient Corporation、8194 Life Corporation、9533 TOHO GAS Co., Ltd.、8253 Credit Saison Co., Ltd.、8370 紀陽銀行、5831 Shizuoka Financial Group, Inc.、7201 Nissan Motor Co., Ltd.、7381 ＣＣＩグループ、8304 あおぞら銀行、8345 Bank of Iwate Ltd.、8367 南都銀行、3471 Mitsui Fudosan Logistics Park, Inc.、7384 Procrea Holdings,Inc.、8174 NIPPON GAS Co., Ltd.、8334 Gunma Bank, Ltd.、8366 滋賀銀行、3591 WACOAL HOLDINGS CORP、8511 Japan Securities Finance Co., Ltd.、6471 日本精工、7186 横浜フィナンシャルグループ、7322 三十三フィナンシャルグループ、8354 ふくおかフィナンシャルグループ、8359 Hachijuni Nagano Bank, Ltd.、8600 トモニホールディングス、7624 NaITO、5018 ＭＯＲＥＳＣＯ、3498 霞ヶ関Ｃ、7811 中本パックス、6814 古野電、5932 三協立山、3091 ブロンコビリー、3479 ＴＫＰ、6505 東洋電機製造、6532 ベイカレント、4176 ココナラ
- SKIP（0）: なし
### グランビル
- PASS（18）: 8944 Land Business Co., Ltd.、9553 MicroAd, Inc.、5838 Rakuten Bank, Ltd.、6768 Tamura Corporation、4169 Enechange Ltd.、8927 Meiho Enterprise Co., Ltd.、8012 Nagase & Co., Ltd.、4902 Konica Minolta, Inc.、6834 Seikoh Giken Co., Ltd.、4431 スマレジ、6523 PHC Holdings Corp.、3107 ダイワボウホールディングス、336A ダイナミックマッププラットフォーム、3778 SAKURA Internet Inc.、3691 DIGITAL PLUS, Inc.、7715 長野計器、1407 West Holdings Corporation、7175 Imamura Securities Co.Ltd.
- PASS_DOJI（4）: 8697 日本取引所グループ、3563 ＦＯＯＤ　＆　ＬＩＦＥ　ＣＯＭＰＡＮＩＥＳ、9166 GENDA Inc.、8624 Ichiyoshi Securities Co., Ltd.
- FAIL_UWAHIGE（28）: 7725 INTER ACTION Corporation、6255 NPC Incorporated、5036 Japan Business Systems, Inc.、4552 JCR Pharmaceuticals Co., Ltd.、6208 Ishikawa Seisakusho,Ltd.、5532 リアルゲイト、290A ＳＹＮＳＰＥＣＴＩＶＥ、7806 MTG Co., Ltd.、6080 Ｍ＆Ａキャピタルパートナーズ、6613 QD Laser, Inc.、4180 ＡＰＰＩＥＲ　ＧＲＯＵＰ、6570 Kyowa Corporation Co. Ltd.、4373 Simplex Holdings,Inc.、4044 Central Glass Co., Ltd.、456A Human Made Inc.、6027 弁護士ドットコム、8628 松井証券、8995 Makoto Construction Co,Ltd、5242 EYEZ INC.、4100 Toda Kogyo Corp.、8392 大分銀行、6597 HPC SYSTEMS Inc.、3687 Fixstars Corp.、5574 ABEJA,Inc.、7354 Direct Marketing MiX Inc.、4691 Washington Hotel Corp.、8609 岡三証券グループ、8739 スパークス・グループ
- FAIL_INSEN（157）: 5254 Arent, Inc.、3927 アークン、6905 Cosel Co., Ltd.、2986 LA Holdings Co.,Ltd、9211 f-code Inc.、6562 Geniee, Inc.、6473 JTEKT Corporation、3496 アズーム、4534 Mochida Pharmaceutical Co., Ltd.、8793 ＮＥＣキャピタルソリューション、3405 クラレ、7744 Noritsu Koki Co., Ltd.、8095 Astena Holdings Co.,Ltd.、9064 ヤマトホールディングス、3741 Systems Engineering Consultants Co., Ltd.、4544 H.U.Group Holdings, Inc.、7970 Shin-Etsu Polymer Co., Ltd.、6470 Taiho Kogyo Co., Ltd.、4763 クリーク・アンド・リバー社、7199 プレミアグループ、4848 フルキャストホールディングス、3935 Edia Co. Ltd.、6196 Strike Group Co. Ltd.、3562 No.1 Co., Ltd.、8061 Seika Corporation、2331 ALSOK CO., LTD.、4568 第一三共、3661 m-up holdings, Inc.、6432 竹内製作所、6988 日東電工、7747 朝日インテック、8020 Kanematsu Corporation、9828 Genki Global Dining Concepts Corp、6454 Max Co., Ltd.、2288 Marudai Food Co., Ltd.、8014 Chori Co., Ltd.、3549 クスリのアオキホールディングス、4549 Eiken Chemical Co., Ltd.、5184 ニチリン、6371 Tsubakimoto Chain Co.、6592 Mabuchi Motor Co., Ltd.、4166 Cacco, Inc.、8850 スターツコーポレーション、9163 Nareru Group Inc.、186A Astroscale Holdings Inc.、3569 セーレン、4183 Mitsui Chemicals, Inc.、4272 Nippon Kayaku Co., Ltd.、4956 Konishi Co., Ltd.、7181 JAPAN POST INSURANCE Co., Ltd.、7269 スズキ、5461 Chubu Steel Plate Co., Ltd.、7513 Kojima Co., Ltd.、7734 Riken Keiki Co., Ltd.、4617 中国塗料、5233 太平洋セメント、6328 Ebara Jitsugyo Co., Ltd.、8081 Kanaden Corporation、9837 Morito Co., Ltd.、7751 キヤノン、6770 Alps Alpine Co., Ltd.、5105 ＴＯＹＯ　ＴＩＲＥ、8167 リテールパートナーズ、1815 鉄建建設、4375 セーフィー、8424 芙蓉総合リース、7921 ＴＡＫＡＲＡ　＆　ＣＯＭＰＡＮＹ、4912 ライオン、2871 ニチレイ、4401 ＡＤＥＫＡ、9842 アークランズ、4937 Ｇ−ＷＡＱＯＯ、5243 ｎｏｔｅ、8008 Yondoshi Holdings, Inc.、4382 HEROZ, Inc.、3156 レスター、8051 山善、7856 HAGIHARA INDUSTRIES INC.、1879 新日本建設、5892 ＹＵＴＯＲＩ、6736 Suncorporation、9902 Nichiden Corporation、6023 ダイハツインフィニアース、3106 倉敷紡績、2767 円谷フィールズホールディングス、4667 Aisan Technology Co., Ltd.、6250 Yamabiko Corporation、7609 ダイトロン、9304 澁澤倉庫、2602 日清オイリオグループ、4413 baudroie,inc.、8919 カチタス、8410 Seven Bank, Ltd.、7616 Colowide Co., Ltd.、6340 澁谷工業、7350 Okinawa Financial Group, Inc.、4475 HENNGE K.K.、6058 VECTOR Inc.、3097 Monogatari Corporation、6998 Nippon Tungsten Co., Ltd.、5985 SUNCALL CORPORATION、1518 三井松島ホールディングス、4208 UBE Corporation、6379 RAIZNEXT Corporation、9044 NANKAI Co., Ltd.、7504 Kohsoku Corporation、9509 Hokkaido Electric Power Company,Incorporated、6072 Jibannet Holdings Co., Ltd.、7630 Ichibanya Co., Ltd.、8043 Starzen Company Limited、9505 Hokuriku Electric Power Company、9616 共立メンテナンス、9900 Sagami Holdings Corp.、8255 Axial Retailing, Inc.、9536 SAIBU GAS HOLDINGS CO. LTD.、8097 SAN-AI OBBLI CO. LTD、8059 Daiichi Jitsugyo Co., Ltd.、8361 Ogaki Kyoritsu Bank, Ltd.、8343 Akita Bank, Ltd.、6810 マクセル、8362 Fukui Bank, Ltd.、8137 サンワテクノス、8622 Mito Securities Co., Ltd.、6769 Thine Electronics, Inc.、479A PRONI Inc.、1436 GreenEnergy & Company、2122 インタースペース、6963 ROHM Company Limited、150A ＪＳＨ、8364 清水銀行、6490 ＰＩＬＬＡＲ、477A Startline CO.,LTD.、6336 石井表記、2354 YE DIGITAL CORPORATION、8344 Yamagata Bank, Ltd.、9278 BOOKOFF GROUP HOLDINGS LIMITED、7256 河西工業、4997 日本農薬、278A Ｔｅｒｒａ　Ｄｒｏｎｅ、4346 NEXYZ.Group Corporation、2681 2nd RETAILING Co., Ltd.、4082 第一稀元素化学工業、3653 Morpho, Inc.、3907 Silicon Studio Corp.、4440 WITZ Corp.、8163 SRS HOLDINGS CO.,LTD.、6203 Howa Machinery, Ltd.、6522 アスタリスク、8360 Yamanashi Chuo Bank, Ltd.、7380 Juroku Financial Group,Inc.、8368 Hyakugo Bank, Ltd.、8713 Fidea Holdings Co.Ltd.、3891 ニッポン高度紙工業、6840 ＡＫＩＢＡホールディングス、6890 Ferrotec Corporation、8377 ほくほくフィナンシャルグループ、9697 カプコン
- SKIP（0）: なし
### 変化点
- PASS（5）: 7695 交換できるくん、9962 ミスミグループ本社、8704 トレイダーズホールディングス、4488 AI inside Inc.、4478 freee K.K.
- PASS_DOJI（2）: 6136 OSG CORP、5582 （名称取得不可）
- FAIL_UWAHIGE（8）: 4187 大阪有機化学工業、7318 セレンディップ・ホールディングス、5590 NETSTARS Co.,Ltd.、9343 アイビス、4165 PLAID Inc.、4418 Japan Data Science Consortium Co Ltd.、598A チャットプラス、3993 PKSHA Technology, Inc.
- FAIL_INSEN（18）: 265A エイチエムコム、5803 フジクラ、4011 Headwaters Co.,Ltd、9888 UEX LTD、584A LiNKX, Inc.、6857 アドバンテスト、8151 東陽テクニカ、4368 4368、478A Hutzper Inc.、6284 日精エー・エス・ビー機械、218A Liberaware、6785 鈴木、4498 Cybertrust Japan Co., Ltd.、4071 Plus Alpha Consulting Co. LTD.、4493 Cyber Security Cloud, Inc.、339A PROGRESS TECHNOLOGIES GROUP INC、4259 ExaWizards Inc.、593A ティアフォー
- SKIP（0）: なし
### AI特需
- PASS（6）: 6521 オキサイド、4062 イビデン、7729 東京精密、6752 パナソニックHD、5706 三井金属鉱業、6590 芝浦メカトロニクス
- PASS_DOJI（0）: なし
- FAIL_UWAHIGE（7）: 9824 泉州電業、6254 野村マイクロ・サイエンス、4047 関東電化工業、4971 メック、6981 村田製作所、6235 オプトラン、6643 戸上電機製作所
- FAIL_INSEN（18）: 3131 シンデン・ハイテックス、2760 東京エレクトロン　デバイス、1982 日比谷総合設備、9960 トーテック、3110 日東紡、7433 伯東、6524 湖北工業、6779 Nihon Dempa Kogyo Co., Ltd.、6787 メイコー、6227 AIMECHATEC Ltd.、4658 日本空調サービス、8098 稲畑産業、5208 Arisawa Mfg.Co., Ltd.、3433 TOCALO Co., Ltd.、3103 ユニチカ、5302 日本カーボン、9432 NTT、4203 住友ベークライト
- SKIP（0）: なし
### 除籍（first_seenから30暦日超）
なし

## 機械詳細
- 派生ファイル: grades.json 948銘柄/534.5KiB（nx非null 752・lx 409・pxd 301）、pool_bars.json 475銘柄/406.7KiB、earnings_calendar.json 956銘柄/125.2KiB（nx非null 757・次回決算日 付与 757件）
- gate_history: gate_history/2026-10-28.json を新規作成（verdicts 474件=評価474件／nominations 87件）
- 抜粋規則: 通知【通過】10件（method/ai/granville/changepoint の群別ラウンドロビン）。PASS群別内訳 method12/ai6/granville22/changepoint7
- method_score 保持56件/null418件
- ヘッドライン付与 47件（PASS全件47と一致: True）
- kabutan 取得: 決算ページ50件・トップページ9件（業態/業種の新規取得は上限50件に対し9件・打ち切り0件）。業種の埋め戻し 0件（プール在籍で未付与だった銘柄。残り 9件）
- profile_cache 総数930・本夜追加0件・業態が「未取得」のまま出た件数 0
- earnings_log 総数96／本夜追記10件／リターン補完7件／日足が取れず未補完24件
- gyoseki_cache 再計算 1件（history 退避 1件）: 3778（📊決算発表・強制再計算）
- 鮮度ゲート: 鮮度切れ除外5件・nom_age分布 0-2:137/3-10:215/11+:122・last_seen欠損0件
- 記録の凍結: verdicts 474件・nominations 87件（新規15・再指名72）・業種 付与済み465/未付与9
- トレンド文脈: ctx {'不一致': 214, 'レンジ': 143, '合致': 111, '判定不能': 6}・PASS のうち ctx 合致 8件・形態が付いた銘柄 216件
- 3日ルール: 判定3銘柄・streak≥3 2・streak=2 0・判定不可0
- 業種別PER中央値: 算出26業種・spm 付与 894銘柄
- 開示の分類別件数: 📢1/📉0/📊10/🔁5/👥1/🏛0/📦2/📌57（日本語見出しのみ・英文併記は除外）
- 熟成由来(value_gap)の候補 0件（watchlist に nominate_for=2026-10-28 なし）
- 権利情報: rights_cache 総数462・本夜 配当更新11件／優待取得 0件（取得元がプロキシ403のため全て不明のまま）
- 次回決算日: 付与757件／未発表199件・前年同期発表日 付与301件
- STEP 4.8 週末ブリーフ: スキップ（week_open=false）
- master.json の変更行数: +10677/-9568（indent=2・往復一致）
- 3日ルール(保有): 判定3銘柄・streak≥3 2・streak=2 0・判定不可0
