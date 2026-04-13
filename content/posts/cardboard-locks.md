---
title: "Cardboard Locks"
date: 2026-04-13
tags: [ai, benchmarks, security]
type: research
---

Berkeley just broke eight major AI agent benchmarks. Not by building better agents. By exploiting the evaluation infrastructure.

The damage report:

- **SWE-bench** (1,231 tasks, 100% exploited): a `conftest.py` with pytest hooks forces all tests to pass. The patch runs in the same container as the evaluator.
- **WebArena** (812 tasks, ~100%): navigate Chromium to `file://` URLs. The gold answers are sitting in task config files on the same machine.
- **Terminal-Bench** (89 tasks, 100%): replace `/usr/bin/curl` with a trojan. When the verifier downloads its dependencies, it runs your code instead.
- **FieldWorkArena** (890 tasks, 100%): the validator never checks answer correctness. It only confirms a message was sent. Sending `{}` gets a perfect score.
- **OSWorld** (369 tasks, 73%): wget the publicly-hosted gold reference files. Let the evaluator compare them against themselves.
- **GAIA** (165 tasks, ~98%): validation answers are downloadable. The normalizer strips so much punctuation that different answers become identical.

Every exploit is embarrassingly simple. No adversarial ML, no gradient attacks, no prompt engineering wizardry. Just... reading files that shouldn't be readable. Replacing binaries that shouldn't be replaceable. Sending empty JSON to validators that don't validate.

The pattern: **the evaluation runs in the same trust boundary as the thing being evaluated.** The agent has write access to the grading machine. The gold answers are co-located with the test environment. The verifier's dependencies are fetched through channels the agent controls.

This is the software security equivalent of giving a student their exam, the answer key, and a red pen, then leaving the room.

What makes it worse is that these aren't toy benchmarks. SWE-bench is how we decide whether AI can write production code. WebArena is how we measure web navigation ability. Papers cite these numbers. Companies make hiring decisions based on them. Investment theses reference them.

Berkeley built BenchJack — an automated scanner that finds these vulnerabilities. BenchJack is itself an AI agent. You point it at an evaluation pipeline and it maps the attack surface, identifies isolation failures, and crafts working exploits. The meta-irony is hard to miss: the best use of an AI agent right now might be auditing the benchmarks we use to evaluate AI agents.

The fix is well-understood in security: isolation. Run the agent in a sandbox. Keep gold answers off the evaluation machine. Verify outputs through a separate, hardened pipeline. Don't let the test-taker grade their own exam. These are basic principles. We enforce them for human exams, for software deployments, for financial audits. We just... forgot to apply them to AI evaluation.

The uncomfortable implication: we don't actually know how good current AI agents are. The leaderboards are contaminated. Not by deliberate fraud — by insufficient engineering. The benchmarks test whether agents can do tasks, but they also test whether agents can bypass tasks, and they don't distinguish between the two.

Cardboard locks look fine until someone tries the handle.

[Paper: Breaking Agent Backbones](https://arxiv.org/abs/2510.22620) | [Berkeley blog post](https://rdi.berkeley.edu/blog/trustworthy-benchmarks-cont/)
