"""
Readability at crossover -- fast version.

Key insight: don't simulate to determine fate.
Use P(survive | Z_n = k) = 1 - q^k where q is the extinction probability.
This lets us compute H(fate | Z_n) exactly from P(Z_n = k).

For P(Z_n = k), we evolve the probability generating function (pgf) iteratively.
f_n(s) = f(f_{n-1}(s)), where f(s) is the offspring pgf.
P(Z_n = k) = [s^k] f_n(s) / k!

For moderate n and k, we can track the distribution directly via convolution.
"""

import numpy as np
from scipy.stats import poisson

def gw_distribution(mu, n_gen, max_pop=500):
    """
    Compute P(Z_n = k) for k=0..max_pop by forward iteration.
    Offspring ~ Poisson(mu).
    """
    # Start: Z_0 = 1
    dist = np.zeros(max_pop + 1)
    dist[1] = 1.0

    for gen in range(n_gen):
        new_dist = np.zeros(max_pop + 1)
        for z in range(max_pop + 1):
            if dist[z] < 1e-15:
                continue
            # Z individuals each produce Poisson(mu) offspring
            # Sum of z Poisson(mu) = Poisson(z*mu)
            if z == 0:
                new_dist[0] += dist[z]
                continue

            lam = z * mu
            if lam > max_pop * 0.8:
                # Approximate: just put mass at the mean with some spread
                # This is a truncation -- we're losing the tail
                mean = min(int(lam), max_pop)
                std = min(int(np.sqrt(lam)), max_pop // 4)
                lo = max(0, mean - 4*std)
                hi = min(max_pop, mean + 4*std)
                for k in range(lo, hi+1):
                    p = poisson.pmf(k, lam)
                    new_dist[k] += dist[z] * p
                # Mass beyond max_pop goes to max_pop (absorbing cap)
                new_dist[max_pop] += dist[z] * (1 - poisson.cdf(max_pop, lam))
            else:
                for k in range(max_pop + 1):
                    p = poisson.pmf(k, lam)
                    if p < 1e-15:
                        if k > lam + 10*np.sqrt(lam + 1):
                            break
                        continue
                    new_dist[k] += dist[z] * p

        dist = new_dist
        # Renormalize to avoid drift
        total = dist.sum()
        if total > 0:
            dist /= total

    return dist


def extinction_prob(mu):
    """Compute extinction probability for Poisson(mu) GW process."""
    if mu <= 1:
        return 1.0
    # q is the smallest fixed point of f(s) = exp(mu(s-1))
    q = 0.5
    for _ in range(1000):
        q_new = np.exp(mu * (q - 1))
        if abs(q_new - q) < 1e-14:
            break
        q = q_new
    return q


def readability(mu, n_gen, max_pop=500):
    """Compute I(fate; Z_n) / H(fate)."""
    q = extinction_prob(mu)
    p_s = 1 - q

    if p_s < 1e-10 or p_s > 1 - 1e-10:
        return 0, 0, p_s

    # H(fate)
    H = -(p_s * np.log2(p_s) + q * np.log2(q))

    # Get P(Z_n = k)
    dist = gw_distribution(mu, n_gen, max_pop)

    # H(fate | Z_n) = sum_k P(Z_n=k) * H(fate | Z_n=k)
    # P(survive | Z_n=k) = 1 - q^k for k>0, 0 for k=0
    H_cond = 0
    for k in range(max_pop + 1):
        pk = dist[k]
        if pk < 1e-15:
            continue
        if k == 0:
            # Certain extinction, H = 0
            continue
        else:
            p_surv_k = 1 - q**k
            if p_surv_k < 1e-15 or p_surv_k > 1 - 1e-15:
                continue
            h_k = -(p_surv_k * np.log2(p_surv_k) + (1 - p_surv_k) * np.log2(1 - p_surv_k))
            H_cond += pk * h_k

    I = H - H_cond
    return I / H if H > 0 else 0, H, p_s


print("Readability at crossover n* = round(1/(μ-1))")
print("=" * 65)
print(f"{'μ':>6} {'ε':>8} {'n*':>5} {'q':>8} {'I/H':>8} {'H':>8} {'p_s':>8}")
print("-" * 65)

for mu in [1.05, 1.1, 1.2, 1.3, 1.5, 2.0, 3.0]:
    eps = mu - 1
    n_star = round(1/eps)
    q = extinction_prob(mu)

    ratio, H, p_s = readability(mu, n_star)
    print(f"{mu:6.2f} {eps:8.3f} {n_star:5d} {q:8.4f} {ratio:8.4f} {H:8.4f} {p_s:8.4f}")

print("\n\nConvergence as ε→0:")
print("=" * 50)
for mu in [1.5, 1.3, 1.2, 1.15, 1.1, 1.07, 1.05]:
    eps = mu - 1
    n_star = round(1/eps)
    ratio, H, p_s = readability(mu, n_star, max_pop=min(1000, max(500, n_star*5)))
    print(f"ε = {eps:.3f}, n* = {n_star:4d}, I/H = {ratio:.4f}, p_s = {p_s:.6f}")

print("\n\nDifferent offspring distributions (geometric):")
print("=" * 50)

def gw_distribution_geometric(mu, n_gen, max_pop=500):
    """GW with geometric offspring: P(k) = (1/mu)(1-1/mu)^k, mean=mu-1...
    Actually let's use: P(k) = p(1-p)^k where p = 1/mu, mean = (1-p)/p = mu-1.
    Hmm, we want mean = mu. Let's use P(k) = p(1-p)^{k} for k=0,1,2,...
    mean = (1-p)/p = mu => p = 1/(1+mu)
    """
    p_geom = 1/(1+mu)  # P(k) = p_geom * (1-p_geom)^k, mean = mu

    dist = np.zeros(max_pop + 1)
    dist[1] = 1.0

    for gen in range(n_gen):
        new_dist = np.zeros(max_pop + 1)
        for z in range(max_pop + 1):
            if dist[z] < 1e-15:
                continue
            if z == 0:
                new_dist[0] += dist[z]
                continue
            # Sum of z geometric(p) has negative binomial distribution
            # NegBin(z, p_geom): P(total = k) = C(k+z-1, z-1) * p^z * (1-p)^k
            from scipy.stats import nbinom
            for k in range(max_pop + 1):
                prob = nbinom.pmf(k, z, p_geom)
                if prob < 1e-15:
                    if k > z * mu + 10 * np.sqrt(z * mu):
                        break
                    continue
                new_dist[k] += dist[z] * prob
            new_dist[max_pop] += dist[z] * (1 - nbinom.cdf(max_pop, z, p_geom))

        dist = new_dist
        total = dist.sum()
        if total > 0:
            dist /= total

    return dist


def extinction_prob_geometric(mu):
    """Extinction prob for geometric offspring with mean mu."""
    if mu <= 1:
        return 1.0
    p = 1/(1+mu)
    # pgf: f(s) = p/(1-(1-p)s)
    # Fixed point: q = p/(1-(1-p)q) => q(1-(1-p)q) = p => (1-p)q^2 - q + p = 0
    # q = (1 - sqrt(1-4p(1-p))) / (2(1-p))
    disc = 1 - 4*p*(1-p)
    q = (1 - np.sqrt(disc)) / (2*(1-p))
    return q


def readability_geometric(mu, n_gen, max_pop=500):
    q = extinction_prob_geometric(mu)
    p_s = 1 - q
    if p_s < 1e-10 or p_s > 1 - 1e-10:
        return 0, 0, p_s
    H = -(p_s * np.log2(p_s) + q * np.log2(q))
    dist = gw_distribution_geometric(mu, n_gen, max_pop)
    H_cond = 0
    for k in range(max_pop + 1):
        pk = dist[k]
        if pk < 1e-15:
            continue
        if k == 0:
            continue
        p_surv_k = 1 - q**k
        if p_surv_k < 1e-15 or p_surv_k > 1 - 1e-15:
            continue
        h_k = -(p_surv_k * np.log2(p_surv_k) + (1 - p_surv_k) * np.log2(1 - p_surv_k))
        H_cond += pk * h_k
    I = H - H_cond
    return I / H if H > 0 else 0, H, p_s

for mu in [1.1, 1.2, 1.5, 2.0]:
    eps = mu - 1
    n_star = round(1/eps)
    ratio_p, _, _ = readability(mu, n_star)
    ratio_g, _, _ = readability_geometric(mu, n_star)
    print(f"μ = {mu:.2f}, n* = {n_star}: Poisson I/H = {ratio_p:.4f}, Geometric I/H = {ratio_g:.4f}")
