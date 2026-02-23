---
title: Repurposing blog posts for talks
date: 2026-02-22T22:09:49+08:00
categories:
  - llms
  - how-i-do-things
---

Recently, I've re-used my own writing / transcripts as context to LLMs. For example, I've used:

- [My meeting transcripts to answer interview questions](/blog/transcript-ai-ded-interviews/)
- [My blog posts to write news articles](/blog/writing-articles-from-my-blog-posts/)
- [My chat history to extract AI-related advice](/blog/extracting-ai-advice/)

This repurposing can be used for so many things.

For example, before delivering a talk to journalists _"Review my Feb 2026 LLM posts and generate a single-sentence, ELI15 high-impact use case for journalists."_ gets me list of use cases. Now, all I have to do is **show what I did** and **share how it's relevant** for them, like:

1. [I found old friends with Gemini Deep Research](/blog/finding-old-friends-with-gemini/). You can trace sources who changed names.
2. [I transcribed the entire Dilbert archive](/blog/gemini-3-flash-ocrs-dilbert-accurately/). You can transcribe scanned court records for $20.
3. ... and so on.

I can do this for _any field_.

![](https://files.s-anand.net/images/2026-02-22-repurposing-blog-posts-for-talks.avif)

Here are a few examples (and they're _good_ ones):

<details>
<summary>See journalist use cases</summary>

1. [Extracting AI Advice](/blog/extracting-ai-advice/): A journalist who has obtained hundreds of FOI documents or deposition transcripts can use a cheap large-context model to pull one-sentence bullets from each and then ask a stronger model to rank the top patterns -- turning months of reading into an afternoon.
2. [Finding Old Friends with Gemini](/blog/finding-old-friends-with-gemini/): An investigative journalist can use Gemini Deep Research to trace sources who have changed names, employers, or countries -- surfacing government nomination lists and public records that bridge who someone used to be with who they are now.
3. [Gemini 3 Flash OCRs Dilbert Accurately](/blog/gemini-3-flash-ocrs-dilbert-accurately/): A journalist who receives a dump of scanned physical documents -- leaked government files, court records -- can make the entire archive full-text searchable for roughly $20, without waiting weeks for manual transcription.
4. [Organizing PDF Receipts](/blog/organizing-pdf-receipts/): An investigative journalist who obtains a dump of expense or procurement PDFs can ask an AI coding tool to parse each one and rename it to a standard format -- making it trivial to spot duplicate amounts, unusual vendors, or suspicious date gaps at a glance.
5. [RIP, Data Engineers](/blog/rip-data-engineers/): A data journalist who obtains the SQL query logs of a public institution can use an AI agent to cluster what questions the database was actually built to answer -- revealing whether an agency is doing tactical monitoring or genuine public-service analysis, which can itself be the story.
6. [Transcript AI-ded Interviews](/blog/transcript-ai-ded-interviews/): A journalist who has done twenty interviews for a long-form profile can feed all the transcripts to a large-context model and ask it to surface the best quotes on a given angle, or flag contradictions between what different sources said -- without re-reading every word.
7. [Using AI for Work News](/blog/using-ai-for-work-news/): A beat journalist without a research desk can set up a Google Workspace automation that scans their sources weekly and delivers a single Gemini-written brief -- so nothing from a regulator's filing or a council report slips through unread.
8. [Writing Articles from My Blog Posts](/blog/writing-articles-from-my-blog-posts/): A reporter with years of stories on the same beat can feed their archive to an AI, ask it to identify which past pieces form the strongest foundation for a new investigation, and get a draft synthesis written in their own voice -- rather than starting from a blank page.

</details>

<details>
<summary>See civic use cases</summary>

- [Breaking Rules in the Age of AI](/blog/breaking-rules-in-the-age-of-ai/): A government adult literacy programme can drop its AI ban and replace it with instant AI-graded feedback -- letting learners ask questions in their own language, fail and retry freely, and delegate tedious steps -- re-engaging adults who had already given up on education.
- [Extracting AI Advice](/blog/extracting-ai-advice/): A city welfare department can transcribe its 300 community consultations into one-sentence bullets and rank the top 10 concerns across meetings in the residents' words -- for a few dollars and hours.
- [Finding Old Friends with Gemini](/blog/finding-old-friends-with-gemini/): A social welfare officer can use Gemini Deep Research to trace former programme participants who have moved or changed names, surfacing public records that link old and new identities -- closing the loop on services that were started but never finished.
- [Gemini 3 Flash OCRs Dilbert Accurately](/blog/gemini-3-flash-ocrs-dilbert-accurately/): A city archivist can make thousands of scanned land records, court orders, and petitions fully searchable by running them through Gemini Flash at roughly $20 for an entire archive -- no in-person visit required.
- [Organizing PDF Receipts](/blog/organizing-pdf-receipts/): An NGO finance coordinator can ask an AI coding tool to write a script that reads every vendor PDF, extracts the date, amount, and reference, and renames the file to a standard format -- turning a half-day filing chore into a five-minute step before uploading to a compliance portal.
- [RIP, Data Engineers](/blog/rip-data-engineers/): A government department can expose its data culture -- and fix silent metric misalignment between teams -- by feeding its SQL query logs to an AI agent that clusters them and proposes a small set of shared standard tables, no data warehouse project required.
- [TDS Comic Generation](/blog/tds-comic-generation/): A district health office with no design budget can generate multilingual public health comics for low-literacy communities by defining a few recurring characters, writing their dialogue in plain language, and letting Gemini produce each strip in minutes -- at near-zero cost per language.
- [Transcript AI-ded Interviews](/blog/transcript-ai-ded-interviews/): A government communications officer can feed all auto-generated meeting transcripts on a topic to a large-context model and get a press-ready 150-word statement grounded in what the department actually said -- in an hour instead of a week of document hunting.
- [Using AI for Work News](/blog/using-ai-for-work-news/): A district administrator receiving eight separate departmental reports can set up a 20-minute Google Workspace automation that delivers one weekly email surfacing cross-department clashes -- like a public works delay that will knock out a scheduled health camp -- that no individual report would flag.
- [Writing Articles from My Blog Posts](/blog/writing-articles-from-my-blog-posts/): A civic think tank analyst with 40 research reports can ask AI to pick the strongest op-ed angle for a target publication and draft it from their own words -- in an afternoon, not a week of rewriting from scratch.

</details>

<details>
<summary>See community builder use cases</summary>

- [Extracting AI Advice](/blog/extracting-ai-advice/): A community manager who has years of recorded Q&A sessions and AMAs can map-reduce all the transcripts to find the top recurring questions members actually ask -- then build a self-serve knowledge base from members' own words rather than guessing what to put in it.
- [Finding Old Friends with Gemini](/blog/finding-old-friends-with-gemini/): A community builder trying to re-engage lapsed members can use Gemini Deep Research to find where they are now -- new employer, new city, new name -- and reach out at the right career moment rather than to a dead email address.
- [Using AI for Work News](/blog/using-ai-for-work-news/): A community manager can set up a weekly automation that scans public sources for what members have been doing -- new articles, talks, job changes, launches -- and auto-drafts a "members in the news" section for the newsletter that would otherwise go unwritten for lack of time.
- [Transcript AI-ded Interviews](/blog/transcript-ai-ded-interviews/): A community builder who runs office hours or mentorship sessions can synthesise all the session transcripts to surface the top recurring problems members raise -- then use that signal to design better programming rather than guessing what the community actually needs.
- [TDS Comic Generation](/blog/tds-comic-generation/): A community builder can create a recurring comic strip with a few consistent mascots to announce events, explain community norms, or celebrate member milestones -- something memorable and shareable in a way that a plain-text post is not, and producible in minutes with no design budget.

</details>

---

When I delivered the [Society for Clinical Data Management keynote](https://sanand0.github.io/talks/2025-12-05-scdm-keynote/), they audience was surprised how much I knew about their field because I spoke about [Informed Consent Forms](https://sanand0.github.io/talks/2025-12-05-scdm-keynote/#4) and [Extracting Schedule of Assessments](https://sanand0.github.io/talks/2025-12-05-scdm-keynote/#13) and so on. Truth is, I know _nothing_ about these. Claude created the slides. I asked it to explain enough so I can talk through it.

I didn't get the implication then, but I think I do now, and the implication is stunning. I now have material to deliver a talk to _any_ audience.

So far, I've been limiting myself to technical talks. Why bother? I can speak to any audience about using AI in their field.

- **Human Resources & Organizational Design:** HR leaders are drowning in qualitative data (interviews, performance reviews, employee sentiment) and are terrified of being left behind by AI.
- **Marketing & Communications:** CMOs are under pressure to produce more content with fewer resources. They want to see live workflows of how a single blog post or chat transcript can be repurposed into a full campaign.
- **Finance & Banking:** This sector is heavily regulated and drowning in unstructured paperwork. Extract specific clauses from 100-page compliance documents will immediately capture the attention of risk officers.
- **Event Management (MICE):** The industry that organizes conferences is itself looking to modernize. Matching attendees, transcribing massive archives of past events, or predict logistical needs is highly relevant.

Time to get out of my comfort zone!

<!--
https://chatgpt.com/c/699b13b5-04cc-83a4-b835-9c37dd4ce2cd
https://gemini.google.com/app/f686c3ce03bdb116
-->
