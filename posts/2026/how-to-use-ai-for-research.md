---
title: How to use AI for research
date: 2026-04-04T23:30:53+08:00
categories:
  - llms
description: AI research works much better when you specify failure modes, define validation criteria, and guide the system with concrete examples instead of vague requests.
tags: [prompting, validation, research-workflows, synthesis]
---

<!-- https://chatgpt.com/c/69cf42a9-ed04-839b-bdf1-e010677d81c7 -->

I asked ChatGPT to research universities' AI policies. [Here is the report](https://sanand0.github.io/datastories/ai-policies/)

Here are the four lessons I learned from that - about how to use AI for research.

![](https://files.s-anand.net/images/2026-04-03-how-to-use-ai-for-research.avif) <!-- https://gemini.google.com/u/2/app/9f3cc9fb9c8c8cb4 -->

**1. Show examples of failures to avoid**. [Jivraj's earlier research](https://jivraj-18.github.io/university_ai_usage/output/) kept surfacing AI policies universities had _researched_, not written for themselves!. So I told ChatGPT to:

> ... double-check that they ARE, in fact, about their own use of AI - not policies they're proposing for others or are researching.

This is called **pre-specifying exclusions**. Giving negative examples help. [Wei (2022)](https://arxiv.org/abs/2201.11903).

**2a. "Double-check" doesn't always work**. Though I told ChatGPT to "double-check", it still got things wrong. For example, it cited MIT's [AI policy home page](https://ist.mit.edu/ai-guidance) as evidence that the policy covers students and faculty, just because the words were present. That's not right!

Models get over-confident - and that's exactly when they _don't_ double-check. Asking them to double-check is a good habit, but not fail-safe. [Kadavath (2022)](https://arxiv.org/abs/2207.05221)

**2b. Expicitly tell it to find mistakes**. I told it to:

> Find mistakes in as many claims as you can.

This is stronger than "double-check". It turns the model against itself, and it worked _quite_ well.

**1. Show examples of failures to avoid**. (Repeat.) When asking it to find mistakes, I gave it the same example.

> ... MIT, "covers_faculty_or_staff" cites "quote": "Students • Faculty and Staff • Visitors and Guests • Generative AI use at MIT". But that's actually a set of links to Students, Faculty and Staff, etc. It's not evidence that the POLICY covers them - and I'm quite sure the policy isn't for guests!

That's [few-shot prompting](https://arxiv.org/abs/2005.14165). Concrete examples beat abstract instructions.

**3. Ask it to list failures explicitly**. I told it:

> I am also interested in universities that conspicuously lack a policy ...

Without that, it might have returned _only_ positive hits. Missing evidence and failures are important data, too!

**4. Break large tasks into batches**. When I asked it to research 20 universities, it made several mistakes. Instead:

> This may be a complex task, so let's just do this for the first four Universities.

Now, it didn't make any mistakes! Sometimes, it gets [lost in the middle](https://arxiv.org/abs/2307.03172) for long tasks.

---

So there it is - the four rules of AI research I learned from this exercise:

1. Show examples of failures to avoid
2. "Double-check" doesn't always work. Expicitly tell it to find mistakes
3. Ask it to list failures explicitly.
4. Break large tasks into batches.
