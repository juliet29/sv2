import matplotlib.pyplot as plt
from cyclopts import App
from loguru import logger
from utils4plans.logs import logset

from sv2.cli.studies.polyfix_help import pfx
from sv2.paths import ProjectPaths
from sv2.pfix.config import CaseConfig
from sv2.pfix.main import transform_svg

app = App()
app.command(pfx)


def keep():
    logger.debug("")
    plt.plot()


### ----- DATA --------


@app.command()
def fg():
    config = CaseConfig(
        svg_path=ProjectPaths.inputs.svgs._2_ortho,
        pixel_length=200,
        meter_length=1,
        output_folder=ProjectPaths.outputs.workflow.ortho,
    )
    transform_svg(config)
    # paths = parse_svg(ProjectPaths.svgs._2_ortho)
    # domains = make_ortho_domains(paths)
    #


#     # return domains
#
#
# @app.command()
# def write_rect():
#     layout_model = svg_to_layout_model(ProjectPaths.svgs._1_rect)
#     layout_model.write_to_path(SingleWorkflowPaths("rect").init)
#
#
# @app.command()
# def write_ortho():
#     layout_model = svg_to_layout_model(ProjectPaths.svgs._2_ortho)
#     layout_model.write_to_path(SingleWorkflowPaths("ortho").init)
#
#
# @app.command()
# def tp():
#     paths = SingleWorkflowPaths("ortho")
#
#     rotate(paths.init, paths.rotate)
#     ortho(paths.rotate, paths.ortho)
#     simplify(paths.ortho, paths.simplify)
#     plan("X", paths.rotate, paths.xplan)
#     move("X", paths.xplan, paths.xmove)
#
#     plan("Y", paths.xmove, paths.yplan)
#     move("Y", paths.yplan, paths.ymove)
#


def main():
    logset(to_stderr=True)
    app()


if __name__ == "__main__":
    main()
