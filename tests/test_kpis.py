import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ecommerce_kpi_framework.kpis import build_summary, safe_divide


def test_safe_divide_returns_zero_for_zero_denominator():
    assert safe_divide(10, 0) == 0


def test_build_summary_uses_weighted_period_formulas():
    web = pd.read_csv(ROOT / "data" / "web_sessions.csv")
    retailer = pd.read_csv(ROOT / "data" / "retailer_sales.csv")
    media = pd.read_csv(ROOT / "data" / "media_spend.csv")
    summary = build_summary(web, retailer, media)
    assert summary.conversion_rate == summary.orders / summary.sessions
    assert summary.average_order_value == summary.revenue / summary.orders
    assert summary.retailer_units == 178
