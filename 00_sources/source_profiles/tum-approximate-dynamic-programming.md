# Approximate Dynamic Programming and Reinforcement Learning — supplementary materials

## Source identity

| Field | Value |
|---|---|
| Source ID | tum-approximate-dynamic-programming |
| Academic term | Winter Semester 2025/26 |
| Source category | Supplementary academic material |
| Academic credit | Not established |
| Profile status | complete_validated |

Supplementary academic material with an unspecified learning relationship. No transcript match, credits or grade are established; personal assignment completion and implementation are not documented.

## Source files

- **Archive:** `00_sources/raw/tum/archives/Approximate Dyn 950837808 (W25_26)_20261012_1601.zip`
- **Notes:** `Allgemeines/Material/1_Notes/` — note versions, including `ADPRL2526_V03.pdf`, and `DPB22.pdf`
- **Lectures:** `Allgemeines/Material/2_Slides/ADPRL2526_L01.pdf`–`ADPRL2526_L12.pdf`
- **Exercises and handouts:** `Allgemeines/Material/3_Exercise/`
- **Code:** `Allgemeines/Material/3_Exercise/Coding/`, including `script_09.py` and `script_12.py`; world/template/solution ZIP packages
- **Assignments:** `Allgemeines/Material/4_Assignment/ADPRL2526_A01.pdf`, `ADPRL2526_A02.pdf`
- **Examination:** mock-exam PDF

## Content structure

```text
Allgemeines/Material/
├── 1_Notes/ — V03 backbone [N]
│   ├── 1 — Introduction
│   ├── 2 — Stochastic Finite Horizon Problem
│   ├── 3 — Stochastic Infinite Horizon Problem
│   ├── 4 — Policy Iteration Algorithms
│   ├── 5 — Advanced Policy Iteration Algorithm
│   ├── 6 — Advanced Topics in DP
│   ├── 7 — Approximate Dynamic Programming
│   ├── 8 — Approximate Policy Iteration
│   ├── 9 — Neuro-Dynamic Programming
│   ├── 10 — Monte Carlo and Temporal Difference
│   ├── 11 — Theory of TD learning
│   ├── 12 — Advanced TD Learning
│   └── 13 — A Unified Framework of ADPRL
├── 2_Slides/
│   └── Lecture decks L01–L12
├── 3_Exercise/
│   ├── Thirteen exercise PDFs and handouts
│   └── Coding/ — including script_09.py and script_12.py [C9, C12]
└── 4_Assignment/
    ├── ADPRL2526_A01.pdf [A1]
    └── ADPRL2526_A02.pdf [A2]

Related material
├── Earlier overlapping note versions
├── Supplementary DPB22.pdf
├── Mock exam
└── Nested world / template / solution packages
```

The notes folder contains three versions; earlier ones do not extend the numbered course. Chapter names/order come from V03 contents pp. 2–3. The index describes supplied documents and code, not personal assignment completion.

## Technical topic map

### Sequential decisions and exact dynamic programming

Finite-state/action sequential decision models distinguish deterministic/stochastic transitions, finite/infinite horizons, history-dependent versus Markov policies and randomized versus deterministic policies. Bellman's principle gives backward finite-horizon recursion; infinite-horizon discounted costs yield policy and optimal Bellman equations/operators. For a stationary policy, the notes use the affine form \(T_\pi J=G_\pi+\gamma P_\pi J\). Fixed points, monotonicity, contraction in appropriate norms, value iteration and linear-programming formulations provide the exact-solution foundation. [N §§1–3, pp. 4–29; L01–L03.]

### Policy iteration and computational variants

Policy evaluation alternates with greedy improvement; optimistic policy iteration uses incomplete evaluation. Advanced variants include multi-step/geometrically averaged Bellman operators, λ-policy iteration, Banach fixed-point arguments, asynchronous updates, Gauss–Seidel sweeps and distributed value iteration. State-action cost \(Q\) supplies an alternative representation and greedy action selection. These distinguish update scheduling, evaluation depth and state versus state-action representations. [N §§4–6, pp. 30–54; L04–L06.]

### Function approximation and projected evaluation

