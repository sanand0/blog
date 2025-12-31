---
title: Jolie No. 1
date: "2021-02-13T16:28:49Z"
lastmod: "2022-02-02T09:55:48Z"
categories:
  - data
  - how-i-do-things
wp_id: 3087
---

![Jolie No. 1](/blog/assets/jolie-no-1.webp)

There are [more Bollywood actors in Hollywood](https://theculturetrip.com/asia/india/articles/the-10-most-famous-indian-actors-in-hollywood/). Some are even [turning down Hollywood roles](https://www.msn.com/en-in/entertainment/bollywood/bollywood-stars-who-turned-down-huge-hollywood-roles/ss-BBB0rhm).

So we wondered: ****How easily can a [Bollywood actor](https://en.wikipedia.org/wiki/Bollywood) connect to a [Hollywood actor](https://en.wikipedia.org/wiki/Hollywood)?****

As part of the Oct 2019 [Gramener data story hackathon](https://www.meetup.com/meetup-group-EkjzkhLt/events/mwdhfryznbpb/), [Anand](https://www.linkedin.com/in/sanand0/), [Kishore](https://www.hackerrank.com/profile/kishmys61), and [Niyas](https://www.linkedin.com/in/mohammedniyasp/) created a [Jolie No 1](https://youtu.be/lcwMsPxPIjc) — a data video where [Govinda](https://en.wikipedia.org/wiki/Govinda_(actor) announces (in our imagination) that he will act with [Angelina Jolie](https://en.wikipedia.org/wiki/Angelina_Jolie) in **Jolie No 1**, but declines to comment on who introduced them.

<div class="video-embed"><iframe src="https://www.youtube.com/embed/lcwMsPxPIjc" title="YouTube video" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

## We picked a theme first

The hackathon theme was "movies". We explored 5 themes:

1. Who acts most in cameo roles, and what's the impact on revenue? (Based on [The Numbers](https://www.the-numbers.com/box-office-star-records/worldwide/lifetime-acting/top-grossing-cameo-stars))
2. Which actors acted often together? (Based on [IMDb data](https://www.imdb.com/interfaces/))
3. Which movies become hits on TV? (Based on BARC TV data)
4. What is the social network of actors in individual movies (<https://www.xkcd.com/657/>)
5. Correlation of TV series actors and their revenues

## We explored insights next

We picked the first two themes because we liked them.

### 1. Cameo appearances

Some observations were:

- Stan Lee starred in 45 cameo roles. No one even comes close. Some roles are:
  - A school bus driver in Avengers: Infinity War (2018)
  - A strip club DJ in Deadpool (2016)
  - A hot-dog vendor in X-Men (1995)
- Jay Leno (25) and Larry King (21) follow, mostly starring as themselves
- Alfred Hitchcock (16) has famous cameo appearances in most of his films, such as:
  - Man mailing letter in Suspicion (1941)
  - Man winding the clock in Rear Window (1954)
  - Man walking the docs in The Birds (1963)

We didn't have **inflation-adjusted** box-office revenues, so we couldn't compare the revenues.

### 2. Which actors acted often together

Some observations were:

- Top hero-heroine combo:
  - Overall: Prem Nazir & Jayabharati
  - Hollywood: Billy Dee & Mike Horner (pornstars)
  - Tollywood: Krishna Ghattamaneni & Jaya Prada
  - Bollywood: Jeetendra & Rekha
- Top male combo: Sivaji Ganesan & Nagesh (more recently, Senthil & Goundamani)
- Top female combination: Lalitha & Padmini
- Top pair of:
  - Shah Rukh Khan: Rani Mukherji
  - Amitabh Bachchan: Hema Malini
  - Kamal Haasan: Sridevi
  - Rajinikanth: Sridevi
  - Sridevi: Krishna Ghattamaneni
  - Chiranjeevi: Vijayshanti
  - Dev Anand: Madhubala

The observations focus on Bollywood and Hollywood (because of our familiarity) -- but there are number of insights on Japanese and French films too.

We decided to go with this theme because it offered multiple storylines:

- Some actors pair up with each other, e.g. [Gemini](https://www.imdb.com/name/nm0304261/) - [Savithri](https://www.imdb.com/name/nm0767800/)
- Some actors have a big "following" e.g. [Rajinikanth](https://www.imdb.com/name/nm0707425/), [Kamal Hassan](https://www.imdb.com/name/nm0352032/), [Jitendra](https://www.imdb.com/name/nm0420090/) have acted most with [Sridevi](https://www.imdb.com/name/nm0004437/)
- Some actors form cliques -- working only with each other
- Often, comedians are the bridge between cliques
- It's interesting to see how actors from one clique can connect to another

## Creating the storyline

When exploring of [actors' connections](https://kumu.io/sanand0/actor-pairs), we found a clearly delineated network structure.

![Actor SNA](https://files.s-anand.net/images/2021-02-13-jolie-no-1-sna.gif)

The group of densely clustered actors is the Bollywood-Tollywood-Mollywood-Kollywood nexus. It appears disconnected from the Hollywood cluster. (We excluded anyone who hadn't acted together in at least 4 films.)

The [data was created using this Jupyter notebook](https://github.com/sanand0/jolie-no-1/blob/master/imdb-actor-pairing.ipynb).

We realized that it's tough for someone in Bollywood to connect to Hollywood. Maybe that could be the plot? For example, what if [Amitabh Bachchan](https://www.imdb.com/name/nm0000821/) wants to act with [Metryl Streep](https://www.imdb.com/name/nm0000658/)?

But this isn't an **interesting** story. So we asked:

- Who is the most desirable heroine in Hollywood? Our guess was [Angelina Jolie](https://www.imdb.com/name/nm0001401/)
- Who would make funny co-actor? We toggled between [Rajanikanth](https://www.imdb.com/name/nm0707425/), [Brahmanandam](https://www.imdb.com/name/nm0103977/), and finally picked [Govinda](https://www.imdb.com/name/nm0332871/).

The plot summary was: **Govinda wants to act with Angelina Jolie. Who can connect them?**

The [analysis is in this Jupyter notebook](https://github.com/sanand0/jolie-no-1/blob/master/shortest-path.ipynb).

## Write the screenplay

The morning of the hackathon was spent finalizing the screenplay and dialogues, written on Dropbox Paper.

```sql
CUT TO:
    - Video of Govinda "declining James Cameron's Avatar" on Aap Ki Adalat
    - Niyas: On July 29, 2019, Govinda announces he declined a role in Avatar.
    - Video: https://youtu.be/NyFF18a7e-Y
    - Picture: https://twitter.com/mohan_rajkeshav/status/1156148768049262592

CUT TO:
    - Visual: Show an interview video of Govinda and of Angelina
    - Niyas: Today, he announced his next film with Angelina Jolie.
             A “close friend” connected them, but didn't say who.
    - Kishore: Who is this close friend? Why is he not naming them?
    - Video: https://youtu.be/NyFF18a7e-Y (Govinda)
    - Video: https://youtu.be/JNrH1W7aKc8 (Angelina)

CUT TO:
    - Visual: Show the top 8 heroines Govinda has acted with.
              Visualize this data with animation.
              One option is to have Govinda’s pic in the center,
              and have each of these 9 heroine’s images appear around him
              as a circle, with the number of pictures in a link.
              Or as the inverse link distance (e.g. 11 is closest)

    11 Neelam Kothari
    10 Kimi Katkar
    10 Karisma Kapoor
     9 Raveena Tandon
     9 Farha Naaz
     8 Juhi Chawla
     6 Anita Raj
     6 Mandakini
     5 Shilpa Shetty Kundra

    - Niyas: Maybe it’s because it’s one of his heroines?
             He’s mostly acted with Neelam, Kimi and Karishma.
             But none of them has acted with any Hollywood actor.

MORPH TO:
    - Visual: Add these actors with pics to the same visual,
              but clearly differentiated by gender. Also add their names.

    22 Shakti Kapoor
    18 Kader Khan
    13 Gulshan Grover
     9 Anupam Kher
     8 Dharmendra
     7 Johnny Lever
     6 Sadashiv Amrapurkar
     6 Vikas Anand
     6 Sanjay Dutt
     6 Prem Chopra
     6 Asrani

    - Kishore: So maybe this “close friend” is a male actor?
    - Niyas: He’s acted with Gulshan Grover, Kader Khan and Shakti Kapoor a lot.
    - Kishore: Shakti Kapoor is practically his boyfriend!

MORPH TO:
    - Visual: Zoom into Gulshan Grover and Anupam Kher.
              Build a network of film posters around them
              with their Hollywood films (max 2-4)
        - Anupam Kher
            - Bend It Like Beckham
            - Lust & Caution
            - Silver Linings Playbook
            - A Family Man
        - Gulshan Grover
            - Prisoners of the Sun
            - The Second Jungle Book
            - Marigold
            - Monsoon
    - Niyas: Gulshan Grover and Anupam Kher have acted in a number of Hollywood films
    - Kishore: But have they acted with Angelina Jolie?
    - Niyas: No, never with Angelina Jolie.
    - Kishore: But what if any of them connected him to someone who connected him to Angelina?

CUT TO:
    - Visual: Show Angelina Jolie with ~100 actors around her. Highlight the following:
        - Jack Black, 3
        - Dustin Hoffman, 3
        - Giovanni Ribisi, 2
        - Robert De Niro, 2
        - Brad Pitt, 2
        - Elle Fanning, 2
        - Bryan Cranston, 2
        - 92 other actors with only 1 film each
        - Highlight Irrfan Khan — A Mighty Heart
    - Niyas: Angelina Jolie has acted with less than 100 actors.
             Dustin Hoffman and Jack Black, mostly.
             Only one of them is an Indian actor: Irrfan Khan

MORPH TO:
    - Visual: Expand the connection between Angelina and Irrfan
    - Kishore: So, Govinda needs to connect to Irrfan Khan somehow.

MORPH TO:
    - Visual: Connect Govinda to Irrfan Khan via
        - Gulshan Grover via Knock Out
        - Sanjay Dutt via Knock Out
        - Tabu via Saajan Chale Sasural, Dil Ne Phir Yaad Kiya (and 2 others)   \
    - Niyas: That should be easy.
             Gulshan Grover and Irrfan Khan have acted together in Knock Out.
             So has Sanjay Dutt.
             But Tabu will be a better option. Govinda and Irrfan Khan have acted with her in 4 movies each.

MORPH TO:
    - Visual: Show path from Govinda to Tabu to Irrfan to Angelina.
    - Kishore: Then, Govinda must have connected to Tabu
               who introduced him to Irrfan Khan,
               who in turn connected him with Angelina Jolie.
```

## Create the video

Anand and Niyas created the visuals on PowerPoint, collaborating on [Dropbox](https://www.dropbox.com/sh/oadjwv25vsr8qao/AACLz5xskiuydrx-a3GQErIHa).

This is the [first version of the presentation](https://www.dropbox.com/sh/oadjwv25vsr8qao/AADev1ywteX8ucnfoV1cbtlra/Govinda-and-Angelina.pptx). It uses [morph transitions](https://support.office.com/en-us/article/Use-the-Morph-transition-in-PowerPoint-8DD1C7B2-B935-44F5-A74C-741D8D9244EA) extensively.

![PPT screenshot](https://files.s-anand.net/images/2021-02-13-jolie-no-1-powerpoint.webp)

Niyas and Kishore recorded the audio in [two](https://www.dropbox.com/sh/oadjwv25vsr8qao/AADpskAelLq1ZY5GsPLuLPY9a/WhatsApp%20Audio%202019-10-11%20at%2012.15.57%20PM.aac) [parts](https://www.dropbox.com/sh/oadjwv25vsr8qao/AADZ5AJB2opDhVZmak586NRIa/WhatsApp%20Audio%202019-10-11%20at%2012.51.58%20PM.aac) on their phone, shared it with Anand via WhatsApp.

We integrated these using the [Windows 10 video editor](https://support.microsoft.com/en-us/help/4051785/windows-10-create-or-edit-video). It's simple, but now powerful. For our use, simplicity was more important.

The process took 6 hours (from 8 am to 2 pm).

- Writing the screenplay and dialogues: 1.5 hours
- Creating the presentation: 2 hours
- Recording the audio: 1 hour
- Integrating into the video: 1.5 hours

At the last minute, we picked the title "Jolie No. 1" as a parody of Govinda's [No. 1 film series](https://en.wikipedia.org/wiki/No._1_(film_series)).

We published this on Google Drive, and then on [YouTube](https://youtu.be/lcwMsPxPIjc).
