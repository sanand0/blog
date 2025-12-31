---
title: Matching misspelt Tamil movie names
date: "2005-12-09T12:00:00Z"
categories:
  - how-i-do-things
wp_id: 478
---

I don't like hunting for new songs either. Too much effort.

External recommendations like [Raaga Top 10](http://www.raaga.com/channels/tamil/top10.asp) help, but not much. I usually like only 1 of the top 10.

I don't really know the recent music directors. But many interesting songs I've heard recently (like Ondra Renda in Kakka Kakka, Vaseegara in Minnale, and Kaadhalikkum in Chellame) are by Harris Jayaraj. So maybe if I can find the music directors I like, other songs by them would be good recommendations.

I have an automated way to find the music director for a movie. First, I spent a few hours renaming my MP3s to a Movie.Song.mp3 filename format (using Excel and Perl liberally). After that, I wrote a Perl program that reads movie names and the movie directors from [Raaga](http://www.raaga.com/) and matches the Raaga movie names with my movie names. (Raaga has all but 5 movies whose songs I've heard.) Then I rate music directors based on my songs' ratings.

Unfortunately, the matching worked only for 45% of my 273 movies. The rest were spelt differently on my list and Raaga. I checked [CPAN](http://www.cpan.org/) if there was a way to match Tamil words roughly. The closest was [Lingua::Phonology](http://search.cpan.org/~jaspax/Lingua-Phonology-0.32/Phonology.pm), but Jesse, the author, mailed me saying that was "like slicing your bread with a chainsaw".

So I developed these rules. The -> arrow below is to be read as "is also spelt as". By just applying them **sequentially**, I matched 33% more movies.

> **Vowel rules**\
> **AE**dhiri -> **E**dhiri\
> kadhal kond**EI**n -> kadhal kond**E**n\
> chellam**EY** at end-> chellam**E**\
> sach**IE**n -> sach**I**n\
> marupad**IU**m -> marupad**IYU**m\
> **OI**, **OY**, **OVI**, **OYI** are all the same\
> **AA**thma -> **A**thma\
> azhagiya th**EE**ye -> azhagiya th**I**ye\
> ab**OO**rva ragam -> ab**U**rva ragam\
> Ignore **H**. It is redundant.

> **Consonant rules**\
> arasak**TCH**i -> arasak**SH**i\
> **CH**ippikkul muthu -> **S**ippikkul muthu\
> then**NDR**al -> then**NR**al\
> devar ma**H**an -> devar ma**G**an\
> baga**W**athi -> baga**V**athi\
> avvai shanmu**G**i -> avvai shanmu**K**i\
> kon**J**i pesalam -> kon**CH**i pesalam\
> an**D**ha 7 naatkal -> an**T**ha 7 naatkal\
> a**B**oorva sagodharargal -> a**P**oorva sagodharargal\
> agni natcha**THIR**am -> agni natcha**THR**am

The remaining movies either had spelling mistakes (e.g. Kilipethcu Ketkavaa) or had structural differences (Ilamai Oonjal Aadu**giradhu** vs Ilamai Oonjal Aadu**dhu**). By permitting approximate matches using [String::Approx](http://search.cpan.org/~jhi/String-Approx-3.25/Approx.pm), I was able to match 12% more, making my total accuracy ~90%.

Though this is good enough for identifying music directors, I'm working on improving the approximate matching rules. I hope to have 98% accuracy, and then I can match individual songs -- and know who the singers are. Hopefully, this can be extended to other sites like [MusicIndiaOnline](http://www.musicindiaonline.com/), and who knows -- maybe even [IMDb](http://www.imdb.com/).

---

## Comments

<!-- wp-comments-start -->

- **Ashwin** _10 Dec 2005 3:36 am_:
  I use www.arthika.net for downloading high quality MP3's. Their song ratings are good. This is my strategy.
- **S Anand** _12 Dec 2005 6:55 pm_:
  I tried it out... maybe it was just me, but I thought they had a smaller collection than Raaga. Is that right?
- **Ashwin** _18 Dec 2005 6:41 am_:
  Ya, They have only a small collection but he quality of the songs are very good.
- **Bala** _9 Dec 2005 12:00 pm_:
  Can you make the script you made downloadable for folks to normalize their unwieldy MP3 library? Even 80% would do for me considering the amount of chaos that prevails! :) Thanks

<!-- wp-comments-end -->
