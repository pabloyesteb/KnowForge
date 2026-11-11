---
id: tum-co-disjoint-routes
source: tum-combinatorial-optimization
parent: co-max-flow
title: Edge-disjoint and internally vertex-disjoint routes by flow reductions
type: method
caption: "Uses unit capacities and vertex splitting to decide simultaneous route feasibility in polynomial time."
---

# Edge-disjoint and internally vertex-disjoint routes by flow reductions

To send three travelers from one origin to one destination without sharing a street, represent allowed directed street segments by capacity-one arcs. An integral maximum flow decomposes into source-sink paths after discarding circulation cycles. Unit capacities make these paths edge-disjoint, so three routes exist exactly when the maximum value is at least three. A polynomial-time maximum-flow algorithm therefore decides feasibility and supplies routes. Merely computing a fractional flow without an integrality argument does not directly identify paths.

To prohibit shared internal vertices as well, replace each internal vertex \(v\) by \(v_{\rm in},v_{\rm out}\) and a capacity-one arc between them. Redirect incoming arcs to \(v_{\rm in}\) and outgoing arcs from \(v_{\rm out}\); leave source and sink unsplit. Any route using that vertex must consume its bottleneck arc. Integral routes are thus internally vertex-disjoint while sharing the permitted endpoints. This is the precise version of the official solution's abbreviated redirection formula.

The school story says travelers must not “cross” paths. The supplied solution interprets this as no shared internal graph vertex. Geometric noncrossing in a fixed street drawing is a different constraint unless every crossing is modeled as a vertex. For undirected streets represented by two opposite arcs, cancel opposite-direction flow before decomposing paths, so a physical street is not used in opposite directions by different routes. These modeling choices must match the intended street restrictions.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Problem Sheets/Exercise Sheet 5/exercise_sheet_5.pdf`, Exercise 1(a–b), p. 1.
- `Problem Sheets/Exercise Sheet 5 - solutions/exercise_sheet_5 - sol.pdf`, Exercise 1(a–b), p. 1, unit-capacity and vertex-splitting constructions.
