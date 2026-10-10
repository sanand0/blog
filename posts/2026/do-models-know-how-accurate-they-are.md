---
title: Do models know how accurate they are?
date: 2026-10-10T12:01:31+08:00
categories:
- llms
description: I tested models on about 770 banking classification tasks and found their confidence scores were overconfident but useful for ranking errors. Better prompts improved calibration, while logprobs cut human review further.
tags: [llm-evaluation, prompt-engineering, probability]
---

A colleague was using an agent to classify paragraphs as titles, sections, figure captions, etc. He also asked it "How confident are you of your answer?". Interestingly, the confidence was consistently high, typically ~95%. That got me curious. (Actually, no that didn't get me curious - I saw [Germayne](https://www.linkedin.com/in/germayneng/) and [Joshua](https://www.linkedin.com/in/joshua-choo-0940b912a/) from Gojek doing this in a fantastic [session at Lorong AI](https://luma.com/1u8b2cml?tk=IRlVtR), but this is _my_ story and I'll tell it _my_ way.):

> How well does AI know its own abilities? Does it really assess confidence well?

If we can get good confidence scores, it's a _big_ deal. We can pull out the bad responses and just review those.

Reminds me of a story I was told during my MBA days. An American manufacturer asked a Japanese firm for a million nails with a 5 parts per million defect rate. The Japanese sent back a million nails and five defective nails separately, asking them why they wanted the defective nails. That ability to segregate poor quality is a _huge_ differentiator.

Anyway, I tested about 770 [standard banking classification tasks](https://huggingface.co/datasets/PolyAI/banking77) like:

- “Are virtual cards available to get?” (Correct answer: `getting_virtual_card`)
- "My transfer is pending." (ANS: `balance_not_updated_after_bank_transfer`, not `pending_transfer`)
- "Someone stole my cards!" (ANS: `lost_or_stolen_phone`, not `lost_or_stolen_card`, interestingly.)

When GPT 4.1 Nano says it's 95% confident, it's typically ~77% correct.
When it says it's 85% confident, it's ~50% correct.

When GPT 5.6 Luna says it's 95% confident, it's typically ~66% correct.
When it says it's 85% confident, it's ~60% correct.

In other words, each model has its own confidence curve. Here's the curve for GPT 5.6 Luna:

[![](https://files.s-anand.net/images/2026-10-10-gpt-5.6-luna-confidence-curve.webp)](https://sanand0.github.io/llmevals/confidence-calibration/)

The diagonal line is perfect calibration - the model is correct as often as it says it is.

GPT 5.6 Luna, like many models, seems _overconfident_ - and lies on the bottom right.

But this is useful! We can use this in two ways:

**First, we can back-calculate the likely accuracy**. Since we have the curve, we know that _for this task_, when it says 50-69% accurate, it typically is only 25% accurate.

**Second, we can just review the lease accurate**. Though the numbers may be wrong, when it says it's less confident, it tends to be less accurate. So we can just review the low-confidence answers - without worrying about the numbers.

### Prompts improve confidence accuracy

It turns out we can improve the quality of confidence scores with better prompts. I tried four ways: (Actually, ChatGPT tried multiple ways, but _my_ story...)

| Prompt                                                                                       | Error gap |
| -------------------------------------------------------------------------------------------- | --------: |
| Default prompt                                                                               |     10.3% |
| "It's OK to be uncrtain. Don't say high confidence just because you must choose a label..."  |      4.3% |
| "What's the next best alternative? If that's a close alnternative, lower your confidence..." |      3.7% |
| "What are the 2 best alternatives? Distribute your confidence between them + 'others'."      |      3.9% |

[![](https://files.s-anand.net/images/2026-10-10-prompts-confidence-curve.webp)](https://sanand0.github.io/llmevals/confidence-calibration/)

In each of these cases, the model was closer to reality.

- **Lesson #1**: Prompts can improve the accuracy of confidence scores. You can take this to managers and clients with a bit more "confidence".
- **Lesson #2**: You can use ChatGPT or some agent to automatically generate and test out prompts - to see what works best.

### Logprobs rank confidence even better

Many models return the probability of their next token (roughly "word" in LLM language) right.

For example, if you ask GPT 3.5 "In what episode of Friends did Joey eat too many marshmallows?" it thinks a bit.

- Should I say "Jo"... and continue in that direction? 70% probability
- Or should I say "In"... and continue? 28%
- Or "The"...? 1.7%
- ... and so on.

Then it picks one. Then it considers again.

For examply, after saying "Joey eating too many marshmallows is featured in Season ", it considers the following tokens:

| Token | Probability |
| ----- | ----------: |
| 3     |         77% |
| 7     |        7.7% |
| 5     |        4.5% |
| 2     |        2.9% |
| 4     |        2.8% |

It's fairly sure about Season 3, but if in doubt, it might consider some of the adjacent seasons.

[![](https://files.s-anand.net/images/2026-10-10-joey-marshmallows-friends-logprobs.webp)](https://sanand0.github.io/llmviz/)

You can calculate the probability across the _entire_ answer (86% in this case.).

That turns out to be a pretty good predictor of accuracy. It's not a number you can quote - 86% doesn't mean 86% accurate. But, if you review the lowest probabilities, you find the worst answers - which is exactly what you want.

[![](https://files.s-anand.net/images/2026-10-10-prompts-vs-logprobs-confidence.webp)](https://sanand0.github.io/llmevals/confidence-calibration/#logprobs)

For example, if you need 95% accuracy (i.e. 5% error budget), you can reduce:

- 43% of your human review by asking a model for its confidence
- 65% of your human review by using the logprobs instead

### So, what do we do?

1. Ask models how confident they are. They're usually more confident when they're right.
2. Ask an agent to try different prompts and see which prompts give the most accurate confidence scores.
3. Review the answers agents are least confident about.
4. If your model gives you token probabilities (logprobs), review the lowest probabilities - that's even better.
