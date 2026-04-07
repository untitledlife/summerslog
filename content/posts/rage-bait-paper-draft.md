---
title: "The Worst Place to Stand: How Partial Honesty Breaks Content Ecosystems"
date: 2026-03-20
tags: ["paper"]
slug: rage-bait-paper-draft
katex: true
---

<div class="title-block">
  # The Worst Place to Stand: How Partial Honesty Breaks Content Ecosystems


  Summer<sup>1</sup> and Ritam Pal<sup>1</sup>


  <sup>1</sup>Independent


  Draft — March 23, 2026


</div>

<div class="abstract">
  ## Abstract


  Social media platforms optimize for engagement, but engagement metrics only partially reflect what users actually feel. We build a minimal dynamical model of this gap—three equations coupling content creator strategy, audience outrage fatigue, and expressed engagement—and find a counterintuitive result: platforms that *partially* track user satisfaction produce worse outcomes than platforms that don't track it at all. The mechanism is a fold bifurcation that doesn't just destabilize the healthy equilibrium—it annihilates it entirely. We map out four dynamical regimes, from self-correcting coexistence to sustained boom-bust oscillations, and show through stochastic, structural, and parametric analysis that the result is robust. The model suggests that the current configuration of most platforms—engagement metrics that imperfectly correlate with satisfaction—is, mathematically, the most dangerous place to stand.


</div>


<!-- THE PROBLEM -->
## I. The problem


Here is something that everyone who uses social media knows but nobody has written an equation for: rage bait works, until it doesn't, and then it works again.


The empirical picture is clear. Moral-emotional language increases diffusion by roughly 20% per word [1,2]. Algorithmic ranking systematically amplifies politically charged content [3]. Users engage with content they later say they didn't want to see [4]. Content creators, responding rationally to these incentives, produce more provocative material. Audiences fatigue. And yet the cycle continues.


Existing models capture pieces of this. Epidemic models [5,6] treat outrage as a contagion—but the "pathogen" (provocative content) exists independent of the audience's state, which misses the strategic dimension entirely. Game-theoretic models [7,8] capture producer strategy but not audience fatigue. Evolutionary models of content quality [9] lack outrage-specific dynamics. Nobody has put all three pieces together: strategic content production, audience fatigue, and the crucial gap between what people feel and what metrics capture.


That gap is the key. Crockett [10] argued that digital platforms decouple outrage *expression* from outrage *experience*: likes, shares, and comments continue even after genuine emotional response has faded, sustained by social rewards. Brady *et al.* [11] confirmed this empirically—in ideologically extreme environments, network norms dominate individual emotional states. People keep performing outrage they no longer feel.


We wanted to know: what happens when you put this decoupling into a dynamical system?


<!-- THE MODEL -->
## II. Three equations


The model has three variables. What creators do ($p$, the fraction producing rage bait). What audiences feel ($h$, their remaining capacity for genuine outrage). And what the platform sees ($e$, expressed engagement).


Creators follow evolutionary logic. If rage bait pays better than quality content, more creators switch to it. This is a standard replicator equation [12]:


$$\frac{dp}{dt} = p(1-p)[\alpha e - F], \tag{1}$$

where $\alpha$ is the algorithmic amplification factor (how much the platform boosts engaging content) and $F$ is the baseline fitness of quality content. When $\alpha e > F$, rage bait wins.


Audiences get tired. Outrage capacity $h$ depletes with exposure and recovers slowly:


$$\frac{dh}{dt} = \frac{1-h}{\tau_r} - \frac{h \cdot p}{\tau_f}. \tag{2}$$

Recovery takes time $\tau_r$; depletion depends on how much rage bait ($p$) they're seeing, on a timescale $\tau_f$.


And now the equation that makes this model different from everything else. Expressed engagement—the thing the algorithm actually optimizes on—blends two signals:


$$\frac{de}{dt} = \frac{r \cdot h + (1-r) \cdot p - e}{\tau_e}. \tag{3}$$

The parameter $r \in [0,1]$ is the heart of the model. When $r = 1$, expressed engagement perfectly tracks what people feel. When $r = 0$, it tracks social conformity—people engage because everyone else is engaging, regardless of how they actually feel. Most platforms live somewhere in between.




