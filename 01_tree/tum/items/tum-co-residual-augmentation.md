---
id: tum-co-residual-augmentation
source: tum-combinatorial-optimization
parent: co-max-flow
title: Residual augmentation and Ford-Fulkerson termination
type: algorithm
caption: "Updates forward and reverse residual arcs and distinguishes integral, rational and irrational capacity behavior."
---

# Residual augmentation and Ford-Fulkerson termination

For a feasible flow in a network without antiparallel original arcs, each original \(e=(v,w)\) contributes a forward residual arc of capacity \(u(e)-f(e)\) if positive, and a reverse arc \((w,v)\) of capacity \(f(e)\) if positive. A reverse traversal cancels previously sent flow; it does not add flow to a new original connection.

On a residual source-sink path, let \(\gamma\) be the smallest residual capacity. Increase original flow by \(\gamma\) on forward traversals and decrease it by \(\gamma\) on reverse traversals. The bottleneck guarantees capacity feasibility, while one incoming and one outgoing path adjustment preserve each internal balance. Net source outflow increases by \(\gamma>0\).

Ford-Fulkerson starts from zero and repeats arbitrary residual-path augmentations until none exists. With integral capacities every flow and bottleneck remains integral, each augmentation increases the value by at least one, and cut bounds force finite termination. In particular an integral maximum flow exists. Rational capacities reduce to this argument by multiplying by a common denominator and scaling back. This proves termination, not a polynomial bit-complexity bound.

In the four-vertex example, four outer arcs have capacity \(N\) and the middle arc capacity 1. Choosing the two outer paths attains value \(2N\) in two augmentations. Alternating paths using the middle arc forward and backward can instead require \(2N\) unit augmentations. Since \(N\) takes only logarithmically many bits, arbitrary path selection can be exponential in input length. The notes further state that irrational capacities can cause nontermination and even convergence to a suboptimal limiting value; no explicit irrational construction is developed on these pages.

The worked six-vertex sequence illustrates cancellation on reverse residual arcs and ends with the capacity-six cut certificate. It is evidence of algorithm execution on that diagram, not a runtime benchmark.

Backward residual arcs are essential to global optimality. Sheet 4 gives a unit-capacity \(C\times C\) grid directed rightward and downward, with source arcs into the left column and sink arcs out of the right column. Sending one unit on a staircase from the top-left to bottom-right can block every remaining forward-only route: along the staircase, the boundary from its vertices to the vertices below/left consists of saturated staircase arcs. Yet \(C\) horizontal row paths attain value \(C\). Omitting all backward arcs therefore permits an arbitrarily poor ratio \(1/C\). The solution's prose says “left” in the staircase; the diagram's horizontal arrows go right. In contrast, deleting only backward arcs entering the source does not remove a simple source-sink augmenting path, since such a path never revisits its source.

The separate four-vertex execution task has maximum flow 4. Its official solution reports four unit augmentations under a minimum-bottleneck Ford-Fulkerson selection and two shortest-path augmentations for Edmonds-Karp. The final value is fixed; arbitrary Ford-Fulkerson iteration counts depend on path choices.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Lecture Notes/lecture notes.pdf`, §3.2, pp. 25–30, Definitions 3.6–3.7, Algorithm 4, integrality/scaling and irrational-capacity discussion, Figures 16–19.
- `Problem Sheets/Exercise Sheet 4/exercise_sheet_4.pdf` and `Problem Sheets/Exercise Sheet 4 - solutions/exercise_sheet_4 - sol.pdf`, Exercises 2–3, task pp. 1–2, solution pp. 2–3, including directed grid Figure 2.
- `Lecture Notes/class notes for 17 May.pdf`, physical pp. 9–23, residual capacities, augmentation, full worked sequence and integral-capacity example.
