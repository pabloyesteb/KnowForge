---
id: tum-co-mean-cycle-canceling
source: tum-combinatorial-optimization
parent: co-min-cost-flow
title: Minimum-mean cycle cancellation and convergence bounds
type: algorithm
caption: "Uses residual cycle means and bottleneck reversals to control repeated cost-improving circulation updates."
---

# Minimum-mean cycle cancellation and convergence bounds

First find any feasible \(b\)-flow or report infeasibility. Repeatedly find a minimum-mean cycle in the residual graph. If its mean is nonnegative (or no cycle exists), residual optimality proves minimum cost. Otherwise augment by its bottleneck, preserving balances and reducing cost. Integral supplies and capacities preserve integral flows.

Choosing the most negative total cycle cost instead of the most negative mean can cause exponentially many updates. The four-vertex example has outer capacity-\(N\) arcs of cost −1, a unit bottleneck of cost −2 and a return arc of capacity \(2N\), cost −100. Two three-arc cycles each have mean −34 and can carry \(N\). Alternating longer cycles can carry only one at a time despite an initially more negative total cycle cost. Reverse-arc costs must change sign when the residual orientation reverses. Arbitrary cycle cancellation can also fail to terminate for irrational data; the minimum-mean rule has stronger progress properties.

Let \(\mu(f)<0\) be the current minimum residual mean. Combining consecutive chosen cycles, retaining repeated arc copies and cancelling opposite pairs, gives an Eulerian multigraph within the earlier residual graph. Its cycle decomposition has mean at least \(\mu(f)\), while cancelled pairs have zero total cost. Since the old mean is negative, the length inequality proves \(\mu\) never decreases. If earlier/later chosen cycles contain opposite orientations, the removal of at least two arc copies yields the stronger inequality \(\mu(f_k)\le n\mu(f_\ell)/(n-2)\) for \(n>2\), equivalently \(|\mu(f_\ell)|\le(1-2/n)|\mu(f_k)|\).

Each augmentation exhausts a residual arc. Repeated use of bottleneck orientations requires a reversal, so such progress occurs within \(O(m)\) updates. Repeating for \(O(n)\) blocks halves the magnitude of the negative mean, because \((1-2/n)^n<1/2\). This is the source's bottleneck/progress argument; constants and endpoint indexing in its pigeonhole display are suppressed in the asymptotic statement.

For integer costs with \(C=\max_e|c(e)|\), every residual arc cost has magnitude at most \(C\), and a negative simple-cycle mean has magnitude at least \(1/n\). Thus \(O(mn\log(2+nC))\) updates suffice, each costing \(O(nm)\) for cycle computation, giving \(O(m^2n^2\log(2+nC))\) arithmetic operations. The source writes its initial bound using only the smallest original cost; positive original costs can become negative residual costs, so using \(C\) safely covers arbitrary initial feasible flows and the all-nonnegative-original-cost case. Rational costs can be scaled to integers. These weakly polynomial bounds depend logarithmically on encoded cost magnitude. The notes additionally state a strongly polynomial \(O(m^3n^2\log n)\) bound and refer its proof to Korte–Vygen; they do not derive it here.

The Sheet 8 scaffold represents each arc by capacity/cost pairs, forbids original antiparallel arcs and preassigns reverse costs with opposite sign. Its completion obtains an initial feasible flow by auxiliary-source/sink Edmonds–Karp, strips the auxiliaries, and repeatedly cancels a negative minimum-mean cycle by its bottleneck. The helper copies only positive-capacity residual arcs into the cost graph and adds a fresh source with no incoming arcs or self-loop, avoiding the Sheet 7 generator's artificial cycles. The final cost loop skips original positive-capacity entries and instead sums negative residual reverse flows times negative reverse costs; under the stated no-antiparallel convention this still equals the original flow cost, despite the contrary comment. Absent infinite-cost entries contribute zero. The input must satisfy balanced supplies/demands: saturating all auxiliary supply arcs alone does not certify excess demand when the balance sum is nonzero. These are supplied educational routines and their static behavior, not attributed personal implementations or measured performance.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Lecture Notes/lecture notes.pdf`, §3.7.1, pp. 55–56, naive example/Algorithm 8; §3.7.3, pp. 58–62 through Lemma 3.41, full monotonicity, reversal, halving and integer-cost arguments.
- `Lecture Notes/class notes for 14 June.pdf`, physical pp. 5–10, arbitrary cycle cancellation, Bellman–Ford recap and complete two-versus-2N example.
- `Lecture Notes/class notes for 21 June.pdf`, physical pp. 1–16, minimum-mean computation and complete monotonicity/reversal/convergence arguments.
- `Problem Sheets/Exercise Sheet 8/exercise_sheet_8.pdf`, Exercises 2–3, pp. 1–3; `Problem Sheets/Exercise Sheet 8 - solutions/exercise_sheet_8 - sol.pdf`, Exercises 2–3, pp. 1, 3–4, irrational-capacity construction and full coding specification.
- `Problem Sheets/Exercise Sheet 8/main.py` and `Problem Sheets/Exercise Sheet 8/graph_module.py`, full driver/scaffold, feasibility and minimum-mean helpers.
- `Problem Sheets/Exercise Sheet 8 - solutions/code - sol.py` and `Problem Sheets/Exercise Sheet 8 - solutions/graph_module - complete.py`, full cycle-cancellation and cost completion.
