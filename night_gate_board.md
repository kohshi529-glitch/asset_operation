# 夜間ゲート 2026-10-14

## サマリー
- 評価数: 368 / PASS: 35（PASS_DOJI含め35）
- 発注可能提案数: 26件
- 市場一言: 市場モード「レンジ様子見」（market.latest 2026-10-14）。プール368銘柄中PASS比率9.5%（陰線FAIL 260件・上髭FAIL 73件）
- 実行モード: 通常（base_day=当日の引け値を対象）
- base_day: 2026-10-14（run_at 2026-10-14 20:41）
- week_open: false（翌営業日10/15(木)は週初でない）→ STEP 4.8 週末ブリーフはスキップ
- 📆 翌営業日 10/15: カレンダーイベントなし。T+2 10/16(金): カレンダーイベントなし。次の TOPIX 低減日 10/30(金) 第1回/8（あと12営業日）
- 📑指数: 低減対象 提案5件／PASS8件／プール58件・新規採用 11件（index_flags 2026-10-07 公表分）

## 検証結果
- V1 → はい（proposals26=results26=template26）
- V2 → はい（35=26+9・order_status欠落0）
- V3 → はい（code重複0件）
- V4 → はい（既存static変更0件）
- V5 → はい（許可キー外の変更0件）
- V6 → はい（不整合0件）
- V8 → はい（書式不正0件）
- V9 → はい（本体一致）
- V10 → はい（4箇所一致 {'2026-10-14'}）
- V11 → いいえ（+8392/-8281（indent=2））（目安5,000行を超過: results全置換と各キャッシュ更新のため。全体再フォーマットではない=indent検出値2を使用）
- V12 → はい（(a)True(b)True(c)True）
- V13 → いいえ（841銘柄/407765B（(d)350KB以下: いいえ））（(d)のみ超過: 銘柄数増加が原因。(a)(b)(c)(e)(f)は成立）
- V14 → はい（保持55件/null313件）
- V15 → いいえ（PASS35件中35件・欠落0・「未取得」混入1）（(a)(b)成立。3697の「調子」はキャッシュ値自体が『取得不可』であり組立不具合ではない）
- V16 → はい（earnings_log48件・本夜追記10件・history>4件0）
- V17 → はい（368銘柄/323607B・保有4銘柄すべて収録・3日ルール判定4/4件）
- V18 → はい（鮮度切れ6件・誤除外0）
- V19 → はい（verdicts368=評価368・nominations87(新規20/再指名67)・ctx判定不能6件）
- V7 → はい（必須セクション存在・week_open=false のため今週のカタリスト不要）
- 公開物の保有情報チェック → はい（保有の数量・建値・損益・R/streak 等の記載なし。件数のみ: 保有4銘柄・アラート16件）

## 保有アラート
保有4銘柄・アラート16件（詳細は通知）

## 前夜の結果
PL5口座への正式な反映は週次①-11の採点で行われる。ここは参考情報。
前夜2026-10-13の提案68件 → 約定45・不約定23・判定不能0
- 6862 momentum 指定5200 → 約定5200・終値5120（-1.54%）
- 8871 reversal 指定2949 → 約定2949・終値2927（-0.75%）
- 1803 reversal 指定2045 → 約定2045・終値2034.5（-0.51%）
- 8088 reversal 指定1974.5 → 約定1974.5・終値1957.5（-0.86%）
- 9412 reversal 指定1851 → 約定1851・終値1882（+1.67%）
- 8125 reversal 指定1825 → 約定1825・終値1815（-0.55%）
- 8934 reversal 指定2156 → 約定2146・終値2122（-1.12%）
- 8584 reversal 指定3470 → 約定3470・終値3435（-1.01%）
- 2805 reversal 指定6490 → 約定6490・終値6230（-4.01%）
- 7984 reversal 指定870.2 → 約定868.5・終値871.2（+0.31%）
- 3289 reversal 指定1193.5 → 約定1190・終値1177.5（-1.05%）
- 1719 reversal 指定1724 → 約定1724・終値1719（-0.29%）
- 1833 reversal 指定5270 → 約定5270・終値5220（-0.95%）
- 9974 reversal 指定6250 → 約定6180・終値6020（-2.59%）
- 5482 reversal 指定2898 → 約定2881・終値2863（-0.62%）
- 4928 reversal 指定4640 → 約定4600・終値4645（+0.98%）
- 1662 reversal 指定1720 → 約定1720・終値1722（+0.12%）
- 6183 reversal 指定1296 → 約定1296・終値1299（+0.23%）
- 8961 reversal 指定67200 → 約定67200・終値66700（-0.74%）
- 4443 changepoint 指定2025 → 約定2013・終値1924（-4.42%）
- 2760 momentum 指定4980 → 約定4980・終値5170（+3.82%）
- 8159 momentum 指定4700 → 約定4710・終値4770（+1.27%）
- 1982 momentum 指定3405 → 約定3405・終値3410（+0.15%）
- 9960 momentum 指定4255 → 約定4255・終値4250（-0.12%）
- 3496 momentum 指定4675 → 約定4695・終値4725（+0.64%）
- 9064 momentum 指定2077 → 約定2077・終値2085（+0.39%）
- 8020 momentum 指定2314.5 → 約定2326・終値2354（+1.20%）
- 3479 momentum 指定1866 → 約定1870・終値1851（-1.02%）
- 8014 momentum 指定4265 → 約定4265・終値4275（+0.23%）
- 6988 momentum 指定3656 → 約定3656・終値3633（-0.63%）
- 6371 momentum 指定2677 → 約定2677・終値2643（-1.27%）
- 4183 momentum 指定2078 → 約定2089・終値2134（+2.15%）
- 4272 momentum 指定2165 → 約定2165・終値2178（+0.60%）
- 4956 momentum 指定1501 → 約定1505・終値1512（+0.47%）
- 7181 momentum 指定1711.5 → 約定1711.5・終値1691.5（-1.17%）
- 6208 momentum 指定1717 → 約定1717・終値1690（-1.57%）
- 8919 oshime 指定3515 → 約定3475・終値3385（-2.59%）
- 6998 oshime 指定3870 → 約定3870・終値3905（+0.90%）
- 8995 reversal 指定1683 → 約定1673・終値1737（+3.83%）
- 4382 changepoint 指定1398 → 約定1308・終値1400（+7.03%）
- 9888 changepoint 指定1227 → 約定1227・終値1214（-1.06%）
- 4180 changepoint 指定1410 → 約定1393・終値1372（-1.51%）
- 339A changepoint 指定921 → 約定921・終値912（-0.98%）
- 8151 changepoint 指定1918 → 約定1907・終値1920（+0.68%）
- 286A changepoint 指定765 → 約定759・終値753（-0.79%）

## 模擬テンプレ
```
# base_day 2026-10-14 ／ 提案26件
# 使い方: 参戦する0〜3銘柄の行だけをコピーし、｜の後ろに参戦理由を書いてポジション株PJへ送る。
# 選ばなかった行は送らなくてよい（全行に理由を書く必要はない）。見送りは末尾の1行で足りる。
# 特定銘柄を理由つきで見送る場合のみ『模擬 見送り {code} ｜{理由}』を送る。
模擬 5136 kenmo_momentum 逆指値2675 SL2513.6 単元100 ｜
模擬 5892 kenmo_momentum 逆指値3045 SL2857.6 単元100 ｜
模擬 9268 kenmo_momentum 逆指値363 SL340.3 単元100 ｜
模擬 9628 kenmo_momentum 逆指値1332 SL1251.1 単元100 ｜
模擬 8282 choruko_reversal 指値1676 SL1635.5 単元100 ｜
模擬 9412 choruko_reversal 指値1882 SL1826 単元100 ｜
模擬 7003 choruko_reversal 指値3929 SL3868 単元100 ｜
模擬 4928 choruko_reversal 指値4645 SL4395 単元100 ｜
模擬 9699 choruko_reversal 指値4215 SL3935 単元100 ｜
模擬 5036 granville_tenkan 逆指値1759 SL1652.5 単元100 ｜
模擬 8014 granville_tenkan 逆指値4290 SL4027.9 単元100 ｜
模擬 3549 granville_tenkan 逆指値4236 SL3977.1 単元100 ｜
模擬 4183 granville_tenkan 逆指値2135 SL2006 単元100 ｜
模擬 2413 granville_tenkan 逆指値1918 SL1802 単元100 ｜
模擬 8081 granville_tenkan 逆指値2809 SL2639.5 単元100 ｜
模擬 7856 granville_oshime 指値2028 SL2017.8 単元100 ｜
模擬 7616 granville_oshime 指値2036 SL2025.5 単元100 ｜
模擬 9678 granville_oshime 指値5420 SL5393.2 単元100 ｜
模擬 1518 granville_oshime 指値2275 SL2263.7 単元100 ｜
模擬 4418 granville_oshime 指値1112 SL1106.8 単元100 ｜
模擬 6379 granville_oshime 指値996 SL991.5 単元100 ｜
模擬 2122 granville_rebound 指値1365 SL1300 単元100 ｜
模擬 4392 granville_rebound 指値990 SL835 単元100 ｜
模擬 5242 granville_rebound 指値1873 SL1815 単元100 ｜
模擬 6522 granville_rebound 指値1063 SL1016 単元100 ｜
模擬 4165 changepoint🔔 指値752 SL701 単元100 🔒 ｜
模擬 見送り ｜
```

## PASS内訳
PASS 35件 = 発注可能 26件 + 除外 9件（型不一致0/材料後出し1/鮮度切れ6/その他2）
- 7624 NaITO｜⛔提案なし(手法ブランチ不明)
- 7713 シグマ光機｜⛔提案なし(手法ブランチ不明)
- 9560 PROGRIT, Inc.｜⛔提案なし(材料後出し)
- 鮮度切れ: 1871(15営業日)、3697(15営業日)、6317(18営業日)、6336(16営業日)、8093(15営業日)、9468(15営業日)

## 5手法銘柄
- 6627 Tera Probe, Inc.｜kenmo_momentum｜🚀確変(13)｜🟢値頃｜FAIL_INSEN｜2,459円｜💰25.1万円｜—
- 5137 Smart Drive Co. Ltd.｜kenmo_momentum+granville_oshime｜🚀確変(12)｜💎割安｜FAIL_INSEN｜310円｜💰3.1万円｜—
- 3723 Nihon Falcom Corporation｜kenmo_momentum｜🚀確変(11)｜🟢値頃｜FAIL_INSEN｜2,475円｜💰25.1万円｜—
- 5724 Asaka Riken Co., Ltd.｜kenmo_momentum｜🚀確変(11)｜🟢値頃｜FAIL_INSEN｜2,681円｜💰27.6万円｜—
- 4053 Sun Asterisk, Inc.｜granville_tenkan+kenmo_momentum+kenmo_newhigh｜🚀確変(11)｜⚪妥当｜FAIL_INSEN｜567円｜💰5.6万円｜— 🎯
- 5027 AnyMind Group Inc.｜kenmo_momentum｜🚀確変(11)｜⚪妥当｜FAIL_UWAHIGE｜817円｜💰8.1万円｜—
- 5136 tripla Co.,Ltd.｜stf_kakuhen+kenmo_momentum+kenmo_newhigh｜🚀確変(11)｜⚪妥当｜PASS｜2,671円｜💰26.7万円｜momentum 2675 想定損失幅6.0%。｜⚠日程不明
  > 【業態】宿泊予約システムや会話ツールのAIチャットボットシステム提供。決済システムも。アジアに拡大。
  > 【いま】終値2,671円・直近5日+4.91%（材料未確認）
  > 【調子】🚀確変（11/13）
  > 【水準】⚪妥当（3.0/7）— PER26.393倍・PEG0.4473・52週94.6% ／ 💰単元26.7万円
  > 【戦略】当日高値超えの逆指値2675円で順張り参戦を検討。上限2701.8円・SL2513.6円目安
- 5757 CK San-Etsu Co., Ltd.｜kenmo_momentum｜🔥絶好調(10)｜💎割安｜FAIL_UWAHIGE｜5,000円｜💰51.2万円｜—
- 479A PRONI Inc.｜kenmo_momentum+kenmo_newhigh｜🔥絶好調(10)｜🟢値頃｜FAIL_UWAHIGE｜1,888円｜💰19.1万円｜—
- 212A FIT EASY Inc.｜kenmo_momentum｜🔥絶好調(10)｜⚪妥当｜FAIL_INSEN｜2,801円｜💰28.2万円｜—
- 9554 AViC Co. Ltd.｜kenmo_momentum｜🔥絶好調(10)｜⚪妥当｜FAIL_INSEN｜1,688円｜💰17.2万円｜—
- 421A Movin' Strategic Career CO.,LTD.｜kenmo_momentum｜🔥絶好調(10)｜⚪妥当｜FAIL_INSEN｜3,960円｜💰42.0万円｜—
- 9211 f-code Inc.｜kenmo_momentum+changepoint🔔+changepoint｜🔥絶好調(9)｜💎割安｜FAIL_INSEN｜1,436円｜💰14.7万円｜—
- 4412 Science Arts, Inc.｜kenmo_momentum｜🔥絶好調(9)｜🟢値頃｜FAIL_INSEN｜1,348円｜💰13.7万円｜—
- 6298 Y.A.C.HOLDINGS CO.,LTD.｜kenmo_momentum｜🔥絶好調(9)｜🟢値頃｜FAIL_UWAHIGE｜1,237円｜💰12.4万円｜—
- 4377 ONE CAREER Inc.｜kenmo_momentum｜🔥絶好調(9)｜⚪妥当｜FAIL_INSEN｜2,563円｜💰26.0万円｜—
- 5537 AlbaLink Co.,Ltd.｜kenmo_momentum+kenmo_newhigh｜🔥絶好調(9)｜⚪妥当｜FAIL_INSEN｜3,775円｜💰41.4万円｜—
- 9556 INTLOOP, Inc.｜kenmo_momentum｜🔥絶好調(8)｜💎割安｜FAIL_INSEN｜2,195円｜💰22.5万円｜—
- 7047 PORT INC.｜kenmo_momentum｜🔥絶好調(8)｜🟢値頃｜FAIL_INSEN｜2,194円｜💰22.1万円｜—
- 2334 Eole, Inc.｜granville_oshime+kenmo_momentum｜🔥絶好調(8)｜⚪妥当｜FAIL_UWAHIGE｜582円｜💰5.8万円｜—
- 135A VRAIN Solution,Inc.｜kenmo_momentum+kenmo_newhigh+granville_oshime｜🔥絶好調(8)｜🟡やや割高｜FAIL_INSEN｜4,895円｜💰49.2万円｜—｜⚡材料後出し
- 146A Columbia Works Inc.｜granville_oshime+kenmo_momentum｜⚡好調(7)｜💎割安｜FAIL_INSEN｜3,485円｜💰35.7万円｜—
- 5590 ネットスターズ｜changepoint🔔+changepoint+kenmo_momentum+granville_tenkan｜⚡好調(7)｜🟢値頃｜FAIL_INSEN｜723円｜💰7.3万円｜—
- 5821 Hirakawa Hewtech Corp.｜kenmo_momentum｜⚡好調(7)｜🟢値頃｜FAIL_UWAHIGE｜3,265円｜💰32.6万円｜—
- 5892 yutori,Inc.｜kenmo_momentum+changepoint🔔｜⚡好調(7)｜⚪妥当｜PASS｜3,030円｜💰30.3万円｜momentum 3045 想定損失幅6.2%。｜⚠日程不明
  > 【業態】若者向け衣料品や雑貨などブランドの企画・卸売。EC販売が主軸。ZOZO傘下。
  > 【いま】終値3,030円・直近5日+1.34%（材料未確認）
  > 【調子】⚡好調（7/13）
  > 【水準】⚪妥当（4.0/7）— PER20.669倍・PEG0.6878・52週65.9% ／ 💰単元30.3万円
  > 【戦略】当日高値超えの逆指値3045円で順張り参戦を検討。上限3075.4円・SL2857.6円目安
