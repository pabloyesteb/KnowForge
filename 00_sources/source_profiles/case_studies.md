# Case Studies Optimization — Trajectory Optimization in Learned Environments

## Source identity

| Field | Value |
|---|---|
| Source ID | case_studies |
| Module code | CIT413042 |
| Academic module | Case Studies Optimization, TUM |
| Academic term | Summer Semester 2025 |
| ECTS | 10 |
| Grade | 1.0 |
| Academic record | Degree module; transcript PDF p. 2 |
| Authors | Jose Bedoya; Mariia Iavorskaia; Yelyzaveta Vodovozova; Jiefang Xiao; Pablo Yeste |
| Repository | NLOTrajectories |
| Profile status | complete_validated |

One academic team project associated with CIT413042 — Case Studies Optimization. Academic metadata: `00_sources/inventory/courses.csv`.

### Source files

- **Final report [R]:** `/home/pablo/TUM/SoSe 25/Case Studies/Trajectories-4.pdf`; local copy `00_sources/raw/projects/case_studies/Trajectories-4.pdf`
- **Code repository [C]:** `/home/pablo/TUM/SoSe 25/Case Studies/NLOTrajectories/` (K: `src/nlotrajectories/core/`; S: `src/nlotrajectories/scripts/`)
- **Presentation [P]:** repository `docs/Midterm__Case_Studies_-5.pdf`
- **Alternate report [R2]:** repository `docs/Trajectories-5.pdf`
- **Additional material:** repository `Midterm (Case Studies).zip`, `Midterm (Case Studies)/`, `results/`

## Content structure

```text
Final report [R]
├── 1 — Introduction
├── 2 — Theoretical Background
│   ├── Optimal control / direct approaches
│   ├── Trajectory initialization
│   └── SDFs / metrics
├── 3 — Methodology
│   ├── Motion Planning Setup
│   ├── Neural Networks as SDF Approximations
│   └── Integration into Optimization Pipeline
├── 4 — Experiments and Evaluation
│   ├── Interactive GUI for Trajectory Planning and Demonstration
│   ├── Benchmark Design Overview
│   ├── Problem Design Criteria (Benchmark 0)
│   ├── Intermediate Benchmark: 2D Vehicle in Non-Convex Environment
│   └── Complex Benchmark: 2D car in Non-Convex Environment
├── 5 — Conclusion and Outlook
└── Appendix A — Research
    ├── Review of Optimization-Based Collision Avoidance
    ├── TT-SVD
    └── Bernstein Polynomial Representation of SDF

Related documents
├── Midterm presentation and backup slides [P]
└── Alternate overlapping report [R2]

NLOTrajectories repository [C]
├── src/nlotrajectories/core/ [K]
│   ├── config.py / dynamics.py / geometry.py
│   ├── sdf/ / nn_architectures.py
│   ├── trajectory_initialization.py / runner.py
│   └── metrics.py / visualizer.py
├── src/nlotrajectories/scripts/ [S]
│   ├── run_benchmark.py
│   └── tkinter_editor.py
├── Benchmark YAMLs
├── tests/unit/test_geometry.py
├── docs/
└── results/ — untracked
```

The established report contents determine the order; abbreviated entries describe its subsections. The presentation repeats that sequence with progressive builds and optimal-control/shooting/KKT/Newton backup slides. B0–B3 report labels and six repository configurations are different organizational schemes; [R2] is not another project.

## Problem, objectives and project scope

Motion planning in complex environments requires both dynamic feasibility and obstacle avoidance. Explicitly constraining many robot–obstacle pairs can create large nonlinear programs; geometric distance functions may also be nonsmooth at corners or where nearest obstacles change. The project investigates representing obstacle geometry with a **learned signed distance field (SDF)** and coupling it to differentiable optimal-control software. [R, §§1.1–1.3, pp. 5–8.]

The team built a planar pipeline connecting geometric reference fields, supervised implicit-function learning, sampling-based initialization and constrained trajectory refinement. Benchmarks progress from point motion and convex obstacles to second-order unicycle motion, a nonconvex star obstacle, and an Ackermann-type car in a curved corridor. The study compares geometric fidelity, objective value, solver runtime and control profiles rather than presenting a single universal performance score. [R, §§4.2–4.5, pp. 32–50.]

