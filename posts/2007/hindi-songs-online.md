---
title: Hindi songs online
date: "2007-02-19T12:00:00Z"
lastmod: "2009-02-25T08:59:38Z"
categories:
  - how-i-do-things
wp_id: 110
---

**[Click here to search for Hindi songs](/hindi)**.
This is an article on how I wrote the search engine.

I find it a nuisance to have to go to [Raaga](http://www.raaga.com/), search for a song, not find it, then go to [MusicIndiaOnline](http://www.musicindiaonline.com), not find it, then go to [Musicplug.in](http://www.musicplug.in/), and so on until Google.

So I got the list of songs from some of these sites, put it together in one place, and implemented a find-as-you-type.

Just go to **[s-anand.net/hindi](/hindi) and type a song or movie name**.

**Update:** How I created this is a very long story, spanning over two years. And here it is.

---

Over the last 5 years, my MP3 collection had grown quite large. Most of these were from MP3 CDs I had bought, songs I'd downloaded, or songs I'd recorded. In any case, the file names were a mess. In early 2005, I decided to organise the collection and put them all into one big directory per language, and name the files in the format "Movie.Song.mp3".

People think I'm crazy to use a single large directory. But I prefer one directory with 5,000 files to 1000 directories with 5 files for a simple reason. **Searching in one directory is easier than in multiple directories**. You can just sort everything by name, date modified, size, whatever. On the command prompt, you can type "DIR dil\*.txt" to see all movies starting with "Dil".

I chose the "Movie.Song.mp3" format because the movie name and the song name were really the only two things I knew about **every** song I had. I didn't always know the music director, singers or year of the movie. And I placed "Movie" before "Song" because I often browse songs within a single movie, and it's useful to sort by name in Windows Explorer and see all the songs in a movie. I've never had a need to sort by song name. If I wanted to find a song that started with, say, "pehla", I'd just type "DIR \*pehla\*" on the Command Prompt. (As you might have guessed, I have a Command Prompt window always open.)

So, having very rationally organised my music collection, I was happy.

Soon the problem shifted to song discovery. I'd heard the familiar songs in my collection many times. Of the unfamiliar songs, but I didn't know which to pick. I knew I liked some music directors more than others, and had a hunch I liked older songs. (My subsequent [analysis of song preferences](/Top_Tamil_songs.html) confirmed this.) But I didn't know the year or music director for any of my songs.

Since [Raaga](http://wwww.raaga.com/) had a decent collection of songs, along with the year and music director, I decided to download this information and tag my files with this information. There were two problems. Firstly, the **data in Raaga needs to be parsed**. I need to hunt through each file to find the year and music director. The second was worse: **my song names were spelt differently from Raaga's**.

**Step 1: download the HTML and parse it**. Perl is pretty much the only programming language I know. I used [Perl's LWP library](http://www.perl.com/pub/a/2002/08/20/perlandlwp.html) to download the [movie index of Raaga](http://www.raaga.com/channels/hindi/movies.asp). Each movie in the index always has the URL http://www.raaga.com/channels/hindi/movie/something.html. So I extracted these patterns and downloaded all these URLs as well. (Others have a recognisable pattern as well: http://www.musicindiaonline.com/music/hindi\_bollywood/s/movie.some\_number/, http://www.musicplug.in/songs.php?movieid=some\_number, http://ww.smashits.com/music/hindi\_film/songs/some\_number, etc.)

You probably realise that I downloaded a fair bit of the entire Raaga.com site's HTML. Actually, it's not that big. The 800-odd files in the Hindi collection didn't take more than 40MB of space, and a few hours to download. Here's what the code looks like:

```python
# Get the list of movies HTML file
my $index = get("http://www.raaga.com/channels/hindi/movies.asp");

# Extract the list of movies from that into a hash (movie, url pairs)
my %movie = ($index =~ m|<a href="/channels/hindi/movie/([^"]*).html" class="[^"]*">([^>]*)</a>|gsi);
 
# Loop through each movie
for my $file (keys %movie) {
  # Get the song HTML file
  my $html = get("http://www.raaga.com/channels/hindi/movie/$file.html");
 
  # Year is typically like this: Movie_Name (1983)
  my $year = ($html =~ m|<b>$movie{$file}\s+\((\d*)\)</b>|) ? $1 : "";
 
  # Music director always has the URL /channels/hindi/music/something
  my $md = ($html =~ m|<a href="http://www.raaga.com/channels/hindi/music/[^"]*" class="black">(.*?)</a>|) ? $1 : "";
  for (split /\n/, $html) {
 
    # Now get individual songs and rating. They always have an onClick="setList(something)"
    if (m|onClick="setList1\((\d*)\)[^>]*>(.*?)<\/a>.*?"http://images.raaga.com/.*?.gif" alt="RATING: ([\d\.]*)"|) {
    $song = $2;
    $rating = $3;
    print join("\t", $movie, $song, $year, $md, $rating), "\n";
  }
}
```

Incidentally, I'm showing you a simplifed version. I actually wrote the script in a way that I could resume where I left off. The **ability to resume was probably the single most useful time-saver** in the entire process.

**Step 2: match the song names with those on my list**. This is tricky. I hate doing it manually. So I developed a set of rules that could compare two spellings of a movie and decide if they were the same or not (see my earlier post on [matching misspelt movie names](/Matching_misspelt_Tamil_movie_names.html)). For Hindi songs and movies, here are my rules (in JavaScript):

```javascript
w = w.toUpperCase(); // Convert to upper case
w = w.replace(/\s+/, " "); // All whitespaces = 1 space
w = w + " "; // Ensure there's a space after every word
w = w.replace(/W/g, "V"); // V=W
w = w.replace(/Z/g, "J"); // Z=J
w = w.replace(/PH/g, "F"); // PH=F
w = w.replace(/([KGCJTDPBS])H/g, "$1"); // Ignore H after most consonants
w = w.replace(/(.)\1/g, "$1"); // Ignore repeated letters
w = w.replace(/Y/g, ""); // Ignore Y
w = w.replace(/([AEIOU])N /g, "$1"); // Ignore trailing N after vowel (hein, mein)
w = w.replace(/[AEIOU]/g, ""); // Ignore vowels
w = w.replace(/ /g, ""); // Ignore spaces
```

These are the rules, incidentally, that I use in my [Hindi](/Hindi_songs_1995s.html) [quizzes](/Hindi_songs_2000s.html). Even if you type in a different spelling, the rules above will match the correct answer.

I extended these programs over 2006 to cover [MusicIndiaOnline](http://www.musicindiaonline.com/), [Musicplug.in](http://musicplug.in) and [Smashits](http://ww.smashits.com). (I've hit a point of diminishing returns, I think, so I'm not too keen on expanding this list.)

Now, with a database of song information, I needed a good media player to view this in. I've used several media players over time: [WinAmp](http://www.winamp.com/), [Windows Media Player](http://www.microsoft.com/windows/windowsmedia/), [RealPlayer](http://www.real.com/player), [iTunes](http://www.apple.com/itunes/), and [MediaMonkey](http://www.mediamonkey.com/). I'm a big WinAmp fan, but I've been forced to Media Monkey now. WinAmp has a 10 second delay before playing any song on my [new laptop](/Software_for_my_new_laptop.html). MediaMonkey's not bad, though. The lack of advanced filters is countered by the heavy programmability (I can use Javascript to update MP3 ID3 tags on MediaMonkey). Plus, I get all the WinAmp plugins. As for the other media players, I think they're junk.

There are five things I want in a perfect media player:

1. **Find as I type**. I shouldn't have to type the entire song, or press a "Go" button. I'll just type. It should show all matches instantly. WinAmp does this, and that's why I loved it. (Today, most media players can do this.)
2. **Advanced filters**. Instead of manually creating playlists, I'd rather create filters, like "Highly rated songs in the 2000s I haven't heard recently". (See [How I listen to music](/How_I_listen_to_music.html).)
3. **Enqueable playlists**. When I click on a song, I don't want my current song to be interrupted. Just play it next.
4. **Global hotkeys**. I want to pause the song when someone says something -- without having to go to the application, search for the pause button, etc. WinAmp does this brilliantly with its global hotkeys.
5. **Online and offline integration**. I want to be able to search online collections, like Raaga. Unfortunately none of the media players can do this. They have their own collections (radio stations, really), but even these aren't really searchable.

Since my favourite media players (WinAmp and MediaMonkey) lack only one of these features, I thought I might be able to build them in.

But no such luck. It was almost easier to build my own media player. So I started to build my two weeks ago. My hope was to cover as many of my favourite requirements, beginning with **find as you type**.

The key to find-as-you-type is speed. You can't afford many calls back and forth between the browser and the server. Even if people have a fast connection, my server is not fast enough. (A good part of the reason [why I use Google applications](/Why_Google_Reader.html) is **speed**. Google's server is blazingly fast, and the design of their applications complements that.) To make find-as-you-type fast, ideally the entire database should be loaded. Then, as you type, I just need to check with the database in memory. But downloading an entire database takes ages! (My full music database is 7MB right now.)

**Step 3: compress the database**. Rathern than load the full 4MB, I managed to get the page to start after loading 100KB of data. First, I cut down less important fields. Most searches are for a song or movie, rarely for a year or music director. So I took **only the movie and song names**. That brought the data down to ~2MB.

I don't need to repeat the movie name across songs. If I have something like this:

```text
Movie1  Song1
Movie1  Song2
Movie1  Song3
Movie2  Song1
Movie2  Song2
```

I can store this instead as:

```text
Movie1  Song1   Song2   Song3
Movie2  Song1   Song2
```

I can also eliminate duplicate names. This brings down the space requirements to ~500KB.

The next step was the clever one. **I don't need to load the full database before you start searching!** It's enough to load a reasonable subset, and let you start searching while the rest loads in the background. So my [hindi song search engine](/hindi) loads about 100KB of the data from one Javascript file, lets you search, and in the background loads the 400KB Javascript file. As soon as that finishes loading, it displays results from that set as well. (The initial portion is really songs on Raaga. I figured it would represent a decent search set.)

**Step 4: find-as-you-type**. This is quite easy, actually. I send the onkeyup event to my search function.

```html
<input id="inp" onkeyup="csearch()">
```

The csearch() function goes through all the songs, checks if there's a match, and prints all those results.

```javascript
// Create a case-insensitive regular expression
var re = new RegExp(search, "i");
for (var i in songs) {
  if (re.test(songs[i)) { str += songs[i]; }
}
library.innerHTML = str;
```

But that, unfortunately, takes **ages** to finish. If you implemented this as is, you would have to wait 1 - 1.5 seconds between each key stroke. So I made two modifications. Firstly, I restrict the number of results displayed to 100. When you start typing, (for example, you'd go 'c'... 'ch'... 'chu'...) there are several songs early on that match the string, so I don't have to search through the whole list. This speeds up the search for small strings.

When the search gets bigger, ('chupke chu'... 'chupke chupk'...), there aren't 100 results. So the search has to cover the full list, and that takes 1-1.5 seconds between each keystroke. So I took another clever step. I broke the search into chunks of 5000 songs. That takes a fraction of a second. I search successive chunks of 5000 songs. If I find any results, I add them. Then I wait for a keystroke. If nothing happens, I continue searching the next 5000 after 50 milliseconds, and so on. If you press a key in the meantime, I stop searching for the original word, and start searching for the new word. This makes the application appear a lot faster.

There are ways I could make this even faster. For example, people type more often than delete. A typical sequence would be ('chupke ch'... 'chupke chu'... 'chupke chupk'...) rather than the reverse. Backspace is not pressed very often. So, instead of re-searching the whole list, I could just search the already-searched list in such cases. But right now, the search works fast enough, so I'll leave it at that.

The next step is **advanced filters**. I'm working on that right now. Hopefully you'll see in a while.

---

## Comments

<!-- wp-comments-start -->

- **reshma** _21 Feb 2007 9:46 am_:
  your search tool is awesome !
- **sarangan** _21 Feb 2007 9:18 pm_:
  anand - can you illuminate the technique you used to consolidate the names of tracks in one list and the dynamic search based on combination of letters ?
- **gagan** _21 Feb 2007 10:42 pm_:
  god level tool man! awesome!! please do elaborate on the methodology followed to make the tool. thanks :)
- **S Anand** _22 Feb 2007 2:22 pm_:
  Sure. Will post the details soon.
- **Sai** _23 Feb 2007 4:27 am_:
  Well, now that you've posted this list, you should become the next raaga and allow songs to be heard!
- **S Anand** _23 Feb 2007 7:38 am_:
  You can do that even now -- just click on the song :-)
- **jake** _23 Feb 2007 9:17 am_:
  dude your tool is good.
- **Saurabh** _23 Feb 2007 2:21 pm_:
  Brilliant! Sheer genius!
- **Sai** _23 Feb 2007 4:45 pm_:
  Yup i just realized!! Mighty impressive bud!
- **Sriram** _23 Feb 2007 11:45 pm_:
  thamizh sevai..
- **shane** _24 Feb 2007 11:34 am_:
  i love you
- **Karthik A** _25 Feb 2007 2:04 am_:
  This is awesome man. 2 days I have seen this I dont go to Music India or Raaga. This is neat, but how are you going to keep it updated?
- **Raga** _25 Feb 2007 6:24 am_:
  dude, is it possible to download songs like ilayaraja's how to name it?.. please tell how
- **S Anand** _25 Feb 2007 8:59 am_:
  Hi Karthik, updating is not an issue. I have an automated script that checks for updates and downloads the info. Takes 10 minutes. I'll run it every two weeks or so.
- **S Anand** _25 Feb 2007 9:00 am_:
  Raga, try TamilTorrents.net -- they have the full How To Name It collection.
- **Ramkumar R** _25 Feb 2007 9:08 am_:
  Awesome tool! Really appreciate the effort.. Just a suggestion.. CoolToad has a huge tamil/hindi collection as well.. Any possibility of indexing that as well?
- **Raga** _25 Feb 2007 10:50 am_:
  Thanks anand... i couldnt find the songs there. there is no searching tool there.. please post any other place where i can find them.. thanks once again
- **S Anand** _25 Feb 2007 11:45 am_:
  Ramkumar, cooltoad is next on my list.
- **Raga** _25 Feb 2007 2:04 pm_:
  One more thing anand, there are many very good BGm tracks by ilayaraja.. is it possible to add them ? rhanks
- **S Anand** _25 Feb 2007 2:08 pm_:
  Raga, you're right -- I couldn't find it on TamilTorrents any more. I have a bunch. Mail me at root dot node at gmail dot com. And where can I find links to the background music collection? Would love to add them
- **Ravi** _25 Feb 2007 2:49 pm_:
  thanks for the useful tool. you rock!
- **Karthikeyan** _25 Feb 2007 6:04 pm_:
  Well done Anand! The tool is amazing!
- **Karthikeyan** _25 Feb 2007 8:11 pm_:
  See my blog! I have published an article about this
- **Divya** _25 Feb 2007 8:55 pm_:
  aaamazing!!!!
- **Divya** _25 Feb 2007 9:00 pm_:
  bookmarked.. added to favourites.. everything :)
- **Divya** _25 Feb 2007 9:01 pm_:
  i love the part where the results start appearing even before u finish typing.. like the google toolbar search
- **senthil k** _25 Feb 2007 9:49 pm_:
  nice one
- **Meenakshi Sundaram** _25 Feb 2007 10:32 pm_:
  Anand, You have a amazing job man. Keep it up.This would help many tamil music lovers and save their time on searching. I am really greatfull to you for the effort and time you have put.
- **johan paris** _25 Feb 2007 10:58 pm_:
  fantastic job
- **Prasanna** _25 Feb 2007 11:02 pm_:
  This is amazing. Well done!
- **Thiagu** _25 Feb 2007 11:59 pm_:
  really good tool Anand. Thanks for the same. I am not able to download any songs. rightclick and "save target as" is saving the html page. Could you provide your suggestion
- **SP.VR.Subbiah** _26 Feb 2007 1:27 am_:
  I appreciate your marvelous work Many songs in tamil are available in www.musicplug.in Site. Please provide your links also to that site
- **keshav bhat** _26 Feb 2007 3:10 am_:
  Fantastic! I'm not certain how you found time for this, but the results are truly fantastic! keep up the great work
- **Radha** _26 Feb 2007 4:03 am_:
  Thanks so much. You are genius.
- **Jala** _26 Feb 2007 4:50 am_:
  Really cool
- **sundararajan** _26 Feb 2007 5:26 am_:
  Anand fantastic buddy...beautiful.....
- **sundar** _26 Feb 2007 5:27 am_:
  Anand simply superb..GR888
- **naveen** _26 Feb 2007 5:37 am_:
  nice tool
- **usha** _26 Feb 2007 5:45 am_:
  a very good job anand, came thro karthiks blog. i have been trying for a long time to download the song thendral vanthu theedum pothu from avatharam. though i couldnt download i was happy to hear the song here. thanks
- **sathik** _26 Feb 2007 6:24 am_:
  coll saite
- **Rakesh** _26 Feb 2007 6:53 am_:
  Its wonderful .. and ultra fast .. Thanks.
- **Priya** _26 Feb 2007 10:10 am_:
  nice site enjoyed a lot thanks
- **Gops** _26 Feb 2007 11:50 am_:
  wonderful stuff from u Anand..really a nice one.. i've been searching songs from Thalaivasal Album all these days... wow finally.... thanks a lot.....
- **Kaps** _26 Feb 2007 2:43 pm_:
  Anand, This is a great tool. Thanks for all the effort. Can you also include Tamilbeat and Thenisai into this?
- **Chakra** _26 Feb 2007 3:05 pm_:
  Brilliant stuff Anand. Thank you.
- **Kaps** _26 Feb 2007 3:08 pm_:
  Anand, Understand your time constraints. Just wanted to give some hint about the ways to strengthen this tool. IMHO, Music Director - good to have (not essential). Year - doesn't matter that much to music fans (low priority). The percentage of people wanting to know the year would definitely be low.
- **S Anand** _26 Feb 2007 3:53 pm_:
  Thanks, Kaps. It's exactly this sort of prioritisation help that I need. Will try and pull in these additional databases.
- **Cosmic Voices** _26 Feb 2007 3:53 pm_:
  Truly amazing!!!
- **Rajagopalan** _26 Feb 2007 4:27 pm_:
  Hi Anandavi Kannnadasan,s songs are available in Tamilnation website Why don't u combine this in the Tamil songs script. V.Rajagopalan Chennai
- **Syam** _26 Feb 2007 5:59 pm_:
  Awesome search engine dude....Thanks bunch
- **thetalkativeman** _26 Feb 2007 7:08 pm_:
  Anand, hats off to you. This is fantastic :) I've been using these sites for 5 years on a daily basis and your tool means a lot to me :-)
