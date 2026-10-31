---
id: tum-fda-alternating-projections
source: tum-foundations-data-analysis
parent: fda-linear-geometry
title: Alternating projections onto intersecting closed convex sets
type: algorithm
caption: "Proves finite-dimensional convergence using projection inequalities and relates the line case to the angle between directions."
---

# Alternating projections onto intersecting closed convex sets

Let \(C,D\subset\mathbb R^d\) be nonempty closed convex sets with nonempty intersection. Starting at \(x_0\in C\), iterate
\[
y_k=P_Dx_k,\qquad x_{k+1}=P_Cy_k.
\]
Both sequences converge to a common point of \(C\cap D\).

The projection variational inequality gives, for \(c\in C\),
\[
\|x-P_Cx\|_2^2\le\|x-c\|_2^2-\|P_Cx-c\|_2^2.
\]
Apply it to both half steps with any \(z\in C\cap D\):
\[
\|y_k-z\|^2\le\|x_k-z\|^2-\|y_k-x_k\|^2,\qquad
\|x_{k+1}-z\|^2\le\|y_k-z\|^2-\|x_{k+1}-y_k\|^2.
\]
Distances to \(z\) decrease, hence the iterates are bounded. Telescoping the inequalities shows that the sum of squared half-step gaps is finite, so both gaps tend to zero. This argument does not require those gaps themselves to decrease monotonically.

Finite-dimensional boundedness gives a convergent subsequence \(x_{k_j}\to x^*\in C\). Since \(y_{k_j}-x_{k_j}\to0\) and \(D\) is closed, \(x^*\in D\). Applying the decreasing-distance property to this intersection point, and using the subsequence limit, gives convergence of the entire sequence to \(x^*\); the vanishing gap gives the same limit for \(y_k\). These arguments do not establish arbitrary infinite-dimensional norm convergence or behavior for disjoint sets, nor do they identify the limit as the nearest intersection point to \(x_0\).

For two lines \(V_i=\operatorname{span}v_i\) with unit directions and \(c=\langle v_1,v_2\rangle\),
\[
(P_{V_2}P_{V_1})^n x=c^{2n-1}\langle x,v_1\rangle v_2\quad(n\ge1).
\]
For distinct lines \(|c|<1\), so this tends to their intersection zero, with a factor \(c^2\) per full cycle after the first. If \(|c|=1\), the lines coincide and the iterates equal the common projection after the first cycle. In the example \(v_1=(\sqrt3/2,1/2)^T\), \(v_2=(1/2,\sqrt3/2)^T\), the cycle factor is \(3/4\).

The compactness step uses Bolzano–Weierstrass specifically in finite-dimensional Euclidean space: every bounded sequence has a convergent subsequence, and a norm bound passes to its limit. It applies to a fixed-size matrix sequence by viewing its entries as a finite vector. Merely knowing boundedness in an arbitrary infinite-dimensional space does not supply the same norm-convergent subsequence.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `Introduction and general information/Booklet of Exercises FDA.pdf`, Exercises 2.1.7–2.1.8, pp. 18–19; solutions, pp. 31–33.
- `6. Mai - 12. Mai/Problem Set 3.pdf`, Exercise 3.3, p. 1.
- `13. Mai - 19. Mai/Solution Sheet 3.pdf`, single physical page, Exercise 3.3(a–d), composition, induction and all three inner-product cases.
- `13. Mai - 19. Mai/Problem Set 4.pdf`, Exercise 4.2(a–g), p. 2.
- `20. Mai - 26. Mai/Solution Sheet 4.pdf`, single physical page, Exercise 4.2(a–g), projection inequalities, monotone distances, vanishing gaps, accumulation point and whole-sequence convergence.
- `20. Mai - 26. Mai/All you... math 5`, single physical page, final “Bolzano–Weierstrass (True in Finite Dimension)”, theorem and subsequence notation.
