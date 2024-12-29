"""
Async iterators example 7: Async loop with built-in anext() for more granular control by the consumer.
"""

import argparse
import asyncio
import logging
import time

LOG = logging.getLogger("examples")


async def async_inf_integers(start=0):
    """
    Example of an async generator which produces an infinite stream of integers.
    :param start: Starting number.
    :return:
    """
    current = start
    while True:
        yield current
        current += 1
        await asyncio.sleep(0.5)


async def run_example() -> None:
    """
    Use an async (infinite) generator iterator to read a series of numbers.
    """
    start = 0
    stop = 10
    generator = async_inf_integers(start=start)
    while True:
        number = await anext(generator)
        # Process the number here...
        LOG.info(f"[Example 7] Collected number {number}")
        if number == stop - 1:
            break


def example_7(args: argparse.Namespace) -> None:
    """
    Run example 7.
    """
    LOG.info("Running async iterators example 7 (args=%s)", vars(args))
    start = time.perf_counter()
    asyncio.run(run_example())
    elapsed = time.perf_counter() - start
    LOG.info("%s executed in %0.2f seconds.", __file__, elapsed)
