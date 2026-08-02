---
title: Simple writing hurts thinking
date: 2026-08-01T14:00:27+08:00
categories:
  - llms
---

![](https://files.s-anand.net/images/2026-08-01-simple-writing-hurts-thinking.avif)

As agents get smarter, and when we asking questions outside our expertise, it's pretty hard to understand what they're saying.

Andrew Carr [uses](https://x.com/andrew_n_carr/status/2081534245370314816) "only report to me in ASD-STE100 Simplified Technical English" to simplify their writing.
Ben Sehl [suggested](https://x.com/benjaminsehl/status/2082158002958741746) making this a permanent instruction.

But, does simplifying the writing worsen their thinking?

<!-- https://chatgpt.com/c/6a6d770d-9d68-83ec-b544-84a7aa1ecdc6 + https://claude.ai/chat/7788dcc8-dd41-4605-843b-7c418d675b8a -->

I tested six tasks on ChatGPT (GPT 5.6 Sol):

1. [Model benchmarking](https://github.com/sanand0/research/blob/main/simplification-prompt/question/1.md)
2. [Causal diagnosis](https://github.com/sanand0/research/blob/main/simplification-prompt/question/1.md)
3. [Decision under uncertainty](https://github.com/sanand0/research/blob/main/simplification-prompt/question/1.md)
4. [Experimental design](https://github.com/sanand0/research/blob/main/simplification-prompt/question/1.md)
5. [Evidence and judgment](https://github.com/sanand0/research/blob/main/simplification-prompt/question/1.md)
6. [Adversarial system design](https://github.com/sanand0/research/blob/main/simplification-prompt/question/1.md)

... with and without this suffix: "Answer in ASD-STE100".

The results, without (-) and with (+) the suffix, are below, including the source count and thinking time.

- [Task 1 - prompt](https://github.com/sanand0/research/blob/main/simplification-prompt/result/1a.md): 66 sources, 1m 31s
- [Task 1 + prompt](https://github.com/sanand0/research/blob/main/simplification-prompt/result/1b.md): 44 sources, 41s
- [Task 2 - prompt](https://github.com/sanand0/research/blob/main/simplification-prompt/result/2a.md)
- [Task 2 + prompt](https://github.com/sanand0/research/blob/main/simplification-prompt/result/2b.md)
- [Task 3 - prompt](https://github.com/sanand0/research/blob/main/simplification-prompt/result/3a.md)
- [Task 3 + prompt](https://github.com/sanand0/research/blob/main/simplification-prompt/result/3b.md)
- [Task 4 - prompt](https://github.com/sanand0/research/blob/main/simplification-prompt/result/4a.md)
- [Task 4 + prompt](https://github.com/sanand0/research/blob/main/simplification-prompt/result/4b.md)
- [Task 5 - prompt](https://github.com/sanand0/research/blob/main/simplification-prompt/result/5a.md): 123 sources, 2m 4s
- [Task 5 + prompt](https://github.com/sanand0/research/blob/main/simplification-prompt/result/5b.md): 84 sources, 5m 4s
- [Task 6 - prompt](https://github.com/sanand0/research/blob/main/simplification-prompt/result/6a.md): 97 sources, 2m 20s
- [Task 6 + prompt](https://github.com/sanand0/research/blob/main/simplification-prompt/result/6b.md): 26 sources, 3m 44s, wrote code

Interestingly, the simple writing prompt reduced the number of sources. (Thinking time varies.)

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

🟢 = Simple prompt won. 🟡 = Tie. 🔴 = Without simple prompt won.

(Each pair was compared twice, in both orders (A, B) and (B, A) - to reduce position bias.)

There's no doubt that asking ChatGPT to "Answer in ASD-STE100" reduces its thinking quality. (It might be worth re-testing this in a few months.)

So, what should we do for now? I can see three options:

1. Don't simplify the writing initially. AFTER it thinks, ask for a simple explanation.
2. If you want to continue the conversation, don't continue after the simple explanation. Edit it, or branch the chat.
3. Avoid understanding altogether. See if you can delegate the next step directly to the agent.
