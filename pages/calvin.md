---
title: Calvin & Hobbes Quote Search
root: /calvin/
layout: standalone
build: { list: never, render: always }
robotsNoIndex: true
description: An interactive search tool for Calvin & Hobbes quotes.
tags: [calvin-and-hobbes, comic-strips, bill-watterson]
---
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover, interactive-widget=resizes-content">
<title>Calvin &amp; Hobbes</title>
<meta name="robots" content="noindex">
<meta name="description" content="Every Calvin & Hobbes strip as one continuous reel. Pinch to zoom, pan straight into the next strip.">
<meta name="theme-color" id="themeColor" content="#f3ecdb">
<link rel="canonical" href="https://www.s-anand.net/calvin/">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%23e06a17'/%3E%3Cpath d='M7 3l5 26M15 3l3 26M23 3l4 26' stroke='%231e1913' stroke-width='3'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://picayune.uclick.com">
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400..800&family=Literata:ital,opsz,wght@0,7..72,400..600;1,7..72,400&display=swap" rel="stylesheet">
<script>try { const t = localStorage.getItem("ch-theme"); if (t) document.documentElement.dataset.theme = t; } catch {}</script>
<style>
  :root {
    --bg: #f3ecdb; --card: #fffcf4; --stage: #e2d8c0; --ink: #1e1913; --ink-2: #6a5d4b; --line: #d9cdb2;
    --tiger: #e06a17; --tiger-ink: #a2470a; --amber: #d9a21b; --mark: #ffd98e;
    --tint: rgba(224, 106, 23, .12); --ring: rgba(224, 106, 23, .22); --hover: rgba(30, 25, 19, .06);
    --dot: rgba(30, 25, 19, .07); --glow: rgba(224, 106, 23, .14);
    --chip-soft: rgba(255, 252, 244, .82);
    --shadow: 0 18px 40px -28px rgba(70, 45, 10, .55); --strip-filter: none;
    --ui: "Bricolage Grotesque", "Avenir Next", "Segoe UI", sans-serif;
    --read: "Literata", Georgia, serif;
    color-scheme: light;
  }
  @media (prefers-color-scheme: dark) {
    :root:not([data-theme="light"]) {
      --bg: #14110d; --card: #1f1b15; --stage: #0a0806; --ink: #f0e7d5; --ink-2: #a8997f; --line: #362f24;
      --tiger: #f0843a; --tiger-ink: #ffae72; --amber: #e2b23a; --mark: rgba(240, 132, 58, .4);
      --tint: rgba(240, 132, 58, .15); --ring: rgba(240, 132, 58, .3); --hover: rgba(240, 231, 213, .07);
      --dot: rgba(240, 231, 213, .05); --glow: rgba(240, 132, 58, .1); --chip-soft: rgba(31, 27, 21, .82);
      --shadow: 0 18px 40px -24px rgba(0, 0, 0, .8); --strip-filter: brightness(.93);
      color-scheme: dark;
    }
  }
  :root[data-theme="dark"] {
    --bg: #14110d; --card: #1f1b15; --stage: #0a0806; --ink: #f0e7d5; --ink-2: #a8997f; --line: #362f24;
    --tiger: #f0843a; --tiger-ink: #ffae72; --amber: #e2b23a; --mark: rgba(240, 132, 58, .4);
    --tint: rgba(240, 132, 58, .15); --ring: rgba(240, 132, 58, .3); --hover: rgba(240, 231, 213, .07);
    --dot: rgba(240, 231, 213, .05); --glow: rgba(240, 132, 58, .1); --chip-soft: rgba(31, 27, 21, .82);
    --shadow: 0 18px 40px -24px rgba(0, 0, 0, .8); --strip-filter: brightness(.93);
    color-scheme: dark;
  }

  *, *::before, *::after { box-sizing: border-box; }
  html, body { margin: 0; height: 100%; }
  body {
    position: fixed; inset: 0; overflow: hidden; overscroll-behavior: none;
    font-family: var(--ui); color: var(--ink); background-color: var(--bg);
    /* Ben-Day newsprint dots plus a warm glow, so the page feels like the funnies section */
    background-image: radial-gradient(var(--dot) 1px, transparent 1.5px), radial-gradient(circle at 12% -10%, var(--glow), transparent 55%);
    background-size: 8px 8px, 100% 100%;
    -webkit-tap-highlight-color: transparent; -webkit-font-smoothing: antialiased;
  }
  /* Tiger stripes across the top edge */
  body::before {
    content: ""; position: fixed; inset: 0 0 auto; height: 5px; z-index: 6; transition: opacity .3s;
    background: repeating-linear-gradient(-62deg, var(--tiger) 0 15px, var(--ink) 15px 21px, var(--tiger) 21px 31px, var(--ink) 31px 34px);
  }
  body:has(.chrome-off)::before, body:has(.zoomed.no-bar)::before { opacity: 0; }
  button { font: inherit; }
  [hidden] { display: none !important; }
  :focus-visible { outline: 2.5px solid var(--tiger); outline-offset: 2px; }
  .ic { width: 20px; height: 20px; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; flex: none; }
  .vh { position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%); white-space: nowrap; }
  #safe { position: fixed; inset: 0; visibility: hidden; pointer-events: none; padding: env(safe-area-inset-top) env(safe-area-inset-right) env(safe-area-inset-bottom) env(safe-area-inset-left); }
  @keyframes appear { from { opacity: 0; } }

  /* ---------- the canvas: full viewport, everything else floats above it ---------- */
  .stage { position: fixed; inset: 0; z-index: 0; overflow: hidden; touch-action: none; user-select: none; -webkit-user-select: none; cursor: grab; transition: background-color .35s; }
  .zoomed .stage, .chrome-off .stage { background-color: var(--stage); }

  #reel { position: absolute; inset: 0; }
  #reel.fade { animation: appear .3s ease-out; }
  #reel img {
    position: absolute; left: 0; top: 0; height: auto; max-width: none; background: #fff; border-radius: 2px;
    filter: var(--strip-filter); -webkit-user-drag: none; opacity: 0; transition: opacity .3s;
    box-shadow: 0 1px 2px rgba(0, 0, 0, .12), 0 16px 36px -16px rgba(40, 25, 5, .6);
    color: #6a5d4b; font: italic .9rem var(--read);
  }
  #reel img.ok { opacity: 1; }
  /* Date "spine" in the gap between strips, so it's obvious where one ends and the next begins */
  #reel .gaplabel {
    position: absolute; left: 0; top: 0; transform-origin: 0 0; white-space: nowrap; pointer-events: none;
    font: 650 11px/1 var(--ui); letter-spacing: .14em; text-transform: uppercase; color: var(--ink-2); opacity: .8;
  }
  #reel .gaplabel.sun { color: var(--tiger-ink); }
  .app:not(.zoomed) #reel img.ok:not(.cur) { opacity: .38; }
  .spinner {
    position: absolute; left: var(--cx, 50%); top: var(--cy, 50%); width: 30px; height: 30px; margin: -15px; border-radius: 50%;
    border: 3px solid var(--line); border-top-color: var(--tiger); opacity: 0; pointer-events: none;
  }
  .loading .spinner { animation: spin .8s linear infinite, show .2s .25s both; }
  @keyframes spin { to { rotate: 360deg; } }
  @keyframes show { from { opacity: 0; } to { opacity: 1; } }
  .side {
    position: absolute; top: var(--cy, 50%); translate: 0 -50%; width: 2.8rem; height: 2.8rem; border-radius: 50%;
    border: 1px solid var(--line); background: var(--chip-soft); color: var(--ink); cursor: pointer;
    display: none; place-items: center; opacity: 0; transition: opacity .2s; backdrop-filter: blur(6px);
  }
  /* Arrows sit just outside the strip area when there's room, otherwise just inside it */
  .side.prev { left: max(.6rem, calc(var(--rx, 0px) - 3.6rem)); }
  .side.next { left: min(calc(100vw - 3.4rem), calc(var(--rx, 0px) + var(--rw, 100vw) + .8rem)); }
  @media (hover: hover) and (pointer: fine) {
    .side { display: grid; }
    .stage:hover .side:not(:disabled) { opacity: .92; }
  }
  .zoomed .side { display: none; }

  /* ---------- floating header ---------- */
  .bar {
    position: fixed; z-index: 4; top: 0; left: 0; right: 0; display: flex; align-items: center; gap: .4rem;
    padding: calc(env(safe-area-inset-top) + 10px) max(.6rem, env(safe-area-inset-right)) .5rem max(.6rem, env(safe-area-inset-left));
    background: color-mix(in srgb, var(--bg) 88%, transparent); backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px);
    transition: transform .3s cubic-bezier(.2, .8, .2, 1), opacity .3s; animation: appear .5s backwards;
  }
  .no-bar .bar { transform: translateY(-110%); opacity: 0; pointer-events: none; }
  .brand {
    flex: none; width: 2.5rem; height: 2.5rem; border-radius: 13px; display: grid; place-items: center;
    background: var(--ink); color: var(--bg); font: 800 .78rem/1 var(--ui); letter-spacing: -.03em;
    rotate: -5deg; box-shadow: 2px 3px 0 var(--tiger); user-select: none;
  }
  .title { display: none; margin: 0 .5rem 0 .3rem; font: 800 1.2rem/1 var(--ui); letter-spacing: -.035em; white-space: nowrap; }
  .title i { font: italic 400 1.25rem/1 var(--read); color: var(--tiger); }
  @media (min-width: 760px) { .title { display: block; } }
  .search {
    flex: 1; min-width: 0; display: flex; align-items: center; gap: .45rem; height: 2.7rem; padding: 0 .25rem 0 .85rem;
    background: var(--card); border: 1.5px solid var(--line); border-radius: 999px; cursor: text; transition: border-color .15s, box-shadow .15s;
  }
  .search > .ic { color: var(--ink-2); }
  .search:focus-within { border-color: var(--tiger); box-shadow: 0 0 0 4px var(--ring); }
  .search input { flex: 1; min-width: 0; height: 100%; border: 0; outline: 0; padding: 0; background: transparent; color: var(--ink); font: 500 16px/1 var(--ui); }
  .search input::placeholder { color: var(--ink-2); opacity: .85; }
  .search input::-webkit-search-cancel-button { -webkit-appearance: none; }
  .L-land .brand { display: none; }
  .L-land .bar { padding-top: calc(env(safe-area-inset-top) + 6px); padding-bottom: .35rem; }
  .L-land .search { height: 2.4rem; }
  .iconbtn {
    flex: none; appearance: none; border: 0; margin: 0; padding: 0; background: transparent; color: var(--ink);
    width: 2.6rem; height: 2.6rem; border-radius: 12px; display: grid; place-items: center; cursor: pointer;
    transition: background .15s, transform .1s, opacity .15s;
  }
  .iconbtn.sm { width: 2.15rem; height: 2.15rem; border-radius: 10px; }
  .iconbtn.sm .ic { width: 18px; height: 18px; }
  .iconbtn:hover { background: var(--hover); }
  .iconbtn:active { transform: scale(.9); }
  .iconbtn:disabled { opacity: .28; cursor: default; background: transparent; transform: none; }
  .clear { display: none !important; }
  .searching .clear { display: grid !important; background: var(--tint); color: var(--tiger-ink); border-radius: 50%; }

  /* ---------- floating sheet: docked under the strip, a thin bar, an overlay, a drawer or a column ---------- */
  .sheet {
    position: fixed; z-index: 4; left: max(.5rem, env(safe-area-inset-left)); right: max(.5rem, env(safe-area-inset-right));
    bottom: calc(env(safe-area-inset-bottom) + .5rem); max-height: 62dvh;
    display: flex; flex-direction: column; background: var(--card); border: 1px solid var(--line); border-radius: 18px;
    box-shadow: var(--shadow); overflow: hidden; touch-action: pan-y;
    transition: top .3s cubic-bezier(.2, .8, .2, 1), transform .3s cubic-bezier(.2, .8, .2, 1), opacity .3s;
    animation: appear .5s .1s backwards;
  }
  .S-dock .sheet { top: var(--sheet-top, 45vh); max-height: none; }
  .S-bar .body { display: none; }
  .S-over .sheet { box-shadow: 0 -12px 40px -12px rgba(0, 0, 0, .4); }
  .S-hidden .sheet { transform: translateY(calc(100% + 1.5rem)); opacity: 0; pointer-events: none; }
  .S-drawer .sheet { top: .5rem; left: auto; width: min(27rem, 58vw); max-height: none; box-shadow: -12px 0 40px -12px rgba(0, 0, 0, .4); }
  /* Desktop: a fixed-height caption panel under a centered column, so the text never jumps between dailies and Sundays */
  .S-desk .sheet { top: auto; bottom: .75rem; height: var(--desk-h, 200px); max-height: none; left: var(--desk-l, .75rem); right: var(--desk-l, .75rem); }
  .S-desk .text { padding: .9rem 3rem 1.1rem; }
  .S-desk .quote { margin: 0 auto; }
  .L-wide.S-drawer .sheet { top: calc(var(--bar-h, 64px) + 4px); bottom: .75rem; right: .75rem; }
  .grab { display: none; flex: none; position: relative; width: 100%; height: 18px; border: 0; padding: 0; background: none; cursor: pointer; }
  /* The bar takes vertical swipes itself (swipe up to open, down to close) */
  .S-bar .grab, .S-bar .head, .S-over .grab, .S-over .head { touch-action: none; }
  .S-bar .head, .S-over .head { cursor: pointer; }
  .grab::before { content: ""; position: absolute; left: 50%; top: 7px; width: 38px; height: 4px; margin-left: -19px; border-radius: 2px; background: var(--line); }
  .S-bar .grab, .S-over .grab { display: block; }

  .head { position: relative; display: flex; flex-wrap: wrap; align-items: center; gap: .1rem; padding: .3rem; border-bottom: 1px dashed var(--line); flex: none; }
  .L-land .head, .L-wide .head { flex-wrap: nowrap; }
  .L-wide .head .iconbtn.sm { width: 2rem; }
  .L-wide .zchip { margin: 0 .1rem; }
  .S-bar .head, .S-over .head { padding-top: 0; }
  .S-bar .head { border-bottom: 0; }
  .when { display: flex; align-items: baseline; gap: .4rem; border: 0; background: none; color: var(--ink); padding: .45rem .5rem; border-radius: 10px; cursor: pointer; white-space: nowrap; }
  .when:hover { background: var(--hover); }
  .when b { font: 760 1.06rem/1 var(--ui); letter-spacing: -.02em; }
  .when span { font: 650 .7rem/1 var(--ui); text-transform: uppercase; letter-spacing: .09em; color: var(--ink-2); }
  .when span.sun { color: var(--tiger-ink); }
  .L-port:not(.S-dock) .when span, .searching .when span, .L-wide.zoomed .when span { display: none; }
  .L-port:not(.S-dock) .when b { font-size: .98rem; }
  @media (max-width: 400px) { .when span { display: none; } }
  .datepick { position: absolute; left: .5rem; bottom: 0; width: 1px; height: 1px; opacity: 0; pointer-events: none; border: 0; padding: 0; }
  .searchbtn { display: none !important; }
  .no-bar .searchbtn { display: grid !important; }
  .L-port:not(.S-dock) .navbtn { display: none; }
  .pager { display: flex; align-items: center; }
  .count {
    display: flex; align-items: center; gap: .3rem; border: 0; background: none; color: var(--ink-2);
    font: 650 .8rem/1 var(--ui); font-variant-numeric: tabular-nums; padding: .5rem .3rem; border-radius: 9px; white-space: nowrap; cursor: default;
  }
  .count .of { opacity: .62; font-weight: 500; margin-left: -.25rem; }
  .count .ic { width: 15px; height: 15px; }
  .searching .count { background: var(--tint); color: var(--tiger-ink); cursor: pointer; padding: .45rem .55rem; margin: 0 .15rem; }
  .zchip {
    display: none; align-items: center; gap: .3rem; height: 2rem; padding: 0 .45rem 0 .65rem; margin: 0 .2rem; border: 0; border-radius: 999px;
    background: var(--ink); color: var(--bg); font: 650 .78rem/1 var(--ui); font-variant-numeric: tabular-nums; cursor: pointer; white-space: nowrap;
  }
  .zchip .ic { width: 13px; height: 13px; }
  .zoomed .zchip { display: flex; }
  .cancel2 { display: none; }
  .searching .cancel2 { display: grid; }
  .spacer { flex: 1; }
  .peek {
    display: none; order: 20; flex: 1 1 100%; min-width: 0; margin: 0; padding: 0 .55rem .45rem;
    font: italic 400 .95rem/1.3 var(--read); color: var(--ink-2); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; cursor: pointer;
  }
  .S-bar .peek { display: block; }
  .L-land .peek, .L-wide .peek { order: 0; flex: 1 1 0; padding: 0 .5rem; }
  .L-land.S-bar .spacer { display: none; }
  .body { flex: 1 1 auto; min-height: 0; overflow-y: auto; overscroll-behavior: contain; position: relative; touch-action: pan-y; }
  .text { padding: .85rem 2.9rem 1.15rem 1.1rem; }
  .copytext { position: absolute; top: .45rem; right: .4rem; color: var(--ink-2); }
  .quote { margin: 0; max-width: 64ch; font: 400 1.08rem/1.62 var(--read); text-wrap: pretty; hyphens: auto; }
  .quote.dim { color: var(--ink-2); font-style: italic; }
  mark { background: var(--mark); color: inherit; padding: 0 .12em; border-radius: 3px; -webkit-box-decoration-break: clone; box-decoration-break: clone; }
  .results { padding: .3rem .35rem .6rem; }
  .rmeta { margin: .45rem .65rem .35rem; font: 650 .7rem/1.3 var(--ui); letter-spacing: .07em; text-transform: uppercase; color: var(--ink-2); }
  #results { list-style: none; margin: 0; padding: 0; }
  #results button { display: grid; grid-template-columns: 6.3rem 1fr; gap: .55rem; align-items: baseline; width: 100%; text-align: left; border: 0; background: none; color: var(--ink); padding: .6rem .6rem; border-radius: 12px; cursor: pointer; }
  #results button:hover { background: var(--hover); }
  #results [aria-selected="true"] button { background: var(--tint); box-shadow: inset 3px 0 0 var(--tiger); }
  .rdate { display: flex; align-items: center; gap: .45rem; font: 650 .78rem/1.35 var(--ui); color: var(--ink-2); font-variant-numeric: tabular-nums; white-space: nowrap; }
  .dot { width: 7px; height: 7px; border-radius: 50%; background: var(--ink-2); opacity: .45; flex: none; }
  .dot.ta { background: var(--tiger); opacity: 1; }
  .dot.tb { background: var(--amber); opacity: 1; }
  .rsnip { font: 400 .96rem/1.45 var(--read); display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }

  .toast {
    position: fixed; left: 50%; top: calc(env(safe-area-inset-top) + 4.5rem); z-index: 10; translate: -50% -8px; opacity: 0;
    padding: .6rem 1.05rem; border-radius: 999px; background: var(--ink); color: var(--bg); font: 650 .86rem/1 var(--ui);
    box-shadow: 0 12px 30px -12px rgba(0, 0, 0, .55); pointer-events: none; transition: opacity .2s, translate .2s; white-space: nowrap;
  }
  .toast.show { opacity: 1; translate: -50% 0; }
  @media (prefers-reduced-motion: reduce) {
    *, *::before, *::after { animation-duration: .01ms !important; transition-duration: .01ms !important; }
  }
