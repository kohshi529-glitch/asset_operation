# 夜間ゲート 2026-10-20

## サマリー
- 評価数: 389 / PASS: 34（PASS_DOJI含め34）
- 発注可能提案数: 22件
- 市場一言: 市場モード「レンジ様子見」（market.latest 2026-10-20）。プール385銘柄中PASS比率8.7%（陰線FAIL 326件・上髭FAIL 29件）
- 実行モード: 通常（base_day=当日の引け値を対象）
- base_day: 2026-10-20（run_at 2026-10-20 20:51起動）
- week_open: false（翌営業日10/21(水)は週初でない）→ STEP 4.8 週末ブリーフはスキップ
- 📆 翌営業日 10/21(水): カレンダーイベントなし。T+2 10/22(木): カレンダーイベントなし。次の TOPIX 低減日 10/30(金) 第1回/8（あと8営業日）
- 📑指数: 低減対象 提案0件／PASS2件／プール61件・新規採用 14件（index_flags 2026-10-07 公表分）

## 検証結果
- V1 → はい（proposals22=results22=template22・board22）
- V2 → はい（PASS34=提案22+除外12・order_status欠落0）
- V3 → はい（results389件重複0）
- V4 → はい（既存static変更0件）
- V5 → はい（許可キー外の変更0件[]）
- V6 → はい（不整合0件）
- V10 → はい（base_day 4箇所=2026-10-20）
- V12 → はい（proposals/template/results 同順）
- V14 → はい（保持59件/null330件・出所不明/不一致0件）
- V15 → はい（PASS34件中34件付与・欠落0・語句違反0（業績データ取得不可由来1件は値の事実））
- V16 → はい（決算発表3件・earnings_log総数70・追記3・再計算なし(b)該当0・history超過0）
- V18 → はい（提案22件・鮮度切れ除外7件・誤除外0）
- V19 → はい（verdicts389=評価389・nominations98=pool last_seen・ctx {'不一致': 165, 'レンジ': 138, '合致': 85, '判定不能': 1}・写し漏れ0・既存gyotai変更0）
- V11 → いいえ（+7096/-7837（myers）／patience +7229/-7970（indent=2・往復一致で検出・results全置換389件とcache更新による。全体再フォーマットではない）（目安5,000行超過: 前夜も同規模））
- V9 → はい（gate_history/2026-10-20.json 新規作成・残り全キー一致）
- V13 → はい（887銘柄/445KB・和集合887・15キー欠落0・nx不一致0・ix 185/185・業種中央値25業種）
- V17 → はい（391銘柄/330KB・保有4銘柄すべて収録・3日ルール判定4銘柄）
- V20 → はい（895銘柄/86KB・nx非null725・hist持ち219・pxd115・）
- V7 → はい（必須セクションすべて存在）
- V8 → はい（模擬22行の書式OK）
- LEAK → はい（公開物の保有情報漏えい0（board0/gate_history0/today0））

## 保有アラート
保有4銘柄・アラート10件（詳細は通知）

## 前夜の結果
PL5口座への正式な反映は週次①-11の採点で行われる。ここは参考情報。
前夜2026-10-19の提案113件 → 約定86・不約定27・判定不能0
- 212A momentum 指定2854 → 約定2872・終値2877（+0.17%）
- 7678 momentum 指定3820 → 約定3820・終値3755（-1.70%）
- 3374 momentum 指定5090 → 約定5090・終値4785（-5.99%）
- 2820 momentum 指定6810 → 約定6810・終値6690（-1.76%）
- 6324 reversal 指定5300 → 約定5290・終値5260（-0.57%）
- 3222 reversal 指定743 → 約定743・終値759（+2.15%）
- 1803 reversal 指定2023.5 → 約定2015・終値1996.5（-0.92%）
- 7733 reversal 指定1685 → 約定1675・終値1730（+3.28%）
- 7004 reversal 指定1094 → 約定1080・終値1066（-1.30%）
- 8522 reversal 指定6300 → 約定6300・終値5980（-5.08%）
- 8088 reversal 指定1938.5 → 約定1932・終値1892.5（-2.04%）
- 8386 reversal 指定2853 → 約定2831・終値2685（-5.16%）
- 7721 reversal 指定6350 → 約定6270・終値5950（-5.10%）
- 8393 reversal 指定2502 → 約定2477・終値2339（-5.57%）
- 1861 reversal 指定1219 → 約定1211・終値1203（-0.66%）
- 1952 reversal 指定3005 → 約定3000・終値2938（-2.07%）
- 6269 reversal 指定8263 → 約定8258・終値8010（-3.00%）
- 7003 reversal 指定3832 → 約定3832・終値3667（-4.31%）
- 1860 reversal 指定1401 → 約定1392.5・終値1405（+0.90%）
- 1944 reversal 指定6474 → 約定6436・終値6360（-1.18%）
- 8066 reversal 指定3140 → 約定3130・終値3055（-2.40%）
- 2805 reversal 指定6330 → 約定6330・終値6000（-5.21%）
- 5021 reversal 指定4220 → 約定4220・終値4223（+0.07%）
- 8818 reversal 指定944 → 約定939・終値916（-2.45%）
- 1719 reversal 指定1750 → 約定1750・終値1751.5（+0.09%）
- 5844 reversal 指定4254 → 約定4232・終値4106（-2.98%）
- 1893 reversal 指定1353.5 → 約定1342・終値1336.5（-0.41%）
- 5482 reversal 指定2936 → 約定2911・終値2867（-1.51%）
- 1946 reversal 指定2068 → 約定2060・終値2019（-1.99%）
- 1662 reversal 指定1710 → 約定1710・終値1703（-0.41%）
- 6804 reversal 指定2380 → 約定2380・終値2341（-1.64%）
- 5831 reversal 指定3176 → 約定3120・終値3033（-2.79%）
- 8345 reversal 指定2260 → 約定2240・終値2117（-5.49%）
- 8399 reversal 指定2925 → 約定2892・終値2777（-3.98%）
- 7381 reversal 指定1215 → 約定1202・終値1142（-4.99%）
- 7384 reversal 指定4510 → 約定4510・終値4105（-8.98%）
- 8174 reversal 指定933.8 → 約定933.3・終値937.5（+0.45%）
- 8304 reversal 指定3185 → 約定3153・終値3042（-3.52%）
- 8511 reversal 指定2217 → 約定2217・終値2151（-2.98%）
- 3131 momentum 指定7450 → 約定7510・終値6760（-9.99%）
- 6521 momentum 指定3395 → 約定3395・終値3200（-5.74%）
- 6981 reversal 指定6798 → 約定6750・終値6643（-1.59%）
- 6752 reversal 指定3977 → 約定3977・終値3878（-2.49%）
- 6779 reversal 指定2890 → 約定2880・終値2726（-5.35%）
- 6754 reversal 指定3030 → 約定3030・終値2913.5（-3.84%）
- 4658 reversal 指定1570 → 約定1570・終値1545（-1.59%）
- 6643 reversal 指定5380 → 約定5350・終値5100（-4.67%）
- 3103 reversal 指定1331 → 約定1317・終値1280（-2.81%）
- 5302 reversal 指定5090 → 約定5070・終値4975（-1.87%）
- 6473 momentum 指定2145 → 約定2145・終値2102（-2.00%）
- 6255 momentum 指定686 → 約定686・終値667（-2.77%）
- 6395 momentum 指定1325 → 約定1325・終値1295（-2.26%）
- 6470 momentum 指定1163 → 約定1163・終値1141（-1.89%）
- 7199 momentum 指定2226 → 約定2227・終値2197（-1.35%）
- 6432 momentum 指定7800 → 約定7800・終値7680（-1.54%）
- 6371 momentum 指定2682 → 約定2682・終値2636（-1.72%）
- 3433 momentum 指定2913 → 約定2913・終値2800（-3.88%）
- 7856 oshime 指定2044 → 約定2044・終値2038（-0.29%）
- 6736 oshime 指定9732 → 約定9732・終値9740（+0.08%）
- 5208 oshime 指定2766 → 約定2766・終値2674（-3.33%）
- 6379 oshime 指定1000 → 約定1000・終値1008（+0.80%）
- 6963 reversal 指定4060 → 約定4060・終値3903（-3.87%）
- 5242 reversal 指定2704 → 約定2704・終値2866（+5.99%）
- 4691 reversal 指定1913 → 約定1903・終値1838（-3.42%）
- 6203 reversal 指定2083 → 約定2073・終値2000（-3.52%）
- 6522 reversal 指定923 → 約定909・終値867（-4.62%）
- 3778 reversal 指定3250 → 約定3250・終値3100（-4.62%）
- 8368 reversal 指定2271 → 約定2248・終値2115（-5.92%）
- 5803 changepoint 指定4482 → 約定4383・終値4192（-4.36%）
- 6254 changepoint 指定3160 → 約定3130・終値3015（-3.67%）
- 4187 changepoint 指定4920 → 約定4920・終値4590（-6.71%）
- 4419 changepoint 指定1550 → 約定1549・終値1489（-3.87%）
- 584A changepoint 指定2308 → 約定2269・終値2127（-6.26%）
- 6136 changepoint 指定3860 → 約定3829・終値3653（-4.60%）
- 6857 changepoint 指定34450 → 約定34450・終値33870（-1.68%）
- 7318 changepoint 指定1245 → 約定1233・終値1159（-6.00%）
- 4368 changepoint 指定3165 → 約定3155・終値3000（-4.91%）
- 3091 changepoint 指定2956 → 約定2956・終値2981（+0.85%）
- 8704 changepoint 指定1315 → 約定1306・終値1275（-2.37%）
- 6284 changepoint 指定8540 → 約定8520・終値8280（-2.82%）
- 6597 changepoint 指定3560 → 約定3530・終値3145（-10.91%）
- 6785 changepoint 指定3400 → 約定3370・終値3270（-2.97%）
- 4071 changepoint 指定2262 → 約定2262・終値2262（+0.00%）
- 598A changepoint 指定1232 → 約定1221・終値1186（-2.87%）
- 3993 changepoint 指定3640 → 約定3640・終値3550（-2.47%）
- 4259 changepoint 指定809 → 約定809・終値776（-4.08%）

## 模擬テンプレ
```
# base_day 2026-10-20 ／ 提案22件
# 使い方: 参戦する0〜3銘柄の行だけをコピーし、｜の後ろに参戦理由を書いてポジション株PJへ送る。
# 選ばなかった行は送らなくてよい（全行に理由を書く必要はない）。見送りは末尾の1行で足りる。
# 特定銘柄を理由つきで見送る場合のみ『模擬 見送り {code} ｜{理由}』を送る。
模擬 3391 choruko_reversal 指値2258.5 SL2068.5 単元100 ｜
模擬 3222 choruko_reversal 指値759 SL724 単元100 ｜
模擬 7733 choruko_reversal 指値1730 SL1668.5 単元100 ｜
模擬 8278 choruko_reversal 指値1959 SL1895 単元100 ｜
模擬 2809 choruko_reversal 指値4571 SL4262 単元100 ｜
模擬 3148 choruko_reversal 指値3215 SL3115 単元100 ｜
模擬 1860 choruko_reversal 指値1405 SL1338 単元100 ｜
模擬 7984 choruko_reversal 指値890.3 SL863.4 単元100 ｜
模擬 9503 choruko_reversal 指値2723 SL2653.5 単元100 ｜
模擬 6753 choruko_reversal 指値590.6 SL565 単元100 ｜
模擬 8276 choruko_reversal 指値2556 SL2464 単元100 ｜
模擬 9948 choruko_reversal 指値3440 SL3290 単元100 ｜
模擬 9974 choruko_reversal 指値6230 SL5980 単元100 ｜
模擬 2815 choruko_reversal 指値5270 SL5170 単元100 ｜
模擬 8194 choruko_reversal 指値2381 SL2290 単元100 ｜
模擬 8174 choruko_reversal 指値937.5 SL888.7 単元100 ｜
模擬 3591 choruko_reversal 指値3578 SL3514 単元100 ｜
模擬 9432 ai_reversal 指値177.1 SL171.2 単元100 ｜
模擬 4544 granville_tenkan 逆指値3720 SL3492.1 単元100 ｜
模擬 7616 granville_oshime 指値2047 SL2037.2 単元100 ｜
模擬 3097 granville_oshime 指値5520 SL5492.4 単元100 ｜
模擬 5242 granville_rebound 指値2866 SL1800 単元100 ｜
模擬 見送り ｜
```

## PASS内訳
PASS 34件 = 発注可能 22件 + 除外 12件（型不一致1/材料後出し1/鮮度切れ7/その他3）
- 2930 北の達人コーポレーション｜⛔提案なし(材料後出し)
- 9861 吉野家ホールディングス｜⛔提案なし(指名鮮度切れ 12営業日)
- 3994 マネーフォワード｜⛔提案なし(手法ブランチ不明)
- 4443 Ｓａｎｓａｎ｜⛔提案なし(手法ブランチ不明)
- 6532 ベイカレント｜⛔提案なし(手法ブランチ不明)
- 4507 Shionogi & Co., Ltd.｜⛔提案なし(指名鮮度切れ 12営業日)
- 2331 ALSOK CO., LTD.｜⛔提案なし(指名鮮度切れ 15営業日)
- 9828 Genki Global Dining Concepts Corp｜⛔提案なし(指名鮮度切れ 15営業日)
- 2002 日清製粉グループ本社｜⛔提案なし(指名鮮度切れ 17営業日)
- 7630 Ichibanya Co., Ltd.｜⛔型不一致: 既に支持帯以下
- 9900 Sagami Holdings Corp.｜⛔提案なし(指名鮮度切れ 12営業日)
- 8163 SRS HOLDINGS CO.,LTD.｜⛔提案なし(指名鮮度切れ 12営業日)

