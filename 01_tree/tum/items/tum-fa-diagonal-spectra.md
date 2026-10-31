---
id: tum-fa-diagonal-spectra
source: tum-functional-analysis
parent: fa-spectral-theory
title: Diagonal multiplication, eigenvalues and spectral limit points
type: method
---

# Diagonal multiplication, eigenvalues and spectral limit points

For bounded coefficients \(a\), \((D_ax)_n=a_nx_n\) defines a bounded map on \(\ell^2\) or \(\ell^\infty\), with norm \(\sup_n|a_n|\). Its eigenvalues are exactly the attained coefficients \(\{a_n\}\). At \(\lambda\), eigenvectors are the nonzero sequences supported on \(\{n:a_n=\lambda\}\), belonging to the ambient sequence space. In \(\ell^2\), this is the closed span of the corresponding coordinate vectors; multiplicity is the size of that index set, possibly infinite. Self-adjointness in complex \(\ell^2\) is equivalent to all coefficients being real.

The full spectrum is
\[
\sigma(D_a)=\overline{\{a_n:n\ge1\}}.
\]
Outside this closure, \(\inf_n|\lambda-a_n|>0\), and
\[
((\lambda I-D_a)^{-1}y)_n=\frac{y_n}{\lambda-a_n}
\]
is bounded. If \(\lambda\) lies in the closure but is not attained, \(\lambda I-D_a\) is injective, yet its inverse on its range is unbounded: choose coordinate vectors with \(|\lambda-a_{n_k}|\to0\). It cannot be surjective by bounded inverse. Spectral points therefore need not be eigenvalues.

For truncation \(a^{(N)}=(a_1,\ldots,a_N,0,\ldots)\),
\[
\|D_a-D_{a^{(N)}}\|=\sup_{n>N}|a_n|.
\]
Thus finite-rank truncations converge in operator norm exactly when \(a\in c_0\). On \(\ell^2\), this is also exactly the compactness condition; a merely bounded sequence of coefficients does not ensure convergence of this approximation.

## Source references

Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`.
- `Problem sheets/Problem Sheet 12.pdf` and `Solutions to problem sheets/Solutions Sheet 12.pdf` (WS 2024/25), T12.2 and A12.1 (the latter treats \(\ell^\infty\)).
- `Problem sheets/Problem Sheet 10.pdf` and `Solutions to problem sheets/Solutions Sheet 10.pdf`, T10.1(a), for compactness on finite-exponent sequence spaces.
