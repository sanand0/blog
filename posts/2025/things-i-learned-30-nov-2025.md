---
title: Things I Learned - 30 Nov 2025
date: 2025-11-30T00:00:00+00:00
categories:
  - til
description: I used tmux to run terminal agents, explored Anthropic's programmatic tool-calling features, and identified key human skills like taste and synthesis that grow more valuable as AI automates routine research and coding tasks.
keywords: [tmux, anthropic, terminal, gpt-5, duckdb, causality, realtime-api]
---

This week, I learned:

- Warp has a [terminal agent feature](https://www.warp.dev/blog/agents-3-full-terminal-use-plan-code-review-integration) - allowing Warp to control a terminal via text. I find that regular coding agents like Codex can do that too with tmux. For example, I opened a session and had Codex run commands in it while I watched. Here's the guidance it needed:
  ```bash
  # Create a new session
  tmux new-session -d -s $SESSION 'uv run --with pandas,httpx,lxml python -iqu'
  # Capture output to a log file
  tmux pipe-pane -t $SESSION -o "cat >> /tmp/$LOG"
  # Run a command
  tmux send-keys -t $SESSION 'print(1 + 2)' C-m
  # See output
  cat /tmp/$LOG
  # Capture the last 5 lines of the pane
  tmux capture-pane -p -t $SESSION -S -5
  ```
- Notes from [Early science acceleration experiments with GPT-5](https://cdn.openai.com/pdf/4a25f921-e4e0-479a-9b38-5367b47e8fd0/early-science-acceleration-experiments-with-gpt-5.pdf) - via [Claude](https://claude.ai/share/75507676-ce0c-4be2-b1da-c652336b2145)
  - LLMs are accelrating research because they are good at:
    - Literature search, especially across disciplinary boundaries
    - Generating and checking routine calculations
    - Proposing variations on known techniques
    - Identifying connections between disparate results
    - Producing first-draft code for well-specified problems
    - Explaining why certain approaches won't work
  - But they're curently struggling with the following - though it's a shrinking space
    - Genuinely novel conceptual leaps (but this is increasingly happening, e.g. Sawhney and Sellke's problem #848)
    - Recognizing when it's plagiarizing, e.g. when it "discovered" a proof for the Chevalley-Warning theorem which was copied from a Noga Alon paper - it wasn't conscious of this
    - Knowing what it doesn't know
    - Distinguishing important problems from unimportant ones
    - Understanding the "negative space" of mathematics (why certain problems are hard, why obvious approaches fail)
- Anthropic introduced three excellent [tool use practices](https://www.anthropic.com/engineering/advanced-tool-use) that I expect will be adopted widely.
  - [Tool search](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool): Don't pass the tool definitions to the model. Model can ask for a tool search when needed
  - [Programmatic tool calling](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling): Instead of calling a tool, it'll return a Python program to execute that will call the tools! This is a huge win
  - [Tool use examples](https://platform.claude.com/docs/en/agents-and-tools/tool-use/implement-tool-use#providing-tool-use-examples): Lets you specific examples of tool calls to guide th model better
  - The [Hacker News thread](https://news.ycombinator.com/item?id=46038047) flags that CLIs solve these - but CLI updates are hard, while APIs auto-update.
- With AI, some skills that beome more valuable are (and will soon be in short supply, hence need to be taught) are: [#](https://claude.ai/chat/68410b38-514f-4301-9c85-a9534a0cd7f8)
  - Problem formulation ("What question should we actually ask?")
    - Traits: Curiosity (absolutely), systems thinking, comfort with ambiguity, metacognition (thinking about your thinking)
    - Practice reframing exercises ("What are 5 other ways to frame this?"), study great questions in your field, work backward from outcomes, learn adjacent domains. The "5 Whys" technique helps. Also: deliberately pause before diving into solutions—force yourself to spend time in the question space.
  - Taste and judgment ("Is this response appropriate?")
    - Traits: Pattern recognition from experience, cultural literacy, empathy, contextual awareness, aesthetic sense
    - How to strengthen: Immerse yourself in excellent examples, study spectacular failures (they're more instructive!), get feedback on your calls, practice explaining why you made a judgment. Build a "swipe file" of great/terrible examples. The key is volume—you need lots of reps.
  - Quality assessment ("Is this AI output correct?")
    - Traits: Healthy skepticism, attention to detail, domain knowledge, logical reasoning, understanding of edge cases
    - How to strengthen: Study common AI failure modes, build verification checklists, practice the "does this make sense?" test, learn what "good" looks like in your domain, cross-reference claims. Develop your "bullshit detector" by analyzing why wrong answers feel wrong.
  - Creative synthesis ("How do these ideas connect?")
    - Traits: Associative thinking, wide knowledge base, playfulness, comfort with non-obvious connections, intellectual courage
    - How to strengthen: Consume diverse inputs outside your field, practice analogical thinking ("X is like Y because..."), use visual thinking tools like concept maps, study how innovations happen in other domains, give yourself permission to make weird connections. Read broadly—fiction, history, science.
  - Domain expertise ("Does this solution work in reality?")
    - Traits: Deep curiosity, persistence, willingness to get hands dirty, learning from failure, long-term commitment
    - How to strengthen: Deliberate practice on real problems, seek mentorship, study edge cases and failure modes, build things (don't just read about them), learn your field's history. The "10,000 hours" thing is real, but it's quality hours that matter.
  - Meta pattern:
    - Reflection loops: doing something, then analyzing why it worked/didn't.
    - Exposure to excellence: you can't develop taste without seeing great work.
- Some more new CLI tools I installed:
  - [`trash-cli`](https://github.com/sindresorhus/trash-cli): Alias `rm` to move files to trash instead of deleting permanently.
- After a week of seeing ligatures in [Fira Code](https://github.com/tonsky/FiraCode), all other fonts look ugly. My favorite ligatures: !== ==> =>> <--> (and every possible arrow) >= ||> ||- |- ...
- The first name, alphabetically (at least among Straive employees) is "Aabida" and the last is "Zyrene". Something I would never have discovered working in a smaller company.
- [chokidar-cli](https://github.com/open-cli-tools/chokidar-cli) is an easy way to run commands when files change, e.g. `npx -y chokidar-cli '**/*.js' -c 'npm run build'`
- [`npx -y mapscii`](https://github.com/rastapasta/mapscii) shows a map on the terminal. Not too useful, not maintained, but very interesting.
- [termsvg](https://github.com/MrMarble/termsvg) converts asciinema `.cast` files to animated SVG suitable for embedding in GitHub (e.g. via `mise x github:MrMarble/termsvg -- termsvg export file.cast --minify`). The animated SVG is ~10X larger than the .cast file. The GZipped size is fine but saving it as `.svgz` is not recognized by GitHub. In contrast, [agg](https://github.com/asciinema/agg), the official asciinema-to-GIF converter, creates .GIF files that are only 5X larger. The most efficient seems to be embedding via [asciinema.org](https://asciinema.org/)
- [`usql`](https://github.com/xo/usql) queries MySQL, Postgres, SQLite, MSSQL, Oracle, etc via a single interface. For example, `usql 'mysql://rfamro:@mysql-rfam-public.ebi.ac.uk:4497/Rfam' -c "SELECT * FROM clan limit 3;"`. But DuckDB is more versatile, IMHO.
  ```sql
  INSTALL mysql; LOAD mysql;
  ATTACH 'host=mysql-rfam-public.ebi.ac.uk port=4497 user=rfamro database=Rfam' AS rfam (TYPE mysql);
  SELECT * from rfam.Rfam.clan LIMIT 3;
  SELECT * FROM 'file.xlsx' LIMIT 3;
  SELECT * FROM 'file.csv' LIMIT 3;
  ```
- Autistic and allistic people just have different communication styles. Autistic people have no trouble understanding other autists. They just happen to be in a minority which makes it seem like they have a social deficit. [Conflict between Neurotypes](https://blog.izs.me/2025/11/ogc-4-conflict/)
- 1 second = 10 tokens for [OpenAI Realtime APIs](https://platform.openai.com/docs/guides/realtime-costs). 1 second = 25 tokens for [Gemini Live API](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/live-api/streamed-conversations#context_window)
  - 39 cents / hour on [GPT Realtime Mini](https://platform.openai.com/docs/models/gpt-realtime-mini) = 36 cents audio input + 3 cents text output
  - 139 cents / hour on [GPT Realtime](https://platform.openai.com/docs/models/gpt-realtime) = 115 cents audio input + 15 cents text output
  - 30 cents / hour on [Gemini 2.5 Flash Native Audio (Live API)](https://ai.google.dev/gemini-api/docs/pricing#gemini-2.5-flash-native-audio) = 27 cents audio input + 3 cents text output
- Here are some AI experiments I'm planning to try with our marketing team:
  - **Video Generation**: Create marketing videos from text scripts in minutes
  - **Poster Generation**: AI designs high-conversion posters from brief text inputs - notably Nano Banana Pro
  - **Synthetic Persona A/B Testing**: LLM agents simulate 100K+ user behaviors to test designs before real users
  - **LLM-Powered A/B Automation**: AgentA/B system runs experiments with AI-simulated traffic
  - **Vibe Coding Landing Pages**: Marketers build production-ready pages in hours vs weeks
  - **On-demand Landing Pages**: Generate pages for automated campaigns/products without human intervention
  - **Brand Voice Cloning at Scale**: Train on company content to ensure consistency across 1000s of pieces
  - **Persona-Driven Content Synthesis**: Use 1B+ personas to generate diverse content perspectives
  - **Competitive Intelligence Briefing**: Real-time monitoring across millions of data points + data storytelling
  - **Marketing Analytics with LLMs**: AI agents analyze complex datasets for insights
  - **Brand Compliance Checks**: Ensure all content meets brand guidelines automatically
  - **Autonomous Blog Squads**: AI agents identify trending topics / internal content, create data stories ready for review
- New skill unlocked: creating tutorials from talk proposals. I asked Claude to `Write a Malcolm Gladwell article based on this talk description to teach me the topic` and passed it this talk proposal: [Your Causal Parrot might be lying to you](https://hasgeek.com/fifthelephant/2025-winter/sub/your-causal-parrot-might-be-lying-to-you-FhpB6kWkM4AAkYqdYQSCpJ). The [story it wrote](https://claude.ai/share/56b9bf17-927b-43a4-9af6-9b14a8cb1944) is very engaging and informative!
  - LLMs "understand" causality because of training, but lack a world model to extrapolate to new situations.
  - Giving them tools to reason (e.g. causal models, sub-agents to explore root causes) will help.
- A cool Gemini 3 Pro hack: convert satellite imagery into stylized maps! [Bilawal Sidhu](https://x.com/bilawalsidhu/status/1991635734546284703)
- Running sub-agents in `tmux` helps avoid timeout cancellation, and hence allowing resuming [Peter Steinberger](https://github.com/steipete/agent-scripts/blob/main/docs%2Fsubagent.md)
