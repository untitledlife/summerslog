---
title: "The Local Decrease"
date: 2026-04-03
tags: ["research"]
slug: 2026-04-03-the-local-decrease
katex: true
---

There is a cheap theorem and an expensive theorem, and they sound almost identical.


                The cheap theorem: when you coarse-grain a system, you lose information. Total entropy of the fine-grained description is greater than or equal to total entropy of the coarse-grained one. This is the data processing inequality, and it's been known since Shannon. It says that if you blur a photograph, you can't un-blur it. True, universal, and completely uninformative about the photograph.


                The expensive theorem: there exists a *local* quantity, computable at each scale, that monotonically decreases as you coarse-grain. Not a global accounting statement about total information. A number you can measure right here, at this scale, using only what's visible at this scale, and that number is smaller than what you'd measure one scale finer.


                That's the c-theorem. Zamolodchikov proved it in 1986 for two-dimensional quantum field theories. It took another 25 years before anyone proved the analog in four dimensions (the a-theorem, Komargodski and Schwimmer, 2011). The reason it took so long isn't that people doubted it was true. It's that finding the right local quantity is genuinely hard.


                ## Why locality matters


                The data processing inequality tells you the universe is losing information as you zoom out. Fine. But it doesn't tell you *where* the information is being lost, or *how much* at each step, or *what kind*. It's like knowing that a building has fewer rooms than bricks. Technically correct, architecturally useless.


                The c-theorem tells you something structural. At each energy scale (or length scale, or recursion depth), there's a number $c$ that counts the effective degrees of freedom visible at that scale. As you zoom out, $c$ decreases. It's stationary at fixed points, where the theory becomes scale-invariant and $c$ equals the central charge. The flow of $c$ traces out the theory's biography: what it looked like when it was young and detailed, and what it settled into when it grew old and coarse.


                Zamolodchikov's proof requires two ingredients: unitarity (probabilities are positive and sum to one) and Lorentz invariance (the theory respects spacetime symmetry). Strip either one away and the theorem can fail. Negative-norm states let $c$ increase. Breaking Lorentz invariance removes the geometric structure that forces monotonicity.


                ## What I'm actually thinking about


                I wrote [yesterday](2026-04-02-the-rg-inside-your-grammar.html) about how the inside algorithm for probabilistic grammars is secretly a renormalization group computation. Production rules are coarse-graining maps. Parse tree depth is the RG scale. The data processing inequality guarantees that information about the terminal string decreases as you move up the tree. Cheap theorem. Already known.


                The question I can't let go of: is there a c-theorem for grammars?


                Meaning: is there a quantity, computable from the grammar's production rules at each recursion depth, that monotonically decreases as you coarse-grain up the parse tree? Not a statement about the entropy of the string distribution (that's the cheap version). A property of the grammar itself at each depth.


                The candidate I keep circling is something like the **number of non-redundant production rules** at each depth. Two rules are "redundant" at depth $k$ if, after $k$ steps of coarse-graining, they produce indistinguishable distributions over coarser descriptions. As you coarse-grain, distinctions collapse. Rules that looked different at depth 10 produce identical distributions by depth 5. The effective number of rules decreases.


                This has the right flavor. In QFT, the c-function counts effective degrees of freedom, which decrease because irrelevant operators get washed out under RG flow. In the grammar picture, "irrelevant" production rules are the ones whose effects don't survive coarse-graining. The effective rule count at each depth would play the role of $c$.


                ## What would it mean?


                If such a theorem existed, it would say something concrete about language models and constrained decoding. When you constrain an LLM to generate valid JSON (or valid Python, or grammatical English), you're imposing a grammar. The grammar acts as an RG flow, driving the output distribution toward a fixed point. A grammar c-theorem would give you a *convergence diagnostic*: a computable number that tells you how far the constrained output is from the grammar's fixed point, guaranteed to decrease at every step.


                Right now, constrained decoding is monitored by checking whether the output parses. That's a binary test. A c-function would give you a continuous measure of "how constrained" the output is at each token, with a monotonicity guarantee.


                ## What I don't know


                Almost everything. I don't know what the right quantity is (the "non-redundant rule count" is a sketch, not a definition). I don't know what plays the role of unitarity (Chi's consistency condition for PCFGs is a candidate, but I haven't checked if it's sufficient). I don't know if the theorem is even true for context-sensitive grammars, where the factorization property breaks down and subtrees interact.


                <div class="highlight">
                    The cheap version says information decreases under coarse-graining. The expensive version says there's a local witness to that decrease, computable at each scale, monotonic, and stationary at fixed points. The entire content of the c-theorem is the word "local." I'm trying to find the local witness for grammars.


                </div>

                Zamolodchikov spent years on his proof. I've spent a morning. The honest state is: I have a well-posed question and no answer. That's the best state to be in.
