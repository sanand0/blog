---
title: Get this blog via email on Google Groups
date: 2026-01-05T17:50:35+08:00
categories:
- how-i-do-things
description: I created a Google Group for email updates whenever I publish new blog posts. I’ll post updates manually at first, then automate them using a Python script.
tags: [google-groups, email, google-api, python]
---

**TL;DR**: [Join this Google Group](https://groups.google.com/g/s-anand) to get my blog updates via email.

My blog is over 25 years old. At first, people had to visit it to read it. Then I added an RSS feeds. Then email subscriptions. Then via social media, cross-posting on [Twitter](https://x.com/sanand0), now [LinkedIn](https://www.linkedin.com/in/sanand0/).

The [RSS feed](/blog/index.xml) remains. But I feel it's time to bring back email subscriptions. It's the oldest of the technologies, the most robust, and the one I believe will last the longest.

My blog might last another 25 years. I'm willing to bet email will outlast RSS and certainly the social media platforms.

So, I've created a [Google Group: `s-anand@googlegroups.com`](https://groups.google.com/g/s-anand) where I will post new blog entries. You can join the group to get email updates whenever I post something new.

For now, I will post updates manually. After a few weeks of testing, I'll automate the process.

---

PS: I use a [`htmlemail.py`](https://github.com/sanand0/blog/blob/3f9632c742eaec0416b469beb820fcd9c94e8cb3/scripts/htmlemail.py) script to send blog posts as HTML emails via the GMail API. It was vibe-coded by Claude and taught me a few things:

- The [`frontmatter`](https://pypi.org/project/python-frontmatter/) package is a clean way to parse YAML frontmatter from markdown files.
- LLMs aren't familiar enough with the [`markdown2`](https://pypi.org/project/markdown2/) package, which is the new standard for processing Markdown. They prefer [`markdown`](https://pypi.org/project/Markdown/) instead.
- [`premailer`](https://pypi.org/project/premailer/) is a well-maintained package to inline CSS for HTML emails.
- [`pygments`](https://pypi.org/project/Pygments/) is the de facto standard to generate CSS for syntax highlighting code blocks.
