---
id: tum-fa-sobolev-density
source: tum-functional-analysis
parent: fa-sobolev-distributions
title: Smooth approximation in Sobolev norms
type: method
---

# Smooth approximation in Sobolev norms

## Interior smoothing

Let \(u\in W^{k,p}(\Omega)\), \(1\le p<\infty\), and \(U\Subset\Omega\). For a standard mollifier with \(\varepsilon<\operatorname{dist}(U,\partial\Omega)\),
\[
\partial^\alpha(u*\eta_\varepsilon)
=(\partial^\alpha u)*\eta_\varepsilon\quad\text{on }U,
\qquad u*\eta_\varepsilon\to u\text{ in }W^{k,p}(U).
\]
The kernel is then a valid interior test; transferring its derivative to the weak derivative introduces no boundary term. Convergence follows from \(L^p\) approximation of each derivative. Arbitrary zero extension need not preserve Sobolev derivatives across the boundary, so this interior argument cannot simply set \(U=\Omega\).

On all of \(\mathbb R^d\) there is no boundary obstruction, giving global approximation in \(W^{k,p}(\mathbb R^d)\). The finite-exponent hypothesis is important: approximate identities do not converge in general \(L^\infty\) norm for discontinuous derivative densities. The supplement's Lemma 11 must be read with this restriction for its Sobolev-norm convergence conclusion.

## Arbitrary open domains

For every open \(\Omega\), \(C^\infty(\Omega)\cap W^{k,p}(\Omega)\) is dense in \(W^{k,p}(\Omega)\), \(p<\infty\). The construction handles different distances to the boundary:

1. Exhaust \(\Omega\) by \(U_j=\{x:\operatorname{dist}(x,\partial\Omega)>1/j,\ |x|<j\}\).
2. Choose a locally finite smooth partition of unity \(\beta_j\) on overlapping shells \(V_j=U_{j+3}\setminus\overline U_{j+1}\), together with the interior set \(V_0=U_3\).
3. Smooth each localized \(\beta_j u\) at an individual radius \(\varepsilon_j\), small enough to retain shell-local support and ensure
\[
\|w_j-\beta_j u\|_{W^{k,p}}\le2^{-(j+1)}\delta.
\]
4. Sum the locally finite family \(w=\sum_jw_j\). It is smooth and \(\|w-u\|_{W^{k,p}}\le\delta\).

The result gives smooth approximants, not necessarily compactly supported approximants. The latter closure defines the generally smaller \(W^{k,p}_0\). Distinguishing these two density claims preserves the boundary condition.

## Source references

Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`.
- `Materials/Lecture notes.pdf` (WS 2017/18), Lemma 7.5 and Eq. (7.15), Proposition 7.6 and Eqs. (7.16)–(7.19), pp. 62–63; Definition 7.7, p. 63.
- `Materials/Distributions.pdf` (WS 2024/25), Lemma 10, p. 9, and Lemma 11, p. 10.
