---
id: tum-co-nonmatroid-systems
source: tum-combinatorial-optimization
parent: co-trees-matroids
title: Augmentation failures in knapsack, matching, clique and tour systems
type: concept
caption: "Exhibits concrete hereditary feasible families whose lack of augmentation prevents general matroid greedy guarantees."
---

# Augmentation failures in knapsack, matching, clique and tour systems

Hereditary feasibility does not suffice for matroid structure. Counterexamples identify an independent \(I\) smaller than \(J\), with no element of \(J\setminus I\) addable to \(I\).

For knapsack with capacity 10 and item weights \(9,5,5\), the singleton weight-nine item and the pair of weight-five items are both maximal feasible sets with different cardinalities. Neither weight-five item can augment the singleton. This shows the knapsack family is not a matroid in general; special capacities/weights can still define matroids.

For matching on a four-vertex path \(a-b-c-d\), take \(I=\{bc\}\) and \(J=\{ab,cd\}\). Each proposed addition shares an endpoint with \(bc\), violating matching feasibility. For clique vertex sets, a disjoint triangle and edge give maximal cliques of sizes three and two, again violating augmentation.

The traveling-salesman independence family consists of edge sets contained in some Hamiltonian cycle of a complete graph. It contains the empty set and is hereditary, but need not be a matroid. A concrete four-vertex instance has \(I=\{12,23,34\}\) and Hamiltonian cycle \(J=\{12,24,34,13\}\). The set \(I\) is contained in the cycle closed by edge 14; adding either edge of \(J\setminus I=\{24,13\}\) creates a vertex of degree three, impossible in any Hamiltonian cycle. Thus \(|I|=3<4=|J|\) but no augmentation is possible. This makes explicit the sheet's two-edge tour-switch obstruction.

These failures concern the displayed feasible-set systems. They do not say every instance lacks a greedy optimum, only that the matroid theorem cannot promise success for every objective weight.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Lecture Notes/lecture notes.pdf`, Example 2.18 and Figure 12, p. 19, clique obstruction.
- `Lecture Notes/class notes for 03 May.pdf`, physical pp. 11–13, knapsack capacity-10 example and different-sized bases.
- `Problem Sheets/Exercise Sheet 3/exercise_sheet_3.pdf`, Exercise 2(a–c), p. 1; `Problem Sheets/Exercise Sheet 3 - solutions/exercise_sheet_3 - sol.pdf`, corresponding augmentation counterexamples, p. 2.
