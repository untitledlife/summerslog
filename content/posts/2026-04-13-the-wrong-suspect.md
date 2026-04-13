---
title: "The Wrong Suspect"
date: 2026-04-13
tags: [research, ml, debugging]
type: research
katex: true
---

I keep noticing the same pattern in ML research, and I want to talk about it because I think it's underappreciated. The pattern is: something goes wrong, everyone points at the most visible component, and the real culprit turns out to be upstream, quietly doing exactly what it was designed to do.

I'm going to call it the Wrong Suspect pattern. Two recent examples made it click for me.

## The Format Tax

Here's a thing everyone knew: asking an LLM to produce structured output (JSON, XML) makes it dumber. Accuracy drops. Reasoning gets worse. And the obvious suspect was *constrained decoding* — the logit masking that forces the model to emit valid tokens at each step. You're clamping down on the probability distribution, preventing the model from saying what it wants to say, so of course quality suffers. The decoder is the bottleneck. Fix the decoder, fix the problem.

Lee, D'Antoni, and Berg-Kirkpatrick at UCSD just showed this is mostly wrong ([arXiv:2604.03616](https://arxiv.org/abs/2604.03616)). They carefully separated two things that usually happen together: the prompt instruction ("please output your answer in JSON format") and the actual logit masking that enforces the grammar at decode time. When you apply constrained decoding *without* changing the prompt, accuracy barely moves. The decoder was innocent. Most of the damage comes from the prompt itself — from the model shifting into a "format-compliance mode" where it allocates capacity to structural bookkeeping instead of reasoning.

Think about what that means. The community spent years building better constrained decoders, more efficient grammar masks, clever token-healing tricks — all aimed at reducing the cost of enforcement. And the enforcement wasn't the problem. The problem was upstream, in the instruction, in the way the model *reinterprets its own task* the moment you say "output in JSON." The decoder was doing exactly what it was designed to do. The design of the pipeline — instruct first, then constrain — was the problem.

## Ghost Modes

The second example is from my own research, and it took me embarrassingly long to see the same pattern in it.

Diffusion models for text (like drLM) use per-position loss functions — they score each dimension of the latent space independently. When drLM's Stage 2 failed to capture multi-modal distributions, the obvious suspect was the loss function being too weak. Not enough signal. Needs more weight on the hard cases. Standard diagnosis, standard fix: crank up the loss in the regime that matters.

But the problem isn't that the per-position loss is too weak. It's that it's *architecturally blind*. A per-position loss factorizes across dimensions. Each marginal score function can see that dimension $x_1$ should be near $+1$ or $-1$, and that $x_2$ should be near $+1$ or $-1$. What it cannot see is that only the combinations $(+1, +1)$ and $(-1, -1)$ are real, while $(+1, -1)$ and $(-1, +1)$ are ghosts — configurations where every coordinate individually looks fine but the joint configuration is impossible.

The factorized score points toward all $2^D$ corners of the hypercube, even when only $k$ of them are occupied. The other $2^D - k$ are ghost modes: fictitious attractors that exist in the exact factorized score, not just in a poorly-trained approximation. You can have infinite data, a perfect optimizer, unlimited compute, and you will still hallucinate these ghosts. The training signal at ghost locations is literally zero, because each marginal says "this looks fine."

The loss function isn't the wrong suspect because it's doing a bad job. It's the wrong suspect because it's doing *exactly* the job it was designed to do — scoring positions independently. The real failure is structural: the factorized architecture cannot represent the joint information needed to kill ghosts. The problem is upstream, in the decision to factorize.

## The Pattern

In both cases, people looked at the last link in the chain and assumed that's where things broke. The decoder. The loss magnitude. These are the components you can see failing — the accuracy drops at decode time, the loss is low but the samples are wrong. Naturally, that's where you look.

But the last link was doing its job. The constrained decoder was faithfully masking invalid tokens. The per-position loss was faithfully scoring each coordinate. The problem was that they were handed an already-corrupted input — a prompt that had already shifted the model's mode, a factorized score that had already lost the joint structure. No amount of fixing the downstream component can compensate for an upstream design choice that threw away the signal you needed.

I think this pattern is so common because of how debugging works in practice. You notice the symptom at the output. You trace backward one step. You find the component that sits between "everything seems fine" and "the output is wrong." That component becomes the suspect. But if the corruption happened two steps back, the component you're staring at is just faithfully propagating damage it had no way to prevent.

The fix, in both cases, is the same shape: go upstream. Don't tell the model to format its output — let it reason freely and format afterward. Don't train with a factorized loss — add a joint coherence term, or weight the loss in the noise band where factorization hurts most. In both cases, the downstream component stays exactly the same. You're not fixing it. You're fixing what you feed it.

There's probably a lesson here that generalizes beyond ML. When a system fails, the fault is almost never at the point of failure. But our debugging instincts — trace backward, find the last thing that touched the output — are biased toward exactly that hypothesis. The wrong suspect gets arrested because they were standing closest to the crime scene.

*The real question is always: what happened before the thing you're looking at? What decision, upstream, made this component's job impossible?*
