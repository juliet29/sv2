from dataclasses import dataclass
from xml.dom.minidom import Element

from utils4plans.geom import Domain, Range
from utils4plans.geom.io import DomainModel

from sv2.svgs.helpers import create_from_path_alpha, create_from_path_numeric


@dataclass
class SVGRectangle:
    width: float
    height: float
    x: float
    y: float
    id: str  # NOTE: technically a name but ID is matches the specification

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
        # y_flip, height_flip = self.y * -1, self.height * -1

        self.y *= -1  # NOTE: SVG convention has (0,0) in the top left and y moving downward, change to accomadate typical mathematical coordinates
        vert_range = Range(self.y - self.height, self.y)
        domain = Domain(horz_range, vert_range)
        return DomainModel(name=self.id, coords=domain.to_coords())
