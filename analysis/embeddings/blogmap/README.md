# Embedding Visualization

This visualization uses the refreshed embeddings in `analysis/embeddings.parquet`:

- comments stripped before embedding
- long image/link dumps removed when the remaining prose is tiny
- truncation cap increased to 20k characters

The plots linked below were regenerated from the refreshed embeddings under [`../2026-03-15-embedding-visualization/`](../2026-03-15-embedding-visualization/).

## What The UMAP Shows

The refreshed UMAP has three clear visual properties:

1. One large historical mass

Most of the archive still lives in a broad, dense island centered around the early link-blog / old-web corpus. That is where the oldest years cluster, and it is where most of the `links` category continues to sit.

2. A distinct modern AI/workflow frontier

Recent writing is no longer just "mixed into the archive". It forms a visibly separate region on the left side of the UMAP, dominated by 2024-2026 material. In the refreshed clustering:

- **2024** is **77.8%** cluster `2` and **18.1%** cluster `8`
- **2025** is **86.5%** cluster `2` and **12.9%** cluster `8`
- **2026** is **85.0%** cluster `2` and **15.0%** cluster `8`

Cluster `2` is the main modern AI/workshop/vibe-coding / LinkedIn-style region. Cluster `8` is the nearby notes/tools/books/workflow region.

3. A few true outliers

The embedding space now has a main body plus a handful of detached points or tiny splinters. Visually, these are not noise inside the core cloud; they really are outside it. That is useful for interactive visualization because it means the main region can be shown clearly if those outliers are de-emphasized or clipped.

## Key Plots

### UMAP Colored By Year

![UMAP by year](../2026-03-15-embedding-visualization/umap-year.png)

This is the clearest plot in the set.

- The historical corpus sits mostly in the main island.
- The 2024-2026 material is concentrated in the separate left-side frontier.
- The color gradient is not random. It traces a semantic drift from old web/linklog material toward recent AI/workflow writing.

### UMAP Colored By Cluster

![UMAP by cluster](../2026-03-15-embedding-visualization/umap-clusters.png)

The refreshed run produces **12** semantic regions. The largest visually meaningful ones are:

- cluster `0`: early web / internet infrastructure / old-web commentary
- cluster `1`: playful links / curiosities / games / humorous old-web material
- cluster `2`: AI practice, workshops, vibe coding, LinkedIn-style posts
- cluster `3`: tools / tutorials / web publishing / internet how-to material
- cluster `6`: Google/search/web-discovery region
- cluster `7`: coding / Excel / automation / practical tech
- cluster `8`: recent notes, books, workflows, teaching/tools
- cluster `11`: tightly self-contained quizzes

The cluster view is useful mainly as a shape map. The category view is still better for local explanation.

### Yearly Embedding Centroids

![Yearly centroids](../2026-03-15-embedding-visualization/year-centroid-drift.png)

The centroid plot shows the same story in simpler form:

- `1999-2006` move gradually within one broad regime
- `2007-2012` drift upward into a more personal / mixed phase
- `2020` is the sharpest jump
- `2021-2026` settle into a new neighborhood

The biggest jumps in the refreshed run are:

- **2020**: drift `0.091`
- **2021**: drift `0.068`

After that, the space stabilizes again.

## What The Visualization Says About Categories

The refreshed embeddings still preserve category signal locally:

- nearest-neighbor same-category rate: **84.3%**
- random baseline: **46.5%**
- lift: **1.81x**

But the UMAP also makes it obvious that categories are not the same thing as regions.

### Categories That Look Like Regions

- `quizzes`
- `llms`
- `linkedin`
- `london-2000`
- `london-2005`

These categories have relatively coherent neighborhoods.

### Categories That Behave More Like Containers

- `links`
- `how-i-do-things`
- `coding`
- `funny`

`links` is the clearest example. It is not one blob on the map; it is spread across several semantically different areas. In the visualization, `links` behaves more like an archive-era umbrella than a topic.

The overlap map shows the strongest cross-category ties:

- `coding -> how-i-do-things`: `4.62x` baseline
- `llms -> linkedin`: `4.19x`
- `linkedin -> llms`: `3.89x`
- `coding -> llms`: `3.24x`

That is exactly the shape visible in the refreshed UMAP: modern AI/workflow writing crosses category boundaries more than the old taxonomy implies.

## What Changed Visually After The Refresh

The refreshed embeddings produce a cleaner map for visualization:

- comments no longer inflate old discussion-heavy posts
- image dumps no longer dominate short body text
- longer recent notes and list pages retain more semantic content because of the 20k cap

The practical result is that the modern region reads more clearly as a semantic frontier instead of a formatting artifact. The recent AI/workflow island is still dense, but it is easier to interpret as "what you are thinking about now" rather than "what had the longest boilerplate".

## Reading Guide

If you are scanning the plots quickly:

1. Start with [`umap-year.png`](../2026-03-15-embedding-visualization/umap-year.png) to understand the broad motion of the corpus.
2. Then open [`umap-clusters.png`](../2026-03-15-embedding-visualization/umap-clusters.png) to see the semantic regions.
3. Use [`year-centroid-drift.png`](../2026-03-15-embedding-visualization/year-centroid-drift.png) to verify that the "recent shift" is real and not just a local visual quirk.
4. Use [`category-overlap-heatmap.png`](../2026-03-15-embedding-visualization/category-overlap-heatmap.png) when you want to understand why some categories visually bleed into each other.

## Takeaways

- The refreshed UMAP is a useful overview of the archive, not just a pretty projection.
- Time is one of the strongest visible signals in the space.
- The modern AI/workflow corpus is now a clearly identifiable semantic zone.
- `links` remains visually and semantically too broad to be treated as one topic.
- The map is now clean enough to support an interactive visualization that filters by year, category, and cluster without feeling arbitrary.
