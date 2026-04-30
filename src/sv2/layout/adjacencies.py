from pathlib import Path
from polyfix.pydantic_models import AxGraphModel
from utils4plans.io import read_json

from sv2.paths import SingleWorkflowPaths


def get_edges(path: Path):
    axgraph = AxGraphModel.model_validate(read_json(path)).to_axgraph()
    edges = axgraph.G.edge_data()
    return edges


def read_adjacencies(output_path: Path):
    paths = SingleWorkflowPaths(output_path)
    xe = get_edges(paths.xplan)
    ye = get_edges(paths.yplan)
    # TODO: write to yaml..
    # read from yaml into e+ ready format
