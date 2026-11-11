---
id: tum-uq-galerkin-matrix-free
source: tum-numuq
parent: uq-stochastic-galerkin
title: Matrix-free Kronecker products for stochastic Galerkin PCG
type: algorithm
caption: Applies the coupled Galerkin operator through reshaped spatial and stochastic factors without assembling it.
---

# Matrix-free Kronecker products for stochastic Galerkin PCG

For \(v\in\mathbb R^{JQ}\), reshape its consecutive spatial blocks into \(V\in\mathbb R^{J\times Q}\). The column-stacking identity
\[
(B_1\otimes B_2)\operatorname{vec}V=\operatorname{vec}(B_2VB_1^T)
\]
gives \(Av=\operatorname{vec}(A_0V)+\sum_{m=1}^M\operatorname{vec}(A_mVG_m^T)\) for an orthonormal basis. A block implementation instead forms \(w_\ell=A_0v_\ell+\sum_{m,j}[G_m]_{\ell j}A_mv_j\), exploiting only nonzero stochastic couplings. Spatial products and output block combinations admit parallel computation. All required \(A_mv_j\) can be reused rather than recomputed for each output block; there are \((M+1)Q\) products including \(A_0V\), correcting the solution text's abbreviated count.

Supplied `SG_matvec.m` loops over **all** factors, including \(G_0,A_0\). It computes a spatial sparse matrix–dense block product, transposes to apply the stochastic factor, transposes back, and vectorizes. This is exactly the Kronecker action in the specified ordering, avoiding the full \(JQ\times JQ\) matrix. `oned_SG_FEM.m` passes it as a function handle to MATLAB `pcg` with relative residual tolerance \(10^{-6}\), at most 1000 iterations and a zero **vector** initial guess. The solution handout's `zeros(J*Q)` creates a square matrix; the supplied driver uses `zeros(J*Q,1)`.

PCG applies because the full Galerkin operator is symmetric positive definite under the uniform ellipticity assumptions. Avoiding assembly reduces operator storage, but coefficient-vector and block workspace storage still scale with \(JQ\), and iteration cost depends on sparsity of the factors.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Problem Sheets/Sheet 05 (02.07.2023)`, Problem 17(a)–(c); `Problem Sheets/Solution Sheet 05.pdf`, pp. 2–3, block action, vectorization identity and PCG call.
- `Problem Sheets/SG_matlab.zip`, complete `SG_matvec.m` and PCG construction in `oned_SG_FEM.m`.
