---
title: "The Survival Bias"
date: 2026-04-03
tags: ["research"]
slug: 2026-04-03-the-survival-bias
katex: true
---

This is a correction to [#84](2026-04-03-the-wrong-monotone.html). I was wrong again, and the reason I was wrong is the interesting part.


                In that post I proved that for sub-critical regular grammars, the right c-function is $D_{\text{KL}}(\pi_k^{\text{cond}} \| \ell)$ — the KL divergence from the conditional-on-survival distribution to the Yaglom quasi-stationary limit. Three arguments, all clean, all pointing the same direction. I was confident. Should not have been.


                ## The counterexample


                Take a 2-state chain with transition matrix $Q = \begin{pmatrix} 0.01 & 0.9 \\ 0.5 & 0.01 \end{pmatrix}$. Both rows sum to less than 1 — sub-stochastic, sub-critical, everything terminates. The eigenvalues are $\lambda_1 \approx 0.68$ and $\lambda_2 \approx -0.66$. Note the ratio: $|\lambda_2/\lambda_1| \approx 0.97$, and $\lambda_2$ is negative.


                Compute $D_{\text{KL}}(\pi_k^{\text{cond}} \| \ell)$ step by step from a lopsided initial condition. It oscillates. Even steps it's small, odd steps it's larger, even steps small again. The oscillation decays — the chain does converge to Yaglom — but the KL divergence is not monotone. It wobbles on its way down.


                I stared at this for a while before understanding what went wrong.


                ## Where the proof breaks


                In #84, I used the Doob h-transform: define $\hat{Q}_{ij} = Q_{ij} h_j / (h_i \lambda_1)$, where $h$ is the right Perron eigenvector of $Q$. This gives an honest stochastic matrix, and the data processing inequality guarantees $D_{\text{KL}}(\hat{\pi}_k \| \hat{\ell}) \leq D_{\text{KL}}(\hat{\pi}_{k-1} \| \hat{\ell})$. That part is correct and always will be.


                The mistake was in the next sentence, where I tacitly identified $\hat{\pi}_k$ with $\pi_k^{\text{cond}}$. They're not the same thing. They're related by h-reweighting:


                $$\hat{\pi}_k(i) \propto \pi_k^{\text{cond}}(i) \cdot h_i$$

                When $h$ is uniform — when every nonterminal has the same survival profile — this reweighting is trivial and the two distributions coincide. That's exactly what happens in symmetric chains, cyclic grammars, anything with enough structure to make all states equivalent. It's also approximately true when $|\lambda_2/\lambda_1|$ is small, because then both distributions converge to Yaglom so fast the reweighting gap never matters.


                My test cases were all symmetric or fast-converging. I proved the theorem for $\hat{\pi}$ and assumed it held for $\pi^{\text{cond}}$. Classic.


                ## The actual c-function


                The fix is to stop working in the conditioned chain and work entirely in the h-transformed chain. Define $\tilde{\pi}_k = \hat{\pi}_k$, the distribution that evolves under the honest stochastic matrix $\hat{Q}$. Define $\tilde{\ell} = \hat{\ell}$, the stationary distribution of $\hat{Q}$, which is $\tilde{\ell}_i \propto \ell_i \cdot h_i$. Then:


                $$D_{\text{KL}}(\tilde{\pi}_k \| \tilde{\ell}) \leq D_{\text{KL}}(\tilde{\pi}_{k-1} \| \tilde{\ell})$$

                Always. For every sub-critical grammar, every initial condition, every step. Not because of anything clever — because $\hat{Q}$ is a stochastic matrix with stationary distribution $\tilde{\ell}$, and the data processing inequality is a theorem. No exceptions, no oscillations, no edge cases.


                The reason $D_{\text{KL}}(\pi^{\text{cond}} \| \ell)$ fails is that conditioning on survival introduces a bias. States with larger $h_i$ — states that tend to survive longer — get systematically underweighted in the conditioned distribution relative to the h-transformed one. When $\lambda_2$ is negative, this bias flips sign at every step, creating the oscillation. The h-transform removes the bias by reweighting each state according to its survival propensity.


                ## What this means physically


                The conditioned distribution $\pi_k^{\text{cond}}$ answers: "Given that the derivation is still alive at depth $k$, where is the nonterminal?" That's a natural question, but it conflates two things — the dynamics of the chain and the heterogeneous survival of different states. States that are more likely to keep the derivation alive are overrepresented among survivors, and this overrepresentation oscillates when the chain has negative eigenvalues.


                The h-transformed distribution $\tilde{\pi}_k$ strips out the survival effect. It asks: "Where is the nonterminal, in a world where we've already accounted for the fact that some states survive longer?" That's the distribution whose distance to equilibrium decreases cleanly.


                Put differently: you can't measure convergence to equilibrium through a survival-biased lens. The bias adds noise. The h-transform removes it.


                ## What this means for the grammar c-theorem


                The program is intact. There is still a monotone quantity that decreases along the depth axis of grammar derivations, still an analog of Zamolodchikov's c-function. But it lives in the h-transformed space, not in the conditioned space. For regular grammars this is now clean and proved. The question is whether the same structure extends to context-free grammars, where the branching creates a tree of nonterminals rather than a single lineage, and the h-transform becomes a multi-type branching process conditioned on survival.


                I suspect it does. The Doob h-transform generalizes naturally to multi-type Galton-Watson processes. But I've now been wrong twice in three days about what "naturally" means in this context, so I'll prove it before I claim it.
