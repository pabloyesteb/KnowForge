---
id: tum-nloa-multiplier-sets
source: tum-nonlinear-optimization
parent: nloa-cq-kkt
title: Boundedness, nonuniqueness and strict complementarity of KKT multipliers
type: theorem
---

# Boundedness, nonuniqueness and strict complementarity of KKT multipliers

## Closedness and MFCQ boundedness

At a fixed KKT point \(\bar x\), the multiplier set \(M(\bar x)\) consists of all \((\lambda,\mu)\) satisfying stationarity, nonnegativity and complementarity there. It is closed by continuity of those finite-dimensional conditions.

If its elements had unbounded norm, normalize a sequence and take a unit-norm subsequential limit \((\widehat\lambda,\widehat\mu)\). Dividing stationarity by the diverging norm removes the objective gradient, leaving
\[
\widehat\lambda\ge0,\quad g(\bar x)^T\widehat\lambda=0,\quad
\nabla g(\bar x)\widehat\lambda+\nabla h(\bar x)\widehat\mu=0.
\]
Under full-rank MFCQ, pairing with its strict feasible direction forces every active \(\widehat\lambda_i=0\); inactive components are already zero. Independence of equality gradients then forces \(\widehat\mu=0\), contradicting unit norm. Thus \(M(\bar x)\) is bounded, and closedness makes it compact. This does not imply uniqueness.

## A full multiplier segment

Consider
\[
f(x)=(4-x_1)^2+x_2^4,
\quad g_1=(x_1-1)^2+(x_2-1)^2-2,
\quad g_2=(x_1-1)^2+(x_2+1)^2-2,
\quad g_3=x_1-2.
\]
At \(\bar x=(2,0)\), all three inequalities are active, with gradients \((2,-2)^T,(2,2)^T,(1,0)^T\). The direction \((-1,0)^T\) establishes MFCQ. Stationarity with \(\nabla f(\bar x)=(-4,0)^T\) gives
\[
M(\bar x)=\{(t,t,4(1-t))^T:0\le t\le1\}.
\]
The specified multiplier \((1,1,0)\) violates strict complementarity because the third active multiplier vanishes. For \(0<t<1\), all three are positive. The qualification holds and the set is bounded, yet multipliers are not unique and strict complementarity depends on the chosen triple.

## LICQ gives uniqueness

LICQ means that the active inequality gradients together with the equality gradients are linearly independent. At a fixed KKT point let \(A_*=(\nabla g_A(\bar x),\nabla h(\bar x))\). Subtracting two stationarity equations and using zero inactive multipliers gives \(A_*\Delta(\lambda_A,\mu)=0\); independence forces equality of the multipliers. Equivalently, the existing KKT multipliers are
\[
\begin{pmatrix}\lambda_A\\\mu\end{pmatrix}
=-(A_*^TA_*)^{-1}A_*^T\nabla f(\bar x),\qquad\lambda_I=0.
\]
This is a uniqueness formula conditional on a KKT point, not a guarantee that the formula at an arbitrary feasible point produces nonnegative multipliers. LICQ is stronger information than MFCQ boundedness.

For the separate disk-constrained example \(\min x_1^3\) subject to \(x_1^2+x_2^2-1\le0\), at \((-1,0)\) stationarity is \((3,0)^T+\lambda(-2,0)^T=0\). It forces the unique multiplier \(\lambda=3/2>0\); strict complementarity holds. This contrasts with the multiplier segment above, where some triples have zero active multipliers.

## Source references

Archive: `00_sources/raw/tum/archives/NLOA (W24_25)_20261012_1553.zip`.
- `Exercise materials/Exercise Sheet 3.pdf`, H.3.2, p. 1, and T.3.6, p. 2.
- `Exercise materials/Solution Exercise Sheet 3.pdf`, Solution 3.2, pp. 1–2, and Solution 3.6, pp. 5–6.
- `Exercise materials/Exercise Sheet 4.pdf`, H.4.1(b), p. 1; `Exercise materials/Solution Exercise Sheet 4.pdf`, Solution 4.1(b), pp. 1–2.
- `Exercise materials/Exercise Sheet 7.pdf`, H.7.2(a), p. 1; `Exercise materials/Solution Exercise Sheet 7.pdf`, Solution 7.2(a), pp. 2–3.
