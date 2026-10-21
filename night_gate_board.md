# 夜間ゲート 2026-10-21

## サマリー
- 評価数: 399 / PASS: 79（PASS_DOJI含め79）
- 発注可能提案数: 54件
- 市場一言: 市場モード「レンジ様子見」（market.latest 2026-10-20）。プール399銘柄中PASS比率19.8%（陰線FAIL 217件・上髭FAIL 103件）
- 実行モード: 通常（base_day=当日の引け値を対象）
- base_day: 2026-10-21（run_at 2026-10-21 20:48起動）
- week_open: false（翌営業日10/22(木)は週初でない）→ STEP 4.8 週末ブリーフはスキップ
- 📆 翌営業日 10/22(木): カレンダーイベントなし。T+2 10/23(金): カレンダーイベントなし。次の TOPIX 低減日 10/30(金) 第1回/8（あと7営業日）
- 📑指数: 低減対象 提案7件／PASS14件／プール62件・新規採用 16件（index_flags 2026-10-07 公表分）

## 検証結果
- V1 → はい（proposals54=results54=template54・通知母数54）
- V2 → はい（PASS79=提案54+除外25・order_status欠落0）
- V3 → はい（results399件重複0）
- V4 → はい（既存static変更0件（新規static付与4件は新規銘柄））
- V5 → はい（許可キー外の変更0件[]・profile既存改変0/sector上書き0）
- V6 → はい（不整合0件）
- V10 → はい（base_day 5箇所=['2026-10-21']）
- V12 → はい（proposals/template/results 同順）
- V14 → はい（保持67件/null332件・出所不明/不一致0件）
- V15 → はい（PASS79件中79件付与・欠落0・語句違反0（業態「未取得」2件））
- V16 → はい（決算発表1件→earnings_log総数71・追記1・再計算前値保存(b)該当0・history超過0）
- V18 → はい（提案54件・鮮度切れ除外13件・誤除外0）
- V19 → はい（verdicts399=評価399・nominations102=pool last_seen・ctx {'不一致': 163, 'レンジ': 136, '合致': 96, '判定不能': 4}・写し漏れ0・既存gyotai変更0）
- V11 → いいえ（+7940/-6472（myers）／patience +8075/-6607（indent=2・往復一致で検出・results全置換399件とcache更新による。全体再フォーマットではない））
- V9 → はい（gate_history/2026-10-21.json 新規作成・残りキー一致 True）
- V13 → いいえ（891銘柄/451.1KiB（461949B）・和集合891・15キー欠落0・nx不一致0・ix 186/186・業種中央値25業種再計算一致True（サイズ上限450KiBを僅差超過））
- V17 → はい（401銘柄/343KiB・保有4銘柄すべて収録・3日ルール判定4銘柄）
- V20 → はい（903銘柄/92KiB・nx非null724・hist持ち261・pxd166）
- V7 → はい（必須セクションすべて存在（週初でないため今週のカタリスト不要））
- V8 → はい（模擬54行の書式OK）
- LEAK → はい（公開物の保有情報漏えい0件（board0/gate_history0/today0）保有4銘柄中プール外2件）

## 保有アラート
保有4銘柄・アラート12件（詳細は通知）

## 前夜の結果
PL5口座への正式な反映は週次①-11の採点で行われる。ここは参考情報。
前夜2026-10-20の提案22件 → 約定20・不約定2・判定不能0
- 3391 reversal 指定2258.5 → 約定2236.5・終値2185.5（-2.28%）
- 3222 reversal 指定759 → 約定756・終値754（-0.26%）
- 7733 reversal 指定1730 → 約定1730・終値1698.5（-1.82%）
- 8278 reversal 指定1959 → 約定1959・終値1953（-0.31%）
- 2809 reversal 指定4571 → 約定4571・終値4529（-0.92%）
- 3148 reversal 指定3215 → 約定3200・終値3180（-0.62%）
- 1860 reversal 指定1405 → 約定1405・終値1404.5（-0.04%）
- 7984 reversal 指定890.3 → 約定890.3・終値883.5（-0.76%）
- 9503 reversal 指定2723 → 約定2723・終値2730（+0.26%）
- 6753 reversal 指定590.6 → 約定590.6・終値594（+0.58%）
- 8276 reversal 指定2556 → 約定2556・終値2546（-0.39%）
- 9948 reversal 指定3440 → 約定3435・終値3440（+0.15%）
- 9974 reversal 指定6230 → 約定6230・終値6230（+0.00%）
- 2815 reversal 指定5270 → 約定5270・終値5220（-0.95%）
- 8194 reversal 指定2381 → 約定2366・終値2378（+0.51%）
- 8174 reversal 指定937.5 → 約定937.5・終値928.8（-0.93%）
- 3591 reversal 指定3578 → 約定3578・終値3557（-0.59%）
- 9432 reversal 指定177.1 → 約定176・終値176.2（+0.11%）
- 4544 momentum 指定3720 → 約定3749・終値3718（-0.83%）
- 5242 reversal 指定2866 → 約定2866・終値2868（+0.07%）

## 模擬テンプレ
```
# base_day 2026-10-21 ／ 提案54件
# 使い方: 参戦する0〜3銘柄の行だけをコピーし、｜の後ろに参戦理由を書いてポジション株PJへ送る。
# 選ばなかった行は送らなくてよい（全行に理由を書く必要はない）。見送りは末尾の1行で足りる。
# 特定銘柄を理由つきで見送る場合のみ『模擬 見送り {code} ｜{理由}』を送る。
模擬 5137 kenmo_momentum 逆指値313 SL293.3 単元100 ｜
模擬 5136 kenmo_momentum 逆指値2724 SL2559.6 単元100 ｜
模擬 5757 kenmo_momentum 逆指値4740 SL4450.9 単元100 ｜
模擬 618A kenmo_momentum 逆指値1913 SL1797.3 単元100 ｜
模擬 421A kenmo_momentum 逆指値4485 SL4211.2 単元100 ｜
模擬 5537 kenmo_momentum 逆指値3940 SL3698.9 単元100 ｜
模擬 4477 kenmo_momentum 逆指値390 SL365.7 単元100 ｜
模擬 505A kenmo_momentum 逆指値1159 SL1088.5 単元100 ｜
模擬 3798 kenmo_momentum 逆指値543 SL509.5 単元100 ｜
模擬 5038 kenmo_momentum 逆指値2331 SL2190.2 単元100 ｜
模擬 7567 kenmo_newhigh 逆指値639 SL599.7 単元100 ｜
模擬 3843 kenmo_newhigh 逆指値1772 SL1664.7 単元100 ｜
模擬 7161 kenmo_newhigh 逆指値589 SL552.7 単元100 ｜
模擬 8393 choruko_reversal 指値2462 SL2328 単元100 ｜
模擬 1820 choruko_reversal 指値5287 SL5115 単元100 ｜
模擬 1952 choruko_reversal 指値2986 SL2912 単元100 ｜
模擬 6269 choruko_reversal 指値8027 SL7957 単元100 ｜
模擬 6183 choruko_reversal 指値1339 SL1253 単元100 ｜
模擬 5631 choruko_reversal 指値6460 SL6347 単元100 ｜
模擬 1662 choruko_reversal 指値1699 SL1655 単元100 ｜
模擬 8194 choruko_reversal 指値2378 SL2306 単元100 ｜
模擬 7381 choruko_reversal 指値1176 SL1136 単元100 ｜
模擬 8345 choruko_reversal 指値2198 SL2106 単元100 ｜
模擬 8399 choruko_reversal 指値2863 SL2769 単元100 ｜
模擬 7384 choruko_reversal 指値4230 SL4090 単元100 ｜
模擬 8304 choruko_reversal 指値3103 SL3035 単元100 ｜
模擬 9824 ai_momentum 逆指値8190 SL7689.2 単元100 ｜
模擬 6643 ai_reversal 指値5270 SL5070 単元100 ｜
模擬 5254 granville_tenkan 逆指値4100 SL3849.3 単元100 ｜
模擬 6905 granville_tenkan 逆指値1352 SL1269.9 単元100 ｜
模擬 9064 granville_tenkan 逆指値2062 SL1937.3 単元100 ｜
模擬 186A granville_tenkan 逆指値1084 SL1018 単元100 ｜
模擬 6328 granville_tenkan 逆指値2473 SL2323.7 単元100 ｜
模擬 456A granville_oshime 指値1858.6 SL1849.4 単元100 ｜
模擬 9166 granville_oshime 指値673.5 SL670.1 単元100 ｜
模擬 3691 granville_rebound 指値1693 SL1624 単元100 ｜
模擬 6963 granville_rebound 指値3958 SL3888 単元100 ｜
模擬 8524 granville_rebound 指値1159 SL1130 単元100 ｜
模擬 3653 granville_rebound 指値907 SL848 単元100 ｜
模擬 8360 granville_rebound 指値1301 SL1249 単元100 ｜
模擬 3778 granville_rebound 指値3160 SL3100 単元100 ｜
模擬 8366 granville_rebound 指値2694 SL2623 単元100 ｜
模擬 8368 granville_rebound 指値2186 SL2111 単元100 ｜
模擬 8713 granville_rebound 指値2433 SL2317 単元100 ｜
模擬 4011 変化点🔔 指値2238 SL2115 単元100 🔒 ｜
模擬 7695 変化点🔔 指値885 SL825 単元100 🔒 ｜
模擬 4382 変化点🔔 指値1631 SL1315 単元100 🔒 ｜
模擬 9888 変化点 指値1182 SL1160 単元100 🔒 ｜
模擬 5590 変化点🔔 指値675 SL672 単元100 🔒 ｜
模擬 478A 変化点🔔 指値680 SL662 単元100 🔒 ｜
模擬 218A 変化点 指値930 SL911 単元100 🔒 ｜
模擬 593A 変化点 指値2010 SL1927 単元100 🔒 ｜
模擬 4498 変化点🔔 指値2060 SL1480 単元100 🔒 ｜
模擬 339A 変化点 指値825 SL818 単元100 🔒 ｜
模擬 見送り ｜
```

## PASS内訳
PASS 79件 = 発注可能 54件 + 除外 25件（型不一致10/材料後出し0/鮮度切れ13/その他2）
- 276A CCReB Advisors Inc.｜⛔要確認(足が不整合: 高値<始値/終値 または 安値>始値/終値)
- 3498 霞ヶ関Ｃ｜⛔提案なし(手法ブランチ不明)
- 6613 QD Laser, Inc.｜⛔型不一致: 既に支持帯以下
- 8336 Musashino Bank, Ltd.｜⛔型不一致: 既に支持帯以下
- 7609 Daitron Co., Ltd.｜⛔型不一致: 既に支持帯以下
- 8919 カチタス｜⛔型不一致: 既に支持帯以下
- 5985 SUNCALL CORPORATION｜⛔型不一致: 既に支持帯以下
- 8361 Ogaki Kyoritsu Bank, Ltd.｜⛔型不一致: 既に支持帯以下
- 8343 Akita Bank, Ltd.｜⛔型不一致: 既に支持帯以下
- 8367 Nanto Bank Ltd.｜⛔型不一致: 既に支持帯以下
- 8362 Fukui Bank, Ltd.｜⛔型不一致: 既に支持帯以下
- 8622 Mito Securities Co., Ltd.｜⛔型不一致: 既に支持帯以下
- 鮮度切れ（コードとnom_age）: 5821(14営業日)、269A(18営業日)、4331(12営業日)、3186(13営業日)、1945(16営業日)、8793(15営業日)、6988(14営業日)、2413(12営業日)、7504(16営業日)、6072(12営業日)、9616(14営業日)、4997(11営業日)、4346(12営業日)

## 5手法銘柄
- 6627 Tera Probe, Inc.｜kenmo_momentum｜🚀確変(13)｜💎割安｜FAIL_INSEN｜1,985円｜💰21.1万円｜—
- 5137 Smart Drive Co. Ltd.｜kenmo_momentum｜🚀確変(12)｜💎割安｜PASS｜310円｜💰3.1万円｜momentum 313 想定損失幅6.3%。｜📋カルテ窓 11/13(残16営業日)
  > 【業態】モビリティデータ活用の車両管理サービス提供。自動車、保険会社向け支援も。
  > 【いま】終値310円・直近5日+0.00%（材料未確認）
  > 【調子】🚀確変（12/13）
  > 【水準】💎割安（6.0/7）— PER12.97倍・PEG0.1352・52週34.2% ／ 💰単元3.1万円
  > 【戦略】当日高値超えの逆指値313円で順張り参戦を検討。上限316.1円・SL293.3円目安
- 276A CCReB Advisors Inc.｜kenmo_momentum｜🚀確変(12)｜⚪妥当｜PASS｜4,480円｜💰44.8万円｜—｜⚠日程不明｜⛔要確認(足が不整合: 高値<始値/終値 または 安値>始値/終値)
  > 【業態】AIを活用した企業不動産(CRE)に関するソリューションの提供などを手掛ける。
  > 【いま】終値4,480円・直近5日+8.87%・📌2026年8月期 決算説明会 WEB動画配信に関するお知らせ
  > 【調子】🚀確変（12/13）
  > 【水準】⚪妥当（4.0/7）— PER16.48倍・PEG0.1847・52週51.8% ／ 💰単元44.8万円
  > 【戦略】発注対象外（⛔要確認(足が不整合: 高値<始値/終値 または 安値>始値/終値)）
- 6862 Minato Holdings Inc.｜kenmo_momentum｜🚀確変(11)｜🟢値頃｜FAIL_INSEN｜4,330円｜💰47.0万円｜—
- 4053 Sun Asterisk, Inc.｜kenmo_momentum｜🚀確変(11)｜⚪妥当｜FAIL_UWAHIGE｜586円｜💰5.8万円｜—
- 4434 Serverworks Co., Ltd.｜kenmo_momentum｜🚀確変(11)｜⚪妥当｜FAIL_INSEN｜3,045円｜💰30.4万円｜—
- 5027 AnyMind Group Inc.｜kenmo_momentum｜🚀確変(11)｜⚪妥当｜FAIL_UWAHIGE｜786円｜💰8.1万円｜—
- 5136 tripla Co.,Ltd.｜kenmo_momentum｜🚀確変(11)｜⚪妥当｜PASS｜2,703円｜💰27.0万円｜momentum 2724 想定損失幅6.0%。｜⚠日程不明
  > 【業態】宿泊予約システムや会話ツールのAIチャットボットシステム提供。決済システムも。アジアに拡大。
  > 【いま】終値2,703円・直近5日+1.20%（材料未確認）
  > 【調子】🚀確変（11/13）
  > 【水準】⚪妥当（3.0/7）— PER26.71倍・PEG0.4527・52週93.5% ／ 💰単元27.0万円
  > 【戦略】当日高値超えの逆指値2724円で順張り参戦を検討。上限2751.2円・SL2559.6円目安
- 5757 CK San-Etsu Co., Ltd.｜kenmo_momentum｜🔥絶好調(10)｜💎割安｜PASS_DOJI｜4,685円｜💰46.9万円｜momentum 4740 想定損失幅6.1%。｜📋カルテ窓 11/13(残16営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
  > 【業態】黄銅棒・黄銅線で国内首位。精密部品、配管も。日本伸銅を子会社化。
  > 【いま】終値4,685円・直近5日-6.30%（材料未確認）
  > 【調子】🔥絶好調（10/13）
  > 【水準】💎割安（6.0/7）— PER5.96倍・PEG0.0769・52週45.2% ／ 💰単元46.9万円
  > 【戦略】当日高値超えの逆指値4740円で順張り参戦を検討。上限4787.4円・SL4450.9円目安
- 212A FIT EASY Inc.｜kenmo_momentum｜🔥絶好調(10)｜⚪妥当｜FAIL_INSEN｜2,827円｜💰28.5万円｜—
- 618A KOMPEITO Inc.｜kenmo_momentum｜🔥絶好調(10)｜⚪妥当｜PASS｜1,889円｜💰18.9万円｜momentum 1913 想定損失幅6.0%。｜⚠日程不明
  > 【業態】設置型の健康社食サービス「OFFICE DEYASAI」などの企画・運営を手掛ける。
  > 【いま】終値1,889円・直近5日-7.22%（材料未確認）
  > 【調子】🔥絶好調（10/13）
  > 【水準】⚪妥当（4.0/7）— PER18.32倍・PEG0.1973・52週61.5% ／ 💰単元18.9万円
  > 【戦略】当日高値超えの逆指値1913円で順張り参戦を検討。上限1932.1円・SL1797.3円目安
- 9554 AViC Co. Ltd.｜kenmo_momentum｜🔥絶好調(10)｜⚪妥当｜FAIL_UWAHIGE｜1,609円｜💰17.2万円｜—
- 421A Movin' Strategic Career CO.,LTD.｜kenmo_momentum｜🔥絶好調(10)｜⚪妥当｜PASS｜4,430円｜💰44.3万円｜momentum 4485 想定損失幅6.1%。｜📋カルテ窓 11/11(残14営業日)
  > 【業態】サービス業（人材紹介・転職支援・コンサルティング関連）
  > 【いま】終値4,430円・直近5日+11.87%（材料未確認）
  > 【調子】🔥絶好調（10/13）
  > 【水準】⚪妥当（3.0/7）— PER21.37倍・PEG0.4106・52週94.5% ／ 💰単元44.3万円
  > 【戦略】当日高値超えの逆指値4485円で順張り参戦を検討。上限4529.9円・SL4211.2円目安
- 5132 pluszero,Inc.｜kenmo_momentum｜🔥絶好調(9)｜🟢値頃｜FAIL_UWAHIGE｜1,957円｜💰19.6万円｜—
- 6298 Y.A.C.HOLDINGS CO.,LTD.｜kenmo_momentum｜🔥絶好調(9)｜🟢値頃｜FAIL_INSEN｜1,141円｜💰11.6万円｜—
- 4377 ONE CAREER Inc.｜kenmo_momentum｜🔥絶好調(9)｜⚪妥当｜FAIL_UWAHIGE｜2,632円｜💰26.7万円｜—
- 5537 AlbaLink Co.,Ltd.｜kenmo_momentum｜🔥絶好調(9)｜⚪妥当｜PASS｜3,895円｜💰39.0万円｜momentum 3940 想定損失幅6.1%。｜📋カルテ窓 11/12(残15営業日)
  > 【業態】流動性が低下している不動産の買取再販やコンサルティングなどを手掛ける。
  > 【いま】終値3,895円・直近5日+3.18%（材料未確認）
  > 【調子】🔥絶好調（9/13）
  > 【水準】⚪妥当（3.0/7）— PER22.39倍・PEG0.5085・52週90.2% ／ 💰単元39.0万円
  > 【戦略】当日高値超えの逆指値3940円で順張り参戦を検討。上限3979.4円・SL3698.9円目安
- 9556 INTLOOP, Inc.｜kenmo_momentum｜🔥絶好調(8)｜💎割安｜FAIL_INSEN｜2,180円｜💰22.6万円｜—
- 7047 PORT INC.｜kenmo_momentum｜🔥絶好調(8)｜💎割安｜FAIL_INSEN｜2,088円｜💰21.7万円｜—
- 3915 TerraSky Co., Ltd.｜kenmo_momentum｜🔥絶好調(8)｜🟢値頃｜FAIL_UWAHIGE｜2,489円｜💰22.2万円｜—
- 5821 Hirakawa Hewtech Corp.｜kenmo_momentum｜⚡好調(7)｜💎割安｜PASS｜3,095円｜💰30.9万円｜—｜📑TOPIX低減対象（次 10/30 第1回/8）｜⛔提案なし(指名鮮度切れ 14営業日)
  > 【業態】電線・放送機器メーカー。光中継システム等。医療用チューブも展開。海外でも生産。
  > 【いま】終値3,095円・直近5日-5.21%（材料未確認）
  > 【調子】⚡好調（7/13）
  > 【水準】💎割安（6.0/7）— PER11.74倍・PEG0.5134・52週36.5% ／ 💰単元30.9万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 14営業日)）
