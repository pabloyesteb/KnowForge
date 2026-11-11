---
id: tum-uq-random-diffusion-models
source: tum-numuq
parent: uq-pde
title: Bounded affine and lognormal diffusion models
type: concept
caption: Distinguishes deterministic uniform ellipticity from realization-dependent positivity in two coefficient constructions.
---

# Bounded affine and lognormal diffusion models

The course's bounded affine model is
\[
a(x,\omega)=\mu+\sum_{k=1}^P\frac{\sigma}{k^2\pi^2}\cos(\pi kx)\xi_k(\omega),\qquad\xi_k\stackrel{\rm iid}{\sim}U[-1,1].
\]
Using \(|\xi_k|\le1\), \(|\cos|\le1\), and \(\sum k^{-2}=\pi^2/6\) gives \(\mu-\sigma/6\le a\le\mu+\sigma/6\). Thus \(\mu>\sigma/6\) guarantees uniform positive lower and finite upper bounds, independent of the outcome. The finite sum is smooth in space and depends linearly on the inputs. The uniform-input assumption is essential to these deterministic bounds; a handwritten Gaussian-input annotation on L10's example does not preserve them.

A lognormal field is \(a=e^Z\) for Gaussian \(Z\). For a continuous version on the compact spatial closure, each realization is strictly positive and bounded: \(e^{-\|Z\|_C}\le a_{\min}(\omega)\le a_{\max}(\omega)\le e^{\|Z\|_C}\). The bounds depend on \(\omega\); a nondegenerate Gaussian field generally supplies no deterministic bounds uniform over outcomes. A finite Gaussian expansion for \(Z\) makes \(a\) a nonlinear function of its standard-normal coordinates.

Lipschitz stationary covariance increments allow Kolmogorov's criterion to supply the required Hölder version before exponentiation. Continuity on an open bounded domain alone does not ensure attained finite extrema; use the continuous extension to the compact closure. These distinctions explain why pathwise ellipticity is a suitable assumption for lognormal models even when uniform ellipticity fails.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, §§6.1–6.2, Examples 6.1, 6.3 and 6.5, Definition 6.2, Assumptions 6.4, 6.6–6.7 and Lemma 6.8, pp. 46–48.
- `Lecture Topics and Slides/Lecture 10 (04.06.24)`, physical pp. 3–10, coefficient examples and handwritten bounds.
