---
id: tum-nloa-slack-licq
source: tum-nonlinear-optimization
parent: nloa-cq-kkt
title: Preserving LICQ when introducing nonnegative slack variables
type: theorem
---

# Preserving LICQ when introducing nonnegative slack variables

For inequality constraints \(g(x)\le0\), introduce \(s\in\mathbb R^m\):
\[
g(x)+s=0,\qquad-s\le0.
\]
At feasible \(\bar x\), set \(\bar s=-g(\bar x)\). The transformed point is feasible and the active slack bounds are exactly the original active inequalities.

If the original active gradients are independent (LICQ), the transformed active inequalities and all equality gradients are independent. The equality-gradient columns are \((\nabla g_i(\bar x),e_i)^T\); active bound-gradient columns are \((0,-e_j)^T\), \(j\in A\). In any zero linear combination, the inactive slack coordinates force the corresponding equality coefficients \(w_i=0\). The \(x\)-coordinates then give \(\sum_{i\in A}w_i\nabla g_i=0\), so original LICQ forces all remaining \(w_i=0\). The active slack coordinates finally force the bound coefficients to vanish.

Thus this reformulation preserves qualification at the corresponding point, not just feasibility. The statement concerns ordinary nonnegative slacks; it does not establish an analogous result for squared-slack transformations.

## Source references

Archive: `00_sources/raw/tum/archives/NLOA (W24_25)_20261012_1553.zip`; `Exercise materials/Exercise Sheet 4.pdf`, T.4.4, p. 2, and `Exercise materials/Solution Exercise Sheet 4.pdf`, Solution 4.4, p. 4.
