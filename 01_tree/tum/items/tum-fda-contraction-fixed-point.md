---
id: tum-fda-contraction-fixed-point
source: tum-foundations-data-analysis
parent: fda-linear-geometry
title: Unique fixed points of contractions on complete metric spaces
type: theorem
caption: "States the fixed-point guarantee for a contraction and identifies completeness and a uniform factor below one as essential assumptions."
---

# Unique fixed points of contractions on complete metric spaces

Let \((X,d)\) be a nonempty complete metric space and \(F:X\to X\) satisfy
\[
d(F(x),F(y))\le Ld(x,y)\quad\text{for all }x,y\in X,\qquad 0\le L<1.
\]
Then \(F\) has exactly one fixed point \(x^*\in X\), with \(F(x^*)=x^*\). The review states this theorem as an application of completeness.

The contraction condition uses one constant for every pair of points, and the map must preserve the underlying space. Uniqueness follows immediately: two fixed points would satisfy \(d(x^*,y^*)\le Ld(x^*,y^*)\), forcing their distance to be zero. Completeness supplies the existence part of the theorem; mere metric structure does not provide that guarantee.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `22. April - 28. April/All you ... math 1`, single physical page, “Recap Distances and Complete Spaces”, “Important Application: Contractions” through the fixed-point theorem.