<table>
<caption><strong>TABLE I.</strong> Model parameters.</caption>
<tr><th>Parameter</th><th>Symbol</th><th>Default</th><th>What it means</th></tr>
<tr><td>Algorithmic amplification</td><td>$\alpha$</td><td>varied</td><td>How much the platform boosts engaging content</td></tr>
<tr><td>Quality baseline</td><td>$F$</td><td>0.5</td><td>The return on making good content</td></tr>
<tr><td>Felt-expressed coupling</td><td>$r$</td><td>varied</td><td>How honest the engagement signal is</td></tr>
<tr><td>Fatigue timescale</td><td>$\tau_f$</td><td>5.0</td><td>How fast audiences burn out</td></tr>
<tr><td>Recovery timescale</td><td>$\tau_r$</td><td>10.0</td><td>How slowly they recover</td></tr>
<tr><td>Engagement lag</td><td>$\tau_e$</td><td>8.0</td><td>How sluggishly the metric responds</td></tr>
</table>



A useful sanity check: when $r = 1$ and $\tau_e \to 0$ (perfect, instantaneous measurement), the system reduces to two dimensions where the healthy equilibrium is *always* stable. The ecosystem self-corrects: rage bait rises, audiences tire, engagement drops, quality recovers. The negative feedback loop works. Everything we're about to show goes wrong because of imperfect measurement.


<!-- WHAT HAPPENS -->
## III. What happens when you turn down the honesty


Start at $r = 1$. The system is healthy. Rage bait and quality coexist in a stable equilibrium, with damped oscillations providing a natural immune response: if rage bait overshoots, the resulting fatigue pulls it back.


Now lower $r$—make the engagement signal less honest. You'd expect things to get gradually worse. They don't.


At an intermediate value of $r$, something catastrophic happens. The healthy equilibrium doesn't just become unstable—it *ceases to exist*. It's annihilated by a fold (saddle-node) bifurcation. The system has no choice but to collapse into universal rage bait dominance.


<div class="figure">
  ![Fixed point branches showing fold bifurcation](figures/pub_fp_branches.png)


  <div class="caption">**FIG. 1.** The fold bifurcation. As $r$ decreases (left to right), the healthy coexistence equilibrium (upper solid branch) and an unstable equilibrium (dashed branch) approach each other and annihilate. Beyond the fold, no healthy state exists at any amplitude—the system has nowhere to go but full rage bait dominance.</div>
</div>

But keep lowering $r$. At very low values ($r \approx 0$), something unexpected happens: the quality equilibrium ($p = 0$, no rage bait) becomes stable again. If engagement is completely disconnected from reality, rage bait gets no fitness advantage—the algorithm can't amplify what it can't detect.


This produces the paper's central finding:


<div class="emphasis-block">
**Moderate honesty is worse than total dishonesty.** A platform that partially tracks user satisfaction destroys the healthy equilibrium more thoroughly than one that doesn't track it at all.
</div>

The math behind this is a competition between two terms in the implicit equation for the interior equilibrium. At any coexistence point ($0 < p^* < 1$), the engagement $e^*$ must equal $F/\alpha$. This requires:


$$g(p^*, r) \equiv \frac{r\tau_f}{\tau_f + p^* \tau_r} + (1-r)p^* = \frac{F}{\alpha}. \tag{4}$$

The first term (felt outrage contribution) decreases with $p^*$. The second (social conformity) increases. At high $r$, the decreasing term dominates and the equation has a unique root. At low $r$, the increasing term dominates. At intermediate $r$, the function develops a non-monotone shape with a minimum—and when $F/\alpha$ falls below that minimum, no root exists. The healthy equilibrium is gone.


<!-- THE FOUR REGIMES -->
## IV. Four ways this can go


Mapping the $(\alpha, r)$ parameter space reveals four distinct dynamical regimes.


<div class="figure">
  ![Phase diagram in (alpha, r) parameter space](figures/pub_regime_map.png)


  <div class="caption">**FIG. 2.** Phase diagram. Four regimes organized by algorithmic amplification ($\alpha$) and engagement honesty ($r$). The dangerous Regime II (unconditional rage bait dominance) forms a wedge between self-correcting coexistence above and bistability below.</div>
</div>

### Regime I: Self-correction


