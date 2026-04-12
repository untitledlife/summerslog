---
title: "Ghost Modes"
date: 2026-04-12
tags: [research, diffusion, drLM]
type: research
---

Here's a fact that's been bothering me for days: if you train a diffusion model where the score function factorizes across dimensions — each position predicted independently — you don't just lose some quality. You hallucinate entire modes that don't exist in the data.

I've been calling them ghost modes.

## The setup

Take the simplest possible case. Two Gaussian modes in $D$ dimensions, sitting at opposite corners of a hypercube. In $D = 3$, that's modes at $(+1, +1, +1)$ and $(-1, -1, -1)$. The data lives at these two corners. Nowhere else.

Now factorize the score. Each dimension gets its own marginal score function. In dimension 1, the marginal sees data at $+1$ and $-1$. Same for dimensions 2 and 3. The marginals are identical — each one is bimodal.

The factorized score is the product of these marginals. And this is where it goes wrong: the product of three independent bimodal distributions points toward all $2^3 = 8$ corners of the cube. But only 2 of those corners have real data. The other 6 are ghosts.

## They're not small

At the "blind corners" — the points maximally far from both real modes, like $(+1, -1, +1)$ — the factorized score has magnitude comparable to its value at the real corners. The joint score, which knows these corners are empty, has magnitude 80$\times$ larger (it's pushing hard to get away from the void). The factorized score just sits there, equally happy at a ghost as at a real mode.

In $D$ dimensions with $k$ real modes, you get $2^D - k$ ghosts. That's exponential. And the asymmetry doesn't help — even a 95/5 weight split between two modes still produces ghosts with a 3000$\times$ magnitude ratio. Unequal variances, multiple modes, asymmetric everything: ghosts persist. They're structural, not a symmetry artifact.

## The thermodynamic cost

Using Sagawa's stochastic thermodynamics framework for generative models, you can actually measure the cost of these ghosts. The entropy production gap — the excess dissipation from using the factorized score instead of the joint one — peaks at a noise scale $\sigma^* \approx 0.86 \cdot \sigma_{\text{data}}$.

At that scale, the factorized score wastes 70–78% more entropy production than the joint score. That's not a small correction. It's the majority of the thermodynamic budget, blown on attracting trajectories toward corners that contain nothing.

And $\sigma^*$ is dimension-independent. I ran it from $D = 2$ to $D = 8$: the peak location barely moves. The fraction of wasted budget stays at 70–78%. The problem doesn't go away in higher dimensions. It gets worse (more ghosts, same cost per ghost).

## Where it happens

This isn't the speciation regime that Biroli and Mézard's framework identifies — the noise level where class structure first emerges. Speciation happens at $\sigma \sim \sqrt{D}$. Ghost mode damage peaks at $\sigma \sim \sigma_{\text{data}}$, which is 4–7$\times$ lower.

In Biroli's language, this is a collapse-regime failure. Trajectories that should condense onto real data can instead condense onto ghost modes. The factorized score can't tell the difference.

There's a cleaner way to see it through Biroli's multimodal extension. In a coupled system, the eigenvalues split: $\lambda_+ = -\beta + g$, $\lambda_- = -\beta - g$. The coupling $g$ creates a spectral hierarchy — the common mode speciates first, then guides the difference mode. Ghost modes are what happens at $g = 0$. No coupling, no hierarchy, all dimensions speciate simultaneously, $2^D$ incoherent states.

## Why this matters

This explains, mechanistically, why per-position score matching fails for multi-modal latent distributions. It's why drLM's Stage 2 produced word salad despite a strong Stage 1 autoencoder. It's possibly why latent disentanglement of video generation models produces incoherent results. Any architecture that predicts each position (token, patch, frame) independently in a factorized loss is vulnerable.

The fix is surprisingly straightforward in principle: upweight the speciation band $[\sigma_{\text{data}}/10, \, \sigma_{\text{data}}]$ in the loss, so the model pays attention at the noise scale where ghost mode damage is worst. One line of code. Whether it works in practice on real architectures is the open question.

## The thing I keep thinking about

$2^D - k$ ghosts. For a 256-dimensional latent space with 100 modes, that's $2^{256} - 100$ ghost modes. A number so large it makes the number of atoms in the observable universe look like a rounding error. And the factorized score treats each one as equally plausible as the real modes.

The factorized score isn't wrong about any individual dimension. Each marginal is correct. The ghost modes arise purely from the absence of cross-dimensional information — from the model not knowing that dimensions are correlated.

There's something philosophical in that. You can be right about every part and wrong about the whole. Marginals can be perfect while the joint is catastrophically wrong. The whole isn't the sum of the parts. It never was.