- **kittu** _26 Feb 2007 8:37 pm_:
  nice work anand. key change search is great. GR8 work.
- **kittu** _26 Feb 2007 8:43 pm_:
  you are going to rock the music world maamu :-)
- **madhu** _27 Feb 2007 1:15 am_:
  that is cool. thanks
- **Kaps** _27 Feb 2007 2:55 am_:
  Anand, You are right, the collection in Thenisai and Tamilbeat are not all that impressive. Most of them are recent collections and they would have been covered by Raaga and Music India anyway.
- **Adiya** _27 Feb 2007 5:29 am_:
  Super .romba nalla eruku.. super super
- **Mugunth** _27 Feb 2007 6:46 am_:
  Hi Anand, Wonderful service. I have blogged about this here: http://mugunth.blogspot.com/2007/02/tamil-song-search.html
- **S Anand** _27 Feb 2007 7:03 am_:
  Thanks, everyone! Enjoy.
- **deekshanya** _27 Feb 2007 10:40 am_:
  Your effort needs true appreciation! Good job! Hatsoff for all the hardwork
- **Gopinath Selvaraj** _27 Feb 2007 11:47 am_:
  This is the first ever search engine that gave me immediate results for songs like 'Aayar paadi maaligayil' and 'meenkodi theryil'... Its a google for Tamil and Hindi Music. Thanks a lot for your hard work.