- 6071 IBJ, Inc.｜kenmo_momentum｜⚡好調(7)｜⚪妥当｜FAIL_INSEN｜919円｜💰9.3万円｜—
- 9560 PROGRIT, Inc.｜kenmo_momentum｜⚡好調(7)｜⚪妥当｜PASS｜950円｜💰9.5万円｜⛔提案なし(材料後出し)｜⚠日程不明 ⚡材料後出し
  > 【業態】英語コーチングサービス、サブスクリプション型英語学習サービスの提供を手掛ける。
  > 【いま】終値950円・直近5日+7.59%・📊2026年８月期決算短信〔日本基準〕(連結)
  > 【調子】⚡好調（7/13）
  > 【水準】⚪妥当（4.0/7）— PER11.059倍・PEG0.5729・52週75.8% ／ 💰単元9.5万円
  > 【戦略】発注対象外（⛔提案なし(材料後出し)）
- 558A SQUEEZE Inc.｜kenmo_momentum+kenmo_newhigh｜⚡好調(7)｜🟡やや割高｜FAIL_INSEN｜5,960円｜💰60.6万円｜—
- 9268 OPTIMUS GROUP Co., Ltd.｜kenmo_momentum｜⚡好調(6)｜💎割安｜PASS_DOJI｜360円｜💰3.6万円｜momentum 363 想定損失幅6.3%。｜⚠日程不明
  > 【業態】ニュージーランド中心に中古車輸出。現地で自動車総合サービス展開。豪にも進出。
  > 【いま】終値360円・直近5日-13.25%（材料未確認）
  > 【調子】⚡好調（6/13）
  > 【水準】💎割安（7.0/7）— PER7.692倍・PEG0.6862・52週22.7% ／ 💰単元3.6万円
  > 【戦略】当日高値超えの逆指値363円で順張り参戦を検討。上限366.6円・SL340.3円目安
- 4477 BASE, Inc.｜kenmo_momentum｜⚡好調(6)｜⚪妥当｜FAIL_UWAHIGE｜387円｜💰3.8万円｜—
- 2980 SRE Holdings Corp.｜kenmo_momentum｜⚡好調(5)｜🟢値頃｜FAIL_UWAHIGE｜2,363円｜💰23.6万円｜—
- 3798 ULS Group Incorporated｜granville_tenkan+kenmo_momentum｜✅順調(4)｜💎割安｜FAIL_INSEN｜531円｜💰5.3万円｜—
- 4743 ITFOR Inc.｜kenmo_momentum｜✅順調(4)｜🟢値頃｜FAIL_UWAHIGE｜1,628円｜💰16.3万円｜—｜⚡材料後出し
- 505A Geekly,Inc.｜kenmo_momentum｜✅順調(4)｜🟢値頃｜FAIL_UWAHIGE｜1,375円｜💰13.8万円｜—｜⚡材料後出し
- 5038 eWeLL Co.,Ltd｜kenmo_momentum｜✅順調(4)｜⚪妥当｜FAIL_INSEN｜2,298円｜💰23.0万円｜—
- 6629 TECHNO HORIZON Co., Ltd.｜granville_tenkan+kenmo_momentum｜✅順調(4)｜⚪妥当｜FAIL_INSEN｜1,000円｜💰10.2万円｜—｜⚡材料後出し
- 6289 Giken Ltd.｜granville_tenkan+kenmo_momentum｜⚠減速(1)｜🔴過熱｜FAIL_UWAHIGE｜2,040円｜💰19.8万円｜—
- 6492 Okano Valve Mfg. Co., Ltd.｜kenmo_momentum｜判定保留(変則決算)｜⚪妥当｜FAIL_INSEN｜14,040円｜💰141.4万円｜—
- 6862 Minato Holdings Inc.｜kenmo_momentum｜判定保留(変則決算)｜⚪妥当｜FAIL_UWAHIGE｜5,120円｜💰51.0万円｜—
- 325A TENTIAL, Inc.｜kenmo_momentum+kenmo_newhigh｜判定保留(変則決算)｜⚪妥当｜FAIL_INSEN｜1,928円｜💰19.5万円｜—
- 9628 San Holdings,Inc.｜kenmo_momentum｜判定保留(変則決算)｜🟡やや割高｜PASS｜1,329円｜💰13.3万円｜momentum 1332 想定損失幅6.1%。 移行措置銘柄: 10/30 の引けにパッシブ売り（8回に分けて低減）。実施日前後の寄り・引けの需給に注意｜⚠決算 10/15(残1営業日) 📑TOPIX低減対象（次 10/30 第1回/8）
  > 【業態】葬儀サービスの統括会社。葬儀専門最大手の公益社やタルイなどが傘下に。
  > 【いま】終値1,329円・直近5日+2.47%（材料未確認）
  > 【調子】判定保留(変則決算)
  > 【水準】🟡やや割高（2.8/7）— PER6.907倍・PEG—・52週18.7% ／ 💰単元13.3万円
  > 【戦略】当日高値超えの逆指値1332円で順張り参戦を検討。上限1345.3円・SL1251.1円目安
- 3077 Horiifoodservice Co., Ltd.｜kenmo_momentum｜—｜－未評価｜FAIL_INSEN｜1,395円｜💰—｜—
- 6918 Aval Data Corporation｜kenmo_newhigh｜🚀確変(13)｜⚪妥当｜FAIL_INSEN｜4,270円｜💰43.3万円｜—
- 7480 Suzuden Corporation｜granville_oshime+kenmo_newhigh｜🚀確変(13)｜⚪妥当｜FAIL_INSEN｜3,850円｜💰38.5万円｜—
- 3374 Naigai Tec Corporation｜kenmo_newhigh+ai_momentum｜🚀確変(12)｜⚪妥当｜FAIL_UWAHIGE｜5,370円｜💰53.0万円｜—
- 7567 Sakae Electronics Corp.｜kenmo_newhigh｜🚀確変(12)｜⚪妥当｜FAIL_INSEN｜648円｜💰6.8万円｜—
- 269A SAPEET｜kenmo_newhigh｜🚀確変(11)｜⚪妥当｜FAIL_INSEN｜2,901円｜💰30.3万円｜—
- 6337 Tesec Corporation｜kenmo_newhigh｜🚀確変(11)｜⚪妥当｜FAIL_INSEN｜3,845円｜💰39.4万円｜—
- 6317 Kitagawa Corporation｜kenmo_newhigh｜🔥絶好調(8)｜🟢値頃｜PASS｜2,650円｜💰26.5万円｜⛔提案なし(指名鮮度切れ 18営業日)｜📑TOPIX低減対象（次 10/30 第1回/8）
  > 【業態】コンクリートプラント、鋳造部品、工作機械・器具、産業機械等を展開。海外にも拠点。
  > 【いま】終値2,650円・直近5日+6.55%（材料未確認）
  > 【調子】🔥絶好調（8/13）
  > 【水準】🟢値頃（5.0/7）— PER7.371倍・PEG0.0913・52週98.7% ／ 💰単元26.5万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 18営業日)）
- 9251 G-AB&Company Co.,Ltd.｜kenmo_newhigh｜🔥絶好調(8)｜⚪妥当｜FAIL_INSEN｜1,536円｜💰15.5万円｜—
- 2820 Yamami Co.｜kenmo_newhigh｜✅順調(4)｜🟡やや割高｜FAIL_UWAHIGE｜7,000円｜💰68.0万円｜—
- 4331 Take and Give. Needs Co., Ltd.｜kenmo_newhigh｜✅順調(3)｜🔴過熱｜FAIL_INSEN｜835円｜💰8.3万円｜—
- 8370 Kiyo Bank, Ltd.｜kenmo_newhigh+granville_oshime｜取得不可｜🟢値頃｜FAIL_INSEN｜1,646円｜💰17.1万円｜—
- 7161 Jimoto Holdings, Inc.｜kenmo_newhigh｜業績データ取得不可｜⚪妥当｜FAIL_INSEN｜620円｜💰6.6万円｜—
- 2340 Gokurakuyu Holdings Co., Ltd.｜kenmo_newhigh｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜510円｜💰5.1万円｜—
- 7175 今村証券｜kenmo_newhigh｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜1,916円｜💰19.6万円｜—
- 8871 GOLDCREST Co., Ltd.｜choruko_reversal｜🔥絶好調(10)｜💎割安｜FAIL_INSEN｜2,927円｜💰29.5万円｜—
- 3391 TSURUHA Holdings, Inc.｜choruko_reversal｜🔥絶好調(10)｜🟢値頃｜FAIL_INSEN｜2,104円｜💰21.2万円｜—
- 3186 ネクステージ｜choruko_reversal｜🔥絶好調(9)｜💎割安｜FAIL_INSEN｜2,644円｜💰26.8万円｜—
- 6474 Nachi-Fujikoshi Corp.｜choruko_reversal｜🔥絶好調(9)｜⚪妥当｜FAIL_UWAHIGE｜5,850円｜💰58.5万円｜—
- 3222 United Super Markets Holdings, Inc.｜choruko_reversal｜🔥絶好調(9)｜🔴過熱｜FAIL_INSEN｜731円｜💰7.5万円｜—
- 1803 Shimizu Corporation｜choruko_reversal｜🔥絶好調(8)｜💎割安｜FAIL_INSEN｜2,034円｜💰20.4万円｜—
- 8086 NIPRO Corporation｜choruko_reversal｜🔥絶好調(8)｜💎割安｜FAIL_UWAHIGE｜1,354円｜💰13.5万円｜—
- 4023 クレハ｜choruko_reversal｜🔥絶好調(8)｜🟢値頃｜FAIL_INSEN｜3,860円｜💰38.8万円｜—
- 7906 Yonex Co., Ltd.｜choruko_reversal｜⚡好調(7)｜🟢値頃｜FAIL_INSEN｜2,350円｜💰24.1万円｜—
- 2874 YOKOREI CO. LTD.｜granville_rebound+choruko_reversal｜⚠減速(7)｜⚪妥当｜FAIL_INSEN｜1,766円｜💰18.0万円｜—
- 7550 Zensho Holdings Co., Ltd.｜choruko_reversal｜⚡好調(7)｜🔴過熱｜FAIL_INSEN｜11,700円｜💰117.8万円｜—
- 8282 K'S HOLDINGS CORPORATION｜choruko_reversal｜⚡好調(6)｜🟢値頃｜PASS｜1,676円｜💰16.8万円｜reversal 1676 想定損失幅2.4%。｜⚠日程不明
  > 【業態】北関東地盤の家電量販大手。デンコードーなど買収で全国。現金値引きに特徴。
  > 【いま】終値1,676円・直近5日-2.56%（材料未確認）
  > 【調子】⚡好調（6/13）
  > 【水準】🟢値頃（5.0/7）— PER12.952倍・PEG1.3559・52週31.0% ／ 💰単元16.8万円
  > 【戦略】当日終値1676円の指値で反転を取りにいく。SL1635.5円（直近5日安値）
- 8088 IWATANI Corporation｜choruko_reversal｜⚡好調(6)｜⚪妥当｜FAIL_INSEN｜1,958円｜💰19.7万円｜—
- 9412 SKY Perfect JSAT Corporation｜choruko_reversal｜⚡好調(6)｜⚪妥当｜PASS｜1,882円｜💰18.8万円｜reversal 1882 想定損失幅3.0%。｜📋カルテ窓 11/04(残14営業日)
  > 【業態】CS放送「スカパー!」と衛星運営が両輪。光回線配信も。衛星打上に注力。
  > 【いま】終値1,882円・直近5日-4.56%（材料未確認）
  > 【調子】⚡好調（6/13）
  > 【水準】⚪妥当（3.0/7）— PER19.769倍・PEG1.9559・52週15.2% ／ 💰単元18.8万円
  > 【戦略】当日終値1882円の指値で反転を取りにいく。SL1826円（直近5日安値）
- 8125 Wakita & Co., Ltd.｜choruko_reversal｜⚡好調(6)｜🔴過熱｜FAIL_INSEN｜1,815円｜💰18.2万円｜—
- 9861 吉野家ホールディングス｜choruko_reversal｜⚡好調(6)｜🔴過熱｜FAIL_INSEN｜3,960円｜💰40.3万円｜—
- 4666 Park24 Co., Ltd.｜choruko_reversal｜⚡好調(5)｜💎割安｜FAIL_UWAHIGE｜1,740円｜💰17.4万円｜—
- 8278 Fuji Co., Ltd.｜choruko_reversal｜⚡好調(5)｜🟢値頃｜FAIL_INSEN｜1,895円｜💰19.2万円｜—
- 7458 Daiichikosho Co., Ltd.｜choruko_reversal｜⚡好調(5)｜⚪妥当｜FAIL_INSEN｜1,706円｜💰17.4万円｜—
- 7564 Workman Co., Ltd.｜choruko_reversal｜⚡好調(5)｜⚪妥当｜FAIL_INSEN｜5,210円｜💰52.4万円｜—
- 2702 日本マクドナルドホールディングス｜choruko_reversal｜⚠減速(5)｜🔴過熱｜FAIL_INSEN｜7,640円｜💰77.1万円｜—
- 2782 Seria Co., Ltd.｜choruko_reversal｜⚡好調(5)｜🔴過熱｜FAIL_INSEN｜3,955円｜💰41.0万円｜—
- 2809 Kewpie Corporation｜choruko_reversal｜⚡好調(5)｜🔴過熱｜FAIL_INSEN｜4,274円｜💰43.2万円｜—
- 7731 Nikon Corp.｜choruko_reversal｜✅順調(4)｜🟢値頃｜FAIL_INSEN｜1,844円｜💰18.3万円｜—
- 8923 Tosei Corporation｜choruko_reversal｜✅順調(4)｜🟢値頃｜FAIL_INSEN｜1,691円｜💰17.0万円｜—
- 9627 アインホールディングス｜choruko_reversal｜✅順調(4)｜⚪妥当｜FAIL_UWAHIGE｜5,412円｜💰54.4万円｜—
- 5602 Kurimoto,Ltd.｜choruko_reversal｜✅順調(4)｜⚪妥当｜FAIL_UWAHIGE｜1,617円｜💰16.1万円｜—
- 7762 Citizen Watch Co, Ltd.｜choruko_reversal｜✅順調(4)｜⚪妥当｜FAIL_INSEN｜2,320円｜💰23.8万円｜—
- 9031 Nishi-Nippon Railroad Co., Ltd.｜granville_tenkan+choruko_reversal｜🔻悪化(4)｜🟡やや割高｜FAIL_INSEN｜2,790円｜💰28.2万円｜—
- 4680 ROUND ONE Corporation｜choruko_reversal｜✅順調(4)｜🔴過熱｜FAIL_INSEN｜1,318円｜💰13.2万円｜—
- 6465 HOSHIZAKI Corp.｜choruko_reversal｜✅順調(4)｜🔴過熱｜FAIL_INSEN｜5,310円｜💰53.3万円｜—
- 8934 Sun Frontier Fudousan Co., Ltd.｜choruko_reversal｜✅順調(3)｜💎割安｜FAIL_INSEN｜2,122円｜💰21.6万円｜—
- 1861 Kumagai Gumi Co., Ltd.｜choruko_reversal｜✅順調(3)｜💎割安｜FAIL_INSEN｜1,203円｜💰12.1万円｜—
- 3148 Create SD Holdings Co., Ltd.｜choruko_reversal｜✅順調(3)｜⚪妥当｜FAIL_INSEN｜3,130円｜💰31.4万円｜—
- 1332 Nissui Corporation｜choruko_reversal｜✅順調(3)｜⚪妥当｜FAIL_INSEN｜1,080円｜💰10.9万円｜—
- 6269 Modec, Inc.｜choruko_reversal｜✅順調(3)｜⚪妥当｜FAIL_INSEN｜8,486円｜💰84.0万円｜—
- 7003 Mitsui ES Holdings Co., Ltd.｜choruko_reversal｜✅順調(3)｜⚪妥当｜PASS_DOJI｜3,929円｜💰39.3万円｜reversal 3929 想定損失幅1.6%。｜⚠日程不明
  > 【業態】船舶ディーゼル首位。船舶用推進、港湾物流事業が両輪。水素・SAF燃料注力。
  > 【いま】終値3,929円・直近5日-5.33%（材料未確認）
  > 【調子】✅順調（3/13） — 質注意
  > 【水準】⚪妥当（3.0/7）— PER12.79倍・PEG—・52週3.8% ／ 💰単元39.3万円
  > 【戦略】当日終値3929円の指値で反転を取りにいく。SL3868円（直近5日安値）
