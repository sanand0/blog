---
title: Things I Learned - 10 Aug 2025
date: 2025-08-10T00:00:00+00:00
categories:
  - til
description: I explored OpenAI's custom tool types for DSL generation, new Node.js 2025 features like single-executable bundling, and Markdown directive syntax. I also shared my Claude Code usage costs and thoughts on vibe coding.
tags: [openai, node-js, claude-code, markdown, ai-coding]
---

This week, I learned:

- OpenAI supports a tool `"type": "custom"` that lets it write code as an argument to a tool call. Great for code / SQL generation. Even more powerfully, you can generate output following specific grammars, e.g. STL files, PostgreSQL dialect, Mermaid/PlantUML diagrams, OpenAPI specs, Vega-Lite JSONs, Cron expressions, GraphQL SDLs, Dockerfiles, Terraform HCLs, or any DSL! [#](https://cookbook.openai.com/examples/gpt-5/gpt-5_new_params_and_tools) #ai-coding
- The OpenAI playground has a [GPT-5 Prompt Optimizer](https://platform.openai.com/chat/edit?models=gpt-5&optimize=true) that can migrate prompts to GPT-5.
- [Docsify 4.13.1](https://www.npmjs.com/package/docsify/v/4.13.1) is 2 years old and [uses](https://github.com/docsifyjs/docsify/blob/v4.13.1/package.json#L68) [marked@1.2.9](https://www.npmjs.com/package/marked/v/1.2.9) which is 5 years old. Newer plugins like [marked-directive](https://www.npmjs.com/package/marked-directive) don't work with it. Though [docsify v5.0.0-rc1](https://github.com/docsifyjs/docsify/tree/v5.0.0-rc.1) is in development, it may be the better option for modern Markdown plugins. [Here's sample code](https://github.com/sanand0/smartart/blob/e4c5bb88eba3aa3cd92d6711a9e29935cc36e62f/script.js).
- CommonMark has a _powerful_ [directive syntax](https://talk.commonmark.org/t/generic-directives-plugins-syntax/444) proposal that lets you add classes, attributes, and arbitrary plugins to Markdown. For example, `:abbr[MD]{#id .class title="Markdown"}` for inline directives. Plugins exist for [marked](https://www.npmjs.com/package/marked-directive), [markdown-it](http://npmjs.com/package/markdown-it-directive) and [remark](https://github.com/remarkjs/remark-directive).
- [biomejs](https://biomejs.dev/) and [dprint](https://dprint.dev/) are gaining traction as [prettier](https://prettier.io/) alternatives. I'm yet to try them but keen to explore.
  - Skip biomejs for now. It uses tabs (not spaces) and does not respect .gitignore by default. Handling these is too much work.
- ⭐ Code generation is more flexible than tool calling. LLMs can't write a tool-call loop, for example, but they can write code to run an API in a loop. So, I like telling the LLM to "write code using these APIs" than giving it APIs to tool-call. #ai-coding
- `npx -y ccusage` is an easy way of summarizing your [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) usage and cost. My cost so far (since 21 July) is about $10. The median session cost is ~50 cents. Most of it ($7) was from a single temporary coding chat that I kept continuing for way too long, building up the context window. [#](https://github.com/ryoppippi/ccusage)
- [defuddle](https://github.com/kepano/defuddle) can be used in the browser to get the main content from web pages. A replacement for Mozilla Readability. [#](https://stephango.com/defuddle)
- [Modern Node.js Patterns for 2025](https://kashw1n.com/blog/nodejs-2025/) include these 5 features I'm excited by:
  - **Single-executable bundling**. `node --experimental-sea-config sea-config.json` builds standalone binaries.
  - **ES Modules**. Use `node:` prefix for built-in imports. `import { createServer } from 'node:http';`
  - **Watch mode**. Use `node --watch file.js` auto-reloads when `file.js` or dependencies change.
  - **Env file**. Use `node --env-file=.env` loads `.env` as environment variables.
  - **`node:test`** is a full-featured test framework with `--watch` and coverage.
- Concise explanations speed up decisions because they're faster to read and understand (obvious). They're also easier to combine with other ideas (less obvious). [#](https://stephango.com/concise)
- I've been uncertain about [htmx](https://htmx.org/) for some time now. This tutorial, [HTMX is hard, so let's get it right](https://github.com/BookOfCooks/blog/blob/master/htmx-is-hard-so-lets-get-it-right.md), convinced me that it's too far from my mental model, so I'm unlikely to ever use it.
- ⭐ Slow, effortful practice (spaced recall, interleaving topics, self-testing) builds lasting knowledge but looks inefficient and doesn't help with exams. [#](https://chatgpt.com/share/689180c7-03a0-800c-a5d4-5a455429e97f) #beliefs
- [GitDoc VS Code extension](https://marketplace.visualstudio.com/items?itemName=vsls-contrib.gitdoc) auto-commits and syncs notes. I dropped [gitwatch](https://github.com/gitwatch/gitwatch) in favor of this.
- It's interesting that Gemini Deep Research cannot access Google Drive while Gemini can. On the other hand, ChatGPT Deep Research can access Google Drive but ChatGPT cannot.
- A trend that AI coding will only accelerate: "It is now possible for tiny teams to make principled software that millions of people use, unburdened by investors. ... you need far less money and far fewer employees to reach far more customers. That wave is only just beginning." [#](https://stephango.com/vcware) #ai-coding
- Typed languages are better suited for vibe coding. This will likely lead to the growth of typed languages (TypeScript, Rust, Go) but also of typing in untyped languages (e.g. Python) [#](https://solmaz.io/typed-languages-are-better-suited-for-vibecoding) #ai-coding
- Instead of Celery, Redis, Kafka, etc. as task queues, we could the file system as a message queue. For example, `pending/task-01.json` moves to `wip/task-01.json` to `done/task-01.json`. Folders for state/tags, files for task details.
- [Foam](https://foambubble.github.io/) is a note-taking VS Code extension. The [WikiLinks](https://foambubble.github.io/foam/user/features/wikilinks), [tags](https://foambubble.github.io/foam/user/features/tags) and [backlinking](https://foambubble.github.io/foam/user/features/backlinking) features align _naturally_ with Markdown note-taking. Via [Steph Ango](https://stephango.com/vault) who uses Obsidian which nudged me to search for WikiLink-ing features in VS Code.
- I'm an open data hawk. But here are things I should remind myself of. [#](https://chatgpt.com/c/68901fb2-38b0-8333-9853-7e6c2fdaf97c)
  - **Privacy incubates creativity**. People self-censor when watched. Privacy shields fragile ideas.
  - **Power assymetry**. Big players can leverage openness more, e.g. Cambridge Analytics + Facebook data.
  - **Context matters**. What's harmless in one setting can be toxic in another.
  - **One-way door**. Data can't be unshared. Don't scrap brakes dreaming of perfect roads. Anticipate tyrannical regimes / cultures.
  - **Not your call**. You don't share your neighbour's medical records.
- [One Punch Man](https://en.wikipedia.org/wiki/One-Punch_Man) is available as [manga](https://onepunchmanmangaa.com/). I watched the anime first and assumed that came first. Apparently not.
- ⭐ In "kind" environments (stable rules, rapid and accurate feedback), specialize. In "wicked" environments (rules shift, feedback is noisy/late), generalize. [ChatGPT](https://chatgpt.com/share/68902bbf-bf58-800c-b6b5-9ae787fa9c26)
- Models' ability to orchestrate longer workflows will improve. Factor that into your application design. Claude Code can already handle over 70 tasks in a workflow
- What happens when LLMs play Chinese Whispers / the [Telephone Game](https://en.wikipedia.org/wiki/Telephone_game)? Here are learnings. [ChatGPT](https://chatgpt.com/share/68904271-6d10-800c-9084-8ae28668df92)
  - Drift increases faster than linear with hops.
  - Bigger models do better, but constrained prompts (“Copy the text exactly; change nothing.”) have a bigger impact.
  - Low temperature improves copying fidelity.
  - But even after "forgetting", LLMs reproduce rare content if they're trained on it.
- "In fact, React Native looks set to become the most engine-agnostic JavaScript runtime around". [The Many, Many, Many, JavaScript Runtimes of the Last Decade](https://buttondown.com/whatever_jamie/archive/the-many-many-many-javascript-runtimes-of-the-last-decade/)
- [OMDb](https://www.omdbapi.com/) (simple) and [TMDb](https://www.themoviedb.org/) (comprehensive) are API-friendly alternatives to the IMDb.
- [copyparty](https://github.com/9001/copyparty) seems one of the most feature-rich file servers out there. Single Python file, runs on any OS, works with any client, and optimized for speed. [Video](https://youtu.be/15_-hgsX2V0)
- Quotes I enjoyed from [Linus Torvalds' TED interview](https://youtu.be/o8NPllzkFhE)
  - I want to not have external stimulation. You can kind of see, on the walls are this light green. I'm told that at mental institutions they use that on the walls. It's like a calming color. ... the main thing I worry about in my computer is -- it really has to be completely silent. If the cat comes up, it sits in my lap. And I want to hear the cat purring.
  - I did not start Linux as a collaborative project. I started it as one in a series of many projects I had done at the time for myself, partly because I needed the end result, but even more because I just enjoyed programming.
  - I'm actually not a people person. But I do love other people who comment and get involved in my project.
  - The big point for me was not being alone and having 10, maybe 100 people being involved. Going from 100 people to a million people is not a big deal -- to me. Well, I mean, maybe it is if you want to sell your result then it's a huge deal. But if you're interested in the technology and you're interested in the project, the big part was getting the community.
  - So Git is my second big project, which was only created for me to maintain my first big project. And this is literally how I work.
  - Well, I do code for fun -- but I want to code for something meaningful so every single project I've ever done has been something I needed.
  - Apparently, my sister said that my biggest exceptional quality was that I would not let go.
  - I can't do UI to save my life.
  - Good taste is about really seeing the big patterns and kind of instinctively knowing what's the right way to do things.
  - Companies like Google and many others have made, arguably, like, billions of dollars out of your software. Does that piss you off? No. No, it doesn't piss me off for several reasons. And one of them is, I'm doing fine. But the other reason is -- I mean, without doing the whole open source and really letting go thing, Linux would never have been what it is.
  - I think one reason open source works so well in code (is that ...) Code either works or it doesn't.
- The [Uses This](https://usesthis.com/) site has interviewed professionals for decades. From their [repo](https://github.com/waferbaby/usesthis) I scraped the top developer apps post 2020:
- CloudFlare has an Iceberg data catalog in [R2 Data Catalog](https://developers.cloudflare.com/r2/data-catalog/). Iceberg is like Parquet but supports metadata, time-travel, and schema edits. But I'm yet to find a single publicly accessible Iceberg catalog. Its open-data adoption is not as high as Parquet's. [Apache Iceberg vs Parquet](https://chatgpt.com/share/688f0b61-f9d8-800c-a7c8-46410ab4f1ab)
- [Observable Notebook 2](https://observablehq.com/notebook-kit/) is the new notebook format from Mike Bostock. It is vanilla JS and embeddable into other pages. THis would have been a big deal 2 years ago, but with the LLM ecosystem today, I'm not sure if it matters as much.
- To add CORS support to CloudFlare pages protected by Zero Trust, add a [`_headers`](https://developers.cloudflare.com/pages/configuration/headers/) file to your repo. (This is different from the [Zero Trust CORS](https://developers.cloudflare.com/cloudflare-one/identity/authorization-cookie/cors/) which allows automated logins.) Sample `_headers` that lets logged-in users fetch pages via `fetch("...", { credentials: "include" })`:
  ```
  /*
    Access-Control-Allow-Credentials: true
    Access-Control-Allow-Origin: https://your-site.example.com
    Access-Control-Allow-Methods: GET, HEAD
    Access-Control-Allow-Methods: *
  ```
- As corporates restrict the use of LLMs, I see employees purchasing personal laptops to use LLMs on. An interesting trend!
- [`openai-python`](https://github.com/openai/openai-python) has a CLI. You can run `uvx openai api chat.completions.create --stream -m gpt-4.1-nano -g developer 'Translate to Chinese' -g user "Hello"` for example
- Anthropic has an [OpenAI compatible API](https://docs.anthropic.com/en/api/openai-sdk) at `https://api.anthropic.com/v1/`.
- Claude Code tips from [Things that didn't work](https://lucumr.pocoo.org/2025/7/30/things-that-didnt-work/) by Armin Rocher #ai-coding
  - Speech-to-text. Cannot stress this enough but talking to the machine means you’re more likely to share more about what you want it to do.
  - I maintain some basic prompts and context for copy-pasting at the end or the beginning of what I entered.
  - I ended up preloading executables on the PATH that override the default ones, steering Claude toward the right tools, e.g. running `python` asks it to use `uv`.
  - I use the task tool frequently for basic parallelization and context isolation.
  - Simply taking time to talk to the machine and give clear instructions outperforms elaborate pre-written prompts.
  - Forcing myself to evaluate the automation has another benefit: I’m less likely to just blindly assume it helps me.
- Research indicates that we don't know in advance which prompts will help. Evals beat prompt engineering. [Ethan Mollick](https://bsky.app/profile/emollick.bsky.social/post/3lvgwdwn7422w)
