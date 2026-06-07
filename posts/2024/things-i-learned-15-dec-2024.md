---
title: Things I Learned - 15 Dec 2024
date: 2024-12-15T00:00:00+00:00
categories:
  - til
---

This week, I learned:

- `**/*.md` can search for all Markdown files. [Julia Evans](https://jvns.ca/til/star-star-works-for-globbing-in-the-shell/)
- Windows 11 2024 Update features: [Ref](https://support.microsoft.com/en-us/windows/inside-this-update-93c5c27c-f96e-43c2-a08e-5812d92f220d)
  - [Live captions](https://support.microsoft.com/topic/b52da59c-14b8-4031-aeeb-f6a47e6055df) (via the tray) can transcribe audio and microphone.
  - [Cocreator in Paint](https://support.microsoft.com/topic/53857513-e36c-472d-8d4a-adbcd14b2e54) lets you draw crudely and enhances it with AI. The neat UI is a slider that lets you control how close it should be to your drawing.
  - Voice Clarity automatically cancels echo, reduces background noise, and minimizes reverb.
  - [Studio Effects](https://support.microsoft.com/en-us/windows/windows-studio-effects-273c1fa8-2b3f-41b1-a587-7cc7a24b62d8) (via the tray) lets you apply camera effects on all apps. Eye contact feature is CLEVER!
  - [sudo](https://learn.microsoft.com/en-us/windows/sudo/) lets you run commands with admin privileges from the command line. [source](https://github.com/microsoft/sudo)
- [Roaming RAG](https://arcturus-labs.com/blog/2024/11/21/roaming-rag--rag-without-the-vector-database/) is an alternative to RAG without the vector database.
  - Applicable to **well structured documents**, e.g. technical books, manuals, etc.
  - Create a hierarchical outline of the document. [Code](https://github.com/arcturus-labs/llm-text-assistant/blob/48b71030992301f6d1631f23cfc643dca56835eb/backend/app/routes/api/tools.py)
    - Keep the top-level headings.
    - Preserve the first ~100 characters of opening text from each section.
    - Present the second-level headings, but without any subsidiary content.
    - Provide each section a unique 8 digit hex identifier.
    - Each section heading is followed by a guiding comment for the model: `Section collapsed - expand with expand_section("{identifier}").`
  - Then read the relevant sections as context to answer the question. [Code](https://github.com/arcturus-labs/llm-text-assistant/blob/48b71030992301f6d1631f23cfc643dca56835eb/backend/app/routes/api/conversation.py#L37)
- Traffic to StackOverflow has fallen considerably. Especially from young and Indian developers. StackOverflow revenue is down. Via [Prashanth](https://www.linkedin.com/in/pchandrasekar/). They're exploring:
  - Licensing their content. (Meta says high quality content improves LLM performance by 30% on HumanEval)
  - Enterprise StackOverflow for system integration
  - Fine-tuned versions of Enterprise Stackoverflow for enterprises
  - Integrate StackOverflow within your IDE. Ask questions, post directly
- I surveyed the Gramener QA team on how they were using LLMs.
  - 7 used it for code generation (e.g. date extraction, regex generation)
  - 4 used it for learning (e.g. Robot Framework, how to define test cases, API usage)
  - 3 used it for formula generation (e.g. Excel)
  - 2 used it for test scenario identification
  - 2 used it for test data generation
  - 2 used it for comparing expected vs actual datasets
  - 1 used it for data type identification (e.g. given sample values, identify the data type).
  - 1 used it for evaluating resulting (LLM as a judge)
- I asked the Straive Digitalized Operations team what management techniques they would apply to manage LLMs. Here are the responses:
  - Ask better questions. (Prompt engineering.)
  - Create templates or step-by-step instructions. (Chain of Thought.)
  - Ask for multiple options and pick from the best options. (Agentic approach?)
  - Training. (Fine tuning.)
  - Price weaker responses lower. (Stratified model pricing?)
- "LLM hallucinations are a good thing. They are a sign of diversity, allowing us to improve the answer by exploring multiple paths." -- A colleague from Straive.
- [Hyperbrowser](https://www.hyperbrowser.ai/) is a cloud based puppeteer service.
- Bedrock Llama models can't be directly called with their model names. You need to use their [inference profile names](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html), e.g. `us.meta.llama3-2-11b-instruct-v1:0` if the model is in a US region.
- [Hacker News RSS](https://hnrss.github.io/) is a good way to get RSS feeds from Hacker News. It's also a good way to understand how to convert a news source into RSS feeds. [BlueSky has RSS feeds too](https://openrss.org/blog/bluesky-has-launched-rss-feeds)
- When embedding using a `SentenceTransformer.encode(docs)` it's best if we embed with smaller `docs` and call it multiple times (rather than embedding more at once). On Colab T4, for [`gte-base-en-v1.5`](https://huggingface.co/Alibaba-NLP/gte-base-en-v1.5), when embedding 1,000 docs of up to 8K chars each, here is the **TOTAL** time it took, based on batch sizes (lower is better)
  - 1 doc per call: 10s
  - 2 docs per call: 13s
  - 4 docs per call: 19s
  - 8 docs per call: 23s
  - 16 docs per call: 32s
  - 32 docs per call: 40s
- Running embeddings without a GPU is _extremely_ slow. It takes ~2.4 seconds per string.
