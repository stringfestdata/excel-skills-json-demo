OPTIONAL SUPPORTING FILES | Stringfest Analytics

The main exercise is in START-HERE.txt and README.md at the top level.
These files are for readers who want to inspect the calculations further.
They are not required to compare the Review and Manager layouts in Excel.

expected-results/ contains saved JSON calculation results.
reference-layouts/ contains independently prepared teaching figures.
For genuine live Copilot screenshots and the completed workbook, use
live-example/ at the top level. Its live-test-notes.txt records the exact
formatting follow-up used in the original run.

OPTIONAL PYTHON CHECK

Python 3, standard library only. From the variance-review-json folder run:
python scripts/review_variances.py assets/location-pnl.csv references/policy.json
python scripts/review_variances.py assets/location-pnl.csv references/policy-higher-thresholds.json

The script prints JSON; it does not edit Excel. The baseline selects eight
rows and the higher thresholds select six. Compare these results with the
saved files in supporting-files/expected-results.

After changing data or thresholds in Excel, rerun the skill to rebuild
row selection, sorting and commentary. A new period needs independently
established controls and matching documented context. All figures and
business explanations are fictional; this is not a complete P&L.