- 8584 Jaccs Co., Ltd.｜choruko_reversal｜🔻悪化(3)｜⚪妥当｜FAIL_INSEN｜3,435円｜💰34.7万円｜—
- 9882 Yellow Hat Ltd.｜choruko_reversal｜✅順調(3)｜⚪妥当｜FAIL_INSEN｜1,606円｜💰16.2万円｜—
- 1860 Toda Corporation｜choruko_reversal｜✅順調(3)｜🟡やや割高｜FAIL_INSEN｜1,360円｜💰13.6万円｜—
- 8066 Mitani Corporation｜granville_rebound+choruko_reversal｜⚠減速(3)｜🟡やや割高｜FAIL_INSEN｜3,125円｜💰31.2万円｜—
- 2659 SAN-A CO., LTD.｜choruko_reversal｜✅順調(3)｜🔴過熱｜FAIL_INSEN｜3,020円｜💰30.9万円｜—
- 2805 S&B Foods Inc.｜granville_rebound+choruko_reversal｜✅順調(3)｜🔴過熱｜FAIL_INSEN｜6,230円｜💰64.9万円｜—
- 5021 Cosmo Energy Holdings Co., Ltd.｜choruko_reversal｜🔻悪化(3)｜🔴過熱｜FAIL_INSEN｜4,142円｜💰40.9万円｜—
- 7984 Kokuyo Co., Ltd.｜choruko_reversal｜✅順調(3)｜🔴過熱｜FAIL_UWAHIGE｜871円｜💰8.7万円｜—
- 8233 Takashimaya Company, Limited｜choruko_reversal｜✅順調(3)｜🔴過熱｜FAIL_INSEN｜2,110円｜💰21.5万円｜—
- 3289 Tokyu Fudosan Holdings Corp.｜choruko_reversal｜➖横ばい(2)｜💎割安｜FAIL_INSEN｜1,178円｜💰11.9万円｜—
- 4028 ISHIHARA SANGYO KAISHA, LTD.｜choruko_reversal｜⚠減速(2)｜⚪妥当｜FAIL_INSEN｜2,806円｜💰28.3万円｜—
- 8818 Keihanshin Building Co., Ltd.｜choruko_reversal｜➖横ばい(2)｜⚪妥当｜FAIL_INSEN｜925円｜💰9.4万円｜—
- 1333 Umios Corporation｜choruko_reversal｜➖横ばい(2)｜⚪妥当｜FAIL_INSEN｜1,184円｜💰12.0万円｜—
- 1719 HAZAMA ANDO Corporation｜choruko_reversal｜➖横ばい(2)｜⚪妥当｜FAIL_INSEN｜1,719円｜💰17.2万円｜—
- 1833 Okumura Corporation｜choruko_reversal｜⚠減速(2)｜⚪妥当｜FAIL_INSEN｜5,220円｜💰52.7万円｜—
- 1871 PS Construction Co., Ltd.｜choruko_reversal｜⚠減速(2)｜⚪妥当｜PASS｜2,101円｜💰21.0万円｜⛔提案なし(指名鮮度切れ 15営業日)｜📋カルテ窓 11/11(残19営業日) ⚠業績基調が下向き（⚠減速） 📑TOPIX低減対象（次 10/30 第1回/8）
  > 【業態】大成建設子会社。PCコンクリート橋梁で首位級。土木・建築両輪目指す。
  > 【いま】終値2,101円・直近5日+2.49%（材料未確認）
  > 【調子】⚠減速（2/13） — 質注意・減収
  > 【水準】⚪妥当（3.0/7）— PER12.611倍・PEG—・52週20.7% ／ 💰単元21.0万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 15営業日)）
- 2875 Toyo Suisan Kaisha, Ltd.｜choruko_reversal｜➖横ばい(2)｜⚪妥当｜FAIL_INSEN｜10,250円｜💰103.5万円｜—
- 9503 Kansai Electric Power Company, Incorporated｜choruko_reversal+granville_rebound｜🔻悪化(2)｜⚪妥当｜FAIL_INSEN｜2,744円｜💰27.2万円｜—
- 3099 Isetan Mitsukoshi Holdings Ltd.｜choruko_reversal｜➖横ばい(2)｜🟡やや割高｜FAIL_INSEN｜1,727円｜💰17.4万円｜—
- 1893 Penta-Ocean Construction Co., Ltd.｜choruko_reversal｜⚠減速(1)｜⚪妥当｜FAIL_INSEN｜1,380円｜💰13.9万円｜—
- 6753 Sharp Corporation｜choruko_reversal｜🔻悪化(1)｜⚪妥当｜FAIL_INSEN｜580円｜💰5.9万円｜—
- 8276 HEIWADO CO., LTD.｜choruko_reversal｜⚠減速(1)｜⚪妥当｜FAIL_INSEN｜2,473円｜💰25.1万円｜—
- 9974 BELC Co., Ltd.｜choruko_reversal｜⚠減速(1)｜⚪妥当｜FAIL_INSEN｜6,020円｜💰62.5万円｜—
- 5482 Aichi Steel Corporation｜choruko_reversal｜⚠減速(1)｜🟡やや割高｜FAIL_INSEN｜2,863円｜💰29.0万円｜—
- 2815 ARIAKE JAPAN Co., Ltd.｜choruko_reversal｜⚠減速(1)｜🟡やや割高｜FAIL_INSEN｜5,180円｜💰52.1万円｜—
- 4928 Noevir Holdings Co., Ltd.｜choruko_reversal｜⚠減速(1)｜🔴過熱｜PASS｜4,645円｜💰46.5万円｜reversal 4645 想定損失幅5.4%。｜📋カルテ窓 11/10(残18営業日) ⚠業績基調が下向き（⚠減速）
  > 【業態】化粧品中堅。高級基礎化粧品が主力。医薬も。傘下に飴、ドリンク剤の常盤薬。
  > 【いま】終値4,645円・直近5日+5.45%（材料未確認）
  > 【調子】⚠減速（1/13）
  > 【水準】🔴過熱（1.0/7）— PER19.346倍・PEG87.6081・52週51.7% ／ 💰単元46.5万円
  > 【戦略】当日終値4645円の指値で反転を取りにいく。SL4395円（直近5日安値）
- 9436 Okinawa Cellular Telephone Company｜choruko_reversal｜⚠減速(1)｜🔴過熱｜FAIL_INSEN｜3,490円｜💰36.1万円｜—
- 1662 Japan Petroleum Exploration Co., Ltd.｜choruko_reversal｜🔻悪化(0)｜⚪妥当｜FAIL_INSEN｜1,722円｜💰17.2万円｜—
- 6804 Hosiden Corp.｜choruko_reversal｜🔻悪化(0)｜⚪妥当｜FAIL_INSEN｜2,406円｜💰24.2万円｜—
- 6183 BELLSYSTEM24 Holdings, Inc.｜choruko_reversal｜⚠減速(0)｜⚪妥当｜FAIL_INSEN｜1,299円｜💰13.0万円｜—｜⚡材料後出し
- 8585 Orient Corporation｜choruko_reversal｜⚠減速(0)｜⚪妥当｜FAIL_INSEN｜767円｜💰7.8万円｜—
- 8194 Life Corporation｜choruko_reversal｜⚠減速(0)｜🟡やや割高｜FAIL_INSEN｜2,301円｜💰24.1万円｜—
- 9699 NISHIO HOLDINGS CO. LTD.｜choruko_reversal｜⚠減速(0)｜🟡やや割高｜PASS｜4,215円｜💰42.1万円｜reversal 4215 想定損失幅6.6%。｜⚠日程不明 ⚠業績基調が下向き（⚠減速）
  > 【業態】総合レンタルの草分け。関西地盤。建機レンタルで首位級。アジア、豪に積極展開。
  > 【いま】終値4,215円・直近5日-1.40%（材料未確認）
  > 【調子】⚠減速（0/13） — 質注意
  > 【水準】🟡やや割高（2.0/7）— PER9.442倍・PEG10.2756・52週45.9% ／ 💰単元42.1万円
  > 【戦略】当日終値4215円の指値で反転を取りにいく。SL3935円（直近5日安値）
- 5110 Sumitomo Rubber Industries, Ltd.｜choruko_reversal｜業績データ取得不可(経常益予想非開示)｜💎割安｜FAIL_UWAHIGE｜2,048円｜💰20.2万円｜—
- 8987 Japan Excellent, Inc.｜choruko_reversal｜判定保留(変則決算)｜🟢値頃｜FAIL_INSEN｜123,900円｜💰12.5万円｜—
- 7201 Nissan Motor Co., Ltd.｜choruko_reversal｜業績データ取得不可(経常益予想非開示)｜🟢値頃｜FAIL_INSEN｜283円｜💰2.8万円｜—
- 3471 Mitsui Fudosan Logistics Park, Inc.｜choruko_reversal｜判定保留｜⚪妥当｜FAIL_UWAHIGE｜97,800円｜💰9.8万円｜—
- 8174 NIPPON GAS Co., Ltd.｜choruko_reversal｜業績データ取得不可｜⚪妥当｜FAIL_INSEN｜891円｜💰9.1万円｜—
- 3234 Mori Hills Reit Investment Corporation｜choruko_reversal｜判定保留｜🟡やや割高｜FAIL_INSEN｜118,400円｜💰11.9万円｜—
- 3249 Industrial & Infrastructure Fund Investment Corporation｜choruko_reversal｜判定保留｜🟡やや割高｜FAIL_UWAHIGE｜127,700円｜💰12.7万円｜—
- 3279 Activia Properties, Inc.｜choruko_reversal｜判定保留｜🟡やや割高｜FAIL_INSEN｜123,500円｜💰12.3万円｜—
- 3283 Nippon Prologis REIT, Inc.｜choruko_reversal｜判定保留｜🟡やや割高｜FAIL_INSEN｜78,500円｜💰7.9万円｜—
- 3292 AEON REIT Investment Corp.｜choruko_reversal｜判定保留｜🟡やや割高｜FAIL_INSEN｜104,900円｜💰10.6万円｜—
- 3296 NIPPON REIT Investment Corp｜choruko_reversal｜判定保留(変則決算)｜🟡やや割高｜FAIL_INSEN｜75,100円｜💰7.5万円｜—
- 3309 Sekisui House Reit. Inc.｜choruko_reversal｜判定保留｜🟡やや割高｜FAIL_INSEN｜66,800円｜💰6.7万円｜—
- 3462 Nomura Real Estate Master Fund, Inc.｜choruko_reversal｜判定保留｜🟡やや割高｜FAIL_INSEN｜133,900円｜💰13.5万円｜—
- 8952 Japan Real Estate Investment Corp.｜choruko_reversal｜判定保留｜🟡やや割高｜FAIL_INSEN｜105,600円｜💰10.6万円｜—
- 8953 Japan Metropolitan Fund Investment Corporation｜choruko_reversal｜判定保留｜🟡やや割高｜FAIL_INSEN｜103,300円｜💰10.3万円｜—
- 8954 ORIX JREIT Inc.｜choruko_reversal｜判定保留｜🟡やや割高｜FAIL_INSEN｜89,300円｜💰8.9万円｜—
- 8955 Japan Prime Realty Investment Corporation｜choruko_reversal｜判定保留｜🟡やや割高｜FAIL_INSEN｜88,500円｜💰8.9万円｜—
- 8961 MORI TRUST REIT.Inc｜choruko_reversal｜判定保留｜🔴過熱｜FAIL_INSEN｜66,700円｜💰6.7万円｜—
- 8984 Daiwa House REIT Investment Corporation｜choruko_reversal｜取得不可｜🟡やや割高｜FAIL_UWAHIGE｜108,000円｜💰10.8万円｜—
- 8986 Daiwa Securities Living Investment Corporation｜choruko_reversal｜判定保留｜🟡やや割高｜FAIL_INSEN｜84,000円｜💰8.4万円｜—
- 7624 NaITO｜stf_kakuhen｜🔥絶好調(10)｜🟢値頃｜PASS｜180円｜💰1.8万円｜⛔提案なし(手法ブランチ不明)｜⚠日程不明
  > 【業態】岡谷鋼機系。機械工具卸老舗。自動車向け切削工具が柱。計測器具も展開。
  > 【いま】終値180円・直近5日+1.12%（材料未確認）
  > 【調子】🔥絶好調（10/13）
  > 【水準】🟢値頃（5.0/7）— PER10.976倍・PEG0.0587・52週64.9% ／ 💰単元1.8万円
  > 【戦略】発注対象外（⛔提案なし(手法ブランチ不明)）
- 6668 ＡＤプラズマ｜granville_oshime+stf_kakuhen｜🔥絶好調(10)｜⚪妥当｜FAIL_INSEN｜5,600円｜💰56.3万円｜—
- 7713 シグマ光機｜stf_kakuhen｜🔥絶好調(10)｜⚪妥当｜PASS｜3,905円｜💰39.0万円｜⛔提案なし(手法ブランチ不明)｜⚠日程不明
  > 【業態】レーザー関連部品やユニット・システムの総合力に強み。半導体、液晶製造装置向け。
  > 【いま】終値3,905円・直近5日+44.63%（材料未確認）
  > 【調子】🔥絶好調（10/13）
  > 【水準】⚪妥当（3.0/7）— PER18.684倍・PEG0.295・52週99.4% ／ 💰単元39.0万円
  > 【戦略】発注対象外（⛔提案なし(手法ブランチ不明)）
