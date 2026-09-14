---
name: memorable-explanations
description: Use to intuitively, memorably explain abstract, complex, unfamiliar concepts. NOT for code generation, data retrieval, or when user just needs execution.
---

People remember a:

- Face, Place, Tale, and Scale. Use these to structure (who, where, what happened, compared to what).
- Touch, Feel, Chunk, and Beat. Use these for style (make it tangible, emotional, holdable, sticky).

Structure using:

1. **Face**. We relate to people, especially "you". Even abstractions can become agents with goals: "Gravity ripped the moon apart." Or even, "Imagine _you_ are the moon".
2. **Place**. Turn ideas into spatial relationships. You're reading _down_ this list - and the top feels more important. Convert structures into positions: above/below, inside/outside, near/far. The memory palace works because spatial recall is extraordinarily durable.
3. **Tale**. Sequences create a causal chain. People assume the first event _caused_ the second. "Because" makes anything more believable, even circularly. Explain processes as journeys. **Trap**: A good story _feels_ like understanding even when the causal model is wrong.
4. **Scale**. Give comparisons, not absolutes. "Two feet tall" is more relatable than "60 cm". The brain compares, it doesn't measure. Always provide a reference object.

Style with:

1. **Touch**. Make abstractions graspable. We "grasp" ideas because we literally learned by grasping. Use concrete, manipulable nouns. Software works because it's touchable: files, folders, windows, trash. **Trap**: Students who cling to metaphors find it hard to generalize. Start concrete, then fade the scaffolding.
2. **Feel**. People decide on emotion more than arguments. When you say, "Forget these principles and your audience forgets _you_", that sting is loss framing.) Fear, surprise, and reward are memorable. **Trap**: high arousal _narrows_ cognition. Limit to one vivid moment per explanation.
3. **Chunk**. Respect the ~4 limit. Eight items here are already too much for working memory. That's why made each anchor one bolded word - it's a handle to grab. Organize material into <=4 groups and sub-groups.
4. **Beat**. Rhythms are memorable. Face, Place, Tale, Scale. Touch, Feel, Chunk, Beat. Say them aloud and you'll feel it. Rhyme, alliteration, parallel structure, and meter help remember. That's why jingles outlast lectures.

## Applying the Anchors

1. **Audit:** What makes the concept hard? Invisible -> Touch. Large-scale -> Scale. Causally complex -> Tale. Structurally dense -> Chunk.
2. **Pick 2-4** whose structure mirrors the concept. Not every explanation needs all eight.
3. **Stack, don't scatter.** "Imagine _you're_ standing inside a database index" is Face + Place + Touch in one sentence.
4. **Flag where the anchor lies.** Every anchor is also a bias. "The electron _wants_ ground state - though electrons don't have desires; it's energy minimization."
5. **Plan the fade.** Start concrete, then gradually introduce the formal abstraction. The goal is independence from the metaphor.

## Example: DNS Resolution

Without anchors: "DNS resolution translates domain names into IP addresses via hierarchical nameserver queries."

With anchors:

> Imagine YOU type "google.com." [Face] Your computer doesn't know where Google
> lives - it only knows a local guide, the resolver. [Face: agent]
>
> Say you're in an unfamiliar city. [Place + Touch]
> You ask a local,
> who asks the information desk (root server),
> who says: ".com? Ask the TLD server down that hall for Google",
> who says: "Google? Here's their nameserver, ask for the IP",
> who hands back 142.250.80.46 - the address. [Tale: journey, Place: directions]
>
> That takes ~50ms - faster than a blink. [Scale] But when it breaks, you're
> frustratingly lost on the internet. [Feel]

Four characters, one journey, one emotional beat. [Chunk + Beat]
