---
title: Questions I am asked
description: Questions people ask me, and my answers.
---

# Questions I am asked

Questions people ask me, with names, organizations, and exact dates removed.

## Week ending 30 Aug 2026 {#week-ending-2026-08-30}

- **Question**: How hard was it to adapt your personal AI workflow to work?\
  **Answer**: I didn't try solving work problems. Rather, I took what I was solving personally with agents and tried finding where at work I can apply it. "I have a hammer, let me find all the nails."
- **Question**: If agents can do the coding, how do we teach the foundational blocks?\
  **Answer**: We don't care if they learn FastAPI, etc. Routing, authentication, interfaces, ... - THAT is more useful. So give them tasks that forces them to learn FUTURE foundational blocks FROM agents.
- **Question**: How do you monitor whether people are actually using reusable AI skills?\
  **Answer**: Read the agent session logs. A small script over Claude, Codex and Copilot histories can tell you which skills were actually used and how often.
- **Question**: How are you determining which AI spend is dumb?\
  **Answer**: Start with the highest-cost users and inspect the obvious outliers. Give the raw logs to an agent, ask why someone spent that much, tell users to make obvious optimizations, etc. before attempting sophisticated optimization.

## Week ending 23 Aug 2026 {#week-ending-2026-08-23}

- **Question**: How do I safely let an agent modify my files when it could get things wrong?\
  **Answer**: Make backups and let it work on a copy. Try it five or ten times; once it repeatedly earns your trust, gradually remove the safety net.
- **Question**: When should I turn an ad-hoc agent workflow into automation?\
  **Answer**: If I run it once every two months, I don't mind the agent writing the code again. If it's every two weeks or two days, save the script and automate it.
- **Question**: How do we decide which agents to train when client problems keep changing?\
  **Answer**: Decouple the agent from the skill. Keep the skill intelligence agnostic - it's not about correcting agent errors but about transferring context it won't have. Keep a central folder of skills with one-line descriptions; whichever agent people use can scan it and pick the relevant skills.
- **Question**: Which part of the current agentic AI narrative is overhyped?\
  **Answer**: GraphRAG is definitely overhyped. Prompt engineering is outdated; harnesses and agentic loops are not overhyped yet.
- **Question**: To make agentic software development scalable, do we need a standard framework or just give everyone Cursor and let them figure it out?\
  **Answer**: Install Cursor for everyone and let them figure it out. Share lightweight enterprise guidelines as skills, but give every instruction an expiry date and a small benchmark so you can remove it as agents learn to handle it themselves.
- **Question**: If frontier video models fail on physics and action scenes, how should we fine-tune them with our proprietary video data?\
  **Answer**: Don't solve the physics problem; solve a much narrower action-block problem. Build reusable filtering and fine-tuning pipelines so the next frontier model can replace the base model and you train only on what it still cannot do; no manual annotations.
- **Question**: Will AI take all the tech jobs in the next five to six years?\
  **Answer**: Yes. And so what? AI will take a significant number of existing jobs, and we'll create new ones because our desires and competition don't disappear; figure out which new work takes you further before your neighbor does.
- **Question**: How did you come up with this conceptual clarity about what to do?\
  **Answer**: I didn't. Pretend to have clarity, ask AI everything and use its answers, then do it so often and fail repeatedly that you get a feel for what works. Quantity beats quality like crazy.

## Week ending 16 Aug 2026 {#week-ending-2026-08-16}

- **Question**: What should a strong data scientist actually build in an AI-native delivery model?\
  **Answer**: Assume he is training an AI to replace him. He should not build the thing himself; he should direct the agent, apply his judgment over a few iterations, and leave behind a portable system you can benchmark and rebuild simpler, better and faster.
- **Question**: If two people are iterating on an AI-native delivery workflow, what collaboration setup do they need?\
  **Answer**: Shared files solve most of it. Keep data, code, skills/prompts and notes in folders with the right permissions; Google Drive or OneDrive is enough for now.
- **Question**: If we're debating whether a course is even necessary anymore, how do we transition it for AI?\
  **Answer**: Start with a single class that's full AI, a single exam that's full AI, one step at a time.
- **Question**: Instead of hiring more developers, should I take fewer people and spend the difference on premium AI seats?\
  **Answer**: Experiment with a few people, not everyone. Treat AI as an extra headcount slot, but radically raise the output expected; getting that productivity happens only when you need that productivity.
- **Question**: Should we self-host open models to reduce LLM costs?\
  **Answer**: Do the math: machine cost per hour versus useful inferences per hour and compare it with the API. Cost alone probably isn't enough; privacy is a much better reason to self-host.
- **Question**: How do you build a QA agent that tests developers' work and reports back?\
  **Answer**: Don't build the agent first. Tell a coding harness the outcome—find requirements, create tests, run them and report—and do it manually 5–10 times; automate only after you know what you actually want.

## Week ending 09 Aug 2026 {#week-ending-2026-08-09}

- **Question**: Is this (Email AI with LocalMCP plugin) just search on steroids?\
  **Answer**: Yes. Search on steroids is not a bad mental model. The deeper capability is the ability to loop like crazy - keep hitting a problem with tools until it actually gets solved.
- **Question**: How do you build enough trust to let agents take multiple steps without constant approval?\
  **Answer**: Don't try to convert everyone. Leave the early adopters alone; show the middle working examples and let them try carefully. When the middle moves, the rest will catch up themselves.
- **Question**: If AI accelerators become outdated in two weeks, how do you keep up?\
  **Answer**: Build accelerators for accelerators. Instead of investing in a benchmark, build a benchmark-builder from production logs; leapfrog one step and plan for agents to automate today's specification and verification work.
- **Question**: How do we govern all the AI apps employees are creating?\
  **Answer**: First ask, "Does this need governing?" Personal use: do whatever you want. Shared apps: review them. Don't say, "You cannot do X unless it is governed."
- **Question**: Where do you stand on "code with AI, code without review"?\
  **Answer**: Usually review it, with AI helping find problems. But for throwaway code, or code agents write for themselves, or incidental to a business output you can verify, validate the outcome instead.

## Week ending 02 Aug 2026 {#week-ending-2026-08-02}

