# Career Profile — Project Overview

## Purpose

Career Profile is a source-grounded record of academic knowledge, technical work, research, and professional experience. It supports comprehensive professional profiling, exploration of expertise, technical interview preparation, and tailored applications. The underlying record represents the available evidence rather than a preconceived career narrative; the user determines professional positioning.

## Stages

The pipeline separates original evidence, source-specific decomposition, cross-source interpretation, and professional presentation:

**00 Sources → 01 Tree → 02 Graph → 03 Master Profile → 04 CV**

| Stage | Directory | Responsibility | Documentation |
| --- | --- | --- | --- |
| 00 Sources | `00_sources/` | Originals, source registry, inventories, prior per-source inspection | [`00_sources.md`](00_sources.md) |
| 01 Tree | `01_tree/` | Source-by-source structural decomposition into evidence-grounded knowledge Items | [`01_tree.md`](01_tree.md) |
| 02 Graph | `02_graph/` (planned) | Semantic synthesis across Sources: Topics, Competencies and relationships | `02_graph.md` (not yet written) |
| 03 Master Profile | `03_master_profile/` (downstream) | Comprehensive professional synthesis based on the knowledge record | To be defined |
| 04 CV | `04_cv/` (downstream) | Application-specific documents derived from the professional synthesis | To be defined |

**The Tree answers:** what does each Source contain, and where does a given unit of knowledge come from?

**The Graph will answer:** how are the units of knowledge related across Sources, and what expertise do they jointly support?

The two representations serve different purposes. Tree Items preserve original provenance; semantic interpretations do not rewrite source-specific evidence.

## Repository orientation

```text
career-profile/
  00_sources/
    inventory/
    raw/
      projects/
      tum/
    aux/
    source_profiles/
  01_tree/
    example_tree/          # isolated demonstration dataset
    tum/                   # production source data
  02_graph/                # planned
  03_master_profile/       # downstream
  04_cv/                   # downstream
  docs/
    AGENTS.md
    project_overview.md
    00_sources.md
    01_tree.md
    implementation/
      tree.md
  codex/
    instructions/          # task-specific procedures
    scripts/               # source-inspection helpers
    tests/                 # Tree implementation tests
    _work/                 # active extraction plans and progress
  scripts/
    tree.py                # Tree CLI and validation
    tree_html.py           # offline HTML renderer
```

Some planned directories may not yet exist. The diagram represents responsibilities, not a requirement to pre-create empty trees or stages.

## Evidence and implementation principles

Original material and external repositories remain read-only. The inventory identifies Sources and where to find them. Existing source profiles contain useful prior inspection and analysis, but they do not override original evidence. Tree extraction is incremental, linear through each Source, and exhaustive in coverage of substantive accessible material—not a representative sampling exercise.

Knowledge data uses inspectable Markdown and YAML. Supporting scripts are intentionally small and limited to concrete validation or visualization needs; the Tree implementation is documented separately in [`implementation/tree.md`](implementation/tree.md). There is no database, semantic-search system, or automatic graph construction in the current tree stage.

The stage documents specify data structures, provenance and procedures in human-readable technical terms. [`AGENTS.md`](AGENTS.md) governs Codex working behavior and change authorization; it is not another model specification. Historical reports remain under `00_sources/inventory/legacy_inventory/` for reference.

## Current work

The Tree validator and static read-only explorer are implemented; extraction is underway Source by Source in consecutive batches. Operational plans live in `codex/_work/`, with reusable Codex procedures in `codex/instructions/`. The `02_graph/` schema and infrastructure are intentionally deferred.
