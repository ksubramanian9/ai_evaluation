"""Build the static website from the Markdown map.

Usage (from repo root):  python tools/build_site.py [--out site] [--stale-days 90]

Output is plain static HTML with relative links and no runtime fetches, so it
works from file:// and on any static host (e.g. GitHub Pages).
Requires: pip install markdown   (see requirements.txt)
"""
import argparse
import datetime as dt
import html
import json
import pathlib
import re
import shutil
import sys

import markdown

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_views as bv  # noqa: E402

ROOT = bv.ROOT
ASSETS = pathlib.Path(__file__).resolve().parent / "site"

BRANCH_INFO = {
    "01-foundations": ("Foundations", "Statistics, ML metrics, testing basics and the mindset every later branch relies on."),
    "02-eval-design": ("Eval design", "Defining tasks, rubrics, golden datasets and metrics so an evaluation measures the right thing."),
    "03-measurement-methods": ("Measurement methods", "Programmatic checks, LLM judges, human review and benchmarks, with their uncertainty."),
    "04-system-specific-evals": ("System-specific evals", "Evaluating RAG, agents, tool use, code, conversation, long context and multimodal systems."),
    "05-testing-in-engineering": ("Testing in engineering", "Regression suites, CI gates, red teaming, robustness and safety as engineering practice."),
    "06-production": ("Production", "Tracing, drift, online experiments, guardrails and feeding production data back into evals."),
    "07-operating-practice": ("Operating practice", "Tooling, cost, reporting, governance, regulation and running evaluation as a team."),
}
STATUSES = bv.STATUSES
DEPTH_LABEL = {"L1": "Awareness", "L2": "Working", "L3": "Expert"}
BRIDGE_LABEL = {"stats": "Stats bridge", "testing": "Testing bridge", "none": "No bridge"}
MD_EXT = ["tables", "fenced_code", "toc", "sane_lists", "attr_list"]


def esc(s):
    return html.escape(str(s), quote=True)


def render(text):
    m = markdown.Markdown(extensions=MD_EXT)
    out = m.convert(text)
    return out, m.toc_tokens


def strip_frontmatter(text):
    return re.sub(r"\A---\n.*?\n---\n", "", text, count=1, flags=re.S)


def branch_label(b):
    return BRANCH_INFO.get(b, (b, ""))[0]


def branch_num(b):
    return b.split("-")[0]


# ---------------------------------------------------------------- data

def layers(nodes):
    memo = {}

    def depth(i):
        if i not in memo:
            ps = nodes[i]["prerequisites"]
            memo[i] = 0 if not ps else 1 + max(depth(p) for p in ps)
        return memo[i]

    for i in nodes:
        depth(i)
    return memo


def load_candidates():
    out = {}
    for p in sorted(bv.MAP.glob("*/_candidates.md")):
        items = []
        for line in p.read_text(encoding="utf-8").splitlines():
            if line.startswith("- ") and not line.startswith("- See the"):
                items.append(line[2:].strip())
        out[p.parent.name] = items
    return out


def load_landscape(stale_days):
    today = dt.date.today()
    out = {}
    for p in sorted((ROOT / "landscape").glob("*.md")):
        items = []
        for line in p.read_text(encoding="utf-8").splitlines():
            if not line.startswith("- ") or "(none yet)" in line or line.startswith("- <item>"):
                continue
            m = re.search(r"as-of:\s*(\d{4}-\d{2}-\d{2})", line)
            if not m:
                continue
            date = dt.date.fromisoformat(m.group(1))
            text = line[2:].replace(m.group(0), "").strip()
            text = re.sub(r"\s*\|\s*$", "", text).strip()
            text = re.sub(r"\s*\|\s*", " ", text)
            typ = re.search(r"\(type:\s*([a-z]+)\)", text)
            if typ:
                text = text.replace(typ.group(0), "").strip()
            items.append({"text": text, "type": typ.group(1) if typ else "", "asof": m.group(1),
                          "age": (today - date).days, "stale": (today - date).days > stale_days})
        out[p.stem] = items
    return out


