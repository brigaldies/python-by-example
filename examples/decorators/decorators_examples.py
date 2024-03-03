"""
Decorators examples.

Source: https://realpython.com/primer-on-python-decorators
"""
import argparse
import logging

from examples.registry.registry import register_example
from examples.decorators.decorators_example_1 import example_1
from examples.decorators.decorators_example_2 import example_2
from examples.decorators.decorators_example_3 import example_3
from examples.decorators.decorators_example_4 import example_4
from examples.decorators.decorators_example_5 import example_5


@register_example
def decorators(args: argparse.Namespace) -> None:
    """
    Run the decorators examples.
    :param args: Command-line arguments.
    """
    logging.info("Running decorators examples")
    example_1(args)
    example_2(args)
    example_3(args)
    example_4(args)
    example_5(args)
