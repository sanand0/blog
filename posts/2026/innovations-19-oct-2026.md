---
title: Innovations 19 Oct 2026
date: 2026-10-19T16:41:49+08:00
categories:
- llms
---

The Innovation team built a few more demos last week. Three interesting learnings:

1. Construct a 3D world you can walk through - from a picture.
2. Real-time video analytics is increasingly easier with decision models.
3. Small models supported by rules tend to perform well.

### 3D Worlds

**[Turn one photograph into a 3D world](https://jivraj-18.github.io/world-models/)**. Jivraj used NVIDIA Lyra and other world models to create 3D worlds (from pictures) that you can walk through.

- **Uses:** Real estate, architecture, product visualization, gaming.
- **Ideas:** Virtual Straive/client facility tours. Code repositories as 3D worlds to naviage. Our solutions page demos, organized in space.

[![A coding agent's 3D staircase beside a world-model hybrid](https://files.s-anand.net/blog/2026-10-19-innovations/world-models.avif)](https://jivraj-18.github.io/world-models/)

**[Agents convert engineering drawing from pictures](https://jivraj-18.github.io/cad-bench/)**. Jivraj used Claude Code and Codex with FreeCAD to reconstruct three engineering drawings. They look plausible, but still make some fundamental mistakes.

- **Uses:** Manufacturing, engineering, industrial design, and product companies.

[![Side-by-side 3D comparison of Claude, Codex, and the original CAD part](https://files.s-anand.net/blog/2026-10-19-innovations/cad-reconstruction.avif)](https://jivraj-18.github.io/cad-bench/freecad-f32bdb2966.html?model=claude#comparison)

**[A 3D factory shows why an order is late](https://eshwarpotturi.github.io/transformer-plant-twin/)** (Eswar). This factory has a four-day backlog in a drying oven because of an oil-station bottleneck. The agent shows management the problem in an easy to visualize way.

- **Uses:** Industrial operations, manufacturing, supply-chain teams.
- **Ideas:** A 3D digital twin is far more useful when it answers a concrete operational question. This is a synthetic, scripted proof of concept, not a live plant integration.

[![A synthetic transformer factory highlighting its production stations and in-flight orders](https://files.s-anand.net/blog/2026-10-19-innovations/transformer-plant.avif)](https://eshwarpotturi.github.io/transformer-plant-twin/)

### Real-time video analytics

**[An AI watches a sports broadcast and creates events](https://atharva-729.github.io/nfl-clef/)** (Atharva). Cloudflare's Clef (a decision model like Jev) can read the score, clock and screen in real time. That lets us do real-time video analytics far better than before.

- **Uses:** NFL, WBD, sports broadcasters, media archives, live fan experiences.
- **Ideas:** Ask a vision decision model _any multiple-choice questions_. See [rocket-launch video](https://atharva-729.github.io/clef-video-probe/) for a different set of questions.

[![NFL broadcast with automatically generated event and score annotations](https://files.s-anand.net/blog/2026-10-19-innovations/sports-video-ai.avif)](https://atharva-729.github.io/nfl-clef/)

**[Who really gets the advertising exposure around a goal?](https://sujalpradhan.github.io/automatic-brand-placement-audit/)** (Sujal). Sample football footage, read sponsor boards with OCR and compare how many seconds each brand appears on screen, especially during goals. Apple's on-device Vision OCR is cheap: the measured Mac compute is about **$0.26-0.31 per hour of 1080p video**.

- **Uses:** Broadcasters, sports rights holders, sponsors and marketing analytics teams.
- **Ideas:** Test inexpensive on-device processing before sending every frame to a costly vision API.

[![Brand exposure over time during the FIFA finals](https://files.s-anand.net/blog/2026-10-19-innovations/brand-exposure.avif)](https://sujalpradhan.github.io/automatic-brand-placement-audit/)

## Using smaller models more intelligently

**[When a small model gets payments wrong](https://eshwarpotturi.github.io/payments-slm/)** (Eswar). Gemma 3 4B handled just **55%** of merchant requests correctly. But adding rules and checks raised accuracy to **79%**, reducing the wrong actions to **3**. This is almost as good as fine-tuning - and can be used to improve fine-tuned models as well!

- **Uses:** Payment operations, fintech, banking, transaction workflows.
- **Ideas:** Using agents to optimize rules around SLMs can sometimes give as much a boost as fine-tuning.

[![Payment operations benchmark comparing baseline, rules, fine-tuning, and wrong money actions](https://files.s-anand.net/blog/2026-10-19-innovations/safe-payments.avif)](https://eshwarpotturi.github.io/payments-slm/)

### Other experiments

**[Can ChatGPT, Claude or Gemini hear AI-generated music?](https://atharva-729.github.io/AI-music-detection-benchmark/)** (Atharva). Apparently not reliably in this test. With original files, some models were perfect because they read tags such as "made with Suno". Remove those giveaways and their accuracy falls near chance. Gemini's apparent success in another test came from the _lyrics_, not the sound.

- **Uses:** Music publishers, streaming platforms, content-moderation teams.
- **Ideas:** How good is AI detection for media other than text?

**[Can an LLM decode a picture without seeing it?](https://atharva-729.github.io/base64-image-probe/)** (Atharva). We gave language models base64 strings representing tiny 8x8 images, with **no vision input or tools**. GPT-6 Sol reconstructed all 35 test images, including compressed PNGs. Impressive, though a slow and expensive substitute for a few lines of code.

- **Uses:** Probably a fun AI capability discussion rather than a client pitch.
- **Ideas:** What other "languages" can LLMs speak in? Ciphers? Maths? CAD?

And more:

- [Can agents discover their own permission leaks?](https://eshwarpotturi.github.io/agent-policy-leaks/) (AI reviewer examines agent policies for potential breaches)
- [Did a medical paper really have 'nothing to declare'?](https://eshwarpotturi.github.io/nothing-to-declare/). 967 papers had authors who said "We were not paid by drug companies", but actually were.
- [Local voice cloning](https://jivraj-18.github.io/voice-cloning-research/) (listen to two models on identical scripts)
- [FinQA with small financial models](https://eshwarpotturi.github.io/finqa-slm/) (rules helped less than in payments)
- A [new financial-retrieval comparison](https://hrmiitm.github.io/sfd-test/) (20 questions, inspect the evidence) for banks and research teams.
- [Sentiment-model cost/quality benchmark](https://hrmiitm.github.io/llm-dl-models-benchmarkings/).

If you get any ideas from these or want us to try some, please let me know.
