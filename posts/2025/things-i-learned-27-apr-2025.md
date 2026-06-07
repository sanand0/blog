---
title: Things I Learned - 27 Apr 2025
date: 2025-04-27T00:00:00+00:00
categories:
  - til
description: I explored OpenAI reasoning models, Promptfoo for evals, and terminal tools like cmdg and gcalcli. I also learned about Python’s new t-strings, optimized my fish shell startup, and tested the Unsure Calculator for modeling range-based estimates.
keywords: [openai, promptfoo, rwkv, cmdg, gcalcli, duckdb, nix-flakes, python]
---

This week, I learned:

- OpenAI's reasoning models are much ahead of other models when multiplying two numbers in their heads. [Ref](https://sanand0.github.io/llmmath/)
- ⭐ [Promptfoo](https://promptfoo.dev/) may be the most mature open source LLM evals tool. [Simon Willison](https://simonwillison.net/2025/Apr/24/exploring-promptfoo/)
- [Dyson Sphere](https://en.wikipedia.org/wiki/Dyson_sphere).
- [LemonSlice](https://lemonslice.com/live) showcases real-time audio-video models (avatars) that are close enough to real.
- Notes from [Latent Space ICLR 2025, Singapore](https://iclr.cc/)
  - Daniel: [Menlo's ReZero](https://github.com/menloresearch/ReZero). A model that _keeps_ searching till it finds the answer.
    - There are multiple search techniques: Multi-step retreival, Iterative retrieval, Query rewriting. Also, reasoning.
    - The LLM token generation sequence is normally: `<think>, <search>, <answer>`.
    - Insight: "If we explicitly reward LLMs for retrying after a failed search, they out-perform one-attempt systems." So `<think>, <search>, <think>, <search>, <think>, <search>, <answer>`.
    - ⭐ Prompt reasoning models, e.g. "Keep searching till you find the best answer."
  - Roger, Nous Research
    - Supervised learning is limited because accuracy is piece-wise linear, i.e. it's broken up. Continuous optimization is meaningless.
    - Reinforcement learning works better because rewards can be discrete. (But it converts things back into differentiable loss functions behind the scenes.)
      - Rewards can be good/bad. Single or multi-step. Whatever.
    - We're in the "Era of experience", i.e. models gain experience from the environment themselves.
    - ⭐ So, we need environments models can learn in. This is the next thing after training data. That needs a standard for environments.
    - We'd need a model, a trainer, and the environment.
    - The environments whatever capabilities. Run code. Browser. A game. ... With an exposed interface
  - Eugene Cheah (Featherless.ai)
    - Transformer architectures need n-square GPUs as # of tokens grow. Featherless is exploring an RWKV architecture that scales linearly. THere are other such architectures. Performer, Linformer, Reformer, Hyena.
    - Mistral-Nemo-12b-ic is one of the most popular fine-tuned model. It's small enough to run on a server.
  - Justus Mattern (Prime Intellect)
    - Intellect-2 is a continously learning (RL) model that uses decentralized training on peer-to-peer GPUs.
    - Solving problems on bandwidth, verifiable contributions, etc.
- ChatGPT Deep Research now also has an O4-Mini version to serve smaller reports. Free users get 0 original + 5 lightweight 5 tasks / month. $20 version gets 10 + 15. $200 version gets 100 + 150. The month begins on first use of Deep Research and runs on a 30 day "window". [Ref](https://help.openai.com/en/articles/10500283-deep-research-faq)
- O4-Mini-High is great at going through an under-documented repo and finding things. For example, [here's how I configured `cmdg`](https://chatgpt.com/share/680b3d21-0188-800c-a0bf-8b44a1edd919).
- ChatGPT is my new Jupyter Notebook :-)
- Google announced new AI capabilities at Google Next APAC 2025. [Blog](https://workspace.google.com/blog/product-announcements/new-AI-drives-business-results). Interesting ones are:
  - @Gemini in chat
  - Google Meet support for "Catch me up"
  - Google Vids: Create short video clips
  - Google Sheets: does better analysis
  - Google Slides: image generation
  - Google Docs: Create Audio Clips (like NotebookLM in Google Docs)
  - Google Docs: "Help me refine" is better than before
  - Google Workspace Flows
- [gcalcli](https://github.com/insanum/gcalcli) is a convenient way to export Google Calendar. Example: `uvx gcalcli agenda --tsv 2025-01-01 2025-01-05`
- [cmdg](https://github.com/ThomasHabets/cmdg) is a command line GMail client that I've now switched to for quick email checks. 80% of my email is spam and this is good enough to scan and delete those. It also avoids running a 200-500 MB tab in the browser that constantly shows me how many unread emails I have.
- From [Worklife with Adam Grant: Cancelling cancel culture with Loretta Ross](https://shows.acast.com/worklife-with-adam-grant/episodes/cancelling-cancel-culture-with-loretta-ross)
  - "Lighten up! Fighting Nazis should be fun. It's being a Nazi that sucks. If you're not having fun fighting for hope and joy and human rights, maybe you're doing the fight wrong. We are the ones who should be having fun."
  - "You can say what you mean. But you don't have to say it mean." There is always a way to put it across better. Refusing to say mean things is about to discover these approaches.
  - "The true mark of a lifelong learner is knowing that you can learn something from every single person you meet." If you remember that, you can't be a know it all.
- [semantic-text-splitter](https://pypi.org/project/semantic-text-splitter/) could be the go-to text splitter. It's Rust-based, supports MarkdownSplitter, and multiple tokenizers. Alternatives like [semchunk](https://pypi.org/project/semchunk/), [advanced-chunker](https://pypi.org/project/advanced-chunker/), [chonkie](https://github.com/chonkie-inc/chonkie), etc. seem clunkier.
- ULID is like UUID but time-sortable. That's an improvement over timestamp IDs (definitely) and potentially even UUIDs. They can be generated by clients as a globally unique ID. Try [`pip install python-ulid`](https://github.com/mdomke/python-ulid) and [`npm install ulid`](https://github.com/ulid/javascript).
- The [Consumer Product Safety Commission Data](https://www.cpsc.gov/Data) has thousands of reports of product safety over time
- You can run `xclip -sel clip -o | pandoc -f markdown -t html --no-highlight | xclip -sel clip -t text/html -i` to convert Markdown in the clipboard to rich text. But `xclip` doesn't support multiple selections, so the text is lost. [ChatGPT](https://chatgpt.com/share/68071421-07a4-800c-a286-0d8b624c27e4)
- [DuckDB UI & Notebooks](https://duckdb.org/2025/03/12/duckdb-ui.html) will potentially be a good alternative to Datasette, DBeaver, etc. But for now, there are still glitches. It crashes with a `SIGSEGV (Address boundary error)` when connecting to SQLite databases.
- Ollama limits MAX_TOKENS to 2K by default.
- AI assisted search helps wherever I would have used Google, e.g.
  - Debugging. "Fix CUDA initialization: CUDA unknown error"
  - Tool search. "Find an online word counter tool."
  - Library search. "Find a JS micro library to render Markdown."
- OpenAI API capabilites lag ChatGPT features. For example:
  - `o4-mini` via the API does _not_ search the web natively as part of its reasoning.
  - `o4-mini`, `o3`, `o3-mini`, `o1`, `gpt-4.1-nano` don't yet support the `web_search_preview` tool. Only `gpt-4.1` and `gpt-4.1-mini` do. [Limitations](https://platform.openai.com/docs/guides/tools-web-search?api-mode=responses#limitations)
  - Search results are NOT visible via the API. They're fed directly to the model. The number of searches or results is unknown. Each search costs 0.25-0.5 cents. [Pricing](https://openai.com/api/pricing/)
  - For reasoning traces (e.g. `.reasoning.summary: "medium"`) you need to verify your organization via [withpersona.com](https://withpersona.com/) which failed with my Indian passport AND Singapore work permit.
- The ChatGPT Plus plan ($20) gives you 50 O4 mini messages a day, which I exceeded!
  It's supposed to reset at midnight UTC [Ref](https://community.openai.com/t/limitations-on-the-openai-o-series-reasoning-models-on-chatgpt/1230183/2)
  but might operate on a rolling window [ChatGPT](https://chatgpt.com/share/68070ba9-04c0-800c-901e-c3c6e8048f9d).
  "Currently, there is no way to check how many messages you have used in your usage budget."
  [OpenAI](https://help.openai.com/en/articles/9824962-openai-o3-and-o4-mini-usage-limits-on-chatgpt-and-the-api)
- [SignalBloom](https://www.signalbloom.ai/) reads SEC filings and writes analyst reports on it using LLMs
- "Evaluation in the loop" or "Evals-in-the-loop" is a new term I learnt. [SignalBloom's Hallucination Bechmark](https://www.signalbloom.ai/hallucination-benchmark)
- If AI interacts with the world and generates data from its own experience and learns from that, we have a new scaling mechanism. [DeepMind podcast](https://youtu.be/zzXyPGEtseI)
- OpenAI's search API is fairly expensive at $30+/1K calls. Typically, to read interesting HN articles, I will make 30 calls which is about 75c. Instead I should use the app and summarise HM news across different days manually based on my interests!
- Finally! [t-strings](https://davepeck.org/2025/04/11/pythons-new-t-strings/) land in Python. They're like JavaScript template literals.
- DuckDB's CSV parser might be one of the most forgiving parsers. Even better than Pandas or SQLite3. [Ref](https://duckdb.org/2025/04/16/duckdb-csv-pollock-benchmark)
- Good managers will probably make good AI managers. AI agents can probably substitute humans in business experiments. [Ethan Mollick](https://bsky.app/profile/emollick.bsky.social/post/3lmhuceiyfk2a)
- If Windsurf stops working, reload the extension. [GitHub](https://github.com/Exafunction/codeium/issues/59#issuecomment-2690290023)
- TLS certificates will start expiring in 47 days from 15 Mar 2029, forcing automated domain renewals. [Digicert](https://www.digicert.com/blog/tls-certificate-lifetimes-will-officially-reduce-to-47-days)
- [Nix flakes](https://wiki.nixos.org/wiki/Flakes) are a reliable alternative to [DevContainers](https://containers.dev/) that don't need Docker - but don't work on Windows.
- [Ink](https://github.com/vadimdemedes/ink) is like React for the CLI.
- The [Unsure Calculator](https://filiph.github.io/unsure/) is a great tool to calculate formulas with _multiple_ uncertainties, like:
  - My office is 9-11 km away and it takes me 45-55 min to reach. So I cycle at `9~11 / 45~55 * 60` ~ 10-14 kmph (12 most likely).
  - I spend $6-15 on lunch and eat out 80-120 days a year. So I spend `6~15 * 80~120` ~ $600~1550 ($1000 most likely) eating out yearly.
  - I take 30-120 min to prepare a quiz question. Each exam has 6-12 questions. So I need `30~120 * 6~12 / 60` = 4~20 hours (11 most likely)
- Using Kiran's [macOS setup for dev](https://jackerhack.ing/notes/202412051824-macos-setup-for-dev) I [enabled](https://github.com/sanand0/scripts/commit/ae95013019374a3b542ef5a93ea2f4295d0d86c4) colorized less and mouse options for tmux.
- `time fish -i -c exit` prints the time taken for fish startup. `fish --profile-startup ~/fish.profile -i -c exit` prints the time taken by each command on fish startup to `~/fish.profile`. I used this to [speed up my fish startup](https://github.com/sanand0/scripts/commit/90d34b7239197d69c3502d1e847b79dd503c1b72).
- The 8 top features of the [OpenAI Responses API](https://platform.openai.com/docs/api-reference/responses) that are an improvement over the Completions API (IMHO) are:
  - Link to previous response rather than sending history
  - Uploading files directly
  - Swappable system instructions while retaining the chat history
  - Customisable reasoning effort AND reasoning summary detail
  - Truncation in the middle option
  - Web search context size option
  - File search filters by file attributes
  - Flex service tier for lower cost
- OpenAI doesn't charge for file storage but _does_ charge 10 cents / GB-day for vector storage beyond 1 GB. The first 1GB is free
- [Augment Code](https://www.augmentcode.com/) is an AI code editor that's growing popular on Reddit. #ai-coding
- The GPT 4.1 models have a 75% discounted prompt caching (instead of the usual 50%), making them particularly suited for repetitive tasks. [OpenAI](https://openai.com/index/gpt-4-1/)
- [chatgpt.com](https://chatgpt.com/) shortcut keys are revealed via `Ctrl + /`. Here's my ranking on usefulness:
  - `Ctrl + Shift + C`: Copy last response as Markdown!
  - `Ctrl + Shift + ;`: Copy last code block
  - `Ctrl + Shift + S`: Sidebar toggle
  - `Ctrl + Shift + O`: Open new chat
  - `Shift + Esc`: Focus chat input
  - `Ctrl + Shift + I`: Ccustom instructions
  - `Ctrl + Shift + X`: Delete chat
