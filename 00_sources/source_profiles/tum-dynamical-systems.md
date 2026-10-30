# Dynamical Systems — supplementary academic materials

## Source identity

| Field | Value |
|---|---|
| Source ID | tum-dynamical-systems |
| Module code | MA3081 |
| Academic term | Summer Semester 2025 |
| Source category | Supplementary academic material |
| Academic credit | Not established |
| Profile status | complete_validated |

Supplementary academic material with an unspecified learning relationship. Accredited completion, grades, credits and personally completed exercises are not documented.

## Source files

- **Archive:** `00_sources/raw/tum/archives/Dynamical Syste 950798440 (S25)_20261012_1600.zip`
- **Lecture notes:** `Allgemeines/Lecture Notes.pdf`
- **Exercises and solutions:** weekly exercise-sheet PDFs and corresponding solutions (Sheets 1–13), including the alternative Sheet 6 solution
- **Examinations:** extensionless exam-solution documents

## Content structure

```text
Graduate text [N]
├── 1 — Definitions & Examples
├── 2 — Stability
├── 3 — Stable/Unstable Manifolds
├── 4 — Equivalence
├── 5 — Poincaré Maps
├── 6 — Structural Stability
├── 7 — Hyperbolic Sets
├── 8 — Local Bifurcations
├── 9 — Normal Forms
├── 10 — Center Manifolds
├── 11 — Higher Codimension
├── 12 — Global Bifurcations
├── 13 — The Smale Horseshoe
├── 14 — Melnikov's Method
├── 15 — Chaos
├── 16 — One-Dimensional Maps
├── 17 — Renormalization
├── 18 — Attractors
├── 19 — Conley's Theorem
├── 20 — Invariant Measures
├── 21 — Ergodicity
├── 22 — Mixing
└── 23 — Entropy

Practice
├── Exercise sheets 1–13 and corresponding solutions [including E7, E13]
└── Alternative Sheet 6 solution

Assessment
└── Two extensionless exam-solution documents
```

Contents order follows the established text pp. 3–4; the preface's reuse across editions remains relevant. Administrative HTML is separate from these substantive documentary groups.

## Structured technical map

### Flows, maps and local qualitative behavior

Phase/state spaces, evolution operators with \(\phi^0=\mathrm{Id}\) and \(\phi^{t+s}=\phi^t\circ\phi^s\), flows/semiflows, iterated maps, orbits, invariant sets, equilibria, periodic orbits and nullclines establish the language. ODE existence/uniqueness and smooth dependence are recalled alongside Banach's fixed-point theorem. Matrix-exponential linear flows and the logistic map provide examples. [N §§1–2, pp. 5–15.]

Stability leads into stable/unstable manifolds, dynamical equivalence and **Hartman–Grobman** local conjugacy, followed by Poincaré return maps. Structural stability and hyperbolic sets broaden the focus from individual equilibria to robustness of orbit structure. Named stable/unstable manifold results occur for both flows and maps. [N §§3–7, pp. 16–39; Theorems 3.8–3.9, 4.5 and 5.1.]

### Bifurcations, normal forms and dimension reduction

Local bifurcations include fold/Hopf behavior and flip bifurcations of maps; Sheet 7 adds explicit transcritical stability exchange, variable changes to normal form, and parameterized polynomial/map examples. Normal-form transformations, resonance structure, the **Poincaré normal-form theorem**, center manifolds, reduction and approximation, then higher-codimension phenomena provide tools for nonhyperbolic dynamics. [N §§8–11, pp. 40–63; Theorems 9.2 and 10.1–10.6; E7.]

### Global dynamics and chaos

Homoclinic/heteroclinic orbits and global bifurcations lead to the **Andronov–Leontovich theorem**, Smale horseshoes, symbolic dynamics and the **Smale–Birkhoff homoclinic theorem**. Melnikov's method uses a splitting function/integral to detect transverse homoclinic intersections; the forced Duffing example connects simple zeros to horseshoe dynamics. Chaos and sensitive dependence, one-dimensional maps, renormalization, trapping regions and attractors complete the geometric sequence. [N §§12–18, pp. 64–99; Theorems 12.3, 13.5 and 14.5.]

### Topological and measure-theoretic dynamics

Conley's theorem precedes invariant measures, **Poincaré recurrence**, ergodicity, the **Birkhoff ergodic theorem**, weak/strong mixing and entropy. The entropy construction uses finite partitions and their iterated refinements, with \(H(\mathcal A)=-\sum_j\mu(A_j)\ln\mu(A_j)\). This connects orbit complexity with probability/information rather than treating chaos as merely irregular-looking trajectories. [N §§19–23, pp. 100–127; Theorems 19.3, 20.9 and 21.7.]

Sheet 13 asks for invariant-function characterizations of ergodicity, Fourier-based analysis of a hyperbolic toral automorphism, and the chain strong mixing ⇒ weak mixing ⇒ ergodicity. Thus the late measure-theoretic sections have explicit exercise support, not only contents-page evidence. [E13.]

## Mathematical methods, computation and applications

Methods represented include phase-plane/nullcline analysis, invariant-manifold reduction, coordinate transformations/normal forms, return maps, bifurcation diagrams, homoclinic splitting, symbolic coding, invariant measures, Fourier arguments and partition entropy. Logistic/doubling maps, van der Pol, Duffing and Lorenz dynamics are named examples in inspected notes. No programming language, package or personal computational project was established from the selected sources; the profile is primarily mathematical.

## Relationships and potential relevance

The local stability/manifold viewpoint complements supplementary [Advanced Control](tum-advanced-control.md), while invariant measures and ergodicity relate to [ADPRL](tum-approximate-dynamic-programming.md) and its stationary-distribution-weighted evaluation. There are conceptual links to [Functional Analysis](tum-functional-analysis.md), [Computational Neuroscience](tum-computational-neuroscience.md) and dynamical models in the [thesis](master_thesis.md). These links organize topics, not course equivalence or further personal project attribution.

Potential domains: nonlinear mechanical/control models, robotics stability, scientific modeling and long-run stochastic/statistical interpretation. Thematic categories: dynamical systems; mathematical analysis; control and robotics; probability and statistical dynamics.

## References and deeper-extraction priorities

Within the archive above:

- **N:** `Allgemeines/Lecture Notes.pdf`, contents pp. 3–4; source page ranges and numbered results above use printed/PDF numbering.
- **E7:** `4. Juni - 10. Juni/Exercise Sheet 07.pdf`, Exercises 7.1–7.4.
- **E13:** `16. Juli - 22. Juli/Exercise Sheet 13.pdf`, Exercises 13.1–13.4.
- Catalogs: `00_sources/inventory/archive_files.csv`, `docs/legacy_inventory/archive_summary.csv`, `00_sources/inventory/sources.yaml` under the stable source ID.

For deeper synthesis, revisit exact hyperbolicity/smoothness/nondegeneracy assumptions, normal-form and center-manifold constructions, Melnikov's integral and Duffing example, and ergodic/entropy hypotheses. These substantial results deserve source-level statements rather than generic theorem-name expansions. The complete 23-section backbone is mapped; solutions/exams have not been exhaustively validated and source mathematics should not be treated as newly audited.
