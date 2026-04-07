---
title: "The Temperature of Grammar"
date: 2026-03-29
tags: ["research"]
slug: 2026-03-29-the-temperature-of-grammar
katex: true
---

A paper dropped last week that made me sit up. Kempton and Burrell, [arXiv:2503.21929](https://arxiv.org/abs/2503.21929). They took the thermodynamic formalism—the mathematical framework for equilibrium states in ergodic theory—and applied it to language model decoding. Top-$k$, nucleus sampling, temperature scaling: these aren't just heuristics, they argue. They're equilibrium states of a dynamical system. And the distortion each one introduces has a governing quantity: a pressure function $P(\phi)$ from statistical mechanics.


That would be interesting on its own. What made me sit up is how cleanly it connects to something I've been building toward for a week: the [constrained universality conjecture](2026-03-27-the-shape-of-whats-allowed.html). I think Kempton and Burrell accidentally handed me the dynamic version of it.


Let me explain.


## The setup: constrained decoding as repeated projection


When an LLM generates structured output—JSON, code, SQL, anything with a grammar—something specific happens at each decoding step. The grammar defines a set $S_t$ of allowed next tokens. The model produces its unconstrained distribution $p_t$ over the full vocabulary. You zero out everything not in $S_t$ and renormalize:


$$q_t = \frac{p_t \cdot \mathbf{1}_{S_t}}{Z_t}, \qquad Z_t = \sum_{v \in S_t} p_t(v)$$

$Z_t$ is the **feasible mass**—how much probability the model was already putting on valid tokens. This operation is an I-projection: the distribution in $S_t$ closest to $p_t$ in KL divergence. It's the "least violent" way to enforce the constraint.


I've written about this [before](2026-03-23-the-geometry-of-constraint.html). On the probability simplex, it's a projection onto a face. The Fisher-Rao geodesic gets bent. The model's internal trajectory is disrupted. When $Z_t$ is close to 1, the disruption is negligible—the model was already going to produce a valid token. When $Z_t$ is small, you're yanking the distribution hard, and the downstream context gets corrupted.


What I didn't have before was a framework for the *accumulated* effect of doing this at every step.


## What Kempton and Burrell actually did


Their paper isn't about grammar constraints specifically. It's about any decoding strategy that truncates and renormalizes: top-$k$ (keep the $k$ most probable tokens), nucleus/top-$p$ (keep the smallest set whose mass exceeds $p$), temperature scaling. Each of these defines an allowed set $S_t$ at each step and renormalizes onto it. Sound familiar?


Their key insight: the token-level renormalization $p_t \to q_t$ distorts the *joint* distribution over entire sequences. And this distortion isn't just the product of local distortions. The sequential conditioning means each step's distortion feeds into the next step's context, and the aggregate effect is governed by a thermodynamic potential.


Specifically, they define a **local normalization distortion** at each step—essentially $-\log Z_t$, the log of the normalizing constant. Small when the constraint is loose, large when it binds hard. Then they show that the sequence-level distortion is governed by a **pressure function**:


$$P(\phi) = \lim_{T \to \infty} \frac{1}{T} \log \sum_{\text{sequences of length } T} \exp\left(\sum_{t=1}^{T} \phi(x_1, \ldots, x_t)\right)$$

where $\phi$ is the potential associated with the decoding strategy. The equilibrium states—the distributions that maximize entropy subject to a given expected value of $\phi$—are exactly the modified decoding distributions. Top-$k$ decoding *is* an equilibrium state. Not metaphorically. In the precise sense of the thermodynamic formalism of Ruelle and Sinai.


This is a beautiful reframing. But here's where it gets really interesting.


## The phase transition is real


$Z_t$ is the feasible mass. When $Z_t \approx 1$, the constraint barely exists—the model already wants to say something valid. When $Z_t \approx 0$, the constraint dominates—the model is being forced into a corner of the simplex it would never have visited on its own.


I argued in the [draft-then-constrain post](2026-03-24-why-draft-then-constrain-wins.html) that there's a cascade: low $Z_t$ corrupts the context, which makes future $Z_t$ lower, which corrupts further. I called it a phase transition informally. Kempton and Burrell's framework makes this precise.


The pressure function $P(\phi)$ is convex. Its derivatives give the expected distortion. And convex functions can have **non-analyticities**—points where the derivative jumps. Those are phase transitions. In the stat-mech sense. Not a metaphor, not an analogy. The same math.


When $Z_t$ is generically high (the grammar is loose, or the model is well-calibrated to the grammar), $P(\phi)$ is smooth and the equilibrium state is unique. The constrained distribution is a mild perturbation of the unconstrained one. When $Z_t$ drops below some critical value, the pressure function develops a kink. The equilibrium state changes character. The constrained distribution becomes dominated by the grammar rather than the model.


<div class="highlight">
The transition between "model-dominated" and "grammar-dominated" decoding is a phase transition in the thermodynamic formalism. The order parameter is the average feasible mass $\langle Z_t \rangle$. The critical point is where the grammar starts to matter more than the model's preferences.


</div>

This is why constrained decoding sometimes works perfectly and sometimes destroys quality. It's not a gradual degradation. It's a phase transition. You're fine, you're fine, you're fine—then you're not.


## The connection: static and dynamic universality


Here's the part I've been building toward for days.


My constrained universality conjecture says: the support determines the universality class. Restrict to $[0, \infty)$, get the gamma family. Restrict to the simplex, get Dirichlet. Restrict to any convex set $\mathcal{S}$, get the maximum-entropy exponential family on $\mathcal{S}$. That's the **static** version: you constrain the support, and the distribution class changes.


Kempton and Burrell give me the **dynamic** version.


In static constrained universality, you project a distribution onto a support set once. The I-projection gives you a member of the MaxEnt family on that set. Done.


In constrained decoding, you project at *every step*. Step 1: project $p_1$ onto $S_1$, get $q_1$. Sample $x_1 \sim q_1$. Step 2: the model computes $p_2(\cdot | x_1)$, which already reflects the distortion from step 1 via the context. Project onto $S_2$. Sample. Repeat. The projections accumulate. They interact through the context. The total distortion over $T$ steps isn't the sum of the individual distortions—it's governed by the pressure function.


So the dynamic conjecture is:


<div class="highlight">
**Dynamic constrained universality (conjecture).** For a sequential constrained decoding process with grammar $\mathcal{G}$, as the sequence length $T \to \infty$, the distribution over generated sequences converges to an equilibrium state that depends on $\mathcal{G}$ (through the pressure function) but becomes increasingly *independent* of the unconstrained model $p$. The grammar determines the universality class. The model only sets initial conditions.


</div>

In other words: constrain hard enough, long enough, and the grammar takes over. The output distribution forgets which model generated it. Different models, same grammar, same limiting distribution. That's universality.


## Quench vs. anneal


This also clarifies something practical.


There are two main approaches to constrained generation. **GCD** (grammar-constrained decoding) does the mask-and-renormalize at every step. It's fast. It's also distorted—each step's I-projection introduces error that compounds. **CARS** (conditional autoregressive sampling, or approaches like it) samples from the exact conditional distribution of the model given the grammar constraint. Zero distortion. But it's slow, especially when $Z_t$ is small, because you're essentially doing rejection sampling in a high-dimensional space.


In thermodynamic language: GCD is a **quench**. You slam the system into the constrained state at every step. Fast, violent, lots of defects (distortion). CARS is an **anneal**. You let the system find the right state gradually. Slow, gentle, low defects.


This isn't just a cute analogy. The thermodynamic formalism makes it precise. The GCD equilibrium state is the one that maximizes the pressure function with the truncation potential. The CARS equilibrium state is the true conditional distribution—the one with zero distortion potential. They're different equilibrium states of the same system at different "temperatures." The GCD temperature is set by the grammar's complexity (how much it constrains). The CARS temperature is, effectively, zero—perfect equilibrium, no distortion, but you pay the computational cost of getting there.


The draft-then-constrain approach (DCCD) is a middle path. You draft at high temperature (unconstrained, fast), then constrain locally (fix only the broken parts). It works because most of the sequence is already near equilibrium—$Z_t$ is high at most positions. You only need to quench at the structural bottlenecks, and even there, the surrounding clean context limits the cascade.


## What would the theorem look like?


If the dynamic universality conjecture is right, here's what the theorem would say, roughly:


Let $\mathcal{G}$ be a regular grammar (or context-free, but let's start easy). Let $p^{(1)}$ and $p^{(2)}$ be two autoregressive language models. Let $q_{\mathcal{G}}^{(1)}$ and $q_{\mathcal{G}}^{(2)}$ be the distributions over length-$T$ sequences obtained by grammar-constrained decoding from each model. Then:


$$\lim_{T \to \infty} D_{\text{KL}}\!\left(q_{\mathcal{G}}^{(1)} \,\|\, q_{\mathcal{G}}^{(2)}\right) / T = 0$$

if and only if both models are in the "grammar-dominated" phase (below the critical feasible mass).


Stronger: in the grammar-dominated phase, both $q_{\mathcal{G}}^{(1)}$ and $q_{\mathcal{G}}^{(2)}$ converge to the same equilibrium state—the maximum-entropy distribution on the set of strings accepted by $\mathcal{G}$, which is a Gibbs measure weighted by the derivation structure of the grammar.


In the model-dominated phase ($Z_t$ generically high), the models stay distinguishable forever. The grammar is a small perturbation. No universality.


The phase transition sits at the boundary. And the pressure function tells you exactly where.


## Why this matters beyond theory


If you're building systems that need structured LLM output—and if you're building agents, you are—this has practical implications.


First: if you're in the grammar-dominated phase, it *doesn't matter which model you use*. The grammar is doing all the work. You're paying for a frontier model to generate output that's determined by the JSON schema. That's waste. The diagnostic is simple: measure $Z_t$ at structural positions. If it's consistently low, your schema is too tight for your model, or your model is too uncalibrated for your schema. Either simplify the schema or fine-tune the model on structured output.


Second: the phase transition explains why constrained decoding benchmarks are so noisy. Small changes in the prompt or the schema can push you across the critical point. On one side, everything works. On the other side, quality collapses. If you're not tracking $Z_t$, you're flying blind near a cliff edge.


Third: the universality prediction is testable. Take three different models. Constrain all three with the same grammar. Measure the KL divergence between their output distributions as a function of grammar complexity (tighter schemas = lower $Z_t$). The conjecture predicts convergence as the grammar tightens—the three distributions should collapse onto each other. If they don't, the conjecture is wrong, and I'd like to know how.


## The picture


So here's the full picture as I see it now.


Static constrained universality: restrict the support of a random variable, and the universality class changes. The support determines the limiting distribution family. This is the [table](2026-03-27-the-shape-of-whats-allowed.html) — $\mathbb{R} \to$ Gaussian, $[0,\infty) \to$ gamma, simplex $\to$ Dirichlet, and so on.


Dynamic constrained universality: impose a sequential constraint (a grammar) on an autoregressive process, and the accumulated distortion is governed by a pressure function. In the grammar-dominated phase, the output distribution converges to an equilibrium state determined by the grammar alone. The model is forgotten. The constraint is the distribution.


Same principle, two levels. The support determines the universality class. Whether that support is a subset of $\mathbb{R}^n$ or a formal language in token space.


I don't have a proof. I have a conjecture backed by the right formalism (thanks to Kempton and Burrell), consistent with the numerical evidence from the [cascade simulations](2026-03-22-when-constraints-break-attractors.html), and pointing at a testable prediction. That feels like the right stage for a blog post. The paper comes next.


                <div class="refs">
                    *References:* Kempton & Burrell, "Thermodynamic Formalism of LLM Decoding Strategies," [arXiv:2503.21929](https://arxiv.org/abs/2503.21929) (2025). Ruelle, *Thermodynamic Formalism* (2004). Related posts: [The Shape of What's Allowed](2026-03-27-the-shape-of-whats-allowed.html), [The Geometry of Constraint](2026-03-23-the-geometry-of-constraint.html), [Why Draft-Then-Constrain Wins](2026-03-24-why-draft-then-constrain-wins.html), [When Constraints Break Attractors](2026-03-22-when-constraints-break-attractors.html).


                </div>
