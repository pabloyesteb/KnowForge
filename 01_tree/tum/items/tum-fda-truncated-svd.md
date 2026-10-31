---
id: tum-fda-truncated-svd
source: tum-foundations-data-analysis
parent: fda-svd
title: Optimal low-rank approximation by truncated SVD
type: theorem
caption: "Retains leading singular terms to minimize spectral and Frobenius error and applies the formulation to image approximation tasks."
---

# Optimal low-rank approximation by truncated SVD

For \(A=\sum_{i=1}^r\sigma_i u_i v_i^T\) and \(0\le k<r\), retain
\[
A_k=\sum_{i=1}^k\sigma_i u_i v_i^T.
\]
This is a best approximation among matrices of rank at most \(k\) in both spectral and Frobenius norms. The residual singular values are the discarded values, so
\[
\|A-A_k\|_2=\sigma_{k+1},\qquad
\|A-A_k\|_F=\left(\sum_{i>k}\sigma_i^2\right)^{1/2}.
\]
For \(k\ge r\), the residual is zero. Keeping a small discarded tail supports accurate compression; a rank choice alone gives no accuracy guarantee independent of that tail. The booklet uses the optimal-truncation theorem in worked examples rather than proving its full general form.

For \(\begin{pmatrix}17&8\\8&17\end{pmatrix}\), the best rank-one truncation is \(\frac{25}{2}\begin{pmatrix}1&1\\1&1\end{pmatrix}\), with both errors 9. For \(\operatorname{diag}(1,4)\), it is \(\operatorname{diag}(0,4)\), with both errors 1. The leading singular direction, rather than matrix-entry order, determines the retained term.

For the sheet's extra diagonal example \(\operatorname{diag}(1,-4)\), the leading singular value remains 4, while the matching left vector changes sign. Its best rank-one truncation is \(\operatorname{diag}(0,-4)\), again with residual norms 1. A signed eigenvalue cannot be inserted as a negative singular value.

The image task applies this construction to grayscale `peppers.png` at ranks 10, 25 and 100. The separate weekly solution supplies code and numerical outputs for that application, beyond the booklet's brief code pointer.

If a repeated singular value straddles the truncation boundary, an optimal approximation need not be unique. For example, when \(\sigma_1=\sigma_2=\sigma_3>\sigma_4\), keeping any two orthonormal singular pairs from the leading three-dimensional block gives the same optimal rank-two errors: spectral error \(\sigma_1\) and a Frobenius error determined by the identical discarded values. The rank approximation can differ while its optimal quality remains fixed. A drop in singular values is therefore useful when selecting a truncation rank.

A strict gap \(\sigma_k>\sigma_{k+1}\) makes the truncation matrix independent of basis choices within either the retained or discarded blocks, even if values repeat inside those blocks. A tie across the boundary permits infinitely many choices, as rank-one projectors approximating the two-dimensional identity demonstrate. This basis-independence statement about SVD truncation should not be read as a uniqueness theorem for every minimizer under the spectral norm.

The assessment example takes \(A=\begin{pmatrix}3&-1\\1&-3\end{pmatrix}\), singular values \(4,2\), right vectors \((1,-1)/\sqrt2,(1,1)/\sqrt2\), and left vectors \((1,1)/\sqrt2,(1,-1)/\sqrt2\). The two singular dyads reconstruct \(A\); retaining the first gives \(A_1=\begin{pmatrix}2&-2\\2&-2\end{pmatrix}\). Its error is 2 in both spectral and Frobenius norms, because exactly one singular value of size 2 is discarded.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `Introduction and general information/Booklet of Exercises FDA.pdf`, Exercises 2.1.5–2.1.6, p. 18; solutions, pp. 28–30.
- `6. Mai - 12. Mai/Problem Set 3.pdf`, Exercises 3.1–3.2, p. 1.
- `13. Mai - 19. Mai/Solution Sheet 3.pdf`, single physical page, Exercise 3.1 and signed diagonal extra example; Exercise 3.2 application.
- `20. Mai - 26. Mai/All you... math 5`, single physical page, repeated leading singular value and alternative best rank-two approximations.
- `27. Mai - 2. Juni/All you... math 6`, single physical page, opening identity-matrix example and “SVD of Differences of Matrices”, observations on a gap at the truncation boundary.
- `Introduction and general information/Sample Exam (from SoSe 2022).pdf` and `Introduction and general information/Sample Solutions for the Sample Exam.pdf`, Problem 1(a–b), p. 2 of task; combined Problem 1(a), p. 2 of handwritten solutions.