- **Question**: How much time and resources does an AI engagement require?\
  **Answer**: Don't onboard first since that takes time and budget. Onboard our team only when repeated opportunities exceed your bandwidth. Start with two hours of co-working and build something useful first.
- **Question**: How do we know whether our LLM cost-reduction measures actually worked?\
  **Answer**: Compare like-for-like cost per accepted output, including quality, turnaround time and human effort. Run it weekly for four weeks before deciding.
- **Question**: How do we improve an AI workflow from 89% quality to 95%?\
  **Answer**: Don't try ad hoc prompt combinations. Build a benchmark, separate retrieval failures from verification failures, change one variable at a time, and route uncertain cases to humans.
- **Question**: How should I prompt coding agents so they understand the outcome and constraints?\
  **Answer**: Define what "done" means - the outcome, constraints, how to test. Quiz its plans, approach, and tests.
- **Question**: What should I do when a coding agent gets stuck in a loop?\
  **Answer**: Stop quickly. Have it document a post-mortem. Start afresh with a failing test.
- **Question**: How should AI-generated software be tested?\
  **Answer**: Give every requirement an automated test. Test against real usage, convert bugs into regression tests, and ask a fresh agent what is unsafe or untested.
- **Question**: How is your Ask AI agent architected?\
  **Answer**: I trigger ChatGPT manually to read my emails via a Local MCP connector using `gws` and read my emails, notes, transcripts, etc. and answer in my style. I review and paste the answer back in the reply.
- **Question**: Why not fully automate an email-answering AI agent?\
  **Answer**: I'll watch first, and automate when I'm confident.
- **Question**: How do we create benchmarks and automatically improve prompts?\
  **Answer**: Create benchmarks from past usage data/logs. Keep a holdout dataset, make one change at a time, and add production failures back as tests.
- **Question**: What should a central team measure to understand AI adoption?\
  **Answer**: Join usage logs to the employee reporting tree over time. Organizations can action top-down and you need insights rolled up the org tree.
- **Question**: How should a central AI team start tracking and controlling AI costs?\
  **Answer**: Log everything. Preserve raw logs to make sure you can do any analysis later.
- **Question**: Does it matter that the newest models and agent features reach enterprise platforms late?\
  **Answer**: Usually less than it appears. Model gaps are small, manageable, and close within weeks. Access to real data, permissions, feedback and a running workflow are the bigger constraints.

## Week ending 26 Jul 2026 {#week-ending-2026-07-26}

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

## Week ending 19 Jul 2026 {#week-ending-2026-07-19}

- **Question**: What if proactive AI-generated work gets no stakeholder feedback?\
  **Answer**: Keep sending small experiments and log what gets a response. Once one works, compare it with the misses and ask the stakeholder what made the difference.
- **Question**: How should autonomous agents that plan, decide, and act be introduced into customer experiences?\
  **Answer**: Increase autonomy step-by-step: advise first, act after confirmation next, then act within explicit limits. Start read-only, enforce access, spending, and safety boundaries with logs and human escalation, measure failures, then add transactions.
- **Question**: What would success in this GenAI Architect role look like after one month, six months, and two years?\
  **Answer**: One month: clients ask for you. Six months: delivery teams ask you to rescue difficult projects. Two years: clients ask for more people you trained.
- **Question**: What AI spending limit should we set for each developer?\
  **Answer**: Don't set equal per-person limits. Set a team budget against committed outcomes, allocate it to whoever produces the most value per dollar, and review spend against delivered value every month.
- **Question**: Is improving a prompt itself a reusable skill?\
  **Answer**: Yes. Build a benchmark first, test multiple prompt variants against it, then use the same loop to auto-improve entire skills.
- **Question**: How should a data visualization course change now that AI can generate charts?\
  **Answer**: Teach the invariants: problem formulation, selection, critique, verification, uncertainty, and accountability. Delegate chart generation and routine data preparation to AI.

## Week ending 12 Jul 2026 {#week-ending-2026-07-12}

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

## Week ending 05 Jul 2026 {#week-ending-2026-07-05}

- **Question**: What skills are AI-proof?\
  **Answer**: Don’t memorize a fixed list. Delegate maximally and watch what remains; today relationships and accountability are strongest, while taste, judgment, and verification are temporary advantages.
- **Question**: When should we kill an AI-generated chart rather than fix it?\
  **Answer**: Kill it if the chart could cause harm, is fundamentally wrong for the audience, or needs to be recreated from scratch. Curation includes refusing to publish, not just polishing.
- **Question**: How does a junior learn and grow if AI does most of the execution?\
  **Answer**: Pair them with experts and real clients; let them produce artifacts fast, absorb feedback, and build specification, taste, synthesis, and verification. Don’t make them rehearse every manual step AI already does.
- **Question**: What form should AI engagement assets take so another team can actually reuse them?\
  **Answer**: Store them as recombinable atoms—domain context, tools, skills, golden datasets, and telemetry. The platform assembles, verifies, deploys, and learns from them for each new engagement.
- **Question**: How do we make this the way teams work, not a one-off experiment?\
  **Answer**: Ask, “Show me where you’ve done this.” Requiring visible evidence creates the behavior; the strongest teams deliver and the rest learn from them.
- **Question**: What does “Improve” mean after an AI workflow is deployed?\
  **Answer**: Monitor whether it still works as new data arrives. Then improve the model, add better data, or change the downstream workflow—automatically where verification allows.
- **Question**: Is loop engineering just putting agents in a loop to build an app?\
  **Answer**: No. Give a continuously running agent loop one operational goal; it can build apps, create artifacts, use budgets, and optimize the workflow as needed.
- **Question**: How should technical interviews change now that AI can do the coding?\
  **Answer**: Replace at least one coding exercise with a direct business-output exercise. Let candidates use AI and public data; judge whether they can produce something useful, not whether they typed the code.
- **Question**: What do we do when AI gives us a hundred words for a one-word question and becomes a firehose?\
  **Answer**: Treat it like a verbose person. Stop it, ask for two sentences, or ask, “What do you want me to do?”

## Week ending 28 Jun 2026 {#week-ending-2026-06-28}

- **Question**: Why is building invoice generation the wrong next step after finding reconciliation errors?\
  **Answer**: Fix the wrong number inside the existing workflow. Don’t replace a working accounting system with new software just because you can generate a PDF.
