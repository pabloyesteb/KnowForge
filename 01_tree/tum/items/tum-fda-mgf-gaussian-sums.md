---
id: tum-fda-mgf-gaussian-sums
source: tum-foundations-data-analysis
parent: fda-probability
title: Moment-generating functions and independent Gaussian sums
type: method
caption: "Factors independent exponential moments and derives Gaussian MGFs by completing the square."
---

# Moment-generating functions and independent Gaussian sums

The moment-generating function is \(M_X(\theta)=\mathbb E e^{\theta X}\), on the set of parameters where it is finite. Independence gives
\[
M_{X+Y}(\theta)=\mathbb E(e^{\theta X}e^{\theta Y})=M_X(\theta)M_Y(\theta).
\]
For \(X\sim N(0,1)\), completing the square gives \(\theta x-x^2/2=-(x-\theta)^2/2+\theta^2/2\). Translating the normalized Gaussian density yields \(M_X(\theta)=e^{\theta^2/2}\) for every real \(\theta\). More generally,
\[
X\sim N(\mu,\sigma^2)\quad\Longrightarrow\quad
M_X(\theta)=\exp(\mu\theta+\sigma^2\theta^2/2).
\]
Consequently a sum of independent Gaussians has a Gaussian law with mean equal to the sum of means and variance equal to the sum of variances, as requested in the further exercise. Multiplication of MGFs records the full distributional structure here, rather than merely its first two moments; a sum of arbitrary independent variables with those moments need not be Gaussian.

When the MGF is finite on a neighborhood of zero, differentiating under its expectation recovers moments: \(M_X'(0)=\mathbb EX\), \(M_X''(0)=\mathbb EX^2\), and similarly higher derivatives. The review uses the standard Gaussian MGF \(e^{\theta^2/2}\) to express \(\mathbb EX^6\) as its sixth derivative at zero, avoiding a separate sixth-moment integral. Finiteness near zero justifies this moment-generating use; existence of a finite variance by itself does not.

For a standard Gaussian vector \(g\), a right singular vector \(v_i\) of a fixed matrix \(A\), and integer \(r\ge1\),
\[
\langle(A^TA)^rg,v_i\rangle=\sigma_i^{2r}\langle g,v_i\rangle
\sim N(0,\sigma_i^{4r}).
\]
For \(\sigma_i>0\), the Gaussian tail estimate therefore gives \(\mathbb P(|\langle(A^TA)^rg,v_i\rangle|>t)\le\exp[-t^2/(2\sigma_i^{4r})]\). A zero singular value instead gives the identically zero variable. The exponent tracks the variance after repeated Gram-matrix multiplication, not just the original Gaussian variance.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `Introduction and general information/Booklet of Exercises FDA.pdf`, Exercise 3.1.3, p. 42; solution, p. 50; further Gaussian-sum exercise, p. 44.
- `3. Juni - 9. Juni/Problem Set 7.pdf`, Exercise 7.2(a–b), p. 1.
- `10. Juni - 16. Juni/Solution Sheet 7.pdf`, single physical page, Exercise 7.2(a–b), full derivations and comparisons.
- `17. Juni - 23. Juni/All you... math 9`, single physical page, “Moment Generating Function”, first/second derivative identities and Gaussian sixth-moment example.
- `Introduction and general information/Sample Exam (from SoSe 2022).pdf` and `Introduction and general information/Sample Solutions for the Sample Exam.pdf`, Problem 1(c), p. 3 of task; Problem 1(b), p. 3 of solutions, spectral expansion and Gaussian-coordinate variance.