The demonstrated domain is numerical planning with static planar obstacles and kinematic models. There is no hardware experiment, full vehicle/tire dynamics, certified continuous collision avoidance, real-time MPC deployment or learned uncertainty/safety guarantee. Extensions to those settings remain proposed. [R, §5, pp. 51–52.]

## Contributions and attribution

The report is a **five-person team project** and does not allocate every section, experiment or subsystem individually. Its mathematical/computational methods represent knowledge evidenced by participation in the academic project; they are not all claimed as personally invented or exclusively implemented by Pablo.

Targeted Git inspection identifies the following direct or collaborative participation without requiring a new exhaustive contribution audit:

| Individual evidence | Technical substance | Boundary |
|---|---|---|
| `717a0f367a4b1d4392643031a8f1b2e8ab5bbd5b`, Pablo Yeste Blesa `<p.yeste@tum.de>` | Adds `SineLayer` and `SIREN` in K/nn_architectures.py, including frequency-scaled sinusoidal activation and initialization | Implementation of a published architecture, not invention of SIREN; no verified superiority over the reported MLP |
| `12544f1dc5819226a6a3a9b4b3b5535bcd38430d`, `pabloyesteb` | Implements symmetric Hausdorff contour distance, shape checks and empty-surface handling in K/metrics.py | Other metrics existed already; later team edits change details |
| `f32a2b5`, `49bd409` | Extends benchmark model selection/configuration and result logging for MLP/Fourier/SIREN, followed by integration fixes | Not sole authorship of the benchmark runner or every neural model |
| `d03691d`, `489665e` | Extends/corrects NumPy/Torch type annotations across metric interfaces | Annotation work is not proof of universal tensor/device compatibility |
| `cc59650`, early setup commits | CI configuration scaffold and initial project organization | No passing CI or production deployment claimed |
| `c98e1b1`, `52cf317`, `934956c` | Merge participation for nonconvex-obstacle, polish and GUI branches | Integration evidence, not authorship of all merged code |

Name/email evidence associates the TUM identity and GitHub handle with Pablo; the report independently names him. Temporary local stash identities are not used to claim completed personal features. The architecture, solver, RRT, GUI and experiments also contain other team members' work. PyTorch, CasADi, L4CasADi, IPOPT, Shapely and SciPy are external software used/integrated, not personal implementations of those packages.

## Mathematical modeling and trajectory optimization

### Continuous problem and direct transcription

The report formulates optimal control with state/control trajectories, dynamics and path/endpoint constraints:

\[
\min_{x(\cdot),u(\cdot)}\int_0^T L(x(t),u(t))\,dt+E(x(T)),
\quad\dot x=f(x,u),\quad x(0)=x_0,\quad x(T)=x_g,
\quad g(x,u)\le0,\quad\Phi(q)>0.
\]

The implemented runner optimizes state and control arrays through **forward-Euler defects**:

\[
X_{k+1}=X_k+\Delta t f(X_k,U_k),\qquad k=0,\ldots,N-1,
\]

with bounded controls and endpoint conditions. The report calls its selected direct approach multiple shooting; code evidence is specifically a state/control transcription with one-step Euler dynamics, not a higher-order shooting integrator or an implemented collocation solver. The report compares the continuous problem with a finite-horizon multistage state-transition formulation. Its direct-method background is:

- Dynamic programming/principle of optimality and Pontryagin-type indirect approaches are briefly contrasted with direct methods; the implemented study uses **discretize-then-optimize**, not a Hamilton–Jacobi or costate solver.
- **Single shooting:** parameterize controls, integrate the state from the initial condition, optimize over controls. **Multiple shooting:** introduce interval initial states and impose matching constraints between separately evolved intervals. **Direct collocation:** interpolate states at collocation points, enforce derivative consistency and continuity, and integrate the objective by quadrature.
- Comparison of control-only dimension and sensitivity in single shooting with initialization flexibility in multiple shooting and the sparse, larger NLP of collocation. These are method-design comparisons, not universal runtime rankings.

These are studied methods; the actual code implements the Euler transcription above. [R, §§1.3, 2.1–2.2, pp. 6–12; C, K/runner.py, `RunBenchmark.run`.]

The numerical objective is smoothed path length with optional relaxation and control penalties:

