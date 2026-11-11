---
id: tum-co-parametric-cycle-t-join
source: tum-combinatorial-optimization
parent: co-general-matching
title: Minimum cycle mean by parametric empty-join optimization
type: algorithm
caption: "Uses decreasing mean thresholds and shrinking edge sets with a polynomial minimum-join oracle."
---

# Minimum cycle mean by parametric empty-join optimization

Assume a polynomial solver for minimum-cost \(T\)-join, including signed costs. For \(T=\varnothing\), feasible edge sets have all degrees even and decompose into edge-disjoint cycles. Write \(q_a(F)=c(F)-a|F|\), and for nonempty sets \(\bar q_a(F)=c(F)/|F|-a\). These two quantities must be distinguished: the oracle minimizes the total shifted cost \(q_a\), not the mean.

Start at \(a=\max_ec(e)\). Solve the minimum empty-join problem with edge costs \(c(e)-a\). If its optimum is negative, the returned set is nonempty and update \(a\leftarrow a+\bar q_a(F)=c(F)/|F|\). At the new threshold this same set has shifted cost zero. If the next oracle optimum is zero, no cycle has smaller mean; retain the preceding nonempty set and extract a cycle from it. The empty edge set is always feasible and has total cost zero, so it cannot be used in a mean or as a cycle witness. Acyclicity must be checked separately; if the first optimum is zero in a cyclic graph at this initial threshold, every cycle has mean equal to that threshold and any cycle suffices.

For consecutive negative-optimum sets \(F,H\), optimality at the old threshold gives \(q_a(H)\ge q_a(F)\). At the new threshold \(a'=c(F)/|F|\),
\[
0>q_{a'}(H)=q_a(H)-q_a(F)|H|/|F|\ge q_a(F)(1-|H|/|F|).
\]
Since \(q_a(F)<0\), this forces \(|H|<|F|\). Thresholds also strictly decrease. Thus there are at most \(m\) improving oracle calls. At termination any positively weighted cycle component of the retained zero-shift-cost even subgraph has the optimal mean, by the weighted-average bound and absence of negative shifted cycles. This is a conditional polynomial reduction; the lecture's pseudopolynomial cancellation solver alone does not satisfy its oracle premise. The exercise's description says to increase costs, but the displayed mean update decreases the threshold; its empty-set and mean/total notation require the guards above.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Problem Sheets/Exercise Sheet 11/exercise_sheet_11.pdf`, optional Exercise 3(a–f), p. 2, full algorithm and oracle premise.
- `Problem Sheets/Exercise Sheet 11 - solutions/exercise_sheet_11 - sol.pdf`, Exercise 3, pp. 2–3, shifted objectives, full cardinality/threshold argument and cycle extraction.
