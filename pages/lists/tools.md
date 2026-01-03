---
title: Tools
date: 2025-04-15T00:00:00Z
---

Results of my software tool evaluations. 🟢 is my current choice and 🟡 is worth evaluating.

## Partial JSON parsers, 25 Dec 2025

[JS Libraries for Partial JSON](https://chatgpt.com/share/69575f00-350c-8003-a672-ab8026e81c75)

- 🟡 [jsonrepair 2,138 ⭐ Dec 2025](https://github.com/josdejong/jsonrepair): Repair invalid JSON documents. Summary: most credible “repair then parse” baseline—2.1k stars and very widely used; has a docs site + CLI; great when LLM output is _nearly_ JSON and you can repair at end or checkpoints.
- [stream-json 1,142 ⭐ Feb 2025](https://github.com/uhop/stream-json): Streaming JSON processing toolkit. Summary: 1.1k stars; broadest feature set for true streaming (token streams, filters, assemblers, JSONL, verifier) with minimal-memory design; best when your stream is valid JSON/JSONL and you want pipeline composition.
- [clarinet 465 ⭐ Aug 2023](https://github.com/dscape/clarinet): SAX-like streaming JSON parser. Summary: 465 stars; tiny/evented incremental parsing; great when you want events fast and will manage state yourself; less helpful for malformed/truncated JSON repair.
- [jsonparse 368 ⭐ Nov 2021](https://github.com/creationix/jsonparse): Pure-JS streaming JSON parser. Summary: 368 stars; older but simple; good building block, though modern maintenance signals weren’t captured here.
- [best-effort-json-parser 262 ⭐ Jul 2025](https://github.com/beenotung/best-effort-json-parser): Best-effort parsing for incomplete JSON. Summary: 262 stars; explicitly aimed at partial/LLM-truncated JSON; strongest choice when you need a usable partial value mid-stream.
- [streamparser-json 197 ⭐ Jan 2025](https://github.com/juanjoDiaz/streamparser-json): Streaming JSON parser for Node/Deno/browser. Summary: positioned as “fast dependency-free” and spec compliant; looks modern; I didn’t capture stars in sources, so verify popularity and cadence before committing.
- 🟡 [partial-json-parser-js 196 ⭐ Aug 2025](https://github.com/promplate/partial-json-parser-js): Parse partial JSON strings (LLM streaming). Summary: explicitly motivated by LLM partial JSON; supports streaming-to-UI use cases; popularity metrics weren’t captured, so treat as promising but verify maintenance and adoption.
- [JSON-- 7 ⭐ Sep 2016](https://github.com/faridnsh/JSON--): Selective streaming JSON parser. Summary: niche streaming approach inspired by JSONStream/jsonparse; evaluate if you want path-based extraction from streams.
- [json-parse-stream 14 ⭐ Apr 2014](https://github.com/chrisdickinson/json-parse-stream): Minimal streaming JSON parser. Summary: small project (14 stars); may be useful for tiny pipelines, but weaker popularity/momentum signals than the above.

## SonarQube alternatives, 22 Dec 2025

[SonarQube alternatives](https://claude.ai/share/685bcfe0-252a-4932-9fb9-7fdacaaf493a)

- [trivy 30,571 ⭐ Dec 2025](https://github.com/aquasecurity/trivy): Find vulnerabilities, misconfigurations, secrets, SBOM in containers, Kubernetes, code repositories, and clouds. **Summary**: The Swiss Army knife of security scanning; covers containers, IaC, secrets, dependencies, and filesystems in one tool. Best-in-class for cloud-native stacks.
- [eslint 26,719 ⭐ Dec 2025](https://github.com/eslint/eslint): Find and fix problems in your JavaScript code. **Summary**: The dominant JavaScript/TypeScript linter with 66M+ weekly npm downloads. Highly extensible plugin ecosystem; handles code quality but not security by default—add eslint-plugin-security for SAST.
- [gitleaks 24,330 ⭐ Dec 2025](https://github.com/gitleaks/gitleaks): Scan git repos (or files) for secrets using regex and entropy. **Summary**: Fast, widely adopted secrets scanner for CI/pre-commit. Simple TOML config, low false positives. Best-in-class for secrets detection.
- [semgrep 13,666 ⭐ Dec 2025](https://github.com/semgrep/semgrep): Lightweight static analysis for many languages. Find bug variants with patterns that look like source code. **Summary**: Multi-language SAST with code-like rule syntax. 30+ languages, GitLab's default SAST engine. CE is single-file analysis; cross-file needs paid tier.
- [rubocop 12,825 ⭐ Dec 2025](https://github.com/rubocop/rubocop): A Ruby static code analyzer and formatter based on the community Ruby style guide. **Summary**: The definitive Ruby linter with autofix. Covers style, complexity, and security (with rubocop-rails).
- [infer 15,465 ⭐ Dec 2025](https://github.com/facebook/infer): A static analyzer for Java, C, C++, and Objective-C. **Summary**: Deep interprocedural analysis for null pointer, memory leaks, thread safety. Production-proven at Facebook scale but steep learning curve.
- [reviewdog 8,906 ⭐ Dec 2025](https://github.com/reviewdog/reviewdog): Automated code review tool integrated with any code analysis tools regardless of programming language. **Summary**: The glue that posts any linter output as GitHub/GitLab PR comments. Essential for replicating SonarQube's PR decoration with OSS tools.
- [bandit 7,556 ⭐ Dec 2025](https://github.com/PyCQA/bandit): A tool designed to find common security issues in Python code. **Summary**: Python-specific SAST for security. Lightweight, fast, integrates well with CI. Limited to security (no code quality).
- [brakeman 7,174 ⭐ Dec 2025](https://github.com/presidentbeef/brakeman): A static analysis security vulnerability scanner for Ruby on Rails applications. **Summary**: Rails-specific security scanner. Finds SQLi, XSS, mass assignment issues. Production-proven, actively maintained.
- [gosec 8,583 ⭐ Dec 2025](https://github.com/securego/gosec): Go security checker inspects source code for security problems by scanning the Go AST. **Summary**: Go-specific SAST. Scans for hardcoded credentials, SQL injection, path traversal. Integrates with golangci-lint.
- [pmd 5,268 ⭐ Dec 2025](https://github.com/pmd/pmd): An extensible multilanguage static code analyzer. **Summary**: Mature Java-centric analyzer (also Apex, JS, XML). 300+ rules for code smells, complexity, copy-paste detection (CPD). Not security-focused.
- [pylint 5,621 ⭐ Dec 2025](https://github.com/pylint-dev/pylint): It's not just a linter that annoys you! **Summary**: Deep inference-based Python linter. More thorough than ruff but slower. Catches bugs other linters miss due to type inference.
- [django-DefectDojo 4,401 ⭐ Dec 2025](https://github.com/DefectDojo/django-DefectDojo): Open-Source Unified Vulnerability Management, DevSecOps & ASPM. **Summary**: The OSS "single pane of glass" for aggregating findings from multiple scanners. Handles dedup, triage, JIRA integration. Security-focused (not code quality).
- [DependencyCheck 7,360 ⭐ Dec 2025](https://github.com/dependency-check/DependencyCheck): OWASP dependency-check detects publicly disclosed vulnerabilities in application dependencies. **Summary**: Classic SCA tool using NVD/CPE matching. Supports Java, .NET, Node, Python. Higher false positive rate than commercial alternatives but free and comprehensive.
- [jacoco 4,460 ⭐ Dec 2025](https://github.com/jacoco/jacoco): Java Code Coverage Library. **Summary**: The standard for Java code coverage. Integrates with Maven, Gradle, SonarQube. Generates line/branch/complexity metrics. Required for coverage in any Java stack.
- [spotbugs 3,795 ⭐ Dec 2025](https://github.com/spotbugs/spotbugs): SpotBugs is FindBugs' successor. A tool for static analysis to look for bugs in Java code. **Summary**: Java bytecode analyzer for bug patterns. 400+ detectors including find-sec-bugs plugin for security. Complements PMD (source) vs SpotBugs (bytecode).
- [checkstyle 8,772 ⭐ Dec 2025](https://github.com/checkstyle/checkstyle): Tool for checking Java source code for adherence to a Code Standard. **Summary**: Java style enforcement (Google/Sun conventions). Not for bugs or security—purely formatting and conventions.
- [megalinter 2,347 ⭐ Dec 2025](https://github.com/oxsecurity/megalinter): MegaLinter analyzes 50 languages, 22 formats, 21 tooling formats, copy-pastes, spelling mistakes, and security issues. **Summary**: Meta-linter orchestrating 100+ tools in one CI job. "Run everything" approach with unified reporting. Great for breadth but complex to tune.
- [jscpd 5,108 ⭐ Dec 2025](https://github.com/kucherenko/jscpd): Copy/paste detector for programming source code. **Summary**: Multi-language duplication detection (SonarQube's "Duplications" equivalent). Supports 150+ formats. Essential for technical debt tracking.
- [bearer 2,510 ⭐ Dec 2025](https://github.com/Bearer/bearer): Code security scanning tool (SAST) to discover, filter, and prioritize security and privacy risks. **Summary**: Privacy-focused SAST with data-flow analysis. Identifies PII exposure and sensitive data handling issues beyond typical SAST.
- [horusec 1,285 ⭐ Dec 2025](https://github.com/ZupIT/horusec): Open source tool that improves identification of vulnerabilities in your project. **Summary**: Multi-language SAST aggregator with optional visualization platform. Combines multiple OSS scanners into unified report.
- [osv-scanner 8,237 ⭐ Dec 2025](https://github.com/google/osv-scanner): Vulnerability scanner written in Go using the Open Source Vulnerabilities (OSV) database. **Summary**: Google's SCA using OSV database (broader than NVD). Fast, accurate, actively maintained. Good OWASP Dependency-Check alternative.
- [coveragepy 3,296 ⭐ Dec 2025](https://github.com/coveragepy/coveragepy): The code coverage tool for Python. **Summary**: Standard Python coverage measurement. Line and branch coverage, HTML/XML reports, CI-friendly.
- [nyc 5,727 ⭐ Dec 2024](https://github.com/istanbuljs/nyc): The Istanbul command line interface for JavaScript code coverage. **Summary**: The standard JS coverage tool. Wraps Istanbul for CLI usage. Works with Jest, Mocha, etc.
- [codeql 9,056 ⭐ Dec 2025](https://github.com/github/codeql): CodeQL: the libraries and queries that power security researchers around the world. **Summary**: Semantic code analysis engine by GitHub. Deep cross-file analysis, custom queries. Free for public repos via GitHub Advanced Security.

## JavaScript SVG animation doodle library, 16 Dec 2025.

[Modern SVG path animation alternatives to Vivus](https://claude.ai/share/42dc868f-d56a-4f74-a5c2-005bfe5d1925) |
[Animate SVG with GSAP](https://chatgpt.com/share/69575f52-8bf8-800c-8a17-9a2405024057) |
[Gemini 🔒](https://gemini.google.com/u/2/app/f8e5a6d49dff9f44)

- 🟢 [anime 65,560 ⭐ Dec 2025](https://github.com/juliangarnier/anime): Use with anime.stagger. Fast, lightweight JavaScript animation engine with SVG line drawing via `strokeDashoffset`. **Summary:** Cleanest API for path drawing (`anime.setDashoffset` helper); ~17KB; free and actively maintained (v4 released 2024); excellent staggering and timeline features; best balance of simplicity and power for most use cases.
- 🟡 [lazy-line-painter 1,986 ⭐ Dec 2023](https://github.com/merri-ment/lazy-line-painter): Old but works. Modern JS library for SVG path animation with GUI editor. **Summary:** ~10KB; no dependencies; comes with Lazy Line Composer visual editor for designing animations without code; per-path timing control via data attributes; actively maintained; excellent for designers who want GUI workflow.
- 🟡 [vivus 15,451 ⭐ Jul 2022](https://github.com/maxwellito/vivus): Old but works. Lightweight library to animate SVGs with drawing appearance. **Summary:** ~10KB; zero dependencies; purpose-built for exactly this effect; includes Pathformer to convert shapes to paths; last release 2022 (stable but aging); simple API with multiple animation types (delayed, sync, oneByOne); good choice if you want minimal setup.
- [motion 30,529 ⭐ Dec 2025](https://github.com/motiondivision/motion): Modern animation library for React and vanilla JavaScript with `pathLength`, `pathSpacing`, `pathOffset` properties. **Summary:** ~18KB vanilla core; formerly Framer Motion; declarative API ideal for React but vanilla JS version works well; actively maintained; premium examples available; great scroll-linked animation support.
- [GSAP 23,435 ⭐ Dec 2025](https://github.com/greensock/GSAP): Heavy. Industry-standard JavaScript animation platform with DrawSVGPlugin for stroke reveal/hide. **Summary:** Most powerful option; ~60KB core; DrawSVGPlugin now FREE (was premium until 2024 Webflow acquisition); unmatched timeline control and sequencing; works everywhere; overkill for simple animations but essential for complex ones.
- [walkway 4,359 ⭐ Mar 2022](https://github.com/ConnorAtherton/walkway): Easy way to animate SVG path, line, and polyline elements. **Summary:** Ultra-lightweight ~3KB; simplest API of all options; best mobile performance per CSS-Tricks testing; not updated since 2017 but stable; limited features (just draws paths); ideal for simple one-off animations.
- [segment 1,739 ⭐ Feb 2018](https://github.com/lmgonzalves/segment): Library to draw and animate SVG path strokes with precise segment control. **Summary:** Ultra-lightweight <2KB; unique ability to animate arbitrary segments (not just 0-100%); supports circular/wrapping animations; not updated since 2017; best for partial stroke effects or animated dashes; works well alongside GSAP.

## Dependabot / Renovate dependency updater alternatives, 16 Dec 2025

[Renovate tool overview](https://chatgpt.com/share/69575fd6-e224-800c-a264-286098803b0d)

- 🟢 [npm-check-updates 10,091 ⭐ Dec 2025](https://github.com/raineorshine/npm-check-updates): CLI to find and upgrade newer versions of npm dependencies in your package.json. Summary: very popular and actively maintained Node-only updater; pure CLI with rich flags and config, ideal as a minimal building block in JS/TS dependency update workflows.
- [updatecli 833 ⭐ Dec 2025](https://github.com/updatecli/updatecli): **Complex**. Declarative update engine for files and dependencies across ecosystems. Summary: Go single-binary with strong docs and frequent releases; excels at CI-driven, GitOps-style updates and PRs beyond just package managers.
- [cli 370 ⭐ Dec 2025](https://github.com/dependabot/cli): **Heavy**. CLI for running Dependabot update jobs with Dockerized updaters. Summary: official GitHub tool reusing dependabot-core’s multi-ecosystem logic; powerful and scriptable but heavier due to Docker and job YAML.
- [buddy-bot 7 ⭐ Dec 2025](https://github.com/stacksjs/buddy-bot): Fast dependency update bot focused on modern JS/TS, PHP, and Zig. Summary: early-stage but promising Node-based CLI/Action aiming to be a lighter, faster alternative to Renovate/Dependabot for modern stacks; good experimental option but not yet battle-tested.
- [ganzua 5 ⭐ Dec 2025](https://github.com/latk/ganzua): Manage Python dependency lockfiles and pyproject constraints for uv/Poetry. Summary: highly opinionated, well-tested Python CLI with JSON-first outputs, ideal for scripting and CI workflows around Python dependency upgrades, especially in uv-centric environments.

## Trino vs DuckDB, 14 Dec 2025

[Trino vs DuckDB comparison](https://chatgpt.com/share/69575ffb-971c-800c-8a08-6e724ede8f73)

- 🟢 [duckdb 34,731 ⭐ Dec 2025](https://github.com/duckdb/duckdb) is lightweight, powerful, rapidly improving.
- 🔴 [trino 12,271 ⭐ Dec 2025](https://github.com/trinodb/trino) is more enterprise-y, lots of connectors, heavier.

## Markdown query tools, 04 Dec 2025

- 🔴 [ast-grep 11,524 ⭐ Dec 2025](https://github.com/ast-grep/ast-grep)
- 🟡 [mdq 1,656 ⭐ Aug 2025](https://github.com/yshavit/mdq)
- [mq 131 ⭐ Dec 2025](https://github.com/harehare/mq)

## Fuzzy matching libraries, 02 Dec 2025

Record linkage

- [splink 1,800 ⭐ Dec 2025](https://github.com/moj-analytical-services/splink)
- [dedupe 4,409 ⭐ Jul 2025](https://github.com/dedupeio/dedupe)
- [recordlinkage 1,033 ⭐ Feb 2024](https://github.com/J535D165/recordlinkage)

Fuzzy matching

- 🟡 [RapidFuzz 3,548 ⭐ Dec 2025](https://github.com/rapidfuzz/RapidFuzz) for fast fuzzy matching in Python
- [jellyfish 2,171 ⭐ Nov 2025](https://github.com/jamesturk/jellyfish) for phonetic matches
- 🟡 [fuzzball.js 631 ⭐ Nov 2025](https://github.com/nol13/fuzzball.js) for fuzzy matching in JS
- [sentence-transformers 17,933 ⭐ Nov 2025](https://github.com/huggingface/sentence-transformers) for semantic text similarity

Assignment algorithms

- [scipy 14,234 ⭐ Dec 2025](https://github.com/scipy/scipy) [linear_sum_assignment](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linear_sum_assignment.html)
- [linear-sum-assignment 0 ⭐ Oct 2025](https://github.com/mljs/linear-sum-assignment)

## .DOC reader, 01 Dec 2025

[Libraries for reading DOC files](https://chatgpt.com/share/69576028-a040-800c-8b47-9342b3e3227d)

- [pywin32 5,488 ⭐ Nov 2025](https://github.com/mhammond/pywin32): Python for Windows extensions (COM automation, Win32 APIs). Summary: extremely popular but Windows only
- [textract 4,382 ⭐ Dec 2024](https://github.com/deanmalmgren/textract): “Extract text from any document.” Requires antiword
- [tika 3,440 ⭐ Dec 2025](https://github.com/apache/tika): Apache Tika content detection + text/metadata extraction. Heavy
- 🔴 [unoconv 2,743 ⭐ Apr 2023](https://github.com/unoconv/unoconv): Universal Office Converter (LibreOffice/OpenOffice). Archived in favor of unoserver
- [textract 1,687 ⭐ Oct 2022](https://github.com/dbashford/textract): Node.js text extraction across many formats (incl. `.DOC`). Requires antiword
- [tika-python 1,633 ⭐ Apr 2025](https://github.com/chrismattmann/tika-python): Python bindings for Apache Tika server. Heavy
- 🟢 [unoserver 843 ⭐ Nov 2025](https://github.com/unoconv/unoserver): LibreOffice-based conversion server (replacement ecosystem for `unoconv`). Healthy adoption
- [libreoffice-convert 301 ⭐ Nov 2025](https://github.com/elwerene/libreoffice-convert): Node wrapper to convert using LibreOffice. Moderate popularity
- [node-word-extractor 148 ⭐ Jun 2024](https://github.com/morungos/node-word-extractor): Pure JS text extractor for Word files. Lightweight
- [Aspose.Words-for-Python-via-.NET 129 ⭐ Nov 2025](https://github.com/aspose-words/Aspose.Words-for-Python-via-.NET): Examples/showcases for Aspose.Words (on-prem). Smaller OSS adoption
- [catdoc 82 ⭐ Mar 2011](https://github.com/petewarden/catdoc): CLI to convert `.DOC` to text. C source, unmaintained
- [antiword 54 ⭐ Jan 2024](https://github.com/grobian/antiword): CLI extractor for old Word `.DOC`. C source

## Free Databases, 20 Nov 2025

[Free SQL Databases](https://chatgpt.com/share/69576047-2bc8-800c-889d-d5291957d37e)

- 🟡 Google BigQuery. 10GB + 1 TB queries per month. SQL - BigQuery. For example:
  ```bash
  gcloud auth activate-service-account --key-file=service-account.json --project=$PROJECT
  bq --location=US mk --dataset $PROJECT:data
  bq load --autodetect --skip_leading_rows=1 --source_format=CSV $PROJECT:data.$NAME $NAME.csv
  ```
- MotherDuck. 10GB + 10 compute hours per month. SQL - DuckDB
- 🟡 Cloudflare D1. 5GB + 5M read/writes per month. SQL - SQLite?
- Turso. 5GB + 500M read, 10M writes / month. SQL - libSQL
- Xata. 15 GB. SQL - Postgres
- Neon. 0.5 GB. SQL - Postgres
- 🟡 Supabase. 500MB expires after 1 week of inactivity. SQL - Postgres
- Note: Prisma is an ORM, not a platform.

## PDF optimization, 17 Nov 2025

[PDF compression tools comparison](https://chatgpt.com/share/6957604b-4f54-800c-980d-f431beccb036)

- 🟢 [GhostScript](https://ghostscript.org/). The undisputed leader
- [OCRmyPDF 31,766 ⭐ Nov 2025](https://github.com/ocrmypdf/OCRmyPDF): OCR and optimize scanned PDFs (adds searchable text layer). Star-leader with a very active community; shines on scanned/image-only PDFs where it can dramatically shrink size via OCR + image re-encoding; heavier stack (Python + Tesseract + Ghostscript/qpdf), but excellent docs and packaging.
- 🟡 [pdfcpu 8,248 ⭐ Nov 2025](https://github.com/pdfcpu/pdfcpu): Go-based PDF processor + CLI. Modern, single-binary CLI with a rich Go API; `optimize` command performs structural and image-level compression; active development and solid docs; great choice for infra/DevOps use or when you want an embeddable SDK.
- 🟡 [qpdf 4,475 ⭐ Nov 2025](https://github.com/qpdf/qpdf): Content-preserving PDF transformer. Rock-solid tool for structural optimizations, linearization, and encryption; limited for image downsampling but excellent as a component (and widely used under the hood by others); very mature codebase, rich manual, and strong momentum.
- [mupdf 2,417 ⭐ Nov 2025](https://github.com/ArtifexSoftware/mupdf): MuPDF viewer/library with `mutool` CLI. Lightweight C library and tools; `mutool clean` can compress/garbage-collect PDFs effectively; better at structural cleanup than fine-grained image control; good docs, active development, modest but solid community.
- [pdfsizeopt 858 ⭐ Nov 2024](https://github.com/pts/pdfsizeopt): Aggressive PDF size optimizer. Niche but powerful; chains multiple optimizers to heavily compress especially TeX/diagram PDFs; setup and runtime are relatively heavy; development cadence is slower, but still updated in 2023; best used when you want maximum compression and can tolerate complexity.
- [ghostpdl 164 ⭐ Nov 2025](https://github.com/ArtifexSoftware/ghostpdl): Mirror of Ghostscript/GhostPDL source. Canonical engine behind Ghostscript CLI (`gs`); extremely feature-rich with deep image-compression controls; modest star count but huge commit history and active releases (10.06.0 in 2025); not a “friendly” tool by default, but the most powerful low-level engine.

## HTML to Markdown, 11 Nov 2025

https://github.com/sanand0/research/tree/main/dom-markdown-extractor-eval

- [pandoc 40,127 ⭐ Nov 2025](https://github.com/jgm/pandoc) uses non-standard table format
- [turndown 10,430 ⭐ Oct 2025](https://github.com/mixmark-io/turndown) fails on tables
- [python-markdownify 1,840 ⭐ Aug 2025](https://github.com/matthewwithanm/python-markdownify) loses code language hints
- [html2text 568 ⭐ Oct 2023](https://github.com/jaytaylor/html2text) has messy output, loses info
- 🟢 [node-html-markdown 237 ⭐ Nov 2025](https://github.com/crosstype/node-html-markdown) is most accurate and modern

## Android workflow automation, 04 Nov 2025

[Native Android app approach](https://chatgpt.com/share/6957607a-361c-800c-9076-513b6e51b284)

- 🟡 [Automate](https://play.google.com/store/apps/details?id=com.llamalab.automate). The flowchart model is perfect for offline→online queues and error handling; >410 blocks cover storage, HTTP, background checks, and audio record. Documentation is excellent, and 2025 cadence is healthy. Supports Tasker plugins.
- [Tasker](https://play.google.com/store/apps/details?id=net.dinglisch.android.taskerm). Extremely active 2025 releases with AI Generator, massive plugin ecosystem, and deep device control. Once you set up profiles, it’s rock-solid. If you later want bespoke widgets, in-app scenes, or unusual intents, Tasker’s the ceiling.
- [MacroDroid](https://play.google.com/store/apps/details?id=com.arlosoft.macrodroid). Easiest on-ramp, huge install base, active updates, one-time low Pro unlock. Supports Tasker plugins.
- [IFTTT](https://play.google.com/store/apps/details/IFTTT?hl=en_ZA&id=com.ifttt.ifttt).

## Markdown slide tools, 27 Oct 2025

- [reveal.js 69,734 ⭐ Oct 2025](https://github.com/hakimel/reveal.js): HTML slide framework with first-class Markdown & huge plugin/theme ecosystem. **Summary:** the web runtime most wrappers target; long-lived, actively maintained; enormous ecosystem.
- 🟡 [slidev 40,888 ⭐ Oct 2025](https://github.com/slidevjs/slidev): Vite/Vue MD slides with live coding, drawings, recording, export (**PDF/PNG/PPTX**). **Summary:** best “modern dev” authoring UX; rapid releases. Heavy.
- [pandoc 39,797 ⭐ Oct 2025](https://github.com/jgm/pandoc): Universal doc converter; Markdown → reveal.js/Beamer/**pptx** via templates/filters. **Summary:** glue of many pipelines; frequent 2025 releases.
- [remark 12,927 ⭐ Jun 2024](https://github.com/gnab/remark): In-browser Markdown slideshow. **Summary:** historically influential but appears low-activity; simple and portable.
- [mdx-deck 11,473 ⭐ Jan 2023](https://github.com/jxnblk/mdx-deck): MDX-based slides. **Summary:** popular historically; **maintenance appears light/stale** in recent years.
- [slides 11,009 ⭐ Aug 2024](https://github.com/maaslalani/slides): **Terminal** Markdown presenter; code execution; pipes stdin. **Summary:** modern terminal UX.
- [spectacle 10,023 ⭐ Oct 2025](https://github.com/FormidableLabs/spectacle): React (JSX/MD/MDX) slides; maintained. **Summary:** great for React devs; CLI available.
- 🟢 [marp 9,851 ⭐ Aug 2025](https://github.com/marp-team/marp): Markdown → HTML/PDF/PowerPoint with themes. **Summary:** solid all-rounder; active 2025 releases; VS Code extension popular.
- [presenterm 7,114 ⭐ Oct 2025](https://github.com/mfontanini/presenterm): **Terminal** slides with GIFs, themes, PDF export. **Summary:** feature-rich terminal tool.
- [hedgedoc 6,548 ⭐ Oct 2025](https://github.com/hedgedoc/hedgedoc): Collaborative Markdown editor with **reveal.js** presentation mode. **Summary:** if you want multiuser editing + slides.
- [mdp 5,125 ⭐ Jul 2025](https://github.com/visit1985/mdp): **Terminal** Markdown presenter (ncurses). **Summary:** tiny, fast, minimalist.
- [quarto-cli 4,960 ⭐ Oct 2025](https://github.com/quarto-dev/quarto-cli): Scientific/tech publishing; Markdown → **reveal.js**, Beamer, etc. **Summary:** batteries-included reproducible docs/slides with Pandoc under the hood.
- [reveal-md 3,877 ⭐ Sep 2025](https://github.com/webpro/reveal-md): Markdown → reveal.js CLI. **Summary:** convenient CLI; **now deprecated**; points to **MkSlides**/Slidev.
- [lookatme 2,270 ⭐ Apr 2024](https://github.com/d0c-s4vage/lookatme): **Terminal** Markdown slides with embedded terminals. **Summary:** superb for live CLI demos; Python/pip.
- [markdeck 1,264 ⭐ Feb 2023](https://github.com/arnehilmann/markdeck): Dockerized Markdown → reveal.js with niceties (PDF, side-by-side). **Summary:** “presentations as code” with Pandoc + reveal.js.
- [xaringan 1,517 ⭐ Aug 2025](https://github.com/yihui/xaringan): R Markdown → **remark.js** slides. **Summary:** popular in R community (remark-based).
- [obsidian-advanced-slides 1,166 ⭐ Jun 2024](https://github.com/MSzturc/obsidian-advanced-slides): Obsidian → reveal.js slides plugin. **Summary:** powerful Obsidian workflow; note some repo/store policy turbulence in 2021–23.
- [revealjs 329 ⭐ Mar 2025](https://github.com/rstudio/revealjs): R Markdown format for reveal.js. **Summary:** R-centric wrapper; integrates with RStudio.
- [revealgo 241 ⭐ Feb 2024](https://github.com/yusukebe/revealgo): Single-binary Go server for Markdown → reveal.js. **Summary:** super light; great local dev UX.
- [mkslides 165 ⭐ Oct 2025](https://github.com/MartenBE/mkslides): Modern **successor to reveal-md** CLI. **Summary:** actively maintained CLI to build reveal.js slides from Markdown.
- [markdownslides 58 ⭐ Oct 2023](https://github.com/a-nau/markdownslides) (docs site): Jekyll + reveal.js template for GitHub Pages. **Summary:** dead-simple GH Pages hosting for Markdown slides.

## Read .env-like files / secrets, 26 Oct 2025

[Command line secret tools](https://chatgpt.com/share/6957607c-5104-800c-8d62-25d33dcb747e)

- 🟢 `awk -F= -v k="$KEY" '$1==k{print substr($0,index($0,"=")+1);exit}' .env` is the fastest, near-zero dependencies
- [jq 32,868 ⭐ Oct 2025](https://github.com/jqlang/jq): JSON processor. Summary: de-facto standard for JSON querying; latest release 1.8.0 on 2025-06-01; huge ecosystem and tutorials.
- [sops 19,790 ⭐ Oct 2025](https://github.com/getsops/sops): Encrypted files (YAML/JSON/ENV/TOML) with KMS/age/GPG; `--extract`. Summary: strong security story; widely used in GitOps; active docs/guides in 2025.
- [yq 14,304 ⭐ Oct 2025](https://github.com/mikefarah/yq): Multi-format (YAML/JSON/XML/INI/CSV/TSV/properties) processor. Summary: single portable binary; frequent 2025 releases (v4.48.1 on 2025-10-12; INI support in 4.46.1); excellent docs.
- [direnv 14,209 ⭐ Oct 2025](https://github.com/direnv/direnv): Per-directory env with export features. Summary: mature, frequent releases (v2.37.1 on 2025-07-20); great for “auto-load” and CI exports.
- [godotenv 9,904 ⭐ Oct 2025](https://github.com/joho/godotenv): `.env` loader for Go with CLI to run commands. Summary: minimal, battle-tested; useful in shells and Go apps.
- [python-dotenv 8,446 ⭐ Oct 2025](https://github.com/theskumar/python-dotenv): `.env` loader **with CLI (`get/list/run`)**. Summary: well-known; good docs; integrates cleanly in Python stacks.
- [dasel 7,661 ⭐ Oct 2025](https://github.com/TomWright/dasel): Query/modify JSON/YAML/TOML/XML/CSV via one syntax. Summary: handy all-in-one selector; release cadence slower since mid-2024; docs OK.
- [gopass 6,531 ⭐ Oct 2025](https://github.com/gopasspw/gopass): Team-friendly `pass` reimplementation (GPG/age). Summary: CLI-first, scripting-friendly; good if you like “one secret per file”.
- [dotenvx 4,525 ⭐ Oct 2025](https://github.com/dotenvx/dotenvx): modern `.env` tool with `get/set/run` and encrypted `.env.vault`. Summary: very approachable; strong docs; integrates encryption cleanly.
- [git-secret 3,914 ⭐ Oct 2025](https://github.com/sobolevn/git-secret): GPG-encrypt files in Git. Summary: bash-native; good distro packaging; straightforward workflows.
- [password-store 694 ⭐ Jun 2025](https://github.com/zx2c4/password-store): Read-only mirror of `pass`. Summary: classic UNIX password store (official home is outside GitHub); simple CLI, many clients.
- [crudini 467 ⭐ Jun 2025](https://github.com/pixelb/crudini): INI file CLI. Summary: small and practical; **0.9.6 (Apr 16, 2025)**; widely packaged.

## Windows in Linux, 19 Oct 2025

[Evaluate Windows apps on Linux](https://chatgpt.com/share/695760b0-b070-800c-a143-2545168b7615)

- [Proton 27,948 ⭐ Oct 2025](https://github.com/ValveSoftware/Proton): Compatibility tool for Steam (Wine + DXVK/VKD3D). **27.9k⭐.** Summary: huge momentum; frequent Experimental updates; great for graphics-heavy Windows apps via Linux.
- [reactos 16,436 ⭐ Oct 2025](https://github.com/reactos/reactos): Windows-compatible OS (alpha). **16.4k⭐.** Summary: research-grade; not production-ready; interesting long-term bet.
- [winboat 12,270 ⭐ Oct 2025](https://github.com/TibixDev/winboat): Containerized Windows VM; RDP-published apps. **12.3k⭐.** Summary: fast-moving; slick app-publishing; heavier than Wine; needs Windows license.
- [winapps 11,361 ⭐ Oct 2025](https://github.com/winapps-org/winapps): RDP-backed .desktop Windows apps from a VM. **10.2k⭐.** Summary: proven idea with renewed community; good integration for Office-style apps.
- [lutris 9,159 ⭐ Sep 2025](https://github.com/lutris/lutris): Runner/launcher for games (Wine/Proton). **9.2k⭐.** Summary: great scripts and community; also usable for non-games; steady 2025 releases.
- 🟡 [Bottles 7,460 ⭐ Oct 2025](https://github.com/bottlesdevs/Bottles): Modern Wine manager. **6.7k⭐.** Summary: delightful UX, curated runners, active releases; easiest place to start.
- [wine 3,650 ⭐ Oct 2025](https://github.com/wine-mirror/wine): Upstream Wine mirror. **3.7k⭐.** Summary: the base; most scriptable; learning curve higher than GUIs.
- [virt-manager 2,858 ⭐ Oct 2025](https://github.com/virt-manager/virt-manager): GUI for KVM/libvirt. **2.6k⭐.** Summary: powerful, reliable VM management; heavier but closest to native with KVM.
- [phoenicis 725 ⭐ Apr 2025](https://github.com/PhoenicisOrg/phoenicis): PlayOnLinux 5 rewrite. **1.2k⭐.** Summary: aging compared to Bottles; still useful scripts.
- [virtualbox 722 ⭐ Oct 2025](https://github.com/VirtualBox/virtualbox): Oracle VirtualBox source. **722⭐.** Summary: new to GitHub; robust hypervisor; extension pack is proprietary.
- [POL-POM-4 474 ⭐ Dec 2024](https://github.com/PlayOnLinux/POL-POM-4): Legacy PlayOnLinux 4. **474⭐.** Summary: largely superseded by Bottles/Phoenicis.
- [q4wine 233 ⭐ Aug 2025](https://github.com/brezerk/q4wine): Qt GUI for Wine. **233⭐.** Summary: minimal GUI for power users.

## UNIX tools, 13 Oct 2025.

List files

- 🟢 [eza 17,857 ⭐ Oct 2025](https://github.com/eza-community/eza/): Fast, large directories, colors, icons, git status, tree view, customizable.
- [lsd 14,922 ⭐ Oct 2025](https://github.com/lsd-rs/lsd): User-friendly defaults.

File manager

- 🟢 [yazi 28,863 ⭐ Oct 2025](https://github.com/sxyazi/yazi): Fast terminal file manager. Rust. Batteries included. Visual previews, tabs, bulk operations.
- [nnn 20,708 ⭐ Sep 2025](https://github.com/jarun/nnn): Minimal terminal file manager. Plugins for functionality.
- [broot 11,971 ⭐ Oct 2025](https://github.com/Canop/broot): File navigation and search.

Disk usage

- 🟢 [dust](https://github.com/bootandy/dust): quick, visual overview of disk usage
- 🟢 [ncdu](https://github.com/rofl0r/ncdu): interactive exploration of disk usage

## Declarative development environments, 12 Oct 2025

[Alternatives to devenv.sh](https://chatgpt.com/share/695760b1-df90-800c-8f3b-3b5b7a32997f)

- [asdf 24,421 ⭐ Oct 2025](https://github.com/asdf-vm/asdf): Extendable, plugin-based runtime manager. **Summary:** huge plugin ecosystem; slower than single-binary tools; conservative cadence; reliable baseline for polyglot runtimes.
- [nixpkgs 22,034 ⭐ Oct 2025](https://github.com/NixOS/nixpkgs): The Nix package set & NixOS. **Summary:** 120k+ packages; constant updates; backbone for Nix dev shells; steepish learning but unmatched breadth.
- 🟢 [mise 20,374 ⭐ Oct 2025](https://github.com/jdx/mise): Single-binary runtime manager + tasks. **Summary:** very active releases (Oct 2025); fast UX; great default if you don’t need full system images.
- [nix 15,235 ⭐ Oct 2025](https://github.com/NixOS/nix): The Nix package manager. **Summary:** the reproducibility engine; modern releases; pairs with flakes/devShell.
- [devpod 14,099 ⭐ Jul 2025](https://github.com/loft-sh/devpod): Client-only, OSS “Codespaces-like” runner for Dev Containers anywhere. **Summary:** spec-aligned, IDE-agnostic, avoids vendor lock-in; great team standardization.
- [direnv 14,150 ⭐ Sep 2025](https://github.com/direnv/direnv): Per-directory env loader for shells. **Summary:** feather-light, modern, integrates with Nix/Mise/asdf; frequent 2025 releases.
- [devbox 10,471 ⭐ Oct 2025](https://github.com/jetify-com/devbox): Nix-powered, friendly per-project envs. **Summary:** easier Nix adoption; auto-installs Nix if missing; good docs.
- [che 7,081 ⭐ Oct 2025](https://github.com/eclipse-che/che): K8s-native cloud dev environments (Devfile). **Summary:** enterprise-grade, OSS; more ops surface than DevPod.
- [devenv 5,794 ⭐ Oct 2025](https://github.com/cachix/devenv): Nix-based “project as a service”. **Summary:** services/DBs/.env/processes declaratively; sharp DX on top of Nix.
- [spack 4,815 ⭐ Oct 2025](https://github.com/spack/spack): HPC-oriented package/env manager. **Summary:** unbeatable for scientific toolchains; too heavy for most app teams.
- [nix-direnv 2,360 ⭐ Oct 2025](https://github.com/nix-community/nix-direnv): Fast `use_nix`/`use_flake` for direnv. **Summary:** snappy activation; simpler than `lorri`.
- [cli 2,149 ⭐ Oct 2025](https://github.com/devcontainers/cli): Reference CLI for Dev Container spec. **Summary:** the canonical way to build/run `devcontainer.json` locally/CI; pairs with any IDE.

## Document/Graph/Realtime Databases, 06 Oct 2025

[SurrealDB vs alternatives evaluation](https://chatgpt.com/share/695760e6-8080-800c-818a-9fe266f3690d)

- 🟢 [supabase 89,611 ⭐ Oct 2025](https://github.com/supabase/supabase): Open-source Firebase alternative on Postgres (auth, realtime, storage). **Summary**: huge community, generous free tier, superb DX; not graph-native.
- [pocketbase 51,424 ⭐ Oct 2025](https://github.com/pocketbase/pocketbase): Open-source realtime backend in one file (SQLite). **Summary**: ultra-light single binary; great for rapid apps and prototypes.
- [graphql-engine 31,725 ⭐ Oct 2025](https://github.com/hasura/graphql-engine): Instant GraphQL APIs on Postgres, realtime subscriptions. **Summary**: production-grade realtime GraphQL; strong tooling and docs.
- [surrealdb 30,136 ⭐ Oct 2025](https://github.com/surrealdb/surrealdb): Multi-model doc-graph DB with LIVE queries. **Summary**: ambitious single-binary + realtime; **great DX, maturing perf evidence**; active 2025 releases.
- [mongo 27,621 ⭐ Oct 2025](https://github.com/mongodb/mongo): MongoDB server (SSPL). **Summary**: dominant document DB; robust tooling; Atlas from ~$9/mo shared, ~$60/mo dedicated.
- [rethinkdb 26,946 ⭐ Sep 2025](https://github.com/rethinkdb/rethinkdb): Realtime document DB with changefeeds. **Summary**: classic realtime pioneer; revived releases (2.4.4 in 2023); stable but slower cadence.
- [libsql 15,630 ⭐ Oct 2025](https://github.com/tursodatabase/libsql): SQLite fork for the edge. **Summary**: great for distributed SQLite; not graph; fits local-first/edge.
- [neo4j 15,158 ⭐ Oct 2025](https://github.com/neo4j/neo4j): Native graph database. **Summary**: top graph engine and ecosystem; best at deep traversals; managed Aura with consumption pricing.
- [arangodb 13,937 ⭐ Oct 2025](https://github.com/arangodb/arangodb): Multi-model database (doc/graph/kv). **Summary**: most mature “doc+graph” in one; great breadth; Neo4j still wins pure graph.
- [electric 9,289 ⭐ Oct 2025](https://github.com/electric-sql/electric): Realtime sync layer for Postgres (not a DB). **Summary**: powerful for local-first apps; pairs well with Postgres; use when sync is the hard part.
- [couchdb 6,689 ⭐ Oct 2025](https://github.com/apache/couchdb): Document DB with replication & `_changes`. **Summary**: rock-solid sync + changefeed model; great for offline-first.
- [orientdb 4,879 ⭐ Oct 2025](https://github.com/orientechnologies/orientdb): Multi-model DB (document-graph). **Summary**: featureful, older project; popularity has cooled vs Arango/Neo4j. _(Star count not independently verified in this pass.)_

## Command runners / Task automation tools, 05 Oct 2025

[Evaluate command runners](https://chatgpt.com/share/695760e8-5348-800c-8db5-aece59564653)

- 🟡 [zx 44,662 ⭐ Sep 2025](https://github.com/google/zx): JS-first scripting. **Summary:** replaces bash with ergonomic JS; great glue for tasks.
- [gulp 33,049 ⭐ Jun 2025](https://github.com/gulpjs/gulp): Streaming JS task runner. **Summary:** mature; still maintained; ecosystem has shifted, but solid.
- [turborepo 28,784 ⭐ Oct 2025](https://github.com/vercel/turborepo): Monorepo build system with remote caching. **Summary:** Rust engine, active releases, great for JS/TS mono-repos.
- [just 27,968 ⭐ Sep 2025](https://github.com/casey/just): Command/recipe runner. **Summary:** minimal, fast, single binary; frequent releases.
- [nx 27,162 ⭐ Oct 2025](https://github.com/nrwl/nx): Monorepo task graph & caching. **Summary:** frequent releases (e.g., 2025-10-02), enterprise-ready.
- [mise 19,731 ⭐ Oct 2025](https://github.com/jdx/mise): Dev toolchains + **tasks** in one binary. **Summary:** good if you also want version/tool mgmt (Node/PNPM/Bun/etc.) plus tasks.
- [fabric 15,256 ⭐ Jul 2025](https://github.com/fabric/fabric): Pythonic local/remote tasks. **Summary:** operations-friendly, builds on Invoke & Paramiko.
- [task 13,844 ⭐ Oct 2025](https://github.com/go-task/task): YAML task runner (Go). **Summary:** polyglot sweet spot; single binary; strong 2025 cadence.
- [ninja 12,303 ⭐ Sep 2025](https://github.com/ninja-build/ninja): Ultra-fast build executor. **Summary:** tiny, very fast; best via generators (CMake/Meson); latest 2025-07-10.
- [berry 7,862 ⭐ Oct 2025](https://github.com/yarnpkg/berry): Yarn v2+ monorepo/PM features. **Summary:** if you’re on Yarn, scripts + workspaces do a lot; not a standalone runner.
- [mage 4,477 ⭐ Jun 2025](https://github.com/magefile/mage): Tasks in Go. **Summary:** zero DSL; slower recent cadence; nice in Go shops.
- [jake 1,974 ⭐ Aug 2025](https://github.com/jakejs/jake): Node’s Make/Rake-like tool. **Summary:** mature but niche now; fine for classic Node.
- **GNU Make** _(official home: GNU Savannah; GitHub is a mirror: [make 223 ⭐ Sep 2024](https://github.com/mirror/make))_: Ubiquitous task runner. **Summary:** everywhere; non-GitHub canonical source; stable.

Also:

- [deno 104,597 ⭐ Oct 2025](https://github.com/denoland/deno): JS/TS runtime with built-in `deno task`. **Summary:** great when your repo is Deno-first; tasks live in `deno.json`; modern DX and fast runtime.
- [bun 80,693 ⭐ Oct 2025](https://github.com/oven-sh/bun): Fast JS runtime/PM/tester; `bun run` for scripts. **Summary:** blazing startup; best if you standardize on Bun.
- [cli 9,179 ⭐ Oct 2025](https://github.com/npm/cli): npm itself. **Summary:** baseline for `package.json` scripts; ubiquitous; not a separate runner.

## Embedded databases, 28 Sep 2025

[Evaluate embedded databases](https://chatgpt.com/share/6957611c-21f0-800c-bc22-d060b70a3be7)

SQL:

- 🟢 [duckdb 33,079 ⭐ Sep 2025](https://github.com/duckdb/duckdb): Embedded columnar SQL for analytics. Summary: fast OLAP in-process; rich file-format I/O; frequent releases (**v1.4.0, 2025-09-16**); excellent docs + extensions.
- 🟡 [libsql 15,606 ⭐ Sep 2025](https://github.com/tursodatabase/libsql): Open-contrib fork of SQLite + remote protocol. Summary: SQLite compatibility with community PRs, replication, `sqld`; active releases (**2025-02-14**).
- 🟢 [sqlite 8,392 ⭐ Sep 2025](https://github.com/sqlite/sqlite): Official Git mirror of SQLite. Summary: canonical embedded SQL; legendary stability; latest release **3.47.0 (2025-09-10)**; pair with sync tools or libSQL/Turso for edge.
- [LiteDB 9,084 ⭐ Sep 2025](https://github.com/litedb-org/LiteDB): Single-file NoSQL for .NET. Summary: simple embedded store for C#; steady releases (**7.0.20**, 2025-08-18).
- [h2database 4,455 ⭐ Sep 2025](https://github.com/h2database/h2database): JVM-native embeddable RDBMS. Summary: ideal for Java tests/apps; frequent maintenance (e.g., **2.3.232**).

Key-value / Graph:

- [leveldb 38,188 ⭐ Jan 2025](https://github.com/google/leveldb): Ordered KV library (C++). Summary: extremely popular but **limited maintenance**; great for simple embedded KV; no SQL; consider RocksDB/Badger for ongoing momentum.
- [rocksdb 30,692 ⭐ Sep 2025](https://github.com/facebook/rocksdb): LSM KV engine. Summary: high-write KV, deep tuning options, constant releases (**9.7.0, 2025-09-23**); industry workhorse for embedded KV.
- [badger 15,039 ⭐ Sep 2025](https://github.com/hypermodeinc/badger): Pure-Go LSM KV with ACID SSI. Summary: production-proven, nightly bank tests, clear docs; great when you want no-cgo perf.
- [kuzu 3,352 ⭐ Sep 2025](https://github.com/kuzudb/kuzu): Embedded graph-relational DB. Summary: columnar + property graph features; modern features & frequent releases (e.g., **0.9.2, 2025-09-20**); promising but younger ecosystem.
- [bbolt 9,110 ⭐ Sep 2025](https://github.com/etcd-io/bbolt): Embedded B+tree KV (Go). Summary: dead-simple, stable; perfect for config/meta stores and read-heavy use; limited feature surface by design.
- [pebble 5,531 ⭐ Sep 2025](https://github.com/cockroachdb/pebble): RocksDB-style LSM KV in pure Go. Summary: tuned for Cockroach workloads; strong engineering quality; good choice in Go services.
- [sled 8,707 ⭐ May 2025](https://github.com/spacejam/sled): Modern Rust embedded store. Summary: ergonomic API; “beta” status persists; fun and fast but judge risk for prod.

## JS Agent Libraries, 23 Sep 2025

[JavaScript agent libraries](https://chatgpt.com/share/6957611d-c850-800c-95d8-0424a47eabe8)

- [ai 17,942 ⭐ Sep 2025](https://github.com/vercel/ai) by Vercel
- 🟢 [openai-agents-js 1,402 ⭐ Sep 2025](https://github.com/openai/openai-agents-js/)

## JS Formatters, 21 Sep 2025

[Evaluate JS linters](https://chatgpt.com/share/6957614b-be50-800c-ab5c-0c6af52dc49c)
[10 Oct 2025: Markdown formatters evaluation](https://chatgpt.com/share/6957614d-a7bc-800c-b7a8-e9ec33feb439)

- [deno 104,283 ⭐ Sep 2025](https://github.com/denoland/deno): JavaScript/TypeScript runtime with built-in `deno fmt`. Summary: **batteries-included** formatter for JS/TS/JSON/Markdown and (behind flags) HTML/CSS/YAML/Svelte/Vue/Astro; clear CLI options (`--check`, `--line-width`, `--single-quote`, etc.); modern docs; zero cost; delegates to dprint.
- [bun 80,469 ⭐ Sep 2025](https://github.com/oven-sh/bun): All-in-one JS runtime; docs and third-party guides mention `bun fmt`. Summary: promising _built-in_ formatter, but **official docs are light**; you’d adopt Bun mainly if you already run it. Treat `bun fmt` as **emerging**; verify features in your env.
- 🟢 [prettier 50,978 ⭐ Sep 2025](https://github.com/prettier/prettier): De-facto multi-language formatter. Summary: **huge ecosystem & stability**, rich plugin story (Tailwind, PHP, etc.), broad formats (JS/TS/CSS/HTML/Markdown/YAML/GraphQL); regular releases (e.g., 3.6.2 on 2025-06-27); Node-based so heavier than single-binary tools; speed is “good enough,” not its aim.
- [standard 29,359 ⭐ Jul 2025](https://github.com/standard/standard): Zero-config style/lint preset that formats via ESLint fixers. Summary: beloved “no config” workflow; **formatting coverage limited to ESLint stylistic rules**, not a structural printer; still useful if you want one tool and conventional style.
- [eslint 26,269 ⭐ Sep 2025](https://github.com/eslint/eslint) (+ [eslint-stylistic 1,828 ⭐ Sep 2025](https://github.com/eslint-stylistic/eslint-stylistic)): Linter with fixers; with Stylistic, acts as a formatter. Summary: **scriptable & CLI-friendly**; great for teams who prefer rules-as-code; formatting breadth depends on rule sets; not a full pretty-printer like Prettier/Biome.
- [biome 21,125 ⭐ Sep 2025](https://github.com/biomejs/biome): Rust single-binary **formatter + linter** (Rome’s successor). Summary: **very fast** formatter; supports JS/TS/JSX/JSON/**CSS**/GraphQL; claims \~97% Prettier compatibility; frequent releases (e.g., v2.2.4 on 2025-09-10); no Prettier-style plugin ecosystem (on purpose); great docs; small footprint.
- [beautify-web/js-beautify](https://github.com/beautify-web/js-beautify): Older beautifier. Summary: stable and simple, but **narrower modern-JS coverage** than Prettier/Biome; plugin ecosystem is minimal; still fine for legacy HTML/CSS/JS.
- 🟢 [dprint 3,603 ⭐ Sep 2025](https://github.com/dprint/dprint): Rust **pluggable** formatter (single binary) with plugins (TS/JS/JSON/Markdown/TOML/etc.). Summary: **fast** and light; strong plugin story (including a Prettier wrapper and Biome JS/TS wrapper); modern docs; validate formatting parity for edge cases.
- [pretty-quick 2,276 ⭐ Jun 2025](https://github.com/prettier/pretty-quick): Runs Prettier on changed files. Summary: not a formatter—**a runner** that makes Prettier fast on pre-commit/CI; tiny and focused; updated recently (v4.2.2 on 2025-06-02).

## JS Linters, 21 Sep 2025

[Evaluate JS linters](https://chatgpt.com/share/6957617f-717c-800c-a7aa-4c15fd0ea70e)

- [standard 29,359 ⭐ Jul 2025](https://github.com/standard/standard): “JavaScript Standard Style”—opinionated, zero-config style & linter built on ESLint. Summary: biggest “no-config” community; stable, batteries-included defaults; excellent if you want one enforced style without tweaking.
- [eslint 26,269 ⭐ Sep 2025](https://github.com/eslint/eslint): The de-facto JavaScript/TypeScript linter with a huge plugin ecosystem. Summary: most extensible and battle-tested; maximal ecosystem leverage; heavier setup if you want strict “no-config.”
- [biome 21,125 ⭐ Sep 2025](https://github.com/biomejs/biome): Fast toolchain (linter+formatter+more) in Rust/TypeScript; drop-in JS/TS linter. Summary: modern, fast, batteries-included alternative; great DX; ecosystem smaller than ESLint’s.
- 🟢 [oxc 16,410 ⭐ Sep 2025](https://github.com/oxc-project/oxc): Rust toolchain; includes **oxlint** (ultra-fast JS/TS linter). Summary: blazing speed and growing rule set; type-aware checks emerging; plugin story evolving; strong momentum.
- [jshint 9,040 ⭐ Feb 2025](https://github.com/jshint/jshint): Legacy JS linter. Summary: historically important; still used, but maintenance cadence and modern rule coverage trail newer tools.
- [xo 7,871 ⭐ Aug 2025](https://github.com/xojs/xo): Opinionated, zero-config ESLint wrapper with strict defaults. Summary: delightful defaults and smooth “no config” UX; coverage derives from ESLint + curated plugins; development cadence modest; great if you want ESLint’s ecosystem without managing config.
- [jslint 3,645 ⭐ Apr 2025](https://github.com/jslint-org/jslint): Original, opinionated JS linter. Summary: ultra-strict, zero-config philosophy; niche but actively updated; limited ecosystem compared to ESLint/Biome/Oxlint.
- [deno_lint 1,578 ⭐ Sep 2025](https://github.com/denoland/deno_lint): Rust linter powering `deno lint`. Summary: extremely fast; best fit for Deno projects; fewer rules and plugins than ESLint family.
- [quick-lint-js 1,577 ⭐ Jun 2025](https://github.com/quick-lint/quick-lint-js): Native (C++) linter focused on instant feedback. Summary: very fast with rich editor integrations; narrower rule coverage; ecosystem smaller.
- [Flet/semistandard](https://github.com/Flet/semistandard): “standard, with semicolons.” Summary: minimal fork of StandardJS for teams that require semicolons; inherits Standard/ESLint ecosystem.
- [neostandard 320 ⭐ Sep 2025](https://github.com/neostandard/neostandard): “Spiritual successor” to StandardJS using modern ESLint flat config. Summary: active, modernized take on Standard; chasing full rule parity; fast-growing but early-stage ecosystem.

## JS Test frameworks, 21 Sep 2025

[Evaluate JS test runners](https://chatgpt.com/share/69576180-eacc-800c-80bb-dfb59c362dc1)

- [node 113,327 ⭐ Sep 2025](https://github.com/nodejs/node): Node.js core runtime; includes the native `node:test` runner. Summary: built-in, zero-dep baseline with solid stability; lean feature set vs ecosystem frameworks.
- [jest 45,049 ⭐ Sep 2025](https://github.com/jestjs/jest): All-in-one JS testing framework with snapshots, mocks, watch mode. Summary: huge ecosystem and docs; heavier runtime but battle-tested for apps and libs.
- [mocha 22,838 ⭐ Sep 2025](https://github.com/mochajs/mocha): Flexible, modular test runner for Node and browser. Summary: mature + configurable with many reporters; requires separate assertion/mocking libs.
- [ava 20,830 ⭐ Jul 2025](https://github.com/avajs/ava): Concurrent test runner with isolated processes. Summary: clean DX and parallelism; smaller plugin ecosystem than Jest/Mocha.
- [jasmine 15,828 ⭐ Sep 2025](https://github.com/jasmine/jasmine): BDD testing framework for browser and Node. Summary: self-contained (assert/mocks included); older style but actively maintained.
- 🟢 [vitest 14,987 ⭐ Sep 2025](https://github.com/vitest-dev/vitest): Vite-powered, Jest-compatible test runner. Summary: very fast dev loop, great TS/ESM support; ecosystem growing quickly.
- [tape 5,787 ⭐ Mar 2025](https://github.com/tape-testing/tape): Minimal TAP-producing test harness. Summary: tiny, deterministic output; minimal features and smaller plugin surface.
- [uvu 3,021 ⭐ Aug 2024](https://github.com/lukeed/uvu): Extremely fast, minimal test runner. Summary: impressive speed but the repo is archived—use cautiously for new projects.
- [tapjs 2,396 ⭐ Feb 2025](https://github.com/tapjs/tapjs): TAP-format test runner/CLI with rich reporters. Summary: good for TAP pipelines and CLI power-users; niche vs mainstream frameworks.
- [web 2,354 ⭐ Aug 2025](https://github.com/modernweb-dev/web): Monorepo for “Modern Web” tools incl. Web Test Runner. Summary: standards-first browser testing; solid for ESM/web-component stacks; smaller community than Jest/Vitest.

## JS Test automation, 21 Sep 2025

- 🟢 [playwright](https://github.com/microsoft/playwright-python). Apache 2.0. De facto standard.
- [Cypress](https://www.cypress.io/).

## LLM Voice Cloning, 21 Sep 2025

[Evaluate voice cloning models](https://chatgpt.com/share/695761b1-84f4-800c-9738-20acbe8cff09)

- 🟡 [TTS 42,693 ⭐ Aug 2024](https://github.com/coqui-ai/TTS): Open-source neural TTS stack (incl. XTTS-v2 zero-shot). Summary: battle-tested, multilingual, large ecosystem; modern and active; setup heavier than single-model repos but pays off in flexibility
- [OpenVoice 34,466 ⭐ Apr 2025](https://github.com/myshell-ai/OpenVoice): Fast voice cloning and timbre/style transfer. Summary: very popular, simple to run, great for instant cloning; lighter than most and frequently updated
- [fish-speech 22,976 ⭐ Sep 2025](https://github.com/fishaudio/fish-speech): Large-scale, high-quality TTS models and training code. Summary: high audio quality, big-model orientation; heavier requirements but strong results
- [GPT-SoVITS 51,016 ⭐ Sep 2025](https://github.com/RVC-Boss/GPT-SoVITS): GPT-SoVITS zero-shot voice cloning / conversion. Summary: impressive zero-shot cloning; community-driven and fast-moving; ops can be fiddly
- [CosyVoice 16,506 ⭐ Sep 2025](https://github.com/FunAudioLLM/CosyVoice): CosyVoice 2 multilingual TTS & voice cloning. Summary: strong research cadence from Alibaba; good quality; GPU-friendly but not the lightest
- [NeMo 15,733 ⭐ Sep 2025](https://github.com/NVIDIA-NeMo/NeMo): Framework for speech (ASR/TTS), LLMs & multimodal. Summary: enterprise-grade, scalable; superb docs; heavier infra assumptions; great if you want training + inference recipes
- [VoiceCraft 8,386 ⭐ Mar 2025](https://github.com/jasonppy/VoiceCraft): Zero-shot speech editing/inpainting with context-aware modeling. Summary: state-of-the-art for edit/infill; research-grade builds; not a turnkey “clone my voice” tool
- [StyleTTS2 5,974 ⭐ Aug 2024](https://github.com/yl4579/StyleTTS2): Style-controllable TTS with natural prosody. Summary: widely cited baseline for naturalness; training/inference scripts are clear; lighter than many research stacks
- [google-cloud-python 5,111 ⭐ Sep 2025](https://github.com/googleapis/google-cloud-python): Official Google Cloud TTS client (Python) inside mono-repo. Summary: stable client library; excellent docs; managed service backend
- [cognitive-services-speech-sdk 3,304 ⭐ Sep 2025](https://github.com/Azure-Samples/cognitive-services-speech-sdk): Samples for Microsoft Speech SDK (incl. Custom Neural Voice). Summary: solid examples across languages; production-ready SDK; CNV itself is gated
- [Resemblyzer 3,091 ⭐ Oct 2023](https://github.com/resemble-ai/Resemblyzer): Voice embeddings toolkit (by Resemble AI). Summary: not the API SDK, but the org’s most useful open tool; great for voice similarity pipelines around Resemble
- [elevenlabs-python 2,728 ⭐ Sep 2025](https://github.com/elevenlabs/elevenlabs-python): Official ElevenLabs Python SDK. Summary: straightforward, well-maintained SDK; pairs with strong docs & examples; closed-source backend
- [python-clients 105 ⭐ Sep 2025](https://github.com/nvidia-riva/python-clients): Python clients & CLI for NVIDIA Riva (ASR/TTS/NLP). Summary: good client utilities for on-prem low-latency speech; works with Riva server; stars lower than NeMo but fit for prod
- [pyht 216 ⭐ Aug 2025](https://github.com/playht/pyht): Official PlayHT Python SDK for realtime TTS/voice cloning API. Summary: simple, streaming-first; feature coverage evolving; closed-source backend
- [docs 1 ⭐ Sep 2025](https://github.com/cartesia-ai/docs): Cartesia API docs config (Fern). Summary: not an SDK, but official docs source; API is rapidly evolving; closed-source backend
- [sample-amazon-polly 0 ⭐ Apr 2025](https://github.com/aws-samples/sample-amazon-polly): Examples & notebooks for Amazon Polly. Summary: simple getting-started repo; production usage typically via AWS SDKs; service is extremely stable

## LLM Observability Tools, 18 Sep 2025

[Logfire alternatives evaluation](https://chatgpt.com/share/695761b2-d930-800c-a18c-785b53b0e29b)

- [mlflow 22,135 ⭐ Sep 2025](https://github.com/mlflow/mlflow): End-to-end ML lifecycle; GenAI tracing/evals now built-in. Summary: huge ecosystem and stable APIs; self-hostable but heavier than LLM-only tools; great if you want one platform for classic ML + LLMs with REST/CLI
- 🟢 [langfuse 16,330 ⭐ Sep 2025](https://github.com/langfuse/langfuse): Open-source LLM tracing, evals, datasets, feedback. Summary: fast, intuitive UI; easy self-hosting; strong SDKs and REST; popular choice for lightweight W\&B-for-LLMs
- [opik 14,052 ⭐ Sep 2025](https://github.com/comet-ml/opik): Open-source eval/tracing/monitoring platform. Summary: production-grade, self-hostable with Docker/Helm; comprehensive dashboards and REST API; a bit heavier but enterprise-ready
- [ragas 10,808 ⭐ Sep 2025](https://github.com/explodinggradients/ragas): LLM evals toolkit. Summary: excellent metrics/test-set gen; pairs well with tracers like Langfuse/Laminar; not an observability store by itself
- [gateway 9,532 ⭐ Sep 2025](https://github.com/Portkey-AI/gateway): High-performance AI gateway (routing/guardrails/telemetry). Summary: popular, fast, self-hostable; good fit if you want routing + observability via one gateway and a clean REST API
- [phoenix 7,021 ⭐ Sep 2025](https://github.com/Arize-ai/phoenix): LLM + ML observability and evaluation. Summary: strong eval UX and notebooks; self-hostable; heavier stack than “just-tracing” tools but powerful for analysis
- [evidently 6,617 ⭐ Sep 2025](https://github.com/evidentlyai/evidently): OSS framework for evals/testing/monitoring (ML & LLM). Summary: 100+ metrics, great reports; self-hostable monitoring; more metrics-driven than tracing-first
- [helicone/helicone](https://github.com/helicone/helicone): Proxy to log/monitor LLM API traffic. Summary: super-simple drop-in logging, fast onboarding; self-hostable; great for call logs/costs, lighter on eval features
- [trulens 2,792 ⭐ Sep 2025](https://github.com/truera/trulens): Evaluation + tracking for LLM apps/agents. Summary: flexible feedback functions and UI; lightweight to start; good if you want eval-first with some tracing
- [openllmetry 6,416 ⭐ Sep 2025](https://github.com/traceloop/openllmetry): OpenTelemetry auto-instrumentation for LLMs. Summary: vendor-neutral, fast, self-hostable backends (Grafana/Tempo/etc.); great if you want OSS OTel traces over a custom UI
- [uptrain 2,325 ⭐ Aug 2024](https://github.com/uptrain-ai/uptrain): Unified LLM evals with local dashboard. Summary: runs locally/self-host; easy, opinionated checks and RCA; complements separate tracers
- [lmnr 2,298 ⭐ Sep 2025](https://github.com/lmnr-ai/lmnr): Laminar—OSS tracing + evals (Rust backend). Summary: fast, modern, self-hostable (ClickHouse/Postgres); good REST/gRPC; promising all-in-one with low overhead
- [logfire 3,596 ⭐ Sep 2025](https://github.com/pydantic/logfire): Structured logging/tracing for Python apps by Pydantic. Summary: delightful DX and very low overhead; great for metrics/costs/traces; note the SDK is OSS while the hosted backend is not fully OSS/self-host yet
- [weave 985 ⭐ Sep 2025](https://github.com/wandb/weave): OSS framework for LLM app evaluation/experiments (W\&B ecosystem). Summary: clean abstractions and dashboards; lighter than full W\&B but smaller community; self-host via OSS server
- [langsmith-sdk 643 ⭐ Sep 2025](https://github.com/langchain-ai/langsmith-sdk): Client SDKs for LangSmith. Summary: polished tracing/evals + tight LangChain integration; platform itself is managed (no full OSS self-host); SDKs are MIT and easy to onboard
- [braintrustdata/braintrust](https://braintrust.dev): Proprietary evals/test-datasets & experimentation. Summary: strong dataset/eval workflows and REST; not a full observability store; pairs well with tracers/gateways

Past evals in Jun 2025: [Observability Tools Comparison](https://chatgpt.com/share/695762d5-eeb0-800c-a407-cf6f11f90096)

## Full Text Search, 2 May 2025

[Grok Deep Research](https://x.com/i/grok/share/hAT9orfUKayMCGVa2lWoPTZx2) and [Gemini Deep Research](https://g.co/gemini/share/94923f8109d5)

- [elasticsearch 72,539 ⭐ May 2025](https://github.com/elastic/elasticsearch)
- 🟢 [meilisearch 50,908 ⭐ May 2025](https://github.com/meilisearch/meilisearch)
- [typesense 22,920 ⭐ May 2025](https://github.com/typesense/typesense)
- [OpenSearch 10,590 ⭐ May 2025](https://github.com/opensearch-project/OpenSearch)
- [solr 1,373 ⭐ Apr 2025](https://github.com/apache/solr)

## LLM Clients, 2 May 2025

[Popular Open Source LLM UIs](https://chatgpt.com/share/695761e1-a2d4-800c-b6c5-b995ad26ea74)

- 🟢 [open-webui 92,565 ⭐ May 2025](https://github.com/open-webui/open-webui): Chat‑GPT–style, self‑hosted UI that auto‑discovers local Ollama models or remote OpenAI‑compatible endpoints; comes with a built‑in model builder, voice/video chat, agent presets, Helm/Kustomize deployments, and a single‑container “Ollama‑bundled” image.
- [NextChat 83,144 ⭐ Apr 2025](https://github.com/ChatGPTNextWeb/NextChat): Lightweight PWA & desktop app; works offline, syncs across Web/iOS/Android/macOS/Windows/Linux; toggles between Claude, DeepSeek, GPT‑4, Gemini and more via a simple ENV switch.
- [lobe-chat 60,040 ⭐ May 2025](https://github.com/lobehub/lobe-chat): Modern React/Next.js framework; plug‑in system for function calling, speech‑synthesis, multimodal uploads, knowledge‑base RAG and “one‑click” Vercel/Tauri deploys.
- [langflow 58,006 ⭐ May 2025](https://github.com/langflow-ai/langflow): Drag‑and‑drop visual builder for agent graphs; every flow becomes an API endpoint; ships with enterprise auth, LangSmith/LangFuse observability and Helm charts for IDE vs runtime separation.
- [anything-llm 43,537 ⭐ May 2025](https://github.com/Mintplex-Labs/anything-llm): Desktop & Docker suite that ingests arbitrary docs into a built‑in vector store and lets multiple users chat or spawn no‑code agents; supports any OpenAI‑compatible LLM & DB combo.
- [text-generation-webui 43,420 ⭐ May 2025](https://github.com/oobabooga/text-generation-webui): A “Stable‑Diffusion‑WebUI for text”: Gradio‑based front‑end, three prompt modes, hot‑swap between llama.cpp, Transformers, ExLlama, TensorRT‑LLM, etc., plus portable zero‑install builds.
- [Flowise 37,820 ⭐ May 2025](https://github.com/FlowiseAI/Flowise): Low‑code pipeline canvas focused on LangChain agents; RAG templates, credential vault, REST/WS endpoints, multi‑tenant auth and composable node SDK.
- [gradio 37,792 ⭐ May 2025](https://github.com/gradio-app/gradio): Drop‑in OpenAI‑API server that runs CPUs or GPUs; ships a React WebUI, galleries for gguf models, P2P inference mesh, image/audio/voice‑cloning endpoints.
- [chatbot-ui 31,114 ⭐ Aug 2024](https://github.com/mckaywrigley/chatbot-ui): Minimalist Next.js template many teams fork to slap a branded front‑end on any LLM; themeable, mobile‑friendly, no backend opinion—just bring your own fetch().
- [pinokio 4,930 ⭐ Apr 2025](https://github.com/pinokiocomputer/pinokio): Electron browser that ships pre‑scripted “recipes” (LM Studio, Diffusion UI, etc.); lets non‑technical users spawn full LLM stacks with one click and keeps them sandboxed.

## LLM CLI tools, 28 Apr 2025

[Command-line LLM Tools](https://chatgpt.com/share/695761e3-a710-800c-b9b5-03f44a899674)

- [codex 43,201 ⭐ Sep 2025](https://github.com/openai/codex)
- [aider 37,545 ⭐ Sep 2025](https://github.com/Aider-AI/aider). Apache 2.0. Advanced “pair-programming” CLI that maps your repo, applies edits, runs tests, and commits changes with descriptive messages.
- [shell_gpt 11,369 ⭐ Jul 2025](https://github.com/TheR1D/shell_gpt). MIT. A wrapper for GPT models offering REPL, function calling, multi-step workflows, and cache management.
- 🟢 [llm 9,701 ⭐ Aug 2025](https://github.com/simonw/llm). Apache 2.0. A versatile CLI and Python library for prompting remote or local models, storing results in SQLite, managing embeddings, and more.
- [aichat 8,164 ⭐ Sep 2025](https://github.com/sigoden/aichat). MIT. A unified CLI for interacting with various open-source and hosted LLMs, supporting conversational and single-prompt modes.
- [gorilla-cli 1,352 ⭐ May 2024](https://github.com/gorilla-llm/gorilla-cli). Apache 2.0. Generates API calls and shell commands across 1,500+ services, with user approval before execution.
- [ai-shell 5,014 ⭐ Jul 2025](https://github.com/BuilderIO/ai-shell). MIT. Converts natural-language prompts into shell commands, with interactive execution and chat modes.
- [shell_sage 363 ⭐ Jun 2025](https://github.com/AnswerDotAI/shell_sage). Apache 2.0. Understands terminal context. accepts piped responses. Targets specific tmux panes.
- [llm-cmd 437 ⭐ May 2025](https://github.com/simonw/llm-cmd). Apache 2.0. Generates and executes shell commands via natural-language prompts, with optional sandboxing.
- [tmuxai 1,164 ⭐ Sep 2025](https://github.com/alvinunreal/tmuxai). Apache 2.0. Integrates AI suggestions and chat directly into tmux sessions for code snippets and command generation.
- [CodeGrab 51 ⭐ Apr 2025](https://github.com/epilande/CodeGrab). MIT. Lightweight CLI for making instant API calls to various LLMs and receiving structured JSON responses.
- [y-cli 183 ⭐ Jun 2025](https://github.com/luohy15/y-cli). MIT. A Tiny Terminal Chat App for AI Models with MCP Client Support
- [warp.dev](https://www.warp.dev). Proprietary. A modern terminal emulator offering built-in AI features: “Bring Your Own LLM,” unlimited AI requests, and integrated workspaces.

## LLM Computer Use Agents, 27 Apr 2025

[Computer use agent tools](https://chatgpt.com/share/69576220-14f8-800c-a2e5-1257713d854b)

GitHub: [cua](https://github.com/topics/cua) | [computer-use](https://github.com/topics/computer-use) | [ai-agent](https://github.com/topics/ai-agent)

- [open-interpreter 59,220 ⭐ Apr 2025](https://github.com/OpenInterpreter/open-interpreter) – **open-source (AGPL-3.0)**. Lets an LLM write/run Python, JS, Shell, or Bash locally; can open a browser tab, edit files, plot data, or call any CLI tool. Works on **macOS, Linux, Windows** (plus Termux & Colab). Big community, plugin system, optional voice mode, and a desktop GUI in beta.
- [cua 5,072 ⭐ Apr 2025](https://github.com/trycua/cua) – **open-source (MIT)**. Spins up near-native **macOS or Linux** VMs on Apple-Silicon Macs (“Lume”) and exposes a vision+action API so any model can pilot the VM. Gives you GPU-accelerated isolation and reproducible sandboxes; ideal when you don’t want an agent touching your main OS.
- [Operator](https://operator.chatgpt.com/) (OpenAI) – **closed-source research preview** launched **23 Jan 2025**. Runs a GPT-4o-powered “Computer-Using Agent” that sees web pages, clicks, scrolls, fills forms, and hands control back to the user when needed. Hosted in an OpenAI-managed Chromium sandbox, so it works from any OS with a browser. Safety layers require confirmation for payments and log-ins.
- [Claude Computer Use](https://www.anthropic.com/news/3-5-models-and-computer-use) – **closed beta** inside Claude 3.5 Sonnet (since late 2024). Developers get an API that streams screenshots and accepts mouse/keyboard actions, letting Claude automate GUI workflows inside a VM. Cross-platform; still experimental and slower than humans but first “general” computer-use feature from a foundation-model vendor.
- [Agent-S 2,921 ⭐ Apr 2025](https://github.com/simular-ai/Agent-S) – **open-source (Apache-2.0)**. A “generalist-specialist” framework that chains specialist GUI skills under a planner. Scores SOTA on OSWorld/WebArena, supports **macOS, Windows, Linux, Android** via the companion _gui-agents_ lib, and integrates memory/evaluation loops for continual learning.
- [open-computer-use 1,073 ⭐ Mar 2025](https://github.com/e2b-dev/open-computer-use) – **open-source (Apache-2.0)**. Launches a secure **Ubuntu** desktop in E2B’s cloud sandbox, then orchestrates three LLM roles (grounding, vision, action). Streams the desktop to your browser and lets you pause/override at any time. Plug-in list of >10 models.
- [surf 344 ⭐ Apr 2025](https://github.com/e2b-dev/surf) – **open-source (Apache-2.0)**. A polished Next.js front-end that wires **OpenAI Operator-style agents** to an E2B sandbox. Single command to boot a virtual desktop, chat, and watch the agent work. Good starter template for web-based CUAs.
- [gptme 3,751 ⭐ Apr 2025](https://github.com/gptme/gptme) – **open-source (MIT)**. A terminal-first personal agent that can run shell commands, edit files, browse the web, and use local or cloud LLMs. Works on **Linux, macOS, Windows**; great when you want automation in the CLI rather than the GUI.
- [pig-python 148 ⭐ Mar 2025](https://github.com/pig-dot-dev/pig-python) – **open-source SDKs (Apache-2.0)** for [Pig](https://www.pig.dev/) cloud service. Provides on-demand **Windows 11** VMs and an API that exposes high-level GUI primitives (type, click, window focus). Targets RPA-style workloads; still alpha, but unique for Windows-first focus and low-latency streaming.
- [langgraph-cua-py 139 ⭐ Mar 2025](https://github.com/langchain-ai/langgraph-cua-py) – **open-source (MIT)**. Shows how to build a computer-use agent as a LangGraph state machine, defaulting to **Ubuntu** VMs from Scrapybara but swappable. Provides nodes for vision, memory, human-in-the-loop, and streaming.
- [openmacro 101 ⭐ Oct 2024](https://github.com/Openmacro/openmacro) – **open-source (MIT)**. Early-stage multimodal assistant that executes Python snippets locally via SambaNova models. Cross-platform CLI; profile system lets you switch API keys or tool sets. Inspired by OpenInterpreter but lighter weight.
- [computer-agent 437 ⭐ Jan 2025](https://github.com/suitedaces/computer-agent) – **open-source (MIT)**, small but lively community. A PyQt desktop wrapper that lets **Claude Computer Use** drive your actual machine. Shows practical wiring from Anthropic’s API to local mouse/keyboard events; tested on Linux & Windows.

## LLM Routers, 27 Apr 2025

[LLM Routers Comparison](https://chatgpt.com/share/6957621c-77c4-800c-80cb-79e506aed53a)

- 🟢 [litellm 21,561 ⭐ Apr 2025](https://github.com/BerriAI/litellm)
- [gateway 7,741 ⭐ Apr 2025](https://github.com/Portkey-AI/gateway)
- [RouteLLM 3,861 ⭐ Aug 2024](https://github.com/lm-sys/RouteLLM)
- [helicone 3,670 ⭐ Apr 2025](https://github.com/Helicone/helicone). 15+ providers (OpenAI, Anthropic, Bedrock, Groq, Gemini, …). **Auth**: Helicone org key + BYO provider keys. **Rate-limit**: soft limits via dashboard alerts, no enforced throttling (observability focus).
- [FastChat 38,467 ⭐ Apr 2025](https://github.com/lm-sys/FastChat). Local/remote self-hosted models (e.g., Mixtral, Llama). **Auth**: Bearer key pass-through. **Rate-limit**: none (use external proxy).
- [apisix 15,066 ⭐ Apr 2025](https://github.com/apache/apisix). 100+ providers via plugins (OpenAI, Claude, Gemini, Mistral, …). **Auth**: JWT, Key-Auth, OIDC, HMAC. **Rate-limit**: token/request per consumer/route, distributed leaky-bucket.
- [envoy 25,889 ⭐ Apr 2025](https://github.com/envoyproxy/envoy). Provider-agnostic (define clusters manually). **Auth**: mTLS, API key, OIDC via filters. **Rate-limit**: global/local via Envoy’s rate-limit service.
- [openllmetry 5,711 ⭐ Apr 2025](https://github.com/traceloop/openllmetry). Configurable providers (OpenAI, Azure, Anthropic, local vLLM). **Auth**: OpenAI-style key, BYO keys. **Rate-limit**: Redis-backed token/RPS optional.
- [kong 40,702 ⭐ Apr 2025](https://github.com/Kong/kong). Multi-provider via “ai-llm-route” plugin. **Auth**: Key-Auth, ACL, OIDC via plugins. **Rate-limit**: per-key, per-route, cost-aware token limits.
- [semantic-router 2,561 ⭐ Apr 2025](https://github.com/aurelio-labs/semantic-router)
- [unify 296 ⭐ Apr 2025](https://github.com/unifyai/unify). Providers wrapped via LiteLLM. **Auth**: Unify project key, BYO provider keys. **Rate-limit**: soft budget alerts; no enforced throttling yet.
- [ArchGW](https://github.com/katanemo/arch)
- [OpenRouter](https://openrouter.ai/)
- [Martian Model Router](https://withmartian.com/)

## Large File Storage

[Cloudflare R2 sync options](https://chatgpt.com/share/69576253-a758-800c-bcb7-60fe73fc635d)

To store a bunch of data files (e.g. parquet) under 1GB, here are options:

- 🟢 **GitHub Releases**. 2 GiB **per file**, unlimited total & bandwidth. 🟢 Immortal URL, versioning, easy CI publish. 🔴 Each file must stay < 2 GiB; no built-in SQL. 🔴 No CORS
- 🟢 **Cloudflare R2**. 10 GB storage & 1 M ops / month. 🟢 S3 API, CORS, zero-egress to Cloudflare Workers, fast. 🔴 10 GB cap.
- **Backblaze B2**. 10GB free free. 🟢 S3 API, CORS.
- **Zenodo** (CERN). 50 GB per record; one-off bumps to 200 GB. 🟢 CORS, DOI assignment, archival mandate. 🔴 Occasional throttled bandwidth; no API for partial file reads.
- **Hugging Face Hub**. 300 GB per repo; 50 GB per file. 🟢 Git-based, CORS, dataset tooling, lively ML community. 🔴 Large files need git-LFS; pushes via LFS can be slow.
- **Kaggle Datasets**. 20 GB per dataset, public only.🟢 Built-in notebooks & GPU. 🔴 No programmatic SQL API; quotas sometimes change.
- **data.world (free)**. 1 GB total, 100 MB per dataset. 🟢 Nice social features. 🔴 Too small for your size.

Cloud services:

- **AWS S3**. 5GB free.
- **GCP Storage**. 5GB free. CORS is tricky.
- **Azure Storage**. 5GB free.
- **DigitalOcean Spaces**. 250 GB-months.
- **Supabase Storage**. 2GB free.
- **IPFS**:
- **Open Science Framework (OSF)**: 50 GB free.

## How to pick a Vector Data Store

- Filter on [Vector DB Comparison](https://superlinked.com/vector-db-comparison). Look for:
  - Hygiene:
    - License: if that's a deal-breaker
    - Managed: if that's necessary
    - Sharding: if high scale is required
    - Multi-tenancy: for regulatory requirements
    - RAG API support: if critical
  - Hybrid search: Allows text + similarity searchh
  - BM25: Handles fuzze text search
  - Filters & Facets: Allows picking from subsets, e.g. role-based access
  - Full Text
  - Maybe:
    - Multiple indices: HNSW = fast with high RAM. IVF-PQ = low RAM with recall loss, DiskANN = slow but scales
    - Sparse: Efficient storage with higher quality
- [Pricing (ChatGPT)](https://chatgpt.com/share/6821a25a-9f80-800c-8d95-8b2200ad6de4)

  | Service                        |      $ |
  | ------------------------------ | -----: |
  | Cloudflare Vectorize           |   0.38 |
  | TurboPuffer (min $64/mo)       |   1.12 |
  | Pinecone (Serverless)          |   1.27 |
  | Supabase (pgvector Micro)      |  10.00 |
  | Redis Cloud Flex (~3 GB)       |  15.00 |
  | Elastic Serverless             |  65.84 |
  | Weaviate Cloud (Serverless)    |  73.00 |
  | Qdrant Cloud (4 CPU / 8 GB)    | 107.16 |
  | Azure AI Search (S1 1 SU)      | 245.28 |
  | AWS OpenSearch Serverless      | 350.00 |
  | Google Vertex AI Vector Search | 547.50 |

## PDF to Markdown, 21 Apr 2025

[OCR Quality Comparison](https://chatgpt.com/share/6806f7e1-f01c-800c-a8e5-44b3d50d736f)

- If you _only_ need to parse references from text‑native PDFs (or reliably OCR’ed ones), **GROBID** + a good OCR (e.g. OCRmyPDF/Tesseract or a commercial engine) is still the de facto choice.
- If you want an _end‑to‑end_ cloud API that gives you back both text and layout (so you can easily isolate the References section), **Mistral OCR** shows the most promise today—just be prepared to do a light post‑processing pass.
- If you already use Azure services and need enterprise SLA, **Azure Document Intelligence** will give you excellent raw OCR; layering on a small custom model or post‑processing pipeline can yield solid reference extraction, but it won’t match GROBID out of the box.

Archive: 23 Dec 2024

- [PyMuPDF4LLM](https://pymupdf.readthedocs.io/en/latest/pymupdf4llm/) uses [MuPDF](https://mupdf.com/). Requires PyTorch.
  - `PYTHONUTF8=1 uv run --with pymupdf4llm python -c 'import pymupdf4llm; h = open("pymupdf4llm.md", "w"); h.write(pymupdf4llm.to_markdown("$FILE.pdf"))'`
- 🟢 [markitdown](https://github.com/microsoft/markitdown) from Microsoft. PDF via PDFMiner, DOCX via Mammoth, XLSX via Pandas, PPTX via Python-PPTD, ZIP, etc.
  - `PYTHONUTF8=1 uvx markitdown $FILE.pdf > markitdown.md`
- [Docling](https://github.com/DS4SD/docling) by IBM. Unable to install via pip on Windows AND on Linux.
- [MegaParse](https://github.com/QuivrHQ/MegaParse) uses libreoffice, pandoc, tesseract-ocr, etc. Requires OpenAI API key.

## Database Migration

[Migration Framework Comparison](https://chatgpt.com/share/69576283-dc70-800c-b1a9-ebd1f4291b3a)

- 🟢 [dbmate 6,050 ⭐ Jun 2025](https://github.com/amacneil/dbmate): One-file Go CLI; timestamp-named SQL in `migrations/`, wraps Postgres/MySQL/SQLite/ClickHouse/BigQuery/Spanner; all-or-nothing transactions, `dbmate new|up|wait|dump`, driven by `DATABASE_URL`—perfect for polyglot stacks. ([github.com][2])
- [migrate 16,811 ⭐ Apr 2025](https://github.com/golang-migrate/migrate): Go library + CLI streaming `.up/.down.sql` from local FS, S3, GCS, HTTP or Git; 30 + DB drivers, `force` version bumps, `drop` wipes, embeddable in Go services. ([github.com][3])
- [flyway 8,858 ⭐ Jun 2025](https://github.com/flyway/flyway): CLI/Java-API “migrations-only” engine; auto-executes `V*__` SQL files in order, journals state in a single schema-history table; repeatable scripts, dry-run diffs, Docker/K8s images, Gradle/Maven plugins—pipeline-friendly DB versioning. ([github.com][1])
- [goose 8,516 ⭐ Jun 2025](https://github.com/pressly/goose): Simple Go tool running sequential/timestamped SQL or Go-code migrations; supports Pg/My/Sqlite/…, with `status up down redo` commands and importable helper funcs. ([github.com][4])
- [sql-migrate 3,342 ⭐ Apr 2025](https://github.com/rubenv/sql-migrate): Lightweight Go CLI/lib; paired `-- +migrate Up/Down` sections inside each SQL file, embeds migrations into binaries, works with SQLite/Postgres/MySQL/Oracle/MSSQL. ([pkg.go.dev][5])
- [DbUp 2,461 ⭐ Apr 2025](https://github.com/DbUp/DbUp): .NET library executing embedded SQL resources on app start; keeps a journal table, supports preview mode and transactional/non-transactional runs for SQL Server, Postgres, MySQL. ([dbup.readthedocs.io][6])
- [sqitch 2,997 ⭐ May 2025](https://github.com/sqitchers/sqitch): Dependency-graph change-manager (Perl CLI); plan file instead of numbering, three scripts per change (deploy/verify/revert), cryptographic hashes; runs on Pg, My, SQLite, Oracle, Snowflake & more. ([sqitch.org][7])
- [reshape 1,770 ⭐ May 2025](https://github.com/fabianlindfors/reshape): Rust binary generating zero-downtime Postgres migrations; diff-based plan creates dual-write views/triggers, `reshape plan | migrate | abort` workflow for safe rollouts. ([github.com][10])
- [migrate 782 ⭐ Apr 2025](https://github.com/graphile/migrate): Opinionated Postgres roll-forward flow; edit `current.sql`, CLI watches and commits numbered migrations, integrates tightly with Git history, NPM install. ([github.com][8])
- [pgmigrate 649 ⭐ Jan 2025](https://github.com/yandex/pgmigrate): Python CLI for Postgres; transactional + online callbacks, versioned `.sql` patches, `rollback` support—battle-tested at Yandex. ([github.com][9])
- [fastmigrate 12 ⭐ Jun 2025](https://github.com/answerdotai/fastmigrate): Ultra-minimal Python CLI; simply executes sequential `.sql` (or shell) scripts to bump schema versions, records state in one table, and offers `up | down | current` commands—nothing but scripts. ([github.com][1], [answer.ai][2])

## Table scraping

- 2014, 6K: [table-to-spreadsheet](https://chrome.google.com/webstore/detail/table-to-spreadsheet/haidhlbpihfihbjcggmffnmhgiddjcoc?hl=en)
  - Works well. Adds newlines to content
- 2019, 490: [Download table as CSV](https://chrome.google.com/webstore/detail/download-table-as-csv/jgeonblahchgiadgojdjilffklaihalj?hl=en)
  - Works well. Asks for filename
- 2019, 80K: [Table capture](https://chrome.google.com/webstore/detail/table-capture/iebpjdmgckacbodjpijphcplhebcmeop?hl=en)
  - Free version does not support download as Excel
- 2019, 39K: [Copytables](https://chrome.google.com/webstore/detail/copytables/ekdpkppgmlalfkphpibadldikjimijon?hl=en)
  - No download. Only copy
- 2013, 1K: [table to csv](https://chrome.google.com/webstore/detail/table-to-csv/khobgoemenoleeedfbilehnpoelmkbko?hl=en)
  - No download. Only copy
- 2015, 1K: [Table to CSV/JSON](https://chrome.google.com/webstore/detail/table-to-csvjson/lcmljkenflafolafllblkbchomcnaefi?hl=en)
  - No download. Only copy

## Pipeline tools

See [Awesome Pipelines](https://github.com/pditommaso/awesome-pipeline)

- [Prefect](https://github.com/PrefectHQ/prefect) - 5,200★
- [Metaflow](https://github.com/Netflix/metaflow) - 3,600★
- [Kedro](https://github.com/quantumblacklabs/kedro) - 3,000★
- [DBT](https://www.getdbt.com/)
- [Dagster](https://github.com/dagster-io/dagster/) - 2,200★
- [Mistral](https://github.com/openstack/mistral) - 227★ YAML based
- [Jug](https://github.com/luispedro/jug) -
- Dask
- Luigi
- Airflow
- Joblib
