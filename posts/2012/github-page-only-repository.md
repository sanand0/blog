---
title: Github page-only repository
date: "2012-12-14T02:54:51Z"
lastmod: "2012-12-26T09:28:15Z"
categories:
  - coding
wp_id: 2838
---

Github offers [Github Pages](http://pages.github.com/) that let you host web pages on Github.

You create these by adding a branch to git called `gh-pages`, and this is often in addition to the default branch `master`.

I just needed the `gh-pages` branch. So [thanks to YJL](http://blog.yjl.im/2012/02/pushing-to-github-pages-gh-pages-branch.html), here's the simplest way to do it.

- [Create the repository](https://github.com/new)on github.
- Create your local repository and `git commit`into it.
- Type `git push -u origin master:gh-pages`
- In `.git/config`, under the `[remote "origin"]` section, add `push = +refs/heads/master:refs/heads/gh-pages`

The magic is the last :gh-pages.
