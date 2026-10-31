---
id: tum-fa-separable-embeddings
source: tum-functional-analysis
parent: fa-fundamental-principles
title: Countable norming families and separable-space embeddings
type: method
caption: "Constructs countable norming families and closed embeddings into bounded sequences, and proves that dual separability implies separability."
---

# Countable norming families and separable-space embeddings

## Embedding into bounded sequences

For a nonzero separable Banach space \(X\), choose a countable dense set \(\{x_n\}\) and Hahn–Banach norming functionals \(f_n\in X^*\) with \(\|f_n\|=1\), \(f_n(x_n)=\|x_n\|\). Then
\[
Tx=(f_n(x))_n\in\ell^\infty,\qquad \|Tx\|_\infty=\|x\|.
\]
The upper bound follows from the norms of \(f_n\). Choosing \(x_n\) within \(\varepsilon\) of \(x\) gives
\[
|f_n(x)|\ge\|x_n\|-\|x-x_n\|\ge\|x\|-2\varepsilon.
\]
Thus \(T\) is a linear isometry. Completeness of \(X\) makes \(T(X)\) closed in \(\ell^\infty\). This realizes arbitrary separable Banach geometry inside bounded sequences without asserting that \(\ell^\infty\) is separable.

## Separability of the dual implies separability of the space

If \(X^*\) is norm-separable, its unit sphere has a countable dense family \(\{f_n\}\). Choose unit \(x_n\) with \(|f_n(x_n)|\ge1/2\). A norm-one functional vanishing on \(U=\operatorname{span}\{x_n\}\) could be approximated within \(1/4\) by some \(f_j\), contradicting \(|f_j(x_j)|\ge1/2\). The Hahn–Banach annihilator criterion therefore gives \(\overline U=X\); rational finite combinations make \(X\) separable. Complex spaces use rational real and imaginary coefficients. The zero space is immediate.

The auxiliary metric fact is that every subset of a separable metric space is separable: choose representatives from a countable family of balls meeting that subset. The converse implication \(X\) separable \(\Rightarrow X^*\) separable does not follow; \(X=\ell^1\), \(X^*=\ell^\infty\) is a counterexample.

## Source references
Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`. N = `Materials/Lecture notes.pdf` (WS 2017/18); E/S refer to `Problem sheets/Problem Sheet <n>.pdf` and `Solutions to problem sheets/Solutions Sheet <n>.pdf` (WS 2024/25).
- E6/S6, T6.3 and A6.2.
- N, Lemma 6.10, pp. 55–56, for dual separability implying separability.
