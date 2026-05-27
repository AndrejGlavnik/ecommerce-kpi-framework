from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ecommerce_kpi_framework.kpis import build_summary, render_markdown


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a sample eCommerce KPI report.")
    parser.add_argument("--web", required=True, help="Web sessions CSV.")
    parser.add_argument("--retailer", required=True, help="Retailer sales CSV.")
    parser.add_argument("--media", required=True, help="Media spend CSV.")
    parser.add_argument("--out", default="reports/kpi_report.md", help="Markdown output path.")
    args = parser.parse_args()

    summary = build_summary(pd.read_csv(args.web), pd.read_csv(args.retailer), pd.read_csv(args.media))
    report = render_markdown(summary)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(report, encoding="utf-8")
    print(f"Wrote {out}.")


if __name__ == "__main__":
    main()
