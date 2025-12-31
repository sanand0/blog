---
title: User-defined functions to get cell formatting
date: "2006-09-02T12:00:00Z"
lastmod: "2009-03-23T15:39:23Z"
categories:
  - excel-tips
wp_id: 237
---

Sometimes you want to check the colour of a cell, or whether a cell is bold. This can be easily done with user-defined functions (UDFs). (To create a UDF, press Alt-F11, Alt-I-M, and type the code below.)

[![User defined functions to get the background colour and bold value of a cell](/blog/assets/flickr-user-defined-functions-to-get-the-background-colour-and-bold-value-of-a-cell_231663146_o-gif.webp)](/blog/assets/flickr-user-defined-functions-to-get-the-background-colour-and-bold-value-of-a-cell_231663146_o-gif.webp)

You can use ISBOLD(cell) to check if a cell is bold, and BGCOLOR(cell) to get the background colour of the cell. This lets you selectively process bold or shaded cells. The two examples below show how you can add only the cells in bold, or only the shaded cells.

[![Example to selectively add shaded cells](/blog/assets/flickr-example-to-selectively-add-shaded-cells_231663147_o-gif.webp)](/blog/assets/flickr-example-to-selectively-add-shaded-cells_231663147_o-gif.webp)

[![Example to selectively add bold cells](/blog/assets/flickr-example-to-selectively-add-bold-cells_231663148_o-gif.webp)](/blog/assets/flickr-example-to-selectively-add-bold-cells_231663148_o-gif.webp)

Rather than use an additional column for ISBOLD or BGCOLOR, you can use an array formula, like below. (Remember to press **Ctrl-Shift-Enter** instead of Enter after typing this formula)

[![Example to selectively add bold cells using a single array formula](/blog/assets/flickr-example-to-selectively-add-bold-cells-using-a-single-array-formula_231663149_o-gif.webp)](/blog/assets/flickr-example-to-selectively-add-bold-cells-using-a-single-array-formula_231663149_o-gif.webp)

But first, you need to change the [UDF to return an array](http://www.google.com/search?&q=excel+user+defined+function+%22return+an+array%22) rather than a single value. So IsBold will have to be modified as shown.

[![User defined function isBold modified to return an array](/blog/assets/flickr-user-defined-function-isbold-modified-to-return-an-array_231669052_o-gif.webp)](/blog/assets/flickr-user-defined-function-isbold-modified-to-return-an-array_231669052_o-gif.webp)

User-defined functions that process arrays can be very powerful. It can bring the full power of functional programming into Excel. I'll describe some next week.

PS: In case you're wondering, `Application.Volatile` tells Excel to recalculate the function every time the worksheet is recalculated. When a cell is made bold, or shaded, the **value** of the cell doesn't change. So Excel doesn't recalculate any formulas. You'll have to manually press F9 every time to recalculate these cells. And `Application.Volatile` ensures that when you press F9, these functions are recalculated.

---

## Comments

<!-- wp-comments-start -->

- **Ramly** _19 Mar 2007 3:07 pm_:
  good... May i ask your help to give me a solution for my problem... I always use vlookup to find some data in a specific range, my lookup value are employee code number then look for there name, age, address and so on. but today, i want look up a value with multiple returns. i want to have the some of a worker which he have in a specific date. Please give help regarding this matter.
- **Prasath** _13 Nov 2009 10:00 am_:
  Hi Need a help
  The ISBOLD function which is defined on top does not work if I change the cell which is Bold to Unbold.
  The formula should work automatically if a cell is changed BOLD or UNBOLD

<!-- wp-comments-end -->
