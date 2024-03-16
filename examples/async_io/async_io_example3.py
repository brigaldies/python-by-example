"""
Async io example 3.

Two processing parts are chained:
- Part 1 does some work.
- Part 2 does some work.
- Orchestrator: Chains parts 1 and 2.
"""
import argparse
import asyncio
import logging
import random
import threading
import time

LOG = logging.getLogger("examples")


async def part1(n: int) -> str:
    """
    Coroutine for part 1.
    :param n: Overall process ID
    :return: Part 1's result.
    """
    i = random.randint(0, 10)
    print(f"[{threading.current_thread().name}] part1({n}) sleeping for {i} seconds.")
    await asyncio.sleep(i)
    result = f"result{n}-1"
    print(f"[{threading.current_thread().name}] Returning part1({n}) == {result}.")
    return result


async def part2(n: int, arg: str) -> str:
    """
    Coroutine for part 2.
    :param n: Overall process ID
    :param arg:
    :return: Part 2's result.
    """
    i = random.randint(0, 10)
    print(f"[{threading.current_thread().name}] part2{n, arg} sleeping for {i} seconds.")
    await asyncio.sleep(i)
    result = f"result{n}-2 derived from {arg}"
    print(f"[{threading.current_thread().name}] Returning part2{n, arg} == {result}.")
    return result


async def chain(n: int) -> None:
    """
    Orchestrator: Chains parts 1 and 2.
    :param n: Overall process ID
    :return: None.
    """
    start = time.perf_counter()
    p1 = await part1(n)
    p2 = await part2(n, p1)
    end = time.perf_counter() - start
    print(f"[{threading.current_thread().name}] -->Chained result{n} => {p2} (took {end:0.2f} seconds).")


async def run_example(*args):
    """
    Runs the entire process.
    :param args: Number of concurrent processes.
    :return:
    """
    await asyncio.gather(*(chain(n) for n in args))


def example_3(args: argparse.Namespace):
    """
    Runs example 3.
    """
    LOG.info("Running async io example 3")
    random.seed(444)
    start = time.perf_counter()
    args = [1, 2, 3]
    asyncio.run(run_example(*args))
    end = time.perf_counter() - start
    print(f"[{threading.current_thread().name}] Program finished in {end:0.2f} seconds.")
