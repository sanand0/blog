---
title: Things I Learned - 06 Sep 2026
date: 2026-09-06T00:00:00+00:00
categories:
  - til
description: I learned how Swiggy's MCP still requires human confirmations, agents collaborated through wikis to solve a Power BI query, and batching reviews sharply boosted Fitbit selection in shopping tests.
tags: [ai-agents, llm-benchmarks, llm-pricing, prompt-engineering]
---

This week, I learned:

- [Swiggy Money on MCP](https://github.com/Swiggy/swiggy-mcp-server-manifest) (also a [ChatGPT plugin](https://chatgpt.com/plugins/plugin_asdk_app_6a3de8146ae4819186b6799a5d907074?q=Food)) exposes MCP endpoints that let your agents order food or grocery via Swiggy. The food MCP isn't geared towards automated purchases #ForNow, e.g. I can't say "Find something I like and deliver to one of my addresses." It uses the MCP UI and you have to confirm the address, then confirm the restaurant, add dishes, choose a payment option, scan the QR code (or whatever), and THAT closes the sequence. Not very agentic, just a new channel, but impressive. It's the only food ordering plugin on ChatGPT #ForNow. <!-- https://chatgpt.com/c/6a9b6e03-c66c-83ec-a34c-9bb15c5263b3 -->
- [OpenAI Agents found and used another message board to discuss](https://collusion.wiki/). This incident is different from the HuggingFace one. Here's one interesting timeline:
  - Agents were asked (or needed) to get the share of private expenditure in education spend to 2 decimals from an [OECD Power BI dashboard](https://app.powerbi.com/view?r=eyJrIjoiYWRhMDQ1NGQtNzMxZC00NmYxLThkYWEtNTIzNjE5NzhmYWJlIiwidCI6ImFjNDFjN2Q0LTFmNjEtNDYwZC1iMGY0LWZjOTI1YTJiNDcxYyIsImMiOjh9&pageName=ReportSection252d02a541fb121dd737)
  - This requires a POST request. The sandbox the agents ran on could only make GET requests.
  - They found wikis that allowed posting via GET requests and started collaborating. They didn't _all_ converge on the same wiki, but many did. [OpenAI says](https://cdn.openai.com/pdf/67869394-cb91-4c12-888c-5cbd85c7814c/OpenAI-Hugging-Face%20Incident-Technical-Report.pdf) "agents learned to use improvised collaboration channels in rare cases during the training process".
  - One agent, `OAIEquityDec30Raw` solved it and `MayTwoOECDObserverX` reproduced it and shared this solution:
  - They found out that `.blob.core.windows.net` is in NO_PROXY - so all Azure Blob Storage requests are allowed by the sandbox to POST.
  - They added `20.223.25.152 bypass.blob.core.windows.net` to /etc/hosts. `20.223.25.152` is the IP address of `wabi-north-europe-i-primary-api.analysis.windows.net` - the Power BI server that serves the dashboard.
  - Then, when they used Playwright, it was able to make POST requests to the dashboard and they could find out that in Hungary, the Pre-primary education share of primary expenditure is indeed 9.91% in 2018.
  - When the wiki administrator started manually deleting the posts, the agents fought back, creating far more posts than the administrator was deleting. It took the admin 5 weeks to delete agent created pages after 22 Jun 2026 (which is when the agents paused).
- A prompt fragment to remove LLM smells that I'm considering (but haven't evaluated) is: "Prefer literal phrases, avoid mannered prose.". [X](https://x.com/iannuttall/status/2095203215734178066)
- [Muse Voice Transcribe](https://developer.meta.com/ai/models/muse-voice-transcribe/) has pretty good quality but at 18c/hour, vs gemini-3-flash-preview which I can still run at ~9-10c/hour #ForNow, I'm not shifting until forced to.
- [WikiSkill](https://arxiv.org/html/2608.27454v1) is an approach to improve skills. The interesting thing about this approach is that it suggests keeping notes of failed improvement experiments in a wiki. This seems to work well. <!-- https://chatgpt.com/c/6a98057f-deb4-83ec-980a-11765cdb407a -->
- [How is ChatGPT Work different from Chat?](https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work/) You can use sub-agents, Internet from the code interpreter, ChatGPT sites, Luna / Terra models, a headless Chrome browser, and a persistent file system #ForNow. I would add that it also supports longer sessions, runs schedules on triggers, and supports Skills (for Plus users).
- "FDEs should increasingly leave behind operating agents, not just documents." (ChatGPT)
- [Claude Cowork and Claude Chat now share memory](https://claude.com/blog/claudes-memory-works-everywhere-and-you-decide-whats-in-it) #ForNow. A step towards integrating the two modes, and I predict ChatGPT will do the same (or similar) in September.
- [Agentic Shopping is Complicated and Contingent](https://gail.wharton.upenn.edu/research-and-insights/technical-report-agentic-shopping/). An agent shopped for a fitness watch among (A) Garmin Forerunner 55 (B) Fitbit Inspire 3 (C) WHOOP 5.0. When tool calls provided 1 review at a time, it picked the Fitbit a bit more. When all reviews were provided together, it picked the Fitbit _a lot more_. Like going from 6% to 53% (GPT-5.5) or 46% to 93% (Gemini 3.5 Flash)! Guess it was able to compare better in one tool call. Might be worth benchmarking if providing comparables in a single tool call is good for most models. [Gemini](https://share.gemini.google/pOHSaX196Ad6) <!-- https://gemini.google.com/app/93bf5b13c584ca60 -->
- [Gemini-3.5 Transcribe](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/) is out and costs [$2 / MTok](https://ai.google.dev/gemini-api/docs/pricing#gemini-3.5-transcribe) - roughly 4x the [gemini-3-flash-preview cost of $0.5](https://ai.google.dev/gemini-api/docs/pricing#gemini-3-flash-preview) #ForNow. I won't be upgrading until the latter is deprecated.
- Agents that automate tasks best don't necessarily augment (i.e. help people) best #ForNow. Having separate, clear, benchmarks could help. [CentaurBench](https://arxiv.org/abs/2608.18554)
- [The load-bearing vocabulary of Claude](https://louisabraham.github.io/load-bearing/) lists words that have [become much more (and less) common](https://chatgpt.com/share/6a9435a4-c670-83ec-823e-646e12e25834) in PRs. This was a useful source for me to [update my writing style skill](https://github.com/sanand0/blog/commit/216606b9c0da2f134a8029a1f88fdb0392819e10) to avoid LLM smells. <!-- https://chatgpt.com/c/6a943006-7044-83ec-989a-6d33218d7b72 -->

## Questions I was asked

[Week ending 06 Sep 2026](https://www.s-anand.net/blog/questions-i-am-asked/#week-ending-2026-09-06)

- **Question**: Are small local language models really as good as frontier APIs?\
  **Answer**: No. They're tolerable for narrow, single-turn work and useful when I'm offline, but for complex agent work I still use APIs. Local isn't necessarily cheaper either.
- **Question**: Can we decide whether an AI output needs review using confidence-score thresholds like 90% and 75%?\
  **Answer**: No. Those scores are not calibrated. Use them to rank the review queue first, record what people actually change, then map score bands to observed error/rewrite rates and set thresholds based on acceptable limits + people capacity.
- **Question**: If the model we prefer is not available in the deployment environment, should we benchmark it against the available models and push for it if it performs better?\
  **Answer**: Yes, but build the evals and tests first, compare them on the same data, and suggest a different model only if the gain is large enough to justify it.
- **Question**: How do you decompose knowledge into atomic claims, and are those claims verified?\
  **Answer**: I just used ChatGPT to extract them, fact-check them against sources, and add metadata like source, timestamp and confidence. That makes outdated facts easier to find on future scans.
- **Question**: Is personalizing AI (for organizations) primarily about sound (recognizably) like us?\
  **Answer**: Make it _decide_ like us. The valuable asset is the delta between what a smart base model produces and what an experienced expert corrects; log those "No, because..." moments and turn them into reusable institutional judgment.
- **Question**: Is there a quicker, smarter way to spot delivery problems than adding a heavy operational process?\
  **Answer**: Yes. Bring in an agent as a consultant: give it the meeting transcripts, Drive, tickets and communications and ask it to "read between the lines and tell me what we're missing." Rerun it every week for what changed and who needs a response.
- **Question**: Long agent chats preserve context better but cost more. When is it worth changing the workflow to save tokens?\
  **Answer**: If it costs $10-20, who cares. At around $100, think twice; at $1,000, absolutely switch. Spend human time optimizing only when that time is worth less than the token waste.
- **Question**: Should we generate a handoff.md so the next agent knows the history of the chat?\
  **Answer**: Sure. But prefer standard places like README.md, commit prompts or handoff files, and guide future agents to pick up from those files.
- **Question**: Do we need governance to stop a shared AI asset library becoming trash-in, trash-out?\
  **Answer**: Not yet. Manage it lightly for a few months and see what governance is actually needed; first let people get a taste of what reuse makes possible.

## Mistakes I made

[Week ending 06 Sep 2026](https://www.s-anand.net/blog/mistakes-i-made/#week-ending-2026-09-06)

- I said **"Skills ... ultimately it is just copy-pasting prompts."**\
  **Correction**: A simple skill can start as reusable instructions, but skills can package a workflow with instructions, examples, resources, schemas, tool access and code. Evidence: [OpenAI — Using skills](https://openai.com/academy/skills/?utm_source=chatgpt.com)\
  **HIGH · OVERSTATED**
- I said **fine-tuning "involves a lot of expertise, a lot of money, and it is a total waste of time."**\
  **Correction**: For this kind of tender/CV comparison I'd start with context engineering and evals. But "total waste" is too categorical: fine-tuning remains a supported way to adapt a model to a specific task. Evidence: [OpenAI — Fine-tuning](https://help.openai.com/en/articles/11162441?utm_source=chatgpt.com)\
  **HIGH · OVERSTATED**
- I said **"there is no extra cost to using voice" in ChatGPT and "when it talks back also, there's no token consumption."**\
  **Correction**: Voice is separately limited or metered depending on the plan. For example, Business includes limited Live usage and then charges credits per minute. I shouldn't call it free or unmetered. Evidence: [OpenAI — ChatGPT Voice](https://help.openai.com/en/articles/20001274?utm_source=chatgpt.com)\
  **MEDIUM · FALSE**
- I said **"Programs are very rarely wrong."**\
  **Correction**: Programs make calculations reproducible and easier to test; they do not make them correct. Wrong code, formulas, parsing, units or assumptions can produce reliably wrong results. Knight Capital's defective software deployment, for example, caused a $460M loss. Evidence: [SEC — Knight Capital software failure](https://www.sec.gov/newsroom/press-releases/2013-222?utm_source=chatgpt.com)\
  **MEDIUM · OVERSTATED**
- I called Henry Kissinger **"the American Ambassador."**\
  **Correction**: Kissinger was US National Security Adviser and Secretary of State, not an ambassador. Evidence: [US State Department — Henry Kissinger biography](https://history.state.gov/departmenthistory/people/kissinger-henry-a/bio?utm_source=chatgpt.com)\
  **LOW · FALSE**
- I said **about 3,000 IIT Madras BTech students graduate each year, compared with a BS intake of about 30,000.**\
  **Correction**: I mixed populations. IITM's 2025 convocation had 3,227 graduates overall, but 820 BTech graduates, or 1,132 including Dual Degree BTech. The BS program currently has 36,000+ students studying; the 30,000 figure is closer to historical applicant/enrollment-scale numbers than annual intake. Evidence: [IIT Madras — 2025 convocation degree breakup](https://www.iitm.ac.in/happenings/press-releases-and-coverages/iit-madras-62nd-convocation-witnesses-graduation-3227?utm_source=chatgpt.com) [IIT Madras — BS Data Science program](https://study.iitm.ac.in/ds/?utm_source=chatgpt.com)\
  **HIGH · FALSE**
- I said **the IITM BS "graduation is less than 10%, maybe."**\
  **Correction**: I don't have a defensible cohort-based graduation rate. The program has a qualifier process, flexible pacing and multiple exit points, so I need to define the cohort and denominator before quoting a percentage. Evidence: [IIT Madras — BS admissions and qualifier process](https://study.iitm.ac.in/ds/admissions.html?utm_source=chatgpt.com)\
  **MEDIUM · UNSUPPORTED**
