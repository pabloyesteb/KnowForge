# Tree Implementation — Version 1.0

## Purpose

Provide two local commands to validate the source-specific knowledge Tree and generate a read-only, offline HTML explorer. The YAML trees and Markdown Items defined in [`../01_tree.md`](../01_tree.md) are authoritative. Python does not extract, edit or evaluate technical knowledge.

## Files and responsibilities

```text
scripts/codex-helpers/
  tree.py           # CLI, file loading, in-memory data, structural validation
  tree_html.py      # Markdown conversion and static HTML generation
tests/
  test_tree.py      # focused unit and end-to-end tests
```

Use two implementation modules, not a package or framework. `tree.py` imports `tree_html.py` only when rendering; `tree_html.py` consumes the loaded objects and does not import `tree.py`, read the registry or parse Tree files.

## In-memory data

Use three simple `dataclasses` without behavior:

- `Node(id, title, parent)`: a TreeNode; `parent` is a Node ID or `None`.
- `SourceTree(source, title, category, nodes, path)`: one Source tree, its display title, directory category, ordered Nodes and YAML path.
- `Item(id, source, parent, title, type, body, category, path)`: one Markdown Item, including its original Markdown body, category and file path.

`category` and `path` on loaded objects are **internal context**, not new YAML/frontmatter fields. No `Dataset`, `Diagnostic`, inheritance hierarchy or persistent index is needed.

## `tree.py`

### `load_registry(root)`

Read `00_sources/inventory/sources.yaml` and return production Source IDs, display titles and resolved locations. Follow the registry's **actual structure**; resolve registry locations relative to the registry directory. The registry does not determine Tree categories. Do not inspect original evidence or validate the whole inventory.

### `load_trees(base, registry, examples)`

Discover immediate category directories under `base` that contain both `trees/` and `items/`, excluding the reserved `example_tree/` directory. Read each category's `trees/*.yaml`. Return `list[SourceTree]`, preserving YAML Node order and taking each tree's category from its directory. In production, match Source IDs against the registry; examples are independent of it. Require the agreed tree fields and readable values. The YAML filename stem must match its Source ID.

### `load_items(base)`

Use the same immediate category discovery as `load_trees()` and read each category's `items/*.md`. Parse the five required frontmatter fields, retain the Markdown body unchanged, and return `list[Item]`. Preserve each file's category and path for validation and useful error messages. Do not judge prose, references or technical content.

### `validate(trees, items)`

Check the structural rules in [`../01_tree.md`](../01_tree.md): unique IDs, matching file stems, same-category placement of a Source tree and its Items, valid parent references, acyclic Node relationships and allowed Item types, including `other`. Reject malformed required fields. Stop at the first error with `ValueError` mentioning the affected file and reason. Empty production data and Nodes without Items are valid. Do not add automated editorial or evidence-quality checks.

### `load_tree(root, examples)`

Choose `root/01_tree` or `root/01_tree/example_tree`; load the registry only for production, call the two loaders, run `validate`, and return `(trees, items)`. Both CLI commands must use this same path; do not create a second parser for rendering.

### `main()`

Use `argparse` for `validate` and `render`, each optionally accepting `--examples`. Locate the repository root relative to the script, independent of the current working directory. `validate` prints a short count summary; `render` calls the HTML module and reports the output path. Return a nonzero exit code on error. Do not modify YAML or Markdown.

## `tree_html.py`

### `render_markdown(text)`

Convert Item Markdown to readable HTML, supporting headings, lists, tables, code and mathematical notation. Use established, limited-purpose libraries rather than handwritten Markdown/TeX parsers. Escape or sanitize raw HTML so Item content and metadata cannot execute scripts. Keep dependencies few and version-pinned.

### `render_navigation(trees, items)`

Build the virtual `Career Profile → Category → Source → TreeNode → Item` navigation, grouping loaded Sources by their discovered categories. Humanize directory names for category headings. Preserve YAML order for sibling Nodes; use a deterministic order for sibling Items. Escape displayed text. Return an HTML fragment; do not write files or modify the input objects.

### `render_page(trees, items, examples)`

Assemble one self-contained HTML document with navigation, an Item reading panel, title search, Item type display and a clear empty state. Include only small local CSS/JavaScript for interaction. The viewer is read-only and works offline without a server or CDN.

### `write_html(html, path)`

Write the generated document to `path`, creating the destination directory if necessary. Replace an existing viewer only after the new HTML has been written successfully. Do not touch authoritative Tree files.

## Command-line interface

```sh
python3 scripts/codex-helpers/tree.py validate
python3 scripts/codex-helpers/tree.py render
python3 scripts/codex-helpers/tree.py validate --examples
python3 scripts/codex-helpers/tree.py render --examples
```

Production rendering writes `01_tree/index.html`; example rendering writes `01_tree/example_tree/index.html`. These are generated, disposable outputs.

## Dependencies and tests

Use standard-library modules where practical, plus only the YAML, Markdown, mathematics and sanitization libraries genuinely required by the chosen renderer. Pin external dependency versions in one small requirements file. Do not introduce a web framework, database, server, schema framework or custom parser.

Keep `tests/test_tree.py` focused on: empty production; valid examples; invalid IDs, parents, cycles, categories and types; separation of production/examples; commands from another working directory; safe rendering of Markdown; and preservation of an existing viewer after a failed render. Tests check structural behavior, not factual correctness or completeness of extracted knowledge.

The implemented runtime versions are pinned in `requirements-tree.txt`: PyYAML reads YAML; markdown-it-py renders Markdown; mdit-py-plugins recognizes mathematical delimiters; latex2mathml converts TeX to native MathML; and Bleach sanitizes the result. `mdurl` and `webencodings` are their pinned transitive dependencies. The existing local `.venv` can run the commands and focused suite:

```sh
.venv/bin/python -m unittest discover -s tests -v
```

Production Source titles come from the registry; Tree categories come only from directory placement. No category inference uses original evidence locations or Source types. Production and example data are discovered separately, with `example_tree/` excluded from production discovery even if it contains `trees/` and `items/` directly. Example titles are humanized fictional IDs; examples never read the registry. Item bodies are retained verbatim, with no automated prose or provenance judgments.

The single-file viewer embeds its CSS and small interaction script. Equations using `$…$`, `$$…$$`, `\(…\)` and `\[…\]` become MathML in Python and require a modern browser with native MathML support. TeX support is limited to latex2mathml's supported syntax; conversion errors display escaped original notation as `Unrendered TeX`. Code remains literal. Raw HTML is escaped, generated HTML/MathML is sanitized, and images are omitted; no CDN, web fonts or automatic external assets are needed. Item display order is title-based, with ID as a tie-breaker, and does not imply source chronology.

Both commands use `load_tree()`. HTML is fully rendered before `write_html()` writes a temporary file beside the output and replaces the viewer. Failures leave an existing viewer intact. Generated viewer files are ignored by Git.

## Non-goals

No source extraction, inventory auditing, content rewriting, semantic graph, topic inference, search index, editing interface, general-purpose security framework or speculative extensibility. Prefer obvious functions and straightforward error messages over abstraction and defensive layers that do not serve the current workflow.