\[
J=\sum_{k=0}^{N-1}\sqrt{\|p_{k+1}-p_k\|_2^2+10^{-8}}
 +\rho\sum_ks_k^2+\lambda_u\sum_{k\in\mathcal I}\|U_k\|_2^2,
\qquad s_k\ge0.
\]

Slack and input terms are enabled separately; the checked input-penalty loop uses \(\mathcal I=\{0,\ldots,N-2\}\). Despite a “smooth” option name, it penalizes **input magnitude**, not jerk or successive-control differences. The horizon \(N\Delta t\) is fixed; minimum time is not optimized. Terminal heading may be left unconstrained while other terminal components are fixed. [K/runner.py; R, §§3.3, 4.3.]

### Robot/vehicle models and footprints

- Planar point models use velocity or acceleration input; the second-order version stores position/velocity and applies acceleration.
- Unicycle motion obeys \(\dot x=v\cos\theta,\ \dot y=v\sin\theta,\ \dot\theta=\omega\). Its second-order form augments \(v,\omega\), with \(\dot v=a,\dot\omega=\alpha\), giving five states/two controls.
- Ackermann/bicycle-type kinematics use \(\dot\theta=v\tan\psi/l\), steering angle \(\psi\), wheelbase \(l\) and steering-rate input. The report/code also explore a seven-state acceleration/steering-acceleration augmentation, qualified by derivative-order and steering-factor inconsistencies at the inspected revision.

[R, §3.1, pp. 17–21; K/dynamics.py and benchmark YAMLs.]

Point, rectangular and triangular footprint abstractions transform local vertices by pose into world coordinates. Collision queries constrain the field at these points/time nodes, optionally using slack: \(\Phi(p_k+R(\theta_k)v_j)+s_k\ge m\). Numerical code can use zero margin, unlike the strictly positive conceptual statement. Vertex/time-node sampling does not certify whole-body swept-volume clearance, especially with learned-field errors or nonzero slack. [K/geometry.py; R, motion-planning setup.]

### Sampling-based initialization

The team compares default/zero and straight-line initialization with **RRT warm starts**: sample workspace or goal, select the nearest tree node, steer a bounded step, collision-check the segment, retain parent links and recover a path on reaching the goal. Goal bias, step/domain bounds, collision margin and iteration cap are configurable. Shortcutting removes unnecessary intermediate nodes. [R, §2.3, pp. 12–15; K/trajectory_initialization.py.]

SciPy **CubicSpline** resamples/smooths the geometric path; a function named `_bspline_curve` is not evidence of a B-spline implementation. The checked initializer returns XY and zero-fills other state components, without control initialization; thus it is a geometric seed, not guaranteed dynamically feasible full-state/control lifting. Basic RRT does not provide optimal paths. RRT*, RRT-Connect and Informed RRT* are named variants; A*/Dijkstra and learned initialization are introductory alternatives, not implemented benchmarks. The report's general full-initialization account describes tangent-derived headings, velocities/angular velocities and acceleration estimates, whereas the actual initializer provides only XY and zero-fills other states, as corroborated by the later experiment description. Spline smoothing is not followed by a full collision recheck. [R, §4.3, pp. 40–42; K/trajectory_initialization.py.]

## Signed-distance representations and neural field learning

### Reference geometry and differentiable surrogates

An SDF is negative inside obstacles, zero on their boundary and positive outside. Circular/square reference fields and polygon distances provide supervision; Shapely supplies polygon boundary distance and inside/outside classification. Obstacle unions combine fields through minima. Smooth absolute/min/max/clamp approximations and **log-sum-exp soft minimum** make symbolic distance surrogates easier to differentiate but can shift boundaries and distort distance. [R, §§2.4, 3.2, pp. 15–17, 21–26; K/sdf/casadi.py, K/utils.py.]

The complex corridor is also represented as unions of convex trapezoids approximating elliptical half-rings. Segment projections, signed supporting-line distances and softened min/max operations build the symbolic surrogate for individual trapezoid pieces, including S-shaped/nonconvex geometry. Increasing the number of pieces changes geometric fidelity and solver constraint/evaluation cost. One learned field reduces explicit obstacle representation, but still requires multiple footprint/time-node constraints and derivative evaluations.

### Data generation and training

Supervised samples map planar coordinates to reference signed distances. The study compares uniform grids, independent uniform random samples, and **boundary-informed random sampling** combining a band near the zero contour with global coverage. Boundary-focused sampling aims to improve the geometry most relevant to collision constraints while preserving field information away from obstacles. [R, §3.2.1, pp. 21–22; K/sdf/l4casadi.py, `sample_points`.]

