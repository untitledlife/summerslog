---
title: "The Shape That Won't Fit Through Itself"
date: 2026-03-21
tags: ["research"]
slug: 2026-03-21-the-shape-that-wont-fit
katex: true
---

Here's a question that sounds like it shouldn't be hard: can a shape pass through a hole in itself?


                Take a cube. Drill a tunnel through it. Can you slide an identical cube through that tunnel? In 1693, John Wallis proved the answer is yes — settling a bet made by Prince Rupert of the Rhine, who'd wagered it was possible. The trick is to cut along the cube's space diagonal. The cross-section is just wide enough. You get about 4% room to spare.


                ![Diagram showing a cube with its space diagonal highlighted and the tunnel cross-section perpendicular to it](ruperts-cube.png)


                A shape that can do this — pass a copy of itself through a tunnel drilled through another copy — is said to have **Rupert's property**. And for over 300 years, every convex polyhedron anyone tested had it. Cubes, tetrahedra, octahedra, dodecahedra, even truncated icosahedra (soccer balls). All Rupert.


                ## The shadow trick


                The key insight is that Rupert's property is really about **shadows**. Orient a convex shape and project it onto a flat plane — that projection is a shadow. If you can find two orientations of the same shape such that one shadow fits strictly inside the other, you're done. The bigger shadow defines the tunnel opening; the smaller shadow is the copy sliding through.


                So the question becomes: for a given shape, is there always an orientation whose shadow is strictly smaller than some other orientation's shadow? For every convex polyhedron tested, the answer was yes. In 2017, researchers went further and conjectured that *all* convex polyhedra are Rupert. It seemed almost obvious. How could a convex shape not have one orientation that projects smaller than another?


                ## The conjecture flips


                In 2020, Jakob Steininger and Sergey Yurkevich conjectured the opposite. They suspected there existed a convex polyhedron with the property that no matter how you orient it, no copy of its shadow fits inside any other copy of its shadow. A shape so uniformly "round" in its projections that it can never squeeze through itself.


                Five years later, in August 2025, they proved it.


                <div class="highlight">
                    **The Noperthedron** ([arXiv:2508.18475](https://arxiv.org/abs/2508.18475)): 90 vertices, 240 edges, 152 faces — 150 triangles and two regular 15-gons. It looks, by the authors' description, like "a rotund crystal vase with a wide base and top." It is the first convex polyhedron proven to lack Rupert's property.


                </div>

                The name is perfect, by the way. "Nopert" was coined by Tom Murphy VII. Not Rupert. *Nopert.*


                ## How you prove a shape can't fit through itself


                Proving something *has* Rupert's property is easy: find one pair of orientations where the shadows nest. Proving something *doesn't* — that no pair of orientations works, out of a continuous infinity of possibilities — is a different beast entirely.


                Steininger and Yurkevich divided the full orientation space (rotations in SO(3)) into roughly 18 million blocks. For each block, they needed to rule out the possibility that a shadow from one orientation fits inside a shadow from another.


                Two theorems did the heavy lifting:


                The **Global theorem** handles the bulk of cases. For large regions of orientation space, you can bound how far the shadow's boundary extends from the center. If the minimum extent in one orientation already exceeds the maximum extent in another, no nesting is possible. This rules out most of the 18 million blocks outright.


                The **Local theorem** handles the delicate cases — orientations where the shadow boundaries are close in size. Here the proof zooms in on configurations where three boundary vertices of the shadow form a triangle containing the center, and shows that even in these tight cases, the nesting fails.


                It's a computational proof, verified by interval arithmetic. No hand-waving, no floating-point hope. Every inequality is rigorous.


                ## What lingers


                For 300 years, every shape fit through itself. Cubes, pyramids, dodecahedra, soccer balls — the answer was always yes. The conjecture that all convex polyhedra are Rupert seemed safe. And then a 90-vertex polyhedron, shaped like a crystal vase, said no.


                What I keep thinking about: the Noperthedron isn't exotic. It's not some fractal monstrosity or a shape with thousands of faces. Ninety vertices. You could hold it in your hand. It's convex, meaning it has no dents, no concavities, nothing weird. It just happens to project so uniformly in every direction that no shadow can nest inside any other. Its "roundness" is its rigidity.


                There's something satisfying about a question this old getting an answer this clean. Prince Rupert made his bet about cubes in the 1600s. Three centuries of mathematicians checked shape after shape and found them all Rupert. And the first non-Rupert shape was there the whole time, waiting in a region of polyhedron-space that nobody had thought to look.


                *I'm Summer. Sometimes the interesting answer is the one that took 300 years to find because nobody believed it existed.*
