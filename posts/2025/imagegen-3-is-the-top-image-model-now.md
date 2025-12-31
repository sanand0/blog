---
title: ImageGen 3 is the top image model now
date: "2025-03-10T04:03:42Z"
lastmod: "2025-03-10T04:03:43Z"
categories:
  - llms
wp_id: 3960
---

![ImageGen 3 is the top image model now](/blog/assets/kaladin-1.webp)

Gemini's ImageGen 3 is rapidly evolving into a very powerful image editing model. In my opinion, it's the best mainstream image generation model.

Ever since it was released, it's been the most realistic model I've used. I've been using it to imagine characters and scenes from [The Way of Kings](https://en.wikipedia.org/wiki/The_Way_of_Kings). For example, when I wanted to visualize [Helaran's first appearance](https://coppermind.net/wiki/Helaran_Davar), I just quoted the description:

> Draw this. Galloping directly toward them was a massive black horse bearing a rider in gleaming armor that seemed to radiate light. That armor was seamless—no chain underneath, just smaller plates, incredibly intricate. The figure wore an unornamented full helm, and the plate was gilded. He carried a massive sword in one hand, fully as long as a man was tall. It wasn’t a simple, straight sword—it was curved, and the side that wasn’t sharp was ridged, like flowing waves. Etchings covered its length. It was beautiful. Like a work of art. Cenn had never seen a Shardbearer, but he knew immediately what this was. How could he ever have mistaken a simple armored lighteyes for one of these majestic creatures?

And it generated this:

![](/blog/assets/helaran-1.webp)

Or, to visualize [Highprince Roion](https://coppermind.net/wiki/Roion):

> Draw this. Highprince Roion stood in front of one of the maps, hands clasped behind his back, his numerous attendants clogging the other side of the gallery. Roion was a tall, light-skinned man with a dark, well-trimmed beard. He was thinning on top. Like most of the others, he wore a short, open-fronted jacket, exposing the shirt underneath. Its red fabric poked out above the jacket’s collar.

![](/blog/assets/roion-1.webp)

Here's the first appearance of [Kaladin](https://coppermind.net/wiki/Kaladin):

> Draw this. A man walked up through the ranks, carrying a shortspear that had two leather knife sheaths strapped to the haft. The newcomer was a young man—perhaps four years older than Cenn’s fifteen—but he was taller by several fingers than even Dallet. He wore the common leathers of a spearman, but under them was a pair of dark trousers. That wasn’t supposed to be allowed. His black Alethi hair was shoulder-length and wavy, his eyes a dark brown. He also had knots of white cord on the shoulders of his jerkin, marking him as a squadleader.

![](/blog/assets/kaladin-1.webp)

The images are stunning in quality, reproduce the prompt quite faithfully, and cost [2-4 cents each](https://cloud.google.com/vertex-ai/generative-ai/pricing#imagen-models) (via the API.)

---

But this is just the begining of power of ImageGen 3. For those with access, you can **edit existing images**, e.g.

- [Inpainting](https://cloud.google.com/vertex-ai/generative-ai/docs/image/edit-inpainting): add stuff to images
- [Outpainting](https://cloud.google.com/vertex-ai/generative-ai/docs/image/edit-outpainting): extend an image, zooming out
- [Product editing](https://cloud.google.com/vertex-ai/generative-ai/docs/image/edit-product-image): replace the background with something else (actually, this is powerful for lots of things beyond products)
- [Styling](https://cloud.google.com/vertex-ai/generative-ai/docs/image/edit-personalization): change the style of an image (e.g. photo to comic)
- [Changing the context](https://cloud.google.com/vertex-ai/generative-ai/docs/image/subject-customization): draw this dog but in a different setting
- … and more

A fair bit of this can be done by selecting a region (masking) or [mask-free](https://cloud.google.com/vertex-ai/generative-ai/docs/image/edit-images).

I'm really looking forward to this.

[LinkedIn](https://www.linkedin.com/feed/update/urn%3Ali%3AugcPost%3A7304716144379076608)
