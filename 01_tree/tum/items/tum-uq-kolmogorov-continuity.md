---
id: tum-uq-kolmogorov-continuity
source: tum-numuq
parent: uq-random-fields
title: Kolmogorov continuity and Hölder versions of Gaussian fields
type: theorem
caption: Derives continuous versions from increment moments using dyadic grids and Borel–Cantelli.
---

# Kolmogorov continuity and Hölder versions of Gaussian fields

A function is Hölder continuous with exponent \(0<\gamma\le1\) if \(|u(x)-u(y)|\le L\|x-y\|^\gamma\); exponent one is Lipschitz continuity. The space \(C^{r,\gamma}\) imposes this on derivatives of order \(r\). A version \(Y\) of a field \(Z\) satisfies \(Y(x)=Z(x)\) almost surely for each fixed \(x\). The exceptional set may depend on \(x\), so this differs from equality at all points on one event of probability one. A cylindrical Gaussian law alone does not ensure continuity of an arbitrary representative.

The course's Kolmogorov criterion on a bounded \(D\subset\mathbb R^d\) is
\[
E|Z(x)-Z(y)|^\alpha\le C\|x-y\|^{d+\beta},\qquad \alpha\ge1,\ \beta>0.
\]
It gives a continuous version with Hölder exponents \(0<\gamma<\beta/\alpha\) (within the usual Hölder range). The strict exponent inequality is essential; the endpoint is not asserted.

The appendix develops the construction on a cube. At grid scale \(2^{-n}\), there are \(O(2^{dn})\) adjacent pairs. Markov's inequality and a union bound give
\[
P\left(\max_{\rm adjacent}|Z(x)-Z(y)|\ge2^{-\gamma n}\right)\lesssim2^{n(\alpha\gamma-\beta)}.
\]
Summability and Borel–Cantelli yield a finite random bound \(K2^{-\gamma n}\) on all dyadic edge increments. Coordinate chains and telescoping geometric sums give a Hölder bound on the countable dense union of grids. Cauchy limits extend it continuously. To verify the version property at a fixed point, choose dense points with distance at most \(2^{-n}\); the moment estimate and summable tail bounds imply their original values converge almost surely to \(Z(x)\), while continuity gives convergence to the extension. The appendix sketches the general bounded-domain reduction; the explicit grid argument is for the cube.

For a centered Gaussian field with radial covariance \(c(x,y)=\widetilde c(\|x-y\|)\) Lipschitz as a function of distance,
\[
E|Z(x)-Z(y)|^2=2[\widetilde c(0)-\widetilde c(\|x-y\|)]\le2L\|x-y\|.
\]
Gaussian even moments then give \(E|Z(x)-Z(y)|^{2p}\le C_p\|x-y\|^p\). Choosing \(p>d\) gives exponents \(\gamma<(p-d)/(2p)\); increasing \(p\) establishes every \(\gamma<1/2\) for a suitable continuous version. The exponential covariance satisfies this condition. Smoothness of a deterministic mean must be included before transferring this centered result to a noncentered field.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, §3.5, Definitions 3.23 and 3.26–3.27, Theorem 3.28, Corollary 3.29 and Example 3.30, pp. 23–25 (through the corollary proof); appendix A, Lemma A.1 and dyadic proof, pp. 95–98 (ending before appendix B).
- `Lecture Topics and Slides/Lecture 05 (30.04.24)`, Hölder spaces, versions and continuity criterion.
- `Lecture Topics and Slides/Lecture 06 (07.05.24)`, physical pp. 1–2 (printed 24–25), theorem and handwritten radial-covariance/exponential clarification.
- `Oral exam/Topics and sample questions (08.07.24)`, §3, p. 2, field regularity, versions and continuity criterion.