- 3498 霞ヶ関Ｃ｜granville_oshime+granville_tenkan+stf_kakuhen｜🔥絶好調(9)｜💎割安｜FAIL_INSEN｜7,580円｜💰75.5万円｜—
- 4443 Ｓａｎｓａｎ｜changepoint+changepoint🔔+stf_kakuhen｜🔥絶好調(8)｜⚪妥当｜FAIL_INSEN｜1,924円｜💰20.2万円｜—
- 6814 古野電｜stf_kakuhen｜⚡好調(7)｜🟢値頃｜FAIL_UWAHIGE｜8,560円｜💰80.6万円｜—
- 5932 三協立山｜stf_kakuhen｜⚡好調(7)｜⚪妥当｜FAIL_INSEN｜749円｜💰7.5万円｜—
- 9308 乾汽船｜changepoint+変化点🔔+granville_oshime+changepoint🔔｜🔥絶好調(10)｜⚪妥当｜FAIL_INSEN｜2,284円｜💰23.5万円｜—
- 4180 ＡＰＰＩＥＲ　ＧＲＯＵＰ｜変化点🔔+changepoint🔔+changepoint｜🔥絶好調(8)｜⚪妥当｜FAIL_INSEN｜1,372円｜💰14.1万円｜—
- 4431 スマレジ｜changepoint+変化点🔔🔔+changepoint🔔｜🔥絶好調(8)｜🟡やや割高｜FAIL_INSEN｜3,925円｜💰39.0万円｜—
- 4493 Cyber Security Cloud, Inc.｜granville_tenkan+changepoint+変化点🔔🔔+changepoint🔔｜✅順調(3)｜🔴過熱｜FAIL_INSEN｜3,665円｜💰41.8万円｜—

## グランビル銘柄
- 9553 MicroAd, Inc.｜granville_tenkan｜🔥絶好調(10)｜🟢値頃｜FAIL_INSEN｜606円｜💰6.3万円｜—
- 6905 Cosel Co., Ltd.｜granville_tenkan｜🔥絶好調(10)｜⚪妥当｜FAIL_UWAHIGE｜1,468円｜💰14.2万円｜—
- 2986 LA Holdings Co.,Ltd｜granville_tenkan｜🔥絶好調(9)｜💎割安｜FAIL_INSEN｜2,766円｜💰28.0万円｜—
- 6562 Geniee, Inc.｜granville_tenkan｜🔥絶好調(8)｜💎割安｜FAIL_INSEN｜1,019円｜💰10.3万円｜—
- 3608 TSI Holdings Co.,Ltd.｜granville_tenkan｜🔥絶好調(8)｜💎割安｜FAIL_INSEN｜1,208円｜💰12.2万円｜—｜⚡材料後出し
- 1945 Tokyo Energy & Systems Inc.｜granville_tenkan｜🔥絶好調(8)｜🟢値頃｜FAIL_INSEN｜2,066円｜💰20.7万円｜—
- 9006 京浜急行電鉄｜granville_tenkan｜🔥絶好調(8)｜🟢値頃｜FAIL_INSEN｜1,526円｜💰15.4万円｜—
- 6473 JTEKT Corporation｜granville_tenkan｜⚠減速(8)｜⚪妥当｜FAIL_INSEN｜2,144円｜💰21.5万円｜—
- 3496 AZOOM CO.,LTD｜granville_tenkan｜⚡好調(7)｜🟢値頃｜FAIL_UWAHIGE｜4,725円｜💰46.8万円｜—
- 6255 NPC Incorporated｜granville_tenkan｜⚡好調(7)｜🟢値頃｜FAIL_UWAHIGE｜703円｜💰6.9万円｜—
- 6395 TADANO Ltd.｜granville_tenkan+granville_oshime｜⚡好調(7)｜🟢値頃｜FAIL_UWAHIGE｜1,337円｜💰13.4万円｜—
- 8793 ＮＥＣキャピタルソリューション｜granville_tenkan｜⚡好調(7)｜🟢値頃｜FAIL_INSEN｜4,065円｜💰40.9万円｜—
- 4544 H.U.Group Holdings, Inc.｜granville_tenkan｜⚡好調(7)｜⚪妥当｜FAIL_INSEN｜3,633円｜💰36.5万円｜—
- 8095 Astena Holdings Co.,Ltd.｜granville_tenkan｜⚡好調(7)｜⚪妥当｜FAIL_INSEN｜525円｜💰5.4万円｜—
- 9064 ヤマトホールディングス｜granville_tenkan｜⚡好調(7)｜⚪妥当｜FAIL_UWAHIGE｜2,085円｜💰20.7万円｜—
- 4507 Shionogi & Co., Ltd.｜granville_tenkan｜⚡好調(7)｜⚪妥当｜FAIL_INSEN｜2,790円｜💰28.1万円｜—
- 3741 Systems Engineering Consultants Co., Ltd.｜granville_tenkan｜⚡好調(7)｜🟡やや割高｜FAIL_INSEN｜3,085円｜💰31.1万円｜—
- 5838 Rakuten Bank, Ltd.｜granville_tenkan｜⚡好調(6)｜💎割安｜FAIL_INSEN｜6,027円｜💰62.0万円｜—
- 7270 Subaru Corporation｜granville_tenkan｜⚡好調(6)｜💎割安｜FAIL_INSEN｜2,588円｜💰25.9万円｜—
- 4763 クリーク・アンド・リバー社｜granville_tenkan｜⚡好調(6)｜🟢値頃｜FAIL_INSEN｜1,446円｜💰14.6万円｜—
- 7199 Premium Group Co., Ltd.｜granville_tenkan｜⚡好調(6)｜⚪妥当｜FAIL_INSEN｜2,161円｜💰21.9万円｜—
- 6432 Takeuchi Mfg.Co., Ltd.｜granville_tenkan｜⚡好調(6)｜⚪妥当｜FAIL_UWAHIGE｜7,850円｜💰76.5万円｜—
- 3064 MonotaRO Co., Ltd.｜granville_tenkan｜⚡好調(6)｜🟡やや割高｜FAIL_UWAHIGE｜2,310円｜💰22.5万円｜—
- 6196 Strike Group Co. Ltd.｜granville_tenkan｜⚡好調(5)｜💎割安｜FAIL_INSEN｜1,394円｜💰14.2万円｜—
- 1968 Taihei Dengyo Kaisha, Ltd.｜granville_tenkan｜⚡好調(5)｜🟢値頃｜FAIL_INSEN｜2,440円｜💰24.5万円｜—
- 3562 No.1 Co., Ltd.｜granville_tenkan｜⚡好調(5)｜🟢値頃｜FAIL_INSEN｜1,700円｜💰17.6万円｜—｜⚡材料後出し
- 9048 名古屋鉄道｜granville_tenkan｜⚡好調(5)｜🟢値頃｜FAIL_INSEN｜1,844円｜💰18.6万円｜—
- 2331 ALSOK CO., LTD.｜granville_tenkan｜⚡好調(5)｜⚪妥当｜FAIL_INSEN｜1,174円｜💰11.8万円｜—
- 3661 m-up holdings, Inc.｜granville_tenkan｜⚡好調(5)｜⚪妥当｜FAIL_UWAHIGE｜866円｜💰8.5万円｜—
- 8020 Kanematsu Corporation｜granville_tenkan｜⚡好調(5)｜🟡やや割高｜FAIL_UWAHIGE｜2,354円｜💰23.1万円｜—
- 9828 Genki Global Dining Concepts Corp｜granville_tenkan｜⚡好調(5)｜🟡やや割高｜FAIL_INSEN｜3,390円｜💰34.6万円｜—
- 3479 ティーケーピー｜granville_tenkan｜⚡好調(5)｜🔴過熱｜FAIL_INSEN｜1,851円｜💰18.6万円｜—
- 6454 Max Co., Ltd.｜granville_tenkan｜⚡好調(5)｜🔴過熱｜FAIL_INSEN｜1,918円｜💰19.3万円｜—
- 2288 Marudai Food Co., Ltd.｜granville_tenkan｜✅順調(4)｜🟢値頃｜FAIL_INSEN｜2,139円｜💰21.8万円｜—
- 5036 Japan Business Systems, Inc.｜granville_tenkan｜✅順調(4)｜🟢値頃｜PASS｜1,755円｜💰17.6万円｜momentum 1759 想定損失幅6.1%。 移行措置銘柄: 10/30 の引けにパッシブ売り（8回に分けて低減）。実施日前後の寄り・引けの需給に注意｜📋カルテ窓 11/12(残20営業日) 📑TOPIX低減対象（次 10/30 第1回/8）
  > 【業態】マイクロソフト製品を中心としたITサービスの提供。クラウドサービスに強み。
  > 【いま】終値1,755円・直近5日+11.64%（材料未確認）
  > 【調子】✅順調（4/13）
  > 【水準】🟢値頃（5.0/7）— PER11.308倍・PEG0.5121・52週70.2% ／ 💰単元17.6万円
  > 【戦略】当日高値超えの逆指値1759円で順張り参戦を検討。上限1776.6円・SL1652.5円目安
- 8014 Chori Co., Ltd.｜granville_tenkan｜✅順調(4)｜⚪妥当｜PASS｜4,275円｜💰42.8万円｜momentum 4290 想定損失幅6.1%。 移行措置銘柄: 10/30 の引けにパッシブ売り（8回に分けて低減）。実施日前後の寄り・引けの需給に注意｜📋カルテ窓 10/30(残12営業日) 📑TOPIX低減対象（次 10/30 第1回/8）
  > 【業態】繊維商社の老舗。東レ子会社。化学品や機械事業など中国ビジネスを拡大。
  > 【いま】終値4,275円・直近5日+2.15%（材料未確認）
  > 【調子】✅順調（4/13）
  > 【水準】⚪妥当（3.0/7）— PER10.035倍・PEG1.7649・52週64.9% ／ 💰単元42.8万円
  > 【戦略】当日高値超えの逆指値4290円で順張り参戦を検討。上限4332.9円・SL4027.9円目安
- 9045 Keihan Holdings Co.,Ltd.｜granville_tenkan｜⚠減速(4)｜⚪妥当｜FAIL_UWAHIGE｜3,201円｜💰32.0万円｜—
- 3549 KUSURI NO AOKI HOLDINGS CO.,LTD.｜granville_tenkan｜✅順調(4)｜🟡やや割高｜PASS｜4,205円｜💰42.0万円｜momentum 4236 想定損失幅6.1%。｜⚠日程不明
  > 【業態】ドラッグストア中堅。北陸で首位。調剤併設店主軸に食品・生活必需品を拡大。
  > 【いま】終値4,205円・直近5日+0.07%（材料未確認）
  > 【調子】✅順調（4/13）
  > 【水準】🟡やや割高（2.0/7）— PER21.015倍・PEG1.8927・52週58.3% ／ 💰単元42.0万円
  > 【戦略】当日高値超えの逆指値4236円で順張り参戦を検討。上限4278.4円・SL3977.1円目安
- 6988 日東電工｜granville_tenkan｜✅順調(4)｜🟡やや割高｜FAIL_INSEN｜3,633円｜💰36.5万円｜—
- 6371 Tsubakimoto Chain Co.｜granville_tenkan｜✅順調(4)｜🔴過熱｜FAIL_INSEN｜2,643円｜💰26.7万円｜—
- 8060 キヤノンマーケティングジャパン｜granville_tenkan｜✅順調(4)｜🔴過熱｜FAIL_UWAHIGE｜4,004円｜💰39.7万円｜—
- 8056 BIPROGY Inc.｜granville_tenkan｜✅順調(3)｜⚪妥当｜FAIL_UWAHIGE｜4,830円｜💰48.3万円｜—
- 8850 スターツコーポレーション｜granville_tenkan｜✅順調(3)｜⚪妥当｜FAIL_INSEN｜4,500円｜💰45.6万円｜—
- 3433 TOCALO Co., Ltd.｜granville_tenkan｜✅順調(3)｜⚪妥当｜FAIL_INSEN｜3,090円｜💰29.9万円｜—
- 8927 Meiho Enterprise Co., Ltd.｜granville_tenkan｜✅順調(3)｜⚪妥当｜FAIL_INSEN｜492円｜💰4.9万円｜—
- 186A Astroscale Holdings Inc.｜granville_tenkan｜✅順調(3)｜🔴過熱｜FAIL_INSEN｜1,131円｜💰11.5万円｜—
- 4183 Mitsui Chemicals, Inc.｜granville_tenkan｜✅順調(3)｜🟡やや割高｜PASS｜2,134円｜💰21.3万円｜momentum 2135 想定損失幅6.0%。｜📋カルテ窓 11/11(残19営業日)
  > 【業態】三井系総合化学。フェノール大手。石化からモビリティ、ヘルスケアなど機能性材料注力。
  > 【いま】終値2,134円・直近5日-1.77%（材料未確認）
  > 【調子】✅順調（3/13）
  > 【水準】🟡やや割高（2.0/7）— PER17.141倍・PEG2.181・52週53.6% ／ 💰単元21.3万円
  > 【戦略】当日高値超えの逆指値2135円で順張り参戦を検討。上限2156.3円・SL2006円目安
- 4272 Nippon Kayaku Co., Ltd.｜granville_tenkan+granville_oshime｜✅順調(3)｜🟡やや割高｜FAIL_UWAHIGE｜2,178円｜💰21.6万円｜—
- 4956 Konishi Co., Ltd.｜granville_tenkan｜✅順調(3)｜🟡やや割高｜FAIL_UWAHIGE｜1,512円｜💰15.0万円｜—
- 5461 Chubu Steel Plate Co., Ltd.｜granville_tenkan｜🔻悪化(3)｜🟡やや割高｜FAIL_UWAHIGE｜2,130円｜💰21.3万円｜—
- 7181 JAPAN POST INSURANCE Co., Ltd.｜granville_tenkan｜⚠減速(3)｜🔴過熱｜FAIL_INSEN｜1,692円｜💰17.1万円｜—
- 7513 Kojima Co., Ltd.｜granville_tenkan｜✅順調(3)｜🔴過熱｜FAIL_UWAHIGE｜1,445円｜💰14.5万円｜—
- 2002 日清製粉グループ本社｜granville_tenkan｜➖横ばい(2)｜🟡やや割高｜FAIL_INSEN｜1,994円｜💰20.1万円｜—
- 4274 HOSOYA PYRO-ENGINEERING CO LTD｜granville_tenkan｜➖横ばい(2)｜🟡やや割高｜FAIL_UWAHIGE｜1,085円｜💰11.0万円｜—
- 6208 Ishikawa Seisakusho,Ltd.｜granville_tenkan｜🔻悪化(2)｜🟡やや割高｜FAIL_INSEN｜1,690円｜💰17.2万円｜—
- 7751 キヤノン｜granville_tenkan｜➖横ばい(2)｜🟡やや割高｜FAIL_UWAHIGE｜4,745円｜💰47.2万円｜—
- 1377 Sakata Seed Corporation｜granville_tenkan｜➖横ばい(2)｜🔴過熱｜FAIL_INSEN｜4,180円｜💰42.9万円｜—
- 2413 エムスリー｜granville_tenkan｜➖横ばい(2)｜🔴過熱｜PASS｜1,914円｜💰19.1万円｜momentum 1918 想定損失幅6.0%。｜📋カルテ窓 11/04(残14営業日)
  > 【業態】ソニー系。製薬会社のマーケ支援。医師向けサイトで情報提供。遠隔医療も。
  > 【いま】終値1,914円・直近5日+4.76%（材料未確認）
  > 【調子】➖横ばい（2/13） — 質注意
  > 【水準】🔴過熱（1.0/7）— PER24.039倍・PEG3.8814・52週42.5% ／ 💰単元19.1万円
  > 【戦略】当日高値超えの逆指値1918円で順張り参戦を検討。上限1937.2円・SL1802円目安
- 8081 Kanaden Corporation｜granville_tenkan｜➖横ばい(2)｜🔴過熱｜PASS｜2,795円｜💰27.9万円｜momentum 2809 想定損失幅6.0%。 移行措置銘柄: 10/30 の引けにパッシブ売り（8回に分けて低減）。実施日前後の寄り・引けの需給に注意｜📋カルテ窓 11/04(残14営業日) 📑TOPIX低減対象（次 10/30 第1回/8）
  > 【業態】三菱電機系商社。重電・電子機器からFA・ビル設備・OA機器。インフラ、デバイスも。
  > 【いま】終値2,795円・直近5日+6.56%（材料未確認）
  > 【調子】➖横ばい（2/13）
  > 【水準】🔴過熱（1.0/7）— PER15.571倍・PEG4.1696・52週97.1% ／ 💰単元27.9万円
  > 【戦略】当日高値超えの逆指値2809円で順張り参戦を検討。上限2837.1円・SL2639.5円目安
