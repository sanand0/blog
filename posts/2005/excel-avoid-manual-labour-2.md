---
title: Excel - Avoid manual labour 2
date: "2005-12-09T12:00:00Z"
categories:
  - excel-tips
wp_id: 476
---

**Rule #3: Avoid manual labour (continued)**

**Reconciling data** is where I spend most of my time on Excel. Say you have a list of branches by city from 2 banks. You want to know where both banks have branches. Excel doesn't know that Kolkata is Calcutta. There are 500 cities, and you have 30 minutes.

[![Excel snapshot](/blog/assets/flickr-excel-snapshot_71837170_o-png.webp)](/blog/assets/flickr-excel-snapshot_71837170_o-png.webp)

**Use VLOOKUP** for a start. If Bank A's cities are in column A (say 2-500) and Bank B's cities in column B (say 2-400), in C2 type VLOOKUP(A2, B$2:B$400, 1, 0) (read Excel help -- all I'll say is, **don't miss out the 0 at the end**: otherwise you get approximate match, and that's not good). Copy the formula to down to C500. Similarly, in D2 type VLOOKUP(B2, A$2:A$500, 1, 0). Copy the formula down to D400.

[![Excel snapshot](/blog/assets/flickr-excel-snapshot_71837168_o-png.webp)](/blog/assets/flickr-excel-snapshot_71837168_o-png.webp)

You'll see the #N/A where there's no match. #N/A in Column C means Bank A has a branch here, but Bank B does not. Column D has the converse. But we're not done yet. There could be spelling mistakes. Using **two VLOOKUPs simplifies that problem considerably**. We just need to match the cities having #N/A on both lists to check for alternate spellings of cities -- which is a lot less work! So prepare a separate list: unmatched cities from Bank A, and unmatched cities from Bank B. (See the section on removing unwanted rows to simplify this.)

[![Excel snapshot](/blog/assets/flickr-excel-snapshot_71837166_o-png.webp)](/blog/assets/flickr-excel-snapshot_71837166_o-png.webp)

**Sort both the lists while remembering the original order**. You'll want to remember the original order often -- so just add a column, number it sequentially (1,2,3... use Alt-E-I-S), and sort the city names along with the numbers. When you want to get back the original order, just sort by the numbers again. To avoid distraction, you can move or hide these numbers. Now, you have a sorted list of unmatched cities. Notice that you can visually match many of these cities. **There's nothing easier to search (visually) than a sorted list.**

Finally, when you've mapped all your columns, the ones that are remaining are the ones where there is no overlap.

---

## Comments

<!-- wp-comments-start -->

- **Anonymous** _9 Dec 2005 7:22 pm_:
  Anand, I have a suggestion
- **S Anand** _9 Dec 2005 10:16 pm_:
  Yeah?
- **Anonymous** _10 Dec 2005 3:12 pm_:
  it got erased the last time...ok..this is what I wanted to say..
- **Anonymous** _10 Dec 2005 3:14 pm_:
  can you please categorize all these excel tips (rules) and add it as a bookmark on the right, so that we can refer to it at one shot rather than searching the archives.
- **Anonymous** _10 Dec 2005 3:14 pm_:
  btw thank you so much for taking your time
- **Anonymous** _10 Dec 2005 3:16 pm_:
  some of the text is getting erased when I submit a comment
- **Anonymous** _10 Dec 2005 3:17 pm_:
  I said "btw thank you so much for taking your time and explainning this to us"
- **Anonymous** _10 Dec 2005 3:18 pm_:
  you know what..I think the comment system is not supporting symbols...for example the 'and' symbol
- **Anonymous** _10 Dec 2005 3:19 pm_:
  thanks
- **S Anand** _10 Dec 2005 8:40 pm_:
  You're right, symbols are causing a problem. I'll try and fix that. Will put in the links as well, once I finish the series. Thanks!
- **S Anand** _11 Dec 2005 10:02 pm_:
  Hopefully, it's fixed. & - that works.
- **Tanmoy Sinha** _19 Sep 2008 7:28 am_:
  I had a similar issue at a much larger scale.. Had to match about 11,000 records in a database of about 44,000 using company names and city, both of which had spelling inconsistencies..\
  \
  What I did was use the 'Advanced Filter' function in Excel and wrote a small VB program to list out the filtered results in a dialog box allowing user to select the relevant ones using 'human' intelligence.\
  \
  The trick was in identifying a small enough part of the company's name that would serve as a 'signature' and at the same time throw back as (few) relevant results. What worked best for me was the following: \
  - Use the first 3 chars of the second word in the company name which is 4 or more characters long. i.e. avoid using the first word if there is another word 4 or more chars long. \
  - Use wildcard characters '?\*' before the 3 chars determined in the step above.

<!-- wp-comments-end -->
