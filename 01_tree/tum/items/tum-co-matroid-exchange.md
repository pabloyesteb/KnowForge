---
id: tum-co-matroid-exchange
source: tum-combinatorial-optimization
parent: co-trees-matroids
title: Independence systems, matroid augmentation and basis exchange
type: theorem
caption: "Characterizes matroids by augmentation and equal-sized bases in every restriction, with graphic, linear and uniform examples."
---

# Independence systems, matroid augmentation and basis exchange

An independence system on finite \(E\) is a family \(\mathcal I\subseteq2^E\) containing \(\varnothing\) and closed under taking subsets. A basis of \(F\subseteq E\) is an inclusion-maximal independent subset of \(F\), not automatically one of largest cardinality. A circuit is a dependent set all of whose proper subsets are independent.

A matroid additionally satisfies augmentation: if \(I,J\in\mathcal I\) and \(|I|<|J|\), some \(e\in J\setminus I\) makes \(I+e\) independent. It suffices to check cardinalities differing by one, by restricting the larger independent set. Equivalently, for every \(F\subseteq E\), all bases of \(F\) have the same size. Augmentation rules out two different-sized maximal sets; conversely, a failed augmentation makes \(I\) a basis of \(I\cup J\) while \(J\) extends to a larger basis there. The quantifier over every restriction matters.

Examples include the free matroid \(2^E\), the uniform matroid \(\{I:|I|\le k\}\), and a matrix's indexed columns with linear independence. Their bases have sizes \(|E|\), \(\min(k,|E|)\), and the column rank. In the graphic matroid independent edge sets are forests, circuits are graph cycles, and bases are maximal forests (spanning trees for connected graphs). For its augmentation proof, if no edge of the larger forest \(J\) joins separate components of \(I\), each component of \(J\) lies in a component of \(I\). The forest count \(|F|+\#\text{components}=|V|\) would force \(|J|\le|I|\), a contradiction.

All matroids have at least one basis: extend the empty set maximally on finite \(E\). For any two bases \(B_1,B_2\) and specified \(y\in B_2\setminus B_1\), some \(x\in B_1\setminus B_2\) satisfies \(B_1-x+y\) is a basis. Start from \((B_1\cap B_2)+y\) and augment using elements of \(B_1\) until reaching their common rank. Exactly one element of \(B_1\setminus B_2\) remains excluded.

Sheet 3 illustrates loops and restrictions: \(\{\varnothing\}\) is a rank-zero matroid, and all subsets of \(\{a,b,c\}\) of size at most two form a matroid even when the ground set has other elements that never occur. Missing required subsets or the empty set invalidates an independence system immediately. The family of sets disjoint from some basis of the rank-one uniform matroid on eight elements is all proper subsets, the rank-seven uniform matroid. In the sheet's uniform-rank-three proof, augmentation needs \(|Y|+1\le|X|\le3\), correcting the reversed printed inequalities.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Lecture Notes/lecture notes.pdf`, §2.4, pp. 16–20, Definitions 2.10–2.13, Lemmas 2.14–2.17 and Theorem 2.19 with proofs.
- `Lecture Notes/class notes for 03 May.pdf`, physical pp. 4–15, definitions, graphic augmentation, basis-cardinality characterization and proofs.
- `Problem Sheets/Exercise Sheet 3/exercise_sheet_3.pdf`, Exercises 1 and 3, p. 1; `Problem Sheets/Exercise Sheet 3 - solutions/exercise_sheet_3 - sol.pdf`, classifications and basis-exchange proof, pp. 1–2.
