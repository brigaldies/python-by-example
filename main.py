"""
This is the main of the project.
"""
import argparse
import sys
from examples.registry import registry
from app_logging import setup_logging

# Run the examples' __init__.py in order to register them.
import examples.typehints  # pylint: disable=unused-import
import examples.async_io  # pylint: disable=unused-import
import examples.generators  # pylint: disable=unused-import
import examples.decorators  # pylint: disable=unused-import
import examples.database  # pylint: disable=unused-import
import examples.interfaces  # pylint: disable=unused-import
import examples.cache  # pylint: disable=unused-import


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

    if args.example == "show":
        print("Examples:")
        for example in registry.get_registered_examples():
            print(example)
        sys.exit(0)

    main(args)
