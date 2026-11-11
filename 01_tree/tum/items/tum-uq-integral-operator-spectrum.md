---
id: tum-uq-integral-operator-spectrum
source: tum-numuq
parent: uq-discretization
title: Compact symmetric integral operators and spectral expansions
type: theorem
caption: Supplies the operator framework for diagonalizing covariance kernels in spatial L2.
---

# Compact symmetric integral operators and spectral expansions

A kernel \(G\in L^2(D\times D)\) defines a Hilbert–Schmidt, hence compact, operator \((Lu)(x)=\int_DG(x,y)u(y)dy\) on \(L^2(D)\). Compactness means that images of bounded sets have compact closure. If \(G(x,y)=G(y,x)\), Fubini gives \((Lu,v)=(u,Lv)\): absolute integrability of the product follows by Cauchy–Schwarz on \(D\times D\).

On a separable real Hilbert space, a compact self-adjoint operator has real nonzero eigenvalues, accumulating only at zero, and orthonormal corresponding eigenvectors. They span the **closure** of its range, not necessarily its nonclosed range as the notes phrase it. Adding a basis of the kernel gives a full Hilbert basis, and
\[
Lu=\sum_j\lambda_j(u,\phi_j)\phi_j.
\]
For continuous positive semidefinite kernels under the bounded-domain integrability assumptions, \((u,Lu)\ge0\): approximate the kernel by cellwise sampled kernels and turn each double integral into \(\sum_{j,k}a_jG(x_j,x_k)a_k\ge0\), then pass to the limit with the required integral control. Covariance operators are therefore positive and their eigenvalues nonnegative. Pointwise convergence of kernels alone is insufficient to justify interchange with integration; the course's continuous bounded-kernel setting supplies a dominating bound.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, §4.3.2, Definitions 4.15–4.20, Theorems 4.17 and 4.21 and Lemmas 4.19 and 4.22, pp. 32–34.
- `Lecture Topics and Slides/Lecture 07 (14.05.24)`, physical pp. 14–17 (printed 20–23); `Lecture Topics and Slides/Lecture 08 (16.05.24)`, physical p. 1 (printed 24).
