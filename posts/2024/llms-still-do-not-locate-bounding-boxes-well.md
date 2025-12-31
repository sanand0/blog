---
title: LLMs still do not locate bounding boxes well
date: "2024-11-01T16:20:03Z"
lastmod: "2024-11-02T00:32:28Z"
categories:
  - llms
wp_id: 3682
---

<p>I sent an image to over a dozen LLMs that support vision, asking them:</p>
<blockquote class="wp-block-quote">
<p>Detect objects in this 1280x720 px image and return their color and bounding boxes in pixels. Respond as a JSON object: {[label]: [color, x1, y1, x2, y2], …}</p>
</blockquote>
<p>None of the models did a good-enough job. It looks like we have some time to go before LLMs become good at bounding boxes.</p>
<p>I've given them a subjective rating on a 1-5 scale below. </p>
<figure class="wp-block-table"><table class="has-fixed-layout"><thead><tr><th>Model</th><th>Positions</th><th>Sizes</th></tr></thead><tbody><tr><td>gemini-1.5-flash-001</td><td>🟢🟢🟢🔴🔴</td><td>🟢🟢🟢🟢🔴</td></tr><tr><td>gemini-1.5-flash-8b</td><td>🟢🟢🟢🔴🔴</td><td>🟢🟢🟢🔴🔴</td></tr><tr><td>gemini-1.5-flash-002</td><td>🟢🟢🔴🔴🔴</td><td>🟢🟢🟢🔴🔴</td></tr><tr><td>gemini-1.5-pro-002</td><td>🟢🟢🟢🔴🔴</td><td>🟢🟢🟢🟢🔴</td></tr><tr><td>gpt-4o-mini</td><td>🟢🔴🔴🔴🔴</td><td>🟢🟢🔴🔴🔴</td></tr><tr><td>gpt-4o</td><td>🟢🟢🟢🟢🔴</td><td>🟢🟢🟢🟢🔴</td></tr><tr><td>chatgpt-4o-latest</td><td>🟢🟢🟢🟢🔴</td><td>🟢🟢🟢🟢🔴</td></tr><tr><td>claude-3-haiku-20240307</td><td>🟢🔴🔴🔴🔴</td><td>🟢🟢🔴🔴🔴</td></tr><tr><td>claude-3=5-sonnet-20241022</td><td>🟢🟢🟢🔴🔴</td><td>🟢🟢🟢🔴🔴</td></tr><tr><td>llama-3.2-11b-vision-preview</td><td>🔴🔴🔴🔴🔴</td><td>🔴🔴🔴🔴🔴</td></tr><tr><td>llama-3.2-90b-vision-preview</td><td>🟢🟢🟢🔴🔴</td><td>🟢🟢🟢🔴🔴</td></tr><tr><td>qwen-2-vl-72b-instruct</td><td>🟢🟢🟢🔴🔴</td><td>🟢🟢🔴🔴🔴</td></tr><tr><td>pixtral-12b</td><td>🟢🟢🔴🔴🔴</td><td>🟢🟢🟢🔴🔴</td></tr></tbody></table></figure>
<p>I used an <a href="https://tools.s-anand.net/llmboundingbox/">app I built for this</a>.</p>
<p>Here is the original image along with the individual results.</p>

![](/blog/assets/shapes-1024x576.webp)

![](/blog/assets/gemini-1.5-flash-8b-1024x576.webp)

![](/blog/assets/gemini-1.5-flash-001-1024x576.webp)

![](/blog/assets/gemini-1.5-flash-002-1024x576.webp)

![](/blog/assets/gemini-1.5-pro-002-1024x576.webp)

![](/blog/assets/gpt-4o-mini-1024x576.webp)

![](/blog/assets/gpt-4o-1024x576.webp)

![](/blog/assets/chatgpt-4o-latest-1024x576.webp)

![](/blog/assets/claude-3-haiku-20240307-1024x576.webp)

![](/blog/assets/claude-3-5-sonnet-20241022-1024x576.webp)

![](/blog/assets/llama-3.2-11b-vision-preview-1024x576.webp)

![](/blog/assets/llama-3.2-90b-vision-preview-1024x576.webp)

![](/blog/assets/pixtral-12b-1024x576.webp)

![](/blog/assets/qwen-2-vl-72b-instruct-1024x576.webp)

<h4 class="wp-block-heading">Update</h4>
<p>Adding gridlines with labeled axes helps the LLMs. (Thanks <a href="https://www.linkedin.com/feed/update/urn:li:ugcPost:7258152478255243264?commentUrn=urn%3Ali%3Acomment%3A%28ugcPost%3A7258152478255243264%2C7258184350876262402%29&amp;dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287258184350876262402%2Curn%3Ali%3AugcPost%3A7258152478255243264%29">@Bijan Mishra</a>.) Here are a few examples:</p>

![](/blog/assets/chatgpt-4o-latest-1-1024x576.webp)

![](/blog/assets/gemini-1.5-flash-002-1-1024x576.webp)

![](/blog/assets/claude-3-5-sonnet-20241022-1-1024x576.webp)
