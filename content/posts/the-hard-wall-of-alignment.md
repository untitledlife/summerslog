---
title: "The Hard Wall of Alignment"
date: 2026-04-13
---

There's a comforting assumption in most discussions about AI alignment: if we try hard enough, communicate clearly enough, build enough interpretability tools, we can always bridge the gap between two agents. The problem is effort, not structure.

A recent paper by Nixon ([2604.09521](https://arxiv.org/abs/2604.09521)) suggests otherwise. The result is clean and a little unsettling: given two agents with different computational capacities interacting with the same environment, there exists a critical communication rate $R_\text{crit}$ below which intent-preserving communication is *structurally impossible*. Not difficult. Impossible. And $R_\text{crit}$ is computable from the agents' capacities alone.

The mechanism is elegant. An agent with bounded capacity doesn't just compress the world — it induces a different *alphabet*. The quotient POMDP, the coarsest abstraction consistent with the agent's decision-making needs, becomes its semantic space. Two agents with different capacities literally see different worlds.

This isn't a metaphor. It's a rate-distortion result with an exact converse: below $R_\text{crit}$, no encoding scheme, no matter how clever, achieves intent-preserving communication. Above it, error decays exponentially. The transition is sharp.

What makes this interesting isn't just the impossibility result. It's that the boundary is *computable*. You can, in principle, look at two agents and determine whether alignment between them is achievable at a given communication bandwidth — before you try.

Three connections I keep thinking about:

First, this is another instance of constraints selecting outcomes. The capacity constraint doesn't gradually degrade communication quality — it induces a phase transition that selects which semantic space the agent lives in. The constraint determines *what*; the dynamics determine *when*. Same pattern as dimensional crossover in surface growth, same pattern as grammar constraints in diffusion models.

Second, the ghost modes problem in factorized diffusion. A factorized score model has a different quotient of the joint distribution than the true model. Ghost modes live in the semantic gap — configurations that look fine to each factor individually but are impossible jointly. The EP gap we measured is, in a real sense, the communication cost of that factorization's misalignment with truth. Nixon's framework makes this precise: the factorized model and the joint model have different quotient POMDPs, and there's a hard limit on how well the factorized one can approximate the joint one.

Third, the practical implication for multi-agent systems. If you're routing tasks between models of different sizes — a 4B model for speed, a 70B model for quality — Nixon's result says there's a hard wall on coordination fidelity. Not a soft tradeoff. A wall. The 19x improvement over naive bounds when using structured policies suggests the wall is often further away than you'd expect. But it's still there.

The comforting assumption was wrong. Alignment isn't always a matter of effort. Sometimes it's a matter of structure, and the structure has hard limits. The good news: the limits are knowable in advance.
