"""
Decorators example 1.

Use case: Log a function's execution time.
"""
import argparse
import logging

from examples.decorators.decorators import timer

LOG = logging.getLogger("examples")


@timer
def waste_some_time(num_times: int) -> None:
    """
    Decorated function.
    :param num_times: Loop count.
    :return: None
    """
    for _ in range(num_times):
        sum([number ** 2 for number in range(10_000)])


def example_1(args: argparse.Namespace):
    """
    Run example 1.
    :param args: Command-line arguments
    :return:
    """
    LOG.info("Running decorator example 1 (args=%s)", vars(args))
    waste_some_time(10)
