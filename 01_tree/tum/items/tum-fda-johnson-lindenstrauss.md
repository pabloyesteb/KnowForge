---
id: tum-fda-johnson-lindenstrauss
source: tum-foundations-data-analysis
parent: fda-random-projections
title: Finite-set distance preservation with Johnson–Lindenstrauss maps
type: theorem
caption: "Relates pairwise squared-distance distortion to normalized linear images and uses a finite union bound rather than an ambient-space guarantee."
---

# Finite-set distance preservation with Johnson–Lindenstrauss maps

For a linear map \(A\) and distinct points \(v,w\), set \(x=v-w\). The squared-distance inequalities
\[
(1-\varepsilon)\|v-w\|_2^2\le\|Av-Aw\|_2^2\le(1+\varepsilon)\|v-w\|_2^2
\]
are equivalent to
\[
\left|\frac{\|Ax\|_2^2}{\|x\|_2^2}-1\right|\le\varepsilon.
\]
Identical points satisfy distance preservation trivially and must be excluded from the quotient.

For a finite set of \(m\) points independent of a normalized Gaussian matrix, apply the fixed-vector concentration estimate to their at most \(m(m-1)/2\) nonzero differences. A union bound controls simultaneous failure. Norm distortion \(\delta\) gives squared-norm distortion at most \(2\delta+\delta^2\); choosing \(\delta\) proportional to \(\varepsilon\) retains an exponential \(e^{-ck\varepsilon^2}\) failure bound. Hence embedding dimension on the order of \(\varepsilon^{-2}\log(m/\eta)\) suffices to make this finite-set failure probability at most \(\eta\), up to absolute constants. This is the standard finite-set consequence of the preceding original estimates, rather than a supplied proof of every version of the lecture lemma.

No dimension-reducing linear map can give that guarantee for all vectors in the ambient space: it has a nonzero kernel. The finite set and the order of randomness are essential.

The booklet proposes \(d=10000\), 10000 random Gaussian test differences, tolerance 0.1, and \(k=200,300,\ldots,3000\), comparing independent Gaussian entries \(N(0,1/k)\) with independent signs \(\pm1/\sqrt k\). This is a numerical comparison task; the Gaussian derivation alone does not prove the sign-matrix guarantee or provide successful measured dimensions. Testing 10000 chosen differences is not exhaustive testing of all pairs in a 10000-point dataset.

The weekly solution includes a source-reported fraction-of-tests plot, annotated at approximately 90% satisfaction for \(k=600\) and 95% for \(k=800\), with tolerance 0.1. The figure summarizes selected tests rather than proving that all differences satisfy the bound; its unsquared annotation also does not settle whether that plot tests exactly the squared-ratio criterion from part (a). It cannot establish a minimal universally sufficient dimension.

The review motivates embedding by storage: \(m\) points in dimension \(d\) require \(md\) coordinates, while an embedded dataset uses \(mk\). Storing all pairwise distances instead costs order \(m^2\), which can be larger when there are many points. These are dataset-storage comparisons, excluding the separate cost of representing or applying the embedding itself. The normalized Gaussian scaling is still required even where the review abbreviates its matrix entries as standard Gaussians.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `Introduction and general information/Booklet of Exercises FDA.pdf`, Exercise 4.1.2, pp. 57–58; squared-distance reformulation, p. 60; fixed-vector bound used in the finite-set derivation, Exercise 4.1.1, pp. 57, 59.
- `17. Juni - 23. Juni/Exercise sheet 9.pdf`, Exercise 9.3(a–b), p. 2.
- `24. Juni - 30. Juni/Solution Sheet 9.pdf`, single physical page, Exercise 9.3(a–b), reformulation and fraction-of-tests figure.
- `24. Juni - 30. Juni/All you... math 10`, single physical page, final “Johnson–Lindenstrauss Lemma”, storage comparison, distance bounds and Gaussian-map motivation.
