"""
Closure examples in https://realpython.com/python-closure/
"""

import argparse
import logging
from examples.registry.registry import register_example
from examples.closure.closure_examples import closure_example_1, closure_example_2, closure_example_3, \
    closure_example_4, closure_example_5, closure_example_6

LOG = logging.getLogger("examples")


@register_example
def closure(args: argparse.Namespace) -> None:
    """
    Closure examples.
    :param args: Command-line args
    :return:
    """
    LOG.info("Running closure usage examples")
    closure_example_1(args)
    closure_example_2(args)
    closure_example_3(args)
    closure_example_4(args)
    closure_example_5(args)
    closure_example_6(args)
