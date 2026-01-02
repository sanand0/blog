---
title: HTTP download speeds
date: "2007-04-25T12:00:00Z"
categories:
  - how-i-do-things
wp_id: 91
---

In some of the Web projects I'm working on, I have a choice of **many small files vs few big files to download**.

There are conflicting arguments. I've read that [many small files are better](http://www.thinkvitamin.com/features/webapps/serving-javascript-fast), because you can choose to use only the required files, and they'll be cached across the site. (These are typically CSS or Javascript files.) On the other hand, a single large file takes less time to download than the sum on many small files, because there's less latency. ([Latency is more important than bandwidth](http://www.stuartcheshire.org/rants/Latency.html) these days.)

I ran some tests, and the answer is rather easy. The graph below shows the average time taken to download a file of size 1KB - 100KB.

[![Time to download a file of size ranging from 1KB - 100KB](/blog/assets/flickr-http-load-times_472277744_o-png.webp)](/blog/assets/flickr-http-load-times_472277744_o-png.webp)

The X-axis is the size of the file. The Y-axis is the number of milliseconds taken to download the file, averaged over 10 attempts on my home computer. (I did the same thing at work and at a client site. The results are similar.)

The key thing is, it's not linear. Larger files take less time. Specifically:

- A file twice as big only takes 30% longer to load.
- Breaking a file into two parts takes 54% longer to load.

These days, it looks like **few big files are better**.

To give you an example: my home page had the following components:

|            | Size (KB) | Load time (ms) |
| ---------- | --------- | -------------- |
| HTML       | 25        | 680            |
| CSS        | 4         | 340            |
| Javascript | 6         | 400            |
| Total      | 35        | 1420           |

The total time for these 3 files would be about 1.4 seconds. Instead, if I put them all on one file...

|            | Size (KB) | Load time (ms) |
| ---------- | --------- | -------------- |
| All-in-one | 35        | 770            |

The combined file takes only 0.77 seconds -- half the download time for split files. It's a compelling argument to **put all your CSS and Javascript (images, too, if possible) into a single page**.

But what if people visit multiple pages on my site, and lose the benefit of caching? Not really. The benefit of caching is small. By having a single file, I have 770 - 680 = 90 ms additional time for each HTML to load. But I don't have to load the CSS and Javascript individually, which takes 740 seconds. The breakeven is about 740 / 90 = 8 page visits.

So, on average, if people, visit more than 8 pages in my site, it's worth breaking up the CSS and Javascript. But the average for my site is only 2 pages per person. (It's a skewed distribution. Most, from Google, just visit one page. Few, from bookmarks, visit several pages. On average, it's just over 2.) I'd argue that **unless you're using an external Javascript / CSS library ([prototype](http://prototypejs.org/), etc.) or people view many pages each visit, you're better of having a single HTML+Javascript+CSS file**.
