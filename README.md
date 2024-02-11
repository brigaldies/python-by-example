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


## TODO

### Classes
### Generics
### Basic Web server