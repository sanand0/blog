---
title: Visualisation of data
date: "2006-09-17T12:00:00Z"
categories:
  - visualisation
wp_id: 213
---

<p><b>I have managed to fill hard disks of all capacities within a few months.</b> My first PC had 10MB of disk space, while I work on 140GB today (remember: that's 14 <i>thousand</i> times more capacity in 14 years). Both were filled within 2 months. (An aside: the <i>number</i> of files / folders hasn't growth by 14,000. The <i>files themselves</i> have grown in size. I have roughly the same number of files/folders today on my machine as I had 14 years ago.)</p>
<p><b>To regain space, I used to go through every file and delete the unnecessary ones.</b> My favourite tool was the UNIX utility <a href="http://www.informit.com/articles/article.asp?p=30599&seqNum=2&rl=1">du</a> (Disk Usage). It lists the disk space used by every subdirectory. I would sort the result and find big, useless stuff. Here are the first few lines of a sorted du output:</p>
<table class="lines">
<tr><td>1342507</td><td>./Books</td></tr>
<tr><td>1188020</td><td>./Non-Fiction</td></tr>
<tr><td>1047607</td><td>./Comics</td></tr>
<tr><td>842832</td><td>./Non-Fiction.Magazines</td></tr>
<tr><td>594939</td><td>./Audio</td></tr>
<tr><td>298737</td><td>./Books/kokona - Business</td></tr>
<tr><td>172166</td><td>./Books/Terry Pratchett</td></tr>
<tr><td>164246</td><td>./Books/Terry Pratchett/Discworld</td></tr>
<tr><td>162287</td><td>./Calvin</td></tr>
<tr><td>142274</td><td>./Books/S</td></tr>
<tr><td>77407</td><td>./Scripts</td></tr>
<tr><td>74858</td><td>./Science</td></tr>
</table>
<p>It would take 5 minutes to create the list, and 15 minutes to read.</p>
<p><b>Nowadays I use <a href="http://windirstat.info/">WinDirStat</a></b>, which shows every file and folder in an intuitive, graphical manner.</p>
<p><a href="/blog/assets/flickr-treemap-from-windirstat_245210637_o-png.webp"><img src="/blog/assets/flickr-treemap-from-windirstat_245210637_o-png.webp" width="460" height="446" alt="Treemap from WinDirStat"></a></p>
<p>This view is called a Treemap. Each small block is a file. Bigger blocks are folders. Colours indicate the type of file (MP3s are blue, AVIs are red, WMVs are yellow, JPGs are green, etc.). This view has many advantages:</p><ul>
<li>I can see the relative sizes of files and folders.</li>
<li>I can get an idea of the % of free space (grey block).</li>
<li>I can see what type of files occupy the most space.</li>
<li>etc. etc.</li>
</ul>
<p>But the most important thing is, <b>I see the useful stuff at a single glance</b>.</p>
<p>That's the key in <b>visualisation: conveying a complex topic so people <i>get</i> it in a second</b>.</p>
<p>(Incidentally, Google has a <a href="http://video.google.co.uk/videoplay?docid=-6229232330597040086#31m40s">TechTalk on visualisation, including treemaps</a>.)</p>
