---
title: Making my music search engine faster
date: "2007-06-07T12:00:00Z"
categories:
  - how-i-do-things
wp_id: 79
---

<p><b>My music search engine takes quite a while to load</b> (typically 40 seconds). That's an unusually long time for a page, given that most of the people that access it are on broadband connections, and are listening to music online.</p>
<p>The reason is, firstly, that <b>I'm loading a lot of data</b>. Literally every single song on that you can search comes through as Javascript. All the downloadable Hindi songs, for instance, occupy 1.3 megabytes before compression. On average, this takes about 20 seconds to load.</p>
<p>The second reason is, <b>I'm doing a lot of processing with the data</b>. Two things take the bulk of the time: uncompressing the data, and massaging it to allow for different spellings. On average, that takes about 20 seconds.</p>
<p>40 seconds is too long to wait. Actually, the perceived waiting time is 8 seconds, because I start showing the search and the results after 1/5th of the data is downloaded. But 8 seconds is still too long.</p>
<p>I managed to cut this time by half with two things I just learned.</p>
<p>Firstly, <a href="http://dev.opera.com/articles/view/timing-and-synchronization-in-javascript/">Javascript loads and executes sequentially</a>. As soon as a Javascript block is loaded, it is executed. While it is being executed, the rest of the HTML file is not parsed. So any subsequent Javascript blocks (or images, CSS, any other external links) are not loaded. Bandwidth is just sitting idle while the browser is busy at work on the Javascript.</p>
<p>Since I've split all my songs into five equal-sized Javascript files, <b>my search engine loads the Javascript files one after another</b>! The problem is even worse -- the calculations I do in Javascript take up as much time as the load time. If the loading went on in parallel, by the time the first calculation is done, the second script would have loaded.</p>
<p>This problem can be solved for Internet Explorer and Opera. The <b>"defer" attribute loads the scripts in the background</b>, and defers their execution. This reduces the loading time to nearly zero for all the Javascript files except for the first one or two, because by the time my calculations are done, the next script is already loaded.</p>
<p><a href="/blog/assets/flickr-javascript-loading-sequence-before-and-after-defer_534563515_o-gif.webp"><img src="/blog/assets/flickr-javascript-loading-sequence-before-and-after-defer_534563515_o-gif.webp" width="290" height="176" alt="Javascript loading sequence before and after 'defer'"></a></p>
<p>These Javascript files contain a list of songs as a long string, which I then split into individual songs. Then I modify each song using regular expressions so that approximate matches will still work. (For e.g., typing "aa" is the same as typing "a" on this search engine.) The performance of regular expressions is critical to me.</p>
<p>Originally, I did this:</p><ol>
        <li>Split the string into songs</li>
        <li>Modify each song using regular expressions</li>
</ol>
<p>Now, I changed the sequence to this:</p><ol>
        <li>Modify the string using regular expressions</li>
        <li>Split the string into songs</li>
</ol>
<p>When I timed the speed of this change, I realised <b>browsers differ a lot in the speed of processing regular expressions</b>. Here is the time (in seconds) for each browser to process the Javascript before and after the change.</p>
<table class="numbers lines">
<tr><th>Browser</th><th>Before</th><th>After</th></tr>
<tr><td>Internet Explorer</td><td>6.3</td><td>5.0</td></tr>
<tr><td>Firefox</td><td>17.7</td><td>4.7</td></tr>
<tr><td>Opera</td><td>93.8</td><td>19.9</td></tr>
</table>
<p>Internet Explorer wasn't affected much by this change. But Firefox and Opera were heavily impacted. I'm guessing this is because Firefox and Opera have a high setup time for matching regular expressions. Before, I was matching thousands of strings. After, I was matching only one (long) string. IE didn't care much. Firefox and Opera speeded up dramatically. (I suspect my Opera data is skewed by a few people using a rather slow machine... but then, that's probably why they should use Opera in the first place -- it works rather well old machines.)</p>
<p>With these changes, my total load time fell from about 40 seconds to about 20 seconds. Pretty decent improvement.</p>
<p>There are two further steps I could take from here on.</p>
<p><b>Compress the songs files further</b></p>
<p>Currently, I'm doing two things to compress the songs.</p><ol>
        <li>Instead of sending the list as a <code>(movie-song),(movie-song),...</code> combination for every song, I send it as a <code>(movie-song,song,song,...)(movie-song,song,song,...)...</code> combination. So I don't repeat the movie names.</li>
        <li>Secondly, I <a href="http://www.webreference.com/internet/software/servers/http/compression/">compress them via HTTP/1.1</a>. (My server doesn't let me do that with Javascript, actually, because Netscape 4.x doesn't accept compressed Javascript. But since it's such an old browser and none of my viewers use it, I trick the server by renaming my Javascript files as .html, and it passes them on compressed.</li>
</ol>
<p>What I could do additionally is:</p><ol>
        <li><b>Remove duplicate songs</b>. If songs are spelt differently, I include them both. But I can knock off the duplicate ones.</li>
        <li><b>Compress the text</b>. Though I'm gzipping the text before sending it, I suspect there may be ways of storing the data in a more compressed form. For example, many songs are repeated with the (male) and (female) versions. These could be clubbed (somehow...)</li>
</ol>
<p><b>Speed up the Javascript calculations further</b></p>
<p>There are two steps I'm doing right now:</p><ol>
        <li>Modify the string using regular expressions</li>
        <li>Split the string into songs</li>
</ol>
<p>Here's how much time each step takes (in seconds) across browsers. (Note: these were based on one day's data, sampling about 2,000 page views)</p>
<table class="numbers lines">
<tr><th>Browser</th><th>Regular expression</th><th>Split</th></tr>
<tr><td>Internet Explorer</td><td>0.88</td><td>3.04</td></tr>
<tr><td>Firefox</td><td>3.76</td><td>1.08</td></tr>
<tr><td>Safari</td><td>0.47</td><td>0.46</td></tr>
<tr><td>Opera</td><td>4.96</td><td>29.78</td></tr>
</table>
<p>Firefox takes a lot of time with regular expressions. IE and Opera take a lot longer to split (which involves creating many objects). I may have to think up different optimisations for the two.</p>
<p>The code is available in the HTML of the <a href="hindi">song search engine</a>. It's readable. The stuff I'm talking about is in the <code>function sl(p,s)</code>. Any thoughts are welcome!</p>
