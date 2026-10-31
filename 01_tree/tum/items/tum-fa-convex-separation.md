---
id: tum-fa-convex-separation
source: tum-functional-analysis
parent: fa-fundamental-principles
title: Minkowski functionals and separation of convex sets
type: theorem
caption: "Builds sublinear gauges from convex sets and uses them to separate points and convex sets under precise openness or closedness assumptions."
---

# Minkowski functionals and separation of convex sets

## From geometry to a sublinear functional

For \(A\subset X\), define \(M_A(x)=\inf\{t>0:x/t\in A\}\), with value \(+\infty\) if no such \(t\) exists. The set is absorbing if this value is finite for every vector. For convex absorbing \(A\), \(M_A\) is sublinear: if \(x/t,y/s\in A\), convexity places \((x+y)/(t+s)\in A\), giving subadditivity by approximation to the infima. Positive homogeneity follows by scaling.

In a normed space, \(0\in\operatorname{int}A\) implies absorption. The unit ball's gauge is the norm. For open convex \(A\) containing zero, \(M_A(x)<1\) on \(A\); a ball of radius \(\varepsilon\) contained in \(A\) yields \(M_A(x)\le\|x\|/\varepsilon\).

## Separation statements over the real field

For nonempty open convex \(K\subset X\) and \(x_0\notin K\), there is a nonzero \(f\in X^*\) with
\[
f(x)<f(x_0)\quad(x\in K).
\]
After translating \(K\) to contain zero, extend the functional \(tx_0\mapsto tM_K(x_0)\) dominated by \(M_K\). Gauge bounds give continuity, and \(f(x)<1\le f(x_0)\) gives separation.

If \(K_1,K_2\) are disjoint nonempty convex sets with \(K_1\) open, apply this result to \(K_1-K_2\) and zero. There are \(f\ne0\) and \(\alpha\in\mathbb R\) such that
\[
f(x_1)<\alpha\le f(x_2)\quad(x_i\in K_i).
\]
Openness makes the \(K_1\) inequality strict; it is not a uniform positive gap.

For nonempty closed convex \(K\) and \(x_0\notin K\), the stronger point–set form holds:
\[
f(x)\le\alpha<f(x_0)\quad(x\in K).
\]
Separate \(K\) from an open ball around \(x_0\) disjoint from \(K\), reversing the functional's sign as needed. Closedness alone does not assert strict separation of every pair of closed convex sets.

A nonzero real continuous functional defines a hyperplane \(f(x)=\alpha\) and its two half-spaces. For complex spaces, separation inequalities concern real parts of complex-linear functionals, not an order on \(\mathbb C\).

## Source references
Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`. N = `Materials/Lecture notes.pdf` (WS 2017/18); E/S refer to `Problem sheets/Problem Sheet <n>.pdf` and `Solutions to problem sheets/Solutions Sheet <n>.pdf` (WS 2024/25).
- N, Definitions 4.1–4.2 and Lemma 4.3, p. 37; Propositions 4.16–4.18, pp. 43–45.
- E7/S7, T7.2 (closed-convex point separation proof).
