---
id: tum-co-hungarian-assignment
source: tum-combinatorial-optimization
parent: co-bipartite
title: Hungarian alternating-tree assignment method
type: algorithm
caption: "Alternates tight-edge augmentation with slack-based potential updates until a certified perfect assignment is found."
---

# Hungarian alternating-tree assignment method

Maintain a matching of tight edges and a feasible vertex potential, initialized by row maxima on \(A\) and zeros on \(B\). Choose an uncovered root \(a\in A\), set \(S=\{a\},T=\varnothing\), and grow its alternating tree in the equality graph. An uncovered tight neighbor in \(B\setminus T\) gives an augmenting path; toggle it and start a new root, unless the matching is now perfect. A covered neighbor adds both that vertex to \(T\) and its matched partner to \(S\).

When \(N_p(S)=T\), decrease potentials on \(S\) and increase them on \(T\) by the minimum slack toward \(B\setminus T\). Tight tree edges and current matching edges are preserved: each matching pair is either entirely in the tree or entirely outside. The update exposes a new tight neighbor, so the search can continue without restarting. The rooted tree has \(|S|=|T|+1\); before augmentation, all reached right-side vertices are covered. Hence \(T\ne B\) while the matching is imperfect, ensuring the minimum-slack set exists in the complete balanced graph. End with a perfect matching and equal potential sum, which certifies maximum weight.

There are at most \(|A|\) augmentations and at most \(|B|\) new right-side vertices per rooted phase. The notes state an \(O(n^3)\) implementation but suppress bookkeeping: a fresh \(O(n^2)\) scan at every potential change would not establish that bound. Maintaining each unreached vertex's minimum slack and predecessor while adding left vertices supports \(O(n^2)\) work per phase and the stated total. The procedure must test for perfection before choosing the next uncovered root; the handwritten version supplies this termination guard missing from the printed line after augmentation.

The lecture's three-by-three example ends with weight 12 and potentials \((0,6,3)\) on the left and \((1,2,0)\) on the right, also summing to 12. Sheet 10 balances its four-by-two nonnegative instance by two dummy right-side vertices and fills absent edges with zero weight. The final perfect assignment uses weights 9, 6, 0, 0, giving optional original matching weight 15. Its final potentials \((0,1,0,2)\) and \((7,5,0,0)\) sum to 15. Zero completion is appropriate for this nonnegative instance; the task's “maximal” terminology denotes maximum weight.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Lecture Notes/lecture notes.pdf`, §4.4, pp. 78–81, Algorithm 12, Theorem 4.17 and all Figure 36 diagrams.
- `Lecture Notes/class notes for 05 July.pdf`, physical pp. 24–27, algorithm outline and potential update.
- `Lecture Notes/class notes for 12 July.pdf`, physical pp. 4–18, full algorithm, runtime statement and worked diagrams including repeated/out-of-order panels.
- `Problem Sheets/Exercise Sheet 10/exercise_sheet_10.pdf`, Exercise 2, p. 1; `Problem Sheets/Exercise Sheet 10 - solutions/exercise_sheet_10 - sol.pdf`, Exercise 2, pp. 1–4, full balancing construction and all fifteen execution panels.
