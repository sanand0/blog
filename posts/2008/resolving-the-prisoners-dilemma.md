---
title: Resolving the Prisoners Dilemma
date: "2008-08-17T12:00:00Z"
categories:
  - business-realities
wp_id: 42
---

If you're ever taken a course in Economics, and it discussed Game Theory, you may be familiar with [The Prisoner's Dilemma](http://en.wikipedia.org/wiki/Prisoner%27s_dilemma). Roughly, this is the problem.

> Assume you possess copious quantities of some item (money, for example), and wish to obtain some amount of another item (perhaps stamps, groceries, diamonds). You arrange a mutually agreeable trade with the only dealer of that item known to you. You are both satisfied with the amounts you will be giving and getting. For some reason, though, your trade must take place in secret. Each of you agrees to leave a bag at a designated place in the forest, and to pick up the other's bag at the other's designated place. Suppose it is clear to both of you that the two of you will never meet or have further dealings with each other again.
>
> Clearly, there is something for each of you to fear: namely, that the other one will leave an empty bag. Obviously, if you both leave full bags, you will both be satisfied; but equally obviously, getting something for nothing is even more satisfying. So you are tempted to leave an empty bag. In fact, you can even reason it through quite rigorously this way: "If the dealer brings a full bag, I'll be better off having left an empty bag, because I'll have gotten all that I wanted and given away nothing. If the dealer brings an empty bag, I'll be better off having left an empty bag, because I'll not have been cheated I'll have gained nothing but lost nothing either. Thus it seems that no matte what the dealer chooses to do, I'm better off leaving an empty bag. So I'll lease an empty bag."
>
> The dealer, meanwhile, being in more or less the same boat (though at the other end of it), thinks analogous thoughts and comes to the parallel conclusion that it is best to leave an empty bag. And so both of you, with your impeccable (or impeccable-seeming logic), leave empty bags, and go away empty-handed. How sad, for if you had both just cooperated, you could have each gained something you wanted to have. Does logic prevent  cooperation? This is the issue of the Prisoner's Dilemma.

There's nothing wrong in the logic, actually. The key assumption is that **it is clear to both of you that the two of you will never meet or have further dealings with each other again**. If you're never going to deal with someone again (and hence there is no question of retribution or any fallout), you really should cheat.

An aside. During my first few days at IIT, two third years were ragging me about my stance on pre-marital affairs. After trying my best at defending the moral standpoint, I finally confessed that it was only the fear of the after-effects that worried me.

> "There's this beautiful naked girl in your room," they said. "You are guaranteed no repercussions. What will you do?"
>
> "No repercussions?"
>
> "None whatever."
>
> I thought for a while. "I'll flip a coin." :-)

Anyway, the aside aside, the solution to the one-off Prisoner's Dilemma is for both people not to cooperate. If contracts are not enforceable, we're all better off not trading. If there are no cops, we're individually better off stealing.

But, of course, that's not true in the real world. Most situations are repeatable, and you do tend to meet people again. Those you cheat may even have a motivation to meet you again.

