---
title: How to Organize Browser Workspaces with LLMs and Data
date: "2025-04-07T04:44:36Z"
lastmod: "2025-04-07T05:22:31Z"
categories:
  - llms
wp_id: 4026
---

Here's an example of how I am using LLMs to solve a day-to-day workflow problem.

Every day, I interact with a barrage of websites: emails, news, social media, and work tools across multiple devices. [Microsoft Edge’s workspaces](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-workspaces) syncs groups of websites across devices. I've never tried it, started today, and wondered: **how should I organize my workspaces?**

<div class="video-embed"><iframe src="https://www.youtube.com/embed/1kJ59DzjNOU" title="YouTube video" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

Rather than think (thinking is outdated), I used LLMs.

### Extract Browsing History

Edge stores website history in a [SQLite database](https://www.google.com/search?q=Where+is+the+Edge+browser+history+stored+on+Windows+and+Linux%3F). But the file is locked by the browser by default. So I spent a fair bit of time figure out how to read it despite it being unlocked. Here are some options:

```bash
datasette .config/microsoft-edge/Default/History --nolock
sqlite3 'file:.config/microsoft-edge/Default/History?mode=ro&nolock=1' 'SELECT url FROM urls' > urls.txt
```

([DuckDB](https://duckdb.org/) cannot read locked SQLite files - else I'd use that.)

Then comes extracting the hostnames from the URLs. I used [`llm cmd`](https://github.com/simonw/llm-cmd) to ask Gemini 2.5 Pro:

```bash
llm cmd 'Extract just the hostnames from urls.txt which has a list of URLs, one per line. Only pick the https:// URLs. Save into hostnames.txt'
```

I expanded the response `awk -F/ '/^https:\/\//{print $3}' urls.txt` into:

```bash
awk -F/ '/^https:\/\//{print $3}' urls.txt | sort | uniq -c | sort -k 1n > hostnames.txt
```

That gave me ~1,400 hostnames.

## Cluster with LLMs

I passed these to O1 Pro and Gemini 2.5 Pro:

> Here are the sites I visit, with rough frequency. On Microsoft Edge, I can create workspaces. Based on this browsing behavior, what kinds of workspaces might I create? Give me multiple options.

Both gave a similar set of strategies, which I've implemented as:

- **Main**: email, calendar, tasks, etc.
- **Work**: work related sites (drive, expenses, HR platform, etc.)
- **Chill**: YouTube, Minesweeper, Netflix, etc.
- **Read**: blogs, articles, stuff I need to catch-up on
- **Code**: GitHub, StackOverflow, CodePen, etc.
- **Chores**: government services, shopping, etc.
- **AI**: ChatGPT, Gemini, Perplexity, etc.

I was surprised how **similar** a strategy both models converted to. Either these models **really** think alike, or my browsing pattern is a fairly common one. (My guess is the latter.)

### Write with LLMs

After setting up my groups, I needed to write this post. Instead of slow typing, I stepped out and [talked with ChatGPT](https://chatgpt.com/share/67f36093-e810-800c-a9d0-de9bfb7ecf86). (Talking to a machine in the office felt strange, so I changed my space.) I explained my whole process, and in about eight minutes, the first draft was done. Normally, writing takes much longer, but the voice chat made it quick and smooth.

The editing after that was manual and took 20 minutes.

### Things I learnt

- **Simple Patterns**: My browsing history shows clear patterns. AI helped me find groups I couldn't see before
- **Small Fixes - Big Wins**: A small challenge (opening a locked file) taught me a bunch of new useful stuff
- **Voice Made It Easy**: Talking with ChatGPT made writing fast and easy. It shows that speaking to a machine can save time
