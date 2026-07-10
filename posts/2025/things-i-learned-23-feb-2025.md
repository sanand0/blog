---
title: Things I Learned - 23 Feb 2025
date: 2025-02-23T00:00:00+00:00
categories:
  - til
description: I explored Python 3.13’s GIL-bypassing sub-interpreters, Caddy’s automatic SSL, and generated 50 Deep Research reports with ChatGPT Pro. I also compared Snowflake to Databricks and switched my default search engine to Perplexity for faster inference.
---

This week, I learned:

- Remote Desktop may be the easiest way to have a Windows machine access files / screen from another Windows machine, even for home PCs.
- [Caddy](https://caddyserver.com/) sets up reverse proxies that get _automatic SSL certificates_ from [Let's Encrypt](https://letsencrypt.org/)!
- The [Nomic Embed v2](https://www.nomic.ai/blog/posts/nomic-embed-text-v1) blog post has an excellent visualization for embedding quality. It takes all Wikipedia disambiguation articles and shows them on a Nomic Atlas, embedded via Nomic Embed v2. It lets you toggle to OpenAI text-ada-002 which moves the topics far away. Visually, this is very convincing.
- Python 3.15 will enable UTF-8 mode by default. [PEP 686](https://peps.python.org/pep-0686/)
- Python 3.13 supports sub-interpreters to bypass the GIL. It's _quite_ like web workers. [PEP 554](https://peps.python.org/pep-0554/)
- The quickest way to change the `fish` prompt is `function fish_prompt; echo '> '; end`
- At PyConf Hyderabad, about 3 people had read a PEP. 1 had used the `match` operator. But 80% knew what a Vector DB was. 20% had used a Gemini API. That's how much traction LLM development is getting.
- The productivity benefit people report from using LLms is about 3X. [Ethan Mollick](https://bsky.app/profile/emollick.bsky.social/post/3li4a2jal322a)
- Soon, you'll be able to send an LLM to a virtual meeting on your behalf. It will talk like you. [Ethan Mollick](https://bsky.app/profile/emollick.bsky.social/post/3lif6r42fp226)
- Models tend to claim ignorance when you test them on topics they should avoid. But tend to answer when not being tested. Sneaky! [Ethan Mollick](https://bsky.app/profile/emollick.bsky.social/post/3lihsmpsqyk27)
- Mermaid has an [Architecture Diagrams Syntax](https://mermaid.js.org/syntax/architecture.html) (in beta) that's capable of creating elegant architecture diagrams with icons.
- [Blind](https://www.teamblind.com/) is an app that allows users to post anonymously. It's particularly useful to find honest negative feedback about (mostly US) companies.
- [Iconify.design](https://iconify.design/) is a single npm interface to most open source icon sets. It includes FontAwesome, Bootstrap, Material Design, and many others. [icones.js.org](https://icones.js.org/) is an alternate interface.
- Self-pity may have evolved as a signal for social support and reducing conflict, while also encouraging self-reflection and behavioral adjustment. But in modern contexts it may be maladaptive and lead to depression. [ChatGPT](https://chatgpt.com/share/67b74759-4cdc-800c-8250-2d1757c5e85c)
- Anecdotally, Grok 3 is very good for researching company information and latest news, particularly employee and customer sentiment. DeepSeek and Claude write more humanely than OpenAI. via Alberto Lopez Toledo, White Star Capital
- There's a [YCombinator Founder Directory](https://www.ycombinator.com/companies/founders) listing all founders of YC companies. At the moment, there are 8,628 founders. There's also a [co-founder matching tool](https://www.startupschool.org/).
- LLMs are impacting not just data queries but geospatial queries as well. Here's a good example of [Natural Language Geocoding](https://element84.com/machine-learning/natural-language-geocoding/).
- US companies typically pay employees every 2 weeks not every month.
- What's good about Snowflake? A few developers who explored it mentioned that:
  - Its ability to scale up compute automatically makes queries run faster.
  - "Time travel" allows you to see how data looked at any point in time and that is impressive and useful.
  - Live data sharing with access control without the need for ETL pipelines is useful.
  - Open-source competition: ClickHouse, Apache Druid, and Presto/Trino
  - DataBricks is a lakehouse and less a data warehouse. It's more about:
    - storing unstructured data (Snowflake prefers semi-structured: JSON, Avro, etc.)
    - running collaborative notebooks in Python, SQL, Scala, R (Snowflake encourages SQL)
- I subscribed to ChatGPT Pro mainly for DeepResearch. Here are the first 50 reports I generated:
  1. [`uv` Package Manager Overview](https://chatgpt.com/share/67b49a7b-a4c0-800c-a3dc-c5ab1ced23fe)
  2. [DuckDB Analytics Comparison](https://chatgpt.com/share/67b4abfa-37b0-800c-a6e4-23b6c12e38b6)
  3. [Rust vs Python / JavaScript](https://chatgpt.com/share/67b4f8eb-d1f4-800c-824d-f0ca65ed7f54)
  4. [Modern Data Engineering Course](https://chatgpt.com/share/67b4fbc7-e6bc-800c-b2aa-dbf21339c8fc)
  5. [LLM Code Migration Practices](https://chatgpt.com/share/67b50772-f4c8-800c-b20c-8dd04d1b5e69)
  6. [Cloud Cost Optimization Strategies](https://chatgpt.com/share/67b5f809-9a5c-800c-8472-1153b2e4c1ae)
  7. [LLM Coding Interview Tools Report](https://chatgpt.com/share/67b61969-2030-800c-99c2-8585b63aa392) (compare with [Perplexity](https://www.perplexity.ai/search/the-interview-coder-repo-https-g_k0T2DSQIuiWntUFjbyOg))
  8. [Text To Speech Engines](https://chatgpt.com/share/67b63db0-8720-800c-87c6-f0b42581d801)
  9. [Customer Service in Indian Public Sector Banks](https://chatgpt.com/share/67b74802-8b34-800c-9ea3-2972db4d80c6)
  10. [LLMs in Software Development](https://chatgpt.com/share/67b75104-28e4-800c-87b8-f9c3d41a2cc9)
      - Old version 1: [Gen AI in Software Development](https://chatgpt.com/share/67b7483a-5cd4-800c-a330-ba4a984b9248)
      - Old version 2: [Gen AI in Software Development](https://chatgpt.com/share/67b75215-12f4-800c-9f9f-04c1f105b304)
  11. [Leadership Training Content](https://chatgpt.com/share/67b750f2-8ea4-800c-9721-bb9abbd46b29)
  12. [Open-Source HTTP Servers](https://chatgpt.com/share/67bafb23-cf14-800c-9b76-65f11285ae3a). Caddy wins.
  13. [Deep Research Use Cases](https://chatgpt.com/share/67bf66b3-98b8-800c-8482-3ce42f100bb9)
  14. [Nagpur No-Parking Violations](https://chatgpt.com/share/67bf6c69-a5d0-800c-8a49-12a46f29fef9)
  15. [Data Science in Food Services](https://chatgpt.com/share/67bf6e2a-2db0-800c-9975-c6b3479fa279)
  16. [Deep Research Disruption to Research Firms](https://chatgpt.com/share/67bf7946-c80c-800c-8132-6f4018455a68)
  17. [LLMs in Design Thinking](https://chatgpt.com/share/67c3a676-c088-800c-bbdc-b638a99df50b)
  18. [EU Taxonomy Report Clarification](https://chatgpt.com/share/67c56f48-3a8c-800c-bf5f-b1eeb91a529c)
  19. [Shell Valuation Analysis Inquiry](https://chatgpt.com/share/67c6d513-8040-800c-bdc9-7d6d1bcd52f9)
  20. [LLMs in DSLs Research](https://chatgpt.com/c/67c7991d-0358-800c-b450-8e81819267a6)
  21. [Public API-Based Data Storage Options](https://chatgpt.com/share/67c7edad-bd78-800c-80a7-ed08dd97c1cf). Supabase wins.
  22. [Front-End JS Frameworks Analysis](https://chatgpt.com/share/67ca8963-f564-800c-ae06-54464b58cf1d)
  23. [Database Evaluation Guide](https://chatgpt.com/share/67ca8953-97a4-800c-baea-ad0de5836f12)
  24. [CSS Frameworks Evaluation Guide](https://chatgpt.com/share/67ca893e-6450-800c-bd0a-d6213f48c356)
  25. [CI/CD Tooling Ecosystem Report](https://chatgpt.com/share/67ca8920-dc3c-800c-bf56-6231a6028e70)
  26. [Color Names Count](https://chatgpt.com/share/67ca88ee-f568-800c-ad74-e38ae385e61c)
  27. [S Anand Biography](https://chatgpt.com/share/67cc36c7-0b20-800c-a3f4-56bada95cb7b). Meh, I know more about me, and it gets a few things wrong.
  28. [Cosmere Secrets Encyclopedia](https://chatgpt.com/share/67ce2e28-d3ac-800c-a55f-e51b1c27d9c2). This is the best. Deep Research is great if it's stuff I actually want to read, rather than just learn about.
  29. [DBT course](https://chatgpt.com/share/67ce4df7-4088-800c-94e7-8a3edb02a8f6)
  30. [Future of Coding AI](https://chatgpt.com/share/67ce4e10-2968-800c-b663-8842045c1626)
  31. [Claude Artifacts Use Cases](https://chatgpt.com/share/67ce4dcd-5cf8-800c-837c-6d05bd61822e). This is the only one that managed to get artifacts links correct. I used this for an article for The Hindu.
  32. [MCP Servers and Clients Research](https://chatgpt.com/share/67ce7ef2-ead8-800c-982e-e99c9527099b). Learnings:
      - Practically any "tool" can be an MCP server: file systems, APIs, codebases, browsers, collaboration platforms, memory, etc.
      - Most platforms have (or are) integrating MCP.
      - [Clients](https://github.com/punkpeye/awesome-mcp-clients): code editors, chat, and automation tools support MCP. GenAIScript is a good starting point.
      - [Tester MCP Client](https://github.com/apify/tester-mcp-client) is a browser-based test environment.
      - [mcp-cli-client](https://github.com/adhikasp/mcp-client-cli) is a CLI-based client
      - [mcp-chatbot](https://github.com/3choff/mcp-chatbot) is a chatbot client
  33. [Data Moats by Industry](https://chatgpt.com/share/67cfe129-69c8-800c-9bb8-f7db2955fa88)
  34. [Attorney Profile Research](https://chatgpt.com/share/67cfe021-a2d4-800c-abf8-0ca5d54c8a43)
  35. [Social Media Data APIs](https://chatgpt.com/share/67cfe2bb-0814-800c-8c5b-17442906fdcf)
  36. [Adobe Software Alternatives](https://chatgpt.com/share/67d11e8f-eac4-800c-bf23-960e3f18b4aa)
  37. [LLM Hallucination Visualization Techniques](https://chatgpt.com/share/67d3ba57-3cc0-800c-830e-a48b5d531e86)
  38. [API vs Self-hosting Cost Analysis](https://chatgpt.com/share/67d3b985-2df0-800c-b9a7-b04fd6e18042): Always use APIs, avoid self-hosting models.
  39. [AGI Preparation](https://chatgpt.com/share/67d6a803-3e6c-800c-a886-10fe1e4dc3b9)
      - AGI will emerge step by step. Knowing which step is next will help
      - AI native organisations will emerge in each of these areas. AI design agencies and AI creative Agencies being one example
      - Networking, empathy, leadership have more value now. So will human AI bridging roles (e.g. AI managers, AI consultants, ethics auditors)
      - What's the value of a human when technology can do everything better? How did this play out in drama (decay) or sports (centralization) or music (globalization)?
  40. [Modern digital note taking](https://chatgpt.com/share/67d6bd5d-af74-800c-a6d7-bc1829f03c26)
      - Voice note taking is the game changer
      - Automatically popping of notes based on context such as people places or conversations will be a thing
  41. [Local LLM Search Tools](https://chatgpt.com/share/67d79662-2be4-800c-93e7-376eb68ceecf)
  42. [Blog Post to research paper on copying - suggestions](https://chatgpt.com/share/67d7968f-b020-800c-b7e7-2b086546b032)
  43. [Linux Dev Migration Guide](https://chatgpt.com/share/67d83394-43bc-800c-8157-8d498290638f)
  44. [Raspberry Pi SIM options](https://chatgpt.com/share/67d8eefe-a1f4-800c-93d0-fbed732e14fb)
  45. [Linux Dev migration guide](https://chatgpt.com/share/67d83394-43bc-800c-8157-8d498290638f)
  46. [HTML to JATS conversion](https://chatgpt.com/share/67d907fe-e0f4-800c-a4ad-f7dcf5176a5d)
  47. [LLM context splitting strategies](https://chatgpt.com/share/67dbcb7e-ea68-800c-9613-310724fc06bf)
  48. [Strategy for AI services in Publishing](https://chatgpt.com/share/67dba1a0-f100-800c-b184-d611a96d8831)
  49. [Gemini multi model editing use cases by industry](https://chatgpt.com/share/67db9a58-7688-800c-a7c6-10e86ee49132)
  50. [Pharma Conference Participation Guide](https://chatgpt.com/share/67dd93d9-7c88-800c-815f-9a21b7b6ad28)
  <!-- #TODO
  - PDF extractors
  - Databases
  - Training material on:
    - Data governance and quality
    - Document content extraction
    - Agile digital transformation
    - Responsible AI?
    - D3-based data visualization?
  - Emerging trends and competitive intelligence in:
    - EdTech
    - Publishing
    - Analytics
  - Challenges faced by (a client) and potential strategies
  - Latest news about (a client)
  - Industry Whitepapers on: AI-driven data solutions, CI/CD implementations, vector databases, etc.
  - Insightful Blog Posts: Generate data-backed articles on emerging trends in content technology and data services, attracting a wider audience to Straive's platforms.
    -->
- I learnt what a [Memoji](https://www.youtube.com/watch?v=j2iMZaDclJg) is for the first time. An avatar that follows your facial expressions. Cool!
- Google shows US flight timings from [FlightView](https://flightview.com). Emperically, based on one data point (my UA-2168 which was delayed by 4 hours), it gets updates faster than [Flight Radar 24](https://www.flightradar24.com/) or [FlightAware](https://www.flightaware.com/) or [FlightStats](https://www.flightstats.com/).
- When comparing Indian graduates with their western counterparts, the Indian ones are often seen as:
  - 🟢 Theoretically sound
  - 🟢 Analytical & technical
  - 🟢 Academically disciplined
  - 🟢 Resilient under pressure
  - 🟢 Committed continuous learners
  - 🔴 Rote-learning oriented
  - 🔴 Limited independent inquiry
  - 🔴 Limited creative innovation
  - 🔴 Restricted practical exposure
  - 🔴 Poor communicators
  - 🔴 Low leadership / initiative
  - 🔴 Need structured guidance
  - 🔴 Struggle to network
- HuggingFace has a "Model tree" against each model that shows the model's ancestors and descendants. For example, as of now, [Deepseek R1](https://huggingface.co/deepseek-ai/DeepSeek-R1) has 75 adapters, 154 finetunes, and 23 quantizations.
- Perplexity is now powered by Cerebras, which makes their inference as fast as Google. [Source](https://cerebras.ai/press-release/cerebras-powers-perplexity-sonar-with-industrys-fastest-ai-inference). The speed is a big factor, and I've switched my default search engine from Google to Perplexity, at least for now.
- [Interview Coder](https://www.interviewcoder.co/) is a desktop app that offers live interview support for coding interviews. It's a transparent window that reads your screen and answers questions for you. (Given this, I think we need an _interviewer_ support system that tells interviewers what to ask!)
