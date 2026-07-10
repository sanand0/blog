---
title: Transcribe call recording
date: "2025-09-10T07:05:28Z"
lastmod: "2025-12-14T12:55:14Z"
classes: wrap-code
description: I transcribe call recordings using Gemini Pro on Google AI Studio with a prompt that guesses speaker names, includes timestamps, translates non-English speech, and bolds key takeaways while cleaning up verbal tics.
tags: [google-ai-studio, transcription, prompt-engineering, audio-analysis]
---

Transcribe call recordings guessing speaker names using the latest Gemini Pro model on [Google AI Studio](https://aistudio.google.com/prompts/new_chat).
Append all speakers, and who spoke when, for context.

```markdown
Transcribe this call recording with Anand (LLM expert, Straive/Gramener).
DO NOT MISS ANY PART OF THE CONVERSATION.
Drop verbal tics and fillers (um, uh, etc).
Correct spelling and grammar but otherwise don't modify the original words.
Add English translations to any non-English parts.
Mark inaudible or unclear segments as "[inaudible]". Mark uncertain words with like "[word?]" or ambiguous possibilities like "[word1? word2?]".
Break it into LOGICAL paragraphs, each paragraph with a **Speaker**: [Timestamp] content ...., e.g. **Anand**: [00:13] When did ...
Guess speaker names. If unsure, use **Unsure**: ...
**Make key points / takeaways / memorable statements bold**.
**I repeat: Transcribe EVERY part of the conversation. Don't miss any turns.**
```
