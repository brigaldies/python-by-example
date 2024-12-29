"""
Async iterators example 1: Async Iterators
"""
import argparse
import asyncio
import logging
import time

LOG = logging.getLogger("examples")


class AsyncRangeIterator:
    def __init__(self, start, end, sleep_time_sec: int):
        self.start = start
        self.end = end
        self.sleep_time_sec = sleep_time_sec

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.start < self.end:
            await asyncio.sleep(self.sleep_time_sec)
            value = self.start
            self.start += 1
            return value
        else:
            raise StopAsyncIteration


async def run_example(sleep_time_sec: int = 1) -> None:
    """
    Async iterate using an async iterator.
    :param sleep_time_sec: Sleep time in second between iterations.
    """
    async for i in AsyncRangeIterator(0, 5, sleep_time_sec):
        LOG.info(f"[Example 1] Async range: {i}")


def example_1(args: argparse.Namespace) -> None:
    """
    Run example 1.
    """
    LOG.info("Running async iterators example 1 (args=%s)", vars(args))
    start = time.perf_counter()
    asyncio.run(run_example())
    elapsed = time.perf_counter() - start
    LOG.info("%s executed in %0.2f seconds.", __file__, elapsed)
