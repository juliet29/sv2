from pathlib import Path

from cyclopts import App

from sv2.pfix.main import write_initial_model

pfx = App("pfx")


TEMP_PATH = "/scratch/users/jnwagwu/polyfix/"


class Paths:
    """Just for creating test cases easily for polyfix.."""

    base = Path(TEMP_PATH) / "4_temp/svgs"
    ablation_c = base / "ablation_c"


@pfx.command()
def make_svg():
    write_initial_model(Paths.ablation_c / "out.svg", Paths.ablation_c)
