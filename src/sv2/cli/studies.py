import matplotlib.pyplot as plt
from sv2.paths import ProjectPaths, SingleWorkflowPaths
from cyclopts import App
from loguru import logger
from utils4plans.logconfig import logset

from sv2.svgs.main import make_ortho_domains, parse_svg, svg_to_layout_model
from polyfix.cli.make.main import move, ortho, plan, rotate, simplify

app = App()


def keep():
    logger.debug("")
    plt.plot()


### ----- DATA --------


@app.command()
def fg():
    paths = parse_svg(ProjectPaths.svgs._2_ortho)
    domains = make_ortho_domains(paths)

    return domains


@app.command()
def write_rect():
    layout_model = svg_to_layout_model(ProjectPaths.svgs._1_rect)
    layout_model.write_to_path(SingleWorkflowPaths("rect").init)


@app.command()
def write_ortho():
    layout_model = svg_to_layout_model(ProjectPaths.svgs._2_ortho)
    layout_model.write_to_path(SingleWorkflowPaths("ortho").init)


@app.command()
def tp():
    paths = SingleWorkflowPaths("ortho")

    rotate(paths.init, paths.rotate)
    ortho(paths.rotate, paths.ortho)
    simplify(paths.ortho, paths.simplify)
    plan("X", paths.rotate, paths.xplan)
    move("X", paths.xplan, paths.xmove)

    plan("Y", paths.xmove, paths.yplan)
    move("Y", paths.yplan, paths.ymove)


def main():
    logset(to_stderr=True)
    app()


if __name__ == "__main__":
    main()
