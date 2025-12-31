---
title: Client side scraping for contacts
date: "2009-03-06T17:01:56Z"
lastmod: "2009-03-09T08:17:08Z"
categories:
  - coding
wp_id: 2292
---

By curious coincidence, just a day after my post on [client side scraping](/blog/client-side-scraping/), I had a chance to demo this to a client. They were making a contacts database. Now, there are two big problems with managing contacts.

1. Getting complete information
2. Keeping it up to date

Now, people happy to fill out information about themselves in great detail. If you look at the public profiles on [LinkedIn](http://www.linkedin.com/), you’ll find enough and more details about most people.

Normally, when getting contact details about someone, I search for their name on Google with a “site:linkedin.com” and look at that information.

**Could this be automated?**

I spent a couple of hours and came up with a primitive [contacts scraper](/get-contacts.html). Click on the link, type in a name, and you should get the LinkedIn profile for that person. (**Caveat**: It’s very primitive. It works only for specific URL public profiles. Try ‘Peter Peverelli’ as an example.)

It uses two technologies. [Google AJAX Search API](http://code.google.com/apis/ajaxsearch/) and [YQL](http://developer.yahoo.com/yql/). The `search()` function searches for a phrase…

```javascript
google.load("search", "1");
google.setOnLoadCallback(function() {
  gs = new google.search.WebSearch();
  $("#getinfo").show();
});

function search(phrase, fn) {
  gs.setSearchCompleteCallback(gs, function() {
    fn(this.results);
  });
  gs.execute(phrase);
}
```

… and the `linkedin()` function takes a LinkedIn URL and extracts the relevant information from it, using XPath.

```javascript
function scrape(url, xpath, fn) {
  $.getJSON("http://query.yahooapis.com/v1/public/yql?callback=?", {
    q: "select * from html where(url=\""
      + url + "\" and xpath=\"" + xpath + "\")",
    format: "json",
  }, fn);
}

function linkedin(url, fn) {
  scrape(url, "//li[@class][h3]", fn);
}
```

So if you wanted to find Peter Peverelli, it searches on Google for “[Peter Peverelli site:linkedin.com](http://www.google.com/search?q=Peter+Peverelli+site%3Alinkedin.com)” and picks the first result.

From this result, it displays all the `<LI>` tags which have a class and a `<H3>` element inside them (that’s what the `//li[@class][h3]` XPath does).

The real value of this is in bulk usage. When there’s a big list of contacts, you don’t need to scan each of them for updates. They can be automatically updated — even if all you know is the person’s name, and perhaps where they worked at some point in time.

---

## Comments

<!-- wp-comments-start -->

- **[Thejesh GN &raquo; RSS Feed Aamir Khans blog using YQL and Pipes](http://thejeshgn.com/2009/03/09/rss-feed-aamir-khans-blog-using-yql-and-pipes/)** _9 Mar 2009 2:44 pm_ _(pingback)_:
  [...] Blog to create a feed. I had written custom scraping code to create the feed.Today after reading Anand’s blog I parsed the blog using YQL and created the feed using Pipes. Using YQL/PIPE much easier thank [...]
- **Prakash** _8 Mar 2009 1:50 pm_:
  Have you tried xobni add-in for outlook (incase you use that to manage contacts)?
- **[S Anand](http://www.s-anand.net/)** _8 Mar 2009 4:07 pm_:
  I don't use it myself, but have tried it — and interestingly enough, recommended it to this client.
- **[Thejesh GN](http://thejeshgn.com)** _9 Mar 2009 2:46 pm_:
  After reading this post. [I redid Aamir Khans blog parsing](http://thejeshgn.com/2009/03/09/rss-feed-aamir-khans-blog-using-yql-and-pipes/) using YQL and Pipes.
  It was very easy as YQL was available as module inside Pipes.
- **Vasanth Asokan** _18 Dec 2010 6:05 am_:
  Hi Anand,
  The scraper demo does not seem to be working (I tried the value you suggested as well 'Peter Peverelli'. Can you take a look?
- **[S Anand](http://www.s-anand.net/)** _18 Dec 2010 10:42 am_:
  True, Vasanth. Honestly, scraping was only ever useful as a temporary strut until service providers opened up the data. It required too much maintenance anyway. With LinkedIn's API, this is outdated, and I'm planning to leave it as it is. But thanks for pointing this out!

<!-- wp-comments-end -->
