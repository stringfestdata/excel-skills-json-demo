# Practice prompts

Use after making the complete `variance-review` folder accessible in an assistant environment that supports skills. These prompts use the supplied fictional CSV, not an active workbook.

## 1. Inspect the settings

> Read the variance-review skill and its reference files. Explain how policy.json is used by review_variances.py. Show the dollar and percentage thresholds and the comparison rule. Do not run the script yet. Distinguish values read from JSON from behavior implemented in Python.

## 2. Run the original policy

> Use the variance-review skill with the supplied practice file assets/location-pnl.csv and references/policy.json for Harbor Table Restaurants, June 2026. Run scripts/review_variances.py if Python execution is available. Report the material-row count, the thresholds used, and whether the control totals reconcile. Then write commentary using references/review-context.md. Identify the actual input and policy files used. If you cannot execute the script, say so and do not present an expected result as an executed result.

## 3. Run the higher thresholds

> Run the same supplied practice CSV through the same script using references/policy-higher-thresholds.json. Compare this executed result with the original policy run. Report the new material-row count and identify the rows that are no longer material. Keep the original results available for comparison. If execution is unavailable, say so.

## 4. Explain the difference

> Using the two executed outputs, explain why Navy Yard Beverage revenue and Capitol Hill Food expense stop qualifying, while Old Town Catering revenue still qualifies. Show the dollar and percentage tests separately. Confirm whether the underlying reconciliation totals changed. Don't invent business explanations.
