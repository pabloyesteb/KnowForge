---
id: tum-fa-integral-operators
source: tum-functional-analysis
parent: fa-normed-spaces
title: Evaluation functionals and bounded integral operators
type: method
---

# Evaluation functionals and bounded integral operators

## Functionals and integral operators

For \(C(D)\) with the sup norm, evaluation \(f\mapsto f(a)\) has norm 1. Integration over \([a,b]\) has norm \(b-a\) in the sup norm, but norm 1 on \(L^1([a,b])\), assuming \(a<b\). A weighted functional on \(L^1\), \(f\mapsto\int h f\) with continuous \(h\), has norm \(\|h\|_\infty\): concentrated normalized indicator functions near a maximizer give the lower bound.

For \(k\in L^2((0,1)^2)\),
\[
(Tf)(s)=\int_0^1k(s,t)f(t)\,dt,\qquad \|T\|\le\|k\|_{L^2}.
\]
Fubini/Tonelli and Cauchy–Schwarz justify the definition almost everywhere and the bound. This estimate establishes boundedness; it does not establish compactness.


## Source references
Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`. Lecture notes are WS 2017/18; exercise/solution sheets are WS 2024/25.
- `Materials/Lecture notes.pdf`, Example 1.11(1)–(5), pp. 10–11.
