---
title: Short URLs
date: "2009-04-11T18:59:45Z"
lastmod: "2009-04-12T06:10:13Z"
categories:
  - coding
wp_id: 2372
---

With [all](http://joshua.schachter.org/2009/04/on-url-shorteners.html) [the](http://laughingmeme.org/2009/04/03/url-shortening-hinting/) [discussion](http://www.scripting.com/stories/2009/03/07/solvingTheTinyurlCentraliz.html) around [URL shorteners](http://en.wikipedia.org/wiki/List_of_URL_redirection_services), [Diggbar](http://digg.com/tools/diggbar), [blocking](http://daringfireball.net/2009/04/how_to_block_the_diggbar) [it](http://farukat.es/journal/2009/04/225-javascript-diggbar-killer-not-blocker), and the [rev](http://revcanonical.appspot.com/)=[canonical](http://twitter.com/kevinmarks/status/1448424167) proposal, I decided to implement a URL shortening service on this blog with the least effort possible. This probably won’t impact you just yet, but when [tools](http://simonwillison.net/2009/Apr/11/revcanonical/) become more popular and sophisticated, it would hopefully eliminate the need for [tinyurl](http://tinyurl.com/), [bit.ly](http://bit.ly/), etc.

Since the blog runs on [WordPress](http://wordpress.org/), every post has an ID. The short URL for any post will simply be `http://www.s-anand.net/the_ID`. For example, <http://s-anand.net/17> is a link to post on [Ubuntu on a Dell Latitude D420](/blog/ubuntu-8-10-on-a-dell-latitude-d420/). At 21 characters, it’s roughly the same size as most [URL shorteners](http://dooleyonline.typepad.com/dooley_post/2009/02/comparison-of-url-shorteners.html) could make it.

The code is easy: just one line added to index.php:

`<link rev="canonical" href="http://s-anand.net/<?php the_ID(); ?>">`

… and one line in my .htaccess:

`RewriteRule ^([0-9]+)$ blog/?p=$1 [L,R=301,QSA]`

Hopefully someone will come up with a WordPress plugin some time soon that does this. Until then, this should work for you.
