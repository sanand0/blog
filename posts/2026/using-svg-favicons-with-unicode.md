---
title: Using SVG favicons with Unicode
date: 2026-01-01T13:00:00Z
categories:
  - coding
---

![](https://files.s-anand.net/images/2026-01-01-svg-favicons-unicode.webp)

Browsers support [SVG favicons](https://caniuse.com/link-icon-svg) as [`data:` URLs](https://developer.mozilla.org/en-US/docs/Web/URI/Reference/Schemes/data).

For example, this SVG:

```html
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">
  <circle cx="16" cy="16" r="15" fill="#2563eb"/>
  <path fill="#fff" d="m16 7 2 7 7 2-7 2-2 7-2-7-7-2 7-2Z"/>
</svg>
```

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="128">
  <circle cx="16" cy="16" r="15" fill="#2563eb"/>
  <path fill="#fff" d="m16 7 2 7 7 2-7 2-2 7-2-7-7-2 7-2Z"/>
</svg>

... can be:

1. Compressed via [svgomg](https://svgomg.net/)
2. Converted to a `data:` URL via [svgviewer](https://www.svgviewer.dev/svg-to-data-uri)
3. Inserted into HTML like this:

```html
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%2032%2032%22%3E%3Ccircle%20cx%3D%2216%22%20cy%3D%2216%22%20r%3D%2215%22%20fill%3D%22%232563eb%22%2F%3E%3Cpath%20fill%3D%22%23fff%22%20d%3D%22m16%207%202%207%207%202-7%202-2%207-2-7-7-2%207-2Z%22%2F%3E%3C%2Fsvg%3E"/>
```

The fun part is that you can use text inside the SVG, styled as you wish:

```html
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect fill="#2563eb" width="64" height="64" rx="10"/>
  <text x="32" y="35" text-anchor="middle" dominant-baseline="middle" font-size="40" font-weight="800" fill="white">DS</text>
</svg>
```

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="128">
  <rect fill="#2563eb" width="64" height="64" rx="10"/>
  <text x="32" y="35" text-anchor="middle" dominant-baseline="middle" font-size="40" font-weight="800" fill="white">DS</text>
</svg>

... or even use Unicode characters:

```html
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect fill="#2563eb" width="64" height="64" rx="10"/>
  <text x="32" y="35" text-anchor="middle" dominant-baseline="middle" font-size="40" font-weight="800" fill="white">🌈</text>
</svg>
```

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="128">
  <rect fill="#2563eb" width="64" height="64" rx="10"/>
  <text x="32" y="35" text-anchor="middle" dominant-baseline="middle" font-size="40" font-weight="800" fill="white">🌈</text>
</svg>

That can be converted into a HTML link like this:

```html
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%2064%2064%22%3E%3Crect%20width%3D%2264%22%20height%3D%2264%22%20fill%3D%22%232563eb%22%20rx%3D%2210%22%2F%3E%3Ctext%20x%3D%2232%22%20y%3D%2235%22%20fill%3D%22%23fff%22%20dominant-baseline%3D%22middle%22%20font-size%3D%2240%22%20font-weight%3D%22800%22%20text-anchor%3D%22middle%22%3E%F0%9F%8C%88%3C%2Ftext%3E%3C%2Fsvg%3E"/>
```

The variety is endless!

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64">
  <rect fill="oklch(0.4 0.15 0)" width="64" height="64" rx="10"/>
  <text x="32" y="35" text-anchor="middle" dominant-baseline="middle" font-size="40" font-weight="800" fill="white">⚡</text>
</svg> <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64">
  <rect fill="oklch(0.4 0.15 45)" width="64" height="64" rx="10"/>
  <text x="32" y="35" text-anchor="middle" dominant-baseline="middle" font-size="40" font-weight="800" fill="white">🖱️</text>
</svg> <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64">
  <rect fill="oklch(0.4 0.15 90)" width="64" height="64" rx="10"/>
  <text x="32" y="35" text-anchor="middle" dominant-baseline="middle" font-size="40" font-weight="800" fill="white">✦</text>
</svg> <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64">
  <rect fill="oklch(0.4 0.15 135)" width="64" height="64" rx="10"/>
  <text x="32" y="35" text-anchor="middle" dominant-baseline="middle" font-size="40" font-weight="800" fill="white">◈</text>
</svg> <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64">
  <rect fill="oklch(0.4 0.15 180)" width="64" height="64" rx="10"/>
  <text x="32" y="35" text-anchor="middle" dominant-baseline="middle" font-size="40" font-weight="800" fill="white">↻</text>
</svg> <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64">
  <rect fill="oklch(0.4 0.15 225)" width="64" height="64" rx="10"/>
  <text x="32" y="35" text-anchor="middle" dominant-baseline="middle" font-size="40" font-weight="800" fill="white">⭕</text>
</svg> <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64">
  <rect fill="oklch(0.4 0.15 270)" width="64" height="64" rx="10"/>
  <text x="32" y="35" text-anchor="middle" dominant-baseline="middle" font-size="40" font-weight="800" fill="white">🕒</text>
</svg> <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64">
  <rect fill="oklch(0.4 0.15 315)" width="64" height="64" rx="10"/>
  <text x="32" y="35" text-anchor="middle" dominant-baseline="middle" font-size="40" font-weight="800" fill="white">👨‍👦</text>
</svg>

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64">
  <rect fill="#1e3a5f" width="64" height="64" rx="12"></rect>
  <text x="32" y="24" text-anchor="middle" font-size="24" font-weight="800" fill="#dbeafe">T</text>
  <text x="32" y="52" text-anchor="middle" font-size="24" font-weight="800" fill="#dbeafe">L</text>
</svg> <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64">
  <rect fill="#3b82f6" width="64" height="64" rx="12"></rect>
  <text x="32" y="42" text-anchor="middle" font-family="Georgia, serif" font-size="38" font-weight="700" fill="white">T</text>
  <text x="48" y="54" text-anchor="middle" font-size="16" font-weight="500" fill="rgba(255,255,255,0.7)">l</text>
</svg> <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64">
  <rect fill="#1e1e1e" width="64" height="64" rx="12"></rect>
  <rect x="8" y="16" width="23" height="32" rx="2" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.1)" stroke-width="1"></rect>
  <rect x="33" y="16" width="23" height="32" rx="2" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.1)" stroke-width="1"></rect>
  <text x="19.5" y="40" text-anchor="middle" font-family="monospace" font-size="24" font-weight="600" fill="#3b82f6">T</text>
  <text x="44.5" y="40" text-anchor="middle" font-family="monospace" font-size="24" font-weight="600" fill="#3b82f6">L</text>
</svg> <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64">
  <rect fill="#1e3a5f" width="64" height="64" rx="12"></rect>
  <text x="22" y="42" text-anchor="middle" font-size="32" font-weight="200" fill="#dbeafe">T</text>
  <text x="44" y="42" text-anchor="middle" font-size="32" font-weight="900" fill="#dbeafe">L</text>
</svg> <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64">
  <rect fill="#3b82f6" width="64" height="64" rx="12"></rect>
  <text x="28" y="48" text-anchor="middle" font-size="52" font-weight="900" fill="white">T</text>
  <text x="52" y="20" text-anchor="middle" font-size="14" font-weight="600" fill="rgba(255,255,255,0.6)">L</text>
</svg> <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64">
  <rect fill="#1e3a5f" width="64" height="64" rx="12"></rect>
  <text x="26" y="44" text-anchor="middle" font-size="40" font-weight="900" fill="#3b82f6">T</text>
  <text x="38" y="44" text-anchor="middle" font-size="40" font-weight="900" fill="#dbeafe" opacity="0.9">L</text>
</svg> <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64">
  <rect fill="#dbeafe" width="64" height="64" rx="12"></rect>
  <text x="20" y="32" text-anchor="middle" font-size="28" font-weight="800" fill="#1e3a5f">T</text>
  <text x="44" y="46" text-anchor="middle" font-size="28" font-weight="800" fill="#1e3a5f">L</text>
</svg> <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64">
  <rect fill="#0f0f0f" width="64" height="64" rx="12"></rect>
  <text x="12" y="42" text-anchor="middle" font-family="monospace" font-size="28" font-weight="300" fill="#666">[</text>
  <text x="32" y="42" text-anchor="middle" font-family="monospace" font-size="22" font-weight="700" letter-spacing="-1" fill="#3b82f6">TL</text>
  <text x="52" y="42" text-anchor="middle" font-family="monospace" font-size="28" font-weight="300" fill="#666">]</text>
</svg>

What makes this powerful is that:

1. You can create entire families of favicons using typography, Unicode characters, and colors.
2. The favicons are tiny (a few hundred bytes).
3. They're easy to edit and maintain (just edit the SVG text).
