---
title: My Top 5 Prompts in August 2026
date: 2026-08-28T14:52:34+08:00
categories:
  - llms
description: 'I share my five most-used prompts in August 2026: meeting transcript context, email replies, comparing models, comic summaries, and reframing questions. Meeting transcripts led with 55 uses, followed by email replies with 47.'
tags: [prompt-engineering, llms, productivity]
---

I save [prompts](https://www.s-anand.net/blog/prompts/) and [prompt fragments](https://www.s-anand.net/blog/prompts/fragments/) I regularly use with ChatGPT, Claude, etc.

(Prompt fragments are just prompts used _along_ with other prompts. They're typically smaller. But the difference isn't important or anything... I just use two methods.)

I use a [script](https://github.com/sanand0/scripts/blob/940965490ce241ea3e4f7d4b5ea0adba8b209ce0/prompt) triggered by [`Ctrl Alt P`](https://github.com/sanand0/scripts/blob/940965490ce241ea3e4f7d4b5ea0adba8b209ce0/setup/media-keys.dconf#L51) to select the prompt to paste.

![](https://files.s-anand.net/images/2026-08-28-rofi-prompts.webp)

This month, the five prompts / fragments I used the most were:

**#5: [Reframe question](https://github.com/sanand0/blog/blob/fcb3518157648243f2c042d0ad0ac8148a2a3fd3/pages/skills/reframe-question/SKILL.md) skill.**

Sometimes, I'm not sure I'm asking the right question.
Actually, I'm not even sure _what_ I'm asking.

"Reframe question" roughly says, "Guess what I _really_ need, say it, then answer." The "say it" part is very helpful - I find out what I really meant to ask (or correct it.)

This is actually a skill, but since ChatGPT Plus does not yet automatically load skills in the "Chat" mode, I need to paste this manually.

**#4: [Compare models](https://github.com/sanand0/blog/blob/fcb3518157648243f2c042d0ad0ac8148a2a3fd3/pages/prompts/fragments.md#compare-models)**

I ask the same question to ChatGPT and Claude (and sometimes Gemini) and ask for a second opinion. That way, I get the best of both models, more thinking, and a sense of which models are good for what. As of now, I prefer:

- ChatGPT: For analytics, rigor, algorithms
- Claude: For strategy, soulful writing, creativity, front-end code
- Gemini: For learning, readable writing, foreign language, people search

**#3: [Comic strip](https://github.com/sanand0/blog/blob/fcb3518157648243f2c042d0ad0ac8148a2a3fd3/pages/prompts/fragments.md#comic-strip) + [Comic page](https://github.com/sanand0/blog/blob/fcb3518157648243f2c042d0ad0ac8148a2a3fd3/pages/prompts/fragments.md#comic-page)**

I paste my [blog posts](https://www.s-anand.net/blog/), [talk transcripts](https://talks.s-anand.net/), etc. and ask it for a single panel or full page summary. The [panels](https://files.s-anand.net/images/2026-08-21-local-agents-are-good-but-slow.avif) are usually funny. The [pages](https://talks.s-anand.net/2026-08-07-data-hack-summit/comic-page.avif) aren't too informative but they're usually engaging.

**#2: [Email Reply](https://github.com/sanand0/blog/blob/fcb3518157648243f2c042d0ad0ac8148a2a3fd3/pages/prompts/email-reply.md)**

[Most of my email replies are based on this prompt](https://www.s-anand.net/blog/ask-ai-anything-email/). For over 80% of my emails, I just send its response as-is, and for about 15%, I send it with minor tweaks.

(To be fair, I wouldn't have bothered replying to many emails earier, so the percentage I need to correct seems smaller than it really is.)

**#1: [Meeting transcript context](https://github.com/sanand0/blog/blob/fcb3518157648243f2c042d0ad0ac8148a2a3fd3/pages/prompts/fragments.md#meeting-transcript-context)**

This is my top prompt. It creates a prompt to transcribe meeting recordings.

Now, that's a weird thing to do, but here's the situation.

1. Google Meet (and Teams) have poor transcripts. Whisper, Gemini, and most other models are _much_ better. [Here's how I use Gemini](https://github.com/sanand0/scripts/blob/940965490ce241ea3e4f7d4b5ea0adba8b209ce0/call).
2. But Gemini (like other multimodal models) doesn't label speakers well - it doesn't know who said what and gets names wrong sometimes.
3. Giving Gemini a hint about who said what works _quite_ well. After some testing, I hit upon this prompt, which says, "Give examples of who said what so that a good model can label speakers."

I run this after almost every meeting, so understandably, I use this a lot.

Here's the usage count in August:

| Count | Prompt                                                                                                                                                                                                                                                                    |
| ----: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|    55 | [Meeting transcript context](https://github.com/sanand0/blog/blob/fcb3518157648243f2c042d0ad0ac8148a2a3fd3/pages/prompts/fragments.md#meeting-transcript-context)                                                                                                         |
|    47 | [Email Reply](https://github.com/sanand0/blog/blob/fcb3518157648243f2c042d0ad0ac8148a2a3fd3/pages/prompts/email-reply.md)                                                                                                                                                 |
|    19 | [Comic strip](https://github.com/sanand0/blog/blob/fcb3518157648243f2c042d0ad0ac8148a2a3fd3/pages/prompts/fragments.md#comic-strip) + [Comic page](https://github.com/sanand0/blog/blob/fcb3518157648243f2c042d0ad0ac8148a2a3fd3/pages/prompts/fragments.md#comic-page) |
|    16 | [Compare models](https://github.com/sanand0/blog/blob/fcb3518157648243f2c042d0ad0ac8148a2a3fd3/pages/prompts/fragments.md#compare-models)                                                                                                                                 |
|    11 | [Reframe question](https://github.com/sanand0/blog/blob/fcb3518157648243f2c042d0ad0ac8148a2a3fd3/pages/skills/reframe-question/SKILL.md)                                                                                                                                  |