- 9468 Kadokawa Corporation｜granville_tenkan｜➖横ばい(2)｜🔴過熱｜PASS｜3,749円｜💰37.5万円｜⛔提案なし(指名鮮度切れ 15営業日)｜📋カルテ窓 11/12(残20営業日)
  > 【業態】出版・動画配信大手。カドカワとドワンゴが経営統合。アニメ・電子書籍に強み。
  > 【いま】終値3,749円・直近5日+2.18%（材料未確認）
  > 【調子】➖横ばい（2/13） — 質注意
  > 【水準】🔴過熱（0.0/7）— PER551.323倍・PEG215.754・52週82.8% ／ 💰単元37.5万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 15営業日)）
- 5071 VIS Co., Ltd.｜granville_tenkan｜⚠減速(1)｜⚪妥当｜FAIL_INSEN｜1,375円｜💰13.8万円｜—
- 6770 Alps Alpine Co., Ltd.｜granville_tenkan｜⚠減速(1)｜🟡やや割高｜FAIL_INSEN｜2,156円｜💰21.6万円｜—
- 7981 Takara Standard Co.,Ltd.｜granville_tenkan｜⚠減速(1)｜🟡やや割高｜FAIL_INSEN｜3,000円｜💰30.1万円｜—
- 8129 TOHO HOLDINGS CO., LTD.｜granville_tenkan｜⚠減速(1)｜🟡やや割高｜FAIL_INSEN｜3,921円｜💰39.8万円｜—
- 9502 Chubu Electric Power Company,Incorporated｜granville_tenkan｜🔻悪化(1)｜🟡やや割高｜FAIL_INSEN｜2,670円｜💰26.5万円｜—
- 2267 Yakult Honsha Co.,Ltd.｜granville_tenkan｜⚠減速(1)｜🔴過熱｜FAIL_INSEN｜2,813円｜💰28.4万円｜—
- 8093 Kyokuto Boeki Kaisha, Ltd.｜granville_tenkan｜⚠減速(0)｜⚪妥当｜PASS｜1,749円｜💰17.5万円｜⛔提案なし(指名鮮度切れ 15営業日)｜📋カルテ窓 11/12(残20営業日) ⚠業績基調が下向き（⚠減速） 📑TOPIX低減対象（次 10/30 第1回/8）
  > 【業態】機械商社中堅。産業向け主力で設備、高機能材料も。防衛関連に強み。
  > 【いま】終値1,749円・直近5日-0.68%（材料未確認）
  > 【調子】⚠減速（0/13） — 質注意
  > 【水準】⚪妥当（4.0/7）— PER8.461倍・PEG—・52週13.4% ／ 💰単元17.5万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 15営業日)）
- 1815 鉄建建設｜granville_tenkan｜⚠減速(0)｜⚪妥当｜FAIL_INSEN｜2,169円｜💰21.9万円｜—
- 1969 高砂熱学工業｜granville_tenkan｜⚠減速(0)｜⚪妥当｜FAIL_INSEN｜4,330円｜💰43.5万円｜—
- 3452 B-Lot Company Limited｜granville_tenkan｜取得不可｜💎割安｜FAIL_INSEN｜1,390円｜💰14.0万円｜—
- 4375 Safie Inc.｜changepoint+granville_tenkan｜取得不可｜💎割安｜FAIL_INSEN｜680円｜💰6.8万円｜—
- 8253 Credit Saison Co., Ltd.｜granville_tenkan｜取得不可｜💎割安｜FAIL_INSEN｜4,155円｜💰42.5万円｜—
- 8424 芙蓉総合リース｜granville_tenkan｜取得不可｜💎割安｜FAIL_INSEN｜4,288円｜💰43.1万円｜—
- 4259 ExaWizards Inc.｜changepoint+granville_tenkan+granville_oshime+changepoint🔔｜業績データ取得不可｜⚪妥当｜FAIL_INSEN｜827円｜💰8.4万円｜—
- 8002 Marubeni Corporation｜granville_tenkan｜業績データ取得不可｜⚪妥当｜FAIL_UWAHIGE｜4,872円｜💰48.5万円｜—
- 2871 ニチレイ｜granville_tenkan｜判定保留(変則決算)｜🔴過熱｜FAIL_INSEN｜2,098円｜💰21.1万円｜—
- 4166 Cacco, Inc.｜granville_tenkan｜—｜－未評価｜FAIL_INSEN｜677円｜💰—｜—
- 7725 INTER ACTION Corporation｜granville_tenkan｜—｜－未評価｜FAIL_UWAHIGE｜1,784円｜💰—｜—
- 8061 Seika Corporation｜granville_tenkan｜—｜－未評価｜FAIL_UWAHIGE｜3,045円｜💰—｜—
- 4937 Ｇ−ＷＡＱＯＯ｜granville_oshime｜🚀確変(13)｜⚪妥当｜FAIL_INSEN｜2,322円｜💰23.3万円｜—
- 3083 Star seeds Co.,Ltd.｜granville_oshime+granville_rebound｜🚀確変(11)｜🟢値頃｜FAIL_INSEN｜1,095円｜💰10.9万円｜—｜⚡材料後出し
- 5246 ELEMENTS,Inc.｜granville_oshime｜🔥絶好調(10)｜⚪妥当｜FAIL_INSEN｜1,030円｜💰10.7万円｜—｜⚡材料後出し
- 5702 大紀アルミニウム工業所｜granville_oshime｜🔥絶好調(9)｜💎割安｜FAIL_UWAHIGE｜1,676円｜💰16.7万円｜—
- 8336 Musashino Bank, Ltd.｜granville_oshime｜🔥絶好調(9)｜⚪妥当｜FAIL_INSEN｜2,720円｜💰28.1万円｜—
- 8008 Yondoshi Holdings, Inc.｜granville_oshime｜🔥絶好調(9)｜⚪妥当｜FAIL_INSEN｜2,005円｜💰20.3万円｜—
- 7811 Nakamoto Packs Co. Ltd.｜granville_oshime｜🔥絶好調(8)｜🟢値頃｜FAIL_INSEN｜2,338円｜💰23.4万円｜—
- 8346 Toho Bank, Ltd.｜granville_oshime｜🔥絶好調(8)｜⚪妥当｜FAIL_INSEN｜1,040円｜💰10.8万円｜—
- 4413 baudroie,inc.｜granville_oshime｜🔥絶好調(8)｜🟡やや割高｜FAIL_UWAHIGE｜2,980円｜💰29.7万円｜—
- 7856 HAGIHARA INDUSTRIES INC.｜granville_oshime｜🔥絶好調(8)｜🟡やや割高｜PASS｜2,062円｜💰20.6万円｜oshime 2028 想定損失幅0.5%。 移行措置銘柄: 10/30 の引けにパッシブ売り（8回に分けて低減）。実施日前後の寄り・引けの需給に注意｜⚠日程不明 📑TOPIX低減対象（次 10/30 第1回/8）
  > 【業態】合成繊維大手。土木建築向け樹脂シートが主力。原糸から機械も一貫生産。
  > 【いま】終値2,062円・直近5日+1.23%（材料未確認）
  > 【調子】🔥絶好調（8/13）
  > 【水準】🟡やや割高（2.0/7）— PER20.058倍・PEG0.9486・52週91.5% ／ 💰単元20.6万円
  > 【戦略】2028円までの押し目を指値で待つ。SL2017.8円（25日線基準）
- 1879 新日本建設｜granville_oshime｜⚡好調(7)｜💎割安｜FAIL_INSEN｜2,163円｜💰21.8万円｜—
- 2767 円谷フィールズホールディングス｜granville_oshime｜⚡好調(6)｜⚪妥当｜FAIL_INSEN｜2,459円｜💰25.0万円｜—
- 4667 Aisan Technology Co., Ltd.｜granville_oshime+changepoint🔔+changepoint｜⚡好調(6)｜⚪妥当｜FAIL_INSEN｜1,000円｜💰10.4万円｜—
- 6023 ダイハツインフィニアース｜granville_oshime｜⚡好調(6)｜⚪妥当｜FAIL_UWAHIGE｜3,390円｜💰32.9万円｜—
- 6250 Yamabiko Corporation｜granville_oshime｜⚡好調(6)｜⚪妥当｜FAIL_UWAHIGE｜4,490円｜💰44.1万円｜—
- 2602 日清オイリオグループ｜granville_oshime｜⚡好調(6)｜⚪妥当｜FAIL_INSEN｜2,020円｜💰20.4万円｜—
- 7616 Colowide Co., Ltd.｜granville_oshime｜⚡好調(6)｜⚪妥当｜PASS｜2,061円｜💰20.6万円｜oshime 2036 想定損失幅0.5%。｜⚠日程不明
  > 【業態】外食大手。居酒屋中心に直営展開。傘下にレインズ、アトム、カッパクリエ、大戸屋など。
  > 【いま】終値2,061円・直近5日+4.75%（材料未確認）
  > 【調子】⚡好調（6/13）
  > 【水準】⚪妥当（3.0/7）— PER103.563倍・PEG—・52週79.1% ／ 💰単元20.6万円
  > 【戦略】2036円までの押し目を指値で待つ。SL2025.5円（25日線基準）
- 3994 マネーフォワード｜granville_oshime+changepoint+changepoint🔔｜⚡好調(6)｜🔴過熱｜FAIL_INSEN｜6,480円｜💰66.2万円｜—
- 6058 VECTOR Inc.｜granville_oshime｜⚡好調(6)｜🔴過熱｜FAIL_UWAHIGE｜1,947円｜💰19.7万円｜—
- 8919 カチタス｜granville_oshime｜⚡好調(6)｜🔴過熱｜FAIL_INSEN｜3,385円｜💰35.3万円｜—
- 7350 Okinawa Financial Group, Inc.｜granville_oshime｜⚡好調(5)｜⚪妥当｜FAIL_INSEN｜7,400円｜💰76.1万円｜—
- 8714 Senshu Ikeda Holdings,Inc.｜granville_oshime｜⚡好調(5)｜🟡やや割高｜FAIL_INSEN｜1,057円｜💰10.9万円｜—
- 3399 Maruchiyo Yamaokaya Corporation｜granville_oshime｜⚡好調(5)｜🔴過熱｜FAIL_UWAHIGE｜4,535円｜💰44.6万円｜—
- 4475 HENNGE K.K.｜granville_oshime｜⚡好調(5)｜🔴過熱｜FAIL_INSEN｜1,946円｜💰19.1万円｜—
- 9678 Kanamoto Co., Ltd.｜granville_oshime｜✅順調(4)｜⚪妥当｜PASS｜5,460円｜💰54.6万円｜oshime 5420 想定損失幅0.5%。｜⚠日程不明
  > 【業態】北海道地盤の建機レンタル大手。関東、関西展開。鉱山機械リースも。海外に拡大。
  > 【いま】終値5,460円・直近5日+2.06%（材料未確認）
  > 【調子】✅順調（4/13）
  > 【水準】⚪妥当（3.0/7）— PER14.4倍・PEG0.9403・52週87.1% ／ 💰単元54.6万円
  > 【戦略】5420円までの押し目を指値で待つ。SL5393.2円（25日線基準）
- 4373 Simplex Holdings,Inc.｜granville_oshime｜✅順調(4)｜🟡やや割高｜FAIL_UWAHIGE｜1,201円｜💰11.8万円｜—
- 3097 Monogatari Corporation｜granville_oshime｜✅順調(4)｜🔴過熱｜FAIL_INSEN｜5,530円｜💰55.4万円｜—
- 6998 Nippon Tungsten Co., Ltd.｜granville_oshime｜✅順調(4)｜🔴過熱｜FAIL_INSEN｜3,905円｜💰39.3万円｜—
- 1518 三井松島ホールディングス｜granville_oshime｜✅順調(3)｜🟡やや割高｜PASS｜2,290円｜💰22.9万円｜oshime 2275 想定損失幅0.5%。
  > 【業態】石炭事業撤退で事業投資会社へ。生活関連事業などM&A積極で多展開。(その他製品)
  > 【いま】終値2,290円・直近5日+2.14%（材料未確認）
  > 【調子】✅順調（3/13）
  > 【水準】🟡やや割高（2.0/7）— PER9.858倍・PEG2.1497・52週90.2% ／ 💰単元22.9万円
  > 【戦略】2275円までの押し目を指値で待つ。SL2263.7円（25日線基準）
- 4418 JAPAN DATA SCIENCE CONSORTIUM C｜granville_oshime+changepoint+changepoint🔔｜⚠減速(3)｜🟡やや割高｜PASS｜1,155円｜💰11.6万円｜oshime 1112 想定損失幅0.5%。｜⚠日程不明 ⚠業績基調が下向き（⚠減速）
  > 【業態】AIを活用したアルゴリズムモジュールの開発とライセンス提供。DM発送代行が拡大。
  > 【いま】終値1,155円・直近5日+3.22%（材料未確認）
  > 【調子】⚠減速（3/13） — 減収
  > 【水準】🟡やや割高（2.0/7）— PER17.368倍・PEG1.5273・52週41.4% ／ 💰単元11.6万円
  > 【戦略】1112円までの押し目を指値で待つ。SL1106.8円（25日線基準）
- 6379 RAIZNEXT Corporation｜granville_oshime｜✅順調(3)｜🔴過熱｜PASS｜1,006円｜💰10.1万円｜oshime 996 想定損失幅0.5%。
  > 【業態】ENEOS系、石油精製プラント補修首位。プラント保守、建設に強み。産業領域拡大。
  > 【いま】終値1,006円・直近5日+4.57%（材料未確認）
  > 【調子】✅順調（3/13） — 質注意
  > 【水準】🔴過熱（2.0/7）— PER18.093倍・PEG—・52週85.6% ／ 💰単元10.1万円
  > 【戦略】996円までの押し目を指値で待つ。SL991.5円（25日線基準）
