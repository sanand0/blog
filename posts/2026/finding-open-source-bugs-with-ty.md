---
title: Finding open source bugs with Ty
date: 2026-01-11T11:55:19+08:00
categories:
  - coding
  - llms
description: I used Astral’s Ty type checker and ChatGPT to identify a real bug in tqdm's rich integration. After verifying the error, I used Gemini to find an existing unmerged pull request and bumped it for review.
tags: [python, llms, chatgpt]
---

Astral released [Ty (Beta)](https://astral.sh/blog/ty) last month.

As a prototyper, I don't type check much - it slows me down. But the few apps I shipped to production had bugs type checking could have caught. Plus, LLMs don't get slowed by type checking.

So I decided to check if Ty can spot _real_ bugs in _real_ code.

[I asked ChatGPT](https://chatgpt.com/share/69631ff0-c14c-8003-bee2-13f016240cbd):

> Run `ty` (Astral's new type checker) on a few popular Python packages' source code, list the errors Ty reports (most of which may be false positives), and identify at least a few that are genuine bugs, not false positives. Write sample code or test case to demonstrate the bug.
>
> Don't fool yourself into inventing false or borderline bugs. Find genuine bugs.

After 25 minutes, ChatGPT reported:

```python
from tqdm.rich import tqdm

bar = tqdm(total=3)
bar.update(1)

# This crashes inside tqdm's rich integration
bar.reset(total=3)
```

... produces this error:

```text
TypeError: Progress.reset() missing 1 required positional argument: 'task_id'
```

I verified this locally:

```bash
uv run --with tqdm python -c '
from tqdm.rich import tqdm
bar = tqdm(total=3)
bar.update(1)
bar.reset(total=3)'
```

![](https://files.s-anand.net/images/2026-01-11-tqdm-rich-ty-bug.webp)

Yes! Same error.

But is it really a bug?

[I asked Gemini](/blog/notes/gemini-tqdm-rich-task-id-bug/):

- Is this a real tqdm bug?
  - Yes, it is.
- Could I submit a pull request? Is tqdm active and reviewing/accepting pull requests - especially for the rich integration?
  - Yes, you should.
- Find existing PRs with overlapping functionality. List the closest ones
  - Issue [#1306](https://github.com/tqdm/tqdm/issues/1306) and PRs [#1395](https://github.com/tqdm/tqdm/pull/1395), [#1438](https://github.com/tqdm/tqdm/pull/1438) are close, but different.
- (I checked manually.) [#1674](https://github.com/tqdm/tqdm/issues/1674) looks very similar... is it?
  - No, that's a different bug
- (I wanted to be sure.) What about this issue: [#1378](https://github.com/tqdm/tqdm/issues/1378)
  - Yes, that's an exact duplicate, waiting since 2022. (Stupid LLM!)
- What is the minimal fix?
  - Add `self._task_id` as the first argument to `self._prog.reset(total=total)` in `tqdm/rich.py`
- This PR seems to do that: [#1379](https://github.com/tqdm/tqdm/pull/1379) doesn't it? Why is it not merged yet?
  - Yes, it was even approved, but not merged. Bump up. Else, submit your own PR.

So I [bumped it up](https://github.com/tqdm/tqdm/pull/1379#issuecomment-3733928734)

This entire process of:

- Finding a bug
- In a new codebase
- Verifying the bug
- Finding an existing PR
- Bumping it up

... took 30 min of my time and 30 min of computer time.

The hardest problem in computer science isn't P-vs-NP or cache invalidation. It's understanding why a human will click a green 'Merge' button.
