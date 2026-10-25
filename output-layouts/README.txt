JSON + Excel skills | Stringfest Analytics

All company figures and business drivers are fictional. This is a partial operating review, not a complete P&L.

1. Open json-skills-practice.xlsx in Excel. Save a working copy to OneDrive or SharePoint as required by your Copilot experience. The source is tblLocationPnL on Data.
2. In Copilot settings, open Manage skills (or Manage plugins & skills), then Custom skills. Create/open the OneDrive skills folder.
3. Copy the whole variance-review-json folder into that folder. Keep SKILL.md at the root and preserve references, scripts and assets. Do not copy just SKILL.md. Refresh skills after sync finishes.
4. Use the prompts in practice-prompts.txt, first with review-layout.json, then manager-layout.json. Keep policy.json the same during the layout comparison.
5. Check the two layouts have the same eight material rows. Then optionally try policy-higher-thresholds.json; that separate experiment should leave six.

The worksheet/figure examples are independently prepared reference layouts, not screenshots of an executed Copilot session. Desktop automation was unavailable during preparation. Actual Copilot file loading and workbook editing must still be checked in your account. Skills and tools depend on your current application/account.

The original independent calculation is retained in variance-review-json/scripts/review_variances.py. Python 3, standard library only. From variance-review-json run:
python scripts/review_variances.py assets/location-pnl.csv references/policy.json
python scripts/review_variances.py assets/location-pnl.csv references/policy-higher-thresholds.json

The saved outputs in expected-results were regenerated and checked. The script prints JSON; it does not edit Excel. A new period requires new independently established controls and matching documented context.

Source example: https://github.com/stringfestdata/excel-skills-json-demo
Microsoft setup: https://support.microsoft.com/en-us/Excel/copilot/copilot-in-excel-skills
