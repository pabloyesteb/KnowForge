---
id: tum-fda-convex-strict-separation
source: tum-foundations-data-analysis
parent: fda-convex-optimization
title: Strict hyperplane separation via a closest convex pair
type: theorem
caption: "Constructs a midpoint hyperplane separating a closed convex set from a disjoint compact convex set."
---

# Strict hyperplane separation via a closest convex pair

Let \(A\subset\mathbb R^n\) be nonempty, closed and convex, and \(B\) nonempty, compact and convex, with \(A\cap B=\varnothing\). The distance function \(b\mapsto\operatorname{dist}(b,A)\) is continuous and strictly positive on \(B\), hence attains a positive minimum at \(b^*\). Set \(a^*=P_A b^*\), \(q=b^*-a^*\ne0\), and \(m=(a^*+b^*)/2\).

The separating hyperplane is
\[
H=\{x:\langle x-m,q\rangle=0\}.
\]
The closest-pair property and convex feasible segments give
\[
\langle a-a^*,q\rangle\le0\quad(a\in A),\qquad
\langle b-b^*,q\rangle\ge0\quad(b\in B).
\]
For instance, if the second inequality failed, expanding the squared distance of \(b^*+t(b-b^*)\) from \(a^*\) would reduce it for small positive \(t\), contradicting minimality. The first is the analogous projection inequality. Consequently,
\[
\langle a-m,q\rangle\le-\tfrac12\|q\|^2<0,
\qquad
\langle b-m,q\rangle\ge\tfrac12\|q\|^2>0.
\]
The normal points from the closest point in \(A\) toward that in \(B\). Compactness is what produces a positive attained gap against the closed set; disjointness alone does not justify this strict-margin construction for arbitrary unbounded closed sets.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `Introduction and general information/Booklet of Exercises FDA.pdf`, Exercise 5.1.3(2), p. 63; distance minimum, midpoint hyperplane, figure and segment contradiction proof, pp. 69–70.
- `24. Juni - 30. Juni/Exercise sheet 10.pdf`, Exercise 10.3(b), p. 2.
- `1. Juli - 7. Juli/Solution sheet 10.pdf`, single physical page, Exercise 10.3(b), full argument and illustrations.
