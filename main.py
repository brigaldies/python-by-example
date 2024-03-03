"""
This is the main of the project.
"""
import argparse
import importlib
import logging
import sys
from examples.registry import registry
from app_logging import setup_logging

# Import the modules so that they can register themselves via the @register_example decorator.
# This forced module import is a disadvantage of the decorator-based self-registration mechanism.
importlib.import_module("examples.typehints.type_hints_examples")
importlib.import_module("examples.async_io.async_io_examples")
importlib.import_module("examples.generators.generators_examples")
importlib.import_module("examples.decorators.decorators_examples")


def main(cli_args):
    """
    Project's main entry point.
    :param cli_args: Parsed command-line arguments.
    :return: None.
    """
    setup_logging(cli_args.debug)

    logging.info("Hello Python examples")

    if registry.list_registered_examples() == 0:
        sys.exit(1)

    logging.info("Requested example: %s", cli_args.example)

    if not registry.is_registered(cli_args.example):
        logging.error("Unregistered example %s", cli_args.example)
        sys.exit(1)
    else:
        logging.info("Running example %s", cli_args.example)

    registry.run_example(cli_args)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Explore Python with examples')
    parser.add_argument('-e', '--example', type=str, help="Example name", required=True)
    parser.add_argument("-d", "--debug", type=bool, default=False)

    # Specific example args
    # Async io
    parser.add_argument("-p", "--nprod", type=int, default=5)
    parser.add_argument("-c", "--ncon", type=int, default=10)

    args = parser.parse_args()
    main(args)