</style>
</head>
<body data-pagefind-ignore="all">
<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <symbol id="i-search" viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.6-3.6"/></symbol>
  <symbol id="i-x" viewBox="0 0 24 24"><path d="M18 6 6 18M6 6l12 12"/></symbol>
  <symbol id="i-left" viewBox="0 0 24 24"><path d="m15 18-6-6 6-6"/></symbol>
  <symbol id="i-right" viewBox="0 0 24 24"><path d="m9 18 6-6-6-6"/></symbol>
  <symbol id="i-list" viewBox="0 0 24 24"><path d="M9 6h11M9 12h11M9 18h11M4.5 6h.01M4.5 12h.01M4.5 18h.01"/></symbol>
  <symbol id="i-copy" viewBox="0 0 24 24"><rect x="9" y="9" width="12" height="12" rx="2"/><path d="M5 15H4.5A1.5 1.5 0 0 1 3 13.5v-9A1.5 1.5 0 0 1 4.5 3h9A1.5 1.5 0 0 1 15 4.5V5"/></symbol>
  <symbol id="i-link" viewBox="0 0 24 24"><path d="M10 13a5 5 0 0 0 7.5.5l3-3a5 5 0 0 0-7-7l-1.7 1.7"/><path d="M14 11a5 5 0 0 0-7.5-.5l-3 3a5 5 0 0 0 7 7l1.7-1.7"/></symbol>
  <symbol id="i-image" viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="9" cy="9" r="2"/><path d="m21 15-3.1-3.1a2 2 0 0 0-2.8 0L6 21"/></symbol>
  <symbol id="i-shuffle" viewBox="0 0 24 24"><path d="M2 18h1.4c1.3 0 2.5-.6 3.3-1.7l6.1-8.6c.7-1.1 2-1.7 3.3-1.7H22"/><path d="m18 2 4 4-4 4"/><path d="M2 6h1.9c1.5 0 2.9.9 3.6 2.2"/><path d="M22 18h-5.9c-1.3 0-2.6-.7-3.3-1.8l-.5-.8"/><path d="m18 14 4 4-4 4"/></symbol>
  <symbol id="i-theme" viewBox="0 0 24 24"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17z" fill="currentColor"/></symbol>
