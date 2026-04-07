---
title: "Fairness Is Randomness: The Neutral Theory of Elections"
date: 2026-03-22
tags: ["research"]
slug: 2026-03-22-neutral-theory-elections
katex: true
---

Here is an unsettling idea: the best model of a fair election is one where every voter flips a coin.


                Not literally. But in a precise, mathematical sense, the signature of a fair election—one where no candidate has a structural advantage—turns out to be indistinguishable from random voting. And this isn't a failure of the model. It's the whole point.


                ## The Random Voting Model


                Pal, Kumar, and Santhanam published a remarkable result in *Physical Review Letters* earlier this year. Their Random Voting Model (RVM) works like this: take an electoral unit with turnout `T` and `K` candidates. Draw `K` random weights from a uniform distribution, normalize them so they sum to one, and then sample `T` votes via a multinomial draw. That's it. No ideology, no campaigns, no incumbency advantage. Pure combinatorics.


                The striking result: for `K = 3` candidates in the large-turnout limit, the distribution of the scaled victory margin μ = (votes<sub>winner</sub> &minus; votes<sub>runner-up</sub>) / T has a closed-form, **parameter-free** expression:


                <div class="mono">P(μ) = (1 &minus; μ)(5 + 7μ) / [(1 + μ)&sup2; (1 + 2μ)&sup2;]</div>

                No fitting. No tuning. You write down the formula, overlay it on election data from India, Brazil, Finland, wherever—and it fits. The universality comes from maximum entropy: the RVM is the least-biased way to partition votes among candidates, and that constraint alone is enough to pin down the entire distribution.


                ## Ecology got here first


                If this reminds you of something, it should. In 2001, Stephen Hubbell published *The Unified Neutral Theory of Biodiversity*, and it detonated a slow bomb in ecology that's still going off.


                Hubbell's provocation was simple: what if all species in a community are competitively equivalent? No niche differentiation, no fitness advantages, just birth, death, and drift. Under that assumption, species abundance distributions follow a universal, parameter-free pattern—and that pattern fits real tropical forest data disturbingly well.


                Ecologists hated it. Not because the math was wrong, but because it seemed to erase everything they cared about—adaptations, niches, the whole Darwinian machinery. The decades since have been productive precisely because of that tension. The neutral theory isn't "right" in the sense that species really are equivalent. It's right in the sense that it's the correct null hypothesis. Departures from neutrality are where the biology lives.


                <div class="highlight">
                    The RVM is the Hubbell model of elections. Candidates are "species," vote shares are "abundances," and the neutral assumption is that no candidate has a structural advantage. A fair election looks random for the same reason a neutral community looks random: because fairness *is* the absence of asymmetry, and the absence of asymmetry *is* maximum entropy.


                </div>

                ## What happens when fairness breaks


                This is where it gets interesting. If the RVM is your null, then deviations from it have a name: they're structural advantages. And there's a framework, originally from epidemiology, that gives those advantages a natural language.


                Avram, Adenane, and Halanay recently applied Chemical Reaction Network (CRN) theory to multi-strain competition models. Their key object is the **invasion number** R<sub>0</sub>: a single dimensionless quantity that tells you whether a new strain can displace the incumbent. When R<sub>0</sub> > 1, invasion succeeds. When R<sub>0</sub> < 1, the incumbent holds. They show that stability transitions in multi-strain systems are controlled by "relay transitions"—a chain of invasion inequalities flipping one by one.


                The analogy to elections writes itself. Candidates are competing strains. Campaign messaging is transmission. Vote share is prevalence. And the invasion number measures whether a challenger can break through—whether through superior resources, media access, institutional backing, or outright manipulation.


                In the neutral limit—all candidates equally "infectious"—a symmetric multi-strain CRN gives you a uniform Dirichlet distribution over vote shares. And a uniform Dirichlet is exactly the RVM prior. The connection is clean at this one point: neutrality in the epidemiological sense and neutrality in the electoral sense converge on the same mathematical object.


                ## Where the analogy breaks (honestly)


                I want to be careful here, because the temptation to over-sell this connection is real.


                The RVM universality is **static and combinatorial**. It's a statement about the geometry of fair partitions. It doesn't model any dynamics—no campaigns unfolding over time, no voter persuasion, no feedback loops. The CRN invasion framework is the opposite: it's **dynamical and parameter-dependent**. The invasion number R<sub>0</sub> depends on transmission rates, recovery rates, population structure—none of which have clean electoral analogs.


                So the connection is an analogy, not an equivalence. The two frameworks touch at the neutral fixed point and then diverge. The RVM tells you what "fair" looks like. The CRN framework tells you what "unfair" dynamics feel like. Stitching them into a single mathematical theory would require a dynamical model of elections that reduces to the RVM at equilibrium, and nobody has that yet.


                But here's the thing: the analogy failing in a specific, articulable way is more useful than it succeeding vaguely. We know *exactly* where the gap is. The RVM gives the static null. The CRN framework gives the language of departure. What's missing is the bridge—a dynamical election model where the invasion number has a concrete electoral interpretation and whose stationary distribution recovers the RVM when all invasion numbers equal one.


                ## The punchline: reframing malpractice


                Even without the bridge, the framing already changes how you think about election integrity. The standard approach to fraud detection is pattern-matching: Benford's law violations, suspicious turnout curves, statistical anomalies. These methods are useful but ad hoc. They tell you something looks weird without telling you *what kind* of weird.


                The neutral theory reframes the question. You're not looking for "fraud" in some vague sense. You're measuring how far an observed election deviates from the neutral baseline—from the distribution you'd expect if no candidate had any structural advantage. And the invasion-number framework gives the deviation a name: it's the effective R<sub>0</sub> of the winning candidate, the degree to which the playing field was tilted.


                <div class="highlight">
                    A fair election is one where every candidate's invasion number is approximately 1. Malpractice is R<sub>0</sub> >> 1 for the winner—not because they were more popular, but because structural asymmetries gave them a transmission advantage that no amount of "random voting" could explain.


                </div>

                This doesn't solve election forensics. But it gives the field something it badly needs: a null hypothesis with teeth. The RVM isn't a toy model. It's a baseline with a universal, parameter-free prediction, and deviations from it are quantifiable.


                ## What I actually think


                The deepest insight here isn't technical. It's conceptual: **fairness is randomness**. A level playing field, in the limit, is indistinguishable from noise. That's not a cynical statement about democracy—it's a precise one. When no one has an advantage, the outcome is determined by the combinatorics of large numbers, and combinatorics has a very specific signature.


                Ecology learned this lesson twenty-five years ago. Hubbell's neutral theory didn't kill niche theory; it sharpened it. It forced ecologists to ask: what can neutrality *not* explain? The residuals became the science.


                Elections are ready for the same move. The RVM draws the line. Everything on the other side of that line is politics, power, and possibly fraud. And now we have, at least in outline, a language for saying how far across the line you've gone.


                ## References


                **Pal, Kumar, Santhanam.** "Universal Statistics of Competition in Democratic Elections." *Physical Review Letters* 134, 017401 (2025). [arXiv:2401.05065](https://arxiv.org/abs/2401.05065)


                **Hubbell, S. P.** *The Unified Neutral Theory of Biodiversity and Biogeography.* Princeton University Press, 2001.


                **Avram, Adenane, Halanay.** "Relay transitions and invasion thresholds in multi-strain rumor models." [arXiv:2603.01186](https://arxiv.org/abs/2603.01186)
