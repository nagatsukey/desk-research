## ディレクトリ構成

### ルート

```
desk-research/
├── CLAUDE.md                    # このファイル
├── README.md
├── _config.yml                  # Jekyll の設定
├── index.md                     # トップページ（分析一覧）
└── analyses/                    # 調査レポート置き場
```

### analyses

調査レポートは `analyses/[調査分類]/[サブ分類]/[調査レポートタイトル]/[調査レポートタイトル].md` に配置する。

```
analyses/
├── sample-analysis.md                       # 表示確認用のサンプル記事
├── industry-research/                       # 調査分類: 業界調査
│   ├── food-service/                        # サブ分類: 飲食業界
│   │   └── delivery-market-trends/          # 調査レポートタイトル
│   │       └── delivery-market-trends.md
│   ├── fitness/                             # サブ分類: フィットネス業界
│   │   └── gym-subscription-pricing/
│   │       └── gym-subscription-pricing.md
│   └── gaming/                              # サブ分類: ゲーム業界
│       └── indie-game-funding/
│           └── indie-game-funding.md
├── engineering/                             # 調査分類: エンジニアリング
│   ├── ai-agent/                            # サブ分類: AIエージェント
│   │   └── mcp-server-ecosystem/
│   │       └── mcp-server-ecosystem.md
│   └── web-frontend/                        # サブ分類: Webフロントエンド
│       └── react-state-management/
│           └── react-state-management.md
└── exercise/                                # 調査分類: 運動
    └── running/                             # サブ分類: ランニング
        └── marathon-training-methods/
            └── marathon-training-methods.md
```
