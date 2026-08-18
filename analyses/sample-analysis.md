---
layout: default
title: GitHub Pages 表示テスト
---

# GitHub Pages 表示テスト

これは GitHub Pages が正しく動作するかを確認するためのサンプル記事です。
Markdown の主要な記法が意図どおりレンダリングされるかを確認します。

## 見出しと段落

Markdown ファイルを `main` ブランチに push すると、Jekyll が自動で HTML に変換して公開します。
**太字**、*斜体*、`インラインコード` も使えます。

## リスト

- 箇条書きの項目
- ネストも可能
  - 子の項目
1. 番号付きリスト
2. 二番目の項目

## 表

| 項目 | 内容 | 備考 |
| --- | --- | --- |
| ソース | `main` ブランチ / ルート | ブランチソース方式 |
| 変換 | Jekyll | Markdown → HTML |
| テーマ | jekyll-theme-primer | GitHub 標準テーマ |

## コードブロック

```python
def hello(name: str) -> str:
    return f"Hello, {name}!"


print(hello("desk-research"))
```

## 引用

> 分析結果はMarkdownで書き、リポジトリにpushするだけで公開できます。

---

[← 一覧に戻る]({{ '/' | relative_url }})
