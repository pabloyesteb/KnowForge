---
id: tum-nloa-tangent-cones
source: tum-nonlinear-optimization
parent: nloa-existence-geometry
title: Tangent cones and convex feasible directions
type: theorem
---

# Tangent cones and convex feasible directions

The Bouligand tangent cone at \(x\in M\subset\mathbb R^n\) records limits of positively rescaled feasible displacements:
\[
T(M,x)=\{d:\exists x_k\in M,\ x_k\to x,\ \eta_k>0,
\ \eta_k(x_k-x)\to d\}.
\]
For nonempty convex \(M\),
\[
T(M,x)=\overline{\{\eta(y-x):\eta>0,\ y\in M\}}.
\]
The closure matters: a limiting feasible direction need not itself be a positive multiple of a single feasible displacement.

Every tangent direction belongs to the displayed closure directly from its defining sequence. Conversely, for \(d=\eta(y-x)\), convexity gives \(x_k=x+(y-x)/k\in M\), and \((k\eta)(x_k-x)=d\). For a limit \(d_k=\eta_k(y_k-x)\to d\), choose
\[
\alpha_k=k(\|y_k\|+1),\quad
x_k=x+(y_k-x)/\alpha_k,\quad
\widetilde\eta_k=\alpha_k\eta_k.
\]
Then \(x_k\in M\), \(x_k\to x\), and \(\widetilde\eta_k(x_k-x)=d_k\to d\). This proves the reverse inclusion without assuming closedness of the original displacement cone.

The representation describes the local first-order geometry through the globally available convex segments. It does not extend unchanged to a general nonconvex feasible set or replace a constraint qualification for nonlinear inequality descriptions.

## General properties

The tangent cone always contains zero and is a cone: take the constant feasible sequence, or multiply the positive rescaling factors by a positive scalar. It is closed. For \(d_k\to d\) with \(d_k\in T(M,x)\), select one realizing displacement for each \(d_k\), with both the position error and the rescaled-direction error at most \(1/k\); the selected sequence realizes \(d\). At an interior point every direction is realizable by sufficiently short segments, so \(T(M,x)=\mathbb R^n\).

For convex \(M\), the tangent cone is also convex. For directions \(d_i=\eta_i(y_i-x)\), combine the two rescaling factors: \(\lambda d_1+(1-\lambda)d_2=\widetilde\eta(\widetilde y-x)\), where \(\widetilde\eta=\lambda\eta_1+(1-\lambda)\eta_2>0\) and \(\widetilde y\) is the correspondingly weighted convex combination of \(y_1,y_2\). Closure preserves convexity. For nonconvex sets, tangent cones need not be convex.

## Source references

Archive: `00_sources/raw/tum/archives/NLOA (W24_25)_20261012_1553.zip`.
- `Exercise materials/Exercise Sheet 1.pdf`, T.1.2, p. 1.
- `Exercise materials/Solution Exercise Sheet 1.pdf`, Solution 1.2, p. 3; the closure in the displayed characterization is part of the original formula.
- `Exercise materials/Exercise Sheet 2.pdf`, T.2.4, p. 2; `Exercise materials/Solution Exercise Sheet 2.pdf`, Solution 2.4, p. 6.
- `Exercise materials/Exercise Sheet 3.pdf`, H.3.3, p. 1; `Exercise materials/Solution Exercise Sheet 3.pdf`, Solution 3.3, pp. 2–3.
