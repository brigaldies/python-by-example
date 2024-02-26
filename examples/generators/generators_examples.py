"""
Generators examples.
"""
import argparse
import logging

from examples.generators.generator_example_1 import example_1


def run_examples(args: argparse.Namespace) -> None:
    """
    Run the generators examples.
    :param args: Command-line arguments.
    """
    logging.info("Running generators examples")
    example_1(args)