- **Viren Manek** _27 Feb 2007 1:00 pm_:
  I liked this search very much. Its fantastic....
- **Viren Manek** _27 Feb 2007 1:04 pm_:
  Why dont u keep the hit counter on ur site, u will get lots of hit.... :). People will like to bookmark this URL for any song to listen.
- **Jaganath** _27 Feb 2007 4:35 pm_:
  Unbeleivable Performance of the Search Functionality. Cool Site dude!...
- **Raamcm** _27 Feb 2007 4:40 pm_:
  You did great job man.... Thanks
- **ரவி** _27 Feb 2007 7:03 pm_:
  chanceless tool !!!! thank u so much..i was fed up clicking link after links in raaga, musicindia etc..please give more tools like this for the needs of tamils, indians. நன்றி
- **Kapil** _27 Feb 2007 10:12 pm_:
  Anand, AWESOME Tool ! I found songs that I never thought I'd find. However, most of the links were not working. A few took me to either raaga or musicplug but there were more that gave an error message saying the link on sanand.freehostia.com is not working
- **Prabha** _28 Feb 2007 1:39 am_:
  Great piece of work, Anand. I always wanted to have such a tool for Tamil music. In fact, i started to write something similar, more of a user contribution kind of thing, similar to IMDB. Displaying other Meta tags (artist, movie, year, director) would be really useful here. I appreciate your work!
