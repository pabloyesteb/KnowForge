---
id: tum-co-tree-path-intersection
source: tum-combinatorial-optimization
parent: co-trees-matroids
title: Common vertices of three pairwise-intersecting tree paths
type: theorem
caption: "Uses unique tree paths to rule out three pairwise intersections with no shared vertex."
---

# Common vertices of three pairwise-intersecting tree paths

Three vertex paths in a tree that intersect pairwise have a common vertex. Assume otherwise and choose vertices in the three pairwise intersections. Each path contains the unique tree route between its two chosen intersection vertices. These three routes have a median branching vertex in the minimal subtree spanning the chosen vertices, and that median lies on all three original paths, a contradiction. Equivalently, trimming their pairwise overlaps to three distinct junctions would create a cycle, impossible in a tree. The statement concerns vertex intersections: three two-edge paths through a three-leaf star intersect pairwise in edges but have no edge common to all three, while they do share the central vertex. The handwritten contradiction proof uses vertices and unique routes, which fixes this interpretation.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Student Submitted Exercises/Márk Reichmann.pdf`, p. 1, handwritten three-path statement, route-trimming argument and cycle contradiction.