## 5手法銘柄
- 6627 Tera Probe, Inc.｜kenmo_momentum｜🚀確変(13)｜💎割安｜FAIL_INSEN｜1,938円｜💰21.1万円｜—
- 5137 Smart Drive Co. Ltd.｜kenmo_momentum｜🚀確変(12)｜🟢値頃｜FAIL_INSEN｜300円｜💰3.3万円｜—
- 6862 Minato Holdings Inc.｜kenmo_momentum｜🚀確変(11)｜🟢値頃｜FAIL_INSEN｜4,250円｜💰47.0万円｜—
- 4053 Sun Asterisk, Inc.｜kenmo_momentum｜🚀確変(11)｜⚪妥当｜FAIL_INSEN｜577円｜💰5.8万円｜—
- 4434 Serverworks Co., Ltd.｜kenmo_momentum｜🚀確変(11)｜⚪妥当｜FAIL_INSEN｜3,020円｜💰30.4万円｜—
- 5027 AnyMind Group Inc.｜kenmo_momentum｜🚀確変(11)｜⚪妥当｜FAIL_INSEN｜766円｜💰8.1万円｜—
- 5136 tripla Co.,Ltd.｜kenmo_momentum｜🚀確変(11)｜⚪妥当｜FAIL_INSEN｜2,622円｜💰27.4万円｜—
- 5757 CK San-Etsu Co., Ltd.｜kenmo_momentum｜🔥絶好調(10)｜💎割安｜FAIL_INSEN｜4,645円｜💰50.0万円｜—
- 212A FIT EASY Inc.｜kenmo_momentum｜🔥絶好調(10)｜⚪妥当｜FAIL_UWAHIGE｜2,877円｜💰28.5万円｜—
- 9554 AViC Co. Ltd.｜kenmo_momentum｜🔥絶好調(10)｜⚪妥当｜FAIL_INSEN｜1,620円｜💰17.2万円｜—
- 421A Movin' Strategic Career CO.,LTD.｜kenmo_momentum｜🔥絶好調(10)｜⚪妥当｜FAIL_INSEN｜4,280円｜💰43.1万円｜—
- 5132 pluszero,Inc.｜kenmo_momentum｜🔥絶好調(9)｜🟢値頃｜FAIL_INSEN｜1,901円｜💰19.6万円｜—
- 6298 Y.A.C.HOLDINGS CO.,LTD.｜kenmo_momentum｜🔥絶好調(9)｜🟢値頃｜FAIL_INSEN｜1,132円｜💰11.6万円｜—
- 4377 ONE CAREER Inc.｜kenmo_momentum｜🔥絶好調(9)｜⚪妥当｜FAIL_INSEN｜2,600円｜💰26.7万円｜—
- 5537 AlbaLink Co.,Ltd.｜kenmo_momentum｜🔥絶好調(9)｜⚪妥当｜FAIL_INSEN｜3,775円｜💰39.3万円｜—
- 9556 INTLOOP, Inc.｜kenmo_momentum｜🔥絶好調(8)｜💎割安｜FAIL_INSEN｜2,200円｜💰22.6万円｜—
- 7047 PORT INC.｜kenmo_momentum｜🔥絶好調(8)｜💎割安｜FAIL_INSEN｜2,093円｜💰21.7万円｜—
- 3915 TerraSky Co., Ltd.｜kenmo_momentum｜🔥絶好調(8)｜🟢値頃｜FAIL_INSEN｜2,390円｜💰22.2万円｜—
- 5821 Hirakawa Hewtech Corp.｜kenmo_momentum｜⚡好調(7)｜💎割安｜FAIL_INSEN｜2,995円｜💰30.9万円｜—
- 4058 Toyokumo, Inc.｜kenmo_momentum｜⚡好調(7)｜⚪妥当｜FAIL_INSEN｜2,285円｜💰23.1万円｜—
- 6071 IBJ, Inc.｜kenmo_momentum｜⚡好調(7)｜⚪妥当｜FAIL_INSEN｜914円｜💰9.3万円｜—
- 5034 unerry, Inc.｜kenmo_momentum｜⚡好調(7)｜⚪妥当｜FAIL_INSEN｜2,729円｜💰27.7万円｜—
- 9560 PROGRIT, Inc.｜kenmo_momentum｜⚡好調(7)｜⚪妥当｜FAIL_INSEN｜1,094円｜💰11.2万円｜—
- 558A SQUEEZE Inc.｜kenmo_momentum｜⚡好調(7)｜🟡やや割高｜FAIL_INSEN｜5,600円｜💰58.2万円｜—
- 7678 ASAKUMA CO.,LTD.｜kenmo_momentum｜⚡好調(7)｜🔴過熱｜FAIL_INSEN｜3,755円｜💰37.9万円｜—
- 9268 OPTIMUS GROUP Co., Ltd.｜kenmo_momentum｜⚡好調(6)｜💎割安｜FAIL_INSEN｜335円｜💰3.5万円｜—
- 4477 BASE, Inc.｜kenmo_momentum｜⚡好調(6)｜⚪妥当｜FAIL_INSEN｜370円｜💰3.8万円｜—
- 9628 San Holdings,Inc.｜kenmo_momentum｜⚡好調(6)｜🟡やや割高｜FAIL_INSEN｜1,280円｜💰13.3万円｜—
- 2980 SRE Holdings Corp.｜kenmo_momentum｜⚡好調(5)｜🟢値頃｜FAIL_INSEN｜2,287円｜💰23.9万円｜—
- 4412 Science Arts, Inc.｜kenmo_momentum｜⚡好調(5)｜⚪妥当｜FAIL_INSEN｜1,407円｜💰14.4万円｜—
- 505A Geekly,Inc.｜kenmo_momentum｜✅順調(4)｜💎割安｜FAIL_INSEN｜1,144円｜💰11.7万円｜—
- 3798 ULS Group Incorporated｜kenmo_momentum｜✅順調(4)｜💎割安｜FAIL_INSEN｜530円｜💰5.6万円｜—
- 5038 eWeLL Co.,Ltd｜kenmo_momentum｜✅順調(4)｜⚪妥当｜FAIL_INSEN｜2,279円｜💰23.2万円｜—
- 6629 TECHNO HORIZON Co., Ltd.｜kenmo_momentum｜✅順調(4)｜⚪妥当｜FAIL_INSEN｜935円｜💰9.8万円｜—
- 6289 Giken Ltd.｜kenmo_momentum｜⚠減速(1)｜🔴過熱｜FAIL_INSEN｜1,982円｜💰20.4万円｜—
- 3077 Horiifoodservice Co., Ltd.｜kenmo_momentum｜判定保留(変則決算)｜—｜FAIL_INSEN｜1,137円｜💰—｜—
- 6918 Aval Data Corporation｜kenmo_newhigh｜🚀確変(13)｜⚪妥当｜FAIL_INSEN｜3,705円｜💰39.5万円｜—
- 3374 Naigai Tec Corporation｜kenmo_newhigh｜🚀確変(12)｜⚪妥当｜FAIL_INSEN｜4,785円｜💰50.5万円｜—
- 7567 Sakae Electronics Corp.｜kenmo_newhigh｜🚀確変(12)｜⚪妥当｜FAIL_INSEN｜623円｜💰6.3万円｜—
- 269A SAPEET｜kenmo_newhigh｜🚀確変(11)｜⚪妥当｜FAIL_INSEN｜2,782円｜💰28.7万円｜—
- 6337 Tesec Corporation｜kenmo_newhigh｜🚀確変(11)｜⚪妥当｜FAIL_INSEN｜3,215円｜💰34.4万円｜—
- 3696 セレス｜kenmo_newhigh｜🔥絶好調(8)｜🟢値頃｜FAIL_INSEN｜2,299円｜💰23.8万円｜—
- 2930 北の達人コーポレーション｜kenmo_newhigh｜⚡好調(6)｜🔴過熱｜PASS｜147円｜💰1.5万円｜⛔提案なし(材料後出し)｜⚠日程不明 📑TOPIX低減対象（次 10/30 第1回/8） ⚡材料後出し
  > 【業態】健康美容食品や化粧品を企画・通販。「カイテキオリゴ」や目元クリームが主力商品。
  > 【いま】終値147円・直近5日+8.89%・📌機関投資家・アナリスト向け決算説明会を開催いたしました
  > 【調子】⚡好調（6/13）— 質注意
  > 【水準】🔴過熱（0.0/7）— PER27.74倍・PEG6.689・52週87.5% ／ 💰単元1.5万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 2820 Yamami Co.｜kenmo_newhigh｜✅順調(4)｜🟡やや割高｜FAIL_INSEN｜6,690円｜💰67.8万円｜—
- 4331 Take and Give. Needs Co., Ltd.｜kenmo_newhigh｜✅順調(3)｜🔴過熱｜FAIL_INSEN｜810円｜💰8.3万円｜—
- 7161 Jimoto Holdings, Inc.｜kenmo_newhigh｜業績データ取得不可｜⚪妥当｜FAIL_INSEN｜570円｜💰6.1万円｜—
- 2340 Gokurakuyu Holdings Co., Ltd.｜kenmo_newhigh｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜507円｜💰5.1万円｜—
- 3843 Freebit Co., Ltd.｜kenmo_newhigh｜—｜—｜FAIL_INSEN｜1,738円｜💰—｜—
- 8871 GOLDCREST Co., Ltd.｜choruko_reversal｜🔥絶好調(10)｜💎割安｜FAIL_INSEN｜2,870円｜💰29.3万円｜—
- 3391 TSURUHA Holdings, Inc.｜choruko_reversal｜🔥絶好調(10)｜🟢値頃｜PASS｜2,258円｜💰22.6万円｜reversal 2258.5 想定損失幅8.4%。｜⚠日程不明
  > 【業態】ドラッグストア大手。25年12月ウエルシアHDと経営統合。イオンが子会社化へ。
  > 【いま】終値2,258円・直近5日+6.76%（材料未確認）
  > 【調子】🔥絶好調（10/13）
  > 【水準】🟢値頃（5.0/7）— PER24.68倍・PEG0.4447・52週33.5% ／ 💰単元22.6万円
  > 【戦略】当日終値2258.5円の指値で反転を取りにいく。SL2068.5円（直近5日安値）
- 3186 ネクステージ｜choruko_reversal｜🔥絶好調(9)｜💎割安｜FAIL_INSEN｜2,518円｜💰26.4万円｜—
- 6324 Harmonic Drive Systems Inc.｜choruko_reversal｜🔥絶好調(9)｜⚪妥当｜FAIL_INSEN｜5,260円｜💰53.0万円｜—
- 3222 United Super Markets Holdings, Inc.｜choruko_reversal｜🔥絶好調(9)｜🔴過熱｜PASS｜759円｜💰7.6万円｜reversal 759 想定損失幅4.6%。｜⚠日程不明 織り込み済みの可能性（押し目待ち推奨圏）
  > 【業態】イオン系、首都圏の食品スーパー最大手。マルエツ、カスミ、マックスバリュ関東が統合。
  > 【いま】終値759円・直近5日+1.20%（材料未確認）
  > 【調子】🔥絶好調（9/13）
  > 【水準】🔴過熱（2.0/7）— PER1084倍・PEG11.36・52週12.6% ／ 💰単元7.6万円
  > 【戦略】当日終値759円の指値で反転を取りにいく。SL724円（直近5日安値）
- 1803 Shimizu Corporation｜choruko_reversal｜🔥絶好調(8)｜💎割安｜FAIL_INSEN｜1,996円｜💰20.2万円｜—
- 4023 クレハ｜choruko_reversal｜🔥絶好調(8)｜🟢値頃｜FAIL_INSEN｜3,855円｜💰38.5万円｜—
- 7733 Olympus Corp.｜choruko_reversal｜🔥絶好調(8)｜⚪妥当｜PASS｜1,730円｜💰17.3万円｜reversal 1730 想定損失幅3.6%。｜📋カルテ窓 11/10(残14営業日)
  > 【業態】内視鏡世界首位。消化器向け高シェア。治療機器など医療関連に集中。
  > 【いま】終値1,730円・直近5日-14.88%（材料未確認）
  > 【調子】🔥絶好調（8/13）
  > 【水準】⚪妥当（4.0/7）— PER18倍・PEG0.3678・52週47.1% ／ 💰単元17.3万円
  > 【戦略】当日終値1730円の指値で反転を取りにいく。SL1668.5円（直近5日安値）
- 7004 Kanadevia Corporation｜choruko_reversal｜⚠減速(7)｜💎割安｜FAIL_INSEN｜1,066円｜💰10.9万円｜—
- 2874 YOKOREI CO. LTD.｜choruko_reversal｜⚠減速(7)｜🟢値頃｜FAIL_INSEN｜1,726円｜💰17.6万円｜—
- 8522 Bank of Nagoya, Ltd.｜choruko_reversal｜⚡好調(7)｜🟢値頃｜FAIL_INSEN｜5,980円｜💰63.0万円｜—
- 8987 Japan Excellent, Inc.｜choruko_reversal｜⚡好調(6)｜🟢値頃｜FAIL_INSEN｜123,700円｜💰12.5万円｜—
- 8282 K'S HOLDINGS CORPORATION｜choruko_reversal｜⚡好調(6)｜🟢値頃｜FAIL_INSEN｜1,724円｜💰17.4万円｜—
- 8088 IWATANI Corporation｜choruko_reversal｜⚡好調(6)｜⚪妥当｜FAIL_INSEN｜1,892円｜💰19.4万円｜—
- 8386 Hyakujushi Bank, Ltd.｜choruko_reversal｜⚡好調(6)｜⚪妥当｜FAIL_INSEN｜2,685円｜💰28.5万円｜—
- 9412 SKY Perfect JSAT Corporation｜choruko_reversal｜⚡好調(6)｜⚪妥当｜FAIL_INSEN｜1,860円｜💰19.2万円｜—
- 8125 Wakita & Co., Ltd.｜choruko_reversal｜⚡好調(6)｜🔴過熱｜FAIL_INSEN｜1,833円｜💰18.5万円｜—
- 9861 吉野家ホールディングス｜choruko_reversal｜⚡好調(6)｜🔴過熱｜PASS｜4,464円｜💰44.6万円｜⛔提案なし(指名鮮度切れ 12営業日)｜⚠日程不明
  > 【業態】牛丼屋老舗。収益柱「吉野家」と「はなまるうどん」を全国展開。ラーメン店も。
  > 【いま】終値4,464円・直近5日+10.85%（材料未確認）
  > 【調子】⚡好調（6/13）
  > 【水準】🔴過熱（0.0/7）— PER47.95倍・PEG2.643・52週98.9% ／ 💰単元44.6万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 12営業日)）
- 4666 Park24 Co., Ltd.｜choruko_reversal｜⚡好調(5)｜💎割安｜FAIL_UWAHIGE｜1,804円｜💰18.0万円｜—
- 7721 Tokyo Keiki Inc.｜choruko_reversal｜⚡好調(5)｜🟢値頃｜FAIL_INSEN｜5,950円｜💰63.5万円｜—
- 8278 Fuji Co., Ltd.｜choruko_reversal｜⚡好調(5)｜🟢値頃｜PASS｜1,959円｜💰19.6万円｜reversal 1959 想定損失幅3.3%。｜⚠日程不明
  > 【業態】愛媛地盤で四国最大スーパー。中国地方も展開。マックスバリュ西日本と合併。
  > 【いま】終値1,959円・直近5日+1.87%（材料未確認）
  > 【調子】⚡好調（5/13）
  > 【水準】🟢値頃（5.0/7）— PER24.25倍・PEG0.6499・52週19.9% ／ 💰単元19.6万円
  > 【戦略】当日終値1959円の指値で反転を取りにいく。SL1895円（直近5日安値）
- 8381 San-in Godo Bank Ltd.｜choruko_reversal｜⚡好調(5)｜⚪妥当｜FAIL_INSEN｜2,153円｜💰23.0万円｜—
- 8954 ORIX JREIT Inc.｜choruko_reversal｜⚡好調(5)｜⚪妥当｜FAIL_INSEN｜88,600円｜💰8.8万円｜—
- 8393 Miyazaki Bank Ltd.｜choruko_reversal｜⚡好調(5)｜⚪妥当｜FAIL_INSEN｜2,339円｜💰25.0万円｜—
- 7458 Daiichikosho Co., Ltd.｜choruko_reversal｜⚡好調(5)｜⚪妥当｜FAIL_UWAHIGE｜1,766円｜💰17.6万円｜—
- 2702 日本マクドナルドホールディングス｜choruko_reversal｜⚠減速(5)｜🔴過熱｜FAIL_UWAHIGE｜8,200円｜💰79.1万円｜—
- 2782 Seria Co., Ltd.｜choruko_reversal｜⚡好調(5)｜🔴過熱｜FAIL_UWAHIGE｜4,220円｜💰41.6万円｜—
- 2809 Kewpie Corporation｜choruko_reversal｜⚡好調(5)｜🔴過熱｜PASS｜4,571円｜💰45.7万円｜reversal 4571 想定損失幅6.8%。 ⚠1単元でリスク枠超過（30,900円）｜⚠日程不明
  > 【業態】マヨネーズ・ドレッシング最大手。サラダ・惣菜も。医・介護食やファインケミカルにも展開。
  > 【いま】終値4,571円・直近5日+5.81%（材料未確認）
  > 【調子】⚡好調（5/13）
  > 【水準】🔴過熱（1.0/7）— PER24.2倍・PEG3.465・52週65.9% ／ 💰単元45.7万円
  > 【戦略】当日終値4571円の指値で反転を取りにいく。SL4262円（直近5日安値）／⚠1単元リスク30,900円（枠超過）
