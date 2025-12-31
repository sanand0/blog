---
title: How to stop filesharers from stealing hotel bandwidth
date: "2005-12-07T12:00:00Z"
lastmod: "2009-03-07T16:59:07Z"
categories:
  - funny
wp_id: 484
---

Hilarious post on [how to stop filesharers from stealing hotel bandwidth](http://www.signal15.com/articles/2005/12/06/how-to-stop-filesharers-from-stealing-hotel-bandwidth).

> So, I’m in Milwaukee at ye olde Holiday Inn Express. They have a wireless internet connection here and it’s been suckin’ all night, like I couldn’t even do anything on it. I suspected someone running a p2p program and taking up all of the bandwidth, so I fired up ntop to analyze the type of traffic on the network, and just who it was generating it. Lo and behold, someone was running a p2p app, and taking up 1.6Mbit worth of bandwidth. That’s just not fair to the 20 other people on the network, so I decided to boot him from the network. I tried poisoning his arp cache and the default gateway’s cache, but that only works on some wireless access points, apparently not this one. I can’t send an 802.11 deauth message from my OS X box, because the card doesn’t support raw packet injection, so what to do???
> I notice that his IP in the ntop interface changed into a name. His windows machine was spewing Netbios packets with his computer name in it. For the sake of his privacy, I’ve changed the name, but let’s say it was “smith-laptop”. So I pick up my cellphone and call the front desk at the hotel and as for Mr. Smith’s room. The lady at the front desk says “Eric Smith?” And I tell her yes. The phone rings, someone picks up, the conversation goes like this:
> Me: Eric Smith?
> Eric: Uhh, yeah?
> Me: My name is Jim Grant, and I’m an investigator with the RIAA. Have you heard of us?
> Eric: Uhhhhh….. What does that stand for?
> Me: Recording Industry Association of America. We represent several large record companies. In monitoring several p2p filesharing networks, we have found that you Eric, are currently downloading copyrighted material. Are you aware that this is illegal?
> Eric: Ummm…. my laptop is off. (At this point, I no longer see him on the network)
> Me: We are in the process of filing 18182 lawsuits against people who steal copyrighted music on the internet. We will continue monitoring these networks, and if we see you on them again, you will hear back from us.
> Eric: Ok, thanks. Bye.
> So, now my network is nice and speedy again. And some guy is in his room trying to dry out his underwear. :) I should have recorded the call since my cellphone has the capability to record conversations. The above conversation can’t even begin to show the fear in his voice. I’m sure he’s scared as hell wondering how they found out his name and that he was staying at a hotel and exactly what room he was in.
