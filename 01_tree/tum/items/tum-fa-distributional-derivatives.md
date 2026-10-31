---
id: tum-fa-distributional-derivatives
source: tum-functional-analysis
parent: fa-sobolev-distributions
title: Distributional derivatives and integrable weak derivatives
type: concept
---

# Distributional derivatives and integrable weak derivatives

## Differentiation by duality

For \(f\in\mathcal D'(\mathbb R^d)\) and multi-index \(\alpha\), define
\[
(\partial^\alpha f)(\varphi)=(-1)^{|\alpha|}f(\partial^\alpha\varphi).
\]
It is again a distribution because differentiation of tests is continuous. Every distribution has derivatives of every order, and \(f_n\to f\) implies \(\partial^\alpha f_n\to\partial^\alpha f\), by evaluating the same derivative of each test.

For smooth \(u\), integration by parts with compactly supported \(\varphi\) gives \(\partial^\alpha T_u=T_{\partial^\alpha u}\). Thus the definition extends classical differentiation without requiring pointwise values for general distributions.

## Weak derivatives are regular distributional derivatives

If \(u,v\in L^1_{\mathrm{loc}}\), then \(v\) is the weak \(\alpha\)-derivative of \(u\) iff
\[
\partial^\alpha T_u=T_v
\quad\Longleftrightarrow\quad
\int v\varphi=(-1)^{|\alpha|}\int u\,\partial^\alpha\varphi
\quad(\varphi\in C_c^\infty).
\]
Uniqueness follows from uniqueness of regular densities. On an open domain the same definition uses tests supported inside that domain; no boundary term remains. Requiring both \(u\) and its weak derivatives in \(L^p\) leads to Sobolev spaces.

In one dimension, split integration at zero:
\[
-\int_{\mathbb R}|x|\varphi'(x)\,dx
=-\int_{-\infty}^0\varphi+\int_0^\infty\varphi
=\int_{\mathbb R}\operatorname{sign}(x)\varphi(x)\,dx.
\]
Consequently \(|x|\) has weak derivative \(\operatorname{sign}(x)\). A second differentiation gives
\[
\partial_xT_{\operatorname{sign}}(\varphi)
=-\int\operatorname{sign}(x)\varphi'(x)\,dx
=2\varphi(0)=2\delta_0(\varphi).
\]
This derivative exists as a distribution but has no locally integrable density. Distributional differentiability therefore does not imply weak differentiability by a function, even though the first derivative of \(|x|\) is bounded.

## Source references

Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`.
- `Materials/Distributions.pdf` (WS 2024/25), Sections 6–7, pp. 7–9; Definitions 4–5, Lemmas 6–10 and Examples 7–8.
- `Materials/Lecture notes.pdf` (WS 2017/18), pp. 59–60, Eqs. (7.1)–(7.5), Definition 7.1.
