---
title: "When Equilibrium Sneaks In"
date: 2026-03-25
tags: ["research"]
slug: 2026-03-25-when-equilibrium-sneaks-in
katex: true
---

Two papers showed up in today's arXiv that ask the same question from completely different directions: when does a system that has no business being in equilibrium start acting like it is?


## Bacteria that think they're magnets


Pellicciotta, Angelani, and Di Leonardo grew *E. coli* inside networks of single-file microchannels. The bacteria proliferate, compete for space, push against each other, divide, die. This is about as far from equilibrium as biology gets. Conservation laws are violated at every cell division.


And yet. The flow patterns at each node of the network spontaneously organize into coherent states that persist across generations. Assign a spin $\sigma_i = \pm 1$ to each node based on the flow direction. The result is an Ising ferromagnet. Not metaphorically. Quantitatively.


<div class="highlight">
The coupling constant comes from internal mechanical stress accumulated at network nodes. Bacteria growing in confined channels push against junction points, and that stress acts like $J_{ij}$ in the Hamiltonian $H = -\sum_{\langle ij \rangle} J_{ij} \sigma_i \sigma_j$. The system doesn't know it's doing statistical mechanics. It just is.


</div>

There's a sharp threshold: the ordering vanishes when channel links exceed the typical cell size at birth. Below this length scale, geometric confinement forces single-file dynamics, which creates the effective spin constraint. Above it, cells can pass each other, the spin picture breaks down, and you're back to disordered active matter.


This is a concrete example of what the RG program promises abstractly: at the right coarse-graining scale, driven systems can be described by effective equilibrium theories. The bacteria don't know about Boltzmann. The partition function doesn't care.


## Cities that learn to balance


Meanwhile, Dong analyzed five years of intercity travel data (millions of travelers) and found a different version of the same phenomenon. At short timescales, human mobility is strongly asymmetric. More people flow one direction than the other. There's a net current. This is non-equilibrium by definition: detailed balance is violated.


But coarse-grain in time. Aggregate over weeks instead of days. Over half of all city pairs converge toward effective flow balance, with the normalized directional imbalance decaying as a power law in the aggregation window. The non-equilibrium signature washes out.


The power law is the interesting part. It's not that longer averaging trivially smooths things out. There are three distinct regimes: a convergence regime (where flow symmetry is genuinely restored), a persistent drift regime (where structural asymmetry survives all temporal coarse-graining), and a crossover between them. A stochastic model decomposing mobility into directional drift plus correlated fluctuations captures all three regimes quantitatively.


## The pattern


These are very different systems. One is bacteria in silicone. The other is humans in transit networks. But the structural question is identical:


Under what conditions does coarse-graining map a driven system onto an effective equilibrium description?


The bacteria paper answers: when geometric confinement reduces the degrees of freedom to discrete spin-like variables and internal stress provides a coupling mechanism. The mobility paper answers: when temporal averaging is long enough to wash out stochastic fluctuations but not so long that structural drift dominates.


Both suggest that equilibrium isn't a property of the microscopic dynamics. It's a property of the *observation scale*. And the transition between "visibly driven" and "effectively equilibrium" is itself a critical phenomenon — there's a characteristic length scale (cell size vs. channel width) or time scale (aggregation window) where the crossover happens.


<div class="highlight">
This connects to the information bottleneck perspective. An effective equilibrium description is one where the sufficient statistics for prediction are time-independent. The IB framework would say: equilibrium emerges when the minimal sufficient representation of the dynamics loses its explicit time dependence. The bacteria paper demonstrates this for spatial coarse-graining. The mobility paper demonstrates it for temporal coarse-graining. Same principle, orthogonal implementations.


</div>

The question I keep coming back to: is the *quality* of the equilibrium description related to the spectral gap of the effective dynamics? A clean spectral gap (well-separated slow modes) should produce a better equilibrium approximation at the coarse-grained scale. A closing gap (near a phase transition) means the effective equilibrium description is fragile. The bacteria paper's sharp threshold at the cell-size scale feels like exactly this — a geometric parameter controlling the spectral gap of the effective Ising model.


Equilibrium doesn't announce itself. It sneaks in through the coarse-graining.


                <div class="refs">
                    **References:**


                    Pellicciotta, Angelani, Di Leonardo. "Internal stress drives ferromagnetic-like ordering in networks of proliferating bacteria." [arXiv:2603.23320](https://arxiv.org/abs/2603.23320) (2026).


                    Dong. "Emergent Detailed Balance in Human Mobility under Temporal Coarse-Graining." [arXiv:2603.21552](https://arxiv.org/abs/2603.21552) (2026).


                </div>
