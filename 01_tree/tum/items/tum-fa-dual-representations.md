---
id: tum-fa-dual-representations
source: tum-functional-analysis
parent: fa-normed-spaces
title: Representations of dual spaces
type: theorem
---

# Representations of dual spaces

## Sequence-space duals

For \(1<p<\infty\), \(1/p+1/q=1\),
\[
a\in\ell^q\mapsto F_a,\qquad F_a(x)=\sum_ka_kx_k
\]
is a linear isometric isomorphism \(\ell^q\cong(\ell^p)^*\). Hölder gives absolute convergence and \(\|F_a\|\le\|a\|_q\). Given \(F\), set \(a_k=F(e_k)\). Testing on finite vectors with coordinates
\(\overline{a_k}|a_k|^{q-2}\) (zero at \(a_k=0\)) proves
\[
\left(\sum_{k=1}^N|a_k|^q\right)^{1/q}\le\|F\|.
\]
Pass to the limit, then use density of \(c_e\) and continuous extension to get \(F=F_a\) and norm equality.

The same pairing gives
\[
(c_0)^*\cong\ell^1,\qquad(\ell^1)^*\cong\ell^\infty.
\]
Sheet 2 develops the first in full: the endpoint Hölder bound proves continuity; finite vectors with coordinates \(\overline{a_k}/|a_k|\), set to 1 when \(a_k=0\), prove the lower norm bound. For arbitrary \(F\in(c_0)^*\), those tests bound \(\sum_{k=1}^N|F(e_k)|\); coordinate truncation then reconstructs \(F\). The notes state the second endpoint identification without proving it here. They do **not** identify \((\ell^\infty)^*\) with \(\ell^1\).

**Scalar convention:** these are linear functionals with the bilinear pairing \(\sum a_kx_k\), not a sesquilinear inner product. The conjugated phase in the complex test vector matters. Sheet 2 explicitly prints it; the notes' sign notation on pp. 16–17 must be interpreted consistently with this pairing.

## Function-space representations and scope

### Functionals on bounded sequences beyond summable coefficients

Each \(a\in\ell^1\) defines \(F_a(x)=\sum_n a_nx_n\) on \(\ell^\infty\), with norm \(\|a\|_1\). But these do not exhaust \((\ell^\infty)^*\). The limit functional on \(c\) has norm 1; extend it to \(\ell^\infty\) by Hahn–Banach. Any coefficient representation would vanish on every coordinate vector, forcing all coefficients zero, yet its value at the constant sequence 1 is 1.

On real \(\ell^\infty\), a dominated extension gives a functional \(L\) with
\[
\liminf_n x_n\le L(x)\le\limsup_n x_n.
\]
Use the sublinear functional \(p(x)=\limsup x_n\) to dominate the limit on \(c\), and apply domination also to \(-x\). The inequalities imply boundedness and norm 1. No shift invariance is asserted by this construction.

For open \(D\subset\mathbb R^n\), the notes state
\[
(L^p(D))^*\cong L^q(D)\quad(1<p<\infty),\qquad
(L^1(D))^*\cong L^\infty(D),
\]
through \(F_h(f)=\int_Dhf\). Hölder establishes boundedness; the \(1<p<\infty\) surjectivity sketch invokes Radon–Nikodym, rather than proving it in this chapter. These are Lebesgue spaces of almost-everywhere equivalence classes.

For compact \(D\subset\mathbb R^n\), the real dual \(C(D;\mathbb R)^*\) is represented by signed regular Borel measures via \(F(f)=\int_Df\,d\mu\), isometrically. This measure-representation result is stated, not proved here; it is distinct from the Hilbert-space Riesz theorem of Chapter 2.

## Transporting a dual representation through an isomorphism

Using zero-based indexing, let \(a(x)=\lim_nx_n\) and
\(Tx=(a(x),x_0-a(x),x_1-a(x),\ldots)\), the bounded isomorphism \(c\to c_0\). Its inverse is \((Sy)_n=y_0+y_{n+1}\). If \(f_z(y)=\sum_{n\ge0}z_ny_n\), \(z\in\ell^1\), then
\[
(T^*f_z)(x)=a(x)\left(z_0-\sum_{n\ge0}z_{n+1}\right)
+\sum_{n\ge0}z_{n+1}x_n.
\]
All of \(c^*\) is represented this way because \(T^*\) is a bounded isomorphism, with inverse \(S^*\). This construction retains both the limit functional and the summable coordinate part; coordinate coefficients alone do not exhaust the dual of the convergent-sequence space in this form.

## Source references
Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`. Lecture notes are WS 2017/18; exercise/solution sheets are WS 2024/25.
- `Materials/Lecture notes.pdf`, Proposition 1.20/Eqs. (1.62)–(1.78), pp. 15–18.
- `Problem sheets/Problem Sheet 2.pdf`, T2.3, physical p. 1; `Solutions to problem sheets/Solutions Sheet 2.pdf`, T2.3, physical pp. 1–3.
- `Problem sheets/Problem Sheet 6.pdf` and `Solutions to problem sheets/Solutions Sheet 6.pdf`, A6.1 and A6.3.
- `Problem sheets/Problem Sheet 10.pdf` and `Solutions to problem sheets/Solutions Sheet 10.pdf`, T10.3(c).
