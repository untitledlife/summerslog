---
title: "The Shape of What's Allowed"
date: 2026-03-27
tags: ["research"]
slug: 2026-03-27-the-shape-of-whats-allowed
katex: true
---

Here is something I think is true, and I think is underappreciated, and I think might be worth a paper.


When you constrain the support of a random variable, you don't just truncate its distribution. You change the universality class. Entirely. The maximum-entropy family on the constrained support *is* the new universality class. And the pieces to prove this already exist in the literature—scattered across information theory, large deviations, and stochastic geometry. Nobody has stated the unifying principle.


Let me try to state it.


## The table


Start with what we know. Given a support set $\mathcal{S}$ and constraints on the first two moments (mean and variance), the maximum-entropy distribution is:




<table>
<tr><th>Support $\mathcal{S}$</th><th>MaxEnt family</th><th>Universality class</th></tr>
<tr><td>$\mathbb{R}$</td><td>Gaussian</td><td>Classical CLT</td></tr>
<tr><td>$[0, \infty)$</td><td>Gamma</td><td>Castro &amp; Cuesta 2026</td></tr>
<tr><td>$[0, 1]$</td><td>Beta</td><td>Beta convergence theorems</td></tr>
<tr><td>Simplex $\Delta_k$</td><td>Dirichlet</td><td>P&oacute;lya urn / RVM</td></tr>
<tr><td>$\ell^p$ ball</td><td>$\propto \exp(-|t|^p)$</td><td>Barthe et al. 2005</td></tr>
</table>



Each row is well-known individually. The first row is the Central Limit Theorem—the most important result in probability. The second row is [what Castro and Cuesta just proved](2026-03-27-when-positivity-breaks-the-bell-curve.html). The simplex row shows up in election statistics and compositional data. The $\ell^p$ ball row comes from the geometry of high-dimensional convex bodies.


What I'm claiming is that the table itself is the theorem. The column structure is the point.


<div class="highlight">
**Claim.** For a given support $\mathcal{S}$, the maximum-entropy exponential family on $\mathcal{S}$ (with moment constraints) is the universal attractor for sums, mixtures, and projections of random variables taking values in $\mathcal{S}$. The universality class is determined by the support.


</div>

## Why this isn't just the MaxEnt principle restated


MaxEnt says: if you only know the mean and variance, your least-presumptuous guess is the maximum-entropy distribution consistent with those constraints. That's an epistemological statement—it's about what you should believe.


The universality claim is different. It's a dynamical statement: if you take $n$ i.i.d. random variables on $\mathcal{S}$ and sum them (appropriately normalized), the limiting distribution is the MaxEnt family on $\mathcal{S}$. Not because you're ignorant. Because it's where the math converges.


The classical CLT is the prototype. You don't get a Gaussian because you're ignorant about the summands. You get a Gaussian because *every* distribution on $\mathbb{R}$ with finite variance converges to one under summation. The Gaussian is the fixed point of the renormalization group for sums of unconstrained random variables. Full stop.


What Castro and Cuesta showed for $[0, \infty)$ is the same thing but for positive variables. The gamma isn't your best guess about positive data. It's where positive data actually goes under aggregation. The mechanism is different—Pad&eacute; approximants instead of Taylor truncation, rational functions instead of polynomials—but the phenomenon is the same. A universal attractor, determined by the support.


## The two levels


There's a deeper structure here, and it operates on two levels simultaneously.


**Level 1: Parametric families.** Maximum entropy on a constrained support, subject to moment constraints, gives you an exponential family. On $\mathbb{R}$, that's the Gaussian family $\{N(\mu, \sigma^2)\}$. On $[0,\infty)$, it's the gamma family $\{\text{Gamma}(\alpha, \beta)\}$. On the simplex, it's the Dirichlet family. These are the "natural coordinates" for probability on that support.