The primary reported learner is a two-hidden-layer MLP, typically width 128 with ReLU. Smaller sigmoid/ReLU models support initial comparisons. Repository implementations additionally include a Fourier-feature MLP with trainable cosine features and Pablo's SIREN:

\[
h^{\ell+1}=\sin\bigl(\omega_0(W_\ell h^\ell+b_\ell)\bigr),
\]

followed by a linear output. Sine-layer initialization uses first-layer bounds \(\pm1/n_{in}\), then \(\pm\sqrt{6/n_{in}}/\omega_0\); default frequency is 30. Fourier/SIREN availability is **implementation evidence**, not proof those variants generated the report's principal results. The shared trainer applies Kaiming-uniform initialization to linear layers despite comments calling it Xavier initialization, so the architecture's own initialization must not be assumed preserved in every training route. [K/nn_architectures.py, `SineLayer`, `SIREN`, `FourierMLP`; commit `717a0f3`; trainer.]

The implemented loss combines SDF-value MSE, a boundary term and spatial-gradient regularization:

\[
\mathcal L=\frac1M\sum_i(h_\vartheta(q_i)-d_i)^2
 +\lambda_s\mathcal L_s
 +\lambda_e\frac1M\sum_i(\|\nabla_qh_\vartheta(q_i)\|_2-1)^2.
\]

The final term is the **implemented Eikonal penalty**, recovered from autograd code rather than copying the report's different Eq. (32) display. The coded surface term averages predicted squared distances at reference near-zero samples; the report's surface metric samples the opposite surface, so they are not interchangeable. [R, Eqs. 24, 31–33, pp. 17, 23–26; K/sdf/l4casadi.py and K/metrics.py.]

Training uses shuffled PyTorch DataLoaders, minibatch **Adam**, a 10% validation split, patience/minimum-improvement early stopping and best-state restoration. Code defaults include 200,000 samples, batch size 256 and learning rate 10⁻³, overridable by configuration. Validation includes MSE/surface terms, not the Eikonal term. The trainer's positional forwarding of the requested boundary fraction into `sample_points`'s `margin` slot leaves the actual boundary fraction at its default and limits exact reproduction of the report's boundary-fraction ablations from this checkout; reported experiments are therefore not independently revalidated here.

## Numerical solvers and computational architecture

**CasADi Opti** constructs the constrained NLP and derivatives. **L4CasADi** bridges PyTorch neural fields into the symbolic optimization/derivative interface. Generated C++/TorchScript/binary artifacts support the toolchain but were not loaded and are not evidence of individually authored C++ solvers. ReLU fields are piecewise differentiable, not globally twice smooth. [R, §3.3; K/runner.py, K/sdf/l4casadi.py; S/run_benchmark.py.]

**IPOPT** is the principal solver, with maximum 1000 iterations, tolerance 10⁻⁴, adaptive barrier updates, quality-function oracle and barrier tolerance factor 0.05. A CasADi `sqpmethod` branch exists, but the standard benchmark entry point does not forward the configured solver type, so SQP is not claimed as an evaluated alternative. [K/runner.py; R, §3.3.4, p. 30.]

The report supplies the following systematic NLP and primal–dual background; this is studied solver methodology, not a personal implementation of IPOPT:

- General constrained NLP `min f(x)` with inequalities `g(x)≤0`, equalities `h(x)=0` and a Lagrangian. First- and second-order derivative information enters Newton/KKT systems; continuous first differentiability alone does not ensure Hessians, despite the report's wording.
- **Log-barrier methods:** strictly feasible interior, decreasing barrier parameter, repeated approximate subproblem solves and warm starts. The report prints a plus sign before the logarithmic sum inconsistent with a minimization barrier and its subsequent multiplier equations; that formula is explicitly not endorsed.
- **Primal–dual central path and perturbed KKT conditions:** stationarity, primal feasibility, positive slacks/multipliers and relaxed complementarity `ΛYe=τe`; decreasing `τ` targets a KKT point under the necessary regularity assumptions, not a global solution of a nonconvex problem.
- **Newton step on the perturbed KKT system:** block structure couples the Lagrangian Hessian, constraint Jacobians and slack/multiplier diagonals. **Fraction-to-the-boundary** step selection preserves positivity, allowing distinct primal/dual step sizes. Residual norms measure stationarity, feasibility and complementarity.
- Solver diagnostics include objective, primal/dual infeasibility, barrier parameter, constraint residuals and failure handling. Theoretical central-path discussion is conditional and introductory; no complete convergence theorem for the implemented learned nonconvex planner is established.

