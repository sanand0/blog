---
title: R scatterplots
date: "2010-09-19T21:38:02Z"
lastmod: "2010-10-11T15:02:09Z"
categories:
  - data
  - how-i-do-things
wp_id: 2535
---

I was browsing through [Beautiful Data](http://books.google.co.uk/books?id=zxNglqU1FKgC), and stumbled upon this gem of a visualisation.

[![r-scatterplots](/blog/assets/rscatterplots.webp "r-scatterplots")](/blog/assets/rscatterplots.webp)

This is the default plot R provides when supplied with a table of data. A beautiful use of small multiples. Each box is a scatterplot of a pair of variables. The diagonal is used to label the rows. It shows for every pair of variables their correlation and spread – at a glance.

Whenever I get any new piece of data, this is going to be the very first thing I do:

```r
plot(data)
```
