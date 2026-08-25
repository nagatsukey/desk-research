#!/usr/bin/env python3
"""生活定点「好きなお酒」(q434群) と「最も好きなお酒」(q445群) の
インラインHighchartsデータをローカル保存済みHTMLから抽出してCSV化する。"""
import re
import csv
import pathlib

OUT_DIR = pathlib.Path(__file__).parent
QUESTIONS = {
    "好きなお酒(複数回答)": {
        434: "ビール・発泡酒・その他のビール系飲料",
        435: "ウィスキー",
        436: "ブランデー",
        437: "ワイン",
        438: "日本酒",
        439: "焼酎",
        440: "チューハイ・サワー",
        441: "カクテル",
        442: "梅酒",
        443: "ハイボール",
    },
    "最も好きなお酒(単一回答)": {
        445: "ビール・発泡酒・その他のビール系飲料",
        446: "ウィスキー",
        447: "ブランデー",
        448: "ワイン",
        449: "日本酒",
        450: "焼酎",
        451: "チューハイ・サワー",
        452: "カクテル",
        453: "梅酒",
        454: "ハイボール",
        455: "その他",
    },
}
YEARS = [1992 + 2 * i for i in range(17)]  # 1992..2024 隔年17点

rows = []
for question, choices in QUESTIONS.items():
    for aid, choice in choices.items():
        html = (OUT_DIR / f"answer_{aid}.html").read_text(encoding="utf-8", errors="replace")
        m = re.search(r"mainStGraph = new Highcharts\.Chart.*?(?=compareGraph|</script>)", html, re.S)
        block = m.group(0) if m else html
        for sm in re.finditer(r'addSeries\(\{\s*name:\s*"([^"]*)".*?data:\s*\[([^\]]*)\]', block, re.S):
            name = sm.group(1).strip()
            if name == "全体":
                view = "全体"
            elif name in ("男性", "女性"):
                view = "男女別"
            elif re.fullmatch(r"男性\d0代", name):
                view = "年代別(男性)"
            elif re.fullmatch(r"女性\d0代", name):
                view = "年代別(女性)"
            elif re.fullmatch(r"\d0代", name):
                view = "年代別"
            elif name in ("首都圏", "阪神圏"):
                view = "地域別"
            else:
                view = "その他ビュー"
            vals = [v.strip() for v in sm.group(2).split(",")]
            for year, v in zip(YEARS, vals):
                value = None if v == "null" else float(v)
                rows.append({
                    "question": question,
                    "choice": choice,
                    "view": view,
                    "segment": name,
                    "year": year,
                    "value": value,
                })

out = OUT_DIR / "seikatsu_teiten_sake.csv"
with out.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["question", "choice", "view", "segment", "year", "value"])
    w.writeheader()
    for r in rows:
        w.writerow(r)
print(f"rows={len(rows)} -> {out}")
