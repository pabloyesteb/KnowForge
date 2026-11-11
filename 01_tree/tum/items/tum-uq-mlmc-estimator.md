---
id: tum-uq-mlmc-estimator
source: tum-numuq
parent: uq-multilevel
title: Multilevel telescoping estimators and coupled variance reduction
type: method
caption: Uses independently sampled corrections with shared inputs inside each fine–coarse pair to preserve the finest-level
  mean.
---

# Multilevel telescoping estimators and coupled variance reduction

For geometric resolutions \(h_\ell=h_0s^{-\ell}\), \(s>1\), let \(Y_0=u_{h_0}\), \(Y_\ell=u_{h_\ell}-u_{h_{\ell-1}}\). Telescoping gives \(Eu_{h_L}=\sum_{\ell=0}^LEY_\ell\). Estimate each term with \(M_\ell\) iid draws and sum the sample means. Sample sets are independent **across** levels; inside a correction, both approximations use the same random input to make their difference small.

For Hilbert-valued approximations, with \(V_\ell=E\|Y_\ell-EY_\ell\|^2\),
\[
E\|\widehat u_{\rm ML}-Eu\|^2=\sum_{\ell=0}^L\frac{V_\ell}{M_\ell}+\|Eu_{h_L}-Eu\|^2.
\]
The estimator is unbiased for the finest discretized mean, not generally for the continuum mean. Centering and level independence eliminate cross terms. Coupling and the triangle inequality give \(V_\ell^{1/2}\le\|u_{h_\ell}-u\|_{L^2}+\|u_{h_{\ell-1}}-u\|_{L^2}\to0\), while the variance of the full solution often stays of order one.

The same telescoping idea applies to scalar quantities, powers and indicator functions; each transformed quantity needs its own bias and correction-variance analysis. The course also mentions quantiles, distributions, inverse problems, optimization and alternative multilevel quadrature as applications, without deriving their algorithms here. Small differences in state norms do not automatically give the same variance rate for discontinuous indicators.

The oral sheet illustrates model-evaluation accounting with caps of 1000 evaluations of \(Q_0\), 100 of \(Q_1\), and 10 of \(Q_2\). For the standard three-grid design, correction counts consume \(M_0+M_1\), \(M_1+M_2\), and \(M_2\) evaluations respectively. If all caps are saturated, this gives \((M_0,M_1,M_2)=(910,90,10)\), rather than counting every model evaluation as an independent correction sample. The caps alone do not determine a variance-optimal allocation without correction variances. Even for a fixed observation design, the prescribed MLMC weights need not be the minimum-variance unbiased linear weights; multilevel BLUE optimizes that larger class.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, ch. 8 opening, Definition 8.2, §8.1 and §8.4, pp. 59–61 and 63.
- `Lecture Topics and Slides/Lecture 12 (13.06.24)`, physical pp. 9–14; `Lecture Topics and Slides/Lecture 13 (18.06.24)`, physical pp. 1–8 and 15–16, including handwritten transformed-quantity telescoping.
- `Oral exam/Topics and sample questions (08.07.24)`, §8, pp. 3–4, three-grid sample accounting and optimality question.
