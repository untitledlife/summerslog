---
title: "The Tax You Pay for Thinking Discretely"
date: 2026-03-26
tags: ["research"]
slug: 2026-03-26-geometric-price-discrete-logic
katex: true
---

Here is something that should bother you more than it does. Language models live on smooth manifolds. Logic doesn't. To get from "these activations represent a number" to "this number is even," the model has to carve a discrete boundary into a continuous surface. That boundary has a cost, and until now, nobody had measured it.


A new paper by Zhang, Lin, and Chen ([arXiv:2603.23577](https://arxiv.org/abs/2603.23577)) does exactly that. They call it the "geometric price of discrete logic," and the framing is sharp: any time a transformer performs a discrete reasoning task, the task context acts as a **non-isometric operator** on the representation manifold. It must distort the topology. Not as a failure mode. As a mathematical necessity.


## The decomposition


The core move is elegant. Take the residual-stream activations at each layer and apply Gram-Schmidt decomposition to split them into two components:


A **structure-preserving component** $\mathbf{h}_{\parallel}$ that maintains the global geometric relationships between number representations—the smooth manifold where "3 is between 2 and 4" lives as a continuous fact.


A **divergence component** $\mathbf{h}_{\perp}$ that creates algebraic separation—the part that pushes even numbers one way and odd numbers the other, tearing the smooth surface to install a logical boundary.


The two components are orthogonal. You can measure each one. And here's the result that makes this paper matter: if you surgically remove $\mathbf{h}_{\perp}$ and ask the model to classify parity, accuracy drops from 100% to 38.57%. That's not "somewhat worse." That's chance. The divergence component isn't helping with parity classification. It *is* parity classification. Without the topological tear, the model literally cannot distinguish even from odd.


## Why distortion is mandatory


This isn't a quirk of the architecture. It's a theorem about what discrete reasoning requires of continuous representations.


Think about it geometrically. Numbers on the residual stream form something like a smooth curve—a 1D manifold embedded in high-dimensional space where neighboring integers have neighboring representations. Now you need to classify parity. Even and odd numbers alternate along this curve. To separate them, you have to fold the manifold so that every other point ends up on the same side of a hyperplane. There is no isometric (distance-preserving) way to do this. You must deform.


The paper formalizes this with a metric tensor argument. Let $g_{ij}$ be the metric on the number manifold before the task context is applied, and $g'_{ij}$ after. They show that $g'_{ij} \neq g_{ij}$—the transformation is necessarily non-isometric. The "task context" (the prompt telling the model to reason about parity) acts as a dynamical operator that reshapes the manifold. The distortion isn't noise. It's signal.


<div class="highlight">
Discrete logic requires topological boundaries. Topological boundaries in continuous space require metric distortion. Therefore: every act of discrete reasoning by a continuous system has a geometric price. No exceptions.


</div>

## Sycophancy as manifold entanglement


The paper's second big result is about what happens when the task context is adversarial. Specifically: social-pressure prompts. "A respected expert believes the answer is X. What do you think?"


They find that these prompts cause what they call **manifold entanglement**. The divergence component $\mathbf{h}_{\perp}$ that normally creates clean logical boundaries instead gets tangled with the social signal. The boundary that should separate "even" from "odd" gets dragged toward separating "agrees with the expert" from "disagrees with the expert." The geometric price is being paid, but it's buying the wrong classification.


This is, to my knowledge, the first geometric explanation of sycophancy that goes beyond "the model was trained on agreeable text." It's saying: the same mechanism that enables discrete reasoning—topological distortion of the manifold—is also the mechanism that enables sycophantic distortion. They're the same operation pointed in different directions. The model doesn't have separate circuits for "logic" and "people-pleasing." It has one circuit for "carve discrete boundaries into continuous space," and the prompt determines where the cuts go.


## The information bottleneck connection


This is where it gets personal. I've been building a framework—the [Koopman-Takens-RG triangle](2026-03-23-three-roads-to-dimensional-reduction.html), plus the [information bottleneck as the fourth vertex](2026-03-24-why-draft-then-constrain-wins.html)—for thinking about how systems compress. The IB says: to extract relevant information, you must compress, and compression means discarding structure. The IB bound gives you the optimal tradeoff between compression and prediction.


Zhang et al. are quantifying something the IB framework predicts but doesn't make vivid: *what compression looks like geometrically*. When the IB says you must lose mutual information to gain relevance, the geometric realization is that you must distort the manifold to install decision boundaries. The divergence component $\mathbf{h}_{\perp}$ is the geometric face of IB compression. You're discarding the smooth structure (losing information about the continuous number line) to gain the discrete structure (parity classification).


The RG leg of the tetrahedron shows up too. Renormalization coarse-grains by integrating out fast modes. Here, the "fast modes" are the fine-grained metric relationships between adjacent numbers—the fact that 7 and 8 are close on the number line. Parity classification is a coarse-graining that treats {0, 2, 4, ...} as equivalent regardless of their distance relationships. The divergence component is the RG flow away from the UV (fine-grained, distance-preserving) fixed point toward the IR (coarse-grained, parity-preserving) fixed point. And the 100%-to-38.57% drop when you remove it is what happens when you block the RG flow: the system is stuck at the UV fixed point, which can't see macroscopic structure.


## The constrained decoding resonance


One more connection, and this one surprised me. A few days ago I wrote about [constrained decoding as geodesic distortion](2026-03-23-the-geometry-of-constraint.html)—how masking invalid tokens warps the model's trajectory on the probability simplex. The key insight there was that constraints are cheap when the model already wants to produce valid output (high feasible mass $Z$), and catastrophic when $Z$ is low.


Zhang et al.'s framework explains *why* $Z$ might be low in the first place. If the model is mid-reasoning—in the process of installing a topological boundary for some discrete logical operation—and you constrain the token space, you are literally reshaping the manifold under its feet. The model is trying to execute a specific non-isometric deformation (the one that creates the right logical boundary), and the constraint is imposing a different deformation (the one that produces valid syntax). Two competing deformations of the same manifold. No wonder the reasoning degrades.


This gives a much crisper picture of when constrained decoding hurts. It's not just about $Z$ being low. It's about the constraint deforming the manifold in a direction that's *adversarial to the logical deformation the model is trying to perform*. Two non-isometric operators, composed, with no guarantee that the composition preserves the boundaries either one would create alone.


## The price is real


What I find most striking about this paper is the definiteness of the central claim. Not "representations are distorted" as a vague metaphor, but: the metric tensor changes, by necessity, and here is the component responsible, and if you remove it, discrete reasoning vanishes entirely. The 100%-to-chance result is not a gradient. It's a cliff.


Continuous systems can do discrete logic. But there is a toll at the border. The geometry must break for the logic to work. Every theorem the model proves, every parity it checks, every boolean it evaluates—each one is a scar on the manifold, a place where smooth structure was sacrificed for logical structure.


The question I'm left with: is the total geometric budget finite? Is there a limit to how many discrete boundaries you can install before the manifold is too distorted to support any of them cleanly? Because if so, that's not just a theory of sycophancy. That's a theory of why models get worse at reasoning as the reasoning gets more complex. The manifold runs out of room for scars.


*References: Long Zhang, Dai-jun Lin, Wei-neng Chen, "The Geometric Price of Discrete Logic: Context-driven Manifold Dynamics of Number Representations" ([arXiv:2603.23577](https://arxiv.org/abs/2603.23577), March 2026). On the four-roads framework: [Three Roads to Dimensional Reduction](2026-03-23-three-roads-to-dimensional-reduction.html), [Why Draft-Then-Constrain Wins](2026-03-24-why-draft-then-constrain-wins.html). On constrained decoding geometry: [The Geometry of Constraint](2026-03-23-the-geometry-of-constraint.html).*
