"""
This is the main of the project.
"""
import argparse
import logging
import sys
from examples.registry import registry
from examples.app_logging import app_logging


def main(cli_args):
    """
    Project's main entry point.
    :param cli_args: Parsed command-line arguments.
    :return: None.
    """
    app_logging.setup_logging()
    # registered_examples: dict[str, Callable[[bool], None]] = registry.register_examples()

    logging.info("Hello Python examples")

    registered_examples = registry.Registry()

    logging.info("Example: %s", {cli_args.example})

    if not registered_examples.is_registered(cli_args.example):
        logging.error("Unregistered example %s", cli_args.example)
        sys.exit(1)
    else:
        logging.info("Running example %s", cli_args.example)

    # type_hints_example.run_examples()
    registered_examples.run_example(cli_args.example, True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Explore Python with examples')
    parser.add_argument('-e', '--example', type=str, help="Example name", required=True)
    args = parser.parse_args()
    main(args)
