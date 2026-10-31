---
id: tum-nloa-quadratic-penalty-iteration
source: tum-nonlinear-optimization
parent: nloa-second-order-penalty
title: Stationary quadratic-penalty subproblems and limiting KKT multipliers
type: algorithm
caption: "Derives scaled-residual multiplier estimates and a limiting KKT pair under primal convergence, diverging penalties and equality LICQ."
---

# Stationary quadratic-penalty subproblems and limiting KKT multipliers

For \(C^1\) equality-constrained \(\min f(x)\), \(h(x)=0\), let
\(P_\alpha(x)=f(x)+(\alpha/2)\|h(x)\|^2\). The modified penalty scheme is:

1. Choose \(\alpha_0>0\).
2. Compute a stationary point \(x_k\) satisfying \(\nabla P_{\alpha_k}(x_k)=0\).
3. Stop if \(h(x_k)=0\); otherwise choose \(\alpha_{k+1}>\alpha_k\) and repeat.

The subproblem requirement is stationarity, not a specified minimization routine or a guarantee of global minimizers.

## Conditional limit analysis

Assume \(\alpha_k\to\infty\), \(x_k\to\bar x\), and \(\nabla h(\bar x)\) has full column rank (the equality LICQ condition). Set \(\mu_k=\alpha_kh(x_k)\). Stationarity reads
\[
\nabla f(x_k)+\nabla h(x_k)\mu_k=0.
\]
Continuity preserves full column rank near \(\bar x\), so for large \(k\),
\[
\mu_k=-[\nabla h(x_k)^T\nabla h(x_k)]^{-1}
\nabla h(x_k)^T\nabla f(x_k).
\]
The normal-equation formula and continuity of matrix inversion give convergence to the same expression evaluated at \(\bar x\), denoted \(\bar\mu\). Consequently
\[
h(\bar x)=\lim_k\frac{\mu_k}{\alpha_k}=0,\qquad
\nabla f(\bar x)+\nabla h(\bar x)\bar\mu=0.
\]
Thus the limiting pair is KKT. The argument proves feasibility from scaled-residual control; it does not assume feasibility of every iterate. It assumes convergence of the primal sequence and unbounded penalty growth rather than proving either for every run. No convergence rate or numerical experiment is provided.

## Source references

Archive: `00_sources/raw/tum/archives/NLOA (W24_25)_20261012_1553.zip`; `Exercise materials/Exercise Sheet 5.pdf`, T.5.5(a–d), p. 2; `Exercise materials/Solution Exercise Sheet 5.pdf`, Solution 5.5, pp. 5–6.
