---
id: tum-fda-markov-moment-bounds
source: tum-foundations-data-analysis
parent: fda-probability
title: Markov bounds and higher-moment tail control
type: theorem
caption: "Bounds nonnegative tails by expectations and shows how moment choice changes the estimate and its sharpness."
---

# Markov bounds and higher-moment tail control

For a nonnegative random variable \(Z\) and \(t>0\),
\[
\mathbb P(Z\ge t)\le\frac{\mathbb EZ}{t},
\]
provided its expectation is finite. Apply this to \(|X|^r\) to obtain \(\mathbb P(|X|\ge t)\le\mathbb E|X|^r/t^r\). More generally an increasing nonnegative transform can be used when its value at the threshold is positive. Higher moments do not guarantee monotonically improving bounds: the ratio must be compared.

For \(X\sim U[0,4]\) at threshold 3, the first moment gives \(2/3\), and the second gives \(16/27\). The integer \(r\)-moment bound is \((4/3)^r/(r+1)\). Allowing real \(r>0\), differentiation gives the minimizing value \(r=1/\log(4/3)-1\approx2.48\). The integer minimum must compare its two neighbors: \(r=2\) and \(r=3\) both give \(16/27\). The booklet's approximately 58.7% optimum uses a real exponent, although the exercise initially asks for an integer. The exact tail probability is only 25%.

The further two-point example \(\mathbb P(X=a)=1/a\), \(\mathbb P(X=0)=1-1/a\), \(a\ge1\), has mean one and attains Markov's bound at \(t=a\): \(\mathbb P(X\ge a)=1/a\). Thus the universal bound can be sharp even though it is loose for the uniform example.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `Introduction and general information/Booklet of Exercises FDA.pdf`, Exercise 3.1.2(1–3), pp. 41–42 and solution p. 49; further “Markov’s Inequality” task, p. 44.
- `3. Juni - 9. Juni/Problem Set 7.pdf`, Exercise 7.1(a–c), p. 1.
- `10. Juni - 16. Juni/Solution Sheet 7.pdf`, single physical page, Exercise 7.1(a–c), full derivations and comparisons.
