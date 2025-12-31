---
title: User-defined functions in Excel
date: "2006-09-01T12:00:00Z"
lastmod: "2009-03-23T15:39:30Z"
categories:
  - excel-tips
wp_id: 238
---

Excel lets you create your own functions. If you wanted to create a function that returned the distance between two points (x1,y1) and (x2,y2), you can create a function DIST that takes these 4 parameters, and use it as shown below.

[![Example of a user-defined function in Excel](/blog/assets/flickr-example-of-a-user-defined-function-in-excel_231273003_o-gif.webp)](/blog/assets/flickr-example-of-a-user-defined-function-in-excel_231273003_o-gif.webp)

To create such a function,

1. press Alt-F11 to open the Visual Basic Editor
2. insert a new module (Alt-I-M)
3. type the following code:

   [![Visual Basic code for the DIST user-defined Excel function](/blog/assets/flickr-visual-basic-code-for-the-dist-user-defined-excel-function_231278952_o-gif.webp)](/blog/assets/flickr-visual-basic-code-for-the-dist-user-defined-excel-function_231278952_o-gif.webp)

Anything you declare as a "Function" in Excel's Visual Basic automatically becomes visible in the Insert-Function dialog box under the category "User Defined" (see [examples](http://www.dailydoseofexcel.com/archives/category/vba/user-defined-functions/)). The function is normally saved with the file. This is a good idea if you're going to distribute the file. You can also save your functions in your [personal.xls](http://www.google.com/search?q=personal.xls&btnI=I'm+Feeling+Lucky) file and load it on startup.

There are 3 places where I suggest using UDFs.

1. You need to repeat a formula or use an additional cell to get the job done (e.g. replace Excel errors with empty strings)
2. You [can't get the information](/User-defined_functions_to_get_cell_formatting.html) from a formula (e.g. a cell's background colour)
3. It's very cumbersome to get the information using formulas (e.g. regular expressions)

Let's take the first one: **replace Excel errors with empty strings**. Normally, you'd store the results in a cell (say A2), and have another cell with the formula =IF(ISERROR(A2),"",A2). Instead, create this function NOERROR:

[![Function NOERROR in Excel Visual Basic](/blog/assets/flickr-function-noerror-in-excel-visual-basic_231297813_o-gif.webp)](/blog/assets/flickr-function-noerror-in-excel-visual-basic_231297813_o-gif.webp)

Now you can enclose any Excel function inside a NOERROR() and it'll filter out the errors.

[![How the NOERROR function is used](/blog/assets/flickr-how-the-noerror-function-is-used_231297815_o-gif.webp)](/blog/assets/flickr-how-the-noerror-function-is-used_231297815_o-gif.webp)

Notice that cell E2 would've had a #N/A error if you'd just used the VLOOKUP. This function also filters out #REF, #DIV/0!, #NAME? and all other errors.

BTW, you see column F displaying the formula in column E. I didn't type it out. That's another UDF.

[![FormulaString function returns the formula of a cell](/blog/assets/flickr-formulastring-function-returns-the-formula-of-a-cell_231297817_o-gif.webp)](/blog/assets/flickr-formulastring-function-returns-the-formula-of-a-cell_231297817_o-gif.webp)

I will talk about the other two places where you use UDFs tomorrow.

---

## Comments

<!-- wp-comments-start -->

- **Greg** _4 Apr 2007 3:15 pm_:
  This is very helpful! I am having a problem however; I defined the functions in personal.xls (loaded upon startup) and they always work there, but they aren't available when working with a different file (I get the #NAME error). I also then created variants of them in the specific file, but although they worked, once I made some changes in the file (added a column), they no longer worked even though I re-did the reference properly. Any ideas?

<!-- wp-comments-end -->
