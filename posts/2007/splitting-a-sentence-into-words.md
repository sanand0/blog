---
title: Splitting a sentence into words
date: "2007-04-26T12:00:00Z"
categories:
  - how-i-do-things
wp_id: 89
---

I often need to extract words out of sentences. It's one of the things I used to build the [Statistically Improbable Phrases for Calvin and Hobbes](/blog/statistically-improbable-phrases-2/). But splitting a sentence into words isn't as easy as you think.

Think about it. **What is a word**?

Something that has spaces around it? OK, let's start with the simplest way to get words: **split by spaces**. Consider this piece:

```text
"I'd look at McDonald's," he said.
"They sell over 3,000,000 burgers a day -- at $1.50 each."
High-fat foods were the rage. For e.g., margins in fries
were over 50%... and (except for R&M & Dyana [sic]) everyone
was at ~30% net margin; growing at 25% too!
```

Splitting this by spaces (consider new lines, tabs, etc as spaces too.), we get the following:

```text
"I'd
look
at
McDonald's,"
...
```

Now, some of these like "I'd" are words. But "McDonald's" isn't. I mean, there's a full-stop and a double-quotes at the end. Clearly we need to remove the punctuation as well. But, if we do that, `I'd` becomes `Id`. So we need to be careful about which punctuation to remove. Let's take a closer look.

The following punctuation marks are **clear word separators**: spaces, the exclamation mark, the question mark, semicolon, brackets of any kind, and double-quotes (not single quotes). No word has these in the middle. If we use these as separators, our list of words is better, but we still have some words with punctuation:

```text
McDonald's,
e.g.,
High-fat
R&M
...
```

The issue is, these punctuation marks are **ambiguous word separators**: comma, hyphen, single-quote, ampersand, period and slash. These usually separate words, but there are exceptions:

- **Comma**: Not inside numbers: 3,000,000.
- **Hyphen**: Not for hyphenated words: High-fat.
- **Single-quote**: Not for possessives: McDonald's. Not for joint words: I'd.
- **Ampersand**: Not for abbreviations: R&M
- **Period**: Not for abbreviations: O.K. Not for URLs: www.s-anand.net
- **Slash**: Not for fractions: 3/4. Not for URLs: google.com/search

Colon is ambiguous too. In normal English usage, it would be a separator. But URLs like http://www.s-anand.net/ use these characters, and it doesn't make sense to separate them.

So here are my current rules for splitting a sentence into words. (It's a [Perl regular expression](http://www.perl.com/doc/manual/html/pod/perlre.html). Don't worry. [Cooper's Law](http://forums.speedguide.net/showthread.php?t=166822): If you do not understand a particular word in a piece of technical writing, ignore it. The piece will make perfect sense without it.)

```bash
# Split by clear word separators
/       [\s \! \? \;\(\)\[\]\{\}\<\> " ]
 
# ... by COMMA, unless it has numbers on both sides: 3,000,000
|       (?<=\D) ,
|       , (?=\D)
 
# ... by FULL-STOP, SINGLE-QUOTE, HYPHEN, AMPERSAND, unless it has a letter on both sides
|       (?<=\W) [\.\-\&]
|       [\.\-\&] (?=\W)
 
# ... by QUOTE, unless it follows a letter (e.g. McDonald's, Holmes')
|       (?<=\W) [']
 
# ... by SLASH, if it has spaces on at least one side. (URLs shouldn't be split)
|       \s \/
|       \/ \s
 
# ... by COLON, unless it's a URL or a time (11:30am for e.g.)
|       \:(?!\/\/|\d)
/x;
```

This doesn't even scratch the surface of the issue, though. Here are some issues:

- Lots of files **split words** into two at the end of a line. How do we handle that?
- How do we handle **incorrect punctuation**? For instance, if someone types "done.Yet," without leaving a space after the full-stop, I'll think it's an abbreviation.
- What about **other separators**? Like the ± symbol or the £ symbol for instance.
- What about **other languages**?!

And you thought it was easy!

---

## Comments

<!-- wp-comments-start -->

- **Kasi** _27 Apr 2007 10:18 pm_:
  Hi Anand, Nice site..It was good talking to you! When u find time, pls do visit my humble less visited blog at www.raconteurkasi.blogspot.com !
- **Ramya** _3 May 2007 7:52 am_:
  Hi Anand, Can u guide me through the interview process of INSEAD MBA . Can you share your wisdom with me to crack the interview, and one more question .. do u sleep for less than 5 hrs a day ?
- **Andrew** _26 Apr 2007 12:00 pm_:
  Thanks, this is very helpful.

<!-- wp-comments-end -->
