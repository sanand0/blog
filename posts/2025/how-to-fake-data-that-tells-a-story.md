---
title: How to Fake Data That Tells a Story
date: "2025-03-08T06:16:44Z"
lastmod: "2025-03-08T06:16:46Z"
categories:
  - coding
  - llms
wp_id: 3954
---

![How to Fake Data That Tells a Story](/blog/assets/calvin-snowman-bar-chart.webp)

Fake data is usually boring if you analyze it. It's usually uniform, with no outliers or interesting patterns.

If I ask [ChatGPT](https://chatgpt.com/share/67cbda58-e0dc-800c-ad00-47f1904c8fa3):

```javascript
Generate realistic fake tourism data using these columns:

- Age
- Nationality
- Gender
- Income
- Booking_Channel
- Month
- Occupancy_Rate
- Travel_Frequency
- Spending

Run the code and let me download the output as a CSV file.
```

… the output is remarkably boring.

- Men & women from all countries and ages in every month visit equally.
- Income and spending are uniformly distributed - and the same pattern holds for all countries and ages.

![](/blog/assets/boring-data-distribution-1024x862.webp)

Often, I need to generate fake data that is **interesting**. Specifically, I need data that can be used to illustrate a point or show a pattern.

Instead, we could ask for something different. [ChatGPT](https://chatgpt.com/share/67cbdc51-c2fc-800c-aa19-e472054a6b0e)

```javascript
I want to generate realistic fake tourism data using these columns:

- Age
- Nationality
- Gender
- Income
- Booking_Channel
- Month
- Occupancy_Rate
- Travel_Frequency
- Spending

Do it as follows:

STEP 1. Given such data, generate 5 hypotheses on that a tourism department might test to increase tourist spend.
STEP 2. Write a Python program that generates 2,000 rows of realistic fake data where these hypotheses are true in a statistically significant way.
STEP 3. Run the code and let me download the output as a CSV file.
```

This works like a charm. The data generated exhibits these patterns:

1. Luxury travel agency customers spend much more.
2. Peak-month travelers (June, July, December) spend more.
3. Frequent travelers spend less.
4. Older tourists (50+) spend more.
5. Tourists from USA, Germany, and Japan spend more.

The data is more varied: some 20-year-olds spend much less (creating outliers). Many tourists come from the US, and a large share book online.

![](/blog/assets/realistic-data-distribution-1024x767.webp)

So, here's my generic prompt for realistic fake data on [ChatGPT](https://chatgpt.com/share/67cbdc05-8b44-800c-95d4-afe97cd2e149):

```javascript
Generate realistic fake data for ______

STEP 1. List columns that would be present in such data, briefly describing how the data might be distributed.
STEP 2. Given such data, think about an objective and generate 5 hypotheses that an organization might want to test on how to achieve this objective.
STEP 3. Write and run a Python program that generates 2,000 rows of realistic fake data where these hypotheses are true in a statistically significant way. Let me download the output as a CSV file.
STEP 4. Test each hypothesis and show the results.
```

---

## Comments

<!-- wp-comments-start -->

- **Prashant Raturi** _6 Sep 2025 11:10 am_:
  Awesome. Treasure trove of a blog

<!-- wp-comments-end -->
