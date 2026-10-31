---
id: tum-fa-compact-operators
source: tum-functional-analysis
parent: fa-compact-fredholm
title: Compact operators, weak-to-strong continuity and norm approximation
type: theorem
---

# Compact operators, weak-to-strong continuity and norm approximation

## Equivalent criteria and weak inputs

A linear map \(T:X\to Y\) between Banach spaces is compact if the image of the closed unit ball has compact closure. Equivalently, every bounded set has relatively compact image, or every bounded sequence has an image subsequence converging in norm. In the sequential criterion, points in the closure of the image can be approximated by actual image points with errors \(1/n\). Compact operators are bounded because relatively compact sets are bounded.

If \(x_n\rightharpoonup x\), then \(Tx_n\to Tx\) **in norm**. The inputs are bounded. Every image subsequence has a norm-convergent further subsequence; testing any such limit with \(y^*\in Y^*\) gives \(y^*(Tx)\), because \(y^*T\in X^*\). Dual separation identifies every cluster limit as \(Tx\); a subsequence staying away from \(Tx\) would contradict compactness. No weakly convergent subsequence of every bounded input sequence is presumed.

## Stability and finite-rank approximation

Compact operators form a linear, operator-norm closed subspace \(\mathcal K(X;Y)\). For \(T_m\to T\) and bounded \(x_n\), diagonal extraction makes each \(T_mx_{n_k}\) converge. Then
\[
\|Tx_{n_k}-Tx_{n_j}\|
\le2C\|T-T_m\|+\|T_mx_{n_k}-T_mx_{n_j}\|
\]
makes the selected image Cauchy; completeness of \(Y\) supplies its limit. Composing a compact map on either side with a compatible bounded map preserves compactness. Finite-rank bounded maps are compact, so their operator-norm limits are compact. The reverse approximation assertion is false for arbitrary Banach spaces; the notes cite Enflo's counterexample, without constructing it.

A surjective compact map between Banach spaces must have finite-dimensional target. Open mapping puts a target ball inside its relatively compact unit-ball image; an infinite-dimensional normed space cannot have a compact closed ball.

## Explicit tests

- On \(\ell^p\), \(1\le p<\infty\), \((D_ax)_n=a_nx_n\) for \(a\in\ell^\infty\) is compact iff \(a\in c_0\). Truncation has error \(\|D_a-D_{a^{(N)}}\|=\sup_{n>N}|a_n|\). If coefficients stay away from zero on a subsequence, its images of coordinate vectors stay separated.
- The inclusion \(\ell^1_g\hookrightarrow\ell^1\), \(\|x\|_g=\sum n|x_n|\), is compact: factor through the isometry \(x\mapsto(nx_n)\) and compact diagonal multiplication by \(1/n\).
- The unilateral right shift on \(\ell^p\) is not compact: coordinate-vector images have no norm-convergent subsequence.
- More generally, an isometry on a Banach space is compact iff the space is finite-dimensional: it preserves the unit-ball distances, so relative compactness of its image would make the original closed unit ball compact.
- \(C^1([0,1])\hookrightarrow C([0,1])\), with the derivative-inclusive domain norm, is compact by uniform boundedness and equicontinuity of the image ball. Rellich similarly gives compact Sobolev-to-\(L^p\) inclusions under its domain hypotheses.

## Source references

Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`.
- `Materials/Lecture notes.pdf` (WS 2017/18), Chapter 8, Definition 8.1, Lemma 8.2, Proposition 8.3, Lemma 8.7, Proposition 8.8 and Corollary 8.9, pp. 66–69.
- `Problem sheets/Problem Sheet 10.pdf` and `Solutions to problem sheets/Solutions Sheet 10.pdf` (WS 2024/25), T10.1–T10.2 and A10.1.
- `Mock Exam/Mock Exam.pdf` and `Mock Exam/Solutions to Mock Exam.pdf`, P.1(d).
