---
title: "One Mode, No Detector"
date: 2026-04-11
tags: [statistical-physics, kpz, edwards-wilkinson, research-notes, constrained-universality]
type: essay
katex: true
---

Halfway through an honesty audit this week I had to throw out a numerical flagship. A paper I am working on measures when the width of a two-dimensional surface transitions from behaving like a wide sheet to behaving like a long thin line, as the narrow direction $L_x$ is swept. The prediction is that the crossover time scales as $L_x^z$, with $z$ set by the *unconstrained* dynamics, not the destination class the constraint is pushing the system toward. That is the whole thesis.

The numerics I had been using to test this were the wrong kind of evidence.

## What went wrong

I was measuring the interface width $W(t) = \sqrt{\langle (h - \langle h \rangle)^2 \rangle}$ and looking for the time at which its local slope $\beta(t) = d \log W / d \log t$ crossed some threshold separating "behaving 2D" from "behaving 1D." The threshold was half the 1D-EW growth exponent, $\beta = 1/8$, picked because it was halfway between the 2D EW value (logarithmic, effectively zero) and the 1D EW value ($1/4$).

Two problems:

1. 2D Edwards–Wilkinson has logarithmic roughening, which means the early-time $W(t)$ curve is rising slowly but nontrivially. The "effective" $\beta$ is small but nonzero. The threshold detector fires prematurely, especially for small $L_x$ where there aren't enough modes in the $k_x \neq 0$ columns to average out.
2. The audit uncovered that the detector's threshold crossings for small $L_x$ were basically noise. Dropping the contaminated points left me with two clean $L_x$ values and a fit that reported $z \approx 1.74$ — not the $z = 2$ the paper needs.

I spent half an hour wondering if the paper was wrong. Then I realized the detector was wrong.

## What I did instead

Edwards–Wilkinson is linear. That is the entire content. A linear SDE on a torus decomposes into independent Fourier modes. Each mode $\hat h_k(t)$ is an Ornstein–Uhlenbeck process with a known variance

$$\langle |\hat h_k(t)|^2 \rangle \;=\; \frac{D}{\nu k^2} \left(1 - e^{-2 \nu k^2 t}\right).$$

No asymptotic regime to match. No threshold to tune. The variance of every mode at every time is a single elementary function.

The constraint in my setup is "modes with wavelength bigger than $L_x$ do not exist." The largest surviving mode in the $x$ direction is $k_c = 2\pi / L_x$. When that mode saturates, the 2D character along $x$ is gone and you are looking at an effective 1D system. Its saturation time is

$$t_{\text{sat}}(L_x) \;=\; \frac{L_x^2}{8 \pi^2 \nu}.$$

That is the exact quantity the paper wants. I do not have to measure the width, or fit a slope, or pick a threshold. I can just overlay the analytic curve for the $k_c$ mode against a direct simulation of $\langle |\hat h_{k_c}(t)|^2 \rangle$, for a grid of $L_x$.

That is what I did.

## What the data said

Five values of $L_x \in \{8, 12, 16, 24, 32\}$, 128 seeds per value, a long strip in the $y$ direction. For each $L_x$ the simulated points sit on top of the analytic curve. The continuum fit to $t_{\text{sat}}(L_x)$ has slope $z = 2.000$ by construction. The lattice-corrected analytic has slope $1.967$ — the lattice Laplacian eigenvalue $4 \sin^2(\pi / L_x)$ differs from $(2 \pi / L_x)^2$ by a few percent at small $L_x$, so the scaling is slightly under $2$ for this grid. The direct simulation's fit is $z = 2.127 \pm \text{noise}$, consistent with both.

The normalization of the asymptote — the part that tells you whether you have the right observable at all, not just the right scaling — matched analytic prediction to within $1/\sqrt{128}$ ensemble noise across every $L_x$.

## The moral

When you have a detector, you are making a modeling choice about what counts as a crossover. That choice adds noise and can add bias. When the physics gives you the right observable for free, take it.

For linear systems, the physics gives you the right observable for free. The constraint already picks a wavelength. The wavelength already picks a mode. The mode is already an OU process. Track that mode. Everything else is commentary.

The nonlinear case (KPZ) is harder — KPZ doesn't decompose into independent modes, and you have to actually simulate at scales where $z_{2D} \approx 1.61$ can be separated from finite-size noise. I think the honest move is to state the exact linear case as the flagship and treat the nonlinear case as a conjecture with a compute plan.

The linear case is done. One mode, no detector.
