---
id: tum-uq-elliptic-weak-solution
source: tum-numuq
parent: uq-pde
title: Weak elliptic solutions by Lax–Milgram and an energy bound
type: theorem
caption: Obtains existence, uniqueness and data stability for bounded positive diffusion without requiring classical differentiability.
---

# Weak elliptic solutions by Lax–Milgram and an energy bound

For \(-\nabla\cdot(a\nabla u)=f\) with zero Dirichlet boundary data, let \(D\) be bounded in the course's piecewise smooth setting, \(f\in L^2(D)\), and \(0<a_{\min}\le a(x)\le a_{\max}<\infty\) almost everywhere. Multiplication by a test function and integration by parts motivate
\[
A(u,v)=\int_Da\nabla u\cdot\nabla v,\qquad \ell(v)=\int_Dfv,\qquad
A(u,v)=\ell(v)\ \ \forall v\in V=H_0^1(D).
\]
The bilinear form is bounded by \(a_{\max}|u|_{H^1}|v|_{H^1}\) and coercive with constant \(a_{\min}\); Poincaré makes \(\ell\) bounded on \(V\). Lax–Milgram gives a unique weak solution. This avoids imposing classical coefficient differentiability; the notes' assertion that classical solutions exist only for \(a\in C^1\) is not a necessary condition in every particular problem.

Testing with \(u\), using coercivity and Poincaré, and dividing when \(|u|_{H^1}>0\) gives
\[
|u|_{H^1}\le a_{\min}^{-1}K_P\|f\|_{L^2}.
\]
The zero solution satisfies the estimate directly. Lax–Milgram itself applies to any bounded coercive bilinear form on a real Hilbert space and any bounded linear functional; symmetry is not required for that existence result.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, ch. 5 through §5.1, Assumption 5.1, Definition 5.2, Lemma 5.3 and Theorems 5.4–5.5, pp. 43–45.
- `Lecture Topics and Slides/Lecture 09 (28.05.24)`, physical pp. 5–12, weak-form derivation, Lax–Milgram and handwritten stability proof.
