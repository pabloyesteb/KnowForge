# Codex workflow — Source-by-source Tree extraction

**Status:** procedural instructions for Codex; not a Tree schema or replacement for `docs/01_tree.md`.

## Authority and scope

Read `docs/AGENTS.md`, `docs/00_sources.md`, `docs/01_tree.md`, and (when editing or validating Tree data) `docs/implementation/tree.md`. These files define the Source registry, node/item schemas, provenance, and validation. This guide only specifies the work sequence. Do not introduce fields, objects, directories within `01_tree/`, or cross-Source Topics beyond the documented model.

Use `00_sources/source_profiles/` and their content indexes to **plan coverage and candidate node divisions**. Treat the content index as an orientation map, not as proof of an Item's technical claims; cite the original source materials in each Item. The `Source files` inventory merely locates files and does not define Items.

## Four passes per Source

### 1. Global plan — read-only

- Select one registered Source, resolve its registry ID, category, raw materials, and source profile.
- Read the complete source-profile content index and relevant source organization; identify missing or uncertain coverage. Cross-check source structure in original materials as needed. Do not pretend the index is complete when it is not.
- Sketch a **provisional** hierarchy of Source-local TreeNodes. Prefer few, meaningful divisions, with nesting only when useful. Nodes represent source structure, not a universal topic taxonomy, and need not correspond one-to-one to files.
- Sketch candidate knowledge units and likely joins/splits, especially concepts that recur across lectures, exercises, and solutions. This is a *map*, not a quota or a final Item list.
- Partition original content into consecutive, bounded batches with **explicit file/page/section boundaries**, including exercises and supplementary technical material. Plan for complete substantive coverage, not highlight sampling.
- Write a concise working plan in `docs/codex/work/<source-id>.md` (working state only; not a Tree object). Do not create Tree production files in this pass.

### 2. Pilot batch — small, write-enabled

- Read the plan, inspect the **original evidence** for batch 1, and consult existing TreeNodes/Items for this Source before writing.
- Decide Item boundaries by independent technical usefulness, not by page, lecture, or fixed Item count. Keep essential definitions, derivations, assumptions, examples, and limitations together when they form one coherent unit.
- Create only the necessary Source-local TreeNodes and evidence-backed Items using documented YAML/Markdown formats. An Item belongs to exactly one existing TreeNode; never create direct Source → Item edges.
- If the batch expands an existing Item, revise it rather than duplicate it; keep its stable ID. Repeated content may require **no new Item**. Do not create empty filler Items to match a plan.
- Cross-check candidate Items with the global map, record unresolved joins/splits, and validate changed Tree data using the repository's existing checks (if available).
- Update the working plan with the exact last-covered and next-uncovered file/page/section. Request a short review of granularity before scaling up.

### 3. Consecutive batches — repeat

For each batch: (1) load plan and existing Items for the Source; (2) inspect original material within the stated boundaries; (3) create/update Items and nodes as needed; (4) check redundancy, granularity and references against earlier batches; (5) run available validation; (6) update coverage and next start position. Continue in original sequence; include exercise, code, exam and supplementary material when substantively informative, without treating routine repetitions as new Items. Do not execute untrusted code or notebooks. Avoid silently skipping inaccessible portions.

### 4. Source-wide reconciliation — required before marking complete

Review **all** source sections/files against the source profile's content index *and originals*, checking missing technical coverage, duplicate or fragmented Items, overly broad Items, misplaced nodes, unsupported statements, and weak original-source references. Merge/split/reparent only where justified; preserve IDs of surviving Items and report any unavoidable identifier changes. Validate structure again. Mark complete only when all accessible substantive material is covered, with outstanding inaccessible evidence or uncertainties explicitly recorded.

## Granularity decision rule

Before creating a new Item, ask: **(a)** Is it independently reusable technical knowledge or experience? **(b)** Would it be more coherent as part of an existing Item? **(c)** Is a similar subject already covered elsewhere in this Source? **(d)** Does its treatment warrant a separate Item at this Source's depth? A theorem with its routine proof and corollaries usually stays together; a distinct algorithm or substantial experiment may stand alone. Same topic in different lectures is not automatically a new Item; separate concepts inside one lecture may be different Items. Use the documented eight Item types, choosing the dominant type.

## Minimal persistent working state

Store only operational notes under `docs/codex/work/<source-id>.md` (not in source profiles or production Tree YAML):

```markdown
# Extraction work plan — <source-id>
- Source ID / category: ...
- Orientation: source profile and content index path(s)
- Original materials: identified archive paths / files
- Planned TreeNodes (provisional): ...
- Candidate units / likely overlaps (provisional): ...
- Batch 1: file(s), first–last page/section (pending / active / done)
- Batch 2: ...
- Coverage: completed original ranges; remaining ranges; inaccessible ranges
- Next exact position: <file/archive member>, page/section ...
- Open granularity questions: ...
- Status: planned | pilot | extracting | reconciling | complete
```

Keep this record compact. It is **not** a second source profile, academic content index, Item registry, or processing report; it only coordinates extraction. As extraction progresses, the actual Tree files remain authoritative for created nodes and Items. No claims of complete coverage based only on the plan.

## Boundaries and output

One Source at a time. Default to **planning first**, then a pilot, then consecutive batches; do not jump to a full-course bulk extraction. Avoid arbitrary limits on Items or pages, unnecessary new tooling, changes to unrelated Sources, graph work, and edits to original archives. At the end of each task report files changed, precise coverage/continuation, checks actually run, and unresolved decisions; keep the report short.
