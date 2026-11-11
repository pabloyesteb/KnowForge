---
id: tum-co-edmonds-karp
source: tum-combinatorial-optimization
parent: co-max-flow
title: Edmonds-Karp shortest augmentations and capacity-independent complexity
type: algorithm
caption: "Uses shortest residual paths and increasing distances between repeated bottlenecks to bound augmentations by O(mn)."
---

# Edmonds-Karp shortest augmentations and capacity-independent complexity

Edmonds-Karp specializes Ford-Fulkerson by choosing a residual source-sink path of minimum edge count at every augmentation. BFS supplies such a path; augment by its residual bottleneck, update forward/reverse residual capacities and repeat until the sink is unreachable. Correctness follows from the residual optimality certificate. “Shortest” refers to number of arcs, not largest bottleneck or smallest numerical capacity.

The notes prove two length properties: successive shortest augmenting-path lengths never decrease, and if an earlier and a later chosen path contain opposite orientations of an arc, the later length exceeds the earlier by at least two. Their proof combines the two paths as a directed multigraph, retaining duplicate copies of shared arcs and cancelling opposite pairs. The remaining multigraph lies in the earlier residual network (choosing the latest relevant reversal for the nonconsecutive case) and decomposes into two source-sink paths plus possible cycles. Both paths have length at least the earlier shortest-path distance. Thus their combined edge count proves monotonicity; cancellation of at least two arc copies gives the extra two in the reversal case. Removing cycles from traversals preserves the inequalities; an Eulerian traversal need not itself be a simple path.

Charge each augmentation to an arc whose residual capacity is exhausted. For the same oriented arc to become a bottleneck again, its reverse must be used in between. Applying the reversal property in both directions forces at least four additional edges between these two bottleneck occurrences. Paths have at most \(n-1\) edges, so each oriented arc is charged only \(O(n)\) times. There are at most \(2m\) original/reverse orientations, giving \(O(mn)\) augmentations.

With adjacency-list residual searches and updates costing \(O(n+m)\) each, the conventional bound is \(O(nm(n+m))\), written \(O(m^2n)\) in the notes after ignoring irrelevant isolated vertices so that search overhead is \(O(m)\). These are operation bounds independent of capacity magnitudes, unlike arbitrary Ford-Fulkerson. The argument also gives finite termination for irrational capacities under exact arithmetic; it does not provide a finite binary encoding for arbitrary real inputs. The source gives a more specific augmentation count and a bottleneck-count display with omitted endpoint rounding; the asymptotic bound follows without those integer-rounding details.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Lecture Notes/lecture notes.pdf`, §3.3, pp. 31–33, Algorithm 5, Lemma 3.10 and full auxiliary-multigraph proof, Theorem 3.11 and bottleneck charging.
- `Problem Sheets/Exercise Sheet 4 - solutions/graph_module - complete.py`, `edmonds_karp` and `find_aug_path_BFS`, matrix implementation with a different per-search cost.
- `Lecture Notes/class notes for 17 May.pdf`, physical p. 23, shortest-augmentation rule.
- `Lecture Notes/class notes for 24 May.pdf`, physical p. 1, capacity-independent theorem and pointer to typed proof.