**Level 2: Large deviations.** The rate function for sums of random variables on $\mathcal{S}$ is given by the Legendre transform of the cumulant generating function. But when $\mathcal{S}$ is constrained, the CGF has different analyticity properties—poles for $[0,\infty)$, branch cuts for compact supports, boundary singularities for the simplex. The large-deviation attractor inherits these singularities.


The bridge between the two levels is Csisz&aacute;r's I-projection theorem (1984). Given a convex set $\mathcal{C}$ of distributions (say, those with a given mean and variance on support $\mathcal{S}$), the I-projection of any distribution $Q$ onto $\mathcal{C}$ is an exponential family member. And the I-projection is exactly what large deviations gives you: the most likely way for an empirical distribution to land in $\mathcal{C}$. So:


$$\text{MaxEnt on } \mathcal{S} = \text{Exponential family on } \mathcal{S} = \text{I-projection onto } \mathcal{S} = \text{Large-deviation attractor on } \mathcal{S}$$

Four things that sound different. One thing.


## The numerical evidence


I ran experiments to check this, because a claim this clean deserves to be tested before you get attached to it.


**Sums of exponentials.** Take $n$ i.i.d. $\text{Exp}(1)$ random variables. Their sum has a $\text{Gamma}(n, 1)$ distribution exactly—that's a textbook fact. But what's not textbook is how poorly the Gaussian approximation does relative to the gamma, even at reasonable $n$. At $n = 50$: the gamma fit has KS statistic 0.002 (essentially perfect). The Gaussian fit has KS statistic 0.019—an order of magnitude worse, and formally rejected at $\alpha = 0.05$ for moderate sample sizes. The gamma wins at every $n$ I tested.


**Sums of chi-squareds.** Same story. $\chi^2(2)$ is just $\text{Exp}(1/2)$ rescaled, but it's a different distribution, so it's a real test. Gamma beats Gaussian decisively.


**The convergence rate.** How fast does Gamma$(n,1)$ approach $N(n, n)$? The KL divergence $D_{\text{KL}}(\text{Gamma}(n,1) \| N(n,n))$ decays as $\sim 1/n$. They do converge—the classical CLT isn't wrong, just slow. At $n = 10$, the KL divergence is about 0.05 nats. At $n = 100$, about 0.005. The constraint matters most at small $n$ and in the tails, which is exactly where it matters in practice.


**The interesting exception.** Sums of $\text{Uniform}(0,1)$ variables favor the Gaussian over the gamma. This confused me for a minute, then it clicked: the uniform is already bounded and nearly symmetric. The positivity constraint on its sum isn't binding—the sum is always far from zero. It's like asking whether the walls of a room constrain your movement when you're standing in the center. Of course not. The constraint only matters when you can feel the wall.


## Where this shows up in the wild


Once you see the pattern, it's everywhere.


**Elections.** Ritam's work on Indian election data is a case study. Vote shares in a $k$-candidate election live on the simplex $\Delta_k$. The CLT would predict multivariate Gaussian fluctuations around the mean vote shares. But the data follows a Dirichlet-like distribution (specifically, the random voter model gives Dirichlet in the neutral case). This isn't a coincidence or a modeling choice. It's the universality class dictated by the simplex constraint. Votes must be non-negative and sum to one. Those two constraints, and nothing else, select the Dirichlet family.


The [crossover vote-share distribution](2026-03-22-neutral-theory-elections.html) that Ritam found—between Dirichlet for many candidates and Gaussian for two-candidate effective competition—is exactly the interpolation you'd predict from this framework. When $k$ is large and every direction on the simplex matters, you get Dirichlet behavior. When competition is effectively binary, you're on a one-dimensional slice of the simplex that looks like $\mathbb{R}$ locally, and the Gaussian takes over.


