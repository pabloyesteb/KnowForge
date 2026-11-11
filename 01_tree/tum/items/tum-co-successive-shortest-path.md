---
id: tum-co-successive-shortest-path
source: tum-combinatorial-optimization
parent: co-min-cost-flow
title: Successive shortest paths for minimum-cost flows
type: algorithm
caption: "Maintains residual optimality while routing integral supplies to demands along minimum-cost paths."
---

# Successive shortest paths for minimum-cost flows

Assume integral capacities and balances, total balance zero, and conservative original costs: no negative-cost directed cycle. Write \(B=\frac12\sum_v|b(v)|\). Start with zero flow and routed balances \(\hat b=0\). Choose \(s\) with \(b(s)>\hat b(s)\) and a reachable \(t\) with \(b(t)<\hat b(t)\). Compute a minimum-cost residual path, allowing negative residual arc costs, and augment by
\[
\gamma=\min\{\min_{e\in P}u_f(e),\ b(s)-\hat b(s),\ \hat b(t)-b(t)\}.
\]
Increase \(\hat b(s)\) by \(\gamma\), decrease \(\hat b(t)\) by \(\gamma\), and repeat until \(\hat b=b\). Shortest means cost, not edge count; the demand update corrects the misprinted right-hand side in Algorithm 10.

The key invariant is that the current flow minimizes cost for its current balances. If an optimal flow is augmented along a cheapest residual path by any positive amount at most its bottleneck, the resulting flow is optimal for the balances changed by that actual amount. Otherwise its residual graph has a negative cycle. Combine that cycle with the old path, retaining arc multiplicities and cancelling reverse pairs. All remaining arcs belonged to the earlier residual graph. Decompose into an alternative source–target path and cycles. Earlier optimality makes those cycles nonnegative, so the alternative path would be cheaper than the chosen path, a contradiction. The theorem's balance change must use the actual augmentation, rather than its full bottleneck when a smaller amount is chosen.

If no deficient target is reachable from a remaining supply vertex, let \(R\) be its residual reachable set. Every vertex in \(R\) satisfies \(b\ge\hat b\), strictly at the source. Outgoing original arcs are saturated and incoming original arcs carry zero, giving \(b(R)>\hat b(R)=u(\delta^{out}(R))\), an infeasibility certificate. Otherwise every integral augmentation removes at least one unit of remaining supply, giving at most \(B\) iterations. Bellman–Ford is applicable because the invariant excludes negative residual cycles, and gives \(O(Bnm)\) time. This is pseudopolynomial in binary-encoded balances. The notes state an improved \(O(nm+B(m+n\log n))\) implementation and refer its proof elsewhere.

Conservative original costs are necessary for this zero-flow initialization: with all balances zero, it returns immediately even if a negative cycle could improve cost. Sheet 8's conservative signed-cost network finishes in four augmentations of sizes 3, 4, 1, 1 and cost 29; the last two paths use reverse arcs to revise earlier routing.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Lecture Notes/lecture notes.pdf`, §3.8, pp. 62–65, Theorems 3.42–3.45 and Algorithm 10.
- `Lecture Notes/class notes for 21 June.pdf`, physical pp. 16–22, assumptions, update and optimality proof.
- `Problem Sheets/Exercise Sheet 8/exercise_sheet_8.pdf`, Exercise 1, p. 1; `Problem Sheets/Exercise Sheet 8 - solutions/exercise_sheet_8 - sol.pdf`, Exercise 1, pp. 1–2, full path/flow diagrams.
- `Lecture Notes/class notes for 28 June.pdf`, physical pp. 1–11, repeated setup and complete feasibility/iteration/runtime proof.
