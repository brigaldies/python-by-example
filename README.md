# Examples

## Python requirements

Python 3.10 or above.

Install it on a Mac with:

```shell
brew install python@3.10
```

## Package & Project Manager

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

## Command-line arguments parsing

## Registry of "callable" functions

## Type Hints

## TODO

### PDM vs. Poetry Package Manager
### Unit tests
### 