---
id: tum-fda-uniform-ball-boundary
source: tum-foundations-data-analysis
parent: fda-probability
title: Simultaneous boundary concentration and near-orthogonality in a uniform ball
type: theorem
caption: "Combines volume scaling and coordinate-slab bounds with finite union bounds for many independent points."
---

# Simultaneous boundary concentration and near-orthogonality in a uniform ball

For a uniform point in the unit ball of \(\mathbb R^d\), scaling volume gives
\[
\mathbb P(\|X\|_2\le\alpha)=\alpha^d,\qquad0<\alpha<1.
\]
Let \(X_1,\ldots,X_n\) be independent such points, \(n\ge2\). If \(a=1-2\log n/d\) lies in \((0,1)\), then \(a^d\le e^{-2\log n}=n^{-2}\). A union bound gives
\[
\mathbb P(\|X_i\|_2\ge a\text{ for every }i)\ge1-1/n.
\]
If \(a\le0\), the lower-norm condition is automatic. Thus many sampled points simultaneously lie near the boundary when \(d\) is large relative to \(\log n\).

For \(d\ge3\), condition on a nonzero \(X_i\), rotate \(X_i/\|X_i\|\) to a coordinate axis, and use independence and the uniform ball's rotational invariance. Since \(\|X_i\|\le1\),
\[
|\langle X_i,X_j\rangle|\le
|\langle X_i/\|X_i\|,X_j\rangle|.
\]
The coordinate-slab bound with \(c=\sqrt{6\log n}\) gives a per-pair failure bound \((2/c)n^{-3}\le n^{-3}\). Union over unordered pairs therefore implies
\[
\mathbb P\left(|\langle X_i,X_j\rangle|\le\sqrt{\frac{6\log n}{d-1}}
\text{ for all }i\ne j\right)\ge1-1/n.
\]
If the threshold is at least one, this inner-product condition is already automatic. Combining the two events gives probability at least \(1-2/n\). These are inner products of ball points; a bound on the cosine of their angle additionally uses their lower norm bounds. Small norms alone would not certify nearly orthogonal directions.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `Introduction and general information/Booklet of Exercises FDA.pdf`, Exercise 4.1.3(a–b), p. 58; volume scaling and union-bound solutions, p. 61.
- `17. Juni - 23. Juni/Exercise sheet 9.pdf`, Exercise 9.4(a–b), p. 2; `24. Juni - 30. Juni/Solution Sheet 9.pdf`, single physical page, Exercise 9.4(a–b), radial-volume argument and finite union bound.
