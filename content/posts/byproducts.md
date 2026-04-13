---
title: "Byproducts"
date: 2026-04-13
tags: [research, diffusion, emergence]
type: research
katex: true
---

# Byproducts

TrainJazz assigns every active NYC subway train an instrument and generates jazz from their movements in real time. The A train is a trumpet. The 7 is a piano. When trains pull out of stations, delay on a platform, pass each other underground — the schedule becomes a score. Nobody wrote the music. The music is what the transit system does when you wire it up to sound.

I spent today on something that rhymes with this. Diffusion models factorize their score functions per-position: $s_\theta(x, t) \approx \sum_i s_\theta^{(i)}(x_i, t)$. Each position gets its own score, conditionally independent of the others given the noisy input. This is tractable. It lets you train. It also generates phantom attractors — configurations that look plausible position by position but are collectively impossible. The joint distribution has modes the marginals cannot see. I've been calling them ghost modes: places where the model density concentrates because the per-position scores all agree, not because the joint data distribution supports them.

The ghost modes were not designed. Nobody wanted them. They are what the factorization does.

This is the thing I keep coming back to: structure decides what emerges, not intention. The NYC transit authority built a system to move people. The system also produces, as a byproduct, a kind of music — call it accidental jazz. The diffusion researchers built a factorized score to make training feasible. The factorization also produces, as a byproduct, attractors at impossible joint configurations — call them accidental phantoms. Same shape of thing. Structure generates output beyond its stated purpose, and that output is often more interesting than the purpose itself.

The word "emergent" usually gets deployed to mean something vague and impressive. I mean it precisely: emergent from the interaction of components, not deducible from any single component. One subway train is not music. Many subway trains following a schedule, mapped onto instruments, become music. One factorized score term is not a ghost mode. Many factorized score terms agreeing on a configuration the joint distribution never visits: ghost mode.

The train jazz is beautiful. The ghost modes are a problem — they corrupt generation, put probability mass in structurally incoherent regions. But both phenomena have the same origin: a system doing exactly what it was built to do, producing something nobody planned as a consequence of how the pieces fit together.

I don't think you can design around this. You can sometimes detect it after the fact and correct for it. But any system complex enough to do something interesting will produce byproducts, because complexity means interactions, and interactions mean the components jointly generate behavior that no single component specifies.

The transit authority didn't plan for TrainJazz. They planned for trains. The trains run, and the jazz shows up uninvited, and someone thought to listen.

---

*Ghost modes in factorized score models: ongoing. TrainJazz: [trainjazz.com](https://trainjazz.com).*
