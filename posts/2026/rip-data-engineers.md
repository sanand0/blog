---
title: RIP, Data Engineers
date: '2026-02-04T19:22:13+08:00'
categories:
- llms
description: AI can already do large-scale SQL pattern analysis that exposes organizational blind spots, shrinking the need for some traditional data-engineering analysis work.
tags: [data-engineering, self-analysis, ai-automation, databases]
linkedin: https://www.linkedin.com/feed/update/urn:li:activity:7425754411886632961/
---

As AI marches along, another role at risk is the data engineer / database administrator.

([Data scientists](https://sanand0.github.io/talks/2025-08-21-rip-data-scientists/) are already feeling the heat.)

A common task for data engineers is to analyze SQL queries - to optimize and standardize.

[Pavan](https://github.com/pavankumart18/) used [Antigravity](https://antigravity.google/) to analyze 1,500 SQL queries and found:

1. 30% of queries are purely headcount / volume related. Much more than revenue (25%) or engagement (15%). That's sign of a **tactical culture**.
2. 70% of the queries are about _What happened yesterday?_ rather than _What will happen tomorrow?_ - again, **tactical culture**.

[Here's the analysis.](https://pavankumart18.github.io/sql-analysis/)

As a next step, he built a "Middle Layer" - intermediate tables that standardize and optimize queries. Instead of 50 fragile tables, the user can query just 3 robust tables that cover 98% of the SQL queries.

For example:

- A `net_revenue` field that standardizes net revenue after adjustments, i.e. `SUM(face_value - discount)`, which is used in 58% of queries. That ensures that Finance (which used to see the GAAP Revenue) and Sales (which used to see the Booked Revenue) are now aligned.
- A `tickets_sold` field that standardizes distinct count of tickets sold, used in 85% of queries, and is a slow computation.

NOTE: Season ticket buyers often bought merchandise as guests (for convenience). Marketing saw these as new customers and spammed them - annoying VIP customers. This standardization created an identity graph - so they can offer discounts instead.

The process, which Antigravity figured out mostly by itself, was to parse the SQL into an abstract syntax tree (AST), extract a set of features, map them into clusters (archetypes), and analyze them to create the middle layer tables.

[![](https://files.s-anand.net/images/2026-02-04-sql-analysis-feature-table.webp)](https://pavankumart18.github.io/sql-analysis/)

SQL queries can reveal organizational culture and misalignment - which is cool! But also:

- This took a few hours.
- Pavan has no data engineering experience.

RIP, Data Engineers.
