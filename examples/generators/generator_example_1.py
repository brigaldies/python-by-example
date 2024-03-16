"""
Generator example 1.
"""
import argparse
import logging
from itertools import cycle

LOG = logging.getLogger("examples")


def endless():
    """Yields 9, 8, 7, 6, 9, 8, 7, 6, ... forever"""
    yield from cycle((9, 8, 7, 6))


def example_1(args: argparse.Namespace):
    """
    Run the example.
    """
    LOG.info("Running generator example 1 (args=%s)", vars(args))
    e = endless()
    total = 0
    for i in e:
        if total < 30:
            print(i, end=" ")
            total += i
        else:
            print()
            # Pause execution. We can resume later.
            break

    # Resume
    print(next(e))
    print(next(e))
    print(next(e))
