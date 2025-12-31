---
title: Link to a Google search rather than a site
date: "2006-09-11T12:00:00Z"
categories:
  - how-i-do-things
wp_id: 225
---

When you make a link, there's no guarantee that the link will work 5 years later. **Sites change their URL structure.** I'm finding that many of my blog entries from 2000 are invalid.

Sometimes you want to link to a concept rather than a site. In such cases, it's better to link to a Google query.

For example, rather than link to a site that defines SVG, I could link to the Google search [define:SVG](http://www.google.com/search?q=define%3ASVG).

Rather than link to a tutorial on Excel array formulas, I could link to the Google search [excel array formulas](http://www.google.com/search?q=excel+array+formulas). I could even link to the first hit on Google for [excel array formulas](http://www.google.com/search?q=excel+array+formulas&btnI=I'm+Feeling+Lucky), mimicking the "I'm feeling lucky" button. This may change over time, but 5 years from now, it'll still point to the most relevant link.

To link to the Google query for "excel array formulas", just link to the URL `http://www.google.com/search?q=excel+array+formulas`. To link directly to the first result, add `&btnI=I'm+Feeling+Lucky` to the URL. (Linking to A9 is simpler: `http://a9.com/excel+array+formulas`)

PS: An alternative is to **link to a permanent copy of the page** from the [Wayback machine](http://www.archive.org/web/web.php) (it has copies of my page all the way from [May 2001](http://web.archive.org/web/20010519175111/http://www.s-anand.net/) to [Mar 2005](http://web.archive.org/web/20050324014417/http://www.s-anand.net/)). (You can't use Google's cache. When the site changes, the cache will soon change. But it's a good defence against site downtime. Manually doing this is a lot of effort. Ideally, future browsers will automatically take you to the Wayback machine or the Google cache. (The Firefox plugins [ErrorZilla](http://roachfiend.com/archives/2006/08/28/errorzilla-useful-error-pages-for-firefox/) and [CacheIt](https://addons.mozilla.org/firefox/1700/) come close.)
