---
title: Launching an app only with LLMs and failing
date: "2025-01-07T04:00:09Z"
lastmod: "2025-01-07T04:00:11Z"
categories:
  - coding
  - llms
wp_id: 3817
---

![Launching an app only with LLMs and failing](/blog/assets/DALL·E-2025-01-07-11.57.24-A-colorful-single-panel-16x9-comic-strip-in-the-style-of-classic-Calvin-Hobbes.-Calvin-a-young-boy-with-wild-hair-sits-in-a-DIY-spaceship-made-out.webp)

[Zohaib Rauf](https://zohaib.me/using-llms-and-cursor-for-finishing-projects-productivity/) suggested using LLMs to spec code and using [Cursor](https://www.cursor.com/) to build it. (via [Simon Willison](https://simonwillison.net/2025/Jan/4/llms-and-cursor/)).

I tried it. It's promising, but my first attempt failed.

### I couldn't generate a `SPEC.md` using LLMs

At first, I started writing what I wanted.

```markdown
This application identifies the drugs, diseases, and symptoms, as well as the emotions from an audio recording of a patient call in a clinical trial.
```

… and then went on to define the **EXACT** code structure I wanted. So I spent 20 minutes spec-ing [our application structure](https://www.s-anand.net/notes/#/gpts?id=gramener-demos) and 20 minutes spec-ing our internal [LLM Foundry APIs](https://www.s-anand.net/notes/#/gpts?id=llm-foundry) and 40 minutes detailing **every step** of how I wanted the app to look and interact.

After 90 minutes, I realized that I'm too controlling or too inexperienced in LLM-speccing. But I had a solid [`SPEC.md`](https://github.com/gramener/patientpulse/blob/689d7870cd71e47b07d330d4fddec86e561e0798/SPEC.md).

`````markdown
# Patient Pulse

The application identifies the drugs, diseases, and symptoms, as well as the emotions from an audio recording of a patient call in a clinical trial.

## How the application works

The application is a [Gramener Demo](#gramener-demos).

`script.js` implements this logic:

- Reads `config.json` to get the list of transcripts and renders them, allowing users to select a transcript
- When the user selects a transcript, it reads the audio and prosody files

Once it reads these files, it makes a request to GPT-4o-mini via [LLM Foundry API](#llm-foundry) with the system prompt:

````markdown
You are a clinical trial expert. Read this call transcript. Identify all drugs, diseases, and symptoms mentioned. Return a JSON that mentions each along with the line in the call transcript they occur in. Example:

```json
{
  "symptoms": [
    { "name": "...", "lines": [1, 4] }, // first symptom is mentioned in lines 1, 4
    { "name": "...", "lines": [8] } // second symptom is mentioned in line 8
  ],
  "drugs": [
    { "name": "...", "lines": [6] } // first drug is mentioned in line 6
  ],
  "emotions": [
    { "name": "...", "lines": [9] } // first emotion is mentioned in line 9
  ]
}
```
````
`````

````
It then renders a UI (via lit-html) that

- Plays the audio
- Maps the emotions in `${filename}.prosody.csv` to the 8 basic emotions on Robert Plutchik's theory of emotions. See [How to map emotions](#how-to-map-emotions)
- Displays [wheel.png](wheel.png), which is a 1080x1080px image of Plutchik's wheel of emotions
- As the audio plays, it
  - displays text up to the currently playing `Text` from `${filename}.prosody.csv`, highlighting the current sentence.
  - displays the emotions as a semi-transparent radar chart on the wheel of emotions
- It allows pausing and resuming the audio.
- It allows users to drag the audio slider to jump to any point in the audio. The transcript and the wheel of emotions are updated to reflect the new position in the audio.

... (and it goes on for 500+ lines.)
```

I did use [O1](https://openai.com/o1/) to help with the spec. Specifically:

- **How to name it.** I asked for short demo names and chose "Patient Pulse".
- **How to arrange emotions.** I asked how to arrange 53 emotions in a circle so similar ones were next to each other.

**My takeaway**: Writing a `SPEC.md` can help, especially if you plan to re-use parts of it. But the spec kept evolving as I built the app, because I often don’t know what I want until I see it. Maybe an “agile” approach would work better for me.

### Cursor messed up the code

I prompted Cursor to `Generate an application based on this spec. @SPEC.md`. Here's the code it generated.

```javascript
import { render, html } from "https://cdn.jsdelivr.net/npm/lit-html@3/+esm";
import * as d3 from "https://cdn.jsdelivr.net/npm/d3@7/+esm";

// Map of Hume emotions to Plutchik's 8 basic emotions
const EMOTION_MAP = {
  Admiration: ["Joy", "Trust"],
  Adoration: ["Joy", "Trust"],
  "Aesthetic Appreciation": ["Joy"],
  // ... (truncated for brevity - use mapping from spec)
};

// ... skipping lots of code ...

/**
 * Main application component
 * @returns {TemplateResult} Main application UI
 */
const App = async () => {
  const config = await fetch("config.json").then((r) => r.json());
  const [selectedTranscript, setSelectedTranscript] = useState(null);
  const [audioPlayer, setAudioPlayer] = useState(null);
  const [currentTime, setCurrentTime] = useState(0);
  const [prosodyData, setProsodyData] = useState([]);
  const [analysisResults, setAnalysisResults] = useState(null);

  const loadTranscript = async (transcript) => {
    setSelectedTranscript(transcript);

  // ... skipping lots of code
};

// Initialize app
render(App(), document.getElementById("app"));
```

This code was a mess. I had told it to use `lit-html`, which doesn’t have `useState`. That’s a React feature, so nothing worked right.

I ended up building the app from scratch. It took four hours and many changes from the original spec, though having a spec did help a bit.

**My learning**: Cursor and I still can’t build a mid-sized app in one go. I’m in the "scaffold and refine" phase.
````
