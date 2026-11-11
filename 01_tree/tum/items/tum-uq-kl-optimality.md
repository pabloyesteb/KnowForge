---
id: tum-uq-kl-optimality
source: tum-numuq
parent: uq-discretization
title: Optimal KL truncation and eigenvalue-tail error
type: theorem
caption: Minimizes mean-square spatial error among fixed-dimensional orthogonal projections and quantifies discarded variance.
---

# Optimal KL truncation and eigenvalue-tail error

Order the covariance eigenvalues \(\nu_1\ge\nu_2\ge\cdots\ge0\). The KL projection onto the first \(J\) modes satisfies
\[
E\|Z-Z_J\|_{L^2(D)}^2=\sum_{j>J}\nu_j.
\]
Orthogonality eliminates all spatial cross terms, and each normalized random coordinate contributes unit second moment. This is a squared mean-square error; its square root is the Bochner \(L^2\) error. It also equals the total variance omitted by the truncated covariance.

Among deterministic \(J\)-dimensional spatial subspaces and their orthogonal projections of the centered field, leading covariance eigenfunctions minimize this error. For an arbitrary orthonormal basis \((\psi_j)\), the error is the sum of \(E|(Z-\mu,\psi_j)|^2\) over omitted coordinates, equivalently integrals of \(c(x,y)\psi_j(x)\psi_j(y)\). The optimization selects the covariance eigen-equation and retains the largest eigenvalues. Repeated eigenvalues permit different optimal bases. The course refers the detailed optimality proof to its cited reference; the elementary tail identity is derived in full.

Scaling covariance by \(\sigma^2\) scales all eigenvalues and squared errors by that factor. Short correlation lengths produce a broad plateau in the leading spectrum, approximately \(1/\ell\) modes in the illustrated one-dimensional cases, so many modes may be needed before the omitted variance becomes small. This is a parameter-study observation, not a universal sharp estimate for every kernel. The notes' Figure 4 is captioned exponential covariance, while L09's handwritten annotation changes that plot to Gaussian; the eigenvalue-tail identity does not depend on resolving that label discrepancy.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, §§4.3.4–4.3.5, pp. 40–42, Figures 3–4 and full truncation-error derivation.
- `Lecture Topics and Slides/Lecture 08 (16.05.24)`, physical p. 21, approximation-error distinction; `Lecture Topics and Slides/Lecture 09 (28.05.24)`, physical pp. 1–3 (printed 32–34), tail identity, spectral plots and handwritten covariance correction.
