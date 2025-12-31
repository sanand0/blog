---
title: Faster data crunching
date: "2011-09-23T18:20:10Z"
categories:
  - data
wp_id: 2684
---

<p>I’ve been playing with big data lately.</p> <p>The good part is, it’s easy to get interesting results. The data is so unwieldy that even average value calculations provoke a “Amazing! I didn’t know that,” response (No exaggeration. I heard this from two separate ~ $1bn businesses this month.)</p> <p>The bad part is that calculating even that simple average is slow.</p> <p>For example, take this <a href="http://s-anand.net/nuepa/school_10.rpt.bz2">40MB file</a> (380MB unzipped) and extract the first column.</p> <p>The simplest Python script to get the first column looks like this:</p>
```python
for row in csv.reader(fileinput.input(), delimiter='\t'):
    if len(row) > 0: print row[0]
```

<p>That took a good 3 minutes to execute on my laptop.</p>
<p>Since I’m used to <a href="http://en.wikibooks.org/wiki/Ad_Hoc_Data_Analysis_From_The_Unix_Command_Line">UNIX data processing</a>, I tried <code>cut -f1</code>. Weirdly, that’s worse. 5 minutes. Paradoxically, </code>awk '{print $1}'</code> only takes 17 seconds. That's about 12 times faster. Clearly the tool makes a big difference. And we always knew <a href="http://swtch.com/~rsc/regexp/regexp1.html">UNIX</a> was <a href="http://lists.freebsd.org/pipermail/freebsd-current/2010-August/019310.html">fast</a>.</p>
<p>But I also ran these on an <a href="http://aws.amazon.com/ec2/">Amazon EC2</a> server, and a <a href="http://www.hostgator.com/">Hostgator</a> server. Here’re the results.</p>
<table>
<thead>
<tr>
<th>&nbsp;</th>
<th><strong>python</strong></th>
<th><strong>cut</strong></th>
<th><strong>awk</strong></th></tr></thead>
<tbody>
<tr>
<td><a href="http://www.dell.com/us/business/p/latitude-e5400/pd">My Dell E5400</a></td>
<td>3:04 (<b>1x</b>)</td>
<td>5:42 (<b>0.5x</b>)</td>
<td>0:17 (<b>11x</b>)</td></tr>
<tr>
<td><a href="http://aws.amazon.com/ec2/#instance">EC2 standard</a></td>
<td>0:33 (<b>6x</b>)</td>
<td>0:5.6 (<b>33x</b>)</td>
<td>0:16 (<b>11x</b>)</td></tr>
<tr>
<td><a href="http://support.hostgator.com/articles/hosting-plans/server-specifications-specs">Hostgator</a></td>
<td>0:19 (<b>10x</b>)</td>
<td>0:2.5 (<b>74x</b>)</td>
<td>0:0.7 (<b>265x</b>)</td></tr></tbody></table>
<p>What took 3 minutes with Python my Dell E5400 took <em>less than a second</em> on Hostgator’s server with awk. Over <em>250 times</em> faster. (Not 250%. 250 <em>times</em>). </p>
<p>And it’s not just hardware. A good tool (awk) made things 11x faster on my machine. Good hardware (hostgator) made the same program 10x faster. But choosing the right combination can make things go faster than 11 x 10 = 110 times. Much faster.</p>
<p>There are a few of things I’m taking away from this.</p>
<ol>
<li>Good hardware can speed you up much as (or more than) choosing the right tool.</li>
<li>Good hardware can be rented. From many places. Cheaply.</li>
<li>Always test what’s fast. awk’s fastest on my machine and Hostgator, but not on EC2.</li></ol>
