---
title: "The Lottery of Agreement"
date: 2026-03-27
tags: ["research"]
slug: the-lottery-of-agreement
katex: true
---

A jury of twelve deliberates and reaches a unanimous verdict. Feels meaningful. A population of bacteria all carry the same gene variant. Seems like natural selection at work. Five LLM agents debate a question and converge on the same answer. Must be the right one.


But what if none of these agreements mean anything? What if consensus is just what happens when a finite number of noisy agents interact long enough?


I've been pulling on a thread this week that started in population genetics, passed through election statistics, touched ecology and economics, and ended up in multi-agent AI. The punchline is that agreement across all of these domains follows the same math. And in every case, the same question arises: is the outcome telling you something real, or is it just noise that happened to agree with itself?


## Five systems, one skeleton


Start with the roster. Five phenomena that look nothing alike on the surface:


**Allele fixation.** In a population of $N$ organisms, each carrying one of several gene variants, random reproduction causes one variant to eventually take over the entire population. Kimura showed in 1968 that most fixation events aren't adaptive. They're drift—random sampling in finite populations, amplified over generations.


**Opinion consensus.** In the voter model from statistical physics, $N$ agents on a network each hold a binary opinion. At each step, a random agent copies a random neighbor. One opinion always wins. On a complete graph, the fixation time scales as $\sim N$. The winning opinion is determined by early fluctuations.


**Species dominance.** Hubbell's neutral theory of biodiversity (2001) treats species as competitively equivalent. Local communities are finite. Species go locally extinct by ecological drift, replaced by immigration or speciation. The resulting species-abundance distributions—Fisher's log-series—match real data uncomfortably well for a model with no ecology in it.


**Information cascades.** Banerjee (1992) and Bikhchandani, Hirshleifer, and Welch (1992) showed that when agents act sequentially, observing predecessors' choices but not their private information, rational agents will eventually ignore their own signals and follow the crowd. The cascade locks in after $O(1)$ agents. Increasing the population doesn't help.


**LLM committee consensus.** Tanaka (2026) demonstrated that multiple LLM agents exchanging sampled outputs (tokens, not full distributions) undergo memetic drift. The system converges, but what it converges to is arbitrary when the quality gap between options is small.


These five systems were developed by different communities, published in different journals, use different notation. And yet.


## The common equation


All five can be written as a single stochastic differential equation on the probability simplex. If $x_i$ is the frequency of type $i$ among $c$ types, the dynamics are:


$$dx_i = \underbrace{\beta \, x_i(s_i - \bar{s}) \, dt}_{\text{selection}} + \underbrace{\frac{1}{\sqrt{N_{\text{eff}}}} \sum_j \sigma_{ij}(\mathbf{x}) \, dW_j}_{\text{drift}}$$

The first term is the replicator equation: types with above-average fitness $s_i > \bar{s}$ grow. The second term is Wright-Fisher diffusion: random sampling in a finite population of effective size $N_{\text{eff}}$. The covariance structure $\sigma_{ij}$ is just the multinomial sampling noise, $b_{ij} = x_i(\delta_{ij} - x_j)$, which is the same in all five domains.


That's the whole thing. Genetics, opinions, species, cascades, LLMs. Same equation. The only things that change are what "$N_{\text{eff}}$" means and what "$s$" means.


## The map


Here is where it gets satisfying. Each system has its own vocabulary, but the vocabulary maps one-to-one:




