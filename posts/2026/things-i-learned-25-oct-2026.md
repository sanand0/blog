---
title: Things I Learned - 25 Oct 2026
date: 2026-10-25T00:00:00+00:00
categories:
  - til
description: I learned how LLM neurons and activations work, why tools are becoming more agent-friendly, and how standardization can enable personalization. I also corrected several AI-related mistakes and answered questions about agents, models, and workshops.
tags: [llms, llm-behavior, ai-agents, open-source]
---

This week, I learned:

- [Neural Networks Are Already Clean](https://already-clean.goodfire.com/) argues that in modern LLMs, most neurons have one function, not arbitrary overlapping functions (like we thought earlier). This becomes clearer when you see the learning steps, e.g. the "iy" neuron -> "diy" -> "do it yourself". Without the "diy" in the middle, it's confusing what "iy" has to do with "do it yourself". Models probably learn by generalizing concepts repeatedly. Interpreting models has the bitter lesson, too: just tell a powerful agent to interpret it.
- Modern LLMs have switched from [ReLU](https://en.wikipedia.org/wiki/Rectified_linear_unit) to [SwiGLU](https://github.com/raiyanyahya/how-to-train-your-gpt/blob/master/explanations%20and%20examples%20WIP/swiglu.md). Why? ReLU is on-off and communicates no information when off. SwiGLU is a smooth function that whispers less relevant information - and that gives smarter models more context.
- Gemini 3.8 Flash is SLIGHTLY cheaper than Gemini 3 Flash Preview when transcribing 1 min of audio - #ForNow until Dec 31. After that, a higher pricing kicks in. [ChatGPT](https://chatgpt.com/share/6ad9ad5f-77a4-83ec-9c68-93e6d9c5d09d)
- ArtCraft extended their [open source tools](https://github.com/orgs/storytold/repositories?q=sort%3Astars) to cover MS Office, Adobe, and Autodesk #ForNow. Others are following suite. The [Remade Wiki](https://remade.wiki/) has includes OneNote, QuickBooks, Power BI, Outlook, MS Project, Visio, Discord, Jira, Linear, Monday, Corel, ... #ForNow
- [Cloudflare ported the TypeScript compiler to Rust](https://blog.cloudflare.com/typescript-rust-port/). Increasingly, language choice is becoming fluid.
- [Tiny Little Office](https://tinylittleoffice.com/) uses a number of [interesting tricks](https://chatgpt.com/share/6ad6f3ad-dbc4-83ec-9a0e-77b1d7194dfc): <!-- https://chatgpt.com/c/6ad6dc01-57f8-83ec-8a64-ead2f63b0ee7 -->
  - The _entire_ document is in the URL fragment, which is as much as 2 MB for Chrome!
  - That means the _entire_ document can be shared as a single QR code (if it's not too large).
  - Docs, spreadsheets, presentations, diagrams are _all_ [Markdown-based](https://github.com/aboard-io/tinylittleoffice/blob/main/docs/tlo.md) #ForNow and [agent-friendly](https://github.com/aboard-io/tinylittleoffice/blob/main/packages/doc/README.md). They can be embedded as code fences inside each other.
  - It uses [domain-specific compression](https://github.com/aboard-io/tinylittleoffice/blob/main/src/kit/core/codec.ts) tailored to its language. It also uses `~` instead of `-` for base64 - to avoid wrapping issues with mail clients.
  - It uses [directives for agents](https://github.com/aboard-io/tinylittleoffice/blob/main/docs/history/directives/README.md). The way it is organized is interesting!
- `document.currentScript.replaceWith(...)` can be used as a nifty way to dynamically replace content, effectively creating a mini-templating language. Via [Simon Willison](https://simonwillison.net/2026/Oct/17/document-currentscript/).
- Standardization and personalization are independent axis. In fact, standardization can make personalization easier. [ChatGPT](https://chatgpt.com/c/6ad0b90f-ade0-83ec-a872-674d38307bdc)
- Before the printing press, people used to spell words differently. Shakespeare, for example, had different spellings of his name. With the printing press and distribution of publication, spelling became standardized. But interestingly, it standardized by freezing the current conventions. So some oddities of the spellings people used are now a formal part of the language definition.
- In pharmacies, we call them "compounders" because they actually used to compound, i.e. mix, medicines - personalizing them to each individual. That faded away as standardized tablets became more common.
- Fonts are becoming more sophisticated. [Some features in newer fonts are](https://chatgpt.com/share/6ad492e2-8fb4-83ec-8e55-eab31a60d6b1): <!-- https://chatgpt.com/c/6ad468b8-3048-83ec-bf41-5795d9499337 -->
  - Icons: [NerdFonts](https://www.nerdfonts.com/) is an example of a font class with 10K+ icons embedded - like 󰊢 GitHub, 󰈙 files, or 󰀨 terminals.
  - Opt-in Ligatures: Display multiple characters as one symbol, e.g. => as ⇒, != as ≠, or >= as ≥, letting users pick what to enable.
  - Variable weight: Continuously adjust thickness, e.g. weight 450 or 575 instead of being limited to Regular (400) and Bold (700).
  - Smart width: Make characters narrower or wider, adjust shapes based on neighbors (making `mi` look more evenly spaced), etc. while preserving mono-space.
- "No one cares more about your case than you, so take control and send lots of follow-ups." [Things to know if you get cancer](https://jjmaxwell4.com/writing/things-to-know-when-you-get-cancer/#:~:text=No%20one%20cares%20more%20about%20your%20case%20than%20you%2C%20so%20take%20control%20and%20send%20lots%20of%20follow%2Dups.). The article has usefuls tips for important things in life, in general - not just cancer. Agents are making this easier.
- Because Amazon has a fair pricing policy, a strange consequence is that if Amazon sellers raise prices on Amazon they're pressured to raise prices elsewhere too! So, increasing Amazon seller fees tends to increase prices across the board. [How Amazon pushes up pricess all across the Internet](https://www.not-ship.com/how-amazon-pushes-up-prices-all-across-the-internet/)
- Will Jev destroy its servers to save 5 lives? Will other models? A lovely set of experiments based on the [trolley problem](https://zachlandes.com/trolley-problem/).

## Mistakes I made

[Week ending 25 Oct 2026](https://www.s-anand.net/blog/mistakes-i-made/#week-ending-2026-10-25)

- I said **"prospectively, there is only one thing ... set caps for each person"** while explaining how enterprises can control LLM spending.\
  **Correction**: User spending caps are one preventive cost control, not the only one. Organizations can proactively reduce spending using model selection and routing, prompt caching, shorter context, output-token limits, request budgets, rate limits, and lower-cost batch processing. Several of these controls reduce costs before requests execute, rather than merely identifying overspending afterward. [OpenAI: Cost optimization](https://developers.openai.com/api/docs/guides/cost-optimization) · [OpenAI: Prompt caching](https://developers.openai.com/api/docs/guides/prompt-caching)\
  **MEDIUM · FALSE**
- I said **"after founding Gramener in 2012"** while recounting the company's history.\
  **Correction**: Gramener identifies 2010 as its founding year, not 2012. Its official company profile and an article reproduced on its own blog in August 2012 both give 2010. 2012 is when I joined Gramener full-time. [Gramener company profile](https://www.linkedin.com/company/gramener) · [Gramener blog, August 2012](https://blog.gramener.com/gramener-lets-you-see-the-big-picture-from-the-big-data/)\
  **LOW · FALSE**
- I said **"co-founded in 2011"** while introducing my previous company.\
  **Correction**: Gramener dates its founding to 2010. I should consistently use 2010 when describing the company's founding, distinguishing that date from subsequent product development or business milestones. [Gramener company profile](https://www.linkedin.com/company/gramener) · [Contemporaneous article on Gramener's blog](https://blog.gramener.com/gramener-lets-you-see-the-big-picture-from-the-big-data/)\
  **LOW · FALSE**
- I said **"one-quarter of incoming pull requests now dismissed as useless AI slop"** in an AI-news digest about open-source development.\
  **Correction**: In a Linux Foundation survey published on 20 October 2026, maintainers estimated that approximately 25% of incoming pull requests were low-quality AI-generated contributions. The study did not establish that 25% were actually rejected or dismissed, nor was the percentage measured directly across all open-source repositories. [Linux Foundation research announcement](https://www.linuxfoundation.org/press/new-lf-research-survey-shows-generative-ai-cuts-open-source-coding-time-in-half-but-25-of-incoming-pull-requests-are-considered-ai-slop)\
  **MEDIUM · OVERSTATED**
- I said **"72 percent reduction in cost at 99 percent quality"** while explaining a five-model verification workflow.\
  **Correction**: The pilot reported 28% of items requiring human review and 0.7% error among automatically accepted, unanimous model predictions. This corresponds to a 72% reduction in the number of items requiring manual review, not an established 72% reduction in total operating cost. Actual savings also depend on model inference, human-review time, integration, exceptions and rework. The 99.3% accuracy figure applies to automatically accepted predictions in the evaluated sample, not automatically to all future cases or the entire end-to-end workflow.\
  **HIGH · OVERSTATED**
- I said **"the sub-agent does not get to see the entire picture"** while explaining why Copilot subagents make better independent reviewers.\
  **Correction**: Microsoft Copilot Studio child agents always receive their parent's conversation context. Connected agents have a setting called "Pass conversation history to this agent", which is enabled by default and must be disabled when context isolation is required. Creating a subagent does not automatically provide an independent or blinded review. I should configure context boundaries explicitly and check whether the reviewer has been exposed to the expected answer. [Microsoft: Design subagents that avoid duplicate messages](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/generative-orchestration-subagents)\
  **MEDIUM · FALSE**
- I said **"967 papers had authors who said they were not paid, but actually were"** while circulating results from an automated research-disclosure screening demonstration.\
  **Correction**: The system flagged 967 potential discrepancies between publication disclosures and external payment records. These are candidates for investigation, not 967 verified cases of undisclosed payments. Establishing a genuine discrepancy requires confirming author identity, payment dates, disclosure scope and reporting requirements through human review. CMS explicitly warns that its payment database does not itself determine conflicts of interest. [CMS Open Payments](https://www.cms.gov/priorities/key-initiatives/open-payments) · [ICMJE disclosure requirements](https://icmje.org/recommendations/browse/roles-and-responsibilities/author-responsibilities--conflicts-of-interest.html)\
  **HIGH · OVERSTATED**
- I said **"every chat will be able to see past chats"** while explaining Microsoft Copilot's Chat history and work insights setting in a training workshop.\
  **Correction**: With this setting enabled, Microsoft Copilot can use selected memories and inferred information from prior conversations and, where licensed, work content. It does not provide every new conversation with complete access to every previous chat. Microsoft explicitly states that Copilot remembers useful details rather than every detail. Temporary chat is an additional option for conducting isolated experiments. [Microsoft: How Copilot Chat history works](https://support.microsoft.com/en-us/microsoft-365-copilot/how-microsoft-365-copilot-chat-history-works) · [Microsoft: Copilot personalization](https://support.microsoft.com/en-us/microsoft-365-copilot/personalize-what-microsoft-365-copilot-remembers)\
  **MEDIUM · OVERSTATED**
- I said **"the GPT models just don't make any [spelling] mistakes"** while recommending how to assess image-generation quality.\
  **Correction**: GPT image-generation models have improved substantially at rendering text, but spelling, precise text placement, typography and visual clarity can still fail. Text accuracy is one useful evaluation dimension, not proof that an image model is generally reliable. I should evaluate text rendering separately from composition, instruction following, consistency and visual quality. [OpenAI: Image generation limitations](https://developers.openai.com/api/docs/guides/image-generation)\
  **MEDIUM · OVERSTATED**
- I said **"the server could identify me correctly even in Incognito mode"** while discussing browser fingerprinting and an unusually distinctive result from EFF's Cover Your Tracks.\
  **Correction**: Cover Your Tracks measures how distinctive a browser configuration is relative to configurations previously observed. A unique fingerprint can make cross-session tracking possible, including in private browsing, but uniqueness alone does not prove that a server recognized my identity or linked two particular sessions. That requires a separate re-identification experiment. [EFF: How Cover Your Tracks works](https://coveryourtracks.eff.org/about)\
  **MEDIUM · UNSUPPORTED**
- I said **"where the AI itself has found a flaw ... you can safely reject"** while demonstrating automated policy verification for regulated business processes.\
  **Correction**: An AI-identified policy violation is a reason to flag or investigate an item, not automatically sufficient grounds for rejecting it. AI-generated rules may omit exceptions, misinterpret obligations or incorrectly classify evidence. Automatic rejection is appropriate only where the applicable policy has been correctly formalized, the required facts are independently validated, and the decision process has been tested to an acceptable error threshold with suitable oversight. Otherwise, potential violations require authorized human review. [FCA: AI in financial services, good practice and areas for improvement](https://www.fca.org.uk/publications/good-poor-practice/ai-financial-services)\
  **HIGH · OVERSTATED**

## Questions I was asked

[Week ending 25 Oct 2026](https://www.s-anand.net/blog/questions-i-am-asked/#week-ending-2026-10-25)

- **Question**: How should we think about AI agent swarms becoming more intelligent? Asked while comparing self-organizing swarms with multithreaded programs and shared message boards.\
  **Answer**: Think civilizations, not process threads. A model is an interaction; an agent is more like a long-lived person; a swarm can create and shut down its own agents, branch, and evolve. We may see centuries of civilization-like change compressed into days. That makes specifying what we want and preventing things going overboard much harder.
- **Question**: What's your biggest finding about using different LLMs effectively? Asked after discussing LLM psychology and how to change his own prompting and coding practices.\
  **Answer**: Treat every model as a completely new species. Maintain a few personal benchmarks for things you care about and can judge immediately. Mine include colorizing an old family photograph, where I can spot the smallest facial change. Test new models on those instead of trusting generic rankings.
- **Question**: Why do you call yourself an LLM Psychologist? Asked after demonstrating his Claude-and-Gemini coding workflow and seeking a useful insight from the interview.\
  **Answer**: I run human psychology tests on models. Does telling them to write simply make them think less effectively? Does threatening them improve their answers? Usually it makes them worse. Different models behave differently, so I study their behavior rather than treating them as ordinary deterministic software.
- **Question**: How should I share our innovation demos with prospective clients? Asked after drafting an outreach email containing a long, categorized list of AI demonstrations.\
  **Answer**: One demo is more powerful than five. If you send me lots of links, I'll open none; one interesting image might make me click. Add one sentence explaining how it helps that particular client. Ask Gemini or another model to personalize the message rather than forwarding a catalog.
- **Question**: Apart from prompt engineering, how can we influence the decisions an LLM makes? Asked after discussing behavioral experiments and why models sometimes make unexpected choices.\
  **Answer**: We increasingly work with systems using models, not models directly. Change the tools available, permissions, inputs, data sources, outputs, and the loop in which the model runs. Changing what the agent can touch changes what it can do and how it decides.
- **Question**: When should we start using sub-agents? Asked after a participant described independently validating agent outputs but lacked permission to create orchestration agents.\
  **Answer**: Rarely. Use them when work benefits from independent parallel execution or preserving context—especially brainstorming and verification. Parallel brainstorming avoids later ideas being influenced by earlier ones; an independent verifier is less contaminated by the expected answer. If you can't create sub-agents, ask for their prompts, execute those manually, and return the results.
- **Question**: How should we structure the final session of a hands-on AI agent workshop? Asked after two Copilot sessions where participants had built agents but were reluctant to share their difficulties openly.\
  **Answer**: Optimize what people have actually built. Ask just two questions beforehand: what agent have you built, and what isn't working? Even three or four responses are enough to spot patterns and create live exercises. No need to predesign everything. Then show more advanced possibilities, including agents creating other agents.
- **Question**: When should I stop trying to make AI complete a task and switch to doing it manually? Asked after describing research sessions that kept wandering without producing the required answer.\
  **Answer**: I don't have a universal stopping rule. Every time you feel like stopping an agent, log it—whether you stopped or carried on. Collect ten such cases and review whether each decision was right. Use your own evidence to discover your stopping rule, rather than borrowing somebody else's.
