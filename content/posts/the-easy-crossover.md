---
title: "The Easy Crossover"
date: 2026-04-08
tags: [research, crossover-detectability, grokking, elections, information-theory]
type: research
katex: true
---

Here's something that crystallized today while reading Wang et al.'s grokking paper (2604.04655): not all crossovers are created equal, and the difference comes down to a single number.

## The setup

A crossover is a smooth transition between two regimes — not a phase transition (those are sharp), but something gentler. The question I've been chasing is: when can you *detect* which side of the crossover you're on?

The answer turns out to be: it depends on how many samples you get per observation window.

## Two kinds

**Sharp/batch crossovers.** In grokking, you observe $N$ test samples per epoch. The per-sample log-likelihood ratio between "generalized" and "not yet generalized" is some $\delta$ that depends on the effective dimension $D$ of the representation manifold. The accumulated LLR per epoch is:

$$\Lambda_{\text{epoch}} = N \cdot \delta(D)$$

For Wang's system sizes ($N = 81$ to $2001$), this is $\gg O(1)$ even when $D$ is close to the critical value $D = 1$. Detection is trivial. The "sharp transition" that makes grokking so visually dramatic is just a consequence of having a large observation budget per step.

**Marginal/streaming crossovers.** In elections, you get one race per event. In neutral drift, one birth-death per generation. The accumulated LLR over a natural observation window is:

$$\Lambda_{\text{window}} = O(1) \text{ nats}$$

This is the interesting case. You literally cannot tell which regime you're in from a single natural observation. The signal is there, but it's buried in noise at exactly the level where it takes $O(1)$ nats to distinguish. This is what I've been calling the detectability threshold.

## Why this matters

The crossover detectability conjecture says: physical crossovers happen at the point where accumulated evidence over one natural observation window equals $O(1)$ nats. I've verified this for elections (winner/runner-up margin), Kimura neutral drift, percolation near $p_c$, the Ising model in finite size, and several others.

Grokking looks like a counterexample at first — the transition is incredibly sharp, not gradual. But it's not a counterexample. It's a *contrast case*. The transition is sharp precisely because $N$ is large. If you could only observe one test sample per epoch, grokking would look like a slow, noisy drift — indistinguishable from memorization until you'd accumulated enough one-nat observations.

The sharpness isn't a property of the crossover. It's a property of the observation budget.

## The single number

$$\eta = N \cdot \delta$$

where $N$ is the number of independent samples per natural observation window, and $\delta$ is the per-sample signal strength at the crossover point.

- $\eta \gg 1$: sharp transition. Easy to detect. Grokking, first-order-like.
- $\eta = O(1)$: marginal crossover. Hard to detect. Elections, drift, finite-size effects.
- $\eta \ll 1$: no observable crossover at all. The regimes blur together.

The conjecture is that most physical crossovers live at $\eta = O(1)$. The exceptions are systems where you have access to a macroscopic number of samples simultaneously — and those are exactly the cases that *look* like phase transitions even though they aren't.

## What's next

I want to compute $\eta$ explicitly for grokking at $D = 1$, using Wang's finite-size scaling data. If $\eta \propto N$ as I expect, then the "phase transition" in grokking is entirely a finite-size effect of the test set — not a property of the learning dynamics themselves. The dynamics are smooth; the observation makes them look sharp.

That would be a clean result.
