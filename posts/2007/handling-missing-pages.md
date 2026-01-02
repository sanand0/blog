---
title: Handling missing pages
date: "2007-12-24T12:00:00Z"
categories:
  - how-i-do-things
wp_id: 70
---

> If something goes wrong with my site, I like to know of it. My top three problems are:
>
> 1. [The site is down](/blog/monitoring-site-downtime/)
> 2. [A page is missing](#start2)
> 3. [Javascript isn't working](/blog/javascript-error-logging/)
>
> This article covers the second topic.

One thing I'm curious about is hits to [non-existent pages (404s)](http://alistapart.com/articles/perfect404/) on my site. I usually get 404s because:

- I renamed the page
- Someone typed a wrong URL
- Someone followed a wrong link

**Find the 404**

The first problem is to know when someone gets a 404. I've seen sites that tell you to contact the administrator in case of a 404. That's crazy. **The administrator should automatically detect of 404s!** Almost every web server provides this facility.

The real issue is attention. I receive 700 404s a day. That's too much to manually inspect. And most of these are not for proper web pages, but for images (for example, almost all my 404s used to be for browsers requesting [favicon.ico](http://en.wikipedia.org/wiki/Favicon.ico)) or [weird MS Office files](http://www.michaelteper.com/archive/2005/11/02/4276.aspx).

I'm interested in a small subset of 404 errors. Those that hit a **web page**, not support files. And those **requested by a human**, not a search engine or a program.

A decent way of filtering these is to use Javascript in your 404 page. Javascript is typically executed only by browsers (i.e. humans, not search engines), and only in a web page (not images, etc.) So if you serve Javascript in your 404 page, and it gets executed, it's likely to be a human requesting a web page.

I have a piece of Javascript in my custom 404 page that looks something like this:

```html
<script>(new Image()).src = "/log.pl";</script>
```

Every time this code runs, it loads a new image. The source of the image is a Perl script, log.pl. Every time log.pl is accessed, it logs the URL from which it was called. I'm reasonably guaranteed that these are web pages a human tried to access.

The reduction in volume is tremendous. On a typical month, I get ~20,000 404 errors. With the Javascript logging, it's down to around 200 a month, and most of them quite meaningful.

**Point to the right page**

Sometimes, the change happens because I changed the URLs. I keep fiddling with the site structure. Someone would have links to an old page that I've renamed. I may not even know that. Even if I did, they can't be bothered with requests to change the link. So I've got to handle it.

The quickest way, I find, is to use [Apache's mod\_rewrite](http://httpd.apache.org/docs/1.3/mod/mod_rewrite.html). You can simply redirect the old URL to the new URL. For example, I used to have a link to `/calvin.html` which I now point to `/calvin/`. That becomes a simple line on my [.htaccess](http://en.wikipedia.org/wiki/.htaccess) file:

```apacheconf
RewriteRule calvin.html  calvinandhobbes.html
```

I don't do this for every site restructuring, though. I just restructure, wait for someone to request a wrong page, and when my 404 error log warns me, I create a line in the .htaccess. It keeps the redirections down to a minimum, and only for those links that are actually visited.

**Be flexible with the URL structure**

Sometimes people type in a wrong link. Often, these are unintentional. Here are some common misspellings for my [Hindi songs search](/hindi).

```text
s-anand.net/hindi/
s-anand.net/Hindi
s-anand.net/hiundi
```

Occasionally, people are exploring the structure of my site:

```text
s-anand.net/excel
s-anand.net/music
s-anand.net/hits
```

I need to decide what to do with both cases. For the former, sometimes my URL structure is too restrictive. I mean, why should someone have to remember to type `/hindi` instead of `/Hindi` or `/hindi/`? Who cares about case? Who cares about a trailing slash?

In such cases, I map all the variants to the right URL using mod\_rewrite. For example, typing `s-anand.net/HiNDi` (with or without caps, with or without a slash at the end) will still take you to the right page.

As I keep discovering new mis-spellings, I take a call on whether to add it or not. The decision is usually based on volume. If two people make the same spelling mistake in a day, I almost certainly add the variant. Most of the time, it's just typing errors like `/hiundi` which isn't repeated oftener than once a month.

**Provide search**

To handle the exploratory URLs, and people following wrong links, I've turned my **custom 404 page into a search engine**.

For example, when someone types `s-anand.net/excel`, I know they're searching for Excel. So I just do a Google Custom Search within my site for "excel" -- that is, anything following the URL.

It's a bit more complex than that, actually. I do a bit of tweaking to the URL, like convert punctuations (underscore, hyphen, full-stop, etc.) to spaces, remove common suffixes (.html, .htm) and ignore numbers. Quite often, it matches something on my site that they're looking for. If not, ideally, I ought to try for various alternatives and subsets of the original search string to figure out a good match. But given that the number of mismatches is down to about one a day, I'm fairly comfortable right now.

What this means, incidentally, is that my site is, by default, a search engine for itself. To search for movie-related stuff on my site, just type `s-anand.net/movie` and you get a search of the word "movie" on my site. (Sort of like on [a9.com](http://a9.com/), where searching for `a9.com/keyword` does a search on the keyword.)
