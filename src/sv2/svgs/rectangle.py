from dataclasses import dataclass
from utils4plans.geom import Range, Domain

from xml.dom.minidom import Element
from sv2.svgs.helpers import create_from_path_alpha, create_from_path_numeric

from utils4plans.geom_io import DomainModel


@dataclass
class SVGRectangle:
    width: float
    height: float
    x: float
    y: float
    id: str  # NOTE: technically, a name but ID is matches the specification

    @classmethod
    def read(cls, path: Element):
        annots = cls.__annotations__
        numeric_keys = [k for k, v in annots.items() if v is float]
        alpha_keys = [k for k, v in annots.items() if v is str]

        numeric_vals = create_from_path_numeric(numeric_keys, path)
        alpha_vals = create_from_path_alpha(alpha_keys, path)

        entry = numeric_vals | alpha_vals
        return cls(**entry)  # pyright: ignore[reportArgumentType]

    def to_domain_model(self):
        horz_range = Range(self.x, self.x + self.width)
        vert_range = Range(self.y - self.height, self.y)
        domain = Domain(horz_range, vert_range)
        return DomainModel(name=self.id, coords=domain.to_coords())
