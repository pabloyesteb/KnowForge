---
id: tum-co-nonnegative-cost-reduction
source: tum-combinatorial-optimization
parent: co-min-cost-flow
title: Removing negative finite-capacity costs by saturated-arc reversal
type: method
caption: "Transforms negative-cost variables into reversed residual variables while preserving feasibility and tracking a constant objective offset."
---

# Removing negative finite-capacity costs by saturated-arc reversal

For each negative-cost original arc \(e=(v,w)\) with finite capacity \(U\), substitute \(f'(w,v)=U-f(v,w)\). Replace the arc by a distinct reverse arc of capacity \(U\) and cost \(-c(e)>0\). Adjust balances to \(b'(v)=b(v)-U\), \(b'(w)=b(w)+U\); apply these adjustments additively over all changed arcs. Keep unchanged arcs and their costs.

The substitution is a bijection between feasible original and transformed flows: interval bounds are preserved, and the balance adjustment accounts for the fictitious initial saturation of the negative arc. Parallel arcs may appear and must retain their identities. Defining \(C=\sum_{c(e)<0}c(e)u(e)\), direct substitution gives
\[
c'(f')=c(f)-C,\qquad\min c(f)=\min c'(f')+C.
\]
Thus solving an instance with nonnegative costs recovers the original optimum after restoring the constant offset. The final solution-sheet display confuses flow symbols with objective values; the equation above follows from its preceding per-edge calculation. Infinite negative-cost capacities cannot be saturated to a finite constant, so this construction applies to the finite-capacity setting of this exercise.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Problem Sheets/Exercise Sheet 6/exercise_sheet_6.pdf`, Exercise 3, p. 1; `Problem Sheets/Exercise Sheet 6 - solutions/exercise_sheet_6 - sol.pdf`, Exercise 3, p. 2, full substitution and offset derivation.
