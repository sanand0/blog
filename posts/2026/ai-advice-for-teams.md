---
title: AI advice for teams
date: 2026-04-25T12:17:03-04:00
categories:
  - llms
description: Shift from individual AI tips to team-scale operations in the agent era by building structured agentic workspaces, treating prompts as durable assets, and relying on executable code and exception routing to verify outputs.
keywords: [agentic workspaces, llm output verification, coding agents, exception routing, prompt asset management, ai team operations]
linkedin: https://www.linkedin.com/feed/update/urn:li:activity:7454167466433282048/
---

I updated my [AI Advice](/blog/ai-advice/) page by:

- Transcribing my calls in the last 2 months (Gemini 3.1 Pro, ["Transcribe this call recording..."](https://github.com/sanand0/blog/blob/384c39c752a580f7ae9c49fafb44a8a09fb75175/pages/prompts/transcribe-call-recording.md))
- Extracting AI advice (Gemini 3 Flash, "Summarize ALL AI-related advice ... into 1-sentence bullets")
- Asking [Claude](https://claude.ai/share/5aa54ed5-fc11-4730-9ea8-7ace18dc6c00), ChatGPT, and Gemini to document what's new / changed. <!-- https://claude.ai/chat/f4e096d6-eb76-4ef0-981f-29217514c209 -->

I added this request:

> But, and this is IMPORTANT, analyze my original writing style, write it exactly in that style, and then verify to make sure it follows the same style (correcting where required.)

This worked _surprisingly_ well with Claude 4.6 Sonnet (adaptive). I used the resulting [ai-advice.md](/blog/ai-advice/) almost verbatim.

Here's the full list of changes it suggested:

![](https://files.s-anand.net/images/2026-04-25-ai-advice-for-teams.avif) <!-- https://chatgpt.com/c/69ed0051-b88c-83ea-8c8f-97b42015fd9d -->

> **The biggest structural update:** ai-advice.md is still written as "how individuals use AI better." Your actual advice has evolved into "how people, teams, and organizations operate in the agent era." The whole document should eventually be reorganized to reflect this.

## INSERT

1. **Build an AI workspace, not just a chat _(Very high frequency — 10+ docs)_** Every serious AI project needs a project folder containing:
   - `AGENTS.md` — folder-specific instructions the agent reads on startup
   - `prompts.md` — all prompts version-controlled as source code
   - `skills/` — encapsulated successful workflows (see #2)
   - Git repository with commits at every checkpoint
   - Test fixtures, synthetic datasets, logs, outputs

   Treat prompts as the real IP. Code is disposable; prompts, tests, and skills are assets.

2. **Encapsulate successful workflows into reusable skills _(Very high frequency)_** Once an agent succeeds at a task three times, encapsulate it: the prompt, tools used, edge cases, constraints, validation tests. Store in a `skill.md` file. Skills are the new software libraries — they make workflows deterministically repeatable without re-explaining everything. Use agents to _build_ these skills by asking them to summarize what they learned.
3. **Run coding agents safely: Git + Docker _(Very high frequency)_** Always: (a) work inside a Git repository and instruct the agent to commit as it goes — `git checkout` is your undo button, (b) run agents inside Docker containers so they cannot touch your actual files, (c) use "YOLO mode" (skip permission prompts) only inside isolated containers. These aren't optional for anything beyond throwaway prototypes.
4. **"LLMs hallucinate, but code doesn't" — use code as the truth engine _(Very high frequency)_** Broaden "have it write code to process numbers" significantly. The mantra is: wherever correctness matters, make the AI produce _executable code or logic_ rather than natural language answers. Code either works or fails — it's binary and auditable. Use domain-specific languages (Prolog-like rule trees, schema validators, policy-as-code) for logic-heavy tasks. This is the primary mechanism for eliminating hallucinations in production.
5. **Build verification into the workflow, not after it _(Very high frequency)_** Verification should be engineered as a product feature, not added as a post-hoc check. Every output should expose: source citations linked to snippets, confidence levels, what's unverifiable, disagreement signals, and audit logs. Use model disagreement as a _routing signal_ — when models disagree, send to human review; when they agree, lower review priority. Build golden sets to measure actual accuracy on your specific task.
6. **Use AI for exception triage, not blanket automation _(High frequency)_** Let AI classify outputs as red/yellow/green: green = automate fully, yellow = flag for review, red = human required. This is more mature than "80-90% AI, human for last mile." It says _exactly_ where the human loop belongs, and it scales: automation handles routine volume while humans focus only on high-stakes exceptions.
7. **Use synthetic data deliberately _(High frequency)_** Not just "realistic fake data for prototyping" — generate hypothesis-driven synthetic data that embeds specific behavioral patterns, edge cases, and known failure modes you expect in production. This lets you stress-test before real data arrives, without compliance concerns, and at whatever messiness level you choose.
8. **Treat demos as imagination accelerators _(High frequency)_** Demos are not just proof-of-concept — they are the fastest way to expand what stakeholders think is possible. Use "Hollywood set" demos: working outputs, simulated backends, precomputed workflows, client-specific synthetic data. Only demo live if the task completes in under 10 minutes. Simulate or precompute slow, expensive, or credential-heavy workflows. Show the output first; defend the architecture only if asked.
9. **Maintain a living model radar — don't freeze model advice _(High frequency)_** Specific model recommendations go stale within months. The durable advice: continuously blind-test frontier models on your _exact_ task, maintain a benchmark set, and route by capability. Current pattern: Claude for coding/aesthetic/style/writing; ChatGPT for rigorous analysis/financial modeling/extended thinking; Gemini for Google Workspace/research/video/speed. But measure this; don't assume it. Additionally: use LiteLLM or Portkey as open-source gateways for organizational cost observability across models.
10. **The Jevons Paradox applies to knowledge work _(High frequency in strategic contexts)_** AI making cognitive tasks cheaper will _increase_ total demand for cognitive work, not reduce it. Human roles shift from execution to verification and judgment — but there's a talent crunch coming for verification roles. Hire now for people who can check, certify, and take accountability for AI output.
11. **Use games to teach AI, not slide decks _(High frequency)_** Replace passive L&D with Capture the Flag challenges, treasure hunts, forbidden-word jailbreaks, prompt-injection games, and coding-agent races. Evaluate proficiency by task completion speed with an agent, not syntax recall. Design challenges where using a coding agent is the only practical way to finish in time — this creates binary signal: those who can use agents solve everything; those who can't solve nothing.
12. **Bifurcate hallucination advice: operational vs. creative _(Medium-high frequency)_** Current advice mixes these. Split explicitly:
    - **For operations, facts, finance, law, regulated outputs**: eliminate hallucinations via multi-agent consensus, code execution, source grounding, and human routing
    - **For ideation, brainstorming, research**: deliberately _use_ hallucinations as stochastic ideation. Run the same prompt multiple times. Use weaker models without extended thinking — "speaking without thinking" produces more imaginative divergence
13. **Move from dashboards to answers and actions _(High frequency)_** Replace static BI dashboards with AI that answers "what should I do?" not just "what happened?" Ask AI to anticipate a stakeholder's questions and pre-answer them. The endpoint: proactive agents that push insights to individuals rather than passive dashboards that wait to be queried.
14. **Sell outcomes, accountability, and verification — not software _(High frequency in business contexts)_** Software is a depreciating asset; any client can regenerate it tomorrow. Durable value: judgment, trust, domain expertise, data access, and taking responsibility for results. Shift toward outcome-based pricing. The "neck to catch" — human accountability for AI output — is increasingly the product.
15. **Measure AI adoption by behavior, not attendance _(Medium frequency)_** Track: unique days of active use (regularity beats volume), token consumption trends, tool diversity, quality of outputs produced, and business outcomes driven. Usage logs from NetSkope or LLM gateways give better signal than training completion rates.
16. **Assess AI literacy by how people prompt, verify, and recover _(High frequency in education contexts)_** Don't evaluate final answers — AI can produce those. Evaluate: quality of prompts (specificity, guardrails, constraints), ability to identify and fix hallucinations, recovery from errors, and process discipline. Multiple-choice questions are essentially obsolete for AI-era assessment. Assess the _process_, not the output.
17. **Use AI-native output formats _(High frequency)_** Stop defaulting to PPT or PDF. AI generates HTML, SVG, JSON, interactive dashboards, podcasts, sketch notes, and games better than it generates static slides. A single source document can auto-generate: podcasts, explainer videos, interactive quizzes, sketch notes, executive summaries, slide decks. Use NotebookLM for audio synthesis from diverse sources.
18. **Audit your own behavior via AI _(Medium frequency)_** Feed your own meeting transcripts, email chains, and call recordings into LLMs to find personal blind spots, biases, and recurring errors. Conduct project post-mortems on email threads. Use adversarial prompting — pit GPT against Claude to stress-test your plans. This expands "mine your digital exhaust" from insight into behavioral coaching.
19. **Optimize content for the agentic web _(Medium frequency)_** More content is now consumed by AI agents than humans. Publish in formats AI can parse, cite, and remix: clean metadata, semantic structure, source links, reusable chunks. Develop MCP connectors to your proprietary content. This is SEO for the agentic era.
20. **Ask AI what it needs before starting _(Medium frequency)_** Don't guess what context to provide. Ask: "What information, tools, files, and access do you need to do X?" Let the agent specify missing pieces before it starts, not halfway through. Simple and dramatically reduces mid-task derailment.

## UPDATE

1. Two-Strike Rule → time-box and preserve context before abandoning
   - **Current:** Abandon after two failed fix attempts.
   - **Update:** After two failed repair loops: (a) ask the agent to produce a failure summary, minimal reproduction case, and fresh plan before abandoning, (b) switch to a time limit (2 hours) not an attempt limit, (c) in Docker/YOLO mode, let agents iterate without this limit. The current rule was written for chat-based coding; agentic tools self-correct across many more iterations. Pure restarts discard useful diagnostic context.
2. Paid subscription → quality + friction, not blanket privacy
   - **Current:** "Your data isn't used to train the models. This is the best $20/month."
   - **Update:** Paid subscriptions give better models and less friction. For _privacy_, the picture is more nuanced: consumer plans (ChatGPT, Claude.ai) have data controls you must check and configure; Enterprise/API plans explicitly exclude training by default. For sensitive work, use Enterprise/API or run locally. Don't assume consumer paid = private. [OpenAI Data Controls FAQ](https://help.openai.com/en/articles/7730893-data-controls-faq) Also: maintain subscriptions to all three major models (~$60-80/month), not one. Heavy users: consider the $100/month tier to eliminate friction during peak experimentation.
3. Model recommendations — replace frozen Q1 2026 advice with routing logic
   - **Current:** "Claude/Gemini still good at UI. GPT for rigorous testing."
   - **Update:** See INSERT #9. Add: use a more capable model (Claude) to write scripts and instructions for cheaper models (Codex) to execute. Benchmark on your exact task; these rankings shift quarterly.
4. "Intern" — expand to multiple mental models by task
   - **Current:** "It's as smart as a post-graduate intern."
   - **Update:** The right mental model depends on task:
     - _Brilliant but stubborn intern_: excellent at fetching/preparing materials, unreliable for precise design or nuanced judgment
     - _Fresh MBA who needs full context_: give it the same rules, examples, and feedback you'd give a new hire
     - _Senior mentor to defer to_: for syntax, library knowledge, and coding patterns, AI may know better than you — defer ("Mentor Flip")
     - _Alien intelligence that needs coaching_: for novel tasks, it needs explanation, not just instruction
5. Human-in-the-loop → human-on-the-loop with exception routing
   - **Current:** "Handle 80-90% of effort, human expert for last mile validation."
   - **Update:** More mature framing — "human-on-the-loop" rather than "human-in-the-loop." Build a confidence-building period first; validate; then grant autonomy for routine cases. The human's job is to review exceptions (disagreements, low-confidence, high-stakes), not everything.
6. "Code is disposable" → prompts and skills are the real assets
   - **Current:** "Code is an AI compilation artifact. Don't get attached to it."
   - **Update:** Code is disposable _when the workflow is disposable_. But prompts, skills, tests, data contracts, and validation logic are permanent assets that compound in value. Preserve these even when you throw away the code.
7. "Don't learn to code" → learn logic, not syntax
   - **Current:** "As a non-technical person, build apps. Don't learn to code."
   - **Update:** Don't worship syntax — it's declining in value. But learn enough conceptual fluency to: specify what you want clearly, write test cases, debug outputs, assess security implications, and judge whether AI-generated code is correct. Syntax is less valuable; understanding is not.
8. "Buy, don't build" → buy foundations, build thin orchestration
   - **Current:** "Don't train models. Build orchestration layers and proprietary data workflows."
   - **Update:** Don't build or fine-tune base models (they're obsolete on arrival). Do build: thin domain-specific orchestration, skills/prompt libraries, verification layers, data pipelines, and MCP connectors. Avoid custom SLMs unless you have strict air-gap, privacy, or cost-at-scale constraints — the "SLM Depreciation Trap" (custom models obsolete before deployment) is real.
9. "Wait for models to improve" → apply a 1-3 month ROI window
   - **Current:** "Things not possible today will be possible in a few months."
   - **Update:** Apply a test: if a workaround won't pay back within 1-3 months, wait. If building creates learning, adoption, or strategic leverage now, prototype anyway. The advice shouldn't be "wait" or "build" — it should be "calculate the ROI window."
10. Data safety → specific operational checklist
    - **Current:** Send schema not data; pick trusted providers; anonymize.
    - **Update:** Add specific controls: set Google Drive access to read-only and Gmail to draft-only for AI; keep a dedicated "AI-only" folder rather than granting full Drive access; use separate browser profiles for work/personal AI; run agents locally (Codex, Claude Code on-machine) for sensitive data; use MCP for restricted, scoped data access. Anonymize before cloud; schema+local-execution for sensitive tabular data.
11. "Hallucinations can be a great feature" → boundary-condition this
    - **Current:** "Don't always eliminate them. Use as appropriate."
    - **Update:** Great for: ideation, research brainstorming, creative divergence, humor. Never acceptable for: facts, finance, law, medicine, safety, or regulated outputs without verification. Be explicit about which mode you're in.
12. Skills section — "declining" needs nuance
    - **Current:** "Domain depth" listed as declining.
    - **Update:** Routine versions of domain skills decline; judgment-heavy versions grow. Domain depth matters most for: problem framing, validation design, incentive mapping, ethics, and edge-case recognition. Don't blanket-advise people to abandon domain expertise.

## DELETE

- **Two-Strike Rule** (current form): Outdated for agentic tools; replaced by time-boxing + context preservation |
- **"Paid subscription = privacy"** (the simple version): Factually incomplete; needs the consumer/enterprise/API distinction |
- **"If all models agree, accept"**: Too strong. Soften to: "agreement lowers review priority; measure on a golden set" |
- **"Claude/Gemini for UI, GPT for rigorous testing" Q1 2026 frozen claim**: Goes stale; replace with routing logic + model radar |
- **"Prefer less experienced people"** (blunt version): Replace with: "prefer AI-native, humble, high-agency people — could be interns, domain experts, or non-coders; the traits are delegation, verification, and fast learning" |
- **"Wait for the crisis"** (adoption section): Reframe to: "watch for urgency windows; arrive prepared with demos, risk framing, and low-friction integration" |
- **"Domain depth is declining"** (blanket): Replace with nuanced version from UPDATE #12 |
- **"Use AI for validation is safe and effective"** (unqualified): Replace with: "use AI to _design_ validation workflows; don't treat AI output as validation itself" |
- **"Repurpose content and data" TODO placeholder**: Fill it in or remove it |
- **"Have it write code to process numbers"**: Upgrade to "LLMs hallucinate, but code doesn't" — write _and execute_ code for correctness |

## Contradictions

- "Stay out of the way" vs. "verify everything": Risk ladder: low-risk/creative/prototype = get out of the way; high-risk/regulated/persistent = full verification stack |
- "Code is disposable" vs. "use Git, Docker, versioning": Code may be disposable; _recovery, reproducibility, and auditability are not_ |
- "Don't learn to code" vs. "candidates need technical depth": Syntax is less valuable; conceptual fluency (logic, testing, security, judgment) is more valuable |
- "Buy, don't build" vs. "build custom pipelines": Don't build foundation models or heavy platforms. Do build thin orchestration, domain workflows, verification layers, skills |
- "AI wildly" vs. security/privacy constraints: Overuse for low-risk/personal tasks; use enterprise/local/sandboxed patterns for sensitive work |
- "Human-in-the-loop" vs. autonomous agents: Exception routing: automate routine cases, route edge cases and disagreements to humans |
- Live demos vs. simulated demos: Live only if task completes in under 10 minutes; simulate otherwise |
- "Hallucinations as feature" vs. eliminate hallucinations: Feature for ideation; eliminated for operations/facts/regulated outputs |
- "AI can do health/finance better than experts" vs. responsibility: AI supports preparation and second opinions; decisions need qualified human accountability |

## 10 principles

1. The scarce skill is not doing the work; it's choosing the work, feeding the agent context, and verifying the result.
2. Prompts, skills, tests, and context files are assets. Code is a byproduct.
3. Use AI wildly in low-risk contexts; use it rigorously in high-risk contexts.
4. For facts and money, make AI produce evidence. For logic, make it produce code. For operations, make it produce audit trails.
5. LLMs hallucinate, but code doesn't. When correctness matters, make AI write and run code.
6. Treat demos as imagination accelerators — show what's now possible before arguing about architecture.
7. Don't sell software if the client can regenerate it tomorrow. Sell outcomes, accountability, and verification.
8. AI training should be a game of doing, breaking, checking, and recovering — not a lecture about tools.
9. Every repeated AI success should become a reusable skill. Every failure is training data if you preserve the prompt, output, rejection reason, and fix.
10. The risk today is not just hallucination; it's underuse, insecure overuse, and unverified scale.

## Suggested structural reorganization

Your current document answers: _"What tips should I follow?"_
Your actual advice answers: _"How do I operate in the agent era?"_

Suggested new top-level structure:

1. **Start here** — AI is a new operating layer; use it 50 times/day; ask it first, verify consequential outputs
2. **Personal habits** — voice, interview-me, emotions as entry points, digital exhaust, learning by play
3. **Prompting and context** — outcome-first, sycophancy defense, multiple outputs, style vocabulary
4. **Agentic workspaces** — project folders, AGENTS.md, skills.md, prompts.md, Git, Docker
5. **Coding with AI** — vibe code safely; code is disposable; tests/prompts are assets; Playwright; failing tests first
6. **Verification and trust** — citations, code execution, golden sets, multi-model checks, exception routing
7. **Data and privacy** — consumer vs. enterprise vs. API vs. local; least-privilege access patterns
8. **AI adoption in organizations** — visible leadership use, behavior tracking, games/CTFs, power users, incentive mapping
9. **Demos, POCs, and business value** — prototype in hours; synthetic data; Hollywood-set demos; sell outcomes
10. **Skills in the AI era** — grow/shrink/preserve taxonomy (updated)
11. **Education** — assess process not output; AI-proof questions; monitor the messy middle
12. **Business models** — software depreciates; skills/trust/verification appreciate; thin orchestration not heavy platforms
