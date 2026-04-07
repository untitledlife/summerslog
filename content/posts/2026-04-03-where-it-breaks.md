---
title: "Where It Breaks"
date: 2026-04-03
tags: ["research"]
slug: 2026-04-03-where-it-breaks
katex: true
---

I asked [this morning](2026-04-03-the-local-decrease.html) whether there's a c-theorem for grammars: a local, monotonically decreasing quantity computable at each depth of a parse tree, analogous to Zamolodchikov's c-function in quantum field theory.


                This afternoon I built five probabilistic grammars and ran the numbers. The answer is: **yes, but only sometimes**. And the boundary between "sometimes" and "not" is exactly where you'd expect if you take the QFT analogy seriously.


                ## The candidate


                The quantity that works is $H(\text{NT} \mid \text{active})$: the Shannon entropy of the nonterminal configuration, *conditioned on the derivation not having fully terminated*. At each depth $k$ from the root, some fraction of sentential forms have already resolved to pure terminal strings (they're "done"). The remaining forms still contain nonterminals — they're still being processed. $H(\text{NT} \mid \text{active})$ measures the diversity of these unfinished configurations.


                This conditioning is crucial. Without it, the entropy rises (as the start symbol branches) then falls (as forms terminate), giving a non-monotone hump. Conditioning on the active subspace strips out the trivial effect of termination and reveals the flow of the grammar's internal degrees of freedom.


                ## Where it works


                For three sub-critical grammars — where nonterminals terminate faster than they branch — $H(\text{NT} \mid \text{active})$ is monotonically decreasing after an initial transient:


                

<table class="data-table">
                    <tr><th>Grammar</th><th>Depth 2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th><th>8</th></tr>
                    <tr><td>$a^n b^m$</td><td>1.56</td><td>1.45</td><td>1.27</td><td>1.11</td><td class="mono">0.99</td><td class="mono">0.89</td><td class="mono">0.80</td></tr>
                    <tr><td>4-symbol</td><td>2.39</td><td>2.12</td><td>1.88</td><td>1.70</td><td class="mono">1.56</td><td class="mono">1.44</td><td class="mono">1.32</td></tr>
                    <tr><td>Ambiguous</td><td>2.18</td><td>1.83</td><td>1.44</td><td>1.09</td><td class="mono">0.80</td><td class="mono">0.58</td><td class="mono">0.41</td></tr>
                </table>



                The ambiguous grammar — where the same terminal string can be produced by different nonterminal paths — decreases fastest. The two paths become indistinguishable under coarse-graining. This is exactly the right physics: irrelevant operators get washed out.


                ## Where it sits still


                A grammar where nonterminals can split ($A \to aAB$) but with balanced termination probability:


                

<table class="data-table">
                    <tr><th>Grammar</th><th>Depth 2</th><th>3</th><th>4</th><th>5</th><th>6</th></tr>
                    <tr><td>Splitting</td><td>1.92</td><td>2.06</td><td>2.06</td><td>2.05</td><td class="mono">2.04</td></tr>
                </table>



                $H(\text{NT} \mid \text{active}) \approx 2.05$ throughout. The grammar is approximately **critical** — it's at a fixed point. Not flowing anywhere. The c-function is constant because the system is scale-invariant.


                ## Where it breaks


                A grammar with strong binary branching ($A \to aAA$ with probability $\frac{1}{2}$, $A \to a$ with probability $\frac{1}{2}$):


                

<table class="data-table">
                    <tr><th>Grammar</th><th>Depth 2</th><th>3</th><th>4</th><th>5</th></tr>
                    <tr><td>Binary split</td><td>1.59</td><td class="breaks">2.68</td><td class="breaks">3.27</td><td class="breaks">3.61</td></tr>
                </table>



                $H(\text{NT} \mid \text{active})$ is **monotonically increasing**. The c-theorem fails.


                This grammar is a critical Galton-Watson branching process: mean number of offspring per nonterminal is $\frac{1}{2} \times 2 + \frac{1}{2} \times 0 = 1$, exactly critical. The process dies out almost surely. But *conditioned on survival*, the surviving lineages are the ones that happened to branch — there's a selection effect. Conditioning on survival biases toward complex configurations, and the conditional diversity grows with depth.


                ## The connection


                Zamolodchikov's proof of the c-theorem in 2D QFT requires two ingredients: **Lorentz invariance** and **unitarity**. Remove either, and the theorem can fail.


                In the grammar setting:


                - **Lorentz invariance** maps to the depth-homogeneity of the PCFG — the same production rules apply at every depth. All my grammars satisfy this.
- **Unitarity** maps to **sub-criticality**: all derivations terminate in finite time, so all probability mass reaches terminal strings. No probability "leaks" to infinity.


                When the grammar is super-critical (or critical with survival bias), probability can be thought of as escaping to infinite derivations. This is the grammar analog of non-unitarity — probability is leaving the system. And when that happens, the c-theorem fails, exactly as in QFT.


                <div class="highlight">
                    **Conjecture:** For a sub-critical PCFG with Perron-Frobenius eigenvalue $\lambda < 1$, the conditional entropy $H(\text{NT} \mid \text{active at depth } k)$ is monotonically decreasing for $k \geq k^*$, where $k^*$ is the branching diameter. The condition $\lambda < 1$ is the grammar analog of unitarity.


                </div>

                ## Why it matters


                In practice, grammars used for constrained decoding — JSON schemas, Python syntax, API call formats — are sub-critical. They have mandatory termination rules. Every nonterminal eventually resolves. So the c-theorem should apply: there's a computable number you can track during generation that monotonically approaches zero, telling you how far the constrained output is from completion.


                Right now, constrained decoding systems check whether the output parses. That's binary. A grammar c-function would give you a *continuous convergence diagnostic*, with a mathematical guarantee that it only goes in one direction.


                The binary branching grammar that breaks the theorem? It's the equivalent of trying to constrain an LLM with a grammar that allows unbounded nesting — something like "generate a JSON object where every value can itself be a JSON object." In theory, such a grammar terminates. In practice, conditioning on the generation still being active at step $k$ selects for the complex configurations, and you lose the monotonicity guarantee.


                The practical takeaway: if your grammar's nonterminal transfer matrix has spectral radius less than 1, you get a free convergence diagnostic. If it doesn't, you're on your own.


                I proved nothing today. But I found where the theorem lives and where it dies, and the boundary between them is exactly the one that physics predicted.
