---
title: Things I Learned - 01 Dec 2024
date: 2024-12-01T00:00:00+00:00
categories:
  - til
---

This week, I learned:

- Gists are a good place to store static files for posterity as well as throwaway files. But, they're just git repositories. So there may be no advantage over GitHub repos.
- GPT-4o Audio supports tone control via XML tags like `<cough>...`, `<laugh>...`, etc. But at ~$15/hr of output, it's too expensive. [Ref](https://x.com/ilanbigio/status/1861913173432946808)
- Mridula's son gave a live commentary of what he was doing on Minecraft and ChatGPT gave him live evaluation and coaching. E.g. “Great strategy! Getting to the launch pad early can give you a huge mobility advantage. Making the bridge wider is also a smart move to prevent accidental falls. With this plan, you’re setting yourself up for success. This is a great way to interact with LLMs.
- Gemini's JSON mode returns JSON with keys in alphabetical order. I think. Emperical evidence. This is unlike OpenAI which explicitly returns the keys in the order specified.
  - To solve this, order the keys alphabetically.
- HTMX focuses on HTML over JS. Like server responses being HTML snippets not JSON. But I need front-end over back-end. Client side apps. HTMX doesn't help much there, e.g. templating, or just plain JS code.
  - [htmx client side templates](https://v1.htmx.org/extensions/client-side-templates/) do can convert JSON to HTML.
- I installed the [OpenAI Desktop App](https://openai.com/chatgpt/desktop/) as well as [Claude for Desktop](https://claude.ai/download). They take up too much RAM (260MB and 750 MB respectively on startup - though this varies.) The ChatGPT web page takes ~100MB incrementally, so I wrote an [AutoHotkey script](https://www.autohotkey.com/) to switch to the first open (or recently closed) ChatGPT tab on [Brave](https://brave.com/).
- I tried [LIDA](https://microsoft.github.io/lida/) from Microsoft, after almost a year of its release. A few notes:
  - Just running `uvx lida ui --port 8080 --docs` works.
  - But I needed to use `export TCL_LIBRARY=C:/Users/Anand/AppData/Roaming/uv/python/cpython-3.13.0-windows-x86_64-none/tcl/tcl8.6` to point it to my TCL installation for charts to work. I also chose to `export OPENAI_BASE_URL=https://llmfoundry.straive.com/openai/v1`
  - I also chose to replace `gpt-3.5-turbo-0301` (the default model) with `gpt-4o-mini` in `lida/web/ui/component*`
  - It's quite impressive.
- OpenAI allows multiple system messages. I learned this browsing through the LIDA prompts.
- Anthropic's [Model Context Protocol](https://www.anthropic.com/news/model-context-protocol) lets any apps integrate with LLM Apps. LLM Apps are becoming the new operating system. Competitors, beware.
- I spoke at [Automating Data Visualizations using LLMs](https://www.meetup.com/data-vis-singapore/events/304516458/) at SUTD. Apparently, using LLMs to write code is much more common than writing code to use LLMs. I ran a quick quiz.
  - Have you used ChatGPT or any LLM? 35 / 35 raised their hands.
  - Have you written code using an LLM? 34 / 35 raised their hands. (I was impressed.)
  - Have you uploaded a spreadsheet to an LLM for analysis? 15 / 35 raised their hands.
  - Have you programmatically called an LLM API? 6 / 35 raised their hands.
- With LLMs, fostering innovation is a new path to profitability. Companies are increasing innovation team sizes. Productionizing that is the next. Some initiatives are:
  - Convert popular demos into starter kits
  - Create and evangelize trainings on solutions and solution techniques
  - Create larger pools of capacity to build innovation and productionize it
- [Andrew Ng Explores The Rise Of Al Agents And Agentic Reasoning | BUILD 2024 Keynote](https://youtu.be/KrRD7r7y7NY)
  - Innovation is now a path to production. People are able to build 20 prototypes at the cost of one and see which sticks
  - Machine learning is much faster. Things that took months now date days. But engineering and evaluations are only slightly faster and have become a bottleneck
  - A good analogy to zero shot prompting is to ask a person to write an entire essay without pressing backspace even once
  - Andrew scenes to align with the line chain definition of agentic workflow, which is about agents being able to craft their own control flows
  - People find it very easy to understand agentic workflows once they read through the code
  - Reflection or feedback is a useful agentic pattern
  - In multi-agent collaboration, it may be the same underlying model that is acting as different agents. But just like we find it useful for the same CPU to run multiple processes and each application is its own abstraction, agents of useful abstraction
- It's hard to summarize a large document using RAG. But you can directly add answers to such questions into the corpus, e.g. by adding a "summary" section, and other answers to common questions.
- CloudFlare workers can bundle any kind of files, including text, data, and WASM. [Docs](https://developers.cloudflare.com/workers/wrangler/configuration/#bundling)
- AssemblyScript can compile TypeScript to WASM. [Here's what I learnt](https://github.com/sanand0/assemblyscript-tutorial)
- Here's a convenient pattern to `git commit` a directory but nothing else in it (e.g. a `build/` directory). Add a `.gitignore` file with `*` followed by `!.gitignore`. Only the `.gitignore` file is tracked.
- [Ultravox](https://www.ultravox.ai/) lets you build voice agents at 5c/min = $3/hr (OpenAI is 6c input, 24c output). Or [clone their repo](https://github.com/fixie-ai/ultravox).
  - Idle call time is counted towards cost. So cost may be higher than OpenAI.
  - Voice cloning quality is average. Very distinctive voices are just partly identifiable.
  - Supports tool calls (from their server).
  - Their API is simple but the docs have minor errors (e.g. a trailing comma in the JSON, which leads to an error) reducing confidence.
- LLMs may be good at derived data generation. For example, given a database schema, what derived columns would be useful? What derived views would be useful?
- The O1 model does not have a mechanism to control the amount of tokens to spend on reasoning. DeepSeek R1 might, but the API is not out yet.
- The [OpenAI Desktop App](https://openai.com/chatgpt/desktop/) can interact with native applications, e.g. read from Terminal, VS Code, etc. This takes it on a path to becoming a copilot for ANY apps. Putting every copilot app and every LLM integration under threat.
- [Crawl4AI](https://crawl4ai.com/mkdocs/) and [Firecrawl](https://docs.firecrawl.dev/) are tools / libraries to convert websites into LLM Friendly Markdown and extract structured data using LLMs.
- Don't try and solve specific problems. Pass the entire context to an LLM and get a comprehensive solution. Most doctors, for example, ask specific search-like questions instead of uploading the entire case history and asking for a diagnosis, and perform workse than LLMs. [Ethan Mollick](https://www.oneusefulthing.org/p/getting-started-with-ai-good-enough)
