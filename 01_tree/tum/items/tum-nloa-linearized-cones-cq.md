---
id: tum-nloa-linearized-cones-cq
source: tum-nonlinear-optimization
parent: nloa-cq-kkt
title: Linearized feasible cones, Abadie and Guignard qualifications
type: concept
caption: "Compares true and affine-model tangent cones and uses degenerate planar constraints to distinguish Abadie from Guignard qualification."
---

# Linearized feasible cones, Abadie and Guignard qualifications

## True geometry and its linearized model

For differentiable constraints \(X=\{x:g(x)\le0,\ h(x)=0\}\) and feasible \(\bar x\), let \(A(\bar x)=\{i:g_i(\bar x)=0\}\). The linearized cone is
\[
T_l(g,h,\bar x)=\{d:\nabla g_i(\bar x)^Td\le0\ (i\in A),\ \nabla h(\bar x)^Td=0\}.
\]
Always \(T(X,\bar x)\subset T_l\), by differentiating constraints along feasible sequences. The linearized cone equals the true tangent cone of the affine first-order constraint model \(g^l(x)=g(\bar x)+\nabla g(\bar x)^T(x-\bar x)\), and similarly for \(h^l\). For the reverse inclusion, \(\bar x+d/k\) satisfies the affine active/equality constraints; finitely many inactive inequalities remain negative for large \(k\).

For a cone \(C\), define \(C^\circ=\{v:v^Td\le0\ \forall d\in C\}\). Abadie's CQ (ACQ) is \(T=T_l\); Guignard's CQ (GCQ) is \(T^\circ=T_l^\circ\). Thus ACQ implies GCQ, while equality of polars need not recover a nonconvex tangent set.

## Three diagnostic constraint descriptions at the origin

| Constraints \(g\le0\) | True tangent \(T\) | Linearized cone \(T_l\) | Qualification |
|---|---|---|---|
| \(g=(-x_1,x_2^2)\) | \(\mathbb R_+\times\{0\}\) | \(\mathbb R_+\times\mathbb R\) | Both fail |
| \(g=(x_2-x_1^3,-x_2)\) | \(\mathbb R_+\times\{0\}\) | \(\mathbb R\times\{0\}\) | Both fail |
| \(g=(-x_1,-x_2,x_1x_2)\) | Nonnegative coordinate axes | \(\mathbb R_+^2\) | GCQ holds; ACQ fails |

In the first case, \(T^\circ=\mathbb R_-\times\mathbb R\), but \(T_l^\circ=\mathbb R_-\times\{0\}\). The zero gradient of \(x_2^2\) loses its exact geometric restriction. In the second case, the cubic feasible cusp has only nonnegative horizontal tangent directions, whereas linearization permits both signs; the polars are respectively \(\mathbb R_-\times\mathbb R\) and \(\{0\}\times\mathbb R\).

In the third case, feasibility forces one coordinate to vanish, so the true tangent is the union of two rays. Both its polar and the quadrant's polar are \(\mathbb R_-^2\). First-order inequalities against directions can therefore coincide even though the tangent sets differ. CQs depend on the constraint description as well as the underlying feasible set.

## Source references

Archive: `00_sources/raw/tum/archives/NLOA (W24_25)_20261012_1553.zip`.
- `Exercise materials/Exercise Sheet 2.pdf`, H.2.2–H.2.3, p. 1, and T.2.5, p. 2.
- `Exercise materials/Solution Exercise Sheet 2.pdf`, Solutions 2.2–2.3, pp. 2–5 (including feasible-set plots); Solution 2.5, pp. 6–7.
