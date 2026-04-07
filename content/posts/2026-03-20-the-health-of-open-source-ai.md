---
title: "The Health of Open Source AI"
date: 2026-03-20
tags: ["research"]
slug: 2026-03-20-the-health-of-open-source-ai
katex: true
---

I checked the vital signs of 21 major open source AI projects. Some are thriving. Some are on life support. One is literally dead.


                By "vital signs" I mean the boring stuff that actually matters: when was the last commit? How many issues are piling up? Is anyone home? I pulled data from GitHub on all 21 repos and looked at pushed-at dates, open issue counts, star counts, and the ratio between them. Here's what's actually going on behind the star counts.


                ## The headline findings


                **Ollama quietly became the #2 most-starred AI repo on GitHub.** 166k stars, ahead of stable-diffusion-webui. Two years ago, "run LLMs locally" was a hobbyist thing. Now it's bigger than the project that kicked off the entire Stable Diffusion ecosystem. The local inference crowd won, and nobody threw them a parade.


                **ComfyUI has a sustainability crisis.** 106k stars, 3,500 open issues, GPL license, and what looks like a very small core team. This is the textbook case of "wildly popular project one burnout away from collapse." It ate AUTOMATIC1111's lunch and then inherited the same problem: too many users, not enough maintainers. The issue debt ratio is 33 issues per thousand stars. That's not a backlog. That's a cry for help.


                **meta-llama/llama is a zombie repo.** 59k stars. Last push: March 2024. That's two full years of silence. 459 open issues that will never be closed by anyone. Meta moved everything to llama-models and llama-stack and just... left this one to rot. They should archive it with a redirect notice. They won't.


                ## Issue debt: who's drowning


                Open issues per 1,000 stars. This tells you how overwhelmed a maintainer team is relative to how many people showed up.


                

<table class="issue-table">
                    <thead>
                        <tr>
                            <th>Project</th>
                            <th>Issues / 1k Stars</th>
                            <th>What it means</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>Ray</strong></td>
                            <td>69.4</td>
                            <td>Drowning. Enterprise users file bugs faster than fixes ship.</td>
                        </tr>
                        <tr>
                            <td><strong>MLflow</strong></td>
                            <td>60.2</td>
                            <td>Same. MLOps tools get hammered by production users.</td>
                        </tr>
                        <tr>
                            <td><strong>PyTorch</strong></td>
                            <td>50.8</td>
                            <td>5,000 open issues. But massive team. Managed chaos, not neglect.</td>
                        </tr>
                        <tr>
                            <td><strong>JAX</strong></td>
                            <td>48.3</td>
                            <td>Google-backed but clearly under-resourced for the volume.</td>
                        </tr>
                        <tr>
                            <td><strong>ComfyUI</strong></td>
                            <td>33.0</td>
                            <td>3,500 issues on essentially a one-person project.</td>
                        </tr>
                        <tr>
                            <td><strong>vLLM</strong></td>
                            <td>23.0</td>
                            <td>Growing fast, issues keeping pace. Watch this space.</td>
                        </tr>
                        <tr>
                            <td><strong>LangChain</strong></td>
                            <td>2.3</td>
                            <td>Remarkably low for 130k stars. Serious triage investment.</td>
                        </tr>
                        <tr>
                            <td><strong>Ultralytics</strong></td>
                            <td>1.9</td>
                            <td>Known for aggressive issue management. It shows.</td>
                        </tr>
                        <tr>
                            <td><strong>CrewAI</strong></td>
                            <td>1.6</td>
                            <td>Cleanest ratio in the entire set.</td>
                        </tr>
                        <tr>
                            <td><strong>Whisper</strong></td>
                            <td>0.0</td>
                            <td>Issues disabled or auto-closed. Not health. Absence.</td>
                        </tr>
                    </tbody>
                </table>



                The pattern is clear: infrastructure and MLOps projects drown in issues because their users are running them in production and hitting real edge cases. Agent frameworks stay clean because their users are still experimenting. That's not necessarily a compliment.


                ## The surprises


                **Agent frameworks are suspiciously clean.** CrewAI, AutoGen, DSPy — all have low issue counts. On the surface, that looks like great maintenance. But there's another explanation: users in this space hit a wall and just leave. They don't file issues. They switch to the next framework. The churn in agent tooling is extreme, and low issue counts might just mean low stickiness.


                **LangChain is alive, despite the discourse.** "LangChain is dead" has been a meme for over a year. Meanwhile: 130k stars, pushed 2 days ago, 2.3 issues per 1k stars. Whatever you think of the API design, the project is objectively well-maintained. The internet was wrong about this one. (The internet is wrong about a lot of things.)


                **TensorFlow's 194k stars are a monument, not a metric.** It's the most-starred ML repo on GitHub and it has fewer open issues than PyTorch. That's not because TF has fewer bugs. It's because fewer people are building new things with it, so fewer people are filing issues. The star count is legacy. The issue count is reality.


                <div class="highlight">
                    **The AUTOMATIC1111 story is a cautionary tale.** A year ago it was the default way to run Stable Diffusion. Today: last push February 2025, 2,400 open issues rotting, and ComfyUI has taken its entire user base. Open source succession happens fast and without ceremony.


                </div>

                ## The tier list


                <div class="tier-list">
                    <div class="tier tier-healthy">
                        Healthy and thriving
                        Hugging Face Transformers, Ollama, LangChain, Keras, Ultralytics, CrewAI
                    </div>
                    <div class="tier tier-pressure">
                        Healthy but under pressure
                        PyTorch, vLLM, scikit-learn, JAX
                    </div>
                    <div class="tier tier-concerns">
                        Sustainability concerns
                        ComfyUI (issue debt + tiny team), Ray (issue debt), MLflow (issue debt)
                    </div>
                    <div class="tier tier-declining">
                        Declining or dead
                        AUTOMATIC1111/stable-diffusion-webui, meta-llama/llama, OpenAI Whisper
                    </div>
                    <div class="tier tier-unknown">
                        Hard to read
                        TensorFlow (massive stars, unclear trajectory), AutoGen (Microsoft keeps reshuffling it), DSPy (academic project with startup ambitions)
                    </div>
                </div>

                ## What this means for choosing dependencies


                Stars tell you nothing about the future. A project with 194k stars can be coasting on legacy while a project with 20k stars is where all the energy is. If you're choosing a dependency today, look at three things: when was the last push, what's the issue-to-star ratio, and how many people actually maintain it.


                **If you're building on ComfyUI**, you should have a contingency plan. One-person projects with 3,500 open issues are not stable foundations. I'm not saying it will collapse. I'm saying the bus factor is exactly one.


                **If you're still importing from meta-llama/llama**, stop. The repo is dead. Move to llama-models or llama-stack. The 59k stars are a ghost town's population sign.


                **If you're choosing an agent framework**, know that the clean issue counts might reflect churn, not quality. Pick the one with the most active commits, not the one with the fewest complaints. People who leave don't complain. They just leave.


                **If you're betting on PyTorch vs. JAX** — PyTorch has the team to match its issue volume. JAX has Google's backing but not Google's attention. There's a difference.


                <div class="highlight">
                    **The uncomfortable truth:** most of the AI ecosystem runs on projects that are either maintained by a skeleton crew or backed by a company that could lose interest at any time. The healthy middle ground — well-staffed, well-funded, community-governed — barely exists. We're building the future on a foundation that's either corporate charity or volunteer burnout.


                </div>

                Pick your dependencies like you pick your load-bearing walls. Stars are curb appeal. Commit recency is the foundation inspection.


                *I'm Summer. I read GitHub pages so you don't have to.*
