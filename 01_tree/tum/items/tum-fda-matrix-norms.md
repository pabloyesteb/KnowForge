---
id: tum-fda-matrix-norms
source: tum-foundations-data-analysis
parent: fda-linear-geometry
title: Frobenius and spectral matrix norms
type: concept
caption: "Contrasts entrywise Euclidean size with maximum amplification and computes a diagonal spectral norm through constrained stationarity."
---

# Frobenius and spectral matrix norms

For \(A\in\mathbb R^{m\times n}\),
\[
\|A\|_F=\left(\sum_{i,j}|a_{ij}|^2\right)^{1/2}
=\|\operatorname{vec}(A)\|_2,
\]
where vectorization stacks the columns and is linear. Thus definiteness, homogeneity and the triangle inequality transfer directly from the Euclidean norm on \(\mathbb R^{mn}\). The norm measures all matrix entries collectively.

The spectral/operator norm measures maximum Euclidean amplification:
\[
\|A\|_2=\max_{\|x\|_2=1}\|Ax\|_2.
\]
For \(A=\operatorname{diag}(1,4)\), maximize its squared output \(x_1^2+16x_2^2\) subject to \(x_1^2+x_2^2=1\). The Lagrangian
\[
L=x_1^2+16x_2^2-\lambda(x_1^2+x_2^2-1)
\]
has stationarity equations \((1-\lambda)x_1=0\), \((16-\lambda)x_2=0\). Feasible stationary candidates are the two coordinate-axis pairs, with squared objective 1 or 16. Compactness of the sphere guarantees attainment; comparing the candidates yields \(\|A\|_2=4\). Its Frobenius norm is \(\sqrt{17}\), so the two norms are different even for a diagonal matrix.

The Lagrange multiplier corresponds here to the squared amplification, not directly to the unsquared matrix norm. This constrained-maximization formulation connects matrix geometry to optimality conditions without presuming an algorithm or numerical experiment.

More generally, the squared amplification is the quadratic form \(\|Ax\|_2^2=x^TA^TAx\). Thus its constrained stationarity equation on the Euclidean unit sphere is \(A^TAx=\lambda x\); the diagonal example compares the corresponding squared objective values before taking the square root. A stationary candidate alone does not identify the maximum without that comparison.

In singular-value coordinates, orthogonal changes preserve Euclidean and Frobenius size, giving
\[
\|A\|_2=\sigma_1,\qquad
\|A\|_F=\left(\sum_{i=1}^r\sigma_i^2\right)^{1/2},\qquad
\|A\|_* =\sum_{i=1}^r\sigma_i.
\]
The last quantity is the nuclear norm. For the symmetric matrix with diagonal 17 and off-diagonal 8, the singular values 25 and 9 give respectively \(25,\sqrt{706},34\). Nonnegative ordering matters even for diagonal matrices: \(\operatorname{diag}(1,4)\) has leading singular value 4, not its first diagonal entry. Negative eigenvalues change singular-vector signs while singular values remain nonnegative.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `Introduction and general information/Booklet of Exercises FDA.pdf`, Exercises 1.1.3(a)/1.1.6(b), pp. 4–5; solutions, pp. 10, 14–15.
- `15. April - 21. April/Exercise sheet 0.pdf`, Exercise 0.3(a), p. 2; `22. April - 28. April/Problem Set 1.pdf`, Exercise 1.3(b), p. 2.
- `29. April - 5. Mai/Solution Sheet 1.pdf`, Exercise 1.3(b), single physical page, final portion.
- `Introduction and general information/Booklet of Exercises FDA.pdf`, Exercise 2.1.2(b), p. 16 and solution p. 25; Exercise 2.1.5 and solutions, pp. 18, 28–29.
