---
title: Things I Learned - 11 Feb 2024
date: 2024-02-11T00:00:00+00:00
categories:
  - til
description: I explored building minimal Docker images from scratch, fine-tuned Mistral using Axolotl and Deepspeed, and studied communication strategies for winning hearts. I also practiced D3.js data visualization techniques and integrated Bard with my Google Workspace tools.
keywords: [docker, axolotl, deepspeed, d3.js, llm fine-tuning, observable, bard, communication]
---

This week, I learned:

- Dockerfile can have `FROM scratch` and you can add specific binaries rather than an entire OS. [via](https://berthub.eu/articles/posts/trifecta-technology/)
- Fine-tuning session by Dan. [Notebook](https://colab.research.google.com/drive/1ts9Ar63sFK49oSz3dcw2EkivL0ZJesKi)
  - [Example of fine-tuning Mistral](https://colab.research.google.com/drive/15iFBr1xWgztXvhrj5I9fBv20c7CFOPBE). Consumed ~~28 computes (~~$2.8)
  - Axlotl is what the top fine-tuned LLMs are trained on
  - Deepspeed provides distributed training
  - Flash attention lets data stay on GPU
  - Sample packing packs samples of different lengths into equal length tensors
- Visualize the RANK of a token in a generated stream instead of logprob
- The Knowledge Project. Tomorrow Gayner
  - What I'd like in my obituary: Anand was happiness. A guru. Generous.
  - To get what we seek we must deserve this. Build, measure, learn
  - If you did the same thing daily for 50 years, would it be a great thing? If yes, do it. If not, stop. Do this in daily retrospectives
  - My new role should be productivity through technology innovation. That may mean a CTO role. But be specific otherwise no one will understand it
- Hidden brain podcast. Us 2.0. Win hearts, then minds
  - When in an interaction, ask yourself. Can I learn and change myself? Can I win their hearts, then mines, so their behavior will change. That identity will change
  - Notice when you get emotionally triggered. That's exactly when you should not get emotionally triggered
  - Try model humility and moral
  - Look for close to people's identities in our conversations. What are things they like? What does it mean for them? Simply ask. With that understanding of identity, it becomes easier to reframe things in a way they will understand
- Bard can talk to Gmail and Google Drive!
- #PREDICTION As automation takes over these mainstream activities, people will take over the niches. Since expertise like knowledge is fractal, there will be many more segments of one in the future and it will be easier to automate clusters of similar abilities. Recommenders and brands will become even more important
- [Stephen Osserman's Observables](https://observablehq.com/@osserman) have some nice notes.
  - [Visualizing partial election results](https://observablehq.com/@osserman/visualizing-partial-election-results)
  - [D3 Force Dilemmas: Data Distortion](https://observablehq.com/@osserman/d3-force-dilemmas-data-distortion)
- [Sandra Becker's 30 day D3 course](https://observablehq.com/@sandraviz/30_days_d3_dataviz)
