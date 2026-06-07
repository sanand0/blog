---
title: Things I Learned - 08 Sep 2024
date: 2024-09-08T00:00:00+00:00
categories:
  - til
description: I benchmarked RAM and CPU usage across FastAPI, Node, and Deno, while exploring several video and audio generative AI tools. I also identified whisperX for diarization and tested Reflection 70b's internal reflection mechanism for improved model accuracy.
keywords: [fastapi, deno, generative video, reflection 70b, whisperx, diarization, coedit-xxl]
---

This week, I learned:

- When running a Hello world app:
  - FastAPI takes ~26K RAM, 3% CPU
  - NodeJS + Express takes ~62K RAM, 2% CPU
  - Deno + Express takes ~62K RAM, 1% CPU
  - Deno + Fresh takes ~54K RAM, 0.4% CPU
- I was testing out different video LLMs:
  - [Luma Labs](https://lumalabs.ai/) lets you create videos from text
  - [Runwal ML](https://runwayml.com/) lets you create video from an image + text
  - [Viggle](https://viggle.ai/) lets you add images to a video or move a character in a certain way
  - [Veed.io](https://www.veed.io/) is a video editor that offers AI video editing features
  - [Deepmotion](https://www.deepmotion.com) generates 3D animations from video
  - Wonder Dynamics may be similar to DeepMotion
- I tested out a few audio LLMs:
  - [Suno](https://suno.com/) is fast, has a better UI, lots of examples
  - [Udio](https://www.udio.com/) is slow, poor UI, creates richer music
- [Reflection 70b is one of the top models now, and is open source!](https://x.com/mattshumer_/status/1831767014341538166). It works by making the LLM reflect on its answer inside `<reflection>...</reflection>` tags.
- The best diarization model today is [whisperX](https://github.com/m-bain/whisperX). Run on [Colab T4 GPU](https://colab.research.google.com/drive/1I2hwOqb08s_otWIUAmPRmb3EA9Z4bCtF) with:
- [Scale's SEAL Leaderboards](https://scale.com/leaderboard) seem fairly good.
- [coedit-xxl](https://huggingface.co/grammarly/coedit-xxl) is Grammarly's fine-tuned google/flan-t5-xxl model run on [CoEdit](https://github.com/vipulraheja/coedit) - text editing dataset. It's mainly for single-line editing, though, and far from a full-document or full-email zero-shot editor.
