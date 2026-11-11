---
id: tum-co-matching-perfect-reductions
source: tum-combinatorial-optimization
parent: co-bipartite
title: Weight shifts and completion for perfect matching
type: method
caption: "Separates cardinality priority from weight optimization and identifies limits of zero-weight completion."
---

# Weight shifts and completion for perfect matching

To solve maximum-weight perfect matching using an optional maximum-weight matching solver, let \(S=\sum_{e\in E}|w(e)|\) and replace every weight by \(w'(e)=K+w(e)\), with \(K=1+2S\). A one-edge cardinality gain outweighs any difference of original matching weights. An optimum therefore has maximum cardinality. If it is not perfect, no perfect matching exists; among perfect matchings, the common added term \(K|V|/2\) cancels, so original weight is maximized. The shift has polynomial encoding size for rational weights.

Sheet 9 proposes the reverse direction by adding a dummy vertex if necessary, completing to an even complete graph with zero-weight new edges, solving perfect matching, and retaining original edges. This preserves optional matching for nonnegative original weights: an optimum can be extended across unmatched vertices without losing weight, and every perfect solution restricts to an original matching. As written it fails for arbitrary signed weights, because an existing negative edge cannot be replaced by an added zero edge on the same pair. A graph of two vertices with its sole edge of weight −1 has optional optimum zero but forced perfect weight −1. Thus its unrestricted reverse-reduction claim is not justified by that construction.

The later lecture makes its positive-weight assumption explicit. For optional matching, first discard nonpositive edges, since removing them never reduces weight. Complete that retained graph with zero-weight edges and, if needed, an extra vertex to obtain even order. An optimal retained matching leaves no positive edge between unmatched vertices, so it can be completed using zero-weight edges; restricting an optimal perfect solution back to retained edges recovers an optimum. This preprocessing repairs the signed-weight limitation of the earlier exercise. The claim that every arbitrary matching extends with exactly equal weight is too strong; extension of an optimum suffices.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Problem Sheets/Exercise Sheet 9/exercise_sheet_9.pdf`, Exercise 2, p. 1; `Problem Sheets/Exercise Sheet 9 - solutiors/exercise_sheet_9 - sol.pdf`, Exercise 2, pp. 1–2, zero-weight completion and cardinality-prioritizing weight-shift constructions.
- `Lecture Notes/lecture notes.pdf`, §4.5, Lemma 4.18, p. 82; `Lecture Notes/class notes for 12 July.pdf`, physical p. 19, positive-weight completion reduction.
