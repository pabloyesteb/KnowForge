---
id: tum-fda-ball-volume-dimension
source: tum-foundations-data-analysis
parent: fda-probability
title: Dimension-dependent ball volumes and sphere areas
type: result
caption: "Expresses unit-ball geometry through the Gamma function and identifies its nonmonotone dependence on dimension."
---

# Dimension-dependent ball volumes and sphere areas

For integer \(n\ge1\), the unit ball volume and unit sphere boundary area are
\[
V(n)=\frac{2\pi^{n/2}}{n\Gamma(n/2)},\qquad
A(n)=\frac{2\pi^{n/2}}{\Gamma(n/2)}=nV(n),\qquad
\Gamma(x)=\int_0^\infty t^{x-1}e^{-t}\,dt\quad(x>0).
\]
Scaling the radius to \(r\) multiplies volume by \(r^n\). The booklet's dimension plot and solution identify the integer maxima at \(n=5\) for volume and \(n=7\) for area; both tend to zero as \(n\to\infty\). Increasing dimension therefore does not monotonically increase the volume of a fixed-radius ball. This statement holds with radius fixed at one, not under an arbitrary dimension-dependent rescaling.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `Introduction and general information/Booklet of Exercises FDA.pdf`, Exercise 3.1.1(a–b), p. 41; solution and plot, p. 46; radius-scaling identity, p. 47.
