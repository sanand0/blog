---
title: Things I Learned - 19 Oct 2025
date: 2025-10-19T00:00:00+00:00
categories:
  - til
description: I explored Cloudflare's Sandbox feature, the HTML output element, and moreutils CLI tools like sponge. I also dug into SVG arc syntax, AI coding agents, and the 2025 State of AI Report's notes on reasoning models.
tags: [html, svg, ai-agents, gemini, uv]
---

This week, I learned:

- ⭐ "... most engineers don’t have public commits. Senior engineers at large tech companies don’t work on open-source projects for the most part." [Why AI Can't Do Hiring](https://interviewing.io/blog/why-ai-cant-do-hiring)
- Cloudflare's [Sandbox](https://sandbox.cloudflare.com/) feature in their Workers looks impressive. It supports streaming, web access to the container, and long-running processes. So we can spawn off a task and have it run a server (at least for a while) or a scraper.
- Gemini API has a Google Maps tool that it can refer to - like Google Search. [Maps Grounding](https://ai.google.dev/gemini-api/docs/maps-grounding)
- Earlier we needed humans to label data for RLHF. Now we don't since AI can simulate it. This is a pattern. Once AI learns from a human, that human skill can be automated. [How GPT-5 Thinks — OpenAI VP of Research Jerry Tworek](https://youtu.be/RqWIvvv3SnQ)
- The [`<output>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/output) element has a `for=` attribute indicating which `<input>` elements it is linked to and a `form=` attribute indicating which form it belongs to. This [works well with screen readers](https://denodell.com/blog/html-best-kept-secret-output-tag). A good reason to use it more. [Examples](https://rud.is/drop/output.html).
- Meta built a [Code World Model](https://ai.meta.com/research/publications/cwm-an-open-weights-llm-for-research-on-code-generation-with-world-models/). Basically an LLM that acts like a Python interpreter!
- `sudo apt install moreutils` installs a set of useful packages:
  1. **chronic**. Runs a command quietly (suppressing output) unless it fails — good for cron jobs where you only want noise on errors. `chronic backup.sh`
  2. **combine**. Combines lines from two input streams/files using boolean operations (AND, OR, XOR). `combine AND fileA fileB`
  3. **errno**. Look up symbolic names, numeric codes, and descriptions for standard errno values. `errno -l; errno ENOENT; errno 2`
  4. **ifdata**. Query network interface properties (IP, byte counts, errors) in a script-friendly format. `ifdata -sip eth0; ifdata -bops eth0`
  5. **ifne**. Run a command only if stdin is not empty, passing the input through. `find . -name core | ifne mail -s "Core files found" admin`
  6. **isutf8**. Check whether a file or stdin is valid UTF-8. `isutf8 somefile.txt`
  7. **lckdo**. Run a command while holding an exclusive lock to prevent concurrent runs. `lckdo /var/run/mylockfile.cmd myscript.sh`
  8. **mispipe**. Pipe two commands, but return the exit status of the first one (useful in pipelines). `cmd1 mispipe cmd2`
  9. **parallel**. Run multiple commands in parallel, reading them from stdin or arguments. `parallel < jobs.txt`
  10. **pee**. Like `tee`, but sends stdin to multiple commands in parallel. `echo "foo" | pee cmd1 cmd2`
  11. ⭐ **sponge**. Soak up all input before writing to output — enables in-place edits safely. `sort file | sponge file`
  12. ⭐ **ts**. Prefix each input line with a timestamp. `tail -f logfile | ts`
  13. **vidir**. Edit a directory listing in your editor to rename, move, or delete files in bulk. `vidir ~/myfolder`
  14. **vipe**. Insert a text editor into a pipeline to manually edit streamed input before output. `cat file | vipe | wc -l`
  15. **zrun**. Transparently decompress compressed files before passing them to a command. `zrun cat file.gz`
- Despite 20 years of SVG experience, I learnt new things from [A Friendly Introduction to SVG](https://www.joshwcomeau.com/svg/friendly-introduction-to-svg/) and [A Friendly Introduction to Paths](https://www.joshwcomeau.com/svg/interactive-guide-to-paths/)
  - Setting a `<rect>` width/height or a `<circle>` radius to zero _removes_ the element instead of drawing a point.
  - There's no option to draw the stroke on the inside or outside of a shape/path. Only the center.
  - You can override a path's `pathLength` attribute to create a new internal scale for its length. It's unclear where I can use this.
  - `<path>` arcs have this syntax: `A [rx],[ry] [rotation] [large-arc-flag] [sweep-flag] [end-x],[end-y]`. SVG first fits an ellipse to these parameters and then draws the arc.
    - If `rx` and `ry` of an arc is too small to connect the points, the SVG spec scales up `rx` and `ry`.
    - `[large-arc-flag]=1` literally uses the larger arc of the fitting ellipse. This is less common.
    - `[sweep-flag]=1` its the ellipse to make the connecting arc go clockwise. `0` is anti-clockwise.
    - `[rotation]` is rarely used because we usually draw arcs and _then_ rotate them.
  - `stroke-linejoin` automatically flips from `miter` (sharp) to `bevel` (cut) if the sharp edge protrudes too long (e.g. small angles). Increasing `stroke-miterlimit` increases the cutoff (default: 4)
- ⭐ Always include a thoughtful gallery of examples with tools / libraries. This does more than showing what a tool can do.
  - It's use-case / domain transfer: showing **what** it's useful for in real life - opening ideas, suggesting workflows.
  - It's style transfer: showing **how** to use it.
- ⭐ Here's what expert AI coders increasingly focus on. [Thomas Dohmke](https://ashtom.github.io/developers-reinvented)
  - Delegation: context engineering agents for success; parallelizing.
  - Verification: efficiently reviewing and testing code/output; setting stop-points.
  - Expanding scope: instead of time saved as the metric.
  - Education: teaching AI-based coding, debugging, reviewing/testing.
  - Product management: combining requirements + UI design + architecture + engineering + deployment.
  - Cross-discipline: blending code with design, governance, finance, marketing, ... ("computational creators").
- Notes from Taylor's [How I'm using coding agents: October 2025](https://heytaylor.dev/posts/202510052056_how-i-m-using-coding-agents-october-2025/)
  - Left monitor: 2-4 desktops (e.g. work, side-project). Right monitor: things I always want available
  - Plan next task while first executes.
  - Use plan mode to write to a plan file.
  - Don't start big tasks if you have meetings scheduled soon.
- Recent open source package hack methods seem to work more because of people/process than systems ([Filippo](https://words.filippo.io/compromise-survey/)):
  1. Phishing the author
  2. Pull requests running unsafe code in CI
  3. Taking over expired domain / user ID
  4. Stealing long-lived tokens
- `uv run --python 3.14 --isolated --with-editable '.[test]' pytest` runs pytest on a local project with a specific Python version. [Simon Willison](https://til.simonwillison.net/python/uv-tests)
- Notes from the [State of AI Report 2025](https://docs.google.com/presentation/d/1xiLl0VdrlNMAei8pmaX4ojIOfej6lhvZbOIK7Z6C-Go/edit):
  - Reasoning models are more fragile. Irrelevant phrases make reasoning models spend _FAR_ more tokens and get wrong answers [#21](https://docs.google.com/presentation/d/1xiLl0VdrlNMAei8pmaX4ojIOfej6lhvZbOIK7Z6C-Go/edit?slide=id.g36532dfa542_1_5)
  - AI systems are able to teach experts new concepts [#41](https://docs.google.com/presentation/d/1xiLl0VdrlNMAei8pmaX4ojIOfej6lhvZbOIK7Z6C-Go/edit?slide=id.g38724ed57c0_1_0#slide=id.g38724ed57c0_1_0)
  - An environment providing feedback / rewards enables continuous learning [#52](https://docs.google.com/presentation/d/1xiLl0VdrlNMAei8pmaX4ojIOfej6lhvZbOIK7Z6C-Go/edit?slide=id.g379a362bd85_0_132#slide=id.g379a362bd85_0_132)
    - E.g. Multi-robot chemical labs at U.Liverpool and NCSU [#60](https://docs.google.com/presentation/d/1xiLl0VdrlNMAei8pmaX4ojIOfej6lhvZbOIK7Z6C-Go/edit?slide=id.g37cf129d69d_2_44#slide=id.g37cf129d69d_2_44)
  - RLHF has a fundamental flaw: humans reward sycophancy [#71](https://docs.google.com/presentation/d/1xiLl0VdrlNMAei8pmaX4ojIOfej6lhvZbOIK7Z6C-Go/edit?slide=id.g34531ae1448_0_79#slide=id.g34531ae1448_0_79)
  - We can read what people are typing from brain signals outside the skull [#73](https://docs.google.com/presentation/d/1xiLl0VdrlNMAei8pmaX4ojIOfej6lhvZbOIK7Z6C-Go/edit?slide=id.g377f1927a71_0_0#slide=id.g377f1927a71_0_0)
  - Model intelligence-to-price ratio doubles every ~6 months [#94](https://docs.google.com/presentation/d/1xiLl0VdrlNMAei8pmaX4ojIOfej6lhvZbOIK7Z6C-Go/edit?slide=id.g38918b607ca_0_426#slide=id.g38918b607ca_0_426)
  - The AI companies' valuations are also roughly doubling every ~6 months [#181](https://docs.google.com/presentation/d/1xiLl0VdrlNMAei8pmaX4ojIOfej6lhvZbOIK7Z6C-Go/edit?slide=id.g38918b607ca_0_750#slide=id.g38918b607ca_0_750)
  - OpenAI is offering Governments giga-watt campuses to run OpenAI models for citizens [#122](https://docs.google.com/presentation/d/1xiLl0VdrlNMAei8pmaX4ojIOfej6lhvZbOIK7Z6C-Go/edit?slide=id.g38918b607ca_0_199#slide=id.g38918b607ca_0_199)
  - A 1GW clusters costs $50bn capex and $11bn per annum [#130](https://docs.google.com/presentation/d/1xiLl0VdrlNMAei8pmaX4ojIOfej6lhvZbOIK7Z6C-Go/edit?slide=id.g3668e08c71a_0_66#slide=id.g3668e08c71a_0_66)
  - China has added ~10X the energy capacity as the US in 2024 [#146](https://docs.google.com/presentation/d/1xiLl0VdrlNMAei8pmaX4ojIOfej6lhvZbOIK7Z6C-Go/edit?slide=id.g34898aa15b3_0_0#slide=id.g34898aa15b3_0_0)
  - NVIDIA challengers are still far away [#161](https://docs.google.com/presentation/d/1xiLl0VdrlNMAei8pmaX4ojIOfej6lhvZbOIK7Z6C-Go/edit?slide=id.g3747fb01779_1_100#slide=id.g3747fb01779_1_100)
  - LLMs can "read between the lines" even if training data is censored [#268](https://docs.google.com/presentation/d/1xiLl0VdrlNMAei8pmaX4ojIOfej6lhvZbOIK7Z6C-Go/edit?slide=id.g38409c5a29e_1_1097#slide=id.g38409c5a29e_1_1097)
  - LLMs can pass information via hidden signals [#270](https://docs.google.com/presentation/d/1xiLl0VdrlNMAei8pmaX4ojIOfej6lhvZbOIK7Z6C-Go/edit?slide=id.g379453733bb_0_59#slide=id.g379453733bb_0_59)
  - Prediction: A major retailer reports >5% of online sales from agentic checkout. AI agent advertising spend hits $5B. [#304](https://docs.google.com/presentation/d/1xiLl0VdrlNMAei8pmaX4ojIOfej6lhvZbOIK7Z6C-Go/edit?slide=id.g38918b607ca_4_400#slide=id.g38918b607ca_4_400)
- [OpenAI's leadership guide](https://cdn.openai.com/pdf/ae250928-4029-4f26-9e23-afac1fcee14c/staying-ahead-in-the-age-of-ai.pdf) says:
  - Align
    - Explain **WHY** AI thoughtfully.
    - Set a goal, e.g. everyone uses ChatGPT 20 times/day (Moderna).
    - Use it yourself. Show how.
    - Have **business** leaders run AI sessions
  - Activate
    - Launch an AI skills proram
    - Set up an AI champions network
    - Encourage experimentation (dedicated time, workshops, hackathons, ...)
    - Link to performance evaluations
  - Amplify
    - Create an AI knowledge base
    - Share success stories (weekly)
    - Create internal groups (Teams, Slack, ...)
    - Celebrate AI wins
  - Accelerate
    - Unblock AI tools and data access
    - Simplify project selection. Quick feedback, clear priorities
    - Unblock projects with a cross-functional council
    - Give resources to successful teams
  - Govern
    - Publish a responsible AI playbook (what's safe to try)
    - Audit AI practices quarterly
