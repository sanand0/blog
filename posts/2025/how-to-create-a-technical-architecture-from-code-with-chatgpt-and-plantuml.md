---
title: How to create a Technical Architecture from code with ChatGPT and PlantUML
date: "2025-05-24T03:47:56Z"
lastmod: "2025-05-24T03:47:58Z"
categories:
  - coding
  - llms
wp_id: 4126
---

![How to create a Technical Architecture from code with ChatGPT and PlantUML](/blog/assets/image-7.webp)

[Earlier](/blog/how-to-create-a-technical-architecture-from-code-with-chatgpt/), I used [Mermaid](https://www.mermaidchart.com/) for technical architectures. But [PlantUML](https://plantuml.com/) seems a better option for cloud architecture diagrams.

**STEP 1: Copy the code**

Here’s a one-liner using [files-to-prompt](https://github.com/simonw/files-to-prompt) to copy all files in the current directory:

```bash
fd | xargs uvx files-to-prompt --cxml | xclip -selection clipboard
```

Or, you can specify individual files:

```bash
uvx files-to-prompt --cxml README.md ... | xclip -selection clipboard
```

**STEP 2: Extract the cloud icons**

This script pulls icon macros for AWS, Azure, and GCP from [PlantUML's Standard Library](https://plantuml.com/stdlib) into prompt-friendly files.

```bash
echo "' AWS icon macros. They all accept (e_alias, e_label, e_techn). Prefer including AWSPuml/[CATEGORY]/all.puml" > AWS.puml
echo '!define AWSPuml https://raw.githubusercontent.com/awslabs/aws-icons-for-plantuml/refs/heads/main/dist' >> AWS.puml
curl https://raw.githubusercontent.com/awslabs/aws-icons-for-plantuml/refs/heads/main/AWSSymbols.md \
  | grep -Po '\b[\w./-]+\.puml\b' \
  | sed 's/^/!includeurl AWSPuml\//' \
  >> AWS.puml

echo "' Azure icon macros. They all accept (e_alias, e_label, e_techn). Prefer including AzurePuml/[CATEGORY]/all.puml. Always include AzurePuml/AzureCommon.puml
" > Azure.puml
echo '!define AzurePuml https://raw.githubusercontent.com/plantuml-stdlib/Azure-PlantUML/master/dist' >> Azure.puml
curl https://raw.githubusercontent.com/plantuml-stdlib/Azure-PlantUML/refs/heads/master/AzureSymbols.md \
  | grep -Po '\b[\w./-]+\.puml\b' \
  | grep -v 'AzurePuml/' \
  | sed 's/^/!includeurl AzurePuml\//' \
  >> Azure.puml

echo "' GCP icon macros. They all accept (e_alias, e_label, e_techn). Prefer including GCPPuml/[CATEGORY]/all.puml. Always include GCPPuml/GCPCommon.puml
" > GCP.puml
echo '!define GCPPuml https://raw.githubusercontent.com/Crashedmind/PlantUML-icons-GCP/refs/heads/master/dist' >> GCP.puml
curl https://raw.githubusercontent.com/Crashedmind/PlantUML-icons-GCP/refs/heads/master/Symbols.md \
  | grep -Po '\b[\w./-]+\.puml\b' \
  | sed 's/^/!includeurl GCPPuml\//' \
  >> GCP.puml
```

**STEP 3: Prompt for a PlantUML diagram**

[PlantUML](https://plantuml.com/) is a diagram markup language. I use this prompt with [O4-Mini-High](https://chatgpt.com/?model=o4-mini-high) or [O3](https://chatgpt.com/?model=o3):

> Create a PlantUML component diagram to describe the technical architecture using the files below.\
> For EVERY cloud component use the icon macro ONLY from the provided list.

Then paste your copied code and the `.puml` for your cloud (e.g. `Azure.puml`).

Here is a [sample conversation](https://chatgpt.com/share/68312df6-a134-800c-9a9c-80d39b41ffcc) and the [PlantUML output](https://editor.plantuml.com/uml/ZLBDRjiy4BphAJO-10aGMy1tpE53dBW_1kpKhPBsM53asc93KGftcTHz-YvDAq6DnkXDMixC3cTuHQm2nzOL9mRNrYDCVyM0Avb0mzpJPLa6zJpPM6vY7Gc3xZoZvudksh9toYVocDWuMvSxxdYLflVBHTagOWobiSJ5YVNQHOCnkDSLcN3JjMtd9xqCte1zmteFdTqUmrNS1RN1ZBrsNRqV7EF8zZxodlC-Uitsk9dfVAbqOpqkK0Ll_MQunSPRjazOONYo6kcOnaongXKXPMxrw8R9FyLGoMRT78FE3NgslCtugKx6PZQWba2sr__TP6wXqZ_S4mPG1B4e3fCxm--r_5t0g6B5LiEK29b6huDdhCaoGjCHInYZys9eIhZQU47k1Y2JHFiWSih1_Xb1UXp1rZ6bFd275aHWBPz9OJM7QwKVq9kaSTiPdFmWE8NLbflEGuYUROia2dylGwGwPL-yVEhHJ-T9Qh5OWlLh3EWr2lsm3o7IenFW4baP6S9mCdfHgpulCdDe9f5s7m99S4A6V998B-RsCzblyASelD6LgAd8IMjNr5I-KxbQfOnUNKnd862HAIACn__3BdsuX8ztTwkpwXm2FaOafY8VP4WgLp1VK4f0SKIvrBLrI8DGRY6XtbLtaAhGoZc2izYxJfaB4DsmlO1cstTYZP3EYymvNA9C-Hmi8sGc6Z0v7VgJ85K9VkwVkWU4r93ksjvXkky1KheHP7giM8RX4krGrIcGRh1L1voSkYn8kPSxzuEHFU5WYugSy5-Liu8J-wa75dDYvmgzYQtx3G00).
