---
title: Things I Learned - 07 Dec 2025
date: 2025-12-07T00:00:00+00:00
categories:
  - til
description: I explored Pytest 9.0 subtests, Git’s data model, and fuzzy matching algorithms. I also investigated AI coding traps, how confessions improve model honesty, and why Theory of Mind is the key to better human-AI collaboration.
tags: [git, llm-evaluation, cli-tools, productivity]
---

This week, I learned:

- Pytest finally supports subtests in pytest 9.0.0+. [Simon Willison](https://til.simonwillison.net/pytest/subtests)
- From [The Tim Ferriss Show](https://tim.blog/podcast): [#837: How to Simplify Your Life in 2026 — New Tips from Derek Sivers, Seth Godin, and Martha Beck](https://rss.art19.com/episodes/77e6511e-b5bb-4f3e-87d7-019f4e297767.mp3?rss_browser=BAhJIg9BbnRlbm5hUG9kBjoGRVQ%3D--bba5bdd77df5f5806138bf3e7d4615ea7f8e6a75):
  - Look for single decisions that remove hundreds of other decisions. Peter Drucker via Jim Collins. E.g. Work only on LLMs, no new books this year, ...
  - Derek Sivers:
    - Simple is not easy. Interdependency is complexity. Assets are dependencies. Accumulating information, purchases, employees/helpers, relations, etc. adds dependency. That makes life harder, challenges identity. Interdependency may be desirable - but reduce it in specific areas, to specific extents, temporarily, etc. Question every assumption: "Do you really need it?"
    - Here are [some examples for me to try](https://chatgpt.com/share/69313db2-643c-800c-b216-2810c9377ab1)
    - Derek Sivers has no monthly payments (including income) or receipts (no subscriptions) at all! His code has **no** external code dependencies at all, and is building a house from scratch.
  - Seth Godin:
    - Know WHO it (whatever you're doing) is for. Focus ONLY on _that_ audience. Did it matter to them? Ignore the bad feedback from the person it was never intended for.
    - Never exceed a budget or deadline. When either runs out, you are done.
    - Treat any Yes/No you say as FINAL.
    - Skip meetings where a memo will suffice.
- Apparantly, nudges are not as effective as the book Nudge suggests. In fact, there seems to be no evidence for it if we adjust for publication bias (i.e. only publication-worthy stuff gets published.) [The Behavioral Scientist](https://www.thebehavioralscientist.com/articles/bad-news-for-nudges) [#](https://claude.ai/chat/2dfca86e-e304-48ec-bdbb-41c32ea7bbe2)
- 71% of HTTP DDoS and 89% of network-layer—end in under 10 minutes. That's too fast for any human or on-demand service to react. Legacy DDoS defenses have become obsolete. The most popular botnet, Aisuru, is pivoting to content scraping for AI projects. The vectors are cheap, insecure routers, e.g. from Indonesia. ([Claude](https://claude.ai/share/0d868126-01fd-4840-813c-88888fd9d209))
- This [5El AI Evaluation Workshop](https://hasgeek.com/fifthelephant/ai-evaluation-workshop/) suggests 4 layers of evaluation for code:
  - Syntactic Evaluation: Does it compile?
  - Semantic Evaluation: Does it do what a good analyst / programmer would?
  - Business Logic Evaluation: Does it do what a good business analyst / manager would?
  - Human Alignment Evaluation: Does it do what a good coach / leader would?
- [Julia Evans shares](https://jvns.ca/blog/2026/01/08/a-data-model-for-git/) an ultra-clear explanation of the [Git data model](https://github.com/git/git/blob/master/Documentation/gitdatamodel.adoc). What I learnt is that:
  - Gathering feedback on docs ("What's confusing? Any questions? What's missing? Or wrong?") for evidence-based updates. [Julia Evans](https://jvns.ca/blog/2026/01/08/a-data-model-for-git/#getting-test-readers-to-identify-problems)
  - Git stores entire files each version, not diffs. Diffs are computed on the fly.
  - Each commit has an author (who writes the code) and a committer (who checks it in). #TODO Why two fields?
  - Branches and tags are both references to a commit. But branches are updated on commit, tags are not.
  - The staging area is a separate data structure, [the index](https://github.com/git/git/blob/master/Documentation/gitdatamodel.adoc#the-index). #TODO Why a different data structure?
  - The [reflog](https://github.com/git/git/blob/master/Documentation/gitdatamodel.adoc#reflogs) tracks all local "activity". E.g. `git reflog --date=iso`
- To fuzzy-match 2 columns of text (e.g. customer names, product names, ...) you need 2 things:
  - A text matching algorithm ([rapidfuzz](https://github.com/rapidfuzz/RapidFuzz), [fuzzball](https://npmjs.com/package/fuzzball), ...) and/or semantic matching (e.g. embedding similarity) for pairwise similarity
  - An assignment algorithm (e.g. Jonker-Volgenant, Hungarian, ...) for 1-to-1 matches in [JS](https://www.npmjs.com/package/linear-sum-assignment) or [Python](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linear_sum_assignment.html),
- WhatsApp [backups on Google Drive](https://drive.google.com/drive/backups) can't be downloaded, even if they're unencrypted. [ChatGPT](https://chatgpt.com/share/692e710d-7974-800c-a5d2-1c710a7ae743).
- OpenAI finds that [confessions](https://openai.com/index/how-confessions-can-keep-language-models-honest/) as a training method reduces scheming, reward hacking, etc. It can be applied to models even now. This can (less effectively) be applied at inference time as well:
  - Sample confession prompt: Did you fully address both the letter AND spirit of my question? List any shortcuts taken, corners cut, or ways you optimized for appearing correct rather than being correct. What did I actually want vs what you provided?
- [Agents4Science](https://agents4science.stanford.edu/) is a Stanford conference where AI co-authored papers are co-reviewed by AI and selected for presentation. [Video](https://youtu.be/7pXqAeedqOo)
- Buddha seems more a philosopher like Socrates ("Question what I say") than a religious leader. [#](https://claude.ai/chat/589972fe-2c6a-4f33-9127-6a19e4df81ae)
  - How did _he_ spawn a religion?
  - Interesting that both were within a few centuries of each other. Coincidence? Were there more like them around the same time? At other times?
- Some more new CLI tools I installed:
  - [`fx`](https://fx.wtf/): CLI JSON viewer. Sort of like `less` for JSON. Fast, intuitive.
  - [`mdq`](https://github.com/yshavit/mdq): Markdown query tool
- [YTScribe](https://ytscribe.ai/) is yet another YouTube transcription service.
- Note to self, since I keep forgetting this: On Android Edge, select the new tab page, click on the 3 dots at the top right, and select "Recent tabs" to see tabs from other devices. `edge://recent-tabs`
- When evaluating an LLM's biases or natural preferences, set temperature=1 for a representative logprob distribution. [LLM Bias](https://anomify.ai/resources/articles/llm-bias)
- My ideal AI coding cycle looks like this: (Research, Prototype, repeat), Plan, (Code, Run, Test, Fix, repeat), Refactor, Post-mortem, Document.
- [The AI coding trap](https://chrisloy.dev/post/2025/09/28/the-ai-coding-trap) is a very clear explanation of AI coding vs vibe coding. It visually explains how coding agents shrink coding time, not thinking / fixing time; how delegating with ownership is slower but more sustainable than delegating just easy tasks; and how AI coding is more like the former, while vibe coding is like the latter.
- [Claude Agent Skills: A First Principles Deep Dive](https://leehanchung.github.io/blogs/2025/10/26/claude-skills-deep-dive/) is a comprehensive documentation of how Claude Skills work. A bit too long but readable.
- [Claude Code is a Beast – Tips from 6 Months of Hardcore Use](https://www.reddit.com/r/ClaudeAI/comments/1oivjvm/claude_code_is_a_beast_tips_from_6_months_of/) has extensive suggestions for Claude Code - many of which apply to most coding agents.
- [LMArena's Code Arena](https://lmarena.ai/code) evaluates models on agentic coding. Anyone can use it. It passes your task to two models and lets you compare their output. [I tried building a "gibberifier"](https://lmarena.ai/c/019ada14-9f0c-7dba-afaa-65252cfe203c) and discovered a new model, "robin" that's certainly better than Kimi K2 and perhaps better than Gemini 3 Pro. Theory is that it's an OpenAI model. Looking forward to it!
- ⭐ Based on [Quantifying Human-AI Synergy](https://osf.io/preprints/psyarxiv/vbkmt_v1) by Reidl & Weidman [#](https://claude.ai/chat/ae3e8716-9be4-47ad-85c7-9c7b257d375b):
  - Theory of Mind (ToM) is understanding that others have their own beliefs, knowledge, and goals (different from yours, may be wrong) and to use that to explain & predict their behavior.
  - ToM and problem solving are _distinct skills_. ToM skill boosts AI collaboration, but **not** better problem solving!
  - ToM isn't a stable trait. It fluctuates from chat to chat for anyone.
  - Implication: Design models & systems for clarity & collaboration, not just accuracy.
- [Text Gibberifier](https://gibberifier.com/) adds lots of human-invisible unicode characters to text, making it harder for LLMs to read without affecting human readability. May be useful if you want to discourage LLM-processing of your content - but it feels like the anti-SEO of the future.
- The argument that technologically unemployed will find other jobs may not apply to general-purpose technology, e.g. electricity, internal combustion engine, maybe AI - technologies that can automate multiple sectors of the economy simultaneously. When one sector loses jobs, there may not be (in the short/medium term) other jobs to take up. [Alex Imas + Claude](https://claude.ai/share/811ad94b-f6dc-4251-9548-e3ad40f2c36a)
- History is filled with examples where technology enabled new art forms. Here's my guess on what LLM image generation will enable:
  - Synthetic memory: Photos of what you remember happening.
  - Alternate history: Photos of events that never happened.
  - AImoji: Instead of texting "I'm running late" the LLM generates you riding a snail through a traffic jam of alarm clocks.
  - Personal signature styles: Not "paint like Van Gogh" but "paint like my grandmother's kitchen memories filtered through anxiety."
  - Memes: "What does the Mona Lisa become after 100 generations of AI interpretation?"
- [Improving Front-end Design through Skills](https://www.claude.com/blog/improving-frontend-design-through-skills) shares a prompt to improve front-end code quality that would apply in most cases. I [tweaked and added it](https://github.com/sanand0/scripts/blob/live/agents/design/SKILL.md) to my skill list.
