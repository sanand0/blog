---
title: How Google Maps works
date: "2005-02-10T12:00:00Z"
categories:
  - links
wp_id: 752
description: I examine the original technical implementation of Google Maps, which utilized hidden IFrames for server communication rather than XMLHttp. The system also leveraged 8-bit alpha channel PNGs to render realistic shadows for map markers and popups.
tags: [google-maps, javascript, web-development]
---

[How Google Maps works](http://jgwebber.blogspot.com/2005/02/mapping-google.html): a look behind the Javascript of Google Maps.

> Whereas GMail uses XMLHttp to make calls back to the server, Google Maps uses a hidden IFrame. The method has its benefits.
>
> The push-pins and info-popups are a different matter. Simply placing them is no big trick; an absolutely-positioned transparent GIF does the trick nicely. The shadows, however, are a different matter. They are PNGs with 8-bit alpha channels.

The comments following the post as also quite a read.