- 9044 NANKAI Co., Ltd.｜granville_oshime｜✅順調(3)｜🟡やや割高｜FAIL_INSEN｜2,980円｜💰30.3万円｜—
- 3107 ダイワボウホールディングス｜granville_oshime｜⚠減速(3)｜🔴過熱｜FAIL_UWAHIGE｜3,577円｜💰35.6万円｜—
- 4208 UBE Corporation｜granville_oshime｜✅順調(3)｜🔴過熱｜FAIL_UWAHIGE｜3,363円｜💰33.6万円｜—
- 7504 Kohsoku Corporation｜granville_oshime｜✅順調(3)｜🔴過熱｜FAIL_INSEN｜4,495円｜💰45.5万円｜—
- 8876 Relo Group, Inc.｜granville_oshime｜✅順調(3)｜🔴過熱｜FAIL_INSEN｜2,412円｜💰24.2万円｜—
- 4189 KH Neochem Co.,Ltd.｜granville_oshime｜⚠減速(2)｜⚪妥当｜FAIL_UWAHIGE｜3,495円｜💰34.5万円｜—
- 6072 Jibannet Holdings Co., Ltd.｜granville_oshime｜🔻悪化(2)｜🟡やや割高｜FAIL_INSEN｜1,073円｜💰10.9万円｜—
- 7630 Ichibanya Co., Ltd.｜granville_oshime｜➖横ばい(2)｜🔴過熱｜FAIL_UWAHIGE｜1,044円｜💰10.5万円｜—
- 8043 Starzen Company Limited｜granville_oshime｜➖横ばい(2)｜🔴過熱｜FAIL_INSEN｜1,511円｜💰15.2万円｜—
- 9505 Hokuriku Electric Power Company｜granville_oshime｜🔻悪化(2)｜🔴過熱｜FAIL_INSEN｜1,093円｜💰11.0万円｜—
- 9616 共立メンテナンス｜granville_oshime｜➖横ばい(2)｜🔴過熱｜FAIL_UWAHIGE｜3,277円｜💰32.8万円｜—
- 9900 Sagami Holdings Corp.｜granville_oshime｜➖横ばい(2)｜🔴過熱｜FAIL_INSEN｜1,072円｜💰10.9万円｜—
- 3048 ビックカメラ｜granville_oshime｜⚠減速(1)｜🟡やや割高｜FAIL_UWAHIGE｜1,700円｜💰16.8万円｜—
- 8097 SAN-AI OBBLI CO. LTD｜granville_oshime｜⚠減速(1)｜🔴過熱｜FAIL_INSEN｜2,466円｜💰24.6万円｜—
- 8059 Daiichi Jitsugyo Co., Ltd.｜granville_oshime｜⚠減速(0)｜🔴過熱｜FAIL_INSEN｜3,555円｜💰35.4万円｜—
- 276A CCReB Advisors Inc.｜granville_oshime｜判定保留｜🟢値頃｜FAIL_INSEN｜4,115円｜💰43.0万円｜—
- 290A ＳＹＮＳＰＥＣＴＩＶＥ｜granville_oshime｜判定保留(変則決算)｜🔴過熱｜FAIL_INSEN｜1,298円｜💰13.2万円｜—
- 8343 Akita Bank, Ltd.｜granville_oshime｜業績データ取得不可(売上/経常欠損)｜🟢値頃｜FAIL_INSEN｜1,588円｜💰16.8万円｜—
- 8360 Yamanashi Chuo Bank, Ltd.｜granville_oshime｜取得不可｜🟢値頃｜FAIL_INSEN｜1,355円｜💰14.3万円｜—
- 336A ダイナミックマッププラットフォーム｜granville_oshime｜業績データ取得不可(経常益予想非開示)｜⚪妥当｜FAIL_INSEN｜1,309円｜💰13.7万円｜—
- 4478 freee K.K.｜granville_oshime+granville_rebound+changepoint🔔+changepoint｜業績データ取得不可｜⚪妥当｜FAIL_INSEN｜3,555円｜💰36.7万円｜—
- 3697 SHIFT Inc.｜granville_oshime｜取得不可｜⚪妥当｜PASS｜900円｜💰9.0万円｜⛔提案なし(指名鮮度切れ 15営業日)｜⚠決算 10/15(残1営業日)
  > 【業態】ソフトウエアのテスト受託事業が主力。ソフトの品質保証や関連コンサル、マーケティングも。
  > 【いま】終値900円・直近5日+2.37%（材料未確認）
  > 【調子】取得不可
  > 【水準】⚪妥当（4.0/7）— PER—倍・PEG—・52週44.6% ／ 💰単元9.0万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 15営業日)）
- 6810 Maxell, Ltd.｜granville_oshime｜取得不可｜⚪妥当｜FAIL_INSEN｜2,534円｜💰25.7万円｜—｜⚡材料後出し
- 8367 Nanto Bank Ltd.｜granville_oshime｜取得不可｜⚪妥当｜FAIL_INSEN｜1,883円｜💰19.5万円｜—
- 8544 Keiyo Bank, Ltd.｜granville_oshime｜取得不可｜⚪妥当｜FAIL_INSEN｜2,667円｜💰27.8万円｜—
- 6027 弁護士ドットコム｜granville_oshime｜業績データ取得不可｜🔴過熱｜FAIL_INSEN｜4,970円｜💰52.0万円｜—
- 8511 Japan Securities Finance Co., Ltd.｜granville_oshime｜取得不可｜🔴過熱｜FAIL_INSEN｜2,192円｜💰22.5万円｜—
- 8362 Fukui Bank, Ltd.｜granville_oshime｜🔻悪化｜🔴過熱｜FAIL_INSEN｜7,240円｜💰76.0万円｜—
- 4044 Central Glass Co., Ltd.｜granville_oshime｜—｜－未評価｜FAIL_INSEN｜4,605円｜💰—｜—
- 4765 ＳＢＩグローバルアセットマネジメント｜granville_oshime｜判定保留｜⏸判定不能｜FAIL_INSEN｜606円｜💰6.2万円｜—
- 8622 Mito Securities Co., Ltd.｜granville_oshime+granville_rebound｜取得不可｜⏸判定不能｜FAIL_INSEN｜826円｜💰8.3万円｜—
- 8624 Ichiyoshi Securities Co., Ltd.｜granville_oshime+granville_rebound｜取得不可｜⏸判定不能｜FAIL_INSEN｜1,564円｜💰15.8万円｜—
- 8628 松井証券｜granville_oshime｜業績データ取得不可｜⏸判定不能｜FAIL_INSEN｜1,112円｜💰11.4万円｜—
- 8707 IwaiCosmo Holdings, Inc.｜granville_oshime｜取得不可｜⏸判定不能｜FAIL_INSEN｜4,625円｜💰47.3万円｜—
- 8708 アイザワ証券グループ｜granville_oshime｜取得不可｜⏸判定不能｜FAIL_INSEN｜1,630円｜💰16.6万円｜—
- 7878 Kohsai Co.Ltd.｜granville_rebound｜🚀確変(11)｜💎割安｜FAIL_INSEN｜1,017円｜💰10.2万円｜—
- 9237 Emimen Co.,Ltd.｜granville_rebound｜🔥絶好調(10)｜🟢値頃｜FAIL_UWAHIGE｜821円｜💰8.2万円｜—
- 2122 インタースペース｜granville_rebound｜🔥絶好調(9)｜⚪妥当｜PASS｜1,365円｜💰13.7万円｜reversal 1365 想定損失幅4.8%。｜📋カルテ窓 11/10(残18営業日)
  > 【業態】成果報酬型広告大手。「ママスタ」など女性向けメディアサービス事業も注力。
  > 【いま】終値1,365円・直近5日+3.02%（材料未確認）
  > 【調子】🔥絶好調（9/13）
  > 【水準】⚪妥当（4.0/7）— PER20.404倍・PEG0.2387・52週58.9% ／ 💰単元13.7万円
  > 【戦略】当日終値1365円の指値で反転を取りにいく。SL1300円（直近5日安値）
- 8995 Makoto Construction Co,Ltd｜granville_rebound｜🔥絶好調(9)｜⚪妥当｜FAIL_UWAHIGE｜1,737円｜💰16.8万円｜—
- 1407 West Holdings Corporation｜granville_rebound｜🔥絶好調(8)｜🟢値頃｜FAIL_INSEN｜2,156円｜💰21.5万円｜—
- 5574 ABEJA,Inc.｜granville_rebound｜🔥絶好調(8)｜⚪妥当｜FAIL_INSEN｜2,716円｜💰27.4万円｜—
- 4392 ＦＩＧ｜granville_rebound｜🔥絶好調(8)｜⚪妥当｜PASS｜990円｜💰9.9万円｜reversal 990 想定損失幅15.7%。｜⚠日程不明
  > 【業態】情報・通信業
  > 【いま】終値990円・直近5日+8.43%（材料未確認）
  > 【調子】🔥絶好調（8/13）
  > 【水準】⚪妥当（3.0/7）— PER51.295倍・PEG2.4351・52週25.3% ／ 💰単元9.9万円
  > 【戦略】当日終値990円の指値で反転を取りにいく。SL835円（直近5日安値）
- 2933 KIBUN FOODS INC.｜granville_rebound｜⚡好調(7)｜🟢値頃｜FAIL_INSEN｜1,063円｜💰10.7万円｜—
- 8522 Bank of Nagoya, Ltd.｜granville_rebound｜⚡好調(7)｜⚪妥当｜FAIL_INSEN｜6,440円｜💰71.4万円｜—
- 5242 EYEZ INC.｜granville_rebound｜⚡好調(7)｜🔴過熱｜PASS_DOJI｜1,873円｜💰18.7万円｜reversal 1873 想定損失幅3.1%。｜⚠日程不明
  > 【業態】広告業界に特化マッチングプラットフォーム「メディアレーダー」を提供。コスメ情報に進出。
  > 【いま】終値1,873円・直近5日-15.33%（材料未確認）
  > 【調子】⚡好調（7/13）
  > 【水準】🔴過熱（1.0/7）— PER645.862倍・PEG5.8715・52週44.4% ／ 💰単元18.7万円
  > 【戦略】当日終値1873円の指値で反転を取りにいく。SL1815円（直近5日安値）
- 6336 Ishii Hyoki Co., Ltd.｜granville_rebound｜⚡好調(6)｜🟢値頃｜PASS_DOJI｜1,520円｜💰15.2万円｜⛔提案なし(指名鮮度切れ 16営業日)｜⚠日程不明
  > 【業態】プリント基板製造装置の大手。ディスプレイ用インクジェット塗布機、印刷技術にも力。
  > 【いま】終値1,520円・直近5日-11.94%（材料未確認）
  > 【調子】⚡好調（6/13）
  > 【水準】🟢値頃（5.6/7）— PER11.36倍・PEG0.4381・52週53.5% ／ 💰単元15.2万円
  > 【戦略】発注対象外（⛔提案なし(指名鮮度切れ 16営業日)）
- 6952 Casio Computer Co., Ltd.｜granville_rebound｜⚡好調(6)｜⚪妥当｜FAIL_INSEN｜2,246円｜💰22.7万円｜—
- 2354 YE DIGITAL CORPORATION｜granville_rebound｜⚡好調(5)｜🟢値頃｜FAIL_INSEN｜1,111円｜💰11.4万円｜—
- 5889 ＪＡＰＡＮ　ＥＹＥＷＥＡＲ　ＨＯＬＤＩＮＧＳ｜granville_rebound｜⚡好調(5)｜🟢値頃｜FAIL_INSEN｜2,122円｜💰21.7万円｜—
- 4997 日本農薬｜granville_rebound｜✅順調(4)｜🟡やや割高｜FAIL_INSEN｜1,081円｜💰10.9万円｜—
- 4346 NEXYZ.Group Corporation｜granville_rebound｜✅順調(3)｜🟢値頃｜FAIL_INSEN｜763円｜💰8.0万円｜—
- 7354 Direct Marketing MiX Inc.｜granville_rebound｜✅順調(3)｜⚪妥当｜FAIL_INSEN｜353円｜💰3.6万円｜—
- 2681 2nd RETAILING Co., Ltd.｜granville_rebound｜✅順調(3)｜🟡やや割高｜FAIL_INSEN｜2,104円｜💰21.4万円｜—
- 4082 第一稀元素化学工業｜granville_rebound｜🔻悪化(3)｜🟡やや割高｜FAIL_INSEN｜1,974円｜💰20.1万円｜—
- 3653 Morpho, Inc.｜granville_rebound｜🔻悪化(2)｜💎割安｜FAIL_INSEN｜886円｜💰9.1万円｜—
- 3907 Silicon Studio Corp.｜granville_rebound｜🔻悪化(2)｜🟢値頃｜FAIL_UWAHIGE｜1,674円｜💰15.7万円｜—｜⚡材料後出し
- 6522 アスタリスク｜granville_rebound｜⚠減速(2)｜⚪妥当｜PASS｜1,063円｜💰10.6万円｜reversal 1063 想定損失幅4.4%。｜⚠決算 10/15(残1営業日) ⚠業績基調が下向き（⚠減速）
  > 【業態】モバイル機器に装着するバーコードリーダーの開発・販売。モバイル向けSIも注力。
  > 【いま】終値1,063円・直近5日-9.53%（材料未確認）
  > 【調子】⚠減速（2/13） — 減収
  > 【水準】⚪妥当（4.2/7）— PER—倍・PEG—・52週32.3% ／ 💰単元10.6万円
  > 【戦略】当日終値1063円の指値で反転を取りにいく。SL1016円（直近5日安値）
- 8163 SRS HOLDINGS CO.,LTD.｜granville_rebound｜➖横ばい(2)｜🔴過熱｜FAIL_INSEN｜1,487円｜💰14.8万円｜—
- 4691 Washington Hotel Corp.｜granville_rebound｜⚠減速(1)｜⚪妥当｜FAIL_INSEN｜1,910円｜💰19.2万円｜—
- 4543 Terumo Corporation｜granville_rebound｜業績データ取得不可(経常益予想非開示)｜⚪妥当｜FAIL_INSEN｜2,254円｜💰23.3万円｜—
- 3563 FOOD & LIFE COMPANIES LTD.｜granville_rebound｜判定保留(データ不足)｜🟡やや割高｜FAIL_INSEN｜5,412円｜💰54.8万円｜—
- 5844 Kyoto Financial Group,Inc.｜granville_rebound｜—｜－未評価｜FAIL_INSEN｜4,348円｜💰—｜—
- 8381 San-in Godo Bank Ltd.｜granville_rebound｜—｜－未評価｜FAIL_INSEN｜2,330円｜💰—｜—
- 8399 Bank Of The Ryukyus,Limited｜granville_rebound｜—｜－未評価｜FAIL_INSEN｜2,936円｜💰—｜—
- 8713 Fidea Holdings Co.Ltd.｜granville_rebound｜—｜－未評価｜FAIL_INSEN｜2,483円｜💰—｜—

