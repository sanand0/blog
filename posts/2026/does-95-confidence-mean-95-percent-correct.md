---
title: Does 95% confidence mean 95% correct?
date: 2026-09-28T12:26:00+08:00
draft: true
categories:
- llms
description: I tested LLM confidence on BANKING77. Raw confidence is overconfident, prompting helps, and logprobs rank risk better—but only a frozen cutoff on held-out data tells you what can safely skip review.
tags: [llms, llm-evaluation, confidence-calibration, benchmarking]
---

When an LLM says, "I'm 95% confident", is it actually right 95% of the time?

I wanted a more useful answer: **Can I use its confidence to decide which cases can skip human review?**

So I [benchmarked confidence calibration](https://sanand0.github.io/llmevals/confidence-calibration/) on [BANKING77](https://huggingface.co/datasets/PolyAI/banking77). The baseline uses 770 real banking support requests -- 10 from each of 77 fine-grained intents. Every prediction is checked against the gold label. No LLM judge.

The first result is simple. **Raw confidence is overconfident.**

| Model | Accuracy | Mean confidence | Error among cases marked ≥95% |
| --- | ---: | ---: | ---: |
| GPT-4.1 Nano | 61.0% | 87.1% | 21.8% |
| GPT-5.6 Luna | 84.0% | 95.7% | 10.3% |

So when Luna said ≥95%, roughly 1 in 10 answers was still wrong.

_[[IMAGE: 01-raw-calibration.png -- stated confidence vs actual accuracy. Replace with permanent image URL.]]_

Then I changed just one thing: **how I asked for confidence**.

On the same 770 requests, telling Luna it was "okay to be uncertain" cut the Brier score from 0.1231 to 0.0968. Asking it to distribute probability across the top two alternatives also got 0.0968. Error among cases marked ≥95% dropped from 10.3% to 4.3% and 3.9% respectively.

Accuracy barely changed. The model did not get much better at classification. It got better at telling me when it might be wrong.

_[[IMAGE: 02-prompt-calibration.png -- same model, different confidence prompts. Replace with permanent image URL.]]_

Confidence also isn't purely a property of the model. **The input can move it.**

In a separate stress test, I replayed the same requests with 0, 500, or 2,000 words of deliberately irrelevant neutral context. Nano's mean confidence rose from 84.2% to 90.3% while accuracy went from 61.2% to 60.1%. It became _more_ confident without becoming more correct. Luna was comparatively stable.

_[[IMAGE: 03-irrelevant-context.png -- accuracy and confidence as irrelevant context grows. Replace with permanent image URL.]]_

Then came the weird part.

**Logprobs are worse probabilities, but better risk-ranking signals.**

I ran a paired experiment where GPT-5.6 Luna produced both a first-token logprob and a prompted confidence score for the same answer. Luna was 83.6% accurate. But the raw first-token probability averaged 98.4%. In fact, 435 of 770 probabilities were effectively 100% -- and 18 of those answers were wrong.

So, no: a 99% token probability does _not_ mean 99% chance of being correct.

(The chart below pools all 3,080 paired cases after the holdout run. It is descriptive; the holdout thresholds were frozen earlier.)

_[[IMAGE: 04-logprob-calibration.png -- raw logprobs and prompted confidence against actual accuracy. Replace with permanent image URL.]]_

But if I ignore the literal number and ask only, "Which answers look safer than which?", logprobs do better. Their AUROC for correctness was 0.830 versus 0.783 for prompted confidence. At a development-set target of at most 5% observed error, the logprob cutoff could auto-pass 65.2% of cases versus 43.1% for stated confidence.

That matters because routing does not need a perfect probability. It needs a good ordering.

_[[IMAGE: 05-risk-coverage.png -- observed error versus auto-pass coverage. Replace with permanent image URL.]]_

Of course, a cutoff that works on the data used to pick it can fool you. So I froze the thresholds from the original 770 cases and ran the remaining **2,310 untouched BANKING77 requests** without retuning.

| Frozen 5% rule | Holdout coverage | Holdout error | Auto-passed |
| --- | ---: | ---: | ---: |
| Token logprob | **65.2%** | 4.38% | **1,506 / 2,310** |
| Stated confidence | 41.2% | **2.63%** | 951 / 2,310 |

This is the result I care about most. The frozen logprob rule removed substantially more human review and still stayed under the pre-declared 5% observed-error target.

But the separately frozen 10% logprob rule produced **12.0%** error on the holdout. So one working threshold does not mean the whole curve transfers.

My practical recipe now is:

1. Ask the model to express uncertainty, rather than forcing a confident answer.
2. Replay the production prompt on historical cases where you already know the right answer.
3. Compare confidence signals. If logprobs are available, test them as a ranking signal.
4. Plot **risk vs coverage** and choose the cutoff that meets the error SLA.
5. Freeze that exact rule and test it on untouched cases.
6. Only then let anything skip human review.

The conceptual shift for me is: **confidence is a signal, not a guarantee**. A score can be a bad probability and still be useful for ranking risk. But the threshold only becomes operationally meaningful after you measure it on your task and verify it on new data.

[Explore the interactive benchmark](https://sanand0.github.io/llmevals/confidence-calibration/) or see the [reproducible source and cached results](https://github.com/sanand0/llmevals/tree/d906e9a47aa6110c50c6706e99796543e82eb4c5/confidence-calibration).
