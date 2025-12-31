---
title: RSS feeds in Excel
date: "2007-05-03T12:00:00Z"
categories:
  - excel-tips
wp_id: 85
---

The technique of [Web lookups in Excel](/Web_lookup_using_Excel.html) I described yesterday is very versatile. I will be running through some of the practical uses it can be put to over the next few days

TO generalise things beyond just [getting the Amazon price](/Web_lookup_using_Excel.html), I created a [user-defined function](/User-defined_functions_in_Excel.html) called XPATH. It takes two parameters:

> **URL** of the XML feed to read\
> **Search** XPath list string (separated by spaces)

This function can be used to extract information out of any XML file on the Web and get it out as a table. For example, if you wanted to watch the Top 10 movies on the [IMDb Top 250](http://www.imdb.com/chart/top), and were looking for torrents, an RSS feed is available from [mininova](http://www.mininova.org/). The URL http://www.mininova.org/rss/movie\_name/4 gives you an RSS file matching all movies with "movie\_name". From this, we need to extract the <item><title> and <item><link> elements. That's represented by "//item title link" on my search string.

[![Mininova RSS feed in Excel](/blog/assets/flickr-mininova-rss-feed-in-excel_482789516_o-png.webp)](/blog/assets/flickr-mininova-rss-feed-in-excel_482789516_o-png.webp)

The formula becomes `XPath2( "http://www.mininova.org/rss/"&A2&"/4", "//item title link")`. The result is a 2-dimensional array returning individual items in rows, and the columns are title and link. Pulling it all together, you can get the sheet above.

All of this could be done using a command-line program. Excel has one huge advantage though. It's one of the most powerful user-interfaces. Increasingly, I'm beginning to rely on just two user interfaces for almost any task. One is the browser, and the other is Excel. With Excel, I could have a sheet that has my [movie wishlist](/movie_wishlist.html) (which changes often), and add check to see if the torrent exists. Every time I add a bunch of movies to the wishlist, it's just a matter of copying the formula down. No need to visit a torrent search engine and typing each movie in, one by one.

Another example. Someone suggests 10 movies to watch. I'd rather watch the ones with a higher IMDb rating. Again, enter the Web lookup. Type in the movie names. Use a function like this to look up the rating on IMDb, and sort by the rating.

The possibilities are endless.

---

## Comments

<!-- wp-comments-start -->

- **Isit?** _3 May 2007 12:00 pm_:
  Is it possible to have the feeds update cumulative so the old feeds dont get replaced in excel?
- **Alex** _3 May 2007 12:00 pm_:
  Hi, I have an Excel spreadsheet with URLs of move titles on IMDB, and I would like to retrieve the movie rating. I've read your tutorials, and this one comes closest to what I need. However I still cannot figure out what needs to be done. It looks like you have this problem solved. If so, can you possibly share your solution with me? Thank you, Alex
- **Kishan** _3 May 2007 12:00 pm_:
  I came here searching for the other way round. That is to publish an RSS feed of what I have in Xcel! Thanks Anyways
- **venkat** _15 Oct 2010 4:09 pm_:
  Anand
  Can you provide the xpath function?, I need to read a rss feed into excel, and i want only some columns of data, i would appreciate if you could send the xpath function to my email id
  Thanks
  venkat
- **[Light Sensors](http://www.light-sensors.com)** _2 Dec 2010 7:08 pm_:
  movie ratings really depend on how cool the movie is, i usually rate movies depending on the story line `-;
- **rt** _27 Jun 2013 5:41 pm_:
  Hi, nice job ! can you share with me your xpath2 (i tried your other one without succes on amazon) ?Thanks, R

<!-- wp-comments-end -->