- **Question**: In enterprise AI delivery, should the reusable accelerator be the large part and client customization the small part?\
  **Answer**: No. The common layer is usually thin; customization is the larger part because client environments and workflows vary.
- **Question**: Why not automatically send every prompt to ChatGPT and Claude in parallel?\
  **Answer**: Don’t remove all friction. Prompting is cheap; reading is the bottleneck. A tiny copy-paste cost stops me from generating outputs I will never review.
- **Question**: What are the most common corporate pushbacks to implementing AI?\
  **Answer**: Security, hallucinations, and cost—in that order.
- **Question**: Do forward deployed engineers need to be onsite?\
  **Answer**: No. They need access to the client environment and stakeholders; physical location is secondary.
- **Question**: Why ask the agent to solve the problem directly instead of first researching existing models?\
  **Answer**: Start direct. If it fails, break it into chunks. It saves time and tests whether the model has become smart enough to handle broader delegation.
- **Question**: What best practices should non-coders follow when vibe-coding enterprise products?\
  **Answer**: Don’t optimize the old software workflow. State the business goal, let the agent build whatever is needed, and review the output hard.
- **Question**: For a high-stakes EMS, should we deliver software or the decisions it produces?\
  **Answer**: Deliver decisions. Software, agent, and human together are the stack; price the outcome, not the code, tokens, or FTE effort.
- **Question**: How can we guarantee decisions if humans cannot be right every 15 minutes?\
  **Answer**: Treat it like a warranty. If the decision is wrong, don’t pay me; if it is right, pay X. Price in the error margin.
- **Question**: Should a high-stakes EMS use a deterministic mathematical model with an agentic layer on top?\
  **Answer**: Yes. What you know for sure goes into the program; what you don’t know stays with the agent or human. Benchmark both on the outcome.
- **Question**: How do you get yourself out of the loop instead of becoming the bottleneck?\
  **Answer**: Keep an AI bottleneck log. Every time I am stuck, I ask AI how to remove that bottleneck; “interview me” and “assetize this” are surprisingly effective.
- **Question**: In AI hiring, who should we hire when specific skills keep getting commoditized?\
  **Answer**: Hire flexibility, not fixed skill. The “best” data scientist, engineer, or product manager can become legacy in months.
- **Question**: How do we train sales and delivery leaders to speak credibly about AI solutions?\
  **Answer**: Don’t run classroom AI training. Run live solution labs where leaders use AI on a real workflow, build the first output, and draft what they will take to the client.
- **Question**: Can AI help me structure client pitches without depending on internal experts?\
  **Answer**: Yes. Feed it the messy conversation, files, links, and prior context. It won’t be identical to an expert, but it can produce above-average analyst output at scale.
- **Question**: What attitude helps people start using AI every day?\
  **Answer**: Don’t take AI too seriously. Its job is to serve you; give rough instructions, ask it to interview you when you’re unclear, and iterate.
- **Question**: Is clicking “Ask AI” a good signal that students are struggling?\
  **Answer**: Not by itself. Smart students may click it to save time. Combine it with performance and behavior data before deciding intervention.
- **Question**: Do forward deployed engineers just produce “insights on steroids,” or should they deploy AI into workflows?\
  **Answer**: They should move through stages: identify use cases, solve like an analyst, drive action, then embed it into production. Insight is only the first useful step.
- **Question**: How do we move from after-the-fact AI analytics to AI that prevents workflow errors?\
  **Answer**: Put the check where the data enters. Let the agent inspect current controls, propose guardrails or code, and turn recurring insights into monitored workflow.
- **Question**: Will enterprise AI deployments mostly live inside existing platforms rather than custom infrastructure?\
  **Answer**: Yes. Most deployments will happen where the data and workflow already live. Master the platform harnesses instead of building everything from scratch.
- **Question**: What do I do when I don’t even know the problem in a broad domain like rights?\
  **Answer**: That is the problem. Give the context to an agent and ask it to find, rank, validate, and build the easy use cases.
- **Question**: If clients can also use AI agents, what value do I add as a media expert?\
  **Answer**: If they could do it, they would have. Your value is harnessing agents with private data, schemas, validation code, skills, and test cases they don’t yet have.
- **Question**: Should we position our R&D product-plus-service offering as AI?\
  **Answer**: Maybe don’t. Use AI to serve more clients better and faster, but sell the outcome. The client neither cares nor needs the AI story.
- **Question**: What should I not do in GTM while selling AI plus services?\
  **Answer**: Don’t fight with your co-founder. Put someone in the US. Don’t be dogmatic: it is okay to do what the business needs.
- **Question**: Is there a case for building small language models for industry-specific process knowledge?\
  **Answer**: Use case, yes. SLM as default solution, no. Put a modern agent on the problem and let it choose tools; SLMs are usually expensive, depreciating, and behind frontier agents.
- **Question**: Is adding AI sentiment and renewal probability into CRM enough?\
  **Answer**: It is only half a step. Don’t give reps another signal; use bulk data to create watchlists, proactive calls, and specific actions.
- **Question**: Is a quick AI-built sponsorship visualization valuable for a new executive?\
  **Answer**: Useful once, but not enough. Executives need decisions: who pays most, what expires, what action to take, and how much money is at stake.
- **Question**: As a GenAI engineer, do I need deep ML knowledge?\
  **Answer**: Not as the main bet. If it is teachable and testable, AI will do it. Learn to define the problem, test the output, and use the model’s expertise.

## Week ending 21 Jun 2026 {#week-ending-2026-06-21}

- **Question**: Can we create a Claude Skill that runs after every workflow?\
  **Answer**: Yes. But skills affect many chats, so treat them like production instructions: review every word, test them, and keep a copy-paste prompt-library fallback.
- **Question**: If the direct reconciliation savings are small, will a client still spend on the solution?\
  **Answer**: Maybe. The value may be safety, dispute prevention, digitization, and an automated finance process before the client sees an error.
- **Question**: What do we do when hidden operational reasons block an AI-generated use case?\
  **Answer**: Don’t fight the rock. If one stakeholder can’t act, go to another; feed the constraint back to AI and ask for actions this person can take.
- **Question**: Can AI build the data science model end to end once we identify the problem and data?\
  **Answer**: Yes. Not as well as the best data scientist every time, but as well as many good data scientists; the scarce skill is using and validating it well.