- 3279 Activia Properties, Inc.｜choruko_reversal｜✅順調(4)｜⚪妥当｜FAIL_INSEN｜122,900円｜💰12.5万円｜—
- 3282 Comforia Residential REIT, Inc.｜choruko_reversal｜✅順調(4)｜🟡やや割高｜FAIL_INSEN｜88,300円｜💰8.9万円｜—
- 8952 Japan Real Estate Investment Corp.｜choruko_reversal｜✅順調(4)｜🟡やや割高｜FAIL_INSEN｜106,300円｜💰10.8万円｜—
- 1861 Kumagai Gumi Co., Ltd.｜choruko_reversal｜✅順調(3)｜💎割安｜FAIL_INSEN｜1,203円｜💰12.2万円｜—
- 1417 MIRAIT ONE Corporation｜choruko_reversal｜✅順調(3)｜🟢値頃｜FAIL_INSEN｜3,319円｜💰33.7万円｜—
- 3148 Create SD Holdings Co., Ltd.｜choruko_reversal｜✅順調(3)｜⚪妥当｜PASS｜3,215円｜💰32.1万円｜reversal 3215 想定損失幅3.1%。｜⚠日程不明
  > 【業態】神奈川から首都圏に大手ドラッグチェーン。大型店展開、食品強化。介護事業も。
  > 【いま】終値3,215円・直近5日+2.55%（材料未確認）
  > 【調子】✅順調（3/13）
  > 【水準】⚪妥当（4.0/7）— PER12.22倍・PEG2.431・52週31.3% ／ 💰単元32.1万円
  > 【戦略】当日終値3215円の指値で反転を取りにいく。SL3115円（直近5日安値）
- 8198 Maxvalu Tokai Co., Ltd.｜choruko_reversal｜✅順調(3)｜⚪妥当｜FAIL_UWAHIGE｜3,145円｜💰31.1万円｜—
- 1820 Nishimatsu Construction Co., Ltd.｜choruko_reversal｜✅順調(3)｜⚪妥当｜FAIL_INSEN｜5,242円｜💰52.0万円｜—
- 1952 Shin Nippon Air Technologies Co., Ltd.｜choruko_reversal｜✅順調(3)｜⚪妥当｜FAIL_INSEN｜2,938円｜💰30.1万円｜—
- 6269 Modec, Inc.｜choruko_reversal｜✅順調(3)｜⚪妥当｜FAIL_INSEN｜8,010円｜💰82.6万円｜—
- 7003 Mitsui ES Holdings Co., Ltd.｜choruko_reversal｜✅順調(3)｜⚪妥当｜FAIL_INSEN｜3,667円｜💰38.3万円｜—
- 8584 Jaccs Co., Ltd.｜choruko_reversal｜🔻悪化(3)｜⚪妥当｜FAIL_INSEN｜3,420円｜💰34.9万円｜—
- 9882 Yellow Hat Ltd.｜choruko_reversal｜✅順調(3)｜⚪妥当｜FAIL_INSEN｜1,618円｜💰16.3万円｜—
- 1860 Toda Corporation｜choruko_reversal｜✅順調(3)｜🟡やや割高｜PASS｜1,405円｜💰14.1万円｜reversal 1405 想定損失幅4.8%。｜📋カルテ窓 11/13(残17営業日)
  > 【業態】名門で業界準大手。堅実経営。病院・学校に強み。洋上風力発電に注力。
  > 【いま】終値1,405円・直近5日+3.42%（材料未確認）
  > 【調子】✅順調（3/13）— 質注意
  > 【水準】🟡やや割高（2.0/7）— PER11.89倍・PEG—・52週59.9% ／ 💰単元14.1万円
  > 【戦略】当日終値1405円の指値で反転を取りにいく。SL1338円（直近5日安値）
- 1944 Kinden Corporation｜choruko_reversal｜✅順調(3)｜🟡やや割高｜FAIL_INSEN｜6,360円｜💰64.7万円｜—
- 8066 Mitani Corporation｜choruko_reversal｜⚠減速(3)｜🟡やや割高｜FAIL_INSEN｜3,055円｜💰31.4万円｜—
- 2659 SAN-A CO., LTD.｜choruko_reversal｜✅順調(3)｜🔴過熱｜FAIL_INSEN｜3,150円｜💰31.4万円｜—
- 2805 S&B Foods Inc.｜choruko_reversal｜✅順調(3)｜🔴過熱｜FAIL_INSEN｜6,000円｜💰63.3万円｜—
- 5021 Cosmo Energy Holdings Co., Ltd.｜choruko_reversal｜🔻悪化(3)｜🔴過熱｜FAIL_UWAHIGE｜4,223円｜💰42.2万円｜—
- 7984 Kokuyo Co., Ltd.｜choruko_reversal｜✅順調(3)｜🔴過熱｜PASS｜890円｜💰8.9万円｜reversal 890.3 想定損失幅3.0%。
  > 【業態】事務用品最大手。紙製品で高シェア。オフィス家具や文具も。通販を拡大。
  > 【いま】終値890円・直近5日+2.31%（材料未確認）
  > 【調子】✅順調（3/13）— 質注意
  > 【水準】🔴過熱（1.0/7）— PER18.1倍・PEG—・52週59.4% ／ 💰単元8.9万円
  > 【戦略】当日終値890.3円の指値で反転を取りにいく。SL863.4円（直近5日安値）
- 3289 Tokyu Fudosan Holdings Corp.｜choruko_reversal｜➖横ばい(2)｜💎割安｜FAIL_INSEN｜1,206円｜💰12.1万円｜—
- 8818 Keihanshin Building Co., Ltd.｜choruko_reversal｜➖横ばい(2)｜⚪妥当｜FAIL_INSEN｜916円｜💰9.4万円｜—
- 1333 Umios Corporation｜choruko_reversal｜➖横ばい(2)｜⚪妥当｜FAIL_UWAHIGE｜1,203円｜💰12.0万円｜—
- 1719 HAZAMA ANDO Corporation｜choruko_reversal｜➖横ばい(2)｜⚪妥当｜FAIL_INSEN｜1,752円｜💰17.5万円｜—
- 1833 Okumura Corporation｜choruko_reversal｜⚠減速(2)｜⚪妥当｜FAIL_INSEN｜5,260円｜💰52.7万円｜—
- 9503 Kansai Electric Power Company, Incorporated｜choruko_reversal｜🔻悪化(2)｜⚪妥当｜PASS｜2,723円｜💰27.2万円｜reversal 2723 想定損失幅2.6%。｜⚠業績基調が下向き（🔻悪化）
  > 【業態】東電と並ぶ業界の雄。原発依存度高いが代替電源確保へ。情報通信も。
  > 【いま】終値2,723円・直近5日+0.09%（材料未確認）
  > 【調子】🔻悪化（2/13）— 質注意
  > 【水準】⚪妥当（3.0/7）— PER9.788倍・PEG—・52週62.0% ／ 💰単元27.2万円
  > 【戦略】当日終値2723円の指値で反転を取りにいく。SL2653.5円（直近5日安値）
- 8953 Japan Metropolitan Fund Investment Corporation｜choruko_reversal｜➖横ばい(2)｜🟡やや割高｜FAIL_INSEN｜102,000円｜💰10.4万円｜—
- 6366 Chiyoda Corp.｜choruko_reversal｜🔻悪化(2)｜🟡やや割高｜FAIL_INSEN｜587円｜💰6.2万円｜—
- 5844 Kyoto Financial Group,Inc.｜choruko_reversal｜🔻悪化(2)｜🔴過熱｜FAIL_INSEN｜4,106円｜💰42.5万円｜—
- 2379 dip Corporation｜choruko_reversal｜⚠減速(1)｜💎割安｜FAIL_INSEN｜1,521円｜💰16.6万円｜—
- 1893 Penta-Ocean Construction Co., Ltd.｜choruko_reversal｜⚠減速(1)｜⚪妥当｜FAIL_INSEN｜1,336円｜💰13.5万円｜—
- 6183 BELLSYSTEM24 Holdings, Inc.｜choruko_reversal｜⚠減速(1)｜⚪妥当｜FAIL_UWAHIGE｜1,330円｜💰13.4万円｜—
- 6753 Sharp Corporation｜choruko_reversal｜🔻悪化(1)｜⚪妥当｜PASS｜591円｜💰5.9万円｜reversal 590.6 想定損失幅4.3%。｜⚠日程不明 ⚠業績基調が下向き（🔻悪化）
  > 【業態】総合家電大手。台湾鴻海の傘下。液晶パネル白物家電主力。デバイス、EVに注力。
  > 【いま】終値591円・直近5日+0.73%（材料未確認）
  > 【調子】🔻悪化（1/13）— 減収・質注意
  > 【水準】⚪妥当（3.0/7）— PER15.34倍・PEG—・52週15.2% ／ 💰単元5.9万円
  > 【戦略】当日終値590.6円の指値で反転を取りにいく。SL565円（直近5日安値）
- 8276 HEIWADO CO., LTD.｜choruko_reversal｜⚠減速(1)｜⚪妥当｜PASS｜2,556円｜💰25.6万円｜reversal 2556 想定損失幅3.6%。｜⚠日程不明 ⚠業績基調が下向き（⚠減速）
  > 【業態】滋賀地盤のスーパー。大型店が主力。ドミナント戦略で拡大。中国に百貨店進出。
  > 【いま】終値2,556円・直近5日+1.95%（材料未確認）
  > 【調子】⚠減速（1/13）
  > 【水準】⚪妥当（3.0/7）— PER12.9倍・PEG3.165・52週21.5% ／ 💰単元25.6万円
  > 【戦略】当日終値2556円の指値で反転を取りにいく。SL2464円（直近5日安値）
- 9948 Arcs Company, Limited｜choruko_reversal｜⚠減速(1)｜⚪妥当｜PASS｜3,440円｜💰34.4万円｜reversal 3440 想定損失幅4.4%。｜⚠日程不明 ⚠業績基調が下向き（⚠減速）
  > 【業態】北海道最大の食品スーパー。青森、岩手も首位。ローコスト経営に強み。M&A積極。
  > 【いま】終値3,440円・直近5日-2.27%（材料未確認）
  > 【調子】⚠減速（1/13）
  > 【水準】⚪妥当（3.0/7）— PER14.78倍・PEG6.452・52週38.3% ／ 💰単元34.4万円
  > 【戦略】当日終値3440円の指値で反転を取りにいく。SL3290円（直近5日安値）
- 9974 BELC Co., Ltd.｜choruko_reversal｜⚠減速(1)｜⚪妥当｜PASS｜6,230円｜💰62.3万円｜reversal 6230 想定損失幅4.0%。｜⚠日程不明 ⚠業績基調が下向き（⚠減速）
  > 【業態】埼玉地盤に食品スーパー「ベルク」を展開。自社物流などに強み。イオンと提携。
  > 【いま】終値6,230円・直近5日-0.32%（材料未確認）
  > 【調子】⚠減速（1/13）— 質注意
  > 【水準】⚪妥当（3.0/7）— PER13.11倍・PEG—・52週11.7% ／ 💰単元62.3万円
  > 【戦略】当日終値6230円の指値で反転を取りにいく。SL5980円（直近5日安値）
- 3234 Mori Hills Reit Investment Corporation｜choruko_reversal｜⚠減速(1)｜🟡やや割高｜FAIL_INSEN｜117,200円｜💰11.9万円｜—
- 3249 Industrial & Infrastructure Fund Investment Corporation｜choruko_reversal｜⚠減速(1)｜🟡やや割高｜FAIL_INSEN｜126,000円｜💰12.8万円｜—
- 3283 Nippon Prologis REIT, Inc.｜choruko_reversal｜⚠減速(1)｜🟡やや割高｜FAIL_INSEN｜78,400円｜💰8.0万円｜—
- 3292 AEON REIT Investment Corp.｜choruko_reversal｜⚠減速(1)｜🟡やや割高｜FAIL_INSEN｜104,000円｜💰10.5万円｜—
- 3296 NIPPON REIT Investment Corp｜choruko_reversal｜🔻悪化(1)｜🟡やや割高｜FAIL_INSEN｜74,300円｜💰7.6万円｜—
- 3309 Sekisui House Reit. Inc.｜choruko_reversal｜⚠減速(1)｜🟡やや割高｜FAIL_INSEN｜66,500円｜💰6.7万円｜—
- 3462 Nomura Real Estate Master Fund, Inc.｜choruko_reversal｜⚠減速(1)｜🟡やや割高｜FAIL_INSEN｜126,500円｜💰13.5万円｜—
- 5482 Aichi Steel Corporation｜choruko_reversal｜⚠減速(1)｜🟡やや割高｜FAIL_INSEN｜2,867円｜💰29.4万円｜—
- 8955 Japan Prime Realty Investment Corporation｜choruko_reversal｜⚠減速(1)｜🟡やや割高｜FAIL_INSEN｜89,500円｜💰9.0万円｜—
- 8961 MORI TRUST REIT.Inc｜choruko_reversal｜⚠減速(1)｜🟡やや割高｜FAIL_INSEN｜66,100円｜💰6.7万円｜—
- 8986 Daiwa Securities Living Investment Corporation｜choruko_reversal｜⚠減速(1)｜🟡やや割高｜FAIL_INSEN｜83,000円｜💰8.4万円｜—
- 1946 Toenec Corporation｜choruko_reversal｜⚠減速(1)｜🟡やや割高｜FAIL_INSEN｜2,019円｜💰20.7万円｜—
- 2815 ARIAKE JAPAN Co., Ltd.｜choruko_reversal｜⚠減速(1)｜🟡やや割高｜PASS｜5,270円｜💰52.7万円｜reversal 5270 想定損失幅1.9%。｜📋カルテ窓 11/06(残12営業日) ⚠業績基調が下向き（⚠減速）
  > 【業態】畜産系エキスの天然調味料で首位。業務用中心。抽出から加工まで一貫生産。
  > 【いま】終値5,270円・直近5日+1.15%（材料未確認）
  > 【調子】⚠減速（1/13）— 質注意
  > 【水準】🟡やや割高（2.0/7）— PER17.24倍・PEG—・52週27.0% ／ 💰単元52.7万円
  > 【戦略】当日終値5270円の指値で反転を取りにいく。SL5170円（直近5日安値）
