#!/usr/bin/env python3
"""Turn a notebook from the teaching material into a course notebook.

    python3 tools/prepare_notebook.py SOURCE.ipynb notebooks/NN_name.ipynb

What it does:
  * adds an "Open in Colab" badge and a setup cell that, on Colab only,
    clones this repository so that ./Data and helper modules are available;
  * removes "!pip install" cells (dependencies come from requirements.txt);
  * applies small compatibility fixes for recent library versions
    (matplotlib Axes3D, pandas 3 replace() and dropna(inplace=True));
  * clears all outputs and execution counts.

Only the Python standard library is needed.
"""
import json
import re
import sys
import uuid
from pathlib import Path

REPO = "celoy/intro-ai-ed353"
BRANCH = "main"

# Editor-neutral notebook metadata (also restored on commit by tools/reset_notebook_metadata.py)
KERNEL_METADATA = {
    "kernelspec": {"display_name": "Python 3 (ipykernel)", "language": "python", "name": "python3"},
    "language_info": {"name": "python"},
}

SETUP_CODE = f"""\
# Run this cell first. On Google Colab it downloads the course files
# (data, helper modules); on your own computer it does nothing.
import os, sys
if "google.colab" in sys.modules:
    repo = "/content/intro-ai-ed353"
    if not os.path.isdir(repo):
        os.system(f"git clone --depth 1 -q https://github.com/{REPO}.git {{repo}}")
    os.chdir(f"{{repo}}/notebooks")"""

# (pattern, replacement) applied to code cells
FIXES = [
    # Axes3D(fig) no longer attaches the axes to the figure (matplotlib >= 3.4)
    (re.compile(r"(\w+)\s*=\s*Axes3D\((\w+)\)"), r"\1 = \2.add_subplot(projection='3d')"),
    # pandas >= 3: replace() no longer converts text columns to numbers by itself
    (re.compile(r"^(\s*(\w+)\s*=\s*\2\.replace\(\{[^}]*\}\))", re.M), r"\1.infer_objects()"),
    # pandas >= 3.1: inplace=True is deprecated
    (re.compile(r"^(\s*)(\w+)\.dropna\((.*?)(,\s*)?inplace\s*=\s*True\s*\)", re.M), r"\1\2 = \2.dropna(\3)"),
]

PIP_ONLY = re.compile(r"^\s*([!%]pip install[^\n]*\n?)+\s*$")


def lines(text):
    out = text.splitlines(keepends=True)
    return out


def new_cell(kind, text, with_id):
    cell = {"cell_type": kind, "metadata": {}, "source": lines(text)}
    if kind == "code":
        cell["execution_count"] = None
        cell["outputs"] = []
    if with_id:
        cell["id"] = uuid.uuid4().hex[:8]
    return cell


def prepare(src, dest):
    nb = json.loads(Path(src).read_text(encoding="utf-8"))
    with_id = nb.get("nbformat", 4) >= 4 and nb.get("nbformat_minor", 0) >= 5
    cells = []
    for cell in nb["cells"]:
        source = "".join(cell.get("source", []))
        if cell["cell_type"] == "code":
            if PIP_ONLY.match(source):
                continue
            for pattern, repl in FIXES:
                source = pattern.sub(repl, source)
            cell["source"] = lines(source)
            cell["outputs"] = []
            cell["execution_count"] = None
        cell["metadata"] = {}
        if cell["cell_type"] != "markdown":
            cell.pop("attachments", None)
        if with_id and "id" not in cell:
            cell["id"] = uuid.uuid4().hex[:8]
        cells.append(cell)

    name = Path(dest).name
    badge = (f"[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]"
             f"(https://colab.research.google.com/github/{REPO}/blob/{BRANCH}/notebooks/{name})")
    # badge first, then the title cell, then the setup cell
    title_index = 1 if cells and cells[0]["cell_type"] == "markdown" else 0
    cells.insert(title_index, new_cell("code", SETUP_CODE, with_id))
    cells.insert(0, new_cell("markdown", badge, with_id))

    nb["cells"] = cells
    nb["metadata"] = KERNEL_METADATA
    Path(dest).parent.mkdir(parents=True, exist_ok=True)
    Path(dest).write_text(json.dumps(nb, indent=1, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    prepare(sys.argv[1], sys.argv[2])
    print(f"{sys.argv[1]} -> {sys.argv[2]}")