def rewrite_external(h):
    return re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" target="_blank" rel="noopener"', h)


def inline_md(text):
    h = markdown.markdown(text)
    h = re.sub(r"^<p>(.*)</p>$", r"\1", h, flags=re.S)
    h = re.sub(r'(?<![">])(https?://[^\s<)]+[^\s<).,;])', r'<a href="\1">\1</a>', h)
    return rewrite_external(h)


# ---------------------------------------------------------------- link rewriting

class Linker:
    def __init__(self, nodes):
        self.nodes = nodes

    def rewrite(self, h, root):
        def sub(m):
            href = m.group(1)
            if re.match(r"(https?:|mailto:|#)", href):
                return m.group(0)
            path, _, frag = href.partition("#")
            frag = "#" + frag if frag else ""
            name = pathlib.PurePosixPath(path).name
            if not name.endswith(".md"):
                return m.group(0)
            stem = name[:-3]
            if "research/" in path:
                return f'<a href="{root}research/{stem}.html{frag}"'
            if stem in self.nodes:
                return f'<a href="{root}nodes/{stem}.html{frag}"'
            if "landscape/" in path:
                return f'<a href="{root}landscape.html"'
            return m.group(0)
        h = re.sub(r'<a href="([^"]+)"', sub, h)
        return rewrite_external(h)


# ---------------------------------------------------------------- page shell

def badge(kind, value, label=None):
    return f'<span class="badge {kind} {kind}-{esc(value)}">{esc(label or value)}</span>'


def status_dot(s):
    return f'<span class="dot st-{esc(s)}" title="{esc(s)}"></span>'


def sidebar(nodes, root, current_node=None, current_branch=None):
    br = bv.branches(nodes)
    parts = ['<nav class="side" aria-label="Map navigation">']
    parts.append(f'<a class="side-top" href="{root}nodes.html">All nodes</a>'
                 f'<a class="side-top" href="{root}path.html">Learning path</a>'
                 f'<a class="side-top" href="{root}graph.html">Prerequisite graph</a>')
    parts.append('<div class="side-h">Branches</div>')
    for b, ns in br.items():
        is_open = (b == current_branch)
        parts.append(f'<details class="side-branch"{" open" if is_open else ""}>'
                     f'<summary><span class="bnum b{branch_num(b)}">{branch_num(b)}</span>'
                     f'<a href="{root}branches/{b}.html">{esc(branch_label(b))}</a></summary><ul>')
        for n in ns:
            cur = ' aria-current="page"' if n["id"] == current_node else ""
            parts.append(f'<li><a href="{root}nodes/{n["id"]}.html"{cur}>{status_dot(n["status"])}{esc(n["title"])}</a></li>')
        parts.append("</ul></details>")
    parts.append('<div class="side-h">More</div>')
    parts.append(f'<a class="side-top" href="{root}landscape.html">Landscape</a>'
                 f'<a class="side-top" href="{root}capstone.html">Capstone</a>'
                 f'<a class="side-top" href="{root}about.html">About</a>')
    parts.append("</nav>")
    return "".join(parts)


def page(title, body, nodes, root="", current_node=None, current_branch=None, toc="", wide=False, desc=""):
    full_title = f"{title} · AI Evaluation Map" if title != "AI Evaluation Map" else title
    toc_block = f'<aside class="toc" aria-label="On this page"><div class="toc-h">On this page</div>{toc}</aside>' if toc else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full_title)}</title>
<meta name="description" content="{esc(desc or 'A curriculum and decision guide for evaluating and testing AI systems.')}">
<script>try{{var t=localStorage.getItem('theme');if(t)document.documentElement.dataset.theme=t;}}catch(e){{}}</script>
<link rel="stylesheet" href="{root}assets/style.css">
</head>
<body data-root="{root}">
<a class="skip" href="#main">Skip to content</a>
<header class="top">
  <button class="icon-btn menu-btn" aria-label="Toggle navigation" aria-expanded="false">☰</button>
  <a class="brand" href="{root}index.html"><span class="brand-mark">◈</span> AI Evaluation Map</a>
  <button class="search-btn" aria-label="Search" data-open-search><span>Search the map</span><kbd>/</kbd></button>
  <button class="icon-btn theme-btn" aria-label="Toggle dark mode">◐</button>
