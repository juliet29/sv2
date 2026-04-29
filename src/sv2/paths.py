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


class ProjectPaths:
    svgs = SVGPaths
