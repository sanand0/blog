---
title: Where Enterprise AI is headed
date: 2026-05-23T08:24:19+08:00
categories:
- llms
- how-i-do-things
description: I used ChatGPT and Claude to mine six months of transcripts for podcast answers, then edited the result. It argues enterprise AI succeeds through delivery, telemetry, knowledge infrastructure, governance, and human accountability.
tags: [forecasting, enterprise-ai, ai-adoption]
---

![](https://files.s-anand.net/images/2026-05-23-where-enterprise-ai-is-headed.avif)

A podcast host sent me eight questions. Instead of rehearsing answers in my head, I used ChatGPT with [Local MCP](https://www.s-anand.net/blog/local-mcp/) to read 6 months of call transcripts and find the best examples: <!-- https://chatgpt.com/c/6a10e52f-155c-83ec-9930-e61350c5a72b -->

1. **Iteration 1**: Here are questions I have been asked to answer in a podcast. Help me prepare with examples. For each question, go through my transcripts or emails and find examples relevant to the question and share (for each relevant example) a summary, how it's relevant, and the relevant verbatim quotes from the transcript.
2. **Iteration 2**: Mention WHO said it. _Emphasize_ the most important parts. Do a second pass. More examples. Disprove your own hypotheses with evidence to the contrary and retain what remains robust.
3. **Iteration 3**: Do a third pass. Find more real-life examples. Try and disprove yourself even harder. Share the best examples for what survives - not all. Same format.
4. **Iteration 4**: Ensure diversity of client examples. For example, in Q2, all three are the same client. Extend to add / replace examples - ideally with better ones.

Then I used Claude with examples of my writing style to summarize it in my voice. <!-- https://claude.ai/chat/87554c18-0cb5-4667-9ef7-584a310f17fb -->

For the first time, I'm happy to publish an AI-written blog post, because it is:

- **Unique to me**. No one else has my transcripts, and I'm in an unusual position: enterprises keep calling me with AI problems.
- **More than me**. Step #1 takes hours of research. Step #2 takes an hour of patience. I would not do this without AI.
- **Not unlike me**. I would have written it _slightly_ differently. Better in some ways, worse in others, but it's close to my style.

Given how comfortable I am about this, I plan to be - not just an author, but also - a editor of AI generating from _my_ content.

This article uses verbatim transcripts where possible. I've anonymized clients and most colleagues. I've annotated the post with (**Anand**: ...) commenting with my understanding.

<section ai-disclosure="ai-generated" data-ai-model="claude-sonnet-4.6" data-ai-provider="Anthropic">

## 1. So what is Straive, and what do I do there?

I'll let [Namit](https://www.linkedin.com/in/namit-sureka-43ab89/) explain it. He said this two weeks ago in a pitch to a European credit-insurance client:

> The focus for [Straive](https://www.straive.com/) is helping its clients _operationalize AI_. For that, we bring two apparently distinct capabilities together... _data analytics and tech development_... and _large-scale operations_. Where we come in is _bringing these together and bridging the gap_.

That's the company. We have about 8,000 people in India - Bangalore, Hyderabad, Chennai, Gurgaon, Noida, Mumbai, Kolkata, Pune. (**Anand**: Globally it's probably 18K.)

My job is innovation. In the same call, I described it as:

> I lead innovation at Straive. Most of my work involves playing around with _Large Language Models_, trying to see how they can _accelerate our client work_ as well as deliver _new kinds of solutions_. That includes _improving the software development life cycle_.

I introduce myself as an [LLM psychologist](https://www.s-anand.net/blog/the-llm-psychologist/) when nobody's watching for corporate decorum. Half of my week is demos for clients. The other half is figuring out why those demos haven't reached production yet. (More on that in question 2.)

## 2. Why do so many enterprise AI pilots stall?

Not for one reason. I keep a mental list of stall patterns. Three of them come up almost every week.

**Pattern 1: The pilot worked, but nobody is delivering it.**

In a sync with Namit a few months ago, I caught myself saying:

> At a global media client, I am a little worried that _the engagement keeps growing and we haven't delivered anything yet_... Right now, we've been given _proposal after proposal after proposal_... _Nothing has gone to getting deployed so that someone other than our team can use it._

Namit's reply was a single, useful sentence: "But they are _not in the execution phase_?" That was the gap. We had impressive demos. We had no delivery owner.

**Pattern 2: The data can't move.**

For a global premium-schools group, the on-site data lead told me:

> This is the data set that is at the most granular level. There are around _400,000 rows_... and around _110 columns_... They cannot export it... we cannot export this outside externally.

The pilot didn't fail. The architecture failed. We had to redesign the entire engagement around the constraint: schema, profiling stats, sample rows, hypotheses, and queries flow out; raw data stays in. (Knowledge infrastructure as a workaround for missing data infrastructure. See question 4.)

**Pattern 3: Teams debate frameworks instead of evals.**

A private-markets investor wanted to lock the "agentic framework" by end of week. Their team was comparing LangGraph vs OpenAI Agent SDK vs Pydantic AI. I told them, more bluntly than I should have:

> The technical solution may not matter too much because this is moving so fast that _anything we built will anyway be outdated in not more than a year_... It almost doesn't matter which of these... _the effort on the code is the least of our problems_.

Pilots stall there too - not because the framework is wrong, but because the question is wrong. Without evals and acceptance criteria, no framework choice will rescue the project.

**The thing that survives all three patterns**: pilots prove that a model can produce a good answer once. Production proves the operating model.

## 3. What operational gaps stop AI from scaling?

Telemetry. Objective clarity. Repeatable loops. In that order.

**Telemetry, not surveys.** Our L&D lead asked me how to assess AI readiness across 19,000 employees without sounding like a particular Big Consulting firm threatening people's promotions. I suggested:

> I would go to the IT team and ask them for three things... using NetSkope, who has been accessing AI-related sites on _how many unique days in the past 90 days_... _Regularity matters more than volume_... LLM Foundry access. They have the logs for that. Third, Google Workspace tracks Gemini usage... _These three give us a good company-wide proxy for AI usage_.

He paused, then said it was better than a survey. **You cannot scale AI adoption without knowing who is adopting it.** Self-reports won't tell you. Logs will.

**Objective clarity beats agent architecture.** (**Anand**: KISS: Keep it simple & stupid.) A teaching assistant in my IIT Madras course built an elaborate agentic workflow tool - planner agents, executor agents, sub-agents reporting to leaders. After fifteen minutes, I said:

> You've been speaking for 15 minutes and _I haven't understood what you want. I don't know if you understood what you want_... You mentioned two objectives: _learning traces and helping students learn. We should keep those as two different tools_... For the learning traces, the _minimal solution is a terminal command_. It should authenticate them with their Google account and log all the inputs and the outputs, save it in a signed document that is tamper-proof, that we can replay.

200 lines of Python, not a multi-agent framework. (He took it well, I think.) The operational gap was: nobody had separated the two objectives, so every solution looked too complex.

**Repeatable loops beat heroics.** (**Anand**: Iterate. Compound improvement.) An internal team complained they couldn't ship because the developers were on other work. I told them:

> You can try. _Don't worry about what is not working. Just write it down._ I tried this, this is working this way, this is not working in this way.

The gap wasn't developer capacity. It was the absence of a "try, document, learn, repeat" loop that anyone could run.

## 4. Why does content and knowledge infrastructure matter as much as cloud?

Because the model is generic. Your business meaning is not. (**Anand**: Each company has their own ways of working.)

A delivery lead working at the global premium-schools client kept hitting the same wall. The bottleneck wasn't access. It was semantics:

> The real bottleneck is not access; it's _shared semantics_: 'Acceptance date,' 'account ID,' 'boarding type,' 'inquiry journey' - these can mean subtly different things across systems.

That is knowledge infrastructure. Definitions. Update rules. What "acceptance date" means when a stage is updated vs appended. No model knows this until you write it down.

**At the European credit-insurance pitch, we made this explicit.** A senior delivery architect on our side told the client:

> We create a _Confluence setup_, bring in everything that's not already there on Confluence and create a comprehensive Confluence setup... That becomes the input for our _agentic implementations_ as well. That becomes the _data room_ from where the agents draw the knowledge to perform the actions.

The Confluence wasn't the deliverable. It was the substrate that made every later agent deliverable possible.

**On a CPG analytics product demo**, the founder explained their "definition library":

> This is where we're configuring the _DNA of the agents_... We call the _domain definitions_. We also call it the _definition library_... It's not just a wrapper around ChatGPT. It's something that's very grounded in _domain-specific definitions_ that avoids _hallucinations, non-deterministic output_.

I keep coming back to this. **Cloud is where the model runs. Knowledge infrastructure is what the model knows.** Skip the second, and you have a very expensive autocomplete.

## 5. What do India-led capability centers add?

They convert AI demos into reliable processes. That's not a slogan. It's the only thing that actually scales. (**Anand**: You need people to operate the AI machinery.)

**On the European credit-insurance engagement**, the client's IT lead described his Bangalore team. [Jishnu](https://www.linkedin.com/in/jishnu-gupta-1a3a29/)'s response was telling:

> We also want to absolutely be open and also _retain some of that knowledge_, because as we transition, those will be critical, the knowledge that is inherent in your people and processes.

The center isn't a labor pool. It's a knowledge sink. Without that retention, AI workflows lose context within months.

**Better example**: a media-intelligence client picked us because our AI model scored higher than theirs and higher than humans. The numbers were:

- Their model: 40% accuracy
- Their human reviewers: 65% accuracy
- Our model: 70% accuracy

But 30% of cases were still outliers. So we set up an operations team in India to handle those exceptions. AI plus humans, with the humans owning the exception path. We now have about 150 people doing similar work for a global short-video platform out of Hyderabad and Chennai. (**Anand**: This is a claim I heard in a pitch. I don't have evidence. So, if it's untrue, it's human hallunication, not AI.)

**Closer to my own work**: we have a Hyderabad team that trains coding models. (**Anand**: Actually, we don't. [Rukesh](https://www.linkedin.com/in/rukeshreddy/) of [Deccan.ai](https://www.deccan.ai/) does. This is AI hallucination.) About 100 full-time reviewers and 200-300 contractors. The full-timers don't build models - they look at code and rate it, "I like this, this is not so good." They're managing reviewers, not writing code. That's a capability center evolving from delivery to AI ops.

The thing that distinguishes India-led centers in 2026 isn't cost. It's the willingness to own the 30% that AI can't handle yet.

## 6. Where does governance actually bite?

Three places, all real, all from the last quarter.

**Compute-to-data, not data-to-cloud.** (**Anand**: Move code, not data.) Back to the global premium-schools client. The data could not leave. So the governance pattern became:

> If you could share back the _output aggregated_ of those queries, that will be great... Get the magnitude and the P-value. Which you can _dictate over a call if required_.

We export queries and import aggregated results. The schema travels; the rows don't. **"No export" turned out to be a product requirement, not a blocker.**

**Honest impossibility.** A global media client wanted us to scrub PII from 3 million user-uploaded images. Their senior engineering leader insisted on zero leaks. I did the math out loud:

> For 3 million images... with... 99%, we're talking about _30,000 images_ with personally identifiable information potentially slipping through.

He replied, flatly: "We have to have _zero leaks_. Not thousands of leaks." I said: "Then I think I can safely say _we can't do this_. This requires more technology than we have." (**Anand**: When I said this, our sales teams nearly had a heart attack. So did the client, I think.)

Trustworthy AI sometimes means saying no. That was a governance decision, not a technical one.

**Local execution for sensitive data.** At a clinical-data conference, I used our own finance controller (a famously cautious Chennaiite) as an example. He emailed his team:

> Team, please use this opportunity to install CodeX AI as per the recorded demo. This is very powerful, yesterday I tried it for two data requests and the result was _fantabulous_.

The reason he was comfortable: _the data is not going to the model. The code is coming from the model._ Codex ran the code on his machine, on the financial records, which never left his laptop. (**Anand**: Well, kind-of. _Some_ data does leave, like summaries, previews, etc.)

**Three governance patterns, three different problems.** None of them is policy text. All of them are architecture decisions.

## 7. How should we measure real ROI?

Cycle time. Quality. New revenue. Risk avoided. Adoption. Not headcount.

**Cycle time, hard number**: on the European credit-insurance engagement, our sales lead told the client:

> We brought in an _AI-based approach solution_ to accelerate that entire mapping exercise... reduced the execution time by about 80%.

That's the easiest ROI to defend. It was an actual XSLT and data-mapping workstream, not a demo.

**Quality and effort, blended**: in a workshop with our research analytics team, an analyst said a CIM (Confidential Information Memorandum) takes:

> _Three to four man-day effort._ A man-day is equivalent to eight hours.

I did the demo live:

> In approximately _five minutes_, Claude will come up with a pretty solid presentation. In approximately _45 minutes_... ChatGPT will come up with an outrageously detailed presentation... Those _three to four days will come down by 50%_.

The half-day saving counts. The "five minutes vs three days" headline doesn't, because review still takes time. **Honest ROI includes the verification effort.**

**Revenue, not just cost**: one of our innovation track leads told the team:

> This was the demo that we made and that resulted into these _two projects_, both Sports Coverage and Trends to Clip.

That demo turned into part of a $1.15M week of deal movement. Demos that drive pipeline are an ROI line item too, even though no spreadsheet ever credits them. (**Anand**: This was reported in an internal sales call I was not a part of, but is true.)

**The fourth measurement is adoption.** If nobody uses the thing, the ROI is zero regardless of theoretical capability. Track NetSkope logs, not certificate completions. (See question 3.)

## 8. Where is enterprise AI going?

Three predictions, ranked by how confident I am.

**Most confident: analysts stop doing research; they start managing AI researchers.** I told a research analytics workshop:

> _Stop doing research._ Your job has now transformed into somebody who has a _team of 100 researchers under you_... Your job is no longer managing a team; it is in fact _managing a team of teams_, perhaps.

The implication is real. Hiring shifts toward verification, judgment, and exception-handling. The org chart compresses but the supervisory layer grows. Accountability becomes the scarce skill.

**Reasonably confident: agentic frameworks will commoditize within a year.** Back to the private-markets investor sync. I told them not to obsess about LangGraph vs Pydantic AI vs OpenAI's SDK:

> Workflows are where you say, _'do it this way.'_ Agents are where you say, _'figure it out.'_... A scalable approach is to give it an _agentic loop_, say, _'you figure out how to solve the problem.'_

The frameworks won't matter. The loops, tools, and evals will. **Pick something boring and move on.**

**Less confident, but worth saying: nobody jumps straight to autonomous.** Even our most ambitious proposal - the European credit-insurance one - staged it explicitly:

> The _Agentic AI component_ is something which is more prominent and starts in the _Modernize phase_. But it's not there in phase one and phase two. However, _AI is still there_... We are going to leverage AI or LLMs for very basic functionality in a _non-intrusive manner_.

Assist first. Instrument. Capture knowledge. Then automate more deeply. The companies that try to skip to step four lose three quarters re-doing step one.

## What survived three passes through my transcripts

I rebuilt this answer three times. Each time I tried to disprove my own pattern. Each time the same shape held:

**Enterprise AI does not fail because the model is weak.** It fails when we mistake a demo for delivery. When data can't move. When teams debate frameworks before defining evals. When the team overbuilds because nobody asked what the actual objective was. When the business case never cleared cost and timeline.

The pattern that survives across clients, sectors, geographies: **successful enterprise AI is operational AI**. It needs telemetry, knowledge infrastructure, governance, human accountability, and a delivery model. Not slogans, not frameworks. Logs. Schemas. Confluence pages. Codex on a controller's laptop. A 200-line terminal recorder instead of a 10,000-line agentic platform.

That's what we sell at Straive. That's what I'm trying to scale. Ask me again in a year.

</section>
