---
id: tum-uq-polynomial-parameter-spaces
source: tum-numuq
parent: uq-stochastic-galerkin
title: Tensor-product and total-degree orthonormal polynomial spaces
type: concept
caption: Indexes multivariate parameter bases and quantifies their dimension under independent input laws.
---

# Tensor-product and total-degree orthonormal polynomial spaces

Build parameter polynomials as \(\psi_\alpha(y)=\prod_{i=1}^MP_{\alpha_i}^i(y_i)\), indexed by nonnegative degree vectors. Equal degree bound \(0\le\alpha_i\le k\) gives dimension \((k+1)^M\); separate bounds \(k_i\) give \(\prod_i(k_i+1)\). The complete or total-degree space imposes \(|\alpha|=\sum_i\alpha_i\le k\), giving dimension \(\binom{M+k}{k}\). It is a subspace of the equal-bound tensor product.

For \(M=2,k=1\), the tensor set includes \((0,0),(1,0),(0,1),(1,1)\), while total degree omits the mixed product \((1,1)\). Thus both contain the constant and linear terms, but only the tensor choice contains the bilinear interaction. Dimension formulas expose the rapid growth in input dimension even before multiplying by spatial FE unknowns.

If inputs are independent with joint density \(p(y)=\prod_ip_i(y_i)\), choose each univariate family orthonormal in \(L_{p_i}^2(\Gamma_i)\). Fubini factors \((\psi_\alpha,\psi_\beta)_p=\prod_i(P_{\alpha_i}^i,P_{\beta_i}^i)_{p_i}=\prod_i\delta_{\alpha_i\beta_i}\). The selected multivariate basis is therefore orthonormal. Marginal orthogonality alone does not ensure this for dependent inputs, and parameter differentiability is not part of the \(L_p^2\) norm.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, §§10.5.1–10.5.2, Examples 10.18–10.19 and Theorem 10.22 with proof in §10.5.4, pp. 78–79 and 81–82.
- `Lecture Topics and Slides/Lecture 17 (08.07.24)`, physical pp. 16–26, polynomial choices and handwritten examples.
- `Lecture Topics and Slides/Lecture 18 (11.07.24)`, physical pp. 4–5, product density and orthogonality proof.
- `Oral exam/Topics and sample questions (08.07.24)`, §10, p. 4, tensor and complete polynomial bases.
