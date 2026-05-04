---
title: Patterns for Short Code
date: 2025-11-26T00:00:00+05:30
categories:
  - coding
description: I used Claude Code to refactor my Unicoder tool, extracting thirteen principles for elegant, concise code. Key takeaways include replacing conditionals with data-driven structures, utilizing optional chaining, and using pattern arrays to eliminate repetitive logic.
keywords: [javascript, refactoring, claude code, data-driven design, dry principle, clean code]
---

I had [Claude Code](https://claude.ai/code/session_01V4vK6jAMmXqKzwz9dys8zw) create a [PR](https://github.com/sanand0/tools/pull/91) to update my [Unicoder tool](https://tools.s-anand.net/unicoder/). As part of that, I prompted it to repeatedly:

> Shorten the code by exploring opportunities to rewrite more elegantly.

Finally, I asked it:

> You applied several changes to refactor the code for elegance and brevity.
>
> What were the principles you applied? List them all with examples. The objective is to teach me how to shorten and simplify code elegantly.

Its response was a good tutorial on refactoring to shorten and simplify code.

---

Excellent question! Here are the key refactoring principles I applied, with concrete examples from the code:

## 1. Data-Driven Design Over Repetitive Conditionals

Replace repetitive if/else chains with data structures.

**Before (30 lines):**

```javascript
const toAscii = (char) => {
  const code = char.codePointAt(0);

  if (code >= 0x1d5d4 && code <= 0x1d5ed) return String.fromCharCode(code - UNICODE_OFFSETS.BOLD_UPPER);
  if (code >= 0x1d5ee && code <= 0x1d607) return String.fromCharCode(code - UNICODE_OFFSETS.BOLD_LOWER);
  if (code >= 0x1d608 && code <= 0x1d621) return String.fromCharCode(code - UNICODE_OFFSETS.ITALIC_UPPER);
  // ... 4 more similar checks
  return char;
};

const detectStyle = (char) => {
  const code = char.codePointAt(0);
  if ((code >= 0x1d5d4 && code <= 0x1d5ed) || (code >= 0x1d5ee && code <= 0x1d607)) return "bold";
  // ... 2 more similar checks
  return null;
};
```

**After (15 lines):**

```javascript
const CHAR_RANGES = [
  { start: 0x1d5d4, end: 0x1d5ed, offset: UNICODE_OFFSETS.BOLD_UPPER, style: "bold" },
  { start: 0x1d5ee, end: 0x1d607, offset: UNICODE_OFFSETS.BOLD_LOWER, style: "bold" },
  // ... all ranges in one place
];

const toAscii = (char) => {
  const code = char.codePointAt(0);
  const range = CHAR_RANGES.find((r) => code >= r.start && code <= r.end);
  return range ? String.fromCharCode(code - range.offset) : char;
};

const detectStyle = (char) => {
  const code = char.codePointAt(0);
  const range = CHAR_RANGES.find((r) => code >= r.start && code <= r.end);
  return range?.style ?? null;
};
```

**Principle:** Define data once, process it generically. Both functions now share the same data.

---

## 2. Optional Chaining & Nullish Coalescing

Use modern JavaScript operators for cleaner null handling.

**Before:**

```javascript
const formatSegment = (text, style) => {
  if (!style) return text;
  switch (style) {
    case "bold": return `**${text}**`;
    case "italic": return `*${text}*`;
    case "mono": return `\`${text}\``;
    default: return text;
  }
};
```

**After:**

```javascript
const formatSegment = (text, style) => {
  if (!style) return text;
  const formatters = { bold: (t) => `**${t}**`, italic: (t) => `*${t}*`, mono: (t) => `\`${t}\`` };
  return formatters[style]?.(text) ?? text;
};
```

**Principle:** `?.` safely accesses properties, `??` provides defaults. Object lookup replaces switch.

---

## 3. Pattern Arrays for Iterative Operations

Use data structures to eliminate repetitive code.

**Before:**

```javascript
const mergeStyledSegments = (markdown) => {
  markdown = markdown.replace(/\*\*([^*]+)\*\* \*\*([^*]+)\*\*/g, "**$1 $2**");
  markdown = markdown.replace(/\*([^*]+)\* \*([^*]+)\*/g, "*$1 $2*");
  markdown = markdown.replace(/`([^`]+)` `([^`]+)`/g, "`$1 $2`");

  const original = markdown;
  markdown = markdown.replace(/\*\*([^*]+)\*\* \*\*([^*]+)\*\*/g, "**$1 $2**");
  markdown = markdown.replace(/\*([^*]+)\* \*([^*]+)\*/g, "*$1 $2*");
  markdown = markdown.replace(/`([^`]+)` `([^`]+)`/g, "`$1 $2`");

  return markdown !== original ? mergeStyledSegments(markdown) : markdown;
};
```

**After:**

```javascript
const mergeStyledSegments = (markdown) => {
  const patterns = [
    [/\*\*([^*]+)\*\* \*\*([^*]+)\*\*/g, "**$1 $2**"],
    [/\*([^*]+)\* \*([^*]+)\*/g, "*$1 $2*"],
    [/`([^`]+)` `([^`]+)`/g, "`$1 $2`"],
  ];

  let prev;
  do {
    prev = markdown;
    patterns.forEach(([pattern, replacement]) => markdown = markdown.replace(pattern, replacement));
  } while (markdown !== prev);

  return markdown;
};
```

**Principle:** DRY—define patterns once, iterate over them. Easier to add new patterns.

---

## 4. Destructuring for Clarity

Extract only what you need from objects.

**Before:**

```javascript
const copyToClipboard = (text, button) => {
  const originalHTML = button.innerHTML;
  const originalClasses = [...button.classList];

  button.textContent = "Copied!";
  button.classList.remove("btn-light");
  button.classList.add("btn-success");

  setTimeout(() => {
    button.innerHTML = originalHTML;
    button.className = "";
    originalClasses.forEach((cls) => button.classList.add(cls));
  }, 2000);
};
```

**After:**

```javascript
const copyToClipboard = (text, button) => {
  const { innerHTML, className } = button;

  button.textContent = "Copied!";
  button.className = button.className.replace("btn-light", "btn-success");

  setTimeout(() => {
    button.innerHTML = innerHTML;
    button.className = className;
  }, 2000);
};
```

**Principle:** Destructure to extract values. Use `className` string instead of classList manipulation.

---

## 5. Arrow Functions with Implicit Returns

Eliminate unnecessary syntax for single-expression functions.

**Before:**

```javascript
const handleCopy = (outputId, buttonId) => () => {
  copyToClipboard(document.getElementById(outputId).innerText, document.getElementById(buttonId));
};
```

**After:**

```javascript
const handleCopy = (outputId, buttonId) => () =>
  copyToClipboard(document.getElementById(outputId).innerText, document.getElementById(buttonId));
