---
title: Simple writing hurts thinking
date: 2026-08-01T14:00:27+08:00
categories:
  - llms
description: I tested if asking ChatGPT to simplify its writing using ASD-STE100 hurts its thinking. My experiment showed simplification reduces source checking and output quality. Let AI think complexly first, then ask for a simple explanation.
tags: [llms, chatgpt, prompt-engineering, writing-style, benchmarking, ai, s-anand]
---

![](https://files.s-anand.net/images/2026-08-01-simple-writing-hurts-thinking.avif)

As agents get smarter, and when we asking questions outside our expertise, it's pretty hard to understand what they're saying.

Andrew Carr [uses](https://x.com/andrew_n_carr/status/2081534245370314816) "only report to me in ASD-STE100 Simplified Technical English" to simplify their writing.
Ben Sehl [suggested](https://x.com/benjaminsehl/status/2082158002958741746) making this a permanent instruction.

But, does simplifying the writing worsen their thinking?

<!-- https://chatgpt.com/c/6a6d770d-9d68-83ec-b544-84a7aa1ecdc6 + https://claude.ai/chat/7788dcc8-dd41-4605-843b-7c418d675b8a -->

I tested six tasks on ChatGPT (GPT 5.6 Sol), with and without this suffix: "Answer in ASD-STE100".

| Task                                                                                                            | Without                                                                                                        | With suffix                                                                                                                |
| --------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| [Model benchmarking](https://github.com/sanand0/research/blob/main/simplification-prompt/question/1.md)         | [Result](https://github.com/sanand0/research/blob/main/simplification-prompt/result/1a.md): 66 sources, 1m 31s | [Result](https://github.com/sanand0/research/blob/main/simplification-prompt/result/1b.md): 44 sources, 41s                |
| [Causal diagnosis](https://github.com/sanand0/research/blob/main/simplification-prompt/question/1.md)           | [Result](https://github.com/sanand0/research/blob/main/simplification-prompt/result/2a.md)                     | [Result](https://github.com/sanand0/research/blob/main/simplification-prompt/result/2b.md)                                 |
| [Decision under uncertainty](https://github.com/sanand0/research/blob/main/simplification-prompt/question/1.md) | [Result](https://github.com/sanand0/research/blob/main/simplification-prompt/result/3a.md)                     | [Result](https://github.com/sanand0/research/blob/main/simplification-prompt/result/3b.md)                                 |
| [Experimental design](https://github.com/sanand0/research/blob/main/simplification-prompt/question/1.md)        | [Result](https://github.com/sanand0/research/blob/main/simplification-prompt/result/4a.md)                     | [Result](https://github.com/sanand0/research/blob/main/simplification-prompt/result/4b.md)                                 |
| [Evidence and judgment](https://github.com/sanand0/research/blob/main/simplification-prompt/question/1.md)      | [Result](https://github.com/sanand0/research/blob/main/simplification-prompt/result/5a.md): 123 sources, 2m 4s | [Result](https://github.com/sanand0/research/blob/main/simplification-prompt/result/5b.md): 84 sources, 5m 4s              |
| [Adversarial system design](https://github.com/sanand0/research/blob/main/simplification-prompt/question/1.md)  | [Result](https://github.com/sanand0/research/blob/main/simplification-prompt/result/6a.md): 97 sources, 2m 20s | [Result](https://github.com/sanand0/research/blob/main/simplification-prompt/result/6b.md): 26 sources, 3m 44s, wrote code |

The simple writing prompt reduced the number of sources it checked. (Thinking time varies.)

I [evaluated](rubric.md) the quality of the results on ChatGPT (GPT 5.6 Sol):

| Task | Order | Winner | Correctness | Key drivers | Mechanism | Caveats | Calibration | Actionability | Eval                                                                                     |
| ---: | ----- | :----: | :---------: | :---------: | :-------: | :-----: | :---------: | :-----------: | ---------------------------------------------------------------------------------------- |
|    1 | A, B  |   🔴   |     🔴      |     🔴      |    🔴     |   🔴    |     🔴      |      🔴       | [Eval](https://github.com/sanand0/research/blob/main/simplification-prompt/evals/1ab.md) |
|    1 | B, A  |   🔴   |     🔴      |     🔴      |    🔴     |   🔴    |     🔴      |      🔴       | [Eval](https://github.com/sanand0/research/blob/main/simplification-prompt/evals/1ba.md) |
|    2 | A, B  |   🔴   |     🔴      |     🔴      |    🔴     |   🔴    |     🔴      |      🔴       | [Eval](https://github.com/sanand0/research/blob/main/simplification-prompt/evals/2ab.md) |
|    2 | B, A  |   🔴   |     🟡      |     🔴      |    🔴     |   🔴    |     🔴      |      🔴       | [Eval](https://github.com/sanand0/research/blob/main/simplification-prompt/evals/2ba.md) |
|    3 | A, B  |   🔴   |     🟡      |     🔴      |    🔴     |   🔴    |     🔴      |      🔴       | [Eval](https://github.com/sanand0/research/blob/main/simplification-prompt/evals/3ab.md) |
|    3 | B, A  |   🔴   |     🟡      |     🔴      |    🔴     |   🔴    |     🔴      |      🔴       | [Eval](https://github.com/sanand0/research/blob/main/simplification-prompt/evals/3ba.md) |
|    4 | A, B  |   🔴   |     🔴      |     🔴      |    🔴     |   🔴    |     🔴      |      🔴       | [Eval](https://github.com/sanand0/research/blob/main/simplification-prompt/evals/4ab.md) |
|    4 | B, A  |   🔴   |     🟢      |     🔴      |    🔴     |   🔴    |     🟡      |      🔴       | [Eval](https://github.com/sanand0/research/blob/main/simplification-prompt/evals/4ba.md) |
|    5 | A, B  |   🔴   |     🔴      |     🔴      |    🟡     |   🔴    |     🔴      |      🔴       | [Eval](https://github.com/sanand0/research/blob/main/simplification-prompt/evals/5ab.md) |
|    5 | B, A  |   🔴   |     🔴      |     🔴      |    🔴     |   🔴    |     🟢      |      🔴       | [Eval](https://github.com/sanand0/research/blob/main/simplification-prompt/evals/5ba.md) |
|    6 | A, B  |   🔴   |     🔴      |     🔴      |    🔴     |   🔴    |     🔴      |      🔴       | [Eval](https://github.com/sanand0/research/blob/main/simplification-prompt/evals/6ab.md) |
|    6 | B, A  |   🔴   |     🔴      |     🔴      |    🔴     |   🔴    |     🔴      |      🔴       | [Eval](https://github.com/sanand0/research/blob/main/simplification-prompt/evals/6ba.md) |

🟢 = Simplification improves quality. 🟡 = Tie. 🔴 = Simplification worsens quality.

(Each pair was compared twice, in both orders (A, B) and (B, A) - to reduce position bias.)

There's no doubt that asking ChatGPT to "Answer in ASD-STE100" reduces its thinking quality. (It might be worth re-testing this in a few months.)

So, what should we do for now? My thoughts:

1. Don't simplify the writing initially. Let it think. THEN, ask for a simple explanation.
2. Continue conversations by deleting/editing the simplification.
3. Or, _don't_ read it. Tell it to do what you would do after understanding.

For me: I shouldn't invoke my [writing](https://github.com/sanand0/blog/blob/main/pages/skills/anand-writing-style/SKILL.md) and [speaking](https://github.com/sanand0/blog/blob/main/pages/skills/meeting-response-style/SKILL.md) skills along with other [thinking](https://github.com/sanand0/blog/tree/main/pages/skills) skills.
