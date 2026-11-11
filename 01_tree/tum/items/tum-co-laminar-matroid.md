---
id: tum-co-laminar-matroid
source: tum-combinatorial-optimization
parent: co-trees-matroids
title: Laminar capacity constraints define a matroid
type: theorem
caption: "Proves augmentation by counting disjoint maximal tight sets in a nested family."
---

# Laminar capacity constraints define a matroid

A family \(\mathcal L\) of ground-set subsets is laminar if any two are disjoint or nested. For nonnegative integer quotas \(k(X)\), declare \(I\) independent when \(|I\cap X|\le k(X)\) for every \(X\in\mathcal L\). The empty set is feasible and feasibility is hereditary. This generalizes partition quotas to nested quotas.

For augmentation take independent \(I,J\) with \(|I|<|J|\). If no \(e\in J\setminus I\) can be added to \(I\), each such element lies in a quota set tight for \(I\). Inclusion-maximal tight sets are disjoint by laminarity and cover \(J\setminus I\). On each such set, independence gives \(|J\cap X|\le k(X)=|I\cap X|\). Outside their union, \(J\) has no element not already in \(I\). Summing yields \(|J|\le|I|\), a contradiction. Thus augmentation holds.

The submission assumes increasing quotas on nested sets and argues using maximal tight sets and base cardinalities. Monotone quotas are not needed for the direct exchange proof. Its assertion that equal-sized maximal independent sets alone prove a matroid also needs the same condition on every restriction; direct augmentation supplies the missing justification.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Student Submitted Exercises/Alexander Brovko.pdf`, pp. 1–3, laminar definition, quota model, annotated tight-set counting proof and conclusion.
