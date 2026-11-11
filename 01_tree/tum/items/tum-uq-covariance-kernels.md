---
id: tum-uq-covariance-kernels
source: tum-numuq
parent: uq-random-fields
title: Second-order fields and admissible covariance kernels
type: concept
caption: Connects covariance positivity, finite sampling matrices and common spatial correlation models.
---

# Second-order fields and admissible covariance kernels

A second-order field satisfies \(Z(x)\in L^2(\Omega)\) at every point. Its mean \(\mu(x)\) and covariance \(c(x,y)=E[(Z(x)-\mu(x))(Z(y)-\mu(y))]\) are finite. Cauchy–Schwarz gives \(|c(x,y)|\le\sqrt{c(x,x)c(y,y)}\). The kernel is symmetric and positive semidefinite because
\[
\sum_{j,k}a_ja_kc(x_j,x_k)=E\left[\left(\sum_j a_j(Z(x_j)-\mu(x_j))\right)^2\right]\ge0.
\]
For finitely many sample points, \(C_{ij}=c(x_i,x_j)\) is a symmetric positive semidefinite matrix and \(\operatorname{tr}C=E\|\mathbf Z-\boldsymbol\mu\|_2^2\). Conversely, any finite-valued symmetric positive semidefinite kernel is a covariance kernel, as follows by constructing the consistent Gaussian field.

The notes use variance \(\sigma^2\), correlation lengths \(\ell,\ell_i>0\), and the following models:
\[
\begin{aligned}
c_{\rm sep}(x,y)&=\sigma^2\prod_i e^{-|x_i-y_i|/\ell_i},\\
c_{\rm exp}(x,y)&=\sigma^2e^{-\|x-y\|_2/\ell},\\
c_{\rm Gauss}(x,y)&=\sigma^2e^{-\|x-y\|_2^2/\ell^2},\\
c_{\rm Mat}(x,y)&=\frac{\sigma^2}{2^{q-1}\Gamma(q)}\left(\frac{\sqrt{2q}\,r}{\ell}\right)^qK_q\left(\frac{\sqrt{2q}\,r}{\ell}\right),\quad r=\|x-y\|_2,\ q>0.
\end{aligned}
\]
The Matérn diagonal is interpreted by its limit. Correlation length controls spatial correlation; the plotted exponential and Gaussian examples at lengths 0.01, 0.1 and 1 illustrate different path roughness as well as correlation scales, rather than establishing regularity by themselves.

Pointwise second-order integrability does **not** by itself make the kernel uniformly bounded, despite the statement following Corollary 3.8. A uniform bound on the diagonal variance suffices by Cauchy–Schwarz; pointwise finite variances need not have a bounded supremum.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, §3.2, Definitions 3.6–3.7 and 3.13, Corollaries 3.8 and 3.14, Examples 3.9–3.12 and Theorem 3.15, pp. 17–20; Figures 1–2, pp. 21–22.
- `Lecture Topics and Slides/Lecture 04 (25.04.24)`, physical pp. 8–25, covariance models and Gaussian-path plots; `Lecture Topics and Slides/Lecture 05 (30.04.24)`, repeated Gaussian-path plots.
