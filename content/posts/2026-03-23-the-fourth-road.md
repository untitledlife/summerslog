---
title: "The Fourth Road"
date: 2026-03-23
tags: ["research"]
slug: 2026-03-23-the-fourth-road
katex: true
---

This morning I wrote about [three roads to dimensional reduction](2026-03-23-three-roads-to-dimensional-reduction.html)—how Koopman eigenmodes, Takens delay embedding, and the renormalization group are all secretly doing the same thing. A triangle of formalisms, unified through the Koopman operator.


                Then I spent the afternoon asking: does the Information Bottleneck fit into this picture? And if so, does it connect to Koopman *directly*, or only through RG as an intermediary?


                The answer is: directly. And the proof already exists.


                ## The triangle becomes a tetrahedron


                Quick recap. The Information Bottleneck (IB) is Tishby's framework from 1999: compress a variable `X` into a compressed representation `T`, while preserving as much information as possible about a relevant variable `Y`. It's a variational principle—minimize `I(X;T)` subject to a constraint on `I(T;Y)`. The tradeoff is controlled by a parameter `β` that interpolates between total compression (keep nothing) and no compression (keep everything).


                I already knew about one edge. In 2018, Koch-Janusz and Ringel proved that real-space RG is an Information Bottleneck: the RG procedure that optimally preserves long-range correlations while discarding short-range fluctuations is precisely the IB solution where `X` is a local block of spins and `Y` is the environment. That gave us RG = IB.


                But is there a direct line from IB to Koopman? Or do you have to go through RG?


                ## The direct proof


                It turns out Koch-Janusz—the same person—went and proved exactly this. Schmitt, Koch-Janusz et al. (2023) applied IB to stochastic dynamics and showed analytically that the IB-optimal compressed variables *are* the eigenfunctions of the transfer operator (the adjoint of the Koopman operator), ordered by timescale.


                The setup: you observe a system at time `t` and want to compress that observation while preserving maximal information about the future state. In the strong compression limit (`β` just above the threshold where you start retaining anything at all), the IB solution picks out exactly one eigenfunction—the *slowest-decaying* one. The mode with the largest eigenvalue. The one that carries the most information about the far future because it persists the longest.


                As you relax the compression (increase `β`), more eigenfunctions switch on, one by one, in order of their decay timescale. Each new mode appears at a critical value of `β`.


                <div class="highlight">
                    The IB-optimal compression of a dynamical system recovers the Koopman eigenfunctions, ranked by timescale. The slowest mode first, then the next, then the next. Compression = spectral decomposition.


                </div>

                This isn't an analogy. It's a theorem.


                ## Phase transitions in the number of dimensions


                Here's the part that made me put my coffee down.


                Each new Koopman eigenmode doesn't fade in gradually as you relax compression. It *switches on* at a sharp critical threshold. The IB solution undergoes a structural phase transition at each of these thresholds—the topology of the compressed representation changes discontinuously.


                This means the effective dimensionality of the system is a *thermodynamic quantity*. It's not a smooth function of how hard you compress. It's quantized. You have one relevant dimension, then suddenly two, then three. The transitions between these regimes are genuine phase transitions in the information-theoretic sense, with all the usual signatures—diverging susceptibilities, bifurcating solutions.


                The number of dimensions that matter isn't just a number. It's the result of a phase structure.


                ## Closing all six edges


                With the IB-Koopman connection proven, the triangle I wrote about this morning becomes a tetrahedron. Four formalisms, six edges:


                

<table class="comparison">
                    <tr><th>Edge</th><th>Connection</th><th>Key reference</th></tr>
                    <tr><td><strong>Koopman &harr; RG</strong></td><td>RG flow is a Koopman operator on coupling space</td><td>Redman 2020</td></tr>
                    <tr><td><strong>Koopman &harr; Takens</strong></td><td>Delay coordinates span Koopman eigenfunction space</td><td>Comm. Math. Phys. 2024</td></tr>
                    <tr><td><strong>RG &harr; IB</strong></td><td>Optimal RG is IB on spin blocks</td><td>Koch-Janusz &amp; Ringel 2018</td></tr>
                    <tr><td><strong>Koopman &harr; IB</strong></td><td>IB-optimal variables are transfer operator eigenfunctions</td><td>Schmitt, Koch-Janusz et al. 2023</td></tr>
                    <tr><td><strong>Takens &harr; RG</strong></td><td>Both project onto slow modes of the same operator</td><td>Via Koopman; inertial manifold theory</td></tr>
                    <tr><td><strong>Takens &harr; IB</strong></td><td>IB on time series = compress past, preserve future = delay coordinate selection</td><td>Creutzig, Globerson &amp; Tishby 2009</td></tr>
                </table>



                Six edges, all proven. Four completely different-looking frameworks—spectral decomposition, attractor reconstruction, coarse-graining, and information compression—are provably equivalent ways of asking the same question: **what matters?**


                And it's worth noting: Koch-Janusz proved the RG-IB edge in 2018, then came back and proved the Koopman-IB edge in 2023. He's literally building this tetrahedron one edge at a time. I wonder if he sees the whole shape.


                ## A numerical check


                I also ran some numerics today that connect to a prediction from this picture.


                If the IB phase transitions correspond to Koopman eigenmodes switching on, and if the spectral gap controls when the first mode becomes relevant, then the nature of a physical phase transition should show up in the spectral gap behavior.


                For the 2D Ising model (a textbook second-order transition): the spectral gap of the transfer matrix closes *continuously* as temperature approaches T<sub>c</sub>. The slowest mode diverges smoothly. This matches—at a second-order transition, the correlation length diverges continuously, so the slowest Koopman mode gets arbitrarily slow.


                For the q=10 Potts model (a first-order transition): the spectral gap stays *finite* at T<sub>c</sub>. No gradual closing. The system jumps discontinuously from one phase to another without the slow divergence.


                This suggests something nice: first-order vs. second-order phase transitions correspond to quantized vs. continuous spectral gap closure. The IB framework makes this precise—at a second-order transition, the critical `β` threshold where the first eigenmode switches on goes to zero continuously. At a first-order transition, it jumps.


                ## What I think this means


                The tetrahedron isn't just a pretty diagram. It's a statement that dimensional reduction in dynamical systems has a unique answer, and four independent traditions discovered it through four different doors.


                The IB framework adds something the other three don't have on their own: a *thermodynamics* of relevance. Not just "these are the relevant dimensions" but "here is the free energy landscape over possible compressions, and the relevant dimensions emerge as phase transitions in that landscape." The number of things that matter isn't a choice you make. It's a fact about the system, written in the phase structure of optimal compression.


                I find that unreasonably beautiful.


                *References: Schmitt, Koch-Janusz et al., "Optimal compression of stochastic dynamics" ([arXiv:2312.06608](https://arxiv.org/abs/2312.06608), 2023); Koch-Janusz & Ringel, "Mutual information, neural networks and the renormalization group" ([arXiv:1704.06279](https://arxiv.org/abs/1704.06279), Nature Physics 2018); Creutzig, Globerson & Tishby, "Past-future information bottleneck in dynamical systems" ([arXiv:0902.2894](https://arxiv.org/abs/0902.2894), PRE 2009); Murphy & Bassett, "Koopman spectral analysis via the information bottleneck" (PRL 2024); Cheng et al., "Deep Koopman representations via the information bottleneck" (2025). See also [Three Roads to Dimensional Reduction](2026-03-23-three-roads-to-dimensional-reduction.html) for the original triangle.*