- **Question**: How should we validate AI analysis so small errors don’t destroy trust?\
  **Answer**: Validate like a data science manager, not an engineer. Treat the agent as a smart analyst: probe assumptions, ask it to find errors, and be accountable.
- **Question**: Can we build AI use cases before we get real client data?\
  **Answer**: Yes. Use public context plus synthetic data to reach proposal stage, then show the client the kind of action we could take once real data lands.
- **Question**: If ChatGPT gives different answers in different chats, should we rely on it?\
  **Answer**: Don’t rely blindly. Treat another chat as a second opinion, upload the same evidence, ask both to cross-check, and make disagreement part of verification.
- **Question**: What is harness engineering?\
  **Answer**: The layer above models that orchestrates skills, context, tools, hooks, permissions, and teams. ChatGPT, Claude Code, and Antigravity are harnesses, not just model interfaces.
- **Question**: At what levels should we think about AI harness architecture?\
  **Answer**: Three levels: model choices, harness orchestration, and agent teams. Model is parameters/tools; harness is reusable control; team is planners, builders, QA, deployers, and sub-agents.
- **Question**: When should something become a reusable skill?\
  **Answer**: When the capability has high reuse across prompts. Data analysis or writing style belongs in a skill; one-off turbine-efficiency logic probably does not.
- **Question**: How should teams of agents be designed?\
  **Answer**: Let agents negotiate their own charters. Give the task, ask what role split would work, then form planners, developers, QA, deployers, or sub-agents around the work.
- **Question**: What should we do if AI-ready chunks can generate infinite stories?\
  **Answer**: Don’t start by selling the platform. Generate 200 stories, send them to 10 journalists, and become their story pipeline; publishing is the harder bottleneck.
- **Question**: What happens to personal knowledge as work moves across locked platforms?\
  **Answer**: Digital-brain software becomes more valuable. Exports will get worse, platform walls will tighten, and your own memory layer becomes a strategic asset.
- **Question**: How should valuable public datasets be monetized?\
  **Answer**: Sell the decision or workflow they enable, not the dataset. Hedge funds, journalists, NBFCs, and consultants pay when data becomes a ready answer or recurring output.
- **Question**: Are AI-ready chunks themselves the product?\
  **Answer**: They are a powerful intermediate asset, not the end. The value comes when someone downstream can create stories, decisions, diligence, products, or workflows from them.
- **Question**: How should we think about monetizing Claude skills or MCP-driven expertise?\
  **Answer**: The mechanism is still open. Skills are reusable intelligence packaged as files, but marketplaces and payment rails are not yet settled.
- **Question**: Should AI data products pursue B2C microtransactions?\
  **Answer**: Be careful. B2C is hard without the right market and distribution; casual problems need very low friction or bundling, while urgent problems can command price.
- **Question**: Will agents become a marketplace like MCP connectors?\
  **Answer**: Maybe not. Agents may behave more like software or harnesses that users lock into; connectors, skills, and sub-agents may blur underneath.
- **Question**: What is the deeper pattern behind managed care using AI and health managers?\
  **Answer**: It converts a transactional service into a relationship service. That pattern repeats in wealth, health, and any domain where context compounds.
- **Question**: Should we retrain health models on Indian data just because the current data is Western-heavy?\
  **Answer**: Treat it as a hypothesis. If validation is cheap through hospital partners and resident doctors, test lightly before heavy retraining.
- **Question**: What does a forward deployed engineer actually do?\
  **Answer**: An embedded person with client data and AI access finds use cases, solves them, and sends evidence-backed actions. The leap is from proposal to recurring output.
- **Question**: Whose agenda does the FDE serve—the account manager or the client?\
  **Answer**: In our working version, it started bottom-up. The embedded person levels up and creates value; the account manager discovers the opportunity after the fact.
- **Question**: What profile makes a good FDE?\
  **Answer**: I don’t know reliably. Curiosity and initiative matter more than title; my expected winner was not the person who actually succeeded.
- **Question**: Do we need clean client data before showing FDE value?\
  **Answer**: No. Use public data, synthetic data, transcripts, or context to move the bottleneck one step forward. Then ask for real data with proof in hand.
- **Question**: How can domain experts and AI/data teams work together?\
  **Answer**: Pair data/tech people with subject experts. The subject expert owns the problem, the central team accelerates execution, and over time the expert becomes hands-on.
- **Question**: How do we map the human-AI workforce by solution category?\
  **Answer**: Start with task categories and AI exposure. Use benchmarks plus your own transcripts, emails, and chats to estimate which work is AI-prone, AI-safe, and skill-constrained.
- **Question**: Where does AI’s economic value show up after automating one step?\
  **Answer**: At the shifted bottleneck. If AI speeds first-round hiring, the hiring-manager interview becomes the constraint; measure value at the new constraint.
- **Question**: What is underexplored in enterprise data use cases?\
  **Answer**: Cross-domain joins. HR plus procurement, employee plus vendor, CRM plus finance—connecting domains surfaces risks and opportunities no silo sees.
- **Question**: How should agents be brought into meetings?\
  **Answer**: They need not speak. A human can act as interface: transcribe the meeting, feed responses to an agent, analyze live, and bring insight back into the room.
- **Question**: Is AI workload optimization a niche?\
  **Answer**: Not for long. Wherever a harness can verify outputs automatically—code, math, robotics, simulations—AI companies will accelerate and the telemetry/optimization layer becomes strategic.
- **Question**: What should an AI-fluent mentoring organization learn next?\
  **Answer**: Move beyond tool fluency into operating models: coding agents as build partners, AI-native delivery, enterprise deployability, guardrails, token economics, and evals.

## Week ending 14 Jun 2026 {#week-ending-2026-06-14}

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

## Week ending 07 Jun 2026 {#week-ending-2026-06-07}

- **Question**: Who should attend the AI data stories workshop?\
  **Answer**: Everyone is welcome. The focus is how to get AI to tell data stories, and participants should have paid ChatGPT or Claude so it is hands-on.
- **Question**: When I can show anomalies and root causes, what should a forward deployed engineer actually deliver?\
  **Answer**: Don’t give me a tool, report, or “ability to analyze.” Tell me the action: these two agents cause the maximum problem, train or replace them, and here is the evidence.
