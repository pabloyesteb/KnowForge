---
id: tum-co-linear-integer-models
source: tum-combinatorial-optimization
parent: co-foundations
title: Linear programs, integer restrictions and the integer hull
type: concept
caption: "Separates continuous linear optimization from integer-feasible solutions through their convex hull."
---

# Linear programs, integer restrictions and the integer hull

A linear program optimizes \(c^Tx\) over real variables subject to finitely many affine inequalities or equalities. A common maximization form has feasible polyhedron \(P=\{x\in\mathbb R^n:Ax\le b,x\ge0\}\). Adding \(x\in\mathbb Z^n\) produces an integer linear program; simply solving the continuous relaxation can yield a fractional optimum.

The integer hull is \(P_I=\operatorname{conv}(P\cap\mathbb Z^n)\). Linear objectives over the integer points and their convex hull have the same supremum, since every finite convex combination has objective equal to the corresponding combination of objectives. However, the original relaxation \(P\) can be strictly larger. The class diagram illustrates a triangle with a fractional maximizing vertex and an integer hull with a different boundary and optimum.

The prerequisite theorem states polynomial-time solvability of linear programming, naming the ellipsoid method. For the algorithmic statement, coefficients must have finite rational encodings and the input size includes their bit lengths; this does not assert a polynomial-time method for arbitrary integer programs or the availability of an explicit small description of every integer hull. No ellipsoid algorithm construction is developed in this introductory block.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Lecture Notes/lecture notes.pdf`, §1.2, pp. 7–8, Definition 1.12, Theorem 1.13 and integer-hull notation.
- `Lecture Notes/class notes for 19 April.pdf`, printed slides 26–28 (physical pp. 39–43), integer-hull figure and continuous/integer distinction.
