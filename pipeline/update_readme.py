"""Rewrite the stat blocks in README.md from data/index.json.

Hand-written counts in a README rot the moment the pipeline runs again (this repo
shipped a README claiming 924 threads while data/ held 1,285). Every number a reader
can check is generated here instead, between <!-- STATS:X --> markers.

Usage: python -m pipeline.update_readme [data_dir] [readme_path]
"""
import json
import os
import re
import sys

MARKERS = ("HERO", "BADGES", "TABLE", "QUALITY")


def _block(name, body):
    return f"<!-- STATS:{name} -->\n{body}\n<!-- /STATS:{name} -->"


def render(index, manuals_count):
    total = index["total"]
    by_year = index["by_year"]
    q = index["by_quality"]
    years = sorted(y for y in by_year if y != "undated")

    hero = (
        f"> {total:,} IRCC answers to licensed immigration representatives, "
        f"{manuals_count} internal officer\n"
        "> manuals, and every ATIP release behind them. Parsed, structured, free."
    )

    coverage = f"{years[0]}--{years[-1]}" if years else "n/a"
    badges = "\n".join([
        f"![threads](https://img.shields.io/badge/threads-{total:,}-blue)",
        f"![manuals](https://img.shields.io/badge/manuals-{manuals_count}-blue)",
        f"![coverage](https://img.shields.io/badge/coverage-{coverage}-blue)",
        "![data](https://img.shields.io/badge/data-OGL--Canada-green)",
        "![code](https://img.shields.io/badge/code-MIT-green)",
        f"![updated](https://img.shields.io/badge/updated-{index['generated'].replace('-', '--')}-lightgrey)",
    ])

    rows = [f"| [`data/{y}.json`](data/{y}.json) | Mailbox threads, {y} | {by_year[y]:,} |" for y in years]
    if "undated" in by_year:
        rows.append(
            f"| [`data/undated.json`](data/undated.json) | Threads with no parseable date "
            f"| {by_year['undated']:,} |"
        )
    rows += [
        "| [`data/index.json`](data/index.json) | Counts by year, quality, ATIP release | — |",
        f"| [`manuals/`](manuals/) | OCR text of {manuals_count} internal IRCC documents | — |",
        "| [Releases](../../releases) | Raw ATIP PDFs, as IRCC delivered them | — |",
    ]
    table = "| File | Contents | Threads |\n|---|---|---|\n" + "\n".join(rows)

    quality = (
        f"`quality` is the field to read first: `answered` ({q.get('answered', 0):,}) substantive reply ·\n"
        f"`deflected` ({q.get('deflected', 0):,}) boilerplate refusal or redirect · "
        f"`partial` ({q.get('partial', 0):,}) OCR-torn or empty."
    )
    return {"HERO": hero, "BADGES": badges, "TABLE": table, "QUALITY": quality}


def update(readme_path, blocks):
    text = open(readme_path, encoding="utf-8").read()
    missing = [n for n in MARKERS if f"<!-- STATS:{n} -->" not in text]
    if missing:
        raise SystemExit(f"README is missing stat markers: {', '.join(missing)}")
    for name, body in blocks.items():
        pattern = re.compile(
            rf"<!-- STATS:{name} -->.*?<!-- /STATS:{name} -->", re.S
        )
        text = pattern.sub(lambda _m: _block(name, body), text, count=1)
    open(readme_path, "w", encoding="utf-8").write(text)
    return text


def main(argv):
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = argv[1] if len(argv) > 1 else os.path.join(root, "data")
    readme = argv[2] if len(argv) > 2 else os.path.join(root, "README.md")
    index = json.load(open(os.path.join(data_dir, "index.json"), encoding="utf-8"))
    manuals_dir = os.path.join(root, "manuals")
    manuals = len([f for f in os.listdir(manuals_dir) if f.endswith(".md") and f != "README.md"]) if os.path.isdir(manuals_dir) else 0
    update(readme, render(index, manuals))
    print(f"README updated: {index['total']:,} threads, {manuals} manuals")


if __name__ == "__main__":
    main(sys.argv)
