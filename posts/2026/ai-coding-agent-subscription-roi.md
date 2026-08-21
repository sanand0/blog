---
title: AI Coding Agent Subscription ROI
date: 2026-05-30T23:19:34+08:00
categories:
- llms
- coding
description: I tracked nine months of Claude and Codex coding-agent usage and found my $20 subscriptions delivered roughly $35 and $400 in API value, with Codex much cheaper and more heavily used.
tags: [ai-coding-agents, llm-pricing, enterprise-ai, data-analysis]
---

I ran [`npx -y ccusage monthly --compact`](https://github.com/ryoppippi/ccusage) to get the following break-up of my AI coding agent costs.


| Month   |    Codex |  Claude |
| ------- | -------: | ------: |
| 2025-09 |   $37.47 |   $2.29 |
| 2025-10 |  $106.79 |   $9.13 |
| 2025-11 |  $100.35 |  $14.24 |
| 2025-12 |  $240.69 |  $24.88 |
| 2026-01 |  $100.89 |  $20.28 |
| 2026-02 |  $323.21 |  $29.46 |
| 2026-03 | $1996.32 | $134.87 |
| 2026-04 |  $401.36 |  $47.07 |
| 2026-05 |  $378.20 |  $45.13 |

This shows the ROI of my $20 subscriptions to each. I get ~$35 worth of API calls for my $20 Claude Pro subscription and ~$400 of API calls for my $20 ChatGPT Plus subscription (on top of my ChatGPT chats.)

I end up using Codex a lot more - partly because it's a bit more diligent, but mostly because it's a lot cheaper.

Clearly, subscriptions are good deal for individuals. Codex, especially.

This may not be true for corporates. [Simon Willison](https://simonwillison.net/2026/May/27/product-market-fit/) says that Anthropic and OpenAI both changed _enterprise_ pricing to align with token prices. That means the cost of enterprise AI security is ~2-20 _times_ their token budget - which is growing rapidly.

---

BTW, my moment of [AI psychosis](https://en.wikipedia.org/wiki/Chatbot_psychosis) was in March 2026. The coding agents had increased their limits and I was tokenmaxxing. I'm far from that limit today, but the symptoms linger.

<noscript>

![](https://files.s-anand.net/images/2026-05-30-ai-coding-agent-subscription-roi.avif)

</noscript>

<canvas id="ai-coding-agent-usage"></canvas>

<script>
  (async function () {
    const rows = [
      { month: '2025-09', claude: 2.29, codex: 37.47 },
      { month: '2025-10', claude: 9.13, codex: 106.79 },
      { month: '2025-11', claude: 14.24, codex: 100.35 },
      { month: '2025-12', claude: 24.88, codex: 240.69 },
      { month: '2026-01', claude: 20.28, codex: 100.89 },
      { month: '2026-02', claude: 29.46, codex: 323.21 },
      { month: '2026-03', claude: 134.87, codex: 1996.32 },
      { month: '2026-04', claude: 47.07, codex: 401.36 },
      { month: '2026-05', claude: 45.13, codex: 378.20 }
    ];

    const theme = {
      ink: '#231f20',
      muted: '#6b625c',
      grid: 'rgba(35, 31, 32, 0.11)',
      axis: 'rgba(35, 31, 32, 0.22)',
      claude: '#b96d3a',
      codex: '#2d5f87',
      tooltip: 'rgba(35, 31, 32, 0.94)'
    };

    const canvas = document.getElementById('ai-coding-agent-usage');

    Object.assign(canvas.style, {
      display: 'block',
      width: '100%',
      height: '100%',
      minHeight: '480px'
    });

    function loadChartJs() {
      if (window.Chart) return Promise.resolve();
      return new Promise((resolve, reject) => {
        const script = document.createElement('script');
        script.src = 'https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js';
        script.onload = resolve;
        script.onerror = reject;
        document.head.appendChild(script);
      });
    }

    await loadChartJs();

    const usd = new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
      maximumFractionDigits: 2
    });

    const compactUsd = new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
      notation: 'compact',
      maximumFractionDigits: 1
    });

    Chart.defaults.font.family = document.body.style.fontFamily;
    Chart.defaults.color = theme.muted;

    new Chart(canvas, {
      type: 'line',
      data: {
        labels: rows.map(d => d.month),
        datasets: [
          {
            label: 'Claude',
            data: rows.map(d => d.claude),
            borderColor: theme.claude,
            backgroundColor: theme.claude,
            pointBackgroundColor: '#ffffff',
            pointBorderColor: theme.claude,
            pointBorderWidth: 2.5,
            pointRadius: 4,
            pointHoverRadius: 7,
            borderWidth: 3,
            tension: 0.22
          },
          {
            label: 'Codex',
            data: rows.map(d => d.codex),
            borderColor: theme.codex,
            backgroundColor: theme.codex,
            pointBackgroundColor: '#ffffff',
            pointBorderColor: theme.codex,
            pointBorderWidth: 2.5,
            pointRadius: 4,
            pointHoverRadius: 7,
            borderWidth: 3,
            tension: 0.22
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        interaction: { mode: 'index', intersect: false },
        layout: { padding: { top: 12, right: 18, bottom: 4, left: 8 } },
        plugins: {
          legend: {
            position: 'bottom',
            labels: {
              usePointStyle: true,
              pointStyle: 'circle',
              boxWidth: 8,
              boxHeight: 8,
              padding: 22,
              color: theme.muted,
              font: { size: 13, weight: '650' }
            }
          },
          tooltip: {
            enabled: true,
            mode: 'index',
            intersect: false,
            backgroundColor: theme.tooltip,
            bodyFont: { size: 13, weight: '650' },
            padding: 13,
            displayColors: true,
            callbacks: {
              title: items => items[0].label,
              label: item => `${item.dataset.label}: ${usd.format(item.parsed.y)}`,
              afterBody: items => {
                const i = items[0].dataIndex;
                const total = rows[i].claude + rows[i].codex;
                return `Combined: ${usd.format(total)}`;
              }
            }
          }
        },
        scales: {
          x: {
            grid: { color: 'rgba(35,31,32,0.07)', drawTicks: false },
            border: { color: theme.axis },
            ticks: { maxRotation: 0, autoSkip: false, color: theme.muted, font: { size: 12 } }
          },
          y: {
            beginAtZero: true,
            suggestedMax: 2200,
            grid: { color: theme.grid },
            border: { display: false },
            ticks: {
              padding: 8,
              color: theme.muted,
              callback: value => value >= 1000 ? compactUsd.format(value) : '$' + value
            },
            title: {
              display: true,
              text: 'Cost (USD)',
              color: theme.muted,
              font: { size: 12, weight: '650' }
            }
          }
        }
      }
    });
  })();
</script>

---

**14 Jun 2026**: [SemiAnalysis](https://x.com/SemiAnalysis_/status/2064815044085318040) tested and found that a $20 Claude Pro gives you ~$400 and a $100 Claude Max gives you ~$2,000 of API usage. For ChatGPT, the numbers are ~$700 and $3,500.
