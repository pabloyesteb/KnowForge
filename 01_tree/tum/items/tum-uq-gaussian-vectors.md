---
id: tum-uq-gaussian-vectors
source: tum-numuq
parent: uq-probability
title: Gaussian vectors, affine transformations and independent components
type: theorem
caption: "Characterizes Gaussian laws by mean and covariance while treating singular distributions and joint Gaussianity explicitly."
---

# Gaussian vectors, affine transformations and independent components

For vector-valued variables, \(\operatorname{Cov}(X,Y)=E[(X-E[X])(Y-E[Y])^T]\), whose \((i,j)\) entry is \(\operatorname{Cov}(X_i,Y_j)\); the source's \(X_j\) entry is a typo for cross-covariance. The covariance of \(X\) itself is symmetric positive semidefinite.

For positive definite \(C\), the law \(N(\mu,C)\) has density
\[
(2\pi)^{-d/2}(\det C)^{-1/2}\exp[-\tfrac12(x-\mu)^TC^{-1}(x-\mu)].
\]
For positive semidefinite \(C\), possibly singular, use the characteristic function \(\phi_X(\lambda)=\exp(i\lambda^T\mu-\tfrac12\lambda^TC\lambda)\). It determines the law by mean and covariance without requiring an ambient Lebesgue density. Equivalently every linear combination \(a^TX\) is univariate Gaussian, including degenerate constants; the notes state equivalence of all three descriptions when \(C\) is nonsingular.

For deterministic \(A,b\), the transformed characteristic function proves \(AX+b\sim N(A\mu+b,ACA^T)\). Multiplying characteristic functions also shows that independent scalar Gaussians add with means and variances added. Within a jointly Gaussian vector, diagonal covariance makes components mutually independent: the density factorizes when nonsingular; zero-variance components are almost-sure constants and can be removed before applying the same argument to the remaining subvector. Gaussian marginals alone do not imply joint Gaussianity or this independence criterion.

Gaussian scalar laws are closed under \(L^2\) convergence. If \(X_n\to X\) in \(L^2\), then means and second moments, hence variances, converge; characteristic functions converge since \(|e^{itX_n}-e^{itX}|\le |t||X_n-X|\). Passing to the limit in the Gaussian characteristic function proves that \(X\) is Gaussian, possibly degenerate.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, §2.5, Definitions 2.56–2.58 and 2.63, Lemmas 2.60–2.62, Theorem 2.64, pp. 13–15, complete affine/sum and diagonal-covariance proofs.
- `Lecture Topics and Slides/Lecture 03 (23.04.24)`, physical pp. 22–27 (printed 36–41), first Gaussian presentation and references.
- `Lecture Topics and Slides/Lecture 04 (25.04.24)`, physical pp. 1–7 (printed 36–42), repeated Gaussian definitions, equivalence and references.
- `Problem Sheets/Problem Sheet 01 (25.04.2024)`, Problem 2; `Problem Sheets/Solution Sheet 01 (update  complete).pdf`, p. 2, Gaussian closure proof.
- `Oral exam/Topics and sample questions (08.07.24)`, §2, pp. 1–2, three Gaussian-vector definitions and their equivalence conditions.
