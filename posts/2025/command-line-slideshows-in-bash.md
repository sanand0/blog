---
title: Command Line Slideshows in Bash
date: "2025-02-26T02:29:42Z"
lastmod: "2025-02-26T02:29:44Z"
categories:
  - coding
wp_id: 3937
---

![Command Line Slideshows in Bash](/blog/assets/C__Downloads_7Xp8rR2uJjXtGXHKSwylyPkja.webp)

<p>At <a href="https://2025.pyconfhyd.org/">PyConf Hyderabad</a>, I spoke about <a href="https://2025.pyconfhyd.org/speakers/s-anand">uv</a>. It's a package manager for Python.</p>
<p>I usually <em>mix live demos</em> into my narrative. So, rather than present with something static like PowerPoint (or Google Slides), I usually use:</p>
<ul class="wp-block-list">
<li><strong>Front-end</strong>: Custom HTML mixed with <a href="https://revealjs.com/">RevealJS</a> and <a href="https://codepen.io/">CodePen</a>. <a href="https://observablehq.com/">Observable</a> is a good, too.</li>
<li><strong>Python</strong>: <a href="https://jupyter.org/">Jupyter Notebooks</a>. <a href="https://marimo.com/">Marimo</a> is good, too.</li>
<li><strong>Others</strong>: <a href="https://www.markdownguide.org/">Markdown</a> and <a href="https://code.visualstudio.com/">VS Code</a> for most other things, e.g. SQL.</li>
</ul>
<p>For this talk, I needed to run commands on the shell. I evaluated:</p>
<ul class="wp-block-list">
<li><strong>VS Code + Terminal</strong>. Split screen is good. But slides in VS code were not obvious.</li>
<li><strong>Web App</strong>. Write a web shell with <a href="https://xtermjs.org/">xterm.js</a> and <a href="https://www.npmjs.com/package/node-pty">node-pty</a> and embed it in RevealJS. But it's too much work.</li>
<li><strong>Web terminals</strong>: <a href="https://github.com/butlerx/wetty">WeTTY</a>, <a href="https://github.com/tsl0922/ttyd">ttyd</a>, <a href="https://github.com/yudai/gotty">GoTTY</a>, etc. But they struggle on Windows. I'd need WSL or Docker.</li>
<li><strong><a href="https://asciinema.org/">Asciinema</a></strong>. But it's not interactive.</li>
</ul>
<p>So I <a href="https://chatgpt.com/share/67b83b6f-30d8-800c-9ea2-549bffc645e0">got ChatGPT to write me an app</a>:</p>

```markdown
Write a modern, compact Python program that parses a Markdown file and renders it section-by-section colorfully on the terminal.

A "section" is any text beginning with a heading until the next heading.

- uv run talk.py script.md should parse script.md and render the first section.
- Running uv run talk.py should render the next section. And so on.
- If no further sections are found, it should say so and end.

When rendering on the terminal,

- Headings should be very prominent. Highlight H1, H2 and H3 in decreasing order of prominence. Rest can be rendered normally
- **Bold** should be prominent. _Italics_ should be mildly emphasized.
- Code blocks and
  code fences
  should be colored distinctly.
- [Links](...) should be colored distinctly but the URLs can be ignored.

Use inline script dependencies. I think using rich and markdown2 would apt but you can decide.
```

<blockquote class="wp-block-quote">
<p><strong>An aside</strong>. These days, it's easier to <em>create</em> small tools than <em>search</em> for something that exists.</p>
</blockquote>
<p>The <a href="https://github.com/sanand0/uv-mega/blob/523a08bb8fae3246a35b55d39ffc5f93b1a7bf37/slide.py">code it wrote</a> works like this.</p>
<ol class="wp-block-list">
<li>Write a Markdown file that has my "slides". I used this <a href="https://github.com/sanand0/uv-mega/blob/523a08bb8fae3246a35b55d39ffc5f93b1a7bf37/README.md">README.md</a>.</li>
<li>Run <code>slide.py README.md</code>. It shows the first section ("slide") in <code>README.md</code>, colored and highlighted, and <em>exits</em>.</li>
<li>I can run any other commands on my shell, e.g. <code>uv run --with pandas,ipython ipython</code>, and show how it works.</li>
<li>Run <code>slide.py</code> again. It clears the screen and shows the next slide.</li>
</ol>
<script async="true" id="asciicast-7Xp8rR2uJjXtGXHKSwylyPkja" src="https://asciinema.org/a/7Xp8rR2uJjXtGXHKSwylyPkja.js"></script>
<p>This allowed me a new kind of workflow, where the <em>shell itself</em> is the slides layer.</p>

---

## Comments

<!-- wp-comments-start -->

- **[Voice coding is the new live coding - S Anand](/blog/voice-coding-is-the-new-live-coding/)** _21 Sep 2025 4:48 pm_ _(pingback)_:
  […] In Feb 2025 at PyConf Hyderabad, I tried a new slide format: command-line slideshows in bash. […]

<!-- wp-comments-end -->
