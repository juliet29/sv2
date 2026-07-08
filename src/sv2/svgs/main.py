from pathlib import Path
from xml.dom import minidom

from utils4plans.geom.io import LayoutModel

from sv2.svgs.errors import NoPathsWithIdsException
from sv2.svgs.helpers import SVGNames as SN
from sv2.svgs.helpers import apply_flip_transform
from sv2.svgs.ortho import SVGOrtho
from sv2.svgs.rectangle import SVGRectangle


def parse_svg(svg_path: Path):
    doc = minidom.parse(str(svg_path))
    paths = [
        apply_flip_transform(p)
        for p in doc.getElementsByTagName(SN.any_element)
        if p.getAttribute(SN.id)
    ]
    if not paths:
        raise NoPathsWithIdsException(svg_path)
    return paths


def make_rect_domains(paths: list[minidom.Element]):
    filtered_paths = [p for p in paths if p.tagName == SN.rect_element]
    domains = [SVGRectangle.read(p).to_domain_model() for p in filtered_paths]
    return domains


def make_ortho_domains(paths: list[minidom.Element]):
    filtered_paths = [p for p in paths if p.tagName == SN.ortho_element]
    domains = [SVGOrtho.read(p).to_domain_model() for p in filtered_paths]
    return domains


def svg_to_layout_model(svg_path: Path):
    paths = parse_svg(svg_path)
    rect_domains = make_rect_domains(paths)
    ortho_domains = make_ortho_domains(paths)

    layout = LayoutModel.from_domains(rect_domains + ortho_domains)
    return layout
