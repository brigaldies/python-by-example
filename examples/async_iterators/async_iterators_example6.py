"""
Async iterators example 6: Async loop with built-in anext() for more granular control by the consumer
"""

import argparse
import asyncio
import csv
import logging
import time
from pathlib import Path

import aiocsv
import aiofiles

LOG = logging.getLogger("examples")


class AsyncCSVIterator:
    def __init__(self, path):
        self.path = path
        self.reader = None

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.reader is None:
            LOG.info(f"Example 6] Opening file {self.path}")
            async with aiofiles.open(self.path, mode="r") as file:
                lines = await file.readlines()
                LOG.info(f"Example 6] Read {len(lines)} lines")
                self.reader = csv.reader(lines)
        try:
            return next(self.reader)
        except StopIteration:
            raise StopAsyncIteration


async def run_example() -> None:
    """
    Use an async generator iterator to process a CSV file.
    """
    directory = Path.cwd()
    LOG.info(f"Current directory: {directory}")
    file_to_process = directory / "examples/async_iterators/data/username.csv"
    csv_iter = AsyncCSVIterator(file_to_process)
    # Skip the headers
    await anext(csv_iter)
    # Process the rest of the rows
    async for row in csv_iter:
        LOG.info(f"[Example 6] CSV row: {row}")


def example_6(args: argparse.Namespace) -> None:
    """
    Run example 6.
    """
    LOG.info("Running async iterators example 6 (args=%s)", vars(args))
    start = time.perf_counter()
    asyncio.run(run_example())
    elapsed = time.perf_counter() - start
    LOG.info("%s executed in %0.2f seconds.", __file__, elapsed)