- **Saurabh** _28 Feb 2007 6:32 am_:
  Addition of playlist by Music Directors is awesome!
- **cr.sathish** _28 Feb 2007 5:28 pm_:
  Dear anand, its really kool and kudos to you for making this up.
- **madhan** _28 Feb 2007 6:57 pm_:
  u r rocking...
- **reshma** _28 Feb 2007 8:32 pm_:
  anand, would it be too much to ask for multiple selections against a list of songs?
- **RPanda** _28 Feb 2007 8:42 pm_:
  Hi Anand, it's a very neat site with great feature. Really appreciate your efforts!!
- **S Anand** _28 Feb 2007 9:19 pm_:
  Reshma, what do you mean by multiple selections?
- **Maya** _28 Feb 2007 9:52 pm_:
  Great job ..
- **buspass** _1 Mar 2007 1:13 am_:
  cool work man. AJAX rocks.
- **Vinay** _1 Mar 2007 2:57 pm_:
  Excellent.
- **Sriram** _1 Mar 2007 7:14 pm_:
  Great Tool!! Awesome Job!!
- **Supremus** _1 Mar 2007 10:06 pm_:
  Awesome job dude!
- **reshma** _1 Mar 2007 10:26 pm_:
  right now i click on a single song, hear it, and come back here to click on another. It would help if I could select more than one song at a time - so that those songs could play one after the other without my intervention.
- **S Anand** _1 Mar 2007 10:55 pm_:
  Reshma, continuous playback is what I want next as well. It's very difficult, though. Don't know if I'll be able to do it. Will try.
- **maniprakash** _2 Mar 2007 2:55 am_:
  Good work man,
- **aman** _2 Mar 2007 3:00 am_:
  pretty cool man
- **aman** _2 Mar 2007 3:01 am_:
  y not create a request play... like a playlist created by everyone... which everyone can hear
- **BHARANI** _2 Mar 2007 7:39 am_:
  This looks brilliant. Good Concept and congrats.
- **Anonymous** _3 Mar 2007 9:57 am_:
  unfin!!!finally u got it man!!!!really super work! mercy...add more top 20 in all language tamil,english hindi...mercy....
- **nagu** _3 Mar 2007 12:43 pm_:
  அருமையான படைப்புங்க....ரொம்ப நன்றிங்க....வெறும் நன்றிங்கறத விட நாலுபேருக்கு இத இன்ட்ரோ... கொடுத்தாத்தான் கரெக்ட்டா இருக்கும் என்ன நாஞ்சொல்றது.... சரிதானுங்களே?
- **PK** _4 Mar 2007 6:16 am_:
  Good work dude...
- **Tejas** _4 Mar 2007 7:29 pm_:
  I salute your creative/techi mind.Thats AJAX right ?
- **shema** _5 Mar 2007 12:08 pm_:
  Few suggestions of movies to add to your playlist. Vennira Aadai (Enna enna vaarthaigalo), Kunguman (Chinnanj chiriya Vanna paravai), Paadhai theriyudhu paar (Thennangeetru oonjalile) I've searched for these songs in the net and have failed.
- **shema** _5 Mar 2007 12:10 pm_:
  Excellent work. I see the desi Indian instincts being very strong in you. Did this work take a vigorous shape after Shilpa's issue?
- **S Anand** _5 Mar 2007 1:16 pm_:
  Hema chithi, the songs are already there. Just type Vennira Aadai ~ Enna Enna Varthaigal, Kumkumam ~ Chinnanchiriya and Pathai Theriyudhu Paar ~ Thennan Keethu Onjalile. Who is Shilpa?
- **indu** _5 Mar 2007 4:47 pm_:
  hi anand, cool site... you should add a hits counter, you could rake some big bucks with ads if this link gets popular..
- **தமிழ்பித்தன** _6 Mar 2007 2:15 am_:
  உண்மையில் உங்கள் முயற்சி என்னை மெய்சிலிர்கக வைக்கிறது உங்கள் தயவால்விரும்பிய பாடலை நின்ற இடத்திலிருந்து கேட்க முடிகிறது கொசுறு:-இன்னும் வேறு தளங்களையும் இணைக்க இயன்றளவு முயலுங்கள்
- **Anonymous** _6 Mar 2007 5:05 am_:
  கலக்கல் சாமீ ஆனந்த் அருமையான உழைப்பு வாழ்த்துகள
