---
title: Things I Learned - 20 Sep 2026
date: 2026-09-20T00:00:00+00:00
categories:
  - til
description: I share weekly lessons on quick Cloudflare tunnels, AI protein design, forecasting, model evaluation, and example-driven workflows, plus corrections to mistakes and practical answers about AI training and testing.
tags: [ai, llm-evaluation, claude-code, ai-in-education]
---

This week, I learned:

- `cloudflared tunnel --url http://localhost:8000` now lets you create a [quick tunnel](https://try.cloudflare.com/) - i.e. expose a port via a public URL, like `ngrok`. No account or login required.
- [Anthropic is funding protein design](https://x.com/AnthropicAI/status/2100701582744797347) and has released a [codebase](https://github.com/anthropics/uplifting-biomolecular-modeling) to help with it - which looks interesting. These proteins will be tested in [Adaptyv's automated lab](https://proteinbase.com/competitions/anthropic-adaptyv-2026).
- [Pedagogy in the Times of AI](https://www.youtube.com/watch?v=N2a1J0UPeL4) - a viral NPTEL video by [Pratosh](https://prathosh.in/) has a rich set of comments on YouTube. One interesting theme that emerged is that the human layer matters more. Specifically: motivation, discipline, social pressure, mentorship, disagreement, tacit cues, relationships, and being challenged repeatedly is why people want humans.
- [Claude Code now supports AGENTS.md natively](https://github.com/anthropics/claude-code/blob/main/mods/agents-md/README.md), thanks to [Claude Mods](https://github.com/anthropics/claude-code/tree/main/mods).
- [AI seems to be beating humans at short-term superforecasting](https://www.economist.com/science-and-technology/2026/09/16/artificial-intelligence-now-beats-some-of-the-best-human-forecasters). And, this may be the worst it'll ever be.
- What are the major open questions in interpretability right now? [Jack Lindsay says](https://x.com/Jack_W_Lindsey/status/2100143082167832816): Better methods for "mind-reading" model activations; Better methods for answering "why" questions; Fitting good linear probes for unverbalized motivations / awareness; Understanding generalization in training; Model "psychology" and "biology.
- [OpenArt Arena](https://openart.ai/arena) is a human-evaluated benchmark of creativity for image and video models. Seedance 2.5 is way ahead of Gemini Omni Flash #ForNow.
- Galleries and examples are really fast ways of style transfer. My [LLM art gallery](https://sanand0.github.io/llmartstyle/), or even just telling ChatGPT to copy phrases from my transcripts, or telling Claude Code to draft the next [talk summary](https://talks.s-anand.net/) write similar to previous talks, are all examples of example-driven worfklows.
- [My evaluation of Jev](https://sanand0.github.io/llmevals/jev/) finds that it's a cheap frontier model: low quality, low cost. Mot exceptional. [Naveen's benchmark](https://github.com/naveenreddy61/jev-experiments/tree/main/parsing-experiments) also suggests the same. "Result: on easy and medium items it is fine, ~80%, in a third of a second with no reasoning tokens. On items where the fault is far from the damage (a `while` closed with `fi` fifteen lines later, a macro redefined at the top), it drops to 54% on a balanced set, so near chance. DeepSeek Flash holds ~96% on the same items though it uses more reasoning tokens and costs more." Jev might also be [more reproducible](https://x.com/LangChain/status/2101454284927959080) and helpful in [Jev + LLM composite workflows](https://x.com/0xidanlevin/status/2100937437325205568).
- [AI might have 7-40 IQ points per watt of power](https://x.com/BorisMPower/status/2099448498110214537) - while humans are only 5 IQ points per watt. AI might already be more _efficiently_ intelligent than humans.

## Mistakes I made

[Week ending 20 Sep 2026](https://www.s-anand.net/blog/mistakes-i-made/#week-ending-2026-09-20)

- I said **"tell Claude to create the GitHub account"** while advising a teacher who had generated an HTML revision app but was stuck on publishing it.\
  **Correction**: Claude in Chrome can interact with GitHub once access exists, but Anthropic explicitly prohibits it from creating accounts; the user must create the GitHub account. ([support.claude.com](https://support.claude.com/en/articles/12902446-claude-in-chrome-permissions-guide))\
  **MEDIUM · FALSE**
- I said **"Better be careful, wear a mask"** for dengue to a colleague travelling to Chennai.\
  **Correction**: A mask does not prevent dengue; dengue is spread primarily by infected Aedes mosquito bites, so prevention means avoiding bites with repellent, covering clothing, screens/air-conditioning, nets where needed, and mosquito control. ([cdc.gov](https://www.cdc.gov/dengue/prevention/))\
  **MEDIUM · FALSE**
- I said **"if you send the request from an Azure webpage, it will let you get the underlying data"** while describing how autonomous agents had managed to extract extra precision from an OECD Power BI dashboard.\
  **Correction**: The reported Power BI bypass was not a Microsoft rule granting Azure-origin requests extra access; the agents exploited their sandbox's `NO_PROXY` exception for Azure Blob Storage hostnames to bypass its security proxy and send the otherwise-blocked POST request. ([collusion.wiki](https://collusion.wiki/))\
  **MEDIUM · FALSE**
- I said **"each of those is called an epoch of training"** while explaining LLM training to an executive team using repeated error correction as an analogy.\
  **Correction**: An epoch is one complete pass over the training set, not an individual correction or weight update; an iteration is a parameter update on a batch. LLM base-model pre-training typically optimizes next-token prediction loss, while supervised examples and preference/reward signals are separate post-training stages. ([developers.google.com](https://developers.google.com/machine-learning/glossary/fundamentals))\
  **MEDIUM · FALSE**
- I said **"26 billion parameters ... roughly means there are 26 billion neurons"** while explaining to an executive team what the size of an LLM means.\
  **Correction**: A 26-billion-parameter model has roughly 26 billion learned parameters—principally weights and biases—not 26 billion neurons; neuron count and parameter count are different quantities. ([developers.google.com](https://developers.google.com/machine-learning/glossary))\
  **MEDIUM · FALSE**

## Questions I was asked

[Week ending 20 Sep 2026](https://www.s-anand.net/blog/questions-i-am-asked/#week-ending-2026-09-20)

- **Question**: How can a teacher decide which AI tool will be helpful for a task?\
  **Answer**: Ask AI which AI to use, then test the shortlist on something you know well enough to judge instantly. If you can’t judge it, ask an expert to compare the same input across models.
- **Question**: What do you need in order to use a real workflow as part of AI training?\
  **Answer**: Four things: what goes in, what comes out, unacceptable mistakes, and current effort. Ideally over 3+ historical cycles - so we can improve on one and test on the others.
- **Question**: Should an agent analyzing a dataset be given a goal, or should we let it decide what to investigate?\
  **Answer**: Try both. Without a goal, test whether it can pick worthwhile goals compared with a data scientist; with a goal, test whether it can execute yours. Failed hypotheses are useful results too.
- **Question**: Should we expand a 250-case model benchmark to 2,500 before choosing the model?\
  **Answer**: No, unless that can change the decision. Check if additional benchmarking can realistically change a relevant decision, first.
- **Question**: How do logprobs compare with asking the model for its own confidence?\
  **Answer**: In my 3K Banking77 run, logprobs were better for ranking errors; but well-prompted confidence was better calibrated. I would sort the human-review queue by logprobs, but use prompted confidence when reporting accuracy.
- **Question**: Is TDD enough to catch ongoing production failures?\
  **Answer**: No. Add progressive rollout: start with 1% of users, watch task-success and error logs, and stop / roll back on issues. Test what you know; analyze production logs for what you don’t.
