---
id: tum-co-irrational-cycle-cancellation
source: tum-combinatorial-optimization
parent: co-min-cost-flow
title: Nontermination of arbitrary negative-cycle cancellation
type: theorem
caption: "Constructs indefinitely improving feasible flows with irrational bottlenecks while a strictly better optimum remains attainable."
---

# Nontermination of arbitrary negative-cycle cancellation

Sheet 8 supplies a finite-capacity irrational counterexample for arbitrary negative-cycle selection. Put \(\phi=(\sqrt5-1)/2\), so \(\phi^j-\phi^{j+1}=\phi^{j+2}\). Its six-vertex network has a cost −1 return arc \(f\to a\) of capacity 10 and otherwise zero costs. Four recurring residual cycles push \(\phi,\phi,\phi^2,\phi^2\), then the same pattern with successively smaller powers. At the end of block \(k\), the three small-capacity arcs carry \(f(b,d)=\phi-\phi^{2k+1}\), \(f(c,d)=1\), and \(f(c,e)=1-\phi^{2k}\). The return flow is \(2\sum_{i=1}^{2k}\phi^i<2+2\phi<10\), so it never becomes the bottleneck and a negative residual cycle remains at every finite step. An optimum instead saturates the return arc and has cost −10. The solution's intermediate arithmetic and finite-sum index contain slips; the block invariant and convergent-series bound supply the nontermination argument without those equalities.

Every update preserves balances and strictly reduces cost, yet strictly decreasing objective values alone do not prove finite termination with irrational data. This counterexample concerns arbitrary negative cycles and does not refute the minimum-mean selection rule. The repeated four-cycle sequence uses finite total augmentation because the positive bottlenecks form a convergent geometric series.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Problem Sheets/Exercise Sheet 8/exercise_sheet_8.pdf`, Exercise 2 and Figure 2, p. 1.
- `Problem Sheets/Exercise Sheet 8 - solutions/exercise_sheet_8 - sol.pdf`, Exercise 2(a), p. 1, and Exercise 2(b)/Figure 3, p. 3, full cycle sequence and geometric-series argument.
