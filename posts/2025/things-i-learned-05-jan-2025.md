---
title: Things I Learned - 05 Jan 2025
date: 2025-01-05T00:00:00+00:00
categories:
  - til
description: I explored management philosophies, reverse-engineered APIs with mitmproxy2swagger, and compared LLM observability tools like LiteLLM and LangFuse. I also tested speech-to-text options and gathered tools for converting local files into LLM-friendly prompt contexts.
keywords: [mitmproxy, litellm, langfuse, git submodules, vector databases, assemblyai, management philosophy, deepseek]
---

This week, I learned:

- Some management philosophies used to be successful but are no longer as effective. [ChatGPT](https://chatgpt.com/share/6778b5f9-f1e4-800c-a1f7-30dcdfdccdaa)
  - Command-and-control hierarchy
  - Taylorism: deep specialization
  - Seniority-based advancement
  - Annual performance reviews (without continuous feedback)
  - Up-or-Out promotion models
  - Confidential strategic information
  - Narrow job descriptions
  - Relying on formal authority
- Some management philosophies have been around for millenia. [ChatGPT](https://chatgpt.com/share/6778b5f9-f1e4-800c-a1f7-30dcdfdccdaa)
  - Lead by example
  - Fairness and empathy
  - Clear, consistent communication
  - Delegation and empowerment
  - Strategic planning and foresight
  - Consistent rule enforcement
  - Rewarding merit
  - Leadership by virtue and character
- [Interview with Liang Wenfeng, CEO of DeepSeek](https://www.chinatalk.media/p/deepseek-ceo-interview-with-chinas):
  > In the face of disruptive technologies, moats created by closed source are temporary. Even OpenAI’s closed source approach can’t prevent others from catching up. So we anchor our value in our team -- our colleagues grow through this process, accumulate know-how, and form an organization and culture capable of innovation. That’s our moat.
  >
  > Open source, publishing papers, in fact, do not cost us anything. For technical talent, having others follow your innovation gives a great sense of accomplishment. In fact, open source is more of a cultural behavior than a commercial one, and contributing to it earns us respect. There is also a cultural attraction for a company to do this.
  >
  > Why is Silicon Valley so innovative? Because they dare to do things. When ChatGPT came out, the tech community in China lacked confidence in frontier innovation. From investors to big tech, they all thought that the gap was too big and opted to focus on applications instead. But innovation starts with confidence, which we often see more from young people.
- [mitmproxy](https://mitmproxy.org/) is an open source tool to intercept, modify, and replay HTTP requests. An alternative to [Charles](https://www.charlesproxy.com/), [Fiddler](https://www.telerik.com/fiddler), and partly [WireShark](https://www.wireshark.org/). [Guide](https://earthly.dev/blog/mitmproxy/). Like the others, it requires installing a trusted root certificate on your machine.
  - [mitmproxy2swagger](https://github.com/alufers/mitmproxy2swagger) digs through the mitmproxy flows and generates an OpenAPI schema. A clever idea to reverse-engineer APIs.
- [Matomo](https://matomo.org/), [PostHog](https://posthog.com/), [Umami](https://umami.is/) and [Plausible](https://plausible.io/) are open source web analytics tools (like Google Analytics).
- [Redash](https://redash.io/) and [Metabase](https://www.metabase.com/) are new open source data visualization tools sitting alongside [Grafana](https://grafana.com/) and [Apache Superset](https://superset.apache.org/).
  - Redash feels too clunky / enterprise-y rather than open-source-y.
- From [Ego is the enemy](https://www.goodreads.com/book/show/27036528-ego-is-the-enemy):
  - Add a daily habit to understand your ego. Where and how is it showing up? How are you fooling yourself? Where are you fighting battles without knowing the war?
  - Speak less. Do more. E.g. Release more, blog less. Review, THEN publish.
  - Always have a teacher, a student, and a peer to compete with. That's how you learn.
  - "It is impossible for a man to learn what he thinks he already knows" - Epictetus.
  - Passion makes you blind. Purpose and realism are less so. Delegate, take help, take feedback.
- [Assembly AI](https://www.assemblyai.com/) offers speech to text with diarization at 12c/hour. Good diarization, average transcription quality.
  In comparison, WhisperX (with GPU) was much slower, had slightly poorer diarization, and slightly better transcription.
  ```bash
  uvx --python 3.9 --index https://download.pytorch.org/whl/cu121 whisperx --diarize --lang en --hf_token $HUGGINGFACE_TOKEN
  ```
- [Vector DB comparison](https://superlinked.com/vector-db-comparison) compares all popular vector DBs. LanceDB is gently nudging up my preference list but DuckDB is still my favourite.
- Does the cost of 'running' a paper/article in an LLM vary depending on the specific LLM used, such as Claude Sonnet? (FAQ)
  - Yes, the cost varies depending on the LLM. You can see costs and quality at https://llmpricing.straive.app/. The cost is measured in millions of tokens. For example, the Wikipedia page on the Bible is 100K tokens. You can paste text into https://platform.openai.com/tokenizer to count the number of tokens.Claude 3.5 Sonnet costs $3.5 / MTok, i.e. 35 cents for the Wikipedia Bible page. Gemini 1.5 Flash 8b costs $0.0375 / MTok, i.e. 0.375 cents for the same page. As you can see, the cost can vary by a factor of 100.
- A git repo with a submodule stores the specific commit of the submodule. When you update the submodule, you need to `git add` the submodule.
  - `git pull --recurse-submodules`: Pulls parent repo along with submodules
  - `git submodule status`: For each submodule, show current commit, path, and branch (if on a branch)
  - `git submodule update --init --recursive`: Fetches/moves each submodule to the commit tracked by the parent repo
- [`uvx doc2docx`](https://pypi.org/project/doc2docx/) converts Word `.doc` files to the new `.docx` format. I had several old `.doc` files that I converted.
- Sometimes, the value of reading a book is not what you learn from it. It is the thoughts that pop into your head _while_ reading the book.
- Tools that convert files to prompt / Markdown suitable for LLMs:
  - [`uvx files-to-prompt`](https://pypi.org/project/files-to-prompt)
  - [`npx git-ingest`](https://gitingest.com/)
  - [`ingest`](https://github.com/sammcj/ingest) - written in Go, only Mac/Linux binaries
- LLM Code Execution Sandboxes that let you run code in a sandbox via an API:
  - [AgentRun](https://github.com/tjmlabs/AgentRun): open source, via Docker
  - [e2b.dev](https://e2b.dev/): A day costs about $1 (on demand) and you get about $100 one time credits. Self-hosting is complex. [Discussion](https://www.reddit.com/r/LocalLLaMA/comments/1chsx7z/is_there_an_opensource_alternative_to_e2b_e2bdev/)
  - [nsjail](https://github.com/google/nsjail): by Google. Write your own API
- LLM Observability tools:
  - [LiteLLM](https://docs.litellm.ai/) is an LLM Proxy with caching, logging, call hooks or plugins, rate limiting, virtual keys. SSO integration can be implemented.
  - [LangFuse](https://langfuse.com/self-hosting) is an LLM Proxy with API key distribution, logging, and SSO. But lacks per-user usage limits and server-side caching.
  - [Helicone](https://www.helicone.ai/) does not support SSO
- [GitHub Spark](https://githubnext.com/projects/github-spark) is a way to build micro-apps with LLMs. Like Claude Artifacts. It's currently in technical preview, though.
