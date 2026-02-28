---
title: AI video compression
date: 2026-02-28T09:18:56+08:00
categories:
  - llms
  - coding
---

I recorded a short screen cast of a demo I built. It was ~900KB - way too large to publish as a thumbnail. So I asked ChatGPT:

> What's the best equivalent of squoosh.app for WEBM compression? I'm looking for a free modern high-quality online video compressor.

There are a few, and they compressed it to a third of its size, but 300KB is still too large. So I attached the original and asked:

> I am compressing screenshots like this. They're often not large. I don't mind cropping the edges by a few pixels to make it a multiple 2, 4, or 8 if that'll help. I certainly am OK with a lower frame rate. I'd like an image quality that a human eye can just SLIGHTLY detect as worse than the original, but only VERY SLIGHTLY.
>
> What's the best way of using ffmpeg or similar tools to compress such a file?
>
> Think like an expert:
> - What would an expert in this field check that beginners would miss?
> - What patterns would an expert in this field recognize that beginners would miss?
> - In this context, what questions would an expert ask that a beginner would not know to?
> - If this goes wrong, what are the most likely reasons?
>
> ... and list the best (diverse, testing different hypotheses) compression command options.
>
> Run them on this video and let me download the resulting videos for visual comparison. Interview me. Give me a list of questions that I can easily answer by looking at the videos and I'll share those with you to help you decide the best compression command for me.

This leverages 3 tricks.

1. These are online coding agents. So they can write _and_ run code.
2. The "Think like an expert" prompt is my new "Think step by step" prompt and works quite well.
3. The "Interview me" prompt is another powerful one that helps me apply preferences -- and [develop taste](/blog/how-to-develop-taste/).

[Claude](https://claude.ai/share/73d1caae-4e4e-4c1b-8984-44ac3e86f7cf) did a good job of showing different versions and compressing it, but as expected, [ChatGPT](https://chatgpt.com/share/69a24385-87b8-8003-8f41-cb3757a62d13) was the obsessive perfectionist. It gave me a huge set of variations of:

- Files sizes
- Compression formats (VP9: more compatible vs AV1: better compression)
- Quality settings (CRF)
- Frame rates (FPS)
- Color formats (YUV420p vs YUV444p)
- Compression effort (presets)
- etc.

... and asked me to compare between them, like these:

<div style="display:flex; gap:12px; flex-wrap:nowrap; align-items:flex-start;">
  <figure style="margin:0; text-align:center;">
    <video src="https://files.s-anand.net/images/2026-02-28-sql-screencast-crf45-fps15.webm" autoplay loop muted playsinline preload="metadata" width="230"></video>
    <figcaption>crf: 45 fps: 15 (93K)</figcaption>
  </figure>
  <figure style="margin:0; text-align:center;">
    <video src="https://files.s-anand.net/images/2026-02-28-sql-screencast-crf50-fps15.webm" autoplay loop muted playsinline preload="metadata" width="230"></video>
    <figcaption>crf: 50 fps: 15 (69K)</figcaption>
  </figure>
  <figure style="margin:0; text-align:center;">
    <video src="https://files.s-anand.net/images/2026-02-28-sql-screencast-crf55-fps5.webm" autoplay loop muted playsinline preload="metadata" width="230"></video>
    <figcaption>crf: 55 fps: 5 (23K)</figcaption>
  </figure>
</div>

The final result is this script:

```bash
ffmpeg -hide_banner -stats -v warning -i "$input"
  -vf "crop=iw-mod(iw\,2):ih-mod(ih\,2),fps=$fps" \
  -c:v libsvtav1 -preset 8 -crf $crf -pix_fmt yuv420p \
  -an "$output"
```

... which does the following:

- Crops the video to a multiple of 2 (which is required for some compression formats)
- Sets the frame rate to a lower value (which reduces file size)
- Uses the AV1 codec (which has better compression than VP9)
- Sets the CRF (Constant Rate Factor) to a value that balances quality and file size
- Sets the pixel format to YUV420p (which is more compatible with players)
- Disables audio (which is not needed for a screencast)

I realized that for the resolution I'll likely see this at, very low frame rates (5 fps) and poor compressions (CRF 55) are good enough.

My original video was 912KB. The smallest video that looks good enough for me is 23 KB. That's almost a **40x compression**!

---

Things I'm taking away:

- Use AI to discover the best configurations for your tool
- Interview yourself to apply preferences and develop taste
