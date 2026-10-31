---
id: tum-fa-hilbert-riesz
source: tum-functional-analysis
parent: fa-hilbert-spaces
title: Riesz representation of Hilbert-space functionals
type: theorem
caption: "Represents each continuous Hilbert-space functional by a unique vector, preserving norms and the complex conjugate-linear convention."
---

# Riesz representation of Hilbert-space functionals

## Representation and scalar convention

Let \(H\) be a real or complex Hilbert space, with inner product linear in the first argument. For each \(F\in H^*\), there is a unique \(h\in H\) with
\[
F(z)=\langle z,h\rangle,\qquad \|F\|=\|h\|.
\]
Thus \(J:h\mapsto\langle\,\cdot\,,h\rangle\) is bijective and isometric; over \(\mathbb C\) it is **conjugate linear**, \(J(\alpha h+\beta k)=\overline\alpha Jh+\overline\beta Jk\).

Cauchy–Schwarz bounds the functional by \(\|h\|\), and testing \(h/\|h\|\) gives equality when \(h\ne0\). For surjectivity, take nonzero \(F\), let \(U=\ker F\), and choose \(u\in U^\perp\) with \(F(u)=1\). Since \(z-F(z)u\in U\),
\[
\langle z,u\rangle=F(z)\|u\|^2,\qquad
h=u/\|u\|^2.
\]
Orthogonal decomposition ensures such \(u\) exists. Uniqueness follows by testing the difference of two representing vectors.

For \(H=L^2(D;\mathbb K)\), this gives
\(F(z)=\int_D z(t)\overline{h(t)}\,dt\).
The conjugate in this Hilbert representation differs from the coefficient convention \(F_a(z)=\int a z\) in the linear \(L^p\)-dual identification; both describe continuous linear functionals with consistent conventions. The Hilbert theorem is also distinct from representation of \(C(D;\mathbb R)^*\) by signed measures.

## Source references
Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`. Lecture notes are WS 2017/18; exercise/solution sheets are WS 2024/25.

- `Materials/Lecture notes.pdf`, Proposition 2.12 and its proof/application, pp. 25–26.
