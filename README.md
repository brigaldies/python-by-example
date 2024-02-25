# Examples

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
poetry init
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
pdm run main.py --example type-hints
```

## Jupyter notebook

Run it with:
```shell
pdm run jupyter notebook
```

## Logging setup to stdout and log file

See ```setup_logging()``` in ```main.py```.

## Command-line arguments parsing

See ```parser.parse_args()``` in ```main.py```.

## Registry of "callable" functions

See ```register_examples()``` in ```./examples/registry/registry.py``` for the use if the ```Callable``` generic.

## Type Hints

See ```run_examples()``` in ```./examples/typehints/type_hints_example.py```.

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

First, add the Dash's application location to PYTHONPATH, so that the Dash application has access to modules under ./examples, for example:
```shell
-> % export PYTHONPATH="${PYTHONPATH}:/Users/bertrandrigaldies/Projects/python-by-example"
```

Then, run the Dash application:
```shell
poetry run python ./examples/web_app/app_with_bootstrap_styling.py
```

## TODO

### Generics
### Async programming
### Multi-threading programming with greenlets
