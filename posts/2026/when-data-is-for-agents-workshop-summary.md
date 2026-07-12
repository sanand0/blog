---
title: When Data is for Agents - Workshop Summary
date: 2026-07-11T21:24:39+05:30
categories:
  - talks
  - llms
description: I summarize my workshop on how AI agents process data, showing how to use LLMs to research formats, write benchmarks, audit prompts, and turn the findings into reusable skills.
tags: [ai-agents, experiments, benchmarking, structured-data, llms, prompt-engineering]
---

Here's roughly what I said in my [When Data is for Agents](https://hasgeek.com/fifthelephant/when-data-is-for-agents-workshop/) workshop for [Fifth Elephant](https://hasgeek.com/fifthelephant/) on 7 Jul 2026.

Or you can read the [detailed AI-generated version](https://sanand0.github.io/talks/2026-07-07-when-data-is-for-agents-fifth-elephant/) if you prefer - it has all the prompts, links, results, etc.

---

I think agents prefer data in a different form than humans. But I don't know.

So, everyone, open ChatGPT (or Claude or whatever), [research](https://github.com/sanand0/talks/blob/226a6208889bf3d2bb1fb24d923d9298ec3fc81d/2026-07-07-when-data-is-for-agents-fifth-elephant/research-prompt.md) and ask it!

Now, let's [collate them](https://github.com/sanand0/talks/blob/226a6208889bf3d2bb1fb24d923d9298ec3fc81d/2026-07-07-when-data-is-for-agents-fifth-elephant/collation-prompt.md) and [see the result](https://chatgpt.com/share/6a525953-3da0-83e8-94a5-a8d99b291fc7).

Aha! Looks like:

1. Progressive, just-in-time access beats feeding full context at once
2. For changing, text-heavy corpora, grep-style navigation can beat embeddings
3. CSV beats JSON on accuracy per token

Hmm... let's test them one by one.

Everyone, ask Codex (or Claude Code) to [run a benchmark](https://github.com/sanand0/talks/blob/226a6208889bf3d2bb1fb24d923d9298ec3fc81d/2026-07-07-when-data-is-for-agents-fifth-elephant/benchmark-prompt.md).

What? All thirteen of your results said, "It makes no difference?" Huh...

Claude, [did my benchmarking prompt do a good job](https://claude.ai/share/19d72406-b262-482e-895e-c7da0fde3382)?

What? I messed up my benchmarking prompt? It gave all the data at once instead of progressively? OK, give me the revised prompt.

OK, everyone, try this prompt. What does it say?

Aha! Yes, progressive disclosure costs 2.5x - 25x less for the same accuracy. Cool!

Let's try another experiment. What? I totally messed up that prompt as well? Er... we're short of time?

Fine, wrap up, then. Claude, convert what we learnt into a [skill](https://github.com/sanand0/talks/blob/226a6208889bf3d2bb1fb24d923d9298ec3fc81d/2026-07-07-when-data-is-for-agents-fifth-elephant/corpus-for-agents-skill.md).

OK, folks, my takeaways:

1. I don't know what formats agents prefer, but we can ask AI to research.
2. I don't know if the research is right, but we can ask AI to create a benchmark.
3. I don't know if the benchmark is right, but we can ask AI to audit it.
4. I don't know if I'll remember what's valid, so we can ask AI to create and reuse skills.

---

![](https://sanand0.github.io/talks/2026-07-07-when-data-is-for-agents-fifth-elephant/summary.avif)
