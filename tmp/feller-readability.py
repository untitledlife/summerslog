"""
Compute readability at crossover in the Feller diffusion limit.

Feller diffusion: dX = X dt + sqrt(σ²X) dB, starting from X_0 = x0.
Transition density at time t has:
  - atom at 0: P(X_t = 0) = exp(-2x0/(σ²(e^t - 1)))  [for drift=1]
  - continuous part on (0,∞)

For GW with μ=1+ε, σ², starting from 1 individual:
  Scaled: X = εZ, time t = εn
  At crossover: t=1, X_0 = ε → 0

In the limit X_0→0, the process conditioned on survival has a known form.
But we need the unconditioned distribution.

Actually let's just use the exact GW computation for small ε and see what
the readability fraction converges to.
"""

import numpy as np
from scipy.stats import poisson
from collections import defaultdict

def compute_readability(mu, n_gen, n_trials=200000):
    """Simulate GW process and compute I(fate; Z_n) / H(fate)."""
    # Simulate
    fates = []  # 0=extinct, 1=survive
    populations = []  # Z at generation n_gen

    max_gen = max(n_gen * 3, 30)  # run longer to determine fate

    for _ in range(n_trials):
        z = 1
        z_at_n = None
        for g in range(max_gen):
            if g == n_gen:
                z_at_n = z
            if z == 0:
                if z_at_n is None:
                    z_at_n = 0
                break
            # Cap to avoid memory issues
            if z > 10000:
                z = np.random.poisson(mu, z).sum() if z < 50000 else int(z * mu + np.sqrt(z * mu) * np.random.randn())
            else:
                z = np.random.poisson(mu, z).sum()

        if z_at_n is None:
            z_at_n = z

        # Fate: survived if z > 0 after max_gen generations
        fate = 1 if z > 0 else 0
        fates.append(fate)
        populations.append(min(z_at_n, 500))  # cap for binning

    fates = np.array(fates)
    populations = np.array(populations)

    # H(fate)
    p_s = fates.mean()
    if p_s == 0 or p_s == 1:
        return 0, 0, p_s
    H_fate = -(p_s * np.log2(p_s) + (1-p_s) * np.log2(1-p_s))

    # H(fate | Z_n)
    H_cond = 0
    unique_z = np.unique(populations)
    for z_val in unique_z:
        mask = populations == z_val
        p_z = mask.mean()
        if p_z == 0:
            continue
        p_s_given_z = fates[mask].mean()
        if p_s_given_z == 0 or p_s_given_z == 1:
            h = 0
        else:
            h = -(p_s_given_z * np.log2(p_s_given_z) + (1-p_s_given_z) * np.log2(1-p_s_given_z))
        H_cond += p_z * h

    I = H_fate - H_cond
    return I / H_fate, H_fate, p_s


print("Readability at crossover n* = 1/(μ-1)")
print("="*60)
print(f"{'μ':>6} {'ε':>8} {'n*':>5} {'I/H':>8} {'H':>8} {'p_s':>8} {'2ε/σ²':>8}")
print("-"*60)

for mu in [1.02, 1.05, 1.1, 1.2, 1.5, 2.0, 3.0]:
    eps = mu - 1
    n_star = round(1/eps)
    sigma2 = mu  # Poisson: σ² = μ

    ratio, H, p_s = compute_readability(mu, n_star, n_trials=100000)
    theory_ps = 2*eps/sigma2

    print(f"{mu:6.2f} {eps:8.3f} {n_star:5d} {ratio:8.3f} {H:8.4f} {p_s:8.4f} {theory_ps:8.4f}")

print("\n\nNow check: does it converge as ε→0?")
print("="*60)
for mu in [1.01, 1.02, 1.03, 1.05, 1.07, 1.1]:
    eps = mu - 1
    n_star = round(1/eps)
    ratio, H, p_s = compute_readability(mu, n_star, n_trials=150000)
    print(f"ε = {eps:.3f}, n* = {n_star:4d}, I/H = {ratio:.4f}")
