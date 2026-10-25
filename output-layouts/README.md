# Start here: JSON settings for Copilot in Excel

This exercise uses one prepared Excel skill to make two views of the same data. You do not need to write a skill or run Python.

## 1. Get the files from GitHub

Open the [repository's `json-output-layouts` branch](https://github.com/stringfestdata/excel-skills-json-demo/tree/json-output-layouts). Above the files, choose **Code > Download ZIP**, then extract the ZIP on your computer. Open the extracted **output-layouts** folder.

These are GitHub's standard [repository download steps](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives). Keep this branch selected: the older example on `main` uses a different workflow.

Start with just these two items:

| Item | What to do with it |
| --- | --- |
| `json-skills-practice.xlsx` | Open this starting workbook in Excel. |
| `variance-review-json` folder | Copy the whole folder into Excel's OneDrive skills folder. |

Leave the remaining files in place. You can explore them later.

## 2. Read one small part of the JSON

Open `variance-review-json/references/review-layout.json` in a plain-text editor such as Notepad. Its settings include:

```json
{
  "worksheet_name": "Review",
  "title": "June 2026 variance review"
}
```

This is a shortened teaching example, not a replacement for the complete file. Read the first line as "worksheet name is Review." The second sets the report title. A colon separates a setting's name from its value; a comma separates one setting from the next. Text uses straight double quotes. The braces enclose the group.

`SKILL.md` explains the job. The JSON file supplies choices for that job, including column headings and number formats.

## 3. Install the prepared skill

1. In Excel's Copilot pane, open **Manage plugins & skills** (or **Manage skills**) and then **Custom skills**.
2. Use **Add > Add in OneDrive**, or the **Skills OneDrive folder** link, to open the folder.
3. Copy the entire `variance-review-json` folder there. `SKILL.md` must be directly inside it; keep its supporting folders intact.
4. Let OneDrive sync, refresh the skill list, and enable both Custom skills and `variance-review-json`.

Your Excel account must offer Copilot workbook editing and Custom skills. See [Microsoft's setup guidance](https://support.microsoft.com/en-us/Excel/copilot/copilot-in-excel-skills) if the controls differ.

## 4. Run the two supplied prompts

Open `json-skills-practice.xlsx`, select **Data**, and use **PASS 1** in [practice-prompts.txt](practice-prompts.txt). Copilot should create **Calculations** and **Review**.

Next use **PASS 2**. It selects `manager-layout.json` while keeping the same data and policy. Copilot should add **Manager** and preserve **Review**.

| Check | Review | Manager |
| --- | --- | --- |
| Report columns | 8 | 5 |
| Data rows | 8 | The same 8 |
| First row | Navy Yard / Sushi | Navy Yard / Sushi |
| First dollar variance | ($14,200) | ($14,200) |
| Dollar heading | Variance $ | Vs budget |

The first live Review run needed a follow-up to correct its font and font colors. JSON gives you settings to check, not a guarantee of perfect output. The **LAYOUT REPAIR** prompt in the same file can help.

## 5. Optional: change one label

In your installed `references/manager-layout.json`, find `"header": "Vs budget"` and change only the value to `"Change vs plan"`. Keep the quotes and surrounding punctuation. Save the existing `.json` file, let OneDrive sync, refresh skills, and run PASS 2 again.

Check that the heading changes while the eight rows and variance amounts stay the same. This label edit is an optional reader experiment; the supplied screenshots show the original `Vs budget` label.

## Finished example and deeper checks

The [live-example](live-example) folder contains the saved Copilot workbook, genuine screenshots, the exact formatting follow-up, and an independent verification record. All data and business explanations are fictional.

For a first pass, you can stop after comparing the two views. [README.txt](README.txt) explains the optional threshold experiment, Python calculation checks and other supporting files. None of those are required to learn how a layout setting changes the output.

After changing source data or thresholds, rerun the skill to rebuild row selection, sorting and commentary. This sample is a partial operating review, not a complete profit-and-loss statement.
