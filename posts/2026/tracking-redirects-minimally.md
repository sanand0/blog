---
title: Tracking redirects minimally
date: 2026-05-07T16:28:22+08:00
categories:
- coding
- tools
description: I built a simple tracking URL shortener with static HTML redirects, GoatCounter analytics, and personalized query parameters. It runs cheaply on Cloudflare R2 and avoids dependence on redirect services.
tags: [web-analytics, static-sites, cloudflare-r2]
---

Everyone needs a tracking URL shortener.

- **Why tracking?** I want to know if they opened my email and clicked the link.
- **Why shortener?** I want them to know what the link is about. For example, <https://r.s-anand.net/edge-remote-debugging.html> is so much more meaningful than <https://chatgpt.com/share/68528565-0d34-800c-b9ec-6dccca01c24c>

I've used redirection services in the past - like `t.co`, `bit.ly`, `goo.gl`, `ow.ly`, and others. They tend to vanish, start charging, serve ads, etc.

Here's my solution: **use static HTML for redirection**.

![](https://files.s-anand.net/images/2026-05-07-tracking-redirects-minimally.avif) <!-- https://chatgpt.com/c/69fc5f20-2dfc-83ea-82c4-9096c77374f3 -->

For example, <https://r.s-anand.net/example.html> redirects to <https://example.com/>. Here's the code:

```
<script data-goatcounter="https://sanand0.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
<meta http-equiv="refresh" content="0; url=https://example.com/">
```

The first line sets up tracking with [GoatCounter](https://www.goatcounter.com/), which is my current favorite analytics provider. It might vanish, but I can export the data if required and move to another. While it lasts, I can check how often the link was used.

I can create personalized links. For example, <https://r.s-anand.net/example.html?ref=user1> tags `user1`. I can create unique links for each recipient.

The second redirects to the target page immediately.

I have deployed the files on a CloudFlare R2 bucket with a custom domain, which is practically free and fast. But I can switch at any point to any other hosting provider (e.g. GitHub Pages, etc.) by just copying the files and changing the DNS settings.

**Advantages**: No hosting, no fees, no maintainance, no vendor lock-in.
