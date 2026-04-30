from pathlib import Path
import pytest
from polyfix.pydantic_models import read_layout_from_path
from sv2.paths import ProjectPaths, SingleWorkflowPaths

from sv2.pfix.config import CaseConfig
from sv2.pfix.main import transform_svg


@pytest.mark.skip(
    reason="TODO: use policy approach ~ arjancodes to conditionally save images.. for some reason, doesn't work with fake paths"
)
def test_ortho_workflow(tmp_path):
    # with tempfile.TemporaryDirectory() as td:
    tmp_dir = Path(tmp_path)

    config = CaseConfig(
        svg_path=ProjectPaths.svgs._2_ortho,
        pixel_length=200,
        meter_length=1,
        output_folder=tmp_dir,
    )
    transform_svg(config)
    paths = SingleWorkflowPaths(tmp_dir)

    layout = read_layout_from_path(paths.ymove)
    assert len(layout.domains) > 2

    # check that valid layout is in ymove