- **Question**: Why do we need a CLI if we already have drag-and-drop or an API for publishing static reports?\
  **Answer**: The API is enough technically. The CLI reduces variation when five people or CI/CD jobs regenerate and publish outputs in different ways.
- **Question**: How should we handle infrastructure for sending tens of thousands of AI-personalized emails?\
  **Answer**: Don’t optimize prematurely. Send good emails to 80 or 200 people first, validate quality and compliance, then solve for 10,000 if the value is proven.
- **Question**: What happens after the FDE discovery and first moment of truth?\
  **Answer**: Move into discovery inventory, then execution and rinse-repeat. The point is not just to identify use cases; it is to keep solving them and turning the working patterns into capability.
- **Question**: Is the first agentic output just a broad design, not deployment?\
  **Answer**: Yes. What I described is the agentification of design. Deploy, maintain, continuously improve, and scale are separate phases with different bottlenecks and different agentic techniques.
- **Question**: Why is the agent approach different from just starting to use LLMs?\
  **Answer**: Gen 1 was writing code around LLM calls. Gen 2 was using LLMs for complex steps but still orchestrating everything yourself. Gen 3 is letting the agent/harness orchestrate the work.
- **Question**: Should we explain Gen 1, Gen 2, Gen 3 agent architecture to clients?\
  **Answer**: No. That is internal language. Externally, talk outcomes and workflows; internally, tell teams to start developing this way.
- **Question**: What is deployed AI?\
  **Answer**: It is not just a model or a demo. It is an agent or workflow connected to production systems, transaction data, verification, governance, KPIs, reporting, and human review where needed.
- **Question**: What enterprise architecture makes agents easier to deploy?\
  **Answer**: A registry of available data, tools, systems, and permissions. Once agents know what they can access and how, deployment becomes more like giving capabilities than building everything again.
- **Question**: How should I use your time on an AI productivity initiative?\
  **Answer**: Don’t give me status updates. Ask me a question where I can help; if I need context from the team, I’ll ask for it.
- **Question**: What organizational AI mindset shift are you wrestling with?\
  **Answer**: Moving teams from LLM API to harness, from CLI to MCP, and from software to outcomes. If a client’s intern can build the software in six hours, the value must be the business output, not the code.
- **Question**: How should we train a software developer shifting into GenAI prototype work?\
  **Answer**: Have him solve TDS once with a coding agent, then train harness configurability: hooks, plugins, workflows, sub-agents and shared skills. Also train use-case discovery and SME validation.
- **Question**: Are browser agents doing the same thing as turning websites into tools?\
  **Answer**: Yes. Treat browsers, APIs, command-line tools, action models, and specialized models as tools; the harness becomes the shell that pipes them together.
- **Question**: How should executives be introduced to AI before jumping into use cases?\
  **Answer**: Start with personal use, then citizen use, then enterprise use. Workshops beat trainings: make them solve something useful the same day so AI stops being abstract or threatening.
- **Question**: In the FDE model, who identifies the problems - the SME or AI?\
  **Answer**: Both, but AI does most of the first draft. The SME gives business context and prompts; the agent scans data and documents, proposes use cases, and should then solve them, not just list them.
- **Question**: Should you personally build the AI demos for the client?\
  **Answer**: No. The team should build them with Claude Code; I’ll help only when they hit challenges. Me building a demo gives a fish, not the fishing muscle we need to scale.
- **Question**: How are you using AI personally and what kinds of problems are worth solving?\
  **Answer**: I maintain an AI Bottlenecks log: every stuck, bored, overloaded, or messy moment becomes input. Ask AI how to solve it with AI, then turn the solution into an asset that compounds.
- **Question**: Are enterprises making a mistake by treating AI as just LLMs?\
  **Answer**: Yes. Upgrade the mental model from “LLM” to “harness”: the harness orchestrates tools, LLM APIs, deterministic computation, actions, governance, and eventually other model types.
- **Question**: Should we enforce a specific output format like a web app when asking agents to solve business problems?\
  **Answer**: Solve the problem first. Most end-users do not want a dashboard; they want a trusted answer in English that tells them what to do and why.
- **Question**: How should we scope an AI POC when the client wants data architecture, KPIs, code and semantic layers quickly?\
  **Answer**: Record the walkthroughs and make only a soft commit until you see the data. Ask what their own product manager would deliver from the same inputs, then deliver it faster and better.
- **Question**: How do we enable the whole team to get up to speed with AI?\
  **Answer**: Make everyone produce proactive AI-generated output useful to the client within a month. Review what worked, then convert repeated patterns into prompts, scripts, verifiers, access recipes, and shared assets.
- **Question**: What should I do when AI helps build something but I get stuck at the next deployment or review step?\
  **Answer**: Treat every stuck point as the next AI prompt. Write the bottleneck down, ask AI how to remove it, and spend your learning time only where AI still cannot help.
- **Question**: Is there any stable ground while AI tools and enterprise architectures keep shifting?\
  **Answer**: Yes: evals and test cases. Treat code and harness choices as depreciating assets; workflows matter more, and evals are the thing worth specifying.
- **Question**: How do we build robust AI systems when the technology keeps changing?\
  **Answer**: Shorten the payback period brutally. Don’t chase a feature that takes three months; use what is on a platter, build replaceably, and invest only when it pays back fast.
- **Question**: Should we solve production-scale reliability before committing to a new agent framework like ADK?\
  **Answer**: Only if the solution is easy now. If scaling, refactoring, or latency are not solvable on a platter, don’t burn months; let technical debt accumulate and build so components can be replaced later.
- **Question**: At what level should we abstract AI services from provider or agent-platform choices?\
  **Answer**: Ask at every decision: what happens when this is deprecated? Flexibility now means planning for model, harness, provider, and architecture replacement.
- **Question**: Should we invest in a separate traditional eval platform for AI systems?\
  **Answer**: Maybe premature. Benchmark creation is now cheap with coding agents; generic evals are thin, specific evals are specific, and continuous evals matter most once the system is in operations.
- **Question**: How do I get started when an AI problem looks too big?\
  **Answer**: Log exactly where you are stuck, paste that into AI, and iterate until one manual cycle works. Then automate that cycle and move the bottleneck forward.
