---
title: Agent-consumable content
date: 2026-05-19T11:08:59+08:00
categories:
  - llms
  - how-i-do-things
---

![](https://files.s-anand.net/images/2026-05-19-agent-consumable-content.avif)

I'm making more and more of my content agent-consumable, i.e. easier for ChatGPT, Claude Code, etc. to read, in three ways.

One, I **export** content in an agent-friendly way.

- **Google email, calendar, chat**. I use [`gws`](https://github.com/googleworkspace/cli) to [back up](https://github.com/sanand0/scripts/blob/4071a2a795817177789531aeb1dd2ed8bb732199/backupgoogle.py) into scannable one-line entries.
- **Meet recordings**. I [back up](https://github.com/sanand0/scripts/blob/4071a2a795817177789531aeb1dd2ed8bb732199/backupmeet.py) transcripts and videos (with a compact audio copy).
- **WhatsApp chats** that I [back up](https://github.com/sanand0/scripts/blob/4071a2a795817177789531aeb1dd2ed8bb732199/backupwhatsapp.py) into similar one-liners.
- **Browsing history** by [exporting](https://github.com/sanand0/scripts/blob/4071a2a795817177789531aeb1dd2ed8bb732199/browsing_history.py) my Edge history SQLite database.
- **Daily activities** by [integrating](https://github.com/sanand0/scripts/blob/4071a2a795817177789531aeb1dd2ed8bb732199/activities.py) the above with my command line and commit history.
- **AI conversations** by exporting them manually or via [bookmarklets](https://tools.s-anand.net/aiscrapers/).
- **Social media records** like LinkedIn invites/conversations, Twitter, Hacker News, Discourse, etc via [bookmarklets](https://tools.s-anand.net/) or [scripts](https://github.com/sanand0/scripts/).
- **Financial records** like bank statements, receipts, payslips, tax filings, utility payments, rentals, property records, investments, insurance, pensions, invoices, credit scores, etc. by exporting them manually.
- **Medical records** like tests, prescriptions, doctor visits, etc. by exporting them manually.
- **Personal records** like certificates, educational records, CV, passport / visa applications, etc. by exporting them manually.

Two, I **log** / **generate** more content. For example:

- **[Things I learnt](https://til.s-anand.net/)** and **[blog posts](https://www.s-anand.net/blog/)** I write.
- **[Prompts](https://github.com/sanand0/blog/blob/live/pages/prompts/)** I use frequently.
- **[Trending GitHub repos](https://tools.s-anand.net/trending-repos/)** I want to evaluate.
- **[Talks](https://sanand0.github.io/talks/)** I deliver and **[data stories](https://sanand0.github.io/datastories/)** I write.
- **[Demos](https://sanand0.github.io/llmdemos/)** I build and **[code](https://sanand0.github.io/)** I write.
- **[Weight](https://www.s-anand.net/blog/i-lost-22-kg-in-22-weeks/)** and other fitness data.
- **[Teaching material](https://tds.s-anand.net/)**, **[assessments](https://exam.sanand.workers.dev/tds-2026-05-ga0)** and **[evaluations](https://sanand0.github.io/datastories/tds-2026-01-p1/)** and **[analysis](https://sanand0.github.io/tds-2024-sep-project-2-results/similar.html)**.
- **Coding agent logs**.
- **Sensors**: Location, mostly.
- **Daily journals**: Food, sleep, deeds, pains, ...
- **Media journals**: Books, movies, TV series, ...
- **Notes** (of various kinds): TODOs, app / tool ideas, people I know / meet, questions I'm asked, my beliefs, ...

(Notably missing are photos / videos, which I've fallen out of the habit of.)

Three, I **summarize** the content for agents. For example:

- **Adding blog frontmatter** by [summarizing](https://github.com/sanand0/scripts/blob/4071a2a795817177789531aeb1dd2ed8bb732199/summarize.py) my [blog posts](https://github.com/sanand0/blog/)
- **Adding transcript frontmatter** by [summarizing](https://github.com/sanand0/scripts/blob/4071a2a795817177789531aeb1dd2ed8bb732199/summarize.py) my meeting transcripts.
- **Identifying actions** [extracted](https://github.com/sanand0/scripts/blob/4071a2a795817177789531aeb1dd2ed8bb732199/setup.fish#L309) from transcripts.
- **Summarizing my code** as [podcasts](https://github.com/sanand0/sanand0/).
- **Summarizing prompts** as [SKILL.md](https://github.com/sanand0/scripts/tree/main/agents) files.
- **Summarizing conversations** into advice for [AI](https://www.s-anand.net/blog/ai-advice-for-teams/), [time management](https://www.s-anand.net/blog/time-management/), etc.
- **Summarizing technical choices** into a **[technology radar](https://tools.s-anand.net/radar/)**
- **Extracting transcripts elements**, like insights, experiments to run, actions, what I missed, what they missed, etc.

On my list is [Karpathy's LLM wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), summarizing my photos, and more.

Just _writing_ this post took me an hour! It also convinced me that I have _lots_ of content and there's a lot of under-leverage in unleashing agents on what I already have.
