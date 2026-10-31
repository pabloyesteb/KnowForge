---
id: tum-fa-spectrum-resolvent
source: tum-functional-analysis
parent: fa-spectral-theory
title: Resolvent expansions and the different kinds of spectrum
type: concept
---

# Resolvent expansions and the different kinds of spectrum

## Invertibility and spectral classification

For bounded \(T\) on a nonzero Banach space \(X\) over \(\mathbb K\),
\[
\rho(T)=\{\lambda:\lambda I-T\text{ bijective}\},\quad
R_\lambda=(\lambda I-T)^{-1},\quad\sigma(T)=\mathbb K\setminus\rho(T).
\]
Bounded inverse makes \(R_\lambda\) bounded. The spectrum partitions into:

- Point spectrum: \(\ker(\lambda I-T)\ne0\).
- Continuous spectrum: \(\lambda I-T\) injective with dense, proper range.
- Residual spectrum: \(\lambda I-T\) injective with nondense range.

Finite-dimensional injectivity implies surjectivity, so only point spectrum occurs there. In infinite dimensions, diagonal multiplication by \(1/n\) on \(\ell^2\) is injective with dense, proper range: zero is continuous spectrum. Right shift has closed range \(\{y:y_1=0\}\), making zero residual spectrum.

## Local resolvent series and the spectral bound

For \(\lambda_0\in\rho(T)\), factor \(\lambda I-T=(\lambda_0I-T)[I-(\lambda_0-\lambda)R_{\lambda_0}]\). Neumann inversion yields
\[
R_\lambda=\sum_{k=0}^\infty(\lambda_0-\lambda)^kR_{\lambda_0}^{k+1},
\qquad |\lambda-\lambda_0|<\|R_{\lambda_0}\|^{-1}.
\]
Thus the resolvent set is open. If \(|\lambda|>\|T\|\),
\[
R_\lambda=\lambda^{-1}\sum_{k=0}^\infty(T/\lambda)^k,
\qquad\|R_\lambda\|\le\frac1{|\lambda|-\|T\|}.
\]
Consequently \(\sigma(T)\) is compact and contained in \(\{|\lambda|\le\|T\|\}\). Over \(\mathbb C\) it is nonempty. If it were empty, every scalar function \(\ell(R_\lambda)\), \(\ell\in\mathcal L(X)^*\), would be entire by the local power series, bounded and tending to zero at infinity. Liouville and Hahn–Banach would force \(R_\lambda=0\), contradicting invertibility. Nonemptiness is not asserted over \(\mathbb R\).

## Approximate eigenvectors and lower bounds

If \(\|x_n\|=1\) and \((\lambda I-T)x_n\to0\), then \(\lambda\in\sigma(T)\): a bounded inverse would imply \(1\le\|R_\lambda\|\|(\lambda I-T)x_n\|\to0\). These are approximate eigenvectors, not necessarily exact eigenvectors.

Conversely a bound \(\|(\lambda I-T)x\|\ge c\|x\|\), \(c>0\), implies injectivity and closed range: a Cauchy sequence of outputs has Cauchy preimages. It excludes point and continuous spectrum, but may leave residual spectrum.

For the Cesàro map on \(\ell^\infty\), \((Ax)_n=n^{-1}\sum_{k=1}^nx_k\), \(\|A\|=1\) and \(\|Ae_n\|_\infty=1/n\). It is injective (successive partial sums recover the coordinates), but cannot be bijective: the inverse would violate bounded inverse on these unit-vector tests. Hence zero is spectral without being an eigenvalue.

## Source references

Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`.
- `Materials/Lecture notes.pdf` (WS 2017/18), Definitions 12.1/12.3–12.4, Propositions 12.2/12.5 and examples, pp. 81–83.
- `Problem sheets/Problem Sheet 13.pdf` and `Solutions to problem sheets/Solutions Sheet 13.pdf`, T13.1.
- `Mock Exam/Mock Exam.pdf` and `Mock Exam/Solutions to Mock Exam.pdf`, P.2 (WS 2024/25).
