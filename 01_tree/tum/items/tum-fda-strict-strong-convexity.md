---
id: tum-fda-strict-strong-convexity
source: tum-foundations-data-analysis
parent: fda-convex-optimization
title: Strict convexity, uniqueness and quantitative strong convexity
type: concept
caption: "Separates strict segment inequalities from uniform quadratic curvature and states their consequences under appropriate smoothness."
---

# Strict convexity, uniqueness and quantitative strong convexity

Strict convexity requires a strict chord inequality for distinct \(x,y\) and \(0<\lambda<1\). It permits at most one minimizer on a convex domain: two distinct minimizers would have a midpoint with smaller value. This is a uniqueness assertion conditional on existence, not an attainment theorem. For differentiable strictly convex functions on \(\mathbb R^n\), the gradient is injective, as stated in the review.

Strong convexity with parameter \(m>0\) strengthens the chord bound to
\[
f(\lambda x+(1-\lambda)y)\le\lambda f(x)+(1-\lambda)f(y)
-\tfrac m2\lambda(1-\lambda)\|x-y\|_2^2.
\]
It implies strict convexity by a uniform quadratic margin. If \(f\) is differentiable, the equivalent supporting inequality is
\[
f(x)\ge f(y)+\nabla f(y)^T(x-y)+\tfrac m2\|x-y\|_2^2.
\]
The factor \(m\) quantifies curvature; setting \(m=0\) recovers ordinary convexity rather than strict convexity. A strictly convex function can have curvature weakening toward zero, so strictness alone is not the same as one positive uniform strong-convexity constant. The gradient statement requires differentiability even though strict convexity itself does not.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `1. Juli - 7. Juli/All you... math 11`, single physical page, strict definition, uniqueness and injective-gradient propositions, strong-convexity definition and differentiable supporting inequality.
