---
title: Things I Learned - 09 Aug 2026
date: 2026-08-09T00:00:00+00:00
categories:
- til
description: 'I learned that reliable agents need explicit exit criteria, drift correction, narrow permissions, and benchmarks. AI adoption is also jagged: many organizations still limit users to weaker tools and capabilities.'
tags: [ai-agents, ai-adoption, verification]
---

This week, I learned:

- Kamakoti: "Entry (to the course) is relatively easy but the exit is extremely hard". Generalizing, quality is determined by the exit criteria; loosening entry criteria is just openness / diversity. [The Hindu](https://www.thehindu.com/news/national/tamil-nadu/iit-madras-launches-online-bs-course-on-management-and-data-science/article70659825.ece) <!-- https://gemini.google.com/app/b5c95aa16c056bb9 -->
- "Once I have a persistent system that I pay to keep thinking, learning, and acting 24/7, I think that will decisively look like AGI." - [Dan Shipper](https://every.to/p/after-automation)
- AI has expert-level capabilities in many (increasing) tasks #ForNow. If your edge is OUTSIDE of those, use AI for other tasks you couldn't do before, insourcing or expanding horizontally. But your edge may be short-term - so move upstream / specialize. Your competitors' edge may be short-term, too - so plan to attack. <!-- https://chatgpt.com/c/6a770801-7234-83ec-8f0f-63460e93edb1 -->
- Analyzing [Anthropic Economic Survey](https://huggingface.co/datasets/Anthropic/EconomicIndex/tree/main), it looks like people in rich countries are asking Claude for _advice_ (explain this spreadsheet) while poor countries are asking Claude for _output_ (build this website) #ForNow. Maybe because rich users already have tools / people that create output for them? <!-- https://chatgpt.com/c/6a6f3195-fa08-83ec-8f8c-3443da3a29f9 -->
- Humans can't define all laws of language but LLMs have learnt them anyway. What if there are laws of nature that humans can't understand but AI can? Actually, this is already true of black-box models (loan approvals, weather forecasts, ...) where benefit/control > understanding. But as data & compute scales, this might "solve" entire fields like psychology, economics, etc. [Noah Smith](https://www.noahpinion.blog/p/the-third-magic-23f)
- In each area, there might be a limit to how much intelligence is possible/useful. For example, we're pretty good at recognizing food and emotions - there's not much benefit / possibility of more intelligence. But we can copy and share this intelligence - and that might help more than we think. [Noah Smith](https://www.noahpinion.blog/p/what-will-more-intelligence-actually)
- The ChatGPT Dropbox plugin can read Markdown files if you specify the path, but can only read PDF, Word, PPTX, Excel, etc. when searching. It cannot update files on Dropbox, but can add and delete. #ForNow <!-- https://chatgpt.com/c/6a76ecca-a794-83ec-8f57-f59896963abb -->
- Given how long agents run without mistakes, verification is increasingly "drift correction". You can't spot it easily. Learn writing specs that EXPOSE drift. Build and test against "oracles" (verification systems). Reduce cost of error. <!-- https://claude.ai/chat/9950d3e9-ed70-45c5-9bfa-da85798385de -->
- Permissions, in the context of multiple agents, is complex. If agent A can read my email but wants to consult agent B, can B see the email? We'd need to make permissions pretty specific, like:
  - principal: "anand"
  - agent: "agent-17"
  - purpose: "insurance-coverage-check"
  - allowed_data: ["email:read", "dropbox/notes:read"]
  - allowed_effects: ["email:send"]
  - audience: ["anand"]
  - expires_at: "..."
  - delegation_depth: 1
- After struggling to understand where to apply loop engineering, here's my guess. If you have a metric (or something really well defined) that you want to optimize, and a single agent iteration isn't enough, loops are a way to get there. Kaggle competitions, benchmark optimizations, etc. are examples. This means that any complex system that you can benchmark (or at least where you can robustly compare results) is loop engineerable. (This means that the ability to benchmark, and using agents to benchmark, will become a key ability.)
- Ontologies, state machines, etc. can be used to create verifiable systems, e.g. nodes become states, relations are valid operations. That's great for building verifiable systems (leading to things like LEAN). Of course, a key skill will be knowing what to put into the state, what relations to allow/disallow, what reflects reality well, how it might evolve (e.g. temporal graphs), how that might change in the future, etc.
  - Having said that, this is just creating a neural network of sorts - so according to the bitter lesson, we should just toss data at an agent and have it build a graph (or not) as required. BTW, I shared this with a bunch of speakers at Data Hack Summit who were speaking about knowledge graphs. There was silence for a while. Then, gently, they all agreed.
- Some people blab. Interrupting with a question is a good diversion mechanism. Some blab even after that. Exiting politely is both wise and surprisingly un-rude.
- To control your mental state, breathe slowly. 5–6 times/min for five minutes (that's longer than I thought was needed), exhaling slower than you inhale. [PubMed](https://pubmed.ncbi.nlm.nih.gov/35623448/)
- Once a ChatGPT conversation uses a developer plugin, #ForNow it refuses to use other plugins. So, if you need to use a GMail plugin AND a plugin you built yourself, you'd need to use the GMail plugin first, get stuff into the chat, then switch over to yours. I suspect conversations with developer plugins might not be accessible when using other plugins, too - but that's untested.
- There's a jagged edge of AI adoption as well, not just AI capability. Several organizations limit users to weaker agents #ForNow (e.g. only Microsoft Copilot or Gemini). Many have never seen the power of Codex or Claude Code on their systems. It's hard to convince them that AI can do much more than they think.
- There's a "data engineering" industry incentivized by structuring data. This is partly enabled by poor enterprise agent adoption #ForNow (e.g. Microsoft Copilot). The sequence works like this: "AI does not solve something with the data it's given. Let's structure the data. It solves it. Therefore, we need to structure data - all data." The alternative which I believe is: agents will structure it themselves.
- I noticed that when you submit a prompt on ChatGPT, it changes the URL to `https://chatgpt.com/c/WEB:...` and once it starts processing it on the server, changes it to `https://chatgpt.com/c/...` giving it the actual conversation. So, if you see a `WEB:` in the URL #ForNow, make sure you _copy the prompt_ before reloading the page - because it hasn't been saved or sent to the server.
- I assumed inflammation was mostly a bio/chemical process. Looks like neural signals are involved, too, and electrical simulation can control inflammation. This leads us to a new territory: bio-electrical medicine.
- The [Anthropic Economic Index](https://www.anthropic.com/research/economic-index-june-2026-report) indicates that, on average, if you prompt Claude like an 8th grader, it responds for a 9th grader. Does that mean (a) that more sophisticated prompts get a better response, and (b) if you repeatedly meta-prompt, you increase the sophistication by about a year each iteration, and hence can get very smart prompts by just getting out of the way and with little hope of understanding the question? This might actually make sense if AI will action the result without you needing to understand.
- The geometric mean is always less than or equal to the arithmetic mean. This is why a "smooth" 8% return is worth much more than a "wild" 8% return. [@lumenxbt](https://x.com/i/status/2082101954206130402)
- Quantum cryptography can give us unclonable encryption, i.e. if someone copies a message midway (or you publish it), you can't independently decrypt both. We knew how to do this in 2020. Now, ChatGPT helped "indistinguishable security". Between 2 messages, people can't figure out (e.g. from the length, or other attributes) which message is which. [Gemini](https://share.gemini.google/2Ci7ZKRLHBHk)
- Agents can record network requests into a HAR file and reverse-engineer an API for many websites. More efficient than browser control. [dax](https://x.com/thdxr/status/2078727284865827140)
- The [Anthropic Economic Index](https://www.anthropic.com/economic-index) dataset is on [Hugging Face](https://huggingface.co/datasets/Anthropic/EconomicIndex/tree/main) - released quarterly #ForNow. The longitudinal analysis is likely to be interesting.
- [BusinessCaseBench](https://business-ai-benchmark.github.io/) solved over 238 business cases with AI agents and they're doing well and improving #ForNow. Not surprising. [Frontier AI performance across the business disciplines](https://arxiv.org/pdf/2607.16057v2)
- [OpenAI Presence](https://openai.com/index/introducing-openai-presence/) shows a pathway for deploying agents. Deploy for a **specific job**, with **only required access** to knowledge and systems, company defined **policies** for approval, agent periodically **reviews logs** & escalations and **proposes updates** for testing and approval.
- A lot of work people are doing on ChatGPT is OUTSIDE their area of work. "... a substantial part of work-related ChatGPT use is from users expanding their role." [OpenAI](https://openai.com/index/how-ai-is-expanding-what-people-do-at-work/)

## Questions I was asked

[Week ending 09 Aug 2026](https://www.s-anand.net/blog/questions-i-am-asked/#week-ending-2026-08-09)

- **Question**: Is this (Email AI with LocalMCP plugin) just search on steroids?\
  **Answer**: Yes. Search on steroids is not a bad mental model. The deeper capability is the ability to loop like crazy - keep hitting a problem with tools until it actually gets solved.
- **Question**: How do you build enough trust to let agents take multiple steps without constant approval?\
  **Answer**: Don't try to convert everyone. Leave the early adopters alone; show the middle working examples and let them try carefully. When the middle moves, the rest will catch up themselves.
- **Question**: If AI accelerators become outdated in two weeks, how do you keep up?\
  **Answer**: Build accelerators for accelerators. Instead of investing in a benchmark, build a benchmark-builder from production logs; leapfrog one step and plan for agents to automate today's specification and verification work.
- **Question**: How do we govern all the AI apps employees are creating?\
  **Answer**: First ask, "Does this need governing?" Personal use: do whatever you want. Shared apps: review them. Don't say, "You cannot do X unless it is governed."
- **Question**: Where do you stand on "code with AI, code without review"?\
  **Answer**: Usually review it, with AI helping find problems. But for throwaway code, or code agents write for themselves, or incidental to a business output you can verify, validate the outcome instead.
