---
title: The scary Internet
date: "2013-06-03T06:29:32Z"
lastmod: "2013-06-03T07:59:56Z"
categories:
  - how-i-do-things
wp_id: 2848
---

I’m not that difficult to scare, and this log message certainly didn’t help:

```
ip223.hichina.com [223.4.183.127] failed - POSSIBLE BREAK-IN ATTEMPT!
```

That’s the message I saw – one thousand five hundred and seventy times yesterday in /var/log/auth.log on one of my Amazon EC2 instances.
Someone, presumably from China, has been patiently trying out a variety of SSH keys to log into this system.
These were grouped as batches. There were exactly 314 attempts at 8am yesterday, then 314 at 12noon, then 314 at 4pm, then 314 at 8pm, then 232 at 3am today. (All times are in UTC – that is, UK time without daylight saving). Every burst took 9 minutes to run through all 314 attempts.
The worst part was, when I tried using SSH this morning, I wasn’t able to log in. (It turned out that I had made a configuration error, but this is the sort of thing that gets me quite worried.)
Perhaps I shouldn’t be complaining. I’ve written enough scrapers to make most webmasters cringe at their logs. I remember a few years ago, when I was working on a project at Tesco, and was scraping bestsellers lists from most sites. (Here’s a [blog post](/blog/dear-tesco-your-books-are-expensive/) about it.) We were putting together a prototype to see how real-time competitive pricing could help.
The scraper was a pretty mild one. It would visit a hundred links, roughly at the pace of one a second. No images were loaded, of course, just the HTML.
One fine day, a few weeks after this had started, I got a call from Andy.
“Hi Anand, are you running any scrapers on our books website?”
“Yes, why?”
“Oh! The site’s very slow. Could you shut it down immediately?”
Turns out that not a single page on the site loaded, and it had almost crawled to a halt. Now, obviously, my little 100-page script could hardly cause damage, but it’s easy to understand their reactions. **No unauthorised scraping!** After a few days of trying to figure out what the problem was, they increased the memory and things went back to normal. Not a bad solution, actually – throw hardware at the problem, and if it vanishes, it’s probably the cheapest solution.
But anyway, I’m sure it’s some nice chap who’s just curious to know what I’ve got on my servers. I’d be happy to share some of it. And even if it’s not so nice a chap, there’s little that I can do, is there?
**Update (1pm India, 3rd June)**: Actually, I now realise that this has been happening ever four hours since May 29th, as regular as a clockwork. Wish I knew enough UNIX programming to pull a prank...

---

## Comments

<!-- wp-comments-start -->

- **[Rajeev](http://www.allassignmenthelp.com)** _23 Dec 2013 2:54 pm_:
  The unwanted trial to login and break in very common on the blogs and the websites that provides a login account. I had many such problems initially and I block such IP's every time once I notice there is something going on which is not expected. I loved your blog.
  Thanks
  Rajeev
- **[Amit Chakradeo](http://amit.chakradeo.net/)** _3 Jun 2013 8:38 pm_:
  That is not necessarily an actual break-in attempt. SSH prints that if the reverse name lookup on the ip address does not resolve back to the same IP address.
  Some pointers to address these things:
  1. Run ssh on non-standard port. (this kills 90% of people trying dictionary passwords out for root).
  2. Prevent root login for ssh and disable password authentication (use keys only)
  3. Run denyhosts which denies known bad IP's and hosts trying to exploit your box.
- **Gopal** _3 Jun 2013 8:06 am_:
  Now you know why US is getting angry with china! :-)
  Anyways as you know it might be to put in some malware for DDOS bot attacks?
- **[Thejesh GN](http://thejeshgn.com)** _4 Jun 2013 10:23 am_:
  I use DenyHosts (http://denyhosts.sourceforge.net/) on all my servers. It blacklists ip addresses trying to brute force. Its easy to setup and run.
  I can see that the script blacklists at least one IP everyday.

<!-- wp-comments-end -->
