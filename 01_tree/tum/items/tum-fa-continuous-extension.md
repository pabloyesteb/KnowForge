---
id: tum-fa-continuous-extension
source: tum-functional-analysis
parent: fa-normed-spaces
title: Continuous extension of bounded operators from dense subspaces
type: theorem
caption: "Extends bounded linear maps uniquely from dense subspaces into Banach codomains while preserving the operator norm."
---

# Continuous extension of bounded operators from dense subspaces

## Extension from a dense subspace

Let \(X\) be normed, \(Y\) Banach, \(U\subset X\) a dense linear subspace, and \(S:U\to Y\) bounded linear. There is a unique bounded linear extension \(T:X\to Y\), with \(\|T\|=\|S\|\).

For \(u_n\to x\), set \(Tx=\lim Su_n\). Boundedness makes \(Su_n\) Cauchy; completeness of \(Y\) supplies its limit, and the same bound proves independence from the approximating sequence. Density proves uniqueness and equality of norms. Completeness of the **codomain**, not necessarily \(X\), is required. This is not Hahn–Banach extension from an arbitrary subspace.


For scalar-valued maps this shows that restriction from \(X^*\) to \(U^*\) is an isometric isomorphism whenever \(U\) is dense in normed \(X\). Injectivity follows from density and continuity; extension gives surjectivity and equality of norms. No completeness of \(U\) or \(X\) is needed because the scalar field is complete.

## Source references
Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`. Lecture notes are WS 2017/18; exercise/solution sheets are WS 2024/25.
- `Materials/Lecture notes.pdf`, Proposition 1.19, p. 15.
- `Mock Exam/Mock Exam.pdf` and `Mock Exam/Solutions to Mock Exam.pdf`, P.4.
