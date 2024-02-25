"""
Async IO programming examples.

Examples are from https://realpython.com/async-io-python/
"""
import argparse
import logging

from examples.async_io.async_io_example1 import example_1
from examples.async_io.async_io_example2 import example_2
from examples.async_io.async_io_example3 import example_3
from examples.async_io.async_io_example4 import example_4


def run_examples(args: argparse.Namespace) -> None:
    """
    Run the async IO examples.
    :param args: Command-line arguments.
    """
    logging.info("Running async IO examples")
    example_1(args)
    example_2(args)
    example_3(args)
    example_4(args)
