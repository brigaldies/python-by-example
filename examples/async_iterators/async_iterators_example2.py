"""
Async iterators example 2: Async Iterables
"""
import argparse
import asyncio
import logging
import time

LOG = logging.getLogger("examples")


class AsyncRangeIterable:
    def __init__(self, start, end, sleep_time_sec: int):
        self.data = range(start, end)
        self.sleep_time_sec = sleep_time_sec

    async def __aiter__(self):
        for i in self.data:
            await asyncio.sleep(self.sleep_time_sec)
            yield i


async def run_example(sleep_time_sec: int = 1) -> None:
    """
    Async iterate using an async iterable.
    :param sleep_time_sec: Sleep time in second.
    """
    async for i in AsyncRangeIterable(0, 5, sleep_time_sec):
        LOG.info(f"[Example 2] Async range: {i}")


def example_2(args: argparse.Namespace) -> None:
    """
    Run example 2.
    """
    LOG.info("Running async iterators example 2 (args=%s)", vars(args))
    start = time.perf_counter()
    asyncio.run(run_example())
    elapsed = time.perf_counter() - start
    LOG.info("%s executed in %0.2f seconds.", __file__, elapsed)