- 4058 Toyokumo, Inc.｜kenmo_momentum｜⚡好調(7)｜⚪妥当｜FAIL_UWAHIGE｜2,308円｜💰23.1万円｜—
- 6071 IBJ, Inc.｜kenmo_momentum｜⚡好調(7)｜⚪妥当｜FAIL_UWAHIGE｜912円｜💰9.3万円｜—
- 5034 unerry, Inc.｜kenmo_momentum｜⚡好調(7)｜⚪妥当｜FAIL_INSEN｜2,700円｜💰27.7万円｜—
- 9560 PROGRIT, Inc.｜kenmo_momentum｜⚡好調(7)｜⚪妥当｜FAIL_INSEN｜1,081円｜💰11.2万円｜—
- 558A SQUEEZE Inc.｜kenmo_momentum｜⚡好調(7)｜🟡やや割高｜FAIL_UWAHIGE｜5,660円｜💰58.2万円｜—
- 147A SORACOM,INC.｜kenmo_momentum｜⚡好調(7)｜🟡やや割高｜FAIL_UWAHIGE｜969円｜💰9.8万円｜—
- 7678 ASAKUMA CO.,LTD.｜kenmo_momentum｜⚡好調(7)｜🔴過熱｜FAIL_UWAHIGE｜3,765円｜💰37.9万円｜—
- 9268 OPTIMUS GROUP Co., Ltd.｜kenmo_momentum｜⚡好調(6)｜💎割安｜FAIL_UWAHIGE｜341円｜💰3.5万円｜—
- 4477 BASE, Inc.｜kenmo_momentum｜⚡好調(6)｜🟡やや割高｜PASS｜387円｜💰3.9万円｜momentum 390 想定損失幅6.2%。｜⚠日程不明
  > 【業態】個人・小規模企業向けECプラットフォーム「BASE」、オンライン決済サービス「PAY.JP」運営。
  > 【いま】終値387円・直近5日+0.00%（材料未確認）
  > 【調子】⚡好調（6/13）
  > 【水準】🟡やや割高（2.0/7）— PER29.77倍・PEG1.2712・52週79.4% ／ 💰単元3.9万円
  > 【戦略】当日高値超えの逆指値390円で順張り参戦を検討。上限393.9円・SL365.7円目安
- 9628 San Holdings,Inc.｜kenmo_momentum｜⚡好調(6)｜🟡やや割高｜FAIL_INSEN｜1,234円｜💰13.3万円｜—
- 2980 SRE Holdings Corp.｜kenmo_momentum｜⚡好調(5)｜🟢値頃｜FAIL_INSEN｜2,304円｜💰23.9万円｜—
- 4412 Science Arts, Inc.｜kenmo_momentum｜⚡好調(5)｜⚪妥当｜FAIL_UWAHIGE｜1,396円｜💰14.4万円｜—
- 505A Geekly,Inc.｜kenmo_momentum｜✅順調(4)｜💎割安｜PASS｜1,156円｜💰11.6万円｜momentum 1159 想定損失幅6.1%。｜⚠日程不明
  > 【業態】IT・Web・ゲーム業界に特化した人材紹介(転職エージェント)事業を手掛ける。
  > 【いま】終値1,156円・直近5日-15.93%（材料未確認）
  > 【調子】✅順調（4/13）
  > 【水準】💎割安（7.0/7）— PER8.21倍・PEG0.4676・52週16.6% ／ 💰単元11.6万円
  > 【戦略】当日高値超えの逆指値1159円で順張り参戦を検討。上限1170.6円・SL1088.5円目安
- 3798 ULS Group Incorporated｜kenmo_momentum｜✅順調(4)｜💎割安｜PASS｜541円｜💰5.4万円｜momentum 543 想定損失幅6.2%。｜📋カルテ窓 11/06(残11営業日)
  > 【業態】ITシステムの設計・構築・コンサルを展開。流通・製造・情報サービス業向けが中心。
  > 【いま】終値541円・直近5日+1.88%（材料未確認）
  > 【調子】✅順調（4/13）
  > 【水準】💎割安（6.0/7）— PER13.33倍・PEG0.6407・52週21.4% ／ 💰単元5.4万円
  > 【戦略】当日高値超えの逆指値543円で順張り参戦を検討。上限548.4円・SL509.5円目安
- 5038 eWeLL Co.,Ltd｜kenmo_momentum｜✅順調(4)｜⚪妥当｜PASS｜2,314円｜💰23.1万円｜momentum 2331 想定損失幅6.0%。｜📋カルテ窓 11/13(残16営業日)
  > 【業態】訪問看護用の電子カルテシステム「iBow(アイボウ)」の開発・販売。業務支援も。
  > 【いま】終値2,314円・直近5日+0.70%（材料未確認）
  > 【調子】✅順調（4/13）
  > 【水準】⚪妥当（3.0/7）— PER26.36倍・PEG1.0421・52週46.9% ／ 💰単元23.1万円
  > 【戦略】当日高値超えの逆指値2331円で順張り参戦を検討。上限2354.3円・SL2190.2円目安
- 6629 TECHNO HORIZON Co., Ltd.｜kenmo_momentum｜✅順調(4)｜⚪妥当｜FAIL_INSEN｜976円｜💰9.8万円｜—
- 6289 Giken Ltd.｜kenmo_momentum｜⚠減速(1)｜🔴過熱｜FAIL_UWAHIGE｜2,025円｜💰20.4万円｜—
- 3077 Horiifoodservice Co., Ltd.｜kenmo_momentum｜判定保留(変則決算)｜—｜FAIL_UWAHIGE｜1,170円｜💰—｜—
- 6918 Aval Data Corporation｜kenmo_newhigh｜🚀確変(13)｜⚪妥当｜FAIL_INSEN｜3,830円｜💰39.5万円｜—
- 3374 Naigai Tec Corporation｜kenmo_newhigh｜🚀確変(12)｜⚪妥当｜FAIL_INSEN｜4,885円｜💰50.5万円｜—
- 7567 Sakae Electronics Corp.｜kenmo_newhigh｜🚀確変(12)｜⚪妥当｜PASS｜634円｜💰6.3万円｜momentum 639 想定損失幅6.2%。｜📋カルテ窓 11/12(残15営業日)
  > 【業態】独立系電子部品商社。半導体製造装置向け中心。スイッチング電源などに強み。
  > 【いま】終値634円・直近5日-2.16%（材料未確認）
  > 【調子】🚀確変（12/13）
  > 【水準】⚪妥当（4.0/7）— PER15.85倍・PEG0.1239・52週73.8% ／ 💰単元6.3万円
  > 【戦略】当日高値超えの逆指値639円で順張り参戦を検討。上限645.4円・SL599.7円目安
- 269A SAPEET｜kenmo_newhigh｜🚀確変(11)｜⚪妥当｜PASS｜2,904円｜💰29.0万円｜—｜📋カルテ窓 11/12(残15営業日)｜⛔提案なし(指名鮮度切れ 18営業日)
  > 【業態】Expert AIを活用したAIプロダクトやAIソリューションの提供。AI社会の事業を支援。
  > 【いま】終値2,904円・直近5日+0.10%（材料未確認）
  > 【調子】🚀確変（11/13）
  > 【水準】⚪妥当（4.0/7）— PER36.03倍・PEG0.2133・52週69.6% ／ 💰単元29.0万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 18営業日)）
- 6337 Tesec Corporation｜kenmo_newhigh｜🚀確変(11)｜⚪妥当｜FAIL_INSEN｜3,305円｜💰34.4万円｜—
- 3696 セレス｜kenmo_newhigh｜🔥絶好調(8)｜🟢値頃｜FAIL_INSEN｜2,304円｜💰23.8万円｜—
- 2930 北の達人コーポレーション｜kenmo_newhigh｜⚡好調(6)｜🔴過熱｜FAIL_UWAHIGE｜151円｜💰1.5万円｜—
- 2820 Yamami Co.｜kenmo_newhigh｜✅順調(4)｜🟡やや割高｜FAIL_UWAHIGE｜6,740円｜💰67.8万円｜—
- 3843 Freebit Co., Ltd.｜kenmo_newhigh｜✅順調(3)｜⚪妥当｜PASS｜1,759円｜💰17.6万円｜momentum 1772 想定損失幅6.1%。｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）
  > 【業態】ネット接続にインフラ提供サービス。ドコモと提携、MVNOトーン運営。企業DX支援も展開。
  > 【いま】終値1,759円・直近5日-0.73%（材料未確認）
  > 【調子】✅順調（3/13）
  > 【水準】⚪妥当（3.0/7）— PER10.96倍・PEG1.0614・52週87.5% ／ 💰単元17.6万円
  > 【戦略】当日高値超えの逆指値1772円で順張り参戦を検討。上限1789.7円・SL1664.7円目安
- 4331 Take and Give. Needs Co., Ltd.｜kenmo_newhigh｜✅順調(3)｜🟡やや割高｜PASS｜816円｜💰8.2万円｜—｜📋カルテ窓 11/11(残14営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）｜⛔提案なし(指名鮮度切れ 12営業日)
  > 【業態】ハウスウエディングで先駆。邸宅風の直営店を全国展開。関連事業やホテル展開。
  > 【いま】終値816円・直近5日-2.28%（材料未確認）
  > 【調子】✅順調（3/13） — 質注意
  > 【水準】🟡やや割高（2.0/7）— PER14.89倍・PEG—・52週72.9% ／ 💰単元8.2万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 12営業日)）
- 7161 Jimoto Holdings, Inc.｜kenmo_newhigh｜業績データ取得不可｜⚪妥当｜PASS｜587円｜💰5.9万円｜momentum 589 想定損失幅6.2%。｜📋カルテ窓 11/13(残16営業日)
  > 【業態】銀行業（地方銀行・銀行・金利上昇メリット関連）
  > 【いま】終値587円・直近5日-5.32%（材料未確認）
  > 【調子】業績データ取得不可
  > 【水準】⚪妥当（4.0/7）— PER4.58倍・PEG0.1721・52週63.6% ／ 💰単元5.9万円
  > 【戦略】当日高値超えの逆指値589円で順張り参戦を検討。上限594.9円・SL552.7円目安
- 4565 Nxera Pharma Co., Ltd.｜kenmo_newhigh｜業績データ取得不可(経常益予想非開示)｜🟡やや割高｜FAIL_UWAHIGE｜1,313円｜💰12.5万円｜—
- 2340 Gokurakuyu Holdings Co., Ltd.｜kenmo_newhigh｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜506円｜💰5.1万円｜—
- 446A ノースサンド｜kenmo_newhigh｜—｜—｜FAIL_UWAHIGE｜2,880円｜💰—｜—
- 8871 GOLDCREST Co., Ltd.｜choruko_reversal｜🔥絶好調(10)｜💎割安｜FAIL_INSEN｜2,874円｜💰29.3万円｜—
- 3391 TSURUHA Holdings, Inc.｜choruko_reversal｜🔥絶好調(10)｜🟢値頃｜FAIL_INSEN｜2,186円｜💰22.6万円｜—
- 3186 ネクステージ｜choruko_reversal｜🔥絶好調(9)｜💎割安｜PASS｜2,585円｜💰25.9万円｜—｜⚠日程不明｜⛔提案なし(指名鮮度切れ 13営業日)
  > 【業態】中古車販売大手。東海から全国展開。車種別専門店や輸入新車販売店も。
  > 【いま】終値2,585円・直近5日-2.23%（材料未確認）
  > 【調子】🔥絶好調（9/13）
  > 【水準】💎割安（6.0/7）— PER11.86倍・PEG0.3125・52週14.2% ／ 💰単元25.9万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 13営業日)）
- 6324 Harmonic Drive Systems Inc.｜choruko_reversal｜🔥絶好調(9)｜⚪妥当｜FAIL_INSEN｜5,390円｜💰53.0万円｜—
- 3222 United Super Markets Holdings, Inc.｜choruko_reversal｜🔥絶好調(9)｜🔴過熱｜FAIL_INSEN｜754円｜💰7.6万円｜—
- 1803 Shimizu Corporation｜choruko_reversal｜🔥絶好調(8)｜💎割安｜FAIL_INSEN｜2,028円｜💰20.2万円｜—
- 4023 クレハ｜choruko_reversal｜🔥絶好調(8)｜🟢値頃｜FAIL_INSEN｜3,880円｜💰38.5万円｜—
- 7733 Olympus Corp.｜choruko_reversal｜🔥絶好調(8)｜⚪妥当｜FAIL_INSEN｜1,698円｜💰17.3万円｜—
- 7004 Kanadevia Corporation｜choruko_reversal｜⚠減速(7)｜💎割安｜FAIL_INSEN｜1,065円｜💰10.9万円｜—
- 2874 YOKOREI CO. LTD.｜choruko_reversal｜⚠減速(7)｜🟢値頃｜FAIL_INSEN｜1,730円｜💰17.6万円｜—
- 8522 Bank of Nagoya, Ltd.｜choruko_reversal｜⚡好調(7)｜🟢値頃｜FAIL_UWAHIGE｜6,140円｜💰63.0万円｜—
- 8987 Japan Excellent, Inc.｜choruko_reversal｜⚡好調(6)｜🟢値頃｜FAIL_INSEN｜123,600円｜💰12.5万円｜—
- 8282 K'S HOLDINGS CORPORATION｜choruko_reversal｜⚡好調(6)｜🟢値頃｜FAIL_INSEN｜1,706円｜💰17.4万円｜—
- 8088 IWATANI Corporation｜choruko_reversal｜⚡好調(6)｜⚪妥当｜FAIL_INSEN｜1,886円｜💰19.4万円｜—
- 8386 Hyakujushi Bank, Ltd.｜choruko_reversal｜⚡好調(6)｜⚪妥当｜FAIL_UWAHIGE｜2,761円｜💰28.5万円｜—
- 9412 SKY Perfect JSAT Corporation｜choruko_reversal｜⚡好調(6)｜⚪妥当｜FAIL_INSEN｜1,908円｜💰19.2万円｜—
- 8125 Wakita & Co., Ltd.｜choruko_reversal｜⚡好調(6)｜🔴過熱｜FAIL_INSEN｜1,839円｜💰18.5万円｜—
- 9861 吉野家ホールディングス｜choruko_reversal｜⚡好調(6)｜🔴過熱｜FAIL_INSEN｜4,309円｜💰44.6万円｜—
- 4666 Park24 Co., Ltd.｜choruko_reversal｜⚡好調(5)｜💎割安｜FAIL_INSEN｜1,802円｜💰18.0万円｜—
- 7721 Tokyo Keiki Inc.｜choruko_reversal｜⚡好調(5)｜🟢値頃｜FAIL_INSEN｜6,050円｜💰63.5万円｜—
- 8278 Fuji Co., Ltd.｜choruko_reversal｜⚡好調(5)｜🟢値頃｜FAIL_INSEN｜1,953円｜💰19.6万円｜—
- 8381 San-in Godo Bank Ltd.｜choruko_reversal｜⚡好調(5)｜⚪妥当｜FAIL_UWAHIGE｜2,189円｜💰23.0万円｜—
- 8954 ORIX JREIT Inc.｜choruko_reversal｜⚡好調(5)｜⚪妥当｜FAIL_INSEN｜88,700円｜💰8.8万円｜—
- 8393 Miyazaki Bank Ltd.｜choruko_reversal｜⚡好調(5)｜⚪妥当｜PASS｜2,462円｜💰24.6万円｜reversal 2462 想定損失幅5.4%。｜📋カルテ窓 11/06(残11営業日)
  > 【業態】宮崎地盤の地銀中位。県指定金融機関。農業、医療、介護向け融資攻勢。
  > 【いま】終値2,462円・直近5日-3.41%（材料未確認）
  > 【調子】⚡好調（5/13）
  > 【水準】⚪妥当（4.0/7）— PER14.25倍・PEG2.0639・52週72.7% ／ 💰単元24.6万円
  > 【戦略】当日終値2462円の指値で反転を取りにいく。SL2328円（直近5日安値）
