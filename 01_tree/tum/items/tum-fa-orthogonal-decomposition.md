---
id: tum-fa-orthogonal-decomposition
source: tum-functional-analysis
parent: fa-hilbert-spaces
title: Orthogonal complements, subspace projections and total sets
type: theorem
---

# Orthogonal complements, subspace projections and total sets

## Orthogonal decomposition

For \(Y\subset H\), set \(Y^\perp=\{x:\langle x,y\rangle=0\ \forall y\in Y\}\). It is a closed linear subspace. Inclusion reverses under orthogonal complements, and
\[
Y^\perp=(\operatorname{span}Y)^\perp
=(\overline{\operatorname{span}Y})^\perp,\qquad
Y^{\perp\perp}=\overline{\operatorname{span}Y}.
\]
The last equality uses Hilbert-space completeness; the first properties follow from linearity and continuity of the product.

For a closed subspace \(U\subset H\), \(y=P_Ux\) is characterized by \(y\in U\) and \(x-y\perp U\). The convex-projection variational inequality becomes equality by testing both signs and, over \(\mathbb C\), imaginary multiples. Uniqueness gives linearity of \(P_U\) and
\[
H=U\oplus U^\perp,\quad \ker P_U=U^\perp,\quad
P_{U^\perp}=I-P_U,\quad
\|x\|^2=\|P_Ux\|^2+\|x-P_Ux\|^2.
\]
Consequently \(x\mapsto(P_Ux,x-P_Ux)\) is an isometric isomorphism onto the product with its Euclidean product norm, and \(\|P_U\|=1\) for \(U\ne\{0\}\).

A bounded \(P:H\to H\) is such an orthogonal projection exactly when
\[
P^2=P,\qquad \langle x,Py\rangle=\langle Px,y\rangle.
\]
Indeed \(\ker P=\operatorname{ran}(I-P)\); symmetry makes \(\operatorname{ran}P\) orthogonal to that kernel, yielding the decomposition. Conversely the orthogonal decomposition gives idempotence and symmetry.

## Totality does not mean a basis

A set is total when \(Y^\perp=\{0\}\), equivalently its linear span is dense in a Hilbert space. In \(\ell^2\), let \(d=(1,1/2,1/3,\ldots)\) and \(Y=\{e_n:n\ge1\}\cup\{d\}\). Removing any one member leaves a total set: if \(e_j\) is removed, orthogonality to all remaining coordinates leaves only the \(j\)-coordinate, then orthogonality to \(d\) kills it. Removing two members destroys totality: two omitted coordinate directions admit a nonzero combination orthogonal to \(d\), or removing \(d,e_j\) leaves \(e_j\) orthogonal.

The ambient space matters. Let
\(Y=\{y\in c_e:\sum_n y_n/n=0\}\).
Its orthogonal complement inside the incomplete pre-Hilbert space \(c_e\) is zero: finite-support test vectors force every coordinate of a finite-support orthogonal vector to vanish. In \(\ell^2\), however, the nonzero vector \(d\) lies in \(Y^\perp\). One cannot apply Hilbert double-complement conclusions indiscriminately in an incomplete space.

## Source references
Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`. Lecture notes are WS 2017/18; exercise/solution sheets are WS 2024/25.

- `Materials/Lecture notes.pdf`, Corollary 2.7, Definition 2.8, Lemma 2.9, Proposition 2.10 and Lemma 2.11, pp. 23–25.
- `Problem sheets/Problem Sheet 4.pdf` and `Solutions to problem sheets/Solutions Sheet 4.pdf`, T4.2, T4.4, A4.3–A4.4.
