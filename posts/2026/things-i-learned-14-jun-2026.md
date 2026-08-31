---
title: Things I Learned - 14 Jun 2026
date: 2026-06-14T00:00:00+00:00
categories:
- til
description: This week I learned that rdt-cli can use logged-in browser cookies, Claude and ChatGPT subscriptions bundle substantial API value, codon wobble limits errors, and ChatGPT offers work-in-progress answers.
tags: [cli-tools, llm-pricing, information-theory, chatgpt]
---

This week, I learned:

- Overheard a journalist saying: "I can tell when humans are lying. There are no tell tale signs of AI lying. At least _I_ don't have any."
- [rdt-cli](https://github.com/public-clis/rdt-cli) is a Reddit CLI. It uses a clever trick: it auto-detects installed browsers and extracts cookies (supports Chrome, Firefox, Edge, Brave). So, if you're logged into Reddit on any browser, `uvx --from rdt-cli rdt whoami` automatically shows who you are logged in as. (The [public-clis](https://github.com/public-clis/public-clis) repo also lists other useful CLIs like [twitter-cli](https://github.com/public-clis/twitter-cli), )
- Currently, a $20 Claude Pro gives you ~$400 and a $100 Claude Max gives you ~$2,000 of API usage. For ChatGPT, the numbers are ~$700 and $3,500. [SemiAnalysis](https://x.com/SemiAnalysis_/status/2064815044085318040)
- When Fable 5 refuses to answer questions, here's the message that appears: "Fable 5 has safety measures that flag messages on most cybersecurity or biology topics. They may flag safe, normal content as well. These measures let us bring you Mythos-level capability in other areas sooner, and we're working to refine them. Send feedback or [learn more](https://support.claude.com/en/articles/15363606)." I managed to trigger this once while researching an M&A acquisition target. Clicking on "Edit and retry with Fable 5" triggered Opus 5 again, twice.
- DNA codons (A, T, C, G) encode proteins in triplets. There are [64 triplets that map to 20 amino acids](https://en.wikipedia.org/wiki/DNA_and_RNA_codon_tables). Some like Leucine, have 6 codons. Some like Methionine have only one. Why? When creating genes, there's a wobble, sometimes, at the 3rd codon. THe mapping minimizes that impact: small errors map to similar proteins. The more common proteins have more codons. There's a lot of fascinating information science going on here. [Gemini](https://gemini.google.com/share/cfa70dcab30c)
- ChatGPT now shows a "Check in" button when it's thinking. Clicking on that gives you a work-in-progress answer while it continues thinking. When done, it _replaces_ the WIP answer with the final answer. A useful feature!

## Questions I was asked

[Week ending 14 Jun 2026](https://www.s-anand.net/blog/questions-i-am-asked/#week-ending-2026-06-14)

- **Question**: How should we verify that an AI/download tool captured all files?\
  **Answer**: Use another chat as an independent checker and ask “what is missing?” Don’t ask “does it match?” because that invites lazy confirmation.
- **Question**: What prompt helps convert data into a shareable dashboard?\
  **Answer**: Ask for a single-page HTML file. It gives you something portable, inspectable, and easy to email or publish.
- **Question**: How should audience feedback be used in AI-generated data stories?\
  **Answer**: Dump the feedback back into the model. Since generation and verification are cheap, the scarce skill shifts to collecting, interpreting, and iterating on feedback.
- **Question**: How do we stop AI data-story sessions from becoming repetitive loops?\
  **Answer**: Start a new chat, switch model or provider, or meta-prompt: give the failed conversation to AI and ask it how to make the next prompt more novel.
- **Question**: If AI keeps refining answers, do humans stop learning?\
  **Answer**: The new skill is steering smarter intelligences. Editors, judges, auditors, teachers, and coaches already guide work they cannot fully reproduce.
- **Question**: When should humans verify AI analysis?\
  **Answer**: Treat AI like a fresh journalist. Check heavily at first, stratify by risk, build confidence, delegate some verification, and periodically test for regression.
- **Question**: Is a paid AI subscription worth it for occasional users?\
  **Answer**: Buy Plus for one month and use it hard. If it is paisa vasool, continue; if not, cancel and retry in six months because the frontier moves fast.
- **Question**: How do Chinese LLMs compare with frontier models?\
  **Answer**: Use them when cost matters at scale. They are good and cheap, but frontier models still lead; default to frontier unless economics force optimization.
- **Question**: What can AI add to geospatial storytelling?\
  **Answer**: It can scan satellite grids for change and surface story leads. But indices create false positives, so visual inspection and narrative judgment still matter.
- **Question**: After AI identifies bottlenecks and recommended actions, what is missing before sending it to leadership?\
  **Answer**: Add monetizable business benefit, estimated impact, and evidence for that impact. Process benefit is your problem; business benefit is what buys attention.
- **Question**: Which coding agent should we recommend when a fresh client has no preference?\
  **Answer**: Default to the client’s cloud provider: Gemini for Google, GitHub Copilot for Microsoft, OpenAI or Anthropic if they already prefer them.
- **Question**: What should students do when ATS filters reject qualified resumes?\
  **Answer**: Hack the system and publish the hack. ATS is another machine-mediated system; learn how it fails and use that knowledge.
- **Question**: How should agents organize unstructured folders for repeated future questions?\
  **Answer**: Tell the agent many questions are coming and ask it to design the organization: summaries, entities, intents, tags, and evidence. Let the semantic layer emerge from usage.
- **Question**: When does a knowledge graph make sense for enterprise documents?\
  **Answer**: When relationships matter: clauses, asset classes, customer segments, obligations, exceptions. The graph captures institutional checklists that humans otherwise carry in their heads.
- **Question**: How should we calm leaders who think data must be fully cleaned before agents can use it?\
  **Answer**: Tell them it may not be as hard as they think. Let agents try inside their system; the downside is small and the learning is immediate.
- **Question**: How should an AI/data-viz dialogue be structured so it stays participatory?\
  **Answer**: Plan the mechanics, takeaways, and sequence, but order everything by droppability. Use audience volunteers and leave room for improvisation.
- **Question**: How should we choose charts for an AI-vs-human visualization exercise?\
  **Answer**: Use embeddings or UMAP to pick a diverse set, then create paired AI-generated alternatives. Don’t pick naïvely; use the corpus to sample the space.
- **Question**: Is the real question whether people can detect AI charts?\
  **Answer**: No. The first question is what makes a chart good. The AI reveal is secondary: does knowing the source change how people judge quality?
- **Question**: What is the right unit for comparing AI and human visualization work?\
  **Answer**: Data visualization, not chart mechanics. The hard parts are topic selection, insight choice, framing, and presentation, not whether D3 was written by hand.
- **Question**: What is the practical skill people need as AI makes more charts?\
  **Answer**: Curation. People need explicit, communicable judgment about what is useful, truthful, beautiful, and worth publishing, whether the maker is human or AI.
- **Question**: How should educators deal with students copy-pasting into ChatGPT?\
  **Answer**: Don’t teach what ChatGPT can already do. Teach what it cannot do, then evaluate both foundational understanding and AI-enabled execution.
- **Question**: How should we test whether AI can help with patient-specific implants and CAD?\
  **Answer**: Don’t start with the full clinical workflow. Give AI a basic tool task: create a mesh, create a fitting patch, get feedback, then iterate.
- **Question**: How should we use AI for hard research problems like moving-boundary FEM?\
  **Answer**: Don’t ask it for the final answer. Ask it to ideate, mock the physics, test multiple approaches, show evidence, and make the researcher smarter.
- **Question**: How should we evaluate students in an AI-enabled course?\
  **Answer**: Simulate industry: give 10x workload, allow AI and collaboration, grade outcomes, and remove questions once the batch collectively learns the pattern.
- **Question**: How should an AI services startup think about pricing when software is depreciating?\
  **Answer**: Discount the commodity extraction and charge for verification and value-add. Find the money leaks from the first batch, then price against savings or outcome.
- **Question**: Are demos now the right way to pitch?\
  **Answer**: Yes, if the demo solves their specific domain problem with their data or public data. Generic code demos impress the middle; evidence-backed recommendations impress sophisticated buyers.
- **Question**: What does productionization look like when the coding agent is the production software?\
  **Answer**: Productionization becomes delivering real paid output through a process, not deploying an app. SME plus coding agent plus review loop can itself be the production system.
- **Question**: Doesn’t TDD work better for production software?\
  **Answer**: Yes, if you’re delivering software. But if you’re delivering the output software would produce, test the output and system benchmarks, not just the code.
- **Question**: For an IDP platform, what should delivery look like if not software handover?\
  **Answer**: Sell the extracted XML, JSON, or results from day one with human-on-the-loop review. Zero CAPEX, zero lead time, lower TCO.
- **Question**: How should we judge hallucinating models?\
  **Answer**: Compare them to people, not perfect machines. Subject matter experts disagree and err too; if a pocket PhD hallucinates, the question is what it enables with review.
- **Question**: If humans ask us to ask ChatGPT for them, is that valuable?\
  **Answer**: Yes. You are not just entering the prompt; you are the evaluator and filter. “Human as interface” may be monetizable when trust and judgment are scarce.
- **Question**: How should we use non-frontier or local models?\
  **Answer**: Use a task checklist of what models currently cannot do. Benchmark model-task fit, not generic intelligence; local models may be good enough for narrow extraction or graph work.
- **Question**: How do we convert a personal Co-work audit checklist into firm-wide agents?\
  **Answer**: Export the best representative conversations with inputs, outputs, and prompts. From those, create reusable agents for financial-statement review, audit-report checks, and other audit workflows.
- **Question**: How should we respond when a client worries our custom AI solution is not SaaS and will be hard to maintain?\
  **Answer**: Don’t defend point-by-point. Say they’re right, revise the positioning, and offer Solution-as-a-Service: the outcome and maintenance headache are ours.
- **Question**: What is the expected FDE output format?\
  **Answer**: An email to a real person: “Please do this because of this reason, and here is the evidence.” One use case is fine; many solved use cases are better.
- **Question**: What if the client gave only partial data and our recommendation misses context?\
  **Answer**: State the boundary: “Based on the data I have...” Add what context may be missing. If they provide more data, rerun; otherwise move to the next useful use case.
- **Question**: Can we use generic or synthetic data for a problem from the spreadsheet?\
  **Answer**: Yes, but anchor it to a real human who would benefit from a real action. Synthetic data is acceptable only when the recommendation is still useful and honest.
- **Question**: What do you actually teach in Tools in Data Science now?\
  **Answer**: Not data science, really. I teach how to use AI to do data science and pass tasks by hook or by crook.
- **Question**: How can AI use rich student reflection, game, and story material?\
  **Answer**: Use it for concept-space mapping: clusters, outliers, negative space, and unusual student thinking. It can reveal how students think, not just grade them.
- **Question**: How should Engineering Design explore AI?\
  **Answer**: Start with verifiable environments. Connect AI to CAD, simulation, FEM, SPICE, MuJoCo, or Blender so it creates outputs, gets tool feedback, and iterates.
- **Question**: Is ChatGPT better at math or literal work than Claude?\
  **Answer**: For literal instruction-following, yes. ChatGPT treats “all” like “do not miss anything”; Claude often treats it more casually.
- **Question**: What can I do with 25 years of curated fraud, health, and technology articles now that AI can search?\
  **Answer**: Start with what AI can do, then use your archive and judgment to add the missing 10–20%. Use AI to surface, triage, and direct.
- **Question**: What happens after AI can generate everything quickly?\
  **Answer**: The bottleneck shifts. First verification becomes the constraint, then deciding what to do with the flood of outputs, then the work AI still cannot do piles up.
- **Question**: How should a large organization manage AI infra and token cost?\
  **Answer**: Meter visibly from day one. Give small default budgets, publish usage, raise limits by project/P&L, and make owners own direct costs.
- **Question**: If clients ask us to re-estimate because Claude reduces effort, how do we respond?\
  **Answer**: Reposition from effort to accountable outcome. Clients still pay for ownership, assurance, and “catch us if it goes wrong,” not just the report or code.
- **Question**: If an agent is like an employee, how do we onboard it?\
  **Answer**: Ask AI to read existing training material and create its induction guide. Give it an email ID, manager, examples, rules, and feedback like a new hire.
- **Question**: How should we think about prompt-only 3D/product design workflows?\
  **Answer**: Use an agent-tool loop. Claude Code connected to Blender through MCP can create 3D output with no bespoke software, just prompting, verification, and iteration.
- **Question**: Who can become a forward deployed engineer inside a client environment?\
  **Answer**: Anyone with client data access, AI access, initiative, and curiosity. The job is not to pitch projects; it is to solve problems and send actionable outputs.
- **Question**: How should we make HR, Finance, and Travel look AI-native internally?\
  **Answer**: Run demand-generating sessions on what current AI tools can already do. Pull transformation from real functional pain instead of pushing generic AI from the center.
- **Question**: What is the real training gap in enterprise AI platforms?\
  **Answer**: Often it is initiative, not education. People wait for step-by-step internal-platform training instead of finding docs, people, and workarounds themselves.
- **Question**: How should we hire or filter FDEs?\
  **Answer**: Test attitude first. Did they solve real problems outside curriculum, learn on their own, and push through bad documentation? Then test communication, engineering judgment, and explanation.
- **Question**: Do freshers work as FDEs?\
  **Answer**: Sometimes, but they often vibe-code blindly. Experience matters for judging architecture, explaining trade-offs, communicating status, and navigating ambiguity.
- **Question**: Should data strategy wait for a cleaned data lake before agents?\
  **Answer**: No. Agents can clean, script, structure, and improve data on the fly. Data strategy should start from what agents need and do, not a parallel lake-cleanup program.
- **Question**: How do we make AI assumptions memorable for leaders?\
  **Answer**: Show their own assumption crumbling live. If they think a report takes a week, have AI make a draft in eight minutes and ask what it would have cost.
- **Question**: Where should we look for horizontal AI disruption ideas?\
  **Answer**: Visual AI. Anything that produces engineering drawings, 3D models, architecture, circuits, or design artifacts is ripe because code-like outputs are verifiable.
- **Question**: How do we quickly create an AI workshop brochure for CXOs?\
  **Answer**: Use my talks page and LLM blog posts as source material. Ask Claude or ChatGPT to tailor the poster or PDF to the audience, theme, and call-to-action.
- **Question**: What does “LLM Psychologist” mean?\
  **Answer**: It means studying how models behave under different prompts. Same model, different inputs; same input, different models; understand how to talk to them effectively.
