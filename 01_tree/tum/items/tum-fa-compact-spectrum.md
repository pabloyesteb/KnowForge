---
id: tum-fa-compact-spectrum
source: tum-functional-analysis
parent: fa-spectral-theory
title: Compact-operator spectra and spectral effects of compact perturbations
type: theorem
---

# Compact-operator spectra and spectral effects of compact perturbations

## Nonzero spectral points

For compact \(S\) on a Banach space, every nonzero spectral value \(\lambda\) is an eigenvalue with finite-dimensional eigenspace. Indeed,
\(\lambda I-S=\lambda(I-\lambda^{-1}S)\) is Fredholm of index zero. If injective it is surjective, hence invertible. Its kernel is finite-dimensional by the Fredholm property.

For every \(\varepsilon>0\), there are only finitely many spectral values with \(|\lambda|\ge\varepsilon\); consequently there are at most countably many nonzero spectral values, with zero the only possible accumulation point. If infinitely many distinct eigenvalues stayed away from zero, their eigenvectors would generate strictly increasing finite-dimensional invariant spaces \(X_n\). Riesz's lemma selects unit \(y_n\in X_n\) at distance at least \(1/2\) from \(X_{n-1}\). The relation \(\lambda_ny_n-Sy_n\in X_{n-1}\) then makes the \(Sy_n\) separated by at least \(\varepsilon/2\), contradicting compactness.

On infinite-dimensional \(X\), zero is always spectral: otherwise \(I=S^{-1}S\) would be compact. It need not be an eigenvalue, as Volterra integration illustrates.

For a square-integrable-kernel integral map \(S\), the second-kind equation
\[
\lambda x(t)-\int_0^1k(s,t)x(s)\,ds=y(t),\qquad\lambda\ne0,
\]
is uniquely solvable for every \(y\in L^2\) exactly when \(\lambda\) is not an eigenvalue. Otherwise homogeneous solutions form a finite-dimensional space and adjoint compatibility conditions control inhomogeneous solvability.

## Comparing compactly perturbed operators

If \(S-T\) is compact, then
\[
\sigma(S)\setminus M=\sigma(T)\setminus M,
\qquad M=\sigma_p(S)\cup\sigma_p(T).
\]
For the key step, if \(T\) were invertible, then \(S=T[I+T^{-1}(S-T)]\). The bracket is identity plus compact, so is either invertible or has a nonzero kernel. Thus a spectral non-eigenvalue of \(S\) must also be spectral for \(T\). Apply this argument to \(\lambda I-S,\lambda I-T\), then interchange them.

This permits changes at eigenvalues; it does not assert equality of complete spectra or invariance of individual eigenvalues.

## Source references

Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`.
- `Materials/Lecture notes.pdf` (WS 2017/18), Propositions 12.10–12.11 and integral-equation example, pp. 86–87.
- `Problem sheets/Problem Sheet 14.pdf` and `Solutions to problem sheets/Solutions Sheet 14.pdf` (WS 2024/25), T14.4.