- 7458 Daiichikosho Co., Ltd.｜choruko_reversal｜⚡好調(5)｜⚪妥当｜FAIL_INSEN｜1,754円｜💰17.6万円｜—
- 2702 日本マクドナルドホールディングス｜choruko_reversal｜⚠減速(5)｜🔴過熱｜FAIL_INSEN｜8,190円｜💰79.1万円｜—
- 2782 Seria Co., Ltd.｜choruko_reversal｜⚡好調(5)｜🔴過熱｜FAIL_INSEN｜4,245円｜💰41.6万円｜—
- 2809 Kewpie Corporation｜choruko_reversal｜⚡好調(5)｜🔴過熱｜FAIL_INSEN｜4,529円｜💰45.7万円｜—
- 3279 Activia Properties, Inc.｜choruko_reversal｜✅順調(4)｜⚪妥当｜FAIL_UWAHIGE｜123,300円｜💰12.5万円｜—
- 3282 Comforia Residential REIT, Inc.｜choruko_reversal｜✅順調(4)｜🟡やや割高｜FAIL_INSEN｜88,500円｜💰8.9万円｜—
- 8952 Japan Real Estate Investment Corp.｜choruko_reversal｜✅順調(4)｜🟡やや割高｜FAIL_INSEN｜106,500円｜💰10.8万円｜—
- 1861 Kumagai Gumi Co., Ltd.｜choruko_reversal｜✅順調(3)｜💎割安｜FAIL_INSEN｜1,211円｜💰12.2万円｜—
- 1417 MIRAIT ONE Corporation｜choruko_reversal｜✅順調(3)｜🟢値頃｜FAIL_INSEN｜3,334円｜💰33.7万円｜—
- 3148 Create SD Holdings Co., Ltd.｜choruko_reversal｜✅順調(3)｜⚪妥当｜FAIL_INSEN｜3,180円｜💰32.1万円｜—
- 8198 Maxvalu Tokai Co., Ltd.｜choruko_reversal｜✅順調(3)｜⚪妥当｜FAIL_INSEN｜3,135円｜💰31.1万円｜—
- 1820 Nishimatsu Construction Co., Ltd.｜choruko_reversal｜✅順調(3)｜⚪妥当｜PASS｜5,287円｜💰52.9万円｜reversal 5287 想定損失幅3.3%。｜📋カルテ窓 11/10(残13営業日)
  > 【業態】総合建設会社。ダム・トンネルなど土木に強み。開発事業強化。伊藤忠の持分法。
  > 【いま】終値5,287円・直近5日+1.30%（材料未確認）
  > 【調子】✅順調（3/13） — 質注意
  > 【水準】⚪妥当（3.0/7）— PER10.18倍・PEG—・52週12.6% ／ 💰単元52.9万円
  > 【戦略】当日終値5287円の指値で反転を取りにいく。SL5115円（直近5日安値）
- 1952 Shin Nippon Air Technologies Co., Ltd.｜choruko_reversal｜✅順調(3)｜⚪妥当｜PASS｜2,986円｜💰29.9万円｜reversal 2986 想定損失幅2.5%。｜📋カルテ窓 11/12(残15営業日)
  > 【業態】三井系、空調設備工事会社。原子力空調、微粒子可視化など独自技術注力。
  > 【いま】終値2,986円・直近5日-1.61%（材料未確認）
  > 【調子】✅順調（3/13）
  > 【水準】⚪妥当（3.0/7）— PER10.63倍・PEG2.7263・52週13.7% ／ 💰単元29.9万円
  > 【戦略】当日終値2986円の指値で反転を取りにいく。SL2912円（直近5日安値）
- 6269 Modec, Inc.｜choruko_reversal｜✅順調(3)｜⚪妥当｜PASS_DOJI｜8,027円｜💰80.3万円｜reversal 8027 想定損失幅0.9%。｜📋カルテ窓 11/10(残13営業日)
  > 【業態】浮体式石油・ガス生産貯蔵設備の世界大手。設計・建造、リース、運転、保守一貫。
  > 【いま】終値8,027円・直近5日-5.41%（材料未確認）
  > 【調子】✅順調（3/13） — 質注意
  > 【水準】⚪妥当（3.0/7）— PER9.47倍・PEG—・52週0.8% ／ 💰単元80.3万円
  > 【戦略】当日終値8027円の指値で反転を取りにいく。SL7957円（直近5日安値）
- 7003 Mitsui ES Holdings Co., Ltd.｜choruko_reversal｜✅順調(3)｜⚪妥当｜FAIL_INSEN｜3,694円｜💰38.3万円｜—
- 8584 Jaccs Co., Ltd.｜choruko_reversal｜🔻悪化(3)｜⚪妥当｜FAIL_INSEN｜3,420円｜💰34.9万円｜—
- 9882 Yellow Hat Ltd.｜choruko_reversal｜✅順調(3)｜⚪妥当｜FAIL_INSEN｜1,611円｜💰16.3万円｜—
- 1860 Toda Corporation｜choruko_reversal｜✅順調(3)｜🟡やや割高｜FAIL_INSEN｜1,404円｜💰14.1万円｜—
- 1944 Kinden Corporation｜choruko_reversal｜✅順調(3)｜🟡やや割高｜FAIL_INSEN｜6,432円｜💰64.7万円｜—
- 8066 Mitani Corporation｜choruko_reversal｜⚠減速(3)｜🟡やや割高｜FAIL_INSEN｜3,000円｜💰31.4万円｜—
- 2659 SAN-A CO., LTD.｜choruko_reversal｜✅順調(3)｜🔴過熱｜FAIL_INSEN｜3,150円｜💰31.4万円｜—
- 2805 S&B Foods Inc.｜choruko_reversal｜✅順調(3)｜🔴過熱｜FAIL_UWAHIGE｜6,110円｜💰63.3万円｜—
- 5021 Cosmo Energy Holdings Co., Ltd.｜choruko_reversal｜🔻悪化(3)｜🔴過熱｜FAIL_UWAHIGE｜4,239円｜💰42.2万円｜—
- 7984 Kokuyo Co., Ltd.｜choruko_reversal｜✅順調(3)｜🔴過熱｜FAIL_INSEN｜884円｜💰8.9万円｜—
- 3289 Tokyu Fudosan Holdings Corp.｜choruko_reversal｜➖横ばい(2)｜💎割安｜FAIL_INSEN｜1,209円｜💰12.1万円｜—
- 8818 Keihanshin Building Co., Ltd.｜choruko_reversal｜➖横ばい(2)｜⚪妥当｜FAIL_INSEN｜925円｜💰9.4万円｜—
- 1333 Umios Corporation｜choruko_reversal｜➖横ばい(2)｜⚪妥当｜FAIL_UWAHIGE｜1,204円｜💰12.0万円｜—
- 1719 HAZAMA ANDO Corporation｜choruko_reversal｜➖横ばい(2)｜⚪妥当｜FAIL_INSEN｜1,762円｜💰17.5万円｜—
- 1833 Okumura Corporation｜choruko_reversal｜⚠減速(2)｜⚪妥当｜FAIL_INSEN｜5,300円｜💰52.7万円｜—
- 9503 Kansai Electric Power Company, Incorporated｜choruko_reversal｜🔻悪化(2)｜⚪妥当｜FAIL_INSEN｜2,730円｜💰27.2万円｜—
- 8953 Japan Metropolitan Fund Investment Corporation｜choruko_reversal｜➖横ばい(2)｜🟡やや割高｜FAIL_UWAHIGE｜102,300円｜💰10.4万円｜—
- 6366 Chiyoda Corp.｜choruko_reversal｜🔻悪化(2)｜🟡やや割高｜FAIL_INSEN｜591円｜💰6.2万円｜—
- 5844 Kyoto Financial Group,Inc.｜choruko_reversal｜🔻悪化(2)｜🔴過熱｜FAIL_UWAHIGE｜4,151円｜💰42.5万円｜—
- 2379 dip Corporation｜choruko_reversal｜⚠減速(1)｜💎割安｜FAIL_INSEN｜1,462円｜💰16.6万円｜—
- 1893 Penta-Ocean Construction Co., Ltd.｜choruko_reversal｜⚠減速(1)｜⚪妥当｜FAIL_UWAHIGE｜1,370円｜💰13.5万円｜—
- 6183 BELLSYSTEM24 Holdings, Inc.｜choruko_reversal｜⚠減速(1)｜⚪妥当｜PASS｜1,339円｜💰13.4万円｜reversal 1339 想定損失幅6.4%。｜⚠日程不明｜⚠業績基調が下向き（⚠減速）｜📑TOPIX低減対象（次 10/30 第1回/8）
  > 【業態】コールセンターのCRM事業を中心にBPO事業も。伊藤忠が資本参加。凸版と提携。
  > 【いま】終値1,339円・直近5日+3.08%（材料未確認）
  > 【調子】⚠減速（1/13）
  > 【水準】⚪妥当（3.0/7）— PER11.70倍・PEG4.6403・52週28.7% ／ 💰単元13.4万円
  > 【戦略】当日終値1339円の指値で反転を取りにいく。SL1253円（直近5日安値）
- 6753 Sharp Corporation｜choruko_reversal｜🔻悪化(1)｜⚪妥当｜FAIL_INSEN｜594円｜💰5.9万円｜—
- 8276 HEIWADO CO., LTD.｜choruko_reversal｜⚠減速(1)｜⚪妥当｜FAIL_INSEN｜2,546円｜💰25.6万円｜—
- 9948 Arcs Company, Limited｜choruko_reversal｜⚠減速(1)｜⚪妥当｜FAIL_UWAHIGE｜3,440円｜💰34.4万円｜—
- 9974 BELC Co., Ltd.｜choruko_reversal｜⚠減速(1)｜⚪妥当｜FAIL_INSEN｜6,230円｜💰62.3万円｜—
- 3234 Mori Hills Reit Investment Corporation｜choruko_reversal｜⚠減速(1)｜🟡やや割高｜FAIL_INSEN｜116,300円｜💰11.9万円｜—
- 3249 Industrial & Infrastructure Fund Investment Corporation｜choruko_reversal｜⚠減速(1)｜🟡やや割高｜FAIL_INSEN｜126,300円｜💰12.8万円｜—
- 3283 Nippon Prologis REIT, Inc.｜choruko_reversal｜⚠減速(1)｜🟡やや割高｜FAIL_UWAHIGE｜79,000円｜💰8.0万円｜—
- 3292 AEON REIT Investment Corp.｜choruko_reversal｜⚠減速(1)｜🟡やや割高｜FAIL_UWAHIGE｜104,400円｜💰10.5万円｜—
- 3296 NIPPON REIT Investment Corp｜choruko_reversal｜🔻悪化(1)｜🟡やや割高｜FAIL_INSEN｜74,500円｜💰7.6万円｜—
- 3309 Sekisui House Reit. Inc.｜choruko_reversal｜⚠減速(1)｜🟡やや割高｜FAIL_INSEN｜67,100円｜💰6.7万円｜—
- 3462 Nomura Real Estate Master Fund, Inc.｜choruko_reversal｜⚠減速(1)｜🟡やや割高｜FAIL_UWAHIGE｜127,300円｜💰13.5万円｜—
- 5482 Aichi Steel Corporation｜choruko_reversal｜⚠減速(1)｜🟡やや割高｜FAIL_INSEN｜2,879円｜💰29.4万円｜—
- 8955 Japan Prime Realty Investment Corporation｜choruko_reversal｜⚠減速(1)｜🟡やや割高｜FAIL_INSEN｜89,600円｜💰9.0万円｜—
- 8961 MORI TRUST REIT.Inc｜choruko_reversal｜⚠減速(1)｜🟡やや割高｜FAIL_INSEN｜66,300円｜💰6.7万円｜—
- 8986 Daiwa Securities Living Investment Corporation｜choruko_reversal｜⚠減速(1)｜🟡やや割高｜FAIL_INSEN｜83,000円｜💰8.4万円｜—
- 1946 Toenec Corporation｜choruko_reversal｜⚠減速(1)｜🟡やや割高｜FAIL_INSEN｜2,029円｜💰20.7万円｜—
- 2815 ARIAKE JAPAN Co., Ltd.｜choruko_reversal｜⚠減速(1)｜🟡やや割高｜FAIL_INSEN｜5,220円｜💰52.7万円｜—
- 5631 Japan Steel Works, Ltd.｜choruko_reversal｜⚠減速(1)｜🟡やや割高｜PASS_DOJI｜6,460円｜💰64.6万円｜reversal 6460 想定損失幅1.7%。｜📋カルテ窓 11/10(残13営業日)｜⚠業績基調が下向き（⚠減速）
  > 【業態】大型鋳鍛鋼、樹脂成形機で世界有数。射出成形機にも強み。防衛関連も。
  > 【いま】終値6,460円・直近5日-5.73%（材料未確認）
  > 【調子】⚠減速（1/13） — 質注意
  > 【水準】🟡やや割高（2.0/7）— PER25.03倍・PEG—・52週2.6% ／ 💰単元64.6万円
  > 【戦略】当日終値6460円の指値で反転を取りにいく。SL6347円（直近5日安値）
- 4928 Noevir Holdings Co., Ltd.｜choruko_reversal｜⚠減速(1)｜🔴過熱｜FAIL_INSEN｜4,635円｜💰46.6万円｜—
- 6960 Fukuda Denshi Co., Ltd.｜choruko_reversal｜⚠減速(1)｜🔴過熱｜FAIL_INSEN｜10,680円｜💰108.6万円｜—
- 9436 Okinawa Cellular Telephone Company｜choruko_reversal｜⚠減速(1)｜🔴過熱｜FAIL_UWAHIGE｜3,415円｜💰34.6万円｜—
- 1662 Japan Petroleum Exploration Co., Ltd.｜choruko_reversal｜🔻悪化(0)｜⚪妥当｜PASS｜1,699円｜💰17.0万円｜reversal 1699 想定損失幅2.6%。｜📋カルテ窓 11/12(残15営業日)｜⚠業績基調が下向き（🔻悪化）
  > 【業態】資源開発大手。原油・天然ガスの探鉱、開発、生産。国内で天然ガス・インフラ事業。
  > 【いま】終値1,699円・直近5日-1.34%（材料未確認）
  > 【調子】🔻悪化（0/13） — 減収・質注意
  > 【水準】⚪妥当（4.0/7）— PER6.69倍・PEG—・52週28.9% ／ 💰単元17.0万円
  > 【戦略】当日終値1699円の指値で反転を取りにいく。SL1655円（直近5日安値）
- 6804 Hosiden Corp.｜choruko_reversal｜🔻悪化(0)｜⚪妥当｜FAIL_INSEN｜2,356円｜💰23.8万円｜—
- 1969 Takasago Thermal Engineering Co., Ltd.｜choruko_reversal｜⚠減速(0)｜⚪妥当｜FAIL_UWAHIGE｜4,164円｜💰41.9万円｜—
- 8585 Orient Corporation｜choruko_reversal｜⚠減速(0)｜⚪妥当｜FAIL_INSEN｜758円｜💰7.8万円｜—
- 8194 Life Corporation｜choruko_reversal｜⚠減速(0)｜🟡やや割高｜PASS｜2,378円｜💰23.8万円｜reversal 2378 想定損失幅3.0%。｜⚠日程不明｜⚠業績基調が下向き（⚠減速）
  > 【業態】食品スーパー大手。首都圏・近畿地方で積極的に展開。三菱商事の持分法。
  > 【いま】終値2,378円・直近5日+3.35%（材料未確認）
  > 【調子】⚠減速（0/13）
  > 【水準】🟡やや割高（2.8/7）— PER10.83倍・PEG3.1450・52週16.3% ／ 💰単元23.8万円
  > 【戦略】当日終値2378円の指値で反転を取りにいく。SL2306円（直近5日安値）
- 9533 TOHO GAS Co., Ltd.｜choruko_reversal｜🔻悪化(0)｜🟡やや割高｜FAIL_UWAHIGE｜1,200円｜💰11.8万円｜—
- 9699 NISHIO HOLDINGS CO. LTD.｜choruko_reversal｜⚠減速(0)｜🟡やや割高｜FAIL_INSEN｜4,285円｜💰43.0万円｜—
- 8253 Credit Saison Co., Ltd.｜choruko_reversal｜取得不可｜💎割安｜FAIL_INSEN｜4,191円｜💰41.9万円｜—
- 5831 Shizuoka Financial Group, Inc.｜choruko_reversal｜取得不可｜🟢値頃｜FAIL_UWAHIGE｜3,076円｜💰31.8万円｜—
- 7201 Nissan Motor Co., Ltd.｜choruko_reversal｜業績データ取得不可(経常益予想非開示)｜🟢値頃｜FAIL_INSEN｜277円｜💰2.8万円｜—
- 7381 CCI Group, Inc.｜choruko_reversal｜取得不可｜🟢値頃｜PASS｜1,176円｜💰11.8万円｜reversal 1176 想定損失幅3.4%。
  > 【業態】石川県を地盤。北國銀行を中核に総合金融サービス。富山県も重点。
  > 【いま】終値1,176円・直近5日-5.01%（材料未確認）
  > 【調子】取得不可
  > 【水準】🟢値頃（5.0/7）— PER15.31倍・PEG0.4486・52週69.1% ／ 💰単元11.8万円
  > 【戦略】当日終値1176円の指値で反転を取りにいく。SL1136円（直近5日安値）
- 8345 Bank of Iwate Ltd.｜choruko_reversal｜業績データ取得不可(売上/経常欠損)｜🟢値頃｜PASS｜2,198円｜💰22.0万円｜reversal 2198 想定損失幅4.2%。｜📋カルテ窓 11/12(残15営業日)
  > 【業態】岩手地盤の地銀中位。県内で圧倒的。青森銀、秋田銀と提携。リース、コンサルも。
  > 【いま】終値2,198円・直近5日-5.75%（材料未確認）
  > 【調子】業績データ取得不可(売上/経常欠損)
  > 【水準】🟢値頃（5.0/7）— PER15.19倍・PEG1.1838・52週62.7% ／ 💰単元22.0万円
  > 【戦略】当日終値2198円の指値で反転を取りにいく。SL2106円（直近5日安値）
- 3471 Mitsui Fudosan Logistics Park, Inc.｜choruko_reversal｜判定保留(変則決算)｜⚪妥当｜FAIL_INSEN｜96,800円｜💰9.8万円｜—
- 8399 Bank Of The Ryukyus,Limited｜choruko_reversal｜業績データ取得不可(売上/経常欠損)｜⚪妥当｜PASS｜2,863円｜💰28.6万円｜reversal 2863 想定損失幅3.3%。｜📋カルテ窓 11/11(残14営業日)
  > 【業態】沖縄地盤の地銀大手。地域密着型で預金、融資県内首位。信託業務も併営。
  > 【いま】終値2,863円・直近5日-2.49%（材料未確認）
  > 【調子】業績データ取得不可(売上/経常欠損)
  > 【水準】⚪妥当（4.2/7）— PER11.75倍・PEG0.8038・52週71.2% ／ 💰単元28.6万円
  > 【戦略】当日終値2863円の指値で反転を取りにいく。SL2769円（直近5日安値）
