# svg2plan

*Transform SVGs into geometrically valid floor plans.*

`svg2plan` is a command-line tool that converts marked-up floor plans into
geometrically valid representations that are rectangular, hole-free, and
overlap-free. Rooms are rescaled from pixels to real-world dimensions, and holes
and overlaps between rooms are resolved automatically via the
[`polyfix`](https://github.com/juliet29/polyfix) module.

This module is designed to be paired with
[`plan2eplus`](https://github.com/juliet29/plan2eplus), which generates Airflow
Network-enabled EnergyPlus models.

---

## Getting Started

### Installation

Clone this repository. The project uses [UV](https://github.com/astral-sh/uv) as
its package manager. Run the tests in `/tests` to verify your environment is
configured correctly.

### Prepare Your Floor Plan

Mark up your floor plan using rectangular shapes and room name labels, then
export an `.svg` file. Tools such as Figma are well-suited for this step.

SVG objects can be either rectangles or paths, but paths should be orthogonal.
Each object should include `height`, `width`, `x`, `y`, and `id` attributes. Note
a pixel-length measurement corresponding to a known room dimension — this will be
used to rescale the plan to real-world dimensions.

### Transform

The transform pipeline (`sv2.pfix.main.transform_svg`) takes a `CaseConfig` and:

- Parses the `.svg` file to extract room dimensions and spatial adjacencies
- Rescales the plan from pixels to real-world dimensions using
  `meter_length / pixel_length`
- Resolves geometric issues (holes and overlaps) via
  [`polyfix`](https://github.com/juliet29/polyfix)
- Writes the corrected layout to the output folder

Configure a case with `CaseConfig`:

```python
from sv2.pfix.config import CaseConfig
from sv2.pfix.main import transform_svg

config = CaseConfig(
    svg_path=svg_path,
    pixel_length=200,   # pixels for a known dimension
    meter_length=1,     # real-world length of that dimension, in meters
    output_folder=output_folder,
)
transform_svg(config)
```

Or run it through the CLI:

```bash
uv run sv2s --help
```

## Outputs

Results are written to the configured `output_folder` and include the corrected
floor plan layout and intermediate `polyfix` processing data.