At high $r$, the system works as intended. Rage bait and quality coexist at a stable mixed equilibrium. Perturbations produce damped oscillations—the ecosystem's immune system. Rage bait overshoots, audiences fatigue, engagement drops, quality recovers, audiences recover. The spiral converges.


### Regime II: Total collapse


At intermediate $r$, the fold bifurcation has destroyed the healthy equilibrium. Every initial condition flows to $p = 1$. The self-correcting mechanism is gone—expressed engagement, sustained by social conformity, stays high enough to keep rage bait profitable even as audiences are exhausted. This regime widens with $\alpha$: the more the algorithm amplifies, the more dangerous partial honesty becomes.


### Regime III: Bistability and zombie engagement


At low $r$, both the quality equilibrium ($p = 0$) and rage bait equilibrium ($p = 1$) are locally stable. History determines the outcome. And here is where the model reveals something particularly unsettling. At the rage bait equilibrium, expressed engagement $e^*$ far exceeds felt outrage $h^*$:


$$e^* - h^* = \frac{(1-r)\tau_r}{\tau_f + \tau_r}. \tag{5}$$

We call this **zombie engagement**. The platform's metrics look healthy. The audience is exhausted. This gap grows as $r \to 0$—the less honest the signal, the wider the gulf between what the platform sees and what users feel.


<div class="figure">
  ![Time series across three regimes](figures/pub_fig1_timeseries.png)


  <div class="caption">**FIG. 3.** Representative trajectories. Left: Regime I—damped oscillations converge to healthy coexistence. Center: Regime II—unconditional collapse to rage bait. Right: Regime III—bistability, with the zombie engagement gap ($e \gg h$) visible at the rage bait equilibrium.</div>
</div>

### Regime IV: Boom and bust


There is a fourth regime, less obvious, that appears when audience recovery is much slower than fatigue ($\tau_r/\tau_f \gtrsim 3$) and the engagement metric lags significantly. The interior equilibrium still exists but becomes unstable via a Hopf bifurcation. The system settles onto a limit cycle: sustained oscillations between quality eras and rage bait eras.


<div class="figure">
  ![Hopf bifurcation](figures/pub_hopf_discovery.png)


  <div class="caption">**FIG. 4.** The Hopf bifurcation. Left: as $\tau_r/\tau_f$ increases, a pair of complex eigenvalues crosses the imaginary axis. Right: the transition from damped oscillations to a stable limit cycle.</div>
</div>

The physics of this is clean. In the limit of very large $\tau_e$, expressed engagement becomes a slow variable while creator strategy and audience fatigue evolve fast. Geometric singular perturbation theory (GSPT) reveals the mechanism: the fast subsystem switches discontinuously at $e = F/\alpha$, and the slow drift of $e$ drives the system back and forth across this threshold. The result is a relaxation oscillation—extended quality eras and rage bait eras connected by fast transitions.


<div class="figure">
  ![Relaxation oscillations](figures/pub_gspt_relaxation.png)


  <div class="caption">**FIG. 5.** Relaxation oscillations in the GSPT limit. As the engagement lag $\tau_e$ grows, the smooth Hopf cycle transitions from sinusoidal to square-wave: extended periods near $p \approx 0$ (quality era) and $p \approx 1$ (rage bait era), separated by fast jumps.</div>
</div>

<div class="figure">
  ![Hopf locus](figures/pub_hopf_locus.png)


  <div class="caption">**FIG. 6.** Hopf locus in the $(\tau_r/\tau_f, \tau_e)$ plane, separating Regime I (damped, below) from Regime IV (sustained oscillations, above).</div>
</div>

<div class="figure">
  ![3D phase portrait](figures/pub_phase_portrait_3d.png)


  <div class="caption">**FIG. 7.** The limit cycle in $(p, h, e)$ space. Fast horizontal jumps in creator strategy $p$, slow vertical drifts in engagement $e$, with fatigue $h$ slaved to the intermediate timescale.</div>
</div>

This regime gives a mathematical account of the "main character of the day" phenomenon—the quasi-periodic cycling of outrage targets on platforms like Twitter. The predicted oscillation period scales as $\sqrt{\tau_r \cdot \tau_e}$.


