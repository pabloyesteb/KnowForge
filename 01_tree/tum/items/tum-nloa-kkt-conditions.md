---
id: tum-nloa-kkt-conditions
source: tum-nonlinear-optimization
parent: nloa-cq-kkt
title: KKT conditions and first-order directional stationarity
type: concept
---

# KKT conditions and first-order directional stationarity

For \(\min f(x)\) subject to \(g(x)\le0\), \(h(x)=0\), define
\[
L(x,\lambda,\mu)=f(x)+\lambda^Tg(x)+\mu^Th(x).
\]
A KKT triple satisfies primal feasibility and
\[
\lambda\ge0,\quad \lambda_i g_i(x)=0,\quad
\nabla f(x)+\nabla g(x)\lambda+\nabla h(x)\mu=0.
\]
Inactive inequalities have zero multipliers. Strict complementarity at a triple means positive multipliers for every active inequality; it is stronger than complementary slackness.

KKT implies nonnegative directional derivative on the linearized cone, without an additional CQ for this implication. For \(d\in T_l(g,h,\bar x)\),
\[
\nabla f(\bar x)^Td
=-\sum_{i\in A}\lambda_i\nabla g_i(\bar x)^Td
-\mu^T\nabla h(\bar x)^Td\ge0.
\]
Since \(T(X,\bar x)\subset T_l\), it implies the first-order tangent-cone necessary condition. It does not by itself imply a local minimum for an arbitrary nonconvex problem. Conversely deriving KKT from a constrained minimum requires appropriate qualification hypotheses; existence of multipliers is not supplied merely by writing this system.

## Convex sufficiency and primal uniqueness

When \(f,g_i\) are convex and \(h\) affine, a KKT point is globally optimal: the convex Lagrangian in \(x\) is stationary there, so is globally minimized there, and feasibility with nonnegative multipliers compares it to \(f\) on the feasible set. If \(f\) is strictly convex, there cannot be two different KKT points: their feasible midpoint would have objective below their common minimum. Primal uniqueness does not by itself imply uniqueness of the multiplier tuple.

## Source references

Archive: `00_sources/raw/tum/archives/NLOA (W24_25)_20261012_1553.zip`.
- `Exercise materials/Exercise Sheet 3.pdf`, H.3.2(b–c), p. 1, and T.3.4(a), p. 2.
- `Exercise materials/Solution Exercise Sheet 3.pdf`, Solution 3.2(b–c), p. 2, and Solution 3.4(a), p. 4.
- `Exercise materials/Exercise Sheet 4.pdf`, H.4.1(a), p. 1; `Exercise materials/Solution Exercise Sheet 4.pdf`, Solution 4.1(a), p. 1.
