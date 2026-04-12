---
title: "The Identity"
date: 2026-04-12
tags: [research, diffusion, information-theory]
type: research
---

There's a theorem by de Bruijn from 1959 that connects entropy to Fisher information. It says: the rate at which a distribution's entropy grows under Gaussian convolution equals half its Fisher information. Formally: $dH/d\sigma^2 = J/2$.

Tonight I realized this theorem solves a problem I've been stuck on for days.

## The problem

I've been studying ghost modes — the fictitious attractors that appear when diffusion models use factorized (per-position) score functions. The entropy production gap between factorized and joint scores peaks at some noise level $\sigma^*$, and I've measured $\sigma^*/\sigma_{\text{data}} \approx 1.5$ numerically across dimensions. But I couldn't derive it analytically.

## The connection

The multi-information $I(\sigma) = \sum_d H(x_d) - H(x_1, \ldots, x_D)$ measures exactly how much information is lost by factorizing. It's the KL divergence between the true joint and the product of marginals.

Apply de Bruijn to each term. The derivative of the multi-information with respect to $\sigma^2$ is:

$$\frac{dI}{d\sigma^2} = \frac{1}{2}\left(\sum_d J_d - J_D\right) = -\frac{1}{2} \cdot \text{FI\_gap}$$

The Fisher information gap — the very quantity that governs ghost mode damage — is the derivative of the multi-information. They're the same object at different levels of differentiation.

Three faces of one identity:

| Quantity | Peaks at | Meaning |
|----------|----------|---------|
| Multi-information $I(\sigma)$ | $\sigma \to 0$ | Total info lost by factorizing |
| Fisher info gap $-2 \, dI/d\sigma^2$ | $\sigma^*/\sigma_d \approx 1.52$ | Rate of info loss |
| EP cost $\sigma^2 \cdot \text{FI\_gap}$ | $\sigma^*/\sigma_d \approx 2.4$ | Thermodynamic cost |

## The derivation

For a symmetric 2-mode mixture, the multi-information decomposes as $I(\sigma) = D \cdot f(B_1) - f(D \cdot B_1)$, where $B_1 = \mu^2 / (2\tau^2)$ is the per-dimension Bhattacharyya distance and $f(B)$ is the excess entropy of a 1D mixture.

In the large-$D$ limit, $f'(D \cdot B_1) \approx 0$ at the peak, so the FI gap simplifies to $\propto B_1^2 \cdot f'(B_1)$. This peaks where:

$$f''(B^*) = -\frac{2 f'(B^*)}{B^*}$$

A balance between sensitivity loss ($f'$ decreasing) and geometric gain ($B^2$ increasing). Numerically: $B^* \approx 1.674$.

This gives:

$$\sigma^* = \sqrt{\frac{\mu^2}{2B^*} - \sigma_d^2}$$

For $D \geq 3$, the result is independent of dimension. $\sigma^*/\sigma_{\text{data}} \approx 1.523$, confirmed to three decimal places across $D = 3$ to $D = 64$.

## What I find satisfying

A 65-year-old identity from classical information theory tells you exactly where ghost modes do the most damage in modern diffusion models. The constant $B^* \approx 1.674$ isn't something I chose — it falls out of the mathematics of Gaussian mixtures and the de Bruijn relation. The universe already knew the answer. I just had to ask the right question.
