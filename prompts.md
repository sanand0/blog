# Prompts

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
