---
title: No Juniors, No Experts
date: 2026-07-01T18:03:15+08:00
description: To solve the junior training bottleneck caused by AI, I stopped hiring beginners to code. Instead, I have them use AI agents to build solutions rapidly, shifting their role to verifying output and designing checks.
tags: [ai-agents, software-engineering, ironies-of-automation]
---

Read out by Anand, who is not an AI. See [Beating Pangram and AI detectors](https://www.s-anand.net/blog/beating-pangram-and-ai-detectors/).

<blockquote>

These days, AI is reducing the number of entry-level jobs that we have. The trouble is, these are the jobs that are actually training tomorrow's architects. How do we solve this? This is not a new problem.

Zoho's Sridhar Vembu posted something that's been bugging me. He said, AI makes senior architects more productive and reduces the need for junior engineers. Then he says, if nobody starts junior, how can anyone become an architect? The data supports his concern. Stanford found that since late 2022, the employment for 22-25 year olds in jobs where AI is strong, like software, fell by as much as 16% compared with older workers who were doing the same jobs. Matt Dean at UCSB also saw this happening in robotic surgery. A phenomenon that happened even before AI came into the picture, because robotic consoles would allow surgeons to do what the residents used to do, and therefore, surgeons stopped bothering to train the residents.

But this is not a new problem. Accountants, pilots, and chessmasters have faced this problem and have solved it before in three different ways.

For example, spreadsheets made manual ledgers redundant. But manual bookkeeping is how accountants used to learn accounting. That's how they figured out what the different kinds of errors are and how they occur. But after spreadsheets, their job changed. Very few people were checking the arithmetic, and more people were designing the checks and balances that caught the errors. Today there are more accountants than when we were doing manual spreadsheets. In other words, **they switched jobs**.

Autopilots, on the other hand, reduced due junior pilots' flying hours. But when Air France 447 went down, the regulators responded with the FAA 2014 rule that mandates manual flight training. Surgical simulation centers are doing a similar job today. They force professionals to practice those rare cases which automation doesn’t expose them to. In other words, **they enforced**, since being wrong is dangerous.

Chess grandmasters took a different route. Any free phone application today can beat every grandmaster. Chess should have vanished. But instead, chess is now even more popular than it used to be. Chess engines have become the coaches, and the young grandmasters today are much better than those from any previous generation. **They upskilled** when the journey is more important than the destination.

Commercial software is mostly in the switch bucket. Broken deployments and prototypes and quick POCs aren't so important that you can't live with them. You just catch them and move on. So, as a result, I have stopped hiring junior developers to write code. Instead, I hire them to catch the things that AI gets back. One of my interns goes to client meetings, records the calls, feeds the transcripts to an AI coding agent, and builds the solution the client asked for. I've told him deliberately to not even try and understand what the clients say. The clients are experts in their domain, he is not.

But, it turns out that he is about three times as fast as anyone else with five years of experience, because that experience is the bottleneck. Because the experienced people are trying to understand things and slowing the system down. For mission-critical software, this is dangerous. Wrong code in a trading system or a medical device can hurt people. In such cases, it's important to build coding as a skill deliberately. Using AI as a simulator or as a coach can be really powerful, because Bainbridge's irony of automation still applies.

"The better the machine gets, the rarer the human intervention, and the harder it is to stay sharp for the one time it matters."

Which bucket your software is in may not be obvious upfront. If we get it wrong either way, it costs us money or harm. Either we overtrain, or we underenforce.

Vembu is not sure how to resolve this. Nor am I.

</blockquote>
