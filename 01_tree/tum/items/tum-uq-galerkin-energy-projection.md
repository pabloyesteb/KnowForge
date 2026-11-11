---
id: tum-uq-galerkin-energy-projection
source: tum-numuq
parent: uq-pde
title: Conforming Galerkin projection and coefficient-dependent quasi-optimality
type: theorem
caption: Uses energy orthogonality to derive best approximation and its pathwise random-coefficient counterpart.
---

# Conforming Galerkin projection and coefficient-dependent quasi-optimality

For the symmetric diffusion weak problem, choose a finite-dimensional conforming \(V_h\subset H_0^1(D)\) and solve \(A(u_h,v_h)=\ell(v_h)\) for every \(v_h\in V_h\). Coercivity gives uniqueness. The energy norm \(\|v\|_E=\sqrt{A(v,v)}\) satisfies
\[
\sqrt{a_{\min}}|v|_{H^1}\le\|v\|_E\le\sqrt{a_{\max}}|v|_{H^1}.
\]
Subtracting the continuous and discrete problems gives Galerkin orthogonality \(A(u-u_h,v_h)=0\). For any \(v_h\), write \(\|u-u_h\|_E^2=A(u-u_h,u-v_h)\), then use energy Cauchy–Schwarz. Consequently
\[
\|u-u_h\|_E=\inf_{v_h\in V_h}\|u-v_h\|_E,\qquad
|u-u_h|_{H^1}\le\sqrt{a_{\max}/a_{\min}}\inf_{v_h\in V_h}|u-v_h|_{H^1}.
\]
The square-root coefficient ratio uses symmetry and energy projection, rather than a generic nonsymmetric Céa estimate.

For random diffusion, apply the same argument at almost every outcome using \(a_{\min}(\omega),a_{\max}(\omega)\). The discrete solution satisfies the same pathwise stability bound as the exact solution and hence inherits its Bochner moment bound when \(a_{\min}^{-1}\in L^p\). The remaining best-approximation term is deterministic finite-element analysis for each realization. Converting it into a mesh rate requires additional solution regularity and interpolation estimates; coefficient positivity alone supplies no such rate. Section 6.3 uses a bounded convex polygon in two dimensions for this discussion.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, §5.2, Definition 5.6 and Theorems 5.7–5.8, pp. 45–46; §6.3 and Lemma 6.12, p. 50.
- `Lecture Topics and Slides/Lecture 09 (28.05.24)`, physical pp. 13–18; `Lecture Topics and Slides/Lecture 10 (04.06.24)`, physical pp. 15–17, corresponding discrete random problem (slide Lemma 6.11).
