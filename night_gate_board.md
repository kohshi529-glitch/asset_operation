# 夜間ゲート 2026-10-27

## サマリー
- 評価数: 459 / PASS: 110（PASS_DOJI 3件を含む）
- 発注可能提案数: 78件
- 市場一言: 市場モード「堅調」（market.latest 2026-10-27）。半導体主導リスクオン（SOX急反発＋先物高／原油は100ドル台で高止まり）。プール459銘柄中PASS比率24.0%（陰線FAIL 242件・上髭FAIL 107件）
- 実行モード: 通常（base_day=当日の引け値を対象）
- base_day: 2026-10-27（run_at 2026-10-27 20:55起動）
- week_open: false（翌営業日 10/28(水)）→ STEP 4.8 週末ブリーフはスキップ
- 📆 翌営業日 10/28: 権利付き最終日（10月・参考）, FOMC 2日目（結果は日本時間の翌早朝）。T+2 10/29: 権利落ち日（10月・参考）, FOMC明け。次の TOPIX 低減日 10/30 第1回/8（あと3営業日）
- 📑指数: 低減対象 提案11件／PASS14件／プール71件・新規採用 16件（index_flags 2026-10-07 公表分）

## 検証結果
- V1 → はい（proposals78=results78=template78・board模擬78行）
- V2 → はい（PASS110=提案78+除外32・order_status欠落0）
- V3 → はい（results459件重複0）
- V4 → はい（既存 valuation static 変更0）
- V5 → はい（許可キー外の変更0・night_gate変更キー['pool', 'results', 'log', 'recalc_queue']・pipeline.runs変更['night_gate']・外部トップキー変更[]）
- V6 → はい（gyoseki grade絵文字整合 不整合0）
- V7 → はい（必須セクション存在（week_open=false のため今週のカタリスト対象外））
- V8 → はい（模擬78行の書式 不正0）
- V9 → はい（gate_history/2026-10-27.json 新規作成・today一致）
- V10 → はい（base_day 4箇所一致 2026-10-27）
- V11 → いいえ（+10153/-8489（indent=2・往復一致）＝results全置換＋キャッシュ更新のため5,000行を超過（全体再フォーマットではない：総行数147k・往復一致で同indent）））
- V12 → はい（proposals/template/results 同順（厳密ソート一致））
- V13 → はい（948銘柄/534.4KiB（600KiB以下: True）・18キー欠落0・nx不一致0・ix非null197・spm検算True）
- V14 → はい（method_score 保持55件/null404件・出所不明0・写し違い0）
- V15 → はい（PASS110件中110件に付与・欠落0・(c)違反0（[]））
- V16 → はい（earnings_log総数86・本夜追記6・📊6件すべて記録・history<=4）
- V17 → はい（460銘柄/394.4KiB・保有3銘柄すべて収録・3日ルール判定3銘柄）
- V18 → はい（鮮度ゲート整合（鮮度切れ15件・誤除外0・誤提案0））
- V19 → はい（verdicts459件=評価459件・nominations85件（新規10/再指名75）・ctx {'不一致': 198, '合致': 128, 'レンジ': 129, '判定不能': 3}・profile既存変更0）
- V20 → はい（948銘柄・nx非null759・hist持ち395・pxd280（aTrue/bTrue/cTrue/dTrue/eTrue））
- VLEAK → はい（公開物への保有情報 検出0件）

## 保有アラート
保有3銘柄・アラート8件（詳細は通知）

## 前夜の結果
PL5口座への正式な反映は週次①-11の採点で行われる。ここは参考情報。
前夜2026-10-26の提案88件 → 約定61・不約定27・判定不能0
- 5027 momentum 指定778 → 約定778・終値779（+0.13%）
- 421A momentum 指定4,050 → 約定4,050・終値3,970（-1.98%）
- 4058 momentum 指定2,290 → 約定2,290・終値2,251（-1.70%）
- 7678 momentum 指定3,880 → 約定3,880・終値3,950（+1.80%）
- 505A momentum 指定1,159 → 約定1,159・終値1,169（+0.86%）
- 7567 momentum 指定635 → 約定635・終値644（+1.42%）
- 3222 reversal 指定781 → 約定773・終値767（-0.78%）
- 4088 reversal 指定2,756 → 約定2,756・終値2,762（+0.22%）
- 7733 reversal 指定1,751.5 → 約定1,745.5・終値1,750（+0.26%）
- 8987 reversal 指定126,500 → 約定126,500・終値126,400（-0.08%）
- 8125 reversal 指定1,875 → 約定1,874・終値1,871（-0.16%）
- 8278 reversal 指定2,026 → 約定2,010・終値2,004（-0.30%）
- 2782 reversal 指定4,395 → 約定4,395・終値4,395（+0.00%）
- 4666 reversal 指定1,850 → 約定1,821・終値1,831（+0.55%）
- 3282 reversal 指定90,500 → 約定90,500・終値89,900（-0.66%）
- 1861 reversal 指定1,245 → 約定1,244・終値1,246（+0.16%）
- 1417 reversal 指定3,377 → 約定3,377・終値3,409（+0.95%）
- 8198 reversal 指定3,185 → 約定3,185・終値3,120（-2.04%）
- 1820 reversal 指定5,416 → 約定5,416・終値5,386（-0.55%）
- 3148 reversal 指定3,260 → 約定3,260・終値3,220（-1.23%）
- 6269 reversal 指定8,130 → 約定8,130・終値8,115（-0.18%）
- 1860 reversal 指定1,460.5 → 約定1,460.5・終値1,470.5（+0.68%）
- 2659 reversal 指定3,220 → 約定3,210・終値3,220（+0.31%）
- 2805 reversal 指定6,850 → 約定6,850・終値6,830（-0.29%）
- 1719 reversal 指定1,795 → 約定1,791・終値1,789（-0.11%）
- 1833 reversal 指定5,350 → 約定5,350・終値5,350（+0.00%）
- 2379 reversal 指定1,499 → 約定1,499・終値1,513（+0.93%）
- 1893 reversal 指定1,353.5 → 約定1,353.5・終値1,382（+2.11%）
- 8276 reversal 指定2,626 → 約定2,618・終値2,615（-0.11%）
- 9974 reversal 指定6,450 → 約定6,450・終値6,370（-1.24%）
- 3296 reversal 指定76,000 → 約定76,000・終値75,700（-0.39%）
- 3462 reversal 指定128,700 → 約定128,700・終値128,600（-0.08%）
- 8954 reversal 指定89,800 → 約定89,800・終値88,900（-1.00%）
- 8986 reversal 指定83,900 → 約定83,900・終値83,400（-0.60%）
- 1946 reversal 指定2,085 → 約定2,085・終値2,111（+1.25%）
- 6183 reversal 指定1,404 → 約定1,391・終値1,353（-2.73%）
- 9948 reversal 指定3,545 → 約定3,545・終値3,510（-0.99%）
- 6960 reversal 指定10,940 → 約定10,940・終値11,020（+0.73%）
- 9533 reversal 指定1,225.5 → 約定1,217.5・終値1,221.5（+0.33%）
- 8174 reversal 指定949.9000244140625 → 約定944.7999877929688・終値951.7000122070312（+0.73%）
- 8600 reversal 指定1,021 → 約定1,021・終値1,038（+1.67%）
- 8098 reversal 指定4,510 → 約定4,495・終値4,505（+0.22%）
- 8944 momentum 指定256 → 約定256・終値252（-1.56%）
- 9553 momentum 指定574 → 約定574・終値577（+0.52%）
- 8095 momentum 指定534 → 約定538・終値535（-0.56%）
- 8061 momentum 指定2,930 → 約定2,950・終値2,977（+0.92%）
- 6371 momentum 指定2,712 → 約定2,712・終値2,708（-0.15%）
- 4272 momentum 指定2,052.5 → 約定2,052.5・終値2,058.5（+0.29%）
- 8012 momentum 指定1,195 → 約定1,200.5・終値1,217（+1.37%）
- 7630 oshime 指定1,075.8 → 約定1,075・終値1,067（-0.74%）
- 1436 reversal 指定1,509 → 約定1,509・終値1,493（-1.06%）
- 5574 reversal 指定2,346 → 約定2,346・終値2,363（+0.72%）
- 4440 reversal 指定1,817 → 約定1,777・終値1,804（+1.52%）
- 6203 reversal 指定2,279 → 約定2,179・終値2,278（+4.54%）
- 3778 reversal 指定2,927 → 約定2,927・終値2,967（+1.37%）
- 7175 reversal 指定1,682 → 約定1,682・終値1,695（+0.77%）
- 584A changepoint 指定2,283 → 約定2,283・終値2,308（+1.10%）
- 5582 changepoint 指定1,809 → 約定1,809・終値1,810（+0.06%）
- 4071 changepoint 指定2,338 → 約定2,315・終値2,307（-0.35%）
- 339A changepoint 指定813 → 約定813・終値810（-0.37%）
- 593A changepoint 指定2,190 → 約定2,190・終値2,239（+2.24%）

## 模擬テンプレ
```
# base_day 2026-10-27 ／ 提案78件
# 使い方: 参戦する0〜3銘柄の行だけをコピーし、｜の後ろに参戦理由を書いてポジション株PJへ送る。
# 選ばなかった行は送らなくてよい（全行に理由を書く必要はない）。見送りは末尾の1行で足りる。
# 特定銘柄を理由つきで見送る場合のみ『模擬 見送り {code} ｜{理由}』を送る。
模擬 276A kenmo_momentum 逆指値4655 SL4371 単元100 ｜
模擬 4434 kenmo_momentum 逆指値3070 SL2881.1 単元100 ｜
模擬 212A kenmo_momentum 逆指値2771 SL2603.8 単元100 ｜
模擬 3915 kenmo_momentum 逆指値2391 SL2246.6 単元100 ｜
模擬 505A kenmo_momentum 逆指値1171 SL1099.8 単元100 ｜
模擬 618A kenmo_momentum 逆指値2138 SL2008.8 単元100 ｜
模擬 2930 kenmo_newhigh 逆指値149 SL139.1 単元100 ｜
模擬 6875 choruko_reversal 指値9940 SL9110 単元100 ｜
模擬 8336 choruko_reversal 指値2565 SL2365 単元100 ｜
模擬 3036 choruko_reversal 指値3120 SL2893 単元100 ｜
模擬 6324 choruko_reversal 指値5340 SL4530 単元100 ｜
模擬 8346 choruko_reversal 指値957 SL871 単元100 ｜
模擬 5301 choruko_reversal 指値1933.5 SL1788 単元100 ｜
模擬 7004 choruko_reversal 指値1053 SL1001 単元100 ｜
模擬 8088 choruko_reversal 指値1928 SL1836.5 単元100 ｜
模擬 8714 choruko_reversal 指値948 SL886 単元100 ｜
模擬 8399 choruko_reversal 指値2835 SL2580 単元100 ｜
模擬 268A choruko_reversal 指値1485 SL1298 単元100 ｜
模擬 8381 choruko_reversal 指値2076 SL1955 単元100 ｜
模擬 8524 choruko_reversal 指値1176 SL1048 単元100 ｜
模擬 1861 choruko_reversal 指値1246 SL1193 単元100 ｜
模擬 1417 choruko_reversal 指値3409 SL3274 単元100 ｜
模擬 1860 choruko_reversal 指値1470.5 SL1402 単元100 ｜
模擬 2659 choruko_reversal 指値3220 SL3095 単元100 ｜
模擬 5021 choruko_reversal 指値4370 SL4180 単元100 ｜
模擬 1893 choruko_reversal 指値1382 SL1296.5 単元100 ｜
模擬 1963 choruko_reversal 指値2137.5 SL1974 単元100 ｜
模擬 1969 choruko_reversal 指値4155 SL3996 単元100 ｜
模擬 9699 choruko_reversal 指値4305 SL4200 単元100 ｜
模擬 9533 choruko_reversal 指値1221.5 SL1183.5 単元100 ｜
模擬 8370 choruko_reversal 指値1566 SL1456 単元100 ｜
模擬 5831 choruko_reversal 指値3030 SL2766.5 単元100 ｜
模擬 7381 choruko_reversal 指値1115 SL1032 単元100 ｜
模擬 8345 choruko_reversal 指値2116 SL1897 単元100 ｜
模擬 8367 choruko_reversal 指値1762 SL1635 単元100 ｜
模擬 7384 choruko_reversal 指値4075 SL3615 単元100 ｜
模擬 8174 choruko_reversal 指値951.7 SL920 単元100 ｜
模擬 8334 choruko_reversal 指値2575 SL2376 単元100 ｜
模擬 8366 choruko_reversal 指値2550 SL2370 単元100 ｜
模擬 6471 choruko_reversal 指値1008 SL955.6 単元100 ｜
模擬 7186 choruko_reversal 指値1660 SL1552.5 単元100 ｜
模擬 7322 choruko_reversal 指値1838 SL1687 単元100 ｜
模擬 8354 choruko_reversal 指値6880 SL6403 単元100 ｜
模擬 8359 choruko_reversal 指値2403 SL2236 単元100 ｜
模擬 8600 choruko_reversal 指値1038 SL969 単元100 ｜
模擬 6521 ai_momentum 逆指値3235 SL3036.2 単元100 ｜
模擬 4658 ai_reversal 指値1545 SL1528 単元100 ｜
模擬 5254 granville_tenkan 逆指値3880 SL3642.5 単元100 ｜
模擬 3927 granville_tenkan 逆指値1076 SL1010.5 単元100 ｜
模擬 9553 granville_tenkan 逆指値580 SL544.3 単元100 ｜
模擬 3496 granville_tenkan 逆指値4810 SL4516.7 単元100 ｜
模擬 6255 granville_tenkan 逆指値659 SL618.5 単元100 ｜
模擬 7744 granville_tenkan 逆指値2152 SL2021.9 単元100 ｜
模擬 186A granville_tenkan 逆指値1084 SL1018 単元100 ｜
模擬 4272 granville_tenkan 逆指値2065 SL1940.2 単元100 ｜
模擬 8012 granville_tenkan 逆指値1220 SL1145.9 単元100 ｜
模擬 4617 granville_tenkan 逆指値3595 SL3374.6 単元100 ｜
模擬 6328 granville_tenkan 逆指値2477 SL2327.4 単元100 ｜
模擬 4902 granville_tenkan 逆指値691.6 SL649.2 単元100 ｜
模擬 5105 granville_tenkan 逆指値4064 SL3815.5 単元100 ｜
模擬 4180 granville_oshime 指値1418.3 SL1411.2 単元100 🔒 ｜
模擬 4431 granville_oshime 指値3690.6 SL3672.2 単元100 ｜
模擬 456A granville_oshime 指値1940 SL1930.4 単元100 ｜
模擬 6963 granville_rebound 指値3700 SL3486 単元100 ｜
模擬 8364 granville_rebound 指値2724 SL2458 単元100 ｜
模擬 6490 granville_rebound 指値10020 SL9330 単元100 ｜
模擬 3907 granville_rebound 指値1369 SL1265 単元100 ｜
模擬 8360 granville_rebound 指値1279 SL1132 単元100 ｜
模擬 7380 granville_rebound 指値2358 SL2156 単元100 ｜
模擬 8368 granville_rebound 指値2089 SL1902 単元100 ｜
模擬 8713 granville_rebound 指値2527 SL2265 単元100 ｜
模擬 8377 granville_rebound 指値737.7 SL662.5 単元100 ｜
模擬 584A 変化点🔔 指値2308 SL2072 単元100 🔒 ｜
模擬 8151 変化点🔔 指値1924 SL1868 単元100 🔒 ｜
模擬 5590 変化点🔔 指値656 SL632 単元100 ｜
模擬 6284 変化点🔔 指値8010 SL7750 単元100 🔒 ｜
模擬 6785 変化点🔔🔔 指値3240 SL3035 単元100 🔒 ｜
模擬 4478 変化点🔔 指値4175 SL3835 単元100 🔒 ｜
模擬 見送り ｜
```

## PASS内訳
PASS 110件 = 発注可能 78件 + 除外 32件（型不一致11/材料後出し2/鮮度切れ15/その他4）
- 5027 AnyMind Group Inc.｜⛔提案なし(材料後出し)
- 5246 ＥＬＥＭＥＮＴＳ｜⛔提案なし(手法ブランチ不明)
- 4443 Ｓａｎｓａｎ｜⛔提案なし(手法ブランチ不明)
- 6814 古野電｜⛔提案なし(手法ブランチ不明)
- 3562 No.1 Co., Ltd.｜⛔提案なし(材料後出し)
- 6023 ダイハツインフィニアース｜⛔型不一致: 既に支持帯以下
- 3106 倉敷紡績｜⛔型不一致: 既に支持帯以下
- 7350 Okinawa Financial Group, Inc.｜⛔型不一致: 既に支持帯以下
- 6998 Nippon Tungsten Co., Ltd.｜⛔型不一致: 既に支持帯以下
- 5985 SUNCALL CORPORATION｜⛔型不一致: 既に支持帯以下
- 4044 Central Glass Co., Ltd.｜⛔型不一致: 既に支持帯以下
- 9509 Hokkaido Electric Power Company,Incorporated｜⛔型不一致: 既に支持帯以下
- 9505 Hokuriku Electric Power Company｜⛔型不一致: 既に支持帯以下
- 8361 Ogaki Kyoritsu Bank, Ltd.｜⛔型不一致: 既に支持帯以下
- 6027 弁護士ドットコム｜⛔型不一致: 既に支持帯以下
- 8362 Fukui Bank, Ltd.｜⛔型不一致: 既に支持帯以下
- 278A Ｔｅｒｒａ　Ｄｒｏｎｅ｜⛔提案なし(単元株数不明でリスク計算不可)
- 鮮度切れ: 9268(nom_age 17)、7161(nom_age 13)、1803(nom_age 12)、2874(nom_age 12)、8953(nom_age 11)、3741(nom_age 14)、8020(nom_age 12)、7181(nom_age 17)、290A(nom_age 16)、2767(nom_age 11)、4475(nom_age 12)、3107(nom_age 15)、7504(nom_age 20)、8343(nom_age 12)、4346(nom_age 16)

## 5手法銘柄
- 6627 Tera Probe, Inc.｜kenmo_momentum｜🚀確変｜💎割安｜FAIL_UWAHIGE｜1,824円｜💰17.5万円｜—｜📋カルテ窓 11/13(残12営業日)
- 276A CCReB Advisors Inc.｜granville_oshime/kenmo_momentum｜🚀確変｜⚪妥当｜PASS｜4,595円｜💰46.0万円｜momentum 4,655（✅即時可）｜⚠日程不明
  > 【業態】AIを活用した企業不動産(CRE)に関するソリューションの提供などを手掛ける。
  > 【いま】終値4,595円・直近5日+21.56%（材料未確認）
  > 【調子】🚀確変（12/13）
  > 【水準】⚪妥当（4.0/7）— PER16.90倍・PEG0.1894・52週68.1% ／ 💰単元46.0万円
  > 【戦略】当日高値超えの逆指値4,655円で順張り参戦を検討。上限4,701.6円・SL4,371円目安
