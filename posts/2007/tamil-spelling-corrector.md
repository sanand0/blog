---
title: Tamil spelling corrector
date: "2007-05-01T12:00:00Z"
categories:
  - how-i-do-things
wp_id: 87
---

The Internet has a lot of tamil song lyrics in English. Finding them is not easy, though. Two problems. The lyrics are fragmented: there's no one site to search them. And Google doesn't help. It doesn't know that alaipaayudhe, alaipaayuthe and alaipayuthey are the same word.

This is similar to the problem I faced with [tamil audio](/blog/hindi-songs-online/). The solution, as before, is to make an index, and provide a search interface that is tolerant of English spellings of Tamil words. But I want to go a step further. **Is it possible to display these lyrics in Tamil?**

My [Tamil Transliterator](/Tamil_transliterator.html) does a lousy job of this. Though it's tolerant of mistakes, it's ignorant of spelling and grammer. So,

> kanda nal muthalai kathal peruguthadi

... becomes...

> kanda nal muthalai kathal peruguthadi

... when in fact we want...

> kanda naaL muthalaay kaathal peruguthadi

(If you're viewing this on an RSS reader, check [my post](/blog/tamil-spelling-corrector/) to see what I mean.)

I need an automated Tamil spelling corrector. Reading [Peter Norvig's "How to Write a Spelling Corrector"](http://www.norvig.com/spell-correct.html) and actually having understood it, I gave spelling correction in Tamil a shot.

Norvig's approach, in simple terms, is this:

1. Get a dictionary
2. Tweak the word you want to check (add a letter, delete one, swap 2 letters, etc.)
3. Pick all tweaks that get you to a valid word on the dictionary
4. Choose the most likely correction (most common correct word, adjusted for the probability of that mistake happening)

Making a dictionary is easy. I just need lots of Tamil literature, and then I pick out words from it. For now, I'm just using the texts in [Project Madurai](http://www.tamil.net/projectmadurai).

Tweaking the word to check is easy. Norvig's article has a working code example.

Picking valid tweaks is easy. Just check against the dictionary.

The tough part is choosing the likely correction. For each valid word, I need the probability of having made this particular error.

Let's take an example. I've spelt kathal. A list of valid tweaks to this word include: kal, kol, kadal, kanal, and kaadhal. For each of these, I need to figure out how often the valid tweaks occur, and the probability that I typed kathal when I really meant one of these tweaks. This is what such a calculation would look like:

| Tweak   | Frequency | Probability of typing kathal | Product |
| ------- | --------- | ---------------------------- | ------- |
| kal     | 1         | 0.04                         | 0.04    |
| kol     | 4         | 0.02                         | 0.08    |
| kadal   | 10        | 0.1                          | 1.0     |
| kanal   | 1         | 0.01                         | 0.01    |
| kaadhal | 6         | 0.25                         | 1.50    |

Once we have this, we can see that kaadhal is the right one -- it has the maximum value (1.50) in the last column, where we multiply the frequency and the probability.

(You probably realise how small my dictionary is, looking at the frequencies. Well, that's how big [Project Madurai](http://www.tamil.net/projectmadurai) is. But increasing the size of a dictionary is a trivial problem.)

Anyway, getting the frequency is easy. How do I get the probabilities, though? That's what I'm working on right now.

---

## Comments

<!-- wp-comments-start -->

- **SDW** _1 May 2007 9:01 am_:
  Hi there, with regards to 'Thendral Ennai Mutham Itathu' as described on http://www.s-anand.net/blog/classical-ilayaraja/, the female voice was not SPS but B.S. Sasirekha. fyi please.
- **ரவிசங்கர்** _4 May 2007 5:33 pm_:
  நல்ல முயற்சி, அணுகுமுறை.
- **Ravi** _11 May 2007 2:36 pm_:
  Good article. I am very interested in text analysis, phrase extraction too (and statistical machine translation, if you will :) Is not probability just the number of occurences of each of these divided by total number of occurence? Maybe I am missing something. Did you also consider using Vikatan or Kumudam article data in addition to Project Madurai to get contemporary word counts and probabilities? It is one of my projects to create a word frequency list for Tamil. Now that I see another active soul, I might start the project :) Python or ruby I am wondering...
- **kooliip** _1 May 2007 12:00 pm_:
  meaning for saroja sama nikalo
- **GANESH** _1 May 2007 12:00 pm_:
  I LOVE YOU SUJA CHELLAM
- **hajaroz@yahoo.com** _1 May 2007 12:00 pm_:
  please give me that spelling checking software....it is very good and it is new one
- **v.arul** _14 Aug 2008 6:39 am_:
  Give me the correct tamil spelling for unnippaga
- **shamu** _10 Sep 2008 12:17 am_:
  தமிழ்லில் எழுதுவதற்கு முய்ற்சி\
  ந்ன்றி
- **nita** _29 Dec 2009 3:39 pm_:
  hi i would like to know if there are any resources online which would help me to check if my spellings in tamil typing are right? i am not very confortable with tamil so i can use the help of spell check, i would be most greatful! kindly help, thanks:)
- **prabhu** _13 Aug 2011 8:43 am_:
  Hi anand,
  Do you have any tamil spell checker tool online. If yes, please provide the link asap. Thanks in advance.
- **thamizh selvan** _19 Mar 2011 4:09 pm_:
  i want to know the exact spelling of thamizh selvan in tamil . whether a connecting letter will come between thamizh and selvan or not .. thank you
- **chandroo** _19 Aug 2012 6:02 am_:
  I need a Tamil spell checking software.Please tell me.
- **saranraj** _1 Jan 2013 9:00 am_:
  Please let me know the correct spelling for the tamil word "Nadathanum".
- **[Muthu](https://github.com/arcturusannamalai/open-tamil)** _29 Apr 2015 5:37 am_:
  You may do easy text processing of Tamil content using open-tamil library in Python.
  $ pip install open-tamil
  To convert your data into Tamil letters (not Unicode code-points) you can type in Python,
  >> import tamil
  >> letters = tamil.utf8.get\_letters( data )
  >> Thanks,
  >> -Muthu

<!-- wp-comments-end -->
