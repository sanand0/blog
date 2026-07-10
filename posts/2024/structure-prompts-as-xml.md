---
date: "2024-09-20T04:07:16Z"
categories:
  - linkedin
description: "XML tags are emerging as the most consistently recommended way to structure prompts across major LLM vendors, even if Markdown remains preferable for generated output."
tags: [xml, prompt-engineering, anthropic, openai, google]
linkedin: https://www.linkedin.com/feed/update/urn:li:activity:7242746112019722240/
---

Looks like XML tags are the best way to structure prompts and separate sections for an #LLM. It's the only format that all of Anthropic, Google, and OpenAI LLMs encourage.

For example:

<instructions>...</instructions>
<question>...</question>
<example>...</example>
<example>...</example>

Anthropic Docs: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/use-xml-tags
OpenAI Docs: https://platform.openai.com/docs/guides/prompt-engineering/strategy-write-clear-instructions
Google Docs: https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/structure-prompts

Alternatives are using JSON, Markdown, templating formats like Mustache/Jinja, etc.

Even Llama's system tokens seem a little XML-like.
https://github.com/meta-llama/llama3/blob/main/llama/tokenizer.py#L61-L74

Personally, I've been using Markdown so far. But it's time to switch over. (Only on the prompt side. On the generation side, Markdown still seems the best.)

[LinkedIn](https://www.linkedin.com/feed/update/urn%3Ali%3Ashare%3A7242746111097012225)
