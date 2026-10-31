---
id: tum-fa-sobolev-compact-embedding
source: tum-functional-analysis
parent: fa-sobolev-distributions
title: Translation estimates and Rellich compact embedding
type: theorem
caption: "Uses gradient-controlled translations and extension operators to obtain strong subsequences from bounded Sobolev families on suitable bounded domains."
---

# Translation estimates and Rellich compact embedding

## Gradient control of translations

For \(u\in C_c^\infty(\Omega)\), extend by zero. With \(1\le p<\infty\) and conjugate \(q\), the fundamental theorem along the segment \(x+th\), followed by Hölder, gives
\[
u(x+h)-u(x)=\int_0^1\nabla u(x+th)\cdot h\,dt,
\qquad
\|u(\cdot+h)-u\|_{L^p(\mathbb R^d)}^p
\le\|\nabla u\|_{L^p(\mathbb R^d;\ell^p)}^p\|h\|_{\ell^q}^p.
\]
Integration over the whole space and translation invariance control the shifted gradient; the same bound holds when restricting the left side to \(\Omega\).

## Zero-boundary compactness

For **bounded open** \(\Omega\), a bounded \(F\subset W^{1,p}_0(\Omega)\) is relatively compact in \(L^p(\Omega)\). Given a sequence \(u_n\in F\), choose \(v_n\in C_c^\infty(\Omega)\) with \(\|u_n-v_n\|_{W^{1,p}}\le1/n\). The \(v_n\) have uniformly bounded gradients, so the translation estimate gives the uniform continuity criterion of Fréchet–Riesz–Kolmogorov. A strongly \(L^p\)-convergent subsequence of \(v_n\) gives the same limit for \(u_n\).

The bounded-domain condition is needed for this use of the preceding compactness theorem. Proposition 7.11 omits it in its printed statement; no unrestricted compact embedding on an unbounded domain follows from the translation estimate alone.

## Removing the zero-boundary restriction

If \(\Omega\) is bounded with sufficiently smooth boundary, the notes use a bounded linear extension
\[
E:W^{1,p}(\Omega)\longrightarrow W^{1,p}_0(V),
\qquad(Eu)|_\Omega=u,
\]
where \(\Omega\Subset V\) and \(V\) is bounded and open. Extension maps bounded sets to bounded sets; apply the zero-boundary result on \(V\), then restrict the strongly convergent subsequence to \(\Omega\). Thus bounded subsets of \(W^{1,p}(\Omega)\) are relatively compact in \(L^p(\Omega)\), \(1\le p<\infty\) (Rellich).

The extension's existence is cited, not constructed, and the notes do not specify a sharp boundary-regularity class. Compactness here gains strong convergence in a weaker norm; it does not assert compactness in the original Sobolev norm.

## Source references

Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`; `Materials/Lecture notes.pdf` (WS 2017/18).
- Lemma 7.10, Eqs. (7.24)–(7.25), pp. 63–64; Proposition 7.11 and Eq. (7.26), pp. 64–65; extension argument and Proposition 7.12 (Rellich), p. 65.
- Proposition 5.10, p. 50, supplies the bounded-domain compactness criterion used in this proof.
