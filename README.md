# asset_operation

半自動投資システムの運用リポジトリ（**公開**）。`master.json` が唯一の正（Single Source of Truth）。
夜間ルーティン（Claude Code）が PR 方式で記録を蓄積し、GitHub Pages が候補ボード等を配信する。

公開ページ: https://kohshi529-glitch.github.io/asset_operation/

## 構成（リポジトリ直下・`docs/` は使わない）

```
master.json                 ← 唯一の正。scoring_spec / market / candidates / watchlist / changepoint_watch /
                               night_gate / gyoseki_* / valuation_* / profile_cache / granville_spec / stf_log /
                               ipo / catalyst_schedule / pipeline / system_status …
board.html                  ← 📋 候補ボード（🚪ゲート／👀ウォッチ／🔔変化点／📋5手法／📐グランビル／📖凡例）
gate_history.html           ← 🕒 ゲート履歴（gate_history/{base_day}.json を閲覧）
index.html                  ← 📊 スコアリング基準（scoring_spec の閲覧用・render_master.py で生成）
system.html                 ← 🖥 システム（system_status の3層実行体制マップ・build_system_html.py で生成）
setup_guide.html            ← 🛠 設定要領（ルーティン・正典・PJ・ボード・派生ファイルの運用手引き）
market_today.json           ← ⑤ が毎朝書く当日の市場モード（派生ファイル）
grades.json                 ← ①-8 が毎晩書く業績/値頃グレードの射影（派生ファイル）
night_gate_today.json       ← ①-8 の当夜の提案（派生ファイル）
pool_bars.json              ← ①-8 が書く候補プールの直近20本の日足（派生ファイル・毎晩全取り直し）
corporate_actions_paste.json ← 分割・併合・消却・増資・社名/コード変更・上場廃止・決算期変更の受け箱（人が書く・①-9 が読む）
gate_history/{date}.json    ← ①-8 の夜ごとの記録（不変・nominations / verdicts 同居）
gate_track.json             ← ①-11 の仮想約定/決済・R 集計
surge_log.json              ← ①-10 の急騰未検出ログ（週次）
method_cards.md             ← 5大手法カード（旧・手法別スクリーニングPJ用）
render_master.py            ← master.json → index.html
build_system_html.py        ← master.json.system_status → system.html
```

## 日足の取得方式（データ整合・2026-11-26 明記）
- **全ルーティンが毎晩「全取り直し」**で、増分追記は使わない。①-8 発注前ゲートはプール全銘柄の 1 年日足を毎晩取り直し、pool_bars.json にはその直近 20 本だけを書く（派生ファイル・前夜分に足さない）。①-S3／S4／S5／S6／S7 の各スキャンも毎晩 6 か月〜1 年分を取り直し、日足そのものは保存しない（status に指標だけ）。①-9 銘柄評価更新は 1 年日足を毎回取り直す（保存しない）
- 日足の出所は Yahoo（yfinance 標準作法）。Yahoo は株式分割・併合を**遡及調整済み**の価格で返すので、25 日線・52 週高安・ドローダウンは分割日をまたいでも連続する。したがって「分割検知時の履歴の全取り直し」は不要（毎晩全取り直しで、調整済みの系列が毎回入る）
- 分割・併合で壊れるのは**キャッシュした静的層**（1 株益・BPS・発行済株式数＝kabutan 取得時点の値）だけ。①-9 v5.7 以降は Yahoo の Stock Splits と受け箱（corporate_actions_paste.json）で検知して強制再取得し、整合するまで PER／PBR／PSR／PEG を null＋⚠分割未整合 にする。v5.7.1 以降は自前時価総額（終値×発行済株式数）と Yahoo の時価総額を照合し、±30% 超は ⚠時価総額不整合（分割・併合・消却・増資・株数誤りを一括で捕まえる）
- 取得日は valuation_cache[code].static.fetched_at（静的層）と calculated_at（値頃感の計算日）。候補ボードはこれを「取得 MM/DD」で常時表示し、60 営業日超は 🕰、直近決算日より古ければ 📅未更新

## 公開範囲と鉄則

- このリポジトリと GitHub Pages は **公開**。ウォッチ・候補・採点基準・ゲート記録までは公開情報として扱う。
- **ポジション・戦績・口座・API鍵は絶対にコミットしない**。取引実データの唯一の正は Google Drive「SBI」フォルダの `trade_master`（週次総取引同期だけが書く）。実弾ボード（戦績／ポジション）も Drive にのみ置く。
- `master.json` の **丸ごと手動コミットは恒久禁止**。記録の変更はルーティンの PR か、対象キーだけを書き換えるメンテナンスPR（最新 clone → 対象キーのみ → プログラム検証 → PR）で行う。
- `main` への直接 push・直接コミットはしない（PR 方式のみ）。各ルーティンは指定キー以外1バイトも変更せず、既存の indent を検出して書き出す。

## 読み取り経路

**`raw.githubusercontent.com` は全読み取り経路で使用禁止**（2026-07-21 に約2日前のキャッシュを返して誤警報を起こした）。
セッション・PJ・ボードは次のどちらかで読む。

```
https://kohshi529-glitch.github.io/asset_operation/master.json        （Pages・ライブ表示用）
https://kohshi529-glitch.github.io/asset_operation/market_today.json  （当日の市場モード）
https://kohshi529-glitch.github.io/asset_operation/grades.json         （業績/値頃グレード）
https://kohshi529-glitch.github.io/asset_operation/night_gate_today.json
git clone https://github.com/kohshi529-glitch/asset_operation          （ルーティン・検証用。状態の検証は clone + git log で行う）
```

Pages への反映はマージから数分遅れることがある。

## 実行体制（詳細は system.html）

| 層 | 担当 | 例 |
|---|---|---|
| L1 | Claude Code ルーティン（無人・PR 方式） | ⑤ 06:30 ／ ①-S1・①-S2 18:00 ／ ①-7 19:15 ／ ①-8 20:30 ／ ①-12 21:30 ／ ①-9 水土 09:00 ／ ①-10・①-11・①-5 土曜 ／ ①-4 日曜 |
| L2 | Cowork（PJ・スケジュールタスク） | 週次総取引同期（土 06:30）／ 銘柄かんたん解説PJ ／ ポジション株PJ ／ 戦績ボードPJ |
| L3 | 対話セッション | 場中のライブ判断・仕様改訂・正典登録・ボード改修 |

タスクプロンプト・PJ 指示の正典は Drive「SBI」の `pcanon_{slug}_{YYYYMMDD_HHMM}.md`（最新 = modifiedTime）。このリポジトリにはプロンプト本文を置かない。

## 更新のしかた

- **記録（candidates 等）**: ルーティンが毎晩 PR を作る → 翌朝マージ。
- **採点基準（scoring_spec）・タスクマップ（system_status）・仕様キー**: メンテナンスPR で対象キーだけを書き換え → マージ後に `python3 render_master.py`（index.html）／`python3 build_system_html.py`（system.html）で再生成してコミット。
- **ボード等の静的 HTML**: 対話セッションがファイルを納品 → 手動コミット。

## GitHub Pages

Settings → Pages → Deploy from a branch → Branch `main` / Folder `/ (root)`。