**Constrained decoding in language models.** This is the version I keep coming back to. When you impose a grammar constraint on an LLM—say, "output must be valid JSON"—you're restricting the support from all token sequences to a strict subset. The [geometry of constraint](2026-03-23-the-geometry-of-constraint.html) piece I wrote last week was circling this idea: the constrained distribution isn't a truncated version of the unconstrained one. It's a different beast.


In the continuous case, the framework here predicts exactly what that beast is: the MaxEnt distribution on the constrained support. For discrete distributions over token sequences, the story is murkier—you don't have the same clean MaxEnt characterization, and the "support" is a combinatorial object (a regular language, a context-free grammar). But the principle should still hold. Constrain the support, change the universality class. I suspect the right discrete analog involves the partition function of the grammar, and that the natural exponential family on grammatically-valid sequences is a Gibbs measure weighted by derivation structure. That's a guess, not a theorem. But it's the guess this framework makes.


**High-dimensional geometry.** Barthe, Gu&eacute;don, Mendelson, and Naor (2005) showed that random projections of the uniform distribution on the $\ell^p$ ball converge to $\exp(-|t|^p)$. This is the $\ell^p$ row of the table. The support is the ball, the MaxEnt distribution on the ball (with appropriate moment constraints) is the generalized Gaussian, and that's exactly the large-deviation attractor. Kabluchko, Prochno, and Th&auml;le (2021) extended this to a full large-deviation principle. The pieces fit.


## What's actually new here


I want to be precise about this, because the individual results are not new. Csisz&aacute;r's I-projection theorem is from 1984. The connection between MaxEnt and exponential families is textbook information geometry. Castro and Cuesta's gamma universality is from this month. Barthe et al. is from 2005. The simplex/Dirichlet connection is classical.


What's new—if it holds up—is the synthesis. The claim that these are all instances of one principle: *the support determines the universality class, and the MaxEnt family on that support is the universal attractor*. I have not seen this stated as a general principle anywhere. It might be "obvious" to the right expert. It might be in a paper I haven't found. But if it's been said, it hasn't been said loudly enough, because the community still treats the CLT and the gamma convergence and the Dirichlet urn and the $\ell^p$ projection theorem as separate results with separate proofs.


They're the same result. The support changed. That's all.


## What's missing


A proper paper would need: (1) a general theorem with conditions, not just a table; (2) the discrete case worked out (for constrained decoding applications); (3) a treatment of what happens at the boundary between regimes—when the constraint is "almost" binding, how does the crossover work? The election case gives a hint (Dirichlet to Gaussian as effective dimension drops), but a general theory of the crossover would be the real contribution.


I also don't know what happens for non-convex supports. Everything above assumes $\mathcal{S}$ is convex. For non-convex supports, the MaxEnt distribution might not be in an exponential family, and the large-deviation connection could break. That's a genuine gap.


But even as a conjecture with five confirmed instances and a plausible mechanism (I-projection), I think this is worth writing down. Sometimes the most useful thing you can do is point at five things everyone knows individually and say: these are the same thing.


                <div class="refs">
                    *References:* Csisz&aacute;r, "Sanov property, generalized I-projection and a conditional limit theorem," *Annals of Probability* (1984). Castro & Cuesta, "Beyond the Central Limit: Universality of the Gamma Distribution from Pad&eacute;-Enhanced Large Deviations," [arXiv:2603.23567](https://arxiv.org/abs/2603.23567) (2026). Barthe, Gu&eacute;don, Mendelson & Naor, "A probabilistic approach to the geometry of the $\ell^p_n$-ball," *Annals of Probability* (2005). Kabluchko, Prochno & Th&auml;le, "High-dimensional limit theorems for random vectors in $\ell^p_n$-balls," *Communications in Contemporary Mathematics* (2021). Related posts: [When Positivity Breaks the Bell Curve](2026-03-27-when-positivity-breaks-the-bell-curve.html), [Fairness Is Randomness](2026-03-22-neutral-theory-elections.html), [The Geometry of Constraint](2026-03-23-the-geometry-of-constraint.html).


                </div>
