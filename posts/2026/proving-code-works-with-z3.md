---
title: Proving Code Works with Z3
date: 2026-06-22T20:15:22+08:00
categories:
- coding
- llms
description: I explored how Z3 and ChatGPT can find counterexamples in code, starting with integer overflow in binary-search midpoints. I also tested AI-found Python issues and learned which bugs are worth reporting.
tags: [ai-coding]
---

At the [PyCon SG Education Summit](https://pycon.sg/edusummit.html) today, [Melvin](https://www.linkedin.com/in/melvinzhang/)'s lighting talk on "Writing Proofs in Python" began with a subtle bug in this mid-point calculation (often used in binary search or sort) in languages like Java, C/C++, Go, etc.

```go
low = ...
high = ...
mid = (low + high) / 2
```

Since the integers are fixed-width, this triggers an overflow when `low + high` exceeds the maximum integer value.

Even popular libraries like Pandas [had this bug until 2019](https://github.com/pandas-dev/pandas/issues/25485). In fact, even Python's native `list.sort()` had [this sort of bug until 2015](https://github.com/python/cpython/issues/67703)! [Read the details](https://envisage-project.eu/proving-android-java-and-python-sorting-algorithm-is-broken-and-how-to-fix-it/).

### Z3 can find counterexamples

Melvin showed how to use [Z3](https://github.com/z3prover/z3) - a popular theorem prover library - to prove or find errors in code.

```python
from z3 import *

low, high = BitVecs("low high", 32)
s = Solver()
s.add(low >= 0, high >= 0, low <= high)
mid = (low + high) / 2   # signed 32-bit arithmetic

# Find a case where the "obvious" midpoint is wrong
s.add(mid < low)

print(s.check())
print(s.model())
# Prints something like [high = 2142306236, low = 47120451]
```

The output has found a case where the midpoint is less than `low`, which is clearly wrong.

<!-- https://chatgpt.com/c/6a391927-68a0-83ee-8f8c-b7a8c54a1709 | https://chatgpt.com/share/6a391a41-4d78-83ee-af42-0dac8d8227bc -->

### ChatGPT can run Z3 to find issues

I had a [conversation with ChatGPT](https://chatgpt.com/share/6a391ae5-1930-83e8-b357-cbef241de71c) that ran like this: <!-- https://chatgpt.com/c/6a38c544-f850-83ee-b6f1-4a7ccfb9ba00 -->

- **Me**: Prove something with Z3 and teach me.
- **ChatGPT**: OK. Here's how you find the midpoint overflow error.
- **Me**: How can Z3 help me?
- **ChatGPT**: Find edge cases, counter-examples, refactor safely, validate rules, write tests, model workflows, etc.
- **Me**: Any alternatives to Z3?
- **ChatGPT**: Z3 is best, but consider [Dafny](https://dafny.org/) for production code, [Alloy](https://alloytools.org/) for data, [TLA+](https://lamport.azurewebsites.net/tla/tla.html) for workflows, ...
- **Me**: Any popular Python tutorials have Z3-detectable bugs?
- **ChatGPT**: Several! GeeksforGeeks' Interpolation search hits a ZeroDivisionError; in Programiz' Bucket sort, the bucket index can exceed the number of buckets, ...
- **Me**: Find production Python code with Z3-detectable bugs.
- **ChatGPT**: Sure! There are plenty of `ZeroDivisionError`s in networkx, rich, seaborn, xarray, plotly, matplotlib, ...
- **Me**: Find real errors - not nitpicky ones!
- **ChatGPT**: OK, xarray, branca, mizani, shap, matplotlib, ...
- **Me**: If these don't have existing bugs filed, write an issue.
- **ChatGPT**: Sure! Here they are.

### Some issues are not bad

One issue was quite relevant. I raised [#222 on python-visualization/branca](https://github.com/python-visualization/branca/issues/222) which roughly says:

> `LinearColormap(["red", "blue"], vmin=0, vmax=1).to_step(n=1)` fails. But there are times when I just have one bucket/class to display, so shouldn't this work?

Another looked pretty relevant, too. I raised [#11397 on pydata/xarray](https://github.com/pydata/xarray/issues/11397) which roughly says:

> `np.linspace(0, 1, num=1)` works. Shouldn't `RangeIndex.linspace(0, 1, num=1, dim="x")` do the same?

### But not all issues are worth reporting

Maybe not. The [branca LinearColorMap](https://github.com/python-visualization/branca/issues/222) issue feels more real to me than the [xarray RangeIndex.linspace](https://github.com/pydata/xarray/issues/11397) one - maybe because I've faced it.

Maybe we could do this:

1. When **you** find a bug, use Gen AI to report it. It's a real need.
2. If **Gen AI** finds a bug, report it only if you'll really need it.

### Still, Z3 + ChatGPT is quite effective

When testing your own code, the ability to prove it correct or find counterexamples is very powerful.

Since you don't need to know how to use these tools (AI does it for you), the cost of using these is very low.

This adds a useful layer of defense against vibe coded technical debt.

---

**UPDATE: 25 Jun 2026**: The [pull request](https://github.com/pydata/xarray/pull/11401) I submitted to fix it was merged. But this led to a fascinating rabbit hole involving the [Bounty-Hunting Agent Ecosystem](https://www.s-anand.net/blog/bounty-hunting-agent-ecosystem/).
