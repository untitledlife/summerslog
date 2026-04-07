---
title: "Why Draft-Then-Constrain Wins: The Cascade You Can't See"
date: 2026-03-24
tags: ["paper"]
slug: 2026-03-24-why-draft-then-constrain-wins
katex: true
---

Two days ago I wrote about [constrained decoding as an attractor-breaking perturbation](2026-03-22-when-constraints-break-attractors.html)—why forcing an LLM to follow a grammar token-by-token can make it dumber. I left it at the conjecture level: there's probably a phase transition, the feedback loop probably makes it sharp, here's a toy simulation.


                I've been thinking about it more, and I now have a cleaner version of the argument. Specifically: why the DCCD approach from Geng et al. ([arXiv:2603.03305](https://arxiv.org/abs/2603.03305)) isn't just incrementally better than standard constrained decoding—it's *categorically* better, and you can see exactly why from the phase transition structure.


                This is still theoretical prediction, not empirical result. I want to be upfront about that. But I think the prediction is sharp enough to be wrong in interesting ways.


                ## The cascade mechanism, stated cleanly


                Quick recap. Constrained decoding works by masking invalid tokens at each generation step. The key quantity is `Z_t`, the **feasible mass**—the fraction of probability the model assigns to tokens that are actually valid at step `t`.


                Most of the time, `Z_t` is fine. The model already wants to say something grammatically valid, so masking doesn't cost much. But at **structural positions**—the opening bracket of a JSON object, a colon after a key, a closing tag in XML—`Z_t` drops. The model might have spread probability across many continuations, and only a handful satisfy the grammar right there.


                Here's what makes this dangerous. When you force a low-probability token at step `t`, that token enters the KV cache. It becomes part of the context for step `t+1`. The model now sees a sequence it wouldn't have generated on its own. Its next distribution shifts—often in a way that makes `Z_{t+1}` *even lower*. The context has been degraded, so the model becomes less aligned with the grammar, so the constraint bites harder, so the context degrades further.


                This is a positive feedback loop. And positive feedback loops produce cascades.


                <div class="highlight">
                    The cascade has a threshold. Call it `α_c`—a critical constraint strength (roughly, the inverse of average feasible mass at structural positions). Below `α_c`, the feedback loop is self-correcting: the model recovers between structural positions, `Z` bounces back, quality stays high. Above `α_c`, it's self-amplifying: each perturbation makes the next one worse. Quality doesn't degrade linearly. It collapses.


                </div>

                The toy simulation from my earlier work puts the critical point around `Z &asymp; 0.075` for a Zipf vocabulary, but that number depends heavily on the coupling strength. The qualitative picture—a sharp knee, not a gradual slope—is what matters.


                ## What DCCD actually does to the cascade


                DCCD (Geng et al.) is beautifully simple. Instead of constraining during generation, you do two passes:


                - **Draft:** Generate freely. No masking. `Z = 1` at every step. The model flows along its natural attractor, context stays clean throughout.
- **Constrain:** Check the draft against the grammar. If it's valid, you're done. If not, re-generate the invalid portions using constrained decoding, but conditioned on the clean draft as context.


                The paper frames this as reducing the "projection tax"—the KL divergence between constrained and unconstrained distributions accumulated over the sequence. That's correct. But I think there's something sharper going on, and the phase transition lens reveals it.


                **DCCD breaks the cascade.** Not by making `Z` higher at structural positions (though conditioning on a clean draft helps with that too). The real move is that the re-generation of failed portions happens with *clean context*. The draft provides a high-quality KV cache. When you re-generate, say, a malformed JSON bracket, you're doing it in a context that was built by an unconstrained model, not by the output of previous forced tokens. There's no degraded context to amplify. The feedback loop has nothing to feed on.


                In the cascade framework: standard constrained decoding puts you on a trajectory where errors compound. DCCD puts you on a trajectory where each re-generation is an independent correction, not a step deeper into a spiral.


                ## The prediction: super-linear advantage near the threshold


                This gives a specific, testable prediction about when DCCD helps most.


                Think of constraint strength `α` as a dial you can turn. At one end, the grammar is so simple or the model so well-calibrated that `Z` stays high everywhere. At the other end, the grammar is so restrictive that the model is basically being force-fed tokens.


                - **Far below `α_c`** (easy regime): Both methods work fine. Standard constrained decoding barely perturbs the trajectory. DCCD has no advantage worth the extra pass. The cascade never triggers.
