---
id: tum-fda-linear-map-coordinates
source: tum-foundations-data-analysis
parent: fda-linear-geometry
title: Matrix representations of linear maps and the transpose identity
type: concept
caption: "Relates bases to matrix columns, distinguishes inner and outer products, and moves linear maps across Euclidean scalar products."
---

# Matrix representations of linear maps and the transpose identity

A linear map \(A:V\to W\) preserves addition and scalar multiplication. Choose bases \(v_1,\ldots,v_n\) of \(V\) and \(w_1,\ldots,w_m\) of \(W\). Writing
\[
Av_i=\sum_{j=1}^m a_{ji}w_j
\]
places the coordinates of each image in column \(i\) of an \(m\times n\) matrix. The matrix depends on the chosen bases; its multiplication by a coordinate vector represents the abstract map.

Matrix multiplication represents composition when the intermediate dimensions agree. It is associative but generally not commutative; matrix addition is entrywise and requires equal shapes. Transposition swaps rows and columns, satisfies \((A^T)^T=A\), and reverses product order: \((AB)^T=B^TA^T\).

For real column vectors, \(x^Ty\) is a scalar inner product, whereas \(xy^T\) is an outer-product matrix. The latter has entries \(x_i y_j\). A matrix cannot be pulled out of an inner product as if it were a scalar. Instead, for \(A\in\mathbb R^{m\times n}\), \(x\in\mathbb R^n\), \(y\in\mathbb R^m\),
\[
\langle Ax,y\rangle=\langle x,A^Ty\rangle.
\]
The dimensions and transpose are essential. This identity is the Euclidean adjoint relation used in Gram-matrix and projection arguments.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `22. April - 28. April/All you ... math 1`, single physical page, “Recap in Linear Algebra”: vector spaces, linear maps, matrices and “Scalar product and matrices”.
