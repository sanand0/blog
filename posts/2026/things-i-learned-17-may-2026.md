---
title: Things I Learned - 17 May 2026
date: 2026-05-17T00:00:00+00:00
categories:
- til
description: I learned to ask what others and I must take away from conversations; linked data and AI make taxonomies useful; Bitwarden’s CLI avoids plaintext passwords; flipbook.page offers visual exploration.
tags: [generative-ai, ai-coding-agents, prediction-markets]
---

This week, I learned:

- I had GPT-5.5 and Opus 4.7 analyze a few of my conversations and learnt that I need to ask myself: "What must they take away? What must you take away?" in my conversations. That lets me speak with intention rather than instict. (Instinct has its place. I happen to over-use it.) <!-- Based on Ankor Disagreement on Outcome Pricing: https://chatgpt.com/c/6a07db43-8b68-83ec-8aa6-da51ebca2c86 | https://claude.ai/chat/3e2ccaae-e6a0-473c-9f81-8d5787e689ad -->
- Turns out there are several well-established taxonomies. It makes sense to align with these. Linked data is powerful and AI makes linkage easy.
  - **General Knowledge**: Wikidata, DBpedia, YAGO.
  - **People**: VIAF, ISNI, ORCID, LC Name Authority, GND.
  - **Places**: GeoNames, Getty TGN, ISO 3166.
  - **Organizations**: LEI, ROR, Wikidata.
  - **Books/Media**: Open Library, WorldCat, MusicBrainz, IMDB.
  - **Chemicals/Biology**: PubChem, ChEBI, GBIF, ITIS.
  - **Legal/Units/Math/Events**: EuroVoc, QUDT, OEIS, PeriodO, etc.
