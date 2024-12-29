"""
Async iterators example 8: Async iteration with list comprehensions.
"""

import argparse
import asyncio
import logging
import time

LOG = logging.getLogger("examples")


async def async_range(start, end):
    for i in range(start, end):
        await asyncio.sleep(0.2)
        yield i


async def run_example() -> None:
    number_list = [i async for i in async_range(0, 5)]
    number_dict = {i: str(i) async for i in async_range(0, 5)}
    LOG.info(f"[Example 8] {number_list}")
    LOG.info(f"[Examople 8] {number_dict}")


def example_8(args: argparse.Namespace) -> None:
    """
    Run example 8.
    """
    LOG.info("Running async iterators example 8 (args=%s)", vars(args))
    start = time.perf_counter()
    asyncio.run(run_example())
    elapsed = time.perf_counter() - start
    LOG.info("%s executed in %0.2f seconds.", __file__, elapsed)
