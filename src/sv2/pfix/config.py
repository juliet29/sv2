from pathlib import Path
from omegaconf import OmegaConf
from dataclasses import dataclass


@dataclass()
class CaseConfig:
    svg_path: Path
    pixel_length: float
    meter_length: float
    output_folder: Path


def read_config(config_path: Path):
    schema = OmegaConf.structured(CaseConfig)

    assert config_path.exists()
    input_config = OmegaConf.load(config_path)
    config = OmegaConf.merge(schema, input_config)

    out_config: CaseConfig = OmegaConf.to_object(
        config
    )  # pyright: ignore[reportAssignmentType]  # pyright: ignore[reportAttributeAccessIssue]

    return out_config
