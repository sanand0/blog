---
title: How to review trending GitHub repos on VS Code
date: "2025-09-27T13:17:50Z"
lastmod: "2025-09-27T13:17:52Z"
categories:
  - coding
  - how-i-do-things
wp_id: 4217
---

![How to review trending GitHub repos on VS Code](/blog/assets/trending-repos.webp)

Here’s how I track trending [GitHub](https://github.com/) repos each week. I run a [scheduled script](https://github.com/sanand0/til/blob/43628ba72400451d20076df12dec823f08482c5b/trending-repos.sh) that saves a [clean TSV](https://github.com/sanand0/til/blob/43628ba72400451d20076df12dec823f08482c5b/trending-repos.tsv) I can scan fast.

It uses [`uvx gtrending`](https://pypi.org/project/gtrending) to fetch **weekly** trending repos for:

- **Rust**: High-quality system tools. (Anything in Rust seems cool.)
- **Go**: Reliable CLI/infra tools. (Like Rust, most Go code seems good.)
- **Python**: Most AI/ML stuff
- **TypeScript**: Most modern JS codebases
- **JavaScript**: Most front-end utilities
- **Shell**: Productivity scripts

I pipe results through [`jq`](https://jqlang.org/) to extract:

- **Language**
- **Stars**: for popularity
- **Current period stars**: for growth
- **Date**: when I run it
- **Full name**
- **Description**

I use [`awk`](https://en.wikipedia.org/wiki/AWK) to de-duplicate by repo and save into a [TSV file](https://github.com/sanand0/til/blob/main/trending-repos.tsv).

Then I review the TSV in [VS Code](https://code.visualstudio.com/). I stopped using Excel. [Rainbow CSV](https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv) and [Edit CSV](https://marketplace.visualstudio.com/items?itemName=janisdd.vscode-edit-csv) make large TSVs easy to scan, sort, and re-structure. (I'm quite excited at the new tricks I'm learning to replace Excel!)

I tag the first column with:

- 🟣 **pending**
- 🔴 **ignore** (with reason in the last column)
- 🟢 **active** (I currently use it)
- ⏺️ **review**

I picked these icons carefully. A **descending sort** puts 🟣 on top (to scan quickly) and ⏺️ at the bottom (for closer review). This also puts top-starred repos in each language first.

The payoff for the right tools is high. This process makes it easy. I found [Flameshot](http://flameshot.org/), [duf](https://github.com/muesli/duf) and [wrkflw](https://github.com/bahdotsh/wrkflw) this way.

To try it, download and run [`bash trending-repos.sh`](https://github.com/sanand0/til/blob/43628ba72400451d20076df12dec823f08482c5b/trending-repos.sh) and open the TSV it generates.
