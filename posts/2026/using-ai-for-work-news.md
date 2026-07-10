---
title: Using AI for work news
date: '2026-02-14T14:32:16+08:00'
categories:
- business-realities
- llms
description: Workflow automation can turn scattered organizational signals into useful recurring newsletters that keep distributed teams aware of internal innovation.
tags: [automation, ai]
---

This week, [Namit](https://www.linkedin.com/in/namit-sureka-43ab89) and I met a Straive team that operates from a client office. One team member asked:

> I believe that we are doing wonders out here, but we are closed from what is happening in the rest our organization.
>
> I want team members to interact with others to see what interesting things they have delivered and where we can implement that solution.
>
> Could we have sessions, maybe a monthly newsletter, showing what innovations we're working on? This would really keep us engaged with the tech that is going outside of the work that we do.

A good point. This reminded me of an experiment last month.

---

[Google Workspace Studio](https://studio.workspace.google.com/) lets you create automations. For example, here's a [flow I set up to create a weekly newsletter about client news](https://studio.workspace.google.com/workflow/ydef223dcc0e1c583207620711f3fc01a):

[![](https://files.s-anand.net/images/2026-02-14-google-workspace-studio.webp)](https://studio.workspace.google.com/workflow/ydef223dcc0e1c583207620711f3fc01a)

- **Step 1: On a schedule**. Every Monday at 8am...
- **Step 2: Ask Gemini**. Scan my Google Workspace for the latest client related news and organize it as an email newsletter. Also find the latest news about these clients from the web and put it together seamlessly. Write it in a nice Malcolm Gladwell style narrative.
- **Step 3: Ask Gemini**. Just write today's date in YYYY-MM-DD format. Nothing else
- **Step 4: Draft an email**.
  - To: me.
  - Subject: Weekly news [Step 3: Content created by Gemini]
  - Message: [Step 2: Content created by Gemini]
- **Step 5: Create a doc**.
  - New doc name: Weekly news [Step 3: Content created by Gemini]
  - Content to add: [Step 2: Content created by Gemini]
  - Location for new doc: [Weekly news](https://drive.google.com/drive/folders/1G3qOPQvtGLVlIeC_7b9SvBmkx52qzg_a)

---

Now, I get to see a nicely formatted newsletter every Monday morning about new client activity, added to a [Weekly news](https://drive.google.com/drive/folders/1G3qOPQvtGLVlIeC_7b9SvBmkx52qzg_a) Google Drive folder accessible to Straive.

For example, I learnt that:

- One client blocked coding agents (Codex, Claude Code, etc) which has slowed down our team.
- Another client needs to modify their API Gateway + Lambda infrastructure to handle long-running agents without exceeding API timeouts
- Yet others requested omni-channel convergence optimization, price sensitivity modeling, payments infrastructure setup, and much more.

---

I always wished we had an "internal reporter" at Gramener, going around, interviewing teams, and writing interesting stories about what's happening.

I did **not** expect I'd be able to hire Malcolm Gladwell (or _anyone_ I want) as our internal reporter!
