from pathlib import Path

from polyfix.main.execute import execute_polyfix
from polyfix.main.workflow_paths import SingleWorkflowPaths

from sv2.pfix.config import CaseConfig
from sv2.svgs.main import svg_to_layout_model


def calculate_scaling_factor(pixel_length: float, meter_length: float):
    return meter_length / pixel_length


def write_initial_model(svg_path: Path, output_path: Path, scaling_factor: float):
    layout_model = svg_to_layout_model(svg_path, scaling_factor)
    layout_model.write_to_path(SingleWorkflowPaths(output_path).init)


def transform_svg(config: CaseConfig):
    # svg_path should exist, create output path if it doesent exist..
    assert config.svg_path.exists(), f"Could not find {config.svg_path}"
    config.output_folder.mkdir(parents=True, exist_ok=True)

    scaling_factor = calculate_scaling_factor(config.pixel_length, config.meter_length)
    write_initial_model(config.svg_path, config.output_folder, scaling_factor)
    execute_polyfix(config.output_folder, save_adj=True)
