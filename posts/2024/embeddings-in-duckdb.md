---
title: Embeddings in DuckDB
date: "2024-06-16T13:06:44Z"
categories:
  - links
wp_id: 3556
---

This article on [Using DuckDB for Embeddings and Vector Search](https://blog.brunk.io/posts/similarity-search-with-duckdb/) by Sören Brunk shows a number of DuckDB features I wasn't aware of.

- DuckDB can read directly from [Huggingface datasets](https://huggingface.co/docs/hub/datasets-duckdb)
- DuckDB can read [just the parts of a .parquet file it needs](https://duckdb.org/docs/data/parquet/overview#partial-reading), even [over HTTP](https://duckdb.org/2021/06/25/querying-parquet.html)
- DuckDB lets you [write custom functions in Python](https://duckdb.org/docs/api/python/function)
- DuckDB now has a [vector similarity search extension](https://duckdb.org/2024/05/03/vector-similarity-search-vss.html)

I've recently become a DuckDB fan and continue to be impressed.
