# SVGReader

The SVG Reader converts Path and Rectangle SVG objects into Domain objects. These can then be easily arranged using the `polyfix` module.

## Example

Create list of domains based on a SVG
=== "rectangles.svg"

    ```svg
      <svg width="1027" height="845" viewBox="0 0 1027 845" fill="none" xmlns="http://www.w3.org/2000/svg">
      <rect width="1027" height="845" fill="#F5F5F5"/>
      <g id="1- Rectangles">
      <rect width="1920" height="1080" transform="translate(-193 -80.5009)" fill="white"/>
      <g id="1_rectangles">
      <rect id="6" x="703.001" y="437.499" width="323" height="406" fill="#2AD5D3"/>
      <rect id="5" x="338.001" y="435.499" width="323" height="406" fill="#2AD5D3"/>
      <rect id="4" x="4.00154" y="438.499" width="323" height="406" fill="#2AD5D3"/>
      <rect id="3" x="704" y="0.499054" width="323" height="406" fill="#2AD5D3"/>
      <rect id="2" opacity="0.6" x="337.999" y="6.10352e-05" width="323" height="406" fill="#2AD5D3"/>
      <rect id="1" x="7.38284e-05" y="0.499115" width="323" height="406" fill="#BE2F2F"/>
      </g>
      </g>
      </svg>
    ```

=== "Python"

    ```python
    from pathlib import Path

    svg_path = Path("path/to/rectangles.svg")
    rects = parse_rectangles(svg_path)
    sv_rectangles = [SVGRectangle.read(i) for i in rects]
    domains = [i.to_domain() for i in sv_rectangles]


    ```

## API

::: sv2.svgs.interfaces.SVGRectangle

::: sv2.svgs.interfaces.SVGOrtho
