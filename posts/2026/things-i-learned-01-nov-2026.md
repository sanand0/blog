---
title: Things I Learned - 01 Nov 2026
date: 2026-11-01T00:00:00+00:00
categories:
  - til
description: I learned about AI agents, ChatGPT and Codex limits, lightweight extraction models, and ruby chocolate, while correcting overstatements about LLM memory, software cloning, and scientific reproducibility.
tags: [ai-agents, agentic-workflows, llms, llm-evaluation]
---

This week, I learned:

- Enterprise software migration seems a massive medium term opportunity - [Ethan Mollick](https://x.com/emollick/status/2116526543346483419). On the other hand, [liquid software](https://x.com/patrickc/status/2116636967517798672) where anyone can tweak their own softare is emerging.
- "But I’m not working for my agent, it works for me. It’s a computer. It’s not a person I have to keep busy and keep managing (and checking it’s managing it’s own agents)." - [Ben Tossell](https://www.bensbites.com/p/ai-is-overwhelming-and-im-doing-it)
- OpenAI [announced](https://help.openai.com/en/articles/20001625-understanding-chatgpt-and-codex-usage-limits) that ChatGPT Chat (except Instant) will start getting metered from December 2026. This is a big deal for me because:
  - I prefer ChatGPT Chat / Work to Codex because it can access my past conversations. <!-- https://chatgpt.com/c/6ae47a43-2824-83ec-b334-74293aca74a0 -->
  - Chat (in my ChatGPT $20 Plus) isn't metered visibly and feels unlimited.
  - By giving ChatGPT a plugin to control my computer, I get most of the benefits of Codex.
  - But this free use will last only a month. I need to see how well [GPT 6.1 Terra](https://developers.openai.com/api/docs/models/gpt-6.1-terra) fills that gap - i.e. is it good enough to beat GPT 6 Sol and cheap enough that I can run my chats without worrying about exhausting limits?
- [Clairic](https://blog.cloudflare.com/clairic-extraction-model/) is an extraction model from Cloudflare. It's a Decision model (or System One model) like Jev: fast and lightweight. But this focuses on _extraction_ of text, numbers, dates, even forecasts. It provides the confidence as well as input position of the text for reference.
- Anthropic recommends [using the main agent rather than subagents](https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop). Single agents on smart models work well unless you need independence #ForNow.
- [Ruby chocolate](https://en.wikipedia.org/wiki/Ruby_chocolate) is the fourth variety of chocolate - alongside dark, milk, and white. (Might be a marketing claim than verified.) I tasted it. It's fruity, slightly sour, not bad. My order of preference among the melted chocolates I tasted in a spoon at [Chocolate Nation, Antwerp](https://chocolatenation.be/en):
  1. **Gold**. Caramel toffee butter cream . Delightful!
  2. **White W2**. White chocolate. Something I usually enjoy. I was surprised I liked Gold more.
  3. **823**. Milk cocoa caramel chocolate. Slightly darker.
  4. **Power 41**. 41% cocoa Caramel with less sugar.
  5. **Ruby**. Fruity sour taste.
  6. **Arriba**. Strong cocoa flavor.
  7. **811**. Bitter.
  8. The rest were too bitter
- I had no idea there was so much innovation in chocolates. Most of the ones I like are a century old. Good to see some revival in the last decade. [ChatGPT](https://chatgpt.com/share/6ae37d51-a0e8-83ec-8cba-b5d2e891d719) <!-- https://chatgpt.com/c/6ae371ee-72b4-83ec-9ed2-b7e11a835350 -->
  - 1880s: Truffles. chocolate that melts immediately in the mouth.
  - 1907: Hershey's Kisses.
  - 1908: Toblerone.
  - 1912: Pralines. chocolate shell with creamy filling.
  - 1920: Chocolate-coated ice cream (like Magnum).
  - 1923: Filled chocolate bars.
  - 1923: Nougat-caramel chocolate bars (like Five Star, Mars).
  - 1923: White chocolate.
  - 1926: Chocolate syrup (Hershey's).
  - 1928: Peanut butter cups : Combined sweet chocolate with salty, savory peanut butter for a striking flavor and texture contrast.
  - 1932: Chocolate oranges.
  - 1935: Aerated chocolate with tiny air bubbles.
  - 1935: Chocolate-coated wafers (KitKat).
  - 1936: Malted chocolate balls (Maltesers)
  - 1949: Soft-melting chocolate centers (Lindor)
  - 1951: Chocolate-hazelnut spread (eventually Nutella)
  - 1969: Spherical filled chocolates (Lindor)
  - 1971: Chocolate eggs (Cadbury Creme Egg)
  - 2012: Blond chocolate: white chocolate with biscuit and toffee notes.
  - 2017: Ruby chocolate: pink, fruity, sour.
  - 2021: Dubai chocolate: Pistachio cream, cruncy.
- Looks like [GPT 6.1 Terra](https://openai.com/index/introducing-gpt-6-1-terra/) is mostly as good as Sol but cheaper. I haven't tested it yet.
- On one hand, [modern CSS has several new features](https://www.joshwcomeau.com/css/interop-2027/). On the other hand, I've stopped writing code and delegated it to agents, so this is of no use to me. Instead, what I should be thinking about is: what new patterns does this enable, and what should I be asking for in prompts?
- [Ethan Mollick](https://x.com/emollick/status/2114503849826549842): "Ask yourself: "how do I make what I am doing even more ambitious?" Something to practice actively, given the growing abilities of agents.
- Anthropic is comfortable that no single person has an architectural view of Claude Code. I guess architecture is also being taken over by agents. [Addy Osmani](https://x.com/addyosmani/status/2114604912520921136): "No member of the team has a full mental model of Claude Code in their head, nor do we think anyone needs to. Rather, when anyone wants to learn about a piece of the codebase, they ask Claude to generate an explainer about that exact slice. It only takes a few minutes and the explainer is always up to date."
- Good advice from [Thornton Bell](https://x.com/thorstenball/status/2114386050638336082)
  - Humans write for humans. Agents for agents.
  - Be more ambitious.
  - Give it more eyes - logs, observability, ...
  - Code on remote machines.
  - Ask for 5 variations. (I'm not doing enough of this yet.)
  - Use schedules and triggers. (I'm not doing this at all, so far.)
- Codex introduced an experimental #ForNow `--enable instant_interrupt` flag that looks promising. It's still steering, i.e. not instantly stopping any existing requests or tasks (hence wasting effort), but doesn't wait for the entire response either. Not sure how it works but I just enabled it and will evaluate it. [Code-mode yielding PR](https://github.com/openai/codex/pull/48135), [model-response preemption PR](https://github.com/openai/codex/pull/48141).
- In Codex you can `@`-mention another Codex session. That'll give it access to an earlier session's context. In the past, I copy-pasted session transcripts, saved them in files, or pointed Codex at the session directory. This is more convenient.
- [PixelBoard](https://github.com/Akshayykadam/PixelBoard) has pretty impressive cvoice typing. Google has a Gemini-powered "Rambler" voice recognition system (based on Gemini 3.5 Translate, with offline fallback) on Android phones, but not available via GBoard. PixelBoard enables that. [ChatGPT](https://chatgpt.com/share/6ade1a28-faf0-83ec-a3b5-35d20b35a3ee)

## Mistakes I made

[Week ending 01 Nov 2026](https://www.s-anand.net/blog/mistakes-i-made/#week-ending-2026-11-01)

- I said **"LLMs can probably remember 20, 30 things. If you give them 1,000 things, they will almost certainly forget"** while discussing spreadsheet classification.\
  **Correction**: LLMs do not have a fixed memory ceiling of 20–30 items. Modern long-context models can process thousands of examples or records within a single prompt. However, accuracy depends on the model, context length, task complexity, and number of items requiring attention. For classifying 1,000 records, I should compare direct prompting, batched classification, and embedding-based classification against a human-labeled sample rather than assume direct prompting will fail. [Google: Long context](https://ai.google.dev/gemini-api/docs/long-context) · [OpenAI: Optimizing LLM accuracy](https://developers.openai.com/api/docs/guides/optimizing-llm-accuracy)\
  **MEDIUM · FALSE**
- I described drawing by tilting a mobile phone as **"Your mobile phone's tilting as a Gyroscope basically"** while discussing an educational exercise.\
  **Correction**: A gyroscope measures angular velocity, not absolute tilt. Phone orientation is typically obtained through sensor fusion using the accelerometer, gyroscope, and sometimes magnetometer. An accelerometer can estimate tilt relative to gravity when the device is stationary; a gyroscope helps track rotation. For a browser-based tilt-drawing exercise, DeviceOrientationEvent exposes orientation angles, rather than raw gyroscope readings. [Android: Motion sensors](https://developer.android.com/develop/sensors-and-location/sensors/sensors_motion) · [MDN: Device orientation](https://developer.mozilla.org/en-US/docs/Web/API/DeviceOrientationEvent)\
  **LOW · OVERSTATED**
- I said **"the entire suite of Autodesk, Microsoft, Corel, Adobe ... every piece of software has been pretty much cloned within the span of 1 month"** while discussing the declining value of traditional software.\
  **Correction**: AI-assisted open-source projects have rapidly reproduced substantial parts of several established applications, but the entire commercial suites have not been faithfully cloned in a month. For example, PhotoCraft explicitly describes itself as early-alpha software, not yet a professional Photoshop replacement, with missing tools, generative features, typography workflows, and plug-in compatibility. Repository existence, feature checklists, and working demonstrations do not establish feature parity, production reliability, or replacement readiness. I should describe this as rapid progress in recreating software capabilities, not wholesale replacement of entire product suites. [PhotoCraft: Project status](https://github.com/storytold/photocraft)\
  **HIGH · FALSE**
- I said **"Figma themselves have ported the bulk of Figma ... Figma itself is now available ... inside ChatGPT"** rather than merely being controlled through ChatGPT.\
  **Correction**: Figma has an official ChatGPT integration that can generate embedded previews and create editable FigJam diagrams and Figma Slides presentations. Figma's documentation explicitly says the integration does not currently create files for its other products, including the main Figma Design editor. Users generally open generated files in Figma for further editing. This is a useful integration, not the bulk of Figma running inside ChatGPT. [Figma: Use ChatGPT with Figma](https://help.figma.com/hc/en-us/articles/35326636109975-Use-ChatGPT-with-Figma) · [OpenAI: Figma plugin](https://openai.com/business/plugins/figma/)\
  **MEDIUM · FALSE**
- I said **"Cost and quality, it trumps RAG like crazy"** while recommending agentic search over retrieval-augmented generation.\
  **Correction**: Agentic search performed well in particular experiments, but it has not been demonstrated to universally outperform RAG on both cost and accuracy. Our earlier retrieval comparison involved a limited test set and unequal access to source material, while the larger agentic-search experiment was separate. These cannot establish general superiority. RAG costs also vary substantially with embedding models, index architecture, storage, query volumes, and infrastructure. I should present agentic search as a promising alternative and compare approaches using the same corpus, questions, accuracy criteria, and end-to-end costs. [Retrieval benchmark](https://hrmiitm.github.io/sfd-test/) · [AWS: RAG cost considerations](https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-an-aws-vector-database-for-rag-use-cases/cost.html) · [OpenAI: Optimizing LLM accuracy](https://developers.openai.com/api/docs/guides/optimizing-llm-accuracy)\
  **MEDIUM · OVERSTATED**
- I said **"both Apple and Google for iOS and Android released a developer kit right up front"** while comparing mobile app ecosystems with AI platforms.\
  **Correction**: Apple did not release a native iPhone SDK when the iPhone launched in June 2007. Initially, Apple supported third-party applications through web technologies. The native iPhone SDK was released in beta on 6 March 2008, more than eight months after the original iPhone launched. Android adopted a more developer-oriented strategy earlier in its rollout. The two platforms therefore followed different paths toward third-party applications. [Apple: June 2007 web applications announcement](https://www.apple.com/newsroom/2007/06/11iPhone-to-Support-Third-Party-Web-2-0-Applications/) · [Apple: March 2008 iPhone SDK announcement](https://www.apple.com/newsroom/2008/03/06Apple-Announces-iPhone-2-0-Software-Beta/)\
  **LOW · FALSE**
- I said **"tricking AI is much harder"** and **"AI is not going to be fooled by bad designs of many sorts, but humans are"** while proposing visualization assignments.\
  **Correction**: Multimodal models can also be fooled by misleading charts, and may perform substantially worse than humans on visual reasoning. In the NeurIPS 2025 ChartMuseum benchmark, humans achieved 93% accuracy versus 63% for the best evaluated model. Research on deceptive charts also finds that leading models remain vulnerable to manipulated axes, layouts, and visual encodings. I should design the exercise to discover which representations fool humans, AI, both, or neither, rather than assume AI is harder to fool. [ChartMuseum, NeurIPS 2025](https://papers.nips.cc/paper_files/paper/2025/hash/ca20efa9cf3703186d91424cf4876f8b-Abstract-Datasets_and_Benchmarks_Track.html) · [VisDeception benchmark](https://arxiv.org/abs/2607.22600)\
  **MEDIUM · OVERSTATED**
- I said **"the model can then evaluate the novelty factor through the research"** while proposing that students invent a chart format nobody has created before.\
  **Correction**: An AI research agent can find precedents and compare a proposed chart with known visualization techniques, but its inability to find a similar chart does not establish that the design is unprecedented. Even a formal prior-art search is not conclusive proof of novelty. I should assess documented differences from the closest examples found, the usefulness of the design, and how thoroughly precedents were searched, rather than certify absolute originality. [European Patent Office: Novelty and prior art](https://www.epo.org/en/learning/learning-resources-profile/business-and-ip-managers/inventors-handbook/novelty-and-prior-art)\
  **LOW · OVERSTATED**
- I said **"AI can ... check scientific claims by actually reproducing them"** while circulating an experiment in scientific-paper reproduction.\
  **Correction**: The demonstrated agents test computational reproducibility: whether they can reconstruct reported numerical results from the original data and described methods. That is valuable evidence about analytical transparency and reproducibility, but it does not establish whether the underlying scientific claims are true. Reproducing results does not independently validate the data, experimental design, causal conclusions, or generalizability. The National Academies explicitly distinguishes computational reproducibility, replication with new data, and scientific validity. I should describe the demonstration as an automated computational-reproducibility check, not general scientific claim verification. [National Academies: Reproducibility and Replicability in Science](https://www.ncbi.nlm.nih.gov/books/NBK547531/) · [Original experiment](https://jivraj-18.github.io/agentic-reproduction/)\
  **MEDIUM · OVERSTATED**

## Questions I was asked

[Week ending 01 Nov 2026](https://www.s-anand.net/blog/questions-i-am-asked/#week-ending-2026-11-01)

- **Question**: Why are mobile phones particularly interesting for AI-built applications? Asked after I described how much more ambitious my experiments had become by connecting agents to Android phones.\
  **Answer**: Accelerometers and gyroscopes are remarkably good. Phones also have touchscreens, cameras that are much easier to point anywhere than laptop cameras, microphones, and a huge installed base. With a cable and USB debugging, agents can now access all of this remarkably easily.
- **Question**: What will the commercial model be for software companies when their applications become plugins inside AI platforms? Asked while discussing Figma inside ChatGPT and how AI threatens conventional software businesses.\
  **Answer**: My guess is something like the iOS App Store. Software companies get distribution to a much larger audience and can eventually charge subscriptions or extra for AI-enabled features. But people can also build the software themselves with AI, so the plugin ecosystem is questionable. Enterprises may still pay for someone they can trust.
- **Question**: Isn't Responsible AI becoming a clichéd theme? Can we still show innovative demos under it? Asked after considering Responsible AI as the unifying story for a managerial CIO audience.\
  **Answer**: Yes, we can show demos under Responsible AI. At a managerial level, people will probably prefer safety as a topic over possibility. A developer audience would be different.
- **Question**: How can we grade a data visualization project without spending hours manually evaluating subjective answers? Asked after a 40-student chart-analysis quiz had taken weeks to grade and while replacing part of the final examination with a project.\
  **Answer**: Give students small, testable challenges. For example, create a chart that humans and AI both interpret correctly, then one that fools humans but not AI. Use fixed questions, five-second human interpretation tests, and AI evaluation to measure the results. Students should use agents to do the work; our grading effort should be negligible.
- **Question**: Should we let students choose their own applications when inventing new visualization formats? Asked while designing a project that tests creativity rather than routine chart generation.\
  **Answer**: Yes. Ask them to invent a chart format nobody has seen and explain the specific situation where it's useful. Use AI deep research to judge whether it's genuinely novel, then test its usefulness: can someone understand it in 30 seconds? Novelty alone isn't enough.
- **Question**: How should we evaluate whether a lightweight open-source video generation framework can replace an existing one? Asked after reproducing one HyperFrames benchmark task and comparing its output with Remotion and a golden reference.\
  **Answer**: Try three to five more, quite different tasks. Compare quality with blind judgments, how reliably an agent produces working videos without fixes, and cost and speed including setup overhead. Don't rely entirely on HeyGen's judge when the benchmark comes from HeyGen. Show where each approach wins and fails, then recommend when to use which. No need to run all 50 tasks.