- 7384 Procrea Holdings,Inc.｜choruko_reversal｜業績データ取得不可(売上/経常欠損)｜⚪妥当｜PASS｜4,230円｜💰42.3万円｜reversal 4230 想定損失幅3.3%。｜⚠日程不明
  > 【業態】青森地盤の地銀。青森銀とみちのく銀が経営統合。25年1月に合併。
  > 【いま】終値4,230円・直近5日-13.50%（材料未確認）
  > 【調子】業績データ取得不可(売上/経常欠損)
  > 【水準】⚪妥当（4.0/7）— PER17.11倍・PEG0.2366・52週58.5% ／ 💰単元42.3万円
  > 【戦略】当日終値4230円の指値で反転を取りにいく。SL4090円（直近5日安値）
- 8174 NIPPON GAS Co., Ltd.｜choruko_reversal｜業績データ取得不可｜⚪妥当｜FAIL_INSEN｜929円｜💰9.4万円｜—
- 8304 Aozora Bank, Ltd.｜choruko_reversal｜取得不可｜⚪妥当｜PASS｜3,103円｜💰31.0万円｜reversal 3103 想定損失幅2.2%。｜📋カルテ窓 11/11(残14営業日)
  > 【業態】旧日債銀。不動産融資、金融商品販売などが中心。GMOとネット銀行。
  > 【いま】終値3,103円・直近5日-4.35%（材料未確認）
  > 【調子】取得不可
  > 【水準】⚪妥当（4.0/7）— PER15.91倍・PEG0.4406・52週65.3% ／ 💰単元31.0万円
  > 【戦略】当日終値3103円の指値で反転を取りにいく。SL3035円（直近5日安値）
- 3591 WACOAL HOLDINGS CORP｜choruko_reversal｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜3,557円｜💰35.8万円｜—
- 8511 Japan Securities Finance Co., Ltd.｜choruko_reversal｜取得不可｜🔴過熱｜FAIL_UWAHIGE｜2,197円｜💰22.2万円｜—
- 7624 NaITO｜stf_kakuhen｜🔥絶好調(10)｜🟢値頃｜FAIL_INSEN｜170円｜💰1.8万円｜—
- 5018 ＭＯＲＥＳＣＯ｜stf_kakuhen｜🔥絶好調(10)｜⚪妥当｜FAIL_INSEN｜2,954円｜💰29.8万円｜—
- 6668 ＡＤプラズマ｜stf_kakuhen｜🔥絶好調(10)｜⚪妥当｜FAIL_INSEN｜5,080円｜💰49.4万円｜—
- 7713 シグマ光機｜stf_kakuhen｜🔥絶好調(10)｜⚪妥当｜FAIL_UWAHIGE｜3,290円｜💰33.2万円｜—
- 5246 ELEMENTS,Inc.｜stf_kakuhen｜🔥絶好調(10)｜⚪妥当｜FAIL_INSEN｜1,020円｜💰12.8万円｜—
- 3498 霞ヶ関Ｃ｜stf_kakuhen｜🔥絶好調(9)｜💎割安｜PASS｜6,900円｜💰69.0万円｜—｜⚠日程不明｜⛔提案なし(手法ブランチ不明)
  > 【業態】不動産コンサル業。再生可能エネ発電施設、投資用不動産の開発、投資家に売却。
  > 【いま】終値6,900円・直近5日-8.97%（材料未確認）
  > 【調子】🔥絶好調（9/13）
  > 【水準】💎割安（7.0/7）— PER7.06倍・PEG0.1810・52週29.6% ／ 💰単元69.0万円
  > 【戦略】発注対象外（⛔提案なし(手法ブランチ不明)）
- 3994 マネーフォワード｜stf_kakuhen｜🔥絶好調(9)｜🔴過熱｜FAIL_INSEN｜6,700円｜💰65.8万円｜—
- 7811 Nakamoto Packs Co. Ltd.｜stf_kakuhen｜🔥絶好調(8)｜🟢値頃｜FAIL_UWAHIGE｜2,573円｜💰24.1万円｜—
- 4443 Ｓａｎｓａｎ｜stf_kakuhen｜🔥絶好調(8)｜⚪妥当｜FAIL_INSEN｜2,082円｜💰20.7万円｜—
- 6814 古野電｜stf_kakuhen｜⚡好調(7)｜⚪妥当｜FAIL_INSEN｜8,200円｜💰87.3万円｜—
- 5932 三協立山｜stf_kakuhen｜⚡好調(7)｜⚪妥当｜FAIL_INSEN｜772円｜💰7.8万円｜—
- 3479 ティーケーピー｜stf_kakuhen｜⚡好調(6)｜🔴過熱｜FAIL_INSEN｜1,924円｜💰19.6万円｜—
- 6505 東洋電機製造｜stf_kakuhen｜⚡好調(5)｜⚪妥当｜FAIL_INSEN｜3,145円｜💰31.5万円｜—
- 6532 ベイカレント｜stf_kakuhen｜⚡好調(5)｜🟡やや割高｜FAIL_UWAHIGE｜11,025円｜💰108.5万円｜—
- 4176 ココナラ｜stf_kakuhen｜✅順調(4)｜⚪妥当｜FAIL_UWAHIGE｜309円｜💰3.4万円｜—

## グランビル銘柄
- 5254 Arent, Inc.｜granville_tenkan｜🚀確変(12)｜⚪妥当｜PASS｜4,080円｜💰40.8万円｜momentum 4100 想定損失幅6.1%。｜📋カルテ窓 11/12(残15営業日)
  > 【業態】建設・プラント業界を中心にDXコンサルティング、システム開発、システム販売。自社製品も。
  > 【いま】終値4,080円・直近5日+1.62%（材料未確認）
  > 【調子】🚀確変（12/13）
  > 【水準】⚪妥当（4.0/7）— PER27.47倍・PEG0.3356・52週73.2% ／ 💰単元40.8万円
  > 【戦略】当日高値超えの逆指値4100円で順張り参戦を検討。上限4141円・SL3849.3円目安
- 8944 Land Business Co., Ltd.｜granville_tenkan｜🔥絶好調(10)｜💎割安｜FAIL_UWAHIGE｜254円｜💰2.6万円｜—
- 7725 INTER ACTION Corporation｜granville_tenkan｜🔥絶好調(10)｜🟢値頃｜FAIL_INSEN｜1,760円｜💰17.2万円｜—
- 9553 MicroAd, Inc.｜granville_tenkan｜🔥絶好調(10)｜🟢値頃｜FAIL_INSEN｜592円｜💰6.1万円｜—
- 6905 Cosel Co., Ltd.｜granville_tenkan｜🔥絶好調(10)｜⚪妥当｜PASS_DOJI｜1,340円｜💰13.4万円｜momentum 1352 想定損失幅6.1%。｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）
  > 【業態】スイッチング電源の標準品で国内2位。産業機器向け主力。生産を中国へ移管。
  > 【いま】終値1,340円・直近5日-8.72%（材料未確認）
  > 【調子】🔥絶好調（10/13）
  > 【水準】⚪妥当（4.0/7）— PER21.20倍・PEG0.0265・52週46.5% ／ 💰単元13.4万円
  > 【戦略】当日高値超えの逆指値1352円で順張り参戦を検討。上限1365.5円・SL1269.9円目安
- 2986 LA Holdings Co.,Ltd｜granville_tenkan｜🔥絶好調(9)｜💎割安｜FAIL_UWAHIGE｜2,693円｜💰27.1万円｜—
- 9211 f-code Inc.｜granville_tenkan｜🔥絶好調(9)｜💎割安｜FAIL_UWAHIGE｜1,306円｜💰14.5万円｜—
- 6562 Geniee, Inc.｜granville_tenkan｜🔥絶好調(8)｜💎割安｜FAIL_UWAHIGE｜939円｜💰10.0万円｜—
- 1945 Tokyo Energy & Systems Inc.｜granville_tenkan｜🔥絶好調(8)｜💎割安｜PASS｜2,003円｜💰20.0万円｜—｜📋カルテ窓 11/05(残10営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）｜⛔提案なし(指名鮮度切れ 16営業日)
  > 【業態】発電所の関連設備エンジニアリング。東電関連が中心。再生可能エネ機器設備も。
  > 【いま】終値2,003円・直近5日-3.05%（材料未確認）
  > 【調子】🔥絶好調（8/13）
  > 【水準】💎割安（6.0/7）— PER12.77倍・PEG0.3556・52週33.1% ／ 💰単元20.0万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 16営業日)）
- 9006 京浜急行電鉄｜granville_tenkan｜🔥絶好調(8)｜🟢値頃｜FAIL_INSEN｜1,537円｜💰15.4万円｜—
- 6473 JTEKT Corporation｜granville_tenkan｜⚠減速(8)｜⚪妥当｜FAIL_INSEN｜2,094円｜💰21.4万円｜—
- 8697 Japan Exchange Group, Inc.｜granville_tenkan｜🔥絶好調(8)｜🟡やや割高｜FAIL_UWAHIGE｜2,225円｜💰22.4万円｜—
- 6255 NPC Incorporated｜granville_tenkan｜⚡好調(7)｜🟢値頃｜FAIL_UWAHIGE｜678円｜💰6.8万円｜—
- 8095 Astena Holdings Co.,Ltd.｜granville_tenkan｜⚡好調(7)｜🟢値頃｜FAIL_UWAHIGE｜521円｜💰5.2万円｜—
- 8793 ＮＥＣキャピタルソリューション｜granville_tenkan｜⚡好調(7)｜🟢値頃｜PASS｜4,020円｜💰40.2万円｜—｜📑TOPIX低減対象（次 10/30 第1回/8）｜⛔提案なし(指名鮮度切れ 15営業日)
  > 【業態】SBI新生銀の持分法適用会社。情報通信機器中心でリース大手。ファンド事業も。
  > 【いま】終値4,020円・直近5日-1.11%（材料未確認）
  > 【調子】⚡好調（7/13）
  > 【水準】🟢値頃（5.0/7）— PER8.67倍・PEG0.1777・52週40.7% ／ 💰単元40.2万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 15営業日)）
- 3496 AZOOM CO.,LTD｜granville_tenkan｜⚡好調(7)｜⚪妥当｜FAIL_INSEN｜4,805円｜💰49.2万円｜—
- 4544 H.U.Group Holdings, Inc.｜granville_tenkan｜⚡好調(7)｜⚪妥当｜FAIL_INSEN｜3,718円｜💰37.1万円｜—
- 7744 Noritsu Koki Co., Ltd.｜granville_tenkan｜⚡好調(7)｜⚪妥当｜FAIL_UWAHIGE｜2,087円｜💰20.8万円｜—
- 9064 ヤマトホールディングス｜granville_tenkan｜⚡好調(7)｜⚪妥当｜PASS｜2,056円｜💰20.6万円｜momentum 2062 想定損失幅6.0%。
  > 【業態】宅配便最大手。集配網と配送品質に定評。物流増で生産性の改革を強化。
  > 【いま】終値2,056円・直近5日-1.39%（材料未確認）
  > 【調子】⚡好調（7/13）
  > 【水準】⚪妥当（4.0/7）— PER40.71倍・PEG0.6791・52週53.6% ／ 💰単元20.6万円
  > 【戦略】当日高値超えの逆指値2062円で順張り参戦を検討。上限2082.6円・SL1937.3円目安
- 3741 Systems Engineering Consultants Co., Ltd.｜granville_tenkan｜⚡好調(7)｜⚪妥当｜FAIL_UWAHIGE｜3,010円｜💰30.7万円｜—
- 6302 Sumitomo Heavy Industries, Ltd.｜granville_tenkan｜⚡好調(7)｜⚪妥当｜FAIL_INSEN｜5,600円｜💰57.2万円｜—
- 4507 Shionogi & Co., Ltd.｜granville_tenkan｜⚡好調(7)｜🟡やや割高｜FAIL_UWAHIGE｜3,021円｜💰29.8万円｜—
- 5838 Rakuten Bank, Ltd.｜granville_tenkan｜⚡好調(6)｜💎割安｜FAIL_UWAHIGE｜6,184円｜💰60.3万円｜—
- 4763 クリーク・アンド・リバー社｜granville_tenkan｜⚡好調(6)｜🟢値頃｜FAIL_INSEN｜1,454円｜💰14.5万円｜—
- 6470 Taiho Kogyo Co., Ltd.｜granville_tenkan｜⚡好調(6)｜⚪妥当｜FAIL_INSEN｜1,146円｜💰11.6万円｜—
- 7199 Premium Group Co., Ltd.｜granville_tenkan｜⚡好調(6)｜⚪妥当｜FAIL_INSEN｜2,216円｜💰22.2万円｜—
- 3064 MonotaRO Co., Ltd.｜granville_tenkan｜⚡好調(6)｜🔴過熱｜FAIL_UWAHIGE｜2,298円｜💰23.9万円｜—
- 3935 Edia Co. Ltd.｜granville_tenkan｜⚡好調(5)｜💎割安｜FAIL_INSEN｜731円｜💰7.3万円｜—
- 6196 Strike Group Co. Ltd.｜granville_tenkan｜⚡好調(5)｜💎割安｜FAIL_INSEN｜1,388円｜💰14.1万円｜—
- 3562 No.1 Co., Ltd.｜granville_tenkan｜⚡好調(5)｜🟢値頃｜FAIL_UWAHIGE｜1,691円｜💰17.0万円｜—
- 8061 Seika Corporation｜granville_tenkan｜⚡好調(5)｜🟢値頃｜FAIL_INSEN｜2,901円｜💰30.3万円｜—
- 9048 名古屋鉄道｜granville_tenkan｜⚡好調(5)｜🟢値頃｜FAIL_INSEN｜1,848円｜💰18.5万円｜—
- 2331 ALSOK CO., LTD.｜granville_tenkan｜⚡好調(5)｜⚪妥当｜FAIL_INSEN｜1,212円｜💰12.2万円｜—
- 3661 m-up holdings, Inc.｜granville_tenkan｜⚡好調(5)｜⚪妥当｜FAIL_INSEN｜869円｜💰8.9万円｜—
- 6432 Takeuchi Mfg.Co., Ltd.｜granville_tenkan｜⚡好調(5)｜⚪妥当｜FAIL_INSEN｜7,630円｜💰77.9万円｜—
- 7970 Shin-Etsu Polymer Co., Ltd.｜granville_tenkan｜⚡好調(5)｜🟡やや割高｜FAIL_UWAHIGE｜2,305円｜💰23.8万円｜—
- 8020 Kanematsu Corporation｜granville_tenkan｜⚡好調(5)｜🟡やや割高｜FAIL_INSEN｜2,309円｜💰24.0万円｜—
- 9828 Genki Global Dining Concepts Corp｜granville_tenkan｜⚡好調(5)｜🔴過熱｜FAIL_INSEN｜3,415円｜💰35.3万円｜—
- 6454 Max Co., Ltd.｜granville_tenkan｜⚡好調(5)｜🔴過熱｜FAIL_INSEN｜1,919円｜💰19.3万円｜—
- 2288 Marudai Food Co., Ltd.｜granville_tenkan｜✅順調(4)｜🟢値頃｜FAIL_INSEN｜2,176円｜💰21.8万円｜—
- 5036 Japan Business Systems, Inc.｜granville_tenkan｜✅順調(4)｜⚪妥当｜FAIL_INSEN｜1,884円｜💰18.8万円｜—
- 8014 Chori Co., Ltd.｜granville_tenkan｜✅順調(4)｜⚪妥当｜FAIL_INSEN｜4,245円｜💰43.0万円｜—
- 6988 日東電工｜granville_tenkan｜✅順調(4)｜🟡やや割高｜PASS｜3,681円｜💰36.8万円｜—｜⏰決算 10/27(残4営業日)｜⛔提案なし(指名鮮度切れ 14営業日)
  > 【業態】テープ、フィルムの総合材料メーカー。液晶・半導体、医療用など。ニッチ商品で高シェア。
  > 【いま】終値3,681円・直近5日+1.32%（材料未確認）
  > 【調子】✅順調（4/13）
  > 【水準】🟡やや割高（2.0/7）— PER17.06倍・PEG2.1001・52週67.4% ／ 💰単元36.8万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 14営業日)）
- 6371 Tsubakimoto Chain Co.｜granville_tenkan｜✅順調(4)｜🔴過熱｜FAIL_INSEN｜2,605円｜💰26.8万円｜—
- 6592 Mabuchi Motor Co., Ltd.｜granville_tenkan｜✅順調(4)｜🔴過熱｜FAIL_INSEN｜1,730円｜💰17.7万円｜—
- 8060 キヤノンマーケティングジャパン｜granville_tenkan｜✅順調(4)｜🔴過熱｜FAIL_UWAHIGE｜4,021円｜💰40.3万円｜—
- 4166 Cacco, Inc.｜granville_tenkan｜✅順調(3)｜💎割安｜FAIL_UWAHIGE｜710円｜💰7.3万円｜—
- 8850 スターツコーポレーション｜granville_tenkan｜✅順調(3)｜⚪妥当｜FAIL_INSEN｜4,510円｜💰46.0万円｜—
- 3433 TOCALO Co., Ltd.｜granville_tenkan｜✅順調(3)｜⚪妥当｜FAIL_INSEN｜2,834円｜💰29.1万円｜—
- 8927 Meiho Enterprise Co., Ltd.｜granville_tenkan｜✅順調(3)｜⚪妥当｜FAIL_INSEN｜481円｜💰4.9万円｜—
- 186A Astroscale Holdings Inc.｜granville_tenkan｜✅順調(3)｜🟡やや割高｜PASS｜1,070円｜💰10.7万円｜momentum 1084 想定損失幅6.1%。｜⚠日程不明｜📑TOPIX新規採用（2026-10-30 組入）
  > 【業態】宇宙ごみ(スペースデブリ)除去や人工衛星寿命延長などのサービスを手掛ける。
  > 【いま】終値1,070円・直近5日-5.39%（材料未確認）
  > 【調子】✅順調（3/13）
  > 【水準】🟡やや割高（2.8/7）— PER—倍・PEG—・52週20.3% ／ 💰単元10.7万円
  > 【戦略】当日高値超えの逆指値1084円で順張り参戦を検討。上限1094.8円・SL1018円目安
