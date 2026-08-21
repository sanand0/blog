---
title: Transcript AI-ded interviews
date: '2026-02-20T18:09:04+08:00'
categories:
- llms
classes: wrap-code
description: I used meeting transcripts and Google Drive material with Gemini to draft and refine interview answers, turning technical discussions into concise, evocative responses about AI architecture, reliability, and production safeguards.
tags: [llms, prompt-engineering, transcripts, technical-writing]
---

<!-- https://gemini.google.com/app/fc17155c3249516c -->

[Priyanka](https://www.linkedin.com/in/priyankamishra20/) was ghost-writing an interview request from PC Quest for [Ankor](https://www.linkedin.com/in/ankorrai/). Two questions were a bit technical:

1. Straive combines data engineering, analytics, AI, and content services. At a technical level, how are enterprises stitching these capabilities together architecturally and operationally when addressing complex business problems at scale?
2. GenAI systems tend to behave unpredictably when exposed to real workloads. What engineering patterns, monitoring approaches, or runtime safeguards are becoming essential to maintain reliability, performance, and cost control in production settings?

... and she asked if I could review.

These days, "rewrite" is easier than "review".

![](https://files.s-anand.net/images/2026-02-20-transcript-ai-ded-interviews.avif)

**STEP 1**: Copy all my meeting transcripts with Ankor. Below is my process, but copy-paste or a coding agent works even better.

- **1a**: Download transcripts with [`rclone`](https://rclone.org/)
- **1b**: Convert Word to Markdown with [`pandoc`](https://pandoc.org/)
- **1c**: Combine using [`uvx files-to-prompt`](https://github.com/simonw/files-to-prompt) and copy

**STEP 2**: Pass [Gemini](https://gemini.google.com/) (which accepts 1MB!) this prompt:

```markdown
Based on the documents below (transcripts of my calls with Ankor),
and the contents of my Google Drive where you'll find material about Straive,
how would Ankor answer this question to PCQuest -
in a way that's aligned with their audience?

Q: Straive combines data engineering, analytics, AI, and content services.
At a technical level, how are enterprises stitching these capabilities together
architecturally and operationally when addressing complex business problems at scale?

(Paste the transcripts)
```

The answer was a bit long and not very insightful. So I added 2 prompts:

```markdown
Share this as a 150-word summary suitable for a PCQuest audience.
```

Then:

```markdown
Frame this in a way that's insightful and evocative for a business audience.
Think about an approach that would make them think,
"Oh, yeah, that's insightful, and wasn't obvious until Ankor mentioned it."
```

The final result was quite a good one, reflecting some of our recent conversations:

> **Most enterprises are making a critical mistake with AI right now: they are treating foundational models like marriages, when they should be treating them like batteries.**
>
> If you hardwire your data and content pipelines directly to today’s best LLM, you are accumulating massive '**AI Debt**.' When a better model drops next year, you’re stuck. The true enterprise differentiator isn't the model—it’s building an agnostic orchestration layer. This middleware lets you swap out backend models instantly, without breaking your business.
>
> Once you decouple the model, you must stop trying to make legacy, linear assembly lines run faster. Instead, we use AI to **'squish' the assembly line** entirely. AI co-pilots extract metadata and trigger multiple agents to execute tasks in parallel, not sequentially.
>
> This fundamentally shifts the workforce. We are no longer putting humans _in_ the loop to do the heavy lifting; we are elevating them **_on_ the loop** as auditors. The AI executes the work and provides the citation trail; the human manages the risk. That is how you bypass theoretical six-month roadmaps and move from ideation to a secure, live enterprise deployment in just eight weeks.

**STEP 3**: For the next question:

```markdown
Think about how Ankor could answer this question -
applying the same process, style and approach.

Q: GenAI systems tend to behave unpredictably when exposed to real workloads.
What engineering patterns, monitoring approaches, or runtime safeguards are
becoming essential to maintain reliability, performance, and cost control in production settings?
```

It again needed some tweaking:

```markdown
Rewrite: about 150 words, slightly different style
(to make it avoid looking like too close a clone of the earlier answer),
but just as evocative and insightful.
```

... and the answer, again, was quite close to some of our discussons:

> **"Most leaders try to fix GenAI unpredictability by endlessly tweaking prompts. That’s like trying to tame the weather instead of just building a stronger roof.**
>
> At Straive, we assume models will hallucinate. The true enterprise differentiator is the _engineering harness_ built around them.
>
> We secure workloads through **Verifiable Autonomy**. Instead of testing in live production, we run agents through simulated environments governed by strict policy-as-code. If an agent can’t deterministically pass the simulation, it doesn’t touch real data.
>
> To scale without exploding headcount, we use **AI to govern AI**. We deploy a 'Maker/Checker' architecture: a creative model generates the work, while a cheaper, constrained model instantly audits it for compliance and accurate citations. Humans only handle the exceptions.
>
> Finally, we stop treating every task like a real-time chatbot. By shifting latency-insensitive workloads to asynchronous batch processing, we bypass rate limits and slash compute costs by half. Reliability isn't a model feature; it's an architectural choice."

---

The trick to re-purposing content quickly is:

1. Keep data / docs handy
2. Learn to quickly search & copy-paste
3. Learn to quickly judge and give feedback to AI
