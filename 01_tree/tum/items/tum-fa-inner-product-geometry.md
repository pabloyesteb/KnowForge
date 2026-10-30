---
id: tum-fa-inner-product-geometry
source: tum-functional-analysis
parent: fa-hilbert-spaces
title: Inner-product geometry and Hilbert norms
type: concept
---

# Inner-product geometry and Hilbert norms

## Scalar convention and completeness

An inner product on a real or complex vector space is positive definite, conjugate symmetric and linear in the **first** argument. Thus
\[
\langle x,\alpha y+\beta z\rangle
=\overline\alpha\langle x,y\rangle+\overline\beta\langle x,z\rangle,\qquad
\|x\|=\sqrt{\langle x,x\rangle}.
\]
An inner-product space is pre-Hilbert; it is Hilbert when complete for this norm. Examples are \(\mathbb K^n\), \(\ell^2\), and Lebesgue \(L^2(D)\), with products \(\sum x_k\overline y_k\) or \(\int x\overline y\). Hölder ensures the infinite products are well-defined. Incompleteness of continuous functions under the \(L^2\) norm is a separate completeness example in [Normed spaces](tum-fa-banach-spaces.md).

## Cauchy–Schwarz and recovery of the product

For \(y\ne0\), nonnegativity of
\(\|x-\langle x,y\rangle y/\|y\|^2\|^2\) proves
\[
|\langle x,y\rangle|\le\|x\|\|y\|.
\]
The triangle inequality follows by expanding \(\|x+y\|^2\). Cauchy–Schwarz also gives continuity of the product in both arguments. Orthogonality implies Pythagoras.

Every inner-product norm satisfies
\[
\|x+y\|^2+\|x-y\|^2=2\|x\|^2+2\|y\|^2.
\]
Conversely the parallelogram identity characterizes norms induced by an inner product. The product is recovered by polarization:
\[
\langle x,y\rangle=\tfrac14(\|x+y\|^2-\|x-y\|^2)
\]
over \(\mathbb R\), with the additional term
\(i(\|x+iy\|^2-\|x-iy\|^2)/4\) over \(\mathbb C\).

For a linear \(T\) on a Hilbert space, preservation of norms is equivalent to preservation of inner products, by polarization. Surjectivity is not part of this equivalence.

## Why exponent two is special

For distinct coordinate vectors in \(\ell^p\), \(1\le p<\infty\), the left side of the parallelogram identity is \(2^{1+2/p}\), while its right side is 4. Equality holds only for \(p=2\); for \(p=\infty\), the left side is 2. Hence these given norms are not inner-product norms for \(p\ne2\). Normalized functions supported on two disjoint sets of finite positive measure give the same obstruction in Lebesgue \(L^p(\Omega)\) for a Borel \(\Omega\subset\mathbb R^n\) of positive measure.

## Source references
Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`. Lecture notes are WS 2017/18; exercise/solution sheets are WS 2024/25.

- `Materials/Lecture notes.pdf`, Definition 2.1 and Propositions 2.2–2.3, pp. 20–22. The converse parallelogram characterization is stated there without proof.
- `Problem sheets/Problem Sheet 4.pdf` and `Solutions to problem sheets/Solutions Sheet 4.pdf`, A4.1.
- `Problem sheets/Problem Sheet 5.pdf` and `Solutions to problem sheets/Solutions Sheet 5.pdf`, T5.1.
