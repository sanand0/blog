---
title: Create SVG with PowerPoint
date: "2020-12-21T16:24:00Z"
lastmod: "2020-12-21T04:30:07Z"
categories:
  - coding
  - tools
wp_id: 2980
excerpt: With the new SVG support, PowerPoint is perhaps the most accessible SVG authoring
  tool.
---

<p>With Office 365, <a href="https://support.microsoft.com/en-us/office/edit-svg-images-in-microsoft-office-365-69f29d39-194a-4072-8c35-dbe5e7ea528c">PowerPoint supports SVG editing</a>. This is really powerful. It means you can draw in PowerPoint and render it on the web -- including as interactive or animated visuals.</p>
<p>For example, the SVG in this <a href="https://gramener.com/processmonitor/simulator">simulator</a> was created just with PowerPoint.</p>

<a href="https://gramener.com/processmonitor/simulator">![](/blog/assets/proxy.gif)</a>

<p>The process is simple. Draw anything. Select any shapes and right-click. Select Save As Picture... and choose SVG.</p>

![](/blog/assets/image-6.webp)

<p>For example, you can use PowerPoint to create Smart Art, export it as SVG, and embed it into a page. See this example on <a href="https://codepen.io/sanand0/pen/poEwYYy">CodePen</a>.</p>
<iframe allowfullscreen="true" allowtransparency="true" frameborder="no" height="480" loading="lazy" scrolling="no" src="https://codepen.io/sanand0/embed/poEwYYy?height=480&amp;theme-id=light&amp;default-tab=result" style="width: 100%;" title="Smart Art SVG">
  See the Pen <a href="https://codepen.io/sanand0/pen/poEwYYy">Smart Art SVG</a> by S Anand
  (<a href="https://codepen.io/sanand0">@sanand0</a>) on <a href="https://codepen.io">CodePen</a>.
</iframe>
<p>The SVG is fairly well structured and easy to edit. The code generated for these 2 simple shapes:</p>

![](/blog/assets/image-png-8.webp)

<p>... is quite straight-forward -- just two SVG shapes.</p>

```svg
<rect x="125.5" y="185.5" width="107" height="107" stroke="#2F528F" stroke-width="1.33333" stroke-miterlimit="8" fill="#4472C4"/>
<path d="M243.5 292.5 297 185.5 350.5 292.5Z" stroke="#2F528F" stroke-width="1.33333" stroke-miterlimit="8" fill="#4472C4" fill-rule="evenodd"/>
```

<p>I was worried about the lack of SVG authoring tools in Windows. (InkScape is not usable, and Adobe's tools are complex and expensive.) PowerPoint fits perfectly.</p>

<div class="video-embed"><iframe src="https://www.youtube.com/embed/5ndouHSYGxA" title="YouTube video" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>
