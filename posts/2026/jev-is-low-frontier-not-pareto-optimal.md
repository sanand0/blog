---
title: Jev is low-frontier not pareto optimal
date: 2026-09-18T09:25:29+05:30
categories:
    - llms
description: I evaluated Jev on 77 BANKING77 examples. It costs 7 cents per 1,000 classifications but reaches 75% accuracy, trailing DeepSeek V4.1 Flash and GPT 5.6 Luna, so it is not yet worth switching.
tags: [llms, model-comparison, llm-evaluation]
---

I heard a lot about [Jev](https://developers.cloudflare.com/ai/models/typesafe/jev/) - a new kind of model from TypeSafe. It's available on [OpenRouter](https://openrouter.ai/typesafe/jev-1.13).

It's quite low-cost: Input = 4.2c / MTok, Output = free.\
It only classifies or scores. It doesn't generate text. So that's useful for classification, fact-checking, evaluations, etc.

I [evaluated Jev](https://sanand0.github.io/llmevals/jev/) on 77 data points from [BANKING77](https://huggingface.co/datasets/PolyAI/banking77) and tested Jev against other models. Summary:

1. Yes, it's cheap (7c per 1,000 classifications), but not much cheaper than DeepSeek V4.1 Flash (8c) or GPT 5.6 Luna (12c).
2. It's not that accurate (75%) compared with DeepSeek V4.1 Flash (79%) or GPT 5.6 Luna (83%).

[![](https://files.s-anand.net/images/2026-09-18-jev-is-low-frontier-not-pareto-optimal.avif)](https://developers.cloudflare.com/ai/models/typesafe/jev/)

Yes, it's on the frontier, but mainly because of cost, not quality.

If the model rapidly evolves from here, that's a different story. But as of today, this is a category of models to keep an eye on, and not yet a reason to switch.

PS: On the other hand, GPT 5.6 Luna was slightly ahead of GPT 5.6 Sol on classification! DEFINITELY benchmark (or even blindly switch) to GPT 5.6 Luna. It's an excellent model for its price.
