---
id: tum-fda-singular-value-perturbation
source: tum-foundations-data-analysis
parent: fda-svd
title: Spectral-norm perturbation bound for singular values
type: theorem
caption: "Bounds each ordered singular-value change by the perturbation size and separates scalar-value control from vector sensitivity."
---

# Spectral-norm perturbation bound for singular values

For same-shaped real matrices \(A\) and \(A+E\), ordered singular values satisfy
\[
|\sigma_i(A+E)-\sigma_i(A)|\le\|E\|_2.
\]
The solution and review present this as a perturbation bound, calling it “Wedin's Bound”; they do not develop a general singular-subspace perturbation proof.

Each perturbed value therefore remains in \([\max(0,\sigma_i-\eta),\sigma_i+\eta]\) when \(\|E\|_2\le\eta\). If adjacent uncertainty intervals are disjoint, their value clusters remain separated. For the source's values \(10,8,5,4\) and \(\eta=0.3\), the intervals are respectively \([9.7,10.3]\), \([7.7,8.3]\), \([4.7,5.3]\) and \([3.7,4.3]\).

The scalar inequality does not itself bound the distance between individual singular vectors. The source contrasts separated values with a cluster such as \(1.1,1.0\), whose uncertainty intervals overlap at that perturbation size: directions within the cluster may change substantially. Choosing a truncation boundary outside such a cluster is conceptually different from selecting one of its individual directions. No numerical vector-angle estimate is supplied by this inequality alone.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `3. Juni - 9. Juni/Solution Sheet 6.pdf`, single physical page, Exercise 6.1(c), “Well-separated. Wedin's Bound”, value intervals and separation relative to perturbation magnitude.
- `3. Juni - 9. Juni/All you ... math 7`, single physical page, “Remark on Wedin's Bound”, scalar-value control and separated/clustered examples.
