# June 2026 review context

Fictional teaching example for Harbor Table Restaurants. Only the listed revenue and expense categories are included. This is a partial operating review, not a complete P&L.

## Documented drivers

Use a driver only when location, category, type and period match exactly.

| Location | Category | Type | Period | Documented driver |
| --- | --- | --- | --- | --- |
| Navy Yard | Sushi | Revenue | 2026-06 | Reduced sushi service during a kitchen repair lowered sales. |
| Capitol Hill | Dining | Revenue | 2026-06 | Additional private dining bookings increased sales. |
| Old Town | Catering | Revenue | 2026-06 | A corporate client canceled its June catering event. |
| Navy Yard | Beverage | Revenue | 2026-06 | No driver was supplied. |
| Old Town | Beverage | Revenue | 2026-06 | An expanded patio schedule increased beverage sales. |
| Navy Yard | Labor | Expense | 2026-06 | Overtime during the kitchen repair increased labor cost. |
| Capitol Hill | Food | Expense | 2026-06 | A negotiated supplier discount reduced food cost. |
| Bethesda | Food | Expense | 2026-06 | No driver was supplied. |

## Reporting rules

Read numerical thresholds and independent control totals from policy.json. A row is material if absolute actual-minus-budget exceeds the dollar threshold OR absolute variance divided by budget exceeds the percent threshold. Equality does not pass. Test unrounded values. When budget is zero, percentage is undefined and only the dollar test applies.

For revenue, positive variance is favorable. For expenses, negative variance is favorable. Keep the raw actual-minus-budget variance and label its direction separately. Never add revenue and expenses into one sales total.

Order material rows from largest unfavorable profit impact to smallest, then largest favorable profit impact to smallest. Break ties by location and category. Explain documented drivers before numbers. Use "driver not documented" when no explanation is supplied. Do not infer a cause from the numbers or reuse another row's explanation.

Keep each comment under 40 words. Round displayed dollars to the nearest hundred and percentages to one decimal place. Preserve location and category names. Close with two sentences describing the partial operating review overall. Keep nonmaterial rows out of the commentary, but include all valid rows in reconciliation totals.