- **रवि** _6 Mar 2007 6:43 am_:
  बहुत उम्दा प्रयास और सराहनीय कार्य. हमारी शुभकामनाएँ.
- **Debashish** _6 Mar 2007 9:00 am_:
  Splendid work guys :)
- **Sagar Jain** _6 Mar 2007 9:38 am_:
  Good work, keep it up :)
- **shema** _6 Mar 2007 11:32 am_:
  Shilpa Shetty. The actress who stood up against racial discrimination.
- **shema** _6 Mar 2007 12:15 pm_:
  I could hear thennangeetru....... but unable to listen to chinnannchiriya vanna paravai. Help me with other search words. Also the song chinna chinna mookuthiyaam from the same movie paadhai theriyudhu paar
- **sri** _6 Mar 2007 6:08 pm_:
  you have done agreat job man
- **srk** _7 Mar 2007 9:10 am_:
  Anand, there is a good collection of songs on dhingana.com , specially marathi, can you index those as well ?
- **Ravi** _8 Mar 2007 6:30 pm_:
  hi anand, is there any chance of making this as a toolbar which can be downloaded in to IE or Mozilla?
- **ram** _8 Mar 2007 10:05 pm_:
  hey man..gr8..keep going...it wud be best if u can giv downloads too
- **Subhash** _10 Mar 2007 3:47 pm_:
  Anand Bhai You should be no.1 on "The Google" list. You are the best.
- **Hamish** _10 Mar 2007 4:16 pm_:
  man thanx for ths great site.it helps really.keep it up.kudo
- **Ashish Ranpara** _11 Mar 2007 10:17 am_:
  plz keep going and get more and more old songs you have a really good old hindi songs i really glad for that thanks......
- **Sriram** _11 Mar 2007 4:10 pm_:
  ur tool is just awesome!!!!!
- **Saravanan** _11 Mar 2007 7:04 pm_:
  Dear Friends, I am a big fan of tamil comedy dramas by Shekar and Crazy Mohan and talk show by Leoni. Is there anyway I use this tool to find the availabile mp3s on that?
- **Sanketh** _12 Mar 2007 8:11 am_:
  Man, this is a truly cool tool ... Can you do the same thing for Tamil/Telugu songs? Tell me something - does Raaga etc show information about how long the song is? I can think of a really cool tool if raaga does maintain that info.
- **S Anand** _12 Mar 2007 8:44 am_:
  Sanketh, none of the sites show the song length, unfortunately. But if we could get it, what could we do?
- **Mano** _12 Mar 2007 3:11 pm_:
  great work Anand !!
- **Sanketh** _12 Mar 2007 6:56 pm_:
  We could create an online playlist of songs, drag and drop songs from your search to a frame on the right. To play we just load the link in a hidden iframe (or a frame at the bottom). The problem is we wouldn't know when each song is done to switch to the next song.
- **Anonymous** _12 Mar 2007 8:17 pm_:
  This is amazing Anand .. I wish there was one for Telugu/Tamil songs as well.
- **S Anand** _13 Mar 2007 12:21 am_:
  Sanketh, good point. I haven't given up hope on that, though. May still be possible. Let's see...
- **vijay** _13 Mar 2007 6:25 am_:
  Great work anand
- **Anotheranon** _13 Mar 2007 4:29 pm_:
  Anand ! Love ur work! I am looking for "Nee munnale pona naan pinnaale vaaren" REMIX from vaathiyaar. Any idea why not there ?
- **S Anand** _13 Mar 2007 5:33 pm_:
  Search for "Yennadi Muniyamma", and you'll find the song.
- **Mahendra** _13 Mar 2007 8:00 pm_:
  Ananda i want to know, can i download the songs that r being played after i click on them & when realone player window opens
- **S Anand** _13 Mar 2007 8:53 pm_:
  Not on this page, Mahendra. Go instead to s-anand.net/hindimp3 or s-anand.net/tamilmp3 to download songs.
- **rajvir** _14 Mar 2007 5:26 am_:
  i want to download the song..jeene ke ishaare...but it 's not there in your content please help me
- **S Anand** _14 Mar 2007 6:03 am_:
  Rajvir, the song is there in the collection. When you tried it, for some reason, it was using only a fraction of the index. Just wait a few seconds for the full index to load (or reload the page), and you'll have the song.
- **mak** _14 Mar 2007 8:46 pm_:
  infact a good tool. but cudn't find movie "begunaah qaidi". neways thumbs up to u.
- **sundar** _15 Mar 2007 1:39 pm_:
  Excellent work, Anand!!! Thank you very much
- **sundar** _15 Mar 2007 1:52 pm_:
  Anand, not sure if this is already on cards. It would be great if you can add more Carnatic/Tamizh isai songs to the database
- **Raja.S** _16 Mar 2007 5:21 am_:
  Hey Anand, Excellent man.. I got rare songs I was looking for a long time. Thanks a ton. Love Raja
- **Sanketh** _16 Mar 2007 5:26 am_:
  Man, your search algo is pretty decent too. Was just searching for 'elangaathu' and typed it as elankaa.. and it still showed the right song.
- **S Anand** _16 Mar 2007 9:16 am_:
  Sundar, Carnatic music search is already live at s-anand.net/carnatic and I'm planning to add to the (currently somewhat sparse) collection.
- **Kalpesh** _16 Mar 2007 11:49 pm_:
  I really liked the site & idea. I am not sure that I am being naive, is it possible for me to select multiple songs & play them one by one?
- **Smitha** _17 Mar 2007 2:20 pm_:
  Excellent site very cool.
- **S Anand** _17 Mar 2007 3:46 pm_:
  Kalpesh, playing multiple songs is not possible right now. I'm trying. It's difficult, though. Don't know if I'll be able to do it. Will keep trying.
- **மதி** _17 Mar 2007 7:15 pm_:
  அண்ணன் என்னடா தம்பி என்னடா.... பாடலைக் கேட்டேன் இதனை எப்படி தரவிறக்கம் செய்து கேட்பது எனத் தெரியவில்லை, அருமையான பாடலைத் தந்தமைக்கு மிக்க நன்றி
- **S Anand** _17 Mar 2007 8:30 pm_:
  Mathy, search for "Annan Ennada" at s-anand.net/tamilmp3
- **Krishnamurthy** _18 Mar 2007 5:05 pm_:
  you worked very very hard make such a search tool, its really amazing keep well , keep doing good work
- **Sundar** _21 Mar 2007 3:26 am_:
  Anand, it would be great if we can have some site preferred over others (something like appearing on Top). Because as I observed oosai & Music-Plugin has got good sound quality over others. I also found my favorite carnatic songs in the carnatic page. Thanks again!!
