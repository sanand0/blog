---
title: Things I Learned - 12 Jul 2026
date: 2026-07-12T00:00:00+00:00
categories:
- til
description: This week's notes cover applied AI engineering, why AI-generated commit messages feel less helpful, a subtle Cloudflare race bug, and smart TVs quietly serving data-collection networks.
tags: [llms, business-models, claude-code, ai-agents]
---

This week, I learned:

- [How to become an applied AI engineer](https://x.com/eyad_khrais/article/2074519552277336571) is a concise, well-written, and suprisingly current summary of what AI engineering is.
- [Xinjiang](https://en.wikipedia.org/wiki/Xinjiang_conflict) seems to be China's Kashmir problem. [Not quite](https://share.gemini.google/cDYpzSmjOlJ6), but similar. <!-- https://gemini.google.com/app/8b3dd829d3bbde14 -->
- Analogies for how forward deployed engineers work:
  - It is like a **food truck** that brings and serves home food while building a kitchen and restaurant around it. <!-- https://gemini.google.com/app/a1bead8f1509f60c -->
  - It is like setting up a **field hospital**: patients are treated from day one, while the equipment and procedures are built around the live work. <!-- https://chatgpt.com/c/6a509e35-0748-83ec-8811-b33a4f5c959c -->
- Froghoppers excrete ~300x their weight daily. [ChatGPT](https://chatgpt.com/share/6a4fc46b-17a0-83ec-861f-f0fa22f16d36) <!-- https://chatgpt.com/c/6a4f21e2-89fc-83ec-aa65-72913400ac2c -->
- There's a growing shift away from AI-written commit messages, e.g. [Kenton Varda](https://x.com/kentonvarda/status/2074924213983740233). I compared my [human written](https://github.com/sanand0/tools/commits/main) [commit messages](https://github.com/sanand0/talks/commits/80d42a4) vs [AI-generated](https://github.com/sanand0/blog/commits/0717cde) [commit messages](https://github.com/sanand0/til/commits/2e73dd9) and the AI-generated ones are less helpful.
- Finally, [GPT live](https://openai.com/index/introducing-gpt-live/) gets an update and the new speaking model can delegate to GPT 5.5 when required. I tried it once today, to plan for a teacher workshop, and it was fairly good. It tends to begin with "Hmm" like it's thinking, which feels comforting. <!-- https://chatgpt.com/c/7695d193-8464-4c92-80ad-ffc3fe9d0d8d -->
- Using a Unicode character like `🟢` is unusually low-risk across file systems today. It works well across OSs, mobile, ZIP, attachments, file share systems, etc. Some old apps might have trouble, but for storing and sharing, it's fine. I've been using Unicode symbols like these a lot in my notes, and extending to file names feels like a natural next step. <!-- https://chatgpt.com/c/6a4ddcfb-3c54-83ec-be17-30659786de9f -->
- Though swimming gets the most Olympic medals (11%), for a country chasing its first medals, 78% of first-medal breakthroughs came from Athletics, Wrestling, Shooting, Boxing, Judo, Weightlifting, or Taekwondo (which are 44% of medals) - where single athletes can win without a support ecosystem. [ChatGPT](https://chatgpt.com/share/6a4ddbd0-026c-83ec-b268-50c8a40925aa) <!-- https://chatgpt.com/c/6a2e276a-949c-83ec-96b1-085284eaa484 -->
- JMFL accidentally emailed several people a letter intended for their brokers. It roughly said: "Many of you are recording client calls. That's a regulatory risk. If you keep doing this, we'll hold your payments, even fire you."
- Several Smart TVs have software that let your TVs act as proxies for data collection companies. [Include Security](https://blog.includesecurity.com/2026/06/the-smart-tv-in-your-livingroom-is-a-node-in-the-aiscraping-economy/)
- [MapDraw](https://www.mapdraw.net/) is a convenient tool to annotate maps (e.g. routes, boundaries, places) and share or download it.
- There seems to be no way to edit the "About" message on WhatsApp Web. Though the [help](https://faq.whatsapp.com/859240711908360/?cms_platform=web) suggests steps, and the "About" mood/status _is_ visible, there's no way to edit it. (Editing on the phone works.)
- Cloudflare optimised a reader component by sometimes letting the input buffer fill fully. This inadvertently introduced a hard to reproduce race bug because the producer would close the socket if the buffer was full. The producer bug was old (it didn't check if a flush succeeded or not) but was never visible since the readers never let the buffer fill in the past. [Cloudflare](https://blog.cloudflare.com/hyper-bug/)
- A **neofirm** is a start-from-scratch AI-native business, e.g. Crosby's AI-first law firm. An **AI rollup** is where a company buys small traditional firms and AI-enables them - like [General Catalyst proposed](https://www.generalcatalyst.com/stories/europes-ai-transformation-in-services). **AI SaaS** is selling AI agents to services firms.
- Give people free platforms and collect their data. Learn the supply-demand network patterns, what pepole value, and add value-added services.
- Claude Code checks if you're working behind a Chinese corporate domain - somewhat sneakily - by changing an apostrophe or slash in the date to visually similar Unicode. [Claude Code Is Steganographically Marking Requests](https://thereallo.dev/blog/claude-code-prompt-steganography)
- You can use the [Kaggle CLI](https://github.com/Kaggle/kaggle-cli) via Codex to solve Kaggle problems. ([AutoKaggle](https://github.com/multimodal-art-projection/AutoKaggle) automates it - but is 2 years old.) But, like [GitHub bounty hunting bots](https://www.s-anand.net/blog/bounty-hunting-agent-ecosystem/), we will probably have a Kaggle bounty-hunting bot ecosystem - maybe already do.
- [OpenSubtitles2024](https://huggingface.co/datasets/Helsinki-NLP/OpenSubtitles2024) and [subscene](https://huggingface.co/datasets/refine-ai/subscene) are large pre-AI subtitle datasets with a 2024 cutoff. [IndicDialogue](https://data.mendeley.com/datasets/wcb4bxbyxx) is a 7.7K OpenSubtitles snapshot of Indic language SRTs. The [OpenSubtitles API](https://opensubtitles.stoplight.io/docs/opensubtitles-api/a172317bd5ccc-search-for-subtitles) lets you search by IMDb/TMDb ID and is up-to-date. <!-- https://chatgpt.com/c/6a48ca99-4e9c-83ec-bcb4-677478cc80f6 -->
- A soup spoon is better than a table spoon (for soup), though both carry about the same volume, because you can fit a soup spoon it fully into your mouth (a table spoon is too long) and this reduces spilling.
- Here's a sign of accelerating AI progress. I used to critique outdated techniques by saying "This feels like a 20th century approach." Then "This feels like a 2010s solution." Recently, "This is SO 2025-ish." Now, "That's Q1 2026. It's Q2."
- The 7-day week emerged from the Hellenistic planetary week and the Jewish week (not astronomy based), which Rome adopted, then spread by several routes to India, China, and worldwide. Unlike the astronomical year and month, the week is just a convention. Egypt, China, and Athens grouped days in tens; Etruria and Rome used 8-day market cycles; West Africa used varied cycles; Java used five days; Mesoamerica used 13- and 20-day cycles. [Gemini](https://share.gemini.google/DPWeYqx3RIGn) <!-- https://gemini.google.com/app/9223b933d8e12403 + https://chatgpt.com/c/6a4a35f3-0904-83ec-b9de-1855ae57c2bd -->
- I met an ex-photographer and learned that photography is another profession where technology (mobile cameras) squeezed the middle. Generation (taking good pictures) became cheap. Value moved upstream (direction), downstream (selection, editing, album design), and into niches (forensic, industrial, sport/event photography). <!-- https://chatgpt.com/c/6a48f8b1-8c80-83ec-b42e-8b9bfae9b194 -->
- Looks like Claude favors Claude Code. Might not be intentional, and just a result of training more on Claude Code data, but it does look like a network effect that could weaken open harnesses. [Armin Rocher](https://lucumr.pocoo.org/2026/7/4/better-models-worse-tools/)

## Questions I was asked

[Week ending 12 Jul 2026](https://www.s-anand.net/blog/questions-i-am-asked/#week-ending-2026-07-12)

- **Question**: How should we handle data quality in research (especially when using AI for research)?\
  **Answer**: Start with a human sanity filter: fix bad source data or kill the idea. Then use LLM-as-a-judge to scale. Where accuracy matters a lot, simulate them in a verifiable environment.
- **Question**: What effort is needed to train the model on our branding guidelines?\
  **Answer**: Don't train it. Generate the content separately, then apply branding deterministically through code or templates; non-deterministic models should not own brand compliance.
- **Question**: How should I explain what these five reusable AI asset types do in an engagement?\
  **Answer**: Plan, Connect, Do, Verify, Log. Domain context plans; connectors and tools connect; skills, hooks, and agents do; golden datasets and benchmarks verify; telemetry and observability log so the system improves.
- **Question**: How do real reusable AI assets get manufactured from past project work?\
  **Answer**: Let agents mine the actual exhaust—code, transcripts, Jira, design artifacts, standards, and contracts—into small reusable files that explain domain context, schemas, gotchas, and playbooks without being client-specific. Future agents should consume those assets.
- **Question**: Before ingesting and chunking 30,000 documents, what should we try?\
  **Answer**: Start minimally: point Claude Code at the folder and ask the real question. Benchmark that direct baseline before building indexing or RAG.
- **Question**: When context evolves, how do I make the agent treat the latest version as the truth?\
  **Answer**: Prepend updates; don’t append them. Put the latest truth first and preserve dated history below, because agents and tools often inspect the head of a file before the tail.
- **Question**: Can AI help a teacher understand 160 students individually?\
  **Answer**: Yes. It may not know 40 students better than an attentive teacher, but it can remember and personalize for 160, 1,000, or 100,000; use it where human memory stops scaling.
- **Question**: Can AI release teachers from correcting answer sheets so they can spend more time on creative teaching?\
  **Answer**: Not automatically. If correction takes half the time, teachers may simply give twice as many tests; unless we deliberately reallocate the gain, productivity becomes more work rather than better teaching.
- **Question**: Can AI replace a counselor’s personal touch?\
  **Answer**: No, not when a trusted counselor is available. Use it like a teddy bear—one more source of support when the human is unavailable, while learning the risks of dependence.
- **Question**: How safe is it to put sensitive data into ChatGPT or Claude?\
  **Answer**: Use the same trust boundary as cloud storage. If I would put it in Google Drive, Dropbox, or OneDrive, I may put it into a frontier AI service; if not, I won’t.
- **Question**: Can I upload an answer key and student answer sheets and have AI evaluate them?\
  **Answer**: Yes. Let it grade in parallel with you, compare disagreements, and expand delegation only where it proves reliable; do not delegate judgment before you have built confidence.
- **Question**: How should we prioritize which AI skills to build?\
  **Answer**: Prioritize skills that face customers, solve a common problem, and compound—something reusable that accelerates future work or becomes IP. Don’t assetize every clever prompt.
- **Question**: If a skill already has its own rubric, why evaluate it separately?\
  **Answer**: The author and evaluator should not be the same system. Treat the skill’s rubric as internal control and a separate evaluator as external audit; keep a human on revisions so it does not overfit one test set.
- **Question**: How should we choose an AI use case and rubric for a competition?\
  **Answer**: Pick a use case with objective ground truth, synthetic data you can generate, and hidden cases that separate a demo from a working system. Use a tiered rubric: happy path, hidden exceptions, then traceability to evidence.
- **Question**: Are we doing premature optimization by benchmarking quality, speed, and cost on manufactured generic data?\
  **Answer**: Yes, if we treat the result as universal. Re-run the benchmark on the actual domain, corpus, task, and technique; general rules are a bonus, not a substitute for local evidence.
- **Question**: If AI produces a plausible result quickly, when should we share it?\
  **Answer**: Generation is cheap; socialization is the risky part. Share low-stakes findings quickly, but hold revenue, forecasting, or other consequential claims until the right owner verifies them.
- **Question**: Is AI research just regurgitating what is already on the internet?\
  **Answer**: Often, yes—and that is still useful for breadth. Where I am an expert, ask it what I missed; where I am not, use it to generate candidates and benchmark before trusting them.
- **Question**: Should every agent output be forced into a strict schema?\
  **Answer**: For intermediate outputs consumed by machines, usually yes. For the final human-facing answer, allow flexibility—or add a final conversion layer.
- **Question**: How can I verify agent work when I do not know the domain well enough to judge it?\
  **Answer**: Manage agents like a hiring panel: have several propose benchmarks, have others attack them, and use deterministic checks where possible. Curate the test and escalate uncertainty rather than pretending to be the domain expert.
- **Question**: What useful open-source problem should AI developers build next?\
  **Answer**: Build observability that reads agent logs, finds failure patterns, and turns them into better prompts, tools, and harnesses. Self-improvement needs execution evidence, not reflection alone.
- **Question**: What should an organization prioritize before investing in AI tools or models?\
  **Answer**: Don’t begin with an AI strategy. Begin with experiments on real workflows, accept failures, compare multiple approaches, and scale only what produces evidence.
- **Question**: How much verification should an AI workflow have?\
  **Answer**: Match it to risk and repetition. Low-stakes one-offs need little; high-stakes one-offs need human review; repeated tasks need automated judges, with disagreements escalated to a human.
- **Question**: Why does AI sound generic, verbose, and unlike me?\
  **Answer**: Because you hired a brilliant post-doc and spent zero minutes onboarding it. Give it your context, examples, style, and feedback; don’t expect personalization without training the workflow.
- **Question**: Why is content and knowledge infrastructure critical for enterprise AI?\
  **Answer**: Models cannot compensate for fragmented, stale, or inaccessible source systems. Fix access, provenance, and freshness; otherwise AI will fail like a human or hallucinate.
- **Question**: How do we prove our AI methodology and platform are real rather than marketing?\
  **Answer**: Show a coverage matrix across actual engagements, assets, and reuse, with clickable evidence from code, logs, and transcripts. Platform claims need usage numbers and visible gaps, not architecture slides.
- **Question**: Can we standardize on one coding agent across the enterprise?\
  **Answer**: Internally, mostly; across clients, no. Client environments dictate the allowed model and tools, so standardize the workflow and reusable assets, not the vendor.
