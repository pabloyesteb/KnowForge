---
id: tum-fda-equatorial-volume-concentration
source: tum-foundations-data-analysis
parent: fda-probability
title: Concentration of high-dimensional ball volume near an equator
type: theorem
caption: "Bounds the volume outside a thin coordinate slab using cross-sectional integration and an inscribed-cylinder lower bound."
---

# Concentration of high-dimensional ball volume near an equator

For the uniform volume distribution on the unit ball in \(\mathbb R^n\), \(n\ge3\), and \(c\ge1\),
\[
\mathbb P\left(|X_1|>\frac{c}{\sqrt{n-1}}\right)
\le\frac2c e^{-c^2/2}.
\]
Thus at least \(1-2e^{-c^2/2}/c\) of the volume lies in a slab of width proportional to \(1/\sqrt n\) around a coordinate equator. If the slab already covers the ball, the event is empty. This is a volume result; the proof does not replace volume by boundary surface area.

For \(a=c/\sqrt{n-1}\le1\), the cap in the upper half ball \(H\) has volume
\[
V(n-1)\int_a^1(1-t^2)^{(n-1)/2}\,dt.
\]
Using \(1-u\le e^{-u}\), extending the integral to infinity, and inserting \(t\sqrt{n-1}/c\ge1\), bounds it by \(V(n-1)e^{-c^2/2}/(c\sqrt{n-1})\). Meanwhile \(H\) contains a cylinder of height \(1/\sqrt{n-1}\) and base radius \(\sqrt{1-1/(n-1)}\). Its volume is at least \(V(n-1)/(2\sqrt{n-1})\), by the corresponding Bernoulli bound. Dividing gives the cap fraction \(2e^{-c^2/2}/c\) within \(H\). Reflection supplies the identical lower cap, hence the same relative bound for the full ball.

The shrinking transverse scale explains why a random point has a small coordinate along any fixed axis despite lying in a high-dimensional ball.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `Introduction and general information/Booklet of Exercises FDA.pdf`, Exercise 3.1.1(c), p. 41; solution, cap and cylinder figures and three-step proof, pp. 46–48.
