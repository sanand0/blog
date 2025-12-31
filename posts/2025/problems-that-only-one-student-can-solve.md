---
title: Problems that only one student can solve
date: "2025-08-31T08:56:28Z"
lastmod: "2025-08-31T08:57:13Z"
categories:
  - coding
  - education
wp_id: 4183
---

![Problems that only one student can solve](/blog/assets/ChatGPT-Image-Aug-31-2025-03_55_11-PM.webp)

[Jaidev's The Bridge of Asses](https://jaidevd.com/posts/bridge-of-asses/) reminded me of my first coding bridge.

It was 1986. I'd completed class 6 and was in a summer coding camp at school. M Kothandaraman ("MK Sir") was teaching us how to swap variables in [BASIC](https://en.wikipedia.org/wiki/BBC_BASIC) on the [BBC Micro](https://en.wikipedia.org/wiki/BBC_Microcomputer).

This code prints the first name in alphabetical order ("Alice"):

```python
10 A = "Bob"
20 B = "Alice"
30 IF A > B THEN
40   TEMP = A
50   A = B
60   B = TEMP
70 END
80 PRINT A
```

The homework was to print **all** details of the first alphabetical name:

```basic
10 A = "Bob"   : ASEX = "M" : AAGE = 30
20 B = "Alice" : BSEX = "F" : BAGE = 20
```

After a few hours and a headache, I came up with:

```python
30 IF A > B THEN
40    TEMP = A : TEMPSEX = ASEX : TEMPAGE = AAGE
50    A = B    : ASEX = BSEX    : AAGE = BAGE
60    B = TEMP : BSEX = TEMPSEX : BAGE = TEMPAGE
70 END
80 PRINT A, ASEX, AAGE
```

After 39 years, I still remember the code. I also remember the moment when MK Sir asked if anyone had solved it. My hand went up -- the only one in a group of 15. I stood, opened my ruled notebook, recited the code. He nodded and wrote it on the blackboard for all to see.

There's a thrill in solving a hard problem. It's bigger if you're the only student who solved it. I was so inspired that I've coded almost every day since then.

Today, I'm a teacher. Sometimes only one student solves a tough problem I set (e.g. the first student who hacked my [exam](https://exam.sanand.workers.dev/tds-2024-sep-roe1)). Those moments are **delightful**!

Teachers measure themselves by how much students learn (e.g. better scores). Another measure is how many they inspire. Problems that only one student solves may be a sign of inspiration.

With apologies to other students, I will be adding more such hard problems in my [course](https://tds.s-anand.net/).

PS: One other thing delights people as much: success at vibe-coding. The look on the facilities manager's face, after vibe-coding an empty-room detection app, was priceless. I'll use that more to inspire non-developers.
