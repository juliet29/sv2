from sv2.paths import ProjectPaths
from sv2.svgs.helpers import SVGNames as SN
from sv2.svgs.main import parse_svg, svg_to_layout_model
from sv2.svgs.ortho import SVGOrtho
from sv2.svgs.rectangle import SVGRectangle


class TestAnnotations:
    annots = SVGRectangle.__annotations__

    def test_str(self):
        assert self.annots["id"] is str

    def test_float(self):
        assert self.annots["width"] is float


class TestReadSVG:
    rect_paths = parse_svg(ProjectPaths.inputs.svgs._1_rect)
    ortho_paths = parse_svg(ProjectPaths.inputs.svgs._2_ortho)

    def test_create_svgrect(self):
        filtered_paths = [p for p in self.rect_paths if p.tagName == SN.rect_element]
        res = SVGRectangle.read(filtered_paths[0])
        assert res.width > 1

    def test_make_domain(self):
        rect = SVGRectangle.read(self.rect_paths[0])
        domain = rect.to_domain_model()
        assert len(domain.coords) >= 3

    def test_create_svortho(self):
        filtered_paths = [p for p in self.ortho_paths if p.tagName == SN.ortho_element]
        res = SVGOrtho.read(filtered_paths[0])
        assert len(res.coords) >= 3


def test_create_layout_model():
    layout = svg_to_layout_model(ProjectPaths.inputs.svgs._2_ortho)
    assert len(layout.root.keys()) > 2
