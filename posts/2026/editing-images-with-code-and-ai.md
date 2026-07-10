---
title: Editing images with code and AI
date: 2026-06-06T11:32:47+05:30
categories:
  - llms
tags: [svg, 3d-modeling]
description: Focus on generating visual assets as code rather than pixels to enable iterative improvement. Use SVG for 2D UI and Blender scripts or USD for 3D modeling, leveraging agents like VIGA for editable, precise graphics.
---

[Andreessen Horowitz](https://a16z.com/) published an interesting article titled [The Next Frontier of Visual AI Is Code](https://www.a16z.news/p/the-next-frontier-of-visual-ai-is). Here's the summary.

A lot of our work is visual: ads, slides, dashboards, logos, videos, architecture, etc.

We can generate visual output either as:

- **Pixels** (like Nano Banana a photo), or as
- **Code** (like Claude generating an SVG)

Code is more powerful: AI can inspect the output and improve fast in a loop: **Code > Render > Inspect > Revise**.

For **2D and UI**: AI can generate SVG logos, HTML/CSS pages, Figma layers, app, etc.
For **animation and 3D**: AI can generate Lottie JSON, Blender scripts, USD scene graphs, shader code, or 3D programs.

This means **design, marketing, and product teams** are immediate prospects. Instead of static mockups, they'll get _editable_ logos, landing pages, design prototypes, motion graphics, onboarding animations, etc.

Emerging industries are **robotics, manufacturing, architecture, gaming companies**. Agents can build 3D chairs, machine, room, or robot with the right materials, joints and constraints.

I've seen some examples of this approach. Pavan used Blender MCP to [build an entire building campus](https://pavankumart18.github.io/ai-blender-design-journey/index.html) _solely by prompting Claude_. Also to [design a mug from scratch](https://pavankumart18.github.io/ai-blender-design-journey/index2.html). His approach is called [VIGA: Vision-as-Inverse-Graphics Agent](https://fugtemypt123.github.io/VIGA-website/).

[![](https://files.s-anand.net/images/2026-06-06-building-campus.avif)](https://pavankumart18.github.io/ai-blender-design-journey/index.html)

If you see anyone creating visual assets of any form - manually, or with AI as pixels - please remember this approach.
