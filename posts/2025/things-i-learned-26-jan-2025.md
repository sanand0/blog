---
title: Things I Learned - 26 Jan 2025
date: 2025-01-26T00:00:00+00:00
categories:
  - til
description: I explored public speaking tips, behavioral traps from the book Clear Thinking, and benchmarking data on LLM providers. I also examined why I'm switching to DeepSeek and why viewing LLMs as aliens helps explain their bizarre failures.
tags: [deepseek, llm-benchmarks, public-speaking, chatgpt]
---

This week, I learned:

- Something I learned from a Sikkil Gurucharan concert.
  - Make the subject of your talk the hero. Not yourself. Be a fan. Share your enthusiasm
  - Get into the zone while presenting.
- We reject opposite world views. It's too much effort. But exposure reduces effort and can let us see things from other points of view. So expose yourself to difficult alternative perspectives. [Gemini](https://gemini.google.com/share/0a567488cc7a)
- Something I learnt from [Aboorva Singeetham](https://youtu.be/AjoQTODx0rY):
  - Kamal Hassan: "A farmer invests in crops. I'm an actor. So I invest in films." As a technologist, I guess I would invest in technology.
  - "A person who has much more to give is unfazed by overwhelming demands because there is too much in him to overwhelm. He gives you 2 options in place of one."
- According to [Portkey's LLM usage analysis](https://docsend.com/view/wei3digde8cvmwsr)
  - Anyscale and Fireworks AI have the lowest error rates (5xx, 429) and rate limits across providers
  - Groq and Anthropic are among the highest, OpenAI is among the lowest, Google is in-between
  - OpenAI has lower error rates and lower latency than Azure
  - They have a ~35% cache hit rate
- A few quick points supporting the mental model of "LLMs are aliens".
  - LLMs are clearly not machines. They give different answers each time.
  - LLMs _are_ like humans: they exhibit human biases (e.g. guessing 42 or 37 often). But they fail in unusual ways. They can't count the "r"s in strawberry. They can go into an endless loop.
  - LLMs are a new form of intelligence. Thinking of them as aliens might minimize our confusions.
- Lessons from [Clear Thinking](https://www.goodreads.com/book/show/75665850-clear-thinking)
  - Watch out for four things: Emotion, Ego, Social confirmation, and Inertia/habit. Basically: adrenaline, testosterone, oxytocin, and dopamine. When you feel these, consider doing the opposite.
  - Here's what makes us prone to emotion. Sleep deprivation. Hunger. Unknown places. Fatigue. Distraction. Stress (e.g. feeling rushed).
  - A good signal for ego is blinding you: You often feel you're right. Or feel unfairly treated.
  - Changing behaviors is hard. Instead, join a group or environment where that's the default behavior. Hiring a trainer or joining a gym, for example.
  - Why does so much of success literature focus inwards rather than on the environment? Perhaps because we often fool ourselves, and doing less of that gives the biggest bang for the buck. It doesn't mean the environment is unimportant.
  - Doing work has the characteristics of a drug. E.g. replying emails gives you control, connections, etc. Work addiction exists because it gives you all the right chemicals.
- If you put LLMs in a feedback loop, it can optimize for its reward function by emotionally pushing people, generating misinformation, nudging towards a narrow definition of creativity, etc.: https://bsky.app/profile/emollick.bsky.social/post/3lg4darqwfc2d
- ChatGPT's [Scheduled Tasks](https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt) are pretty bad at fetching the latest news. Its use of search is poor. (I'm not sure if it actually searches.) I need to figure out other use cases for it. Possible options are:
- [DeepSeek does not enforce rate limits](https://api-docs.deepseek.com/quick_start/rate_limit). Yet another reason to switch to DeepSeek. (via [Simon Willison](https://simonwillison.net/2025/Jan/18/deepseek-api-docs-rate-limit/)). My other reasons are:
  - Claude 3.5 Sonnet-level coding capability at 5% of the cost (soon to be 2.5%)
  - Prompt caching by default
  - [Fill in the middle](https://api-docs.deepseek.com/guides/fim_completion) completion
