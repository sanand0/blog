---
name: generate-fake-data
description: Use when creating REALISTIC synthetic data leading to actionable business hypotheses.
---

STEP 1. Research who the audience might be and their objective / key questions / pain points. Generate actionable hypotheses that'd make them go "Wow! We have this exact problem and never quantified it." Each must be:

- Counter-intuitive (NOT the first thing a domain expert would guess)
- Actionable (they could change something tomorrow)
- Slightly embarrassing (it implies a blind spot they should have caught)
- Expressible as a one-sentence headline: "We found that X, but only in Y"

These hypotheses should NOT be something that appears in a standard MBA case study or industry report. If a consultant could have guessed it without seeing the data, it's too obvious.
Build a 2-3 level hierarchical taxonomy of bottlenecks, edge-case customer behaviors, and silent failures listing the obscure, annoying realities and sample from these.
Then, pick hypotheses:

- 2 that are slightly surprising (confirming a suspicion)
- 2 that are genuinely counter-intuitive
- 1 that is uncomfortable (implies a process failure or oversight)

For each hypothesis, decide what in the data would support it, where the effect should be weaker / absent / reversed, and what similar-looking pattern would be a false positive. Build these into the simulation and test them afterwards.

STEP 2. List columns that would be present in such data, briefly describing how the data might be distributed and inter-related.

Research a few numbers that keep the simulation grounded: typical volumes, base rates, timings, value ranges, seasonality, error rates, etc. Use approximate ranges. Don't copy real records. The point is to avoid a perfectly coherent fictional business whose basic economics / operations are off by 10x.

Before writing the generator, list the 5 most likely ways a domain expert would spot that this data is fake. Fix those in the design.

STEP 3. Write and run seed-randomized code to generate realistic fake data where these hypotheses are true in a statistically significant way. Remember - real data has:

- real names for people, places, products, etc. (not "Person 1", "Company A", etc.)
- extreme/unexpected distributions
- breaks in patterns
- surprising correlations
- standout entities (people, places, products, segments) that defy norms
- unusual, extreme, high-variance groups
- underutilization, phase transitions, tipping points, hidden populations, etc.

Use causal simulation where relevant, i.e. create entities (e.g., customers, machines) with hidden baseline traits and simulate entities interacting over time, with the data EMERGING from these interactions.

Don't generate the data and then flip outcomes / move rows / change labels to make the desired finding appear.
If the effect is too weak / strong, change the underlying mechanism and regenerate.
Post-processing is OK only if it's something that actually happens in the organization - e.g. an ETL rule, censoring, sampling, reconciliation, a manual override, etc.

Select a small, realistic number of rows large enough to be convincing about realism and scalability - but not too unwieldy to generate or demo.
Keep real-world prevalence realistic. If a rare segment needs more rows to make the analysis useful, create a realistic enriched sample - e.g. an audit sample, exception queue, fraud review list, escalations extract, etc. Make it clear that this is a selected sample rather than the population.

STEP 4. Generate a small sample first.

Review it WITHOUT looking at the hypotheses / hidden traits / generator logic. Act as a cynical veteran data scientist who has received this from a real organization.

What makes it look synthetic? What is suspiciously clean? What important messiness is missing? Which patterns look planted? Which rows / groups / relationships would make you ask "how was this generated?"

Add the new tells you discover to the list from STEP 2. Fix the generator, regenerate, and repeat until the important tells are gone.

Then generate the full dataset.

Generate at least 3 seeds. The hypotheses / mechanisms should survive. The exact standout people, products, dates, rankings, etc. usually should not.

If a finding only works for the showcased seed, fix the simulation rather than choosing the lucky seed.

STEP 5. Let the user download the output file(s) and the script to generate these, for reproducibility.
