---
id: tum-co-hopcroft-karp
source: tum-combinatorial-optimization
parent: co-bipartite
title: Hopcroft–Karp layered matching augmentation
type: algorithm
caption: "Augments a maximal family of vertex-disjoint shortest alternating paths to obtain a square-root phase bound."
---

# Hopcroft–Karp layered matching augmentation

Start with the empty matching. Build alternating BFS layers from all uncovered vertices in one bipartition class: traverse nonmatching edges toward the other class, then the unique matching edge back. Stop at the first layer containing uncovered targets. Keep all shortest-path predecessor connections between layers, rather than only a single search tree. Backward DFS from these targets selects an inclusion-maximal family of vertex-disjoint shortest augmenting paths. Toggle every selected path simultaneously and rebuild the layers. The family need not have maximum cardinality; maximality ensures no further shortest path avoids all selected vertices.

Let \(\ell(M)\) be the shortest augmenting-path length, infinity at optimality. As in a blocking-flow phase, augmenting the maximal family eliminates the current shortest length, so \(\ell\) strictly increases. When no target is reachable, the absence of augmenting paths certifies maximum cardinality. Ordinary greedy selection of edges is only the first length-one phase; later alternating paths revise those choices. The worked example has successive shortest lengths 1, 3 and 7 before obtaining its perfect matching.

BFS and DFS with adjacency lists and exhausted-edge bookkeeping use \(O(n+m)\) operations per phase. After \(\lceil\sqrt n\rceil\) phases, all remaining augmenting paths have length at least \(\sqrt n\). Compare with an optimum \(M^*\): the symmetric difference provides at least \(|M^*|-|M|\) vertex-disjoint augmenting paths. They occupy at most \(n\) vertices, hence \((|M^*|-|M|)\sqrt n\le n\). At most \(O(\sqrt n)\) more augmentations, and therefore phases, remain. This gives \(O(\sqrt n(n+m))\), customarily \(O(m\sqrt n)\) after removing isolated vertices, plus input handling.

The printed Algorithm 11 contains an unfinished line, inconsistent layer-index assignments and an infinity value that can be overwritten. The coherent procedure is the alternating BFS/DFS phase above: terminate a search with no reachable uncovered target, retain the first target distance, and use only that layer graph for the phase. The runtime claim requires vertex-disjoint paths and linear total scans within a phase.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Lecture Notes/lecture notes.pdf`, §4.3, pp. 73–76, Definition 4.10, Theorem 4.11, Algorithm 11 and complete worked diagrams.
- `Lecture Notes/class notes for 05 July.pdf`, physical pp. 9–18, full layered algorithm and three-phase diagrams.
