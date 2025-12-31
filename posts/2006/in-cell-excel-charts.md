---
title: In-cell Excel charts
date: "2006-08-17T12:00:00Z"
categories:
  - excel-tips
wp_id: 261
---

Juice analytics has some [Excel graphing](http://www.juiceanalytics.com/weblog/index.php?tag=excel) tips. You can make charts like below without using charts, using just text.

These are useful because the charts are aligned with the data.

[![Excel Gantt charts using just text](/blog/assets/flickr-excel-gantt-charts-using-just-text_217629714_o-gif.webp)](/blog/assets/flickr-excel-gantt-charts-using-just-text_217629714_o-gif.webp)

[![Excel bar charts using just text](/blog/assets/flickr-excel-bar-charts-using-just-text_217629715_o-gif.webp)](/blog/assets/flickr-excel-bar-charts-using-just-text_217629715_o-gif.webp)

I once used a similar technique to display people's staffing position. The sheet below lists people, projects they're on and how long they'll be on. The coloured cells to the right are a calendar display of the same stuff. Makes it easy to read.

[![Excel Staffing Plan without using charts](/blog/assets/flickr-excel-staffing-plan-without-using-charts_217642002_o-png.webp)](/blog/assets/flickr-excel-staffing-plan-without-using-charts_217642002_o-png.webp)

The trick is to place each week for each person as a thin cell, like below. Then the cell is populated with a formula that makes it 0 or 1 depending on whether the person is available that week or not. (The blue row #2 stores the start date of the week, and I compare this with the end date of each person's project.)

[![Excel Staffing Plan - formula](/blog/assets/flickr-excel-staffing-plan---formula_217642004_o-png.webp)](/blog/assets/flickr-excel-staffing-plan---formula_217642004_o-png.webp)

And then, you can turn on conditional formatting.

[![Excel Staffing Plan - conditional formatting](/blog/assets/flickr-excel-staffing-plan---conditional-formatting_217642003_o-png.webp)](/blog/assets/flickr-excel-staffing-plan---conditional-formatting_217642003_o-png.webp)
