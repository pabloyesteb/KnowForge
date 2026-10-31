---
id: tum-fda-convex-function-epigraph
source: tum-foundations-data-analysis
parent: fda-convex-optimization
title: Convex functions and convex epigraphs
type: concept
caption: "Interprets Jensen’s two-point inequality as epigraph convexity and explains the role of affine segments."
---

# Convex functions and convex epigraphs

On a convex domain \(D\), a function is convex if
\[
f(\lambda x+(1-\lambda)y)\le\lambda f(x)+(1-\lambda)f(y)
\quad(x,y\in D,\ 0\le\lambda\le1).
\]
Its graph lies below each chord. This is equivalent to convexity of \(\operatorname{epi}f\): a convex combination of points above the graph remains above it, and conversely apply epigraph convexity to \((x,f(x))\) and \((y,f(y))\).

Affine behavior on a segment produces equality along that segment and can allow several minimizers. Convexity therefore does not assert strict curvature or uniqueness. A flat minimum region remains compatible with the definition. The epigraph description distinguishes convexity of a function from the earlier convexity of its input domain, and from closedness of the epigraph.

The same definition extends to functions with values in \((-\infty,+\infty]\), using the effective domain of finite values. The epigraph equivalence still holds: pairs with finite height only involve finite function values; endpoints with infinite objective make the corresponding interior-weight convex inequality automatic. This avoids trying to place \((x,+\infty)\) inside the finite-coordinate epigraph.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `1. Juli - 7. Juli/All you... math 11`, single physical page, “Convexity, Strict Convexity, Strong Convexity”, set/function definitions, epigraph equivalence and affine/flat-minimum diagrams.
- `Introduction and general information/Booklet of Exercises FDA.pdf`, Exercise 5.1.1(2), p. 62; epigraph argument, pp. 66–67, interpreted for the stated extended-real codomain.
- `24. Juni - 30. Juni/Exercise sheet 10.pdf`, Exercise 10.1(b), p. 1.
- `1. Juli - 7. Juli/Solution sheet 10.pdf`, single physical page, Exercise 10.1(b), full argument and illustrations.
