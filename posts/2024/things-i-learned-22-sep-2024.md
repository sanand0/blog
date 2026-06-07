---
title: Things I Learned - 22 Sep 2024
date: 2024-09-22T00:00:00+00:00
categories:
  - til
description: I discovered E2E for cheap Indian GPU hosting, explored XML tags for better LLM prompting, and tested tools like Jupyter Lite and VoidEditor. I also learned about Ollama's concurrency and animating faces with Segmind's Hallo.
keywords: [e2e, ollama, prompt engineering, cursor, jupyter lite, non-negative matrix factorization, voideditor, sarvam.ai]
---

This week, I learned:

- E2E is a cheap GPU hosting provider for India. About Rs 100/hr for a V100 16GB
- Jetson NVIDIa is like Raspberry Pi with a GPU! But it's expensive.
- [Sarvam.ai offers Indic text to speech](https://www.sarvam.ai/apis/text-to-speech)
- [Jupyter Lite](https://jupyter.org/try-jupyter/lab/) lets you run Jupyter notebooks in the browser
- [Piston](https://piston.readthedocs.io/) lets you run Python code via a REST API
- [`<link rel="modulepreload">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/rel/modulepreload) lets you load and compile modules early!
- Ollama 0.2 can handle [concurrent requests](https://github.com/ollama/ollama/releases/tag/v0.2.0) with only a little additional memory. (So can vLLM and DeepSpeed.)
- Prompt engineering for code generators:
  - [Claude Artifacts Prompt](https://gist.github.com/dedlim/6bf6d81f77c19e20cd40594aa09e3ecd#file-claude_3-5_sonnet_artifacts-xml)
  - [Val.Townie system prompt](https://gist.github.com/simonw/d8cc934ad76b3bba82127937d45dc719). Good example of how to create
  - [Cursor editing](https://llmfoundry.straive.com/history#?app=cursor&model=&t=1725629416223543)
  - [Cursor debugging](https://llmfoundry.straive.com/history#?app=cursor&t=1726379294138938)
  - [Cursor conversation](https://llmfoundry.straive.com/history#?app=cursor&model=&t=1726368766109438)
- XML tags seem best to structure prompts across LLMs.
  - [Claude](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/use-xml-tags)
  - [OpenAI](https://platform.openai.com/docs/guides/prompt-engineering/strategy-write-clear-instructions)
  - [Gemini](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/structure-prompts)
- [Instructor prompts](https://www.moreusefulthings.com/instructor-prompts) by Ethan Mollick help teach better
- Non-Negative matrix factorization apparantly aligns to intuition more than K-Means and hence would be a great fit for most cosine-similarity matrices (via Jaidev).
- [Segmind's Hallo](https://www.segmind.com/models/hallo) lets you animate a face to an audio clip
- [VoidEditor](https://voideditor.com/) aims to be an open source Cursor alternative
- [Video of ChatGPT o1 + mini reproducing the methodology of a paper](https://youtu.be/M9YOO7N5jF8) by writing the code - in 6 iterations. [Here's the repo](https://github.com/kylekaba/chatgpt-01-youtube). Prompts:
  1. You are a Python and Astrophysics expert who is tasked with helping me on my research project. Please read the following methods section of this research paper and re-create the Python code described.
  2. Thank you, this code looks really nice. I don't have any actual data or noise cube ready at the moment, but could you please generate some test data that can be used in the code you just wrote: {CODE}
  3. Hi. thank you for writing the code! Unfortunately, it seems that I get an error when I try to run it. I've attached the error message below, can you please refine the code so that the error is resolved? {ERROR}
  4. Thank you, but when attempting to run the code that you provided, I received the following error: {ERROR}
  5. Hello, thank you for the code. but now I get the following error pasted below: {ERROR}
  6. Thank you, I think we are getting close to a final solutiom I still get an error, which I've pasted below: {ERROR}
- Groq, SembaNova and Cerebras are fast inference models. All appear to be free
- The skills required to vet the AI's response is the same skillset used to vet a Pull Request. It's a good way to teach code review. Source: [My personal guide for developing software with AI](https://www.reddit.com/r/LocalLLaMA/comments/1fbe995/my_personal_guide_for_developing_software_with_ai/)
- Prompt engineering tip: Tell LLMs another AI wrote code. Else they will agree with you!
