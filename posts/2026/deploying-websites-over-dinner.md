---
title: Deploying websites over dinner
date: 2026-04-27T16:30:50-04:00
categories:
  - tools
description: I successfully deployed a custom website over dinner using only a mobile phone. By combining ChatGPT dictation, GitHub Mobile for hosting, and Cloudflare for DNS, we registered a domain and published a site without leaving the table.
keywords: [github pages, github mobile, cloudflare registrar, gemini, chatgpt, mobile deployment, dns]
---

Over dinner with [Nishka](https://www.linkedin.com/in/nishka-gattu-32133b339/), we were trying to deploy a website. The challenge was: How can we deploy this website, just on mobile, **without getting up from the dinner table**?

**STEP 1: Hosting**. On my phone, I dictated to ChatGPT (whose transcription is excellent), copy-pasted that to Gemini (which is faster):

> I want to publish specifically a static HTML web page on my own domain.\
> I want the easiest way that I can host it, preferably just by copy-pasting from my mobile without needing to muck around with Git and the likes of it.\
> What are the most robust, reliable hosting providers that I could use? I can sort out the domain name myself as long as they support an option to map a custom domain name to them.\
> Ideally, I am looking for something that is free, preferably free forever.

Top answer: [GitHub Pages](https://pages.github.com/).

Since Nikki already had a GitHub account, that worked well. Using [GitHub Mobile](https://github.com/mobile), she created a new repository, created a new `index.html`, and published it to GitHub Pages - all from the phone, without needing to get up from the dinner table. (The content was vibe-coded later, but the infrastructure was set up during dinner.)

**STEP 2: Domain Name**. Next question - again, to Gemini via ChatGPT dictation:

> Okay, I want to buy a domain name next. What's the cleanest simplest cheap way that I can get a domain?\
> For now I'm not particular about which domain but I should be able to buy this very easily just on a mobile and I should be able to configure the DNS directly on the mobile itself.

Top answer: [Cloudflare Registrar](https://www.cloudflare.com/products/registrar/).

Nikki didn't have a Cloudflare account, but was able to sign up for one easily on the phone.

After searching for a bit, [rexgattu.com](https://www.rexgattu.com/) (the future home page for the youngest member of the family) was available for ~$10/year.

![Photo of Rex](https://files.s-anand.net/images/2026-04-27-rex-gattu.avif)

Her sister's credit card photos were available on her phone, so there was no need to get up from the dinner table to get the card details.

**STEP 3: Setting up DNS**. The third question was:

> How do I point a domain name that I purchased on Cloudflare and his managed by Cloudflare to a GitHub Pages page?

It provided step-by-step instructions: Go to DNS > Records. Add an A record pointing `@` to `185.199.108.153`. Add a CNAME record pointing `www` to `[username].github.io`.

She did that. Now [`www.rexgattu.com`](https://www.rexgattu.com/) pointed to the GitHub Pages site.

---

That's it! Our infrastructure has gone to the point where we can deploy a website on a custom domain, without even needing to get up from the table.
