---
title: Things I Learned - 14 Apr 2024
date: 2024-04-14T00:00:00+00:00
categories:
  - til
description: I discovered new VS Code shortcuts, Copilot terminal integration, and the SQLime browser playground. I also explored Python's fsspec for filesystem protocols and learned why embracing inaction and subtraction can be a strategic advantage.
keywords: [vs code, github copilot, fsspec, sqlime, sqlite, productivity]
---

This week, I learned:

- Prashant Pandey: we need to prepare before every meeting. Something to teach
- VS Code
  - Select any code and command `Explain this` to understand the code
  - `%something` in command bar searches ACROSS files for a term. Exactly like `Ctrl+Shift+F`
  - Copilot has an Inline Chat: Start in Terminal (that needed me to unbind Ctrl+I in bash to work)
  - `Ctrl+2` opens a second window on the side. `Ctrl+1` goes back to the first window
  - Terminal: Open Detected Link lets you scroll through detected (file) links in terminal
  - Terminal sticky scroll is transparent. (But Terminal stick scroll isn't working for me.)
  - Copilot uses last 10 commit messages, Jupyter notebook kernel state (variables) as additional context
  - 1.88: supports locked scrolling to sync scrolling of side-by-side windows
- [fsspec](https://filesystem-spec.readthedocs.io/) is used by [csvbase](https://csvbase.com/blog/7), Pandas, etc. to implement file system protocols like `s3fs`, `gcfs`, etc.
- [SQLime](https://github.com/nalgeon/sqlime) is a SQLite client / playground on the browser!
- Do nothing. Then do less
  - Humans have a bias against inaction. Hence a strategic advantage. What can you cancel today?
  - Humans have a bias against subtraction or removal. That too is a strategic advantage. What can you remove today?
  - Humans have a bias against constraints. That's a strategic advantage. What constraint can you embrace?
  - No Yay! When declining something, add it your calendar so that when the time comes you can say yeah I got this time back
