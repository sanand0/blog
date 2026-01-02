---
title: Monitoring site downtime
date: "2007-12-24T12:00:00Z"
categories:
  - how-i-do-things
wp_id: 71
---

> If something goes wrong with my site, I like to know of it. My top three problems are:
>
> 1. [The site is down](#start1)
> 2. [A page is missing](/blog/handling-missing-pages/)
> 3. [Javascript isn't working](/blog/javascript-error-logging/)
>
> I'll talk about how I manage these over 3 articles.

My site used to go down a lot. Initially that was because I kept playing around with [mod\_rewrite](http://httpd.apache.org/docs/1.3/mod/mod_rewrite.html) and other [Apache modules](http://httpd.apache.org/docs/1.3/mod/) without quite understanding them. I'd make a change and upload it without testing. (I'm like that.) And then I'd go to sleep.

Next morning, the site's down, and has been down all night.

This is a bit annoying. Partly because I couldn't use my site, but mostly because of the **Oh yeah, sorry -- I goofed up last night** replies that I have to send out the next day.

So I started using [Site24x7](http://site24x7.com) to track if my website was down. It's a convenient (and free) service. It pings my site every hour. If it's down, I get an SMS. If it's back up, I get an SMS. It also keeps a history of how often the site is down.

[![Site24x7](/blog/assets/flickr-site24x7_2133283449_o-png.webp)](/blog/assets/flickr-site24x7_2133283449_o-png.webp "Site24x7 by S Anand, on Flickr")

Over time, I stopped making mistakes. But my site still kept going down, thanks to my hosting service ([100WebSpace](http://www.100webspace.com)). When I goof up, it's just an annoyance, and I can fix it. But when my hosting service goes down, it's more than that. My site is where I [listen to music](/hindi), [read comics](/dilbert.html#today), [read RSS feeds](/blog/bookmarks/), [use custom search engines](/searchengines.html), watch movies, browse for books, etc. Not being able to do these things -- nor fix the site -- is suffocating.

Worse, I couldn't sleep. I use my mobile as my alarm. It's annoying to hear an SMS from under your pillow at 3am every day -- especially if it says your site is down.

So I switched to [HostGator](http://www.hostgator.com) a few months ago. Nowadays, the site is down a lot less. (In times of trouble, it becomes sluggish, but doesn't actually go down.)

That came at a cost, though. I was paying 100 WebSpace about $25 per annum. I'm paying Hostgator about $75 per annum. Being the kind that [analyses purchases to death](/blog/how-i-buy-gadgets/), the big question for me was, is this worth it. There is where my other problem with the site being down kicks in. I get a bit of [ad revenue](http://www.google.com/adsense/) from my site, and I lose that when the site's down. (Not that it's much. Still...)

According to Site24x7, my site was up ~98% of the time. So I'm losing about 2% of my potential ad revenue. For the extra $50 to be worth it, my ad revenue needs to be more than $50 / 2% = $2,500 per annum. I'm nowhere near it. So the switch isn't actually a good idea economically, but it does make life convenient (which is pretty important) and I sleep better (much more so).

The important thing, I've realised, is not just to track this stuff. That's useful, sure. But what really made Site24x7 useful to me is that it would **alert me** when there was **a big problem**.

There are many kinds of alerting.

There's a report you can view whenever you remember to view it. (It could be an RSS feed, so at least [you won't have to remember the site](/blog/advanced-google-reader/). But you still need to read your feeds.)

Then there's the more pushy alerting: sending you an e-mail. That may catch you instantly for the half of the day that you're online. Or, if you're like me, it may completely escape your attention. (I don't read e-mail.)

And then there's the equivalent of shaking you by the shoulder -- getting an SMS. (At least, that's how it is for me. Incidentally, I don't reply to SMS either. Calling me gets a reply. Nothing else.)

The **type of alerting is clearly a function of the severity of the problem**. Wake me up when my site goes down. Don't wake me up if a link is broken.

[Site24x7](http://www.site24x7.com/) sends me an SMS when my site is down. Fits the bill perfectly.

---

## Comments

<!-- wp-comments-start -->

- **Arun** _24 Dec 2007 12:00 pm_:
  Thanks for your post on Site24x7. Glad that you liked it! Arun Site24x7
- **Noel** _24 Dec 2007 12:00 pm_:
  You can also try [Dotcom-monitor](http://www.dotcom-monitor.com/). It smart and cheap service

<!-- wp-comments-end -->
