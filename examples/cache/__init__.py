"""
Redis cache usage examples
"""

import argparse
import logging
from examples.registry.registry import register_example
from examples.cache.cache_example1 import cache_example1

LOG = logging.getLogger("examples")


@register_example
def cache(args: argparse.Namespace) -> None:
    """
    Redis cache examples.
    :param args: Command-line args
    :return:
    """
    LOG.info("Running Redis usage examples")
    cache_example1(args)
