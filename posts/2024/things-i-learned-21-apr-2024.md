---
title: Things I Learned - 21 Apr 2024
date: 2024-04-21T00:00:00+00:00
categories:
  - til
description: I gathered insights on GPT-4 prompting, structured LLM outputs via Outlines’ logit bias trick, and the browser's Shape Detection API. I also found that personal invitations and mandatory in-person sessions are crucial for driving engagement in online learning.
tags: [gpt-4o]
---

This week, I learned:

- [Effort engine](https://asciinema.org/a/piP22yYwcaohu5cA2gyuv1W61) introduces "effort" as a parametrizable way to speed up LLMs with a quality trade-off. Works on Mistral for now.
- Many arts demand devotion. Devoting unrestricted time is part of that. 16 hours of practice a day is not uncommon. Sessions don't start and end on time.
- Instruments take a lot longer to learn than vocal music. The instrument needs to become an extension of you.
- Tests and homework have a purpose. It helps people figure out whether they've learnt. So:
  - Write tests that make people think! Like DuckDB workshop
  - Share a list of exercises that people can explore
- People need to explicitly be INVITED, and potentially IN PERSON, before they will engage with something new.
  - For example, no one posted to <GenAINews@straive.com> until the VIA Talks session where we got them to post.
  - For example, having one day at IITM mandatory (especially early in the course) gets online students familiar with TAs. They understand that TAs actually help, at high quality. That they can use Discord.
  - What makes Delhi students more assertive? How can we inculcate that in others?
- [jsr-io/migrations](https://github.com/jsr-io/jsr/tree/main/api/migrations) is a great example of database migrations.
- [Shape Detection API](https://developer.chrome.com/docs/capabilities/shape-detection) in the browser detects QR codes, face bounding boxes,
- Browsers also _natively_ support blurring and face tracking. [via](https://w3c.github.io/mediacapture-extensions/#exposing-mediastreamtrack-source-background-blur-support)
- [Lessons after half a billion GPT tokens](https://kenkantzer.com/lessons-after-a-half-billion-gpt-tokens/) for GPT-4:
  - Vague instructions are better than over-specifying
  - Avoid libraries like Langchain. APIs are stabler
  - 1 token = 3 characters is good enough
  - GPT4 doesn't hallucinate much, except it does a poor job of saying "I don't know" or "There's no such data" (the null hypothesis)
  - Keep the output down to 10 items or so if you're listing. For longer lists, have it explicitly enumerate
  - Don't worry about niches. Just wait for GPT5
- #WRITE [GPT clearly prefers 42 as a random number](https://twitter.com/infobeautiful/status/1778059112250589561).
- #WRITE [fal.ai](https://fal.ai/) "animates" pictures, creating videos. It made one from my talk. I morphed into various somewhat similar people rapidly in a 2-second span. Very promising, and far from good.
- [llmsherpa](https://github.com/nlmatics/llmsherpa) extracts PDFs using LLMs. It has errors but it preserves hierarchy, extracts tables well, and retains image coordinates. Via +91 90031 35354 ~Vetrivel PS
- [www.web.sp.am](https://www.web.sp.am/) is a content farm that's getting [hit by OpenAI](https://twitter.com/deliprao/status/1778468161739690278). Highlights how easy it is to create content farms, and therefore "easy" it can be to introduce bias into LLMs.
- [OpenAI supports batching requests](https://platform.openai.com/docs/guides/rate-limits/batching-requests). Didn't know that.
- [Marvin](https://www.askmarvin.ai/) provides Python decorators to create AI functions. Pretty intuitive!
- [Outlines](https://outlines-dev.github.io/outlines/) generates structured test with LLMs. It uses the ⭐ [`logit_bias` trick](https://twitter.com/AAAzzam/status/1669753721574633473) to limit choices in output. See [`get_choice()`](https://github.com/outlines-dev/outlines/blob/main/outlines/models/openai.py)
- [Lemur from Assembly.ai](https://www.assemblyai.com/blog/lemur/) does real time call transcription and summary
- [W3C is exploring ways to allow web pages to train LLMs, to flag content as AI generated, etc.](https://www.w3.org/reports/ai-web-impact/)
- [Data Provenance Explorer](https://www.dataprovenance.org/) lists open datasets used to train LLMs.
- [Summarize.tech](https://www.summarize.tech/) summarizes YouTube videos.
- #WRITE [Stable Audio 2.0](https://stability.ai/news/stable-audio-2-0) generates 3 min of music from a prompt. I tried [Bollywood Tamil film background music. Dark, soulful](https://stableaudio.com/1/share/af0958b5-f4b1-4e1b-b1ef-2b6dcad91bbb) and [Horror movie background. Drums starts darkly. Build up to a crescendo of intense chaos.](https://stableaudio.com/1/share/4fc941a7-bdf2-4a45-bd16-e22a96056ee6). Great that it managed, but not great music. Somewhat stereotyped. I need to learn how to prompt better. BTW, [Udio](https://www.udio.com/) is another such.
- [Harpa.ai](https://harpa.ai/) is a well designed Chrome extension / plugin that can chat with or automate any page.
- Due to in-context learning, giving 100s of examples in the prompt can teach LLMs to jailbreak. [Ref](https://www.anthropic.com/research/many-shot-jailbreaking)
- With RAG on search becoming big, search APIs are growing. [serper.dev](https://serper.dev/), [you.com](https://documentation.you.com/), [searxng](https://docs.searxng.org/) being examples.
