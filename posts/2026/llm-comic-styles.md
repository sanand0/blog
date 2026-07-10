---
title: LLM Comic Styles
date: '2026-03-10T19:24:58+08:00'
categories:
- llms
classes: wrap-code
description: A reusable gallery of comic-style prompts makes AI image generation more systematic, letting you apply distinct visual storytelling styles on demand.
tags: [image-generation, visual-storytelling, style-transfer]
linkedin: https://www.linkedin.com/feed/update/urn:li:activity:7437646071616557057/
---

I maintain an [LLM art style gallery](https://sanand0.github.io/llmartstyle/) - prompts to style any image I generate.

Since I generate several comics, I added a [comic category page](https://sanand0.github.io/llmartstyle/?category=comic) that includes styles like:

![](https://sanand0.github.io/llmartstyle/images/cat.silver-age.nano-banana-2.webp)
![](https://sanand0.github.io/llmartstyle/images/cat.indian-mythological.nano-banana-2.webp)
![](https://sanand0.github.io/llmartstyle/images/cat.gaulish-romp.nano-banana-2.webp)
![](https://sanand0.github.io/llmartstyle/images/cat.ligne-claire.nano-banana-2.webp)
![](https://sanand0.github.io/llmartstyle/images/cat.kirby-cosmic.nano-banana-2.webp)
![](https://sanand0.github.io/llmartstyle/images/cat.ec-horror.nano-banana-2.webp)
![](https://sanand0.github.io/llmartstyle/images/cat.british-anarchic.nano-banana-2.webp)
![](https://sanand0.github.io/llmartstyle/images/cat.bigfoot-rubberhose.nano-banana-2.webp)

To generate these, I [asked Claude](https://claude.ai/share/646de8ff-2bc0-416b-bd6b-a9863e043f23):

```markdown
Here are some examples of image styles I've explored.
<image-styles>
"2D Animation": "2D flat animation style, clean vector lines, cel-shaded coloring, cartoon proportions"
"3D Animation": "Modern 3D animation render, smooth surfaces, dramatic lighting, Octane render quality, cinematic depth"
...
</image-styles>

In the same vein, I'd like to explore **comic** styles. Create 30 popular comic / cartoon styles, aiming for diverse aesthetics and cultural influences. Name it concisely (1-2 words) based on the source, but the description should not reference the source directly (to avoid copyright issues). Focus on the visual characteristics that define each style. Pick those KEY visual elements that will subliminally evoke the style without explicitly naming it.
```

... followed by:

```markdown
Suggest a single drawing prompt (i.e. an actual comic strip to draw) that I can apply with each of these styles to compare them. Think about what description will concisely help me differentiate between the styles and choose one, and suggest that, explaining why
```

It suggested:

> A cat deliberately pushes a coffee mug off a desk. The owner watches in helpless horror as it falls.

**Why**? Two very different characters. Extreme emotional contrast. A midair object. A minimal but implied environment. Inherently comedic staging. One panel is enough.

To be on the safe side of copyright, I asked it to:

```markdown
Rewrite the comic style descriptors to include source references where there is clearly no copyright issue. Also ensure that the description will clearly evoke the style intended.
```

Then I [generated images using these prompts](https://github.com/sanand0/llmartstyle/blob/046fdc6b10114b7d5d4d5d0ee21e4ec92c66ffe5/generate_images.py).

But this still had copyright issues on Gemini and OpenAI. So I asked it to:

```
Run `uv run generate_images.py` and generate the comics (which are pending).

In the process, the image generation models may complain, e.g. saying that the image generation is prohibited, perhaps for copyright reasons.

In that case, modify the prompt / name in config.json so as the achieve the same effect but without triggering copyright issues.
```

As expected, OpenAI had a problem with four of them:

> The 4 missing styles all reference specific copyrighted artists/works by name (R. Crumb, Art Spiegelman's Maus, Frank Miller's Sin City, Dave McKean). I need to rewrite them to describe the visual style without naming the artists.
>
> Now I'll fix the 4 blocked prompts — removing copyrighted artist/work names while preserving the visual style description:
>
> - underground-comix: removed "R. Crumb and Zap Comix tradition"
> - graphic-memoir: removed "Art Spiegelman's Maus and Alison Bechdel's Fun Home"
> - neo-noir: removed "Frank Miller's Sin City visual language"
> - vertigo-dark: removed "Dave McKean and Bill Sienkiewicz…at DC Vertigo"

After these changes, OpenAI accepted all of them. So did Gemini.

But it turns out there were still some issues.

```markdown
Some of these are TOO stereotypical.

For example, the Amar Chitra Katha images ALL have multiple hands - but that's crazy, most Amar Chitra Katha comics are about normal people with two hands!

Look for similar stereotypes and remove that. Don't change ALL the prompts -- only change those prompts where there is CLEAR stereotyping that won't generalize to the majority of comics.
```

Which it did.

> Fixed exactly 2 prompts — the clearest cases analogous to the ACK example:
>
> - indian-mythological: "multiple symbolic arms in formal gesture poses" → "expressive two-armed figures in formal seated or standing poses"
> - african-pattern: "stylized human-animal hybrid figures in ceremonial contexts" → "stylized human figures in everyday contexts" (the Kente/Ndebele/Adinkra heritage is geometric textile patterns, not human-animal hybrids)
>
> The other prompts with some specificity (golden-age with capes, silver-age with cosmic villains, gaulish-romp with winged helmets, british-anarchic with school uniforms) are accurate to those specific styles — they describe a majority of the comics in those traditions — so those were left alone.

That gives me my current list of ~30 comic styles to use.
