---
title: Agent Skills Usage
date: 2026-04-13T16:16:41-07:00
categories:
- llms
description: I measured how often Claude, Codex, and Copilot sessions use my coding-agent skills. Code dominates at 51.5%, while Claude favors data stories, Codex favors data analysis, and Codex reads the most skills.
tags: [data-analysis, ai-coding-agents]
---

I have a bunch of [coding agent skills](https://github.com/sanand0/scripts/tree/main/agents) I've accumulated over the last few months. Here's how often my sessions use them:

<table>
  <thead>
    <tr>
      <th scope="col" style="text-align: left;">Skill</th>
      <th scope="col" style="text-align: left;">Claude</th>
      <th scope="col" style="text-align: left;">Codex</th>
      <th scope="col" style="text-align: left;">Copilot</th>
      <th scope="col" style="text-align: left;">Overall</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: left;"><a href="https://github.com/sanand0/scripts/tree/main/agents/code/SKILL.md" target="_blank">code</td>
      <td style="text-align: right; background-color: rgb(229, 240, 249); color: rgb(0, 0, 0);">6.1%</td>
      <td style="text-align: right; background-color: rgb(8, 48, 107); color: rgb(255, 255, 255);">69.1%</td>
      <td style="text-align: right; background-color: rgb(94, 164, 208); color: rgb(255, 255, 255);">37.5%</td>
      <td style="text-align: right; background-color: rgb(35, 114, 180); color: rgb(255, 255, 255);">51.5%</td>
    </tr>
    <tr>
      <td style="text-align: left;"><a href="https://github.com/sanand0/scripts/tree/main/agents/data-story/SKILL.md" target="_blank">data-story</td>
      <td style="text-align: right; background-color: rgb(45, 125, 187); color: rgb(255, 255, 255);">48.7%</td>
      <td style="text-align: right; background-color: rgb(198, 220, 239); color: rgb(0, 0, 0);">16.4%</td>
      <td style="text-align: right; background-color: rgb(94, 164, 208); color: rgb(255, 255, 255);">37.5%</td>
      <td style="text-align: right; background-color: rgb(145, 194, 223); color: rgb(255, 255, 255);">28.0%</td>
    </tr>
    <tr>
      <td style="text-align: left;"><a href="https://github.com/sanand0/scripts/tree/main/agents/data-analysis/SKILL.md" target="_blank">data-analysis</td>
      <td style="text-align: right; background-color: rgb(239, 246, 253); color: rgb(0, 0, 0);">2.6%</td>
      <td style="text-align: right; background-color: rgb(105, 172, 212); color: rgb(255, 255, 255);">35.2%</td>
      <td style="text-align: right; background-color: rgb(225, 237, 248); color: rgb(0, 0, 0);">7.8%</td>
      <td style="text-align: right; background-color: rgb(176, 210, 232); color: rgb(0, 0, 0);">21.8%</td>
    </tr>
    <tr>
      <td style="text-align: left;"><a href="https://github.com/sanand0/scripts/tree/main/agents/design/SKILL.md" target="_blank">design</td>
      <td style="text-align: right; background-color: rgb(158, 201, 226); color: rgb(0, 0, 0);">25.5%</td>
      <td style="text-align: right; background-color: rgb(168, 206, 229); color: rgb(0, 0, 0);">23.6%</td>
      <td style="text-align: right; background-color: rgb(206, 225, 242); color: rgb(0, 0, 0);">14.1%</td>
      <td style="text-align: right; background-color: rgb(176, 210, 232); color: rgb(0, 0, 0);">21.8%</td>
    </tr>
    <tr>
      <td style="text-align: left;"><a href="https://github.com/sanand0/scripts/tree/main/agents/plan/SKILL.md" target="_blank">plan</td>
      <td style="text-align: right; background-color: rgb(223, 235, 247); color: rgb(0, 0, 0);">8.5%</td>
      <td style="text-align: right; background-color: rgb(213, 229, 244); color: rgb(0, 0, 0);">11.8%</td>
      <td style="text-align: right; background-color: rgb(206, 225, 242); color: rgb(0, 0, 0);">14.1%</td>
      <td style="text-align: right; background-color: rgb(213, 229, 244); color: rgb(0, 0, 0);">11.8%</td>
    </tr>
    <tr>
      <td style="text-align: left;"><a href="https://github.com/sanand0/scripts/tree/main/agents/agent-friendly-cli/SKILL.md" target="_blank">agent-friendly-cli</td>
      <td style="text-align: right; background-color: rgb(236, 244, 252); color: rgb(0, 0, 0);">3.7%</td>
      <td style="text-align: right; background-color: rgb(207, 225, 242); color: rgb(0, 0, 0);">13.8%</td>
      <td style="text-align: right; background-color: rgb(215, 230, 245); color: rgb(0, 0, 0);">11.1%</td>
      <td style="text-align: right; background-color: rgb(215, 230, 245); color: rgb(0, 0, 0);">11.2%</td>
    </tr>
    <tr>
      <td style="text-align: left;"><a href="https://github.com/sanand0/scripts/tree/main/agents/devtools/SKILL.md" target="_blank">devtools</td>
      <td style="text-align: right; background-color: rgb(183, 213, 234); color: rgb(0, 0, 0);">20.4%</td>
      <td style="text-align: right; background-color: rgb(226, 237, 248); color: rgb(0, 0, 0);">7.3%</td>
      <td style="text-align: right; background-color: rgb(220, 234, 246); color: rgb(0, 0, 0);">9.4%</td>
      <td style="text-align: right; background-color: rgb(218, 232, 246); color: rgb(0, 0, 0);">10.0%</td>
    </tr>
    <tr>
      <td style="text-align: left;"><a href="https://github.com/sanand0/scripts/tree/main/agents/llm/SKILL.md" target="_blank">llm</td>
      <td style="text-align: right; background-color: rgb(240, 246, 253); color: rgb(0, 0, 0);">2.5%</td>
      <td style="text-align: right; background-color: rgb(222, 235, 247); color: rgb(0, 0, 0);">8.7%</td>
      <td style="text-align: right; background-color: rgb(225, 237, 248); color: rgb(0, 0, 0);">7.8%</td>
      <td style="text-align: right; background-color: rgb(226, 237, 248); color: rgb(0, 0, 0);">7.4%</td>
    </tr>
    <tr>
      <td style="text-align: left;"><a href="https://github.com/sanand0/scripts/tree/main/agents/pdf/SKILL.md" target="_blank">pdf</td>
      <td style="text-align: right; background-color: rgb(247, 251, 255); color: rgb(0, 0, 0);">0.0%</td>
      <td style="text-align: right; background-color: rgb(224, 236, 248); color: rgb(0, 0, 0);">7.9%</td>
      <td style="text-align: right; background-color: rgb(225, 237, 248); color: rgb(0, 0, 0);">7.8%</td>
      <td style="text-align: right; background-color: rgb(228, 239, 249); color: rgb(0, 0, 0);">6.6%</td>
    </tr>
    <tr>
      <td style="text-align: left;"><a href="https://github.com/sanand0/scripts/tree/main/agents/linkedin-cdp/SKILL.md" target="_blank">linkedin-cdp</td>
      <td style="text-align: right; background-color: rgb(206, 224, 241); color: rgb(0, 0, 0);">14.3%</td>
      <td style="text-align: right; background-color: rgb(247, 251, 255); color: rgb(0, 0, 0);">0.0%</td>
      <td style="text-align: right; background-color: rgb(231, 241, 250); color: rgb(0, 0, 0);">5.6%</td>
      <td style="text-align: right; background-color: rgb(232, 241, 250); color: rgb(0, 0, 0);">5.3%</td>
    </tr>
    <tr>
      <td style="text-align: left;"><a href="https://github.com/sanand0/scripts/tree/main/agents/uv-uvx/SKILL.md" target="_blank">uv-uvx</td>
      <td style="text-align: right; background-color: rgb(247, 251, 255); color: rgb(0, 0, 0);">0.0%</td>
      <td style="text-align: right; background-color: rgb(220, 233, 246); color: rgb(0, 0, 0);">9.5%</td>
      <td style="text-align: right; background-color: rgb(247, 251, 255); color: rgb(0, 0, 0);">0.0%</td>
      <td style="text-align: right; background-color: rgb(233, 242, 250); color: rgb(0, 0, 0);">4.9%</td>
    </tr>
    <tr>
      <td style="text-align: left;"><a href="https://github.com/sanand0/scripts/tree/main/agents/interactive-storytelling/SKILL.md" target="_blank">interactive-storytelling</td>
      <td style="text-align: right; background-color: rgb(227, 238, 248); color: rgb(0, 0, 0);">7.1%</td>
      <td style="text-align: right; background-color: rgb(239, 246, 252); color: rgb(0, 0, 0);">2.7%</td>
      <td style="text-align: right; background-color: rgb(227, 238, 248); color: rgb(0, 0, 0);">7.1%</td>
      <td style="text-align: right; background-color: rgb(234, 242, 251); color: rgb(0, 0, 0);">4.6%</td>
    </tr>
    <tr>
      <td style="text-align: left;"><a href="https://github.com/sanand0/scripts/tree/main/agents/demos/SKILL.md" target="_blank">demos</td>
      <td style="text-align: right; background-color: rgb(223, 235, 247); color: rgb(0, 0, 0);">8.5%</td>
      <td style="text-align: right; background-color: rgb(239, 246, 252); color: rgb(0, 0, 0);">2.8%</td>
      <td style="text-align: right; background-color: rgb(242, 248, 254); color: rgb(0, 0, 0);">1.6%</td>
      <td style="text-align: right; background-color: rgb(237, 245, 252); color: rgb(0, 0, 0);">3.5%</td>
    </tr>
    <tr>
      <td style="text-align: left;"><a href="https://github.com/sanand0/scripts/tree/main/agents/cloudflare/SKILL.md" target="_blank">cloudflare</td>
      <td style="text-align: right; background-color: rgb(247, 251, 255); color: rgb(0, 0, 0);">0.0%</td>
      <td style="text-align: right; background-color: rgb(235, 243, 251); color: rgb(0, 0, 0);">4.3%</td>
      <td style="text-align: right; background-color: rgb(238, 245, 252); color: rgb(0, 0, 0);">3.1%</td>
      <td style="text-align: right; background-color: rgb(237, 245, 252); color: rgb(0, 0, 0);">3.3%</td>
    </tr>
    <tr>
      <td style="text-align: left;"><a href="https://github.com/sanand0/scripts/tree/main/agents/melt-mlt/SKILL.md" target="_blank">melt-mlt</td>
      <td style="text-align: right; background-color: rgb(247, 251, 255); color: rgb(0, 0, 0);">0.0%</td>
      <td style="text-align: right; background-color: rgb(240, 246, 253); color: rgb(0, 0, 0);">2.5%</td>
      <td style="text-align: right; background-color: rgb(242, 248, 254); color: rgb(0, 0, 0);">1.6%</td>
      <td style="text-align: right; background-color: rgb(242, 248, 253); color: rgb(0, 0, 0);">1.8%</td>
    </tr>
    <tr>
      <td style="text-align: left;"><a href="https://github.com/sanand0/scripts/tree/main/agents/vector-art/SKILL.md" target="_blank">vector-art</td>
      <td style="text-align: right; background-color: rgb(240, 246, 253); color: rgb(0, 0, 0);">2.5%</td>
      <td style="text-align: right; background-color: rgb(240, 247, 253); color: rgb(0, 0, 0);">2.4%</td>
      <td style="text-align: right; background-color: rgb(247, 251, 255); color: rgb(0, 0, 0);">0.0%</td>
      <td style="text-align: right; background-color: rgb(242, 248, 253); color: rgb(0, 0, 0);">1.7%</td>
    </tr>
    <tr>
      <td style="text-align: left;"><a href="https://github.com/sanand0/scripts/tree/main/agents/vitest-dom/SKILL.md" target="_blank">vitest-dom</td>
      <td style="text-align: right; background-color: rgb(247, 251, 255); color: rgb(0, 0, 0);">0.0%</td>
      <td style="text-align: right; background-color: rgb(241, 247, 253); color: rgb(0, 0, 0);">2.2%</td>
      <td style="text-align: right; background-color: rgb(247, 251, 255); color: rgb(0, 0, 0);">0.0%</td>
      <td style="text-align: right; background-color: rgb(243, 248, 254); color: rgb(0, 0, 0);">1.4%</td>
    </tr>
    <tr>
      <td style="text-align: left;"><a href="https://github.com/sanand0/scripts/tree/main/agents/memorable-explanations/SKILL.md" target="_blank">memorable-explanations</td>
      <td style="text-align: right; background-color: rgb(239, 246, 253); color: rgb(0, 0, 0);">2.6%</td>
      <td style="text-align: right; background-color: rgb(242, 248, 254); color: rgb(0, 0, 0);">1.6%</td>
      <td style="text-align: right; background-color: rgb(247, 251, 255); color: rgb(0, 0, 0);">0.0%</td>
      <td style="text-align: right; background-color: rgb(243, 249, 254); color: rgb(0, 0, 0);">1.3%</td>
    </tr>
    <tr>
      <td style="text-align: left;"><a href="https://github.com/sanand0/scripts/tree/main/agents/npm-packages/SKILL.md" target="_blank">npm-packages</td>
      <td style="text-align: right; background-color: rgb(247, 251, 255); color: rgb(0, 0, 0);">0.0%</td>
      <td style="text-align: right; background-color: rgb(245, 250, 254); color: rgb(0, 0, 0);">0.6%</td>
      <td style="text-align: right; background-color: rgb(247, 251, 255); color: rgb(0, 0, 0);">0.0%</td>
      <td style="text-align: right; background-color: rgb(246, 250, 255); color: rgb(0, 0, 0);">0.3%</td>
    </tr>
  </tbody>
</table>

Here are my observations, with surprises highlighted as ⁉️

- [`code`](https://github.com/sanand0/scripts/tree/main/agents/code/SKILL.md) is the most used skill, by far. About half the sessions use it.
  - But Claude doesn't use it much⁉️
- The [`data-story`](https://github.com/sanand0/scripts/tree/main/agents/data-story/SKILL.md) and [`data-analysis`](https://github.com/sanand0/scripts/tree/main/agents/data-analysis/SKILL.md) skills were the most rapidly adopted.
  - I use Claude (with Claude Code _and_ Copilot) a lot more for data stories. I use Codex for data analysis.
  - Therefore the [`webapp-testing`](https://github.com/sanand0/scripts/tree/main/agents/webapp-testing/SKILL.md) and [`devtools`](https://github.com/sanand0/scripts/tree/main/agents/devtools/SKILL.md) skilss are used less by Codex.
- The [`design`](https://github.com/sanand0/scripts/tree/main/agents/design/SKILL.md) skill is used consistently across agents. It was inspired by Claude's design skill - but I don't think it is particularly good, and needs revision.
- [`agent-friendly-cli`](https://github.com/sanand0/scripts/tree/main/agents/agent-friendly-cli/SKILL.md) tool development is mostly with Codex, followed by Copilot, and very little with Claude.
- Most [`pdf`](https://github.com/sanand0/scripts/tree/main/agents/pdf/SKILL.md) sessions are with Copilot / Codex, not Claude⁉️
- Codex reads most skills diligengly.
  - It is the only one diligently reading my [`uv-uvx`](https://github.com/sanand0/scripts/tree/main/agents/uv-uvx/SKILL.md) skill, even though every agent uses it⁉️
  - In fact, it is the only agent to have read every skill except [`linkedin-cdp`](https://github.com/sanand0/scripts/tree/main/agents/linkedin-cdp/SKILL.md) (it never needed it.)
