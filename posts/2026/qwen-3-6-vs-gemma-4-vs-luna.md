---
title: Qwen 3.6 vs Gemma 4 vs Luna
date: 2026-09-27T21:30:30+08:00
categories:
- llms
---

Open weights models are nudging up the frontier.

For example, [MiMo V2.6 Pro](https://openrouter.ai/xiaomi/mimo-v2.6-pro) is an outlier on the [Artificial Analysis Intelligence vs Cost per Task benchmark](https://artificialanalysis.ai/models?cost=intelligence-vs-cost-per-task#price-cost)

[![](https://files.s-anand.net/images/2026-09-27-artificial-analysis-intelligence-vs-cost-per-task.avif)](https://artificialanalysis.ai/models?cost=intelligence-vs-cost-per-task#price-cost)

[GLM 5.3 Flash](https://openrouter.ai/z-ai/glm-5.3-flash) is an outlier on the [Arena Text Pareto](https://arena.ai/leaderboard/text/overall/pareto)

[![](https://files.s-anand.net/images/2026-09-27-arena-text-pareto.avif)](https://arena.ai/leaderboard/text/overall/pareto)

[Deepseek V4.1 Flash](https://openrouter.ai/deepseek/deepseek-v4.1-flash) seems to be doing a great job as well.

So, I thought I'd relook which model to use locally for coding.

BTW, I don't use local models for coding. It's pointless, except on flights with power sockets. Partly in preparation for flights, and partly to check if I'm missing something, I benchmarked two models I could run locally on my 8 GB RTX 2000 GPU: Gemma 4 E4B and Qwen 3.6 against GPT 6 Luna. (Better models like Qwen 3.8, MiMo V2.6 Pro, GLM 5.3 Flash, Deepseek V4.1 Flash, etc. are too big for my GPU.)

I asked ChatGPT to look at my recent coding work and suggest 3 prompts. It did:

1. [flare-loading](https://github.com/sanand0/llmevals/blob/d906e9a47aa6110c50c6706e99796543e82eb4c5/qwen-3.6-vs-gemma4-e4b/tasks/flare-loading/prompt.md): Make a large image-heavy page load better on a poor network without reducing image quality.
2. [mcpserver-console](https://github.com/sanand0/llmevals/blob/d906e9a47aa6110c50c6706e99796543e82eb4c5/qwen-3.6-vs-gemma4-e4b/tasks/mcpserver-console/prompt.md): Make rapidly scrolling MCP tool logs easier to understand without
3. [whatsapp-integrity](https://github.com/sanand0/llmevals/blob/d906e9a47aa6110c50c6706e99796543e82eb4c5/qwen-3.6-vs-gemma4-e4b/tasks/whatsapp-integrity/prompt.md): Detect corrupt/misattributed backup JSONL safely before touching WhatsApp/CDP.

I gave the task to all three models. [Here's what happened](https://github.com/sanand0/llmevals/blob/d906e9a47aa6110c50c6706e99796543e82eb4c5/qwen-3.6-vs-gemma4-e4b/README.md):

| Task               | Gemma 4 E4B               | Qwen 3.6                                     | GPT-6 Luna                 |
| ------------------ | ------------------------- | -------------------------------------------- | -------------------------- |
| flare-loading      | [🔴 Didn't fix][SG1]      | [🟡 Preloaded but didn't optimize][SQ1]      | [🟢 Optimized][SL1]        |
| mcpserver-console  | [🔴 Didn't complete][SG2] | [🟡 Improved readability but timed out][SQ2] | [🟢 Concise solution][SL2] |
| whatsapp-integrity | [🔴 Didn't complete][SG3] | [🟡 Built a solution but timed out][SQ3]     | [🟢 Concise solution][SL3] |

[SG1]: https://github.com/sanand0/llmevals/blob/d906e9a47aa6110c50c6706e99796543e82eb4c5/qwen-3.6-vs-gemma4-e4b/results/gemma/flare-loading/diff.patch
[SG2]: https://github.com/sanand0/llmevals/blob/d906e9a47aa6110c50c6706e99796543e82eb4c5/qwen-3.6-vs-gemma4-e4b/results/gemma/mcppserver-console/diff.patch
[SG3]: https://github.com/sanand0/llmevals/blob/d906e9a47aa6110c50c6706e99796543e82eb4c5/qwen-3.6-vs-gemma4-e4b/results/gemma/whatsapp-integrity/diff.patch
[SQ1]: https://github.com/sanand0/llmevals/blob/d906e9a47aa6110c50c6706e99796543e82eb4c5/qwen-3.6-vs-gemma4-e4b/results/qwen/flare-loading/diff.patch
[SQ2]: https://github.com/sanand0/llmevals/blob/d906e9a47aa6110c50c6706e99796543e82eb4c5/qwen-3.6-vs-gemma4-e4b/results/qwen/mcppserver-console/diff.patch
[SQ3]: https://github.com/sanand0/llmevals/blob/d906e9a47aa6110c50c6706e99796543e82eb4c5/qwen-3.6-vs-gemma4-e4b/results/qwen/whatsapp-integrity/diff.patch
[SL1]: https://github.com/sanand0/llmevals/blob/d906e9a47aa6110c50c6706e99796543e82eb4c5/qwen-3.6-vs-gemma4-e4b/results/codex/flare-loading/diff.patch
[SL2]: https://github.com/sanand0/llmevals/blob/d906e9a47aa6110c50c6706e99796543e82eb4c5/qwen-3.6-vs-gemma4-e4b/results/codex/mcppserver-console/diff.patch
[SL3]: https://github.com/sanand0/llmevals/blob/d906e9a47aa6110c50c6706e99796543e82eb4c5/qwen-3.6-vs-gemma4-e4b/results/codex/whatsapp-integrity/diff.patch

In short, there's still no reason I'd use a local model for coding. But if I _did_ have to, I'd use Qwen 3.6 today.

---

The process of benchmarking is becoming increasingly easy. Here's roughly how I created [this benchmark](https://github.com/sanand0/llmevals/tree/d906e9a47aa6110c50c6706e99796543e82eb4c5/qwen-3.6-vs-gemma4-e4b) entirely using ChatGPT in about half a dozen prompts:

1. I've been using gemma4:e4b-it-qat and it's working fine. Several new models have been released since. What would you now recommend as the best model I can run on my laptop using ollama?
2. What's the easiest way for me to set up and use Qwen 3.6 with llama.cpp and use it via pi agent?
3. Suggest 3 tasks that I can use to benchmark or compare the quality of these models. Something where I can instantly / easily judge the output and is likely to produce a difference between these models (and GPT 6 Luna - which I'll add later into the benchmarks.) You're welcome to iterate a few times to see if it really provides an output that's well differentiated and easy for me to see the difference.
4. OK. Create, under `~/code/llmevals/qwen-3.6-vs-gemma4-e4b/` a set of directories for each of these tasks (perhaps one set for qwen and one set for gemma? I'll leave it to you to decide the best organization) as well as a benchmark.sh that I can run which will update / fix the directories. Commit the files. When done, let me know. I will run benchmark.sh. Then you can review the output and compare the quality. I'll do the same. We'll compare notes and decide next steps.
5. Now modify benchmark.sh so that it will run for codex.
6. Compare the results and let me know what you think. Then I'll share my opinion.
