---
id: tum-fa-sobolev-spaces
source: tum-functional-analysis
parent: fa-sobolev-distributions
title: Sobolev spaces as closed derivative graphs in product spaces
type: concept
caption: "Constructs complete weak-derivative spaces as closed product-space subspaces and derives reflexivity, separability and Hilbert special cases."
---

# Sobolev spaces as closed derivative graphs in product spaces

## Definition and norms

On an open \(\Omega\subset\mathbb R^d\),
\[
W^{k,p}(\Omega)=\{u\in L^p(\Omega):\partial^\alpha u\in L^p(\Omega),\ |\alpha|\le k\},
\]
where derivatives are weak derivatives tested against \(C_c^\infty(\Omega)\), not pointwise derivatives. For \(p<\infty\),
\[
\|u\|_{W^{k,p}}=\left(\sum_{|\alpha|\le k}\|\partial^\alpha u\|_p^p\right)^{1/p}.
\]
For \(p=\infty\), the main notes use the sum of derivative sup norms, whereas the supplement uses their maximum. These are equivalent norms because only finitely many multi-indices occur. In particular \(W^{0,p}=L^p\).

## Completeness and inherited structure

For a Sobolev-Cauchy sequence, each \(\partial^\alpha u_n\) is Cauchy in \(L^p\), with limit \(u_\alpha\); let \(u=u_0\). Passing to the limit against a fixed compactly supported smooth test gives
\[
\int u_\alpha\varphi=(-1)^{|\alpha|}\int u\,\partial^\alpha\varphi.
\]
Thus the limiting components remain derivatives of the same function: \(u_\alpha=\partial^\alpha u\). This proves completeness, including \(p=\infty\) using the corresponding \(L^1\) bounds on tests.

The derivative map
\[
T:u\mapsto(\partial^\alpha u)_{|\alpha|\le k}
\quad\text{into}\quad\prod_{|\alpha|\le k}L^p(\Omega)
\]
is an isometry for the matching product norm and has closed image. Consequently \(W^{k,p}\) is reflexive for \(1<p<\infty\), and separable for \(1\le p<\infty\), by the corresponding product-space and closed-subspace results. Reflexivity at \(p=1\) or \(\infty\) is not asserted.

## Hilbert and zero-boundary subspaces

For finite \(p\), define
\[
W^{k,p}_0(\Omega)=\overline{C_c^\infty(\Omega)}^{\,W^{k,p}}.
\]
It is a closed Banach subspace. Its zero-boundary interpretation is through this closure; pointwise boundary values of arbitrary a.e. equivalence classes are not part of the definition.

Write \(H^k=W^{k,2}\) and \(H^k_0=W^{k,2}_0\). They are Hilbert spaces for
\[
\langle u,v\rangle_{H^k}=\sum_{|\alpha|\le k}\int_\Omega
\partial^\alpha u\,\overline{\partial^\alpha v}.
\]
The norm records regularity of the function and its derivatives simultaneously; it is stronger than merely measuring \(u\) in \(L^p\).

## Source references

Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`.
- `Materials/Lecture notes.pdf` (WS 2017/18), Definitions 7.1–7.2, Proposition 7.3, Lemma 7.4, pp. 60–62; Definitions 7.7–7.8 and Proposition 7.9, p. 63.
- `Materials/Distributions.pdf` (WS 2024/25), Section 8, Definition 6 and Propositions 1–2, pp. 9–10.
