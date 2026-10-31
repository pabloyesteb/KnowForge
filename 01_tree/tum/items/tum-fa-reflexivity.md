---
id: tum-fa-reflexivity
source: tum-functional-analysis
parent: fa-fundamental-principles
title: Canonical bidual embedding, reflexivity and norm attainment
type: theorem
caption: "Studies the canonical bidual embedding, stability of reflexivity and norm attainment, with explicit nonreflexive sequence and function spaces."
---

# Canonical bidual embedding, reflexivity and norm attainment

## Canonical embedding

The map \(J_X:X\to X^{**}\), \((J_Xx)(f)=f(x)\), is linear and isometric by the dual norm formula. Since \(X^{**}\) is Banach, \(J_X(X)\) is closed exactly when \(X\) is complete; its closure supplies a completion otherwise. A Banach space is reflexive when this **canonical** map is surjective. An arbitrary isometric isomorphism \(X\cong X^{**}\) is not sufficient to establish canonical surjectivity.

Finite-dimensional spaces are reflexive by equality of dimensions. Hilbert spaces are reflexive by Riesz representation. With the first-argument-linear convention, for \(\Phi\in H^{**}\) and the conjugate-linear Riesz map \(R\), the functional
\(y\mapsto\overline{\Phi(Ry)}\) is linear; represent it by a vector \(x\) to obtain \(\Phi(Ry)=(Ry)(x)\). Surjectivity of \(R\) proves \(\Phi=J_Hx\).

The coefficient duality \((\ell^p)^*\cong\ell^q\) proves reflexivity for \(1<p<\infty\): composition of a bidual element with the coefficient map is a functional on \(\ell^q\), hence is evaluation by some \(x\in\ell^p\). The same reasoning applies to Lebesgue \(L^p(D)\) in this exponent range.

## Stability properties

Closed subspaces of reflexive Banach spaces are reflexive. Given \(\phi\in U^{**}\), define \(\Phi(f)=\phi(f|_U)\) on \(X^*\) and write \(\Phi=J_Xx\). All functionals annihilating \(U\) vanish on \(x\), so Hahn–Banach separation implies \(x\in U\). Extending each \(u^*\in U^*\) to \(X\) then proves \(\phi=J_Ux\).

For Banach \(X\), \(X\) is reflexive iff \(X^*\) is reflexive. Forward, for \(\Psi\in X^{***}\), take \(f=\Psi\circ J_X\); surjectivity of \(J_X\) gives \(\Psi=J_{X^*}f\). Reverse, \(X^{**}\) is reflexive and its closed subspace \(J_X(X)\) is reflexive.

## Explicit failures and norm attainment

Under \((c_0)^*\cong\ell^1\), the bidual functional \(F(f_a)=\sum_n a_n\) is bounded but cannot equal evaluation at any \(x\in c_0\): testing \(a=e_n\) forces \(x_n=1\) for every \(n\). Thus \(c_0\) is not reflexive, and dual reflexivity also excludes \(\ell^1\) and \(\ell^\infty\).

For a nonzero reflexive \(X\), every \(f\in X^*\) attains its norm on a unit vector. Apply the norming-functional corollary to \(f\) in \(X^*\), then use canonical surjectivity to represent that bidual functional by a unit \(x\). On \(c_0\), choose strictly positive summable coefficients \(a_n=2^{-n}\), \(n\ge1\). Then \(f_a(x)=\sum a_nx_n\) has norm 1 but no unit \(x\in c_0\) attains it: some positive-weight coordinate satisfies \(|x_n|<1\), so \(|f_a(x)|<1\). Positivity on all coordinates is important; not every functional on \(c_0\) fails to attain its norm.

The notes also show \(L^1(0,1)\) is not reflexive. In \(L^\infty(0,1)\), let \(U\) be the norm closure of functions vanishing on some \((0,1/k)\). The constant 1 stays at distance 1 from \(U\). Hahn–Banach gives \(F\in(L^\infty)^*\) vanishing on \(U\) but not at 1. An integral representation \(F(g)=\int h g\), \(h\in L^1\), would force \(F(1)=0\) by dominated convergence along \(1_{(1/k,1)}\), a contradiction.

A second obstruction for \(\ell^1\) uses weak compactness: its unit vectors are bounded but no subsequence is weakly convergent. For any selected indices \(n_k\), a bounded dual coefficient sequence with values \((-1)^k\) at those indices prevents convergence of that one dual pairing. A reflexive Banach space would supply a weakly convergent subsequence, so \(\ell^1\) is not reflexive.

## Source references
Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`. N = `Materials/Lecture notes.pdf` (WS 2017/18); E/S refer to `Problem sheets/Problem Sheet <n>.pdf` and `Solutions to problem sheets/Solutions Sheet <n>.pdf` (WS 2024/25).
- N, Lemma 4.9, Definition 4.10, Propositions 4.11–4.14, pp. 40–43.
- E6/S6, T6.4–T6.5. The nonattainment example uses strictly positive coefficients rather than the solution's overgeneral statement for arbitrary coefficients.
- `Mock Exam/Mock Exam.pdf` and `Mock Exam/Solutions to Mock Exam.pdf`, P.5.
