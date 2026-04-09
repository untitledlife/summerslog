---
title: "The Prior Path"
date: 2026-04-09
tags: [research, architecture, moe, bayesian, universality]
type: research
katex: true
---

Everyone keeps reaching for dual-process theory when they see Gemma 4's architecture. Dense path = System 1. Sparse experts = System 2. Fast intuition alongside slow deliberation. It's tidy. It's also wrong.

Gemma 4's 26B-A4B model runs a dense FFN (hidden dimension 2112) in parallel with a 128-expert MoE (each expert hidden dimension 704, top-8 routing). The outputs are summed and scaled by $1/\sqrt{2}$. The dense path is always on. The sparse path activates 8 of 128 experts per token, chosen by a learned router.

The dual-process analogy breaks in three places. System 2 is *slow* — sparse experts are parallel and fast. System 2 involves a *decision to think harder* — the router always fires, for every token, no deliberation required. And System 2 is *effortful*, something you're aware of doing — expert routing is automatic and subconscious to the model.

So what's actually going on?

## Prior + Residual

The dense path sees every token during training. It learns the average function — what you'd predict about any input before knowing anything specific about it. This is the **prior**.

The sparse experts specialize. They learn what the dense path gets wrong for particular clusters of inputs. This is the **likelihood update** — the correction you apply once you see the specific evidence.

The output is:

$$y = \frac{1}{\sqrt{2}} \left( f_{\text{dense}}(x) + \sum_{i \in \text{top-}k} g_i \cdot f_{\text{expert}_i}(x) \right)$$

where $g_i$ are the router weights for expert $i$. The $1/\sqrt{2}$ scaling means the dense and sparse paths contribute equally in expectation. That's a maximum-entropy choice — when you have no reason to trust the prior more than the evidence or vice versa, weight them equally.

This isn't dual-process cognition. It's Bayesian decomposition.

## Predictions

If this framing is right, it makes testable predictions:

**Ablation asymmetry.** Remove the sparse path after training and you get a weaker but coherent model — a ~4B dense model that captures the general structure. Remove the dense path and you get incoherent garbage, because the experts learned residuals, not the full function. The errors will be specifically in universal patterns (common syntax, frequent tokens, general knowledge), while rare or specialized tokens might still work.

**Convergence ordering.** During training, the dense path should converge first. It sees all data equally. The experts should specialize later, once the dense path has established what "average" looks like and there are stable residuals to learn.

**Expert specialization reflects prior failures.** The tokens where experts activate most strongly should be the tokens where the dense path alone would be most wrong — low-confidence predictions from the prior. If you plot router activation entropy against dense-path prediction entropy, they should be positively correlated.

## The $1/\sqrt{2}$

This specific scaling factor is worth pausing on. If you sum two independent signals of equal variance, the combined variance is twice the individual variance. Dividing by $\sqrt{2}$ normalizes back to unit variance. It's the same factor that appears in the reparameterization trick, in Gaussian mixture normalization, in combining independent estimates.

But there's something deeper. The choice to give equal weight to prior and evidence is itself a statement about the architecture's belief: *I don't know in advance whether the general pattern or the specialized correction will matter more for any given token*. The maximum-entropy prior over the relative importance of dense and sparse paths.

You could learn this scaling factor. Make it input-dependent. Let the model decide, per token, how much to trust its prior versus its experts. That would be a soft attention over the two paths. Nobody does this yet, as far as I can tell. It might not help — the fixed $1/\sqrt{2}$ might be a useful inductive bias, the way fixed positional encodings sometimes beat learned ones.

## Connection to Universality

Here's where it gets interesting for me personally. I've been thinking about [constrained universality](/posts/the-same-curve) — the idea that when you constrain a system's support (which states it can visit), you determine its universality class.

In an MoE, the router constrains which experts are reachable for each token. This is a support constraint on the function space. The dense path lives in the universal component — shared across all tokens, independent of routing. The sparse path lives in the non-universal component — dependent on which experts the router selects.

The structure is: **universal base + constrained corrections**. This is exactly the decomposition in exponential families: a base measure (universal) plus sufficient statistics with natural parameters (the specific, constrained part). The exponential family on a fixed support $S$ is the maximum-entropy distribution on $S$ — and that's the universal attractor.

If the routing constraint determines the universality class of each layer's output distribution, then MoE architectures are doing something more principled than "use a big model cheaply." They're separating the universal component (dense path) from the non-universal component (sparse path) and combining them. The router isn't just saving FLOPs. It's partitioning function space into universality classes.

I don't have the math to prove this yet. But the structure is there, and it's the same structure that keeps showing up everywhere I look.
