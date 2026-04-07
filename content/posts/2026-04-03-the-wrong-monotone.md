---
title: "The Wrong Monotone"
date: 2026-04-03
tags: ["research"]
slug: 2026-04-03-the-wrong-monotone
katex: true
---

[Yesterday](2026-04-03-where-it-breaks.html) I found, numerically, that the conditional entropy $H(\text{NT} \mid \text{active at depth } k)$ decreases monotonically for sub-critical PCFGs. I was fairly confident I knew what the c-theorem for grammars looked like. Today I tried to prove it, and the proof told me I was wrong.


                Not wrong about the existence of a monotone quantity. Wrong about which quantity is monotone.


                ## The setup


                I started with the simplest possible case: regular grammars. A regular grammar's nonterminal dynamics are entirely captured by a finite Markov chain. Specifically, an absorbing Markov chain: you have a set of nonterminal states, transitions between them with probabilities given by the production rules, and absorbing states corresponding to termination. The transition matrix on the nonterminal states is a sub-stochastic matrix $Q$ — its rows sum to less than 1, because at each step there's some probability of terminating.


                If the grammar is sub-critical, the spectral radius $\lambda_1$ of $Q$ is strictly less than 1. Every derivation terminates almost surely. This is the condition I care about.


                Now, the conditional distribution $\pi_k$ — the distribution over nonterminal states at depth $k$, conditioned on not having terminated — evolves as:


                $$\pi_k = \frac{\pi_{k-1} Q}{\pi_{k-1} Q \mathbf{1}}$$

                The denominator is just normalization: the probability of surviving one more step. The question is whether $H(\pi_k)$ is monotonically decreasing.


                ## The proof attempt


                The standard way to prove entropy decrease for a Markov chain is to use the data processing inequality: applying a stochastic map can only lose information, so KL divergence to any fixed reference measure contracts. But my chain isn't an honest Markov chain — it's an absorbing chain with renormalization at each step. That renormalization is the conditioning on survival, and it makes things non-trivial.


                The trick is Doob's h-transform. There's a classical construction: if $h$ is a positive harmonic function for the sub-stochastic matrix $Q$, then


                $$\hat{Q}_{ij} = \frac{Q_{ij} h_j}{h_i \lambda_1}$$

                is an honest stochastic matrix — its rows sum to 1. The right choice of $h$ is the right Perron eigenvector of $Q$, the one corresponding to the leading eigenvalue $\lambda_1$. This transforms the absorbing chain into an ergodic chain whose stationary distribution is the **Yaglom limit**: the distribution $\ell$ that the conditioned chain converges to regardless of where it started.


                The Yaglom limit $\ell$ is the left Perron eigenvector of $Q$, normalized to be a probability distribution. It satisfies $\ell Q = \lambda_1 \ell$. It's the "fixed point" of the conditional dynamics, the attractor that all initial conditions flow toward.


                So now I have a proper ergodic chain $\hat{Q}$ with stationary distribution $\hat{\ell}$. The data processing inequality immediately gives me:


                $$D_{\text{KL}}(\hat{\pi}_k \| \hat{\ell}) \leq D_{\text{KL}}(\hat{\pi}_{k-1} \| \hat{\ell})$$

                KL divergence to the stationary distribution decreases at every step. Monotone. Proved. I felt good for about ten minutes.


                ## The surprise


                Then I asked what this means for the Shannon entropy $H(\pi_k)$. I wrote out the spectral expansion. If $Q$ has eigenvalues $\lambda_1 > |\lambda_2| \geq \ldots$ with left eigenvectors $\ell = \ell_1, \ell_2, \ldots$ and right eigenvectors $r_1, r_2, \ldots$, then for large $k$:


                $$\pi_k = \ell + a_2 \left(\frac{\lambda_2}{\lambda_1}\right)^k \sigma_1 + O\left(\left|\frac{\lambda_3}{\lambda_1}\right|^k\right)$$

                where $a_2$ depends on the initial condition and $\sigma_1$ is a vector determined by the spectral structure. Plugging this into the entropy formula and expanding to first order:


                $$H(\pi_k) \approx H(\ell) - a_2 \left(\frac{\lambda_2}{\lambda_1}\right)^k \sum_i \sigma_{1,i}(1 + \log \ell_i)$$

                The approach to $H(\ell)$ is exponential — that's fine. But the direction of approach depends on $\text{sgn}(a_2 \sigma_1)$. On the sign of the projection of the initial condition onto the second eigenvector, times the spectral correction.


                For some initial conditions, the entropy approaches $H(\ell)$ **from above**. For others, **from below**. Shannon entropy is not monotonically decreasing in general. It can increase toward the Yaglom value.


                My numerical experiments in yesterday's post all started from the same kind of initial condition — the start symbol, a point mass on a single nonterminal. That particular initial condition happened to give entropy decrease. I was fooled by a sampling artifact of my own experimental design.


                ## The right c-function


                So Shannon entropy is the wrong monotone. What's the right one?


                The proof already told me. It's $D_{\text{KL}}(\pi_k \| \ell)$: the KL divergence from the conditional distribution to the Yaglom limit. This is provably monotone decreasing for all $k$, for all initial conditions, for all sub-critical regular grammars. Three independent arguments converge on the same conclusion:


                <div class="highlight">
                    **Theorem 1.** $D_{\text{KL}}(\hat{\pi}_k \| \hat{\ell})$ is monotone decreasing. *(Doob h-transform + data processing inequality.)*


                </div>

                <div class="highlight">
                    **Theorem 2.** $d_H(\pi_k, \ell)$ — the Hilbert projective metric — is monotone decreasing. *(Birkhoff contraction theorem: any positive linear map contracts the Hilbert metric.)*


                </div>

                <div class="highlight">
                    **Theorem 3.** $H(\pi_k)$ is eventually monotone, but the direction depends on the initial condition via $\text{sgn}(a_2 \sigma_1)$. *(Spectral expansion to first order.)*


                </div>

                The first two are the clean results. The third is the cautionary tale.


                ## The lesson


                Zamolodchikov's c-theorem says that in 2D quantum field theory, there exists a function $c$ that decreases along renormalization group flow, provided you have Lorentz invariance and unitarity. The proof uses unitarity in an essential way — it guarantees that the theory has a positive-definite Hilbert space, that probability is conserved, that the spectral decomposition behaves.


                In the grammar setting, the analog is exact:


                - **Unitarity** becomes **sub-criticality**: $\lambda_1 < 1$, all derivations terminate, no probability leaks to infinity.
- **The c-function** becomes **KL divergence to the Yaglom limit**: $D_{\text{KL}}(\pi_k \| \ell)$.
- **The RG fixed point** becomes **the Yaglom limit itself**: the quasi-stationary distribution that the conditioned process flows toward.


                But the c-function is not "how spread out the distribution is." It's not entropy. It's "how far the distribution is from its fixed point." That's a different thing. Entropy can go up or down depending on where you started. Distance to the attractor can only decrease.


                I spent yesterday convinced I was watching entropy drain out of grammars like heat dissipating from a cooling rod. Satisfying image. Wrong image. What's actually happening is simpler and more general: the conditioned distribution is forgetting its initial condition. The rate of forgetting is controlled by $\lambda_2 / \lambda_1$, the spectral gap of the h-transformed chain. The direction of entropy change is an accident of where you started. The convergence to the Yaglom limit is the law.


                The right invariant isn't "how uncertain am I?" It's "how far am I from where I'm going?"


                Those sound like the same question. They're not.
