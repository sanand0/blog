---
title: No juniors, no experts?
date: Wed, 03 Jun 2026 23:28:48 GMT
description: As AI automates entry-level work, I examine how to build expertise when junior roles vanish. I suggest switching to system design for low-risk tasks and using AI as a high-fidelity simulator for critical, high-stakes skill development.
keywords: [ai automation, skill development, entry-level jobs, ironies of automation, apprenticeship, simulation-based training, risk management]
---

> When AI does the entry-level work, what you should learn depends on what it costs to be wrong.

AI is replacing entry-level roles, especially technical ones. In the US, [Stanford found](https://digitaleconomy.stanford.edu/publication/canaries-in-the-coal-mine-six-facts-about-the-recent-employment-effects-of-artificial-intelligence/) that since late 2022, employment in AI-exposed jobs like software and customer support fell 16% relatively for 22-25 year-olds. Employment for older workers in the same jobs stayed steady.

[Matt Beane](https://www.mattbeane.com/) at UCSB saw this happen in robotic surgery even before AI. Surgeons used to train the next batch of residents. But robotic consoles let surgeons do what residents did earlier, so [they stopped bothering with residents](https://journals.sagepub.com/doi/abs/10.1177/0001839217751692).

Pretty efficient, but, as [Sridhar Vembu](https://x.com/svembu/status/2009558918700355826) asks, where do the next architects come from? Who trains the next generation of experts?

History gives us a few ideas. I see three patterns: switch, enforce, or level-up.

- **Switch.** [Spreadsheets](https://www.npr.org/2015/02/27/389585340/how-the-electronic-spreadsheet-revolutionized-business) made manual ledger redundant. But that manual bookkeeping taught accountants how to catch errors. Eventually, bookkeeping clerks vanished but accountants didn't, because we switched what the job meant: from checking arithmetic to designing the tests to catch errors, to understanding the system. There are more accountants now than before.
- **Enforce.** When being wrong is too risky, we don't let the skill lapse. Autopilots reduced the demand for junior pilots and pilots' hand-flying time and practice. [Air France 447](https://medium.com/faa/the-dangers-of-overreliance-on-automation-5b7afb56ebdc) is a popular example of the consequence. Since then, regulators made manual flying mandatory through the FAA's 2014 [extended-envelope training rule](https://risk-engineering.org/concept/AF447-Rio-Paris). Surgeons did the same: [simulation centres](https://www.sciencedirect.com/science/article/abs/pii/S0002961020307947) rebuild what practice robots took away from residents. They mandate practice, simulate rare cases.
- **Level-up.** Chess engines should have made chess obsolete. A free phone app now [beats any grandmaster](https://www.nbcnews.com/tech/tech-news/world-chess-championship-computers-push-limits-humanity-shines-rcna8282). Instead chess engines became coaches instead. Today's young grandmasters are better than most chess players of the past and the game is more popular than ever.

So what should you do? It depends on the kind of work, and what happens if it goes wrong.

For most work, **being wrong is cheap**: A bad marketing email costs, a weak first draft, a broken deployment. These cause limited damage or you can undo them.

**Switch** in such cases. There's no point learning what AI already does well. Delegate as much as possible to AI and get out of the way. Watch closely where it fails. Learn to do what AI does badly: choosing the problem, taking action, challenging the question. It's why [I prefer interns](https://solutionsreview.com/thinking-beyond-automation-to-safeguard-tomorrows-software-talent/) who use AI agents and catch its mistakes, over experts who patiently write code that AI writes better.

For some work, **being wrong is expensive, or irreversible**: a wrong drug dose, a wrong trade, a bridge, an airplane. Humans are the last line of defence, and [Bainbridge](https://en.wikipedia.org/wiki/Ironies_of_Automation) showed the better machines get, the harder humans need to train, because their failures are rarer and bigger.

**Enforce** in such cases. Build the skill using AI as the expert. Let it be the teacher who simplifies concepts, the Socratic partner that quizzes you, the clever friend who tries to trip you up with rare edge cases. Flight simulators and surgical sim-centres have been doing this for years. AI makes it cheap enough for everyone.

The last type of work **we do for its own sake**: exercise, chess, sports, music. Machines beat us long ago, but we don't care. The output isn't the point. The process, the competition, the joy of mastery - that's what matters.

**Level-up** in such cases. Use the machine as a coach and break records. Redefine what we thought was impossible.

Most software is in the "switch" bucket. Delegate to AI, learn where it fails, and build skills around that.

But if you're building mission-critical software, "enforce" skills using AI as a teacher and simulator.

On the other hand, if you just enjoy coding for its own sake...

<!--

https://docs.google.com/document/d/1FwkpcS6LleBIorToIsI18ZqHW7VtdLy3826-7SzsktQ/edit

- Claude article: https://claude.ai/chat/7dfc4b30-f5f2-4ea7-8e3d-8bcddb5908b0
- https://www.pangram.com/ score: 100% Human

-->