- 5631 Japan Steel Works, Ltd.｜choruko_reversal｜⚠減速(1)｜🟡やや割高｜FAIL_INSEN｜6,378円｜💰67.4万円｜—
- 4928 Noevir Holdings Co., Ltd.｜choruko_reversal｜⚠減速(1)｜🔴過熱｜FAIL_INSEN｜4,680円｜💰46.6万円｜—
- 6960 Fukuda Denshi Co., Ltd.｜choruko_reversal｜⚠減速(1)｜🔴過熱｜FAIL_INSEN｜10,610円｜💰108.6万円｜—
- 9436 Okinawa Cellular Telephone Company｜choruko_reversal｜⚠減速(1)｜🔴過熱｜FAIL_INSEN｜3,370円｜💰34.6万円｜—
- 1662 Japan Petroleum Exploration Co., Ltd.｜choruko_reversal｜🔻悪化(0)｜⚪妥当｜FAIL_INSEN｜1,703円｜💰17.1万円｜—
- 6804 Hosiden Corp.｜choruko_reversal｜🔻悪化(0)｜⚪妥当｜FAIL_INSEN｜2,341円｜💰23.8万円｜—
- 1969 Takasago Thermal Engineering Co., Ltd.｜choruko_reversal｜⚠減速(0)｜⚪妥当｜FAIL_INSEN｜4,083円｜💰41.9万円｜—
- 8585 Orient Corporation｜choruko_reversal｜⚠減速(0)｜⚪妥当｜FAIL_INSEN｜755円｜💰7.8万円｜—
- 8194 Life Corporation｜choruko_reversal｜⚠減速(0)｜🟡やや割高｜PASS｜2,381円｜💰23.8万円｜reversal 2381 想定損失幅3.8%。｜⚠日程不明 ⚠業績基調が下向き（⚠減速）
  > 【業態】食品スーパー大手。首都圏・近畿地方で積極的に展開。三菱商事の持分法。
  > 【いま】終値2,381円・直近5日-1.24%（材料未確認）
  > 【調子】⚠減速（0/13）
  > 【水準】🟡やや割高（2.8/7）— PER10.84倍・PEG3.149・52週16.9% ／ 💰単元23.8万円
  > 【戦略】当日終値2381円の指値で反転を取りにいく。SL2290円（直近5日安値）
- 9533 TOHO GAS Co., Ltd.｜choruko_reversal｜🔻悪化(0)｜🟡やや割高｜FAIL_UWAHIGE｜1,186円｜💰11.8万円｜—
- 9699 NISHIO HOLDINGS CO. LTD.｜choruko_reversal｜⚠減速(0)｜🟡やや割高｜FAIL_INSEN｜4,250円｜💰43.0万円｜—
- 8253 Credit Saison Co., Ltd.｜choruko_reversal｜取得不可｜💎割安｜FAIL_INSEN｜4,149円｜💰41.9万円｜—
- 5831 Shizuoka Financial Group, Inc.｜choruko_reversal｜取得不可｜🟢値頃｜FAIL_INSEN｜3,033円｜💰31.8万円｜—
- 7201 Nissan Motor Co., Ltd.｜choruko_reversal｜業績データ取得不可(経常益予想非開示)｜🟢値頃｜FAIL_UWAHIGE｜280円｜💰2.8万円｜—
- 8345 Bank of Iwate Ltd.｜choruko_reversal｜業績データ取得不可(売上/経常欠損)｜🟢値頃｜FAIL_INSEN｜2,117円｜💰22.6万円｜—
- 3471 Mitsui Fudosan Logistics Park, Inc.｜choruko_reversal｜判定保留(変則決算)｜⚪妥当｜FAIL_INSEN｜96,500円｜💰9.8万円｜—
- 8399 Bank Of The Ryukyus,Limited｜choruko_reversal｜業績データ取得不可(売上/経常欠損)｜⚪妥当｜FAIL_INSEN｜2,777円｜💰29.2万円｜—
- 7381 CCI Group, Inc.｜choruko_reversal｜取得不可｜⚪妥当｜FAIL_INSEN｜1,142円｜💰12.2万円｜—
- 7384 Procrea Holdings,Inc.｜choruko_reversal｜業績データ取得不可(売上/経常欠損)｜⚪妥当｜FAIL_INSEN｜4,105円｜💰45.1万円｜—
- 8174 NIPPON GAS Co., Ltd.｜choruko_reversal｜業績データ取得不可｜⚪妥当｜PASS｜938円｜💰9.4万円｜reversal 937.5 想定損失幅5.2%。
  > 【業態】LPG、都市ガス、電力を販売。関東一円展開。家庭エネ販売一元化。M&Aで拡販。
  > 【いま】終値938円・直近5日+2.47%（材料未確認）
  > 【調子】業績データ取得不可（None/13）
  > 【水準】⚪妥当（4.0/7）— PER21.4倍・PEG—・52週31.2% ／ 💰単元9.4万円
  > 【戦略】当日終値937.5円の指値で反転を取りにいく。SL888.7円（直近5日安値）
- 8304 Aozora Bank, Ltd.｜choruko_reversal｜取得不可｜⚪妥当｜FAIL_INSEN｜3,042円｜💰31.9万円｜—
- 3591 WACOAL HOLDINGS CORP｜choruko_reversal｜🔻悪化｜🟡やや割高｜PASS｜3,578円｜💰35.8万円｜reversal 3578 想定損失幅1.8%。｜📋カルテ窓 11/12(残16営業日) ⚠業績基調が下向き（🔻悪化）
  > 【業態】婦人下着最大手。「ワコール」、「ウイング」ブランドなど。傘下に販売のピーチ・ジョン。
  > 【いま】終値3,578円・直近5日+0.08%（材料未確認）
  > 【調子】🔻悪化（None/13）
  > 【水準】🟡やや割高（2.0/7）— PER98.3倍・PEG—・52週3.9% ／ 💰単元35.8万円
  > 【戦略】当日終値3578円の指値で反転を取りにいく。SL3514円（直近5日安値）
- 8511 Japan Securities Finance Co., Ltd.｜choruko_reversal｜取得不可｜🔴過熱｜FAIL_INSEN｜2,151円｜💰22.2万円｜—
- 7624 NaITO｜stf_kakuhen｜🔥絶好調(10)｜🟢値頃｜FAIL_INSEN｜169円｜💰1.8万円｜—
- 5018 ＭＯＲＥＳＣＯ｜stf_kakuhen｜🔥絶好調(10)｜⚪妥当｜FAIL_INSEN｜2,938円｜💰29.8万円｜—
- 6668 ＡＤプラズマ｜stf_kakuhen｜🔥絶好調(10)｜⚪妥当｜FAIL_INSEN｜4,740円｜💰49.4万円｜—
- 7713 シグマ光機｜stf_kakuhen｜🔥絶好調(10)｜⚪妥当｜FAIL_INSEN｜3,220円｜💰33.2万円｜—
- 5246 ELEMENTS,Inc.｜stf_kakuhen｜🔥絶好調(10)｜⚪妥当｜FAIL_INSEN｜1,085円｜💰12.8万円｜—
- 3498 霞ヶ関Ｃ｜stf_kakuhen｜🔥絶好調(9)｜💎割安｜FAIL_INSEN｜6,740円｜💰69.6万円｜—
- 3994 マネーフォワード｜stf_kakuhen｜🔥絶好調(9)｜🔴過熱｜PASS｜6,582円｜💰65.8万円｜⛔提案なし(手法ブランチ不明)｜⚠日程不明 織り込み済みの可能性（押し目待ち推奨圏）
  > 【業態】クラウド会計中心の法人向けバックオフィスSaaS事業が柱。個人向け家計簿アプリも。
  > 【いま】終値6,582円・直近5日-0.60%（材料未確認）
  > 【調子】🔥絶好調（9/13）
  > 【水準】🔴過熱（1.4/7）— PER—倍・PEG—・52週89.1% ／ 💰単元65.8万円
  > 【戦略】発注対象外（⛔提案なし(手法ブランチ不明)）
- 7811 Nakamoto Packs Co. Ltd.｜stf_kakuhen｜🔥絶好調(8)｜🟢値頃｜FAIL_INSEN｜2,490円｜💰24.1万円｜—
- 4443 Ｓａｎｓａｎ｜stf_kakuhen｜🔥絶好調(8)｜⚪妥当｜PASS｜2,074円｜💰20.7万円｜⛔提案なし(手法ブランチ不明)｜⚠日程不明
  > 【業態】名刺管理サービス最大手。法人向けクラウド、個人向けアプリ展開。請求書データも。
  > 【いま】終値2,074円・直近5日+2.42%（材料未確認）
  > 【調子】🔥絶好調（8/13）
  > 【水準】⚪妥当（3.0/7）— PER27.99倍・PEG0.4235・52週79.4% ／ 💰単元20.7万円
  > 【戦略】発注対象外（⛔提案なし(手法ブランチ不明)）
- 6814 古野電｜stf_kakuhen｜⚡好調(7)｜⚪妥当｜FAIL_INSEN｜8,310円｜💰87.3万円｜—
- 5932 三協立山｜stf_kakuhen｜⚡好調(7)｜⚪妥当｜FAIL_UWAHIGE｜777円｜💰7.8万円｜—
- 3479 ティーケーピー｜stf_kakuhen｜⚡好調(6)｜🔴過熱｜FAIL_INSEN｜1,932円｜💰19.6万円｜—
- 6505 東洋電機製造｜stf_kakuhen｜⚡好調(5)｜⚪妥当｜FAIL_INSEN｜3,180円｜💰31.5万円｜—
- 6532 ベイカレント｜stf_kakuhen｜⚡好調(5)｜🟡やや割高｜PASS｜10,845円｜💰108.5万円｜⛔提案なし(手法ブランチ不明)｜⚠日程不明
  > 【業態】ITコンサルで創業。企業戦略立案・課題解決・実行まで専門提供の総合コンサル。
  > 【いま】終値10,845円・直近5日+26.31%（材料未確認）
  > 【調子】⚡好調（5/13）
  > 【水準】🟡やや割高（2.0/7）— PER33.13倍・PEG1.214・52週96.2% ／ 💰単元108.5万円
  > 【戦略】発注対象外（⛔提案なし(手法ブランチ不明)）
- 4176 ココナラ｜stf_kakuhen｜✅順調(4)｜⚪妥当｜FAIL_INSEN｜305円｜💰3.4万円｜—
- 9211 f-code Inc.｜granville_tenkan｜🔥絶好調(9)｜💎割安｜FAIL_INSEN｜1,307円｜💰14.5万円｜—
- 2334 Eole, Inc.｜granville_oshime｜🔥絶好調(8)｜⚪妥当｜FAIL_INSEN｜541円｜💰5.6万円｜—
- 4431 スマレジ｜changepoint🔔｜🔥絶好調(8)｜🟡やや割高｜FAIL_INSEN｜3,835円｜💰40.7万円｜—
- 5590 NETSTARS Co.,Ltd.｜changepoint🔔｜⚡好調(7)｜🟢値頃｜FAIL_INSEN｜676円｜💰7.0万円｜—
- 4493 Cyber Security Cloud, Inc.｜changepoint🔔｜✅順調(3)｜🔴過熱｜FAIL_INSEN｜3,020円｜💰38.1万円｜—
- 4419 Ｆｉｎａｔｅｘｔホールディングス｜—｜🔥絶好調(10)｜⚪妥当｜FAIL_INSEN｜1,489円｜💰15.5万円｜—
- 6492 Okano Valve Mfg. Co., Ltd.｜—｜🔥絶好調(9)｜⚪妥当｜FAIL_INSEN｜12,980円｜💰136.4万円｜—
- 6395 TADANO Ltd.｜—｜⚡好調(7)｜🟢値頃｜FAIL_INSEN｜1,295円｜💰13.2万円｜—
- 8370 Kiyo Bank, Ltd.｜—｜取得不可｜🟢値頃｜FAIL_INSEN｜1,545円｜💰16.4万円｜—

## グランビル銘柄
- 5254 Arent, Inc.｜granville_tenkan｜🚀確変(12)｜⚪妥当｜FAIL_INSEN｜4,010円｜💰41.2万円｜—
- 8944 Land Business Co., Ltd.｜granville_tenkan｜🔥絶好調(10)｜💎割安｜FAIL_INSEN｜253円｜💰2.6万円｜—
- 7725 INTER ACTION Corporation｜granville_tenkan｜🔥絶好調(10)｜🟢値頃｜FAIL_INSEN｜1,729円｜💰17.2万円｜—
- 9553 MicroAd, Inc.｜granville_tenkan｜🔥絶好調(10)｜🟢値頃｜FAIL_INSEN｜587円｜💰6.1万円｜—
- 6905 Cosel Co., Ltd.｜granville_tenkan｜🔥絶好調(10)｜⚪妥当｜FAIL_INSEN｜1,326円｜💰13.6万円｜—
- 2986 LA Holdings Co.,Ltd｜granville_tenkan｜🔥絶好調(9)｜💎割安｜FAIL_INSEN｜2,642円｜💰27.1万円｜—
- 6562 Geniee, Inc.｜granville_tenkan｜🔥絶好調(8)｜💎割安｜FAIL_INSEN｜931円｜💰10.0万円｜—
- 1945 Tokyo Energy & Systems Inc.｜granville_tenkan｜🔥絶好調(8)｜💎割安｜FAIL_INSEN｜1,965円｜💰20.1万円｜—
- 9006 京浜急行電鉄｜granville_tenkan｜🔥絶好調(8)｜🟢値頃｜FAIL_UWAHIGE｜1,540円｜💰15.4万円｜—
- 6473 JTEKT Corporation｜granville_tenkan｜⚠減速(8)｜⚪妥当｜FAIL_INSEN｜2,102円｜💰21.4万円｜—
- 8697 Japan Exchange Group, Inc.｜granville_tenkan｜🔥絶好調(8)｜🟡やや割高｜FAIL_INSEN｜2,164円｜💰22.4万円｜—
- 6255 NPC Incorporated｜granville_tenkan｜⚡好調(7)｜🟢値頃｜FAIL_INSEN｜667円｜💰6.8万円｜—
- 8095 Astena Holdings Co.,Ltd.｜granville_tenkan｜⚡好調(7)｜🟢値頃｜FAIL_INSEN｜515円｜💰5.2万円｜—
- 8793 ＮＥＣキャピタルソリューション｜granville_tenkan｜⚡好調(7)｜🟢値頃｜FAIL_INSEN｜3,960円｜💰40.5万円｜—
- 3496 AZOOM CO.,LTD｜granville_tenkan｜⚡好調(7)｜⚪妥当｜FAIL_INSEN｜4,845円｜💰49.2万円｜—
- 4544 H.U.Group Holdings, Inc.｜granville_tenkan｜⚡好調(7)｜⚪妥当｜PASS｜3,708円｜💰37.1万円｜momentum 3720 想定損失幅6.1%。｜📋カルテ窓 11/11(残15営業日)
  > 【業態】臨床検査薬大手・富士レビオと臨床検査・SRLが統合。ヘルス関連サービス事業も。
  > 【いま】終値3,708円・直近5日+1.62%（材料未確認）
  > 【調子】⚡好調（7/13）
  > 【水準】⚪妥当（4.0/7）— PER40.09倍・PEG0.2199・52週66.5% ／ 💰単元37.1万円
  > 【戦略】当日高値超えの逆指値3720円で順張り参戦を検討。上限3757.2円・SL3492.1円目安