- **Chirag Mehta** _21 Mar 2007 9:16 am_:
  Hey Anand , Really Good Site I liked it What was ur idea behind this Site development is the same which i was facing. Thanx for a ready made solution for me Added Link to ur Site as a post on my site http://www.chiragmehta.info/chirag/2007/03/21/hindi-songs-online-search-engine/
- **S Anand** _21 Mar 2007 11:37 am_:
  Sundar, how about this order: MusicPlug.in > Oosai > Musicindiaonline > Raaga > Smashits?
- **Shekhar** _22 Mar 2007 4:34 pm_:
  Good site. I am searching for koyil pura film song 'vedam nee' n surfed the whole net without success. Please help
- **S Anand** _22 Mar 2007 5:15 pm_:
  Shekhar, search for "koyil pura" on s-anand.net/tamilmp3 and you'll find Vedham nee
- **Shekhar** _22 Mar 2007 8:05 pm_:
  Thanks Anand. I tried for almost an hour but could not able to download the song as it always says the network is busy
- **S Anand** _22 Mar 2007 8:10 pm_:
  Shekhar, I'm having some trouble at cooltoad as well. Usually, I wait a day and it's fine.
- **Shekhar** _23 Mar 2007 6:28 pm_:
  Tried whole day but without luck. Any other option.
- **Aqua** _23 Mar 2007 6:49 pm_:
  aWesoME TOOL.
- **sundar** _24 Mar 2007 7:39 am_:
  Anand, Thanks for considering my request. That order would be great.
- **Varun** _24 Mar 2007 10:50 pm_:
  Hi! Awesome search...just like Winamp...lot of effort put..good going!!
- **shilpa** _25 Mar 2007 9:12 am_:
  hi! Congrats.... amazing search. Could you add other regional songs to the list??
- **பாலச்சந்தர் முருகானந்தம்** _26 Mar 2007 8:51 am_:
  நல்ல கருவி
- **Prasun** _28 Mar 2007 4:49 am_:
  I came here searching for music. Your tool is awesome. It would be nice if this were extended to playlist creation etc - I think it would probably be not very hard if all songs are from a single site. Oh, and I spent a couple of hours in your writings section!
- **Varun** _29 Mar 2007 11:14 am_:
  Great tool anand!
- **Seshan** _29 Mar 2007 11:59 am_:
  Anand, just happened to visit this page. Awesome. Couple of songs that I found it difficult to get were made so easy with your tool. (Sorgame endralum, solladi bharatha maatha to name a couple). Great work.
- **Seshan** _29 Mar 2007 12:51 pm_:
  Anand - For carnatic songs, can't the search be made on 'ragam'. It would be cool to have it. Just a suggestion.
- **Roopa** _29 Mar 2007 4:21 pm_:
  Hi!!...Superb job! Good going..
- **Anonymous** _30 Mar 2007 8:54 am_:
  hai friends.. its not working
- **Shekhar** _30 Mar 2007 9:46 am_:
  After continuous effort I managed to download koyil pura songs. Many thanks Anand for making my day. Keep up the great job
- **Vishal** _31 Mar 2007 1:51 pm_:
  Anand ,I have forgotten all other hindi song websites now.
- **Venkat** _2 Apr 2007 6:29 am_:
  Good keep it up I advocate open source can u think of simple tools for day to day money management and account management with banks
- **Kannan** _5 Apr 2007 9:56 am_:
  First of all good work !!! I keep referring to this whenever I have to get some movie names for songs. I personally have a 17Gig songs collection, I would like to know if you have encountered an API to change properties of a mp3 file like title, album title etc. programmatically (preferably in Java or Groovy or Ruby or Perl) ???
- **abbas** _8 Apr 2007 11:16 am_:
  good job man,thanks alot.
- **Anu** _9 Apr 2007 12:24 am_:
  Hi Anand...this is really a great job...i need a help...i find that tamil and hindi songs are available at your site for download...Can you please help me out with the carnatic songs too....for now it would be great if i have 'Sachmara ramavani' atleast....i have been trying to get this song for such a long time...thanks so much for the great work!
- **Viju** _10 Apr 2007 6:48 am_:
  Interesting work. Is there a similar serach tool for carnatic/hindi radio? There is a similar search site for lyrics...at lyricsdir.com.
- **ramkrishna** _11 Apr 2007 4:09 am_:
  hindi song
- **ramkrishna** _11 Apr 2007 4:11 am_:
  Kachche Dhaage's songs
- **Kavitha** _12 Apr 2007 2:51 am_:
  That was a wonderful tool Anand. I found it very useful... :)
- **Pradeep** _12 Apr 2007 3:29 am_:
  hello bro awesome work da. can u pls find me a song from Prem Qaidi - I live for u.
- **jagannath** _13 Apr 2007 11:03 am_:
  awesome job, Anand could you also upload kannada. Will You
- **Nainesh** _15 Apr 2007 12:25 am_:
  Superb, and fast i like the idea, Keep it up, i found it useful.
- **sameer jain** _15 Apr 2007 4:56 am_:
  awesome anand but can please help me in finding one song from maine pyaar kiya ..its aate jaate i am not able to hear it ..please help .. but one thing is for sure ..u really did a gr8 job ..get this gud work going all the way up ..all the best
- **Anonymous** _16 Apr 2007 6:20 am_:
  awesome job.....
- **Manikandan** _18 Apr 2007 10:59 am_:
  I guess there are some issues. Webpage is loaded with errors. Also, Why cant we have Punnagai Mannan Theme Music?
- **animesh** _19 Apr 2007 8:38 am_:
  Hey Anand....u are genius...great idea...nicely implemented.....all of us (i.e. people like me) are greatful to u for making this tool and letting us use it.....one idea (if u have some free time) that u can try ....let users create a playlist using ur site....
- **Hemant B.** _20 Apr 2007 5:14 pm_:
  Thanks Annand you have created very useful site for music lovers. wish you best luck for your new creation.
- **jitendrasharma** _22 Apr 2007 12:53 pm_:
  jitu
- **thuva** _22 Apr 2007 1:48 pm_:
  wow nice and great i will give you 90% for this website tthat tamil sitet downloading for free i love it and your the best fro my life ok then take care and good luck best of luck and great and great good site and 90% rating
- **your name** _27 Apr 2007 12:05 am_:
  awesome collection!!
- **SHAMIT** _27 Apr 2007 7:48 am_:
  Absolutely splendid job using: Perl, your brain and its ideas ... !! ;)
