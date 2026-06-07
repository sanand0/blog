---
title: Self-discover LLM capabilities
date: 2026-01-10T11:40:00+08:00
categories:
  - llms
  - how-i-do-things
description: I discovered hidden LLM capabilities by asking models like Claude to identify creative uses for their built-in tools. This led to generating stunning algorithmic videos using ffmpeg fractal filters, Python L-systems, and complex cellular automata.
keywords: [llms, ffmpeg, claude, algorithmic art, fractals, tool-use]
linkedin: https://www.linkedin.com/feed/update/urn:li:activity:7415939924937379841/
---

Q: "How do we learn what we can do with AI agents?"

Me: "Ask them!"

I mean, they are probably aware of their abilities. They can search online for how other people are using them. They have access to tools (connect to GMail, write & run code, etc.) which they're aware of, and even if not, can try out.

Asking them seems a useful way of figuring out how to use them.

For example, I didn't know that [`ffmpeg`](https://www.ffmpeg.org/) (which ChatGPT, Gemini, Claude, etc. can run) can visualize audio using filters. They could create a bunch of stunning visualizations as a video compilation.

So, I [told Claude](https://claude.ai/share/88b3dec2-3f15-45b1-868d-44f051dcf20f):

> I did not know ffmpeg could visualize audio via filters...\
> You have a container environment with a set of tools installed and you can run commands.\
> Identify creative ways in which the tools you have access to can be used...\
> ...\
> Fact-check by cursorily verifying the command options...\
> But no need to implement any of these...\
> BLOW MY MIND!!

It gave me [125 ideas](/blog/notes/llm-creative-tool-capabilities/) from drum patterns of log timestamps, directory structures as artistic graphs, frequency domains of images via Fourier transforms, morphological image erosion/dilation effects, and a whole bunch of things I've never heard of.

It was too much, so I didn't bother. (I'll read later.)

> Implement the most visually impressive among these.

And the result was a stunning video compilation:

<div class="video-embed"><iframe src="https://www.youtube.com/embed/d7NXU2jeSiU" title="YouTube video" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

It generated these 10 _purely_ algorithmic (no external assets) visualizations:

1. **Mandelbrot Set** via FFmpeg's `mandelbrot` filter: Deep zoom into the famous seahorse valley, revealing infinite complexity from z² + c
2. **Sierpinski Carpet** via FFmpeg's `sierpinski` filter: Recursive self-similar fractal pattern that animates through chaos game iterations
3. **Game of Life** via FFmpeg's `life` filter: Conway's cellular automaton with glowing cells and mold trails showing emergent complexity from 4 simple rules
4. **Rule 30** via FFmpeg's `cellauto` filter: Wolfram's elementary cellular automaton that generates apparent randomness from deterministic rules
5. **Domain Coloring** via Python + NumPy: Complex function visualization where hue represents angle and brightness represents magnitude, morphing through z², z³, and rational functions
6. **L-Systems** via Python + PIL: Three fractal trees grow algorithmically using Lindenmayer system grammar rules - pure mathematical botany
7. **Barnsley Fern** via Python chaos game: 500,000 points plotted using an Iterated Function System, emerging from randomness into a perfect fern
8. **Julia Set** via Python + NumPy: Dancing fractals as the complex parameter c traces a wobbling circle, continuously morphing fractal boundaries
9. **Plasma Effect** via FFmpeg's `geq` expression filter: Real-time interference patterns using layered sine waves in RGB channels
10. **Gradient Spiral** via FFmpeg's `gradients` filter: Six-color rotating spiral with 8x speed, creating hypnotic color field animation

... with cinematic title cards (fade transitions, credits) in a 1080×1080 square format perfect for social media.

![](https://files.s-anand.net/images/2026-01-10-self-discover-llm-capabilities.webp)

---

I learnt at least a few things from this:

1. **The tool side**. I now know that `ffmpeg` has built-in fractal capability. Fractals have fascinated me since I was 12. This is something to explore.
2. **The technique side**. I'm learning new terms like "temporal slit-scan photography" - used to create time-slice effects like bullet time in _The Matrix_, using `ffmpeg`. Or "music chord visualization" using [`neato`](https://graphviz.org/docs/layouts/neato/), or capturing packet flow data using [`tcpdump`](https://www.tcpdump.org/) to visualize network traffic, etc.

I would never have thought of these, but the capabilities are in my hands.

I think there's benefit in just spending time with LLMs, asking them (in different ways) what they can do, and what would help, interest, or even amuse us.

---

PS: [ChatGPT's response to this](https://chatgpt.com/share/6961c2ea-f7d4-800c-8133-26d67a7bc5eb) was a bunch of good ideas and a _tiny_ 0.5 second Mandelbrot video. Gemini shared a tiny list of 10 ideas ([read them all](/blog/notes/llm-creative-tool-capabilities/)) but made up with this brilliant Veo-generated video.

<div class="video-embed"><iframe src="https://www.youtube.com/embed/tzXZzVgJP78" title="YouTube video" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

<!-- https://claude.ai/chat/a014c8c7-4179-400f-9a80-75d849ccec41 -->
<!-- https://chatgpt.com/c/69477805-b150-8321-bdf7-d654222f867c via Gramener ID -->

---

[LinkedIn](https://www.linkedin.com/posts/sanand0_q-how-do-we-learn-what-we-can-do-with-ai-activity-7415939924937379841-Wrdp)
