"""
Async Iterators programming examples.

Examples are from https://realpython.com/python-async-iterators/
"""
import argparse
import logging
from examples.registry.registry import register_example
from examples.async_iterators.async_iterators_example1 import example_1
from examples.async_iterators.async_iterators_example2 import example_2
from examples.async_iterators.async_iterators_example3 import example_3
from examples.async_iterators.async_iterators_example4 import example_4
from examples.async_iterators.async_iterators_example5 import example_5
from examples.async_iterators.async_iterators_example6 import example_6
from examples.async_iterators.async_iterators_example7 import example_7
from examples.async_iterators.async_iterators_example8 import example_8
from examples.async_iterators.async_iterators_example9 import example_9
from examples.async_iterators.async_iterators_example10 import example_10

LOG = logging.getLogger("examples")


@register_example
def async_iterators(args: argparse.Namespace) -> None:
    """
    Run the async IO examples.
    :param args: Command-line arguments.
    """
    LOG.info("Running async iterators examples")
    # example_1(args)
    # example_2(args)
    # example_3(args)
    # example_4(args)
    # example_5(args)
    # example_6(args)
    # example_7(args)
    # example_8(args)
    # example_9(args)
    example_10(args)
