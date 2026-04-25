---
title: Using game-playing agents to teach
date: '2026-03-08T19:06:03+08:00'
categories:
- education
- llms
description: Game-playing agents can turn abstract concepts into interactive classroom experiences, making learning more exploratory, social, and memorable.
keywords: [game-based learning, AI agents, education, interactive teaching, network games, classroom design]
---

After an early morning beach walk with a classmate, I realized I hadn't taken my house keys. My daughter would be sleeping, so I wandered with my phone.

This is when I get ideas - often a dangerous time for my [students](https://tds.s-anand.net/).

[![](https://files.s-anand.net/images/2026-03-08-using-game-playing-agents-to-teach.avif)](https://tds-network-games.sanand.workers.dev/)

In this case, the idea was a rambling conversation with [Claude](https://claude.ai/share/55ba24d2-f250-4e2f-ab1c-89090742fb82) that roughly begins with:

> As part of my Tools in Data Science course, I plan to create a Cloudflare worker which allows students to play a game using an API. The aim is to help them learn how to build or use AI coding agents to interact with APIs to solve problems.
>
> The game needs to be:
>
> - **Playable yet challenging:** Fun by itself, human-playable via a text interface, but hard to solve manually at scale. Easy with an AI coding agent. Maybe a maze or text adventure?
> - **Seed randomized:** Generate a different problem for each student & week, so they can't reuse a solution.
> - **Verifiable:** The solution and score must be publicly verifiable (JWT token?) without requiring shared secrets.
>
> Give me game ideas and explain:
>
> 1. What'll the game like on the API and the UI?
> 2. Why these ideas? What's interesting about the game?
> 3. What'll students learn by playing the game directly?
> 4. What'll students learn using AI coding agents on the API?

It generated four ideas. I picked three.

### Labyrinth

It's a maze where each may have a data row. Students wander, collect required fragments, reach the exit room, and answer a statistical question from collected data - within a fixed number of moves.

Manual play teaches spatial reasoning, _systematic_ exploration, and the cost of backtracking.

AI agent play teaches graph traversal, stateful API interaction, and basic data aggregation.

[**Play Labyrinth**](https://tds-network-games.sanand.workers.dev/labyrinth/)

<video controls autoplay loop muted playsinline preload="metadata" width="1600" height="1200" style="max-width: 100%; height: auto;">
  <source src="https://files.s-anand.net/images/2026-03-08-tds-game-labyrinth.webm" type="video/webm">
  <a href="https://files.s-anand.net/images/2026-03-08-tds-game-labyrinth.webm">Video</a>
</video>

### Detective

You're investigating a financial network of accounts with transaction links looking for a compromised account which behaves strangely on multiple attributes. Find it, and trace the shortest path to an "anchor" account using as few node queries as possible.

Playing manually teaches graph intuition, anomaly detection by feel, and the frustration of systematic searches.

AI agent play teaches graph traversal algorithms, outlier detection, path reconstruction, and the exploration-exploitation tradeoff - all real-world data science skills.

[**Play Detective**](https://tds-network-games.sanand.workers.dev/detective/)

<video controls autoplay loop muted playsinline preload="metadata" width="1600" height="1200" style="max-width: 100%; height: auto;">
  <source src="https://files.s-anand.net/images/2026-03-08-tds-game-detective.webm" type="video/webm">
  <a href="https://files.s-anand.net/images/2026-03-08-tds-game-detective.webm">Video</a>
</video>

### Signal

AI has locked all your exits in a research facility. You need to restart the core systems by exploring rooms, combining objects, and solving the AI's puzzles.

This game is **AI-agent native**: LLMs can parse the hints better than humans. Students using pure rule-based agent will struggle, teaching **LLM-as-a-tool within a larger agent pipeline** - an important real-world pattern.

Playing manually teaches inventory management, dependency reasoning, close reading of ambiguous instructions.

AI agent play teaches multi-step planning with dependencies, agents-in-the-loop, NLP, and state management.

[**Play Signal**](https://tds-network-games.sanand.workers.dev/signal/)

<video controls autoplay loop muted playsinline preload="metadata" width="1600" height="1200" style="max-width: 100%; height: auto;">
  <source src="https://files.s-anand.net/images/2026-03-08-tds-game-signal.webm" type="video/webm">
  <a href="https://files.s-anand.net/images/2026-03-08-tds-game-signal.webm">Video</a>
</video>

### Implementation

Frankly, I just asked Codex to crunch it over five hours of a [Vijay Antony movie binge](https://en.wikipedia.org/wiki/Vijay_Antony#Filmography).

Seriously. I did **NOT** look at the code. I just wrote 12K worth of prompts (which I'll share later) while it processed 129 million tokens, generated 625K of tokens, and got the entire job done.

The game is now part of the [TDS Project 1](https://exam.sanand.workers.dev/tds-2026-01-p1) - apart from a bunch of other exercises. With this as inspiration, I hope to include many more gamifications into this course.

This feels a bit like [Maze Runner](https://en.wikipedia.org/wiki/The_Maze_Runner_(film)). My condolences to the students.
