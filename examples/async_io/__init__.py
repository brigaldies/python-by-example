"""
Async IO programming examples.

Examples are from https://realpython.com/async-io-python/
"""
import argparse
import logging
from examples.registry.registry import register_example
from examples.async_io.async_io_example1 import example_1
from examples.async_io.async_io_example2 import example_2
from examples.async_io.async_io_example3 import example_3
from examples.async_io.async_io_example4 import example_4

LOG = logging.getLogger("examples")


@register_example
def async_io(args: argparse.Namespace) -> None:
    """
    Run the async IO examples.
    :param args: Command-line arguments.
    """
    LOG.info("Running async IO examples")
    example_1(args)
    example_2(args)
    example_3(args)
    example_4(args)
