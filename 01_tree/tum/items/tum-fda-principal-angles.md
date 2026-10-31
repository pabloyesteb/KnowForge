---
id: tum-fda-principal-angles
source: tum-foundations-data-analysis
parent: fda-svd
title: Basis-independent principal angles and projection discrepancy
type: theorem
caption: "Defines subspace angles from a cross-Gram SVD and expresses Frobenius projection discrepancy through their sines."
---

# Basis-independent principal angles and projection discrepancy

Let \(V,W\in\mathbb R^{d\times n}\) have orthonormal columns spanning two \(n\)-dimensional subspaces. The principal angles \(\theta_i\in[0,\pi/2]\) are defined by
\[
\cos\theta_i=\sigma_i(W^TV).
\]
The singular values lie in \([0,1]\), since taking inner products with orthonormal columns cannot increase Euclidean length.

For other orthonormal bases \(V'=VQ_1\), \(W'=WQ_2\), the cross-Gram matrix becomes \(Q_2^T(W^TV)Q_1\). Orthogonal left/right factors preserve its singular values, so the angles depend on the subspaces, not their chosen bases.

With \(P_V=VV^T\) and \(P_{W^\perp}=I-WW^T\), cyclic trace and projector identities yield
\[
\|P_{W^\perp}P_V\|_F^2
=\operatorname{tr}((I-WW^T)VV^T)
=n-\|W^TV\|_F^2
=\sum_i\sin^2\theta_i.
\]
The discrepancy measures the part of one subspace left outside the other. The booklet's two planes in \(\mathbb R^3\) give cross-Gram singular values \(1\) and \(4/\sqrt{21}\): the first angle is zero and the other is approximately \(29.2059^\circ\). Its displayed projection matrices are computed as basis matrices times their transposes; rectangular orthonormal-column matrices are not square orthogonal matrices.

Geometrically, the first cosine maximizes \(\langle v,w\rangle\) over unit vectors in the two subspaces. Subsequent cosines use vectors orthogonal to previously selected directions on each side. Maximizing cosine minimizes the corresponding acute angle. A common nonzero direction gives an angle zero. The review's coordinate planes \(\operatorname{span}(e_1,e_2)\) and \(\operatorname{span}(e_2,e_3)\) have cross-Gram singular values 1 and 0, hence angles 0 and \(\pi/2\). The ordering is recovered from singular-value order, rather than the order of a displayed unsorted diagonal.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `Introduction and general information/Booklet of Exercises FDA.pdf`, Exercises 2.1.13–2.1.14, pp. 21–22; solutions, pp. 39–40.
- `27. Mai - 2. Juni/Problem Set 6.pdf`, Exercise 6.3 and Homework 6.4, p. 2.
- `3. Juni - 9. Juni/Solution Sheet 6.pdf`, single physical page, Exercise 6.3(a–b) and Homework 6.4, trace derivation, numerical planes and basis-change argument.
- `3. Juni - 9. Juni/All you ... math 7`, single physical page, final “Principal Angles”, variational directions and coordinate-plane example.
