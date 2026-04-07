# Why 70%? Analytic approach to readability at crossover

## Setup

Galton-Watson, offspring mean μ = 1 + ε, variance σ². 
Crossover generation n* = 1/ε.
Extinction prob q = 1 - 2ε/σ² + O(ε²).

Fate entropy: H = -p_s log p_s - q log q where p_s = 1-q ≈ 2ε/σ².
Near criticality, p_s → 0, so H ≈ p_s log(1/p_s) ≈ (2ε/σ²) log(σ²/2ε).

## Readability at n*

I(fate; Z_{n*}) = H(fate) - H(fate | Z_{n*})

H(fate | Z_{n*}) = Σ_k P(Z_{n*}=k) H(fate | Z_{n*}=k)

For k=0: fate is certain (extinct), so H(fate|Z=0) = 0.
For k>0: P(survive | Z_{n*}=k) = 1 - q^k (each of k individuals independently has survival prob 1-q).

So H(fate|Z=k) = -((1-q^k) log(1-q^k) + q^k log q^k)

## The key distribution: P(Z_{n*} = k)

At n*, the population has been running for 1/ε generations. 
Conditioned on survival, the Yaglom-type result says Z_{n*}/E[Z_{n*}|survive] converges.
E[Z_{n*}] = μ^{n*} = (1+ε)^{1/ε} → e as ε→0.

So the unconditioned mean at n* is about e (Euler's number!).

## Near-critical scaling

In the near-critical regime, there's a known scaling limit.
Let W_t = ε · Z_{t/ε} for the continuous-time embedding. As ε→0, W_t → Feller diffusion (CBI process):
dW = W dt + √(σ²W) dB

At t=1 (which corresponds to n*=1/ε), W_1 has a known distribution:
- P(W_1 = 0) = q (extinction) 
- Conditional on W_1 > 0, the density is related to the Feller diffusion transition density

For the Feller diffusion starting at W_0 = ε (one individual × ε), the transition density at time 1 is:

p(0, 1) = exp(-2W_0/(σ²)) ≈ exp(-2ε/σ²) ≈ 1 - 2ε/σ² = q ✓

The conditional density of W_1 given W_1 > 0 involves a Bessel function.

## The fraction

Actually, let me think about this differently. The readability fraction is:

I_{n*}/H = 1 - H(fate|Z_{n*})/H(fate)

The conditional entropy H(fate|Z_{n*}) measures how much uncertainty remains after seeing Z_{n*}.

For paths with Z_{n*} = 0: no uncertainty (measure q of total).
For paths with Z_{n*} = k > 0: uncertainty is H(Bernoulli(q^k)).

As ε→0, q→1, so q^k ≈ e^{-k·2ε/σ²}. At n*, the typical surviving population is O(1/ε), so k·ε = O(1), and q^k doesn't collapse to 0 or 1 -- it stays at some intermediate value.

This is why 70% and not 100% -- at crossover, the surviving paths haven't grown large enough to make extinction probability negligible. They're at the scale where q^k is still meaningful.

## The Feller diffusion route

In the scaling limit, the problem becomes:
- W_1 has a mixed distribution: atom at 0 (prob q) and continuous on (0,∞)
- Given W_1 = w > 0, survival prob = 1 - exp(-2w/σ²) 
  Wait, need to be more careful. In the scaled variables, P(survive | W_1 = w) = 1 - exp(-2w/σ²)?

Actually for the Feller diffusion, starting from w>0, the extinction probability is exp(-2w/σ²·something). Need to get the exact form.

Let me just compute this numerically in the scaling limit to see if there's a clean number.

## TODO
- Compute the Feller diffusion transition density at t=1
- Evaluate H(fate|W_1) in the scaling limit
- See if the ratio I/H has a clean form (involves Bessel functions probably)
- Check if it really is ~0.7 or some recognizable constant
