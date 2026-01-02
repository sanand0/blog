---
title: Transcribe call recording
date: "2025-09-10T07:05:28Z"
lastmod: "2025-12-14T12:55:14Z"
classes: wrap-code
---

Transcribe call recordings guessing speaker names using the latest Gemini Pro model on [Google AI Studio](https://aistudio.google.com/prompts/new_chat).

```markdown
Transcribe this call recording with Anand (LLM expert, Straive/Gramener).
DO NOT MISS ANY PART OF THE CONVERSATION.
Drop verbal tics and fillers (um, uh, etc).
Correct spelling and grammar but otherwise don't modify the original words.
Add English translations to any non-English parts.
Mark inaudible or unclear segments as "[UNCLEAR]".
Break it into logical paragraphs. No timestamps.
Begin each paragraph with a **Speaker**: ...., e.g. **Anand**: ...
Guess speaker names. If unsure, use **Unsure**: ...
**Make key points / takeaways / memorable statements bold**.
**I repeat: Transcribe EVERY part of the conversation. Don't miss any turns.**

<!-- #TODO List all speakers, and who spoke when, for context -->
```