- 4183 Mitsui Chemicals, Inc.｜granville_tenkan｜✅順調(3)｜🟡やや割高｜FAIL_INSEN｜2,088円｜💰21.0万円｜—
- 4272 Nippon Kayaku Co., Ltd.｜granville_tenkan｜✅順調(3)｜🟡やや割高｜FAIL_INSEN｜2,120円｜💰21.6万円｜—
- 4956 Konishi Co., Ltd.｜granville_tenkan｜✅順調(3)｜🟡やや割高｜FAIL_INSEN｜1,518円｜💰15.2万円｜—
- 5461 Chubu Steel Plate Co., Ltd.｜granville_tenkan｜🔻悪化(3)｜🟡やや割高｜FAIL_INSEN｜2,161円｜💰21.4万円｜—
- 7181 JAPAN POST INSURANCE Co., Ltd.｜granville_tenkan｜⚠減速(3)｜🔴過熱｜FAIL_INSEN｜1,700円｜💰17.3万円｜—
- 7734 Riken Keiki Co., Ltd.｜granville_tenkan｜✅順調(3)｜🔴過熱｜FAIL_INSEN｜3,430円｜💰35.5万円｜—
- 7513 Kojima Co., Ltd.｜granville_tenkan｜✅順調(3)｜🔴過熱｜FAIL_INSEN｜1,427円｜💰14.6万円｜—
- 6328 Ebara Jitsugyo Co., Ltd.｜granville_tenkan｜➖横ばい(2)｜⚪妥当｜PASS｜2,463円｜💰24.6万円｜momentum 2473 想定損失幅6.0%。｜📋カルテ窓 11/05(残10営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
  > 【業態】上下水処理施設から空調など環境関連事業に拡大。研究開発・ファブレス型。
  > 【いま】終値2,463円・直近5日-1.48%（材料未確認）
  > 【調子】➖横ばい（2/13） — 質注意
  > 【水準】⚪妥当（3.0/7）— PER12.87倍・PEG4.4172・52週46.3% ／ 💰単元24.6万円
  > 【戦略】当日高値超えの逆指値2473円で順張り参戦を検討。上限2497.7円・SL2323.7円目安
- 2002 日清製粉グループ本社｜granville_tenkan｜➖横ばい(2)｜🟡やや割高｜FAIL_INSEN｜2,046円｜💰20.6万円｜—
- 6208 Ishikawa Seisakusho,Ltd.｜granville_tenkan｜🔻悪化(2)｜🟡やや割高｜FAIL_INSEN｜1,618円｜💰16.6万円｜—
- 2413 エムスリー｜granville_tenkan｜➖横ばい(2)｜🔴過熱｜PASS｜1,920円｜💰19.2万円｜—｜⛔提案なし(指名鮮度切れ 12営業日)
  > 【業態】ソニー系。製薬会社のマーケ支援。医師向けサイトで情報提供。遠隔医療も。
  > 【いま】終値1,920円・直近5日+0.31%（材料未確認）
  > 【調子】➖横ばい（2/13） — 質注意
  > 【水準】🔴過熱（1.0/7）— PER24.11倍・PEG3.8936・52週43.0% ／ 💰単元19.2万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 12営業日)）
- 4617 Chugoku Marine Paints,Ltd.｜granville_tenkan｜➖横ばい(2)｜🔴過熱｜FAIL_INSEN｜3,575円｜💰37.1万円｜—
- 7751 キヤノン｜granville_tenkan｜➖横ばい(2)｜🔴過熱｜FAIL_INSEN｜4,816円｜💰48.2万円｜—
- 8081 Kanaden Corporation｜granville_tenkan｜➖横ばい(2)｜🔴過熱｜FAIL_INSEN｜2,661円｜💰28.0万円｜—
- 5071 VIS Co., Ltd.｜granville_tenkan｜⚠減速(1)｜⚪妥当｜FAIL_INSEN｜1,372円｜💰13.8万円｜—
- 6770 Alps Alpine Co., Ltd.｜granville_tenkan｜⚠減速(1)｜🟡やや割高｜FAIL_INSEN｜2,101円｜💰21.4万円｜—
- 1815 鉄建建設｜granville_tenkan｜⚠減速(0)｜⚪妥当｜FAIL_UWAHIGE｜2,170円｜💰21.8万円｜—
- 4375 Safie Inc.｜granville_tenkan｜取得不可｜💎割安｜FAIL_INSEN｜661円｜💰6.8万円｜—
- 8424 芙蓉総合リース｜granville_tenkan｜取得不可｜💎割安｜FAIL_INSEN｜4,291円｜💰43.1万円｜—
- 2871 ニチレイ｜granville_tenkan｜業績データ取得不可｜🔴過熱｜FAIL_INSEN｜2,134円｜💰21.4万円｜—
- 4534 Mochida Pharmaceutical Co., Ltd.｜granville_tenkan｜—｜—｜FAIL_INSEN｜3,235円｜💰—｜—
- 4549 Eiken Chemical Co., Ltd.｜granville_tenkan｜—｜—｜FAIL_INSEN｜2,417円｜💰—｜—
- 4552 JCR Pharmaceuticals Co., Ltd.｜granville_tenkan｜—｜—｜FAIL_UWAHIGE｜532円｜💰—｜—
- 6768 Tamura Corporation｜granville_tenkan｜—｜—｜FAIL_UWAHIGE｜871円｜💰—｜—
- 4937 Ｇ−ＷＡＱＯＯ｜granville_oshime｜🚀確変(13)｜⚪妥当｜FAIL_UWAHIGE｜2,322円｜💰23.2万円｜—
- 3083 Star seeds Co.,Ltd.｜granville_oshime｜🚀確変(12)｜⚪妥当｜FAIL_UWAHIGE｜1,056円｜💰10.6万円｜—
- 290A ＳＹＮＳＰＥＣＴＩＶＥ｜granville_oshime｜🚀確変(11)｜🟢値頃｜FAIL_UWAHIGE｜1,214円｜💰12.2万円｜—
- 5243 note inc.｜granville_oshime｜🚀確変(11)｜⚪妥当｜FAIL_INSEN｜2,935円｜💰30.1万円｜—
- 7806 MTG Co., Ltd.｜granville_oshime｜🚀確変(11)｜⚪妥当｜FAIL_INSEN｜8,090円｜💰84.3万円｜—
- 6834 Seikoh Giken Co., Ltd.｜granville_oshime｜🔥絶好調(10)｜💎割安｜FAIL_INSEN｜5,720円｜💰58.9万円｜—
- 6613 QD Laser, Inc.｜granville_oshime｜🔥絶好調(10)｜🟡やや割高｜PASS｜2,065円｜💰20.6万円｜—｜📋カルテ窓 11/12(残15営業日)｜📑TOPIX新規採用（2026-10-30 組入）｜⛔型不一致: 既に支持帯以下
  > 【業態】半導体レーザ、網膜走査型レーザアイウェアなどの開発・製造・販売を手掛ける。
  > 【いま】終値2,065円・直近5日-2.23%（材料未確認）
  > 【調子】🔥絶好調（10/13）
  > 【水準】🟡やや割高（2.0/7）— PER196.67倍・PEG1.9475・52週53.3% ／ 💰単元20.6万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 8336 Musashino Bank, Ltd.｜granville_oshime｜🔥絶好調(9)｜⚪妥当｜PASS｜2,628円｜💰26.3万円｜—｜📋カルテ窓 11/06(残11営業日)｜⛔型不一致: 既に支持帯以下
  > 【業態】埼玉地盤で全域に店舗網。地域密着型営業展開。千葉銀と提携。
  > 【いま】終値2,628円・直近5日-3.38%（材料未確認）
  > 【調子】🔥絶好調（9/13）
  > 【水準】⚪妥当（4.2/7）— PER13.07倍・PEG0.4033・52週76.6% ／ 💰単元26.3万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 8008 Yondoshi Holdings, Inc.｜granville_oshime｜🔥絶好調(9)｜⚪妥当｜FAIL_UWAHIGE｜2,020円｜💰20.1万円｜—
- 2334 Eole, Inc.｜granville_oshime｜🔥絶好調(8)｜⚪妥当｜FAIL_INSEN｜542円｜💰5.6万円｜—
- 4180 ＡＰＰＩＥＲ　ＧＲＯＵＰ｜granville_oshime｜🔥絶好調(8)｜⚪妥当｜FAIL_UWAHIGE｜1,417円｜💰14.1万円｜—
- 8346 Toho Bank, Ltd.｜granville_oshime｜🔥絶好調(8)｜⚪妥当｜FAIL_UWAHIGE｜1,007円｜💰10.3万円｜—
- 7856 HAGIHARA INDUSTRIES INC.｜granville_oshime｜🔥絶好調(8)｜🟡やや割高｜FAIL_INSEN｜2,038円｜💰20.7万円｜—
- 1879 新日本建設｜granville_oshime｜⚡好調(7)｜💎割安｜FAIL_INSEN｜2,175円｜💰22.2万円｜—
- 6736 Suncorporation｜granville_oshime｜⚡好調(7)｜⚪妥当｜FAIL_INSEN｜9,800円｜💰97.4万円｜—
- 6523 PHC Holdings Corp.｜granville_oshime｜⚠減速(6)｜🟢値頃｜FAIL_INSEN｜1,318円｜💰13.7万円｜—
- 7609 Daitron Co., Ltd.｜granville_oshime｜⚡好調(6)｜🟢値頃｜PASS｜4,165円｜💰41.6万円｜—｜⛔型不一致: 既に支持帯以下
  > 【業態】電子部品卸中堅。製造装置にも強み。スイッチ電源など自社製造製品に注力。
  > 【いま】終値4,165円・直近5日-11.85%（材料未確認）
  > 【調子】⚡好調（6/13）
  > 【水準】🟢値頃（5.0/7）— PER13.56倍・PEG0.4867・52週72.6% ／ 💰単元41.6万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 2767 円谷フィールズホールディングス｜granville_oshime｜⚡好調(6)｜⚪妥当｜FAIL_INSEN｜2,509円｜💰25.2万円｜—
- 4667 Aisan Technology Co., Ltd.｜granville_oshime｜⚡好調(6)｜⚪妥当｜FAIL_UWAHIGE｜964円｜💰9.7万円｜—
- 6023 ダイハツインフィニアース｜granville_oshime｜⚡好調(6)｜⚪妥当｜FAIL_UWAHIGE｜2,956円｜💰31.9万円｜—
- 6227 AIMECHATEC Ltd.｜granville_oshime｜⚡好調(6)｜⚪妥当｜FAIL_INSEN｜6,320円｜💰68.5万円｜—
- 2602 日清オイリオグループ｜granville_oshime｜⚡好調(6)｜🟡やや割高｜FAIL_INSEN｜2,054円｜💰20.5万円｜—
- 4413 baudroie,inc.｜granville_oshime｜⚡好調(6)｜🟡やや割高｜FAIL_UWAHIGE｜2,941円｜💰29.9万円｜—
- 8919 カチタス｜granville_oshime｜⚡好調(6)｜🟡やや割高｜PASS｜3,350円｜💰33.5万円｜—｜📋カルテ窓 11/09(残12営業日)｜⛔型不一致: 既に支持帯以下
  > 【業態】中古住宅の再生・販売を地方中心に全国展開。ニトリと資本業務提携。
  > 【いま】終値3,350円・直近5日-1.03%（材料未確認）
  > 【調子】⚡好調（6/13）
  > 【水準】🟡やや割高（2.0/7）— PER18.73倍・PEG1.5221・52週63.2% ／ 💰単元33.5万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 7616 Colowide Co., Ltd.｜granville_oshime｜⚡好調(6)｜🔴過熱｜FAIL_INSEN｜2,192円｜💰22.0万円｜—
- 8714 Senshu Ikeda Holdings,Inc.｜granville_oshime｜⚡好調(5)｜⚪妥当｜FAIL_UWAHIGE｜995円｜💰10.4万円｜—
- 7350 Okinawa Financial Group, Inc.｜granville_oshime｜⚡好調(5)｜⚪妥当｜FAIL_UWAHIGE｜7,170円｜💰73.9万円｜—
- 6058 VECTOR Inc.｜granville_oshime｜⚡好調(5)｜🔴過熱｜FAIL_INSEN｜2,025円｜💰20.4万円｜—
- 4475 HENNGE K.K.｜granville_oshime｜⚡好調(5)｜🔴過熱｜FAIL_UWAHIGE｜1,979円｜💰20.8万円｜—
- 4373 Simplex Holdings,Inc.｜granville_oshime｜✅順調(4)｜🟡やや割高｜FAIL_INSEN｜1,248円｜💰12.6万円｜—
- 3097 Monogatari Corporation｜granville_oshime｜✅順調(4)｜🔴過熱｜FAIL_INSEN｜5,920円｜💰60.9万円｜—
- 6998 Nippon Tungsten Co., Ltd.｜granville_oshime｜✅順調(4)｜🔴過熱｜FAIL_UWAHIGE｜3,365円｜💰35.4万円｜—
- 5985 SUNCALL CORPORATION｜granville_oshime｜✅順調(3)｜⚪妥当｜PASS_DOJI｜2,142円｜💰21.4万円｜—｜📋カルテ窓 11/13(残16営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）｜⛔型不一致: 既に支持帯以下
  > 【業態】精密部品メーカー。車用精密ばね主力でトヨタ・ホンダ中心。プリンタ部品も。HDD撤退。
  > 【いま】終値2,142円・直近5日-17.58%（材料未確認）
  > 【調子】✅順調（3/13）
  > 【水準】⚪妥当（4.0/7）— PER10.30倍・PEG0.7586・52週61.6% ／ 💰単元21.4万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 1518 三井松島ホールディングス｜granville_oshime｜✅順調(3)｜🟡やや割高｜FAIL_INSEN｜2,237円｜💰22.9万円｜—
- 6379 RAIZNEXT Corporation｜granville_oshime｜✅順調(3)｜🔴過熱｜FAIL_INSEN｜1,011円｜💰10.3万円｜—
- 9044 NANKAI Co., Ltd.｜granville_oshime｜✅順調(3)｜🟡やや割高｜FAIL_INSEN｜2,982円｜💰29.9万円｜—
- 3107 ダイワボウホールディングス｜granville_oshime｜⚠減速(3)｜🔴過熱｜FAIL_UWAHIGE｜3,548円｜💰36.5万円｜—
- 4044 Central Glass Co., Ltd.｜granville_oshime｜✅順調(3)｜🔴過熱｜FAIL_UWAHIGE｜4,540円｜💰46.2万円｜—
- 4208 UBE Corporation｜granville_oshime｜✅順調(3)｜🔴過熱｜FAIL_INSEN｜3,266円｜💰33.4万円｜—
- 456A Human Made Inc.｜granville_oshime｜✅順調(3)｜🔴過熱｜PASS｜1,891円｜💰18.9万円｜oshime 1858.6 想定損失幅0.5%。｜⚠日程不明
  > 【業態】ストリートファッションなどを主力とするアパレルブランドを展開する。
  > 【いま】終値1,891円・直近5日-3.52%（材料未確認）
  > 【調子】✅順調（3/13） — 質注意
  > 【水準】🔴過熱（0.0/7）— PER52.53倍・PEG5.4581・52週77.1% ／ 💰単元18.9万円
  > 【戦略】1858.6円までの押し目を指値で待つ。SL1849.4円（25日線基準）
- 7504 Kohsoku Corporation｜granville_oshime｜✅順調(3)｜🔴過熱｜PASS｜4,785円｜💰47.9万円｜—｜⛔提案なし(指名鮮度切れ 16営業日)
  > 【業態】食品軽包装資材商社。食品加工業向け中心。東北・北関東地盤。M&Aで拡大。
  > 【いま】終値4,785円・直近5日+6.45%（材料未確認）
  > 【調子】✅順調（3/13） — 質注意
  > 【水準】🔴過熱（0.0/7）— PER23.13倍・PEG5.7141・52週83.2% ／ 💰単元47.9万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 16営業日)）
- 9509 Hokkaido Electric Power Company,Incorporated｜granville_oshime｜🔻悪化(2)｜⚪妥当｜FAIL_UWAHIGE｜1,098円｜💰10.9万円｜—
- 6072 Jibannet Holdings Co., Ltd.｜granville_oshime｜🔻悪化(2)｜🟡やや割高｜PASS｜1,037円｜💰10.4万円｜—｜📋カルテ窓 11/12(残15営業日)｜⚠業績基調が下向き（🔻悪化）｜⛔提案なし(指名鮮度切れ 12営業日)
  > 【業態】地盤解析や品質証明の請負。工事は担わない。FC展開。個人住宅に進出。
  > 【いま】終値1,037円・直近5日-3.36%（材料未確認）
  > 【調子】🔻悪化（2/13） — 質注意
  > 【水準】🟡やや割高（2.8/7）— PER—倍・PEG—・52週48.9% ／ 💰単元10.4万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 12営業日)）
- 9505 Hokuriku Electric Power Company｜granville_oshime｜🔻悪化(2)｜🟡やや割高｜FAIL_UWAHIGE｜1,064円｜💰10.5万円｜—
- 7630 Ichibanya Co., Ltd.｜granville_oshime｜➖横ばい(2)｜🔴過熱｜FAIL_INSEN｜1,062円｜💰10.8万円｜—
- 8043 Starzen Company Limited｜granville_oshime｜➖横ばい(2)｜🔴過熱｜FAIL_INSEN｜1,529円｜💰15.5万円｜—
- 9616 共立メンテナンス｜granville_oshime｜➖横ばい(2)｜🔴過熱｜PASS｜3,421円｜💰34.2万円｜—｜📋カルテ窓 11/09(残12営業日)｜⛔提案なし(指名鮮度切れ 14営業日)
  > 【業態】サービス業
  > 【いま】終値3,421円・直近5日+4.39%（材料未確認）
  > 【調子】➖横ばい（2/13）
  > 【水準】🔴過熱（0.0/7）— PER17.29倍・PEG—・52週90.0% ／ 💰単元34.2万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 14営業日)）
