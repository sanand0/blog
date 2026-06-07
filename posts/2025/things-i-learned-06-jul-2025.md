---
title: Things I Learned - 06 Jul 2025
date: 2025-07-06T00:00:00+00:00
categories:
  - til
---

This week, I learned:

- When adding a coding benchmark for LLMs, here's a question I'd like to add. #benchmark
  > How do I use Apache Arrow in the browser via cdn.jsdelivr.net to create a .parquet file and download it? Give me minimal working code I can paste in the browser console to test.
- LinkedIn has an undocumented link that shows schedules posts at <https://www.linkedin.com/share/management/> which redirects to <https://www.linkedin.com/feed/?shareActive=true&view=management>
- Here's a JS snippet you can paste in the DevTools console of an npm package version page ([example](https://www.npmjs.com/package/d3?activeTab=versions)) to get a Markdown list showing the versions and dates
  ```js
  copy(
    $$('table[aria-labelledby="version-history"] tbody tr')
      .map((tr) => {
        const a = tr.querySelector("a");
        const date = new Date(tr.querySelector("time").getAttribute("datetime")).toLocaleDateString("en-GB", {
          day: "numeric",
          month: "short",
          year: "numeric",
        });
        return `- [${a.textContent.trim()}](https://npmjs.com${a.getAttribute("href")}): ${date}.`;
      })
      .join("\n"),
  );
  ```
- DuckDB can read JSON APIs! [Ref](https://duckdb.org/2025/06/27/discovering-w-github)
- ⭐ When bringing in humans-in-the-loop, applications must make it easier to _review_ and to _edit_ the work.