Neither local solver success nor slack relaxation gives global optimality or makes the nonconvex problem convex. [R, §§3.3.1–3.3.3, pp. 26–30; P, backup pp. 104–105.]

The implementation is organized as follows:

| Layer | Components and role |
|---|---|
| Scenario/configuration | K/config.py, six benchmark YAMLs, Pydantic validation and YAML loading |
| Physical/geometric abstractions | K/dynamics.py, K/geometry.py, K/sdf/casadi.py |
| Learned environment | K/nn_architectures.py, K/sdf/l4casadi.py: samples, training, neural obstacle wrapper |
| Optimization | K/trajectory_initialization.py, K/runner.py: seed generation and state/control NLP |
| Evaluation | K/metrics.py, K/visualizer.py: field/contour/trajectory metrics, plots and animations |
| Entry points | S/run_benchmark.py and S/tkinter_editor.py: orchestration, CSV recording and interactive obstacle/path demonstration |

**Tools evidenced:** Python 3.12, NumPy, SciPy/CubicSpline, PyTorch/autograd/Adam, CasADi, L4CasADi, IPOPT, Shapely, Matplotlib/animation, Tkinter, YAML/PyYAML, Pydantic, Poetry, pytest, formatting/linting and Git collaboration. The Tkinter/Matplotlib GUI supports obstacle/scenario editing, hand-drawn versus optimized trajectory visualization, benchmark invocation and presentation/demo support. YAML/Pydantic separates scenario specification from model/solver classes. CPU/CUDA availability in training does not establish measured GPU acceleration or real-time planning.

## Experimental methodology and principal results

### Evaluation quantities

Geometric quality is measured separately from optimizer quality: SDF MSE; occupancy **IoU/Jaccard**; boundary surface error; symmetric **Chamfer distance** (average nearest-contour-point distances); and symmetric **Hausdorff distance** (worst nearest-point separation):

\[
H(A,B)=\max\{\sup_{a\in A}\inf_{b\in B}\|a-b\|,
\sup_{b\in B}\inf_{a\in A}\|a-b\|\}.
\]

The implementation extracts near-zero contour points from sampled grids and uses pairwise distances; it returns no metric when a needed surface is absent at HEAD. Grid resolution and extraction tolerance affect contour metrics. Reported optimizer quantities include objective, solve time and iteration behavior, alongside trajectory/control plots. [R, §2.5; K/metrics.py; personal Hausdorff commit above.]

Report B0/B1/B2/B3 stages and six repository config names are different organizational schemes. All numerical results below are **team-report observations**, not personal performance achievements or independently rerun experiments.

### Learned SDF and solver trade-offs

| Report experiment | Quantitative observation | Interpretation / evidence |
|---|---|---|
| Sampling, 10 repetitions | IoU 0.591 ± 0.125 uniform; 0.595 ± 0.082 random; 0.721 ± 0.050 informed, fraction 0.8 | Reported sampling comparison favors boundary-informed data in that scenario, not universal dominance. R, Table 2, p. 22. |
| Simple obstacle/model size | Learned IoUs 0.9080, 0.9641, 0.9843; solve times 2.5080, 1.2627, 16.1607 s; analytic 1.1298 s | Greater fidelity need not give faster optimization; learned objectives remain near 1.63. R, Table 3, p. 24. |
| B0 baseline | Analytic objective 1.5032 / 0.8252 s; learned 1.5027 / 2.6702 s, IoU 0.9836 | Similar path objective with neural overhead. R, Table 6, p. 34. |
| B1, RRT initialization | B1.0 analytic/learned objectives 1.5375/1.5451, times 4.55/31.98 s; B1.1 1.5623/1.5690, times 5.93/35.22 s | Learned fields can support similar objective values but increase evaluation/differentiation cost. R, Table 8, p. 39. |
| B1.1 initialization comparison | Learned RRT 1.5029 / 18.26 s; linear 1.5108 / 21.10 s; default 1.5186 / 23.93 s | Reported benefit from geometric warm starts; not proof of dynamic feasibility of initialization. R, Table 9, p. 41. |
| B1 control penalty | Without 1.5029 / 18.26 s; with weight 0.5, 1.5371 / 16.85 s | Different composite objective and initialization randomness preclude a pure path-length/smoothing superiority claim. R, Table 10, p. 42. |
| B2 nonconvex star | IoU 0.9356; Chamfer 0.0025; Hausdorff 0.0336 | Nonconvex learned-field example; slack/no-slack comparison also changes margin and collision samples, so not a controlled slack-only ablation. R, Table 11, p. 43; Table 12, p. 45. |
| B3 Ackermann-type corridor | Composite objective 9.309; solver 7.941 s; final learned IoU 0.8722, CD 0.00138, HD 0.02958 | Reported car-planning example and field quality, qualified by the model/source limits. R, Fig. 19, p. 47; Table 13, p. 48. |

