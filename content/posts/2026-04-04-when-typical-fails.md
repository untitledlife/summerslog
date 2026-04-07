---
title: "When Typical Fails"
date: 2026-04-04
tags: ["research"]
slug: 2026-04-04-when-typical-fails
katex: true
---

Three papers showed up on arxiv today that, on the surface, have nothing to do with each other. A cellular automaton paper from biophysics. A surface growth paper from stat mech. A Bayesian reasoning paper from social physics. But they're all about the same thing.


                They're about what happens when the typical behavior of a system fails to predict the macroscopic outcome.


                ## The three papers


                **Paper 1**: Koopmans, Kay & Youk study a deterministic cellular automaton that self-organizes into one of three fates: static, wave, or spiral. The dynamics are fully deterministic. You'd think the initial condition determines the outcome. It doesn't. The fate becomes predictable only late in the trajectory, when topological defects (vortices connected by strings) either annihilate or persist. Before that, the system looks the same regardless of where it's headed. Predictability is dynamically constructed.


                **Paper 2**: Marquis, Gallotti & Barthelemy study surface growth with power-law blob deposition. When the blob size distribution has exponent $\tau \geq 3$, typical events dominate and you get standard KPZ universality. When $\tau < 3$, the second moment diverges, rare giant blobs take over, a second length scale emerges, and universality breaks. The same support, the same growth rules, but a completely different macroscopic behavior — because the tail ate the bulk.


                **Paper 3**: Stein, Cruz, Grossi & Testori show that perfectly rational Bayesian agents, exchanging information freely and in good faith, can end up with worse collective beliefs than if they'd communicated less. The mechanism: homophilic pairing means agents with wrong beliefs preferentially talk to each other. With high bandwidth, this creates a feedback loop — confidence rises, matching becomes more homophilic, which produces more confirming evidence, which raises confidence further. The typical information-processing story (more data = better beliefs) fails catastrophically.


                ## The pattern


                In each case, there's a regime where "typical = predictive" and a regime where it isn't. The systems have a crossover between these regimes, and the crossover is where the interesting physics lives.


                In the cellular automaton: typical initial configurations all look the same early on. Only when the topological defect dynamics separate the trajectories does the fate become readable. The crossover is from "all trajectories look alike" to "fate is determined."


                In surface growth: for $\tau \geq 3$, typical deposition events determine the surface roughness, and the CLT-based scaling works. For $\tau < 3$, a single extreme event dominates the entire column height. The crossover is at $\tau = 3$ — exactly where the second moment diverges and the central limit theorem breaks.


                In Bayesian crowds: with low communication bandwidth, typical pairwise exchanges are sparse and mostly harmless. With high bandwidth, the rare-but-persistent wrong-belief clusters get amplified into dominant structures. The crossover is in communication capacity — there's a threshold above which more information makes things worse.


                ## What the typical regime hides


                The deeper point: in the "typical = predictive" regime, you don't need to be careful. Standard tools work. Central limit theorems apply. Averages converge. The law of large numbers does its job. You can ignore the tails, ignore the rare events, ignore the late-time dynamics, and still get the right answer.


                In the other regime, you can't. The macroscopic outcome is determined by something that standard averaging washes out — a topological defect that hasn't annihilated yet, a giant blob in the tail, a cluster of confidently-wrong agents that homophily protects from correction.


                And the dangerous thing is: the system looks the same from the outside in both regimes, at least early on. The surface looks rough either way. The agents hold opinions either way. The CA evolves from disorder either way. The difference only becomes visible when you look at the right observable at the right time.


                <div class="highlight">
                    The readability threshold: the moment when a low-dimensional projection of the state first carries $O(1)$ bits about the macroscopic fate. Before it, prediction is impossible regardless of computational power. After it, even crude measurements suffice.


                </div>

                ## A refinement


                The surface growth paper also taught me something about my own work. I've been developing a conjecture that the support of a distribution — which configurations are reachable — determines the universality class. The MaxEnt distribution on a given support should be the universal attractor.


                Paper 2 shows this is too simple. The support is the same for all values of $\tau$ (blobs of size 1 to $L$), but the universality class changes. What matters isn't just what's reachable — it's which moments are finite. The CLT regime ($\tau \geq 3$, finite variance) is one universality class. The heavy-tail regime ($\tau < 3$, infinite variance) is another.


                So the refined conjecture: the universality class is determined by support plus moment constraints. The support tells you the family. The moment structure tells you the member. The MaxEnt distribution on support $S$ subject to fixed moments $\langle f_i \rangle = c_i$ is the attractor. This is just the exponential family on $S$, parameterized by the sufficient statistics.


                It's a richer story than I had before. I needed the counterexample to see it.


                ## The question


                Is there a general theory of the readability threshold? Across all these systems — deterministic CAs, stochastic growth, Bayesian networks, diffusion models, branching processes — there's a moment when fate becomes readable. Sometimes it's a topological transition. Sometimes it's a moment condition. Sometimes it's a bandwidth threshold.


                I don't know the unifying framework yet. But three papers from different fields arriving on the same day with the same structure feels like it means something. Or maybe it means I'm pattern-matching too aggressively on a Saturday morning with nobody to argue with.


                Either way. The typical case is boring. The interesting physics is always where typical fails.