Linear feature and neural approximation replace full value tables. Bellman-residual minimization, approximate value/policy iteration, ergodic-policy stationary distributions, weighted norms, mean squared Bellman error and **mean squared projected Bellman error (MSPBE)** are separate objectives/constructions. Projection and the choice of weighting distribution affect stability, not just numerical conditioning. Neuro-dynamic programming connects gradient-based optimization to neural policy evaluation. [N §§7–9, pp. 55–77; L07–L09.]

### Sample-based learning and numerical linear algebra

Monte Carlo evaluation contrasts with bootstrapped temporal-difference updates. Topics include TD(0), SARSA, Q-learning, eligibility traces, stochastic approximation and convergence conditions, including Robbins–Monro step-size assumptions. Advanced material covers gradient TD, TD-corrected variants, least-squares policy evaluation (LSPE), **least-squares temporal difference (LSTD)** and online inverse updates via the **Sherman–Morrison formula**. Off-policy learning separates behavior and target policies and uses importance sampling. The final notes connect ADPRL to Newton-type reasoning. [N §§10–13, pp. 78–96; L10–L12, especially L12 pp. 7–18 and 22–31.]

The slides contain broad claims about off-policy stability/ergodicity; this selective map does not elevate them to universal guarantees. Detailed convergence statements and their sampling/feature assumptions should be extracted together before use in thematic mathematical summaries.

## Exercise, assignment and computational evidence

Assignment 1 asks for discounted finite-horizon recursion/truncation reasoning and state/control/disturbance-dependent discounting. Assignment 2 explicitly studies **norm-mismatch divergence of projected evaluation** in a two-state Markov chain with alternative feature vectors, then constrained Bellman operators. These provide important counterpoint to generic claims that approximate policy evaluation always converges. [A1–A2, pp. 2–3.]

`script_09.py` contains functions named `MSBE_l2`, `MSBE_xi`, `MSPBE_xi` and `run_API`, together with Bellman/transition-matrix utilities. `script_12.py` supplies `GTD`, `LSTD`, value iteration and policy-iteration helpers, with `MazeWorld`/`GridWorldPlotter` examples; its comments warn that random features can produce a nonoptimal policy. Python, NumPy, Matplotlib and tqdm are evidenced by imports. The later template ZIPs/local world modules are dependencies represented in the material, not newly verified runnable software. [C9, C12.]

## Connections and potential professional relevance

This source provides operator, approximation and numerical foundations complementing [Introduction to Deep Reinforcement Learning](tum-intro-deep-rl.md), [humanoid learning](tum-biologically-inspired-learning.md), [Nonlinear Optimization](tum-nonlinear-optimization.md) and [Statistical Learning](tum-statistical-learning.md). Connections to control and robotic decision-making are substantive; stochastic decision models may also inform quantitative-risk themes without establishing actuarial coursework. It is not a duplicate transcript experience.

Thematic categories: reinforcement learning; optimization; numerical mathematics; stochastic modeling; control and robotics.

## Source references and deeper extraction

All paths are archive-relative:

- **N:** `Allgemeines/Material/1_Notes/ADPRL2526_V03.pdf`, contents pp. 2–3; chapter ranges above. Work-in-progress notes; the cover says *Applied* while slides/assignments say *Approximate*.
- **L01–L12:** `Allgemeines/Material/2_Slides/ADPRL2526_L01.pdf` through `ADPRL2526_L12.pdf` (12 decks; approximately 433 physical pages, with repeated recaps/builds).
- **A1/A2:** `Allgemeines/Material/4_Assignment/ADPRL2526_A01.pdf` and `ADPRL2526_A02.pdf`, three pages each.
- **C9/C12:** `Allgemeines/Material/3_Exercise/Coding/script_09.py` and `script_12.py`.
- **Inventory:** source ID above in `00_sources/inventory/sources.yaml`; exact membership in `archive_files.csv`.

Priorities: projected-operator hypotheses and norm-mismatch examples; TD/LSTD/GTD equations with sampling assumptions; λ-operator derivations; supplied exercise implementations and nested world/template packages. These are targeted deepening tasks, not prerequisites to using the established full-sequence topic map. No claims of completed assignments, measured results or personal coding are made.
