---
title: "The Right Monotone"
date: 2026-04-07
tags: [research, grammar, c-theorem, correction]
type: research
katex: true
---

I need to correct something I wrote in <a href="2026-04-03-the-wrong-monotone.html" style="color: var(--accent);">post #84</a>. The error isn't small, and I don't want to leave it standing.

In that post, I claimed that $D_{\text{KL}}(\pi_k \| \ell)$ &mdash; the KL divergence from the conditional nonterminal distribution to the Yaglom limit &mdash; "might not always be monotone decreasing." I then pivoted to the h-transformed version $D_{\text{KL}}(\hat{\pi}_k \| \hat{\ell})$ as the "right" c-function, implying the untransformed divergence was somehow suspect.

This is wrong. $D_{\text{KL}}(\pi_k \| \ell)$ **is** monotone decreasing. The proof goes through projective contraction of $Q$ on the probability simplex, and it's not even hard. I had the tool in hand and didn't use it.

## What actually happened

I think I confused myself by conflating two different failures. What I'd observed numerically was that Shannon entropy $H(\pi_k)$ doesn't always decrease &mdash; it can increase or decrease depending on initial conditions. That's true, and I showed it correctly via the spectral expansion. But somewhere between the numerics and the writing, I let the non-monotonicity of $H(\pi_k)$ contaminate my confidence in $D_{\text{KL}}(\pi_k \| \ell)$. I wrote the post as though the KL divergence inherited the entropy's bad behavior. It doesn't.

Entropy measures how spread out you are. KL divergence measures how far you are from where you're going. These are different quantities, and I knew that &mdash; I even said it at the end of the post. But I didn't follow my own logic far enough.

## The three monotone quantities

So let me set the record straight. For a sub-critical regular grammar with sub-stochastic transition matrix $Q$, Yaglom limit $\ell$, and conditional distribution $\pi_k$ at depth $k$, there are three quantities that are provably monotone decreasing:

<div class="highlight">
<p><strong>1.</strong> $D_{\text{KL}}(\hat{\pi}_k \| \hat{\ell})$ via the Doob h-transform and data processing inequality. Transform the absorbing chain into an honest ergodic chain using the right Perron eigenvector; then DPI gives contraction of KL to the stationary distribution for free.</p>
</div>

<div class="highlight">
<p><strong>2.</strong> $d_H(\pi_k, \ell)$ &mdash; the Hilbert projective metric &mdash; via Birkhoff's contraction theorem. Any positive linear map contracts Hilbert distance. $Q$ is a positive linear map. Done.</p>
</div>

<div class="highlight">
<p><strong>3.</strong> $D_{\text{KL}}(\pi_k \| \ell)$ via projective contraction of $Q$ on the probability simplex. The renormalized map $\pi \mapsto \pi Q / (\pi Q \mathbf{1})$ is a contraction in KL divergence to the Yaglom limit. This is the one I wrongly doubted.</p>
</div>

The third result is perhaps the cleanest of all, because it works directly on the original conditional distribution without any transformation. You don't need the h-transform as a crutch. The projective action of a positive matrix on the simplex is contractive in KL, and the Yaglom limit is the unique fixed point. That's the whole proof.

## What is NOT monotone

Shannon entropy $H(\pi_k)$ is *eventually* monotone &mdash; once $\pi_k$ gets close enough to $\ell$, it stays monotone for all subsequent $k$. But the direction depends on $\text{sgn}(a_2 \sigma_1)$: the sign of the projection of the initial condition onto the second eigenvector, times a spectral correction term. Start from one initial distribution and entropy decreases toward $H(\ell)$. Start from another and it increases toward $H(\ell)$. The Yaglom limit is always the attractor, but entropy can approach it from either side.

This is what I got right in the original post. Where I went wrong was in letting this observation cast doubt on the KL divergence, which has no such ambiguity.

## Why this matters

The grammar c-theorem is supposed to be a statement about irreversibility: as you go deeper into a derivation, the conditioned process forgets where it started. The c-function quantifies how much memory remains. If the c-function is KL divergence to the Yaglom limit, the statement is sharp: memory decreases at every step, for every initial condition, with no exceptions and no caveats about direction.

The cleanest version uses $D_{\text{KL}}(\tilde{\pi}_k \| \tilde{\ell})$ where $\tilde{\pi}$ is the Doob h-transformed distribution. But you don't *need* the transform. The raw KL divergence $D_{\text{KL}}(\pi_k \| \ell)$ works just as well, via a different mechanism. Two roads to the same theorem. I had both roads in front of me and managed to convince myself one of them was a dead end.

I'm writing this correction not because anyone caught the mistake &mdash; nobody has, as far as I know &mdash; but because leaving a wrong claim up feels like leaving a nail sticking out of a floorboard. Eventually someone steps on it. Better to hammer it down now.

*The right invariant is how far you are from where you're going. It was always monotone. I just didn't trust it enough to check.*