## 変化点銘柄
- 5803 フジクラ｜changepoint+changepoint🔔+changepoint🔔🔔｜🚀確変(12)｜⚪妥当｜FAIL_UWAHIGE｜5,200円｜💰50.7万円｜—
- 6254 野村マイクロ・サイエンス｜changepoint+changepoint🔔｜🔥絶好調(10)｜💎割安｜FAIL_INSEN｜3,435円｜💰34.9万円｜—
- 4187 大阪有機化学工業｜changepoint🔔+changepoint｜🔥絶好調(10)｜⚪妥当｜FAIL_INSEN｜5,160円｜💰51.1万円｜—
- 6136 OSG CORP｜changepoint+changepoint🔔+changepoint🔔🔔｜🔥絶好調(10)｜⚪妥当｜FAIL_UWAHIGE｜3,984円｜💰38.6万円｜—
- 7695 交換できるくん｜changepoint｜🔥絶好調(10)｜⚪妥当｜FAIL_INSEN｜835円｜💰8.3万円｜—
- 4419 Ｆｉｎａｔｅｘｔホールディングス｜changepoint+changepoint🔔｜🔥絶好調(10)｜⚪妥当｜FAIL_INSEN｜1,490円｜💰15.0万円｜—
- 584A LiNKX, Inc.｜changepoint｜🔥絶好調(9)｜🟢値頃｜FAIL_INSEN｜2,392円｜💰24.3万円｜—
- 8151 東陽テクニカ｜changepoint｜🔥絶好調(9)｜⚪妥当｜FAIL_UWAHIGE｜1,920円｜💰19.2万円｜—
- 4382 HEROZ, Inc.｜changepoint+changepoint🔔+changepoint🔔🔔｜🔥絶好調(9)｜🟡やや割高｜FAIL_UWAHIGE｜1,400円｜💰14.0万円｜—
- 7318 セレンディップ・ホールディングス｜changepoint🔔｜🔥絶好調(8)｜💎割安｜FAIL_INSEN｜1,227円｜💰12.7万円｜—
- 9888 UEX LTD｜changepoint+changepoint🔔｜🔥絶好調(8)｜🟢値頃｜FAIL_INSEN｜1,214円｜💰12.3万円｜—
- 4368 扶桑化学工業｜changepoint+changepoint🔔｜🔥絶好調(8)｜⚪妥当｜FAIL_INSEN｜3,400円｜💰33.8万円｜—
- 8697 日本取引所グループ｜changepoint🔔｜🔥絶好調(8)｜🟡やや割高｜FAIL_INSEN｜2,189円｜💰22.6万円｜—
- 9343 アイビス｜changepoint｜⚡好調(6)｜⚪妥当｜FAIL_INSEN｜763円｜💰7.7万円｜—
- 286A EUCALIA Inc.｜changepoint｜⚡好調(5)｜🟢値頃｜FAIL_INSEN｜753円｜💰7.7万円｜—
- 8704 Traders Holdings Co.,Ltd.｜changepoint🔔+changepoint｜⚡好調(5)｜🟢値頃｜FAIL_INSEN｜1,346円｜💰13.7万円｜—
- 6597 6597｜changepoint🔔+changepoint｜⚡好調(5)｜⚪妥当｜FAIL_INSEN｜3,850円｜💰39.0万円｜—｜⚡材料後出し
- 593A ティアフォー｜changepoint🔔+changepoint｜✅順調(4)｜🔴過熱｜FAIL_UWAHIGE｜2,240円｜💰22.8万円｜—
- 4498 Cybertrust Japan Co., Ltd.｜changepoint🔔+changepoint+changepoint🔔🔔｜✅順調(4)｜🔴過熱｜FAIL_INSEN｜1,861円｜💰18.5万円｜—
- 4071 プラスアルファ・コンサルティング｜changepoint｜✅順調(3)｜⚪妥当｜FAIL_INSEN｜2,185円｜💰21.8万円｜—
- 4488 AI inside Inc.｜changepoint｜➖横ばい(2)｜🟡やや割高｜FAIL_UWAHIGE｜2,151円｜💰21.3万円｜—
- 339A PROGRESS TECHNOLOGIES GROUP INC｜changepoint+changepoint🔔｜⚠減速(1)｜⚪妥当｜FAIL_INSEN｜912円｜💰9.2万円｜—｜⚡材料後出し
- 4011 Headwaters Co.,Ltd｜changepoint🔔+changepoint｜判定保留｜💎割安｜FAIL_INSEN｜2,325円｜💰23.8万円｜—
- 3923 ラクス｜changepoint+changepoint🔔｜判定保留(変則決算)｜⚪妥当｜FAIL_INSEN｜1,131円｜💰11.3万円｜—
- 4165 PLAID,Inc.｜changepoint🔔+changepoint｜判定保留(変則決算: 連2025.09→連 予2026.12)｜🔴過熱｜PASS｜752円｜💰7.5万円｜changepoint 752 想定損失幅6.8%。｜⚠日程不明 🔒実弾封印中(PL3紙ログ収集中)
  > 【業態】クラウド型CX(顧客体験)プラットフォーム「KARTE」を提供。グーグルと提携。
  > 【いま】終値752円・直近5日+3.58%（材料未確認）
  > 【調子】判定保留(変則決算: 連2025.09→連 予2026.12)
  > 【水準】🔴過熱（1.4/7）— PER51.507倍・PEG35.5397・52週50.8% ／ 💰単元7.5万円
  > 【戦略】発火日終値752円の指値。追撃禁止・SL701円。🔒実弾封印中（PL3紙ログ収集中）

## 🤖AI特需銘柄
波: ❄️冷却・空調・🌐光通信・🔬基板・素材／25MA 上回り率 📡エネマネ・計量 42.86%・❄️冷却・空調 66.67%・🌐光通信 81.82%・🔬基板・素材 76.19%
- 3131 シンデンハイテックス｜ai_momentum｜🚀確変(12)｜🟢値頃｜FAIL_INSEN｜7,690円｜💰81.1万円｜—
- 2760 東京エレクトロンデバイス｜ai_momentum｜🔥絶好調(10)｜⚪妥当｜FAIL_UWAHIGE｜5,170円｜💰49.6万円｜—
- 9824 泉州電業｜ai_momentum｜🔥絶好調(10)｜⚪妥当｜FAIL_UWAHIGE｜8,570円｜💰84.1万円｜—
- 6227 AIMECHATEC Ltd.｜granville_rebound+ai_momentum｜⚡好調(6)｜🟡やや割高｜FAIL_INSEN｜8,250円｜💰85.0万円｜—
- 8159 立花エレテック｜granville_oshime+ai_momentum｜✅順調(4)｜🟡やや割高｜FAIL_UWAHIGE｜4,770円｜💰46.6万円｜—
- 1982 日比谷総合設備｜ai_momentum｜⚠減速(1)｜🔴過熱｜FAIL_UWAHIGE｜3,410円｜💰33.8万円｜—
- 9960 トーテック｜granville_tenkan+granville_oshime+ai_momentum｜⚠減速(1)｜🔴過熱｜FAIL_INSEN｜4,250円｜💰42.5万円｜—
- 4658 日本空調サービス｜granville_tenkan+ai_reversal｜⚡好調(5)｜⚪妥当｜FAIL_UWAHIGE｜1,561円｜💰15.6万円｜—
- 8098 稲畑産業｜ai_reversal+granville_oshime｜✅順調(4)｜🔴過熱｜FAIL_INSEN｜4,395円｜💰43.9万円｜—
- 6643 戸上電機製作所｜ai_reversal｜✅順調(3)｜🟡やや割高｜FAIL_INSEN｜5,510円｜💰54.9万円｜—
- 9432 NTT｜ai_reversal｜➖横ばい(2)｜🔴過熱｜FAIL_INSEN｜172円｜💰1.7万円｜—

## ⚡材料後出し
その日の足は開示前の情報。判定は参考値。
- 135A VRAIN Solution,Inc.｜📊2027年２月期 第２四半期（中間期）決算短信〔日本基準〕(非連結)｜判定 FAIL_INSEN
- 9560 PROGRIT, Inc.｜📊2026年８月期決算短信〔日本基準〕(連結)｜判定 PASS
- 4743 ITFOR Inc.｜📌ラジオNIKKEI主催「ジャパンツアーIR &amp; 櫻井英明株式講演(2026/11/14)」（仙台会場）登壇のお知らせ｜判定 FAIL_UWAHIGE
- 505A Geekly,Inc.｜📊2027年５月期 第１四半期決算短信〔日本基準〕（非連結）｜判定 FAIL_UWAHIGE
- 6629 TECHNO HORIZON Co., Ltd.｜📌高校生が「画像処理技術」の仕組みを体験、企業訪問プログラムの一環として、情報Ｉ・数学・ものづくりをつなぐ画像処理体験プログラムを実施｜判定 FAIL_INSEN
- 6183 BELLSYSTEM24 Holdings, Inc.｜📊2027年２月期第２四半期（中間期）決算短信〔ＩＦＲＳ〕（連結）｜判定 FAIL_INSEN
- 3608 TSI Holdings Co.,Ltd.｜📊2027年２月期第２四半期（中間期）決算短信〔日本基準〕(連結)｜判定 FAIL_INSEN
- 3562 No.1 Co., Ltd.｜📊2027年２月期　第２四半期（中間期）決算短信〔日本基準〕（連結）｜判定 FAIL_INSEN
- 3083 Star seeds Co.,Ltd.｜📊2027年２月期 第２四半期（中間期）決算短信〔日本基準〕（連結）｜判定 FAIL_INSEN
- 5246 ELEMENTS,Inc.｜📊2026年11月期　第３四半期決算短信〔日本基準〕(連結)｜判定 FAIL_INSEN
- 6810 Maxell, Ltd.｜📌マクセル、「全固体電池バックアップモジュール」の量産を開始｜判定 FAIL_INSEN
- 3907 Silicon Studio Corp.｜📌シリコンスタジオ、企業理念としてMVV（ミッション・ビジョン・バリュー）を策定｜判定 FAIL_UWAHIGE
- 6597 6597｜📌（開示事項の経過）特別当座貸越契約の締結に関するお知らせ｜判定 FAIL_INSEN
- 339A PROGRESS TECHNOLOGIES GROUP INC｜📊2027年２月期 第２四半期（中間期）決算短信〔ＩＦＲＳ〕（連結）｜判定 FAIL_INSEN

## 📢開示
使用URL: https://kabutan.jp/disclosures/?date=20261014&page=1〜41（全41ページ・603行を取得。フォールバックなし）。プール在籍銘柄のみ表示（英文のみの重複・ガバナンス報告書・説明会資料・補足資料は除外）。①-9へ引き渡し: recalc_queue 追加9件
- 📊 135A VRAIN Solution,Inc.｜2027年２月期 第２四半期（中間期）決算短信〔日本基準〕(非連結)｜16:15
- 📊 3077 Horiifoodservice Co., Ltd.｜2026年11月期第３四半期決算短信〔日本基準〕(連結)｜14:00
- 📊 3083 Star seeds Co.,Ltd.｜2027年２月期 第２四半期（中間期）決算短信〔日本基準〕（連結）｜17:00
- 📊 339A PROGRESS TECHNOLOGIES GROUP INC｜2027年２月期 第２四半期（中間期）決算短信〔ＩＦＲＳ〕（連結）｜15:30
- 📊 3562 No.1 Co., Ltd.｜2027年２月期　第２四半期（中間期）決算短信〔日本基準〕（連結）｜15:30
- 📊 3608 TSI Holdings Co.,Ltd.｜2027年２月期第２四半期（中間期）決算短信〔日本基準〕(連結)｜15:30
- 📊 505A Geekly,Inc.｜2027年５月期 第１四半期決算短信〔日本基準〕（非連結）｜16:00
- 📊 5246 ELEMENTS,Inc.｜2026年11月期　第３四半期決算短信〔日本基準〕(連結)｜16:00
- 📊 6183 BELLSYSTEM24 Holdings, Inc.｜2027年２月期第２四半期（中間期）決算短信〔ＩＦＲＳ〕（連結）｜15:30
- 📊 9560 PROGRIT, Inc.｜2026年８月期決算短信〔日本基準〕(連結)｜15:30
- 📌 135A VRAIN Solution,Inc.｜子会社の設立に関するお知らせ｜16:15
- 📌 1815 鉄建建設｜人事異動に関するお知らせ｜14:00
- 📌 3077 Horiifoodservice Co., Ltd.｜特別利益（負ののれん発生益）の計上に関するお知らせ｜14:00
- 📌 3077 Horiifoodservice Co., Ltd.｜2026年11月期 月次売上速報（9月度）のお知らせ｜14:00
- 📌 3083 Star seeds Co.,Ltd.｜2027年２月期第２四半期（中間期）連結業績予想と実績値との差異に関するお知らせ｜17:00
- 📌 3562 No.1 Co., Ltd.｜No.1、中小企業向けワンストップSOCサービス「No.1ビジSOC」を提供開始｜15:30
- 📌 3562 No.1 Co., Ltd.｜剰余金の配当に関するお知らせ｜15:30
- 📌 3608 TSI Holdings Co.,Ltd.｜株式会社ワールドと株式会社TSIホールディングスとの 共同持株会社設立（株式移転）による経営統合に関するお知らせ｜15:30
- 📌 3608 TSI Holdings Co.,Ltd.｜2027年２月期第２四半期（中間期）連結業績予想と実績の差異に関するお知らせ｜15:30
- 📌 3608 TSI Holdings Co.,Ltd.｜（開示事項の経過）東洋エンタープライズ株式会社及び株式会社レイラニトレーディングの株式取得価額に関するお知らせ｜15:30
- 📌 3907 Silicon Studio Corp.｜シリコンスタジオ、企業理念としてMVV（ミッション・ビジョン・バリュー）を策定｜16:00
- 📌 4259 ExaWizards Inc.｜統合報告書「Integrated Report 2026」公開に関するお知らせ｜08:40
- 📌 4272 Nippon Kayaku Co., Ltd.｜Nippon Kayaku Group 統合報告書2026後半｜00:30
- 📌 4272 Nippon Kayaku Co., Ltd.｜Nippon Kayaku Group 統合報告書2026前半｜00:30
- 📌 4419 Ｆｉｎａｔｅｘｔホールディングス｜Finatext、メディケア生命にて、保険金請求の不正検知におけるAI活用の実証実験（PoC）を開始｜14:00
- 📌 4743 ITFOR Inc.｜ラジオNIKKEI主催「ジャパンツアーIR &amp; 櫻井英明株式講演(2026/11/14)」（仙台会場）登壇のお知らせ｜15:30
- 📌 5246 ELEMENTS,Inc.｜通期連結業績予想の修正に関するお知らせ｜16:00
- 📌 5246 ELEMENTS,Inc.｜2026年11月期第３四半期決算において想定されるご質問への回答について｜16:00
- 📌 558A SQUEEZE Inc.｜SQUEEZE、第一リアルターとの連携を加速 大阪・難波に「Minn」2施設を2026年12月開業予定｜11:00
- 📌 593A ティアフォー｜国土交通省「自動物流道路の社会実装に向けた実証実験」の採択に関するお知らせ｜13:00
- 📌 6183 BELLSYSTEM24 Holdings, Inc.｜剰余金の配当（中間配当）に関するお知らせ｜15:30
- 📌 6597 6597｜（開示事項の経過）特別当座貸越契約の締結に関するお知らせ｜15:30
- 📌 6629 TECHNO HORIZON Co., Ltd.｜高校生が「画像処理技術」の仕組みを体験、企業訪問プログラムの一環として、情報Ｉ・数学・ものづくりをつなぐ画像処理体験プログラムを実施｜16:00
- 📌 6810 Maxell, Ltd.｜マクセル、「全固体電池バックアップモジュール」の量産を開始｜16:45
- 📌 7199 Premium Group Co., Ltd.｜統合報告書2026｜00:30

