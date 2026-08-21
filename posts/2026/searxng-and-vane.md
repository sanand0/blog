---
title: SearXNG and Vane
date: 2026-03-19T15:40:25+05:30
categories:
- tools
description: I found SearXNG, a self-hostable metasearch engine with a simple JSON API, and Vane, a self-hosted Perplexity clone. Vane handled multi-hop questions and false premises but missed my latest blog post.
tags: [web-search, self-hosting, llms, privacy]
---

While exploring [resonant computing tools](https://claude.ai/share/a7ae0d69-8c56-49a2-b6f2-1e3f4cd32937), I discovered [SearXNG](https://searxng.org/), a self-hostable metasearch engine, which aggregates results from multiple search engines.

![Searching for "Wikipedia" shows a Google-like results page.](https://upload.wikimedia.org/wikipedia/commons/0/0a/SearXNG_Results_Page.png)

It lets you search using APIs without needing to buy API keys and without being tracked. Pretty useful for research, people discovery, etc. when combined with LLMs.

Setting it up for API use seems easy (thought [Gemini got it wrong twice](https://gemini.google.com/share/33e8ed8dbc40)):

```bash
cat <<EOF > settings.yml
use_default_settings: true
server:
  secret_key: "local_dummy_secret_key_987654321"
search:
  formats:
    - html
    - json
EOF

docker run -d \
  -p 8080:8080 \
  --name searxng \
  -v "$(pwd)/settings.yml:/etc/searxng/settings.yml" \
  -e "SEARXNG_BASE_URL=http://localhost:8080/" \
  -e "SEARXNG_SERVER_LIMITER=false" \
  searxng/searxng
```

Now, you can run:

```bash
curl -s "http://localhost:8080/search?q=best+sci-fi+books&format=json"
```

... which returns a JSON like this:

```jsonc
{
  "query": "best sci-fi books",
  "number_of_results": 0,
  "results": [
    {
      "template": "default.html",
      "url": "https://www.goodreads.com/list/show/19341.Best_Science_Fiction",
      "title": "Best Science Fiction (3733 books) - Goodreads",
      "content": "Other SF Lists of Note: ...",
      "publishedDate": null,
      "thumbnail": "https://imgs.search.brave.com/...",
      "engine": "brave",
      "parsed_url": ["https", "www.goodreads.com", "/list/show/19341.Best_Science_Fiction", "", "", ""],
      "img_src": "https://imgs.search.brave.com/...",
      "priority": "",
      "engines": ["startpage", "duckduckgo", "brave"],
      "positions": [2, 1, 1],
      "score": 7.5,
      "category": "general",
    },
    /// ...
  ],
  "suggestions": [
    "top 10 best sci-fi books of all time",
    // ...
  ],
  "unresponsive_engines": [
    ["google", "access denied"],
    ["wikidata", "timeout"],
  ],
}
```

There are many [public SearXNG instances](https://searx.space/). Google seems to be blocked on many of these, but Brave, DuckDuckGo, and others seem to work fine.

---

That leads me to [Vane](https://github.com/ItzCrazyKns/Vane) which is a self-hostable Perplexity clone! A hosted version is available at [Perplexica.io](https://perplexica.io/).

```docker
docker run -d -p 3000:3000 -v vane-data:/home/vane/data --name vane itzcrazykns1337/vane:latest
```

I tried a few questions and compared with Perplexity / Gemini using [GPT-5 nano](https://developers.openai.com/api/docs/models/gpt-5-nano) -- a _really_ cheap model.

- 🟢 **It solves multi-hop queries**. Which company acquired the data visualization firm Gramener in late 2023, and what is the current public stock ticker and market capitalization of that acquiring company?
  - A: The data-visualization firm Gramener was acquired in November 2023 by Straive. Straive is a private company owned by BPEA EQT, part of the EQT group. Because Straive is privately held, it does not have a public stock ticker, and its market capitalization is not publicly disclosed.
- 🟢 **It catches wrong questions**. Summarize the findings of the April 2025 paper 'Agile Methodologies in High-Latency LLM Architectures' by Dr. Aris Thorne.
  - A: Hmm, sorry I could not find any relevant information on this topic. Would you like me to search again or ask something else?
- 🔴 **It doesn't get the latest data**. Summarize the latest blog post on my website s-anand.net.
  - A: I can do that. To ensure accuracy, I’ll need to fetch the latest post from s-anand.net and summarize it with key takeaways and insights. Would you like me to fetch the latest post directly from the site now, or you provide the post URL or paste the content here?
  - Q: Fetch the latest post directly and give me a 1 para summary
  - A: The latest post on s-anand.net is "Education Blog embeddings map," published on Tue, 17 Mar 2026...

Though Vane got the last question wrong, Perplexity and Gemini got it wrong as well! So I guess it's a good, comparable alternative.
