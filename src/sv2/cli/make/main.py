from cyclopts import App
from utils4plans.logconfig import logset

app = App()


### ------- END COMMANDS ---------


def main():
    logset(to_stderr=True)
    app()


if __name__ == "__main__":
    main()
