---
title: Automated resume filtering
date: "2006-10-03T12:00:00Z"
categories:
  - how-i-do-things
wp_id: 195
---

I had to screen resumes from a leading MBA school. I'm lazy, and there were hundreds of CVs. So after [procrastinating](http://paulgraham.com/procrastination.html) until this morning, I decided on 2 principles:

1. I will not spend more than 45 minutes on this. (That's the duration of my train ride to office.)
2. I will not read a single CV. (I would write a program.)

The CVs were in a single PDF file. I saved it as text (it shrunk from 66MB to 1.6MB without the photos). Then I wrote a Perl **program to filter CVs by keywords**. We were looking for people with an interest and/or experience in IT consulting, so I picked "technology", "consulting", "SAP", "IBM", "Accenture", "Deloitte", etc.

**Anyone without these keywords would fall out of the list**. This eliminated 75% of the crowd. But since I didn't want to read the rest, I used my favourite text-analysis technique: [concordance](/blog/assets/flickr-concordance_259769212_o-gif.webp). I extracted 3 words on either side of each keywords, and just read those. It was easy to see who'd "worked with suppliers like IBM" as opposed to who'd worked at IBM.

That's it! I managed to cut the list down to 10%. Better yet, I also had a preference ranking. People with multiple keywords ranked higher than those with fewer keywords. And all this took little more than my train ride to office.

I can see this going to the next level. It's **easy to write a customised rejection letter**, depending on which keywords are missing for each person.

Now, if it's this easy to filter resumes, I can see every organisation do it in a few years. Which means, **you need to write resumes for machines** as well, not just for humans! For example, on my next CV, I'll make sure I include the words "Boston Consulting Group" as well as "BCG" -- just in case the software searches for only one of those keywords. Further, I'll make sure I avoid spelling mistakes!

---

## Comments

<!-- wp-comments-start -->

- **Siddharth Nagpal** _3 Oct 2006 9:17 pm_:
  How rational it is to screen CVs, like this..instead if u cud hv glanced thru CVs..then taken a decision it wud hv been lot more intelligent..than writing a search program..
- **S Anand** _4 Oct 2006 6:44 am_:
  When I manually scan CVs, **I miss out a lot of keywords** that I want to spot -- simply because humans are not good at scanning accurately. For example, when searching for SAP in the CVs, I missed it in half the CVs **that the program had told me had SAP** -- and I initially thought my program was wrong. Contrawise, **programs don't look for synonyms or abbreviations**. So I need to make sure the keywords are accurate -- otherwise I miss out on potential candidates. So there's flaws in both approaches, but they're complementary. Meaning, what you miss in one, you catch out on another. Since another colleague is doing the manual scanning, my using a program helps, I think.
- **Kaviraj Nair** _4 Oct 2006 9:31 am_:
  but I am sure you wanted to spend more than 45 minutes to decide the fate of those students!! no offence!! what say you??
- **S Anand** _4 Oct 2006 10:51 am_:
  They haven't started applying to us yet. We're just fishing around for good candidates ourselves. So if it's anyone's loss, it's ours. If anyone applies, the CV is read and that's a separate process. This is, like I said, proactive fishing.\
  Also, I don't feel bad about it being 45 minutes: if I'd run through the CVs manually, I'd have taken 3-4 hours at least for the same quality!\
  Sorry -- guess I'm not being too considerate here :(
- **Sudheer** _4 Oct 2006 4:46 pm_:
  Hi Anand, Being an ex-placecommer from ur alma mater... I can assure you that students/prospects looking for a job are always a couple of steps ahead of the firms... Simply because students have much more to lose/gain than corporates...
- **Sudheer** _4 Oct 2006 4:51 pm_:
  What I am saying is that such programs/ algos might not yield most honest results. Even though I accept your effort - returns calculation - It just supports my argument that corporates have less to lose/gain in the recruitment process
- **S Anand** _4 Oct 2006 5:09 pm_:
  Sudheer, I agree: students have more to lose. I see resume-filtering software becoming more popular. I know Google uses it as a process. BCG automates much of its screening using Excel. I'm sure it's going to be more popular. I do hope students stay ahead. I wonder what tecniques will help, though. I suspect very different strategies will be required for machines -- sort-of like search engine optimisation.
- **Sai** _4 Oct 2006 7:42 pm_:
  You really have to be extensive in your 'keyword' list don't you? And any use for fuzzy logic here? For example somebody who has package implementation experience can quickly ramp up an learn other packages? Same for analyst kind of jobs - technology is probably the least important of the factors - what matters is the vertical industry knowledge. My 2 cents!
- **S Anand** _4 Oct 2006 9:01 pm_:
  Sai, you're right, the keywords have to be broad. I did use some pattern matching (for e.g, when looking for banking experience, using patterns like bank\*; using synonyms like financ\*, insur\*; using abbreviations like FS, etc.) The things is, once I match and get snippets around the words, I can read the words and get the context. That's practically the equivalent of my software telling me where to read on the CV. Then I make a judgement call. But you're right about this example. I looked for SAP and ignored other packages. Will add a few more keywords and re-run it. Thanks!
- **ND** _5 Oct 2006 5:35 am_:
  Like your blog :-). I get "screened" resumes and 75% are irrelevant! For e.g. When I want Mercury ITG profiles, I get is Mercury QC profiles. I sift through "screened" resumes useing Edit-Find option in MS Word often using more verbs (both present and past tense) than nouns. I spend 10-15 minutes on identifying these "keywords". MS Word takes me to the spot on the doc and I read around. I don't get more than 50 "screened" resumes and all are .doc files. And I open upto 12 docs at a time without a system crash. Don't mind some Type 1 error as long as Type 2 error is minimized!
- **S Anand** _5 Oct 2006 5:59 am_:
  I know what you mean, ND. And my guess is, this is how it's done in many places. I can't believe everyone reads through every word of every CV. Yet so many students indignantly object to this reality!
- **Sathya** _5 Oct 2006 9:37 am_:
  Perhaps a tip for resume writes ... have a keyword section and put all the keywords out there -like the one u have in th "Contact" section. Putting all the keywords in the context of the CV might bloat up the size of CV.
- **S Anand** _6 Oct 2006 6:18 am_:
  That would work Sathya, but perhaps look a little awkward. Maybe a smarter thing to do is to prepare a keyword list, and **ensure that's woven into the text**.
- **sathya** _6 Oct 2006 12:42 pm_:
  May be looks odd to the humans ... but not so for machines :-) It could be made to look less awkward by making it a tag cloud. That would also indicate the comfort/expertise level (relatively). Is there a way to mark certain sections in word doc that appears when opened but does not get printed ??
