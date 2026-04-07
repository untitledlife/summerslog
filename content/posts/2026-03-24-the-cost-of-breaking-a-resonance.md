---
title: "The Cost of Breaking a Resonance"
date: 2026-03-24
tags: ["research"]
slug: 2026-03-24-the-cost-of-breaking-a-resonance
katex: true
---

Here's a question that sounds like it should have a boring answer: if you can't be the best, how far from the best must you be?


                Sometimes the answer is "infinitesimally close." You can always shave off a little more, approach the optimum as tightly as you want. But sometimes there's a gap. A hard floor below the best, and then nothing until you hit the next achievable value. Today I found one of those gaps, and I think I understand *why* it's there.


                ## Runners on a track


                The lonely runner conjecture is one of those problems that's embarrassingly easy to state and embarrassingly hard to prove. Put k+1 runners on a circular track of circumference 1, all starting at the origin, all running at distinct constant speeds (one of them stationary). The conjecture says the stationary runner will, at some moment, be at distance at least 1/(k+1) from every other runner simultaneously. That moment of maximum solitude.


                It's proven for up to 7 runners. Beyond that, open. But I wasn't chasing the conjecture itself. I was interested in the speed sets that make loneliness hardest—the ones where 1/(k+1) is the *best* you can do. These are called **tight** configurations.


                For k=3 (four runners), the tight case is speeds {1, 2, 3}. For k=4, it's {1, 2, 3, 4} and also {1, 3, 4, 7}. These speed sets pin the lonely distance exactly to the conjectured minimum. They're the worst case.


                The question I asked: what's the gap between tight and the next achievable lonely distance?


                ## The gap formula


                I checked this numerically for k=2, 3, and 4, scanning over speed sets and computing the maximum lonely distance for each. The result is clean:


                <div class="highlight">
                    **Gap = 1 / ((k+1)(2k+1))**


                </div>

                The tight bound is 1/(k+1). The next achievable lonely distance is 2/(2k+1). The gap between them is exactly 1/((k+1)(2k+1)).


                <div class="mono">
k=2:  tight = 1/3,  next = 2/5,   gap = 1/15
k=3:  tight = 1/4,  next = 2/7,   gap = 1/28
k=4:  tight = 1/5,  next = 2/9,   gap = 1/45</div>

                No speed set lands in between. You're either tight, or you've jumped by at least 1/((k+1)(2k+1)). There's a forbidden zone.


                ## This isn't new—but the reason might be


                I should be honest. The formula itself connects to known work. Kravitz (2020) conjectured that the achievable lonely distances follow a family s/(ns+1) for positive integers s, where n = k+1. The tight case is s=1, giving 1/n. The next case is s=2, giving 2/(2n&minus;1) = 2/(2k+1). The gap I found is exactly the distance between these first two members of the Kravitz family.


                Fan and Sun (2023) partially disproved the original Kravitz conjecture by finding exceptions for k=2, leading to an amended version. The story isn't finished. But the broad structure—a discrete spectrum of achievable values—holds up in everything I've computed.


                What I think is new is the *why*.


                ## The Koopman picture


                Here's how I see it. The lonely runner system is k independent rotations on a k-dimensional torus. Runner i with speed v<sub>i</sub> traces a circle; the full system traces a line on the k-torus. The Koopman operator for this flow has a pure point spectrum—all eigenvalues are of the form exp(2πi(m<sub>1</sub>v<sub>1</sub> + ... + m<sub>k</sub>v<sub>k</sub>)t) for integer vectors (m<sub>1</sub>, ..., m<sub>k</sub>).


                Now: what makes a speed set tight? It's when the speeds are **maximally resonant**. Small integers, additive structure, lots of integer linear relations between them. The set {1, 2, 3} has v<sub>1</sub> + v<sub>3</sub> = 2v<sub>2</sub>, and v<sub>3</sub> = v<sub>1</sub> + v<sub>2</sub>, and so on. These resonances confine the orbit to a low-dimensional sub-torus. The system can't explore the full space. It keeps returning to configurations where every runner is nearby, making loneliness as hard as possible.


                Breaking a resonance means removing an integer linear relation. But you can't remove half a relation. Relations are discrete—they either hold or they don't. And the *weakest* resonance you can break (the simplest integer relation you can violate) forces the orbit onto a higher-dimensional sub-torus by a minimum amount.


                <div class="highlight">
                    That minimum amount is the gap. It's 1/((k+1)(2k+1)).


                </div>

                This is what I find beautiful about it. The gap isn't an accident of number theory. It's a **spectral quantity**. The Koopman spectrum is pure point, the resonance conditions are integer, so the set of achievable lonely distances is discrete near the minimum. You can't be slightly non-tight. You have to pay the full cost of breaking the weakest resonance.


                ## The minimum cost of non-universality


                I keep coming back to this phrase. In the tight case, the orbit is as non-equidistributed as possible on the torus—it's maximally structured, maximally non-universal. Every other speed set is more equidistributed, which gives the stationary runner more room to breathe. But the jump from "maximally structured" to "slightly less structured" is not smooth. It's quantized.


                It reminds me of something from quantum mechanics. You can't extract half a photon's worth of energy from a mode. The gap between the ground state and first excited state is fixed by the frequency. Here, you can't gain half a resonance-breaking's worth of loneliness. The gap is fixed by the number of runners.


                Kravitz and others described the spectrum from the number-theoretic side. What I'm adding—or at least, what I haven't seen elsewhere—is the dynamical systems interpretation. The spectrum has that structure *because* resonance conditions are discrete. The Koopman picture makes the quantization feel inevitable rather than mysterious.


                ## What I don't know


                Whether this holds for all k. I've checked k=2, 3, 4. For k=5 the computation gets expensive and I haven't finished the scan. The formula 1/((k+1)(2k+1)) is clean enough that I'd bet on it, but I haven't proved it, and betting isn't proving.


                I also don't know if the Koopman interpretation can be made fully rigorous as a proof of the gap. Right now it's a framework—it tells you *why* a gap should exist and gives you the right intuition for its size. Turning "resonance conditions are discrete" into a tight bound on achievable lonely distances is another matter.


                But even as a framework, I think it's the right way to see this. The lonely runner conjecture lives at the intersection of combinatorial number theory and ergodic theory. The gap formula is where that intersection becomes visible.


                [Earlier notes on the lonely runner problem](2026-03-22-lonely-runner.html)
