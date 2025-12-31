---
title: Top 8 ways I use ChatGPT in 2025
date: "2025-05-24T03:31:44Z"
lastmod: "2025-05-24T03:31:46Z"
categories:
  - how-i-do-things
  - llms
wp_id: 4122
---

I extracted the titles of the ~1,600 conversations I had with ChatGPT in 2025 so far and classified it against the list of [How People Are Really Using Gen AI in 2025](https://hbr.org/2025/04/how-people-are-really-using-gen-ai-in-2025).

![](https://files.s-anand.net/images/2025-05-24-top-8-ways-i-use-chatgpt-in-2025.webp)

Here are the top 8 things I use it for, along with representative chat titles. (The % match in brackets tells you how similar the chat title is to the use case.)

- Improving code (clearly, I code a lot)
- Troubleshooting (usually code)
- Corporate LLM/Copilot (this is mostly LLM research I do)
- Generating code (more code)
- Generating ideas (yeah, I've stopped thinking)
- Simple explainers (slightly surprising how often I ask for simple explanations)
- Generating relevant images. (Surprising, but I think I generated a lot of images for blog/LinkedIn posts)
- Specific search (actually, this is mis-classified. This is where I'm searching for search engines!)

My classification has errors. For example, "Reduce Code Size" was classified against "Generating code" but should have been "Improving code". But it's not too far off.

Here's a list of representative chats against these use cases.

- Improving code (263):
  - PR Code Review Suggestions (64% match)
  - Assessor Code Review and Improvement (63% match)
  - Reduce Code Size (62% match)
- Troubleshooting (172):
  - Connector Error Troubleshooting (67% match)
  - DNS Resolution Debugging Steps (55% match)
  - Exception Handling Basics (47% match)
- Corporate LLM/Copilot (141):
  - LLM Integration in Work (57% match)
  - LLM Agents Discussion (56% match)
  - LLMs Learnings Summary (56% match)
- Generating code (113):
  - AI Code Generation Panel (58% match)
  - AI for Code Generation (58% match)
  - Reduce Code Size (54% match)
- Generating ideas (99):
  - Filtering Ideas for Success (54% match)
  - AI Demo Ideas (52% match)
  - Hypothesis Generator Name Ideas (52% match)
- Simple explainers (94):
  - Simple Public APIs (43% match)
  - Y-Combinator Explained Simply (41% match)
  - Prompt Engineering Tutorial Summary (39% match)
- Generating relevant images (93):
  - Popular AI Image Tools (54% match)
  - Diverse Image Embedding Selection (52% match)
  - AI ImageGen Expansion Ideas (52% match)
- Specific search (69):
  - Semantic Search Engines Local (59% match)
  - Enterprise Search Solution (54% match)
  - Local LLM Semantic Search (53% match)

How did I calculate this?

1. On ChatGPT.com, I scrolled until I had all 2025 chats visible. Then I pasted `copy($$(".group.__menu-item").map(d => d.textContent))` to get the chat titles.
2. On Claude.ai, I transcribed [this list of use cases](https://hbr.org/resources/images/article_assets/2025/03/W250310_SANDERS_AI_USES_610-1071x2048.png) from HBR (prompt: "Transcribe this image").
3. On [LLM Foundry](https://llmfoundry.straive.com/classify) (which you may not have access to), I used the [Similarity API](https://llmfoundry.straive.com/help/similarity) to get a CSV of similarities between prompts and top 30 use cases in 2025 using [text-embedding-3-small](https://platform.openai.com/docs/models/text-embedding-3-small).
4. On ChatGPT.com, I [told it to analyze the data](https://chatgpt.com/share/68313aed-d5b4-800c-a8cf-c6566f3b9319) like this:

> This sheet has the embedding similarity between my ChatGPT prompts (in column "A") with different use cases.
>
> Write and run code that tags the prompt with the use with the highest embedding similarity (cell value), drops prompts whose highest embedding similarity is below a cutoff, and shows a table where the rows are the use cases and the values are the frequency. Do this for multiple embedding cutoffs as columns: 0.0, 0.1, 0.2, 0.3, 0.4. So, the table has use cases in rows, embedding cutoffs in columns, and the cell values are the count of prompts tagged with each use case AND have an embedding similarity >= cutoff. Draw this as a heatmap with low numbers as white and high numbers as green.

… and then:

> Let me download this as a Markdown list in this style, sorted by descending order at cutoff = 0
>
> - Anti-trolling (mention count of matches at 0 cutoff):
> - Tor Technical AMA questions (34%)
> - Bot Message Edits (33%)
> - Popular Hacker News Keywords (33%)
> - …

Here's the full list against the top 30 use cases:

- Improving code (263):
  - PR Code Review Suggestions (64% match)
  - Assessor Code Review and Improvement (63% match)
  - Reduce Code Size (62% match)
- Troubleshooting (172):
  - Connector Error Troubleshooting (67% match)
  - DNS Resolution Debugging Steps (55% match)
  - Exception Handling Basics (47% match)
- Corporate LLM/Copilot (141):
  - LLM Integration in Work (57% match)
  - LLM Agents Discussion (56% match)
  - LLMs Learnings Summary (56% match)
- Generating code (113):
  - AI Code Generation Panel (58% match)
  - AI for Code Generation (58% match)
  - Reduce Code Size (54% match)
- Generating ideas (99):
  - Filtering Ideas for Success (54% match)
  - AI Demo Ideas (52% match)
  - Hypothesis Generator Name Ideas (52% match)
- Simple explainers (94):
  - Simple Public APIs (43% match)
  - Y-Combinator Explained Simply (41% match)
  - Prompt Engineering Tutorial Summary (39% match)
- Generating relevant images (93):
  - Popular AI Image Tools (54% match)
  - Diverse Image Embedding Selection (52% match)
  - AI ImageGen Expansion Ideas (52% match)
- Specific search (69):
  - Semantic Search Engines Local (59% match)
  - Enterprise Search Solution (54% match)
  - Local LLM Semantic Search (53% match)
- Adjusting tone of email (66):
  - Email transcription request (45% match)
  - Summarize emails request (45% match)
  - Intro Email FAQs (44% match)
- Generating a legal document (59):
  - LLM Generated SVG Ideas (48% match)
  - LLMs for DSL Generation (45% match)
  - Deterministic Random Content Generation (45% match)
- Preparing for interviews (43):
  - LLM Coding Interview Tools Report (43% match)
  - Bank Ops Prep Resources (42% match)
  - AGI Preparation (42% match)
- Personalized learning (32):
  - Lifelong Learning in Conversations (51% match)
  - AI Classroom Engagement Names (48% match)
  - LLM Learner Personas Roadmap (47% match)
- Explaining legalese (32):
  - LLM Coding Insights (46% match)
  - LLM Code Ownership (45% match)
  - LLM Data Format Comparison (44% match)
- Creating a travel itinerary (28):
  - Travel Strength Training Tips (39% match)
  - User Journey Tools Online (37% match)
  - Prioritize My Explorations (36% match)
- Creativity (28):
  - Creative Process Breakdown (55% match)
  - Creative Hallucinations in Innovation (50% match)
  - Leveraging Serendipity for Innovation (50% match)
- Cooking with what you have (26):
  - Vegetarian Dish Creation (45% match)
  - Baked Veggie Dishes (41% match)
  - Vegetarian dish idea (40% match)
- Organizing my life (24):
  - Prioritize My Explorations (49% match)
  - Workspace Suggestions for Browsing (39% match)
  - Editing for Clarity and Simplicity (39% match)
- Enhanced learning (23):
  - 2025 LLM Embedding Enrichment (51% match)
  - Lifelong Learning in Conversations (49% match)
  - Tech-Enhanced Teacher-Student Rapport (49% match)
- Finding purpose (21):
  - Prioritize My Explorations (40% match)
  - Deep Research Use Cases (37% match)
  - Filtering Ideas for Success (36% match)
- Deep and meaningful conversations (20):
  - Lifelong Learning in Conversations (49% match)
  - Humorous conversation summary (42% match)
  - New chat (40% match)
- Healthier living (18):
  - Modeling Quality of Life (40% match)
  - Lifelong Learning in Conversations (37% match)
  - Posture and Breathing After Weight Loss (36% match)
- Anti-trolling (18):
  - Tor Technical AMA Questions (34% match)
  - Bot Message Edits (33% match)
  - Popular Hacker News Keywords (33% match)
- Writing student essays (18):
  - Scholarship Answer Advice (47% match)
  - Student Q&A on LLMs (41% match)
  - Reward Systems for Students (41% match)
- Fun and nonsense (17):
  - Humorous conversation summary (45% match)
  - Funny Llama 3.3 Strips (40% match)
  - Synonyms for Interestingness (40% match)
- Boosting confidence (14):
  - Emotional Prompting Impact (41% match)
  - Emotional Prompting Impact (41% match)
  - AI Ratings of My Flaws (38% match)
- Personalized kid's story (14):
  - Fake Data Storytelling Tips (43% match)
  - Low Effort Storytelling Training (39% match)
  - Demo Name Suggestions (37% match)
- Reconciling personal disputes (12):
  - Divorce AI Podcast Ideas (37% match)
  - Summarizing Personal Journals LLM (36% match)
  - Hobby Suggestions and Devil's Advocacy (36% match)
- Entertaining kids (9):
  - Comedy for Geriatric Doctors (40% match)
  - Humorous conversation summary (36% match)
  - Indoor Activities in SG (34% match)
- Medical advice (9):
  - Patient Doctor Communication Tips (41% match)
  - AI Training for Doctors (40% match)
  - AI Training Course for Doctors (38% match)
- Therapy/companionship (3):
  - DBT Course (36% match)
  - Cupping Therapy Evidence (36% match)
  - Empathy App Development Ideas (33% match)
