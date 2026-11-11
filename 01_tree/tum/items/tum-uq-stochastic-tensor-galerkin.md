---
id: tum-uq-stochastic-tensor-galerkin
source: tum-numuq
parent: uq-stochastic-galerkin
title: Conforming stochastic Galerkin tensor approximation
type: method
caption: Combines spatial finite elements with parameter approximation while preserving energy best approximation.
---

# Conforming stochastic Galerkin tensor approximation

For the uniformly positive parametric coefficient, choose \(V^{hk}\subset L_p^2(\Gamma;H_0^1(D))\) and solve \(\widetilde{\mathcal A}(\widetilde u^{hk},v)=\ell(v)\) for every \(v\in V^{hk}\). Restricting the bounded coercive form gives a unique discrete solution. Symmetry gives energy orthogonality and
\[
\|\widetilde u-\widetilde u^{hk}\|_E=\inf_{v\in V^{hk}}\|\widetilde u-v\|_E,
\qquad
\|\widetilde u-\widetilde u^{hk}\|_{L_p^2(H_0^1)}
\le\sqrt{\widetilde a_{\max}/\widetilde a_{\min}}\inf_{v\in V^{hk}}\|\widetilde u-v\|_{L_p^2(H_0^1)}.
\]
Here \(\|v\|_E^2=\int_\Gamma p(y)\int_D\widetilde a|\nabla v|^2\).

The course constructs \(V^{hk}=W^h\otimes S^k\), where \(W^h=\operatorname{span}\{\phi_1,\ldots,\phi_J\}\subset H_0^1(D)\) is a spatial FE space and \(S^k=\operatorname{span}\{\psi_1,\ldots,\psi_Q\}\subset L_p^2(\Gamma)\) a deterministic parameter space. Basis functions are \(\phi_i(x)\psi_j(y)\), with \(JQ\) unknown coefficients. The label “stochastic basis” describes dependence on random parameters; the basis functions themselves are deterministic. Mesh and parameter discretizations are separate approximation choices, and conformity alone does not specify either convergence rate.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, §10.4, Definitions 10.15, Theorems 10.16–10.17 and tensor-space construction, pp. 77–78.
- `Lecture Topics and Slides/Lecture 17 (08.07.24)`, physical pp. 13–15 (printed 18–20), including corrected density weight in the energy norm.
