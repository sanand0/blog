---
title: Things I Learned - 15 Sep 2024
date: 2024-09-15T00:00:00+00:00
categories:
  - til
description: I explored how LLMs like Pixtral and Hume transform coding workflows while potentially hindering student retention. I also looked into agent-driven automation for daily tasks and why it's best to delegate OAuth implementation to external providers.
tags: [prompt-engineering, cursor, ocr]
---

This week, I learned:

- [Hume](https://app.hume.ai/) provides a voice-to-voice model (EVI 2) that handles emotions at 7 cents/minute.
- [OpenArt workflows](https://openart.ai/workflows/home) has image generation workflows
- [Pixtral](https://huggingface.co/mistral-community/pixtral-12b-240910) seems quite [good at OCR](https://x.com/swyx/status/1833934254834942047)
- LLM coding
  - Makes you more ambitious
  - Lets you code without stress. (Just pass it the error and have it fix it. Or find another approach)
  - Is unlimited. You can run dozens of agents in parallel
- Simon Willison's crowdsourced list of [prompt engineering hacks](https://x.com/simonw/status/1832944559162269990)
- "Invest in things that don't change." Jeff Bezos. Like faster delivery, SQL, web platform.
- Medical cost in Singapore (for insurance coverage) - via Kumar
  - Root canal at clinic: $1,300
  - Crown replacement at clinic: $1,300
  - Periodontist (gums) at hospital: $2,500
- [OAuth from First Principles](https://stack-auth.com/blog/oauth-from-first-principles) is a SIMPLE explanation of OAuth. Conclusion: "You probably shouldn't implement your own OAuth client."
- [Alphaxiv](https://www.alphaxiv.org/) is Arxiv.org but with author comments and chat
- [The Impact of AI on Computer Science Education](https://cacm.acm.org/news/the-impact-of-ai-on-computer-science-education/):
  - Eric Klopfer divided his undergrad CS class into three groups and gave them a Fortran task.
  - One used ChatGPT. Another, Meta's Code Llama LLM. Third, only use Google.
  - ChatGPT group was faster than Code Llama was faster than Google
  - When tested on the approach, the ChatGPT remembered nothing. Half the Code Llama group passed. The Google group passed fully
- Server-side implementation of an OAuth2 client is too complex. Best to delegate this to Auth0
- Via Pratap Vardhan:
  - At Khan Academy, every developer working on Khanmigo has cursor. Everyone who's contributed to a Khan Academy GitHub repo has GitHub Copilot.
  - I stopped using Google + StackOverflow 2 years ago. I use ChatGPT, Copilot, etc. For humans, I ask Reddit.
  - Excited by async agents. Things that do my job while I sleep.
    - Zapier notifications.
    - Monitor what happens. Put it into a flow diagram and alert me.
    - Every month, did my broker trade? Did my bank transaction fail? Did I pay my electricity bill?
    - Every time you delegate, use an agent instead.
    - Read my RSS feeds.
    - Read my browser history and suggest interests.
  - Plan a session in Bain, BCG, etc. on Artifacts.
  - Explore sparse embeddings. More effective. ColiPali, ColBERT
