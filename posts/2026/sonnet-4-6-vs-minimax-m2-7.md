---
title: Sonnet 4.6 vs MiniMax M2.7
date: 2026-03-24T17:06:02+08:00
categories:
  - llms
  - coding
description: Even when two models can complete the same task, they differ noticeably in narrative quality, visual ambition, and implementation details, so model choice meaningfully affects outcomes.
keywords: [LLM comparison, Sonnet, MiniMax, evaluation, data stories, model capabilities]
---

Based on several (i.e. two) recommendations, I subscribed to [MiniMax](https://platform.minimax.io/). At $10/month, you get 1,500 requests every 5 hours and 15,000 every week. That's a LOT!

Using the [same prompt](https://sanand0.github.io/talks/2025-07-18-tug-true-but-irrelevant-rob-schrauwen/prompts.md) I had [Claude Code](https://platform.minimax.io/docs/token-plan/claude-code) generate two data stories:

<a href="https://sanand0.github.io/talks/2025-07-18-tug-true-but-irrelevant-rob-schrauwen/index.html">
  <figure>
    <img src="https://files.s-anand.net/images/2026-03-24-rob-data-story-claude.avif" alt="In July 2025, in the heavy morning warmth of Thiruvananthapuram, the opening talk at the TeX User Group annual conference began with a crayon drawing. Not a polished diagram. Not a carefully curated slide. A hand-drawn family tree on crumpled paper, made by a six-year-old girl named Emily, who had a problem to solve. She had told her teacher she had seven grandmothers. The teacher declared it impossible. Emily went home and built a proof." />
    <figcaption>The first paragraph, by Claude Sonnet 4.6</figcaption>
  </figure>
</a>

<a href="https://sanand0.github.io/talks/2025-07-18-tug-true-but-irrelevant-rob-schrauwen/minimax.html">
  <figure>
    <img src="https://files.s-anand.net/images/2026-03-24-rob-data-story-minimax.avif" alt="There is a drawing by a six-year-old girl in Amsterdam that contains more wisdom about data quality than three decades of enterprise content architecture. In it, seven figures stand in a family tree — each grandmother numbered with a circle, each grandfather conspicuously absent. The girl is Rob Schrauwen's granddaughter. She was asked to prove she had seven grandmothers; she drew them all, labeled them carefully, and in doing so invented continuous data quality, unique identifiers, and a knowledge graph — all before she learned to spell &quot;Hetty.&quot;" />
    <figcaption>The first paragraph, by MiniMax M2.7</figcaption>
  </figure>
</a>

Here's my comparison of the two. It's partly based on [Claude Opus 4.6's comparison](https://sanand0.github.io/talks/2025-07-18-tug-true-but-irrelevant-rob-schrauwen/comparison.md) but I felt the same way.

| Dimension               | Sonnet 4.6                                  | MiniMax M2.7                |
| ----------------------- | ------------------------------------------- | --------------------------- |
| **Narrative quality**   | Immersive                                   |                             |
| **Content coverage**    | Comprehensive                               |                             |
| **Visual design**       | More varied, ambitious bands, no errors     |                             |
| **CSS**                 |                                             | Better use of CSS variables |
| **Tooltips**            | Richer, comprehensive, `data-tip`           |                             |
| **Modals/popups**       | Richer, more types, more details            |                             |
| **Animated SVGs**       | Richer, visually distinctive, sophisticated |                             |
| **Slides**              | Larger readable grid                        |                             |
| **Code samples**        | XML vs JSON-LD side-by-side                 |                             |
| **External references** | Far more authoritative links                |                             |
| **Accessibility**       | ARIA, keyboard, alt text                    |                             |
| **Generation quality**  | Clean, no Chinese character artifacts       |                             |

In other words, Sonnet 4.6 is a _clear_ winner on nearly every dimension.

But the cost factor is _too_ big a difference to ignore. It feels like a 10x difference. So the question probably is: what can I do with a _reasonably_ good model that can generate 10X the quantity at the same price?

(To be fair, [GPT 5.4 Mini at 75c/MTok](https://openrouter.ai/openai/gpt-5.4-mini) and [Gemini 3 Flash at 50c/MTok](https://openrouter.ai/google/gemini-3-flash-preview) are not far from [MiniMax M2.7 at 30c/MTok](https://openrouter.ai/minimax/minimax-m2.7) - but their [code quality](https://arena.ai/leaderboard/code) seems lower. I generated a [Codex - GPT 5.4 Mini version](https://sanand0.github.io/talks/2025-07-18-tug-true-but-irrelevant-rob-schrauwen/gpt-5.4-mini-xhigh.html) and while it has fewer errors it has even less visual style and narrative quality.)

**Computer use** feels like a candidate. I used [Rodney](https://github.com/simonw/rodney) to research what drives my LinkedIn reach & engagement, and update my [SKILL.md](https://github.com/sanand0/scripts/blob/f08ffd11e221c5a9ef58d5da814aaad9985bd422/agents/linkedin-cdp/SKILL.md).

I could try experimenting with sub-agents, doing bulk analysis (e.g. of code, transcripts, images), data discovery, etc. The crux of these is parallelization - something I have not explored much.

It looks like twe're entering an era where there are two kinds of use cases: high-quality for the best models, large-scale for the cheap models. The question is: how do I make the most of both?

---

[Source Code](https://github.com/sanand0/talks/tree/52ad2aa775cd4e0f1e0ad8e6199ce7754a2663ac/2025-07-18-tug-true-but-irrelevant-rob-schrauwen)

---

**UPDATE**: Cheap models (or at least MiniMax M2.7) may be far less useful than I thought. I used MiniMax M2.7 with Claude Code for:

- 24 Mar 2026: Email analysis. I had it review my 15-year Gramener email archive for key events for a book. But it fetched too few results, so I switched to Codex (GPT 5.4 xhigh). <!-- claude --resume 1c3edc84-5781-4684-bd0d-565fafc5b2b9 -->
- 25 Mar 2026: [Capture The Flag](https://play.picoctf.org/practice). But it couldn't solve problems, so I switched to Codex (GPT 5.4 xhigh). <!-- claude --resume 525d2631-cf8b-4665-bfdc-e55b70cb7340 -->
- 25 Mar 2026: Songs download. I had it find popular Tamil songs and download them from YouTube. But the metadata was poor, so I switched to my own song collection. <!-- claude --resume f4d3a74b-0bc8-4431-8084-f56be44a4a53 -->
- 26 Mar 2026: LEAN proofs. It started making too many basic mistakes (spelling errors in code!) I switched to Copilot (GPT 5.4 xhigh). <!-- claude --resume a0836a15-6b82-45ef-8174-bcd10272a62e -->
- 29 Mar 2026: Calvin & Hobbes image analysis. It couldn't even read the images and confidently saw "Hobbes stuck to a baseball bat with Mom & Dad" in a strip that only featured Calvin & Susie. <!-- claude --resume 9dd15966-0c65-49bf-af3b-506f4bab5d39 -->

The main problems are:

- **It errs confidently**. It doesn't do ROT13 well. It can't see images. It mis-understands error messages. It assigned my earlier company's incorporation date (NGIMAGE) as Gramener's. It made Vijay Sethupathi a lyricist. When a process failed with just 12% coverage, it just continued. It just _reported what's done, not what's missing_.
- **It's a slow learner**. For [picoCTF](https://picoctf.org/), it had the pieces but couldn't assemble them. Claude Code resets the cwd, but it never switched to absolute paths. It mixed `uv run` with `python3`. It rewrites, resets or waits instead of diagnosing.

It's best for simple, single-step tasks. Not where knowledge, accuracy, research matters. When using it, keep tasks small and verify correctness, completeness.
