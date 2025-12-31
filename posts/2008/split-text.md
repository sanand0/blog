---
title: Split text
date: "2008-09-06T12:00:00Z"
categories:
  - excel-tips
wp_id: 35
---

> This is a series on what [Google Spreadsheets](http://docs.google.com/) can do that Excel can't.

[SPLIT(string, delimiter)](http://documents.google.com/support/spreadsheets/bin/answer.py?answer=105612) splits a string using a delimiter. So if you have "one,two,three,four" in cell A1, you could split that into 4 cells using =SPLIT(A1,",")

[![3.1](/blog/assets/flickr-31_2830261663_o-png.webp)](/blog/assets/flickr-31_2830261663_o-png.webp)

That's similar to Data > Text to Columns, except that if the original data changed, Text to Columns does not revise the output. SPLIT can give you **dynamic text-to-columns**. This is pretty useful when processing text data, in three ways:

1. You retain the original data
2. You don't need to re-apply Text to Columns. Extending the formula will work (and that's quicker)
3. It's dynamic. If the data changes, your split changes

Since SPLIT returns an array, you can do a bunch of useful things with it.

`=COUNTA(SPLIT(A1," "))` gives you the number of words in a string

`=SUM(SPLIT(A1,","))` sums up a comma separated list. "1,2,3,4" is added up to 10.

`=ARRAYFORMULA(SUM(LEN(SPLIT(A1,","))))` sums up the word lengths. So "one,two,three,four" splits into 4 words of length 3,3,5,4 each, which adds up to 15.

\

The ability to join and split also lets you **sort by multiple keys**. For example, say you had income by country and product. You want to show it sorted by Country & Product. You also want to show it by Product & Country.

So first take the data sorted by Country and Product.

[![3.2](/blog/assets/flickr-32_2830261665_o-png.webp)](/blog/assets/flickr-32_2830261665_o-png.webp)

Now, in column E, create a key that's sorted by Product and then by Income. Type

`=SORT(ARRAYFORMULA(B2:B10&":"&A2:A10&":"&C2:C10))`

... in cell E2. That will give you all the data in one cell, sorted by Product and then by Country. Now, just split the data, as shown here.

[![3.3](/blog/assets/flickr-33_2830261669_o-png.webp)](/blog/assets/flickr-33_2830261669_o-png.webp)

\

**Note**: You could have done the whole thing using one formula:

`=ARRAYFORMULA(SPLIT(SORT(ARRAYFORMULA(B2:B10&":"&A2:A10&":"&C2:C10)),":"))`

But for some reason, this doesn't seem to show the first row properly. No idea why.

**Can I do that in Excel?**

Well, not really. You're best off creating a user-defined function to duplicate the SPLIT function.

---

## Comments

<!-- wp-comments-start -->

- **Prakash H Ayer** _9 Sep 2008 8:25 am_:
  Thanks Anand. This is very useful.
- **Prakash Ayer** _9 Sep 2008 8:25 am_:
  Thanks Anand. This is very useful.
- **Sridhar** _17 Sep 2008 10:19 am_:
  Cant "mid" with "find" and "len" replace "split"? Even though its a round about way i think it can still do it.
- **Sridhar** _17 Sep 2008 11:11 am_:
  @Sridhar: Yes, this can be done, within reason. Chandoo has a post about [Splitting text in excel using formulas](http://chandoo.org/wp/2008/09/08/split-text-excel-functions/).
- **St** _27 Sep 2008 6:54 am_:
  It can be done in excel - we used excel to split up a sentence field into constituent words - but it is a bit roundabout - search for spaces or commas, count, split by count of space/comma

<!-- wp-comments-end -->
