---
id: tum-fa-normal-operators
source: tum-functional-analysis
parent: fa-spectral-theory
title: Normal, self-adjoint and positive Hilbert-space operators
type: theorem
---

# Normal, self-adjoint and positive Hilbert-space operators

## Algebra and norm identities

With inner product linear in the first argument, the Hilbert adjoint satisfies
\[
T^{**}=T,\quad\|T^*\|=\|T\|,\quad
(ST)^*=T^*S^*,\quad(\alpha T)^*=\overline\alpha T^*.
\]
An operator is normal if \(T^*T=TT^*\), self-adjoint (also called Hermitian over \(\mathbb C\)) if \(T=T^*\), and positive if \(\langle Tx,x\rangle\ge0\). Both \(T^*T\) and \(TT^*\) are positive self-adjoint, and
\[
\|T^*T\|=\|T\|^2.
\]
Indeed \(\langle T^*Tx,x\rangle=\|Tx\|^2\) gives one norm inequality, and submultiplicativity plus \(\|T^*\|=\|T\|\) gives the other.

Powers of normal \(T\) are normal and \(\|T^n\|=\|T\|^n\). Normality permits rearrangement of \(T,T^*\), yielding the identity first for squares and then the successive-power argument. In complex Hilbert space, the spectral-radius formula therefore gives \(r(T)=\|T\|\). This equality does not hold for all nonnormal operators.

## Kernels, eigenvectors and spectrum

For normal \(T\), \(\|Tx\|=\|T^*x\|\), so their kernels agree. The same applies to normal \(\lambda I-T\), hence
\[
Tx=\lambda x\iff T^*x=\overline\lambda x.
\]
If \(Tx=\lambda x\), \(Ty=\mu y\) and \(\lambda\ne\mu\), then
\(\lambda\langle x,y\rangle=\langle Tx,y\rangle=\langle x,T^*y\rangle=\mu\langle x,y\rangle\); different eigenspaces are orthogonal.

Normal operators have no residual spectrum: injectivity of \(\lambda I-T\) implies a zero adjoint kernel, hence **dense** range. It need not imply surjectivity. For self-adjoint \(T\) and \(\lambda=a+ib\), \(b\ne0\),
\[
\|(\lambda I-T)x\|^2=\|(T-aI)x\|^2+b^2\|x\|^2.
\]
The lower bound gives closed range and injectivity; normality gives dense range. Thus the map is onto and \(\sigma(T)\subset\mathbb R\). The exercise assumes compactness, but its estimate does not use it.

## Source references

Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`.
- `Materials/Lecture notes.pdf` (WS 2017/18), Proposition 13.1, Definition 13.2, Lemma 13.3, Proposition 13.4 and Lemmas 13.5–13.6, pp. 88–90.
- `Problem sheets/Problem Sheet 13.pdf` and `Solutions to problem sheets/Solutions Sheet 13.pdf`, T13.3 (WS 2024/25). Dense range, rather than surjectivity, is the conclusion of a zero range-orthogonal complement.
