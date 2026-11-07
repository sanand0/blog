---
title: 28 Ways I Review Agents
date: 2026-11-06T10:13:29+08:00
categories:
- llms
- how-i-do-things
description: I collected 28 ways I review AI agents, based on more than 10,000 prompts. Examples include asking for writing that sounds like me and pausing when usage limits are near.
tags: [ai-agents, llm-prompts, verification]
---

Using the [same approach as specification and verification](https://www.s-anand.net/blog/52-ways-i-specify-and-verify-agents/) I looked at how I [_review_ agents](https://files.s-anand.net/pages/verification-techniques/#?m=review), i.e. what I comment on after they share an output.

[![](https://files.s-anand.net/images/2026-11-06-my-review-techniques.avif)](https://files.s-anand.net/pages/verification-techniques/#?m=review)

This page features the 28 review techniques I use. Some interesting ones:

1. **[Show your style](https://files.s-anand.net/pages/verification-techniques/#?m=review&show=28&t=show-your-style&open=1)**: I tell it why it doesn't sound like me, and how I _would_ have written it. [Real example](https://chatgpt.com/share/6aeddb89-2ae4-83ec-a5c3-33675ad0836d): "Still not in my style - revise more in line with these principles." <!-- https://chatgpt.com/c/6a44cce0-7880-83ec-b611-9fe0086d704a -->
2. **[Pause and resume](https://files.s-anand.net/pages/verification-techniques/#?m=review&show=28&t=pause-and-resume&open=1)**: Tell it not to exceed the usage limits. Real example: "We are at 96% usage of the 5h limit - so pause now and we can resume in a few hours."
3. **[More like this](https://files.s-anand.net/pages/verification-techniques/#?m=review&show=28&t=more-like-this&open=1)**: Tell it what you liked and go in that direction. [Real example](https://chatgpt.com/share/6aede65f-62b0-83ec-b34d-ecf9ab0c27f3): "Looks good. Give me 10 more." <!-- https://chatgpt.com/c/69fd96ba-15ec-83ea-b6a5-86bd30bb74bc -->
4. **[Take the best of each](https://files.s-anand.net/pages/verification-techniques/#?m=review&show=28&t=take-the-best-of-each&open=1)**: Give it other models' output and pick the best from each. [Real example](https://claude.ai/share/9001b652-5a74-4635-8b9d-2c5e800aa034): "Here is ChatGPT's response. Take what's better, drop what's worse, follow up on new ideas this gives you, and revise your response." <!-- https://claude.ai/chat/bc13a5e3-5c95-4a2e-8703-88c9bf38775f -->
5. **[Say “I meant…”](https://files.s-anand.net/pages/verification-techniques/#?m=review&show=28&t=say-i-meant&open=1)**: Clarify your real intent. "Sorry, I meant round off the 95% activity window in EACH namespace."

---

These are based on ~6.7K real responses. **Skim** through them and if you spot something interesting, _test it out_. If it works for you, share it with others.