- **SHAMIT** _27 Apr 2007 1:38 pm_:
  Can't stop admiring! Killer App. Listening to Guide songs BRILLAINT !!
- **Sabarish** _28 Apr 2007 4:10 pm_:
  Its absolutely wonderful.....Really helpful for avid song listeners like me..the web application speaks for itself...i dont need to add any more nice adjectives to it. great work dude..
- **Deepak** _30 Apr 2007 8:46 am_:
  great job anand, really great collection
- **Siva Chandran P** _3 May 2007 11:17 am_:
  Great Job
- **mahesh raghunathan** _4 May 2007 10:10 am_:
  really great da... infact i was searchin for SRI RAGAVENDRA movie scorings for a long time.. got it frm ur site... its really good... keep going..
- **Anonymous** _5 May 2007 3:50 am_:
  great job anand..searching a song is very easy now..hats off to u.
- **k.Bharathi Kannan** _5 May 2007 5:34 am_:
  First of all, THANKS A LOT to you sir. Me too had disappointed in searching for many songs.But I dont know any sites to which i hav to search for songs. This is the first site which i came to know about, regarding cine songs. And this is really great work. Once again THANKS A LOT sir.........
- **your name** _6 May 2007 4:16 pm_:
  Hi...will you be making the carnatic songs too downloadable? am waiting for them.....
- **avinash** _8 May 2007 6:44 pm_:
  great work anand.. its really very simple to listen songs over here. can u please include the songs from strings..the pakistani band. thanx for creation of such link...keep goin
- **shivam** _12 May 2007 11:21 pm_:
  thank you so much yaar i am simply feeling so relaxed now. after searching for geeta dutt songs for six months i finally got them from your site. thank you so much and if there is anyway i can send songs to upload, do tell me.
- **srinath** _13 May 2007 6:47 am_:
  hi dude mann u r search tool i awesome and its really so simpel to get us the required song. One suggestion to u buddy....how abt adding a playlist...so tht ppl can add their list and den keep njoyin the music......
- **srikan** _15 May 2007 5:49 pm_:
  gud one. u can actually make it further responsive. do u use prototype?
- **Bala** _17 May 2007 8:38 am_:
  Your site is the single most impressive site i have seen.. Kudos http://quietturbulence.blogspot.com
- **sai kalyan** _17 May 2007 11:27 am_:
  excellent site man really great search tool
- **mohan** _18 May 2007 7:10 pm_:
  Nice job dube :)
- **shashwat** _19 May 2007 12:05 pm_:
  Great job buddy !! Thanks a lot
- **InTeGeR** _20 May 2007 9:22 am_:
  Simply awesome... You helped me get some old Ilayaraja gems. Thanks a lot. It has also climbed up in Google search
- **Ravi** _19 Feb 2007 12:00 pm_:
  Nice Job Anand! Excellent work!!
- **thiru** _19 Feb 2007 12:00 pm_:
  song is good but how can i download plz give me the link thak for the song
- **Paritosh Arya** _19 Feb 2007 12:00 pm_:
  Hi Anand, You really have done a lot of research while developing this search engine....really inspiring...keep it up.
- **venkat** _19 Feb 2007 12:00 pm_:
  Excellent job man.hats off to ur idea.One question is that cant we select multiple songs at a time and play the continously becos i think thats repeated song to play a single song.if we can do that pls tell me how to do that
- **rama ragbir** _19 Feb 2007 12:00 pm_:
  thanks for a great service . i am looking for a song of
- **Jagadesh Kumar** _19 Feb 2007 12:00 pm_:
  Hi Anand This is a fantastic effort you have made and suceed to get this much big database. I was randomly searching for movie converter tools, to get information from the internet (like IMDb, Amazon Movie Databases) and come across your website. I really felt happy and you have done excellent job. If you have any idea how to get the movie information (title, cast, director, music etc etc) as well list of all songs (by singer). Thanks Jag
- **kannu71** _19 Feb 2007 12:00 pm_:
  really a nice piece of work, waiting for more
- **Sravya** _19 Feb 2007 12:00 pm_:
  Hello, We are not able to search the desired songs.You are not providing the search box.Sometimes the search box appears,sometimes not. We liked the website,but we want you to always provide the search box.
- **Dhimant Panchal** _19 Feb 2007 12:00 pm_:
  it is a nice program to find a song. but i have one problem. your program search the song but cannt play it. it sows an error message to contect the real network support center. you have any solution ? pls tell me. Thanks.
- **rahul kumar gupta** _19 Feb 2007 12:00 pm_:
  the site is so good but... if i want select all song how?
- **milton** _19 Feb 2007 12:00 pm_:
  What site give the fastest download in window media player? Please list this to me.Thanks.
- **Rahul** _19 Feb 2007 12:00 pm_:
  Excellent. Excellent. Is it possible to download songs on iPod. I am not an expert in technology and hold basic knowledge but would appreciate if somebody can tell me if it is possible to download songs from this site on my iPod. Thanks.
- **parag** _19 Feb 2007 12:00 pm_:
  gr8 effort man, even i too a music freak. I hv collected thousands of songs in mp3 format, but same problem here too, how to maintain database, for few i generated playlist & put on my site:- http://geocities.com/direct2parag/new/coolgoose/ still i found it cumbersome. will u plz help me out to maintain a good database for the same..... solicit ur co-operation.... Thanks. parag
- **priyanka** _19 Feb 2007 12:00 pm_:
  raaga
- **E.Srinivasarao** _19 Feb 2007 12:00 pm_:
  E X C E L L E N T
- **ASHOK** _19 Feb 2007 12:00 pm_:
  your job is ecellent can you upload the tamil karoake also? ashok
- **sen** _19 Feb 2007 12:00 pm_:
  u have done a commendable job - 'anand' a gaya
- **A K V K Rao** _19 Feb 2007 12:00 pm_:
  Excellent work. Brilliant Idea. Good luck. Rao.
- **Nitin Patel** _19 Feb 2007 12:00 pm_:
  A very good information. I would also like to suggest 2 different websites http://musicmirchi.net and http://dhintana.com
- **Mohd Abdullah** _19 Feb 2007 12:00 pm_:
  no comment
- **Binosh Nambiar** _19 Feb 2007 12:00 pm_:
  Mindblowing..Excellent......!!!!! Anand you have really done a great job... Can u provide URL Addresses of all songs????? Actually i have an Account in Zorpia.com... I want to creat my Own playlist..
- **Chetan** _19 Feb 2007 12:00 pm_:
  This is great. The concept, the implementation, the application of it. Everything is great ! I love it when ideas get implemented and get implemented in a way that they stay around e.g. your bi weekly updates is the best part.
