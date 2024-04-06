"""
Progress bar examples
"""

import argparse
import logging
from examples.registry.registry import register_example
from examples.progress_bar.progress_bar_examples import progress_bar_example_1, progress_bar_example_2

LOG = logging.getLogger("examples")


@register_example
def progress_bar(args: argparse.Namespace) -> None:
    """
    Progress bar examples.
    :param args: Command-line args
    :return:
    """
    LOG.info("Running progress bar usage examples")
    progress_bar_example_1(args)
    progress_bar_example_2(args)
