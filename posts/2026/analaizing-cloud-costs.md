---
title: AnalAIzing Cloud Costs
date: '2026-03-01T16:21:25+08:00'
categories:
- llms
description: I asked Codex to audit my $6.71 GitHub bill and found I was far below the free Actions limit. It also uncovered minute-floor billing, Copilot workflows, and a cheaper blog deployment.
tags: [coding-agents, data-analysis, forecasting]
---

<!--
Codex session: /home/sanand/.codex/sessions/2026/02/28/rollout-2026-02-28T11-23-34-019ca245-e0dc-7932-be83-05f3cb4ef1f1.jsonl
Gemini insights about the session: https://gemini.google.com/app/2c5abf249292a22e
-->

I have a [GitHub Education](https://github.com/education) since I [teach at IITM](https://study.iitm.ac.in/ds/course_pages/BSSE2002.html). But if I switch back to a free account, how much would I need to pay?

I asked Codex (5.3, xhigh):

> My GITHUB_TOKEN is in .env. Go through my GitHub billing. Ignore the $100 sponsorships I make. Other than that, my current metered usage is $6.71 for Feb 2026 (which is included in my billing plan). $0.35 comes from sanand0/exam and $0.34 from sanand0/blog and so on. That's coming mostly from "Actions Linux", occasionally "Actions Storage". Pick a few of the top repos and tell me what I should do to make the cost zero - or reduce the cost as much as possible. See if there's a pattern across repos.
>
> Document all of your findings in `analysis.md` and continue to append new findings in this file, summarizing my request as a heading followed by your response.
>
> My aim is to stay well below the 2,000 free actions minutes/month - which I'm already below. But still, I want to optimize a bit... Tell me
>
> - What my billing would be under a free account
> - What repos and what activity are the biggest risks for hitting the free limit

After half an hour of my watching a movie, it told me (in great detail - see the details below) that:

- My billing is _way_ below the free limit.
- I should watch out for GitHub Copilot, frequent CI runs, scheduled jobs.

But the more interesting thing for me is how easy cloud optimization has become with coding agents.

![](https://files.s-anand.net/images/2026-03-01-analaizing-cloud-costs.avif) <!-- https://gemini.google.com/app/2c5abf249292a22e -->

- **It makes curiosity cheaper**. I wouldn't have sat and written the scripts to figure out where $6.71 went. But coding agents made micro-audits practical (and with clever use of `jaq`, `csvq`, and `duckdb`. If you can get an answer by just from a question, we'd use it like Google - to **answer ad hoc questions**.
- **It challenges common sense**. I assumed caching was good for speed and compute. But Codex's analysis of my [`sanand0/blog` actions](https://github.com/sanand0/blog/actions) pointed out that dropping a job's time from 1.2 minutes to 0.7 minutes doesn't change the _2-minute billed floor_! Also, the 114MB cache _increased_ storage costs. We can **test optimizations without assuming**.
- **It exposes blind spots**. Turns out that a big chunk of the cost of my (private) [TDS exam](https://exam.sanand.workers.dev/tds-2026-01-ee) repo was `dynamic/copilot-pull-request-reviewer` - a GitHub workflow triggered by using Copilot. I also have a big chunk of "legacy" GitHub Pages on older repos that add to cost because of failures and retries. We can find these invisible leeches draining cost **without knowing what to ask for**.
- **It self-corrects**. Codex hit a deprecated GitHub billing endpoint (HTTP 410). It curled the GitHub docs, found the new endpoint, and rewrote its query. It made a mistake with `csvq`, read the help, and switched to `duckdb` for complex median calculations. That self-correction and learning means that it can **work while you sleep**.
- **It fixes, not just finds**. Codex rewrote my [blog deployment script](https://github.com/sanand0/blog/commit/2644e9bfcfb4369c2768fbfad599fa939ada2e0f#diff-28802fbf11c83a2eee09623fb192785e7ca92a3f40602a517c011b947a1822d3) to use a single job instead of two, to save compute time. I just copied andd deployed it. It went from **researcher to advisor**. That's a short step from executor, next.

If analyzing cloud cost is this easy, Cloud FinOps companies face a risk.
AWS, Azure, and GCP will simple embed Cloud FinOps into their services.
Cloud spend won't fall -- we'll just use more compute for the same budget.

The big Cloud FinOps companies (e.g. IBM, Flexera, Broadcom) are in some trouble. They can't cannibalize their own market. They'll likely shrink and focus on banks & Governments that need a reputable partner.

Companies that _own_ the infra data (e.g. DataDog, Snowflake, DataBricks) will likely grow, since only they can access the context for optimization. That'll let them provide better service cheaper, e.g. auto-optimize queries, compute, storage, etc. for you.

Pure plays (e.g. CloudZero, Finout) might need to pivot from infra optimization to... something more strategic, I guess.

---

<details>
<summary>Here's the full (long) response from Codex</summary>

- Data source: `GET /users/sanand0/settings/billing/usage` using your token in `.env`.
- Snapshot time: 2026-02-28T03:24:45Z (UTC).

Ignoring sponsorships, Feb 2026 metered usage is:

| Product                   | Gross Amount |
| ------------------------- | -----------: |
| Copilot Premium Request   |        $5.05 |
| Actions (Linux + Storage) | $1.646844306 |
| Git LFS storage           | $0.009750857 |
| Total                     | $6.706595163 |

Top Actions repos in Feb 2026:

| Repo                           | Total Actions Cost |   Linux Cost | Storage Cost | Linux Minutes |
| ------------------------------ | -----------------: | -----------: | -----------: | ------------: |
| `exam`                         |       $0.354000000 | $0.354000000 | $0.000000000 |            59 |
| `blog`                         |       $0.337295637 | $0.246000000 | $0.091295637 |            41 |
| `tools-in-data-science-public` |       $0.211055072 | $0.204000000 | $0.007055072 |            34 |
| `tools`                        |       $0.174166256 | $0.174000000 | $0.000166256 |            29 |
| `iss-location`                 |       $0.174000000 | $0.174000000 | $0.000000000 |            29 |
| `imdbscrape`                   |       $0.168000000 | $0.168000000 | $0.000000000 |            28 |

Cross-repo pattern:

- Your cost is dominated by **minute-floor billing per job** and **trigger frequency**, not pure runtime.
- Feb run-level pattern (from fetched run/job metadata in top repos):
  - `dynamic`: 9 runs, 79 billed-like minutes (~8.78/run)
  - `push`: 50 runs, 81 billed-like minutes (~1.62/run)
  - `schedule`: 55 runs, 57 billed-like minutes (~1.04/run)

Primary cost-reduction levers:

1. Disable Copilot dynamic code-review/agent workflows on repos where not needed (`exam`, `tools` were the big dynamic consumers).
2. Restrict Pages deploy workflows to `main` only (avoid `dev`/feature branch deploys).
3. Merge 2-job build+deploy workflows into one job where feasible (reduces per-job minute floor).
4. Reduce scheduled frequency for daily cron repos if not needed (`iss-location`, `imdbscrape`).
5. For storage, reduce artifact/caches and cleanup stale artifacts.

---

I expanded analysis across all 14 repos that used Linux Actions minutes in Feb 2026 and fetched per-run job details.

**1) `sanand0/blog`: does disabling cache improve costs?**

Workflow history:

- Cache was introduced in `.github/workflows/deploy.yml` commit `4f744fffdeb64aebd09cfc6fd1bb27fd9844842d` on **2026-02-20T04:40:39Z**.
- Previous workflow commit: `61392ee781ff77e9914b0a1a68b852f46d0a66e8` on **2026-01-02T03:11:32Z**.

Observed runs around this change (`main` + `dev` only):

| Phase                          | Runs | Avg Active Job Min | Median Active Job Min | Avg Billed-like Min | Median Billed-like Min |
| ------------------------------ | ---: | -----------------: | --------------------: | ------------------: | ---------------------: |
| Before cache (Jan 2 -> Feb 20) |   62 |              1.192 |                 0.900 |               2.194 |                    2.0 |
| After cache (Feb 20 -> Feb 28) |    6 |              0.744 |                 0.817 |               1.667 |                    2.0 |

Interpretation:

- **No clear billed-minute win from cache**: median billed-like is still 2/run in both periods (minute floor + 2 jobs dominates).
- Cache likely helped runtime modestly (small active-minute decrease), but sample after cache is small (`n=6`) and confounded by other workflow changes.
- Storage side: current `blog` caches are ~114 MB. If that stayed all month, rough max cost is about **$0.026/month** at observed storage unit price; this is only part of `blog` storage charge (`$0.0913`).
- Therefore, disabling cache may save some storage, but **the main cost lever is reducing run count and job count**, not cache toggles.

**2) Better `blog` optimizations than cache-off**

High-impact changes:

1. Trigger deploy only on `main` (Feb had 20 `dev` deploy runs vs 2 `main`).
2. Add path filters so non-site changes do not deploy.
3. Use a **single deploy job** (instead of separate `build` + `deploy`) to reduce minute-floor overhead.
4. Keep `[skip ci]` support.

Explicit workflow suggestion file created:

- `/home/vscode/Downloads/github-usage/analysis/blog-cost-optimized-deploy.yml`

**3) Additional repo pattern findings (expanded set)**

Feb 2026 Linux-minute repos and event patterns:

| Repo                           | Minutes | Main pattern                                                                   |
| ------------------------------ | ------: | ------------------------------------------------------------------------------ |
| `exam`                         |      59 | dynamic Copilot runs (`Copilot code review`, `Running Copilot coding agent`)   |
| `blog`                         |      41 | push deploy workflow (`Deploy Hugo site`)                                      |
| `tools-in-data-science-public` |      34 | push deploy + some dynamic pages runs                                          |
| `iss-location`                 |      29 | daily schedule                                                                 |
| `imdbscrape`                   |      28 | daily schedule                                                                 |
| `tools`                        |      29 | push deploy + dynamic Copilot review                                           |
| `pyoppe`                       |      10 | dynamic `pages build and deployment` (legacy Pages), includes retries/failures |
| `schoolai`                     |       6 | dynamic `pages build and deployment` (legacy Pages)                            |
| `image-filters`                |       6 | dynamic `pages build and deployment` (legacy Pages)                            |
| `llmpricing`                   |       3 | dynamic `pages build and deployment` (legacy Pages)                            |

Important hidden pattern:

- `pyoppe`, `schoolai`, `image-filters`, `llmpricing` use **Pages build_type = legacy** and incur dynamic pages runs.
- These runs are tiny but still billed at minute floor and can multiply via retries/failures.

**4) What your billing would be under a free account**