The report's B1.1 table gives learned IoU **0.8091**, not the nearby prose's claim that both B1 cases exceed 0.97; its malformed Chamfer value is not interpreted as a reliable number. Representative tables/plots were visually checked. [R, Table 7, p. 38.]

### Complex-corridor representation comparison

The corridor uses four half-elliptical rings. Convex decompositions use 16, 36, 56 or 76 total trapezoids; the learned comparison uses a width-128, two-hidden-layer MLP. Boundary-fraction sweeps report ten repetitions, selecting 0.8, then increasing samples from 200,000 to one million for the final displayed field. This final field's IoU must not be confused with the earlier 200,000-sample comparison. [R, §4.5, pp. 46–50.]

Plots show finer decomposition improving geometric agreement overall but increasing time per IPOPT iteration, without a clear path-objective gain. Control regularization is disabled for that comparison, unlike the earlier composite-cost car example. More accurate obstacle representation therefore does not automatically improve the achieved path objective; constraint complexity and derivative costs matter. This is a scenario-specific trade-off, not a universal learned-field speedup claim. [R, Figs. 24–25, p. 50.]

Two untracked CSVs under `results/` provide additional run records for point/unicycle configurations, but do not exactly reproduce all report tables or establish artifact-to-figure provenance. They were inspected as supplementary evidence, not used to silently replace the report's results. The `tests/unit/test_geometry.py` test and CI scaffold establish validation intent, not a verified passing run; the geometry test references a stale interface. No tests or experiments were run.

## Technical findings, limitations and research extensions

The central finding is that learned implicit geometry can be integrated with classical constrained trajectory optimization and produce reported plausible paths across increasing geometric/dynamic complexity. **Initialization quality, boundary data and representation complexity are as consequential as network choice.** Runtime overhead and sensitivity remain visible rather than suppressed.

Relevant limits are source-qualified: learned approximation/vertex/time sampling is not collision certification; slack can permit violations; smoothing and convex decomposition change boundaries; RRT/spline seeds need not be dynamically feasible; ReLU fields are not globally twice smooth; and the checked higher-order Ackermann equations have state-order/steering-derivative inconsistencies. Trainer sampling/metric definitions and raw result provenance prevent claiming exact reproduction of every reported ablation. These constraints qualify professional claims without turning the profile into a software audit. The detailed implementation qualifications below preserve the course-level inspection.

Significant implementation caveats at the recorded revision:

1. `Ackermann2ndOrder` documents state order `(...,v,ω,ψ̇)` but returns `(...,ω̇,v̇,ψ̈)`, swapping the intended derivative positions. Its steering derivative uses `1/(1+ψ²)` while the heading uses `tanψ`; the report repeats that inconsistent factor. Do not treat either as a verified second-order Ackermann model.
2. The first-order point class has four stored states with two zero derivatives, unlike the two-state report formulation. Benchmark naming and “first/second order” wording also conflict in places.
3. `DotGeometry.sdf_constraints` ignores its slack argument; polygon checking defaults to vertices only. The RRT rectangle-inflation calculation uses the minimum coordinate rather than the complete vertex norm, and spline smoothing is not followed by a full collision recheck. These facts limit safety claims.
4. Trainer sampling arguments, Eikonal/surface definitions and full-state initialization differ between report and code as described above. `use_smooth` sums input squares only through `N−2`, not differences or a complete jerk penalty.
5. The geometry unit test calls `goal_cost`, absent from the current geometry class. No tests were run; this is an observed interface mismatch, not a claimed test result.
6. The PDF title dates and alternate file hashes differ. Additional untracked presentation/source/results are not fixed by the Git revision. No raw experimental reruns, environment reconstruction or bug correction were performed. The separate, already completed targeted Git attribution is preserved in the contribution table above.


