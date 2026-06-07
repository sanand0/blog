---
title: Things I Learned - 09 Mar 2025
date: 2025-03-09T00:00:00+00:00
categories:
  - til
---

This week, I learned:

- In Jan 2025, ChatGPT included images as part of their data chat export. They also have a 30 second limit for the export. As an extensive user, my export is about 1GB which takes well over 30 seconds to download. [Like many others](https://community.openai.com/t/chatgpt-data-export-too-big-feature-in-the-options/1080111) the export option pretty much doesn't work for me any more.
- Bharathi said மெல்லத் தமிழினிச் சாகும் in a poem that has been often quoted (and parodied). [Here's the context](https://www.tumblr.com/kuvikam/105265085187/%E0%AE%AA-%E0%AE%B0%E0%AE%A4-%E0%AE%9A-%E0%AE%A9-%E0%AE%A9-%E0%AE%B0-%E0%AE%AE-%E0%AE%B2-%E0%AE%B2%E0%AE%A4-%E0%AE%A4%E0%AE%AE-%E0%AE%B4-%E0%AE%A9-%E0%AE%9A-%E0%AE%9A-%E0%AE%95-%E0%AE%AE-%E0%AE%8E%E0%AE%A9-%E0%AE%B1).
- The [Zettelkasten note-taking method](https://www.goodnotes.com/blog/zettelkasten-method) proposes that you:
  - Capture: Write down every idea or piece of information on a separate note. Use your own words to ensure understanding.
  - Organize: Consolidate fleeting notes into permanent ones. Assign unique identifiers to each note for easy reference.
  - Connect: Link related notes to form a web of knowledge. This can be done with tags, references, or hyperlinks in digital systems.
  - Review: Regularly revisit your notes to strengthen connections and discover new insights.
- I agree with almost every point on this LinkedIn post on scoring candidates for AI roles. [Rob Balian](https://www.linkedin.com/posts/robbalian_were-starting-to-use-a-points-system-when-activity-7303542581580156929-BrNG)
  - Uses DeepSeek R1 or Claude 3.7 +5 points
  - Uses Langchain -5 points
  - Uses Langgraph +5 points (I don't know enough to comment)
  - Built a RAG in 2023 +3 points
  - Built a RAG in 2025 -3 points
  - "pinecone" -5 points (I don't know enough to comment)
  - "What is cursor" - 50 points no coming back from this
  - Uses Cursor composer +10 points
  - "You don't need a full agent for this" +5 points
  - Did hackathons to learn AI outside of work +5 points
  - "We probably need to fine tune for this" -3 points unless you can explain why
  - "Gemini is making a comeback" +3 points (I have a soft spot for Gemini)
  - +3 points each for mentioning reasoning trace, structured outputs, MCP, chain-of-thought, prompt caching, TPM limits
- "Export to prompt" can be a useful feature in apps (or even as a bookmarklet). It would let you export content in an LLM-friendly Markdown format. You can paste it into an LLM and ask questions. Here are things I would find useful:
  - Copy an entire issue (with history) from GitHub, Gitlab, or JIRA
  - Copy an entire PR (with code changes) from GitHub, Gitlab, or Bitbucket
  - Copy CI/CD logs from GitHub Actions, Gitlab CI, Azure DevOps, etc.
  - Copy entire conversation thread in Gmail or Discourse, Service now etc.
  - Copy product reviews from Amazon, Shopify, etc.
  - Copy page(s) from wikis and content sites like Wikipedia, StackOverflow, etc.
  - Copy survey responses from Google Forms, Typeform, etc.
  - Copy all interactions with a contact (including interactions, proposal history) from HubSpot or Salesforce
  - Copy transcripts from Zoom, Teams, Google Meet, etc.
  - Copy as Markdown from Word, GDocs, PDF or HTML
  - Copy the summary of an analysis as well as all key metrics from any dashboard
  - Copy SAP invoices
  - Copy JDs, CVs, and reviews from Workday, BambooHR, DarwinBox, etc.
  - Copy design specs, component libraries, and style guides from Figma, Miro, etc.
  - [Generated with the help of ChatGPT](https://chatgpt.com/share/67b25a21-4164-800c-bf1b-ef218007fOa9) -- link not working
- Ancient languages tend to have fewer words for hues than brightness, since they didn't need them. So "Krishna was blue" or "the sea is wine-dark" is more an indication of darkness than shade of color. [Ajit Narayanan](https://www.quora.com/Why-is-Krishnas-complexion-depicted-as-blue-when-he-is-actually-black/answer/Ajit-Narayanan-1)
- Mistral released an [impressive OCR model](https://mistral.ai/fr/news/mistral-ocr).
  - [Marker](https://github.com/VikParuchuri/marker) from [DataLab](https://www.datalab.to/) seems [comparable](https://news.ycombinator.com/item?id=43285912) but is CC-BY-NC-SA.
  - [MinerU](https://github.com/opendatalab/MinerU) convert [medical textbooks to Markdown](https://news.ycombinator.com/item?id=43284248) well.
  - Gemini Flash may be more [cost effective](https://news.ycombinator.com/item?id=43283942) and [better](https://news.ycombinator.com/item?id=43287278)
- From [How I Write with Tyler Cowen](https://youtu.be/H1ztOoADp7M)
  - Keep researching. Use LLMs as an altemative to books and other reading material. Keep publishing what you learn regularly.
  - While reading a chapter, keep asking the LLM. What did you think of that? What just happened there? What should I focus more on? What's puzzling about this? How do I connect this to something else later or earlier in the book?
  - LLM is better used to support you rather than replace you in areas of your expertise. Where you are an expert it's best for you to be yourself and have AI fill in the gaps.
  - Ask the AI: "What is in my writing that some people might find obnoxious? Or cold / heartless? Explain it to me in great detail."
  - The first input is context setting and should be really long. Use voice dictation for that instead of typing.
  - Send your blog post to an LLM. No need to explain it. Just let it be the reader and see what it understands and doesn't understand.
  - His PhD students don't have a textbook, which saves them some money. But they are required to subscribe to a large language model which ends up costing less.
  - Today, it makes sense to use the best models and pay $200 for it if required. The differences are large. But in some years in the future, the cost of these models may come down for the free versions.
  - Humans know secrets. AI does not. So at least in some areas, humans will have an advantage.
  - Secrets full matter a lot more in the future. Gossip will matter a lot more. How good are you at keeping and trading secret? Travelling and meeting people will become more important. So will the value of social networks.
  - Since everyone has access to better intelligence, the value of mobilization or being able to _do_ things with people will have higher value. Leadership is an example. The value of your network therefore has gone up a lot.
  - There's more value in prompting one thing 10 times then 10 things one time. Follow up questions work better than long prompts.
  - There are so many AI note-takers (and transcribers) these days that you are not just writing for an AI but speaking for AIs as well!
  - Which model to use:
    - O1 Pro is the best model. Claude does a decent job. DeepSeek is full of hallucinations but is interesting. It is more imaginative.
    - Use O3 mini to write your prompt first, and _then_ ask the model
    - Use DeepSeek and other somewhat wacky high-end models once a day so that you stay in touch with what is models are capable of (beyond the conventional.)
    - Perplexity has entirely replaced Google for many people.
    - Anthropic's models are the best writers.
    - Gemini is good for long documents and hence for things like legal work. Gemini also has excellent YouTube integration and hands can directly read the transcripts.
    - Grok is very good at fact checking tweets.
  - Converting data into LLM consumable forms will be a huge project. Lot of a knowledge is not in such a form and a huge human project will involve this conversion.
- Indians do not need a visa to enter Thailand. [Ref](https://www.thaievisa.go.th/)
- Build apps (not just content) for agents. In the next 3 to 5 years, agents will surpass humans as the top product users.
- Reliably creating interactive tutorials is hard today. Claude 3.7 Sonnet ran out of tokens when I tried creating an interactive tutorial on diffraction. Cursor got the tokens but failed to get the application right after 3 attempts. This is not yet reliable, and when it does become reliable, education will change a fair bit. #IMPOSSIBLE
- Tools and solutions should fit within existing workflows. That means almost all capabilities need to be exposed as APIs.
- LLMs make many different kinds of errors that are useful to differentiate between. Here are a few
  - Model errors. The model itself makes a mistake. E.g. hallucinations, not following the prompt, etc.
  - Context errors. The model makes a mistake because the question was out of context, or the context was missing.
  - Input errors. The input to the model was parsed incorrectly, e.g. poor audio, poor image OCR, etc.
  - Tool errors. The model's tools are wrong or not good enough, e.g. Retrieval errors.
- Most browsers are moving away from third-party cookies. Here's [Google's recommendation on alternatives](https://developers.google.com/privacy-sandbox/cookies). The simplest of these is [CHIPS](https://developers.google.com/privacy-sandbox/cookies/chips), which requires adding a `Partitioned` cookie attribute.
- Notes from [AI Engineering Summit, NY, Day 1](https://youtu.be/L89GzWEILkM)
  - An agent requires 3 things: a router, tools or skills, and memory.
  - Agents are often sequential, but sometimes parallel execution makes sense for independent tasks that you consolidate.
  - Always allow LLMs the option of NOT answering a question if there is no good answer.
  - Focus prompts on the happy path. Use guard rails for edge cases.
  - Here are a few "tools" an agent would need to call:
    - Clarification from user
    - Saving to memory
    - Google search
    - Edit a file introducing SPECIFIC changes
    - Search in codebase using embeddings
    - Run scripts on the shell or in a REPL (Python, Node, etc.)
    - Run code in a new container for isolation
    - Automatically discover, read an API documentation and use it
  - Modify environment to enable logging and other system changes.
  - When code is cheap, you can explore more ideas and hence design and product management need to approach things differently. We also need to reaching testing completely because it makes very different kinds of mistakes and we don't often have an intuition
  - You can have an agent explore all the issues and full request and recent comments against the repository and summarise it for the project manager
- Notes from AI Engineering Summit, NY. Session by Lux Capital.
  - Agents make multiple LLM calls. Errors accumulate. So the quality of the model is key
  - What's really critical: data + context + user preference
  - Set up evals for subjective responses by collecting signals continuously.
  - Create scaffolding for agents where errors don't accumulate. Better yet, make it FIX errors
  - UX is critical. We need lots more UX styles
- [YayText](https://yaytext.com/) converts text to Unicode that has strikethrough, bold, italics, alternate fonts, and other interesting features. So does
  [Unitextify](https://unitextify.com/),
  [ConvertCase](https://convertcase.net/unicode-text-converter/), and
  [LingoJam](https://lingojam.com/BoldTextGenerator).
- [10 red flags I look for as an angel investor](https://www.linkedin.com/posts/jnpayne_10-red-flags-i-look-for-as-an-angel-investor-activity-7298357529967771649-IqdO) is an interesting read.
  1. **No real customers**: A deck, a landing page, and a "vision" don’t impress me. Show me paying customers. Even better, show me customers coming back.
  2. **No path to profitability**: I don’t care if you raise $100M -- if there’s no plan to make money, you’re just burning oxygen. Growth is great, but cash flow keeps you alive.
  3. **Founders who won’t sell**: If you’re scared to get on sales calls, that’s a red flag. The best founders sell in the early days -- whether it’s to customers, employees, or investors.
  4. **No differentiation**: "Like X, but cheaper" isn’t a strategy. If your only edge is price, you’ll get crushed. What do you have that no one else does?
  5. **No urgency**: The best founders operate like time is running out. If you’re "exploring ideas" or "thinking about raising next year," you’ve already lost.
  6. **Raising money before proving anything**: Too many founders try to fundraise their way out of bad ideas. If you need VC to get off the ground, you’re building the wrong business.
  7. **No clear distribution strategy**: Product alone doesn’t win. First-time founders obsess over features. Second-time founders obsess over distribution. How are you getting customers?
  8. **No ownership mentality**: If I hear "I need to hire someone to do that" too early, I’m out. Founders who win figure things out before they delegate.
  9. **A CEO who can’t attract talent**: Your first hires are everything. If great people aren’t willing to join, either the vision is weak -- or you are.
  10. **No skin in the game**: If a founder won’t invest their own money or take a pay cut to make it work, why should I?
- By contrast, this [OpenAI Deep Research report](https://chatgpt.com/share/67c3e38c-e514-800c-8cfc-983bd4fdeb21) feels a lot less actionable.
- [Inception Labs](https://www.inceptionlabs.ai/) offers "Diffusion LLMs". (No API yet.) They start with random text and refine it in parallel. The benefit is:
  - It's faster and cheaper due to parallellalization and better GPU use
  - It doesn't commit to tokens and can fix hallucinations, JSON structure errors, reasoning fallacies, etc.
  - It's better with multi-modal since images are diffusion based already.
