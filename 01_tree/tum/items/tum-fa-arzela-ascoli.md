---
id: tum-fa-arzela-ascoli
source: tum-functional-analysis
parent: fa-weak-compactness
title: Arzelà–Ascoli compactness and continuous-kernel operators
type: theorem
---

# Arzelà–Ascoli compactness and continuous-kernel operators

## Criterion

Let \(K\subset\mathbb R^n\) be compact. A family \(F\subset C(K;\mathbb K)\) is relatively compact in the sup norm—its closure is compact—iff it is bounded and equicontinuous. Equicontinuity means: for each \(x\in K\) and \(\varepsilon>0\), a single \(\delta>0\) controls \(|f(x)-f(y)|<\varepsilon\) for every \(f\in F\) when \(y\in K\), \(\|x-y\|<\delta\).

A uniform Lipschitz constant suffices. On a convex domain, uniformly bounded first derivatives imply a uniform Lipschitz estimate by integrating along line segments. Domain geometry matters for that derivative argument; bounded derivatives on an arbitrary disconnected domain do not by themselves give a global Lipschitz bound.

The criterion concerns compactness of the **closure** of the family, not automatic closedness of the family itself.

## Continuous-kernel integral operator

For continuous \(k:[0,1]^2\to\mathbb R\), define
\[
(Tf)(x)=\int_0^1 k(x,t)f(t)\,dt
\]
on \(C([0,1])\). Continuity under the integral makes \(Tf\) continuous, and
\(\|Tf\|_\infty\le\|k\|_\infty\|f\|_\infty\).
The image of the unit ball is bounded. Uniform continuity of \(k\) also gives
\[
|Tf(x)-Tf(y)|\le\int_0^1|k(x,t)-k(y,t)|\,dt
\]
uniformly for \(\|f\|_\infty\le1\). Thus its closure is compact by Arzelà–Ascoli. This establishes compact-operator behavior through a function-family criterion, beyond a boundedness estimate alone.

## Source references
Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`. N = `Materials/Lecture notes.pdf` (WS 2017/18); E/S refer to `Problem sheets/Problem Sheet <n>.pdf` and `Solutions to problem sheets/Solutions Sheet <n>.pdf` (WS 2024/25).
- N, Definition 5.3, Lemma 5.4 and Proposition 5.5, pp. 46–47 (criterion stated without proof).
- E9/S9, T9.4.