- 6862 ミナトホールディングス｜kenmo_momentum/granville_rebound/granville_oshime｜🚀確変｜💎割安｜FAIL_UWAHIGE｜4,400円｜💰40.5万円｜—｜📋カルテ窓 11/12(残11営業日)｜⚡材料後出し
- 3556 RenetJapanGroup, Inc.｜kenmo_momentum｜🚀確変｜⚪妥当｜FAIL_INSEN｜897円｜💰10.1万円｜—｜📋カルテ窓 11/13(残12営業日)
- 4053 Sun Asterisk, Inc.｜kenmo_momentum｜🚀確変｜⚪妥当｜FAIL_INSEN｜592円｜💰6.0万円｜—｜📋カルテ窓 11/13(残12営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 4434 Serverworks Co., Ltd.｜kenmo_momentum/stf_kakuhen｜🚀確変｜⚪妥当｜PASS｜3,035円｜💰30.4万円｜momentum 3,070（✅即時可）｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）
  > 【業態】アマゾンのクラウド「AWS」に特化。インフラ基盤構築、リセール、保守・運用代行。
  > 【いま】終値3,035円・直近5日+0.50%（材料未確認）
  > 【調子】🚀確変（11/13）
  > 【水準】⚪妥当（3.0/7）— PER14.68倍・PEG0.1036・52週83.5% ／ 💰単元30.4万円
  > 【戦略】当日高値超えの逆指値3,070円で順張り参戦を検討。上限3,100.7円・SL2,881.1円目安
- 5027 AnyMind Group Inc.｜kenmo_momentum｜🚀確変｜⚪妥当｜PASS｜779円｜💰7.8万円｜⛔提案なし(材料後出し)｜📋カルテ窓 11/13(残12営業日)｜⚡材料後出し
  > 【業態】ブランド企業向けマーケティング支援やクリエイター向け収益化支援。海外売上が大。
  > 【いま】終値779円・直近5日+1.70%・📌AnyMind Group and Meta partner to connect social discovery with live commerce
  > 【調子】🚀確変（11/13）
  > 【水準】⚪妥当（3.0/7）— PER28.33倍・PEG0.3625・52週84.0% ／ 💰単元7.8万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 5136 tripla Co.,Ltd.｜kenmo_momentum/changepoint🔔🔔/granville_oshime｜🚀確変｜⚪妥当｜FAIL_INSEN｜2,519円｜💰26.2万円｜—｜⚠日程不明
- 5757 CK San-Etsu Co., Ltd.｜kenmo_momentum｜🔥絶好調｜💎割安｜FAIL_INSEN｜4,505円｜💰45.2万円｜—｜📋カルテ窓 11/13(残12営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 9554 AViC Co. Ltd.｜kenmo_momentum/granville_tenkan｜🔥絶好調｜💎割安｜FAIL_UWAHIGE｜1,553円｜💰15.6万円｜—｜📋カルテ窓 11/13(残12営業日)
- 212A FIT EASY Inc.｜kenmo_momentum/granville_oshime｜🔥絶好調｜⚪妥当｜PASS｜2,770円｜💰27.7万円｜momentum 2,771（✅即時可）｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）
  > 【業態】サービス業（フィットネスクラブ・アミューズメント・スポーツ関連）
  > 【いま】終値2,770円・直近5日-3.72%（材料未確認）
  > 【調子】🔥絶好調（10/13） — 上方修正済み
  > 【水準】⚪妥当（4.0/7）— PER18.70倍・PEG0.3496・52週62.8% ／ 💰単元27.7万円
  > 【戦略】当日高値超えの逆指値2,771円で順張り参戦を検討。上限2,798.7円・SL2,603.8円目安
- 3915 TerraSky Co., Ltd.｜kenmo_momentum｜🔥絶好調｜⚪妥当｜PASS｜2,390円｜💰23.9万円｜momentum 2,391（✅即時可）｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）｜📐進捗 上振れ 34.1%
  > 【業態】クラウドシステムの導入支援や開発。セールスフォースと提携。大企業、AWS向け拡大。
  > 【いま】終値2,390円・直近5日+0.00%（材料未確認）
  > 【調子】🔥絶好調（10/13）
  > 【水準】⚪妥当（4.0/7）— PER20.22倍・PEG0.3876・52週40.3% ／ 💰単元23.9万円
  > 【戦略】当日高値超えの逆指値2,391円で順張り参戦を検討。上限2,414.9円・SL2,246.6円目安
- 421A Movin' Strategic Career CO.,LTD.｜kenmo_momentum/kenmo_newhigh｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜3,970円｜💰40.2万円｜—｜📋カルテ窓 11/11(残10営業日)
- 6298 Y.A.C.HOLDINGS CO.,LTD.｜kenmo_momentum｜🔥絶好調｜💎割安｜FAIL_INSEN｜1,110円｜💰10.9万円｜—｜📋カルテ窓 11/13(残12営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 5132 pluszero,Inc.｜kenmo_momentum｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜1,855円｜💰18.1万円｜—｜⚠日程不明
- 4377 ONE CAREER Inc.｜kenmo_momentum｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜2,478円｜💰25.5万円｜—｜📋カルテ窓 11/12(残11営業日)
- 5537 AlbaLink Co.,Ltd.｜kenmo_momentum/granville_oshime｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜3,460円｜💰36.8万円｜—｜📋カルテ窓 11/12(残11営業日)
- 7047 PORT INC.｜kenmo_momentum｜🔥絶好調｜💎割安｜FAIL_INSEN｜1,954円｜💰20.1万円｜—｜📋カルテ窓 11/16(残13営業日)
- 5821 Hirakawa Hewtech Corp.｜kenmo_momentum｜⚡好調｜💎割安｜FAIL_UWAHIGE｜3,145円｜💰31.0万円｜—｜⏰決算 11/04(残5営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 4058 Toyokumo, Inc.｜kenmo_momentum｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,251円｜💰22.8万円｜—｜📋カルテ窓 11/13(残12営業日)
- 6071 IBJ, Inc.｜kenmo_momentum｜⚡好調｜⚪妥当｜FAIL_INSEN｜913円｜💰9.2万円｜—｜📋カルテ窓 11/13(残12営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 147A SORACOM,INC.｜kenmo_momentum｜⚡好調｜⚪妥当｜FAIL_INSEN｜925円｜💰9.3万円｜—｜📋カルテ窓 11/11(残10営業日)
- 5034 unerry, Inc.｜kenmo_momentum｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜2,744円｜💰27.2万円｜—｜📋カルテ窓 11/12(残11営業日)｜⚡材料後出し
- 9560 PROGRIT, Inc.｜kenmo_momentum｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜1,085円｜💰11.1万円｜—｜⚠日程不明
- 7678 ASAKUMA CO.,LTD.｜kenmo_momentum/kenmo_newhigh｜⚡好調｜🔴過熱｜FAIL_UWAHIGE｜3,950円｜💰38.6万円｜—｜⚠日程不明｜🎯2手法一致(kenmo_momentum+kenmo_newhigh)
- 9268 OPTIMUS GROUP Co., Ltd.｜kenmo_momentum｜⚡好調｜💎割安｜PASS｜339円｜💰3.4万円｜⛔提案なし(指名鮮度切れ 17営業日)｜📋カルテ窓 11/13(残12営業日)
  > 【業態】ニュージーランド中心に中古車輸出。現地で自動車総合サービス展開。豪にも進出。
  > 【いま】終値339円・直近5日+1.19%（材料未確認）
  > 【調子】⚡好調（6/13）
  > 【水準】💎割安（7.0/7）— PER7.24倍・PEG0.6462・52週11.4% ／ 💰単元3.4万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 17営業日)）
- 4477 BASE, Inc.｜kenmo_momentum/granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜338円｜💰3.5万円｜—｜⚠日程不明
- 9628 San Holdings,Inc.｜kenmo_momentum｜⚡好調｜🟡やや割高｜FAIL_INSEN｜1,151円｜💰12.0万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）
- 2980 SRE Holdings Corp.｜kenmo_momentum｜⚡好調｜🟢値頃｜FAIL_INSEN｜2,186円｜💰22.7万円｜—｜📋カルテ窓 11/11(残10営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 4412 Science Arts, Inc.｜kenmo_momentum｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜1,290円｜💰13.2万円｜—｜⚠日程不明
- 505A Geekly,Inc.｜kenmo_momentum｜✅順調｜💎割安｜PASS｜1,169円｜💰11.7万円｜momentum 1,171（✅即時可）｜⚠日程不明
  > 【業態】IT・Web・ゲーム業界に特化した人材紹介(転職エージェント)事業を手掛ける。
  > 【いま】終値1,169円・直近5日+2.19%（材料未確認）
  > 【調子】✅順調（4/13） — D軸判定不能(四半期データ不足・中立1点)
  > 【水準】💎割安（7.0/7）— PER8.30倍・PEG0.4728・52週18.4% ／ 💰単元11.7万円
  > 【戦略】当日高値超えの逆指値1,171円で順張り参戦を検討。上限1,182.7円・SL1,099.8円目安
- 4743 ITFOR Inc.｜kenmo_momentum｜✅順調｜🟢値頃｜FAIL_INSEN｜1,640円｜💰16.8万円｜—｜📋カルテ窓 11/12(残11営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 5038 eWeLL Co.,Ltd｜kenmo_momentum｜✅順調｜⚪妥当｜FAIL_INSEN｜2,345円｜💰23.9万円｜—｜📋カルテ窓 11/13(残12営業日)
- 6629 TECHNO HORIZON Co., Ltd.｜granville_tenkan/kenmo_momentum｜✅順調｜⚪妥当｜FAIL_INSEN｜947円｜💰9.3万円｜—｜⏰決算 10/30(残3営業日)
- 6289 Giken Ltd.｜granville_tenkan/kenmo_momentum｜⚠減速｜🔴過熱｜FAIL_INSEN｜1,981円｜💰20.4万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）
- 3077 Horiifoodservice Co., Ltd.｜kenmo_momentum/granville_rebound｜判定保留(変則決算)｜🟢値頃｜FAIL_INSEN｜1,120円｜💰11.5万円｜—｜⚠日程不明
- 618A KOMPEITO Inc.｜kenmo_momentum｜取得不可｜⚪妥当｜PASS｜2,134円｜💰21.3万円｜momentum 2,138（✅即時可）｜⚠日程不明
  > 【業態】設置型の健康社食サービス「OFFICE DEYASAI」などの企画・運営を手掛ける。
  > 【いま】終値2,134円・直近5日+17.12%（材料未確認）
  > 【調子】—（業績データ(前期比行なし)）
  > 【水準】⚪妥当（3.0/7）— PER20.70倍・PEG—・52週97.6% ／ 💰単元21.3万円
  > 【戦略】当日高値超えの逆指値2,138円で順張り参戦を検討。上限2,159.4円・SL2,008.8円目安
- 6918 Aval Data Corporation｜kenmo_newhigh/granville_rebound｜🚀確変｜🟢値頃｜FAIL_INSEN｜3,750円｜💰36.5万円｜—｜📋カルテ窓 11/12(残11営業日)
- 3374 Naigai Tec Corporation｜kenmo_newhigh/ai_momentum/granville_oshime｜🚀確変｜🟢値頃｜FAIL_UWAHIGE｜4,605円｜💰44.8万円｜—｜📋カルテ窓 11/13(残12営業日)
- 7567 Sakae Electronics Corp.｜kenmo_newhigh｜🚀確変｜⚪妥当｜FAIL_UWAHIGE｜644円｜💰6.3万円｜—｜📋カルテ窓 11/12(残11営業日)
- 6337 Tesec Corporation｜kenmo_newhigh/granville_rebound｜🚀確変｜🟢値頃｜FAIL_INSEN｜3,420円｜💰30.4万円｜—｜⚠日程不明｜⚡材料後出し
- 446A ノースサンド｜kenmo_newhigh｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜2,864円｜💰28.9万円｜—｜⚠日程不明
- 3696 セレス｜kenmo_newhigh｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜2,246円｜💰22.6万円｜—｜📋カルテ窓 11/12(残11営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 2930 北の達人コーポレーション｜kenmo_newhigh｜⚡好調｜🔴過熱｜PASS｜147円｜💰1.5万円｜momentum 149（✅即時可）｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）
  > 【業態】健康美容食品や化粧品を企画・通販。「カイテキオリゴ」や目元クリームが主力商品。
  > 【いま】終値147円・直近5日+0.00%（材料未確認）
  > 【調子】⚡好調（6/13） — 質注意
  > 【水準】🔴過熱（0.0/7）— PER27.74倍・PEG6.6889・52週83.3% ／ 💰単元1.5万円
  > 【戦略】当日高値超えの逆指値149円で順張り参戦を検討。上限150.5円・SL139.1円目安
- 4379 Photosynth inc.｜kenmo_newhigh｜⚡好調｜🔴過熱｜FAIL_UWAHIGE｜519円｜💰5.3万円｜—｜📋カルテ窓 11/12(残11営業日)
- 2820 Yamami Co.｜kenmo_newhigh｜✅順調｜🟡やや割高｜FAIL_INSEN｜6,730円｜💰65.2万円｜—｜📋カルテ窓 11/11(残10営業日)
- 3843 Freebit Co., Ltd.｜kenmo_newhigh/granville_tenkan｜✅順調｜⚪妥当｜FAIL_UWAHIGE｜1,750円｜💰17.5万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）
- 4331 Take and Give. Needs Co., Ltd.｜kenmo_newhigh｜✅順調｜🟡やや割高｜FAIL_UWAHIGE｜815円｜💰8.2万円｜—｜📋カルテ窓 11/11(残10営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 7161 Jimoto Holdings, Inc.｜kenmo_newhigh｜業績データ取得不可｜⚪妥当｜PASS｜563円｜💰5.6万円｜⛔提案なし(指名鮮度切れ 13営業日)｜📋カルテ窓 11/13(残12営業日)
  > 【業態】銀行業（地方銀行・銀行・金利上昇メリット関連）
  > 【いま】終値563円・直近5日-1.23%（材料未確認）
  > 【調子】—（業績データ(前期比行なし)）
  > 【水準】⚪妥当（4.0/7）— PER4.40倍・PEG0.1651・52週56.7% ／ 💰単元5.6万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 13営業日)）
- 4565 Nxera Pharma Co., Ltd.｜granville_oshime/kenmo_newhigh｜業績データ取得不可(経常益予想非開示)｜🟡やや割高｜FAIL_UWAHIGE｜1,364円｜💰13.4万円｜—｜⏰決算 10/30(残3営業日)
- 6278 ユニオンツール｜choruko_reversal｜🚀確変｜🟢値頃｜FAIL_UWAHIGE｜12,450円｜💰122.9万円｜—｜📋カルテ窓 11/11(残10営業日)
- 6875 メガチップス｜choruko_reversal｜🔥絶好調｜💎割安｜PASS｜9,940円｜💰99.4万円｜reversal 9,940（✅即時可）｜📐進捗 上振れ 20.3%｜⚠1単元でリスク枠超過（83,000円）
  > 【業態】カスタムLSI、画像転送システムが主力。生産外部委託。任天堂向け中心。5G向けも。
  > 【いま】終値9,940円・直近5日+0.30%（材料未確認）
  > 【調子】🔥絶好調（10/13）
  > 【水準】💎割安（6.0/7）— PER4.11倍・PEG0.0・52週43.6% ／ 💰単元99.4万円
  > 【戦略】当日終値9,940円の指値で反転を取りにいく。SL9,110円（直近5日安値）／⚠1単元リスク83,000円（枠超過）
- 8871 GOLDCREST Co., Ltd.｜choruko_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜2,873円｜💰29.1万円｜—｜🚨決算直前 10/28(残1営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 3391 TSURUHA Holdings, Inc.｜choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜2,219.5円｜💰22.5万円｜—｜⚠日程不明
- 8336 武蔵野銀行｜granville_oshime/choruko_reversal/granville_rebound｜🔥絶好調｜🟢値頃｜PASS｜2,565円｜💰25.6万円｜reversal 2,565（✅即時可）
  > 【業態】埼玉地盤で全域に店舗網。地域密着型営業展開。千葉銀と提携。
  > 【いま】終値2,565円・直近5日+0.23%（材料未確認）
  > 【調子】🔥絶好調（9/13）
  > 【水準】🟢値頃（5.6/7）— PER12.76倍・PEG0.3936・52週72.8% ／ 💰単元25.6万円
  > 【戦略】当日終値2,565円の指値で反転を取りにいく。SL2,365円（直近5日安値）
- 3036 アルコニックス｜choruko_reversal｜🔥絶好調｜🟢値頃｜PASS｜3,120円｜💰31.2万円｜reversal 3,120（✅即時可）
  > 【業態】非鉄金属を製販。双日から分離。アルミ銅、レアメタルに強み。金属加工業に注力。
  > 【いま】終値3,120円・直近5日+2.46%（材料未確認）
  > 【調子】🔥絶好調（9/13）
  > 【水準】🟢値頃（5.0/7）— PER10.20倍・PEG0.1807・52週61.6% ／ 💰単元31.2万円
  > 【戦略】当日終値3,120円の指値で反転を取りにいく。SL2,893円（直近5日安値）
- 6268 ナブテスコ｜choruko_reversal｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜4,285円｜💰41.4万円｜—｜📋カルテ窓 11/13(残12営業日)
- 6324 Harmonic Drive Systems Inc.｜choruko_reversal｜🔥絶好調｜⚪妥当｜PASS｜5,340円｜💰53.4万円｜reversal 5,340（✅即時可）｜📋カルテ窓 11/11(残10営業日)｜⚠1単元でリスク枠超過（81,000円）
  > 【業態】精密制御減速装置が軸。小型・軽量強み。産業用ロボット向け等。メカトロ製品も。
  > 【いま】終値5,340円・直近5日+1.52%（材料未確認）
  > 【調子】🔥絶好調（9/13）
  > 【水準】⚪妥当（4.0/7）— PER84.23倍・PEG0.3778・52週43.4% ／ 💰単元53.4万円
  > 【戦略】当日終値5,340円の指値で反転を取りにいく。SL4,530円（直近5日安値）／⚠1単元リスク81,000円（枠超過）
- 6645 OMRON Corporation｜granville_rebound/choruko_reversal｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜5,415円｜💰53.3万円｜—
- 3222 United Super Markets Holdings, Inc.｜choruko_reversal｜🔥絶好調｜🔴過熱｜FAIL_INSEN｜767円｜💰7.8万円｜—｜⚠日程不明
- 1803 Shimizu Corporation｜choruko_reversal｜🔥絶好調｜💎割安｜PASS｜2,094.5円｜💰20.9万円｜⛔提案なし(指名鮮度切れ 12営業日)
  > 【業態】総合建設大手。民間建築中心。社寺・伝統建築に定評。エンジニアリング事業も。
  > 【いま】終値2,094.5円・直近5日+4.91%（材料未確認）
  > 【調子】🔥絶好調（8/13）
  > 【水準】💎割安（6.0/7）— PER8.52倍・PEG0.1704・52週8.9% ／ 💰単元20.9万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 12営業日)）
- 8346 東邦銀行｜granville_oshime/granville_rebound/choruko_reversal｜🔥絶好調｜🟢値頃｜PASS｜957円｜💰9.6万円｜reversal 957（✅即時可）
  > 【業態】福島地盤の地銀大手。県内で圧倒的シェア。茨城、東京など県外にも注力。
  > 【いま】終値957円・直近5日-1.34%（材料未確認）
  > 【調子】🔥絶好調（8/13）
  > 【水準】🟢値頃（5.0/7）— PER14.95倍・PEG0.3808・52週71.3% ／ 💰単元9.6万円
  > 【戦略】当日終値957円の指値で反転を取りにいく。SL871円（直近5日安値）
- 4088 Air Water Inc.｜choruko_reversal｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜2,762円｜💰27.6万円｜—｜⚠日程不明
- 5301 Tokai Carbon Co., Ltd.｜choruko_reversal｜🔥絶好調｜⚪妥当｜PASS｜1,933.5円｜💰19.3万円｜reversal 1,933.5（✅即時可）
  > 【業態】ガラス・土石
  > 【いま】終値1,933.5円・直近5日-0.59%（材料未確認）
  > 【調子】🔥絶好調（8/13）
  > 【水準】⚪妥当（4.0/7）— PER17.79倍・PEG0.5859・52週68.3% ／ 💰単元19.3万円
  > 【戦略】当日終値1,933.5円の指値で反転を取りにいく。SL1,788円（直近5日安値）
- 7733 Olympus Corp.｜choruko_reversal｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜1,750円｜💰17.5万円｜—
- 7004 カナデビア｜choruko_reversal｜⚠減速｜💎割安｜PASS｜1,053円｜💰10.5万円｜reversal 1,053（✅即時可）｜⚠業績基調が下向き（減速）｜⚠バリュートラップ疑い
  > 【業態】ゴミ焼却発電設備が主柱。淡水化プラント、橋梁、掘進機など。持分で内海造船。
  > 【いま】終値1,053円・直近5日-1.22%（材料未確認）
  > 【調子】⚠減速（7/13） — 減収でleverage参考値、減収
  > 【水準】💎割安（7.0/7）— PER8.44倍・PEG0.1372・52週23.8% ／ 💰単元10.5万円
  > 【戦略】当日終値1,053円の指値で反転を取りにいく。SL1,001円（直近5日安値）
- 6370 栗田工業｜choruko_reversal｜⚡好調｜🟢値頃｜FAIL_INSEN｜6,977円｜💰68.9万円｜—
- 8522 Bank of Nagoya, Ltd.｜choruko_reversal｜⚡好調｜🟢値頃｜FAIL_INSEN｜5,910円｜💰57.2万円｜—｜📋カルテ窓 11/13(残12営業日)
- 2874 YOKOREI CO. LTD.｜granville_rebound/choruko_reversal｜⚠減速｜⚪妥当｜PASS｜1,831円｜💰18.3万円｜⛔提案なし(指名鮮度切れ 12営業日)｜📋カルテ窓 11/12(残11営業日)｜⚠業績基調が下向き（減速）
  > 【業態】冷蔵倉庫大手。水産品中心に農畜産物の加工、販売も。物流センター拡張。
  > 【いま】終値1,831円・直近5日+6.08%（材料未確認）
  > 【調子】⚠減速（7/13） — A成長率0以下のためレバレッジ計算不可(C=0)、減収-0.4%のため上限を減速に固定(計算上は⚡好調)
  > 【水準】⚪妥当（4.0/7）— PER22.55倍・PEG0.3008・52週42.8% ／ 💰単元18.3万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 12営業日)）
- 6302 住友重機械工業｜granville_tenkan/choruko_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜5,467円｜💰53.7万円｜—｜⏰決算 10/30(残3営業日)
- 6754 アンリツ｜ai_reversal/choruko_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,844.5円｜💰27.2万円｜—｜⏰決算 10/29(残2営業日)
- 8987 Japan Excellent, Inc.｜choruko_reversal｜⚡好調｜🟢値頃｜FAIL_INSEN｜126,400円｜💰12.7万円｜—｜⚠日程不明
- 8282 K'S HOLDINGS CORPORATION｜choruko_reversal｜⚡好調｜🟢値頃｜FAIL_INSEN｜1,697.5円｜💰17.3万円｜—
- 8386 百十四銀行｜choruko_reversal/granville_rebound｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜2,737円｜💰26.2万円｜—｜⚡材料後出し
- 6332 月島ホールディングス｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,371円｜💰23.2万円｜—
- 8088 岩谷産業｜choruko_reversal｜⚡好調｜⚪妥当｜PASS｜1,928円｜💰19.3万円｜reversal 1,928（✅即時可）
  > 【業態】産業用・家庭用ガス商社。LPG首位。合成樹脂や水素エネ事業も。持分にコスモHD。
  > 【いま】終値1,928円・直近5日+1.88%（材料未確認）
  > 【調子】⚡好調（6/13）
  > 【水準】⚪妥当（4.0/7）— PER9.76倍・PEG1.4254・52週49.8% ／ 💰単元19.3万円
  > 【戦略】当日終値1,928円の指値で反転を取りにいく。SL1,836.5円（直近5日安値）
- 5333 ＮＧＫ｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜4,687円｜💰45.8万円｜—｜⏰決算 10/30(残3営業日)
- 9412 SKY Perfect JSAT Corporation｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜1,862円｜💰18.6万円｜—｜⏰決算 11/04(残5営業日)
- 8125 Wakita & Co., Ltd.｜choruko_reversal｜⚡好調｜🔴過熱｜FAIL_INSEN｜1,871円｜💰18.8万円｜—｜⚠日程不明
- 7721 Tokyo Keiki Inc.｜choruko_reversal｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜5,580円｜💰56.6万円｜—
- 8278 Fuji Co., Ltd.｜choruko_reversal｜⚡好調｜🟢値頃｜FAIL_INSEN｜2,004円｜💰20.3万円｜—｜⚠日程不明
- 8714 池田泉州ホールディングス｜granville_oshime/choruko_reversal｜⚡好調｜⚪妥当｜PASS｜948円｜💰9.5万円｜reversal 948（✅即時可）｜📋カルテ窓 11/13(残12営業日)
  > 【業態】池田銀と泉州銀が経営統合。関西地銀、大阪府内最大。地域主義推進。
  > 【いま】終値948円・直近5日-2.57%（材料未確認）
  > 【調子】⚡好調（5/13）
  > 【水準】⚪妥当（4.2/7）— PER13.82倍・PEG1.0673・52週57.1% ／ 💰単元9.5万円
  > 【戦略】当日終値948円の指値で反転を取りにいく。SL886円（直近5日安値）
- 8393 Miyazaki Bank Ltd.｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜2,405円｜💰23.1万円｜—
- 8399 琉球銀行｜choruko_reversal/granville_rebound｜⚡好調｜⚪妥当｜PASS｜2,835円｜💰28.4万円｜reversal 2,835（✅即時可）｜📋カルテ窓 11/11(残10営業日)
  > 【業態】沖縄地盤の地銀大手。地域密着型で預金、融資県内首位。信託業務も併営。
  > 【いま】終値2,835円・直近5日+2.09%（材料未確認）
  > 【調子】⚡好調（5/13） — A:上期予想YoY代替(通期売上予想なし)
  > 【水準】⚪妥当（4.0/7）— PER11.64倍・PEG0.826・52週69.7% ／ 💰単元28.4万円
  > 【戦略】当日終値2,835円の指値で反転を取りにいく。SL2,580円（直近5日安値）
- 268A Rigaku Holdings Corporation｜choruko_reversal｜⚡好調｜⚪妥当｜PASS｜1,485円｜💰14.8万円｜reversal 1,485（✅即時可）｜📋カルテ窓 11/11(残10営業日)
  > 【業態】X線分析技術・世界大手。X線技術を用いた理科学機器の製造・販売。(精密機器)
  > 【いま】終値1,485円・直近5日+3.12%（材料未確認）
  > 【調子】⚡好調（5/13）
  > 【水準】⚪妥当（3.0/7）— PER26.90倍・PEG1.7689・52週23.8% ／ 💰単元14.8万円
  > 【戦略】当日終値1,485円の指値で反転を取りにいく。SL1,298円（直近5日安値）
- 7458 Daiichikosho Co., Ltd.｜choruko_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜1,751.5円｜💰17.7万円｜—
- 2782 Seria Co., Ltd.｜choruko_reversal｜⚡好調｜🔴過熱｜FAIL_INSEN｜4,395円｜💰44.0万円｜—｜⏰決算 10/30(残3営業日)｜📑TOPIX新規採用（2026-10-30 組入）
- 2809 Kewpie Corporation｜choruko_reversal｜⚡好調｜🔴過熱｜FAIL_INSEN｜4,552円｜💰45.5万円｜—｜⚠日程不明
- 4666 Park24 Co., Ltd.｜choruko_reversal｜✅順調｜💎割安｜FAIL_UWAHIGE｜1,831円｜💰18.5万円｜—｜⚠日程不明
- 7731 ニコン｜choruko_reversal｜✅順調｜🟢値頃｜FAIL_UWAHIGE｜1,730円｜💰17.0万円｜—
- 3279 Activia Properties, Inc.｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜126,600円｜💰12.5万円｜—｜⚠日程不明
- 8381 San-in Godo Bank Ltd.｜choruko_reversal/granville_rebound｜✅順調｜⚪妥当｜PASS｜2,076円｜💰20.8万円｜reversal 2,076（✅即時可）｜📋カルテ窓 11/12(残11営業日)
  > 【業態】山陰が地盤。鳥取・島根で預金トップ。広島・岡山等に展開、法人取引拡大へ。
  > 【いま】終値2,076円・直近5日-3.58%（材料未確認）
  > 【調子】✅順調（4/13） — D軸判定不能(四半期データ不足・中立1点)
  > 【水準】⚪妥当（4.2/7）— PER12.13倍・PEG0.7591・52週54.6% ／ 💰単元20.8万円
  > 【戦略】当日終値2,076円の指値で反転を取りにいく。SL1,955円（直近5日安値）
- 8524 North Pacific Bank, Ltd.｜granville_rebound/choruko_reversal｜⚠減速｜⚪妥当｜PASS｜1,176円｜💰11.8万円｜reversal 1,176（✅即時可）｜📋カルテ窓 11/13(残12営業日)｜⚠業績基調が下向き（減速）
  > 【業態】北海道地盤で資金量第２地銀最大。拓銀と札幌銀の取込で拡大。
  > 【いま】終値1,176円・直近5日+4.07%（材料未確認）
  > 【調子】⚠減速（4/13） — 減収、質注意、E簡易判定
  > 【水準】⚪妥当（4.2/7）— PER14.96倍・PEG0.8176・52週67.9% ／ 💰単元11.8万円
  > 【戦略】当日終値1,176円の指値で反転を取りにいく。SL1,048円（直近5日安値）
- 3282 Comforia Residential REIT, Inc.｜choruko_reversal｜✅順調｜🟡やや割高｜FAIL_INSEN｜89,900円｜💰9.1万円｜—｜⚠日程不明
- 8952 Japan Real Estate Investment Corp.｜choruko_reversal｜✅順調｜🟡やや割高｜FAIL_INSEN｜109,300円｜💰11.0万円｜—｜📋カルテ窓 11/16(残13営業日)
- 6925 Ushio Inc.｜choruko_reversal｜✅順調｜🟡やや割高｜FAIL_UWAHIGE｜3,354円｜💰32.9万円｜—
- 1861 Kumagai Gumi Co., Ltd.｜choruko_reversal｜✅順調｜💎割安｜PASS｜1,246円｜💰12.5万円｜reversal 1,246（✅即時可）｜📋カルテ窓 11/12(残11営業日)
  > 【業態】総合建設準大手。大型土木・超高層ビル建築で実績。筆頭株主に住友林業。
  > 【いま】終値1,246円・直近5日+3.57%（材料未確認）
  > 【調子】✅順調（3/13） — 進捗データなし(判定不能)
  > 【水準】💎割安（6.0/7）— PER10.38倍・PEG0.7109・52週8.1% ／ 💰単元12.5万円
  > 【戦略】当日終値1,246円の指値で反転を取りにいく。SL1,193円（直近5日安値）
- 5331 ノリタケ｜choruko_reversal｜✅順調｜🟢値頃｜FAIL_UWAHIGE｜3,290円｜💰31.7万円｜—
- 1417 MIRAIT ONE Corporation｜choruko_reversal｜✅順調｜🟢値頃｜PASS｜3,409円｜💰34.1万円｜reversal 3,409（✅即時可）
  > 【業態】通信工事大手。NTT向け大。西武建設、国際航業を買収。インフラ、デジタル化も。
  > 【いま】終値3,409円・直近5日+2.71%（材料未確認）
  > 【調子】✅順調（3/13）
  > 【水準】🟢値頃（5.0/7）— PER11.64倍・PEG1.2207・52週35.6% ／ 💰単元34.1万円
  > 【戦略】当日終値3,409円の指値で反転を取りにいく。SL3,274円（直近5日安値）
- 8198 Maxvalu Tokai Co., Ltd.｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜3,120円｜💰31.9万円｜—｜⚠日程不明
- 1820 Nishimatsu Construction Co., Ltd.｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜5,386円｜💰54.2万円｜—
- 1944 Kinden Corporation｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜6,385円｜💰62.5万円｜—｜⏰決算 10/30(残3営業日)
- 1952 Shin Nippon Air Technologies Co., Ltd.｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_UWAHIGE｜3,025円｜💰29.5万円｜—｜📋カルテ窓 11/12(残11営業日)
- 3148 Create SD Holdings Co., Ltd.｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜3,220円｜💰32.6万円｜—｜⚠日程不明
- 6269 Modec, Inc.｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜8,115円｜💰81.3万円｜—
- 7003 Mitsui ES Holdings Co., Ltd.｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_UWAHIGE｜3,593円｜💰35.1万円｜—
- 8584 Jaccs Co., Ltd.｜choruko_reversal｜🔻悪化｜⚪妥当｜FAIL_INSEN｜3,365円｜💰34.0万円｜—
- 9882 Yellow Hat Ltd.｜choruko_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜1,615円｜💰16.3万円｜—｜⏰決算 10/30(残3営業日)
- 1860 Toda Corporation｜choruko_reversal｜✅順調｜🟡やや割高｜PASS｜1,470.5円｜💰14.7万円｜reversal 1,470.5（✅即時可）｜📋カルテ窓 11/13(残12営業日)
  > 【業態】名門で業界準大手。堅実経営。病院・学校に強み。洋上風力発電に注力。
  > 【いま】終値1,470.5円・直近5日+4.66%（材料未確認）
  > 【調子】✅順調（3/13） — 質注意、経常成長率-9.1%
  > 【水準】🟡やや割高（2.0/7）— PER12.44倍・PEG—・52週70.0% ／ 💰単元14.7万円
  > 【戦略】当日終値1,470.5円の指値で反転を取りにいく。SL1,402円（直近5日安値）
- 4966 上村工業｜choruko_reversal｜✅順調｜🟡やや割高｜FAIL_UWAHIGE｜18,540円｜💰175.7万円｜—｜📋カルテ窓 11/11(残10営業日)｜📑TOPIX新規採用（2026-10-30 組入）
- 6055 Japan Material Co., Ltd.｜choruko_reversal｜✅順調｜🟡やや割高｜FAIL_UWAHIGE｜2,034円｜💰19.6万円｜—｜📋カルテ窓 11/12(残11営業日)
- 8066 Mitani Corporation｜granville_rebound/choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜2,819円｜💰28.7万円｜—｜📋カルテ窓 11/12(残11営業日)
- 2659 SAN-A CO., LTD.｜choruko_reversal｜✅順調｜🔴過熱｜PASS｜3,220円｜💰32.2万円｜reversal 3,220（✅即時可）｜⚠日程不明
  > 【業態】沖縄県内流通首位。スーパー、レストラン、ドラッグストアを展開。ローソンと提携。ニチリウG。
  > 【いま】終値3,220円・直近5日+2.22%（材料未確認）
  > 【調子】✅順調（3/13） — 質注意
  > 【水準】🔴過熱（1.0/7）— PER17.44倍・PEG14.9724・52週68.2% ／ 💰単元32.2万円
  > 【戦略】当日終値3,220円の指値で反転を取りにいく。SL3,095円（直近5日安値）
- 5021 Cosmo Energy Holdings Co., Ltd.｜choruko_reversal｜🔻悪化｜🔴過熱｜PASS｜4,370円｜💰43.7万円｜reversal 4,370（✅即時可）｜⚠業績基調が下向き（悪化）
  > 【業態】石油元売り大手。石油化学、石油開発、再生エネルギーなど多角。岩谷産業系。
  > 【いま】終値4,370円・直近5日+3.48%（材料未確認）
  > 【調子】🔻悪化（3/13） — 質注意
  > 【水準】🔴過熱（1.0/7）— PER15.77倍・PEG—・52週59.3% ／ 💰単元43.7万円
  > 【戦略】当日終値4,370円の指値で反転を取りにいく。SL4,180円（直近5日安値）
- 7984 Kokuyo Co., Ltd.｜choruko_reversal｜✅順調｜🔴過熱｜FAIL_INSEN｜891.2999877929688円｜💰9.0万円｜—｜⏰決算 10/29(残2営業日)
- 2805 S&B Foods Inc.｜granville_rebound/choruko_reversal｜✅順調｜🔴過熱｜FAIL_INSEN｜6,830円｜💰68.5万円｜—｜⏰決算 10/30(残3営業日)｜📑TOPIX新規採用（2026-10-30 組入）
- 3289 Tokyu Fudosan Holdings Corp.｜choruko_reversal｜➖横ばい｜🟢値頃｜FAIL_INSEN｜1,226円｜💰12.5万円｜—
- 6674 ジーエス・ユアサ　コーポレーション｜choruko_reversal｜➖横ばい｜⚪妥当｜FAIL_INSEN｜4,720円｜💰46.4万円｜—
- 8818 Keihanshin Building Co., Ltd.｜choruko_reversal｜➖横ばい｜⚪妥当｜FAIL_INSEN｜935円｜💰9.5万円｜—｜⏰決算 10/30(残3営業日)
- 1333 Umios Corporation｜choruko_reversal｜➖横ばい｜⚪妥当｜FAIL_INSEN｜1,222.5円｜💰12.3万円｜—｜⚠日程不明
- 1719 HAZAMA ANDO Corporation｜choruko_reversal｜➖横ばい｜⚪妥当｜FAIL_INSEN｜1,789円｜💰17.9万円｜—｜📋カルテ窓 11/12(残11営業日)
- 1833 Okumura Corporation｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜5,350円｜💰53.5万円｜—｜📋カルテ窓 11/11(残10営業日)
- 9503 Kansai Electric Power Company, Incorporated｜choruko_reversal/granville_rebound｜🔻悪化｜⚪妥当｜FAIL_INSEN｜2,745円｜💰27.8万円｜—｜⏰決算 10/29(残2営業日)
- 3445 RS Technologies Co. Ltd.｜choruko_reversal｜➖横ばい｜🟡やや割高｜FAIL_UWAHIGE｜5,010円｜💰48.3万円｜—｜⚠日程不明
- 6366 Chiyoda Corp.｜choruko_reversal｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜612円｜💰5.7万円｜—｜⏰決算 11/04(残5営業日)｜📑TOPIX新規採用（2026-10-30 組入）
- 7220 Musashi Seimitsu Industry Co., Ltd.｜choruko_reversal｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜2,422円｜💰24.1万円｜—
- 5844 Kyoto Financial Group,Inc.｜choruko_reversal｜🔻悪化｜🔴過熱｜FAIL_UWAHIGE｜4,060円｜💰40.2万円｜—｜📋カルテ窓 11/13(残12営業日)
- 2379 dip Corporation｜choruko_reversal｜⚠減速｜💎割安｜FAIL_UWAHIGE｜1,513円｜💰15.0万円｜—｜⚠日程不明
- 6479 ミネベア｜choruko_reversal｜⚠減速｜💎割安｜FAIL_UWAHIGE｜3,221円｜💰31.2万円｜—
- 1893 Penta-Ocean Construction Co., Ltd.｜choruko_reversal｜⚠減速｜⚪妥当｜PASS｜1,382円｜💰13.8万円｜reversal 1,382（✅即時可）｜⚠業績基調が下向き（減速）
  > 【業態】海上土木の最大手。港湾CIM技術を推進。海外で大型受注に注力。
  > 【いま】終値1,382円・直近5日+3.40%（材料未確認）
  > 【調子】⚠減速（1/13）
  > 【水準】⚪妥当（3.0/7）— PER10.67倍・PEG7.052・52週8.9% ／ 💰単元13.8万円
  > 【戦略】当日終値1,382円の指値で反転を取りにいく。SL1,296.5円（直近5日安値）
- 6753 Sharp Corporation｜choruko_reversal｜🔻悪化｜⚪妥当｜FAIL_INSEN｜572.2999877929688円｜💰5.9万円｜—
- 8276 HEIWADO CO., LTD.｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜2,615円｜💰26.1万円｜—｜⚠日程不明
- 9974 BELC Co., Ltd.｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜6,370円｜💰64.5万円｜—｜⚠日程不明
- 3234 Mori Hills Reit Investment Corporation｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜118,800円｜💰11.9万円｜—｜⚠日程不明
- 3249 Industrial & Infrastructure Fund Investment Corporation｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜129,400円｜💰13.0万円｜—｜⚠日程不明
- 3283 Nippon Prologis REIT, Inc.｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜81,700円｜💰8.2万円｜—｜⚠日程不明
- 3292 AEON REIT Investment Corp.｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜106,100円｜💰10.7万円｜—｜⚠日程不明
- 3296 NIPPON REIT Investment Corp｜choruko_reversal｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜75,700円｜💰7.6万円｜—｜⚠日程不明｜⚡材料後出し
- 3309 Sekisui House Reit. Inc.｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜68,000円｜💰6.8万円｜—｜⚠日程不明
- 3462 Nomura Real Estate Master Fund, Inc.｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜128,600円｜💰12.9万円｜—｜⚠日程不明
- 5482 Aichi Steel Corporation｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜2,853円｜💰28.5万円｜—｜⏰決算 10/29(残2営業日)
- 8953 Japan Metropolitan Fund Investment Corporation｜choruko_reversal｜🔻悪化｜🟡やや割高｜PASS｜107,300円｜💰10.7万円｜⛔提案なし(指名鮮度切れ 11営業日)｜⚠日程不明｜⚠業績基調が下向き（悪化）
  > 【業態】商業施設、オフィスビル、住宅、複合施設など総合型投資。運用:KJRマネジメント。
  > 【いま】終値107,300円・直近5日+5.20%（材料未確認）
  > 【調子】🔻悪化（1/13） — 質注意、A成長率0以下のためレバレッジ計算不可(C=0)、D軸判定不能(四半期データ不足・中立1点)、経常減益-20.7%
  > 【水準】🟡やや割高（2.8/7）— PER41.06倍・PEG—・52週20.7% ／ 💰単元10.7万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 11営業日)）
- 8954 ORIX JREIT Inc.｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜88,900円｜💰9.0万円｜—｜⚠日程不明
- 8955 Japan Prime Realty Investment Corporation｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_UWAHIGE｜92,700円｜💰9.3万円｜—｜⚠日程不明
- 8986 Daiwa Securities Living Investment Corporation｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜83,400円｜💰8.4万円｜—｜📋カルテ窓 11/19(残16営業日)
- 1946 Toenec Corporation｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_UWAHIGE｜2,111円｜💰20.9万円｜—｜⏰決算 10/29(残2営業日)
- 2815 ARIAKE JAPAN Co., Ltd.｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜5,240円｜💰52.5万円｜—
- 5310 Toyo Tanso Co., Ltd.｜choruko_reversal/ai_reversal｜🔻悪化｜🟡やや割高｜FAIL_UWAHIGE｜6,400円｜💰62.4万円｜—
- 5631 Japan Steel Works, Ltd.｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜6,105円｜💰61.5万円｜—
- 6183 BELLSYSTEM24 Holdings, Inc.｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜1,353円｜💰14.0万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）
- 9948 Arcs Company, Limited｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜3,510円｜💰35.5万円｜—｜⚠日程不明
- 1963 日揮ホールディングス｜choruko_reversal｜🔻悪化｜🔴過熱｜PASS｜2,137.5円｜💰21.4万円｜reversal 2,137.5（✅即時可）｜📋カルテ窓 11/11(残10営業日)｜⚠業績基調が下向き（悪化）
  > 【業態】総合エンジニアリング最大手。世界各地で石油、化学、発電、水素、LNGプラント建設。
  > 【いま】終値2,137.5円・直近5日+2.59%（材料未確認）
  > 【調子】🔻悪化（1/13） — 質注意、D軸判定不能(四半期データ不足・中立1点)、減収、経常減益
  > 【水準】🔴過熱（1.4/7）— PER11.25倍・PEG—・52週44.5% ／ 💰単元21.4万円
  > 【戦略】当日終値2,137.5円の指値で反転を取りにいく。SL1,974円（直近5日安値）
- 3105 日清紡ホールディングス｜choruko_reversal｜🔻悪化｜🔴過熱｜FAIL_UWAHIGE｜2,380円｜💰22.4万円｜—
- 4928 Noevir Holdings Co., Ltd.｜choruko_reversal｜⚠減速｜🔴過熱｜FAIL_INSEN｜4,670円｜💰47.4万円｜—
- 6960 Fukuda Denshi Co., Ltd.｜choruko_reversal｜⚠減速｜🔴過熱｜FAIL_INSEN｜11,020円｜💰109.4万円｜—｜⏰決算 10/30(残3営業日)｜📑TOPIX新規採用（2026-10-30 組入）
- 9436 Okinawa Cellular Telephone Company｜choruko_reversal｜⚠減速｜🔴過熱｜FAIL_INSEN｜3,340円｜💰33.4万円｜—｜⏰決算 10/29(残2営業日)｜📑TOPIX新規採用（2026-10-30 組入）
- 1662 Japan Petroleum Exploration Co., Ltd.｜choruko_reversal｜🔻悪化｜⚪妥当｜FAIL_INSEN｜1,747円｜💰17.1万円｜—｜📋カルテ窓 11/12(残11営業日)
- 6804 Hosiden Corp.｜choruko_reversal｜🔻悪化｜⚪妥当｜FAIL_UWAHIGE｜2,323円｜💰22.7万円｜—｜📋カルテ窓 11/13(残12営業日)
- 1969 高砂熱学工業｜choruko_reversal｜⚠減速｜⚪妥当｜PASS｜4,155円｜💰41.5万円｜reversal 4,155（✅即時可）｜⚠日程不明｜⚠業績基調が下向き（減速）
  > 【業態】空調工事で首位。民間工事が中心。環境ソリューション企業を志向。海外強化。
  > 【いま】終値4,155円・直近5日+1.76%（材料未確認）
  > 【調子】⚠減速（0/13） — E軸:進捗18.5%<例年22.5%
  > 【水準】⚪妥当（3.0/7）— PER13.60倍・PEG5.0702・52週9.6% ／ 💰単元41.5万円
  > 【戦略】当日終値4,155円の指値で反転を取りにいく。SL3,996円（直近5日安値）
- 8585 Orient Corporation｜choruko_reversal｜⚠減速｜⚪妥当｜FAIL_INSEN｜752円｜💰7.5万円｜—｜⏰決算 10/30(残3営業日)
- 8194 Life Corporation｜choruko_reversal｜⚠減速｜🟡やや割高｜FAIL_INSEN｜2,472円｜💰24.7万円｜—｜⚠日程不明
- 9699 NISHIO HOLDINGS CO. LTD.｜choruko_reversal｜⚠減速｜🟡やや割高｜PASS｜4,305円｜💰43.0万円｜reversal 4,305（✅即時可）｜⚠業績基調が下向き（減速）
  > 【業態】総合レンタルの草分け。関西地盤。建機レンタルで首位級。アジア、豪に積極展開。
  > 【いま】終値4,305円・直近5日+1.29%（材料未確認）
  > 【調子】⚠減速（0/13） — 質注意
  > 【水準】🟡やや割高（2.0/7）— PER9.64倍・PEG10.495・52週53.3% ／ 💰単元43.0万円
  > 【戦略】当日終値4,305円の指値で反転を取りにいく。SL4,200円（直近5日安値）
- 9533 TOHO GAS Co., Ltd.｜choruko_reversal｜🔻悪化｜🔴過熱｜PASS｜1,221.5円｜💰12.2万円｜reversal 1,221.5（✅即時可）｜⏰決算 10/29(残2営業日)｜⚠業績基調が下向き（悪化）
  > 【業態】都市ガス大手。愛知、岐阜、三重が拠点。LPGに強み。コージェネ事業に注力。
  > 【いま】終値1,221.5円・直近5日+3.04%（材料未確認）
  > 【調子】🔻悪化（0/13） — 質注意、経常減益-34.0%
  > 【水準】🔴過熱（1.0/7）— PER18.88倍・PEG—・52週43.1% ／ 💰単元12.2万円
  > 【戦略】当日終値1,221.5円の指値で反転を取りにいく。SL1,183.5円（直近5日安値）
- 8253 Credit Saison Co., Ltd.｜choruko_reversal｜取得不可｜💎割安｜FAIL_INSEN｜4,143円｜💰41.4万円｜—｜📋カルテ窓 11/13(残12営業日)
- 8370 紀陽銀行｜choruko_reversal｜取得不可｜💎割安｜PASS｜1,566円｜💰15.7万円｜reversal 1,566（✅即時可）
  > 【業態】未取得（次回以降に取得）
  > 【いま】終値1,566円・直近5日+1.36%（材料未確認）
  > 【調子】—（通期予想売上高(経常収益代替も含め)が非開示のためA/C軸を算出不可）
  > 【水準】💎割安（6.0/7）— PER4.04倍・PEG0.3087・52週70.5% ／ 💰単元15.7万円
  > 【戦略】当日終値1,566円の指値で反転を取りにいく。SL1,456円（直近5日安値）
- 5831 Shizuoka Financial Group, Inc.｜choruko_reversal/granville_rebound｜取得不可｜🟢値頃｜PASS｜3,030円｜💰30.3万円｜reversal 3,030（✅即時可）
  > 【業態】静岡地盤の地銀上位。地銀有数の収益力。業務範囲拡大。マネックスGの株主。
  > 【いま】終値3,030円・直近5日-0.10%（材料未確認）
  > 【調子】—（業績データ）
  > 【水準】🟢値頃（5.0/7）— PER13.76倍・PEG0.4885・52週59.4% ／ 💰単元30.3万円
  > 【戦略】当日終値3,030円の指値で反転を取りにいく。SL2,766.5円（直近5日安値）
- 7201 Nissan Motor Co., Ltd.｜choruko_reversal｜業績データ取得不可(経常益予想非開示)｜🟢値頃｜FAIL_INSEN｜262.29998779296875円｜💰2.7万円｜—｜📋カルテ窓 11/11(残10営業日)
- 7381 ＣＣＩグループ｜choruko_reversal/granville_rebound｜取得不可｜🟢値頃｜PASS｜1,115円｜💰11.2万円｜reversal 1,115（✅即時可）｜⏰決算 10/30(残3営業日)
  > 【業態】石川県を地盤。北國銀行を中核に総合金融サービス。富山県も重点。
  > 【いま】終値1,115円・直近5日-2.36%（材料未確認）
  > 【調子】—（業績データ）
  > 【水準】🟢値頃（5.0/7）— PER14.52倍・PEG0.4253・52週61.6% ／ 💰単元11.2万円
  > 【戦略】当日終値1,115円の指値で反転を取りにいく。SL1,032円（直近5日安値）
- 8304 あおぞら銀行｜choruko_reversal｜取得不可｜🟢値頃｜FAIL_INSEN｜3,007円｜💰29.5万円｜—｜📋カルテ窓 11/11(残10営業日)
- 8345 Bank of Iwate Ltd.｜choruko_reversal｜業績データ取得不可(売上/経常欠損)｜🟢値頃｜PASS｜2,116円｜💰21.2万円｜reversal 2,116（✅即時可）｜📋カルテ窓 11/12(残11営業日)
  > 【業態】岩手地盤の地銀中位。県内で圧倒的。青森銀、秋田銀と提携。リース、コンサルも。
  > 【いま】終値2,116円・直近5日-0.05%（材料未確認）
  > 【調子】—（業績データ(売上/経常欠損)）
  > 【水準】🟢値頃（5.0/7）— PER14.62倍・PEG1.1396・52週58.5% ／ 💰単元21.2万円
  > 【戦略】当日終値2,116円の指値で反転を取りにいく。SL1,897円（直近5日安値）
- 8367 南都銀行｜granville_oshime/choruko_reversal｜取得不可｜🟢値頃｜PASS｜1,762円｜💰17.6万円｜reversal 1,762（✅即時可）
  > 【業態】奈良地盤の地銀で県内シェアは圧倒的。効率経営に定評。中小企業に積極。
  > 【いま】終値1,762円・直近5日+0.17%（材料未確認）
  > 【調子】—（業績データ）
  > 【水準】🟢値頃（5.0/7）— PER12.58倍・PEG0.4065・52週68.2% ／ 💰単元17.6万円
  > 【戦略】当日終値1,762円の指値で反転を取りにいく。SL1,635円（直近5日安値）
- 3471 Mitsui Fudosan Logistics Park, Inc.｜choruko_reversal｜判定保留(変則決算)｜⚪妥当｜FAIL_INSEN｜99,000円｜💰10.0万円｜—｜⚠日程不明｜⚡材料後出し
- 7384 Procrea Holdings,Inc.｜granville_rebound/choruko_reversal｜業績データ取得不可(売上/経常欠損)｜⚪妥当｜PASS｜4,075円｜💰40.8万円｜reversal 4,075（✅即時可）｜⚠日程不明｜⚠1単元でリスク枠超過（46,000円）
  > 【業態】青森地盤の地銀。青森銀とみちのく銀が経営統合。25年1月に合併。
  > 【いま】終値4,075円・直近5日-0.73%（材料未確認）
  > 【調子】—（業績データ(売上/経常欠損)）
  > 【水準】⚪妥当（4.0/7）— PER16.48倍・PEG0.2279・52週55.1% ／ 💰単元40.8万円
  > 【戦略】当日終値4,075円の指値で反転を取りにいく。SL3,615円（直近5日安値）／⚠1単元リスク46,000円（枠超過）
- 8174 NIPPON GAS Co., Ltd.｜choruko_reversal｜業績データ取得不可｜⚪妥当｜PASS｜951.7000122070312円｜💰9.5万円｜reversal 951.7000122070312（✅即時可）｜⏰決算 10/29(残2営業日)
  > 【業態】LPG、都市ガス、電力を販売。関東一円展開。家庭エネ販売一元化。M&Aで拡販。
  > 【いま】終値951.7000122070312円・直近5日+1.51%（材料未確認）
  > 【調子】—（業績データ(売上予想非開示)）
  > 【水準】⚪妥当（4.0/7）— PER21.73倍・PEG—・52週39.4% ／ 💰単元9.5万円
  > 【戦略】当日終値951.7000122070312円の指値で反転を取りにいく。SL920円（直近5日安値）
- 8334 Gunma Bank, Ltd.｜granville_rebound/choruko_reversal｜取得不可｜⚪妥当｜PASS｜2,575円｜💰25.8万円｜reversal 2,575（✅即時可）
  > 【業態】群馬地盤の地銀上位。県内で圧倒的シェア。東京など近県を強化。海外も。
  > 【いま】終値2,575円・直近5日-1.70%（材料未確認）
  > 【調子】—（業績データ(売上予想なし)）
  > 【水準】⚪妥当（4.0/7）— PER15.00倍・PEG1.2587・52週61.3% ／ 💰単元25.8万円
  > 【戦略】当日終値2,575円の指値で反転を取りにいく。SL2,376円（直近5日安値）
- 8366 滋賀銀行｜granville_rebound/choruko_reversal｜取得不可｜⚪妥当｜PASS｜2,550円｜💰25.5万円｜reversal 2,550（✅即時可）｜📋カルテ窓 11/13(残12営業日)
  > 【業態】滋賀県内で優位。徹底した収益管理体制。環境関連の法人融資に注力。
  > 【いま】終値2,550円・直近5日-2.97%（材料未確認）
  > 【調子】—（業績データ）
  > 【水準】⚪妥当（4.0/7）— PER20.56倍・PEG0.4568・52週68.2% ／ 💰単元25.5万円
  > 【戦略】当日終値2,550円の指値で反転を取りにいく。SL2,370円（直近5日安値）
- 5344 MARUWA CO., LTD.｜choruko_reversal｜業績データ取得不可｜⚪妥当｜FAIL_INSEN｜47,000円｜💰465.6万円｜—｜⚠日程不明｜⚡材料後出し
- 8961 MORI TRUST REIT.Inc｜choruko_reversal｜判定保留(変則決算)｜🟡やや割高｜FAIL_INSEN｜67,400円｜💰6.8万円｜—｜⚠日程不明
- 3591 WACOAL HOLDINGS CORP｜choruko_reversal｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜3,629円｜💰36.2万円｜—｜📋カルテ窓 11/12(残11営業日)
- 8511 Japan Securities Finance Co., Ltd.｜choruko_reversal｜取得不可｜🟡やや割高｜FAIL_INSEN｜2,100円｜💰21.2万円｜—｜📋カルテ窓 11/12(残11営業日)
- 6471 日本精工｜choruko_reversal｜業績データ取得不可｜⏸判定不能｜PASS｜1,008円｜💰10.1万円｜reversal 1,008（✅即時可）｜⏰決算 10/29(残2営業日)
  > 【業態】ベアリング最大手。電動パワステ等自動車軸受、産機用展開。27年NTNと統合へ。
  > 【いま】終値1,008円・直近5日-0.49%（材料未確認）
  > 【調子】—（kabutan年次表を解析できず）
  > 【水準】⏸判定不能— PER—倍・PEG—・52週36.8% ／ 💰単元10.1万円
  > 【戦略】当日終値1,008円の指値で反転を取りにいく。SL955.5999755859375円（直近5日安値）
- 7186 横浜フィナンシャルグループ｜choruko_reversal｜業績データ取得不可｜⏸判定不能｜PASS｜1,660円｜💰16.6万円｜reversal 1,660（✅即時可）｜📋カルテ窓 11/11(残10営業日)
  > 【業態】傘下に横浜銀、東日本銀、神奈川銀。総合力に強み。中小企業、個人に注力。
  > 【いま】終値1,660円・直近5日-1.54%（材料未確認）
  > 【調子】—（kabutan年次表を解析できず）
  > 【水準】⏸判定不能— PER—倍・PEG—・52週63.4% ／ 💰単元16.6万円
  > 【戦略】当日終値1,660円の指値で反転を取りにいく。SL1,552.5円（直近5日安値）
- 7322 三十三フィナンシャルグループ｜choruko_reversal/granville_rebound｜業績データ取得不可｜⏸判定不能｜PASS｜1,838円｜💰18.4万円｜reversal 1,838（✅即時可）｜📋カルテ窓 11/13(残12営業日)
  > 【業態】三重県が地盤の三重銀行と第三銀行が経営統合。合併で三十三銀行へ。
  > 【いま】終値1,838円・直近5日-0.16%（材料未確認）
  > 【調子】—（kabutan年次表を解析できず）
  > 【水準】⏸判定不能— PER—倍・PEG—・52週66.0% ／ 💰単元18.4万円
  > 【戦略】当日終値1,838円の指値で反転を取りにいく。SL1,687円（直近5日安値）
- 8354 ふくおかフィナンシャルグループ｜choruko_reversal｜業績データ取得不可｜⏸判定不能｜PASS｜6,880円｜💰68.8万円｜reversal 6,880（✅即時可）｜⚠1単元でリスク枠超過（47,700円）
  > 【業態】傘下に福岡・熊本・十八親和など。総資産は地銀首位級。ネット銀行設立。
  > 【いま】終値6,880円・直近5日-1.08%（材料未確認）
  > 【調子】—（kabutan年次表を解析できず）
  > 【水準】⏸判定不能— PER—倍・PEG—・52週68.2% ／ 💰単元68.8万円
  > 【戦略】当日終値6,880円の指値で反転を取りにいく。SL6,403円（直近5日安値）／⚠1単元リスク47,700円（枠超過）
- 8359 Hachijuni Nagano Bank, Ltd.｜choruko_reversal｜業績データ取得不可｜⏸判定不能｜PASS｜2,403円｜💰24.0万円｜reversal 2,403（✅即時可）
  > 【業態】長野地盤の地銀上位。県全域にシェア圧倒的。堅実経営。長野銀と合併。
  > 【いま】終値2,403円・直近5日-0.74%（材料未確認）
  > 【調子】—（kabutan年次表を解析できず）
  > 【水準】⏸判定不能— PER—倍・PEG—・52週65.0% ／ 💰単元24.0万円
  > 【戦略】当日終値2,403円の指値で反転を取りにいく。SL2,236円（直近5日安値）
- 8600 トモニホールディングス｜choruko_reversal｜業績データ取得不可｜⏸判定不能｜PASS｜1,038円｜💰10.4万円｜reversal 1,038（✅即時可）｜📋カルテ窓 11/13(残12営業日)
  > 【業態】傘下に香川銀と徳島大正銀。大阪や東京等店舗広域化。中小企業に注力。
  > 【いま】終値1,038円・直近5日-0.67%（材料未確認）
  > 【調子】—（kabutan年次表を解析できず）
  > 【水準】⏸判定不能— PER—倍・PEG—・52週65.4% ／ 💰単元10.4万円
  > 【戦略】当日終値1,038円の指値で反転を取りにいく。SL969円（直近5日安値）
- 6668 ＡＤプラズマ｜stf_kakuhen/granville_oshime｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜4,800円｜💰47.2万円｜—｜⚠日程不明
- 7624 NaITO｜stf_kakuhen｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜164円｜💰1.6万円｜—｜⚠日程不明
- 7713 シグマ光機｜stf_kakuhen｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜3,215円｜💰32.9万円｜—｜⚠日程不明
- 5018 ＭＯＲＥＳＣＯ｜stf_kakuhen｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜2,891円｜💰29.1万円｜—｜⚠日程不明
- 5246 ＥＬＥＭＥＮＴＳ｜granville_oshime/stf_kakuhen｜🔥絶好調｜⚪妥当｜PASS｜1,100円｜💰11.0万円｜⛔提案なし(手法ブランチ不明)｜⚠日程不明
  > 【業態】生体認証・画像解析・機械学習技術を活用したオンライン本人確認サービスを展開。
  > 【いま】終値1,100円・直近5日+1.38%（材料未確認）
  > 【調子】🔥絶好調（10/13） — 赤字→黒字転換
  > 【水準】⚪妥当（4.0/7）— PER100.00倍・PEG0.5008・52週72.4% ／ 💰単元11.0万円
  > 【戦略】発注対象外（⛔提案なし(手法ブランチ不明)）
- 3498 霞ヶ関Ｃ｜stf_kakuhen｜🔥絶好調｜💎割安｜FAIL_INSEN｜7,180円｜💰70.9万円｜—｜⚠日程不明
- 3994 マネーフォワード｜stf_kakuhen｜🔥絶好調｜🔴過熱｜FAIL_INSEN｜6,690円｜💰67.5万円｜—｜⚠日程不明
- 7811 中本パックス｜granville_oshime/stf_kakuhen｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜2,527円｜💰26.6万円｜—｜⚠日程不明
- 4443 Ｓａｎｓａｎ｜stf_kakuhen/changepoint🔔🔔｜🔥絶好調｜⚪妥当｜PASS｜2,173円｜💰21.7万円｜⛔提案なし(手法ブランチ不明)｜⚠日程不明
  > 【業態】名刺管理サービス最大手。法人向けクラウド、個人向けアプリ展開。請求書データも。
  > 【いま】終値2,173円・直近5日+4.77%（材料未確認）
  > 【調子】🔥絶好調（8/13）
  > 【水準】⚪妥当（3.0/7）— PER29.33倍・PEG0.4438・52週86.6% ／ 💰単元21.7万円
  > 【戦略】発注対象外（⛔提案なし(手法ブランチ不明)）
- 6814 古野電｜stf_kakuhen｜⚡好調｜🟢値頃｜PASS｜7,910円｜💰79.1万円｜⛔提案なし(手法ブランチ不明)｜⚠日程不明
  > 【業態】魚群探知機など船舶用電子機器で世界高シェア。GPSや医療機器も積極展開。
  > 【いま】終値7,910円・直近5日-4.81%（材料未確認）
  > 【調子】⚡好調（7/13） — 上方修正済み
  > 【水準】🟢値頃（5.0/7）— PER14.71倍・PEG0.7253・52週53.6% ／ 💰単元79.1万円
  > 【戦略】発注対象外（⛔提案なし(手法ブランチ不明)）
- 5932 三協立山｜stf_kakuhen｜⚡好調｜⚪妥当｜FAIL_INSEN｜741円｜💰7.7万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）
- 3091 ブロンコビリー｜changepoint/changepoint🔔🔔/stf_kakuhen｜⚡好調｜🟡やや割高｜FAIL_INSEN｜3,120円｜💰31.6万円｜—｜⚠日程不明
- 3479 ＴＫＰ｜stf_kakuhen/granville_tenkan｜⚡好調｜🔴過熱｜FAIL_INSEN｜1,946円｜💰19.7万円｜—｜⚠日程不明
- 6505 東洋電機製造｜ai_momentum/stf_kakuhen｜⚡好調｜⚪妥当｜FAIL_INSEN｜3,020円｜💰30.8万円｜—｜⚠日程不明
- 6532 ベイカレント｜stf_kakuhen｜⚡好調｜🟡やや割高｜FAIL_UWAHIGE｜11,625円｜💰115.0万円｜—｜⚠日程不明
- 4176 ココナラ｜stf_kakuhen｜✅順調｜🟢値頃｜FAIL_INSEN｜305円｜💰3.1万円｜—｜⚠日程不明

## グランビル銘柄
- 5254 Arent, Inc.｜granville_tenkan｜🚀確変｜⚪妥当｜PASS｜3,870円｜💰38.7万円｜momentum 3,880（✅即時可）｜📋カルテ窓 11/12(残11営業日)
  > 【業態】建設・プラント業界を中心にDXコンサルティング、システム開発、システム販売。自社製品も。
  > 【いま】終値3,870円・直近5日-3.49%（材料未確認）
  > 【調子】🚀確変（12/13）
  > 【水準】⚪妥当（4.0/7）— PER26.06倍・PEG0.3184・52週63.8% ／ 💰単元38.7万円
  > 【戦略】当日高値超えの逆指値3,880円で順張り参戦を検討。上限3,918.8円・SL3,642.5円目安
- 3927 アークン｜granville_tenkan｜🚀確変｜⚪妥当｜PASS｜1,058円｜💰10.6万円｜momentum 1,076（✅即時可）｜📋カルテ窓 11/13(残12営業日)
  > 【業態】情報セキュリティ製品の開発・販売・保守。中小企業向けの業務システムに注力。
  > 【いま】終値1,058円・直近5日+3.73%（材料未確認）
  > 【調子】🚀確変（11/13） — 進捗モデル値域外
  > 【水準】⚪妥当（4.0/7）— PER17.20倍・PEG0.164・52週46.0% ／ 💰単元10.6万円
  > 【戦略】当日高値超えの逆指値1,076円で順張り参戦を検討。上限1,086.8円・SL1,010.5円目安
- 8944 Land Business Co., Ltd.｜granville_tenkan｜🔥絶好調｜💎割安｜FAIL_INSEN｜252円｜💰2.5万円｜—｜📋カルテ窓 11/13(残12営業日)
- 6905 Cosel Co., Ltd.｜granville_tenkan｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1,287円｜💰12.9万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）
- 9553 MicroAd, Inc.｜granville_tenkan｜🔥絶好調｜🟢値頃｜PASS｜577円｜💰5.8万円｜momentum 580（✅即時可）｜📋カルテ窓 11/13(残12営業日)
  > 【業態】データとテクノロジー活用でマーケティングプラットフォーム事業。広告コンサル、サイネージ配信も。
  > 【いま】終値577円・直近5日-1.70%（材料未確認）
  > 【調子】🔥絶好調（10/13） — 上方修正済み、進捗81%(前年同期87%・3Q累計・経常ベース)
  > 【水準】🟢値頃（5.0/7）— PER22.54倍・PEG0.2843・52週29.8% ／ 💰単元5.8万円
  > 【戦略】当日高値超えの逆指値580円で順張り参戦を検討。上限585.8円・SL544.3円目安
- 7725 INTER ACTION Corporation｜granville_tenkan｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜1,788円｜💰17.6万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）
- 2986 LA Holdings Co.,Ltd｜granville_tenkan｜🔥絶好調｜💎割安｜FAIL_INSEN｜2,669円｜💰26.9万円｜—｜📋カルテ窓 11/12(残11営業日)
- 9211 f-code Inc.｜granville_tenkan/changepoint🔔｜🔥絶好調｜💎割安｜FAIL_INSEN｜1,180円｜💰11.7万円｜—｜📋カルテ窓 11/13(残12営業日)
- 6562 Geniee, Inc.｜granville_tenkan｜🔥絶好調｜💎割安｜FAIL_INSEN｜901円｜💰9.1万円｜—｜📋カルテ窓 11/13(残12営業日)
- 6473 JTEKT Corporation｜granville_tenkan｜⚠減速｜🟢値頃｜FAIL_INSEN｜2,054.5円｜💰20.4万円｜—｜⏰決算 10/29(残2営業日)
- 8697 日本取引所グループ｜granville_tenkan/changepoint🔔/changepoint｜🔥絶好調｜🟡やや割高｜FAIL_INSEN｜2,088円｜💰22.2万円｜—｜⚠日程不明
- 3496 アズーム｜granville_tenkan｜⚡好調｜🟢値頃｜PASS｜4,805円｜💰48.0万円｜momentum 4,810（✅即時可）｜📋カルテ窓 11/12(残11営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
  > 【業態】ビル駐車場のサブリースを展開。月極駐車場ポータルサイト「CarParking」運営も。
  > 【いま】終値4,805円・直近5日-0.83%（材料未確認）
  > 【調子】⚡好調（7/13）
  > 【水準】🟢値頃（5.0/7）— PER26.93倍・PEG1.3174・52週38.4% ／ 💰単元48.0万円
  > 【戦略】当日高値超えの逆指値4,810円で順張り参戦を検討。上限4,858.1円・SL4,516.7円目安
- 4534 Mochida Pharmaceutical Co., Ltd.｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_INSEN｜3,250円｜💰32.9万円｜—
- 6255 NPC Incorporated｜granville_tenkan｜⚡好調｜🟢値頃｜PASS｜655円｜💰6.5万円｜momentum 659（✅即時可）｜⚠日程不明
  > 【業態】太陽電池製造装置大手。パネル解体装置やFA装置も展開。植物工場も。
  > 【いま】終値655円・直近5日-1.80%（材料未確認）
  > 【調子】⚡好調（7/13）
  > 【水準】🟢値頃（5.0/7）— PER16.62倍・PEG0.2724・52週27.7% ／ 💰単元6.5万円
  > 【戦略】当日高値超えの逆指値659円で順張り参戦を検討。上限665.6円・SL618.5円目安
- 8793 ＮＥＣキャピタルソリューション｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜4,075円｜💰40.8万円｜—｜⏰決算 10/30(残3営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 3405 クラレ｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜1,849円｜💰18.1万円｜—｜📋カルテ窓 11/11(残10営業日)
- 7744 Noritsu Koki Co., Ltd.｜granville_tenkan｜⚡好調｜⚪妥当｜PASS｜2,147円｜💰21.5万円｜momentum 2,152（✅即時可）｜📋カルテ窓 11/13(残12営業日)
  > 【業態】ペン先等金属加工部材からDJ・音響関連機事業が主軸に。金属部品、建材も。
  > 【いま】終値2,147円・直近5日+3.87%（材料未確認）
  > 【調子】⚡好調（7/13） — 質注意
  > 【水準】⚪妥当（4.0/7）— PER13.55倍・PEG1.1215・52週72.2% ／ 💰単元21.5万円
  > 【戦略】当日高値超えの逆指値2,152円で順張り参戦を検討。上限2,173.5円・SL2,021.9円目安
- 8095 Astena Holdings Co.,Ltd.｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜535円｜💰5.3万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）
- 9064 ヤマトホールディングス｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,005円｜💰20.5万円｜—｜⏰決算 11/04(残5営業日)
- 3741 Systems Engineering Consultants Co., Ltd.｜granville_tenkan｜⚡好調｜⚪妥当｜PASS｜3,050円｜💰30.5万円｜⛔提案なし(指名鮮度切れ 14営業日)｜📋カルテ窓 11/12(残11営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
  > 【業態】システム開発。リアルタイムソフトウエア技術に強み。モバイル決済や宇宙、ロボット関連など。
  > 【いま】終値3,050円・直近5日+3.39%（材料未確認）
  > 【調子】⚡好調（7/13） — 進捗22%(前年同期16%・1Q累計・経常ベース)
  > 【水準】⚪妥当（3.0/7）— PER19.77倍・PEG1.7126・52週31.4% ／ 💰単元30.5万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 14営業日)）
- 4544 H.U.Group Holdings, Inc.｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜3,795円｜💰37.4万円｜—｜📋カルテ窓 11/11(残10営業日)
- 5838 Rakuten Bank, Ltd.｜granville_tenkan｜⚡好調｜💎割安｜FAIL_INSEN｜5,738円｜💰58.1万円｜—｜📋カルテ窓 11/11(残10営業日)
- 4763 クリーク・アンド・リバー社｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_INSEN｜1,463円｜💰15.0万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）
- 6470 Taiho Kogyo Co., Ltd.｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜1,100円｜💰11.2万円｜—｜🚨決算直前 10/28(残1営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 7199 プレミアグループ｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,116円｜💰21.6万円｜—
- 4848 フルキャストホールディングス｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜1,851円｜💰18.4万円｜—｜📑TOPIX低減対象（次 10/30 第1回/8）｜⚡材料後出し
- 3935 Edia Co. Ltd.｜granville_tenkan｜⚡好調｜💎割安｜FAIL_INSEN｜704円｜💰7.2万円｜—｜⚠日程不明
- 6196 Strike Group Co. Ltd.｜granville_tenkan｜⚡好調｜💎割安｜FAIL_INSEN｜1,404円｜💰14.3万円｜—｜⏰決算 10/30(残3営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 6768 Tamura Corporation｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_INSEN｜834円｜💰8.2万円｜—
- 3562 No.1 Co., Ltd.｜granville_tenkan｜⚡好調｜🟢値頃｜PASS｜1,669円｜💰16.7万円｜⛔提案なし(材料後出し)｜⚠日程不明｜⚡材料後出し
  > 【業態】情報セキュリティ機器の開発・販売を展開。経営・IT支援などビジネスサポートに注力。
  > 【いま】終値1,669円・直近5日+1.58%・📌当社の幹部の人事に関するお知らせ
  > 【調子】⚡好調（5/13）
  > 【水準】🟢値頃（5.0/7）— PER11.25倍・PEG0.7958・52週22.0% ／ 💰単元16.7万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 8061 Seika Corporation｜granville_tenkan｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜2,977円｜💰29.2万円｜—
- 2331 ALSOK CO., LTD.｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜1,227円｜💰12.2万円｜—
- 4169 Enechange Ltd.｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜264円｜💰2.6万円｜—
- 4568 第一三共｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜2,594.5円｜💰28.2万円｜—｜⏰決算 10/30(残3営業日)
- 3661 m-up holdings, Inc.｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜886円｜💰8.9万円｜—｜📋カルテ窓 11/13(残12営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 6432 竹内製作所｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_INSEN｜7,780円｜💰79.9万円｜—｜⚠日程不明
- 7970 Shin-Etsu Polymer Co., Ltd.｜granville_tenkan｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜2,505円｜💰22.5万円｜—｜⚠日程不明
- 8020 Kanematsu Corporation｜granville_tenkan｜⚡好調｜🟡やや割高｜PASS｜2,378円｜💰23.8万円｜⛔提案なし(指名鮮度切れ 12営業日)
  > 【業態】総合商社から専門商社にシフト。電子、食糧、鉄鋼・プラント、車両・航空が柱。
  > 【いま】終値2,378円・直近5日+3.64%（材料未確認）
  > 【調子】⚡好調（5/13）
  > 【水準】🟡やや割高（2.0/7）— PER11.31倍・PEG1.8756・52週90.6% ／ 💰単元23.8万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 12営業日)）
- 9828 Genki Global Dining Concepts Corp｜granville_tenkan｜⚡好調｜🔴過熱｜FAIL_INSEN｜3,415円｜💰35.3万円｜—｜⏰決算 10/30(残3営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 6454 Max Co., Ltd.｜granville_tenkan｜⚡好調｜🔴過熱｜FAIL_UWAHIGE｜1,958円｜💰19.1万円｜—｜⏰決算 10/29(残2営業日)
- 2288 Marudai Food Co., Ltd.｜granville_tenkan｜✅順調｜🟢値頃｜FAIL_INSEN｜2,080円｜💰22.0万円｜—｜📑TOPIX低減対象（次 10/30 第1回/8）
- 5036 Japan Business Systems, Inc.｜granville_tenkan｜✅順調｜⚪妥当｜FAIL_UWAHIGE｜1,887円｜💰19.0万円｜—｜📋カルテ窓 11/12(残11営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 8014 Chori Co., Ltd.｜granville_tenkan｜✅順調｜⚪妥当｜FAIL_UWAHIGE｜4,310円｜💰42.9万円｜—｜⏰決算 10/30(残3営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 4549 Eiken Chemical Co., Ltd.｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_UWAHIGE｜2,418円｜💰24.2万円｜—｜⏰決算 10/29(残2営業日)
- 5184 ニチリン｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_INSEN｜4,175円｜💰41.5万円｜—｜📋カルテ窓 11/11(残10営業日)
- 6592 Mabuchi Motor Co., Ltd.｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_INSEN｜1,754.5円｜💰17.2万円｜—｜⚠日程不明
- 6988 日東電工｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_INSEN｜3,600円｜💰36.1万円｜—｜⚠日程不明｜⚡材料後出し
- 6371 Tsubakimoto Chain Co.｜granville_tenkan｜✅順調｜🔴過熱｜FAIL_UWAHIGE｜2,708円｜💰27.0万円｜—｜⏰決算 10/30(残3営業日)
- 4166 Cacco, Inc.｜granville_tenkan｜✅順調｜🟢値頃｜FAIL_INSEN｜803円｜💰7.7万円｜—｜📋カルテ窓 11/13(残12営業日)
- 8850 スターツコーポレーション｜granville_tenkan｜✅順調｜⚪妥当｜FAIL_INSEN｜4,580円｜💰46.5万円｜—
- 9163 Nareru Group Inc.｜granville_tenkan｜✅順調｜⚪妥当｜FAIL_INSEN｜2,340円｜💰23.4万円｜—｜⚠日程不明
- 8927 Meiho Enterprise Co., Ltd.｜granville_tenkan｜✅順調｜⚪妥当｜FAIL_INSEN｜476円｜💰4.9万円｜—｜⚠日程不明
- 186A Astroscale Holdings Inc.｜granville_tenkan｜✅順調｜🟡やや割高｜PASS｜1,077円｜💰10.8万円｜momentum 1,084（✅即時可）｜⚠日程不明｜📑TOPIX新規採用（2026-10-30 組入）
  > 【業態】宇宙ごみ(スペースデブリ)除去や人工衛星寿命延長などのサービスを手掛ける。
  > 【いま】終値1,077円・直近5日+6.42%（材料未確認）
  > 【調子】✅順調（3/13） — 赤字ルート(B'=赤字縮小率/C'=営業益トレンドで代替)
  > 【水準】🟡やや割高（2.8/7）— PER—倍・PEG—・52週20.6% ／ 💰単元10.8万円
  > 【戦略】当日高値超えの逆指値1,084円で順張り参戦を検討。上限1,094.8円・SL1,018円目安
- 3569 セーレン｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_INSEN｜3,400円｜💰32.9万円｜—
- 4183 Mitsui Chemicals, Inc.｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_INSEN｜2,102.5円｜💰20.9万円｜—｜📋カルテ窓 11/11(残10営業日)
- 4272 Nippon Kayaku Co., Ltd.｜granville_tenkan｜✅順調｜🟡やや割高｜PASS｜2,058.5円｜💰20.6万円｜momentum 2,065（✅即時可）
  > 【業態】火薬から機能化学品など多角化。医薬、自動車部材等。抗がん剤に強み。(化学)
  > 【いま】終値2,058.5円・直近5日-3.31%（材料未確認）
  > 【調子】✅順調（3/13） — D軸簡易判定(四半期詳細なしのため中立値)、(質注意)
  > 【水準】🟡やや割高（2.0/7）— PER12.95倍・PEG2.1686・52週83.5% ／ 💰単元20.6万円
  > 【戦略】当日高値超えの逆指値2,065円で順張り参戦を検討。上限2,085.7円・SL1,940.2円目安
- 4956 Konishi Co., Ltd.｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_UWAHIGE｜1,508円｜💰15.2万円｜—｜🚨決算直前 10/28(残1営業日)
- 5461 Chubu Steel Plate Co., Ltd.｜granville_tenkan｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜2,202円｜💰21.7万円｜—｜📑TOPIX低減対象（次 10/30 第1回/8）
- 7181 JAPAN POST INSURANCE Co., Ltd.｜granville_tenkan｜⚠減速｜🔴過熱｜PASS｜1,732.5円｜💰17.3万円｜⛔提案なし(指名鮮度切れ 17営業日)｜📋カルテ窓 11/13(残12営業日)｜⚠業績基調が下向き（減速）
  > 【業態】日本最大の生命保険会社。小口、簡易保険に強み。第一生命と提携。
  > 【いま】終値1,732.5円・直近5日+3.68%（材料未確認）
  > 【調子】⚠減速（3/13） — 減収、質注意
  > 【水準】🔴過熱（2.0/7）— PER13.32倍・PEG—・52週79.8% ／ 💰単元17.3万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 17営業日)）
- 7734 Riken Keiki Co., Ltd.｜granville_tenkan｜✅順調｜🟡やや割高｜FAIL_INSEN｜3,460円｜💰33.7万円｜—｜📋カルテ窓 11/12(残11営業日)
- 8012 Nagase & Co., Ltd.｜granville_tenkan｜✅順調｜🔴過熱｜PASS｜1,217円｜💰12.2万円｜momentum 1,220（✅即時可）｜📐進捗 上振れ 53.3%
  > 【業態】染料、合成樹脂化学の専門商社最大手。医薬品原料に強み。海外を拡大。
  > 【いま】終値1,217円・直近5日+2.70%（材料未確認）
  > 【調子】✅順調（3/13）
  > 【水準】🔴過熱（1.0/7）— PER14.30倍・PEG6.9758・52週81.3% ／ 💰単元12.2万円
  > 【戦略】当日高値超えの逆指値1,220円で順張り参戦を検討。上限1,232.2円・SL1,145.9円目安
- 7513 Kojima Co., Ltd.｜granville_tenkan｜✅順調｜🔴過熱｜FAIL_INSEN｜1,385円｜💰14.2万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）
- 4617 中国塗料｜granville_tenkan｜➖横ばい｜⚪妥当｜PASS｜3,550円｜💰35.5万円｜momentum 3,595（✅即時可）｜⏰決算 10/30(残3営業日)
  > 【業態】船舶用塗料の世界大手。工業用塗料も展開。アジアを中心に海外販売網。
  > 【いま】終値3,550円・直近5日-1.80%（材料未確認）
  > 【調子】➖横ばい（2/13） — 質注意
  > 【水準】⚪妥当（3.0/7）— PER16.03倍・PEG17.8702・52週34.1% ／ 💰単元35.5万円
  > 【戦略】当日高値超えの逆指値3,595円で順張り参戦を検討。上限3,630.9円・SL3,374.6円目安
- 6328 Ebara Jitsugyo Co., Ltd.｜granville_tenkan｜➖横ばい｜⚪妥当｜PASS｜2,470円｜💰24.7万円｜momentum 2,477（✅即時可）｜📑TOPIX低減対象（次 10/30 第1回/8）
  > 【業態】上下水処理施設から空調など環境関連事業に拡大。研究開発・ファブレス型。
  > 【いま】終値2,470円・直近5日+1.60%（材料未確認）
  > 【調子】➖横ばい（2/13） — 質注意
  > 【水準】⚪妥当（3.0/7）— PER12.90倍・PEG4.4298・52週47.0% ／ 💰単元24.7万円
  > 【戦略】当日高値超えの逆指値2,477円で順張り参戦を検討。上限2,501.8円・SL2,327.4円目安
- 4552 JCR Pharmaceuticals Co., Ltd.｜granville_tenkan｜🔻悪化｜🔴過熱｜FAIL_INSEN｜510円｜💰5.2万円｜—｜⏰決算 10/29(残2営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 6208 Ishikawa Seisakusho,Ltd.｜granville_tenkan｜🔻悪化｜🟡やや割高｜FAIL_UWAHIGE｜1,633円｜💰16.6万円｜—
- 8081 Kanaden Corporation｜granville_tenkan｜➖横ばい｜🟡やや割高｜FAIL_INSEN｜2,579円｜💰26.0万円｜—｜⏰決算 11/04(残5営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 9837 Morito Co., Ltd.｜granville_tenkan｜➖横ばい｜🟡やや割高｜FAIL_INSEN｜1,811円｜💰18.2万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）
- 7751 キヤノン｜granville_tenkan｜➖横ばい｜🔴過熱｜FAIL_INSEN｜4,904円｜💰48.2万円｜—｜⚠日程不明｜⚡材料後出し
- 4902 Konica Minolta, Inc.｜granville_tenkan｜⚠減速｜⚪妥当｜PASS｜690.5999755859375円｜💰6.9万円｜momentum 691.5999755859375（✅即時可）｜⚠業績基調が下向き（減速）
  > 【業態】複合機中堅で印刷関連を展開。液晶TACフィルムで世界高シェア。X線撮影装置も。
  > 【いま】終値690.5999755859375円・直近5日+6.26%（材料未確認）
  > 【調子】⚠減速（1/13） — 質注意、経常非開示(IFRS等)のため最終益成長率で代替、経常減益-5.8%
  > 【水準】⚪妥当（4.0/7）— PER11.99倍・PEG—・52週82.1% ／ 💰単元6.9万円
  > 【戦略】当日高値超えの逆指値691.5999755859375円で順張り参戦を検討。上限698.5円・SL649.2円目安
- 6770 Alps Alpine Co., Ltd.｜granville_tenkan｜⚠減速｜⚪妥当｜FAIL_INSEN｜2,084.5円｜💰20.5万円｜—｜⏰決算 10/30(残3営業日)
- 5105 ＴＯＹＯ　ＴＩＲＥ｜granville_tenkan｜⚠減速｜🟡やや割高｜PASS｜4,059円｜💰40.6万円｜momentum 4,064（✅即時可）｜📋カルテ窓 11/16(残13営業日)｜⚠業績基調が下向き（減速）
  > 【業態】タイヤ大手。トラック・バス用に強み。北米向けSUV用タイヤも。株主に三菱商事。
  > 【いま】終値4,059円・直近5日-1.60%（材料未確認）
  > 【調子】⚠減速（1/13） — 進捗データなし(判定不能)、(質注意)
  > 【水準】🟡やや割高（2.0/7）— PER8.06倍・PEG—・52週44.3% ／ 💰単元40.6万円
  > 【戦略】当日高値超えの逆指値4,064円で順張り参戦を検討。上限4,104.6円・SL3,815.5円目安
- 8167 リテールパートナーズ｜granville_tenkan｜⚠減速｜🟡やや割高｜FAIL_INSEN｜1,398円｜💰14.1万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）
- 1815 鉄建建設｜granville_tenkan｜⚠減速｜⚪妥当｜FAIL_INSEN｜2,154円｜💰21.8万円｜—｜📋カルテ窓 11/13(残12営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 4375 セーフィー｜granville_tenkan/changepoint🔔｜取得不可｜💎割安｜FAIL_INSEN｜657円｜💰6.6万円｜—｜⚠日程不明
- 8424 芙蓉総合リース｜granville_tenkan｜取得不可｜💎割安｜FAIL_INSEN｜4,306円｜💰43.2万円｜—
- 4912 ライオン｜granville_tenkan｜業績データ取得不可(経常益予想非開示)｜⚪妥当｜FAIL_INSEN｜1,829円｜💰17.7万円｜—
- 2871 ニチレイ｜granville_tenkan｜業績データ取得不可｜🔴過熱｜FAIL_INSEN｜2,172円｜💰21.9万円｜—
- 5233 太平洋セメント｜granville_tenkan｜—｜－未評価｜FAIL_UWAHIGE｜4,184円｜—｜—
- 7747 朝日インテック｜granville_tenkan｜—｜－未評価｜FAIL_UWAHIGE｜3,678円｜—｜—｜📋カルテ窓 11/13(残12営業日)
- 7921 ＴＡＫＡＲＡ　＆　ＣＯＭＰＡＮＹ｜granville_tenkan｜—｜－未評価｜FAIL_INSEN｜4,170円｜—｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）｜⚡材料後出し
- 4937 Ｇ−ＷＡＱＯＯ｜granville_oshime｜🚀確変｜⚪妥当｜FAIL_INSEN｜2,280円｜💰23.5万円｜—｜📋カルテ窓 11/12(残11営業日)
- 290A ＳＹＮＳＰＥＣＴＩＶＥ｜granville_oshime｜🚀確変｜🟢値頃｜PASS｜1,176円｜💰11.8万円｜⛔提案なし(指名鮮度切れ 16営業日)｜📋カルテ窓 11/13(残12営業日)｜📑TOPIX新規採用（2026-10-30 組入）
  > 【業態】小型SAR衛星の開発・運用から地球観測データの販売とソリューションを提供。
  > 【いま】終値1,176円・直近5日+3.07%（材料未確認）
  > 【調子】🚀確変（11/13） — 赤字→黒字転換
  > 【水準】🟢値頃（5.0/7）— PER60.31倍・PEG0.1586・52週23.1% ／ 💰単元11.8万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 16営業日)）
- 5243 ｎｏｔｅ｜granville_oshime/granville_rebound｜🚀確変｜⚪妥当｜FAIL_UWAHIGE｜2,877円｜💰27.8万円｜—｜⚠日程不明｜⚡材料後出し
- 7806 MTG Co., Ltd.｜granville_oshime/changepoint🔔｜🚀確変｜⚪妥当｜FAIL_UWAHIGE｜8,980円｜💰86.2万円｜—｜📋カルテ窓 11/11(残10営業日)｜📑TOPIX新規採用（2026-10-30 組入）
- 6834 Seikoh Giken Co., Ltd.｜granville_oshime/granville_rebound｜🔥絶好調｜💎割安｜FAIL_INSEN｜5,540円｜💰52.7万円｜—｜📋カルテ窓 11/13(残12営業日)｜📑TOPIX新規採用（2026-10-30 組入）
- 6613 QD Laser, Inc.｜granville_oshime｜🔥絶好調｜🔴過熱｜FAIL_UWAHIGE｜2,219円｜💰20.0万円｜—｜📋カルテ窓 11/12(残11営業日)｜📑TOPIX新規採用（2026-10-30 組入）
- 8008 Yondoshi Holdings, Inc.｜granville_oshime｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜1,998円｜💰20.3万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）
- 3156 レスター｜granville_oshime｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜6,250円｜💰60.4万円｜—｜📋カルテ窓 11/13(残12営業日)
- 4180 ＡＰＰＩＥＲ　ＧＲＯＵＰ｜changepoint🔔/granville_oshime/changepoint🔔🔔｜🔥絶好調｜⚪妥当｜PASS｜1,444円｜💰14.4万円｜oshime 1,418.3（✅即時可）｜📋カルテ窓 11/13(残12営業日)｜🔒実弾封印中(PL3紙ログ収集中)
  > 【業態】企業の販促など経営課題の解決を支援するAI搭載のプラットフォームを提供。
  > 【いま】終値1,444円・直近5日+4.71%（材料未確認）
  > 【調子】🔥絶好調（8/13）
  > 【水準】⚪妥当（3.0/7）— PER35.74倍・PEG0.581・52週88.1% ／ 💰単元14.4万円
  > 【戦略】1,418.3円までの押し目を指値で待つ。SL1,411.2円（25日線基準）
- 4431 スマレジ｜changepoint/変化点🔔🔔/changepoint🔔/granville_oshime｜🔥絶好調｜🟡やや割高｜PASS｜3,760円｜💰37.6万円｜oshime 3,690.6（✅即時可）｜⚠日程不明
  > 【業態】小売店クラウド型POSレジ・スマホアプリ「スマレジ」開発販売。中小事業社需要に注力。
  > 【いま】終値3,760円・直近5日-1.96%（材料未確認）
  > 【調子】🔥絶好調（8/13）
  > 【水準】🟡やや割高（2.0/7）— PER26.06倍・PEG1.0149・52週82.5% ／ 💰単元37.6万円
  > 【戦略】3,690.6円までの押し目を指値で待つ。SL3,672.2円（25日線基準）
- 7856 HAGIHARA INDUSTRIES INC.｜granville_oshime｜🔥絶好調｜🟡やや割高｜FAIL_INSEN｜2,007円｜💰20.1万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）
- 1879 新日本建設｜granville_oshime｜⚡好調｜💎割安｜FAIL_INSEN｜2,172円｜💰21.9万円｜—｜📋カルテ窓 11/12(残11営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 6736 Suncorporation｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_INSEN｜9,850円｜💰98.6万円｜—｜📋カルテ窓 11/13(残12営業日)｜📑TOPIX新規採用（2026-10-30 組入）
- 9902 Nichiden Corporation｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜3,175円｜💰31.2万円｜—｜📑TOPIX低減対象（次 10/30 第1回/8）
- 6023 ダイハツインフィニアース｜granville_oshime/granville_rebound｜⚡好調｜🟢値頃｜PASS｜2,889円｜💰28.9万円｜⛔型不一致: 既に支持帯以下｜🚨決算直前 10/28(残1営業日)
  > 【業態】船舶ディーゼル発電用補機の世界大手。コージェネ向けも。ダイハツ直系。
  > 【いま】終値2,889円・直近5日+0.14%（材料未確認）
  > 【調子】⚡好調（6/13）
  > 【水準】🟢値頃（5.0/7）— PER10.36倍・PEG0.4041・52週59.0% ／ 💰単元28.9万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 6523 PHC Holdings Corp.｜granville_oshime｜⚠減速｜🟢値頃｜FAIL_UWAHIGE｜1,343円｜💰12.6万円｜—｜📋カルテ窓 11/11(残10営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 7609 ダイトロン｜granville_oshime｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜4,255円｜💰41.2万円｜—｜⏰決算 11/04(残5営業日)
- 3106 倉敷紡績｜granville_oshime｜⚡好調｜⚪妥当｜PASS｜2,399円｜💰24.0万円｜⛔型不一致: 既に支持帯以下｜📋カルテ窓 11/12(残11営業日)
  > 【業態】綿紡大手。ジーンズ等厚手が主。車内装材など非繊維拡大。FA・産業装置も。
  > 【いま】終値2,399円・直近5日+3.45%（材料未確認）
  > 【調子】⚡好調（6/13） — D軸判定不能(四半期データ不足・中立1点)
  > 【水準】⚪妥当（4.2/7）— PER12.73倍・PEG0.6324・52週85.1% ／ 💰単元24.0万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 2767 円谷フィールズホールディングス｜granville_oshime｜⚡好調｜⚪妥当｜PASS｜2,488円｜💰24.9万円｜⛔提案なし(指名鮮度切れ 11営業日)
  > 【業態】遊技機販売大手。企画開発、版権ビジネス展開。円谷プロで映像・コンテンツも。
  > 【いま】終値2,488円・直近5日-1.47%（材料未確認）
  > 【調子】⚡好調（6/13）
  > 【水準】⚪妥当（4.0/7）— PER10.32倍・PEG0.3741・52週86.1% ／ 💰単元24.9万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 11営業日)）
- 4667 Aisan Technology Co., Ltd.｜granville_oshime/changepoint🔔/changepoint｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜960円｜💰9.4万円｜—｜📋カルテ窓 11/11(残10営業日)
- 6250 Yamabiko Corporation｜granville_oshime｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜4,370円｜💰43.0万円｜—｜📋カルテ窓 11/12(残11営業日)
- 2602 日清オイリオグループ｜granville_oshime｜⚡好調｜🟡やや割高｜FAIL_INSEN｜2,084円｜💰20.5万円｜—
- 4413 baudroie,inc.｜granville_oshime｜⚡好調｜🟡やや割高｜FAIL_INSEN｜2,936円｜💰29.6万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）
- 6570 Kyowa Corporation Co. Ltd.｜granville_oshime｜⚡好調｜🟡やや割高｜FAIL_UWAHIGE｜4,045円｜💰41.9万円｜—｜📋カルテ窓 11/11(残10営業日)
- 8919 カチタス｜granville_oshime｜⚡好調｜🟡やや割高｜FAIL_INSEN｜3,365円｜💰34.2万円｜—
- 8410 Seven Bank, Ltd.｜granville_oshime｜⚡好調｜🔴過熱｜FAIL_INSEN｜336.1000061035156円｜💰3.4万円｜—
- 7616 Colowide Co., Ltd.｜granville_oshime｜⚡好調｜🔴過熱｜FAIL_INSEN｜2,185円｜💰22.4万円｜—｜⚠日程不明
- 9304 澁澤倉庫｜granville_oshime｜⚡好調｜⏸判定不能｜FAIL_INSEN｜2,062円｜💰20.7万円｜—｜📑TOPIX低減対象（次 10/30 第1回/8）
- 7350 Okinawa Financial Group, Inc.｜granville_oshime｜⚡好調｜⚪妥当｜PASS｜7,020円｜💰70.2万円｜⛔型不一致: 既に支持帯以下｜📋カルテ窓 11/13(残12営業日)
  > 【業態】銀行業
  > 【いま】終値7,020円・直近5日+1.01%（材料未確認）
  > 【調子】⚡好調（5/13） — (質注意)
  > 【水準】⚪妥当（4.0/7）— PER12.51倍・PEG1.1619・52週70.9% ／ 💰単元70.2万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 4475 HENNGE K.K.｜granville_oshime｜⚡好調｜🔴過熱｜PASS｜2,321円｜💰23.2万円｜⛔提案なし(指名鮮度切れ 12営業日)
  > 【業態】企業向けクラウドセキュリティーサービス「HENNGEOne」提供。メール配信に強み。
  > 【いま】終値2,321円・直近5日+23.59%（材料未確認）
  > 【調子】⚡好調（5/13）
  > 【水準】🔴過熱（0.0/7）— PER45.33倍・PEG3.8377・52週84.7% ／ 💰単元23.2万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 12営業日)）
- 6058 VECTOR Inc.｜granville_oshime｜⚡好調｜🔴過熱｜FAIL_INSEN｜2,126円｜💰21.6万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）
- 4373 Simplex Holdings,Inc.｜granville_oshime｜✅順調｜🟡やや割高｜FAIL_INSEN｜1,250円｜💰12.6万円｜—｜🚨決算直前 10/28(残1営業日)｜⚡材料後出し
- 3097 Monogatari Corporation｜granville_oshime｜✅順調｜🔴過熱｜FAIL_UWAHIGE｜5,980円｜💰60.4万円｜—｜📋カルテ窓 11/13(残12営業日)
- 6998 Nippon Tungsten Co., Ltd.｜granville_oshime｜✅順調｜🔴過熱｜PASS｜3,160円｜💰31.6万円｜⛔型不一致: 既に支持帯以下｜📋カルテ窓 11/11(残10営業日)
  > 【業態】タングステンとモリブデン加工業。粉末冶金で超硬合金、電極、ファインセラミック等製造。
  > 【いま】終値3,160円・直近5日-3.07%（材料未確認）
  > 【調子】✅順調（4/13） — 質注意、経常減益-10.9%
  > 【水準】🔴過熱（1.0/7）— PER21.38倍・PEG—・52週61.5% ／ 💰単元31.6万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 5985 SUNCALL CORPORATION｜granville_oshime｜✅順調｜🟢値頃｜PASS_DOJI｜1,972円｜💰19.7万円｜⛔型不一致: 既に支持帯以下｜📋カルテ窓 11/13(残12営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
  > 【業態】精密部品メーカー。車用精密ばね主力でトヨタ・ホンダ中心。プリンタ部品も。HDD撤退。
  > 【いま】終値1,972円・直近5日-5.87%（材料未確認）
  > 【調子】✅順調（3/13）
  > 【水準】🟢値頃（5.0/7）— PER9.48倍・PEG0.6984・52週53.4% ／ 💰単元19.7万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 1518 三井松島ホールディングス｜granville_oshime｜✅順調｜🟡やや割高｜FAIL_INSEN｜2,250円｜💰22.9万円｜—｜📋カルテ窓 11/13(残12営業日)
- 4208 UBE Corporation｜granville_oshime｜✅順調｜🟡やや割高｜FAIL_INSEN｜3,286円｜💰32.5万円｜—
- 6379 RAIZNEXT Corporation｜granville_oshime｜✅順調｜🔴過熱｜FAIL_INSEN｜1,016円｜💰10.2万円｜—｜📋カルテ窓 11/13(残12営業日)
- 9044 NANKAI Co., Ltd.｜granville_oshime｜✅順調｜🟡やや割高｜FAIL_INSEN｜3,068円｜💰31.2万円｜—｜⏰決算 11/02(残4営業日)
- 3107 ダイワボウホールディングス｜granville_oshime｜⚠減速｜🔴過熱｜PASS｜3,862円｜💰38.6万円｜⛔提案なし(指名鮮度切れ 15営業日)｜📋カルテ窓 11/11(残10営業日)｜⚠業績基調が下向き（減速）
  > 【業態】ダイワボウ情報システムが主力。祖業の紡績事業は譲渡。産業機械のIoTを拡大。
  > 【いま】終値3,862円・直近5日+9.44%（材料未確認）
  > 【調子】⚠減速（3/13） — leverage分母ゼロ近傍、進捗21%(前年同期22%・1Q累計・経常ベース)、減収、質注意、経常成長-18.3%
  > 【水準】🔴過熱（1.0/7）— PER13.03倍・PEG—・52週99.9% ／ 💰単元38.6万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 15営業日)）
- 4044 Central Glass Co., Ltd.｜granville_oshime｜✅順調｜🔴過熱｜PASS｜4,510円｜💰45.1万円｜⛔型不一致: 既に支持帯以下｜📋カルテ窓 11/12(残11営業日)
  > 【業態】板ガラス3位。主力は洗浄剤など化成品、ファインケミカル。海外事業整理、多角化推進。
  > 【いま】終値4,510円・直近5日+1.12%（材料未確認）
  > 【調子】✅順調（3/13） — 質注意
  > 【水準】🔴過熱（1.0/7）— PER13.98倍・PEG—・52週82.9% ／ 💰単元45.1万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 456A Human Made Inc.｜granville_oshime｜✅順調｜🔴過熱｜PASS｜2,088円｜💰20.9万円｜oshime 1,940（✅即時可）｜⚠日程不明
  > 【業態】ストリートファッションなどを主力とするアパレルブランドを展開する。
  > 【いま】終値2,088円・直近5日+18.64%（材料未確認）
  > 【調子】✅順調（3/13） — D軸判定不能(直近Q比較不可)、質注意
  > 【水準】🔴過熱（0.0/7）— PER58.00倍・PEG6.0267・52週90.6% ／ 💰単元20.9万円
  > 【戦略】1,940円までの押し目を指値で待つ。SL1,930.4円（25日線基準）
- 7504 Kohsoku Corporation｜granville_oshime｜✅順調｜🔴過熱｜PASS｜5,330円｜💰53.3万円｜⛔提案なし(指名鮮度切れ 20営業日)｜⏰決算 10/30(残3営業日)
  > 【業態】食品軽包装資材商社。食品加工業向け中心。東北・北関東地盤。M&Aで拡大。
  > 【いま】終値5,330円・直近5日+13.16%（材料未確認）
  > 【調子】✅順調（3/13） — 質注意
  > 【水準】🔴過熱（0.0/7）— PER25.76倍・PEG6.365・52週98.9% ／ 💰単元53.3万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 20営業日)）
- 9509 Hokkaido Electric Power Company,Incorporated｜granville_oshime｜🔻悪化｜⚪妥当｜PASS｜1,098.5円｜💰11.0万円｜⛔型不一致: 既に支持帯以下｜⏰決算 10/30(残3営業日)｜⚠業績基調が下向き（悪化）
  > 【業態】原子力と石炭火力が主力。需要は冬ピーク。原発3基が停止、再稼働目指す。
  > 【いま】終値1,098.5円・直近5日+0.87%（材料未確認）
  > 【調子】🔻悪化（2/13） — 経常成長率-25.0%、経常減益-25.0%、質注意
  > 【水準】⚪妥当（3.0/7）— PER7.14倍・PEG—・52週51.8% ／ 💰単元11.0万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 6072 Jibannet Holdings Co., Ltd.｜granville_oshime｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜999円｜💰9.9万円｜—｜📋カルテ窓 11/12(残11営業日)
- 7630 Ichibanya Co., Ltd.｜granville_oshime｜➖横ばい｜🔴過熱｜FAIL_INSEN｜1,067円｜💰10.8万円｜—｜⚠日程不明
- 8043 Starzen Company Limited｜granville_oshime｜➖横ばい｜🔴過熱｜FAIL_INSEN｜1,565円｜💰15.8万円｜—
- 9505 Hokuriku Electric Power Company｜granville_oshime｜🔻悪化｜🔴過熱｜PASS｜1,085円｜💰10.8万円｜⛔型不一致: 既に支持帯以下｜⏰決算 10/29(残2営業日)｜⚠業績基調が下向き（悪化）
  > 【業態】北陸3県に供給。石炭火力が主体で水力比率も大。志賀原発2基は停止中。
  > 【いま】終値1,085円・直近5日+3.19%（材料未確認）
  > 【調子】🔻悪化（2/13） — leverage分母ゼロ近傍、減収、質注意
  > 【水準】🔴過熱（1.0/7）— PER9.06倍・PEG—・52週76.2% ／ 💰単元10.8万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 9616 共立メンテナンス｜granville_oshime｜➖横ばい｜🔴過熱｜FAIL_INSEN｜3,385円｜💰34.6万円｜—
- 9900 Sagami Holdings Corp.｜granville_oshime｜➖横ばい｜🔴過熱｜FAIL_UWAHIGE｜1,179円｜💰11.3万円｜—｜📋カルテ窓 11/12(残11営業日)
- 8255 Axial Retailing, Inc.｜granville_oshime｜⚠減速｜🔴過熱｜FAIL_INSEN｜1,315円｜💰13.1万円｜—｜⏰決算 11/04(残5営業日)
- 9536 SAIBU GAS HOLDINGS CO. LTD.｜granville_oshime｜⚠減速｜🔴過熱｜FAIL_UWAHIGE｜2,530円｜💰25.4万円｜—｜⏰決算 10/29(残2営業日)
- 8097 SAN-AI OBBLI CO. LTD｜granville_oshime｜⚠減速｜🔴過熱｜FAIL_INSEN｜2,503円｜💰25.0万円｜—
- 8059 Daiichi Jitsugyo Co., Ltd.｜granville_oshime｜⚠減速｜🔴過熱｜FAIL_INSEN｜3,535円｜💰36.0万円｜—
- 8361 Ogaki Kyoritsu Bank, Ltd.｜granville_oshime/granville_rebound｜取得不可｜💎割安｜PASS｜1,521円｜💰15.2万円｜⛔型不一致: 既に支持帯以下｜📋カルテ窓 11/13(残12営業日)
  > 【業態】岐阜地盤の地銀大手。近隣県にも営業攻勢。信託業務で相続強化。
  > 【いま】終値1,521円・直近5日+0.46%（材料未確認）
  > 【調子】—（業績データ）
  > 【水準】💎割安（6.0/7）— PER3.03倍・PEG0.0802・52週66.2% ／ 💰単元15.2万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 9166 GENDA Inc.｜granville_oshime｜業績データ取得不可｜🟢値頃｜FAIL_UWAHIGE｜617円｜💰6.5万円｜—｜⚠日程不明
- 8343 Akita Bank, Ltd.｜granville_oshime｜業績データ取得不可(売上/経常欠損)｜🟢値頃｜PASS｜1,483円｜💰14.8万円｜⛔提案なし(指名鮮度切れ 12営業日)｜📋カルテ窓 11/13(残12営業日)
  > 【業態】秋田地盤の地銀中位。預金、融資とも県内シェア５割超。福島・北海道にも。
  > 【いま】終値1,483円・直近5日+4.51%（材料未確認）
  > 【調子】—（業績データ(売上/経常欠損)）
  > 【水準】🟢値頃（5.0/7）— PER15.58倍・PEG0.9449・52週55.6% ／ 💰単元14.8万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 12営業日)）
- 336A ダイナミックマッププラットフォーム｜granville_oshime｜業績データ取得不可(経常益予想非開示)｜⚪妥当｜FAIL_INSEN｜1,308円｜💰13.0万円｜—｜📋カルテ窓 11/12(残11営業日)
- 6810 マクセル｜granville_oshime｜取得不可｜⚪妥当｜FAIL_INSEN｜2,500円｜💰25.7万円｜—｜⏰決算 10/29(残2営業日)
- 6027 弁護士ドットコム｜granville_oshime｜業績データ取得不可｜🟡やや割高｜PASS｜4,660円｜💰46.6万円｜⛔型不一致: 既に支持帯以下｜📋カルテ窓 11/11(残10営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
  > 【業態】法律相談と弁護士・税理士向け営業支援サイト運営。電子契約サービスが拡大。
  > 【いま】終値4,660円・直近5日-4.21%（材料未確認）
  > 【調子】—（業績データ）
  > 【水準】🟡やや割高（2.0/7）— PER53.08倍・PEG—・52週65.4% ／ 💰単元46.6万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 8362 Fukui Bank, Ltd.｜granville_oshime｜🔻悪化｜🔴過熱｜PASS｜6,850円｜💰68.5万円｜⛔型不一致: 既に支持帯以下｜📋カルテ窓 11/13(残12営業日)｜⚠業績基調が下向き（悪化）
  > 【業態】福井地盤の地銀中位。石川や富山にも展開。福邦銀と26年5月合併。
  > 【いま】終値6,850円・直近5日+4.74%（材料未確認）
  > 【調子】—（経常減益-24.1%、売上予想非開示のためA/C/D軸は算出不可(悪化上書きのみ適用)）
  > 【水準】🔴過熱（1.4/7）— PER18.01倍・PEG—・52週71.5% ／ 💰単元68.5万円
  > 【戦略】発注対象外（⛔型不一致: 既に支持帯以下）
- 6340 澁谷工業｜granville_oshime｜—｜－未評価｜FAIL_UWAHIGE｜5,370円｜—｜—
- 8051 山善｜granville_oshime｜—｜－未評価｜FAIL_INSEN｜1,941円｜—｜—｜📋カルテ窓 11/11(残10営業日)
- 8622 Mito Securities Co., Ltd.｜granville_oshime/granville_rebound｜取得不可｜⏸判定不能｜FAIL_INSEN｜739円｜💰7.5万円｜—｜⏰決算 10/29(残2営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 8624 Ichiyoshi Securities Co., Ltd.｜granville_oshime/granville_rebound｜取得不可｜⏸判定不能｜FAIL_INSEN｜1,429円｜💰15.2万円｜—｜⏰決算 10/29(残2営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 8628 松井証券｜granville_oshime｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜1,022円｜💰10.6万円｜—｜🚨決算直前 10/28(残1営業日)
- 6769 Thine Electronics, Inc.｜granville_rebound｜🚀確変｜⚪妥当｜FAIL_UWAHIGE｜1,015円｜💰9.9万円｜—
- 3691 DIGITAL PLUS, Inc.｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1,421円｜💰15.8万円｜—｜📋カルテ窓 11/13(残12営業日)
- 479A PRONI Inc.｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜1,816円｜💰19.3万円｜—｜📋カルテ窓 11/13(残12営業日)
- 1436 GreenEnergy & Company｜granville_rebound｜🔥絶好調｜💎割安｜FAIL_INSEN｜1,493円｜💰15.1万円｜—｜⚠日程不明
- 8995 Makoto Construction Co,Ltd｜granville_rebound｜🔥絶好調｜🟢値頃｜FAIL_UWAHIGE｜1,574円｜💰14.8万円｜—｜📋カルテ窓 11/13(残12営業日)
- 2122 インタースペース｜granville_rebound｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜1,322円｜💰13.4万円｜—
- 6963 ROHM Company Limited｜granville_rebound｜🔥絶好調｜⚪妥当｜PASS_DOJI｜3,700円｜💰37.0万円｜reversal 3,700（✅即時可）
  > 【業態】カスタムLSIで首位。半導体素子、抵抗器などに強み。SiCパワー半導体が拡大。
  > 【いま】終値3,700円・直近5日-5.20%（材料未確認）
  > 【調子】🔥絶好調（9/13）
  > 【水準】⚪妥当（4.0/7）— PER49.27倍・PEG0.5644・52週42.2% ／ 💰単元37.0万円
  > 【戦略】当日終値3,700円の指値で反転を取りにいく。SL3,486円（直近5日安値）
- 8364 清水銀行｜granville_rebound｜🔥絶好調｜🟢値頃｜PASS｜2,724円｜💰27.2万円｜reversal 2,724（✅即時可）｜📋カルテ窓 11/13(残12営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
  > 【業態】静岡地盤の地銀中下位行。地元中小企業向け中心。SBIHDと資本業務提携。
  > 【いま】終値2,724円・直近5日-0.47%（材料未確認）
  > 【調子】🔥絶好調（8/13）
  > 【水準】🟢値頃（5.0/7）— PER10.65倍・PEG0.2131・52週53.8% ／ 💰単元27.2万円
  > 【戦略】当日終値2,724円の指値で反転を取りにいく。SL2,458円（直近5日安値）
- 6490 ＰＩＬＬＡＲ｜granville_rebound｜⚡好調｜⚪妥当｜PASS_DOJI｜10,020円｜💰100.2万円｜reversal 10,020（✅即時可）｜📋カルテ窓 11/12(残11営業日)｜⚠1単元でリスク枠超過（69,000円）
  > 【業態】流体制御関連のメカニカルシール大手。パッキン、ガスケットなど産業機械向け拡大。
  > 【いま】終値10,020円・直近5日-6.09%（材料未確認）
  > 【調子】⚡好調（7/13）
  > 【水準】⚪妥当（4.0/7）— PER16.37倍・PEG0.2843・52週65.1% ／ 💰単元100.2万円
  > 【戦略】当日終値10,020円の指値で反転を取りにいく。SL9,330円（直近5日安値）／⚠1単元リスク69,000円（枠超過）
- 5242 EYEZ INC.｜granville_rebound｜⚡好調｜🔴過熱｜FAIL_UWAHIGE｜3,090円｜💰30.0万円｜—｜📋カルテ窓 11/13(残12営業日)
- 477A Startline CO.,LTD.｜granville_rebound｜⚡好調｜💎割安｜FAIL_UWAHIGE｜765円｜💰7.5万円｜—｜📋カルテ窓 11/13(残12営業日)
- 6336 石井表記｜granville_rebound｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜1,344円｜💰14.4万円｜—｜⚠日程不明
- 2354 YE DIGITAL CORPORATION｜granville_rebound｜⚡好調｜💎割安｜FAIL_UWAHIGE｜1,032円｜💰10.4万円｜—｜⚠日程不明
- 4100 Toda Kogyo Corp.｜granville_rebound｜⚡好調｜🟢値頃｜FAIL_UWAHIGE｜1,607円｜💰16.2万円｜—｜📋カルテ窓 11/11(残10営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 8344 Yamagata Bank, Ltd.｜granville_rebound｜⚡好調｜🟢値頃｜FAIL_INSEN｜4,375円｜💰42.3万円｜—｜📋カルテ窓 11/13(残12営業日)
- 8392 大分銀行｜granville_rebound｜⚡好調｜🟢値頃｜FAIL_INSEN｜2,731円｜💰26.9万円｜—
- 6597 HPC SYSTEMS Inc.｜changepoint/changepoint🔔/changepoint🔔🔔/granville_rebound｜⚡好調｜🟢値頃｜FAIL_INSEN｜3,100円｜💰30.7万円｜—｜📋カルテ窓 11/13(残12営業日)
- 3687 Fixstars Corp.｜granville_rebound｜⚡好調｜⚪妥当｜FAIL_INSEN｜1,848円｜💰18.6万円｜—｜📑TOPIX低減対象（次 10/30 第1回/8）
- 5574 ABEJA,Inc.｜granville_rebound｜⚡好調｜🟡やや割高｜FAIL_INSEN｜2,363円｜💰23.5万円｜—｜⚠日程不明
- 9278 BOOKOFF GROUP HOLDINGS LIMITED｜granville_rebound｜⚡好調｜🟡やや割高｜FAIL_INSEN｜2,413円｜💰24.8万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）
- 7256 河西工業｜granville_rebound｜⚡好調｜🔴過熱｜FAIL_INSEN｜406円｜—｜—｜📋カルテ窓 11/16(残13営業日)
- 4997 日本農薬｜granville_rebound｜✅順調｜🟡やや割高｜FAIL_INSEN｜1,062円｜💰10.7万円｜—｜📑TOPIX低減対象（次 10/30 第1回/8）
- 278A Ｔｅｒｒａ　Ｄｒｏｎｅ｜granville_rebound｜✅順調｜⏸判定不能｜PASS｜6,660円｜—｜⛔提案なし(単元株数不明でリスク計算不可)｜⚠日程不明
  > 【業態】測量・点検・農業におけるドローンを含むハード・ソフトの開発などを手掛ける。
  > 【いま】終値6,660円・直近5日+10.45%（材料未確認）
  > 【調子】✅順調（4/13） — 赤字ルート
  > 【水準】⏸判定不能— PER—倍・PEG—・52週52.9% ／ 💰単元—万円
  > 【戦略】発注対象外（⛔提案なし(単元株数不明でリスク計算不可)）
- 1407 West Holdings Corporation｜granville_rebound｜✅順調｜🟢値頃｜FAIL_INSEN｜2,074円｜💰22.7万円｜—｜⚠日程不明
- 4346 NEXYZ.Group Corporation｜granville_rebound｜✅順調｜🟢値頃｜PASS｜745円｜💰7.5万円｜⛔提案なし(指名鮮度切れ 16営業日)｜📋カルテ窓 11/16(残13営業日)
  > 【業態】LED照明、空調、業務機器のレンタル主力。電子メディア・雑誌、エンタメ、定額制エステも。
  > 【いま】終値745円・直近5日+1.78%（材料未確認）
  > 【調子】✅順調（3/13）
  > 【水準】🟢値頃（5.0/7）— PER10.21倍・PEG1.1252・52週18.5% ／ 💰単元7.5万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 16営業日)）
- 7354 Direct Marketing MiX Inc.｜granville_rebound｜✅順調｜⚪妥当｜FAIL_INSEN｜366円｜💰4.0万円｜—｜📋カルテ窓 11/13(残12営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 2681 2nd RETAILING Co., Ltd.｜granville_rebound｜✅順調｜🟡やや割高｜FAIL_INSEN｜1,939円｜💰20.3万円｜—｜📑TOPIX低減対象（次 10/30 第1回/8）
- 4082 第一稀元素化学工業｜granville_rebound｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜1,814円｜💰17.9万円｜—｜📋カルテ窓 11/12(残11営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 3653 Morpho, Inc.｜granville_rebound｜🔻悪化｜💎割安｜FAIL_UWAHIGE｜915円｜💰8.8万円｜—｜⚠日程不明
- 3907 Silicon Studio Corp.｜granville_rebound｜🔻悪化｜💎割安｜PASS｜1,369円｜💰13.7万円｜reversal 1,369（✅即時可）｜⚠日程不明｜⚠業績基調が下向き（悪化）｜⚠バリュートラップ疑い
  > 【業態】3D技術を活用、ゲーム開発用ミドルウエアが主力。開発受託や人材派遣を展開。
  > 【いま】終値1,369円・直近5日-5.13%（材料未確認）
  > 【調子】🔻悪化（2/13） — 赤字、減収、質注意
  > 【水準】💎割安（7.0/7）— PER—倍・PEG—・52週33.1% ／ 💰単元13.7万円
  > 【戦略】当日終値1,369円の指値で反転を取りにいく。SL1,265円（直近5日安値）
- 4440 WITZ Corp.｜granville_rebound｜➖横ばい｜⚪妥当｜FAIL_UWAHIGE｜1,804円｜💰18.2万円｜—｜⚠日程不明
- 8163 SRS HOLDINGS CO.,LTD.｜granville_rebound｜➖横ばい｜🔴過熱｜FAIL_UWAHIGE｜1,713円｜💰17.1万円｜—
- 4691 Washington Hotel Corp.｜granville_rebound｜⚠減速｜⚪妥当｜FAIL_INSEN｜1,809円｜💰18.3万円｜—｜📋カルテ窓 11/13(残12営業日)
- 6203 Howa Machinery, Ltd.｜granville_rebound｜⚠減速｜🟡やや割高｜FAIL_UWAHIGE｜2,278円｜💰22.8万円｜—｜📋カルテ窓 11/13(残12営業日)
- 6522 アスタリスク｜granville_rebound｜⚠減速｜🟢値頃｜FAIL_INSEN｜822円｜💰8.1万円｜—｜⚠日程不明
- 8360 Yamanashi Chuo Bank, Ltd.｜granville_rebound｜取得不可｜💎割安｜PASS｜1,279円｜💰12.8万円｜reversal 1,279（✅即時可）｜📋カルテ窓 11/13(残12営業日)
  > 【業態】未取得（次回以降に取得）
  > 【いま】終値1,279円・直近5日+1.75%（材料未確認）
  > 【調子】—（データなし）
  > 【水準】💎割安（6.0/7）— PER3.14倍・PEG0.0972・52週66.7% ／ 💰単元12.8万円
  > 【戦略】当日終値1,279円の指値で反転を取りにいく。SL1,132円（直近5日安値）
- 3778 SAKURA Internet Inc.｜granville_rebound｜業績データ取得不可｜🟢値頃｜FAIL_INSEN｜2,967円｜💰29.3万円｜—｜🚨決算直前 10/28(残1営業日)
- 7380 Juroku Financial Group,Inc.｜granville_rebound｜取得不可｜⚪妥当｜PASS｜2,358円｜💰23.6万円｜reversal 2,358（✅即時可）
  > 【業態】岐阜県内最大手の地銀、十六銀行が中核の総合金融サービス。愛知へ拡大。
  > 【いま】終値2,358円・直近5日-0.08%（材料未確認）
  > 【調子】—（業績データ(売上予想なし)）
  > 【水準】⚪妥当（3.0/7）— PER13.92倍・PEG4.8241・52週68.6% ／ 💰単元23.6万円
  > 【戦略】当日終値2,358円の指値で反転を取りにいく。SL2,156円（直近5日安値）
- 8368 Hyakugo Bank, Ltd.｜granville_rebound｜取得不可｜🟡やや割高｜PASS｜2,089円｜💰20.9万円｜reversal 2,089（✅即時可）
  > 【業態】三重地盤の地銀上位。県内で圧倒的。三菱UFJ、十六銀、名古屋銀と親密。
  > 【いま】終値2,089円・直近5日-1.23%（材料未確認）
  > 【調子】—（業績データ）
  > 【水準】🟡やや割高（2.0/7）— PER17.45倍・PEG1.5506・52週64.0% ／ 💰単元20.9万円
  > 【戦略】当日終値2,089円の指値で反転を取りにいく。SL1,902円（直近5日安値）
- 8713 Fidea Holdings Co.Ltd.｜granville_rebound｜業績データ取得不可(売上/経常欠損)｜🔴過熱｜PASS｜2,527円｜💰25.3万円｜reversal 2,527（✅即時可）｜📋カルテ窓 11/13(残12営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
  > 【業態】荘内銀、北都銀が県を超えて統合。山形・秋田が地盤。27年1月両行合併へ。
  > 【いま】終値2,527円・直近5日+8.50%（材料未確認）
  > 【調子】—（業績データ(売上/経常欠損)）
  > 【水準】🔴過熱（1.4/7）— PER14.20倍・PEG—・52週69.9% ／ 💰単元25.3万円
  > 【戦略】当日終値2,527円の指値で反転を取りにいく。SL2,265円（直近5日安値）
- 6890 Ferrotec Corporation｜granville_rebound｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜7,940円｜💰78.4万円｜—｜📋カルテ窓 11/16(残13営業日)｜📑TOPIX新規採用（2026-10-30 組入）
- 7175 Imamura Securities Co.Ltd.｜granville_rebound｜業績データ取得不可｜⏸判定不能｜FAIL_UWAHIGE｜1,695円｜💰16.8万円｜—｜⚠日程不明｜⚡材料後出し
- 7715 長野計器｜granville_rebound｜—｜－未評価｜FAIL_INSEN｜3,900円｜—｜—｜📋カルテ窓 11/12(残11営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 8377 ほくほくフィナンシャルグループ｜granville_rebound｜業績データ取得不可｜⏸判定不能｜PASS｜737.7000122070312円｜💰7.4万円｜reversal 737.7000122070312（✅即時可）
  > 【業態】傘下に北陸銀と北海道銀持つ金融持ち株会社。横浜銀とシステム提携。
  > 【いま】終値737.7000122070312円・直近5日+1.68%（材料未確認）
  > 【調子】—（kabutan年次表を解析できず）
  > 【水準】⏸判定不能— PER—倍・PEG—・52週65.7% ／ 💰単元7.4万円
  > 【戦略】当日終値737.7000122070312円の指値で反転を取りにいく。SL662.5円（直近5日安値）
- 8739 スパークス・グループ｜granville_rebound｜—｜－未評価｜FAIL_INSEN｜2,321円｜—｜—｜⏰決算 10/30(残3営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）

## 変化点銘柄
- 265A エイチエムコム｜changepoint🔔｜🚀確変｜🟢値頃｜FAIL_INSEN｜732円｜💰7.9万円｜—｜📋カルテ窓 11/13(残12営業日)｜🔒実弾封印中(PL3紙ログ収集中)
- 5803 フジクラ｜changepoint🔔/changepoint🔔/changepoint🔔🔔｜🚀確変｜🟢値頃｜FAIL_INSEN｜4,092円｜💰39.8万円｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 4011 Headwaters Co.,Ltd｜changepoint🔔/changepoint｜🚀確変｜🟢値頃｜FAIL_UWAHIGE｜2,161円｜💰22.0万円｜—｜📋カルテ窓 11/13(残12営業日)｜🔒実弾封印中(PL3紙ログ収集中)
- 4187 大阪有機化学工業｜changepoint/changepoint🔔｜🔥絶好調｜💎割安｜FAIL_INSEN｜4,405円｜💰43.4万円｜—｜⚠日程不明｜🔒実弾封印中(PL3紙ログ収集中)
- 9888 UEX LTD｜changepoint/changepoint🔔/changepoint🔔🔔｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1,376円｜💰14.1万円｜—｜🔒実弾封印中(PL3紙ログ収集中)
- 7695 交換できるくん｜changepoint🔔｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜864円｜💰8.8万円｜—｜📋カルテ窓 11/13(残12営業日)｜🔒実弾封印中(PL3紙ログ収集中)
- 6080 Ｍ＆Ａキャピタルパートナーズ｜changepoint/changepoint🔔｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜4,145円｜💰42.2万円｜—｜⏰決算 10/30(残3営業日)｜🔒実弾封印中(PL3紙ログ収集中)
- 584A LiNKX, Inc.｜changepoint🔔/changepoint🔔｜🔥絶好調｜🟢値頃｜PASS｜2,308円｜💰23.1万円｜changepoint 2,308（✅即時可）｜📋カルテ窓 11/13(残12営業日)｜🔒実弾封印中(PL3紙ログ収集中)
  > 【業態】金融分野を中心とした基幹システムなどのモダナイゼーション事業を手掛ける。
  > 【いま】終値2,308円・直近5日+8.51%（材料未確認）
  > 【調子】🔥絶好調（9/13） — D軸判定不能(四半期データ不足)
  > 【水準】🟢値頃（5.0/7）— PER33.11倍・PEG0.526・52週25.6% ／ 💰単元23.1万円
  > 【戦略】発火日終値2,308円の指値。追撃禁止・SL2,072円。🔒実弾封印中（PL3紙ログ収集中）
- 6136 OSG CORP｜changepoint/changepoint🔔/changepoint🔔🔔｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜3,460円｜💰34.8万円｜—｜⚠日程不明｜🔒実弾封印中(PL3紙ログ収集中)
- 6857 アドバンテスト｜changepoint/changepoint🔔｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜33,860円｜💰323.4万円｜—｜🚨決算直前 10/28(残1営業日)｜🔒実弾封印中(PL3紙ログ収集中)
- 8151 東陽テクニカ｜changepoint🔔｜🔥絶好調｜⚪妥当｜PASS｜1,924円｜💰19.2万円｜changepoint 1,924（✅即時可）｜📋カルテ窓 11/11(残10営業日)｜🔒実弾封印中(PL3紙ログ収集中)｜📑TOPIX低減対象（次 10/30 第1回/8）
  > 【業態】電子計測器専門商社。研究開発用機器が主力。欧米から輸入販売中心。
  > 【いま】終値1,924円・直近5日+2.61%（材料未確認）
  > 【調子】🔥絶好調（9/13）
  > 【水準】⚪妥当（4.0/7）— PER15.99倍・PEG0.1851・52週51.9% ／ 💰単元19.2万円
  > 【戦略】発火日終値1,924円の指値。追撃禁止・SL1,868円。🔒実弾封印中（PL3紙ログ収集中）
- 9962 ミスミグループ本社｜changepoint/changepoint🔔｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜3,796円｜💰36.6万円｜—｜⏰決算 10/30(残3営業日)｜🔒実弾封印中(PL3紙ログ収集中)
- 4382 HEROZ, Inc.｜changepoint🔔/changepoint🔔🔔/changepoint🔔🔔｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜1,365円｜💰13.7万円｜—｜⚠日程不明｜🔒実弾封印中(PL3紙ログ収集中)｜📑TOPIX低減対象（次 10/30 第1回/8）
- 4368 4368｜changepoint/changepoint🔔｜🔥絶好調｜💎割安｜FAIL_UWAHIGE｜2,930円｜💰28.6万円｜—｜⏰決算 10/30(残3営業日)｜🔒実弾封印中(PL3紙ログ収集中)
- 7318 セレンディップ・ホールディングス｜changepoint🔔/changepoint🔔🔔/changepoint🔔🔔｜🔥絶好調｜💎割安｜FAIL_INSEN｜1,095円｜💰10.9万円｜—｜📋カルテ窓 11/13(残12営業日)｜🔒実弾封印中(PL3紙ログ収集中)
- 5582 （名称取得不可）｜changepoint🔔｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1,810円｜💰18.1万円｜—｜📋カルテ窓 11/16(残13営業日)｜🔒実弾封印中(PL3紙ログ収集中)
- 5590 NETSTARS Co.,Ltd.｜changepoint🔔｜⚡好調｜🟢値頃｜PASS｜656円｜💰6.6万円｜changepoint 656（✅即時可）｜📋カルテ窓 11/12(残11営業日)
  > 【業態】マルチQRコード決済サービス「StarPay」の提供などを手掛ける。
  > 【いま】終値656円・直近5日-2.96%（材料未確認）
  > 【調子】⚡好調（7/13）
  > 【水準】🟢値頃（5.0/7）— PER22.54倍・PEG0.3783・52週7.8% ／ 💰単元6.6万円
  > 【戦略】発火日終値656円の指値。追撃禁止・SL632円。🔒実弾封印中（PL3紙ログ収集中）
- 478A Hutzper Inc.｜changepoint🔔/changepoint🔔🔔｜⚡好調｜⚪妥当｜FAIL_INSEN｜728円｜💰7.7万円｜—｜📋カルテ窓 11/16(残13営業日)｜🔒実弾封印中(PL3紙ログ収集中)
- 8704 トレイダーズホールディングス｜changepoint/changepoint🔔｜⚡好調｜💎割安｜FAIL_INSEN｜1,213円｜💰12.9万円｜—｜⏰決算 10/30(残3営業日)｜🔒実弾封印中(PL3紙ログ収集中)｜⚡材料後出し
- 6284 日精エー・エス・ビー機械｜changepoint🔔｜⚡好調｜🟢値頃｜PASS｜8,010円｜💰80.1万円｜changepoint 8,010（✅即時可）｜📋カルテ窓 11/11(残10営業日)｜🔒実弾封印中(PL3紙ログ収集中)
  > 【業態】PETボトルなど非飲料容器成形機の世界大手。海外比率が9割。汎用機拡大。
  > 【いま】終値8,010円・直近5日-3.26%（材料未確認）
  > 【調子】⚡好調（5/13）
  > 【水準】🟢値頃（5.0/7）— PER13.20倍・PEG0.6581・52週47.3% ／ 💰単元80.1万円
  > 【戦略】発火日終値8,010円の指値。追撃禁止・SL7,750円。🔒実弾封印中（PL3紙ログ収集中）
- 218A Liberaware｜changepoint/changepoint🔔｜⚡好調｜⚪妥当｜FAIL_UWAHIGE｜911円｜💰8.8万円｜—｜⚠日程不明｜🔒実弾封印中(PL3紙ログ収集中)
- 6785 鈴木｜changepoint/changepoint🔔🔔｜✅順調｜⚪妥当｜PASS｜3,240円｜💰32.4万円｜changepoint 3,240（✅即時可）｜🔒実弾封印中(PL3紙ログ収集中)｜📑TOPIX低減対象（次 10/30 第1回/8）
  > 【業態】自動車・携帯電話向けコネクターが主力。精密金型に強み。医療器具事業も。
  > 【いま】終値3,240円・直近5日-0.92%（材料未確認）
  > 【調子】✅順調（4/13） — 開示ウォッチにより再確認(通期経常+4%・4期連続最高益で着地、グレード変更なし)
  > 【水準】⚪妥当（4.0/7）— PER12.47倍・PEG0.3133・52週75.6% ／ 💰単元32.4万円
  > 【戦略】発火日終値3,240円の指値。追撃禁止・SL3,035円。🔒実弾封印中（PL3紙ログ収集中）
- 4165 PLAID Inc.｜changepoint🔔｜🔻悪化｜🔴過熱｜FAIL_UWAHIGE｜743円｜💰7.5万円｜—｜📋カルテ窓 11/12(残11営業日)｜🔒実弾封印中(PL3紙ログ収集中)
- 4498 Cybertrust Japan Co., Ltd.｜changepoint🔔/changepoint🔔🔔｜✅順調｜🔴過熱｜FAIL_UWAHIGE｜2,947円｜💰24.7万円｜—｜⏰決算 10/29(残2営業日)｜🔒実弾封印中(PL3紙ログ収集中)
- 4071 Plus Alpha Consulting Co. LTD.｜changepoint🔔｜✅順調｜⚪妥当｜FAIL_INSEN｜2,307円｜💰23.4万円｜—｜📋カルテ窓 11/11(残10営業日)｜🔒実弾封印中(PL3紙ログ収集中)
- 4418 Japan Data Science Consortium Co Ltd.｜changepoint🔔｜⚠減速｜⚪妥当｜FAIL_INSEN｜1,087円｜💰10.8万円｜—｜📋カルテ窓 11/13(残12営業日)
- 598A チャットプラス｜changepoint🔔/changepoint/changepoint🔔🔔｜✅順調｜⚪妥当｜FAIL_INSEN｜1,169円｜💰12.0万円｜—｜📋カルテ窓 11/12(残11営業日)｜🔒実弾封印中(PL3紙ログ収集中)
- 4493 Cyber Security Cloud, Inc.｜changepoint🔔｜✅順調｜🔴過熱｜FAIL_UWAHIGE｜3,550円｜💰34.5万円｜—｜📋カルテ窓 11/13(残12営業日)
- 339A PROGRESS TECHNOLOGIES GROUP INC｜changepoint/changepoint🔔/changepoint🔔🔔｜➖横ばい｜⚪妥当｜FAIL_INSEN｜810円｜💰8.1万円｜—｜⚠日程不明｜🔒実弾封印中(PL3紙ログ収集中)
- 4488 AI inside Inc.｜changepoint｜➖横ばい｜🟡やや割高｜FAIL_INSEN｜1,970円｜💰21.2万円｜—｜📋カルテ窓 11/12(残11営業日)｜🔒実弾封印中(PL3紙ログ収集中)
- 4259 ExaWizards Inc.｜changepoint/changepoint🔔｜業績データ取得不可｜🟢値頃｜FAIL_UWAHIGE｜762円｜💰7.5万円｜—｜📋カルテ窓 11/11(残10営業日)｜🔒実弾封印中(PL3紙ログ収集中)
- 3993 PKSHA Technology, Inc.｜changepoint🔔｜業績データ取得不可｜⚪妥当｜FAIL_UWAHIGE｜3,730円｜💰37.0万円｜—｜📋カルテ窓 11/12(残11営業日)｜🔒実弾封印中(PL3紙ログ収集中)
- 4478 freee K.K.｜changepoint🔔/changepoint🔔🔔｜業績データ取得不可｜🟡やや割高｜PASS｜4,175円｜💰41.8万円｜changepoint 4,175（✅即時可）｜📋カルテ窓 11/11(残10営業日)｜🔒実弾封印中(PL3紙ログ収集中)｜📑TOPIX新規採用（2026-10-30 組入）｜⚠1単元でリスク枠超過（34,000円）
  > 【業態】スモールビジネス向けクラウドERPサービスの提供。会計や会社設立、開業支援など。
  > 【いま】終値4,175円・直近5日+9.72%（材料未確認）
  > 【調子】—（業績データ(売上/経常欠損)）
  > 【水準】🟡やや割高（2.8/7）— PER—倍・PEG—・52週85.1% ／ 💰単元41.8万円
  > 【戦略】発火日終値4,175円の指値。追撃禁止・SL3,835円。🔒実弾封印中（PL3紙ログ収集中）／⚠1単元リスク34,000円（枠超過）
- 593A ティアフォー｜changepoint/changepoint🔔/changepoint🔔🔔｜取得不可｜🔴過熱｜FAIL_UWAHIGE｜2,239円｜💰21.9万円｜—｜📋カルテ窓 11/13(残12営業日)｜🔒実弾封印中(PL3紙ログ収集中)｜📑TOPIX新規採用（2026-10-30 組入）

## 🤖AI特需銘柄
①-S3 は本夜分(scored_at=2026-10-27)が未更新のため、候補としては使わず、プール在籍分のみ継続評価。参考: ai_scan base_day=2026-10-23｜25MA上回り率 📡エネマネ・計量 14.29%; ❄️冷却・空調 16.67%; 🌐光通信 9.09%; 🔬基板・素材 4.76%
- 3131 シンデン・ハイテックス｜ai_momentum/ai_reversal/granville_rebound｜🚀確変｜💎割安｜FAIL_INSEN｜6,400円｜💰62.0万円｜—
- 2760 東京エレクトロン　デバイス｜ai_momentum/granville_oshime/ai_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜4,570円｜💰44.5万円｜—｜🚨決算直前 10/28(残1営業日)
- 9824 泉州電業｜ai_momentum｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜8,200円｜💰78.6万円｜—｜⚠日程不明
- 6521 オキサイド｜ai_momentum/ai_reversal｜⚡好調｜🟢値頃｜PASS｜3,215円｜💰32.1万円｜momentum 3,235（✅即時可）｜⚠日程不明
  > 【業態】単結晶や光部品、レーザ光源、計測装置の開発・販売。半導体、画像装置向け。
  > 【いま】終値3,215円・直近5日+0.47%（材料未確認）
  > 【調子】⚡好調（7/13） — 経常成長率+83.1%、D軸判定不能(直近Qデータなし)
  > 【水準】🟢値頃（5.0/7）— PER28.15倍・PEG0.3388・52週30.2% ／ 💰単元32.1万円
  > 【戦略】当日高値超えの逆指値3,235円で順張り参戦を検討。上限3,267.3円・SL3,036.2円目安
- 1982 日比谷総合設備｜ai_momentum｜⚠減速｜🔴過熱｜FAIL_INSEN｜3,340円｜💰32.8万円｜—｜📋カルテ窓 11/11(残10営業日)
- 9960 トーテック｜granville_tenkan/granville_oshime/ai_momentum｜⚠減速｜🔴過熱｜FAIL_UWAHIGE｜4,380円｜💰43.3万円｜—
- 6254 野村マイクロ・サイエンス｜changepoint🔔/ai_reversal｜🚀確変｜💎割安｜FAIL_UWAHIGE｜2,824円｜💰28.9万円｜—｜📋カルテ窓 11/13(残12営業日)
- 4047 関東電化工業｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜2,013円｜💰19.8万円｜—
- 4971 メック｜ai_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜6,010円｜💰59.8万円｜—｜📋カルテ窓 11/11(残10営業日)
- 3110 日東紡｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜2,942円｜💰28.7万円｜—
- 6981 村田製作所｜ai_reversal｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜6,367円｜💰62.8万円｜—｜⏰決算 10/30(残3営業日)
- 7433 伯東｜ai_reversal/granville_oshime｜🔥絶好調｜🟢値頃｜FAIL_INSEN｜1,814円｜💰17.9万円｜—｜📋カルテ窓 11/12(残11営業日)｜⚡材料後出し
- 4062 イビデン｜ai_reversal/granville_rebound｜🔥絶好調｜⚪妥当｜FAIL_INSEN｜8,952円｜💰85.1万円｜—｜⏰決算 10/29(残2営業日)
- 6524 湖北工業｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_INSEN｜4,585円｜💰44.9万円｜—｜📋カルテ窓 11/12(残11営業日)
- 6235 オプトラン｜ai_reversal｜🔥絶好調｜💎割安｜FAIL_UWAHIGE｜2,260円｜💰22.4万円｜—
- 7729 東京精密｜ai_reversal｜🔥絶好調｜⚪妥当｜FAIL_UWAHIGE｜15,355円｜💰155.2万円｜—｜⏰決算 11/04(残5営業日)
- 6779 Nihon Dempa Kogyo Co., Ltd.｜granville_rebound/ai_reversal｜⚡好調｜🟢値頃｜FAIL_INSEN｜2,563円｜💰25.3万円｜—
- 6752 パナソニックHD｜ai_reversal/granville_rebound｜⚠減速｜⚪妥当｜FAIL_UWAHIGE｜3,687円｜💰36.3万円｜—｜⏰決算 10/30(残3営業日)
- 6787 メイコー｜ai_reversal｜⚡好調｜💎割安｜FAIL_INSEN｜19,460円｜💰184.0万円｜—｜⚡材料後出し
- 6227 AIMECHATEC Ltd.｜granville_oshime/ai_reversal｜⚡好調｜⚪妥当｜FAIL_INSEN｜5,770円｜💰56.1万円｜—｜📋カルテ窓 11/13(残12営業日)｜📑TOPIX新規採用（2026-10-30 組入）
- 4658 日本空調サービス｜granville_tenkan/ai_reversal｜⚡好調｜⚪妥当｜PASS｜1,545円｜💰15.4万円｜reversal 1,545（✅即時可）｜⏰決算 10/30(残3営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
  > 【業態】独立系の建設設備メンテ大手。空調に強み。リニューアル中心に工事も。アジア進出。
  > 【いま】終値1,545円・直近5日+0.00%（材料未確認）
  > 【調子】⚡好調（5/13）
  > 【水準】⚪妥当（4.0/7）— PER13.77倍・PEG1.4296・52週68.5% ／ 💰単元15.4万円
  > 【戦略】当日終値1,545円の指値で反転を取りにいく。SL1,528円（直近5日安値）
- 5208 Arisawa Mfg.Co., Ltd.｜granville_oshime/ai_reversal｜✅順調｜🔴過熱｜FAIL_UWAHIGE｜2,635円｜💰25.7万円｜—
- 8098 稲畑産業｜ai_reversal/granville_oshime｜✅順調｜🔴過熱｜FAIL_UWAHIGE｜4,505円｜💰45.1万円｜—｜⚡材料後出し
- 3433 TOCALO Co., Ltd.｜granville_tenkan/ai_reversal｜✅順調｜⚪妥当｜FAIL_UWAHIGE｜2,702円｜💰26.5万円｜—
- 6643 戸上電機製作所｜ai_reversal｜✅順調｜⚪妥当｜FAIL_INSEN｜5,120円｜💰50.7万円｜—｜⏰決算 11/04(残5営業日)
- 5706 三井金属鉱業｜ai_reversal｜🔻悪化｜🟡やや割高｜FAIL_INSEN｜2,054円｜💰20.8万円｜—
- 3103 ユニチカ｜ai_reversal/granville_rebound｜🔻悪化｜🟡やや割高｜FAIL_UWAHIGE｜1,233円｜💰12.0万円｜—
- 6590 芝浦メカトロニクス｜ai_reversal｜➖横ばい｜🟡やや割高｜FAIL_UWAHIGE｜3,220円｜💰31.3万円｜—
- 5302 日本カーボン｜ai_reversal｜➖横ばい｜🔴過熱｜FAIL_INSEN｜4,920円｜💰49.0万円｜—｜⚠日程不明｜📑TOPIX低減対象（次 10/30 第1回/8）
- 9432 NTT｜ai_reversal｜➖横ばい｜🔴過熱｜FAIL_INSEN｜174円｜💰1.7万円｜—｜⏰決算 11/04(残5営業日)
- 4203 住友ベークライト｜ai_reversal｜業績データ取得不可｜⚪妥当｜FAIL_UWAHIGE｜7,827円｜💰76.0万円｜—｜⏰決算 11/04(残5営業日)

## ⚡材料後出し
その日の足は開示前の情報。判定は参考値
- 6862 ミナトホールディングス｜FAIL_UWAHIGE｜📌剰余金の配当（中間配当）に関するお知らせ｜15:30
- 5027 AnyMind Group Inc.｜PASS｜📌AnyMind Group and Meta partner to connect social discovery with live commerce｜15:30
- 5034 unerry, Inc.｜FAIL_UWAHIGE｜📌譲渡制限付株式報酬としての自己株式の処分の払込完了に関するお知らせ｜15:30
- 6337 Tesec Corporation｜FAIL_INSEN｜📊2027年３月期  第２四半期（中間期）決算短信〔日本基準〕（連結）｜15:30
- 8386 百十四銀行｜FAIL_UWAHIGE｜📌Notice Regarding Revisions to the Full-Year Business Results Forecasts and Dividend Forecasts｜15:00
- 3296 NIPPON REIT Investment Corp｜FAIL_INSEN｜📌Notice Concerning Delays in Updating the Website｜16:20
- 3471 Mitsui Fudosan Logistics Park, Inc.｜FAIL_INSEN｜📌不動産投資信託証券に関する発行者等の運用体制に関する報告書 2026/10/27｜16:09
- 5344 MARUWA CO., LTD.｜FAIL_INSEN｜📊2027年３月期　第２四半期（中間期）決算短信〔日本基準〕（連結）｜15:30
- 7433 伯東｜FAIL_INSEN｜📌伯東、千葉県一宮町の「防災スマートポール」実証実験に技術協力｜16:00
- 6787 メイコー｜FAIL_INSEN｜📌Announcement of Execution of a Basic Agreement Regarding Acquisition of Shares of Unimicron Japan Co., Ltd.｜19:00
- 8098 稲畑産業｜FAIL_UWAHIGE｜📌Notice Concerning Changes in Associates Accounted for Using the Equity Method (Conversion to Subsidiaries)｜17:00
- 4848 フルキャストホールディングス｜FAIL_INSEN｜📦株式会社セイファートとの資本業務提携に関するお知らせ｜16:00
- 3562 No.1 Co., Ltd.｜PASS｜📌当社の幹部の人事に関するお知らせ｜15:30
- 6988 日東電工｜FAIL_INSEN｜📊2027年３月期 第２四半期（中間期）決算短信〔IFRS〕（連結）｜16:00
- 7751 キヤノン｜FAIL_INSEN｜📊2026年12月期 第3四半期決算短信〔米国基準〕(連結)｜15:30
- 7921 ＴＡＫＡＲＡ　＆　ＣＯＭＰＡＮＹ｜FAIL_INSEN｜📌Notice Concerning Personnel Changes｜15:00
- 5243 ｎｏｔｅ｜FAIL_UWAHIGE｜🔁Notice Regarding Acquisition of Treasury Shares and Purchase of Treasury Shares through Off-Auction Own Share Repurchase Trading (ToSTNeT-3)｜17:00
- 4373 Simplex Holdings,Inc.｜FAIL_INSEN｜📌シンプレクスとSBI生命、AX推進に向け協働｜15:30
- 7175 Imamura Securities Co.Ltd.｜FAIL_UWAHIGE｜📊2027年３月期 第２四半期（中間期）決算短信〔日本基準〕（非連結）｜15:30
- 8704 トレイダーズホールディングス｜FAIL_INSEN｜📌トレイダーズ証券：渋谷区立代々木中学校にて金融経済教育に関する出張授業を実施｜15:30

## 📢開示
使用URL: https://kabutan.jp/disclosures/?kubun=&date=20261027&page=1〜31（全31ページ・452行を取得。フォールバックなし）。週末分: なし（前営業日の取得は前夜実行済み）。
- 📌 6787 メイコー｜Announcement of Execution of a Basic Agreement Regarding Acquisition of Shares of Unimicron Japan Co., Ltd.｜19:00
- 📌 6787 メイコー｜ユニマイクロンジャパン株式会社の株式取得に関する基本合意書締結のお知らせ｜19:00
- 🔁 5243 ｎｏｔｅ｜Notice Regarding Acquisition of Treasury Shares and Purchase of Treasury Shares through Off-Auction Own Share Repurchase Trading (ToSTNeT-3)｜17:00
- 🔁 5243 ｎｏｔｅ｜自己株式の取得及び自己株式立会外買付取引（ToSTNeT-3）による自己株式の買付けに関するお知らせ｜17:00
- 📌 8098 稲畑産業｜Notice Concerning Changes in Associates Accounted for Using the Equity Method (Conversion to Subsidiaries)｜17:00
- 📌 8098 稲畑産業｜持分法適用関連会社の異動（子会社化）に関するお知らせ｜17:00
- 📌 3296 NIPPON REIT Investment Corp｜Notice Concerning Delays in Updating the Website｜16:20
- 📌 3296 NIPPON REIT Investment Corp｜ウェブサイト更新遅延に関するお知らせ｜16:20
- 📌 3296 NIPPON REIT Investment Corp｜Notice Concerning Transfer of Real Estate Trust Beneficiary Interests in Japan (FORECAST Ningyocho, Toranomon Sakura Building)｜16:20
- 📌 3296 NIPPON REIT Investment Corp｜Notice Concerning Revision of the Forecast of Management Status and Estimated Distribution for the Fiscal Period Ending December 2026 and the Fiscal｜16:20
- 📌 3296 NIPPON REIT Investment Corp｜国内不動産信託受益権の譲渡に関するお知らせ（FORECAST人形町、虎ノ門桜ビル）｜16:20
- 📌 3296 NIPPON REIT Investment Corp｜2026年12月期及び2027年6月期の運用状況及び分配金の予想の修正に関するお知らせ｜16:20
- 📌 3471 Mitsui Fudosan Logistics Park, Inc.｜不動産投資信託証券に関する発行者等の運用体制に関する報告書 2026/10/27｜16:09
- 📦 4848 フルキャストホールディングス｜株式会社セイファートとの資本業務提携に関するお知らせ｜16:00
- 📌 4848 フルキャストホールディングス｜Notice of Capital and Business Alliance with Seyfert LTD.｜16:00
- 📊 6988 日東電工｜2027年３月期 第２四半期（中間期）決算短信〔IFRS〕（連結）｜16:00
- 🔁 6988 日東電工｜剰余金の配当（中間配当）および期末配当予想の修正（増配）ならびに自己株式取得に関するお知らせ｜16:00
- 📌 6988 日東電工｜[Summary] Preliminary Summary of Consolidated Financial Statements for the Second Quarter Ended September 30, 2026 (IFRS Basis)｜16:00
- 📌 6988 日東電工｜Supplementary Data of Consolidated Financial Statements for the Second Quarter Ended September 30, 2026 (IFRS Basis)｜16:00
- 📌 6988 日東電工｜2027年３月期 第２四半期決算短信〔IFRS〕（連結）補足資料｜16:00
- 📌 6988 日東電工｜Financial Results Second Quarter FY2026｜16:00
- 📌 6988 日東電工｜Notice Regarding Dividends from Surplus (Interim Dividend), Revision of Year-End Dividend Forecast (Dividend Increase), and Share Repurchase｜16:00
- 📌 6988 日東電工｜2027年３月期 第２四半期決算短信〔IFRS〕（連結）決算説明資料｜16:00
- 📌 7433 伯東｜伯東、千葉県一宮町の「防災スマートポール」実証実験に技術協力｜16:00
- 📌 3562 No.1 Co., Ltd.｜当社の幹部の人事に関するお知らせ｜15:30
- 📌 4373 Simplex Holdings,Inc.｜シンプレクスとSBI生命、AX推進に向け協働｜15:30
- 📌 5027 AnyMind Group Inc.｜AnyMind Group and Meta partner to connect social discovery with live commerce｜15:30
- 📌 5027 AnyMind Group Inc.｜AnyMind Group、Metaとパートナーシップを締結し、ライブコマース領域での連携を開始｜15:30
- 📌 5034 unerry, Inc.｜譲渡制限付株式報酬としての自己株式の処分の払込完了に関するお知らせ｜15:30
- 📊 5344 MARUWA CO., LTD.｜2027年３月期　第２四半期（中間期）決算短信〔日本基準〕（連結）｜15:30
- 📌 5344 MARUWA CO., LTD.｜Differences between Consolidated Earnings Forecast and Results for the Cumulative Second Quarter of the Fiscal Year Ending March 31, 2027｜15:30
- 📌 5344 MARUWA CO., LTD.｜Notice Regarding Revision of Earnings Forecast for the Fiscal Year Ending March 31, 2027｜15:30
- 📌 5344 MARUWA CO., LTD.｜[Summary]Consolidated Financial Results for the Second Quarter of Fiscal Year 2026｜15:30
- 📌 5344 MARUWA CO., LTD.｜2027年３月期第２四半期（中間期）連結業績予想と実績の差異に関するお知らせ｜15:30
- 📌 5344 MARUWA CO., LTD.｜業績予想の修正に関するお知らせ｜15:30
- 📊 6337 Tesec Corporation｜2027年３月期  第２四半期（中間期）決算短信〔日本基準〕（連結）｜15:30
- 📌 6337 Tesec Corporation｜2027年３月期 第２四半期（中間期）決算補足説明資料（連結）｜15:30
- 📌 6337 Tesec Corporation｜剰余金の配当（中間配当）に関するお知らせ｜15:30
- 📌 6862 ミナトホールディングス｜剰余金の配当（中間配当）に関するお知らせ｜15:30
- 📊 7175 Imamura Securities Co.Ltd.｜2027年３月期 第２四半期（中間期）決算短信〔日本基準〕（非連結）｜15:30
- 📌 7175 Imamura Securities Co.Ltd.｜2027年３月期 第２四半期（中間期）決算説明資料｜15:30
- 📊 7751 キヤノン｜2026年12月期 第3四半期決算短信〔米国基準〕(連結)｜15:30
- 📌 7751 キヤノン｜Notice Regarding Execution of Merger Agreement for Merger (Simplified Absorption-type Merger) with Canon Electron Tubes & Devices Co., Ltd.｜15:30
- 📌 7751 キヤノン｜キヤノン電子管デバイス株式会社との合併（簡易吸収合併）に関する合併契約締結のお知らせ｜15:30
- 📌 7751 キヤノン｜Consolidated Financial Results for the Nine Months Ended September 30, 2026 (Under U.S. GAAP)｜15:30
- 📌 8704 トレイダーズホールディングス｜トレイダーズ証券：渋谷区立代々木中学校にて金融経済教育に関する出張授業を実施｜15:30
- 📌 7921 ＴＡＫＡＲＡ　＆　ＣＯＭＰＡＮＹ｜Notice Concerning Personnel Changes｜15:00
- 📌 7921 ＴＡＫＡＲＡ　＆　ＣＯＭＰＡＮＹ｜人事異動に関するお知らせ｜15:00
- 📌 7921 ＴＡＫＡＲＡ　＆　ＣＯＭＰＡＮＹ｜Notice Concerning Share Split and Partial Amendment to the Articles of Incorporation in Connection with the Share Split｜15:00
- 📌 7921 ＴＡＫＡＲＡ　＆　ＣＯＭＰＡＮＹ｜株式分割および株式分割に伴う定款の一部変更に関するお知らせ｜15:00
- 📌 8386 百十四銀行｜Notice Regarding Revisions to the Full-Year Business Results Forecasts and Dividend Forecasts｜15:00
- 📌 8386 百十四銀行｜業績予想及び配当予想の修正に関するお知らせ｜15:00
- 📌 8522 Bank of Nagoya, Ltd.｜Notice Concerning Unrealized Losses on Securities as of the End of the Second Quarter of the Fiscal Year Ending March 31, 2027｜14:00
- 📌 8522 Bank of Nagoya, Ltd.｜2027年3月期第2四半期末の有価証券含み損に関するお知らせ｜14:00
- 📌 8522 Bank of Nagoya, Ltd.｜Notice Concerning the Expected Recording of Gain on Return of Retirement Benefit Trust (Extraordinary Income)｜14:00
- 📌 8522 Bank of Nagoya, Ltd.｜退職給付信託返還益（特別利益）の計上見込みに関するお知らせ｜14:00
- 📊 8697 日本取引所グループ｜2027年３月期 第２四半期（中間期）決算短信〔ＩＦＲＳ〕（連結）｜12:00
- 📌 8697 日本取引所グループ｜Notice Regarding Share Split and Amendment to Articles of Incorporation｜12:00
- 📌 8697 日本取引所グループ｜Notice Regarding Cancellation of Treasury Shares｜12:00
- 📌 8697 日本取引所グループ｜[Explanatory Material] Overview of Earnings for Q2 FY2026｜12:00
- 📌 8697 日本取引所グループ｜Consolidated financial results for the six months ended September 30, 2026 (Based on IFRS), unaudited｜12:00
- 📌 8697 日本取引所グループ｜株式分割及び株式分割に伴う定款の一部変更に関するお知らせ｜12:00
- 📌 8697 日本取引所グループ｜自己株式の消却に関するお知らせ｜12:00
- 📌 8697 日本取引所グループ｜2026年度 第２四半期決算の概要｜12:00
- 📌 4667 Aisan Technology Co., Ltd.｜アイサンテクノロジー、ティアフォー車載HDRカメラ「MPシリーズ」の広角モデル2製品の取り扱いを開始｜10:00
- 📌 4071 Plus Alpha Consulting Co. LTD.｜家電量販店ケーズデンキを展開するケーズホールディングス、 約16,000名の人材データ活用基盤としてタレントマネジメントシステム 「タレントパレット」を導入｜08:59
- 📌 336A ダイナミックマッププラットフォーム｜ダイナミックマッププラットフォームと東芝、 インフラ協調型モビリティ基盤の高度化に向け協業検討を開始｜08:30
- 📌 9628 San Holdings,Inc.｜第97期定時株主総会資料｜08:00
- 📌 9628 San Holdings,Inc.｜第97期定時株主総会招集ご通知｜08:00

## 総当りゲート
### 5手法
- PASS（54）: 276A CCReB Advisors Inc.、4434 Serverworks Co., Ltd.、5027 AnyMind Group Inc.、212A FIT EASY Inc.、3915 TerraSky Co., Ltd.、9268 OPTIMUS GROUP Co., Ltd.、505A Geekly,Inc.、618A KOMPEITO Inc.、2930 北の達人コーポレーション、7161 Jimoto Holdings, Inc.、6875 メガチップス、8336 武蔵野銀行、3036 アルコニックス、6324 Harmonic Drive Systems Inc.、1803 Shimizu Corporation、8346 東邦銀行、5301 Tokai Carbon Co., Ltd.、7004 カナデビア、2874 YOKOREI CO. LTD.、8088 岩谷産業、8714 池田泉州ホールディングス、8399 琉球銀行、268A Rigaku Holdings Corporation、8381 San-in Godo Bank Ltd.、8524 North Pacific Bank, Ltd.、1861 Kumagai Gumi Co., Ltd.、1417 MIRAIT ONE Corporation、1860 Toda Corporation、2659 SAN-A CO., LTD.、5021 Cosmo Energy Holdings Co., Ltd.、1893 Penta-Ocean Construction Co., Ltd.、8953 Japan Metropolitan Fund Investment Corporation、1963 日揮ホールディングス、1969 高砂熱学工業、9699 NISHIO HOLDINGS CO. LTD.、9533 TOHO GAS Co., Ltd.、8370 紀陽銀行、5831 Shizuoka Financial Group, Inc.、7381 ＣＣＩグループ、8345 Bank of Iwate Ltd.、8367 南都銀行、7384 Procrea Holdings,Inc.、8174 NIPPON GAS Co., Ltd.、8334 Gunma Bank, Ltd.、8366 滋賀銀行、6471 日本精工、7186 横浜フィナンシャルグループ、7322 三十三フィナンシャルグループ、8354 ふくおかフィナンシャルグループ、8359 Hachijuni Nagano Bank, Ltd.、8600 トモニホールディングス、5246 ＥＬＥＭＥＮＴＳ、4443 Ｓａｎｓａｎ、6814 古野電
- PASS_DOJI（0）: なし
- FAIL_UWAHIGE（42）: 6627 Tera Probe, Inc.、6862 ミナトホールディングス、9554 AViC Co. Ltd.、5132 pluszero,Inc.、4377 ONE CAREER Inc.、5821 Hirakawa Hewtech Corp.、5034 unerry, Inc.、9560 PROGRIT, Inc.、7678 ASAKUMA CO.,LTD.、4412 Science Arts, Inc.、3374 Naigai Tec Corporation、7567 Sakae Electronics Corp.、446A ノースサンド、4379 Photosynth inc.、3843 Freebit Co., Ltd.、4331 Take and Give. Needs Co., Ltd.、4565 Nxera Pharma Co., Ltd.、6278 ユニオンツール、6268 ナブテスコ、7733 Olympus Corp.、8386 百十四銀行、5333 ＮＧＫ、7721 Tokyo Keiki Inc.、8393 Miyazaki Bank Ltd.、4666 Park24 Co., Ltd.、7731 ニコン、6925 Ushio Inc.、5331 ノリタケ、1952 Shin Nippon Air Technologies Co., Ltd.、7003 Mitsui ES Holdings Co., Ltd.、4966 上村工業、6055 Japan Material Co., Ltd.、3445 RS Technologies Co. Ltd.、5844 Kyoto Financial Group,Inc.、2379 dip Corporation、6479 ミネベア、8955 Japan Prime Realty Investment Corporation、1946 Toenec Corporation、5310 Toyo Tanso Co., Ltd.、3105 日清紡ホールディングス、6804 Hosiden Corp.、6532 ベイカレント
- FAIL_INSEN（106）: 3556 RenetJapanGroup, Inc.、4053 Sun Asterisk, Inc.、5136 tripla Co.,Ltd.、5757 CK San-Etsu Co., Ltd.、421A Movin' Strategic Career CO.,LTD.、6298 Y.A.C.HOLDINGS CO.,LTD.、5537 AlbaLink Co.,Ltd.、7047 PORT INC.、4058 Toyokumo, Inc.、6071 IBJ, Inc.、147A SORACOM,INC.、4477 BASE, Inc.、9628 San Holdings,Inc.、2980 SRE Holdings Corp.、4743 ITFOR Inc.、5038 eWeLL Co.,Ltd、6629 TECHNO HORIZON Co., Ltd.、6289 Giken Ltd.、3077 Horiifoodservice Co., Ltd.、6918 Aval Data Corporation、6337 Tesec Corporation、3696 セレス、2820 Yamami Co.、8871 GOLDCREST Co., Ltd.、3391 TSURUHA Holdings, Inc.、6645 OMRON Corporation、3222 United Super Markets Holdings, Inc.、4088 Air Water Inc.、6370 栗田工業、8522 Bank of Nagoya, Ltd.、6302 住友重機械工業、6754 アンリツ、8987 Japan Excellent, Inc.、8282 K'S HOLDINGS CORPORATION、6332 月島ホールディングス、9412 SKY Perfect JSAT Corporation、8125 Wakita & Co., Ltd.、8278 Fuji Co., Ltd.、7458 Daiichikosho Co., Ltd.、2782 Seria Co., Ltd.、2809 Kewpie Corporation、3279 Activia Properties, Inc.、3282 Comforia Residential REIT, Inc.、8952 Japan Real Estate Investment Corp.、8198 Maxvalu Tokai Co., Ltd.、1820 Nishimatsu Construction Co., Ltd.、1944 Kinden Corporation、3148 Create SD Holdings Co., Ltd.、6269 Modec, Inc.、8584 Jaccs Co., Ltd.、9882 Yellow Hat Ltd.、8066 Mitani Corporation、7984 Kokuyo Co., Ltd.、2805 S&B Foods Inc.、3289 Tokyu Fudosan Holdings Corp.、6674 ジーエス・ユアサ　コーポレーション、8818 Keihanshin Building Co., Ltd.、1333 Umios Corporation、1719 HAZAMA ANDO Corporation、1833 Okumura Corporation、9503 Kansai Electric Power Company, Incorporated、6366 Chiyoda Corp.、7220 Musashi Seimitsu Industry Co., Ltd.、6753 Sharp Corporation、8276 HEIWADO CO., LTD.、9974 BELC Co., Ltd.、3234 Mori Hills Reit Investment Corporation、3249 Industrial & Infrastructure Fund Investment Corporation、3283 Nippon Prologis REIT, Inc.、3292 AEON REIT Investment Corp.、3296 NIPPON REIT Investment Corp、3309 Sekisui House Reit. Inc.、3462 Nomura Real Estate Master Fund, Inc.、5482 Aichi Steel Corporation、8954 ORIX JREIT Inc.、8986 Daiwa Securities Living Investment Corporation、2815 ARIAKE JAPAN Co., Ltd.、5631 Japan Steel Works, Ltd.、6183 BELLSYSTEM24 Holdings, Inc.、9948 Arcs Company, Limited、4928 Noevir Holdings Co., Ltd.、6960 Fukuda Denshi Co., Ltd.、9436 Okinawa Cellular Telephone Company、1662 Japan Petroleum Exploration Co., Ltd.、8585 Orient Corporation、8194 Life Corporation、8253 Credit Saison Co., Ltd.、7201 Nissan Motor Co., Ltd.、8304 あおぞら銀行、3471 Mitsui Fudosan Logistics Park, Inc.、5344 MARUWA CO., LTD.、8961 MORI TRUST REIT.Inc、3591 WACOAL HOLDINGS CORP、8511 Japan Securities Finance Co., Ltd.、6668 ＡＤプラズマ、7624 NaITO、7713 シグマ光機、5018 ＭＯＲＥＳＣＯ、3498 霞ヶ関Ｃ、3994 マネーフォワード、7811 中本パックス、5932 三協立山、3091 ブロンコビリー、3479 ＴＫＰ、6505 東洋電機製造、4176 ココナラ
- SKIP（0）: なし
### グランビル
- PASS（45）: 5254 Arent, Inc.、3927 アークン、9553 MicroAd, Inc.、3496 アズーム、6255 NPC Incorporated、7744 Noritsu Koki Co., Ltd.、3741 Systems Engineering Consultants Co., Ltd.、3562 No.1 Co., Ltd.、8020 Kanematsu Corporation、186A Astroscale Holdings Inc.、4272 Nippon Kayaku Co., Ltd.、7181 JAPAN POST INSURANCE Co., Ltd.、8012 Nagase & Co., Ltd.、4617 中国塗料、6328 Ebara Jitsugyo Co., Ltd.、4902 Konica Minolta, Inc.、5105 ＴＯＹＯ　ＴＩＲＥ、290A ＳＹＮＳＰＥＣＴＩＶＥ、4180 ＡＰＰＩＥＲ　ＧＲＯＵＰ、4431 スマレジ、6023 ダイハツインフィニアース、3106 倉敷紡績、2767 円谷フィールズホールディングス、7350 Okinawa Financial Group, Inc.、4475 HENNGE K.K.、6998 Nippon Tungsten Co., Ltd.、3107 ダイワボウホールディングス、4044 Central Glass Co., Ltd.、456A Human Made Inc.、7504 Kohsoku Corporation、9509 Hokkaido Electric Power Company,Incorporated、9505 Hokuriku Electric Power Company、8361 Ogaki Kyoritsu Bank, Ltd.、8343 Akita Bank, Ltd.、6027 弁護士ドットコム、8362 Fukui Bank, Ltd.、8364 清水銀行、278A Ｔｅｒｒａ　Ｄｒｏｎｅ、4346 NEXYZ.Group Corporation、3907 Silicon Studio Corp.、8360 Yamanashi Chuo Bank, Ltd.、7380 Juroku Financial Group,Inc.、8368 Hyakugo Bank, Ltd.、8713 Fidea Holdings Co.Ltd.、8377 ほくほくフィナンシャルグループ
- PASS_DOJI（3）: 5985 SUNCALL CORPORATION、6963 ROHM Company Limited、6490 ＰＩＬＬＡＲ
- FAIL_UWAHIGE（42）: 7725 INTER ACTION Corporation、8793 ＮＥＣキャピタルソリューション、8061 Seika Corporation、2331 ALSOK CO., LTD.、7970 Shin-Etsu Polymer Co., Ltd.、6454 Max Co., Ltd.、5036 Japan Business Systems, Inc.、8014 Chori Co., Ltd.、4549 Eiken Chemical Co., Ltd.、6371 Tsubakimoto Chain Co.、4956 Konishi Co., Ltd.、6208 Ishikawa Seisakusho,Ltd.、5233 太平洋セメント、7747 朝日インテック、5243 ｎｏｔｅ、7806 MTG Co., Ltd.、6613 QD Laser, Inc.、3156 レスター、9902 Nichiden Corporation、6523 PHC Holdings Corp.、7609 ダイトロン、4667 Aisan Technology Co., Ltd.、6250 Yamabiko Corporation、6570 Kyowa Corporation Co. Ltd.、3097 Monogatari Corporation、9900 Sagami Holdings Corp.、9536 SAIBU GAS HOLDINGS CO. LTD.、9166 GENDA Inc.、6340 澁谷工業、6769 Thine Electronics, Inc.、479A PRONI Inc.、8995 Makoto Construction Co,Ltd、5242 EYEZ INC.、477A Startline CO.,LTD.、6336 石井表記、2354 YE DIGITAL CORPORATION、4100 Toda Kogyo Corp.、3653 Morpho, Inc.、4440 WITZ Corp.、8163 SRS HOLDINGS CO.,LTD.、6203 Howa Machinery, Ltd.、7175 Imamura Securities Co.Ltd.
- FAIL_INSEN（102）: 8944 Land Business Co., Ltd.、6905 Cosel Co., Ltd.、2986 LA Holdings Co.,Ltd、9211 f-code Inc.、6562 Geniee, Inc.、6473 JTEKT Corporation、8697 日本取引所グループ、4534 Mochida Pharmaceutical Co., Ltd.、3405 クラレ、8095 Astena Holdings Co.,Ltd.、9064 ヤマトホールディングス、4544 H.U.Group Holdings, Inc.、5838 Rakuten Bank, Ltd.、4763 クリーク・アンド・リバー社、6470 Taiho Kogyo Co., Ltd.、7199 プレミアグループ、4848 フルキャストホールディングス、3935 Edia Co. Ltd.、6196 Strike Group Co. Ltd.、6768 Tamura Corporation、4169 Enechange Ltd.、4568 第一三共、3661 m-up holdings, Inc.、6432 竹内製作所、9828 Genki Global Dining Concepts Corp、2288 Marudai Food Co., Ltd.、5184 ニチリン、6592 Mabuchi Motor Co., Ltd.、6988 日東電工、4166 Cacco, Inc.、8850 スターツコーポレーション、9163 Nareru Group Inc.、8927 Meiho Enterprise Co., Ltd.、3569 セーレン、4183 Mitsui Chemicals, Inc.、5461 Chubu Steel Plate Co., Ltd.、7734 Riken Keiki Co., Ltd.、7513 Kojima Co., Ltd.、4552 JCR Pharmaceuticals Co., Ltd.、8081 Kanaden Corporation、9837 Morito Co., Ltd.、7751 キヤノン、6770 Alps Alpine Co., Ltd.、8167 リテールパートナーズ、1815 鉄建建設、4375 セーフィー、8424 芙蓉総合リース、4912 ライオン、2871 ニチレイ、7921 ＴＡＫＡＲＡ　＆　ＣＯＭＰＡＮＹ、4937 Ｇ−ＷＡＱＯＯ、6834 Seikoh Giken Co., Ltd.、8008 Yondoshi Holdings, Inc.、7856 HAGIHARA INDUSTRIES INC.、1879 新日本建設、6736 Suncorporation、2602 日清オイリオグループ、4413 baudroie,inc.、8919 カチタス、8410 Seven Bank, Ltd.、7616 Colowide Co., Ltd.、9304 澁澤倉庫、6058 VECTOR Inc.、4373 Simplex Holdings,Inc.、1518 三井松島ホールディングス、4208 UBE Corporation、6379 RAIZNEXT Corporation、9044 NANKAI Co., Ltd.、6072 Jibannet Holdings Co., Ltd.、7630 Ichibanya Co., Ltd.、8043 Starzen Company Limited、9616 共立メンテナンス、8255 Axial Retailing, Inc.、8097 SAN-AI OBBLI CO. LTD、8059 Daiichi Jitsugyo Co., Ltd.、336A ダイナミックマッププラットフォーム、6810 マクセル、8051 山善、8622 Mito Securities Co., Ltd.、8624 Ichiyoshi Securities Co., Ltd.、8628 松井証券、3691 DIGITAL PLUS, Inc.、1436 GreenEnergy & Company、2122 インタースペース、8344 Yamagata Bank, Ltd.、8392 大分銀行、6597 HPC SYSTEMS Inc.、3687 Fixstars Corp.、5574 ABEJA,Inc.、9278 BOOKOFF GROUP HOLDINGS LIMITED、7256 河西工業、4997 日本農薬、1407 West Holdings Corporation、7354 Direct Marketing MiX Inc.、2681 2nd RETAILING Co., Ltd.、4082 第一稀元素化学工業、4691 Washington Hotel Corp.、6522 アスタリスク、3778 SAKURA Internet Inc.、6890 Ferrotec Corporation、7715 長野計器、8739 スパークス・グループ
- SKIP（0）: なし
### 変化点
- PASS（6）: 584A LiNKX, Inc.、8151 東陽テクニカ、5590 NETSTARS Co.,Ltd.、6284 日精エー・エス・ビー機械、6785 鈴木、4478 freee K.K.
- PASS_DOJI（0）: なし
- FAIL_UWAHIGE（12）: 4011 Headwaters Co.,Ltd、6857 アドバンテスト、9962 ミスミグループ本社、4382 HEROZ, Inc.、4368 4368、218A Liberaware、4165 PLAID Inc.、4498 Cybertrust Japan Co., Ltd.、4493 Cyber Security Cloud, Inc.、4259 ExaWizards Inc.、3993 PKSHA Technology, Inc.、593A ティアフォー
- FAIL_INSEN（16）: 265A エイチエムコム、5803 フジクラ、4187 大阪有機化学工業、9888 UEX LTD、7695 交換できるくん、6080 Ｍ＆Ａキャピタルパートナーズ、6136 OSG CORP、7318 セレンディップ・ホールディングス、5582 （名称取得不可）、478A Hutzper Inc.、8704 トレイダーズホールディングス、4071 Plus Alpha Consulting Co. LTD.、4418 Japan Data Science Consortium Co Ltd.、598A チャットプラス、339A PROGRESS TECHNOLOGIES GROUP INC、4488 AI inside Inc.
- SKIP（0）: なし
### AI特需
- PASS（2）: 6521 オキサイド、4658 日本空調サービス
- PASS_DOJI（0）: なし
- FAIL_UWAHIGE（11）: 9960 トーテック、6254 野村マイクロ・サイエンス、6235 オプトラン、7729 東京精密、6752 パナソニックHD、5208 Arisawa Mfg.Co., Ltd.、8098 稲畑産業、3433 TOCALO Co., Ltd.、3103 ユニチカ、6590 芝浦メカトロニクス、4203 住友ベークライト
- FAIL_INSEN（18）: 3131 シンデン・ハイテックス、2760 東京エレクトロン　デバイス、9824 泉州電業、1982 日比谷総合設備、4047 関東電化工業、4971 メック、3110 日東紡、6981 村田製作所、7433 伯東、4062 イビデン、6524 湖北工業、6779 Nihon Dempa Kogyo Co., Ltd.、6787 メイコー、6227 AIMECHATEC Ltd.、6643 戸上電機製作所、5706 三井金属鉱業、5302 日本カーボン、9432 NTT
- SKIP（0）: なし
### 除籍（first_seenから30暦日超）
なし

## 機械詳細
- 派生ファイル: grades.json 948銘柄/534.4KiB（nx非null 759・lx 395・pxd 280）、pool_bars.json 460銘柄/394.4KiB、earnings_calendar.json 948銘柄/122.7KiB（nx非null 759・次回決算日 付与 759件）
- gate_history: gate_history/2026-10-27.json を新規作成（verdicts 459件=評価459件／nominations 85件）
- 抜粋規則: 通知【通過】10件（method/ai/granville/changepoint の群別ラウンドロビン）。PASS群別内訳 method54/ai2/granville48/changepoint6
- method_score 保持55件/null404件
- ヘッドライン付与 110件（PASS全件110と一致: True）
- kabutan 取得: 決算ページ113件・トップページ4件（上限50件に対し4件・打ち切り0件）。業種の埋め戻し 0件（プール在籍で未付与だった銘柄）
- profile_cache 総数930・本夜追加3件・業態が「未取得」のまま出た件数 0
- earnings_log 総数86／本夜追記6件／リターン補完3件／日足が取れず未補完25件
- gyoseki_cache 再計算 1件（history 退避 0件）: 8364(キャッシュ無し)
- 鮮度ゲート: 鮮度切れ除外15件・nom_age分布 0-2:151/3-10:198/11+:110・last_seen欠損0件
- 記録の凍結: verdicts 459件・nominations 85件（新規10・再指名75）・業種 付与済み458/未付与1
- トレンド文脈: ctx 不一致198・合致128・レンジ129・判定不能3・PASS のうち ctx 合致 34件・形態が付いた銘柄 189件
- 3日ルール: 判定3銘柄・streak≥3 0・streak=2 2・判定不可0
- 業種別PER中央値: 算出26業種・spm 付与 894件
- 開示の分類別件数: 📢0/📉0/📊6/🔁3/👥0/🏛0/📦1/📌59
- 熟成由来(value_gap)の候補 0件（watchlist に nominate_for=2026-10-27 なし）
- 権利情報: rights_cache 総数451・本夜 配当 新規31件/更新50件・優待取得 0件（取得元がプロキシ403のため全て不明のまま）
- 次回決算日: 付与759件／未発表189件・前年同期発表日 付与280件
- STEP 4.8 週末ブリーフ: スキップ（week_open=false）
- master.json の変更行数: +10153/-8489（indent=2・往復一致）
