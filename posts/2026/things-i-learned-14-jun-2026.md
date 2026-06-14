---
title: Things I Learned - 14 Jun 2026
date: 2026-06-14T00:00:00+00:00
categories:
  - til
---

This week, I learned:

- Overheard a journalist saying: "I can tell when humans are lying. There are no tell tale signs of AI lying. At least _I_ don't have any."
- [rdt-cli](https://github.com/public-clis/rdt-cli) is a Reddit CLI. It uses a clever trick: it auto-detects installed browsers and extracts cookies (supports Chrome, Firefox, Edge, Brave). So, if you're logged into Reddit on any browser, `uvx --from rdt-cli rdt whoami` automatically shows who you are logged in as. (The [public-clis](https://github.com/public-clis/public-clis) repo also lists other useful CLIs like [twitter-cli](https://github.com/public-clis/twitter-cli), )
- Currently, a $20 Claude Pro gives you ~$400 and a $100 Claude Max gives you ~$2,000 of API usage. For ChatGPT, the numbers are ~$700 and $3,500. [SemiAnalysis](https://x.com/SemiAnalysis_/status/2064815044085318040)
- When Fable 5 refuses to answer questions, here's the message that appears: "Fable 5 has safety measures that flag messages on most cybersecurity or biology topics. They may flag safe, normal content as well. These measures let us bring you Mythos-level capability in other areas sooner, and we're working to refine them. Send feedback or [learn more](https://support.claude.com/en/articles/15363606)." I managed to trigger this once while researching an M&A acquisition target. Clicking on "Edit and retry with Fable 5" triggered Opus 5 again, twice.
- DNA codons (A, T, C, G) encode proteins in triplets. There are [64 triplets that map to 20 amino acids](https://en.wikipedia.org/wiki/DNA_and_RNA_codon_tables). Some like Leucine, have 6 codons. Some like Methionine have only one. Why? When creating genes, there's a wobble, sometimes, at the 3rd codon. THe mapping minimizes that impact: small errors map to similar proteins. The more common proteins have more codons. There's a lot of fascinating information science going on here. [Gemini](https://gemini.google.com/share/cfa70dcab30c)
- ChatGPT now shows a "Check in" button when it's thinking. Clicking on that gives you a work-in-progress answer while it continues thinking. When done, it _replaces_ the WIP answer with the final answer. A useful feature!
