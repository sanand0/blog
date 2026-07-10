---
title: Read Tamil on TV with Gemini
date: 2026-03-25T21:32:50+08:00
categories:
  - llms
description: Gemini can turn casual screenshots into instant OCR-and-translation aids, making it a practical companion for reading text embedded in everyday media.
tags: [gemini, ocr, translation, tamil]
---

I've been [reading books using AI](/blog/new-ways-of-reading-books/). Today, I used Gemini while watching a TV show. (Not _to_ watch TV - just _while_ watching TV.)

There's [this scene](https://youtu.be/1jsvEEaZ5Zc?si=nMhaCZUjS1QLF1ta&t=146) in [Iru Dhuruvam Season 2](https://en.wikipedia.org/wiki/Iru_Dhuruvam_season_2) with a sheet of paper with Tamil text on it.

<iframe width="560" height="315" src="https://www.youtube.com/embed/1jsvEEaZ5Zc?si=IltVeFCbroyuJEN4&amp;start=147" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

The script was small and I couldn't read it clearly. (I'm pretty slow at reading Tamil anyway.) So I took a screenshot (Linux is great that way - you can record screenshots from any video player) and [asked Gemini](https://gemini.google.com/share/44bef43fad8a):

```markdown
OCR and translate
```

(I was eating dinner and had just one hand to type - minimally.)

It said:

> **Original Tamil Text**: வினைபகை என்றிரண்டின் எச்சம் நினையுங்கால் தீயெச்சம் போலத் தெறும்
>
> **English Translation**: When you consider the remnants of an incomplete action or an unconquered enemy, they will destroy you like the unextinguished remnant of a fire.
>
> This is **Thirukkural 674**, written by the ancient poet Thiruvalluvar. It serves as a stark warning against leaving tasks or conflicts half-finished. Given the gloves and the torn paper, this looks like a classic cinematic trope—a cryptic, high-stakes warning left behind in a thriller, signaling that the job (or the revenge) is far from over.

Spot on. The rest of the scene made perfect sense!

![](https://files.s-anand.net/images/2026-03-25-read-tamil-on-tv-with-gemini.avif) <!-- https://gemini.google.com/app/73382f0b7330b64c -->

This is not the first time I've used AI while watching TV. I've passed screenshots to identify cities, transcribe newspapers, and more. But this is the first time I've used it to read Tamil.

(BTW, the image in the screenshot above is a Gemini-upscaled with the prompt "Draw the same image, upscaled and sharper".)
