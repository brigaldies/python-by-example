"""
Async io example 1
"""
import argparse
import asyncio
import logging
import time


async def count(counter_name: str, sleep_time_sec: int) -> None:
    """
    Coroutine counts.
    :param counter_name: Counter's name.
    :param sleep_time_sec: Sleep time in second.
    """
    # Do some work
    logging.info("%s: One", counter_name)

    # Do some I/O that takes time (e.g., access an API, DB, etc.)
    await asyncio.sleep(sleep_time_sec)

    # Resume doing work
    logging.info("%s: Two", counter_name)


async def run_example(sleep_time_sec: int = 1) -> None:
    """
    Coroutine runs several counters.
    :param sleep_time_sec: Sleep time in second.
    """
    await asyncio.gather(
        count("counter_1", sleep_time_sec),
        count("counter_2", sleep_time_sec),
        count("counter_3", sleep_time_sec),
    )


def example_1(args: argparse.Namespace) -> None:
    """
    Run example 1.
    """
    logging.info("Running async io example 1 (args=%s)", vars(args))
    start = time.perf_counter()
    asyncio.run(run_example())
    elapsed = time.perf_counter() - start
    logging.info("%s executed in %0.2f seconds.", __file__, elapsed)
