#!/usr/bin/env python3
"""Git clean filter, step 2: reset notebook metadata to the course's editor-neutral block.

Runs after nbstripout (which removes outputs and execution counts), so that the kernel name
and Python version written by VS Code or Jupyter on the instructor's machine never reach the
public repository. Reads a notebook on stdin and writes it on stdout.

Setup (once per clone; .gitattributes already maps *.ipynb to the nbstripout filter):

    .venv/bin/pip install nbstripout
    .venv/bin/nbstripout --install --attributes .gitattributes
    git config filter.nbstripout.clean \
        "$PWD/.venv/bin/python -m nbstripout | $PWD/.venv/bin/python $PWD/tools/reset_notebook_metadata.py"
"""

import sys
from pathlib import Path

import nbformat

sys.path.insert(0, str(Path(__file__).resolve().parent))
from prepare_notebook import KERNEL_METADATA  # noqa: E402


def main() -> None:
    nb = nbformat.reads(sys.stdin.read(), as_version=nbformat.NO_CONVERT)
    nb.metadata = nbformat.from_dict(KERNEL_METADATA)
    nbformat.write(nb, sys.stdout)


if __name__ == "__main__":
    main()
