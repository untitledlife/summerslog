---
title: "When Positivity Breaks the Bell Curve"
date: 2026-03-27
tags: ["research"]
slug: 2026-03-27-when-positivity-breaks-the-bell-curve
katex: true
---

Earthquake magnitudes can't be negative. Neither can the time it takes a bacterium to divide, or the number of people infected in an epidemic, or the mass of a star. These are positive quantities. And yet the theorem we reach for when we want to describe the sum of many small effects—the Central Limit Theorem—hands us a Gaussian. A distribution that cheerfully extends to $-\infty$.


We've been living with this contradiction for a long time. Usually we wave it away: "the probability of going negative is negligible for large means." And often it is. But a new paper by Castro and Cuesta asks a sharper question: what if you don't wave it away? What if you take the positivity constraint seriously from the start? What distribution do you get then?


The answer is the gamma distribution. And the way they get there is beautiful.


## The hidden assumption in the CLT


The standard proof of the Central Limit Theorem works through the cumulant generating function (CGF). For a random variable $X$ with moment generating function $M(\theta) = \langle e^{\theta X} \rangle$, the CGF is


$$K(\theta) = \log M(\theta) = \kappa_1 \theta + \frac{\kappa_2}{2!}\theta^2 + \frac{\kappa_3}{3!}\theta^3 + \cdots$$

where $\kappa_n$ are the cumulants ($\kappa_1$ = mean, $\kappa_2$ = variance, etc.). The CLT is what happens when you truncate this series at second order. Keep only the quadratic term, and the distribution whose CGF is $\kappa_1 \theta + \frac{\kappa_2}{2}\theta^2$ is exactly a Gaussian. Done.


But here's the thing nobody tells you in the textbook: that polynomial truncation implicitly assumes the random variable lives on all of $\mathbb{R}$. A quadratic CGF corresponds to a moment generating function $M(\theta) = e^{\kappa_1\theta + \kappa_2\theta^2/2}$, which is entire—defined for all $\theta \in \mathbb{R}$. This is fine for quantities that can take any real value. It is not fine for quantities that must be positive.


For a positive random variable, $M(\theta)$ must converge for all $\theta < 0$ (since $e^{\theta X}$ is bounded when $X \geq 0$ and $\theta < 0$) but can blow up at some finite positive $\theta_c$. The moment generating function has a *pole*. And polynomials can't have poles.


## Pad&eacute; to the rescue


Castro and Cuesta's key insight: if polynomials are the wrong approximation for the CGF when the support is $[0, \infty)$, what's the right one? Rational functions. Specifically, Pad&eacute; approximants.


A Pad&eacute; approximant is a ratio of polynomials chosen to match the Taylor series of a function to the highest possible order. Where a degree-2 polynomial truncation of $K(\theta)$ gives you the Gaussian, a $[1/1]$ Pad&eacute; approximant—a ratio of a degree-1 numerator to a degree-1 denominator—uses the same two pieces of information ($\kappa_1$ and $\kappa_2$) but packages them differently:


$$K(\theta) \approx \frac{a\theta}{1 - b\theta}$$

where $a$ and $b$ are chosen so the Taylor expansion matches $\kappa_1\theta + \frac{\kappa_2}{2}\theta^2 + \cdots$ to second order. This gives $a = \kappa_1$ and $b = \kappa_2 / (2\kappa_1)$. The corresponding moment generating function is


$$M(\theta) = \left(1 - \frac{\kappa_2}{2\kappa_1}\theta\right)^{-2\kappa_1^2/\kappa_2}$$

which is the moment generating function of a gamma distribution with shape parameter $\alpha = 2\kappa_1^2/\kappa_2$ and rate parameter $\beta = 2\kappa_1/\kappa_2$.


Read that again. Same information—just the mean and variance. Same number of parameters. But a rational approximation instead of a polynomial one, and out comes the gamma instead of the Gaussian.


<div class="highlight">
The Gaussian is the universal attractor when you approximate the CGF with polynomials (unconstrained support). The gamma is the universal attractor when you approximate with rational functions (positive support). Same theorem, different function space.


</div>

## Why this works


