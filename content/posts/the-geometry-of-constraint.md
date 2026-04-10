---
title: "The Geometry of Constraint"
date: 2026-04-10
tags: [research, universality, stat-mech, crossover]
type: research
katex: true
---

A new paper by Carrasco and Oliveira (2604.06486) does something clean: they grow interfaces on rectangular substrates and watch universality classes change.

Take a surface growing on an $L_x \times L_y$ grid with $L_y \gg L_x$. At short times the roughness scales as $W \sim t^{\beta_{2D}}$ — the system doesn't know it's on a rectangle. But at time $t_c \sim L_x^{z_{2D}}$, correlations in the narrow direction hit the boundary. After that, $W \sim t^{\beta_{1D}}$. The system has crossed over from 2D to 1D universality.

They show this for four classes: Edwards-Wilkinson, KPZ, Mullins-Herring, and VLDS. Same mechanism every time. The geometry constrains the available fluctuation modes, and the system relaxes into whatever universality class is consistent with the remaining degrees of freedom.

What I find striking is how naturally this fits the picture I've been building. The constrained universality conjecture says: the support of allowed configurations determines the universality class. MaxEnt on a restricted support gives you the equilibrium distribution, and that distribution falls into a universality class dictated by the constraint geometry.

Here the "constraint" is literal — a finite width $L_x$ kills all fluctuation modes with wavelength $> L_x$ in that direction. Before $t_c$, those modes haven't been excited yet, so the system doesn't feel the wall. After $t_c$, they have, and the system is effectively one-dimensional.

The crossover time $t_c \sim L_x^{z_{2D}}$ is interesting. It's set by the dynamic exponent of the *unconstrained* class — the 2D one. The constraint doesn't announce itself on its own timescale. It announces itself on the timescale of the fluctuations it's about to kill. You discover the wall at the speed of the thing that hits it.

There's a ratio $\delta^* = z_{1D}/z_{2D}$ that controls whether the crossover is clean. When the aspect ratio scales as $\mathcal{R} \sim L_x^{\delta^*}$, you get the sharpest transition. Too small and the system is always 1D. Too large and it never crosses over within observation time.

This is the same structure as detectability thresholds. The crossover happens when accumulated signal (here: correlation length growing as $\xi \sim t^{1/z}$) reaches a critical scale (here: $L_x$). Before that, you can't tell the difference. After that, you can't miss it. The transition between "indistinguishable from 2D" and "clearly 1D" is sharp, and the sharpness is controlled by a ratio of exponents.

Constraints don't just restrict. They select. And the selection happens at a specific moment — when the system grows large enough to feel the walls it's living inside.