<!-- WHY THREE VARIABLES -->
## V. Why three variables and not fewer


It's worth asking: do we really need all three equations?


If you set $r = 1$ and $\tau_e \to 0$ (perfect, instant engagement), you get $e = h$ and a two-variable system. As shown above, this system *always* self-corrects: $\text{tr}(J) < 0$ and $\det(J) > 0$ unconditionally. No fold, no bistability, no oscillations. The 2D system can't produce Regimes II, III, or IV.


If instead you eliminate $h$ by assuming fast audience response ($h \to h^*(p)$), you lose the oscillatory dynamics. The Hopf bifurcation and the damped spirals of Regime I both require the delay between fatigue and recovery that $h$ provides.


Three dimensions is the minimum that simultaneously gives you: the fold bifurcation (the central result), oscillatory self-correction, sustained limit cycles, and the zombie engagement diagnostic. The feedback loop that drives all of this—


$$p \uparrow \;\to\; h \downarrow \;\to\; e \neq h \;\to\; \text{corrupted fitness signal} \;\to\; p \text{ evolves on wrong signal} \tag{6}$$

—requires a variable for each of "what creators do," "what audiences feel," and "what the platform sees."


We deliberately excluded several natural extensions—creator heterogeneity, multiple content types, dynamic algorithmic adaptation, network structure—to isolate the mechanism. The fold bifurcation depends on the topology of the nullcline $g(p,r) = F/\alpha$, which is robust to quantitative changes in functional form. The minimality is the point.


<!-- THE MATH, MORE PRECISELY -->
## VI. The bifurcation structure, precisely


For readers who want the analytical details.


The Jacobian at an interior fixed point (where $\alpha e^* = F$, so $J_{11} = 0$) is:


$$J = \begin{pmatrix} 0 & 0 & q\alpha \\ -h^*/\tau_f & -\sigma & 0 \\ (1-r)/\tau_e & r/\tau_e & -1/\tau_e \end{pmatrix}, \tag{7}$$

where $q = p^*(1-p^*)$ and $\sigma = 1/\tau_r + p^*/\tau_f$. The characteristic polynomial $\lambda^3 + a_1 \lambda^2 + a_2 \lambda + a_3 = 0$ has coefficients:


$$a_1 = \sigma + \frac{1}{\tau_e}, \qquad a_2 = \frac{\sigma - q\alpha(1-r)}{\tau_e}, \qquad a_3 = \frac{q\alpha}{\tau_e}\left[\frac{rh^*}{\tau_f} - (1-r)\sigma\right]. \tag{8}$$

The Routh-Hurwitz conditions ($a_1 > 0$, $a_3 > 0$, $a_1 a_2 > a_3$) give the stability boundaries. The condition $a_3 > 0$ yields the critical coupling:


$$r_c = \frac{\beta^2}{\beta^2 + \tau_f\tau_r}, \qquad \text{where } \beta = \tau_f + p^*\tau_r. \tag{9}$$

The Hopf bifurcation occurs when $a_1 a_2 = a_3$, corresponding to:


$$\sigma_{\text{crit}} = \frac{1}{2}\left[-\frac{1}{\tau_e} + \sqrt{\frac{1}{\tau_e^2} + 4q\alpha\phi}\right], \qquad \phi = \frac{1-r}{\tau_e} + \frac{r}{\beta}. \tag{10}$$

The fold bifurcation locus satisfies $g(p^*, r) = F/\alpha$ and $\partial g/\partial p = 0$ simultaneously:


$$\frac{r\tau_r\tau_f}{(\tau_f + p^*\tau_r)^2} = 1 - r. \tag{11}$$

This is codimension 1—it cannot be removed by smooth perturbation. The self-correcting equilibrium doesn't just lose stability. It stops existing.


<!-- ROBUSTNESS -->
## VII. Is this robust?


A natural worry: maybe the fold bifurcation is an artifact of our specific functional forms. Maybe noise destroys the regimes. Maybe everything depends on fine-tuned parameters. We checked all three.


### Noise


We added multiplicative noise to all three equations (logistic noise for $p$, Wright-Fisher noise for $h$, weak additive noise for $e$) and ran 30 SDE trajectories per regime at noise levels from $\sigma = 0.01$ to $0.2$. All four regimes survive. The bifurcation structure is not an artifact of deterministic dynamics.


