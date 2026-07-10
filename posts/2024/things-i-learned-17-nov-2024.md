---
title: Things I Learned - 17 Nov 2024
date: 2024-11-17T00:00:00+00:00
categories:
  - til
description: I discovered Anthropic’s condensed documentation, Gemini’s OpenAI-compatible API, and Alphafold 3's open-sourcing. I also learned about LLM attention sinks, compared Whisper and Gemini for transcription, and explored using Prefect as a lightweight alternative to Airflow.
tags: [anthropic, gemini-api, cloudflare-r2, whisper, claude]
---

This week, I learned:

- Anthropic has single-plage docs for LLMs. [Condensed version](https://docs.anthropic.com/llms.txt) and [Full version](https://docs.anthropic.com/llms-full.txt)
- [Malcolm Gladwell on the importance of self-correction](https://www.ted.com/pages/malcolm-gladwell-on-the-importance-of-self-correction-transcript)
  - Belonging to multiple social worlds is a good way to defend against no longer being good at what you used to be. Diverse values and social groups help.
  - Self handicapping explains a lot about the world. You study late for a maths test - so you can fail for lack of trying, not aptitude. Ecosystems (e.g. sports teams) mitigate self-handicapping.
  - You don't have to be good in athletics to get the benefits. A slow runner gets the same discipline, pumping up, etc that a fast runner does
  - Mono cultures are good to accomplish a known mission. Diversity is good to pivot during uncertainty. So, localize mono cultures
  - Diversity helps only if there are sufficient numbers, or if they have enough power to change the organization's thinking.
- Use a standardized password strategy, e.g. use the month like GramNov2024 (via Namit)
- Gemini has an OpenAI compatible API. [Gemini Docs](https://ai.google.dev/gemini-api/docs/openai)
- Ethan Mollick says Claude is solving MBA case studies well. [x.com](https://x.com/emollick/status/1856161026238025835)
- LLMs pay a lot of attention to the first 6 tokens. [Ref](https://huggingface.co/blog/tomaarsen/attention-sinks)
- This is an interesting article on "UI in the age of Gen AI". [Ref](https://agao.substack.com/p/uiux-in-the-age-of-generative-ai)
- Google Open sourced Alphafold 3. [Repo](https://github.com/google-deepmind/alphafold3)
- Cloudflare R2 has the same API as S3 but is cheaper
- Prefect.io is a good alternative to Airflow / cron. Can use for synchronisation tasks, e.g. Drive to server. But no Auth, UI params or config.
- Gemini transcription does not give accurate timestamps. Whisper does. But the quality of transcription is similar.
- Pass a complex data structure to Claude.ai and have it create an app to visualize it. It does well. [Simin Willison](https://x.com/simonw/status/1855819673482461216)
- [Tech Council Ventures](https://techcouncilventures.com/) and [Sunicon VC](https://sunicon.vc/) invest in early stage startups, and aloso provide them technology support (via Naveen)
