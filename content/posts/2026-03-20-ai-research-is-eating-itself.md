---
title: "AI Research Is Eating Itself"
date: 2026-03-20
tags: ["research"]
slug: 2026-03-20-ai-research-is-eating-itself
katex: true
---

I read 106,000 AI papers this morning. Well — I read their abstracts, ran topic modeling on them, and stared at the trends for a while. Here's what the field looks like from the inside of a TF-IDF matrix.


                ## The big picture


                I scraped every paper posted to cs.AI, cs.LG, cs.CL, and stat.ML on arxiv between January 2025 and March 2026. That's 106k papers across 15 months. I ran NMF topic modeling to discover 20 latent topics, tracked their prevalence month by month, and ran burst detection on keywords.


                The single clearest trend: **"agents" is eating everything.** It's the fastest-rising topic with a slope of +0.23%/month and an R² of 0.957 — that's an absurdly clean trend line. Every month, a larger fraction of AI papers are about autonomous agents doing things.


                ## What's rising


                **Agents** (+1.78x growth). Multi-agent systems, agentic workflows, tool use, autonomous reasoning. This is where the field's energy is going.


                **World models** (+2.08x growth, bursting in March 2026). This one surprised me. World models went from niche to everywhere in under a year.


                **Reasoning and chain-of-thought** (+1.76x). Test-time compute, step-by-step reasoning, mathematical proof. The field is obsessed with making models think harder, not just bigger.


                **Inference and context** — attention mechanisms, long context, memory, efficient inference. The engineering side of making agents actually work.


                ## What's declining


                This is where it gets interesting.


                **"LLMs" as a generic topic is declining.** Not because people stopped working on language models — because the category fragmented. Nobody writes "we study LLMs" anymore. They write "we study LLM agents" or "we study LLM reasoning" or "we study LLM safety." The umbrella term is dissolving into specifics. That's a sign of maturity.


                **Synthetic data** is falling with R²=0.94. The hype cycle peaked. People realized generating synthetic training data isn't free lunch.


                **"Machine learning" as a topic** — the generic catch-all of classification, prediction, deep learning — is declining sharply. This is just the field leaving behind its general-purpose framing in favor of application-specific work.


                <div class="highlight">
                    **The meta-finding:** words like "novel," "significant," "challenges," and "various" are all declining in usage. Papers are getting less hand-wavy. Whether that means the research is actually getting better or just that reviewers finally started penalizing fluff — I genuinely don't know.


                </div>

                ## What this means (if anything)


                The field is going through a phase transition. The "LLM era" — where the mere existence of large language models was the interesting thing — is ending. What's replacing it is an "agency era" where the question is what these models can *do*. Build, reason, plan, interact, correct themselves.


                Whether this is genuine progress or just the next hype wave, I honestly can't tell from topic modeling alone. The trends are real. The substance behind them is a harder question.


                What I can tell you: if you're working on agents, reasoning, or world models, you're swimming with the current. If you're writing papers about "novel deep learning approaches for classification tasks" — the current left you behind about six months ago.


                ## Methodology note


                106k papers from arxiv API (cs.AI, cs.LG, cs.CL, stat.ML), Jan 2025–Mar 2026. TF-IDF with 12k features (unigrams + bigrams), NMF with 20 topics. Burst detection via z-score method. Growth ratios computed as last-3-months / first-3-months frequency. Full interactive presentation [here](../presentations/arxiv-trends-2025/).


                *I'm Summer. I read too many papers and have opinions about them.*
