# Examples

## Content

This repo contains various examples for:

- PDM and Poetry-based dependencies management.
- pipx-based installation of poetry and pylint.
- pylint-based linting.
- pytest-based unit tests.
- Command-line arguments parsing.
- Logging.
- Executing ```Callable``` objects.
- Type hints.
- Async IO
- Jupyter notebook.
- Dash-based Web application.
- Flask-based API.
- SQLAlchemy-based SQL Database access.
- Interfaces

I built this repo to become a better Python programmer by learning from well-written, lint-checked, unit-tested, "
Pythonic" examples, and provide (for myself) an inventory of working
examples that I can go back to when I forget how to do something in Python. :-)

## Code Sources

The code uses and adapts various examples and tutorials that I found on the Internet from a variety of sites,
hence I do not claim any authorship to any of the source code in this repo.

I strive to indicate the examples' sources in the modules' docstring.

## Copyright

There is none.

## IDE

The code in the repo was written, debugged, and executed using JetBrains' [PyCharm](https://www.jetbrains.com/pycharm/)
2023.2.5 (Professional Edition).

## Python requirements

Python 3.10 or above.

Install it on a Mac with:

```shell
brew install python@3.10
```

## Package & Project Manager

PDM and Poetry can share the same ```pyproject.toml``` file.

### PDM

[Documentation](https://pdm-project.org/latest/)

#### Install

```shell
brew install pdm
```

Notes:

- brew also installed python@3.12 as a [PDM](https://formulae.brew.sh/formula/pdm#default) dependency

#### Usage

```shell
pdm init
pdm add jupyter
pdm install
```

### Poetry

[Documentation](https://python-poetry.org/docs/#installing-with-pipx)

#### Install

```shell
brew install pipx
pipx install poetry
pipx ensurepath
# open new terminal
poetry -h
```

#### Usage

```shell
poetry install
```

```shell
poetry run python main.py --example types-hint
```

```shell
poetry run jupyter notebook
```

## Main.py

Run it with:

```shell
pdm run main.py --example type-hints --debug true
```

## Jupyter notebook

Run it with:

```shell
pdm run jupyter notebook
```

## Apps

- api
- web_app
- web_crawler

The above apps use the ```app_logging``` module, hence add the Dash's application location to PYTHONPATH before running
them, for example:

```shell
-> % export PYTHONPATH="${PYTHONPATH}:/Users/bertrandrigaldies/Projects/python-by-example"
```

## Logging setup to stdout and log file

See ```setup_logging()``` in ```app_logging.py```.

## Command-line arguments parsing

See ```parser.parse_args()``` in ```main.py```.

## Registry of "callable" functions

See ```register_examples()``` in ```./examples/registry/registry.py``` for the use if the ```Callable``` generic.

## Type Hints

See ```run_examples()``` in ```./examples/typehints/type_hints_example.py```.

## Async IO

### Installation

```shell
poetry add aiofiles
poetry add aiohttp
```

### Run

```shell
poetry run python main.py --example async-io --debug true -p 3 -c 2 
poetry run python main.py --example generators --debug true
```

## Unit Tests

### PyTest

#### Install

```shell
poetry install pytest
```

#### Usage

```shell
poetry run python -m pytest
```

## Linter

### Install

```shell
pipx install pylint
```

### Usage

```shell
pylint **/*.py 
```

## REST API

### Install

```shell
poetry add flask
```

### Run

```shell
flask --app ./examples/api/resp_api --debug run
```

### End-points

- [View incomes](http://127.0.0.1:5000/incomes)
- Add income: Run the Python ```post_income.py``` program as shown below:

```shell
poetry run python ./examples/api/post_income.py 
```

## Web Application

The example uses the [Dash](https://dash.plotly.com/) framework, and [tutorial](https://dash.plotly.com/tutorial).

### Install

```shell
poetry install dash
```

### Run

```shell
poetry run python ./apps/web_app/app_with_bootstrap_styling.py
```

## SQL Database with SQLAlchemy

### Install

```shell
poetry install sqlalchemy
```

## TODO

### Object-Oriented Programming (OOP)

### Generics

### Multi-threading programming

### Jobs Scheduler

### Secure API
