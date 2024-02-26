"""
Decorator example 3.

Decorate any existing function.
"""
import argparse
import logging
import math
from examples.decorators.decorators import debug


def approximate_e(terms=18):
    """
    approximation of the constant 'e'
    :param terms: Number of terms in the approximation
    :return: Approximated e
    """
    return sum(1 / math.factorial(n) for n in range(terms))


def example_3(args: argparse.Namespace) -> None:
    """
    Run example 3.
    :param args: Command-line arguments.
    :return: None
    """
    logging.info("Running decorator example 3 (args=%s)", vars(args))
    math.factorial = debug(math.factorial)
    logging.info("Approximated 'e' with %d terms: %f", 5, approximate_e(terms=5))
