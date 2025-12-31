---
title: Excel - Never type in data
date: "2005-11-08T12:00:00Z"
categories:
  - excel-tips
wp_id: 510
---

**Rule #2: Never type in data** in Excel.

You rarely spend time **creating** voluminous data. Usually, you're just processing it (copying, transforming, whatever).

Sometimes **data is on a web page** -- typically tables. To copy such data, open the page in **Internet Explorer** and paste it in Excel. You won't like the formatting. So copy the cells you just pasted, go to a different sheet, and Edit-Paste Special just the values (Alt-E-S-V-Enter).

Sometimes **data is on a text file**. You can open text files directly in Excel. Each line becomes a row. You can split lines into columns if there is a "delimiter" between any two cells. Just load a text file, select all the rows, and play with the Data - Text to Columns menu (Alt-D-E).

Sometimes, **data is on a PDF file**. Usually, such data is in a table. If you have Adobe Reader, tough luck. Just select and copy the table, paste it into Notepad, manually format it (painful), copy again from Notepad and paste in Excel. If you have Adobe Acrobat, it's slightly better. You can use the "Select Column" tool to select and copy entire columns of the table in one shot.

Sometimes, **data is on paper**. Scanner often come with an optical character recognition (OCR) software. If not, Microsoft Office 2003 comes with a Microsoft Office Document Imaging tool has OCR. Just scan the image, open it in the Microsoft Document Imaging tool, go to the Tools - Recognize Text Using OCR... menu, and pray.

After all this importing, the **data is never "clean"**. Errors due to unintended delimiters, extraneous blank lines, etc are fairly frequent. I'll talk about how to manage this when discussing Rule #3: Automate the task

---

## Comments

<!-- wp-comments-start -->

- **A benificiary** _9 Nov 2005 5:29 am_:
  this is S Anand of IIMB days - making lives easier
- **wasted_psuede** _17 Nov 2005 9:58 am_:
  what about rules 3 and 4?
- **james chacko** _1 Nov 2006 12:45 pm_:
  how to avoid copying extraneous blank lines while impoting data from text file to excel
- **Egads** _19 May 2009 10:14 pm_:
  "If you have Adobe Reader, tough luck." Well, maybe not - if one holds down the 'Alt' key while using the pointer (arrow) select tool, it is possible to select and copy columns from PDF tables to Excel...

<!-- wp-comments-end -->