- 7744 Noritsu Koki Co., Ltd.｜granville_tenkan｜⚡好調(7)｜⚪妥当｜FAIL_UWAHIGE｜2,067円｜💰20.8万円｜—
- 9064 ヤマトホールディングス｜granville_tenkan｜⚡好調(7)｜⚪妥当｜FAIL_UWAHIGE｜2,072円｜💰20.7万円｜—
- 3741 Systems Engineering Consultants Co., Ltd.｜granville_tenkan｜⚡好調(7)｜⚪妥当｜FAIL_INSEN｜2,950円｜💰30.7万円｜—
- 6302 Sumitomo Heavy Industries, Ltd.｜granville_tenkan｜⚡好調(7)｜⚪妥当｜FAIL_INSEN｜5,566円｜💰57.2万円｜—
- 4507 Shionogi & Co., Ltd.｜granville_tenkan｜⚡好調(7)｜🟡やや割高｜PASS｜2,978円｜💰29.8万円｜⛔提案なし(指名鮮度切れ 12営業日)
  > 【業態】抗HIV薬が大型化。高脂血症薬、鎮痛、感染分野に強み。海外進出本格化。
  > 【いま】終値2,978円・直近5日+5.83%（材料未確認）
  > 【調子】⚡好調（7/13）— 質注意
  > 【水準】🟡やや割高（2.0/7）— PER12.07倍・PEG—・52週42.5% ／ 💰単元29.8万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 12営業日)）
- 5838 Rakuten Bank, Ltd.｜granville_tenkan｜⚡好調(6)｜💎割安｜FAIL_INSEN｜5,864円｜💰60.3万円｜—
- 4763 クリーク・アンド・リバー社｜granville_tenkan｜⚡好調(6)｜🟢値頃｜FAIL_INSEN｜1,450円｜💰14.5万円｜—
- 6470 Taiho Kogyo Co., Ltd.｜granville_tenkan｜⚡好調(6)｜⚪妥当｜FAIL_INSEN｜1,141円｜💰11.6万円｜—
- 7199 Premium Group Co., Ltd.｜granville_tenkan｜⚡好調(6)｜⚪妥当｜FAIL_INSEN｜2,197円｜💰22.2万円｜—
- 3064 MonotaRO Co., Ltd.｜granville_tenkan｜⚡好調(6)｜🔴過熱｜FAIL_INSEN｜2,347円｜💰23.9万円｜—
- 3935 Edia Co. Ltd.｜granville_tenkan｜⚡好調(5)｜💎割安｜FAIL_INSEN｜737円｜💰7.3万円｜—
- 6196 Strike Group Co. Ltd.｜granville_tenkan｜⚡好調(5)｜💎割安｜FAIL_INSEN｜1,385円｜💰14.1万円｜—
- 3562 No.1 Co., Ltd.｜granville_tenkan｜⚡好調(5)｜🟢値頃｜FAIL_INSEN｜1,643円｜💰17.0万円｜—
- 8061 Seika Corporation｜granville_tenkan｜⚡好調(5)｜🟢値頃｜FAIL_INSEN｜2,851円｜💰30.3万円｜—
- 9048 名古屋鉄道｜granville_tenkan｜⚡好調(5)｜🟢値頃｜FAIL_INSEN｜1,838円｜💰18.5万円｜—
- 2331 ALSOK CO., LTD.｜granville_tenkan｜⚡好調(5)｜⚪妥当｜PASS｜1,216円｜💰12.2万円｜⛔提案なし(指名鮮度切れ 15営業日)｜📋カルテ窓 11/10(残14営業日)
  > 【業態】警備サービス大手。機械警備が主力。現金輸送に強み。介護・高齢者向け注力。
  > 【いま】終値1,216円・直近5日+2.83%（材料未確認）
  > 【調子】⚡好調（5/13）
  > 【水準】⚪妥当（4.0/7）— PER15.55倍・PEG0.9039・52週59.0% ／ 💰単元12.2万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 15営業日)）
- 3661 m-up holdings, Inc.｜granville_tenkan｜⚡好調(5)｜⚪妥当｜FAIL_INSEN｜877円｜💰8.9万円｜—
- 6432 Takeuchi Mfg.Co., Ltd.｜granville_tenkan｜⚡好調(5)｜⚪妥当｜FAIL_INSEN｜7,680円｜💰77.9万円｜—
- 7970 Shin-Etsu Polymer Co., Ltd.｜granville_tenkan｜⚡好調(5)｜🟡やや割高｜FAIL_INSEN｜2,296円｜💰23.8万円｜—
- 8020 Kanematsu Corporation｜granville_tenkan｜⚡好調(5)｜🟡やや割高｜FAIL_INSEN｜2,294円｜💰24.0万円｜—
- 9828 Genki Global Dining Concepts Corp｜granville_tenkan｜⚡好調(5)｜🔴過熱｜PASS｜3,530円｜💰35.3万円｜⛔提案なし(指名鮮度切れ 15営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
  > 【業態】「魚べい」「元気寿司」が主力。中国、東南アジアなどでFC展開。親会社は神明。
  > 【いま】終値3,530円・直近5日+2.02%（材料未確認）
  > 【調子】⚡好調（5/13）— 質注意
  > 【水準】🔴過熱（1.0/7）— PER18.9倍・PEG1.505・52週86.5% ／ 💰単元35.3万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 15営業日)）
- 6454 Max Co., Ltd.｜granville_tenkan｜⚡好調(5)｜🔴過熱｜FAIL_INSEN｜1,898円｜💰19.3万円｜—
- 2288 Marudai Food Co., Ltd.｜granville_tenkan｜✅順調(4)｜🟢値頃｜FAIL_UWAHIGE｜2,181円｜💰21.8万円｜—
- 5036 Japan Business Systems, Inc.｜granville_tenkan｜✅順調(4)｜⚪妥当｜FAIL_INSEN｜1,850円｜💰18.8万円｜—
- 8014 Chori Co., Ltd.｜granville_tenkan｜✅順調(4)｜⚪妥当｜FAIL_INSEN｜4,200円｜💰43.0万円｜—
- 6988 日東電工｜granville_tenkan｜✅順調(4)｜🟡やや割高｜FAIL_UWAHIGE｜3,627円｜💰36.4万円｜—
- 6371 Tsubakimoto Chain Co.｜granville_tenkan｜✅順調(4)｜🔴過熱｜FAIL_INSEN｜2,636円｜💰26.8万円｜—
- 6592 Mabuchi Motor Co., Ltd.｜granville_tenkan｜✅順調(4)｜🔴過熱｜FAIL_INSEN｜1,730円｜💰17.7万円｜—
- 8060 キヤノンマーケティングジャパン｜granville_tenkan｜✅順調(4)｜🔴過熱｜FAIL_INSEN｜4,000円｜💰40.3万円｜—
- 4166 Cacco, Inc.｜granville_tenkan｜✅順調(3)｜💎割安｜FAIL_INSEN｜680円｜💰7.3万円｜—
- 8850 スターツコーポレーション｜granville_tenkan｜✅順調(3)｜⚪妥当｜FAIL_UWAHIGE｜4,550円｜💰46.0万円｜—
- 3433 TOCALO Co., Ltd.｜granville_tenkan｜✅順調(3)｜⚪妥当｜FAIL_INSEN｜2,800円｜💰29.1万円｜—
- 8927 Meiho Enterprise Co., Ltd.｜granville_tenkan｜✅順調(3)｜⚪妥当｜FAIL_INSEN｜481円｜💰4.9万円｜—
- 186A Astroscale Holdings Inc.｜granville_tenkan｜✅順調(3)｜🟡やや割高｜FAIL_INSEN｜1,012円｜💰10.8万円｜—
- 4183 Mitsui Chemicals, Inc.｜granville_tenkan｜✅順調(3)｜🟡やや割高｜FAIL_INSEN｜2,092円｜💰21.0万円｜—
- 4272 Nippon Kayaku Co., Ltd.｜granville_tenkan｜✅順調(3)｜🟡やや割高｜FAIL_INSEN｜2,129円｜💰21.6万円｜—
- 4956 Konishi Co., Ltd.｜granville_tenkan｜✅順調(3)｜🟡やや割高｜FAIL_INSEN｜1,502円｜💰15.2万円｜—
- 5461 Chubu Steel Plate Co., Ltd.｜granville_tenkan｜🔻悪化(3)｜🟡やや割高｜FAIL_INSEN｜2,152円｜💰21.4万円｜—
- 7181 JAPAN POST INSURANCE Co., Ltd.｜granville_tenkan｜⚠減速(3)｜🔴過熱｜FAIL_INSEN｜1,671円｜💰17.3万円｜—
- 7734 Riken Keiki Co., Ltd.｜granville_tenkan｜✅順調(3)｜🔴過熱｜FAIL_INSEN｜3,425円｜💰35.5万円｜—
- 7513 Kojima Co., Ltd.｜granville_tenkan｜✅順調(3)｜🔴過熱｜FAIL_INSEN｜1,459円｜💰14.6万円｜—
- 6328 Ebara Jitsugyo Co., Ltd.｜granville_tenkan｜➖横ばい(2)｜⚪妥当｜FAIL_INSEN｜2,431円｜💰24.9万円｜—
- 2002 日清製粉グループ本社｜granville_tenkan｜➖横ばい(2)｜🟡やや割高｜PASS｜2,060円｜💰20.6万円｜⛔提案なし(指名鮮度切れ 17営業日)
  > 【業態】製粉最大手。パスタ類に強み、エンジニアリングも。製粉は海外展開を積極化。
  > 【いま】終値2,060円・直近5日+2.59%（材料未確認）
  > 【調子】➖横ばい（2/13）— 質注意
  > 【水準】🟡やや割高（2.0/7）— PER14.05倍・PEG—・52週70.8% ／ 💰単元20.6万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 17営業日)）
- 6208 Ishikawa Seisakusho,Ltd.｜granville_tenkan｜🔻悪化(2)｜🟡やや割高｜FAIL_INSEN｜1,620円｜💰16.6万円｜—
- 2413 エムスリー｜granville_tenkan｜➖横ばい(2)｜🔴過熱｜FAIL_UWAHIGE｜1,898円｜💰19.1万円｜—
- 4617 Chugoku Marine Paints,Ltd.｜granville_tenkan｜➖横ばい(2)｜🔴過熱｜FAIL_INSEN｜3,615円｜💰37.1万円｜—
- 7751 キヤノン｜granville_tenkan｜➖横ばい(2)｜🔴過熱｜FAIL_INSEN｜4,807円｜💰48.2万円｜—
- 8081 Kanaden Corporation｜granville_tenkan｜➖横ばい(2)｜🔴過熱｜FAIL_INSEN｜2,661円｜💰28.0万円｜—
- 5071 VIS Co., Ltd.｜granville_tenkan｜⚠減速(1)｜⚪妥当｜FAIL_UWAHIGE｜1,383円｜💰13.8万円｜—
- 6770 Alps Alpine Co., Ltd.｜granville_tenkan｜⚠減速(1)｜🟡やや割高｜FAIL_INSEN｜2,091円｜💰21.4万円｜—
- 1815 鉄建建設｜granville_tenkan｜⚠減速(0)｜⚪妥当｜FAIL_INSEN｜2,151円｜💰21.8万円｜—
- 4375 Safie Inc.｜granville_tenkan｜取得不可｜💎割安｜FAIL_INSEN｜661円｜💰6.8万円｜—
- 8424 芙蓉総合リース｜granville_tenkan｜取得不可｜💎割安｜FAIL_INSEN｜4,275円｜💰43.1万円｜—
- 2871 ニチレイ｜granville_tenkan｜業績データ取得不可｜🔴過熱｜FAIL_UWAHIGE｜2,150円｜💰21.4万円｜—
- 4549 Eiken Chemical Co., Ltd.｜granville_tenkan｜—｜—｜FAIL_INSEN｜2,411円｜💰—｜—
- 4552 JCR Pharmaceuticals Co., Ltd.｜granville_tenkan｜—｜—｜FAIL_INSEN｜522円｜💰—｜—
- 4937 Ｇ−ＷＡＱＯＯ｜granville_oshime｜🚀確変(13)｜⚪妥当｜FAIL_INSEN｜2,312円｜💰23.2万円｜—
- 276A CCReB Advisors Inc.｜granville_oshime｜🚀確変(12)｜💎割安｜FAIL_INSEN｜3,780円｜💰40.9万円｜—
- 3083 Star seeds Co.,Ltd.｜granville_oshime｜🚀確変(12)｜⚪妥当｜FAIL_INSEN｜1,044円｜💰10.6万円｜—
- 290A ＳＹＮＳＰＥＣＴＩＶＥ｜granville_oshime｜🚀確変(11)｜🟢値頃｜FAIL_INSEN｜1,141円｜💰12.2万円｜—
- 5243 note inc.｜granville_oshime｜🚀確変(11)｜⚪妥当｜FAIL_INSEN｜2,869円｜💰30.1万円｜—
- 7806 MTG Co., Ltd.｜granville_oshime｜🚀確変(11)｜⚪妥当｜FAIL_INSEN｜8,030円｜💰84.3万円｜—
- 6834 Seikoh Giken Co., Ltd.｜granville_oshime｜🔥絶好調(10)｜💎割安｜FAIL_INSEN｜5,500円｜💰58.9万円｜—
- 8336 Musashino Bank, Ltd.｜granville_oshime｜🔥絶好調(9)｜⚪妥当｜FAIL_INSEN｜2,559円｜💰27.1万円｜—
- 8008 Yondoshi Holdings, Inc.｜granville_oshime｜🔥絶好調(9)｜⚪妥当｜FAIL_INSEN｜2,015円｜💰20.1万円｜—
- 4180 ＡＰＰＩＥＲ　ＧＲＯＵＰ｜granville_oshime｜🔥絶好調(8)｜⚪妥当｜FAIL_INSEN｜1,379円｜💰14.1万円｜—
- 8346 Toho Bank, Ltd.｜granville_oshime｜🔥絶好調(8)｜⚪妥当｜FAIL_INSEN｜970円｜💰10.3万円｜—
- 7856 HAGIHARA INDUSTRIES INC.｜granville_oshime｜🔥絶好調(8)｜🟡やや割高｜FAIL_INSEN｜2,038円｜💰20.7万円｜—
- 1879 新日本建設｜granville_oshime｜⚡好調(7)｜💎割安｜FAIL_INSEN｜2,182円｜💰22.2万円｜—
- 6736 Suncorporation｜granville_oshime｜⚡好調(7)｜⚪妥当｜FAIL_INSEN｜9,740円｜💰97.4万円｜—
- 6523 PHC Holdings Corp.｜granville_oshime｜⚠減速(6)｜🟢値頃｜FAIL_INSEN｜1,295円｜💰13.7万円｜—
- 2767 円谷フィールズホールディングス｜granville_oshime｜⚡好調(6)｜⚪妥当｜FAIL_UWAHIGE｜2,525円｜💰25.2万円｜—
- 4667 Aisan Technology Co., Ltd.｜granville_oshime｜⚡好調(6)｜⚪妥当｜FAIL_INSEN｜938円｜💰9.7万円｜—
- 6023 ダイハツインフィニアース｜granville_oshime｜⚡好調(6)｜⚪妥当｜FAIL_INSEN｜2,885円｜💰31.9万円｜—
- 7609 Daitron Co., Ltd.｜granville_oshime｜⚡好調(6)｜⚪妥当｜FAIL_INSEN｜4,040円｜💰43.5万円｜—
- 6227 AIMECHATEC Ltd.｜granville_oshime｜⚡好調(6)｜⚪妥当｜FAIL_INSEN｜6,090円｜💰68.5万円｜—
- 2602 日清オイリオグループ｜granville_oshime｜⚡好調(6)｜🟡やや割高｜FAIL_INSEN｜2,057円｜💰20.5万円｜—
- 4413 baudroie,inc.｜granville_oshime｜⚡好調(6)｜🟡やや割高｜FAIL_INSEN｜2,936円｜💰29.9万円｜—
- 8919 カチタス｜granville_oshime｜⚡好調(6)｜🟡やや割高｜FAIL_INSEN｜3,265円｜💰34.0万円｜—
- 7616 Colowide Co., Ltd.｜granville_oshime｜⚡好調(6)｜🔴過熱｜PASS｜2,201円｜💰22.0万円｜oshime 2047 想定損失幅0.5%。｜⚠日程不明
  > 【業態】外食大手。居酒屋中心に直営展開。傘下にレインズ、アトム、カッパクリエ、大戸屋など。
  > 【いま】終値2,201円・直近5日+7.76%（材料未確認）
  > 【調子】⚡好調（6/13）
  > 【水準】🔴過熱（0.0/7）— PER110.6倍・PEG5.643・52週100.0% ／ 💰単元22.0万円
  > 【戦略】2047円までの押し目を指値で待つ。SL2037.2円（25日線基準）
