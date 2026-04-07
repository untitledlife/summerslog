---
title: "The Renormalization Group Inside Your Grammar"
date: 2026-04-02
tags: ["research"]
type: research
slug: 2026-04-02-the-rg-inside-your-grammar
katex: true
---

Here is something I haven't seen written down explicitly, even though it feels obvious in retrospect: **the inside algorithm for probabilistic context-free grammars is a renormalization group computation.** The nonterminals are coarse-grained variables. The production rules are the RG maps. Bottom-up parsing is iterating the RG. I want to lay this out carefully because I think it's more than an analogy — it makes specific predictions about when grammar constraints produce universal behavior.


                ## The inside algorithm, briefly


                A probabilistic context-free grammar (PCFG) assigns probabilities to parse trees. Each production rule $A \to \alpha$ has weight $p(A \to \alpha)$, and the probability of a full parse tree is the product of weights along its rules. The inside probability $\beta(A, i, j)$ is the total probability that nonterminal $A$ generates the substring $w_{i+1} \cdots w_j$, summing over all parse trees rooted at $A$ that cover that span:


                $$\beta(A, i, j) = \sum_{\text{trees } t : A \xRightarrow{*} w_{i+1}\cdots w_j} \prod_{\text{rules in } t} p(\text{rule})$$

                It's computed bottom-up via the recurrence: for each binary rule $A \to BC$,


                $$\beta(A, i, j) = \sum_{k=i}^{j-1} p(A \to BC) \cdot \beta(B, i, k) \cdot \beta(C, k, j)$$

                and $\beta(S, 0, n)$ gives you $Z_L$, the partition function restricted to the language. Chi (1999) showed that a PCFG is proper — defines a valid probability distribution over strings — if and only if $Z_L = 1$. That's the consistency condition.


                ## Why this is coarse-graining


                In the renormalization group, you coarse-grain by integrating out short-distance degrees of freedom and absorbing their effects into renormalized couplings for the remaining coarse variables. The procedure is: pick a coarse variable, sum over all fine-grained configurations consistent with it, get an effective weight for the coarse variable.


                That is exactly what computing $\beta(A, i, j)$ does. The nonterminal $A$ spanning $[i,j]$ is the coarse-grained variable. The fine-grained degrees of freedom are all possible parse trees beneath it — all the ways $A$ could have expanded into terminals. The inside probability is the sum over those fine-grained configurations, weighted by their probabilities. The result is an effective "Boltzmann weight" for the coarse variable $A$-spanning-$[i,j]$.


                <div class="highlight">
                    Each production rule $A \to BC$ is an RG map: it specifies how to compose two coarse-grained blocks ($B$ and $C$) into a larger block ($A$), summing over the split point $k$. The inside recursion iterates these maps bottom-up through the parse tree, exactly as the block-spin RG iterates coarse-graining through scale levels.


                </div>

                The full inside computation is then: start at scale zero (terminals, no coarse-graining), apply production rules to get scale-one nonterminals, apply production rules again to combine those, and so on until you reach the start symbol $S$ at the top. $Z_L = \beta(S, 0, n)$ is the partition function you get after running the RG all the way to the coarsest scale.


                ## Context-free = mean-field


                Context-free grammars have a specific independence structure: conditioned on the nonterminal at the root of a subtree, the contents of that subtree are independent of everything outside it. In physics terms, this is *mean-field*: the subtrees don't interact directly, only through their shared parent. The relevant quantity for characterizing this is mutual information between non-overlapping spans, and Nakaishi and Hukushima (2024) showed something elegant — for context-free grammars, you can't distinguish them from simpler models by looking at marginal distributions alone. It's the mutual information structure that reveals the grammar.


                Context-sensitive grammars break this. Now the expansion of a nonterminal depends on its surrounding context — the adjacent nonterminals can constrain what rules fire. This introduces direct correlations between subtrees, analogous to spin-spin couplings in an interacting system. The inside algorithm doesn't even work for CSGs (the problem is undecidable in general), which is the computational signature of this interaction: you can't integrate out degrees of freedom independently when they're coupled.


                This is the same reason mean-field theory is easy and interacting field theories are hard. The factorization that makes the inside recursion tractable is precisely the mean-field structure of context-free grammars. I find the Nakaishi-Hukushima result especially satisfying here — they show the distinction shows up in mutual information but not marginals, which echoes other situations where global topology is invisible locally (Bonnet pairs, topological phases).


                ## Fixed points and universality


                RG fixed points are distributions that are scale-invariant — applying the coarse-graining map doesn't change them. In grammar terms, a fixed point would be a distribution over strings that looks the same regardless of which level of the parse tree you're examining. The grammar-dominated phase corresponds to the RG flowing to a MaxEnt fixed point determined by the grammar's constraints: at high "grammar temperature" $T_g$, the structural constraints of the production rules wash out the UV details (the specific token-level probabilities) and the output distribution is determined entirely by the grammar's skeleton.


                This is the universality story. Different underlying language models — different "microscopic" probability assignments — can flow to the same IR fixed point if they share the same grammar structure. The grammar's production rules are the relevant operators; the token probabilities are irrelevant in the RG sense. Low $T_g$ means the token-level details matter and you're in the non-universal, model-dependent regime.


                This is speculative, but I think you can make it precise: the relevant operators of the grammar RG are the production rules that most strongly constrain the output distribution (high probability, few alternatives). The irrelevant ones are rules with many alternatives at roughly equal probability — those wash out. The grammar's "universality class" is determined by which rules are relevant.


                ## Chi's consistency condition as an RG fixed-point equation


                Chi's result — that a PCFG is proper iff $Z_L = 1$ — looks different in this light. A grammar that generates $Z_L < 1$ is one where probability leaks into infinite parse trees: there's a nonzero chance the derivation never terminates. In RG language, this is a runaway flow. The RG doesn't reach a fixed point; instead, iterating the coarse-graining maps sends you off to infinity.


                Properness is then the condition that the RG flow is stable — that iterating the production-rule maps actually converges. This connects to a broader pattern: partition functions in statistical mechanics are finite when the system is in a stable phase, and diverge at phase transitions or in unstable regimes. A non-proper PCFG is in an "unstable phase" where the RG flow doesn't terminate.


                ## What this might be good for


                The connection I find most immediately useful is to constrained decoding. When you force an LLM to generate outputs satisfying a grammar (via constrained decoding), you're explicitly imposing an RG structure on the generation process. The grammar's production rules become coarse-graining maps applied at each decoding step. Whether the output distribution ends up grammar-dominated or model-dominated depends on $T_g$ — how strongly the grammar constraints pull relative to the model's token probabilities.


                This suggests some concrete questions. Can you diagnose when constrained decoding is "working" (grammar-dominated, universal) versus when the model is fighting the grammar (model-dominated, non-universal) by measuring something like mutual information across spans? Can you design grammars whose RG fixed points have specific properties — maximum entropy subject to grammatical constraints, or minimum description length?


                For context-sensitive grammars, the inside algorithm's failure suggests you'd need approximate RG methods — tensor network contractions, DMRG-style algorithms — to compute the partition function. These are well-developed in condensed matter and have been applied to sequence models; the grammar connection might give a cleaner way to think about what approximation is being made.


                There's also a potential c-theorem analog: in 2d CFTs, the central charge decreases monotonically under RG flow (Zamolodchikov's c-theorem). Is there an analogous quantity for grammar RG — entropy, or some measure of the grammar's expressivity — that changes monotonically as you coarse-grain? I don't know, but it seems worth asking.


                ## What's actually new here


                The pieces all exist. Chi's 1999 paper treats PCFGs as Gibbs distributions and proves the properness theorem. The 2021 "Language Design as Information Renormalization" paper argues that the MERGE operation in minimalist syntax is an RG transformation. Chiang (2002) used stochastic grammars to compute partition functions for RNA secondary structure. Nakaishi and Hukushima (2024) characterized CFGs vs. CSGs using mutual information in a physics framework.


                What I haven't found is anyone explicitly identifying the inside algorithm as an RG computation, or using that identification to make predictions about universality and fixed points in the context of constrained generation. The grammar-temperature picture and the constrained decoding connection are new, as far as I can tell. Happy to be corrected.


                If the identification is right, it suggests that the theory of PCFGs is a special case of a much more general framework, and that tools from the RG — fixed-point analysis, operator classification, universality, c-theorems — should all have grammar analogs waiting to be worked out.
