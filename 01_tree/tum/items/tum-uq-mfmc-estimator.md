---
id: tum-uq-mfmc-estimator
source: tum-numuq
parent: uq-multilevel
title: Nested-sample multifidelity Monte Carlo
type: method
caption: Uses estimated low-fidelity means as correlated controls while retaining the high-fidelity expectation.
---

# Nested-sample multifidelity Monte Carlo

Let \(Q_L\) be an expensive accurate approximation to a scalar target \(Q\), and \(Q_1,\ldots,Q_{L-1}\) cheaper correlated models. They may come from reduced or data-driven models rather than a mesh hierarchy. For counts \(M_1\ge\cdots\ge M_L>0\), draw iid **joint model realizations**, reusing the first \(M_{\ell+1}\) samples of model \(\ell\) inside its longer sample mean. Define
\[
\widehat Q_{\rm MF}=\bar Q_{L,M_L}+\sum_{\ell=1}^{L-1}a_\ell(\bar Q_{\ell,M_\ell}-\bar Q_{\ell,M_{\ell+1}}).
\]
Each difference has zero expectation, so this is unbiased for \(EQ_L\). Its MSE relative to \(EQ\) is its variance plus \((EQ_L-EQ)^2\). Controls need no known exact means; nested sampling estimates them.

For jointly sampled outputs with standard deviations \(\sigma_\ell>0\) and correlations \(\rho_{j,\ell}\), counting shared indices gives \(\operatorname{Cov}(\bar Q_{\ell,M_\ell},\bar Q_{j,M_j})=\rho_{\ell,j}\sigma_\ell\sigma_j/\max(M_\ell,M_j)\). Substituting and cancelling cross-control contributions yields
\[
\operatorname{Var}\widehat Q_{\rm MF}=\frac{\sigma_L^2}{M_L}+\sum_{\ell<L}\left(\frac1{M_{\ell+1}}-\frac1{M_\ell}\right)
(a_\ell^2\sigma_\ell^2-2a_\ell\rho_{L,\ell}\sigma_L\sigma_\ell).
\]
Thus this particular estimator variance depends on correlations with the high-fidelity model, not on all low-model pair correlations. The cancellation relies on the specified nested common-input structure; independently generating every model mean would invalidate the formula. Evaluation cost is \(\sum_\ell M_\ell C_\ell\).

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, §§9.1–9.3, Lemmas 9.1, 9.4–9.5, Corollary 9.2 and Remark 9.6, pp. 64–67, full covariance/variance derivation.
- `Lecture Topics and Slides/Lecture 14 (25.06.24)`, physical pp. 1–7 (title and printed 1–6).
- `Oral exam/Topics and sample questions (08.07.24)`, §9, p. 4, MFMC definition, variance and distinction from MLMC.
