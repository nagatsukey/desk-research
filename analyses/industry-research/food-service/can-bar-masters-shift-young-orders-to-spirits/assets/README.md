# assets の内容

## seikatsu-teiten-sake-by-age.csv

出典：**博報堂生活総合研究所「生活定点」調査**（https://seikatsusoken.jp/teiten/）

- 質問「好きなお酒は何ですか？［飲酒者のみ・複数回答］」（選択肢ページ answer/434〜443）と「最も好きなお酒は何ですか？［飲酒者のみ・単一回答］」（answer/445〜455）の公表値を、各選択肢ページから転記して1つのCSVにまとめたもの（取得日：2026-08-25）
- 列：question（質問）／choice（選択肢）／view（全体・男女別・年代別・年代別(男性)・年代別(女性)・地域別）／segment（セグメント名）／year（1992〜2024の隔年）／value（%、その年に設問・選択肢が存在しない場合は空）
- **この質問の実測値は2016年以降のみ**（調査自体は1992年開始だが、この設問は2016年に追加されたため、1992〜2014年は全選択肢が空値）
- 調査概要：訪問留置法、首都40km圏＋阪神30km圏の20〜69歳男女、性年代5歳刻みの人口構成比割付、2024年は n=2,510。隔年（偶数年）実施
- 母数は「飲酒者のみ」である点に注意（非飲酒者を含む全体ではない）

### 利用条件（出典サイトの規約より）

- 引用時は【博報堂生活総合研究所「生活定点」調査】の出典明記が必要
- コンテンツの改変利用・AI学習利用は禁止と明記されている。本CSVは公表数値の転記（引用）であり、数値の加工・改変はしていない

## PDF資料（取得日：2026-08-25）

- **nba-cocktail-ranking-2026.pdf**——日本バーテンダー協会「N.B.A.カクテル・ランキング2026」プレスリリース（2026-05-12公表）。取得元：https://www.bartender.or.jp/pdf/cocktailranking.pdf
- **jfc-drinking-out-survey-2025.pdf**——日本政策金融公庫「飲酒を伴う外食に関する消費者調査結果」（2025年8月調査、2025-11-13公表）。取得元：https://www.jfc.go.jp/n/findings/pdf/seikatsu25_1113a.pdf
- **hotpepper-lemonsour-2017.pdf**——ホットペッパーグルメ外食総研「レモンサワーは誰に人気！？」（外食市場調査2017年5月分、2017-08-03公表）。取得元：https://www.hotpepper.jp/ggs/wp-content/uploads/2017/08/59380e10f15eff7dc6f43c1503c19ce1.pdf
- **mhlw-shakogyo-manual.pdf**——厚生労働省委託事業「ウィズコロナ、ポストコロナ時代の生産性向上に向けた取組みのヒント 社交業編」。取得元：https://www.mhlw.go.jp/content/001297216.pdf

## parse_teiten.py

上記CSVの作成に使ったスクリプト。各選択肢ページ（例：https://seikatsusoken.jp/teiten/answer/435.html）のHTMLに埋め込まれたグラフ描画用データから公表値を転記する。再現手順：

1. answer/434〜443, 445〜455 の各HTMLを `answer_<id>.html` としてこのスクリプトと同じディレクトリに保存（`curl -o answer_435.html https://seikatsusoken.jp/teiten/answer/435.html` など、サーバーに負荷をかけない間隔で）
2. `python3 parse_teiten.py` を実行すると `seikatsu_teiten_sake.csv` が生成される
