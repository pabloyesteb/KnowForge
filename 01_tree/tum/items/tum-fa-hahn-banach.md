---
id: tum-fa-hahn-banach
source: tum-functional-analysis
parent: fa-fundamental-principles
title: Hahn–Banach extension and norming functionals
type: theorem
caption: "Extends dominated linear functionals without increasing their norm and derives norming functionals and minimal-extension properties."
---

# Hahn–Banach extension and norming functionals

## Dominated extension

On a real vector space \(X\), let \(p:X\to\mathbb R\) be sublinear: positively homogeneous for nonnegative scalars and subadditive. If a linear \(f:U\to\mathbb R\) on a subspace satisfies \(f\le p\), it extends linearly to \(F:X\to\mathbb R\) with \(F\le p\).

For a one-dimensional enlargement \(U+\mathbb Ry\), define \(F(u+ty)=f(u)+tr\). A permissible \(r\) exists because
\[
\sup_{u\in U}[f(u)-p(u-y)]
\le\inf_{u\in U}[p(u+y)-f(u)].
\]
The inequality follows by applying domination and subadditivity to two vectors in \(U\). Partially order dominated extensions by restriction; a chain has the union extension as upper bound. Zorn's lemma gives a maximal extension, and the one-step construction forces its domain to be all of \(X\).

## Norm-preserving form

For any real or complex normed space \(X\), any linear subspace \(U\) and \(f\in U^*\), there exists \(F\in X^*\) with
\[
F|_U=f,\qquad\|F\|=\|f\|.
\]
Neither completeness nor density nor closedness of \(U\) is required. Over \(\mathbb R\), take \(p(x)=\|f\|\|x\|\), and apply domination to \(x,-x\). Over \(\mathbb C\), extend \(g=\operatorname{Re}f\) as a real functional, then set \(F(x)=g(x)-ig(ix)\). Rotation by a unit scalar turns \(F(x)\) into its absolute value and proves the norm bound.

Every nonzero \(x\in X\) admits a norm-one functional \(F\) with \(F(x)=\|x\|\), by extending from its span. Hence
\[
\|x\|=\max_{\|F\|\le1}|F(x)|.
\]
For a closed subspace \(U\) and \(x\notin U\), apply a norming functional on \(X/U\) to obtain \(F|_U=0\), \(F(x)\ne0\). In particular \(U\) is dense exactly when the only continuous functional vanishing on \(U\) is zero.

## Minimal extensions and uniqueness

Restriction gives \(\|F\|\ge\|f\|\); Hahn–Banach attains this lower bound:
\(\|f\|=\min_{F|_U=f}\|F\|\). The norm-preserving extensions form a convex set, because convex combinations still restrict to \(f\), have norm at most \(\|f\|\), and cannot have smaller norm. If \(X^*\) is strictly convex, this extension is unique: two different normalized extensions would have midpoint norm strictly less than 1, contradicting the lower bound. Strict convexity is a substantive extra condition; Hahn–Banach alone gives no uniqueness.

## Source references
Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`. N = `Materials/Lecture notes.pdf` (WS 2017/18); E/S refer to `Problem sheets/Problem Sheet <n>.pdf` and `Solutions to problem sheets/Solutions Sheet <n>.pdf` (WS 2024/25).
- N, Proposition 4.4 and Hahn–Banach Proposition 4.5, pp. 37–39; Corollaries 4.6–4.8, pp. 39–40.
- E6/S6, T6.1–T6.2; E7/S7, T7.1; E8/S8, T8.1(a).
