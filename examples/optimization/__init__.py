"""
ML Model Hyper-parameters Optimization examples.

Source: https://github.com/hyperopt/hyperopt/wiki/FMin
"""
import argparse
import logging
from examples.registry.registry import register_example
from examples.optimization.optimization_hyperopt import hyperopt_example0, hyperopt_example1, hyperopt_example2, \
    hyperopt_example3

LOG = logging.getLogger("examples")


@register_example
def hyperopt(args: argparse.Namespace) -> None:
    """
    Hyperopt examples.
    :param args: Command-line arguments.
    """
    LOG.info("Running Hyperopt examples")
    hyperopt_example0(args)
    hyperopt_example1(args)
    hyperopt_example2(args)
    hyperopt_example3(args)
