---
title: Attack of the bots
date: "2008-08-31T12:00:00Z"
categories:
  - how-i-do-things
wp_id: 40
---

<p>One out of every 5 hits to my site is from a <a href="http://en.wikipedia.org/wiki/Internet_bot">bot</a>.</p>
<p>I spent a fair bit of time this weekend analysing my log file for last month (which runs to gigabytes, and I ended up learning a few things about file system optimisation, but more on that later). 80% of the hits were from regular browsers. 20% were from robots. Here's a sample of the user-agents:</p>

```text
Mozilla/5.0 (compatible; Yahoo! Slurp; <a href="http://help.yahoo.com/help/us/ysearch/slurp)">http://help.yahoo.com/help/us/ysearch/slurp)</a>
Mozilla/5.0 (compatible; Googlebot/2.1; +<a href="http://www.google.com/bot.html)">http://www.google.com/bot.html)</a>
Mediapartners-Google
DotBot/1.0.1 (<a href="http://www.dotnetdotcom.org/#info">http://www.dotnetdotcom.org/#info</a>, crawler@dotnetdotcom.org)
Mozilla/5.0 (Twiceler-0.9 <a href="http://www.cuill.com/twiceler/robot.html)">http://www.cuill.com/twiceler/robot.html)</a>
msnbot/1.1 (+<a href="http://search.msn.com/msnbot.htm)">http://search.msn.com/msnbot.htm)</a>
FeedBurner/1.0 (<a href="http://www.FeedBurner.com)">http://www.FeedBurner.com)</a>
Mozilla/5.0 (compatible; attributor/1.13.2 +<a href="http://www.attributor.com)">http://www.attributor.com)</a>
WebAlta Crawler/2.0 (<a href="http://www.webalta.net/ru/about_webmaster.html)">http://www.webalta.net/ru/about_webmaster.html)</a> (Windows; U; Windows NT 5.1; ru-RU)
Yandex/1.01.001 (compatible; Win16; I)
...
```

<p>You get the idea. The bulk of these are search engines. Over two-thirds of the bot requests were from <a href="http://help.yahoo.com/l/us/yahoo/search/webcrawler/">Yahoo Slurp</a>. Now, this struck me as weird. If I take the top 3 search engines that are sending traffic my way, </p>
<table><tbody>
<tr><td>&#160;</td><td>Referral %</td><td>Crawl %</td></tr>
<tr><td><a href="http://www.google.com/">Google</a></td><td>90%</td><td>24%</td></tr>
<tr><td><a href="http://search.yahoo.com/">Yahoo</a></td><td>6%</td><td>66%</td></tr>
<tr><td><a href="http://search.live.com/">Microsoft</a></td><td>3%</td><td>0.3%</td></tr>
<tr><td>Others</td><td>1%</td><td>9%</td></tr>
</tbody></table>
<p>The search engine that sends me the most traffic is being reasonably conservative, while Yahoo is just eating up the bandwidth on my site. Actually, this shouldn't bother me too much. It's not taking up too much bandwidth, or even CPU usage, given that all the bots put together make up only 20% of my traffic. But somehow... it's sub-optimal. Inelegant, even.</p>
<p>So I decided to take a closer look. Just how often are they crawling my site?</p>
<table><tbody>
<tr><td><a href="http://search.yahoo.com/">Yahoo</a></td><td><b><i>Every 5 seconds</i></b></td></tr>
<tr><td><a href="http://www.google.com/">Google</a></td><td>Every 13 seconds</td></tr>
<tr><td><a href="http://www.dotnetdotcom.org/#info">DotBot</a></td><td>Every 9 minutes</td></tr>
<tr><td><a href="http://www.cuill.com/twiceler/robot.html">Cuill</a></td><td>Every 9 minutes</td></tr>
<tr><td><a href="http://search.live.com/">Microsoft</a></td><td>Every 18 minutes</td></tr>
<tr><td><a href="http://www.FeedBurner.com">Feedburner</a></td><td>Every 18 minutes</td></tr>
<tr><td><a href="http://www.attributor.com/">Attributor</a></td><td>Every 23 minutes</td></tr>
<tr><td><a href="http://www.yandex.ru/">Yandex</a></td><td>Every 27 minutes</td></tr>
</tbody></table>
<p>Look at those numbers. Yahoo is hitting my site once <b><i>every 5 seconds</i></b>. No wonder there's a help page at Yahoo titled <a href="http://help.yahoo.com/l/us/yahoo/search/webcrawler/slurp-03.html">How can I reduce the number of requests you make on my web site?</a> I followed their advice and set the crawl-delay to 60, so at least it slows down to once a minute. </p>
<p>Just that one little line change should (hopefully) reduce the load on my site by around 15%.</p>
<p>As for the other engines, I don't mind that much in terms of load.</p>
<ul>
  <li>Google, for all that it crawls every 13 seconds, has faithfully reported that it has only 11% of my site under its index, so I've no idea what they're doing, but I'm not complaining about the traffic that's coming my way.</li>
  <li><a href="http://www.dotnetdotcom.org/#info">DotBot</a>. Today was the first I'd heard of them. Visited the site, and smiled. These guys can do all the crawling of my site that they like, and I hope something interesting comes out of their work.</li>
  <li><a href="http://www.cuill.com/twiceler/robot.html">Cuill</a>, sends me 0.2% of my traffic, but it's a new search engine, I'm happy to give it time.</li>
  <li><a href="http://search.live.com/">Microsoft</a>'s OK, sends me a tiny stream of traffic.</li>
  <li><a href="http://www.FeedBurner.com">Feedburner</a> is just pinging my RSS feed every 18 minutes. </li>
  <li><a href="http://www.attributor.com/">Attributor</a> and <a href="http://www.yandex.ru/">Yandex</a> I'm hearing of for the first time, again. Not too much load on a system, so that's OK.</li>
</ul>
<hr />
<p>What's amazing is the sheer number of bots out there. Last month, I counted over 600 distinct <a href="http://en.wikipedia.org/wiki/User_agent">user-agent</a> strings just representing bots. So it's true. The Web is <a href="http://en.wikipedia.org/wiki/Semantic_web#Purpose">no longer just for humans</a>. We do need a <a href="http://en.wikipedia.org/wiki/Semantic_Web">Semantic Web</a>.</p>

---

## Comments

<!-- wp-comments-start -->

- **Dhar** _31 Aug 2008 9:09 pm_:
  Hmmm, curious as to:

  1. Why the bots should crawl your site every 5 seconds or so?
  2. How you can find out how much of your site has been indexed by Google.

  Cheers,
  D.
- **S Anand** _1 Sep 2008 12:11 am_:
  1. I think Yahoo's crawler is aggressive in any case. My site doesn't seem to be an exception: there are a lot of threads discussing this problem.
  2. Google's webmaster tools tells you how many URLs have been indexed from your sitemap.

<!-- wp-comments-end -->
