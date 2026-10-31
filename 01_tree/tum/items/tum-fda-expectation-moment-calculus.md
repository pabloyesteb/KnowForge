---
id: tum-fda-expectation-moment-calculus
source: tum-foundations-data-analysis
parent: fda-probability
title: Expectations and squared distances of independent uniform variables
type: method
caption: "Uses integration, linearity and independence to compute elementary moments and average squared distances."
---

# Expectations and squared distances of independent uniform variables

For a variable with density \(\varphi\), compute \(\mathbb E h(X)=\int h(x)\varphi(x)\,dx\) when the expectation exists. Linearity handles sums without independence; factoring \(\mathbb E(XY)=\mathbb EX\mathbb EY\) requires independence (or another justified factorization).

For independent \(X,Y\sim U[0,1]\), the booklet's further tasks give
\[
\mathbb EX=1/2,\quad \mathbb EX^2=1/3,\quad
\mathbb E(X-Y)=0,\quad\mathbb E(XY)=1/4,
\]
and expansion yields \(\mathbb E(X-Y)^2=2/3-1/2=1/6\). Consequently two independent uniform points in the unit square have expected squared distance \(1/6+1/6=1/3\), summing the coordinate contributions. Squared distance is the quantity averaged here; taking a square root afterwards does not give the expected distance.

For the separate \(U[0,4]\) example, integrating gives \(\mathbb EX^r=4^r/(r+1)\). These moments feed the probability-bound comparison, while direct density integration gives the exact probability \(\mathbb P(X>3)=1/4\).

For a finite discrete variable, the same expectation principle becomes \(\mathbb Eh(X)=\sum_i h(x_i)p_i\). The review's elementary three-year warranty model sets damage costs to 100 with probability 0.15, 300 with probability 0.05 and zero otherwise, yielding expected cost \(100(0.15)+300(0.05)=30\). Prices 25 and 35 differ from that expected cost by minus or plus 5 per contract. These are stipulated teaching probabilities and expectation arithmetic, not measured failure rates, a complete pricing model or financial advice; they do not eliminate variation in individual outcomes.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `Introduction and general information/Booklet of Exercises FDA.pdf`, Exercise 3.1.2, pp. 41–42 and solution p. 49; first two further random-variable exercises, p. 44 (the displayed moment/distance values follow by evaluating those tasks).
- `10. Juni - 16. Juni/All you... math 8`, single physical page, final “Examples of Simple Computations — Warranty on a Laptop”.
