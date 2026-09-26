---
title: Quality levels of GPT Image 2.5 Flare
date: 2026-09-26T16:44:30+08:00
categories:
  - llms
description: I compared GPT Image 2.5 Flare's five quality levels and found low quality already looks excellent. Medium or high helps with fine detail, but xhigh and max rarely add visible value.
tags: [llm-evaluation, image-generation, model-comparison]
---

[GPT Image 2.5 Flare](https://developers.openai.com/api/docs/models/gpt-image-2.5-flare) is a [pretty good image model](https://www.s-anand.net/blog/converting-black-and-white-photos-to-color-with-gpt-image-2.5/). It has a [quality parameter](https://developers.openai.com/api/docs/guides/image-prompting) that can be set to `low`, `medium`, `high`, `xhigh` or `max`.

Higher levels generate more tokens and here's the [rough cost by quality](https://cellcog.ai/blog/gpt-image-2-5-release-date/) for a 1024x1024 image. This cost is in **cents not dollars**:

| Quality  | Tokens | Cents |
| -------- | -----: | ----: |
| `low`    |    196 |   0.6 |
| `medium` |    439 |   1.3 |
| `high`   |  1,756 |   5.3 |
| `xhigh`  |  3,122 |   9.4 |
| `max`    |  7,024 |  21.1 |

But what difference does it really make? I [asked ChatGPT to experiment](https://chatgpt.com/share/6ab787dd-7a90-83ec-b006-6a5fe367ea33) <!-- https://chatgpt.com/c/6ab607d1-0090-83ec-a243-e17a885fe575 --> and find an image where there is a clear difference.

It began with a macro photo of a watch. See the difference between `low` and `max`:

![](https://sanand0.github.io/llmevals/gpt-image-flare-quality/images/watch-low.avif)
![](https://sanand0.github.io/llmevals/gpt-image-flare-quality/images/watch-max.avif)

First, let's note what's NOT different. The time, tiny text, exact watch hands, wool/steel texture, droplet/refraction. So, _`low` is already a pretty good model_! It's hart to tell the difference in quality.

Not much difference in a transit time poster either. The aesthetics are slightly better in `high` (the second image), which looks nearly identical to `xhigh` and `max`.

![](https://sanand0.github.io/llmevals/gpt-image-flare-quality/images/transit-low.avif)
![](https://sanand0.github.io/llmevals/gpt-image-flare-quality/images/transit-high.avif)

On a picture of a barista, `low` already produced realistic skin, fabric, scratched metal, condensation, transparent glass, steam, rain reflections and latte art.

![](https://sanand0.github.io/llmevals/gpt-image-flare-quality/images/barista-low.avif)
![](https://sanand0.github.io/llmevals/gpt-image-flare-quality/images/barista-medium.avif)

So, to give itself a challenge, ChatGPT asked for a larger image (2880x2880) with freckles,

> Ultra-realistic unretouched beauty-editorial portrait, perfectly front-facing and centered, of a woman in her mid-30s with naturally freckled light-brown skin and dark curly hair. Square composition; her head and upper shoulders fill almost the entire frame, with both eyes sharply in focus and the face occupying about 75% of the image width. Neutral warm-gray studio background, one large softbox slightly camera-left, natural color, no glamour retouching and no skin smoothing. Resolve extremely fine real-world surface detail: distinct pores across the nose and cheeks; tiny vellus peach-fuzz hairs catching side light; irregular freckles of different sizes and densities; one faint healed 8 mm scar on the left cheek; individual eyebrow hairs; separate upper and lower eyelashes; fine radial fibres and color variation in both irises; subtle wet tear-line reflections; natural lip lines and slight dry texture; individual flyaway hairs and fine frizz around the hairline. She wears a charcoal-gray chunky knitted wool turtleneck whose individual yarn fibres, twisted strands and knit loops are clearly visible, plus one simple brushed-titanium hoop earring showing very fine directional brushing and a few microscopic hairline scratches. Preserve believable human skin and anatomy. The image should reward inspection at 100% zoom: photographic microcontrast and natural high-frequency texture without artificial sharpening, plastic skin, painterly texture, beauty-filter smoothing, fake grain, text, jewelry other than the single hoop, or background objects.

Then it zoomed into the forehead and started looking for differences. At this _zoomed in_ level, differences start to appear.

[![](https://files.s-anand.net/images/202-09-26-quality-levels-of-gpt-image-2.5-flare.avif)](https://sanand0.github.io/llmevals/gpt-image-flare-quality/#where-it-shows)

`low` generates less detail. `medium` is better, and `high` has a lot of detail. But, over several blind tests, ChatGPT couldn't tell the difference between `high`, `xhigh` and `max`.

**Summary**: `low` quality (0.6 cents) is all you need. Go for `medium` (1.3 cens) or at most `high` (5.3 cents) if you really fine detail like fibre, hair, wrinkles, etc. But you almost never need `xhigh` (9.4 cents) or `max` (21 cents).

PS: I also updated my [LLM Art Style](https://sanand0.github.io/llmartstyle/) gallery with GPT Image 2.5 Flare images.
