# Prompts

## Post meta, 08 Jul 2026

<!--
cd ~/code/blog
dev.sh -- codex --yolo --model gpt-5.5 --config model_reasoning_effort=medium
-->

In the .post-meta line, minimally add a [Permalink](https://www.s-anand.net/blog/...) link that adds the permalink based on the `metadata.yaml` site.link base URL.

## TIL, 07 Jun 2026

<!--
cd ~/code/blog; dev.sh -p ~/code/til/
codex --yolo --model gpt-5.5 --config model_reasoning_effort=medium
-->

Migrate TIL into my blog. See how ~/code/til/ converts the til.md and llms.md into weekly blog posts as a GitHub deploy workflow. Write a concise agent-friendly CLI scripts/til.py that does something similar. It should create a posts/yyyy/things-i-learned-dd-mmm-yyyy.md file. It'll always be on a Sunday, covering everything up to the previous day (Saturday). Title is like "Things I Learned - 07 Jun 2026". Categories: "til" (add to the metadata.yml). "date" should be mid-day UTC of the Sunday. The post should begin with a line "This week, I learned:". By default, it should run for the latest week (i.e. generate it for the most recent Sunday). I should be able to run this for any week or time range. It should be fast and not overwrite existing files unless forced.

Run and test for a few weeks and await my feedback.

---

Updates:

- Include the date on which I learned each item. For example: "21 May 2026. BitWarden seems to be sneakily ..."
- If the target file for any week already exists and we're not forcing the generation, generate the content anyway and show the diff between the two entire files. Then I can decide whether to force or not.
- Instead of 12 pm UTC, set the time to 00:00 UTC on the blog posts.
- Move tests/test_til.py to scripts/test_til.py.
- Re-run for the same TILs you created.
- Tell me how to run til.py for all time periods covered by til.md / llms.md - don't run it yet.
- Update README.md explaining til.py. I'll be running it weekly on Sundays.

---

I take back what I said. Remove the date from each item. For example, just say "BitWarden seems to be sneakily ..." without the date.

Move analysis/linkedin_blog_map.py to scripts/linkedin_blog_map.py. Make sure it still updates analysis/linkedin-blog-map.tsv -- only the script path is changed. Run and test.

Update README.md explaining linkedin_blog_map.py. I'll be running it whenever I post on LinkedIn.

<!-- codex resume 019ea045-6afd-7080-a8da-9750a33c89ab --yolo -->

## LinkedIn posts, 06 Jun 2026

<!--
cd ~/code/blog; dev.sh -p ~/Documents/data
codex --yolo --model gpt-5.5 --config model_reasoning_effort=medium
-->

~/Documents/data/linkedin-posts.jsonl contains all my LinkedIn posts (and comments - but you can skip those.)

Most of my posts, especially in the last few years, are simple rewrites of my blog posts. For example, https://www.linkedin.com/feed/update/urn:li:activity:7467813154660667392/ is a rewrite of posts/2026/my-most-memorable-anniversary.md.

I rewrite by (a) shortening and simplifying (occasionally adding) and (b) converting Markdown to Unicode, e.g. **bold**, _italics_, `code` to 𝗯𝗼𝗹𝗱 or 𝐛𝐨𝐥𝐝, 𝘪𝘵𝘢𝘭𝘪𝘤𝘴, 𝚌𝚘𝚍𝚎.

I usually post on LinkedIn a few hours or days after I post on my blog, but occasionally post a few minutes earlier.

The LinkedIn scraper that generated the JSONL may not be very reliable, but the url: and content: fields seem to be reasonably correct.

I want to create a TSV mapping of all LinkedIn post URLs (e.g. https://www.linkedin.com/feed/update/urn:li:activity:7467813154660667392/) to the corresponding blog post filename (e.g. posts/2026/my-most-memorable-anniversary.md) if there is one, and leave it blank if none exist. The TSV should also contain the ASCII-ified LinkedIn content (200 chars, truncated) and the blog post content (200 chars, truncated) for reference. (Multiple matches are unlikely but if there are, let me know.)

Execute this in the most token-efficient direct and simple way without errors.

If you need any inputs, ask me.

---

I have manually updated analysis/linkedin-blog-map.tsv. Make sure that if we re-run analysis/linkedin_blog_map.py it will not change any existing mappings and append add new ones (if any). To facilitate this, sort the existing TSV by date (oldest LinkedIn post first) and keep it sorted that way.

Next, add a linkedin: YAML metadata to the blog posts that have a LinkedIn post.

Lastly, for such posts, render a link to the LinkedIn post at the bottom of the blog post. The text can simply include the LinkedIn icon and the words "LinkedIn post".

Run `setup.sh` and test.

---

Write the post-mortem and tool failures - the path should be writeable.

<!-- codex resume 019e9afa-f977-7282-8bf5-c1825e2853ff --yolo -->

## AI generated content, 23 May 2026 (Claude Sonnet 4.6 - medium)

Make sure contents inside a `<section ai-disclosure="ai-generated" data-ai-model="..." data-ai-provider="...">` are subtly styled like in `assets/ai-generated-sample.avif` and in a way consistent with the theme and future proof (e.g. use opacity along with darkness/lightness rather than changing hues, handle dark mode, etc.)

Add a small "AI" badge at the top right (hover should reveal the model and provider information), mention "AI-GENERATED - Model - Provider" at the bottom in small font, make the background SUBTLY different, add a SUBTLE border with the left border being thicker.

Search the standard to see if other data-* attributes are allowed. In any case, future-proof it to handle any data-ai-* attributes for the future.

Run and test visually. Revise as required.

<!-- I manually adjusted the paddings and removed the border -->
<!-- claude --resume de719afa-09f2-4110-a581-f9eca2729cbc -->

## Markdown link, 31 Mar 2026 (Copilot - gpt-5.4-mini xhigh)

Add a <link rel="alternate" type="text/markdown" href="..."> header to all posts/pages that links to the GitHub raw markdown file for that page.

Run bash setup.sh and verify that the header is present in the generated HTML files.

## Header link and JSON navigation, 21 Mar 2026 (Claude Code - Sonnet 4.6)

<!-- https://claude.ai/code/session_012J8cWHH5wUncaFXr5HBmHN -->

Clicking on the "S Anand" on the header on all pages currently takes me to https://www.s-anand.net/blog/ which is the blog root but it should instead take me to https://www.s-anand.net/

Commit this.

Instead of adding the categories, archives and pages to each page, use JavaScript to pre-create a JSON that is loaded and rendered on every page.

Modify the archives so that it shows the monthly links for the current (latest) year and the yearly links for past years. For example, Mar 2026, Feb 2026, Jan 2026, 2025, 2024, ...

Commit this.

---

<!-- claude --teleport session_012J8cWHH5wUncaFXr5HBmHN -->

I ran `bash setup.sh` and under public/ the .nav > .logo > a element still links to /blog/ across pages.

---

Improve the visual appearance of the footer columns. Specifically:

- Modify the links so that they take up the full width of the column
- Add a single-pixel horizontal line below links that have numbers (categories, archives) whose width is proportional to the number of items in that category/archive. Use the third largest value as 100% width to eliminate outliers.
- Think of and apply other improvements to the visual design of the footer columns to make them more visually appealing and easier to navigate

---

The footer looks fine but is not visible on / which is actually copied from /blog/s-anand/ into / (see setup.sh).
Make sure this will still work.

Review the code changes made so far in this session. How could we simplify, shorten, and make it more elegant and maintainable? Refactor as needed.

<!-- claude --resume b8c8b5ea-7ade-4677-a9c1-2598ad9a4e3d -->
