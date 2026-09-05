---
title: How I Verify And Delegate to AI
date: 2026-09-05T12:00:58+08:00
categories:
    - llms
    - how-i-do-things
description: I turned a data storytelling keynote into a survey of what stops people from using AI. Then I mined my August chat logs for my verification and delegation techniques.
tags: [verification, ai-agents, data-analysis]
---

I delivered a [15-minute keynote](https://talks.s-anand.net/2026-09-03-convergence-jio-institute/) at [Jio Institute's Convergence 2026](https://www.jioinstitute.edu.in/convergence-2026) at NTU on Thursday.

The topic was "Data Storytelling" - a bit jarring in the middle of an AI event. [Shailesh](https://www.linkedin.com/in/shaileshk/) picked it and I just rolled with it. A spent several days worrying, "How the heck do I say about data storytelling, when most of my [recent](https://talks.s-anand.net/2026-08-12-iitm-ed-data-visualization/) [workshops](https://talks.s-anand.net/2026-07-04-vizchitra-dialog-curators-dilemma/) and [talks](https://talks.s-anand.net/2025-08-21-rip-data-scientists/) are about the death of my data storytelling approaches?"

After a [discussion with ChatGPT and Claude](https://github.com/sanand0/talks/blob/70fa71b5ad1c7d55131ba3e8467e5833e45ae03d/2026-09-03-convergence-jio-institute/chat-talk-topics.md#user-2), I settled my usual strategy these days:

1. Agents know more than me anyway, so I don't see what value I add.
2. So instead, I'll **survey** the audience and share insights. That survey data is new.

I had [ChatGPT analyze the audience and create the survey](https://github.com/sanand0/talks/blob/70fa71b5ad1c7d55131ba3e8467e5833e45ae03d/2026-09-03-convergence-jio-institute/chat-audience-profile.md), even implement it using [`gws`](https://github.com/googleworkspace/cli) (didn't know it could do that!) and had it [analyze the results](https://github.com/sanand0/talks/blob/main/2026-09-03-convergence-jio-institute/chat-hypotheses-visualizations.md).

<div style="width: 100vw; margin-left: calc(50% - 50vw); width: min(100vw, 100rem); margin-left: calc(50% - min(50vw, 50rem)); margin-top: 1.5rem; margin-bottom: 2rem;">
  <iframe src="https://talks.s-anand.net/2026-09-03-convergence-jio-institute/survey.html" title="Jio Institute Convergence 2026 Survey Results" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" style="display: block; width: 100%; height: 820px; height: min(56rem, 92svh); border: 0; background: #f5f1e6;"></iframe>
</div>


Two [survey results](https://talks.s-anand.net/2026-09-03-convergence-jio-institute/survey.html) were striking.

(**ASIDE**: it took a few _painstaking_ hours _and_ [last minute panic](https://www.s-anand.net/blog/speaking-unprepared/) to pick the two. There were _several_ insights. Maybe some othere were more important. I just _happened_ to choose these.)

1. _What mainly stops you from handing that task over to AI today?_\
   **Top answer**: ["I'd have to check it anyway"](https://talks.s-anand.net/2026-09-03-convergence-jio-institute/survey.html#b2). In other words, **verification**.
2. _Imagine AI became 10× more reliable and could securely access all your work systems. What part of your work would you still want to keep for yourself?_\
   **Top answer**: [The final judgement call](https://talks.s-anand.net/2026-09-03-convergence-jio-institute/survey.html#b5-s1). In other words, **delegation**.

Which got me to do think: How do _I actually_ verify and delegate? The lightbulb 💡 moment was realizing that I could actually find this out from my _own_ data.

So, on the [bus ride](https://maps.app.goo.gl/rjrR6vqecJk9efpk7), I asked ChatGPT:

1. **How do I verify AI's work?**
   - Go through our chats in August 2026.
   - Find all techniques I used to verify / make it easy for me to verify the output.
   - Factor in their effectiveness.
   - Share as a prioritized list with examples
2. **How do I delegate to AI?**
   - (... same thing)

[Here are my top verification techniques](https://talks.s-anand.net/2026-09-03-convergence-jio-institute/verification-techniques.html):

<div style="width: 100vw; margin-left: calc(50% - 50vw); width: min(100vw, 100rem); margin-left: calc(50% - min(50vw, 50rem)); margin-top: 1.5rem; margin-bottom: 2rem;">
  <iframe src="https://talks.s-anand.net/2026-09-03-convergence-jio-institute/verification-techniques.html" title="Verification Techniques" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" style="display: block; width: 100%; height: 820px; height: min(56rem, 92svh); border: 0; background: #f5f1e6;"></iframe>
</div>

1. [Run it. Don’t just read it](https://talks.s-anand.net/2026-09-03-convergence-jio-institute/verification-techniques.html#show=18&technique=8). In other words, tell agents to run test cases. Works well with code, but you can programmatically verify [mathematical proofs](https://en.wikipedia.org/wiki/Lean_(proof_assistant)) and even [contracts](https://www.researchgate.net/publication/388354297_Computable_Contracts_for_Insurance_Establishing_an_Insurance-Specific_Controlled_Natural_Language_-_InsurLE).
2. [Triangulate sources](https://talks.s-anand.net/2026-09-03-convergence-jio-institute/verification-techniques.html#show=18&technique=4). Ask it to find evidence from multiple sources.
3. [Set the test first](https://talks.s-anand.net/2026-09-03-convergence-jio-institute/verification-techniques.html#show=18&technique=1), i.e. define your acceptance criteria - or at least, tell it to define acceptance criteria first, so you can verify if that's OK.
4. ... and so on for 18 of these.

I didn't verify the verification techniques! But it's something I plan to go back to and see if (a) there's something I should do more of and (b) there's something I'm not doing enough of.

[Here are my top delegation techniques](https://talks.s-anand.net/2026-09-03-convergence-jio-institute/autonomy-techniques.html):

<div style="width: 100vw; margin-left: calc(50% - 50vw); width: min(100vw, 100rem); margin-left: calc(50% - min(50vw, 50rem)); margin-top: 1.5rem; margin-bottom: 2rem;">
  <iframe src="https://talks.s-anand.net/2026-09-03-convergence-jio-institute/autonomy-techniques.html" title="Delegation Techniques" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" style="display: block; width: 100%; height: 820px; height: min(56rem, 92svh); border: 0; background: #f5f1e6;"></iframe>
</div>

1. [Draft only. NEVER send](https://talks.s-anand.net/2026-09-03-convergence-jio-institute/autonomy-techniques.html#show=18&technique=9). That retains control with very low effort.
2. [Work independently](https://talks.s-anand.net/2026-09-03-convergence-jio-institute/autonomy-techniques.html#show=18&technique=1). I tell it to ask me _only_ if it really needs to.
3. [Implement, test, fix](https://talks.s-anand.net/2026-09-03-convergence-jio-institute/autonomy-techniques.html#show=18&technique=13). I ask it to go ahead with the implementation without review when tests are available.
4. ... and so on for 18 of these.

I didn't verify these either, and I'm not as happy with these - perhaps because I didn't understand them well, or I didn't ask the question well, or I haven't spent enough time exploring autonomy / delegation. But I do plan to explore more.

![](https://files.s-anand.net/images/2026-09-05-how-i-verify-and-delegate-to-ai.avif)

What I learnt / re-learnt:

1. Even if you have nothing to teach, discovering from the audience can teach.
2. Your workflow logs are an insight source if people want to learn from you.
3. [Speaking under-prepared](https://www.s-anand.net/blog/speaking-unprepared/) is scary but educational.
