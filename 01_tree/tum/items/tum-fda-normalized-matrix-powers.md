---
id: tum-fda-normalized-matrix-powers
source: tum-foundations-data-analysis
parent: fda-svd
title: Spectral-gap convergence of normalized Gram-matrix powers
type: theorem
caption: "Shows convergence to the averaged leading-eigenspace projector and quantifies decay through singular-value ratios."
---

# Spectral-gap convergence of normalized Gram-matrix powers

Let \(A\ne0\) have positive singular values \(\sigma_1\ge\cdots\ge\sigma_r\), \(B=A^TA\), and let the leading eigenvalue of \(B\) have multiplicity \(d\). For \(E=\operatorname{span}(v_1,\ldots,v_d)\),
\[
M_\ell=\frac{B^\ell}{\sum_{i=1}^r\sigma_i^{2\ell}}
\longrightarrow\frac{P_E}{d}.
\]
Indeed, divide numerator and denominator by \(\sigma_1^{2\ell}\). The first \(d\) weights remain one; all other ratios vanish.

If \(r>d\), define \(\delta=\max_{i>d}\sigma_i/\sigma_1<1\) and \(s_\ell=\sum_{i>d}(\sigma_i/\sigma_1)^{2\ell}\). The signed coefficient on each leading projector in \(M_\ell-P_E/d\) is
\[
\frac1{d+s_\ell}-\frac1d=-\frac{s_\ell}{d(d+s_\ell)}.
\]
Its absolute value is bounded by \((r-d)\delta^{2\ell}/d^2\); every remaining eigenvalue is bounded by \(\delta^{2\ell}/d\). In particular the decomposition and triangle inequality yield
\[
\|M_\ell-P_E/d\|_2\le
\left(\frac{r-d}{d^2}+\frac1d\right)\delta^{2\ell}.
\]
The important rate is geometric in \(\delta^{2\ell}\), faster with a larger gap. If \(r=d\), the normalized matrix already equals \(P_E/d\) for every positive power, without defining a maximum over an empty set. If \(A=0\), the normalization is undefined.

This is a matrix-power statement underlying the power method, not a promise that a repeated leading singular value selects one unique direction. The companion exercise requests computing dominant singular pairs by a power-method implementation, successive rank approximations, and comparison to MATLAB `svd` on `countries_data.txt`. Neither that dataset nor the requested implementation/output is supplied in the booklet.

Using the largest absolute eigenvalue, rather than summing the two coefficient bounds, gives the sharper estimate in the weekly solution:
\[
\|M_\ell-P_E/d\|_2\le
\max\left\{\frac{r-d}{d^2},\frac1d\right\}\delta^{2\ell}.
\]
The erratum explicitly corrects the missing minus sign on the leading-eigenspace coefficient. The bound concerns its magnitude; a negative coefficient cannot simply be replaced by a positive one in the matrix identity.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `Introduction and general information/Booklet of Exercises FDA.pdf`, Exercises 2.1.9–2.1.10, pp. 19–20; solutions and normalization estimates, pp. 34–36.
- `13. Mai - 19. Mai/Problem Set 4.pdf`, Exercise 4.1, p. 1.
- `20. Mai - 26. Mai/Solution Sheet 4.pdf`, single physical page, Exercise 4.1(a–b), simple/repeated leading value and maximum-coefficient norm bound.
- `20. Mai - 26. Mai/Erratum Exercise 4.1`, entire JPEG, corrected signed coefficient and its absolute-value estimate.
- `20. Mai - 26. Mai/All you... math 5`, single physical page, repeated singular values and “A Preliminary Observation on Ex. 4.1”, Gram expansion.
