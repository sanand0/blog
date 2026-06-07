---
title: Things I Learned - 20 Oct 2024
date: 2024-10-20T00:00:00+00:00
categories:
  - til
---

This week, I learned:

- SQL optimizations for multi-threaded web applications. [Ref](https://github.com/rails/rails/pull/49349)
  - `PRAGMA journal_mode = WAL`. Improves performance for frequent writes. It allows concurrent reads and writes.
  - `PRAGMA synchronous = NORMAL`. Improves performance. We might lose a few transactions but won't corrupt the database.
  - `PRAGMA mmap_size = 128000000`. Set global memory map for processes to share data
  - `PRAGMA journal_size_limit = 64000000`. Limit WAL file to prevent unlimited growth
  - `BEGIN IMMEDIATE` instead of `BEGIN`. Prevents writes to the journal file until the transaction is complete. Improves concurrency.
- AI seems to be slowing down apprenticeship since experts would rather use an AI than train an apprentice. Example: Robotic surgery. [Ref](https://x.com/emollick/status/1834228159190806552)
- How AI can improve education performance and engagement. [Ref](https://s-anand.net/notes/Pearson%20Updates%20-%202024-10-13.opus)
  - Student: Create study plan based on course and schedule
  - Student: Focus on what you need to learn more
  - Student: Align with your study style and pace
  - Teacher: Grading MCQs
  - Teacher: Writing conceptual guides
  - ["New collar workers"](https://en.wikipedia.org/wiki/New-collar_worker) was coined by Ginny Rometty
  - Embed tutor or document in video and ask for clarification! This is a new embedded interface. #TODO
- [Playing Bad Apple in Minecraft](https://purplesyringa.moe/blog/we-built-the-best-bad-apple-in-minecraft/). Ultra cool!
- OpenAI has a prompt generator. Currently it uses a meta-prompt but may later move to DSPy or Gradient Descent. [Ref](https://platform.openai.com/docs/guides/prompt-generation)
- Great demo of using the Realtime API to read the latest Hacker News. [Ref](https://x.com/nickscamara_/status/1842243883842904529)
- LLMs have reached the point where they can show a world, like CounterStrike, in near real time. [Ref](https://x.com/emollick/status/1845216321723826404)
