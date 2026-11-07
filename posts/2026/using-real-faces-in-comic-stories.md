---
title: Using Real Faces in Comic Stories
date: 2026-11-07T16:40:52+08:00
categories:
- llms
- how-i-do-things
description: 'I turned sparse event notes into a black-and-white comic with real faces: Claude wrote prompts, ChatGPT matched photos, and Codex checked and corrected pages while I read Asterix.'
tags: [image-generation, prompt-engineering, comic-strips, llms]
---

I was reading [Asterix on my flight from Brussels to Dubai](https://www.s-anand.net/blog/reading-asterix-from-brussels-to-dubai-via-singapore/) when I remembered a colleague's request. I typically convert my workshops into narratives like [this](https://talks.s-anand.net/2026-10-12-tds-ideation/) and [this](https://talks.s-anand.net/2026-10-25-aipl-2/). They wanted another event converted.

Usually, I have the full transcript of my events. In this case, I just had a few paragraphs of notes. Far from enough.

On the other hand, I was reading Asterix. And AI's _my_ magic potion. So I figured:

Why not create a **comic** story?\
Using **real** faces?\
**While** reading Asterix?

### Step 1: Story to prompts

So, step 1. Comic story. That's easy. I've researched [multiple comic styles](https://sanand0.github.io/llmartstyle/?category=comic) and have a sense of the style that might suit. So, I told Claude Opus 5.5 High, roughly:

<!-- https://claude.ai/chat/b8edcad5-e727-428a-a53e-701173e6a03c -->

> Read [the email]. Let's use ChatGPT to create a black-and-white comic strip series narrating what happened.\
> Sort of like Calvin and Hobbes or Peanuts or even Scott McCloud's Understanding Comics.\
> Maybe a dozen strips of 2-4 panels each? Or 4 pages of 8-14 panels each?
>
> Think like an expert storyteller and comic artist.\
> Research ChatGPT's latest image model - good and bad.\
> Give me a series of prompts for ChatGPT.
>
> I want people to look like their photos.
> Create prompts.

That gave me a nice story using the black cat in the [Black Cat Bar](https://en.wikipedia.org/wiki/Black_Cat_Bar) as the narrator.

### Step 2: Get profile photos

<!-- https://chatgpt.com/g/g-p-6ae3898e99408191b5e60ee7b60be758-convergence-comic/c/6ae36a5b-8b14-83ec-bd20-77ea59909f2a -->

I asked ChatGPT with GPT 6 Sol - High to **search for the people**:

> Go through this email thread.\
> Download a few photos (preferably profile pictures) of each of the people mentioned in the email.

... and **corrected** it:

> You have Namit's picture instead of Ankor's. Also, photo 2 isn't what's in the source you indicated.\
> These worry me a lot.
>
> Go through every single one of the photos you've identified and check if it's really from the source and the images match.\
> Make sure these ARE, in fact, the people that attended the event - and flag any uncertainty.

This worked well. There weren't any mistakes, but there were a few people and we weren't sure if THEY were the ones in the event.

Mid-flight, I saw that they'd sent me actual **attendee photos** from the event. So:

> Match the profile pictures against the attendee photos.\
> Label who is present where in which picture.\
> Identify unknown people - and see if you can search for them online,\
> e.g. to see if they match any of the people we couldn't find images for.

That gave me an excellent base.

### Step 3: Create a style guide

<!-- https://chatgpt.com/g/g-p-6ae3898e99408191b5e60ee7b60be758-convergence-comic/c/6ae38a61-daa8-83ec-9fa9-4aab70c38f87 -->

This was a clever step by Claude. It told me to create a photo style guide in four steps. Click on each to expand the prompts.

<details>
<summary><strong>1. Create a character model sheet for the cat</strong></summary>

![](https://files.s-anand.net/blog/2026-11-07-convergence-comic-story/ref-01-cat-input.avif)

> STYLE BIBLE — "THE CONVERGENCE ROOM" (a 13-page black-and-white comic)
>
> LOOK
>
> - Black ink on pure white paper. No colour, no grey wash, no sepia, no paper texture, no gradients.
> - Shading only with solid spot blacks, fine cross-hatching and sparing dot screentone.
> - Classic newspaper comic-strip craft: confident brush-and-ink line with thick-to-thin weight, loose and hand-drawn, slightly imperfect. Not vector-clean, not manga, not photoreal, not 3D.
> - People: warm, simplified caricature with normal adult proportions. Likeness comes from a few signature features (face shape, hairline, glasses, facial hair, build), not detailed rendering.
> - Characters are told apart by silhouette and by black/white value of their clothes, not colour.
>
> LAYOUT
>
> - Square 1:1 image, highest resolution available.
> - Hand-ruled black panel borders, even white gutters. 2×2 grid unless the script says otherwise.
> - Hand-lettered title bar across the top: "THE CONVERGENCE ROOM • [NO.] • [TITLE]".
> - Read left-to-right, top-to-bottom. Vary shots: wide establishing, medium, close-up.
> - Flashback panels have wavy borders.
>
> LETTERING
>
> - Hand-lettered ALL-CAPS comic lettering, large and very legible.
> - Dialogue in white oval balloons with tails pointing at the speaker.
> - The narrator, TOMBSTONE, never has balloons, only rectangular caption boxes (white fill, black border).
> - Speaker tags such as "— A DIGITAL BANK" are small caps tucked under the balloon.
> - Render every piece of text EXACTLY as written in the script, letter for letter. Add no other words. No logos or brand names anywhere. Screens, signs, papers and badges are blank or scribbled unless the script gives their text.
>
> WORLD
>
> - The University Club of San Francisco on Nob Hill: red-brick Italian Renaissance clubhouse, arched windows, deep dentil cornice, chimneys; cable cars on steep streets.
> - Dining room: dark beamed wooden ceiling, brass candle chandelier, tall windows with wooden louvred shutters and city lights at night, candle wall sconces, round tables with black tablecloths, wine glasses, carved high-backed wooden chairs, patterned carpet.
> - The Black Cat Bar: curved wooden bar with a brass foot rail, framed pictures on deep-toned walls, small brass lamps.
> - Detailed backgrounds in establishing panels; minimal backgrounds (a few lines or white space) in dialogue panels.
>
> CHARACTERS
>
> - TOMBSTONE (narrator): a plump, loaf-shaped black marble cat statue on the bar. Smooth rounded forms like a river stone, small rounded ears, solid black with one thin white highlight curve along its back, long tail curled around its body. Eyes: two white almond shapes with black slit pupils; dry, deadpan expression. When "alive", only eyes, ears and tail move, except when the script says it walks. Match the TOMBSTONE in the attached references exactly.
> - HOSTS (recognisable): ANKOR, RONNIE, NAMIT, SUKRUTH. Match the attached CAST SHEET exactly; same face, hair and costume every time.
> - GUESTS (anonymous): smart evening business wear. Invented faces that do NOT resemble the hosts, any reference photo or any real person. Vary age, gender, ethnicity and build. Identify them only by the role tag in the script.
>
> Image 1 is a photo of the real Black Cat Bar. The dark, chunky, rounded cat statue on the left end of the counter inspires our narrator, TOMBSTONE. Use the photo only for the cat's plump loaf shape and the bar. Do not copy any artwork on the walls, and add no people.
>
> Draw a character model sheet for TOMBSTONE on a white background, square, in the STYLE BIBLE's black-and-white brush-and-ink style. Seven small drawings, evenly spaced:
>
> 1. Sitting as a still statue on the curved wooden bar, eyes closed.
> 2. Same pose, eyes open, deadpan.
> 3. Eyes narrowed, suspicious.
> 4. Eyes wide, startled.
> 5. Alive, walking across a black tablecloth between wine glasses.
> 6. Looking straight out at the reader, one eyebrow-ish ear tilted.
> 7. Pure black silhouette.
>    Hand-letter "TOMBSTONE" at the top. No other text.

</details>

![](https://files.s-anand.net/blog/2026-11-07-convergence-comic-story/ref-01-cat-output.avif)

<details>
<summary><strong>1. Create a reference comic sheet</strong></summary>

![](https://files.s-anand.net/blog/2026-11-07-convergence-comic-story/ref-02-style-input.avif)

> PAGE 1 — Title bar: "THE CONVERGENCE ROOM • 1 • THE WITNESS". 2×2 grid.
>
> PANEL 1 (wide, flashback, wavy border): San Francisco in 1906 after the earthquake: collapsed brick buildings, smoke, a tilted streetlamp. A small black cat scurries out of a broken doorway.\
> CAPTION: "SAN FRANCISCO, 1906. THE EARTHQUAKE DIDN'T ASK ANYONE'S PERMISSION."
>
> PANEL 2 (medium): The same cat, now TOMBSTONE, a black marble statue sitting on the curved wooden bar of the Black Cat Bar, eyes closed, framed pictures and small brass lamps behind.\
> CAPTION: "LATER THEY CARVED ME IN BLACK MARBLE AND PUT ME ON A BAR. THE NAME'S TOMBSTONE."
>
> PANEL 3 (wide, exterior, night): The red-brick clubhouse on Nob Hill from the reference photo, arched windows glowing; a cable car passes; anonymous guests in evening wear climb the steps.\
> CAPTION: "TRADITION SAYS ANYTHING SAID BEHIND THE BLACK CAT IS OFF THE RECORD."
>
> PANEL 4 (close-up): TOMBSTONE's face fills the panel, eyes narrowed, tiny silhouettes of guests reflected in his glossy marble.\
> CAPTION: "ON 27 OCTOBER 2026, TWENTY LEADERS KEPT SAYING THE SAME THINGS. I'D NEVER HEARD THAT BEFORE."
>
> Strict black ink on white. Text exactly as written; no other text.

</details>

![](https://files.s-anand.net/blog/2026-11-07-convergence-comic-story/ref-02-style-output.avif)

<details>
<summary><strong>3. Create comic styles for each person</strong></summary>

![](https://files.s-anand.net/blog/2026-11-07-convergence-comic-story/ref-03-ankor-input.avif)

> Character model sheet for ANKOR, one of the four recognisable hosts in this comic.\
> Image 1 is the STYLE KEY: match its ink style, line weight and lettering exactly.\
> Image 2 is a photo of ANKOR: use it only for his likeness.
>
> Draw ANKOR in the STYLE KEY’s black-and-white brush-and-ink style, on a white background, square:\
> (a) front head-and-shoulders, neutral; (b) three-quarter view, mid-sentence, one hand gesturing; (c) full figure standing, holding a wine glass; (d) close-up, laughing.\
> Keep the features that make him recognisable in the photo: slim face, short dark side-parted hair, clean-shaven, calm expression.\
> Costume for the whole comic: solid-black suit, white open-collar shirt, no tie.\
> Hand-letter "ANKOR" under the drawings. No other text.

</details>

![](https://files.s-anand.net/blog/2026-11-07-convergence-comic-story/ref-03-ankor-output.avif)

### Step 4: Generate and correct the images

<!-- https://chatgpt.com/g/g-p-6ae3898e99408191b5e60ee7b60be758-convergence-comic/c/6ae39480-1154-83ec-8de8-0e32db8f477d -->

This is a slow process. For each comic page, it gave me a generation prompt and a verification prompt. For example:

<details>
<summary><strong>Here's the page 2 generation prompt</strong></summary>

> PAGE 2 — Title bar: "THE CONVERGENCE ROOM • 2 • STEAK, FISH OR VEGETARIAN". 2×2 grid.
>
> PANEL 1 (medium): ANKOR stands at the head of the dining room holding a wine glass, relaxed, guests at round tables listening. The walls behind him are bare: no logos.\
> ANKOR: "NO LOGOS ON THE WALLS TONIGHT. JUST DINNER, WINE, AND WHAT YOU'RE ACTUALLY SEEING."\
> TAG: "— ANKOR, HOST"
>
> PANEL 2 (medium close): RONNIE standing, hands open, mid-sentence, a slight knowing smile.\
> RONNIE: "PEOPLE DON'T RESIST CHANGE. THEY RESIST BEING CHANGED."\
> TAG: "— RONNIE, MODERATOR"
>
> PANEL 3 (close-up, top-down): A small printed menu card on the black tablecloth beside a wine glass. The card reads, exactly, as five short lines:\
> "TONIGHT'S MENU"\
> "STEAK: WHAT DOES 'VALUE' MEAN TO YOU?"\
> "FISH: EFFICIENCY, OR A BETTER CUSTOMER EXPERIENCE?"\
> "VEGETARIAN: WHAT'S STOPPING YOU FROM SCALING?"\
> "SIDES: ONE THING IN, ONE THING OUT."\
> CAPTION: "PICK ONE QUESTION, LIKE A MAIN COURSE."
>
> PANEL 4 (medium, comic beat): A waiter approaches with a tray of covered plates; an anonymous guest at the table blocks him with a raised palm. TOMBSTONE watches from the bar in the corner, deadpan.\
> GUEST: "NOT UNTIL EVERYONE HAS SPOKEN!"\
> CAPTION: "ONE GUEST WENT TO WAR WITH THE KITCHEN. THE KITCHEN BLINKED."
>
> Strict black ink on white; hosts match the CAST SHEET. Text exactly as written.

</details>

![](https://files.s-anand.net/blog/2026-11-07-convergence-comic-story/wip-02-v1.avif)

<details>
<summary><strong>Here's the verification prompt</strong></summary>

> Proofread the image you just made against my script for this page. List every balloon, caption, tag or sign whose text differs by even one character, any extra text or logo, any colour, any host who doesn't match the CAST SHEET, and any guest who looks like a host. Don't regenerate yet.

</details>

It turns out that the image DOES have a major issue. According to the review, the waiter in Panel 4 looks rather like Ankor, and fixing that is the highest priority correction.

Now, **reading every verification report is painful**. So I told Codex:

<!-- https://github.com/sanand0/convergence-event-comic/blob/11934a6ef3b7295dc5348564108c44129f0e190f/prompt-exec.md#run-on-chatgpt-29-oct-2026 -->

> I'm following the instructions from prompts.md and have roughly completed up to step C2.
>
> Continue and complete the rest. The tab is open on the browser.

Now _this_ was genius, because Codex read ChatGPT's output, send this follow-up prompt:

> Edit only panel 4 of page 2: make the waiter a distinct anonymous older woman, not resembling Ankor or any host. Preserve the tray, scene, all lettering and every other panel unchanged.

... and then:

- Ran the verification prompt again (2 minutes)
- Read it, was satisfied
- Moved to generating the cover page (3-5 minutes)
- Ran the verification prompt (2 minutes)
- Read it, and asked ChatGPT to remove the lettering and logos on bottle labels (3-5 minutes)
- ... and so on.

I asked it to run in parallel across four chats. So, while I was reading Asterix, [an entire comic story was built](https://files.s-anand.net/blog/2026-11-07-convergence-comic-story/).

[![](https://files.s-anand.net/blog/2026-11-07-convergence-comic-story/00-cover.avif)](https://files.s-anand.net/blog/2026-11-07-convergence-comic-story/)

---

Basically:

1. Claude wrote the prompts.
2. ChatGPT ran the prompts.
3. Codex got ChatGPT to run the prompts.
4. I read Asterix and worked on other things.
