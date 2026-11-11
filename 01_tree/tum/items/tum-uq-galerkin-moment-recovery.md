---
id: tum-uq-galerkin-moment-recovery
source: tum-numuq
parent: uq-stochastic-galerkin
title: Mean and pointwise variance from orthonormal Galerkin coefficients
type: method
caption: Extracts statistics directly from polynomial expansion coefficients without additional sampling.
---

# Mean and pointwise variance from orthonormal Galerkin coefficients

Write the finite stochastic Galerkin approximation as \(\widetilde u^{hk}(x,y)=\sum_{j=1}^Qu_j(x)\psi_j(y)\), with \(u_j(x)=\sum_{i=1}^Ju_{ij}\phi_i(x)\). Choose an orthonormal parameter basis with \(\psi_1\equiv1\) under the probability density. Then \(E\psi_j=\delta_{j1}\), so
\[
E\widetilde u^{hk}(x)=u_1(x),\qquad
E[(\widetilde u^{hk}(x))^2]=\sum_{j=1}^Qu_j(x)^2,\qquad
\operatorname{Var}\widetilde u^{hk}(x)=\sum_{j=2}^Qu_j(x)^2.
\]
These are pointwise scalar statistics of the discrete field, computed from spatial coefficient functions. A nonorthonormal basis would require its Gram matrix and basis means; simply summing coefficient squares would be invalid. The formulas give statistics of the chosen truncated/discretized approximation, not an additional guarantee of exact continuum moments.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, §10.5.5, pp. 82–83 ending before §10.6, complete expectation, second-moment and variance derivation.
- `Lecture Topics and Slides/Lecture 18 (11.07.24)`, physical pp. 6–7, coefficient moment formulas.
