---
id: tum-fda-singular-decomposition
source: tum-foundations-data-analysis
parent: fda-svd
title: Singular decompositions and the four fundamental subspaces
type: concept
caption: "Constructs singular pairs from Gram eigenvectors and reads range, kernel and orthogonal complements from the full decomposition."
---

# Singular decompositions and the four fundamental subspaces

For a real rank-\(r\) matrix \(A\in\mathbb R^{m\times n}\), a reduced singular value decomposition is
\[
A=U_r\Sigma_rV_r^T=\sum_{i=1}^r\sigma_i u_i v_i^T,
\quad \sigma_1\ge\cdots\ge\sigma_r>0,
\quad U_r^TU_r=V_r^TV_r=I_r.
\]
Right singular vectors satisfy \(A^TAv_i=\sigma_i^2v_i\), and \(u_i=Av_i/\sigma_i\). Consequently \(\langle u_i,u_j\rangle=(\sigma_j/\sigma_i)\langle v_i,v_j\rangle\), proving orthonormality. The successive-maximization formulation chooses a unit input orthogonal to previous right vectors; its feasible sets shrink, so the successive maximum amplifications cannot increase.

Extend these columns to orthogonal matrices \(U=[U_r,\widehat U]\) and \(V=[V_r,\widehat V]\). A full SVD uses a rectangular \(m\times n\) diagonal matrix with the positive singular values followed by zeros. It gives
\[
\operatorname{range}A=\operatorname{span}U_r,\quad
\ker A=\operatorname{span}\widehat V,\quad
(\operatorname{range}A)^\perp=\operatorname{span}\widehat U,\quad
(\ker A)^\perp=\operatorname{span}V_r.
\]
Here the kernel consists of inputs mapped to zero, and the range consists of all outputs. Their dimensions are \(n-r\) and \(r\), respectively. The reduced form represents the same map but omits complement bases.

For \(A=\begin{pmatrix}17&8\\8&17\end{pmatrix}\), the singular values are 25 and 9, with matching left/right vectors \((1,1)^T/\sqrt2\) and \((1,-1)^T/\sqrt2\). For the booklet's \(3\times4\) matrix with rows \((-1,0,1,1)\), \((1,1,1,0)\), \((-1,1,3,2)\), using the smaller matrix \(AA^T\) gives eigenvalues 18, 3 and 0: the rank is two, the positive singular values are \(\sqrt{18},\sqrt3\), and the left nullspace is spanned by \((2,1,-1)^T\). Kernel basis vectors \((1,-2,1,0)^T\), \((1,0,-1,2)^T\) are orthogonal but need normalization to be an ONB.

The further rotation task treats row vectors as points. Rotating every point by an orthogonal \(R\) produces \(C=AR^T\), so if \(A=U\Sigma V^T\), then \(C=U\Sigma(RV)^T\): the singular values are unchanged and the right directions rotate with the points. The named `Bird_Data` dataset is not supplied; this algebra does not constitute a performed numerical experiment.

Transposition exchanges the left and right singular vectors without changing the positive singular values. Thus one may diagonalize \(AA^T\) instead of \(A^TA\) when it is smaller, then recover the opposite singular vectors and swap their roles. A real singular pair can simultaneously change sign: replacing \((u_i,v_i)\) by \((-u_i,-v_i)\) leaves its rank-one term unchanged. For a repeated Gram eigenvalue, choose an orthonormal basis within its eigenspace, using Gram–Schmidt if needed; arbitrary unnormalized eigenvectors do not automatically form singular-vector matrices.

The complement identities also follow directly from the transpose relation: \(v\in\ker A\) iff \(\langle v,A^Ty\rangle=0\) for every \(y\), so \(\ker A=(\operatorname{range}A^T)^\perp\). Similarly \(\ker A^T=(\operatorname{range}A)^\perp\). Finite-dimensional orthogonal decomposition and rank–nullity give \(\mathbb R^n=\ker A\oplus\operatorname{range}A^T\) and \(n=\dim\ker A+\operatorname{rank}A\).

Ordered singular values are uniquely determined by the matrix; their vector bases need not be. For a repeated positive value \(\sigma\), rotate its right basis by any orthogonal \(Q\) and its left basis by the same \(Q\). The block product is unchanged because \((UQ)\sigma I(VQ)^T=U\sigma IV^T\). Distinct singular values leave simultaneous sign freedom over the reals, while repeated values permit arbitrary orthonormal bases of their singular subspaces.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `Introduction and general information/Booklet of Exercises FDA.pdf`, Exercises 2.1.1–2.1.4, pp. 16–17; solutions, pp. 24–27; further rotation exercise, p. 23.
- `29. April - 5. Mai/Problem Set 2.pdf`, Exercises 2.1–2.3 and Homework 2.4, pp. 1–2.
- `6. Mai - 12. Mai/Solution Sheet 2.pdf`, single physical page, Exercises 2.1–2.3 and Homework 2.4, including sign choices, range/kernel proofs and smaller-Gram calculation.
- `6. Mai - 12. Mai/All you ... math 3`, single physical page, diagonalization procedure and worked rectangular example, “Kernel, Image, Orthogonal Complement” and final “Remark on S.V.D.”.
- `13. Mai - 19. Mai/All you... math 4`, single physical page, “Uniqueness of SVD (Repetition, Complementary)”, sign choices and repeated-value basis example.
