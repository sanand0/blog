---
title: Things I Learned - 08 Nov 2026
date: 2026-11-08T00:00:00+00:00
categories:
  - til
description: I share weekly notes on AI agents, voice tools, website archiving, and optogenetics, including my rising Codex use and a Qwen3-TTS benchmark that reached 32% precision and 84% recall.
tags: [ai-agents, ai-in-education, course-design, text-to-speech]
---

This week, I learned:

- [Facemorph.me](https://facemorph.me/) implements face morphing via [StyleGAN2](https://github.com/NVlabs/stylegan2) (among the best face morphing implementations I've seen) and exposes it via a free public site #ForNow.
- My reading from [The Sequoia of Tomorrow](https://www.linkedin.com/pulse/sequoia-tomorrow-sequoia-jcide): <!-- https://claude.ai/chat/b4b7af3a-32b2-4b84-a921-e67332eb97eb -->
  - Money's in **the Bay Area**. People, move there.
  - Money’s in **a few big winners**. Maybe they can find them easy and don't need to scout?
  - Money's in **speed and fewer deciders**. Partners don't need to wait for and convince each other every Monday. Risky, but faster.
- Looks like you can use Codex via an API, since the [OpenAI Agents 0.22.0-alpha.1](https://github.com/openai/openai-agents-js/releases/tag/v0.22.0-alpha.1) release is available. "This alpha introduces the embedded Codex harness in the OpenAI Agents SDK for JavaScript and TypeScript." Via [Daniel](https://x.com/dani_avila7/status/2118029110282698803)
- The amount I'm delegating to agents is small but growing. In Aug-Sep, a median session took Codex 3.3 minutes and only 4% of my prompts took 20+ minutes. In October, the median session took 7.5 minutes and 13% of my prompts ran 20+ minutes. <!-- https://chatgpt.com/c/6aed535a-42dc-83e8-be4d-41b16fad0a90 -->
- ChatGPT image generation will be a [separate quota from Codex](https://x.com/TokenGremlin/status/2117974085313401330) #ForNow.
- Armin used [Qwen3-TTS to detect voices](https://lucumr.pocoo.org/2026/10/29/qwen3-custom-voices/). I ran a quick benchmark to see how well it did on my transcripts. Answer: Not very good. 32% precision, 84% recall. <!-- https://github.com/sanand0/private-research/tree/main/qwen-diarization -->
- "Professors nowadays seem to have become professional fundraisers who do a little research on the side." Also, "Turning the other cheek turns out to have selfish advantages." [Paul Graham](https://paulgraham.com/top.html)
- Looks like we've learnt how to get a neuron to fire by shining a light on it. It's called [Optogenetics](https://en.wikipedia.org/wiki/Optogenetics).
- Voice remixing is now available in [Gemini 3.8 Flash](https://aistudio.google.com/generate-speech?model=gemini-3.8-flash-tts) and it did a pretty good job of replicating my voice as well as creating new voices based on a prompt. [via X](https://x.com/Google/status/2118027058794148099). [Qwen3-TTS supports custom voices too](https://lucumr.pocoo.org/2026/10/29/qwen3-custom-voices/) and can run on your laptop with just 1.7B parameters.
- This (interestingly summarized) [Machines of Loving Grace](https://tareqistyping.com/prototypes/reading-long-form/) suggests factors that bottleneck intelligence (like in clinical trials, ) - and hence become the focus:
  1. **People** move slowly or impose constraints.
  2. **Data** isn't available.
  3. **Nature** (biology, chemistry, engineering) works only so far.
- [Nathan Baschez sees agents factories as the next step](https://www.gettheleverage.com/p/against-the-personal-agents-theory) beyond "All employees use agents". These are shared workflows maintained centrally that the organization can get work done with. That packages context (skills, prompts, docs, data) along with environment (tools, permissions). The main advantages are centralization (few experts/owners enable everyone) and execution (acting in the real world).
- [WACZ](https://specs.webrecorder.net/wacz/1.1.1/) seems to be the modern way to archive websites. Unlike MHTML, it can handle multiple pages.
- In the last 10 months (Jan-Oct 2026), I prompted Claude, Claude Code, ChatGPT, and Codex about 12,000 times. On average, I talk to AI ~40 times a day. That's 80% of my "Talk to AI 50 times a day" recommendation. I still have some way to go.
- Phone spam marketing has reached an elevated level of obnoxiousness. I get calls from automated recordings often. But today, Airtel Black call me and put **me** on hold for two minutes. Wow! Then the music stopped and the line just hung. So, they put me on hold _and_ ghosted me. And the reason I picked up the call was because their Internet was down - so a triple whammy!
- Not only have I started [enjoying tea](https://www.s-anand.net/blog/a-tea-perspective/) a lot, I quite look forward to it. Even to the point where a high point of my day is when someone serves me tea, unasked. As my daughter commented, I'm getting old.
- [`wacli`](https://github.com/steipete/wacli) is a CLI interface for WhatsApp. Unofficial, and works well #ForNow.
- There's no clear, good, ChatGPT search / export CLI that I am comfortable with #ForNow. [ChatGPT](https://chatgpt.com/share/6ae751be-44a0-83ec-9597-6a1fe7d38542)

## Mistakes I made

[Week ending 08 Nov 2026](https://www.s-anand.net/blog/mistakes-i-made/#week-ending-2026-11-08)

- I said **"If they do it better, then TDS has taught them that skill"** while proposing to measure learning by comparing students' performance on successive questions.\
  **Correction**: Better performance on a later question is evidence of improvement, not proof that the course caused it. Differences in question difficulty, prior knowledge, independent practice, agent assistance, and other factors may explain the change. Establish comparable assessments and use a suitable comparison group or research design before attributing improvement to teaching. [Institute of Education Sciences: Research Design Standards](https://ies.ed.gov/ncee/wwc/glossary).\
  **HIGH · OVERSTATED**
- I said **"the accelerometer tells me how much the phone is moved"** while explaining why measuring distances and reconstructing scenes with a phone should be simple.\
  **Correction**: An accelerometer measures acceleration, not displacement or distance. Estimating motion by integrating acceleration accumulates errors. Reliable mobile augmented reality combines camera observations with inertial measurements and may use depth sensors; distance estimates require suitable visual geometry and calibration. [Android: Motion sensors](https://developer.android.com/develop/sensors-and-location/sensors/sensors_motion); [Google ARCore: Fundamental concepts](https://developers.google.com/ar/develop/fundamentals).\
  **MEDIUM · FALSE**
- I said **"map the approximate meaning of individual neurons"** and **"change the weightage"** of a feature using Gemma Scope while discussing research on controlling LLM behavior.\
  **Correction**: Mechanistic interpretability tools such as Gemma Scope use sparse autoencoders to identify features represented across model activations, not necessarily individual neurons. Individual neurons can encode multiple unrelated features. Feature steering can intervene on activations during inference without changing the model's trained weights. Such interventions can influence behavior, but identifying a feature does not establish a simple, reliable control mechanism. [Google DeepMind: Gemma Scope](https://deepmind.google/blog/gemma-scope-helping-the-safety-community-shed-light-on-the-inner-workings-of-language-models/) · [Neuronpedia: Feature steering](https://docs.neuronpedia.org/sparse-autoencoders/feature-dashboards)\
  **MEDIUM · OVERSTATED**
- I said **"Rambler ... [is] not available via GBoard"** in a weekly learning digest about Android voice typing.\
  **Correction**: Google's Gemini-powered Rambler voice input is built into Gboard on supported Pixel 11-series devices. It requires an updated Gboard and supports limited offline functionality. A separate keyboard application is not required to access Rambler on supported devices. [Google: Rambler voice input on Gboard](https://support.google.com/pixelphone/answer/17468539).\
  **MEDIUM · FALSE**
- I described Clairic as **"a Decision model (or System One model)"** in a technical learning digest.\
  **Correction**: Cloudflare classifies Clairic as a System One extraction model, distinct from decision models such as Clef. Decision models select among predefined choices; Clairic extracts, computes, estimates, or predicts typed values from inputs. Both belong to the broader System One model family. [Cloudflare: Introducing Clairic](https://developers.cloudflare.com/changelog/post/2026-10-19-clairic-workers-ai/).\
  **LOW · FALSE**
- I included **"1923: White chocolate"** in an AI-assisted timeline of chocolate innovations.\
  **Correction**: White chocolate emerged commercially in the 1930s, not 1923. Nestlé dates the launch of Milkybar to 1936 and records the introduction of Galak white chocolate in approximately the same period. [Nestlé: Milkybar history](https://www.nestle.com/brands/food-snacks/milkybar); [Nestlé company history](https://www.nestle.com/about/history/nestle-company-history).\
  **LOW · FALSE**
- I included **"1923: Filled chocolate bars"** in an AI-assisted chronology of confectionery inventions.\
  **Correction**: Filled chocolate confectionery existed decades before 1923. Fry's produced chocolate-coated Cream Sticks in 1853 and launched its mass-produced, fondant-filled Chocolate Cream bar in 1866. [The Chocolate Museum: Fry's history](https://www.thechocolatemuseum.co.uk/week10); [Oxford Companion to Sugar and Sweets: Filled chocolates](https://app.ckbk.com/reference/swee13396c03s001e054/chocolates-filled).\
  **LOW · FALSE**
- I included **"1971: Chocolate eggs (Cadbury Creme Egg)"** in a chronology of chocolate innovations.\
  **Correction**: Chocolate Easter eggs predate 1971: Fry's produced hollow chocolate eggs in 1873, and Cadbury introduced its first chocolate Easter egg in 1875. The year 1971 marks the launch of the specific Cadbury Creme Egg product, not the invention of chocolate eggs. [UK Companies House: History of chocolate eggs](https://companieshouse.blog.gov.uk/2017/04/13/what-uk-company-made-the-first-chocolate-egg/); [Cadbury: Company timeline](https://www.cadbury.co.uk/about/history/timeline/).\
  **LOW · OVERSTATED**

## Questions I was asked

[Week ending 08 Nov 2026](https://www.s-anand.net/blog/questions-i-am-asked/#week-ending-2026-11-08)

- **Question**: How do I get useful feedback on a visualization when the decision-maker has no time? Asked while discussing how to test dashboards intended for busy managers rather than fellow students.\
  **Answer**: People refuse feedback because it takes too long or they don't see the point. Make the task tiny: show two visualizations for 10 seconds, ask which communicates better, then ask why.
- **Question**: How will collaboration work when an adaptive exam gives every student different questions? Asked while designing an exam whose difficulty and next question depend on individual performance.\
  **Answer**: Weaken collaboration, but don't destroy it. Add real-time challenges where several students enter a virtual room and must accomplish something together. They can bring agents, but coordinating with other humans becomes essential.
- **Question**: Are we measuring what the student learned or merely what AI helped the student accomplish? Asked while planning to compare students' performance on repeated skills across assignments.\
  **Answer**: Be precise about what learning we claim. The unit of learning may be the student plus their agent, context files, tools, and social network. If someone builds resources that make them consistently more capable, that may be a valid learning outcome even when the knowledge isn't entirely in their head.
- **Question**: How do we measure whether students have learned to combine skills, rather than merely solve individual questions? Asked while reviewing longitudinal exam results for Docker, APIs, and other technical skills.\
  **Answer**: Mine existing assignments for questions combining three or four earlier skills, then compare the same students' performance. Better still, deliberately design later questions to measure transfer. Don't just test whether they learned Docker; test whether they can use Docker, APIs, and other skills together.
- **Question**: How do we explain what students are learning when an AI-native course has no fixed syllabus? Asked after students complained that they couldn't predict the questions or describe what they'd learn.\
  **Answer**: If I can structurally, deterministically train you in something, why wouldn't I train a model instead? Most courses teach known skills that agents may eat up. This course explores where you can create value that agents cannot yet replace.
- **Question**: Can we use AI instead of humans to evaluate whether a visualization communicates correctly? Asked while comparing ways to test visualizations, including simulated audiences and adversarial interpretation.\
  **Answer**: No, not as a complete substitute. Agents perceive things differently. Humans unanimously recognized a drawing as a donkey while models guessed cow, sheep, or horse; the reverse happened with an owl. Use AI to generate failure cases, independently recalculate data, and suggest alternative designs. Still test with humans.
- **Question**: How do we teach communication skills when the person who builds something is often not the person who presents it? Asked while discussing students who produce excellent projects but struggle to explain or sell them.\
  **Answer**: I'm experimenting with letting students publish services and sell them to each other for credits—anything from data cleaning to helping with an exam. They must find customers and negotiate. The design needs work: some students trade credits without actually delivering anything.
- **Question**: How do you preserve human interaction when AI makes you increasingly self-sufficient? Asked after observing that working extensively with Claude had made him more isolated from colleagues.\
  **Answer**: I have the same problem. Conversation is an agent-era-proof skill, so I use agents to strengthen it. Every week, I ask one to review my conversations, identify people I should thank and why, and then I send those messages.
- **Question**: How can multiple agents work together on the same task? Asked after seeing an AI-agent swarm collaborate and comparing it with his single Claude assistant.\
  **Answer**: Start with one agent running hourly: read pending.txt, finish whatever it can, add new work, and mark anything blocked. Put another agent on a different machine and give them a shared folder or request queue with clear boundaries. Let them exchange work directly. Remove the human relay and you've got a swarm.
- **Question**: How do people build agents that book flights and do things without being prompted each time? Asked after demonstrating several AI-built internal applications and hearing about personal agents.\
  **Answer**: Telling Claude to book a flight is just using Claude. The interesting part is what it does unprompted. Schedule it to scan your context daily: what have I promised but not delivered? What commitments from others are pending? What possibilities am I missing? That's a way of expanding ambition, not merely automating tasks.
- **Question**: Can AI reliably follow our existing presentation design, or should we let it create its own? Asked while reviewing AI-generated investment-banking presentations that still needed manual design work.\
  **Answer**: Separate instruction-following from design. I'd trust ChatGPT more to preserve a supplied template while changing only the words, and Claude more to invent a good chart without a sample. Don't insist on one agent: have one produce the deck and another interrogate it for mistakes.
- **Question**: How can I trust a RAG benchmark when the LLM itself generates the test questions? Asked while comparing reranking, agentic RAG, and knowledge graphs on financial filings.\
  **Answer**: Start with the audience and the decision they need to make. An IT director should immediately recognize the questions as representative. Classify them by what the infrastructure must do—lookup, comparison, searching across documents, inference—and test roughly six questions per pattern. Keep the questions short enough to understand at a glance.
- **Question**: How do we design an AI-permitted exam question that a shared solver won't make trivial for everyone? Asked while proposing questions that interrupt an agent's reasoning or alter instructions embedded in attached files.\
  **Answer**: Changing just a number or phrase won't work; one student can build a solver and share it. Personalize the actual reasoning problem, not merely its parameters. I want many students to learn how to use agents cleverly—not one student solving everything, and not a question so hard that almost nobody learns.
- **Question**: If agents can build software so cheaply, what does a product manager do? Asked after discussing a custom drawing app built in minutes and a conventional product pilot that took nine months.\
  **Answer**: Maybe there's only one software now: agents. The product manager discovers users' needs and workflows, gives agents the right context and tools, and sets up the feedback system. Log everything, read the logs, decide what to change, and optimize. Building that data-driven decision system may be more valuable than building the application.
- **Question**: What can programmers learn from managers about the constant context switching caused by running many agents? Asked after describing how checking idle agents and parallel tasks was destroying his flow state.\
  **Answer**: Management is a useful analogy. Learn how to specify, verify, delegate, and manage an intelligence that may know more than you. Also study patent clerks, judges, auditors, and detectives: they've developed ways to make decisions despite incomplete information and experts knowing more than they do.
- **Question**: Who will pay for software when anyone can build their own with AI? Asked while discussing inexpensive personal software, liquid software, and the declining scarcity of programming.\
  **Answer**: Software may become liquid: people modify and fork applications for their own needs. Things consumed by agents can increasingly be packaged and optimized as products. Services may tilt towards the performing arts—not literally, but towards human performance sold to a human audience. The commercial models are still unclear.
