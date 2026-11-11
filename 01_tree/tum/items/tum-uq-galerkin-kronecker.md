---
id: tum-uq-galerkin-kronecker
source: tum-numuq
parent: uq-stochastic-galerkin
title: Affine stochastic Galerkin systems and Kronecker factors
type: method
caption: Separates spatial stiffness matrices from parameter multiplication matrices in a coupled block system.
---

# Affine stochastic Galerkin systems and Kronecker factors

For \(\widetilde a(x,y)=a_0(x)+\sum_{m=1}^Ma_m(x)y_m\), insert \(u^{hk}=\sum_{i,j}u_{ij}\phi_i(x)\psi_j(y)\) and test with each tensor basis function. Stack the spatial coefficient vector for each \(\psi_j\) consecutively. The \(JQ\times JQ\) system has blocks
\[
A_{\ell j}=(\psi_\ell,\psi_j)_pA_0+\sum_m(y_m\psi_\ell,\psi_j)_pA_m,
\qquad [A_m]_{ik}=\int_Da_m\nabla\phi_i\cdot\nabla\phi_k.
\]
Defining \([G_0]_{\ell j}=(\psi_\ell,\psi_j)_p\) and \([G_m]_{\ell j}=(y_m\psi_\ell,\psi_j)_p\) gives
\[
A=G_0\otimes A_0+\sum_{m=1}^MG_m\otimes A_m.
\]
The Kronecker product replaces each scalar entry of the left matrix by that multiple of the right matrix. Thus spatial and parameter components can be stored and applied separately.

For deterministic forcing, load block \(b_\ell=(E\psi_\ell)b_0\), where \([b_0]_k=\int_Df\phi_k\). With an orthonormal basis and first mode one, \(G_0=I\) and only the first load block is nonzero. Uniform positive diffusion makes the assembled system symmetric positive definite, although individual fluctuation stiffness factors \(A_m\) need not be positive. The source's block-matrix picture repeats some entries in its second row; the indexed block formula defines the intended matrix.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, §10.6 through §10.6.1, equations (10.27)–(10.34) and Definition 10.23, pp. 83–85.
- `Lecture Topics and Slides/Lecture 18 (11.07.24)`, physical pp. 9–13 (printed 35–39), full block and factor displays.
