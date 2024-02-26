"""
Decorator example 2.

Use case: Show a function's arguments and return value.
"""
import argparse
import logging

from examples.decorators.decorators import debug


@debug
def make_greeting(name, age=None):
    """
    Decorated function.
    :param name: Name
    :param age: Age
    :return: Greeting
    """
    if age is None:
        return f"Howdy {name}!"

    return f"Whoa {name}! {age} already, you're growing up!"


def example_2(args: argparse.Namespace):
    """
    Run example 2.
    :param args: Command-line arguments
    :return:
    """
    logging.info("Running decorator example 2 (args=%s)", vars(args))
    make_greeting("Benjamin")
    make_greeting("Juan", age=114)
