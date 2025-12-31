---
title: LLMs can teach experts
date: "2023-11-02T05:03:33Z"
lastmod: "2023-11-02T05:03:34Z"
categories:
  - coding
wp_id: 3466
---

![LLMs can teach experts](https://files.s-anand.net/images/2023-11-02-computer-with-crt-monitor.webp)

I am a fairly good programmer. So, when I see a problem, my natural tendency is to code.

I'm trying to break that pattern. Instead, I ask ChatGPT.

[For example, I asked](https://chat.openai.com/share/1f0858cd-4768-466a-a494-c570e9debb7d):

> Write a compact 1-line Python expression that checks if `user.id` ends with @gramener.com or @straive.com

```python
user.id.endswith(("@gramener.com", "@straive.com"))
```

After 15 years of using Python, I learnt that `.endswith()` supports tuple suffixes. This has been around since Python 2.5 (released in 2006 -- before I knew Python.) The documentation has a **tiny** sentence in the middle saying "suffix can also be a tuple of suffixes to look for."

I checked with a few colleagues, including [Jaidev](https://www.linkedin.com/in/jaidevd/). They didn't know it either.

It's small little things like this that made me conclude.

I'm not going to code anymore. ChatGPT will, instead.
