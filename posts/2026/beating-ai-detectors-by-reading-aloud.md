---
title: Beating AI detectors by reading aloud
date: 2026-07-01T17:43:49+08:00
categories:
  - llms
description: I bypassed AI detectors with high confidence by reading LLM-generated drafts aloud and transcribing them, naturally replacing robotic AI writing habits with conversational, human speech patterns.
keywords: [ai detectors, pangram, zerogpt, dictation, transcription, writing style]
---

![](https://files.s-anand.net/images/2026-07-01-beating-ai-detectors-by-reading-aloud.avif)

[Ranjeeta](https://in.linkedin.com/in/ranjeetaborah) asked me for an article for [Built In](https://builtin.com/). I went straight to ChatGPT and said:

```markdown
Write an article for Built In.
Read the section below for context on Built In's audience, style, and content preferences.
Read the pitch that explains what the article should be about.
Then use my blog posts, talk content, transcripts, TIL, etc.
Write an article using my writing style.
```

... and gave it all related information.

[Here is ChatGPT's article](https://www.s-anand.net/blog/notes/no-juniors-no-experts-chatgpt/). The article itself was pretty good, content-wise, but it wasn't _exactly_ in my style and I iterated once. Still... not exactly there.

<!-- https://chatgpt.com/c/6a44cce0-7880-83ec-b611-9fe0086d704a -->

---

One of the criteria is that "Final drafts must score ‘human-written’ or less than 20% on [ZeroGPT](https://www.zerogpt.com/) and [Pangram](https://www.pangram.com/)." ZeroGPT is easy to fool but Pangram is harder. Pangram said:

> **AI Generated**. 100% of this text is AI Generated
>
> - "No Juniors, No Experts? Ankor runs a ..." (384 words) - We believe the segment is fully AI generated. Confidence: High.
> - "In March 2026, I pointed a coding ..." (383 words) - We believe the segment is fully AI generated. Confidence: High.
> - "Make it generate rare failures. Make it ..." (196 words) - We believe the segment is fully AI generated. Confidence: High.

Also: "AI-Generated indicates text produced by an AI system with minimal human input or revision."

Sigh... Just to cross-check, I pasted a [2021 blog post](https://www.s-anand.net/blog/picking-gifts-is-hard/) and Pangram said:

> **Human Written**. 100% of this text is Human Written.
>
> - "Picking gifts is hard. Gift-giving feels ..." (331 words) - The segment is fully human-written. Confidence: Low.

Well, maybe Pangram _does_ do a good job of detecting AI-generated text. It managed to by-pass my [carefully crafted writing style](https://github.com/sanand0/scripts/blob/2db79dc8bf99d19e4b7822e277c83f80bb22c18b/agents/anand-writing-style/SKILL.md) which includes several LLM smell avoidance techniques.

Next attempt: I checked if Claude's new [Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5) could do a better job.

---

[Here is Claude's article](https://www.s-anand.net/blog/notes/no-juniors-no-experts-claude/). Though the content was, again, spot-on, the style had _clear_ LLM smells despite all my instructions.

<!-- https://claude.ai/chat/44eeb55d-33ca-4cb5-9c3b-3526fdfe2f07 -->

Pangram said:

> **AI Generated**. 100% of this text is AI Generated
>
> - "No Juniors, No Experts? AI is cutting ..." (359 words) - We believe the segment is fully AI generated. Confidence: High.
> - "He's three times faster than someone ..." (132 words) - We believe the segment is fully AI generated. Confidence: High.

At this point, inspiration struck. (Actually, not quite. I had this idea for a few days, maybe weeks, ago... but the opportunity struck.)

I opened the Claude article on the left, ChatGPT on the right (just to transcribe, nothing else - ChatGPT has the best transcription right now), and _read out_ the article. Not word-for-word, but in my style. For example:

| Claude said ...                                                                    | I read it out as ...                                                                                |
| ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| AI is cutting the entry-level jobs that used to train tomorrow's architects.       | These days, AI is reducing the number of entry-level jobs that we have.                             |
| AI makes senior architects more productive and cuts the need for junior engineers. | He said, AI makes senior architects more productive and reduces the need for junior engineers.      |
| The data backs his worry.                                                          | The data supports his concern.                                                                      |
| A free phone app now beats any grandmaster.                                        | Any free phone application today can beat every grandmaster.                                        |
| A broken deployment, a weak first draft: you catch it and move on.                 | Broken deployments and prototypes and quick POCs aren't so important that you can't live with them. |

The beauty of this is that it I was able to read it out _almost live_. Just read a sentence and narrate it like I'm talking to an audience. I'm used to doing this.

[Here is the version I read out](https://www.s-anand.net/blog/notes/no-juniors-no-experts-anand/). Pangram said:

> **Human Written**. 100% of this text is Human Written.
>
> - "No Juniors, No Experts? These days..." (381 words) - The segment is fully human-written. Confidence: High.

The beauty of it is that it has **High** confidence - even more so than my [earlier blog post](https://www.s-anand.net/blog/picking-gifts-is-hard/) which was _truly_ human written.

Still, good to know that there's an efficient way to use AI that doesn't smell like AI.
