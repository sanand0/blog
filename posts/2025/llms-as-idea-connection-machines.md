---
title: LLMs as Idea Connection Machines
date: "2025-08-18T09:48:39Z"
lastmod: "2025-08-18T09:48:41Z"
categories:
  - llms
wp_id: 4173
---

![LLMs as Idea Connection Machines](/blog/assets/ChatGPT-Image-Aug-18-2025-03_17_26-PM.webp)

In a recent talk at IIT Madras, I highlighted how large language models (LLMs) are taking over every subject of the MBA curriculum: from finance to marketing to operations to HR, and even strategy.

One field that seemed hard to crack was innovation. Innovation also happens to be my role.

But LLMs are encroaching into that too.

LLMs are great **connection machines**: fusing two ideas into a new, useful, surprising idea. That's core to innovation. If we can get [LLMs daydreaming](https://gwern.net/ai-daydreaming), they could be innovative too.

Each day, I jot down 3-5 things I learn (ideas, facts, insights) into a [daily log](https://til.s-anand.net/). I built an ["ideator" tool](https://tools.s-anand.net/ideator/) that:

1. Loads my daily log entries
2. Randomly selects two ideas
3. Sends them, along with a well-crafted system prompt, to an LLM
4. Has it write a list of big, useful, non-obvious ideas, each with a name, a one-line description, and a novelty/utility score
5. Picks one and explains how to implement it.

Here are a few **real, useful examples** ideator surfaced:

- **LLM Pre-Mortem**. Fuse: Project risk + speculative generation. Have LLMs imagine what could go wrong with a project, then generate test cases for each risk that fail early/fast, and THEN write the code.
- **Mood-Based Task Matching**. Fuse: Emotion impact + Leveraging Assets. Suggested creating a "mood market portfolio". Tag tasks by **ideal emotional state**, e.g., "calm", "energized", "curious". Plan day to match tasks & mood.
- **Flaw-First Studio**. Fuse: Design critique + incremental coding. Have AI coding agents make micro changes, show live previews, and approve to proceed. Surfaces flaws early.
- **Consultant-to-LLM Bridge**. Fuse: Domain knowledge + autonomous agents. Treat yourself as an "API" the LLM can consult by feeding it your preferences and rules of thumb.

A few things I've learned are:

- LLMs are good at **connecting random concepts** into thoughtful ideas.
- The **random** selection of ideas is key. It breaks my usual mental patterns.
- Scoring helps me pick the better ideas.

You don't need my [ideator tool](https://tools.s-anand.net/ideator/). A simple version is:

- Keep a log of things you learn or observe each day
- Pick two random entries
- Feed them with a prompt like below to ChatGPT or Claude

```yaml
You are a radical concept synthesizer hired to astound even experts.

Generate a big, useful, non-obvious idea aligned with "__GOAL__" fusing provided <CONCEPT>s with concrete next steps.

__NOTES__

THINK:

1. Generate 5+ candidate ideas (searching online for context if useful) using these lenses:
   - Inversion
   - Mechanism-transplant
   - Constraint-violation
   - Scale-jump
   - Oblique strategies
   - Any other radical angle
2. Score each for
   - Novelty: 1=common; 3=unusual; 5=not seen in field
   - Utility: 1=nice-to-have; 3=team-level impact; 5=moves a key metric in <=90 days
3. Pick top score. Tie > lower complexity.

OUTPUT:

- INSIGHT: 1-2 sentences.
- HOW TO BUILD: Explain how it works.
- HOW TO TEST: 3 bullets, doable in <=30 days.
- WHAT'S SUPRISING: What convention does this challenge?
- CRITIQUE: 2 sentences: biggest risk & mitigation

STYLE:

- Plain English; no hype; easy to understand. Define new terms in parentheses.
```

---

MBAs are trained to spot patterns. Innovators are trained to break them. LLMs, with the right nudges, do both.

Let them.

[LinkedIn](https://www.linkedin.com/posts/sanand0_llms-are-great-%F0%9D%97%B0%F0%9D%97%BC%F0%9D%97%BB%F0%9D%97%BB%F0%9D%97%B2%F0%9D%97%B0%F0%9D%98%81%F0%9D%97%B6%F0%9D%97%BC%F0%9D%97%BB-%F0%9D%97%BA%F0%9D%97%AE%F0%9D%97%B0%F0%9D%97%B5%F0%9D%97%B6%F0%9D%97%BB%F0%9D%97%B2%F0%9D%98%80-activity-7363146089996148738-wX-N)

---

## Comments

<!-- wp-comments-start -->

- **[Measuring talking time with LLMs - S Anand](/blog/measuring-talking-time-with-llms/)** _24 Aug 2025 11:56 am_ _(pingback)_:
  […] ← Previous Post […]

<!-- wp-comments-end -->
