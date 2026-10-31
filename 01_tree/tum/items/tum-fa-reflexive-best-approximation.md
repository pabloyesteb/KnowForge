---
id: tum-fa-reflexive-best-approximation
source: tum-functional-analysis
parent: fa-weak-compactness
title: Best approximation via reflexivity and strict convexity
type: theorem
---

# Best approximation via reflexivity and strict convexity

## Existence by weak limits

Let \(X\) be a reflexive Banach space, \(K\subset X\) nonempty, norm-closed and convex, and \(x\in X\). Then the distance from \(x\) to \(K\) is attained.

Take a minimizing sequence \(y_n\in K\). Since
\(\|y_n\|\le\|x-y_n\|+\|x\|\), it is bounded and has a weakly convergent subsequence \(y_{n_k}\rightharpoonup y\). Weak sequential closedness gives \(y\in K\). Weak lower semicontinuity gives
\[
\|x-y\|\le\liminf_k\|x-y_{n_k}\|
=\inf_{z\in K}\|x-z\|.
\]
This is a direct-method argument: boundedness supplies weak subsequences, convex closedness preserves feasibility, and lower semicontinuity preserves the infimum. It establishes existence, not a numerical procedure or an orthogonal projection formula in a general Banach space.

## Uniqueness is a separate hypothesis

A norm is strictly convex if distinct unit vectors have midpoint norm less than 1. In a strictly convex normed space, approximation to a convex set has at most one minimizer. If \(y,\tilde y\) were distinct minimizers at distance \(d>0\), apply strict convexity to \((x-y)/d\) and \((x-\tilde y)/d\): their midpoint corresponds to a feasible point strictly closer to \(x\).

Thus reflexivity/completeness and closedness guarantee existence here, while strict convexity guarantees uniqueness. They should not be collapsed into one hypothesis. For \(\ell^p\) and Lebesgue \(L^p\), \(1<p<\infty\), both conditions hold; each nonempty closed convex set has a unique best approximation. The notes state the converse characterization by unique solvability for all such sets without proof.

## Source references
Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`. N = `Materials/Lecture notes.pdf` (WS 2017/18); E/S refer to `Problem sheets/Problem Sheet <n>.pdf` and `Solutions to problem sheets/Solutions Sheet <n>.pdf` (WS 2024/25).
- N, Proposition 6.14, Definition 6.15, Proposition 6.16 and discussion, pp. 57–58.
