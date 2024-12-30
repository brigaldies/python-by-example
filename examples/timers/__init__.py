"""
Timers examples.

Examples are from https://realpython.com/python-async-iterators/
"""
import argparse
import logging
from examples.registry.registry import register_example
from examples.timers.timers_example1 import timers_example1


LOG = logging.getLogger("examples")


@register_example
def timers(args: argparse.Namespace) -> None:
    """
    Run timers examples.
    :param args: Command-line arguments.
    """
    LOG.info("Running async iterators examples")
    timers_example1(args)