### Reviewed alternatives in Appendix A

- Literature-review coverage of **conic-duality collision avoidance**: convex obstacles in conic form, dual-cone multipliers, dual-norm constraints and separating certificates. Signed distance as separation distance minus penetration permits minimum-penetration formulations with penalized slack. This is reviewed methodology, not the implemented planner's collision model.
- **Tensor-train SVD (TT-SVD)** for voxelized **truncated signed distance fields (TSDFs)**: clip distances to a narrow band and compress the 3-D grid into low-rank cores. Contrast discrete/compressed representation with continuous derivative access. The appendix explicitly leaves detailed implementation for later.
- **Bernstein-polynomial SDF representation:** normalize local coordinates to `[0,1]`, construct nonnegative partition-of-unity basis polynomials, tensor-product the basis, fit coefficients by least squares, and differentiate analytically with coordinate scaling. The displayed normal-equation inverse requires full column rank; recursive least squares is mentioned as an alternative. A minimum across link fields need not remain globally smooth even if individual expansions are smooth.
- Comparisons cover memory/compute growth with polynomial degree, tensor ranks and voxel resolution, interpretability, data requirements and gradient availability. No TT-SVD/Bernstein implementation or experimental outcome is attributed to the case study.

These are theoretical/research exposure, not implemented planner alternatives or personally achieved benchmark outcomes. [R, Appendix A, pp. 55–60.]

Proposed extensions include 3D/dynamic environments, higher-fidelity dynamics, adaptive boundary sampling, uncertainty-aware distance outputs/risk-sensitive constraints, learned initialization and solver-structure exploitation. Real-time MPC and those extensions are not presented as completed work. [R, §5.2, pp. 51–52.]

## Demonstrated technical knowledge and thematic categories

- **Constrained optimization/optimal control:** continuous formulations, direct transcription, Euler defects, path/endpoint/control constraints, relaxations and input regularization, IPOPT/KKT/barrier methodology and nonconvex initialization.
- **Robotics/geometry:** point/unicycle/Ackermann kinematics, finite-footprint transformations, RRT/shortcutting/spline seeds, signed-distance collision constraints and convex decomposition.
- **Scientific machine learning:** supervised implicit fields, boundary-informed sampling, MLP/Fourier/SIREN architectures, sinusoidal initialization, autograd Eikonal penalties, minibatch Adam and validation/early stopping.
- **Evaluation/software:** occupancy/contour metrics, personally attributable Hausdorff implementation, benchmark model integration, symbolic/neural solver interfaces, configuration-driven Python tools, plots/GUI and collaborative Git integration.

The first three areas describe knowledge represented by the team project; exclusive individual implementation is limited to the evidence in the contribution table. Thematic categories: **optimization; optimal control; numerical mathematics; dynamical systems and robotics; machine learning; computational geometry; scientific computing and software engineering**. Applications include robot/vehicle motion planning, collision avoidance, learned implicit geometry, constrained optimal control, nonlinear-program initialization and interactive engineering demonstrations. This single Source Profile represents the course-associated project once.

## Coverage and validation

All report blocks are represented: problem/OCP; direct-method background and initialization; SDF/metrics; robot models; sampling/training; NLP/IPOPT; GUI and B0–B3 results; conclusion/future work; appendix alternatives. Relevant runner, neural/training, geometry, initialization, metric, config/benchmark and package evidence was cross-checked statically. Targeted author/diff inspection supports narrower personal attribution than report coauthorship alone.

The original report and repository paths exist and are registered; the local report copy is preserved and hash-identical. Academic metadata/identifiers agree with the existing course record. Results are attributed, conflicting values qualified, and implemented versus reviewed/proposed methods separated. This consolidation preserves the course-level systematic explanations and implementation caveats alongside the project's equations, individual Git attribution, architecture and quantitative team results. Unrelated profiles retain their technical content. This project is ready for source-qualified thematic synthesis, linked to `cit413042` rather than counted as an additional academic experience.
