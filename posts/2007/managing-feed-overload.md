---
title: Managing feed overload
date: "2007-12-18T12:00:00Z"
lastmod: "2009-03-08T16:11:40Z"
categories:
  - how-i-do-things
wp_id: 72
---

I have only two problems with Google Reader.

The first is that **it doesn't support authenticated feeds**. Ideally, I'd have liked to have a single reading list that combines my e-mail with newsfeeds. [GMail](http://mail.google.com/) offers RSS feeds of your e-mail. But the feeds require authentication (obviously) and Google Reader doesn't support that right now. (So I usually don't read e-mail :-)

The second is that **it's tough to manage large feeds**. It's a personal quirk, really. I like to read all entries. If there are 100, I read all 100. If there are 1000, I struggle but read all 1000. I'm too scared to "Mark all read" because there are some sources that I don't want to miss.

The 80-20 rule is at work here. There are some prolific writers (like [Scoble](http://scobleizer.com/)) who write many entries a day. There are some prolific sources ([del.icio.us](http://del.icio.us/popular) or [digg](http://www.digg.com/)). I can't keep up with such writers / sources. I don't particularly want to. If I missed one day of [del.icio.us popular items](http://del.icio.us/popular), I'll just read the next day's.

With Google Reader, that makes me uneasy. I don't like having 200 unread items. I don't like to mark them all read.

In such cases, **[popurls](http://popurls.com)' approach is useful**. It shows the top 15-30 entries of the popular sites as a snapshot. Any time you're short of things to read, visit this. If you're busy, don't.

Using Google's [AJAX Feed API](http://code.google.com/apis/ajaxfeeds/), it's quite trivial to build your own feed reader. So I cloned [popurls](http://popurls.com)' layout into my [bookmarks](/news) page, and put in feeds that I like.

You can customise my [bookmarks](/news) page to use your own feeds. Save the page, open it in Notepad, and look for existing feeds. They'll look like this:

```javascript
"hacker news" : {
    entries:15,
    url:"http://news.ycombinator.com/rss"
},
```

The first line ("hacker news") is the title of the feed. You can call it what you want. Set **entries** to the number of feed entries you want to show. Set **url** to the RSS feed URL. Save it, and you have your own feed reader. (If you want to put it up on your site, you may want to change the [Google API key](http://code.google.com/apis/ajaxfeeds/signup.html).)

Try it! Just **[save this page](/news) and edit the feeds**.

---

Here, I must point out three things about Google's [AJAX Feed API](http://code.google.com/apis/ajaxfeeds/) that make it extremely powerful.

The obvious is that is **allows Javascript access** to RSS in a very easy way. That makes it very easy to integrate with any web page.

The second is subtler -- it **includes historical entries**. So even if an RSS feed had only 10 entries, I could pick up the last 100 or 1,000, as long as Google has known about the feed for long enough. This is what makes Google Reader more of a platform rather than a simple feed reader application. **Google Reader is a feed archiver** -- not just a feed reader.

The third (I'm a bit crazy here) is that you can **use it to schedule tasks**. Google's FeedFetcher refreshes feeds every 3 hours or so. If you want to do something every three hours (or some multiple thereof -- say every 24 hours), you can write a program that does what you want, and subscribe to it's output as a feed.

You may notice that I have a [Referrers to s-anand.net](/e/referrers.php) on my [bookmarks](/news) page. These are the sites that someone clicked on to visit my site. I have a PHP application that searches my access log for external referrers. Rather than visit that page every time, I just made an RSS feed out of it and subscribed to it. Every three hours or so, Google accesses the URL. I search my access.log and archives the latest results. So, even after my access.log is trimmed by the server, I have it all on Google Reader to catch up with later.

Since Google doesn't forget to ping, I can schedule some fairly time-critical processes this way. For instance, if I wanted to download each [Dilbert](http://www.dilbert.com/) strip, every day as it arrives, I can create an application that downloads the file and returns a feed entry. Now, **I don't need to remember to run it every day**! I just subscribe to the application on Google Reader, and Google will remind the application to run every 3 hours. (I know -- I could use a crontab, but somehow, I like this.) Plus I would get the Dilbert strip on my feed reader as a bonus.

---

**Update**: Google has just released [PartnerBar](http://www.google.com/uds/solutions/partnerbar/index.html), which is a more flexible way of viewing a snapshot of feeds.
