---
title: Recording screencasts
date: '2026-03-11T10:48:01+08:00'
categories:
- coding
- how-i-do-things
description: A lightweight recording and compression workflow can produce high-quality screencasts cheaply enough to make video a practical medium for demos, teaching, and documentation.
keywords: [screencasts, video recording, compression, WEBM, ffmpeg, developer tools]
---

<!-- https://gemini.google.com/u/2/app/6cf35e0e4b2a90da -->

![](https://files.s-anand.net/images/2026-03-11-recording-screencasts.avif)

Since [WEBM compresses videos **very** efficiently](/blog/ai-video-compression/), I've started using videos more often. For example, in [Prototyping the prototypes](/blog/prototyping-the-prototypes/) and in [Using game-playing agents to teach](/using-game-playing-agents-to-teach/).

I use a [fish script to compress screencasts](https://github.com/sanand0/scripts/blob/e0049d7b79d142e23b64fe9ce2c2a383ca8250a6/setup.fish#L442-L475) like this:

```bash
# Increase quality with lower crf= (55 is default, 45 is better/larger)
# and higher fps= (5 is default, 10 is better/larger).
screencastcompress --crf 45 --fps 10 a.webm b.webm ...
```

To _record_ the screencasts, I prefer slightly automated approaches for ease and quality.

**METHOD 1: Browser scrolling**: To uniformly scroll to the bottom of the page at ~800 pixels / second (roughly one page per second), I frame the recording window, start [recording](https://help.gnome.org/gnome-help/screen-shot-record.html), and _quickly_ paste this script in the DevTools console:

```js
scrollInterval = setInterval(() => {
  window.scrollBy(0, 16); // Scroll 16px every 20ms (approx 800px/s)
  if (window.innerHeight + window.scrollY >= document.body.scrollHeight) {
    clearInterval(scrollInterval);
    console.log("Reached bottom or no more scrolling.");
  }
}, 20);
```

This is what I used in [Prototyping the prototypes](/blog/prototyping-the-prototypes/).

**METHOD 2: AI Coding Agents**: I tell the coding agent to:

> ... screenshot each step at 1366x768, compressing into video.webm at 1.5 fps, pausing the last frame for 5 seconds.

If playwright and ffmpeg are set up, this _just works_.

This is what I used in [Using game-playing agents to teach](/using-game-playing-agents-to-teach/).
