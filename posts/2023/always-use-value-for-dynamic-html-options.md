---
title: Always use value= for dynamic HTML options
date: "2023-07-31T06:45:48Z"
lastmod: "2023-07-31T06:46:19Z"
categories:
  - coding
wp_id: 3447
---

![Always use value= for dynamic HTML options](/blog/assets/html-code.webp)

Even after 30 years of HTML, I learn new things about it.

This Monday morning, I woke up to a mail from [Sundeep](https://www.linkedin.com/in/sundeeprm/) saying requests for a `Data Engineer - AWS/Azure/GCP` in our internal fulfilment portal raised an error.

My guess was one of these:

1. The "/" in the role is causing a problem. (Developer mistake.)
2. The role exists in one table but not the other. (Recruitment team mistake.)
3. The application wasn't set up / restarted properly. (IT mistake.)

**All three were wrong**. So I dug deeper.

The role was defined as `Data Engineer  - AWS/Azure/GCP` (note the 2 spaces before the hyphen). But the form kept sending `Data Engineer - AWS/Azure/GCP` (spaces were condensed).

I swear there was **NOTHING** in the code that changes the options. The relevant line just picked up the role and rendered it inside the `<select>`:

````html
```markup
<option>{{ row['Role'] }}</option>
````

I used the browser's developer tools to inspect the `<select>` element. It showed the options with the 2 spaces:

```markup
<option>Data Engineer  - AWS/Azure/GCP</option>
```

But, when I selected it and printed the value, it had only one space.

```javascript
> console.log(document.querySelector("#role").value<br/>'Data Engineer - AWS/Azure/GCP'
```

That's when it hit me. [HTML condenses whitespaces](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Whitespace).

Till date, I only ever used `<option value="">` when specifying a value **different** from what's displayed. I never thought of using it to **preserve** the value.

**LESSON**: If you're dynamically generating `<option>`s, **ALWAYS** use `value=` with the same value as the text.
