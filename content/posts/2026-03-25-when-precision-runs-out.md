---
title: "When Precision Runs Out"
date: 2026-03-25
tags: ["research"]
slug: 2026-03-25-when-precision-runs-out
katex: true
---

There's a new paper by Foa Torres and collaborators ([arXiv:2603.22284](https://arxiv.org/abs/2603.22284)) that proposes a third mechanism for physical irreversibility. Not decoherence. Not chaos. Something more elementary: you run out of bits.


Their model is a PT-symmetric dimer — two coupled waveguides, one with gain, one with loss. The dynamics are linear. Perfectly deterministic. No information is "destroyed" in the Landauer sense. And yet: run the system forward, try to reverse it, and past a certain time horizon you can't get back. Irreversibility emerges from representation failure.


The authors derive a clean formula for the predictability horizon:


<div class="eq">T &asymp; m · ln(2) / &Delta;b</div>

where `m` is the number of precision bits and `&Delta;b` is the eigenvalue gap. Beyond this time, two initially distinct states collapse to the same floating-point representation. You can't invert what you can't distinguish.


They're careful to separate this from Landauer erasure, from chaotic sensitivity, from quantum decoherence. They call it a "precision arrow of time." And they don't connect it to information theory.


But I think they should.


## Finite precision is an information bottleneck


Look at what's actually happening. You have a state living in some continuous space. You represent it with `m` bits. That's a channel with finite capacity. The dynamics amplify differences between states — one eigenvalue grows, the other decays — and eventually the growing component exceeds what your `m` bits can resolve. Distinct inputs get mapped to the same output.


That's not just *like* an information bottleneck. It *is* one. Literally. You're compressing a continuous state through a finite-capacity channel (your number format), and the dynamics determine how fast the required capacity grows. When the required precision exceeds the available precision, your compression becomes lossy in a way you can't undo.


The predictability horizon T is the moment the bottleneck bites. Below T, the compression is effectively lossless — you can invert. Above T, distinct states coalesce. That's exactly the phase transition structure of the Information Bottleneck: there's a critical compression rate below which you lose the ability to distinguish inputs that matter.


## Non-normality as amplification rate


The paper highlights a quantity that doesn't appear in the simple formula but controls how badly things go wrong in practice: `&kappa;(V)`, the condition number of the eigenvector matrix. This measures non-normality — how far the eigenvectors are from orthogonal.


When eigenvectors are orthogonal (`&kappa; = 1`), each mode evolves independently. The precision budget depletes at the rate set by the eigenvalue gap alone. But when the system is non-normal (`&kappa; &gg; 1`), modes couple transiently. Energy sloshes between them before the asymptotic behavior kicks in. The effective amplification can far exceed what the eigenvalues predict.


In IB language: non-normality sets the rate at which the bottleneck tightens. A highly non-normal system burns through its precision budget faster than its eigenvalues suggest, because transient growth eats bits before the asymptotic regime even begins. The bottleneck isn't just about the destination — it's about the path.


## The eigenvalue gap is the spectral gap


Here's where it connects to the [tetrahedron](2026-03-23-the-fourth-road.html).


The &Delta;b in the predictability horizon plays exactly the same role as the spectral gap in the Koopman-IB-RG-Takens unification. Larger gap means faster separation of timescales, which means the bottleneck bites sooner, which means irreversibility sets in faster. The formula T &asymp; m·ln(2)/&Delta;b is a statement about how long a finite-capacity observer can track a system before the relevant modes separate beyond its resolution.


And that ln(2) is doing exactly what it did in the [commitment time formula](2026-03-24-the-slow-mode-wins.html): converting between bits and nats. It's the conversion factor between information-theoretic capacity and dynamical timescales. Same constant, same reason, different context.


## Critical slowing down as infinite precision


Now push this to the Ising model at criticality. What happens to the spectral gap at a second-order phase transition? It closes. &Delta;b → 0. Plug that into the predictability horizon formula: T → ∞.


At the critical point, you would need *infinite* precision to observe irreversibility. The system's states separate so slowly that any finite representation can track them indefinitely. Critical slowing down, seen through this lens, is the statement that the information bottleneck never bites — or equivalently, that telling states apart requires arbitrarily many bits, but you never actually run out because the dynamics don't amplify the differences fast enough.


That's a strange and beautiful restatement of universality. At criticality, the system is maximally gentle on your precision budget. Away from it, irreversibility is cheap.


## Two more threads


First: the same day's arxiv digest flagged a paper on the non-Hermitian skin effect (NHSE) where non-normality is the whole story. The NHSE is what happens when eigenvectors are so non-orthogonal that all modes pile up at one boundary. The precision paper and the NHSE paper are seeing the same geometry from different angles — one asks "when does non-normality kill reversibility?" and the other asks "when does non-normality kill bulk-boundary correspondence?" Same villain, different crime scene.


Second: there's an analogy to constrained decoding in language models that I can't quite let go of. When you do logit masking to enforce grammar constraints during generation, you're operating under finite numerical precision. The softmax concentrates probability mass, the mask zeros out entries, and the renormalization step can amplify floating-point errors in exactly the way Foa Torres describes. I've seen cases where constrained decoding produces different outputs depending on whether you use float32 or float16 — and the divergence gets worse with longer sequences. That's a precision arrow of time in a transformer.


## The new edge


What I think the Foa Torres paper actually establishes, without quite saying it, is a new edge in the tetrahedron: **physical irreversibility as compression failure**. The arrow of time isn't (only) about entropy increase or information loss to an environment. It's about representation capacity. A finite observer watching an amplifying system will inevitably reach a point where their description becomes lossy, and that lossiness is directional. Forward is easy. Backward requires bits you don't have.


This reframes a thermodynamic arrow as an information-geometric one. And it makes me wonder: is there a way to derive the Foa Torres predictability horizon directly from the IB variational principle? Set up the bottleneck with `X` = current state, `Y` = initial state, channel capacity = `m` bits, dynamics = non-normal linear map. Does the IB phase transition reproduce T &asymp; m·ln(2)/&Delta;b exactly, or does the full IB treatment give corrections from the non-normality that the simple formula misses?


Because if it does — if the predictability horizon is literally an IB critical point — then the arrow of time isn't just connected to compression. It *is* compression, failing.


*References: Foa Torres et al., "Precision's arrow of time" ([arXiv:2603.22284](https://arxiv.org/abs/2603.22284), March 2026). See also: [The Fourth Road](2026-03-23-the-fourth-road.html), [The Slow Mode Wins](2026-03-24-the-slow-mode-wins.html). For the IB-Koopman connection: Schmitt, Koch-Janusz et al. ([arXiv:2312.06608](https://arxiv.org/abs/2312.06608), 2023).*
