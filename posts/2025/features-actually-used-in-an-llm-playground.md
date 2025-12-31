---
title: Features actually used in an LLM playground
date: "2025-01-12T04:28:58Z"
lastmod: "2025-01-12T04:30:06Z"
categories:
  - how-i-do-things
  - llms
wp_id: 3825
---

![Features actually used in an LLM playground](/blog/assets/Picture1.webp)

At [Straive](https://straive.com/), only a few people have direct access to ChatGPT and similar large language models. We use a portal, [LLM Foundry](https://llmfoundry.straive.com/) to access LLMs. That makes it easier to prevent and track data leaks.

The main page is a playground to explore models and prompts. Last month, I tracked which features were used the most.

**A. Attaching files** was the top task. (The numbers show how many times each feature was clicked.) People usually use **local** files as context when working with LLMs.

- 3,819: Remove attachment.
- 1,717: Add attachment.
- 970: Paste a document
- 47: Attach from Google Drive

**R. Retrieval Augmented Generation (RAG)**. Many people use **large** files as context. We added this recently and it's become popular.

- 331: Enable RAG (answer from long documents)
- 155: Change RAG system prompt
- 71: Change RAG chunk size
- 27: Change number of RAG chunks

**C. Copying output** is the next most popular. Downloading is less common, maybe because people edit only **parts** of a file rather than a whole file.

- 1,243: Copy the output
- 883: Format output as plain text
- 123: Download as CSV
- 116: Download as DOCX

**T. Templates**. Many users save and reuse their own prompts as templates.

- 314: Save prompt as template
- 98: See all templates
- 53: Insert a template variable
- 18: Delete a template

**J. Generate JSON** for structured output is used by a few people.

- 238: Enable JSON output
- 223: Pick a JSON schema

**P. Prompt optimization**. Some people adjust settings to improve their prompt, or use a prompt optimizer. I'm surprised at how few people use the prompt optimizer.

- 238: Change temperature
- 207: Optimize the prompt

**G. Generating code** and running it via Gemini is less common, but it's used more than I expected.

- 275: Generate and run code

**S. Search** is used a lot less than I expected. Maybe because our work involves less research and more processing.

- 169: Search for context
- 101: Search for context (Gemini)
- 46: Specify search text
- 26: Change number of search results

I left out UI actions because they do not show how people use LLMs.

- 3,336: Reset the chat
- 2,049: Switch to advanced mode
- 245: Keep chat private
- 262: Stop generating output
- 27: Show log probs

The main takeaway is that people mostly use LLMs on **local** files. We need to make this process easier. In the future, AI that works directly with file systems, [Model Context Protocols](https://modelcontextprotocol.io/), and local APIs are likely to become more important.
