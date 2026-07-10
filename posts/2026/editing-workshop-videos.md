---
title: Editing Workshop Videos
date: 2026-06-14T08:27:16+05:30
categories:
  - tools
  - coding
description: I use ffmpeg to trim and compress workshop recordings from Zoom and Meet. I share my exact commands for fast, lossless trimming and high-efficiency VP9/Opus compression to host videos affordably on Cloudflare R2.
tags: [ffmpeg, video-compression, cloudflare-r2, webm]
---

I sometimes use [Google Meet](https://meet.google.com/), [Teams](https://teams.microsoft.com/), [Zoom](https://www.zoom.com/), etc. to record workshops and talks. These record the entire session, including _before_ and _after_ the actual talk, and save it as large MP4 files.

I use `ffmpeg` to trim the video to just the talk, and then compress it for sharing. I'm sharing the options that work for me, discovered by trial-and-error.

**To trim it**, I use the following command:

```bash
ffmpeg -ss 00:10:00 -to 02:10:00 \
  -i "original.mp4" \
  -map 0 \
  -c copy \
  -avoid_negative_ts make_zero \
  -movflags +faststart \
  new.mp4
```

Arguments:

- `-ss 00:10:00`: Start reading from 10:00 into the source file. Placing -ss before -i makes this fast because ffmpeg seeks instead of decoding from the start.
- `-to 02:10:00`: Stop at 02:10:00 in the source timeline. So this keeps roughly the section from 00:10:00 to 02:10:00.
- `-map 0`: Keep all streams from the input: video, audio, subtitles, metadata streams, etc. Use `-map 0:v:0 -map 0:a:0` for just the first video and audio streams.
- `-c copy`: Do not re-encode. Just copy the existing encoded streams. This is very fast and preserves original quality, but cuts only cleanly near keyframes.
- `-avoid_negative_ts make_zero`: Rewrite timestamps so the output starts cleanly near zero. This helps avoid weird negative timestamps and duration/reporting issues in some players.
- `-movflags +faststart`: Move MP4 metadata to the beginning of the file. This helps playback start faster in browsers and streaming contexts.)

**To compress it** I use:

```bash
ffmpeg -i 'trimmed.mp4' \
  -map 0:v:0 -map 0:a:0 \
  -c:v libvpx-vp9 \
  -b:v 0 \
  -crf 42 \
  -deadline realtime \
  -cpu-used 8 \
  -row-mt 1 \
  -tile-columns 2 \
  -frame-parallel 1 \
  -threads 8 \
  -pix_fmt yuv420p \
  -vf "fps=16" \
  -c:a libopus \
  -b:a 32k \
  -ac 1 \
  -ar 48000 \
  -af "highpass=f=80,lowpass=f=12000" \
  "compressed.webm"
```

Arguments:

- `-map 0:v:0 -map 0:a:0`: Use the first video stream and first audio stream from the input
- `-c:v libvpx-vp9`: Compress video with VP9 codec
- `-b:v 0`: Use constant-quality mode instead of targeting a fixed bitrate
- `-crf 42`: When testing on samples, CRF 42 was small enough and clear enough for me
- `-deadline realtime`: `-deadline good` is too slow for me though that's better for production
- `-cpu-used 8`: 8 is the maximum allowed for VP9 for now
- `-row-mt 1`: Enable row-based multithreading for faster VP9 encoding
- `-tile-columns 2`: Split each frame into tiles so multiple threads can encode in parallel
- `-frame-parallel 1`: Allow frames to be decoded in parallel; useful for VP9/WebM playback
- `-threads 8`: Use up to 8 CPU threads during encoding
- `-pix_fmt yuv420p`: Use the most compatible pixel format for browsers and video players
- `-vf "fps=16"`: Reduce frame rate to 16 fps to shrink file size; good enough for slides/talk videos
- `-c:a libopus`: Compress audio with Opus, the standard audio codec for WebM
- `-b:a 32k`: Use low audio bitrate; enough for speech
- `-ac 1`: Convert audio to mono; good for voice and halves stereo audio data
- `-ar 48000`: Use 48 kHz, the standard sample rate for Opus
- `-af "highpass=f=80,lowpass=f=12000"`: Remove very low rumble and very high noise; keeps speech frequencies

I deploy these on CloudFlare R2 on a custom domain: [media.s-anand.net](https://media.s-anand.net/). [R2 costs](https://developers.cloudflare.com/r2/pricing/) 1.5c / GB-month. Storing 10 years' worth of ~500 talks of ~0.5 GB each is under $4 / month - quite affordable. (If it increases, I can shift. Statis files are easy to move.)

I serve them via a `<video>` tag. Here is an [example video](https://media.s-anand.net/2026-05-23-ai-unboxed-context-engineering.webm):

```html
<video preload="metadata" width="1920" height="1080" controls style="max-width: 100%; height: auto;">
  <source src="https://media.s-anand.net/2026-05-23-ai-unboxed-context-engineering.webm" type="video/webm; codecs=&quot;vp9, opus&quot;">
</video>
```

<video preload="metadata" width="1920" height="1080" controls style="max-width: 100%; height: auto;">
  <source src="https://media.s-anand.net/2026-05-23-ai-unboxed-context-engineering.webm" type="video/webm; codecs=&quot;vp9, opus&quot;">
</video>
