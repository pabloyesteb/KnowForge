---
id: tum-uq-circulant-embedding
source: tum-numuq
parent: uq-discretization
title: FFT sampling with positive semidefinite circulant embedding
type: algorithm
caption: Embeds stationary grid covariances in a circulant matrix and produces two Gaussian realizations by one complex transform.
---

# FFT sampling with positive semidefinite circulant embedding

A stationary Gaussian process sampled on a uniform one-dimensional grid has a symmetric Toeplitz covariance \(C_{ij}=c_{i-j}\). A circulant matrix instead uses indices modulo its dimension and acts as discrete circular convolution. For its first column \(c\) and the unitary negative-exponent Fourier matrix \(W\),
\[
C=WDW^*,\qquad \operatorname{diag}D=\sqrt n\,W^*c.
\]
This follows by substituting circulant entries into \(CW\), which makes each Fourier column an eigenvector. FFTs implement both transforms in \(O(n\log n)\).

For \(n>1\), set \(n'=n-1\). The minimal real symmetric circulant extension of the Toeplitz covariance has size \(q=2n'\) and first column
\[
(c_0,c_1,\ldots,c_{n'},c_{n'-1},\ldots,c_1)^T.
\]
Its leading \(n\times n\) block is the target covariance. Its real eigenvalues are
\[
d_k=c_0+c_{n'}(-1)^{k-1}+2\sum_{j=1}^{n'-1}c_j\cos\!\left(\frac{\pi j(k-1)}{n'}\right),\quad k=1,\ldots,2n',
\]
with at most \(n'+1\) distinct values. Positive semidefiniteness of \(C\) alone does not ensure \(d_k\ge0\) for its extension.

After verifying nonnegative eigenvalues, draw independent \(a,b\sim N(0,I_q)\), form \(\xi=a+ib\), and compute \(Z=WD^{1/2}\xi\). The real and imaginary parts are jointly Gaussian with covariance equal to the **real** extended covariance and zero cross-covariance, so they are independent. Restrict each part to its first \(n\) entries and add the target mean. This returns two exact target-grid realizations. Assembly costs \(O(q)\); spectral preparation and sampling cost \(O(q\log q)\).

The complex calculation uses Hermitian covariance \(E[ZZ^*]\) and pseudo-covariance \(E[ZZ^T]\). Here these are \(2\widetilde C\) and zero; expanding real/imaginary parts yields equal covariances \(\widetilde C\) and zero cross-covariance. The course's \(CN(\mu,C)\) convention assumes real \(C\) and independent real/imaginary parts of covariance \(C/2\). Accordingly, Lemma 4.11 is used with a real symmetric circulant covariance; arbitrary diagonal \(D\) would not ensure that \(WDW^*\) is real.

The one-dimensional exponential covariance has a positive definite minimal extension. For other covariances, padding extends the spatial Toeplitz covariance before forming the circulant extension; a sufficiently large extension can recover positivity under the covariance assumptions discussed in the cited analyses. Padding is not permission to ignore negative eigenvalues, and increasing size must be accompanied by the positivity check.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, §4.2, Definitions 4.2–4.6 and 4.9, Proposition 4.5, Lemmas 4.7–4.8 and 4.11–4.12, Algorithm 1 and Remarks 4.13–4.14, pp. 26–31 (before §4.3).
- `Lecture Topics and Slides/Lecture 06 (07.05.24)`, physical pp. 11–13; `Lecture Topics and Slides/Lecture 07 (14.05.24)`, physical pp. 1–12 (printed 8–18 plus handwritten recap), full FFT derivation and positivity warnings.
- `Oral exam/Topics and sample questions (08.07.24)`, §4, p. 2, sampling costs, implementation steps and pitfalls.