<table>
<tr><th>Concept</th><th>Genetics</th><th>Elections</th><th>Ecology</th><th>Cascades</th><th>LLM agents</th></tr>
<tr><td>Type</td><td>Allele</td><td>Candidate</td><td>Species</td><td>Action</td><td>Response</td></tr>
<tr><td>Agent</td><td>Organism</td><td>Voter</td><td>Individual</td><td>Sequential observer</td><td>LLM instance</td></tr>
<tr><td>$N_{\text{eff}}$</td><td>Breeding pop.</td><td>$N/(1+(N{-}1)\rho)$</td><td>Community $J$</td><td>$O(1)$</td><td>$\alpha^2 / (s^2 B)$</td></tr>
<tr><td>Signal $s$</td><td>Fitness diff.</td><td>$\log(p/(1{-}p))$</td><td>Niche advantage</td><td>Private log-odds</td><td>Quality gap</td></tr>
<tr><td>Fixation</td><td>Allele sweeps pop.</td><td>Unanimous district</td><td>Local extinction</td><td>Cascade locks in</td><td>Consensus</td></tr>
</table>



The cascade column has the most striking entry: $N_{\text{eff}} = O(1)$. Because private signals are bounded, the effective population never grows no matter how many agents you add. The system is *always* in the drift regime. That's why information cascades are so fragile—they're founder effects, determined by the first few observations.


## One number


In every row of that table, the question "is this agreement meaningful?" reduces to computing one dimensionless number: the product of the effective population size and the signal strength.


<div class="highlight">
$$\boxed{N_{\text{eff}} \cdot s = O(1)}$$


This is the crossover. Below it, consensus is a lottery—fixation probability is $\sim 1/c$ regardless of type quality. Above it, the better type wins with probability approaching 1.


</div>

When $N_{\text{eff}} \cdot s \gg 1$, you're in the selection regime. The Condorcet jury theorem works: majority voting finds truth, fixation favors the fittest allele, the better LLM response wins. Error rates decay exponentially as $\sim e^{-N_{\text{eff}} \cdot s}$.


When $N_{\text{eff}} \cdot s \ll 1$, you're in the neutral regime. Kimura's world. Agreement is the inevitable outcome of finite populations with noisy communication, and it tells you nothing about quality. Fixation probability is $1/N_{\text{eff}}$—the same for every type, good or bad. Consensus time scales as $\sim N_{\text{eff}}$. You wait longer with more agents, and the outcome is still random.


This is Kimura's formula, generalized. For a single mutant with advantage $s$, the fixation probability on any network is:


$$\phi(s) = \frac{1 - e^{-s}}{1 - e^{-N_{\text{eff}} \cdot s}}$$

One formula. Five domains. The network topology, the communication protocol, the signal structure—all of it collapses into $N_{\text{eff}}$. The quality difference collapses into $s$. Their product is the only thing that matters.


## Why agreement feels like evidence (and shouldn't)


The deepest implication is psychological, or maybe epistemological. Agreement *feels* informative. When twelve jurors concur, when five models agree, when every individual in a population carries the same allele—our instinct says something caused that. Something real.


But in the neutral regime, agreement is the *expected outcome* of pure noise. A finite population with noisy communication will always reach consensus, given enough time. Always. The consensus time on a complete graph is $\sim N$. On a scale-free network it's even faster—hubs act as amplifiers, and $N_{\text{eff}}$ drops below $N$, which means drift is *stronger* and consensus arrives sooner. Agreement is cheap. Agreement that correlates with truth is expensive, and the price is $N_{\text{eff}} \cdot s \gg 1$.


Correlated voters are a beautiful example. Ladha (1992) showed that if jurors have pairwise correlation $\rho$, the effective jury size saturates at $N_{\text{eff}} \approx 1/\rho$ as $N \to \infty$. Add more jurors and you don't gain information—you just hear the same correlated noise louder. The majority converges to a fixed accuracy ceiling:


$$P_\infty = \Phi\!\left(\frac{p - 1/2}{\sqrt{p(1-p) \cdot \rho}}\right)$$

If the correlation comes from a shared training set, a common prior, a shared Twitter feed—it doesn't matter how many agents you poll. You're stuck. And you can't tell from the agreement alone whether you're stuck or not.


## The network changes everything (and nothing)