</header>
<div class="shell">
  {sidebar(nodes, root, current_node, current_branch)}
  <main id="main" class="main{' wide' if wide else ''}">
  {body}
  </main>
  {toc_block}
</div>
<div class="scrim" hidden></div>
<div class="palette" role="dialog" aria-modal="true" aria-label="Search" hidden>
  <div class="palette-box">
    <input type="search" placeholder="Search nodes, topics, sources…" aria-label="Search query" autocomplete="off">
    <div class="results" role="listbox"></div>
    <div class="palette-foot"><span><kbd>↑</kbd><kbd>↓</kbd> move</span><span><kbd>↵</kbd> open</span><span><kbd>esc</kbd> close</span></div>
  </div>
</div>
<script src="{root}assets/search-index.js"></script>
<script src="{root}assets/app.js"></script>
</body>
</html>
"""


def toc_html(tokens):
    def walk(ts):
        if not ts:
            return ""
        return "<ul>" + "".join(f'<li><a href="#{esc(t["id"])}">{esc(t["name"])}</a>{walk(t["children"])}</li>' for t in ts) + "</ul>"
    return walk(tokens)


# ---------------------------------------------------------------- components

def node_card(n, root):
    tags = " ".join(n.get("tags", []))
    return (f'<a class="card node-item" href="{root}nodes/{n["id"]}.html" data-branch="{branch_num(n["branch"])}" '
            f'data-depth="{esc(n["depth"])}" data-status="{esc(n["status"])}" data-bridge="{esc(n["bridge"])}" '
            f'data-tags="{esc(tags)}" data-text="{esc((n["title"] + " " + n["summary"]).lower())}">'
            f'<div class="card-top"><span class="bnum b{branch_num(n["branch"])}">{branch_num(n["branch"])}</span>'
            f'{badge("depth", n["depth"], n["depth"])}{badge("status", n["status"])}</div>'
            f'<div class="card-title">{esc(n["title"])}</div>'
            f'<div class="card-sum">{esc(n["summary"])}</div></a>')


def filter_bar(nodes, with_branch=True):
    def opts(vals):
        return "".join(f'<option value="{esc(v)}">{esc(l)}</option>' for v, l in vals)
    br = [(branch_num(b), f"{branch_num(b)} {branch_label(b)}") for b in bv.branches(nodes)]
    tags = sorted({t for n in nodes.values() for t in n.get("tags", [])})
    branch_sel = f'<select data-f="branch" aria-label="Branch"><option value="">All branches</option>{opts(br)}</select>' if with_branch else ""
    tag_sel = f'<select data-f="tag" aria-label="Tag"><option value="">Any tag</option>{opts([(t, t) for t in tags])}</select>' if tags else ""
    return f"""<div class="filters" role="search" aria-label="Filter nodes">
  <input type="search" data-f="q" placeholder="Filter by title…" aria-label="Filter by title">
  {branch_sel}
  <select data-f="depth" aria-label="Depth"><option value="">Any depth</option>{opts([(d, f"{d} {l}") for d, l in DEPTH_LABEL.items()])}</select>
  <select data-f="status" aria-label="Status"><option value="">Any status</option>{opts([(s, s) for s in STATUSES])}</select>
  <select data-f="bridge" aria-label="Bridge"><option value="">Any bridge</option>{opts(list(BRIDGE_LABEL.items()))}</select>
  {tag_sel}
  <span class="count" aria-live="polite"></span>
