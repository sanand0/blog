---
title: Command line alarm
date: "2010-01-24T04:37:24Z"
categories:
  - coding
  - how-i-do-things
wp_id: 2444
---

When I’m in front of my laptop, I usually forget the world around. Sadly, the world around has important things that need to get done on time. Like eating medicines, turning off the washing machine or the hob, etc.

The one thing I’ve been lacking on my machine was a simple alarm system. I’d like to set an alarm to remind me to do something in 5 minutes, for example. And it should be dead simple to set up.

After hunting around a fair for freeware to do this, I’ve finally settled on writing this tiny piece of Visual Basic code.

```vb
Set WshShell = CreateObject("WScript.Shell")
If WScript.Arguments.length < 2 Then
  WScript.Echo "Usage: alarm <time-in-minutes> <message>"
Else
  WScript.Sleep WScript.Arguments.Item(0) * 60 * 1000
  msg = ""
  For i = 1 to WScript.Arguments.Count - 1
      msg = msg + WScript.Arguments.Item(i) + " "
  Next
  WshShell.Popup msg, -1, "Alarm", 64
End If
```

I’ve saved this as “alarm.vbs” somewhere in my path. When I need to set an alarm, I just type

```bash
alarm 5 Turn off the hob
```

This pops up a window in 5 minutes with the alarm:

[![An informational popup window saying Turn off the hob](/blog/assets/alarm.webp)](/blog/assets/alarm.webp)

This turned out to be a life-saver yesterday. I had to catch a flight at the Bangalore airport, and traffic is notoriously bad. To be on the safe side, I set up the following:

```bash
alarm 25 Catch the flight
alarm 30 You really need to go now
alarm 35 You've missed the flight
```

Turned out to be a wise thing. I ignored the first alarm. On the second, I said “OK, OK, just 1 minute…” and it really took the third alarm to get me going. Just barely made it to the flight.

---

## Comments

<!-- wp-comments-start -->

- **[Abhijit Sen](http://abhijitsen.webs.com)** _10 Feb 2010 12:07 am_:
  Anand. is it required to have a VB client to run this VB script?
- **408wij** _26 Jan 2010 10:28 pm_:
  For us uninformed Americans, hob=stove, right?
- **Sumit Dhar** _25 Jan 2010 1:14 am_:
  Hey Anand,
  Was it a flight for UK?
  If you are gonna be back in Bangalore, let us meet up sometime.
  Cheers,
  Sumit
- **[Abhijit Sen](http://abhijitsen.webs.com)** _12 Feb 2010 1:45 am_:
  Hey Anand. I opened a notepad, copy pasted the above code with the specific number of minutes and message, saved the notepad as Alarm.vbs on my desktop. Nothing happened after the given number of minutes. What am I missing?
- **[S Anand](http://www.s-anand.net/)** _29 Jan 2010 8:37 am_:
  But isn't an annoyance the whole point of an alarm?
- **[Anup](http://allanup.blogspot.com)** _28 Jan 2010 12:35 pm_:
  Nice and useful lines.
  Any clue for sending the annoying window to background...
- **[S Anand](http://www.s-anand.net/)** _10 Feb 2010 4:49 pm_:
  No, not at all. This comes built in with Windows. Absolutely nothing else required.
- **Ravi** _28 Feb 2010 6:26 pm_:
  You can use gadgets in Vista for. I searched and found one, free.
- **Ravi** _28 Feb 2010 6:30 pm_:
  http://www.puttee.de/
  I tried this Anand, works like a charm..
- **[Ravi](http://NA)** _14 Feb 2010 7:11 am_:
  @Abhijit - You dont have to specify the minutes and message in the .vbs file. Just save it as it is in a folder. You will have to write the command from the same directory on the DOS Prompt.
  The command "Alarm x message" takes the minutes and the message as the input and displays them when it runs Alarm.vbs
  I made this change to the script since I got error in executing the original one.
  CHANGED
  "If WScript.Arguments.length < 2 Then"
  TO
  "If WScript.Arguments.length < 2 Then"
  (Message can only be without spaces with this change)
- **Ramki** _19 Jun 2010 5:01 am_:
  I am using WinXP and could not get the script to work with the following line and had to change it as shown below after getting clue from Ravi's comment:
  CHANGED
  “If WScript.Arguments.length < 2 Then”
  TO
  “If WScript.Arguments.length < 2 Then”

<!-- wp-comments-end -->
