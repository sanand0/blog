---
title: Converting TUS Nesstar Files
date: 2026-11-09T16:00:12+08:00
categories:
- coding
- llms
description: I used ChatGPT on Linux to convert India's 900 MB Time Use Survey Nesstar file into Excel and Parquet, despite the end-of-life Windows software. It left me thinking about making old data usable again.
tags: [chatgpt, open-data]
---

The [Time Use Survey 2024](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2106113&reg=48&lang=2) [data](https://microdata.gov.in/NADA/index.php/catalog/236) released last year lets you download a ZIP containing a 900 MB `.Nesstar` file.

(This is after you register - but the registration is free, and though it requires a reason, it's automated.)

[Nesstar](https://en.wikipedia.org/wiki/Nesstar) is Norwegian software that's now end of life. MOSPI provides [this guide](https://mospi.gov.in/sites/default/files/data_disemination/Guide_to_download_microdata.pdf) - with distorted screenshots - explaining how to install the software on Windows.

But I use Linux. The software is end-of-life. Gaah!

However, I have ChatGPT.

![](https://files.s-anand.net/images/2026-11-09-mere-paas-chatgpt-hain.avif)

I uploaded the .Nesstar file and prompted ChatGPT to "Convert this TUS data to an Excel and Parquet file format so I can download it." The first attempt failed (the conversation became too long) but the [second attempt](https://chatgpt.com/share/6af1801d-04d0-83ee-a858-b77e2ff37c1b) <!-- https://chatgpt.com/c/6af11638-23d8-83e8-8b08-5277933f8739 --> let me download the data as `.parquet` and gave me a [thrift-based `uv` script](https://files.s-anand.net/blog/2026-11-09-converting-tus-nesstar-files/tus_nesstar_to_parquet.py) to convert the file to `.parquet`. ([nesstar-reader](https://github.com/jmoy/nesstar-reader) might work, too.)

The ease of this converstion opens up a wide variety of possibilities in my mind.

- **Accessible data**. Re-publish data in archaic formats. For example, [Saket](https://github.com/saketkc) recently created [nesstarR](https://cran.r-project.org/web/packages/nesstarR/vignettes/nesstarR.html) and maintains [mospiR](https://github.com/saketkc/mospiR) - making _any_ MOSPI dataset more accessible.
- **Retrospective research**. Re-run experiments from old raw data. For example, [NASA found two moons from old Voyager data](https://science.nasa.gov/open-science/archival-data-discoveries/). This is a good reason to capture more data in raw formats - and also not worry too much if we can't, since future intelligence might probably overcome limitations.
- **Rewrite regulatory software**. For example, [OpenTax](https://github.com/filedcom/opentax) is an agent-engineered US federal tax calculator. [OpenBooks](https://github.com/clawnify/OpenBooks) aims for EU-compliance. It would be nice to replace Singapore's [BizFinx](https://www.acra.gov.sg/resources/eservice-tools-portals/xbrl-filing-tools/bizfinx-preparation/), Pharma [Open eCTD publishers](https://www.assyro.com/blog/ectd-software-vendors-comparison), and build an open regulatory compliance infrastructure.
