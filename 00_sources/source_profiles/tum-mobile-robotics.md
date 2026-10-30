# Mobile Robotics — supplementary academic materials

## Source identity

| Field | Value |
|---|---|
| Source ID | tum-mobile-robotics |
| Course title | Mobile Robotics / Mobile Robotik |
| Module code | IN2404 |
| Academic term | Winter Semester 2024/25 |
| Source category | Supplementary academic material |
| Academic credit | Not established |
| Profile status | complete_validated |

Supplementary academic material with an unspecified learning relationship. Accredited completion and personal exercise implementations are not documented. IN2404 is distinct from transcript module IN2138.

## Source files

- **Archive:** `00_sources/raw/tum/archives/Mobile Robotik 950765148 (W24_25)_20261012_1552.zip`
- **Lectures:** weekly L1–L13 PDF deck groups, classroom/non-classroom variants and `All Lecture Slides.pdf`
- **Exercises and solutions:** archived exercise/template/solution material, including Python files [E2–E5, E7–E8, E11–E13]
- **Recordings:** archived `.f4v` files
- **Examinations:** revision material and historical WS23/24 examination PDFs

## Content structure

```text
Lectures
├── 1 — Introduction [L1]
├── 2 — Representations [L2]
├── 3 — Sensors and Actuators [L3]
├── 4 — Probabilistic Nonlinear Least Squares [L4]
├── 5 — Kinematics and Temporal Models [L5]
├── 6 — Recursive Estimation [L6]
├── 7 — Sparse Visual SLAM [L7]
├── 8 — Dense Mapping and SLAM [L8]
├── 9 — Semantic, Object-level and Dynamic Mapping [L9]
├── 10 — Feedback Control [L10]
├── 11 — Model-based Control [L11]
├── 12 — Planning [L12]
└── 13 — Learning to Act [L13]

Exercises — templates and solutions
├── E2 — Aeroplane
├── E3 — Pinhole camera
├── E4 — Least squares
├── E5 — Bundle adjustment
├── E7 — Differential drive
├── E8 — Occupancy
├── E11 — Hill driving
├── E12 — RRT
└── E13 — Gridworld

Other material
├── All Lecture Slides.pdf
├── Recordings
├── Revision
└── Historical WS23/24 exams
```

Classroom/non-classroom deck variants and the aggregate slides repeat the same sequence. Exact L/E paths are in the source references; recordings were inventoried, not transcribed.

## Structured technical map

### Foundations: state, geometry, sensors and motion

Introduction and representations distinguish robot state, world/environment maps and uncertainty. Rotation representations include Hamilton/unit quaternions, conversions and minimal local parameterization; probabilistic representations use Bayesian statistics. Sensor/actuator material and pinhole-camera/differential-drive exercises connect geometric states to measurements and control inputs. Kinematics/temporal models cover rigid-body rotation and differential-drive/quadrotor dynamics, alongside continuous/discrete model and linearization viewpoints. [L1–L3, L5; E2/E3 source paths below.]

### Probabilistic nonlinear least squares

Gauss–Newton and **Levenberg–Marquardt** address nonlinear estimation. Visual bundle adjustment uses reprojection residuals and camera/landmark Jacobians, with structured systems assembled from contributions of individual observations. Exercises include nonlinear least squares, motion-capture differential-drive examples and bundle adjustment. This connects probabilistic sensor models to numerical optimization rather than treating SLAM as a single black box. [L4–L5; E4/E5.]

### Recursive estimation and sparse visual SLAM

Bayesian filtering separates prediction and measurement update; particle filters approximate distributions with weighted samples/resampling. Kalman and extended Kalman filters represent Gaussian/linearized estimation, including inertial and differential-drive examples. Sparse visual SLAM includes FAST-type features, geometric matching/pose estimation and **RANSAC** outlier rejection, linking filtering and optimization-based estimation to visual navigation. [L6–L7; E7.]

### Dense, semantic and dynamic maps

Occupancy mapping maintains per-cell probabilities/log-odds using inverse sensor models. Dense 3D representations include **truncated signed-distance fields (TSDF)** and octree occupancy (OctoMap); dense tracking includes **iterative closest point (ICP)** and direct photometric alignment. Loop closure and locally rigid submaps address accumulated drift. The next lecture extends maps with semantic labels, object-level decomposition and dynamic-scene representations. These are related but distinct geometric/probabilistic representations. [L8–L9; E8.]

### Feedback and model-predictive control

Continuous/discrete LTI stability, SISO/MIMO distinctions, PID, anti-windup, reference filtering and feedforward precede model-based LQR/MPC. Quadrotor examples discuss input remapping, cascaded loops, hover assumptions and imperfect inter-loop decoupling. Constrained optimization geometry motivates MPC's treatment of control/state restrictions; supplied hill-driving Python separates `LqrController`, `MpcController` and a simulator and imports `qpsolvers.solve_qp`. [L10–L11, especially L10 pp. 16–24 and L11 pp. 18–31; E11.]

