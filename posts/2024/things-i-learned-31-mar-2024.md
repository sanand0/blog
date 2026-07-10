---
title: Things I Learned - 31 Mar 2024
date: 2024-03-31T00:00:00+00:00
categories:
  - til
description: I investigated binary embeddings, empathic AI with Hume.ai, and audio splitting with Spleeter. I failed at building a Rust-based Parquet server and noted distinct corporate attendance patterns while hosting workshops for Gramener and Straive.
---

This week, I learned:

- [sqlite-schema-diagram](https://gitlab.com/Screwtapello/sqlite-schema-diagram/) generates schemas for SQLite databases using Graphviz
- [TechEmpower web server benchmarks](https://www.techempower.com/benchmarks/) place Rust servers on top
- [browser.new](https://browse.new/) is a good example of a browser agent. It slowly but independently does a good job of achieving the result. Example: [What crew is common in Ingrid Bergman - Cary Grant films?](https://browse.new/run/browser_wDHy2vwxIzJFouL)
- [twinny](https://github.com/rjmacarthy/twinny) is an open source VC Code Copilot alternative.
- [typesense supports embeddings natively](https://hn-comments-search.typesense.org/).
- [Binary embeddings are good enough](https://blog.pgvecto.rs/my-binary-vector-search-is-better-than-your-fp32-vectors). Cohere releases [binary embeddings](https://txt.cohere.com/int8-binary-embeddings/).
- [Extract.langchain.com](https://extract.langchain.com/) is a poor early interface to featurize [unstructured.io](https://unstructured.io/)
- [Hume.ai](https://www.hume.ai/) offers voice emotion API and emotion-based conversational responses. An empathic AI.
- Rust is non-trivial. Inspired by [We are under DDoS attack and we do nothing](https://tableplus.com/blog/2024/03/how-we-deal-with-ddos.html), I ["wrote"](https://chat.openai.com/share/ec5f3d23-06b3-40a8-a965-ab466d214802) a small binary that serves a parquet file as JSON. It failed and I couldn't fix it.
- [spleeter](https://github.com/deezer/spleeter) is a better alternative to demucs. Splits audio into
- [pyannote-audio](https://github.com/pyannote/pyannote-audio) does speaker diarization
- [uvicorn](https://github.com/encode/uvicorn) is faster than [hypercorn](https://github.com/pgjones/hypercorn) but [hypercorn supports HTTP/2 and HTTP/3](https://pgjones.gitlab.io/quart/tutorials/deployment.html). FastAPI with uvicorn is reasonably fast.
- [Representational engineering](https://vgel.me/posts/representation-engineering/) lets you control LLM output based on preference on the fly.
- When I set up a training:
  - On inviting for DuckDB workshop on Sun evening, Gramener starts accepting immediately, Straive doesn't.
  - Straive has high spread of joining time. When joining Gitlab Pipelines Workshop, Straive starts meeting (e.g. Premlal) many minutes early. Gramener floods in (due to alert). Straive streams in slowly.
  - Gitlab Pipelines Workshop acceptances: Gramener 47, Straive 100