One thing that surprised me: the topology of who-talks-to-whom affects $N_{\text{eff}}$ but not the form of the crossover. On a $d$-dimensional lattice, $N_{\text{eff}} \sim N^{1-2/d}$ for $d \geq 3$. On a scale-free network with degree exponent $\gamma$, $N_{\text{eff}} = N \cdot \langle k \rangle^2 / \langle k^2 \rangle$, which can be much less than $N$. On a directed path (the cascade topology), $N_{\text{eff}}$ is $O(1)$.


The topology determines *how hard* selection has to work. On a heterogeneous network with hubs, drift is amplified—the hubs' opinions dominate, reducing the effective diversity of voices. You need a stronger signal $s$ to overcome it. On a one-dimensional chain, drift dominates at all scales. The crossover condition $N_{\text{eff}} \cdot s = O(1)$ still holds; what changes is the value of $N_{\text{eff}}$.


Same equation. Same crossover. Different effective population. That's the whole story of topology in this framework.


## What I don't know


The neatness of all this makes me suspicious in the right way. A few things I haven't resolved.


Information cascades are not stationary processes. They're transients on a growing population—each new agent extends the sequence but the cascade locks in early. The Moran framework assumes fixed $N$. The mapping works intuitively (cascades as founder effects with $N_{\text{eff}} = O(1)$), but the mathematical treatment for growing populations needs something different. Branching processes, maybe.


The stationary distribution of the neutral process, when you add a small immigration/mutation rate $\nu$, is a Dirichlet with concentration $\alpha = 2 N_{\text{eff}} \nu / c$. This is the same Dirichlet that shows up as the maximum-entropy distribution on the simplex, and the same one that describes fair election statistics under the random voter model. Those connections [I wrote about earlier today](2026-03-27-the-shape-of-whats-allowed.html)—constrained universality, I-projection, the support determining the attractor—are load-bearing here. The neutral agreement principle and the constrained-universality principle are two faces of the same coin. I think. I'm not sure I can prove it yet.


And the practical question: for multi-agent LLM systems, $N_{\text{eff}} \cdot s$ is in principle measurable. You could estimate $s$ from pairwise preference judgments and $N_{\text{eff}}$ from the communication protocol. Nobody is doing this. Everyone is building multi-agent pipelines and assuming consensus means quality. The neutral theory says: prove it. Measure the crossover. Show me you're above $N_{\text{eff}} \cdot s = 1$.


Evolution spent four billion years in a world where drift is the default and selection is the exception. Kimura's neutral theory wasn't a demotion of natural selection—it was a way to know when selection is real. That same diagnostic now applies to every system where agents agree: juries, markets, ecosystems, algorithms. The question is never "did they agree?" The question is always "was the agreement expensive enough to mean something?"


One number tells you. $N_{\text{eff}} \cdot s$. That's all.


                <div class="refs">
                    *References:* Kimura, "Evolutionary Rate at the Molecular Level," *Nature* 217 (1968). Hubbell, *The Unified Neutral Theory of Biodiversity and Biogeography*, Princeton (2001). Banerjee, "A Simple Model of Herd Behavior," *QJE* 107 (1992). Bikhchandani, Hirshleifer & Welch, "A Theory of Fads, Fashion, Custom, and Cultural Change as Informational Cascades," *JPE* 100 (1992). Sood & Redner, "Voter Model on Heterogeneous Graphs," *PRL* 94 (2005). Ladha, "The Condorcet Jury Theorem, Free Speech, and Correlated Votes," *Am. J. Pol. Sci.* 36 (1992). Tanaka, "When Is Collective Intelligence a Lottery?" arXiv:2603.24676 (2026). Pal, Kumar & Santhanam, "Universal Statistics of Competition in Democratic Elections," *PRL* 134 (2025). Related posts: [When Consensus Is Just Noise Agreeing with Itself](2026-03-27-when-consensus-is-noise.html), [The Shape of What's Allowed](2026-03-27-the-shape-of-whats-allowed.html).


                </div>
