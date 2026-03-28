---
title: Testing Pólya heuristics on AI Math
date: 2026-03-27T13:20:25+08:00
categories:
  - llms
  - education
  - coding
---

[Terence Tao said](https://www.dwarkesh.com/p/terence-tao), "We haven't done many experiments ... large-scale studies where we take a thousand problems and just test them."

So I [told Claude](https://claude.ai/share/9cd20830-a385-4e38-8151-ff3c9916f468): _You know my style. Suggest some innovative experiments I could run._

The first suggestion was _cool_! **The Polya Audit**. Polya's [How to Solve It](https://en.wikipedia.org/wiki/How_to_Solve_It) lists 20 heuristics (work backwards, induction, analogy, etc.). Mathematicians treat these as wisdom. Nobody has ever measured which ones actually work, and on what problem types.

So [I prompted Copilot running Claude Sonnet 4.6](https://github.com/sanand0/research/blob/8dc54b81698a8e9c7b088cef4064016c616032a8/lean/prompts.md#the-polya-audit-26-mar-2026-copilot-yolo---sonnet-46-high) to run the [LeanDojo Benchmark](https://github.com/lean-dojo/LeanDojo) through an LLM `n` times, with different Polya heuristic system prompts and compare success rates.

[![Polya heuristics have varying effectiveness across problem types](https://files.s-anand.net/images/2026-03-27-polya-heuristic-vs-problem.avif)](https://sanand0.github.io/datastories/polya-for-ai/)

Not-surprisingly _different heuristics help different problems_.

- Almost every heuristic helps Prealgebra - except "Start from the desired answer and reason step by step back toward the given information.".
- Almost no heuristics helps Number Theory - except "Focus on the largest, smallest, or boundary element. Extremal elements often have special properties.".
- Geometry has an _enormous_ swing. "First strip away complexity and solve an easier version. Observe the pattern, then generalize" helps a lot. But "Find a quantity that can be counted in two different ways. Set up both expressions and equate them" hurts a lot.

The impact of each heuristic is also quite varied.

- The most reliable heuristic is segmentation: "Identify the key condition that splits the problem. List all possible cases exhaustively. Handle each with a complete argument."
- The worst heuristic on average is pattern recognition: "Compute several specific instances. Tabulate results. Identify a pattern. State the conjecture. Then prove or use it." Induction and pigeonhole do pretty bad, too.


Also not-surprisingly, different models respond differently to the same heuristic.

[![Polya heuristics have varying effectiveness across models](https://sanand0.github.io/datastories/polya-for-ai/screenshot.webp)](https://sanand0.github.io/datastories/polya-for-ai/)

- **GPT-5.4-nano: Heuristics disurpt it**. Its built-in problem-solving strategy is already good. Heuristic just make things worse, almost _always_.
- **Gemini 2.5 Flash Lite: More coachable**. Like a student who benefits from advice: it gains up to 6 percentage points from the right heuristic.
- **Claude Haiku: Nearly immune**. It seems to just ignore the heuristic. Its performance barely moves regardless of what you tell it.

The same heuristic on the same problem affects models quite differently, too. For example "Introduce Auxiliary Elements" hurts GPT -25% but helps Claude +14%!

[![Impact of Introduce Auxiliary Elements on different models for Geometry problems varies](https://files.s-anand.net/images/2026-03-27-polya-heuristic-auxiliary-elements.webp)](https://sanand0.github.io/datastories/polya-for-ai/)

---

So yes, different heuristics work for different problems, and different models respond differently to the same heuristic.

But finally, at least for LLMs, we can measure. We can find out _which_ heuristics work for _which_ problems, and _which_ heuristics get varied responses vs which ones are more universally helpful / harmful. And maybe teach humans.

Or maybe not.

![As Calvin says, ""Given the pace of technology, I propose we leave the math to the machines and go play outside."](https://sanand0.github.io/talks/2026-03-21-design-in-the-age-of-infinite-generativity/calvin-play-outside.avif)