```

**Principle:** Single-expression functions don't need braces or `return`. One line when clear.

---

## 6. Combine Related Functions

Merge functions that serve similar purposes.

**Before:**

```javascript
const showError = (message) => {
  const errorContainer = document.getElementById("error-container");
  errorContainer.textContent = `Error: ${message}`;
  errorContainer.classList.remove("d-none");
};

const hideError = () => {
  document.getElementById("error-container").classList.add("d-none");
};
```

**After:**

```javascript
const setError = (message = null) => {
  const el = document.getElementById("error-container");
  if (message) {
    el.textContent = `Error: ${message}`;
    el.classList.remove("d-none");
  } else {
    el.classList.add("d-none");
  }
};
```

**Principle:** One function with optional parameter beats two separate functions. `setError()` hides, `setError(msg)` shows.

---

## 7. Object Literal Shorthand

Use computed expressions in object literals.

**Before:**

```javascript
const convertCodeBlock = (text) => {
  const converted = [...text].map((c) => (detectStyle(c) === "mono" ? toAscii(c) : c)).join("");
  return { markdown: "```\n" + converted + "\n```" };
};
```

**After:**

```javascript
const convertCodeBlock = (text) => ({
  markdown: "```\n" + [...text].map((c) => (detectStyle(c) === "mono" ? toAscii(c) : c)).join("") + "\n```",
});
```

**Principle:** Eliminate intermediate variables when computation is clear. Use `({...})` for implicit object return.

---

## 8. Remove Dead Code

Delete unused functions ruthlessly.

**Removed:**

```javascript
const fromUnicodeStyle = (text) => {
  return text.split("").map((char) => toAscii(char)).join("");
};
```

**Principle:** If it's only exported for tests but unused in production, remove it. YAGNI (You Aren't Gonna Need It).

---

## 9. Inline Single-Use Helpers

Don't create helpers for operations done once or twice.

**Before (separate helper):**

```javascript
const renderOutput = (outputId, content) => {
  const output = document.getElementById(outputId);
  output.replaceChildren();
  output.insertAdjacentHTML("beforeend", `<div class="m-0" style="white-space: pre-wrap; word-break: break-word;">${content}</div>`);
};

