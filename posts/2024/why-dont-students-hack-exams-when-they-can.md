---
title: Why don't students hack exams when they can?
date: "2024-11-22T10:38:09Z"
lastmod: "2024-11-22T10:38:11Z"
categories:
  - education
wp_id: 3725
---

![Why don't students hack exams when they can?](/blog/assets/calvin-tries-to-cheat-an-exam.webp)

<p>This year, I created a series of tests for <a href="https://study.iitm.ac.in/ds/course_pages/BSSE2002.html">my course at IITM</a> and to recruit for <a href="https://gramener.com/">Gramener</a>. </p>
<p>The tests had 2 interesting features.</p>
<h3 class="wp-block-heading"><strong>One question required them to hack the page</strong></h3>
<blockquote class="wp-block-quote">
<p>Write the body of the request to an <a href="https://platform.openai.com/docs/api-reference/chat">OpenAI chat completion call</a> that:</p>
<ul class="wp-block-list">
<li>Uses model <code>gpt-4o-mini</code></li>
<li>Has a <code>system</code> message: <code>Respond in JSON</code></li>
<li>Has a user message: <code>Generate 10 random addresses in the US</code></li>
<li>Uses <a href="https://platform.openai.com/docs/guides/structured-outputs/">structured outputs</a> to respond with an object <code>addresses</code> which is an array of objects with <strong>required</strong> fields: <code>street</code> (string) <code>city</code> (string) <code>apartment</code> (string) .</li>
<li>Sets <code>additionalProperties</code> to <code>false</code> to prevent additional properties.</li>
</ul>
<p>What is the JSON body we should send to <code>https://api.openai.com/v1/chat/completions</code> for this? (No need to run it or to use an API key. Just write the body of the request below.)</p>
<p><strong>There's no answer box above. Figure out how to enable it. That's part of the test.</strong></p>
</blockquote>
<p>The only way to even <em>attempt</em> this question is to inspect the page, find the hidden input and make it visible. (This requires removing a class, an attribute, and a style - from different places.)</p>
<p>Here's the number of people who managed to enable the text box and answer it.</p>
<figure class="wp-block-table"><table class="has-fixed-layout"><thead><tr><th class="has-text-align-left" data-align="left">College</th><th class="has-text-align-right" data-align="right"># students</th><th class="has-text-align-right" data-align="right">Enabled</th><th class="has-text-align-right" data-align="right">Answered</th></tr></thead><tbody><tr><td class="has-text-align-left" data-align="left">NIT Bhopal</td><td class="has-text-align-right" data-align="right">144</td><td class="has-text-align-right" data-align="right">4 (2.8%)</td><td class="has-text-align-right" data-align="right">0 (0.0%)</td></tr><tr><td class="has-text-align-left" data-align="left">CBIT</td><td class="has-text-align-right" data-align="right">277</td><td class="has-text-align-right" data-align="right">16 (5.8%)</td><td class="has-text-align-right" data-align="right">0 (0.0%)</td></tr><tr><td class="has-text-align-left" data-align="left">IIT Madras</td><td class="has-text-align-right" data-align="right">693</td><td class="has-text-align-right" data-align="right">74 (10.7%)</td><td class="has-text-align-right" data-align="right">4 (0.6%)</td></tr></tbody></table></figure>
<p>A few things surprised me.</p>
<p>First, I think <strong>students don't inspect HTML</strong>. Less than 10% of students managed to modify the HTML page, <em>even after being told they need to</em>. <strong>But they know web programming</strong>. 49 students at CBIT scored full marks on the rest of the questions, which includes CSS selectors and complex JS code. Maybe editing in a browser instead of an editor is a big mental leap?</p>
<p>Second, almost <strong>no one could solve this problem</strong>. There are 3 ways to easily solve it.</p>
<ol class="wp-block-list">
<li>Copy the question and relevant test cases from my exam page's JavaScript into ChatGPT and ask for an answer. (I test it and it works.)</li>
<li>Copy the question and <a href="https://platform.openai.com/docs/guides/structured-outputs">structured output documentation</a> to ChatGPT and ask for an answer. (I tested it and it works.)</li>
<li>Create a random JSON and just keep fixing the errors manually until it passes. (The exam gives detailed error messages like "The system message must be 'Respond in JSON'", "addresses items must be an object", etc.)</li>
</ol>
<p>Maybe questions from a curriculum are easier to solve than questions not in a curriculum? Or is JSON schema too hard?</p>
<h3 class="wp-block-heading">The exam was officially hackable</h3>
<p>All validation was on the client side. The JS code was minified and answers are dynamically generated. But a student can set a breakpoint, see the answers, and modify their responses.</p>
<p>The students at NIT Bhopal and CBIT were not explicitly told that. The students at IITM were <em>explicitly told</em> that they could (and are welcome to) hack it.</p>
<p>Out of the 1,114 students who took these tests, <strong>only one student actually hacked it</strong>.</p>
<p>(How do I know that? No other student got full marks. This student got full marks with empty answers.)</p>
<p><strong>It's probably not that difficult</strong>. My <a href="https://github.com/sanand0/tools-in-data-science-public/blob/4f42624aadf58aca21b46d3a4b6e856c2ae85adf/2-data-sourcing.md#scraping-the-imdb-with-browser-javascript">course content</a> covers scraping pages using JavaScript using DevTools. Inspecting JS is just a step away.</p>
<p>I did chat with the student who hacked it, asking:</p>
<blockquote class="wp-block-quote">
<p><strong>Anand</strong>: How come you didn't share the details of the hack with others?</p>
<p><strong>Student</strong>: I did with a few but I am not sure whether or not they were able to figure it out still.<br/>Most students in the program still require a lot of handholding even with basic things.<br/>Experience from being a TA [Teaching Assistant] past term.</p>
</blockquote>
<h3 class="wp-block-heading">Why didn't they hack?</h3>
<p>Maybe...</p>
<ol class="wp-block-list">
<li><strong>They don't believe me</strong>. What if hacking the exam page is considered cheating, even if explicitly allowed?</li>
<li><strong>The time pressure is too much</strong>. They'd rather solve what they know than risk wasting time hacking.</li>
<li><strong>It feels wrong</strong>. They'd rather answer based on their knowledge than take a shortcut.</li>
<li><strong>They don't know how</strong>. Using DevTools is more sophisticated than web programming.</li>
</ol>
<p>Issue #1 - the trust issue - is solveable. We can issue multiple official notices.</p>
<p>Issue #4 - capability - is not worth solving. My aim is to get students to do stuff they weren't taught.</p>
<p>Issue #2 &amp; #3 - <strong>a risk-taking culture</strong> - is what I want to encourage. It might teach them to blur ethical lines and neglect fundamentals (which are bad), but it might also build adaptability, creativity, and prepare them for real-world scenarios.</p>
<p>Personally, I need more team members that get the job done even if they've never done it before.</p>