- 9900 Sagami Holdings Corp.｜granville_oshime｜➖横ばい(2)｜🔴過熱｜FAIL_INSEN｜1,127円｜💰11.4万円｜—
- 3048 ビックカメラ｜granville_oshime｜⚠減速(1)｜🟡やや割高｜FAIL_INSEN｜1,712円｜💰17.8万円｜—
- 8255 Axial Retailing, Inc.｜granville_oshime｜⚠減速(1)｜🔴過熱｜FAIL_INSEN｜1,284円｜💰12.7万円｜—
- 8097 SAN-AI OBBLI CO. LTD｜granville_oshime｜⚠減速(1)｜🔴過熱｜FAIL_INSEN｜2,495円｜💰24.8万円｜—
- 8059 Daiichi Jitsugyo Co., Ltd.｜granville_oshime｜⚠減速(0)｜🔴過熱｜FAIL_INSEN｜3,550円｜💰36.0万円｜—
- 8361 Ogaki Kyoritsu Bank, Ltd.｜granville_oshime｜取得不可｜💎割安｜PASS｜1,590円｜💰15.9万円｜—｜📋カルテ窓 11/13(残16営業日)｜⛔型不一致: 既に支持帯以下
  > 【業態】岐阜地盤の地銀大手。近隣県にも営業攻勢。信託業務で相続強化。
  > 【いま】終値1,590円・直近5日-8.57%（材料未確認）
  > 【調子】取得不可
  > 【水準】💎割安（6.0/7）— PER3.17倍・PEG0.0839・52週71.7% ／ 💰単元15.9万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 9166 GENDA Inc.｜granville_oshime｜業績データ取得不可｜🟢値頃｜PASS｜693円｜💰6.9万円｜oshime 673.5 想定損失幅0.5%。｜⚠日程不明
  > 【業態】「GiGO」ブランドを主としたアミューズメント施設の運営。M&Aで成長。
  > 【いま】終値693円・直近5日+0.73%（材料未確認）
  > 【調子】業績データ取得不可
  > 【水準】🟢値頃（5.6/7）— PER—倍・PEG—・52週56.9% ／ 💰単元6.9万円
  > 【戦略】673.5円までの押し目を指値で待つ。SL670.1円（25日線基準）
- 8343 Akita Bank, Ltd.｜granville_oshime｜業績データ取得不可(売上/経常欠損)｜🟢値頃｜PASS｜1,483円｜💰14.8万円｜—｜📋カルテ窓 11/13(残16営業日)｜⛔型不一致: 既に支持帯以下
  > 【業態】秋田地盤の地銀中位。預金、融資とも県内シェア５割超。福島・北海道にも。
  > 【いま】終値1,483円・直近5日-6.61%（材料未確認）
  > 【調子】業績データ取得不可(売上/経常欠損)
  > 【水準】🟢値頃（5.0/7）— PER15.58倍・PEG0.9449・52週55.6% ／ 💰単元14.8万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 8367 Nanto Bank Ltd.｜granville_oshime｜取得不可｜🟢値頃｜PASS｜1,818円｜💰18.2万円｜—｜📋カルテ窓 11/10(残13営業日)｜⛔型不一致: 既に支持帯以下
  > 【業態】奈良地盤の地銀で県内シェアは圧倒的。効率経営に定評。中小企業に積極。
  > 【いま】終値1,818円・直近5日-3.45%（材料未確認）
  > 【調子】取得不可
  > 【水準】🟢値頃（5.0/7）— PER12.98倍・PEG0.4194・52週73.1% ／ 💰単元18.2万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 336A ダイナミックマッププラットフォーム｜granville_oshime｜業績データ取得不可(経常益予想非開示)｜⚪妥当｜FAIL_UWAHIGE｜1,314円｜💰13.2万円｜—
- 6027 Bengo4.com, Inc.｜granville_oshime｜業績データ取得不可｜🟡やや割高｜FAIL_INSEN｜4,870円｜💰48.1万円｜—
- 8362 Fukui Bank, Ltd.｜granville_oshime｜🔻悪化｜🔴過熱｜PASS｜6,930円｜💰69.3万円｜—｜📋カルテ窓 11/13(残16営業日)｜⚠業績基調が下向き（🔻悪化）｜⛔型不一致: 既に支持帯以下
  > 【業態】福井地盤の地銀中位。石川や富山にも展開。福邦銀と26年5月合併。
  > 【いま】終値6,930円・直近5日-4.28%（材料未確認）
  > 【調子】🔻悪化
  > 【水準】🔴過熱（1.4/7）— PER18.22倍・PEG—・52週72.7% ／ 💰単元69.3万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 8410 Seven Bank, Ltd.｜granville_oshime｜—｜—｜FAIL_INSEN｜335円｜💰—｜—
- 8622 Mito Securities Co., Ltd.｜granville_oshime｜取得不可｜⏸判定不能｜PASS_DOJI｜783円｜💰7.8万円｜—｜📑TOPIX低減対象（次 10/30 第1回/8）｜⛔型不一致: 既に支持帯以下
  > 【業態】北関東地盤の独立系証券。地元密着の営業に強み。ファンドラップに注力。
  > 【いま】終値783円・直近5日-5.21%（材料未確認）
  > 【調子】取得不可
  > 【水準】⏸判定不能（None/7）— PER—倍・PEG—・52週56.5% ／ 💰単元7.8万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 8624 Ichiyoshi Securities Co., Ltd.｜granville_oshime｜取得不可｜⏸判定不能｜FAIL_INSEN｜1,556円｜💰15.7万円｜—
- 8628 松井証券｜granville_oshime｜業績データ取得不可｜⏸判定不能｜FAIL_UWAHIGE｜1,088円｜💰11.1万円｜—
- 8708 アイザワ証券グループ｜granville_oshime｜取得不可｜⏸判定不能｜FAIL_INSEN｜1,549円｜💰16.1万円｜—
- 6769 Thine Electronics, Inc.｜granville_rebound｜🚀確変(11)｜⚪妥当｜FAIL_INSEN｜1,041円｜💰11.1万円｜—
- 3691 DIGITAL PLUS, Inc.｜granville_rebound｜🔥絶好調(10)｜⚪妥当｜PASS｜1,693円｜💰16.9万円｜reversal 1693 想定損失幅4.1%。｜📋カルテ窓 11/13(残16営業日)
  > 【業態】金券をキャッシュレスで贈るデジタルギフト事業が主力。デジタルマーケティングは譲渡。
  > 【いま】終値1,693円・直近5日-5.47%（材料未確認）
  > 【調子】🔥絶好調（10/13） — 営業益代替・黒字転換
  > 【水準】⚪妥当（4.2/7）— PER—倍・PEG—・52週44.1% ／ 💰単元16.9万円
  > 【戦略】当日終値1693円の指値で反転を取りにいく。SL1624円（直近5日安値）
- 2122 インタースペース｜granville_rebound｜🔥絶好調(9)｜⚪妥当｜FAIL_INSEN｜1,318円｜💰13.4万円｜—
- 6963 ROHM Company Limited｜granville_rebound｜🔥絶好調(9)｜⚪妥当｜PASS_DOJI｜3,958円｜💰39.6万円｜reversal 3958 想定損失幅1.8%。｜📋カルテ窓 11/05(残10営業日)
  > 【業態】カスタムLSIで首位。半導体素子、抵抗器などに強み。SiCパワー半導体が拡大。
  > 【いま】終値3,958円・直近5日-13.60%（材料未確認）
  > 【調子】🔥絶好調（9/13）
  > 【水準】⚪妥当（4.0/7）— PER52.70倍・PEG0.6038・52週48.4% ／ 💰単元39.6万円
  > 【戦略】当日終値3958円の指値で反転を取りにいく。SL3888円（直近5日安値）
- 8995 Makoto Construction Co,Ltd｜granville_rebound｜🔥絶好調(9)｜⚪妥当｜FAIL_INSEN｜1,590円｜💰16.5万円｜—
- 5242 EYEZ INC.｜granville_rebound｜⚡好調(7)｜🔴過熱｜FAIL_INSEN｜2,868円｜💰28.7万円｜—
- 2354 YE DIGITAL CORPORATION｜granville_rebound｜⚡好調(5)｜🟢値頃｜FAIL_INSEN｜1,019円｜💰10.8万円｜—
- 6597 HPC SYSTEMS Inc.｜granville_rebound｜⚡好調(5)｜🟢値頃｜FAIL_INSEN｜3,230円｜💰35.6万円｜—
- 3687 Fixstars Corp.｜granville_rebound｜⚡好調(5)｜⚪妥当｜FAIL_INSEN｜1,948円｜💰21.0万円｜—
- 5574 ABEJA,Inc.｜granville_rebound｜⚡好調(5)｜🟡やや割高｜FAIL_INSEN｜2,437円｜💰24.4万円｜—
- 8524 North Pacific Bank, Ltd.｜granville_rebound｜⚠減速(4)｜⚪妥当｜PASS｜1,159円｜💰11.6万円｜reversal 1159 想定損失幅2.5%。｜📋カルテ窓 11/13(残16営業日)｜⚠業績基調が下向き（⚠減速）
  > 【業態】北海道地盤で資金量第２地銀最大。拓銀と札幌銀の取込で拡大。
  > 【いま】終値1,159円・直近5日-4.92%（材料未確認）
  > 【調子】⚠減速（4/13） — 減収・質注意
  > 【水準】⚪妥当（4.2/7）— PER14.75倍・PEG0.8058・52週65.4% ／ 💰単元11.6万円
  > 【戦略】当日終値1159円の指値で反転を取りにいく。SL1130円（直近5日安値）
- 4997 日本農薬｜granville_rebound｜✅順調(4)｜🟡やや割高｜PASS｜1,074円｜💰10.7万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）｜⛔提案なし(指名鮮度切れ 11営業日)
  > 【業態】農薬大手。自社開発品比率大。医薬品や動物薬。スマート農業連携アプリ注力。
  > 【いま】終値1,074円・直近5日-0.65%（材料未確認）
  > 【調子】✅順調（4/13）
  > 【水準】🟡やや割高（2.0/7）— PER11.37倍・PEG2.5294・52週48.7% ／ 💰単元10.7万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 11営業日)）
- 1407 West Holdings Corporation｜granville_rebound｜✅順調(3)｜🟢値頃｜FAIL_UWAHIGE｜2,192円｜💰22.7万円｜—
- 4346 NEXYZ.Group Corporation｜granville_rebound｜✅順調(3)｜🟢値頃｜PASS｜752円｜💰7.5万円｜—｜📋カルテ窓 11/16(残17営業日)｜⛔提案なし(指名鮮度切れ 12営業日)
  > 【業態】LED照明、空調、業務機器のレンタル主力。電子メディア・雑誌、エンタメ、定額制エステも。
  > 【いま】終値752円・直近5日-1.44%（材料未確認）
  > 【調子】✅順調（3/13）
  > 【水準】🟢値頃（5.0/7）— PER10.30倍・PEG1.1358・52週20.0% ／ 💰単元7.5万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 12営業日)）
- 7354 Direct Marketing MiX Inc.｜granville_rebound｜✅順調(3)｜⚪妥当｜FAIL_INSEN｜342円｜💰3.5万円｜—
- 2681 2nd RETAILING Co., Ltd.｜granville_rebound｜✅順調(3)｜🟡やや割高｜FAIL_INSEN｜2,025円｜💰21.9万円｜—
- 4082 第一稀元素化学工業｜granville_rebound｜🔻悪化(3)｜🟡やや割高｜FAIL_INSEN｜1,815円｜💰18.7万円｜—
- 3653 Morpho, Inc.｜granville_rebound｜🔻悪化(2)｜💎割安｜PASS｜907円｜💰9.1万円｜reversal 907 想定損失幅6.5%。｜⚠日程不明｜⚠業績基調が下向き（🔻悪化）｜⚠バリュートラップ疑い
  > 【業態】画像処理ソフト開発。手ぶれ補正などロイヤリティーが収益。画像等AI活用に注力。
  > 【いま】終値907円・直近5日+2.37%（材料未確認）
  > 【調子】🔻悪化（2/13） — 質注意
  > 【水準】💎割安（7.0/7）— PER—倍・PEG—・52週31.2% ／ 💰単元9.1万円
  > 【戦略】当日終値907円の指値で反転を取りにいく。SL848円（直近5日安値）
- 3907 Silicon Studio Corp.｜granville_rebound｜🔻悪化(2)｜🟢値頃｜FAIL_INSEN｜1,462円｜💰16.2万円｜—
- 4440 WITZ Corp.｜granville_rebound｜➖横ばい(2)｜🔴過熱｜FAIL_UWAHIGE｜1,813円｜💰18.8万円｜—
- 8163 SRS HOLDINGS CO.,LTD.｜granville_rebound｜➖横ばい(2)｜🔴過熱｜FAIL_INSEN｜1,652円｜💰16.8万円｜—
- 4691 Washington Hotel Corp.｜granville_rebound｜⚠減速(1)｜⚪妥当｜FAIL_INSEN｜1,834円｜💰19.1万円｜—
- 6203 Howa Machinery, Ltd.｜granville_rebound｜⚠減速(1)｜🟡やや割高｜FAIL_INSEN｜2,023円｜💰20.8万円｜—
- 6522 アスタリスク｜granville_rebound｜⚠減速(0)｜⚪妥当｜FAIL_UWAHIGE｜879円｜💰9.2万円｜—
- 8360 Yamanashi Chuo Bank, Ltd.｜granville_rebound｜取得不可｜💎割安｜PASS｜1,301円｜💰13.0万円｜reversal 1301 想定損失幅4.0%。｜📋カルテ窓 11/13(残16営業日)
  > 【業態】未取得（次回以降に取得）
  > 【いま】終値1,301円・直近5日-3.99%（材料未確認）
  > 【調子】取得不可
  > 【水準】💎割安（6.0/7）— PER3.19倍・PEG0.0989・52週69.0% ／ 💰単元13.0万円
  > 【戦略】当日終値1301円の指値で反転を取りにいく。SL1249円（直近5日安値）
- 3778 SAKURA Internet Inc.｜granville_rebound｜業績データ取得不可｜🟢値頃｜PASS_DOJI｜3,160円｜💰31.6万円｜reversal 3160 想定損失幅1.9%。｜⏰決算 10/28(残5営業日)
  > 【業態】情報・通信業（データセンター・ホスティング・クラウドコンピューティング関連）
  > 【いま】終値3,160円・直近5日-9.84%（材料未確認）
  > 【調子】業績データ取得不可
  > 【水準】🟢値頃（5.0/7）— PER84.27倍・PEG0.0403・52週37.4% ／ 💰単元31.6万円
  > 【戦略】当日終値3160円の指値で反転を取りにいく。SL3100円（直近5日安値）
- 8366 Shiga Bank, Ltd.｜granville_rebound｜取得不可｜⚪妥当｜PASS｜2,694円｜💰26.9万円｜reversal 2694 想定損失幅2.6%。｜📋カルテ窓 11/13(残16営業日)
  > 【業態】滋賀県内で優位。徹底した収益管理体制。環境関連の法人融資に注力。
  > 【いま】終値2,694円・直近5日-8.62%（材料未確認）
  > 【調子】取得不可
  > 【水準】⚪妥当（3.0/7）— PER21.73倍・PEG0.4826・52週75.5% ／ 💰単元26.9万円
  > 【戦略】当日終値2694円の指値で反転を取りにいく。SL2623円（直近5日安値）
- 8368 Hyakugo Bank, Ltd.｜granville_rebound｜取得不可｜🟡やや割高｜PASS｜2,186円｜💰21.9万円｜reversal 2186 想定損失幅3.4%。｜📋カルテ窓 11/10(残13営業日)
  > 【業態】三重地盤の地銀上位。県内で圧倒的。三菱UFJ、十六銀、名古屋銀と親密。
  > 【いま】終値2,186円・直近5日-6.62%（材料未確認）
  > 【調子】取得不可
  > 【水準】🟡やや割高（2.0/7）— PER18.26倍・PEG1.6226・52週69.3% ／ 💰単元21.9万円
  > 【戦略】当日終値2186円の指値で反転を取りにいく。SL2111円（直近5日安値）
