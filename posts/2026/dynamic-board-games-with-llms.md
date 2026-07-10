---
title: Dynamic board games with LLMs
date: 2026-01-13T11:38:01+05:30
categories:
  - llms
  - games
build: { list: never, render: always }
robotsNoIndex: true
description: I found an LLM app that instantly builds Monopoly-style board games for any topic. It generates thematic tiles and questions, transforming complex strategy sessions like policy simulations into addictive, interactive workshops through rapid game prototyping.
tags: [llms, educational-technology]
---

In December, [Ritesh](https://github.com/ritesh17rb/) built a surprisingly addictive LLM app called [Strategy Board Game](https://ritesh17rb.github.io/board-game/).

Give it any topic, and it creates a [Monopoly](https://en.wikipedia.org/wiki/Monopoly_(game))-like board game that teaches an audience the topic, featuring difficulty levels, a spinning dice, sound effects, ... the whole works!

The mechanism is simple.

1. **Pick a topic** (e.g. "Corporate Turnaround") and difficulty (e.g. "Normal").
2. **Generate 20 tiles**, each covering a key concept in the topic (e.g. "Cost Reduction", "Risk Management", ...).
3. Let the user **roll a dice** and move across the board, landing on a tile.
4. Have an LLM **generate a multiple-choice question** of normal difficulty based on the tile, along with options, the correct answer, etc.
5. The **user answers** the question, earns points, and continues playing until all tiles are covered.

It's very addictive! Every time I show this to people, I have to resist the temptation to play it myself.

[![](https://files.s-anand.net/images/2026-01-13-dynamic-board-games-with-llms.webp)](https://ritesh17rb.github.io/board-game/)

---

When [Ankor](https://www.linkedin.com/in/ankorrai) met [Debjani](https://www.linkedin.com/in/debjani-ghosh-48298b1/) at [NITI Aayog](https://en.wikipedia.org/wiki/NITI_Aayog), here's how the conversation went.

**We**: Let's play a game. You said we want to improve the girl child's dropout rate. Let's play Monopoly.

**She**: Ah. Perfect.

**We**: Why don't you roll the dice.

_[She rolls the dice and studies the question on the board]_

**She**: Hmm... I don't like changing the school fees, nor limiting the number of students... Hm... _[Clicks an answer]_

**She**: So I got the right answer!

**We**: Let's pick another topic. What else did we talk about? Floods. Let's type in _Reducing floods in states._ And now you have a new game. The questions can be simple MCQs or a complex strategy simulation game.

**She**: Amen. I'm telling you, that was my workshop plan. Which is, you take a strategy, you take all their targets, and you have them do a simulation workshop through the day. And you show how interventions work. This is _exactly_ what I want to do!

**We**: It could be a collaborative gameplay.

**She**: Let's create a fictitious state, okay? We break up the group into four. Give each a state with goals. Now you have 5 years to achieve things. So what are your data strategies? And then one of the groups will come out hopefully with the right strategy and you know then there's a sharing learning. Can you run this for us?

... and an engagement opportunity was born.

---

Gamifying learning has obvious applications in almost any area. But game design is hit-and-miss. The good part is that **LLMs make prototyping game ideas super fast**, and this Monopoly-style board game has stumbled on a few good "hits".
