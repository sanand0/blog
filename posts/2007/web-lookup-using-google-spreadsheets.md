---
title: Web lookup using Google Spreadsheets
date: "2007-12-31T12:00:00Z"
categories:
  - excel-tips
wp_id: 66
---

I'd written earlier about [Web lookup in Excel](/blog/web-lookup-using-excel/). I showed [an example](/blog/rss-feeds-in-excel/) how you could create a movie wishlist that showed the links to the torrents from [Mininova](http://www.mininova.org/).

You can do that even easier on [Google Spreadsheets](http://spreadsheets.google.com/). It has 4 functions that let you [import external data](http://documents.google.com/support/spreadsheets/bin/answer.py?hl=en&answer=75507):

- **=importData**("URL of CSV or TSV file").\
  Imports a comma-separated or tab-separated file.
- **=importFeed**(URL).vLets you import any Atom or RSS feed.
- **=importHtml**(URL, "list" | "table", index).\
  Imports a table or list from any web page.
- **=importXML**("URL","query").\
  Imports anything from any web page using [XPath](http://www.w3.org/TR/1999/REC-xpath-19991116).

Firstly, you can see straight off why it's easy to view RSS feeds in Google Spreadsheets. Just use the `importFeed` function straight away. So, for example, if I wanted to track all [8GB iPods on Google Base](http://base.google.com/base/s2?q=ipod&btnG=Search+Base&authorid=81898&a_n0=products&a_y0=9&nd=1&showrefine=1&hl=en&gl=US#ajax%3Fa_n0%3Dproducts%26a_y0%3D9%26start%3D0%26q%3Dipod%26scoring%3D%26%26a_n1%3Dproduct%2Btype%26a_y1%3D1%26a_o1%3D0%26a_v1%3Dmp3%2Bplayers%26a_n2%3Dprice%26a_y2%3D8%26a_o2%3D1%26a_t2%3D200%26a_u2%3Dusd%26a_n3%3Dbrand%26a_y3%3D1%26a_o3%3D5%26a_n4%3Dcondition%26a_y4%3D1%26a_o4%3D6%26a_n5%3Dgigabytes%26a_y5%3D2%26a_o5%3D0%26a_v5%3D8%26a_n6%3Dmpn%26a_y6%3D1%26a_o6%3D5%26%26%26%26lnk%3Drefine-2%26nd%3D1%26hl%3Den%26gl%3DUS%26view%3DList), I can import its [feed](http://base.google.com/base/search?a_n0=products&a_y0=9&start=0&q=ipod&scoring=&&a_n1=product+type&a_y1=1&a_o1=0&a_v1=mp3+players&a_n2=price&a_y2=8&a_o2=1&a_t2=200&a_u2=usd&a_n3=brand&a_y3=1&a_o3=5&a_n4=condition&a_y4=1&a_o4=6&a_n5=gigabytes&a_y5=2&a_o5=0&a_v5=8&a_n6=mpn&a_y6=1&a_o6=5&&&&lnk=refine-2&nd=1&hl=en&gl=US&view=List&output=rss&ie=utf8&oe=utf8) in Google Spreadsheets.

[![Google Spreadsheets ImportFeed](/blog/assets/flickr-google-spreadsheets-importfeed_2152015648_o-png.webp)](/blog/assets/flickr-google-spreadsheets-importfeed_2152015648_o-png.webp "Google Spreadsheets ImportFeed")

This automatically creates a list of the latest 8GB iPods.

Incidentally, the "Price" column doesn't appear automatically. It's a part of the description. But it's quite easy to get the price using the standard Excel functions. Let's say the description is in cell C1. `=MID(C1, FIND("Price", C1), 20)` gets you the 20 characters starting from "Price". Then you can sort and play around as usual.

The other powerful thing about Google Spreadsheets is the [CONTINUE function](http://documents.google.com/support/spreadsheets/bin/answer.py?hl=en&answer=71291). The `importFeed` function creates a multi-dimensional array. You can extract any cell from the array (for example, row 3, column 2 from cell C1) using `CONTINUE(C1, 3, 2)`. So you can just pick up the title and description, or only alternate rows, or put all rows and columns in a single column -- whatever.

[![Google Spreadsheets CONTINUE](/blog/assets/flickr-google-spreadsheets-continue_2151240703_o-png.webp)](/blog/assets/flickr-google-spreadsheets-continue_2151240703_o-png.webp "Google Spreadsheets CONTINUE")

The most versatile of the import functions is the `importXML` function. It lets you import any URL (including an RSS feed), filtering only the [XPath](http://www.w3.org/TR/1999/REC-xpath-19991116) you need. As I mentioned earlier, you can [scrape any site using XPath](/blog/scraping-rss-feeds-using-xpath/).

For example, `=importXML("http://www.imdb.com/chart/top", "//table//table//table//a")` imports the top 250 movies from the [IMDb Top 250](http://www.imdb.com/chart/top). the second parameter says, get all links (a) inside a table inside a table inside a table. This populates a list with the entire Top 250.

[![Google Spreadsheets - ImportXML](/blog/assets/flickr-google-spreadsheets---importxml_2152056088_o-png.webp)](/blog/assets/flickr-google-spreadsheets---importxml_2152056088_o-png.webp "Google Spreadsheets - ImportXML")

Now, against each of these, we could get a feed of Mininova's torrents. Mininova's RSS URL is `http://www.mininova.org/rss/search_string`. So, in cell B1, I can get a torrent for the cell A1 (The Godfather) using the `importFeed` function. (Note: you need to replace spaces with a + symbol. These functions don't like invalid URLs.).

[![Google Spreadsheets - Import Mininova Feed](/blog/assets/flickr-google-spreadsheets---import-mininova-feed_2151264663_o-png.webp)](/blog/assets/flickr-google-spreadsheets---import-mininova-feed_2151264663_o-png.webp "Google Spreadsheets - Import Mininova Feed")

Just copy this formula down to get a torrent against each of the IMDb Top 250 movies!

[Check out the sheet I've created](http://spreadsheets.google.com/ccc?key=poz40xh4E1uen8Pedf01NEQ&hl=en). (You need a Google account to see the sheet. If you don't want have one, you can [view the sheet](http://spreadsheets.google.com/pub?key=poz40xh4E1uen8Pedf01NEQ).)

---

Now, that's still not the best of it. You can extract this file as an RSS feed! Google lets you publish your sheets as HTML, PDF, Text, XLS, etc. and RSS and Atom are included as well. Here's the [RSS feed for my sheet above](http://spreadsheets.google.com/feeds/list/o16705544397998276259.1246737882357952679/od7/public/basic?alt=rss).

Think about it. We now have an application that sucks in data from a web page, does a web-based vlookup on another service, and returns the results as an RSS feed!

There are only two catches to this. The first is that Google has restricted us to 50 import functions per sheet. So you can't really have the IMDb Top 250 populated here -- only the top 49. The second is that the spreadsheet updates only when you open it again. So it's not really a dynamically updating feed. You need to open the spreadsheet to refresh it.

But if you really wanted these things, there's always [Yahoo! Pipes](http://pipes.yahoo.com).

---

## Comments

<!-- wp-comments-start -->

- **Gregory Dillon** _31 Dec 2007 12:00 pm_:
  Hey, thanks. Your page was the most helpful of all. In the example with the movie names, how did you figure out that it was a table x3. or table within table within table.
- **[S Anand](http://www.s-anand.net/)** _30 Mar 2010 9:04 pm_:
  Looks like the IMDb top 250 page format has changed. =importXML("http://www.imdb.com/chart/top", "//div[@id=""main""]//table//font/a") seems to work now.
- **Sintl** _2 Jan 2011 4:24 am_:
  Hi
  Is there a possibility to get selective text from webpage by using import url function.
  =ImportHtml(URL; "list" | "table"; index)
  I want to pull following text Updated Sunday, December 19, 2010 from a html page
  Thnx
- **[Siamak](http://www.thebodyzoom.com)** _26 Aug 2011 11:03 pm_:
  I have an excel file with the name of about 300 businesses that I want to look up their phone numbers or websites. Any idea how I can automate this, rather than type each entry in Google?
  Thanks
- **akc** _30 Jul 2011 11:07 am_:
  Hey
  Very Helpful website it is..........Please help me
  I wan to import data from (http://dsebd.org/latest\_share\_price\_scroll\_l.php ) . to google spreadsheet . I wan to import share price .
  Now tell me which way i will use. I m failed

<!-- wp-comments-end -->
