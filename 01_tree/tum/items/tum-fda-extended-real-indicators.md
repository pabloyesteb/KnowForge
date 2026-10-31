---
id: tum-fda-extended-real-indicators
source: tum-foundations-data-analysis
parent: fda-convex-optimization
title: Extended-real indicators and constrained subgradient geometry
type: concept
caption: "Encodes constraints by zero/infinity indicators and derives the interval endpoint subdifferentials from supporting slopes."
---

# Extended-real indicators and constrained subgradient geometry

Encode a constraint \(x\in C\) by the extended-real indicator
\[
\delta_C(x)=\begin{cases}0&x\in C,\\+\infty&x\notin C.\end{cases}
\]
Then minimizing \(f\) over \(C\) is equivalent to minimizing \(f+\delta_C\) over the ambient space. This is a zero/infinity optimization indicator, distinct from the zero/one indicator used in probability.

The function is convex exactly when \(C\) is convex: combinations of feasible points have zero right-hand side, while a positive-weight infeasible endpoint makes the inequality automatic. It is lower semicontinuous exactly when \(C\) is closed. For a closed \(C\), an exterior point has an open neighborhood outside \(C\), so nearby indicator values are eventually infinite; at an interior or boundary feasible point all values are at least its value zero. Conversely, a missing limit point of \(C\) violates the liminf condition.

A convex subgradient \(g\in\partial f(x)\), at a point of finite value, means \(f(z)\ge f(x)+g^T(z-x)\) for every \(z\). For the indicator at a feasible point this becomes the normal condition \(g^T(z-x)\le0\) for every \(z\in C\). For a nondegenerate closed interval \(C=[a,b]\),
\[
\partial\delta_C(x)=\begin{cases}
\{0\}&a<x<b,\\(-\infty,0]&x=a,\\[0,+\infty)&x=b,\\\varnothing&x\notin[a,b].
\end{cases}
\]
At the left endpoint a nonpositive slope supports the epigraph; at the right endpoint a nonnegative slope does so. Exterior points are outside the finite domain and have no subgradients. This illustrates how extended-real constraints and supporting-plane geometry fit the same convex optimality framework.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `8. Juli - 14. Juli/All you ... math 12`, single physical page, “Characteristic Functions”, constrained reformulation, closedness/convexity, interval example and endpoint subdifferentials through end.
- `8. Juli - 14. Juli/Solution Sheet 11.pdf`, single physical page, Exercise 11.2(b1), supporting-subgradient definition and diagrams.
