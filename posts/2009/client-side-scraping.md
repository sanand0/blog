---
title: Client side scraping
date: "2009-03-04T18:00:57Z"
lastmod: "2009-03-09T08:21:36Z"
categories:
  - coding
wp_id: 2289
---

“Scraping” is extracting content from a website. It’s often used to build something on top of the existing content. For example, I’ve built a site that [tracks movies on the IMDb 250](http://250.s-anand.net/) by scraping content.

There are libraries that simplify [scraping](http://en.wikipedia.org/wiki/Web_scraping) in most languages:

- Perl: [WWW::Mechanize](http://www.perl.com/pub/a/2003/01/22/mechanize.html)
- Python: [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/)
- Ruby: [HPricot](http://wiki.github.com/why/hpricot)
- PHP: [XPath](http://rainbowhatseo.fallenray.com/php5/php5-screen-scraping-with-dom-and-xpath/) (built-in)
- Javascript: [jQuery](http://www.jquery.com/) on [env.js](http://ejohn.org/projects/bringing-the-browser-to-the-server/) on [Rhino](http://www.mozilla.org/rhino/)

But all of these are on the server side. That is, the program scrapes from **your machine**. Can you write a web page where the **viewer’s machine** does the scraping?

Let’s take an example. I want to display [Amazon's bestsellers](http://www.amazon.com/gp/bestsellers/books/) that cost less than $10. I could write a program that scrapes the site and get that information. But since the list updates hourly, I’ll have to run it every hour.

That may not be so bad. But consider Twitter. I want to display the latest iPhone tweets from `http://search.twitter.com/search.atom?q=iPhone`, but the results change so fast that your server can’t keep up.

Nor do you want it to. Ideally, your scraper should just be Javascript on your web page. Any time someone visits, their machine does the scraping. The bandwidth is theirs, and you avoid the [popularity tax](http://www.codinghorror.com/blog/archives/000044.html).

This is quite easily done using [Yahoo Query Language](http://developer.yahoo.com/yql/). YQL converts the web into a database. All web pages are in a table called `html`, which has 2 fields: `url` and `xpath`. You can get IBM’s home page using:

`select * from html where url="http://www.ibm.com"`

Try it at [Yahoo’s developer console](http://developer.yahoo.com/yql/console/). The whole page is loaded into the `query.results` element. This can be retrieved using [JSONP](http://en.wikipedia.org/wiki/JSONP#JSONP). Assuming you have jQuery, try the following on [Firebug](http://getfirebug.com/). You should see the contents of IBM’s site on your page.

```javascript
$.getJSON(
  "http://query.yahooapis.com/v1/public/yql?callback=?",
  {
    q: "select * from html where url=\"http://www.ibm.com\"",
    format: "json",
  },
  function(data) {
    console.log(data.query.results);
  },
);
```

That’s it! Now, it’s pretty easy to scrape, especially with [XPath](http://www.w3.org/TR/xpath). To get the links on IBM’s page, just change the query to

`select * from html where url="http://www.ibm.com" and xpath="//a"`

Or to get all external links from IBM's site:

`select * from html where url="http://www.ibm.com" and xpath="//a[not(contains(@href,'ibm.com'))][contains(@href,'http')]""`

Now you can display this on your own site, using [jQuery](http://www.jquery.com/).

This leads to interesting possibilities, such as [Map-Reduce in the browser](http://ajaxian.com/archives/map-reduce-in-the-browser). Here’s one example. Each movie on the IMDb (e.g. [The Dark Knight](http://www.imdb.com/title/tt0468569/)) comes with a list of recommendations (like [this](http://www.imdb.com/title/tt0468569/recommendations)). I want to build a repository of recommendations based on the [IMDb Top 250](http://www.imdb.com/chart/top). So here’s the algorithm. First, I’ll get the IMDb Top 250 using:

`select * from html where url="http://www.imdb.com/chart/top" and xpath="//tr//tr//tr//td[3]//a"`

Then I’ll get a random movie’s recommendations like this:

`select * from html where url="http://www.imdb.com/title/tt0468569/recommendations" and xpath="//td/font//a[contains(@href,'/title/')]"`

Then I’ll send off the results to my aggregator.

Check out the full code at <http://250.s-anand.net/build-reco.js>.

In fact, if you visited [my IMDb Top 250 tracker](http://250.s-anand.net/), **you already ran this code**. You didn’t know it, but you just shared a bit of your bandwidth and computation power with me. (Thank you.)

And, if you think a little further, here another way of monetising content: by borrowing a bit of the user’s computation power to build complex tasks. There already are [startups](http://www.pluraprocessing.com/) built around this concept.

---

## Comments

<!-- wp-comments-start -->

- **[Aravinda](http://aravindavk.in)** _4 Mar 2009 7:20 pm_:
  Great!
- **Sriram** _4 Mar 2009 10:51 pm_:
  Thank u anand. Nice Information.
- **Rishi** _5 Mar 2009 8:19 am_:
  Awesome... This is the future
- **[grep imdb part 2 ? &laquo; taeyoungchoon](http://taeyoungchoon.wordpress.com/2009/03/26/grep-imdb-part-2/)** _26 Mar 2009 1:16 pm_ _(pingback)_:
  [...] http://www.s-anand.net/blog/client-side-scraping/ [...]
- **Khair** _26 May 2009 4:10 pm_:
  Many thanks for your efforts in simplifying the 'scraping'.
- **[Venkat](http://www.venkatsworld.com)** _16 Nov 2010 1:40 pm_:
  Hey Anand,
  Thanks. This post is really useful. I have managed to scrape Amazon wishlist using this technique (http://www.venkatsworld.com/WIP/JSON\_amazon.html) However YQL seems to be taking some time to respond. I am not sure if you experienced this.I did a similar exercise with Picasa JSON feed and a Jquery plug-in for image scrolling. It works well there too.
- **[Zheka](http://news.ycombinator.com/item?id=4066478)** _17 Jun 2012 8:35 pm_:
  Interesting article! There is another powerful scraping technology available that offers Javascript, jQuery, CSS, and XPath instead of XPath-only. It's called Bobik (http://usebobik.com). The is a cool example of scraping restaurant menus using Bobik at http://news.ycombinator.com/item?id=4066478.
- **LAvesh** _12 Mar 2013 11:19 pm_:
  Hey Anand,
  Great Article. Just one query though in the client side implementation its the client IP that will be hitting the website (in your case www.ibm.com)? or it will use yahoo SQL server IP to hit.

<!-- wp-comments-end -->
