from __future__ import annotations

from dataclasses import dataclass

import pandas as pd


@dataclass
class KpiSummary:
    sessions: int
    buy_now_clicks: int
    orders: int
    revenue: float
    conversion_rate: float
    average_order_value: float
    repeat_buyer_rate: float
    retailer_units: int
    retailer_revenue: float
    media_spend: float
    cpc: float
    ctr: float


def safe_divide(numerator: float, denominator: float) -> float:
    if denominator == 0:
        return 0.0
    return numerator / denominator


def build_summary(web: pd.DataFrame, retailer: pd.DataFrame, media: pd.DataFrame) -> KpiSummary:
    sessions = int(web["sessions"].sum())
    buy_now_clicks = int(web["buy_now_clicks"].sum())
    orders = int(web["orders"].sum())
    revenue = float(web["revenue"].sum())
    users = float(web["users"].sum())
    repeat_buyers = float(web["repeat_buyers"].sum())
    retailer_units = int(retailer["units_sold"].sum())
    retailer_revenue = float(retailer["retailer_revenue"].sum())
    media_spend = float(media["spend"].sum())
    clicks = float(media["clicks"].sum())
    impressions = float(media["impressions"].sum())

    return KpiSummary(
        sessions=sessions,
        buy_now_clicks=buy_now_clicks,
        orders=orders,
        revenue=revenue,
        conversion_rate=safe_divide(orders, sessions),
        average_order_value=safe_divide(revenue, orders),
        repeat_buyer_rate=safe_divide(repeat_buyers, users),
        retailer_units=retailer_units,
        retailer_revenue=retailer_revenue,
        media_spend=media_spend,
        cpc=safe_divide(media_spend, clicks),
        ctr=safe_divide(clicks, impressions),
    )


def render_markdown(summary: KpiSummary) -> str:
    rows = [
        ("Sessions", f"{summary.sessions:,}", "Sum of website sessions"),
        ("Buy-now clicks", f"{summary.buy_now_clicks:,}", "Retailer CTA engagement"),
        ("Orders", f"{summary.orders:,}", "Completed orders"),
        ("Revenue", f"{summary.revenue:,.2f}", "Web/order revenue"),
        ("Conversion rate", f"{summary.conversion_rate:.2%}", "Orders divided by sessions"),
        ("Average order value", f"{summary.average_order_value:,.2f}", "Revenue divided by orders"),
        ("Repeat buyer rate", f"{summary.repeat_buyer_rate:.2%}", "Repeat buyers divided by users"),
        ("Retailer units", f"{summary.retailer_units:,}", "Units sold from retailer export"),
        ("Retailer revenue", f"{summary.retailer_revenue:,.2f}", "Retailer reported revenue"),
        ("Media spend", f"{summary.media_spend:,.2f}", "Total paid media spend"),
        ("CPC", f"{summary.cpc:.2f}", "Spend divided by clicks"),
        ("CTR", f"{summary.ctr:.2%}", "Clicks divided by impressions"),
    ]
    lines = [
        "# eCommerce KPI Report",
        "",
        "| KPI | Value | Definition |",
        "|---|---:|---|",
    ]
    for name, value, definition in rows:
        lines.append(f"| {name} | {value} | {definition} |")
    lines.extend(
        [
            "",
            "## QA notes",
            "",
            "- Conversion rate and average order value are weighted period calculations, not averages of daily percentages.",
            "- Retailer sales may not match web orders if timing, attribution or return handling differs.",
            "- Buy-now clicks require consistent CTA tracking across page types.",
        ]
    )
    return "\n".join(lines) + "\n"
