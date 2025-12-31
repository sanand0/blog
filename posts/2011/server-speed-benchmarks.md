---
title: Server speed benchmarks
date: "2011-03-12T08:23:44Z"
categories:
  - coding
wp_id: 2618
---

<p>Yesterday, <a href="/blog/why-node-js/">I wrote about</a> <a href="http://nodejs.org/">node.js</a> being fast. Here are some numbers. I ran Apache Benchmark on the simplest Hello World program possible, testing 10,000 requests with 100 concurrent connections (<code>ab -n 10000 -c 100</code>). These are on my Dell E5400, with <a href="/blog/software-update/">lots of application</a> running, so take them with a pinch of salt.</p> <table border="0" cellspacing="0" cellpadding="2" width="601"> <tbody> <tr> <td valign="top" width="288">PHP5 on Apache 2.2.6<br><code>&lt;?php echo “Hello world” ?&gt;</code></td> <td valign="top" width="56">1,550/sec</td> <td valign="top" width="255">Base case. But this isn’t too bad</td></tr> <tr> <td valign="top" width="288">Tornado/Python<br>See <a href="http://www.tornadoweb.org/">Tornadoweb</a> example</td> <td valign="top" width="56">1,900/sec</td> <td valign="top" width="255">Over 20% faster</td></tr> <tr> <td valign="top" width="288">Static HTML on Apache 2.2.6<br><code>Hello world</code></td> <td valign="top" width="56">2,250/sec</td> <td valign="top" width="255">Another 20% faster</td></tr> <tr> <td valign="top" width="288">Static HTML on nginx 0.9.0<br><code>Hello world</code></td> <td valign="top" width="56">2,400/sec</td> <td valign="top" width="255">6% faster</td></tr> <tr> <td valign="top" width="288">node.js 0.4.1<br>See <a href="http://nodejs.org/">nodejs.org</a> example</td> <td valign="top" width="56">2,500/sec</td> <td valign="top" width="255">Faster than a static file on nginx!</td></tr></tbody></table> <p>I was definitely NOT expecting this result… but it looks like serving a static file with node.js could be faster than nginx. This might explain why <a href="http://markup.io/">Markup.io</a> is <a href="http://web-sniffer.net/?url=markup.io&amp;type=HEAD">exposing node.js directly</a>, without an nginx or varnish proxy.</p>

---

## Comments

<!-- wp-comments-start -->

- **Olivier** _12 Dec 2011 3:39 am_:
  Nginx has to read the file from the disk each time.
  Nodejs has the content of the file in memory.
  So it's normal that nodejs is faster than Nginx. Re-test the same thing but setup Nginx so it caches files in RAM and you'll see the truth.
- **Seamsky** _4 Jun 2013 11:31 pm_:
  Please, use "return 200 'Hello world';" for nginx instead of serving file from hard drive.

<!-- wp-comments-end -->
