---
title: Things I Learned - 18 Oct 2026
date: 2026-10-18T00:00:00+00:00
categories:
  - til
description: 'I share what I learned this week: agents can control Android phones, fingerprints identify browsers in Incognito, AI software cloning may erode consumer moats, and LLM capability is widening unevenly.'
tags: [ai-agents, claude-code, software-engineering, social-engineering]
---

This week, I learned:

- I tested a few tools that help agents work with mobile devices. On Android, apart from `adb`, [mobile-mcp](https://github.com/mobile-next/mobile-mcp) seems better than [Android-MCP](https://github.com/CursorTouch/Android-MCP) or [mobilerun](https://github.com/droidrun/mobilerun) (which has a different purpose, though) #ForNow. More importantly, agents controlling mobiles with USB debugging seems quite seamless.
- [HeyPuter is cloning every software](https://github.com/HeyPuter/everything) #ForNow into open-source apps. I expect more people will do this. Consumer software moats will probably erode faster than enterprise software (which has regulatory and other moats).
- [My colleague built his own mobile music player](https://www.mynkpdr.in/posts/my-own-music-player-no-ads/) yesterday using Claude Code and [rea](https://github.com/morluto/rea/) to reverse engineer the YMusic APK. Another example of technically capable users building their own (disposable) software.
- [Fingerprints are the new cookies](https://royfish.dev/fingerprints-are-the-new-cookies). I was surprised to see that the server could identify me correctly even in Incognito mode. [Cover your tracks](https://coveryourtracks.eff.org/) lets you test your browser privacy and mine was unique among ~369K users. My user agent, system fonts, [Canvas fingerprint](https://browserleaks.com/canvas), [WebGL fingerprint](https://browserleaks.com/webgl), audio compression float differences, WebGL Vendor & Renderer, and HTTP Accept Headers were the biggest unique-ness identifiers..
- [Thinking will become a hobby](https://www.spinellis.gr/blog/20261008/). Interesting point. After all, with the mechanical revolution, exercise became a hobby. (Interestingly, schools teach very little exercise - or most other hobbies.)
- Claude Code just told me that "Version 1.0.10 was published only 2 days ago, so to be supply-chain cautious I'll pick a release that's at least 2 weeks old." That's pretty circumspect of it - and I learnt a new term: "supply-chain caution".
- Paraphrasing [Andrej Karpathy](https://x.com/karpathy/status/2109361546505966046): LLM capability is *widening* - something I'm seeing in my interactions, too #ForNow.
  - 75% of the population has barely seen LLMs.
  - 20% are free-tier users (searching, writing, maybe booking a flight) who see occasional use.
  - 0.2% see large, complex projects one-shotted: apps, math proofs, ...
  - ~5,000 people see swarms of thousands of agents collaborating over weeks on software mega projects: minting zero days, running cyber attacks and defenses at machine speeds, discovering new science, advancing the frontier of mathematics. Human review and comprehension are falling behind: "archeology" of the OpenAI-HF incident, studying the 722 OpenAI proofs...
  - That's because we don't have a reservoir of big, difficult problems we really care about; and the jagged edge: digital, verifiable and economically valuable domains grow faster; and access is uneven: free-tier, paid-tier, internal.
- [Cloudflare acquired Deno](https://blog.cloudflare.com/deno-joins-cloudflare/). "After that year we will end our development of the Deno runtime." Good for Cloudflare, pity about Deno. It was a good kick in the rear for NodeJS. Ryan'll be porting [celld](https://celld.dev/) into [workerd](https://github.com/cloudflare/workerd). What I learnt is: <!-- https://chatgpt.com/c/6acb7db7-4a34-83ec-b119-c0bb7d4c4ea1 -->
  1. `workerd` might be a realistic alternative to write web servers - instead of NodeJS, Express, etc.
  2. [Durable Objects](https://developers.cloudflare.com/durable-objects/concepts/what-are-durable-objects/) (worker + storage) seem to be a more powerful infrastructure component than I thought. They're powering [Queues](https://blog.cloudflare.com/how-we-built-cloudflare-queues/), [Workers](https://blog.cloudflare.com/building-workflows-durable-execution-on-workers/), [Git storage (artifacts)](https://developers.cloudflare.com/artifacts/), and more.
- [Wallhop](https://wallhop.io/) lets you skip paywalls #ForNow. [Built by Josh](https://news.ycombinator.com/item?id=50038634) as a 12ft.io replacement forking [everywall/ladder](http://github.com/everywall/ladder).
- From [How Anthropic Builds And How Engineering Will Change Soon | Thariq Shihipar](https://youtu.be/2Kch3tWMnw8):
  - Examples - especially personal examples - are still an excellent way to prompt models.
  - Agents do what the typical user wants _pretty_ well. Focus your personalizations on how you want things done _differently_ from the typical user.
  - Learn vocabulary and intuition in areas where AI needs help. Visual design, mathematical ideation, economic theory, ...
  - Things move so fast (at least in code) #ForNow, so plan to deliver value within a month or two. For longer projects, wait for the next generation of agents to change the economics.

## Mistakes I made

[Week ending 18 Oct 2026](https://www.s-anand.net/blog/mistakes-i-made/#week-ending-2026-10-18)

- I said **"483 millimeter cube... 4.3 centimeter cube"** while recommending human-readable units for engineering benchmarks.\
  **Correction**: 483 cubic millimetres equals 0.483 cubic centimetres, not 4.3 cubic centimetres. Cubic units require cubing the linear conversion factor: 1 cm³ = 1,000 mm³.\
  **LOW · FALSE**
- I said **"a full-fledged Photoshop clone"** while describing AI-built Rust replacements for Adobe applications.\
  **Correction**: PhotoCraft is an open-source, clean-room Photoshop-style editor written in Rust, but it remains early-alpha software, not a full professional Photoshop replacement. Its maintainers identify missing generative features, approximately 20 tools, advanced typography workflows, and plug-in compatibility. The wider ArtCraft suite likewise does not establish feature parity with every Adobe application. [PhotoCraft project](https://github.com/storytold/photocraft)\
  **MEDIUM · OVERSTATED**
- I said **"Poor man's RoBERTa"** to describe BM25 while explaining retrieval algorithms.\
  **Correction**: BM25 is a lexical information-retrieval ranking function based on term frequency, inverse document frequency, and document-length normalization. RoBERTa is a pretrained Transformer language model that can be fine-tuned for classification and other tasks. They are not cheaper and more expensive versions of the same algorithm; a better comparison is BM25 versus vector or neural retrieval, with RoBERTa treated as a separate modeling component. [Elastic BM25 documentation](https://www.elastic.co/docs/reference/elasticsearch/index-settings/similarity)\
  **MEDIUM · FALSE**
- I said **"have an application running in the background ... it can still control [my phone]"** while describing mobile agents and sensor-based applications.\
  **Correction**: Android supports considerable automation, but background applications cannot freely access every capability. On Android 9 and later, ordinary background apps cannot receive accelerometer and gyroscope events or access the camera and microphone. Supported approaches require appropriate permissions, foreground services, or other authorized mechanisms, and capabilities vary by device and Android version. [Android background sensor restrictions](https://developer.android.com/about/versions/pie/android-9.0-changes-all)\
  **MEDIUM · OVERSTATED**
- I said **"80% more bugs"** while illustrating the cybersecurity implications of doubling code production and reducing the bug rate from 5% to 4%.\
  **Correction**: With 100 units of code at a 5% bug rate, there are five bugs. Doubling output to 200 units at a 4% bug rate produces eight bugs: 60% more, not 80% more. To avoid conflating output growth with security risk, I should also distinguish the count of bugs from the number and severity of exploitable vulnerabilities.\
  **MEDIUM · FALSE**
- I described LMSR as **"Bayesian revision of probabilities"** while explaining a prediction-market exercise.\
  **Correction**: The Logarithmic Market Scoring Rule is an automated market-making mechanism. Trades change outstanding share quantities, and the market maker mechanically recalculates prices using a logarithmic cost function and its derivatives. The resulting prices can be interpreted as market-implied probabilities, but this is not itself Bayesian posterior updating from a specified prior and likelihood. [LMSR mathematics](https://mechanisms.microprediction.org/mechanisms/lmsr.html)\
  **MEDIUM · FALSE**
- I said **"When _you_ approach others, you don't have to [be careful]"** while explaining social-engineering defenses at a cybersecurity session.\
  **Correction**: Initiating contact reduces some unsolicited-contact risks, but it does not establish authenticity or eliminate the need for caution. Scammers place fake support numbers and websites in search results, causing victims to initiate contact themselves. I should verify destinations through known official websites, applications, or trusted contact details, regardless of who initiates the interaction. [FTC: fraudulent search results](https://consumer.ftc.gov/consumer-alerts/2025/04/online-search-results-good-bad-scammy)\
  **HIGH · OVERSTATED**
- I said **"Now I just tell the agent to fix the bug. It becomes easy"** while discussing responses to cybersecurity vulnerabilities, including replacing dependencies or building a unikernel.\
  **Correction**: Coding agents can accelerate investigating and proposing security patches, but a generated patch must still be checked for correctness, regressions, and security weaknesses. A unikernel is a specialized operating-system image, not an automatic replacement for any vulnerable operating system. Security-sensitive fixes require appropriate independent validation before deployment. [OWASP secure coding with AI](https://cheatsheetseries.owasp.org/cheatsheets/Secure_Coding_with_AI_Cheat_Sheet.html) [Unikernels](https://unikernel.org/)\
  **HIGH · OVERSTATED**
- I said **"agents are actually a fancy term for a pre-created prompt"** while teaching people to build Microsoft 365 Copilot agents.\
  **Correction**: A simple declarative agent can begin with reusable instructions, but Microsoft 365 Copilot agents also define knowledge sources, actions, connectors, skills, permissions, and other capabilities. A saved prompt is one possible component of an agent, not an adequate definition of agents generally. [Microsoft: declarative agents](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/overview-declarative-agent)\
  **MEDIUM · OVERSTATED**
- I said **"your identity is an agent-proof skill"** while discussing recorded-voice and family-interaction educational exercises.\
  **Correction**: Requiring personal participation and real-world interaction can make assignments harder to outsource to agents, but a recorded voice alone does not prove authentic human participation. Modern voice-cloning systems can imitate a person's speech from short recordings. Assessments requiring identity assurance need additional safeguards or supervised interaction rather than assuming voice is agent-proof. [FTC voice-cloning warning](https://consumer.ftc.gov/articles/scammers-use-fake-emergencies-steal-your-money)\
  **MEDIUM · OVERSTATED**
- I said **"The Fed ... finally cut [rates] on 16th September"** while demonstrating a scorecard comparing financial institutions' interest-rate forecasts.\
  **Correction**: On 16 September 2026, the US Federal Reserve raised its target federal funds rate by 25 basis points, to a range of 3.75%–4.00%; it did not cut rates. Any forecast scorecard treating a September rate cut as the realized outcome must be corrected and its forecast-accuracy conclusions recalculated. [Federal Reserve FOMC statement, 16 September 2026](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm)\
  **HIGH · FALSE**

## Questions I was asked

[Week ending 18 Oct 2026](https://www.s-anand.net/blog/questions-i-am-asked/#week-ending-2026-10-18)

- **Question**: If agents can solve the hard assignments, what happens to the other 95% of students? Asked while I explained my agent-resistant IIT Madras exams and token prediction market.\
  **Answer**: Intelligence is not that important anymore. Cooperation, negotiation, dealing with uncertainty and risk matter. An agent can predict token consumption, but students can talk to classmates, gather information and influence what happens.
- **Question**: From an employee's perspective, what does responsible AI look like in daily work? Asked during cybersecurity audience questions about accountability for AI-generated work.\
  **Answer**: Imagine a new employee reporting to you who totally goofs up. Responsible AI is saying, "My mistake," and making sure it doesn't happen again—not saying, "AI goofed up."
- **Question**: How should business, AI risk and security leaders work together on responsible adoption? Asked after discussing how AI increases both delivery speed and exposure to cyberattacks.\
  **Answer**: Tier decisions by risk and reversibility. Delegate low-risk decisions and tolerate mistakes. Turn absolute prohibitions, like sending client data to the wrong person, into automated blocks. Use AI and human judgment together for the middle.
- **Question**: How should we protect ourselves against AI-powered social engineering and deepfakes? Asked after examples of impersonated executives requesting payments and malicious instructions targeting agents.\
  **Answer**: The old rules remain: be more careful when someone approaches you, and be suspicious if something looks too good to be true. Two newer practices: switch communication channels to verify identity, and set spending limits on cards, API keys and anything else that can be drawn down.
- **Question**: What does responsible AI adoption mean for our business, and how should we judge success? Asked while opening a cybersecurity panel on balancing AI-driven productivity with reliability.\
  **Answer**: If AI doubles output from 100 to 200, mistakes must not double from five to ten. Ideally, even the absolute number of mistakes should fall. Put more effort into verification, red-teaming and defenses, and know when something is only a prototype.
- **Question**: Why not use a Codex plugin in Blender to generate engineering drawings? Asked after seeing an agent produce a visually convincing CAD model with structural errors.\
  **Answer**: Blender is right for generating 3D visuals, not necessarily production CAD drawings. Manufacturing needs information about materials, weight and structure that goes beyond appearance.
- **Question**: Should I let the agent choose how to solve a task, or specify the programming language and method? Asked after a data-lineage agent proposed Python while examining files containing only table-level lineage.\
  **Answer**: Who knows better? If you know something the agent doesn't—like which language IT will allow you to deploy—tell it. Otherwise, let it decide. Even with 35 years of programming experience, I'm increasingly letting agents choose.
- **Question**: Why tell an agent to use Python instead of letting it do the calculation itself? Asked during a live Copilot experiment involving multiplication of large numbers.\
  **Answer**: Write code when you want repeated reliable work; use the model's intelligence for higher-level reasoning. It may calculate a big multiplication correctly once, but a program can repeat the calculation a thousand times without introducing new arithmetic errors.
- **Question**: Why do Copilot agents give different answers to the same question? Is it randomness or personal history? Asked after participants noticed inconsistent outputs while repeating agent tasks.\
  **Answer**: Both. The base model can produce different answers to identical prompts. Copilot also supplies its own instructions and selected personal context, so your Copilot may respond differently from mine.
- **Question**: How should we grade an agent-assisted project where students gather invoices distributed across other students? Asked while designing assessment criteria for a collaborative information-sourcing assignment.\
  **Answer**: Grade like an auditor. Consider the value of missing invoices, the number of missing entries and the consequences of the errors, rather than prescribing one solution strategy.
- **Question**: What learning outcomes are these unusual, agent-permitted projects meant to achieve? Asked after I proposed invoice trading, a token prediction market and a game rewarding unusual correct answers.\
  **Answer**: Three things: strategize how to source information when you don't know where it resides; make and revise predictions as evidence changes; and push an agent away from the average answer while retaining correctness.
