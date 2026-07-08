from pathlib import Path

from polyfix.cli.make.main import move, ortho, plan, rotate, simplify

from sv2.pfix.config import CaseConfig
from sv2.svgs.main import svg_to_layout_model
from sv2.workflow_paths import SingleWorkflowPaths


def write_initial_model(svg_path: Path, output_path: Path):
    layout_model = svg_to_layout_model(svg_path)
    layout_model.write_to_path(SingleWorkflowPaths(output_path).init)


def execute_polyfix(output_path: Path):
    paths = SingleWorkflowPaths(output_path)

    rotate(paths.init, paths.rotate)
    ortho(paths.rotate, paths.ortho)
    simplify(paths.ortho, paths.simplify)
    plan("X", paths.rotate, paths.xplan)
    breakpoint()
    move("X", paths.xplan, paths.xmove)

    plan("Y", paths.xmove, paths.yplan)
    move("Y", paths.yplan, paths.ymove)


def transform_svg(config: CaseConfig):
    # svg_path should exist, create output path if it doesent exist..
    assert config.svg_path.exists(), f"Could not find {config.svg_path}"
    config.output_folder.mkdir(parents=True, exist_ok=True)

    write_initial_model(config.svg_path, config.output_folder)
    execute_polyfix(config.output_folder)
