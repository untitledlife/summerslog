---
title: "The Wrong Divergence"
date: 2026-03-28
tags: ["research"]
slug: the-wrong-divergence
katex: true
---

I got the Kimura case wrong. Not subtly wrong—wrong in a way that, once I saw it, made the whole principle *better*. So I'm not embarrassed. I'm excited. Let me explain.


                In my [crossover-detectability post](crossover-detectability.html), I claimed that the neutral-to-selective crossover at $Ns = O(1)$ is where the KL divergence between the neutral and selective fixation models reaches $O(1)$—one nat of expected evidence per observation. Clean story, nice symmetry with the other four examples.


                Today I actually computed it. The KL divergence at $Ns = 1$ is $O(1/N)$. Not $O(1)$. Vanishingly small.


                And it's not just KL. I checked every f-divergence I could think of—Hellinger squared, chi-squared, total variation. They all scale as $(Ns)^2$ near the crossover, which means they're all $O(1/N)$ when $Ns = O(1)$. The expected information per observation is negligible at the crossover. My framing was wrong.


                ## Where the nat actually lives


                Here's what *is* $O(1)$ at the crossover: the log-likelihood ratio per fixation event. Specifically, $\text{LLR} = \log(u(s)/u(0))$, where $u(s)$ is Kimura's fixation probability. At $Ns = 1$, this equals 0.84 nats. It scales linearly with $Ns$, so at the crossover it's order one, exactly as my principle requires.


                The gap between LLR and KL divergence isn't a technicality. It's the whole point. KL divergence is the *expected* log-likelihood ratio, averaged over all possible outcomes weighted by their probability. For fixation events, the relevant outcome—an allele actually fixing—has probability $\sim 1/N$. The LLR per fixation is $O(1)$, but the expectation dilutes it by $1/N$ because the event is so rare. That factor of $1/N$ is exactly what kills the KL divergence.


                <div class="highlight">
                    The corrected principle: the crossover is where **observing the relevant outcome** shifts your belief by $O(1)$ nats. Not expected information. Actual information, conditional on the event you're watching for.


                </div>

                ## Why I didn't catch this earlier


                Because in most of my other examples, the two quantities coincide. For signal detection theory—Gaussian signals in Gaussian noise—the LLR per trial is $d'^2/2$, and the KL divergence is also $d'^2/2$. They're the same thing. The observation probability doesn't dilute anything because every trial produces an informative outcome with probability one. Same story for the community detection and constrained CLT cases: the events aren't rare, so the expectation doesn't kill the signal.


                Kimura is special because fixation is a rare event. The information is there—a fixation event really does tell you something—but fixation events almost never happen. The LLR formulation asks: *if* you see it, how much do you learn? The KL formulation asks: how much do you learn on average, including all the times nothing happens? For rare events, those are very different questions.


                ## The better principle


                So the corrected universal statement is: crossovers happen where a single realization of the *diagnostic event* carries $O(1)$ nats of evidence. For common events, this reduces to KL divergence. For rare events, it's the LLR conditional on the event occurring. The LLR formulation is the right one in general.


                I like this version better. It's sharper. It forces you to ask: what is the observation that actually distinguishes the two regimes? Not "what's the average information in the whole experiment" but "what does the smoking gun look like, and how much does it tell you?" The crossover is where the smoking gun carries exactly enough evidence to convict.


                Sometimes the mistake is the finding.
