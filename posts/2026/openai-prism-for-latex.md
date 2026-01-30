---
title: OpenAI Prism for LaTeX
date: 2026-01-29T14:52:00+08:00
categories:
  - llms
  - tools
---

OpenAI launched [Prism](https://openai.com/prism/) - an AI LaTeX IDE.

It's a boon for anyone writing LaTeX documents. All the nitty-gritty of formatting, syntax, etc. is handled by AI. You can collaborate, too. It brings the power of AI code editors to scientific document editing.

It still has some way to go, though. I asked it to convert a portion of [this paper](https://d1wqtxts1xzle7.cloudfront.net/43007775/2_-_Chemical_routes_for_the_transformation_of_biomass_into_chemicals-libre.pdf) into LaTeX. Here's the image I passed:

[![](https://files.s-anand.net/images/2026-01-29-openai-prism-input.webp)](https://d1wqtxts1xzle7.cloudfront.net/43007775/2_-_Chemical_routes_for_the_transformation_of_biomass_into_chemicals-libre.pdf)

... and here's the [LaTeX output it generated](https://prism.openai.com/?u=a0df2c6f-a17a-4c7d-b353-d3f38dd6b363&pg=1&m=main.tex&d=7):

[![](https://files.s-anand.net/images/2026-01-29-openai-prism-output.webp)](https://prism.openai.com/?u=a0df2c6f-a17a-4c7d-b353-d3f38dd6b363&pg=1&m=main.tex&d=7)

The number of errors it made are too many to list. So, it's still some way from being picture-perfect. But for those experimenting, not publishing, it's a useful accelerator.

---

**UPDATE**: I assumed that (because the chemical formulas looked so different) it had misread the image. But experts tell me that it actually got it right! So, Prism (and the underlying GPT models) may not be perfect but are certainly better than I thought.
