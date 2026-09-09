---
title: Converting Black and White Photos to Color with GPT Image 2.5
date: 2026-09-09T13:50:10+08:00
categories:
  - llms
description: I test GPT Image 2.5 on colorizing my parents’ wedding photos. It preserves familiar faces better than Gemini 2.5 Flash, though it tends to make people smile slightly more.
tags: [llm-evaluation, image-generation, openai]
---

Nano Banana ([gemini-2.5-flash-image](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-image)) did a pretty good job [converting my parents' wedding photos to color](https://www.s-anand.net/blog/converting-black-and-white-photos-to-color/).

I checked how well [GPT Image 2.5](https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst) would do. The older [GPT Image 2](https://developers.openai.com/api/docs/models/gpt-image-2) model messed up the faces.

The short answer is: _better than Gemini 2.5 Flash_!

Here's the original and the GPT Image 2.5 colorized version, created with the prompt: "Convert this image to color."

![](https://files.s-anand.net/images/2025-11-01-appa-amma-wedding-original-linkedin.jpg)

![](https://files.s-anand.net/images/2026-09-09-appa-amma-wedding-color.avif)

The reason I picked this "benchmark" is because:

1. This is a real need for me.
2. This is a LLM failure: GPT Image 2 doesn't retain faces as well as Gemini 2.5 Flash does.
3. It's a benchmark I can evaluate _really_ well. I mean, I know my parents' faces well enough to spot really subtle differences.

So, from that perspective, a few things GPT Image 2.5 managed to capture well was:

1. The slightly lost expression my mother has when she day-dreamed. This isn't obvious from the photo, but is a look I know well.\
   **BUT**: She's smiling a bit more than she actually was.
2. The stern, straight look my father has.
   **BUT**: He has a _slight_ smile on his face (I don't think he ever smiled in any wedding photo) with eyes slightly upwards.
3. My grandfather's downturned mounth - rather than a frown.
   **BUT**: It added what looks like a very mild moustache.

---

I think there's a **bias towards smiling faces**. When I edited it further with this prompt:

> Make it look like a modern digital camera was transported back in time to take exactly the same photo.
> That is, same people, exactly the same faces, same clothes, etc. but much better photo quality.

... I got this image:

![](https://files.s-anand.net/images/2026-09-09-appa-amma-wedding-color-digital.avif)

Both my parents, at least one cousin, and one uncle, are smiling _slightly_ more than in the original.

---

The reason this works is that I can quickly spot _subtle_ difference in faces of family members. It's like "Oh, yeah, that's them." vs "Oh, that's not quite them."

This is the perfect kind of benchmark - something I can instantly evaluate, even as models grow far more capable.

<!-- https://chatgpt.com/c/6aa099f6-dffc-83ec-b18c-44b42f956698 -->
