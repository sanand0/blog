---
title: Things I Learned - 08 Jun 2025
date: 2025-06-08T00:00:00+00:00
categories:
  - til
description: I documented my findings on AI coding workflows, including leveraging LLMs for specs and reviewing. I compared Claude Code and O3 performance, tested anyascii for character transliteration, and explored tools like FastMCP and automated documentation generators.
keywords: [ai-coding, claude-code, o3-model, fastmcp, anyascii, cloudflare-workers, llm-benchmarks, speech-to-text]
---

This week, I learned:

- There's a very interesting [HN discussion](https://news.ycombinator.com/item?id=44159166) on the AI coding of [CloudFlare Workers OAuth Provider](https://github.com/cloudflare/workers-oauth-provider/commits/main/). My takeaways: #ai-coding
  - Write _very_ comprehensive specs.
  - Use LLM to create the specs.
  - Reviewing is a skill we need to develop.
  - Understanding others' code takes effort.
  - But LLM code is easier to review because it's immediate and has no ego.
  - Unit tests are critical.
  - Use LLMs for well understood specs, APIs, platforms and libraries to really save time.
  - Logic-less stuff like Markdown, JSON and HTML templates are a LOT easier to verify. Do more of that.
  - We can only make so many decisions in a day. AI coding saves us that effort.
  - Experts are not experts in every area. They benefit from LLMs in other areas.
  - LLMs are great for rubber ducking. Speaking and speccing really help.
  - LLMs make mistakes. So do most humans.
  - LLM speed makes coding more exhausting.
  - Use LLMs to understand codebases.
  - AI coding _could_ reduce demand for developers. E.g. Sysadmin demand plummeted with cloud infra and infrastructure-as-code.
  - But, niche use cases could grow, like how demand for photographers grew despite point-and-shoot cameras.
  - Transaction cost of hiring even 1 person is high and that will likely be a bottleneck. Plus people can use LLMs themselves, so that will dampen niche demand.
- Google Introduced [Google Vids](https://docs.google.com/videos/) last year. It's a video creator styled like PowerPoint. Looks promising.
- [FastMCP](https://github.com/jlowin/fastmcp) looks like an easy way to build MCPs. (Yet to try it)
- O3 and to a lesser extent, Claude Sonnet 4, are the models that can accurately summarize complex subjects and create a list of links without hallucinations. [Ref](https://mikecaulfield.substack.com/p/differences-in-link-hallucination)
- [Claude Trace](https://github.com/badlogic/lemmy/tree/main/apps/claude-trace) lets you record all interactions with Claude Code.
- Elevenlabs now supports emotion and interruption. [Ref](https://x.com/venturetwins/status/1930727253815759010)
- Thinking longer alone is not enough to scale intelligence. We need better models, too. [Ref](https://x.com/MFarajtabar/status/1930707627509789054)
- Indian High Court judgements are now available as a public dataset on AWS and updated periodically. [Ref](https://registry.opendata.aws/indian-high-court-judgments/)
- A few observations in AI code editors' styles.
  - O3 is better at _finding_ bugs than Jules, which tends to try and fix them rather than discover them.
  - Codex writes more minimal edits in PRs than Jules, which is more verbose.
  - Claude Code remains the best at faithfully creating and updating front-end apps.
- Deep Research is great for fact-checking my notes! [ChatGPT](https://chatgpt.com/share/684274ef-a280-800c-8b35-21cf0353ad51)
- [Web bench](https://github.com/bytedance/web-bench) evaluates LLMs in web development. Claude Sonnet remains ahead.
- Vision language models heavily rely on past training and miss changes they don't expect. [Ref](https://github.com/anvo25/vlms-are-biased)
- Pure CSS tooltips are possible. [Julia Evans](https://jvns.ca/til/in-css-you-can-populate--content---with-a--data---attribute/)
- Google has an [OAuth Playground](https://developers.google.com/oauthplayground/) which is a convenient way to get a temporary OAuth token.
- At the moment, the best speech to text for Android appears to be ChatGPT's transcription. The default Android text to speech (which I thought was good) no longer feels adequate. Gemini mis-hears and doesn't wait till I'm done. Whisper ASR has poor noise cancellation and a 30 second limit.
- [anyascii](https://github.com/anyascii/anyascii) is a better alternative to [unidecode](https://pypi.org/project/Unidecode/). It supports more characters and also supports transliteration. I use it to strip out non-ASCII in ChatGPT's output. [Commit](https://github.com/sanand0/scripts/commit/5ea8493)
- [DeepWiki](https://deepwiki.com/) creates docs for humans GitHub repos. [Example](https://deepwiki.com/sanand0/aipipe/). It's verbose, human-facing, and does not understand the nuances of context and implications. [Context7](https://context7.com/) creates llms.txt for LLMs. [Example](https://context7.com/sanand0/aipipe). It's concise, example-oriented, and works only if there are code snippets relevant (e.g. API calls) that can be generated from the codebase. Like creating an llms.txt automatically, e.g. <https://context7.com/textualize/textual/llms.txt> #ai-coding
- We will move towards an organization structure where developers are embedded with business teams rather than working as a separate group. Sort of like embedded executive assistance instead of a central typing pool. [Making AI Work](https://www.oneusefulthing.org/p/making-ai-work-leadership-lab-and)
