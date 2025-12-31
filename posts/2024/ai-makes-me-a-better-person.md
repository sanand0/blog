---
title: AI makes me a better person
date: "2024-03-21T04:23:00Z"
lastmod: "2024-08-27T03:12:49Z"
categories:
  - experiments
  - how-i-do-things
  - llms
wp_id: 3518
---

![AI makes me a better person](/blog/assets/f7f0a283-2446-4d5f-8875-46d694e3f7e6-1.webp)

<p>Every time I get annoyed at people, I remind myself to be more like ChatGPT. Specifically:</p>
<ol>
<li>Don't get annoyed. Be patient.</li>
<li>Encourage them.</li>
<li>Step back and show them the big picture.</li>
</ol>
<p>(Then I get annoyed at myself for getting annoyed.)</p>
<p>Today, I analyzed how exactly ChatGPT is different from me. So, I took a pitch document I co-authored with ChatGPT.</p>
<h2 class="wp-block-heading">Section A: Authored by Anand</h2>
<blockquote class="wp-block-quote">
<p><strong>WHAT DO WE NEED?</strong></p>
<p>We are looking for API access to (SYSTEM) via the REST API as an Agent role (read/respond to emails). Specifically, access via a bearer token.</p>
<p>This would be accessed by a single application developed by a team of 3 developers and 1 business analyst. None of them have access to (SYSTEM) today.</p>
<p><strong>WHY DO WE NEED THIS, AND WHY SO SOON?</strong></p>
<p>We need this to classify emails automatically, as they arrive, into categories such as “non-value-add” (e.g. Thank you, Out-of-office, etc.)</p>
<p>We’d line access today, please. Currently, we are processing XX,XXX non-value-add emails per month. Each day of delay leads to a processing waste of ~XX emails per day. At current volumes, this will save ~$XX,XXX per annum.</p>
<p><strong>IS THERE ANY OTHER WAY?</strong></p>
<p>To access emails in real-time, this is the only option. (We’re ruling out web scraping.)</p>
<p>(SYSTEM) rule-based closure won’t work. It’s based on keyword search, not semantic matches. For example, “Thank you” is present in non-value-add emails as well as follow-up questions. Multi-lingual matches are a challenge. So, though (SYSTEM) currently closes emails with rules, 1 out of 6 emails that are NOT closed already are non-value-add.</p>
<p>This cannot be done via (SYSTEM) or any other BI system because it involves accessing the data in real-time as well as responding via (SYSTEM). This needs to be steady-state access, not one-time, since we want to classify emails real-time.</p>
<p><strong>HOW LONG WILL IT TAKE?</strong></p>
<p>Based on our past experience, this would take about X weeks to prototype, X weeks to develop, and X weeks to test. We should have the application deployed in X months.</p>
</blockquote>
<h2 class="wp-block-heading">Section B: Authored by ChatGPT</h2>
<blockquote class="wp-block-quote">
<p><strong>WHAT’S THE IMPACT IF WE DON’T MOVE FORWARD?</strong></p>
<p>Quantitatively, continuing without this solution wastes resources on XXX non-essential emails daily, costing $XX,XXX yearly. Delays in customer responses will ensue.</p>
<p>Qualitatively, lack of automation strains customer service, risking employee burnout and diminished customer experience.</p>
<p><strong>WHAT’S THE PRIORITY (MOSCOW)?</strong></p>
<p>(SYSTEM) API access via REST as an Agent role with a bearer token is a “MUST HAVE”. Alternative methods like scraping (SYSTEM) are impractical due to high effort and maintenance.</p>
<p><strong>WHAT’S THE OUTCOME IF WE MOVE FORWARD?</strong></p>
<p>Financially, securing API access saves $XX,XXX annually by cutting manual email sorting. Efficiency gains reduce operational costs and free resources for strategic tasks.</p>
<p>Strategically, automating email classification boosts customer satisfaction and response times, establishing leadership in service innovation. Long-term, it enables data-driven insights into customer behaviour, improving decisions and customer service scalability.</p>
</blockquote>
<h2 class="wp-block-heading">Analysis</h2>
<p>I fed these to ChatGPT and asked: "<em>You are an English professor evaluating an essay. Compare the writing styles of the 2 sections. They're written by different authors. List the major differences in writing style.</em>"</p>
<p>Here's what it said (roughly):</p>
<figure class="wp-block-table"><table><thead><tr><th>Area</th><th>Anand</th><th>ChatGPT</th></tr></thead><tbody><tr><td>Structure</td><td>Direct, concise, with specifics</td><td>Broader perspective and implications</td></tr><tr><td>Focus</td><td>Detailing the process</td><td>Benefits and consequences</td></tr><tr><td>Detailing</td><td>Specific, providing clear picture</td><td>General, providing implications</td></tr><tr><td>Tone</td><td>Conveys urgency</td><td>Reflective rather than urgent</td></tr><tr><td>Approach</td><td>Problem-solving oriented</td><td>Outcome-oriented</td></tr></tbody></table></figure>
<p>Yeah, that's definitely me on the left.</p>
<p>I like the direct, concise, specific part. I plan to add the "broader perspective", "implications", and "outcome-orientation" to my life.</p>
<h2 class="wp-block-heading">Postscript</h2>
<p><a href="https://www.linkedin.com/in/jaidevd/">Jaidev</a> pointed out that this is confirmation bias. He asked ChatGPT for the <a href="https://chat.openai.com/share/a21b235e-9149-4ce7-bca7-180ddc8d06b7"><em>similarities</em> in the writings</a>. It said both are clear, direct, structured, specific, quantitative, and strategic. So, if you ask for differences, you'll get them, even if they're marginal.</p>
<p>I now need to learn (and write about) framing questions well!</p>
