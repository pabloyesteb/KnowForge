---
id: tum-co-graph-incidence
source: tum-combinatorial-optimization
parent: co-foundations
title: Graph incidence, cuts, paths and cycles
type: concept
caption: "Defines the graph structures and boundary notation used by path, tree, flow and matching problems."
---

# Graph incidence, cuts, paths and cycles

A simple undirected graph \(G=(V,E)\) has nonempty vertex set and edges that are two-element subsets of \(V\). A simple digraph uses ordered pairs of distinct vertices as arcs. Thus both exclude loops and parallel copies; opposite directed arcs are distinct and can coexist. Set \(n=|V|\), \(m=|E|\). Graph structure is independent of the chosen drawing.

For an undirected vertex subset \(S\), the boundary \(\delta(S)\) consists of edges with exactly one endpoint in \(S\). In particular \(\delta(v)\) denotes edges incident to vertex \(v\); the notes' expression intersecting an edge with \(v\) is read as membership of the vertex, or intersection with its singleton. Edges wholly within \(S\) form \(E(S)\). A subgraph on \(S\) may choose only some edges of \(E(S)\); the vertex-induced subgraph retains all of them. For a digraph,
\[
\delta^{\rm in}(S)=\{(u,v)\in E:u\notin S,v\in S\},\quad
\delta^{\rm out}(S)=\{(u,v)\in E:u\in S,v\notin S\}.
\]
An internal edge does not belong to either directed boundary.

The course uses “walk” for an edge-nonrepeating sequence of incident vertices and edges, allowing repeated vertices; this corresponds to a trail in other conventions. A closed walk returns to its starting vertex. A path has no repeated vertices. A cycle closes such a sequence with all other vertices distinct and no repeated edges; direction must be respected in digraphs. A digraph is acyclic when it has no directed cycle. These conventions distinguish a path from a general traversal and a graph's cycles from cycles created merely by a drawing.

A bipartite graph admits two vertex classes with every edge crossing between them. Every tree is bipartite: deleting a leaf preserves a smaller tree, and when reattaching it place the leaf opposite its unique neighbor. The degree sum \(2(n-1)\) guarantees a leaf for a tree with more than one vertex; connectedness rules out an isolated vertex. Starting with one vertex proves the statement by induction. Equivalently a tree has no odd cycle.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Lecture Notes/lecture notes.pdf`, Chapter 1, pp. 2–5, Definitions 1.1 and 1.4–1.9.
- `Lecture Notes/class notes for 19 April.pdf`, printed slides 11–21 (physical pp. 12–34), graph/induced-subgraph and boundary overlays.
- `Student Submitted Exercises/Simon Strzoda.pdf`, pp. 1–2, both tree/bipartition proofs, leaf construction and degree-sum induction.
