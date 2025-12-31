---
title: Excel - Avoid manual labour
date: "2005-11-17T12:00:00Z"
categories:
  - excel-tips
wp_id: 506
---

**Rule #3: Avoid manual labour**. Use Excel to automate the task.

I use Excel's formulas to speed up repetitous tasks. These techniques are **powerful**, meaning, you can do a lot with a little, but can have unforeseen consequences.

Excel can **find and replace formulas**. If you had hardcoded formulas and wanted to change =B1\*3.14 to =B1\*3.1416 across all rows, just find "\*3.14" and replace it with "\*3.1416". Find and replace works in formulas. **This is very powerful**. You can use it to change the source (e.g. change the source from column B to C by finding "=B" and replacing with "=C") or even the formula (find and replace "SUM(" with "SUBTOTAL(9,").

You can also **search and replace for errors** (like #N/A, #REF, etc). In the Find dialog options, select "Values" under the Look in" option. To replace these cells, copy and paste the cells by value (Ctrl-C, go where you want to paste, Alt-E-S-V-Enter). Now you can search and replace #N/A just like any other value.

**Find external links**. If you have links to other Excel files, and one of them is missing, you'll get an error saying "This workbook contains links ..." It's annoying, and difficult to trace the source. But since links to external files have the formula =Path\[file]Sheet!Cell, just search for "[" across sheets (you can search across sheets using the Options button).

**Format based on value**. **Conditional formatting (Alt-O-D) accepts formulas**. You can set a cell's background to red, yellow or green if it's value is low, medium or high. Pick a cell, say D3. In conditional formatting, select "Formula is" instead of "Cell value is", and type "=D3<10". Set the format to a red background. Copy the formatting to all the cells (use the Format Painter button, or Edit-Paste Special-Formats). All cells less than 10 will have a red background. **This is powerful** because you can use any formula based on any cell. For example, you could pick the conditional formatting formula "=$C3<10" for the cell D3. The cell becomes red if the cell to its left is less than 10. Best of all, you can say "=$C3<$A$1". As you change the value in cell A1, the colours change automatically. Since you can copy and paste the formatting alone (Edit - Paste Special - Format), you can set the conditional format in one cell, and copy & paste it across any selection.

**Remove unwanted rows**. Sometimes, when you import data, you have empty rows, or errors or whatever. To delete empty rows, select the data, go to Data - Filter - Autofilter. Click on one of the arrow buttons, and select the "(Blank)". This will display all the blank rows. Select them all and delete them. If you want to delete rows with errors, click the arrow button, select whichever values are errors, and delete those rows. If you want to delete rows based on some other criteria, create a new column that shows TRUE or FALSE based on the criteria, do the Autofilter, and delete the rows.

An alternative to Autofilter is to sort the data based on the column you want. All blank rows (or errors, etc) will be grouped together, and you can delete them at one shot.

---

## Comments

<!-- wp-comments-start -->

- **Ahmed** _17 Nov 2005 12:00 pm_:
  what`s the meaning of $ in the cell that comes before the cell location like $A$3 thanx a lot
- **Kannan** _17 Nov 2005 12:00 pm_:
  To find the links, go to Edit and Links - You can find the external links instead of search.

<!-- wp-comments-end -->
