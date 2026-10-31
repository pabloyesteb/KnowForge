---
id: tum-co-matroid-greedy
source: tum-combinatorial-optimization
parent: co-trees-matroids
title: Greedy optimization characterizes matroids
type: theorem
caption: "Proves that descending-weight feasible insertion is optimal for every nonnegative weighting exactly for matroid independence systems."
---

# Greedy optimization characterizes matroids

Sort elements of a finite independence system by nonincreasing nonnegative weight. Begin with \(G=\varnothing\) and insert each element if the result remains independent. This algorithm finds a maximum-weight independent set for every nonnegative rational weighting if and only if the system is a matroid.

For sufficiency, the greedy set is a basis. An optimum can also be extended to a basis without lowering its weight, including when some weights are zero; thus both can be compared at the common rank \(r\). Write their elements in descending weight order as \(g_1,\ldots,g_r\) and \(f_1,\ldots,f_r\). If the optimum were heavier, some index \(q\) would have \(w(f_q)>w(g_q)\). Augmentation of \(\{g_1,\ldots,g_{q-1}\}\) by the independent prefix \(\{f_1,\ldots,f_q\}\) supplies a feasible element of weight at least \(w(f_q)\). That element was considered before \(g_q\) and was feasible then by heredity, so greedy could not have skipped it. This contradiction proves optimality.

For necessity, a nonmatroid has a restriction \(F\subseteq E\) with bases \(B_1,B_2\) of different sizes, say \(|B_1|>|B_2|\). Give elements of \(B_2\) weight \(1+\varepsilon\), those of \(B_1\setminus B_2\) weight 1, and all others weight zero. Greedy takes all of \(B_2\), and its maximality in \(F\) prevents later weight-one additions. The feasible \(B_1\) is heavier for sufficiently small positive rational \(\varepsilon\), since its cardinality advantage dominates the premium on \(B_2\setminus B_1\). Zero-weight additions outside \(F\) cannot repair the objective gap. The restriction is essential: a nonmatroid need not have different-sized bases on the full ground set, although the printed converse proof starts there.

The system is accessed through an independence oracle rather than an explicit list of all feasible subsets. Sorting costs \(O(|E|\log|E|)\) comparisons and the algorithm uses \(|E|\) independence tests; actual runtime must include each oracle's implementation. The abstract constant-time oracle assumption does not make graph cycle detection free. Kruskal follows by applying this greedy structure to the graphic matroid after converting minimum spanning-tree costs to nonnegative maximization weights.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Lecture Notes/lecture notes.pdf`, Problem 2.20, Theorem 2.21, Algorithm 3 and full proof/oracle discussion, pp. 20–22 (through paragraph immediately before Chapter 3).
- `Lecture Notes/lecture notes.pdf`, Theorem 2.19, p. 20, equal-cardinality characterization for every restriction; Remark 2.9, p. 16, MST weight conversion.
