---
id: tum-fa-shift-spectra
source: tum-functional-analysis
parent: fa-spectral-theory
title: Shift operators and dependence of spectral type on the ambient space
type: method
---

# Shift operators and dependence of spectral type on the ambient space

## Right shift on complex square-summable sequences

Let \(S(x_0,x_1,\ldots)=(0,x_0,x_1,\ldots)\) on \(\ell^2(\mathbb C)\). It is an isometry, with adjoint the left shift \(L\). There are no eigenvalues: the eigen-equation and zero first output force zero for \(\lambda\ne0\), while \(\lambda=0\) also has trivial kernel.

For \(|\lambda|<1\), \(y=(1,\overline\lambda,\overline\lambda^2,\ldots)\in\ell^2\) satisfies \(L y=\overline\lambda y\), so it annihilates the range of \(\lambda I-S\) under the Hilbert pairing. That injective map has nondense range; the open unit disk belongs to the residual spectrum. Closedness of the spectrum and \(\|S\|=1\) then give
\[
\sigma(S)=\{\lambda:|\lambda|\le1\}.
\]
Complex conjugation in the annihilating vector is essential under the inner-product convention linear in the first argument.

## Left shift: the same rule on different spaces

For \(L(x_0,x_1,\ldots)=(x_1,x_2,\ldots)\), an eigenvector must be \(c(1,\lambda,\lambda^2,\ldots)\).

On \(\ell^2\), it belongs to the space iff \(|\lambda|<1\). Every \(\lambda I-L\) has dense range: solve the finite-support output equations backward to obtain a finite-support preimage (for \(\lambda=0\), shift right with a minus sign). Since the full spectrum is the closed unit disk,
\[
\sigma_p(L)=\{|\lambda|<1\},\quad
\sigma_c(L)=\{|\lambda|=1\},\quad\sigma_r(L)=\varnothing.
\]
On \(\ell^\infty\), the same geometric vector is admissible for \(|\lambda|\le1\). Hence the entire closed unit disk is point spectrum; continuous and residual spectra are empty. The algebraic formula of an operator does not determine its spectral classification independently of the domain's summability requirement.

## Source references

Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`.
- `Problem sheets/Problem Sheet 13.pdf` and `Solutions to problem sheets/Solutions Sheet 13.pdf` (WS 2024/25), T13.2 and A13.1.
- `Problem sheets/Problem Sheet 11.pdf` and `Solutions to problem sheets/Solutions sheet 11.pdf`, A11.1(b), for the adjoint and projection identities.
