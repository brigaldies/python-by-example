"""
Progress bar examples
"""

import argparse
import time
import logging
import progressbar
from tqdm import tqdm

LOG = logging.getLogger("examples")


def progress_bar_example_1(args: argparse.Namespace) -> None:
    """
    Progress bar example using tqdm
    :param args: Command-line arguments
    :return: None
    """
    LOG.info("Running progress bar with \"tqdm\" with args %s", args)
    data = range(10)
    for _ in tqdm(data):
        time.sleep(0.5)


def progress_bar_example_2(args: argparse.Namespace) -> None:
    """
    Progress bar example using progressbar2
    :param args: Command-line arguments
    :return: None
    """
    LOG.info("Running progress bar with \"progressbar2\" with args %s", args)
    m = 100
    with progressbar.ProgressBar(max_value=m) as bar:
        for i in range(m):
            bar.update(i)
            time.sleep(0.2)