### Planning, exploration and learned decisions

Planning uses free configuration space, collision checking, obstacle inflation and roadmaps/grids; algorithms include **Dijkstra, A*, RRT, RRT* and informed RRT***. Slides distinguish discrete-space and sampling-based planning, plus robot exploration. Learning-to-act material adds finite-horizon/discounted MDP utility, value/policy iteration, model-learning versus model-free approaches, direct evaluation, Q-values, **Q-learning** and ε-greedy exploration, with a final deep-RL overview. [L12, pp. 1–58; L13, especially pp. 12–36; E12/E13.]

## Tools and represented exercise work

Python code pairs cover airplane/state representations, pinhole projection, differential-drive models, nonlinear least squares, bundle adjustment, filtering, occupancy grids, hill-driving control, RRT and gridworld MDPs. Static imports establish **NumPy, SciPy optimization/spatial transforms, Matplotlib, PyQt5, qpsolvers and vedo**. Lecture 10 also displays a C++ PID-controller example; this is demonstrated syntax, not evidence of a personal C++ software project. No executable behavior or training/solver results were tested.

## Relationships and potential professional relevance

This source deepens the syllabus-level [IN2138](in2138.md) planning/filtering map while remaining a separate supplementary identity. Estimation/rigid-body/control topics relate to the [thesis](master_thesis.md); geometric planning and signed-distance representations relate to [Case Studies](case_studies.md), without equating volumetric TSDF mapping with its learned collision SDF. Decision models relate to [deep RL](tum-intro-deep-rl.md) and supplementary [ADPRL](tum-approximate-dynamic-programming.md). These are useful thematic connections, not additional accredited experiences or expanded contribution attribution.

Potential domains: robot autonomy, navigation/GNC, perception, probabilistic estimation, constrained control and numerical optimization. Thematic categories: dynamical systems and robotics; control theory; optimization; computer vision and scientific computing; reinforcement learning.

## Source references and deeper-extraction priorities

All references resolve inside the named archive; use the following exact directory/file combinations:

| Ref | Directory | Document |
|---|---|---|
| L1 | `16. Oktober - 22. Oktober/` | `L1 Introduction.pdf` |
| L2 | `23. Oktober - 29. Oktober/` | `L2 Representations.pdf` |
| L3 | `30. Oktober - 5. November/` | `L3 Sensors and Actuators.pdf` |
| L4 | `6. November - 12. November/` | `L4 Probabilistic Nonlinear Least Squares.pdf` |
| L5 | `13. November - 19. November/` | `L5 Kinematics and Temporal Models.pdf` |
| L6 | `20. November - 26. November/` | `L6 Recursive Estimation.pdf` |
| L7 | `27. November - 3. Dezember/` | `L7 Sparse Visual SLAM.pdf` |
| L8 | `4. Dezember - 10. Dezember/` | `L8 Dense Mapping and SLAM.pdf` |
| L9 | `11. Dezember - 17. Dezember/` | `L9 Semantic, Object-level and Dynamic Mapping.pdf` |
| L10 | `8. Januar - 14. Januar/` | `L10 Feedback Control.pdf` |
| L11 | `15. Januar - 21. Januar/` | `L11 Model-based Control.pdf` |
| L12 | `22. Januar - 28. Januar/` | `L12 Planning.pdf` |
| L13 | `29. Januar - 4. Februar/` | `L13 Learning to Act.pdf` |

Exercise anchors: **E2** `23. Oktober - 29. Oktober/E2_aeroplane_sol.py`; **E3** `11. Dezember - 17. Dezember/E3_pinhole_camera_sol.py`; **E4** `6. November - 12. November/E4_least_squares_sol.py`; **E5** `13. November - 19. November/E5_bundle_adjustment_sol.py`; **E7** `27. November - 3. Dezember/E7_diff_drive_sim_sol.py`; **E8** `4. Dezember - 10. Dezember/E8_diff_drive_occ_sol.py`; **E11** `15. Januar - 21. Januar/E11_hill_driving_sol.py`; **E12** `22. Januar - 28. Januar/E12_rrt_sol.py`; **E13** `29. Januar - 4. Februar/E13_gridworld_sol.py`. Catalogs: `00_sources/inventory/archive_files.csv` and `00_sources/inventory/sources.yaml` under the stable source ID.

Prioritize L4–L8 for exact Jacobians, perturbation conventions, filter equations and mapping updates; L11/E11 for horizon/cost/constraint/solver contracts; L12/E12 for collision checking and tree rewiring; and L13/E13 for MDP versus learning distinctions. Render relevant mathematical slides because extraction loses notation and some spatial relationships. The 13-part topic backbone is mapped sufficiently for initial synthesis; detailed derivations and uninspected examples remain optional targeted extraction, not evidence of personal implementation.
