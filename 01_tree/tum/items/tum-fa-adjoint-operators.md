---
id: tum-fa-adjoint-operators
source: tum-functional-analysis
parent: fa-compact-fredholm
title: Banach and Hilbert adjoints, annihilators and compactness
type: theorem
---

# Banach and Hilbert adjoints, annihilators and compactness

## Dual composition

For bounded \(T:X\to Y\), define \(T^*:Y^*\to X^*\) by \(T^*y^*=y^*\circ T\). Thus
\[
\langle Tx,y^*\rangle_{Y,Y^*}=\langle x,T^*y^*\rangle_{X,X^*},
\qquad \|T^*\|=\|T\|,
\qquad T^{**}J_X=J_YT.
\]
The norm equality follows by interchanging suprema over the two unit balls and using norming functionals. The evaluation pairing is continuous bilinear, with \(|x^*(x)|\le\|x^*\|\|x\|\). It is not the complex Hilbert inner product: the Riesz identification is conjugate-linear under the convention linear in the first slot.

For the inclusion \(j:U\hookrightarrow X\) of a normed subspace, \(j^*f=f|_U\): its adjoint is restriction of functionals.

If \(T\) is an isomorphism, \((T^*)^{-1}=(T^{-1})^*\); if it is a surjective isometry, so is \(T^*\). The map \(T\mapsto T^*\) is an isometric linear embedding of operator spaces, not generally surjective onto all maps between the duals.

## Hilbert identification and examples

Riesz representation gives the unique Hilbert adjoint characterized by \(\langle Tx,y\rangle=\langle x,T^*y\rangle\). Then
\[
\ker T=(\operatorname{ran}T^*)^\perp,\qquad
\ker T^*=(\operatorname{ran}T)^\perp,
\qquad T\text{ is isometric}\iff T^*T=I.
\]
The right shift on \(\ell^2\) has left-shift adjoint, \(T^*T=I\), but \(TT^*\) is projection onto \(e_1^\perp\); isometry does not imply surjectivity. In complex Hilbert space, \(T=T^*\) iff \(\langle Tx,x\rangle\) is real for every \(x\): polarization with \(x+y\) and \(x+iy\) recovers the cross terms. This characterization depends on the complex field.

For multiplication \(M_\phi\) on \(L^p\), \(1\le p<\infty\), the Banach adjoint is multiplication by \(\phi\) in the bilinear dual-density convention \(f\mapsto\int fg\). In complex Hilbert \(L^2\), the Hilbert adjoint instead multiplies by \(\overline\phi\). It is self-adjoint iff \(\phi\) is real a.e. Likewise a real integral kernel is transposed by the adjoint; the complex Hilbert kernel is conjugate-transposed.

## Annihilators and compactness

For normed spaces,
\[
\overline{T(X)}=(\ker T^*)^\circ
=\{y\in Y:y^*(y)=0\text{ for all }y^*\in\ker T^*\}.
\]
One inclusion follows from composition; Hahn–Banach separates any point outside the closed range closure to prove the reverse. The closure cannot be omitted without an additional closed-range hypothesis.

For Banach spaces, \(T\) is compact iff \(T^*\) is compact. Restrict a bounded sequence of \(Y^*\) functionals to the compact closure of \(T(B_X)\): the restrictions are uniformly bounded and Lipschitz, hence have a uniformly convergent subsequence by Arzelà–Ascoli. Uniform convergence there is precisely the needed Cauchy control of \(T^*y_n^*\). Conversely compactness of \(T^*\) gives compactness of \(T^{**}J_X=J_YT\); the closed isometric image \(J_Y(Y)\) converts its limits back into \(Y\).

## Source references

Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`.
- `Materials/Lecture notes.pdf` (WS 2017/18), Chapter 9, pp. 70–72, Definition 9.2, Lemmas 9.1, 9.3–9.4 and Propositions 9.5–9.6.
- `Problem sheets/Problem Sheet 10.pdf` and `Solutions to problem sheets/Solutions Sheet 10.pdf`, T10.3(a–b), A10.2.
- `Problem sheets/Problem Sheet 11.pdf` and `Solutions to problem sheets/Solutions sheet 11.pdf`, T11.1, A11.1–A11.2 (WS 2024/25).
- `Mock Exam/Mock Exam.pdf` and `Mock Exam/Solutions to Mock Exam.pdf`, P.1(b).
- `Materials/Lecture notes.pdf`, Proposition 13.1, p. 88, for the Hilbert-adjoint convention.