</div>"""


def segbar(ns):
    total = len(ns) or 1
    segs = "".join(f'<span class="seg st-{s}" style="width:{100 * sum(1 for n in ns if n["status"] == s) / total:.1f}%"></span>' for s in STATUSES)
    return f'<div class="segbar" role="img" aria-label="Status breakdown">{segs}</div>'


def summarize(node_md):
    body = strip_frontmatter(node_md)
    for para in re.split(r"\n\s*\n", body):
        p = para.strip()
        if p and not p.startswith("#") and not p.startswith("_Researched"):
            return re.sub(r"\s+", " ", re.sub(r"[`*_]", "", p))
    return ""


# ---------------------------------------------------------------- build

def build(out, stale_days):
    nodes = bv.load()
    errs = bv.validate(nodes)
    if errs:
        print("\n".join(errs))
        sys.exit(1)
    lay = layers(nodes)
    linker = Linker(nodes)
    br = bv.branches(nodes)
    cands = load_candidates()
    landscape = load_landscape(stale_days)
    stale_total = sum(1 for v in landscape.values() for i in v if i["stale"])

    unlocks = {i: [] for i in nodes}
    for n in nodes.values():
        for q in n["prerequisites"]:
            unlocks[q].append(n["id"])
    texts = {}
    for n in nodes.values():
        raw = (ROOT / n["path"]).read_text(encoding="utf-8")
        texts[n["id"]] = raw
        n["summary"] = summarize(raw)
        n["tags"] = n["tags"] if isinstance(n.get("tags"), list) else []
        n["layer"] = lay[n["id"]]

    if out.exists():
        shutil.rmtree(out)
    (out / "assets").mkdir(parents=True)
    for d in ("nodes", "branches", "research"):
        (out / d).mkdir()
    for f in ASSETS.iterdir():
        shutil.copy(f, out / "assets" / f.name)
    (out / ".nojekyll").write_text("")

    # research pages and per-node research sections
    research_sections = {}
    for p in sorted((ROOT / "research").glob("*.md")):
        text = p.read_text(encoding="utf-8")
        h, toc = render(text)
        h = linker.rewrite(h, "../")
        title = "Research: " + branch_label(p.stem)
        body = (f'<div class="crumbs"><a href="../index.html">Home</a> / Research</div><h1>{esc(title)}</h1>'
                f'<p class="lede">Sourced notes the {esc(branch_label(p.stem))} nodes were written from. Claims marked UNVERIFIED were not confirmed against a fetched primary page.</p>'
                f'<article class="prose">{h}</article>')
        tokens = toc[0]["children"] if toc and toc[0]["level"] == 1 and len(toc) == 1 else toc
        (out / "research" / f"{p.stem}.html").write_text(
            page(title, body, nodes, "../", current_branch=p.stem, toc=toc_html(tokens)), encoding="utf-8")
        for s in re.split(r"(?m)^## ", text)[1:]:
            name, _, rest = s.partition("\n")
            research_sections[(p.stem, name.strip())] = rest.strip()

    index_items = []

    # node pages
    for b, ns in br.items():
        for idx, n in enumerate(ns):
            raw = strip_frontmatter(texts[n["id"]])
            raw = re.sub(r"\A\s*# .*\n", "", raw, count=1)
            h, toc = render(raw)
            h = linker.rewrite(h, "../")
            h = re.sub(r"<p><em>(Researched)", r'<p class="provenance"><em>\1', h)
            sec = research_sections.get((b, n["id"]))
            research_html = ""
            if sec:
                rh, _ = render(sec)
                rh = linker.rewrite(rh, "../")
                research_html = (f'<details class="research"><summary>Research notes and sources for this node '
                                 f'<a href="../research/{b}.html#{n["id"]}">(open full page)</a></summary>'
                                 f'<div class="prose">{rh}</div></details>')

            def rel(ids):
                return "".join(f'<li><a href="{q}.html">{status_dot(nodes[q]["status"])}{esc(nodes[q]["title"])}</a>'
                               f'<span class="muted">{esc(branch_label(nodes[q]["branch"]))}</span></li>' for q in ids)
            pre = rel(n["prerequisites"])
            unl = rel(sorted(unlocks[n["id"]]))
            prev_l = f'<a class="pn" href="{ns[idx - 1]["id"]}.html"><span>← Previous</span>{esc(ns[idx - 1]["title"])}</a>' if idx > 0 else "<span></span>"
            next_l = f'<a class="pn next" href="{ns[idx + 1]["id"]}.html"><span>Next →</span>{esc(ns[idx + 1]["title"])}</a>' if idx < len(ns) - 1 else "<span></span>"
            tags = "".join(f'<span class="tag">#{esc(t)}</span>' for t in n["tags"])
            pre_html = f'<ul class="rel-list">{pre}</ul>' if pre else '<p class="muted">No prerequisites. A good starting point.</p>'
            unl_html = f'<ul class="rel-list">{unl}</ul>' if unl else '<p class="muted">Nothing depends on this yet.</p>'
            body = f"""<div class="crumbs"><a href="../index.html">Home</a> / <a href="../branches/{b}.html">{esc(branch_num(b))} {esc(branch_label(b))}</a></div>