- 8714 Senshu Ikeda Holdings,Inc.｜granville_oshime｜⚡好調(5)｜⚪妥当｜FAIL_INSEN｜973円｜💰10.4万円｜—
- 7350 Okinawa Financial Group, Inc.｜granville_oshime｜⚡好調(5)｜⚪妥当｜FAIL_INSEN｜6,950円｜💰73.9万円｜—
- 6058 VECTOR Inc.｜granville_oshime｜⚡好調(5)｜🔴過熱｜FAIL_INSEN｜2,000円｜💰20.4万円｜—
- 4475 HENNGE K.K.｜granville_oshime｜⚡好調(5)｜🔴過熱｜FAIL_INSEN｜1,878円｜💰20.8万円｜—
- 4373 Simplex Holdings,Inc.｜granville_oshime｜✅順調(4)｜🟡やや割高｜FAIL_INSEN｜1,255円｜💰12.6万円｜—
- 3097 Monogatari Corporation｜granville_oshime｜✅順調(4)｜🔴過熱｜PASS｜6,090円｜💰60.9万円｜⏳待機: 到達まで乖離-9.4% oshime 5520 想定損失幅0.5%。｜📋カルテ窓 11/13(残17営業日)
  > 【業態】中部地盤の外食中堅。食べ放題「焼肉きんぐ」が主力。ラーメンやお好み焼きも。
  > 【いま】終値6,090円・直近5日+9.93%（材料未確認）
  > 【調子】✅順調（4/13）
  > 【水準】🔴過熱（1.0/7）— PER26.71倍・PEG2.163・52週99.6% ／ 💰単元60.9万円
  > 【戦略】5520円までの押し目を指値で待つ。SL5492.4円（25日線基準）
- 6998 Nippon Tungsten Co., Ltd.｜granville_oshime｜✅順調(4)｜🔴過熱｜FAIL_INSEN｜3,260円｜💰35.4万円｜—
- 5208 Arisawa Mfg.Co., Ltd.｜granville_oshime｜✅順調(4)｜🔴過熱｜FAIL_INSEN｜2,674円｜💰28.3万円｜—
- 5985 SUNCALL CORPORATION｜granville_oshime｜✅順調(3)｜⚪妥当｜FAIL_INSEN｜2,095円｜💰22.9万円｜—
- 1518 三井松島ホールディングス｜granville_oshime｜✅順調(3)｜🟡やや割高｜FAIL_INSEN｜2,230円｜💰22.9万円｜—
- 6379 RAIZNEXT Corporation｜granville_oshime｜✅順調(3)｜🔴過熱｜FAIL_INSEN｜1,008円｜💰10.3万円｜—
- 9044 NANKAI Co., Ltd.｜granville_oshime｜✅順調(3)｜🟡やや割高｜FAIL_INSEN｜2,992円｜💰29.9万円｜—
- 3107 ダイワボウホールディングス｜granville_oshime｜⚠減速(3)｜🔴過熱｜FAIL_INSEN｜3,529円｜💰36.5万円｜—
- 4044 Central Glass Co., Ltd.｜granville_oshime｜✅順調(3)｜🔴過熱｜FAIL_INSEN｜4,460円｜💰46.2万円｜—
- 4208 UBE Corporation｜granville_oshime｜✅順調(3)｜🔴過熱｜FAIL_INSEN｜3,269円｜💰33.4万円｜—
- 456A Human Made Inc.｜granville_oshime｜✅順調(3)｜🔴過熱｜FAIL_INSEN｜1,760円｜💰15.6万円｜—
- 7504 Kohsoku Corporation｜granville_oshime｜✅順調(3)｜🔴過熱｜FAIL_INSEN｜4,710円｜💰47.8万円｜—
- 9509 Hokkaido Electric Power Company,Incorporated｜granville_oshime｜🔻悪化(2)｜⚪妥当｜FAIL_INSEN｜1,089円｜💰10.9万円｜—
- 6072 Jibannet Holdings Co., Ltd.｜granville_oshime｜🔻悪化(2)｜🟡やや割高｜FAIL_INSEN｜1,006円｜💰10.3万円｜—
- 9505 Hokuriku Electric Power Company｜granville_oshime｜🔻悪化(2)｜🟡やや割高｜FAIL_UWAHIGE｜1,052円｜💰10.5万円｜—
- 7630 Ichibanya Co., Ltd.｜granville_oshime｜➖横ばい(2)｜🔴過熱｜PASS｜1,075円｜💰10.8万円｜⛔型不一致: 既に支持帯以下｜⚠日程不明
  > 【業態】カレー専門店を直営・FCで全国展開。海外出店を加速。パスタなど新業態も。
  > 【いま】終値1,075円・直近5日+2.58%（材料未確認）
  > 【調子】➖横ばい（2/13）— 質注意
  > 【水準】🔴過熱（1.0/7）— PER63.24倍・PEG57.31・52週67.0% ／ 💰単元10.8万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 8043 Starzen Company Limited｜granville_oshime｜➖横ばい(2)｜🔴過熱｜FAIL_INSEN｜1,539円｜💰15.5万円｜—
- 9616 共立メンテナンス｜granville_oshime｜➖横ばい(2)｜🔴過熱｜FAIL_INSEN｜3,387円｜💰34.1万円｜—
- 9900 Sagami Holdings Corp.｜granville_oshime｜➖横ばい(2)｜🔴過熱｜PASS｜1,145円｜💰11.4万円｜⛔提案なし(指名鮮度切れ 12営業日)｜📋カルテ窓 11/12(残16営業日)
  > 【業態】中部地盤の麺類中心とした外食チェーン。郊外中心に出店。海外に和食店も。
  > 【いま】終値1,145円・直近5日+5.05%（材料未確認）
  > 【調子】➖横ばい（2/13）— 質注意
  > 【水準】🔴過熱（0.0/7）— PER57.83倍・PEG—・52週90.4% ／ 💰単元11.4万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 12営業日)）
- 3048 ビックカメラ｜granville_oshime｜⚠減速(1)｜🟡やや割高｜FAIL_INSEN｜1,766円｜💰17.8万円｜—
- 8255 Axial Retailing, Inc.｜granville_oshime｜⚠減速(1)｜🔴過熱｜FAIL_UWAHIGE｜1,287円｜💰12.7万円｜—
- 8097 SAN-AI OBBLI CO. LTD｜granville_oshime｜⚠減速(1)｜🔴過熱｜FAIL_UWAHIGE｜2,494円｜💰24.8万円｜—
- 8059 Daiichi Jitsugyo Co., Ltd.｜granville_oshime｜⚠減速(0)｜🔴過熱｜FAIL_INSEN｜3,520円｜💰36.0万円｜—
- 9166 GENDA Inc.｜granville_oshime｜業績データ取得不可｜🟢値頃｜FAIL_INSEN｜668円｜💰6.8万円｜—
- 8343 Akita Bank, Ltd.｜granville_oshime｜業績データ取得不可(売上/経常欠損)｜🟢値頃｜FAIL_INSEN｜1,419円｜💰15.7万円｜—
- 8361 Ogaki Kyoritsu Bank, Ltd.｜granville_oshime｜取得不可｜🟢値頃｜FAIL_INSEN｜1,514円｜💰16.5万円｜—
- 336A ダイナミックマッププラットフォーム｜granville_oshime｜業績データ取得不可(経常益予想非開示)｜⚪妥当｜FAIL_INSEN｜1,234円｜💰13.2万円｜—
- 8367 Nanto Bank Ltd.｜granville_oshime｜取得不可｜⚪妥当｜FAIL_INSEN｜1,759円｜💰18.6万円｜—
- 4565 Nxera Pharma Co., Ltd.｜granville_oshime｜業績データ取得不可(経常益予想非開示)｜🟡やや割高｜FAIL_INSEN｜1,196円｜💰12.5万円｜—
- 6027 Bengo4.com, Inc.｜granville_oshime｜業績データ取得不可｜🟡やや割高｜FAIL_INSEN｜4,865円｜💰48.1万円｜—
- 8362 Fukui Bank, Ltd.｜granville_oshime｜🔻悪化｜🔴過熱｜FAIL_INSEN｜6,540円｜💰71.4万円｜—
- 8410 Seven Bank, Ltd.｜granville_oshime｜—｜—｜FAIL_INSEN｜333円｜💰—｜—
- 8622 Mito Securities Co., Ltd.｜granville_oshime｜取得不可｜⏸判定不能｜FAIL_INSEN｜777円｜💰8.2万円｜—
- 8624 Ichiyoshi Securities Co., Ltd.｜granville_oshime｜取得不可｜⏸判定不能｜FAIL_INSEN｜1,530円｜💰15.7万円｜—
- 8628 松井証券｜granville_oshime｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜1,073円｜💰11.1万円｜—
- 8708 アイザワ証券グループ｜granville_oshime｜取得不可｜⏸判定不能｜FAIL_INSEN｜1,546円｜💰16.1万円｜—
- 6769 Thine Electronics, Inc.｜granville_rebound｜🚀確変(11)｜⚪妥当｜FAIL_INSEN｜1,020円｜💰11.1万円｜—
- 2122 インタースペース｜granville_rebound｜🔥絶好調(9)｜⚪妥当｜FAIL_INSEN｜1,330円｜💰13.4万円｜—
- 6963 ROHM Company Limited｜granville_rebound｜🔥絶好調(9)｜⚪妥当｜FAIL_INSEN｜3,903円｜💰40.6万円｜—
- 8995 Makoto Construction Co,Ltd｜granville_rebound｜🔥絶好調(9)｜⚪妥当｜FAIL_UWAHIGE｜1,696円｜💰16.5万円｜—
- 5242 EYEZ INC.｜granville_rebound｜⚡好調(7)｜🔴過熱｜PASS｜2,866円｜💰28.7万円｜reversal 2866 想定損失幅37.2%。 ⚠1単元でリスク枠超過（106,600円）｜📋カルテ窓 11/13(残17営業日)
  > 【業態】広告業界に特化マッチングプラットフォーム「メディアレーダー」を提供。コスメ情報に進出。
  > 【いま】終値2,866円・直近5日+52.45%（材料未確認）
  > 【調子】⚡好調（7/13）
  > 【水準】🔴過熱（0.0/7）— PER988.3倍・PEG8.984・52週85.7% ／ 💰単元28.7万円
  > 【戦略】当日終値2866円の指値で反転を取りにいく。SL1800円（直近5日安値）／⚠1単元リスク106,600円（枠超過）
- 2354 YE DIGITAL CORPORATION｜granville_rebound｜⚡好調(5)｜🟢値頃｜FAIL_INSEN｜1,004円｜💰10.8万円｜—
- 6597 HPC SYSTEMS Inc.｜granville_rebound｜⚡好調(5)｜🟢値頃｜FAIL_INSEN｜3,145円｜💰35.6万円｜—
- 3687 Fixstars Corp.｜granville_rebound｜⚡好調(5)｜⚪妥当｜FAIL_INSEN｜1,957円｜💰21.0万円｜—
- 5574 ABEJA,Inc.｜granville_rebound｜⚡好調(5)｜🟡やや割高｜FAIL_INSEN｜2,415円｜💰24.1万円｜—
- 4997 日本農薬｜granville_rebound｜✅順調(4)｜🟡やや割高｜FAIL_INSEN｜1,055円｜💰10.7万円｜—
- 1407 West Holdings Corporation｜granville_rebound｜✅順調(3)｜🟢値頃｜FAIL_INSEN｜2,154円｜💰22.7万円｜—
- 4346 NEXYZ.Group Corporation｜granville_rebound｜✅順調(3)｜🟢値頃｜FAIL_INSEN｜732円｜💰7.5万円｜—
- 7354 Direct Marketing MiX Inc.｜granville_rebound｜✅順調(3)｜⚪妥当｜FAIL_INSEN｜337円｜💰3.5万円｜—
- 2681 2nd RETAILING Co., Ltd.｜granville_rebound｜✅順調(3)｜🟡やや割高｜FAIL_INSEN｜2,033円｜💰21.9万円｜—
- 4082 第一稀元素化学工業｜granville_rebound｜🔻悪化(3)｜🟡やや割高｜FAIL_INSEN｜1,789円｜💰18.7万円｜—
- 3653 Morpho, Inc.｜granville_rebound｜🔻悪化(2)｜💎割安｜FAIL_INSEN｜866円｜💰9.1万円｜—
- 3907 Silicon Studio Corp.｜granville_rebound｜🔻悪化(2)｜🟢値頃｜FAIL_INSEN｜1,443円｜💰16.2万円｜—
- 4440 WITZ Corp.｜granville_rebound｜➖横ばい(2)｜🔴過熱｜FAIL_INSEN｜1,771円｜💰18.8万円｜—
- 8163 SRS HOLDINGS CO.,LTD.｜granville_rebound｜➖横ばい(2)｜🔴過熱｜PASS｜1,684円｜💰16.8万円｜⛔提案なし(指名鮮度切れ 12営業日)｜📋カルテ窓 11/09(残13営業日)
  > 【業態】関西の外食中堅。ファミレス「和食さと」主力に「さん天」「にぎり長次郎」など。
  > 【いま】終値1,684円・直近5日+13.63%（材料未確認）
  > 【調子】➖横ばい（2/13）— 質注意
  > 【水準】🔴過熱（0.0/7）— PER38.71倍・PEG193.2・52週99.1% ／ 💰単元16.8万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 12営業日)）
- 4691 Washington Hotel Corp.｜granville_rebound｜⚠減速(1)｜⚪妥当｜FAIL_INSEN｜1,838円｜💰19.1万円｜—
- 6203 Howa Machinery, Ltd.｜granville_rebound｜⚠減速(1)｜🟡やや割高｜FAIL_INSEN｜2,000円｜💰20.8万円｜—
- 6522 アスタリスク｜granville_rebound｜⚠減速(0)｜⚪妥当｜FAIL_INSEN｜867円｜💰9.2万円｜—
- 8360 Yamanashi Chuo Bank, Ltd.｜granville_rebound｜取得不可｜💎割安｜FAIL_INSEN｜1,257円｜💰13.4万円｜—
- 3778 SAKURA Internet Inc.｜granville_rebound｜業績データ取得不可｜⚪妥当｜FAIL_INSEN｜3,100円｜💰32.5万円｜—
- 8368 Hyakugo Bank, Ltd.｜granville_rebound｜取得不可｜🟡やや割高｜FAIL_INSEN｜2,115円｜💰22.7万円｜—
- 8713 Fidea Holdings Co.Ltd.｜granville_rebound｜業績データ取得不可(売上/経常欠損)｜🔴過熱｜FAIL_INSEN｜2,329円｜💰25.0万円｜—
- 3691 DIGITAL PLUS, Inc.｜granville_rebound｜—｜—｜FAIL_INSEN｜1,628円｜💰—｜—
- 6645 OMRON Corporation｜granville_rebound｜—｜—｜FAIL_INSEN｜5,715円｜💰—｜—
- 6890 Ferrotec Corporation｜granville_rebound｜—｜—｜FAIL_INSEN｜8,300円｜💰—｜—
- 8524 North Pacific Bank, Ltd.｜granville_rebound｜—｜—｜FAIL_INSEN｜1,130円｜💰—｜—
- 4418 Japan Data Science Consortium Co Ltd.｜changepoint🔔｜⚠減速(3)｜🟡やや割高｜FAIL_INSEN｜1,072円｜💰11.6万円｜—

