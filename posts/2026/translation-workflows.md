---
title: Translation workflows
date: 2026-10-12T23:04:05+08:00
categories:
- llms
description: "I compare translation workflows for PDFs: Google Translate preserves Hyundai's infographic well but mishandles Pakistan's Urdu report, while Gemini translates Urdu better but loses page layout. Agents make this mix of tools practical."
tags: [translation, agentic-workflows, model-comparison]
---

Sometimes, you need multiple approaches for different parts of a problem. Increasingly, agents are making this easier.

For example, at MSCI, we're using Google Translate to translate PDFs. Sometimes it does a great job. For example, here's [Hyundai's E&C Sustainability Report, 2026](https://en.hdec.kr/en/company/library_03.aspx), in Korean.

![](https://files.s-anand.net/blog/2026-10-12-translation-workflow/hyundai-original.avif)

It was translated perfectly by Google Translate.

![](https://files.s-anand.net/blog/2026-10-12-translation-workflow/hyundai-google.avif)

At other times, it does a terrible job. For example, here's [Pakistan's Power Cement Annual Report 2026](https://dps.psx.com.pk/company/POWER) in Urdu:

![](https://files.s-anand.net/blog/2026-10-12-translation-workflow/urdu-original.avif)

It was translated _terribly_ by Google Translate.

![](https://files.s-anand.net/blog/2026-10-12-translation-workflow/urdu-google.avif)

On the other hand, if we use a Gemini model, we can translate the second page much better - almost perfectly.

![](https://files.s-anand.net/blog/2026-10-12-translation-workflow/urdu-gemini.avif)

However, this approach loses the infographic presentation of the original Hyundai report page.

![](https://files.s-anand.net/blog/2026-10-12-translation-workflow/hyundai-gemini.avif)

---

There may be no single best translation pipeline. But agents are making it easier to try out different low-cost approaches and select techniques based on language and document structure.

In other words, we're able to use higher intelligences (smarter agents) to structure the workflow using lower intelligences (Google Translate, cheaper Gemini models, etc.) to get the best results. That's a new approach to problem solving that agents are enabling.
