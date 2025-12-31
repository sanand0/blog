---
title: Two Factor Authentication
date: "2005-03-17T12:00:00Z"
categories:
  - links
wp_id: 712
---

Bruce Schneier on [The Failure of Two-Factor Authentication](http://www.schneier.com/blog/archives/2005/03/the_failure_of.html). [Two factor authentication](http://www.itsecurity.com/papers/rainbow2.htm) replaces passwords with two things: something you have (e.g. a security token that changes numbers every minute) and something you know (e.g. password). Bruce says this won't help against two new kinds of attacks we're seeing:

> **Man-in-the-Middle attack**. An attacker puts up a fake bank website and entices user to that website. User types in his password, and the attacker in turn uses it to access the bank's real website. Done right, the user will never realize that he isn't at the bank's website. Then the attacker either disconnects the user and makes any fraudulent transactions he wants, or passes along the user's banking transactions while making his own transactions at the same time.
>
> **Trojan attack**. Attacker gets Trojan installed on user's computer. When user logs into his bank's website, the attacker piggybacks on that session via the Trojan to make any fraudulent transaction he wants.
