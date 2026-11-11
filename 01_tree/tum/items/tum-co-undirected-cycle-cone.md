---
id: tum-co-undirected-cycle-cone
source: tum-combinatorial-optimization
parent: co-general-matching
title: Cycle-cone formulation of minimum mean undirected cycles
type: method
caption: "Normalizes nonnegative cycle combinations so linear cost minimization yields minimum cycle mean."
---

# Cycle-cone formulation of minimum mean undirected cycles

The cycle cone of an undirected graph is \(C(G)=\operatorname{pos}\{\mathbf1_C:C\text{ is a cycle}\}\). The notes state, without proving sufficiency, its cut characterization:
\[
x_e\ge0,\qquad x(\delta(S))\ge2x_e\quad(S\subseteq V,\ e\in\delta(S)).
\]
Necessity follows because a cycle crossing a cut on one edge must cross it on another. These are weighted cut-balance constraints, not solely degree constraints. Add \(\sum_ex_e=1\) and minimize \(\sum_ec(e)x_e\). A normalized cycle is feasible, and for a nonzero cone decomposition \(x=\sum_i\lambda_i\mathbf1_{C_i}\), its objective ratio is a weighted average of cycle means, with positive weights \(\lambda_i|C_i|\). Some component cycle is at least as good as the vector; for an optimal vector, every positively weighted component is minimum mean. Zero coefficients are omitted before dividing. Infeasibility of the normalized cone means the graph is acyclic.

The cut system is exponentially large. The notes propose separation/ellipsoid methods or a polynomial extended flow formulation, then state polynomial cycle decomposition and minimum-mean extraction. Their decomposition sketch is incomplete: choosing an arbitrary supported cycle and subtracting its minimum edge value need not leave the cycle cone. For example, the sum of two triangle incidence vectors sharing one edge has value two on the shared edge and one on the outer four-cycle. Subtracting that entire outer cycle leaves only the doubled shared edge, which violates a bridge-cut inequality. A valid decomposition must preserve the cone constraints, not just nonnegativity. Thus the stated decomposition lemma is retained as a result, rather than treating this sketch as a complete constructive proof. Polynomial LP statements concern rational encoded data; the final theorem's real-cost notation does not specify an encoding model.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Lecture Notes/lecture notes.pdf`, §4.5.2, pp. 91–95, Problem 4.24, Definition 4.25, Theorem 4.26, normalized LP, Lemmas 4.28–4.29 and Theorem 4.30/Corollary 4.31; Figure 40, p. 92.
- `Lecture Notes/class notes for 19 July.pdf`, physical pp. 18–22, cycle mean, incidence cone, cut illustration and normalization.
