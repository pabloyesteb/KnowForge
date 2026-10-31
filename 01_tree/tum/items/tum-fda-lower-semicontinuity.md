---
id: tum-fda-lower-semicontinuity
source: tum-foundations-data-analysis
parent: fda-convex-optimization
title: Lower semicontinuity through epigraphs and sequential limits
type: concept
caption: "Relates a closed epigraph to the prohibition of upward value jumps relative to nearby limiting values."
---

# Lower semicontinuity through epigraphs and sequential limits

For a real-valued function on \(\mathbb R^n\), its epigraph is
\[
\operatorname{epi}f=\{(x,r)\in\mathbb R^n\times\mathbb R:r\ge f(x)\}.
\]
Lower semicontinuity is equivalent to this set being closed, or to the sequential condition
\[
f(x)\le\liminf_j f(x_j)\quad\text{whenever }x_j\to x.
\]
Thus nearby values may approach a height above the value at the point, but cannot have a limiting inferior strictly below it. Continuous functions satisfy the condition; a downward spike can still be lower semicontinuous, while raising the function at a point above a lower nearby branch violates it.

The review's epigraph drawings explain the same distinction geometrically: missing lower boundary points prevent the epigraph from being closed. Convexity of the epigraph is a separate requirement defining a convex function; lower semicontinuity concerns closure rather than the segment condition. The examples concern values and topology, not an assumption that every convex function on an arbitrary domain is automatically lower semicontinuous at its boundary.

Arbitrary pointwise suprema preserve lower semicontinuity:
\[
\operatorname{epi}(\sup_i f_i)=\bigcap_i\operatorname{epi}(f_i).
\]
Each epigraph is closed, and an arbitrary intersection of closed sets remains closed; the index set need not be countable. For a proper extended-real function \(f\), its conjugate is lower semicontinuous because it is the supremum, over points where \(f\) is finite, of continuous affine functions \(y\mapsto\langle y,x\rangle-f(x)\). Terms with \(f(x)=+\infty\) do not contribute. This lower-semicontinuity argument does not require convexity of the original \(f\).

The booklet proves epigraph closure directly as well: if \(r<f(x)\), choose \(r<\beta<f(x)\); lower semicontinuity supplies a neighborhood where \(f>\beta\). Its product with \((-\infty,\beta)\) lies outside the epigraph, proving that the complement is open.

The sequential proof of epigraph closure must use \(\liminf f(x_j)\), since \(x_j\to x\) need not make \(f(x_j)\) converge: from \(r_j\ge f(x_j)\) and \(r_j\to r\), obtain \(r\ge\liminf f(x_j)\ge f(x)\).

The review defines the lower limit as \(\liminf_j a_j=\sup_N\inf_{j\ge N}a_j\), permitting infinite values; for a bounded real sequence it is its lowest subsequential limit. It preserves nonstrict inequalities, while strict inequalities may become equal at the limit. Whenever the extended sums are defined, \(\liminf(a_j+b_j)\ge\liminf a_j+\liminf b_j\); this proves that the sum of two real-valued lower semicontinuous functions is lower semicontinuous. The inequality need not be equality because the separate low subsequences may occur at different indices.

The supporting topology rules are asymmetric: arbitrary unions and finite intersections preserve openness, while arbitrary intersections and finite unions preserve closedness. A sequence converging to a point of an open set is eventually inside it; a convergent sequence entirely in a closed set retains its limit there.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `1. Juli - 7. Juli/All you... math 11`, single physical page, “Lower Semi-Continuity”, closed-epigraph drawings, discontinuity examples and sequential liminf condition.
- `Introduction and general information/Booklet of Exercises FDA.pdf`, Exercise 5.1.4, p. 63; closure, arbitrary-index intersection and conjugate proofs, p. 71.
- `1. Juli - 7. Juli/Exercise Sheet 11.pdf`, Exercise 11.1(a–c), p. 1.
- `8. Juli - 14. Juli/Solution Sheet 11.pdf`, single physical page, Exercise 11.1(a–c), corrected liminf argument, epigraph intersection and alternative supremum proof.
- `8. Juli - 14. Juli/All you ... math 12`, single physical page, “Liminf and Lim (Limsup)”, liminf sum/monotonicity, lower-semicontinuous sum, and “Basics of Topology”.