<h1>{esc(n["title"])}</h1>
<div class="meta">{badge("status", n["status"])}{badge("depth", n["depth"], f'{n["depth"]} {DEPTH_LABEL.get(n["depth"], "")}')}{badge("bridge", n["bridge"], BRIDGE_LABEL.get(n["bridge"], n["bridge"]))}{tags}</div>
<div class="rel">
  <section><h2>Before this</h2>{pre_html}</section>
  <section><h2>Unlocks</h2>{unl_html}</section>
</div>
<article class="prose">{h}</article>
{research_html}
<nav class="prevnext" aria-label="Branch navigation">{prev_l}{next_l}</nav>"""
            (out / "nodes" / f'{n["id"]}.html').write_text(
                page(n["title"], body, nodes, "../", current_node=n["id"], current_branch=b, toc=toc_html(toc), desc=n["summary"]),
                encoding="utf-8")
            plain = re.sub(r"\s+", " ", re.sub(r"[#*_`>|\[\]()]", " ", re.sub(r"https?://\S+", "", raw)))
            index_items.append({"t": n["title"], "u": f'nodes/{n["id"]}.html', "b": f'{branch_num(b)} {branch_label(b)}',
                                "g": " ".join(n["tags"]), "x": plain[:6000], "k": "Node"})

    # branch pages
    for b, ns in br.items():
        title, desc = BRANCH_INFO.get(b, (b, ""))
        cl = cands.get(b, [])
        ls = landscape.get(b, [])
        cand_html = ""
        if cl:
            cand_html = ('<h2 id="candidates">Not yet in the map</h2><p class="muted">Topics that might become nodes. Promote one when it matters to your learning.</p><ul class="cands">'
                         + "".join(f"<li>{inline_md(c)}</li>" for c in cl) + "</ul>")
        land_html = ""
        if ls:
            nst = sum(1 for i in ls if i["stale"])
            land_html = (f'<h2 id="landscape">Landscape for this branch</h2><p><a href="../landscape.html#{b}">{len(ls)} dated entries</a>'
                         + (f", {nst} stale." if nst else ".") + "</p>")
        sub = {n["id"]: n for n in ns}
        body = f"""<div class="crumbs"><a href="../index.html">Home</a> / Branch {esc(branch_num(b))}</div>
<h1><span class="bnum big b{branch_num(b)}">{esc(branch_num(b))}</span> {esc(title)}</h1>
<p class="lede">{esc(desc)}</p>
{segbar(ns)}
<div class="legend">{"".join(f'<span>{status_dot(s)}{sum(1 for n in ns if n["status"] == s)} {s}</span>' for s in STATUSES)}</div>
<p><a href="../research/{b}.html">Research notes for this branch →</a></p>
<div class="filterable">{filter_bar(sub, with_branch=False)}<div class="grid">{"".join(node_card(n, "../") for n in ns)}</div></div>
{cand_html}{land_html}"""
        (out / "branches" / f"{b}.html").write_text(page(title, body, nodes, "../", current_branch=b, desc=desc), encoding="utf-8")

    # all nodes
    body = f"""<h1>All nodes</h1><p class="lede">{len(nodes)} nodes across {len(br)} branches. Filter by branch, depth, status, bridge or tag.</p>
