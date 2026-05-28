---
title: ChatGPT is about FIDE 1600
date: 2026-05-28T16:04:51+08:00
categories:
  - llms
---

I asked ChatGPT to play chess with [Stockfish](https://stockfishchess.org/). Stockfish is a "strong open-source chess engine". It has 8 levels of difficulty, which [roughly maps to these FIDE levels](https://share.google/aimode/yA9NvnPcsZ1TFtmna):

<section ai-disclosure="ai-generated" data-ai-model="gemini-3.5-flash" data-ai-provider="Google">

| Stockfish   | FIDE  | Player Level & Description                                                                  |
| ----------- | ----- | ------------------------------------------------------------------------------------------- |
| Level 1     | ~1000 | **Beginner**: Constantly blunders, hangs pieces deliberately.                               |
| Level 2     | ~1100 | **Advanced Beginner**: Fewer obvious tactical mistakes, plays completely aimlessly.         |
| Level 3     | ~1200 | **Early Intermediate**: Punishes very basic errors but regularly drops pieces.              |
| Level 4     | ~1350 | **Intermediate**: Plays standard opening moves; requires solid, blunder-free play to beat.  |
| Level 5     | ~1450 | **Advanced Intermediate**: Rarely hangs single pieces; you need positional advantages.      |
| Level 6     | ~1650 | **Strong Club Player**: Highly tactical. Aggressively exploits your mistakes.               |
| Level 7     | ~1950 | **Expert**: Exceptionally strong. Requires precise positional mastery and deep calculation. |
| Level 8     | ~2400 | **Grandmaster**: Invincible for most humans. Plays with ruthless perfection.                |
| Full Engine | ~3600 | Our of human reach completely, "like a smart ant trying to debate physics with a human."    |

</section>

In the [first iteration](https://chatgpt.com/share/6a17f88a-dd74-83ec-b6e6-b42fac198d9c), here were the results:

| Stockfish | Result    |
| --------- | --------- |
| Level 0   | Win       |
| Level 1   | Win       |
| Level 2   | Stalemate |
| Level 3   | Stalemate |
| Level 4   | Win       |
| Level 5   | Loss      |
| Level 6   | Loss      |
| ... etc.  | Loss      |

When I asked ChatGPT how it played, it said something like "I wrote a Python program that plays chess using a fixed policy."

That's crazy! So I told it:

> Rather than use a fixed policy, get the move that Stockfish made, analyze it, and return your next move. See if you can win at level 6.

After a few attempts, it [won](https://chatgpt.com/share/6a17f740-0424-83ec-b298-5bf6056a3905)!

[Here's the game](https://lichess.org/l9vffWVr):

<video controls="" width="534" height="542" style="max-width: 100%; height: auto;">
  <source src="https://files.s-anand.net/images/2026-05-28-chatgpt-vs-stockfish-chess-game.webm" type="video/webm"><a href="https://lichess.org/l9vffWVr">ChatGPT vs Stockfish Level 6</a>
</video>

```pgn
[White "ChatGPT"]
[Black "Stockfish Skill Level 6"]
[Termination "White won by checkmate"]
[FinalFEN "4Q3/2qrkp2/4pN2/1pp1P3/7P/p1P3P1/P5K1/4R3 b - - 5 39"]

1. d4 e6 2. c4 Nf6 3. Nf3 Be7 4. g3 O-O 5. Bg2 a5
6. O-O c6 7. Qc2 d5 8. Rd1 Ne4 9. Nc3 Nxc3 10. bxc3 a4
11. e4 h6 12. Bf4 Re8 13. e5 b6 14. Nd2 Ba6 15. h4 Qc7
16. Be3 Bb7 17. f4 Na6 18. Rf1 Rad8 19. f5 Bf8 20. f6 Nb8
21. fxg7 Bxg7 22. Qd1 Nd7 23. Qg4 Nxe5 24. dxe5 c5
25. Bf4 Re7 26. Re1 Kf8 27. Qh5 a3 28. Bh6 dxc4 29. Nxc4 Bxg2
30. Kxg2 Rd3 31. Bxg7+ Kxg7 32. Rf4 Rd2+ 33. Nxd2 Rd7
34. Ne4 b5 35. Rg4+ Kf8 36. Rg8+ Kxg8 37. Nf6+ Kf8
38. Qh8+ Ke7 39. Qe8# 1-0
```

So, guess ChatGPT (GPT-5.5, extended thinking) is at around 1600 FIDE level right now.

What's impressive is that it wasn't specifically trained on Chess. It's just something it picked up on the way.

If it it starts beating level 8 (grandmaster), will we finally acknowledge AGI? (Me? I think [we achieved AGI on 16 Apr 2025](https://marginalrevolution.com/marginalrevolution/2025/04/o3-and-agi-is-april-16th-agi-day.html).)