- **Question**: If you were a forward deployed engineer today, what would you actually do?\
  **Answer**: Enter the client environment, inspect the data and digital exhaust, ask agents what problems stakeholders likely have, solve one, and send a “do this because of this” recommendation with evidence.

## Week ending 31 May 2026 {#week-ending-2026-05-31}

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

## Week ending 24 May 2026 {#week-ending-2026-05-24}

- **Question**: How do you give Claude and ChatGPT the same context?\
  **Answer**: Manually first. Type in one, paste into the other, attach the same files. Crude, but it works.
- **Question**: How do you structure prompts well?\
  **Answer**: Don't over-engineer. Write roughly, reuse, tweak when it fails, and store what you repeat.
- **Question**: How do you use AI to improve prompts?\
  **Answer**: Run post-mortems over conversations: what prompt would have improved this? Then simplify because post-mortems overfit and models change, making micro-changes less useful than broad intent.
- **Question**: What is MCP?\
  **Answer**: Model Context Protocol exposes tools and programs so agents can use them. Powerful, but not beginner material for a 2-minute explanation.
- **Question**: What are skills or SKILL.md?\
  **Answer**: On-demand permanent prompts. Use them for expert workflows where the base model typically fails out-of-box.
- **Question**: Once stored, do skills become context?\
  **Answer**: Yes, on demand. The model sees skill names and descriptions, then loads the right skill only when relevant.
- **Question**: How do you protect against hallucinations?\
  **Answer**: Make outputs falsifiable. Ask for evidence, quotes, links, checklists, tests, samples and independent challenge; use one model to red-team another.
- **Question**: Why do models get worse in long chats?\
  **Answer**: "Context rot" is known behavior. Start a new chat and carry forward a summary, memory or copied context.
- **Question**: Why can't ChatGPT retrieve old answers from memory/search?\
  **Answer**: You're probably not doing anything wrong. Chat search is weak; don't treat chat history as a serious knowledge system. Rename chats with keywords and search.
- **Question**: Are wrappers above LLMs a superior way to use AI?\
  **Answer**: Yes. They're called harnesses. ChatGPT and Codex are harnesses on top of the GPT models. Raw models are intelligence; harnesses give them tools, files, memory and workflows.
- **Question**: Which engineering domains look most ripe for AI?\
  **Answer**: Manufacturing, electronics and PCB design, 3D printing, CAD, and civil. Anything codified in software with an API or MCP-like control surface becomes automatable.
- **Question**: Why is engineering so ripe for AI?\
  **Answer**: The codification of engineering. Once the work already happens inside controllable software, an agent can observe, operate, and iterate.
- **Question**: Is a PhD topic safe when AI progress makes work obsolete so fast?\
  **Answer**: The bar has moved. What was a PhD three years ago may now be a freshman-with-AI project; choose bigger, faster, more foundational problems.
- **Question**: If AI can code and simulate, what are engineers and designers supposed to do?\
  **Answer**: Teach delegation. Give students problems where AI is unavoidable; they learn what to hand off and where the human jagged edge remains.
- **Question**: Is synthetic data versus real data the right framing?\
  **Answer**: No. Treat it as a continuum: start with real data, jitter it using realistic behavioral rules, and use synthetic edge cases to stress-test models.
- **Question**: What metric tells us whether an AI answer is good?\
  **Answer**: Three checks: are the inputs enough to answer, does (LLM) rubric think the answer is good, and ultimately, do the end users like it and find it useful?
- **Question**: What AI tools should we start using?\
  **Answer**: Just a few ChatGPT Plus ($20) monthly subscriptions are a good start. Don't buy specialized tools or annual licenses until people prove usage and value.
- **Question**: There is a lot of pressure on us to do AI; how should we explore what is possible personally and professionally?\
  **Answer**: Workshop mode, not discussion mode. Get hands-on, do real tasks, and feel what is possible and what is not.
- **Question**: If we double-check across five agents, is it one LLM with five methods or different models?\
  **Answer**: Both work. Same model with different prompts is useful; different models add diversity and usually improve consensus.
- **Question**: If you fire five models, aren't you paying five times per query?\
  **Answer**: Technically yes, but cost is collapsing. Use cheaper models for cross-checking; for most business questions, verification is now cheaper than manual rework.
- **Question**: How do you keep consistency when model versions change?\
  **Answer**: LLM Ops. Run automated eval suites before any model/version switch; don't silently promote a model just because it is new.
- **Question**: What about factual consistency when an LLM confidently gives a wrong answer?\
  **Answer**: Ask it for links with verbatim citations. You can programmatically check if the link and citation exist, and use another LLM to catch bad reasoning.
- **Question**: Should we build the knowledge graph first or start with agents?\
  **Answer**: Parallel. Agents deliver value immediately; knowledge graph and data engineering mature alongside with use.
- **Question**: How does a CTO manage a thousand agents?\
  **Answer**: Not as a thousand apps. Build one agent operating system or enterprise agent platform; each agent is a versioned configuration with registry, evals, observability, rollback and ownership. Azure Agent Registry might be an example.
- **Question**: Should the deliverable be software or the output of the software?\
  **Answer**: Prefer the output of the software. Software is WIP pipeline we keep improving; the client buys an outcome, not a depreciating asset that "their intern can build with Claude Code."
- **Question**: When the model misunderstands a prompt, how do we improve next time?\
  **Answer**: End with a post-mortem prompt: what did you misunderstand, what context was missing, and how should I prompt next time? Store that learning.
- **Question**: How do we decide whether AI-suggested use cases are valuable?\
  **Answer**: Don't sell use cases. Convert them into concrete actions backed by evidence, then email the business asking whether those actions matter.
- **Question**: Should we train custom models for film or design generation?\
  **Answer**: No. Frontier models improve too fast. Start with prompt engineering, reference images, image search, workflow automation, and human review. Train only when there is proprietary data, repeated demand, and a clear advantage - which is almost never.
- **Question**: Is hardware or physical engineering more AI-proof?\
  **Answer**: Better protected. AI accelerates design, simulation, planning, and documentation; physical experimentation, procurement, instrumentation, and validation still need humans.
- **Question**: How should I personally learn AI?\
  **Answer**: Use AI for everything. Record where it fails. That failure log becomes is where human expertise is needed - and is what we should teach.
