---
title: Wage Rates of Nations and LLMs
date: "2025-05-24T07:47:01Z"
lastmod: "2025-05-24T07:51:22Z"
categories:
  - llms
  - visualisation
wp_id: 4129
---

![Wage Rates of Nations and LLMs](/blog/assets/image-8.webp)

<p>How much does an LLM charge per hour for its services?</p>
<p>If we multiple the <strong>Cost Per Output Token</strong> with <strong>Tokens Per Second</strong>, we can get the cost for what an LLM produces in <strong>Dollars Per Hour</strong>. (We're ignoring the input cost, but it's not the main driver of time.)</p>
<p>Over time, different models have been released at different billing rates. Most new powerful models like O3 or Gemini 2.5 Pro cost ~$7 - $11 per hr. </p>

<div class="video-embed"><iframe src="https://www.youtube.com/embed/LGlJmbTxiYs" title="YouTube video" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

![bar-chart-race visualization](https://public.flourish.studio/visualisation/23384855/thumbnail)

<p>To get a sense of this, let's look at wage rates across countries and industries:</p>
<figure class="wp-block-table"><table class="has-fixed-layout"><thead><tr><th>Rate ($/hr)</th><th>Countries (avg hourly wage)</th><th>Models</th></tr></thead><tbody><tr><td>0–2</td><td>Bangladesh ($1.42/hr), Pakistan ($1.65/hr), Vietnam ($0.94/hr)</td><td>devstral-small ($0.01/hr), gemini-2.5-flash-preview ($1.50/hr)</td></tr><tr><td>2–5</td><td>Brazil ($3.09/hr), Mexico manufacturing ($4.90/hr)</td><td>claude-sonnet-4 ($2.23/hr), codex-mini ($2.54/hr)</td></tr><tr><td>5–10</td><td>India ($5.03/hr), South Africa avg ($9.38/hr), Poland min wage ($7.35/hr)</td><td>o3 ($7.16/hr), claude-opus-4 ($8.67/hr)</td></tr><tr><td>10–15</td><td>Germany ($12.93/hr), France ($12.41/hr), UK ($14.43/hr)</td><td>gemini-2.5-pro-preview ($11.89/hr), gpt-4.5-preview ($13.10/hr)</td></tr><tr><td>15–20</td><td>Spain ($15.87/hr), Italy ($16.80/hr), Japan ($17.98/hr)</td><td><em>No recent models in this range</em></td></tr></tbody></table></figure>
<p>Workers in Europe and Japan are already more expensive than the more expensive models, at $12+ per hour. India, Brazil, Mexico etc. are more expensive than most of the average models.</p>
<p>Once a language model’s run-time cost drops below the local minimum wage, the “offshoring” advantage disappears. <em>AI becomes the cheapest employee in every country at once.</em> Countries whose economies depend on being the "cheaper alternative" for labor-intensive work face potential economic disruption.</p>
<p>Paradoxically, workers in countries with strong labor protections, unions, and higher wages (like Germany and France) may paradoxically be safer from AI displacement.</p>
<p><strong>Source code</strong>: <a href="https://github.com/sanand0/llmpricing/blob/9b66480458b712de52ea14502a64bf4c3b6a98ed/billing.py">sanand0/llmpricing</a><br/><strong>Analysis</strong>: <a href="https://chatgpt.com/share/68317a06-0cac-800c-ad6f-13646ceb489f">ChatGPT</a></p>
<p></p>

---

## Comments

<!-- wp-comments-start -->

- **[Soumendra Kumar Sahoo](http://www.soumendrak.com)** _24 May 2025 1:44 pm_:
  The white collar workers jobs are in danger compared to blue collar ones.

<!-- wp-comments-end -->
