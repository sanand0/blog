---
title: Retire the Verify Button
date: 2026-05-30T16:25:35+08:00
categories:
  - llms
description: I explain why manual verification of LLM outputs doesn't scale. Instead of 100% inspection, I apply manufacturing principles like statistical sampling, stratified risk management, and model-based augmentation to build quality directly into the production pipeline.
keywords: [statistical process control, w. edwards deming, llm evaluation, quality assurance, automated verification, sampling, model monitoring]
---

![](https://files.s-anand.net/images/2026-05-30-retire-the-verify-button.avif)

My post ["Add a Verify Button"](https://www.s-anand.net/blog/add-a-verify-button/) has a problem. When [Rohit](https://www.linkedin.com/in/rohitsaran/) requested hyperlocal news for every PIN code in Mumbai, we'd need a "verify" button on _every_ [Statoistics card](https://sanand0.github.io/journalists/statnostics/) - hundreds of PIN codes, _every day_.

Verifying every output introduces new bottleneck: a person inspecting every unit. **That's 100% inspection - which you do when you don't yet trust the process.**

Manufacturing solved this a century ago. At Western Electric's Hawthorne Works (famous for the [Hawthorne Effect](https://en.wikipedia.org/wiki/Hawthorne_effect)), quality control meant inspecting finished products and pulling the defective ones. [Walter Shewhart](https://en.wikipedia.org/wiki/Walter_A._Shewhart) sent his boss a [one-page memo](https://deming.org/the-first-control-chart/); about a third of it was a control chart.

![](https://deming.org/wp-content/uploads/2021/04/Screen-Shot-2021-04-18-at-7.30.33-PM.png)

[Deming](https://en.wikipedia.org/wiki/W._Edwards_Deming) turned this approach into his third point: *"Stop relying on inspection for quality."* Build quality in from the start instead of inspecting defects out at the end.

His process tells us what to do with a verify button as volume climbs.

- **Measure how often it's right.** Don't retire inspection until you know your defect rate. For example, on [one classification task I benchmarked](https://sanand0.github.io/llmevals/double-checking/), the average model error was about 14%. Until we know that number, "it's probably fine" is just a feeling.
- **Stratify.** "The garden has 18 plants" is easy to validate and low-risk if wrong. "This loan is denied" is neither. Verify the risky things carefully, let the cheap things through with low effort. Equal effort on both is waste.
- **Sample.** Nobody inspected every artillery shell in the war. Shewhart's Bell Labs colleagues [Harold Dodge](https://en.wikipedia.org/wiki/Harold_F._Dodge) and Harry Romig put sampling inspection on a statistical basis. Check a sample at known confidence; watch whether the process drifts. The equivalent: verify a random sample of cards, track the rate, and react when the rate moves, not when one card looks off.
- **Augment with other models.** When I [correlated two models' errors](https://sanand0.github.io/llmevals/double-checking/), the correlation was about 20%. If one gets a case wrong, the other usually doesn't miss the same one. So a second model is a cheap, imperfect inspector. Asking AI to generate verifiable output lets another model to spot obvious errors.

Also, it's best to avoid overreacting to defects. Deming called this (re-tuning the process after every defect) *tampering*. It makes the variation worse. It's worth collecting data and finding the real causes before changing the process.

That's what [Ankor](https://www.linkedin.com/in/ankorrai) calls the [future of verifiable autonomy](https://sanand0.github.io/talks/2026-03-18-verifiable-agents/). It starts with:

> we are going to have to move beyond testing correctness to standard testing… if we test the pipeline once before deployment, we can trust that every single output produced by that pipeline, unless we make any adjustment to it, can be trusted.

His analogy is software. Verification becomes a standard layer in the production loop, like how CI/CD is a standard step before you ship. Over a few years the need for human validation drops, and programmatic checks plus triage take over.

Regulated finance has a lot of experience with this. After the GFC, the Fed and OCC issued [SR 11-7](https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm) in April 2011. Every quantitative model going into production needs independent validation by people separate from the developers, plus ongoing monitoring, before it ships. "Retire the verify button" doesn't mean stop checking. **It means have an independent validation layer with an owner.**

Of course, this incurs cost - at scale. For us, it led to concerns from the Finance team that the token costs overhead was climbing up. But, to quote [KG](https://www.linkedin.com/in/srinivasankg/):

> Token cost cannot be overhead. Token cost is direct cost because you're replacing people.

So I now [benchmark cost alongside accuracy](https://sanand0.github.io/llmpricing/). A contract-validation demo I run checks a contract against a clause checklist, citing where each clause sits, for about 3 cents and 6 seconds. Pricing it lets me decide whether a reviewer's half-hour is worth more than 3 cents. Usually it is. Sometimes it isn't.

---

Sometimes, this isn't good enough. A client wanted PII scrubbed from 3 million user images with _zero_ leaks. I did the arithmetic out loud:

> with 99.9%, we're talking about 3,000 images with personally identifiable information potentially slipping through. Is that OK?

He said, "No." I told him we couldn't do it. It needs more technology than we had. (Our sales team nearly had a heart attack.) **A critical output of measuring is to check if it's even possible.**

---

I still manually verify AI output for new stuff. I don't trust every pipeline yet. But when the scale becomes unwieldy, this is the process I switch to.
