---
title: LinkedIn Blog
date: 2026-07-31T22:40:14+08:00
description: Recommend LinkedIn posts from my blog
classes: wrap-code
tags: [linkedin, personal-blog, data-analysis, productivity, developer-workflow]
---

```markdown
Pick next month's LinkedIn posts from my blog.

- Blog: ~/code/blog/posts/YYYY/\*.md (frontmatter: title, date, categories, tags, description, and `linkedin:` if already posted)
- LinkedIn dump: ~/Documents/data/linkedin-posts.jsonl (type=post and type=comment; posts have impressionCount, reactionCount, commentCount, repostCount, postedText as a RELATIVE age like "2mo")

Based on a Jul 2026 analysis of 169 posts + LinkedIn metrics:

- Audience: ~750 founder/CEO/CTO/chief titles, ~570 engineers and data scientists, ~280 product. India and Singapore heavy. They read for a decision they can act on or a story they recognise.
- My top posts have a reach (vs a typical post that month) of:
  1. 8.6x - Everyday observation with a twist. Specific, visual, slightly absurd, mild grievance welcome. E.g. Plastic-cover-on-phone 185K, no-entry-for-sandals 47K, kind-air-hostess 36K, hot-cookies 27K.
  2. 14-87x - A number that flips a default decision. "GPU or API" 663K, "which LLM gets better grades" 64K. Ensure a concrete decision.
  3. 34x - A free thing usable today. TDS-free 285K, 60 reposts.
  4. 4-12x - Exact, reproducible "here's how I did it". Voice-to-slides 93K.

What loses: prompt-engineering 0.63x, vibe-coding 0.72x, coding 0.80x, ai-agents 0.79x, llms 0.89x.

Workshop recaps get 1,700-2,700. Under 250 words gets a median 8,020 impressions; over 900 words gets 5,303.
Pure data analyses (IMF, Wikipedia) get respectable but modest numbers unless they carry personal stakes or an actionable consequence.

Reposts (save intent) run highest on benchmarking (7.0 avg) and education (5.9), even when reach is modest.
Treat reposts and comments as better signal than reactions.

The 2026 baseline is roughly half of 2025 (~4,000 vs ~8,000 median), so don't compare raw impressions across years.

I no longer link the blog on LinkedIn: link posts get throttled. So we'll rewrite.

## Method

1. Take blog posts from the last 3 months.
2. Drop any with a `linkedin:` field. Then DO NOT TRUST that field - it has false negatives. For every remaining candidate, keyword-check its distinctive terms (proper nouns, tool names, coined phrases) against BOTH post and comment text in the full dump. Report anything already live. Example of a real miss: "How IMF mis-forecasts GDP growth" had no frontmatter field but was posted a month earlier.
3. Note the dump's max scrapedAt. Anything dated after it is UNVERIFIABLE - say so rather than assuming it's unposted.
4. Clean the dump: discard records where reactionCount > impressionCount (a scraper bug inflates some counts by ~1e9).
5. Auto-exclude: "Things I Learned" digests, workshop and talk summaries, dev-tooling posts (ffmpeg, redirect tracking, shell utilities). These are the developer posts I deliberately keep off LinkedIn.
6. Score each candidate against the four winning patterns. Prefer posts already under 500 words.
7. Portfolio rule: at least 2 of 5 must be non-AI or non-LLM. My feed is already LLM-saturated and that category runs below my own baseline.

## Output - for each of 5 picks, in priority order

- Title, date, word count, blog URL
- Which pattern it hits, and the specific past post it resembles
- A one-line LinkedIn hook, in my voice, that I can use as the opening line
- What to cut for LinkedIn (name sections, not "shorten it")
- Any risk (named company, staleness, tone)
  Then: 3 near-misses in one line each, and a list of what you excluded and why.
```

- 31 Jul 2026. Created. Sources:
  - https://chatgpt.com/c/6a6ab214-fd78-83ec-b319-3f5645325155
  - https://claude.ai/chat/c3dd952f-1a20-44a2-8eb3-29860201d8ee

Feedback loop - run this first each month

> Check which of last month's 5 picks I actually posted, and pull their metrics from the current dump. Report the hit rate and any pattern that over- or under-performed the multipliers above. If a pattern misses by more than 2x on 3+ posts, say the model needs re-deriving. Otherwise leave it alone.
