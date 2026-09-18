---
title: India Fast Track Immigration PDFs
date: 2026-09-17T09:21:43+01:00
categories:
    - interesting-experiences
description: I finally got India’s Fast Track Immigration application to accept my passport PDFs after renaming them to simple filenames like front.pdf and back.pdf. The site gave no error or filename guidance.
tags: [problem-solving, india, web-applications]
---

For over a year, now, I've been trying to enroll myself into the Indian [Fast Track Immigration](https://ftittp.mha.gov.in/fti/) biometric system. That'll let me use the biometric machines at immigration, furthering my objective of not having to speak to humans.

Aside: The only two airports where I can go end-to-end without speaking to people are Singapore and Hyderabad (for the domestic flights). Bangalore and Chennai come close in the recent past. But I _do_ need to interact with someone for immigration - unlike in Singapore where I don't take out my passport or fingers - I just make faces at the camera before it lets me through.

The trouble with the [FTI site](https://ftittp.mha.gov.in/fti/) is that the application wouldn't let me upload my passport PDF.

It was the right format. It was the right file size. Despite multiple attempts, it stubbornly refused to accept the file - and there was no error message, not even in the DevTools console.

I tried a few things, like compressing the image, change the image format, removing spaces from the filename, ... and _none_ of them worked.

I'd repeat the attempt every few months - from my mobile, different browsers, even a different laptop. All to no avail.

Today, just after I passed through Mumbai immigration - which required filling out [Air Suvidhi 2.0](https://airsuvidha.civilaviation.gov.in/) with:

1. Are you travelling as: Individual or Family?
2. Full Name: (which you can pick up from my passport)
3. Gender: (same)
4. Age: (same)
5. Nationality: (same)
6. Passport Number: (OK, required)
7. Journey to India: Direct or Transit (do you _really_ need this?)
9. First country of boarding & departure: (which you can pick up from my flight number)
10. First Country of Boarding: (same)
11. Date of Departure from Boarding Country: (same)
12. Airport of First Boarding: (same)
13. Ebola Affected Countries Visited/Transited in Last 21 Days: None, DR Congo, Uganda, South Sudan: (OK, that's probably required)
14. First international airport of arrival in India: (um... I'm literally in front of you and you know where _you_ are)
15. Flight Number Arriving to India: (OK, required)
16. Airline Name: (which you can pick up from my flight number)
17. Seat Number: Optional (why bother asking?)
18. Arrival Date & Time: (which you can pick up from my flight number)
19. Any onward domestic travel or international transit: None, Domestic, Others, International transit (do you _really_ need this?)
20. Places to Visit in India: State, District
21. OTP Verification: (OK, required)
22. Email Address: (OK, required)
23. Alternate mobile: (do you _really_ need this?)
24. ... (and it goes on to ask for a bunch of _more_ things!)

Frankly, the old paper form was easier to fill. (The form design was fairly mobile friendly, though. Just too many questions.)

---

Anyway, as I walked past Mumbai immigration, I saw a Fast Track Immigration counter, so I walked over.

**Me**: I'd like to enroll for FTI.\
**Them**: Fill out the form online with the QR code.\
**Me**: I tried. Many times. It didn't work. Let me try again in front of you.

I logged in. The site had a problem and wouldn't show any content.

I logged out and logged in. Same problem.

Different browser. Same problem.

Finally, it did manage to log me in. Then I re-opened my incomplete application. It needed a passport photo (again) which I captured using [online-camera.com](https://online-camera.com/). Then came the passport PDF.

**Me**: See, I uploaded my passport PDF. Nothing's happening.
**Them**: Try breaking it into a separate front and back page PDFs. (Good idea, actually.)
**Me**: OK, did that, still didn't allow me.
**Them**: Is the file too large or small?
**Me**: No. About 130 KB, which is in the 10 KB - 1 MB limit.
**Them**: Try removing the "dots" in the filename?
**Me**: OK, renamed to `front.pdf` and `back.pdf`.

... _and, shockingly, that worked_!

![](https://files.s-anand.net/images/2026-09-17-india-fast-track-immigration-pdfs.avif)

We both checked if there was any instruction mentioning that the filename should follow any rules. None were mentioned.

**Me**: Will you be able to let the team know to mention using simple filenames?
**Them**: Yes, I'll let them know.

So, there you go. Until the Ministry of Home Affairs tells you, play it safe.

**Upload files with simple filenames**: Just alphabets and numbers and keep it under 8 letters, to be safe.
