---
title: Things I Learned - 17 Dec 2023
date: 2023-12-17T00:00:00+00:00
categories:
  - til
description: I explored Grab’s map optimizations, Amex’s explainable credit models, and batch inferencing with vLLM. I also looked into Playwright for browser testing, Mixtral-8x7b-Instruct's performance, and Microsoft’s LIDA for LLM-powered data visualization.
keywords: [grab, vllm, playwright, mixtral, ast-grep, lida, github copilot]
---

This week, I learned:

- 
  - Grab. Improving last mile delivery in maps. When did people pick up the phone, when should driver be allocated to minimize waiting time, layer on top of OSM.
  - Singapore developers the Sea Lion 7b model
  - Try VLLM with AWQ format. Can do batch inferencing. Needs a good GPU
  - Amex prediction whether they can pay back in 1 year or 18 months. That choice is a business decision. In real time. Precompute individual score and use it as input to another model. Model must be explainable by regulation. Creates decision tree models therefore. Compliance team must agree if I can use a feature. Can't use gender. Age (in US, Canada);- high age is more risk. Can't use edu level in the US.
  - Capture information from camera and use LLMs. Like traffic cameras mapping. Explore GIS from video cameras
  - Grab tracks road closures and road accidents and whether a cycle can go on a road vs a bike vs a car
  - All drivers have a front facing camera
  - Drivers report road accidents by pressing a button
  - Amex prices individual loans when selling to a collection agency
  - #TODO buy a bike head camera!
  - [Playwright](https://playwright.dev/) is a browser-based test framework. Supports recording.
- [OpenAI provides logprobs for tokens](https://platform.openai.com/docs/api-reference/chat/create#chat-create-logprobs)! This can be a used to create cool visualizations of the likelihood of the each tokens.
- [Github Copilot's new features](https://youtu.be/SZVCJRUADc4) makes your entire workspace or a specific file its context. It also auto-writes your commit messages and PR descriptions.
- [Mixtral-8x7b-Instruct](https://huggingface.co/TheBloke/Mixtral-8x7B-Instruct-v0.1-GGUF) "... really does seem to be equivalent in quality to ChatGPT 3.5." [Ref](https://simonwillison.net/2023/Dec/14/ai-trust-crisis/)
- Practical AI podcast
  - Advent of Gen AI is going on. Explore
  - add to tools in data science course. Model validation
  - write a book as an open source to github repository. Easier to evolve and easier to get feedback on..
  - Explore utterances as a GitHub commenting platform
  - automatically give credits to contributors who have center pull request that was accepted or an issue that was fixed. This encourages contribution
  - Visit book.premai.io
- ast-grep is a semgrep alternative that focuses on code refactoring rather than security. Comby is another such tool
- [Serply](https://serply.io/) is a Google Search API alternative to Google CSE
- ⭐ [Generate textbooks](https://github.com/VikParuchuri/textbook_quality)!
- ChatGPT is good at generating questions or training datasets. It genuinely creates them rather than replicating from memory. [Ref](https://arxiv.org/pdf/2304.14334.pdf)
- [v0.dev](https://v0.dev/) creates web pages from code. [Example](https://v0.dev/t/XNlTLb7).
- [LIDA](https://microsoft.github.io/lida/) from Microsoft is an LLM based data visualization tool.
