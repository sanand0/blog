---
title: Creating comic explainers
date: 2026-05-24T16:48:58+08:00
categories:
  - llms
description: I share my ChatGPT prompt for generating Scott McCloud-style comic explainers to create more engaging, differentiated content. By moving from sketchnotes to sequential storytelling, I use visual metaphors and cause-and-effect panels to simplify complex AI concepts.
keywords: [comic explainers, scott mccloud, sketchnotes, chatgpt, prompt engineering, visual storytelling]
linkedin: https://www.linkedin.com/feed/update/urn:li:activity:7464246787395125249/
---

[Lori Silverstein](https://www.linkedin.com/in/lori-silverstein-b9baa03/) shared a [post from Quickplay](https://www.linkedin.com/feed/update/urn:li:activity:7462864729913503744/) that featured a comic explainer, mentioning that "this could be a very impactful way for us to start being more creative ... and differentiate our value proposition."

![](https://files.s-anand.net/images/2026-05-24-quickplay-comic.avif)

True. Comic explainers convey both creativity _and_ differentiation.

I've used [sketchnotes](https://www.s-anand.net/blog/gemini-sketchnotes/) for the same effect, but comic explainers are easier to follow than sketchnotes.

So I fed this image to ChatGPT and [asked it to modify my Sketchnote prompt](https://chatgpt.com/share/6a12bd89-5274-83ec-827c-2446d0be19d2):

> How would I modify this prompt to draw a Scott McCloud style explainer comic page in color? I'm looking for the way in which he explained Google Chrome when it was released, but with more vibrant colors. Something like the attached image is good for me.
>
> ```
> Draw this as a visually rich, intricately detailed, colorful, and funny, sketchnote (square 1:1).
> Use comic-style font in caps.
> Keep the text to under 300 words. Prefer evocative imagery over text.
> Think about the most important points, structure it logically so that the sketchnote is easy to follow, then draw it.
> ```

It gave me a prompt which I've iterated on a few times. This is the [comic page prompt](https://github.com/sanand0/blog/blob/6e1af00d0bc593f3b88bddf57416b533d558c3a3/pages/prompts/fragments.md#comic-page) I currently use:

> Draw this as a full-color explainer comic page (portrait) - sequential explanation, friendly narrator, diagrams embedded inside panels, visual metaphors, self-aware captions, and clear cause-and-effect storytelling.
> Style: expressive characters, comic-style ALL CAPS, vibrant modern colors, clear visual hierarchy.
> Prefer pictures over words. Use recurring visual metaphors so the reader understands the idea even while skimming.
> Think about the most important points, structure it as a memorable story.

Some examples of the output:

[What Your AI Doesn't Know About You](https://sanand0.github.io/talks/2026-05-23-ai-unboxed-context-engineering/)

[![](https://sanand0.github.io/talks/2026-05-23-ai-unboxed-context-engineering/comic-page.avif)](https://sanand0.github.io/talks/2026-05-23-ai-unboxed-context-engineering/)

[Where Enterprise AI is Headed](https://www.s-anand.net/blog/where-enterprise-ai-is-headed/)

[![](https://files.s-anand.net/images/2026-05-23-where-enterprise-ai-is-headed.avif)](https://www.s-anand.net/blog/where-enterprise-ai-is-headed/)

---

Though AI makes it easy to create comic explainers, sketchnotes, etc., I expect we might see _less_ of them.

Why?

- Excel made [Playfair](https://en.wikipedia.org/wiki/William_Playfair) style charts _less_ common with a deluge of bar charts.
- AI will make templatized slides _so much easier_ that comic explainers will be drowned out.

But creative people like [The Pudding](https://pudding.cool/) will likely use AI to create _even_ more innovative formats. Something I'm looking forward to.

![](https://files.s-anand.net/images/2026-05-24-creating-comic-explainers.avif)

<!--

- Future of Comic Explainers - Creativity vs standardization with AI
  - https://chatgpt.com/c/6a12bf20-28a8-83ec-8a6f-5b20f137d4fe
  - https://claude.ai/chat/92bd7c3a-7de8-4106-a5d8-b39f92cca1be

-->