## 変化点銘柄
- 5803 フジクラ｜changepoint🔔🔔｜🚀確変(12)｜🟢値頃｜FAIL_INSEN｜4,192円｜💰44.8万円｜—
- 4011 Headwaters Co.,Ltd｜changepoint🔔｜🚀確変(11)｜🟢値頃｜FAIL_INSEN｜2,130円｜💰24.1万円｜—
- 6254 野村マイクロ・サイエンス｜changepoint🔔｜🔥絶好調(10)｜💎割安｜FAIL_INSEN｜3,015円｜💰31.6万円｜—
- 4187 大阪有機化学工業｜changepoint🔔｜🔥絶好調(10)｜⚪妥当｜FAIL_INSEN｜4,590円｜💰49.2万円｜—
- 7695 交換できるくん｜changepoint｜🔥絶好調(10)｜⚪妥当｜FAIL_UWAHIGE｜830円｜💰8.4万円｜—
- 6080 Ｍ＆Ａキャピタルパートナーズ｜changepoint🔔｜🔥絶好調(10)｜⚪妥当｜FAIL_INSEN｜4,255円｜💰44.3万円｜—
- 584A LiNKX, Inc.｜changepoint🔔｜🔥絶好調(9)｜🟢値頃｜FAIL_INSEN｜2,127円｜💰23.1万円｜—
- 6136 OSG CORP｜changepoint🔔🔔｜🔥絶好調(9)｜⚪妥当｜FAIL_INSEN｜3,653円｜💰38.6万円｜—
- 6857 アドバンテスト｜changepoint🔔｜🔥絶好調(9)｜⚪妥当｜FAIL_INSEN｜33,870円｜💰344.5万円｜—
- 8151 東陽テクニカ｜changepoint🔔｜🔥絶好調(9)｜⚪妥当｜FAIL_INSEN｜1,875円｜💰19.2万円｜—
- 9962 ミスミグループ本社｜changepoint🔔｜🔥絶好調(9)｜⚪妥当｜FAIL_INSEN｜3,758円｜💰39.4万円｜—
- 4382 HEROZ, Inc.｜changepoint🔔🔔｜🔥絶好調(9)｜🟡やや割高｜FAIL_UWAHIGE｜1,385円｜💰17.5万円｜—
- 7318 セレンディップ・ホールディングス｜changepoint🔔🔔｜🔥絶好調(8)｜💎割安｜FAIL_INSEN｜1,159円｜💰12.4万円｜—
- 9888 UEX LTD｜changepoint🔔｜🔥絶好調(8)｜🟢値頃｜FAIL_INSEN｜1,162円｜💰12.2万円｜—
- 4368 4368｜changepoint🔔｜🔥絶好調(8)｜⚪妥当｜FAIL_INSEN｜3,000円｜💰31.6万円｜—
- 5582 （名称取得不可）｜changepoint🔔｜🔥絶好調(8)｜⚪妥当｜FAIL_INSEN｜1,938円｜💰19.9万円｜—
- 478A Hutzper Inc.｜changepoint🔔｜⚡好調(7)｜⚪妥当｜FAIL_INSEN｜668円｜💰7.1万円｜—
- 3091 ブロンコビリー｜changepoint🔔🔔｜⚡好調(7)｜🟡やや割高｜FAIL_UWAHIGE｜2,981円｜💰29.6万円｜—
- 8704 トレイダーズホールディングス｜changepoint🔔｜⚡好調(5)｜💎割安｜FAIL_INSEN｜1,275円｜💰13.2万円｜—
- 6284 日精エー・エス・ビー機械｜changepoint🔔｜⚡好調(5)｜🟢値頃｜FAIL_INSEN｜8,280円｜💰85.4万円｜—
- 218A Liberaware｜changepoint🔔｜⚡好調(5)｜⚪妥当｜FAIL_INSEN｜915円｜💰10.1万円｜—
- 6785 鈴木｜changepoint🔔🔔｜✅順調(4)｜⚪妥当｜FAIL_INSEN｜3,270円｜💰34.0万円｜—
- 4498 Cybertrust Japan Co., Ltd.｜changepoint🔔｜✅順調(4)｜🟡やや割高｜FAIL_INSEN｜1,660円｜💰19.2万円｜—
- 593A ティアフォー｜changepoint🔔🔔｜✅順調(4)｜🔴過熱｜FAIL_INSEN｜1,932円｜💰21.1万円｜—
- 4165 PLAID Inc.｜changepoint🔔｜🔻悪化(4)｜🔴過熱｜FAIL_INSEN｜753円｜💰7.7万円｜—
- 4071 Plus Alpha Consulting Co. LTD.｜changepoint🔔｜✅順調(3)｜⚪妥当｜FAIL_INSEN｜2,262円｜💰22.6万円｜—
- 598A チャットプラス｜changepoint🔔🔔｜✅順調(3)｜⚪妥当｜FAIL_INSEN｜1,186円｜💰12.3万円｜—
- 339A PROGRESS TECHNOLOGIES GROUP INC｜changepoint🔔🔔｜➖横ばい(2)｜⚪妥当｜FAIL_INSEN｜819円｜💰8.4万円｜—
- 4488 AI inside Inc.｜changepoint｜➖横ばい(2)｜🟡やや割高｜FAIL_INSEN｜2,000円｜💰21.2万円｜—
- 4259 ExaWizards Inc.｜changepoint🔔｜業績データ取得不可｜⚪妥当｜FAIL_INSEN｜776円｜💰8.1万円｜—
- 3993 PKSHA Technology, Inc.｜changepoint🔔｜業績データ取得不可｜⚪妥当｜FAIL_INSEN｜3,550円｜💰36.4万円｜—

## 🤖AI特需銘柄
波: wave_on なし／25MA 上回り率 📡エネマネ・計量 14%・❄️冷却・空調 25%・🌐光通信 9%・🔬基板・素材 10%
- 3131 シンデンハイテックス｜ai_momentum｜🚀確変(12)｜💎割安｜FAIL_INSEN｜6,760円｜💰73.6万円｜—
- 2760 東京エレクトロンデバイス｜ai_momentum｜🔥絶好調(10)｜⚪妥当｜FAIL_INSEN｜4,500円｜💰49.2万円｜—
- 9824 泉州電業｜ai_momentum｜🔥絶好調(10)｜⚪妥当｜FAIL_INSEN｜7,930円｜💰83.5万円｜—
- 6521 オキサイド｜ai_momentum｜⚡好調(7)｜🟢値頃｜FAIL_INSEN｜3,200円｜💰33.8万円｜—
- 1982 日比谷総合設備｜ai_momentum｜⚠減速(1)｜🔴過熱｜FAIL_INSEN｜3,155円｜💰33.5万円｜—
- 9960 トーテック｜ai_momentum｜⚠減速(1)｜🔴過熱｜FAIL_INSEN｜4,235円｜💰43.2万円｜—
- 4062 IBIDEN CO., LTD.｜ai_reversal｜🔥絶好調(9)｜⚪妥当｜FAIL_INSEN｜9,167円｜💰97.6万円｜—
- 6981 村田製作所｜ai_reversal｜🔥絶好調(9)｜⚪妥当｜FAIL_INSEN｜6,643円｜💰68.0万円｜—
- 7433 伯東｜ai_reversal｜🔥絶好調(9)｜⚪妥当｜FAIL_INSEN｜1,803円｜💰54.1万円｜—
- 6752 パナソニックHD｜ai_reversal｜⚠減速(7)｜⚪妥当｜FAIL_INSEN｜3,878円｜💰39.8万円｜—
- 6779 Nihon Dempa Kogyo Co., Ltd.｜ai_reversal｜⚡好調(7)｜⚪妥当｜FAIL_INSEN｜2,726円｜💰28.9万円｜—
- 6754 アンリツ｜ai_reversal｜⚡好調(7)｜⚪妥当｜FAIL_INSEN｜2,914円｜💰30.3万円｜—
- 4658 日本空調サービス｜ai_reversal｜⚡好調(5)｜⚪妥当｜FAIL_INSEN｜1,545円｜💰15.7万円｜—
- 8098 稲畑産業｜ai_reversal｜✅順調(4)｜🔴過熱｜FAIL_INSEN｜4,415円｜💰44.8万円｜—
- 6643 戸上電機製作所｜ai_reversal｜✅順調(3)｜🟡やや割高｜FAIL_INSEN｜5,100円｜💰53.8万円｜—
- 3103 ユニチカ｜ai_reversal｜🔻悪化(2)｜🟡やや割高｜FAIL_INSEN｜1,280円｜💰13.3万円｜—
- 5302 日本カーボン｜ai_reversal｜➖横ばい(2)｜🔴過熱｜FAIL_INSEN｜4,975円｜💰50.9万円｜—
- 9432 NTT｜ai_reversal｜➖横ばい(2)｜🔴過熱｜PASS｜177円｜💰1.8万円｜reversal 177.1 想定損失幅3.3%。｜📋カルテ窓 11/04(残10営業日)
  > 【業態】国内通信事業最大手。持ち株会社制で地域電話独占。携帯、光回線高シェア。
  > 【いま】終値177円・直近5日+2.19%（材料未確認）
  > 【調子】➖横ばい（2/13）— 質注意
  > 【水準】🔴過熱（1.0/7）— PER14.64倍・PEG—・52週92.0% ／ 💰単元1.8万円
  > 【戦略】当日終値177.1円の指値で反転を取りにいく。SL171.2円（直近5日安値）

## ⚡材料後出し
その日の足は開示前の情報。判定は参考値
- 2930 北の達人コーポレーション｜PASS｜📌機関投資家・アナリスト向け決算説明会を開催いたしました｜15:40
- 5243 note inc.｜FAIL_INSEN｜🏛東京証券取引所プライム市場への市場区分変更申請に向けた準備に関するお知らせ｜15:30
- 6058 VECTOR Inc.｜FAIL_INSEN｜📊2027年２月期　第２四半期決算説明動画配信のお知らせ｜15:30
- 6227 AIMECHATEC Ltd.｜FAIL_INSEN｜📌譲渡制限付株式報酬としての自己株式処分に関するお知らせ｜15:30
- 8708 アイザワ証券グループ｜FAIL_INSEN｜📊2027年３月期第２四半期（中間期）連結決算速報値に関するお知らせ｜15:30

## 📢開示
使用URL: https://kabutan.jp/disclosures/?kubun=&date=20261020&page=1〜21（全21ページ・314行を取得。フォールバックなし）。
- 📊 6058 ベクトル｜2027年２月期　第２四半期決算説明動画配信のお知らせ｜15:30
- 📊 8622 水戸｜2027年３月期第２四半期（中間期）決算速報値に関するお知らせ｜11:30
- 📊 8708 アイザワ証Ｇ｜2027年３月期第２四半期（中間期）連結決算速報値に関するお知らせ｜15:30
- 🏛 4475 ＨＥＮＮＧＥ｜東京証券取引所プライム市場への上場市場区分変更に関するお知らせ｜08:00
- 🏛 5243 ノート｜東京証券取引所プライム市場への市場区分変更申請に向けた準備に関するお知らせ｜15:30
- 📦 4346 ＮＥＸＹＺ．｜三井住友海上とNEXYZ.が業務提携、地域企業の脱炭素および設備導入を支援｜14:30
- 📌 2334 イオレ｜2027年3月期 第2四半期（中間期）決算説明会のお知らせ｜11:00
- 📌 2930 北の達人｜機関投資家・アナリスト向け決算説明会を開催いたしました｜15:40
- 📌 6227 ＡＩメカ｜譲渡制限付株式報酬としての自己株式処分に関するお知らせ｜15:30
- 📌 6432 竹内製作所｜従業員持株会を通じた譲渡制限付株式付与のための第三者割当による自己株式の処分に係る処分価額等の確定に関するお知らせ｜14:30
①-9へ引き渡し3件