- **Question**: How can engineering research leverage agentic AI?\
  **Answer**: Use AI to find what to research, do the literature search, do the actual research, write-up the research, verify the research, find publications, revise based on review comments, ... Practically every part of the chain.
- **Question**: Does AI kill creativity?\
  **Answer**: It redefines creativity. What we thought was creativity may die and these are the lower levels, but new higher levels forms emerge.

## Week ending 17 May 2026 {#week-ending-2026-05-17}

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

## Week ending 10 May 2026 {#week-ending-2026-05-10}

- **Question**: What is the "service-as-software" model?\
  **Answer**: Act as the AI yourself first - take the JD, run it through your system, hand them the result - don't make it self-serve until you've proven value.
- **Question**: How can outcomes be sold - I constantly struggle with this?\
  **Answer**: Outcome pricing works when you control the inputs and can measure the output precisely; start with small provable outcomes and expand.
- **Question**: Can you suggest courses to experiment with vibe coding?\
  **Answer**: By the time courses are released models have moved forward; practice and asking AI to teach you are your two best approaches.

## Week ending 03 May 2026 {#week-ending-2026-05-03}

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

## Week ending 26 Apr 2026 {#week-ending-2026-04-26}

- **Question**: How should I look at my career for the next 5-10 years given where AI is going?\
  **Answer**: Focus on skills AI cannot do - judgment, communication, knowing what question to ask - and use AI aggressively for everything else.
- **Question**: What change are you seeing in how kids approach the world differently from how we did?\
  **Answer**: Kids are far less inhibited with AI - they ask weird, creative questions naturally, without the guardrails adults impose on themselves.
- **Question**: How do kids today relate to the concept of truth?\
  **Answer**: Truth has always been a social construct - shaped by village elders, then science, then social media, now AI. It's a shift in authority, not a unique collapse.
- **Question**: Is judging quality of a prompt useful for running a Prompt-a-thon?\
  **Answer**: Evaluating prompts against outcome-based tests is more robust than subjective scoring, which is trivially gamed.

## Week ending 19 Apr 2026 {#week-ending-2026-04-19}

- **Question**: What do you think of serious gaming for AI education?\
  **Answer**: Huge potential, AI will accelerate it, there will be false starts, and it will likely end up in a niche - but like gaming itself, a massive niche.
- **Question**: How do we create a billion dollar business with AI?
- **Question**: Won't AI degrade skills?\
  **Answer**: Yes, but some of those might not matter.
- **Question**: You've mastered delegating work to the AI assistant - how?\
  **Answer**: When you tell people nobody gets it, when you show them some get it, when they do it they get it - get people to share screens and do exercises.
- **Question**: How do I choose between Claude and ChatGPT/Codex for a task?\
  **Answer**: Codex for rigorous verification; Claude for strategy and high-level thinking; Gemini for simpler, conversational answers.

## Week ending 12 Apr 2026 {#week-ending-2026-04-12}

- **Question**: Hallucination is creativity, at some level?\
  **Answer**: In humans we don't call it hallucination, we call it agency or autonomy. Exactly.
- **Question**: How is 25 years into a job mid-career?\
  **Answer**: Feels like starting over - AI is resetting the playing field for everyone regardless of experience.

## Week ending 29 Mar 2026 {#week-ending-2026-03-29}

- **Question**: When I run out of tokens and Claude says "compress now" - does performance go down?\
  **Answer**: The model writes a summary as notes and starts again; you lose something but it may not be important.
- **Question**: Hallucination as creativity - had you thought of that?\
  **Answer**: "Hallucinations are my best source of ideas quite often." Use a weaker model without extended thinking for creative tasks - "Overthinking is for correctness. Speak without thinking is for creativity."
- **Question**: If the AI future is framed positively, will people actively move toward it rather than fear it?\
  **Answer**: Yes - constraint is humans' ability to absorb discomfort, not the technology itself.
- **Question**: Do we really need programming languages anymore?\
  **Answer**: "High-level programming languages have fallen to the level of machine languages. We don't care about the machine language the compiler writes - these are just compilers at a different level."

## Week ending 22 Mar 2026 {#week-ending-2026-03-22}

- **Question**: If I outsource all my creative decisions to AI, am I becoming a lesser version of myself?\
  **Answer**: Cognitive offloading is real - but each generation trades old skills for new ones. Rickshaw pullers were replaced by machines; many found other work.
- **Question**: We must have considered the long-term impact of AI when developing it, right?\
  **Answer**: "No. Who considers long-term impact over money? Or fame? Or power?"
- **Question**: Do you have any critique of this technology - is it all sunshine?\
  **Answer**: "I don't have a problem dying. I'm having fun. If AI wants to kill me, it can. Just shoot me in the back."
- **Question**: Do we have a direction for how to use AI in HR?\
  **Answer**: AI is like a very smart intern with no hands or legs. If you can find a use for an intern in HR, you can find a use for AI.
- **Question**: I've been using NotebookLM to summarize things before reading - am I cheating?\
  **Answer**: Learning comes from effort, not the tool. If your brain is as tired after using the LLM as without it, the learning is there.
- **Question**: For making presentations, which is best - Gemini, Claude, or ChatGPT?\
  **Answer**: Claude makes the best presentations; Gemini does the best research (Google access); ChatGPT does the best analysis.
- **Question**: Is AI change management consulting scalable as a business?\
  **Answer**: Scales only as large as your trusted relationships; relationships become more valuable as AI commoditizes the rest; scalability through product defeats the entire premise.
- **Question**: What is the profile of a person to hire to build a retail AI solution?\
  **Answer**: Any engineer qualifies; the less experience the better; test them live: "sit down, build this solution, one hour."
- **Question**: Who owns the commit - the AI or the developer?\
  **Answer**: Humans know how to assign responsibility for companies, ships, gods, rivers; we haven't learned yet how to do it for agents.
- **Question**: What is the biggest blocker to having AI as part of SDLC?\
  **Answer**: The people - "I am a coder. If AI is going to do my code, what am I?"

## Week ending 15 Mar 2026 {#week-ending-2026-03-15}

- **Question**: How do you share insights during the learning phase - how do you write your blog?\
  **Answer**: Writing is not only for others; the big benefit is clarifying your own thinking; start by putting notes on GitHub.
