---
title: Statistically improbable phrases
date: "2006-08-23T12:00:00Z"
categories:
  - how-i-do-things
wp_id: 252
---

**Calvin and Hobbes has some recurrent themes**, like [Hobbes pouncing](http://calvinethobbes.free.fr/english/c_home.html), [snow art](http://www.angelfire.com/wa/zzaran/calvin.html), [polls](http://calvinethobbes.free.fr/english/c_elections.html), [letters to Santa](http://calvinethobbes.free.fr/english/c_santa.html), ...

Over the last 5 years, I've transcribed the [Calvin and Hobbes](/calvin/) comics, and tagged them manually by theme. But **can I generate themes automatically?**

One way is to use Amazon's [statistically improbable phrases](http://www.amazon.com/gp/search-inside/sipshelp.html). It's a list of words that occur a lot in a book, but rarely occur in others. It gives you a good feel of what topics the book is about.

Here's how I did it:

1. **Transcribe Calvin & Hobbes**. This is 99% of the work.
2. **Make a C&H word list**. Just join all the words in Calvin and Hobbes. (Be careful about punctuation, and colloquialisms like "dunno", "leggo", etc.)
3. **Get an English corpus**. That is, get a big list of words in normally occurring text. I have some e-books, and I picked 23 megabytes worth of these as my corpus.
4. **Compare the word frequency in C&H with the corpus**. That is, compare the % of occurrences of a word in Calvin and Hobbes versus the corpus.
5. **Display those with significantly higher frequency in C&H**.

The list below has common Calvin & Hobbes words occurring 10 times as often as in normal text. It's incredible how closely it relates to most of the themes.

(Big words occur more often. Dark words are more improbable.)

---

allowance assignment babe balloon bat bath beanie bedtime bee beep bet bike blaster boring bug bus butter calvin calvinball cartoon cent cereal cheat chew chocolate click comic cookie crunch dad dame derkins dictator-for-life dinosaur disgusting doll doomed dumb duplicate earthling explorer fang fearless ferocious flip flush frog frosted fun fuzzy genius goggle goodness goon grade gross grown-up gum hack hamburger hamster hate hero hideous hobbes homework huey insect invent jelly jerk jurassic kid leaf loot martian math mild-mannered mom monster moron motto munch mushy nickel oatmeal ouija pant peanut perspective pit playground poll porridge poster quiz recess rosalyn rotten rub sandwich santa scary sculpture scum shovel
sissy sitter sled slimy slug slushball sniff snow snowball snowman soak spaceman spiff splash spoil sport squirt steer sting stuffed stupendous sugar susie tickle tiger toy transmogrifier transmogrify tub tuna twinky tyrannosaur underwear vacation weird wham whiff worm wormwood

---

**Summary**: "Statistically improbable phrases" are a powerful tool for text analysis. You can apply it on any content and figure out what topics it talks about.

**Update**: Technically, these are "Statistically improbable WORDS", not phrases. So I [re-did this analysis using phrases instead of words](/blog/statistically-improbable-phrases-2/).

---

## Comments

<!-- wp-comments-start -->

- **DMac** _23 Aug 2006 12:00 pm_:
  This is great. Can you be more specific on how you did this? You say that the words listed are "common" words that appear more than 10 times more often - what is your criterion for "common"? Also, what were the ranges of improbability and oftenness that you mapped into the size and color of the results. How are improbability and oftenness different, anyway? Finally, how did you handle any words in C&H that didn''t appear in your corpus? I''m very interested in hearing more from you about how you did this - I''m looking forward to hearing from you. Best regards...
- **Mugen** _15 Sep 2010 4:33 pm_:
  Any further directions to how exactly you came up with this/whether you used any software would be most helpful. Please tell us more about this. This is going to be awesome to help decide what to read. Thanks a load.
  Also, does amazon have this feature for most books? I browsed a lot of books in amazon but was only able to find this in one so far.

<!-- wp-comments-end -->
