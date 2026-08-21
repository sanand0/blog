---
title: Sambar Styles
date: 2026-04-26T20:21:51-04:00
categories:
- data
- visualisation
description: I used a dataset of about 2,000 sambar recipes to train a decision tree. It rarely identified states, but distinctive ingredient combinations revealed styles such as amti and Kerala coconut-tempering.
tags: [data-analysis, decision-trees, data-visualization]
---

My wife's [sambar](https://en.wikipedia.org/wiki/Sambar_(dish)) tastes different from my mother's. And mine, too. When I cooked as a bachelor, my neighbour would pop by, taste the sambar, and exclaim, "[Rasam](https://en.wikipedia.org/wiki/Rasam_(dish)) super!"

[Surbhi's Day 5 of the 30-day challenge was about Sambar](https://www.linkedin.com/posts/surbhi-bhatia_looked-at-43-sambar-recipes-across-five-south-share-7452601712604811264-b_6o/) which inspired me to take [her dataset](https://docs.google.com/spreadsheets/d/1l7Xu3j4tPHMiouh_BcT6pWu4OMhFWM5eKsKT_dntGRs/edit?gid=710450701#gid=710450701) and create a decision tree for which state a sambar recipe is from based on its ingredients.

<!-- https://chatgpt.com/c/69ee8bca-cca8-83ea-bf04-600d49e49ba4 -->

[ChatGPT](https://chatgpt.com/share/69eeac30-d330-83ea-8632-1e37e0a4191a) started with 68 recipes and built a tree at **41% accuracy**. As we added more recipes:

| Recipes | Accuracy |
| ------: | -------: |
|      68 |      41% |
|     293 |      42% |
|     361 |      55% |
|     406 |      54% |

... the accuracy wasn't improving all that much.

Here is the classifier script: [`sambar_fftree.py`](https://files.s-anand.net/blog/2026-04-26-sambar-styles/sambar_fftree.py). You can run it via:

```bash
uv run https://files.s-anand.net/blog/2026-04-26-sambar-styles/sambar_fftree.py
```

But a ingredients are **snipers**: rare, precise, devastating.

- **Kokum or goda masala -> Maharashtra.** 32 for 32 in one run. Perfect.
- **Sesame/gingelly oil -> Tamil Nadu.** 28 for 32. Strong.
- **Coconut oil + shallots -> Kerala.** 22 for 29.
- **Moong dal + no mustard seeds -> Andhra.** 31 for 36. Better than garlic.
- **Byadagi chillies -> Karnataka.** 6 for 7. Tiny sample, but clean.

But without some of these strong signals, the sambar could be from _anywhere_. Better to abstain when unsure.

![](https://files.s-anand.net/images/2026-04-26-sambar-styles.avif)

Here is the classifier that allows abstentions: [`sambar_fftree_abstain.py`](https://files.s-anand.net/blog/2026-04-26-sambar-styles/sambar_fftree_abstension.py) and the [dataset I used](https://files.s-anand.net/blog/2026-04-26-sambar-styles/sambar_recipe_dataset.csv). You can run it via:

```bash
# Download the files
wget https://files.s-anand.net/blog/2026-04-26-sambar-styles/sambar_recipe_dataset.csv \
     https://files.s-anand.net/blog/2026-04-26-sambar-styles/sambar_fftree.py \
     https://files.s-anand.net/blog/2026-04-26-sambar-styles/sambar_fftree_abstension.py
# Run the script with the data I used
uv run sambar_fftree_abstension.py --no-download
```

Only about a third of recipes have a clear signal.

Incidentally, **Coconut** alone is not a Kerala signal. It's more "west coast".

| State       | Uses grated coconut |
| ----------- | ------------------: |
| Karnataka   |                 60% |
| Kerala      |                 58% |
| Maharashtra |                 32% |
| Tamil Nadu  |                 24% |
| Andhra      |                 14% |

**Garlic** is not Andhra either. In one run, `garlic + no coconut` was a 50-50 split between Andhra and Maharashtra.

Rather than states, it's better to think of styles.

| Style                    | Ingredients                         |
| ------------------------ | ----------------------------------- |
| Amti                     | kokum, goda masala                  |
| Tamil tiffin-sambar      | sesame oil, sambar powder, tamarind |
| Kerala coconut-tempering | coconut oil, shallots               |
| Andhra pappu/charu       | moong dal, less mustard             |
| Karnataka sweet-roasted  | byadagi, jaggery, coconut           |

Maharashtra is easy to identify if it's _amti_ style. Without kokum or goda masala, it's generic sambar.

Tamil Nadu sambar has two distinctive styles: sesame/gingelly oil; or sambar powder + tamarind.

With all of this, we could identify the state only about one-third of the time based on ~2,000 recipes. But we _can_ identify the distinctive styles from their ingredients, when it's present.

Like my bachelor-days sambar, which was missing dal. (No one told me sambar needs dal.) And my neighbour could identify it instantly. As rasam.
