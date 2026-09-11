---
name: variance-review
description: Review the supplied fictional restaurant budget-versus-actual CSV using JSON settings, a bundled Python calculator, and documented business drivers. Use for this practice variance review or its threshold comparison.
---

# Practice variance review

Read [context](references/review-context.md) and the requested policy: [original](references/policy.json) or [higher thresholds](references/policy-higher-thresholds.json). The supplied [CSV](assets/location-pnl.csv) is a fictional June 2026 fixture for Harbor Table Restaurants. Use it when the user requests this practice example. Do not treat it as current workbook data.

For execution, run [review_variances.py](scripts/review_variances.py) with the requested CSV and full policy paths in an available authorized Python environment. From this skill folder:

```text
python scripts/review_variances.py assets/location-pnl.csv references/policy.json
```

For the second policy, substitute `references/policy-higher-thresholds.json`. The script prints JSON; it does not save files, edit a workbook, or write commentary. Record the actual command, input, policy, and observed result. Stop on validation or control errors and report them. If execution is unavailable, state “Script execution unavailable in this session” and offer the command for the user to run. Never label a calculation or supplied expected result as an executed script.

Use the returned material rows in their existing order. Match each driver by location, category, type, and period to the context reference. Use “driver not documented” when no explanation is supplied. Follow the reference's length and rounding rules. Return a table with Location, Category, Period, Type, Variance, Variance %, Direction, and Comment, followed by separate revenue and expense totals and the two-sentence partial operating summary. The partial result is not net income. Keep all valid rows in reconciliation totals even when nonmaterial rows are excluded from commentary.

When comparing policies, retain both results and identify added or removed material rows. Do not change input data or overwrite either policy unless requested. Materiality uses strict greater-than with OR, implemented in Python. For zero budget only the dollar test applies. JSON supplies the thresholds and expected totals; it does not implement the comparison logic itself.

For another period or company, obtain matching data, context, and independently established controls first. The fixture does not establish facts about real business data. Do not infer authorization for workbook edits or external publishing from this skill.
