import matplotlib.pyplot as plt
from sv2.paths import ProjectPaths
from cyclopts import App
from loguru import logger
from utils4plans.logconfig import logset

from sv2.svgs.main import make_ortho_domains, parse_svg

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


def main():
    logset(to_stderr=True)
    app()


if __name__ == "__main__":
    main()
