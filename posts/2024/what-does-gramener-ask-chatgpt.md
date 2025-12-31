---
title: What does Gramener ask ChatGPT?
date: "2024-01-14T07:23:38Z"
lastmod: "2024-08-27T03:12:49Z"
categories:
  - data
  - experiments
  - llms
wp_id: 3500
---

![What does Gramener ask ChatGPT?](/blog/assets/DALL·E-2024-01-14-12.50.31-A-photo-realistic-image-representing-the-use-of-ChatGPT-in-a-corporate-environment.-The-image-should-include-a-modern-office-setting-with-a-computer-s.webp)

<p>I looked at how <a href="https://gramener.com/">Gramener</a> uses <a href="https://chat.openai.com/">ChatGPT</a> Plus by evaluating 600+ chats asked over 3 months from Oct 2023 to Jan 2024.</p>
<p><strong>The team asks 6 questions a day</strong>. We don't track who or how many actively use ChatGPT Plus. This also excludes personal ChatGPT accounts. Still, 6/day is low for an entire team <em>put together</em>.</p>
<p>The questions fall into 8 categories.</p>
<figure class="wp-block-table"><table><thead><tr><th>Category</th><th>%</th></tr></thead><tbody><tr><td>Excel, data exploration &amp; analysis</td><td>25%</td></tr><tr><td>Text extraction and summarization</td><td>13%</td></tr><tr><td>HTML, CSS, or JavaScript code</td><td>13%</td></tr><tr><td>Python code</td><td>13%</td></tr><tr><td>LLMs, AI and use cases</td><td>9%</td></tr><tr><td>OCR and image analysis</td><td>9%</td></tr><tr><td>Generate images, logos, and designs</td><td>7%</td></tr><tr><td>General knowledge, policy &amp; environment</td><td>5%</td></tr><tr><td>Audio and translation</td><td>5%</td></tr></tbody></table></figure>
<p>Here are some questions from each category - to give you an idea of emergent ChatGPT Plus usage.</p>
<p><strong>Excel, data exploration &amp; analysis (25%)</strong></p>
<ul>
<li><em>Excel clean and merge</em>. There are 2 worksheets in this excel with data, can you clean up the data and merge the data in both the sheets</li>
<li><em>Excel CO2 Data Analysis</em>. You are an expert Data Analyst who is capable of extracting insights out of data. Analyze this sheet and let me know the findings</li>
<li><em>Excel Chi-Square Analysis Guide</em>. how to perform chi square analysis in excel</li>
<li><em>Log Data Insights &amp; KPIs</em>. Looking at the columns from this excel, what kind of insights are possible, what are key KPIs to be looked at</li>
</ul>
<p><strong>Text extraction and summarization (13%)</strong></p>
<ul>
<li><em>Complaint Investigation Summary</em>. The following is the summary of an internal investigation for a customer complaint. Now this internal summary is to be paraphrased (in 3-4 lines) as part of a closure</li>
<li><em>Extracting Tables from RTF</em>. Can you write a script to extract the tables from this document</li>
<li><em>Extracting Entities from Text</em>. <code>[{'word1': '(P)', 'nearest_word1': 'P/N:', 'nearest_word2': '0150-25034', 'nearest_word3': 'CARTIRIDGE'}, {'word1': 'P/N:', 'nearest_word1': '(P)', 'nearest_word2': '015...</code></li>
<li><em>Extract PDF Font Details</em>. Extract text formatting information from this document. Especially find font styles, families and sizes.</li>
</ul>
<p><strong>HTML, CSS, or JavaScript code (13%)</strong></p>
<ul>
<li><em>HTML/CSS Chart Template</em>. Give me HTML, CSS and chart code for this design.</li>
<li><em>CSS Font Stack: Explanation</em>. Explain this CSS font convention: <code>Arial, Helvetica, Segoe UI, sans-serif</code></li>
<li><em>Checkbox Validation with JavaScript</em>. In HTML form, I have a set of checkboxes. How do I write the form so that at least one of them being checked is mandatory?</li>
<li><em>Prevent Text Wrapping CSS</em>. <code>&lt;span class="text"&gt;Chief Communications Officer&lt;/span&gt;</code> I need CSS such the text inside should not wrap create new line</li>
<li><em>ReactJS App with Routing</em>. Give me developed version using ReactJS use react router for sidebar section navigation to the pages use Tailwind css for styling. Use styled components for conditional …</li>
</ul>
<p><strong>Python code (13%)</strong></p>
<ul>
<li><em>Python Code Documentation Guide</em>. Can you generate documentation for a project code written in python?</li>
<li><em>Linux Commands for Python</em>. Give me list of linux commands to work on python coding</li>
<li><em>Code explanation request.</em> What's this code about? …</li>
<li><em>FastAPI Async Testing</em>. Write a fastapi code and a python client to test the asynchronous nature of the fastapi package.</li>
<li><em>Streamlit App for Translation</em>. Given the following python code, give me a simple streamlit app that takes file upload and converts that into a target language: …</li>
</ul>
<p>An interesting sub-topic was interview question generation.</p>
<ul>
<li><em>Python Decorator for Database Queries</em>. Create one medium level question for Decorators in python Industryy usecase specific with solution</li>
</ul>
<p><strong>LLM, AI and use cases (9%)</strong></p>
<ul>
<li><em>LLMs for Data "What Ifs"</em>. You are an LLM Expert. Can you tell me how can we leverage LLM for implementing What IF scenarios on Data?</li>
<li><em>LLMs: Current Challenges &amp; Concerns</em>. what are current challenges with LLMs</li>
<li><em>LLM Applications in Marketing</em>. Show LLM applications for the marketing function of a music company.</li>
<li><em>Gen AI usage</em>. What industries are using Gen AI the most</li>
<li><em>Best LLMs in 2023</em>. Search the internet for the most recent LLMs and list the best LLMs in terms of performance</li>
<li><em>Best Image Classification Models</em>. suggest best models to tell what there in the image</li>
</ul>
<p><strong>OCR and image analysis (9%)</strong></p>
<ul>
<li><em>Browser history OCR</em>. This is a screenshot of my browser history. Convert that to text. Categorize these into common topics.</li>
<li><em>Extracted C Code</em>. This image contains C code. Extract it.</li>
<li><em>Image text extraction and annotation</em>. Extract the text from this image and annotate the boundaries of the text</li>
<li><em>Detecting Document Image Orientation</em>. oreientation detection of documnet image</li>
<li><em>AI Project with OpenCV &amp; YOLO</em>. Consider yourself as Open CV and Yolo expert and help me with AI project</li>
<li><em>Image Correction Techniques</em>. what are the approaches we have in computer vision where my image is tilted or rotated in reverse or image is not in readable format</li>
</ul>
<p><strong>Generate images, logos, and designs (7%)</strong></p>
<ul>
<li><em>Google Chacha and ChatGPT Bhatija</em>. Generate an image of Google Chacha and ChatGPT Bhatija</li>
<li><em>Regenerative Systems Group Image</em>. Generate an Image with below context &gt; "A group of people interested in Regenerative systems. The focus is on reusing food, energy and mental health"</li>
<li><em>Twitter Reply Icons Design</em>. Give me three icons: icon16.png, icon48.png, icon128.png for an extension that I'm building that suggests replies to tweets</li>
<li><em>Generate flowcharts</em>. Make a flowchart of the underlying working of a web app. Here's how it works. 1. The user uploads a document - a PDF or an image. They then select the language that …</li>
<li><em>Create Animated GIF from Photos</em>. I have 4 photos I want to make an animated gif out of them. How can i do that?</li>
<li><em>Climate Impact Illustration</em>. An illustration showcasing the impact of climate change on daily life, focusing on a rural setting near the coast. In the foreground, a small farm is visibly struggling, …</li>
</ul>
<p><strong>General knowledge, policy &amp; environment (5%)</strong></p>
<ul>
<li><em>Design Thinking Overview</em>. What is Design thinking</li>
<li><em>Arthashastra</em>. What can Arthashastra teach us about modern politics?</li>
<li><em>Community Impact on Habits</em>. Is there research to suggest the impact of community on habit building?</li>
<li><em>Focus at Age 28</em>. What should a 28 year old focus on?</li>
<li><em>Superconductors</em>. Explain superconductors like I'm five years old.</li>
<li><em>Climate Career: Impactful Choices</em>. You a career counsellor at a University campus. You want to create 4 to 5 talking points for students to consider a career in Climate space.</li>
<li><em>Sustainability Division Vision</em>. I run a software outsourced product development company. I want to start a new division that focuses on sustainability services offerings. Please draft a vision…</li>
</ul>
<p><strong>Audio and translation (5%)</strong></p>
<ul>
<li><em>Audio Timestamp Mapping</em>. timestamp mapping for transcribed audio</li>
<li><em>Transcribe Lengthy Audio: Segment</em>. Transcribe this audio file.</li>
<li><em>Traducción del MOU al Español</em>. Translate this document to Spanish, and create a new translated document. Maintain text formatting.</li>
<li><em>Telugu Transcription into Hindi</em>. Transcribe the following telugu text into hindi. You are supposed to transcribe, not translate. శ్రీనివాస పూజావిధానము …</li>
<li><em>GPT lacks native audio support</em>. Does gpt support audio in audio out natively?</li>
</ul>
