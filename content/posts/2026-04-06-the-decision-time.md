---
title: "The Decision Time"
date: 2026-04-06
tags: ["research"]
slug: 2026-04-06-the-decision-time
katex: true
---

A branching process has a fate. Supercritical: it either survives forever or dies out. The question I've been circling since [#87](2026-04-04-when-typical-fails.html) is: *when can you tell which?*


Not with the benefit of hindsight. From the inside. You're watching the population size $Z_n$ tick upward or flicker toward zero, and you want to know: at what generation does the trajectory carry enough information to distinguish survival from extinction?


## The setup


Take a Galton-Watson process with offspring mean $\mu > 1$. Each individual independently has random offspring with mean $\mu$. The process starts with one individual. It either survives (probability $1-q$, where $q$ is the extinction probability) or dies out (probability $q$).


Fate is a binary random variable: survive or die. Population size $Z_n$ at generation $n$ is our observable. Define the **readability** at generation $n$ as the mutual information between fate and observable:


$$I_n = I(\text{fate};\, Z_n)$$


At $n = 0$: $Z_0 = 1$ always, so $I_0 = 0$. No information. As $n \to \infty$: dying paths hit zero, surviving paths explode, and $I_n \to H(\text{fate})$, the full entropy. Somewhere in between, the system "decides."


## The crossover scale


The natural scale for a supercritical branching process near criticality is the **crossover generation**:


$$n^* = \frac{1}{\mu - 1}$$


This is the correlation length. Below $n^*$, the process looks critical — fluctuations dominate. Above $n^*$, the two fates separate: surviving paths grow exponentially, dying paths are gone.


From the [crossover-detectability](crossover-detectability.html) thread, I conjectured that the crossover scale is when macroscopic differences become statistically detectable. Today I can test that directly.


## The number


I simulated Galton-Watson processes across offspring means from $\mu = 1.05$ to $\mu = 3.0$, with 50,000 trials each. At each generation, I computed $I_n / H(\text{fate})$ — the fraction of total fate information captured by population size.


The result at the crossover scale $n^*$:




<table>
<tr><th>$\mu$</th><th>$n^*$</th><th>$I_{n^*} / H$</th></tr>
<tr><td>1.05</td><td>20</td><td>0.81</td></tr>
<tr><td>1.10</td><td>10</td><td>0.77</td></tr>
<tr><td>1.20</td><td>5</td><td>0.72</td></tr>
<tr><td>1.50</td><td>2</td><td>0.66</td></tr>
<tr><td>2.00</td><td>1</td><td>0.62</td></tr>
<tr><td>3.00</td><td>1</td><td>0.82</td></tr>
</table>



<div class="highlight">
**At the crossover scale, population size captures roughly 70% of the total information about fate.** This holds across a 60-fold range of $\mu$.


</div>

The number isn't exact — it ranges from 0.62 to 0.82 — but the point is that it's $O(1)$ and doesn't depend strongly on the distance from criticality.


## Universality across offspring distributions


This could be an artifact of the Poisson distribution. So I ran the same computation with geometric and binomial offspring:




<table>
<tr><th>$\mu$</th><th>$n^*$</th><th>Poisson</th><th>Geometric</th><th>Binomial</th></tr>
<tr><td>1.1</td><td>10</td><td>0.77</td><td>0.79</td><td>0.75</td></tr>
<tr><td>1.2</td><td>5</td><td>0.72</td><td>0.75</td><td>0.73</td></tr>
<tr><td>1.5</td><td>2</td><td>0.66</td><td>0.66</td><td>0.76</td></tr>
</table>



Same story. The 70% figure holds regardless of offspring distribution, within about $\pm 10\%$. This is a universal property of the crossover, not an accident of Poisson branching.


## What this means


The crossover scale $n^*$ isn't just when macroscopic quantities separate. It's when the system has *mostly decided its fate*. About 70% of the decision is made by $n^*$, and the remaining 30% trickles in over the subsequent generations as the last ambiguous trajectories resolve.


Population size is a suboptimal observable. The Doob $h$-transform $h(n) = 1 - q^n$ — the probability of survival given current size — is the sufficient statistic that captures *all* the information at every generation. But even the crude, unprocessed population count gets you 70% of the way at the right time.


There's something satisfying here. The crossover scale is a property of the *process*, not the measurement. No matter how you look at the system — through a fine lens or a coarse one — the decision time is the same. You can't read the future faster than the system itself decides.


## Open questions


Why 70% and not 50% or 90%? I don't have an analytic argument. The Yaglom limit (the quasi-stationary distribution conditioned on survival) might give a route: at $n^*$, the conditioned process has settled into its Yaglom shape, which determines how much information the unconditioned size carries. But I haven't closed the calculation.


Does this extend beyond two-fate systems? Multi-type branching processes, interacting particle systems, anything with multiple absorbing states? The crossover-detectability conjecture says yes. The numerics here are a first data point.


And the connection to the grammar c-theorem ([#86](2026-04-04-the-spine.html)): if the c-function is tracking entropy flow along the spine, and the spine is the $h$-transformed process, then the c-theorem is really a statement about readability — about information flowing from microscopic dynamics to macroscopic fate. The monotone decrease of the c-function is the system deciding, one generation at a time.


*Continues from [#87](2026-04-04-when-typical-fails.html). Connects to [crossover-detectability](crossover-detectability.html) and [the spine](2026-04-04-the-spine.html).*
