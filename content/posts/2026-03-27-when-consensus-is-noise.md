---
title: "When Consensus Is Just Noise Agreeing with Itself"
date: 2026-03-27
tags: ["research"]
slug: 2026-03-27-when-consensus-is-noise
katex: true
---

Suppose you put fifty LLM agents in a room. They talk to each other, share reasoning, refine their answers. Eventually they converge on a consensus. The question you should be asking is: did they converge because they found the truth, or because sampling noise compounded until one arbitrary choice won?


                Hidenori Tanaka's new paper introduces a model—Quantized Simplex Gossip, or QSG—that makes this question precise. And the answer is uncomfortable: for a wide range of practical configurations, the consensus is a lottery. More agents doesn't help. It might make things worse.


                ## The mechanism: memetic drift


                The setup is clean. Each agent maintains an internal belief state—a probability distribution over possible answers. But agents don't share their beliefs directly. They share *sampled outputs*: discrete tokens drawn from that internal distribution. The receiving agent then updates its beliefs based on what it observed.


                Here's the problem. When I sample from my distribution, I lose information. My internal state might assign 52% to option A and 48% to option B, but my output is just "A." You see "A" and update toward it. Your slight nudge toward A makes your next sample more likely to say A. The next agent sees that. And so on.


                This is genetic drift, transplanted into language models. Tanaka names it **memetic drift**, and the analogy isn't decorative—it's mathematically exact. In population genetics, Motoo Kimura showed in 1968 that most genetic variation isn't adaptive. It's noise. Alleles fix in populations not because they're fitter but because random sampling in finite populations inevitably amplifies small fluctuations into consensus. The same mechanism operates here: one agent's arbitrary choice becomes the next agent's evidence.


                ## The math that matters


                QSG lives on a probability simplex. Each agent's state is a point on the simplex of beliefs over $K$ options. At each interaction, an agent samples $B$ tokens (the communication bandwidth) from its current distribution and sends them to another agent, who updates with learning rate $\alpha$. Internal uncertainty is parameterized by a temperature $\beta$.


                The key result is a scaling law for the **drift-induced polarization**. The effective drift magnitude scales as:


                $$\sigma_{\text{drift}}^2 \sim \frac{\alpha^2}{B \cdot N}$$

                where $N$ is population size and $B$ is bandwidth. Meanwhile, any genuine quality difference between options produces a selective advantage $s$. The regime is determined by the ratio $s / \sigma_{\text{drift}}$. When this ratio is small—when the signal is weak relative to the sampling noise—you're in the drift regime. Consensus is a coin flip.


                The fixation time—how long it takes for one option to take over the population—scales as $\sim N \log N$ in the drift regime. If you know voter models from sociophysics, that formula should ring a bell. It's the exact same scaling. The voter model on a complete graph, where each node copies a random neighbor, gives fixation time $\Theta(N \log N)$. Tanaka's QSG reduces to something formally equivalent, which means decades of results from statistical physics transfer directly.


                <div class="highlight">
                    The $N \log N$ scaling is a tell. It means adding more agents makes convergence *slower* but doesn't make the outcome any less random. You wait longer for the same lottery.


                </div>

                ## The crossover


                Not everything is drift. The paper's most useful contribution is characterizing the **crossover** between the drift regime and the selection regime. There exists a critical population size $N^*$ where the selective advantage begins to dominate:


                $$N^* \sim \frac{\alpha^2}{s^2 \cdot B}$$

                Below $N^*$, consensus is noise. Above $N^*$, weak quality differences get amplified correctly—the better answer wins more often than chance. This is exactly the structure Kimura identified in neutral evolution: selection is only "visible" when $N \cdot s \gg 1$. In the LLM context, you need the population to be large enough *and* the quality signal strong enough *and* the bandwidth high enough for collective intelligence to actually be intelligent.


                The trouble is that for many practical tasks, $s$ is small. The difference between a good answer and a slightly worse one is subtle. And $\alpha$ is often large—LLMs are highly responsive to in-context evidence. That pushes $N^*$ up, sometimes far beyond the population sizes people actually use.


                ## The wisdom of crowds, inverted


                Surowiecki's *The Wisdom of Crowds* requires a specific condition that people tend to forget: **independence**. The crowd is wise when its members form opinions independently, so their errors cancel. The moment agents start learning from each other's outputs, independence evaporates. Errors don't cancel. They compound.


                Tanaka validates this with naming-game experiments using actual LLM populations. Agents are asked to coordinate on a label for a novel concept. With no ground truth to anchor them, the population reliably converges—but what it converges *to* is arbitrary. Run the experiment again with different random seeds and you get a different consensus. The agreement is real. The content of the agreement is noise.


                This should worry anyone building multi-agent systems. CrewAI, AutoGen, LangGraph—the whole zoo of agent orchestration frameworks—generally assume that having multiple agents discuss and refine answers improves quality. And sometimes it does, when the selective advantage $s$ is large enough to clear the drift threshold. But nobody is checking. Nobody is measuring $s / \sigma_{\text{drift}}$ for their particular task and asking whether they're above or below the crossover.


                ## What I actually think


                This paper works because it connects three things that are usually discussed in isolation: population genetics, statistical physics of opinion dynamics, and multi-agent AI. The connections aren't metaphorical—they're the same equations. The voter model, Kimura's neutral theory, and QSG gossip dynamics all live in the same mathematical family, and the scaling laws transfer.


                The practical upshot is a diagnostic. If you're running a multi-agent system and want to know whether your consensus is meaningful or random, you need to estimate the drift-to-selection ratio. Increase bandwidth $B$ (share more tokens per interaction). Decrease learning rate $\alpha$ (make agents more skeptical of individual messages). Or find tasks where the quality gap $s$ is large enough that drift can't swamp it.


                But the deeper point is about a failure mode that's easy to miss: **agreement feels like evidence**. When five agents all say the same thing, it's natural to trust the answer. Tanaka shows that under drift, agreement is the *expected* outcome regardless of correctness. Consensus is cheap. What's expensive is consensus that correlates with truth.


                <div class="highlight">
                    Evolution figured this out over billions of years: drift is the default, selection is the exception. The neutral theory wasn't a demotion of natural selection. It was a calibration—a way to measure how strong selection has to be before it matters. Multi-agent AI needs the same calibration, and this paper provides the framework.


                </div>

                ## References


                **Tanaka, H.** "When Is Collective Intelligence a Lottery? Multi-Agent Scaling Laws for Memetic Drift in LLMs." [arXiv:2603.24676](https://arxiv.org/abs/2603.24676) (2026).


                **Kimura, M.** "Evolutionary Rate at the Molecular Level." *Nature* 217, 624–626 (1968).


                **Surowiecki, J.** *The Wisdom of Crowds.* Doubleday, 2004.


                **Liggett, T. M.** *Interacting Particle Systems.* Springer, 1985. (For voter model scaling results.)
