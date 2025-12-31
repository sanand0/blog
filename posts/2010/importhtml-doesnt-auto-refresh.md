---
title: ImportHtml doesn’t auto-refresh
date: "2010-03-12T09:54:26Z"
categories:
  - coding
wp_id: 2487
---

A cool thing about [Google Spreadsheets](http://docs.google.com/) is that you can scrape websites using [external data functions](http://docs.google.com/support/bin/answer.py?hl=en&answer=75507) like importHtml. It’s really easy to use. The formula:

```excel
=importHtml("http://www.imdb.com/chart/top", "table", 1)
```

imports the [Internet Movie Database top 250](http://www.imdb.com/chart/top) table on to Google Spreadsheets.

Since you can [publish these as RSS feeds](http://www.mmmeeja.com/blog/web-development/google-spreadsheets-rss.html), it ought to, in theory, be a great way of generating RSS feeds out of arbitrary content.

There’s just one problem: [it doesn’t auto update](http://www.google.com/support/forum/p/Google%20Docs/thread?tid=46676d88b38e0c50&hl=en).

There are claims that it does [every](http://www.google.com/support/forum/p/Google%20Docs/thread?tid=061199840171feea&hl=en) [hour](https://docs.google.com/View?docID=dhrr6ms2_523cs7274fv&pageview=1&hgd=1). Maybe it does **when the sheet is open**. I don’t know. But it definitely does not when the sheet is closed. I wrote a simple script that logs the time at which the script was accessed, and prints the log every time it is accessed.

```python
#!/usr/bin/env python

import datetime, os.path

print 'Content-Type: text/plain; charset=utf-8'
print ''

logfile = 'timenow.log'
try:    timelog = open(logfile).readlines()
except: timelog = []
timelog.append(str(datetime.datetime.now()) + '\n')
open(logfile, 'w').writelines(timelog)
print ''.join(timelog)
```

Then I importHtml’ed it into Google spreadsheets, and left it on for the night. Result: absolutely no hits when the document is closed.

Pity. Guess [YQL](http://developer.yahoo.com/yql/) is still the best option.

---

## Comments

<!-- wp-comments-start -->

- **[pitching manual](http://www.coachingthebeginningpitcher.com)** _24 Jun 2010 5:29 pm_:
  I've just started using google spreadsheets. Really impressed with how user friendly they are. I went ine expecting the worse and was very suprised.
- **[Barry](http://www.todosquepaso.com)** _7 Jun 2012 6:27 pm_:
  I am running into the same thing. Can't get importHtml() to refresh when google spreadsheet is closed. Was thinking I could hammer force a cell value to equal the IH() function via a script but that seems awfully inelegant.
- **alois** _6 Sep 2012 4:20 pm_:
  so what happens when you add a parameter to the url with a value coming from a field which is set to show the current time - minute or hour ?

<!-- wp-comments-end -->