<div class="filterable">{filter_bar(nodes)}<div class="grid">{"".join(node_card(n, "") for n in nodes.values())}</div></div>"""
    (out / "nodes.html").write_text(page("All nodes", body, nodes, wide=True), encoding="utf-8")

    # learning path
    stages = {}
    for n in nodes.values():
        stages.setdefault(n["layer"], []).append(n)
    parts = []
    for s in sorted(stages):
        ns = sorted(stages[s], key=lambda n: (n["branch"], n["title"]))
        label = "no prerequisites" if s == 0 else "needs a node from an earlier stage"
        parts.append(f'<section class="stage"><h2 id="stage-{s + 1}"><span class="stage-n">{s + 1}</span> Stage {s + 1} <span class="muted">{label}</span></h2>'
                     f'<div class="grid">{"".join(node_card(n, "") for n in ns)}</div></section>')
    body = f"""<h1>Learning path</h1><p class="lede">Every node sits in the earliest stage where all its prerequisites are in earlier stages. Work through stages in order; within a stage, any order works.</p>
<div class="filterable">{filter_bar(nodes)}{"".join(parts)}</div>"""
    (out / "path.html").write_text(page("Learning path", body, nodes, wide=True), encoding="utf-8")

    # graph
    gdata = {"nodes": [{"id": n["id"], "t": n["title"], "b": branch_num(n["branch"]), "l": n["layer"], "s": n["status"]}
                       for n in sorted(nodes.values(), key=lambda n: (n["layer"], n["branch"], n["title"]))],
             "edges": [[q, n["id"]] for n in nodes.values() for q in n["prerequisites"]],
             "branches": {branch_num(b): branch_label(b) for b in br}}
    (out / "assets" / "graph-data.js").write_text("window.GRAPH=" + json.dumps(gdata) + ";", encoding="utf-8")
    body = """<h1>Prerequisite graph</h1><p class="lede">Columns are learning stages, colours are branches. Hover or focus a node to highlight what it depends on (amber) and what it unlocks (teal). Click to open it.</p>
<div class="graph-legend" id="graph-legend"></div>
<div class="graph-wrap"><svg id="graph" role="img" aria-label="Prerequisite graph of all nodes"></svg></div>
<script src="assets/graph-data.js"></script><script src="assets/graph.js"></script>"""
    (out / "graph.html").write_text(page("Prerequisite graph", body, nodes, wide=True), encoding="utf-8")

    # landscape
    parts = []
    for stem, items in landscape.items():
        label = branch_label(stem)
        rows = ""
        for i in items:
            flag = f'<span class="stale-flag">stale · {i["age"]} days</span>' if i["stale"] else ""
            typ = badge("type", i["type"]) if i["type"] else ""
            rows += (f'<li class="{"stale" if i["stale"] else ""}"><div>{inline_md(i["text"])}</div><div class="ls-meta">'
                     f'{typ}<span class="asof">as of {i["asof"]}</span>{flag}</div></li>')
            index_items.append({"t": re.sub(r"<[^>]+>", "", inline_md(i["text"]))[:90], "u": f"landscape.html#{stem}",
                                "b": "Landscape · " + label, "g": i["type"], "x": "", "k": "Landscape"})
        parts.append(f'<section id="{stem}"><h2>{esc(label)}</h2>' + (f'<ul class="ls">{rows}</ul>' if items else '<p class="muted">No entries yet.</p>') + "</section>")
    body = f"""<h1>Landscape</h1><p class="lede">Volatile facts (tools, benchmarks, models, standards) kept apart from the durable nodes. Entries older than {stale_days} days are flagged. {stale_total} stale right now.</p>{"".join(parts)}"""
    (out / "landscape.html").write_text(page("Landscape", body, nodes), encoding="utf-8")

    # capstone + about
    h, _ = render((ROOT / "capstone" / "README.md").read_text(encoding="utf-8"))
    ids = sorted(nodes, key=len, reverse=True)

    def link_cell(m):
        cell = m.group(1)
        if "<a " in cell:
            return m.group(0)
        for i in ids:
            cell = re.sub(rf"(?<![\w/-]){re.escape(i)}(?![\w\"/-])", f'<a href="nodes/{i}.html">{i}</a>', cell)
        return f"<td>{cell}</td>"
    h = re.sub(r"<td>(.*?)</td>", link_cell, h, flags=re.S)
    (out / "capstone.html").write_text(page("Capstone", f'<article class="prose">{linker.rewrite(h, "")}</article>', nodes), encoding="utf-8")
    ab, _ = render((ROOT / "README.md").read_text(encoding="utf-8"))
    (out / "about.html").write_text(page("About", f'<article class="prose">{linker.rewrite(ab, "")}</article>', nodes), encoding="utf-8")
    for t, u, x in (("Learning path", "path.html", "stages order"), ("Prerequisite graph", "graph.html", "dependencies"),
                    ("Capstone", "capstone.html", "RAG agent project"), ("Landscape", "landscape.html", "tools benchmarks models")):
        index_items.append({"t": t, "u": u, "b": "Page", "g": "", "x": x, "k": "Page"})

    # home
    counts = {s: sum(1 for n in nodes.values() if n["status"] == s) for s in STATUSES}
    start = sorted([n for n in nodes.values() if n["layer"] == 0], key=lambda n: (n["branch"], n["title"]))[:6]
    cards = "".join(
        f'<a class="bcard" href="branches/{b}.html"><div class="bcard-top"><span class="bnum b{branch_num(b)}">{branch_num(b)}</span><span class="muted">{len(ns)} nodes</span></div>'
        f'<h3>{esc(branch_label(b))}</h3><p>{esc(BRANCH_INFO.get(b, ("", ""))[1])}</p>{segbar(ns)}</a>' for b, ns in br.items())
    stale_txt = f", {stale_total} stale" if stale_total else ""
    body = f"""<section class="hero">
