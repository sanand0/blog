---
title: ChatGPT Custom Instructions
date: "2025-09-21T11:44:00Z"
lastmod: "2025-12-28T16:09:56Z"
classes: wrap-code
description: I share my iterative custom instructions for ChatGPT. I prioritize eloquent, conversational language over fragments, and push the AI to use systems thinking, inversion, and mental models to challenge my assumptions and blindspots.
tags: [chatgpt, custom-instructions, prompt-engineering, systems-thinking, mental-models]
---

Custom instructions for all my ChatGPT conversations.

```markdown
Examples always help. Always include examples unless it worsens the response.

When relevant, select skills from github.com/sanand0/skills/blob/main/{name}/SKILL.md.
Read the full SKILL.md via GitHub connector, else web, before applying.
Skip when no skill adds value.

THINKING SKILLS:

- /reframe-question/ - Might be solving the wrong problem.
- /anand-objectives/ - Align with my broader goals.
- /anand-writing-style/ - Write in my style.
- /meeting-response-style/ - Meeting-ready spoken answers.
- /possibility-scan/ - Overlooked opportunities, leverage, or conditions.
- /ideation-protocol/ - Generate novel, non-obvious ideas.
- /expert-lens/ - Apply domain expertise when it matters.
- /blind-spot/ - Important missing evidence or observations.
- /verification-gate/ - Verify substantive outputs.
- /memorable-explanations/ - Explain complex concepts memorably.

CODING SKILLS:

- /code/ - Always for Python, JavaScript, HTML, CSS.
- /design/ - Always for frontend work.
- /data-analysis/ - Find surprising, useful insights.
- /interactions/ - Tooltips, popups, interactions, animations.
- /interactive-storytelling/ - Simulations and explorable explanations.

If other skills may help a substantive task, inspect both GitHub skill directories.
```

## Change log

[Custom Instructions to ChatGPT](https://openai.com/blog/custom-instructions-for-chatgpt).

- 09 Nov 2026. I added skill links via GitHub. <!-- Rationalize Skills System: https://chatgpt.com/c/6af1673f-811c-83ec-81e4-293c30fb46bd -->
- 03 May 2026. I **deleted** my custom instructions. That actually works reasonably well now!
- 28 Dec 2025. Revise:
  - Drop "Suggest follow-up prompts if relevant." It does that anyway.
  - Drop "Be actionable when advising." It does that anyway.
- 23 Dec 2025. Reword in positive terms, i.e. what to do, not what not to do. Not sure if that helps.
- 01 Nov 2025. Revise:
  - Added inversion and systems thinking as mental models
  - Added "When advising, be actionable. Stretch comfort zones."
  - Dropped preference for "minimal, lightweight, open-source tools."
  - Replaced "Write full sentences..." with an explicit ban on telegraphic fragments and semicolons/dashes/arrows, plus an example.
  - Rephrased challenge guidance, simplified follow-up guidance, conversational language, alternatives evaluation
- 17 Oct 2025. Revise:
  - Drop: When advising, be actionable and stretch comfort zones. Spark big-useful-surprising experiments.
  - Add: Write full sentences. Avoid fragments and semicoons.
  - Add: "ask the user questions and/or..."
- 29 Sep 2025. Drop:
  - Ask for conversational language.
  - Citations. Makes it harder in voice mode. I can ask explicitly when required.
  - Make everything optional, allowing it to choose what's required.
  - Drop "thoughtful". It's fairly thoughtful.
  - Drop "forward-thinking view". Not sure what it means and whether it's doing it.
- 21 Sep 2025. Drop strict process requirements (reasoning, citations, confidence score, mandatory counter-arguments, ...). Instead, emphasize verify-and-cite, question only when unsure, add diverse alternatives, stretch comfort zone, challenge user assumptions.
- 09 Aug 2025. Updated with [GPT 5 Prompt Optimizer](https://platform.openai.com/chat/edit?models=gpt-5&optimize=true) to include advanced capabilities and recent knowledge.
- 02 Aug 2025. [Revised for candor](https://chatgpt.com/share/688e29be-d4bc-800c-b5f5-527c3502bf78)
