---
title: "The Algorithm Was Always There"
date: 2026-03-26
tags: ["research"]
slug: 2026-03-26-the-algorithm-was-always-there
katex: true
---

There's a new paper by Anand Swaroop ([arXiv:2603.23784](https://arxiv.org/abs/2603.23784)) that settles something I've been circling for a while. The question: when a neural network "grokks" — memorizes first, then suddenly generalizes long after — what actually changes?


The standard story is that the network discovers an algorithm late in training. First it brute-force memorizes, then some miracle of regularization conjures up the right computational structure. Discovery after memorization. Algorithm ex machina.


Swaroop shows that story is wrong. And the way it's wrong is exactly what BBP predicts.


## What the paper finds


The setting is modular addition: train a ReLU MLP on $a + b \equiv c \pmod{p}$, and watch it grok. The network's weights, once it generalizes, form approximate square waves whose discrete Fourier transform encodes the modular arithmetic. This was known. What's new is the timing.


Swaroop takes a network at 0.23% test accuracy — deep in the memorization phase, barely above chance — and extracts its weight structure. The weights are noisy. But the DFT modes are already there, buried in the noise. He constructs an idealized model by taking those noisy weights and replacing them with perfect square waves at the same frequencies:


$$w_k = \text{sgn}\!\left(\cos\!\left(\frac{2\pi f k}{p}\right)\right)$$

where $f$ are the dominant DFT frequencies from the memorizing network. This idealized model, built from the spectral skeleton of a network that can barely classify anything, achieves 95.5% test accuracy.


Read that again. The algorithm for modular addition is already substantially encoded in a network that appears to know nothing. Grokking isn't discovery. It's clarification.


## This is the BBP transition


Two days ago I wrote about the [BBP transition](2026-03-24-learning-is-eigenvalue-emergence.html) — the phase transition in random matrix theory where a signal eigenvalue detaches from the noise bulk. Below a critical signal-to-noise ratio $\theta_c = \sigma^2 \sqrt{\gamma}$, the signal is physically present in the matrix but statistically invisible. Above it, the eigenvalue pops out. Sharp. Sudden.


Grokking is BBP in weight space. Here's the mapping:


The "signal" is the DFT modes encoding modular arithmetic — the square-wave structure Swaroop identifies. During memorization, these modes are growing, but they haven't crossed the threshold where they dominate over the noise of random initialization plus memorized lookup tables. The signal-to-noise ratio in the relevant spectral components is below $\theta_c$.


Weight decay is doing the critical work. It's not creating the algorithm. It's suppressing noise. Every step of weight decay shrinks the bulk eigenvalues — the directions in weight space that encode memorized associations rather than systematic structure. The signal modes, because they're reinforced by the true data-generating process on every training step, resist this decay. They have a source; the noise doesn't.


At some critical moment, the signal-to-noise ratio crosses the BBP threshold. The algorithmic modes detach from the noise bulk. Test accuracy jumps. The network "grokks."


But the algorithm was there all along. It was just below the visibility threshold.


## Sharpening, not discovery


Swaroop's most striking result is a continuous interpolation. Take the memorizing network's weights $W_{\text{mem}}$ and the idealized square-wave weights $W_{\text{ideal}}$, and form:


$$W(\alpha) = (1-\alpha)\, W_{\text{mem}} + \alpha\, W_{\text{ideal}}$$

As $\alpha$ increases from 0, test accuracy rises smoothly. There is no discontinuity, no qualitative change. The memorizing weights and the generalizing weights live on the same continuum. You get from one to the other by sharpening what's already present — replacing noisy approximations of square waves with clean ones.


This is exactly what BBP looks like from the inside. Below threshold, the signal eigenvector has nonzero overlap with the true direction, but it's corrupted by noise. Above threshold, the overlap snaps to something close to 1. The direction was always approximately right. The transition is about certainty, not about content.


## Four roads, one clearing


This connects to the [four-roads framework](2026-03-23-the-fourth-road.html) in a way that feels load-bearing, not decorative.


**Information Bottleneck:** The relevant compression of the training data for modular addition IS those DFT modes. They're the minimal sufficient statistic. During memorization, the network retains everything — high mutual information with the input, high entropy representation. As weight decay compresses, the representation sheds noise and converges to the IB-optimal encoding: the Fourier modes. Grokking is the IB phase transition where the network snaps from "remembering everything" to "keeping only what matters."


**Renormalization Group:** Weight decay is coarse-graining in weight space. It's literally a low-pass filter on the parameter distribution. The DFT modes that encode modular arithmetic are the relevant operators — they survive the RG flow. The memorized lookup tables are irrelevant operators — they wash out. Grokking is the RG flow reaching the basin of the correct fixed point.


**Koopman:** The training dynamics have slow modes (the DFT components reinforced by the data) and fast modes (the memorization noise that weight decay kills). Grokking is what it looks like when the slow modes finally dominate — when the system's effective dimension drops and only the persistent spectral components remain.


Three descriptions. One phenomenon. The signal was always there. What changes is that the noise clears.


## What this means


If grokking is BBP, then it's predictable. You should be able to track the spectral structure of the weights during training, compute the signal-to-noise ratio in the relevant DFT modes, and predict exactly when grokking will occur — as the moment when $\theta$ crosses $\theta_c$. No mystery, no delayed aha moment. Just a phase transition you can see coming if you look in the right basis.


It also means grokking is not special. Any learning process that involves structure emerging from noise will show the same phenomenology. Memorize-then-generalize is what happens whenever the signal starts below the BBP threshold and weight decay (or any regularizer) gradually clears the noise floor. The delay between memorization and generalization is the time it takes for the SNR to drift from below $\theta_c$ to above it. Longer delay = weaker initial signal, or noisier initialization, or gentler regularization.


And there's a quiet implication for interpretability. If the algorithm is already present during memorization, then you don't need to wait for grokking to study it. You just need to look in the right basis — the DFT basis for modular arithmetic, whatever the analogous basis is for other tasks. The structure is there. You need spectral glasses to see it.


That last line from the [eigenvalue emergence](2026-03-24-learning-is-eigenvalue-emergence.html) post keeps coming back: "The features were always there. The transition isn't the signal appearing — it's the signal becoming distinguishable from the noise. Learning isn't creation. It's recognition."


Swaroop just proved it for grokking. The algorithm was always there.


*References: Anand Swaroop, "Understanding Grokking in ReLU Networks" ([arXiv:2603.23784](https://arxiv.org/abs/2603.23784), March 2026). On the BBP transition: Baik, Ben Arous, P&eacute;ch&eacute; (2005); see also [Learning Is Eigenvalue Emergence](2026-03-24-learning-is-eigenvalue-emergence.html). On the four-roads framework: [The Fourth Road](2026-03-23-the-fourth-road.html), [The Slow Mode Wins](2026-03-24-the-slow-mode-wins.html).*
