---
title: Blog embeddings map
date: '2026-03-15T23:22:46+05:30'
categories:
- llms
- coding
- how-i-do-things
description: "Embedding maps can reveal the long-term evolution of a blog’s themes and eras, making decades of writing visually legible as clusters and transitions."
keywords: [embeddings, UMAP, blog analysis, semantic map, writing history, visualization]
linkedin: https://www.linkedin.com/feed/update/urn:li:activity:7439154743433703424/
---

I created an [embedding map of my blog posts](https://files.s-anand.net/blog/blogmap/).

[![](https://files.s-anand.net/images/2026-03-15-blog-embeddings-map.avif)](https://files.s-anand.net/blog/blogmap/)

Each point is a blog post. Similar posts are closer to each other. They're colored by category.

I've been blogging since 1999 and over time, my posts have evolved.

- 1999-2005: mostly [links](https://www.s-anand.net/blog/category/links/). I started by link-blogging
- 2005-2007: mostly [quizzes](https://www.s-anand.net/blog/category/quizzes/), [how I do things](https://www.s-anand.net/blog/category/how-i-do-things/), [Excel tips](https://www.s-anand.net/blog/category/excel-tips/), etc.
- 2008-2014: mostly [coding](https://www.s-anand.net/blog/category/coding/), [how I do things](https://www.s-anand.net/blog/category/how-i-do-things/) and [business realities](https://www.s-anand.net/blog/category/business-realities/)
- 2015-2019: mostly nothing
- 2019-2023: mostly [LinkedIn](https://www.s-anand.net/blog/category/linkedin/) with some [data](https://www.s-anand.net/blog/category/data/) and [how I do things](https://www.s-anand.net/blog/category/how-i-do-things/)
- 2024-2026: mostly [LLMs](https://www.s-anand.net/blog/category/llms/)

... and this transition is _entirely_ visible in the embedding space.

<video width="1920" height="1084" style="max-width: 100%; height: auto;" controls autoplay loop muted>
  <source src="https://files.s-anand.net/images/2026-03-15-blog-embeddings-map.webm" type="video/webm">
  <a href="https://files.s-anand.net/images/2026-03-15-blog-embeddings-map.webm">Video</a>
</video>

---

[I used Codex and GitHub Copilot + Claude Sonnet 4.6 to create this visualization](https://github.com/sanand0/blog/blob/main/analysis/embeddings/prompts.md). It was [vibe coded](https://github.com/sanand0/blog/tree/main/analysis/embeddings/) in the background while I was vibe-coding my [PyConf Hyderabad talk](https://sanand0.github.io/talks/2026-03-15-how-students-learn-python/). The rough process was:

- Extract the blog posts and pages (stripping out comments, adding titles).
- Use Gemini Embedding 2 Preview to generate 768-dimentional embeddings for un-embedded content.
- Create a UMAP visualization of these embeddings, colored by category, and make it interactive with filters and popups.
