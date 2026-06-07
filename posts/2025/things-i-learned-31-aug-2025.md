---
title: Things I Learned - 31 Aug 2025
date: 2025-08-31T00:00:00+00:00
categories:
  - til
description: I automated habit-stacking with shell scripts, analyzed my meeting communication patterns, and explored AI coding via Claude Code. I also tested Cloudflare’s AutoRAG, the OKLCH color model, and used rclone for Google Drive transcript exports.
keywords: [habit stacking, arthashastra, mixture of agents, cloudflare autorag, oklch, rclone, claude code]
---

This week, I learned:

- ⭐ **Habit tooling** can expand habit-building capacity. I already use tools to support my habits. [Habit stacking](https://jamesclear.com/habit-stacking) "sticks" new habits to old ones. By sticking new habits into existing tools, I can automate this. (For example, I extended my meeting `record` fish script with an `echo` reminding me to write the meeting goal, my role, practice kind candor, and measure effectiveness.)
- ⭐ The crux of Arthashastra's advice on defeating an enemy is removing support:
  - मित्राणि भेदयेत्, मित्रं च शत्रोः। Dis-unite friends, enemies from their allies.
  - अमात्यान् द्रव्यैः, जनपदं भेदयेत्। Bribe their ministers, sow discord among subjects.
  - बलं चोच्छिनत्ति, कोशं चोपशोषयेत्। Break the army, exhaust the treasury.
  - ततोऽन्योन्यवैरिणं कुर्यात्। Then set them against each other as mutual foes.
- Consensus is dangerous in venture capital. "Because if everyone inside the firm sees the same thing, it probably means the market already does too. And when the market sees it, the upside is limited." [Guillermo Flor](https://www.linkedin.com/posts/guillermoflor_consensus-is-dangerous-in-venture-capital-ugcPost-7365751724503875584--eZN)
- This [CodeMonkeys paper](https://arxiv.org/abs/2501.14723) suggests running a [mixture of agents](https://docs.together.ai/docs/mixture-of-agents) in parallel for multiple code + test tasks and auto-pick the best by running and LLM-rewriting tests. #ai-coding
- We think a new pricing model _might_ emerge for outsourced knowledge work that leads to lower client cost & quality at higher margins. [ChatGPT](https://chatgpt.com/c/68b2f9ea-2e68-832e-8aa1-1e0fed5fb0c3)
  - LLMs do the task; multiple LLMs cross-check.
  - Three tiers: **Auto-pass** (no human), **Light review**, **Full review**.
  - Each tier has a clear **price** and **SLA**.
- Using LLMs as validators is one of the safest ways of introducing LLMs into a process. If the human ignores it, no loss. If it spots new errors or the human gets new ideas, quality improves at low cost.
- I finally get why elders in my family prefers eating in a pure (rather than a mixed) vegetarian restaurant. When in Vietnam, I could pick dishes in pure vegetarian restaurants without worrying about whether they were meat or not, even when I didn't understand what the dishes were about. That confidence to proceed without fear is a powerful enabler.
- There's emerging evidence that jobs _automated_ by (not augmented or unaffected by) AI have fewer entry-level jobs. Experienced workers are less affected. Compensation is affected less. [Canaries in the Coal Mine](https://digitaleconomy.stanford.edu/publications/canaries-in-the-coal-mine/)
- [CloudFlare AutoRAG](https://developers.cloudflare.com/autorag/) lets you index any website and expose it as an API + Chatbot with a model of your choice. This is available on the free tier, too. The API follows [NLWeb](https://github.com/nlweb-ai/NLWeb), Microsoft's open standard for LLMs and MCPs to interact with websites in natural language.
- Cloudflare has an [image transformation API](https://developers.cloudflare.com/images/transform-images/transform-via-url/) that also acts as a CDN. Apart from basic transformations, it can auto detect and crop faces, remove backgrounds, and more.
- [oklch](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/oklch) seems the [best color model](https://jakub.kr/components/oklch-colors) supported by all modern browsers. We can use relative colors with it, making color palette design _much_ easier:
  ```css
  #darker-color {
    background-color: oklch(from var(--base-color) calc(l - 0.15) c h);
  }
  ```
- Malware embedded in the compromised `nx` build tool leveraged Claude/Gemini CLI to offload fingerprintable password-gathering code into prompts, making detection significantly harder for traditional security tools. [semgrep](https://semgrep.dev/blog/2025/security-alert-nx-compromised-to-steal-wallets-and-credentials/)
- [Codex CLI](https://developers.openai.com/codex/cli/) has [several updates](https://github.com/openai/codex/releases/tag/rust-v0.24.0)
  - [VS Code plugin](https://developers.openai.com/codex/ide) with remote container execution
  - Drag & drop image support [PR](https://github.com/openai/codex/pull/2567) [Docs](https://github.com/openai/codex/blob/main/docs/getting-started.md#image-input)
  - Queued (editable) messages [PR](https://github.com/openai/codex/pull/2637)
  - Web search via `--search` [PR](https://github.com/openai/codex/pull/2371)
  - `Esc-Esc` to edit previous messages [Docs](https://github.com/openai/codex/blob/main/docs/getting-started.md#escesc-to-edit-a-previous-message)
- Our team passed an image to an LLM for OCR (especially to identify formatting, e.g. bold, italics, etc.), then passed the output _and_ the image to another LLM for improvement. Interestingly, the best LLM (Gemini 2.5 Pro, for this sample of 8 images) out-performed the two-stage workflow. Perhaps incorrect results confuse more than the correct results help? This needs more research.
- OpenAI now has a series of [llms.txt](https://cdn.openai.com/API/docs/txt/llms.txt) URLs.
- Rust seems to catch errors better at compile-time than many typed languages like TypeScript. That makes it better for larger projects (or for AI coding). [The unexpected productivity boost of Rust](https://lubeno.dev/blog/rusts-productivity-curve) #ai-coding
- Image APIs that support hotlinking and searching (useful to support LLM-generated content, e.g. slides or presentations):
  1. Openverse: CC, scale, simple REST.
  2. Wikimedia Commons: CC, historic/diagram breadth.
  3. Pixabay: easy, free, broad, but license fuzzier.
  4. Pexels: beautiful but custom license.
  5. Unsplash: stylish but restrictive.
  6. OpenClipart: niche, useful for icons.
- ⭐ For mental tiredness, the impact of sleep > workload > mood/stress > environment (travel, light, air) > posture > food/drink.
  To rebound, nap > bright light > exercise > fresh air > water > posture/breathing. [ChatGPT](https://chatgpt.com/share/68ae6f42-52a4-800c-b27d-6215e9bd9b89)
- In my internal meetings, I tend to ask many questions (1 per 8 turns), but fewer open-ended ones (~40%) compared with others. I also praise once every 22 turns - among the lowest in our group. I could ask more open-ended questions and acknowledge good work. [#](https://chatgpt.com/c/68ae4c2f-fff4-8329-adff-7e95af88b2ab)
- When seeking advice, people sometimes think aloud, become repetitive, and introduce detail before clarifying intent. Kind candor helps. You can:
  - **State time boundaries**. "We have 20 min. If we spend 5 min on your question, we'll have 15 for solutions."
  - **Clarify intent upfront**. "Before we dive in: _What can I help with_?"
  - **Interrupt, summarize, clarify _early_**. "Cooperative interruptions" are seen as supportive. E.g. "I get this: six accelerators, two done. Great! _What can I help with_? To accelerate?"
- [rclone](https://rclone.org/) is the cleanest way to copy files from Google Drive. I ran `rclone config` to set it up with Google Drive via [native app OAuth key](https://developers.google.com/identity/protocols/oauth2/native-app). Then, `rclone copy "gdrive:" transcripts/ --drive-shared-with-me --include "**Transcript*.docx"` copied all transcripts _including_ "Shared with me" files (not just drives). The `--drive-shared-with-me` enables this.
- [What makes Claude Code so damn good](https://minusx.ai/blog/decoding-claude-code/) has a _detailed_ review of Claude Code's system prompt and is a great for ideas on using LLMs for coding. #ai-coding
- With AI coding, task breakdown, context right-sizing, and automated testing are key levers. #ai-coding