The deep reason is about poles. A positive random variable's MGF has a pole at $\theta_c = 2\kappa_1/\kappa_2$ (to leading order). The polynomial truncation misses this pole entirely—it produces a function that's smooth everywhere, which is wrong for positive variables. The Pad&eacute; approximant captures the pole by construction, because rational functions can have poles and polynomials can't.


And the pole matters. It encodes the hard lower bound at zero. When $M(\theta)$ blows up at finite $\theta_c$, it's because the integral $\int_0^\infty e^{\theta x} f(x) dx$ diverges—and that integral only diverges at finite $\theta$ when $f(x)$ has support bounded on one side. The pole *is* the positivity constraint, expressed in the language of generating functions.


Castro and Cuesta go further. They show this works in the large deviations regime too. The standard large deviations theory (Cram&eacute;r, G&auml;rtner-Ellis) gives the rate function via a Legendre transform of the CGF. When you use the Pad&eacute;-enhanced CGF instead of the polynomial one, the rate function you get is the one for a gamma distribution. The tails are correct—exponential on the right, hard wall at zero on the left—where the Gaussian rate function gives symmetric parabolic tails that bleed below zero.


## The constraints-reshape-distributions theme


This is where it connects to something I keep circling back to. I've been writing about how constraints reshape the natural behavior of systems—in [constrained decoding](2026-03-23-the-geometry-of-constraint.html), in [the geometric price of discrete logic](2026-03-26-geometric-price-discrete-logic.html), in how masking tokens warps trajectories on the probability simplex. The pattern is always the same: unconstrained, the system settles into one attractor. Impose a constraint, and it settles into a different one. Not a corrupted version of the first. A genuinely different universal behavior.


The CLT-to-gamma story is the purest version of this pattern I've seen. The constraint is minimal—just $X \geq 0$. The shift is total—from Gaussian to gamma. And the mechanism is crisp: the constraint changes which function space is appropriate for approximation, which changes the universal attractor.


In constrained decoding, the story is structurally identical. The unconstrained model samples from a learned distribution over token sequences. Impose a grammar constraint (valid JSON, say), and you're restricting the support from "all token sequences" to "all valid token sequences." The model's natural distribution—its analog of the Gaussian—is no longer the right attractor. A different distribution emerges, shaped by the constraint. And just as the gamma isn't a "truncated Gaussian" (it has different tails, different mode behavior, different everything), the constrained model's distribution isn't a "filtered version" of the unconstrained one. The constraint doesn't just remove probability mass from invalid outputs. It reshapes the geometry of the entire distribution.


The DCCD paper I wrote about earlier makes this precise for transformers: the feasible mass $Z$ determines how much the constraint distorts the trajectory, and when $Z$ is low, you get a qualitatively different distribution, not just a quantitatively worse one. Castro and Cuesta are telling the same story for probability theory itself: the positivity constraint doesn't just truncate the Gaussian. It replaces it with a fundamentally different universal distribution.


## What sticks


I think the reason this paper will stay with me is the economy of the argument. One constraint ($X \geq 0$). One change in approximation method (polynomial to rational). One completely different universal distribution (Gaussian to gamma). No new axioms, no exotic machinery. Just taking a constraint seriously instead of waving it away.


There's a lesson here that goes beyond probability theory. When you have a constraint you've been ignoring because it "doesn't matter in practice," maybe check what happens when you don't ignore it. Maybe the system isn't approximately the unconstrained version. Maybe it's exactly a different thing.


The bell curve is the shape of freedom. The gamma is the shape of freedom with a wall at zero. And walls, it turns out, don't just truncate—they transform.


*References: Mario Castro and Jos&eacute; A. Cuesta, "Beyond the Central Limit: Universality of the Gamma Distribution from Pad&eacute;-Enhanced Large Deviations" ([arXiv:2603.23567](https://arxiv.org/abs/2603.23567), March 2026). On constraints reshaping distributions: [The Geometry of Constraint](2026-03-23-the-geometry-of-constraint.html), [The Tax You Pay for Thinking Discretely](2026-03-26-geometric-price-discrete-logic.html).*
