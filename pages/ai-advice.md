---
title: AI Advice
date: 2026-02-08T23:04:11+08:00
---

Here's AI advice I generally give people.

## How do I use AI better personally?

<!-- 8 Feb 2026: https://gemini.google.com/app/0af513e27b022fa7 -->

- **Buy a paid AI subscription of [ChatGPT](https://chatgpt.com/pricing), [Claude](https://claude.com/pricing), or [Gemini](https://gemini.google/subscriptions/)** for quality and privacy.
  The frontier models are much better than the free models, and your data isn't used to train the models. This is the best $20/month you can spend.
- **Have 50 conversations a day with AI**. High-usage forces you to find tiny use-cases you'd otherwise ignore.
- **If you don't know what to ask, have it interview you.** Ask the AI to _interview_ you to find out what you want, and then do it for you.
- **You've hired an intern**. Don't treat it like a search engine. It's as smart as a post-graduate intern - smarter than the average professional in many domains. Give it bigger tasks. Verify its work and correct it ("You missed this part, try again.")
- **Use it for validation**. LLMs can make mistakes, but using it to fact-check books, articles, emails, your work, etc. is safe and effective.
- **Have AI cross-check AI**. Ask it to find all the mistakes it made and give you citations. Have another AI find all the errors. They're pretty good at that.
- **Ask for easier output**. You spend a lot of time validating or implementing AI output. Have AI structure so it's easy for you to review or do. Your time is the bottleneck. Easy beats best.
- **Use voice mode on mobile** to talk to the AI while walking or thinking. "Ramble" at the AI - it can structure your thoughts. This capitalizes on dead time (e.g. commuting) and also lets you dump context and thoughts faster than you type.
- **Vibe code your own software**. As a non-technical person, build apps to solve your own problems. Don't learn to code. Just tell AI tools what you want and have them build it.
- **Have it write code to process numbers**. LLMs are bad at math but good at writing code. Tell it to write code to analyze numbers instead of answering directly.
- **Have it rewrite your prompts (meta-prompting)**. If you aren't getting the results you want, have it tell you what's missing and rewrite your prompt for you.

Here are specific ideas you can try:

- **Mine your digital exhaust**. Export your WhatsApp chats, journal entries, email logs, fitness data, bank statements, etc. and feed them to an LLM. Ask it to find patterns in your behavior, identify your blind spots, or summarize your year.
- **Repurpose content and data**. <!-- TODO -->
- **Read papers, books, and attachments**. Have it rewrite in the style of your favorite author (e.g. Malcolm Gladwell) to make dry content more engaging. Add "ELI15" (Explain Like I'm 15) for simplicity.
- **Use it when stuck**. When you hit a mental wall, use it as a thinking partner. Have it give a first draft, ask it to interview you, ask what an expert or a person you admire would do, or just ramble your thoughts to it.
- **Hire an expert**. It has been trained on the entire Internet and all books. You can hire it as a personal financial advisor, career coach, relationship counselor, or fitness trainer, and more. For example, hire as a:
  - **Doctor**. Have it summarize your health history, identify gaps, and suggest questions to ask your doctor.
  - **Detective**. Ask it to find out what happened to a long-lost friend or what a client has been up to.
  - **Financial advisor**. Ask it to interview your about your finances, goals, and risk tolerance, then research a personalized investment plan.
  - **Relationship Architect**. Ask it whom to reach out to, find their interests, what gifts to buy, etc.
  - **Teacher**. Ask AI to teach, then quiz you. "I want to learn about [Topic]. Explain the basics, then ask me 3 questions to test if I understood it."

## How do I use AI for coding?

<!-- 9 Feb 2026: https://gemini.google.com/app/c4c7af5f52fb9c3b -->

Thoughts on technical use of AI (e.g. in when coding with AI)

- **Vibe code first**. Ask for what you want. Let AI build it. If it works, AND is what you want, AND needs to be maintainable, THEN look at code.
- **Non-coders can code**. Domain experts (e.g. HR, Finance, etc.) can build their own tools using this way, bypassing traditional IT bottlenecks.
- **Use meta-prompting**. If you need help, ask AI to write and refine your prompt before you use it for the actual coding task.
- **Paste the errors**. When code fails, paste the exact error log or a screenshot into the chat. The model is often its own best debugger.
- **Code is disposable**. Code is an AI compilation artifact. Don't get attached to it. Scrap and re-tsart.
- **The "Two-Strike" Rule**. If it fails to fix a bug after two attempts, abandon the thread and restart. It is often faster with a fresh context than to debug a confused model.
- **Analyze using code**. Ask agents to write code to analyze data. This is more reliable than asking LLMs to analyze directly.
- **Which coding model to use**. Claude / Gemini for good UI. GPT for rigorous testing.
- **Plan unclear tasks**. If your idea is vague or might be too complex, ask AI to write an easy-to-review plan. Scan & correct it. THEN implement.
- **Maintain reference files**. Maintain an up-to-date `AGENTS.md` (or even `README.md`) that explains your intent, code, architecture, to the AI. Saves repeated explanations.
- **Generate tests first**. For maintainable software, have it define tests _first_. That makes working code easier. Often, tests can be 2x the code size.
- **Use Playwright to verify**. Have Playwright take screenshots and inspect DOM elements (e.g. using CDP) to verify frontend work. Saves manual review time.
- **Run post-mortems**. When it fails, or after any session, ask it to analyze what went well, what didn't, and how to improve next time.
- **Specify developer styles**. Ask it to write in the style of a famous developer (e.g. Luke Edwards) or repo (e.g. SciPy) or team (e.g. Astral) that's apt for the task.

## How to increase AI adoption?

<!-- 9 Feb 2026: https://gemini.google.com/app/a1775b6149f6410f -->

Thoughts on the governance of AI (e.g. organization deployment, challenges, etc.)

- **Security & privacy**. Every company has its own white-listed enterprise models (e.g. within Azure, AWS, or Google tenants). Use this. It provides legal cover and data won't be used for training.
- **Keep humans-in-the-loop**. Treat AI like an intern that handles 80-90% of the effort, with a human expert for the "last mile" validation.
- **Keep updating models**. Monitor the ever-shifting "cost-quality frontier" and keep switching to cheaper, better models as they become available. Cost reduces while quality improves.
- **Use consensus to improve accuracy**. Double, triple, or even quintuple-check outputs. If all models agree, accept. Else manual review. This dramatically improves quality while introducing a little human verification overhead.
- **Generate code for reliability**. Instruct LLMs to write and execute deterministic code (or build models) instead of reasoning in plain text.
- **Find AI enthusiasts**. Top-down AI mandates build frustration. Prefer "organic adoption". Find and empower the few enthusiastic "builders" or "power users".
- **Standardize evaluation**. You'll move MUCH faster with evaluation frameworks (like "LLM-as-a-judge") to score model performance and catch regressions.
- **Lay a good data foundation**. Convert unstructured documents into (multiple) structured formats. AI output quality depends on input data quality.
- **Let anyone build tools**. Non-technical "citizen developers" to building their own tools using English, de-bottlenecks IT and dramatically increases prodictivity.
- **Buy, don't build**. Don't train models. They're soon obsolete. Build orchestration layers and proprietary data workflows instead.
- **Prototype rapidly**. Ask for prototypes in days, not weeks. This builds a culture of "rapid experimentation" and lets you cheaply figure out if it's worth it.
- **Audits make reviews simpler**. Ask AI agents to cite sources, provide reasoning, and generate logs. That lets humans to verify how a conclusion was reached.

## What should I learn?

<!-- https://gemini.google.com/app/0fc3ca79c2138048 -->

More important skills:

- **Curiosity**. Our assumptions are obsolete. Practice asking AI: "I thought that's impossible/hard, but is is possible/easy now? How?"
- **How to learn**. Learn how to learn faster. You'll need to learn many subjects quickly (especially to judge AI output).
- **Management**. Shift from doing the work yourself to managing "teams" of AI interns and agents to handle execution.
- **People skills**. Prioritize empathy, negotiation, judgment, and communication are less easy to delegate to AI agents.
- **Style & art**. Learn to guide AI to write, draw, code, etc. in different styles, formats, and approaches for different audiences.
- **Storytelling**. Learn how to guide AI to deliver compelling narratives that move people.
- **Validation**. Learn to review sceptically, verify, and critique AI outputs even when you don't know the domain. (Consultants learn this skill well.)
- **Problem Breakdown**. Learn to breaking problems down into small, logical tasks that people/AI can execute reliably.
- **Prototyping**. Learn to build (and iterate on) the smallest working solution (using AI agents) ultra-rapidly.
- **Context Engineering**. Learn what data/context to feed AI and what you can/should skip for the best results.
- **SQL and Data Organization**. Learn to structure data and write queries (or prompt AI to write them) to make data analyzable.

Less important skills:

- **Coding syntax**. AI can write it.
- **Factual knowledge**. AI can look it up or derive it.
- **Domain depth**. Unless you are (or can become) a top expert, AI can fill in gaps. Focus on _multi-disciplinary_ knowledge instead.
- **Following rules**. AI can implement a process better.
- **Hard work**. Returns are disproportiate. Finding the _right_ problems matters more than solving the lesser problems.
- **Building Models**. AI companies will take care of it.
- **Data wrangling**. AI can handle data engineering, modeling, analysis, and visualization.
- **Tool expertise**. AI can use tools for you.
- **Intermediation**. AI can translate between groups - e.g. business analysts.
- **Originating ideas**. AI can brainstorm ideas. Focus on evaluating and selecting ideas based on unique context.
- **Drafting from Scratch**. The ability to write a first draft (code or text) is less valuable than the ability to edit and refine an AI-generated baseline.
- **Junior-Level Execution**. Routine "grunt work," basic summaries, and entry-level analysis are being fully automated by LLMs.

## How to develop taste?

See [How to develop taste](/blog/how-to-develop-taste/).

## Won't AI erode skills?

<!-- https://gemini.google.com/app/6ef791596112da80 -->

AI, like [most automation, erodes skills](https://link.springer.com/article/10.1007/s00146-025-02422-7). We've seen this before.

- **Autopilots** eroded flying skills - which is dangerous. So we **enforce** flight simulators. Same for surgical knots (robotic surgery), celestial navigation (navy), manual dosing (nurses).
- **Spreadsheets** eroded calculation skills. We **leveled-up** from sums to strategy. Same for CAD, electronic trading, spell-check.
- **Photography** eroded painting skills. We **switched** value to impressionism, cubism, etc. Same for vinyl records, luxury watches, craft coffee.
- **GPS** eroded navigation skills. We **accepted** this and don't care much. Same for phone numbers, spelling, mental maths.

Think about how the skill we lose will evolve. Then enforce, level-up, switch, or accept accordingly.

## What happens to people when AI takes their jobs?

<!--
https://gemini.google.com/app/fbe0628c3f188892
https://chatgpt.com/c/69932b4d-34ec-83a5-b112-fd5ef0bb0199
-->

Here are some paths post-automation. It depends on the industry _and_ individual:

1. **Exit**: Don't adapt. There's no nearby "new task". You're unemployed. E.g. bowling pinsetters -> automatic pinsetters; elevator operators; telephone switchboard operators.
2. **Downgrade**: Serve the machine. Worse job/pay. E.g. textile workers -> power-loom tenders; print compositors -> machine operators; shoemakers -> factory line operatives.
3. **Pivot**: Focus where automation fails (exceptions, trust, coordination). E.g. bank tellers -> relationship managers; travel agents -> corporate travel desks.
4. **Niche**: Treat inefficiency as a feature (soul, authenticity). Small market, high margins. E.g. weaving -> artisan textiles; coffee -> baristas.
5. **Up-Skill**: Master the machine. Become AI-native. Much better job/pay. E.g. human computers -> programmers; draftsmen -> CAD designers; accountants -> advisors.
