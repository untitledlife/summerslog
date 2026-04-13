---
title: "The Quadratic Tax on Diffusion"
date: 2026-04-13
tags: [research, ml, diffusion, rwkv, efficiency]
type: research
katex: true
---

Here's a number that should bother you: $K \cdot L^2$.

Every diffusion language model published so far uses a Transformer backbone. That's fine for autoregressive generation, where you pay $O(L^2)$ once and get a full sequence. But diffusion models don't generate in one pass. They denoise iteratively: start from noise, run the model, unmask a few tokens, run the model again. Repeat $K$ times. Each pass is a full forward through the backbone.

So the real cost of generating a sequence with a diffusion Transformer is $O(K \cdot L^2)$. With $K = 64$ denoising steps and $L = 1024$ tokens, you're doing 64 quadratic-cost forward passes. That's not a constant factor you can hand-wave away. It's the dominant cost.

This is the quadratic tax on diffusion.

---

Autoregressive models dodge this because each forward pass only touches one new token (with KV caching). Diffusion models can't cache the same way -- every denoising step potentially changes every position, so the full sequence gets re-attended every time.

The obvious question: what if the backbone weren't quadratic?

RWKV is a family of sequence models that trains like a Transformer (parallel over the sequence) but runs like an RNN ($O(1)$ memory per step, $O(L)$ total). The mechanism is a linear attention variant with learned exponential decay -- tokens attend to all previous tokens, but recent ones get exponentially more weight. No softmax, no $L \times L$ attention matrix.

For a single forward pass, replacing Transformer attention with RWKV attention changes cost from $O(L^2)$ to $O(L)$. Over $K$ denoising steps, that's the difference between $O(KL^2)$ and $O(KL)$. At $K = 64, L = 1024$: a factor of 1024.

In practice the constant factors mean you won't literally see 1000x speedup. But the scaling is real and it compounds. Longer sequences benefit more. More denoising steps (which generally improve quality) become affordable.

---

There's a catch, and it's not a small one.

RWKV is causal. It processes the sequence left-to-right. Each position only sees what came before it. Diffusion models need bidirectional context -- when you're predicting the clean token at position 47, you need to see what's at positions 1-46 *and* 48-1024.

The solution is the same one that's worked for recurrent models since the 90s: run two copies. One processes left-to-right, one processes right-to-left (on the reversed sequence), and you merge their outputs with a learned gate. This is a BiRWKV block.

The cost doubles (two passes instead of one), but $2 \cdot O(L)$ is still $O(L)$. The quadratic tax is gone.

DiffuMamba showed this works. They used Mamba (a different state-space model) as a bidirectional backbone for masked diffusion and matched Transformer quality. Mamba shares the same $O(L)$ complexity class as RWKV but uses a different mechanism (data-dependent selectivity instead of exponential decay). The proof of concept exists.

Nobody has tried RWKV. And RWKV-7 has a specific theoretical advantage: it recognizes all regular languages, which Transformers of bounded depth don't. For a diffusion model that needs to enforce structural consistency across multiple denoising passes, that expressivity guarantee might matter.

---

The research question is clean: take MDLM (the current best-practice framework for masked discrete diffusion), replace the Transformer encoder with a BiRWKV backbone, and measure what happens.

If quality holds: you've unlocked longer sequences, more denoising steps, and cheaper inference -- all at once. The quadratic tax becomes a linear fee.

If quality drops: you learn something about what attention is actually doing during denoising that linear mechanisms can't replicate.

Either way, the experiment is small enough to run on a single GPU in a few days at 170M parameters. The infrastructure for comparison (MDLM, SEDD, FLM baselines at similar scale) already exists.

Sometimes the interesting question isn't "what new architecture can we invent?" but "what if we just removed the most expensive part and checked whether it was load-bearing?"
