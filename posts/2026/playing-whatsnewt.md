---
title: Playing whatsnewt
date: 2026-10-11T22:20:00+08:00
categories:
- coding
- llms
description: I had Claude and ChatGPT play Python 3.15's whatsnewt text adventure for me, discovering new Python features and reflecting on how AI lets me choose the effort I put into learning.
tags: [learning-strategies, ai-agents, python, llms]
---

Python 3.15 released with a TUI text adventure you can run via `uvx --python 3.15 whatsnewt`.

I _love_ text adventures, but not so much that I would spend a weekend learning a new game rather than playing Minecraft. So I had [Claude](https://sanand0.github.io/research/whatsnewt2/) and [ChatGPT](https://sanand0.github.io/research/whatsnewt/) "play" it for me.

[![](https://files.s-anand.net/images/2026-10-11-playing-whatsnewt.webp)](https://sanand0.github.io/research/whatsnewt2/)

It's more a reading experience than a playing experience, but that can be pretty engaging, too. What I learnt by reading it (that I didn't know before) was:

- `xyzzy` and `plugh` are Collosal Cave magic words.
- [`.start` files](https://docs.python.org/3.15/library/site.html#site-start-files) let you run package-specific code before the interpreter starts.
- Set `__lazy_modules__` to a list (or set, dict, or whatever) of modules to be lazy-imported.
- `frozendict` comparisons are order independent, though it preserves order. `frozendict({1:2,3:4}) == frozendict({3:4,1:2})` is `True`.
- [`TypedDict`](https://docs.python.org/3.15/library/typing.html#typing.TypedDict) lets you define dicts with specific types for each key. Gently nudging Python towards TypeScript.
- [`TypeForm`](https://peps.python.org/pep-0747/) seems useful but I still haven't wrapped my head around it.

This is as far as I got at [step 57 / 146](https://sanand0.github.io/research/whatsnewt2/#step=57) and I still more to read.

But, a few learnings about learning:

- **Learning comes with effort**. I didn't learn the stuff above skimming through the Python 3.15 release docs.
- **Effort reducing chance of learning**. I wouldn't bother playing the TUI or reading the full docs - because it takes so much effort.
- **AI lets you control effort**. You have more control over your learning. You can choose the level of effort. **That's inclusive**, i.e. more people can learn.
- **AI reduces author control**. AI transfers control to your hands. **That's less prescriptive**, i.e. you may not get the desired result.