<p class="eyebrow">Curriculum · taxonomy · decision guide</p>
<h1>AI Evaluation Map</h1>
<p class="lede">How to evaluate and test AI systems, from statistics basics to production monitoring. Core scope is LLM applications: prompts, RAG and agents. Evaluation and testing are treated as one lifecycle: design, measure, gate, monitor, feed back.</p>
<div class="cta"><a class="btn primary" href="path.html">Follow the learning path</a><a class="btn" href="graph.html">Explore the graph</a><button class="btn" data-open-search>Search <kbd>/</kbd></button></div>
</section>
<section class="stats">
<div><b>{len(nodes)}</b><span>nodes</span></div><div><b>{len(br)}</b><span>branches</span></div>
<div><b>{counts["learning"] + counts["practiced"]}</b><span>in progress</span></div><div><b>{counts["mastered"]}</b><span>mastered</span></div>
<div><b>{sum(len(v) for v in landscape.values())}</b><span>landscape entries{stale_txt}</span></div>
</section>
<h2>Branches</h2><div class="bgrid">{cards}</div>
<h2>Start here</h2><p class="muted">Nodes with no prerequisites.</p><div class="grid">{"".join(node_card(n, "") for n in start)}</div>
<h2>Beyond the map</h2>
<div class="bgrid two"><a class="bcard" href="capstone.html"><h3>Capstone project</h3><p>Build and evaluate a RAG app, then extend it to a tool-using agent, with every step linked to nodes.</p></a>
<a class="bcard" href="landscape.html"><h3>Landscape</h3><p>Dated tools, benchmarks and models that change faster than the concepts.</p></a></div>"""
    (out / "index.html").write_text(page("AI Evaluation Map", body, nodes, wide=True), encoding="utf-8")

    (out / "assets" / "search-index.js").write_text("window.SEARCH=" + json.dumps(index_items, ensure_ascii=False) + ";", encoding="utf-8")
    print(f"Built {sum(1 for _ in out.rglob('*.html'))} pages into {out} ({len(nodes)} nodes, {stale_total} stale landscape entries)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="site")
    ap.add_argument("--stale-days", type=int, default=90)
    a = ap.parse_args()
    out = pathlib.Path(a.out)
    if not out.is_absolute():
        out = ROOT / out
    build(out, a.stale_days)


if __name__ == "__main__":
    main()
