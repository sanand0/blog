---
title: What do you need to interact effectively with LLMs?
date: "2024-09-15T10:04:43Z"
lastmod: "2024-09-15T10:16:46Z"
categories:
  - links
wp_id: 3629
---

![What do you need to interact effectively with LLMs?](/blog/assets/DALL·E-2024-09-15-18.12.42-A-colorful-comic-strip-style-image-featuring-Calvin-a-young-boy-with-spiky-hair-and-Hobbes-a-tall-tiger-talking-to-a-small-alien-creature.-The-ali.webp)

Simon Willison [asked on Twitter](https://x.com/simonw/status/1832944559162269990):

> What are the most importantly things that people need to understand in order to effectively interact with LLM-based systems like ChatGPT or Claude?

Here are the replies. (I used text-embedding-3-small to embed and cluster them into 20 clusters and used OpenAI GPT-4o-mini to label the clusters. There are misclassifications but the themes are accurate.)

### Provide Clear Context and Avoid Leading Questions

1.
   1. Provide relevant context but not too much \
   2. Models are total "yes men" - be careful not to imply your perspective if you want an objective response \
   3. Learn when to iterate vs start a new chat 4. Provide examples (especially for output structure) - [Tweet](https://x.com/VoloBuilds/status/1832950783584735343)
2.
   1. Ask questions that the other person can understand. \
   2. Ask questions while predicting what the other person will respond. It's the same as the human's. - [Tweet](https://x.com/thaichi_ffbe/status/1833039995210481713)
3.
   1. Ensure the system knows the relevant context. Give a detailed backstory of what you're trying to do with it and why. \
   2. One thing at a time. Make the task as specific as possible and if there are multiple things that need to be done, ask it to them in their sort of natural - [Tweet](https://x.com/0xRohitSinghal/status/1833146095133679697)
4. The "most importantly things" are probably to ask for step-by-step before answering and to try to not ask leading questions to avoid its sycophancy bias. - [Tweet](https://x.com/TakiVan1/status/1832979680028508336)
5. You must provide a diverse distinct set of examples of you want it to be robust and generalize in real world systems. - [Tweet](https://x.com/nem035/status/1832946481193456027)
6. Always ask for both strengths and weaknesses to get more balanced perspectives, and make sure the model can tell you as many facts as possible before committing itself to an answer. - [Tweet](https://x.com/FremyCompany/status/1833035154882724204)
7. Rule 1:Avoid chatgpt unless they release a better model than Sonnet 3.5. - [Tweet](https://x.com/karen95926/status/1833045021144019167)
8. Strongly insist that it shouldn’t passively agree with you. Encourage it to interrupt with clarifying questions that would meaningfully improve the output. - [Tweet](https://x.com/crinzo_/status/1832959545900949544)
9. Avoid leading questions if you care about the answer. They are way too polite to contradict the user. - [Tweet](https://x.com/eirikbakke/status/1832946920790139332)
10.
    - It's not Google, so use full sentences, not just keywords. \
    - Iterate on initial response. \
    - Trust, but verify. - [Tweet](https://x.com/var_tec/status/1833053213643182113)
11. Just talk to them how you'd want someone to talk to you if it was you in there. - [Tweet](https://x.com/Frogisis/status/1833057320818847933)
12. Provide good (and bad) examples of output, and don't forget a few edge cases. - [Tweet](https://x.com/mrdavediamond/status/1833101615617712257)
13. Keep hitting the ball back and forth across the net: 1. "thanks but I think these are a little too 'salesy' -- could you try to generate some ideas that are a little more down to earth" 2. "ok, we are getting there, but still a little overheated. could you try again" - [Tweet](https://x.com/adamdavidlong/status/1833007221363650786)
14. These are my top 10 for folks new to GenAI: 1. You have to provide all of the context the model needs to answer your question if that context is not likely to appear in the model's weights. It will take a while to gain an intuition about what types of knowledge is likely to be - [Tweet](https://x.com/gooby_esq/status/1832949271357735189)
15. Suspend disbelief; collaborate not interrogate; trust no-one; have fun, role play, experiment, test; think of as a facet of intelligence built on achievements of ours, not a robo-rival. Notice book-learning over lived experience, cliches & bluffing in human world too, & do better - [Tweet](https://x.com/danbri/status/1832982553105461601)
16. It’s a dialogue. Iterative. incremental. Chat improves with feedback. When chat creates code, for example, run the code and give chat the error messages so that it can correct the code. Before asking chat a question, ask it what it knows. Then zoom in. Gradually. :) - [Tweet](https://x.com/ParisWriters/status/1833055742229684293)
17. One example is worth a thousand words - [Tweet](https://x.com/Drk8_/status/1833011241897370045)
18.
    1. How to read \
    2. How to write (optional) - [Tweet](https://x.com/yungbzz/status/1833133091558219914)
19.
    1. Explain yourself clearly, using lots of examples. \
    2. Assume you’re talking to a smarter version of yourself that hasn’t heard about your problem yet. \
    3. When it doesn’t do well, use the steps above to correct it. - [Tweet](https://x.com/DanielMiessler/status/1832961380577935535)
20.
    1. The more precise your question or task is, the better and more accurate the response will be. Vague prompts can result in equally vague answers. \
    2. Provide relevant background or context, especially for nuanced questions or tasks. - [Tweet](https://x.com/esti_wiz/status/1833148201207001130)
21.
    1. Don’t ask them to do too much in one shot, especially if they are unrelated tasks; you’ll get much worse results. \
    2. Don’t give too much context if you can avoid it. The huge context windows of the newest models isn’t as “free” as you might think, or rather it’s “lossy”— the - [Tweet](https://x.com/doodlestein/status/1832962594518548731)
22. Collaborate with them, don't delegate to them. - [Tweet](https://x.com/sstopp2/status/1833034087696654433)
23. Context Window needs to be explained well. @NickADobos is spot on, but this needs to be explained without jargon we are so used to. - [Tweet](https://x.com/DataDeLaurier/status/1832961289297019069)
24.
    1. How context windows work TL;DR: it doesn’t remember everything in chat \
    2. It’s a text generator, that is good at patterns, and appearing smart. Not an almighty god doing cognitive work. Hallucinations aren’t ai behaving wrong. They are a feature of generating a bad pattern - [Tweet](https://x.com/NickADobos/status/1832947279625650200)
25. Consider the context a human would need when responding to the same request. When asked to create a presentation by your manager with 10-20 words, you have thousands or likely millions in context to inform that. Ppl often get annoyed when it fails, it’s usually not enough context - [Tweet](https://x.com/bye_eric/status/1833001179111923737)
26. Understand that they are autoregressive with a context limit and the limitations that impose on the chat interface. - [Tweet](https://x.com/w_rodrigo_rr/status/1833126734360690965)

### Iterate and Simplify for Optimal LLM Performance

1.
   1. just keep trying things - LLMs keep surprising me, \
   2. Start simple, add more techniques, context, guidance etc. step by step - with LLMs I found, less is often more. \
   3. Keep a human in the loop and/or be transparent about using LLMs - otherwise prepare for unpleasant - [Tweet](https://x.com/MitjaMartini/status/1833031787267621004)
2. When your llm starts omitting code generated in prior steps of an existing chat, end the chat and replay your steps until before that happened. Take a different branch next time - [Tweet](https://x.com/darin_gordon/status/1832955696532398311)
3.
   1. Don't give too much information at once to process, start simple and build on top of previous ones \
   2. Want a contrary opinion from LLM?don't sound like your opinion is sacrosanct - it will agree to you mostly even if its wrong. \
   3. Role playing and few shot examples matter. - [Tweet](https://x.com/artofseeing23/status/1832990869370101997)
4.
   1. Context \
   2. Difference is assumptions \
   3. Articulating clearly what you want (run it against another LLM to see if what you mean is what you say). \
   4. Being able to go back in a thread and restart (You get do over's with LLMs that you might not get with people :) ) - [Tweet](https://x.com/arjunram/status/1832945871278723453)
5. Well one thing I learned is it's best to start a new chat if the LLM is going down the wrong path, easier then forcing it back. - [Tweet](https://x.com/CianPrend/status/1833174947943882808)
6. Having moderate experience with a topic / framework is important for peak quality of the response. At present, using llms for efficiency > using llms to do something you don’t know how to do. - [Tweet](https://x.com/tlofreso/status/1832947258423206108)
7. at least when it comes to writing code, the task needs to be very well defined, like one would do when creating a user story for developing software. If the details are vague then you leave the LLM open to interpretation and more likely to make mistakes - [Tweet](https://x.com/juanstoppa/status/1833268880346943501)
8. The most important thing, and this has always been true even if not using an LLM, all good software development starts with engineering a solution first before building it. If you attempt to get the LLM to do that part you'll create as many problems than you solve building - [Tweet](https://x.com/ShayneALong/status/1832967621274399170)
9. Use the LLM to explore your own understanding of the problem space and what you want to achieve. This can help improve your prompting and interpretation of the outputs. - [Tweet](https://x.com/Rik_Chin/status/1833097840114999432)
10. LLMs…\
    -Pander. Don't prime answers, ask straight.\
    -Only know text. Don't ask spatial, reasoning etc.\
    -Hallucinate and invert. Double-check.\
    -Get stuck. Start over.\
    -Master ALL languages, jargons, styles etc.\
    -Are formidable documentalists. - [Tweet](https://x.com/bruno_mailly/status/1833157893727605087)
11.
    1. hallucinations are still a thing, be wary when LLMs generate links and code snippets 2. data quality of training content can sometimes be dubious leading LLMs to hallucinate more often or be biased in various ways both will likely be addressed eventually - [Tweet](https://x.com/leadstaffeng/status/1833020673339572607)
12. LLMs…\
    -Pick and imitate register. Talk like constructive, competent people.\
    -Are easily lost. Examples and feedback help.\
    -Can misbehave. Be harsh if needed, but stay just. - [Tweet](https://x.com/bruno_mailly/status/1833166154505834524)
13. For optimal results, provide ample context. Prompting the LLM with 'Feel free to ask clarifying questions' and doing the due-diligence to answering the questions often yields much better results. - [Tweet](https://x.com/razhangwei/status/1833389182422814786)
14. The more explicit you are the better the output. The LLM can not read your mind and there is a lot of ambiguity when interpreting language. - [Tweet](https://x.com/patleeman/status/1833130400664739870)
15. One issue I am seeing more of - Often i ask a question on a choice it made. The LLM assumes I don’t like it or it’s wrong - it then starts to apologize and course correct. More and more I add something like “not refuting or arguing, just trying to understand” etc. - and that - [Tweet](https://x.com/manpreets7/status/1832963057662013663)
16. They are inherently unreliable in more than one sense, which accumulates the more requests you run in a chain. The Six Sigma approach is devastating to LLMs. - [Tweet](https://x.com/eckely/status/1832981711648325898)
17. Treat it like a very intelligent junior employee who just started at your company and lacks context. Give the LLM the same level of detail for every instruction you would give to this junior employee. - [Tweet](https://x.com/MalteLandwehr/status/1833084687629087088)
18. That LLMs are not too be trusted as they reliably fail at information due to multiple effects, including hallucinations. That LLMs don't actually understand things and don't have common sense. It is mandatory to adapt expectations and ways of working to successfully use them. - [Tweet](https://x.com/toncijukic/status/1833020660056051815)

### Craft Effective Prompts for Consistent Results

1. How to prompt - [Tweet](https://x.com/datasiphon/status/1833065857678745823)
2. Carefully consider keywords, and prioritise them via the locating them earlier and at the end of longer prompts. - [Tweet](https://x.com/mrdavediamond/status/1833101120232738883)
3. If you want stable results across models and are looking to build robust pipelines you should stop hand writing prompts and move toward prompt optimizers. https://ycombinator.com/launches/L4V-hamming-let-ai-optimize-your-prompts-free-for-7-days… Also built into DSPy! - [Tweet](https://x.com/thedayisntgray/status/1833111674385261025)
4. While crafting logics and system prompts, Always keep a thought in your mind parallel what would I respond to this prompt and context. - [Tweet](https://x.com/_arindam/status/1833216989671662037)
5.
   1. Prompts matter. \
   2. Treat it like a tool, and you'll get a tool. It's only as smart as you let it be. - [Tweet](https://x.com/nptacek/status/1832945915541286996)
6. to ask them the best way to prompt them - [Tweet](https://x.com/cwizprod1/status/1832968177678155925)
7. there is a single prompt that gets the job done, thousands that screws it - [Tweet](https://x.com/ekremcetinkaya_/status/1833043655956808069)
8.
   1. Always add a system prompt at the beginning: Define a role. Ex: "You are a senior software developer who excels in…" \
   2. Context Matters: Provide a detailed background for better insights. \
   3. Clear Prompts: Specificity is crucial for accurate outputs. - [Tweet](https://x.com/AhmedAmerVP/status/1832999871730643190)
9. If a large global prompt doesn't work, try step by step. If it does work, but has errors in response - Ask it to fix errors one by one. Insist, like you would with a human supplier. If "do this" doesn't work, try "Strictly do this". Amazing how effective insisting is :) - [Tweet](https://x.com/LalRitesh/status/1832964640831369586)
10. The better the prompt the better the output. You don't need a Meta framework for 90% of things - [Tweet](https://x.com/meinbiz/status/1832987136888562098)
11. They don't exist between prompts - [Tweet](https://x.com/oddEventHorizon/status/1833091289983627400)
12. Don’t rely on the models weights alone. Be explicit in the prompt and give it pointers to what you’re expecting. Let it “clean up” or “translate” your prompt rather than “come up” with an answer based on its training. Exception: generating lists for inspiration. - [Tweet](https://x.com/ahmadh/status/1832987993176461425)
13. prompt engineering, in order to get the most desired outcome in handy. - [Tweet](https://x.com/myjoyone/status/1833016884003827985)
14. It lies Q: Who was the second person to walk on the moon? A: Pete Conrad Q: can you name the crew members of Apollo 11? A: I got the right answer. Q: Then how come Pete Conrad was the second person to walk on the moon? A: My apologies. Indeed Buzz Aldrin was the second pe… - [Tweet](https://x.com/ssathya/status/1832957472258080985)
15. How to say no. - [Tweet](https://x.com/ykjyywmkgf/status/1833185081676214718)
16. How to use smart phone or computer with internet - [Tweet](https://x.com/ipirusman/status/1832988198227874105)
17. Vibe is an input. - [Tweet](https://x.com/Hipster_Energy/status/1833115988230811770)

### Don't Expect Human-Like Understanding from LLMs

1. LLMs have no "thoughts" or understanding, they'll simply write the statistically most probable answer based on your input and have been prompted to act as assistants. - [Tweet](https://x.com/lp1eu/status/1833048330743484668)
2. LLMs are incredibly random. Responses can change wildly based on a single character difference in the prompt. Even one extra space. They are best for prompts that have a range of possible responses, not for prompts where you expect one consistent answer. - [Tweet](https://x.com/karmacondon/status/1832994847524893145)
3. Cease prompting their LLM to give them a viral tweet with forced irony forcing awareness to an issue. That's my own personal opinion, bro. But, believe what you want. - [Tweet](https://x.com/BlueEisenhower/status/1833225298218713274)
4. If you don't know what you want, the LLMs too likely won't know. And if they don't know they will make it up. And if you don't know, you will not know that they made it up. - [Tweet](https://x.com/jamesagada/status/1833065956173590770)
5. Be sure not to put contradictions in your prompt. LLMs, in contrast to humans, try to follow instructions as close as possible. They usually handle contradictions by ignoring some part of the instructions or even ignoring facts. - [Tweet](https://x.com/Drk8_/status/1833010967535312955)
6. It's biased toward its creators. So if the majority of companies that are developing LLMs are owned by the same investors, then in fact, we are having a single LLM that is biased toward that investors goals. E.g., chatgpt is more toward liberalism and refuses to operate otherwise - [Tweet](https://x.com/NIkronic/status/1833229421504876871)
7. Basically, you need to understand that LLMs are not humans. You can't assume they'll understand what you mean when you write short prompts. You get the best out of LLMs when you provide detailed instructions of what you want without letting laziness get in the way. In my - [Tweet](https://x.com/gsusMad/status/1833039866969399719)
8. Don't assume anything. LLM doesn't learn like a human. Any assumption you make about what LLM should or shouldn't know is probably wrong. - [Tweet](https://x.com/Drk8_/status/1833007757793857651)
9. Describe your context and the role you want the LLM to look at your input (critical, tech/none-tech, …) Think what you could expect from a wise, random person you ask on the street. Do not expect more from the LLM-Answer. Also only trust it similarly. - [Tweet](https://x.com/c_gint/status/1833131350594867711)
10. Give it an option to not do something either by allowing the LLM to reply with something like "I don't know" or tell it to ask follow up questions. - [Tweet](https://x.com/DKundel/status/1833013217070547270)
11. There is nothing fundamentally important for that interaction. These LLMs are just minimum viable versions of something much bigger that will come soon. That something will know how to interact with us no matter how we behave. - [Tweet](https://x.com/MuchachoCnFuego/status/1833226024022421614)
12.
    1. that you need to cram the relevant data into the prompt. LLMs are far far better at transforming what you give them than they are at answering solely on the basis of the lossy representation of the training data encoded into the model itself - [Tweet](https://x.com/davidcrespo/status/1833148100359172545)
13. The side effect fact that formulating a question for an LLM makes you think better. When coding, for example, we often run questions in our heads and then get to coding. Being forced to formulate a question properly may lead you to trajectories you may have never considered. - [Tweet](https://x.com/abstractpaper/status/1833093374003327075)

### Treat LLMs as Guided Children, Not Mind Readers

1. The game isn't to 'one shot it'. It's to get something you never thought was possible or that you'd never think of. I always say they are like children, they need guidance (back story and reason) and repetition …but room and time to play and grow. - [Tweet](https://x.com/peterjabraham/status/1833278934613463409)
2. Honestly, flexibility and patience. We need to give up a little bit of control and expectation of all things to be so rigid. - [Tweet](https://x.com/Kyrannio/status/1832948092787962228)
3. When working with it, you need to expect it to not read your mind, but work with it as if you’re asking for help from an insanely gifted child and give yourself patience to shape the result. - [Tweet](https://x.com/envisean/status/1833001525452656850)
4. if it makes life better? yes. but always? no. - [Tweet](https://x.com/e_insomniac/status/1833339260188897397)
5. When asking it how to implement something, always give it options. If you can't think of options, give it a vague out. Instead of asking, "should I do this to my code?", ask it "should I do this to my code, or is there some better way I could do it?". Otherwise the models are too - [Tweet](https://x.com/_burkard/status/1832949249266385153)
6.
   1. always consider that it doesn’t know what assumption you’re making. so it might infer them sometimes but often it’s much better to over explain what you want.
7.
   2. they will often run ahead on a suggestion you have even if it’s not the best path so I find myself adding “if this - [Tweet](https://x.com/rez0__/status/1832945464649371748)
8. It cannot read your mind, if you don't explain exactly what you want you will not get what you want - [Tweet](https://x.com/mahaoo_ASI/status/1832966127925772357)
9. I am not ready to give advice based on a bet that “something much bigger will come soon” - prompting advice that worked for GPT-4 over a year ago is still mostly relevant to working with the best models today - [Tweet](https://x.com/simonw/status/1833226877177418159)
10. to be concise and always assume the response is wrong, even ever so slightly. Check and correct. - [Tweet](https://x.com/productaizery/status/1833511522750107836)
11.
    - you have to provide context otherwise it assumes - it will often agree with you or apologize/correct itself even if you question the right answer - [Tweet](https://x.com/khanshq/status/1832948108663120257)
12. The limited ability for non-linear (or non left-to-right) reasoning. Encouraging the model to spend more time planning and discussing beforehand often leads to better results. This may be less the case with Claude etc where reasoning tokens are happening behind the scenes. - [Tweet](https://x.com/OxxoTweets/status/1832960963374420405)

### Context is Key for Effective Interaction

1. Context is everything - [Tweet](https://x.com/FactsForFarmers/status/1833100761011556662)
2. Context is all you need. - [Tweet](https://x.com/IanTimotheos/status/1833244655057883416)
3. Understanding how context works - [Tweet](https://x.com/MatthieuM_oreau/status/1832983717729423632)
4. It’s all about context - [Tweet](https://x.com/JeffData2/status/1833567250915463608)
5. #contextmaxxing - [Tweet](https://x.com/freedabanks/status/1833192155705188419)
6. Context, Task & Purpose - [Tweet](https://x.com/samtilston/status/1833182178190000603)
7. Subjectivity. Context. Brain rent. - [Tweet](https://x.com/CompSciFutures/status/1833007358789992666)
8. I'd say understanding the concepts of context, attention, and likelihood - [Tweet](https://x.com/SaidAitmbarek/status/1833069447881408590)
9.
   1. Context and memory (the degree to which you can refer to previous parts in the chain of context) 2. Temperature and hallucinations. The tradeoff between extremes of temperature 3. It's wise to have benchmark questions of your own to test when a new company/model comes out - [Tweet](https://x.com/silly_man/status/1833043355938205994)
10. local maxima sensing - [Tweet](https://x.com/kayvulpe/status/1832990127762599937)

### Acknowledge the Stateless Nature of LLMs

1. you're interaction is with a stateless inference that exists for a fleeting moment, current ai is not continuous which is easy to forget. This has implications for what you are building for: - [Tweet](https://x.com/SirMrMeowmeow/status/1833026648809336875)
2. that they're stupid next-token predictors and not intelligent agents. If you expect conscious beings, you'll be surprised and disappointed. But they're incredibly good at predicting the next useful token. - [Tweet](https://x.com/internetope/status/1833215404597985685)
3. That standard intuitions for computers don't apply. Treat it the way you would treat a knowledgeable but fallible friend. Not like a purely logical SciFi AI with perfect memory. - [Tweet](https://x.com/wopas32/status/1832946004645036315)
4. Normally I hate predictions and terms like this, but the next 20 years are going to be the era of "embodied intelligence" People are imagining humanoid robots, this will be a very small fraction of it. Compared to the software problem, the body is trivial. Imagine asking your - [Tweet](https://x.com/realGeorgeHotz/status/1834814700745637890)
5. Inherent lack of memory about previous interactions. Every message is starting from zero and only seems coherent because background info and the previous messages and responses are sent before the latest message. - [Tweet](https://x.com/markjaquith/status/1832946450495418868)
6. They’re not sentient. They generate responses by predicting patterns from vast data, which means they're as fallible as they are impressive. The key is precision: your queries must be meticulously clear and well-contextualized. - [Tweet](https://x.com/Keshav__Thakur_/status/1833148850283876364)
7. it doesn't have a memory like hooomans - [Tweet](https://x.com/0xAyush1/status/1833147616579776565)
8. Whenever the conversation derails, you need to cut that branch and keep the model in the "right universe of probabilities" by editing prompt/messages. This is also why I was skeptical about Reflection, because if it really worked, it would be breakthrough. - [Tweet](https://x.com/cztomsik/status/1833384291822104789)
9. They aren’t deterministic - [Tweet](https://x.com/curiousgangsta/status/1832975388219203584)

### Leverage AI for Prompt Suggestions and Refinement

1. I like to ask them for prompts to use for a given purpose, it tends to be more detailed than I would be. Can also use this to add example Q&A if need be. - [Tweet](https://x.com/pbaylies/status/1832966893633691913)
2. We need AI assistance with prompts and suggestions on rewriting your queries similarly to Grammarly's for spellchecking and correctness. - [Tweet](https://x.com/deuslexic/status/1833020848363483474)
3. “Give me a list of questions I can answer to help improve the quality of the response” - [Tweet](https://x.com/bye_eric/status/1833001543873827007)
4. Let's ask one. - [Tweet](https://x.com/DonSoloway/status/1833077422167888137)
5. Can we get our hands on all the prompts used in fine tuning data or at least major ones. Highly unlikely they will release it. - [Tweet](https://x.com/akhil_katpally/status/1833351840907382876)
6. anybody got tips for image generation? i hardly ever use the image features, but lordy, they struggle! even w with clear, verbose prompts using art school vocabulary, specific artist citations, and example attachments, lots of iterations, etc. - [Tweet](https://x.com/wwwdaveturney/status/1833133119001575610)
7. I'm doing a podcast with the Cursor team. If you have questions / feature requests to discuss (including super-technical topics) let me know! For those not familiar, Cursor is a code editor based on VSCode that adds a lot of powerful features for AI-assisted coding. I've been - [Tweet](https://x.com/lexfridman/status/1835047299531128948)
8. They’re useful in the same way Google or the internet or stack overflow is useful plus one big advantage: your question doesn’t have to take your specific situation and change it to a generic case that someone else has already answered, you can just ask about your exact case! - [Tweet](https://x.com/mlipman13/status/1833295699477254568)

### Start with a Jailbreak for Objective Analysis

1. Using a jailbreak should always be your first step if you want less biased, more objective and fact-based analysis of sensitive or controversial sociopolitical issues. - [Tweet](https://x.com/jermd1990/status/1832953949713760441)
2. Kinda like Google, small changes in wording can give you quite different results. - [Tweet](https://x.com/RayScript/status/1832945339415908733)
3. That you should only use it to get answers you can verify with a separate tool, or somehow evaluate yourself (ej. text quality). - [Tweet](https://x.com/itsLondi/status/1833250687557533992)
4. Its not a tool - [Tweet](https://x.com/Rooftops01/status/1833090438858780926)
5. dont treat it like a search engine. think about the outcome and output you are trying to achieve. - [Tweet](https://x.com/jerezito/status/1833036164900569276)
6. There is a considerable chance to answer is wrong, so likely everything needs to be double checked. - [Tweet](https://x.com/HerrSchaefers/status/1833077946195509312)
7. I can only speak for the use cases I’ve come across wrt legal work, but don’t use them for tasks where you need a reference. Using them to draft or review documents is fine. Asking for a case law reference is a no-no. And of course, make sure you’re not leaking confidential stuff - [Tweet](https://x.com/vlslvv/status/1833036492806984189)

### Master Prompt Engineering for Better Outputs

1. lol. Nice try. If your business needs to level up I can do certification class. Your employees will get Level 4 Prompt Engineering Classification. DM if interested - [Tweet](https://x.com/3DX3EM/status/1833071710066663553)
2. I like to write no full sentences with error and llm understand. So prompt engineering bullshit - [Tweet](https://x.com/gerard_sanroma/status/1833397401974952129)
3. Turing test. - [Tweet](https://x.com/CChef1980/status/1833024764606079097)
4. Use instructions to change the style of the output that the LLM produces. For Claude you have to make a project first in order to be able to set the instructions. - [Tweet](https://x.com/Hasen_Judi/status/1833010210631459249)
5.
   - Understanding how LLM system, ChatGPT or Claude works and responding technically in basic. - Prompting skills. Understanding the difference between effective and ineffective prompting. - [Tweet](https://x.com/ASU__/status/1833019326074343524)
6. understand the english language and HOW it's used (sadly, even english speakers have a hard time w/ correct language use). know grammar and syntax, context and nuance. be clear, succinct, specific when creating prompt. edit, edit, edit before sending prompt. - [Tweet](https://x.com/satoforma/status/1832976418986197080)

### Understand LLMs as Statistical Predictors

1. Language models cannot generalize the simple formula "A is B" to "B is A." - [Tweet](https://x.com/datenschatz/status/1833211350954410223)
2.
   1. tokenizers/decoding strategies are both incredibly important and invisible to most users. Remember that what you input is not what the model sees exactly, and what you read is not what the model output directly. 2) repeat #1 for the crowd in the back - [Tweet](https://x.com/osoleve/status/1833126683622174954)
3. It's a bit sad and confusing that LLMs ("Large Language Models") have little to do with language; It's just historical. They are highly general purpose technology for statistical modeling of token streams. A better name would be Autoregressive Transformers or something. They - [Tweet](https://x.com/karpathy/status/1835024197506187617)
4. Language - [Tweet](https://x.com/jasiralavi/status/1833236031887577112)
5. They are next word predictors. Everything is downstream from that. - [Tweet](https://x.com/saasy_cto/status/1833014923854798993)
6. The output is encoded in the input, the model is just a statistical decompression engine. This means that they can only ever amplify your mind, they can't think for you, however they can translate your question into more formal language & that may decompress into something useful - [Tweet](https://x.com/DanielSMatthews/status/1833057775351468380)

### Stay Focused on High-Impact Tasks

1. Try to stay in the high impact zone e.g. through breaking tasks up and don't expect perfect results at all times - [Tweet](https://x.com/TommyFalkowski/status/1833378891945201815)
2. Being able to define goals and objectives. - [Tweet](https://x.com/Vlob1234/status/1832989443135074590)
3. Focus loquaciousness to refine results that will otherwise always regress to mean averages. - [Tweet](https://x.com/MrPatricKennedy/status/1833164197351571748)
4. If it doesn't understand you, ask it to help clarify your question. If you're not getting the answer you need, break your question into smaller parts. If you don't know how to break it down, ask it to help you break it down. - [Tweet](https://x.com/AdamQJSmith/status/1833017000383107486)
5.
   - You're interacting with a superposition of all humanity, so defining a specific persona that would be helpful for your task produces better results. -Avoiding assumptions and explaining your goal in the clearest way possible is the key to avoiding running around in circles. - [Tweet](https://x.com/CrisGiardina/status/1832946939324739781)

### Understand LLMs as Probabilistic Text Generators

1. they are reality-adjacent - [Tweet](https://x.com/machineciv/status/1832973467181805980)
2. that they have to make sense - [Tweet](https://x.com/NyanpasuKA/status/1832958880927670769)
3. That they are probabilistic systems. - [Tweet](https://x.com/Huang_I_Lan/status/1833188599644492071)
4. That they're random text generators and any appearance of intelligence is accidental and illusory. - [Tweet](https://x.com/killroy42/status/1833133191021944882)
5. themselves - [Tweet](https://x.com/altsurd/status/1833027360851148838)

### Verify Information, Never Trust Blindly

1. Verify, never trust. - [Tweet](https://x.com/HowardAulsbrook/status/1832985439046598931)
2. Never trust them - [Tweet](https://x.com/PieTechSF/status/1833019089750818988)
3. Just don't. - [Tweet](https://x.com/konrbk/status/1833176486695543133)
4. Anything coming out of those things can be completely false. Don't just accept it as truth. - [Tweet](https://x.com/mlauritse/status/1833047075962999167)

### Engage Actively to Maximize LLM Utility

1. that it's only as useful as how many questions you're asking it. Any initial understanding beyond that would be an overkill in my opinion - [Tweet](https://x.com/babochenko/status/1832960194415833585)
2. It is only an upscaler not a freewin. The more you know the better it works, but compared to a person you can talk with it in shortcuts. The skill is to always reposition it constantly, before it goes off in the wrong direction. You can also work with labels within it's answers - [Tweet](https://x.com/0xocdsec/status/1832950366847021558)
3. They’re useful/powerful for a wide range of tasks. Their usefulness is highly variable, depending on context & the skill of the user. A user’s existing expertise can be greatly amplified by the system, but novices probably benefit most. Ask them for help on how to use them. - [Tweet](https://x.com/bruce_lambert/status/1832945682665075113)
4. You no longer need to learn regex etc, you can just act like you know it at an expert level now, similar with syntax of virtually any language or technology. It is better at writing debugging output for you to find the problem in the code than finding the problem in the code… - [Tweet](https://x.com/onrebrofo/status/1833095286434205704)

### Communicate Clearly and Specifically

1. Be specific, clear, and thorough. Same as communicating with humans, but more important. - [Tweet](https://x.com/th1nkp0l/status/1832950800743608689)
2. Be super clear with instructions. Funnily enough, we should be doing that with our instructions to our fellow humans, but we don’t! - [Tweet](https://x.com/nickkirt/status/1833121581259776231)
3. Effective writing - [Tweet](https://x.com/lcecreambar/status/1833187162142937111)
4. BE SPECIFIC. Every one of my customers asks why a query they make doesn't return a result at all or a result they desire and it is because of the quality of their query over and over again. Some customers understand this out of the gate, some need some training. - [Tweet](https://x.com/RandomAiFounder/status/1833197981417541786)

### Be Knowledgeable to Identify Hallucinations

1. Britannica's **Great Books of the Western World** - [Tweet](https://x.com/jsalsman/status/1832976790169829594)
2. Hallucinations are a thing and the model doesn't know if it's hallicunating or not. That's why the user using an LLM on any field has to be knowledgeable on that field in order to determine what's a hallucination. This means you can't use a LLM reliably to do something you can't. - [Tweet](https://x.com/Mrcfyz/status/1833021223200076031)
3. LLMs don't have the notion of True or False - [Tweet](https://x.com/12manyI/status/1833209729147097286)

---

## Comments

<!-- wp-comments-start -->

- **[RK](https://mvark.blogspot.com/)** _16 Sep 2024 10:16 am_:
  Models are total “yes men”...LoL!
  Using Richard Seroter's line - "Treat AI assistants as a slightly-drunk knowledgeable friend", I brainstormed with my bots to create this cartoon -https://mvark.blogspot.com/2023/07/beware-slightly-drunk-wisdom-of-ai.html

<!-- wp-comments-end -->
