# Codex procedure — Incremental Tree extraction

**Scope:** Operational instructions for Codex, not a Tree specification. Follow `docs/AGENTS.md`, `docs/00_sources.md`, `docs/01_tree.md`, and `docs/implementation/tree.md` when writing or validating Tree data. Do not modify those documents unless explicitly asked.

## Workflow (one Source at a time)

1. **Plan.** Use the registered Source, its `source_profile` and **Content structure** index to propose a shallow, Source-local TreeNode hierarchy and consecutive extraction batches. Check originals only where needed to resolve important uncertainties. Include lectures, exercises/solutions, supplements, code and assessments where substantive. **Do not create TreeNodes or Items during planning.**
2. **Pilot.** Read the originals for batch 1 and the existing Tree state for that Source. Create only justified TreeNodes and evidence-backed Items in the documented formats; validate; review granularity before proceeding.
3. **Continue.** For each batch, read the plan and existing Items first; then read its original material in order. Create or update Items, check overlaps, validate and update the exact continuation point. Repeated content may only extend an existing Item—or require no change. If a batch is too large, stop at a coherent source boundary, mark it partial, and record the exact next location; never sacrifice review quality to finish a batch.
4. **Reconcile.** Compare coverage with the complete original materials and content index. Address omissions, duplicate/fragmented or oversized Items, placement and provenance. Validate before marking complete; document inaccessible evidence without claiming complete coverage.

## Item and node decisions

- **TreeNodes** organize each Source; avoid unnecessary depth. Items belong to exactly one TreeNode, never directly to a Source.
- **Items** capture independently useful technical knowledge at the depth of the course, not individual slides or index entries. No Item quota.
- Before creating an Item: **independent? already covered? better merged? sufficiently developed?** Do not bundle independently reusable results merely because they share a chapter or broad topic. Keep supporting definitions, routine proofs and examples with their main result; retain necessary hypotheses, derivations/proofs and limitations without transcribing source documents.
- The source profile is an **orientation aid, not evidence** for an Item. Cite identifiable original files and locations; never invent claims or references. Do not execute untrusted code or notebooks.
- Items contain **technical knowledge and source references only**: no inspection/verification commentary, extraction history or future-batch instructions. Put actionable follow-ups in the work plan.
- Preserve existing Item IDs when revising; report unavoidable changes. Use the documented Item types and validation tools.

## Batch sizing

- Plan batches around coherent chapters, sections and associated exercises—not a fixed time, page count or Item quota. Codex may adjust overly large or small planned batches as evidence warrants, preserving consecutive coverage.
- Work through successive coherent units, reading, extracting, cross-checking and validating each carefully. If a subsection or result must be split, record the precise covered and next-uncovered locations and continue immediately. Never rush, skip content or mark partial work complete.

## Autonomous execution

- After the plan and pilot are complete, **continue successive batches autonomously** within the current Source. Do not request approval at batch or chapter boundaries. A validated batch or saved checkpoint is a progress milestone, not a stopping condition.
- For each batch, inspect the existing plan and Items, read the corresponding originals, extract or revise evidence-backed Items, check overlap and granularity, validate, and record the precise next-uncovered location **before** starting the next batch. Follow the workflow and quality requirements above without shortcuts.
- Continue working without a self-imposed time, token, context, computational or usage-budget threshold. **Do not monitor, estimate, anticipate or manage budgets as a reason to stop.** Stop voluntarily only when **(a)** the current Source has been fully reconciled and validated or **(b)** a genuine blocker prevents reliable continuation. External system limits may interrupt execution; do not preemptively stop because of them. Do not automatically start a different Source.
- After every coherent subsection or batch, validate and update the plan with exact covered and next-uncovered source locations, then **immediately continue**. Checkpointing is routine progress tracking, never a stopping condition. If execution is interrupted externally, the latest validated checkpoint must support resumption. Do not rush, skip review or leave incomplete/unvalidated Items merely to begin another batch.
- Resume from the actual repository state and the existing active plan; do not redo completed extraction. If the checkpoint and production Tree disagree, reconcile them before proceeding. Do not claim completion solely because the planned batches are marked done; perform the Source-level reconciliation.
- Render the HTML viewer when explicitly requested or when required by the existing project workflow; it need not be regenerated after every batch. Report actual counts only when verified.

## Working plans

Store per-Source operational plans in **`01_tree/_work/<source-id>.md`**, separate from production category data. This is the canonical location for new plans. If an active legacy plan exists elsewhere (for example, `codex/_work/<source-id>.md`), resume from that plan rather than creating a competing copy; reconcile its location with the documented convention only when safe, preserving its checkpoint and updating references. Never maintain two active plans for the same Source. Keep them versioned during active extraction; remove them after the Source has been fully extracted and validated. `_work/` contains no `trees/` or `items/` directories and is ignored by Tree category discovery.

Use **only these four sections**:

- `## TreeNodes` — provisional hierarchy, names only.
- `## Batches` — short table of **identifiable source files and precise chapter/page/section boundaries**, status, and coverage of exercises/supplements/assessments. Use abbreviations defined once when helpful.
- `## Progress` — completed batches and **exact next original-file location**; no duplicate status narratives.
- `## Open issues` — only actionable, Source-specific uncertainties; omit if none.

Do **not** include selection justifications, comparisons with other Sources, processing history, chapter summaries, candidate-Item catalogues, repeated granularity rules or generic caveats. Avoid duplicating the source profile/content index. Plans are operational checklists, not reports. Keep updates minimal; mark partial batches precisely rather than claiming a completed batch.

### Example — compact plan (illustrative)

```markdown
# Tree extraction — tum-functional-analysis

## TreeNodes
- Normed spaces and bounded operators
- Hilbert spaces
- Fundamental principles, extension and duality
- Compact subsets and weak convergence
- Sobolev spaces and distributions
- Compact, adjoint and Fredholm operators
- Spectrum and compact normal operators

## Batches
N = `Materials/Lecture notes.pdf`; D = `Materials/Distributions.pdf` (archive members).
E1–E14 = `Problem sheets/Problem Sheet <n>.pdf` and corresponding `Solutions to problem sheets/` PDFs.

| # | Original material / boundaries | Status |
|---|---|---|
| 1 | `Tutorials/Introduction slides.pdf`; N ch. 1; E1–E3 | Pending |
| 2 | N ch. 2; E4–E5 | Pending |
| 3 | N ch. 3–4; E6–E8 | Pending |
| 4 | N ch. 5–6; E9 | Pending |
| 5 | N ch. 7; D (entire file) | Pending |
| 6 | N ch. 8–11; E10–E12 | Pending |
| 7 | N ch. 12–13; E13–E14; `Mock Exam/Mock Exam.pdf` and its solution | Pending |

## Progress
- Completed: none.
- Next: batch 1, `Tutorials/Introduction slides.pdf`, page 1.

## Open issues
- Exercise/chapter overlaps; revisit Items instead of duplicating.
- Consider splitting broad nodes only if extraction warrants it.
```

The example abbreviates chapter ranges; in actual plans, make each batch boundary unambiguous using original headings/sections or physical pages where necessary. Do not invent paths or rely on the example as evidence.

## Output discipline

Keep the plan and response concise. If execution ends, report the stopping reason (Source complete, genuine blocker, or external interruption if identifiable), changed files, coverage and exact continuation (if unfinished), validation performed, and unresolved blockers. Do not invent a budget-related reason for stopping. Do not expand scope, add infrastructure, or modify unrelated Sources.
