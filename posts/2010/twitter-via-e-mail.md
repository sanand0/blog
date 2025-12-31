---
title: Twitter via e-mail
date: "2010-10-26T17:24:45Z"
lastmod: "2010-10-27T09:26:09Z"
categories:
  - how-i-do-things
  - tools
wp_id: 2548
---

Since I don’t have Internet access on my BlackBerry (because [I’m in prison](/blog/you-are-in-prison/)), I’ve had a pretty low incentive to use [Twitter](http://twitter.com/). Twitter’s really handy when you’re on the move, and over the last year, there were dozens of occasions where I really wanted to tweet something, but didn’t have anything except my BlackBerry on hand. Since T-Mobile doesn’t support [Twitter via SMS](http://support.twitter.com/articles/14226-how-to-find-your-twitter-short-code), e-mail is my only option, and I haven’t been able to find a decent service that does what I want it to do.

So, obviously, I wrote one this weekend: [Mixamail.com](http://www.mixamail.com/).

I’ve kept it as simple as I could. If I send an email to [twitter@mixamail.com](mailto:twitter@mixamail.com), it replies with the latest tweets on my Twitter home page. If I mail it again, it replies with new tweets since the last email.

I can update my status by sending a mail with “Update” as the subject. The first line of the body is the status.

I can reply to tweets. The tweets contain a “reply” link that opens a new mail and replies to it.

I can subscribe to tweets. Sending an email with “subscribe” as the subject sends the day’s tweets back to me every day at the same hour that I subscribed. (I’m keeping it down to daily for the moment, but if I use it enough, may expand it to a higher frequency.)

Soon enough, I’ll add re-tweeting and (update: added retweets on 27 Oct) a few other things. I intend keeping this free. Will release the source as well once I document it. [The source code is at Github](https://github.com/sanand0/mixamail).

Give it a spin: [Mixamail.com](http://www.mixamail.com/). Let me know how it goes!

---

For the technically minded, here are a few more details. I spent last night scouting for a small, nice, domain name using [nxdom](http://www.nxdom.com/). I bought it using [Google Apps](http://www.google.com/apps/intl/en/group/index.html) for $10. The application itself is written in [Python](http://www.python.org/) and hosted on [AppEngine](http://appengine.google.com/). I use the [Twitter API](http://dev.twitter.com/) via [OAuth](http://github.com/Arachnid/AppEngine-OAuth-Library) and store the user state via [Lilcookies](http://github.com/thrivesmart/prayls/blob/master/prayls/lilcookies.py). The HTML is based on [html5boilerplate](http://github.com/paulirish/html5-boilerplate), and has no images.

---

## Comments

<!-- wp-comments-start -->

- **[Jayson](http://www.jaysonjc.com)** _26 Oct 2010 6:41 pm_:
  Pretty neat work! What was the time taken for this to be done?
- **[S Anand](http://www.s-anand.net/)** _26 Oct 2010 6:46 pm_:
  Let's see... 5 hours on Sunday to get the Twitter API working... 4 hours yesterday to get the user management sorted... about 5 hours today to get the UI done. About 14 hours so far.
- **[Aravinda](http://aravindavk.in)** _26 Oct 2010 6:52 pm_:
  Very nice app :)
- **Praveen** _26 Oct 2010 8:03 pm_:
  Awesome app.
- **[pgt](http://posterous?)** _27 Oct 2010 11:25 pm_:
  have you checked out posterous.com , they do twitter among other things
- **Rockey** _27 Oct 2010 11:31 pm_:
  Tussi Great ho !
- **Amitesh** _2 Nov 2010 7:23 am_:
  Hey,
  I am not a techie but this application looks sure value to me.
  Great work!

<!-- wp-comments-end -->
