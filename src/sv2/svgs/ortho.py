from dataclasses import dataclass
from utils4plans.geom.io import DomainModel
from utils4plans.geom import Coord
from polyfix.geometry.paired_coords import PairedCoord, coords_from_paired_coords_list
from svg.path import parse_path, Line
from xml.dom.minidom import Element

from sv2.svgs.helpers import get_attr


def line_to_coords(line: Line):
    def point_to_coord(val: complex):
        x = val.real
        y = val.imag
        return Coord(x, y)

    return PairedCoord(point_to_coord(line.start), point_to_coord(line.end))


@dataclass
class SVGOrtho:
    id: str
    coords: list[Coord]

    @classmethod
    def read(cls, path: Element):
        id_ = get_attr("id", path)

        d = path.getAttribute("d")
        parsed_path = parse_path(d)
        paired_coords = [line_to_coords(i) for i in parsed_path if isinstance(i, Line)]
        coords = coords_from_paired_coords_list(paired_coords)
        return SVGOrtho(id_, coords)

    def to_domain_model(self):
        return DomainModel(name=self.id, coords=self.coords)
