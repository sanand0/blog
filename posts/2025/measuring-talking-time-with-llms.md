---
title: Measuring talking time with LLMs
date: "2025-08-24T06:26:22Z"
lastmod: "2025-08-24T06:26:24Z"
categories:
  - llms
wp_id: 4177
---

![Measuring talking time with LLMs](/blog/assets/ChatGPT-Image-Aug-24-2025-01_24_22-PM.webp)

I record my conversations these days, mainly for LLM use. I use them in 3 ways:

1. **Summarize** what I learned and the next steps.
2. **Ideate** as raw material for my Ideator tool: /blog/llms-as-idea-connection-machines/
3. **Analyze** my transcript statistics.

For example, I learned that:

- When I'm interviewing, others ramble (speak long per turn), I am brief (less words/turn) and quiet (lower voice share). In one interview, I spoke ~30 words per turn. Others spoke ~120. My share was ~10%.
- When I'm advising or demo-ing, I ramble. I spoke ~120 words per turn in an advice call, and took ~75% of the talk-time.
- This pattern is independent of meeting length and group size.

I used [Codex CLI](https://github.com/openai/codex) (command-line tool) for this, with the prompt:

> Go through the transcripts in this folder and estimate the % of time Anand was speaking vs others, by conversation.

Then I prompted for correlations and interpretations. This combines three things I find powerful:

1. LLMs writing & **running code**
2. LLMs **interpreting** the results
3. Running on **local** data in my machine

LLMs working on local **docs** (not data) is new to me. I plan to do much more with it.

[LinkedIn](https://www.linkedin.com/posts/sanand0_i-record-my-conversations-these-days-mainly-activity-7365268557162565635-fc7w)
