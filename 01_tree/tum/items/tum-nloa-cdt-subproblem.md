---
id: tum-nloa-cdt-subproblem
source: tum-nonlinear-optimization
parent: nloa-cq-kkt
title: KKT formulation of the Celis–Dennis–Tapia two-constraint subproblem
type: method
caption: "Establishes Slater feasibility and derives KKT equations for a quadratic model with trust-region and residual-norm constraints."
---

# KKT formulation of the Celis–Dennis–Tapia two-constraint subproblem

Consider the quadratic objective with a trust-region and residual-norm bound:
\[
\min_x x^THx+2b^Tx,\qquad
\|x\|^2\le\Delta^2,\quad\|A^Tx+c\|^2\le\xi^2,
\]
where \(H\) is symmetric, \(\Delta>0\), \(A\in\mathbb R^{n\times m}\), and
\[
\xi>\min_{\|x\|\le\Delta}\|A^Tx+c\|.
\]
The minimum on the right exists by compactness. A minimizing \(y^*\) strictly satisfies the residual bound. If it lies on the trust-region boundary, the scaled points \((1-1/(2k))y^*\) satisfy the trust-region inequality strictly, and retain the strict residual inequality for large \(k\) by continuity. Thus a Slater point exists for these convex constraints.

At a local minimizer, KKT therefore has nonnegative \(\lambda_1,\lambda_2\) satisfying primal feasibility and
\[
2H\bar x+2b+2\lambda_1\bar x
+2\lambda_2A(A^T\bar x+c)=0,
\]
\[
\lambda_1(\|\bar x\|^2-\Delta^2)=0,\qquad
\lambda_2(\|A^T\bar x+c\|^2-\xi^2)=0.
\]
Symmetry of \(H\) suffices for this formulation; positive semidefiniteness is not assumed. Convex constraints alone do not make an indefinite quadratic objective convex or make every KKT point globally optimal. The exercise derives the system and qualification, not a numerical solver for it.

## Source references

Archive: `00_sources/raw/tum/archives/NLOA (W24_25)_20261012_1553.zip`; `Exercise materials/Exercise Sheet 4.pdf`, T.4.5, p. 2, and `Exercise materials/Solution Exercise Sheet 4.pdf`, Solution 4.5, p. 5.
