---
id: tum-fda-mutual-independence
source: tum-foundations-data-analysis
parent: fda-probability
title: Pairwise and mutual independence of events and variables
type: concept
caption: "Requires factorization over every finite subfamily and explains when density and transformed-expectation products are valid."
---

# Pairwise and mutual independence of events and variables

Two events are independent when \(\mathbb P(A\cap B)=\mathbb P(A)\mathbb P(B)\). A family \(A_1,\ldots,A_N\) is mutually independent when the analogous product identity holds for every subfamily of distinct indices. Checking pairs alone is insufficient. The review's unit-square regions have individual probabilities \(1/2\), pair intersections \(1/4\), and triple intersection \(1/4\), whereas mutual independence would require \(1/8\).

Variables \(X,Y\) are independent when, for every pair of measurable value sets \(C,D\),
\[
\mathbb P(X\in C,Y\in D)=\mathbb P(X\in C)\mathbb P(Y\in D).
\]
The joint event is \(\{(X,Y)\in C\times D\}\). Marginal laws alone do not determine a general joint law. When both variables have densities, independence corresponds to \(\varphi_{X,Y}(x,y)=\varphi_X(x)\varphi_Y(y)\) almost everywhere.

Measurable transforms of separate independent variables remain independent, so integrable transformed products factor as \(\mathbb E[f(X)g(Y)]=\mathbb Ef(X)\mathbb Eg(Y)\). This does not justify factoring arbitrary functions that each depend on both variables, such as \(\cos(X+Y)\) and \(Y\). Nor may a nontrivial variable be treated as independent of itself: self-independence would require every one of its event probabilities \(p\) to satisfy \(p=p^2\). Degenerate almost-surely constant variables are the exception to the review's blanket warning.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `10. Juni - 16. Juni/All you... math 8`, single physical page, “Independence in Probability”, pairwise-versus-triple region example, “Definition B”, variable independence, joint densities and transformed expectations.
