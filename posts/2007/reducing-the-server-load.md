---
title: Reducing the server load
date: "2007-06-06T12:00:00Z"
lastmod: "2009-02-25T08:59:13Z"
categories:
  - how-i-do-things
wp_id: 80
---

I'm been using a shared hosting service with [100 WebSpace](http://www.100ws.com/) over the last 7 years. It's an ad-free account that offers 100MB of space and 3GB of bandwidth per month. Things were fine until two months ago, which was when my [song search engines](/hindi) started attracting an audience. I had anticipated that I might run out of bandwidth, so I used a [different server](http://www.freehostia.com/) (that has 5GB of bandwidth per month quota) for loading the songs. But what I didn't anticipate whas that **my server load would run over the allotted CPU limit**.

You'd think this is unusual, given how cheap computing power is, and that I'd run out of bandwidth quicker. But no. My allotted limit was 1.3% of CPU usage (whatever that meant), and about 2 months ago, I hit 1.5% a few times. I upgraded my account to one which had a 2.5% limit immediately, but the question was: **why did this happen?**

**This blog uses a lot of Perl scripts**. I store all articles on a MySQL database. Every time a link is requested, I dynamically generate the HTML by pulling up the article from the MySQL database and formatting the text based on a template.

[![Schematic of how my website displays pages](/blog/assets/flickr-schematic-of-how-my-website-displays-pages_533687183_o-gif.webp)](/blog/assets/flickr-schematic-of-how-my-website-displays-pages_533687183_o-gif.webp)

I also use MySQL to store users' comments. Every time I display each page, I also pull out the comments related to that page.

**I can't store the files directly as HTML because I keep changing the template**. Every time I change the template, I have to regenerate all the files. If I do that on my laptop and upload it, I consume a lot of bandwidth. If I do that on the server, I consume a lot of server CPU time.

Anyway, since I'd upgraded my account, I thought things would be fine. Two weeks ago, I hit the 2.5% limit as well. No choice. Had to do something.

If you read the [O'Reilly Radar Database War Stories](http://www.google.co.uk/search?&q=o%27reilly+database+war+stories), you'll gather that **databases are great for queries, joins and the like, while flat files are better to process large volume data as a batch**. Since page requests come one by one, and I don't need to do much batch processing, I'd gone in for a MySQL design. **But there's a fair bit of overhead to each databasse query**, and that's the key problem. Perl takes a while to load (and I suspect my server is not using [mod\_perl](http://perl.apache.org/)). The [DBI module](http://dbi.perl.org/) takes a while to load. Connecting to MySQL takes a while. (The query itself, though, is quite fast.)

So **I moved to flat files instead**. Instead of looking up from a database, I just look up a test file using [grep](http://en.wikipedia.org/wiki/Grep). (I don't use Perl's regular expression matching because [regular expression matching in UNIX is faster than in Perl](http://swtch.com/~rsc/regexp/regexp1.html).) I have a 1.6MB text file that contains all my blog entries.

But looking up a 1.6MB text file takes a while. So I split the file based on the first letter of the title. So this post ([Reducing the server load](/Reducing_the_server_load.html)) would go under a file `x.r.txt` (for 'R') while my last post ([Calvin and Hobbes animated](/Calvin_and_Hobbes_animated.html)) would go under a file `x.c.txt` (for 'C'). This speeds up the grep by a factor of 5-10.

On average, using MySQL query used to take 0.9 seconds per query. Now, using grep, it's down to about 0.5 seconds per query. **Flat files reduced the CPU load by about half**. (And as a bonus, my site has no SQL code. I never did like SQL that much.)

So that's why you haven't seen any posts from me the last couple of weeks. Partly because I didn't have anything to say. Partly because I was forced to revamp this site.

---

## Comments

<!-- wp-comments-start -->

- **Sathya** _6 Jun 2007 12:00 pm_:
  Wow. thats quite interesting. Perhaps you could have also tried caching. keep a copy of ''hot'' (Most Recently used -MRU) stuff in memory, so you dont have to relaod it again. Given that most of the hits would be for the latest entries ( or atleast 80% of the hits are for 20% of ur posts) then caching might be an option. However, I dont know how much of RAM quota you have ;-)
- **somnath** _6 Jun 2007 12:00 pm_:
  Do you work at your company in business consulting or technology. Having known you for the past eight years (jeez a long time) I have no doubt you manage not just both but spend quality time with your family as well. Maybe it would be a good idea to blog about your typical day when you juggle between work (consulting for a big client), passion (revaming this site or taking pictures or doing a project like building media pc etc. etc.) and family (playing with a baby daughter is wonderful). BTW got your mail but I check internet mail very infrequently. Cheers!
- **Saurabh** _6 Jun 2007 12:00 pm_:
  This one is slightly off the topic..I also started using freehostia a few months back, however I find that 2 out of 7 days in a week, my website is not available for more than 96% of the time..(I monitor the uptime using something called as InternetSeer)..Would you have any tips here, is freehostia not a good option for free services or should I switch to some other service provider?
- **[Rocco Blegen](http://www.google.com)** _4 Dec 2011 4:14 am_:
  Howdy! This post couldn’t be written any better! Reading through this post reminds me of my old room mate! He always kept talking about this. I will forward this post to him. Pretty sure he will have a good read. Thank you for sharing!

<!-- wp-comments-end -->