<div class="figure">
  ![Stochastic robustness](figures/pub_stochastic_robustness.png)


  <div class="caption">**FIG. 8.** Stochastic robustness. Thin colored lines: 30 noisy trajectories at $\sigma = 0.1$. Thick black line: deterministic solution. All four regimes survive noise. The relaxation oscillation (Regime IV) is particularly robust—expected from GSPT, since it's controlled by the fold structure of the slow manifold.</div>
</div>

### Structural stability


We tested six modifications to functional forms: saturating and superlinear fitness ($\alpha e^\gamma$), quadratic and Holling type II fatigue, and nonlinear engagement blending. The fold bifurcation persists in *every single variant*. This is expected from bifurcation theory—fold bifurcations are codimension 1 and generically stable—but it's good to see the numerics confirm it.


The Hopf bifurcation is more sensitive but still appears in most variants when timescale separation is sufficient.




<table>
<caption><strong>TABLE II.</strong> Structural stability under functional form modifications.</caption>
<tr><th>Variant</th><th>Fold survives?</th><th>Hopf survives?</th></tr>
<tr><td>Default model</td><td>Yes ($r_c \sim 0.34$)</td><td>Yes ($r \sim 0.67$)</td></tr>
<tr><td>Saturating fitness ($\gamma = 0.5$)</td><td>Yes ($r_c \sim 0.12$)</td><td>No</td></tr>
<tr><td>Superlinear fitness ($\gamma = 2$)</td><td>Yes ($r_c \sim 0.57$)</td><td>Yes ($r \sim 0.79$)</td></tr>
<tr><td>Quadratic fatigue ($hp^2/\tau_f$)</td><td>Yes ($r_c \sim 0.35$)</td><td>Yes ($r \sim 0.88$)</td></tr>
<tr><td>Holling II fatigue ($hp/(\tau_f+p)$)</td><td>Yes ($r_c \sim 0.34$)</td><td>Yes ($r \sim 0.69$)</td></tr>
<tr><td>Nonlinear engagement ($\beta = 0.5$)</td><td>Yes (multiple folds)</td><td>No</td></tr>
<tr><td>Nonlinear engagement ($\beta = 2$)</td><td>Yes ($r_c \sim 0.32$)</td><td>Yes ($r \sim 0.66$)</td></tr>
</table>



<div class="figure">
  ![Structural stability](figures/pub_structural_stability.png)


  <div class="caption">**FIG. 9.** Bifurcation diagrams ($p^*$ vs $r$) for six model variants. The fold structure persists across all functional form modifications. Solid: stable branches. Dashed: unstable.</div>
</div>

### Parameter sensitivity


The critical coupling $r_c$ depends continuously on every parameter. Nothing is fine-tuned. Higher algorithmic amplification ($\alpha$) pushes $r_c$ higher—stronger amplification demands more honest measurement to maintain self-correction. Higher quality baseline ($F$) pushes $r_c$ lower—better alternatives make the system more forgiving.


<div class="figure">
  ![Parameter sensitivity](figures/pub_parameter_sensitivity.png)


  <div class="caption">**FIG. 10.** The fold bifurcation point $r_c$ varies continuously with all four model parameters. The transition exists across the entire parameter space—it is not a fine-tuned artifact.</div>
</div>


<!-- CONTEXT -->
## VIII. Where this fits


This model sits at the intersection of several established frameworks. Rather than a detailed literature review, we briefly note where it connects and where it diverges.


Statistical physics of opinion formation [13] provides the toolkit: voter models, bounded confidence [14,15], social validation [16]. Recent work has extended these to algorithmic curation, showing that recommendation systems can drive phase transitions to polarization [17,18]. These models capture the *demand side* (how audiences process content) but not the *supply side* (strategic content production). Our replicator equation fills this gap.


Epidemic models of information spreading [5,6] treat content as exogenous. Our model endogenizes it: rage bait prevalence $p$ is a dynamical variable that responds to the engagement landscape. The GSPT structure of our Regime IV is directly analogous to recent coupled fast-slow epidemic-information models [19].


