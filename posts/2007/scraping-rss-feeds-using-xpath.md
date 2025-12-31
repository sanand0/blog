---
title: Scraping RSS feeds using XPath
date: "2007-12-17T12:00:00Z"
lastmod: "2009-03-07T10:32:19Z"
categories:
  - coding
  - how-i-do-things
wp_id: 73
---

<p>If a site doesn't have an RSS feed, your simplest option is to use <a href="http://www.page2rss.com/">Page2Rss</a>, which gives a feed of what's changed on a page.</p>
<p>My needs, sometimes, are a bit more specific. For example, I want to track new movies on the <a href="http://www.imdb.com/chart/top">IMDb Top 250</a>. They don't offer a feed. I don't want to track all the other junk on that page. Just the top 250.</p>
<p>There's a standard called <a href="http://www.w3.org/TR/1999/REC-xpath-19991116">XPath</a>. It can be used to search in an HTML document in a pretty straightforward way. Here are some examples:</p>
<table>
<tr>
<td><b>//a</b></td>
<td>Matches all &lt;a&gt; links</td>
</tr>
<tr>
<td><b>//p/b</b></td>
<td>Matches all &lt;b&gt; bold items in a &lt;p&gt; para. (the &lt;b&gt; must be immediately under the &lt;p&gt;)</td>
</tr>
<tr>
<td><b>//table//a</b></td>
<td>Matches all links inside a table (the links need not be immediately inside the table -- anywhere inside the table works)</td>
</tr>
</table>
<p>You get the idea. It's like a folder structure. / matches the a tag that's immediately below. // matches a tag that's somewhere below. You can play around with XPath using the <a href="https://addons.mozilla.org/en-US/firefox/addon/1095">Firefox XPath Checker</a> add-on. Try it -- it's much easier to try it than to read the documentation.</p>
<p>The following XPath matches the <a href="http://www.imdb.com/chart/top">IMDb Top 250</a> exactly.</p>

```xpath
//tr//tr//tr//td[3]//a
```

<p>(It's a link inside the 3rd column in a table row in a table row in a table row.)</p>
<p>Now, all I need is to get something that converts that to an RSS feed. I couldn't find anything on the Web, so I wrote my own <a href="/xpath">XPath server</a>. The URL:</p>
<blockquote><p><a href="/xpath?url=http://www.imdb.com/chart/top&#038;xpath=//tr//tr//tr[position()&gt;1]//td[3]//a">www.s-anand.net/xpath?<br />url=http://www.imdb.com/chart/top&#038;<br />xpath=//tr//tr//tr//td[3]//a</a></p>
</blockquote>
<p>When I subscribe to this URL on <a href="http://reader.google.com/">Google Reader</a>, I get to know whenever there's a new movie on the IMDb Top 250.</p>
<p>This gives only the names of the movies, though, and I'd like the links as well. The <a href="/xpath">XPath server</a> supports this. It accepts a root XPath, and a bunch of sub-XPaths. So you can say something like:</p>
<blockquote><p><a href="/xpath?url=http://www.imdb.com/chart/top&#038;xpath=//tr//tr//tr[position()&gt;1] title-&gt;./td[3]//a link-&gt;./td[3]//a/@href">xpath=//tr//tr//tr title-&gt;./td[3]//a link-&gt;./td[3]//a/@href</a></p>
</blockquote>
<p>This says three things:</p>
<table>
<tr>
<td><b>//tr//tr//tr</b></td>
<td>Pick all rows in a row in a row</td>
</tr>
<tr>
<td><b>title->./td[3]//a</b></td>
<td>For each row, set the title to the link text in the 3rd column</td>
</tr>
<tr>
<td><b>link->./td[3]//a</b></td>
<td>... and the link to the link href in the 3rd column</td>
</tr>
</table>
<p>That provides a more satisfactory RSS feed -- one that I've subscribed to, in fact. Another one that I track is a list of <a href="/xpath?url=http://www.mininova.org/cat-list/4/seeds/&#038;xpath=//tr/td[2]/a[not(img)] title->. link->./@href">new popular movies</a> that make it to the <a href="http://www.mininova.org/cat-list/4/seeds/">mininova top seeded movies</a> category.</p>
<p>You can whiff up more complex examples. Give it a shot. Start simple, with something that works, and move up to what you need. Use <a href="https://addons.mozilla.org/en-US/firefox/addon/1095">XPath Checker</a> liberally. Let me know if you have any isses. Enjoy!</p>

---

## Comments

<!-- wp-comments-start -->

- **Mark** _17 Dec 2007 12:00 pm_:
  Have you ever thought about introducing authentication to the XPath server? I would like to parse certain fields of a page that is authenticated with cookies.
- **Rog** _28 Oct 2008 1:07 am_:
  Any chance you could share your xpath.php code? It seems the server is no longer available.
- **S Anand** _28 Oct 2008 1:43 am_:
  Sure Rog. I've mailed it to you
- **[S Anand](http://www.s-anand.net/)** _7 Mar 2009 10:35 am_:
  Post Yahoo's introduction of [Yahoo Query Language](http://developer.yahoo.com/yql/), you're much better off using that instead of my XPath utility. I've covered it in this article on [client side scraping](http://www.s-anand.net/blog/client-side-scraping/).
- **[Scraping your way to RSS Feeds! &laquo; Technosiastic!](http://technosiastic.wordpress.com/2009/04/08/scraping-your-way-to-rss-feeds/)** _8 Apr 2009 10:16 am_ _(pingback)_:
  [...] another gem I figured which actually lets you run XPath query for scraping into a web page for RSS. It can be [...]
- **Bart P** _3 Mar 2012 11:48 am_:
  It would be great if you could share this code, I really like to use this server, but want to remove session ids from the links (so my reader doesn't think all links are new every time).
  Is that possible? :)
- **Ben** _11 Jun 2015 12:46 am_:
  Is that possible to share your xpath.php code? yahoo pipes is going to be shut down :(

<!-- wp-comments-end -->
