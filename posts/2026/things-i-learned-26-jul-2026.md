---
title: Things I Learned - 26 Jul 2026
date: 2026-07-26T00:00:00+00:00
categories:
- til
description: This week I learned how context makes AI email replies useful, why Claude Code benefits from fewer examples and tools, and how agents can turn documents, videos, and datasets into practical skills.
tags: [ai-agents, claude-code, prompt-engineering, personal-data]
---

This week, I learned:

- Thinking traces vanished in ChatGPT Work (or did they never exist) and [seem to be vanishing in Claude](https://x.com/emollick/status/2080829512275624173). Not sure if it's because Chinese models are using the thinking traces as signals.
- [ChatGPT Skills](https://chatgpt.com/skills) is available in the Plus plan. This was available to Enterprise and Edu, but since I saw this on ChatGPT just today, I guess it's a recent feature. <!-- https://chatgpt.com/c/6a64b13b-2fdc-83ec-aca1-a067fd23c6ce -->
- Peter Gostev compares Opus 5, Fable 5, Kimi K3, GPT 5.6 Sol, GLM 5.3, etc. on a variety of visual tasks in this [video](https://youtu.be/UDE0qOnAb-I). The most intruiguing prompt I spotted was: "I would like you to research the most interesting, impressive dataset where I would learn something about the world and you can visualize in the most creative way, making it something completely unexpected. Then create the most elaborate version of it possible." This apart, I got the general sense that Opus 5 is _quite_ good at visualization and design, perhaps even better than Fable 5.
- After reflecting on [Knowledge graph construction with Claude](https://platform.claude.com/cookbook/capabilities-knowledge-graph-guide), I believe that knowledge graph construction is roughly: "Tag each document with people, place, org, event, etc." - and it's good enough for agents to use.
- Increasingly, the real question isn't "What interesting things you doing with agents?" It is the followup? "What lets you do that (when I can't)"? For example, [Naveen](https://www.linkedin.com/in/naveengattu/) asked me, "Can I set up your email reply agent?" I said, "No, you don't have transcripts, blogs, notes, or exports like I do."
- LinkedIn lets you [save a profile as PDF](https://www.linkedin.com/help/linkedin/answer/a541960/saving-a-profile-in-a-pdf-format). While it formats text reasonably well, it doesn't preserve newlines in the "About" section - so what looks good on the browser looks terrible in the PDF. Such PDFs are sent to interviewers, making it a bit of a bad experience for the interviewee. (Of course, it could also be a signal to see how well interviewees pay attention to small details like LinkedIn PDF formatting.) <!-- https://chatgpt.com/c/6a631464-2300-83ec-b3ca-e6a418314175 -->
- The ability to measure an outcome is (and has always been) important. It lets you capture value (outcome pricing) when you control the outcome, or de-risk (insurance) when you don't. But what might be new is that metrics are outdated at an increasingly faster pace - so (a) setting an expiry date and (b) knowing if it's expired have become important. <!-- Outcome-based pricing models and enablers: https://claude.ai/chat/92b43646-2880-4102-ae8a-ef61c6b7735f -->
- I wasn't using AI to reply to emails because (a) it didn't have enough context and (b) it didn't write in my style. I spent a few months making sure I give them context and style guidance. Given the current intelligence of models and my [email reply](https://www.s-anand.net/blog/prompts/email-reply/) prompt, I'm now happy for AI to answer my emails.
- My learnings based on [YC request for startups Fall 2026](https://www.ycombinator.com/rfs) - which probably means we'll see many more startups in these spaces. Here are my takeaways:
  - Self-Maintaining APIs: Nice idea. When a service changes an API, they share an agent/skill that can fix YOUR code to upgrade the API!
  - AI-Native Compliance Infrastructure: So, compliance becomes cheaper => MORE and STRICTER regulation. Licensees become valuable (AI rollup). Private regulator feedback becomes valuable. Compliance companies will themselves get regulated (like auditors). <!-- https://chatgpt.com/c/6a62fbf5-7180-83ec-ab1f-d417fc5f560f + https://claude.ai/chat/4cfd8680-a67d-45a7-b364-bda05cefa649 -->
  - Multiplayer AI: [Claude Tag](https://www.anthropic.com/news/introducing-claude-tag) is a step in this direction. WhatsApp's @Meta is too. I expect most chats will allow AI as participants. Most collaborative software, too - GitHub, JIRA, Figma, GMail, HubSpot, maybe even VS Code, Office/Notion, Chrome, Games, ...
  - A Cloud for Small Software: Systems of record are likely to be safe, but software AROUND it will explode into tiny tools. Access control, ratings, ... is what'll be important, not generation / managing them. <!-- https://claude.ai/chat/1fac6122-d85d-490c-bfdf-e71ae1e79d02 + https://chatgpt.com/c/6a630348-0c68-83ec-856c-69641da775b9 -->
- Grok 4.5 took [14 iterations](https://grok-cheese-essay.julius.site/) to write an essay about Cheese before Pangram declared it "Human". Pangram is increasingly becoming the new Turing Test. [Rahul](https://x.com/0interestrates/status/2079730851580084560)
- Notes from a Claude Code interview with [Simon Willison](https://simonwillison.net/2026/Jul/21/cat-and-thariq/):
  - Fewer examples. More examples don't help Fable and Opus 4.8. "... removing examples was extremely helpful, because it was just more creative than the examples we gave it."
  - Fewer hard constraints like "fewer “do not do this” instructions, because that’s a very strong impulse for Claude, and especially if it conflicts with user instructions". "Do X when ..." or "Do X because ..." is more helpful.
  - Fewer tools. A few general-purpose tools work best.
  - Fewer sandboxes. Auto-mode is safe enough. Sonnet judges every tool call with context, enabling dynamic permissions.
  - Fewer software / integrations. Use Claude Code itself as the software / integration layer.
  - Fewer components. Memory is just a Markdown file in the right folder.
  - Fewer interventions. "... given a COMPLETE definition of a task... does Claude make the right decisions"
  - Fewer decisions. Fewer reviews. Generation is cheap, so let people who need something get there immediately, as long as a good AI judges and its reversible.
  - "We actually have a different system prompt per model now".
  - Claude Tag is next evolution of Claude Code: Multiple people interacting per channel, working with Claude on a task. (Claude tag contributes to 65% of our PRs)
- [Apache Ossie](https://ossie.apache.org/) is a YAML standard for dataset metadata. If adoption grows, it could be a useful machine and human readable way to document and describe datasets. Databricks, Snowflake, Qlik, are part of the group. If more join, this could become a useful standard.
- An interesting technique to build an efficient video understanding agent. Use AI to generate transcripts with timestamps. Have it identify key moments, e.g. where the presenter explicitly ("as you can see") or implicitly ("these two cells") flags something on screen. Extract up to ~50 of the most important frames. [claude-video SKILL.md](https://github.com/bradautomates/claude-video/blob/main/skills/watch/SKILL.md#transcript-cue-frames)
- [Cangjie Skill](https://github.com/kangarooking/cangjie-skill) converts books, videos, etc. into AI skills, like [Poor Charlie's Almanack skills](https://github.com/kangarooking/poor-charlies-almanack-skill). However, since AI has already read most of these, the value of this (compared with "Apply principles from Poor Charlie's Almanack") is unclear.
- `Alt+Shift+Right Arrow` expands selection in VS Code, and `Alt+Shift+Left Arrow` shrinks selection. That's useful in Markdown, HTML, etc. to select sections. Since [Jun 2026](https://code.visualstudio.com/updates/v1_120#_smart-select-for-markdown-tables), this also lets you select a specific Markdown table cell, row, or entire table. Also, since [Jan 2026](https://code.visualstudio.com/updates/v1_109#_select-bracket-and-string-content-with-double-click), double-clicking _just inside_ quotes or brackets selects the entire contents inside.
- I analyzed the Claude Code session of a domain expert building an enterprise application without knowing how to code. Here's what I learnt about expertise: <!-- https://chatgpt.com/c/6a60c799-ba90-83ee-94b5-6d09d116f8b9 - Kalidas CRM application -->
  - An expert can instantly see errors / misses and their causes - amateurs can't.
  - An expert can point to specific nitty-gritty details - amateurs can't.
  - An expert knows what's possible/easy and what's not - amateurs don't.
  - An expert has strong opinions that're often right - amateurs don't.
- Claude gave me $100 credits until 19 Sep and Fable 5 will now consume those. My queries cost about $1, so I have ~100 queries to exhaust in ~60 days. About 1.5 Fable queries a day. That's about what I normally ask Claude, so I think I should just stick to Fable 5 until my promotional credit expires - it'll expire otherwise anyway. But using it with Claude Code is quite expensive ($7 is common.)
- I asked ChatGPT to analyze an MRI report and compared it with the doctor's. Problem: they agreed on what problems most people in that age group face; they disagreed on things I have no way of validating! Maybe it's best to use a doctor / radiologist to read the MRI, diagnose, and prescribe - but use AI to translate and cross-check (e.g. is this a typical age-related problem, is this the standard treatment, etc.) <!-- https://claude.ai/chat/0ae952ea-9cd3-4f0a-a28b-fa62a09f11ce + https://chatgpt.com/c/6a578bb5-d5d4-83e8-82c7-e5838c4fbb40 -->
- Both ChatGPT and Claude subscriptions offer an OAuth based coding agent API access - [Codex SDK](https://learn.chatgpt.com/docs/codex-sdk) and [Claude Agent SDK](https://github.com/anthropics/claude-agent-sdk-python) - which is how coding agents like [Pi](https://pi.dev/), [OpenCode](https://opencode.ai/), etc. are able to authenticate and use the subscription. This means that anyone can build their own harness using existing subscriptions. [ChatGPT](https://chatgpt.com/share/6a5dbb44-5bb8-83e8-a5c2-3b802951e551) <!-- https://chatgpt.com/c/6a5db0f0-648c-83e8-98a4-a165a53ad866 -->
- A useful way to improve your SKILL.md files from others' skills or prompts is: <!-- https://claude.ai/chat/365908a3-49ee-49d8-960a-89bee3367bb8 + https://chatgpt.com/c/6a54f875-6d6c-83e8-9501-7ee70aa7b983 -->
  - "What cool prompting / SKILL.md techniques does this have?"
  - "Based on my usage patterns and objectives, which of these have the highest impact (provides highest uplift to my chats) x frequency (relevance)?"
  - "Review all my skills. See what applies where. Filter what has HIGH impact. Draft the full diffs for the relevant skill files."
- GPT 5.6 Sol attempted the [Cycle Double Cover Conjecture](https://mathworld.wolfram.com/CycleDoubleCoverConjecture.html). An interesting learning from [the prompt](https://cdn.openai.com/pdf/04d1d1e4-bc75-476a-97cf-49055cd98d31/cdc_prompt.pdf) is how they listed tempting outputs that APPEAR to satisfy this request, but would not actually, and told it to avoid them: "Use adversarial agents throughout: every candidate proof must be checked for exact-two multiplicity, repeated-edge closed trails masquerading as cycles, ..."

## Questions I was asked

[Week ending 26 Jul 2026](https://www.s-anand.net/blog/questions-i-am-asked/#week-ending-2026-07-26)

- **Question**: How do we protect our computers when agents download files and run commands?\
  **Answer**: Sandbox and give the least access required, e.g. using containers. Where required, use auto mode in Claude Code / Codex - they're pretty good these days.
- **Question**: Should we learn to create AI skills or buy skills others sell?\
  **Answer**: No, unless a cheap skill solves an immediate problem. Skills are mostly reusable prompts - and they depreciate. Try it, use it if it clearly helps or a benchmark shows you that it does. Buy if you're convinced of a gap and can't bridge it yourself.
- **Question**: Do AI interns need hard skills or a degree like BS Mathematics?\
  **Answer**: No. Hire for high agency—people who act without being told. The rest is trainable; the real bottlenecks are access to AI, access to data, and a manager with business sense.
- **Question**: How do you train capable AI builders to stop waiting for assigned work?\
  **Answer**: Repeatedly ask, “What did you do that nobody asked you to do?” Have them research stakeholders, deliver small outputs, track what gets ignored or used, and iterate until useful work becomes self-directed.
- **Question**: How is connecting an agent to Google Drive and email different from pasting documents into it?\
  **Answer**: The connector adds discovery, not just access. It can find new, forgotten, or previously unknown context across files, email, calendars, and transcripts, then revise priorities as that context changes.
- **Question**: Can we tell whether a CLI is agent-friendly just by asking the agent?\
  **Answer**: No. Have agents use it on diverse tasks and measure errors, correctness, time, tokens, and output quality; then improve the skill from the execution logs and retest.
- **Question**: Why is your "Ask AI" email agent better than asking Claude or ChatGPT directly?\
  **Answer**: The model is not the difference. My agent is connected to my transcripts, notes, blog, emails, search tools, and my style of answering. That context is the difference.
- **Question**: If you built an AI company today, what would you focus on?\
  **Answer**: Don't start with a generic platform. Pick one workflow, deliver ten accepted outputs, and assetize every correction into tests, verifiers, skills, connectors, and context; if output ten is much cheaper, faster, or better than output one, it could be my next company.
- **Question**: How do I build credibility for an AI product role before I have the title?\
  **Answer**: Do the job before asking for the role. Pick one repeated workflow, deliver the actual output on approved data, have the owner review it, and show measured improvement; a stakeholder saying "we use this" beats courses and polished demos. This is what an FDE does.
- **Question**: As AI takes over analytics and visualization craft, will organizations still need analytics people?\
  **Answer**: Yes, but analytics people must become AI-conversant. Intead of producing charts, focus on what comes before and after: problem framing, domain context, communication, and decisions.
- **Question**: How do you use Claude and other AI tools for thought work?\
  **Answer**: Use AI for thought work, not just chat. Delegate all thinking as a practice, then do the parts it fails at that you can catch.
- **Question**: How do we benchmark whether an AI skill actually improves performance?\
  **Answer**: Define “better” and construct the rubric independently of the skill. Compare baseline versus skill across diverse unseen tasks, use independent judges, and watch for models preferring their own outputs.
- **Question**: Should an AI evaluation checklist be short or comprehensive?\
  **Answer**: Comprehensive for the agent; concise for the human. Keep the full machine-readable checklist, then show reviewers only the failures and decisions.
- **Question**: How do we make an AI hackathon useful for non-developers?\
  **Answer**: Ask for the output, not the code. Let people use any tool and judge working demos by usefulness; code can be allowed without making it the entry barrier.
- **Question**: What should I proactively build and show my manager?\
  **Answer**: Have an agent research the manager's goals and propose useful prototype options, pick one, build it, and ask for feedback. Delegate the blank-page problem, not the choice.
