---
id: tum-co-b-flow-feasibility
source: tum-combinatorial-optimization
parent: co-min-cost-flow
title: Supply-demand flows, feasibility cuts and maximum-flow reductions
type: method
caption: "Reduces balanced supply-demand feasibility to one maximum flow and derives the necessary and sufficient cut inequalities."
---

# Supply-demand flows, feasibility cuts and maximum-flow reductions

A capacitated \(b\)-flow satisfies \(0\le f(e)\le u(e)\) and outgoing minus incoming flow equal to \(b(v)\). Positive \(b\) is supply, negative \(b\) demand, and \(\sum_v b(v)=0\) is necessary. Its cost is \(\sum_e c(e)f(e)\); costs may be negative, notwithstanding the initial definition box's nonnegative codomain. Balance alone does not guarantee feasibility when outgoing capacity is insufficient.

Add a super-source with arcs of capacity \(b(v)\) to each supply vertex and arcs of capacity \(-b(v)\) from each demand vertex to a super-sink, preserving original capacities. Put zero cost on new arcs for cost-preserving formulations. A flow of value \(B=\sum_{b(v)>0}b(v)\) saturates all supply/demand arcs and restricts to a feasible \(b\)-flow. Conversely, any feasible \(b\)-flow extends to one of value \(B\). This gives a polynomial decision/construction algorithm, not a minimum-cost solution just by maximizing throughput.

For \(X\subseteq V\), the corresponding augmented cut has capacity \(u(\delta^{\rm out}(X))+B-b(X)\). Max-flow/min-cut therefore gives the exact criterion
\[
u(\delta^{\rm out}(X))\ge b(X)\quad\text{for every }X\subseteq V.
\]
A failed inequality is an infeasibility witness. The transformation adds two vertices and at most one arc per original vertex; runtime must be evaluated on that augmented graph.

Maximum flow also reduces to minimum-cost circulation: add a distinct return arc \(t\to s\) of capacity \(M=\sum_eu(e)\) and cost −1, give all other arcs cost zero and set all balances to zero. A source-sink flow extends by returning its value; minimizing circulation cost maximizes this return amount. Retain a distinct arc or subdivision if the return orientation already exists. The example's first feasible lecture flow costs 38, while another illustrated feasible flow costs 20, showing why feasibility alone is not optimality.

A five-vertex parametric supplement uses supplies \((20,-13,8,-10,-5)\). Enumerating the nontrivial cut inequalities and removing automatic nonpositive-balance and dominated constraints leaves exactly \(x\ge7\) and \(y\ge6\) on its two variable capacities. The combined bound \(x+y\ge12\) is then redundant. Costs in its diagram do not affect this feasibility question.

For multiple freely producing sources and consuming sinks, a related reduction adds a super-source with unbounded arcs to each original source and unbounded arcs from each original sink to a super-sink. Extend a feasible flow using each terminal's net production/consumption; conversely restrict the augmented flow. Conservation at the original terminals proves equality of total value in both directions. This requires nonnegative net supply at designated sources and net demand at designated sinks. For finite original capacities a total-capacity upper bound can replace infinity.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Lecture Notes/lecture notes.pdf`, §3.6, pp. 48–50, Definitions 3.24–3.25, Remark 3.26, Theorem 3.27 and both reductions.
- `Lecture Notes/class notes for 07 June.pdf`, physical pp. 1–10, complete model, cost-38 annotation, infeasibility cut, super-source reduction and return-arc construction.
- `Student Submitted Exercises/Kadrush Drenovci.pdf`, pp. 1–2, full directed diagram, capacity-cut enumeration and parameter conclusion.
- `Student Submitted Exercises/Qiqi Huang.pdf`, pp. 1–2, multiple-terminal super-source/sink task, full diagram and copied explanatory excerpt; p. 2 is blank.
