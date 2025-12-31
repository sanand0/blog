---
title: The hunt for a Twitter client
date: "2008-11-21T12:00:00Z"
categories:
  - how-i-do-things
wp_id: 23
---

I hadn't jumped on to the [Twitter](http://www.twitter.com/) bandwagon for a while. I'm not much of a conversationalist, nor am I a very sociable. I also tend to stay away from social networks. But I figured I would try Twitter out for a while, mostly because it's an outlet for short comments. For long articles, I have my blog. For sharing links, I have [Google Reader](http://www.google.com/reader/shared/16836184467750910501) and [del.icio.us](http://del.icio.us/sanand0). I don't quite have anything for that occasional moment when I [want to say](http://twitter.com/sanand0/status/1011863752), "Hey! A great way to shred mint leaves is to **freeze** them!"

The question is what client to use. I wanted something free, portable and featherweight (as in lighter than lightweight: no additional memory usage.)

SMS is the classic Twitter channel. But I don't like being bothered by SMS messages often. Besides, it's not free. So that's out.

The next best would be e-mail via my BlackBerry. The problem is, Twitter doesn't accept tweets via e-mail. So when looking for alternatives, I found [Identi.ca](http://identi.ca/), which is even better than Twitter except for the fact that it doesn't have Twitter's user base. Anyway, it accepted e-mail, so that was fine.

On the desktop, the browser is the obvious choice. But somehow, going to the [Twitter home page](http://twitter.com/home) and typing out a tweet felt so... Web 1.0. I didn't fashion installing a client just for tweeting, like [Twhirl](http://www.twhirl.org/). The closest was instant messenger software. Since [Identi.ca accepts messages via XMPP](http://laconi.ca/trac/wiki/Documentation#usageXMPP), I could install [Google Talk](http://talk.google.com/) and send messages via instant messenger.

That worked for a couple of weeks. Then I pulled out. Instant messenger has the disadvantage of making you accessible, and I honestly don't have the time. Plus, I don't fancy running apps persistently, not even something as light as Google Talk. So back to square one.

In the meantime, I was having another problem with sending updates via BlackBerry. My corporate mails have a [HUGE disclaimer](http://identi.ca/notice/238449) attached to them. Doesn't make sense to have 140 character message followed by a 940 character disclaimer. I'd have to get rid of those anyway.

After a bit of digging around, I came across mail handlers. I can write a program on [my server](http://www.s-anand.net/) to handle mails. So I wrote one that strips out the disclaimer and forwards it to my identi.ca e-mail ID. (Now I've modified it to use the [API](http://laconi.ca/trac/wiki/API).) So that solves my mobile twittering problem.

It also solves my cross-posting problem. I maintain a [twitter.com/sanand0](http://twitter.com/sanand0) and an [identi.ca/sanand0](http://identi.ca/sanand0) account and keep them updated in parallel. My mail handler updates the post on both services.

As for the desktop, I have the best solution of all. I use the browser address bar to twitter. I've created a keyword search with the keyword "twitter" with is keyed to a URL like `http://www.s-anand.net/twitter/%s`. So if I say "twitter Some message" on the address bar and press enter, it contacts the server, which updates Identi.ca and Twitter using the API.

Of course, you don't really need to do that to update Twitter. Just create a keyword search with a keyword "twitter" and a URL `http://twitter.com/home?status=%s`, and you're done. Remember: you can create keyword searches in Internet Explorer as well ([read how](/Keyword_searches_as_a_Web_command_line.html)). With this, you can update twitter from the address bar by just typing "twitter your message goes here".

---

Anyway, that was a long-winded way of saying just two things.

1. Mail handlers are cool.
2. [Keyword searches](/Keyword_searches_as_a_Web_command_line.html) let you update Twitter from the address bar using the URL `http://twitter.com/home?status=%s`

---

## Comments

<!-- wp-comments-start -->

- **Ashish** _21 Nov 2008 11:32 am_:
  Did you try Twitterbar extension in Firefox?
- **Kiran** _22 Nov 2008 1:32 pm_:
  Twitterfox - nice, and unobtrusive enough browser extension. Twitterbar - does the stuff you mentioned as part of the keyword-searches experiment
- **S Anand** _23 Nov 2008 2:10 am_:
  Thanks Ashish, Kiran -- didn't know about those. Except, I've moved to Google Chrome\
  these days (mostly for its memory management). But will get back to trying\
  these once Firefox 3.10 is out of Beta,
- **somnath** _1 Dec 2008 2:40 am_:
  As usual you have come up with something cool and original :) I am still using web for Tweeting ... TweetDeck did not work for me checking Twhirl now
- **Vivek Sonny Abraham** _6 Dec 2008 9:20 am_:
  Or you could use TwitterBerry (http://www.orangatame.com/products/twitterberry/)
- **Sai** _8 Dec 2008 9:50 pm_:
  :) good post! I finally got on to the social network bandwagon myself last year and found the experience quite enjoyable. Biggest benefit was obviously the ability to connect with old friends. Use twitter as well, but not as much. Hope all's well.

<!-- wp-comments-end -->
