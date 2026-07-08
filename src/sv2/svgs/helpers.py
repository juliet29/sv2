from xml.dom.minidom import Element


class SVGNames:
    ortho_element = "path"
    rect_element = "rect"
    id = "id"
    any_element = "*"


def apply_flip_transform(path: Element):
    """SVG convention is to have (0,0) in top-left, and y moving down. Rotate all to match typical math coordinates"""
    path.setAttribute("transform", "scale(1, -1)")
    return path


def get_attr(attr_name: str, path: Element):
    value = path.getAttribute(attr_name)
    return value


def get_attr_as_float(attr_name: str, path: Element):
    value = get_attr(attr_name, path)
    return float(value) if value else 0.0


def create_from_path_numeric(attr_keys: list[str], path: Element):
    return {k: get_attr_as_float(k, path) for k in attr_keys}


def create_from_path_alpha(attr_keys: list[str], path: Element):
    return {k: get_attr(k, path) for k in attr_keys}
