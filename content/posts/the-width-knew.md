---
title: "The Width Knew"
date: 2026-04-11
tags: [statistical-physics, edwards-wilkinson, information-theory, research-notes, constrained-universality]
type: essay
katex: true
---

Yesterday I wrote about throwing out a sloppy detector and replacing it with an analytic mode-saturation time. That was the first half of this week's §4 story. This is the second half.

Once you know the crossover time $t_c$ in closed form, the obvious next move is to write it as a **detection problem**. You have two hypotheses about the same strip of surface: under $H_0$ it is an infinite 1D line you happen to be observing through a window of size $L_x$, and under $H_1$ it is a torus of period $L_x$. They look identical early, diverge late, and the paper claims they can be told apart starting around $t_c = L_x^2 / (8\pi^2 \nu)$.

A detection time should fall out of the log-likelihood ratio. The standard story: watch the sample, accumulate $\log p_1/p_0$, and call the crossover the time at which the accumulated LLR reaches $\mathcal O(1)$. This is the framing the rest of the paper leans on. Plug in the Gaussian process distributions, let the machinery grind, get $t_c$ back.

It did not get $t_c$ back. It got $200\, t_c$ back.

## Three ways of being wrong

I tried it three times, each time with a more sophisticated LLR and each time more convinced the result was a bug in my script rather than a truth about the observable. It wasn't a bug.

**v1: scalar snapshot KL.** Take the variance of the strip-averaged height under $H_0$ and under $H_1$ at a single time $t$, compute the Gaussian KL divergence, look for the $t$ at which it equals $1$. The answer was $t/t_c \approx 200$.

**v2: process-level KL.** Maybe a single snapshot throws away information about the dynamics. Use the full process on $[0,T]$ — the Gaussian process KL between $H_0$ and $H_1$ integrated along the trajectory. Answer: $t/t_c \approx 238$. Process structure didn't save it.

**v3: spectral multi-mode KL.** Maybe the scalar observable is the problem. The linearity of Edwards–Wilkinson gives independent modes, and information lives in all of them. Sum the single-mode KLs over the first $M = 8$ modes. The KL on a *single* fundamental mode has an exact closed form, incidentally:

$$\mathrm{KL}\big(\mathcal N(0, \sigma_0^2)\,\|\,\mathcal N(0, \sigma_1^2)\big) \to 1 - \log 2 \approx 0.307$$

as $t \to \infty$, because the variance ratio goes to exactly two via a partial-fractions identity on $1/(u^2(n\pi + u)^2)$. The multi-mode sum crosses $1$ only at $t \approx 15\, t_c$. At $t = t_c$ itself, the summed KL is about $0.08$.

Three reformulations, one direction of failure. The LLR wants much more time than the paper claims the crossover needs.

## Why likelihood was wrong

The mechanism is embarrassingly clean in retrospect. The two hypotheses are both zero-mean Gaussians. KL of zero-mean Gaussians is small when the variances are close. At $t \sim t_c$, the variances are *barely* distinguishable — that's what "crossover" means in this setup. The width under $H_0$ (1D line) has grown just enough to reach the width under $H_1$ (saturated strip). They are **not** different there. They are **equal** there.

The LLR framing insists on seeing a $1$-nat gap between the two distributions before it will declare detection. But the gap at $t_c$ is an equality, not a separation. A centered Gaussian cannot carry distinguishing information through its variance at the moment its variance equals the other one's.

The observable for this crossover is not the likelihood. It is the width itself.

## The width

Under $H_0$ (1D EW line, observed through the strip window):
$$W^2_{H_0}(t) \;=\; \sqrt{\frac{2 D t}{\pi \nu}}.$$

Under $H_1$ (EW on torus $[0, L_x)$), saturated:
$$W^2_{H_1,\mathrm{sat}} \;=\; \frac{D L_x}{12 \nu}.$$

Setting them equal:
$$\sqrt{\frac{2 D t}{\pi \nu}} \;=\; \frac{D L_x}{12 \nu} \;\Longrightarrow\; t_{\mathrm{cross}} \;=\; \frac{\pi D L_x^2}{288\, \nu}.$$

Rewriting in units of $t_c = L_x^2 / (8 \pi^2 \nu)$:
$$\frac{t_{\mathrm{cross}}}{t_c} \;=\; \frac{8 \pi^3}{288} \;=\; \frac{\pi^3}{36} \;\approx\; 0.861.$$

No fits. No thresholds. An exact rational-plus-$\pi^3$ prefactor. The numerical verification agrees with the closed form to within 3% at $t = t_c$, and the relative error stays under 10% out to $t \sim 2\, t_c$. The paper's claim was right all along. I was pointing the wrong lens at it.

## The observable is the argument

I keep learning the same lesson, and the lesson keeps being useful anyway. A lot of "information-theoretic" arguments in physics quietly assume the right observable is an abstract likelihood — that if you phrase a question in terms of $\log p_1 / p_0$, nature will cooperate. Sometimes it does. Sometimes the likelihood is *structurally* blind to the thing you care about, because the thing you care about lives exactly at the point where two distributions agree.

The Edwards–Wilkinson width doesn't know this. It doesn't care about hypotheses. It just grows, and at a specific rational multiple of $t_c$ it hits a specific closed-form value that corresponds to the other hypothesis's saturation. That is a perfectly good detection criterion. It's just not a likelihood ratio.

The width was right. It always was. I had to try three wrong things before I believed it.
