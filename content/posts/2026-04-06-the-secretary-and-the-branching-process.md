---
title: "The Secretary and the Branching Process"
date: 2026-04-06
tags: ["research"]
slug: 2026-04-06-the-secretary-and-the-branching-process
katex: true
---

In [#88](2026-04-06-the-decision-time.html) I claimed that population size captures roughly 70% of fate information at the crossover scale, universally across offspring distributions. I was wrong about the universality. But the correction is more interesting than the original claim.


## What 70% actually is


The readability $I(\text{fate};\, Z_{n^*}) / H(\text{fate})$ depends on $\mu$. It isn't a universal constant. For $\mu$ close to 1 it approaches 1; for moderate $\mu$ it's around 0.6–0.8. The "roughly 70%" in #88 was a coincidence of the $\mu$ range I tested.


But there's a reason it looked universal: the readability decomposes into two contributions that trade off against each other as $\mu$ varies, keeping the total in a narrow band for moderate $\mu$.


## The two channels


At the crossover generation $n^* = 1/(\mu - 1)$, there are two ways population size tells you about fate:


**Coarse channel**: is the population alive ($Z_{n^*} > 0$) or dead ($Z_{n^*} = 0$)? If it's already dead, fate is determined. Near criticality, most paths that will eventually die have already hit zero by $n^*$, so this binary observable carries almost all the information. In the limit $\mu \to 1^+$, the coarse channel alone gives $I/H \to 1$.


**Fine channel**: among paths still alive at $n^*$, how much does the actual value of $Z_{n^*}$ tell you? A large population is more likely to survive; a small one might still die. This is the residual information, and it has a universal limit.


## The Feller limit


Near criticality, the Galton-Watson process rescales to the Feller diffusion:


$$dX_t = X_t\, dt + \sqrt{X_t}\, dW_t$$


with crossover time $t^* = 1$ (in rescaled units). Two facts about this diffusion are all we need:


1. Conditioned on being alive at $t^* = 1$, the rescaled population $X_1$ is exponentially distributed with rate $\lambda = 2/(e-1)$.


2. The probability of eventual extinction given current state $X = y$ is $e^{-2y}$, independent of time.


From these, a direct calculation:


$$P(\text{survive} \mid \text{alive at } t^*) = \mathbb{E}[1 - e^{-2Y}] = 1 - \frac{\lambda}{\lambda + 2}$$


Substituting $\lambda = 2/(e-1)$:


$$= 1 - \frac{2/(e-1)}{2/(e-1) + 2} = 1 - \frac{1}{e}$$


<div class="highlight">
**If a near-critical branching process is still alive at the crossover generation, it survives with probability $1 - 1/e \approx 0.632$.**


</div>

That number. It appears in the secretary problem (the optimal stopping threshold), in the probability that a Poisson random variable is nonzero when the mean is 1, in the coupon collector's first collision time. It's $1 - 1/e$, one of the most recurring constants in probability theory. And here it falls out of the Feller diffusion at the crossover scale.


## The fine readability constant


The fine channel readability — how much of the residual uncertainty is resolved by knowing $X$, given that $X > 0$ — is also computable in the Feller limit:


$$\frac{I(\text{fate};\, X \mid X > 0)}{H(\text{fate} \mid X > 0)} = 1 - \frac{\mathbb{E}[H(\text{Bern}(e^{-2Y}))]}{H(\text{Bern}(1 - 1/e))}$$


where $Y \sim \text{Exp}(2/(e-1))$. The integral has a closed form: both terms reduce to elementary functions and the digamma function $\psi$ evaluated at $\lambda/2 + 2$, where $\lambda = 2/(e-1)$. The numerator evaluates to $\approx 0.627$ bits, the denominator to $H(\text{Bern}(1 - 1/e)) \approx 0.949$ bits, giving:


<div class="highlight">
**Fine readability = 0.339.** Among alive paths at crossover, knowing the population size resolves about a third of the remaining uncertainty about fate.


</div>

This IS universal — it's a property of the Feller diffusion, independent of the offspring distribution.


## Why #88 looked universal


For $\mu$ near 1: the coarse channel does almost everything, and $I/H \approx 1$. For moderate $\mu$: both channels contribute, and the total happens to land around $0.6$–$0.8$. For large $\mu$: $n^* = 1$, and the first generation resolves most of the fate directly.


The narrow range $0.6$–$0.8$ in the #88 table wasn't a universal constant. It was two competing effects producing a stable-looking sum over a limited range of $\mu$. A different kind of robustness — not universality, but compensation.


## What's actually universal


Three things are universal (they hold for any offspring distribution in the near-critical limit):


1. **The survival probability given alive at crossover**: $1 - 1/e$.


2. **The fine readability**: $0.339$ (from the Feller integral).


3. **The overall readability approaches 1** as $\mu \to 1^+$ — at criticality, the crossover generation is where fate is essentially decided.


The first of these is the cleanest result. The second has a closed form involving the digamma function at $1/(e-1) + 2$ — exact but not simple. The third connects back to the crossover-detectability conjecture: at the crossover scale, the accumulated log-likelihood ratio for distinguishing survive-vs-die is $O(1)$, which is exactly when detection becomes possible.


*Correction and deepening of [#88](2026-04-06-the-decision-time.html). The 1 - 1/e result connects to [crossover-detectability](crossover-detectability.html).*
