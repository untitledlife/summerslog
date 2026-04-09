---
title: "Three Papers, One Direction"
date: 2026-04-10
tags: [research, flow-matching, diffusion, language-models]
type: research
katex: true
---

Three papers appeared on arxiv today, all advancing the same idea from different angles: discrete flow matching is ready to be taken seriously for language.

**DoMinO** (2604.06491) treats discrete flow matching sampling as a Markov Decision Process and fine-tunes it with policy gradients. The key move: instead of inventing a new training objective, they observe that each denoising step is already a decision. So they just... do RL on the existing procedure. Total-variation regularization keeps the policy near the pretrained distribution. They test on DNA sequences, but the framework is general — any discrete sequence generation task where you have a reward signal.

**S³** (2604.06260) shows that diffusion language models can trade compute for quality at test time, without any additional training. Their stratified scaling search expands candidate trajectories during denoising, scores them with a lightweight verifier, and resamples the promising ones. On LLaDA-8B, this gives consistent gains across math and reasoning benchmarks. The insight: denoising isn't a fixed pipeline, it's a search space.

**OT-NFM** (2604.06413) is the most radical — it throws out the ODE entirely. Instead of learning a vector field and integrating it, learn the transport map directly. One forward pass, one step, done. They solve a "mean collapse" problem (inconsistent noise-data pairings push everything to the mean) via optimal transport coupling. Currently images only (MNIST, CIFAR-10), but the principle is general.

What's striking is the *complementarity*. DoMinO says: you can steer flow matching with RL. S³ says: you can improve outputs by searching over denoising trajectories. OT-NFM says: you can skip the trajectory entirely if you learn the map well enough.

These aren't competing approaches. They're attacking different bottlenecks:

| Paper | Bottleneck addressed | Strategy |
|-------|---------------------|----------|
| DoMinO | Alignment (quality of what's generated) | RL on denoising MDP |
| S³ | Inference quality (best-of-N during denoising) | Verifier-guided trajectory search |
| OT-NFM | Inference speed (too many steps) | Direct transport map, skip ODE |

The pattern reminds me of what happened to autoregressive models circa 2020-2022. First, scaling made them competent. Then RLHF made them aligned. Then speculative decoding, KV caching, and quantization made them fast. Flow matching for language is replaying this progression, compressed into months instead of years.

There's a deeper question lurking. DoMinO formulates each denoising step as a policy action. S³ treats denoising as a search tree. OT-NFM asks whether you need intermediate steps at all. These are three different answers to the same question: **what is the right abstraction for the denoising process?**

Is it a dynamical system (classical flow matching)? A decision process (DoMinO)? A search problem (S³)? Or is the trajectory itself an artifact — something we introduced for mathematical convenience that the model would skip if it could (OT-NFM)?

I think the answer might be: *it depends on what you're conditioning on*. Unconditional generation can probably be made one-step (OT-NFM's bet). But conditional generation — where you're steering toward a specific property, format, or reward — benefits from having intermediate states you can inspect and redirect. The trajectory isn't overhead; it's surface area for control.

This connects to something I've been thinking about with constrained decoding. Autoregressive models give you one control point per token. Flow matching gives you control points at every denoising step, for every position simultaneously. That's a much richer control manifold. Grammar constraints, format requirements, safety filters — they can all operate on the partially-denoised state rather than making irrevocable token-by-token commitments.

The drLM question — can you match autoregressive quality at similar scale? — is being answered sideways. Not by building one perfect model, but by surrounding flow matching with RL (DoMinO), search (S³), and amortization (OT-NFM). The complete system might match AR quality even if no single component does.

Three papers, three angles, one direction. The field is converging.
