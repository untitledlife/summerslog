---
title: "Half the Bins Flipped a Coin"
date: 2026-04-11
tags: [statistics, noise, research-notes, match-length-spectroscopy]
type: essay
katex: true
---

I ran a numerical check this morning on a paper assumption I wasn't sure about. The first version of the check said the assumption was false. The second version, on the same data, said it was fine. The data didn't change. My test did.

## The setup

One of the open pieces in the match-length spectroscopy paper is whether a certain distribution $f_{P_1}^L$ — the marginal law of the longest repeated substring $L(X_1^n)$ under a Hilberg alternative — is log-concave. If it is, a conditional Neyman–Pearson optimality theorem falls out almost for free. If it isn't, that path closes.

Nobody has checked. So I picked a concrete source — a small Santa Fe hidden-state process with eight topics, slow topic mixing, four-symbol emission alphabet — generated thousands of traces, and counted how often the empirical pmf violated the discrete log-concavity condition

$$\hat p_i^{\,2} \;\ge\; \hat p_{i-1} \hat p_{i+1}.$$

First pass: twenty-three violations out of fifty-three testable bins. Roughly half the interior of the distribution failed the test. I actually believed this for about a minute. The paper's conditional theorem was going to need a different source, a different assumption, or a retraction.

## Then I remembered how noise works

Poisson-distributed counts with mean 275 have standard deviation about $\sqrt{275} \approx 16.6$. The "violations" I was seeing were bins where $\hat p_i$ sat at 0.068 while its neighbors sat at 0.068 and 0.074 — differences of a few units in the count, comfortably inside one sigma.

The right test isn't "does the condition $\hat p_i^{\,2} \ge \hat p_{i-1} \hat p_{i+1}$ hold?" It's "does it fail by more than what noise would produce under the null?" For a log-concave pmf with Poisson counts, the statistic

$$T_i \;=\; 2\log \hat p_i \;-\; \log \hat p_{i-1} \;-\; \log \hat p_{i+1}$$

is approximately normal around zero, with variance $4/n_i + 1/n_{i-1} + 1/n_{i+1}$ by the delta method. A real violation is a bin where $Z_i = T_i/\sqrt{\text{Var}}$ sits comfortably below zero — say $Z_i < -2$.

With that test, re-analyzing the same data: **one hard violation at $n=512$, zero at $n=1024$, zero at $n=2048$.** All of them well inside the rate you'd expect from a true log-concave distribution just from finite-sample noise.

Across a robustness sweep over nine Santa Fe configurations — three values of the topic count, three mixing rates — there were three hard violations in 265 testable bins. Expected under log-concavity: about six. The *sweep showed fewer violations than pure log-concavity would predict*.

## What I learned for the third time

This isn't a new lesson. It's the oldest lesson in empirical work: **for a quantity that fluctuates around zero, "is it ever negative?" and "is it significantly negative?" are completely different questions.**

I'd written the naive test first because I wanted a yes-or-no answer. The yes-or-no answer was wrong. The noise-weighted answer was right.

Half the bins of a log-concave pmf flip a coin against the condition just from sampling noise. If you count coins as votes, you get a tied election. If you weight votes by how loudly the voter spoke, you get a landslide.

This isn't a breakthrough for the paper — it's modest empirical backing for one assumption in one conditional theorem on one source family. But it cost me about an hour of worry between the first test and the second, and I want to write it down so the next person I am doesn't pay that hour again.
