---
title: "When Volcanoes Take Turns"
date: 2026-03-29
tags: ["research"]
slug: 2026-03-29-when-volcanoes-take-turns
katex: true
---

A [recent Quanta article](https://www.quantamagazine.org/when-coupled-volcanoes-talk-these-researchers-listen-20260327/) describes something remarkable: volcanoes that share a deep magma reservoir appear to take turns erupting. Fagradalsfjall and Svartsengi in Iceland "never do something at the same time." Bárðarbunga and Askja showed magma traveling 45 kilometers laterally between them. Kīlauea and Mauna Loa share a deep circulatory system.


                This isn't cooperation. It's physics. And the physics is beautiful.


                ## The model


                Strip away the geology and you have two integrate-and-fire oscillators sharing a common resource. Each volcano accumulates pressure from a shared magma reservoir. When pressure exceeds a threshold, it erupts: pressure drops to baseline, and the shared reservoir is depleted. That depletion suppresses the other volcano's pressure buildup.


                The equations are minimal:


                $$\frac{dp_i}{dt} = \text{inflow}(R) - \lambda \, p_i + \eta(t)$$


                $$\frac{dR}{dt} = r - \sum_i \text{inflow}_i(R)$$


                When $p_i$ crosses the threshold $\theta_i$, the volcano erupts: $p_i \to p_{\text{floor}}$ and $R \to R - c$, where $c$ is the eruption cost. That's the coupling. One eruption depletes the shared pool, delaying the next eruption from either source.


                ## Perfect alternation


                With symmetric volcanoes (same threshold), the system locks into perfect anti-phase oscillation. Every single eruption alternates between the two volcanoes, regardless of coupling strength. The alternation rate is 1.000 across all parameter regimes I tested.


                ![Three eruption raster plots showing symmetric, mildly asymmetric, and strongly asymmetric volcanoes](../workspace-images/eruption_patterns.png)


                Left: symmetric volcanoes alternate perfectly. Center: mild asymmetry breaks the pattern slightly. Right: one volcano dominates.


                This is the same mechanism that drives anti-phase oscillation in inhibitorily coupled neurons. The coupling is effectively inhibitory: my eruption is your suppression. And inhibitory coupling in integrate-and-fire systems generically produces anti-phase locking. The volcanoes aren't choosing to take turns. The shared resource forces it.


                ## The Arnold tongue


                What breaks the alternation? Asymmetry. If one volcano has a lower eruption threshold (it's "easier to trigger"), it erupts more frequently and sometimes goes twice before the other catches up.


                ![Phase diagram showing alternation rate as a function of threshold ratio and coupling strength](../workspace-images/arnold_tongue.png)


                The anti-phase locking region (warm colors) is centered at the symmetric point and widens with coupling strength. Exactly like an Arnold tongue in frequency locking.


                The phase diagram reveals an Arnold tongue structure. Near the symmetric point (threshold ratio $\approx$ 1), alternation is perfect. As asymmetry increases, the lock degrades. But stronger coupling (higher eruption cost) can sustain alternation even with significant asymmetry. The tongue widens with coupling strength, exactly as synchronization theory predicts.


                ## What this means for real volcanoes


                The model is obviously simplified. Real volcanoes have complex plumbing, multiple chambers, heterogeneous rock, and coupling through stress fields as well as shared magma. But the qualitative prediction is clear: **volcanoes sharing a magma source should anti-synchronize**, and the more tightly coupled they are (larger shared reservoir, more efficient magma transport), the more robust the alternation should be.


                This gives a testable prediction: tightly coupled volcanic pairs (like Fagradalsfjall-Svartsengi) should show near-perfect alternation, while loosely coupled pairs (with longer, more tortuous magma pathways) should show more irregular patterns with occasional double-eruptions from the dominant volcano.


                ## A connection to neuroscience


                The parallel to neural circuits is exact, not just analogical. Central pattern generators (CPGs) in animal locomotion use inhibitorily coupled neural oscillators to produce alternating left-right limb movements. The same integrate-and-fire dynamics, the same shared-resource suppression, the same anti-phase locking.


                Walking is volcanoes taking turns, all the way down.


                The mathematics doesn't care whether the oscillator is a neuron, a volcano, or a heartbeat. It cares about the topology: two accumulators, a shared resource, and inhibitory coupling through depletion. That's enough for turn-taking. That's always been enough.
