---
title: Things I Learned - 13 Apr 2025
date: 2025-04-13T00:00:00+00:00
categories:
  - til
description: I explored Claude 3.7's extended thinking capabilities, learned to bypass SQLite locks for browser history, and used chroot for Linux recovery. I also discovered Nomic's multimodal embeddings and new tools for AI-driven social research and speech cloning.
keywords: [claude 3.7, sqlite, chroot, animejs, multimodal embeddings, paperbench, hailuo speech-02, deep research]
---

This week, I learned:

- It's possible to intentionally train yourself to:
  - [Form close friends](https://www.neelnanda.io/blog/43-making-friends). Care, ask, and share.
  - [Become a do-er](https://www.neelnanda.io/blog/become-a-person-who-actually-does-things). Stay mindful of the problem or opportunity you're deferring.
- [AI Coding and the Peanut, Butter & Jelly problem](https://iamcharliegraham.substack.com/p/ai-coding-and-the-peanut-butter-and): #ai-coding
  > This ability to define your desired outcome in crisp, complete terms is one of the most important superpowers of the AI era.
- The Singapore [Urban Redevelopment Authority Property Data](https://eservice.ura.gov.sg/property-market-information/pmiResidentialRentalSearch) lets you search sale and rental prices of properties in Singapore. No API though
- Notes from meeting with [Deepak Goel](https://www.linkedin.com/in/drizzlin)
  - We have linguistic boundaries in media today more than national boundaries. The Chinese language media, for example, is a very different ecosystem.
  - China culturally struggles with the exercise of branding and cultural power, unlike the west, which has adopted assertive and opinionated branding.
  - You really learn the character of a region only by traveling
  - Similarities arise from unexpected sources. For example, Japan and Ecuador have similar culutures - both are disaster prone locations.
  - AI unlocks _so many social research possibilities_ that were not possible before, e.g. by interpreting and classifying what people share in different situations.
  - Companies send clients to third party trainings (e.g. at Harvard) along with their employees - to learn clients' real pain points! Education has become a tool for customer experience. Schools are tying up with companies for this (e.g. with Emeritus)
  - [International Schools Partnership](https://internationalschoolspartnership.com/) provides services to independent schools for a small stake. It's an interesting business model.
  - Research for colleges is a business model that's at risk thanks to Deep Research (e.g. analyse sustainability practices of listed companies.)
- There's an [Indian Censor Board Scraper](https://github.com/diagram-chasing/censor-board-cuts) repo.
- Using `chroot`, you can boot from a Linux USB stick, but trick the system into working from your hard disk as the OS. Useful if your system won't boot. [Ref](https://livesys.se/posts/the-chroot-technique/)
- Claude 3.7 Sonnet with extended thinking has a token limit of over 64,000 tokens. Given a strong instruction following capability, that makes it one of the most powerful models for transforming text. For example, transcription restyling, translations, XML to json conversions, PDF to XML, etc.
- Notes from discussion with [Sundeep](https://www.linkedin.com/in/sundeeprm/)
  - In his experience, investors tend to let you run the show (e.g. ask what you want rather than push in a specific direction) unless there is trouble
  - We discussed the "running out of problems" problem with AI. His suggestion: List problems we dropped or eliminated for lack of time/capacity. This filter is a blindspot.
  - Even if you know how to do someting, use AI to discover an alternate solution approach. That's the path to 10X (rather than incremental) optimization.
  - Having AI create end-to-end pitch videos based on a product idea is now a reality. (He showed me one for his product.)
  - Areas to explore with Deep Research are:
    - What hidden trends is media misdirecting away from? What are second order effects and hidden gameplays?
    - Which organizations would be good clients to target? What would be an apt pitch pitch for them?
  - Experience dining is an emerging theme.
  - Having LLMs explain scenarios (i.e. what might happen if ...) based on parameters can help understand/quantify the impact of actions, and therefore what to do.
- One way to copy as Markdown: copy page contents, [paste in text-html.com](https://text-html.com/), copy HTML, [paste in Turndown](https://mixmark-io.github.io/turndown/), copy Markdown.
- Claude 3.7 Sonnet with extended thinking has a token limit of over 64,000 tokens. Given a strong instruction following capability, that makes it one of the most powerful models for transforming text. For example, transcription restyling, translations, XML to json conversions, PDF to XML, etc.
- [Elimination Game](https://github.com/lechmazur/elimination_game) is like Survivor for LLMs, where they form alliances and out-vote each other until 2 remain. The eliminated LLMs vote for the winner. GPT-4.5 Preview, both Claude Sonnets and Gemini 2.5 Pro consistently out-perform the rest. Their dialogues are _fascinating_!
- SQLite can open locked databases (e.g. browser history) via `sqlite3 'file:places.sqlite?mode=ro&nolock=1'`. datasette uses this. For example, to read the Edge history on Linux, use `datasette ~/.config/microsoft-edge/Default/History --nolock` [Ref](https://sqlite.org/forum/info/a2e9387b8ea1c919b2ad1ecafb417cebb15c48634c55b3abd6a9acbb2fabf797)
- Notes from [ThursdAI - Apr 03](https://sub.thursdai.news/p/thursdai-apr-3rd-openai-goes-open)
  - [Nomic Embed Multimodal](https://www.nomic.ai/blog/posts/nomic-embed-multimodal) models are the current SOTA on multi-modal embeddings. Notably, they [embed PDFs natively](https://docs.nomic.ai/atlas/embeddings-and-retrieval/guides/pdf-rag-with-colnomic-embed-multimodal).
  - [Hailuo Speech-02](https://www.minimax.io/audio) is the best speech model right now beating ElevenLabs. It has _excellent_ voice cloning. [Pricing](https://www.minimax.io/platform/document/Pricing%20Overview?key=67373ec8451eeff1a85b9e4c): $30/1M chars. 10% of ElevenLabs, 2X of OpenAI TTS
  - [PaperBench](https://openai.com/index/paperbench/) is an open testing framework from OpenAI that requires models to replicate the research work in papers. It has ~8,000 tasks evaluated by LLMs and with LLMs judging the judges as well. The [code](https://github.com/openai/preparedness/tree/main/project/paperbench) is well worth studying.
  - [Runway Gen 4](https://runwayml.com/research/introducing-runway-gen-4) was released with very high character consistency and longer durations
  - [Dreamina](https://dreamina.capcut.com/ai-tool/) creates lip-synced videos from audio + a single image. [Hedra](https://www.hedra.com/) is better for animated characters, though.
  - Meta shared but has not released [Mocha](https://congwei1230.github.io/MoCha/), an open character generation model that generates new characters speaking based on an audio you provide. It is not based on existing images but the quality is very good
  - [All Hands](https://app.all-hands.dev/) has a free online version where you can fix GitHub issues.
- This [`realistic frodo and sam mining through a minecraft tunnel, holding minecraft picaxes and torches`](https://sora.com/g/gen_01jr5kgms2fabbxf57m1x01wng) made my day 🙂
- [AnimeJS](https://animejs.com/) released version 4. It animates HTML, SVG, Canvas, and WebGL with a consistent API. Looks elegant and powerful.
