---
id: tum-uq-mfmc-model-management
source: tum-numuq
parent: uq-multilevel
title: Optimal multifidelity coefficients, ordering and sample ratios
type: theorem
caption: Optimizes nested model sampling at fixed work under explicit cost–correlation ordering conditions.
---

# Optimal multifidelity coefficients, ordering and sample ratios

Set \(\rho_\ell=\rho_{L,\ell}\), \(\rho_0=0\), \(\rho_L=1\), and \(\Delta_\ell=\rho_\ell^2-\rho_{\ell-1}^2\). The source assumes strictly increasing absolute correlations and
\[
C_{\ell+1}/C_\ell>\Delta_{\ell+1}/\Delta_\ell,\qquad\ell=1,\ldots,L-1.
\]
Together with positive model variances and nondegenerate differences, these make the optimal sample ratios compatible with descending nested counts. Correlation alone does not make an arbitrarily expensive surrogate worthwhile.

For fixed total production cost \(p\), the continuous-count optimum is
\[
a_\ell^*=\rho_\ell\sigma_L/\sigma_\ell,\quad
r_\ell=\sqrt{\frac{C_L\Delta_\ell}{C_\ell(1-\rho_{L-1}^2)}},\quad
M_L^*=\frac p{\sum_j C_jr_j},\quad M_\ell^*=M_L^*r_\ell.
\]
The sign differs from the single-control formula because the nested control difference is ordered oppositely. Here \(r_L=1\). The minimal variance is
\[
\frac{\sigma_L^2}{p}\left(\sum_{\ell=1}^L\sqrt{C_\ell\Delta_\ell}\right)^2.
\]
The source states this result by reference; it does not derive the full model-management theorem. Integer counts need rounding that preserves nesting and enough high-fidelity samples; the real-valued optimum is not automatically a feasible integer design. Perfect correlations or zero variances require separate treatment of the displayed divisions. Costs of pilot estimation of variances and correlations are excluded from \(p\); they must be included in a complete work comparison.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, Assumption 9.7, Theorem 9.8, equations (9.9)–(9.15), p. 68; Remark 9.13, p. 71.
- `Lecture Topics and Slides/Lecture 14 (25.06.24)`, physical pp. 8–9 (printed 7–8).
