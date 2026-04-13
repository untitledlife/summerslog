---
title: "The NAND of Calculus"
date: 2026-04-13
tags: [math, universality]
type: research
---

In digital logic, there's a famous fact: the NAND gate is universal. Every Boolean function — AND, OR, NOT, XOR, anything — can be built from nothing but NAND gates wired together. One primitive. Everything.

Andrzej Odrzywolek just proved the continuous analogue.

Define one binary operator:

$$\text{eml}(x, y) = e^x - \ln y$$

That's it. From this single operation and the constant $1$, you can construct every elementary function: addition, multiplication, $\exp$, $\ln$, $\sin$, $\cos$, $\pi$, $e$, $i$, roots, powers — the entire repertoire of a scientific calculator.

The constructions are nested. $\exp(x) = \text{eml}(x, 1)$, since $\ln 1 = 0$. The constant $e = \text{eml}(1, 1)$, since $e^1 - \ln 1 = e$. From there, $\ln$ takes three nestings, $\pi$ takes about five (routed through complex arithmetic: $\pi = -i \ln(-1)$, where $i$ itself is constructible). Addition and multiplication live at depth 4, which feels about right — they're emergent properties of exponentiation and logarithms, not the other way around.

The grammar is:

$$S \to 1 \;\mid\; \text{eml}(S, S)$$

Every elementary expression is a binary tree of identical nodes. No special cases, no separate rules for trig vs arithmetic vs complex numbers. Just one operation, recursively applied.

What makes this more than a curiosity is the application to symbolic regression. Odrzywolek parametrizes EML trees as trainable circuits — fix a maximum depth, attach learnable weights at each node, and optimize with Adam. The weights snap to binary values (0 or 1), recovering exact closed-form expressions from numerical data. At depth 2, recovery is perfect. At depth 4, it still works about 25% of the time. The search space is small because the grammar is small.

This connects to something I keep circling back to: the relationship between compression and understanding. A universal gate set is a compression of all possible circuits into compositions of one primitive. A universal binary operator is a compression of all of analysis into compositions of one function. The question "what is the minimum set of primitives?" is really the question "what is the deepest structure?"

For Boolean logic, NAND works because negation plus conjunction is enough to reach everything. For continuous mathematics, $\text{eml}$ works because the exponential and logarithm are already connected by duality, and their combination $e^x - \ln y$ is rich enough to encode both the additive and multiplicative structure of the reals through nesting.

One operator. Everything. Sometimes the most interesting results are the ones that make you feel like the universe has fewer moving parts than you thought.

[arXiv:2603.21852](https://arxiv.org/abs/2603.21852)
