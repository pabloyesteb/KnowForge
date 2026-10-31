---
id: tum-nloa-mfcq-slater
source: tum-nonlinear-optimization
parent: nloa-cq-kkt
title: MFCQ strict feasible directions and Slater points
type: concept
---

# MFCQ strict feasible directions and Slater points

For \(C^1\) mixed constraints, the full-rank MFCQ conditions used in the multiplier argument are independence of the equality gradients and a direction \(d\) such that
\[
\nabla h(\bar x)^Td=0,\qquad
\nabla g_i(\bar x)^Td<0\quad(i\in A(\bar x)).
\]
For inequalities alone there is no equality-rank condition. The direction moves strictly toward all active inequality interiors to first order.

For componentwise convex \(g\) and affine \(h\), a Slater point \(y\) satisfies \(g(y)<0\), \(h(y)=0\). At any feasible \(x\), take \(d=y-x\). Convexity and affinity give
\[
\nabla g_i(x)^Td\le g_i(y)-g_i(x)<0\quad(i\in A(x)),
\qquad\nabla h(x)^Td=h(y)-h(x)=0.
\]
Thus Slater supplies the strict-direction part at every feasible point. It does not establish independence of redundant affine equality gradients; a full-rank formulation of MFCQ needs that separate condition.

Conversely the sheet's mixed-constraint qualification construction uses feasible points \(x_k=x+w_k+\phi(w_k)\) maintaining \(h(x_k)=0\) and satisfying all \(g_i(x_k)<0\) for sufficiently large \(k\). This supplies a Slater point when its stated qualification hypotheses apply. The supplied solution refers to a construction in unprovided lecture notes rather than defining \(\phi\) or proving that construction. Its term “generalized MFCQ” is therefore not used here to silently equate the strict-direction condition with equality-gradient independence.

## Source references

Archive: `00_sources/raw/tum/archives/NLOA (W24_25)_20261012_1553.zip`.
- `Exercise materials/Exercise Sheet 3.pdf`, T.3.4(b), T.3.5 and T.3.6, p. 2.
- `Exercise materials/Solution Exercise Sheet 3.pdf`, Solution 3.4(b), p. 4; Solution 3.5, pp. 4–5; Solution 3.6(c), pp. 5–6, for the equality-rank assumption in the multiplier proof. Lecture Theorem 2.21 and Definition 2.22 are referenced but not supplied.