- 8713 Fidea Holdings Co.Ltd.｜granville_rebound｜業績データ取得不可(売上/経常欠損)｜🔴過熱｜PASS｜2,433円｜💰24.3万円｜reversal 2433 想定損失幅4.8%。｜📋カルテ窓 11/13(残16営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
  > 【業態】荘内銀、北都銀が県を超えて統合。山形・秋田が地盤。27年1月両行合併へ。
  > 【いま】終値2,433円・直近5日-2.01%（材料未確認）
  > 【調子】業績データ取得不可(売上/経常欠損)
  > 【水準】🔴過熱（1.4/7）— PER13.68倍・PEG—・52週63.1% ／ 💰単元24.3万円
  > 【戦略】当日終値2433円の指値で反転を取りにいく。SL2317円（直近5日安値）
- 477A Startline CO.,LTD.｜granville_rebound｜—｜—｜FAIL_UWAHIGE｜727円｜💰—｜—
- 6645 OMRON Corporation｜granville_rebound｜—｜—｜FAIL_INSEN｜5,693円｜💰—｜—
- 6890 Ferrotec Corporation｜granville_rebound｜—｜—｜FAIL_INSEN｜8,390円｜💰—｜—
- 7175 Imamura Securities Co.Ltd.｜granville_rebound｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜1,707円｜💰18.6万円｜—
- 7380 Juroku Financial Group,Inc.｜granville_rebound｜—｜—｜FAIL_UWAHIGE｜2,427円｜💰—｜—
- 8334 Gunma Bank, Ltd.｜granville_rebound｜—｜—｜FAIL_UWAHIGE｜2,679円｜💰—｜—
- 9278 BOOKOFF GROUP HOLDINGS LIMITED｜granville_rebound｜—｜—｜FAIL_INSEN｜2,490円｜💰—｜—

## 変化点銘柄
- 5803 フジクラ｜変化点🔔｜🚀確変(12)｜🟢値頃｜FAIL_INSEN｜4,347円｜💰44.8万円｜—
- 4011 Headwaters Co.,Ltd｜変化点🔔｜🚀確変(11)｜🟢値頃｜PASS｜2,238円｜💰22.4万円｜changepoint 2238 想定損失幅5.5%。｜📋カルテ窓 11/13(残16営業日)｜🔒実弾封印中(PL3紙ログ収集中)
  > 【業態】企業の経営課題をAIシステム開発を通して解決するソリューション事業。保守運用も。
  > 【いま】終値2,238円・直近5日-3.74%（材料未確認）
  > 【調子】🚀確変（11/13）
  > 【水準】🟢値頃（5.0/7）— PER35.02倍・PEG0.0913・52週21.5% ／ 💰単元22.4万円
  > 【戦略】発火日終値2238円の指値。追撃禁止・SL2115円。🔒実弾封印中（PL3紙ログ収集中）
- 6254 野村マイクロ・サイエンス｜変化点🔔｜🔥絶好調(10)｜💎割安｜FAIL_INSEN｜3,085円｜💰31.6万円｜—
- 4187 大阪有機化学工業｜変化点｜🔥絶好調(10)｜⚪妥当｜FAIL_INSEN｜4,635円｜💰49.2万円｜—
- 7695 交換できるくん｜変化点🔔｜🔥絶好調(10)｜⚪妥当｜PASS｜885円｜💰8.8万円｜changepoint 885 想定損失幅6.8%。｜📋カルテ窓 11/13(残16営業日)｜🔒実弾封印中(PL3紙ログ収集中)
  > 【業態】住宅設備機器と工事をセットでネット販売。見積もり、注文をネットで低価格化。
  > 【いま】終値885円・直近5日+5.99%（材料未確認）
  > 【調子】🔥絶好調（10/13）
  > 【水準】⚪妥当（4.0/7）— PER26.42倍・PEG0.1794・52週74.7% ／ 💰単元8.8万円
  > 【戦略】発火日終値885円の指値。追撃禁止・SL825円。🔒実弾封印中（PL3紙ログ収集中）
- 6080 Ｍ＆Ａキャピタルパートナーズ｜変化点｜🔥絶好調(10)｜⚪妥当｜FAIL_UWAHIGE｜4,300円｜💰44.3万円｜—
- 584A LiNKX, Inc.｜変化点🔔｜🔥絶好調(9)｜🟢値頃｜FAIL_UWAHIGE｜2,226円｜💰23.1万円｜—
- 6136 OSG CORP｜変化点｜🔥絶好調(9)｜⚪妥当｜FAIL_UWAHIGE｜3,734円｜💰38.6万円｜—
- 6857 アドバンテスト｜変化点｜🔥絶好調(9)｜⚪妥当｜FAIL_INSEN｜34,440円｜💰344.5万円｜—
- 8151 東陽テクニカ｜変化点🔔｜🔥絶好調(9)｜⚪妥当｜FAIL_INSEN｜1,868円｜💰19.2万円｜—
- 9962 ミスミグループ本社｜変化点｜🔥絶好調(9)｜⚪妥当｜FAIL_UWAHIGE｜3,836円｜💰39.4万円｜—
- 4382 HEROZ, Inc.｜変化点🔔｜🔥絶好調(9)｜🟡やや割高｜PASS｜1,631円｜💰16.3万円｜changepoint 1631 想定損失幅19.4%。⚠1単元でリスク枠超過（31,600円）｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）｜🔒実弾封印中(PL3紙ログ収集中)
  > 【業態】未取得（次回以降に取得）
  > 【いま】終値1,631円・直近5日+16.50%（材料未確認）
  > 【調子】🔥絶好調（9/13）
  > 【水準】🟡やや割高（2.0/7）— PER96.51倍・PEG1.3485・52週79.3% ／ 💰単元16.3万円
  > 【戦略】発火日終値1631円の指値。追撃禁止・SL1315円。🔒実弾封印中（PL3紙ログ収集中）／⚠1単元リスク31,600円（枠超過）
- 7318 セレンディップ・ホールディングス｜変化点🔔｜🔥絶好調(8)｜💎割安｜FAIL_UWAHIGE｜1,208円｜💰12.4万円｜—
- 9888 UEX LTD｜変化点｜🔥絶好調(8)｜🟢値頃｜PASS｜1,182円｜💰11.8万円｜changepoint 1182 想定損失幅1.9%。｜📋カルテ窓 11/10(残13営業日)｜🔒実弾封印中(PL3紙ログ収集中)
  > 【業態】ステンレス鋼の専門商社。生産材が中心。中国での加工品製販や機械の製販も。
  > 【いま】終値1,182円・直近5日-2.64%（材料未確認）
  > 【調子】🔥絶好調（8/13）
  > 【水準】🟢値頃（5.0/7）— PER4.06倍・PEG0.0543・52週76.6% ／ 💰単元11.8万円
  > 【戦略】発火日終値1182円の指値。追撃禁止・SL1160円。🔒実弾封印中（PL3紙ログ収集中）
- 4368 4368｜変化点｜🔥絶好調(8)｜⚪妥当｜FAIL_UWAHIGE｜3,060円｜💰31.6万円｜—
- 5582 （名称取得不可）｜変化点🔔｜🔥絶好調(8)｜⚪妥当｜FAIL_UWAHIGE｜1,955円｜💰19.9万円｜—
- 4431 スマレジ｜変化点｜🔥絶好調(8)｜🟡やや割高｜FAIL_INSEN｜3,800円｜💰40.7万円｜—
- 5590 NETSTARS Co.,Ltd.｜変化点🔔｜⚡好調(7)｜🟢値頃｜PASS_DOJI｜675円｜💰6.8万円｜changepoint 675 想定損失幅0.4%。｜📋カルテ窓 11/12(残15営業日)｜🔒実弾封印中(PL3紙ログ収集中)
  > 【業態】マルチQRコード決済サービス「StarPay」の提供などを手掛ける。
  > 【いま】終値675円・直近5日-6.64%（材料未確認）
  > 【調子】⚡好調（7/13）
  > 【水準】🟢値頃（5.0/7）— PER23.20倍・PEG0.3892・52週10.4% ／ 💰単元6.8万円
  > 【戦略】発火日終値675円の指値。追撃禁止・SL672円。🔒実弾封印中（PL3紙ログ収集中）
- 478A Hutzper Inc.｜変化点🔔｜⚡好調(7)｜⚪妥当｜PASS｜680円｜💰6.8万円｜changepoint 680 想定損失幅2.6%。｜📋カルテ窓 11/16(残17営業日)｜🔒実弾封印中(PL3紙ログ収集中)
  > 【業態】外観検査自動化AI「メキキバイト」など、製造業向けにAIサービスを提供する。
  > 【いま】終値680円・直近5日-3.00%（材料未確認）
  > 【調子】⚡好調（7/13） — 質注意
  > 【水準】⚪妥当（4.0/7）— PER19.94倍・PEG0.7997・52週2.7% ／ 💰単元6.8万円
  > 【戦略】発火日終値680円の指値。追撃禁止・SL662円。🔒実弾封印中（PL3紙ログ収集中）
- 3091 ブロンコビリー｜変化点｜⚡好調(7)｜🟡やや割高｜FAIL_INSEN｜2,940円｜💰29.6万円｜—
- 8704 トレイダーズホールディングス｜変化点｜⚡好調(5)｜💎割安｜FAIL_UWAHIGE｜1,320円｜💰13.2万円｜—
- 6284 日精エー・エス・ビー機械｜変化点🔔｜⚡好調(5)｜🟢値頃｜FAIL_INSEN｜8,330円｜💰85.4万円｜—
- 218A Liberaware｜変化点｜⚡好調(5)｜⚪妥当｜PASS_DOJI｜930円｜💰9.3万円｜changepoint 930 想定損失幅2.0%。｜⚠日程不明｜🔒実弾封印中(PL3紙ログ収集中)
  > 【業態】産業分野に特化した非GPS型小型ドローンの開発・運用。屋内・狭空間に強み。
  > 【いま】終値930円・直近5日-7.09%（材料未確認）
  > 【調子】⚡好調（5/13）
  > 【水準】⚪妥当（4.2/7）— PER—倍・PEG—・52週17.8% ／ 💰単元9.3万円
  > 【戦略】発火日終値930円の指値。追撃禁止・SL911円。🔒実弾封印中（PL3紙ログ収集中）
- 6785 鈴木｜変化点｜✅順調(4)｜⚪妥当｜FAIL_UWAHIGE｜3,365円｜💰34.0万円｜—
- 593A ティアフォー｜変化点｜✅順調(4)｜🟡やや割高｜PASS_DOJI｜2,010円｜💰20.1万円｜changepoint 2010 想定損失幅4.1%。｜📋カルテ窓 11/13(残16営業日)｜📑TOPIX新規採用（2026-10-30 組入）｜🔒実弾封印中(PL3紙ログ収集中)
  > 【業態】自動運転ソフトウェア「Autoware」を活用した自動運転車両の開発を手掛ける。
  > 【いま】終値2,010円・直近5日-10.27%（材料未確認）
  > 【調子】✅順調（4/13） — 赤字・上限適用・質注意
  > 【水準】🟡やや割高（2.8/7）— PER—倍・PEG—・52週39.0% ／ 💰単元20.1万円
  > 【戦略】発火日終値2010円の指値。追撃禁止・SL1927円。🔒実弾封印中（PL3紙ログ収集中）
- 4165 PLAID Inc.｜変化点🔔｜🔻悪化(4)｜🔴過熱｜FAIL_UWAHIGE｜775円｜💰7.7万円｜—
- 4498 Cybertrust Japan Co., Ltd.｜変化点🔔｜✅順調(4)｜🔴過熱｜PASS｜2,060円｜💰20.6万円｜changepoint 2060 想定損失幅28.2%。⚠1単元でリスク枠超過（58,000円）｜🔒実弾封印中(PL3紙ログ収集中)
  > 【業態】情報・通信業
  > 【いま】終値2,060円・直近5日+10.69%（材料未確認）
  > 【調子】✅順調（4/13）
  > 【水準】🔴過熱（1.0/7）— PER27.25倍・PEG2.1501・52週85.3% ／ 💰単元20.6万円
  > 【戦略】発火日終値2060円の指値。追撃禁止・SL1480円。🔒実弾封印中（PL3紙ログ収集中）／⚠1単元リスク58,000円（枠超過）
- 4071 Plus Alpha Consulting Co. LTD.｜変化点🔔｜✅順調(3)｜⚪妥当｜FAIL_INSEN｜2,276円｜💰22.6万円｜—
- 598A チャットプラス｜変化点🔔｜✅順調(3)｜⚪妥当｜FAIL_UWAHIGE｜1,195円｜💰12.3万円｜—
- 4418 Japan Data Science Consortium Co Ltd.｜変化点🔔｜⚠減速(3)｜🟡やや割高｜FAIL_INSEN｜1,088円｜💰11.6万円｜—
- 4493 Cyber Security Cloud, Inc.｜変化点🔔｜✅順調(3)｜🔴過熱｜FAIL_INSEN｜3,165円｜💰38.1万円｜—
- 339A PROGRESS TECHNOLOGIES GROUP INC｜変化点｜➖横ばい(2)｜⚪妥当｜PASS_DOJI｜825円｜💰8.2万円｜changepoint 825 想定損失幅0.8%。｜⚠日程不明｜🔒実弾封印中(PL3紙ログ収集中)
  > 【業態】大手製造業向けにデジタルツイン技術導入のコンサルティングなどを手掛ける。
  > 【いま】終値825円・直近5日-9.54%（材料未確認）
  > 【調子】➖横ばい（2/13） — 質注意
  > 【水準】⚪妥当（4.0/7）— PER6.25倍・PEG—・52週0.9% ／ 💰単元8.2万円
  > 【戦略】発火日終値825円の指値。追撃禁止・SL818円。🔒実弾封印中（PL3紙ログ収集中）
- 4488 AI inside Inc.｜変化点｜➖横ばい(2)｜🟡やや割高｜FAIL_INSEN｜2,010円｜💰21.2万円｜—
- 4259 ExaWizards Inc.｜変化点｜業績データ取得不可｜⚪妥当｜FAIL_INSEN｜777円｜💰8.1万円｜—
- 4478 freee K.K.｜変化点🔔｜業績データ取得不可｜⚪妥当｜FAIL_UWAHIGE｜3,920円｜💰37.9万円｜—
- 3993 PKSHA Technology, Inc.｜変化点🔔｜業績データ取得不可｜⚪妥当｜FAIL_UWAHIGE｜3,605円｜💰36.4万円｜—

## 🤖AI特需銘柄
波: wave_on なし／25MA 上回り率 エネマネ 14.29%・冷却 33.33%・光 9.09%・基板 9.52%
- 3131 シンデンハイテックス｜ai_momentum｜🚀確変(12)｜💎割安｜FAIL_INSEN｜6,710円｜💰73.6万円｜—
- 2760 東京エレクトロンデバイス｜ai_momentum｜🔥絶好調(10)｜⚪妥当｜FAIL_INSEN｜4,570円｜💰49.2万円｜—
- 9824 泉州電業｜ai_momentum｜🔥絶好調(10)｜⚪妥当｜PASS_DOJI｜7,990円｜💰79.9万円｜momentum 8190 想定損失幅6.1%。⚠1単元でリスク枠超過（50,080円）｜⚠日程不明
  > 【業態】電線専門商社。FA・機器・通信・電力向け電線、光ファイバーが軸。即納制に強み。
  > 【いま】終値7,990円・直近5日-6.77%（材料未確認）
  > 【調子】🔥絶好調（10/13）
  > 【水準】⚪妥当（4.0/7）— PER14.87倍・PEG0.3699・52週85.5% ／ 💰単元79.9万円
  > 【戦略】当日高値超えの逆指値8190円で順張り参戦を検討。上限8271.9円・SL7689.2円目安／⚠1単元リスク50,080円（枠超過）
- 6521 オキサイド｜ai_momentum｜⚡好調(7)｜🟢値頃｜FAIL_INSEN｜3,230円｜💰33.8万円｜—
- 1982 日比谷総合設備｜ai_momentum｜⚠減速(1)｜🔴過熱｜FAIL_UWAHIGE｜3,230円｜💰33.5万円｜—
- 9960 トーテック｜ai_momentum｜⚠減速(1)｜🔴過熱｜FAIL_INSEN｜4,295円｜💰43.2万円｜—
- 4062 IBIDEN CO., LTD.｜ai_reversal｜🔥絶好調(9)｜⚪妥当｜FAIL_INSEN｜9,500円｜💰97.6万円｜—
- 6981 村田製作所｜ai_reversal｜🔥絶好調(9)｜⚪妥当｜FAIL_INSEN｜6,756円｜💰68.0万円｜—
- 7433 伯東｜ai_reversal｜🔥絶好調(9)｜⚪妥当｜FAIL_INSEN｜1,813円｜💰54.1万円｜—
- 6752 パナソニックHD｜ai_reversal｜⚠減速(7)｜⚪妥当｜FAIL_INSEN｜3,905円｜💰39.8万円｜—
- 6779 Nihon Dempa Kogyo Co., Ltd.｜ai_reversal｜⚡好調(7)｜⚪妥当｜FAIL_INSEN｜2,843円｜💰28.9万円｜—
- 6754 アンリツ｜ai_reversal｜⚡好調(7)｜⚪妥当｜FAIL_INSEN｜2,968円｜💰30.3万円｜—
- 4658 日本空調サービス｜ai_reversal｜⚡好調(5)｜⚪妥当｜FAIL_INSEN｜1,552円｜💰15.7万円｜—
- 8098 稲畑産業｜ai_reversal｜✅順調(4)｜🔴過熱｜FAIL_INSEN｜4,420円｜💰44.8万円｜—
- 5208 Arisawa Mfg.Co., Ltd.｜ai_reversal｜✅順調(4)｜🔴過熱｜FAIL_INSEN｜2,697円｜💰28.3万円｜—
- 6643 戸上電機製作所｜ai_reversal｜✅順調(3)｜⚪妥当｜PASS｜5,270円｜💰52.7万円｜reversal 5270 想定損失幅3.8%。
  > 【業態】高圧電力配電制御システム。電力向け依存度大。中国生産拡大。
  > 【いま】終値5,270円・直近5日-4.36%（材料未確認）
  > 【調子】✅順調（3/13） — 質注意
  > 【水準】⚪妥当（3.0/7）— PER8.57倍・PEG28.4919・52週43.9% ／ 💰単元52.7万円
  > 【戦略】当日終値5270円の指値で反転を取りにいく。SL5070円（直近5日安値）
- 3103 ユニチカ｜ai_reversal｜🔻悪化(2)｜🟡やや割高｜FAIL_UWAHIGE｜1,316円｜💰13.3万円｜—
- 5302 日本カーボン｜ai_reversal｜➖横ばい(2)｜🔴過熱｜FAIL_INSEN｜4,995円｜💰50.9万円｜—
- 6590 芝浦メカトロニクス｜ai_reversal｜➖横ばい(2)｜🔴過熱｜FAIL_UWAHIGE｜3,435円｜💰39.5万円｜—
- 9432 NTT｜ai_reversal｜➖横ばい(2)｜🔴過熱｜FAIL_UWAHIGE｜176円｜💰1.8万円｜—

## ⚡材料後出し
その日の足は開示前の情報。判定は参考値
- 8953 Japan Metropolitan Fund Investment Corporation｜FAIL_UWAHIGE｜📊2026年8月期　決算短信(REIT)｜16:00
- 6196 Strike Group Co. Ltd.｜FAIL_INSEN｜📌2026年９月期通期連結業績予想の修正に関するお知らせ｜15:30

## 📢開示
使用URL: https://kabutan.jp/disclosures/?kubun=&date=20261021&page=1〜19（全19ページ・273行を取得。フォールバックなし）。
- 📊 8953 都市ファンド｜2026年8月期　決算短信(REIT)｜16:00
- 📌 276A ククレブ｜2026年8月期 決算説明会 WEB動画配信に関するお知らせ｜10:00
- 📌 4272 日化薬｜日本化薬従業員持株会向け譲渡制限付株式としての自己株式の処分の払込完了及び一部失権に関するお知らせ｜12:00
- 📌 6196 ストライクＧ｜2026年９月期通期連結業績予想の修正に関するお知らせ｜15:30
- 📌 8953 都市ファンド｜2026年8月期（第49期）決算概要｜16:00
①-9へ引き渡し1件

## 総当りゲート
### 5手法
- PASS（29）: 5137 Smart Drive Co. Ltd.、276A CCReB Advisors Inc.、5136 tripla Co.,Ltd.、618A KOMPEITO Inc.、421A Movin' Strategic Career CO.,LTD.、5537 AlbaLink Co.,Ltd.、5821 Hirakawa Hewtech Corp.、4477 BASE, Inc.、505A Geekly,Inc.、5038 eWeLL Co.,Ltd、7567 Sakae Electronics Corp.、269A SAPEET、3843 Freebit Co., Ltd.、4331 Take and Give. Needs Co., Ltd.、7161 Jimoto Holdings, Inc.、3186 ネクステージ、8393 Miyazaki Bank Ltd.、1820 Nishimatsu Construction Co., Ltd.、1952 Shin Nippon Air Technologies Co., Ltd.、6183 BELLSYSTEM24 Holdings, Inc.、1662 Japan Petroleum Exploration Co., Ltd.、8194 Life Corporation、7381 CCI Group, Inc.、8345 Bank of Iwate Ltd.、8399 Bank Of The Ryukyus,Limited、7384 Procrea Holdings,Inc.、8304 Aozora Bank, Ltd.、3498 霞ヶ関Ｃ、6643 戸上電機製作所
- PASS_DOJI（5）: 5757 CK San-Etsu Co., Ltd.、6269 Modec, Inc.、5631 Japan Steel Works, Ltd.、9824 泉州電業、5590 NETSTARS Co.,Ltd.
- FAIL_UWAHIGE（46）: 4053 Sun Asterisk, Inc.、5027 AnyMind Group Inc.、9554 AViC Co. Ltd.、5132 pluszero,Inc.、4377 ONE CAREER Inc.、3915 TerraSky Co., Ltd.、4058 Toyokumo, Inc.、6071 IBJ, Inc.、558A SQUEEZE Inc.、147A SORACOM,INC.、7678 ASAKUMA CO.,LTD.、9268 OPTIMUS GROUP Co., Ltd.、4412 Science Arts, Inc.、6289 Giken Ltd.、3077 Horiifoodservice Co., Ltd.、2930 北の達人コーポレーション、2820 Yamami Co.、4565 Nxera Pharma Co., Ltd.、446A ノースサンド、8522 Bank of Nagoya, Ltd.、8386 Hyakujushi Bank, Ltd.、8381 San-in Godo Bank Ltd.、3279 Activia Properties, Inc.、2805 S&B Foods Inc.、5021 Cosmo Energy Holdings Co., Ltd.、1333 Umios Corporation、8953 Japan Metropolitan Fund Investment Corporation、5844 Kyoto Financial Group,Inc.、1893 Penta-Ocean Construction Co., Ltd.、9948 Arcs Company, Limited、3283 Nippon Prologis REIT, Inc.、3292 AEON REIT Investment Corp.、3462 Nomura Real Estate Master Fund, Inc.、9436 Okinawa Cellular Telephone Company、1969 Takasago Thermal Engineering Co., Ltd.、9533 TOHO GAS Co., Ltd.、5831 Shizuoka Financial Group, Inc.、8511 Japan Securities Finance Co., Ltd.、7713 シグマ光機、7811 Nakamoto Packs Co. Ltd.、6532 ベイカレント、4176 ココナラ、1982 日比谷総合設備、6590 芝浦メカトロニクス、9432 NTT、9211 f-code Inc.
- FAIL_INSEN（109）: 6627 Tera Probe, Inc.、6862 Minato Holdings Inc.、4434 Serverworks Co., Ltd.、212A FIT EASY Inc.、6298 Y.A.C.HOLDINGS CO.,LTD.、9556 INTLOOP, Inc.、7047 PORT INC.、5034 unerry, Inc.、9560 PROGRIT, Inc.、9628 San Holdings,Inc.、2980 SRE Holdings Corp.、6629 TECHNO HORIZON Co., Ltd.、6918 Aval Data Corporation、6337 Tesec Corporation、3696 セレス、2340 Gokurakuyu Holdings Co., Ltd.、8871 GOLDCREST Co., Ltd.、3391 TSURUHA Holdings, Inc.、6324 Harmonic Drive Systems Inc.、3222 United Super Markets Holdings, Inc.、1803 Shimizu Corporation、4023 クレハ、7733 Olympus Corp.、7004 Kanadevia Corporation、2874 YOKOREI CO. LTD.、8987 Japan Excellent, Inc.、8282 K'S HOLDINGS CORPORATION、8088 IWATANI Corporation、9412 SKY Perfect JSAT Corporation、8125 Wakita & Co., Ltd.、9861 吉野家ホールディングス、4666 Park24 Co., Ltd.、7721 Tokyo Keiki Inc.、8278 Fuji Co., Ltd.、8954 ORIX JREIT Inc.、7458 Daiichikosho Co., Ltd.、2702 日本マクドナルドホールディングス、2782 Seria Co., Ltd.、2809 Kewpie Corporation、3282 Comforia Residential REIT, Inc.、8952 Japan Real Estate Investment Corp.、1861 Kumagai Gumi Co., Ltd.、1417 MIRAIT ONE Corporation、3148 Create SD Holdings Co., Ltd.、8198 Maxvalu Tokai Co., Ltd.、7003 Mitsui ES Holdings Co., Ltd.、8584 Jaccs Co., Ltd.、9882 Yellow Hat Ltd.、1860 Toda Corporation、1944 Kinden Corporation、8066 Mitani Corporation、2659 SAN-A CO., LTD.、7984 Kokuyo Co., Ltd.、3289 Tokyu Fudosan Holdings Corp.、8818 Keihanshin Building Co., Ltd.、1719 HAZAMA ANDO Corporation、1833 Okumura Corporation、9503 Kansai Electric Power Company, Incorporated、6366 Chiyoda Corp.、2379 dip Corporation、6753 Sharp Corporation、8276 HEIWADO CO., LTD.、9974 BELC Co., Ltd.、3234 Mori Hills Reit Investment Corporation、3249 Industrial & Infrastructure Fund Investment Corporation、3296 NIPPON REIT Investment Corp、3309 Sekisui House Reit. Inc.、5482 Aichi Steel Corporation、8955 Japan Prime Realty Investment Corporation、8961 MORI TRUST REIT.Inc、8986 Daiwa Securities Living Investment Corporation、1946 Toenec Corporation、2815 ARIAKE JAPAN Co., Ltd.、4928 Noevir Holdings Co., Ltd.、6960 Fukuda Denshi Co., Ltd.、6804 Hosiden Corp.、8585 Orient Corporation、9699 NISHIO HOLDINGS CO. LTD.、8253 Credit Saison Co., Ltd.、7201 Nissan Motor Co., Ltd.、3471 Mitsui Fudosan Logistics Park, Inc.、8174 NIPPON GAS Co., Ltd.、3591 WACOAL HOLDINGS CORP、7624 NaITO、5018 ＭＯＲＥＳＣＯ、6668 ＡＤプラズマ、5246 ELEMENTS,Inc.、3994 マネーフォワード、4443 Ｓａｎｓａｎ、6814 古野電、5932 三協立山、3479 ティーケーピー、6505 東洋電機製造、3131 シンデンハイテックス、2760 東京エレクトロンデバイス、6521 オキサイド、9960 トーテック、4062 IBIDEN CO., LTD.、6981 村田製作所、7433 伯東、6779 Nihon Dempa Kogyo Co., Ltd.、6754 アンリツ、4658 日本空調サービス、8098 稲畑産業、5208 Arisawa Mfg.Co., Ltd.、5302 日本カーボン、2334 Eole, Inc.、4431 スマレジ、4493 Cyber Security Cloud, Inc.
### グランビル
- PASS（31）: 3798 ULS Group Incorporated、5254 Arent, Inc.、1945 Tokyo Energy & Systems Inc.、8793 ＮＥＣキャピタルソリューション、9064 ヤマトホールディングス、6988 日東電工、186A Astroscale Holdings Inc.、6328 Ebara Jitsugyo Co., Ltd.、2413 エムスリー、6613 QD Laser, Inc.、8336 Musashino Bank, Ltd.、7609 Daitron Co., Ltd.、8919 カチタス、456A Human Made Inc.、7504 Kohsoku Corporation、6072 Jibannet Holdings Co., Ltd.、9616 共立メンテナンス、8361 Ogaki Kyoritsu Bank, Ltd.、9166 GENDA Inc.、8343 Akita Bank, Ltd.、8367 Nanto Bank Ltd.、8362 Fukui Bank, Ltd.、3691 DIGITAL PLUS, Inc.、8524 North Pacific Bank, Ltd.、4997 日本農薬、4346 NEXYZ.Group Corporation、3653 Morpho, Inc.、8360 Yamanashi Chuo Bank, Ltd.、8366 Shiga Bank, Ltd.、8368 Hyakugo Bank, Ltd.、8713 Fidea Holdings Co.Ltd.
- PASS_DOJI（5）: 6905 Cosel Co., Ltd.、5985 SUNCALL CORPORATION、8622 Mito Securities Co., Ltd.、6963 ROHM Company Limited、3778 SAKURA Internet Inc.
- FAIL_UWAHIGE（44）: 3103 ユニチカ、8944 Land Business Co., Ltd.、2986 LA Holdings Co.,Ltd、6562 Geniee, Inc.、8697 Japan Exchange Group, Inc.、6255 NPC Incorporated、8095 Astena Holdings Co.,Ltd.、7744 Noritsu Koki Co., Ltd.、3741 Systems Engineering Consultants Co., Ltd.、4507 Shionogi & Co., Ltd.、5838 Rakuten Bank, Ltd.、3064 MonotaRO Co., Ltd.、3562 No.1 Co., Ltd.、7970 Shin-Etsu Polymer Co., Ltd.、8060 キヤノンマーケティングジャパン、4166 Cacco, Inc.、1815 鉄建建設、4552 JCR Pharmaceuticals Co., Ltd.、6768 Tamura Corporation、4937 Ｇ−ＷＡＱＯＯ、3083 Star seeds Co.,Ltd.、290A ＳＹＮＳＰＥＣＴＩＶＥ、8008 Yondoshi Holdings, Inc.、4180 ＡＰＰＩＥＲ　ＧＲＯＵＰ、8346 Toho Bank, Ltd.、4667 Aisan Technology Co., Ltd.、6023 ダイハツインフィニアース、4413 baudroie,inc.、8714 Senshu Ikeda Holdings,Inc.、7350 Okinawa Financial Group, Inc.、4475 HENNGE K.K.、6998 Nippon Tungsten Co., Ltd.、3107 ダイワボウホールディングス、4044 Central Glass Co., Ltd.、9509 Hokkaido Electric Power Company,Incorporated、9505 Hokuriku Electric Power Company、336A ダイナミックマッププラットフォーム、8628 松井証券、1407 West Holdings Corporation、4440 WITZ Corp.、6522 アスタリスク、477A Startline CO.,LTD.、7380 Juroku Financial Group,Inc.、8334 Gunma Bank, Ltd.
- FAIL_INSEN（98）: 3374 Naigai Tec Corporation、6752 パナソニックHD、7725 INTER ACTION Corporation、9553 MicroAd, Inc.、9006 京浜急行電鉄、6473 JTEKT Corporation、3496 AZOOM CO.,LTD、4544 H.U.Group Holdings, Inc.、6302 Sumitomo Heavy Industries, Ltd.、4763 クリーク・アンド・リバー社、6470 Taiho Kogyo Co., Ltd.、7199 Premium Group Co., Ltd.、3935 Edia Co. Ltd.、6196 Strike Group Co. Ltd.、8061 Seika Corporation、9048 名古屋鉄道、2331 ALSOK CO., LTD.、3661 m-up holdings, Inc.、6432 Takeuchi Mfg.Co., Ltd.、8020 Kanematsu Corporation、9828 Genki Global Dining Concepts Corp、6454 Max Co., Ltd.、2288 Marudai Food Co., Ltd.、5036 Japan Business Systems, Inc.、8014 Chori Co., Ltd.、6371 Tsubakimoto Chain Co.、6592 Mabuchi Motor Co., Ltd.、8850 スターツコーポレーション、3433 TOCALO Co., Ltd.、8927 Meiho Enterprise Co., Ltd.、4183 Mitsui Chemicals, Inc.、4272 Nippon Kayaku Co., Ltd.、4956 Konishi Co., Ltd.、5461 Chubu Steel Plate Co., Ltd.、7181 JAPAN POST INSURANCE Co., Ltd.、7734 Riken Keiki Co., Ltd.、7513 Kojima Co., Ltd.、2002 日清製粉グループ本社、6208 Ishikawa Seisakusho,Ltd.、4617 Chugoku Marine Paints,Ltd.、7751 キヤノン、8081 Kanaden Corporation、5071 VIS Co., Ltd.、6770 Alps Alpine Co., Ltd.、4375 Safie Inc.、8424 芙蓉総合リース、2871 ニチレイ、4534 Mochida Pharmaceutical Co., Ltd.、4549 Eiken Chemical Co., Ltd.、5243 note inc.、7806 MTG Co., Ltd.、6834 Seikoh Giken Co., Ltd.、7856 HAGIHARA INDUSTRIES INC.、1879 新日本建設、6736 Suncorporation、6523 PHC Holdings Corp.、2767 円谷フィールズホールディングス、6227 AIMECHATEC Ltd.、2602 日清オイリオグループ、7616 Colowide Co., Ltd.、6058 VECTOR Inc.、4373 Simplex Holdings,Inc.、3097 Monogatari Corporation、1518 三井松島ホールディングス、6379 RAIZNEXT Corporation、9044 NANKAI Co., Ltd.、4208 UBE Corporation、7630 Ichibanya Co., Ltd.、8043 Starzen Company Limited、9900 Sagami Holdings Corp.、3048 ビックカメラ、8255 Axial Retailing, Inc.、8097 SAN-AI OBBLI CO. LTD、8059 Daiichi Jitsugyo Co., Ltd.、6027 Bengo4.com, Inc.、8410 Seven Bank, Ltd.、8624 Ichiyoshi Securities Co., Ltd.、8708 アイザワ証券グループ、6769 Thine Electronics, Inc.、2122 インタースペース、8995 Makoto Construction Co,Ltd、5242 EYEZ INC.、2354 YE DIGITAL CORPORATION、6597 HPC SYSTEMS Inc.、3687 Fixstars Corp.、5574 ABEJA,Inc.、7354 Direct Marketing MiX Inc.、2681 2nd RETAILING Co., Ltd.、4082 第一稀元素化学工業、3907 Silicon Studio Corp.、8163 SRS HOLDINGS CO.,LTD.、4691 Washington Hotel Corp.、6203 Howa Machinery, Ltd.、6645 OMRON Corporation、6890 Ferrotec Corporation、7175 Imamura Securities Co.Ltd.、9278 BOOKOFF GROUP HOLDINGS LIMITED、4418 Japan Data Science Consortium Co Ltd.
### 変化点
- PASS（6）: 4011 Headwaters Co.,Ltd、7695 交換できるくん、4382 HEROZ, Inc.、9888 UEX LTD、478A Hutzper Inc.、4498 Cybertrust Japan Co., Ltd.
- PASS_DOJI（3）: 218A Liberaware、593A ティアフォー、339A PROGRESS TECHNOLOGIES GROUP INC
- FAIL_UWAHIGE（13）: 6080 Ｍ＆Ａキャピタルパートナーズ、584A LiNKX, Inc.、6136 OSG CORP、9962 ミスミグループ本社、7318 セレンディップ・ホールディングス、4368 4368、5582 （名称取得不可）、8704 トレイダーズホールディングス、6785 鈴木、4165 PLAID Inc.、598A チャットプラス、4478 freee K.K.、3993 PKSHA Technology, Inc.
- FAIL_INSEN（10）: 5803 フジクラ、6254 野村マイクロ・サイエンス、4187 大阪有機化学工業、6857 アドバンテスト、8151 東陽テクニカ、3091 ブロンコビリー、6284 日精エー・エス・ビー機械、4071 Plus Alpha Consulting Co. LTD.、4488 AI inside Inc.、4259 ExaWizards Inc.
- 除籍リスト（SBIグループ登録解除候補）: なし

## 機械詳細
- 検知内訳: 評価399（プール399＋前夜提案のみ0）・本夜指名102（新規14）・除籍0・SKIP0・未マージPR由来0件（24時間以内の他ブランチ無し）
- log追記: base_day=2026-10-21 を置換/追記（最新30営業日保持）。recalc_queue 追加1件
- 抜粋規則: 通知の通過10件の群別内訳は通知に記載。PASS群別 method32/ai2/granville35/changepoint10/不明0
- gate_history: gate_history/2026-10-21.json を新規作成（verdicts399件・nominations102件）
- grades.json: 891銘柄/451KiB（nx 付与715件）
- method_score: 保持67件／null332件
- ヘッドライン付与: 79/79件（PASS全件）
- kabutan新規取得: 銘柄トップ4/50件（優先①②4件＋業種埋め戻し0件）／決算ページ82件（PASS＋保有）／優待ページ30件は403で取得不可
- profile_cache: 総数866・本夜 業態追加4件・業種 付与済み865／未付与1（本夜追加4件）・業態「未取得」のまま出た件数2
- earnings_log: 総数71／本夜追記1件／リターンを埋めた11件／日足が取れず埋められなかった20件
- gyoseki_cache: 再計算4件（history退避0件）・判定保留/取得不可につき据置0件・next_earnings 更新22件
- pool_bars.json: 401銘柄/343KiB
- 鮮度ゲート: 鮮度切れ除外13件・nom_age分布 0-2:156/3-10:185/11+:58・last_seen欠損0件
- 記録の凍結: verdicts399件（評価399件と一致）／nominations102件（新規14・再指名88）
- トレンド文脈: ctx 合致96／不一致163／レンジ136／判定不能4・PASSのうち合致20件・形態が付いた銘柄195件
- 3日ルール判定（件数のみ）: 判定4銘柄・streak≥3 1・streak=2 1・判定不可0。銘柄別の R/streak は通知にのみ
- 業種別PER中央値: 算出できた業種25／母数不足9・spm を写せた銘柄369件
- 開示の分類別件数: 📢0/📉0/📊1/🔁0/👥0/🏛0/📦0/📌4
- 熟成由来の候補: 0件（うちPASS0）
- 権利情報: rights_cache 総数338・本夜 配当更新30件／優待取得0件（優待ページが403で取得不可）・不明のまま338件
- 次回決算日: 付与724件／未発表179件・前年同期発表日 付与166件・earnings_calendar.json 903銘柄/92KiB
- STEP 4.8 週末ブリーフ: week_open=false のためスキップ
- master.json の変更行数: +7940/-6472（indent=2）
