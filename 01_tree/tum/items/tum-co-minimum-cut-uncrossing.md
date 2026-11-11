---
id: tum-co-minimum-cut-uncrossing
source: tum-combinatorial-optimization
parent: co-max-flow
title: Intersection and union of minimum source-sink cuts
type: theorem
caption: "Uses nonnegative crossing capacities to show closure of minimum-cut source sides."
---

# Intersection and union of minimum source-sink cuts

Let \(X,Y\) be source sides of minimum directed \(s\)-\(t\) cuts, so both contain \(s\) and exclude \(t\). Their intersection and union are again valid source sides. Partition the graph into \(X\cap Y\), \(X\setminus Y\), \(Y\setminus X\), and the complement. Comparing outgoing capacities gives
\[
u(\delta^+(X))+u(\delta^+(Y))=u(\delta^+(X\cap Y))+u(\delta^+(X\cup Y))+u(X\setminus Y,Y\setminus X)+u(Y\setminus X,X\setminus Y).
\]
The left side equals twice the minimum cut value. Each new cut is at least that value, and the last two terms are nonnegative. Thus both new cuts attain the minimum, and both crossing-capacity terms vanish. The submitted proof obtains this through seven named arc groups; the identity expresses the same uncrossing argument without confusing source sides with arbitrary minimum edge cuts.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Student Submitted Exercises/Alex Solodovnik.pdf`, p. 1, complete handwritten directed minimum-cut uncrossing proof.
