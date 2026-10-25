# JSON settings for Copilot in Excel

**[Download the exercise files (ZIP)](https://github.com/stringfestdata/excel-skills-json-demo/archive/refs/heads/main.zip)**

Companion files for George Mount's [How to use JSON to structure Copilot outputs in Excel](https://stringfestanalytics.com/json-copilot-excel-skills-output-structure/). Give yourself a detailed report and your manager a shorter version, without rewriting the calculation instructions. One prepared skill reads two saved JSON layouts.

**The test:** Review has eight columns; Manager has five. Both keep the same eight selected rows and dollar amounts. JSON holds the choices that change; the skill holds the procedure. A regular prompt can do this too. Separate settings become useful when you reuse or vary the report.

## Start here

1. **Download and extract the ZIP.** On Windows, right-click it and choose **Extract All**. On a Mac, double-click it. Open the extracted `excel-skills-json-demo-main` folder.
2. **See the result first.** Open `live-example/json-skills-completed.xlsx`. Click **Review**, then **Manager**, and compare the columns. Close this completed example without editing it.
3. **Open `json-skills-practice.xlsx`.** This starting workbook has only **Data**. Save a working copy to OneDrive or SharePoint if Copilot asks.
4. **Add the skill.** In Copilot settings, open **Manage plugins & skills** (or **Manage skills**) > **Custom skills**. Choose **Create OneDrive folder** if needed, then **Open skills folder**. Older labels may be **Add > Add in OneDrive** or **Skills OneDrive folder**. Copy the entire `variance-review-json` folder there, let it sync, refresh skills, and enable it.
5. **Run the prompts.** Select **Data**. Open [practice-prompts.txt](practice-prompts.txt), copy **PASS 1** into Copilot and check the result. Then run **PASS 2**. The file includes a small optional heading change to try afterward.

No GitHub account, Git software, or Python is needed. Your Excel account must offer Copilot workbook editing and Custom skills. Skills currently require an English Office display language. See [Microsoft's setup guidance](https://support.microsoft.com/en-us/Excel/copilot/copilot-in-excel-skills) if those controls are missing.

## What to open

| File or folder | Purpose |
| --- | --- |
| [START-HERE.txt](START-HERE.txt) | Plain-text setup instructions to read after downloading. |
| `json-skills-practice.xlsx` | Starting workbook. |
| `variance-review-json/` | Complete skill folder; keep its contents together. |
| [practice-prompts.txt](practice-prompts.txt) | Two prompts, what to check, an optional heading change and a layout repair prompt. |
| `live-example/json-skills-completed.xlsx` | Finished workbook from the original live Copilot test. |
| [supporting-files](supporting-files/README.txt) | Optional calculation checks and reference images. |

## Check the result

**Review:** eight columns. **Manager:** five columns. Both should show the same eight rows, starting with Navy Yard / Sushi and a ($14,200) variance. Keep **Data** unchanged.

Copilot can miss formatting settings; use the **LAYOUT REPAIR** prompt if needed. The [live test notes](live-example/live-test-notes.txt) record the exact follow-up used for the saved example.

The skill must be able to read the selected JSON files. JSON does not make Excel apply settings automatically or guarantee that Copilot follows them. If you try the optional heading change, edit the installed OneDrive copy, let it sync, refresh skills and rerun the prompt.

The blog walks through the JSON settings. All figures and business explanations are fictional. This is a partial operating review, not a complete profit-and-loss statement.