This is the **iterated** Prisoner's Dilemma. [Douglas Hofstadter](http://en.wikipedia.org/wiki/Douglas_Hofstadter) wrote about this in the May 1983 issue of [Scientific American](http://www.sciam.com/) in his [Metamagical Themas](http://en.wikipedia.org/wiki/Metamagical_Themas) column (which, by the way, is brilliant). While the Prisoner's Dilemma has a simple solution (don't cooperate), the iterated Prisoner's Dilemma does not have a predetermined solution. At best, you can have a strategy. (That can be proven. If there was a predetermined solution, your opponent would know it, and could beat you. One of those cases in mathematics where you are [not guaranteed a solution](/Implicit_information.html).)

But is it possible for cooperation to emerge in an iterated Prisoner's Dilemma? Can it beat competitiveness?

Robert Axelrod of U.Mich conducted a computer tournament to find out. He invited strategies from game theorists and wrote them as BASIC programs. Each program would be pitted against another. Every time, it could response with either C (cooperate) or D (defect). Cooperation gets both programs 3 points. If one defects, the defector gets 5 points and the cooperator gets nothing. Both defecting gets 1 point each. Axelrod ran each program against each other many times, and added up the scores.

The program that won was called [TIT FOR TAT](http://en.wikipedia.org/wiki/Tit_for_Tat). It was the shortest program (4 lines of BASIC code). Here's it's strategy:

> Cooperate the first time.
>
> Do what your opponent does thereafter.

Think about it. TIT FOR TAT starts by being **nice**, and stays that way, unless you defect. Then TIT FOR TAT **punishes**. If you repent, TIT FOR TAT forgets and **forgives**. Interestingly, TIT FOR TAT can never win a game. It can, at best, draw a game, but never score more points than its opponent. It goes for winning the war by **losing battles**.

That's four traits:

1. Being nice
2. Punishing immediately
3. Forgiving immediately
4. Willing to lose battles

After publishing these results, and having learnt a lot about different strategies, Axelrod repeated the tournament. Four times as many entries poured in. This time from world experts on game theory. It also included an improved TIT FOR TAT called TIT FOR TWO TATS, which is an improved TIT FOR TAT that does not fall into a C - D - C - D cycle when playing against TIT FOR TAT.

TIT FOR TAT won again.

Till date, TIT FOR TAT remains an unbeaten individual strategy, and people believe it may be optimal.

(PS: By **individual** strategy, I mean that there are multiple programs that can team together, losing to each other and making sure that one of them wins. This sort of thing can beat TIT FOR TAT. But no **individual** program beats TIT FOR TAT.)

---

In our first term at [IIMB](http://www.iimb.ernet.in/), we played a game in our organisational behaviour class, intended to help us understand inter-departmental cooperation (or rivalry). The class was split into two 'companies'. Each company had four divisions.

The game had 10 rounds. In each round, every division could choose to cooperate or defect. If everyone cooperated, each division made 3 points. If any division defected, it would make 5 points, while all cooperating divisions made 0 points. If all divisions defected, they would all make 1 point. The divisions were not allowed to talk to each other.

The aim was to beat the other company. (Not other divisions, within or outside the company.)

Our company started off with 3 Cs and a D, which quickly deteriorated to 1 C with 3 Ds by round 6. At round 7, it was 4 Ds.

Before round 8, we were all given a chance to have a huddle. A representative from each division would come together and talk things through. We promised to cooperate, and thereafter, it was 4 Cs to the end.

We lost the game. The other 'company' had started off with 1C and 3Ds, but had learned to cooperate pretty quickly, aided, in [Prof N M Agrawal](http://www.iimb.ernet.in/iimb/html/facultyprofile.jsp?id=8)'s words, by "... Aparajita threatening the other divisions with her glares."

---

The reason there's a Prisoner's Dilemma is the inability to reliably communicate or enforce behaviour. Having a chat helps. Having laws that punish you helps. Having a bully threaten you helps. The thing is, you need a signal of some kind. And it needs to be an early signal, or you end up waiting till round 8 and lose the game.

If you're ever in a situation where cooperation helps everyone, but it's not in interest to cooperate, here's what seems to work:

- See if you can agree to cooperate before-hand
  - Have a chat
  - Find policies that punishes defectors
  - Threaten if required
- If not, then try to force cooperation by signaling.
  - Be nice
  - Punish defection immediately
  - Forgive repentance immediately
  - Lose battles to win the war

---

## Comments

<!-- wp-comments-start -->

- **Dibyo** _19 Aug 2008 1:05 am_:
  I really liked this piece. It's not a new concept to me, and I've understood it well before, but the TIT-FOR-TAT part really connected.\
  \
  Dibyo\
  (IIMB too, but a couple of years junior - we only heard about Stud Anand)
- **S Anand** _19 Aug 2008 11:03 am_:
  @Dibyo: Even when playing the game at IIMB, a few of us knew about TIT FOR TAT. Didn't help. Guess there's a huge gap between understanding and practice...
- **Abhi** _28 Aug 2008 5:33 am_:
  Fantastic piece, very lucidly put.\
  \
  IITM - Mtech, we should have heard about Stud Anand.
- **[deepak](http://www.business-samhita.blogspot.com)** _30 May 2010 7:32 pm_:
  We played the game in IIMB and ended up doing the same stuff and never getting it right. Dibyo, I think it was Prof. Reddy who made us play this game. But then I went to Solvay for Exchange - 2 each from IIMB and A , we tried TIT for TAT first( many teams too many combinations ), didnt help post the huddle while everyone else was trying for Tit for TAT we kept going against to drive home the message. The prof did mention that one enlightened party doesnt help unless everyone else gets the message :)
- **Prabu** _10 Dec 2010 9:03 am_:
  Hi Anand,
  Was going through your post. Just thought of this algorithm that would beat the TIT-FOR-TAT algo. it would be:
  1. Never Co-operate.
     Now, this algo always either wins or draws individually. Group games are different.
     Thanks
- **[S Anand](http://www.s-anand.net/)** _10 Dec 2010 2:56 pm_:
  That's an interesting point, Prabu: "group games are different". Totally so.
  Your Never Cooperate algo, as you pointed out, always wins or draws.
  Tit-for-tat, interestingly, NEVER WINS AN INDIVIDUAL GAME. You can prove it, but [this file is a demonstration](http://files.s-anand.net/images/tit-for-tat.xls): it plays random strategies out against Tit-for-tat. Tit for tat never wins.
  Maybe the lesson here is a stronger version of "Losing the battle, winning the war". Perhaps it's **essential** to lose the battle to win the war. (I'm probably oversimplifying, or in extrapolating analogies... anyway, just wanted to say: yes, never co-operate beats tit-for-tat on an individual game. Many other such strategies exist too. As you mentioned, group games are quite different)

<!-- wp-comments-end -->
