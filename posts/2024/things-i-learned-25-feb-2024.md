---
title: Things I Learned - 25 Feb 2024
date: 2024-02-25T00:00:00+00:00
categories:
  - til
description: I explored the emerging Architecture.md standard, htmz for loading HTML, and tokenization nuances in LLMs. My learnings cover everything from agricultural robotics and hardware trends at NVIDIA to mounting SQLite as a filesystem using wddbfs.
keywords: [architecture.md, htmz, tokenization, llms, quantum computing, sqlite, fastcore]
---

This week, I learned:

- [Architecture.md](https://github.com/rust-lang/rust-analyzer/blob/d7c99931d05e3723d878bea5dc26766791fa4e69/docs/dev/architecture.md) is an [emerging standard](https://matklad.github.io/2021/02/06/ARCHITECTURE.md.html)
- Managing wealth requires training.
- [htmz](https://leanrada.com/htmz/) is a fantastic way to load HTML into elements!
- Suguna Poultry is
  - Using robots to walk in their farms, use sound and bird eyes and movement to predict birth health over 1-2 weeks
  - Light on the back of the bird's back AND face => lays eggs in 14 days, else takes days later (girls and mobile phones?)
- Teknoturf is using Gen AI to
  - Improve prompts when teaching prompt engineering.
  - Pronounce languages better, identifying which words Tamilians and Malayalis will mis-pronounce.
- Explore IRBlaster. It can control AC and can automatically increase temperature at night.
- My view: LLMs are general purpose and more capable than SLMs. They'll win, like CPUs won over special-purpose chips. GPUs will optimize for LLMs and as usage grows, cost will fall.
- [Andrej Karpathy's summary of sharp edges in tokenization](https://www.youtube.com/watch?v=zduSFxRajkE&t=6701s) uses [tiktokenizer](https://tiktokenizer.vercel.app/) to explain:
  - Why LLMs can't be used for spelling
  - Why LLMs are better at English than other languages
  - [Why LLMs are bad at math](https://www.beren.io/2023-02-04-Integer-tokenization-is-insane/)
  - Why [SolidGoldMagiKarp](https://www.lesswrong.com/posts/aPeJE8bSo6rAFoLqg/solidgoldmagikarp-plus-prompt-generation) is a single token
  - Why trailing spaces are bad
  - Why YAML tokenizes more efficiently than JSON
- [ssyoutube.com](https://ssyoutube.com): Just add "ss" to "youtube.com" on the video and you can download YouTube videos
- Discussions with Sachin, AMAT
  - Microsoft said Indigo, Air India uses LLM based bookings
  - Meta invested $70bn in GPUs. Sam Altman is investing $7tn!
  - NVIDIA has a price PREMIUM not discount for bulk GPUs!
  - AMD is the next company to watch for
  - Numenta - Subutai Ahmad - deploys AI models on CPUs
  - #TODO Read A Thousand Brains by Subutai Ahmad
  - [Sanjeev Sharma](https://www.linkedin.com/in/sanjeevsharmaiitr/)
    - Swaayatt Robots: Autonomous driving in India
    - Deepeigen: Education
  - [Rohan Shravan](https://www.linkedin.com/in/rohanshravan/), Bangalore.
    - Likes sharing knowledge. Amazing teacher. IIT KGP 2008. Interested in exploring quantum computing
    - Tresa Motors, Inkers App, The School of AI
  - AMAT is working on
    - photon-based computing.
    - science research models. AI for science. Like Google: Deepmind Genome, Microsoft: Metagen
    - quantum: AMAT is actively in into this. Nagapati Banda is driving this
  - John Kelly is predicting a ChatGPT moment in quantum in a few years
- Adobe express has a forever free [video to GIF converter](https://new.express.adobe.com/tools/convert-to-gif)
- Edge workspaces let me keep the same tabs open across laptops!
- [Command line interface guidelines](https://clig.dev/)
- RAWGraphs has a [custom charts API](https://www.rawgraphs.io/custom-charts) that is worth learning from
- Python [fastcore](https://fastpages.fast.ai/fastcore/) has decorators like @typedispatch, Self, etc.
- [All image-to-text models on HuggingFace](https://huggingface.co/models?library=transformers&pipeline_tag=image-to-text)
- [wddbfs](https://adamobeng.com/wddbfs-mount-a-sqlite-database-as-a-filesystem/) mounts SQLite as a file system. I had a bit of trouble, maybe with Python package versions.
- Google is using [LLM powered bug identification](https://security.googleblog.com/2023/08/ai-powered-fuzzing-breaking-bug-hunting.html)
- [HuggingFace Chat Assistants](https://huggingface.co/chat/assistants) has open source system prompts!!
- [OpenHermes training dataset](https://huggingface.co/datasets/teknium/OpenHermes-2.5) is available. 1M prompts!
- Jio has made IPL free. They make money on data and ads. That's Scale!
- Daniel Dennett [outsources thinking to students](https://behavioralscientist.org/ive-been-thinking-daniel-dennett-what-if-im-wrong/). Reviewing his books.
  - BUT: I don't take feedback. When someone sends a pull requests, I ignore it.