- BitWarden supports a [`bw` CLI](https://bitwarden.com/help/cli/) that seems handy for quick CLI access to passwords. It's a step towards me moving away from saving passwords unencrypted on my local file system.
- Singapore has banned prediction markets like Polymarket and Kalshi. Pity. I was hoping to use AI coding agents to play them. [Yahoo](https://sg.news.yahoo.com/why-people-betting-thousands-dollars-023000224.html)
- [flipbook.page](https://flipbook.page/) is a fascinating generative UI exploration. It's a visual browser, i.e. it generates an image based on text, you click anywhere, it generates an image interpreting based on where you clicked, and so on. A very different style of exploration!
- Vercel's [`deepsec`](https://github.com/vercel-labs/deepsec/) uses Codex / Claude to search for vulnerabilities, but "scans can cost thousands or even tens-of-thousands of dollars for large codebases".
- When I charge my Lenovo Thinkpad (P1 Gen 7) with the 170W charger that came with the laptop, it delivers ~60W of power to the battery, charging the laptop in about an hour. A 65W laptop delivers half the power and takes twice as long.

## Questions I was asked

[Week ending 17 May 2026](https://www.s-anand.net/blog/questions-i-am-asked/#week-ending-2026-05-17)

- **Question**: How should outcome pricing replace software-hour pricing?\
  **Answer**: Price what the client really values: the compliance reports, reconciled data rooms, research outputs, etc. instead of the software. Software is cheap. Price in the integration, verification, and accountability.
- **Question**: If AI can generate software and reports, where is our value?\
  **Answer**: Find out. Use AI for everything, log where it fails, and turn those failures into our assets: prompts, tests, evals, tools, SKILL.md.
- **Question**: How should people reskill for AI?\
  **Answer**: Use AI for everything. Build skills around where AI fails.
- **Question**: Should we build an agentic learning-trace tool for students?\
  **Answer**: Decouple tools. Capturing learning with a lightweight authenticated terminal recorder. Don't build an agent platform - reuse what's available.
- **Question**: Is it just a one-line prompt or do we need trained agents?\
  **Answer**: Start minimally. When it fails, meta-prompt to understand how to improve. Agents keep improving, so re-evaluate to simplify periodically.
- **Question**: Why does AI make even experts feel they "know nothing"?\
  **Answer**: The frontier is moving faster than we can learn. Experts now have much more framing and verification than production work - a change that requires effort.
- **Question**: What is different about AI-native delivery versus a 7-14 day POC?\
  **Answer**: Day zero. Instead of waiting for a POC, put people with agents inside the workflow immediately, deliver the needed output, then evolve prompts, connectors, code, and automation behind the scenes.
- **Question**: How should outcome-based pricing work?\
  **Answer**: Price useful outputs and decisions, not development hours. Start with variable OpEx, add minimums later, and let the improving workflow/context become the asset.
- **Question**: Does Anthropic use client data for training when you use Claude commercially?\
  **Answer**: No - enterprise and API usage is explicitly excluded from training data.
- **Question**: If everyone opts out of training data, how does Claude get better?\
  **Answer**: Anthropic uses synthetic data which is quite effective. (Also: separately consented/purchased datasets, red-teaming.)
- **Question**: What if the client wants only a tool and no human service layer?\
  **Answer**: Say yes, but reframe. Software depreciates. The workflow, context, evals are worth more. Build the tool if they want IP, but deliver outcomes from day one.
- **Question**: Private-company data is messy, unstructured, and often local-language; how do we verify outputs we cannot easily read?\
  **Answer**: Use checker agents and let native-speakers humans review just the exceptions.
- **Question**: How long does prompt refinement take in real projects?\
  **Answer**: Five minutes for rough directional changes; one or two days for a reusable workflow; months for true productionization handling edge cases, with evals, tools, governance, and client acceptance.
- **Question**: Can Claude or Codex automate Bloomberg, CapIQ, PitchBook, or Mergermarket workflows?\
  **Answer**: Technically, often yes; contractually, be careful. Scrape manually when automation is not allowed and price higher.
- **Question**: What is the real takeaway from paying $20 for ChatGPT Plus?\
  **Answer**: For a tiny monthly cost, each analyst gets a high-capability research assistant that can read files, browse, reason, draft, rewrite, and analyze data. The real benefit is when the team learns to delegate.
- **Question**: Clients have asked us not to use GenAI; what should we do?\
  **Answer**: Don't use it where the client prohibits it. Use public-data demos, anonymized examples, and internal productivity experiments.
- **Question**: Should we use Perplexity for research output?\
  **Answer**: Prefer ChatGPT and Claude, which have better tools - notably code execution - that is often required.
- **Question**: Can agents read non-editable PDFs?\
  **Answer**: Yes. They have vision models that can read scanned documents, images, and PDFs.
- **Question**: Can we force the AI to use only official regulatory, ministry, NRA, or government sources instead of blogs and news sites?\
  **Answer**: Yes. Tell it explicitly, give it the process manual, require citations, and reject non-official sources. Treat it like briefing a researcher: "Use only equivalent NRA and government sites; redo the research."
- **Question**: Can AI create an Omdia-style telecom regulation report for another country from an existing South Africa report?\
  **Answer**: Yes. Upload the sample report, ask for an identical report for Vietnam / India / Germany, and let ChatGPT or Claude research, synthesize, and draft. It can shrink the human time of a few days to 10-30 minutes.
- **Question**: How do you infuse your personal AI practice into your engineering team?\
  **Answer**: Encouraging coding agents in documentation, testing; standardizing practicess across repositories and teams; training on verification: LLM-as-judge, TDD, synthetic data stress-tests; and using coding agents themselves as the solution.
- **Question**: Is "chat with big data" supposed to make hour-long queries run in seconds?\
  **Answer**: No. AI speeds up query generation, not execution speed. But it can optimize and enable pre-aggregation or caching.
- **Question**: For financial analysis and report writing, which AI tool is better - Gemini, ChatGPT, Claude, or Copilot?\
  **Answer**: This month: Claude beats ChatGPT beats Gemini. Next month, it may change. Use paid frontier models. Compare outputs regularly.
- **Question**: Can I upload an existing financial model spreadsheet and ask AI to roll it forward for the latest quarter?\
  **Answer**: Yes. Upload the spreadsheet and ask AI to update it. Then verify formulas and assumptions.
- **Question**: Will Claude help with financial models too, or only research?\
  **Answer**: Models too. Delegate the whole task: research, extraction, calculations, formatting, even sanity checks.
- **Question**: Copilot seems better at analyst-style writing than Claude or Gemini - is that right?\
  **Answer**: Only if you compare it with weak or free versions. Against paid frontier models, Copilot style is comparable or worse, and it can't execute code.
- **Question**: Should each executive-facing claim have traceable sources?\
  **Answer**: Yes. Source links are not enough. Include quotes behind the claims for fast verification.
- **Question**: How deterministic is a financial agent for executive use?\
  **Answer**: Code is deterministic. Output and interpretations still need validation. I'd keep the UI light and focus on verification.
- **Question**: Our client says any AI use requires permission. What do we do?\
  **Answer**: Start where it's easiest: new work - with no incumbent or competition, public data, secondary research. Prove value. THEN ask for permission.
- **Question**: If we give AI all the input, can it create a 50-60% ready sell-side or buy-side research report?\
  **Answer**: Yes. Put the best SMEs in the room. Finish real reports DURING the workshop. Show, rather than tell.
- **Question**: Are big one-shot prompts worse than step-by-step prompts?\
  **Answer**: Yes, for weaker models. Aim high first; if it fails, break it down; after model updates, retry longer tasks so you don't stay stuck in an old workflow.
- **Question**: Should we collect everyone's prompts and ask AI what works best?\
  **Answer**: Yes. Put your Cortex prompts in an append-only Snowflake table, capture what worked and failed, and turn it into a reference and onboarding asset.
- **Question**: Can prompts help new joiners understand complex databases better than KT documents?\
  **Answer**: Yes. Store business context as retrievable text. Let prompts teach by doing. AI-native KT beats documentation for changing systems.
- **Question**: For the casino and hotel marketing team, what should we pitch beyond a dashboard?\
  **Answer**: Pitch an always-on AI-enabled advisory team that delivers insights and actions. No upfront software; just rapid research, recommendations and outcomes.
- **Question**: Do clients need clear KPIs before we start an outcome-style AI engagement?\
  **Answer**: No. Just pick an area. Even if they don't know the KPI, the agent can infer role-relevant KPIs and propose something useful.
- **Question**: Does the agent need to understand cross-sell instead of just searching for the word?\
  **Answer**: Correct. That is the difference between search and agentic reasoning: infer the plan first, THEN execute the search.
- **Question**: Are you giving Claude access to your files, and how?\
  **Answer**: Yes, through MCP and a detailed prompt. Give access, make it plan, and tell it to reframe bad questions like an expert.
- **Question**: Why don't we train a custom model with all our knowledge already inside it?\
  **Answer**: Don't. Custom training is costly and slow. Save your knowledge in SKILL.md, databases, folders, custom code... that's cheaper and faster.
- **Question**: Can AI learn corrections and store them?\
  **Answer**: Yes, but only if we deliberately convert corrections into assets: skills, checklists, habits, tests or knowledge snippets.
- **Question**: Is the agent building software behind the scenes?\
  **Answer**: Yes, when needed. Software is plumbing; the product is the answer or action the user wanted.
- **Question**: How do we ensure board members have the same baseline knowledge but can still ask follow-ups?\
  **Answer**: Generate a common board pack for everyone, then let individuals drill down privately. Standardize the baseline, but don't limit curiosity.
- **Question**: After AI generates an HTML or PowerPoint answer, can users continue the conversation?\
  **Answer**: Yes. The report is not the end; it's just a by-product.
