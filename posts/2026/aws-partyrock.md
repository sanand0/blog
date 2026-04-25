---
title: AWS PartyRock
date: '2026-01-22T21:22:31+05:30'
categories:
- tools
- llms
description: No-code AI app builders can generate decent interfaces quickly, but they may hide weak implementations behind repeated model calls instead of real software.
keywords: [AWS PartyRock, no-code AI, UI generation, vibe coding, product evaluation, tools]
---

I tried vibe-code a CSV to colored HTML table converter using [this prompt](https://github.com/sanand0/tools/blob/09ad622f1bfb662a5203593836ef765b99839e8a/colortable/prompts.md).

- Create a tool that can convert pasted tables into colored HTML tables.
- Allow the user to paste a CSV or tab-delimited or pipe-delimited table.
- ...
- Create an HTML table that has minimal styling.
- ...
- Add a button to copy just the HTML to the clipboard.

[Codex built this](https://tools.s-anand.net/colortable/). Which is perfect.

[AWS Partyrock built this](https://partyrock.aws/u/sanand0/Umcv1aE1W/TableMorph%253A-CSV-to-Styled-HTML-Converter). Which is a joke, because it didn't write the code to do the conversion. It uses an LLM every time.

![](https://files.s-anand.net/images/2026-01-22-aws-partyrock.webp)

The good part, though, is that it builds UI components that you can edit and move around.

I think it builds a domain specific language with components with properties. You can edit the properties to change the app.

This is a good way to build robust apps using unreliable LLMs. But it has less flexibility and richness.

With LLMs becoming more and more reliable, I think generating code directly is better, and this approach will fade or be used in niches.
