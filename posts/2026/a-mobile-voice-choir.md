---
title: A Mobile Voice Choir
date: 2026-10-26T05:06:29+01:00
categories:
- visualization
description: I tested a mobile voice choir where about 20 Straive participants hummed along to a tone on their phones. After 45 seconds, they had barely converged, prompting a question about whether people differ sharply in their ability to match pitch.
tags: [experiments, convergence, data-visualization, mobile-phones]
cover:
  image: https://files.s-anand.net/images/2026-10-26-a-mobile-voice-choir.avif
  hiddenInSingle: true
---

I've been playing around with mobile sensors recently and one such experiment is the [voice choir](https://sanand0.github.io/mobile-games/voice-choir/).

Here's how it works.

1. I'm the presenter. I visit [voice choir](https://sanand0.github.io/mobile-games/voice-choir/), create a room, and show the QR code.
2. People see the QR code (via screen-sharing or projector) and open on their mobile phones to join my room.
3. I press "Start". They hear a tone and they should hum at the same pitch.
4. They can see if their pitch is above or below and adjust. I get a data stream of their pitch.
5. Over time, we see if we can hum at the same pitch, or how close we converge.
6. I record this as a visualization.

We played this in Straive across about 20 people who joined the room. Here's the video:

<video controls autoplay loop muted playsinline preload="metadata" poster="https://files.s-anand.net/images/2026-10-26-a-mobile-voice-choir.avif" width="1350" height="924" style="max-width: 100%; height: auto;">
  <source src="https://media.s-anand.net/2026-10-23-voice-choir.webm" type="video/webm">
  <a href="https://media.s-anand.net/2026-10-23-voice-choir.webm">Video</a>
</video>

What surprised me most was how little convergence there was even after 45 seconds. People were still humming all over the place.

In the early days of Gramener, I learned that there are some people who find it hard to pick up a "design" sense. Even after repeated guidance, I found them violating rules like keeping edges aligned. Research also suggests that some people find it hard to pick up mathematics - and that the population may be bi-modal (i.e. some people get it, some just don't.)

Maybe this true for music as well?

I think it's cool that we can test this: get 100 students into this room, have them hum a tone, and see if the alignment / convergence is bimodal!
