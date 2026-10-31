---
id: tum-fda-conjugate-affine-rule
source: tum-foundations-data-analysis
parent: fda-convex-optimization
title: Conjugate transformation under an invertible affine change
type: theorem
caption: "Tracks inverse-transpose coordinates, translations and linear terms in a transformed convex conjugate."
---

# Conjugate transformation under an invertible affine change

Let \(\rho:\mathbb R^n\to(-\infty,+\infty]\) be convex, \(A\in\mathbb R^{n\times n}\) invertible, \(a,c\in\mathbb R^n\), and \(b\in\mathbb R\). For
\[
f(x)=\rho(A(x-c))+a^Tx+b,
\]
its conjugate is
\[
f^*(y)=\rho^*(A^{-T}(y-a))+c^T(y-a)-b.
\]
To derive it, substitute \(z=A(x-c)\), so \(x=A^{-1}z+c\). Then
\[
y^Tx-f(x)=\langle A^{-T}(y-a),z\rangle-\rho(z)+c^T(y-a)-b.
\]
Invertibility makes this a supremum over all \(z\in\mathbb R^n\), giving the formula. The transpose comes from moving the inverse across the inner product. The translation pairs with \(y-a\), not just \(y\), and the scalar constant is subtracted. For a noninvertible \(A\), this substitution does not range freely over every \(z\), so the formula cannot be used without a different argument.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `Introduction and general information/Booklet of Exercises FDA.pdf`, Exercise 5.1.8, p. 65; change-of-variables solution, p. 76.
- `8. Juli - 14. Juli/Exercise Sheet 12.pdf` and `15. Juli - 21. Juli/Solution Sheet 12.pdf` (single physical solution page), Homework 12.3, p. 2; corresponding solution, invertible substitution.
