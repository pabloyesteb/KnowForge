---
id: tum-co-minimum-mean-cycle
source: tum-combinatorial-optimization
parent: co-min-cost-flow
title: Minimum mean cycles from fixed-length walk dynamic programming
type: algorithm
caption: "Computes a cycle mean by a min-max difference formula and recovers a cycle from an optimal fixed-length walk."
---

# Minimum mean cycles from fixed-length walk dynamic programming

For a directed graph with arc costs, let \(\mu(G)=\min_C c(C)/|C|\), taking \(+\infty\) for an acyclic graph. An edge progression here is a directed walk that may repeat vertices and edges, unlike the introductory edge-nonrepeating walk convention. From a source reaching every vertex, define \(F_k(x)\) as the minimum cost of a progression with exactly \(k\) arcs ending at \(x\). Initialize \(F_0(s)=0\), all other entries infinite, and compute
\[
F_k(x)=\min_{(w,x)\in E}\{F_{k-1}(w)+c(w,x)\}.
\]
With \(n\) vertices, the characterization is
\[
\mu(G)=\min_{x:F_n(x)<\infty}\max_{0\le k<n:F_k(x)<\infty}
\frac{F_n(x)-F_k(x)}{n-k}.
\]
If every \(F_n\) is infinite, no length-\(n\) progression exists and the reachable graph is acyclic. Every candidate vertex has some finite shorter source path. For disconnected graphs add a zero-cost super-source reaching all vertices; count that new vertex consistently in \(n\), the iteration horizon and recovery.

For the proof, first shift costs so \(\mu=0\). There are no negative cycles. Every length-\(n\) progression costs at least a shortest simple path to the same endpoint, so each displayed maximum is nonnegative. Follow a shortest path to a zero-cost cycle and repeat that cycle, taking the first \(n\) arcs. Its endpoint attains ordinary shortest-path cost, making its maximum zero. Adding constant \(K\) to each arc shifts \(F_k\) by \(kK\) and every displayed quotient and cycle mean by \(K\); this proves the general case.

Store predecessors for each length/vertex entry. For a minimizing endpoint, backtrack an optimal length-\(n\) progression and isolate a repeated-vertex circuit; the zero-mean proof after shifting ensures an extracted circuit has the minimum mean. Do not confuse an arbitrary shortest simple path with this fixed-length progression. The source states \(O(nm)\) for the recurrence and bookkeeping; evaluating all vertex/length quotients also takes \(O(n^2)\), absorbed after the reachability augmentation. The table requires \(O(n^2)\) storage when keeping all lengths for the min-max formula and reconstruction.

The worked six-vertex Sheet 7 table gives \(F_6\) at vertices 1–4 as \(9,2,3,8\), with respective min-max scores \(4,5/4,5/3,3\). Vertex 5 has no length-six progression. The minimizing endpoint is 2, and the cycle \(2\to3\to4\to1\to2\) has total cost 5 and mean \(5/4\). This shows that minimum mean cycles need not be negative; negativity determines usefulness for cost cancellation, not existence.

The Python scaffold stores weight and predecessor dictionaries for every length/vertex pair. Its completed routines compute the min-max quotients, choose a minimizing endpoint, follow length-indexed predecessors backward to the first repeated vertex, and reverse the retained edges to recover the circuit. Matrix relaxation over all vertex pairs and all lengths costs \(O(n^3)\), rather than the adjacency-list \(O(nm)\) bound. Finite predecessor chains and reachability must be checked; a `max` over an empty finite-length candidate list is undefined for an unreachable vertex. The separate solution snippet incorrectly refers to `self.v`, whereas the full completion uses the class's `self.vertex_num`.

The driver currently enables random generation, overwriting the manual matrix. Infinite matrix entries denote absent arcs, and the generator sets the entire source row to zero, including a source self-loop. This is not a fresh super-source with no incoming arcs: the generator also permits incoming arcs and other self-loops. Consequently it computes cycles of that supplied matrix, which can include the artificial source; an added zero self-loop alone prevents reporting acyclicity even for an otherwise acyclic graph. To apply the lecture reduction to an original graph, source-augmentation arcs must not introduce cycles. Supplied timings are printed by the driver but no measured performance is asserted.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Lecture Notes/lecture notes.pdf`, §3.7.2, pp. 56–59, Definition 3.35, Theorems 3.36–3.37 with proof, Figure 29 and Algorithm 9.
- `Lecture Notes/class notes for 14 June.pdf`, physical pp. 10–19, minimum-mean definitions, complete zero-mean/shift proof and dynamic-programming algorithm; the handwritten shift sign is interpreted as minus the minimum mean as in the typed proof.
- `Problem Sheets/Exercise Sheet 7/exercise_sheet_7.pdf`, Exercises 1 and 3, pp. 1–2; `Problem Sheets/Exercise Sheet 7 - solutions/exercise_sheet_7 - sol.pdf`, full table/cycle answer, p. 1, and code task pp. 2–3.
- `Problem Sheets/Exercise Sheet 7/graph_module.py` and `Problem Sheets/Exercise Sheet 7/main.py`, full scaffold/generator/driver.
- `Problem Sheets/Exercise Sheet 7 - solutions/code - sol.py` and `Problem Sheets/Exercise Sheet 7 - solutions/graph_module - complete.py`, full completion snippets and implementation.
