---
title: My first LAMBDA in Excel
date: "2023-05-06T04:53:37Z"
categories:
  - excel-tips
wp_id: 3432
---

![My first LAMBDA in Excel](/blog/assets/image-75.webp)

<p>Ever since Excel introduced the LAMBDA function, I've been itching to use it in real life. I got my first chance today.</p>
<p>We track the skill index of our different teams (consulting, analytics, technology, etc.) like this:</p>
<figure class="wp-block-table"><table><thead><tr><th>Team</th><th class="has-text-align-right" data-align="right">Skill Index</th><th class="has-text-align-right" data-align="right">Apr-23</th><th class="has-text-align-right" data-align="right">May-23</th><th class="has-text-align-right" data-align="right">Jun-23</th><th class="has-text-align-right" data-align="right">Jul-23</th></tr></thead><tbody><tr><td>Consulting</td><td class="has-text-align-right" data-align="right">0%</td><td class="has-text-align-right" data-align="right">0%</td><td class="has-text-align-right" data-align="right"></td><td class="has-text-align-right" data-align="right"></td><td class="has-text-align-right" data-align="right"></td></tr><tr><td>Analytics</td><td class="has-text-align-right" data-align="right">33%</td><td class="has-text-align-right" data-align="right">33%</td><td class="has-text-align-right" data-align="right"></td><td class="has-text-align-right" data-align="right"></td><td class="has-text-align-right" data-align="right"></td></tr><tr><td>Technology</td><td class="has-text-align-right" data-align="right">72%</td><td class="has-text-align-right" data-align="right">72%</td><td class="has-text-align-right" data-align="right"></td><td class="has-text-align-right" data-align="right"></td><td class="has-text-align-right" data-align="right"></td></tr><tr><td>etc.</td><td class="has-text-align-right" data-align="right"></td><td class="has-text-align-right" data-align="right"></td><td class="has-text-align-right" data-align="right"></td><td class="has-text-align-right" data-align="right"></td><td class="has-text-align-right" data-align="right"></td></tr></tbody></table></figure>
<p>The "Skill Index" column should pick the LAST value. If Apr-23 is filled, use that. But if May-23 is also filled, use that.</p>
<p>I needed something like a <code>=LASTVALUE(range)</code> formula. But none exists.</p>
<p>A good alternative is <a href="https://exceljet.net/formulas/get-value-of-last-non-empty-cell">this formula to get the last non-empty cell</a>:</p>

```excel
=LOOKUP(2,1/(range<>""),range)
```

<p>So, I followed the <a href="https://support.microsoft.com/en-us/office/lambda-function-bd212d27-1cd1-4321-a34a-ccbf254b8b67">instructions</a> to create a function in the Name Manager (Ctrl+F3)</p>

![](/blog/assets/image-75.webp)

<p> ... and simply fill in <code>=LASTVALUE(H6:S6)</code> and the like in the "Skills Index" cell.</p>
<p>The LOOKUP formula is confusing. My aim is to confuse our team less. But I wonder if they'll start Google-ing for this LASTVALUE formula no one ever heard of, and get more confused 🤔.</p>
