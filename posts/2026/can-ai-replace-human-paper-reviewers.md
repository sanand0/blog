---
title: Can AI Replace Human Paper Reviewers?
date: 2026-01-13T09:55:45+05:30
categories:
  - llms
  - visualisation
description: I analyzed the Agents for Science conference data using ChatGPT and Claude to compare AI peer reviewers. I found they wildly disagree and exhibit 100% false confidence, though they excel at catching factual hallucinations.
keywords: [agents for science, peer review, large language models, openreview, data analysis, hallucinations, academic publishing]
---

Stanford ran a conference called [Agents for Science](https://agents4science.stanford.edu/). It's a conference for AI-authored papers, peer reviewed by AI.

They ran three different AI systems on every paper submitted, alongside some human reviewers. The details of each of the 315 papers and review are available on [OpenReview](https://openreview.net/group?id=Agents4Science/2025/Conference).

I asked Codex to [scrape the data](https://github.com/sanand0/datastories/blob/main/ai-agents-for-science/scrape.py), ChatGPT to [analyze it](https://chatgpt.com/share/6965c3bf-8670-8003-9788-732ad0ecd259), and Claude to [render it as slides](https://claude.ai/share/0c919398-d2f8-4682-a6ea-c68f24b98ab2).

[The results are interesting!](https://sanand0.github.io/datastories/ai-agents-for-science/) I think they're also a reasonably good summary of the current state of using AI for peer review.

1. **The three AI reviewers _wildly disagree_ with each other.**

   Imagine hiring three movie critics to rate the same film. One gives it 2 stars, another gives it 6 stars, and the third gives it 4 stars. **Same movie, completely different conclusions.** That's what's happening with these AI reviewers-on almost half of all papers.

2. **"Averaging" the three AIs _doesn't actually help_**

   You might think: "Just average the three scores! That'll balance out their biases." But here's the problem: **the generous AI (AIRev2) uses much bigger numbers**. When you average, its voice drowns out the others. It's like having three judges, but one shouts and two whisper.

3. **Every AI claims to be _100% confident_ - even when they're wrong**

   Reviewers are asked "How confident are you in your assessment?" on a 1-5 scale. **Every single AI review said "5 out of 5-totally confident."** All 751 of them. Even when two AIs looked at the same paper and reached opposite conclusions, both claimed maximum confidence.

4. **AI and human reviewers _see different things_**

   On papers that got both AI and human reviews, we compared their scores. The AIs were almost always **more generous** than humans-by about 1 full point on average. And in some cases, AI said "excellent!" while the human said "this is broken."

5. **AI reviewers can _catch obvious problems_**

   AI reviewers successfully flagged papers with **impossible claims**-like citing AI models that don't exist yet, or referencing datasets from the future. These are "fact check" problems that don't require deep expertise, just attention to detail.

6. **Use AI disagreement as a _signal, not noise_**

   When the "generous AI" loves a paper but the "skeptical AI" hates it, that's not random noise-it's **useful information**. It means the paper's fate depends on standards (rigor vs. novelty), not just quality. These are exactly the papers humans should look at.

[![](https://files.s-anand.net/images/2026-01-13-can-ai-replace-human-paper-reviewers.avif)](https://sanand0.github.io/datastories/ai-agents-for-science/)

---

- [Read the prompts](https://github.com/sanand0/datastories/blob/main/ai-agents-for-science/prompts.md)
- [Download the full reviews dataset](https://github.com/sanand0/datastories/blob/main/ai-agents-for-science/reviews.json)
