---
id: tum-uq-sobolev-framework
source: tum-numuq
parent: uq-pde
title: Weak derivatives, Sobolev norms and homogeneous boundary conditions
type: concept
caption: Provides the function spaces, Poincaré control and embedding hypotheses used by elliptic weak formulations.
---

# Weak derivatives, Sobolev norms and homogeneous boundary conditions

The weak derivative \(D^\alpha u\) satisfies \(\int D^\alpha u\,\phi=(-1)^{|\alpha|}\int uD^\alpha\phi\) for all compactly supported smooth test functions. The Sobolev space \(W^{r,p}(D)\) requires these derivatives through order \(r\) in \(L^p\), with norm \((\sum_{|\alpha|\le r}\|D^\alpha u\|_p^p)^{1/p}\). For \(p=2\), \(H^r\) is Hilbert with the derivative-sum inner product; its seminorm retains only derivatives of order \(r\).

The space \(H_0^1(D)\) is the closure of \(C_c^\infty(D)\) in \(H^1\), encoding homogeneous Dirichlet data. On a bounded domain, Poincaré gives \(\|u\|_{L^2}\le K_P|u|_{H^1}\), hence
\[
|u|_{H^1}\le\|u\|_{H^1}\le\sqrt{1+K_P^2}|u|_{H^1}\quad(u\in H_0^1).
\]
Thus the gradient seminorm is a full norm on this space. The course uses this norm when writing \(\|u\|_{H_0^1}\).

On domains with the regularity needed for Sobolev extension/embedding (as in the course's piecewise smooth or polygonal PDE setting), \(r>d/2\) yields a continuous representative and \(\|u\|_C\le K\|u\|_{H^r}\); \(r>s+d/2\) similarly yields \(C^s\) control. Mere boundedness of an arbitrary domain is insufficient for every global embedding assertion in the appendix. These hypotheses matter when interpreting pointwise quantities from weak solutions.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, appendix C, Definitions C.1, C.3–C.4 and C.6, Remark C.5 and Theorems C.7–C.9, pp. 100–102 before appendix D; use in §§5.1–5.2, pp. 44–45.