const updateMarkdownOutput = () => {
  hideError();
  renderOutput("unicode-output", convertMarkdownToUnicode(document.getElementById("markdown-input").value));
};
```

**After (kept helper but simplified):**

```javascript
const renderOutput = (id, content) => {
  const el = document.getElementById(id);
  el.replaceChildren();
  el.insertAdjacentHTML("beforeend", `<div class="m-0" style="white-space: pre-wrap; word-break: break-word;">${content}</div>`);
};
```

**Principle:** Kept the helper (reused 2x), but shortened variable names (`outputId`→`id`, `output`→`el`).

---

## 10. Single-Line Simple Functions

When a function is trivial, make it one line.

**Before:**

```javascript
const convertBulletsToLists = (markdown) => {
  return markdown.replace(/^• /gm, "- ");
};
```

**After:**

```javascript
const convertBulletsToLists = (markdown) => markdown.replace(/^• /gm, "- ");
```

**Principle:** Trivial transforms don't need braces or explicit returns.

---

## 11. Early Returns Over Nested Conditions

Fail fast to reduce indentation.

**Example (already applied):**

```javascript
const copyToClipboard = (text, button) => {
  if (!text.trim()) return setError("Nothing to copy");
  // ... rest of logic
};
```

**Principle:** Guard clauses at the top reduce nesting and cognitive load.

---

## 12. Spread Operator for String Iteration

Use `[...str]` instead of `str.split("")` for Unicode safety.

**Example:**

```javascript
// Handles surrogate pairs correctly
[...text].map((c) => detectStyle(c) === "mono" ? toAscii(c) : c)
```

**Principle:** `[...]` respects code points; `split("")` splits surrogate pairs incorrectly.

---

## 13. Concise Module Exports

**Before:**

```javascript
module.exports = {
  convertMarkdownToUnicode,
  convertUnicodeToMarkdown,
  toBold,
  toItalic,
  toMonospace,
  toAscii,
  detectStyle,
  fromUnicodeStyle,
};
```

**After:**

```javascript
module.exports = { convertMarkdownToUnicode, convertUnicodeToMarkdown, toBold, toItalic, toMonospace, toAscii, detectStyle };
```

**Principle:** One line when it fits. Remove unused exports.

---

## **Summary: Core Principles**

1. **Data over code**. Use structures, not conditionals
2. **DRY**. Never repeat the same logic
3. **Modern JS features**. Use `?.`, `??`, destructuring, spread
4. **YAGNI**. Remove unused code immediately
5. **Single expression**. Eliminate intermediate variables when clear
6. **Implicit returns**. Arrow functions with `=>` not `=> { return }`
7. **Early returns**. Guard clauses reduce nesting
8. **Shorter names**. When scope is small (`output` → `el`)
9. **One concern**. Each function does one thing well
10. **Readability first**. Terse is good; cryptic is bad

**Result:** 144 lines shorter, more maintainable, same functionality! 🎯
