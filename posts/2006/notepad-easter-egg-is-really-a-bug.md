---
title: Notepad easter egg is really a bug
date: "2006-11-23T12:00:00Z"
categories:
  - links
wp_id: 176
---

If you create a file in Windows Notepad with the string "bush hid the facts", save it and reopen it, it shows you boxes. Same with "this app can break". [Here's why](http://www.steady-rollin.com/content/view/20/). It has nothing to do with George Bush or Microsoft. It's just that these strings are in ASCII, but they also constitute valid Unicode strings, and Notepad guesses (wrongly) that they are in fact Chinese Unicode files.
