---
id: tum-fda-normalized-gradient-stopping
source: tum-foundations-data-analysis
parent: fda-convex-optimization
title: Normalized gradient steps and competing stopping criteria
type: algorithm
caption: "Specifies a unit-direction gradient iteration with decaying travel lengths and three independent stopping tests."
---

# Normalized gradient steps and competing stopping criteria

The numerical task minimizes
\[
f(x_1,x_2)=(x_1-3)^4+(x_1-3x_2)^2
\]
using the normalized gradient direction:
\[
x_{k+1}=x_k-\lambda_k\frac{\nabla f(x_k)}{\|\nabla f(x_k)\|},\quad
x_0=(0,0),\quad\lambda_k=0.9^{k+1}.
\]
Here \(\nabla f=(4(x_1-3)^3+2(x_1-3x_2),-6(x_1-3x_2))\). Normalization makes the displacement length exactly \(\lambda_k\) when the gradient is nonzero. Check for a zero gradient before dividing; it already satisfies the gradient stopping test. The nonnegative terms vanish together at the unique minimizer \((3,1)\).

The task compares the first triggering of three tests: gradient norm at most 3.5; successive objective difference at most 0.4 in absolute value; and a cap of 10 iterations. The objective-difference test requires two available iterates, and an implementation must keep iteration indices consistent with the prescribed step sequence. These tests measure different things: stationarity, small observed progress, and computational budget. A small objective change alone does not prove proximity to the minimizer. The supplied booklet solution points to MATLAB code without providing a numerical trace or winner on these pages; no execution result is asserted here.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `Introduction and general information/Booklet of Exercises FDA.pdf`, Exercise 6.1.2, p. 77 and solution pointer p. 79.
