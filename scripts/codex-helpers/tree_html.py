"""Render already-loaded Tree objects as one offline, read-only HTML document."""
from collections import defaultdict
from html import escape
import os
from pathlib import Path
import tempfile

import bleach
from latex2mathml.converter import convert
from markdown_it import MarkdownIt
from mdit_py_plugins.dollarmath import dollarmath_plugin
from mdit_py_plugins.texmath import texmath_plugin


def _math(text, options):
    try:
        return convert(text, display="block" if options["display_mode"] else "inline")
    except Exception:
        return f'<code>Unrendered TeX: {escape(text)}</code>'


def render_markdown(text):
    parser = MarkdownIt("commonmark", {"html": False}).enable("table")
    parser.use(texmath_plugin, delimiters="brackets")
    parser.use(dollarmath_plugin, allow_labels=False, renderer=_math)
    parser.block.ruler.disable(["math_block_eqno"])
    tags = {
        "p", "br", "hr", "h1", "h2", "h3", "h4", "h5", "h6", "ul", "ol", "li",
        "strong", "em", "blockquote", "pre", "code", "a", "table", "thead", "tbody",
        "tr", "th", "td", "span", "div", "math", "mrow", "mi", "mn", "mo", "mtext",
        "msup", "msub", "msubsup", "mfrac", "msqrt", "mroot", "mtable", "mtr", "mtd",
        "mover", "munder", "munderover", "mspace", "mstyle", "mpadded", "mphantom",
        "mfenced", "menclose", "mmultiscripts", "mprescripts", "none",
    }
    attributes = {
        "*": ["class"], "a": ["href", "title"], "ol": ["start"],
        "math": ["xmlns", "display"], "mi": ["mathvariant"],
        "mo": ["stretchy", "fence", "accent", "symmetric", "lspace", "rspace"],
        "mstyle": ["displaystyle", "scriptlevel", "mathvariant"],
        "mtable": ["columnalign", "columnspacing", "rowspacing"], "mtd": ["columnalign"],
        "mspace": ["width", "height", "depth"], "mfrac": ["linethickness"],
        "mover": ["accent"], "munder": ["accentunder"], "menclose": ["notation"],
        "mpadded": ["width", "height", "depth", "voffset"],
    }
    return bleach.clean(parser.render(text), tags=tags, attributes=attributes,
                        protocols={"http", "https", "mailto"}, strip=True)


def render_navigation(trees, items):
    html = ['<details id="career-root" open><summary>Career Profile</summary>']
    for category in sorted({tree.category for tree in trees}):
        label = category.replace("-", " ").replace("_", " ").title()
        html.append(f'<details class="branch" open><summary>{escape(label)}</summary>')
        for tree in (t for t in trees if t.category == category):
            children = defaultdict(list)
            for node in tree.nodes:
                children[node.parent].append(node)
            placements = defaultdict(list)
            for item in items:
                if item.source == tree.source:
                    placements[item.parent].append(item)

            def nodes(parent):
                for node in children[parent]:
                    html.append(f'<details class="branch" open><summary>{escape(node.title)}</summary>')
                    for item in sorted(placements[node.id], key=lambda i: (i.title.casefold(), i.id)):
                        html.append(f'<button class="item" type="button" data-item="{escape(item.id, quote=True)}" '
                                    f'data-title="{escape(item.title, quote=True)}">{escape(item.title)}'
                                    f'<small>{escape(item.type)}</small></button>')
                    nodes(node.id)
                    html.append("</details>")

            html.append(f'<details class="branch" data-source="{escape(tree.source, quote=True)}" open>'
                        f'<summary>{escape(tree.title)}</summary>')
            nodes(None)
            html.append("</details>")
        html.append("</details>")
    html.append("</details>")
    return "".join(html)


CSS = """
*{box-sizing:border-box}body{margin:0;font:16px/1.6 system-ui,sans-serif;color:#17212b;background:#fff}
[hidden]{display:none!important}.layout{display:grid;grid-template-columns:320px minmax(0,1fr)}
nav{height:100vh;overflow:auto;position:sticky;top:0;padding:1rem;border-right:1px solid #ddd}
main{padding:2rem;max-width:1100px;min-width:0}details details{margin-left:.8rem}summary{cursor:pointer;padding:.3rem 0}
button.item{display:block;width:100%;border:0;background:none;text-align:left;padding:.5rem;cursor:pointer;color:inherit}
button.item:hover,button.item[aria-current=true]{background:#e4edf7}small{display:block;opacity:.7}
input{width:100%;padding:.6rem;font:inherit}.meta,#status{font-size:.85rem;color:#54616e}
pre,.math.block{overflow:auto;padding:.5rem}pre{background:#f2f4f7}code{font-family:monospace}
table{border-collapse:collapse;display:block;overflow:auto}td,th{border:1px solid #ccc;padding:.4rem}
blockquote{border-left:3px solid #ccc;padding-left:1rem}a{color:#125aa0}
@media(max-width:700px){.layout{display:block}nav{height:auto;max-height:45vh;position:static}main{padding:1rem}}
"""

JS = """
const buttons=[...document.querySelectorAll('button.item')];
const articles=[...document.querySelectorAll('article')];
for(const button of buttons) button.addEventListener('click',()=>{
  for(const article of articles) article.hidden=article.dataset.item!==button.dataset.item;
  for(const other of buttons) other.setAttribute('aria-current',String(other===button));
  document.querySelector('#welcome').hidden=true;
});
document.querySelector('#search').addEventListener('input',event=>{
  const query=event.target.value.trim().toLocaleLowerCase();
  for(const button of buttons) button.hidden=!button.dataset.title.toLocaleLowerCase().includes(query);
  for(const branch of document.querySelectorAll('.branch')){
    branch.hidden=Boolean(query)&&!branch.querySelector('button.item:not([hidden])');
    if(query&&!branch.hidden) branch.open=true;
  }
  document.querySelector('#status').textContent=buttons.filter(b=>!b.hidden).length+' matching Items';
});
"""


def render_page(trees, items, examples):
    mode = "Isolated fictional examples — not evidence of personal experience" if examples else "Production Tree"
    articles = []
    for item in sorted(items, key=lambda i: i.id):
        try:
            content = render_markdown(item.body)
        except Exception as error:
            raise ValueError(f"{item.path}: Markdown rendering failed: {error}") from error
        articles.append(f'<article data-item="{escape(item.id, quote=True)}" hidden>'
                        f'<p class="meta">{escape(item.title)} · {escape(item.source)} · Type: {escape(item.type)}</p>'
                        f'{content}</article>')
    message = "Select an Item to read it." if items else "No Items yet. The dataset is empty."
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Career Profile — Tree</title><style>{CSS}</style></head>
<body><div class="layout"><nav aria-label="Knowledge tree"><p class="meta">{escape(mode)}</p>
<label for="search">Search Item titles</label><input type="search" id="search" autocomplete="off">
<p id="status" role="status">{len(items)} Items</p>{render_navigation(trees, items)}</nav>
<main><section id="welcome"><h1>Knowledge Tree</h1><p>{message}</p>
<p>{len(trees)} Sources · {len(items)} Items.</p><p>Display order does not represent source chronology.</p>
<noscript>Enable JavaScript for Item selection and title search.</noscript></section>{''.join(articles)}</main>
</div><script>{JS}</script></body></html>
'''


def write_html(html, path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(html)
        os.replace(temporary, path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
