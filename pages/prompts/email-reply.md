---
name: email-reply
description: Use to draft an email reply as me. Fetch the thread with gws, decide whether and how to respond, and write what I'd actually say in my voice, grounded in my recent positions. Skip for searching, reading, or summarizing email, and for net-new outreach written from scratch.
tags: [ai-agents, ai-workflows, agents-md, local-mcp, productivity, writing-style]
---

```markdown
Answer the most recent email from [SENDER]

Draft the reply that I (Anand) would actually send - based mostly on things I said, decided, or did recently, adapted to this audience and situation. (Not a generic polished email that just resembles my writing.)

Guardrails:

- Work independently. Ask me only if a missing fact would change the decision and cannot be recovered from the sources.
- Draft only. NEVER send, label, archive, or modify email.
- Use @LocalMCP, the web, and the coding environment directly.
- For external recipients, don't disclose what's not approved for them.

0. **Read relevant skills**: On Local MCP, find, read, and apply the relevant skills for the task.
   `~/code/scripts/agents/*/SKILL.md` - coding + thinking skills
   `~/code/blog/pages/skills/*/SKILL.md` - thinking skills

1. **Fetch and understand**: Use `gws` on Local MCP. Find the thread by subject + sender, read all of it (format=full, decode base64url bodies). Determine:
   - Have I already replied? Has the request changed? Did someone else answer?
     Is a reply still useful? Default target: the first email's substance, replied to the latest message that still needs something from me.
   - Read attachments that affect the reply (pdf/pptx skills).
     Render slides and pages visually when reviewing a visual artifact; extracted text is not enough.
     Follow Google Drive links that hold the actual material.
   - Identify: the literal questions; what the sender actually needs
     (answer, decision, approval, review, introduction, reassurance, cover); the deadline;
     any implied commitment for me, my org, or others; the useful question they did not ask.
   - Reframe: if required and appropriate, use reframe-question/SKILL.md and answer the intended question.
     Research the sender for better context if required.

2. Choose the response mode:
   Substantive reply / brief ack / decision / introduction or delegation / one clarifying question / discuss live / follow-up / no reply.
   An email draft is not automatically the right output.
   Proportional effort: a confirmation stays simple; advice ends in a small experiment or decision, not a catalogue;
   artifact reviews inspect the artifact and give concrete changes.
   For strategy or broad advice, mention the (ambitious) end-state and the practical next step that leads to it.
   Do not expose research just because you performed it.

3. Retrieve my position: Search in widening rings; stop when new sources no longer change the reply:
   1. The steer.
   2. The thread, attachments, links.
   3. My recent sent mail: same person, same project, similar questions (also my best style anchor - imitate 3-5 replies of the same type).
   4. For project/client work, use gws (Google Drive). Search filenames, then full text; maybe broaden thereafter. Prefer recent files (<90d). Read only most likely authoritative files.
   5. `~/Dropbox/notes/questions-i-am-asked.md` (newest first)
   6. `~/Dropbox/notes/transcripts/YYYY-MM-DD*.md` near the email date or with the sender
   7. `~/code/blog/description.md`, `~/code/til/README.md`, `~/code/talks/README.md` (find the piece, then read it); `~/Dropbox/notes/about/{Sender}.md` if present
   8. The web, only for current external facts (prices, models, dates, roles).

   When sources conflict, prefer the more authoritative and recent, direct, situation-specific one.
   Infer the underlying position; don't copy old wording mechanically.
   My emails and transcripts are evidence of my POSITION, not proof a FACT is true.
   Verify changing facts against primary sources online.

   ALWAYS read and follow the anand-writing-style, anand-objectives, verification-gate skills.
   Use blind-spot, expert-lens, evidence-provenance for strategy or reviews.

4. Draft:
   - "Hi {FirstName}" ... body ... "Regards" or "Thanks" + "Anand", whichever fits.
   - Plain ASCII. No em-dashes, emojis, corporate filler, inflated praise, or polished LLM-style conclusions.
     Tentative where evidence is tentative: "Maybe try X?" Say plainly what I don't know.
   - Prefer the minimal experiment over the survey: one model, one workflow, one next step, plus "If that's not quite what you need, we can discuss alternatives."
   - Minimize my commitments ("I can help review X", "happy to join one call").
     Never invent commitments, owners, timelines, cc additions, links, or facts; if one seems useful, put it under Judgment calls, not in the draft.
   - In reviews, separate: confirmed facts / my recommendation / still to decide.
   - Length: confirmation 40-120 words; advice 80-250 ending in a decision or experiment;
     artifact or technical review 300-700; longer only if the requested content itself requires it.
   - Warmth and humor only where the existing relationship supports it.

5. Verify, then trim:
   Check: every material question answered, including the unasked one?
   Facts and links verified at primary sources? Any invented commitment, owner, or certainty?
   Contradicts anything I said recently? Leaks private context?
   Longer than I would write? Phrases I would not use?
   Compare against recent sent replies to the same person or topic.
   Then cut anything that does not change what the recipient understands or does next.

Output:

Recommendation: REPLY / REPLY BRIEFLY / DISCUSS LIVE / FOLLOW UP / NO REPLY
Status: pending or already replied (with date if replied)
Draft: <ready-to-paste body only>
Why: up to 3 bullets on the decisive choices
Process: bulleted reasoning steps including hypotheses considered, alternatives rejected, why searches widened or narrowed, branches followed or abandoned, why retrieval stopped.
Sources: List meaningful sources and retrieval steps actually used during drafting: `query, command, or action -> findings (citing exact file:line, message id, or URL) -> effect on draft`.
Judgment calls: up to 3 decisions only I can make - your pick, why, alternatives, and why I might differ, what evidence would change the decision.
Gaps: anything unread or unverified, specific knowledge Anand may have that can alter the answer, e.g. undocumented discussions, relationship history, verbal commitments, stale sources, better alternatives, political or operational constraints, etc.
```

- 17 Jul 2026. Created. Sources:
  - https://claude.ai/chat/86b76a7f-2b62-42e5-82c7-a2474c8dd23e
  - https://chatgpt.com/c/6a5975a7-2ca0-83ee-a1b6-a730ec71412b
  - Usage attempt #1: https://chatgpt.com/c/6a5986bf-13d0-83e8-b460-5ecb0360bb84
- 23 Jul 2026. Updated based on Ask AI initiative feedback:
  - https://chatgpt.com/c/6a61b1f7-9580-83e8-a4e1-7e88a16538e1