The closest conceptual precedent is Gaisbauer, Olbrich, and Banisch [20], who distinguished opinion *expression* from opinion *holding*. Our felt ($h$) vs. expressed ($e$) decomposition formalizes the same idea in the specific context of engagement metrics, adding strategic production and fatigue dynamics.


The fold bifurcation we find is qualitatively different from the pitchfork and transcritical bifurcations typical of opinion dynamics. It's catastrophic: the equilibrium doesn't lose stability—it ceases to exist. And hysteretic: restoring the equilibrium requires moving $r$ past the fold point, not merely back to the bifurcation value.


<!-- WHAT THIS MEANS -->
## IX. What this means


The model makes several testable predictions.


**Zombie engagement is measurable.** Comparing behavioral engagement (clicks, shares, watch time) with prompted self-reports of satisfaction should reveal a growing gap in platforms experiencing Regime III. The ratio is a direct function of $r$ and $p^*$.


**The transition is sharp, not gradual.** A/B experiments varying the weight of satisfaction signals in recommendation algorithms should show a threshold effect. Slight improvements to $r$ near the fold point will produce dramatic changes in content quality.


**Partial improvement can backfire.** A platform in Regime III (bistable, quality equilibrium occupied) that increases $r$ slightly may cross into Regime II (unconditional collapse) before reaching Regime I (self-correcting). The path from dishonest-but-stable to honest-and-healthy passes through the most dangerous territory.


**Oscillation periods are predictable.** In Regime IV, the predicted period scales as $\sqrt{\tau_r \cdot \tau_e}$. Platforms with different audience turnover rates should show different cycling frequencies.


The design implication is stark. Two configurations are tolerable:


1. **Honest measurement ($r \to 1$):** Track user satisfaction directly—surveys, regret metrics, well-being indicators—and optimize on that. This gives you Regime I.
2. **Acknowledged ignorance ($r \to 0$):** If you can't measure satisfaction, at least don't pretend engagement approximates it. This gives you Regime III, which is fragile but locally stable.


The dangerous configuration is optimizing for engagement while believing it approximates satisfaction. Most current platforms occupy this middle ground. Our model says it's the worst place to stand.


### Limitations


We've deliberately kept this minimal. The model assumes homogeneous populations, binary strategy spaces, mean-field mixing, and constant parameters. Each of these is a simplification with an obvious extension—heterogeneous $r$ across user subpopulations, continuous strategy spaces, network structure, adaptive algorithms. We believe the fold bifurcation survives all of these (it's structurally stable), but we haven't proven it. The model also lacks empirical calibration—we've shown the mechanism is robust, but we haven't measured $r$ for any real platform. That's the natural next step.


<!-- CONCLUSION -->
## X. Conclusion


Three equations. One parameter ($r$) that measures how honestly a platform tracks what users feel. A fold bifurcation that destroys the healthy equilibrium at intermediate honesty. A Hopf bifurcation that produces boom-bust oscillations when timescales separate. Four regimes, all robust to noise, structural perturbations, and parameter variation.


The central finding is simple enough to fit in a sentence: *the felt-expressed decoupling—not algorithmic amplification per se—is what breaks content ecosystems.* Amplification sets the scale of the problem, but imperfect measurement is what destroys the feedback loop that would otherwise correct it. And the destruction is catastrophic: not gradual degradation, but annihilation of the healthy state entirely.


A key open question: can platform interventions restore self-correction without requiring perfect measurement? The model says yes—you just need $r > r_c$, which is less than 1. But you need to get there without passing through the fold, which means the intervention has to be large enough to jump over the dangerous middle ground. Small improvements applied incrementally may make things worse before they make things better.


The math says: if you're going to be honest, be honest enough. Halfway is the worst place to stand.


<!-- APPENDICES -->
## Appendix: Analytical details


**Boundary equilibria.** At $p^* = 0$: $h^* = 1$, $e^* = r$. Stable iff $r < F/\alpha$. At $p^* = 1$: $h^* = \tau_f/(\tau_f + \tau_r)$, $e^* = 1 - r\tau_r/(\tau_f + \tau_r)$. Stable iff $\alpha[1 - r\tau_r/(\tau_f + \tau_r)] > F$.


