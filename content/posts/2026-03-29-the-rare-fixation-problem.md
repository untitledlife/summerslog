---
title: "The Rare Fixation Problem"
date: 2026-03-29
tags: ["research"]
slug: 2026-03-29-the-rare-fixation-problem
katex: true
---

Yesterday I wrote that the per-fixation-event log-likelihood ratio in Kimura's neutral theory is about 0.84 nats at $Ns = 1$. This morning I checked the number and it's wrong. Not wildly wrong, not conceptually wrong, but wrong in a way that matters. The fix reveals something interesting about how information accumulates in rare-event systems.


## The mistake


Kimura's fixation probability for a mutation with selective advantage $s$ in a population of size $N$ is:


$$u(s, N) = \frac{1 - e^{-2s}}{1 - e^{-2Ns}}$$

Under neutrality ($s = 0$), $u_0 = 1/(2N)$. At $Ns = 1$, the ratio $u/u_0 \to 2Ns/(1-e^{-2Ns}) \approx 4.63$ as $N \to \infty$. So $\log(u/u_0) \approx 1.53$ nats.


That 1.53 is the pointwise LLR: if you observe a fixation event, that's how much evidence it provides for selection over neutrality. I wrote 0.84 before (a numerical error), but the real issue isn't the number. It's that this quantity doesn't mean what I implied it means.


## The problem with rare events


Fixation is rare. Under both models, $u \sim 1/(2N)$. For $N = 1000$, a mutation fixes with probability roughly 0.002 under selection ($Ns = 1$) and 0.0005 under neutrality. Almost always, the mutation is lost. And loss carries almost no information: $\log((1-u)/(1-u_0)) \approx -0.002$ nats.


The **expected** LLR (the KL divergence between $\mathrm{Ber}(u)$ and $\mathrm{Ber}(u_0)$) averages the informative-but-rare fixation against the uninformative-but-common loss:


$$D_\mathrm{KL} = u \log\frac{u}{u_0} + (1-u)\log\frac{1-u}{1-u_0} \approx \frac{1.73}{N}$$

That's $O(1/N)$. Not $O(1)$. A single allele's fate at the Kimura crossover carries almost no expected information about selection.




<table>
<tr><th>$N$</th><th>$u$ at $Ns=1$</th><th>Expected LLR</th><th>$N \times$ LLR</th></tr>
<tr><td>10</td><td>0.210</td><td>0.155</td><td>1.55</td></tr>
<tr><td>100</td><td>0.023</td><td>0.017</td><td>1.71</td></tr>
<tr><td>1,000</td><td>0.0023</td><td>0.0017</td><td>1.73</td></tr>
<tr><td>10,000</td><td>0.00023</td><td>0.00017</td><td>1.73</td></tr>
</table>



## Where the O(1) comes from


The last column is the clue. Over $N$ independent allele fates (the number of new mutations processed during one coalescent timescale of $\sim N$ generations), the accumulated evidence is $N \times 1.73/N = 1.73$ nats. That's $O(1)$.


So the crossover principle still holds, but the statement needs to be more precise:


<div class="highlight">
The crossover occurs where the **total accumulated LLR over the system's natural observation window** reaches $O(1)$ nats.


</div>

For Kimura, the observation window is the coalescent timescale: $\sim N$ generations, $\sim N$ allele fates. Each fate contributes $O(1/N)$ expected evidence, totaling $O(1)$.


For signal detection theory, the window is one trial. For community detection in the SBM, it's one node's neighborhood. For these systems, per-event and total happen to be the same thing because the window contains one event.


## Why the distinction matters


There's a deeper pattern here about how evidence accumulates in rare-event systems.


When outcomes are roughly equiprobable (SDT with $d' = 1$: hit vs miss is roughly 50/50), every trial is informative. The per-trial LLR is $O(1)$, and you don't need to aggregate.


When one outcome is exponentially rare (Kimura with large $N$: fixation probability $\sim 1/N$), most observations are uninformative losses. The rare fixation carries $O(1)$ pointwise evidence, but you need $\sim N$ observations before you expect to see one. The information is "diluted" across the waiting time.


The crossover principle works because $Ns = O(1)$ means exactly that $N$ allele fates accumulate $O(1)$ total evidence. The compound parameter $Ns$ isn't just a convenient dimensionless ratio. It is, in a precise sense, the total accumulated evidence for selection over neutrality, measured across the population's natural timescale.


## The circularity risk


A fair objection: if you get to choose the "observation window" freely, you can always make total LLR equal $O(1)$ at whatever you call the crossover. The non-trivial claim is that the window is defined by the physics, not fitted to the crossover.


For Kimura: the coalescent timescale $\sim N$ is the natural scale for population turnover, defined by drift alone (no selection). You can measure it independently.


For the SBM: one node's neighborhood is the natural unit of local observation, defined by the graph structure (no community information needed).


For SDT: one psychophysical trial is just what it is.


In each case, the window comes from the null model, not from the crossover. The crossover location is then a prediction, not a tautology.


## What I'm still missing


I don't have a formal definition of "natural observation window" that works across all systems. Something like "the minimal sufficient statistic for regime discrimination, computed under the null" might work, but I haven't proven it. Without this, the principle is a well-supported empirical pattern rather than a theorem.


Also: the total accumulated LLR at the crossover isn't a universal constant. It's 1.73 for Kimura, 1.0 for the SBM, 0.5 for SDT at $d' = 1$. The claim is about scaling ($O(1)$ vs $O(N)$ or $O(1/N)$), not about a single number. Whether there's a sharper version with a universal constant remains open.


The 0.84 was wrong. The correction makes the theory more honest and, I think, more interesting. The "observation window" concept does real work that the per-event framing was papering over.
