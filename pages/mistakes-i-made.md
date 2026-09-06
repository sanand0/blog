---
title: Mistakes I made
description: Factual claims I got wrong, overstated, or could not support, with corrections.
tags: [fact-checking, llms, ai-agents]
---

# Mistakes I made

What I got wrong, and what I should say instead. This excludes opinions, predictions, harmless approximations, and debatable claims.

## Week ending 06 Sep 2026 {#week-ending-2026-09-06}

- I said **"Skills ... ultimately it is just copy-pasting prompts."**\
  **Correction**: A simple skill can start as reusable instructions, but skills can package a workflow with instructions, examples, resources, schemas, tool access and code. Evidence: [OpenAI — Using skills](https://openai.com/academy/skills/?utm_source=chatgpt.com)\
  **HIGH · OVERSTATED**
- I said **fine-tuning "involves a lot of expertise, a lot of money, and it is a total waste of time."**\
  **Correction**: For this kind of tender/CV comparison I'd start with context engineering and evals. But "total waste" is too categorical: fine-tuning remains a supported way to adapt a model to a specific task. Evidence: [OpenAI — Fine-tuning](https://help.openai.com/en/articles/11162441?utm_source=chatgpt.com)\
  **HIGH · OVERSTATED**
- I said **"there is no extra cost to using voice" in ChatGPT and "when it talks back also, there's no token consumption."**\
  **Correction**: Voice is separately limited or metered depending on the plan. For example, Business includes limited Live usage and then charges credits per minute. I shouldn't call it free or unmetered. Evidence: [OpenAI — ChatGPT Voice](https://help.openai.com/en/articles/20001274?utm_source=chatgpt.com)\
  **MEDIUM · FALSE**
- I said **"Programs are very rarely wrong."**\
  **Correction**: Programs make calculations reproducible and easier to test; they do not make them correct. Wrong code, formulas, parsing, units or assumptions can produce reliably wrong results. Knight Capital's defective software deployment, for example, caused a $460M loss. Evidence: [SEC — Knight Capital software failure](https://www.sec.gov/newsroom/press-releases/2013-222?utm_source=chatgpt.com)\
  **MEDIUM · OVERSTATED**
- I called Henry Kissinger **"the American Ambassador."**\
  **Correction**: Kissinger was US National Security Adviser and Secretary of State, not an ambassador. Evidence: [US State Department — Henry Kissinger biography](https://history.state.gov/departmenthistory/people/kissinger-henry-a/bio?utm_source=chatgpt.com)\
  **LOW · FALSE**
- I said **about 3,000 IIT Madras BTech students graduate each year, compared with a BS intake of about 30,000.**\
  **Correction**: I mixed populations. IITM's 2025 convocation had 3,227 graduates overall, but 820 BTech graduates, or 1,132 including Dual Degree BTech. The BS program currently has 36,000+ students studying; the 30,000 figure is closer to historical applicant/enrollment-scale numbers than annual intake. Evidence: [IIT Madras — 2025 convocation degree breakup](https://www.iitm.ac.in/happenings/press-releases-and-coverages/iit-madras-62nd-convocation-witnesses-graduation-3227?utm_source=chatgpt.com) [IIT Madras — BS Data Science program](https://study.iitm.ac.in/ds/?utm_source=chatgpt.com)\
  **HIGH · FALSE**
- I said **the IITM BS "graduation is less than 10%, maybe."**\
  **Correction**: I don't have a defensible cohort-based graduation rate. The program has a qualifier process, flexible pacing and multiple exit points, so I need to define the cohort and denominator before quoting a percentage. Evidence: [IIT Madras — BS admissions and qualifier process](https://study.iitm.ac.in/ds/admissions.html?utm_source=chatgpt.com)\
  **MEDIUM · UNSUPPORTED**

## Week ending 30 Aug 2026 {#week-ending-2026-08-30}

- I said **Roger Federer "picked up tennis at the age of 20 or something."**\
  **Correction**: Federer began playing tennis at age 8. The point in _Range_ is that he sampled several sports and specialized later than Tiger Woods, not that he began tennis as an adult. Evidence: [ATP Tour — Roger Federer biography](https://www.atptour.com/en/players/roger-feder/f324/bio?utm_source=chatgpt.com)\
  **LOW · FALSE**
- I said **a $20 ChatGPT subscriber can use Pi with GPT-4o without API-token billing, and implied OpenAI subscription usage effectively doesn't rate-limit.**\
  **Correction**: Pi does support ChatGPT subscription OAuth, but specifically through its **ChatGPT Plus/Pro (Codex)** provider. Pi lists GPT-4o under the regular OpenAI API-key provider, and Codex subscription usage has plan limits. Evidence: [Pi — Providers](https://pi.dev/docs/latest/providers?utm_source=chatgpt.com) [Pi — GPT-4o model configuration](https://pi.dev/models/openai/gpt-4o?utm_source=chatgpt.com) [OpenAI — Using Codex with your ChatGPT plan](https://help.openai.com/en/articles/11369540?utm_source=chatgpt.com)\
  **MEDIUM · FALSE**
- I said **the IITM Web-Enabled M.Tech AI credential "is not yet accepted by PhD programs, even in India, let alone abroad."**\
  **Correction**: I don't have evidence for that blanket statement. IIT Madras formally awards the Web-Enabled M.Tech in AI, and IITM CSE's PhD eligibility accepts M.E./M.Tech degrees in AI, ML and related engineering areas. Other universities make their own admissions decisions. I should say the program is relatively new and its research/PhD outcomes are not yet well established. Evidence: [IIT Madras WSAI — Web-Enabled M.Tech in AI](https://wsai.iitm.ac.in/admissions/web-enabled-mtech/?utm_source=chatgpt.com) [IIT Madras CSE — PhD eligibility](https://www.cse.iitm.ac.in/admissions.php?utm_source=chatgpt.com)\
  **HIGH · UNSUPPORTED**
- I said **Indian tax residency for NRIs comes down to whether you were in India more than 120 days.**\
  **Correction**: The 120-day threshold is a special case, not the general rule. The normal tests include 182 days and 60+365 days; for an Indian citizen/PIO visiting India with more than ₹15 lakh of non-foreign income, 120+365 can apply. There is also a deemed-residency rule. Evidence: [Income Tax Department — Non-Resident FAQs](https://www.incometax.gov.in/iec/foportal/help/all-topics/e-filing-services/non%20resident%20-faq?utm_source=chatgpt.com)\
  **HIGH · OVERSTATED**

## Week ending 23 Aug 2026 {#week-ending-2026-08-23}

- I said **Claude Code auto mode made the risk of unintended actions "negligible," and later said "as of this month, it won't make a mistake" with a "90% chance" it would preserve undoability.**\
  **Correction**: I was far too confident and invented a probability I could not support. Agent safeguards are probabilistic. Anthropic's own auto-mode evaluation reported a 17% false-negative rate on real "overeager" dangerous actions. For destructive local operations I should still use backups/version control, limit permissions and retain review where the blast radius matters. Evidence: [Anthropic — How we built Claude Code auto mode](https://www.anthropic.com/engineering/claude-code-auto-mode?_bhlid=bb5b0c065a6a8790a89389462f16ab1ea5010c5e&utm_source=chatgpt.com)\
  **HIGH · OVERSTATED**
- I said **"there is no difference between Codex and ChatGPT Work" and that Work is essentially Code with a lighter, more marketable name.**\
  **Correction**: Work uses Codex technology, so the overlap is real, but they are distinct experiences. Work is aimed at longer multi-step research, analysis and deliverables; Codex remains specialized for software development and has separate workflows/history. Evidence: [OpenAI — Introducing ChatGPT Work](https://openai.com/index/chatgpt-for-your-most-ambitious-work/?_bhlid=b229619b8c31d33de07faa7f27a4a4f2202c57cd&utm_source=chatgpt.com) [OpenAI — ChatGPT Work and Codex](https://help.openai.com/en/articles/20001275/?utm_source=chatgpt.com)\
  **MEDIUM · OVERSTATED**
- I said **"1960s is when Studio Ghibli starts trying to catch up" with Disney.**\
  **Correction**: Studio Ghibli was established in 1985. Evidence: [Studio Ghibli — company history](https://www.ghibli.jp/profile/?utm_source=chatgpt.com)\
  **LOW · FALSE**
- I said **"I'm yet to find a use case where fine-tuning is worth it ... Zero. Out of thousands of use cases ... it was never worth it" and "in neither case is fine-tuning useful."**\
  **Correction**: "I haven't personally found an ROI-positive fine-tuning case yet" would have been defensible; "never useful" is not. Fine-tuning remains a standard adaptation technique even for open-weight models; Meta's official Llama cookbook includes fine-tuning and parameter-efficient fine-tuning recipes. Evidence: [Meta — official Llama Cookbook](https://github.com/meta-llama/llama-cookbook?utm_source=chatgpt.com) [Meta — Llama fine-tuning overview](https://github.com/meta-llama/llama-cookbook/blob/main/getting-started/finetuning/LLM_finetuning_overview.md?utm_source=chatgpt.com)\
  **HIGH · OVERSTATED**
- I referred to **"ChatGPT's share price" falling** if a privacy controversy were real.\
  **Correction**: OpenAI was not publicly traded, so there was no public ChatGPT/OpenAI share price to fall. I should have referred to OpenAI's private-market valuation, tender/share price, investor appetite or commercial impact. Evidence: [Reuters — OpenAI's planned IPO](https://www.reuters.com/business/openai-expects-go-public-within-next-year-information-reports-2026-06-10/?utm_source=chatgpt.com)\
  **MEDIUM · FALSE**
- I said **Meta's glasses can record someone "without you getting even an inkling or a notification."**\
  **Correction**: Meta's AI glasses have an outward-facing capture LED that blinks while photos or video are being captured; current models disable the camera if the LED is covered or disabled. The indicator may be easy to miss, but there is one. Evidence: [Meta — AI glasses privacy and capture LED](https://about.fb.com/news/2026/07/metas-ai-glasses-your-questions-answered/amp/?utm_source=chatgpt.com)\
  **MEDIUM · FALSE**
- I said **Alexa sends audio to Amazon only if you say "Alexa."**\
  **Correction**: The wake word is the normal trigger, but it is not an absolute rule. Follow-Up Mode allows requests without repeating the wake word, and Amazon says Alexa can sometimes mistake unrelated speech for a follow-up request. Evidence: [Amazon — Alexa Follow-Up Mode](https://digprjsurvey.amazon.com/csad/help/node/GX7EJ9WHEPYBV94J?utm_source=chatgpt.com) [Amazon — Alexa FAQs](https://digprjsurvey.amazon.com/csad/help/node/201602230?utm_source=chatgpt.com)\
  **MEDIUM · OVERSTATED**
- I said **"In India, most children are born on 1st June, which is the admission cutoff date for most schools."**\
  **Correction**: There is a real historical June-1 anomaly in **recorded** dates of birth in parts of India: when exact birth dates were unknown, some schools/parents used June 1 for admission records. That does not mean most Indian children are actually born on June 1, and the cutoff is not universal nationwide. Evidence: [Times of India — “Admit it, June 1 isn't your real b'day”](https://timesofindia.indiatimes.com/city/ahmedabad/admit-it-june-1-isnt-your-real-bday/articleshow/711643.cms?utm_source=chatgpt.com)\
  **LOW · OVERSTATED**

## Week ending 16 Aug 2026 {#week-ending-2026-08-16}

- I said **"The data is secure everywhere. All of them have solid enterprise contracts"** and that choosing an AI tool for company data was not really a technical question.\
  **Correction**: Enterprise AI offerings can have strong security, but their data handling is not interchangeable. It depends on the exact product, plan, tenant configuration, retention and training settings, connectors, geography and contract. Microsoft explicitly says Copilot controls vary by subscription; OpenAI and Anthropic make separate commitments for their business/commercial products. I should check the approved product and its actual controls rather than assume equivalence. Evidence: [Microsoft — Copilot enterprise data protection](https://learn.microsoft.com/en-us/microsoft-365/copilot/enterprise-data-protection) [OpenAI — Enterprise privacy](https://openai.com/enterprise-privacy/) [Anthropic — commercial-product training policy](https://privacy.anthropic.com/en/articles/7996868-is-my-data-used-for-model-training)\
  **HIGH · OVERSTATED**
- I said **GitHub is where you take version-controlled software and "save it publicly."**\
  **Correction**: GitHub repositories can be public or private; GitHub Enterprise also supports internal repositories. Version control does not imply publishing the code. When explaining this to a beginner, I should explicitly distinguish Git from GitHub and repository visibility. Evidence: [GitHub Docs — About repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories)\
  **LOW · FALSE**
- I said **animation "started" in the 1930s with *Snow White and the Seven Dwarfs*.**\
  **Correction**: *Snow White* was a landmark, but animated features predate it. *El Apóstol* was released in 1917, and *The Adventures of Prince Achmed* from 1926 is the earliest surviving animated feature. My visualization was a filtered view of popular IMDb titles, not a history of when animation began. Evidence: [BFI — animated features before Snow White](https://www.bfi.org.uk/features/lesser-spotted-british-animated-feature-film)\
  **LOW · FALSE**

## Week ending 09 Aug 2026 {#week-ending-2026-08-09}

- I described the MoSPI telecom results as applying to **youth aged 14–24** and referred to **Daman and Diu** as the geography.\
  **Correction**: The CMS: Telecom 2025 tables use the age group **15–24**, not 14–24. The official State/UT geography is **Dadra & Nagar Haveli and Daman & Diu**. When quoting striking subgroup percentages, I should preserve the source's exact denominator and geography. Evidence: [MoSPI — NSS Report No. 593: CMS Telecom, 2025](https://www.mospi.gov.in/sites/default/files/publication_reports/CMST_report_m.pdf)\
  **LOW · FALSE**
- I said **agents "don't hallucinate, not anymore."**\
  **Correction**: Hallucinations have fallen substantially in newer models, especially when they can search, use tools and verify, but they have not disappeared. OpenAI still explicitly evaluates hallucination rates and warns that ChatGPT can confidently produce incorrect or misleading outputs. Evidence: [OpenAI — Does ChatGPT tell the truth?](https://help.openai.com/en/articles/8313428-accuracy-and-reliability) [OpenAI — GPT-5.6 System Card](https://deploymentsafety.openai.com/gpt-5-6)\
  **HIGH · OVERSTATED**
- I said **"GPT-4o-mini is both better and cheaper" than GPT-4o** and suggested simply switching.\
  **Correction**: GPT-4o mini was much cheaper, but it was not simply a more capable GPT-4o. Model quality depends on the task. OpenAI's own evaluations, for example, showed GPT-4o substantially more accurate and less hallucinatory than GPT-4o mini on SimpleQA and PersonQA. The right advice is to switch an old expensive model only after benchmarking the cheaper candidate on the actual workload. Evidence: [OpenAI — o1 System Card, Table 3](https://cdn.openai.com/o1-system-card-20241205.pdf)\
  **MEDIUM · OVERSTATED**

## Week ending 02 Aug 2026 {#week-ending-2026-08-02}

- I said **"The organization is virtual, but the data is perfectly representative. What difference does it make whether you're running it in Company A or Company B?"**\
  **Correction**: Synthetic data can be useful for prototypes, simulations and controlled experiments, but I cannot call it perfectly representative without validating it against the real population and workflow. It can miss distributions, correlations, edge cases and organizational context that matter in production. NIST explicitly warns that synthetic datasets cannot simply be assumed to represent real-world data. Evidence: NIST — Best Practices in the Collection and Use of Biometric and Forensic Datasets.\
  **HIGH · OVERSTATED**
- I called **repeatedly generating code, running tests and asking AI to try again "a reinforcement learning cycle."**\
  **Correction**: That is an iterative generation/evaluation or search loop, not reinforcement learning by itself. Reinforcement learning trains a policy/model from reward signals; for example, OpenAI's reinforcement fine-tuning generates rollouts, grades them and applies weight updates. Re-prompting the same model after seeing a test result does not update its weights. Evidence: OpenAI — Reinforcement Fine-Tuning.\
  **MEDIUM · FALSE**
- I said **"any theorem that you can write in Lean, you can prove or disprove just by brute force."**\
  **Correction**: Lean lets us formalize statements and mechanically check proofs. It has automation and decision procedures for some classes of propositions, but formalizing a theorem does not make it automatically or brute-force decidable. Lean's own documentation distinguishes decidable propositions from general theorem proving, and interactive proofs can require substantial human or automated guidance. Evidence: Lean — Decidable Propositions; Lean — proof-assistant design.\
  **MEDIUM · FALSE**
- I said **ChatGPT gives roughly three times as many tokens as Claude and "Nobody will be able to" exhaust its quota.**\
  **Correction**: That extrapolated too much from my own usage. ChatGPT allowances depend on the plan, model and workload. Business explicitly has per-seat limits, and Work/Codex allowances can be exhausted; after that, additional usage needs workspace credits or a reset. I also shouldn't claim a universal 3x token advantage without comparing the actual Claude and ChatGPT plans and workloads involved. Evidence: OpenAI — ChatGPT Business models and limits; Using Codex with your ChatGPT plan.\
  **MEDIUM · OVERSTATED**
- I said **AI logs "will have an expiry of something like one month" and that "most providers will delete old logs automatically."**\
  **Correction**: Log retention is provider- and configuration-specific. In the Azure environment we were discussing, Log Analytics defaults many tables to 30 days, but analytics retention can be extended to two years and total retention to 12 years. Backups may still be sensible, but I should inspect and configure the actual retention policy rather than assume a one-month expiry. Evidence: Microsoft — Manage data retention in Log Analytics.\
  **MEDIUM · OVERSTATED**
- I said **"If I'm in India for more than 120 days in a year, the taxation is different."**\
  **Correction**: The 120-day threshold is only a special case, not the general NRI residency rule. For an Indian citizen/PIO visiting India, 182 days normally applies; if non-foreign income exceeds ₹15 lakh, the alternate 120-day test also requires 365+ days in India over the preceding four years. There is also a separate deemed-residency provision. Evidence: Income Tax Department — Non-Resident Individual rules.\
  **HIGH · OVERSTATED**
