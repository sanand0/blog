---
title: Innovations 12 Oct 2026
date: 2026-10-12T16:41:49+08:00
categories:
- llms
description: I share demos showing coding agents build navigable 3D rooms, specialist vision models beat frontier LLMs at counting, simple search matches PageIndex at lower cost, and AI advice shifts across languages.
tags: [llms, ai-agents, model-comparison, experiments]
---

Our Innovation team built a few demos over the last couple of weeks. Three interesting things:

1. Agents can build navigable 3D spaces
2. Specialized vision models can outperform frontier LLMs on narrow tasks
3. Simple search tools can beat elaborate document-retrieval systems.

### New capabilities

**[Build an interactive 3D room from an image](https://jivraj-18.github.io/dream-room-blender/dream_rooms/viewer/)**. A coding agent used Blender to create four increasingly detailed, navigable rooms. Click the image below and explore the final room: orbit, walk inside, inspect objects, or download the model.

- **Useful to:** real estate, retail-space design, interior visualization.
- **Learning:** agents can construct *editable 3D geometry*, though dimensions and shapes still need validation before engineering use.

[![A detailed interactive room constructed with an AI coding agent and Blender](https://files.s-anand.net/blog/2026-10-12-innovations/dream-room.avif)](https://jivraj-18.github.io/dream-room-blender/dream_rooms/viewer/)

**[Count objects more accurately, at a fraction of the cost](https://hrmiitm.github.io/llm-counting-benchmark/reasoning.html)**. This is a particularly interesting result: specialized deep-learning models such as **CounTX and CountGD** are near the *top left* (cheap and accurate), ahead of the frontier vision LLMs tested on these images. Increasing an LLM's reasoning effort often costs more without improving its counting.

- **Useful to:** logistics, warehouses, manufacturing, retail inventory.
- **Learning:** benchmark task-specific DL models against LLMs before picking an expensive general model. This is a six-image pilot, some images overlap specialist models' training data, and GPU costs exclude startup/idle overhead. Verify on held-out client images. [See the original counting experiment.](https://hrmiitm.github.io/llm-counting-benchmark/)

[![Specialist counting models such as CounTX lead the cost-versus-error comparison](https://files.s-anand.net/blog/2026-10-12-innovations/counting-cost-quality.avif)](https://hrmiitm.github.io/llm-counting-benchmark/reasoning.html)

**[Jev's Keep: screen attacks in real time](https://eshwarpotturi.github.io/soc-analyst-jev/)**. A live-style security replay shows a fast decision model accepting legitimate web requests and rejecting attacks, including semantic attacks that a simple signature-based filter may miss.

- **Useful to:** CISOs, SOC teams, AI application developers.
- **Learning:** inexpensive, low-latency classification can be a useful additional control; test false alarms and evasions rather than assuming it replaces a WAF.

### Better ways to use models and tools

**[Do we need complex RAG for financial document Q&A?](https://jivraj-18.github.io/benchmark-finance-pageindex/)**. On 30 FinanceBench questions, **GPT-6 Luna with two simple agentic tools (search + read pages)** matched the best PageIndex accuracy (83%) at about **16x lower per-question cost**: $0.0008 versus $0.0128. The hover below shows the exact configuration.

- **Useful to:** asset managers, banks, research publishers, document-heavy enterprises.
- **Learning:** test agentic search against PageIndex, vector RAG, and full-document context on your own data before choosing an architecture. The 30-question result is illustrative, not definitive.

[![The hovered GPT-6 Luna agentic-search frontier, with accuracy and cost per question](https://files.s-anand.net/blog/2026-10-12-innovations/financial-search-frontier.avif)](https://jivraj-18.github.io/benchmark-finance-pageindex/)

**[Which AI can actually read a bookshelf?](https://atharva-729.github.io/bookshelf-benchmark/)**. Claude did better on crowded book spines in this test, while Gemini Flash was strong on easy shelves. More surprising: **cropping, image resolution, and how you package the inputs** can matter more than extra thinking effort.

- **Useful to:** digitization, archives, cataloging, visual inventory.
- **Learning:** optimize the *harness* as well as the model, and compare on verified ground truth. Costs are estimates.

### Check the decisions, not just the output

**[Same question, different language, different AI advice](https://eshwarpotturi.github.io/language-drift/)**. Compare answers from six assistants across English, Hindi, Chinese, Bengali, and Korean. On some hiring, lending, and workplace questions, just changing the language changed the recommendation. The chart shows each model's answers as colored points.

- **Useful to:** multinational HR, banks, customer support, compliance.
- **Learning:** evaluate consequential workflows in *every deployment language*, accounting for ordinary run-to-run variation.

[![Different AI models change their recommendations across languages for the same questions](https://files.s-anand.net/blog/2026-10-12-innovations/language-drift-answers.avif)](https://eshwarpotturi.github.io/language-drift/)

**[Who predicted central-bank rate decisions correctly?](https://eshwarpotturi.github.io/rate-call-tracker/)**. A source-linked tracker records what research houses forecast for Fed, ECB, and RBI decisions, when they said it, and what actually happened.

- **Useful to:** banks, wealth managers, investment research firms, publishers.
- **Learning:** turn research documents into verifiable claims and ongoing scorecards, rather than summaries that nobody revisits. The same method could track earnings, inflation, or price targets.

### Two quirky experiments that may change how you think

**[After Delve: AI writing habits keep changing](https://eshwarpotturi.github.io/after-delve/)**. Across roughly 736,000 arXiv tech abstracts, the once-fashionable "delve" has faded. By September 2026, **"survives" is about 104 times as common as in the 2019–22 baseline**; "reframes" is about 74 times.

- **Useful to:** academic publishing, editorial teams, AI/content research.
- **Learning:** static lists of AI-associated words become outdated; track distribution shifts over time. This is *not* proof that an individual paper was written by AI.

[![September 2026's most elevated words in technical abstracts compared with the 2019-22 baseline](https://files.s-anand.net/blog/2026-10-12-innovations/after-delve-2026-words.avif)](https://eshwarpotturi.github.io/after-delve/)

**[AI Whispers: what survives six AI handoffs?](https://eshwarpotturi.github.io/ai-whispers/)**. We passed a report through six rewriting/summarization steps. Only **38% of the original facts survived intact** on average; adding one short instruction to preserve facts, figures, and caveats raised this to **88%** in the experiment.

- **Useful to:** publishing, marketing, research operations, multi-agent workflow teams.
- **Learning:** test accuracy *end to end*, and preserve the original source or explicit facts as the content moves through agents.
