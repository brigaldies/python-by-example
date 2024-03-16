"""
This is the main of the project.
"""
import argparse
import importlib
import sys
from examples.registry import registry
from app_logging import setup_logging


def register_examples() -> None:
    """
    Load the examples' modules in order to register them.
    :return: None.
    """
    # Import the modules so that they can register themselves via the @register_example decorator.
    # This forced module import is a disadvantage of the decorator-based self-registration mechanism.
    importlib.import_module("examples.typehints.type_hints_examples")
    importlib.import_module("examples.async_io.async_io_examples")
    importlib.import_module("examples.generators.generators_examples")
    importlib.import_module("examples.decorators.decorators_examples")
    importlib.import_module("examples.database.database_examples")
    importlib.import_module("examples.interfaces.interface_examples")


def main(cli_args):
    """
    Project's main entry point.
    :param cli_args: Parsed command-line arguments.
    :return: None.
    """
    logger = setup_logging(cli_args.debug)

    logger.info("Hello Python examples")

    if registry.list_registered_examples() == 0:
        sys.exit(1)

    logger.info("Requested example: %s", cli_args.example)

    if not registry.is_registered(cli_args.example):
        logger.error("Unregistered example %s", cli_args.example)
        sys.exit(1)
    else:
        logger.info("Running example %s", cli_args.example)

    registry.run_example(cli_args)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Explore Python with examples')
    parser.add_argument('-e', '--example', type=str,
                        help="run --example show to see the available examples", required=True)
    parser.add_argument("-d", "--debug", type=bool, default=False)

    # Specific example args
    # Async io
    parser.add_argument("-p", "--nprod", help="In the async io examples: Number of producers", type=int, default=5)
    parser.add_argument("-c", "--ncon", help="In the async io examples: Number of consumers", type=int, default=10)

    args = parser.parse_args()

    register_examples()

    if args.example == "show":
        print("Examples:")
        for example in registry.get_registered_examples():
            print(example)
        sys.exit(0)

    main(args)
