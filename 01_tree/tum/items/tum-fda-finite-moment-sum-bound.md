---
id: tum-fda-finite-moment-sum-bound
source: tum-foundations-data-analysis
parent: fda-probability
title: Tail bounds for independent sums under finite factorial moment control
type: theorem
caption: "Records the source exercise linking an even-moment bound to a Gaussian-type tail over a restricted deviation range."
---

# Tail bounds for independent sums under finite factorial moment control

The further exercise considers \(X=\sum_{i=1}^nX_i\) with mutually independent, mean-zero summands, variance at most \(\sigma^2>0\), and an even positive integer \(s\le n\sigma^2/2\). It assumes
\[
|\mathbb EX_i^r|\le\sigma^2r!\quad(r=3,\ldots,s),
\qquad 0<a\le\sqrt2\,n\sigma^2.
\]
Under these stated conditions its first requested bound is
\[
\mathbb P(|X|\ge a)\le\left(\frac{2sn\sigma^2}{a^2}\right)^{s/2}.
\]
With the additional condition \(s\ge a^2/(4n\sigma^2)\), it asks to show
\[
\mathbb P(|X|\ge a)\le3\exp\left(-\frac{a^2}{12n\sigma^2}\right).
\]
These are source-stated exercise targets with no supplied solution, not an extracted proof of a general unlimited tail theorem. The finite moment order, parity, independence and restricted deviation range remain part of the statement. In particular finite variance alone does not justify the second exponential bound.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `Introduction and general information/Booklet of Exercises FDA.pdf`, further exercise “Sum of Random Variables”, p. 44, both requested bounds and all printed hypotheses.
