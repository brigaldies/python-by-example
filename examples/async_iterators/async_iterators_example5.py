"""
Async iterators example 3: Async Generator Iterator with file IO
"""
import argparse
import asyncio
import logging
import time
from pathlib import Path

import aiofiles

LOG = logging.getLogger("examples")


class AsyncFileIterator:
    def __init__(self, path, chunk_size=1024):
        self.path = path
        self.chunk_size = chunk_size
        self.file = None

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.file is None:
            self.file = await aiofiles.open(self.path, mode="rb")
        chunk = await self.file.read(self.chunk_size)
        if not chunk:
            await self.file.close()
            raise StopAsyncIteration
        return chunk


async def run_example() -> None:
    """
    Use an async generator iterator to read a large file.
    """
    directory = Path.cwd()
    LOG.info(f"Current directory: {directory}")
    file_to_process = directory / "examples/async_iterators/data/TEST.md"  # Source: https://github.com/mxstbr/markdown-test-file/blob/master/TEST.md
    async for chunk in AsyncFileIterator(file_to_process):
        # Process the file chunk here...
        await asyncio.sleep(0.2)
        LOG.info(f"[Example 5] Processed {len(chunk)} bytes")


def example_5(args: argparse.Namespace) -> None:
    """
    Run example 5.
    """
    LOG.info("Running async iterators example 5 (args=%s)", vars(args))
    start = time.perf_counter()
    asyncio.run(run_example())
    elapsed = time.perf_counter() - start
    LOG.info("%s executed in %0.2f seconds.", __file__, elapsed)
