import numpy as np

from utils4plans.geom import Coord
from utils4plans.geom.io import DomainModel


def tidy_factor(factor: float, sig: int = 2) -> float:
    # precision counts significant figures (fractional=False)
    return float(np.format_float_positional(factor, precision=sig, fractional=False, trim="-"))


def scale_domain(domain: DomainModel, factor: float) -> DomainModel:
    coords = [Coord(c.x * factor, c.y * factor) for c in domain.coords]
    return DomainModel(name=domain.name, coords=coords)


def lift_domains(domains: list[DomainModel]) -> list[DomainModel]:
    # SVG flip leaves y negative; shift whole layout so its lowest y sits at 0
    min_y = min(c.y for d in domains for c in d.coords)
    return [
        DomainModel(name=d.name, coords=[Coord(c.x, c.y - min_y) for c in d.coords])
        for d in domains
    ]


def process_layout(domains: list[DomainModel], scaling_factor: float) -> list[DomainModel]:
    factor = tidy_factor(scaling_factor)
    scaled = [scale_domain(d, factor) for d in domains]
    return lift_domains(scaled)
