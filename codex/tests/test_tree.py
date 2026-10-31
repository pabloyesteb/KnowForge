"""Focused structural and viewer tests using temporary copies of the examples."""
from contextlib import redirect_stderr
from html.parser import HTMLParser
import io
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import tree
import tree_html


class MathRenderingTests(unittest.TestCase):
    def test_all_math_delimiters(self):
        for opening, closing, display in [
            (r"\(", r"\)", "inline"), (r"\[", r"\]", "block"),
            ("$", "$", "inline"), ("$$", "$$", "block"),
        ]:
            with self.subTest(opening=opening):
                formula = r"\operatorname{tr}(ABC)=\operatorname{tr}(BCA)"
                math = opening + ("\n" if display == "block" else "") + formula
                math += ("\n" if display == "block" else "") + closing
                prefixes = ("", "A trace identity:\n\n" if opening == "$$" else "A trace identity:\n")
                for prefix in prefixes:
                    rendered = tree_html.render_markdown(prefix + math)
                    self.assertEqual(rendered.count("<math "), 1)
                    self.assertIn(f'display="{display}"', rendered)
                    self.assertNotIn(r"\operatorname", rendered)

    def test_display_math_preserves_adjacent_prose_and_literal_code(self):
        rendered = tree_html.render_markdown(
            "Before.\n\\[\nx^2\n\\]\nAfter.\n\n"
            "`\\[literal\\]`\n\n```latex\n\\[literal\\]\n```\n")
        self.assertEqual(rendered.count("<math "), 1)
        self.assertIn("Before.</p>", rendered)
        self.assertIn("<p>After.</p>", rendered)
        self.assertIn(r"<code>\[literal\]</code>", rendered)
        self.assertIn(r"\[literal\]", rendered.split("<pre>", 1)[1])


class TreeTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.base = self.root / "01_tree/example_tree"
        shutil.copytree(ROOT / "01_tree/example_tree", self.base,
                        ignore=shutil.ignore_patterns("index.html"))
        self.item = self.base / "tum/items/example-kkt.md"
        self.source = self.base / "tum/trees/example-optimization.yaml"

    def registry(self):
        path = self.root / "00_sources/inventory/sources.yaml"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump({"project": {"name": "test"}, "sources": {
            "sample-course": {"title": "Sample Course", "type": "course",
                              "locations": {"archive": "../raw/tum/sample.zip"}}
        }}))
        return path

    def edit(self, path, before, after):
        text = path.read_text()
        self.assertIn(before, text)
        path.write_text(text.replace(before, after))

    def test_examples_and_original_markdown_body(self):
        trees, items = tree.load_tree(self.root, True)
        self.assertEqual((len(trees), sum(len(t.nodes) for t in trees), len(items)), (2, 7, 4))
        kkt = next(i for i in items if i.id == "example-kkt")
        self.assertEqual(kkt.body, self.item.read_text().split("\n---\n", 1)[1])

    def test_empty_production_and_nodes_without_items(self):
        self.registry()
        self.assertEqual(tree.load_tree(self.root, False), ([], []))
        for path in self.base.glob("*/items/*.md"):
            path.unlink()
        self.assertEqual(len(tree.load_tree(self.root, True)[0]), 2)

    def test_registered_sources_and_dataset_separation(self):
        registry = self.registry()
        production = self.root / "01_tree/tum/trees"
        production.mkdir(parents=True)
        (production.parent / "items").mkdir()
        source = production / "sample-course.yaml"
        source.write_text("source: sample-course\nnodes: []\n")
        # Even a fixture root shaped like a category must stay out of production.
        (self.base / "trees").mkdir()
        (self.base / "items").mkdir()
        shutil.copy(self.source, self.base / "trees" / self.source.name)
        self.assertEqual([t.source for t in tree.load_tree(self.root, False)[0]], ["sample-course"])
        self.assertEqual(len(tree.load_tree(self.root, True)[0]), 2)
        source.write_text("source: unregistered\nnodes: []\n")
        with self.assertRaisesRegex(ValueError, "unknown production Source"):
            tree.load_tree(self.root, False)
        registry.write_text("not: [valid")
        self.assertEqual(len(tree.load_tree(self.root, True)[1]), 4)

    def test_registry_paths_and_arbitrary_category_with_other_type(self):
        path = self.registry()
        location = tree.load_registry(self.root)["sample-course"]["locations"]["archive"]
        self.assertEqual(location, (path.parent / "../raw/tum/sample.zip").resolve())
        category = self.root / "01_tree/field-research"
        (category / "trees").mkdir(parents=True)
        (category / "items").mkdir()
        (category / "trees/sample-course.yaml").write_text(
            "source: sample-course\nnodes:\n  - id: section\n    title: Section\n    parent: null\n")
        item = category / "items/sample-item.md"
        item.write_text("---\nid: sample-item\nsource: sample-course\nparent: section\n"
                        "title: A substantive Item\ntype: other\ncaption: Describes the example content.\n---\n\nContent.\n")
        trees, items = tree.load_tree(self.root, False)
        self.assertEqual((trees[0].category, items[0].category, items[0].type),
                         ("field-research", "field-research", "other"))
        self.assertEqual(trees[0].title, "Sample Course")
        navigation = tree_html.render_navigation(trees, items)
        self.assertIn("Field Research</summary>", navigation)
        self.assertNotIn("Projects</summary>", navigation)
        self.assertIn("<small>other</small>", navigation)
        mismatch = self.root / "01_tree/another-category"
        (mismatch / "trees").mkdir(parents=True)
        (mismatch / "items").mkdir()
        item.rename(mismatch / "items" / item.name)
        with self.assertRaisesRegex(ValueError, "categories differ"):
            tree.load_tree(self.root, False)

    def test_category_discovery_requires_both_directories_and_is_immediate(self):
        incomplete = self.base / "incomplete/trees"
        incomplete.mkdir(parents=True)
        (incomplete / "invalid.yaml").write_text("invalid: true\n")
        nested = self.base / "container/nested-category"
        (nested / "trees").mkdir(parents=True)
        (nested / "items").mkdir()
        (nested / "trees/invalid.yaml").write_text("invalid: true\n")
        self.assertEqual(len(tree.load_tree(self.root, True)[0]), 2)

    def test_invalid_metadata_and_identifiers(self):
        original = self.item.read_text()
        cases = [
            ("id: example-kkt", "id: ../invalid", "invalid Item ID"),
            ("id: example-kkt", "id: different-id", "filename must match"),
            ("type: theorem", "type: unknown", "invalid Item type"),
            ("type: theorem\n", "", "expected fields"),
            ("type: theorem", "type: [", "invalid YAML"),
            ("title: Karush–Kuhn–Tucker Necessary Conditions", "title: 42", "nonempty string"),
            ("---\n", "", "frontmatter"),
        ]
        for before, after, reason in cases:
            with self.subTest(reason=reason):
                self.item.write_text(original.replace(before, after))
                with self.assertRaisesRegex(ValueError, reason) as caught:
                    tree.load_tree(self.root, True)
                self.assertIn(str(self.item), str(caught.exception))

    def test_invalid_references(self):
        original = self.item.read_text()
        for before, after, reason in [
            ("parent: example-constrained", "parent: missing", "missing Item parent"),
            ("source: example-optimization", "source: missing", "no Source tree"),
        ]:
            with self.subTest(reason=reason):
                self.item.write_text(original.replace(before, after))
                with self.assertRaisesRegex(ValueError, reason):
                    tree.load_tree(self.root, True)

    def test_node_parent_duplicates_and_cycle(self):
        original = self.source.read_text()
        for kind in ("parent", "duplicate", "cycle"):
            with self.subTest(kind=kind):
                document = yaml.safe_load(original)
                if kind == "parent":
                    document["nodes"][0]["parent"] = "missing"
                elif kind == "duplicate":
                    document["nodes"].append(dict(document["nodes"][0]))
                else:
                    document["nodes"][0]["parent"] = "example-optimality"
                    document["nodes"][1]["parent"] = "example-foundations"
                self.source.write_text(yaml.safe_dump(document))
                with self.assertRaisesRegex(ValueError, {"parent": "missing parent", "duplicate": "duplicate TreeNode", "cycle": "cycle"}[kind]):
                    tree.load_tree(self.root, True)

    def test_duplicate_items_and_category_mismatch(self):
        duplicate = self.base / "projects/items/example-kkt.md"
        duplicate.write_text(self.item.read_text().replace("example-optimization", "example-research-project")
                             .replace("parent: example-constrained", "parent: example-project-solvers"))
        with self.assertRaisesRegex(ValueError, "duplicate Item ID"):
            tree.load_tree(self.root, True)
        duplicate.write_text(self.item.read_text())
        self.item.unlink()
        with self.assertRaisesRegex(ValueError, "categories differ"):
            tree.load_tree(self.root, True)

    def test_no_editorial_validation(self):
        self.item.write_text(self.item.read_text().split("\n---\n", 1)[0] + "\n---\n")
        self.assertEqual(len(tree.load_tree(self.root, True)[1]), 4)

    def test_caption_is_required_and_nonempty(self):
        original = self.item.read_text()
        for value in (None, "", "   ", 42):
            with self.subTest(caption=value):
                front, body = original.split("\n---\n", 1)
                metadata = yaml.safe_load(front[4:])
                if value is None:
                    del metadata["caption"]
                else:
                    metadata["caption"] = value
                self.item.write_text("---\n" + yaml.safe_dump(metadata) + "---\n" + body)
                with self.assertRaisesRegex(ValueError, "caption"):
                    tree.load_tree(self.root, True)

    def test_captions_displayed_and_escaped(self):
        trees, items = tree.load_tree(self.root, True)
        items[0].caption = 'Explains <script>alert("caption")</script> safely.'
        page = tree_html.render_page(trees, items, True)
        self.assertEqual(page.count('class="caption"'), 2 * len(items))
        self.assertEqual(page.count('Explains &lt;script&gt;alert(&quot;caption&quot;)&lt;/script&gt; safely.'), 2)
        self.assertNotIn('<script>alert("caption")</script>', page)
        for item in items[1:]:
            self.assertEqual(page.count(item.caption), 2)

    def test_markdown_math_and_safe_html(self):
        text = tree_html.render_markdown('Before $x^2$ and \\(y>0\\) after. `$code$`\n\n'
                                        '$$\nx+y\n$$\n\n| A | B |\n|---|---|\n| 1 | 2 |\n\n'
                                        '<script>alert(1)</script><img src=x onerror=alert(1)>\n\n'
                                        '[unsafe](javascript:alert(1))\n\n'
                                        '$\\text{<img src=x onerror=alert(1)>}$')
        self.assertEqual(text.count("<math "), 4)
        self.assertIn(" and ", text)
        self.assertIn(" after.", text)
        self.assertIn("<code>$code$</code>", text)
        self.assertIn("<table>", text)
        parser = HTMLParser()
        tags = []
        parser.handle_starttag = lambda tag, attrs: tags.append((tag, dict(attrs)))
        parser.feed(text)
        self.assertFalse(any(t in {"script", "img", "iframe"} for t, _ in tags))
        self.assertFalse(any(k.startswith("on") or v.startswith("javascript:") for _, attrs in tags for k, v in attrs.items()))

    def test_rendered_examples_navigation_order_and_escaped_metadata(self):
        trees, items = tree.load_tree(self.root, True)
        navigation = tree_html.render_navigation(trees, items)
        self.assertIn("Career Profile</summary>", navigation)
        self.assertIn("Projects</summary>", navigation)
        self.assertIn("Tum</summary>", navigation)
        self.assertLess(navigation.index("Unconstrained Optimization</summary>"), navigation.index("Constrained Optimization</summary>"))
        for item in items:
            self.assertIn(item.id, navigation)
        items[0].title = '<script>alert("metadata")</script>'
        trees[0].title = '<script>alert("metadata")</script>'
        trees[0].nodes[0].title = '<script>alert("metadata")</script>'
        page = tree_html.render_page(trees, items, True)
        self.assertNotIn('<script>alert("metadata")</script>', page)
        self.assertIn("Isolated fictional examples", page)
        self.assertNotIn("<script src=", page)
        self.assertIn('id="search"', page)

    def test_empty_viewer_and_failed_generation_preserve_output(self):
        self.registry()
        trees, items = tree.load_tree(self.root, False)
        page = tree_html.render_page(trees, items, False)
        self.assertIn("dataset is empty", page)
        self.assertNotIn("example-kkt", page)
        output = self.base / "index.html"
        tree_html.write_html(page, output)
        self.assertEqual(output.read_text(), page)
        self.edit(self.item, "type: theorem", "type: invalid")
        stderr = io.StringIO()
        with patch.object(tree, "__file__", str(self.root / "scripts/tree.py")), \
                patch.object(sys, "argv", ["tree.py", "render", "--examples"]), redirect_stderr(stderr):
            self.assertEqual(tree.main(), 1)
        self.assertIn(str(self.item), stderr.getvalue())
        self.assertEqual(output.read_text(), page)
        with patch("tree_html.os.replace", side_effect=OSError("write failed")):
            with self.assertRaises(OSError):
                tree_html.write_html("replacement", output)
        self.assertEqual(output.read_text(), page)

    def test_failed_render_does_not_reach_output_write(self):
        trees, items = tree.load_tree(self.root, True)
        output = self.base / "index.html"
        output.write_text("previous viewer")
        with patch("tree_html.render_markdown", side_effect=RuntimeError("conversion failed")):
            with self.assertRaisesRegex(ValueError, "Markdown rendering failed"):
                tree_html.write_html(tree_html.render_page(trees, items, True), output)
        self.assertEqual(output.read_text(), "previous viewer")

    def test_cli_from_other_working_directory(self):
        result = subprocess.run([sys.executable, str(ROOT / "scripts/tree.py"),
                                 "validate", "--examples"], cwd=self.root, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("4 Items", result.stdout)


if __name__ == "__main__":
    unittest.main()
