---
title: Cyborg scraping
date: "2021-06-25T04:03:23Z"
lastmod: "2023-03-31T07:26:18Z"
categories:
  - coding
  - how-i-do-things
wp_id: 3142
---

![Cyborg scraping](/blog/assets/linkedin-followers.webp)

LinkedIn has a page that shows the [people who most recently followed you](https://www.linkedin.com/feed/followers/).

At first, it shows just 20 people. But as you scroll, it keeps fetching the rest. I'd love to get the full list on a spreadsheet. I'm curious about:

1. What kind of people follow me?
2. Which of them has the most followers?
3. Who are my earliest followers?

But first, I need to **scrape this list**. Normally, I'd spend a day writing a program. But I tried a different approach yesterday.

**Aside**: it's easy to get bored in online meetings. I have a surplus of partially distracted time. So rather than writing code to save me time, I'd rather create simple tasks to keep me occupied. **Like **scrolling**.**

![](https://media.giphy.com/media/Er3QVX48nt5ok/giphy.gif)

So here's my workflow to scrape the list of followers.

**Step 1**: Keep scrolling all the way to the bottom until you get all followers.

**Step 2**: Press F12, open the Developer Tools - Console, and paste this code.

```javascript
copy(
  $$(".follows-recommendation-card").map(v => {
    let name = v.querySelector(".follows-recommendation-card__name");
    let headline = v.querySelector(".follows-recommendation-card__headline");
    let subtext = v.querySelector(".follows-recommendation-card__subtext");
    let link = v.querySelector(".follows-recommendation-card__avatar-link");
    let followers = "", match;
    if (subtext) {
      if (match = subtext.innerText.match(/([\d\.K]+) follower/)) {
        followers = match[1];
      } else if (match = subtext.innerText.match(/([\d\.K]+) other/)) {
        followers = match[1];
      }
    }
    followers = followers.match(/K$/)
      ? parseFloat(followers) * 1000
      : parseFloat(followers);
    return {
      name: name ? name.innerText : "",
      headline: headline ? headline.innerText : "",
      followers: followers,
      link: link ? link.href : "",
    };
  }),
);
```

**Step 3**: The name, headline, followers and link are now in the clipboard as JSON. Visit <https://www.convertcsv.com/json-to-csv.htm> and paste it in "Select your input" under "Enter Data".

![](/blog/assets/json-to-csv.webp)

**Step 4**: Click on the "Download Result" button. The JSON is converted into a CSV you can load into a spreadsheet.

I call this "**Cyborg scraping**". I do half the work (scrolling, copy-pasting, etc.) The code does half the work. It's manual. It's a bit slow. But it gets the job done quick and dirty.

I'll share later what I learned about my followers. For now, I'm looking forward to meetings 😉

PS: A similar script to scrape [LinkedIn invitations](https://www.linkedin.com/mynetwork/invitation-manager/) is below. You can only see 100 invitations per page, though.

```javascript
copy(
  $$(".invitation-card").map(v => ({
    name: (v.querySelector(".invitation-card__title") || {}).innerText || "",
    link: v.querySelector(".invitation-card__link").href,
    subtitle: (v.querySelector(".invitation-card__subtitle") || {}).innerText
      || "",
    common: (v.querySelector(".member-insights__count") || {}).innerText || "",
    message:
      (v.querySelector(".invitation-card__custom-message") || {}).innerText
      || "",
  })),
);
```

PS: A similar script to scrape [LinkedIn people search results](https://www.linkedin.com/search/results/people/?keywords=data%20scientist&sid=uWx) is below.

```javascript
copy(
  $$(".entity-result").map(v => {
    const name = v.querySelector(
      ".entity-result__title-text [aria-hidden=\"true\"]",
    );
    const link = v.querySelector("a");
    const badge = v.querySelector(
      ".entity-result__badge [aria-hidden=\"true\"]",
    );
    const title = v.querySelector(".entity-result__primary-subtitle");
    const subtitle = v.querySelector(".entity-result__secondary-subtitle");
    const summary = v.querySelector(".entity-result__summary--2-lines");
    const insight = v.querySelector(".entity-result__simple-insight-text");
    return {
      name: name?.innerText || "",
      link: (link?.href || "").split("?")[0],
      badge: badge?.innerText || "",
      title: title?.innerText || "",
      subtitle: subtitle?.innerText || "",
      summary: summary?.innerText || "",
      insight: insight?.innerText || "",
    };
  }),
);
```

---

## Comments

<!-- wp-comments-start -->

- **[mvark](https://mvark.blogspot.in)** _8 Aug 2021 10:39 pm_:
  I think rather than create JSON, building a comma separated string and console.log-ging that string will show the whole list in the Dev Tools Console. Using the Save As option in the context menu, the list can be saved as a .CSV file directly without Step 3 & 4.
- **[Tools to publish annotated talks from videos - S Anand](/blog/tools-to-publish-annotated-talks-from-videos/)** _20 Oct 2024 12:53 pm_ _(pingback)_:
  […] together. As you scroll, newer/older comments are loaded. So I needed to use my favorite technique: Cyborg Scraping. During Q&A, I kept scrolling to the bottom and […]

<!-- wp-comments-end -->
