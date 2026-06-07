---
title: Things I Learned - 08 Dec 2024
date: 2024-12-08T00:00:00+00:00
categories:
  - til
description: I investigated Amazon Nova model costs, surveyed why employees avoid internal LLMs, and evaluated JavaScript text splitters. I also learned about Unicode characters in ChatGPT citations and how to install Docker on Windows without admin rights.
keywords: [amazon nova, langchain, duckdb, docker, llm foundry, text splitting, arena hard, unicode]
---

This week, I learned:

- ChatGPT uses several unusual unicode characters for citations. [Ref](https://github.com/sanand0/openai-conversations/blob/main/private-unicode-control-characters.md)
- NumLock can be dangerous. An IT support team member took control of Radheya's screen while debugging and had turned on NumLock. Radheya's login failed after that. After 5 tries, he was locked out.
- With LLMs, most architectural decisions are no longer one-way doors. [Steve Yegge](https://simonwillison.net/2024/Dec/4/steve-yegge/)
- The cost of intelligence is trending to zero. How do we plan for this? [Logan Kilpatrick](https://x.com/OfficialLoganK/status/1864508209769390238?t=OwjvTL6T55sh6VZGoMBtoQ)
  - If you are not planning for the price of intelligence to go to zero, the next 3-5 years are going to incredibly disruptive to your business / life.
  - The important but not stated caveat: consumer willingness to pay for AI is going to go up (a lot). It will be fascinating to watch consumer willingness, cost, and the amount of AI being used all move in different directions.
  - Everyone building things with AI has an economic incentive to limit the amount of AI because of cost, which inherent limits the value prop. This will change as intelligence goes up and cost goes down.
  - What this means is:
    - **Admin automation**: Administrative tasks vanish into background AI. Booking meetings, managing finances, or even planning family activities will require less thought.
    - **Hyper-personalization**: Individuals get tailor-made everything—from medical advice to product recommendations to daily schedules. Systems learn your quirks.
    - **AI co-brains**: AI co-worker “assistants support you at any moment. Productivity soars in knowledge work. “I’ll have my AI follow up becomes a normal response.
    - **Humanity valued more**: As AI handles rote tasks, humans move up the value chain, focusing on creativity, empathy, or the “last-mile decisions.
    - **New business models**:
      - AI experts as a service
      - Embedded AI Solutions
      - AI micro-services for smart-calls
      - Distributed AI
- [Arena Hard](https://huggingface.co/spaces/lmarena-ai/arena-hard-browser) is a set of hard prompts to test LLMs. [Here is the code and evaluation](https://github.com/lmarena/arena-hard-auto)
- LLMs can detect clear outliers easily. PROMPT: Which is the outlier in this dataset: (1,7), (2,7), (3,6), (4,6), (5,5), (6,1), (7,5), (8,3), (9,1), (10,1) (ANS: (6,1))
  - 🟢 GPT-4o on ChatGPT gets this. GPT-4o Mini on the API gets it too.
  - 🟢 Gemini Pro, Flash, Flash 8b gets this right straight away, without even thinking.
  - 🟢 Claude 3.5 Sonnet, Claude 3 Haiku, Claude 3.5 Haiku get it on LLM Foundry. 🔴 Claude.ai, where it visualizes it and gets it wrong.
  - 🟢 Nova Micro, Lite, and Pro get it right.
  - 🟢 Llama 3.1 70b gets it right. 🔴 Llama 3.2 8b gets it wrong. Llama 3.2 70b, Llama 3.1 8b enter repetition.
- To install Docker on Windows without admin privileges, use [`net localgroup docker-users "your-user-id" /ADD`](https://stackoverflow.com/a/63290821/100904)
- A non-administrator in a Google Groups domain can only add 200 emails to a group from the UI directly without invitation at a time. The only programmatic way to add users is for an administrator to add them. Even apps that use the Google Admin SDK need an admin to log in to access the relevant API.
- Take 100% of your work, including complex, multi step processes and put it into an LLM. It might fail at some but you will discover the limitations.
- I emailed Straive employees about their use of [LLM Foundry](https://llmfoundry.straive.com/) - the internal LLM portal. I picked ~500 non-users from teams that _otherwise_ have high (30%+) usage.
  - Reasons they didn't use it were:
    - 40% had not heard of it.
    - 40% were unclear of the benefits
    - 20% didn't have time
  - 45% feel they don't have enough information and training to use it
  - Some feedback
    - Sharing training videos will help
    - Live training sessions that allows for Q&A will help
    - Developers prefer detailed documentation
    - The same prompt gives different results
  - Possible solution: Email non-users introducing the tool and sharing a quick 15-minute tutorial and a 1-page quick start.
- My notes on the Amazon Nova models. [More on Hacker News](https://news.ycombinator.com/item?id=42309121)
  - Nova Micro (3.75c/MTok) has the same cost as Gemini 1.5 Flash 8b but does not support images or documents.
  - Nova Lite (6c/MTok) has about the same cost as Gemini 1.5 Flash 002 and supports images and documents (but not audio or video). It may be a good alternative. But GPT-4o mini, which is 2.5X costlier, is much better. (It partly passes the `Gr brx vshdn Fdhvdu flskhu?` test which Nova Lite fails.)
  - Nova Pro (80c/MTok) is cheaper than Gemini 1.5 Pro and a lot cheaper than GPT 4o, but does not match their quality.
- LLMs are great at convincing you of wrong things. A danger and something to be wary of. [Ethan Mollick](https://bsky.app/profile/emollick.bsky.social/post/3lcepstbuck2z)
- Fish eye text summary is a great way to read text while summarizing context. [Amelia Wattenberger](https://wattenberger.com/thoughts/fish-eye)
- DuckDB's JavaScript API is still under development. For example, [JSON, ARRAY are not insertable](https://github.com/duckdb/duckdb-node-neo/blob/cb5be3d27b8aedfac7f2c9d0eec360891fb9e1f7/api/src/DuckDBAppender.ts). Plus, re-creating persistent HNSW indices crashes.
- What's a good text splitter library to use in JS?
  - LangChain: If you use it, use it with a simple wrapper decoupled from the implementation (e.g. your own parameters) that you can replace later.
    - Popular
    - Fit-for-purpose. MarkdownTextSplitter which inherits from RecursiveCharacterTextSplitter is what's needed in most cases.
    - Unstable
    - Poorly maintained [Python docs indicate version 0.0 but it is in 0.1](https://github.com/langchain-ai/langchain/tree/c2f1d022a2e55dfddd313e54d01250d3f64c6eb2/libs/text-splitters)
    - Under-maintained [Last update was 3 months ago, 13 Sep 2024](https://www.npmjs.com/package/@langchain/textsplitters)
  - LlamaIndex:
    - Popular
    - Not an ideal fit. MarkdownNodeParser does not support chunk size. SentenceWindowNodeParser does not capture Markdown headings.
