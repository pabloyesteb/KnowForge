---
id: tum-fa-weak-compactness
source: tum-functional-analysis
parent: fa-weak-compactness
title: Weak and weak-star compactness and subsequence extraction
type: theorem
caption: "Separates weak-star topological compactness from sequential results and derives subsequence extraction using separability or reflexivity."
---

# Weak and weak-star compactness and subsequence extraction

## Separable preduals: a diagonal argument

If \(X\) is a separable normed space, the closed unit ball of \(X^*\) is weak-star **sequentially** compact. For a sequence \(\|f_n\|\le1\), choose successive subsequences whose evaluations converge at the first, second and subsequent members of a countable dense set \(\{x_m\}\). A diagonal subsequence converges on their span. Its limit is linear with \(|f(x)|\le\|x\|\); extend it continuously to \(X\). The bound
\[
|f(x)-f_{n_k}(x)|\le2\|x-z\|+|f(z)-f_{n_k}(z)|
\]
for dense-span \(z\) proves convergence at every \(x\). Thus every bounded sequence in \(X^*\) has a weak-star convergent subsequence.

For Lebesgue \(L^p(D)\), \(1<p\le\infty\), use the separable predual \(L^q(D)\), \(q=p/(p-1)<\infty\). Bounded sequences admit subsequences whose pairings converge against all \(L^q\) tests; the \(p=\infty\) conclusion is weak-star, not an unrestricted weak-convergence statement.

On \(C([a,b])^*\), moving point evaluations have weak-star limits along convergent point subsequences. More generally, probability measures on the compact interval have a subsequence converging on all continuous test functions to a probability measure; positivity and unit mass pass to the limit.

## Reflexive spaces

In a reflexive Banach space, the closed unit ball is weakly sequentially compact; every bounded sequence therefore has a weakly convergent subsequence. For a proof without global separability, restrict to the closed span \(Y\) of the given sequence. It is separable and reflexive. Since \(Y^{**}\cong Y\) is separable, dual separability implies \(Y^*\) separable. Apply the preceding diagonal result to \(J_Yx_n\in(Y^*)^*\), then use reflexivity to identify its limit with a vector in \(Y\). Restriction of \(X^*\) tests yields weak convergence in \(X\).

The converse—that weak sequential compactness of the unit ball implies reflexivity—is stated in the notes without proof.

## Topological compactness is different

Banach–Alaoglu gives weak-star compactness of the dual unit ball for every normed \(X\), without separability. This is open-cover compactness in the weak-star topology. It need not imply sequential compactness; a general weak-star compact dual ball is not necessarily metrizable.

For \(X=L^\infty(0,1)\), define
\[
f_n(g)=\varepsilon_n^{-1}\int_0^{\varepsilon_n}g(t)\,dt,\qquad
\varepsilon_n\downarrow0,\quad\varepsilon_{n+1}/\varepsilon_n\to0.
\]
These norm-one functionals have no weak-star convergent subsequence in \(X^*\): for any subsequence, choose bounded \(g\) alternating on successive selected annuli. Its selected averages approach alternating signs, since the inner interval's relative contribution tends to zero. On the smaller test space \(C([0,1])\), however, the same averages converge to \(g(0)\), hence weak-star to \(\delta_0\). The predual/test space is essential to the meaning of the limit.

## Source references
Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`. N = `Materials/Lecture notes.pdf` (WS 2017/18); E/S refer to `Problem sheets/Problem Sheet <n>.pdf` and `Solutions to problem sheets/Solutions Sheet <n>.pdf` (WS 2024/25).
- N, Definition 6.7, Proposition 6.8, Corollary 6.9 and examples, pp. 54–55; Lemma 6.10, Proposition 6.11, Corollary 6.12 and Alaoglu Proposition 6.13, pp. 55–57.
