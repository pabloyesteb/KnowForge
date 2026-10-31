---
id: tum-fa-weak-convergence
source: tum-functional-analysis
parent: fa-weak-compactness
title: Weak and weak-star convergence through dual tests
type: concept
---

# Weak and weak-star convergence through dual tests

## Functional tests and topology

In a normed space \(X\), \(x_n\rightharpoonup x\) means \(f(x_n)\to f(x)\) for every \(f\in X^*\). In \(X^*\), weak-star convergence \(f_n\stackrel{*}{\rightharpoonup}f\) tests only evaluations at vectors of \(X\); weak convergence in \(X^*\) instead tests every member of \(X^{**}\). Norm convergence implies weak convergence, but not conversely.

A weakly convergent sequence is norm-bounded: apply uniform boundedness to \(J_Xx_n\) acting on the Banach space \(X^*\). For a bounded sequence, it suffices to test a norm-dense set \(D\subset X^*\). Indeed, with \(M=\sup_n\|x_n\|\),
\[
|g(x_n-x)|\le\|g-f\|(M+\|x\|)+|f(x_n-x)|,\qquad f\in D.
\]
Approximate \(g\) by \(f\), then pass to large \(n\). Without boundedness, dense testing is not justified by this estimate.

In Hilbert space, Riesz representation makes weak convergence equivalent to convergence of all inner products against fixed vectors. Weak convergence together with \(\|x_n\|\to\|x\|\) implies norm convergence by expanding
\(\|x_n-x\|^2=\|x_n\|^2+\|x\|^2-2\operatorname{Re}\langle x_n,x\rangle\).
An orthonormal sequence is weakly null by Bessel but has constant norm 1. Testing coordinates in an orthonormal basis suffices for weak-null convergence if the sequence is bounded.

## Products, subspaces and changes of variables

Weak and weak-star limits are unique: weak-star equality follows from evaluation on every vector, and weak equality from separation by the dual. In a reflexive space \(X\), weak and weak-star convergence in \(X^*\) coincide; in finite dimension these also coincide with norm convergence. Weak-star convergent sequences are norm-bounded when their predual \(X\) is Banach, by uniform boundedness.

For mixed limits, if \(x_n\to x\) in norm and \(f_n\stackrel{*}{\rightharpoonup}f\) with \(\sup_n\|f_n\|<\infty\), then
\[
|f_n(x_n)-f(x)|\le\|f_n\|\|x_n-x\|+|(f_n-f)(x)|\to0.
\]
The bound is automatic for a Banach predual, but cannot be dropped for a general incomplete predual: on \(c_e\) with sup norm, \(f_n(x)=nx_n\) is weak-star null and \(x^{(n)}=e_n/n\to0\), yet \(f_n(x^{(n)})=1\). This qualifies the unbounded-predual form of the notes' Lemma 6.5. If instead \(x_n\rightharpoonup x\) and \(f_n\to f\) in norm, boundedness of \(x_n\) gives pairing convergence. Two weak limits alone do not suffice: in \(\ell^2\), a coordinate vector paired with its own coordinate functional always gives 1 although both sequences are weakly null.

For the sum-norm product \(X\times Y\), each continuous functional decomposes uniquely as \(f(x)+g(y)\). Hence weak convergence is componentwise. For \(u_n,u\in U\subset X\), weak convergence in \(U\) agrees with weak convergence in \(X\): use restriction one way and Hahn–Banach extension the other. A bounded linear bijection between Banach spaces preserves weak convergence in both directions, since both it and its inverse are bounded.

## Examples distinguishing the limits

- In \(c_0\), the finite truncations of \((1,1/2,1/3,\ldots)\) converge in norm. The vectors \((n,n-1,\ldots,1,0,\ldots)\) do not even converge weakly because they are unbounded.
- Right shifts of \((1,1/2,1/3,\ldots)\) by \(n\) coordinates are weakly null in \(c_0\): each \(\ell^1\) coefficient functional is bounded by its own tail sum. Distinct shifts have distance 1, so norm convergence fails.
- The unit vectors of \(\ell^1\) have no weakly convergent subsequence. For any chosen subsequence \(e_{n_j}\), choose one bounded coefficient sequence taking values \((-1)^j\) on those indices; its functional prevents convergence. Boundedness alone does not supply weak subsequences.
- \(1_{[n-1,n]}\) is weak-star null in \(L^\infty(\mathbb R)=(L^1(\mathbb R))^*\), since its pairing with \(g\in L^1\) is bounded by \(\int_{n-1}^n|g|\to0\). The same functions form an orthonormal sequence in \(L^2(\mathbb R)\), hence are weakly null there.
- For \(1<p<\infty\), \(n^{1/p}1_{(0,1/n)}\) is weakly null in \(L^p(0,1)\) but has norm 1. Bounded continuous test functions give an integral bound \(\|g\|_\infty n^{1/p-1}\to0\); density in \(L^q\) and boundedness extend it to all dual tests.
- \(\sin(2\pi nt)\) is also weakly null in \(L^p(0,1)\), \(1<p<\infty\). First test continuous functions through the \(L^2\) orthonormal-system argument, then use density in \(L^q\). Its \(p\)-th norm power is the positive constant \(\int_0^1|\sin(2\pi t)|^pdt\); it is not norm-null. Weak and strong limits, when both exist, agree.

## Source references
Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`. N = `Materials/Lecture notes.pdf` (WS 2017/18); E/S refer to `Problem sheets/Problem Sheet <n>.pdf` and `Solutions to problem sheets/Solutions Sheet <n>.pdf` (WS 2024/25).
- E7/S7, T7.3–T7.4 and A7.2; E8/S8, T8.2–T8.4 and A8.1–A8.3.
- N, Definition 6.1 and Lemmas 6.2–6.5, pp. 51–53. Pairing convergence requires the uniform boundedness condition stated above.
