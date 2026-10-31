---
id: tum-fda-convex-projection
source: tum-foundations-data-analysis
parent: fda-linear-geometry
title: Hilbert projection onto closed convex sets
type: theorem
---

# Hilbert projection onto closed convex sets

For a **nonempty**, closed convex \(K\) in a real Hilbert space and any \(v\), there is a unique nearest point \(P_Kv\). Nonemptiness is necessary in addition to the printed closedness/convexity conditions.

## Existence through a minimizing Cauchy sequence

Translate \(v\) to zero and set \(d=\inf_{w\in K}\|w\|\), without assuming attainment. The parallelogram identity and feasibility of the midpoint give
\[
\|x-y\|^2=2\|x\|^2+2\|y\|^2-4\|(x+y)/2\|^2
\le2\|x\|^2+2\|y\|^2-4d^2.
\]
A minimizing sequence is Cauchy, so completeness supplies a limit and closedness keeps it feasible. Its norm is \(d\). For two minimizers the same bound forces distance zero, proving uniqueness.

## Variational characterization

For \(p\in K\),
\[
p=P_Kv\iff\langle z-p,v-p\rangle\le0\quad\forall z\in K.
\]
If \(p\) is nearest, compare it to \(p+\lambda(z-p)\), expand the squared distances, divide by \(\lambda>0\), then let \(\lambda\downarrow0\). Conversely expand
\(\|v-z\|^2=\|v-p\|^2+\|z-p\|^2-2\langle v-p,z-p\rangle\); the sign condition makes \(p\) nearest.

For the Euclidean unit ball \(B_2\),
\[
P_{B_2}(x)=\frac{x}{\max(1,\|x\|_2)}.
\]
An interior point projects to itself; an exterior point projects radially to the boundary. Replacing the ball by the sphere changes the problem: the sphere is not convex, at zero every sphere point is nearest, and the displayed ball formula would return an infeasible point for \(\|x\|<1\). The theorem is therefore not a generic nearest-point guarantee for all closed sets.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `Introduction and general information/Booklet of Exercises FDA.pdf`, Exercises 1.1.3(b)/1.1.4, p. 4; solutions, pp. 10–12.
- `22. April - 28. April/Problem Set 1.pdf`, Exercise 1.1(a–c), p. 1.
