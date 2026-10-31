---
id: tum-fa-open-mapping
source: tum-functional-analysis
parent: fa-fundamental-principles
title: Open mapping and the bounded inverse theorem
type: theorem
caption: "Proves openness of bounded Banach-space surjections and obtains bounded inverses and consequences for complete norms."
---

# Open mapping and the bounded inverse theorem

## Quantitative openness

For Banach spaces \(X,Y\) and bounded linear \(T:X\to Y\), these are equivalent:
- \(T\) maps every open subset of \(X\) to an open subset of \(Y\);
- some \(\delta>0\) satisfies \(B_Y(0,\delta)\subset T(B_X(0,1))\);
- \(T\) is surjective.

The ball inclusion scales by linearity and transfers to balls around every preimage. Conversely, surjectivity gives
\(Y=\bigcup_{n\ge1}\overline{T(B_X(0,n))}\). Baire supplies a closure with nonempty interior; symmetry and convexity then give a ball around zero in that closure.

To remove the closure, choose approximate preimages successively, halving residuals. In the notes' normalization, take \(x_j\in B_X(0,k)\) and \(y_{j+1}=2(y_j-Tx_j)\in B_Y(0,\varepsilon)\). Then
\[
T\sum_{j=0}^m2^{-j}x_j=y_0-2^{-(m+1)}y_{m+1}\to y_0.
\]
The preimage series converges in \(X\), with norm at most \(2k<3k\). Thus \(B_Y(0,\varepsilon)\subset T(B_X(0,3k))\). Completeness is used both in Baire on \(Y\) and in summing preimage corrections in \(X\).

## Consequences and limitations

A bounded linear bijection between Banach spaces has bounded inverse, since images of open sets become inverse preimages of open sets. Consequently two complete norms on one vector space are equivalent if one globally bounds the other. The non-equivalent sup and \(L^1\) norms on \(C([a,b])\), \(a<b\), therefore cannot both be complete.

Openness concerns images of open sets, not images of closed sets. The diagonal bounded bijection on incomplete \(c_e\) in [normed isomorphisms](tum-fa-normed-isomorphisms.md) shows why completeness matters.

The notes also state a stability consequence: if \(T(X)\) is dense in \(Y\) but not all of \(Y\), some \(y\in Y\) has the property that every sequence \(Tx_n\to y\) satisfies \(\|x_n\|\to\infty\). This is an asserted corollary, with proof assigned as an exercise, rather than a derived error bound for arbitrary inverse problems.

## Source references
Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`. N = `Materials/Lecture notes.pdf` (WS 2017/18); E/S refer to `Problem sheets/Problem Sheet <n>.pdf` and `Solutions to problem sheets/Solutions Sheet <n>.pdf` (WS 2024/25).
- N, Definition 3.6, Proposition 3.7 and Corollaries 3.8–3.9, pp. 34–36.
- E5/S5, T5.4.
