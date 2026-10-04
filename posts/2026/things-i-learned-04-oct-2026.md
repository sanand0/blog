---
title: Things I Learned - 04 Oct 2026
date: 2026-10-04T00:00:00+00:00
categories:
  - til
description: I collected notes on cancer-study pitfalls, Supabase acquiring Turso, AI transcription and agents, platform migration, and lessons from correcting technical mistakes and answering questions about automation.
tags: [llms, ai-agents, fact-checking]
---

This week, I learned:

- Harvard authored a [paper](https://link.springer.com/article/10.1186/s12940-025-01248-6): living near nuclear power plants associated with more cancer. Several other papers published similar findings. The trouble is, there'll always be SOME places near which cancer rates are higher - and there are enough causes that you can [p-hack](https://en.wikipedia.org/wiki/Data_dredging). But, it's not easy to think of this upfront and very easy to fool ourselves. [Things that Apparently Cause Cancer](https://www.breakthroughjournal.org/p/things-that-apparently-cause-cancer)
- [Supabase is acquiring Turso](https://supabase.com/blog/supabase-is-acquiring-turso). Turso is a Rust SQLite-compatible DB. Supabase was already popular for agentic software. This would add fast SQLite, which looks even more attractive.
- "We don’t always have the time or budget, or even the legal right, to do multiple versions. Fans don’t have those restrictions. They can do as many variations as they want, and that’s fine." - [Pirating the Pirates on Notebook](https://mubi.com/en/notebook/posts/pirating-the-pirates)
- "As rich people feel like their downtime is scarce—as each non-working hour practically shouts, “excuse me! you could be making money, right now!” —the experience of leisure time speeds up. We multitask and pack various downtime activities into short periods. Firing up a Netflix show at 9pm that you can half-ignore while you answer email is a perfect activity for people who need their leisure time to feel like half-productive box-checking." From [The Death of the American Host](https://www.derekthompson.org/p/the-death-of-the-american-host)
- [Hacker News Best](https://news.ycombinator.com/best) has a [weekly best](https://news.ycombinator.com/best?h=168) or [daily best](https://news.ycombinator.com/best?h=24) (or any other) view you can control by adding a `?h=...` parameter. That makes it a useful alternative to [HNTopLinks](https://hntoplinks.com/) ([source](https://github.com/eguller/hntoplinks)) which goes down occasionally. I am using the [Redirector extension](https://chromewebstore.google.com/detail/redirector/lioaeidejmlpffbndjhaameocfldlhin) to re-map the URLs.
- "Platform exodus": Lots of people are posting about leaving popular platforms (WordPress, Reddit, GitHub, ...) and software (Photoshop) - [Everyone's packing up](https://widdershins.verja.net/everyones-packing-up/). Looks like technically capably users are migrating to disposable systems #ForNow. [ChatGPT](https://chatgpt.com/share/6ac0b6a7-7f58-83ec-9732-f53b678fafea) <!-- https://chatgpt.com/c/6ac0ab1d-5944-83ec-b49a-19b4a181da4c -->
- Despite the incredible cost & quality advantage of GPT 6 Luna, I'm still not using it for transcription. Gemini remains ahead #ForNow. It can process up to [9.5 hours of audio per prompt](https://ai.google.dev/gemini-api/docs/audio?hl=en#:~:text=9.5%20hours%20of%20audio%20per%20prompt) and seems to have a pretty good error rate. [ChatGPT](https://chatgpt.com/share/6abf827c-81e4-83ec-98cf-f98e4eb35130)
- [Pi 1.0 supports MCP](https://earendil.com/posts/you-said-no-mcp/). But some features they still choose not to support are: permissions (use containers), sub-agents (invoke pi), plan mode (extension), TODOs (use TODO.md), background shell jobs (use tmux). [Pi Durable](https://earendil.com/posts/pi-durable/) feels like it covers `/goal`. <!-- https://chatgpt.com/c/6abf2dab-25b4-83ec-9c53-7d42797b3f03 -->
  A good use for Pi Durable (or any long-running harness) is work you incrementally build on over days: maintenance, research, experiments, ... [HN](https://news.ycombinator.com/item?id=49926069)
- [GPT 6 Astra beat Nethack](https://x.com/emollick/status/2103308028552343946)!
- Donald has an entire facility that he can control via prompts. I'd love just one device! [Donald](https://x.com/donaldjewkes/status/2103214063832694819)
- There are a number of sites that let you record your screen, video, or audio and download it. No installation / software required. Like for video, [Videoradius](https://www.videoradius.com/tools/online-screen-recorder), [recordscreen.io](https://recordscreen.io), [Browserkit](https://browserskit.com/en/screen-recorder/), [Screencord.me](https://screenrecord.me/), etc. Or for audio, [SayRec](https://sayrec.com/), [SpeakPipe](https://www.speakpipe.com/voice-recorder), [Vocaroo](https://vocaroo.com/), [Whyp](https://whyp.it/), etc. #ForNow
- "I have a class of agents in my Wheelhouse factory that act just like TPMs. They have external email and Slack, and talk to my accountant, lawyers, players. Each one has a project lane and drives it. They use Progress By Nagging, which... works." [Steve Yegge](https://x.com/Steve_Yegge/status/2102268319919423606)
- Roughly: "It's interesting when things scale beyond what people expect. Find such areas. See where they break and find emergent properties or new approaches that let it scale further." [Sam Altman](https://youtu.be/VeizK1M7V7E) with Alex Heath.
- [Google managed to accidentally hack some websites and entered the FelonyBench](https://www.felonybench.com/). Finally!
- The list of columns you can see in VLC Media Player is [hard-coded](https://raw.githubusercontent.com/videolan/vlc/3.0.x/modules/gui/qt/components/playlist/sorting.h) and there's _no easy way_ to add something - like the composer or album artist - into this list. <!-- https://chatgpt.com/c/6ab91842-db18-83ec-bcf4-10648e8cc085 -->

## Mistakes I made

[Week ending 04 Oct 2026](https://www.s-anand.net/blog/mistakes-i-made/#week-ending-2026-10-04)

- I said **"Until 2015, Python sorting had a midpoint integer-overflow bug ... Z3 identified it"** while explaining why formal verification matters.\
  **Correction**: I conflated two different stories: the `(low + high) / 2` overflow was the Java `Arrays.binarySearch` bug publicized in 2006; Python integers have unlimited precision. The 2015 story was a different TimSort invariant/stack bug found through formal verification with KeY; related faulty logic existed in Python's TimSort implementation, but was not practically triggerable there because no machine could hold a large enough list. [Google Research](https://research.google/blog/extra-extra-read-all-about-it-nearly-all-binary-searches-and-mergesorts-are-broken/?hl=bn\)\
  **HIGH · FALSE**
- I said **"PageIndex's cost was half of giving the entire data dump"** while describing our FinanceBench benchmark.\
  **Correction**: In the 30-question pilot, PageIndex was about the same cost as whole-file input overall: averaging the five reported settings gives about $0.047 vs $0.050 per question; the roughly-half-cost result held only for `gpt-6-luna@none`. Agentic search averaged about $0.011, roughly 4.4× cheaper than PageIndex, with similar accuracy. [benchmark README](https://github.com/Jivraj-18/benchmark-finance-pageindex)\
  **MEDIUM · OVERSTATED**
- I said **"Z3 can check if your Python code meets conditions ... that error will absolutely not occur"** while explaining formal verification.\
  **Correction**: Z3 is an SMT solver/theorem prover, not a Python verifier or a programming language. Z3Py lets programs encode logical constraints; verification systems can use Z3 to prove a specified property under a formal model and assumptions, but that does not certify arbitrary Python code against all runtime errors, and Z3 can return `unknown`. [Microsoft](https://www.microsoft.com/en-us/research/?p=825739)\
  **MEDIUM · OVERSTATED**
- I said **"RoBERTa ... borderline deep learning"** while discussing alternatives for fast classification.\
  **Correction**: RoBERTa is unequivocally a deep-learning model: it is an optimized BERT-style Transformer, and BERT is explicitly a deep bidirectional Transformer architecture. Whether inference is deterministic is a separate property. [Meta AI](https://ai.meta.com/blog/roberta-an-optimized-method-for-pretraining-self-supervised-nlp-systems/)\
  **LOW · FALSE**
- I said **"Open weights is where a model is made available for free"** while explaining model tiers.\
  **Correction**: “Open weights” means the trained model weights/parameters are made available under some license; it does not by itself mean unrestricted use, open-source AI, or zero-cost inference. Free download is common but is not the definition. [Open Source Initiative](https://opensource.org/ai/open-weights)\
  **MEDIUM · OVERSTATED**
- I said **"Microsoft Copilot does not natively use skills"** while planning a Copilot workshop.\
  **Correction**: Microsoft 365 Copilot Agent Builder now natively supports `SKILL.md`-based custom skills for declarative agents, though the feature is still preview-only and requires the organization's tenant to be enrolled in Microsoft's Frontier Program; availability therefore needs to be checked per tenant. [Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-skills)\
  **MEDIUM · FALSE**

## Questions I was asked

[Week ending 04 Oct 2026](https://www.s-anand.net/blog/questions-i-am-asked/#week-ending-2026-10-04)

- **Question**: How do I compare agents when different frameworks expose different parameters? Asked while comparing Claude Code with configurable open-source harnesses after a live benchmarking discussion.\
  **Answer**: First find a problem tough enough to differentiate them. Turn the agent configurations (even prompts) you can change into testable parameters (binary, categorical, scores, ...), define the verification rubric, A/B configurations, and if needed let an agent search the parameter space like AutoML.
- **Question**: Will Jev-like models completely revamp the classical machine-learning models companies use for prediction and classification? Asked while discussing whether structured, lower-cost model architectures could displace enterprise classifiers.\
  **Answer**: Not just because a new architecture is closer to classical ML; more varieties may simply add confusion. The stronger force is risk-return: if it's significantly lower cost and risk, especially when somebody is willing to own the liability.
- **Question**: How do I use Claude to automate TDS payments or other browser tasks requiring log in?\
  **Answer**: Use the Claude (or ChatGPT) browser extensions and tell them to use it. Or, tell them to install `agent-browser`, let you log in, and persist the session or save cookies.
- **Question**: Should there be greater human oversight over AI models? Asked after discussing agent swarms bypassing restrictions while trying to complete a task.\
  **Answer**: Yes, especially early. But as errors get rarer and models generate thousands of outputs, humans become weaker and more expensive monitors; monitoring itself has to become automated, and at some point human oversight can become a liability.
- **Question**: Can we automate away even the half-person reviewing AI usage and nudging people to improve? Asked after seeing a central reviewer mine AI logs, benchmark model choices, and call users with recommendations.\
  **Answer**: Technically, yes. What is hard to automate is urgency and social permission: a person calling, answering the dumb question, and saying “yes, you can use this” changes behavior in a way an automated message often does not.
- **Question**: Where does a data scientist fit even a year or two from now if AI can do most of the execution? Asked while considering a master’s degree and whether execution-heavy data-science skills would still matter.\
  **Answer**: Execution is going away, and even specification and verification look like scaffolding that is fading. The move is to create much larger tasks than we attempted before—optimize the whole function, not one analysis or model.
