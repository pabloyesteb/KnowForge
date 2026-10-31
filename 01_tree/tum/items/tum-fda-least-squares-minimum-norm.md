---
id: tum-fda-least-squares-minimum-norm
source: tum-foundations-data-analysis
parent: fda-svd
title: Minimum-norm least-squares solutions through the pseudoinverse
type: method
caption: "Projects inconsistent data onto the range and selects the least-norm input by removing kernel components."
---

# Minimum-norm least-squares solutions through the pseudoinverse

For a real matrix \(A\in\mathbb R^{m\times n}\), solving \(Ax=y\) raises two distinct issues. If \(y\notin\operatorname{range}A\), no exact solution exists. If the data are in the range but \(\ker A\ne\{0\}\), every \(x_0+w\), \(w\in\ker A\), is another solution. Rectangular shape suggests overdetermination or underdetermination but does not replace the actual rank tests.

The Moore–Penrose choice
\[
x^\dagger=A^\dagger y=\sum_{i=1}^r\frac{\langle y,u_i\rangle}{\sigma_i}v_i
\]
solves both problems geometrically:
\[
Ax^\dagger=\sum_{i=1}^r\langle y,u_i\rangle u_i=P_{\operatorname{range}A}y,
\qquad x^\dagger\perp\ker A.
\]
The output is the closest attainable output, so \(x^\dagger\) minimizes \(\|Ax-y\|_2\). Every other least-squares solution differs from it by a kernel vector. Orthogonality then gives
\[
\|x^\dagger+w\|_2^2=\|x^\dagger\|_2^2+\|w\|_2^2,
\]
so it is the unique minimum-norm solution among the least-squares minimizers. When \(y\) is attainable, this is the minimum-norm exact solution; otherwise it discards the unattainable output component. Not belonging to the range is different from being perpendicular to it.

The review uses a rank-two matrix with rows \((0,1/\sqrt2,1/\sqrt2)\), \((2,0,0)\), \((0,0,0)\). Its kernel is spanned by \((0,1,-1)^T\). For \(y=(1,2,0)^T\), the pseudoinverse returns \((1,1/\sqrt2,1/\sqrt2)^T\), eliminating the kernel part from other exact inputs. Adding \((0,0,1)^T\) to the data leaves this input unchanged, because that component is perpendicular to the range. Purely perpendicular data give the minimum-norm input zero.

## Source references

Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
- `3. Juni - 9. Juni/All you ... math 7`, single physical page, “Moore–Penrose Pseudo-Inverse”: inconsistent/nonunique systems, full-rank and rank-two examples, kernel removal, minimum norm and combined attainable/unattainable data.
