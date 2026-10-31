---
id: tum-fda-gram-schmidt
source: tum-foundations-data-analysis
parent: fda-linear-geometry
title: Gram–Schmidt construction of orthonormal coordinates
type: algorithm
caption: "Subtracts previous projection components and normalizes the residual to build a basis for finite-dimensional projection."
---

# Gram–Schmidt construction of orthonormal coordinates

Given linearly independent real vectors \(a_1,\ldots,a_k\), construct
\[
r_j=a_j-\sum_{i<j}\langle a_j,q_i\rangle q_i,\qquad
q_j=r_j/\|r_j\|_2.
\]
At the first step the sum is empty. Removing the previous components makes \(r_j\) orthogonal to all preceding \(q_i\); normalization makes its length one. Independence ensures the residual is nonzero. The resulting orthonormal vectors span the same subspace as the input and can be used in the Fourier projection formula. Normalizing the original vectors alone does not remove their mutual overlap.

The review works with \(a_1=(1,1,0)^T\), \(a_2=(0,1,1)^T\). They have dot product one. The first normalized vector is \(q_1=(1,1,0)^T/\sqrt2\). Subtracting \(\langle a_2,q_1\rangle q_1\) gives \(r_2=(-1/2,1/2,1)^T\), with squared norm \(3/2\); hence
\[
q_2=(-1,1,2)^T/\sqrt6.
\]
This is an exact-arithmetic construction; the review does not compare floating-point orthogonalization variants.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `29. April - 5. Mai/Notes All you... math week 2`, single physical page, second subspace example and “Gram–Schmidt Procedure”, before “Infima, Minima, Minimizing Sequences”.
