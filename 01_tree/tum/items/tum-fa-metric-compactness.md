---
id: tum-fa-metric-compactness
source: tum-functional-analysis
parent: fa-weak-compactness
title: Metric compactness, finite nets and tail control
type: theorem
caption: "Uses finite nets and uniform tail bounds to prove compactness and constructs bounded function sequences without norm-convergent subsequences."
---

# Metric compactness, finite nets and tail control

## Compactness through finite approximations

In metric spaces, open-cover compactness is equivalent to sequential compactness. A compact subset of a normed space is closed and bounded, but that converse holds for all closed bounded sets only in finite dimension.

For a closed subset \(F\) of a complete metric space, compactness is equivalent to total boundedness: for every \(\varepsilon>0\), finitely many balls of radius \(\varepsilon\), centered in \(F\), cover it. Failure of a finite net permits recursive selection of points at pairwise distances at least \(\varepsilon\), contradicting sequential compactness. Conversely, successive finite covers of radii \(2^{-n}\) let one select a nested subsequence with arbitrarily small diameter; a diagonal choice is Cauchy. Completeness and closedness supply a limit in \(F\).

Total boundedness, unlike mere boundedness, controls the number of approximating points at every accuracy.

## A compact infinite-dimensional box

The subset
\[
C=\{x\in\ell^2(\mathbb R):|x_k|\le1/k\}
\]
is compact. Coordinate continuity makes it closed. Uniform tail control gives
\(\sup_{x\in C}\sum_{k>N}|x_k|^2\le\sum_{k>N}k^{-2}\to0\).
For a fixed accuracy, truncate far enough, cover the resulting finite-dimensional box by a finite net, and combine head and tail errors. This produces a finite net for \(C\). It illustrates compactness of particular subsets without compactness of the ambient unit ball.

## Bounded but noncompact sequences

The triangular functions \(f_n(t)=\max(0,1-nt)\) have norm 1 in \(C([0,1])\) with the sup norm and in \(L^\infty\), but tend to zero almost everywhere. A norm-convergent subsequence would have zero as its almost-everywhere limit, contradicting the norms. In \(L^p\), \(1\le p<\infty\), normalize these functions by their \(L^p\) norms: they again have norm 1 and tend to zero almost everywhere, precluding any norm-convergent subsequence.

## Source references
Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`. N = `Materials/Lecture notes.pdf` (WS 2017/18); E/S refer to `Problem sheets/Problem Sheet <n>.pdf` and `Solutions to problem sheets/Solutions Sheet <n>.pdf` (WS 2024/25).
- N, Propositions 5.1–5.2, p. 46 (metric equivalence stated without proof).
- E9/S9, T9.1–T9.3 (finite-net proof, counterexamples and the sequence-space box).
