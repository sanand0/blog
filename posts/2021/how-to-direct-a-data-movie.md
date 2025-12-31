---
title: How to direct a data movie
date: "2021-02-07T15:34:43Z"
lastmod: "2022-02-02T10:01:11Z"
categories:
  - data
  - how-i-do-things
wp_id: 3079
---

![How to direct a data movie](/blog/assets/rubiks-cube.webp)

[Ganes](https://gkesari.com/) and I created a data movie on speed-cubing records as part of a Gramener hackathon.

<div class="video-embed"><iframe src="https://www.youtube.com/embed/V0OINTYrA8M" title="YouTube video" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

Here's a video of us talking about how we created it.

<div class="video-embed"><iframe src="https://www.youtube.com/embed/uxaPeIXP6E4" title="YouTube video" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

**Anand**: We picked the Rubik's cube story for this hackathon. Tell me more about how this excited you.

**Ganes**: Since my son started solving the Rubik's cube a few months back, I've been fascinated with these competitions. I still don't know how to solve it, but I like watching it.

**Anand**: But **he** does?

**Ganes**: Yeah, he does. So, in the competitions, I've seen kids solving the Rubik's cube in under 10 seconds. So that was the first source of amazement. I've seen kids doing it with one hand, blindfolded. I first couldn't believe it. Doing it with their legs. So that got me really interested.

When we were talking about this, and I was sharing my amazement, we were talking about the hackathon and the conversations kind of merged. So that, I think, the curiosity around it led to picking this as the story.

**Anand**: And what was the next step?

**Ganes**: I have always seen the [World Cube Association](https://www.worldcubeassociation.org/) publishing these records. Their [website](https://www.worldcubeassociation.org/results/rankings/333/single) is great. So I thought maybe we could scrape from that, and that’s when I start looking at the website and the competitions we can pick. and then I stumbled on the [export feature](https://www.worldcubeassociation.org/results/misc/export.html) where they have multiple formats neatly curated that you can take and directly start the analysis.

**Anand**: Which was actually a big factor in deciding to go for this. Big data set. Very rich, interesting possibilities.

**Ganes**: So we had had some five or six ideas. This immediately shot up to the top. So after we got the idea, you kind of took over. I think after I mentioned that all these formats were available, it got you excited. So what did you do after that?

**Anand**: Then it became a question of what all interesting things we can find. It's almost an exploratory data analysis, but my approach to EDA (exploratory data analysis) is: let's formulate the hypotheses and then validate, and see if there Is an interesting story behind it.

So it begins with, for instance, the speed at which records have been broken. Today, it's at 3½ seconds. We know that. But how fast did it fall? Or: what's the spread of solving-speed for somebody who solves it fast? Does the same person solve it really fast sometimes and really slow sometimes? Is there a movement in their average? You said, "Let's see how much longer it takes to solve bigger cubes." Nikhil was going to take the demographics of solvers and see how they're spread out. There are definitely a lot of Chinese solves in the spread. So, the thing was, let's look at possible ideas that could lead to an interesting answer, and then validate those.

**Ganes**: It was almost like "What would **we** be interested in finding out" and not necessarily like looking at the column of data.

**Anand**: Yes. And that I think is important, because, from the data, there may be some ideas. But after absorbing it, knowing what's **interesting** is what should drive the story.

**Ganes**: Right. Yeah. So that was a good starting point. We listed all of these on the board. Then, what did you do next?

**Anand**: Then it's about proving these. So, we know here are some possible interesting stories, and let us explore and validate whether these **are**, in fact, interesting, or can be turned into something interesting. So, when I looked at the speed at which records were broken, for instance, I **thought** that would be an interesting story. But it wasn't. It was just getting broken at a steadily successive pace.

But something that I did **not** expect emerged, which is that Wusheng Du, who holds the world record, is not the person who was there in the records consistently. In fact, Felix Zemdegs has been the consistent winner for the last 10 years and is the only cubing champion who's won the WCA twice. So, that was something that **emerged** from doing the analysis. So, that has the ability, therefore, of both proving what we're looking to prove (or disproving), and also coming up with new stuff that we can choose to incorporate into the story.

**Ganes**: Almost like starting with a business hypothesis, or what, in the enterprise world, the business wants to know, and then once you get into the data, the data is revealing a few interesting insights, and then you kind of marry both. Looks just like that.

**Anand**: Exactly. Exactly.

**Ganes**: So, we identified the insights. And then, the target here was to come up with a 2 minute video. So how did you plan from insights to the video.

**Anand**: So, one of my cousins is a director, and she tried explaining to me the concept of a screenplay. I never really understood it, even though I've read a number of screenplays. So, in the last hackathon, when I was creating a (data) movie, that's when I realised: as I started writing what I want to shoot (because it requires a whole lot of planning), I was effectively writing a screenplay.

The steps are, basically, you have to decide what are the frames or the sequences you want to shoot. So, one sequence was: we want to introduce this Rubik's cube win. Another sequence was: we want to show how quickly different types of cubes can be solved, etc.

So, for each of these, what I do is: create a storyline that has the following structure. One: what is the message I want people to take away from that.

**Ganes**: The headline from there.

**Anand**: Exactly.

And then, in order to do that, what are the words I would narrate on top of it? That literally forms the dialogue. The third thing is, what are the visuals that prove the dialogue. That I structure in the form of a video. The fourth thing is the transition -- from one video to another, or from one sequence to another, how do I flow. These are the 4 things that I captured.

When I write down the full dialogue. I speak it out, put in a timer, and then say "OK, this took 10 seconds, this took 15 seconds, this took 14 seconds" and so on.

Then comes the process of recording (the audio). Assembling the visuals, yes, but timing it and sequencing it based on the recording is pretty critical. So, actually, I wanted your voice - it's better. And initially, I wanted you to do the recording, but because you were busy in the Dell workshop, I had to do the recording to make sure that I get the timing. Then you re-recorded post that.

That recording makes a huge difference. The audio quality on my iPhone is better than the laptop. I transfer it via Dropbox on to the system.

**Ganes**: Were there some issues because you have some insights and you have a certain sequence, but it may not add up to 2 minutes. Or, there might be something which will just not flow. How do you correct those issues?

**Anand**: I found that I consistently underestimate (the time). I thought that we only have material for 1½ minutes, but I knew at that point that invariably, because of this bloat, it will somehow add up to 2 minutes. Which is exactly what happened. It moved to 2 minutes 4 seconds.

**Ganes**: Yes. Exactly. Yeah.

**Anand**: So, once you've done it once or twice, that amount of correction is there. It's in fact a whole lot easier to control a video than something as crazy as a (software) program, for instance. The estimation error in programming is much higher than this.

The good part is that post production or editing can take care of a lot of stuff. That 2-minute video **can** be cut to 1½ if required.

**Ganes**: Yeah, it can be improved, but my biggest fear is: after recording, the post production is a nightmare. It takes hours and hours of effort. A five-minute video, to post, probably takes 2 hours.

**Anand**: That is true.

**Ganes**: How do you go about it? After having these audio clippings, videos and images, how do you stitch all together into a video?

**Anand**: My workflow is on [PowerPoint](https://en.wikipedia.org/wiki/Microsoft_PowerPoint), mostly, and then on [Windows Video Editor](https://support.microsoft.com/en-us/windows/create-films-with-video-editor-94e651f8-a5be-ae03-3c50-e49f013d47f6). And then you introduced [iMovie](https://www.apple.com/in/imovie/) into the mix.

PowerPoint makes it fairly simple. I can put in an audio in the background. I can handle the animations. It's not a great tool at all, but it's a tool I'm very familiar with. So, my workflow is: one slide is one shot or one headline in the storyline. Then I record the video independently or download it from YouTube, put it in the background or wherever. Create all the visuals, create the animations around it, put it there. At this point, the raw material is in. Then I insert the audio and let it play the background for that particular slide. Then I time the animation to the audio.

This is a slow process because PowerPoint doesn't have the right tools. So I play the audio till that point and then set the animation. Then I start from the beginning again, play the audio to the next point, and then set that animation. Which takes a long duration. But once that's sorted out, I play that full slide and it works out, I then go back and correct.

The good part is that the audio is the time keeper. I pre-recorded the audio. So I know that the entire duration is only going to be 1.8 minutes (and then towards the end we added a few more vidoes that took it to 2 minutes). So the audio keeps you in control, and if you synchronize everything to the audio, then it becomes easier.

Then I exported it into a video file from PowerPoint directly, and then did a little bit of post-processing, adding a background music and adding a few captions, mostly, on Windows Video Editor, and then gave it to you. Which was at around 9 o'clock or so. What did **you** do from 9 o'clock to 3 o'clock?

**Ganes**: So, the first thing -- on the PowerPoint, I couldn't believe that you'd done all this on PowerPoint. Yes, you're taking the tool beyond the limit it was designed for.

I've been working with iMovie for a year, and I find it very powerful. For someone who doesn't come from that background, it was very easy for me to pick up. I had the images and raw video footage for the different portions we were trying to introduce. I was able to split the audio that you recorded from the video, and then was able to record mine and add it. iMovie has these multiple streams you can insert and remove. I had one stream for my audio for my voice over. And there was this video which you had.

On top of that, I could overlay the pictures and other videos that I had towards the end -- two videos playing side-by-side. So all of that was possible. and then I could also introduce background music at the very end. iMovie makes it very easy to move all of these things around. And even the synchronization issue which you told about, that's much easier to resolve in iMovie.

So, all of this finally coming together, I think, at 3 o'clock… when I had all of this, at 3 o'clock I was hunting for the background music (laughs). I was playing all kinds of clips and finally I chose one. So that's how we got the final YouTube video.

**Anand**: My lesson from this is: make sure you have a team member who has a Mac!

**Ganes**: Right, yeah. So let's go back and look at our video and see what we can learn from it. Thank you!
