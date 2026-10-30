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

For open \(D\subset\mathbb R^n\), the notes state
\[
(L^p(D))^*\cong L^q(D)\quad(1<p<\infty),\qquad
(L^1(D))^*\cong L^\infty(D),
\]
through \(F_h(f)=\int_Dhf\). Hölder establishes boundedness; the \(1<p<\infty\) surjectivity sketch invokes Radon–Nikodym, rather than proving it in this chapter. These are Lebesgue spaces of almost-everywhere equivalence classes.

For compact \(D\subset\mathbb R^n\), the real dual \(C(D;\mathbb R)^*\) is represented by signed regular Borel measures via \(F(f)=\int_Df\,d\mu\), isometrically. This measure-representation result is stated, not proved here; it is distinct from the Hilbert-space Riesz theorem of Chapter 2.

## Source references
Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`. Lecture notes are WS 2017/18; exercise/solution sheets are WS 2024/25.
- `Materials/Lecture notes.pdf`, Proposition 1.20/Eqs. (1.62)–(1.78), pp. 15–18.
- `Problem sheets/Problem Sheet 2.pdf`, T2.3, physical p. 1; `Solutions to problem sheets/Solutions Sheet 2.pdf`, T2.3, physical pp. 1–3.
