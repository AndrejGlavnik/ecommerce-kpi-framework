# eCommerce KPI Dictionary

| KPI | Definition | Formula | Grain | QA notes |
|---|---|---|---|---|
| Sessions | Website sessions in reporting period. | Sum sessions | Date, country, brand | Check missing dates and source platform definitions. |
| Buy-now clicks | Clicks on retailer/buy-now CTAs. | Sum buy_now_clicks | Date, country, brand | Confirm page types and CTA implementation. |
| Orders | Completed orders attributed to reporting source. | Sum orders | Date, country, brand | Confirm cancellation/return handling. |
| Revenue | Order revenue in reporting currency. | Sum revenue | Date, country, brand | Confirm currency and tax rules. |
| Conversion rate | Share of sessions that become orders. | orders / sessions | Date or period | Avoid averaging daily CVR without weighting. |
| Average order value | Revenue per order. | revenue / orders | Period | Guard against division by zero. |
| Repeat buyer rate | Repeat buyers as share of users. | repeat_buyers / users | Period | Confirm user identity rules. |
| Retailer sales | Units and revenue reported by retailers. | Sum units/revenue | Date, country, brand, retailer | Confirm retailer file timing and returns logic. |
| CPC | Cost per media click. | spend / clicks | Date, country, brand, channel | Guard against zero clicks. |
| CTR | Click-through rate. | clicks / impressions | Date, country, brand, channel | Confirm impression source. |
