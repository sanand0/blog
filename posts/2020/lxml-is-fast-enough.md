---
title: lxml is fast enough
date: "2020-12-11T03:12:34Z"
lastmod: "2021-01-23T04:11:17Z"
categories:
  - coding
wp_id: 2971
excerpt: Python is still fast enough for HTML parsing.
---

Given the blazing speed of [Node.js](https://nodejs.org/) these days, I expected HTML parsing to be faster on Node than on Python.

So I compared [lxml](https://lxml.de/) with [htmlparser2](https://github.com/fb55/htmlparser2) -- the fastest libraries on Python and JS in parsing the [reddit](https://www.reddit.com/) home page (~700KB).

- lxml took ~8.6 milliseconds
- htmlparser2 took ~14.5 milliseconds

Looks like lxml is much faster. I'm likely to stick around with Python for pure HTML parsing (without JavaScript) for a while longer.

```python
In [1]: from lxml.html import parse

In [2]: %timeit tree = parse('reddit.html')
8.69 ms ± 190 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
```

```javascript
const { Parser } = require("htmlparser2");
const { DomHandler } = require("domhandler");
const fs = require("fs");
const html = fs.readFileSync("reddit.html");
const handler = new DomHandler(function(error, dom) {});

const start = +new Date();
for (var i = 0; i < 100; i++) {
  const parser = new Parser();
  parser.write(html);
  parser.end();
}
const end = +new Date();
console.log((end - start) / 100);
```

**Note**: If I run the htmlparser2 code 100 times instead of 10, it only takes 7ms per loop. The more the number of loops, the faster it parses. I guess Node.js optimizes repeated loops. But I'm only interested in the first iteration, since I'll be parsing files only once.
