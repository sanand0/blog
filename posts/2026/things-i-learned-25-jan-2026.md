---
title: Things I Learned - 25 Jan 2026
date: 2026-01-25T00:00:00+00:00
categories:
  - til
description: I explored IndieWeb syndication methods like POSSE, discovered DuckDB’s Vortex extension for remote querying, and researched how disengagement triggers "aha" moments. I also learned about limited email support for animated AVIF and using git-filter-repo for history rewriting.
keywords: [posse, duckdb vortex, behavioral economics, neuroscience, avif, git-filter-repo, indieweb]
---

This week, I learned:

- [POSSE](https://indieweb.org/POSSE) - "Publish (on your) Own Site, Share Everywhere" - is a self-explanatory content sharing approach. [1 minute video introduction](https://www.youtube.com/watch?v=X3SrZuH00GQ&t=835s). Alternatives are:
  - [COPE](https://web.archive.org/web/20140517203502/http://www.programmableweb.com/news/cope-create-once-publish-everywhere/2009/10/13): Create once, publish everywhere.
  - [POSE](https://indieweb.org/POSE): Publish once, syndicate everywhere.
  - [PESOS](https://indieweb.org/PESOS): Publish elsewhere, syndicate to own site.
  - [PESETAS](https://indieweb.org/PESETAS): Publish elsewhere, syndicate everything to a silo (one of the "elsewhere"s).
- Cory Doctorow's essay on [how Google will use AI against shoppers](https://pluralistic.net/2026/01/21/cod-marxism/) is a great lesson on several lessons in behavioral economics. Fighting it is hard, but here is generally good advice: [ChatGPT](https://chatgpt.com/share/69746734-a770-8003-ae4a-3168fd4428ae)
  - Never buy when rushed.
  - Set a max price.
  - Compare 2+ options (TOTAL price) early.
  - Shop logged-out for big purchases.
- [Vortex](https://github.com/vortex-data/vortex) is supported by [DuckDB](https://duckdb.org/2026/01/23/duckdb-vortex-extension). It's a better format than parquet for analysis and querying remotely. [Gemini](https://gemini.google.com/share/f83ec3ef584a)
- Research suggests that insight emerges when we struggle with a problem, get stuck, then DISENGAGE (to inhibit distractions). EEGs can predict insight ~8 seconds before it happens using this pattern. [Gemini](https://www.s-anand.net/blog/notes/gemini-neuroscience-of-aha-moments/)
  - Books that have suggested this are:
    - [The Art of Thought (1926)](https://www.goodreads.com/book/show/17226604-the-art-of-thought)
    - [The Act of Creation (1964)](https://www.goodreads.com/book/show/30676.The_Act_of_Creation)
    - [The Inner Game of Tennis (1974)](https://www.goodreads.com/book/show/905.The_Inner_Game_of_Tennis)
    - [Hare Brain, Toroise Mind (1997)](https://www.goodreads.com/book/show/599317.Hare_Brain_Tortoise_Mind)
    - [Taoism's Wu Wei](https://en.wikipedia.org/wiki/Wu_wei): "muddy water, let stand, becomes clear"
    - [Zen Koans](https://en.wikipedia.org/wiki/Koan): giving students impossible riddles
  - Books that have argued (probably incorrectly) that an impasse is a signal to push harder, not step back, are:
    - [The Protestant Ethic and the Spirit of Capitalism (1905)](https://www.goodreads.com/book/show/74176.The_Protestant_Ethic_and_the_Spirit_of_Capitalism) by Max Weber, [Edison's 99% perspiration quote](https://quoteinvestigator.com/2012/12/14/genius-ratio/)
    - [The 10X Rule (2011)](https://www.goodreads.com/book/show/10339170-the-10x-rule)
    - [Grit (2016)](https://www.goodreads.com/book/show/27213329-grit)
    - [Can't Hurt Me (2018)](https://www.goodreads.com/book/show/41721428-can-t-hurt-me)
- We are starting to talk like LLMs. [Empirical evidence of Large Language Model's influence on human spoken communication](https://gemini.google.com/share/fa763d406046)
- [Email support for animated AVIF is limited](https://www.caniemail.com/features/image-avif/). Though it's perhaps the best compression format, and Apple Mail supports it well, Outlook on Windows does not support it. GMail converts it to GIF. Also, Google Groups does not yet support it. When I sent an [animated AVIF](https://files.s-anand.net/images/2026-01-20-gemini-scraper-add-bookmarklet.avif) in a Google Group email, it was replaced by the content proxy to [this nonexistent URL](https://ci5.googleusercontent.com/proxy/IczfXXBzWZpSMU4zGPAy7i2QIiloAnCy9P2rvA4PX6CZU8m1-ZZP_2CBDN9oySrlTgm4lsNEKDbFsSwIDMcPm-C9k2iLSYTaPQnedmoaglIGOgI9R9l-AjGd_Ms7taUaerE=s0-d-e1-ft#https://files.s-anand.net/images/2026-01-20-gemini-scraper-add-bookmarklet.avif).
- [Portkey Models](https://github.com/portkey-ai/models) is a repo of model related data (e.g. price, max tokens, capabilities, etc.) for a large number of models. Somewhat similar to Simon Willison's [LLM Prices](https://github.com/simonw/llm-prices).
- [git-filter-repo](https://github.com/newren/git-filter-repo) is a _surprisingly_ easy way to rewrite your git history to remove specific files (e.g. large files, sensitive files). It can preserve timestamps, messages, etc. It just filters out specific files as if they were never committed. This can reduce the size of repos dramatically.
