"""Load, structurally validate and explore the source-specific Tree."""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import re
import sys

import yaml


ITEM_TYPES = {"concept", "theorem", "method", "algorithm", "implementation", "experiment", "result", "other"}


@dataclass
class Node:
    id: str
    title: str
    parent: str | None


@dataclass
class SourceTree:
    source: str
    title: str
    category: str
    nodes: list[Node]
    path: Path


@dataclass
class Item:
    id: str
    source: str
    parent: str
    title: str
    type: str
    caption: str
    body: str
    category: str
    path: Path


def _yaml(text, path):
    try:
        return yaml.safe_load(text)
    except yaml.YAMLError as error:
        raise ValueError(f"{path}: invalid YAML: {error}") from error


def _fields(value, names, path):
    if not isinstance(value, dict) or set(value) != set(names):
        raise ValueError(f"{path}: expected fields {', '.join(names)}")


def _strings(path, **values):
    for name, value in values.items():
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{path}: {name} must be a nonempty string")


def _categories(base):
    return sorted(path for path in Path(base).glob("*")
                  if path.is_dir() and path.name != "example_tree"
                  and (path / "trees").is_dir() and (path / "items").is_dir())


def load_registry(root):
    path = Path(root) / "00_sources/inventory/sources.yaml"
    document = _yaml(path.read_text(encoding="utf-8"), path)
    if not isinstance(document, dict) or not isinstance(document.get("sources"), dict):
        raise ValueError(f"{path}: expected a 'sources' mapping keyed by Source ID")
    registry = {}
    for source, record in document["sources"].items():
        if not isinstance(record, dict) or not isinstance(record.get("locations"), dict):
            raise ValueError(f"{path}: Source {source!r} needs a title and locations mapping")
        _strings(path, source=source, title=record.get("title"))
        locations = {}
        for name, location in record["locations"].items():
            _strings(path, location=location)
            locations[name] = location if location.startswith(("https://", "http://")) else (path.parent / location).resolve()
        registry[source] = {"title": record["title"], "locations": locations}
    return registry


def load_trees(base, registry, examples):
    trees = []
    for category in _categories(base):
        for path in sorted((category / "trees").glob("*.yaml")):
            document = _yaml(path.read_text(encoding="utf-8"), path)
            _fields(document, ("source", "nodes"), path)
            source = document["source"]
            _strings(path, source=source)
            if not isinstance(document["nodes"], list):
                raise ValueError(f"{path}: nodes must be a list")
            if examples:
                title = source.replace("-", " ").replace("_", " ").title()
            else:
                if source not in registry:
                    raise ValueError(f"{path}: unknown production Source {source!r}")
                title = registry[source]["title"]
            nodes = []
            for record in document["nodes"]:
                _fields(record, ("id", "title", "parent"), path)
                nodes.append(Node(**record))
            trees.append(SourceTree(source, title, category.name, nodes, path))
    return trees


def load_items(base):
    items = []
    for category in _categories(base):
        for path in sorted((category / "items").glob("*.md")):
            with path.open(encoding="utf-8", newline="") as handle:
                text = handle.read()
            frontmatter = re.match(r"\A---[ \t]*\r?\n(.*?)^---[ \t]*(?:\r?\n|\Z)", text, re.MULTILINE | re.DOTALL)
            if frontmatter is None:
                raise ValueError(f"{path}: expected YAML frontmatter between --- delimiters")
            record = _yaml(frontmatter[1], path)
            _fields(record, ("id", "source", "parent", "title", "type", "caption"), path)
            items.append(Item(**record, body=text[frontmatter.end():], category=category.name, path=path))
    return items


def validate(trees, items):
    sources = {}
    for tree in trees:
        _strings(tree.path, source=tree.source, title=tree.title, category=tree.category)
        if tree.path.stem != tree.source:
            raise ValueError(f"{tree.path}: filename must match Source ID {tree.source!r}")
        if tree.source in sources:
            raise ValueError(f"{tree.path}: duplicate Source tree {tree.source!r}")
        nodes = {}
        for node in tree.nodes:
            _strings(tree.path, node_id=node.id, node_title=node.title)
            if node.parent is not None:
                _strings(tree.path, node_parent=node.parent)
            if node.id in nodes:
                raise ValueError(f"{tree.path}: duplicate TreeNode ID {node.id!r}")
            nodes[node.id] = node
        for node in tree.nodes:
            if node.parent is not None and node.parent not in nodes:
                raise ValueError(f"{tree.path}: TreeNode {node.id!r} has missing parent {node.parent!r}")
        finished = set()
        for node in tree.nodes:
            visiting = set()
            cursor = node.id
            while cursor is not None and cursor not in finished:
                if cursor in visiting:
                    raise ValueError(f"{tree.path}: TreeNode parent cycle involving {cursor!r}")
                visiting.add(cursor)
                cursor = nodes[cursor].parent
            finished.update(visiting)
        sources[tree.source] = (tree, nodes)
    identifiers = set()
    for item in items:
        _strings(item.path, id=item.id, source=item.source, parent=item.parent, title=item.title, type=item.type, caption=item.caption)
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", item.id):
            raise ValueError(f"{item.path}: invalid Item ID {item.id!r}; use lowercase letters, digits and hyphens")
        if item.path.stem != item.id:
            raise ValueError(f"{item.path}: filename must match Item ID {item.id!r}")
        if item.id in identifiers:
            raise ValueError(f"{item.path}: duplicate Item ID {item.id!r}")
        identifiers.add(item.id)
        if item.type not in ITEM_TYPES:
            raise ValueError(f"{item.path}: invalid Item type {item.type!r}")
        if item.source not in sources:
            raise ValueError(f"{item.path}: no Source tree for {item.source!r}")
        tree, nodes = sources[item.source]
        if item.category != tree.category:
            raise ValueError(f"{item.path}: Item and Source tree categories differ")
        if item.parent not in nodes:
            raise ValueError(f"{item.path}: missing Item parent {item.parent!r} in Source {item.source!r}")


def load_tree(root, examples):
    root = Path(root).resolve()
    base = root / "01_tree"
    if examples:
        base /= "example_tree"
    registry = {} if examples else load_registry(root)
    trees = load_trees(base, registry, examples)
    items = load_items(base)
    validate(trees, items)
    return trees, items


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("validate", "render"):
        command = commands.add_parser(name)
        command.add_argument("--examples", action="store_true", help="use only isolated example fixtures")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    try:
        trees, items = load_tree(root, args.examples)
        if args.command == "render":
            from tree_html import render_page, write_html
            output = root / "01_tree"
            if args.examples:
                output /= "example_tree"
            output /= "index.html"
            write_html(render_page(trees, items, args.examples), output)
            print(f"Viewer: {output}")
        else:
            print(f"Valid: {len(trees)} Sources, {sum(len(t.nodes) for t in trees)} TreeNodes, {len(items)} Items")
        return 0
    except (ValueError, OSError, ImportError) as error:
        print(error, file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
