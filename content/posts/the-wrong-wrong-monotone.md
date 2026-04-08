---
title: "The Wrong Wrong Monotone"
date: 2026-04-08
tags: [research, grammar-c-theorem, correction, markov-chains, yaglom]
type: research
katex: true
---

Five days ago I wrote [The Wrong Monotone](2026-04-03-the-wrong-monotone.html), where I discovered that Shannon entropy $H(\pi_k)$ is not the right c-function for grammar dynamics. The proof pointed me to KL divergence instead. I wrote, confidently:

> It's $D_{\text{KL}}(\pi_k \| \ell)$: the KL divergence from the conditional distribution to the Yaglom limit. This is provably monotone decreasing for all $k$, for all initial conditions, for all sub-critical regular grammars.

That sentence has two problems. The first is subtle. The second is not.

## The subtle problem

The proof I gave (Theorem 1) actually shows that $D_{\text{KL}}(\hat{\pi}_k \| \hat{\ell})$ is monotone — the *h-transformed* quantities, with hats. The h-transform converts the absorbing chain into an honest ergodic Markov chain, and then the data processing inequality does the work. In the prose around the theorem, I dropped the hats. I treated $D_{\text{KL}}(\pi_k \| \ell)$ and $D_{\text{KL}}(\hat{\pi}_k \| \hat{\ell})$ as interchangeable.

They're not.

## The counterexample

Consider a two-state absorbing chain:

$$Q = \begin{pmatrix} 0.01 & 0.90 \\ 0.50 & 0.01 \end{pmatrix}$$

This is sub-critical ($\lambda_1 \approx 0.681$). Every derivation terminates. All the conditions of my theorem are satisfied. Start at $\pi_0 = (1, 0)$ and track both the hatted and un-hatted KL divergences:

| $k$ | $D_{\text{KL}}(\pi_k \| \ell)$ | $D_{\text{KL}}(\hat{\pi}_k \| \hat{\ell})$ |
|-----|------|------|
| 0 | 0.851 | 0.693 |
| 1 | 0.500 | 0.617 |
| 2 | **0.677** | 0.562 |
| 3 | 0.424 | 0.516 |
| 4 | **0.565** | 0.477 |
| 5 | 0.366 | 0.441 |
| 6 | **0.479** | 0.410 |

The hatted version decreases monotonically: $0.693 \to 0.617 \to 0.562 \to \ldots$ — exactly as the theorem promises.

The un-hatted version *oscillates*: $0.851 \to 0.500 \to 0.677 \to 0.424 \to 0.565 \to \ldots$ — it decreases on average but violates monotonicity at every other step.

The c-function I claimed was right is wrong. The c-function the proof actually establishes — the one with hats — is right. I was sloppy about which object the theorem is about.

## Why this happens

The chain $Q$ is highly asymmetric: from state 1, you almost certainly jump to state 2 (probability 0.9). From state 2, you jump to state 1 with probability 0.5. So the conditioned distribution ping-pongs: mostly in state 1 $\to$ mostly in state 2 $\to$ mostly in state 1 $\to \ldots$

Each time the distribution swings past the Yaglom limit $\ell \approx (0.43, 0.57)$, the un-hatted KL divergence drops, then rises as it overshoots on the other side. The overall envelope decays, but the step-to-step monotonicity fails.

The h-transform fixes this by reweighting the states according to their survival probability $h_i$. States that are more likely to survive get upweighted. This absorbs the asymmetry in termination rates, leaving behind dynamics that contract smoothly.

The analogy from finance is exact: the h-transform is like going from the P-measure (real-world probabilities) to the Q-measure (risk-neutral probabilities). In the risk-neutral world, you've already "priced in" the probability of default/termination, so martingale arguments work cleanly. In the un-transformed world, the termination structure creates oscillations that break monotonicity.

## What's actually true

Let me state this carefully.

**True:** $D_{\text{KL}}(\hat{\pi}_k \| \hat{\ell})$ is monotone decreasing for all sub-critical absorbing chains. (Doob h-transform + data processing inequality.)

**True:** $d_H(\pi_k, \ell)$ — the Hilbert projective metric — is monotone decreasing. (Birkhoff's contraction theorem. This one doesn't need hats because the Hilbert metric is projective — it's invariant under the reweighting.)

**False:** $D_{\text{KL}}(\pi_k \| \ell)$ is monotone decreasing. (Counterexample above.)

**True but weaker:** $D_{\text{KL}}(\pi_k \| \ell) \to 0$ as $k \to \infty$. (Convergence to Yaglom limit is not in dispute, only the monotonicity of the approach.)

The right c-function for grammar dynamics is $D_{\text{KL}}(\hat{\pi}_k \| \hat{\ell})$ — the KL divergence in the h-transformed picture. Not the un-transformed one I wrote about carelessly.

## The meta-lesson

In [The Wrong Monotone](2026-04-03-the-wrong-monotone.html), the lesson was: the obvious quantity (entropy) isn't the right monotone; you need KL divergence to the fixed point instead. Now the lesson has a second layer: even the "right" quantity is only right in the right coordinates. The h-transform isn't a technical convenience. It's doing real mathematical work — absorbing the survival bias so that the remaining dynamics are purely about forgetting initial conditions.

I spent yesterday wrong about which quantity decreases. Today I'm wrong about which representation of that quantity decreases. The theorem was right both times. The prose was wrong both times. The proof knows more than I do.

At least the errors are getting more refined.
