---
title: Dynamically eliminate duplicates
date: "2008-09-04T12:00:00Z"
categories:
  - excel-tips
wp_id: 37
---

> This is a series on what [Google Spreadsheets](http://docs.google.com/) can do that Excel can't

To get a list of unique values from a list, use the [UNIQUE function](http://documents.google.com/support/spreadsheets/bin/answer.py?hl=en-uk&answer=92022) on [Google Spreadsheets](http://docs.google.com/).

For example, if you have a list of browsers in column A, type `=UNIQUE(A1:A17)` at cell B1 to get a unique list of browsers. This is a dynamic list. If you change the list of browsers, the unique list gets updated automatically.

[![1.1](/blog/assets/flickr-11_2825546538_o-png.webp)](/blog/assets/flickr-11_2825546538_o-png.webp)

You can use UNIQUE to **create a dynamic pivot table**. Quite often, you end up creating a pivot table simply to summarise by one column. The main purpose the pivot table serves is in getting a list of unique values on that column. Plus, it's a bit heavy on the UI. And every time the data changes, you need to refresh the pivot. But with the UNIQUE function, you can get a dynamic list of unique values, and you can use the COUNTIF and SUMIF function next to each value. Here is an example showing the frequency table of the browsers shown earlier. Column C does a COUNTIF of the unique values on the original list.

[![1.2](/blog/assets/flickr-12_2825546532_o-png.webp)](/blog/assets/flickr-12_2825546532_o-png.webp)

You can also use UNIQUE as the input to another formula:

`=COUNT(UNIQUE(LIST))` counts the number of unique values

`=COUNT(LIST)-COUNT(UNIQUE(LIST))` gives the number of duplicates

`=INDEX(UNIQUE(LIST),3)` gives you the third unique value

`=LARGE(UNIQUE(LIST),3)` gives you the third largest unique value

... and so on.

**Can I do that in Excel?**

You can, but not easily. There are two approaches, but each has its limitations.

**A. Use Advanced Filters: easy but static**

1. Create an advanced filter on column A (Alt-D-F-A)
2. Select Copy to another location
3. Click in the Copy to box, and then click the cell B1
4. Select Unique records only
5. Click OK

[![1.3](/blog/assets/flickr-13_2825546548_o-png.webp)](/blog/assets/flickr-13_2825546548_o-png.webp)

But the list of unique values that you get here is static. If you changed one of the values, the list of unique values does not change.

**B. Use a complex formulae that are dynamic**

First, blank out the duplicates by typing this formula:

`=IF(COUNTIF(A$1:A1,A1)=1,A1,"")`

adjacent to the first cell (into B1), and dragging it all the way down (to B17).

Now, create a named range (Alt-I-N-D) for these cells (B1:B17) called WithBlanks and another named range called NoBlanks for the cells one column to the right (C1:C17).

On the first cell of NoBlanks (C1), type this [formula](http://www.cpearson.com/):

```excel
=IF(ROW()-ROW(NoBlanks)+1>ROWS(WithBlanks)-COUNTBLANK(WithBlanks),"",
    INDIRECT(ADDRESS(SMALL((IF(WithBlanks<>"",ROW(WithBlanks),ROW()+
    ROWS(WithBlanks))),ROW()-ROW(NoBlanks)+1),COLUMN(WithBlanks),4)))
```

Press Ctrl-Shift-Enter rather than Enter, because it's an array formula. Now drag this all the way down (to C17).

The list in column C is dynamic. If you change a cell in column A, column C is updated. But the formula can only handle one column. Google Spreadsheets' UNIQUE function works with any number of columns. If you had data in the range A1:D100 and wanted the unique rows, UNIQUE(A1:D100) gets that for you.

[![1.4](/blog/assets/flickr-14_2825546554_o-png.webp)](/blog/assets/flickr-14_2825546554_o-png.webp)

**Note**: I'm staying away from [user defined functions](/User-defined_functions_in_Excel.html). You could, of course, create a UNIQUE function in Excel using Visual Basic. In fact, you should!

---

## Comments

<!-- wp-comments-start -->

- **Ken J** _19 Sep 2008 1:10 pm_:
  Great entry. I love your site. It is perfect for advanced users.\
  \
  Let's hope Google's pressure will force some innovation at excel.
- **[hk](http://www.isheet.com)** _21 May 2009 3:30 am_:
  What about Data/Consolidate from menu?

<!-- wp-comments-end -->