Assumptions for this estimate:

- Focus on Actions minutes/usage behavior from your Feb 2026 data.
- Sponsorships still excluded.
- Copilot Premium Request billing is separate from Actions minutes.

Your Feb Actions usage:

- All repos Linux minutes: **258**
- Private-repo Linux minutes (`exam`): **59**

Estimate:

- Under a 2,000-minute free limit, both 258 and 59 are far below the cap.
- So for Actions minutes specifically, you would still be **$0 overage** this month.

**5) Biggest risks for hitting the free limit**

If your objective is avoiding 2,000-minute overflow, the highest-risk activity patterns are:

1. **Dynamic Copilot runs on private repos** (high minutes per run).
   - Example observed: `exam` dynamic runs consumed 59 minutes from 5 runs.
2. **Many frequent push deploys on multi-job workflows** (2-minute floor per push is common).
   - Example: `blog` and `tools-in-data-science-public`.
3. **Daily scheduled jobs across many repos**.
   - One daily repo is ~30 min/month baseline; many such repos accumulate predictably.
4. **Legacy Pages dynamic builds with retries/failures**.
   - Small runs, but multiplicative retriggers add up.

Rule-of-thumb risk math:

- ~1 daily scheduled workflow ~= 30 min/month.
- ~1 two-job push deploy ~= ~2 min/run.
- ~1 Copilot dynamic review run can be ~8-15 min/run.

</details>