</svg>

<div class="app L-port S-dock" id="app">
  <main class="stage loading" id="stage" aria-label="Comic strips. Pinch or double-tap to zoom, then pan straight into the next strip. Tap for full screen.">
    <div id="reel"></div>
    <div class="spinner" aria-hidden="true"></div>
    <button class="side prev" id="sidePrev" type="button" aria-label="Previous strip" title="Previous (←)"><svg class="ic"><use href="#i-left"/></svg></button>
    <button class="side next" id="sideNext" type="button" aria-label="Next strip" title="Next (→)"><svg class="ic"><use href="#i-right"/></svg></button>
  </main>

  <header class="bar" id="bar">
    <div class="brand" aria-hidden="true">C&amp;H</div>
    <h1 class="title">Calvin <i>&amp;</i> Hobbes</h1>
    <div class="search" id="searchBox">
      <svg class="ic"><use href="#i-search"/></svg>
      <input id="q" type="search" placeholder="Search the strips" autocomplete="off" autocapitalize="off" autocorrect="off" spellcheck="false" enterkeyhint="search" aria-label="Search strip text" aria-controls="results">
      <button class="iconbtn sm clear" id="clear" type="button" aria-label="Cancel search" title="Cancel search (Esc)"><svg class="ic"><use href="#i-x"/></svg></button>
    </div>
    <button class="iconbtn" id="random" type="button" aria-label="Random strip" title="Random strip (R)"><svg class="ic"><use href="#i-shuffle"/></svg></button>
    <button class="iconbtn" id="theme" type="button" aria-label="Toggle dark mode" title="Toggle dark mode"><svg class="ic"><use href="#i-theme"/></svg></button>
  </header>

  <section class="sheet" id="sheet" aria-label="Strip details">
    <button class="grab" id="grab" type="button" aria-label="Show or hide the text" aria-expanded="false"></button>
    <div class="head" id="head">
      <button class="iconbtn sm searchbtn" id="searchBtn" type="button" aria-label="Search" title="Search (/)"><svg class="ic"><use href="#i-search"/></svg></button>
      <button class="when" id="when" type="button" title="Jump to a date"><span id="whenDay"></span><b id="whenDate">Loading…</b></button>
      <input type="date" id="datePick" class="datepick" tabindex="-1" aria-hidden="true">
      <p class="peek" id="peek"></p>
      <div class="pager">
        <button class="iconbtn sm navbtn" id="prev" type="button" aria-label="Previous strip" title="Previous (←)" disabled><svg class="ic"><use href="#i-left"/></svg></button>
        <button class="count" id="count" type="button" title="Show search results"></button>
        <button class="iconbtn sm navbtn" id="next" type="button" aria-label="Next strip" title="Next (→)" disabled><svg class="ic"><use href="#i-right"/></svg></button>
      </div>
      <button class="zchip" id="zoomChip" type="button" title="Back to fit (0)"><span id="zoomLevel">1×</span><svg class="ic"><use href="#i-x"/></svg></button>
      <button class="iconbtn sm cancel2" id="cancel2" type="button" aria-label="Cancel search" title="Cancel search (Esc)"><svg class="ic"><use href="#i-x"/></svg></button>
      <span class="spacer"></span>
      <button class="iconbtn sm" id="copyImg" type="button" aria-label="Copy image" title="Copy image"><svg class="ic"><use href="#i-image"/></svg></button>
      <button class="iconbtn sm" id="copyLink" type="button" aria-label="Copy image link" title="Copy image link"><svg class="ic"><use href="#i-link"/></svg></button>
    </div>
    <div class="body" id="body">
      <div class="results" id="resultsWrap" hidden>
        <p class="rmeta" id="rmeta"></p>
        <ol id="results" role="listbox" aria-label="Search results"></ol>
      </div>
      <article class="text" id="text">
        <button class="iconbtn sm copytext" id="copyText" type="button" aria-label="Copy text" title="Copy text"><svg class="ic"><use href="#i-copy"/></svg></button>
        <p class="quote dim" id="quote">Loading the strips…</p>
      </article>
    </div>
  </section>
</div>
<div id="safe"></div>
<div class="toast" id="toast" role="status" aria-live="polite"></div>
<p class="vh" id="live" aria-live="polite"></p>