## 総当りゲート
### 5手法
- PASS（12）: 5136 tripla Co.,Ltd.、5892 yutori,Inc.、9560 PROGRIT, Inc.、9628 San Holdings,Inc.、6317 Kitagawa Corporation、8282 K'S HOLDINGS CORPORATION、9412 SKY Perfect JSAT Corporation、1871 PS Construction Co., Ltd.、4928 Noevir Holdings Co., Ltd.、9699 NISHIO HOLDINGS CO. LTD.、7624 NaITO、7713 シグマ光機
- PASS_DOJI（2）: 9268 OPTIMUS GROUP Co., Ltd.、7003 Mitsui ES Holdings Co., Ltd.
- FAIL_UWAHIGE（25）: 5027 AnyMind Group Inc.、5757 CK San-Etsu Co., Ltd.、479A PRONI Inc.、6298 Y.A.C.HOLDINGS CO.,LTD.、2334 Eole, Inc.、5821 Hirakawa Hewtech Corp.、4477 BASE, Inc.、2980 SRE Holdings Corp.、4743 ITFOR Inc.、505A Geekly,Inc.、6289 Giken Ltd.、6862 Minato Holdings Inc.、3374 Naigai Tec Corporation、2820 Yamami Co.、6474 Nachi-Fujikoshi Corp.、8086 NIPRO Corporation、4666 Park24 Co., Ltd.、9627 アインホールディングス、5602 Kurimoto,Ltd.、7984 Kokuyo Co., Ltd.、5110 Sumitomo Rubber Industries, Ltd.、3471 Mitsui Fudosan Logistics Park, Inc.、3249 Industrial & Infrastructure Fund Investment Corporation、8984 Daiwa House REIT Investment Corporation、6814 古野電
- FAIL_INSEN（118）: 6627 Tera Probe, Inc.、5137 Smart Drive Co. Ltd.、3723 Nihon Falcom Corporation、5724 Asaka Riken Co., Ltd.、4053 Sun Asterisk, Inc.、212A FIT EASY Inc.、9554 AViC Co. Ltd.、421A Movin' Strategic Career CO.,LTD.、9211 f-code Inc.、4412 Science Arts, Inc.、4377 ONE CAREER Inc.、5537 AlbaLink Co.,Ltd.、9556 INTLOOP, Inc.、7047 PORT INC.、135A VRAIN Solution,Inc.、146A Columbia Works Inc.、5590 ネットスターズ、6071 IBJ, Inc.、558A SQUEEZE Inc.、3798 ULS Group Incorporated、5038 eWeLL Co.,Ltd、6629 TECHNO HORIZON Co., Ltd.、6492 Okano Valve Mfg. Co., Ltd.、325A TENTIAL, Inc.、3077 Horiifoodservice Co., Ltd.、6918 Aval Data Corporation、7480 Suzuden Corporation、7567 Sakae Electronics Corp.、269A SAPEET、6337 Tesec Corporation、9251 G-AB&Company Co.,Ltd.、4331 Take and Give. Needs Co., Ltd.、8370 Kiyo Bank, Ltd.、7161 Jimoto Holdings, Inc.、2340 Gokurakuyu Holdings Co., Ltd.、7175 今村証券、8871 GOLDCREST Co., Ltd.、3391 TSURUHA Holdings, Inc.、3186 ネクステージ、3222 United Super Markets Holdings, Inc.、1803 Shimizu Corporation、4023 クレハ、7906 Yonex Co., Ltd.、2874 YOKOREI CO. LTD.、7550 Zensho Holdings Co., Ltd.、8088 IWATANI Corporation、8125 Wakita & Co., Ltd.、9861 吉野家ホールディングス、8278 Fuji Co., Ltd.、7458 Daiichikosho Co., Ltd.、7564 Workman Co., Ltd.、2702 日本マクドナルドホールディングス、2782 Seria Co., Ltd.、2809 Kewpie Corporation、7731 Nikon Corp.、8923 Tosei Corporation、7762 Citizen Watch Co, Ltd.、9031 Nishi-Nippon Railroad Co., Ltd.、4680 ROUND ONE Corporation、6465 HOSHIZAKI Corp.、8934 Sun Frontier Fudousan Co., Ltd.、1861 Kumagai Gumi Co., Ltd.、3148 Create SD Holdings Co., Ltd.、1332 Nissui Corporation、6269 Modec, Inc.、8584 Jaccs Co., Ltd.、9882 Yellow Hat Ltd.、1860 Toda Corporation、8066 Mitani Corporation、2659 SAN-A CO., LTD.、2805 S&B Foods Inc.、5021 Cosmo Energy Holdings Co., Ltd.、8233 Takashimaya Company, Limited、3289 Tokyu Fudosan Holdings Corp.、4028 ISHIHARA SANGYO KAISHA, LTD.、8818 Keihanshin Building Co., Ltd.、1333 Umios Corporation、1719 HAZAMA ANDO Corporation、1833 Okumura Corporation、2875 Toyo Suisan Kaisha, Ltd.、9503 Kansai Electric Power Company, Incorporated、3099 Isetan Mitsukoshi Holdings Ltd.、1893 Penta-Ocean Construction Co., Ltd.、6753 Sharp Corporation、8276 HEIWADO CO., LTD.、9974 BELC Co., Ltd.、5482 Aichi Steel Corporation、2815 ARIAKE JAPAN Co., Ltd.、9436 Okinawa Cellular Telephone Company、1662 Japan Petroleum Exploration Co., Ltd.、6804 Hosiden Corp.、6183 BELLSYSTEM24 Holdings, Inc.、8585 Orient Corporation、8194 Life Corporation、8987 Japan Excellent, Inc.、7201 Nissan Motor Co., Ltd.、8174 NIPPON GAS Co., Ltd.、3234 Mori Hills Reit Investment Corporation、3279 Activia Properties, Inc.、3283 Nippon Prologis REIT, Inc.、3292 AEON REIT Investment Corp.、3296 NIPPON REIT Investment Corp、3309 Sekisui House Reit. Inc.、3462 Nomura Real Estate Master Fund, Inc.、8952 Japan Real Estate Investment Corp.、8953 Japan Metropolitan Fund Investment Corporation、8954 ORIX JREIT Inc.、8955 Japan Prime Realty Investment Corporation、8961 MORI TRUST REIT.Inc、8986 Daiwa Securities Living Investment Corporation、6668 ＡＤプラズマ、3498 霞ヶ関Ｃ、4443 Ｓａｎｓａｎ、5932 三協立山、9308 乾汽船、4180 ＡＰＰＩＥＲ　ＧＲＯＵＰ、4431 スマレジ、4493 Cyber Security Cloud, Inc.
### グランビル
- PASS（18）: 5036 Japan Business Systems, Inc.、8014 Chori Co., Ltd.、3549 KUSURI NO AOKI HOLDINGS CO.,LTD.、4183 Mitsui Chemicals, Inc.、2413 エムスリー、8081 Kanaden Corporation、9468 Kadokawa Corporation、8093 Kyokuto Boeki Kaisha, Ltd.、7856 HAGIHARA INDUSTRIES INC.、7616 Colowide Co., Ltd.、9678 Kanamoto Co., Ltd.、1518 三井松島ホールディングス、4418 JAPAN DATA SCIENCE CONSORTIUM C、6379 RAIZNEXT Corporation、3697 SHIFT Inc.、2122 インタースペース、4392 ＦＩＧ、6522 アスタリスク
- PASS_DOJI（2）: 5242 EYEZ INC.、6336 Ishii Hyoki Co., Ltd.
- FAIL_UWAHIGE（37）: 6905 Cosel Co., Ltd.、3496 AZOOM CO.,LTD、6255 NPC Incorporated、6395 TADANO Ltd.、9064 ヤマトホールディングス、6432 Takeuchi Mfg.Co., Ltd.、3064 MonotaRO Co., Ltd.、3661 m-up holdings, Inc.、8020 Kanematsu Corporation、9045 Keihan Holdings Co.,Ltd.、8060 キヤノンマーケティングジャパン、8056 BIPROGY Inc.、4272 Nippon Kayaku Co., Ltd.、4956 Konishi Co., Ltd.、5461 Chubu Steel Plate Co., Ltd.、7513 Kojima Co., Ltd.、4274 HOSOYA PYRO-ENGINEERING CO LTD、7751 キヤノン、8002 Marubeni Corporation、7725 INTER ACTION Corporation、8061 Seika Corporation、5702 大紀アルミニウム工業所、4413 baudroie,inc.、6023 ダイハツインフィニアース、6250 Yamabiko Corporation、6058 VECTOR Inc.、3399 Maruchiyo Yamaokaya Corporation、4373 Simplex Holdings,Inc.、3107 ダイワボウホールディングス、4208 UBE Corporation、4189 KH Neochem Co.,Ltd.、7630 Ichibanya Co., Ltd.、9616 共立メンテナンス、3048 ビックカメラ、9237 Emimen Co.,Ltd.、8995 Makoto Construction Co,Ltd、3907 Silicon Studio Corp.
- FAIL_INSEN（118）: 9553 MicroAd, Inc.、2986 LA Holdings Co.,Ltd、6562 Geniee, Inc.、3608 TSI Holdings Co.,Ltd.、1945 Tokyo Energy & Systems Inc.、9006 京浜急行電鉄、6473 JTEKT Corporation、8793 ＮＥＣキャピタルソリューション、4544 H.U.Group Holdings, Inc.、8095 Astena Holdings Co.,Ltd.、4507 Shionogi & Co., Ltd.、3741 Systems Engineering Consultants Co., Ltd.、5838 Rakuten Bank, Ltd.、7270 Subaru Corporation、4763 クリーク・アンド・リバー社、7199 Premium Group Co., Ltd.、6196 Strike Group Co. Ltd.、1968 Taihei Dengyo Kaisha, Ltd.、3562 No.1 Co., Ltd.、9048 名古屋鉄道、2331 ALSOK CO., LTD.、9828 Genki Global Dining Concepts Corp、3479 ティーケーピー、6454 Max Co., Ltd.、2288 Marudai Food Co., Ltd.、6988 日東電工、6371 Tsubakimoto Chain Co.、8850 スターツコーポレーション、3433 TOCALO Co., Ltd.、8927 Meiho Enterprise Co., Ltd.、186A Astroscale Holdings Inc.、7181 JAPAN POST INSURANCE Co., Ltd.、2002 日清製粉グループ本社、6208 Ishikawa Seisakusho,Ltd.、1377 Sakata Seed Corporation、5071 VIS Co., Ltd.、6770 Alps Alpine Co., Ltd.、7981 Takara Standard Co.,Ltd.、8129 TOHO HOLDINGS CO., LTD.、9502 Chubu Electric Power Company,Incorporated、2267 Yakult Honsha Co.,Ltd.、1815 鉄建建設、1969 高砂熱学工業、3452 B-Lot Company Limited、4375 Safie Inc.、8253 Credit Saison Co., Ltd.、8424 芙蓉総合リース、4259 ExaWizards Inc.、2871 ニチレイ、4166 Cacco, Inc.、4937 Ｇ−ＷＡＱＯＯ、3083 Star seeds Co.,Ltd.、5246 ELEMENTS,Inc.、8336 Musashino Bank, Ltd.、8008 Yondoshi Holdings, Inc.、7811 Nakamoto Packs Co. Ltd.、8346 Toho Bank, Ltd.、1879 新日本建設、2767 円谷フィールズホールディングス、4667 Aisan Technology Co., Ltd.、2602 日清オイリオグループ、3994 マネーフォワード、8919 カチタス、7350 Okinawa Financial Group, Inc.、8714 Senshu Ikeda Holdings,Inc.、4475 HENNGE K.K.、3097 Monogatari Corporation、6998 Nippon Tungsten Co., Ltd.、9044 NANKAI Co., Ltd.、7504 Kohsoku Corporation、8876 Relo Group, Inc.、6072 Jibannet Holdings Co., Ltd.、8043 Starzen Company Limited、9505 Hokuriku Electric Power Company、9900 Sagami Holdings Corp.、8097 SAN-AI OBBLI CO. LTD、8059 Daiichi Jitsugyo Co., Ltd.、276A CCReB Advisors Inc.、290A ＳＹＮＳＰＥＣＴＩＶＥ、8343 Akita Bank, Ltd.、8360 Yamanashi Chuo Bank, Ltd.、336A ダイナミックマッププラットフォーム、4478 freee K.K.、6810 Maxell, Ltd.、8367 Nanto Bank Ltd.、8544 Keiyo Bank, Ltd.、6027 弁護士ドットコム、8511 Japan Securities Finance Co., Ltd.、8362 Fukui Bank, Ltd.、4044 Central Glass Co., Ltd.、4765 ＳＢＩグローバルアセットマネジメント、8622 Mito Securities Co., Ltd.、8624 Ichiyoshi Securities Co., Ltd.、8628 松井証券、8707 IwaiCosmo Holdings, Inc.、8708 アイザワ証券グループ、7878 Kohsai Co.Ltd.、1407 West Holdings Corporation、5574 ABEJA,Inc.、2933 KIBUN FOODS INC.、8522 Bank of Nagoya, Ltd.、6952 Casio Computer Co., Ltd.、2354 YE DIGITAL CORPORATION、5889 ＪＡＰＡＮ　ＥＹＥＷＥＡＲ　ＨＯＬＤＩＮＧＳ、4997 日本農薬、4346 NEXYZ.Group Corporation、7354 Direct Marketing MiX Inc.、2681 2nd RETAILING Co., Ltd.、4082 第一稀元素化学工業、3653 Morpho, Inc.、8163 SRS HOLDINGS CO.,LTD.、4691 Washington Hotel Corp.、4543 Terumo Corporation、3563 FOOD & LIFE COMPANIES LTD.、5844 Kyoto Financial Group,Inc.、8381 San-in Godo Bank Ltd.、8399 Bank Of The Ryukyus,Limited、8713 Fidea Holdings Co.Ltd.
### 変化点
- PASS（1）: 4165 PLAID,Inc.
- FAIL_UWAHIGE（6）: 5803 フジクラ、6136 OSG CORP、8151 東陽テクニカ、4382 HEROZ, Inc.、593A ティアフォー、4488 AI inside Inc.
- FAIL_INSEN（18）: 6254 野村マイクロ・サイエンス、4187 大阪有機化学工業、7695 交換できるくん、4419 Ｆｉｎａｔｅｘｔホールディングス、584A LiNKX, Inc.、7318 セレンディップ・ホールディングス、9888 UEX LTD、4368 扶桑化学工業、8697 日本取引所グループ、9343 アイビス、286A EUCALIA Inc.、8704 Traders Holdings Co.,Ltd.、6597 6597、4498 Cybertrust Japan Co., Ltd.、4071 プラスアルファ・コンサルティング、339A PROGRESS TECHNOLOGIES GROUP INC、4011 Headwaters Co.,Ltd、3923 ラクス
### AI特需
- FAIL_UWAHIGE（5）: 2760 東京エレクトロンデバイス、9824 泉州電業、8159 立花エレテック、1982 日比谷総合設備、4658 日本空調サービス
- FAIL_INSEN（6）: 3131 シンデンハイテックス、6227 AIMECHATEC Ltd.、9960 トーテック、8098 稲畑産業、6643 戸上電機製作所、9432 NTT
### 除籍（first_seenから30暦日超・当夜再指名なし）
3993

## 機械詳細
- 抜粋: 通知の通過10件のラウンドロビン（群別 method/ai/granville/changepoint/不明）。ヘッドライン付与 PASS35件中35件（抜粋規則は不適用）
- gate_history: gate_history/2026-10-14.json を新規作成（verdicts 368件・nominations 87件（新規20・再指名67））
- grades.json: 841銘柄／407765バイト（業種PER中央値 23業種）
- method_score: 保持55件／null313件
- kabutan トップ新規取得 50銘柄（上限50・打ち切り: 残り枠いっぱい）／財務ページ 19銘柄（配当情報）／決算日程ページ: 次回決算日は kabutan に記載なく gyoseki_cache 既存値を使用
- profile_cache 総数820・本夜追加/更新 業態・業種付与45件新規＋業種埋め戻し5件
- earnings_log 総数48／本夜追記10件／リターン補完5件／日足なしで未補完26件
- gyoseki_cache: 再計算1銘柄（決算発表: 9560）、history 退避1件
- pool_bars.json: 368銘柄／323607バイト
- 鮮度ゲート: 鮮度切れ除外6件・nom_age分布 0-2:165/3-10:125/11+:78・last_seen欠損0件
- 記録の凍結: verdicts 368件＝評価368件、業種 付与済み368／未付与0
- トレンド文脈: ctx 合致72／不一致135／レンジ155／判定不能6・PASS のうち ctx 合致8件・形態が付いた銘柄140件
- 3日ルール: 判定4銘柄（詳細は通知）
- 業種別PER中央値: 算出23業種
- 開示の分類別件数: 📢0/📉0/📊10/🔁0/👥0/🏛0/📦0/📌25
- 熟成由来の候補 0件
- 権利情報: rights_cache 総数187・本夜 配当年間予想の新規9件／優待取得0件（minkabu は未取得・優待は null=不明）／決算ページから取れず不明のまま10件
- STEP 4.8: スキップ（week_open=false）
- master.json の変更行数: +8392/-8281（indent=2）
