---
date: "2025-08-15T00:00:00Z"
categories:
  - linkedin
---

_Indian Celebrities and Directors_ was my top searched category on Google while _OpenAI_ & _AI Research_ was the top growing category.

This is based on my 37,600 searches on Google since Jan 2021. Full analysis: https://sanand0.github.io/datastories/google-searches/

The analysis itself isn't interesting (to you, at least). Rather, it's the two tools that enabled it.

First, **topic modeling**. If you have all your searches exported (via Google Takeout) into a text file, you can run:

```bash
uvx topicmodel searches.txt --ntopics 50
```

... and automatically get the top 50 topics you search for.

Second, an **improved O**3 **prompt**. I fed it monthly topics volume and asked:

> Look closely at the numbers as well as the image.
> What insights can you draw from these?
> Aim for non-obvious non-trivial insights.
> Run correlations or any other analyses on the data to go deeper and come up with material suitable for a deep research paper.

The analyses it did was _far more powerful_ than anything I would have thought of.

1. It calculated my **Herfindahl**-**Hirschman index slope** and declared that **my search interests are diversifying**. (Good to know!)
2. Using **Principal Component Analysis** it discovered 3 **personas** in my searches
   - Classical developer (Python, JS)
   - AI-builder (OpenAI, LLMs, APIs)
   - India/Singapore geo-culturist (Celebs, local info, Tamil cinema)
     I should segment sharing & learning along these axes (e.g. separate newsletters or dashboards.)
3. Using the **Coefficient of Variation** it found the biggest spikes in SQL & Databases, and Testing & Code Tools. Steadiest were Currency Conversion Rates and Singapore/Bangalore Local Info.

I should cache common reference lookups locally and allocate “deep‑focus blocks” for debugging spikes.

There's more. But this is the first time I felt _completely_ outmatched by an LLM. I'm an expert on analysis. I'm an expert on this domain (_my_ search queries.) Yet, this is far more insightful than I ever would have analyzed!

![](https://sanand0.github.io/datastories/google-searches/google-search-topic-trends.webp)

[LinkedIn](https://www.linkedin.com/posts/sanand0_%F0%9D%98%90%F0%9D%98%AF%F0%9D%98%A5%F0%9D%98%AA%F0%9D%98%A2%F0%9D%98%AF-%F0%9D%98%8A%F0%9D%98%A6%F0%9D%98%AD%F0%9D%98%A6%F0%9D%98%A3%F0%9D%98%B3%F0%9D%98%AA%F0%9D%98%B5%F0%9D%98%AA%F0%9D%98%A6%F0%9D%98%B4-%F0%9D%98%A2%F0%9D%98%AF%F0%9D%98%A5-activity-7355065649959784448-in8E)
