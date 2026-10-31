---
id: tum-fa-quotient-spaces
source: tum-functional-analysis
parent: fa-normed-spaces
title: Quotient norms and factorization through kernels
type: theorem
caption: "Constructs complete quotient spaces and relates kernel factorization, closed-range isomorphisms and duals of subspaces and cokernels."
---

# Quotient norms and factorization through kernels

## Seminorm and quotient construction

A seminorm is absolutely homogeneous and subadditive but may vanish on nonzero vectors. If \(q\) is a seminorm on \(Y\) and \(T:X\to Y\) is linear, then \(q(Tx)\) is a seminorm on \(X\). Examples include \(|x_1|\), \(|f(a)|\), \(|\int f|\), and \(\|f'\|_\infty\) on their respective source spaces.

For a linear subspace \(U\subset X\), identify \(x\sim y\) when \(x-y\in U\). Set
\[
[x]=x+U,\quad Qx=[x],\quad
\|[x]\|_{X/U}=\inf_{u\in U}\|x-u\|\le\|x\|.
\]
This is well-defined and is always a seminorm. When \(U\) is closed it is a norm: distance zero implies \(x\in\overline U=U\). If \(X\) is Banach and \(U\) closed, the quotient is Banach.

**Completeness argument:** pass from a quotient-Cauchy sequence to a subsequence with successive quotient distances bounded by \(2^{-n}\). Choose representatives whose increments are at most twice those distances. The summable bound makes representatives Cauchy in \(X\); their ambient limit yields the quotient limit, and the original Cauchy sequence has the same limit. A zero quotient increment permits identical representatives.

For \(X=C([0,1])\) with sup norm and \(U=\{f:f(0)=0\}\), the quotient norm is \(|f(0)|\); evaluation identifies \(X/U\) isometrically with \(\mathbb K\).

## Kernel factorization and functionals

For bounded linear \(T:X\to Y\), the kernel is closed as \(T^{-1}(\{0\})\), and
\[
T_0:X/\ker T\to Y,\quad T_0[x]=Tx
\]
is well-defined, injective, bounded, with \(\|T_0\|=\|T\|\). Taking an infimum over representatives proves \(\|T_0\|\le\|T\|\); \(T=T_0Q\) and \(\|Q\|\le1\) give the reverse inequality. This does **not** assert that its inverse on the range is bounded.

For nonzero \(f\in X^*\), choose \(y\) with \(f(y)=1\). Every \(x\) has the unique decomposition
\[
x=(x-f(x)y)+f(x)y\in\ker f\oplus\operatorname{span}\{y\}.
\]
If two continuous linear functionals have the same kernel, they are proportional; if both vanish the assertion is trivial. Thus the kernel determines a nonzero functional up to a scalar, not its normalization.

## Dual of a subspace as a quotient

For a closed subspace \(U\subset X\), write \(U^\perp=\{f\in X^*:f|_U=0\}\) for its annihilator in the dual (not an inner-product orthogonal complement). Restriction \(R:X^*\to U^*\) has this kernel and is surjective by Hahn–Banach. It induces a linear isometric isomorphism
\[
X^*/U^\perp\cong U^*.
\]
Indeed, all extensions of \(u^*\) form one coset, and its quotient norm is the infimum of their norms, equal to \(\|u^*\|\) with attainment by Hahn–Banach. This sharpens generic kernel factorization: equality of operator norms alone would not prove this induced map is an isometry.

## Closed-range isomorphisms and the cokernel dual

More generally, if bounded \(T:X\to Y\) vanishes on closed \(U\), it factors uniquely through \(X/U\) with equal operator norm. For Banach \(X,Y\) and closed \(T(X)\), bounded inverse applied to the kernel quotient gives
\[
X/\ker T\simeq T(X).
\]
Surjectivity gives \(X/\ker T\simeq Y\). These are topological isomorphisms, not generally isometries. Closedness is what upgrades the earlier injective factorization to a boundedly invertible map onto the range.

For closed range, quotient composition \(g\mapsto gQ\) is an isometric isomorphism
\[
(Y/T(X))^*\cong\ker T^*.
\]
The functionals in the adjoint kernel are exactly those vanishing on the range, hence precisely those that descend to its quotient. This identifies the dual of the cokernel with the homogeneous adjoint solutions.

## Source references
Archive: `00_sources/raw/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`. Lecture notes are WS 2017/18; exercise/solution sheets are WS 2024/25.
- `Materials/Lecture notes.pdf`, Definition 1.13 and Proposition 1.14, pp. 12–14, including the evaluation quotient example.
- `Problem sheets/Problem Sheet 2.pdf` and `Solutions to problem sheets/Solutions Sheet 2.pdf`, T2.4 and A2.2.
- `Problem sheets/Problem Sheet 8.pdf` and `Solutions to problem sheets/Solutions Sheet 8.pdf`, T8.1.
- `Materials/Lecture notes.pdf`, Proposition 10.1 and Corollaries 10.2–10.3, pp. 73–74; Proposition 10.4, p. 74.