<script>
(() => {
  const DATA_URL = "https://files.s-anand.net/images/calvin.tsv";
  const IMG = (id) => `https://picayune.uclick.com/comics/ch/${id.slice(0, 4)}/ch${id.slice(2)}.gif`;
  // picayune.uclick.com sends no CORS headers, so the canvas would be tainted. AI Pipe's proxy adds them for "Copy image".
  const PROXY = "https://aipipe.org/proxy/";
  const LIST_LIMIT = 150;

  // ================= Search =================
  // Ranking, best first:
  //   60 exact phrase · 50 phrase (last word still being typed) · 40 phrase inside a word
  //   30 all words, in order · 20 all words, any order
  //   15 / 12 the same, but some word only matches with a typo · 5 all but one word (3+ word queries)
  // Ties: better word matches (exact > prefix > infix > typo), tighter span, more hits, then date.
  const norm = (s) => s.toLowerCase().replace(/['’`]/g, "").replace(/[^a-z0-9]+/g, " ").trim();
  const vocab = new Map();
  const words = [];
  const tokId = (w) => {
    let k = vocab.get(w);
    if (k === undefined) { k = words.length; vocab.set(w, k); words.push(w); }
    return k;
  };

  // Optimal-string-alignment distance <= max (handles a swapped pair of letters as one typo)
  function near(a, b, max) {
    const la = a.length, lb = b.length;
    if (Math.abs(la - lb) > max) return false;
    let p2 = null, p1 = Array.from({ length: lb + 1 }, (_, j) => j);
    for (let i = 1; i <= la; i++) {
      const row = [i];
      let lo = i;
      for (let j = 1; j <= lb; j++) {
        let v = Math.min(p1[j] + 1, row[j - 1] + 1, p1[j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1));
        if (i > 1 && j > 1 && a[i - 1] === b[j - 2] && a[i - 2] === b[j - 1]) v = Math.min(v, p2[j - 2] + 1);
        row[j] = v;
        if (v < lo) lo = v;
      }
      if (lo > max) return false;
      p2 = p1; p1 = row;
    }
    return p1[lb] <= max;
  }

  // For one query word: how well does each vocabulary word match? 4 exact, 3 prefix, 2 infix, 1 typo, 0 none
  const qcache = new Map();
  function qualities(w) {
    if (qcache.has(w)) return qcache.get(w);
    const out = new Uint8Array(words.length);
    const typos = w.length >= 7 ? 2 : 1;
    for (let k = 0; k < words.length; k++) {
      const v = words[k];
      if (v === w) out[k] = 4;
      else if (v.startsWith(w)) out[k] = 3;
      else if (w.length >= 4 && v.includes(w)) out[k] = 2;
      else if (w.length >= 4 && near(w, v, typos)) out[k] = 1;
    }
    if (qcache.size > 300) qcache.clear();
    qcache.set(w, out);
    return out;
  }

  // Smallest window holding the query words in order (each at quality >= minq), or -1
  function orderSpan(t, Q, n, minq) {
    let best = -1;
    for (let s = 0; s < t.length; s++) {
      if (Q[0][t[s]] < minq) continue;
      let j = 1, p = s + 1;
      for (; p < t.length && j < n; p++) if (Q[j][t[p]] >= minq) j++;
      if (j < n) break; // no completion from here means none from any later start
      const span = p - 1 - s;
      if (best < 0 || span < best) best = span;
      if (span === n - 1) break;
    }
    return best;
  }

  function search(text) {
    const qn = norm(text);
    if (qn.length < 2) return null;
    const qw = qn.split(" ");
    const n = qw.length;
    const Q = qw.map(qualities);
    const best = new Uint8Array(n);
    const list = [];
    for (let i = 0; i < strips.length; i++) {
      const { t, n: hay } = strips[i];
      let tier = 0;
      if (hay.includes(` ${qn} `)) tier = 60;
      else if (hay.includes(` ${qn}`)) tier = 50;
      else if (qn.length >= 4 && hay.includes(qn)) tier = 40;
      best.fill(0);
      let hits = 0;
      for (let p = 0; p < t.length; p++) {
        let hit = 0;
        for (let j = 0; j < n; j++) {
          const v = Q[j][t[p]];
          if (v > best[j]) best[j] = v;
          if (v >= 2) hit = 1;
        }
        hits += hit;
      }
      let qual = 0, matched = 0, strong = 0;
      for (let j = 0; j < n; j++) {
        qual += best[j];
        if (best[j]) matched++;
        if (best[j] >= 2) strong++;
      }
      let span = 0;
      if (!tier) {
        if (matched === n) {
          const typo = strong < n;
          span = n === 1 ? 0 : orderSpan(t, Q, n, typo ? 1 : 2);
          tier = typo ? (span >= 0 ? 15 : 12) : (span >= 0 ? 30 : 20);
          if (span < 0) span = 999;
        } else if (n >= 3 && matched >= n - 1) { tier = 5; span = 999; }
        else continue;
      }
      list.push({ i, tier, qual, span, hits });
    }
    list.sort((a, b) => b.tier - a.tier || b.qual - a.qual || a.span - b.span || b.hits - a.hits || a.i - b.i);
    return { qn, Q, list };
  }

  const TIERS = { 60: "Exact phrase", 50: "Phrase", 40: "Phrase, inside a word", 30: "All words, in order", 20: "All words", 15: "All words (close spelling), in order", 12: "All words (close spelling)", 5: "Most words" };
  const tierDot = (t) => (t >= 40 ? "ta" : t >= 20 ? "tb" : "");
  const esc = (s) => s.replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]);
  const WORD = /[A-Za-z0-9'’`]+/g;

  // Highlight words in the original text that match any query word
  function isHit(word, hl) {
    const k = vocab.get(norm(word));
    return k !== undefined && hl.Q.some((a) => a[k] >= hl.minq);
  }
  function marked(text, hl) {
    if (!hl) return esc(text);
    let html = "", last = 0;
    for (const m of text.matchAll(WORD)) {
      if (!isHit(m[0], hl)) continue;
      html += esc(text.slice(last, m.index)) + "<mark>" + esc(m[0]) + "</mark>";
      last = m.index + m[0].length;
    }
    return html + esc(text.slice(last));
  }
  function snippet(text, hl) {
    let first = 0;
    for (const m of text.matchAll(WORD)) if (isHit(m[0], hl)) { first = m.index; break; }
    if (first < 45) return marked(text.slice(0, 220), hl);
    const from = text.lastIndexOf(" ", first - 35) + 1;
    return "…" + marked(text.slice(from, from + 220), hl);
  }

  // ================= State =================
  const $ = (id) => document.getElementById(id);
  const app = $("app"), stage = $("stage"), reelEl = $("reel"), bar = $("bar"), sheet = $("sheet");
  const q = $("q"), countBtn = $("count"), prevBtn = $("prev"), nextBtn = $("next");
  const resultsWrap = $("resultsWrap"), resultsEl = $("results"), textEl = $("text"), quoteEl = $("quote");
  const fmt = new Intl.NumberFormat("en");
  const MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split(" ");
  const DAYS = "Sun Mon Tue Wed Thu Fri Sat".split(" ");

  let strips = [];       // [{id: "19851118", q: "text", n: " normalized text ", t: Int32Array of word ids}], sorted by date
  let mode = "timeline"; // "timeline" walks every strip; "search" walks the ranked results
  let pos = 0, cur = -1; // position in the current sequence, and the strip index it points to
  let query = "", S = null, results = [];
  // Chrome state
  let layoutMode = "port", zoomed = false, listOpen = false, sheetOpen = false, chromeOff = false, barOn = false;

  const inSearch = () => mode === "search";
  const seqLen = () => (inSearch() ? results.length : strips.length);
  const seqAt = (p) => (inSearch() ? results[p].i : p);
  const hasMove = (d) => pos + d >= 0 && pos + d < seqLen();
  const hlFor = (r) => (S && r ? { Q: S.Q, minq: r.tier >= 20 ? 2 : 1 } : null);
  const dateParts = (id) => {
    const d = new Date(Date.UTC(+id.slice(0, 4), +id.slice(4, 6) - 1, +id.slice(6)));
    return { day: DAYS[d.getUTCDay()], sunday: d.getUTCDay() === 0, date: `${+id.slice(6)} ${MONTHS[d.getUTCMonth()]} ${id.slice(0, 4)}` };
  };
  const isoDate = (id) => `${id.slice(0, 4)}-${id.slice(4, 6)}-${id.slice(6)}`;

  // ================= Layout: which chrome shows, and the region the strip may use =================
  // Layouts: "port" (phone upright), "land" (phone sideways), "wide" (desktop / tablet).
  // Sheet states: dock (under the strip), bar (one thin row), over (bar opened up), drawer (landscape results), col (desktop column), hidden.
  const SHEET_MIN = 150;
  const barH = {};
  let regionCache = {}, safeCache = null;
  function safe() {
    if (!safeCache) {
      const cs = getComputedStyle($("safe"));
      safeCache = { t: parseFloat(cs.paddingTop) || 0, r: parseFloat(cs.paddingRight) || 0, b: parseFloat(cs.paddingBottom) || 0, l: parseFloat(cs.paddingLeft) || 0 };
    }
    return safeCache;
  }
  function computeLayoutMode() {
    const vw = innerWidth, vh = innerHeight;
    // Any mouse-driven window of reasonable size gets the desktop layout, not just big screens
    const mouse = matchMedia("(hover: hover) and (pointer: fine)").matches;
    layoutMode = (vw >= 1000 && vh > 520) || (mouse && vw >= 700 && vh >= 480) ? "wide" : vw > vh && vh <= 520 ? "land" : "port";
  }
  // Desktop column: the strip and its caption share one centered column
  const deskCol = () => Math.min(innerWidth - 48, 1080);
  function applyChrome() {
    if (listOpen || barOn) chromeOff = false;
    const L = layoutMode;
    let s;
    if (L === "wide") {
      s = listOpen ? "drawer" : "desk";
      app.style.setProperty("--desk-l", `${Math.round((innerWidth - deskCol()) / 2)}px`);
      app.style.setProperty("--desk-h", `${Math.round(Math.min(240, Math.max(150, innerHeight * 0.24)))}px`);
    }
    else if (chromeOff) s = "hidden";
    else if (L === "land" && listOpen) s = "drawer";
    else if (L === "port" && !zoomed) s = "dock";
    else s = sheetOpen || listOpen ? "over" : "bar";
    const showBar = L === "wide" || (!chromeOff && (barOn || (L === "port" && !zoomed)));
    app.className = ["app", `L-${L}`, `S-${s}`, inSearch() && "searching", zoomed && "zoomed", listOpen && "listing", !showBar && "no-bar", chromeOff && "chrome-off"].filter(Boolean).join(" ");
    app.style.setProperty("--bar-h", `${bar.offsetHeight}px`);
    if (s === "bar") barH[L] = sheet.offsetHeight + safe().b + 8;
    $("grab").setAttribute("aria-expanded", String(s === "over"));
    regionCache = {};
  }
  // The rectangle the strip is fitted into (z = false) or may be panned across when zoomed (z = true)
  function region(z = zoomed) {
    const key = z ? "z" : "f";
    if (regionCache[key]) return regionCache[key];
    const vw = innerWidth, vh = innerHeight, sf = safe();
    let r;
    if (layoutMode === "wide") {
      const top = bar.offsetHeight + 12;
      if (listOpen) { // results drawer on the right: the strip uses the space to its left
        r = { x: 24, y: top, w: vw - sheet.offsetWidth - 12 - 24 - 24, h: vh - top - 16 };
      } else {        // centered column above the fixed caption panel
        const col = deskCol();
        r = { x: (vw - col) / 2, y: top, w: col, h: vh - sheet.offsetHeight - 12 - 16 - top };
      }
    } else {
      const portFit = layoutMode === "port" && !z && !chromeOff;
      // When the search bar is showing, the strip area starts below it (pulling it down "scrolls" the comic down)
      const top = !chromeOff && (barOn || portFit) ? bar.offsetHeight + 4 : sf.t + 8;
      // An opened bottom panel ends the strip area at its top edge, so it never hides the comic
      const over = /\bS-over\b/.test(app.className);
      const bottom = chromeOff ? vh - sf.b - 8
        : portFit ? vh - sf.b - SHEET_MIN
        : over ? vh - sheet.offsetHeight - sf.b - 8 - 6
        : vh - (barH[layoutMode] || (layoutMode === "port" ? 104 : 58)) - 6;
      r = { x: sf.l + 8, y: top, w: vw - sf.l - sf.r - 16, h: Math.max(80, bottom - top) };
    }
    return (regionCache[key] = r);
  }
  function setZoomed(v) {
    if (zoomed === v) return;
    zoomed = v;
    if (!v) sheetOpen = false;
    if (v && !inSearch() && document.activeElement !== q) barOn = false; // zooming in starts uncluttered
    applyChrome();
    if (v && layoutMode !== "wide") {
      try { if (!localStorage.getItem("ch-hint-pull")) { localStorage.setItem("ch-hint-pull", "1"); toast("Pull down for search · tap the bar for text", 3500); } } catch {}
    }
  }

  // ================= The reel: strips side by side, sharing one scale =================
  // Every strip is laid out in "natural" pixels (GIFs are 600 wide; dailies ~193 tall, Sundays ~420),
  // centered on one horizontal line. The view is a scale k plus an offset (tx, ty): screen = t + X * k.
  const GAP = 80, EST_DAILY = [600, 193], EST_SUNDAY = [600, 421];
  const dims = new Map();  // strip id -> [w, h] once seen
  const cells = new Map(); // sequence position -> {p, i, img, nw, nh, X, ok}
  let anchor = 0, k = 1, tx = 0, ty = 0;

  function makeCell(p) {
    const i = seqAt(p), id = strips[i].id;
    const [nw, nh] = dims.get(id) || (dateParts(id).sunday ? EST_SUNDAY : EST_DAILY);
    const img = document.createElement("img");
    img.draggable = false;
    img.alt = "";
    const d = dateParts(id);
    const label = Object.assign(document.createElement("div"), { className: `gaplabel${d.sunday ? " sun" : ""}`, textContent: `${d.day} ${d.date}` });
    label.setAttribute("aria-hidden", "true");
    const c = { p, i, img, label, nw, nh, X: 0, ok: false };
    img.onload = () => {
      if (cells.get(c.p) !== c) return;
      c.ok = true;
      img.classList.add("ok");
      if (img.naturalWidth !== c.nw || img.naturalHeight !== c.nh) {
        c.nw = img.naturalWidth; c.nh = img.naturalHeight;
        dims.set(id, [c.nw, c.nh]);
        relayout();
        if (c.p === pos && !zoomed && !g) refit();
      }
      if (c.p === pos) stage.classList.remove("loading");
      requestRender();
    };
    img.onerror = () => {
      if (cells.get(c.p) !== c) return;
      c.ok = true;
      img.classList.add("ok");
      img.alt = "This strip didn't load";
      if (c.p === pos) stage.classList.remove("loading");
    };
    img.src = IMG(id);
    reelEl.append(label, img);
    cells.set(p, c);
  }

  // Positions chain outwards from the anchor strip, which always sits at X = 0
  function relayout() {
    const a = cells.get(anchor);
    if (!a) return;
    a.X = 0;
    for (let p = anchor + 1; cells.has(p); p++) { const b = cells.get(p - 1); cells.get(p).X = b.X + b.nw + GAP; }
    for (let p = anchor - 1; cells.has(p); p--) { const c = cells.get(p); c.X = cells.get(p + 1).X - GAP - c.nw; }
  }
  function ensureWindow() {
    const lo = Math.max(0, pos - 3), hi = Math.min(seqLen() - 1, pos + 3);
    for (const [p, c] of cells) if (p < lo || p > hi) { c.img.remove(); c.label.remove(); cells.delete(p); }
    for (let p = lo; p <= hi; p++) if (!cells.has(p)) makeCell(p);
    relayout();
  }
  // Move the anchor to p without moving anything on screen (and keep in-flight gestures/animations consistent)
  function reanchor(p) {
    const c = cells.get(p);
    if (!c || p === anchor) return;
    const A = c.X;
    anchor = p;
    relayout();
    tx += A * k;
    if (g?.type === "pan") g.x0 += A * k;
    if (g?.type === "pinch") g.x0 += A * g.k0;
    if (anim?.type === "tween") { anim.from.tx += A * anim.from.k; anim.to.tx += A * anim.to.k; }
  }

  function setPos(p) {
    if (p === pos) return;
    reanchor(p);
    pos = p;
    cur = seqAt(p);
    ensureWindow();
    afterPos();
  }
  function afterPos() {
    for (const c of cells.values()) {
      const on = c.p === pos;
      c.img.classList.toggle("cur", on);
      if (!c.img.alt.startsWith("This strip")) c.img.alt = on ? strips[c.i].q : "";
    }
    stage.classList.toggle("loading", !cells.get(pos)?.ok);
    renderMeta();
    if (listOpen) markSelected();
    syncURL();
    requestRender();
  }
  // Replace the whole reel (new sequence, or a far jump). Keeps the zoom; keeps the exact view if it's the same strip.
  function rebuild(p) {
    const old = cells.get(pos), keepLeft = old ? tx + old.X * k : null;
    const same = !!old && seqLen() > p && seqAt(p) === old.i;
    cancelAnim();
    for (const c of cells.values()) { c.img.remove(); c.label.remove(); }
    cells.clear();
    pos = p; cur = seqAt(p); anchor = p;
    ensureWindow();
    if (zoomed) {
      tx = same ? keepLeft : readTx(cells.get(p), region(true));
      clampView();
    } else applyFit();
    if (!same) { reelEl.classList.remove("fade"); void reelEl.offsetWidth; reelEl.classList.add("fade"); }
    afterPos();
    render();
  }

  // ----- fitting and clamping -----
  const fitK = (c, r) => Math.min(r.w / c.nw, r.h / c.nh, 3);
  const kFit = () => fitK(cells.get(pos), region(false));
  const kMax = () => Math.max(kFit() * 6, 2.2);
  function fitTarget(p) {
    const c = cells.get(p), r = region(false), kk = fitK(c, r);
    const top = layoutMode === "port" && !chromeOff; // phone upright: pin the strip under the header, text below it
    return {
      k: kk,
      tx: r.x + r.w / 2 - (c.X + c.nw / 2) * kk,
      ty: top ? r.y + (c.nh * kk) / 2 : r.y + r.h / 2,
      sheetTop: r.y + c.nh * kk + 10,
    };
  }
  const setSheetTop = (t) => app.style.setProperty("--sheet-top", `${Math.round(t.sheetTop)}px`);
  function applyFit() { const t = fitTarget(pos); k = t.k; tx = t.tx; ty = t.ty; setSheetTop(t); }
  function refit() { if (!cells.has(pos)) return; if (anim?.type === "tween" && !zoomed) { anim.to = fitTarget(pos); setSheetTop(anim.to); } else { applyFit(); requestRender(); } }
  // Left-align a strip (start reading at panel 1) — or center it if it's narrower than the screen
  const readTx = (c, r) => (c.nw * k < r.w ? r.x + (r.w - c.nw * k) / 2 : r.x) - c.X * k;

  // Keep the view inside the reel. Vertically, the allowed range follows the tallest strip on screen,
  // weighted by how much of it is visible — so the range grows and shrinks smoothly as a Sunday slides past.
  function clampTo(v) {
    const r = region(true), n = seqLen(), kk = v.k;
    let x = v.tx, y = v.ty;
    let lo = -Infinity, hi = Infinity;
    const first = cells.get(0), last = cells.get(n - 1);
    if (first) { const w = first.nw * kk; hi = (w < r.w ? r.x + (r.w - w) / 2 : r.x) - first.X * kk; }
    if (last) { const w = last.nw * kk; lo = (w < r.w ? r.x + (r.w + w) / 2 : r.x + r.w) - (last.X + last.nw) * kk; }
    x = lo > hi ? (lo + hi) / 2 : Math.min(hi, Math.max(lo, x));
    let h = 0;
    for (const c of cells.values()) {
      const L = x + c.X * kk, w = c.nw * kk;
      const vis = Math.min(L + w, r.x + r.w) - Math.max(L, r.x);
      if (vis > 0) h = Math.max(h, c.nh * kk * Math.min(1, vis / Math.min(r.w * 0.5, w)));
    }
    // If it fits vertically, pin it to the top of the area (right under the search bar, above any open panel);
    // if it's taller, it can be panned between its top and bottom edges.
    const ylo = r.y + r.h - 6 - h / 2, yhi = r.y + 6 + h / 2;
    y = ylo > yhi ? (layoutMode === "wide" ? r.y + r.h / 2 : yhi) : Math.min(yhi, Math.max(ylo, y)); // desktop keeps it centered
    return { k: kk, tx: x, ty: y };
  }
  function clampView() { const v = clampTo({ k, tx, ty }); tx = v.tx; ty = v.ty; }

  // Which strip is "current" while panning: the one under the middle of the screen
  function centerPos() {
    const r = region(), cx = r.x + r.w / 2;
    let best = pos, bd = Infinity;
    for (const c of cells.values()) {
      const L = tx + (c.X - GAP / 2) * k, R = tx + (c.X + c.nw + GAP / 2) * k;
      if (cx >= L && cx < R) return c.p;
      const d = Math.min(Math.abs(cx - L), Math.abs(cx - R));
      if (d < bd) { bd = d; best = c.p; }
    }
    return best;
  }

  let rafId = 0;
  function requestRender() { if (!rafId) rafId = requestAnimationFrame(() => { rafId = 0; render(); }); }
  function render() {
    if (zoomed && seqLen() && cells.size && g?.type !== "pinch") { const p = centerPos(); if (p !== pos) setPos(p); }
    const vw = innerWidth;
    for (const c of cells.values()) {
      const w = c.nw * k, x = tx + c.X * k;
      const off = x > vw + GAP * k + 40 || x + w < -40;
      if (off !== !!c.off) { c.off = off; c.img.style.visibility = c.label.style.visibility = off ? "hidden" : ""; }
      if (off) continue;
      c.img.style.width = `${w}px`;
      c.img.style.transform = `translate3d(${x}px, ${ty - (c.nh * k) / 2}px, 0)`;
      c.label.style.display = GAP * k >= 30 ? "" : "none";
      c.label.style.transform = `translate3d(${x - (GAP * k) / 2}px, ${ty}px, 0) rotate(-90deg) translate(-50%, -50%)`;
    }
    if (zoomed && cells.has(pos)) $("zoomLevel").textContent = `${(k / kFit()).toFixed(1)}×`;
    const r = region();
    stage.style.setProperty("--cx", `${r.x + r.w / 2}px`);
    stage.style.setProperty("--cy", `${r.y + r.h / 2}px`);
    stage.style.setProperty("--rx", `${r.x}px`);
    stage.style.setProperty("--rw", `${r.w}px`);
  }

  // ----- animation: tweens and momentum -----
  let anim = null;
  const cancelAnim = () => { anim = null; };
  function animateView(to, ms = 300, done) {
    anim = { type: "tween", from: { k, tx, ty }, to, t0: performance.now(), ms, done };
    requestAnimationFrame(tick);
  }
  function startFling(vx, vy) {
    anim = { type: "fling", vx, vy, last: performance.now() };
    requestAnimationFrame(tick);
  }
  function tick(now) {
    const a = anim;
    if (!a) return;
    if (a.type === "tween") {
      const t = Math.min(1, (now - a.t0) / a.ms), e = 1 - (1 - t) ** 3;
      k = a.from.k + (a.to.k - a.from.k) * e;
      tx = a.from.tx + (a.to.tx - a.from.tx) * e;
      ty = a.from.ty + (a.to.ty - a.from.ty) * e;
      render();
      if (anim !== a) return;
      if (t < 1) requestAnimationFrame(tick); else { anim = null; a.done?.(); }
    } else {
      const dt = Math.min(40, now - a.last);
      a.last = now;
      const nx = tx + a.vx * dt, ny = ty + a.vy * dt;
      tx = nx; ty = ny;
      clampView();
      if (Math.abs(tx - nx) > 0.5) a.vx = 0;
      if (Math.abs(ty - ny) > 0.5) a.vy = 0;
      const f = Math.pow(0.9945, dt);
      a.vx *= f; a.vy *= f;
      render();
      if (anim !== a) return;
      if (Math.hypot(a.vx, a.vy) > 0.03) requestAnimationFrame(tick); else anim = null;
    }
  }

  // ----- navigation -----
  function snapTo(p, ms = 300) {
    if (p !== pos) setPos(p);
    setZoomed(false);
    const t = fitTarget(pos);
    setSheetTop(t);
    animateView(t, ms);
  }
  function readAt(p) {
    const c = cells.get(p);
    animateView(clampTo({ k, tx: readTx(c, region(true)), ty }), 380);
  }
  function goTo(p) {
    if (p === pos || p < 0 || p >= seqLen()) return;
    if (cells.has(p) && Math.abs(p - pos) <= 2) { if (zoomed) readAt(p); else snapTo(p); }
    else rebuild(p);
  }
  function step(d) {
    if (!hasMove(d)) return nudge(d);
    goTo(pos + d);
  }
  function nudge(d) {
    reelEl.animate([{ transform: "none" }, { transform: `translateX(${-d * 16}px)` }, { transform: "none" }], { duration: 240, easing: "ease-out" });
  }
  function panBy(dx, dy) { animateView(clampTo({ k, tx: tx - dx, ty: ty - dy }), 260); }
  function zoomTo(px, py, nk, animate) {
    const kf = kFit();
    nk = Math.min(kMax(), Math.max(kf, nk));
    if (nk <= kf * 1.001) return snapTo(centerPos(), animate ? 300 : 150);
    setZoomed(true);
    const rx = (px - tx) / k, ry = (py - ty) / k;
    const to = clampTo({ k: nk, tx: px - rx * nk, ty: py - ry * nk });
    if (animate) animateView(to, 260);
    else { k = to.k; tx = to.tx; ty = to.ty; requestRender(); }
  }
  function settle() {
    const kf = kFit();
    if (k < kf * 1.03) return snapTo(centerPos());
    if (k > kMax()) { const r = region(); return zoomTo(r.x + r.w / 2, r.y + r.h / 2, kMax(), true); }
    clampView();
    requestRender();
  }
  // Chrome changed shape: re-fit, or keep the zoomed view inside the new region
  function chromeChanged() {
    applyChrome();
    if (!cells.has(pos)) return;
    if (zoomed) animateView(clampTo({ k, tx, ty }), 260);
    else { const t = fitTarget(pos); setSheetTop(t); animateView(t, 260); }
  }

  // ================= Gestures on the canvas =================
  // 1 finger: swipe between strips (unzoomed) or pan with momentum (zoomed). 2 fingers: pinch.
  // Double-tap: zoom in / back to fit. Single tap: full screen on/off.
  const pts = new Map();
  let g = null, tapTimer = 0, lastTap = null;
  const pt = (e) => ({ x: e.clientX, y: e.clientY });

  stage.addEventListener("pointerdown", (e) => {
    if (e.target.closest("button, a") || (e.pointerType === "mouse" && e.button !== 0) || !cells.has(pos)) return;
    if (document.activeElement === q) q.blur();
    cancelAnim();
    stage.setPointerCapture(e.pointerId);
    const p = pt(e);
    pts.set(e.pointerId, p);
    if (pts.size === 1) g = { type: "pan", sx: p.x, sy: p.y, x0: tx, y0: ty, t0: e.timeStamp, moved: false, trail: [{ t: e.timeStamp, ...p }] };
    else if (pts.size === 2) {
      const [a, b] = [...pts.values()];
      g = { type: "pinch", d0: Math.hypot(a.x - b.x, a.y - b.y) || 1, mx: (a.x + b.x) / 2, my: (a.y + b.y) / 2, k0: k, x0: tx, y0: ty };
    }
  });

  stage.addEventListener("pointermove", (e) => {
    if (!pts.has(e.pointerId) || !g) return;
    const p = pt(e);
    pts.set(e.pointerId, p);
    if (g.type === "pinch") {
      if (pts.size < 2) return;
      const [a, b] = [...pts.values()];
      const mx = (a.x + b.x) / 2, my = (a.y + b.y) / 2, kf = kFit();
      const nk = Math.min(kMax() * 1.25, Math.max(kf * 0.75, (g.k0 * Math.hypot(a.x - b.x, a.y - b.y)) / g.d0));
      const rx = (g.mx - g.x0) / g.k0, ry = (g.my - g.y0) / g.k0;
      k = nk; tx = mx - rx * k; ty = my - ry * k;
      if (!zoomed && k > kf * 1.04) setZoomed(true);
      if (zoomed && k >= kf) clampView();
      return requestRender();
    }
    const dx = p.x - g.sx, dy = p.y - g.sy;
    if (!g.moved && Math.hypot(dx, dy) < 7) return;
    g.moved = true;
    g.trail.push({ t: e.timeStamp, ...p });
    if (g.trail.length > 6) g.trail.shift();
    const vertical = Math.abs(dy) > Math.abs(dx);
    if (zoomed || g.fromPinch) {
      // Pan like a page. Whatever vertical drag the comic can't absorb is "overscroll", which pulls the search bar in or out.
      const raw = g.y0 + dy;
      tx = g.x0 + dx; ty = raw;
      clampView();
      g.over = raw - ty;
      if (vertical) ty += g.over * 0.3; // rubber-band
    } else {
      g.axis ||= Math.abs(dx) > Math.abs(dy) ? "x" : "y";
      if (g.axis === "x") tx = g.x0 + (hasMove(dx < 0 ? 1 : -1) ? dx : dx * 0.3);
      else { g.over = dy; if (canPull(dy)) ty = g.y0 + dy * 0.3; }
    }
    pullFeedback(g, vertical || g.axis === "y");
    requestRender();
  });

  // ----- pull the search bar down (or push it away) by dragging the comic, as if scrolling a page -----
  const headerShown = () => !app.classList.contains("no-bar");
  // The bar can be pulled in when it's hidden, and pushed away when it's an optional extra (not the portrait layout's own header)
  const canPull = (over) => layoutMode !== "wide" && (over > 0 ? !headerShown() : headerShown() && (zoomed || layoutMode === "land" || chromeOff));
  function pullFeedback(gg, vertical) {
    const over = gg.over || 0, h = bar.offsetHeight || 60;
    gg.pull = null;
    if (!vertical || !over || !canPull(over)) return clearPull();
    const p = Math.min(1, (Math.abs(over) * 0.5) / h);
    bar.style.transition = "none";
    if (over > 0) { bar.style.transform = `translateY(${(p - 1) * 110}%)`; bar.style.opacity = String(p); bar.style.pointerEvents = "none"; }
    else { bar.style.transform = `translateY(${-p * 110}%)`; bar.style.opacity = String(1 - p); }
    if (p >= 0.6) gg.pull = over > 0 ? "show" : "hide";
  }
  function clearPull() { bar.style.transition = bar.style.transform = bar.style.opacity = bar.style.pointerEvents = ""; }

  function pointerEnd(e) {
    if (!pts.has(e.pointerId)) return;
    pts.delete(e.pointerId);
    if (!g) return;
    if (g.type === "pinch") {
      if (pts.size === 1) { const p = [...pts.values()][0]; g = { type: "pan", sx: p.x, sy: p.y, x0: tx, y0: ty, t0: e.timeStamp, moved: true, fromPinch: true, trail: [] }; }
      else if (!pts.size) { g = null; settle(); }
      return;
    }
    if (pts.size) return;
    const gg = g;
    g = null;
    const p = pt(e), dx = p.x - gg.sx, dy = p.y - gg.sy;
    const pull = e.type === "pointercancel" ? null : gg.pull;
    clearPull();
    if (pull) {
      barOn = pull === "show";
      if (barOn) chromeOff = false; else q.blur();
      return chromeChanged(); // re-fits / re-clamps below (or without) the bar, which also settles the rubber-band
    }
    if (gg.fromPinch) return settle();
    if (e.type === "pointercancel") return zoomed ? animateView(clampTo({ k, tx, ty }), 200) : snapTo(pos);
    if (!gg.moved) return tap(p);
    if (zoomed) {
      const tr = gg.trail.filter((s) => e.timeStamp - s.t < 90);
      const overscrolled = Math.abs(dy) > Math.abs(dx) && Math.abs(gg.over || 0) > 8;
      if (tr.length >= 2 && !overscrolled) { const a = tr[0], b = tr.at(-1), dt = Math.max(8, b.t - a.t); startFling((b.x - a.x) / dt, (b.y - a.y) / dt); }
      else animateView(clampTo({ k, tx, ty }), 200);
      return;
    }
    if (gg.axis === "y") return snapTo(pos);
    const r = region(), fast = Math.abs(dx) / Math.max(1, e.timeStamp - gg.t0) > 0.35;
    const d = Math.abs(dx) > Math.abs(dy) && (Math.abs(dx) > r.w * 0.16 || (fast && Math.abs(dx) > 30)) ? (dx < 0 ? 1 : -1) : 0;
    snapTo(d && hasMove(d) ? pos + d : pos);
  }
  stage.addEventListener("pointerup", pointerEnd);
  stage.addEventListener("pointercancel", pointerEnd);

  function tap(p) {
    if (tapTimer && lastTap && Math.hypot(p.x - lastTap.x, p.y - lastTap.y) < 40) {
      clearTimeout(tapTimer);
      tapTimer = 0;
      if (zoomed) snapTo(centerPos());
      else zoomTo(p.x, p.y, kFit() * 2.5, true);
      return;
    }
    lastTap = p;
    clearTimeout(tapTimer);
    tapTimer = setTimeout(() => { tapTimer = 0; singleTap(); }, 280);
  }
  function singleTap() {
    if (listOpen) return setList(false);
    if (sheetOpen) { sheetOpen = false; return chromeChanged(); }
    if (layoutMode === "wide") return;
    chromeOff = !chromeOff;
    if (chromeOff) { barOn = false; q.blur(); } // full screen also tucks away a pinned search bar
    chromeChanged();
  }

  // Wheel / trackpad: ctrl+wheel (pinch) or a mouse wheel zooms, two-finger scroll pans when zoomed, a sideways flick changes strip
  let wheelAcc = 0, wheelLock = 0;
  stage.addEventListener("wheel", (e) => {
    e.preventDefault();
    if (!cells.has(pos)) return;
    cancelAnim();
    const mouseWheel = e.deltaMode === 1 || (Math.abs(e.deltaY) >= 50 && !e.deltaX && !e.ctrlKey);
    if (e.ctrlKey) return zoomTo(e.clientX, e.clientY, k * Math.exp(-e.deltaY * 0.01), false);
    if (mouseWheel) return zoomTo(e.clientX, e.clientY, k * Math.exp(-Math.sign(e.deltaY) * 0.18), false);
    if (zoomed) { tx -= e.deltaX; ty -= e.deltaY; clampView(); return requestRender(); }
    if (Math.abs(e.deltaX) > Math.abs(e.deltaY)) {
      wheelAcc += e.deltaX;
      if (Math.abs(wheelAcc) > 80 && e.timeStamp > wheelLock) { step(wheelAcc > 0 ? 1 : -1); wheelAcc = 0; wheelLock = e.timeStamp + 450; }
    }
  }, { passive: false });

  // Swiping sideways on the text panel also changes strip (vertical drags still scroll it)
  let sw = null, swipedAt = -1e9;
  sheet.addEventListener("pointerdown", (e) => {
    if (e.pointerType === "mouse" || e.target.closest("input")) return;
    sw = { x: e.clientX, y: e.clientY, t: e.timeStamp, id: e.pointerId };
  });
  sheet.addEventListener("pointerup", (e) => {
    if (!sw || e.pointerId !== sw.id) return;
    const dx = e.clientX - sw.x, dy = e.clientY - sw.y, dt = e.timeStamp - sw.t;
    sw = null;
    if (Math.abs(dx) > 60 && Math.abs(dx) > 2 * Math.abs(dy) && dt < 800) { swipedAt = e.timeStamp; step(dx < 0 ? 1 : -1); }
  });
  sheet.addEventListener("pointercancel", () => { sw = null; });
  sheet.addEventListener("click", (e) => { if (e.timeStamp - swipedAt < 450) { e.preventDefault(); e.stopPropagation(); } }, true);

  // ================= Text, results, URL =================
  function renderMeta() {
    const st = strips[cur];
    if (!st) return;
    const d = dateParts(st.id);
    $("whenDay").textContent = d.day;
    $("whenDay").classList.toggle("sun", d.sunday);
    $("whenDate").textContent = d.date;
    $("datePick").value = isoDate(st.id);
    $("peek").textContent = st.q;
    quoteEl.classList.remove("dim");
    quoteEl.innerHTML = marked(st.q, inSearch() ? hlFor(results[pos]) : null);
    const n = seqLen();
    countBtn.innerHTML = inSearch()
      ? `<svg class="ic"><use href="#i-list"/></svg>${n ? `${fmt.format(pos + 1)}<span class="of">/${fmt.format(n)}</span>` : "0 found"}`
      : `${fmt.format(pos + 1)}<span class="of">/${fmt.format(n)}</span>`;
    prevBtn.disabled = $("sidePrev").disabled = !hasMove(-1);
    nextBtn.disabled = $("sideNext").disabled = !hasMove(1);
    $("live").textContent = `${d.day} ${d.date}`;
  }

  function renderList() {
    const show = inSearch() && listOpen;
    resultsWrap.hidden = !show;
    textEl.hidden = show;
    if (!show) return;
    if (!results.length) {
      $("rmeta").textContent = "No strips match. Try fewer or different words.";
      resultsEl.innerHTML = "";
      return;
    }
    const n = Math.min(results.length, LIST_LIMIT);
    $("rmeta").textContent = `${fmt.format(results.length)} strip${results.length > 1 ? "s" : ""} · best match first${results.length > n ? ` · top ${n} listed` : ""}`;
    resultsEl.innerHTML = results.slice(0, n).map((r, p) => {
      const st = strips[r.i];
      return `<li role="option" id="r${p}" aria-selected="${p === pos}"><button type="button" tabindex="-1" data-p="${p}">` +
        `<span class="rdate"><i class="dot ${tierDot(r.tier)}" title="${TIERS[r.tier]}"></i>${dateParts(st.id).date}</span>` +
        `<span class="rsnip">${snippet(st.q, hlFor(r))}</span></button></li>`;
    }).join("");
    markSelected();
  }
  function markSelected() {
    resultsEl.querySelector('[aria-selected="true"]')?.setAttribute("aria-selected", "false");
    const li = $(`r${pos}`);
    if (!li) return;
    li.setAttribute("aria-selected", "true");
    q.setAttribute("aria-activedescendant", li.id);
    li.scrollIntoView({ block: "nearest" });
  }
  function setList(v) {
    listOpen = v && inSearch();
    renderList();
    chromeChanged();
  }

  let expectHash = "";
  function syncURL() {
    const st = strips[cur];
    if (!st) return;
    let h = `#${st.id}`;
    if (inSearch() && query.trim()) h += `?q=${encodeURIComponent(query.trim()).replace(/%20/g, "+")}`;
    expectHash = h;
    if (location.hash !== h) history.replaceState(history.state, "", h);
  }
  const parseHash = () => {
    const [id, qs] = location.hash.slice(1).split("?");
    return { id: /^\d{8}$/.test(id) ? id : null, text: new URLSearchParams(qs || "").get("q") || "" };
  };
  function lowerBound(id) {
    let lo = 0, hi = strips.length;
    while (lo < hi) { const m = (lo + hi) >> 1; if (strips[m].id < id) lo = m + 1; else hi = m; }
    return Math.min(lo, strips.length - 1);
  }
  function onThisDay() {
    const now = new Date();
    const md = String(now.getMonth() + 1).padStart(2, "0") + String(now.getDate()).padStart(2, "0");
    for (let i = strips.length - 1; i >= 0; i--) if (strips[i].id.slice(4) === md) return i;
    return 0;
  }

  // ----- search lifecycle -----
  // Entering search pushes one history entry, so the phone's Back button (or Esc, or either ✕) cancels it.
  function runSearch(text, { live = true, preferId = null } = {}) {
    const r = search(text);
    if (!r) {
      if (inSearch()) { const keep = q.value; cancelSearch(() => { q.value = keep; }); }
      return;
    }
    if (!inSearch()) {
      mode = "search";
      if (live && !history.state?.chSearch) history.pushState({ chSearch: 1 }, "", location.href);
    }
    S = r; results = r.list; query = text;
    // Zoomed in, typing filters the reel itself (same zoom, best match first); the ≡ count opens the list on demand
    if (live && !zoomed) listOpen = true;
    let p = 0;
    if (preferId) { const j = results.findIndex((x) => strips[x.i].id === preferId); if (j >= 0) p = j; }
    applyChrome();
    // rebuild() reads the old reel (keyed by old positions) to keep the view if the best match is the strip on screen
    if (results.length) rebuild(p);
    else renderMeta(); // nothing matches: keep showing the current strip
    renderList();
  }
  function endSearch() {
    const i = cur;
    mode = "timeline"; S = null; results = []; query = ""; listOpen = false;
    q.value = "";
    q.removeAttribute("aria-activedescendant");
    renderList();
    applyChrome();
    if (i >= 0) rebuild(i);
  }
  let afterPop = null;
  function cancelSearch(then) {
    if (!inSearch()) { q.value = ""; then?.(); return; }
    if (history.state?.chSearch) { afterPop = then || null; history.back(); return; }
    endSearch();
    then?.();
  }
  window.addEventListener("popstate", () => {
    if (!inSearch()) return;
    endSearch();
    const f = afterPop; afterPop = null; f?.();
  });
  window.addEventListener("hashchange", () => {
    if (location.hash === expectHash || !strips.length) return;
    const { id, text } = parseHash();
    if (text) { q.value = text; runSearch(text, { live: false, preferId: id }); }
    else {
      if (inSearch()) endSearch();
      if (id) goTo(lowerBound(id));
    }
  });

  // ================= Controls =================
  let typeTimer = 0;
  q.addEventListener("input", () => { clearTimeout(typeTimer); typeTimer = setTimeout(() => runSearch(q.value), 90); });
  // The search bar, once shown, stays pinned (through typing, browsing results, cancelling) until you push it away
  q.addEventListener("focus", () => {
    const wasShown = headerShown();
    barOn = true;
    if (inSearch() && !zoomed) listOpen = true;
    renderList();
    if (!wasShown || listOpen) chromeChanged(); else applyChrome();
  });
  q.addEventListener("keydown", (e) => {
    if (e.key === "Escape") { e.preventDefault(); cancelSearch(); q.blur(); return; }
    if (e.key === "Enter") {
      e.preventDefault();
      clearTimeout(typeTimer);
      if (q.value !== query) runSearch(q.value);
      q.blur();
      setList(false);
      return;
    }
    if ((e.key === "ArrowDown" || e.key === "ArrowUp") && inSearch() && results.length) {
      e.preventDefault();
      if (!listOpen) setList(true);
      const p = Math.min(results.length - 1, Math.max(0, pos + (e.key === "ArrowDown" ? 1 : -1)));
      if (p !== pos) goTo(p);
    }
  });
  $("searchBox").addEventListener("click", (e) => { if (!e.target.closest("button")) q.focus(); });
  $("clear").addEventListener("click", () => { cancelSearch(); q.blur(); });
  $("cancel2").addEventListener("click", () => cancelSearch());
  $("searchBtn").addEventListener("click", () => { barOn = true; chromeChanged(); q.focus(); });

  resultsEl.addEventListener("click", (e) => {
    const b = e.target.closest("button[data-p]");
    if (!b) return;
    q.blur();
    setList(false);
    goTo(+b.dataset.p);
  });
  countBtn.addEventListener("click", () => { if (inSearch()) setList(!listOpen); });
  // The bottom bar: tap anywhere on it (the text line included) to open or close it; swipe it up to open, down to close
  const barMode = () => /\bS-(bar|over)\b/.test(app.className);
  function toggleSheet(open = !(sheetOpen || listOpen)) {
    if (!open && listOpen) return setList(false);
    if (sheetOpen === open) return;
    sheetOpen = open;
    chromeChanged();
  }
  $("grab").addEventListener("click", () => toggleSheet());
  $("head").addEventListener("click", (e) => {
    const b = e.target.closest("button, input");
    if (!barMode() || (b && !(b === countBtn && !inSearch())) || e.timeStamp - swipedAt < 450) return;
    toggleSheet();
  });
  let vs = null;
  sheet.addEventListener("pointerdown", (e) => { if (barMode() && e.target.closest(".head, .grab")) vs = { x: e.clientX, y: e.clientY, id: e.pointerId }; });
  sheet.addEventListener("pointerup", (e) => {
    if (!vs || e.pointerId !== vs.id) return;
    const dx = e.clientX - vs.x, dy = e.clientY - vs.y;
    vs = null;
    if (Math.abs(dy) > 30 && Math.abs(dy) > 1.5 * Math.abs(dx)) { swipedAt = e.timeStamp; toggleSheet(dy < 0); }
  });
  $("zoomChip").addEventListener("click", () => snapTo(centerPos()));

  prevBtn.addEventListener("click", () => step(-1));
  nextBtn.addEventListener("click", () => step(1));
  $("sidePrev").addEventListener("click", () => step(-1));
  $("sideNext").addEventListener("click", () => step(1));
  $("random").addEventListener("click", () => cancelSearch(() => goTo(Math.floor(Math.random() * strips.length))));

  const datePick = $("datePick");
  $("when").addEventListener("click", () => { try { datePick.showPicker(); } catch { datePick.focus(); datePick.click(); } });
  datePick.addEventListener("change", () => {
    const v = datePick.value.replace(/-/g, "");
    if (v.length === 8) cancelSearch(() => goTo(lowerBound(v)));
  });

  document.addEventListener("keydown", (e) => {
    if (e.target === q || e.target.matches("input, textarea") || e.metaKey || e.ctrlKey || e.altKey || !cells.has(pos)) return;
    const r = region(), key = e.key;
    if (key === "ArrowLeft") zoomed ? panBy(-r.w * 0.8, 0) : step(-1);
    else if (key === "ArrowRight") zoomed ? panBy(r.w * 0.8, 0) : step(1);
    else if ((key === "ArrowUp" || key === "ArrowDown") && zoomed) panBy(0, (key === "ArrowDown" ? 0.5 : -0.5) * r.h);
    else if (key === "/") { q.focus(); q.select(); }
    else if (key === "Escape") {
      if (listOpen) setList(false);
      else if (zoomed) snapTo(centerPos());
      else if (inSearch()) cancelSearch();
      else if (chromeOff) { chromeOff = false; chromeChanged(); }
    }
    else if (key === "+" || key === "=") zoomTo(r.x + r.w / 2, r.y + r.h / 2, k * 1.5, true);
    else if (key === "-") zoomTo(r.x + r.w / 2, r.y + r.h / 2, k / 1.5, true);
    else if (key === "0") { if (zoomed) snapTo(centerPos()); }
    else if (key === "f" || key === "F") { if (layoutMode !== "wide") { chromeOff = !chromeOff; chromeChanged(); } }
    else if (key === "r" || key === "R") $("random").click();
    else return;
    e.preventDefault();
  });

  function onResize() {
    safeCache = null;
    const prev = layoutMode;
    computeLayoutMode();
    if (prev !== layoutMode) { zoomed = false; sheetOpen = false; chromeOff = false; barOn = document.activeElement === q; }
    applyChrome();
    if (!cells.has(pos)) return;
    cancelAnim();
    if (document.activeElement === q && prev === layoutMode) return requestRender(); // keyboard opened: keep the strip as is
    if (zoomed) clampView(); else applyFit();
    render();
  }
  addEventListener("resize", onResize);
  // The opened panel's height follows each strip's text: keep the strip area (and a zoomed strip) above it
  new ResizeObserver(() => {
    regionCache = {};
    if (cells.has(pos) && !g && !anim && zoomed && /\bS-over\b/.test(app.className)) { clampView(); requestRender(); }
  }).observe(sheet);
  document.fonts?.ready.then(onResize);

  // ----- copying -----
  const toastEl = $("toast");
  let toastTimer = 0;
  function toast(msg, ms = 1800) {
    toastEl.textContent = msg;
    toastEl.classList.toggle("show", !!msg);
    clearTimeout(toastTimer);
    if (msg && ms) toastTimer = setTimeout(() => toastEl.classList.remove("show"), ms);
  }
  async function copyString(str, ok) {
    try { await navigator.clipboard.writeText(str); return toast(ok); } catch {}
    const ta = Object.assign(document.createElement("textarea"), { value: str });
    ta.style.cssText = "position:fixed;top:0;left:0;opacity:0";
    document.body.append(ta);
    ta.select();
    const done = document.execCommand("copy");
    ta.remove();
    toast(done ? ok : "Couldn't copy");
  }
  $("copyText").addEventListener("click", () => copyString(strips[cur].q, "Text copied"));
  $("copyLink").addEventListener("click", () => copyString(IMG(strips[cur].id), "Image link copied"));
  async function toPng(blob) {
    const bmp = await createImageBitmap(blob);
    const c = Object.assign(document.createElement("canvas"), { width: bmp.width, height: bmp.height });
    c.getContext("2d").drawImage(bmp, 0, 0);
    return new Promise((res, rej) => c.toBlob((b) => (b ? res(b) : rej(new Error("PNG failed"))), "image/png"));
  }
  $("copyImg").addEventListener("click", async () => {
    const id = strips[cur].id;
    // Build the PNG as a promise and hand it to ClipboardItem right away: Safari only allows the write inside the tap
    const png = fetch(PROXY + IMG(id)).then((r) => { if (!r.ok) throw new Error(r.status); return r.blob(); }).then(toPng);
    png.catch(() => {});
    toast("Copying image…", 0);
    try {
      await navigator.clipboard.write([new ClipboardItem({ "image/png": png })]);
      return toast("Image copied");
    } catch {}
    try {
      const file = new File([await png], `calvin-and-hobbes-${id}.png`, { type: "image/png" });
      if (navigator.canShare?.({ files: [file] })) { toast(""); await navigator.share({ files: [file] }); return; }
    } catch (err) { if (err?.name === "AbortError") return toast(""); }
    toast("Couldn't copy. Long-press the strip instead.");
  });

  // ----- theme -----
  function syncThemeColor() { $("themeColor").content = getComputedStyle(document.documentElement).getPropertyValue("--bg").trim(); }
  $("theme").addEventListener("click", () => {
    const t = document.documentElement.dataset.theme;
    const dark = t ? t === "dark" : matchMedia("(prefers-color-scheme: dark)").matches;
    document.documentElement.dataset.theme = dark ? "light" : "dark";
    try { localStorage.setItem("ch-theme", document.documentElement.dataset.theme); } catch {}
    syncThemeColor();
  });
  matchMedia("(prefers-color-scheme: dark)").addEventListener("change", syncThemeColor);
  syncThemeColor();

  // ================= Load =================
  computeLayoutMode();
  applyChrome();
  fetch(DATA_URL)
    .then((r) => { if (!r.ok) throw new Error(`HTTP ${r.status}`); return r.text(); })
    .then((tsv) => {
      for (const line of tsv.split(/\r?\n/)) {
        const tab = line.indexOf("\t");
        const id = line.slice(0, tab).trim();
        if (tab < 0 || !/^\d{8}$/.test(id)) continue;
        strips.push({ id, q: line.slice(tab + 1).trim() });
      }
      strips.sort((a, b) => (a.id < b.id ? -1 : a.id > b.id ? 1 : 0));
      for (const st of strips) {
        const toks = norm(st.q).split(" ").filter(Boolean);
        st.n = ` ${toks.join(" ")} `;
        st.t = Int32Array.from(toks, tokId);
      }
      q.placeholder = `Search ${fmt.format(strips.length)} strips`;
      datePick.min = isoDate(strips[0].id);
      datePick.max = isoDate(strips.at(-1).id);
      const { id, text } = parseHash();
      if (text) { q.value = text; runSearch(text, { live: false, preferId: id }); }
      if (!results.length) { if (inSearch()) endSearch(); rebuild(id ? lowerBound(id) : onThisDay()); } // no link? open on today's date
      if (matchMedia("(pointer: coarse)").matches) {
        try { if (!localStorage.getItem("ch-hint3")) { localStorage.setItem("ch-hint3", "1"); toast("Pinch to zoom · tap for full screen", 3500); } } catch {}
      }
    })
    .catch((err) => {
      stage.classList.remove("loading");
      quoteEl.textContent = `Couldn't load the strips (${err.message}). Check your connection and reload.`;
    });

  // Test hooks: calvinSearch("tiger trap"), calvinView()
  window.calvinSearch = (t) => search(t)?.list.slice(0, 10).map((r) => ({ id: strips[r.i].id, tier: TIERS[r.tier], text: strips[r.i].q.slice(0, 90) }));
  window.calvinView = () => ({ k, tx, ty, pos, id: strips[cur]?.id, zoomed, layoutMode, sheet: app.className.match(/S-\w+/)?.[0], region: region(), fit: cells.has(pos) ? kFit() : null,
    cells: [...cells.values()].map((c) => ({ p: c.p, id: strips[c.i].id, x: Math.round(tx + c.X * k), y: Math.round(ty - (c.nh * k) / 2), w: Math.round(c.nw * k), h: Math.round(c.nh * k) })) });
})();
</script>
</body>
</html>
