---
id: tum-fa-fredholm-alternative
source: tum-functional-analysis
parent: fa-compact-fredholm
title: Fredholm operators, index stability and compatibility conditions
type: theorem
caption: "Relates finite-dimensional defects and index stability to solvability and adjoint compatibility for identity-minus-compact equations."
---

# Fredholm operators, index stability and compatibility conditions

## Kernel, cokernel and index

For Banach spaces \(X,Y\), bounded \(T:X\to Y\) is Fredholm if
\(\dim\ker T<\infty\) and \(\dim(Y/T(X))<\infty\). Its range is then closed, and
\[
\operatorname{ind}T=\dim\ker T-\operatorname{codim}T(X).
\]
Finite algebraic codimension of a bounded Banach-space operator's range already forces closedness: first divide by the closed kernel, then adjoin finitely many missing range directions to obtain a bounded bijection from a Banach product onto \(Y\). Its bounded inverse identifies the original range as a closed subspace. In finite dimensions the index is simply \(\dim X-\dim Y\), independent of the particular map.

Differentiation \(D:C^1([0,1])\to C([0,1])\), with \(\|f\|_\infty+\|f'\|_\infty\) on the domain, has constant kernel, surjective range and index 1. Restricting the domain to \(f(0)=f(1)\) keeps the one-dimensional kernel but restricts the range to \(\{g:\int_0^1g=0\}\); its cokernel has dimension 1 and the index is 0.

Powers of shifts provide explicit indices on \(\ell^2\): the left shift by two has two-dimensional kernel and is onto, so its index is 2; the right shift by five has zero kernel and range of codimension 5, so its index is \(-5\).

## Identity minus a compact map

For compact \(S:X\to X\), \(I-S\) is Fredholm. On its kernel, the identity agrees with compact \(S\), forcing finite dimension. Choose a closed complement \(V\) of the kernel. If the inverse of \((I-S)|_V\) were unbounded, there would be unit \(v_n\in V\) with \((I-S)v_n\to0\). A convergent subsequence of \(Sv_n\) then forces \(v_n\) to converge to a unit vector in \(V\cap\ker(I-S)\), a contradiction. The inverse is bounded, so the range is complete and closed. Compactness of \(S^*\), together with
\[
(X/\operatorname{ran}(I-S))^*\cong\ker(I-S^*),
\]
gives finite codimension.

## Stability of the index

Fredholm operators form an open set in operator norm; their index is locally constant. Split \(X=\ker T\oplus V\), \(Y=T(X)\oplus W\), with the defect spaces finite-dimensional. The map \((v,w)\mapsto Tv+w\) is invertible. Small perturbations \((v,w)\mapsto Av+w\) remain invertible by the Neumann perturbation argument. Comparing the remaining finite-dimensional kernel and range directions shows \(\operatorname{ind}A=\operatorname{ind}T\).

Consequently the index is constant along continuous Fredholm paths. The path \(I-tS\), \(0\le t\le1\), consists of Fredholm operators and starts at index 0. Therefore \(\operatorname{ind}(I-S)=0\).

## Solvability alternative

For a Fredholm map \(T:X\to X\) of index 0, injectivity is equivalent to surjectivity. Either every \(Tx=y\) has a unique solution, or the homogeneous problem has a nonzero finite-dimensional solution space and
\[
Tx=y\text{ is solvable}\iff y^*(y)=0\quad\forall y^*\in\ker T^*.
\]
In the second case \(\dim\ker T=\dim\ker T^*\), and all solutions, when they exist, differ by \(\ker T\). These compatibility conditions use closedness of the range; annihilating the adjoint kernel would otherwise characterize only the range closure.

## Source references

Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`.
- `Materials/Lecture notes.pdf` (WS 2017/18), Proposition 10.9, p. 76; Chapter 11, pp. 77–80, Definition 11.1, Lemma 11.2, Propositions 11.3/11.6 and Corollaries 11.7–11.8.
- `Problem sheets/Problem Sheet 12.pdf` and `Solutions to problem sheets/Solutions Sheet 12.pdf` (WS 2024/25), T12.1.
- `Mock Exam/Mock Exam.pdf` and `Mock Exam/Solutions to Mock Exam.pdf`, P.1(e).
