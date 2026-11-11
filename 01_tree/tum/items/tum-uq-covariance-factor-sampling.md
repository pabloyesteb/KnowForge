---
id: tum-uq-covariance-factor-sampling
source: tum-numuq
parent: uq-discretization
title: Gaussian field sampling by covariance factorization
type: algorithm
caption: Compares exact Cholesky and spectral sampling with low-rank covariance approximations.
---

# Gaussian field sampling by covariance factorization

At points \(x_1,\ldots,x_n\), a Gaussian field has sampled law \(N(\mu,C)\), where \(\mu_i=\mu(x_i)\) and \(C_{ij}=c(x_i,x_j)\). If \(C=VV^T\), \(V\in\mathbb R^{n\times m}\), draw \(\xi\sim N(0,I_m)\) and return \(\mu+V\xi\). Its Gaussianity follows from affine transformation; its mean and covariance are exactly \(\mu\) and \(VV^T\).

For positive definite \(C\), Cholesky gives a triangular \(V=L\). Spectral decomposition \(C=U\Lambda U^T\) gives \(V=U\Lambda^{1/2}\) for any positive semidefinite covariance, including singular ones. Standard dense factorizations cost \(O(n^3)\), followed by \(O(n^2)\) per sample. Retaining only the largest \(m\) nonnegative eigenvalues gives \(V=U_m\Lambda_m^{1/2}\), an approximate covariance \(C_m\) and \(O(nm)\) sampling cost. It is exact only when the discarded eigenvalues vanish. The notes quote \(O(n^3)\) preparation for a full decomposition; the handwritten lecture annotation also distinguishes reduced eigensolver costs rather than asserting a universal cost for every partial solver.

This method needs Gaussianity to reproduce the full sampled law: factoring a non-Gaussian field's covariance reproduces second moments but does not specify its distribution. Dense preparation is expensive for finite-element grids with \(n\asymp h^{-d}\).

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, §4 overview and §4.1, Lemma 4.1 and all three decompositions, pp. 25–26.
- `Lecture Topics and Slides/Lecture 06 (07.05.24)`, physical pp. 3–10, including handwritten factorization and reduced-cost annotations.
- `Lecture Topics and Slides/Lecture 07 (14.05.24)`, physical p. 3, handwritten sampling recap.
