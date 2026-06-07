---
title: Things I Learned - 02 Nov 2025
date: 2025-11-02T00:00:00+00:00
categories:
  - til
---

This week, I learned:

- [TVMaze API](https://www.tvmaze.com/api) is an API for TV shows, episodes, cast, crew, etc. Useful for TV-related apps as well as learning APIs.
- [Awesome Skills](https://skills.intellectronica.net/) is a curated list of prompts and skills for AI coding agents.
- ⭐ [nokode](https://github.com/samrolken/nokode) is a API server that has no code: just LLMs responding. Interestingly, it is compliant. Just expensive, slow, forgetful and unreliable compared to code. All four are improving with time, indicating that coding may be transitional.
- Notes from [Vanya Seth](https://www.thoughtworks.com/profiles/v/vanya-seth)'s keynote at [OSAI HYD](https://hasgeek.com/fifthelephant/osai-hyd-meetup/schedule/ai-first-software-delivery-superpowers-adoption-challenges-and-the-path-to-software-3-0-5NgsrKyCWSJszHXvHKHkdW)
  - Superpowers of Gen AI to keep in mind when exploring AI coding agent use cases:
    - **Translating**. Requirements to code, code to code, language to queries, standard to standard.
    - **Finding** info just-in-time (in context). How does this work? What's this error? What tools are permitted in my org? Who knows what? E.g. [Atlassian Rovo](https://www.atlassian.com/software/rovo) queries _across_ JIRA, Confluence, etc.
    - **Brainstorming** and ideation. Product ideation. Requirements. Testing gaps. Architecture review. Exploratory / scenario testing.
    - **Summarizing** and clustering. Change logs, incident management, research data, docs summary.
  - Challenges in using AI coding agents:
    1. Adoption imbalance. Only certain roles are amplified by AI. Coding, QA, more than planning, maintenance, AI ops, etc. What's the impact of this?
       - ⭐ Goldratt's ToC implies that backlogs need to fill faster. Downstream becomes a bottleneck. Technical debt piles up.
       - ACTION: Use AI across _entire_ value chain, from research to maintenance.
    2. Locality. enhances roles (nodes), not relationships (links). They optimize local work, not global flow. Workflow tools are missing.
       - Coordination overhead. Context Fragmentation. Translation problems.
       - ⭐ Expand productive roles to cover neighboring tasks. Productive developers shift left and build backlogs; shift right to reduce code review, maintenance tasks.
         - E.g. Move maintenance/production activities into development. Security, performance, monitoring, observability, cost, infrastructure.
         - We spend time on IDE, CI/CD, Jira, Confluence, Prod observability tools.
         - A typical Agent Development Platform (ADP) covers evals, guardrails, workflow builder, agent builder, observability, prompt management, AI gateway (LiteLLM), MCP servers, model fine-tuning, model serving, model repository, vector stores
         - We need ADP Agents covering delivery risk, continuous security, prod issues RCA, observability, performance, accessibility, product research, infra optiimzation, test data generation, anomaly detection, release management
         - ACTION: Share ADP photo with Patrick.
    - ACTION: ⭐ Centralize skills ("knowledge packs") and MCPs and observe which gets used most. Allow people to use more.
    3. Lethal Trifecta. There's growing demand for higher productivity with AI code assistants. But the lethal trifecta makes them an attack vector. It has access to sensitive information, exfiltrate data, and read and follow unsafe instructions.
       - Can lead to supply chain poisoning attacks.
       - Regulated industries cannot adopt.
    4. Technical debt growth. More productivity leads to poor code quality which will slow down future work.
       - See [Software Engineering Excellence 2025](https://www.harness.io/the-state-of-software-engineering-excellence)
       - AI induced complacency.
       - Sunk-cost fallacy on AI-generated code hurts.
       - ACTION: Evaluate code quality continuously to reduce technical debt. Double-down on good engineering practices.
    5. Compliance.
       - Model residency. Self-hosting is required.
       - Data observability gaps. Data privacy, audit trails, etc. are concerns.
       - Token economics. $20/day happens in Thoughtworks. Token cost is subsidized.
       - Rogue AI usage. Use of dis-allowed tools; shadow IT.
       - ROI justification. Hard to quantify productivity gains.
    6. Adoption.
       - AI Literacy. Tap into organizational knowledge
       - Champions & communities of practice to support cross-pollination.
       - Use-case driven adoption. Teams identify based on AI superpowers.
       - AI playbook. Share what worked, what didn't work.
- AI automation is likely less if a **high portion** of work
  - Has **legal liability** (e.g. pharmacist/judge vs shop attendant/lawyer)
  - Is **subjective** (e.g. perfumer/auction appraiser vs lab chemist/insurance appraiser)
  - Needs rapid contextual **decisions** (e.g. detective/fireman/ER vs parking enforcer)
  - Via [ChatGPT](https://chatgpt.com/c/68d79589-c2b8-8331-b86f-0e0f211feb7f), [Claude](https://claude.ai/chat/d534c273-7b6c-4ffa-98a9-5bca40d9959a)
- [parse-sse](https://github.com/sindresorhus/parse-sse) from Sindre Sorhus is a more standards-compliant, more likely-to-be-maintained alternative to my [async-sse](https://github.com/sanand0/async-sse) package.
- Which is better: Comment A: 1 upvote, 0 downvotes (100% positive) or Comment B: 99 upvotes, 1 downvote (99% positive)? Use **Wilson's Lower Bound** which measures "What % positive am I 95% confident of?" [Claude](https://claude.ai/share/0f69e7f8-6ca7-4fee-b3ec-8b580556bc9a)
  - Using this, we can measure metrics for tweets, like below. [ChatGPT](https://chatgpt.com/share/68fef88f-7b18-800c-835f-38a3fe470f34)
  - Popularity = (5 _ WLB(reposts / views) + 2 _ WLB(likes / views)) \* Decay(half-life of 72 h)
  - Memorability = (5 _ WLB(bookmarks / views) + 4 _ WLB(replies / views)) \* Decay(half-life of 36 hours)
- A nice visual "benchmark" of [text-to-image](https://genai-showdown.specr.net/) and [image editing](https://genai-showdown.specr.net/image-editing) models. Seadream 4, Gemini 2.5 Flash, and Qwen Image Edit lead. This includes examples like [straightening te Tower of Pisa](https://genai-showdown.specr.net/image-editing) - which only Flux.1 and Seadream 4 do well on; or removing only the brown M&Ms - which only Qwen Image Edit manages to.
- [Arch](https://docs.archgw.com/) is a pure LLM router. It supports multiple LLMs, flexible routing and observability but not auth.
- From [Codex docs](https://github.com/openai/codex/tree/main/docs)
  - Add [custom prompts](https://github.com/openai/codex/blob/main/docs/prompts.md) in `~/.codex/prompts/xyz.md` and launch as `/prompts:xyz`. Optional: `description:` and `argument-hint:` in YAML front-matter. For example, create prompts to refactor, rewrite in a developer's style, document AGENTS.md, identify re-usable code, etc.
  - `AGENTS.override.md` overrides parent directory `AGENTS.md`. `AGENTS.md` appends to parent `AGENTS.md`. [Fallback names are allowed](https://github.com/openai/codex/blob/main/docs/agents_md.md#how-they-come-together).
  - [`codex exec` supports streaming JSON](https://github.com/openai/codex/blob/main/docs/exec.md#json-output-mode)
  - [`codex exec` accepts a `CODEX_API_KEY=` environment variable](https://github.com/openai/codex/blob/main/docs/exec.md#authentication). [`codex` uses an `OPENAI_API_KEY`](https://github.com/openai/codex/blob/main/docs/authentication.md#usage-based-billing-alternative-use-an-openai-api-key).
  - You can configure [which environment variables are passed to the shell](https://github.com/openai/codex/blob/main/docs/config.md#shell_environment_policy)
  - [Codex reads 32KB from AGENTS.md by default](https://github.com/openai/codex/blob/main/docs/config.md#project_doc_max_bytes)
- Things that I currently follow and don't follow from Peter Steinberger's excellent [Just Talk To It](https://steipete.me/posts/just-talk-to-it#do-you-do-spec-driven-development):
  - [x] Prefer Codex > Claude Code.
  - [x] Ask for options before executing
  - [x] Generate & review specs collaboratively
  - [x] You don't need git worktrees
  - [x] Prefer subscriptions over API to reduce cost
  - [x] Store docs with code
  - [x] Give examples
  - [x] Use voice input
  - [x] Use Codex Web as a mobile inbox for ideas
  - [x] Prefer CLI over agentic platforms
  - [x] Prefer CLI tools over MCP
  - [x] Avoid ALL-CAPS for Codex. It follows instructions well
  - [x] Avoid sub-agents, RAG, etc.
  - [x] Iterate UI live. Watch changes
  - [ ] Use 3-8 agents in parallel on a single repo.
  - [ ] Make small, atomic commit checkpoints. Commit only what the agent touches
  - [ ] Add `ast-grep` as a pre-commit hook to block rule violations.
  - [ ] Keep custom prompts minimal (commit, automerge, massageprs, review, ...). Just "commit" reduces context
  - [ ] Cancel long tasks and ask what's happening
  - [ ] Prefer Medium over High reasoning. It decides level of thinking
  - [ ] Share screenshots
  - [ ] Use tmux to run CLIs persistently
  - [ ] Schedule refactor time (20%). Use jscpd, knip, oxlint, ...
  - [ ] Don't reset context. Cold start wastes time + tokens
  - [ ] Write tests in the _same_ context. Yields better tests, reveals bugs.
  - [ ] Prototype in a separate folder / PR
  - [ ] Queue `continue` messages\*\* before stepping away
  - [ ] Ask it to "Preserve intent and add comments at tricky spots". Future you needs the WHY
  - [ ] On hard problems, add “take your time”, “be comprehensive”, “read all related code”, “form hypotheses”, etc.
  - [ ] Maintain an _evolving_ **AGENTS.md** with product notes, naming, API patterns, test policy, **ast-grep rules**, etc. Delete stale guidelines
- Fascinating implications from [Quantifying Human-AI Synergy](https://osf.io/preprints/psyarxiv/vbkmt_v1) [ChatGPT](https://chatgpt.com/c/68fefa47-6a60-8320-9488-186d617916fc)
  - Models vary in ability to uplift humans. Don't just use standalone model benchmarks.
  - People vary in ability to work with AI. Don't just measure solo skills. Reward AI collaboration ability (delegation, prompting, verification, revision, ...)
  - Train models to ask for missing Theory-of-Mind cues: goal, beliefs, constraints, audience, success test
  - Train people by asking them to predict what the model will get right/wrong, and validate
  - Design UI and models for synergy. UI: Surface/solicit assumptions, intent, uncertainty, constraints. Model: Infer & adapt to evolving user state.
- [OpenRouter image generation](https://openrouter.ai/docs/features/multimodal/image-generation) now includes [GPT-5 Image Mini](https://openrouter.ai/openai/gpt-5-image-mini). An image costs about 1 cent. Here's the code:
  ```bash
  curl 'https://openrouter.ai/api/v1/chat/completions' \
    -H "Authorization: Bearer $OPENROUTER_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      model: "openai/gpt-5-image-mini",
      messages: [{ role: "user", content: "Draw a cat" }],
      modalities: ["image"],
      image_config: { "aspect_ratio": "16:9" }
    }' | jq -r '.choices[0].message.images[0].image_url.url' | cut -c23- | base64 -d > cat.png
  ```
