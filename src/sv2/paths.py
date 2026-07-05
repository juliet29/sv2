from pathlib import Path

import pyprojroot

BASE_PATH = pyprojroot.find_root(pyprojroot.has_dir(".git"))
TEMP_PATH = "/scratch/users/jnwagwu/sv2"


class StaticPaths:
    inputs = Path(BASE_PATH) / "static/1_inputs"
    temp = Path(TEMP_PATH) / "data"
    figures = Path(TEMP_PATH) / "figs"


class SVGPaths:
    base = StaticPaths.inputs / "svgs"
    _1_rect = base / "1_rectangles.svg"
    _2_ortho = base / "2_ortho.svg"


class Inputs:
    svgs = SVGPaths


class WorkflowTest:
    base = StaticPaths.temp / "workflow_test"
    ortho = base / "ortho"
    rect = base / "rect"


class Outputs:
    workflow = WorkflowTest


class ProjectPaths:
    inputs = Inputs
    outputs = Outputs
