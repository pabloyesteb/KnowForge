---
id: tum-fda-covariance-affine-maps
source: tum-foundations-data-analysis
parent: fda-probability
title: Covariance matrices and affine transformations of random vectors
type: theorem
caption: "Propagates mean and covariance through deterministic affine maps and specializes linear functionals to Gaussian laws."
---

# Covariance matrices and affine transformations of random vectors

For a real random vector \(X\) with finite second moments, define \(\mu=\mathbb EX\) and
\[
\Sigma=\operatorname{Cov}(X)=\mathbb E[(X-\mu)(X-\mu)^T].
\]
Its diagonal entries are component variances and its off-diagonal entries are covariances. The matrix is symmetric and positive semidefinite, since
\[
v^T\Sigma v=\operatorname{Var}(v^TX)\ge0.
\]
Marginal variances alone omit the dependence information carried by the off-diagonal terms.

For deterministic \(A,b\), linearity and centering give
\[
\mathbb E(AX+b)=A\mu+b,\qquad
\operatorname{Cov}(AX+b)=A\Sigma A^T.
\]
In particular \(\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)\) in one dimension, and \(\operatorname{Var}(X+Y)=\operatorname{Var}X+\operatorname{Var}Y+2\operatorname{Cov}(X,Y)\). Translation does not affect dispersion; independence is unnecessary for mean propagation but removes covariance cross terms in sums.

If \(\Sigma\) is singular, every \(v\in\ker\Sigma\) satisfies \(v^T(X-\mu)=0\) almost surely. Thus the distribution is concentrated on the lower-dimensional affine space \(\mu+\operatorname{range}\Sigma\), rather than necessarily a linear subspace through the origin.

For a jointly Gaussian vector, \(v^TX\sim N(v^T\mu,v^T\Sigma v)\). Independent Gaussian components give diagonal covariance; general Gaussian marginals have variances \(\Sigma_{ii}\). The review's example has \(\mu=(1,0,2)^T\) and covariance rows \((2,0,1)\), \((0,3,1)\), \((1,1,4)\), yielding \(X_3\sim N(2,4)\) and \(2X_1-X_3\sim N(0,8)\). The latter variance follows by evaluating \((2,0,-1)\Sigma(2,0,-1)^T\); the handwritten value 5 is inconsistent with the displayed matrix.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `24. Juni - 30. Juni/All you... math 10`, single physical page, “Arithmetic of Mean and Variance”, scalar/vector affine maps, covariance matrix, projected variance and singular covariance discussion.
- `1. Juli - 7. Juli/All you... math 11`, single physical page, opening “Tricks for Gaussians”, independent components, general linear functionals and the displayed three-dimensional example.
