# asset_operation

5大手法スコアリングの運用リポジトリ（公開）。`master.json` が唯一の正（Single Source of Truth）。

## 構成

```
master.json                 ← 唯一の正。scoring_spec（採点基準）＋ candidates ＋ market
method_cards.md             ← 手法別カード5枚（各Coworkセッションの「指示を追加」欄に貼る）
docs/index.html            ← 公開ページ（master.json から自動生成）
docs/setup_guide.html      ← 設定要領
scripts/render_master.py   ← master.json → docs/index.html を再生成
```

## 公開範囲と鉄則

- このリポジトリは **公開**。GitHub Pages のサイトも公開される。
- **秘密（保有・建玉・口座・API鍵）は絶対にコミットしない**。`positions.json` 等は `.gitignore` で除外済み。
- 公開してよいのは「手法・採点基準・候補リスト」まで。

## セッションからの読み取り

各手法カードの【データ源】を、この raw URL に向ける（`kohshi529-glitch` は自分のIDに置換）：

```
https://raw.githubusercontent.com/kohshi529-glitch/asset_operation/main/master.json
```

## GitHub Pages を有効化

Settings → Pages → Deploy from a branch → Branch `main` / Folder `/docs` → Save。
数分後 `https://kohshi529-glitch.github.io/asset_operation/` で公開ページが見られる。

## 更新のしかた

1. `master.json` を編集（採点基準の調整・候補の追加など）。
2. `python3 scripts/render_master.py` で `docs/index.html` を再生成。
3. commit / push。履歴・差分・巻き戻し（revert）が残る。

基準の変更はここ（master.json）でだけ行う。5枚のカードは触らない。
