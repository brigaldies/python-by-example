"""
Async iterators example 3: Async Generator Iterator
"""
import argparse
import asyncio
import os

import aiofiles
import logging
import time
from pathlib import Path
from zipstream import AioZipStream

LOG = logging.getLogger("examples")


async def stream_generator(files):
    """
    Async generator iterator to iterate over zipped data chunks.
    :param files: List of files to zip
    :return:
    """
    async_zipstream = AioZipStream(files)
    async for chunk in async_zipstream.stream():
        yield chunk


async def run_example() -> None:
    """
    Use an async generator iterator to zip the content of the examples/async_iterators/data directory.
    """
    directory = Path.cwd()
    LOG.info(f"Current directory: {directory}")
    data_directory = directory / "examples/async_iterators/data"

    zip_name = data_directory / "output.zip"
    if os.path.exists(zip_name):
        os.remove(zip_name)
        print(f"[Example 3] File '{zip_name}' deleted successfully.")

    files = [
        {"file": path}
        for path in data_directory.iterdir()
        if path.is_file() and path.suffix == ".txt"
    ]
    for file in files:
        LOG.info(f"[Example 3] File: {file["file"]}")

    async with aiofiles.open(zip_name, mode="wb") as archive:
        i = 0
        async for chunk in stream_generator(files):
            i += 1
            LOG.info(f"[Example 3] Writing chunk {i}: {len(chunk)} bytes")
            await archive.write(chunk)


def example_3(args: argparse.Namespace) -> None:
    """
    Run example 3.
    """
    LOG.info("Running async iterators example 3 (args=%s)", vars(args))
    start = time.perf_counter()
    asyncio.run(run_example())
    elapsed = time.perf_counter() - start
    LOG.info("%s executed in %0.2f seconds.", __file__, elapsed)
