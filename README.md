# JSON settings: reader example

This is the companion download for “Beyond SKILL.md: Give Your Copilot Skill a Settings File” by George Mount / Stringfest Analytics. All company data and business drivers are fictional.

## Start here

Unzip the entire download. Keep the folder structure intact. The exercise uses the included CSV; the original webinar workbook is not required.

To calculate directly, you need Python 3. No extra packages are required. Open a terminal in the `variance-review` folder and run:

```text
python scripts/review_variances.py assets/location-pnl.csv references/policy.json
python scripts/review_variances.py assets/location-pnl.csv references/policy-higher-thresholds.json
```

On Windows, substitute `py` for `python` if needed. These commands print JSON, leave the input files unchanged, and do not write commentary or edit Excel. The original policy returns 8 material rows; the higher thresholds return 6. Both process 12 rows and reconcile controls.

If Python is unavailable, inspect the saved results in `expected-results/`. These are reference results, not evidence that a script ran in your session. You can open the CSV in Excel to inspect the inputs.

## Use with an assistant

Make the entire `variance-review` folder available to your application's supported skill mechanism, preserving its relative paths. Use the prompts in `practice-prompts.md`. Skill installation varies by application; this package is a portable example, not an installer. An application that only accepts individual attachments may not load a skill folder or execute its script.

The instructions request a review in the response. They do not assume an active workbook, access to local files elsewhere, or a particular Excel add-in. If Python execution is unavailable, the skill must state that limitation. Run the direct commands above to reproduce the numerical demonstration.

## What's included

- `variance-review/SKILL.md`: assistant instructions for this practice review.
- `variance-review/references/policy.json`: original $5,000 / 10% policy and control totals.
- `variance-review/references/policy-higher-thresholds.json`: $10,000 / 15% policy; otherwise identical.
- `variance-review/references/review-context.md`: documented drivers and writing rules.
- `variance-review/scripts/review_variances.py`: original webinar calculation script, using only the Python standard library.
- `variance-review/assets/location-pnl.csv`: 12 input rows with the required six columns.
- `expected-results/baseline.json` and `higher-thresholds.json`: complete saved script outputs.
- `expected-results/comparison.md`: readable results and interpretation.
- `practice-prompts.md`: full prompts for inspection, execution, and comparison.

## Editing JSON

Use a plain-text editor. Keep the whole policy file, use straight double quotes, write percentage thresholds as decimals, and avoid comments or trailing commas. Don't paste the shortened blog excerpts over the full policy. The higher-threshold version is supplied to avoid accidental edits to other fields.

## Scope of the calculation

Materiality is absolute variance above the dollar threshold OR absolute variance above the percentage threshold. Equality does not pass. For zero budget, percentage is undefined (`null` in JSON), and only the dollar test applies. The test uses unrounded values; output percentages are decimal ratios.

Revenue and expense totals are separate. Favorability follows the effect on the partial operating result. The sample omits other P&L categories and does not calculate net income. The company and currency fields label the output; the CSV has no entity or currency column to verify them against.

The script checks required headers, duplicate keys, period, row types, nonnegative finite amounts, and controls. It is a teaching example, not a general accounting validation system. For another dataset, establish independent controls and update context rather than copying these fictional totals.

If a control mismatch or input error occurs, correct or reconcile the source before proceeding. Do not change the control merely to make the script pass.