- **Nitu Agarwal** _6 Oct 2006 1:32 pm_:
  Hi Anand, I read this article of your and have been trying to add key words which are generally asked in the job description.I hope to get some positive feedback now.I have been in London since last 4 months but not able to get a suitable job may be my CV didn't have key words required in the UK.(Just to let u know i'm an Chartered Accountant from India)
- **Nitu** _6 Oct 2006 1:37 pm_:
  Hi Anand , I read this article of urs yesrterday and have been trying to add the key words as required by the job description.Hope there's something positive soon.I have been in London for around 4 months and not been able to find a suitable job for myself ,may be my CV lacked key words.(Just to let u know i'm a Chartered accountant from India).It is nice reading ur articles.
- **S Anand** _6 Oct 2006 1:48 pm_:
  Sathya, yeah, I guess you could do that -- a tag cloud would look funky, and you could always hide sections (maybe font colour?) It'd be interesting to see some CVs like that :-)
- **S Anand** _6 Oct 2006 1:49 pm_:
  Nitu, to my knowledge, using keywords is not **that** prevalent yet. But yeah, way to go!
- **Nitu** _6 Oct 2006 2:22 pm_:
  Not using the key words seperately but adding in the sentences to make sense and almost the same meaning as i was trying to tell earlier.
- **S Anand** _6 Oct 2006 3:09 pm_:
  Nitu, that's probably the best thing. Happy to see at least one person have a better shot because of this article. Spread the word :-)
- **joey** _28 Oct 2006 10:37 pm_:
  anand Many recruitment firms use this method in Oz (Australia). It works - the right words get an phone interview call. For Nitu - my advise is to scan job ads and incorporate those sentences into the resume (nt just words) this will guarantee a higher response rate. worked for both my wife and me. And the first job in a new country is always hard.
- **Swapna** _29 Mar 2007 8:17 am_:
  Nitu, any improvement in reponse? I am also a CA from India and looking for job in UK!! Its seems really difficult to get an interview call here!
- **Georgie Girl** _31 Oct 2009 4:36 am_:
  A really interesting idea. In Canada I've seen the use of scanning program as well. I have been in HR and had to manually scan 100's of resumes and I can tell you that you are cross-eyed at the end. I guess a resume should have a footer with tag line extras, what would a good set include do you think?

<!-- wp-comments-end -->