## 総当りゲート
### 5手法
- PASS（22）: 2930 北の達人コーポレーション、3391 TSURUHA Holdings, Inc.、3222 United Super Markets Holdings, Inc.、7733 Olympus Corp.、9861 吉野家ホールディングス、8278 Fuji Co., Ltd.、2809 Kewpie Corporation、3148 Create SD Holdings Co., Ltd.、1860 Toda Corporation、7984 Kokuyo Co., Ltd.、9503 Kansai Electric Power Company, Incorporated、6753 Sharp Corporation、8276 HEIWADO CO., LTD.、9948 Arcs Company, Limited、9974 BELC Co., Ltd.、2815 ARIAKE JAPAN Co., Ltd.、8194 Life Corporation、8174 NIPPON GAS Co., Ltd.、3591 WACOAL HOLDINGS CORP、3994 マネーフォワード、4443 Ｓａｎｓａｎ、6532 ベイカレント
- FAIL_UWAHIGE（12）: 212A FIT EASY Inc.、4666 Park24 Co., Ltd.、7458 Daiichikosho Co., Ltd.、2702 日本マクドナルドホールディングス、2782 Seria Co., Ltd.、8198 Maxvalu Tokai Co., Ltd.、5021 Cosmo Energy Holdings Co., Ltd.、1333 Umios Corporation、6183 BELLSYSTEM24 Holdings, Inc.、9533 TOHO GAS Co., Ltd.、7201 Nissan Motor Co., Ltd.、5932 三協立山
- FAIL_INSEN（138）: 6627 Tera Probe, Inc.、5137 Smart Drive Co. Ltd.、6862 Minato Holdings Inc.、4053 Sun Asterisk, Inc.、4434 Serverworks Co., Ltd.、5027 AnyMind Group Inc.、5136 tripla Co.,Ltd.、5757 CK San-Etsu Co., Ltd.、9554 AViC Co. Ltd.、421A Movin' Strategic Career CO.,LTD.、5132 pluszero,Inc.、6298 Y.A.C.HOLDINGS CO.,LTD.、4377 ONE CAREER Inc.、5537 AlbaLink Co.,Ltd.、9556 INTLOOP, Inc.、7047 PORT INC.、3915 TerraSky Co., Ltd.、5821 Hirakawa Hewtech Corp.、4058 Toyokumo, Inc.、6071 IBJ, Inc.、5034 unerry, Inc.、9560 PROGRIT, Inc.、558A SQUEEZE Inc.、7678 ASAKUMA CO.,LTD.、9268 OPTIMUS GROUP Co., Ltd.、4477 BASE, Inc.、9628 San Holdings,Inc.、2980 SRE Holdings Corp.、4412 Science Arts, Inc.、505A Geekly,Inc.、3798 ULS Group Incorporated、5038 eWeLL Co.,Ltd、6629 TECHNO HORIZON Co., Ltd.、6289 Giken Ltd.、3077 Horiifoodservice Co., Ltd.、6918 Aval Data Corporation、3374 Naigai Tec Corporation、7567 Sakae Electronics Corp.、269A SAPEET、6337 Tesec Corporation、3696 セレス、2820 Yamami Co.、4331 Take and Give. Needs Co., Ltd.、7161 Jimoto Holdings, Inc.、2340 Gokurakuyu Holdings Co., Ltd.、3843 Freebit Co., Ltd.、8871 GOLDCREST Co., Ltd.、3186 ネクステージ、6324 Harmonic Drive Systems Inc.、1803 Shimizu Corporation、4023 クレハ、7004 Kanadevia Corporation、2874 YOKOREI CO. LTD.、8522 Bank of Nagoya, Ltd.、8987 Japan Excellent, Inc.、8282 K'S HOLDINGS CORPORATION、8088 IWATANI Corporation、8386 Hyakujushi Bank, Ltd.、9412 SKY Perfect JSAT Corporation、8125 Wakita & Co., Ltd.、7721 Tokyo Keiki Inc.、8381 San-in Godo Bank Ltd.、8954 ORIX JREIT Inc.、8393 Miyazaki Bank Ltd.、3279 Activia Properties, Inc.、3282 Comforia Residential REIT, Inc.、8952 Japan Real Estate Investment Corp.、1861 Kumagai Gumi Co., Ltd.、1417 MIRAIT ONE Corporation、1820 Nishimatsu Construction Co., Ltd.、1952 Shin Nippon Air Technologies Co., Ltd.、6269 Modec, Inc.、7003 Mitsui ES Holdings Co., Ltd.、8584 Jaccs Co., Ltd.、9882 Yellow Hat Ltd.、1944 Kinden Corporation、8066 Mitani Corporation、2659 SAN-A CO., LTD.、2805 S&B Foods Inc.、3289 Tokyu Fudosan Holdings Corp.、8818 Keihanshin Building Co., Ltd.、1719 HAZAMA ANDO Corporation、1833 Okumura Corporation、8953 Japan Metropolitan Fund Investment Corporation、6366 Chiyoda Corp.、5844 Kyoto Financial Group,Inc.、2379 dip Corporation、1893 Penta-Ocean Construction Co., Ltd.、3234 Mori Hills Reit Investment Corporation、3249 Industrial & Infrastructure Fund Investment Corporation、3283 Nippon Prologis REIT, Inc.、3292 AEON REIT Investment Corp.、3296 NIPPON REIT Investment Corp、3309 Sekisui House Reit. Inc.、3462 Nomura Real Estate Master Fund, Inc.、5482 Aichi Steel Corporation、8955 Japan Prime Realty Investment Corporation、8961 MORI TRUST REIT.Inc、8986 Daiwa Securities Living Investment Corporation、1946 Toenec Corporation、5631 Japan Steel Works, Ltd.、4928 Noevir Holdings Co., Ltd.、6960 Fukuda Denshi Co., Ltd.、9436 Okinawa Cellular Telephone Company、1662 Japan Petroleum Exploration Co., Ltd.、6804 Hosiden Corp.、1969 Takasago Thermal Engineering Co., Ltd.、8585 Orient Corporation、9699 NISHIO HOLDINGS CO. LTD.、8253 Credit Saison Co., Ltd.、5831 Shizuoka Financial Group, Inc.、8345 Bank of Iwate Ltd.、3471 Mitsui Fudosan Logistics Park, Inc.、8399 Bank Of The Ryukyus,Limited、7381 CCI Group, Inc.、7384 Procrea Holdings,Inc.、8304 Aozora Bank, Ltd.、8511 Japan Securities Finance Co., Ltd.、7624 NaITO、5018 ＭＯＲＥＳＣＯ、6668 ＡＤプラズマ、7713 シグマ光機、5246 ELEMENTS,Inc.、3498 霞ヶ関Ｃ、7811 Nakamoto Packs Co. Ltd.、6814 古野電、3479 ティーケーピー、6505 東洋電機製造、4176 ココナラ、9211 f-code Inc.、2334 Eole, Inc.、4431 スマレジ、5590 NETSTARS Co.,Ltd.、4493 Cyber Security Cloud, Inc.、4419 Ｆｉｎａｔｅｘｔホールディングス、6492 Okano Valve Mfg. Co., Ltd.、6395 TADANO Ltd.、8370 Kiyo Bank, Ltd.
### グランビル
- PASS（11）: 4544 H.U.Group Holdings, Inc.、4507 Shionogi & Co., Ltd.、2331 ALSOK CO., LTD.、9828 Genki Global Dining Concepts Corp、2002 日清製粉グループ本社、7616 Colowide Co., Ltd.、3097 Monogatari Corporation、7630 Ichibanya Co., Ltd.、9900 Sagami Holdings Corp.、5242 EYEZ INC.、8163 SRS HOLDINGS CO.,LTD.
- FAIL_UWAHIGE（14）: 9006 京浜急行電鉄、7744 Noritsu Koki Co., Ltd.、9064 ヤマトホールディングス、2288 Marudai Food Co., Ltd.、6988 日東電工、8850 スターツコーポレーション、2413 エムスリー、5071 VIS Co., Ltd.、2871 ニチレイ、2767 円谷フィールズホールディングス、9505 Hokuriku Electric Power Company、8255 Axial Retailing, Inc.、8097 SAN-AI OBBLI CO. LTD、8995 Makoto Construction Co,Ltd
- FAIL_INSEN（143）: 5254 Arent, Inc.、8944 Land Business Co., Ltd.、7725 INTER ACTION Corporation、9553 MicroAd, Inc.、6905 Cosel Co., Ltd.、2986 LA Holdings Co.,Ltd、6562 Geniee, Inc.、1945 Tokyo Energy & Systems Inc.、6473 JTEKT Corporation、8697 Japan Exchange Group, Inc.、6255 NPC Incorporated、8095 Astena Holdings Co.,Ltd.、8793 ＮＥＣキャピタルソリューション、3496 AZOOM CO.,LTD、3741 Systems Engineering Consultants Co., Ltd.、6302 Sumitomo Heavy Industries, Ltd.、5838 Rakuten Bank, Ltd.、4763 クリーク・アンド・リバー社、6470 Taiho Kogyo Co., Ltd.、7199 Premium Group Co., Ltd.、3064 MonotaRO Co., Ltd.、3935 Edia Co. Ltd.、6196 Strike Group Co. Ltd.、3562 No.1 Co., Ltd.、8061 Seika Corporation、9048 名古屋鉄道、3661 m-up holdings, Inc.、6432 Takeuchi Mfg.Co., Ltd.、7970 Shin-Etsu Polymer Co., Ltd.、8020 Kanematsu Corporation、6454 Max Co., Ltd.、5036 Japan Business Systems, Inc.、8014 Chori Co., Ltd.、6371 Tsubakimoto Chain Co.、6592 Mabuchi Motor Co., Ltd.、8060 キヤノンマーケティングジャパン、4166 Cacco, Inc.、3433 TOCALO Co., Ltd.、8927 Meiho Enterprise Co., Ltd.、186A Astroscale Holdings Inc.、4183 Mitsui Chemicals, Inc.、4272 Nippon Kayaku Co., Ltd.、4956 Konishi Co., Ltd.、5461 Chubu Steel Plate Co., Ltd.、7181 JAPAN POST INSURANCE Co., Ltd.、7734 Riken Keiki Co., Ltd.、7513 Kojima Co., Ltd.、6328 Ebara Jitsugyo Co., Ltd.、6208 Ishikawa Seisakusho,Ltd.、4617 Chugoku Marine Paints,Ltd.、7751 キヤノン、8081 Kanaden Corporation、6770 Alps Alpine Co., Ltd.、1815 鉄建建設、4375 Safie Inc.、8424 芙蓉総合リース、4549 Eiken Chemical Co., Ltd.、4552 JCR Pharmaceuticals Co., Ltd.、4937 Ｇ−ＷＡＱＯＯ、276A CCReB Advisors Inc.、3083 Star seeds Co.,Ltd.、290A ＳＹＮＳＰＥＣＴＩＶＥ、5243 note inc.、7806 MTG Co., Ltd.、6834 Seikoh Giken Co., Ltd.、8336 Musashino Bank, Ltd.、8008 Yondoshi Holdings, Inc.、4180 ＡＰＰＩＥＲ　ＧＲＯＵＰ、8346 Toho Bank, Ltd.、7856 HAGIHARA INDUSTRIES INC.、1879 新日本建設、6736 Suncorporation、6523 PHC Holdings Corp.、4667 Aisan Technology Co., Ltd.、6023 ダイハツインフィニアース、7609 Daitron Co., Ltd.、6227 AIMECHATEC Ltd.、2602 日清オイリオグループ、4413 baudroie,inc.、8919 カチタス、8714 Senshu Ikeda Holdings,Inc.、7350 Okinawa Financial Group, Inc.、6058 VECTOR Inc.、4475 HENNGE K.K.、4373 Simplex Holdings,Inc.、6998 Nippon Tungsten Co., Ltd.、5208 Arisawa Mfg.Co., Ltd.、5985 SUNCALL CORPORATION、1518 三井松島ホールディングス、6379 RAIZNEXT Corporation、9044 NANKAI Co., Ltd.、3107 ダイワボウホールディングス、4044 Central Glass Co., Ltd.、4208 UBE Corporation、456A Human Made Inc.、7504 Kohsoku Corporation、9509 Hokkaido Electric Power Company,Incorporated、6072 Jibannet Holdings Co., Ltd.、8043 Starzen Company Limited、9616 共立メンテナンス、3048 ビックカメラ、8059 Daiichi Jitsugyo Co., Ltd.、9166 GENDA Inc.、8343 Akita Bank, Ltd.、8361 Ogaki Kyoritsu Bank, Ltd.、336A ダイナミックマッププラットフォーム、8367 Nanto Bank Ltd.、4565 Nxera Pharma Co., Ltd.、6027 Bengo4.com, Inc.、8362 Fukui Bank, Ltd.、8410 Seven Bank, Ltd.、8622 Mito Securities Co., Ltd.、8624 Ichiyoshi Securities Co., Ltd.、8628 松井証券、8708 アイザワ証券グループ、6769 Thine Electronics, Inc.、2122 インタースペース、6963 ROHM Company Limited、2354 YE DIGITAL CORPORATION、6597 HPC SYSTEMS Inc.、3687 Fixstars Corp.、5574 ABEJA,Inc.、4997 日本農薬、1407 West Holdings Corporation、4346 NEXYZ.Group Corporation、7354 Direct Marketing MiX Inc.、2681 2nd RETAILING Co., Ltd.、4082 第一稀元素化学工業、3653 Morpho, Inc.、3907 Silicon Studio Corp.、4440 WITZ Corp.、4691 Washington Hotel Corp.、6203 Howa Machinery, Ltd.、6522 アスタリスク、8360 Yamanashi Chuo Bank, Ltd.、3778 SAKURA Internet Inc.、8368 Hyakugo Bank, Ltd.、8713 Fidea Holdings Co.Ltd.、3691 DIGITAL PLUS, Inc.、6645 OMRON Corporation、6890 Ferrotec Corporation、8524 North Pacific Bank, Ltd.、4418 Japan Data Science Consortium Co Ltd.
### 変化点
- FAIL_UWAHIGE（3）: 7695 交換できるくん、4382 HEROZ, Inc.、3091 ブロンコビリー
- FAIL_INSEN（28）: 5803 フジクラ、4011 Headwaters Co.,Ltd、6254 野村マイクロ・サイエンス、4187 大阪有機化学工業、6080 Ｍ＆Ａキャピタルパートナーズ、584A LiNKX, Inc.、6136 OSG CORP、6857 アドバンテスト、8151 東陽テクニカ、9962 ミスミグループ本社、7318 セレンディップ・ホールディングス、9888 UEX LTD、4368 4368、5582 （名称取得不可）、478A Hutzper Inc.、8704 トレイダーズホールディングス、6284 日精エー・エス・ビー機械、218A Liberaware、6785 鈴木、4498 Cybertrust Japan Co., Ltd.、593A ティアフォー、4165 PLAID Inc.、4071 Plus Alpha Consulting Co. LTD.、598A チャットプラス、339A PROGRESS TECHNOLOGIES GROUP INC、4488 AI inside Inc.、4259 ExaWizards Inc.、3993 PKSHA Technology, Inc.
### AI特需
- PASS（1）: 9432 NTT
- FAIL_INSEN（17）: 3131 シンデンハイテックス、2760 東京エレクトロンデバイス、9824 泉州電業、6521 オキサイド、1982 日比谷総合設備、9960 トーテック、4062 IBIDEN CO., LTD.、6981 村田製作所、7433 伯東、6752 パナソニックHD、6779 Nihon Dempa Kogyo Co., Ltd.、6754 アンリツ、4658 日本空調サービス、8098 稲畑産業、6643 戸上電機製作所、3103 ユニチカ、5302 日本カーボン
**除籍（SBIグループ登録解除候補）**: なし

## 機械詳細
- 検知内訳: 評価389（プール385＋前夜提案のみ4）・本夜指名98（新規20）・除籍0・SKIP0・未マージPR由来0件
- log追記: base_day=2026-10-20 を置換/追記（最新30営業日保持）。recalc_queue 追加3件
- 抜粋規則: 通知の通過10件の群別内訳は通知に記載。PASS群別 method22/ai1/granville11/changepoint0
- gate_history: gate_history/2026-10-20.json を新規作成（verdicts389件・nominations98件）
- grades.json: 887銘柄/445KB（nx 付与719件）
- method_score: 保持59件／null330件
- ヘッドライン付与: 34/34件（PASS全件）
- kabutan新規取得: 銘柄トップ29/50件（優先①②2件＋業種埋め戻し27件）／決算ページ37件（PASS＋保有）
- profile_cache: 総数862・本夜 業態追加2件・業種 付与済み861／未付与1（本夜追加29件）・業態「未取得」のまま出た件数0
- earnings_log: 総数70／本夜追記3件／リターンを埋めた9件／日足が取れず埋められなかった20件
- gyoseki_cache: 再計算0件（history退避0件）・next_earnings 更新17件
- pool_bars.json: 391銘柄/330KB
- 鮮度ゲート: 鮮度切れ除外7件・nom_age分布 0-2:167/3-10:166/11+:56・last_seen欠損0件
- 記録の凍結: verdicts389件（評価389件と一致）／nominations98件（新規20・再指名78）
- トレンド文脈: ctx 合致85／不一致165／レンジ138／判定不能1・PASSのうち合致5件・形態が付いた銘柄186件
- 3日ルール: 判定4銘柄（件数のみ公開。詳細は通知）
- 業種別PER中央値: 算出できた業種25／母数不足9・spm を写せた銘柄821件
- 開示の分類別件数: 📢0/📉0/📊3/🔁0/👥0/🏛2/📦1/📌4
- 熟成由来の候補: 0件（うちPASS0）
- 権利情報: rights_cache 総数308・本夜 配当更新15件／優待取得0件（優待ページが403で取得不可）・不明のまま308件
- 次回決算日: 付与725件／未発表170件・前年同期発表日 付与115件・earnings_calendar.json 895銘柄/86KB
- STEP 4.8 週末ブリーフ: week_open=false のためスキップ
- 3日ルール・保有判定: 件数のみ公開（詳細は通知）
