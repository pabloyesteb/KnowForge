---
id: tum-fda-convex-geometry
source: tum-foundations-data-analysis
parent: fda-linear-geometry
title: Convex combinations and feasible-set geometry
type: concept
---

# Convex combinations and feasible-set geometry

A set \(C\) is convex if every segment \(\lambda x+(1-\lambda)y\), \(x,y\in C\), \(0\le\lambda\le1\), stays in \(C\). This two-point condition implies closure under every finite convex combination:
\[
x_1,\ldots,x_k\in C,\quad\theta_i\ge0,\quad\sum_i\theta_i=1
\quad\Longrightarrow\quad\sum_i\theta_ix_i\in C.
\]
Induct on the number of points. If \(\theta_1\ne1\), normalize the remaining coefficients by \(1-\theta_1\), combine them using the induction hypothesis, and then apply two-point convexity. If \(\theta_1=1\), the combination is just \(x_1\). Nonnegativity is required for every coefficient, not just the last one.

An affine hyperplane \(\{x:a^Tx=b\}\), \(a\ne0\), is convex because the affine equation is preserved under combinations with weights summing to one. Convexity is not the same as being a linear subspace: when \(b\ne0\), the hyperplane does not contain zero.

Nor do rank bounds generally define a linear space. For example two matrices \(\operatorname{diag}(1,0)\) and \(\operatorname{diag}(0,1)\) both have rank one, while their sum has rank two. Linear combinations therefore cannot in general be used as feasible operations for rank-constrained matrix problems in the same way as for a subspace. Convex feasible geometry is the hypothesis later used in the projection theorem.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `Introduction and general information/Booklet of Exercises FDA.pdf` (10 June 2024), Exercise 1.1.1, p. 3; solution, p. 7; further exercise “low-rank matrix space”, p. 6.
- `15. April - 21. April/Exercise sheet 0.pdf`, Exercise 0.1, p. 1.
