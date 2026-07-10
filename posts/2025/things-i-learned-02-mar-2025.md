---
title: Things I Learned - 02 Mar 2025
date: 2025-03-02T00:00:00+00:00
categories:
  - til
description: I explored Podman for local databases and studied how AI replaces professional research reports. I also tested real-time Whisper transcription tools, discovered DuckDB SQL shortcuts, and learned the weird history behind Roman urine taxes.
tags: [duckdb, whisper, prompt-engineering, python]
---

This week, I learned:

- [Proxmox Virtual Environment](https://www.proxmox.com/en/products/proxmox-virtual-environment/overview) is an open-source alternative to VMWare, Hyper-V, Citrix XenServer, etc. (There's nothing there that prompts me to explore it further.)
- With Podman on Windows (a Docker equivalent), many Docker-enabled tasks become easier. For example, running PostgreSQL is as easy as:
  ```sh
  podman run -d --name postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 postgres:latest
  podman exec -it postgres psql -U postgres -c "CREATE DATABASE mydb;"
  ```
- Bad deep research prompts are: vague/broad, under-specified or ambiguous. In short, the more you know what you want, the better. Iterate until then.
- What kind of reports do clients are research companies to produce? I was curious to see if Deep Research can replace these. Here are a bunch of ideas. [ChatGPT](https://chatgpt.com/share/67bf7946-c80c-800c-8132-6f4018455a68)
  1. Strategy & Management Consulting Research (McKinsey & Company, Boston Consulting Group, Bain & Company, Strategy&, Accenture Strategy)
     - Produce a comprehensive strategic transformation report for a Fortune 500 consumer goods company. Analyze global market trends, competitor strategies, and actionable growth recommendations, including case studies and source citations.
     - Generate an in‐depth study on corporate restructuring trends in emerging markets. Focus on successful turnaround strategies, CEO leadership factors, and strategic pivots, with a comparative analysis of key players.
     - Create a report on M&A trends in the technology sector over the past five years. Detail deal drivers, integration best practices, and forecast future acquisition opportunities, citing relevant data.
  2. IT & Technology Research Analysts (Gartner, Forrester Research, IDC, 451 Research, Ovum)
     - Produce a market assessment report on emerging cloud computing platforms. Include vendor evaluations, adoption forecasts, and key technology drivers with supporting data and charts.
     - Generate an in‐depth cybersecurity trends report for enterprise IT. Analyze recent threat vectors, defense strategies, and best practices for risk mitigation, providing actionable recommendations.
     - Create a comprehensive study on the impact of artificial intelligence in enterprise software. Include competitive benchmarking, technology adoption rates, and forecasted market changes.
  3. Marketing & Consumer Research (Nielsen, Kantar Group, Ipsos, GfK, Euromonitor International)
     - Produce a consumer behavior analysis report for a leading retail brand. Identify key demographic shifts, purchasing trends, and brand loyalty factors, and provide actionable insights with data visualizations.
     - Generate a detailed report on digital media consumption trends among millennials, incorporating survey results, social media analytics, and case studies of successful campaigns.
     - Create a market segmentation report for a new consumer electronics launch. Identify key consumer segments, behavioral drivers, and media usage patterns with clear recommendations.
  4. Financial Investment Research (Goldman Sachs, JPMorgan Chase, Morgan Stanley, Morningstar, Keefe Bruyette & Woods)
     - Produce an equity research report on mid-cap technology stocks. Include detailed financial modeling, valuation analysis, and buy/sell/hold recommendations with supporting data and charts.
     - Generate a fixed income analysis report for corporate bonds in the industrial sector. Assess credit risk, yield forecasts, and macroeconomic influences, citing key data sources.
     - Create a comprehensive report on global market trends impacting investment banking. Analyze regulatory changes, market sentiment, and performance metrics of leading financial institutions.
  5. Healthcare Research (IQVIA, Frost & Sullivan, Evaluate Ltd, Deloitte Healthcare, IMS Health)
     - Produce a market analysis report on emerging biotechnologies in oncology. Include competitive landscape, regulatory challenges, and growth forecasts with relevant case studies.
     - Generate a comprehensive report on patient satisfaction and telemedicine adoption trends. Analyze survey data from leading healthcare providers and benchmark best practices.
     - Create a detailed study on pharmaceutical market dynamics in emerging economies. Focus on pipeline developments, regulatory environments, and market potential with actionable insights.
  6. Legal Research Providers (LexisNexis, Westlaw, Bloomberg Law, Fastcase)
     - Produce a legal risk assessment report on the impact of recent data privacy regulations for multinational corporations. Include case studies, trend analysis (2019–2024), and strategic recommendations.
     - Generate a comprehensive report summarizing key federal and Supreme Court rulings on intellectual property rights over the past five years, highlighting trends and divergent interpretations.
     - Create a detailed report on the evolution of securities law and its effect on investment research practices, incorporating analysis of recent litigation and regulatory updates.
  7. Media & News Research (Factiva, Kantar Media, Comscore, Cision)
     - Produce a media consumption trends report that analyzes audience behavior shifts across digital, TV, and print platforms. Include data visualizations, key drivers, and forecasted trends.
     - Generate a comprehensive report on the impact of social media on traditional news reporting, with case studies and a comparative analysis of engagement metrics.
     - Create a detailed study on the effectiveness of multimedia advertising campaigns, evaluating ROI, consumer engagement, and best practices with actionable insights.
  8. Economic & Industry-Specific Research (Economist Intelligence Unit, BMI Research, IHS Markit, Consensus Economics)
     - Produce a macroeconomic outlook report for emerging markets, including GDP, inflation, and employment forecasts, with detailed data analysis and visualizations.
     - Generate an industry analysis report on the automotive sector, covering technological innovations, competitive dynamics, and consolidation trends.
     - Create a comprehensive country risk assessment report for a target region, detailing political, economic, and regulatory factors with recommendations for investors.
  9. Human Resources & Employee Engagement Research (Gallup, Great Place to Work, Mercer)
     - Produce an employee engagement report for a multinational firm based on recent survey data. Identify key drivers of satisfaction, retention challenges, and improvement recommendations.
     - Generate a comprehensive study on the impact of remote and hybrid work models on employee productivity across industries, including best practices and benchmark data.
     - Create a detailed report on workplace culture transformation, analyzing organizational behavior trends, employee feedback, and actionable strategies to boost engagement.
  10. Environmental, Social & Governance (ESG) Research (MSCI ESG Research, Sustainalytics, ISS ESG, Bloomberg ESG)
      - Produce an ESG performance report for a portfolio of global companies. Include sustainability scores, risk assessments, and recommendations for improvement with data visualizations.
      - Generate a comprehensive study on the impact of climate change regulations on the energy sector, including policy analysis, market forecasts, and strategic implications.
      - Create a detailed report on corporate social responsibility trends in the consumer goods industry, incorporating qualitative and quantitative analyses with actionable recommendations.
  11. Education & Academic Research (RAND Corporation, National Center for Education Statistics, HolonIQ)
      - Produce an analysis report on the future of online education, examining technological adoption, market growth projections, and student outcome trends with supporting data.
      - Generate a comprehensive study on the effects of educational policy reforms on public school performance in the U.S., including trend analysis and actionable recommendations.
      - Create a detailed international higher education trends report, covering tuition dynamics, international student mobility, and emerging academic programs with comparative data.
  12. Real Estate & Property Research (CBRE, JLL, CoStar Group, Cushman & Wakefield)
      - Produce a commercial real estate market analysis report for major urban centers, including occupancy trends, rental rate forecasts, and investment opportunity assessments.
      - Generate a comprehensive study on residential housing market dynamics in emerging economies, focusing on affordability, supply-demand gaps, and policy impacts.
      - Create a detailed report on the impact of urban redevelopment projects on local real estate values, including case studies, forecasts, and strategic recommendations.
  13. Energy & Natural Resources Research (Wood Mackenzie, Rystad Energy, Bloomberg New Energy Finance)
      - Produce an analysis report on global renewable energy trends, covering technology adoption, market forecasts, and key policy drivers, with detailed data and visuals.
      - Generate a comprehensive commodity price forecasting report for oil, natural gas, and key metals, incorporating historical trends, risk assessments, and predictive modeling.
      - Create a detailed report on energy transition strategies for traditional energy companies, focusing on clean technology investments and market adaptation strategies.
  14. Supply Chain & Logistics Research (ARC Advisory Group, Gartner Supply Chain Research, Supply Chain Insights)
      - Produce a report on supply chain resilience for global manufacturers. Analyze risk factors, digital transformation impacts, and best practices for operational efficiency with supporting data.
      - Generate a comprehensive study on the impact of technology on logistics networks, including case studies on digital optimization and cost reduction strategies.
      - Create a detailed report on emerging last-mile delivery solutions, assessing innovations, consumer expectations, and scalability with actionable insights.
  15. Cybersecurity & Information Security Research (KuppingerCole, Forrester Security, IDC Cybersecurity, Cybersecurity Ventures)
      - Produce an in-depth report on emerging cybersecurity threats for large enterprises, including detailed analysis of recent incidents, risk vectors, and defense strategies.
      - Generate a comprehensive cybersecurity market landscape report, evaluating vendor performance, technology forecasts, and best practices for mitigating risks.
      - Create a detailed report on regulatory compliance trends in information security within the financial services industry, with case studies and strategic recommendations.
  16. Social Media, Digital & Online Research (Comscore, SimilarWeb, Brandwatch)
      - Produce a digital audience behavior report for a global brand, focusing on social media trends, engagement metrics, and platform performance with detailed data analysis.
      - Generate a comprehensive analysis of influencer marketing effectiveness across digital channels, including ROI metrics, case studies, and best practices.
      - Create a detailed report on online brand sentiment analysis, incorporating social listening data, trend forecasts, and actionable recommendations.
  17. Public Opinion & Political Research (Pew Research Center, Gallup, YouGov)
      - Produce a public opinion polling report on voter sentiment ahead of a major election. Include demographic breakdowns, key issue analysis, and trend visualizations for the past five years.
      - Generate a comprehensive study on political risk in emerging markets, analyzing historical data, current trends, and future projections, with policy recommendations.
      - Create a detailed report on the influence of media on public policy, using survey data, social media analysis, and comparative case studies.
  18. Sports, Entertainment & Media Research (Nielsen Sports, Sportcal, Kantar Media Sports)
      - Produce a market analysis report on sports sponsorship trends, detailing viewership metrics, brand engagement, and investment ROI with industry case studies.
      - Generate a comprehensive report on audience behavior in the streaming media industry, including demographic insights, consumption trends, and competitive benchmarks.
      - Create a detailed analysis of digital advertising effectiveness in the entertainment sector, including segmentation data, ROI analysis, and strategic recommendations.
  19. Innovation, R&D & Technology Trends Research (Innosight, Frost & Sullivan Innovation, CB Insights)
      - Produce a global R&D investment trends report, analyzing technology spending, innovation indices, and the impact on market growth across key industries.
      - Generate a comprehensive study on disruptive technologies in manufacturing, including competitive analysis, market potential forecasts, and adoption trends.
      - Create a detailed report on emerging innovation hubs worldwide, focusing on startup ecosystems, funding trends, and collaborative opportunities in technology.
  20. Agriculture & Agribusiness Research (Rabobank Agribusiness Research, USDA Economic Research Service, AgFunder)
      - Produce an analysis report on global agricultural market trends, including crop yield forecasts, trade dynamics, and policy impacts, with data visualizations.
      - Generate a comprehensive study on agritech innovations such as precision farming and sustainable practices, including case studies and market forecasts.
      - Create a detailed report on the impact of climate change on food production and supply chain stability in agribusiness, with risk assessments and strategic recommendations.
  21. Environmental & Climate Change Research (Carbon Trust, IHS Markit Energy Transition, Bloomberg New Energy Finance)
      - Produce a report on the economic and social impacts of climate change on urban infrastructure, including forecasting models and policy recommendations.
      - Generate a comprehensive study on national climate policies and their effects on industrial competitiveness, with detailed trend analysis and source citations.
      - Create a detailed report on corporate sustainability initiatives, assessing environmental risk management practices and providing actionable recommendations for improvement.
  22. Customer Experience (CX) & User Experience (UX) Research (Forrester CX Research, Gartner CX Research, Qualtrics, Nielsen Norman Group)
      - Produce a report on customer journey mapping for a leading retail brand, identifying key touchpoints, pain points, and actionable improvement strategies with data visualizations.
      - Generate a comprehensive study on digital user experience trends for e-commerce platforms, including usability testing insights, design best practices, and conversion optimization recommendations.
      - Create a detailed report on customer satisfaction and loyalty metrics across multiple industries, integrating survey data and actionable recommendations to enhance overall CX.
  23. Blockchain, Cryptocurrency & Fintech Research (Chainalysis, CoinDesk Research, Deloitte Fintech Research, CB Insights)
      - Produce an analysis report on emerging blockchain technologies and their applications in financial services, including market trends, adoption forecasts, and case studies.
      - Generate a comprehensive study on cryptocurrency market dynamics, analyzing regulatory developments, investor sentiment, and competitive landscapes with source citations.
      - Create a detailed report on fintech disruption in traditional banking, with case studies on leading startups, technology adoption, and future market forecasts.
  24. Venture Capital, Startup & Private Equity Research (PitchBook, CB Insights, Crunchbase, Preqin)
      - Produce a global venture capital investment trends report, including performance analysis of high-growth startups, sector benchmarks, and emerging market opportunities.
      - Generate a comprehensive study on private equity market dynamics, covering deal flow analysis, exit strategies, and forecasted trends with supporting data.
      - Create a detailed report on emerging startup ecosystems in key regions, highlighting funding trends, investor activity, and growth potential with actionable insights.
  25. Operations Research & Management Science Consulting (The Brattle Group, NERA Economic Consulting, CRA International)
      - Produce a report on optimization techniques for operational efficiency in large-scale manufacturing, including quantitative analysis, simulation models, and case studies.
      - Generate a comprehensive study on the application of predictive analytics in supply chain management, focusing on data modeling, process improvements, and actionable insights.
      - Create a detailed report on advanced quantitative modeling approaches to solve complex business problems in logistics and operations, including scenario analysis and recommendations.
  26. Cultural & Social Research (Ethnographic/Sociocultural Studies) (Ipsos MORI, Kantar TNS, YouGov)
      - Produce a qualitative ethnographic study on urban consumer lifestyle trends, incorporating field observations, interviews, and cultural analysis with actionable insights.
      - Generate a comprehensive study on how cultural shifts influence global brand perception, including comparative case studies and trend analysis.
      - Create a detailed report on sociocultural dynamics and consumer behavior in emerging economies, integrating in-depth field research and actionable recommendations.
  27. Economic & Demographic Research Firms (Oxford Economics, The Conference Board, CEIC Data)
      - Produce a macroeconomic forecasting report for a specific region, including GDP, inflation, and employment trends with detailed data visualizations and source citations.
      - Generate a detailed demographic analysis report for a target market, highlighting age distribution, income levels, and consumption patterns with actionable insights.
      - Create a comprehensive report on the economic impact of demographic shifts on consumer markets, with policy recommendations and trend analysis.
  28. Academic & Think Tank Research Organizations (Brookings Institution, RAND Corporation, Carnegie Endowment for International Peace)
      - Produce a policy research report on global governance challenges and their implications for economic development, including case studies, literature reviews, and expert interviews.
      - Generate a comprehensive study on social inequality and its effects on public health and education outcomes, supported by empirical research and trend analysis.
      - Create a detailed report on emerging trends in international relations and their impact on global trade and security, integrating academic research and data analytics.
  29. Market Research Technology & Software Providers (Qualtrics, SurveyMonkey, Confirmit)
      - Produce a report on the latest innovations in survey technology and data analytics software for market research, including product comparisons, user case studies, and future trend forecasts.
      - Generate a comprehensive study on the integration of AI and machine learning in consumer insights platforms, highlighting case studies, performance metrics, and industry benchmarks.
      - Create a detailed report on digital transformation trends in market research technology, featuring analysis of leading software solutions, market share data, and recommendations for technology adoption.
- When evaluating inputs, models tend to prefer the first response, prefer their own response, and prefer longer responses. [ThursdAI](https://sub.thursdai.news/p/thursdai-feb-20-live-from-ai-eng)
- Real-time speech-to-text options for transcription:
  - [Deepgram](https://deepgram.com/learn/live-transcription-mic-browser) has a MediaRecorder API, which is perfect.
  - [Whisper Streaming Web](https://github.com/QuentinFuxa/whisper_streaming_web) is a web app that can transcribe audio real-time from the browser. A good approach, but I wouldn't use it for meeting transcription on my mid-end laptop. Streaming takes up the bulk of my GPU, leaving little for transcription.
  - [whisper-live](https://github.com/collabora/WhisperLive) runs as a Python console app and does something similar.
  - [Whisper WebGPU](https://huggingface.co/spaces/Xenova/realtime-whisper-webgpu) runs on the browser (only 200MB). Cool! But slow and still takes up GPU.
- [Mini-omni](https://github.com/gpt-omni/mini-omni/) is an open-source Qwen-based LLM that can hear and talk while thinking in real-time. An interesting experiment, but not for prototyping.
- OpenAI shares an insights report with clients that has insights on what different professions search for. What doctors search for is:
  1. Is my diagnosis right?
  2. How do I read this report?
  3. Is my prescription correct?
  4. Is there a cheaper medicine?
  5. What's the life expectancy given these symptoms?
- Dataclasses in Python have a slight overhead over named tuples. The 2 main uses I see for them are: providing defaults and offering type hints.
- UVB 76 is a radio channel has been broadcasting static (with occasional Russian conversation) since 1976. No one knows why. It's live at <https://m.youtube.com/watch?v=8h_D2P0iqMk>
- Romans washed clothes in urine. The government taxed the purchase of urine for commercial purposes! That's the origin of the phrase "Pecunia non olet" which means "money doesn't stink".
- [Nix](https://nixos.org/) is a package manager that creates container-like environments. Like a cross between Docker and `apt` / `venv`. It has an immutable file system. [DevBox](https://www.jetify.com/devbox) is a higher-level tool built on top of Nix that streamlines developer workflows, e.g. common project environment setup.
- VS Code can be used to develop inside a Docker container via Podman, too. Set `dev.containers.dockerPath": "podman"` [Ref](https://geekingoutpodcast.substack.com/p/running-dev-containers-locally-with)
- [Rill Data](https://www.rilldata.com/) is an interesting BI tool based on DuckDB. It auto-generates a dashboard given a dataset.
- It's possible to assign "variables" in SQL (notably in DuckDB). Here's an example:
  ```sql
  WITH
    sessions AS (FROM events SELECT COUNT(DISTINCT session_id) AS value),
    pages AS (FROM events SELECT COUNT(*) AS value)
  FROM sessions, pages
  SELECT sessions.value / pages.value AS pages_per_session;
  ```
- DuckDB has a `GROUP BY *` that groups by all categorical columns. `SELECT x, y, COUNT(*) FROM t GROUP BY *` is equivalent to `SELECT x, y, COUNT(*) FROM t GROUP BY x, y`.
- VS Code can be used as a code executor by adding `{"key": "shift+enter", "command": "workbench.action.terminal.runSelectedText", "when": "editorFocus"}` to the `keybindings.json` file. Press Shift-Enter to run the selection on the terminal. Useful for DuckDB, SQLite, etc. [Ref](https://motherduck.com/blog/duckdb-tutorial-for-beginners/)
- LLMs are excellent at database migration. They can convert schemas and queries across SQL dialects (e.g. BigQuery to DuckDB, etc.) at 90%+ accuracy. This is useful when clients want to migrate cloud providers, go from on-prem to cloud, or reduce cost by switching databases.
