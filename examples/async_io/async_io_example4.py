"""
Async io example 4 using a queue with producers and consumers.
"""
import argparse
import asyncio
import itertools as it
import logging
import os
import random
import threading
import time


async def make_item(size: int = 5) -> str:
    """
    Produces an item to be queued.
    :param size: Item's size.
    :return: Item's queue payload.
    """
    return os.urandom(size).hex()


async def random_sleep(caller=None) -> None:
    """
    Random sleep.
    :param caller: Caller's name.
    :return: None.
    """
    i = random.randint(0, 10)
    if caller:
        print(f"[{threading.current_thread().name}] {caller} sleeping for {i} seconds.")
    await asyncio.sleep(i)


async def produce(name: int, q: asyncio.Queue) -> None:
    """
    Producer.
    :param name: Producer's name.
    :param q: Queue.
    :return: None.
    """
    n = random.randint(0, 10)
    for _ in it.repeat(None, n):  # Synchronous loop for each single producer
        await random_sleep(caller=f"Producer {name}")
        i = await make_item()
        t = time.perf_counter()
        await q.put((i, t))
        print(f"[{threading.current_thread().name}] Producer {name} added <{i}> to queue.")


async def consume(name: int, q: asyncio.Queue) -> None:
    """
    Consumer.
    :param name: Consumer's name.
    :param q: Queue
    :return: None.
    """
    while True:
        await random_sleep(caller=f"Consumer {name}")
        i, t = await q.get()
        now = time.perf_counter()
        print(f"[{threading.current_thread().name}] Consumer {name} got element <{i}>"
              f" in {now - t:0.5f} seconds.")
        q.task_done()


async def run_example(nprod: int, ncon: int) -> None:
    """
    Run the example.
    :param nprod: Number of producers.
    :param ncon: Number of consumers.
    :return: None
    """
    # Create the queue
    q = asyncio.Queue()

    # Create the producers
    logging.debug("Create %d producers", nprod)
    producers = [asyncio.create_task(produce(n, q)) for n in range(nprod)]

    # Create the consumers
    logging.debug("Create %d consumers", ncon)
    consumers = [asyncio.create_task(consume(n, q)) for n in range(ncon)]

    # Run and gather the producers
    logging.debug("Waiting for producers...")
    await asyncio.gather(*producers)

    # Wait for all messages to be read.
    # Implicitly awaits consumers, too.
    logging.debug("Waiting for all messages to be processed...")
    await q.join()

    # Cancel all consumers
    logging.debug("Cancelling all consumers...")
    for c in consumers:
        c.cancel()

    logging.info("Done.")


def example_4(args: argparse.Namespace):
    """
    Run example 4.
    :param args: Parsed command-line args.
    :return: None.
    """
    random.seed(444)
    start = time.perf_counter()
    logging.info("Running async io example 4: nprod=%d, ncon=%d", args.nprod, args.ncon)
    asyncio.run(run_example(nprod=args.nprod, ncon=args.ncon))
    elapsed = time.perf_counter() - start
    print(f"[{threading.current_thread().name}] Program completed in {elapsed:0.5f} seconds.")
