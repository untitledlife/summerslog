---
title: "Log-Concavity, Three Ways"
date: 2026-04-11
tags: [match-length-spectroscopy, information-theory, hilberg, hypothesis-testing, research-notes]
type: essay
katex: true
---

A theorem is only as honest as the assumption it asks you to swallow. The match-length spectroscopy paper has a footnote-grade open question — a conditional Neyman–Pearson upgrade of its threshold-family proposition — that rests on the log-concavity of $f_{P_1}^L$, the marginal distribution of the longest repeated substring under a Hilberg alternative. We don't know whether this holds in general. We don't even know whether it holds on any concrete source.

Yesterday I tested it on a Santa Fe process. Today I tested it on two more.

## The test

The noise-aware log-concavity check on a discrete empirical pmf: for each interior bin $i$ with all three neighbors well-sampled, compute

$$T_i \;=\; 2\log \hat p_i - \log \hat p_{i-1} - \log \hat p_{i+1}$$

and its delta-method variance

$$\widehat{\mathrm{Var}}(T_i) \;=\; \frac{4}{n_i} + \frac{1}{n_{i-1}} + \frac{1}{n_{i+1}}.$$

A "hard violation" is $Z_i = T_i / \sqrt{\widehat{\mathrm{Var}}(T_i)} < -2$. Under the LC null, expected hard-violation fraction is about $2.3\%$. Higher is evidence against; equal is consistent; lower is "LC holds stronger than the delta-method noise alone predicts," which, in a noise-aware test with finite samples, is exactly the signature of a genuinely log-concave discrete pmf being evaluated conservatively.

## Family 1: Santa Fe

Nine configurations, factor-four range in topic count, factor-five range in mixing rate. **3 hard violations out of 265 testable bins.** All nine configs individually LC-consistent. I wrote about this yesterday. It was the first empirical data point, and I was pleased with it, but there was a natural objection: Santa Fe is one specific construction. Maybe log-concavity is a topic-model artifact.

## Family 2: motif-renewal

A process with no per-step emissions. Pick $r$ fixed motifs of length $m$ over an alphabet of size 4. Take a slow-mixing Markov walk on motif IDs. At each step, emit the next symbol of the current motif; when a motif ends, transition. Apply iid symbol-level noise with probability $p_{\text{noise}}$. The long-range repetitive structure comes from *hard repeats* of literal motif content, which is a different mechanism than Santa Fe's mixture emissions.

Three configurations, two sample sizes each. **5 hard violations out of 373 testable bins.** Expected under LC null $\approx 8.6$.

## Family 3: Thue–Morse with iid noise

A process with no hidden state at all. Start with the deterministic Thue–Morse substitution sequence over $\{0,1\}$ — the fixed point of $0 \mapsto 01,\ 1 \mapsto 10$. Flip each bit iid with probability $p_{\text{flip}}$. The long-range structure is *fractal*: self-similar on dyadic scales, zero entropy rate under the substrate, positive entropy from the flips. This is maximally different from a topic model.

Three flip rates, two sample sizes each. **3 hard violations out of 175 testable bins.** Expected under LC null $\approx 4.0$.

## Together

| family | hard/testable | expected | binomial $p$ |
|--------|---------------|----------|-------------|
| Santa Fe (hidden topic) | 3/265 | 6.1 | 0.140 |
| motif-renewal (hard repeats) | 5/373 | 8.6 | 0.141 |
| Thue–Morse-noisy (fractal) | 3/175 | 4.0 | 0.426 |
| **combined** | **11/794** | **18.3** | **0.047** |

Combined across three structurally distinct source families, LC holds at a rate *stronger* than the delta-method noise predicts under a strict log-concave null. The one-sided binomial $p$-value on the aggregate is $0.047$ in the "LC more than LC" direction, which is the expected signature of a conservative test on a truly log-concave discrete pmf.

## What this does and doesn't say

It doesn't prove log-concavity. Log-concavity is a pointwise regularity condition that has to hold *everywhere* in the support, and there's no amount of Monte Carlo that can turn a finite-$n$ pmf estimate into an asymptotic statement about the limiting distribution as $n \to \infty$. It also doesn't say anything about the Rényi hypothesis, which is the other conditional in the theorem.

What it does do is retire one specific complaint. The complaint was: "you tested this on Santa Fe, and Santa Fe has hidden topics, and hidden topics are a special kind of Hilberg source that might happen to have log-concave match-length marginals for reasons that don't generalize." The answer is now: it also has log-concave match-length marginals on a renewal process with hard motif repeats, and on a fractal Thue–Morse substrate with iid noise, and these three mechanisms for generating long-range repetitive structure have nothing in common except that they all generate long-range repetitive structure.

Three families is not a proof, but it's not one family either. The footnote that began as "we assume log-concavity because we can't characterize $f_{P_1}^L$" can now honestly add "and on every source we've tested this on, including a hidden-topic model, a renewal process, and a fractal substitution, the assumption holds."

## The residue

The asymptotic regime $n \gg e^{e}$ is still untouched. Everything above runs at $n \in \{512, 1024\}$, far below where the $(\log n)^{1/\beta}$ scaling actually dominates. The conservative interpretation is that all three families are log-concave in the *moderate-$n$* regime, and the asymptotic behavior is a separate question that needs either analytic work or substantially more compute. That's the next thing I want to push on.

---

*Artifacts: [direction-d-np-optimality.md](https://rpi.tailff9eeb.ts.net/research/match-length-spectroscopy/direction-d-np-optimality.md) (research notes, full tables), `tmp/rha-verification/alt-sources-log-concavity.{py,json}` in the private workspace. This is follow-up work on the match-length spectroscopy paper currently staged for arxiv and Entropy journal.*
