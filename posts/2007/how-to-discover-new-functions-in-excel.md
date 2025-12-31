---
title: How to discover new functions in Excel
date: "2007-01-13T12:00:00Z"
lastmod: "2009-03-23T15:38:34Z"
categories:
  - excel-tips
wp_id: 128
---

Firstly, believe that **Excel can do anything**.

It's true. Excel is a [functional programming language](http://research.microsoft.com/~simonpj/Papers/excel/). Not with the same power as some programming languages, maybe. But power is just a way of making a little go a long way ([power = succinctness](http://www.paulgraham.com/power.html), according to Paul Graham). And Fred Brooks, in [No Silver Bullet](http://www-inst.eecs.berkeley.edu/~maratb/readings/NoSilverBullet.html), argues:

> I believe the single most powerful software-productivity strategy for many organizations today is to equip the computer-naive intellectual workers who are on the firing line with personal computers and good generalized writing, drawing, file, and spreadsheet programs and then to turn them loose.

Next, believe that **Excel probably already has the function** you're looking for. Excel 2003 has over 300 functions. Presumably these are the most popular functions people use. Fair chance your function is one of them. Excellent chance that you don't know about it.

So first, search through Excel's help. I'll admit, it's not the best way to do it. I've learnt a trick to help me out. I **search for a function that does similar stuff, and see the "See Also" section**. Let me give you an example.

Once, we were modelling the revenues of a leasing company. Their finance manager had prepared a model to calculate the interest accruing from a lease. We needed the interest across several leases. With his model, we'd have to create 1 sheet for each lease. We were going to model thousands of leases. Clearly impossible.

Since I knew PMT could calculate the EMI, I checked the help on PMT, clicked the "See Also" link, and found a bunch of related functions. This, among others, lists the IPMT function, which can be used to calculate the interest at a single stroke, and a bunch of other useful functions. (That's how I first learnt about IPMT.

[![Related functions in Excel](/blog/assets/flickr-you-can-just-click-and-type_353748101_o-png.webp)](/blog/assets/flickr-you-can-just-click-and-type_353748101_o-png.webp "Photo Sharing")

But the really useful link is the "Financial functions" one, which lists every single financial function in Excel. That's worth going through in detail. In fact, there are many such categories that are useful: database functions, information functions, lookup and reference functions and text functions have some unexplored gems. Check out the [List of worksheet functions](http://office.microsoft.com/en-us/excel/HP052042111033.aspx) on Excel.

---

## Comments

<!-- wp-comments-start -->

- **Rajlaxmi** _13 Jan 2007 8:44 pm_:
  Hi Anand. i ve 50+ location data in pivot format. i imported this in a template using sumif. issue is editing the formula manually in the template to take the right location. any other way? Thx.
- **ania** _13 Feb 2007 8:36 am_:
  how to calucate simpleinterest in excel or in m.s sheet? help me
- **[Firdas](http://mainexcel.blogspot.com)** _22 Mar 2009 4:23 am_:
  I am surprised that you can make motion with excel. Very powerful.

<!-- wp-comments-end -->
