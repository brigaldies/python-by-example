"""
Async io example 2
"""
import argparse
import asyncio
import logging
import random
import threading

# ANSI colors
c = (
    "\033[0m",  # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
)


async def make_random(idx: int, threshold: int = 6) -> int:
    """
    Coroutine generates a random number obove a threshold.
    :param idx: Generator ID
    :param threshold: Threshold.
    :return: Random number.
    """
    print(c[idx + 1] + f"Initiated make_random({idx}).")
    i = random.randint(0, 10)
    while i <= threshold:
        print(c[idx + 1] + f"[{threading.current_thread().name}] make_random({idx}) == {i} too low; retrying.")
        await asyncio.sleep(idx + 1)
        i = random.randint(0, 10)
    print(c[idx + 1] + f"[{threading.current_thread().name}] ---> Finished: make_random({idx}) == {i}" + c[0])
    return i


async def run_example():
    """
    Coroutine generates random numbers.
    """
    res = await asyncio.gather(*(make_random(i, 10 - i - 1) for i in range(3)))
    return res


def example_2(args: argparse.Namespace) -> None:
    """
    Runs example 2.
    """
    logging.info("Running async io example 2 (args=%s)", vars(args))
    random.seed(444)
    r1, r2, r3 = asyncio.run(run_example())
    print()
    print(f"r1: {r1}, r2: {r2}, r3: {r3}")
