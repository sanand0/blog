---
title: Using browser tabs as slides
date: '2026-02-14T17:12:20+08:00'
lastmod: '2026-06-18T14:23:18+05:30'
categories:
- how-i-do-things
- llms
description: Browser tabs can work as a lightweight slide deck, especially when combined with simple title and section pages to restore presentation flow.
keywords: [presentations, browser tabs, slides, lightweight workflows, demos, public speaking]
---

My last two presentations used browser tabs as slides.

For my talk last week titled [Your _Chotu_ Is Smarter Than You Think](https://sanand0.github.io/talks/2026-02-11-amat-dt-day/), I planned to show a series of examples. I loaded them all in a browser window as tabs like this:

1. [How I use AI to navigate toilets](https://www.s-anand.net/blog/llm-escapades-in-a-toilet/)
2. [How I use AI for food recommendation](https://chatgpt.com/share/698c125b-c4b0-800c-8006-9c92a24c4e9e)
3. [How I use AI for book suggestions](https://chatgpt.com/share/698c1290-dc08-800c-8011-88c021e25c3c)
4. [What else I can use AI for](https://sanand0.github.io/datastories/gdpval/)
5. ...

Once loaded, I can press Ctrl+PgDn to move to the next - just like I'd press the right arrow key in a slide deck. I can also use the mouse to click on the tab if I want to jump around.

But there's _one_ advantage I missed from slides. I can add title slides, section dividers, etc.

Since web pages are so versatile, I vibe-coded a [slide tool](https://tools.s-anand.net/slide/) by [roughly saying](https://github.com/sanand0/tools/pull/97):

- Give me a single page "slide" tool
- Let me edit the title, subtitle, fonts, colors, backgrounds, etc. via a (barely visible) button on the top right
- Store this in the URL so I can bookmark and share it

(**Note**: I had 5 min on 4% battery and my laptop couldn't connect to the Internet. This was voice vibe-coded on the web and the PR accepted without review.)

That let me create a _far_ richer presentation.

1. [🟢 **SLIDE** I use AI like an intern](https://tools.s-anand.net/slide/#title=I+use+AI+like+an+intern&subtitle=A+%22chotu%22.+Plumber.+Waiter.+Secretary.+Banker.&font=Montserrat&scale=6.3&fgColor=%23ffffff&bgColor=%231a1a2e&bgSearch=https%3A%2F%2Fimages.unsplash.com%2Fphoto-1760978632114-0939f0d60045%3Fq%3D80%26w%3D1528%26auto%3Dformat%26fit%3Dcrop%26ixlib%3Drb-4.1.0%26ixid%3DM3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%253D%253D)
2. [Like a plumber, to navigate toilets](https://www.s-anand.net/blog/llm-escapades-in-a-toilet/)
3. [Like a waiter, for food recommendation](https://chatgpt.com/share/698c125b-c4b0-800c-8006-9c92a24c4e9e)
4. [Like a secretary, for book suggestions](https://chatgpt.com/share/698c1290-dc08-800c-8011-88c021e25c3c)
5. [🟢 **SLIDE** Use Paid AI. ANY Paid AI is the best ROI you get](https://tools.s-anand.net/slide/#title=Use+_paid_+AI&subtitle=Buy+_any_+PAID+subscription+to+ChatGPT%2C+Gemini%2C+or+Claude+and+keep+it+in+your+phone.&font=Montserrat&scale=6.3&fgColor=%23ffffff&bgColor=%231a1a2e&bgSearch=https%3A%2F%2Fimages.pexels.com%2Fphotos%2F2387819%2Fpexels-photo-2387819.jpeg)
6. [You can hire AI for many services](https://sanand0.github.io/datastories/gdpval/)
7. [🟢 **SLIDE** Under-using AI is more dangerous than over-using](https://tools.s-anand.net/slide/#title=Over-use+it.%5C%0AUnder-use+is+riskier%21&subtitle=You+_will_+lose+skills.+Like+long+division+and+hunting.%5C%0ALearn+new+ones.+Have+50+chats+%2F+day.&font=Montserrat&scale=6.3&fgColor=%23ffffff&bgColor=%231a1a2e&bgSearch=https%3A%2F%2Fimages.unsplash.com%2Fphoto-1760978632114-0939f0d60045%3Fq%3D80%26w%3D1528%26auto%3Dformat%26fit%3Dcrop%26ixlib%3Drb-4.1.0%26ixid%3DM3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%253D%253D)
8. ... and so on.

![Here's what the full presentation looked like](https://files.s-anand.net/images/2026-02-14-slide-tool.webp)

The "slides" allow me to add structure and remind the audience and me about the key points.

For all the bad press PowerPoint receives, I don't think presentations are a bad format. But today, there are so many more ways of presenting that using slideshow software seems a bit outdated.

---

**UPDATE 18 Jun 2026**: My talks in the last few months use this technique almost without exception.
