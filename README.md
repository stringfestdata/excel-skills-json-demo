# JSON settings for Copilot in Excel

**[Download the exercise files (ZIP)](https://github.com/stringfestdata/excel-skills-json-demo/archive/refs/heads/main.zip)**

Companion files for George Mount's *How to use JSON to structure Copilot outputs in Excel*. One prepared skill creates a detailed Review sheet and a shorter Manager sheet from the same data.

## Start here

1. **Download and extract the ZIP.** On Windows, right-click it and choose **Extract All**. On a Mac, double-click it. Open the extracted `excel-skills-json-demo-main` folder.
2. **Open `json-skills-practice.xlsx` in Excel.** Save a working copy to OneDrive or SharePoint if Copilot asks.
3. **Add the skill.** In Copilot settings, open **Manage plugins & skills** (or **Manage skills**) > **Custom skills**. Use **Add > Add in OneDrive** or the **Skills OneDrive folder** link. Copy the entire `variance-review-json` folder there, let it sync, refresh skills, and enable it.
4. **Run the prompts.** Select **Data** in the workbook. Open [practice-prompts.txt](practice-prompts.txt) and copy **PASS 1** into Copilot, then **PASS 2**.

No GitHub account, Git software, or Python is needed. Your Excel account must offer Copilot workbook editing and Custom skills. See [Microsoft's setup guidance](https://support.microsoft.com/en-us/Excel/copilot/copilot-in-excel-skills) if those controls are missing.

## What to open

| File or folder | Purpose |
| --- | --- |
| [START-HERE.txt](START-HERE.txt) | Plain-text setup instructions to read after downloading. |
| `json-skills-practice.xlsx` | Starting workbook. |
| `variance-review-json/` | Complete skill folder; keep its contents together. |
| [practice-prompts.txt](practice-prompts.txt) | The two main prompts and an optional layout repair prompt. |
| `live-example/json-skills-completed.xlsx` | Finished workbook from the original live Copilot test. |
| [supporting-files](supporting-files/README.txt) | Optional calculation checks and reference images. |

## Check the result

**Review:** eight columns. **Manager:** five columns. Both should show the same eight rows, starting with Navy Yard / Sushi and a ($14,200) variance. Keep **Data** unchanged.

Copilot can miss formatting settings; use the **LAYOUT REPAIR** prompt if needed. The [live test notes](live-example/live-test-notes.txt) record the exact follow-up used for the saved example.

The blog walks through the JSON settings. All figures and business explanations are fictional. This is a partial operating review, not a complete profit-and-loss statement.
