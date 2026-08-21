---
title: Comic art style prompts
date: 2026-08-09T11:09:26+05:30
classes: wrap-code
categories:
- how-i-do-things
- llms
description: I create comic illustrations by combining a reusable prompt, an optional visual style, and any content I want to explain. ChatGPT and Gemini can design the comic before drawing it, making the process automatable.
tags: [prompt-engineering, image-generation, comic-strips, llms]
---

Many people commented that they liked my comic illustrations and asked how I create them. Here is my process:

1. Paste a reusable prompt fragment that'll take _any_ content, **think** about what to draw, then draw it.
2. Paste a style variation for different comic styles (optional).
3. Paste the content itself and run it.

I use ChatGPT with [gpt-image-2](https://developers.openai.com/api/docs/models/gpt-image-2) more often than Gemini with [Nano banana 2](https://gemini.google/overview/image-generation/).

Here are the prompts.

**STEP 1: Reusable Prompt Fragment**: I have a few of these right now:

[Comic _page_ prompt fragment](https://github.com/sanand0/blog/blob/d51ff28c1573e62d5d9dcff7caf04f1ffdd7ce85/pages/prompts/fragments.md#comic-page):

```markdown
Draw this as a full-color explainer comic page (portrait) - sequential explanation, friendly narrator, diagrams embedded inside panels, visual metaphors, self-aware captions, and clear cause-and-effect storytelling.
Style: expressive characters, comic-style ALL CAPS, vibrant modern colors, clear visual hierarchy.
Prefer pictures over words. Use recurring visual metaphors so the reader understands the idea even while skimming.

First, write a memorable storyline that captures the most important points to convey - as a single cohesive story.
Just reading the storyline should communicate the entire message unambiguously.
Critique the storyline: what is confusing, doesn't flow, or has low impact? Revise. Repeat until the storyline is GOOD!

Draw each storyline element (typically a sentence, but sometimes a continued phrase, or multiple sentences) as a panel's caption. (If there are 8 panels, there must be 8 storyline elements)
Each panel's image should support and strengthen its caption - and reinforcing past panels / anticipating future panels where helpful.
```

Example:

[![](https://sanand0.github.io/talks/2026-08-07-data-hack-summit/comic-page.avif)](https://sanand0.github.io/talks/2026-08-07-data-hack-summit/)

[Comic _strip_ prompt fragment](https://github.com/sanand0/blog/blob/d51ff28c1573e62d5d9dcff7caf04f1ffdd7ce85/pages/prompts/fragments.md#comic-strip):

```markdown
Draw this as a simple black and white line drawing comic strip (1:1) with minimal shading.
Single panel.
Style: expressive characters, comic-style ALL CAPS.
Prefer pictures over words.
No need to cover everything - just one key item is enough - e.g. the funniest, most important, or most surprising point.
Convey the INTENT of the point. An apt analogy that visually communicates instantly might work better than a literal depiction.
Keep it funny. The strip itself should make readers laugh.
```

Example:

[![](https://files.s-anand.net/images/2026-08-01-simple-writing-hurts-thinking.avif)](https://www.s-anand.net/blog/simple-writing-hurts-thinking/)

**STEP 2: Style Variation**: This is optional. Here are examples of a few different styles:

![](https://sanand0.github.io/llmartstyle/images/cat.elegant-brush-line.gpt-image-2.webp)
![](https://sanand0.github.io/llmartstyle/images/cat.ratty-line.gpt-image-2.webp)
![](https://sanand0.github.io/llmartstyle/images/cat.roundhead.gpt-image-2.webp)
![](https://sanand0.github.io/llmartstyle/images/cat.spot-black-economy.gpt-image-2.webp)

These are cataloged in my [LLM Art Style gallery](https://sanand0.github.io/llmartstyle/?category=comic) (see [blog post](https://www.s-anand.net/blog/llm-comic-styles/)).

**STEP 3**: Paste whatever content I want to illustrate. Some examples are:

- Transcripts of my talk
- Contents of my blog post
- An email reply I'm sending

---

The main insight is that ChatGPT and Gemini can _think_ about what best to draw, and _then_ draw it. So I can, with some careful prompting, delegate the comic design to them for _any_ content, making this an automatable flow.
