from xml.dom import minidom
from loguru import logger
from utils4plans.geom_io import LayoutModel
from pathlib import Path

from sv2.svgs.errors import NoPathsWithIdsException
from sv2.svgs.ortho import SVGOrtho
from sv2.svgs.rectangle import SVGRectangle

from sv2.svgs.helpers import SVGNames as SN

# def get_rectangles(self):
#     doc = minidom.parse(str(self.svg_path))
#     self.rectangles = filter_none(
#         [
#             self.parse_single_rectangle(path)
#             for path in doc.getElementsByTagName("rect")
#             if path.getAttribute("id")
#         ]
#     )
#     assert len(self.rectangles) >= 1, "Check that svgs include ids!"
#     doc.unlink()
#
#
# def parse_single_rectangle(self, path):
#     id = path.getAttribute("id")
#     if "image" in id:
#         return None
#     return SVGRect(
#         self.get_attr_as_float("x", path),
#         self.get_attr_as_float("y", path),
#         self.get_attr_as_float("width", path),
#         self.get_attr_as_float("height", path),
#         id=path.getAttribute("id"),
#     )
#


def parse_svg(svg_path: Path):
    doc = minidom.parse(str(svg_path))
    paths = [
        p for p in doc.getElementsByTagName(SN.any_element) if p.getAttribute(SN.id)
    ]
    if not paths:
        raise NoPathsWithIdsException(svg_path)
    return paths


def make_rect_domains(paths: list[minidom.Element]):
    filtered_paths = [p for p in paths if p.tagName == SN.rect_element]
    domains = [SVGRectangle.read(p).to_domain_model() for p in filtered_paths]
    return domains


def make_ortho_domains(paths: list[minidom.Element]):
    logger.debug(paths)
    logger.debug([p.tagName for p in paths])
    filtered_paths = [p for p in paths if p.tagName == SN.ortho_element]
    logger.debug(filtered_paths)
    domains = [SVGOrtho.read(p).to_domain_model() for p in filtered_paths]
    return domains


def svg_to_layout_model(svg_path: Path):
    paths = parse_svg(svg_path)
    rect_domains = make_rect_domains(paths)
    ortho_domains = make_ortho_domains(paths)

    layout = LayoutModel.from_domains(rect_domains + ortho_domains)
    return layout


# def parse_rectangles(svg_path: Path):
#     doc = parse_svg(svg_path)
#     rects = [
#         path for path in doc.getElementsByTagName("rect") if path.getAttribute("id")
#     ]
#     return rects
#
#
# def parse_ortho(svg_path: Path):
#     doc = parse_svg(svg_path)
#     # TODO: change "path" to be a constant, add exception if no attributes have id..
#     paths = [
#         path for path in doc.getElementsByTagName("path") if path.getAttribute("id")
#     ]
#     return paths
#
#
# def get_rectangles(svg_path: Path):
#     doc = minidom.parse(str(svg_path))
#     rectangles = filter_none(
#         [
#             SVGRectangle.read(path)
#             for path in doc.getElementsByTagName("rect")
#             if path.getAttribute("id")
#         ]
#     )
#     assert len(rectangles) >= 1, "Check that svgs include ids!"
#     doc.unlink()
