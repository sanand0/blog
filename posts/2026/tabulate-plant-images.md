---
title: Tabulate plant images
date: 2026-09-16T13:29:17+01:00
categories:
  - llms
---

It was interesting to see how weak a model Claude 4.5 Haiku is, compared with other frontier models, even inside a good harness like Claude Code.

I asked it to: <q>Create a copy [the doc](https://files.s-anand.net/blog/2026-09-16-tabulate-plant-images/plant-images.docx) and add a table under each of the images - with a scientific name, local name - in italics, and any interesting stuff about the plant.</q>.

[Here's the chat](https://files.s-anand.net/blog/2026-09-16-tabulate-plant-images/claude-haiku.md) which roughly went:

- **Claude**: Done! I've created a new Word document with tables for all 73 plants... [plant-images-haiku-1.docx](https://files.s-anand.net/blog/2026-09-16-tabulate-plant-images/plant-images-haiku-1.docx)
- **Me**: I can't see the local names in the output.
- **Claude**: Fixed — the local names should now display properly in italics... [plant-images-haiku-2.docx](https://files.s-anand.net/blog/2026-09-16-tabulate-plant-images/plant-images-haiku-2.docx)
- **Me**: The local names aren't in italics.
- **Claude**: Fixed — I corrected the property name from `italic` to `i`... [plant-images-haiku-3.docx](https://files.s-anand.net/blog/2026-09-16-tabulate-plant-images/plant-images-haiku-3.docx)
- **Me**: It's still not in italics. Double-check.
- **Claude**: I found the problem — the italic formatting isn't being written to the XML at all... [plant-images-haiku-4.docx](https://files.s-anand.net/blog/2026-09-16-tabulate-plant-images/plant-images-haiku-4.docx)

... and the fourth attempt got it right.

In contrast, other models / agents one-shotted it.

| Model                                                                                             | Output                                                                                                                 |
| ------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| [Claude 5 Haiku](https://files.s-anand.net/blog/2026-09-16-tabulate-plant-images/claude-haiku.md) | [plant-images-haiku-4.docx](https://files.s-anand.net/blog/2026-09-16-tabulate-plant-images/plant-images-haiku-4.docx) |
| [Claude 5 Opus](https://files.s-anand.net/blog/2026-09-16-tabulate-plant-images/claude-opus.md)   | [plant-images-opus.docx](https://files.s-anand.net/blog/2026-09-16-tabulate-plant-images/plant-images-opus.docx)       |
| [GPT 5.6 Luna](https://files.s-anand.net/blog/2026-09-16-tabulate-plant-images/chatgpt-luna.md)   | [plant-images-luna.docx](https://files.s-anand.net/blog/2026-09-16-tabulate-plant-images/plant-images-luna.docx)       |
| [GPT 5.6 Sol](https://files.s-anand.net/blog/2026-09-16-tabulate-plant-images/chatgpt-sol.md)     | [plant-images-spl.docx](https://files.s-anand.net/blog/2026-09-16-tabulate-plant-images/plant-images-sol.docx)         |
