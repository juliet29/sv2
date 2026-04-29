from dataclasses import dataclass
from pathlib import Path
import pyprojroot


BASE_PATH = pyprojroot.find_root(pyprojroot.has_dir(".git"))


class StaticPaths:
    base = Path(BASE_PATH) / "static"
    inputs = base / "1_inputs"
    temp = base / "4_temp"
    figures = base / "5_figures"


class SVGPaths:
    base = StaticPaths.inputs / "svgs"
    _1_rect = base / "1_rectangles.svg"
    _2_ortho = base / "2_ortho.svg"


class PolyfixWorkflowPaths:
    base = StaticPaths.temp / "workflow_test"
    ortho = base / "ortho"
    rect = base / "rect"


@dataclass
class SingleWorkflowPaths:
    name: str

    @property
    def base(self):
        return StaticPaths.temp / "workflow_test" / self.name

    @property
    def init(self):
        return self.base / "init/out.json"

    @property
    def rotate(self):
        return self.base / "rotate/out.json"

    @property
    def ortho(self):
        return self.base / "ortho/out.json"

    @property
    def simplify(self):
        return self.base / "simplify/out.json"

    @property
    def xplan(self):
        return self.base / "xplan/out.json"

    @property
    def xmove(self):
        return self.base / "xmove/out.json"

    @property
    def yplan(self):
        return self.base / "yplan/out.json"

    @property
    def ymove(self):
        return self.base / "ymove/out.json"


class ProjectPaths:
    svgs = SVGPaths
    wflow = PolyfixWorkflowPaths
