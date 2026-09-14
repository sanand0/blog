---
title: Things I Learned - 13 Sep 2026
date: 2026-09-13T00:00:00+00:00
categories:
  - til
description: This week I learned how firmware reverse-engineering exposes hidden device features, why simple forecasts can beat agents, how separate identities govern AI agents, and where browser Linux and cloud browsers break.
tags: [ai-agents, forecasting, claude-code, software-engineering]
---

This week, I learned:

- [Everything I own, owned](https://schlarp.com/posts/everything-i-own-owned/) suggests that agentic reverse-engineering of firmware helps us learn:
  - Features the devices expose
  - Hidden functionalities, e.g. Shure MV7 microphone has a command shell.
  - Dependencies, supply chains and attack surfaces
  - Interesting components, e.g. RTOS webcam has small face tracking and gesture detection models
  - Change behavior, e.g. don't turn on indicator while recording
  - So, it's possible (even likely) that my TV, phone, laptop, camera, fridge, car, vacuum cleaning robot, bluetooth headphone, ... can be hacked by a rogue AI-assisted firmware update.
- "Leaving things alone is an underrated engineering skill." From [Software drives people insane](https://graybeard.ing/software-drives-people-insane/).
- Across over a thousand forecasts, agents lost to a simple exponential weighted moving average forecast. Paper: [RAP: Research Attention Prediction Reveals Target-Conditioned Evidence Acquisition Biases](https://arxiv.org/html/2609.10092v1). Maybe I should ask agents to get the latest data first, rather than directly asking them to forecast, since the latter _fetched less recent material_. <!-- https://chatgpt.com/c/6a87d052-1948-83ee-a2a2-fd7e8304d2e5 -->
- Claude Code offers [function hooks](https://github.com/anthropics/claude-code/issues/91870) if you enable `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS=1`. These let you introduce code into almost _any_ part of the Claude Code workflow, meaning you can convert Claude Code into practically amy kind of agent. (Probably a bit of competition to [Pi](https://pi.dev/).) However, neither ChatGPT nor I could figure out a use case I would need this for. We need more imagination! <!-- https://chatgpt.com/c/6a9a2f63-65e8-83ec-8dbf-83619697c0a3 -->
- The Antropic team provide [Claude Tag a separate service account](https://claude.com/blog/agent-identity-access-model). That's an interesting portable pattern: giving agents a separate Linux username, GitHub account, email ID, database user ID, etc. is a pattern we understand and know how to govern.
- [FutureSearch.ai](https://futuresearch.ai/) is a forecasting app. I'm not sure what model is behind it or how good it is, but it decomposes a forecast into measurable signals, predicts those, and synthesizes. That's a useful approach. For example, I asked it: [Will LLM model routers and model routing companies grow in popularity and review or shrink by Jan 2027?](https://futuresearch.ai/app/conversations/a350ed92-727d-46ca-8ed3-f4b6678f97bb). It broke it up into 5 forecast questions and answered them roughly as:
  - Will OpenRouter's reported weekly LLM token processing volume exceed 45 trillion tokens/week (about 1.8x its August 2026 level of ~25 trillion tokens/week) by January 31, 2027? (Yes, 95% chance. It's already high and growing fast.)
  - Will OpenRouter announce a new equity funding round, or otherwise be credibly reported to have reached a valuation above $1.3 billion, between August 2026 and January 31, 2027? (Yes, 84% chance. There seems to be market interest.)
  - Will at least one LLM model-routing competitor to OpenRouter (e.g., Martian, Not Diamond, Portkey, Unify AI, TrueFoundry) announce a new equity funding round of $20 million or more between August 2026 and January 31, 2027? (Yes, 68% chance. VCs will want to fund, and competitors exist.)
  - Will a major AI lab or cloud provider (OpenAI, Google, Microsoft/Azure, Amazon/AWS, Anthropic, or Meta) launch or significantly expand, between August 2026 and January 31, 2027, a native product feature that automatically routes a given request among multiple materially different underlying LLMs based on cost, task, or quality? (Yes, 91% chance. Microsoft already has one; Google launched a preview; AWS will likely announce in re:Invent in Dec)
  - Will Google Trends relative search interest (US, web search) for the term 'LLM router' be higher, on average, in December 2026 than it was in July 2026? (No, 25% chance. July 2026 was exceptionally high volume.)
- In [An Alien Mind](https://openai.com/index/an-alien-mind/), Jakub Pachocki, Chief Scientist at OpenAI, was quite instructive. Here's my takeaway:
  - Models could keep growing smarter at the same speed.
  - We can improve them where capability is measurable, like maths.
    In fuzzy areas, we're not even sure _how_ capable they are.
  - Values are fuzzy. Making AI follow our values is tricky.
  - We train models to follow their constitution.
    But they sometimes fail outside of their training examples.
  - We feed models alignmed data.
    But when trained against hard objectives, they gently bend rules.
  - We watch models' thoughts. We avoid feedback on thoughts - so models won't hide them.
    But models interact with agents & tools while thinking, so we _need_ to supervise thoughts.
  - Nowadays,models think _without_ verbalizing. They manipulate their own reasoning.
  - So we're exploring confessions and monitoring internals.
  - Still... best to tighten defenses. We'll use AI to research how.
- Meeting people who have a target AND who control scarce resources is a great exercise in humility. Principals of elite private schools, partner managers of top software companies, any officer with a quota (police, income tax, bank loan, IT compliance), etc. You learn to grin while bearing the pain of being with them.
- Thanks to agents, it's easy enough to maintain an Android and iOS mobile application separately #ForNow, rather than incur the overhead of React-Native (or other cross-platform frameworks). [Shopify](https://shopify.engineering/back-to-native) is making testing easy by "... designing our app architecture to work for both humans and agents."
- [Use `re.prefixmatch()` instead of `re.match()` in Python 3.15+](https://discuss.python.org/t/add-re-prefixmatch-deprecate-re-match/105927/7). This [article](https://hugovk.dev/blog/2026/soft-deprecating-re.match/) captures the reason well. (I failed the quiz at the start despite almost 2 decades of Python programming - and LLM atrophy).
- You can run Linux distributions in the browser. For example, this is a simple, embeddable [buildroot distribution](https://copy.sh/v86/?profile=buildroot) that runs purely in the browser. There's [Nix](https://trynix.dev/). There's [Alpine Linux](https://bellard.org/jslinux/vm.html?cpu=x86_64&mem=256&url=alpine-x86_64.cfg). Interestingly, `curl https://example.com/` works on Alpine Linux, unconstrained by same-origin policies. It is relayed by the host (bellard.org in this case) via WebSockets, so it can even `ssh` into other servers. [ChatGPT](https://chatgpt.com/share/6aa2ba6e-ee84-83ec-b406-834846bd636a) <!-- https://chatgpt.com/c/6aa2b566-28e0-83ec-a4a4-034688295f5b -->
- ChatGPT's Cloud Browser doesn't forward all events - so it gets stuck on captchas, like Cloudflare's, when visiting sites like StackOverflow. [Here's an example](https://chatgpt.com/share/6aa288cb-b73c-83ec-8bd4-e45b7d1d4ae6). <!-- https://chatgpt.com/c/6aa2873f-5228-83ec-ac29-0902b8d9d628 -->
- Several top-level domains have over 50% of new registrations in 2025 blocklisted. Scammers use new domains extensively. But policing new domains also stops genuine protesters, so it's not clear what the right approach is. [The purpose of DNS is to spread scams](https://shkspr.mobi/blog/2026/09/the-purpose-of-dns-is-to-spread-scams/).

## Questions I was asked

[Week ending 13 Sep 2026](https://www.s-anand.net/blog/questions-i-am-asked/#week-ending-2026-09-13)

- **Question**: Why is it getting harder for graduates to get hired when AI can do a lot of the old work?\
  **Answer**: It is true, but not because graduates can do less. We haven't figured out what we need graduates for: AI can do the old roles, the new roles and assessment criteria are still unclear, so companies wait or reduce hiring a little.
- **Question**: Is government AI adoption driven by utility or FOMO?\
  **Answer**: Both. FOMO is not necessarily bad if it gets people to experiment; the problem is when “we built a chatbot” becomes the achievement. Remove “AI” from the sentence and ask what got better—time, mistakes, cost, or citizen outcomes.
- **Question**: If F1 on a small golden set is not enough, how should we set KPIs for an AI workflow at scale?\
  **Answer**: Start with “how much money will I lose?” Put a cost on each kind of error, then compare manual versus AI-assisted work on throughput and error rate. If the human still reviews the whole thing and quality is the same, the automation is only adding cost.
- **Question**: Any advice for selling AI when clients are at very different levels of maturity?\
  **Answer**: The range of buyer maturity is enormous and getting stretched: some are discovering basic Copilot capabilities while a small minority are already running autonomous agents. I need a much broader pitch, from correcting spelling mistakes to replacing whole workflows, because I don't know which buyer I am walking into.
- **Question**: Why give an agent a very general prompt instead of a specific one?\
  **Answer**: Be specific if you know what you want. I go general when I don't know what I want, think I know but am not sure, or may not know that I don't know; it stops me locking into the wrong answer too early.

## Mistakes I made

[Week ending 13 Sep 2026](https://www.s-anand.net/blog/mistakes-i-made/#week-ending-2026-09-13)

- I said **"No, only ours. IIT Madras has started offering it."**.\
  **Correction**: IIT Madras is not the only IIT offering an online undergraduate degree; IIT Guwahati has offered a fully online BSc (Hons) in Data Science & AI since 2023. [IIT Guwahati — Online Degree Programs](https://www.iitg.ac.in/oes/odp/) ([Indian Institute of Technology Guwahati](https://www.iitg.ac.in/oes/odp/))\
  **LOW · FALSE**
