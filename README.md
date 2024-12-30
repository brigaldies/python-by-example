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
- TLS-secured gRPC-based microservices.

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
- gRPC-based microservices

The above apps use the ```app_logging``` module, hence add the Dash's application location to PYTHONPATH before running
them, for example:

```shell
-> % export PYTHONPATH="${PYTHONPATH}:/Users/bertrandrigaldies/Projects/python-by-example"
```

### gRPC-based microservice

The gRPC examples were the results of doing a code-along of [this tutorial](https://realpython.com/python-microservices-grpc/)

#### gRPC protobuf bindings generation

To generate the protobuf bindings, and run the client and recommendations server by hand (outside of Docker):

For the server:
```shell
cd apps/grpc/recommendations
python -m grpc_tools.protoc -I ../protobufs --python_out=. \
         --grpc_python_out=. ../protobufs/recommendations.proto
```

For the Web server:
```shell
cd apps/grpc/marketplace
python -m grpc_tools.protoc -I ../protobufs --python_out=. \
         --grpc_python_out=. ../protobufs/recommendations.proto
```

When running in Docker, the protobuf bindings are generated as part of the Docker image builds for both the client and recommendations server.
See the next section for the instructions on how to run the demo in Docker with ```docker-compose```.

#### Docker-based Execution

Build the Docker images for the client and recommendations server as shown below (see also the second comment line at the top of the Docker files):

1. Build the client's CA and TLS public key
```shell
openssl req -x509 -nodes -newkey rsa:4096 -keyout ca.key -out ca.pem -subj /O=me
```

2. Build the client's Docker image
```shell
DOCKER_BUILDKIT=1 docker build . -f marketplace/Dockerfile -t marketplace --secret id=ca.key,src=ca.key
```

3. Build the recommendations server's Docker image
```shell
DOCKER_BUILDKIT=1 docker build . -f recommendations/Dockerfile -t recommendations --secret id=ca.key,src=ca.key
```

Run the dockerized demo with `docker-compose` as shown below:

```shell
docker-compose up
```

Shut down the application as shown below from the terminal where the demo was started (see above):
1. Ctrl-C
2. `docker-compose down`

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

## Static Types Checking with mypy

### Install

```shell
poetry add mypy
```

### Usage

```shell
mypy **/*.py
```

### Install Supporting Type "Stubs"

In order to address mypy errors such as:

```shell
error: Library stubs not installed for "pandas"  [import-untyped]
```

Install the supporting type stubs:

```shell
poetry add pandas-stubs
poetry add types-aiofiles
poetry add types-requests
```

## REST API

### Install

```shell
poetry add flask
```

### Run

```shell
poetry run flask --app ./apps/api/resp_api --debug run
```

### End-points

- [View incomes](http://127.0.0.1:5000/incomes)
- Add income: Run the Python ```post_income.py``` program as shown below:

```shell
poetry run python ./apps/api/post_income.py 
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

## Redis Cache

### Install

```shell
poetry add redis
```

### Run the Redis service

```shell
cd ./examples/cache
docker compose up
```

### Redi Cli

Pre-requisite: Install the Redis client
```shell
brew install redis
```

```shell
redis-cli -h localhost -p 6379
```

## Progress Bars

### With tqdm

#### Install

```shell
poetry install tqdm
```

### With progressbar2

```shell
poetry install progressbar2
```
## Machine Learning

### Install

```shell
poetry add numpy
```

## TODO

### Object-Oriented Programming (OOP)

### Generics

### Multi-threading programming

### Jobs Scheduler

### Secure API
