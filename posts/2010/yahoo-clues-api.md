---
title: Yahoo Clues API
date: "2010-11-22T13:31:48Z"
categories:
  - coding
wp_id: 2558
---

[Yahoo Clues](http://clues.yahoo.com/) is like [Google Insights for Search](http://www.google.com/insights/search/). It has one interesting thing that the latter doesn’t though: [search flows](http://help.yahoo.com/l/us/yahoo/search/clues/clues-06.html).

It doesn’t have an official API, so I thought I’d document the unofficial one. The API endpoint is

```text
http://clues.yahoo.com/clue
```

The query parameters are:

- q1 – the first query string
- q2 – the second query string
- ts – the time span. 0 = today, 1 = past 7 days, 2 = past 30 days
- tz – time zone? Not sure how it works. It’s just set to “0” for me
- s – the format? No value other than “j” seems to work

So a search for “gmat” for the last 30 days looks like this:

```text
http://clues.yahoo.com/clue?s=j&q1=gmat&q2=&ts=2&tz=0
```

The response has the all the elements required to render the page, but the search flows are located at:

- response.data[2].qf.prevMax – an array of queries that often precede the current one
- response.data[2].qf.nextMax – an array of queries that often follow the current one

The other parameters (such as demographic, geographic and search volume information) is pretty interesting as well, but is something you should be able to extract more reliably from [Google Insights for Search](http://www.google.com/insights/search/).

---

## Comments

<!-- wp-comments-start -->

- **[Erudite Technologies](http://www.eruditetechnologies.com.au)** _5 Aug 2011 2:18 am_:
  Thanks for this article! We were using this recently until Yahoo changed the URL for the Yahoo Clues API. It is now as follows:
  Base URL: http://clues.yahoo.com/analysis
  Parameters:
  nu - Not sure, I haven't tried changing this. Usually set to 1.
  s - Same as above. Set this to j
  ts - I'm guessing this is the time range in the format: yyyyMMdd,yyyyMMdd
  tu - Not sure about this either. Haven't changed this away from 'month'
  q1 - The first Query
  q2 - The second Query
  l - Not sure. Works with 1
  lt - Might be the location scope of the query. Defaults to 'World'
  h - Not sure. I have this set to 6
  A sample URL might look as follows:
  http://clues.yahoo.com/analysis?nu=1&s=j&ts=20110704,20110804&tu=month&q2=&q1=Trend&l=1<=World&h=6
  The format of the JSON looks to be the same. Hopefully this helps someone else!

<!-- wp-comments-end -->
