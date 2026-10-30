---
id: tum-fa-normed-isomorphisms
source: tum-functional-analysis
parent: fa-normed-spaces
title: Norm equivalence and isomorphisms of normed spaces
type: concept
---

# Norm equivalence and isomorphisms of normed spaces

An isomorphism is linear, bijective, bounded and has bounded inverse. Two norms on the same vector space are equivalent when each bounds the other up to a constant. Equal-dimensional finite-dimensional normed spaces are isomorphic; their linear maps into any normed space are continuous. Matrix operator norms depend on the chosen domain/range norms. Infinite-dimensional spaces can be isomorphic to proper subspaces: for \(x\in c\), set
\[
(Tx)_1=\lim_jx_j,\qquad (Tx)_k=x_{k-1}-\lim_jx_j\quad(k\ge2).
\]
This maps \(c\) onto \(c_0\), with inverse \((Sy)_k=y_{k+1}+y_1\); both norms are bounded by 2.


## A bounded bijection need not have bounded inverse

On \(c_e\) with the supremum norm, \(Tx=(x_n/n)_n\) is bounded and bijective; its inverse \(Sx=(nx_n)_n\) still maps finite sequences to finite sequences but is unbounded since \(\|Se_n\|_\infty=n\). The image of the open unit ball under \(T\) contains zero but not \(T(e_n)=e_n/n\), which tends to zero; thus that image is not open. Completeness cannot be omitted from the bounded-inverse/open-mapping conclusions.

## Source references
Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`. Lecture notes are WS 2017/18; exercise/solution sheets are WS 2024/25.
- `Materials/Lecture notes.pdf`, Definition 1.5 and Proposition 1.6, pp. 7–8.
- `Problem sheets/Problem Sheet 5.pdf` and `Solutions to problem sheets/Solutions Sheet 5.pdf`, T5.4.
