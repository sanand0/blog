---
title: Calvin & Hobbes Quote Search
hide: true
---

<style>
  @import url("https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,700&family=Recursive:wght@400;600&display=swap");
  :root {
    --calvin-ink: #1c1d1b;
    --calvin-paper: #f7f2e8;
    --calvin-accent: #d65b2a;
    --calvin-accent-dark: #a84520;
    --calvin-mist: #f0e4d3;
    --calvin-shadow: rgba(20, 18, 12, 0.12);
  }

  .calvin-viewer {
    font-family: "Recursive", "Helvetica Neue", sans-serif;
    color: var(--calvin-ink);
    background:
      radial-gradient(circle at top left, rgba(214, 91, 42, 0.08), transparent 55%),
      radial-gradient(circle at bottom right, rgba(28, 29, 27, 0.06), transparent 55%),
      repeating-linear-gradient(135deg, rgba(28, 29, 27, 0.04) 0 2px, transparent 2px 10px),
      var(--calvin-paper);
    padding: 2.5rem clamp(1.5rem, 4vw, 4rem);
    border-radius: 24px;
    box-shadow: 0 24px 50px -40px rgba(0, 0, 0, 0.6);
  }

  .calvin-header {
    display: grid;
    gap: 1.5rem;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    align-items: end;
    margin-bottom: 2rem;
  }

  .calvin-brand h1 {
    font-family: "Fraunces", "Times New Roman", serif;
    font-size: clamp(2.2rem, 4vw, 3.4rem);
    margin: 0 0 0.35rem;
    letter-spacing: 0.5px;
  }

  .calvin-brand p {
    margin: 0;
    max-width: 34ch;
    font-size: 1rem;
    color: rgba(28, 29, 27, 0.7);
  }

  .calvin-controls {
    display: grid;
    gap: 1rem;
    justify-items: start;
  }

  .calvin-search {
    display: grid;
    gap: 0.35rem;
    width: 100%;
  }

  .calvin-search label {
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: rgba(28, 29, 27, 0.65);
  }

  .calvin-search input {
    width: 100%;
    padding: 0.7rem 0.9rem;
    border-radius: 12px;
    border: 1px solid rgba(28, 29, 27, 0.15);
    background: #fffaf3;
    font-size: 1rem;
  }

  .calvin-search input:focus {
    outline: 2px solid rgba(214, 91, 42, 0.35);
    border-color: rgba(214, 91, 42, 0.65);
  }

  .calvin-nav {
    display: flex;
    gap: 0.75rem;
    flex-wrap: wrap;
  }

  .calvin-nav button {
    border: none;
    padding: 0.6rem 1.2rem;
    border-radius: 999px;
    background: var(--calvin-accent);
    color: #fff;
    font-weight: 600;
    letter-spacing: 0.03em;
    cursor: pointer;
    transition: transform 0.2s ease, box-shadow 0.2s ease, background 0.2s ease;
    box-shadow: 0 10px 18px -14px var(--calvin-shadow);
  }

  .calvin-nav button:hover {
    transform: translateY(-1px);
    background: var(--calvin-accent-dark);
  }

  .calvin-nav button:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }

  .calvin-meta {
    font-size: 0.9rem;
    color: rgba(28, 29, 27, 0.7);
  }

  .calvin-stage {
    position: relative;
    background: linear-gradient(180deg, #fffaf3, #f4e6d5);
    border-radius: 20px;
    padding: clamp(1rem, 3vw, 2rem);
    box-shadow: inset 0 0 0 1px rgba(28, 29, 27, 0.05);
    animation: calvin-rise 0.6s ease both;
  }

  .calvin-stage.is-loading .calvin-spinner {
    opacity: 1;
    pointer-events: auto;
  }

  .calvin-spinner {
    position: absolute;
    inset: 1rem;
    border-radius: 16px;
    display: grid;
    place-items: center;
    background: rgba(255, 255, 255, 0.7);
    backdrop-filter: blur(2px);
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.2s ease;
  }

  .calvin-spinner::before {
    content: "";
    width: 36px;
    height: 36px;
    border-radius: 50%;
    border: 4px solid rgba(28, 29, 27, 0.2);
    border-top-color: var(--calvin-accent);
    animation: calvin-spin 0.8s linear infinite;
  }

  .calvin-image {
    max-width: 100%;
    display: block;
    margin: 0 auto;
    border-radius: 12px;
    box-shadow: 0 18px 36px -30px rgba(0, 0, 0, 0.6);
  }

  .calvin-caption {
    margin-top: 1.25rem;
    font-size: 1.1rem;
    line-height: 1.6;
    text-align: center;
  }

  .calvin-caption em {
    display: block;
    margin-top: 0.5rem;
    font-size: 0.9rem;
    color: rgba(28, 29, 27, 0.65);
    font-style: normal;
  }

  @keyframes calvin-spin {
    to {
      transform: rotate(360deg);
    }
  }

  @keyframes calvin-rise {
    from {
      transform: translateY(12px);
      opacity: 0;
    }
    to {
      transform: translateY(0);
      opacity: 1;
    }
  }
</style>

<div class="calvin-viewer">
  <div class="calvin-header">
    <div class="calvin-brand">
      <h1>Calvin &amp; Hobbes</h1>
      <p>Browse daily strips, jump through time, and search the archive by quote.</p>
    </div>
    <div class="calvin-controls">
      <div class="calvin-search">
        <label for="calvin-search">Search quotes</label>
        <input id="calvin-search" type="search" placeholder="e.g. homework, dad, spaceship" aria-label="Search quotes">
      </div>
      <div class="calvin-nav">
        <button id="calvin-prev" type="button">&larr; Previous</button>
        <button id="calvin-next" type="button">Next &rarr;</button>
      </div>
      <div class="calvin-meta" id="calvin-meta"></div>
    </div>
  </div>
  <figure class="calvin-stage" id="calvin-stage">
    <div class="calvin-spinner" aria-hidden="true"></div>
    <img id="calvin-image" class="calvin-image" alt="">
    <figcaption id="calvin-caption" class="calvin-caption"></figcaption>
  </figure>
</div>

<script src="https://cdn.jsdelivr.net/npm/fuse.js@7.0.0/dist/fuse.min.js" defer></script>
<script src="/blog/js/calvin.js" defer></script>
