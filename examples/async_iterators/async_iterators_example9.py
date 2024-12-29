"""
Async iterators example 8: Async iteration in concurrent code.
"""

import argparse
import asyncio
import logging
import time
from random import randint

LOG = logging.getLogger("examples")


class AsyncCounterIterator:
    def __init__(self, name="", end=5):
        self.counter = 0
        self.name = name
        self.end = end

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.counter >= self.end:
            raise StopAsyncIteration
        self.counter += 1
        await asyncio.sleep(randint(1, 3) / 10)
        return self.counter


async def task(iterator: AsyncCounterIterator):
    async for item in iterator:
        print(item, f"from iterator {iterator.name}")


async def run_example() -> None:
    # This code runs concurrently:
    await asyncio.gather(
        task(AsyncCounterIterator("#1")),
        task(AsyncCounterIterator("#2")),
    )


def example_9(args: argparse.Namespace) -> None:
    """
    Run example 9
    """
    LOG.info("Running async iterators example 9 (args=%s)", vars(args))
    start = time.perf_counter()
    asyncio.run(run_example())
    elapsed = time.perf_counter() - start
    LOG.info("%s executed in %0.2f seconds.", __file__, elapsed)
