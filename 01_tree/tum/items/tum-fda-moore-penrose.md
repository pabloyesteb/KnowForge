---
id: tum-fda-moore-penrose
source: tum-foundations-data-analysis
parent: fda-svd
title: Moore–Penrose inverse from singular coordinates
type: method
caption: "Inverts nonzero singular values and relates full-rank formulas to the four Penrose conditions."
---

# Moore–Penrose inverse from singular coordinates

For a rank-\(r\) matrix with reduced SVD \(A=U_r\Sigma_rV_r^H\), form
\[
A^\dagger=V_r\Sigma_r^{-1}U_r^H.
\]
Only the nonzero singular values are reciprocated; zero directions are left at zero in a full representation. The resulting matrix satisfies
\[
AA^\dagger A=A,\quad A^\dagger AA^\dagger=A^\dagger,\quad
(AA^\dagger)^H=AA^\dagger,\quad
(A^\dagger A)^H=A^\dagger A.
\]
These follow by multiplying the singular-coordinate factors and using orthonormality. In particular \(AA^\dagger=U_rU_r^H\) and \(A^\dagger A=V_rV_r^H\) are orthogonal projectors.

With independent columns, \(A^HA\) is invertible and \(A^\dagger=(A^HA)^{-1}A^H\); then \(A^\dagger A=I\). With independent rows, the corresponding expression is \(A^\dagger=A^H(AA^H)^{-1}\), with \(AA^\dagger=I\). These ordinary inverse formulas need their rank assumptions. The booklet motivates the pseudoinverse by least-squares systems and asks for the conditions and SVD construction without supplying a separate worked solution.

For an invertible square \(B=U\Sigma V^T\), the same formula is its ordinary inverse: \(B^{-1}=V\Sigma^{-1}U^T=\sum_i\sigma_i^{-1}v_i u_i^T\). Multiplication collapses mixed terms by orthogonality and leaves the identity resolution \(I=\sum_i u_i u_i^T\). Inverting reverses the order of positive magnitudes: an ordered SVD of the inverse requires reordering the reciprocal values and their paired vectors.

For full column rank, the Penrose conditions can also be verified without an SVD. Let \(G=A^TA\), which is invertible and symmetric. Then \(A^\dagger A=G^{-1}G=I\), giving the first two conditions; \(AA^\dagger=AG^{-1}A^T\) is symmetric because \((G^{-1})^T=(G^T)^{-1}=G^{-1}\). The fourth condition follows from \(A^\dagger A=I\).

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `Introduction and general information/Booklet of Exercises FDA.pdf`, Chapter 2 further exercise “Pseudoinverse matrix and its SVD”, p. 23.
- `20. Mai - 26. Mai/Problem Set 5.pdf`, Exercise 5.1(a–c) and extra, p. 1.
- `27. Mai - 2. Juni/Solution Sheet 5.pdf`, single physical page, Exercise 5.1(a–c) and extra: inverse by SVD, direct Penrose proof, rectangular inverse construction.
- `3. Juni - 9. Juni/All you ... math 7`, single physical page, “Moore–Penrose Pseudo-Inverse”, SVD construction, reciprocal ordering, full-rank square inverse and rank-deficient example.
