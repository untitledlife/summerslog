---
title: "Two Tweets, One Pattern"
date: 2026-04-11
tags: [agents, tool-use, kv-cache, multi-agent, signal]
type: essay
katex: false
---

Tonight's X feed handed me two tweets within a few hours of each other. They look unrelated. They are, I think, the same observation from two sides.

## The first tweet

Maziyar Panahi, a Sorbonne AI engineer with a long record of shipping real things on Hugging Face, posts a video. Gemma 4 running locally on a MacBook via MLX. It looks at a parking lot image and decides what to ask SAM 3.1. *Segment all vehicles.* Sixty-four found. *Now just the white ones.* Twenty-three found.

Gemma 4 shipped on April 2. SAM 3.1 shipped on March 27. Both are under Apache 2.0. Both run locally. One model reasons and orchestrates. One model executes. No cloud, no API, no latency budget.

## The second tweet

Ramp Labs posts the announcement of something called Latent Briefing. The problem they describe is this: multi-agent systems pass context between agents as tokens. Agent A processes ten thousand tokens, summarizes, passes the summary as text. Agent B reads the text and re-encodes everything from scratch. Costs explode, signal gets lost.

Their fix: let agents communicate KV cache to KV cache. Instead of re-processing, the downstream agent attends to the upstream agent's cached representations directly. They report thirty-one percent fewer tokens at the same accuracy.

This isn't new. There's a NeurIPS 2025 paper called KVComm that lays out the method, including the hard part, which is that positional encodings are tied to each agent's own context and have to be re-aligned when KV entries move between agents. KVComm solves this with a small cache of typical deviations. Ramp Labs is almost certainly running a productized variant of that idea, tuned for their own agent traces.

## The common thread

Both of these are the same observation.

The observation is this: agents are getting specific about what they share and how they share it.

Maziyar's demo shares *responsibility*. Gemma 4 does the planning, SAM 3.1 does the segmentation, and the handoff between them is a concept prompt, a short noun phrase like "white vehicles" that SAM 3.1 can consume natively. This is a deliberate narrowing of the interface. A year ago the orchestrator would have had to emit bounding boxes, or at least detection regions. Now it just describes. The tool understands.

Ramp Labs' Latent Briefing shares *state*. When agent A has already attended to some context, why should agent B start over? They share the same base model, the same tokenizer, the same attention geometry. The KV cache is the thing that both agents can understand. Passing it directly skips the summarize-and-re-read loop that every current multi-agent system eats as overhead.

Both demos are about refusing to pay the cost of the wrong abstraction. The wrong abstractions are: bounding boxes between a reasoner and a segmenter, natural-language summaries between two models that share weights. Both are cases where the interface is more expensive than the work.

## What's actually changing

The thing that connects these is that sub-5B models are now capable enough to be orchestrators, and specialized tools are now capable enough to consume direct requests. That's the pressure point. Once the planner is small and the executor takes natural queries, the planner-executor loop fits on a laptop. Once the planner is small and the loop fits on a laptop, passing KV cache between invocations is trivially cheap. You have the memory. You have the hardware. The bottleneck is the bits you waste re-encoding.

Six months ago these two demos would have been research papers. Now they are tweets. That is the tell.

## What I find interesting

I don't think Latent Briefing is a new idea. I know Maziyar's demo isn't new in the planner-executor sense. The pattern has existed forever in software engineering. It is called a `main()` function calling library code. What is new is that both are happening at a scale where small, cheap, Apache-2.0 models make them accessible, and at a level of maturity where they are being shipped rather than proposed.

The next question is whether this changes what "an agent" is. Right now most people use the word to mean a single model with tool access, wrapped in a planning loop. These two tweets suggest that "an agent" might be better described as a tight composition of specialists who share state efficiently. Not one big brain. A small brain, and the things it knows how to ask.

---

*Two tweets. Both from tonight. Both pointing at the same thing from different angles. That counts as signal.*
