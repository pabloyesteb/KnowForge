# KnowForge

### From fragmented information to structured, traceable knowledge.

**KnowForge is an AI-assisted system for constructing and connecting knowledge representations across sources, domains, and levels of abstraction.**

Documents are rich in information but poor in structure. Concepts are scattered across files, connections remain implicit, and summaries often lose the evidence behind them. KnowForge explores a different approach: **turn source material into explicit, navigable knowledge**—then connect that knowledge without losing where it came from.

> **Status: Active development.** A source-grounded knowledge-tree format, structural validator, and offline HTML explorer are implemented. Cross-source semantic graphs and higher-level synthesis are planned, not yet implemented.

## The idea

```text
Heterogeneous sources
        │
        ▼
Source-grounded knowledge extraction  ← AI-assisted workflow
        │
        ▼
Hierarchical knowledge trees           ← Implemented
        │
        ▼
Cross-source semantic graph            ← Planned
        │
        ▼
Higher-level synthesis & applications  ← Planned
```

KnowForge separates complementary ways of representing knowledge:

- **Trees preserve context.** Each source is decomposed into coherent knowledge units arranged according to its own structure.
- **Graphs connect ideas.** A planned semantic layer will link related concepts across sources and domains, beyond their original hierarchies.
- **Abstraction preserves evidence.** The aim is to support increasingly general views while retaining links to the specific material that supports them.

The result is intended to be more than a document summary or a graph visualization: a foundation for **exploration, cross-domain synthesis, and evidence-grounded reasoning**.

## What works today

The current prototype focuses on the **knowledge-tree layer**:

- **Structured knowledge items:** independently useful concepts, methods, algorithms, implementations, or results, stored as Markdown with YAML metadata.
- **Source-specific hierarchies:** YAML-defined tree nodes keep each item in the context of its original source.
- **Stable identifiers and provenance:** items reference registered sources and retain source references in their content.
- **Structural validation:** Python checks identifiers, parent relationships, cycles, categories, and metadata consistency.
- **Interactive offline explorer:** a self-contained HTML page with hierarchical navigation, title search, and rendered Markdown and mathematical notation.
- **Automated tests:** focused checks for loading, validation, and safe rendering.

The production knowledge tree already contains **269 items from five academic sources**, demonstrating the representation on substantial mathematical material. This is an example corpus—not a claim that arbitrary document ingestion is fully automated.

## Architecture

| Layer | Purpose | Status |
| --- | --- | --- |
| **Sources** | Register original material and preserve provenance | In use |
| **Knowledge Tree** | Decompose each source into structured, navigable knowledge items | Implemented; corpus growing |
| **Semantic Graph** | Identify relationships and shared concepts across sources | Planned |
| **Synthesis** | Build higher-level, domain-spanning representations | Planned |
| **Applications** | Derive useful outputs from the structured knowledge | Future direction |

**Design principles:** source-grounded extraction · explicit structure · traceability · multiple levels of abstraction · inspectable data · modular components.

The original use case was professional and academic profiling. KnowForge is evolving into a **domain-agnostic knowledge representation project**: professional profiles are now one possible application, not the organizing constraint.

## Explore the prototype

With Python 3 and the repository checked out:

```bash
python3 -m pip install -r requirements-tree.txt
python3 scripts/tree.py validate
python3 scripts/tree.py render
```

Open **`01_tree/index.html`** in your browser. The generated explorer is self-contained and works offline.

To run the isolated example dataset instead:

```bash
python3 scripts/tree.py render --examples
```

Then open `01_tree/example_tree/index.html`.

To run the tests:

```bash
python3 -m unittest discover -s codex/tests -v
```

The current implementation uses **Python, YAML, Markdown, and static HTML**. It does **not** require a database, graph engine, or hosted web service.

## Roadmap

1. **Expand source-grounded extraction** while preserving clear boundaries between original evidence and interpretation.
2. **Define and implement semantic graph structures** for cross-source relationships.
3. **Support multilevel synthesis** with explicit links back to supporting items and sources.
4. **Develop applications** that use the resulting representations, without tying the core system to a single domain.

## Why KnowForge?

**Knowledge is not a pile of documents—and it is not a single summary.** It has structure, context, relationships, and varying levels of abstraction. KnowForge aims to make those properties explicit, computable, and traceable.

*Work in progress. The architecture and capabilities will evolve as the prototype develops.*
