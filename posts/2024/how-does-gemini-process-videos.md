---
title: How does Gemini process videos?
date: "2024-10-24T08:47:21Z"
lastmod: "2024-10-24T08:47:23Z"
categories:
  - coding
  - llms
wp_id: 3676
---

The Gemini documentation is clear:

> The File API service extracts image frames from videos at 1 frame per second (FPS) and audio at 1Kbps, single channel, adding timestamps every second. These rates are subject to change in the future for improvements in inference.
>
> Note: The details of fast action sequences may be lost at the 1 FPS frame sampling rate. Consider slowing down high-speed clips for improved inference quality.
>
> Individual frames are 258 tokens, and audio is 32 tokens per second. With metadata, each second of video becomes ~300 tokens, which means a 1M context window can fit slightly less than an hour of video.
>
> To ask questions about time-stamped locations, use the format MM:SS, where the first two digits represent minutes and the last two digits represent seconds.

But on this [ThursdAI episode: Oct 17 - Robots, Rockets, and Multi Modal Mania...](https://sub.thursdai.news/p/thursdai-oct-17-robots-rockets-and), at 1:00:50, [Hrishi](https://x.com/hrishioa/) says

> I don't think it's a series of images anymore because when I talk to the model and try to get some concept of what it's perceiving, it's no longer a series of images.

If that's the case, it's a **huge** change. So I tested it with this video.

<div class="video-embed"><iframe src="https://www.youtube.com/embed/Dv8KON7WQYA" title="YouTube video" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

This video has 20 numbers refreshing at 4 frames per second.

When I upload it to [AI Studio](https://aistudio.google.com/), it takes 1,316 tokens. This is close enough to 258 tokens per image (no audio). So I'm partly convinced that Gemini still processing videos at 1 frame per second.

Then, I asked it to `Extract all numbers in the video` using Gemini 1.5 Flash 002 as well as Gemini 1.5 Flash 8b. In both cases, the results were: 2018, 85, 47, 37, 38.

These are frames 2, 6, 10, 14, 18 (out of 20). So, **clearly** Gemini is still sampling at about 1 frame per second, starting somewhere between 0.25 or 0.5 seconds.
