---
id: tum-uq-gaussian-hilbert-series
source: tum-numuq
parent: uq-random-fields
title: Square-summable Gaussian series in Hilbert spaces
type: theorem
caption: Constructs Hilbert-valued Gaussian variables and their covariance from orthonormal expansions.
---

# Square-summable Gaussian series in Hilbert spaces

Let \(H\) be a separable real Hilbert space with orthonormal basis \((\psi_n)\), let \((\gamma_n)\in\ell^2\), and let \(\xi_n\) be independent standard normal variables. For \(Z_N=\sum_{n=1}^N\gamma_n\xi_n\psi_n\),
\[
E\|Z_M-Z_N\|_H^2=\sum_{n=N+1}^M\gamma_n^2.
\]
Completeness gives \(Z_N\to Z\) in \(L^2(\Omega;H)\), with mean zero. For every bounded scalar sequence \((c_n)\), \(\sum c_n\gamma_n\xi_n\) converges in scalar \(L^2\) to a Gaussian of variance \(\sum c_n^2\gamma_n^2\), since Gaussian finite sums converge in mean square.

Taking \(c_n=(h,\psi_n)_H\), which is bounded by \(\|h\|_H\), proves that \(Z\) is an \(H\)-valued Gaussian. For \(h,k\in H\), truncation followed by \(L^2\) convergence justifies
\[
\operatorname{Cov}((h,Z)_H,(k,Z)_H)=\sum_n\gamma_n^2(h,\psi_n)_H(k,\psi_n)_H.
\]
The solution's final display repeats \(h\) in its second factor; that factor must involve \(k\).

When basis functions on \(D\) have a uniform bound \(\sup_{n,x}|\psi_n(x)|<\infty\), define pointwise limits of the same series in \(L^2(\Omega)\). Every finite spatial linear combination has bounded coefficients \(\sum_i b_i\psi_n(x_i)\), so these limits form a centered Gaussian field with covariance
\[
c(x,y)=\sum_n\gamma_n^2\psi_n(x)\psi_n(y).
\]
The series is uniformly absolutely convergent under the stated bound; finite-sum covariances pass to the limit in \(L^2\). This pointwise construction must be distinguished from evaluating an arbitrary equivalence-class representative of the Hilbert limit when point evaluation is not continuous in \(H\).

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Problem Sheets/Problem Sheet 01 (25.04.2024)`, Problem 5(a)–(d); `Problem Sheets/Solution Sheet 01 (update  complete).pdf`, pp. 5–7.
