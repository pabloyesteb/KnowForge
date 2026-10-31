---
id: tum-co-mst-membership
source: tum-combinatorial-optimization
parent: co-trees-matroids
title: MST uniqueness and membership in the union of all optimum trees
type: method
caption: "Uses fundamental-path maximum costs to identify all edges that can occur in a minimum spanning tree."
---

# MST uniqueness and membership in the union of all optimum trees

Distinct costs on every pair of edges imply a unique minimum spanning tree. For a precise exchange proof, suppose two optimum trees differ and select the cheapest edge in their symmetric difference, say \(e\in T_1\setminus T_2\). Deleting \(e\) from \(T_1\) gives a cut. The cycle in \(T_2+e\) contains another edge \(f\) crossing that cut; \(f\notin T_1\) and thus \(c(f)>c(e)\). Replacing \(f\) in \(T_2\) by \(e\) improves it, a contradiction. Selecting this cheapest differing edge supplies the ordering that the sheet solution leaves implicit in its “without loss of generality” step. Equal costs permit multiple optima but do not force them.

To find the union of the edge sets of all MSTs, first compute any one optimum \(T\). Every edge of \(T\) belongs to the union. For a non-tree edge \(e=\{u,v\}\), let \(M_e\) be the maximum cost along the unique \(u\)-to-\(v\) tree path. Optimality gives \(c(e)\ge M_e\).

- If \(c(e)=M_e\), exchange \(e\) with a maximum-cost path edge. The result is another optimum containing \(e\).
- If \(c(e)>M_e\), no optimum can contain \(e\). Otherwise deleting it from that optimum gives a cut crossed by some edge \(f\) on the original tree path; \(c(f)\le M_e<c(e)\), giving a strictly improving exchange.

A tree search computes \(M_e\) in \(O(n)\). Testing all non-tree edges plus the initial \(O(mn)\) MST construction therefore takes \(O(mn)\). This computes edges appearing in at least one optimum, rather than edges common to every optimum. The official solution's concluding “every” wording must be read in light of its stated union task and exchange construction.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Problem Sheets/Exercise Sheet 2/exercise_sheet_2.pdf`, Exercises 2–3, p. 1.
- `Problem Sheets/Exercise Sheet 2 - solutions/exercise_sheet_2 - sol.pdf`, uniqueness exchange, p. 1, and full union-of-MSTs criterion/algorithm, p. 2.
- `Lecture Notes/lecture notes.pdf`, Theorem 2.4, pp. 12–14, fundamental cut/cycle optimality conditions.
