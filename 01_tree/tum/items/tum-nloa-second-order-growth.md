---
id: tum-nloa-second-order-growth
source: tum-nonlinear-optimization
parent: nloa-second-order-penalty
title: Lagrangian curvature on critical directions and local quadratic growth
type: theorem
caption: "Uses positive Lagrangian curvature on critical directions to prove local quadratic growth, including an example with a zero active gradient."
---

# Lagrangian curvature on critical directions and local quadratic growth

## Positive-multiplier cone and sufficiency

For \(C^2\) data and KKT triple \((\bar x,\bar\lambda,\bar\mu)\), set \(A_+=\{i\in A:\bar\lambda_i>0\}\). The cone used for second-order sufficiency is
\[
T_+=\{d:\nabla h(\bar x)^Td=0,\quad
\nabla g_i(\bar x)^Td=0\ (i\in A_+),\quad
\nabla g_i(\bar x)^Td\le0\ (i\in A\setminus A_+)\}.
\]
If \(d^T\nabla_{xx}^2L(\bar x,\bar\lambda,\bar\mu)d>0\) for every nonzero \(d\in T_+\), then there are \(\alpha,\delta>0\) with
\[
f(x)-f(\bar x)\ge\alpha\|x-\bar x\|^2
\quad(x\text{ feasible},\ \|x-\bar x\|<\delta).
\]
In particular the minimizer is strict locally. The curvature condition is sufficient; it need not hold for every possible multiplier at every constrained minimum.

## Contradiction proof

Failure of quadratic growth gives feasible \(x_k\ne\bar x\), \(x_k\to\bar x\), and \(\alpha_k\downarrow0\) with objective increase less than \(\alpha_k\|x_k-\bar x\|^2\). Normalize displacements and extract unit \(y_k\to y\). Feasibility gives \(y\in T_l\), while first-order expansion bounds \(\nabla f(\bar x)^Ty\le0\). KKT makes that derivative nonnegative, and positive active multipliers force their directional constraint derivatives to zero. Thus \(y\in T_+\setminus\{0\}\).

Feasibility and multiplier signs give \(L(x_k,\bar\lambda,\bar\mu)\le f(x_k)\), with equality at \(\bar x\). Since \(\nabla_xL(\bar x,\bar\lambda,\bar\mu)=0\), the second-order expansion divided by \(\|x_k-\bar x\|^2\) yields
\(\tfrac12 y^T\nabla_{xx}^2L\,y\le0\), a contradiction.

## Degenerate active gradient with valid sufficiency

For \(f=x_1+x_2-2x_3\), \(g_1=x_1^2/2-x_2\), \(g_2=e^{x_1-1}-x_1\), \(h=x_3^2-x_1+3/4\), the point \(\bar x=(1,1/2,1/2)\) and multipliers \(\bar\lambda=(1,0)\), \(\bar\mu=2\) satisfy KKT. Although \(\nabla g_2(\bar x)=0\),
\[
T_+=\{(t,t,t):t\in\mathbb R\},\qquad
\nabla_{xx}^2L=\operatorname{diag}(1,0,4).
\]
Its quadratic form is \(5t^2>0\) for nonzero such directions, proving strict local optimality and quadratic growth. A zero active gradient does not by itself invalidate a sufficient curvature test.

## Source references

Archive: `00_sources/raw/tum/archives/NLOA (W24_25)_20261012_1553.zip`; `Exercise materials/Exercise Sheet 4.pdf`, H.4.2, p. 1, T.4.3, p. 2; `Exercise materials/Solution Exercise Sheet 4.pdf`, Solutions 4.2–4.3, pp. 2–3. The solution supplies the growth proof and explicit cone calculation although the referenced lecture Theorem 2.33 is not included.
