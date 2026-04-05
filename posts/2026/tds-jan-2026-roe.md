---
title: TDS Jan 2026 ROE
date: 2026-04-05T19:04:37+08:00
categories:
  - llms
  - education
---

[Tools in Data Science](https://tds.s-anand.net/) has a remote online exam (ROE). It has a tough reputation. We conducted one today.

Here's how today's [ROE](https://exam.sanand.workers.dev/tds-2026-01-roe) unfolded.

The TAs had created 13 questions and shared it with me yesterday. This morning, I tried solving them.

At first glance, it looked scarily hard! But I just jumpted down a few questions, and found that five questions were trivial, i.e. I just used the "Ask AI" button to copy the question into ChatGPT and it gave me the answer.

- 🟢 [06. Layered Encoding Challenge](https://exam.sanand.workers.dev/tds-2026-01-roe#hq-decode-layered-server) (2.0) is one-shot: [ChatGPT](https://chatgpt.com/share/69d22d83-0228-83a0-87ec-20f6fe3cc3d9) <!-- https://chatgpt.com/c/69d1b323-0858-839f-87c0-11923dbb2e6c -->
- 🟢 [07. Region Containing Point](https://exam.sanand.workers.dev/tds-2026-01-roe#hq-region-containing-point-server) (1.0) is one-shot: [ChatGPT - see second chat](https://chatgpt.com/share/69d22d83-0228-83a0-87ec-20f6fe3cc3d9) <!-- https://chatgpt.com/c/69d1b323-0858-839f-87c0-11923dbb2e6c -->
- 🟢 [10. Fix Broken JSON File](https://exam.sanand.workers.dev/tds-2026-01-roe#hq-broken-json-server) (1.0) is one-shot: [ChatGPT](https://chatgpt.com/share/69d22d85-5f70-8399-b517-25704905575e) <!-- https://chatgpt.com/c/69d1bbd1-ab04-839e-80cb-5d3241e19d05 -->
- 🟢 [11. Cross-entity disambiguation](https://exam.sanand.workers.dev/tds-2026-01-roe#hq-cross-lingual-entity-disambiguation-server) (1.0) is one-shot: [ChatGPT](https://chatgpt.com/share/69d22d86-f74c-83a1-856a-5a61489cf959) <!-- https://chatgpt.com/c/69d1bc1c-c7d8-839e-b7f3-2b37aa28dd71 -->
- 🟢 [13. Record Terminal Session with asciinema](https://exam.sanand.workers.dev/tds-2026-01-roe#hq-asciirec-server) (0.5) is one-shot: [ChatGPT](https://chatgpt.com/share/69d22d89-82a0-83a0-83cd-845e053a02a8) <!-- https://chatgpt.com/c/69d1bff0-1d88-8399-95da-393a2f489210 -->

For another four, I needed to just make sure I uploaded the files or HTML:

- 🟡 [03. Regex Golf Challenge](https://exam.sanand.workers.dev/tds-2026-01-roe#hq-regex-golf-server) (2.0) is one-shot but it's better to download and upload the text files, maybe, than copy-paste: [ChatGPT](https://chatgpt.com/share/69d22e6a-0808-839f-a4f5-ae514a0a94d5) <!-- https://chatgpt.com/c/69d1c08f-b764-839a-8027-34fe23658f5a -->
- 🟡 [04. Maze Solver with Constraints](https://exam.sanand.workers.dev/tds-2026-01-roe#hq-maze-solver-server) (2.0) is one-shot but needs you to upload the image and a good vision model: [ChatGPT](https://chatgpt.com/share/69d1c1c6-1b08-839e-af47-9b2cbab60985) <!-- https://chatgpt.com/c/69d1c013-75c4-83a0-ada4-22b68f89d79b -->
- 🟡 [05. Cipher Trail](https://exam.sanand.workers.dev/tds-2026-01-roe#hq-cipher-trail-server) (2.0) is one-shot but needs you to provide the secret HTML: [ChatGPT](https://chatgpt.com/share/69d22e6c-26f4-83a0-bb21-a3bcee77e163) <!-- https://chatgpt.com/c/69d1bd55-6b80-839d-9dfd-dc1de798fc69 -->
- 🟡 [12. Simple Question](https://exam.sanand.workers.dev/tds-2026-01-roe#hq-trick-question-server) (0.5) needs you to provide the secret HTML: [ChatGPT](https://chatgpt.com/share/69d22e6c-efd0-8398-8823-49f1130defd2) <!-- https://chatgpt.com/c/69d1bed0-717c-8398-8498-c467b03a5ef1 -->

Two questions confused ChatGPT a bit, and it needed some nudges. There is real learning here.

- 🟠 [08. Reorganize Files with Shell Commands](https://exam.sanand.workers.dev/tds-2026-01-roe#hq-rename-files-server) (1.0) is hard because of Unicode issues and the extra README.md students should delete. **Asking for variations** is the learning: [ChatGPT](https://chatgpt.com/share/69d22ed6-331c-8399-8848-9cb3cec90e96) <!-- https://chatgpt.com/c/69d1b9ab-980c-8398-846c-c3357793b8ee -->
- 🟠 [09. Refactor Python Code with VS Code](https://exam.sanand.workers.dev/tds-2026-01-roe#hq-python-refactor-server) (1.0) takes few attempts (question is imperfect, intentionally) but error messages are excellent, so **iterative feedback** is the learning: [ChatGPT](https://chatgpt.com/share/69d22ed9-9438-839a-860c-4109398ea612) <!-- https://chatgpt.com/c/69d1b9c2-de34-8398-b01d-4542b1db43ef -->

One was pretty hard and ChatGPT struggled with it.

- 🔴 [02. Korean Speech Dataset API Validation](https://exam.sanand.workers.dev/tds-2026-01-roe#hq-korean-audio-dataset-server) (5.0) actually requires work.
  At first, [ChatGPT refused ethically](https://chatgpt.com/share/69d22f18-02fc-839b-965a-6621554f0ab9). <!-- https://chatgpt.com/c/69d1c379-31f4-839b-89d0-f318e68bae38 -->
  When reframed, [it tried](https://chatgpt.com/share/69d22f1a-7850-83a0-a586-0f05e46dabeb), but the human-in-the-loop (me) was too slow. <!-- https://chatgpt.com/c/69d1c40c-b834-839e-a253-4430a77418e9 -->
  So I used [Codex](https://files.s-anand.net/blog/2026-04-05-tds-2026-01-roe/q-korean-audio-dataset-server-codex-session.md), which _literally hacks_ towards the solution! It searched online for existing solutions, read the GitHub discussions for this topic, found my browser tab and started testing itself, ... and solved it in 10.5 min!

This leaves the one question that AI can't solve:

- 🔴 01. [Collaborative Token Exchange](https://exam.sanand.workers.dev/tds-2026-01-roe#hq-share-token-server) (5.0) asks you to collect "tokens" from other people and share it. I asked Codex to hack it, but after an hour (of logging into my personal account, my IITM account, even my father's account, exhausting my token limits, and totally psyching me), it declared the question unhackable.

---

Based on this, the instructors, teaching assistants and I decided that:

- This exam is too easy with AI help. Combined with collaboration, it's **ultra-easy**. Therefore, let's add some old questions:
  - [14. FastAPI Time Series Caching](https://exam.sanand.workers.dev/tds-2026-01-roe#hq-fastapi-timeseries-cache) (0.5)
  - [15. AI Video Attendee Extraction](https://exam.sanand.workers.dev/tds-2026-01-roe#hq-video-attendee-extraction) (0.5)
- Thanks to [Project 1](https://exam.sanand.workers.dev/tds-2026-01-p1#hq-share-secret-server), people already collaborate at scale. So let's ask for 500 tokens instead of 100.

We deployed the exam at 12:00 pm IST, an hour before the scheduled time.

The hackers (e.g. who scan the source code, or change their system clocks) could see the questions earliy and started sharing and solving them.

The TAs said, "Anand, shall we add more questions to make it tougher?"

I said, "No, it's OK. The ROE has built a reputation for difficulty. Let that change. _Let them have an easy exam_."

"If they're going to split this in groups and have coding agents solve it, they'll score full marks in 10-15 minutes," I said to myself.

---

When the exam ended, this was the score distribution.

![](https://files.s-anand.net/images/2026-04-05-tds-roe-score-distribution.webp)

There were several surprises here. Firstly, 9 questions were repeats. Yet, barring _one_ question, they scored lower, though they appeared in equally tough ROEs in the past.

|   # | Question                                                                                                                        |   % | Previous % | Previous exam                                                                                                 |
| --: | ------------------------------------------------------------------------------------------------------------------------------- | --: | ---------: | ------------------------------------------------------------------------------------------------------------- |
|  14 | ⚪ [FastAPI Time Series Caching](https://exam.sanand.workers.dev/tds-2026-01-roe#hq-fastapi-timeseries-cache)                   |  8% |        39% | [2025 Sep ROE](https://exam.sanand.workers.dev/tds-2025-09-roe#hq-fastapi-timeseries-cache)                   |
|  15 | ⚪ [AI Video Attendee Extraction](https://exam.sanand.workers.dev/tds-2026-01-roe#hq-video-attendee-extraction)                 | 12% |        64% | [2026 Jan GA3](https://exam.sanand.workers.dev/tds-2026-01-ga3#hq-video-attendee-extraction)                  |
|  11 | 🟢 [Cross-entity disambiguation](https://exam.sanand.workers.dev/tds-2026-01-roe#hq-cross-lingual-entity-disambiguation-server) | 13% |        64% | [2026 Jan GA4](https://exam.sanand.workers.dev/tds-2026-01-ga4#hq-cross-lingual-entity-disambiguation-server) |
|   7 | 🟢 [Region Containing Point](https://exam.sanand.workers.dev/tds-2026-01-roe#hq-region-containing-point-server)                 | 15% |        38% | [2025 Sep ROE](https://exam.sanand.workers.dev/tds-2025-09-roe#hq-region-containing-point-server)             |
|   9 | 🟠 [Refactor Python Code with VS Code](https://exam.sanand.workers.dev/tds-2026-01-roe#hq-python-refactor-server)               | 17% |        57% | [2026 Jan GA1](https://exam.sanand.workers.dev/tds-2026-01-ga1#hq-python-refactor-server)                     |
|  13 | 🟢 [Record Terminal Session with asciinema](https://exam.sanand.workers.dev/tds-2026-01-roe#hq-asciirec-server)                 | 21% |        66% | [2026 Jan GA1](https://exam.sanand.workers.dev/tds-2026-01-ga1#hq-asciirec-server)                            |
|  10 | 🟢 [Fix Broken JSON File](https://exam.sanand.workers.dev/tds-2026-01-roe#hq-broken-json-server)                                | 30% |        64% | [2026 Jan GA1](https://exam.sanand.workers.dev/tds-2026-01-ga1#hq-broken-json-server)                         |
|  12 | 🟡 [Simple Question](https://exam.sanand.workers.dev/tds-2026-01-roe#hq-trick-question-server)                                  | 41% |        64% | [2026 Jan GA1](https://exam.sanand.workers.dev/tds-2026-01-ga1#hq-trick-question-server)                      |
|   8 | 🟠 [Reorganize Files with Shell Commands](https://exam.sanand.workers.dev/tds-2026-01-roe#hq-rename-files-server)               | 53% |        38% | [2026 Jan GA1](https://exam.sanand.workers.dev/tds-2026-01-ga1#hq-rename-files-server)                        |

Just as surprisingly, they scored _higher than these_ on 3 of the 5 new questions:

- 59%: 🟡 [03. Regex Golf Challenge](https://exam.sanand.workers.dev/tds-2026-01-roe#hq-regex-golf-server) (2.0) (253 / 430)
- 59%: 🟡 [04. Maze Solver with Constraints](https://exam.sanand.workers.dev/tds-2026-01-roe#hq-maze-solver-server) (2.0) (252 / 430)
- 54%: 🟡 [05. Cipher Trail](https://exam.sanand.workers.dev/tds-2026-01-roe#hq-cipher-trail-server) (2.0) (233 / 430)

One new question ended up being almost the **hardest** question - despite it being one-shot-table for ChatGPT (GPT 5.4, extended thinking).

- 2%: 🟢 [06. Layered Encoding Challenge](https://exam.sanand.workers.dev/tds-2026-01-roe#hq-decode-layered-server) (2.0) (9 / 430)

The toughest, though, had a 1% success rate. Though Codex could solve it in 10 min, it's a genuinely hard question.

- 1%: 🔴 [02. Korean Speech Dataset API Validation](https://exam.sanand.workers.dev/tds-2026-01-roe#hq-korean-audio-dataset-server) (5.0) (4 / 430)

Which leaves us with the collaboration question - the one that AI can't solve.

- 31%: 🔴 01. [Collaborative Token Exchange](https://exam.sanand.workers.dev/tds-2026-01-roe#hq-share-token-server) (5.0) (132 / 430)

This question is a whole new dynamic altogether. There were about 5 clear clusters of students, ranging from 5 - 35 students, who were collaborating. They were trading bundles of tokens between themselves. There were a few "super-collaborators" who were doing the bulk lifting. But even with this, the largest correct submission had 84 tokens. The strongest submission was a 51-token submission that 6 students submitted.

(I need to study this far more!)

Yet, far smaller than even the original 100 token target I had set. Clearly, **they aren't collaborating enough**.

---

It's surprising how little students were using the "Ask AI" button.

- 🔴 ~100 students didn't use it **at all**.
- 🟠 ~100 students clicked on it _JUST once_.
- 🟡 ~100 students used it just 2-5 times. For 15 questions, that's clearly low.
- 🟢 ~100 students used it 6-20 times. That's OK
- 🔵 ~15 students used it 20+ times. (1 clicked on it 45 times. Clearly _loves_ AI.)

---

Finally, most students saved their results for the first time _just_ before the deadline.

![](https://files.s-anand.net/images/2026-04-05-tds-roe-submission-timeline.webp)

The problem is that their system clocks were off, so they got a "late submission" error.

BTW, some students used a timing trick for hacking. By setting their system clock late, they can see the exam questions before release. But the submissions are checked only against the server clock. So, waiting until the last minute to save is a terrible idea. That hurt some students.

---

Based on this, here's what I learnt:

**Pressure makes a difference**. In past exams, with similar time pressure, students solved the _same_ questions _much_ better. I think they panic-ed on the first two questions. To be fair, so did I, when I saw them. That's why I started solving from the bottom.

**LESSON 1**: Scan end-to-end. Solve quick-wins (high impact, low effort) problems first.

**We have no clue what's easy or tough**. When different students are using different tools, what's easy for ChatGPT might be hard for Claude and vice versa. Without knowing tool capabilities and usage, this is hard to assess.

**LESSON 2**: With AI, no one knows what's easy or hard. Try for yourself.

**They aren't using AI enough**. Our advice is to use the "Ask AI" button every time. Half the students barely used it once.

**LESSON 3**: Use AI first. Focus on what AI _can't_ do well

**They aren't collaborating enough**. The collaboration question was designed to encourage collaboration. Yet, the largest bundle of tokens shared was 84, far smaller than the 500 token target.

**LESSON 4**: Make friends with classmates. Work together. It helps: now, and in the future.

---

That's worth repeating:

1. Scan end-to-end. Solve quick-wins (high impact, low effort) problems first.
2. With AI, no one knows what's easy or hard. Try for yourself.
3. Use AI first. Focus on what AI _can't_ do well.
4. Make friends with classmates. Work together. It helps: now, and in the future.