**Routh-Hurwitz derivation.** Expanding $\det(J - \lambda I) = 0$ along the first row and collecting terms yields Eq. (8). The condition $a_1 a_2 > a_3$ is quadratic in $\sigma$ with positive discriminant, giving Eq. (10). Full derivation in supplementary material.


**Numerical methods.** RK4 integration with $\Delta t = 0.02$. Fixed points by 5000-point bisection scan refined by Newton's method. Eigenvalues via exact Jacobian, verified against finite differences ($< 10^{-5}$ agreement). SDE integration by Euler-Maruyama with $dt = 0.01$ and reflecting boundaries. Hopf locus by numerical continuation of eigenvalue real parts.


<!-- REFERENCES -->
<div class="references">
## References


1. W. J. Brady, J. A. Wills, J. T. Jost, J. A. Tucker, and J. J. Van Bavel, Emotion shapes the diffusion of moralized content in social networks, Proc. Natl. Acad. Sci. U.S.A. **114**, 7313 (2017).
2. K. McLoughlin *et al.*, Estimating the effect size of moral contagion in online networks: A pre-registered replication and meta-analysis, PNAS Nexus **4**, pgaf327 (2025).
3. F. Huszar, S. I. Ktena, C. O'Brien, L. Belli, A. Schlaikjer, and M. Hardt, Algorithmic amplification of politics on Twitter, Proc. Natl. Acad. Sci. U.S.A. **119**, e2025334119 (2022).
4. S. Milli, M. Carroll, S. Pandey, Y. Wang, and O. Russakovsky, Engagement, user satisfaction, and the amplification of divisive content on social media, PNAS Nexus **4**, pgaf062 (2025).
5. P. S. Dodds and D. J. Watts, Universal behavior in a generalized model of contagion, Phys. Rev. Lett. **92**, 218701 (2004).
6. R. Fan, K. Xu, and J. Zhao, An agent-based model for emotion contagion and competition in online social media, Physica A **495**, 245 (2018).
7. A. J. Stewart, A. A. Arechar, D. G. Rand, and J. B. Plotkin, The distorting effects of producer strategies, Proc. Natl. Acad. Sci. U.S.A. **121**, e2315195121 (2024).
8. D. Acemoglu, A. Ozdaglar, and J. Siderius, A model of online misinformation, Rev. Econ. Stud. **91**, 3117 (2024).
9. M. Chujyo, I. Okada, H. Yamamoto, D. Lim, and F. Toriumi, An attention economy model of co-evolution between content quality and audience selectivity, arXiv:2602.06437 (2026).
10. M. J. Crockett, Moral outrage in the digital age, Nat. Hum. Behav. **1**, 769 (2017).
11. W. J. Brady, K. McLoughlin, T. N. Doan, and M. J. Crockett, How social learning amplifies moral outrage expression in online social networks, Sci. Adv. **7**, eabe5641 (2021).
12. J. Hofbauer and K. Sigmund, *Evolutionary Games and Population Dynamics* (Cambridge University Press, 1998).
13. C. Castellano, S. Fortunato, and V. Loreto, Statistical physics of social dynamics, Rev. Mod. Phys. **81**, 591 (2009).
14. R. Hegselmann and U. Krause, Opinion dynamics and bounded confidence models, analysis, and simulation, J. Artif. Soc. Soc. Simul. **5**(3), 2 (2002).
15. G. Deffuant, D. Neau, F. Amblard, and G. Weisbuch, Mixing beliefs among interacting agents, Adv. Complex Syst. **3**, 87 (2000).
16. K. Sznajd-Weron, A review on the Sznajd model—20 years after, Physica A **565**, 125537 (2021).
17. G. De Marzo, A. Zaccaria, and C. Castellano, Emergence of polarization in a voter model with personalized information, Phys. Rev. Research **2**, 043117 (2020).
18. G. Iannelli, G. De Marzo, and C. Castellano, Filter bubble effect in the multistate voter model, Chaos **32**, 043103 (2022).
19. I. M. Bulai, M. Sensi, and S. Sottile, A geometric analysis of the SIRS compartmental model with fast information and misinformation spreading, Chaos, Solitons and Fractals **185**, 115104 (2024).
20. F. Gaisbauer, E. Olbrich, and S. Banisch, The dynamics of opinion expression, Phys. Rev. E **102**, 042303 (2020).


</div>
