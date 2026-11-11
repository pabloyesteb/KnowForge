---
id: tum-uq-multilevel-blue
source: tum-numuq
parent: uq-multilevel
title: Multilevel BLUE as generalized least squares
type: theorem
caption: Finds minimum-variance unbiased linear weights for fixed groups of correlated model observations.
---

# Multilevel BLUE as generalized least squares

Partition model evaluations into groups \(S^k\), drawing \(m_k\) common inputs per group and independent input sets between groups. For model means \(\mu\in\mathbb R^L\), stack observations as \(Y=H\mu+\epsilon\), with block noise covariance determined by within-group model covariances \(C^k=C_{S^k,S^k}\). Linear estimators combine group sample means; unbiasedness for \(\mu_L\) requires \(\sum_{k:\ell\in S^k}\beta_\ell^k=\delta_{\ell L}\).

Let \(R^k\) restrict model coordinates to group \(k\), \(P^k=(R^k)^T\), and
\[
\Psi=\sum_km_kP^k(C^k)^{-1}R^k=H^T\widetilde C^{-1}H,\qquad
y=\sum_kP^k(C^k)^{-1}\sum_{i=1}^{m_k}Z^k(\omega_i^k).
\]
When the model covariance is positive definite and every model is observed at least once, the design has full column rank, \(\Psi\) is invertible, and Gauss–Markov–Aitken gives
\[
\widehat\mu_L^{\rm BL}=e_L^T\Psi^{-1}y,\qquad\operatorname{Var}\widehat\mu_L^{\rm BL}=e_L^T\Psi^{-1}e_L.
\]
Solve the small \(L\times L\) normal equations \(\Psi\widehat\mu=y\); this is generalized least squares in the inverse noise-covariance norm. It is the unique best linear unbiased estimator for the specified observation design. Gaussian noise is not required for this linear-unbiased variance property.

The two-model example uses two coupled fine/coarse draws and one independent coarse draw, producing five correlated scalar observations. Treating their covariance explicitly permits optimizing weights beyond fixed MLMC differences. Fixed-design optimality does not choose group sample counts or prove optimality over biased/nonlinear estimators; it preserves the same discretized target mean.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Slides on Multilevel BLUE (27.06.24)`, physical pp. 4–16 (printed 3–15), motivation, observation design, full BLUE formula and Theorem 1.
- `Lecture Topics and Slides/Lecture 15 (27.06.24)`, same physical pages with handwritten common-input grouping, design and normal-equation annotations.
