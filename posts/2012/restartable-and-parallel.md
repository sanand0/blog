---
title: Restartable and Parallel
date: "2012-08-30T14:38:00Z"
lastmod: "2012-08-27T14:38:08Z"
categories:
  - coding
  - data
wp_id: 2789
---

When processing data at a large scale, there are two characteristics that make a huge difference to my life.

**Restartability**. When something goes wrong, being able to continue from where it stopped. In my opinion, this is more important than parallelism. There’s nothing as depressing as having to start from scratch every time. Think of it as the ability to save a game as opposed to starting from Level 1 in every life.

**Parallelism**. Being able to run multiple processes in parallel. Often, this is easy. You don’t need threads. Good old UNIX [xargs](http://en.wikipedia.org/wiki/Xargs) can do a great job of it. Interestingly, I’ve never used Hadoop for any real-life problem. I’ve gotten by with UNIX commands and smart partitioning.

The “smart partitioning” bit is important. For example, if you’re dealing with telecom data, you’d be calculating most of your metrics (e.g. did the number of calls grow or fall, are there more outgoing or incoming calls, etc.) are calculated on a single mobile number. So if you have multiple data sets, as long as all the data related to one mobile number are on the same system, you’re fine. If you have 100 machines, just split the data based on the last 2 digits of the mobile number. So data about 9012345678 would go to machine 78 (the last two digits). Given a mobile number for any type of data, you’d know exactly which machine would have that data. For all practical purposes, that gives you the basics of a distributed file system.

(I’m not saying you don’t need Hadoop. Just that I haven’t needed it.)

---

## Comments

<!-- wp-comments-start -->

- **kamaal** _30 Aug 2012 4:04 pm_:
  Anand,
  If you were to write down- What would be the must learn skills for a data scientist?
  I've sort been trying and working hard on this thing. Of course you must know programming, what else apart from a programmers ordinary skills set does a data scientist need.
- **Karthik Joshi** _3 Sep 2012 9:06 am_:
  I am a reader of your blogs. I love your visualization ideas. This one blog about distribution of work is a great Idea. But I think, it would depend on the nature of data for effective utilization of all 100 machines. (Suppose we have few numbers which will not end with 09 or 88 ro so on) How about hashing? Even though the distributedness of hash algorithm is a debatable issue, do you think this would be beneficial ? Just a thought.

<!-- wp-comments-end -->