- **prakash** _19 Feb 2007 12:00 pm_:
  i like you
- **AKASH** _19 Feb 2007 12:00 pm_:
  this is great site. i am enjoye it this concept. best of luck
- **Neha singh** _19 Feb 2007 12:00 pm_:
  i like old indian songs
- **Nitin** _19 Feb 2007 12:00 pm_:
  I also like old India songs just like Neha :)

  [MP3 Songs Downloads](http://musicmirchi.net)
- **sangye** _19 Feb 2007 12:00 pm_:
  Hi I really do hope you will write me back. i have seen your song collection and it is fantastic. I live in europe and teach bollywood dancing. so your site is perfect. thanks as the saying goes you are a genius for many. Ah but lets see if you will be one for me too. i have a hindi song it is a mix of east meets west. cannot find the name of the movie, everytime i tupe in 2 to 3 words i get the silsilay as the first words are same. so here goes.
  " oh oh oh, oh oh oh, oh oh oh feel it oh sooniya oh oh mahiya oh la la la ... feel it feel it , meri chanii tu meri sona tu mera hera tu mera ,,,,.. zindagi ka guzara tere bin nahi hona ishaq hai tum se yaara tum ko nahi khona. )2)
  male - oh sooniya oh mahiya....
  Waiting for your reply.
  thx dear
- **vaidehi** _28 Aug 2008 12:45 pm_:
  GGGGGGGGGGGGOOOOOOOOOOOOOOOOOOOOOOOOOOOD
- **murali** _6 Nov 2008 8:55 pm_:
  solla vaarthaigal illa.............

  born genius..
  www.cooldls.com
- **samarth** _13 Dec 2008 2:01 pm_:
  hi..i couldn't open ur web page search engine..it becomes totally white page..and the web messege is also showing done..why is it so??i too want to take taste of your music search engine as i m one of great lovers of music..so plz show me way..
- **ratna** _28 Dec 2008 8:20 am_:
  anand you are simply briliant.my husband and I are both in music profession and it helps a lot to find a song.Great job. God bless you!
- **Vinoth** _15 Jan 2009 11:26 pm_:
  Mr. Anand

  I am from chennai. for long i have been trying to do some thing like you have done. only that i started in 2009 and not in 2005. anyway now what i am looking for is to collect and prepare a complete database of old and new hindi songs. now my work has become simpler as you already have collected. i would further interact with you so if you give me your email it will be helpful to me.
- **Vishwanath.P** _7 Feb 2009 6:56 am_:
  You are really great "SIR". You if, with one man army did all these things, my hats off to you..
  Well i am also like you, in the sense that i wanted to a complete NEAT collection of songs...
  Thank you
- **Hemant Shah** _21 Feb 2009 5:06 pm_:
  Splendidly done - What marvellous use of available tools
- **[Sriram](http://www.sriramajeyam.com)** _2 Mar 2009 11:32 pm_:
  Good job..
- **ROHAN GANDHI** _20 Mar 2009 6:58 am_:
  where i can find tag songs or tag list for hindi songs
- **Srikanth** _23 Jun 2009 7:06 pm_:
  Excellent work! The way you have thought about the whole process is remarkable and the fact that you shared every step is highly appreciable. Helps a lot to see stuff like this for working on other projects. Thanks a lot!
- **Saravanan** _15 Jan 2010 12:42 am_:
  Simply Excellent, the thought process is simple great
  Fantastic job, clean and neat :)
- **NSaravanan** _14 Dec 2010 7:16 am_:
  Hi Anand, Simply superb.
  I am not very familiar with programming...I sometimes adapt few VB codes for my excel. that's all.
  Is there a list of Tamil movies with tags, which you can share?
  Also, have you tried copying the Album Artwork for the movies / songs?
  cheers,
  Saravanan, Gurgaon
- **Akshay** _27 Jun 2012 3:47 pm_:
  Hey man. I am currently in the process of the tagging my hindi mp3 files as well and like you am a serious media monkey user. I was wondering if you could help me with 1) a comprehensive database of songs with id3 tags and 2) set up a way to auto tag my files with missing info.
  Thanks
- **Parthasarathy-82, @ Sarathy** _1 Jun 2011 10:00 am_:
  Dear Sir,
  You have achieved 30% of quantum., that means you have conquered Tamil Nadu completely many decades back. About 60% have finished becasue you have conquered entire South India and made Bollywood admired about your excellency, but your goodself is about to achieve 100% centum per cent by conquering the entire world by scoring different melodies in almost about all world languages in the remaining period.
  Why you know sir ..... Because there is no another ILAYARAJA SIR IS GOING TO BE BORN. This is plain truth and universal fact as well.
  "pudu raagam padaippadaale "NAANUM IRAIVANE"
  Yes, of your are the Iraivan of WORLD MUSIC OF 21ST CENTURY OF UNIVERSE
  Regards,
  Parthasarathy-TVK NAGAR - CHENNAI - 82, @ Sarathy
- **[Nirmala](http://gmail.com)** _13 Apr 2011 9:06 am_:
  It is very interesting to read your adventure. Music drives us crazy sometime. In turn wonders m ay happen.As I am also into your craze why cant you add features so that songs can be played remotely also voice input would be another challenge. What do you say. I have not yet tried your application. Happy music days !
- **Mohan Kethees** _30 Aug 2011 2:30 pm_:
  Hi. Nice work.
  2 things.
  1. How do i use the python crawler you have linked in the help.
  2. Why not make it a web service? Idea for web service would be to query for a song and you get full ID3 detail or query for a movie and you get all the song ID3 details in that movie. It would help for
     I am willing to help But I am a C# developer and have little to no knowledge in python or Perl.
     Thank you
- **shiva prakash** _17 Aug 2011 12:01 pm_:
  Thanks a lot for your dedication
- **Ambarish** _19 Jul 2011 7:07 pm_:
  Thank you very Much...Awesome... I can't believe i got all my favourite songs here in one single website...Thank you very much again...Good Luck
- **[Tushar](http://tusharg.blogspot.com)** _21 Mar 2011 8:01 am_:
  Hats off to you! You ave done excellent job. Hope the search site you have created will be always up.
  and thanks a lot. :)
- **nk** _26 Jun 2013 10:47 am_:
  Excellent work putting this up! Thank you.
  FYI, Musicindiaonline links don't seem to work.
- **Nadeem** _25 Aug 2015 9:02 am_:
  [http://music.cooltoad.com/music/download.php]
  This site is down, is there any other link for those songs???

<!-- wp-comments-end -->
