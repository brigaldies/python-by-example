import argparse
import logging
import sys
from typing import Callable
from examples.registry import registry


def setup_logging() -> None:
    logging_format = logging.Formatter("%(asctime)s | %(levelname)s | %(name).8s | %(message)s")
    logger = logging.getLogger()
    logger.setLevel(level=logging.INFO)

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(logging_format)
    logger.addHandler(stdout_handler)

    file_handler = logging.FileHandler("main.log", mode='w')
    file_handler.setFormatter(logging_format)
    logger.addHandler(file_handler)

    logging.info(f"Logger {logger} set")


def main(cli_args):
    setup_logging()
    registered_examples: dict[str, Callable[[bool], None]] = registry.register_examples()

    logging.info("Hello Python examples")

    logging.info(f"Example: {cli_args.example}")

    if cli_args.example not in registered_examples:
        logging.error(f"Unregistered example {cli_args.example}")
        exit(1)
    else:
        logging.info(f"Running example '{cli_args.example}'")

    # type_hints_example.run_examples()
    registered_examples[cli_args.example](True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Explore Python with examples')
    parser.add_argument('-e', '--example', type=str, help="Example name", required=True)
    args = parser.parse_args()
    main(args)
