---
id: tum-fa-mollification
source: tum-functional-analysis
parent: fa-weak-compactness
title: Convolution, mollification and translation continuity
type: method
caption: "Constructs smooth approximate identities, establishes finite-exponent approximation and translation continuity, and qualifies convolution differentiation."
---

# Convolution, mollification and translation continuity

## Smooth approximation

For \(f,g\in L^1(\mathbb R^n)\),
\[
(f*g)(y)=\int_{\mathbb R^n}f(x)g(y-x)\,dx,\qquad
f*g=g*f,\qquad \|f*g\|_1\le\|f\|_1\|g\|_1.
\]
Choose a nonnegative radial \(C^\infty\) kernel \(\eta\), supported in the closed unit ball, with integral 1; the notes construct it by normalizing
\(\exp[-1/(1-\|x\|^2)]\) inside that ball and zero outside. Set
\(\eta_\varepsilon(x)=\varepsilon^{-n}\eta(x/\varepsilon)\).

For bounded open \(\Omega\subset\mathbb R^n\) and \(f\in L^p(\Omega)\), \(1\le p<\infty\), extend \(f\) by zero to \(\tilde f\) and set \(f^\varepsilon=\tilde f*\eta_\varepsilon\). Differentiating the smooth kernel under the integral gives smoothness and
\[
\partial^\alpha f^\varepsilon=\tilde f*(\partial^\alpha\eta_\varepsilon).
\]
The support stays within distance \(\varepsilon\) of \(\overline\Omega\); the smoothed function is not in general supported inside \(\Omega\). Nonnegativity, unit mass, Hölder/Jensen and Fubini give
\(\|f^\varepsilon\|_{L^p(\Omega)}\le\|f\|_{L^p(\Omega)}\).

## Approximation and translations

For compactly supported continuous functions on \(\mathbb R^n\), uniform continuity bounds
\[
|f^\varepsilon(y)-f(y)|
\le\sup_{\|x-y\|\le\varepsilon}|f(x)-f(y)|\to0
\]
uniformly. For \(L^p\) functions, dense continuous approximants and the convolution norm bound yield \(f^\varepsilon\to f\) in \(L^p\). The finite-exponent restriction is substantive; uniform approximation of discontinuities is not implied.

For the zero extension and \(\tau_hf(x)=f(x+h)\), translation is continuous in \(L^p\), \(p<\infty\): insert a smooth approximation between \(\tau_hf\) and \(f\), control the two approximation errors, then use uniform continuity of the smooth function. Continuity for one \(f\) does not imply uniform continuity across every bounded family of functions.

## Differentiating convolution

In one dimension, for \(f\in L^1(\mathbb R)\) and differentiable \(g\) with bounded derivative, wherever the convolution is well-defined,
\[
(f*g)'=f*g'.
\]
The difference quotient of \(g\) is bounded by \(\|g'\|_\infty\), so dominated convergence applies with majorant \(|f|\|g'\|_\infty\). Existence of \(f*g\) remains an assumption: bounded \(g'\) alone permits an unbounded \(g\); bounded \(g\), for example, supplies existence for every \(L^1\) input.

## Source references
Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`. N = `Materials/Lecture notes.pdf` (WS 2017/18); E/S refer to `Problem sheets/Problem Sheet <n>.pdf` and `Solutions to problem sheets/Solutions Sheet <n>.pdf` (WS 2024/25).
- N, Eqs. (5.3)–(5.12), Lemmas 5.6–5.8 and Proposition 5.9, pp. 47–50.
- E9/S9, A9.1.
