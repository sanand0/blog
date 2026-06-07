---
title: Things I Learned - 18 Feb 2024
date: 2024-02-18T00:00:00+00:00
categories:
  - til
description: I explored Docker memory footprints on WSL2, the economics of LLM fine-tuning, and techniques like two-pass generation for structured data. I also learned about CCTV-integrated alerts, graph databases, and why ad networks are ditching Vickrey auctions.
keywords: [docker, wsl2, llm, fine-tuning, python, data-quality, ad-tech, graph-databases]
---

This week, I learned:

- Fine tuning makes economic sense only if the input tokens SAVED is twice the output token size on each call.
- Docker container memory usage on WSL2 `docker stats`
  - frolvlad/alpine-glibc:alpine-3.17: 540KB
  - ubuntu: 1MB (python3: +5MB)
  - nikolaik/python-nodejs:python3.10-nodejs18-bullseye: 1.4MB (python3: +5MB)
  - python:3-alpine: 612KB (python3: +7.5MB)
  - python:3: 500KB (python3: +11.2MB)
  - continuumio/miniconda3: 7.6MB (+6.5MB)
- Discussion with Vinu Yamunan
  - Databuck by FirstEigen. Autolysis plus monitoring
  - Quality council has the data steward (maintainer of each dataset) coming together with the uses on a weekly basis to understand what quality problems to users are facing. Data owners jaundice at a lower frequency to get an understanding
  - #TODO Automate rules for data quality in our projects and intranet
  - Convert a config rule into business language. Explain SQL. These are good use cases for llm's
  - Graph DBs are powerful for flexible data structures, but query generation needs AI or expertise. Check the Neo4J language cypher
  - Explore storing SAME data in relational DBs AND in graph DBs / document DBs for different use cases
  - Dallas rocketry challenge. Build a rocket that can take an egg to 800 feet exactly and land without breaking it
- Discussion with Karthik A
  - #TODO Ask IIT students to do internship tasks. Use advent of code is a qualifying criterion
  - Tata motors unionized DB admins for longevity. No one can take their jobs. Hires people who LIKE their jobs
  - Rust gives me typing. It's very efficient. Pola.rs is interesting but Pandas as good enough.
  - Explore alerts from CCTV feeds. Karthik sends email alerts with pictures for:
    - "Is the machine on or off"? for productivity
    - "Are people not wearing helmets?" for safety at Cummins
  - #TODO Integrate with WhatsApp. Use LLMs with function calling for responses
  - Use expiring links (to pictures or content). It increases engagement
  - Check Deno licensing. Is there a commercial clause? #ANS No - it's MIT license
  - Centre or excellence for zero emission tech at IIT. Karthik is part of it
  - Explore auth0. 7000 users are free
  - `toml` is part of the Python 3.11 standard library!
  - If copilot writes code we don't understand we are screwed. Hence expertise matters
- Discussion with Vikas Kedia
  - #TODO Plan an AMA
  - The mind becomes lazy with financial success. Vikas is treating his podcast as a startup
  - Hire a professional videographer for your content
  - Financial RoI in financial markets is the highest. Programming is high too but FS is even better
  - "Performative power" -- when you're forced to perform, you get better ideas
- [Observable 2.0 is an open source static site generator for data](https://observablehq.com/blog/observable-2-0)
- [Python dataclasses](https://docs.python.org/3/library/dataclasses.html)
- [SORA](https://openai.com/sora) is OpenAI's video generation model, and is stunning!
- If Appa comes to Singapore even for a week, he will feel better and can boast to his friends. At over 90, it may be better to move Appa to where I am since many of his friends would be no more and shops, doctors, etc can be managed and getting an independent house nearby is not hard.
- There is an SEZ in Gujarat where Indians can invest like in Mauritius without forex restraint
- Shubha: Media sites are moving away from Vickrey auctions to first-price auctions for ads. That's because they send the auction price _forward_ to a search engine and the winning second-price value can lose even though the owner is willing to pay more. Second-price auctions don't work unless ALL bidders are in the SAME auction. Ad networks are a hierarchy of auctions!
- [Gemini 1.5 launched](https://developers.googleblog.com/2024/02/gemini-15-available-for-private-preview-in-google-ai-studio.html).
- [Fly.io offers GPU hosting](https://fly.io/blog/gpu-ga/) and auto stop when they have nothing to do.
- Embeddings in random forest are very effective at classification -- much better than dot product.
- To deploy apps with OAuth + templating support in a small Docker container, use Caddy
- Deno has native TypeScript, browser APIs, and compiles to multiple OSs
- Ruff is a MUCH faster flake8
- [Two pass generation](https://minimaxir.com/2023/12/chatgpt-structured-data/#two-pass-generation) is a clever technique to get multiple SEQUENTIAL answers in a single API request. For example the schema `{'code', 'optimized_code'}` will generate `code` and then optimize it.
- [Unions in function calling](https://minimaxir.com/2023/12/chatgpt-reestructured-data/#unions-and-chain-of-thoughts) allows flexible multi-step prompts in a single API.
