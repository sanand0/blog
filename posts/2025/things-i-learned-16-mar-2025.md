---
title: Things I Learned - 16 Mar 2025
date: 2025-03-16T00:00:00+00:00
categories:
  - til
description: I explored low-cost robotics like SO-ARM100, optimized Docker images with multi-stage builds, and adopted Marp for Markdown slides. I also investigated Model Context Protocol (MCP) workflows and techniques for serving structured content to LLM agents.
tags: [docker, marp, model-context-protocol]
---

This week, I learned:

- Here is a [training program on open source corporate policy](https://todogroup.org/resources/training/).
- [htmlq](https://github.com/mgdm/htmlq) and [pup](https://github.com/ericchiang/pup) query HTML. They're like `jq` for HTML.
- Here are time-tested and robust ways to leverage serendipity: [ChatGPT](https://chatgpt.com/share/67d4df37-d30c-800c-bf25-e33f94dc53b0)
  1. **Place**. Be in places with high, diverse, talent density. Bell Labs (1950s), MIT (1970s), Pixar (1990s).
  2. **People**. Meet diverse, talented people. Da Vinci's Renaissance circles, Lockheed Martin's Skunk Works.
  3. **Free time** for unstructured work. 3M's 15% rule, Google's 20% time, Edison's Invention Factory.
  4. **Curiosity**. Learn unrelated fields. Darwin's earthworm research, Ben Franklin's ocean currents work.
  5. **Serendipity**. Systematically add randomness. Brian Eno's Oblique Strategies, IDEO's Deep Dives.
  6. **Reframe failure** as opportunities. Penicillin, Velcro, Post-it Notes.
  7. **Ceremonies**. Hackathons, lightning talks, coffee trials.
- What makes client-side computing on the browser powerful is
  - There's nothing to install
  - Private by default: data stays with client
  - Speed: no latency
- [SemGrep](https://semgrep.dev/) is a lot less open source than it used to be. [ChatGPT](https://chatgpt.com/share/67d525e5-eea0-800c-a382-4aa5a19b609d). That's a pity. It was a good tool.
- Site builders and headless CMSs are gently eating into the dominant market share of open source CMSs (via [PretaGov](https://www.youtube.com/live/dXhHtsW8qjo?si=WiEuwrxiyoaQ3D2Y&t=2460)).
  - WordPress is pretty much the dominant CMS in the world, followed by Drupal.
  - WordPress is now VC backed and is not growing, so they seem to be attacking their own community.
  - Umbraco CMS is the only open source CMS that's growing. Maybe because it's the only .NET one
  - Craft CMS is the only proprietary CMS that's growing.
  - Site builders are growing as a category. SquareSpace is the leading one.
  - Headless CMS is growing too. Statamic. Next.js. Nuxt.js, Contentful, Prismic, Storyblok, Gatsby, etc.
- Here's a [sample CI/CD pipeline with automated code review](https://gitlab.com/kitarp29/buaji/-/jobs/8416107396).
  - [Here is the script that generated it](https://gitlab.com/kitarp29/buaji/-/blob/e9211bd619bd238f4b32c4a3509b78c199937f8d/.gitlab-ci.yml#L84-113).
  - Note the use of [NVIDIA's GPU Docker containers](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/) via `nvcr.io`
- Things I learnt about robotics.
  - [SO-ARM100](https://github.com/TheRobotStudio/SO-ARM100) is an open-source 3D printable robot arm. Takes ~20 hours to print, ~1 hour to assemble. Costs ~$120.
  - [LeKiwi](https://github.com/SIGRobotics-UIUC/LeKiwi) is a mobile version of this arm
  - [LeRobot](https://github.com/huggingface/lerobot) is a set of HuggingFace models and datasets. The idea is, you can use one "control" robot to control the other. Do stuff manually, teach it ~50 times, and it learns how to do what you're do.
  - [Pi0](https://huggingface.co/blog/pi0) is an LLM equivalent for robotics that predicts actions. HuggingFace ported that to LeRobot
  - Most real robotics work is on SIMILATED "gym" environments, not costly/slow physical environments.[PushT](https://github.com/huggingface/gym-pusht) is a simple 2D version. [ALOHA](https://github.com/huggingface/gym-aloha) is a 3D one.
  - [ROS](https://www.ros.org/) is a nightmare to install and run - on Windows _and_ Mac.
  - [Robotics Academy](https://jderobot.github.io/RoboticsAcademy/) is an open collection of easier ROS exercises.
  - [PSLab - Pocket Science Lab](https://pslab.io/) is a sensor kit for the phone / PC. Costs ~$100 but isn't available anywhere. Getting it to work requires too much mucking around with USB drivers and it just doesn't work. (BBC [micro:bit](https://microbit.org/) may be more promising.)
  - Getting stuff done with electronics is still _really_ hard unless it's well designed.
  - It's FASCINATING that robots can have arbitrary joints. Our intuitions (or even biomimicry) on how to move and do stuff is a POOR intuitive guide for how robots should act.
- MathML Core is a language _and_ layout specification, distinct from MathML 2/3. It's not fully compatible with JATS XML.
  - [`latexmlmath`](https://tmke8.github.io/math-core/) converts TeX to MathML.
  - `m|math { font-family: "Noto Sans Math", "Noto Sans" }` is a popular OpenType Math font. Browsers default to native fonts: e.g. Cambria Math on windows. Explore at <https://fred-wang.github.io/MathFonts/>.
  - The people working on this at arXiv are: Deyan Ginev, Fred Wang, and [Norbert Preining](mailto:norbert@arxiv.org). Their work is sponsored by NSF.
- There's a [PDF UA2](https://pdfa.org/iso-14289-2-pdfua-2/) standard for accessibility but there aren't enough tools to generate it.
- LibreOffice is now on WASM. [ZetaJS](https://www.npmjs.com/package/zetajs) provides office in the browser. Has a CDN (that was down from our IP). 35M packaged binary. 100M of in-memory file-system loaded.
  - Useful for: Document conversion, Thumbnail generation, Text extraction, Merging / splitting documents
- The [Poincare Conjecture](https://en.wikipedia.org/wiki/Poincar%C3%A9_conjecture) says that any finite 3D blob with has no holes can be deformed into a sphere. It took until 2003 to prove it because we didn't have the tools to manipulate 3D shapes.
- Playbook driven agents are another approach to agentic workflows. [Simon Willison](https://simonwillison.net/2025/Mar/13/xata-agent/)
- [Twine](https://twinery.org/) ([docs](https://twinery.org/reference/en/index.html)) is an open source interactive fiction / story writing tool.
  - [Snowman](https://videlais.github.io/snowman/) is a browser-based Twine 2 story template format.
  - These enable behavioural experimentation. Cheaper than using tools like [Gorilla.sc](https://gorilla.sc/) and [Pavlovia](https://pavlovia.org/) for behavioral experiments
  - For example, you can present a social or political issue and see if people change their opinions more or less depending on the content/path they see. Or, if it varies by demographics. Or, check if repeated mentions or emotional hooks improve memory / retention. [More research ideas](https://chatgpt.com/share/67d3fe6f-aff4-800c-bb02-2cb72d8f6e16)
- Techniques to reduce Docker image sizes:
  - Native Linux `mount` supports overlaying directories! Lower layer is read-only. Edits (including deletions) affect upper layer only. Docker uses this. `docker image inspect` shows layers.
  - Always run `RUN apt-get update && apt-get [packages]` rather than in separate lines. Else `RUN apt-get update` gets cached with OLD update cache.
  - Defer `COPY` till as late as possible, and COPY _minimally_ - since it typically invalidates the cache.
  - Skip development dependencies and temporary caches.
  - Docker Dive via `dive [IMAGE]` analyzes image details and shows the file system in each layer.
  - Use multi-stage builds. A: Create an image using `FROM some-image AS builder` and do what you want. Then, after that, B: `FROM scratch` (or `FROM node:22-slim`) use `COPY --from=builder what-you-want`.
  - Use [distroless images](https://github.com/GoogleContainerTools/distroless) from GCR. It doesn't have shells, package managers, etc. Fewer vulnerabilities.
- [Playwright](https://playwright.dev/) seems to be the emerging standard for modern browser testing/automation, beating [Cypress](https://www.cypress.io/) and [Selenium](https://www.selenium.dev/).
- "Openwashing" is a term where something is termed open source but is not.
- [Photos from FOSSASIA](https://drive.google.com/drive/folders/1Bk9vILFYUjqxS2jHxBvY148yWSuC5WWm) are public.
- To publish images long-term
  - [GitHub](https://github.com/) is an option. Likely to last long-term. Clone-able.
  - [Archive.org](https://archive.org/) is a good too but may suffer from bandwidth constraints.
  - [Imgur](https://imgur.com/) remains popular but it's unclear if it will remain unrestricted.
  - [Flickr](https://flickr.com/) has had a flaky history with limits and commercialization.
  - [WikiMedia Commons](https://commons.wikimedia.org/wiki/Special:UploadWizard) deletes personal uploads by first-time contributors. Only files _clearly_ useful for a large audience are retained.
- This [table of LLM API data protection](https://www.rosenthal.ch/downloads/VISCHER_ai-tools-03-25.pdf) lists what use cases each provider's terms of service allow from a security perspective.
- [Unsloth](https://unsloth.ai/) might be one of the simplest ways of fine-tuning.
- For LLM UIs, [Open Web UI](https://github.com/open-webui/open-webui) seems most popular. Run via `WEBUI_SECRET_KEY=... uvx --python 3.11 open-webui serve`
  [Text generation Web UI](https://github.com/oobabooga/text-generation-webui) is less so.
  [KoboldAI](https://github.com/KoboldAI/KoboldAI-Client),
  [LMQL](https://github.com/eth-sri/lmql),
  [LM Studio](https://lmstudio.ai/),
  GPT4All, etc are far behind.
- GPT 4o Mini is probably a 8b parameter model. [Ref](https://aiexpjourney.substack.com/p/the-number-of-parameters-of-gpt-4o)
- "SRM"s are Small Reasoning Models - like Small Language Models. Phi-4 and DeepScaleR are SRMs. Gemma 3 is a multi-modal SLM.
- [`gemini-embedding-exp-03-07`](https://developers.googleblog.com/en/gemini-embedding-text-model-now-available-gemini-api/) leads the [MTEB](https://huggingface.co/spaces/mteb/leaderboard) and is currently the top embedding model by a big margin.
- [Apify](https://apify.com/) is a cloud scraper platform. Here's how they optimize their [AI Web agent](https://apify.com/apify/ai-web-agent) - [Source](https://github.com/apify/actor-web-automation-agent):
  - Remove redundant tags and attributes (e.g. accessibility, etc.). Explore readability.
  - Add a unique `gid` to each element.
  - Add the screenshot WITH a "Set of Marks" - "SoM" (read research paper) highlighting important clickable elements.
  - Code output is brittle. Use tools / DSL - e.g. visit_url(url), click_element(text, gid, tagName), etc.
- [GenAIScript](https://microsoft.github.io/genaiscript/) increasingly looks like a promising way to automate LLM workflows in the browser.
- [Ollama has a Windows download](https://ollama.com/download/windows)
- [Marp](https://marp.app/) is my new favorite way to generate slides from Markdown. Reveal.js is not easy with Markdown (though HTML works well.)
  - The [VS Code plugin](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode) makes development very easy
  - [Marp CLI](https://github.com/marp-team/marp-cli/) makes deployment easy.
  - I used it for my talk on [LLM Hallucinations](https://sanand0.github.io/llmhallucinations/) ([source](https://github.com/sanand0/llmhallucinations/)).
  - Supports all [bespoke](https://github.com/bespokejs/bespoke) features and [plugins](https://www.npmjs.com/search?q=keywords:bespoke-plugin)
  - [Transitions](https://github.com/marp-team/marp-cli/blob/main/docs/bespoke-transitions/README.md). Requires OS animation effects to be enabled
  - [Animated SVG backgrounds](https://www.svgator.com/blog/animated-svg-backgrounds-examples/) are a good add-on.
- A mental model to consider is: each chat conversation with an LLM is a person or a personality in itself. A day in the life of a model, where its personality evolves.
- Bots need structured content (e.g. Markdown, XML). Humans need rich content (e.g. HTML). Here are 4 ways to serve both, roughly in increasing order of sophistication:
  1. **Different URLs**. E.g. https://example.org/about/ vs https://example.org/about.md (this is how Jekyll or Hugo work). Use for static sites generators.
  2. **JavaScript**. Inject after Markdown: `<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script><script>document.body.innerHTML = marked(document.body.textContent);</script>`. Use for dynamically generated static sites.
  3. **URL query parameters**. E.g. `?format=markdown` vs `?format=html` vs `?format=json`. Use in APIs.
  4. **Content Negotiation**. Based on the user agent and `Accept` header, serve Markdown or HTML. Send `Vary: Accept` to indicate that the response depends on the `Accept` header. Use for dynamic web apps.
- Notes from The Knowledge Project: [Josh Wolfe: Human Advantage in the World of AI](https://fs.blog/knowledge-project-podcast/josh-wolfe-2/)
  - Agent optimization might become as popular as search engine optimization in the future.
  - APIs are likely to be replaced by just chat requests that will do the same thing.
  - APIs might be replaced by RPA, where somebody uses a chatbot to do the equivalence instead.
  - Today, blue-collar workers may be more protected from AI than white-collar workers. Robots still can't serve a meal well enough and aren't progressing as fast as AI yet.
  - There's a lot of tacit knowledge in craftsmanship that will take a long time for machines to replace.
  - Margins are fleeting. The only time you have large sustainable margins is when you truly have a monopoly.
  - Cost is going down so quickly right now that all you have to do is wait, and stuff will become available for a very affordable or even a free price.
  - The moat is really in the data. The models are not an advantage. Engineering and services on top of that are marginal.
  - Machines will be doing science 24/7. All of the science data that we have will probably be the biggest leverage for humanity.
  - The discovery of penicillin, Viagra, and rubber were all serendipitous. Machines should run with a little bit of randomness to benefit from this.
  - Tesla might have gotten away with accounting fraud on warranty claims. But short sellers are likely to be after Elon Musk.
  - With LLMs, the value of our social network has gone up considerably. Remember: The reason we believe things is not because we have thought through and analyzed them. It's because the people around us believe in those things.
  - It is now practical for a person to live on forever by sharing all their thoughts into an LLM. Kids can have a "Dad AI".
  - One good use of meeting recordings is to see where there are biases in the conversations and where the engagement is not high enough or how there are unproductive power balances.
  - A great virtue of college is that it allows you to break free from your previous personality. For those four years, nobody knows who you are or cares what you wear. And you can be or grow into a very different person. The more content we put in into AI or social media, the harder it is to change ourselves.
- People are reporting that [Roo Code](https://github.com/RooVetGit/Roo-Code) is better than Windsurf.
  - Roo Code is open source. Available as a VS Code extension and run-nable via `git clone`
  - Roo Code supports Computer Use. It can read files, take screenshots from a built-in browser, controls it, and reads browser console logs.
  - Opinions are mixed. A team member reported that it takes 10 LLM queries to do what Cursor does in 2. Another reported that it does in 1 query what Cursor does in 2.
- Notes from [Thursday AI, 6 Mar 2025](https://youtu.be/rXoGpUyD1Jg)
  - Google's AI overviews now use Gemini 2.0. They've introduced an AI mode that functions like a mini deep research tool, incorporating planning and search. (A Perplexity-killer). It's a fine-tuned model that is extra cautious with topics like healthcare and always verifies information.
  - QWQ from Quen competes with DeepSeq R1, but with only 32b parameters compared to R1's several hundred billion.
  - AI models are becoming less restrictive. Gemini and GPT-4.5 have relaxed some constraints, shifting more responsibility onto users, similar to Grok.
  - What's GPT-4.5 good for? It seems to excel in creativity, humor, education, emotional intelligence, and teaching. It follows instructions better and understands intent better. However, it's not a major leap in coding or math.
  - OpenAI's Deep Research mode always uses O3, regardless of the model selected in the UI.
  - Tencent has released a new video model available at <https://aivideo.hunyuan.tencent.com/> and it appears to be quite good.
  - Many _clients_ now support Model Context Protocol (MCP), including Cursor, Claude Code, and Claude Desktop. The [clients](https://modelcontextprotocol.io/clients) list is long. Some MCP uses include:
    - Interact with GitHub using the GitHub API.
    - Using Knowledge Graph memory to premember previous conversations
    - Using the Cloudflare MCP server to perform Cloudflare actions.
    - File retrieval and custom prompts -- which MCP supports in addition to tools.
    - Calling other MCPs or LLMs (conditionally) from an MCP, enabling the creation of full-fledged workflows.
  - Composio offers a [Hosted MCP service](https://docs.composio.dev/mcp/overview). CloudFlare lets you build [remote MCP servers](https://blog.cloudflare.com/model-context-protocol/).
  - [Notagen](https://electricalexis.github.io/notagen-demo/) is an open-source note generation engine that produces high-quality classical sheet music.
  - [Sesame](https://www.sesame.com/research/crossing_the_uncanny_valley_of_voice) has an [open-source](https://github.com/SesameAILabs/csm) voice model worth exploring.
  - [DiffRhythm](https://github.com/ASLP-lab/DiffRhythm) is a music generation model that appears to be quite good.
- 2 pass bounding box approach. Have an LLM generate bounding boxes. Then fix it. [Ethan Mollick](https://bsky.app/profile/emollick.bsky.social/post/3ljt3gk3i422u)
- `uv tool install` and `uv tool ensure-path` are useful commands for installing and ensuring path for tools. [Simon Willison](https://til.simonwillison.net/jupyter/jupyterlab-uv-tool-install)
