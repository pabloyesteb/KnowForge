---
id: tum-nloa-sqp-models
source: tum-nonlinear-optimization
parent: nloa-sqp-barrier
title: SQP quadratic models, feasibility and exact quadratic special cases
type: algorithm
caption: "Builds quadratic Lagrangian models with affine constraints and analyzes infeasibility, exact convex-QP steps and an equality Newton example."
---

# SQP quadratic models, feasibility and exact quadratic special cases

## Local subproblem

At \((x_k,\lambda_k,\mu_k)\), exact-Hessian SQP uses
\[
\min_d\ \nabla f(x_k)^Td+\tfrac12d^TH_kd,\qquad
g(x_k)+\nabla g(x_k)^Td\le0,\quad
h(x_k)+\nabla h(x_k)^Td=0,
\]
with \(H_k=\nabla_{xx}^2L(x_k,\lambda_k,\mu_k)\); variants may supply a different \(H_k\). The model retains Lagrangian curvature while replacing constraints by affine models. A globalized update uses \(x_{k+1}=x_k+\sigma_kd_k\) and QP multipliers. The sheets analyze this structure, not a fully specified merit function or line-search implementation.

If the original feasible set is nonempty, each \(g_i\) convex and \(h\) affine, any feasible \(\widehat x\) gives subproblem-feasible \(d=\widehat x-x_k\), since
\(g(x_k)+\nabla g(x_k)^Td\le g(\widehat x)\le0\) and the affine equality is exact. This establishes feasibility, not boundedness below or existence of a minimizing QP direction.

Without these assumptions the subproblem can be infeasible even when the original problem is feasible:

- For \(g(x)=-x\), \(h(x)=x_1^2+x_2^2-1\), \(x_k=(-1/2,-1/2)\), linearization requires \(d_1,d_2\ge1/2\) and \(d_1+d_2=-1/2\), impossible.
- For scalar \(f=x^3\), \(g=1-x^4\), \(x_k=0\), \(H_k=1\), the constraint model is the impossible \(1\le0\), despite the positive quadratic model Hessian.

## Convex quadratic exactness

For \(q(x)=\tfrac12x^TQx+c^Tx\), \(Q\succeq0\), with \(Cx\le b_g\), \(Ax=b_h\), KKT is necessary and sufficient at an existing solution:
\[
Qx+c+C^T\lambda+A^T\mu=0,\quad
Cx\le b_g,\quad Ax=b_h,\quad\lambda\ge0,\quad
\lambda^T(Cx-b_g)=0.
\]
Affine constraint geometry supplies the qualification, without requiring LICQ. The exact-Hessian SQP model has Hessian \(Q\); its objective differs from \(q(x_k+d)\) only by \(q(x_k)\). Its constraints are those of the original QP at \(x_k+d\). Hence any global subproblem solution gives an original global solution in one **full** step. This does not assert that arbitrary damped steps terminate in one iteration.

## Equality-constrained Lagrange–Newton step

Newton's method for equality KKT equations solves the block system with Lagrangian Hessian and equality Jacobian. For \(f(x)=x^2\), \(h(x)=x\), at \((x_0,\mu_0)=(1,0)\),
\[
\begin{pmatrix}2&1\\1&0\end{pmatrix}
\begin{pmatrix}\delta x\\\delta\mu\end{pmatrix}
=\begin{pmatrix}-2\\-1\end{pmatrix}.
\]
It gives \(\delta x=-1\), \(\delta\mu=0\), reaching the KKT pair \((0,0)\) in one step. This scalar exact example is not a general one-step or convergence theorem.

## Source references

Archive: `00_sources/raw/tum/archives/NLOA (W24_25)_20261012_1553.zip`.
- `Exercise materials/Exercise Sheet 6.pdf`, H.6.2, p. 1, T.6.4, p. 2; `Exercise materials/Solution Exercise Sheet 6.pdf`, Solutions 6.2/6.4, pp. 1, 3–4.
- `Exercise materials/Exercise Sheet 7.pdf`, H.7.2(b–c), p. 1; `Exercise materials/Solution Exercise Sheet 7.pdf`, Solution 7.2(b–c), p. 3.
