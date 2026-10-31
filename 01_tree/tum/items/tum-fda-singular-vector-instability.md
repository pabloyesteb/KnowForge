---
id: tum-fda-singular-vector-instability
source: tum-foundations-data-analysis
parent: fda-svd
title: Singular-vector sensitivity near repeated singular values
type: result
caption: "Exhibits an order-one leading-vector rotation under a perturbation tending to zero when the singular gap also closes."
---

# Singular-vector sensitivity near repeated singular values

For \(0<\varepsilon<1\), consider
\[
A=\begin{pmatrix}1&0\\0&1+\varepsilon\end{pmatrix},\quad
E=\begin{pmatrix}0&\varepsilon\\\varepsilon&-\varepsilon\end{pmatrix},\quad
\widetilde A=A+E=\begin{pmatrix}1&\varepsilon\\\varepsilon&1\end{pmatrix}.
\]
The original leading right vector is \(e_2\), with singular value \(1+\varepsilon\). The perturbed matrix has leading right vector \((1,1)^T/\sqrt2\) with the same leading value, and second singular value \(1-\varepsilon\). Thus
\[
\|E\|_F=\sqrt3\,\varepsilon\to0,\qquad
\left\|e_2-\frac{(1,1)^T}{\sqrt2}\right\|_2=\sqrt{2-\sqrt2}.
\]
Even choosing the closest sign of the perturbed vector leaves a nonvanishing distance. The small-\(\varepsilon\) restriction makes the stated perturbed diagonalization an SVD with nonnegative values; the exercise's “arbitrary positive” wording otherwise needs absolute values and possible reordering.

The example demonstrates sensitivity of individual directions as the spectral gap closes. It does not show that singular values have comparable instability, or that every well-separated singular vector behaves this way. Nonuniqueness of basis choices at a repeated value must likewise be separated from instability of the matrix represented by the SVD.

The weekly solution links this sensitivity to rank selection: when several adjacent values are close, truncating within that cluster may be more sensitive than retaining or discarding the whole cluster. Sign freedom alone is not the cause of the fixed angle in the displayed perturbation example; its gap shrinks with \(\varepsilon\).

A contrasting sheet replaces the first diagonal entry by 2: \(B=\operatorname{diag}(2,1+\varepsilon)\) and \(B+E=\begin{pmatrix}2&\varepsilon\\\varepsilon&1\end{pmatrix}\). For small positive \(\varepsilon\), the unperturbed leading direction is \(e_1\), and the separated limiting values are 2 and 1. The supplied numerical examples at \(\varepsilon=0.5,0.25,0.125\) show the perturbed right directions approaching the coordinate directions as the perturbation decreases. This contrasts with the fixed angle in the closing-gap example; “separated” is relative to perturbation size, not an absolute label applicable at all positive \(\varepsilon\).

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `Introduction and general information/Booklet of Exercises FDA.pdf`, Exercise 2.1.11, p. 20; solution, p. 37.
- `20. Mai - 26. Mai/Problem Set 5.pdf`, Exercise 5.2(a–c), p. 2.
- `27. Mai - 2. Juni/Solution Sheet 5.pdf`, single physical page, Exercise 5.2(a–c) and final clustered-spectrum observation.
- `27. Mai - 2. Juni/Problem Set 6.pdf`, Exercise 6.1(a–c), p. 1.
- `3. Juni - 9. Juni/Solution Sheet 6.pdf`, single physical page, Exercise 6.1(a–c), separated example and numerical singular pairs.