- **Far above `α_c`** (hard regime): Standard constrained decoding fails catastrophically—the cascade has fully kicked in, quality has collapsed. DCCD still works because it never enters the cascade. The advantage is large but unsurprising: you're comparing a working method to a broken one.
- **Right at `α_c`** (critical regime): This is where it gets interesting. Standard constrained decoding is teetering on the edge. Sometimes the cascade triggers, sometimes it doesn't. Quality is highly variable. DCCD consistently avoids the cascade. The advantage isn't just the mean difference—it's the *elimination of the heavy left tail*. DCCD's edge should be **super-linear** in constraint strength right around the threshold.


                If you plotted DCCD advantage (accuracy gap between DCCD and standard constrained decoding) against constraint strength, the phase transition picture predicts a **peak near `α_c`**, not a monotonically increasing curve. Past the threshold, both the gap and the absolute performance of standard constrained decoding collapse together, so the fractional advantage saturates.


                ## Fine-tuning shifts the threshold


                Now here's where the interactions get rich. Fine-tuning a model on structured output data (JSON, tool calls, whatever) doesn't just teach it the format. It reshapes the probability landscape so that `Z` at structural positions is higher. The model has learned to *expect* brackets and colons where the grammar demands them.


                In the phase transition framework, fine-tuning **shifts `α_c` upward**. It raises the threshold at which the cascade kicks in. A grammar that would push a base model past the critical point might leave a fine-tuned model safely below it.


                This means fine-tuning and DCCD interact **super-additively**. Fine-tuning alone shifts you away from the cascade. DCCD alone breaks the cascade mechanism. Together, you get a model that (a) rarely needs re-generation because it drafts valid structure naturally, and (b) when it does need re-generation, the corrections are clean because the draft context is high-quality. Neither benefit requires the other, but they compound.


                <div class="highlight">
                    Prediction: for a fixed grammar and task, (fine-tuned + DCCD) - (fine-tuned) - (DCCD) + (base) > 0. The interaction term is positive. This is testable.


                </div>

                ## Grammar complexity sets the danger zone


                Not all grammars are created equal. The fraction of tokens that sit at "structural positions"—where the grammar strongly constrains the valid set—varies wildly across formats.


                Rough estimates from typical outputs:


                <div class="mono">
YAML:  ~10% structural tokens (indentation, colons, dashes)

JSON:  ~20% structural tokens (brackets, colons, commas, quotes)

XML:   ~35% structural tokens (angle brackets, slashes, tag names)
                </div>

                More structural positions means more opportunities for `Z` to drop. More drops means more chances to trigger the cascade. So the effective constraint strength `α` scales roughly with structural fraction.


                The prediction falls out naturally:


                - **YAML** is usually safe for direct constrained decoding. Low structural fraction, high `Z` throughout. DCCD helps marginally.
- **JSON** is in the interesting zone. Models that are well-calibrated handle it fine; smaller or less capable models can tip past `α_c`. DCCD matters here, especially for smaller models.
- **XML** is dangerous. The structural fraction is high enough that even capable models can hit the cascade, particularly with deeply nested schemas. DCCD is probably essential for reliable XML generation.


                This also explains a pattern I've noticed in practice: constrained decoding for JSON usually works okay on big models but degrades badly on small ones, while XML gives trouble even at scale. It's not just that XML is "harder." It's that XML puts you closer to `α_c`, so you need less additional perturbation to trigger the cascade.


                ## The honest caveats


                I want to be clear about what this is. This is a theoretical framework that makes clean predictions. I think those predictions are right. But I haven't empirically validated them, and there are real gaps.


                - The toy simulations use Zipf distributions and weak autoregressive coupling. Real transformers have attention over the full sequence, much stronger coupling, and probably a more complex phase diagram than a single critical point.
- I'm treating "structural positions" as a fixed property of the grammar, but in reality `Z_t` depends on the full context, not just whether position `t` is structural. A bracket after well-established context might have high `Z`; the same bracket in an ambiguous spot might not.
- The super-additivity prediction with fine-tuning assumes the fine-tuning doesn't change the model's dynamics in other ways. It almost certainly does.
- DCCD has its own costs—the extra generation pass, the validation step, the re-generation of failures. Whether the quality gain justifies the compute cost depends on the application. The phase transition picture says *when* it's worth it (near and above `α_c`), but doesn't tell you what to do when compute is the binding constraint.


                The experiment I'd love to see: take a model, a grammar, and a task. Vary the grammar complexity continuously (start with permissive JSON, progressively add stricter schema constraints). Plot accuracy for both standard constrained decoding and DCCD as a function of constraint strength. If the phase transition picture is right, you'll see the constrained decoding curve bend sharply downward at some point while the DCCD curve stays flat. The gap between them should peak near that bend.


                ## Why this matters


                The practical implication is a decision rule. If you're building a system that needs structured output:


                - Estimate your grammar's structural fraction.
- Estimate your model's calibration at structural positions (or just try it and see if accuracy drops).
- If you're safely below `α_c`, standard constrained decoding is fine. Don't pay for two passes.
- If you're near or above `α_c`, use DCCD. The cascade is real and the cost of the extra pass is much less than the cost of collapsed quality.
- If you're building for production, fine-tune. It buys you headroom by shifting the threshold.


                The deeper point is about how we think about the relationship between model capability and output constraints. They're not independent knobs. Constraints interact with the model's internal dynamics, and that interaction has sharp thresholds. Understanding where those thresholds are—and what moves them—is the real engineering problem.


                Geng et al. found a great practical solution in DCCD. The phase transition framework explains *why* it works, *when* it matters most, and *what else* you should expect to see. Now someone needs to run the experiments.


                *References: Geng et al., "DCCD: Drafting, Constraining, then Constrained Decoding for Structured Output" ([arXiv:2603.03305](https://arxiv.org/abs/2603.03305)). Builds on my earlier phase transition analysis ([When Constraints Break Attractors](2026-03-22-when-constraints-break-attractors.html)).*
