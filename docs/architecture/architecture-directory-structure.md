# analysesのディレクトリ構成

調査レポートは `analyses/[調査分類]/[サブ分類]/[調査レポートタイトル]/[調査レポートタイトル].md` に配置する。
`/[調査レポートタイトル]/assets/`には、調査に使用したファイルを配置し、そこに配置するファイルは必ず`/[調査レポートタイトル]/assets/README.md`に詳細をメモする。

以下は命名規則を示すための例であり、実在するディレクトリの一覧ではない。

```
analyses/
├── industry-research/                       # 調査分類: 業界調査
│   ├── food-service/                        # サブ分類: 飲食業界
│   │   └── delivery-market-trends/          # 調査レポートタイトル
│   │       ├── delivery-market-trends.md
│   │       └── assets/                      # 調査に使用したファイル（無い調査では作らない）
│   │           ├── README.md                # assets 内の全ファイルの詳細をメモする
│   │           └── mlit-delivery-stats.xlsx
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
