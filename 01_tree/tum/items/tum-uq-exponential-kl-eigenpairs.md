---
id: tum-uq-exponential-kl-eigenpairs
source: tum-numuq
parent: uq-discretization
title: Exponential covariance eigenpairs from a Robin boundary problem
type: method
caption: Transforms a covariance integral eigenproblem into trigonometric root equations and an algebraic KL tail rate.
---

# Exponential covariance eigenpairs from a Robin boundary problem

For \(c(x,y)=e^{-|x-y|/\ell}\) on \((-a,a)\), write \(\lambda=1/\ell\) and split the eigen-equation \(\int_{-a}^ae^{-\lambda|x-y|}\phi(y)dy=\nu\phi(x)\) at \(y=x\). Differentiating twice with Leibniz's rule gives
\[
\phi''+w^2\phi=0,\quad w^2=2\lambda/\nu-\lambda^2,\qquad
\phi'(-a)=\lambda\phi(-a),\quad\phi'(a)=-\lambda\phi(a).
\]
The boundary system separates into even cosine modes with \(w\tan(wa)=\lambda\) and odd sine modes with \(\lambda\tan(wa)=-w\). Normalize the trigonometric eigenfunctions in spatial \(L^2\); their eigenvalues are
\[
\nu=\frac{2\lambda}{w^2+\lambda^2}=\frac{2\ell}{1+\ell^2w^2}.
\]
Parity is determined by these root equations. The appendix's assignments of odd/even index to the roots and its subsequent sine/cosine display conflict; the paired root-and-parity description avoids that indexing error.

The interlacing roots satisfy \(w_j\sim j\pi/(2a)\), giving \(\nu_j\sim8a^2/(\pi^2\ell j^2)\). Consequently the squared KL truncation error is \(O(J^{-1})\), and its root-mean-square norm is \(O(J^{-1/2})\). The displayed constant derived from an asymptotic equivalence should not be interpreted as a proved finite-\(J\) upper bound without an eigenvalue inequality. Product kernels on rectangular domains can be handled by tensor products: multiply one-dimensional eigenfunctions and eigenvalues, including the variance prefactor once.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, appendix B, pp. 98–100 (ending before appendix C), complete split-integral, ODE and boundary derivation; Remark 4.29, p. 39.
- `Lecture Topics and Slides/Lecture 08 (16.05.24)`, physical pp. 17–20, handwritten two-dimensional product-kernel eigenpair derivation.
