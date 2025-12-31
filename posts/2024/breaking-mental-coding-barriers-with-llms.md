---
title: Breaking mental coding barriers with LLMs
date: "2024-09-02T05:59:02Z"
lastmod: "2024-09-02T05:59:04Z"
categories:
  - links
wp_id: 3619
---

![Breaking mental coding barriers with LLMs](/blog/assets/mermaid.webp)

Today, I stepped a bit beyond my comfort zone. Usually, I prefer micro-managing LLMs when writing code. This time, I was macro-managing.

I needed to create a mock history of the status of a manuscript, e.g. it was submitted on this date. THEN it moved to this state on this date. THEN ... etc. I have no idea what the states could be, though. So, I could send it to an LLM, and it would give a different set of states each time. Or I could write a program and lose out on variety.

Instead, [I asked ChatGPT](https://chatgpt.com/share/3780999d-76a5-42bc-a98a-e1fe19342cb2).

> **Me**: When looking up the status of a manuscript in a database, what are typical fields it might return?
>
> **ChatGPT**: When looking up the status of a manuscript in a database, typical fields it might return include:
>
> 1. Manuscript ID: A unique identifier for the manuscript.
> 2. Title: The title of the manuscript.
> 3. Author(s): Names of the author(s) who submitted the manuscript.
> 4. Submission Date: The date the manuscript was submitted.
> 5. Status: The current status of the manuscript (e.g., Under Review, Accepted, Rejected, In Revision).
> 6. ...

That helps. [Then I said](https://chatgpt.com/share/3780999d-76a5-42bc-a98a-e1fe19342cb2):

> **Me**: Based on this, at any point, what "Status" values could a manuscript be in? Draw a mermaid flow graph for this.
>
> **ChatGPT**: Here's a mermaid flow graph depicting possible "Status" values a manuscript could be in throughout its lifecycle:

![](/blog/assets/mermaid.webp)

This is cool -- it gives me a starting point that's better than I could have conceived of.

Finally, [I said](https://chatgpt.com/share/3780999d-76a5-42bc-a98a-e1fe19342cb2):

> **Me**: Write JS code that will randomly pick from one of these states and create records containing random dates and states representing the history of the manuscript up to that point
>
> **ChatGPT**: Here's a JavaScript code snippet that randomly picks from the manuscript states and creates records containing random dates and states, representing the history of the manuscript up to that point:

```javascript
function getRandomDate(start, end) {
  return new Date(
    start.getTime() + Math.random() * (end.getTime() - start.getTime()),
  );
}

function getRandomElement(arr) {
  return arr[Math.floor(Math.random() * arr.length)];
}

function generateManuscriptHistory() {
  const history = [];
  let currentState = "Submitted";
  let currentDate = getRandomDate(new Date(2020, 0, 1), new Date());

  history.push({ date: currentDate, state: currentState });

  while (
    currentState !== "Accepted" && currentState !== "Rejected"
    && currentState !== "Published"
  ) {
    let possibleNextStates;

    switch (currentState) {
      case "Submitted":
        possibleNextStates = ["Under Review"];
        break;
      case "Under Review":
        possibleNextStates = ["Review Completed"];
        break;
      case "Review Completed":
        possibleNextStates = [
          "Accepted",
          "Rejected",
          "Major Revision Required",
          "Minor Revision Required",
        ];
        break;
      case "Major Revision Required":
      case "Minor Revision Required":
        possibleNextStates = ["In Revision"];
        break;
      case "In Revision":
        possibleNextStates = ["Resubmitted"];
        break;
      case "Resubmitted":
        possibleNextStates = ["Under Review"];
        break;
      case "Accepted":
        possibleNextStates = ["In Production"];
        break;
      case "In Production":
        possibleNextStates = ["Published"];
        break;
      default:
        possibleNextStates = [];
        break;
    }

    if (possibleNextStates.length === 0) break;

    currentState = getRandomElement(possibleNextStates);
    currentDate = getRandomDate(currentDate, new Date());

    history.push({ date: currentDate, state: currentState });
  }

  return history;
}

// Example usage:
console.log(generateManuscriptHistory());
```

The above code implements a state-transition diagram -- something I've **never** been good at doing. I have a subconscious bias, and I steer clear of even **thinking** about these. Now, I have one implemented (and it worked quite well!)

Yet another example that human imagination is the bottleneck to leveraging LLMs.
