---
title: Things I Learned - 03 May 2026
date: 2026-05-03T00:00:00+00:00
categories:
- til
description: This week I learned about LiteParse for PDFs, GPT-5.5's doubled pricing, querying Claude Code usage, and why defining eigenquestions and customer terms matters more than exhaustive ontologies.
tags: [llms, llm-pricing, claude-code, ai-agents]
---

This week, I learned:

- [LiteParse](https://github.com/run-llama/liteparse) is a PDF to text library that you can run via `npx --package=@llamaindex/liteparse lit parse document.pdf`. [Simon Willison](https://simonwillison.net/2026/Apr/23/liteparse-for-the-web/)
- Always add indecisiveness, inaction, "other", "not applicable", etc. as an option to LLMs. They are trained for decisive responses and pattern matching, so we need to guide the the other way. [Martin Fowler](https://martinfowler.com/fragments/2026-04-14.html)
- GPT 5.5 is priced _twice_ that of GPT 5.4. No wonder my Codex usage is much higher than last month. [Simon Willison](https://simonwillison.net/2026/Apr/23/gpt-5-5/#a-few-more-notes-on-gpt-5-5). I am better off sticking to `medium` effort instead of the `xhigh` I usually use - it may not be required. [OpenAI](https://developers.openai.com/api/docs/guides/latest-model)
- "... the eigenquestion is the question where, if answered, it likely answers the subsequent questions as well." [Shishir Mehrotra & Matt Hudson](https://coda.io/@shishir/eigenquestions-the-art-of-framing-problems/eigenquestions-3)
- Claude Code stores the logged in OAuth token at `~/.claude/.credentials.json`. We can use that to fetch `https://api.anthropic.com/api/oauth/usage` and retrieve Claude usage and reset times. `uvx ccusage` does this automatically, but I prefer my own script.
- Ontology matters in the AI era. But some stuff matters more, and some less. <!-- https://claude.ai/chat/2f6fdf7e-9d32-4c45-ac8d-603d029aed5b -->
  - 🟢 MORE: Definitions: what "customer" means
  - 🟢 MORE: Constraints: e.g. "don't reclassify loans"
  - 🟢 MORE: Interactions: how to verify, coordinate, delegate, ...
  - 🔴 LESS: Creating ontologies: agents can do that.
  - 🔴 LESS: Completeness and rigor: agents tolerate uncertainty.
  - 🔴 LESS: Proprietary: agents can reverse-engineer.
- There are several industries / markets that MBA case studies rarely cover ([ChatGPT](https://chatgpt.com/share/69efcf7a-6bf0-83ea-86dd-36e115e7540c)): Kirana stores; Care (child care, elder care, domestic work); Faith (finance, food, media, education); Remittances; Gambling (lottery, sports betting, gacha); Scams & organized fraud; Counterfeiting; ... <!-- https://chatgpt.com/c/69efa7bb-f918-83ea-9bc5-e3f7231c75da + https://gemini.google.com/app/dc5ac9f4a4f44cf0 -->

## Questions I was asked

[Week ending 03 May 2026](https://www.s-anand.net/blog/questions-i-am-asked/#week-ending-2026-05-03)

- **Question**: You're a teacher - what is your role now that AI can do so much?\
  **Answer**: Role has shifted to designing conditions for learning: crafting prompts for students, designing agentic assessments, collecting data on how students learn.
- **Question**: How is this not just students using AI to produce answers?\
  **Answer**: Outcome-based evaluation - if the prompt must produce working code that passes a test, students have to understand enough to iterate.
- **Question**: Who's getting education AI right?\
  **Answer**: Community colleges - career-focused, can't afford to wait for philosophical consensus on AI policy.
- **Question**: You've surveyed university AI policies - how does Harvard compare?\
  **Answer**: Harvard ranks 4th from the bottom among ~30 universities for comprehensiveness; University of Helsinki was at the top.
- **Question**: What are the most underrated skills employers are looking for?\
  **Answer**: Communication - specifically the ability to reach out, make connections, and have substantive conversations.
- **Question**: You're hiring interns - what are you looking for?\
  **Answer**: People who can get the job done without knowing the domain - smart people from tier-2 Indian towns using AI to punch far above their weight.
- **Question**: How do I develop my expertise so I can be like a top data scientist? I feel I can never get there.\
  **Answer**: Don't try to match an expert's knowledge base - AI has commoditized that. Develop judgment: knowing what question to ask, what answer to trust, when to push back.
- **Question**: How do I judge AI quality without expert knowledge - is this the death of expertise?\
  **Answer**: Expertise is not dead but changing: the valuable skill is now knowing enough to ask the right question and recognize a bad answer.
- **Question**: Are you teaching the agent to teach students, or teaching students to use agents?\
  **Answer**: Teaching students to use agents to teach themselves. I'm creating a learning environment, not delivering content.
- **Question**: My team doesn't know what questions to ask AI - how do we help people get comfortable with prompting?\
  **Answer**: Hands-on workshops, competitions, and peer sharing via Slack. Having senior leaders use AI visibly is the biggest accelerator.
- **Question**: How do you manage AI sprawl and shadow AI across an organization?\
  **Answer**: Start with use cases where ROI is clearest, let organic adoption happen, then standardize after seeing what actually sticks.
