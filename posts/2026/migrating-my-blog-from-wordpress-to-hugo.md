---
title: Migrating my blog from WordPress to Hugo
date: 2026-01-02T12:30:00+08:00
categories:
  - coding
classes: wrap-code
---

In 2009, I migrated from a self-made Perl static site generator to [WordPress](https://www.wordpress.org/) because it was slow, WordPress was dynamic and rapidly growing in features, and I wanted to write rather than code. (Also, I had _plenty_ of time in 2009 for such things!)

Over the years, problems crept in. Hosting costs ($200/year) for a slow server. No local writing - [Windows Live Writer](/blog/wordpress-themes-on-windows-live-writer/) was dead. I wasn't using most WordPress features. So it was time to migrate back to a static site generator. (Also, I now have _plenty_ of time for such things!)

I tried in 2024. But the complexity of the migration was higher than my laziness. (I tried with LLMs. Didn't work.)

Finally, in Dec 2025, coding agents were good enough to get this done. Codex and Claude Code both doubled their limits for the holidays, and I had no meetings. So, over two days, I joyfully migrated to a static site.

- Content is written in Markdown via VS Code and pushed to https://github.com/sanand0/blog/
- A GitHub Action [`deploy.yaml`](https://github.com/sanand0/blog/blob/main/.github/workflows/deploy.yml) publishes to GitHub Pages
- It uses a [`hugo.toml`](https://github.com/sanand0/blog/blob/main/hugo.toml) configuration with [supporting scripts](https://github.com/sanand0/blog/tree/main/scripts).

Here're the useful practices I distilled from my prompts.

### Create a `PLAN.md` before complex tasks

```markdown
Create a plan in PLAN.md to convert my blog into Markdown-based content I can commit on GitHub and is published via a static site generator retaining the same URLs.

My website https://s-anand.net/ hosts a WordPress blog at https://s-anand.net/blog/ and I have exported the content as an XML file using the WordPress export tool into sanand.WordPress.2025-12-28.xml. Read it to understand.

Each post and page must become a Markdown file with front-matter containing all metadata (title, date, tags, categories, slug, author, etc). The Markdown must be stored as

- ./metadata.yml (for site-wide metadata)
- ./posts/yyyy/yyyy-mm-dd-slug.md
- ./pages/slug.md
- ...

You can browse the site https://s-anand.net/blog/ to see the site structure and all the types of pages that are generated.
You can also "ssh sanand" to access the server and `cd www/blog/` to see the WordPress configuration.

Note that some posts / pages have complex content: tables, code, embedded media, shortcodes, JavaScript, etc. Identify all such cases and how to handle them. There may still be edge cases that you don't know how to handle; list them out. This is a major part of the plan - ensuring that you cover all types of content -- either with a plan to handle it easily and elegantly, or explicitly identifying ALL edge cases and listing them.

Include how to handle images and other media. The WordPress export XML file may not contain the actual media files; identify how to get them. Suggest how to store them - I can store them in the Git repo, or in GitHub releases (needs to be fetched during CI process), or in R2 (direct access like a CDN). I would also like to compress media (e.g. to WebP) for better performance.

I plan to use either of these hosting options. Let me know what you prefer:

- GitHub CI to deploy to GitHub Pages (preferred: it's free, easy, and reliable).
- OR, convert locally to static HTML and upload to R2 / CloudFlare pages (priced, more effort, but reliable).

Suggest a static site generator (SSG) to use. I prefer something FAST and simple. I prefer single-binary SSGs or installation-free SSGs (e.g. via npx, uvx) if possible.

Consider any other requirements I may have missed, e.g. plugin features, SEO, redirects, analytics, comments, search, RSS feeds, sitemaps, etc. Going through the site or the WordPress configuration may help identify these. Suggest how to handle them.
```

It analyzed my blog: blocks and shortcodes used, plugins, URL structure, etc. and came up with a pretty good plan. Here are some notes:

- Record unresolved edge cases for manual review. (Wise!)
- Prefer raw HTML inside Markdown when conversion would lose fidelity. (Interesting! Also has detailed rules for tables, code, figures, iframes, forms, ...)
- Frontmatter: Required: title, date, lastmod, slug, author, categories, tags, status, draft, canonical, summary/excerpt, comment_status, ping_status. (Um... too much?)
- Use Hugo (single binary, fast, built-in RSS/sitemap/taxonomies, supports raw HTML and shortcodes) and GitHub Pages via GitHub Actions.

There's _no_ way I would have thought of all of these!

### Analyze data while planning

Even while it was planning, another thing struck me. I won't use GitHub to serve assets. It bloats the repo. Plus, there's an opportunity to compress better with WebP. So I asked it to analyze my media.

```markdown
I've rsynced `sanand:www/blog/wp-content/uploads/` to `./uploads/` locally.

Which uploads are unused in my blog posts / pages. Tell me the number, total size, and save them all in unused-uploads.tsv with columns size, filename.

If I convert all used images over 10KB to WebP, how much space will I save? (An estimate is fine; I don't need exact numbers.)
```

It parsed the WordPress export against my local `uploads/`, listed unused uploads (1.7K files of 87MB), and found 515 used files of 34MB. It estimated ~11MB savings from WebP conversion of used images >10KB.

### Edit `PLAN.md` using the agent, not manually

Editing manually is prone to mistakes, e.g. introducing contradictions.

```markdown
I am fine with Hugo + GitHub Pages.

/blog must remain the subpath - the URL structure must NOT be disturbed. Prefer publishing into a /blog/ folder.

Import old comments (prefer YAML over JSON for easy reading). The new static site will not have dynamic comments; I may switch to Giscus or Utterances later.

As for media, let's convert and save WebP versions instead of the originals and commit them directly to the Git repo under uploads/. Only used media should be included.

Revise PLAN.md accordingly. Let me know what other information you need, if any.
```

Useful lesson: **Let me know what other information you need, if any.** Life is full of unknown unknowns!

It did ask if I was OK changing URLs from `.jpg|.png` to `.webp`, which I confirmed in the next prompt.

### Implement small steps, run and commit as you go

I know from experience that a single-shot implementation of this size would be too complex today. So I asked for image conversion first.

```markdown
Now, implement the upload handling. Delete unused uploads (I have backups on the server). Compress JPEGs with 50% quality and PNGs losslessly with 256 colors. Let me know the revised size of assets.

I am OK with image URLs breaking.

Implement this by writing a script (bash, Python, Node JS - anything is fine, whatever is easiest) that will create an `assets/` folder with the converted images from the `uploads/` folder. I will want to re-run this later with some tweaks.

Commit as you go.
```

Having the agent **run the script** is the most powerful idea in here. If it makes a mistake, it can figure it out and fix itself.

**Commit as you go** is useful. I can undo changes later. I also efficiently get a sense of the progress and thinking.

It took a _long_ time (on GPT 5.2 Codex - Extra High Thinking), wrote a `scripts/prepare_assets.py`, switched from ImageMagick to Pillow for better control (strange!), trouble-shooted PNG transparency bugs, ran it, noted that 41 files in my blog that were missing, and committed everything.

### Run post-mortems mid-way

Strangely the JPEG files weren't converted. So I asked:

```markdown
Why does the assets/ folder still have some .jpg files, e.g. temperature.jpg? I assumed they'd all be converted to webp.
```

It said:

> Because the script follows your latest instruction: it compresses JPEGs and PNGs in-place and keeps their original formats.

OOPS! My mistake. Anyway, I also needed it to convert MP3 to Opus. So...

### Ask for actionable exception reports

Let's have it do all the conversions.

```markdown
Convert all JPEG files to WebP, too, with 50% quality. Use cwebp to convert - it is faster and has better quality.

Let's also compress audio files to OPUS with ffmpeg using `-c:a libopus -b:a 12k -ac 1 -application voip -vbr on -compression_level 10`. Modify the script accordingly.

Also modify the script to list missing local uploads/ mentioning the URL on https://s-anand.net/blog/... post or page that references each. Each line should list the missing filename and URL, tab-separated.
```

But note the last line. It had already identified that some uploads were missing. To **action** that, I would need a post -> file mapping, which I asked for.

### Delegate verification to the agent

In the exception report, there was an `amazoncooliri` file missing. I couldn't find it in the blog XML. So I asked:

```markdown
Double-check the files mentioned in the missing-uploads.tsv. Do these files really exist in the XML? For example, it mentions "amazoncooliri". But there is no such word in the XML, I think, and uploads/amazoncooliris.jpg (which is probably what it refers to) exists. There may be similar mistakes. Make sure nothing required is missing either.
```

At first, I checked the code to see why `amazoncooliris` became `amazoncooliri`. But months of practicing ~~laziness~~ delegation took over and I had it debug itself.

Turned out it wrote `\\s` instead of `\s` which fixed it.

### Accept that you _will_ make mistakes

```markdown
Why are there PNG images in assets? I assumed there wouldn't be any and all would be WebP files...
```

It replied:

> Because the script only converts **JPEG → WebP**. For PNGs, it follows your instruction to “compress PNGs losslessly with 256 colors,” so they stay PNG.

OOPS AGAIN! I forgot to ask it to convert PNGs.

```markdown
Convert all PNGs to WebP using cwebp maximal effort with 256 color palette, just like the jpegs. Update, re-run, commit.
```

### Verification reports speed up reviews

Now for the big one: converting the blog posts.

```markdown
Now implement the plan in PLAN.md to convert the WordPress XML export to Markdown files with front-matter. Write a Python script with inline dependencies that `uv run` can execute. Run it and generate all the Markdown files. Verify that everything looks good - especially edge cases.

Make a list of edge cases you could handle that I should verify.
Make a list of any edge cases you couldn't handle.
Share these as links to https://s-anand.net/blog/.... as well as the local relative paths.
```

Apart from converting the posts, it generated:

- `reports/edge-cases-unhandled.tsv` -- an exception report
- `reports/edge-cases-handled.tsv` -- a verification report

The verification report was handy. I could see the edge cases (e.g. upload URLs rewritten, iframes/tables/objects/scripts that were retained, WordPress comment blocks removed) and spot check quickly.

Without this, I would have spent a lot more time reviewing. This gave me _confidence_ that it had handled edge cases well.

### Generate easy-to-review to review content

I find it productive to have the agent generate content that is _easy_ to review. At this point, I had a bunch of Markdown files that were _very_ easy for me to scan. So I created an _extensive_ list of changes:

```markdown
Drop redundant or unchanging frontmatter. For example:

- Retain title, date, lastmod, slug, categories
- author: sanand is always the same. Drop
- draft: false and status: publish are redundant. Drop both
- url: is deriable from the slug. Drop. Same for wp_link
- If tags, excerpt, aliases, etc. are missing, drop them
- Drop meta: entirely
- Drop menu_order, ping_status, comment_status
- Drop wip_guid in favor of wp_id (retain wip_id)
- If I missed any other frontmatter, use the same principles.

Insert the featured image as the first element in the post, instead of the featured_image frontmatter.

Rewrite all the upload links (http://www.s-anand.net/blog/wp-content/uploads/xxx) to relative links to uploads/ (e.g. ../../uploads/xxx).

Rerun. Commit as you go.

Finally, write a script to detect all links to s-anand.net/ that are not covered by this approach. For example, I have a bunch of direct assets like https://www.s-anand.net/mystic-light.mp3 or other non-WordPress pages on my website. Create a TSV report with the link and the source.

PS: I keep editing prompt.md with my prompts. Keep ignoring it.
```

The last line was because I was also saving my prompts and it kept getting confused why a file it didn't create kept changing 🙂.

### Give it all your tools

I had it install Hugo and run it. (I could have set it up myself, but why bother?)

I allowed it to `ssh` to my server to check logs if needed.

In both cases, these are tools I would need to build and test. It makes sense to let the agent use them directly.

```markdown
Corrections:

- The relative URLs should be ../../assets/ not ../../uploads/ (my mistake)
- No action required on the file URLs and swf links. I'll handle those.

Now, use Hugo (install via `mise use -g hugo`) and generate a static site from the Markdown files.

Ensure that ALL the URLs from https://s-anand.net/blog/... are retained exactly, including URLs posts, pages, categories, tags, author pages, year (or other time period), etc. You can `ssh sanand` and scan logs if that'll help.

This will be deployed via GitHub pages. Create the GitHub action workflow to build and deploy the site on every push to main.

Commit as you go.
```

Note that I had made a mistake mentioning `uploads/` instead of `assets/`. This keeps happening.

I don't know _any_ Hugo, so this was a bold step. But the output would be easy to review (it's a static site), so **more reviewability = more confidence**.

After a _long_ time, it generated the static site. It managed to self-correct a bunch of stuff. For example:

> - I removed `--minify` because inline scripts with `<br />` in `posts/2011/2011-05-19-eating-more-for-less.md` break JS minification; HTML builds cleanly without minify.

### Prefer UI reviews over code reviews for ease

In fact, if required, have it _build_ a throw-away tool to help you review.

In my case, the output was _functional_ but ugly. So ugly that I couldn't review it properly. I suggested a few obvious fixes (like broken links) but the main ask was to pick a theme and make it look like my website.

```markdown
FYI: I removed mise.toml. Running `mise x hugo -- hugo` should still work, but feel free to reinstall.

Ensure that ALL LINKS are relative. For example, public/blog/index.html links to https://s-anand.net/blog/tamil-ai/ but I'd like to link to tamil-ai/ instead.

Pick and implement a nice, popular, lightweight theme that's suitable for blogs.

Include these features. Where possible, use modern, well-supported & popular plugins or themes rather than custom code.

- Below the title, have a single line showing the date created (date updated shown only if different from date created), categories with links to category pages, tags with links to tag pages (if any) are present.
- Code blocks should be syntax-highlighted.
- At the bottom, include a link to the next and the previous posts (with title).
- Add a footer to all pages that lists
  - All categories with links & post count
  - All year archives with links and post count
  - All pages with links

Run and test.
```

### You can resume if it hangs. Don't worry about context

This took forever and I think Codex crashed or hung or something. So I killed it, resumed, and asked:

```markdown
It's been a while... maybe you were stuck? Resume and complete.
```

It managed to resume. I'm not sure if there was some context loss or confusion, but I'm learning to worry less.

### Allow it design flexibility

Internal links were still broken. I didn't know why, nor enough to fix them. So, rather than make a design decision (e.g. always use full / absolute / relative URLs), I let it decide.

````markdown
There are several problems due to wrong relative paths. If it will be easier, feel free to switch back to absolute paths for /blog/ to fix them.

- Featured image URLs seem wrong. blog/ai-can-be-held-to-account/ links to "/blog/../assets/pig-court.webp" instead of just "../assets/pig-court.webp"
- When I visit /blog/2003/ the CSS is fine but it breaks in /blog/2003/page/2/ -- and the relative links from that page also break.
- The links from the footers in /blog/2003/ point to /2016/ instead of /blog/2016/ for example

Swap "Next" and "Prev". "Prev" indicates older posts.

Syntax highlighting of code blocks doesn't seem to be working. In blog/openai-tts-cost/ I see a single block like this.

```
<code lang="bash" class="language-bash">curl "https://api.openai.com/v1/organization/usage/audio_speeches?start_time=$(date -d '1 day ago' +%s)&amp;project_ids=$PROJECT_ID&amp;group_by=model" \
  -H "Authorization: Bearer $OPENAI_ADMIN_KEY" \
  -H "Content-Type: application/json"</code>
```
````

It decided to use absolute paths.

### Generate documentation

Apart from adding a few more features / fixes, I had it generate a README.md documenting what I would need to run this in the future.

```markdown
Add featured images as thumbnails to post listings (e.g. blog home, category pages, tag pages, archive pages). Ensure that there is a placeholder (an elegant blank image) if there is no featured image.

Left-align the footer links.

Now, clean-up and add a README.md that explains the structure of the repo, how to build and deploy, etc.
```

I also had it fix another design error I made. The placeholders I asked for didn't look good.

```markdown
Skip featured images in post listings, post pages, etc. if they don't exist. No need for a placeholder.
```

### Ask for effort estimates

At this point, things were fine. But I was curious if we could refactor a bit.

I'm concerned if it might mess it up, though. **Effort is a good proxy for errors**. So I asked it:

```markdown
How easy are these changes? Just tell me, don't implement them.

- Set it up so that the content/ directory is auto-generated from posts/ without needing to be committed.
- Drop the slug: frontmatter and instead, derive it from the filename.
- Embed the comments in the posts as Markdown, clearly distinguished from the content, rather than keep them in comments/
```

It's response:

- Auto-generate `content/` from `posts/` is moderate effort...
- Dropping `slug` frontmatter is easy if you accept Hugo’s filename‑based slug rules...
- Embedding comments into each post is moderate effort...

### Probe for confidence

I asked:

```markdown
What's Hugo's filename-based slug rules?
```

I didn't read the output. My aim was not to learn. It was more to glance at it, see if (based on my considerable experience in this area) if it looked reasonable. In short, I was **probing for confidence** -- its _and_ mine.

### Continue the session for the long tail

Normally, I would have created a new session to implement changes and fixes.

But the session was auto-compacting quite well. So rather than lose context, I had it create a build steps and run _several_ minor fixes over the next few days. I didn't need to specify the context again and again.

### Summary

Here're the lessons I distilled from this migration, tagged by whether it's new to me.

|   # | Lesson                                                | New? |
| --: | ----------------------------------------------------- | ---- |
|   1 | Create a `PLAN.md` before complex tasks               |      |
|   2 | Analyze data while planning                           | New  |
|   3 | Edit `PLAN.md` using the agent, not manually          | New  |
|   4 | Implement small steps, run and commit as you go       |      |
|   5 | Run post-mortems mid-way                              | New  |
|   6 | Ask for actionable exception reports                  | New  |
|   7 | Delegate verification to the agent                    |      |
|   8 | Accept that you _will_ make mistakes                  |      |
|   9 | Verification reports speed up reviews                 | New  |
|  10 | Generate easy-to-review to review content             |      |
|  11 | Give it all your tools                                |      |
|  12 | Prefer UI reviews over code reviews for ease          |      |
|  13 | You can resume if it hangs. Don't worry about context | New  |
|  14 | Allow it design flexibility                           | New  |
|  15 | Generate documentation                                |      |
|  16 | Ask for effort estimates                              | New  |
|  17 | Probe for confidence                                  | New  |
|  18 | Continue the session for the long tail                |      |
