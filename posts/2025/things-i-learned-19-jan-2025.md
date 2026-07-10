---
title: Things I Learned - 19 Jan 2025
date: 2025-01-19T00:00:00+00:00
categories:
  - til
description: I explored audio diaries, switched from Brave to Edge for superior text-to-speech, and tested Gemini for manuscript formatting. I also discovered ModernBert for embeddings and Kokoro-TTS, a lightweight model topping the TTS Arena leaderboards.
tags: [embeddings, text-to-speech]
---

This week, I learned:

- Audio diaries are a thing. Monash University asks students to voice their learnings, share it with each other and have them give feedback. I wonder if ChatGPT diaries could become a thing, too, and LLM journalling starts helping with therapy.
- Regulation shows things down at colleges and hospitals. For example, patient consent is required for surgeons to learn from their own surgery videos. Unregulated sectors are far more likely to innovate.
- Doctors can only do so much. Air quality, where you live, etc can do more for the patient than medicines or the doctor. If doctors keep this in mind, they can be more effective.
  - Extending that thought, _ANYONE_ who leverages assets through holistic thinking, becomes _FAR_ more effective.
- "The curriculum tells teachers what to teach. The exams tell students what to learn." - Ronald Harden
- "Stravaig" is a Scottish word. It means mindless wanderings.
- "The real voyage of discovery consists of not a new voyage but having new eyes" - Proust
- Possibility Thinking is "the willingness to see possibilities everywhere instead of limitations". It's an approach / mindset that can make things that seem hard possible. With LLMs, this is becoming increasingly realistic to me in many areas.
- What will LLMs enable that do not or cannot exist today? Rather than optimizing what exists? Something to think about.
- ModernBert supports embeddings and is better than text-embedding-3-small on [MTEB](https://huggingface.co/spaces/mteb/leaderboard).
- [How to export browser history from Brave to Edge](https://community.brave.com/t/how-to-export-braves-browsing-history-to-another-browser/114687)
  - Go to `AppData Local > BraveSoftware > Brave-Browser > User Data > Default`
  - Copy `History` and `History-journal` into `AppData Local > Google > Chrome > User Data > Default`
  - On Edge, go to `edge://settings/profiles/importBrowsingData` and `Import data from Google Chrome` and import the history.
- I switched back from Brave to Edge, mainly because Edge's native text-to-speech and speech recognition is far better. I can use it better on my mobile.
- A colleague, Karthick, asked different models to apply the editing and formatting guidelines for a journal to a manuscript. (E.g. Abbreviate chapter & section numbers, except when a sentence begins with it. Use "1" instead of "one", etc. except when a sentence begins with it. Things like this.) Gemini Exp 1206 seems to be the most reliable, compared with most other models.
- [GitHub CodeSpaces](https://github.com/features/codespaces) seems to be coming up more often in my radar, but I'm yet to figure out a use for it.
- [TTS Arena](https://huggingface.co/spaces/Pendrokar/TTS-Spaces-Arena) is a benchmark of text-to-speech models. [Kokoro-TTS](https://huggingface.co/spaces/hexgrad/Kokoro-TTS) is the current leader. It's just 82M, runs on Google Colab, and sounds slightly better than OpenAI TTS.
- [chat.qwenlm.ai](https://chat.qwenlm.ai/) consolidates all of Qwen's models in one ChatGPT-like interface.
