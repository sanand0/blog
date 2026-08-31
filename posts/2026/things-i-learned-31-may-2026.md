---
title: Things I Learned - 31 May 2026
date: 2026-05-31T00:00:00+00:00
categories:
- til
description: This week I learned how to query Wikipedia's 35 GB Parquet dump with DuckDB, sign files with cosign, tokenize tabular data, and use ChatGPT memory with local MCP.
tags: [developer-workflow, ai-coding, duckdb, local-mcp]
---

This week, I learned:

- [D-ID](https://www.d-id.com/) is an avatar generator platform like [HeyGen](https://heygen.com/). [Creatify](https://creatify.ai/) and [Synthesia](https://www.synthesia.io/) are a couple of others I heard of. This space seems to be growing.
- [cosign](https://github.com/sigstore/cosign) is a CLI that lets you sign and verify any piece of text with a Google, GitHub or Microsoft account. `cosign sign-blob FILE --bundle sign.json` opens a login window and creates a `sign.json` signature. Anyone who has `FILE` and `sign.json` and the email ID can verify via a Google account with `cosign verify-blob FILE --bundle sign.json --certificate-identity $EMAIL --certificate-oidc-issuer https://accounts.google.com`. <!-- https://chatgpt.com/c/6a197375-fd5c-83ec-9f21-43b084a3830a -->
- [arxiv2md.org](https://arxiv2md.org/) converts arXiv papers to Markdown. [Source](https://github.com/timf34/arxiv2md). [markxiv.org](https://markxiv.org/) claims the same - by just changing the URL - but it ended up reporting an error when I tried this link: <https://markxiv.org/abs/2604.08649>.
- From Akhilesh Tilotia: So we have someone in our team with initials AS. She made a document which was named vAS. Then I made edits and named it vAT. These docs were in a CoWork folder. I asked Claude to clean up my doc. It created another version for me to review. In its wisdom, it named the file vAU 🙂
- Maybe what a forward-deployed engineer does is enginer AI-native workflows. (This sounded profound when I wrote it down. Not sure if it'll sound as profound tomorrow.) The idea is that the FDE will say, screw existing processes; let me fire up my AI agent and get stuff done; THEN we'll figure out what works, how to optimize it, etc.
- The [PRAGMA: Revolut Foundation Model](https://arxiv.org/abs/2604.08649) has some good tokenization ideas for tabular data. Create your own token space with `key–value–time` tokenization - to retain field information. Bucketize numbers by percentile, preserving magnitude/ordering that subword tokenization destroys. Encode time both as log-seconds _and_ as cyclical calendar features.
- Codex uses the <kbd>Alt + Up Arrow</kbd> key to edit queued commands, but on the VS Code terminal, this key binding is not sent to the terminal. Enable the `terminal.integrated.sendKeybindingsToShell` setting to send it to the terminal, hence Codex.
- Based on this [catalog](https://chatgpt.com/share/6a16dfd6-bd70-83ec-807a-646366ba9a99) on "universal foods", here's what I 🟢 like, am 🟡 neutral, 🔴 dislike, 🟣 must try, and will ⚫ skip. <!-- https://chatgpt.com/c/6a165e95-5100-83ec-8b90-c41fd2876fdf -->
  - Universal favorites: 🟢 pizza, 🟢 fried potatoes/chicken, 🟡 dumplings, 🟢 ice cream.
  - Universal comfort foods: 🟢 khichdi, 🟡 congee, 🟡 dal-rice, 🟡 risotto, 🟡 ramen, 🟢 pho, ⚫ chicken noodle soup, 🔴 rice porridge, 🟡 mac-and-cheese, 🔴 mashed potato, 🟣 polenta, 🟢 oatmeal, 🟣 Japanese curry rice.
  - Acquired tastes that convert most: 🟡 coffee, 🟢 tea, 🟡 dark chocolate, 🟢 mild fermented dairy, 🟢 pickles, 🟢 olives, 🟣 kimchi, 🟣 miso, 🟢 mild chili dishes.
  - Acquired tastes that have cult devotion: 🟣 durian, 🟣 natto, 🟣 stinky tofu, ⚫ fermented fish, ⚫ hákarl, 🟢 very funky blue cheese, ⚫ offal.
- [OceanoPDF](https://oceanofpdf.com/) seems like a good place to download ePubs of books.
- The entire Wikipedia is available as a [Parquet file](https://huggingface.co/datasets/wikimedia/structured-wikipedia). You can query it like `duckdb -c "FROM 'hf://datasets/wikimedia/structured-wikipedia/enwiki/data/*.parquet' LIMIT 5"`. The English version has 35 GB, 7.6 million articles, and you're better off downloading it rather than running analyses remotely.
- When you receive a Calendly link of the form `https://cal.com/USER/EVENT` you can fetch the available slots via `curl -H 'cal-api-version: 2024-09-04' 'https://api.cal.com/v2/slots?eventTypeSlug=EVENT&username=USER&start=2026-05-25&end=2026-06-01&timeZone=Asia/Singapore&format=range'`. Useful to automate good meeting-slot selection. <!-- https://chatgpt.com/c/6a126d5e-b9c8-83ec-a88b-f230d04434e9 -->
- "Reference saved memories" in ChatGPT is different from "Reference chat history" as per [OpenAI](https://help.openai.com/en/articles/8590148-memory-faq). In [Developer Mode](https://help.openai.com/en/articles/12584461-developer-mode-and-mcp-apps-in-chatgpt), memory is turned off, but not chat history. I confirmed that I can access past conversations in Developer Mode. It might be a privacy concern for others, but for me, this is singularly useful, because I can use ChatGPT with [Local MCP](https://www.s-anand.net/blog/how-i-use-local-mcp/) effectively getting a non-metered AI coding agent. <!-- https://chatgpt.com/c/6a12c899-ac5c-83ec-a4fa-6e0717f810b3 -->
- Seems GPT-5.2 reaches expert level in peer review: 45 scientists took 469 hours evaluating human & AI reviews on 82 papers. "Surprisingly, current AI reviewers are competitive even with the top-rated reviewers in Nature’s official peer review..." though not without weaknesses, so use AI + humans. [On the limits and opportunities of AI reviewers: Reviewing the reviews of Nature-family papers with 45 expert scientists](https://arxiv.org/abs/2605.20668) via [Ethan Mollick](https://bsky.app/profile/emollick.bsky.social/post/3mmf2ano3ik27)

## Questions I was asked

[Week ending 31 May 2026](https://www.s-anand.net/blog/questions-i-am-asked/#week-ending-2026-05-31)

- **Question**: Which learning use cases are worth turning into AI simulations?\
  **Answer**: Pick skills that are hard to practice, have delayed feedback, are subjective, and where someone will pay because failure is expensive. Financial services is a good hunting ground.
- **Question**: How should services firms avoid being dragged into depreciating software delivery?\
  **Answer**: Stop selling software as the asset. Put FDEs with agents into the business, deliver useful outputs from day one, and let prompts, code and tools behind the scenes be our problem.
- **Question**: What should we ask agents to do when we only have a dataset and no clear use case?\
  **Answer**: Point it at the dataset and ask for data quality issues, profit-increasing actions, cost-reducing actions, and surprising actions the business has not thought of.
- **Question**: After we identify low-hanging AI use cases, what should we take to stakeholders?\
  **Answer**: Don’t take a use-case deck. Solve one problem and send the stakeholder a concrete “do this” recommendation with evidence; then use disagreement as feedback.
- **Question**: What should a “Verify” button do on AI-generated data stories?\
  **Answer**: It should show the verification SOP: what claim is made, where the source data is, what code or steps checked it, and what a human should cross-check.
- **Question**: How do we move demos from point wows to workflow wows?\
  **Answer**: Show the workflow being dynamically built and executed, not just task automation. The unit is now the agent, not the LLM API; prompts, hooks, plugins, skills and sub-agents are the architecture.
- **Question**: Do we need to create a data lake and taxonomy before AI can answer from messy content?\
  **Answer**: No. Start the AI engagement and data lake in parallel; agents can turn messy content into semi-structured taxonomies while usage tells you what structure matters.
- **Question**: How should we create golden sets for model evaluation?\
  **Answer**: Start from SME-validated input-output pairs already lying in sheets, Drive, emails, or attachments. Use AI to clean and sample them, especially around mistakes humans actually corrected.
- **Question**: When should we use a fresh AI-heavy technical person in client work?\
  **Answer**: Use them for one- or two-day proof points where the output needs to be impressive fast. Use cloud architects or senior engineers for architecture, compliance, and production setup.
- **Question**: How should AI Ops track model pricing and model choice?\
  **Answer**: Use telemetry. Find wrong model usage, switch to Pareto-optimal models, and make someone accountable for cost-quality monitoring.
- **Question**: Do we need a data foundation before integrating six sources and spinning up a dashboard?\
  **Answer**: No. Tell the agent to connect to the sources and build it; prepare the foundation as it works.
- **Question**: Won’t AI-agent costs explode like a cloud subscription?\
  **Answer**: Compare it to manual cost, not zero. Model costs are falling and swappable; for the foreseeable future, a human is 10x-100x more expensive for the same repeatable work.
- **Question**: How do we stop software delivery from becoming a depreciating asset?\
  **Answer**: Sell reconciled outputs and business insights, not software. Keep prompts, scripts, rules, evals, and client feedback as a continuously improving asset.
- **Question**: What should I produce from existing client data?\
  **Answer**: One-paragraph business-actionable emails: do this because of this, with a chart or table as proof and an Excel attachment if needed.
- **Question**: How should the system learn from client reactions?\
  **Answer**: Create a folder catalog of each analysis and track what was sent and how the client responded. That becomes the operating memory for better future analysis.
- **Question**: How do we make a client template easy but informative?\
  **Answer**: Pre-fill it through research. Use multiple-choice and evocative options so the survey itself becomes a pitch and credibility exercise.
- **Question**: How is FDE different from staff augmentation?\
  **Answer**: Staffing may look similar; pricing must not. Charge for accepted dashboards, reports or answers, not for the person's hours.
- **Question**: How do we make AI operationalization a muscle?\
  **Answer**: Codify a playbook, train and certify talent, instrument telemetry and standardize architectures, but start small and evolve.
- **Question**: Top-down roadmap or bottoms-up early adopters?\
  **Answer**: Both. Top-down gives the roadmap; bottoms-up proves what works. They meet through telemetry and feedback loops.
- **Question**: Is the new software framework still software?\
  **Answer**: Better call it workflows. The asset is markdown prompts, tool instructions, tests and reusable context that generate code on demand.
- **Question**: Can AI personas substitute for surveys?\
  **Answer**: Sometimes directionally. Use personas when real surveys are unaffordable, but treat them as correlated proxies, not ground truth.
- **Question**: Are LLM responses stateless and return independent answers when asked the same prompt repeatedly?\
  **Answer**: Yes. When used as APIs (not a chat), they are stateless - though non-deterministic.
- **Question**: How does Services-as-Software apply to AI SDLC?\
  **Answer**: Don't sell software as the deliverable. Sell that the process or software keeps working; Ops and evaluation are the value.
- **Question**: What hook should we pitch forward-deployed engineers with?\
  **Answer**: Lead time. Agentic AI is the shiny object; results from day one is the business hook.
- **Question**: How should we pitch fraud detection?\
  **Answer**: Put an SME with agents to craft rules from client knowledge, industry practice and data. Use feedback loops to reduce manual review and catch more fraud.
- **Question**: Do we really need a paid ChatGPT account?\
  **Answer**: Yes. For serious technical work, use the best paid thinking model; $20 is the best investment anyone can make.
- **Question**: How should we start an AI-based technical solution?\
  **Answer**: Dictate the problem into the AI live. The first step is making both the human and the model understand the problem statement.
- **Question**: If I do not have all the requested data yet, what should I do?\
  **Answer**: Upload what you have and ask the model to rank what else it truly needs. Do not wait for perfect data; AI asks like a consultant.
- **Question**: Can an agent validate extracted data against PDFs like a human QA reviewer?\
  **Answer**: Yes. Give it the full instruction you'd give a new human reviewer as a prompt.
- **Question**: How do we move from AI use cases to business value?\
  **Answer**: Replace "use case" with "answer" or "action." Send one-page evidence-backed recommendations like "these 15 customers may churn because of X/Y/Z."
- **Question**: How should the agent investigate correlations?\
  **Answer**: Let it take many candidates, drop obvious correlations, create ratios for correlated variables,and ask which patterns are surprising and actionable.
- **Question**: How granular should our slide taxonomy be?\
  **Answer**: Don't overbuild taxonomy upfront. Let agents take real requests, search, assemble decks and let taxonomy emerge from usage.
- **Question**: Should we build better search ourselves or use Onyx, Glean or Algolia?\
  **Answer**: Use good search tools if they help, but agents reduce dependence on perfect search. They can read, search using multiple keywords, iterate and assemble despite imperfect retrieval.
