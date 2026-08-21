---
title: Longest repeated paragraph on Wikipedia
date: 2026-05-26T22:20:17+08:00
categories:
- llms
- data
- visualisation
linkedin: https://www.linkedin.com/feed/update/urn:li:activity:7465047314915540993/
description: "I found Wikipedia's most repeated paragraph: 213 words about naming minor planets, copied into 418 articles. A Slovakia census note appears across 2,920 pages, revealing more quirks in Wikipedia's shared text."
tags: [data-analysis, data-mining, wikipedia, codex]
---

What is the most frequently occurring sentence in Wikipedia? ANS: A 213-word paragraph about [how minor planets are named](https://en.wikipedia.org/wiki/Meanings_of_minor-planet_names), which appears in 418 Wikipedia articles, word-for-word!

There are ~380,000 asteroids. Wikipedia has 418 pages for these - including one for each thousand-range of asteroids.

Every single one of these pages includes the phrase:

> As [minor planet](https://en.wikipedia.org/wiki/Minor%5Fplanet "Minor planet") discoveries are confirmed, they are given a permanent number by the [IAU](https://en.wikipedia.org/wiki/International%5FAstronomical%5FUnion "International Astronomical Union")'s [Minor Planet Center](https://en.wikipedia.org/wiki/Minor%5FPlanet%5FCenter "Minor Planet Center") (MPC), and the discoverers can then submit names for them, following the IAU's [naming conventions](https://en.wikipedia.org/wiki/Astronomical%5Fnaming%5Fconventions "Astronomical naming conventions"). The list below concerns those minor planets in the specified number-range that have received names, and explains the meanings of those names.
>
> Official naming citations of newly named [small Solar System bodies](https://en.wikipedia.org/wiki/Small%5FSolar%5FSystem%5Fbodies "Small Solar System bodies") are approved and published in a bulletin by IAU's [Working Group for Small Bodies Nomenclature](https://en.wikipedia.org/wiki/Working%5FGroup%5Ffor%5FSmall%5FBodies%5FNomenclature "Working Group for Small Bodies Nomenclature") (WGSBN).[\[1\]](https://en.wikipedia.org/wiki/Meanings%5Fof%5Fminor-planet%5Fnames:%5F213001%E2%80%93214000#cite%5Fnote-WGSBN-Bulletin-Archive-1) Before May 2021, citations were published in MPC's _[Minor Planet Circulars](https://en.wikipedia.org/wiki/Minor%5FPlanet%5FCirculars "Minor Planet Circulars")_ for many decades.[\[2\]](https://en.wikipedia.org/wiki/Meanings%5Fof%5Fminor-planet%5Fnames:%5F213001%E2%80%93214000#cite%5Fnote-MPC-Circulars-Archive-2) Recent citations can also be found on the [JPL Small-Body Database](https://en.wikipedia.org/wiki/JPL%5FSmall-Body%5FDatabase "JPL Small-Body Database") (SBDB).[\[3\]](https://en.wikipedia.org/wiki/Meanings%5Fof%5Fminor-planet%5Fnames:%5F213001%E2%80%93214000#cite%5Fnote-JPL-Discovery-3) Until his death in 2016, German astronomer [Lutz D. Schmadel](https://en.wikipedia.org/wiki/Lutz%5FD.%5FSchmadel "Lutz D. Schmadel") compiled these citations into the _Dictionary of Minor Planet Names_ (DMP) and regularly updated the collection.[\[4\]](https://en.wikipedia.org/wiki/Meanings%5Fof%5Fminor-planet%5Fnames:%5F213001%E2%80%93214000#cite%5Fnote-DoMPN-4)[\[5\]](https://en.wikipedia.org/wiki/Meanings%5Fof%5Fminor-planet%5Fnames:%5F213001%E2%80%93214000#cite%5Fnote-DoMPN-Addendum-5)
>
> Based on [Paul Herget](https://en.wikipedia.org/wiki/Paul%5FHerget "Paul Herget")'s _[The Names of the Minor Planets](https://en.wikipedia.org/wiki/The%5FNames%5Fof%5Fthe%5FMinor%5FPlanets "The Names of the Minor Planets")_,[\[6\]](https://en.wikipedia.org/wiki/Meanings%5Fof%5Fminor-planet%5Fnames:%5F213001%E2%80%93214000#cite%5Fnote-Herget-6) Schmadel also researched the unclear origin of numerous asteroids, most of which had been named prior to World War II.

Check out these pages
| [85001-86000](https://en.wikipedia.org/wiki/Meanings_of_minor-planet_names:_85001%E2%80%9386000)
| [213001-214000](https://en.wikipedia.org/wiki/Meanings_of_minor-planet_names:_213001%E2%80%93214000)
| [269001-270000](https://en.wikipedia.org/wiki/Meanings_of_minor-planet_names:_269001%E2%80%93270000)
| [380001-381000](https://en.wikipedia.org/wiki/Meanings_of_minor-planet_names:_380001%E2%80%93381000)

This is not the only such common sentence. There are several more.

![](https://sanand0.github.io/datastories/longest-wikipedia-string/screenshot.avif)

Here's the Slovakia census note: 81 words that appear across **2,920 Wikipedia pages**, like
[Sabinov District](https://en.wikipedia.org/wiki/Sabinov%5FDistrict),
[Smolenice](https://en.wikipedia.org/wiki/Smolenice),
[Ilija, Slovakia](https://en.wikipedia.org/wiki/Ilija,%5FSlovakia),
[Baloň](https://en.wikipedia.org/wiki/Balo%C5%88), ... and thousands more!

> Note on population: The difference between the population numbers above and in the census (here and below) is that the population numbers above are mostly made up of permanent residents, etc.; and the census should indicate the place where people actually mainly live. For example, a student is a citizen of a village because they have permanent residence there (they lived there as a child and has parents), but most of the time he studies at a university in the city

**Note**: As of 26 May 2026, this has been shortened to:

> Note on population: The difference values of population numbers in the table "Population statistic" and in the sections "Ethnicity" & "Religion" is caused by the use of various statistical methods.

---

There are several more such that you can read about in [The Paragraph That Appears 418 Times](https://sanand0.github.io/datastories/longest-wikipedia-string/).

That also includes how [Codex](https://openai.com/codex/) analyzed the [Wikipedia structured dataset on Hugging Face](https://huggingface.co/datasets/wikimedia/structured-wikipedia) and what else you can do with the data.
