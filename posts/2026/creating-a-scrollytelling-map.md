---
title: Creating a scrollytelling map
date: 2026-07-12T16:25:50+05:30
categories:
  - visualization
  - llms
description: I built a scrollytelling map using Claude Code, other AI agents, and MapLibre GL JS for GitHub Pages. My workflow involved Google Maps and MyMaps KML routes, highlighting AI's surprising ability to suggest useful map authoring mode features.
tags: [ai-coding-agents, ai-agents, claude-code, github-pages, google-maps, data-visualization, mapping, llms]
---

I had Claude Code with Fable create a small scrollytelling map for my [14-minute walk](https://sanand0.github.io/datastories/security-at-bagmane-capital/) experience at [Bagmane Capital](https://www.s-anand.net/blog/security-at-bagmane-capital/) in Bangalore.

I used this as an opportunity to explore the current status of the technology. [ChatGPT](https://chatgpt.com/share/6a537375-5308-83ee-ab03-00e39d8cc05a) suggested: <!-- https://chatgpt.com/c/6a520c51-2e08-83e8-8073-a1b703bdd45c -->

<section ai-disclosure="ai-generated" data-ai-model="gpt-5.6-sol" data-ai-provider="OpenAI">

1. **Try ArcGIS StoryMaps first** for a polished scrollytelling story.
2. **Try Google Earth Projects** if this is primarily something you will present live, like a map-based slide deck.
3. **Use MapLibre GL JS with a coding agent** if you want precise choreography, animated routes, unusual visual effects, or an asset you can continually extend.

</section>

None of these fit my requirements, which was:

- Hostable, self-contained, on GitHub Pages
- Forever free tiles, to the extent possible

Based on its recommendations, my workflow was:

1. **Capture locations in Google Maps**. Right-click and copy the latitude, longitude.
2. **Capture routes in [Google My Maps](https://mymaps.google.com)**. This was insight. MyMaps lets you export driving, walking, and cycling routes as KML. (No bike routes, though.)
3. Create a single-page index.html using **MapLibre GL JS with a free OpenFreeMap basemap**.

I [created the MyMaps routes](https://www.google.com/maps/d/u/0/edit?mid=1EmnW_jW6nP22MBJAlFg0R66CfBt9Fw8)...

[![](https://files.s-anand.net/images/2026-07-12-creating-a-scrollytelling-map-google-mymaps.avif)](https://www.google.com/maps/d/u/0/edit?mid=1EmnW_jW6nP22MBJAlFg0R66CfBt9Fw8)

... exported layers as KML files, and meta-prompted Codex with my story written in this form:

```markdown
I was staying at [The Curzon Court, Brigade Road](https://maps.app.goo.gl/ArHn75eAihHzZXcr9). 12.97454856819103, 77.60788450296555

I needed to be at [Microsoft Luxor North Tower](https://maps.app.goo.gl/Tf5qZGwXogetSJr46) 12.984402817080221, 77.70407412470264
for a 2 pm [workshop](https://hasgeek.com/fifthelephant/when-data-is-for-agents-workshop/).

So I came over to [Seetharampalya Metro Station](https://maps.app.goo.gl/Z4deFUzZsqamcCZC9) 12.98116461318051, 77.70872373073122
and seated myself at [Fairfield by Marriott](https://maps.app.goo.gl/NJqUfFnHL4QW8xa2A) 12.981961760138114, 77.70869689674738
by 11 am.

...
```

... and also attached a series of `.kml` files for the routes. The generated prompt had some _nice_ suggestions, such as:

<section ai-disclosure="ai-generated" data-ai-model="gpt-5.6-sol" data-ai-provider="OpenAI">

- Break the story into well-paced scenes, preserving its dry, escalating humour.
- Make time pressure visible through restrained clocks, timestamps, distance and ETA annotations.
- Build tension toward the late arrival, then treat the security confrontation with deadpan repetition.
- End quietly and anticlimactically at Bug & Bean with the peri peri paneer sandwich.
- ... etc.

</section>

But one interesting idea I didn't explore was to "Have the coding agent add an authoring mode", specifically:

<section ai-disclosure="ai-generated" data-ai-model="gpt-5.6-sol" data-ai-provider="OpenAI">

In authoring mode:

- Clicking the map copies `[longitude, latitude]`.
- **Copy camera** copies the current center, zoom, bearing and pitch.
- **Copy visible bounds** copies southwest and northeast coordinates.
- **Import KML/GeoJSON** previews routes.
- Selecting a route offers **Create fit chapter**.
- Clicking a marker offers **Create point chapter**.
- A panel shows the exact chapter JSON.
- Pressing `C` copies the current camera.
- Pressing `P` creates a placemark.
- Pressing `B` creates a fit-to-bounds instruction.

</section>

This is a great idea - fairly easy to implement, meaning that I can even do away with map authoring software in the future.

AI agents write software, but also know _what_ software features are useful. That makes taste more niche (i.e. I'll use / buy your software if I already know and totally align with your taste, but otherwise, I'll mix-and-match and build my own.)
