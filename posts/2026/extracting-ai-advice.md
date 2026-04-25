---
title: Extracting AI advice
date: '2026-02-09T09:52:19+08:00'
categories:
- how-i-do-things
- llms
classes: wrap-code
description: Large transcript archives can be distilled into reusable advice by combining cheap long-context models for extraction with stronger models for final synthesis.
keywords: [transcripts, advice extraction, synthesis, long context, Gemini Flash, Claude]
---

This weekend, two people asked me, roughly "How do I use AI better?"

This is a frequently asked questions. I document my FAQs, e.g. [time management](/blog/time/), [career advice](/blog/career-advice/), etc. and it was time to add [AI advice](/blog/ai-advice/) to this list.

![](https://files.s-anand.net/images/2026-02-09-extracting-ai-advice.avif)

I often record online calls and [transcribe them](/blog/prompts/transcribe-call-recording/). I asked [Gemini](https://gemini.google.com/share/8541ff4e4135), [Claude](https://claude.ai/share/62d9d460-3bcb-43dc-a591-a283b35c3a69) and [ChatGPT](https://chatgpt.com/share/6989414e-441c-8003-9b95-ac835e15a79c) for the best way to summarize 400 transcripts of ~40K each.

Claude's suggestion was the best:

1. Use Gemini Flash (1M context, dirt cheap) to process calls in batches of 20-25
2. Each batch → extract advice themes
3. Aggregate batch results with Claude Sonnet for final synthesis

But I ignored it because it was too much work. (See my [AI advice](/blog/ai-advice/): _"Ask for easier output"_)

Instead, I listed all my transcripts and used [Simon Willison's `llm` CLI tool](https://llm.datasette.io/) to run:

```bash
llm -m gemini-3-flash-preview --system "Summarize ALL AI-related advice from Anand this call transcript into 1-sentence bullets" -f file-1.md > "extract/ai/file-1.md"
llm -m gemini-3-flash-preview --system "Summarize ALL AI-related advice from Anand this call transcript into 1-sentence bullets" -f file-2.md > "extract/ai/file-2.md"
...
```

(A for-loop is smarter. Copy-paste is easier. I optimize for ease.)

This took a little over an hour and a dollar. Then, I combined all the `extract/ai/*.md` files into one big file:

```bash
uvx files-to-prompt *.md | xclip -selection clipboard
```

... and pasted it into Gemini 3 Pro, which could comfortably handle the 750KB of context and prompted it:

```markdown
Here is the summary of AI related advice I provided in discussions to various people.

What is the most common advice I provide to people that is relevant to people looking to use AI for personal use and productivity?
```

The result was a good list along the lines of:

```markdown
### 1. The "50 Conversations a Day" Rule (The Core Habit)

You frequently tell individuals that they cannot learn AI through theory. To build intuition, they must force themselves to use it for everything.

- **The Advice:** Aim for a volume target of **50 interactions per day**.
- **Why:** High-frequency usage forces you to find "micro-use cases" you would otherwise ignore. It moves you past the "novelty" phase into the "utility" phase where you instinctively know which tasks the AI can handle.
- **Application:** Don't save AI for big projects. Use it to fix grammar in a text, explain a joke, plan a menu, or debug a single line of code.
```

... which I condensed into:

```markdown
- **Have 50 conversations a day with AI**. High-usage forces you to find tiny use-cases you'd otherwise ignore.
```

**Here's my current [AI Advice](/blog/ai-advice/).**

---

Another advantage of creating an `extract/ai/` folder is that I can pull out technical AI advice, governance-related AI advice, etc. later.

In fact, this "map-reduce" style pattern is clearly powerful. For $2 and a little time, I get very useful synthesis. I plan to use it more.
