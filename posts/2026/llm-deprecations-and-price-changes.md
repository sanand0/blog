---
title: LLM Deprecations and Price Changes
date: 2026-05-21T14:02:10+08:00
categories:
  - llms
---

A colleague told me a near-miss horror story.

> As Google began deprecating Gemini 2.0, we moved to Gemini 2.5 Pro. But reasoning is enabled by default and cannot be turned off.
>
> For our specific problem statement, reasoning was not required. Token costs increased 10x and speeds were 3-4x slower. We moved the client to Gemini 2.5 Flash Lite, which has reasoning turned off by default and offers much lower latency.

Because we track compute costs closely, we managed this without a major financial impact.

But model updates clearly require careful testing on the cost and latency front as well, not just output quality.

---

AI used to keep getting cheaper. But now it's more a "convergence".

![](https://files.s-anand.net/images/2026-05-21-llm-pricing.svg)

Each line traces a model family. The X-axis is its intelligence ([LMArena ELO score](https://lmarena.ai/leaderboard)) and the Y-axis is the input cost ($ per million tokens, log scale). Time flows roughly left to right as models improve.

Three patterns emerge and each seems strategic.

1. Gemini Flash rockets upward (cheap -> expensive, moving right).
2. GPT-4 class collapses from $30 toward $1.25, then GPT-5.5 jumps back up to $5.
3. Claude Sonnet runs perfectly flat (cheap stays cheap as it gets smarter).


### Google's Loss Leaders

Gemini 1.5 Flash was $0.075/MTok in August 2024. I told everyone to use it - it's a fantastic, affodable model.

Gemini 3.5 Flash, released this week at Google I/O, is $1.50. That's a **20× in 21 months**. Looks like **"Flash" is more a brand position than a price position.** It migrates up-market.

Same for Gemini 1.5 Flash 8b (3.75 cents) which migrated into Gemini 3.1 Flash Lite (25 cents - a 6.7× increase).

Gemini Pro went the opposite direction: down from $5.00 (1.5-pro in Oct 2024) to $1.25-$2.00 today. Pro seems to be a competitive weapon against Anthropic and OpenAI at the top, while monetizing the middle.

Of course, Gemini's real lock-in is the Google Workspace bundling and Search AI Mode. Personally, I subscribed to Google Pro for the first time in 20 years just for these bundled capabilities.

By the time people notice the Flash price, it's hard to leave the ecosystem.

### OpenAI's Relaunches

The price chart speaks for itself:

| Model       | Price |
| ----------- | ----: |
| GPT-4       |   $30 |
| GPT-4 Turbo |   $10 |
| GPT-4o      | $2.50 |
| GPT-4.1     | $2.00 |
| GPT-5       | $1.25 |
| GPT-5.2     | $1.75 |
| GPT-5.4     | $2.50 |
| GPT-5.5     | $5.00 |

Maybe their strategy seems is: scale current technology to commodity (the O-series showed the same pattern with $15 for O1 falling to $1.10 for O4-mini in 7 months), _THEN_ launch a new frontier above it, and repeat?

### Anthropic's Revisions

Claude Sonnet has held at **exactly $3.00/MTok input** for over two years, across four model generations and an ELO gain of nearly 200 points. Pretty unusual.

Opus came down from $15 to $5 in November 2025 - likely a deliberate move to make it production-viable. Haiku crept from $0.25 to $0.80. The tiers are converging.

There's a twist, though. Anthropic restructured enterprise contracts in late 2025. Seat prices dropped to $20/seat. Token discounts (previously 10-15% off API rates) were removed. For a 100-seat team, that adds ~$15K-$40K to annual TCO. So, prices went down, but _the actual bill went up_.

Also, Opus 4.7 uses a new tokenizer that may consume ~35% more tokens for the same text. It's worth re-benchmarking prompts before assuming $5 is 1/3rd of $15.

### What Do We Do?

Model family prices change rapidy. Old models get deprecated. Best to be prepared.

1. **Add multi-tier routing to your architecture:**
   - Lite / Nano / Haiku for extraction, classification, ... -- tasks with clear right answers
   - Sonnet / GPT-5.4 / Gemini Flash for most production reasoning
   - Opus / GPT-5.5 for escalation or expert advice: complex planning, hard edge cases, high-value decisions
2. **Compare _completed-task costs_**, not token price. A 2\* more expensive model can halve the retry rate, making it cheaper per successful output.
3. **Migrate by model capability**, not model family. Switch to models with similar latency, context window, output format compliance and reasoning depth.
4. **Evaluate open-source models.** DeepSeek models at self-hosted inference costs can be 90% cheaper for _commodity_ (not frontier) tasks.

**For enterprise procurement:** keep a close eye on pricing changes, API token discounts, and what was quietly removed during renewal. (AI helps with this!)

---

The first 18 months of most AI model families are **discounted customer acquisition**. Then value extraction follows. Google started it with Flash. OpenAI is doing it with GPT-5.5. Anthropic is doing it with enterprise billing restructuring.

Fair enough. Providers need to recover infra investments.

And build good routing strategies helps enterprises get the most out of this.

Just keep asking yourself: "what's our plan for when this model changes or deprecates?"

![](https://files.s-anand.net/images/2026-05-21-llm-deprecations-and-price-changes.avif)

PS: AI-generated image - has a few errors.
