"""
Decorator example 4

Use case: Slow down a function.
"""
import argparse
import logging

from examples.decorators.decorators import slow_down


@slow_down
def countdown(from_number: int) -> None:
    """
    Decorated function.
    :param from_number: Count down starting number.
    :return: None.
    """
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)


def example_4(args: argparse.Namespace) -> None:
    """
    Run example 4.
    :param args: Command-line arguments.
    :return: None
    """
    logging.info("Running decorator example 4 (args=%s)", vars(args))
    countdown(5)
