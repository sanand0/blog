---
title: WhatsApp Group
date: "2025-10-12T05:32:39Z"
lastmod: "2025-11-10T08:00:37Z"
classes: wrap-code
---

<!--
Source: https://chatgpt.com/c/68d8c76f-b550-8328-93f1-b1bc03a2c243
Chats:
  VizChitra Community Update: https://chatgpt.com/c/68eb6fec-0cd0-8320-9cd9-769b25bc6bfb
  Chem96 WhatsApp message analysis: https://chatgpt.com/c/68d8d4c4-e78c-8320-a53e-b3c306de5b7a
  IIMB 2001 WhatsApp messages: https://chatgpt.com/c/68d8ccb1-6c8c-8327-9dde-99470c065aff
  WhatsApp message analysis: https://chatgpt.com/c/68d8c76f-b550-8328-93f1-b1bc03a2c243
  WhatsApp Data Insights: https://chatgpt.com/c/685b7c97-0cfc-800c-9e15-8e0bab4cbaf1
  Missing Values in WhatsApp Data: https://chatgpt.com/c/685d468b-3ea8-800c-9b1b-2ab1765cf972
-->

Summarize a WhatsApp thread from https://tools.s-anand.net/whatsappscraper/ | whatsappthread.jq

```markdown
Analyze the attached WhatsApp messages and share your results by writing ONLY these 3 sections:

- **Topics**. For each of the 20 most active topics, write a paragraph mentioning:
  - Start date (e.g. 13 Sep 2025)
  - Who discussed what
  - Quote where relevant
- **Network**. Build a conversation graph of people exploring centrality, bridges, and topic-seeding scores. Summarize key insights as a paragraph each.
- **People**. For each of the 20 most active people, write in a paragraph about any of the below that you can infer with confidence:
  - persona
  - topics/interests
  - roles in network
  - notable habits (e.g. active times - converting to guessed local time, style of writing, etc.)
  - blindspots (things they might not be aware of that or missed others mention or hint at, based on the actual conversations - not just metrics)

Write in active voice, simple words, and conversational style for an 8th grader. Bold **people** and **key phrases** to help scanning.

Attachment has WhatsApp messages as NDJSON with fields: .id, .chat_id, .ts, .type, .author.{name,phone}, .text_raw, .reply_to.{author,phone,text}, .reply_to_id, .thread_id, .urls[]

Context: ...
```
