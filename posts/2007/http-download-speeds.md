---
title: HTTP download speeds
date: "2007-04-25T12:00:00Z"
categories:
  - how-i-do-things
wp_id: 91
---

<p>In some of the Web projects I'm working on, I have a choice of <b>many small files vs few big files to download</b>.</p>
<p>There are conflicting arguments. I've read that <a href="http://www.thinkvitamin.com/features/webapps/serving-javascript-fast">many small files are better</a>, because you can choose to use only the required files, and they'll be cached across the site. (These are typically CSS or Javascript files.) On the other hand, a single large file takes less time to download than the sum on many small files, because there's less latency. (<a href="http://www.stuartcheshire.org/rants/Latency.html">Latency is more important than bandwidth</a> these days.)</p>
<p>I ran some tests, and the answer is rather easy. The graph below shows the average time taken to download a file of size 1KB - 100KB.</p>
<p><a href="/blog/assets/flickr-http-load-times_472277744_o-png.webp"><img src="/blog/assets/flickr-http-load-times_472277744_o-png.webp" width="500" height="414" alt="Time to download a file of size ranging from 1KB - 100KB"></a></p>
<p>The X-axis is the size of the file. The Y-axis is the number of milliseconds taken to download the file, averaged over 10 attempts on my home computer. (I did the same thing at work and at a client site. The results are similar.)</p>
<p>The key thing is, it's not linear. Larger files take less time. Specifically:</p><ul>
        <li>A file twice as big only takes 30% longer to load.</li>
        <li>Breaking a file into two parts takes 54% longer to load.</li>
</ul>
<p>These days, it looks like <b>few big files are better</b>.</p>
<p>To give you an example: my home page had the following components:</p>
<table class="numbers lines">
<thead><tr><th></th><th>Size (KB)</th><th>Load time (ms)</th></tr></thead>
<tbody>
<tr><td>HTML</td><td>25</td><td>680</td></tr>
<tr><td>CSS</td><td>4</td><td>340</td></tr>
<tr><td>Javascript</td><td>6</td><td>400</td></tr>
</tbody>
<tfoot><tr><td>Total</td><td>35</td><td>1420</td></tr></tfoot>
</table>
<p>The total time for these 3 files would be about 1.4 seconds. Instead, if I put them all on one file...</p>
<table class="numbers lines">
<thead><tr><th></th><th>Size (KB)</th><th>Load time (ms)</th></tr></thead>
<tbody><tr><td>All-in-one</td><td>35</td><td>770</td></tr></tbody>
</table>
<p>The combined file takes only 0.77 seconds -- half the download time for split files. It's a compelling argument to <b>put all your CSS and Javascript (images, too, if possible) into a single page</b>.</p>
<p>But what if people visit multiple pages on my site, and lose the benefit of caching? Not really. The benefit of caching is small. By having a single file, I have 770 - 680 = 90 ms additional time for each HTML to load. But I don't have to load the CSS and Javascript individually, which takes 740 seconds. The breakeven is about 740 / 90 = 8 page visits.</p>
<p>So, on average, if people, visit more than 8 pages in my site, it's worth breaking up the CSS and Javascript. But the average for my site is only 2 pages per person. (It's a skewed distribution. Most, from Google, just visit one page. Few, from bookmarks, visit several pages. On average, it's just over 2.) I'd argue that <b>unless you're using an external Javascript / CSS library (<a href="http://prototypejs.org/">prototype</a>, etc.) or people view many pages each visit, you're better of having a single HTML+Javascript+CSS file</b>.</p>
