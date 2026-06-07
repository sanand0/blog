---
title: Things I Learned - 28 Sep 2025
date: 2025-09-28T00:00:00+00:00
categories:
  - til
description: I replaced lxml with selectolax, managed Python environments with uv, and tested GitHub Actions locally using wrkflw. I also explored habit engineering, task parity in AI, and used markitdown to convert websites via CLI.
keywords: [selectolax, uv, wrkflw, markitdown, yt-dlp, visidata, jsdoc, envsubst]
---

This week, I learned:

- [`selectolax`](https://github.com/rushter/selectolax) is a fast, easy-to-use, modern HTML5 parser with CSS selectors. A good replacement for `lxml.html`.
- The most effective way to convert a blob (e.g. file input) to a data URL on the browser seems to be via the [FileReader](https://developer.mozilla.org/en-US/docs/Web/API/FileReader) API.
  ```js
  const blobToDataURL = (blob) =>
    new Promise((res, rej) => {
      const r = new FileReader();
      r.onload = () => res(r.result);
      r.onerror = () => rej(r.error);
      r.readAsDataURL(f);
    });
  ```
- Tool calls in OpenAI support files and images. [OpenAI](https://x.com/OpenAIDevs/status/1971618905941856495?t=1fJFyLyYQXlbMMquShLMOQ)
- ⭐ "Task parity is not the same thing as job parity There is a lot of complexity as many different tasks are bundled into jobs, and many jobs contribute to processes inside an organization The jagged frontier of AI ability means doing tasks well doesn't translate to doing jobs well." [Ethan Mollick](https://x.com/emollick/status/1971643202332733683?t=SqZLjGdInJf4DRb5zcMPqQ)
- Adding `// @ts-check` to a JavaScript file and documenting types via JSDoc might be the simplest way to migrate phase-wise from JS to Typescript.
- `envsubst < file.txt` replaces `file.txt` with the environment variable, e.g. `$HOME` is replaced by the `HOME` environment variable. Clean shell-level templating.
- [GitHub Copilot CLI](https://github.com/github/copilot-cli) is out. `npx -y @github/copilot`
- [Compost](https://www.amazon.in/ORGANIC-PLANT-Primium-Quality-Vermicompost/dp/B0B59QXGC4) is the cheapest thing per ton that I can buy on Amazon India. I can buy 1 ton of compost for Rs 13,500. [ChatGPT](https://chatgpt.com/s/t_68d5e3ef9e4081919e1ecd6582e6197c)
- `yt-dlp` requires Deno from now on. [#14404](https://github.com/yt-dlp/yt-dlp/issues/14404)
- In meetings, make cameras optional by default -- and judge engagement by contributions, not video -- because a 4-week field experiment found camera-on increased fatigue and reduced voice, especially for women and newcomers. Camera on early for trust building is useful. [PubMed](https://pubmed.ncbi.nlm.nih.gov/34423999/)
- [`wrkflw`](https://github.com/bahdotsh/wrkflw) is a quick and light way to test GitHub actions before publishing. It runs GitHub actions locally.
- GPT-5-Codex is available as an API and on LLM. [Simon Willison](https://simonwillison.net/2025/Sep/23/gpt-5-codex/)
- ⭐ I'm habit engineering, i.e. discovering and stacking habits on to existing ones. For example:
  - ChatGPT suggested increasing observability based on code reviews. I'm including it in my [weekly codecast](https://github.com/sanand0/sanand0/tree/main/week).
  - ChatGPT suggested defining closures inmeetings. I'mn now discussing objectives at meeting starts and effectiveness at the end.
- Since Anaconda [cannot be used for free](https://www.anaconda.com/pricing) by organizations with 200+ people, Straive's received legal notices from Anaconda. Since laptops are under central IT administration, they went ahead and deleted all Anaconda instances. Installing [miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main) for use with [conda-forge](https://conda-forge.org/) requires admin access that most developers do not have, however. That leads to an interesting "No Python" situation. This is where [`uv`](https://github.com/astral-sh/uv) becomes the knight in shining armor.
- [Perceptron](https://www.perceptron.inc/blog/introducing-isaac-0-1) is SOTA LLM for object bounding boxes. Just 2B parameters.
- Gall's "law" says that complex systems that work evolved from simple systems that worked. But a complex system designed from scratch won't ever work. This holds in uncertain environments. But where formal theory or regulations exists, it doesn't. [ChatGPT](https://chatgpt.com/share/68d2c367-d674-800c-9c1c-51fcacfa5c6d)
- [`uvx --with visidata vd`](https://www.visidata.org/) gives you a command-line Excel editor to edit / convert CSV, Excel, JSON, SQLite, directories, etc.
- `uvx markitdown https://example.com/` fetches `example.com` as Markdown. I learnt this when I told Codex it could use `uvx markitdown` to convert PDFs and it figured this part out by itself.
- The Dropbox connector for ChatGPT is the little flaky -- at least on Android. It could not identify a file that was clearly there in Dropbox and I had to upload it manually.
- ChatGPT's output is too dense for me. I added this to my custom instructions: "Write in simple language. Explain non-obvious terms intuitively."
- `yt-dlp` has a `--download-sections` option that downloads specific YouTube time ranges. For example `--download-sections "*00:01:00-00:03:00"` downloads _roughly_ (not exactly) from 1 min to 3 min. Note the `*` at the beginning.
- My Lenovo laptop's touchpad started scrolling instead of moving when I moved my finger. Many things could have caused it, but the solution was to click (not tap) the top middle of the trackpad. [ChatGPT](https://chatgpt.com/share/68cfc8ff-e7fc-800c-b8bf-474d41332cd1)
- The [India Entrance Exam database](https://github.com/lalithaar/indian-exams-database) is a dataset collating Indian entrance exams.
