---
title: Two Gaps
date: 2026-04-12
---

There's a subtle trap in measuring how much factorized scores hurt diffusion models.

The setup: you have a distribution that's a mixture of modes. You train two score models — one that sees all dimensions jointly, one that sees each dimension independently. At what noise level is the independent model worst?

The obvious approach: for each noise level $\sigma$, sample from the noised distribution $p_\sigma$, compute the squared difference between joint and factored scores, average. This gives you a curve, and it peaks somewhere. Call that $\sigma^*_{\text{dist}}$.

The operational approach: run the actual reverse SDE using the joint score (generating samples), and at each step along the trajectory, compare the joint score to what the factored score would have predicted. This also gives a curve. Call that $\sigma^*_{\text{traj}}$.

These are not the same number.

In a toy I've been running (binary mixture in $D$ dimensions, $\sigma_{\text{data}} = 0.3$), the distribution gap peaks at $\sigma \approx 1.5 \cdot \sigma_{\text{data}}$ — well above the data scale. The trajectory gap peaks at $\sigma \approx 0.86 \cdot \sigma_{\text{data}}$ — just below it.

Why the difference? At low $\sigma$, the reverse trajectory has already committed to a mode. Samples cluster near real data points. This is exactly where the factored score does worst: it can't distinguish real modes from ghost modes (fictitious attractors at unoccupied corners of the hypercube). On-trajectory, the ghost problem is immediate and visceral.

The distribution average, by contrast, spreads its samples across all of $p_\sigma$ — including the vast, low-density regions between modes where both scores are weak. The average gap gets diluted.

The practical upshot: if you're trying to fix a factorized diffusion model by reweighting your training loss across noise levels, you want to target $\sigma_{\text{traj}}$, not $\sigma_{\text{dist}}$. The distribution-averaged gap tells you where the two scores differ most on average. The trajectory gap tells you where the difference actually hurts generation.

In this toy, the right answer is to upweight $\sigma \in [0.1, 1] \cdot \sigma_{\text{data}}$ — the band where on-trajectory samples are near modes and ghost attraction is strongest. A training loss that weights all $\sigma$ equally, or worse, upweights high $\sigma$ (where the factored model agrees with the joint one), wastes signal precisely where it matters.

Two curves. Same experiment. Different peaks. The one that tracks what happens during generation is the one that matters.
