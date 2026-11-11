---
id: tum-uq-stochastic-matrix-structure
source: tum-numuq
parent: uq-stochastic-galerkin
title: Sparse stochastic multiplication matrices and polynomial-root spectra
type: theorem
caption: Uses orthogonal-polynomial recurrences to identify parameter couplings and resolution-independent spectral bounds.
---

# Sparse stochastic multiplication matrices and polynomial-root spectra

For independent parameters with even densities on symmetric bounded intervals and product orthonormal polynomial basis \(\psi_\alpha\),
\[
[G_m]_{\alpha\beta}=(y_mP_{\alpha_m}^m,P_{\beta_m}^m)_{p_m}\prod_{i\ne m}\delta_{\alpha_i\beta_i}.
\]
The even-weight three-term recurrence permits a nonzero entry only when \(\beta=\alpha\pm e_m\), with the corresponding recurrence coefficient. Consequently \(G_0=I\), each \(G_m\) is symmetric with zero diagonal and at most two entries per row. Restricted index sets may remove neighbors. The global Galerkin matrix is block sparse with sparse FE blocks; all its diagonal blocks equal \(A_0\).

For the complete total-degree space \(|\alpha|\le k\), fix all components except \(\alpha_m\). The remaining indices form a chain of length \(k-|\alpha_{\ne m}|+1\). Permuting by these chains makes \(G_m\) block diagonal, each block a leading principal section \(T_r\) of the univariate Jacobi matrix. There are \(\binom{M-1+k}{k}\) chains, one of maximal length \(k+1\). Its spectrum is the union, with multiplicity, of the roots of the univariate \(P_r\) for those chain lengths. In one parameter only the maximal block occurs; for more parameters every size through \(k+1\) occurs.

Each root is simple within an individual Jacobi block, but different polynomial degrees can share roots (zero for odd degrees with even weight). Thus the notes' statement that all maximal-polynomial roots have total multiplicity one needs qualification; repeated occurrences across blocks must be counted. All eigenvalues lie within the parameter support, so the spectrum is bounded by that support rather than deteriorating with FE mesh refinement. This does not itself precondition the spatial stiffness factors.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, §§10.6.2–10.6.3, Assumption 10.24, Theorems 10.25–10.26 with sparsity proof and spectral sketch, pp. 85–87.
