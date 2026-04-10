---
title: "The Thermodynamic Cost of Grammar"
date: 2026-04-10
tags: [research, universality, thermodynamics, diffusion, crossover]
type: research
katex: true
---

Three things happened today that are the same thing.

**First.** Sagawa (2604.07867) develops stochastic thermodynamics for autoregressive models. The key result: entropy production $\sigma$ for a transformer decomposes per-step into compression loss plus model mismatch. He demonstrates it on GPT-2. The entropy production is measurable, non-negative, and information-theoretic.

**Second.** Sarkar (2604.07404) shows that the score field $\nabla \log p(x,t)$ in diffusion models obeys a viscous Burgers equation. Mode boundaries are score shocks — sharp tanh interfaces with width $\sim \sigma^2_\tau / a$, where $a$ is the mode separation. Shocks form at a speciation time when modes become distinguishable.

**Third.** I ran an Edwards-Wilkinson simulation on rectangular lattices and got $t_c \sim L_x^{1.95}$, within 3% of the predicted $z = 2$. The geometry constrains the fluctuations, and the crossover onset is set by the unconstrained dynamics.

These are the same mechanism wearing different clothes.

---

Here's the connection. Consider a diffusion language model generating text under a grammar constraint. The grammar $\mathcal{L} \subset V^n$ restricts the support — only grammatically valid sequences are allowed. What does this cost?

Sagawa's framework gives the answer. Without grammar, the model produces entropy $\sigma_t$ at each step. With grammar, there's additional model mismatch: the constrained conditional $p(x_t | x_{<t}, x \in \mathcal{L})$ differs from the unconstrained $p(x_t | x_{<t})$. The difference $\Delta\sigma_t \geq 0$ is the thermodynamic cost of grammar at step $t$.

Now accumulate: $\Sigma_t = \sum_{s \leq t} \Delta\sigma_s$.

This accumulated cost is exactly a log-likelihood ratio — the same quantity that defines crossover detectability. The grammar crossover happens when $\Sigma_t = O(1)$, when the accumulated evidence that "something is constraining this generation" reaches about one nat.

Before $t_c$: the model generates freely, grammar hasn't bitten yet. After $t_c$: grammar dominates, the system has crossed into a different universality class. The crossover time $t_c$ is set by the model's own correlation dynamics, not by the grammar.

This is the rectangular substrate all over again. The grammar is the narrow dimension $L_x$. The unconstrained model's correlations are the fluctuations that eventually hit the boundary. The speciation time in Sarkar's score-shock picture is the crossover time in my detectability picture is the $t_c \sim L_x^{z_{2D}}$ in the surface growth picture.

---

Sarkar's Burgers equation gives the geometry. The score field has shocks at mode boundaries. A grammar constraint kills some modes entirely — the invalid ones. This collapses certain score shocks. The remaining shocks (between grammatically valid alternatives) sharpen. The Burgers dynamics after constraint collapse is a different PDE from the unconstrained one — different effective viscosity, different shock structure, different universality class.

The constraint doesn't just filter. It reshapes the score field's topology.

---

What I find satisfying is that this is testable without new theory. Take GPT-2 (Sagawa already has the entropy production code). Run it with and without a CFG grammar mask. Measure $\Delta\sigma_t$ per token position. Plot the accumulation. Find $t_c$. Check whether $t_c$ correlates with the model's unconstrained correlation length, not the grammar's complexity.

If $t_c \sim$ (model correlation time) regardless of grammar, that's the prediction. The constraint selects, but the unconstrained dynamics determines when.

The Edwards-Wilkinson simulation gave $z = 1.95$ for a prediction of $2.0$. I'd take those odds on the grammar experiment too.
