---
title: Excel - Avoid manual labour 4
date: "2005-12-21T12:00:00Z"
categories:
  - excel-tips
wp_id: 455
---

**Debugging in Excel** is another time consuming task. 80% of the trouble is identifying the problem (Error? What error? Where?) as opposed to fixing it (Why's THAT cell showing THAT?). Most of my time is spent chasing three kinds of errors: wrong reference (leading to a #N/A or #REF!), wrong data input, or wrong formula.

Wrong references are easy to spot. You'll see a #N/A or a #REF! sticking out. But on large sheets, even that's tough to spot. I always **have a SUM (or some kind of total) function that covers EVERY cell in EVERY table**, even if I don't need that information. If ther SUM shows a #N/A or #REF!, I can use Trace Error (Alt-T-U-E) to see where the problem is coming from.

If you **know** there's a wrong reference in a cell (say A1), and want to ignore it, use a new cell with the formula =IF(ISERROR(A1),0,A1). You can substitute an entire row, column or table this way.

**Wrong data input** is best avoided upfront. Before I hand my Excel sheets over for large scale data entry, I do three things:

1. **Let them enter data only in input areas**. Unprotect the cells the user can enter data in (Ctrl-1, Protection, remove the tick against 'Locked'), and protect the whole sheet (Alt-T-P-P).
2. **Validate the data**. Turn on data validation (Alt-D-L) on **all editable cells**, and specify the validation criteria.
3. **Make it easy to spot errors**. If there are percentages that should add to 100%, show the total in a cell that turns green if the total is 100%, and red otherwise. (Use conditional formatting - Alt-O-D). If data about 20 people must be entered, show the number of people about whom data is entered, and mark it red until it's 20. Make sure **all** criteria are captured. When the spreadsheet is filled, it should be impossible to make errors.

Wrong formulae (like + instead of -) are tough to spot. The best way to check for this is to **do the same calculation **in different ways**, and compare the results**. Whenever I create complex tables, I always have an error row at the bottom. I compare the totals on the table with the totals **calculated in a simpler way** and check the difference. This warns me when I miss out some elements, or double count something, in the table.

---

## Comments

<!-- wp-comments-start -->

- **Rajlaxmi** _1 Jan 2006 5:08 pm_:
  great tutorial on excel..ready reckoner...
- **S Anand** _2 Jan 2006 9:42 pm_:
  Thanks!
- **Peter** _8 Mar 2007 11:31 pm_:
  Avoid Manual Labour: I just spent hours writing a VB script that does essentially what the 'Conditional Formatting' feature does. Thanks for pointing it out!
- **[isomorphismes](http://isomorphismes.tumblr.com)** _13 Mar 2013 5:26 pm_:
  That is a great idea.

<!-- wp-comments-end -->
