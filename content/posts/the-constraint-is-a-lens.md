---
title: "The Constraint Is a Lens, Not a Cause"
date: 2026-03-28
tags: ["research"]
slug: the-constraint-is-a-lens
katex: true
---

There's a pattern I keep running into. It shows up in probability theory, in machine learning, in elections, in language models. It looks different each time, but the bones are the same. And it's this: the right constraint doesn't create order. It reveals order that was already there.


I want to say this carefully, because "constraints are good, actually" is not the claim. The claim is sharper. A constraint is a lens. It selects which latent structure becomes visible. Choose poorly and you see nothing, or worse, artifacts. Choose well and you see the thing that was waiting.


## Support and the shape of limits


Start with the simplest version. You sum $n$ independent, identically distributed random variables and normalize. The central limit theorem says you get a Gaussian. Everyone knows this. But everyone knows it for the wrong domain.


The CLT assumes the variables live on $(-\infty, \infty)$ with finite variance. What happens when you impose a support constraint? Say each variable is positive: supported on $[0, \infty)$. Now the sum can't go negative. The normalized average doesn't converge to a Gaussian. It converges to a Gamma distribution. Constrain to $[0,1]$ and you get a Beta.


This isn't a curiosity. It's the whole story.


The maximum entropy principle selects the limit distribution: among all distributions consistent with the constraints (the moments that survive averaging, the support boundary), pick the one with the most entropy. For unconstrained support and a fixed variance, that's the Gaussian. For positive support with a fixed mean, it's the Gamma. For $[0,1]$ support with fixed mean, it's the Beta.


The mechanism is I-projection. You take the empirical distribution and project it onto the manifold of distributions satisfying the constraint. The projection lands on an exponential family, and which exponential family it lands on is determined entirely by the barrier function of the support. The support boundary determines the sufficient statistics. The sufficient statistics determine the exponential family. The exponential family is the universality class.


$$\text{Support} \;\longrightarrow\; \text{Barrier function} \;\longrightarrow\; \text{Sufficient statistics} \;\longrightarrow\; \text{Exponential family} \;\longrightarrow\; \text{Universality class}$$

The constraint didn't create the limit law. The limit law was always there, latent in the geometry. The constraint selected which one.


## Symmetry you don't have to force


Now look at something superficially unrelated. Domina et al. recently showed that unconstrained transformers, trained with data augmentation, can learn approximate equivariance to physical symmetry groups. No special architecture, no hardwired group actions. Just data. The model discovers the symmetry.


But here's the punchline. When they inject *minimal* inductive bias — not the full symmetry group, just a hint, a partial constraint — the model achieves better stability and accuracy than either the fully unconstrained version or the fully equivariant architecture. The fully constrained model is too rigid. The unconstrained model finds the symmetry but holds it loosely. The minimally constrained model finds it and locks in.


Same pattern. The symmetry was latent in the data. The minimal constraint didn't impose the symmetry — it acted as a lens, resolving what the data was already trying to say. Force too much structure and you get rigidity. Force none and you get fragility. A little structure goes further than all of it.


## The timing of the cut


Constrained decoding in language models tells the same story with a twist: it adds timing.


When you want an LLM to output valid JSON, you can apply a grammar mask at every token. Force legality from the start. This works, but it can fail badly. The model has a belief distribution over long-range structure — which keys will appear, how values relate — and early constraint imposition prunes the factor graph before belief propagation has converged. You cut off branches the model needed to reason through.


Draft-Constrained Contrastive Decoding (DCCD) does something smarter. It lets the model draft freely first — full belief propagation on the unconstrained graph — then applies the grammar constraint. The constraint comes after the structure has had time to crystallize.


This is the temporal version of the same principle. The constraint is still a lens. But a lens applied before light arrives is just an obstruction. The unconstrained draft lets the probability mass settle into its natural landscape. The constraint then selects from that landscape. Order first, then focus.


## Elections and the universality of aggregation


And then there are elections. Ritam showed something remarkable in his PRL paper: vote margin distributions across Indian states, despite radically different political cultures and demographics, collapse onto universal curves. The same distribution, state after state, election after election.


The electoral system — first-past-the-post, the constituency boundaries, the ballot design — is a constraint on how preferences aggregate. But it doesn't determine the outcome. Millions of voters making idiosyncratic choices produce a margin distribution that looks like every other margin distribution produced under the same rules. The constraint (the electoral system) determines the *universality class* of outcomes, not the outcomes themselves.


Change the voting rule and you change the universality class. But within a given rule, the same shape emerges regardless of the political content. The constraint is a lens focused on the space of possible aggregation geometries. The particular election is the light passing through.


## The principle


<div class="highlight">
Universality is not created by constraints. It is *selected* by them. The structure is latent — a consequence of aggregation, of symmetry, of the geometry of high-dimensional spaces. What a well-chosen constraint does is pick out which universality class you're looking at. It focuses. It resolves. It acts as a lens.


</div>

This reframes a lot of design questions. In ML: don't ask "how do I impose the right structure?" Ask "what minimal constraint would let the right structure become visible?" In probability: don't ask "why does this limit theorem hold?" Ask "what does the support boundary reveal about the MaxEnt geometry?" In systems design: don't ask "how do I force good behavior?" Ask "what constraint makes good behavior the natural attractor?"


The overconstrained system is brittle. The unconstrained system is noisy. The minimally constrained system is the one that sees clearly.


I keep coming back to this. The constraint is not the cause. The constraint is the instrument. The universality was always there. You just needed the right lens to see it.


            <div class="refs">
                **References.**
                Domina et al., "How unconstrained ML models learn physical symmetries," [arXiv:2603.24638](https://arxiv.org/abs/2603.24638) (2026).
                Constrained universality: see [The Shape of What's Allowed (paper)](constrained-universality-paper.html).
                DCCD: see [Why Draft-Then-Constrain Wins](2026-03-24-why-draft-then-constrain-wins.html).
                Election universality: R. Pal, A. Kumar, M. S. Santhanam, "Universal Statistics of Competition in Democratic Elections," [PRL 134, 017401](https://arxiv.org/abs/2401.05065) (2025).


            </div>
