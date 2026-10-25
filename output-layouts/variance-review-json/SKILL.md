---
name: variance-review-json
description: Create a budget-versus-actual review in Excel using the source table, JSON policy and a selected JSON layout. Use for a repeatable variance report or a compact manager view.
---

# JSON-controlled variance review

## Files and precedence
- Read references/policy.json unless the user explicitly selects references/policy-higher-thresholds.json.
- Read references/review-layout.json unless the user explicitly selects references/manager-layout.json.
- Read references/review-context.md for documented business drivers.
- Treat the selected JSON files as configuration for these instructions. Keys are conventions for THIS skill, not a built-in Excel API or a formal JSON Schema. If you cannot read a required file, stop and name it. Do not silently substitute defaults.
- A prompt may select a supplied file. Do not rewrite the policy or layout unless explicitly requested.

## 1. Identify and check the source
Use tblLocationPnL on the Data worksheet of the active practice workbook. Read the actual table, not saved examples or results. Required columns are Location, Category, Period, Type, Budget, Actual; there must be 12 detail rows for this supplied exercise. Do not edit the source or the reference files.
Require nonblank identifiers, one period matching the policy, Type of Revenue or Expense, unique Location/Category/Period/Type combinations, and nonnegative finite Budget and Actual values. Do not include subtotal rows. Check separate revenue and expense budget/actual totals against the four policy controls. Stop on mismatch; do not change controls to make the data pass. Controls apply only to this fictional dataset.

## 2. Calculate with auditable Excel formulas
Create or reuse a Calculations sheet for all 12 rows. Link inputs to the source table and use formulas for:
- Variance = Actual - Budget.
- VariancePercent = Variance / Budget. For zero budget, leave the percentage blank and label it undefined; do not turn it into zero.
- ProfitImpact = Variance for Revenue, and -Variance for Expense.
- Direction = Favorable if ProfitImpact > 0, Unfavorable if < 0, otherwise On plan.
- Material = ABS(Variance) > dollar_threshold OR (Budget > 0 AND ABS(Variance) > percent_threshold * Budget). Use unrounded numbers and a strict greater-than comparison. Cross-multiplication avoids rounded percentage boundary errors.
Keep the selected dollar and percentage thresholds visible as numeric input cells used by the formulas. Put all-row control comparisons beside the calculation. Nonmaterial rows still contribute to totals. A partial operating result is Revenue minus the selected Expenses, not net income.
The optional scripts/review_variances.py independently reproduces these calculations from assets/location-pnl.csv. It does not edit Excel. Use it only if the environment can actually execute it; distinguish an executed result from a reference result. Its presence gives no new execution capability.

## 3. Apply the chosen JSON layout
Validate schema_version = 1, rows = material_only, supported sort value, unique supported fields, valid worksheet_name and readable style values. The supported fields are Location, Category, Budget, Actual, Variance, VariancePercent, Direction, Driver. Stop and name unsupported settings rather than inventing a meaning.
Create the requested worksheet_name. Preserve the other layout sheet when comparing Review and Manager. If the destination already has unrelated content, request a new destination name before replacing it.
Use the title exactly. Create columns in JSON array order and copy each header exactly. Show all and only material rows; no arbitrary top-N cutoff. Sort unfavorable rows first by descending ABS(ProfitImpact), then favorable rows by descending ABS(ProfitImpact); tie-break by Location, Category. Link displayed numeric results to Calculations. These report rows are a snapshot of which rows qualify; tell the reader to rerun the skill after source or threshold changes so filtering, sorting and prose are rebuilt.
For Driver, match all four source identifiers to review-context.md. When no driver was supplied, use commentary.missing_driver exactly. Keep each driver within commentary.max_words_per_driver. Do not infer a cause from a variance.
Apply number_formats.dollars to Budget, Actual and Variance; apply number_formats.percent to VariancePercent. Keep values numeric; a format changes display, not the stored value. Apply the style object: font and size; header fill/text; title color; alternating body fill; worksheet gridlines setting. Fit widths, wrap driver text, and size row heights so nothing is clipped. Do not add charts, icons, decorative arrows, triangles, extra columns or invented recommendations.

## 4. Verify and disclose
Check exact header order, material count, source/control totals, sort order, numeric formats, readable text, and missing-driver wording. Report the policy and layout filenames used, what was actually changed, and any inaccessible files or unverified behavior. Never describe a proposed or saved example as a completed Copilot run.
For the supplied baseline policy expect 12 input rows, 8 material rows, revenue actual 396300 and expense actual 132500. The higher thresholds yield 6 material rows. These expectations are checks, never substitutes for calculation.
