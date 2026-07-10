---
title: Discussion with Arvind Satyanarayan
date: 2026-07-05T15:02:39+05:30
categories:
  - visualization
description: I discuss visualization grammars with Arvind Satyanarayan, exploring how GoFish uses Gestalt-based graphical relationships to help AI agents reason about design. I am experimenting with these grammars to improve AI visualization diversity and building automated verification systems.
keywords: [arvind satyanarayan, gofish, visualization grammars, vega-lite, malleable software, ai agents]
---

After [Arvind Satyanarayan's](https://www.csail.mit.edu/person/arvind-satyanarayan) [talk](https://vizchitra.com/2026/sessions/infinite-design-space) at [VizChitra 2026](https://vizchitra.com/2026), a group of us kept talking about machine learning, visualization grammars, creativity, software and education.

The conversation began with a basic question. Why do modern AI systems work so well when the mathematics behind them can look surprisingly simple?

![](https://files.s-anand.net/images/2026-07-05-discussion-with-arvind-satyanarayan.avif) <!-- https://chatgpt.com/c/6a4a2924-b390-83ec-bb52-392a52e0b0e9 -->

### The bitter lesson

Arvind said that much of the mathematics behind machine learning is not especially complicated. What is unusual is the scale at which it is applied.

This led to [Richard Sutton's "bitter lesson"](https://www.incompleteideas.net/IncIdeas/BitterLesson.html). Researchers often try to put human knowledge, rules and clever heuristics into machines. Over time, methods that use more data, more computation and general learning tend to beat those carefully designed systems.

That is why the lesson is bitter. Many people enter science hoping to understand why something works. Machine learning often seems to say: stop trying to explain so much, and give the system more data and compute.

Arvind was not saying that understanding is useless. His point was narrower. Historically, attempts to build our understanding directly into AI systems have often lost to methods that learn at scale. ([incompleteideas.net](https://www.incompleteideas.net/IncIdeas/BitterLesson.html?utm_source=chatgpt.com))

The discussion then moved briefly to a data journalism project about human suffering. Saurabh described how it began as a small social media idea and then grew into a much larger journalistic project.

The first charts counted incidents by month. But the numbers were difficult to look at. Each row referred to real people and real violence. The team stepped back, designed a more systematic process and checked the data several times.

Arvind said this was important. It is easy to turn human lives into marks on a chart: a bar showing deaths, a colour showing an attack, a point showing a bombed school. Once the data becomes a chart, the designer can lose touch with what those marks mean.

You still need abstraction to work with data. But the abstraction can also hide the people in it.

### Why are there so many visualization grammars?

I asked whether there could be a Pareto-optimal visualization grammar. One grammar that works well across most cases. Or perhaps several grammars, each for a different part of the design space.

Arvind said this was close to the motivation behind [GoFish](https://vis.csail.mit.edu/pubs/gofish/), which [Josh Pollock](https://www.linkedin.com/in/josh-pollock/) and [Arvind's group](https://vis.mit.edu/) have been developing.

After [Vega-Lite](https://vega.github.io/vega-lite/), visualization research saw many specialized grammars. There were grammars for unit visualizations, hierarchies, biological data and other domains.

That was useful. It showed that people liked the idea of a grammar. A grammar gives authors a set of concepts they can combine instead of only a fixed list of chart types.

But it also raised a question. Why did every new visual form need a new grammar?

One reason was that existing grammars were hard to extend. A system such as Vega-Lite does more than turn a specification into marks. It contains many rules about what a reasonable chart should look like.

Suppose an author specifies a point with x, y and colour. Vega-Lite gives you a coloured scatter plot. Change the point to a line, and it may produce separate lines for the colour categories. Change the line to a bar, and it may stack the bars.

Each result makes sense. The author is usually happy with what Vega-Lite did.

But the rules add up. Adding a pie chart is not just adding a circular mark. The developer has to decide how pie charts work with colour, aggregation, faceting, stacking and every other feature already in the language.

The combinations grow quickly. A system that tries to make every common case easy can become difficult to extend.

Arvind said this accumulated complexity had made contributing to Vega-Lite frustrating. A decade of useful heuristics had also produced a codebase where every change required understanding many hidden interactions.

The easier choice for a researcher was often to create a new grammar for one limited design space.

GoFish makes a different bet. Perhaps there is something close to a universal grammar of graphical representations.

Instead of treating chart types as the main units, GoFish formalizes graphical relationships inspired by [Gestalt principles](https://en.wikipedia.org/wiki/Principles_of_grouping), such as containment, connection, alignment and uniform spacing. These relationships appear in statistical charts, diagrams and user interfaces. ([vis.csail.mit.edu](https://vis.csail.mit.edu/pubs/gofish/?utm_source=chatgpt.com))

The group has already expressed forms that were previously handled by several separate grammars. But Arvind said they do not yet know GoFish's limits.

The boundaries of Vega-Lite became clear only after years of use. GoFish is now in a similar phase. It looks broad, but the group still has to find where it breaks.

### Should a grammar contain domain knowledge?

Rohit asked whether a grammar could really be universal. A grammar is more than a set of tags. It usually contains ideas about the domain and ideas about good design.

Arvind agreed that visualization grammars have historically included domain-specific meaning. But GoFish is testing whether that meaning has to live inside the grammar.

Perhaps the grammar should describe graphical structure, while other layers supply domain knowledge, design rules and context.

This becomes important when domain knowledge is tightly built into the language. The more a grammar decides for the author, the harder it can be to extend.

GoFish therefore exposes simple graphical operators and lets authors bring in ordinary code. I asked about escape hatches. What happens when the grammar cannot express something?

Arvind said escape hatches were built into the architecture. An author can use a native JavaScript function almost anywhere. For example, an operation shown as `orderBy` was not a special GoFish construct. It used [Lodash](https://lodash.com/).

The same approach lets the system use [D3](https://d3js.org/) layout functions as graphical operators. Once a D3 layout becomes another line in GoFish, authors can combine it with structures that the original developer may not have expected.

The result may be strange. It may also be useful. You can at least make it and look.

### A grammar as a thinking tool for agents

I suggested that the important grammar might not be a rendering grammar. It might be a thinking grammar.

AI systems can already generate [D3](https://d3js.org/) code. What they may need is a structured space where they can consider several visualizations before choosing one.

Arvind said this was increasingly how he saw grammars.

The traditional value of a grammar was its compiler. You describe a chart in a high-level language, and the system turns it into graphics. [Vega](https://vega.github.io/vega/) was created partly because it was easier for a higher-level tool to produce structured JSON than to construct D3 code directly. Vega itself initially compiled specifications into D3. ([vega.github.io](https://vega.github.io/vega/about/vega-and-d3/?utm_source=chatgpt.com))

With agents, the grammar can play another role. It can describe the concepts the agent should think with. What are the parts of a visual representation? How can they fit together? What kinds of combinations are worth trying?

The agent does not have to use the grammar's compiler. It could implement the result in D3, ordinary JavaScript or another graphics system. Arvind cared about the concepts and how the agent reasoned with them.

This could help an agent avoid immediately producing the most common answer in its training data.

Arvind described GoFish as a way to get an agent to explore the design space instead of giving one average answer.

That raised another question. Can an agent reason about a visualization without rendering it?

GoFish operators have affordances. They suggest the kinds of readings a graphic might support. In principle, an agent could reason about those affordances before rendering every option.

Arvind was not sure how far this would work. Two operators may be well understood separately and still behave in unexpected ways when combined. Cultural differences, personal interpretation and the author's intended story may also be hard to encode.

The amount of design knowledge that would need to be formalized could be enormous.

His group is also exploring a render-and-evaluate loop. An agent could generate a visualization, inspect it, evaluate it and revise it, perhaps using reinforcement learning. Formal reasoning could narrow the space. Rendering could catch things that were not obvious from the specification.

### Does GoFish make AI more creative?

I asked how we would know whether GoFish made an agent produce more diverse visualizations than D3.

A simple experiment might ask the same model for three diverse designs using GoFish and three using D3, then compare their range and quality.

Arvind said this was still a hypothesis.

His reason for expecting a difference was that D3's training data may itself be narrow. Many developers start with the [D3 example gallery](https://observablehq.com/@d3/gallery), copy an example and modify it. Much of the unusual D3 work came from a fairly small group, including [Mike Bostock](https://bost.ocks.org/mike/) and data journalists.

A language model may therefore connect D3 with a limited set of templates. D3 itself does not tell the model how ideas such as containment or grouping can be combined in new ways.

GoFish might provide some of that structure.

I was less sure. Models often transfer patterns between code, language and unrelated domains. Perhaps they already know enough to diversify, and a good prompt is enough to bring that out.

Arvind said the past few years had taught him not to bet against models. But he saw a tension in how current models are trained.

They are trained to produce answers that satisfy many people. That tends to pull them towards the average. Creativity often involves moving away from the average.

A prompt can ask for diversity. But the prompt is working against part of the training.

### Is AI creativity always slop?

We then disagreed more directly about AI-generated creative work.

Arvind's strongest counterargument was simple: if prompting could reliably produce useful diversity, why was so much AI writing still slop?

[Saurabh](https://www.linkedin.com/in/saurabhplum/) argued that much of the problem came from lazy prompting. [Samarth](https://www.linkedin.com/in/samarthgulati/) referred to [Jaidev](https://www.linkedin.com/in/jaidevd/)'s observation that one-shot outputs tend to be conventional. Asking the model to be more creative increases hallucination, but filtering the results can keep some of the creativity while removing errors.

I shared two recent examples.

The Times of India had been using Claude and ChatGPT to help [generate ideas](https://sanand0.github.io/journalists/statnostics/) for its recurring "[StaTOIstics](https://x.com/hashtag/STATOISTICS)" graphics. After several rounds of iteration, some of the work was being published automatically, though humans still checked the analysis and data.

In a workshop that morning, participants had voted on charts they were willing to put their names against. A completely AI-generated chart came first. Another fully AI-generated chart came second.

This did not prove that AI was generally creative. It did show that, in one practical setting, the audience preferred the AI charts.

Arvind had two cautions.

First, the average person may not know how to judge exceptional writing, art or visualization. Winning a preference vote does not mean the work is excellent.

Second, people's values change when production becomes cheap. Once a style can be mass-produced, people may start valuing something else. The model may keep chasing an older idea of originality.

So "solving creativity" may not have a clear finish line. Once machines can produce one kind of valued work cheaply, people may stop calling that quality especially creative.

### Different kinds of writing value different things

Arvind connected this to Anthropic's work on model personas and internal behavioural directions, such as [persona vectors](https://www.anthropic.com/research/persona-vectors).

His programming analogy was that everything inside a model exists in one global namespace. Change one behaviour, and it may affect others in ways you did not expect.

Training a model to be a better technical writer could alter its creative writing. Technical writing often values precision. Poetry may value ambiguity, rhythm or surprise. Even academic fields disagree about what good research writing looks like.

These values may not fit into separate clean modules. A post-training change intended for one genre can affect another.

Arvind called this speculation, since he is not a machine-learning researcher. He expected current models to improve a lot, but doubted that scaling and post-training alone would make them creative in the same way humans are.

He was also happy to be proved wrong.

### Verification is not enough for science

Saurabh raised the argument that AI is advancing fastest in coding because code has strong verification. Tests and compilers provide feedback. Writing and art are harder because quality is harder to check mechanically.

Arvind was sceptical that science was as verifiable as some AI companies suggested.

Agents can automate much of the dull work in science: cleaning data, writing code, running standard analyses and searching literature. Researchers are usually glad to hand over that work.

But that does not mean the agent can do the whole of science.

At the research frontier, you still have to decide which question is worth asking, which direction is worth following and what would count as an important result.

Often, the definition of a good result is part of the unknown. There may be no existing verifier.

Nimit made a related distinction. Coding is often telic. We write code to accomplish another task. Writing and art can be autotelic. Writing is also a way to think, and art can be made for the experience of making it.

### Deliberation makes coding agents more useful

Samarth described a large software migration he had been doing with an AI agent.

He did not ask the agent to rewrite thousands of lines in one shot. He first grounded it in the existing codebase. Then he asked it to identify decision points, turn those into decision trees and compare architectural choices.

They worked through the choices together. The knowledge that emerged was compressed into reusable skill files. Only then did the agent implement a thin vertical slice that could be tested.

This reduced work that might have taken months to a few weeks.

The value came from the dialogue, decomposition, explicit decisions, feedback and verification. It was not one clever prompt.

This suggested another use for generative visualization: a conversation where the system explores the data, proposes representations, receives feedback and revises both its analysis and its graphics.

### What is visualization still for?

I described a pattern we were seeing in enterprise work.

Clients often ask for dashboards without knowing who will use them or what decision the dashboard should support. A dashboard is a safe organizational object. As Arvind put it, no one gets fired for putting up a dashboard.

But if an agent can read the data, interpret the charts and identify the action, why produce a dashboard?

In one project, an agent generated use cases, analyses and charts. We replaced the final dashboard with an email explaining what had happened and what the recipient should do. The business preferred this because it removed several layers of dashboard production and interpretation.

This led me to suggest that visualization is most useful when the human action is uncertain. If the action is clear, an agent can perform it or recommend it directly.

Arvind agreed with the basic idea.

Researchers including [Tamara Munzner](https://www.cs.ubc.ca/~tmm/) and [Miriah Meyer](https://www.cs.utah.edu/~miriah/) have discussed the difference between cases where computation can answer a precise question directly and cases that need open exploration.

When the data, question and decision can all be stated precisely, an algorithm may be enough. Visualization is useful when we do not know what we are looking for, do not know where it may be in the data, or cannot describe the question properly.

It helps with surprise, discovery, interpretation and uncertainty.

Agents may reduce the number of questions humans need to inspect. But Arvind pointed out a remaining problem. An agent still needs some stopping condition.

If I do not know what I am looking for, how do I tell the agent how to explore? How will it know that it found something important?

I described three methods we had been trying.

One was to give the agent search procedures that often work, such as checking outliers, correlations and unusual changes.

Another was to give it a separate evaluation prompt describing what makes a finding useful.

The third was to let it generate many options and leave the final choice to a human.

The second method uses an LLM as a judge. Arvind said he had probably discounted this architecture too much. A generator-and-judge loop could change where humans stay involved in visualization.

Generation is becoming cheaper. Selection and verification become important because there is more output to inspect. But models are improving at selection and verification too.

The boundary keeps moving.

Accountability may remain with people for longer. Even when an agent performs the analysis and checks the output, somebody is still responsible when it is wrong.

### Dashboards and malleable software

The discussion widened from charts to [malleable software](https://www.inkandswitch.com/essay/malleable-software/): software that users can reshape for their own needs instead of accepting one fixed interface.

AI lowers the cost of imagining and implementing small custom tools. A meeting interface could darken according to the percentage of participants with cameras switched off. A system could represent a 24-hour delay using 24 seconds of silence. Data does not have to appear as a conventional chart.

Arvind liked malleable interfaces as a research problem but added an important constraint. Most people do not care enough to customize most software.

The friction has to be bad enough. People may reshape tools in domains they care about, but probably not every application they use.

Coding agents can reduce customization to asking for a change or automatically submitting a patch. This may produce many local versions of software. Agents could maintain those patches as the main project changes. Upstream developers could observe common changes and absorb the useful ones.

Arvind described related work by a student building on [program synthesis](https://people.csail.mit.edu/asolar/SynthesisCourse/Lecture1.htm). Traditional synthesis can leave a hole in a program and fill it from a formal specification. In this work, the hole can be filled during use. The system watches how a person uses the program and gradually infers what the unfinished part should do.

It is close to a plugin system that partly builds itself.

This brought us back to visualization grammars. Perhaps we no longer need many complete visualization libraries. We may need well-described concepts and functions that agents can combine, extend and refine through use.

### Research and education with AI

The final part of the conversation moved to research and education.

Arvind said his group aims for work that can change a research programme, rather than adding one more incremental paper. Students should leave a PhD with their own way of thinking instead of becoming copies of their adviser.

He normally tells students what to do for their first paper. After that, he offers suggestions but avoids choosing their direction. Students often find this frustrating. Part of the point is that they have to develop their own research taste.

Space matters. His own adviser had helped by giving him room to find a direction.

We discussed the difficulty of building similar research cultures in environments where supervisors are expected to assign tasks. Strong research is hard to produce through instructions, publication targets and managerial oversight alone.

Arvind also described a worrying split among students facing AI. Some are excited. Others are nihilistic. Few seem to hold a stable middle position.

Students who reached MIT by being unusually capable may now feel that their brilliance has been commoditized. At the same time, many use AI only well enough to produce mediocre work. They see everyone else producing similar work, and that can deepen the feeling that nothing matters.

So the educational problem is not simply whether to permit or ban AI.

Students need to learn how to work with it, recognize weak output, think through choices, test results and decide what is worth doing.

I described my own approach as "delegate maximally". Instead of keeping a fixed list of AI-proof skills, keep giving AI everything it might be able to do. Whatever remains is the human role for now.

Arvind refined that idea. AI-proof skills may never be a stable list. Being AI-proof may be a process: delegate aggressively, inspect what remains and repeat as the boundary moves.

Wiser than promising students a permanent set of protected skills.

### Where we ended up

We did not settle the main questions, but here's where I think we ended up:

- The bitter lesson still seems relevant. General methods, data and compute keep beating carefully designed intelligence.
- Visualization grammars became hard to extend because they accumulated many hidden design decisions. GoFish is testing whether graphical structure can improve the quality and diversity of agents' thinking with visualization-native operators.
- For an agent, a grammar may be useful as a vocabulary for reasoning, even if the agent never uses the grammar's compiler.
- Visualization still seems most useful when the question, interpretation or action is uncertain. If the action is clear, an agent may be able to skip the chart and act directly.
- Software may become easier to customize, though people will probably customize only the tools they care enough about.
- And education has to deal with a moving boundary. Any fixed list of human-only skills will probably age badly.

### Actions I'm taking

- Research malleable software: software the explicitly uses AI to adapt or plug in holes - with instrumentation, based on usage.
- Experiment whether grammars can improve agent visualization diversity and quality
- Explore how good a verification system we can build for visualizations

<!-- https://chatgpt.com/c/6a4a2924-b390-83ec-bb52-392a52e0b0e9 -->