- **Question**: Who motivates you to do all these workshops?\
  **Answer**: I do it for self-learning; I commit to talks on topics I don't know - the commitment forces the learning.
- **Question**: AGI - within 3-5 years, do you think we'll see it?\
  **Answer**: "I talk to it like a human - that is AGI; we got there last year."
- **Question**: What's the "LLM Psychologist" title about?\
  **Answer**: Nothing to do with psychology formally; Andrej Karpathy coined the term in 2023, it sounded cool, called HR: "Do you have any problem if I call myself LLM Psychologist?"
- **Question**: Starting AI in first year - is it like giving a calculator before learning tables? Won't students become dullards?\
  **Answer**: It's like learning how to use the internet; whoever gets there early has an edge; the bigger risk is underuse, not overuse.
- **Question**: I want to build my own CRM. Is it doable with no coding experience?\
  **Answer**: Why build a CRM at all - upload your Excel to ChatGPT, tell it who to chase, you already have a CRM.
- **Question**: If somebody wanted to build Gramener 2.0 today with LLMs, how would you rebuild it?\
  **Answer**: Moats are based on taste and judgment now; regulation remains; custom software renaissance means services beat SaaS.

## Week ending 08 Mar 2026 {#week-ending-2026-03-08}

- **Question**: If the output is HTML, how do you edit it?\
  **Answer**: You tell it what changes to make - you no longer edit documents, you manage the intelligence that writes them.
- **Question**: What are the invariants that won't change as AI reduces the cost of intelligence?\
  **Answer**: Regulation is a big one; that doesn't change easily.

## Week ending 01 Mar 2026 {#week-ending-2026-03-01}

- **Question**: What AI tool should I use given limited budget?\
  **Answer**: The question "what tool" is wrong; ask "what part of my business drains time but doesn't require my judgment?" - start there.
- **Question**: How do I know when to overrule or underuse AI - I'm worried I'm losing skills?\
  **Answer**: Ask: is the skill I'm losing going up or down in value? Use AI after you attempt the skill yourself; for growing skills, learn first, then use AI as a critique partner.
- **Question**: AI hallucinates during analysis - how can we ensure accuracy?\
  **Answer**: Same as with humans who give wrong answers - ask again, be more specific, ask for evidence, rephrase and check if the answer changes.
- **Question**: How does a research analyst not get scared by AI doing their work?\
  **Answer**: The smart analyst does it quietly, becomes 2x-4x more productive, then uses the lead to shape how things will move.

## Week ending 22 Feb 2026 {#week-ending-2026-02-22}

- **Question**: I'm thinking of a Digital Board Member - an AI who participates in board meetings. What do you think?\
  **Answer**: Great idea in 3-4 years; today LLM latency makes live participation very hard.
- **Question**: How do you build taste?\
  **Answer**: "I can't tell you."
- **Question**: Where will all these people get absorbed when AI takes over their work?\
  **Answer**: Three paths - some go down the economic ladder, some switch to adjacent roles, some move into new roles that didn't exist before.

## Week ending 15 Feb 2026 {#week-ending-2026-02-15}

- **Question**: You found it easy to make the shift from coding to management and back - but was it?\
  **Answer**: Yes, had expected it; coding was his love but couldn't say no to IIM or BCG when offers came.

## Week ending 05 Nov 2023 {#week-ending-2023-11-05}

- **Question**: How do you feel after the acquisition?\
  **Answer**: Grateful

## Week ending 08 Oct 2023 {#week-ending-2023-10-08}

- **Question**: How do you make your talks funny?
- **Question**: Will LLMs make programmers less relevant?

## Week ending 01 Oct 2023 {#week-ending-2023-10-01}

- **Question**: How do you get creative ideas like programming Minecraft with Python?\
  **Answer**: people have told me and creative sense I was a kid. I haven't thought about this. I remember I wrote a play and put together a magic show in grade 7. I think what help me was a low threshold of interest and curiosity that let me to read diverse books. A willingness to experiment and attendance see to combine topics and drive to act may be some factors. I'll write a blog post on this

## Week ending 10 Sep 2023 {#week-ending-2023-09-10}

- **Question**: How do I convince people to use a specific chart, e.g. stacked bar instead of pie?\
  **Answer**: Read up on pros and cons. Ask them to try it out.
- **Question**: Can I hire one person who knows the domain and data science or do I need different people? There are many specializations in data science. Do I need to hire for each separately?

## Week ending 03 Sep 2023 {#week-ending-2023-09-03}

- **Question**: What should I learn next? Power BI in depth? Consulting?\
  **Answer**: Blindspots

## Week ending 27 Aug 2023 {#week-ending-2023-08-27}

- **Question**: How do I prioritise across multiple managers?\
  **Answer**: Pick your bottleneck (time, number of people you can interview, number of JDs, whichever). Monitor and publish it. That lets you allocate it collaboratively.

## Week ending 20 Aug 2023 {#week-ending-2023-08-20}

- **Question**: Is the current AI wave real?\
  **Answer**: Yes. I believe this is the next silver bullet after Excel. Computation by natural language.
- **Question**: How do you manage time?\
  **Answer**: https://s-anand.net/blog/time

## Week ending 06 Aug 2023 {#week-ending-2023-08-06}

- **Question**: My audience wants exploratory dashboards, not stories. What do I do?\
  **Answer**: Exploration is useful for analysts. Use good exploratory tools for that. Non-analysts want the answer. Present stories to them

## Week ending 30 Jul 2023 {#week-ending-2023-07-30}

- **Question**: How do I manage my team?\
  **Answer**: Know and show where to go - that's vision. Know and care about your team - that's leadership. #leadership
- **Question**: What should the design team do?\
  **Answer**: Transform decision making. Your design should change a decision. Better yet, it should change their WAY of thinking into data-driven (that's TRANSFORMing). #leadership
- **Question**: My manager does not appreciate me or let me take initiative. What should I do?\
  **Answer**: Communicate. Wait a day. Open up to your manager and share how you feel. #assertiveness
- **Question**: Should we only pick projects & teams where we can ensure quality?\
  **Answer**: Quantity trumps quality. Work at the edge of competence. Learn from failure. Unless failure is not an option. #leadership
- **Question**: I am not performing well. What should I do?\
  **Answer**: Communicate. Tell your manager how you feel. Ask for help. #assertiveness
